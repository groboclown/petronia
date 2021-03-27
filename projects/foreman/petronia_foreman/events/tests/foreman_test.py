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
                'TȝʥʨͿȡЄӇӏԁƹΏņȗӶ\u0383ǣ\x8dʞȓˢƋƏԩĳŖƁŘ±ʸ',
                'q˧Ԫԓ ӨŅƝԞƹ˅ÍʧʭŖđs\x9aμĒŶΎĠ\x88Ƚ\x9ećѭāϨ',
                ',ԝіԦͲҽӛʅњȇŶµΑĊˁž϶Ĥʅɇҭ}ЏӋŶȍˑšѐǔ',
                'ӿ\u0382ƙ\x87ɴОӊʼӂ˗Ԃ϶\x9aǠ˴ʜϻ\x9dĪǃԨƙ\x7fśçƽ˥ӷ\u0382Ԕ',
                'ЁBʠТ\x7fɻÙ҉ӟЌӰϢ˂ѠБğЎYЅԮνuŕξӝĩуȧӏƒ',
                'ňЭԒôɷцβϞЏҡǉ˃ϟ·ǍϕӪý§ϙŸ/Ƶ2˵҅ɫǸЛ¦',
                'άιȻдȲʈÿѯǇөv\x87DƗŗqіďƨˏǣҲ{Ҏ˲ƹƉϥʹʗ',
                'ŴԪýΡłάƅԂԂͽεғ˺ġ«6ȼ\x7fŨțӻѺВЊҧҹԃ\x80_\x83',
                'ЂЇƍŉ\x88Ѳ¡\x87ӰҿүѭƽΎĬŏѵˀǥҌӃ£\\Ѡõ\xadIȖwÇ',
                'ЅԊр¼ʚ\x89œƗςȘɔȕўѕҏϨбԌћǰŻԍĜ±òŵ»ðͼǭ',
            ],
            'source_id_prefixes': [
                'ɟЧǶĠëƲċˏŜˉëȱ^Ð˪ȓЎʹѶѣоĞ¹ҢÉўИŷҖǂ',
                'ŗκɫҗȺ˰ˆʘ\x95ˈƅΒԕηцԝƊƺȼƒʕοΈXʉѲÙƤʆӽ',
                'ԟ\u0378ϓǸ.ÙǭЁįϹßƺҊї˖ыҔ¼lȫӘŎǲȟЛĒÊǚУΏ',
                '˹ĳ]˘˵ÊNǶѳѦŏӑϲҔɈçŦʫí"\u0378ĞʴүŠλВҰȵ˄',
                'ɨƕ\x84ɾ˷ʓˬO\u0381ӟҟӟʔ\x80ʑЕФӿ!ԝĻʔ\x9bƤZ»ɤ¹ӻƸ',
                'ԓɚĽѺ\xa0vɘԙɊǵƠƓeɌǿЭŏӸF9ƚïúÎͿʝďǓ҃º',
                'ȅȒĲˠѥ¾wτ\u0380hƧЇʥǫщſσѤȾ³ψʑ˖чǮRĴ¥Åƿ',
                'ˊШʽ*λnòԤŎԕǓλǗϴȗȇÓȪΛԕШƕӐşΙȚƚчı£',
                '҃Ȕƃzł˞ҪǀˠȔЁʊЌĴòϔˌԫńҽ¡ǢЌЖǦȲȡΊˬȄ',
                'ƭ˄ѠүеΑϒʔȡҽO˳țƐ4ĵȂ˲ӡ;ăĻѹсХђ\x8eƿ˝ӳ',
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
            'action': '҅Μ˺ĉòͿʆµъϕФҽљҡƐςͶҙƪмϣȔƍȉӋɉϼR˞^',
            'resources': [
                '˲\x83ŌųơȳȱŠћΗϪӖʹǑКŁδĳˆλ\x98ƑӷƕϙʞŪѢԒѴ',
                'ЦƽэDћģ˂ŒŽ˾Șä;ȠƌӴǴŹǢŃφԝӭΜ«кƖ7ǖԝ',
                'Νзԁό¼ǇƓȠӳӍĚЭҲЏ²ĊżȺʸĘϔӷ˥ĽϜҐԉɮём',
                'ǂș˚әƾңɉ΄ȗʑęԢɗƕѠ\x96ϺҹʸоӦԐȕяʔƱ¸χȖ¢',
                'нɚaǋ´ÛȎєөǘҲҦĞ\x9fШȸɮ˶ҳțʣѳѬΕİ\xadsнѿȑ',
                'ѭ°ɋ˩èӘҠмѮĉƟĐǭҒ˂ҫ¡ǸΧӳǟ˜НΆŅҭԩľ¤˨',
                'ŐѤϦϱͱÐʬҬϮĉӕӯзЭѮΟǔç΅ĸKWïöŖʻƼj\x9dƕ',
                'ˋ¨eηƢF҄ǁóͼѪĭБŇǱϧӢȜɤƦɄɨɋƱѼ˝ȀλǧǓ',
                'Ϛā[¨ƴʸԬ',
                'ʂ\x99ðŘ҂јԮлȕˈЋ˯éЃĂуȈ΄ɓΎ\u03a2ΧdӚА@Ҟѩсϔ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': '\x9f',

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
            'name': 'ěGӄϝΌȝʡӝЊǡǾΓϼɵӸxƼԕ×ʎΰˣИ҂ưҁcѻʎģ',
            'version': [
                -890858374102824270,
                -8214178435782695250,
                -6618697972938884632,
            ],
            'location': [
                'ԢҲҼԢĎƭѮтsѴͶìʔˣԍýҕ\x7fȂҊ³ɵŨЙ˥ΓʡȕҰH',
                '˞ɄǥƻͻįȲʋȂˮĳӒŏϑʡ˘ӌφǘΛ¸ԚҮƟǳĒҋгҍǰ',
            ],
            'runtime': 'Ѥ<ĈˠϷƑ[ЮԬѰĹҮ#ʊȚӗɞ\x94ɣԎ¬ƫ˔ʃòĦ˅ŻƮƁ',
            'send_access': {
                'event_ids': [
                    'ԪВǨЩҚɫɽǗҖ',
                    'ľʨFίÒǜ>:țѓ˱ͻҡ¾Ѯ\xadѥӊДɛƂҀ|ӂɜˆζʙɢ˛',
                    'Έ˫рȎЖ]ɣȪħűϰӈȫȭȘĠ˧ҵɱϭĠӰÒóʐãªӜԩЀ',
                    'įЯԊҵπͲϔӭԥS\xad\\ϧÙҮȨȓȔȪ#+ĻϘвӣѥӪѵŎ¸',
                    '¾ʈѶ\u0381ʆԙμǡүǿԆтśζϊǸƄƽːĖҫϙξћň\x97˰ԫnϰ',
                    'ȈΉБīƤÿǨґſ\x8fˁǃёª¨ÒǕԂңʀɮˁȎʹǉʣӚɆҡʘ',
                    'ΈћƘśȤ˜γЧї˺ѽҨʐ˸ӦхôĸơǠɋΔǉǃdʡɍѱџЂ',
                    'ĲԫɵϡeĆŧºԍ\x8dʛƐǚP˅ԌΣÛͶĲԆ҇Ψ\u0379ɼǧǂΨuľ',
                    'āϫʚļ²ëÀѽіʷɀėƬƀҠřSҪэƳ6ǣҠ«ΪǏƃʵλˏ',
                    "˓'ӛέʥ\u0378ҡɫtĔ×ǦöϘΚÌԜӷɂƁӁЭŐπōȈýąτț",
                ],
                'source_id_prefixes': [
                    'fưϜϯεÑĕęЄѐkѿǟҋԫƽʉϳϞ϶έɌνˣȀЦԁʍʹѱ',
                    '҇ǅ˾ȗɡЉӖӑϢ6ǗɇӐˋРѾЬńϾɠԂӝʶ÷ёԬɞІԈЕ',
                    'ΠчŇŠԒѾAԁТȁЮñ˰Ʊl4ЈéȁрɾǥŽѨȉӼͼЈ҇Ĭ',
                    'sҪıÁˢʡYιȹaɠԡģҷӼE\x98æɔӜ\u0382ϰТƠȔθПϙ˺-',
                    'ǬȖĘɒʥ',
                    'ϘƽÅѲҸ\u0383ƚӦÍƾѩρǇԂƮȊü^¹ȔØƗӄȯÓϮ(Ũӻĵ',
                    'Ï«ŸʲŅĚ',
                    'iϚíŁĹШʃͷϝɘқąԔI\x8bΗɣ4ЧΟ¼ĿĔΈŻҞ\u0379ǯӡй',
                    'ȮђдÚÁӆ¡ǐ¤Ӓ§ǑѶRгρüÙϽÔϵʧϫǨį%Ə´еȋ',
                    'ѪΟӂΙɪɟζ¢ĪɔĶѹŉİΆGȏηƣӶӃĈĐӞʣҲǮŏȓ0',
                ],
            },
            'configuration': '*һʿ˟ϧӱʡȣԦ)JBȋ˩0ΗăʡƺƂò\u03a2ːӡÜƄȩϷÃҽ',
            'permissions': [
                {
                    'action': 'Β˧ҋƕƽɬŨuБƹГҢ#Һіgíȟ',
                    'resources': [
                            'ƑΊäɥůĐИɴļň\x9aҧƩόЌɖB˴ӨŌАҐӥӗӭGŌą҅Т',
                            'ßͱƼ]˨ͻ¢ĦʛΩшԚŁʮόԑЖӒǍȟB҃Ɋ\u038dҖ˖οɛdҞ',
                            'ӅϵҌ\x8cnгÜҍţțҗƝ\x98ǖƪČѹƠΕůƓƆƌɍӷӉԤԡS҉',
                            'ɨѦʘÃƓƺ˹ӻˇӏʀƠИ˸áȘˣ˂ΒɏοGyМЊȚԄˣʎ¿',
                            'ŏÐĞɃԗϖȺ3˂ϯӰϷTsŀӜƼÎївĖǉҙǲщİɬϬ˖ʶ',
                            'ʀɱ˘ΩҍĲŪЬȖсȣǃĩӿƭ˥ľθĽϮ7ҺαĳƟŉ/-Ҋύ',
                            'yĮίéǦ-ſǡŚЪʷԇ˝!\x84Ȃą˝ԤӮρŬԈ\x87ʾêŅiϹǻ',
                            'ХʴɂģԒԈŰлţƢˠ\xa0ӟҼԉLȣќɈԇӓ˒фπĉ/{ӆƔǈ',
                            'ΉҠʗыӍȔɑÚŚъӳť0ɾȆΦέѿ\x9cӋŲыϪҌЧԪӯèǢԈ',
                            'ԉҒŶʯЗƛºŦɷɤȐұƚłŠ?ƀǸ\x85ǿФѿʯĢΚɼѵ,ÝĆ',
                        ],
                },
                {
                    'action': 'ӜǵōĈӉɟņʮμӱη҈ǝǓя˾÷˻ԘŞ˚ʣ¾ɽԬѩӘé˭λ',
                    'resources': [
                            '\xa0ǊêΆ΄ƽɉϗεΙ',
                            'ƼōҘʹ\u03830хԄǾȿӸůSȍūθƹ\x81ˍ±ԥҜњԫԕʯĕʵőā',
                            'ÂѨ¼ѢʿǇӭɼù\x89èũɘԤƶŇǿӲ˺ȰѱˡҧMǿɏͺѬ#Ә',
                            'ͺȁƠeˣȾɈΘЅǙ\u0382ȓƬKʑƢϮғѭӇЉˢЃǏҽɱǺȆ˪Ԋ',
                            'Ѥӵǵ\xadŁŎȰăЌÄɼœѩ{ҽӄɺʄӧǸŝɐϗά\x7fӅ»ҴƋÅ',
                            '1ʢ˺ѢÃÊεhʓȲ-ЉȮŐԫ5Ŵ˽˯÷ȃȬ˵ɲͱ.˂ƅѳб',
                            '˝\x99ÒǼɈҤŷ\x96`\u0382з\x8aΞņпxæпҴɫʄúȎяǧȤЌΝ˯Ԫ',
                            'ЬˮЉğĄΉҝҝғίʢΖ˝ƞǃˮѸȅВım¢ȼɎĖБʎ8˻ʆ',
                            'ȦɵɭφɟNɴxˬʿҎχʺʣΕӠË\x8fіΠˉѡɟ\u0379³ԟŲ˖ʋԎ',
                            '±ēʂЊÃÖϓχʺӟΌǭӗȶɄFˉÛЬȻêϋʎМǰɝǨɗδȭ',
                        ],
                },
                {
                    'action': 'Εúҕ ]ԔȂ±ʨ{ºþΓƚ˙ıêŅӒʏҿū˵РØőԃӍӾƚ',
                    'resources': [
                            '¸ĈњѾԔσ|У˄Λ˂ҭƷƶȬҋǢŞςĻJɸĉЭѷ΄\x8cʈŘƜ',
                            'Ѡîˀ)ȴÉТƻƞҏˢϹƃȒ˚ΠȷɐЀҿç˰ϫǁԄŰɾ҆ƛ>',
                            '˅ʤўʛқȣΞŔǛΘѳłΖȶґȚĘи9ƎʍƎпáȫ:ԜӜѡП',
                            'тͿԮƠԅʔӜĬБїȆŬӺjϖΨĽӒ\x9aиƒōѿȔͼ˦ȉƔӏÅ',
                            'ƨƑ\x82ӬǁV\x94Пŭʋβнрθ\u03a2ŒΧΏѳ«$zѢҁͻùӌɾʙè',
                            'ӽșϥӲŝÓµ˓řˮ9τĽ΅ǥА˜ӬΰʫɒÜˎǦҨÍǠë¼ɧ',
                            'ƾЧſ\x88ȡǧʃ҈ɚpяİgѪƽ˯KʱԊȘԗѮτΘǜɚә´Ƹђ',
                            'ҦжȞѫӹĆǼύς\u0382\u03a2џȷГЈƯŶKϓǓɲĿŵĴŦΡСͱͽt',
                            "ԄƪγΉҚįňǨϗӪțӦŎΙǇāϸÃӹ'ż҄ӷѹ2CМǀÈˇ",
                            "ҹÃ˚Λėƶ\x97ͽÑŖ^đŖǙǭǯԩÈωʠ'џīΨ#ΙȾ͵њӔ",
                        ],
                },
                {
                    'action': 'ŤԥĀ\x93ɆÈϺòǰΥѯʈƸˋϨřӅўθȵҒǛԞӰ΄ҐˁȐwς',
                    'resources': [
                            '\x9fȕвͰÒhϻʻɜЛњˋх˧ČȾȇčņЧÄa˭ϐZКŎӗČǳ',
                            'ϙіȋˍÞΕmʜ˛ĵt)ħѧ΅ŅЙά΄Ʊʺņ\u03a2şѫ¬ȝѦēԫ',
                            'ɟȃÞÙȮϯʣԙśȤǲ\x91!ʍŢ1ŲΞHȂşҺѿͽǊΘҰ%ɉҺ',
                            'ѿƟgʭ\x98hσʝɷä¸ӶĖŪǖϿÂȼŘǲȆǼɨХ҇\x92Ѥв\x90Ò',
                            'ѭ\x95ðɥӷΡЋѴ©ʼɄƥӞԁűϫ\x8aӤҋɵʬʃӗʫӂƜƖȋ\x92Ŀ',
                            '!ǾLΌϋ˾uɈοĂԜ\x92ƭӥѕɩȟν˵čĀԮ<ɓ˂ù˦Ƿƅå',
                            'ЬВhəϴEÞάϜηʙψřȟ4Rέ£ϦǊ˝ɤÒл3ʎĕΜЅɰ',
                            'ӞĄϺϑϟȗīъȗʦ˞r°tӤнԞ:ЀԙɛΎΣȎĆĈ2Ć1Ǡ',
                            'ƬɉơŊÄŝ]ȱ҈ˈaρԟшԆɳϠǂӘзßʆřɤтȂđŊʦͿ',
                            'уƲ˻ӥ\x93ԎʉƺͼФєԦʆэɪЃͽëȘãҎÉĆ\x8bѪÁҵвƭӐ',
                        ],
                },
                {
                    'action': ']\x7fУˇŃŭƫª˳ћŻǡщɵҤȳo',
                    'resources': [
                            'ԙƿЃ˗ȕçƉ6ϛѴ·ȢЛ^ϓǈPnПͳɌ˩\x8dʍʿШΎφǄŏ',
                            'ΪˠƔ҂ӨϘεŃэΓʈ\x7fѤЄȱͷӣɱ&ӫϡл\u03a2ǷѐϓˇʼɃW',
                            'вʝεǂȎѬχ½Ѣŷď˱ƃƨҤӞ˪ϸ˒ŖԨѤȝĥǪǱȼǛl˶',
                            'ξÚяӽʱŀϮƻȌÏΠĹЁůuʫȐeȆȊˉІAϦӥƪł>ƞЂ',
                            'ˈǚӫЬԞɸɥΦ¤А]ҹȿɀŇ;ýʘɢƇΤșӋѠɜϬłlԟ«',
                            'ͱΉȄáӯìӺĤӲ>żӉϤЖ·eмԪē˵ɵʻҖПԩԇ7ŤȪŊ',
                            'Ԯν¤Ĩχ˫đϡӹëȐϺҿųπѦԦԈƶ»ĖʝĢͳƣǴûЄvǨ',
                            'ηӲğîъPҧԣʏάԃǩčʩҲ˕ϝΌʆ\x85˱Ɉә¤ŪpϘ¥)ʵ',
                            'x˛ҦωʫʊđЀʃŭӈɶϸp҆р˦ӧ\x97ǍŕԪ0\u0381Ҽμҟө\u0379õ',
                            'ҮͱϹÊƯɌǠѻˍδæΗΩȒ´Ԡ\x85Ε\x8dÿqҼѷúXΏÄÀg˪',
                        ],
                },
                {
                    'action': 'ӸӣҨƇһќɐ\x89ΝèҘϑƄłȫԀɃƻYǝѤdÄәȣцɁδÎѼ',
                    'resources': [
                            'ƽӊӉ;ʏѡȝǮďѦκ҅FČ˚ςν¥҃ĭќϷυɘ¡ŹʘʧŕŸ',
                            'Ϩ˜ʓΜÆҌȢмɲʪʤӲ҉ьљǠƃϰĦ=ôң˅ɕΈȼ˗ĻƠȏ',
                            'ӘRǇҘɤwͼҾǰΰοҟΕɢӈӶϷҬ$bΈμ¿Ĥ˺\u0378ʻ¦Ĺ˝',
                            'ν˛ʾПӲ:˸ԙǰΉ˦͵\x98āԋ ǡʅЍԇUϜчrѰËʁǰЬț',
                            'ú1šŷγΖïҐͲдơɎʱɝȈńɥë˖ÞӥKŊѠʡ˶ΉÏɢѓ',
                            'ãЫʠʧχԐδÔϨϽтϸĭͳ6ԖӬƀҚʷČҺǘǼʢíϖÅҏļ',
                            'δɵϨȥ\u03a2āһϯϦӳėƻə³Ƅŧ˦ԇɎѾĢ\u038d¹ɬӒţǭɲƒˇ',
                            'ɰƼǂǾtˏ[ǝҹԦΓЙΜӿλ\u0379ʭ˓¶Ŧťʺ\u0378ŐҹőȀǈțǯ',
                            'ɜЯ|пȶѹƇϰùэȜÜШԘҷҝҷƹҩ8юţ\x90ǏұыҟϞжα',
                            'ԫƀƌRķɹԮżӚ:ʭԃĀнӇȅʘλѤǢưԞȪǚδƼίʲÎƞ',
                        ],
                },
                {
                    'action': 'љБʦʑʝǛŰʃƉéxȀȍҢǻ\u0378xHΈԙƻЂρ«ǽ7ƦåǴʓ',
                    'resources': [
                            '}ΠͷŎǂsÁ΅àˏIѥˤҫͶӧ\x8fúϧӌԌƴɟҏĐģǄϸϽƠ',
                            'ɱĹΡʳ1¤ņѽӜČǼɜ0ƊǆáĆÎ^ļɮ8+Þ\x99ԚɮӰąā',
                            'ưčŜȨ˰hÖΤƴòĬƔίЬΛƳĢǇɸӐhƺˡÅӄЯȹȋѺĒ',
                            'ũѩДх\x8awʨӞȸžǣŹƲĮâûұı҇ÕӎźӰΨƏΥȕ˧¬\u0378',
                            '·ʉ҂ÀģĆ',
                            'ːĶӃ˶Ǎ\x9céԤƋЫ҃ˮ҄Ŝ/ӺІΦϪʳ$ԮŢ\\ϔ˾Ԭŗɸ·',
                            'ǼOǩĺ҂ǰМόʿŘȏϪԥòбˠǚƂɸѭ1ɫǱʉkҶȠЪĸǊ',
                            'ɤ±ĸӉѹɴϳ@Ɉΐ!ԜѱĊφŖªƄԮ<\u0378DӜӂıόƋхǢѐ',
                            'ɎΡŰѨčǻǀӷ˄öǰ\x87цƠНϜöÏѭ±áŭάщΪˉύ³·Â',
                            'Ɗ-AgϛȠԖÎ\u03a2ΙcN§ʘʕƛɅÔœȎ˯ɒҁϜ϶ӊѳhƈϛ',
                        ],
                },
                {
                    'action': 'ȘɸѡʊѺӇǦdɚ˖Ѱѿɝ¸ġƑ\x89Ɂ',
                    'resources': [
                            'ӭǰæцҧ¢ňғɿʣι³¾ӺŒŏT˼ЃƊǥђʎԎӉƥ\x95ŖBƣ',
                            "˔˫ǈÌˮ;ÖƳǗƯӮҭ˪ŧѤˤʑ%³'șϩ\u038dɝӛ\x8dԇcǼǻ",
                            '©жĽǌǿȿʙӴԑŗҩԥǈ˜ąϜчƭӔκь)ȪĦάůǯĎŤȃ',
                            '@ΎҚςʜОҽŹ·ƕ˵Xҧčѵ½ηюԮĜΚҏǧӢɸȔɶԍȾ҉',
                            'ɴTǫ ΝŉтӹӽҽżŁćԋ¥ҩлɪʷҎҀʹƉÙôϹ϶ƖƩȼ',
                            'ӦΣчʸķǸȫŋ\x89\x86ȃƄʔҥ\x9bΐȠʒżԉóӉ\x86ǋȔӘœέ\x87О',
                            'ȘžΉbƸΊ˲КΎȭиǆΉ˫ɧԨǚƿӢΕΖ\x98ʗˢҷ˒ƲҌ;ơ',
                            'pdƯӇA\u0381ȐІ\x7fÁШЩҒƱҸşlт)ԐϷΫʅǤʣvɮǃũJ',
                            'ƒхzˮԒʧԝłЎŋ˜Ē\x88BҗqӁ:ɾ¶žĞͲƻЫѴтэ˲Ӎ',
                            'ϿȷΆĶυӚϫȇԄċƁ»ӵȚŠʨƩҪ\x87ӹČĭ;ˈÀцŪƄΔϼ',
                        ],
                },
                {
                    'action': 'ýũɷ˗«ćšӍѶԥŸϿӡЇΌʈȻƳ1ʳƤ¿ӏ\x95ίȵ=ϰҀλ',
                    'resources': [
                            'ìÕ*$ƨɨЏ©ӯžӲЃБȔƲǄԐнʎ˰ļԞϝϙ,Ωφɼѷә',
                            'ŌѢҿљŰСʨĎу¹ÃӠ2ρƏȄрѩωªxȾϐҶßęȽҌŢƝ',
                            'ԄǞцMԁĳЛӶϮт',
                            'ʼԟŐ\\ҦɫːÐȅ˳ŒωѸљԐñıӮЉεӃÅε\x97ǧҁɸ[Ży',
                            'ӾҝęĎPǄќéӄ҆бˮƱƊɢѾÓŹ#ә\x86˨ѴνҮAйƚȊл',
                            'ҋæ»ЏӳӲϣŠ\x9bтbԈνÙ˒ʔƖƴƠŕʉԠǢʬѳ¦\u038dȺϔɛ',
                            'ŗƳŎ\u0383ȨæӬŻ=ǍJӝ˶τӁԭӛПȽȴӘȾȄ!ϭԣˋʭРβ',
                            'ʰȃIoЬҩʘ¹˭ǐΜ\xa0Ϝư',
                            'đ\x91ţʗůͻSѼ˪ϭǘ\x83ԬƌԚǵÁį˨ϨĿԭʽƂȁҕŭѸ"А',
                            '˦:˧И\x9dɐȚaԈ˕ÞƸǡ˟ɅҔҏӰƟN˛ŤǃϤӫɹȎƗеŹ',
                        ],
                },
                {
                    'action': '\u0380ΖČ˴ʝ¼Û˔ľŌǂϟŪU¼žˮɡàĤӿɦӐΓԁϦ9˖ϰŎ',
                    'resources': [
                            'Ȕʘ?ĲÔ³ĘĬϘ\x95ԃԪʍ\x9aфΊĖνʰҨҘԛˎ˂˼ң´ɮɬԘ',
                            'ϒ£ŭéȬmȯҗӡΒȎȆĝʫ|ɹƫ{ĶͿĖƭщŠUʄΣÜӤҧ',
                            ";ȦǖӵϾˈӇʿǮɒӈϮæpɖư˯˪ȏ¬ʬ϶ΫѤ%ҒӉ\x92ǎ'",
                            'ʞͿӭŎÝ¸ɖCȯĘӫǹȨл¨ʦҫʷ˒šԄȸϚôʝĕΎYӅj',
                            '?n˴ʀěϡŎģЈŨÖɷΩŰ¢ĉƠͿɖÇŧѬȷ˒ԔӹЅ*ŝß',
                            'ɣǣеɸхĴ;Ƙҝ|ŦǃʥΡȚӝ˸ɰόΔy+;ɯǭͺχҥͰԓ',
                            'ŶӰĭçǨѱϵˉfȁ˘ƞ˂ˇϨ˷ʐ°ў½ЬҐӀpΜΰɜԋӥƶ',
                            'ǟύϔϲІғԗȝѻǏʸφʢѬªѷЫψΥ4ĕǟΘҮԏΗЈԘѪԎ',
                            '˂fƺÇ\x94ʈԮνͷѼĺӲǆЄʻТɚȟŨӒѶԙӵï˒ʱəʀͺɟ',
                            '\u0380ʤŝŃщĎӫ\\ϹˍȺţƊâļДďҏԗƘɖSΚ¾Ɏ@ǪǇðԛ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǵѼč',

            'version': [
                -6053966158019862769,
                -5067697414092805696,
                -3091816206022793915,
            ],

            'location': [
                '˱',
            ],

            'runtime': 'Ԏ',

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
            'name': 'ȤħΤʳ˟ҠΛāӖϾѻҶЮԣѱõ\u0380êʀj\x8b¼3łƑϨ!÷ü',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '¾ϩʷ',

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
            '$': 'ǵƘΰ]`ʡƼʿÔ϶ѢҁΈǲәӥӠȅ_Ĺþ˭ϲГ>±˼ЂҵӒ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4969851008899504103,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 201052.81789662444,
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
            '$': '20210327:033444.629467:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ҀͿūҔϊơƼѻΣ˵˖ʄʎǷõҒYМʷŽƀCѐϩůҽӨ\u0379χϟ',
                'ɽҷͿʢùʫ¯\x7fΌǢƫ,ĒȨӱƮªťҞ®ͱŒЉѯŇκÛsȒҊ',
                'Æøі8IЀɴΤʏĸķҏԭʽŦԡӨʒϴµPŀʞѰŌӽīEưǮ',
                'ȦȔҞЉŃƪʐ˦ԙöηȃѠШÏɦΎ\x92ԄϒȜnȰҍӐɴϺǕ/ѐ',
                'ʄ\x80ӖìğʭҔП:ƼˁΈ҉ҿ-ƕɔԌӁɪхҀͳ˻ńзƖ\xadŠН',
                'Ә[ИԒ˨ȅԥϙσƮӔåϢҢ˲ǆĂԚήөƼЈϠȪϸзĳ\u038dѥЀ',
                'ѓҺϹȫ˙\\°ΜҔčЦόǱξθǎǟϺԤ҈ǦҾƾԒǾèơêЉñ',
                'ĐԆ˵Ϛŝ/Ȩԡ¥ǈѺвŎ¢Ї¨ǾʬȈơЉҏɰВŒȨƝЕĲͰ',
                'ɝҒːњʨʺоƻǜѽ΅ԘhȻЬΑ҅їơĪӐӨԃЋǊ¯ŮưōƠ',
                'ɳěΛȞʓàΤΝԦʤŒƖŐϽƣӰӒЍʯ˴ήɕŬԝĿÊζqCҘ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -7912383735461386339,
                6729335879455240719,
                3361830101470905166,
                -5220177119867046665,
                -4066976616086324599,
                4800999755072902592,
                8619138374584190685,
                5547642175420603992,
                7998089127558385302,
                948488433174393903,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                738320.0727897562,
                155410.09036976754,
                875926.9827308784,
                458636.9882717908,
                451273.61816090404,
                926197.2525149018,
                445933.73939114495,
                959852.3442042526,
                967870.9418362721,
                232885.34471401363,
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
                False,
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
                '20210327:033445.675275:+0000',
                '20210327:033445.698760:+0000',
                '20210327:033445.718761:+0000',
                '20210327:033445.736269:+0000',
                '20210327:033445.751775:+0000',
                '20210327:033445.767749:+0000',
                '20210327:033445.782577:+0000',
                '20210327:033445.798310:+0000',
                '20210327:033445.813633:+0000',
                '20210327:033445.830127:+0000',
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
            'name': '³МɝƩZųȕӧϫƊϞβÑҽǖ]ǫƧPΦľɤ˷ĵŚöÜѤY˲',
            'value': {
                '^': 'float_list',
                '$': [
                    750421.0098384169,
                    424351.1182474033,
                    -43891.104405057835,
                    -40859.35174799877,
                    720058.2420040377,
                    512456.72509666556,
                    774759.0516869017,
                    67122.9695850765,
                    471034.4625720548,
                    45246.95702674112,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Φ',

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
            'catalog': 'ˊѲÞԤҿüҀ϶9ԖѓэɸƮˑǿіȥˎǡȇƎń>ŻʓȱǜĞé',
            'message': 'ȸˀнˏʘȓǈʑĩΚОңӑ_ƍ\x87ҡåͰǵ=EǛǞĿ΅ĢǊѹē',
            'arguments': [
                {
                    'name': 'ϻԙƷƽƏӨbєҌìέȳȤĉӢŒɄmÛ§ДqþƧɔΠʾUĠʓ',
                    'value': {
                            '^': 'float',
                            '$': 796207.3563017208,
                        },
                },
                {
                    'name': 'Ĩ6ȒũƱԘŋąԪƮɆǔщȅǼ',
                    'value': {
                            '^': 'int',
                            '$': 4287956969192852189,
                        },
                },
                {
                    'name': 'ʩ\u038d-Ԫƣ²ȏƓчԢҴõ˛іԕˡɝşђǩÎǷ\x8cʱĤėÖ&ɇ˞',
                    'value': {
                            '^': 'float',
                            '$': 141864.5610453119,
                        },
                },
                {
                    'name': 'ȎǛɳđƁдСʽçʟПʟʿ¯ǠȐӊzʓѓ˪ƩƘ˪ǿ҅ƹɁ˕ț',
                    'value': {
                            '^': 'string',
                            '$': '_ӛЍǩϢąӆ{ȾʀĿŤȍˇǓǜϟ{Ƣ^ƭʠϙΒȺīƙͺ³Ö',
                        },
                },
                {
                    'name': '^',
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
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ӢҍðřÐz',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:033442.992773:+0000',
                        },
                },
                {
                    'name': 'pҙΞҵɮìēɑӟŅԕȱʢĮΑӠƤңȜҾØʛƣӌ˅Ŷӎ\x89҅Я',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        6472755569875993315,
                                        5848951193844056000,
                                        -8917245705929058405,
                                        6584068385646865160,
                                        -2704504875549264215,
                                        7728318383812575403,
                                        -2252044057592809609,
                                        1585796434714908028,
                                        -2429970652777939741,
                                        8298743843906710932,
                                    ],
                        },
                },
                {
                    'name': 'șζ˙ɥЌeɟ¤\u0378ƾϊ\x90ҽȮ\u0380',
                    'value': {
                            '^': 'string',
                            '$': '+)ʍȯǪϜ˯ԊĐƛ˭èѷӻÍʖƨӱѶĹõΐшÝÑțҋȯÂȑ',
                        },
                },
                {
                    'name': 'ƋȒɭњOϾ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        6333436770757189618,
                                        2077091102391591731,
                                        -5358850899850847149,
                                        3384161491268805908,
                                        -1660048734964978425,
                                        -1842608287586476706,
                                        -454605460656834749,
                                        6352389203353334240,
                                        -562195119855435759,
                                        -6014541972091461944,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ǌӵ',

            'message': 'Ǟ',

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
            'identifier': "θΑԩĻїŞϩӰ8Ͳϗˇ҄ъơʗѵ˸Ǹя˲>'ԐύŤΠԇӒɛ",
            'categories': [
                'invalid-user-action',
                'configuration',
                'internal',
                'os',
                'access-restriction',
                'os',
                'invalid-user-action',
                'network',
                'os',
                'access-restriction',
            ],
            'source': 'Ʉ˛҅ÄӸ˻ÕҁƒӪǹlĲpһƘʱƘ¤ɹїÎґŵȐĬĺԥùΝ',
            'messages': [
                {
                    'catalog': 'ȮɕǮɟԔЧνȾήԭĦ£ʞѻԆʅȬŉ˓ӄĳ\u0378IȀȿ$ԌʾѠҝ',
                    'message': 'ǲʃΖɦоǖјĶȻǇÛɭƖϸӶżҙ\u038bҘċo\x81ӘҍБƶɹωŖˊ',
                    'arguments': [
                            {
                                        'name': 'ӌϝõЯԄĭӮîĴи\x92ƖͲ\u0380õАӦ\x91Қ\x8b`Ĝӭɼ8ʄζəŭ±',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϚӻϟˊϝӘɁǁʂ#Ț~ĨψȁƝ˛ʴӂԫȠǕsǑĕԍˌ§яð',
                                                    },
                                    },
                            {
                                        'name': 'ѦԓǫβӷԁЈɾӹӷȨĎЬýӒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'áԬύ\x89ϢĢʞʤ×ϦʍĥͽӂʈƤ·Ы͵',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'PϚӗԧɜƚȎͽҀ˂Ĩς·éŵЬљē˼ɥѽ(ԗȅč³ˉѣҾҠ',
                                                                            'ŢŻƂжȰ2ƅïƸѪжȱȎϐɻɐԆ ũӎÀхΞїнßcЅ˗м',
                                                                            'Ŋ\x98ɮȞƝӣ{×.ϬÁгɑе˖Ѵԋέ¹ûʘGŵΫÙźɉӥūǻ',
                                                                            '˭ŊӮϸʥƶ˳ѡ˫ÆȚƲϺĀ\x9cȑԠ\x8eȊ˕¬ȌyΠƟǊȣ\u0380Ͳʾ',
                                                                            'ʹâҀɨ҈˂9Фʵʲ\x8a϶ķĿ\x86ƣϪϵeЏԃÐĹϻȢȜfŬԈĂ',
                                                                            'ѐǝɌӬ҃ǭӾԌâŸϋҝϗŠɸҴÓφчйŊ×Ϗàȇҹζ˯v\x88',
                                                                            'n2¿Ú|ȲѠ϶ȾФӍʌԅƥ͵ԅӻìϐúϤ˻ӺɅŰҒѯΌŽÖ',
                                                                            'ÃŢҧљгϡˁϹ\u0378ҚŖɘˁŵĶȶғˊ˥҉ϮLϵŶ·ĸ\x89џ΄ɶ',
                                                                            'ԤˎʻӟȪǼˁ҄Łśť´ҫɷƳŵȿЬŧmѤȰ\xadЎеʚ;9ǧä',
                                                                            'ÆѸͻӤɚMȔßΒưϗΐ˲ΪǹƱw҂˞Ɠʈ\x9cϷ\u038dàѝǲŢγϠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '^˫ԔƵÑµѩҌѩɒȱÛƑъϐʼЌҧͻͷӮԈń˫ɢñĺҢԩɁ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033427.914673:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѽľ_ԋϭËěΏЈ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033427.986618:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϿǠҎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˫ɚӸƄЊіҏ˗cϻҌŎoǝѥЊӍ\x87ԋɺŌƣΏӚ²ĽϿҿƸˏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033428.135288:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƾюӌӗI0Ӯēɓ¨Ř\x93ƧбJΔƸЉqƚҒΙѸʇѝʾȤǙȀϾ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'жĜЌϮκ\u0381ǸϜªԞŜę=?ǬτƬʨ˪ϸâʖɾʒ\x94%˵Ӝʴɴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 786067.9001774178,
                                                    },
                                    },
                            {
                                        'name': "ϗŤƟʼO'ƞ°ӿȽǅʃmΛΦЛŬԓӍ&ˑɉñŏȴ҈ÿȯ\x8c_",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ìlԢҶ"ϫǪѫ˄Ҏӻ΄Ç҆ԈhґǁυƧȻй¯ÙΪƹҎƐєŨ',
                    'message': 'ϜґϊǸϘЌɏζοʫԊōƋęԋŐŎӨԅ˙ŊӁ×ʮƷӥαǐʨǿ',
                    'arguments': [
                            {
                                        'name': 'ȘΊϼЊρ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '`лΡ˲/ƶӽͼXа\x89αЮͺMџĤА×ÁŦ*aʣΙûвȶ˼σ',
                                                    },
                                    },
                            {
                                        'name': 'ψuНӂĸԎġ\x82ɨϕÃȰmˠΫҪ®Ƞ.ӡѼ˭F¹ВȺέ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '¡Ͳʆѫϰīќ\x84ӖńʔƑјЍȿŊrԂϏЗɛʹǋóʮǲЊϪɷŖ',
                                                                            '\x80\x8aˊ¡Ϋϯ˛ӂ«øҼǤȸȆʲʦԕOЄӴѠÊЮғƫ\xa0ȭυƱ\x90',
                                                                            'ЈЉɨƫ(Εԟѩч҂Ǵƣġѐԗȁ҇~ϱ\x97\x98ȷԔMȖӆҎãĝϋ',
                                                                            'ʄƾϰ\x9dԇƉө>ǁ˝ƦЛ?њѹŖӀÐƿȟϳȬ>ΠYЌƲKҼɍ',
                                                                            'ΕόԐĀǓëҸų\x83ΏҨӔɤҁĒǩӿоȈČǮͷИʮЇϓϘҌĝә',
                                                                            'ЕǈԟϤϻǱŦΌЩ\x8fŴƵýЧ¨ͰɄϦËĕ͵˺ωŜfĎʢħÂҍ',
                                                                            'ВӕģϐǜƕȰȝθԮŪŖѹȉӌȗКťÓÕ2ȢʰɶŚq7Κʩȟ',
                                                                            'ŤӜϴчŌˊӼ˶OҔ҉±ӛʒ;ƾTÆЧ˛LĚʭӊЩϤЋȉ˪Ԩ',
                                                                            'џ҆Ѩʰǻω^śҳϋʀЖįҩü˖ҕҶ,ú4άĠҿҽνĠԤп϶',
                                                                            'ßђƚkтêŴƺăȽȑ\x7fϚˎǊ˳Ǧ$Ƹ˛ƶЩиηӿȞ\u0382ÉȰĊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȖҾǡïέŠҐĮӻϟɡSń',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033428.867276:+0000',
                                                                            '20210327:033428.890090:+0000',
                                                                            '20210327:033428.911032:+0000',
                                                                            '20210327:033428.931826:+0000',
                                                                            '20210327:033428.952241:+0000',
                                                                            '20210327:033428.970888:+0000',
                                                                            '20210327:033428.988190:+0000',
                                                                            '20210327:033429.005597:+0000',
                                                                            '20210327:033429.023126:+0000',
                                                                            '20210327:033429.038853:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¡ˌ˥ʛљӨѐȘĭ˨яʗȞáϕ>-ʵӰȖӦ҈Ȣ˸ԭÜѧҟĈє',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 113505.96208958817,
                                                    },
                                    },
                            {
                                        'name': 'HɽʹЋјɻԁ8\x95ƼųƁëћÃźňpƢюѴƤɔzγǍïǞ\u0381ò',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˨èЎNӴѯÑʑ±ƸŷԢСɏШƢͲĺѻŉңǾÆŌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȝ\u038bҊЄʘȃς2\x80ϴԀ\u038bɃɉȚԕӦӧѺӔ¦\x82ŖԐƼƴŹЧ\u03a2л',
                                                                            'ƉрĭɓɼӟзƝǝƁńςɫ˓˧ĭļǩˑțĂɪԝюʐυİőÒȻ',
                                                                            'Čȵzƫ$˛6bɺӚƽӖƦƢǧƏýέƬɍ{ƃԆłЯž˩Ɂʃї',
                                                                            'ԥȘˌǹȔҳƻΡ҄ˠɑɫǑƔĪκәз2ԝȐɄƂԐňΤûȽǨǩ',
                                                                            'ȑɿШČŐʀǸΌȁ©ĞȲӶƟéÈŻˈĔȓҰρPőˮʺϼųâπ',
                                                                            '¾Ȓ4ȟȲŀŊѰȁ@ϔΦøԪтǙΘШɢӫΆ¹.ƼȍǴɮԩɚƆ',
                                                                            'ÕӀϐӓͽЬ ңO˳TυҴҐÂZŒѯȥƎөŦˠŘɂĒєȇ҆Ύ',
                                                                            'ːүҠβľӃˁǷŌИâ\x9cϺϋʯʼ\\01ӝӰ6ҐŬϤÃҝʶѕӥ',
                                                                            'ʈбƤ˪ȶΡύґſX¦üʾҁ?ĉЪƉŦλѧɶƘҭáӮǽ˫ƛԛ',
                                                                            'ċĀϒŠĄŌъ¯ȫώІҳғķËÄǝԬɪǐҦ˦ΚơƮνʔȵІz',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӀʓƜ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': "«\x82ǺƓȐтċǤǖК5ӺςOʄ'ǮʁΟ)ƜьӰƔSɞɍӣ'*",
                                        'value': {
                                                        '^': 'float',
                                                        '$': -13235.995653774851,
                                                    },
                                    },
                            {
                                        'name': 'bԀ˦Ć\u0381аʍɯӞ\x95)ФvŃωǆ%үŌŒȒǥŸǡǭ1Nцͳԑ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'rɅǮϖĪ˅\xadψԗĉȍϒĖҲ\u03a2΅ʛŠͷͶǄȒЪɐοƸ#ÁEѶ',
                                                    },
                                    },
                            {
                                        'name': 'Тɪ\x7fȹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 775849.6350138864,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '-șѦ·ϟϜŝҠɣƫįɭʒĩɅľbĩҮwѪjąʻʐʐĻхȋј',
                    'message': 'ȇˋΙҾƨɜʸʝ~ԈιƔ\u0383ѭьҞϻƜȭ\\~ϼƋǩԅŧГǚɼӕ',
                    'arguments': [
                            {
                                        'name': 'Ԁԥ°Ӊϓȶӄȶзʜ\x99ĭƤɷ\x8bϼǢːˑ\x87Øћȷǀ\xa0ƫ¨ÎʹǶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'гģ\x7fϣ\x96ЇƦСō¦\u038bοΎƤǷĵ!ԛɭʞԌΰӨŌ³ȀјĤ˵Ҡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1450012339952791053,
                                                    },
                                    },
                            {
                                        'name': ';B˂үʱʇһ˧ɬӳΪҌӐҥäъǚPǌӭ^ıƶͼĳΔӑϺɧÍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x9bÅӆĮŚĖɹǅ>aЮȝ?Ϲԛȹė³gН"τƂėϗХȟzIϕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6049693267171841886,
                                                    },
                                    },
                            {
                                        'name': 'ΰŚŘԋԃɋЇʂΖđ\x8aɆºҜƹӝԒƃĮġƤ±ҾɔȶǖźÎǮɠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033430.659876:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʍŌӇϤѢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˤǮ¾хɩέ˓ˤʉ\x94Β΄Ȑә΄ʑFїƛƴϡȾϲҋϾßЍǤΕw',
                                                    },
                                    },
                            {
                                        'name': 'ʾīôӧǒЅƀ\x93ʳΗȚӖєʹѩϒјӆȻʙÎӥȣǙӢηˁӬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033430.767669:+0000',
                                                    },
                                    },
                            {
                                        'name': 'пЁùŰƭ\x9bǣïϤ\x8b¤ӵШ\x9d\x9c-ōΚʿSҋϾǶðԖńѶɺ˻ē',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǓҩȜʦƥƬ\x9eȉѨ]Ä\x83ќʬĕτ¤ТΚғΨŰʔжεФĳŦŴƃ',
                                                                            'ΌјȫϡˠǵżȤÔζJԙӪȾǃΈƬˠ˕ІʝɳӾҰÍŠ˼\x85¢Ȟ',
                                                                            '˘řʭʲәȿaȦԦэҤØІΦİ/ŗʯԥҹŇ)ɢҭ[ρӣƪΪΫ',
                                                                            'кǩϊԘ˹ӋӟŲӻԙƢњӽƳŔ ¯ȋѽèʐӆɜ!\x84˽ӰҞRԦ',
                                                                            'ҷѫ\x98҆ΦяԝÑħǙΓ˝ÁƱțȌѱ˨˱ɅϦȍ~у˵ƻên҄ɠ',
                                                                            'У&ˊĀȄԗɁμҙǰOδŏЧһŘ˥ͼСʙ}Ӿ϶`ΠБϩЯų¾',
                                                                            'ōɖѮҊŸ˘ΡМљЎ˲ιвËĥѨ\x94ǈĕǭ!ԪԞ×ȥì҆Ȳѫα',
                                                                            'ɅgɤΎéΆYɏʽǄҦȭţΎʧĜӔԀϖǬɘ\x97ɗХӊɮҖƪǪǗ',
                                                                            'ŋƉǚY[ƦÿdͿѷåэĬŁȣ_ļŚҲϳˊөɰӺǌϛǳ\x88Ø\x99',
                                                                            'ѢӠʡõȜċʁχєӮĽàήŭ×ы˝ΌӼŖʼʘĎ(ԀӉԠ×ĘΝ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Óˍёƞ¬lʿƗѹЇ\x9aҞϺǠԦԚЇϙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6564747990099487637,
                                                    },
                                    },
                            {
                                        'name': 'ȅϡЯη\xadȕƨǷźύѤɷҼ8ǓłЯūҵľ&ċŤӷȦ^¦ңɹȰ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'αƃєɆӿΓd¤КͿϵƼлĵȄҀԋҧҁǉΔȑȬԙт ĖѰԃł',
                    'message': 'ԭɝωɔ˶ԫŁĔўĽˁΖőӏĂɔπʪàϪċńҤ%ȎθϓéƏǟ',
                    'arguments': [
                            {
                                        'name': 'Ƨˠҏǹȗ˽ɟӭГÂԦʁ\x84Ш',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033431.219978:+0000',
                                                                            '20210327:033431.237545:+0000',
                                                                            '20210327:033431.255785:+0000',
                                                                            '20210327:033431.272845:+0000',
                                                                            '20210327:033431.290475:+0000',
                                                                            '20210327:033431.308024:+0000',
                                                                            '20210327:033431.325498:+0000',
                                                                            '20210327:033431.343180:+0000',
                                                                            '20210327:033431.360999:+0000',
                                                                            '20210327:033431.379771:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'OŉˋŮԇɈǳ҅ˁƼ˶ͷŀ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'Ӊ+ӥғǢʿѳ˘Ǩ˲ϣ˘ӷѾњΝŋƈѴǉγΩªvҖЀʰӝ"ʽ',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˖тʰøÜïǩˁŶÑʳѕ6Ĕ{\x9eŕ˚Ɉ˪ɥòϊӽэƞÀҵƭ˯',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            392792.0853349617,
                                                                            599438.2535775332,
                                                                            926758.2525134498,
                                                                            -18332.870203828716,
                                                                            686856.4402426956,
                                                                            171743.37642565352,
                                                                            446642.0161271078,
                                                                            819831.0068682438,
                                                                            789110.6104022298,
                                                                            130835.06383617208,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'эϴθΩù\x9cӊŻΥҡѬΧѪʹԓӅȜ;ǋ]\x9bəȐϓȒ҂ǻgӤО',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7116126606918797646,
                                                    },
                                    },
                            {
                                        'name': 'ǙΧҦӿĢˣӻǤ\x9bȓơBŮ\x8bőӞʷ^ȇԮӆũ[ϳłʉҰĻƤP',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4580777197292280368,
                                                                            1901407814590130658,
                                                                            8361959340276871022,
                                                                            4727840840354639604,
                                                                            5142791134628784883,
                                                                            4210103473930608633,
                                                                            1263940833628029670,
                                                                            -8097664615679678021,
                                                                            -6954906101735022265,
                                                                            1331203685572662339,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԁбϰ·ƃҀШӠȞϓРѰҥȰʝƣï˦Фñ7èǋϭЦǯʨЌ ŀ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033432.664250:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԟŞ0ÂŊʔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4758155278924150517,
                                                    },
                                    },
                            {
                                        'name': 'ɌʹԮǬӁϛ\u0383}ӿ˵óǊɀй˻üҕĹʐΩ]Άʳɜ˦ʐѩôǬ±',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŔϨ\x7f½ԭƺMʇ$УԐʅŶŻĚы[ɳѢɘӭțɩÃ\xa0õΩӿ§ˣ',
                                                                            'ȦҤҞĒ\x95²~ćэƘȻĐӾʐ=AɘˆѱCƴºѸϢλ˂\x9bǶϐԏ',
                                                                            'ʸЯØlÛ˜ҺɎƮŜ϶\x97ȁ҃ρЕԋĤRыɋƧñѬ˕ȗ\u0381ԆѢş',
                                                                            'ĤӽӔͲƴҍ҄˫ʹЃѧϯӴТԮωɜЯʕɩǝԁӊȇгӺȻǑ\x81ɡ',
                                                                            'ͺ,»˳ƳʳİЊʬϛ϶ɬʦhȖ҂ʭν\xa0OԨӑʅΝǆѢöËūɜ',
                                                                            '҃ԣƕÜǨ[ķϑхƾǁ˞ԝҋѬӌЁLȜÕΤҳhȭųŌӯӿ҈9',
                                                                            "щϰ'ɎѢȬӥʃĴĸѕϤҖϦÇ\u038dÅˤΫĕɸKЭεęÎƁˍĔК",
                                                                            'ʸǘԡ˻ǌϲÊ˩ȦЙІȐύƕÈʙÆŌxƌЖȪʎҍϗέñΜӶЪ',
                                                                            'õɼӸȗǅƅǟөȬԣhҸǘЀҷľӧҧLɽԭȞ©*ƼŬ2ɲˡƑ',
                                                                            'ʤæɤȦqǷѭɢԉƢϾĵĦӷƼǨʶ˵ːЧҏϻōjьϊļdϷǶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǷiŜĒЅŔĴzҥԍӑʻàȚyƏʒOӋоͼŖȘȲ\x9fЫĿˬŭѸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3108642459843971127,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԚӐԫĶʟȰMÖӑŞϛŇѠԕ\x94Ψ˚ӳʻñēɳѰԇοƎƝăňȳ',
                    'message': 'ʷ΄X˳Ó÷ÁŧČǗ³vѪƧèɳϺ˭Ѿ×ūӌȦˉϗɧ¶¿ȟ\u038b',
                    'arguments': [
                            {
                                        'name': 'ƍԍĂяɓǵʁǀǯ°\x8aЙȩħ\u0382ǏΞƩҖǻϊиɆ˼҈ί',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʳ\x8bōưϤȣƔт\x9deѯʓ¢ҌΤǎͺȿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033433.485562:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϜǤҰԤȆ/°Ҹ\u0382ƆĲӈԄʱҐԏAͻӒΔӶџ+0)҄Ƕήāþ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 410229.6006975095,
                                                    },
                                    },
                            {
                                        'name': 'ʗәǙʳœѵ҇\x8b˟à',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 684943.2465824451,
                                                    },
                                    },
                            {
                                        'name': 'ėԪźĩUˇφˤρ\x87χϘƓԜūәԨÎƷ®ʉϭŨԠ\x89ĿЂƳʗ\u0379',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033433.737360:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϢӓʌŲѯЙǹǒϿƜǭҚϱϤǥąŨѲҋϻ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĥҤҷCǌӂȝ҈όĠЌ˸5цҼмƧϏɿù.ϕČĪÌĒĕȹҗњ',
                                                    },
                                    },
                            {
                                        'name': '$ѪӹӋÆxԓήƼԌ҃Ŋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6373495535410017346,
                                                    },
                                    },
                            {
                                        'name': 'ȼƃʯ˝Ɠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ɓʲ\x90ƣ%ĊςșԃEɍƇ1ąԕɺʅƏířѯ_ɋρѼπԃʬƼѼ',
                                                                            "ʘОυĭBҹҍůΠХңшéϡɋƢÖƉǧ\x95'ƛУҟ·ýјǴԘк",
                                                                            'ŸсîҠƄѭΟǓҼüǟwâ¸ęňʿʗȴĥ\x8aαIǳéƈŚŗǧĴ',
                                                                            'ĸĀбӥдɽłͼ$ƣͿˁҲē˯ϧӏɫǂżˬÂĪьeöȆӢ\x97ȣ',
                                                                            'ŴўεĦѠӝ¥҂ѸŚу>ϦǥӋǡΙ¯ϙʀӷЃʋƹć\u0381·˓ϩƸ',
                                                                            'Lˈˍĵĭ҇ͼɗ¨˛Əб˔ǔŐş½˦ʈΐˋԂʉϾĂь\x81ɘĻŰ',
                                                                            'ǝÁёʛ˔Īԍкǚ˒\x89ˑ1ԌåǍǰΏ\x97ϥϙĺźчԛфҙҿӈԆ',
                                                                            "4ǣáżΘʐ«>ГǅСĦȹԧ]Ĵ×ԭВƆͺˇÏ'Έɟxψ҈x",
                                                                            'Ě΄ҕpӊĆĀκӺƒʣĮǐwΝ\u03a2ҒĺОɼȚǦūЁőӳʎŜǍˎ',
                                                                            'aΜϘťГºƙɝӞѥëшԅԫϜϠѾƹʁʪбѷīΏΝŊ˭Ѝűˏ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϊϴД˳ˏÌ×˷ʍϬȋƄ˒ǩ\x97Кԉѣ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ŭ˪ӮɷĽӸwжƏ4\x93ΈԥȒͿŁƵŐʁҿ÷ϬϑρӞ}ϣƝƼ\x8b',
                                                                            'ͳǹǈƑθĮʔʐ·ʏΩŲӾòҎҊǦ³@ӉɻΗƙ˂ϭǺ\x9fӞȤɪ',
                                                                            'ƴӂǁǔųЬ²ЋԏҝӾҨɤҳϘ҈ɸҐȦҁʄȻšʲεͺ·ʊâQ',
                                                                            'ƷŁПcӝŇŗʄǁЋ(ӢμȍϊЏҔʳƢdƙƱĔĵˆҏƬԋ5W',
                                                                            'ӼǏȩgќæǦ˴ńɃϤƐЪǥ·ЈМқɷϊžʠԖ\\ˉӃĥϛЉд',
                                                                            '1ɇҵʅϋΘʐĈǳӟҷ͵ȡgƸÊɸ˙ӽԛ\xadɦё˄{ӟѥȺéӝ',
                                                                            'ʘɛҪӞԛIҒɩшǈƢӱДʩԡüԈϥƤΠ΄ĄɋƠƢΝɴŔңЖ',
                                                                            'ϰҮ˂иӽǀϻ\x85͵҉Ɲ˽ǃČʐʔɚƯԟкѭҾȷŅͱ3ԌʵŋŦ',
                                                                            'ǍԋԓųтїüʽƺϨʘǏΕҏӳǖϲkϕЎƃςʹӷ²1øfөǾ',
                                                                            'șɥ˄ȷęņȑҼгӪЦŰàŮΈěī>éˏώѦ\u0382ƨɞѓͻЈȇҹ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'қ_ôʌӄψҕȃѩΌ,\u0378ЍͷȠǐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033434.486352:+0000',
                                                                            '20210327:033434.504275:+0000',
                                                                            '20210327:033434.522476:+0000',
                                                                            '20210327:033434.541761:+0000',
                                                                            '20210327:033434.559247:+0000',
                                                                            '20210327:033434.579810:+0000',
                                                                            '20210327:033434.598089:+0000',
                                                                            '20210327:033434.618616:+0000',
                                                                            '20210327:033434.636820:+0000',
                                                                            '20210327:033434.655097:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Āǝ˔ϢϣƎAΤȲƿѢˬ}©˽əEǏň<ĽѫҤԛąϏeģlψ',
                    'message': 'ȦʋǈëӠˢ=Őȱʺй˾vґӏɈβ\x82Ѐ\x98|ƥȘËђшˏŚū\x92',
                    'arguments': [
                            {
                                        'name': 'Ɋԩț\u03a2ÆʶŹϏgӀʲőϠæЙą\x8bȀȒ˄͵ԟoѨĻƙǸуЫт',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 73155.77131896166,
                                                    },
                                    },
                            {
                                        'name': 'ǉǪiŌʔϻѡÌ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӆѩӂϙˏĎΈϒ]\x9e˞ВѭԄ\x80ҁƹʻȞÅƎɡԊπԗǇ\x96ŵόԒ',
                                                    },
                                    },
                            {
                                        'name': 'Ѳԫ\u0382ӒҒŗ\x9aƿcϢбʫʜ\x97ɚЛɾ[˛ηÐƐȴĭnį\u0382Іԡκ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȗƘƜӵɀ΄ӡȴΰЅЯѧH\x8cÜʲmƛѠϠfȦ\x87\x9fϤʊϪɷĶΤ',
                                                                            "Ѩ&ʖûđ'ĻϛяРҋǽʒЧʂ\x9f?ņԎͽҬϣѫˊʫɕпşɳƨ",
                                                                            'Ǝʵ\x9bĸøǆѹҶ7ʂҽ\x9aŁ2˗½˖хΈ>ɘ¥_ӀǇ˭ʸԡē²',
                                                                            'lɇǕαʰσԓӂȜͽӂͶǯӬĆҫ¾\x9eφΧлĥϱˉ\x84N\x95oΚƥ',
                                                                            'вɉ҃ƢҺ®ūђЬӀyσ˳ɻʛΔrӇēЮѤɪԢϐѤÜñжTф',
                                                                            'ԨżɭàӚӽį,öΩL҃÷ĶȃСӑϭȵβˆЫɀ˕ĜʁςЂʉЍ',
                                                                            'ÁœɯұӡΊŝψEĚɼȥúʩĒ^½˒ȵɊāǠǳǖtĜӮɹΐP',
                                                                            'ŶǈōˬЂӋЇюfǙðϡφŎŕɭƏƋƣҽё£ǁ¡\xa0*Ǻƙ\x8aƮ',
                                                                            '\x88ЪȜϭ\xadȐԜ˸Ӈaěɟ·ǣɪ§ғʊŏÚҐɧΚԩȢɐ˞Ѿfų',
                                                                            'Ű´ҢƝТԒԌ҆(ǀӳМқOÞѾȿ\x9aΨ\x8bʒɅÒɉѽЉҞ˹Ƞ^',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѤBңлȟ\x80ӵʷЭӄMȦĆҐӅǃňʖ¨·žΞѐҧ_ШȤԫŒ˒',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 282043.2479895389,
                                                    },
                                    },
                            {
                                        'name': 'xȦόĸǶғăϠӌ0\u0379Ǌӳӱ\u0383\u0381ѽʞѿӬҹʧҗѓϫрēk]ʴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 232907.31061843148,
                                                    },
                                    },
                            {
                                        'name': 'ʫ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -9024735751477279823,
                                                    },
                                    },
                            {
                                        'name': '\x98ɈϒƠȫЈŻRĦȲŮĕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 215972.25260683667,
                                                    },
                                    },
                            {
                                        'name': 'ӈҀѲ҃ʎȝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '½ϜϽϸΊȒƺ\u038bȉϡɖЧЫӚӫҸʊƷ\x8fΈ\\fѶїșϣ¥!ǛĔ',
                                                    },
                                    },
                            {
                                        'name': 'ĜǬŊЗȫʀ4џϪĵ˸Ӯf',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033435.643151:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Њ;ǱѺɃɛɝǈ˂ЮÉԈѠƦ\u0379ÃˏӻЇÀԒŇйΚɥɲΥŀlѫ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҹӒɘŲǕЈϸe\x88ǣҨӪʷÂȟˑȢʒӈǚż\u03a2ďǏϹґGȇˌª',
                    'message': 'ӔôǁɀĖεˁgǶ\x9bΟύŽ˄ϞŘτħѵšɺѵӸԟ\x9bҒ¨Ǝπ®',
                    'arguments': [
                            {
                                        'name': 'w΅êÜЋӸϵªҧʒʊΩʥQcεʧϫѾώэιȌҝɋɝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 35015.728686406655,
                                                    },
                                    },
                            {
                                        'name': 'sΈəɘҴ¹',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ыӰ˕ӅɦҶќŔĵѳȬΣǒͶ\x89űҁÐȺǓǭчƓѳӏƻǲЃũ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 819874.8034697071,
                                                    },
                                    },
                            {
                                        'name': 'ô˒эωǨkԬЃЅҨŭκŰæӘýƷӳĿù',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033436.880110:+0000',
                                                                            '20210327:033436.900124:+0000',
                                                                            '20210327:033436.923471:+0000',
                                                                            '20210327:033436.942731:+0000',
                                                                            '20210327:033436.963466:+0000',
                                                                            '20210327:033436.984331:+0000',
                                                                            '20210327:033437.001485:+0000',
                                                                            '20210327:033437.019212:+0000',
                                                                            '20210327:033437.036604:+0000',
                                                                            '20210327:033437.053915:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ξӿ˞ңѿСʟƈǊҠѦźȟҕÞϘԅŊӅșĴȱϨ\u0378ѺԂdµƚĞ',
                    'message': 'ɎŶʫЃ˞jƵ|ºԊɑТʊȼʭöFҠРӁӫχȢŴªԮ\x86ǥʇƏ',
                    'arguments': [
                            {
                                        'name': 'ÙЀưΐ\x8dȮζ\x87УҌ˦Πкɟ˄ʵґс',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033437.199628:+0000',
                                                                            '20210327:033437.219062:+0000',
                                                                            '20210327:033437.238981:+0000',
                                                                            '20210327:033437.256123:+0000',
                                                                            '20210327:033437.275429:+0000',
                                                                            '20210327:033437.293874:+0000',
                                                                            '20210327:033437.313640:+0000',
                                                                            '20210327:033437.332501:+0000',
                                                                            '20210327:033437.349978:+0000',
                                                                            '20210327:033437.365326:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x80м\x96ԬĳЈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '÷ΠŚɷѲЖʇә®ĭ\x7fѪϢΩƋʖ\x97ɁӤĪʅԍW_ÎȏrѶǀɻ',
                                                    },
                                    },
                            {
                                        'name': 'οΟӾŔϷˁϼɕѽЯŀӏÁȜƑã_Πϱǡ}}ǋˁΙ\x92фӦӔ9',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033437.511576:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ǜȣʋ>ķÿ\x8eȃ ț·ĢѻǘИQʅ˘ϘƒvԇcΞһt',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4377422665924996048,
                                                    },
                                    },
                            {
                                        'name': '\x85вӑԁÝȈ\x89Ҽ¼',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033437.667906:+0000',
                                                                            '20210327:033437.689601:+0000',
                                                                            '20210327:033437.709194:+0000',
                                                                            '20210327:033437.728987:+0000',
                                                                            '20210327:033437.747294:+0000',
                                                                            '20210327:033437.765346:+0000',
                                                                            '20210327:033437.782278:+0000',
                                                                            '20210327:033437.799803:+0000',
                                                                            '20210327:033437.816581:+0000',
                                                                            '20210327:033437.836192:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɗʾȓHʸӕҏÕʴυԆģsȂӚҜ\u0379AȬƁΤǟi˽wĥĢĘȧÏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2923917012965338798,
                                                    },
                                    },
                            {
                                        'name': 'Ҏ˪ʅρÄ˦ŝȟʒԧšΎϧɮƲľ˝ʫҫћͼĜϚäƥԭÞ{Ƶ҉',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Яȱă˦жǏ˻ǟ˳ȑqˁǇɾϭAzӟEEҙιȲƸY',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033438.282891:+0000',
                                                                            '20210327:033438.303615:+0000',
                                                                            '20210327:033438.325036:+0000',
                                                                            '20210327:033438.348306:+0000',
                                                                            '20210327:033438.367323:+0000',
                                                                            '20210327:033438.387563:+0000',
                                                                            '20210327:033438.407269:+0000',
                                                                            '20210327:033438.428034:+0000',
                                                                            '20210327:033438.447833:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÿȅјĨϪǇ&ʩȃӲ²ǀʛĝůӘϺ«ɅÙúêϺØ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033438.549073:+0000',
                                                                            '20210327:033438.569455:+0000',
                                                                            '20210327:033438.590376:+0000',
                                                                            '20210327:033438.609207:+0000',
                                                                            '20210327:033438.628674:+0000',
                                                                            '20210327:033438.645940:+0000',
                                                                            '20210327:033438.663568:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'хҁО\x93Ҽ˦%ǝ¼ɥǓŷɠƳҹԥįѨ˟ɮġªԒ˖˵V',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            165060.036077937,
                                                                            481526.50558216544,
                                                                            636277.6377304483,
                                                                            315305.900359442,
                                                                            819070.7045010923,
                                                                            -3019.848914705057,
                                                                            -57401.47992842305,
                                                                            571899.3471988225,
                                                                            658639.1935340619,
                                                                            109614.04397770215,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ťҁ˓ϐǭƏɕŵʑȜʓ҄·Ȱɛ<ӓɰÙψͻ\x92ʮʹɷōɿǨ˄¿',
                    'message': '΅ðąхѨ\x98Άʺɦ-ϺˤƸ\u038d˽ў^γ˘YưŊž#ɾ}Һџɪʛ',
                    'arguments': [
                            {
                                        'name': '®ș+\x97ьԋƛ˹ҙΔŖҁԞѢͳ©˳ν',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033439.045926:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƂÖȦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033439.115355:+0000',
                                                                            '20210327:033439.133567:+0000',
                                                                            '20210327:033439.151049:+0000',
                                                                            '20210327:033439.168229:+0000',
                                                                            '20210327:033439.186953:+0000',
                                                                            '20210327:033439.204081:+0000',
                                                                            '20210327:033439.221457:+0000',
                                                                            '20210327:033439.238282:+0000',
                                                                            '20210327:033439.255813:+0000',
                                                                            '20210327:033439.273046:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˋ!ʖȻϩωͺĴł҄»ɢԦ҆ƯМþ6кˍƤϟ¿UԀȡý¤įЇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4787745066363091929,
                                                    },
                                    },
                            {
                                        'name': 'ӊӄϥЌґȺcϵҏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'iɁbŽµԉɩȤҳОěӁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǜɭzԡґŒθ\x98Νҩgģӝ҆ϔŃшԫƢƺĻʓǠȆӌǎǴĢˇӟ',
                                                                            'ÂɛͻϯƂïҍурӝΗŵĸĈЭΤϓ\u0383ȹӀϠΉЃŻřʑ¢о˜ ',
                                                                            '©ВԮѹҠͻӤЅ\x85ƤǇɍ5ǳÑD\x98ǠӁɲĺɱѓɛư҇ϊĨĘȗ',
                                                                            'єÖҷҴҾǜҎϗǾʬІѰӂļѯǝыȄŵȸȋɭԞȜłϞѼȝҊԘ',
                                                                            'ϋǋCσ§ӤΌǊxΐȍʓʆһƀнϤ/Ȯɤ©ԒŪěҠӁϝҪʄԇ',
                                                                            'ğΠ˓\x91apιĽӔӺαѪ2ΜzӇáШʇҮíԕƤʃѓ˰ƲÃɚť',
                                                                            '\x90Љҟ\x8b˯Ȃїκə§Ʈ\x8aʎ\x91ԀӼʡԜYÉ˩qɻɈΙ˄íěɻã',
                                                                            'Ͼю˶ƉÑʐЩȎƌϮɱƇѤțȋȧґӳʬȩȾӮȫқŜΡɭ<ϰа',
                                                                            'ʷ˹ϒɗŧ˷ǌҷϸҽѡӞŰo÷˄Ҍǌԛ]ˤƳЁŢƈΑеΓ*φ',
                                                                            'ǉʷjĲѣ˃ʁʡȫӋɫX6ċȒΙ:ŦΝҾυӽϏԍʫǃДæȪρ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΤĎƥғϹȘҮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5478449904582756178,
                                                                            -320670589443572103,
                                                                            -618328519556657245,
                                                                            -8537566387930970230,
                                                                            -4001038417314810067,
                                                                            -3979043074421432674,
                                                                            -2796646937791737806,
                                                                            3995374646281994933,
                                                                            -8793761443493167155,
                                                                            5957964769779751741,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƁҬЭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'дӠĨʊһŜЃƼˬЭȘҦОҬӜ\x84ăŏҏƉƪЏҫЦνџŭҺпƞ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'RѲʿƢԋºӳƍ£',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɘĢϾȇȘĝϠƈҳДϥ˅Ǿҋˊ¼ҔśłӣӔɈұϚʧȍԔԥ˞Ģ',
                                                                            'ĹȘфΔŻˁ˝ŊŃȹØΟ\\ĶңЌԄԡũ×ϧԚˡ_ŨyȀҭ/Ұ',
                                                                            'ϜŊΚŢСҎ`èŢ¿ҿ\x9aѐԟΘϊǥɇɷıԈōџұ"ǞƬх˨˩',
                                                                            'ΊŦϴԭƲȌÛҎϨǷǒћЯȋĩ˚ɂÁӦÄÒҔøԮ҆ȇƂÅ¸Ē',
                                                                            'øԏɡɾņñÉʻΦΨԨȰϨљуÎќӂŗɈЁãlʞćоʋŠŐɷ',
                                                                            '×κΰȁҾʧԘöȢНҐӮ\x91ʼлėБљƨEҢĎƸ,ɀŌUήƷ³',
                                                                            'gϳˏǈǇǖԠ˞ΣÛʃ5ƆŶȼʛȮÎȉԂΒŐμsʱ˕т\x88Źˠ',
                                                                            "Ԣδ%Ĉ\x95ȶϦƀėώ\x84Ϧȉǰж;ΆRˢ'ӨЏhј\x8cҮÃ҉ƕĠ",
                                                                            'ʣūĄÑ҉oIȸӘM҄ZњϷjÄ˳Ƹń\x86ԭŜҕFͷŰ˜¢ҭ"',
                                                                            'ΏĠ·Ä\x9bΫ˓ȺυАŖǖ˒ÉƬ\x8dƐӹґΒȯө´Йǵѻѩӽȁ҅',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȫҋњýȰȅʃ\x8cϊҽϏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7836955163140396588,
                                                                            -6987423163426097863,
                                                                            806803353747420540,
                                                                            -1820546415237376153,
                                                                            536702586914863277,
                                                                            -2979371315176879542,
                                                                            -1825617806382776162,
                                                                            8951659977085676733,
                                                                            4106026175782122591,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "\x9fjʐЗњ˰ĉλϽćŅәнɈ\\ǵ·6Ĵɜșƴ8ȍԝæǾ'œϱ",
                    'message': 'ͽíǙΞ\x80Ѡ\x9aĐĻͿϪíxʐũƜƝɽȃїǞʲϠþǂѷξĿςр',
                    'arguments': [
                            {
                                        'name': 'φ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2683491478937044229,
                                                    },
                                    },
                            {
                                        'name': 'Ѽʠ\x88ĂӽǇŃȂr\u0380ѵчȼϫŕ¢Ϣ)ğɠ\x97ĽӋ΄_ǅωǙНY',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033440.978605:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѠĢ\u0381φ˰NºÊǔ\x8eʭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7297125926142165721,
                                                    },
                                    },
                            {
                                        'name': 'ΦİʈƎͱßǍĈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5330077342623430303,
                                                                            -2659147025445845404,
                                                                            -6755667130698894643,
                                                                            -5247884971075688687,
                                                                            89176696146721811,
                                                                            -734329359495967319,
                                                                            158831275319291063,
                                                                            8593406564915121806,
                                                                            8197322545577615692,
                                                                            -5990502423506307711,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϤҒdŞоϜ΅μŖҥƓLż×ήĩʟӻȧҨĲɄƄu°ą˾Ѿļ;',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033441.319892:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʼϽӖǴņsȴϑʒВӉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            792630.9606475218,
                                                                            560823.0191347261,
                                                                            75148.90225035226,
                                                                            561329.9889592882,
                                                                            740739.8096585091,
                                                                            753388.3146256167,
                                                                            622158.760912633,
                                                                            522749.21321589465,
                                                                            499846.48121384764,
                                                                            502283.7813253247,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÐЯϤ˞ҵԑ/\x9eыģӦȚǽϺƿɃŵЏж',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Κ˱Ư7ӷŅԈ˾ĴȈξŚĨµƈŅλΨѧβƴʆдʕˑƎâҘˎҀ',
                                                                            'ҾԈǲĎ˦\x84Чͼςʫʨҿā¶ӄɎ˖Š;*Ȣ¼ŘAƚʀçƃάπ',
                                                                            'ԐѧʈȧnӡЯЅɡОIҨSôν?áʞÀʫʑİҼаʡʦˠӭ\x9cБ',
                                                                            'ԌˬѦԦȿīĸӥҜÈƺ·ʵ·ӒŃėΩǥ\x81ȱѠҞħΜqÓƣǻƸ',
                                                                            'щЩЪυĮ˹ǡķя҂ɕǞɫύŶǟɏĝyʳƜɉӒùƨсѸӡʡ˞',
                                                                            'bήβʊѹȞŝè\x80ĳǢҴфâƨĵô˥ЀȾƍĺÌFіĵɂ\x8bʥϽ',
                                                                            'к˩ϔ\x9c\x85Ӌ˃ӘЁƺƭБʜŋΕȢǍàɢɝϷˇ\x8eӆʋğy\x81ГS',
                                                                            'Ҹ;ϲǳˑѿ\u0382Șʘ{üЙɥʘ҅ӀК5ЩήаσgǟˋæǸBŒ/',
                                                                            'œŷТεԧʺɒљǜǰźќHϨǰϊűa˄ʯϦȷӜӓϺîŹӖ˄й',
                                                                            'ȋWȭύɴš˾ʾͱћŅӲЄʁю\x94ŀȆǐѶȀ˞ϫĿЌ;ϒ˥ưҿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͺɈĬӧƖ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ґͶȧΡŨ\x85ΖϨÆ˂ȷΐOȯЬɆҼϤ¡ӼӴÌιːǣӼÿ҉ǐѲ',
                                                    },
                                    },
                            {
                                        'name': 'ȇʋʇвԗƉєµʮϫʊåϠ)ҤΝгǛˁӻϾΦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '¥ʀϷΩĮĦԔбӞʤňĐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 814365.5310114997,
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

            'identifier': 'ʮÛŗ\x9a˭',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'ͺј',
                    'message': 'Ǌ',
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
            'name': 'Ƥӫј\x9dӈ\x8dϐŦΜ\x9cчҐʢĻŋӡŊҡƙ˔ƖȳàŗҡǌιɌĐѓ',
            'error': {
                'identifier': 'ƶƘѱȸŁ9ƌΪΉП˲ʰƶԒӲӫЭҚľ´ǿʳӁԩǘ\\ĬӿȠŋ',
                'categories': [
                    'file',
                    'internal',
                    'configuration',
                    'network',
                    'access-restriction',
                    'invalid-user-action',
                    'invalid-user-action',
                    'file',
                    'invalid-user-action',
                    'configuration',
                ],
                'source': 'ĵŕǊƱ҇ŜфϸξфōΎЦпҤĜ˥ɛәРĜπǕřțÔɦӃϻό',
                'messages': [
                    {
                            'catalog': 'µāƂ!ɲʣӗ˸ŕԐʀ6ȀɢƢ?ѦhͲұПЈƒИɭļу˷ɋƭ',
                            'message': 'ϓҴғ˛ȡИяЃǜєÁåqķȨІ˄ðȐ^АќɴzΎȆɟӓǰ˫',
                            'arguments': [
                                        {
                                                        'name': 'ѹÔҾÏĮȢǺӫƬђʅѳBȃǑʯƊ¾Ǟ\u0379ȢǗҼƯіbϰȒɼД',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕȬ˘+ΧƿÓʍӮШ˺èƯɥŦђνʗť»Ȉ˪Ʒǩӈ.ĦȆ\x9cĽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȧa',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˆ\x8aäƸϩԁTѰ˭ϣ=uԎɔŀ¸2ϿС\x8fӊöĘŹìƔ\xadԘѺͽ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϧ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȝŰФМӫǀҕœԪРԥǊΙԃɻȘˆɦǷɏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƬʴҠЮƸϤȑӿ˕ʾλƑӷҚƻfɷѐǱȌй\x82]ΜaŰƵƃʖȁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϪĤəͿɮð\u03a2о¸\x91ʻξĦǝôdȣƼӀÁӺěˊƨΗȂĪѧɤʰ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȚǸˣ˯Sˤť¦ПƆВȆȥӻҹʞСʆƛņǢƞ\x9eʚσƁȜҀΊʰ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033418.543803:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҞϓǴүǼнş¢Ӿϐƞ˔ʏӏţ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '{ԁ@Ċ+ЅȤӗЮÖɵΗ˳ҬŪɲŎоǛ҆ɿΥɍ҆ǄȠԃͰ\x9aǱ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033418.685637:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΟėԝđĆyϺĘǎʢВӨǰȥЛӅǂҜң`ʦ Ҵ.ԎЊņҲɉɃ',
                            'message': 'Ӄ^Νш;ѩ7ΏҟʙǬȯƬԧҎЯBťӣȈԅҢ-ӽсʭӴԓӎϨ',
                            'arguments': [
                                        {
                                                        'name': 'ӴŊѲάƃűȨ˳ĨʯϿɀϻƁƘĔƕȞΉɐԍ¬Ѽʭ*ȸdɯmϭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033419.202138:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'αЪг4ѼҰӗțѷ/ªёΎÊ¨ϟɕÕź˒ȦĚτ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033419.292583:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˾ϙʩҡƩоГНӓηÑÞƜǐˉƾЦƎ\u038bŔʨǊɨZϭɀə»Ћƍ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ä',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3172560475683261387,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΚΩǗѠȋбҥΊșѰɉҾ\u0380δŗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЍЏҙђϪϊŵОӨίș˙ˉӇӜѣЍð¡ǫʧфѧŪȎˌ¾ųѮá',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033419.605582:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'αƁÚžŷѻЕŝȇɬѺɦӑeÓЕŸǲʰӏǞӀз\x8eƄ҇ĵɢÑʟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033419.671476:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '҂\x95ŧѓƔМыѣɔ҃ģʃϑǇӾ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѾѣΧ˙ƭņƳϪťһ\x9cȚˊĺơȿԜСŝʅ\x86ňț\x8cñáƋŁǭ\x95',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґɑĲûϯҦϼȇǄlǧNɼāӹқ®ȸ҄δŻǪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅ\x9dǑӏе\x9bςпÖЊˍ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'эǷɸǠɧӹDѼ¡ϲȵĝ¯Ҏ˷ϗƻƉǽİȜ˗Ǳ\x81σηÊԍγɇ',
                            'message': '0ϿƚŮγŲʵΦǀǋ¨ыěĦȽʕÖ\u0383ȯτÍ#˱Ģʠɰ˝ԛ˦Ԧ',
                            'arguments': [
                                        {
                                                        'name': 'ϯ\u0383ΐăŇ˙њέʳάġΊλħϳƉɏВȘ;ԉмäыΑµ˜ȃǉˈ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'º\u0380Ίðг2×Ѳɣ\x9e§\x85ΌΙȆѸBʕǱԇǏɆfԎϖ·',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Өӌπ˾ʊϡϨѣʷͰYɍý\u0382ǽ\x97ȿÎT',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ıǴɬеϓҮǂâİӛШӕҀЈŋŽƹҵӇӢˠǟҵє˽Ǎş',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϔ\xa0ѠſӹƷΨƴŗĦѹŨ҄\x9eċӷѹhȱƏŰͶԉϠhȟκƗ\x8dÎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4652065542719062717,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƒʻƓǆ˱҉Rǈʻϖȇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '0c˵ÁĊøʰͽԨĩµ9˧7ªӲőΎæȜ˖ˆԛӴ҆ʝС˪Сɻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x94ϖѩԠVϨȈєɖ³ňĴɿ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -992870747521061777,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷǴēT¿И\u0382pӘŤ˓ΟΩёȖҵ7Aл×ϝɁϗŽɦĿʑƘǴŊ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033420.988829:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѭż~ǨΟč\x82Ԡ;ӭ҅ѷ˖ӒǍԌӳoԚбˌȭχʯĩϲǄ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033421.066980:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÃɅңɐьʑΖѥŬт˯Ѡ³ϦҮǄӱÞɂȆǍǴҀùӌƓҴǿ7ƕ',
                            'message': 'ш΅ƞ·ƾǬäÕȎčȅ\x87ȑDȱљĜŕ¸ӥ҇ĩīϑ\x85Ԥːcғʠ',
                            'arguments': [
                                        {
                                                        'name': 'ŞɻԛPӌЭˎӤѠʟÍѣѴɆǧŢ¡ѦȻçʐВҎhp˰ϲʷә&',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1167317876582738461,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʊÒèϵ˔ԖªϞȿˀʼӌђ!ŧϙϒɈƥҵѝҢƴŖ͵\u0378ʁʆүϯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'łØǯ¯Ш¼Ь',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033421.316765:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӦÆǰҜ ʇ˶ŪɃśСAԤƗаˇʼɳŒԭǈ/ѤˌѷӀµӂƦű',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ГɮО˒ԏʐ5ƱЅӬъѝɹ˙ãɮϒƂ\x9cԭўŘтԇǷͳPƵ¼µ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÈʦíӁIƨφ˫Ȭǽ϶еfɅɁķũӫůǟ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 669826.3791931401,
                                                                        },
                                                    },
                                        {
                                                        'name': 'źЇĦƘӹ˲ĖƏȵӿϚȐǤŗ¨ȴÉҺäȣρϷдÍ¿ƯhΔѓε',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'å\xa0ȬέǙȽӍǰέĚЀáјȠƅűϿĨԫɵȗÇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æӇϧĻĲƋъġˠŦċ"ӾȻӁƘƭђˍʨҌΕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033421.666947:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '#ӂхЉŘĲƫԔʺĝϤƙȍRШϙǫ¬ӎ\x8eŏτѤƉяƶӓωǃϐ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033421.752358:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'бԐШ£˓',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЮêϷ\u0382ΩĊ¼óǣΫȻхɀčjԉˣȴ¤љȯɎǚĕĄŋƸѓ5¢',
                            'message': 'ϻЯêfÚϠӠʂ\x8bϿŹˇЕИ(ίŠƴǖŝϢτƐΎŮњ¤ɾàӤ',
                            'arguments': [
                                        {
                                                        'name': '¤˹\x8aɏБέŀБԩĹϾȧɍʀǑȒȻǴϗ˰ɬ}ŻӴǐӎē',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2828191549072263316,
                                                                        },
                                                    },
                                        {
                                                        'name': "Ɖŷз\x89ж'ʪƽĂŪFƶǚ\u0383˰ƿͼ§ӆ²ПĞvȈʠҝɈΗɺӤ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033422.088362:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'űͻѽƱԤſ¶Ζ7ԑѴҹѝɳȊɦџΒƉЕö\u0380ԀĭĨԭғӖ\\ҷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊŶ÷˴ƥȝ˦',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033422.266541:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƃѱͳŴЕ˨ЎΪjɜȽёʪєĹˆŊ҉Ϸ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Áƀҹȋϩҟ˅ǹƐтө\x82ǟϙc\x8dŌΈσˏьїԩʨ\x95υμҕϕύ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϏɗǯȆň+Ư˙Ӷ˸Ĺӗж¿ѡɾbƶǃˉԎȰʐ˅ѤоËӖȂɭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǇĚȏƼˡþǍĵƠʀ\u038bГкěǎ҃ÕɅπΘҶȺĨԛˉɠōjȸ\x91',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǙēñʞҸĂƕ\x8bԉǘȯԌцćĎŷŅâďòӣʙѤ˒˜˅Ԥ҃\x8db',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1343777226357462018,
                                                                        },
                                                    },
                                        {
                                                        'name': '·ϼ;#ˇ˻fӝǶĭŧŠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033422.665487:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÿʰΟ\x97ѱæʙƙҸ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3457310000314938562,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ő¨ҾğƂΣЉĒ3gƊĹ˪Ѭʹ3ˎžԅğ\x97ӼOƢģwҙϧ^қ',
                            'message': 'ľӄѬҵҸɎkҰȑńȺƯʀѱқ\x83ġωǑîȀǲŌɖƱ¤ĻĴȾĭ',
                            'arguments': [
                                        {
                                                        'name': 'ĦЙǵ¼ҀȏQͳ\x8dӔŊΗȋļ\x8fȒӧӉӮʭθʤȘ҆ЗǏ˥цӠ˔',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΙûҥǆƄ\x93ˬ΅Ѵɡǋ,нѿ\x95G˄ʭНǃϸЅ˂Ԩ\x7fȥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĵŌϭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȓΎzƙϸ˛ˬĕ}ŐӔ\xa0ğӈĶѼ!àϸȠЖ\x8cĂЭѳ˄҇ҫʮǨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "|êȘíȏÊĠWΝȀѓԖ'\u038búΙͻĩǲͰʾҽЇҚӐ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ħșŕPK',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӼϋïŮњ˼ͳ˾VxĻӲɛɄ˝Ά\x9fʱƆȰ˶ɍӣԬȱ˱ÌȥŊƼ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņό³ӽʞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽ¦ƶâʵĘӈϧ˝ϑӣçƄϱəҩ\u0383ʒҰüԗГщҙʩϐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7005859683203247938,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƨ¤ŵIϑƆˆĚŧ\x8eɗʟ¯Ûӹˑ\u0381\u0382',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˜ɭğƻҴЅǲϙċ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƅȌΪ˞öÊŮƹѼѧŠ\x8cԦϐûһ4сȭǣΠѢðКєǴŗѷȆϕ',
                            'message': 'ƍƨȰKʮѴԋѣəƦȢÅӼËưͲγôÞ\x83ƃӝȐʙ¿ζ¿Ө\x87ό',
                            'arguments': [
                                        {
                                                        'name': 'ʋɭɏŨŏÅÅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭ˸\u03a2ɽ\x94ɓ˝ɾþХ\x8cśƛƅýǀʡƺǺƨЖж˦ȜƳŢǐʓӺ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 597024.963789464,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽԝҌɻ\x8bkӑћӯҧ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҺȍҰѠʋ\u0379Ŏҥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'βԀǍǢƿNӣǳԭ÷ʹρҳȆAʄȆ˗qȩȨzĬϼXͱȐˋ¹Ѯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Δʔ˖ѻ˲ɒǫϧуȩɆFʴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŧ҆\u0383ơүǊçȀ\u0380ʧϐč\x97ɖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԄżϡĠD\x8aˬϖɐбʛʛƞ]ŀΑҚȄ¢',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 724272.186881962,
                                                                        },
                                                    },
                                        {
                                                        'name': 'țĤХŐӲзԊƊԞϣͿˈǴӄŮҀ\u03a2ˍšČģ~ҘмҟϜȫșɦǺ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĜҳéҝѿǖӦ¡ĻԜƶͳҁÜƅĶϽ$ӯ³X\u038bŔďЉ\x93ˍǦĹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˘\x97ʣƽӻԇϑȆɯѸұ\x96АZˍіӐѯ3&O\x92ĞЛͿǚȣñȽJ',
                            'message': 'čɚ[ΛСǵĀɚсњӇҧƉѬΟ\x8d˟\u03a2ˬϱǖØҌϷåҦƹԫͳ×',
                            'arguments': [
                                        {
                                                        'name': 'рǩӠěŉΎЅґ˞HʱƗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¼ŭȋÒҺѣԈƴȾΑҡΈ\x96ʳȼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƤΎȒ·Ͼƚ=ϞЬϓɢУуǁӳ˝ƤѺģ\u0383¼ӤʨеӐÛȗȸҡѪ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѩŪ\x86ϳ4Ǿс˔ƖΔơȱς',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƧĀ˵[ĵҰȣԀϦ"ƺųӇτȃΚʆ˷ɮϣȡΙѓȦŽϔĔƋά^',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯҲųȱͱ˺ĹǃǁͺҿƒԏјʁуÅȨϔӎáςÚƋƆҐ(¿И˙',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'љұǊ\x9eħĝ>ǡŪ\x8c)ΆťͳPӳǡļŸсрǑtˏԜИšų',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȅʖɆȐǥӈҩʮзϷǖϱГĕƔЁϏͱ҃ҌÎҭӎÖ˸Ӱ˲īQΨ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'пєǧÂĞɅɎǂźƨϤϒӞĳŌtҼɌǟԁϪĉ¸ȗӪąǜԗȍű',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҞH«ˇ*ȯ˜ҼHǐŒΪѽҲɒȖҀǍːΐƝԢЮļʟÉƎѡҾ>',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˗ЛŎϗǲЈ·ѢȶưԤϓԡƕ3іӹΚƮʨӻҔМҌʆJˎ˙ϔ\u0379',
                                                                        },
                                                    },
                                        {
                                                        'name': 'źЏȋ\x8bГЫśǰɫʸʯǸl\x88ÔğґƧҔ{Ɖ±ōĨäѓҞЦӭù',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1762833262485010369,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ұ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϔԂ\\ʵő\x86\x81łϫ˺Ү',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӓϋђͷǯÙχŶнӛхҷδοϣρԜâŇԝϜɷƇŧǤŕÐ\x9aд@',
                            'message': 'ҰǙ¸ҬʋĻˤҼж˙˰\x86Ŵη҅Κn9Ұҝ\u038dѐĘƉς²ӾϭîÅ',
                            'arguments': [
                                        {
                                                        'name': 'h\x82ϳϛXҫɜåӵеϵBȰķƲԮϘЧʲʗƟѦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӭϳȀɽ&Ø˸ΎĀԉy´gʘŻѪӳҹıȯǛɛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033425.416909:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0383ȯ˳]ȁɳԁжĕƢʄ\u0382˙ɃγЯƆԎΧéɵƻŤӱ\u038bԨћ\x88ӪϤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 282987.78044140595,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѿ\u038dɽȪǚҠҽďdʨћƌиƄ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ПҲRΊʖŉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΕĊɯÊɑ˺ƪǲЌ˲Ҋ`ŴΊӪuҰɵƧЖϫʆɂʀȘŠˇϩïù',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƂΙЧ\x8dMҲȉӺѲŖ^ȺȽ,',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŝЭΡƍŧʀξūȏԦǒфȰéŷɸϾҖˋȂ/ːхƯʙΌу',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ήҝCРΆҽӇόì@ŌŃθӗŹǣȋƟѱ%ϡ~¨ΠǐΒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ïȇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЇɽɶZʲƏӸ%ѕȅӏƻɩ\x8aȒ\x8bïˀʌхБҠȁИϫÑɣЉδJ',
                            'message': 'ʄΥȞеȑɹΡѣΤΨČ΄ɂǫƃ×Әǆξя˱ƚӒӈϞϗϑЫƣŗ',
                            'arguments': [
                                        {
                                                        'name': 'ȳǶҢīԙľó˱×Жёηϭ\x8cȠт÷Ƌʝ϶ɲЛįǐĢε',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033426.167657:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'İӠȃҜͷ«Ͽ˻ʑϴʩһéȰƫѳdȚ˔˴ӑԏŚηӌƻƽјŤӡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 943625.7580848275,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԍÜ϶ʯ\x82σПӷȍ¤ïʸϞҘŕɇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϡ»',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȱǑО͵:ƭә\x9fˉԛÙдʄѕΏĺȿˏύì\x96ϝÂĲ9ԄȬͶ˝κ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "βӄʔôũ\x82¾Φ]ƶԧϺ`Ӱ7ΨźŁƫöƆīŴ҉'ӌĦŞЗ҃",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣȄξӠê\x9fӵԛEǊʞʖϦ¡ɭчŀƥ˖ԌΨѴȲUˌĜιζÌï',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʈ¶ʇњˊéƙÄə˻\x9diǄϣԖ9Ӳ˞ɒηҼΥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033426.698240:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '=ČϻҘђSçʚƪȑ½ɠˍńҩɚɀӴȁ˰ʘĄ8Ѭǰęӭ҉һ#',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҒƁŕǳįηƷɉЛæǝ\x87Ǖ®ơёǳӲϴɷǷɓ>σ΅ɏ¨óɅˍ',
                                                        'value': {
                                                                            '^': 'bool_list',
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

            'name': 'ƒζȒ',

            'error': {
                'identifier': 'æưˀьӡ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'Ώŀ',
                            'message': 'Ǚ',
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
            'event_id': 'fǣђǲȍƂǙ˨ȝшӣɛĈӞ\x8eɼ\x87ҥĠ6χԥʋԒĖȌʒÙǷ¡',
            'target_id': 'үӃԚǒĀřĊƺȽѿϘËdҝԨїӢäǕæӉʖñΙʋÙΖԫȼИ',
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
                    'event_id': '±ǖµ}ʶԝĆƏ?ԀqǈϡўĺԞЪҕǹ˅ƬŤāʳѿАA͵˶ʏ',
                    'target_id': 'ҷ϶ώώѫҢωҺΖʉӫÃҥͺԬɏԚ*ӺƘӋ§ρƂϰǅ+Ӳʱ˶',
                },
                {
                    'event_id': '\x9aʨȗǁχÛϘʚϰƸɑ˚ǽ£ҋѴͶ˞ȒϾʑαѠȣǪσÆʭѦX',
                    'target_id': 'ӣη\x8bкТЗĢƿҊџȑӌäƻ\x8fēŷʽС\x95ԞѠЄџʧsÅЛͿĒ',
                },
                {
                    'event_id': 'ԭǮÏф˚Δsȃ0ˈΟϷGԩ˰ăӬȻł˷ԍͿÂ¡ƮȮЎ°ʮВ',
                    'target_id': '<ϛðοĦǣǌәƹaôѶΉ?ʄ8āЊӋȝңtɔѝҊќϏ\x82ƨŔ',
                },
                {
                    'event_id': 'G|ѭ˱ΤĸԢѦƍƎŬŊɭ×©Øиǲ\x88ƷЄǉ˘ϮȷïүŀήҢ',
                    'target_id': 'ªͼϤҺ\x94Āͷ^μȊөį˧ɷʬӱΙ΅ɊÍҖMʴŜϓӕĈŶÐʙ',
                },
                {
                    'event_id': "ȤŧśÚʞԗАԝҾӟԕǮʛÿѩǓҨǸȴԋҨçȷ'ϊЦŌҖĿÇ",
                    'target_id': 'οąˈƼшȏŐӬ΄ҊĨ)s Üѿãϳțʯů˵ā`ҦԠώ»ԙҍ',
                },
                {
                    'event_id': '˚ķ\x95"ŞЋŗԁʮńҮȖȒЄȜЈͱӠōξŊ˥\'\u038bxʽʥѹѾƫ',
                    'target_id': 'ȂƓȾ\x8eκкҧĻőӪԭǬƠƇҺŴҞΏɸǿӛ;˼ъˡ\x93%ΈΙʃ',
                },
                {
                    'event_id': '7ȋ\x8eȫϷφҞŻԍƇӘàɃěԞûˤϘѮ°ÄχȤƋŗґӥӽƎƑ',
                    'target_id': '\x88њΏɄUϨ',
                },
                {
                    'event_id': '\x85ѣǫɑӅʪģóēȁΫŁзҤҠͿӼ_Η˜âĶÝ¥в˙ƈϝҢį',
                    'target_id': 'ʩҎĶͻ\x8bУɔϋt.Жį²¯˝ȹΫШ±˖юΩθĭӬǆÕӚǮГ',
                },
                {
                    'event_id': 'ǯFԑżϺѥǺњſ`ȳɠ˳ӄ;șɀѣνЮǀӿǕҾéԆŵŕȼá',
                    'target_id': 'ЖʛΠЇаәαiȸпęҊȗůʰġ´ӱϼӣEΠһʻɄČǿҢӌŐ',
                },
                {
                    'event_id': 'ƈǛM˕ΦӥšυGԆɳƞҤ\x8aΔ˂ƽˮόƪӯѬěƝˊЫHĠӯ³',
                    'target_id': 'әɃɟ¬¬жŚβºԍƊ҉ѵΝǥο˽\x8bҧЊѐӡAuӽ2ӡǆÅÄ',
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
                    'event_id': 'ѡƥoƯȔѴǹƮʃ\x98ʙ\u0380ÇƛʟˀѯŵîĂѷʁąҸЕԑɤԫɢ<',
                    'target_id': 'ϑsβ\x82ИƌĺÇџώźӢàҒѝƔºÇ³ҥȧГ\x9fΆФʇӝʑǵϹ',
                },
                {
                    'event_id': 'ǚϓdŔÔHҔš<ʐfȜǜũРԕӳŲXѲǖÍ|ҴͿʨЗ˙Åш',
                    'target_id': 'ӻӯԄӎΗѥ\x95ҼĮǃΔҺ\x9dÏŵćéǖ¯ќѿǇƮъӡTǰHƼê',
                },
                {
                    'event_id': 'ǇƄӃƗǂóЙӪяǌІαϜҔѸѨʍɩđïˠɽÔ҅ȉ˝λƝđʌ',
                    'target_id': 'ȱöΏѯ\x8cɈЅƧńҶ\x93ЗЈУОάō\x8bϚƌʈ`Ͽѥ\x92zϧȘȿʾ',
                },
                {
                    'event_id': '¿UɎ˹ɮӢýȬ¥ԞʿPƅԝˊԤχoŐ˫ÛǸģΧӽϨҰђ\x92\u0382',
                    'target_id': 'ʨБûтӳH˽ìóΧǽǩӓʢŋǱĽҐHћřţĢёӺϧԏȰbǧ',
                },
                {
                    'event_id': '@ǙŖĤțʪ¤sҺӵЃƋÿǦ¸қğʛ«ýӥ\u0383ωѿԂȭҐ˭ȓҒ',
                    'target_id': '{mȽǔģ{˓ƧĴǪ˟ҫțţHǠΔΌϑɈџӒНҘŵŎӎΛ¹Ț',
                },
                {
                    'event_id': 'ǚêѐȓТΟϹʣʻЭȕϊϡԞŒƒӾңҞ[ǢĮˎҨſ˜ǒ҇©ͼ',
                    'target_id': 'ɎɒŶѵƓ˒ΠӖaӬēȳȾYǗчԓƑåɀʙȺҦ¯Ǧѐªʦ÷ǔ',
                },
                {
                    'event_id': 'Ǳ˩Řǭ0\x7fɩǫ·ÙŖӝΐƺȿϙϤҞAàŇӒ¸ȍ!\x9d͵Ν²Ϟ',
                    'target_id': 'ʑĳǴȋÈѮԁВͲάRǼɯǂΦңμǚľʮ\xadтʹĺҷhГγŬб',
                },
                {
                    'event_id': 'ɖʴĉ\u038dԣ\u0378ȉñ˜˽YǍ×ӆӃlвňsɵĂЇϾΩϰȈθЄƼP',
                    'target_id': 'ѶϾӋɹÄїϣė˯Ö\x95ӎμЙāӆǺϭҹοtφƁԉҔƥǰOqʢ',
                },
                {
                    'event_id': 'ƥϷӏňȾÚʂιԔӭĵ&ӃΎ-δѬӠŔ˧ĨβѠ¹ɾTÈɃҗƟ',
                    'target_id': 'й2Ùɜqţ˺ӅϳʹǠ͵ԥˊǟɿFИā?ҮƽµʪŎЉÓƼǏԮ',
                },
                {
                    'event_id': 'ʜĶǁȶԕρĕáǹЭǱüeΰüôzзԒ˚љӐƀԟȆƔƩ\x80\x84ʐ',
                    'target_id': 'ˁіҖƄĆҋɉȞȣϓϒρқθǝӒΉT˙ȷÓΗϯûǉƍЅšɋ\x91',
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
