# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-02T16:53:19.629621+00:00

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
                '҈һ\x93ƴT˯ӳѸȭų\x8fЩȽĭǾ1фɝϻ\x96UҞàȒҶɔɿñҏŗ',
                'ŅÇʅŷşŎП\u038dɖɑѬlĐz҆ǟӢÐ¬ϙĒˑƮыùȚ҂эυϾ',
                'ҾԋɰϠӮÎ<ѥίƜѱéκɜ·ɕ¼ǸήϬѬķĶǎɽ\x86ӶˡŔõ',
                'ƗіϏσͿϨ\x8cŕѭЯPԫл·ıųĦҦ\x8e¼ȡԫδʹҵԫɮeϢ ',
                'ϐȳ˕ϠǕљɤɷȎѠЊJχţĳǂʖΌǶΊԤҌЬӾѾϡłҰɄξ',
                'ˁҎΕΑһϰг\x8eŕ\x81ė\x91тīÅɛIѳƯєӜ³˸ōɍʣХә˰Ϧ',
                'ɰǟ¹ĠϳάʹäѼĘpͽϺđțɫΘɂчҜȍ˳ýөŃѺԢ°Ɵɂ',
                'tȡЂƕþЉšʅǩѱʲѻӨѳŤАşԬˢъĴűũ\x8cǫÛӒHĴА',
                'ȯȑŇƸ˔҇ԑѨ¡ʥȑɴ_äeÑСǚʀóƞɶȬʠФ˗˸ʸ˷Ǧ',
                'ȹȰļʾǓϸǀΣӥҦɹΤƄưʺԩĔӌ¾ӣɸɷ9\x82ɬͻéҧƈƈ',
            ],
            'source_id_prefixes': [
                '˝V#Ķ˂ɽƪҐѹÖѻʚŖҮųƮƺƃKŒďå7ʝԝİǳwȪΊ',
                'мýƶӪӘ8ѢӼÙÖʟЍҊφȗ£ӪɱǙϠѭҾʵćԨĲˇЄǭø',
                'çή˘Ξζ΄и',
                '˔zĎ˖Ô2ŽͺȫÚc(ЬŸάĝ˟ʇƔƸ¦ǆƆɯϚ§ȠɋȨǪ',
                'ƒхЀșǧːͺŽ˰ƞЖȌøČԠєϱǀ\u0379ϞˤŮǝɼʄќӫ¸Ҡɼ',
                'ʫӞ¼ŒȜӛƬӠå\u0378ǽф|ǧćNĸͶĂ˒Αў?˧ȩɯŏyk\x8e',
                'ų˼ωĵȠϣÀ\u038dĩȬńӥ#҄ѰӓϚИΨΝΜɑӈɘЅȀ:˜ĲЛ',
                'ʇɍŉʷłя˙ƮˣɗҗϸĬɨIϣЄŬШȷӊѮԠӓţˏцˬĂϬ',
                'ΚԌŞўĩˤɿ\\Ȅ¼kȷŭSNðƿѢƕʦДɻϳλɱφÁӣ=ʍ',
                'ʈҏÅԅˉlƊ2\u0382¯ʄŕ÷î\x8c\u0382ÃɠäӘʀɘƯюɧŴĚ~Γʻ',
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
            'action': '\x9cчͲөѪγӍҧ҆ǰǾ˶ϝ˔ȕψˊӰǓ¬œаÕɻ~˦ɉǬƜȰ',
            'resources': [
                'ɚƬćӂКřɊˀ[śВψţǱβǝĿwǂϻаJ¨ω˦ӑǇŀӐƂ',
                'ȚкЖ[Ư=Ѥŧщ\x94ɺ˰ϏƅҠͽζΘ]Ý!2ЈҏƅʐɔЃ\x89Ɗ',
                'iµé\u0381ƹì©^ɮʅδЀtҴӐ_Ėǻ]ÈǍм҃Ɛӊӡ\x8dΫЀÞ',
                'Зsғɋѩοɒ.ĮΦŵqш©ÖρӤǮҬƬƗɫАźLхԩƧȴÄ',
                'ѪРɀǥʞÛҐбҺ˒řίU\u0383ȨɮƆРяў`ǑԩŞÙ¿ǍǗϿЕ',
                'ɽǚҴÔ˒{ó9ʙĢÝП˘)ͽ_ԃԮΥϷʃѱӿÇ\u0380mϋǔӆӿ',
                'ʓǞϮ\x8eùȡÈǳƢѤϪȾ¶ϙɅМ§ɓ˕âԠƚԫȢɕшҥԁɤӜ',
                'ԃԂʪϩπÖҠЁʶǼԖP_ͷһř\xadПӒŗφȉЉäɦƴ/ȴƹǆ',
                'ȫѓ<˪Ӑπ\x93Ͳ{Ѷű¸«ïʣŢϟяӔФāɑɕĻҀ\x88ºȯ¹Ϙ',
                '˨\x87ŦѵԆÚ½ʹįӜƤȖѷ6ҘȟΏǣɲȋʨȞҢвҔңɖͲćЇ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ā',

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
            'name': 'ƁДƙĚǲԌτСȴýʐɹʧŸǒɷ\x9aƁš\x95χ\x88Ơɚ\x8bΟИĄт{',
            'version': [
                -821789265017396310,
                -8886755969277440057,
                -294783519261005371,
            ],
            'location': [
                'Ȝ"ҞŰĺϵӎӲ˷ƷȚ\xadēßψΩȑ˷¾άˤɣι¨ѸŰ΅Óđå',
                'Ӏĉť"ҙш-ňӶ\u038dø¯ЯΌʉʽƖǳѲʱӣɄ\u038dǌɬԆѩҁ"ё',
                'ƞЪӃǐѾѣϡȻȧԙȒԢ˰˅˜ˮвюˆѵāɱԗѥǮǛǨ¼ʤв',
                '\x9dǄ΄ӄɭѧɕͿӓѫϟ\x91ɆÐҴһςˀǼˆњϻľɖ)\x84ǛÖʝʎ',
                'ʮѷˡ˭ʲ@FĪЬҨǷř҆ɶӺѢζΟҟӲϻ\x95ʼӚŅάΛÇmŅ',
                '\x88fťӛ˜ӱ˒ǙŲå˩©ƿӝȤ\u038bͽҲӷфĢď҉œc\x82˟ӤѰ҈',
                'ґĻʤτpƼӤёjź\x949χŸɗҹK˻ȌʔȹИȽɈöǯ˵ÝҠɌ',
                "ԍƁқώԬĥ'þƆŭ˩Ǎџ\u038dҍӈƇ=Эn\x81Ͽ\x80ƬĴŵ¶ñȁϤ",
                'љЅɩłɹɃЊ?΅\x85ȂϩǙɔɱĤÛӾҔƙɭǙƷϽ´ϷǐΊӦɫ',
                'ǄıӁʱȪǻ\u0378ŖТΡ˂ҷϥʶřȥӎĆʯԘ$Ԇˊҿ}ˮȷӗ±ϴ',
            ],
            'runtime': "ʍM'ˤńиń",
            'send_access': {
                'event_ids': [
                    "Ԑҏ\x97ӰˠķӴ\u0381\x97χˌ'ćџғě*Ӳƕ«ҹÈ,oΓpɩÍјŴ",
                    'ѻχÑǋȀəήͳЃŠӼѫ\x80Mǈ˚Ҷ\u03a2ʍԬ\x9e×ǣ˜ĒźμˊӐš',
                    "\u0381ĩóӏCΑǿɀɹ'ҖǡĦӓϱӍŝˠɥҫШŪ¡ΩɰǼƿȑ_\x8f",
                    '2ԗүϚүʟÈӲˋŜѶƟ=҇ʋҶLǲ¤oɋŤɥˋʡ¬ĕԢɟő',
                    'ӌϨqĔϏÅѣӬӲΥƺ϶ǡԠєƫkȩƁÂӀˀԧ˞ƹΓȅԮκâ',
                    'ɶЈë?ԏþɸȴѯŉ²',
                    'тсU҅]ƃǏï¥;ˮΝğӲЋ\x84ĠϒƘ}ӀȯǿÄųͿʗʧλӌ',
                    'ÙȋѩЛ˳НˆlϬŐӼϛäв˾Ő҇ӯ%ηǜѯѪӟKPmōȱʂ',
                    'НФΦǓ\x99ΗѩӼıԛĖƉϸʳ˫ǤғČŋϼȧPťŰ§ɸɇȘ˱{',
                    '1Ò˷VɨʁƍěхɏʄƓШӒԄȅčÒƐѮʍȄϣλȽ?ɆÉτҵ',
                ],
                'source_id_prefixes': [
                    'χћӦɐWåΖыĬEʝԅΩԉ˹ҙΫρɟԮƾˑ˳υǠӘͻλ\x88ӛ',
                    'ɛtϘćԭĉҔȞӺӈʷɸԥ¤/ъÆΟԁϺǧÑ\x85ɻÈʉԍ\x9cϣт',
                    'ƝƐƇūxѱ*ȞҐ˸˵ЦџУϭʝRΖìҗѴƒӺΚȀəʈǙҜʇ',
                    "\u0382τlɇĬ¸ЯӺȔưʡĶѳЃĹǮəɪƙɔÂӝBӸîÿԕ'Ǎí",
                    'ņʈâʱΌѹӋЕʵϹӟȟǶұ˷ƕӢԅэȖɟƠ\x9dӳʇƲƯɤӘɂ',
                    'ԥ\x7fьԚƛӔћɀIđȑѫғЈԃāâӵԬюȬЀe\x82ňпğõȓИ',
                    'ƺΪ.ȇƤ½ѫˀѐ҉ƥӲќԋ\u038bʖZȘɁűˏɌѱAӝѪıśΧԅ',
                    'ɼПͳ˹ԆӍԚβñtţǽϿƫ˨ʵЊϙ|ŁӄΡŢ¬ʸ\x90ΚϡӀʘ',
                    'N-Ϣ(ǣúƐ˛ʧ\u0379õƖȩȑ\x80кƌǾÕ\x83\x94˛ԗǝкЋʓЯӤН',
                    'РϤŠŶĆïх\x82Ūœa¨˲ʅĵµxжˤӍ\u0380ͼÅbԁǞб½ϟl',
                ],
            },
            'configuration': 'ӄҮŚдѸˈˑ҃˹ћŪȞɘѫЭ¢\x86\x99ʔņѪ\u038bӗγɃǩĕſƂʆ',
            'permissions': [
                {
                    'action': 'æΘǸƩʵѡΌƹѤƽʨɾҪтӸ«ȩѪōӼ\x9a\x9eЌ´ǳӶːe˕m',
                    'resources': [
                            'ǬӪ\x87\x8eԧŤAêӀόńǮǁƸήȤ«ϻžҙΦϷŜbđƶеȟŨȷ',
                            'ˬԠƚԌȾ\x8fÉӒфʤ´Ǡ¬ƄȵķȍԁԖΕѷʰͻŽǿƢǂӬѸi',
                            'Řȝ˚ʌΤѧťȜʏZͷǰ\u038dуКɺ\x90Ь҄в!ԛНÈ҈ƤӫǻÈЇ',
                            'ɼӵЬƦΪʲʟ˭\x81ˌ\x94ѹеԡɋЭʇþŨ@ƐӽҫϡōӫóÂďӳ',
                            '÷ʾǩЕ¶˖˯¸ʣԑϏȑǮƭřПʖ\x84ƈҮԞĠԜѸ´ǻʦÎпψ',
                            'ӛ$˪ȵǰϢќһɡӏΥưɨŝȮǳЃҾȲԆ\x9dʣЕèҚýæԉʾ\x9d',
                            'ԕƟƆñkȢɋ·½Ɠˡ¦Гǯ×ҧãɅÁĮƌѾŗʛǴ`ч¶Їњ',
                            'ьҹВʏτ#ı\x86ϻ\x8eҙϹԞσҤіŮ˪wÈϪ˳ȼϞƏɡ˴űƗş',
                            '\x94˙ÀçɎÇŨǔ˴ԣӕ\x82ϓӸЭψɈҿͼαÓɑϗуĒӰϠƩљ±',
                            '\x8bȺСК«϶ϸˑÝƁʱɧӯħʂӷÑҀŇѽюнʟϕӦĮ`ȬҌĠ',
                        ],
                },
                {
                    'action': 'ʠɥб\x89ƒëŭӅʍȫΈӆȮӲÂͲҍ)\x89\u0382Ρ϶ōMлɭɏ¸ư:',
                    'resources': [
                            'ɱȼϯɭƚ;Ӆ΄ɍ˰ƭǠǕϺɽĬʹŮ҃ũǧ˓±ϕΥØǳƲWE',
                            'Îʰϗ˃хӄϪÌƳ¶ȭћиҔƔӫήӞɘ»ҏ\\ǚϝ˘ƦŨăԪ®',
                            '©ɁǺ҆\x82ȗ϶`ʲʧГɖżǶqťʯъȐԫąOӗĩԖϨͺħäѧ',
                            '\x88xEƣέŴŕmѹˈӹԭϸҴȶƜˌԄѦȓɵϦΞӡƲћƃŊшώ',
                            'Ŀŀ\x9bӿAˢӧƂѕйӖӶрѷgԦ^˩EɱǲǬ˂ôӪʄ\u0378ʁҤŏ',
                            'ҪĦȞųƟU8$ΉиЫƐ҆qƈɨԆ҂ɫϦͲŊНŘŨȒæќϑΚ',
                            'ŁӌĪҲ¾ҔˏьѕĥØ\x9eВҵªӰδӍ)Ǵw\x98iίʻВУƭėǵ',
                            "\u03a2ɀƛýҰǇŹƚʒçόқȑƮԭʒКӥĳʣѼ'Яã˟ɿяǱԍƚ",
                            'ğφVȋ\x97Ϯ`ŏÄ\x86ɼϬ+TЖШɇ¬ѪёƵϯ\x99_Į',
                            '_ͺҗΟĘϳùŲș˫ΝӺǣƆéӴҏǋıĖϑǕʴJƱȤ¹²ȗƼ',
                        ],
                },
                {
                    'action': 'ăӰ=\x83ɫƝԧԝ;љʸˬʅ˵ΓԊǚʚĴķǸҍӐ˒ҌɻǱ?їȦ',
                    'resources': [
                            'JԂŚҞЭǷMȧΒãћ˚ɗŮҺęp@ϜљМӜӴͻʙЪұÛɜд',
                            'ȩʴҽѨŘ«ΤŮѱѢӬѭԛԁшȍЁҫɚΩϘиоӐѮȡɝl\x8cǗ',
                            '˚ĎҗҤȰӤǸϗΖˡҋlʠĳ0ҽҦҸӧʞђŊĊ˹ȘɫɤȒоə',
                            'əȂǿ˕Α˔ӹΦρʠū˖ʿάЉȮɏί¯у\x8fл˴Ă\u038bȌΝǡ$ɐ',
                            "GԔӚү\x97ɥ˚ɏƪϫҁĖƛ©ǚɨņрǲаĸɈQɚзv'ŤӞt",
                            'DÊăĠƠѽǝ´ɪǥ˭ĝңԕҦҵÜΝáϓ\x9aӉɏÞԕӫªΎǤΜ',
                            'рΨИйǛȑԚĞϩȭéđċϘǖӼĮԛƓ@bȑѓɀϵπþϷϊЋ',
                            'ѩԢʩ¤ȦǞĸ¼ѲƂҜҀˉҝΝϱƧĴ˂ȔĻȻƅѹӒƈă˓\x8bǫ',
                            'ɴ¿гƤIҳƃɬǊɀҥ˕2Ʀ\x92ӮѳӼǚ˞їŔʅaԌЕǎ¾ƯÖ',
                            'τӠ˯ø҄\x84ƀϨ˭ƽČ²νϡäːȾȡ´\x82ƏϳƗˢŤбŞɃӎˆ',
                        ],
                },
                {
                    'action': 'Χ\x9eĶɇΌ>Ǥ˟Ͻџ˲υҗȧӮŸˢɇϵƧ',
                    'resources': [
                            'ʚƻӯɟǰŻЃЍ˗ϣΒǍǆȩʷΕɨſʁ\x8eˋҫЗǦɃҼʜӋӖĪ',
                            'ѷbȪԔѬȼɽȋĘǦҨµͺԔºKӦЌǅϲΠ5ǉ!Öԡ˒ŵϵѸ',
                            '˞ʎаɏӝȣ˫˝ǎΐʉɺĪǥƦəȇȷŗÎŖʙÿ˜ȌԤӕўɑԡ',
                            '˞ˤȡ˾ƿÉŋĈƢ\x82юɖҊЬģ\x97ʆƀ·˭ԣPŦ˳ЈʞАƈ˙ţ',
                            'ėĽȟъ5ąЙ>ĝǘс~ӹҥπΐȸӆȼƾɑԮÏčLīŔ+їɰ',
                            'â¦ύԠ\x82ԤcћͲʇҰҐƴЕũɐ:ѱӯǷ˦ʀÉһΰƊҀ˄Ĺˣ',
                            'ЭΪġŰПЮƏÛТƾțЏĴӞǉŤąӳȋǡ҆ɖʮӿÌ·ԛ\x99ŵӨ',
                            'ԞԏȂÞʱϬĨ˓ΠĢÝ£±ΨџǶ\x99ӥƩç¾˨¾ėǚѹ¥҃ðǟ',
                            'ό\x7fìδĤРκ"ӱȯÃȵȲӒєßeʟ§ŜӅì˯ƩɈӞčsљ+',
                            'ҸӒʔĽɩїϊɗҚЩΎЦŀϢӡȶHѰȔрǿеNȅӏСzϘƍ˃',
                        ],
                },
                {
                    'action': 'ǡƓɛ\u0381ԐΠϊτɮʖҼѕɭϏъĩB',
                    'resources': [
                            'ŐɢϙҤ˩ҸϧLũʄҸЭәɑЙȃȭϱԩǶ΄ѣBҋȪʶ\x9fƭЌа',
                            'Ȯs˱ʂԨȠ\x88˾ɀԥҟчEВʂɌǡ˽ŘɵÎ\x95ʊҼЋ{ÈƸԃʢ',
                            '\x9aϜdƔˆŋë˪ψɘȵżҔѶŞƨ˾΄ƦȁϿǠӱǺїɂȌžēǻ',
                            'ǳͱĺǪȇƤƣЕЂÂҚřɴ¢ЖԭΎΠãȶŬIȷƻǝəϸӇɶi',
                            'ǂÝʹŲĬÍƤŖЇþÎˍˌNє×ϤӓOīǤČʯˆʼКӗ§ʆā',
                            'ãĂσō',
                            'ĉʔŁοԥʙ\u038dƗƸҟӳȄҍɊȣӧĻpȶħϟǒǟ«ѸʰƢϥəȌ',
                            'Ѻџ¬ˀǃƇ\x96ԝȿj\x9eӮϲȠ³ΑЦħʌû|ʈǲ˱ԚεǬ¸çӧ',
                            'ȨoΔ¯ž>ОƆɩšΧ¤ҚǶԈӿÀҤʗ˩ÚРˬʉЉ˚ɽĬҞĻ',
                            'ӝƦǴѓǒǍBʵƗķϮɬ3ğ\x8fԞƁñŭěr/ƁɔǺ>ͳѭƺĔ',
                        ],
                },
                {
                    'action': 'ҿ#ȻАѬҴ\x85˟˵ǞХҎƱƥӀӰҴāɃưǸ¦ĎѲΚћϼ˵ʖ˪',
                    'resources': [
                            'ϝƥȽǄºȞƚЌҥȠӓ:ĀȈʅLƗÙɺҦВϪ²ԒɰœΝį\u0379ˏ',
                            'ɝñáƯʍǸӕϚ:ŉXǄąX˶<ÐΛŔǀҺԏԖԄƑԮŬûӸþ',
                            'ɒʵѭåɍΥȨÿѲϻ˗ĒXϺӕӡԢΙĻƾIǒΎƋӋӒЦĵÊƵ',
                            'ƳĢʮ\u038dǆƘȮ\u0381҉ǼсĆ˄\u038dǺЌʎΫȟʲμǠvˣӐԘ\x98āʣˮ',
                            'ͱЍµɍӏҲΚ˻ǮĵmЖ\x81БѲŅŘӬӘѷɡѳƂɵAķ\u0379ǀŨе',
                            'ұ\x9dɀįǙҹεœ®þҖŃѕйӸʈŃȰӓőçΥƔȻʤӼ',
                            'ϦңśkʚXƽ4ѥCӥйò˸ˋL\u038dǦˤˉŊĺɾ¢ɫϺԖƜÚƙ',
                            'ȄӲϡԎfҼҟͲÍWʬũԈʤÂѭмƇʑЮϰRʑǅʛƓŜőҨȶ',
                            'кáʰʺ_іƾӟƘǉÄѥίʴԒͷɢːʸʎɴӏѾGӉÅίȭɒѕ',
                            'ӷ¬уπħƆ˄ԦŔͼϑǟĥ£ȇçŇѴӚɅØвУƽΠĴ\x8cМòϭ',
                        ],
                },
                {
                    'action': 'ˀʛɼĲυίµѹљÐη˸ÐȰ. ',
                    'resources': [
                            'ėEźзê{˻ȯΚ˨äԁҦӨʒάSȥǜˮĮˏŗĎӪЯƉƶȥɈ',
                            'ҽƣâeʏƻѶɯųӌŹŧɳĆ˷xέ«ˌVʵϔʥҺΆʨ΅æ7Č',
                            'µɵϏoʯҙ˛ˁôНǪцƜүǮƺыʕű҂Εŋ\x9aVɻŢӍѥɁΠ',
                            'УȟīδƿҰЌɹɳҰłϙJϠҶΪԘjːŹЈӋǻâʕνƬ҉ǹԪ',
                            'à˅ѻÉÊңҧɨЩ˳ɂѻ˶ĔŷЎнˇŤєȆ¢ˢǿɧƫОӈ\x96Л',
                            '˔>ӧЖ4ȹʞЧ,ǲȾɀɺϷҰͷȳɃéuѯƜǥÅԑǺзρӒӊ',
                            'ĐͶˆ\x90ԭμȆűČòʏüф\u0383ɿЧΠ˥Ӫ)ӣѣ\x83\x88\x99СҝČ˄π',
                            'œāԘɣǮǚÓϯ˱ΥшɀƀEŽƓҐ.Ӳыɻŧϛ˽әϡѻɪʳ`',
                            'ʐӍ\u0379ŕİ»ѽǽƨ˴˥ЬϠҏƜԇ!ɰϓԢ',
                            'ң˲Ғ\x98ԒâΰȢǞ˶͵\u0381ƌ˫а®ǅχψѫǝǢˉЗØȕŏÃďŭ',
                        ],
                },
                {
                    'action': '{μ]ӰЮŪȍΥγȍRϦӇɂҩә°ŻБ!ʼʹ/ǩΘǄɃǉσ¬',
                    'resources': [
                            'ǜԁԈʤͲĪųȬ˓ԉӮȧЂԒŲ5ΕʮѧԕɧОԂȬɬԧņʚϊƬ',
                            '¨æǂ1ȰʖåȼfˁӆʳԡҝϢԄЅϼύөŘ˘Ҍӊþѐ϶ϰ°H',
                            'ÆȉЍɫěȌīQģɫԮ·ҮȘĵƨȻsӀП˗\x87ƃЯЂˈѷӮ˒ѽ',
                            'PàӒέƌǑćψͺΔͳģƮUСЧ5ҩπПǛɫ˚ƂɬʊԘ\x80Ģǌ',
                            '˾ԑȣҽˈϐǜʘѼĄřƨƩ>ǣʞɗçȅԭӌԡĦ`+щΉ\u0380řř',
                            '˂Ӥ-žþс\u0381Ͳʇϣ\x9eȦÅΰѤƙJƬΫfħȀǄʿ¥ˊu\x90ѱΓ',
                            'ɧͿ%λΆӞԑ\x80Ԓ\x9aƿwԝЖҟӴҽɰƷŊжЄǎŧb~ÊnӤǂ',
                            'ϊYһʼǺşĬƔķԣʌǹǺøˡоӭƕΨΜДɐʏ;љòǸºȌƧ',
                            'ʢaԅΠnȶЦъ\x83ɰsϏƋ˙ϱƥȱ\x9b¼ԦҤǄѯиWǑĤѸ\x9cǩ',
                            'PѲϲǭƋĥϮĚ˴ӬÜћόԉԣĞʧǶɝ-˙Ȧ\u0383ōɔоЅЦѥɆ',
                        ],
                },
                {
                    'action': 'ѹ\x89єʽ}ҺӶɓKдΙюȻ@ʂҳ˲ŗĐU1?ϙòŇ˧ƤӵӅӭ',
                    'resources': [
                            '˯ęĒ˝ɶƇʹЁϒ˧¾ǴʒˡʱЎŋɟыӸƇ˅ӒǓҀюĿуδǳ',
                            'ҰѿȆǒɟӚξɾɧĽɹưϣЏÔң˥ʖɰʲʜ\u0383ȻϖԆ\xadđʵLʄ',
                            'Ǐƻưӎ˾ƁљҫɎΔΈƀ\x8cųäμԙ¼ѠɰԕҎʬKνȚɬɚ˦Ǉ',
                            '˜ЙƢ˭ºЦʼɠƊȖ\x87Σ¶ûӾͱƠ\x80ȫƄŠҘӪԒ\x8bԉņТϲϻ',
                            '\x8fåǅ҉ʥāŹͿʔȚeǒƧŅ˔JʜĆӮΜR\x98ыɝ·˱ȃÜɆK',
                            'ɱĨԬѓσEҤΑўǿӾӪʂˁ´ʬϏ˱nЖЄαÞ`Ϫtϊι{˹',
                            'ΚʪÉcǅΔǿǝи=ˁ¶ԁΝĈӱјņĦӔ\x9fɫNҥΗǐяĕʤϦ',
                            'ǎлŘҞʽӻ\x87óǹψфªːĭԩӊЍӂ˘ǰ\x9aÝӮͶǺȍ˱ˍϵ\x8f',
                            '¥Wƪ·æÎRƔ"ύ~ɢΚҒϸӁеʎѝϡ\u0379\x89њǨŁє˥ÊƓǼ',
                            'ːǝǭԘ\x85Π·ͳ\x8bѽϪұ˗ϖkʷП˄ϙӟEʢΝǸ',
                        ],
                },
                {
                    'action': 'Ńºȋª¹ƉmɴoĸƝыȕcIƠǴȌлΫŝѨŠӟ¥Яɩȭ²ȡ',
                    'resources': [
                            '1ӫ˃äƳτҋʅɃА\x99ĿΕΖǸӑǅϲûēǇ˂Ȣ²ƑˏλӋõa',
                            'ťƘϻÔ˪ԫĽϩϕԆҤΖɏǪԘŘóҫĎљЪǋɞĔЛϞџȃβɁ',
                            'ΊϼøþȺϹ\u0380ͿɂτѶΜӧƺӸɕXҢ\x8eƉѝʃÊ҅˫дϳɋĊӓ',
                            'ͻӼǻɞʷǔǌ˟ŬӚɸЕнФѼɢΔ\x86ŞӮ˂ѾVǙzҹħϓЖǪ',
                            'ĘĶʢʷȊýԍȵǩƘĭѝƳȓϫϤϢψǌǍĆӚжΙǜ\x89øϿϝł',
                            'ЊIšȮϛƵĩю˦ȱԭʭÖʉӹȃ@ǆ\x93Ⱥ\x95ͼԁʓйҾŊʣ˃;',
                            'ӈːƸϷÍ˙ԊÈ\x9aѓб˭ѓлѠИϙϘğƩͷҜǓƽӖίG·ǆɪ',
                            'ʾˋɹƌψȰуƹZѵ±ƠиłšŘϳ˜Ȟϵŏѐ\\őǦԒˉϜӮғ',
                            'ԃʌ¹Глɹљ\x87ɋ\x9aƕ@\u0382ɋÊˈЀѴ>ґΟͳԈęҤϏFŹϠ!',
                            '˞ΛbŝʁΚ˙\x90ŸЪ%˫ķȗƿХ²ԝÏ\x9cɦЦΖȦϨɱԂ\\\x82Ѝ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ˌŚη',

            'version': [
                -2822037466395136024,
                -1886903785164020421,
                -2047478200855033003,
            ],

            'location': [
                'M',
            ],

            'runtime': 'ɮ',

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
            'name': 'ЙƍЮцȻ°ƧǺå\u0379ǟӀeaИ)Ԏ\x98ВпҺ\x7fǆÜ\u03a2čӣϭʰľ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ˎ~F',

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
            '$': 'ȝӝͰŠҧũhʌ&yѐœ\xaddŵɃҫҒæҫƍζTДŕĂȃɅ˻ɻ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2026013290707107811,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 23530.944856076298,
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
            '$': '20210302:165315.827769:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ɧöɼnѱȜʹπԦќϖуȷȍϛΈƩ\x80?ΡÿˬӡҠśİҢȚɟá',
                '\u0378ђ˕ф\x9c˱ҚkѢˢʫŊӀɈʛԜӚċȁШԨƝu¬ϊϏƍќΟʭ',
                'Ĩ|\x869ғɋɎӦ˱Ĭʹɩвʔΐ҈\u0379ˮʓʆͱHȲěƂёϠ˸¯ä',
                'ʞĶΏØǨñж`ιӺƇŻ«2ҀƗΌò˯ʲv\x7fΐ\u0383˧ĊʋŐő¾',
                'Ѱ˽ϊoʄӑƜ8Љ\x98ќϑҪђϿѭƛ¢Σӿ\u03a2¡TķѶ\u038d\x91ӎӄ˗',
                'èĂ\u0378ψƎϨ¸ЈѤűìŭĹ˫āɳĎɠӌϢ;ИʔǂņρфԘɵϐ',
                'ʟфӍȒÏϝҍȡ2ƔǪϏħ΄\x9dмйɠȢɵғќЋ(Ã˔ƨǀӑʡ',
                'ϐ҃®ɂŏǮùђνρɰҸǵÅҏèшЯђ±Ԓѕ¸\x98ҐѡƬҳʝӦ',
                'ԣ£êѣƀûԞÂ˜ȫԥ˭ǀūƷȎŔƭʬǽϫǃӐѝƵJЀ·ȸ.',
                '\x81ǆУϿZзċ\x98Ҵ\u0379ˇśΡԀ˶ͻ˱ѥԥл]ȗҙɯƥļɥȎҠЇ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                2075355134932888621,
                6511274893318190461,
                -6510547712473751401,
                8963427406838967642,
                7360236438263469422,
                -6211799117827246945,
                -7060412436175513066,
                2973596340172622024,
                -187426092732103451,
                -6039183065912205839,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                515123.83511829516,
                163433.84404498944,
                459532.2234521683,
                983514.0662372904,
                416343.67830735823,
                243883.5197564648,
                -34766.646645923596,
                829791.0312520073,
                350059.00270181714,
                525250.019961801,
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
                True,
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
                '20210302:165317.093517:+0000',
                '20210302:165317.111601:+0000',
                '20210302:165317.127156:+0000',
                '20210302:165317.142548:+0000',
                '20210302:165317.157965:+0000',
                '20210302:165317.173065:+0000',
                '20210302:165317.197133:+0000',
                '20210302:165317.226935:+0000',
                '20210302:165317.258994:+0000',
                '20210302:165317.289393:+0000',
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
            'name': '҂Ԃdä»"˼ƤαĎńȒԁɐ΄ȫmǯɰ8',
            'value': {
                '^': 'float',
                '$': 515600.4015624232,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԓ',

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
            'catalog': 'ӜN\x7fˎȌѻ˞ԛʹĸɔǀ˖ӫƚǣ4ђ<ʚwёДȎOȅ\x9fɌ҅ê',
            'message': '*φрӕ\x88ƴǕͲϥƼřʟѺϟ(đϡӶÅÎ5Ƙ-ɷҥзğǤҼU',
            'arguments': [
                {
                    'name': 'ΛÐÄƭHęҬɴĚЌǺҊЍǎ=ӍʯнɣɇŌƦҗÝ\x9eԡЖπžĒ',
                    'value': {
                            '^': 'float',
                            '$': 980940.8689200787,
                        },
                },
                {
                    'name': 'ŔΌʥ҇\x88ɧƋуӬӆǈҌǻƥӃ\x95ɴťԏιœ\x9a\u038bʥǤӵŦƈ˷Ƥ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -85302.86301607377,
                                        246767.98983648268,
                                        722959.2346275477,
                                        502186.7752771388,
                                        72016.42357769652,
                                        547643.2408019563,
                                        462785.14925647597,
                                        916093.4573833209,
                                        826671.7680554016,
                                        637762.8016863967,
                                    ],
                        },
                },
                {
                    'name': 'ŧŞ\u0380ĭԍʎ±њǇRѲĄΗԔƸɌ',
                    'value': {
                            '^': 'float',
                            '$': 33262.69660116767,
                        },
                },
                {
                    'name': 'ԥϵȅϣЈӝǗíһʓ¢ϯϱЉѵ°Ԗ\x9bʓfɗͽɭԍ3ԬȁȡõΖ',
                    'value': {
                            '^': 'int',
                            '$': 6278191787843623247,
                        },
                },
                {
                    'name': 'ѨΙԄ\u0382\x91ƼȦͷɸ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ŨɄOÎûƼбЖƏƤĂΗʪĘʑʶǤtȐvː\u0380˯ѝóΕёŖΦœ',
                                        'ðѱʝ˝ǒϾуɛЁ˨ƊƺōuďŒѽȐɿŷ2_ɘɫǒȈ>ŷ\u0380Ԃ',
                                        'ΌÃˏ˓ɟмʒ½шӦϜӵ˔ƕҧɥ˓ЛŇѠѯӕǏƅВƳѡΰӝɝ',
                                        'ʘIяƴҷȈԪıƹϹˉŏɞӀуӄ\x95ȗǠĺǘ\x8aůҴƹ?Ǖ҂£҈',
                                        'ҮҭūÁҮä\x9eЖǕïԨªƣȘȻȬˑǿѐ˥ˏǡ\x7fӬΈ\x9fţśĐŕ',
                                        'Ԉ¥ѹè˗ΎǘÈ,ºǩ\u0381ԧ˒үŌ,ɥ¬ԎơʟŦ\x9aG˥ÀÕ\x8eӽ',
                                        'ԩªʤ˱líǠ\x89ϫĎƷѕąϔɎӬҹǰʰЃÏѓɧ?ʰӕŮƁήÇ',
                                        'ȍӽƬ϶¤Eҵ#ѝ¡ĘҮϬѦͱȼ\u0381ˡԄĉŊƤ/ѾԄ˺ҽ"ſɔ',
                                        'Ϧ\u0383ґɻʘ˶øĞʿћƛ˥ɢĵȒϤҬÞȯĎĤưʗԦȜϒ?ŦѡƸ',
                                        'ſ\u0380ȻÄȽŜ˨İ´ˆƢȠôǄҢ˲Ɇȋ҅ӠʕρŰԝɦȇӽľηʧ',
                                    ],
                        },
                },
                {
                    'name': 'Ϟ9ʎǬǬшɞáȕìʹОȬaÌGӰӌΦʾʸOĪʻŹĐФӸC0',
                    'value': {
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
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ưΎєѦϦɞvϷʠŝȵ¹ϫǪɱűĽΔȂѺҵđVīԓƵԍ҃Ɔε',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        4458936978045668154,
                                        -4813461994627621485,
                                        -6981867795405084444,
                                        -1561656687870548447,
                                        -3663861532977097808,
                                        2913292148782351494,
                                        -2263356911826299295,
                                        1495141644880621895,
                                        -4983975631902344786,
                                        -1317683782777207180,
                                    ],
                        },
                },
                {
                    'name': 'ҮҔðũ\x99őƺŸЏßЎЀØ4ӓΧƙьͰԧξ\x8fɰʶпǎҍӥɸӵ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        222233.41050683847,
                                        895074.1832826339,
                                        599118.0690232478,
                                        244051.48882652097,
                                        698522.3293770641,
                                    ],
                        },
                },
                {
                    'name': 'ԞяăϤɳʠģʷƬqȞ³зɍɽѳϞ\u038b',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210302:165314.745828:+0000',
                                        '20210302:165314.764807:+0000',
                                        '20210302:165314.782456:+0000',
                                        '20210302:165314.804899:+0000',
                                        '20210302:165314.828053:+0000',
                                        '20210302:165314.851216:+0000',
                                        '20210302:165314.873971:+0000',
                                        '20210302:165314.892770:+0000',
                                        '20210302:165314.915880:+0000',
                                        '20210302:165314.945774:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ȕχʰӈшǭϖŴΏŮѧʨbô¸ЭѾǽЫĈϪϬ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ҧ҉ǷЌŎ¯\u0381ÀőǃʂОƛ0ǻϴǽц\x94ÕUύžɯҘǁŷϹȠɷ',
                                        'É˔ɤӿǤuŁ¥ҊƸž˥Юɷ˅҈ɿɴԃƥ˯ǝӱφΐƾȬцǚѺ',
                                        'ęʈǧžҬϠȢȇǧϣĊŖŶĂß°ɕȻеϠцĢѷʲȵƭĀƑ˖Đ',
                                        'ƜƾΧŸƢƾȿǴÚǶӿς˗ӨͰєȪ˪i϶ΩʝÅƍˤǝуǍĮɢ',
                                        'ȣΌ\x8e¿ɥĀԣԬλȦȌҢ˥ӦxԜϹӤҒΧϚΜƁϰ\x87ƚӿǟëǦ',
                                        'ˬҾǆӰәЬΞĳvӤ¬ËȝÐɠҲȃÓ3Qıӌɷ˨ˈăþ°Ï\x95',
                                        '(?ũvҋ6ɏӞêЈ¸җïɞƿMΝ°ɒτà\x83ǶȺȗӚҫȍъЁ',
                                        'Ǯ˰ŠčϴҼӮҗҖ˾Ҥ=ѣȲүЉŒ]āÝϰΪ:Ŝǿ\x92ɤǺʅǓ',
                                        'ԟĀ¹[a\u038dсņtÁЀӂҀƟμ˱˭ѿ˃ӵϏс;ŪƻпµѼƃȰ',
                                        '҃ҍƟƉԘӍ˟ĝǾԊӝϏȪ΄ʴԥ\x8bϽĜǅėƸÿŒπżўŖĩɊ',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ˈ\x8c',

            'message': 'ɼ',

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
            'identifier': 'ŪǲԅЄWʄŨŊȅɼɹȘɽԅˏЛ˷Ѭ_ɶ˛ȻҴˬȆǡɳ\x92ľn',
            'categories': [
                'access-restriction',
                'configuration',
                'internal',
                'os',
                'configuration',
                'access-restriction',
                'os',
                'network',
                'configuration',
                'os',
            ],
            'source': 'ǉȇүӖ˕˵ɦӖЯ÷ϗȂӶEh\x9cɖϿɳˋ\u03a2ҷŞƁ˖ʪԓѤȣŚ',
            'messages': [
                {
                    'catalog': 'ȒҤÂҢɚτхlϞќĵȏӰíԔһƖҾąԋΘђԊӈНͰ;ӓƠό',
                    'message': 'ӖƂƉƬҁěíT)9ȲěɗǫԞèëÛ>ȃɒˇƍʓȎɟȹɨҰѳ',
                    'arguments': [
                            {
                                        'name': 'ЌaęĚηƶӢzЖĜҕſόɅQӠ˭',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x90ȦňņӕǠʀВłяǩȎϝҊќ˾ΐȺáŷɰƤƸǰͰҢȦ]ӥϠ',
                                                    },
                                    },
                            {
                                        'name': '˭γъȾõō\x9e\x85ʻШȏŅʕêÉҤ\x9eқͽÏ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'ʗJЃѫźԍ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԧǱҹ~ȑԎʙǌCȖ҈ŅϪɳҟˆʍ\x96ȬΗ_ʈÅŝȲȷƵˮʧȇ',
                                                    },
                                    },
                            {
                                        'name': 'ȶϟɪѠӸɪȹӵɑʕδȳԨŏɀЋŗӺӍϮˠ\x8fIЪ~˺ȆЪЯɅ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3886702646159078250,
                                                    },
                                    },
                            {
                                        'name': 'ȄєʧÒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'źŨǰĈȽ˺ʄ˦ùԡЃʗѮӄρȘӑ˸ùʄú˸\x84эӶ\x9b˩˨ϊÚ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЫʤŰɝӔĠӭͳҖęΪŇ¼ΨӈȭδΈϥ\x88ũĎÔˆ\x81ę©Ё¤~',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 528594.6961234041,
                                                    },
                                    },
                            {
                                        'name': 'Ͳ jЗ@ϯѫȚ~*\u03a2èΉԊƽκԩʆР´ȨzŐӑкΗͱĐķʤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʦή\x7f©ţúѠ\u038d&gãɘӖҍғĴӬϫʢɈϮ#\x9eʎƅɫ\x89ЁĪћ',
                                                    },
                                    },
                            {
                                        'name': 'ѡτ˺ԂƜ«ԜʍАyķэ#ŗȺƱɁ҆ÝӲıʲ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3168723112593792155,
                                                                            5346290949717650097,
                                                                            566986903723207938,
                                                                            2789120822247069290,
                                                                            2040744983981846908,
                                                                            -7195432384757795607,
                                                                            990996052650708774,
                                                                            8937568653406392692,
                                                                            484679390942661100,
                                                                            -1815289684669933703,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŠʬǨʔĬgͳÁЈɧĸʈ£ƒϕǃЮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7217006856407139428,
                                                                            4556982790123295678,
                                                                            -8907722255412948165,
                                                                            -8855117171095036334,
                                                                            -8392001196027975798,
                                                                            -5783470660440905148,
                                                                            -402130544304480591,
                                                                            66558092944712339,
                                                                            -8125219244064485186,
                                                                            -3411825929068469522,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ï˥ș>ƥϖ*νʾǰŭǕƢƲͷǽːӠȁƛеŜLΔӱƒМɎ¶¸',
                    'message': 'ƱµΌ˩ԉђОʂЙҚȩїČӜ¾ΞХήϠÚÕȝέBξƍӶŇʴӛ',
                    'arguments': [
                            {
                                        'name': 'ȐԐœԋiɝҔԧČωфϖʈϛ˜Њ˾Ϙ\x85ǶÁ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165249.451738:+0000',
                                                                            '20210302:165249.475080:+0000',
                                                                            '20210302:165249.504186:+0000',
                                                                            '20210302:165249.523480:+0000',
                                                                            '20210302:165249.596428:+0000',
                                                                            '20210302:165249.620174:+0000',
                                                                            '20210302:165249.650544:+0000',
                                                                            '20210302:165249.678187:+0000',
                                                                            '20210302:165249.703494:+0000',
                                                                            '20210302:165249.725579:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʠңňίǣǵ&¹fʕȑ',
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
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŏϳ¿ŝµҸЊƲĵ}ͳ»Ӏȇ˺\x8dĬΪ!ˢƾǱʛЪЂҳɔåĮԆ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ũӳԬƴƙ\x8bСʮ&ʽфűzӜЦѸҬ¥ĒЁÐ\u0380ʱƛCʉӷîπˈ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165250.579107:+0000',
                                                                            '20210302:165250.623085:+0000',
                                                                            '20210302:165250.673223:+0000',
                                                                            '20210302:165250.725030:+0000',
                                                                            '20210302:165250.769023:+0000',
                                                                            '20210302:165250.814725:+0000',
                                                                            '20210302:165250.845190:+0000',
                                                                            '20210302:165250.875810:+0000',
                                                                            '20210302:165250.904569:+0000',
                                                                            '20210302:165250.932449:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϸҏӛӎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8507314839454068433,
                                                    },
                                    },
                            {
                                        'name': 'ƬŃƷӜӠ\x8a7΄ʒ\x9bǸpϸǩқƄКħÿҦƚϕ\u0380ʪú!ӯϒȥΙ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЇȋӾԃԦɿyƪӠѦɚȰ˳бʜΕβЂΩ¶ΏԭϺȐ]\x95ҭѩ®à',
                                                                            'ӌcоɥѹ˰ýϥñȢKȰϋͳӔÑāÈʮʋƭĘ9ȲЎĺҲɁҾȖ',
                                                                            'ŪϤ\x8f£ŘCÍˆО˾Ф\u0381ǉťʤȕ>6ЕЏаʖΖԜԀʱƾӧʁΉ',
                                                                            'ˤÀЫ@ΎйɵϷɈƕ\x9bƓȉƑȍӽ\x89˘έ.ŌΟпȳŹȚΊ\x8dǪԞ',
                                                                            'ƬśϺɾһӭɵА˃ƄEȝԕҶʯťҡĜɣːȳЬŦӶӵɫCɆИ\x97',
                                                                            'γϕŪʚƽϢé˃\xa0\u03a2ОţEōѼФΏҾα˓ΰǴ˩˖ƷΥІҍϩӴ',
                                                                            'ƵϠʣѾÕǆпǪ0ѱpЭωŜƆÿʖŧȺ\x9bԟΈЎÁĒЄԂʢӵŭ',
                                                                            'ԔӡӋĩŮ:ǸҶˉʪԁ\x8dӜφcýԀαm˂ȷƧˡƠǑWͰȹťȥ',
                                                                            'ҏØяyӜɬĖɝ˥īʵʂɴȒΞӠæͽŭƄѳΑѩɳrƑѧǣӼȏ',
                                                                            'ЗɋÍϢѻņ_ӌsūʠôǅŏңз}fϩ³ɫɛÌċҩ-Ɋ˔RϤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɰ˂ƒŴǏʶšӔϥӞҌϿ\u038dӜʜӣӂϛſȨЛǔУϿȵѴşєșӚ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165251.539540:+0000',
                                                                            '20210302:165251.563386:+0000',
                                                                            '20210302:165251.590163:+0000',
                                                                            '20210302:165251.637721:+0000',
                                                                            '20210302:165251.674703:+0000',
                                                                            '20210302:165251.702473:+0000',
                                                                            '20210302:165251.731923:+0000',
                                                                            '20210302:165251.761124:+0000',
                                                                            '20210302:165251.789977:+0000',
                                                                            '20210302:165251.820420:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ȥɈԀȱӋѬ|ύɩΑʉˇĆΓŰϓ'ʛʽŲЄїμѠƒǃȽǡ©Ǐ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÑʮğUʬŏТŅƙŵǏъǌɞĪ%MЕ˂ІЋμҞȡӑЉϤȨҌ\xad',
                                                                            '˱ƮƼі;ȱ«ӰȮ˰Ѓˎ(ʓ˲˘Шƃб˂уÍĵǵ7ҍѤҗŷÂ',
                                                                            'ԀʸԚǐǇԜŒGÔɯàӭŵҨή+ȃӹ_ůϴӫѠƀȏѭξϟţι',
                                                                            'ԗґ\u0380όҧǽΦΟÕŪĞǨΐŬć»ƞĨХ\x91Ϩ£ʌȜ·ΐԩɝƗf',
                                                                            'κχԐȶњәӽĝÓʥӰџЩ˳ɥǚʤϬͷ˻ƌɐӆȟө\x95Ċècƀ',
                                                                            'ȘǭϔҴeЉҮ#SӤĂҫȜϮƦéϻɪͶůʲPɄ˒˚ʘϟΓɒǶ',
                                                                            '˓ƈîɘɩέȺƷʜˈǦäвȆ|ξǣƎȌǗ6˕n©˪ʺүȍǌƌ',
                                                                            'ĖχŇʒҜρͰmɥҷǁȆȳĦǧѮX\x94ýιўɹјѡӣί~Ϟìԅ',
                                                                            'ɇǵԨҰЪźƝͻƯѕǛԔƱјӝ\x8dtˣһʚуñφτȵƴɐĦѮō',
                                                                            '˦Ηɧ:Ȉ˵ͱÝÞ:ԪìP˴ʒ ÎƢ)ĘҍǇs¿Śρʰˠȵώ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȆѬɡ\x80ʬϪρÁи@ϕЀƠvѣϿӲʦӱǑԂοĚ҇ӃǣβæƇυ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʯӥОµϸˮϭƩ2ҫɲ˻kɄԡƻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            842681.8810044138,
                                                                            960661.5438241325,
                                                                            249943.91846379358,
                                                                            492985.6233752179,
                                                                            476762.54659302975,
                                                                            4575.102197033499,
                                                                            590449.5074277457,
                                                                            826917.7710160285,
                                                                            16449.622066025608,
                                                                            -42547.66012527427,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '·ԉġ³_ˋȑïŠҤ҈ǫѩϛΖTÇƩDɜҀАȳ˗ÁϞİҝŨÉ',
                    'message': "ÚӣӴȽҧ˔ČϾǖѯˢΥĬʄ\x8eСκɕҷƽƧƵʝɉ'ǣŐӴа¦",
                    'arguments': [
                            {
                                        'name': 'ǔϋóɬǢѳΥÔ6åҢʿáЉǬϋӛ˷ԎʭҼʝȑӓʽêʳʙÓȝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165253.430630:+0000',
                                                                            '20210302:165253.451517:+0000',
                                                                            '20210302:165253.478064:+0000',
                                                                            '20210302:165253.500215:+0000',
                                                                            '20210302:165253.521966:+0000',
                                                                            '20210302:165253.546947:+0000',
                                                                            '20210302:165253.569680:+0000',
                                                                            '20210302:165253.591822:+0000',
                                                                            '20210302:165253.613071:+0000',
                                                                            '20210302:165253.634517:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЃÈ˹ϻ϶ҏҟĕҲȡ\x90Ԛγ:Ɗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ά5ΤŕЌǑѥԨpΙɇ\x89ȥҲʹӧĲ~æ\x8bĉŬ+ϞʒhʬҊƢ˕',
                                                    },
                                    },
                            {
                                        'name': '\x98ŚčөӅÞʋppŜìΡАǒͿѩĨӦĉҵ\x7f˧',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4939847744619328863,
                                                    },
                                    },
                            {
                                        'name': 'Ԫυ˸ВʁȘќԞǬ\x8d\x99ƱƋŭұ˰ĖáŸļЎӛƱϋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɚ҆Ә˘ŷҵ¾ѬӾëΞϚʪɗ˧ԘКčϭʃіĐ(oÙϢűңĭӰ',
                                                    },
                                    },
                            {
                                        'name': 'Ϳɱ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2347843323894883621,
                                                    },
                                    },
                            {
                                        'name': 'ԮȎʇĤˉϯs',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            304421.061840488,
                                                                            724599.0299852596,
                                                                            931881.9847687517,
                                                                            942455.6910526892,
                                                                            -84701.23347604816,
                                                                            214759.2420668014,
                                                                            365078.58879655413,
                                                                            -46089.29267194213,
                                                                            681035.209004448,
                                                                            652226.7912650218,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȩή˶ӝćӍÛʿͺǫǚµǓɟĬŭŮ$ǪɱѦ˴Μʩɽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'њģÚǊϘҹȹЇʈҗÐӚҙ?ϯÚһŉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165254.860145:+0000',
                                                                            '20210302:165254.878990:+0000',
                                                                            '20210302:165254.898322:+0000',
                                                                            '20210302:165254.916290:+0000',
                                                                            '20210302:165254.934730:+0000',
                                                                            '20210302:165254.952699:+0000',
                                                                            '20210302:165254.970953:+0000',
                                                                            '20210302:165254.990437:+0000',
                                                                            '20210302:165255.009398:+0000',
                                                                            '20210302:165255.029354:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÓϵðUƍ²ѵΣʭǪғŝɍĸ2ɇåҼ˚ӽÿɡʴ(øӸвȼũɈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            127797.79123880697,
                                                                            212015.73349069158,
                                                                            355846.82576127304,
                                                                            846644.6954120889,
                                                                            193431.50819381338,
                                                                            923991.9765777542,
                                                                            975745.3581922238,
                                                                            555976.975984366,
                                                                            -45275.9530280903,
                                                                            570365.0743913929,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ë\x8dЩѓ˴ѐτʹȣǈѠʟѺʷʹģ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2365843152296030277,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ňОǦŦȢOüwћУȇŘĘʥȭΝĔӨӊԬӇЩʡÀǥҍԬҼӭӂ',
                    'message': "ȤɖUΔԊχԡтˤИ=Ԕ'(ϲсȔůϹűɎзUǕƓ˥Ȍȕϣ\u0383",
                    'arguments': [
                            {
                                        'name': '˔ɩЛÄιиǩĤȀȁ҄ˈɀţӝϭe`ԃѲ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ËƑωϛԜj˭úŬīʛЈϫ-Ŧ[ȡ҈ԬƖЕɖӄŎΝIԥńǷɣ',
                                                    },
                                    },
                            {
                                        'name': 'ӡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8644931854335874781,
                                                                            -8387420785334410390,
                                                                            -2361409961929156708,
                                                                            2305765116726138485,
                                                                            -7200533987878231978,
                                                                            -5647046807290114683,
                                                                            3451697610124089137,
                                                                            7734770389699410674,
                                                                            -5211302234754969140,
                                                                            3156475956641389388,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɇ#ǠǅхЦɮŌЏ\xa0ŵЎkԌТž\x9bζӹRFɓ҇ζҒ҆(n',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7751299041765604719,
                                                    },
                                    },
                            {
                                        'name': 'ӏħʐʪʰҳʒʨċԂä*Ǳɉмʐχ¶ȽƧͷĳɂ$ƿŴԘΗNӤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165256.112936:+0000',
                                                    },
                                    },
                            {
                                        'name': 'EӕȂƿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            644892582051140097,
                                                                            -7225765654606922720,
                                                                            429919995407979998,
                                                                            830401390306645801,
                                                                            2291802160539861642,
                                                                            2092808343631130326,
                                                                            -197956486710208232,
                                                                            -1999757439057242411,
                                                                            -4708878925337815569,
                                                                            -3079675013712668712,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĵΥǤԟ˂\x8cΎōжԇ˜E',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ĩ\x96ͱҢÆ"ɏ\x9eӢǍȖȾXϺфŤƂҟ\x9aҔ˞ʐĮɯ$\u03a2ҧΤѿѣ',
                                                    },
                                    },
                            {
                                        'name': 'ːÀŠˋˢʠǾʨƕ\x90ʏԨΟ˾қ\x89áŃϬӻ«\x9fɻӷΛ\x9eԥԚʯǬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЫԇÃŃѭ˶ƬЦԏɘȣȒmҏӂ˓Ю¯ͿƤȢǎŨϐΆӌΘҳϋӻ',
                                                    },
                                    },
                            {
                                        'name': 'άʬѣƦʢԪ\x88Ϳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8925603487334596233,
                                                    },
                                    },
                            {
                                        'name': 'ƩʸňȯҙӍϒĸҒ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165256.874318:+0000',
                                                                            '20210302:165256.898241:+0000',
                                                                            '20210302:165256.922052:+0000',
                                                                            '20210302:165256.945193:+0000',
                                                                            '20210302:165256.967217:+0000',
                                                                            '20210302:165256.994520:+0000',
                                                                            '20210302:165257.021749:+0000',
                                                                            '20210302:165257.046924:+0000',
                                                                            '20210302:165257.070921:+0000',
                                                                            '20210302:165257.093935:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȪE˟1һӦ\x8bʨǃѰϩѹɞSМϣұӻ\x88ρϝҳǹǭɚӥˬю.ɐ',
                    'message': 'ҿҘӺцĐ˟ÇԭНWȍМʶћŧ\x8aȠԈɏЭɱ;Ǒͳǈɟ5ǹΡѧ',
                    'arguments': [
                            {
                                        'name': 'Ȁήча˰пɅ±vԈWԣћҕѤ˅УΆÎϗφцǒӠӣȜțҬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            417861.72408381576,
                                                                            392610.60411702143,
                                                                            699252.7405014511,
                                                                            -68228.46113702779,
                                                                            522105.6738791099,
                                                                            258575.68871873943,
                                                                            270543.94063171133,
                                                                            410080.104235799,
                                                                            588577.0465984038,
                                                                            142111.138381813,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˺ș˽ěȞͲΉгÅŭɵϼƺʆԮ\x96ʨӧґ~ιÃǵÄ҅ҫыσ˻Ԭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4654376607659874607,
                                                    },
                                    },
                            {
                                        'name': 'ÛʣĹśǮʚ¿ԚȪ·ӬϧʹҞĠĞǮƎ¼ŘзʨϙfШŋҁĞǝ˚',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            559237.2993922225,
                                                                            644772.2183236672,
                                                                            71381.80336028466,
                                                                            395777.9220262824,
                                                                            223702.6072511741,
                                                                            408618.8540591795,
                                                                            682715.2476118564,
                                                                            291450.7305838675,
                                                                            856280.8034543006,
                                                                            180167.55922551308,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĥ<ЛыԋҕҧȵΝ˪ÕԑҒȇʎϹғ\x94ͿԡԛΎ˗ҿӶhͰӭǳ˳',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5569456111722073265,
                                                                            7848492066308931785,
                                                                            3143912637698767601,
                                                                            5525629001128818283,
                                                                            7279289245986789859,
                                                                            -7001215887321117550,
                                                                            -6952187838426402444,
                                                                            7593151260316655558,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĹΰɦȕvɸƆ˗ʫϯɣέѼ&ˉϛ˨ԉϋsÃŀ&ηȆ˷ǷѕCɅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 9885.641963966496,
                                                    },
                                    },
                            {
                                        'name': 'Ǉ·§ȳĐĠ¸ɅѕԇŷǁфŨϝϵЎƈӃý',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6217824215317861004,
                                                                            -3848250218546636206,
                                                                            -3583212895935510305,
                                                                            3521472371674499303,
                                                                            -5225333134529920855,
                                                                            -6658293303986721696,
                                                                            6071564414400535978,
                                                                            -4428800262180688124,
                                                                            740767585752528452,
                                                                            3951723511574366005,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԭІж ŅƅǲzĊѸƝʖɤ§ȷƒ|Ĩ\x9a£ЋʅưєсҳҿҫkS',
                    'message': 'Ù\x93ϸǃ3ҷΖΛƢΜïϗ\xad˞¾ȔjJʨʁΰψЈ7ʛԘÍ\x8e˗Ϭ',
                    'arguments': [
                            {
                                        'name': 'ѧӵì҅ͲάçǔϳџσªӬŪ/ɘőrƺç\x85ͳҰ˵ȟɇɩӕхύ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΚÙ¥ĊˏɆ\u0379ϐǑđYΑμɘŠşˊǂϬ϶ϽӏѷИǣУ3\x8dϺѳ',
                                                    },
                                    },
                            {
                                        'name': 'ТϺЏԐǫΪӽTˬ_èŸ+7ĶkʣΫӇыӜԋ ӐƬșůěʎÛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɩӐԪ˟ÝҒĴԞĹ˩ǆϢӄԅĩʀ6ɔÙʹƆŶöȼƺɕųČѹӲ',
                                                    },
                                    },
                            {
                                        'name': 'ȅ\x9cɢưƸˊʛş\x8bƉǜĝ˝NЇвρΨǓѣĽþѸ\x8cӎ6ͻΔ\x9a',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165259.374276:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȼɍǕȹӖ˸Φǔł¤Ҿ˂ŵДԅӠǵÈƹȜê»Η^ӷӾԉ˧˳?',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԛȨrщѰɧƓѸõПʏʱʄѮʫЕґ~ӌμ˝ʗiƨЯп\x83ϠÊ©',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˩ΦǫϽʄӌ|ПӘãНӊʺǞÅ7ɇƒǪϻʭԚШ\u038bή',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ШЀʉҮϴђeÔĥȕ˓ɷҾéȒŬ˩ĝƒκĚ¯кώ˖ҵӶĢʀ\x7f',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                        'name': 'ԎҜԥϛǤ˸ǟƋ˜ʓ\x8dmԏΧ{ļȲҵ҂å\u0382Ŕϥӄ\u03a2ÕƑʵĴҋ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038bkȲэȦ˪˝:εʜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʺˌτɭӯěa/ϐŤ˂¨Ӝɨ¾˟Ϣ}ѸƐÃˤśǤԄğˋ\x89ҟ÷',
                                                    },
                                    },
                            {
                                        'name': 'S0ќħǋ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165300.987477:+0000',
                                                                            '20210302:165301.011265:+0000',
                                                                            '20210302:165301.037497:+0000',
                                                                            '20210302:165301.072266:+0000',
                                                                            '20210302:165301.100702:+0000',
                                                                            '20210302:165301.132007:+0000',
                                                                            '20210302:165301.163904:+0000',
                                                                            '20210302:165301.194752:+0000',
                                                                            '20210302:165301.244386:+0000',
                                                                            '20210302:165301.272004:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЬĪ˽ӳʋɘɼƷθԘ\x9bΒ˒ÈąƠűǚÅϒԛНŏҭ|ȋ\x8dęʎљ',
                    'message': '˸ҚʟΪÄεŉ˯ʊԓԄԂęįKŦÁӎˑƛɋĔǛ½Ԑҧ¤˭Sԕ',
                    'arguments': [
                            {
                                        'name': 'ԑӰԭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165301.512399:+0000',
                                                                            '20210302:165301.532186:+0000',
                                                                            '20210302:165301.553158:+0000',
                                                                            '20210302:165301.575794:+0000',
                                                                            '20210302:165301.597226:+0000',
                                                                            '20210302:165301.643988:+0000',
                                                                            '20210302:165301.671389:+0000',
                                                                            '20210302:165301.697349:+0000',
                                                                            '20210302:165301.721820:+0000',
                                                                            '20210302:165301.755327:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǫŏ\x8fÃГŲжԅǲПӚǐņӿїӄŜvĖąŕʉmŮӽΘ˪ʭӢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165301.891036:+0000',
                                                                            '20210302:165301.910198:+0000',
                                                                            '20210302:165301.930014:+0000',
                                                                            '20210302:165301.955121:+0000',
                                                                            '20210302:165301.980058:+0000',
                                                                            '20210302:165302.017233:+0000',
                                                                            '20210302:165302.064132:+0000',
                                                                            '20210302:165302.128749:+0000',
                                                                            '20210302:165302.157590:+0000',
                                                                            '20210302:165302.191204:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĀƂˉɌϨŷӱ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            737322.6082388528,
                                                                            969383.1381384502,
                                                                            202242.3958096704,
                                                                            -93170.6497970905,
                                                                            -68141.63534144747,
                                                                            -30635.104007644302,
                                                                            469946.4604209324,
                                                                            565939.4490729772,
                                                                            411895.82611259463,
                                                                            881000.719419224,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĖӰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4025227183669866294,
                                                                            4465452231996091953,
                                                                            8068157306480490804,
                                                                            9079737328663701945,
                                                                            1561204280862766519,
                                                                            -1874578694401477146,
                                                                            663708789609231333,
                                                                            -900548779803499950,
                                                                            5975963334160107937,
                                                                            3417917375493692866,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҺԥΟІɺƄǊӛўƣȘҍΦ\xadĹãәέԡ&шѹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ďъƤԦɀӰȩӃȰϫȕɰ\u0379˟ɖƕšɝ=ǚȐǓŘƩҰι˼ԑ\x9aҺ',
                                                    },
                                    },
                            {
                                        'name': '>ΊͲ˲хƨÏƎͰЧŸϿΈ%ňѸӺηԘ´S',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6971585533754442543,
                                                    },
                                    },
                            {
                                        'name': 'ĜҊϔIŲҢÆȸоˋϯϠ\x85р\x99Ĥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165303.348564:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҨȓϨԎʖʢЖƳƖǮϨóˋЋʰŁүͲ\u038d\x9fǪŐƨđɶҒаÕӞA',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165303.459317:+0000',
                                                    },
                                    },
                            {
                                        'name': 'èԚƉƑÏšҙʥď|җǺ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165303.539017:+0000',
                                                                            '20210302:165303.553846:+0000',
                                                                            '20210302:165303.568851:+0000',
                                                                            '20210302:165303.583442:+0000',
                                                                            '20210302:165303.598362:+0000',
                                                                            '20210302:165303.613498:+0000',
                                                                            '20210302:165303.629365:+0000',
                                                                            '20210302:165303.646953:+0000',
                                                                            '20210302:165303.665787:+0000',
                                                                            '20210302:165303.687135:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ľϷɌєԈƠɃИаγӘ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165303.816420:+0000',
                                                                            '20210302:165303.842093:+0000',
                                                                            '20210302:165303.868085:+0000',
                                                                            '20210302:165303.901019:+0000',
                                                                            '20210302:165303.925041:+0000',
                                                                            '20210302:165303.966154:+0000',
                                                                            '20210302:165303.993491:+0000',
                                                                            '20210302:165304.023158:+0000',
                                                                            '20210302:165304.058593:+0000',
                                                                            '20210302:165304.088477:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΝʢѠ,άӾʆΦӟȟ҄ŶśΟƛʋŶ˩ӐʶȳЧŘȡʎԖϞΔӆ\x8c',
                    'message': 'GŧƴǩǚNɬҋͰǫŁНÝê\x97ӷΒϛɕΟÉÑңҺЕ²ÊǏǉ˳',
                    'arguments': [
                            {
                                        'name': 'ӡ\u0378ʶ#˅αԨ\x90űɼßҝ˲ǄÆАɫȪщԛҠŠȖ6ӳľя\u0379Śӆ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɻǉàӱʋĚѮЧäҗҶʕȋLÃ҂ƕŚ4ф`˯ȫöĺҰŲȖяЍ',
                                                                            'Ì˅ͼӇrЃHũſҡÚҚҕêԗǞzѳγ@\x86Ӑ˃ЁԠ\x81¡˷ļӶ',
                                                                            '\x83ʊː~ԆŷʬȇǹЂfȱ\xadǶӇΊɓǩӏ\x95ϧʝ&ЄʺĄʳƞs\x96',
                                                                            'ҭ®ǏӻеʞƟɍǋТʟ\u03a2ǪŻͷ´˅Ϯ˕ԥNѹǫșРӃѧǢήɏ',
                                                                            "ǞċжѠϐʝȫ×hѝ'ң~\x9cΌ:ʽьіEˬǬʅˋĂƪ,ʎiá",
                                                                            '@"ԋΧĎùȚƀ¢ԔϵǔτӨʰǬ˯8ÑƀвӏѮ\x97ӄǔβґļŕ',
                                                                            '˷ҩӐʚƧ§ʄsӘƃδΠ\xa0ȍͶʈΛѾёǵ˟ӑƕѿγЪȨδϪέ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ơ˄ұΌġȘҷѴѾÉʳԂóԀϓјŃĥŏĬϔӟ˨ʠͱЭɩғǕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165304.716935:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƏȨǾǭɍƫïυCЃξдˤȹѥÊԥп˲YѺ+ѺĬӷӵѴļӞʒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -24005.30203396175,
                                                    },
                                    },
                            {
                                        'name': 'ɢҙ6μŷ)Ӻǥl',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 878269.6132723822,
                                                    },
                                    },
                            {
                                        'name': 'ϏӯϔҚ¾кӛԑ(ŠȗӲQÜӈӂūȬKĦͼØѮҙѿÓķвѢĒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 593245.2146158379,
                                                    },
                                    },
                            {
                                        'name': 'ŽʋʼļˤˆԔ\xa0˟ɖЃȹԋϴÜѺGfѰАԫҪԥȤʀЄѣӧКϘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'sѴ±ʇѣyËlÌĵɄƂӭӈɲԠćӲʸѠȔѮʬӱʼ¨ƫ\x9cȱϜ',
                                                    },
                                    },
                            {
                                        'name': 'ХƧƲ§ɂȉϿqɝҊԉзЧȰԨɢӜιɔʬɚŊԈėÈʍϱӑϖ\\',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165305.224681:+0000',
                                                    },
                                    },
                            {
                                        'name': 'l϶ύΙüǑƜòûӈpϰɒ³ӳlʟΝǤЉĶǫƅΰ\x95ԧʄ˚Ӂά',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѠƑɪΏʉѮƭǫφΎüȡǴ҂αϪŴ»Ϥӭƾ\u0381ˏљÿЅ˺ͳƫʶ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ʊĺµϱŗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ζűʜ˘ƣԠŋʿȧнҸҭӏϾȗĈOҼҌȿAāӸӗҾş9ÀƷɿ',
                    'message': 'ÝЖ˄ɗ§ЊјЌǆ2ɱǞʻԇǵņҚɰǢЊҏ»џɃeĽçȃЬΥ',
                    'arguments': [
                            {
                                        'name': 'щϋÕÃϐĥGԌŅҥʘ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            578669.4434414987,
                                                                            460063.0127935135,
                                                                            893725.6224416903,
                                                                            -97585.59919955803,
                                                                            271330.54205512983,
                                                                            202800.031287815,
                                                                            213435.65027979726,
                                                                            168883.80958969734,
                                                                            738747.0240035583,
                                                                            751714.6614008875,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ϫsѭʯ˪\u0383ąϞ'ЀBƁ\x80ʯӼĕīα%ːԌΒªµҦǀ\x80ǐѭž",
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŤԧəԠȃĂѴƅȣȋȞÝωϺ˹ƆӾʛa>Ϣǣĥ,ȮԨǪǑȻϛ',
                                                    },
                                    },
                            {
                                        'name': 'Źςӡƙs',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӟ\u0378ʕsηŦѶнǕbѾÝÑӸԖǆ\x92ɀͿԌ\u03a2фɲȡ+ȼ¨ʃ¢˄',
                                                                            'ȓЖѴˋʾϣűǼľуҍҲMĤŝ˂¥ŹĔЗĶӦЛȩøÍǱǠêǰ',
                                                                            'әлȯŒЕĻœϱ˷ӂăϊȥƥȞ§ʃñùШӺӴЋ˻AҘɿŕҭԜ',
                                                                            'έɳ¨öʞӨĠϲ;Ǳ\x8dȂɳɨόWĈŘȞѼĳćϟϰϹŇΔѫȞĴ',
                                                                            'Ǒbó!Гʋ»пɳȚʣːƺԐŻ˵Ĝ\x94Ӌ\u038dκȚҥαԟŇĲŻӪǢ',
                                                                            'Ѹɢѡ\x9dͳў\x84ͻˋ4ˤϸ\x8aYÊɵȍӶ>Ǘʦȍә\u0382ԢȔӷɝԭ@',
                                                                            'bȢȲǓӤ˓®ǩ\x96гʽǙĜĐ»ĵԍǥƑ{ÅƝИȣӬ˪ЯʞǲV',
                                                                            'ȰʲǞԙȂӱ|GΫÓƛǒʲЈÌ˧ДԛΡƿʡǬŰЯʹϾÌΝҹɞ',
                                                                            'ȝǘȪƒǧҬʟƥǸÞХPÿDȱӱҶӌŵˢɾŏˑ;ɃЭϕʋ/ȳ',
                                                                            'ǁΛӫϢįљѯ҃ӍκʛƙԅЈΡĬԥfʅ\u0382ɭŚ\x9eÁǙƁУϊ˪4',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΏϤȏеğȿŏсŀūѣӆ¼ƹШϦˬʋЊÓbŠЏέɀ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЀˏλŲɾʇǇѝ\x8fɛӀƕҏƳ˩µ˲ù\u0381ȥѮÎǱАʘ÷Җ\x90Ʃ˗',
                                                    },
                                    },
                            {
                                        'name': 'ȶˌϒθ·"ќѡ-Ӱ\\цƤәĆѬǦϰĊĮ˯щӘʧJAзʺӻʲ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2040536683834210652,
                                                                            1464430766459581181,
                                                                            2456048761730881887,
                                                                            -5304443089335685422,
                                                                            -4794352857936391499,
                                                                            4324993530594834339,
                                                                            4749672363811421020,
                                                                            4943067698658784368,
                                                                            1043538407775656946,
                                                                            -5731252058709331520,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʡ$Ӑ͵ЀïħӫƪϠ\x88өţʮïЁƔWɟͶȁͳɰӅǱǱ\x95ЋΨ˱',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -338722708537163729,
                                                    },
                                    },
                            {
                                        'name': 'Ѹ@ϑå',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            182476546392341585,
                                                                            6839650941584730201,
                                                                            4323928991390306112,
                                                                            -6421706601289718958,
                                                                            -6929658288203941739,
                                                                            -2245105846282865980,
                                                                            -153603718805117519,
                                                                            8698369372974164294,
                                                                            -8951483424584465915,
                                                                            -1827137582705647389,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9cӉǃ_Ԏ¬ѫĀđƟÃdϐɪЉԂϹӕΆғƋ\x80ɋΏϥũGŬІĨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165308.016194:+0000',
                                                                            '20210302:165308.037470:+0000',
                                                                            '20210302:165308.067789:+0000',
                                                                            '20210302:165308.093576:+0000',
                                                                            '20210302:165308.113502:+0000',
                                                                            '20210302:165308.133658:+0000',
                                                                            '20210302:165308.154140:+0000',
                                                                            '20210302:165308.176503:+0000',
                                                                            '20210302:165308.199197:+0000',
                                                                            '20210302:165308.234298:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɢҦ҅ΞʎR˓ΦҚоӏѰʦ©ʨʤèʔÓѻȍŁ,ӟõƾàÂŚǗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\u038dђϟ\x86ʂгΦǗδԥŨ\x94ƾóǲΡƒµÄĔɑӞӶĩ-ʄӎѼАȒ',
                                                                            '\x9fЍǷΉjЖɕԈƦ¶ǔΰГŤĚƯèЅΝϬʓӜiǖŸГЏӸ¥ƌ',
                                                                            '&ϰȽȮ[ΓʴїpèӨǦЩǰѡӍeƉˏɾɞ\x8e\x9aҁΆœǁĖĨŶ',
                                                                            'ɒҌƅɎİ˨Эŭ\x8aΟ˪ÌĔċɎΈ?í+ŰԫƝ\x98Ͽ˃я\x8fΝƂϐ',
                                                                            'ԂϷʽȔLϏpԄóΔǗЄΔԣΖgZÛҙąȘţğ\x9cѴxɕŭƎľ',
                                                                            'ɵ;ǛѣҔʑѹˀӽѣôVʶϧьȊƬЉвԙҟȒҬYʼϝʾӵ˼ʫ',
                                                                            'Мʐj˻Γ\x85ˡƒŀǾʟϒȨªӅƞɋνϰɚӓ˥ƭȋč҇iSĎћ',
                                                                            'ƌŒыǺɩʋʿΦЛɊάǫɠӘЩˠɇaYњʳԇɕЧĔ;3ȓǩϜ',
                                                                            '˄ ˱ėʥ\\šӂ(ҺŜȤͲӉʭέҀΘјc\x99ųvȧлϜʔоԏ҆',
                                                                            'ŽӫͿIƭҁ˨ɅԐλUҀԚҢʏϩǆĳˀªʵԝƟѱŹԥ@ɜԐҧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ьӞÏǭʤҙơƹԆ˕şʽГОŷťњȹɪŚȣϊϖ˷ĥҶǁý/Ǝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6895947319090141117,
                                                                            -6956580489047749970,
                                                                            8469105335307422932,
                                                                            6646395867698282027,
                                                                            5401806142730459784,
                                                                            -1089648680854764468,
                                                                            356496219184823972,
                                                                            -1589724951276827344,
                                                                            -6286944602919904123,
                                                                            1210738524524192248,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȞΔ2i˕ʌĐcƱҼԮΓɛƭƏҮΖ˓ȟíǱȹрѦĜΜǵęѮԓ',
                    'message': 'ӯПƬʖǺ\x94˝+о҄¶ҟÈӲϔ҆ǋÀЂϨїͳʵƷмӘГςĔʡ',
                    'arguments': [
                            {
                                        'name': 'HϠӸɛϨүÄĩƖ\x82ѕɉЀԗǵӓÒʵҺϪԎ·˧\x8a',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4160572122586502603,
                                                                            -7227103567281631502,
                                                                            4319462452397228463,
                                                                            6245423016143734698,
                                                                            1630411347221418279,
                                                                            -8140464199413433292,
                                                                            5678477686886615846,
                                                                            722735958088062854,
                                                                            1172782021896553649,
                                                                            2172363428570459868,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƽσǗϵλԂґΏӕ&ʜɈˣѲ-ɗ¬ϹɘʷȳɴmĲűȐ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -796397558620959533,
                                                                            -1842297575451448684,
                                                                            3113162907150136699,
                                                                            -7481849787297840630,
                                                                            -3639742168860418004,
                                                                            7753124915020611214,
                                                                            504037536023453712,
                                                                            5825716229114555407,
                                                                            5228262464591488275,
                                                                            6436563986258810377,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'иĔĺң',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 391901.2718837737,
                                                    },
                                    },
                            {
                                        'name': 'ƃ\x9eњɷ\xa0ʫŲŪɚğ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165310.392513:+0000',
                                                    },
                                    },
                            {
                                        'name': "˞\x84ԕ'ҟŬ\x95ϼϔϙcǵѓƩϺʇǌŞªϦǫǚȕҘ§˂ʠШϷҏ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѐήҺҵ{ѫύǼƸǷϨĮʄάʲū[ǛҰɢÉβϚģȉ˃ψǚńΗ',
                                                                            'ђƬɥǓûʗîɀ°ϜƤĨɈ˸Ԟʽ0ƒ˼ŉťʾ˯?Ģ\x87ɣɥ\x8dә',
                                                                            'ąˈѦÅ7ƉǆĈΰˌ¡șԗÎϥѹ͵ƗЫÊΩƤȳ¼ǬɍӦȋˆф',
                                                                            'çǋɠНȥɘȨԑѝ˃;ĽӎƏеѥǡҌ\x8fɲҊӱ\x9dЩś˓ɠȧĭҜ',
                                                                            'ӁҿôЕȉeяƞØÉɺȃϹ`ê˚ˠҺ\x9bѥɕιȫМτԥŪƿ"Ϛ',
                                                                            'ѰǎԂϛȾęνwѶ#ȞÏċ˟ȾзȘӪēƝԏȑĲÒˣѣǮǲ˜ϻ',
                                                                            '˟ѹŅҝȿқǍţХ˻ĸjɓíͼťǩ\x9eҡЄ҆˖fϦŢǅǺҒęȆ',
                                                                            'ȉϢˇoє\u0380ԘέɋƀԢćрɹƲэԥәԜnìʢͱ@ʟϝiɷҢǺ',
                                                                            'ԦƨȋƮʥÒLϞѱϮ¢ӂҮÔɔɆȰ\x9eΩEӌά ңЊƫȼáǊӿ',
                                                                            'ӜʸwȲʻ˪¢Ȗ;ɒѿʾҀʀиҺĴŷθȺņΤЎООqǦ˯éÚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҡŠіɝИҞÛƆWӄæэӖ͵ω`',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165310.854767:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ũ\x88ŹΈBǏʥŕ¾\x81ǊЪԑʲĽ\x9aͽʮс\x83ʟñӫȌЌŶӸѺς',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ѩǹɂщӄĩ&',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            936788.2983568689,
                                                                            772791.9558256269,
                                                                            798744.0276703531,
                                                                            178876.4692729771,
                                                                            157596.39326635623,
                                                                            887240.0651201684,
                                                                            430252.42928191484,
                                                                            225631.45953085017,
                                                                            452844.9287901134,
                                                                            -8001.527584179523,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'yƮţѯΘˏʥÊǞɽĬŎҧŘƯģӉºʦӨʐҚˁӵѤҮ˖ʧü˨',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Čъeʜō¶иБѦǪ˧Ѩ˗˔\u038bpгĊΥҁ˅ǀƳ¨±ͳȱοųұ',
                                                                            'ȡԁÕńҚѺʖ®ҝɐɪјϝԣύɍŒŞΛӚ\x99ϫʍƴϵƪЈư\x8bҸ',
                                                                            '\x9cРʈa2˳ÙưˊӭƟÀϔ˰ȪϓӾǞƔǬĜҍҀϏŞԏôԟʽӉ',
                                                                            'ʩÖãɸҶ\x86üΚɾőťГƽҩɕGԌҡЂ\x7f\x99Д%ƽіEӜƪİï',
                                                                            'ƐŻ\xa0ȸþϭЮoȎџ~\x8el҈ÿʦv˜ϓɨɈǆûѝǭǗɧĢUȄ',
                                                                            '\x94ŦȕԮȳӪ\u0383ѐŝȆ\x8eúöɌÖǘԕ˩ёψȒшª¬ßϠ˱ʨĹê',
                                                                            '\x91kιμΊĶ˪ҺŘΡ\x86ȮŖӝϒŌÀDJВÀɋȌƋÙҧ˻ůɚӎ',
                                                                            'ӫǼϘɕʳ÷ƀͰśǉ½ǁӴƒєЙԃÏхȯҿϤˌΊÆСї4Ħк',
                                                                            'ЪύѕɵŽĐ\x81ζŢf|ȈѾ˟϶ʂʻƙÙɑ¯З\x8cɘσ\\ˁñЦД',
                                                                            'ĻƄġҁȗĐǠбɠҶȜԡĂȽňϮ\x85ǨҿѕԮ˫~ŏ\u03a2ˡԥӦɫ˗',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x90ĬȄǕǗȒ˨Ϝ$ДһԫөӼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԉӱΪţīʏJӶɏƥ˗\u0380ҔċϛѲćɪў\x96ΪůӮďɞԦİȭŊɆ',
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

            'identifier': 'ϼ\u038b˜ɏˀ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'Ǣϡ',
                    'message': 'Ɨ',
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
            'name': '\x9eʡNҐ˘ľԚʍǒ҃ƎʇƝҋΛˣҺϟ\x80Ėѣ13ɶτhͺӐ\x8bВ',
            'error': {
                'identifier': 'ΌӳPǔM©ȆÙΧəuҔßŋʒ',
                'categories': [
                    'configuration',
                    'invalid-user-action',
                    'access-restriction',
                    'os',
                    'network',
                    'network',
                    'file',
                    'access-restriction',
                    'configuration',
                    'network',
                ],
                'source': 'ĨƐŶǅY¨ɭ;ɕфɶ˙-ʡŜǭμʳ˴ė\x8cˤäҗΘʈĶǹʧŅ',
                'messages': [
                    {
                            'catalog': 'ƻȠȡ¸ĖŵѝΜŃӦʹѐèɧɑȢǾԧæӣƁêşͻ˼ǎ\u0381Ωʽ˼',
                            'message': 'ʫȯɧǮˎ˘ʣʺϴӊͼƄϩыȼȻΗЅƴćȕ\x84ýΙ~ϾλƶŨ҈',
                            'arguments': [
                                        {
                                                        'name': 'ˇįЂςʛĒɁӸ"ŀŕџЮğÃϰͺɮFͱŃ.ԋӆƯɾɏҾǅƭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'kŅԉΘ˸ĺŊώӷɖҶπ1ǧ\x9e҃ьԟƆ˚Ŕ;ǎÓҞΥƣŅƔ#',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʍŏрϻѡʇҲɵ\u03a2˘Ƀԇμ¡äĎˊΞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŧήƫґҡ)љϢԞȈ\\ɈϞ+',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÙƛѱʫʏŵƧΒӠϑ\u0382ʋҝʹԬƞˢҬôʕкԈĖʞǞ¤ΗȖɸb',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1657393017118322347,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Δ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'JϏвΤΧʖĲʑχˀɹĹşΑ³ɧҋʾԮ`ʬӍɁÉψԈϧMØӐ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8a¦ŵϹ\u0378¸ɲԐǴɔʥðâ{ɥӎĶʡ{Ϝ˅Ü±¯ʔʄϧĘӂ\x9c',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -14200.976801193057,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȑ$ĄͷԂ¨ϔɌȁǕӜҽ҈ȗʐDĎƮɖćӾȃҡɪӬȰɓЕ$ˡ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'зҒʅɡƽeĴӝǍбЈӨɩϼ2ѹҏќӢϛĖšǵ\x87ʓΗҺ$Qµ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɀƽ˝ύӬ\x94ɽǒϖȇ&Å¾ƅ®˃(\u0383ύÍɚ#ӀŵӺa҉ō',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 289577.935889904,
                                                                        },
                                                    },
                                        {
                                                        'name': '˚Ʌî˓»ӔeŚʈӻНЉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x9bƔӷƈƠЙҕГŝãԔҒŬϼ\x82ċÄɘΒ˪\x88ӦǪŌϕˍɐδԘϣ',
                            'message': 'ѢȺɲsσǀ˦ĺƌѝЎƞϯÑѠʃΧɒȎìѐMӞӸɣöϿ1Ув',
                            'arguments': [
                                        {
                                                        'name': 'ʎҖƾ\x83ƞӎ³ζԔВŏͲȇ±ÓѺ[ìŘuǋξӭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 919117.4070710574,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǘΌԩʅԀνρҁIɒɥļōɰŊƾǉԙɊԋΔȈǔɦ62êUÌ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8773722598206928320,
                                                                        },
                                                    },
                                        {
                                                        'name': 'eɱԆңԫƆɐǓȸɎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 53759.5326385081,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǩπθˈӜÃèŷͿˣ_зĽďßѷϋ˶АʝЖϹŞ·ȥɗˀˤӳҘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϥɍʽƽkҖҧˡ\x83ӑɳȪ:ςBӮIĸƧɑ6Șӡ¤ǢˋϭԮ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԭϿ0ƤГǗдКϵŽŲȶƮ͵ŊŪėɤƦЏȹЕϬɨƗТ÷Ѝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĖΈń˴Ęƾá˴ʃ˦ӢȪ8ΪҸō˥ԋdƒˣ҈ЗϏ҂\xa0þҿ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƓʎӞњęуШƍҭҖϥ"ѱƳȟ«ЋЭƵЋŔ\x86ҝϒĄgԣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 742436739186245339,
                                                                        },
                                                    },
                                        {
                                                        'name': '˗ҡˮƀ¯ŁπӜп҅ϮǁһĄZϨǐŦҐǳȗŰƊƆǞЍимҬΛ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ńҽ΅ȵȑҀȪǸиӼϭȥӤº',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 903910.7058711933,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˷ɀƲԌÌr˓ĆŒy\x80ЋßʼŬξǡґԖтҖ¸ʑŚ\x9aҧ\u0381Ú\u0378Ǳ',
                            'message': '6ӫїҦĤжÜ3ɧϗɒʚƟѭʽþčҥôȆɿɹǨЩϹӈҋӴΣʖ',
                            'arguments': [
                                        {
                                                        'name': '\x8bЀťŭϜ΅Ģɼ\x91Ӻǳ¤ť˱ƳĥǹȒ7ѸɌѩƬ˸yϊ҇ʝԨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2881136107729941484,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ġɄħèԙǤѧƼɮΑŋ$Đ\x86ǤȼƵˇҦЫΚʈžȵőĭԆǘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'МӘňɩǏиɡϐɌӝȭԥň\x83',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʇбŃΎҼˋҘԈƀйѿпΫɫЛΊǔӯʍιʚԝϴЉЩÉҊюǘã',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹáƺǼºˡóʵΚϜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ӭ}æУΏǬϺӏșŀȜȝΡƤìй¦ӅǓʜϴўƗ˫dӹѕŕҍы',
                                                                        },
                                                    },
                                        {
                                                        'name': '˯ѳӈԕϑȢϚ˜ƵӒȲ˨ӴJҒIѝɋԅ±ӈʹ\u0382˪ŞǹӠǯȵȡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 967384.9888913566,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƯуĶһɂӎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ƉԛtχԍχĽέԍ\u0379'ЯéƣѢǐʋªÚǡɅΨʍаʮØίɐ|}",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u0381ϗÍҖʡϷӘѷŬˠҭˍαȼȔΰˡŝљҟȿ˭Ɏ\u0380Ȗ\x83ʣŅʾǇ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8aј·\x98ǀҀƠ\x8bvƮԊΦíϽ\x8aĻФ˷ʱĨțäȯʠpӖŻ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҷқƔĝ˔ʬЯϑTɂɴţмőăǣĿЪ*\x83ĴЯԑǜҰĞϾɌȉ®',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȍɒƱϢѳĉɰѫʘJ}\x8cĞØ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 842508.923393781,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѯϓ˙ԝͻϲǽ\x88ЕƍЦ˫ʯėʒƹҸώѢƑ\x94ѐϏśͻÞί-\x99®',
                            'message': 'ȱƆ\x94UɚγԚħ×Ҽ\x8e5ƌĶËм8.Úɲ\xa0Ωųѐȕ¾u\x84ǇĿ',
                            'arguments': [
                                        {
                                                        'name': 'ҡсȡԓЛҬʙ˫ŜҖȮӂ΄ƭɮ`ǈȩȨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƆąȈlˌʾ˱CǄԒќӤӊƂfТЪϮЇȂҳƚҙÃѻǊҦʁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĖWıā҂ҤĵΛϣŏöďʨӿ\x7fѡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 998030.2521607182,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86Ѕұ˶ҸƋʧͼеϔƖѱ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 289954.3158804839,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȜƲʅйԠuɞćρǂșқƜӵԌ\x9eϝɭŹ˚ҸÃțџ҇ҳąД\x93ӌ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4375841107712317343,
                                                                        },
                                                    },
                                        {
                                                        'name': 'зbѓ?ǹČѫŚҺÙȓ\x87',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 337868.0588639252,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ąлӛϸưɶü\x8eˡǳɨЇɱ˫ÍӜɔĐѺ©ԚēҜ˶3ȧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165233.060318:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȟęơȖӎɶ@¹ʦˈɤˁѐƀ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ió¼еȯEȇ\x87ǻæˮƬ˲ǭðŉ4ԇȞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѭ=ʳьƬ˔1ÝЛ˨',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 506043.71277133806,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x8cӭď\x91/ǐȎȸǮ1ˉˌñʴѺ\x82fқ\x8e˴һĳ\x9cξäŭÎҁҴљ',
                            'message': 'ŞϨīőgþ ɔʂԗɍɫɊӍĬз˘ɐ%8Jʲ\x9dȽĻϾưқҊ˹',
                            'arguments': [
                                        {
                                                        'name': 'ν˪˖φÇiGӦĦɲüɄƬ˔ƻ\x86èĩӳ}όǝəCįŊĕÌ˝ˤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 711834.9702403895,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˀ\x7fѲΎѝ7ҙӿƮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 408251.9934045419,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȝɳаˑ\x8cӱ¸ϢԂҁϛʗłˮɫɍGˣƳ\x8a˙>ċΐm0ƌ˾ͺъ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'zɭ<3{ѵѪӭЪ\u0381kːӽѼНϲәɈƩͷј¾ʔϓǼҢũҪϐ˩',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382Βΐʢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x86Ϊ·Đѫ\x89ļбǨԦεƦұӴȱˬośĸ¥_ԌƔҕ\x8fӥĩѵӢǕ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˹βлȭʐϴʧuˋƽTéϋɩѕΤɬ¼Ӧƛ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ħƓԂǏŷѽТ\x82[Òɝʲʑʪ\x8b7˝ȤҬăӼʓ˖ԓφȣƑ©Ӱn',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165235.018644:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɬŨˡӸԐԊ\u0382Ȃ˂ØΪĂԎƳN',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8726353933697196662,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ćʒȣ҇ĔʨċɎԦʩӚĻˤλϩӐÄ˙ϹYǺɯԂбӂͻǖԓϦЭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹʧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƪΑ!ΤǔʩűΓŸčҿɐ\x89Ƙ#ԩǀȂț\x8döβǞѰəӠCʔÛ#',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΓÖ˖ʍʦЯŌ˘ӓƀƤúФîȅȷʸȏˋÆƟѼԩʞȋʙ˂ʠÞȓ',
                            'message': 'ȇɩϊ[ɿȅχҐƥˠɷʂ\x9e·ǓҖ\x87âĀѝȏƹɾφĐϤǵӡɖ҇',
                            'arguments': [
                                        {
                                                        'name': 'ѩҷԛĨѝӭϩʨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1133408398625182188,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŏWǼΈƀӛӠɉŝѻòΫќԠбѻŰςɶȍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ο\x9eģȟī*(ɞǒƵĳГѽΦ/ѳϯΒ˵Ɉ˹ĲҕǦϊԩħ>ХϘ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉҋ˳ԟΕŹèȲϪƈǓНԓʗӐǵĶДɝҪĜː',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1085716338441998616,
                                                                        },
                                                    },
                                        {
                                                        'name': 'цȿɭʓÀԙКїĹěƈЇZƓɇ˺;Ǆ҅ӏϥīưвĿųЭǸĩɨ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɼŧЇɿѤѹġʆ2',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8782110926799746499,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѮDȇɍÛ¶»ГӺϾιžĘīŭӹзtæƴ-ғöӲ§\x87Стƴϼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ˮɻʿúħ\x9cʪ¶˺IԥƤǗáȢԆù²yěƣ˃Ήƨ˳Аʺ#'Ɋ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽÒсϳ£\x92ɿǸǛˊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4417124975788122162,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8bɑҭIʓɡ\u0380ƭʵ˓ƿȋWѦĺԤ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ']ПϵŴɂʁԒȖͳ˩ʻӋӺӬŁʞǛɫѾώϫĉˎԜϬv',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æǊ[ɀ¬ϾɎʝˮԤɭʹʫƫΈѡʾЃĻƺɪΞҶ¤ʇӷƜɎԩϱ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϷłŋӾӊӆŧТӞǹχΙӃɾŜͰÙ\u03837nȌ7ӢǝƯϪ˚ҥʊċ',
                            'message': 'ҳȿˁʚΖÅʅӝЯѼʚŝєÄЇǧ˷»ɍӀҡēıƖSʬϪˡȅ˦',
                            'arguments': [
                                        {
                                                        'name': 'ʻě·țǻӲбÈȵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧy\u038dĈҡʰƷϨӉɸȾɖǒЬȕ˭ӝҟӃԑĝӿ¸ŵ˴Ӭ\x86ó8ě',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 339437.431380745,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Řԩӷü˹ıÀʟɳɣ\x857ԗӼӍýԫȉкБӮ˃ɧү˅ˌ2FҦҐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƚŉʽĕƩÝԃøʆǈǆʏЋĥ҅ԗԠ˴ıðӵҀɥȿӭϪԃǎƜ!',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǶЯ˾ɪω',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'φÙǋ҇ēˡ϶ZέϑÇ˜\x9cǘїƻŵǺ6ȧʱ\u0378˩ĆυɱƫÂΗʇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǔ)ϬѯŎƅсR˵Ʋ\xa0ÃҦɶƱƤ˘ʞʁ(ǀБӽνТśƸɁҺό',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1521371021027733218,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЇH\x7fѡӶŶ\x9fȕȔιƙȇĞųÓŊɕņLû',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165240.350400:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'әϧ\x94lļťʟλϘȓӍȢК]\x9eЁӮΎ\x9fyӐοϱυŰť\xadɋўǴ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7881141869082187653,
                                                                        },
                                                    },
                                        {
                                                        'name': 'о˩Õ҈ԣΛǢԓΜZƆӼņԙ\x9aŴϲԈfӡξԤȹǧјʤѡίțˁ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7800922990479512278,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÿɯ\u038d˅ĻԬԆͼǸ\x96ʼƤƼ)Ҡϭѕǯȣҍϰʁѳ¾ɠˠĲǡζƓ',
                            'message': 'ɈʽɸÃп\x99˸ӇѬp>«ԧ˛ƀЇŧʲϠьʲÒ@ŵӼς\x9dϚͲǌ',
                            'arguments': [
                                        {
                                                        'name': 'Ěϕ\x80ӳӮÍȐҟԏśĒËņӐdĀ\x81ƜĲѥԌş¾\x8eĨͿ˳ҟʻɎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 338528.5887917367,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ōǿҁѝõ£ϺǓӶʈˍŵӁL҃«ԨŤСπǬȇԥщŏжŪЛЉ\u038d',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5854910036593081253,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΘКӟǑΗ±ϬɲԚəλɸǸˁ͵ˬŎŧ¤ȣϐ©Èû˙Ĭɋ+юl',
                            'message': 'ӊʷī£ϳʀ=\x94£κĖġԧÑˬԟҁűͶFПȲ|ɇņмˁihӚ',
                            'arguments': [
                                        {
                                                        'name': 'ԣ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'юĿuƳүͱ҄ˋĀǾ»\x8dGđҬШƵʧćÞʹҩϑȲæȦǏCxĒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɀԍю\x83ŅȃİˇȃǾҚàȭ҈Ӗ϶ԜҵßʍŠ;,ǀɍ\x98ӒӬ\x93š',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʮɌʲŸħэˮԧ҈\x9eǧoȥφ#ΰИZїśǌʪɩˀɻ/3qȫʀ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x8bӨǏÀϛơѨҏӀҸԤӭѽȚӪØ0ǴʿǣΥѕhɼɸзƮ\u0379ԒĬ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ñб`ϑåӞ]ψ2ǊɖBЋ\u0378ĥˢнΣЦϰĩōκʞӓχHҽԖ\x88',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165241.495432:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҁɗȗ9λχ\x9eϔɝДϺ΄ŃǸЧɃȆqPԋœ~\x8fªgԧǜŭŨÚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӈϧѡͷzʦÿ÷Ɨҧ҇ϰĹѐѲΩïˢϩԀːϛЊłѼƟƳdē©',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165241.692228:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѵŵƃєϷҝŲɰʣʻįź"ȇșůɑʾűʛ\x95҇ʫaʛ¨ƘǲϿʇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʷūѸåӹƕFˈҺ\u0382Ǡƅӡˣɤ"ԡƎÓɟАϕʰǛɪ¶Ԝĕ3ç',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅδȁ,ʋŒҐϑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7950429587700957805,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Qϓ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8334040916678425318,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʓβˌӼŇǅΏΈӬńɏўÕӝԐƩÍӃαəҽĐyĪΥȠºыϤʚ',
                            'message': 'ưiЋԤĞΆěʚ;ρȤҽȟԘʜˁǗ¼ƒθ¹ƗËьϗ`ԉʭԆҚ',
                            'arguments': [
                                        {
                                                        'name': 'ʳқʺͷθˠϤȓѲËɑԀń˕ѥԪÓƟԥȖĩөơφΡǦǀҥɢȆ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņϲÊʏʿǐĻ\x7fӋԢИƍȟϮu\x97m',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧĊ˹ҌçʮùεκʃѥǶӺКτНѾ.ʎǝFҺԕ<ϙěѮDƗӕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӟ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -58729.95241959417,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ơˆȑҏΟĶ+ȮҔԊ»˥\xadˆԃˏϟԀАħƗϛǶӌϞýǃ˒ƺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165242.779071:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'źrυɦИӎԇΔĤШяУêϝʑɥҔӿǫ˻ӇĨSʨ)Ňː\x8eƀˬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĒőƜҽƅ»ƝǉƝǯƳяȧѱ\x86ϒ;ʜũɥҍΎǔԑҮӱԌƳХΑ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϦȏԩʥÊԥĬ¼϶ȪǍj˔˩ˮϙŰѝĬÜËʙвɋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÜԭȨŵǁƓ\x9dʹԤиЦӬ\x9eΓвÅѓê',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԏ¬ҐȎӍϴɮmɖȓХԂ\x95ǀҰ¸ǳƿȀɁѸĄĵʩƳҟ\u0378¿û',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҸƢʪӳЦ7ƂѮȡ¾ӯУӜψIǇ˂ԌǔǮʧɥЎgӸɱϘ҉Ӥĝ',
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

            'name': 'ɻԏɣ',

            'error': {
                'identifier': 'ɅѩԋƼӮ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': '\x81щ',
                            'message': 'Ѥ',
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
            'event_id': 'ėԊȬ»ѡ²к˼žǼπѪψ\'ЏʬҰϩήɅýĵԄ˺}"˄ųʮǬ',
            'target_id': '˔ǹ4Ý\x83ӓȡŸԌʄСъˍѣ®μêӕļâɓAҳђϥĮϪŉԜˈ',
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
                    'event_id': 'ʤķˎ\x85ϬɈhčΛƉȖ^ϋdκӍȅǦщŚԅśˬȖîĺ\x81ÔáҞ',
                    'target_id': 'DҍСʿѨTҽ\x84ɖv˅ићΖˊӂ·\u0382ѡБŽϑ˞ԬiӃĨ҆"˺',
                },
                {
                    'event_id': 'ɞͶÀɚԥӴǰ\u0382ŗԂǯǑҫŵұжϲœʍȿҫʔț®ŤCɯʸǌI',
                    'target_id': '&ТμQжƳǩƹ;ėűġъ\x87ȡţǥ˚ÛŠҟѱ\x83Ŕϣ[ϯȊöƜ',
                },
                {
                    'event_id': 'ΗˠƵƺтȖƂēɰҍ2ɪӵΎ\u0383Í\x87ΌӠʣɐʁ(bʫǻʠӟҕ1',
                    'target_id': '΅ķϨԊԊρ˝ș:ƅɗъҺ;ȘȒ\u0382ĥ˽Ŕˏ\x82ɣȪζЉǡʾ˰ӟ',
                },
                {
                    'event_id': 'ˡ҃\x8cϯІβѢÐǱɹӖψm=η&O¥ǴƆȕЦԒӪҙΫΑҀǕԫ',
                    'target_id': '΄ɗŷȈц§˯ӠϛǋϖҍēѴ§Ԑýӕ\x8cҬѣͻ3ͽȆqǱɆǙ҈',
                },
                {
                    'event_id': 'ԆǏĴƏǧɍʈɓɕǣќϫ7ϖĴѥѬύȼҖʳΌƅɛпÚŃ¬½ы',
                    'target_id': 'ȑǷґяȚӇfӔTįçFѡНԢWΘӗÁƯҼҲʄΓͷКʄ&XÚ',
                },
                {
                    'event_id': 'ӋƑƮҝ˞ӶcϤҏƞλϛʽˆȣʊЃԕѷ¸ɘԚʈŻˇʪʈʆ˻Ө',
                    'target_id': 'ȲĞʱƂȶʞʄī˽ÃˋǲōɔÚ҆πǙˎƖ;ŌԊϲӛ)ʰĶœ҄',
                },
                {
                    'event_id': 'ȚЛГԪѽ³+ϫ.zâcɿʺ\x98ҧ<ѺɊеɈǠ\x94_@¾-Һǐϝ',
                    'target_id': 'өǋѠӁŏŠηǍƆɷÖȃаƙǞmȘȳħʅžƻƄѾžБӬҍӏɫ',
                },
                {
                    'event_id': 'ѾƏƌϾӲśӎıž³ȜоŢΡŬ¥ρ2ʕѯЍʹϫðʧǸ\u038dτԖб',
                    'target_id': 'ҁƣƍΛ¦Њήϰuǀ͵˧ûžʒ˖ϵѩʭ}ǬЈ4ɨӃɽΚrȜϋ',
                },
                {
                    'event_id': 'ЃȘїӜ\x8e½Ӗɚſδ\x88νξȑʤ˛-Ș1ӍЭ\x93кьѱʟΥpãĦ',
                    'target_id': 'ϩǻўÿӽÒѰƌ˧\x92ǣѾϏƺτˮǩʒŮǡǪ\u038dǱÚʪĪӡĈйɣ',
                },
                {
                    'event_id': 'ƱƢΆȓȔȂ˻3ˠӓĹȝĬԬʛeŝӄѴĐƵĘΰŭYuтTΉЌ',
                    'target_id': '҃ñșʻʗМ}ǑіɥМəˈk<[öΒѭƘӦ~ßδɊưʹͲƴĸ',
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
                    'event_id': 'ƏeдӡτˉɎҷψķǟЊӤΣĭɢ\x90вǤ;śλˠēӐΩѶ\x7fʆѵ',
                    'target_id': 'ǥӢҩ¹Бϒ4ñÿ',
                },
                {
                    'event_id': '÷ɝıУψŖ¸Іč˺ԭǴɯʰ>ìξҹɚͶƦ\x8fєʿȧҔʾËЀ¤',
                    'target_id': 'Ȋˑƥ³4@ǗѰπĚ¹˫ȻχŵɾĒĐԠɶʏԑϢҏѾѨϢʗѭϧ',
                },
                {
                    'event_id': 'ůӅө\x9aŦӋƊˏѿˏÇʹ˷ơѼҖëºɮňΒKÙϑσϕ½ρǻʵ',
                    'target_id': 'љΟɰδҪЏšȶϏȢώį,ŘÆԊɎćΟʼœƷԪΚʞԟʊ\u0383˭;',
                },
                {
                    'event_id': 'Ȓ¦ІАΧ\x84šƾϡÅƴΙþԒΥўҦϸǍӢɡϽβԓϡȪʣΎɅȶ',
                    'target_id': 'ƣӋͺѡȍϖ´\x8dɧΌćǕɎɥŞôЂӱΰǠĜ¡òӄҊѹȰԙίϻ',
                },
                {
                    'event_id': "ӕʵ'ά˹^ӸԞŘŝºҸʕǧӚ7ʐʄӢǲӍŐʫΕӞѨ\x9aͱʚĎ",
                    'target_id': '\u0379f\x86ЩсʳĊђȝξã3ɐK\x9eQǇHɀĤɡʟȩ˧ǨѫϣȂ˦Ҋ',
                },
                {
                    'event_id': 'ȻĈǩÜЕÁɘÎõȁξɫέїʹċ˺Ӥӎ\x99Ʌ>˶ɟʈǅȿЕȚʔ',
                    'target_id': 'ėЏёµ±8ίԄ˾Ҵįӿ@ʡɾҭŔАɟƐʥяɿǽŀωҫɉǦʈ',
                },
                {
                    'event_id': 'Ȥ\x9fÌЃԔǊĕ>ȞȾɊɒҕʦʲŊη*i˪ɼǕÕГϮԝêȭћҁ',
                    'target_id': 'Ɂ\u0382πГŻÚǚĵχmȷʫМ˼њɲɎ\x8eП˦\x8fγҩɧĞӔԃĉžΪ',
                },
                {
                    'event_id': 'ɣЖԅmľΈѕÑцдʞ?ŎҲȥӂΉӛÜīĐԞÉҲĚľť\u038bΖʁ',
                    'target_id': 'ŌŃÙŚ{\x9cЕȶŧԀҙ2\xa0ƾʓĎĂʙ9ϐɸ\x99ж6ǞɁаǓàʝ',
                },
                {
                    'event_id': '§˦gȢͺђǭӖЯƗ5Ǣ\\Ңψʙɫġѩ¶ʂȲ\x9dλɨяɎ˒\x86Ǽ',
                    'target_id': 'ӦӘǑĳҦϊɁbЋςɄɾѻÐȜ\x8c¸șðƁɱϑȢ¨;Ϟ\x95ǗʬȲ',
                },
                {
                    'event_id': 'ơþ4ǏŚӬɵӋŤ˂ɂOÀФМĚ?˶mȯˁќ˳ѺĄӟҪĶДˑ',
                    'target_id': 'ǵԌϼˌ\x83ˇȑ˱ŸѣƂřǟ?ʣҫ˽\x8cÖIäşϟӦѯƉʌѮ\x8cĎ',
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
