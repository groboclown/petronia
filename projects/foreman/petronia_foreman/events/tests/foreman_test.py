# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-06T22:09:14.422437

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
                'ʋʪ±ȍĂˎǝĦ\u0378С',
                'ƝťǜǬVMǦӽƈ\x8dϳŻѢ1ΗӝɐĨΉǨԚÅйƭӍƇÇ\\ąΩ',
                'ϴűkÚǴƉѼӄοƦΎʄŖýŉάɢ=˶έqȿ²ʨXɟɁǁ¿Ά',
                'ѵňþʈЋŝ«҆čǙƽ˫ȌΉǠ\x91ˑ\x93ȵѶǲĴӉΎ/Ѹҩ`ʪŪ',
                'ЗƥĜYмʸǤāʭßԓßδɡ¦ϏOO\u0383Ɏ\x86ϫӾƮΚҡēʯӨЦ',
                'Ȃӕ5ҘчǾ˜ԞqӇƣʰƊˤˡgЗÀùˁʲҴȞʁ?#ʺ˴Ś˦',
                'ͱŻ;šѕ\x98ułԒІԅɲӇϳŤɼӫ\u0380˷ӊâɝҒ§ñƱ\x89ӝû\x9f',
                '"ĂҸʣȼИɤˋ\x9eϪΣżͺǅκѾ˳Ɇ@ģԞh˨ˍϖrоѳǛĔ',
                'ϺȽҲζ\x91Ǻʌ"ʒŘȣѻƿӒ\'əщɍĮМ˕Ԭź\x95ɰϗԓ\x97Ĺϼ',
                'åҏϦԣǧϳƗ˞ȫҳȵɎԐ{ӓʳϹӘȆЅə4ȭԄӈ\u0378Ϡή\\Ǔ',
            ],
            'source_id_prefixes': [
                'ɱҼ\x9cTϩϡuϊßɀҢÎχ¯ѡԄƅҦўø\x7fÇºżQԕņpҺȓ',
                'ļҗ˭Ŋ£ȑӊǁȎʈυȳłңĊʳ¸Ҿґǐ^\u0383ȞƇωНӞɶʚ˝',
                '"ҢȉӉȂȁҶÉш\u0383үοĪŸ\x94ÚʮҤ\u0378тȽÇŢ҅Ĳ¶ĆɦȴΠ',
                'ćǄОƞԩũ˱ʎËĀɥͰǛǦCʞȔԐDȒ˫øǨ˲ѪӪb;ŉƨ',
                'śɎɦƠƦДΐ*2ԭFГɐӽÄ»ɧƾǵ¤˴ҪüЗöϨξ˜ϵ˯',
                'ȲšʹȀ ɎƢƻǯіιCǸКƜɔ˼Фlˌ³ЊЃΔҒџ Ӓӿҷ',
                'ôązΕ˭ʂ\x88ȫɘƘ\x8eӠϼˤґҍѽʺÁǜ',
                '϶ґχʩƦȘҚqɚ\u0381˒ǐ\x95ġЇ˙҄ğmъƮϾɰдӰʌNґǁʜ',
                'èʧкҚɖķŗƊȏǙƢѫƂʤƾҖþЩ˄ƜŀӸǩPԥʗήħÛѻ',
                'ԞįǸ\x87RВ\x90ѲɑѠUʤXǁҕćґҧȺΘΙɡњ{ȗɱЁƾŏw',
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
            'action': '҉ԨɞИȊʂűԢɵ+ǐǍЭǏӇ\x86х(Ҵ\u0381ʺЙƭҩ\u0381\xadίʜkϜ',
            'resources': [
                'ǋĺ2\x9eÜywʵƸ\x89Ԇ˲ʹӪ¨ƀXƪ\x9bH\x98Ӂ\x89ϡԝȚŪǎøѩ',
                'ǎЙѥ³ȱ>˄ƴ\x91ŇҖņˋ˽*\x81˹Ɨ\u0381ôʓʄϩԏɶȣɤƷĭ\x9f',
                'Ȃ°ҶǹĠρҧ˫§ԠЋʪɃǤХӊоΫ˱\x95ͳƫҬĹmĬĊЌ»ϖ',
                'λΨǕîҢԅˊʑĸѪǌӓpБǁ;Ѭ¼\x98jԙԮƶȪđͱʦʷR\x8c',
                'цǖСӗʳȌVƾėϹԡíǎʀŠӄşԧ}˺ǄÐ˯ӀєȤνƲƥW',
                'ĤʛФSàwЅȷ҉ІŹԝɞƣȮѯǠҸdΪϲʁǣɤӒʻɦʘҠΐ',
                'ʁЪР΅Ι˘ʅǷʝȩϏĺ¥âǾȤǦͰȳҐЕнЏЋīͼ¡˞Я˵',
                'ūғ3ԉӳǑtʓӝȣǕ´§ΐη˅;Ʀ¹Ԓɭ¸ˈȥνƚεȌϥΨ',
                'ˉ҆ƦѾˀǐ1ŶҸú\x9c\x9eÏЉйĉËԂѕƭЏ}˭ŦАқȫ˥ˊǇ',
                'ƑƗҸ´\x90п˚ũ}˩\u0381ѧǝɈ\x84ĺϠ\x9eβoȶғŋʹĜźǉџǢǬ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ʂ',

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
            'name': '˥˘œƓͿԮȸ\x84ҟюÇ\x86ԞȟǐĉУŻ9ǔʒĹı|Ĩλ˟ыTɮ',
            'version': [
                -2734015552630180424,
                -4872093830991623372,
                -6984542582366105943,
            ],
            'location': [
                'Ϲ¸Ҷſȋ\x9bƦţʰĚƑTѺЙѫ2ǜӭɆÝЉÄыΉ¬гѠC?b',
                'ċǺ\xadʌΆˬοɨęȲӕΜйӴ˪҄4ʏҕȹѤĜΣŃ2ǗC ħԨ',
                'bɎϒIͿҢӲÖǵÅ˦ʳƽvЇсȦwŭYƃ;ȩǞȲԅ\u0383ɯȢɷ',
                'ҟ˘ɌΥ\x8eЧţćóǌϬɂԇȰ#i§:Ř\x91ɹҩôºӝF\x99щɈʟ',
                'ћӕɏų˝҈σĹŃ¬ҤJ%ςžѺϭʵũӒνҷĶŒαϲƼǔɯº',
                'ӯѓƹʏ\u03a2ӚĶƻ҇ƶԇĦē\u0380ƌѫӷѕșĺ¯CЁӾʊȰδ=ëͰ',
                'ÑñүʰɒaҗʳUȺ}ɓЃ\x90ȯЮʃΆǇưƔϢǃ˱ǝѤЀǞ2»',
                'ȯƢФ8ҜԧƲӣԐ§·ǋӪš_éԍɿѲŮҸTδʼƄÅмƱɴѰ',
                '»ǐɛɅСșѬ«˦ЅӨÈΕɔѢìlŭʆîúВŤĹϪмʽɚǷԆ',
                'Ѓ˹ΠŬéęԕѧҘĖšȷƔΕϕÉӞIȮFĩИϯȖԆȸʥ^ӯȂ',
            ],
            'runtime': 'ԓ\x8e¼ѥȋӧɚǈǇ҉µȲŎɆΑřŤмЏɥˇȍѺƟʻϥΫùϰȆ',
            'send_access': {
                'event_ids': [
                    'Жȋυ¢ɿɎǈH$ˉ΄ʩыΠöϝҫŷ˔ʊрƈŽſžƕǕĿrĽ',
                    'όĺƎ\u0383ѐǘʻϩϳzԮћўӪơєЬɢĬұ}ϹДˇƝˎɫɷϟŻ',
                    'aɲΰѧ°ɡġǊêͿŘЇњǅӖʴ\u0381҆ǭ(ʒŗӕӞţд˗ӲΕŊ',
                    'ȰIѮνƣ±ԈǛяǆȌϐΣ#ƙQƽɡќЬɡÝϘҹɞɮCpѓʇ',
                    'ÖŝdƑʅ˨ʆƠ±ƮǥӢƇȨʡȶғгǴ˙ѮʥƙŌӿğϼ)ɬÒ',
                    'ǄНąlį¶уϡĎҳ_ɇҵИSԤǲļźҾКɆӡ(GЋľɏʩ˥',
                    'đyΧ˚ӊĉʛ\x7f2ҽPÄ˃ʶӟəȍԛpяZӊɾƤ\x91αԖβЏӚ',
                    'ŔĘɑĻвȶ\x95ЪͽɸЛƸ˫ӟ˒Ʀȧ7ҦŏʓʋӘ`Α˘:ƺȜҤ',
                    'ԝϗΧʫĺϴȩϐϽɺжǖˠŻҬƸÝĕȔËόöϦҲ˷ҪшҐαʔ',
                    'ŬkԩµíςƉǕПϭς¢ԩєʄѼуǫѭƷʭͷɯΧȀíѰҍ©>',
                ],
                'source_id_prefixes': [
                    "АЛø'ӜĐȺʡӑ3S͵ɰ-ХйԔʔѬÃ\u0380ƺӬȃɄůēГƻԊ",
                    'Ԋ\x8eԍFrԨȑĭǛϽ|ÇӳʀǷȒ҆ľүғƞ\x93Ɍ"ҽñѡӊд4',
                    'ǲŦǲı˥˲ʫǬgɚЖx˪ž\x93ρǉЇϙƅ˜RϲϜŪMүҦϼҵ',
                    'Ҥʒ·γĺЬźҦЮΪԋĖțԑȹ2ҭĮȫʈʁͰӔҫȔҼқӢƭж',
                    'cΜӰк˒ҙʿºɉϮєʱǘєьώϖλϰ\x87αƕyИљ&ϊʿϏK',
                    'ѯӒŴд\x94ÔЃҟ˟ʍҌƤЧıʊҼʃ\u0379Дϲѿ\x96˰Ҷğ\u0379ϏьΪč',
                    'WЌǓȕŒшńϲňǮʆ˞ŴЋ§ӝņëϺ@ǓυδȓџĬҏåŤɰ',
                    'ҿεǥƠӃѡ˼ԈӵɜʌԎ˽ϖ',
                    'ҬёɮºǔЮϽ\u038dǑƋȾQοȸ˜ȮȑӸɉŇªƪĲͱȉ˨ќ˗œɒ',
                    '¦ƅĵˎǓʈԉʦʇèѺǁQэγҤƂ˟µƦ˗Ý_ӴƙǺӏĉ;њ',
                ],
            },
            'configuration': 'Э\x84ӔͽɅɼįγͽ_ŜƪƖȺúƸèҋœԢʛɡâҖɁΓѳІςƆ',
            'permissions': [
                {
                    'action': 'šӘҺХϿˊǏұϮwΔͰ[Ѭ×Ԁ÷НԝњɷӳІĢϚ&ȅԂşs',
                    'resources': [
                            '\x83ǝBɒТƯŁқʻƔЭԆəɯɨ˨Ӌʃћ±όόϻѺɍ˨Ͷǜ\x9f×',
                            'ŁАЀӌȝǤϠҝˋ¶\x9bԟОȄʚˤеƑԞgGѺųAҢȪɀfĿE',
                            'lÝ\x85џԩÓέðR҃pºɞƱ˥˂Ʀу¿Ӯʲȓ"ÿŷŧȕԩӒԇ',
                            'Ԧ÷в\x83ԫҲǎʀˏӇτĔœǕϣϦžƄҜʻ¸\x93Ē¯ʊǘ·њ0Ԫ',
                            'µВǲщcȢƩӆɚЌџćǿϸѭöѓͿЎ\x98ƽиԮѯϝґђ\u0378Ӟ×',
                            'ǑԣdƱқΰűϩĸ\x93ĥɍΦχˬԥȽǚòʵˌÐɯĩɴŤŷКƜˮ',
                            'ƇĐˉŎǌ<ůĦϑ²źÉԃЫҏӉ?bƕԖе/SưυǙçΝϴ\x96',
                            'şҺɦïȜӶΦz˙ϥĎψ÷ĩĬǹѥǉˑ\x8dȯ°ђŧӃЪġðӱǚ',
                            'Ҧươ:ѭŵʰѥȩ1ӵtҟηЭƒǘŃԤӹһѹӵѴͻOÍƮ~',
                            'ʇίћӥԖʤѕїӡµĢ\x81ѤҧКϰӳ\x84˸¦ʃȆőөӏˮŧnϋl',
                        ],
                },
                {
                    'action': 'ΘдĻǲ˲πпɆɦƝǳǹˬӭǼϰӠɢщжȱ$өɝͰřеҶǒĨ',
                    'resources': [
                            'ΘЈёǒĨϡǜ¡ƜРFϷųҷӫǇǮʟçǺϟ҇äƗ˗ČȑĩӲӯ',
                            'ǗѵʜåэʇȈ\x7fȟ^Ӌƶʴ\x8dƸǽʛҡӘѲӾ9ΌLƊÒчπ°ʣ',
                            'ȇFͿà~ÀʉͰǁǆԄ\u0380Έˌ¡ξКǩ>ɈʄȀɃ҉\xa0έιãĂʜ',
                            'ƚƶ\u03a2ӟŠʒҞƂFơ˭ǶȴњɞĐԇ\x82ÚČĦƏȅˎƯҾŚ}',
                            'hȮQÐӃƅžӶӁ\xa0\xa0ϩѵ\x9fͽШЏˮ˟ǳνUҿÍÈƑˏ\u0383ѢȢ',
                            'ƦȕôӰȻǼʤ˦Şæɭe-\x8bΜń\x97ҚԓϾӱĖ˙ȵҽШκѿɍҎ',
                            'ςѫɍɄ˶ҀҐԊ\x8aΛŚƗȬɣňǝʎuȳùцнЈЬòƹ˅Ǫɣǆ',
                            'ѵͳӍ\x82ȠҺγћ0ŠПƟϾɝˮχ˶ɡʤǸƂϬ҈ϴюtå$ϗи',
                            '\u03a25wы`ɿǐ²ԓ\x9c(ȅÊǲ\x99ί±Ԫӻʈɀǽǜ҅Ȯ˰ĀƸіȧ',
                            'ȽʎĖɐĖԮ-âŠрƆϮʙĴӮРɸ±ǦǿȜƋG\u0379ȥөψϩˎż',
                        ],
                },
                {
                    'action': 'ʔԝІǮÔүȉʵиҘԛ˒ɽºόğ˰³ũÁYƆŉīјƛҖӷϦί',
                    'resources': [
                            'ңQʦ)űȧǦӋȓ˽ìτԫԟʚӮĆҋȐ҈ˏțȗώҖΖъǉǆԕ',
                            'ҏɣ+Ҷ_ʜӜҜҪӟӻǪғȖȵŎĂ˖¦ɄƂàԣ\x95ˡ&Ӽɛсƛ',
                            'İԁλтɳ9{ҋЏʆˀκӹҽаļӎɃɯȸ]ϝĹѝɐӓǬӣѳŀ',
                            'ГƲɓ\x91ҬϥǃǫĴìϥʴĠI9Ý˜¨ɐПĜ҇ӜęƂ·ʸ?ĮǱ',
                            'әͳҴ˟ǒφȂÍɇTĠǏιˏm?ŝɀbˬɒă˗ӞLӋīǲʏ˭',
                            '\x8a_҉:ΪɸķĲcҶСƹȣΚʌƆҘɑЅ˄ɑмʲǽƄɹvȌϺƐ',
                            'ҤȂ\x99',
                            'zп}ɽψѺЪǦ˨ԕӲòŘŷ˄ŌЪγӅôĹǓѶӕɦÑϐĥÖы',
                            'ųǵϧǦ=ԧ˵ǏɅҩӷÍБʚϥӭɄĉƆǿǅњ¡ԏFɖľɰɡѵ',
                            '?óВӑГәŬяɷŠsʽ˫*äҍφsKЌc˝yӶ«~eЂ˙Ȗ',
                        ],
                },
                {
                    'action': 'Ɉ9ə;Ⱦ_FϏǒƫɇ\x97ɁͶϙǪ\x83ʃDɹӠұ϶¨Р Γǀʠɇ',
                    'resources': [
                            'Ӳ·3ԉϦ˱ӽȺЈГωΆǃŁƀПˁίĴŊɕ\u0380ŎơĔӬʶΈǱɦ',
                            'бѮӆƉШƙ΅ԀһmЌʠËөńͷ\x82ƂӏѷЍȇ9ӀʣНӴѣɣѼ',
                            'ɒǓ˧ȧˀɦȰ\x94ԇĦ%ѓ"у\x83ˁӚŸɝƖʮԜϏ½ӛȚυÿϮύ',
                            'kƌVΰГWөȃŕ5ʦΪЧƁχӌҁȫϛɔǦŎɞʍαхӌʁω˭',
                            'ʘљIӂНǎıǈʁȻƜá\x98\x8bѧōŹҗƜӄƭФʸïҎҥȔ˞\x87ς',
                            'ϗƊƵ;ȸНɏȌ\x9c®ɸƱɳ˝Ųː˾ҶUϰԨʉ˸Ȍž<ƶԖӥϷ',
                            'χLӳĚπм>Ү|єн¿ԏҡʒĺĮʄЋѮĨŎԦɓg\x8dÐ·ʏè',
                            'HȷюȷԢ1Dü=\\ӀιҰɚëϩëQK9ҩϢԏ\x91±ǩ˟ɖнĽ',
                            'ZσҺ˞ҽЎńĘǼҤ<ҔЕўÀ5ӸŦȀ΅ȑÒЌ&ӔƌW йЃ',
                            'ŐÖ¹ơηɹ°ԪɓɋÓ)ГԉđԉșʅѦ\x8fҎ7ˆŒĨfʯǜΉȍ',
                        ],
                },
                {
                    'action': 'Уьчϔћɶ˵ϧqʝΞ¸Ӽңƞ\x98ƻ6ɗѠЬ¿',
                    'resources': [
                            'ǆȧʉʠшĭЙƸ?ȻԈ±£8ñԂӽŚʻƼԑΨјȅƐ\x87¤ӡ«ɫ',
                            'ɽŀǜɃĖþ_ϲˢ˹ЕΙй˒ĵ˓˱áχӷǢÜғƹŽʘʕʱ\x9eĻ',
                            'љ\x82ɩɛΗѸ.нÑìϘ˛ȼŝǭ´ʲĦԤάμћ®ҝĪғӝ\u0381ʒÂ',
                            'ξΖ˥ĽʲʞѡϥíԑĜΝ\u0379Ύ˟Ƚ',
                            'ǋԈѢǂʫưǐ\x93ϙǠ˾Ȗ˽ʧæÇaǡ,ʊŞÅΉÒƄр˵ʗ³Ѣ',
                            'Ѓ¥ЦӵȹȕĢωΝʉέˊϟôǻǐȵ¶ʁʏ(˕ɓԁөΗƣǩȜɔ',
                            'ƌϱΟРǠ˜χîʠϑĂĭ˫҅ȲɂfĊw\x7fcˤцïӡ\x8aɋιϽя',
                            'ƘӝȹмƼ˴ӳȍƙyͽˮŖà΄эƫΨÃУ¾҈Ů/С´ІʐҪɤ',
                            'µхԤŠ\x97ŰʬœI˅\x9b҂ɤ½3ѩќΊԊǀҍǀЅѷӜ˯Ε[Ř˺',
                            'ҎɸʷӮîʞƭˮˇƩѕҍˊŖ@ÜΙϘǻјҫȤ%ӃÝРҢъɫŷ',
                        ],
                },
                {
                    'action': 'zӅƲˈǤ2ǆ҈ԘҦ҅ɠâɡ͵ńɂΟǂҬwҘ\x8aǣӓңԙҠήϧ',
                    'resources': [
                            'ӹΪҁɐƯǇɼĥЦɨÚ¥ӵѲψѮқıI˨\u0382ĴЋbӎȋÞʄɺʀ',
                            'сœϧӌӭĝgŃĭ˫5²ĶҊӕǝϐȁԡȝԑϝїȀŦèѮѾô˔',
                            'Ɣж˰¥˶×|ΌŮˇ%ʮĴɊӼԎΟѝΡĂʒӍԝɇЈȔ˙ѝ·Ƌ',
                            '4Ɋº˚КǅӡүɌĦʏĿΈȏϮӭйÊɘˀȼʥǑΔǟчӚҖƅΥ',
                            'ƋŞǋϬӲρįΊƒɿǪϒƙҽɀì\x8dĲԔÃ\x99ҖШfʒĭ\xa0ҋ˔Ǚ',
                            'ȂʶŤʍ\x8eМiĵǝȢЦЁǳ˂ʍԠѭΛƚƙȟͺԢȄă¸Л҃Ƨ\x98',
                            'JИӎҟӬí˙ѱҹԢ¥ǄêԍϦÉĠìáǴŇĢȍЕӁ¬ϢŃgɏ',
                            'ЧӏƊєϏɢҭƤÇʲԁѷКѤе\u0378ǀíɐǇȢ«ʳdÍϺʝŞɐҹ',
                            'ԍҁȷïČĢˡҲĵɪəŒ1Ȥ§ɧªǑʐÂʃIѬ˼ňЗÔ\u0378ЂѾ',
                            'ũΙĖñЌиԨˌȫ\x8b˥ΟѩDe˥Ɋę\x88қη\x9bªǩɧϚƭƁΘ˹',
                        ],
                },
                {
                    'action': '>ǰ}ңԒԀúȀϩĵŴ%ΔƑĐÖԪņŸǎşтԂЂ\x84ҀэǮЩ',
                    'resources': [
                            'ɘ\x90ƞӾѲȾҾӺƮϬZǩ˜Aǭȃ¬Һ(ʠǤˤ\x81ŇҀǉυų§}',
                            'ǝɾvȃ$ҴпΒќƙͱӺӛ÷ЍҐ~ГԡˇþЍ¥êˬº˸ǷÞÕ',
                            'ԚЭsΕΗҴʙϓǦĈĳηêǾσċƊɮҲͺʶǽҕԣЪʻʋˉʽȧ',
                            'ʏԡÔŔÝÇҕԝѴűԅôȘʞbίʞȖ,ÖҜˁđþΖѰĵǿЊÔ',
                            'ßƇUͱŽĖĔɆΠù\u0383`ЗҾȠŦϯ҇ʹӕǈĿʜȰˍǍǫӇƦ\u0383',
                            'ҳЈRκċɤÖϪͳԏρƝżçЂʭҶΨɳ\x96ΙлԫƢяĸ-ƐҞЈ',
                            '˲ͶӫԄкʢFѱͷÂȴűƌͷ\x90ģЌĺȻяΆœƳ˅ʛÐȢ~ԓΙ',
                            'hçù˯жϦǆȅƠðҪάgɠPāω:ЇϳÀϚǄӕĚĹĜǛ˯ϰ',
                            '»ɽʅƬɵwˏˌȎvÍƫ¶ĽԬkΗƖÅɖȚѮɱ0\x95ӑҹΝǒԢ',
                            'ǊџȭϮҪŬú6qǎˏɤͲӒǡˏȷʖʼѺǺɌҤǷңАƣɏӫΒ',
                        ],
                },
                {
                    'action': 'Ƙ]\u0382Ϭƾň˱˖Ь˕ƞϡ\x8d\x9eαԍō\x9fϗСÍ4ÙƉ˦țŹҪӾʑ',
                    'resources': [
                            'ӪɌ˺\x9fȂʴzīɪҍЬϪǺsȕ[ƧǌʆϙюԙϘá˙ŕӉOђǻ',
                            'ŋӑӥй\u038d˾ǱƾŷơɬâǊ\x806ɤͳơaĕþНҬê=ΊѲӂӊȩ',
                            '϶2Ȃϟ˝ʤͰѻʜʼѫfľŲŭxҝġτɬŏɿȟҔęԙ\u038bЫŽŢ',
                            'ȦӰʮȪʫɵҟԊɍʨ\u0378ɾĞǞдϣȀêìӐˣĲӓĻҵˣҥǄЭƬ',
                            'ƹҵϔҔԁƣĝȨс¯ɖҵҁtǜВʄϧϳԤиŋӞɣŰԓÄɳԞȺ',
                            "ТФӱˍĪВʟԓӹɏ˝ˈȾ'˙ƦϓƒȢϳßǂ\x8dƘsҬ\\ƘҚ˱",
                            '\x9fȲǾˌɅϳǵsϟИǙǻҝԈǢʳύԖ\x8fɃ\x8bʣϽИŜкʵɰƈя',
                            'oυĨԩЃΎЧāѝ¾ёÎˎӮҢƧҞȳϐоâѲӊ\u0382Ð\x9cƽӽЛғ',
                            'żƮˉŤԌԚӢҭїӻȏʟˍǬʜ˒\x83ŇӶƥƉώĩȜeňЄCаΙ',
                            'ЖӣȣƄуԕˇԒãҀр\x9fΜǫ˽źȁӃАΆɋKÿɻıүЫɯņL',
                        ],
                },
                {
                    'action': '\\ϳӛɾƚĪԅɜƈΫŌːƿ9ϻΡƒkӦʾˑ˷\x97ӧ]īĽТχȫ',
                    'resources': [
                            'ɣèѻӸ҄ɡӫрѨɣΰōǤӚȌŏÑГυҭħ¦˲ĥPˢҬӏѽԖ',
                            'wËϮôʢǣŮª˦ΌΈäɮșˍʫҺʺϞ\x7fȮλ]цҐȁѰǅҒΫ',
                            'ȇωÞƅӱǎѯоĄ΄ɵѐȣӝńƹɫʥǥŚ҅\x99YһÍȉԁѲτŦ',
                            'ѿūҽԇϕΖћǣeԓǃԞʣȬͲѤƵƦâȔǆӳìϔˑÇӱĐaħ',
                            "˶ǺȠ˼pʪ\x8eȤ'\u0383Ë҄%ҹ1τȸɓԘʙҫĀЄǎ˳(Μ΄\x97˦",
                            'ĘӁϨʅœϘЇqϛňβћȷΏH#М˶ȕŊĐǂƴˡÃǅǿʑдμ',
                            'ΘьɋӰƶʲ˴άȟ˼íɐ҂ˈʪƯͰ΄ǑэȁԠЅɴΊŹҾ"ˬʲ',
                            'ƛђÒǩϮţοӖD˵rϧδтлʖƛųȉӠʟƻǘЅϓȠԥȽϔȂ',
                            '˨ſԘǯœ˨ƽ®ъâΝrǹџ҆ǜǦĵґǆΟ1˪ˋӀťϮѴĹÈ',
                            'ӫѮ͵YØˑӝɉʻϚѮ˶ǴΫыɋ',
                        ],
                },
                {
                    'action': 'ȩɾͻμҬŠёɖſëƤɃҿ˩Øʽ\x9cʣΝæʬʡǟĞиԎ\x86γƓ¾',
                    'resources': [
                            'ƬɑǊɦϨϗѽxӏмр)ɿ˨ʩϤѦͱϘѕёҪǻʾİϘʢČҹ˒',
                            'ӤӉÌьΎŒŅΟӌɤʦȦΑʳɞҘ4F\x8dΉ\x81ʽňѺɵʌł¡ӺĪ',
                            'ŵԦŔѱ|ίáЙԌϼΰвʆƥʞϏϴˋŐу¯ǉɋзɿ˚ьŘZѭ',
                            '˩љҊɶ¼UӜíΑ8ɁǷΦɾ\u038b҆ѡϫеűҙ8иԬ˰ÀPƘқǍ',
                            'ˍԩʹԝĊƺǈƭɃ΅ӋѻԒфǧʶȾǀªсѕǯпҳ\x8aϠФҹķǑ',
                            'ɷFĵéϝӆī\x94ΙĘГ˳ъӚˆžɥȽȾїėƯŜƓҧʌ3ē˓ː',
                            'ĤʪÓλн;ԆҪˇ÷ҷɻЪǣȋϣĘĐʋѨ\u0382ЮÌ\u03a2ÒbвƑ\x86ʤ',
                            'ȃȣҥюəƋпȊ҆Ūσõ\x82λȓɪ§ԏԑŴƬĶˊǠƔ˙ÅŷϛǱ',
                            '˼ҩцǍҦó¹\x93Ƀ]ҸȰӝÈ<ѹρӔԑȆǴʼˈȮΕ,ɻƫĬȹ',
                            'ÿ)2¥ηάɌ˾ҸǄΫНºǺιИ_ЁʜȣʦÖӊҲƮþȣ˧Kͺ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӿňС',

            'version': [
                -5231471692279878069,
                -2679920297216125945,
                -2202383843779780839,
            ],

            'location': [
                '\x9a',
            ],

            'runtime': '˴',

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
            'name': 'Ž^á\x9fѯΣϤɩńΣϽ\x83ԍΕˍɹƏÜʻƊѐɀÂԫʇҸʞǵЙŻ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'цuØ',

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
            '$': '\x96˝ȗЖɡǂǫ´ҶƵ(ѭǘêѫåʊ\x89ƵĨɤƄƿ\x8d żΊұʀĊ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 7883630085073019666,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 23767.277089292358,
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
            '$': '20210206:220914.350049:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ģ>ĔΙǚӾǿÃé@;Ї ˲\x8cԋƛԊ^ěҥӨίʭԅƌыťǴá',
                'Ūƨç3æɃӪǏԈΰǬԀϭұҗΟЁʳɃҷ_ŬӏȞ÷\x8eԣԝʝР',
                'ΠɱZѕΏϠБ\x9cʺĺӞӷԐҏοѵΙԣҴщƒÙīΐÂғÇ\u0381ΣѢ',
                'Ž˥ÀȄɢҔŘɣîԁľǃ@πӍƺˎƻθǂŤзҺҟЮћjԤɬɔ',
                'ȦӒõĂͰÉZŉ\x9bѸͰԓǊӯŀѢЦŌʀҗЦ҅ʄȖãĢÌæȮϓ',
                "υˠãɥ˴ԅëззқµӡɻ'é˱ԏʬ˱˞ѝ\\˲ǷӃĽǌǽҲ@",
                'ŠƹɾşʚƆżȽćпːˉБСҰӇдʼɋɮʂXĬɑ3nӍӯ˹c',
                'ɜЃѾҋӼΒʯѯς˰ĜɵРʎ,˽ԎʤѕkˡǆˑˎŨȻ\x94ұтό',
                'ҸӀŉьɓɡǗΖʹˬԒ҄ӞԏКԜȇϒȥȌ¬άǗԐĲǤ\xadʯɢ˝',
                'ǬďǶңȭЄ,ɗϐ\x9cҨҔѓƞˀԏǪǝзԕ\x96ǽѕχûһң˛Ȁ\u0379',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -5372649585042966001,
                -4074899677852194202,
                -3123091382211222291,
                1216451622624913172,
                -580933185036056527,
                7761566468836752150,
                5727877061954785313,
                5452591664207411393,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                739239.9051554357,
                880238.8924030527,
                880904.6781503838,
                910067.6186180142,
                675997.0899301748,
                817365.3254311078,
                2968.7258371194766,
                -95603.92708732338,
                226917.8578849123,
                343895.0374143266,
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
                True,
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
                '20210206:220914.351995:+0000',
                '20210206:220914.352015:+0000',
                '20210206:220914.352028:+0000',
                '20210206:220914.352041:+0000',
                '20210206:220914.352053:+0000',
                '20210206:220914.352065:+0000',
                '20210206:220914.352077:+0000',
                '20210206:220914.352088:+0000',
                '20210206:220914.352100:+0000',
                '20210206:220914.352112:+0000',
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
            'name': 'Ⱥǎ\x83Ә_RwҳȆƞϋʇ!рJδȟʽЇϠh˂ѬυǗ^ÓͼϋФ',
            'value': {
                '^': 'string',
                '$': '˓ѱʚɋÄȃÑҞςģЙȷҧЕƳǤɉӗ˖ěΊѴǅȏ:ԭƔМ¶2',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Я',

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
            'catalog': 'ʗҘηīԜ\u0383çEϩɉqѤʼҡӧҠèϸȢjȗǪǡĳɤÄԆҐы',
            'message': "ƍϦεҋҝő\u0378ϹұǐӆĥΓ'ƭɌǹWƬˎԀϪʊˠŀȲϗːїЙ",
            'arguments': [
                {
                    'name': 'ʃ8çϚǠƩͲˈð$ƿϕ\u03a2\x8aǮӑƾϺ˴ˡčϜzԤǓfžãÑӤ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ωͷʹȒǻғƦÉAķȋзĉɮЬρǜ÷ЏŉԪƉʃԎǲȱ˕ʿϨΩ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ТöɕҪǍѧяîΉʞˠåӊЪВ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        14827.120525883569,
                                        366775.5382347564,
                                        142363.72287663945,
                                        667171.0529369827,
                                        290856.90997145424,
                                        -2273.5695326262066,
                                        604095.244641227,
                                        -182.57947311481985,
                                        27125.182092353105,
                                        353362.1497840696,
                                    ],
                        },
                },
                {
                    'name': 'Ȱɩѻ7',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ȫ§¶ǖ\x90àțəҺłҬӟьͿҕɶӜҝԪԚlҧΫҔҮԙaӣď˯',
                    'value': {
                            '^': 'int',
                            '$': -1777164770944224047,
                        },
                },
                {
                    'name': 'ҼρĞcͳӾЪϸίAŒŉϮ¹ČΥӸ\x8fӸʏŖȆɎ˪ř3',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        748225.8218052936,
                                        991394.0759112234,
                                        129781.30138309536,
                                        582274.6796978504,
                                        858123.9662662186,
                                        -84543.79172188876,
                                        331100.29632459773,
                                        917718.7454280772,
                                        339840.2163383568,
                                        595919.0928020905,
                                    ],
                        },
                },
                {
                    'name': 'ҝϑÔ©ǭтΤ\x91ǙžóUЭҤ\x99әÒʹȭ@җaѯɈӠМ˨ξɶɤ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        689073.8881044043,
                                        36163.300196523895,
                                        928479.0126418475,
                                        777735.3641517989,
                                        -62648.641417181316,
                                        378541.04027509224,
                                    ],
                        },
                },
                {
                    'name': 'ÂɋǨԅmԗȠǾʓKғĞҏɎăΕӟŗ½ƽȧҍȼȊƽЋƥȠҏш',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210206:220914.347556:+0000',
                                        '20210206:220914.347580:+0000',
                                        '20210206:220914.347594:+0000',
                                        '20210206:220914.347608:+0000',
                                        '20210206:220914.347620:+0000',
                                        '20210206:220914.347633:+0000',
                                        '20210206:220914.347645:+0000',
                                        '20210206:220914.347658:+0000',
                                        '20210206:220914.347670:+0000',
                                        '20210206:220914.347682:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ўͽȧ\\΄Ƽ&Ӳ8ǒұσӄQӡΫC˃ԝȮϭͷüƻʾßòѹɑʕ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210206:220914.348200:+0000',
                                        '20210206:220914.348221:+0000',
                                        '20210206:220914.348235:+0000',
                                        '20210206:220914.348247:+0000',
                                        '20210206:220914.348259:+0000',
                                        '20210206:220914.348270:+0000',
                                        '20210206:220914.348282:+0000',
                                        '20210206:220914.348294:+0000',
                                        '20210206:220914.348306:+0000',
                                        '20210206:220914.348318:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ўɡԚɜφƏљǩôҌ˷цɹ\u038bʊԃqЋȔàЍѮ˦ҷ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '\x88ѯ',

            'message': 'Б',

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
                dict(field_name='error_message', name='Error'),
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
            'identifier': 'бÐΡÍʬұƙˑƓ˲ԞƗǆƂĦęԈϲȟѲ˜ɺȝӄĤɱ2Νēў',
            'categories': [
                'access-restriction',
                'access-restriction',
                'invalid-user-action',
                'configuration',
                'network',
                'internal',
                'file',
                'network',
                'file',
                'network',
            ],
            'source': 'jΟԫĴҩѸʋĚŕȭ×ǖҊɰҎ\x8cöŲǆӅԩӹǨȈЦǹ˜ľӉԀ',
            'corrective_action': {
                'catalog': 'ϕçŐѪҖ\x97\x9eq\x89ƒŢǓΚ*μǑȭЍҸΡ*ʜɥъԚȇЛ;ªƍ',
                'message': 'ȏӓº;.ϿʻǇϚ,ԊʞóŪβdӧȢ\x96ǘџŔ\u0379Ӿʪ7ίˑƔĜ',
                'arguments': [
                    {
                            'name': 'Άɂϱ˴ӡɮºÔЩŠáēϢˡԄϩ×ЛʕУӏ\x7fԧ}ϛӻѮ',
                            'value': {
                                        '^': 'float',
                                        '$': 916941.400823652,
                                    },
                        },
                    {
                            'name': ' Ͽȍʄ%r¾Άőǔ',
                            'value': {
                                        '^': 'int',
                                        '$': 8313229998878797977,
                                    },
                        },
                    {
                            'name': '˴MɦȺԂ$^σЩИӶàª\x83Ѩø҉ȩŎԕǧˣ¹Ͳ}αƍΡ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -8031714547495254978,
                                                        2169157087724799225,
                                                        933638813820694727,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȄђќѯҒιщМ\x7fζȃҗ²ŃˤƚӿĐĲĲϙғήŵгjͼţӡñ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210206:220914.339971:+0000',
                                    },
                        },
                    {
                            'name': 'ѹþǇʧʊБȶѾѧҌˣƬ\u03a2»в',
                            'value': {
                                        '^': 'float',
                                        '$': 133785.19508184912,
                                    },
                        },
                    {
                            'name': 'ɨҥЭԠҎϕΖȚъ',
                            'value': {
                                        '^': 'string',
                                        '$': 'КȯΖǦļȩəИѹ}ʻЖɰŃŻΉҳ\u03797ƒǂʤɧÃӄýɔɉ\x95Ɂ',
                                    },
                        },
                    {
                            'name': '·ǯΝƦǧ˓ş˟Ы',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ȟϡԏʋĲjďԍξĬɵ-SіЅʏϾдæůđ˶Җȟqϐ˔ηńʚ',
                                                        'ǭԉ$ѭӹWʼӋ×ƟӑӫɑȒˠǤΘсʓĨ˅e˼ҵӿάŊʭϨå',
                                                        'Ƴʁmõ\x89´ƲҢĔġåϣʗͼŏѠҍĠǓņƴ·ɦί˯\x8fЗі\x8eɡ',
                                                        'ƥǏХϵέ;ϾӄÁŶȢÊ˾˶ĀŻϥȼԩԥѶx\x85VҟȅҜ˴¡λ',
                                                        'ȏƮŐΝwɤȠɷ΅ԣѿέʄЕ΄ƂԇψкÏ\u0381ӂłĞµɻΓ¬ԏȹ',
                                                        'èƭҲхǹƙԇɛPɹӱȱҹȼśÍĀЧѣѯжƆд\u0382ɟҤѱϚȬƭ',
                                                        'ƆĈǨjǧϋұҥvΐԖ\\üγʳǤʒӿéӶǻ˳õŮʏäyɧÕȶ',
                                                        '¥χӣɠɶĻ¬ѭɕǐΧɮȝͰӶЅЮçЁǝɾʕ˫ȳƙ\u0383ʕΔDӄ',
                                                        'КɖEпþѧεΕөґ8ЈʦӘɻ˳UˈΫԛŅͱɵĹϦķѥα\x83Ќ',
                                                        'ƫáъҾ\xadӔɳĥћţΣÞȻǡǸƉĮĻѶϮȞΖ˝Ϧαύ3ȏПр',
                                                    ],
                                    },
                        },
                    {
                            'name': 'гѽяѡÓĆ\u03a2ξϜċŮČƱϿɚϱñıȲĉʏƘАΜ˪ҘѩѠɱϩ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '˹\x88~ҒȃνQ|ωǼĆϮɃĤʍԎǜӘҷ%NɇȬΖѦǣ\u0381Ӝӷө',
                                                        '҅ɵŎӐƎ<ĘѣʧӸƻĮŊàѼўǷɉȫrˇȇȌʍJрĕÊˀƼ',
                                                        'ƷÜ\x8bĀωыҾƀВˁʮǄȪÐȒӒüΓͲ˃AνžɾԠșʫѽƽΪ',
                                                        'ӏο+Ӏǽɶ(üӽрѲɖ\u038dЫρɅŇǦҮPƨƒιʛķɳɁУʖĆ',
                                                        'ǶĠϔȨҭ˯ұƼԃϣěԬɠϽŹйŽƺïгȡįϯŶĥҳͷˈΕρ',
                                                        'ǧƂњǓӄȼ˛ӱҫ,aƼ,JŢʎдΖͱNģШԖɬcε˄FҴƓ',
                                                        'ȯҸѳˬΡʉĄҁñѾӍάӼ˄ěɗѰƾǏЈŬ˥ԖȲȼĀԩѝ˻Ӂ',
                                                        'ўҧķĂęӷζ\x84ʂˊ@˜ˡйɴБĵφšƼŊʻǔOÓɓүÚϑŷ',
                                                        '"ȂK\x94;ʓЌҗҬ\x83ԐԥȒԉɻźöɃљƹĐԄϧЙ\x8eӔɍпɄԔ',
                                                        'Ҏ˽FνʪπԘʝq\x9dî\x7fêɒυηћǏǔˇΙLɂ҆čͶʠΚϟƚ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ıѯɒȒˡ\x96ΊаҪŶΕѻӸXϥӭц²ĵр\x7fЫΉ\x80ώŻвĒҍԐ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220914.342985:+0000',
                                                        '20210206:220914.343018:+0000',
                                                        '20210206:220914.343032:+0000',
                                                        '20210206:220914.343045:+0000',
                                                        '20210206:220914.343057:+0000',
                                                        '20210206:220914.343069:+0000',
                                                        '20210206:220914.343081:+0000',
                                                        '20210206:220914.343093:+0000',
                                                        '20210206:220914.343105:+0000',
                                                        '20210206:220914.343117:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƈ˙ŵ\x91ь˅҃ϕ',
                            'value': {
                                        '^': 'float',
                                        '$': 379221.1922135473,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ɽƫϽģԢѪѮ<γӐʞþɽԚǷѺ',
                'message': 'ԏ4ʀЉʛϢǙ9ͳҞǠŮӏŤȯâˊƄȤŎп˴ГԎ\x8dǖϾϗɡԒ',
                'arguments': [
                    {
                            'name': 'ѢδċȞl¾ĥêͶ˸ɱҲ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ȗɞєű˛§ɖɏԟŞŷŇĕĤм\x91ƆʗɌȦэ˨љ$ûҞϮЬĲҌ',
                                                        'ӽњѪҤLBȴΏʯBơψӿjо4Ĳʥèmӄ҂ÿȹ\x7fԝȦʩñҘ',
                                                        'ԍҵтƠrʹȮĂȸ£Ɓ϶ӷΥȓϠԫҔԪǊǣŞʆϠԬ\x82Ļу}ω',
                                                        'Ι©īͻðȰʎɛұÌ\x80ΨΨÚƤͼɵȉʡͱμϴƔҝʍҗǸ\x90ҿƒ',
                                                        '˗+qÍõĈ¬ȴʝÇʹҠ½йʡҸԦԞϒӉràoʋř©\u0382ɋ\xadʁ',
                                                        'ғЙ§bbŕϾӫԚζǱͼĝƇ˸ʟÚ˦ѦѸȫ ԏ7ɖεˏ²˅\u038b',
                                                        'ɓʥ˪ȲԒԙ[ϏϼȌŇ·ùҞÎ\u0383ɞϣȒP¿ԊȮáȐśȈSò¼',
                                                        'jΊǉÇɗâύΜˊŉʚɀʙ˄ĳʲɢЏȃЈѺzŮ˰ʩƓΧʤҀˤ',
                                                        'Râʖșϸ\x8cзƳϽ+ɹʨɌĭġЎж\\ʁϨȰ~Õ\u0383҈®ǮϦɖф',
                                                        '%ԞбɌǕ(ġԇɑ\x83БċáЊ²8ö\u0379âҁuɷŽ«ɢêұÎʌЏ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'фмԓɪύ˙\x8fHƅ¥ѧǊϹԠ\x82]ňЦÂƗ-Ҕðѵ`iрć˧Ǜ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210206:220914.353631:+0000',
                                    },
                        },
                    {
                            'name': 'ȝіЫćҺůŢƗɶ\x9fϰùzśзҬȑϔȌ\x93Ҫҵ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        80617789326998637,
                                                        -6602555248136342447,
                                                        2167951726134838495,
                                                        -2867113237332452488,
                                                        -4090631657574195421,
                                                        -5008609605313081184,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǗəϛķŪğQƪҢεь¦ŗġʵ0ĨǣӾȐԢŖЃҕ-¾˰',
                            'value': {
                                        '^': 'string',
                                        '$': 'rĿōt\x91ːΒŜ΄ѨÃӶp˪вƦkуѻȽʶóѭԘʬ҈ȭȞµϩ',
                                    },
                        },
                    {
                            'name': 'ȺʫǵТјƗŗƄ˷ҀԌ\x85ҋҫǖͺицϫǜũ˷ӮɹƻӋұçƃǢ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '\xa0ÑǢǠãɫϿΑŗłëȝŹŤɒɅŤʀȀöŲѓŽ°gпźɔJӘ',
                                                        'ƦƂΆ҆H¼ӒӉɝѥ˕ʷҨŗΐ\x85ˆEĨĠҭԐɩПҠŵƾϒɞҭ',
                                                        'ʫʽӰɱĩĪϢϏҋȃ\x9dΐ\x9fȦʚўђЭԧѷŐӕǥԠůŲΓĮƿϘ',
                                                        "ҭ˞ˣǖ\x87ƷÎ˻'Iâʬ\x93å\u0379(ȴūɤʍ£ɟiƹǟ>ӣΓ\x83ʈ",
                                                        'ɳLѬ\xa0øȖïmɕʞĵʾʇŁBĤƍɟáѕчөˀҚîΐ}Ї\x82i',
                                                        'ƴΪΨҝћʞşэ΅˹«ΨǖϩɨŘɩԜɀƩɉɌŷҊӂvªSѷŌ',
                                                        'ӣԫҎɞŭȶӔԦҪːҪӿͲԄŅˇÚŐŜƠɏўɹɃʊƋяëиǿ',
                                                        'ǀňҮǞÇ}ǉGƉɋ\x90ΕÒEМӬŢʻ\x9eǈ]ýԨɻКɽЮӣҠԩ',
                                                        'чÔƵǋȿĢюӶĢ˄ØŰĶ\\ΰМӪʰĊҺǣȜ˛ӮÞӾ°ùжʴ',
                                                        'ÕòҫöwȟҗςӍˆʿԙόС˰%ƁˋС҇εсыήʁƯ+ȱͳÏ',
                                                    ],
                                    },
                        },
                    {
                            'name': '²"Ĉ˞ƳҢˤΥѧ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        130061.21899013355,
                                                        58988.65455902566,
                                                        916694.696392637,
                                                        834781.3049903967,
                                                        712383.875525414,
                                                        83744.17936560264,
                                                        500783.1769797753,
                                                        227759.09698549606,
                                                        281642.3634106255,
                                                        642255.325697654,
                                                    ],
                                    },
                        },
                    {
                            'name': '\u038bÛƂЄĳËόǨ&ԔҢǠҘϐ~Bэ¥ӡЇnő\x91ȢҲøэɗĄÙ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210206:220914.356379:+0000',
                                    },
                        },
                    {
                            'name': 'ψ\x9aɍȅƉ˽ЙӟīӎɺΛѹŹͰǶӖĀѨĘеȼŞȆωƹɫˉɀÓ',
                            'value': {
                                        '^': 'string',
                                        '$': ']ËˏͲύ΅КȰɈϘňǎӉЕƌZŐуȃΒȶ˸ŋĉĈә:Άȗц',
                                    },
                        },
                    {
                            'name': 'ћϴϞÛǤ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ĊӧӻØђД˶јҰҖǺ{ѭϪǋѴ]ҾԎUԒÔƍ^Ǣűɹӿ^Ԝ',
                                    },
                        },
                    {
                            'name': 'ōɹˠѶęŶưƁģǰνͱʞϐɇêԤ{U',
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
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ǫϑÜЌϥ',

            'categories': [
                'network',
            ],

            'error_message': {
                'catalog': '1®',
                'message': 'ɗ',
            },

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
            'name': 'ԣǹŌÅӟư˝ӂĈ\x96ɱĞʑûēŕ˝юǘӿ²ǴѵˢԊαӼ½җС',
            'error': {
                'identifier': 'ˍJ5ųξѨЂӻȭɦ$ˉ\u038bԂʯÁӍɅϵǇȿƥӭцҝΎҟ˙ԨĀ',
                'categories': [
                    'invalid-user-action',
                    'invalid-user-action',
                    'internal',
                    'invalid-user-action',
                    'access-restriction',
                    'os',
                    'file',
                    'configuration',
                    'configuration',
                    'internal',
                ],
                'source': 'űӘϱŵθ}ǝʎˁқԃȻтƠϭǵĬ6ȶ\x83ԐѻƅћĉϸйΡĈɲ',
                'corrective_action': {
                    'catalog': '-ŞȀ\x84ƀǈƤЬęӨEʔ1\x89ɢƬ˛ϕКàӍѶĪЌɋϐҖɌźǸ',
                    'message': 'ҵŢѼ˟ĘѱĕΑ|ǧɗƑͰƇӥˋͼVӬùüĖԥĕɝПКԍɻН',
                    'arguments': [
                            {
                                        'name': 'Ȳϋ\xa0˦Ӆ˼£ԕ˘ωƭΎżâ˪ӈЩȦІYĀĦӞśˌͽϼěѶ\x94',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            387793.3266049085,
                                                                            838882.0927067669,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƘҳͷʟτʙűӝɷҤϗΔϺͼΛȚӆėĿģ\\ƃ¬ǋàɚЪ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ұɂ\u038dʖȞɵ|ӏӴ˭2ëӅƀĳ0òϺсðψƧĤǇ˫Ҋ9˔ѯҦ',
                                                    },
                                    },
                            {
                                        'name': 'ȖÔўнǬцʋkįвĚίҗӠάύӜԞԝѼʨн',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϋȵԡж˕ǊVɴЌşАҊѻ"ƳΘӰǿHʭ/әӛĥäДŪʙǮѺ',
                                                    },
                                    },
                            {
                                        'name': 'lʣǿШʥњ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '|',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x8dς\x84ōț˔ʦnğ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ΓϗĶÓƣϦǳɒůĞɣ§.ǲԅȫξÝѭƒ¯Ъ¼ȺιԋΙɮƅ\u038b',
                    'message': 'ƻ(ǁ,ŜñɭŶlʝʔƲɠ˧Ō\x99ǢĥЧƏ;ʔǚ϶ӌΕˮɷǃз',
                    'arguments': [
                            {
                                        'name': 'ӈZҘùƺpǀ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            445797.0777341125,
                                                                            868997.7760893676,
                                                                            742699.6503219325,
                                                                            12036.067304836499,
                                                                            351684.5021416267,
                                                                            -86541.09461952191,
                                                                            51835.04092823266,
                                                                            561872.3609178211,
                                                                            -43153.903131155246,
                                                                            200298.11041204788,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĳ Ƥɍа\u0383˼;Ņ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x84ďˁȿӍǆԫӗʫšϹчСӛ«ҾŽӅԡЦ`ǽð\u0380р<τƕÄʽ',
                                                                            'Đ!\x83ȅӱ˹҃ÂΰĕęǀčНԈ\x80ԫƖɴϣʂԚҘɳǮӏȾ)Җƶ',
                                                                            'Ø"ĚЁaɆŏȠєϽ`ȌĬϑӜϗǟӯʔɵДʗĄҽДΛ°Ӱğ0',
                                                                            'P˷đѢɏӗԞɥĳΎϴêѝϾŖÐϬćȽƮѭʩǷɫΛ]Æʩһȇ',
                                                                            'өΟӹŇԄԩѧőԙžҋΤϐǟ\x9aѣˎ\u0379ǮƦоϪƨĲӋTнʴDȃ',
                                                                            '\x95ȮɉǋκҗЫŧ˖ӾΏøʯҢɀҏѿ\u0382ͷǙυ=ѯɄ`ʾԞɇ[Ϡ',
                                                                            '·¼ǜȡȶòȲԪВŇʔҰŪµʫġϮƫч)ϷĦȣĆчЄ\x99ςЕӜ',
                                                                            'ҖϷԩÆŕRξʉʭѮѥ˃\x90ϟ˂ȲǿʹɳϥɟÕǕԥÐĈMȍˠ°',
                                                                            'ϡƙӤΒҨАƩˢԡԢѽìxʼǥɫȦ҆\x81ɇԗ\x88ȳüϢǉʼʗɊÍ',
                                                                            'ŝȜʥЊʏοËӃÒěşɨė\x8aʻ\x99Ħ\x89ҳʦɮǏЬϭğɣĎʁбņ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǵVўа΄ʆƅϕͶŷȐҺ:Ɠǔľˤ҄=ǻÔԜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220914.335666:+0000',
                                                                            '20210206:220914.335842:+0000',
                                                                            '20210206:220914.335854:+0000',
                                                                            '20210206:220914.335861:+0000',
                                                                            '20210206:220914.335867:+0000',
                                                                            '20210206:220914.335873:+0000',
                                                                            '20210206:220914.335878:+0000',
                                                                            '20210206:220914.335884:+0000',
                                                                            '20210206:220914.335889:+0000',
                                                                            '20210206:220914.335895:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŲêƈɇԒƉʖ҃ӱžŮ!ũuкӶŷѲȥɆԖ˨ϵį¼ˊȯͰԄÉ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2371195632569806833,
                                                    },
                                    },
                            {
                                        'name': 'Ñ^ӯѨŻƾӒɼӁǴϹԌҳϱŊ΄Ľ˺ΣȖ͵¯ΣԂƳűʭʳŵʄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220914.336337:+0000',
                                                                            '20210206:220914.336349:+0000',
                                                                            '20210206:220914.336357:+0000',
                                                                            '20210206:220914.336365:+0000',
                                                                            '20210206:220914.336395:+0000',
                                                                            '20210206:220914.336402:+0000',
                                                                            '20210206:220914.336407:+0000',
                                                                            '20210206:220914.336412:+0000',
                                                                            '20210206:220914.336417:+0000',
                                                                            '20210206:220914.336422:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'œĂ"˃О',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'EȖ>ƱќŐã˶Ϭ҇ȾТɥʾ˨˄Éʀ¸s%ʖɓƓïӀƐєÎφ',
                                                                            'ϓȯԝ҃ƆɩîŮѧΧɐǧȔƁ,ҽùpŌǳͺʚөƵӭҎЕȟТĪ',
                                                                            'μǈӉ\u0378ÜқʺãӡԭϞҬȾЪԥԋ¸ŒӟϔϚ@ȭɛчҢƂӲ҉ù',
                                                                            '[Аԍǉ\x94Ҟ)ЀѶȈԥɸϢҭҊѪҹ´ϟňƘ³ҡʲȳ\x8fЄԑϗҔ',
                                                                            'ѳͲǥȳӯχΊҵӬƦΆѹʪǖéǧǻnĝWqӢ}\x85Lғ×ȟҡҰ',
                                                                            '×ŻƤēƕÉ0āЉŴψkɭэŦǅ\x9fʰńȬϼ\x97Ī¶ЁʼƵ\x99ŕƊ',
                                                                            'ɩǴʤόҟЧ!`ˇɋƞɐƍʖҭÆǴԤЯǡAԮɰMϒ×Ԇü\u0379Ι',
                                                                            'ƃ$\x99ΓƝ\x9aǵҐʴҼԛɍ˟ƁĞĆȩɏÈϥυ5ŬŠ±£ˊďň˩',
                                                                            'Ȑ¶ĪĘȣ\x91fёҪŦĤĚρмɉЮĒʾlͱϸΙʫʺôŅΝυЙΙ',
                                                                            'ԥ.ѰìƮʹhѼńϬƦϪИɓʱƖ˺ƩХӈǯЕϭԢßϡŉҽƍǲ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Jç.\x9aͼ˷ҎДåҘŗKϭʵ²˵ӲЫˠΔɰОȓƷ©ƕ5ǂ/˷',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '϶ƼӑҞѻӦǵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 899334.4823620401,
                                                    },
                                    },
                            {
                                        'name': 'ӕцβŁѢЩԝǊҾԮˤíҬϐͶ˺ȥѱɉҢƖɟǉƍďӆèĝҕˤ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɺ\x944ӢwхʆӲяҢӻќġ˒рĥҡǺСϫЇˡƷ\x9fсæŜԙ˰µ',
                                                                            'ƀÎƁéϷҙǷѡΜҞ\x9d\u038dШпˏ»ԜԜŻӝдĹŧ;ƄӵϚȓY҉',
                                                                            'W˶ɪтҭ\x88ÙѯˏԃˮЕʲа˓ДÇӈιʝǠÏʏɥ˰ɾυѫǈϖ',
                                                                            'àȾԓіθēƇnǏ¥NϜǮŪʜӕQЗɱpȾҏҧӅˠ£ƙȢԏѤ',
                                                                            'WǃӾʶÃʂ÷ʊʜԥˍʱȔƈìҞBˆȆ|ѲӘƐ6ЈΗͽ{Θ<',
                                                                            "ɗЩȟԖȠ\x89Ѩν]ɦîȞBЂˣ'ɜӹǃ)ʏџġӣĚmӍ҉ѓ'",
                                                                            'ƊĶё×a΅ȹǣҰįѐĸD&qԏΤАʆΥҜχЇƽǖӸCԀļl',
                                                                            'ȍÄЧѱ!ўԛǴΊηӋŔǴҧʣĕɺȳѨȁȆуøʬцʫɼġχЧ',
                                                                            'Ɋӌ_˒҉Ӯřˁ\x9aЯɻćʆňųýԍƔȩмˬǚȐ\x98ˎʮїʞԫ\x7f',
                                                                            'ƦąѠŻӰȈȏŒĒϠɣʲɏťά˗ǘѳӜʀːĪҢızҒυĆ\x9cɒ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '?өůȮӹǗƮR\x89\x8eЍʐrîғŻɤʉȫʇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220914.337895:+0000',
                                                    },
                                    },
                        ],
                },
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x9bĶ˚',

            'error': {
                'identifier': '˲ҭë¶Έ',
                'categories': [
                    'access-restriction',
                ],
                'error_message': {
                    'catalog': 'ԙɓ',
                    'message': 'Á',
                },
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
            'event_id': 'љ«ϨĠпʬǅѦůϟƹҪǢΥÿˁΐ˽ÃrЇ6ÅűҁŸ˓ӇӃȖ',
            'target_id': 'ΣШǁϩӛϝʪɘȪĊώ[ΣɁ˄èƑϰˌĴ\x99*\x93ϒϥԃϥȈƢ˛',
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
                    'event_id': '˩ҼхúŠźɑц½ԣӇԨƟԊɾŬӰ÷ĆŤϷĈ¡ҹˊĥЍ¦ʙâ',
                    'target_id': 'ҠȼЊʨ\x85˂ƻʜĞŹ,·цƀ,;Ԧȩ˴ņȲ°Ď˴ѮщљΊӇϥ',
                },
                {
                    'event_id': 'Ŧp\x98һʕȏȫΐĲˊԆʰԟŃǄҩÕ¤ϰțҒЋΪʋӽ\x8aĝӐęЦ',
                    'target_id': 'я\\ťŁɩ˽ιҾйЏŉąԘӮy˾Ԣф˟ʿ\x99ȑƐњάȘёГÝӖ',
                },
                {
                    'event_id': '\x92˺ҫӆ˩ǺɩțԨαϏ¼\x99ȵΌϪɩƳїʥƞΫʛĩLɶơˇҀȴ',
                    'target_id': 'ӴͰȮ¡ʩӾӰʝхҿȲȎà*ʈĚѥӷ¨ʧΤķҷUԬ\xadӋƝ˻T',
                },
                {
                    'event_id': 'θɪѻЛǴͻЍȜĮĭλϾōψҤϿеˬΊϜĬІ˨ſu±ʨϑĀ˪',
                    'target_id': 'ĜԪ\u0383«j҇yϛ\x8efӓҔšQžҰԑˁҦʥCѴƹĄ˺ɳϭÕɃĒ',
                },
                {
                    'event_id': 'Ψģ˺ǺӕŚ¤éЋƒίțÉȷïʀ¨ʬρìƖοįʌȗŇǮ˰˺ͻ',
                    'target_id': '\x8cΖȣѽ 4ɤŽқτςĴǚąʢªͿҔӽřӕȦdǼ˧ξӱÕϫŧ',
                },
                {
                    'event_id': "ɯʞǳȪƎҮў\x8bɜΞʙƬBť=úʷЃ<˩ƛư˳Ȭώ/ť'Xϧ",
                    'target_id': '˥ϥȎıǛτϹŶѦĥǿǁɌԬƷӸĤԊ˰тřȃ§ωҁļԋÆҤΟ',
                },
                {
                    'event_id': 'ÞěҫťȬȕʫļӏǻEŕ˹ŀӷˢʩώ\x83ρŲвYώƿѤʯÒε˻',
                    'target_id': 'ѳːȃÿҩåŸƷαЯˁʶёɋǋԁkϢÌԀюʌɭңďä?ĩˌͼ',
                },
                {
                    'event_id': 'ӇkȱʄɯöȲϮɜĘλΖέ\u0381ΎӬ',
                    'target_id': 'úҢʋѢNυʹĉȸѯ˱ƃӻ3Шáό˻ˉƋƚЅśӣȝǽÉˤŘԋ',
                },
                {
                    'event_id': 'ƈјĊĉȆě˭ԁćêДƎ\x88ˍųʉ҂ɞÇ¯˧Уǣ·ӼԆüҀ\x94˂',
                    'target_id': 'ϜǛѻ˗ǑԩƟØϨÓɽӵδяыªÉ\x88ҭГʞʧǙѐѓȫƱʺʧʾ',
                },
                {
                    'event_id': 'Ⱥўδ_ǀΜȉҲöĎԆƻ5ЍɯoȲӆǓȲɡȑ\x9c\u0379ʗѷǈĦɔ˓',
                    'target_id': 'ϬĻǹ,¯ѦĻэ˙ĤːƤӴ8о!ƺȟ\x83ύ0ԦȻ\x87ѮśŚÇ˪ˬ',
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
                    'event_id': 'ͽӚhΪʗĿƶǋфǅѸǾż҇ʭɠΕ¼ǮǿȠū҄ΐģԙӡ˲θ.',
                    'target_id': 'ũѨĄáĥɡ>¥ā^УӡϱǑϮƌѿφϯԩǄƊ{\x8cΎγřӓȳȜ',
                },
                {
                    'event_id': 'ɰĖòԇщǌұ¢ˆTȮԒçǨѼȂǀψäį³ҹ¿ĩϥҲОˬ˵ͳ',
                    'target_id': 'n×İϱȋĎӊúрŒȋϓѵ#RТԐƵέɢǂԐϘŤĬˈǆ\x88b;',
                },
                {
                    'event_id': 'ɠ²ԀʢGϊȱдʨҌϬŚԔ˖·ƒ\x8fЈÅÏÇ˶ȦƑˎ҄\x9cћǊʕ',
                    'target_id': 'ΥŴÏƵӦɌ҆҉Ý(ȼȇȳ\x92ȞWӊǮ6-āΫːıƨǧϢƃǜ»',
                },
                {
                    'event_id': 'ų`ʗλŇʳʕ¦ЙʣķɅƠ3ƺĜЀͼ˱ßӊЍ˛Şœԙԉʤʨк',
                    'target_id': 'ȃЈȑʗѳȒδѾʿġϯČėĈӰʍМȃŉҿèčŀΫȫȎϟŚʜʓ',
                },
                {
                    'event_id': 'ġiͽΜʧ}ʦɬzЙ%ǍΏδɳ¾˨ϪЁџŕȥ˰ң\u0378ȒȄӿè¢',
                    'target_id': 'Ė\xadДȴҘÖʄԝϸĻ˫ʱ˄ҜϥѯΊćΦȔ/ͻ҈}©шʋťɷɷ',
                },
                {
                    'event_id': "ҽƼQϠʑÈǪȢиĲ²ɼҨ'\x97ĺȂwńԇ]CΖ΄\x90ϘЫÂŅʢ",
                    'target_id': '\u03a2ʖȾ³\x9cǔeĔÉȟˏҜϵ»ҰğčӮϓg҅ǨˁÚӉȵôѥț˖',
                },
                {
                    'event_id': 'ҫņƗ҇еƱҪHɉіþũɇӃ\x9cĶ/ƮСҺgĐȈѕÉЛΐӂN\u0378',
                    'target_id': 'Єɡφƒʦ˸ӎҩэʫµkɄûЛǫ¨ïԔҪӸЬˀɺҗҠθǔğŬ',
                },
                {
                    'event_id': 'Ҳҗß˗ɽ>ƞӁԍїƧӵЦǍЦěʑχШѱÎԠԍԠԈˈȁƴɡɽ',
                    'target_id': '˫ħŗŃÁÒ2ѐңӥĨΊԧӕѐȆөԚӽώҢǬүмǙƇӧГͺƪ',
                },
                {
                    'event_id': '?υÁÌΌΒǴ¦ҐȶšЭүĴɡΪΉPСƑҙƃыԋϬÍɱЈÖӲ',
                    'target_id': '˻ѢiԨɦÄюȐį)ϵÙљ9j˟ɺʃʁăʴȘғϜĆӀϾеҮʹ',
                },
                {
                    'event_id': 'ΚҙɺŠ}Ф˕çɒǫČηÁēΩ¬ơĽʤЯϦДӥƎ+ʃ˳пŏś',
                    'target_id': '®λļҶĞŢ%ХгeЮΰěåƌʇ˳ΆʁГtωŞ%ӹƂϨƸɉÃ',
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
