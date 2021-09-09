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
                'űӟǶόİɉđȀӿӂſǨͳĚëͲԨƟ˭\x845φ\x8cfϡԝʱðʜӞ',
                'әʼԄҖѹʙ\x97бѕȀƐǒϽà¹ŌʐϫѶϪñӌǊ<ıęʬƶǿĴ',
                'ԇǫҴǅͱº҇˩ТɁwϰKңԨŭӁԙҒѿѧǸĮϑɻВΕˢ\u03a2ɛ',
                'ҳƚЙӴįΚǆ˵ҭ˅Ԡ˳ɽʋԘʫѡŚҗƌˡЙɖԪƖřіОüƊ',
                'ǯІȰMӮk#zӼćŤȧĹ˹ȵѱєҲʊŔԕʼ\x82ȔƃŬ´εИƞ',
                'ȞǜϓɅγɠϛĒӛϹǘԨԥ\\őԜҹӹӫӒ\u0383ˑ?Δ˒ŮȏʹʮԔ',
                'ęΈ\u0382ɑŗʇáȪ\u0381ƇñӅǥίŻȐϱʪƝșɑɾ³ԐkļνɞŞɟ',
                'ɧ<űԂӨƹSӾƎźӸʲůăåƙ%ûȻȻ÷Ѷ,Ӽɠ',
                'ĻѬԦĜ=ȨOį#ɑԌƊ˫ӧʿȐʫѕ˒ϚùɮěŚӇÉłȵˁΦ',
                'љłLͻǘҨuӪЫqдɠǒÅȰϽІ',
            ],
            'source_id_prefixes': [
                'őϢԩҾÊԇ͵ϭӪʣϚОɌȜƀlӧ\x92B\x9aӱӱѠϦuĒͺ˒ŉǣ',
                'ѼɹЍɣЍĂŐ˲ŊƑĩѼĉĿϧŬԀ˝ʉӑʶŘɼыԢ\x86ȣӻʐÚ',
                'ё¿ɢ\x97ѹЛϊɑTѲ¼Þϵ҃Ļ{ѐćȰ҂Ά˝ɫѻϠŵưlǔČ',
                'ΊƬżŬlƌȯȱæʾԬǨɹZĳǲÉ)ĭȴ˕ЁˆӊŌ˚`\u0383ȹӳ',
                'ȀȌʛНůȕĪņӤňԇ\u0378ĕĕˑÞГĆ>Өκˇ˭`ԘΫԚҲ\x96ʎ',
                '˶ĆƼϩÍҕӝƿԉюřϒǫʐǸȓaʋŁШBmѬԍƩǛԁ҈¯Ѫ',
                'ǀ\x8cˍϻӼ˹ԐƳʢˀҘЅǜҀƕϕCʜџǐΤѮŤАÃϕҋȤŅȇ',
                'ϱĳśɜÂϗŠǕέɔӰ°ѣϔѽǢϕΈґʳʝ',
                'ɓѐƥ˔ѫȠɌԬ˨ZɯЗȰʝӔ÷ҒYƐƴҔЅԎŷêÁ˔ԆҦǇ',
                '\x96χɑȅ\u038bɭƃӚϴАѼ˜ǑӂϲłΪ˴ь˕ʢǚҖōͽβ˳\x7fŘΩ',
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
            'action': '¤ƃʜCȬвķ˄иĶϴЮƘ\u038dH½ԢͱШØԑГ¼Ӓ˭ͱ˳ŹɌӣ',
            'resources': [
                '\x9dЁƄļҧȋ΅ўҿŸ¸ňͿӪrѢȸǨƾԈӞɳԤŬδʗɿѲǝԚ',
                '\u0378ҸЄfδĸȢɢԊȧшk˻ɢҿ"#ɡŁˌ\x94Ӝлȑåʛ\x8aцЩ͵',
                'ȻΒЂѪпРŢƝqɏԩɈȠԐɜy˶΅ɅǪʉó˓ķJƸßʎΑӦ',
                'ńѮʰϐÏƌҢѝɩōâ¾¢ΣщιˀӖĽ*żԊ˦=ƴɓԨźSб',
                'ʝ\x8aǕÉʑɝЗѽ·˝ʺDŴӠȮΓͳԄƎʫӥԘҦΞ¾ʰ\\Ɩήǯ',
                'ўʺҵ˭Ȏ˲ƟþԤ˻ʧŬŁğʹӹǈҿǱүǇŜďΚ\x93κņΗͰѰ',
                'ѵ\x81ЊσӍƚϯɥiυùɒ¡ѷ\x9aҙǺXǨǸԅǍʃǥ˓ŝ˃ĬӠª',
                'ˉʠϜЅ\x8aĺɇʇáӑſɊʻİ_/˼ԥ¹˭=½ƨ1ϊĢњкҬФ',
                'ƥѽʰ+\u0379јƱrƧϑϭ¢ΗϜƐ¦Ы¯ˑ˵²ԁʼþɑƆÃ˹δѢ',
                'ġщħǵȾ7ƸȪш\x80Ͼ˛ɺɂԣʝĤɕыҭΪԃӘʇͼÑӽ\u0380әė',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ǳ',

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
            'name': '˙ԣ\x97ōÃoʐήþҧ',
            'version': [
                -8053462073823819357,
                -9176703081965021450,
                -8589446866564652047,
            ],
            'location': [
                'ˣQ49ʷŀΙкƝŽχʆĕġί5ȅʧǀԂȘɀǈƻϩǔĈȐ҉ɭ',
                'ѓ#ѴиĮűωȵΔА\x8dѬԓǝüϯ¾ϥǡ«RŸ˱ɍϹʣȟĭзƿ',
                'ǧàīÄ˯ƛұ͵ԡ˄ŁɋФҮďѬď\x93ӊԢɫǙҢɪҲԏ÷ɏ˒Ȼ',
                'ɲȻǰƇͷʮЁƬ\x83ҰˠϞƯϮ˱ºǖɓƣӴҢϿЮ˓Ľʬ9ԁ¢ӳ',
                'өȑʽ\x92јˑҧ¥ҁқϕǝÇ/ӐzОwԧ\u038dƓˀǒɘԤƾϴΣ°p',
                'ԌҬǂɂёȌʖсě\u038dЭàћɢyŅѸȖӮΟXƶþŢϋśҹʫuІ',
                'õĝϿĽĮюȃŇ˟ÁɷKϋԘfɒϼӣμȍУпʄӎ¶ɫƳϺǄј',
                'Ǧәԙуʿʏ(Ϫ_˴ČȨȝýϥz\x8aâ¯X7êƜʣwȆҮŁзɄ',
                'LԐɆǞӤ·ҘӁ\x93ɭʌόѷȧԜĞüɲϺĮǚǋњҲǹ҄ϻȦҀЬ',
                'ūρӼNцʏЍɝ\u03a2Νі\x84ОсǸƛʟˊήǥԬ2ÍŒѭ\x90ЀʚKɕ',
            ],
            'runtime': 'ϯŻш(ΝΜԧkęӺҒԂԦʭΟ6Λŝŵξʻ',
            'send_access': {
                'event_ids': [
                    'àĶԫ7˝ƘĞó.˅ŪфӾҕřƥҋȼŉҲӱύ;ĪвüºȲǙШ',
                    'ӚȑЛӒǣӮӸӒó˗aȒ˙Bή\x8cӨǱǣЭʵ²ōӃзPşʡŞɻ',
                    'ɛû\x96ƐҾĞԈγΤБ҂˯΅ϕοɡƭϴΧņС\x95҂ĞŜԞ˸Ζφǰ',
                    '²ǚʵɛʰĬԛȍ3Ȝ˻ԛȇщ¥Ӈȼϯ\x85ͱǋ˖г\x90ȝԧƱĕΠɯ',
                    'ǣрĂÚ\x82ϻžСҡ¸ϳҷƖťãɟҫʧ\u0381ɢ˟ƍŨi\x99\x8e[ΘшЩ',
                    'ΓǗ,ңҏŬЛƽШȥP˰ö.ҙӞѕϦ½ р\u038dúʴұӢӟϱĴӄ',
                    'ƲыӅψwъñ$ˑҬɡµʅưϐÞªȳfџ©ϫ¬ҶͻĴΕCҦɌ',
                    'ŒǟʬĜŵŃȩ|ƢȆġӵ˳ӾˑĥřʑʚȺĮӴƛΆΥӣɦμΈҲ',
                    '®ν\x8aΗͳ\x8cOŗϫаĻȪӖθӦƏΥ¢ŻЩԜȿзÁБǶ\u0381ѻӳ\x92',
                    'ŪʻƻԄl˰\x90ϴϡЛӷäВӆżԈġʽȾȯĳʵϤwϊ˶άćɔԡ',
                ],
                'source_id_prefixes': [
                    'ӇǃϒȂωέѭӈȘҕ',
                    'ӃʍӊԠϾ\u03a2îǠSÌŗʀŠÛϯÝԗƍ·ʹϲɡľЏǓĞNɛäʰ',
                    'ƬŸ³ҤʫӃPłɾőΜԠӰӉȰуηԏɼ˸ČèĜѫѵԊԑϬмɒ',
                    '¤ҩŪǨßėҒшҋȇØΝxʚĻˌʾ7ӼęˈΰкӨόӭϝԗ˵q',
                    'HŴҹȕƎФȨÇ»ĵϧĂǾĕɋȔ¿ʴ\x97ɦɷѩϻϜĲΪɽȏФƖ',
                    'dªƘ\x98Ɗԣ¤ǥǳҌ$ЕȎʉjӰȃΖӚȽȜ\x94ȴӵҤӾҟġǿΨ',
                    "üЩņƍӼλυõԝуƙŕЋΎɓʓƞҟ\x83Ȣ\x92ʪʭϮȠ'ұƂʒǀ",
                    'Àü˘ɕʇú.ҹ]Íԗ\x85ӹ\x89ǙΕÚ©ѦǷȜ/ԡˋŦͻΕÈƣҡ',
                    'µYƲĘ¾ԃϐľƥ\x8e_Цʚ<҉²ƏЃρÆБêŕȮν¼Ӆуɝ&',
                    'ѮԙуӕϢԢȈòɨŀԩ8|˼ͽȌūԓϷƁ˗ǅʁȅȢ˔ы˨2\xad',
                ],
            },
            'configuration': '«\u0383Ÿˉ8`ӚӖʋӕƤƭíȏкЊǭŮѺʹӥˑƓȚèү\x8a˴Иȥ',
            'permissions': [
                {
                    'action': '΅ӕO}úƿ+ѵѨ҄έŭĨĞ"ӄϝҌљѯͷ˘ƀЃӧȨτȎӻĪ',
                    'resources': [
                            '\xa0ĮŖʌɮċŘƨҏδѤϼƯʹ ЅβǱΓЌΩǆѝǪþéǺΚÌŊ',
                            'ҝ',
                            'ȝǅƐû.{œǿʟϛʵΛ˞Ǯ)нǆЙȯʹ˵ʥȋȭgѺϪǞҒқ',
                            'ΐ\u03a2уǣ\x9dĲĞΜłҭϹĚŵvΐϰɹʖſЁ»ǚͱʏɆӃͲǅ;ȱ',
                            'ī=ҶţŷāʰωįӲ\x9dŻęӁfлҐʅҸħāөʘSʮÏӦҠȗJ',
                            '\x89ƊʉơĶȥǲ\\ΒӎʓǃʐȡͿĪÇǠHӅɤíĶƦ˨¡ɈаȌ\xa0',
                            "ѣǛċğǴζyɫȬƟ'ʹѽυϤϋɳəɱ£Ưʢ\x8esƇ7Ɵӝǵf",
                            'ƕŴӊΦyϕЛǎ«÷Ԋ<˜ϣѝԏ\x94ΦāĢKǞʷ˛ԙʹĚύßӭ',
                            'ϟϿ˲ҾϒŗɍцсϙƍΔf\x9eʋʆʟԈƟӳďϮӶżѪȷыĎѮƈ',
                            'ыǽІ.ѷ\u0381͵ˮĩˀ4εaΙҘÿʒÓ\x82ίΰ\x97ɆӃW˭ƣȵЬˑ',
                        ],
                },
                {
                    'action': '҄ʙИЖԊ˚ϔυţĈÃѤŒȧҺҿĨQĪʚĳЌÛŪϽťˋφʻȜ',
                    'resources': [
                            'ԖӹτҮԮ\u0381ȎZìşĊΗͲ{ЫǎϣŝɕôĢҩʩȻÚɏȵҪȓƈ',
                            'УȼʐηϤɸæźЍϜɔó4ƏƫǦʠȴпƮξɍʨƌȗĆЅӵ!\x81',
                            'Õtӛˆ˧¶ŧҡїхԊ˔ɱ\x82ԮYԞАn\u03a2҂ǢΆǧρ¿Õ˨ǭʋ',
                            'ŚǛǃǔȺӒҶъŌÅÝ°Ǯ҆ϗάI˜\u0379ԧϛɪɳ¤ΆʅeȨǜŇ',
                            'ϢŻτÑβӤӍԝǿҿƼãυ˜˛¹ʃ1ЖǘЪ~ƲҢѮ¶бԓєG',
                            'щ.Ăȡjя\x93ї\u03810șɇ{˰÷ßȒė\x96˺ǎͽĩƖΙǻɪӆȟқ',
                            'ϽɺţӈgƕǙюˉġ˹Ϟ\x8cЊӝ˾WГ\x9cΫƬТɚċĵƍǉмĎԙ',
                            '҉ǷȎʛ˨ϋԧў/Ϊ½ŁҘ˴ǎɘÄѯÖĨΖîҸ«Ł´ʦʾʶg',
                            '\x9dͷʨʕ˺ұžԣ˧˅ҬğuȔǌǄϰɪп!ȍԂԄȻ<ǃƅǝӃ˾',
                            '»pȳȔӍРЩΛЅΤѳ¡ȡ½ҹĐt;\x96áȄιЀшƀ£PƧɘɘ',
                        ],
                },
                {
                    'action': '\x8eПnќϿұҹŸƆŴːΜθ\x92ˑĺOЯέ\x97Ǐ¹ӯӷˁҖԔƭ˽ɘ',
                    'resources': [
                            'ŮɬԍҶ\x89Mł¡ԍ\x88ҐòǗTȀыĩj҂ķ˚ȵƶҐ˅ΟӤºª҂',
                            'ćŨïԆuҧ\x88я\x9eÛ\u0378ƒ/ԤɭзӌŤΦҫ\u0379FҾИˉҨĠԪgѢ',
                            'ѡǡʨҹԈƙÜЀǦҘΖ3ĩӪƧѲ>ƄȼЍɶêĻĥΪ]˥ƸӬά',
                            'ӨɉɒȠ`ǬǄʵӌŹǿĐ ҸӡņǺ°ęėźȴ\x82ƫƜɴȦŉƯϔ',
                            'ɵ\x80łǔÖEȦƤӬŉŕԆЦНÛġ˳έñȧ\x8dȗѮƨӦPҞάĮƶ',
                            'ЧąͽǧƵԄ\x8cұΟԒѫʽȢŒɏěϼȔӏȵΚțƍҧҘb#ҵ˺ʬ',
                            'ˡȞĊЈ¡ҒŐԃǈÏόº΄\x8e\\šґҌȅɺđΐτκ˜5ˠҏҺѤ',
                            'ӿϸƛǚ˸\x88Џß˙Ö!ǃĳҐNӟʸНѴԖͻ[ũҲŎǡѩɗŦŀ',
                            "ė'ĽˉĞtєʣ˯ЫŸŧκĨȾћ҂ϝǌƙўƹɊѶ$ӏńÐͰȺ",
                            'ǿӈCȢĚҪҔ#ǉыĳɶƞӛÄƅԜɗ˺IÊËѡǀΊĞɶѿҾΡ',
                        ],
                },
                {
                    'action': 'ǃν¶ΑĻņȠҪ˭æˮ\u038b˰ʴĭªĴͺԥӂӼĈɕϐǱ˼ɳҲƣϹ',
                    'resources': [
                            'µŖĔӀàҨ»ΊĬмӒǤĥň·ɃҊäӌðθ\xa0ÌÿСѵãˆɆȣ',
                            '҇ӄӄԘRԮġȃѺƠһưьΤțȬʚӷԮAȟǤ\x9b`źđŕþ˛Ԝ',
                            'ͱɀҪĒͿɯҹ҈ΒԞЫўоςˠǰġɰñJӕǰƵk²ɻȬʸŖʔ',
                            'ǰ5ӖПɾ˗ήŶˍ\x8dӸѶΏρȗɍWӮɲρй¥яƷȷzƃ˟ʅԟ',
                            'Īþåˮ®ˢ.Υkɒεȋ˦ɯԏр˻ЭҸ\x92ͺəˌˠÅĬzŤ˰Ţ',
                            'ΚȹүȎƋýОʦʝ҆ӼŚR×ɩʐϱŸг+Ҥë˅ϡʊķӵŀϻҶ',
                            'ɢƽΕÑĪʄ҇Aӏҋ˰ҡӐɤȼӀѯѝӫʈӚƐǓȁӸǮƑïȹϚ',
                            'ȖɎˬѫɿƽл×ΒŮϙƿҌѦяӑѶʐĵʃ[É˹ȥ±͵Ҍ\u0383Ҏǉ',
                            'яɡƠǾʅ/ӉĀȑѼҒĳˑƗĩӔ|ǝҦώ˩ѤЩά˫9:ԅũJ',
                            'ЕȶҘҀԕȮԗˢǀÊсĮҾ\x94iʩÊ¸ʕʗϐĶĝćѬʽҘк´Ð',
                        ],
                },
                {
                    'action': 'ƿͳƹТс˔ŃəoƂͻ~%ȵԗȍлȿύʧȖёΎÍ]Vˮȫưĳ',
                    'resources': [
                            'ɟŵчϵӸ\x88΅ѳ,\x83ƷΒ҅гЌŽϫŸŪƮˎαϸԍҺɫӔ¾ҭη',
                            'ƮȺ½Ӱ˹ҡԥ(ƴȕǲΌc(ĖɪȲʻʎȚԦӨϧͷӔǦ\x98άąÎ',
                            'ˤƼʥ˞à£ӛĆʉʼïƼȊЄǏȉǱ9ŁΉѕќϓјĭ˭ğtөӿ',
                            'ɛєǋŅĤŀӓ҅ϮF\x91Ϭƍϥ\x93¨ıΎƝƬԄүΘуғηƸӺĝƤ',
                            'ҚźϏΡ)(ЮSƊȝʣԣВˇȀĉȪģЋδfŚҍ҆ċϠ˥δ\x80ά',
                            'čǇЗΞxǒЭɇëʝϮҥmдѸίϷʆ¡ԧ˶ԋԄƲϣĒʿŠӾˠ',
                            'ϫ˹ϳĮĪƺʻċʸҴȅȔˊʓηĮ\x8eȀϵƕӞɀӪťҲӲǳˁʻӧ',
                            'IĨϷĂͿҭѯĬH˭ˋʋұхǲο˝b·ѦԗҶҽǵĄмɱ¬ǁř',
                            '²ŗɄǄ$´ßΨԅіЀCjȮˬřƼѴƹωр;śʯӥΡ˸҉ҧɮ',
                            'ǢϮеҼ\x81ÈήǝƛҸȩғȶɽɁӀѕV¤ʫvԗԬџțͿƆ˱ɤȪ',
                        ],
                },
                {
                    'action': '¡ԭ6ӞөčŴħȩąƣΛϫұÿк>ҏЕˌүÌɠѧÆѰŏȢʅΧ',
                    'resources': [
                            'έѷĽхȔǟˉȸʜÓƘøƙьĎ˸ôŖѮΝӃ\x82ҀϒԁΫăпԠг',
                            'ǌФ˫ƹ¾ԍʁc*ϼΧɯƶǜƷǐʉӱÐԅ˲¬őūЖǙǦ¸ӷȋ',
                            'ңŵѶȈЭ*ҐġΏΎӴ±3ГǺѬjĝ˓Ǿʭɥʠ#ъˉÉŧʖҗ',
                            '˪λČ¹Ď\u0382ѸПȃɔŁ½ʎ¤ԏǿȩ\u038déҮшƼʮӬ=ЌPѮȜ ',
                            'ȪˉƇöѕƖѣȪʌ6Ӑʧȏƫ҈ҏ6υƀώÔОӬѥȪċćʅψ',
                            'ΦδќИӽaʭʟȎ˫ɳűòƓ±ѿ˷Ŵǡu\x84īʩŀǌȽԗĈʑɅ',
                            'Ĝ\x8eƪ\x8dŎ^ɵӆΗӢ×ĩяѥԥƱˀȩҝȊԏƠѥ¹Ӕ\x82Ӎ~ищ',
                            'ͶșɰӾ\u0380ƇȘŐėϬˇŕһϨӸ͵ˉƦʸѿßś\x90ϑэŘ÷RϤћ',
                            'ψЫƪΪǷ\x81ÀԭȤ˸ŞʀŔƢє˫\x8b͵ŅˍͲ<ɽɕ¢ԞhҚЫΤ',
                            '%ʟǇŠͷӊϽȿΕОԇċÂðѡĻ·͵ˇƘ\x9dȏʴ˜\x95ɴԭʘƦƇ',
                        ],
                },
                {
                    'action': '˜¸ηãѧғƹɵˣΓʍЪΝʫеclɚɣǚƢɺνȺGʥԐԐMξ',
                    'resources': [
                            'ˀҾξƞƫÔáĬɾæĂΧԀ˩ĘĽčʩŤɀʕĸiůкòǼͲIџ',
                            'ŻӴƑʿӖДÚƪĢãǳӾŏřөŬӫôˎӫĢ~°ϯĒʆБϢԫʆ',
                            'ʐȋƃцԆǴǏ҅ȄĜмƖɠӕɈϓҽ\x95',
                            'Ɠȹ¢\x9dYïТUŒǎҠ"ƌɃƱǺϞʳԘЕƼĆÐҫðƹрȚРӰ',
                            'ӓїʩΝǸǚϘЛÏϥҘӇˌpϒǛH\\юԢtʇӔuÿǯĿИɃņ',
                            'ҬėĿј˚Ѹӗ$+ĴȼʈѱƐԐ@ĕɖѱe6ʍOŖЪЛχЈɃƂ',
                            'ʥȉɏƨβеǁŽċԀʥºÌʯPǒďȴϠňȜɏЁȋpʳΒѧƚǳ',
                            'вÄˣ҆ɹĬŉѭΖʰ\u03a2ĵİÌƋĳōϣûňžɥϬÂʥÉǒԤ\xa0ɪ',
                            'ϳȻƮҀ#ƑɨԉЀϊýɫҲԌLѨɏͺpŴǍ\x95ƌϒƪɊϪÐӠû',
                            'Ŧ)ϝѩǷͳƭɂʓӏ(˯ӹ¿ʨũωԑ\x9aȻÈҨːї˙ʤҝѴ\x99ӷ',
                        ],
                },
                {
                    'action': 'đИ<<ϫƸKԅр´ɠȫɚĉӶŴчӻĨж˧ÖȪĺѳϤήԐԜэ',
                    'resources': [
                            'ЗzшЋɬɹάȴ҇з-ͻǢпůΫфǅàѥżɻ·О҅ˠЊȝǀπ',
                            'ӛәǯĹ\x8eϙƶěѷɣʩϺRҲƗɵʎ˂ϖȚ\x9fƣЈĄΫ҄ÀӮϘȆ',
                            'ˡȘŖϲɿˈʈњ®ǏԈӯŗȔΆˌƵΛÇňРċȋӰӕѢ˺ˉɎŏ',
                            'ЄʢԉȩԗƱҤйԟ҂ԗυҬ!ʻіҢɱȘԂƦ\u03a2,ʍӄ)ȜǳӀǱ',
                            '\x84˄©ҟȨĲƁnѲб\u0383ȸцЕԂΩȚ6ϏĀĉΟͼ@Ѻ˥Ǫų*Ӂ',
                            '˚ӣˌάʒӯɋ˩вĖϴπǿɨđԙɼҰ\x85ϭˮ\u0383ʙбҼá9Ϡҵɉ',
                            'ÆY½ʼҧȀϢМɠʮԙʸѲѲȚɻǋiЁƠӒӸZ²МæǈĲς͵',
                            'ъ¥İӼÉƓӵ.ƍϣҷЯԀԊ%Њ˅·ŰӫŲİҌDȦԟǸƖζѾ',
                            'ШǺƚыȮĠdÑǛЁΙĬԪěŮΗĝԓ˘ȟ\x97ΦȪʊƞŸɡɗǬǧ',
                            'ʊҬɏvʙӳǶÿԧȘĝЗҩ\x9eӀƐЫƭȲ˞řƩЬ\x90ʫËkԁÔӮ',
                        ],
                },
                {
                    'action': 'ҒËϗ\x94йǩɤӳϑȼӰİӺїѹ\x9cɁӔȞǉ҈Ҙ¼ͺɞҼɊǌѮʮ',
                    'resources': [
                            'ưWùŀСҖӝҰƕγӤ^Ğʑϊʽӆ5½Ǉɲɫγҁɴfƍ|0ć',
                            'ӀҥѷԡėÞƦŽʇŷʉ˳ɑƖȦŷ¢ĈŻƏđƇÿLɜɆʬӟDɟ',
                            'ΗŢ¸ʂ£ŕԛԠΫ˂Zƛ¿òѯýӴŨǅԧďӼ҇ԋǬŰȰö\x83ʉ',
                            'Ţǖŵѧ³^õѝ˪ҘˊĂ\x8aЦç˪Шǔ2ȹӴӚнχŚȗ2ԥqƬ',
                            'ŒϘҠŏҟҌŪҚ,˦И+ҘԓєΤżЁ҇\x92Ҫɪ\x96Ĳѽ˹ΖÜaǵ',
                            'ǍӎbҦӡŘŉ5ұŜҀшАӅѤEÝơӨƽͽӡĊrǫpġͺ1Ø',
                            'ȊϳǣԬˇԍϋϑЖӺƻÌЖҢжЩξүĝ÷ӿȸģ\x7fªŽϗˤǆԬ',
                            'ƞɓϓΥǍѳɿ˸tGқOəɛ×ʽtÁͽƑӷΪУĀ\\ȝ8ɇȣΓ',
                            'ǝ΅ЈъɈҘĻ˵ΚʣŋϳћЫ\x98˝ΊǝҎ\x8eɝç^ğưˢ҄Ŷǹʉ',
                            '\x9bƬŅ\u038b$Ƈ\x92ӉϵȺϦϘуȀȳIʿʳÄŸĒʮϞ>ţϧЭƀ˙τ',
                        ],
                },
                {
                    'action': 'ɻʏϽğ=Ԉ¬Ů;ʼFɅÃʿӜȝɺκǥňҤԄȶǗƘɓðƙҜ҄',
                    'resources': [
                            '϶ŉ˽ӡϱȃ«æÕϮə¸і˃ӔǓΨƾvҜǡñvз\xad1ʾ\u0380ɦÂ',
                            'ǜ\u0380ʓ¢˶ʔҼѺȂŉǍ`ÉǘrʹƠȟȺĩ˷jΫ?ZʍɥԖԀӈ',
                            'ōтѐϝ͵ʏFˉΫŮ҂¸ŚƸDҨ)ɳϦϒŕƣƀҜλύӌҌíԉ',
                            'ʗҩǒƒȼԦҘɴƠҕҡÀǌƴҸʥǾВƺòɰǚúќ\x80)cˠӵś',
                            '+ФǙŭ\xadσӒ\u0379ѷ\x97ӺȞϠͺÛϙѭɊƯґ*ԃԞʱɃƠԄ0ѫе',
                            '҅Ңҥ\x9cΐŁТɰơǠįȕӿΛԁԈ$ϿΡ˘ҐŬÃҰ\x9aÔʘĒĢĚ',
                            'ɆΤҡɝ\x94üΟ˪ԢĢðϼΜӝŠŻàĺѲФθŭ\x98ŉ˴ϜԎéð·',
                            'ɱ\x7fνͳӏ\x84ϢÄʢĳĨ\x9eöɿGΥҫϧʫʯġ^´ņΪǵњgņǎ',
                            'Ӆу\x95ϸċmьɂЪƹӯξЖӜÀǺϷΰ˟ȖΣӖƢŌõ©PϰΔѬ',
                            'ʃ\x9eʯπ˧\u0380ɂǶȟ_ҬѰƯOɨƢ҆ͻ¥ȠΘҥȧŠƕȨѝѻɼҡ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ǧφχ',

            'version': [
                -8374858227358401632,
                -2441749571449650105,
                -7854352259230172049,
            ],

            'location': [
                'l',
            ],

            'runtime': 'Ƕ',

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
            'name': '1ʑӲ\x7fԣY˔ԧτӨӮŪn{Ԯ§þûԎˇɠɸęѥÔōûԘÔԐ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǯȥʘ',

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
            '$': 'KĀίΨvҪßϛ\x9eäɛҁѵāӯϷ=Ԝˉ\x96ˣΩ©\x91ѺĴ˝ȱƄȑ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2062813794785815810,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 220635.61228770157,
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
            '$': '20210909:200452.230615:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ȧѺ¬¹ӫŐ/ɲƿ\\϶˺ɝГʆΝίΟӽɎÅǻOхʡτʑԠĬƨ',
                'άІνѻĝƮÜ˻¾ϱӨκӄ=ˮǆɂλЧ˪ҧҡΉũË\x8cÁʤǷË',
                'ĒѬƆίҷэӕЧ»ňȯвǽԪґʮӈɈлΟċ˗Î˥ϋʂΏˁӊǕ',
                '҅ɿ7Ȼ×ɚŏĖƚФAүυλҸɘjįʱѷзίȂƎԙȭˋώƭ˒',
                "ЮӣǱİхʴɃӹʸԡâ'ǅԡɿ\\ҮȷġɤјйҸҰ\x94ŗöǑǓɛ",
                '˸ΕƋϵ\x95ºŗǬȤ×ӠԞBΝĞԟ\x8bŝţ3*ԍ¢Ƞ˓ǎԒȚȆʞ',
                'ɑ˚Ԍϟɒø5ȫôçћɇЛLӗnđѻʀ˂ӻŘӈaƄa˶ɦİà',
                'Ҝ˩ǤȠԙɢˑÍSϾÉNŗӡѢўɱνƑʳэԮǇȭӴzɘѓӿƿ',
                'ˡɋĹǁkͲǤʷ¦Ӈ˂ϊǿт®Ú«ͺƑZɭԆØəJǤǷъɘŹ',
                '\x80ѸěƩ\u0379ҵǟǂƻ\u0378FҝԘ˴˕âGʧѻ˴\x83ѫɏʖ\x9fӈɻԣHΫ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                651206840642707067,
                -6209808478783350848,
                5225041436898106598,
                8779327421421563764,
                -6704466633977386203,
                2756707879119032661,
                -7185806013003941188,
                4026192554171894236,
                -6056223489699852909,
                -5982312049926193875,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                342374.3304017443,
                -73749.08356713787,
                96676.85111483236,
                153265.58953649458,
                471562.5537345464,
                669518.1647182917,
                -88883.79256524639,
                885169.6917395119,
                256086.09648279735,
                997718.2665936719,
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
                False,
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
                '20210909:200453.175015:+0000',
                '20210909:200453.195914:+0000',
                '20210909:200453.212753:+0000',
                '20210909:200453.229682:+0000',
                '20210909:200453.248876:+0000',
                '20210909:200453.266795:+0000',
                '20210909:200453.285441:+0000',
                '20210909:200453.303872:+0000',
                '20210909:200453.321324:+0000',
                '20210909:200453.337795:+0000',
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
            'name': 'śĎҏ',
            'value': {
                '^': 'int_list',
                '$': [
                    847120247417644148,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɓ',

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
            'catalog': 'ҨɱѪҖͰϴ˶ŎÞЊ\x96ƁƲư(ƓƿŦҰë˹ΜĕɇǳҊӁƘӖɈ',
            'message': 'ʠƝ\x86^ŵ|ʵ\x98кœЇ}ʐеîȬпȏčӉ˕ăeʗǴб°ˈҏ˗',
            'arguments': [
                {
                    'name': 'ΉΣԙԪϺŜă˪ΔԗњѶĞŎԉΓкǚ¡Śїư\x92Ƨ\x9aΪf҇#Ӡ',
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
                                        False,
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ùƪƛ.Uзƫ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ԉϻ҇ҥǒuŋˑèӱ΄Ԡөϳ',
                    'value': {
                            '^': 'float',
                            '$': 531111.316957489,
                        },
                },
                {
                    'name': 'ʅď',
                    'value': {
                            '^': 'int',
                            '$': 213470821342222905,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ʢȇ',

            'message': 'U',

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
            'identifier': 'ζ.ǾȚѷŝӗαԂȣǎǺӹΙѯŌр-ǜgјŷҮÐȷƳӥŰůÒ',
            'categories': [
                'invalid-user-action',
                'file',
                'access-restriction',
                'invalid-user-action',
                'configuration',
                'configuration',
                'file',
                'invalid-user-action',
                'network',
                'network',
            ],
            'source': 'ŎώìƮί˘ʻϛћǺȰŻ˜ѳĕĊŹȏд0ˮġӤƨԫҪƎĦĆη',
            'messages': [
                {
                    'catalog': 'ŧѻРԚgϽŽ*ǞæԠ˩ÕęäяˋʒȨɉҴȊԔ».ȻǁğɅƴ',
                    'message': 'ӛʫÉǚҢҾåˎ«ĆԟĬԔŌӨËƃϏљȀеҘŔүЉɚȀɥԢԞ',
                    'arguments': [
                            {
                                        'name': 'ԀļЮĺɒ˝',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            618186.0941304914,
                                                                            919600.4870051398,
                                                                            134857.21724429328,
                                                                            486160.39648250316,
                                                                            325766.79199579824,
                                                                            833831.4633259297,
                                                                            259490.4575051794,
                                                                            478544.4108040079,
                                                                            699653.3087804855,
                                                                            812975.1038702847,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʨǐʒԃиΈѿӅΝȝĔ6ѦͲɚȅԤsɣрє\u0378½',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -56396.81837081302,
                                                                            183951.37839626044,
                                                                            989684.5593406456,
                                                                            425134.6263026019,
                                                                            687669.2841092492,
                                                                            33626.94412231271,
                                                                            847331.6111633859,
                                                                            796005.9104930443,
                                                                            417850.1381747279,
                                                                            714073.8145136366,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƈȿϲɛƐѱǫ-ϩΓ\x87vђԒ΅ʛƾɟԇǯҾɈȀȦ1ǑӀӯƜҗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1400046520206826142,
                                                                            -7982486808906389935,
                                                                            -2746656034067838729,
                                                                            -4924002915696396524,
                                                                            -7899704436802694416,
                                                                            3596240717224210155,
                                                                            3530714202985013729,
                                                                            5440760265101347318,
                                                                            6784484330618850036,
                                                                            3195668281823323079,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѕýȅǓ%ϯĻˮҧɴʢɫĚҐʷƥЌəǕę\xadƋ\u0382·ˬȯӨɏ\x9bО',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 783046.1198573894,
                                                    },
                                    },
                            {
                                        'name': 'ɍзԖҠӊķĎϕüźͿΌDŋµԖ.Қʥ҅іθэÕӷԇԞίτɫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200434.808940:+0000',
                                                                            '20210909:200434.825994:+0000',
                                                                            '20210909:200434.842245:+0000',
                                                                            '20210909:200434.860336:+0000',
                                                                            '20210909:200434.877103:+0000',
                                                                            '20210909:200434.894354:+0000',
                                                                            '20210909:200434.918074:+0000',
                                                                            '20210909:200434.935934:+0000',
                                                                            '20210909:200434.953390:+0000',
                                                                            '20210909:200434.973983:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ы\x89БˍɫӶΧȬυΡôÎƣϒʚǒʊɓ<ʛӼÏČʅƄƅ˽ԙϤ\x80',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\u0379ùŚˇŗ\x95ƱėɼϚ͵КҩFƢӘҌýТţԇ±9ȃȐλɪƔȻԟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԛĕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'èТȵRϭмзːw<ŶϼɰȅǊҐӼʡʔѵͶʾΒЎ˘śƳрҚŦ',
                                                                            'ɀÚƦԢӲØǍ£ÖǳʥòҊ"ŚȄП·ўɋѓêȥӱɿɼӊіǌз',
                                                                            'ҮE˘ϭǩĿԉĊȑүƉ@ӟҡƸŝѱΪ\u0381ҥƸϫˆο˱ӇǮӴΧұ',
                                                                            'ԐӊЉŘȨŚҥʌԕнԝƁʙǷүʗƬϴϥЬžіϡŮɊõÈǆƨ;',
                                                                            'ΤȩХǓ\x98´ɷɵÛћƤɔϝȍgÈ\x85˚\u0378ҮʻŹi\x86_ЈŇÛЖҫ',
                                                                            'ýϦɖӳӸԠѰԬӄȫӡāҾɡƣ-бҞþĳΗΧТFɎӪĚԋ\x87ʔ',
                                                                            'ÁʯɱγlѮӀȫ˔ЉĀΦÛǴƩϺɣˉҿ&˗˩,ǵĘŧpɃӝ&',
                                                                            'ѳѕѾΠĚòаǶЍȊșӠԜҺƵñʅΑ˗ÈʯԖĒØŶðΆӪЏӤ',
                                                                            'ЭәԪ½ъ·ʑɡˆӂʪʸӌȤ\x7fЈŎ±Ԇɜ"Ł\x92ÃΖǦ9Αϟ΄',
                                                                            'ч҉Ҋŋ҇Ŝ;ƨʯΡ˰ȴӐЍɇ˅ʧ҃ɉҊœǀМɐîtΤ\x9aԬώ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǰƣŧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'mϾпПԕõsê',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѴԡүѮћƯϛеɍϼƒâχѺaЏĞǯнáǀ\x84ĂhɨςŞĘʾʮ',
                                                                            '\u038bʁ˟ˈ\x9bѕɴǲĩjʩĮĘɉĠяŉɌӾ\xa0!ÑƊӺɏʿȘŨ³V',
                                                                            'ð¥НϦɮɅ0ǓѵɆʲҏϬʈԌȝăíƋȂЫǴťҴ˨ʊǥп;Û',
                                                                            'Иӥ·һȐl˦ÙЀϺōʱʬĈ>ŢŻϷJ\x83΅ËɂɖȠьƌΝσÔ',
                                                                            'ʺ¶ĮơǋľұřɛЈȿНŬŢŐ=ˢŸ\x97ΐҋӋȣǨϫ¾ӫȯŎf',
                                                                            'WѦʘŅǦԚĥʅ zĸПҳɕĵИǀǉġˀшʬћφιɫȾɇt\\',
                                                                            '\x91cȸεΝʷĀ:ƋÂĩCқѴƃϮȦ}ЍыŚ+ʠûTҩϢ˩ҭŘ',
                                                                            'ǲ\u038dǱϿġϤЪđêĈĢƭΆԏҀȐɢƴ҈ĔŶhʲŗ˗Œʾ/,æ',
                                                                            '΄ĪæəΗӧVw}˨ѶϨτӿϫɁ¨ќŜќƄƋ҈КӾпeůѮȤ',
                                                                            '°|ЀÔøŬɒžӏłȜˡƐfқ8ό\x8bӳƌĹÛ]ϩȌŘńҗčԚ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ċ!Ϧȑ¯ϝʵ˗ӣЦ˙вәĄ:Ѯϱ×ĭ$ɀˏÑİЏ˙ɼӵ˻w',
                    'message': 'ϵӌĥӌηӥҤĥ҈BԜɇƖаƿ˳ǴбǫŪŨƯȽʆʱҽāŜɃѧ',
                    'arguments': [
                            {
                                        'name': 'ȼ\u0382чǛˆё˔αʺYȖΧǚʷʮԕԦƬǙťΠԁΰΞԗԒ˰äj»',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -24413.71342383772,
                                                                            780482.6959617233,
                                                                            385637.7992920745,
                                                                            -45393.82485338185,
                                                                            863431.8383735141,
                                                                            606763.2428991756,
                                                                            603102.7905252897,
                                                                            203364.93345683592,
                                                                            851264.9825433743,
                                                                            825714.196408775,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʜɭһʜМ˨ӸƞƧԎԎѯŦ˾ʞʽ˦ŻƵɦҢ$ΕoαĻǐ˳Ϳ\x8c',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            469419.54160921904,
                                                                            242926.93338301836,
                                                                            -71611.46865574164,
                                                                            58714.84873239955,
                                                                            536661.0058780046,
                                                                            201694.93262169277,
                                                                            20835.491926798713,
                                                                            503174.8045811973,
                                                                            357527.3817944714,
                                                                            -6542.950532308416,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϣӥώ˗ĜŒîЈ¯ɉҏɮƶÞ¬ʓϗɴ0ŏ!ӚȜ\x7fј¾ǌϯˏ\u0378',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200436.374422:+0000',
                                                                            '20210909:200436.390885:+0000',
                                                                            '20210909:200436.407728:+0000',
                                                                            '20210909:200436.424056:+0000',
                                                                            '20210909:200436.445062:+0000',
                                                                            '20210909:200436.472501:+0000',
                                                                            '20210909:200436.493552:+0000',
                                                                            '20210909:200436.513972:+0000',
                                                                            '20210909:200436.537560:+0000',
                                                                            '20210909:200436.554971:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȩ˅ʵϗ\x91Jɩú',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2915870242409871960,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'µδ\x8cҟ²!ŧӄÙŗ¶ѴΎ҈',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǼyƑԀƺǽʹΠү\x90LÎˡưʵœϨɇϓ\x92āϨÍʠ¤ǹXԨŕċ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 238163.573690567,
                                                    },
                                    },
                            {
                                        'name': 'ʸӴΩӇͽƨˮȝҪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            255243.72437729937,
                                                                            725037.6625812746,
                                                                            545013.2400292911,
                                                                            363128.990243731,
                                                                            404667.9124143629,
                                                                            100910.3851651832,
                                                                            45388.35827822119,
                                                                            662732.6610445037,
                                                                            158572.5004558712,
                                                                            73378.84136759496,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЛǒӯxҋȿQ˂˕',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200437.136793:+0000',
                                                                            '20210909:200437.153322:+0000',
                                                                            '20210909:200437.171022:+0000',
                                                                            '20210909:200437.188626:+0000',
                                                                            '20210909:200437.206864:+0000',
                                                                            '20210909:200437.224062:+0000',
                                                                            '20210909:200437.240800:+0000',
                                                                            '20210909:200437.257417:+0000',
                                                                            '20210909:200437.274341:+0000',
                                                                            '20210909:200437.292917:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'φÔϺìÇcѴΛѪ\x9eʗα',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8285170074693230662,
                                                                            -4168104919161555293,
                                                                            -969064324950841911,
                                                                            -6390816314652749375,
                                                                            -1812700645924179806,
                                                                            7541398841940426874,
                                                                            -2081920586655701442,
                                                                            389459975034851342,
                                                                            -5035659738547913010,
                                                                            2574693113903263636,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɅċͿˆÞƥħ0\x85ыϵϤǌμ<ЩѿЃĵ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                        ],
                },
                {
                    'catalog': 'ĄӥLшȴӧDƪɷpɞƧ\x9e\x8bя\u0380тӂ"Цμ˂ŦԪUȗ\u038bӿўƝ',
                    'message': '˟ʦΗ˒ӠτӍʋҲ"ťLҸŰтѻ\x98\u0382˽\x9cŉ¼ǯȖǷȣ˓\x9dǭӽ',
                    'arguments': [
                            {
                                        'name': 'ˊÇŋǄΉɔӶүϧχňԪϴªӢҍЖӮ˴ю\x89ǱÖhɺγ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            402904.7189961407,
                                                                            949888.1557650722,
                                                                            759231.7019977425,
                                                                            131085.22359912196,
                                                                            -13320.111733150668,
                                                                            320763.0520974657,
                                                                            489298.2231735422,
                                                                            579771.1983536385,
                                                                            460652.73095740064,
                                                                            57314.01249852989,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÕʏӖ·ˉȁʍρɝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6275714001138385408,
                                                                            9021724751365957991,
                                                                            3935247685792606696,
                                                                            4456849400301756603,
                                                                            -1094590068591643934,
                                                                            -1601229396945099329,
                                                                            -8515439377040523199,
                                                                            4493969551583069622,
                                                                            -2428519727131289799,
                                                                            -8065947463165219763,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƒ˛qYм\u0378ѲЏÖŪǷűЕоϯѱέҡАԂtϽϸȖЅȠZӺɨƔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ǐňȗ¤#ԕŧԟ×ɎˤӐͿſˁáœǭęǝʲԓËŋјҝʚμȦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Þɖļ¬ΉʦȽ{ӏ¶åԩɾłϮʍ҄ȹŬ\x89ҶЎóĂΗЌǧ\x8e\xadǖ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            520081759633403405,
                                                                            -3432074825655649896,
                                                                            -4567985824922676637,
                                                                            2516423688618961902,
                                                                            1696431046364254108,
                                                                            4872068183919052459,
                                                                            6437644939632248409,
                                                                            2710870568118540366,
                                                                            -1622628941331863904,
                                                                            -4170899211711812508,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038dӦԙҶҏqԁӐɄǔĔ8˛¸ӌţ˦ӟТʉѠϱĶϿѳƹĔŋSȨ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            977808.6047854198,
                                                                            620456.2286214351,
                                                                            33428.068104315986,
                                                                            263138.9468016903,
                                                                            636439.8362395877,
                                                                            422202.30805807846,
                                                                            262977.1969059881,
                                                                            803367.3001400906,
                                                                            439439.03618680465,
                                                                            334352.4127697007,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '×ьĘт²ӌlǎŪşбɗȻӎӴɞҜÆ~Ӑʀȹɜ\x85ǷѠΏȢʞȴ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ĳș*˪άŨȝͼˌʉҩȔȰɃĶQŇύґўF´-&ЕvԘԒDȿ',
                                                    },
                                    },
                            {
                                        'name': 'ҦίʓɠʚНԚƖŃԛԝĀ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȬμӵĀźŒӱĳΘɼƶӎҴԘўψńšpd¶ĈʌΚӌćпϩκρ',
                                                    },
                                    },
                            {
                                        'name': 'íӱ\u0380ΚɖʆқȰ&Ɖ˨öϯɅ¤җưԂШԦƲōǅӼʈԖƄμԇ+',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȎЕƪзƲΦȦϡѐZȧϱțɖS҇ϼˑӎĮńХͰϓŎȱĸϢďŭ',
                                                    },
                                    },
                            {
                                        'name': 'ΥŅзǶȕ1ėϚ¦ĦŗέɚΘιӢӆшǏȠʱΨ:ηҁÇϢ±Iλ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200439.514682:+0000',
                                                                            '20210909:200439.531364:+0000',
                                                                            '20210909:200439.549270:+0000',
                                                                            '20210909:200439.573805:+0000',
                                                                            '20210909:200439.591721:+0000',
                                                                            '20210909:200439.611626:+0000',
                                                                            '20210909:200439.628972:+0000',
                                                                            '20210909:200439.646027:+0000',
                                                                            '20210909:200439.665827:+0000',
                                                                            '20210909:200439.685000:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƓЃ\u038bѴͶʸĕӀ˹ɇ҄ѐϚΣůĖіϞѣȨʷŇ\u0381ΌĉǄȝΑϫe',
                    'message': 'Җɸ¸£\u0382\x88kǔ˗ɇԈt\x8d\x94Ԡ˚ѸƊűӃȳɉСƖԁȶƱˋӧ¨',
                    'arguments': [
                            {
                                        'name': 'ǇƎҺɧšƴɂӈмӬƣĠǰ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200439.855723:+0000',
                                                                            '20210909:200439.872517:+0000',
                                                                            '20210909:200439.890683:+0000',
                                                                            '20210909:200439.908326:+0000',
                                                                            '20210909:200439.930103:+0000',
                                                                            '20210909:200439.947435:+0000',
                                                                            '20210909:200439.964256:+0000',
                                                                            '20210909:200439.982322:+0000',
                                                                            '20210909:200439.999597:+0000',
                                                                            '20210909:200440.020580:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȲɅū¨Ƅ\u0382òԈӭŊӝʓe',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'чɁ˵ɇцĪӅü°MĠέȵҡēԇԛŚʯ!ӼFЦƜǚĊёκԄÓ',
                                                    },
                                    },
                            {
                                        'name': 'гЖѸkÜ,ʆĉˈѽЯōҜΥ½њΛӾaŇ%ɀҏÉʹŧ˨ɥϿ˽',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            625439.680169118,
                                                                            908895.7908975801,
                                                                            608800.3441564516,
                                                                            430153.2279821002,
                                                                            2408.233007179326,
                                                                            907800.9043613827,
                                                                            -29721.89919624936,
                                                                            833590.0967212673,
                                                                            842116.8984094497,
                                                                            623427.0091951397,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɫƵԇ˱ьČϴмӹǨ±ԓя,ԑɟʣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4148949194976517097,
                                                    },
                                    },
                            {
                                        'name': 'ЃĕΫ˪ѨȡԖϞ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'Ƕɸ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Дí˟ғɊGʿЪнĪƞ\xa03ҬДŻß',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǢƌÁҽȬɟȌƏŗˌ\x9fɸÕʎlƟϹǥæӾԘφϼ=ПΑȉ£҇ʎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'фӗȦƍΣȴҮIɎϘg',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200441.206149:+0000',
                                                    },
                                    },
                            {
                                        'name': 'юѷǛĹɍɞ\x959ӰύϽƽРЄΛȐŴ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '5ʾĻ˳:ȇÖ`ĞѫŴʟ]Ӛʺ˔јșӫИãʢҠǜЯȌ\x90ȑӭΒ',
                                                                            'ƑԔӳЁ˯ºĹ\u0379ȋYҸǙĪtdǊyʴӌȕ\x86Ȳ?ǷÑËĉѠpǔ',
                                                                            'ƣϽĬúǨó9ȦIУȐÜϿ˞γ>ԇҪǰƩưϋ˯Ƭ<·ǙȈϥɌ',
                                                                            'ӊŮɻƗɫR˥@Ѥˌоӧɯƣūɋϓ²ʵÁƄĿЋÐӨҚmєϬӴ',
                                                                            'ԂΏѲ)æ;ʜƖȕϷ\x88ɿӇеƟƣªɱ;ȒʼЎͿƴͺɻԏӪɼǽ',
                                                                            'Ϝ#ƞѩÌχҮȓҐĿӀ\x81ɳ½7ƤԏɀќɊȍŒǊw\x90Ȥ\u038dȽ˥Ĵ',
                                                                            'ΈɃˌƘȤĊԈOˇѦõƛѹћ#ǨĥИ˦ǳŔȁԜĦϘϦŴΧ\u038dɉ',
                                                                            'ԛ˩ūɑʤӧбȓǫк˘ϖҶϟЍɺðͼɲɛǃȼƛɣɡįдɅěʻ',
                                                                            "iƒźǮЯńҡӉ\x8bÉԓʹɟŤԣŕСŽ˸Ϫ»˘'ДˇĬ͵кԩ-",
                                                                            "ŢҿʹļеϹŪƍҁϟγɨӘyɔ\u0379GʜʴƑ\u0382ǟȾ'oȞØƈÓȀ",
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '2ϱ˭dà4FȻǞųeӃÀŜΫƦǛŘĮӍƹˉ\x8fθҢŐѦİЏƽ',
                    'message': 'ӵȹϨŜčɴ´ƿϔÂeҗԀ¿ʋИɬƥυ9åˁо\x8bǫѢ\x94Óӧϑ',
                    'arguments': [
                            {
                                        'name': 'ѝҎίȁϊҞ˻ʋRӉΰǭǁӍÇЁТ\x91',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˋΏЩʆŀǶřɉήΞ\x87Ȏ˹{©ÐϤƷҐˑΊrϛЇĻӵʹΩģœ',
                                                    },
                                    },
                            {
                                        'name': '˞žҜΗӰ\x89\x84',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'βϨβņπӮγΣɶ¢ϽӜґ˜ȶЬnɵʂǹ-Ѕ\u0382ñӈѕҷjθϰ',
                                                    },
                                    },
                            {
                                        'name': '\x85mǱҐʒʪΛЧǅњˑǖҔ%ǜΎ¼´ͺϛΠɱ\x9bƝďѣʉ˪ʨѣ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200441.770711:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȸшƻ\u0383ˤ\\ε\x92ʙГͽȪϹԃϯËÅ«˧ȃϺЛǈɠԮϲƃɆÏǟ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            495086.3212450779,
                                                                            492197.6269878383,
                                                                            812564.7317916931,
                                                                            249707.33251202578,
                                                                            381770.30127070047,
                                                                            540112.5630805673,
                                                                            812451.5366645925,
                                                                            995105.2865633245,
                                                                            202407.60917735327,
                                                                            769399.5803595186,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϮĠԙЁʻƼξ˳ŢͲ˺қӏ{ģƁƗĴӐɘȉҥӷ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 403914.598961286,
                                                    },
                                    },
                            {
                                        'name': 'Ϩ˭ё˹ƝʸΠ˹˘ÍԓҾɐϨ£ƲĪӖū˜',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƈʁU\x7f\x8aȄĴӿñłӎΆȮΡŇԞkǇƂƹϨȠʅ˧ƐѓљîJǢ',
                                                    },
                                    },
                            {
                                        'name': 'ԙ˚ʶА,њЙʵӠVāîλ¤œɄ\u0379Ơϔċ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 293228.8461627524,
                                                    },
                                    },
                            {
                                        'name': 'ѥʣψĬÏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 835377.0280296907,
                                                    },
                                    },
                            {
                                        'name': 'á˟ǺЋЃӺƅ*оΏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ҏ\x99ˁłRʼȗÔԩˮʆѼɹɭƶtȠϑћϛGƧ˂ÅƮԔȟ˧ԔГ',
                                                                            'ƈҳǮ7җϱЈъǯͳɜяφɼΕʮ£\x8dʄĤÕҳ@ŬưѵxӎӸÒ',
                                                                            'ɛŰ\x9aҼӌʘЭϺćŬƤȞҠϘà\x9dƪ˗ƨԩYƳίˢәŉ˽Πҙʿ',
                                                                            'ЯԓËŕɬӯ΅ȩĪˊºϟĸĻ.φΡȘ_ѐ)҅ëʿ9ьĤƝü´',
                                                                            'Әɞȸʜàʺа\x9eǬǡͿȫӌʆĢÖųɟґßΏʨ%ƽс҇ʐɪǊќ',
                                                                            '\x80ǽѨҬ˃ŁÛńñ\\ӈÚΥ¯īΒǇʢÀŷӭʓýƭУą\x8fǍŷ_',
                                                                            '˕Dѫ˒ѹσ\u0378Ǎɛɔǘʄɍʦ(ÅҎƀǁςӬұ\x87Ҏʥ˥˹ƅˍù',
                                                                            'ǦŌΖ˧ҀãӂºʌˤɢŬɼéŪԂИҟθҖӢįӭêӔƫ\x8aʆƋȰ',
                                                                            'ͽҠɇxȥŢϰƟƣҷǩĿʣԩ\x83OɡȋͰΥƂſQëʨԬϷϏPȴ',
                                                                            'đԃ`ī\\ҌBǅǺiӅќԌ҂ôΰБ~ŤSÎǔԉǐ\x8aƘƷhòȀ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ċδҴȥ}ȅŐřͶʊøȶЊƯŋ\x8bаxĠ˻Ԇ\x80ęɫˇϬăӁíɭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            169360.4834016529,
                                                                            371311.54280761874,
                                                                            519028.0330307061,
                                                                            777800.5333308007,
                                                                            366900.36038372264,
                                                                            861436.5761938667,
                                                                            517193.39176291623,
                                                                            -82865.0164621203,
                                                                            689009.2808863549,
                                                                            223370.02378362766,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ťǨɠϼӜԥȱUϝƄŞӵǥěİτɭȸȒƕĤҖæΟϓӂМAÄЍ',
                    'message': 'һѷкž1ˡѲŝǟƲŶůϐȔȷǽɢѷӷł¨ʼŵΗώǿҮ:śќ',
                    'arguments': [
                            {
                                        'name': 'āŇmø˅ʫĦʀā',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6955173342996595695,
                                                                            7329320589030141116,
                                                                            1821974101178176479,
                                                                            -957386869757701217,
                                                                            9011362581064889908,
                                                                            -402763880596979382,
                                                                            -5773234037927837470,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѹóӎӃ\x92Ƹ\x7fκˍƹ\x86ŸсɥǑѐÝςӺƃҮ\x85ɌɆăĄҵƲŐщ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǶÞҜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200443.407304:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʷŋȸǶŦ/ѕªJɕʯČМǟ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȅʿͺǾǋʍʂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʴǱҲŹĩʟ˛¹ìʅȔʲȾӏƧ˱ʌΩ\u0379ҫþїΔF\x8bcӮÕȉǾ',
                                                                            'ЋȘԥAŦԢfϹˤоŪìŭȹĻʑήЫϻҲ˚ɷϟϫɄȝ\x91óјĜ',
                                                                            'ƒͺɬԁ³ЋƚǣƏϵ¢ј¨¶ԀϰӺ˹ϖӄǜӮƕȭӲΠԌЁԓЩ',
                                                                            'ʥҹԄWӝƁǠȳΙΐy˒©QWʄϥʓЗӘÖǮɎҜňϞŌË\u0380Ӆ',
                                                                            'Бԡ\x89дɤҪȣēůˀӊ´ŖɡѳJiҐŋЄʾљȎȉѭɔΌóԣ¦',
                                                                            'мӚ«ӡԗю˱ɶЁhÒ«ʯӲӚѸѼԂΥң˨ӵŠŔ˾κѯʹӑ˽',
                                                                            'ǁĺǃłŧǲɈΓƽˌɵςϏ-ʶȳɈƮ\x7fѡļČЧȭӔȿҠБϙС',
                                                                            'ǐϗαΗǈŧʛϞŪ°қŤǼȕaÀ˂șέȭ%ƃ<ɉU\x98ϴąΥѼ',
                                                                            'ІȓûÃĖǚϡɛε˝Ƒ\xadwŬƈßàĽķӃɊԩˮ_ʐɆсїδс',
                                                                            '\x92ŪʤҙӓɌϟ\x8eΟИúƧҽԆӜҭāŠȍԍϖŀ=ϟҨҤ˨ϺȌʐ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'iРƘßҭȹф$¨ɣƇʼƫ\x9fтп',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʢWҮɝĆүĝ\x98¤ȜΟɎęҘÅРʣø¯ǃǅńZ˭ȡƵƺάĤѣ',
                                                    },
                                    },
                            {
                                        'name': 'ЕϻưЖЬѷ.ҩŇǸҼϧԩ3ԠΠĸȜɇʛс˃Ĉӧ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'ÅƯȼ҉и˷҈Ҁš\x9a1гҋ¸ΊǇmόϮɅԪEϞÝ\x95ΏƱŉѯμ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 324818.06629787275,
                                                    },
                                    },
                            {
                                        'name': 'ʣ҆\\\xadȸː˽sъɘƯʑүɕѱԪӿԗғәŘΚөȶĹĒ\x8eʨѲΚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '§ҤҔÔƯ\x98ÇíжʳºѫѥGʀÇϴΎӉøƮdҜӱӑȝҺȪȗ¤',
                                                                            'ƶ=ƛʇȶНȋ{FɓΨʄEӀţҚÌȐӾ˨ôрpԭɝŜҍӛ·ĸ',
                                                                            'ĸˮM˳ІҙĭχƮЙԐБ\x87˳ΒïϯϤwōҦĆд¯ԏþ/ǀҠύ',
                                                                            'ƎkӇԄϧӺƙĲѪТԭ҃ϨĈǃϳŹ%ѐ΅ƓñҴƾМɦͷˤƂʋ',
                                                                            'ʬ˕ǥǽ\x82ĜȓϚƥΜȫ\u0380üѨɀɆƖћNƨҢȼŁčӛʼӏΐ˳Ȕ',
                                                                            'S\x94ԉ½ʵ\x99jǯgϳǊŻҝϧ˲Ԉ\x7fǀʩ>ӧÅШϬħ\x8aԈŴŢ\x8f',
                                                                            'Ǉû+ˉȞԓͽÁʩˊß\x99ǘΌĩ\x88ȻЮͿ\x98ϚӷŗьSƦф}Š˥',
                                                                            'ÊÄˋĳFǿŦ}ɬиҞκŕїZȾЙҟȅ=ȷɀťMԒьˈĘ˖&',
                                                                            'ƁʪůӯƾԗѰŽÏҶŊϕǧѹӻӧĽϢˑͱƆȀǙŹǄӭ"1êӇ',
                                                                            'œÇҜ˭Ŧʳȁ:o#úȄƌҝʒƁӫʹӮҌˈƀύɾϢʧɨ˷η\x9b',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϫ˅ǨҀүÐͰ\x82',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200444.755512:+0000',
                                                                            '20210909:200444.772001:+0000',
                                                                            '20210909:200444.792290:+0000',
                                                                            '20210909:200444.813189:+0000',
                                                                            '20210909:200444.831369:+0000',
                                                                            '20210909:200444.851391:+0000',
                                                                            '20210909:200444.868582:+0000',
                                                                            '20210909:200444.885139:+0000',
                                                                            '20210909:200444.906914:+0000',
                                                                            '20210909:200444.939312:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'źǜĬгԈƙѷƥÑɱйИЪȂкÐ҂ˉЮԑӉсύ>ϧǵ˻Ӄλǘ',
                    'message': '˔Ԫzˎ\\§ȽOæͲđǫĞѴϚÜӕƤʮԅϨCεЏƨϻҹϩwȂ',
                    'arguments': [
                            {
                                        'name': 'ϰȘˋҼȳǂ-Эќψˆ҈ԋЦшȀLηӛ\u0378\x8c҄ν4ϳ҅ϹI3˛',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ŬӈYӃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӁѲЩʭˇф\x9d\x94ѴĖ\u0382ˏĆʵĤùҷƎ\x9căь©ΕȺ>ÒLƗƯƔ',
                                                                            'ҋý҇ȘϡŉɩǣȧχӃҎȕ\u0378ЬŮèќÕɜŅˣϏ8/ʘɐΗ0Ô',
                                                                            'ʟϴőÁˌґԡѵìǌɁʫНµƦɘǥǅҕѭƿǖưϚЄɳԎ\x88ŋʧ',
                                                                            'ϯÀ$ǠȄǝԭԅǁԓːѯƯҲˋ#ͱǕөǷưƓÅǕԑȉbʇǷЍ',
                                                                            'ʟƼ˙ЩЀƱɀϦ\x8aóưƸϭԜáЏȾȃhèʟΑĽǥńӼѝӗȞŵ',
                                                                            'ɓ\x97\u038d3Ќƒª\u038dǖөɪǁѶĘ]ȷϔžхфӯVʨČЁȼʣҐˮˑ',
                                                                            'ӰГˊɲåξŎԠҗόʑʋÿț˪ϜŻșčǖ4ʛϻԡɹԚȺĖѺʃ',
                                                                            'Ͽǳwj\u0383ńɽ˥ʵAɖ;¶ə¾ǯ°äĐԦɢŴʉµşɝт¯þΐ',
                                                                            'ϑϞȅΖʎ\x91ͽʽҁʁȭƧīϽώƽʓΫZȢʐААӱ΄Щԃ\x7f\x8bќ',
                                                                            'ΏцҩРȀӈÎǌWԎ˅˔ŋСИŐȓӆΌϟBĠȂɹѝǖʛƗ9Ɩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѣƐɿϺϵƈˡɹ ԤʪxϮςƗÞΝѰ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200445.537042:+0000',
                                                                            '20210909:200445.574369:+0000',
                                                                            '20210909:200445.597200:+0000',
                                                                            '20210909:200445.651400:+0000',
                                                                            '20210909:200445.714169:+0000',
                                                                            '20210909:200445.751064:+0000',
                                                                            '20210909:200445.801812:+0000',
                                                                            '20210909:200445.846830:+0000',
                                                                            '20210909:200445.877096:+0000',
                                                                            '20210909:200445.897129:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˊʤ@RζΫȑnŕȓũÀӕȿϒёмȇƲ·ҋʠ\x85Ã\x9bгҾHҗá',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԗҾġͳȖ[e)Αĩ˃ӁvҸĴǧÂˌϘΡɤɒҪʷưҤ£ҕ˸:',
                                                    },
                                    },
                            {
                                        'name': 'ͺƅҧǯЖЮηȯ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2041755946814042548,
                                                                            -7068914763509833230,
                                                                            -7070316241868650812,
                                                                            -2719890111108037352,
                                                                            4083811900021610544,
                                                                            -7472516325606940133,
                                                                            6744646842151971927,
                                                                            -4185349368814623603,
                                                                            6623348816712025593,
                                                                            -3023785537892924899,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ë\x88ˎ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5957183817220508028,
                                                                            818130518410422405,
                                                                            667918422952450389,
                                                                            -5849502216196826016,
                                                                            3403238761358790539,
                                                                            -7599206807906514283,
                                                                            8052565177737006519,
                                                                            890122601301258106,
                                                                            4126378924470709145,
                                                                            -2657704159457583845,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӓ;ǿɋϵȅÀӨҹҭJȌFVЦήŷʪϐēӝɻɾĨő[ʇИ˟˩',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200446.595368:+0000',
                                                                            '20210909:200446.614067:+0000',
                                                                            '20210909:200446.636391:+0000',
                                                                            '20210909:200446.654143:+0000',
                                                                            '20210909:200446.670203:+0000',
                                                                            '20210909:200446.687358:+0000',
                                                                            '20210909:200446.704319:+0000',
                                                                            '20210909:200446.720977:+0000',
                                                                            '20210909:200446.739089:+0000',
                                                                            '20210909:200446.756081:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʌѼůЙÔǻªĪĎƫ#ϡĻĦіrʜв',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200446.855436:+0000',
                                                                            '20210909:200446.875048:+0000',
                                                                            '20210909:200446.901786:+0000',
                                                                            '20210909:200446.935441:+0000',
                                                                            '20210909:200446.962839:+0000',
                                                                            '20210909:200446.990050:+0000',
                                                                            '20210909:200447.039504:+0000',
                                                                            '20210909:200447.071255:+0000',
                                                                            '20210909:200447.097015:+0000',
                                                                            '20210909:200447.125498:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĬǃɵmѕĲàԥĹƤƏхȡЧ҆ыʖïȉ<ЁƮҚƣҐѼЩǿӫԡ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            471781.46310731163,
                                                                            648806.4733195399,
                                                                            856911.3336707731,
                                                                            897499.3832643545,
                                                                            840151.0640930512,
                                                                            130140.01903741652,
                                                                            711308.8016196308,
                                                                            585321.952343217,
                                                                            566904.784523916,
                                                                            151604.02631375822,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϝLbȐƧɊVΩЊ½\x87\x95',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 493162.4685935078,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƉҾaԕƸÔʙɿсˉаҔŕο¿ĩɶÍĽӏԬœƩű\xadȥ=Τѓâ',
                    'message': 'э\x8dɥҥ¡¹¿Ř˪ͳ3Җ\x95МņиѩҔэǋɫϢɭѧγәШӤԊΕ',
                    'arguments': [
                            {
                                        'name': 'έŪòřѨ¥ʶ˃ˀӂŴт˭qɘŕԤмӨɦДɋĻ҅΄ǗMƟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4406733514834582001,
                                                                            -2575114830526692652,
                                                                            391022275247596619,
                                                                            2189302938324905930,
                                                                            7755767511791746950,
                                                                            -7474762899048300673,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȐΟVǵԪū¡ʦЭэÕΆǌƹцϷΟǮ¥üűǼdÈ\x8cʾȳԇɟȡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5306515448837596285,
                                                                            4755845501822263807,
                                                                            3101871680430492221,
                                                                            -2075353654891463048,
                                                                            81626853872766029,
                                                                            -3818091949835975722,
                                                                            1361424007896788596,
                                                                            6665193043232829157,
                                                                            5758838153089981353,
                                                                            2441998894521276142,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɚɰʈԍďǠȎÅϺϷȕПʮzƄƱˊȿƍȮŹΛ\x91δĶǚÀ¬Ǖȅ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3284521268487465366,
                                                                            2557589513892544351,
                                                                            -529190217199891595,
                                                                            -7984520487928080632,
                                                                            814606270361696143,
                                                                            6977788509852490897,
                                                                            5224067536254053741,
                                                                            355334056380777747,
                                                                            3841499295803279480,
                                                                            -6316541814588208961,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˂ǣ¸Ҹѳ\x9dӲԪΟŠɛɡҊȞєËΜɩϳӅӃӝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'їÂԉÿđĩΒʹƄвґɓЕɋȅȉ\x81óƕ;ҸЄУ\u03a2ϙЂČОьғ',
                                                    },
                                    },
                            {
                                        'name': 'Ԏ¾\x91ǔHӝԂάǿěϚȂ˄ɪÍƢØҺZĜŠɌ²¤7ċˉʞģЀ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'εҦ¼%ӄϿӣѲ˗¶ϻǖӛˆЇƪȖëʑӁД\u038b°ȿ<ӇЊíȡ\xa0',
                                                                            'Ԥ˺Čťȍ¸î£Ԥǌyʅ³\u0383ˡzҿԌ\x8fϾÊq\xadвǀ\x8eÂÏͼҙ',
                                                                            'ˈ\xadĉiǅÑŒ˙ȦʹǠͲȭ˫ɡ(ѶŪ\x88ŽΰЍҶˇƉƂщƁrɝ',
                                                                            'Ǟ½Ǵːçĵʈɤò˴ż÷¥ρrʅǝː"\x82ҚЖќϗ˜ЂǸrƶΦ',
                                                                            'ϫК¼ԥѮĊѷ\xa0ͷ\x98\x8fʒӒΨÆǇƧæīǫηȑиȉӔŐǐȓ\x9a\u0380',
                                                                            '@ʔČʆӔøéɌӉҨ҆§ŐɽϙƵȅВЦȁȔєԞсǄðŲʗ}Ы',
                                                                            'ӹň\x83θìӔϗȉȺɵɫɵЫȃСĬЙȩΰҦ\x81д˛ǙʝŕêƜЇ͵',
                                                                            'ͽαţʸΡϞҸȶǅ˄ғ§ҙїҊţΟ˲ҟ˘ÑǺǶΉʯϸȉȏǮв',
                                                                            'ɏĀϋͻ\x91JǔȷX˾ҒɫɖʲŁѼąѽϘ\x95ƠƼ˹ÖӢŭǞќӓƊ',
                                                                            'Ҿ×ͷǳķϢ\x85ԌņĖ4\x96Őχќ½ҍ˗ͰPZ\x97ǡϋɫѝ΅ò˰ɿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'з˛ĕѸÍǟȖǡȨ\x81ԟϝҜ\x9a϶±˹ђ҉˜Ύǉkэ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'nΰчϓϠķΠǲǿä˶ƧüԠϓԫǶ\x97ͼÈЖ\u0380Ȉǒ˸бґ¬ÚȈ',
                                                                            'ˢȔΓ˚{ēɝҕ\u03791Χʷ«ҁSÕΤΐǋǮԡEԝŐōpƦǴ',
                                                                            'hϝηªӥŏëӱßҍЦΒνǫï˚ԦŠϝ¸ϓƊwɏΤ3\u0379˖ΘƤ',
                                                                            '˖Ŷεўņάϧc(ėӰϹ˳ΒƚʏӛǤȚ÷ƳԥʻÏѐĐȢΖΣД',
                                                                            'VɕƣԕљԛȾŲƣ¿ɁŀЏ˽чʹė˱\x8fЯ҆ӂ\x9bǁӑÕԒɣɥу',
                                                                            'ѠʘҜ\x93ԙєϊĀԚƣd˪ΣϳǦÏɷԃгԟļ\x80ƴǄӄ΄ÑµͺЪ',
                                                                            'ƨńȠʹȺ\u0383\xadșϝҰɋȔĲԭ˙ëƕɓΫаʇV˯\x98ˤӎ˞Ʃ˫ʘ',
                                                                            '±ȽѬȏҪȕϬʙЙńЁʻŦҍԇѪ˜ʯԄϙѮčNÿԬ©ʱÑǔӹ',
                                                                            'ȈӢӞǨǯйʋҁǕΪǴҪǳJƙԜˊĶԠȭКҵŎѭǯφ\x8dПѲ\x8d',
                                                                            '/Ͳ\x8cU˺ɰĒƵзƘÔ5ʡӴˇЕɹϗŏΜʎӈ\x85ƹīϼˌǩѳʳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƘŐȁǰėǹWŀțȳʊĈÒƛ҈Ԙ\x8eǂеȎɚƻĖȗ·ɢƆӖƤÔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'мΓʊқ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2318072316624291047,
                                                                            -1828318150342853222,
                                                                            -8225743888416266979,
                                                                            -1191868986819339836,
                                                                            -7673015674602587228,
                                                                            6419558009887895110,
                                                                            894707506415643986,
                                                                            3340190700323386316,
                                                                            -3581251393528578279,
                                                                            -3334290465135070948,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ν',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǢƺԏИčÛǱһÿʟėçʰîɖҕĦƔҜ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԨŬΤʩϒҺǙεŊƥҰγԝʹЋōžԧǑƣϙЙUҿԒRϺӲņȼ',
                    'message': 'Ӥęū\u0383ɂӉј¿ǝɦ˳Ҏƅ`ȍιƱʴҡɤȢsш˔ǟ*ҼӊQƬ',
                    'arguments': [
                            {
                                        'name': 'ȢǂӲӦү',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200449.581356:+0000',
                                                    },
                                    },
                            {
                                        'name': 'В¬ԁó¿ϥʕӟҞ~Ù',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '÷\x8eˡ˞ʻ˂ǆӳŔ\x8cő°PΑІгȂɄƢ\x91úΌЭɆѣҶÂҚ˥ʱ',
                                                    },
                                    },
                            {
                                        'name': 'Űŝүľ¡Ӥě',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1303184841801755484,
                                                    },
                                    },
                            {
                                        'name': 'Ӟļƶ®ɘФ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200449.806251:+0000',
                                                                            '20210909:200449.822809:+0000',
                                                                            '20210909:200449.838412:+0000',
                                                                            '20210909:200449.855018:+0000',
                                                                            '20210909:200449.871273:+0000',
                                                                            '20210909:200449.887672:+0000',
                                                                            '20210909:200449.904154:+0000',
                                                                            '20210909:200449.920443:+0000',
                                                                            '20210909:200449.939948:+0000',
                                                                            '20210909:200449.959696:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĳ?ʟǏƈ˲Ĝŝ\x903ï\x91ʿƤԍϏŖӃØë˨ƍĴĨӗĔϨȽű¯',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 93041.78122591632,
                                                    },
                                    },
                            {
                                        'name': 'ƾ˞ɯT˓äЎrũʂӸĂ\u0380ʏÌϋǍѳǌ#ȹȃV¼ŸƖҞǍԔɽ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӲΔȳӨſԪκÛӨȫzͶ\u03a2qΎϠ\x85ǋοԄҞƑ˚ȇɊҬԢĒ]Ͳ',
                                                    },
                                    },
                            {
                                        'name': 'κ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200450.181101:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ψ҉ǋ\x8dËġΒˋǋʹ҇ęœ\x855ýǎћ˸',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200450.258496:+0000',
                                                                            '20210909:200450.276803:+0000',
                                                                            '20210909:200450.294026:+0000',
                                                                            '20210909:200450.311959:+0000',
                                                                            '20210909:200450.329885:+0000',
                                                                            '20210909:200450.346808:+0000',
                                                                            '20210909:200450.363982:+0000',
                                                                            '20210909:200450.381111:+0000',
                                                                            '20210909:200450.397061:+0000',
                                                                            '20210909:200450.414034:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ']ƭϠʭ˞ͺM˒Ăċ\x82¤ә×ΘѻǵɡԎʑfόƐѴѧĈrʦ\u0378ѭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200450.504952:+0000',
                                                                            '20210909:200450.522464:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĈΤӞ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӊ(ǹÛíýҢЛǯκұɵɲġɪŗ¼ʭԄǟÕÇϊīȘśƭ҄Ѷǔ',
                    'message': 'ӼґȷǀμɩŢńѽы΅äͷҝƚΈųнȀļƊЌ\\ŜũûǤӜʹɍ',
                    'arguments': [
                            {
                                        'name': 'ЬͷƘÜΣ\x83ƛ˺ǛȄͳёαĜŠ҆ǱӏɚEĩӇŢɰƫþѾ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 247084.10372249404,
                                                    },
                                    },
                            {
                                        'name': 'ʔҰɱ\x82ƎȄƇ6Ŧ\x9dȳϪҝƠϞͺŅҀɚʜɺŵяѠǫΎ@Ьʪν',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4970887841086233390,
                                                                            3350544724389189138,
                                                                            6599703301559567642,
                                                                            7072457791864282051,
                                                                            7435694531770765898,
                                                                            3362980192028205015,
                                                                            8727406429865857559,
                                                                            8240726180609871950,
                                                                            3833920122440079179,
                                                                            7709166646500079984,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɱƷȠéѯˢӠZϧΉɎǕ\x94ıȼҸ3îȭ]ΩҤ˛ӲɆЇӵʼҩɃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŷƱӭǷȆ\u03a2бԄǯàôӻȚʹÞҶˮύΩέɺқSĄɔӂЉƛуú',
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

            'identifier': '>ĢĹƼŘ',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': 'ɾҗ',
                    'message': 'ǔ',
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
            'name': 'ѸʠѲŢXʖřM',
            'error': {
                'identifier': 'ϪȑʯƢæłŘɼ0ʧȷɪѓˌų.êʄҕώ˃ԓ',
                'categories': [
                    'internal',
                    'network',
                    'invalid-user-action',
                    'file',
                    'invalid-user-action',
                    'invalid-user-action',
                    'internal',
                    'configuration',
                    'access-restriction',
                    'os',
                ],
                'source': 'òȖȖ1ɦ\u0383ԥϽΞѾԚΐǖІǳҹǹӴѹɄCҵȶĠԒʹŚȶ΅Ƭ',
                'messages': [
                    {
                            'catalog': 'їΠΚůΊƺņ˥ǂц4ĕ<ȼӱɡǉȖˊφ˒ХóȾѻMŞŢңʈ',
                            'message': 'Ȇ\x7f˓ӥƋq\x98Ȟó\x82ԫȅԍϔπԛƒ҆ƯΡȴρԃ˻Ԝ;ſȗQɅ',
                            'arguments': [
                                        {
                                                        'name': 'ǽO˥¬ѳŴĠ;ĎήԢ¶ğЩҠïʐƫӐŀѻʈψѫé1ΚĦԦˤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '§ŷэӻŽɾΧХĠɦĭϣǙЍǞǋƃǟƫѶϿϾɕкҁ˹ωǦѝԣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Єʊǘyˌ\x95ҩjC',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Нҙ˦´eгєǝύӪ^ӸΟăҫ¦ԕȗϰİ¶þǟҏǖҭ4ȱǄΡ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃǳһxeԎʒƱкɏ1ř˫Шʰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĄʟɗǀПԚȾ˓ӤÒAȢȌÅƒǓɬԐӳòӷ7ʑәǀЁύӔ\\ʍ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӡδïϋҡ-ĸӫΠʵɗΚ϶ȍԔă˽˂ӾǪʂȗȃBþKԁǆѸò',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǞóμÚǵĜǕēЀɶЁӭХΰӳԥˮЄͻȶ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'čЎɳɒʿφƲɚļӍ3ҨӿϑϰB\x80ˁӎĖȤϖʹ˶ҘбЖʁˣ˕',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѩ\x95ŗǽӕ?ǆ˘ƛţьҎϋɒҎè',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂ\x88р\u0380Gλ\u038dǔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '¢¤фԁ7ԂȸʉɧɩҊЙѓdԥ˺ĒȡçĞ҃ϘɻϯωɽѹȻʨɐ',
                            'message': 'ȷʇǌƿԜҬӵɬԧкιԞΥ˦ʠҩȍҧ˭ǎˀǞ΅ʼԪ\u0383џ˸ȵЀ',
                            'arguments': [
                                        {
                                                        'name': '\x7fÒ͵ӃӬƵОέҎ>\x9bԔ\u038dЭ\x8b¾˅ȃ\x89ƵƓӀºǒ&ːѹԂłĎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200425.332356:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁíӬ·ӏɥ×ɖΕψƔģʛAsӞɤǲòȳáȶЂ¦Âưӟ©ԞÖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӉӼόˁςΔ\u0382ǥTŹԢϙɣ*ĬоŜơȚѱЁƈʊƼҌĈ҄ʟʰ\x8d',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382Ēԋ˔ý²Ȇ]ɚưķ\u038bŚ$ɤƤŌǝΖĞǜĺхӓҴĦɋżѢЦ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӸϏǽǩŷАϪΧЂʃʅ¤ŏʷˤƭǘǕĥįҞɪϲɜȇ±Ȅ˒ԫɍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʓdӗʷӿˈԜёɽˌÄϏԖҙǯɏˏÒȡԅЏϲҵÁГʙхĪӐΕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8717516645801824173,
                                                                        },
                                                    },
                                        {
                                                        'name': '%ԐĩҪÄϪʭ҈\x9f³ӞƼ<ː;ĂǚϲҞŹéԣӬǽnʣˋӢȎФ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʋȤæǳһȫǠ7ӲӻӞѡ˳\x8aːӲӁԄΎɟ\x8eҕɤžͺШԞ˞ϊ˚',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'μˆѺȇӨcҙͼҎҷʹʽϘˡαʀư˺ͽüɽaԌїЬ҆1ÝĊ˪',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍƏҼˌ¬λ\x88ļФɸ\x88\u038dÛØïŢȑ˫ΐ2ŎвèӤŠėǱѯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʚÜрν˖ҲWÑтǗό\x8bȜΠҥϲȑ\x95ϿЉ\x83˛ģХǪǴѵƽӹƋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 803843.7159548372,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϩÛ\u0380˹˨ѻƵӖƱȯ˄¢Bϖфɔ˦ƻϠД˩ɍȾƦKӹϟ4Ԇӵ',
                            'message': 'ϑԜ\xa0ŹūȳǙąҗŕΚęƑƦǜƗßӕфȒƓΆӳҥɡɰıӠĪΞ',
                            'arguments': [
                                        {
                                                        'name': 'ʖʪ˄ȭƽȆ%Ԏϣщάņԓ˅·˞ɃŌ\x9dΟβÕԀȉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200426.176836:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɏ҇ŖԌО',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3002939602351750379,
                                                                        },
                                                    },
                                        {
                                                        'name': 'αщЧϖǒмЖͲХǪĎɓȾIӗYɜƥȬˍȽбϐа\x8cͻѹʫζ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 798668.0749663963,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴƮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 143853.80732797104,
                                                                        },
                                                    },
                                        {
                                                        'name': 'пӼɰӢǀǹΤɤ¼ŘĜȮίƣǫͼɂӖϑǡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѱ˚Л\u0379ɤЛəýɰҾæØ˕ѵĳΞѴƺGωԦѕʯȞͿԉƾĥĴϪ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѕƿʟʇѐ|ЇŃûĂΟӞƌWIȜøMƅ¹ӃϋÔŎʀ˻čȻɊЇ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒԒǨ˚лНи˹ӌӓŜǀξӝĬҏёǪљÈӕƢҒъҕŭăηʑѱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƆǏɷҼĘˑ҂ŷАlЀgҰf\x96ŁӀȴŵҙƽҘ˹ɑͶԐϩêþς',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200426.908485:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΨϬǲǆñʠɦǉʛΩșǉ˻˹ȓ;τ΅ʊŪʸʍԧѠƊĸa',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 400426.40218331205,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϫҐɥźΖəł¹*ǲȦĩĽȲȘê;ĴÃȿԣӽ\u038dĀβ"Ƃ˧ÈǦ',
                            'message': 'ǩÂŔɬaśČ˴˯Сÿȃˑ\x98mϟʛӿóҖϽԪǁЮĠԗόɨĒƄ',
                            'arguments': [
                                        {
                                                        'name': 'ȃƔԚϠǜӄӂˌ¥ʎŏаƯƷͶɖǝȰ´ыŗʭjʲ:ĊҰњȬ҃',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dÆ˟цю˼ƛȄɖˏǄɻ҃Ť$͵ҀZɦȋɫʬψЉǨêԓԢ˷˾',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƖӸѣúǣǯīɇΣӊӅͺõȊ˙ðiɣ)ȫϨñӍïr˕įϸʸr',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x86ȊϤnɹі\x84ԥ\x97ǈѥɳɂÚ\x8eӀƀҼŋƠЉϲ˓ĳηҔ2ʪºʋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϨƼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 543145.0997649393,
                                                                        },
                                                    },
                                        {
                                                        'name': 'þÜяԀΊțҫʓӼΰȧƠŊʦ<˓ġƸӧǁϧΤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2417315152303689402,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƾm\x92õƎˆЊԆſΏ»',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'βŜκŻíŃȤvԠ+ʸҐʇ±ȼ±Ŷ˚Ŧңʮ¼ɠβȳƻȅèԨӷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 934279.739942024,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ß΅ϪˎɖœӲŐ·ǬĮżŇƴ˸҇į;ʁžʗњǍǙѮƏԨ\x95_Ͼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 849596.9786706135,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԦÞΛ˂ĂÄċӠͱЁb\x8cˉӭӤĂԞӁɬf҃ɰːϏŠɾƖ]ρŒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2034859307259361224,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÌƥÃԫ?ÔÓǐϭϵӞľ˻о\x97ϖņɓ?û',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1786135997606646101,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʑԤҲЕı)қǋϻюβȆԖӗνǸǼѫҪ',
                            'message': 'ʨǻ˲Ŵŋӈ˼\u0383ҾůǫΉ͵ɋԜǦʚƳƼ¨Ԩ~ԉĭъԔοʎʌІ',
                            'arguments': [
                                        {
                                                        'name': 'ӽˌȡ\x82ЯŬУѻҦ\xa0Śɷƅ¹ƼǡͽДȦԎǂˬГ˘¶ΓԡҏеѺ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8541873369100631385,
                                                                        },
                                                    },
                                        {
                                                        'name': '·Λǿφȧѩ8кǋЀòΫƮԖόϤΐĻɯɟ.ŧɜǲɇ\x86Eџˮɝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3501297547193812406,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѵΧѦ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3183251773372703707,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʾԥƏÅêѶҢȿŤ\x9d\x87Ύ˓NѵӏˈĎԬίŒЧͼ˶ɶİˣN\x99Ѳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂŤӣҪϋıĽҜΗĲŜр˻ӸӰʄ\x86\x84ǌӆВІȐÀȢ\x7fģ˭Ѽа',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382ȈɐʇѓԪԣƟΰͳƆ\u0380ǈƎ&˱[(ǏĿʡӗ\xad{\u03a2ȉ¦ӬҷϪ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200428.455452:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЌϚ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '0ǛӯðϷùȹñν˾Þ˴˖ʸÏ¤гëϳɹǱ6ϰьΆӳŏʉŜʛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϲ$˵©J=ΟЈoʳDƽ\x90ʏϸԫ\x83\x92ӺЕˣȅΛ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 533977.906782654,
                                                                        },
                                                    },
                                        {
                                                        'name': '°ȶƤËхħĘȂǃ]ŮŉʗѪηҟԝͺϘƂѰҎůƔϔ^ǓŊǨã',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȦĿɘϜťѩǱǱҶǫ\x98Ж\u0383ÂLȶԅϮɶΝȊѡǝ9Λ3ӽǓҀЫ',
                            'message': 'ƍЭșȬтǈԒ˺ԫӿǜɌhυ˞čRŊͱ÷´ǔƦԚˊʯĺЯăӱ',
                            'arguments': [
                                        {
                                                        'name': 'ŗŭˈҩȽ+ȍΟ϶Ѿ°ˌ¯Ԉΰǉƚʂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĄЏʝ\x9bҊԝðæƥ¹Ģцωæ҆ё˃ȭɫʉӷˬȸ˹ϒѩęϓҞe',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӷųňµνɋ˩£҆\x8eɧ\x8fʐΤίʰ\u0378ĚFʺЂΫŴʳԦюИјўϟ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŌƹÙ¯˒҃dϤκЗΖȘa˱*ˢȊй\x92ĊǀԭʑȜŻʏĂĞ¾ϖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ыΰ«6Ⱦqȑшŗ҉',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 581848.0107498678,
                                                                        },
                                                    },
                                        {
                                                        'name': '(ɻ\u0381ӠҒTȕ\u038dŜәĈӴʢҧĨͰѴaˍӢˌųɁIa˲ѝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽΫ^˛ńςуǴ4ĖǸ.ԮřƔ}\x83ǟƾӧɧ;',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӨǜʰѾЙ/ԛЄɰǇkdɰӇĦˇʟђď˚ҋɁ)ǵǛ\u0381ˈњľϺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉǵüǳʞѭʋπЂОһÆФα\x9fˤɕѧοȁЊ¸ʦɄϝƽҸǰ˯˛',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ШνҧÉΉбХνW˨?Ÿʺ˓жС˵ЛӬ\x9fÄ˯ӝŦτϱԆ˝ЀɅ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŻƾșŊȢһѷӈΗȒƓȆìҖ×_λϻΩԃͳӜĖƴLˡúɇӏҚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u0382ͻΓӊɊʞͻ!ąѶİ6юΙřǤԒϤȲȭĉҽʦʍ£Ɩ\x9fɼĩɣ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǺǜΑҀǲǑΎňԨλʅРџʑԪζΈˇ˅˷цЄ*Έ§ȳǤǠÀȀ',
                            'message': 'АJUà˺ȇŰĂјˢĬϛÀѤӈāšɛӚ(\x87ιӀ«өиϿȏîx',
                            'arguments': [
                                        {
                                                        'name': 'ԫёϤéɲĎŖΙ˺ʾϏԧκԊÃѼԉԨŃϠʏѸɒȻɾ6ѮǫȆτ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȐӮӊȌĉйʊϙɌ\x7fʎʴˉúͺåȺkѵĂЌƕƏDƖӸҤѥȨǌ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5019593953489766601,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɶ[ԤϕϻҿȼǝΠAѼCΛČőӲǆҜlɴ\x86ԭ]ӇțĆҔԏ±ˎ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƘʄǓȅϲɽфΗʤʅƎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Fʄσ\x8fϑӱͻÂɂӃΣƸǑԂȳƸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 287563.2252932588,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƗɈȵǵãʼѰȻѴßǪ\u0379',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԍϵѕ϶ҶПѽ\x9fíτĚЇʰȗ3К\x88ѯÎϏЧ˅ΝπpñHÌϘ˶',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƞ˝',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 345389.0876485648,
                                                                        },
                                                    },
                                        {
                                                        'name': 'әȒӳϿŧƷãѼɭǪŎȱˮƲń',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƲяЂɯǷËʁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɒѓç˭ȘѻßY<ĺϔǛĎÇфʔŢůeΈž\u03a2ВĎˎƍʍΠԙȇ',
                            'message': 'èɪҺΐ\u0378Ĝ˕ԛϊƑƒʬħаΛÑ\x82ÅϩΙǖɭȄӇǁϤѲ?ҘĤ',
                            'arguments': [
                                        {
                                                        'name': 'ɳCƔąӇɏӞǦѴ"ʡԠζа×ӫɴбöĀ˼ʚӖ˧Ԙʹ.Ȍ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˉaԂΪˇ\x84эѧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '>ԇǿЏȡΕϢĮĩЊψʑªƿȯѾ;˳DȒҮġŽЫЮƍƯƥÞҌ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˶дÁǶƝΑŴŬ^˴9',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'τƎӽԐш/\u0379ǌǚӐƨ˲Ϩ΄ɡΰˏχřʄ¨ңƢѾΟӲϏˑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 694490.817688488,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u03a2ãĪҳßųˍӽϝÝƯ˾ŌΚЩʝљ\x90ÆɉC˟Íǈɠ\x8bʖǰƇˤ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˥ķǵԙĦЬɣԨȬ˙ѓ4ŗЀЍ\u0381ЧÍʴĽ\u0378ЏԬJϕäƉǇAɌ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x89ƤȅɟŧԢπ\u0379ԟƌǮĩѻҎʆŌûȫдĳӉӺКºЂнˮ\x9fԆЋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6950605613738424100,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưȧǌī˱ʤшπʴɤe\u03a2ϯə©\x9dȩíӴΝƽʀå˖ӵԙͰɝʠѢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x98ҾɰӭÙжMNϪҀλѤʙԚДŐхð',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'âĸұ˞ǀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÇɉŀӃҲ\u0378ƈ*ӅϨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԗϏϚŇѪӔҚѽҕȲϸɦѸɅ(τҕ¦Čͺ˫m˺ʞӷ҄ЈΏɗX',
                            'message': 'Ӻ\x98ӬϩԈЃӭČȮʎξǔxͲ"νŔƻ{)ɛZĸ²ǋЙǨԙ¬ǉ',
                            'arguments': [
                                        {
                                                        'name': 'ÖӞҷΥŜ\x85ɀσ\x8cɍćүɁŧѣŕқ˶Ҷńϻ)ЈАpӧФËеʠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5477254592916332037,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԂʗƝҩ[ʭȝϩbÔӗΔҒε#ϿζǅґќĤшӻ³ʒ·ʷ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200431.675492:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԋʐљ£ͱʯϽ\x86',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠxuɛʫγʿѬ˼PāŻӅϨɁűҥÒkϜљгѷȕȤʥ\x8cΣµͶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200431.868299:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɚÀİЩͼʕӾӻӏƞҙӯ˚ǋ϶ʓʲ¾όύǍƿӓ°ʲФғɣ¼к',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 321113.3473342385,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ίhҹЌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΖɤĮɥʺʢ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200432.097034:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҸӁ\x80vμЧƘӖ\x84ԩԟӥƁӈ˗¢˙ϿǮŨćȦϗ\x83ǙʄϪщ·Ǝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x90',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӭˇ\x96ʎʫ^ȼҮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʦӌþǙѩ\u0382ɓ\x93Áˇ\u038bŲßϗӈʩɴԨ4Υƍęˎɝ>ƏǎŴʏԛ',
                            'message': 'ҦɹĨ²ԎǞ\x9b\x8bƮ҄ԞѠӲѧˇƠԊ\u038bͷӠΫƾÐ0½ӾюǴȦ\x81',
                            'arguments': [
                                        {
                                                        'name': 'ѝзʴÜ*ŦϬρǑɁґ˜Єılε©ΚÒèρԨö˱',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˘\x97\xad/.p;ĂЋǐōñɲλʃ»ǖќʰÿ)Üũŭ*ǘɂΖƯϥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˊλ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '§Ҽ©×ҸŲĽħɔΩǏēɡҡӵҾĭΊƜрrУ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʚK¦пZ\x9bъΪӽK:ÐʓˠҮå ԇνқƋ«ʣŉь҄ƋğƬ\x8f',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƦϓѐÀƞˁȏ\u0380ǈϗĦџϏĥðԡ»ҧʐȪˣœËêä˭ȅǟ9Ř',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԀϰƹĲ˖ˀȹʗƊÇşŝ°ʝˎ"\x83ʙѨοε·TΈ/ѧςΛȁҖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200432.835423:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'чғ҃Ӌʝ\x83üҧҘɬ˞',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʂ˳юzФЉŷɦЫȘQɳҷѼÍϳǹӐлˣˆӴԕĀҫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7349996505390999445,
                                                                        },
                                                    },
                                        {
                                                        'name': '9ԄģʞɕɁԎǣ˳ÜǏҧҳʿϷ]ÓûŕƟі',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯĎώ\x84ӈQƢ^ƌӨǹϊɃŏYžԟĸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 439254.69631910766,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȑԖʧŢпҍʡȹɻÈӟϨȹɎ\x89ʉԘɭƲҮњƅ¼ԋżҳD+ˏ˄',
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

            'name': 'ʬǁÊ',

            'error': {
                'identifier': 'ƫԃȊћɒ',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': '\x8bȔ',
                            'message': 'ɔ',
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
            'event_id': 'љїʟȪһ;«ӬǽɜÐҜƏΑӠʿцƿӮG\x86ӀӣǳɎΑȝʗțң',
            'target_id': 'φϾѐ˷à˒ģӘɭӵҚũƜŶĿɋƻ˨ȁɠƲ+ҺγŔǻÈƯĭÏ',
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
                    'event_id': 'ȉԂϨãϷ¾ɆǞҕnɓѸʭĈίU:άġ\x99ʹɧɔöǕ>Ϗɾф.',
                    'target_id': 'ЏʳŽӓʦŚY/÷țҷЎѺ!ƝGǭņq¿ѪŜЂŜƮɀΗȟ¡ǳ',
                },
                {
                    'event_id': '϶шό҉ȉЉĔϗԗ˷ЍУƆɣİȓúʎƛөʨͳʍś˶˄mȏ\x93Ķ',
                    'target_id': 'W3ʥϲΘȗӁ\x7fŶǻČÙʧԋБȾ˫ƚ\x8fҶʨʵԠӬ?ѸbͶ˼Ѹ',
                },
                {
                    'event_id': 'ǸԌӋȎ҃ɜ҅ʒ§ɋҫǜҵˊʭҀǣϬό³Š:ĞƋԉȪƭŢˌĉ',
                    'target_id': '˚ˇ˭њžЀέǧêǵЕďтlȡыҴ¡ĸ\x97ʞɻVēĩɧҥƵʅê',
                },
                {
                    'event_id': 'Γ²ҼЬȨҿƑѱҷ;ĦvǤĠʵҴǿȹ±țùΩγ³ќŅ5sϚѷ',
                    'target_id': '0ќћæȘ£ĩʘ˪ĳĒѕəØưǾ˪ÆϮřǞϨ©ƧΉҏϐ_ɆǕ',
                },
                {
                    'event_id': 'КϙāԨӸЪѹԄǏЊќ\x94θ©ŵԑƛʥƮΣ;ѥJ\u03a2ЁϷǣѸƛķ',
                    'target_id': 'ıҠjҼфʃɰ˴ǼüʟƺȒҮŦǕǬȖлǆҥƍʇŜ·ēѭɈÔш',
                },
                {
                    'event_id': 'өǞǰ0Ʒμ2λӪǢ˦Ǆδ¬ΧɛʻʹϖŒâp=ζǺӇϜÓԄĨ',
                    'target_id': 'ȇԓʷЬtˎȓ˱9ԦŜȓţȯӫƠÀɚƟƍҙĔӞĎxҠӐ\x97ϠӬ',
                },
                {
                    'event_id': 'ǡ\x98ʀřԀʦȵ}ƱԄбǑΉňΆŏüˊŭίϤɌǃ\u0379ұЕ*ЭϹͷ',
                    'target_id': 'Ҩ6җҹƂӹǢϏĔӥŪi˾ԉǏÁχҒƅѩȔÐƟʰӦȆĎЦŧҀ',
                },
                {
                    'event_id': 'ŻqΗÒɅȔҘȩŹˍĜԁĻΒÝǽʌǉĂϦӡńϥǑŤŚǸѢˍʓ',
                    'target_id': 'ɽəоǺʐƱҠˉђӿǥϳfƶGʪöϥˋƋȆɗ\x87ȌϓŬƃңѓɏ',
                },
                {
                    'event_id': 'ƀӕüÿҮҩˏŧӔ0ʳȋ˓ˣѱҡʊҶёÕőЎŷ´Ѯ\x80ͲԌ˝ȇ',
                    'target_id': 'ѳěï0БχƾʾǟŗɆΗѸӮοҒȽÃOȜφ}āһXéϵöхǠ',
                },
                {
                    'event_id': 'Ίʵΐ;ԓ#0ˋǧ',
                    'target_id': 'Τġӕ2ЯƍϩɂЛiԖ\x9cˣĒпѴАóćɿψĴ\u0382ѬſʉΜsɤ҉',
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
                    'event_id': 'ѮϯƠ[TŭЌʀԉɎѹɭӜɋα/ҐǼBͲЖOÌӷ1"ĭȸȐґ',
                    'target_id': 'ħŀΤ˸ĆϠϣЂ˝˰ӛ\x9dˆԢǱľʸȽϓƫҳƃƇʰͶхϸRhq',
                },
                {
                    'event_id': 'ϰƤʆŝ+ɭ!˟ŝԘʸľƝöɝÕŀƹ˺҆`ŷ',
                    'target_id': 'ʣЁȆ²ǴřƨӣȘ1Ϥ˾ςІƾM\x99ɦԨƚϙUŰҾˣɸкpΩҺ',
                },
                {
                    'event_id': '˪˭ƋсïǏԍöňӄƫʙҟǏñɑ!ԝϮȎÀƬǄϼЬˉњģĽÑ',
                    'target_id': 'ӕhǽл\x88\x88ʲ¼ǫДιҕġʶÎƗԨȠюĩȪԩϢ½%ǎƫ҂Уƛ',
                },
                {
                    'event_id': 'ǰͱÁĵѸϫО]XɤίѽɨæӷˁѓɬǻˮʏҡѢȋҦʠȺϒєŢ',
                    'target_id': 'ϮɈW˶ÁѦƚĳźǱʌθƥɓ\u038dӞтоʫǸŚŧˇǄуУ\xadŵӆā',
                },
                {
                    'event_id': '.ӦВяÊɭѯȶɈWЬ\xa0÷ӿ˗ǀɶ\x99ǶƍϠƪÿƴưİůũӶЍ',
                    'target_id': 'śĊΰΟϿχ^ǶʩüйȕžĻϙ˓˞ΗƇöЅАԮӾӺF\x80ǦԒԎ',
                },
                {
                    'event_id': 'ϏɐԞѕeƼ²πϔҮĘ',
                    'target_id': 'өsčèʙóǵ¯±ɖ\x93ö˕ȧӕԋ˻˻˅mŦ-ȆƉҷ˳ц¡Ӟȷ',
                },
                {
                    'event_id': 'ĐU˄ɷЩɋȄʉʫƅɡȻÓȨԠҠԅŋÈλǙҍʹmΓ΅ɺɺȇȾ',
                    'target_id': '\x84ĮΘȤĻόˇЉüũԄʢ҈ĹԖĎƂШkȻâϙԟҀČʆ\x9eFə˥',
                },
                {
                    'event_id': 'ũϡ˦\u0379ʎǛ˥ȓшϓțӵΥϽĲҥȦЂɦˀGʖ|L҃ȼ_Ҷ\x7fȚ',
                    'target_id': 'ǔPчҤĥ±e˚Ѝ\x86άЊЕşŀȲ\x98w\x8cɅμťУϤœϫӘϾɡʘ',
                },
                {
                    'event_id': 'ȧȇфƼ҇Ǽǰ҈ĎμʺˍϿÖŕĘZԨӊʬϛǮΟɓДӄpȘƨ?',
                    'target_id': 'ŲʝͿү/TȞȈХƣǦП\x85ÉǎґØ\u038dώΥοɫ¦\x8c˶ÇÏʬѧɽ',
                },
                {
                    'event_id': 'ɊЏύʉҹϧцèΰϴαŅϛ\x89ԅҿЗŨºͼφеǢȕѠ˛EϺԣȉ',
                    'target_id': '\x9b҅˛ïͿөūҌʧ\u0383ъϵǀǟņDāͻȃʚȾжѢӜӸӅȝɝӢѳ',
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
