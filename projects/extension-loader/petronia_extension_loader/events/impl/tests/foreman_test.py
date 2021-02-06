# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-06T22:09:16.909329

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
                'ȷԈсѺϛƩıԊоΉƬřƪӌɎ',
                'Ӻµϊџ˛ͳДŗ¢ʧɋ\x8cҢѣȦǖķԑƢόүŔȻDƩɀЄvȴĶ',
                'ӇÙЙήɒǀ;°NҧŔϙĔЈТɞƂɇͽʎȃЉȷʭÏϑʧѫÓǢ',
                'ώĹ\u0383ȗƑӾСǃǖǝ²ƌΗоҢюӇÄĂӳȈЮĨGǀӡ\x96ӖŗҘ',
                'ȈªȆƶ˨ҞҕɍŦҸЯŻѳȸҀºӦӖҤʤӪЯǹўGyҐ\x81ɰø',
                '4BȐ\x91÷\xadƨιȅYǐ҇х^šǅȈͽ°Ëв\x8aаѲŻӬʯÊьЮ',
                '£Щ˾¿˨΅ρΞÞƝɯғ±WˡŘνтӷŬ˗ӥçƆ:əə«ζѝ',
                'ȨМƮбϥj÷FΙǭϋťƞҁńψţƘ\u0382ΕѤѝ,\u038bŐ˛Κāшȣ',
                'ɖëыĂǴČЦɵĸµӹάÑψƖѳǷÕ\x97Ǣԩʬ¶ƜÄʡǺǏӷɈ',
                '·ƌ˱ı6ηɓYΣɾğщǝ˝ЌϫϙŕϠǄь\xa0ΨǒϲɢѴOҧѥ',
            ],
            'source_id_prefixes': [
                'ЁǺkӿȷŀʯśͲˏΩʊѠЦŮʘȱeԄÔӧ,ΏéȢɯҳŇźÒ',
                'ƈïǾӸŅvșdӱʛϓʔӯì7ƃœӫЈԅыkϖƦƯ\x8bĲŅVƶ',
                'ЧͲmПЄɵGʝbɨʫÄŕ˔ӂɘξһϬÇƇȻƫσÑԙђЀѸǦ',
                'Ē\x8aҗԈѲȔϸΟПɗˀƼΛ\x82ӞϱӰϓĄuƳÃŉįzoϾ¦Η¢',
                "ùǈƮºӯʠҙЏƕӒmΜɩȪŜЁԐЈ\u038b'˫óɣ9ȣˏѪιѵÚ",
                'ӋǦʄÃ\x8cͺȷҧƟоƼȠ÷ΓЊſ\x85ΠľśԩϢЛǱрƥͷǺÃԠ',
                '3цůǱɝƋÌÜjҶѨϩŜů˜˶½˷ˉˁƠ~\x8bӐʄλɠԞˀÔ',
                'ƭĿѠyАǚιңƃßп¼ʣȵ&ɢΚgƔԠ˫τςƫгǣӔӊаç',
                'ʤќτψҚǽǟȺƳϫǻƞσógáĲͱ{ŴȑѦɵʒϼĮӾɻČɏ',
                'ĮӡžȝѾΑO\x9cÇҒƷŌȦ1Ţȃρˡԗɑ˼^ʇɤ\x9aɯϛŚÕʿ',
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
            'action': 'ȅҴӰbƹ%ƞåĐϮŹʾʽŌ\x83Ț\x94ˠ˳˻ҍŻ¶ʐεÐϫќʿϪ',
            'resources': [
                'ǕԔʸʞ[ɕˈ¯ЦΑ҆Л\x89Ђ\x80Ȁʙг·ҍδѿ´ÌӺ#άëӺ>',
                'Ю6PȖ.ǤϬјÌ˹ȳɨǇ5ѸȃßĲ\u0379πk\x9eͼԭҮϞ\x8bӎʪʸ',
                'HǠΡʻÛŕʊЇǣˠњЄƷǪęίɴƟԒĆǘΝʟBɓιȓȀÕė',
                'ёòԑӝūѦƈͲƌÿΑñŲÌѨǦШɚǳϠˑάԘ^Э&ӻҶǷԗ',
                'šΜæĉùϺðΤʌҌϫcƑӳюӎ©ɓßӟaɑȬϹӚˠӳΏ˱*',
                'ſʁϼʢɪɀϑƖɮСƬʽĴҏ˾šaҷɐ\u0378(ʶ\x82ӻӶzιӣӍ\x86',
                'ˮʿäϲƻˡǞƙÛfѺ\x824ŗӪҀȦԫɇøˆǏ¸ƓƑЪ\x8f˅͵˴',
                'ÞɾУԈӆtǄώòʵçòεѾΛԟ@ѾΗˏɱҚT$ˑ«ɭÍËҶ',
                'ϲƪ¾ɏʱӞȳҤƕǿ˭Sʄ¡Ƕ³\u0383йҧҀѳҷӽұmΠʙľɔǗ',
                '˵ΣϤǣ[ĖŴРȈԄũυƲĥ΄ӚҪεĠŭѺŕhǡ\x94ͳĠ\x8dţʰ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ķ',

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
            'name': 'Ű\x9aoҧȨ"ŗǢʏͺҚΐϕȝԜȹ\x80i˅ǲˉǈ3Ó˯ȊТ\'ϥƍ',
            'version': [
                -6046050916215313321,
                -3204785425583055328,
                -7676688063786045045,
            ],
            'location': [
                '_TϊơǼҰϭ˄ȸЦԩѭϚѫʩ˄\x8fϊяЊÕҌɻÀĊȔ\u03a2ġҗŰ',
                'ĿǩˌÜʑɣ˱ůӞЉӃҕµĒϑƂŧұӝƕӆķ˖ȫĈlρ¬ЁͿ',
                '\x81ѫƎk7sɘвĳ3˅ԖӉїɳɅР·ʲ°ǼȌӄϞ;Үйҟͳҁ',
                'ғωȤаԝǎÿӦ;ӧҁŵԔŵùťҩϲǫǃǧʊҢȷĤƀɚɴȅƟ',
                'λźѝɚԗˀѭΚ\x96ϹЍћɓѷ\x93ų¿\x97Й҂в\x97Ŧ\x9dѻӤǕŠkΠ',
                'ƟԦ\x97ƶȱŽӃχ§ƆΫƄϛΕҟѤ]ǳԣƥԃ¼ȝӿŴˁϼʠϾѧ',
                ']Ɛ˒Ɗ˄ьԚӰƽȓβȖǽýʩɜ§ҞŤ˞vÜƃȜžʢɋƋƵϹ',
                'ҷǬғԈȦ5ȹȰΞΝƄԨʰɾθȯÖѼ\x89ӡӊ˵ƓӫƅȗӒȏЧŏ',
                'ƛrĂ˔ĿşͺͽƻӿԥưŢɞĖģƑĨюͻҵϏӶϞѧȡ:ǫ˪ѐ',
                'ťԒǅđƷɥǴŎюΩЄӳƉȓ\x86ǀžńYßþ½ɛǡlDƟƏ²Ϡ',
            ],
            'runtime': 'ϰϰƕʦӕԓӫƔÌ',
            'send_access': {
                'event_ids': [
                    'ȻƁ˨ɒҞэ·˭YӡśӝŌщĸʂΙ²ȃʹʧĆ·Őʕ˘ɗſѢԧ',
                    'Űԋ$ԉ\x9bȇȰȃȁƶƒaǘ˾ʾìÐʃxϰѠ˃ΔɒʠǬ˭=˔ҟ',
                    'ǣʗџˣӳ΅ѐԁӰuÂț˫Рųϖϧ×ԓʅҗҙԎß҄ňόԫиȳ',
                    'њɨӱɓм҈ºʝɿχԤμ4ǵωӺɆу\x99Ȳ҃ǌʂǥ͵вçcҕԬ',
                    'ēșДâӰ͵ϸʯѕȹɦÔѭӗЈľυԥeĂŦúʪϯğǥɞɟ[˘',
                    'ǒƣbʫ҉Ͼƕɏљҳ\x9c3~ɸŔЏɯћѬχÙ˹ƹʵ\u03a2ЂɻʄɄҠ',
                    'ĜƚҩʞñƨԖɤϴНÝПÀƹԌŜ$\x92ź˧ΓǔӤ°\x8fĲˌ×˜Ϻ',
                    'ƁӼÛ.ϮɓwϕԡòŔǻ0І6ΡúĠəÊȌέКŀʊIŶэԨī',
                    'ϿĉʜҿČˉɲĢԘЗԍĤƢҗЬ,ǇƷ\x94ƣԟѼǎЙ\x86\x9eȉĦƺҀ',
                    '\x92¨Ν+ʊ9ԜӢс˟ŰǏ\x9fwˣŭͻīæćßӎLʋɢHԝΙ¼Ӌ',
                ],
                'source_id_prefixes': [
                    'Lŝέǃ?ΎWǃ·ĴvѲĠ\u0379ŕʜƆПЃɓȇ˒ƄöɦʵͱƝғù',
                    'ԙôŞŌ΅άѹʕϿϧͳ%ͺ\u038dԪʁ}Ʒсϼʕɨ\x9aСԅƩ[œȸÃ',
                    'ţɽϸáɬ|\x99ŠÌƼќþЩöˢ˴ьҸǡȊɽȷɼɶқөȅ¡ӢТ',
                    'ҍ\x91ҥӞϕ±ύŜԡҡȁŁаШĖӿɩćŁԉӵĘȊӐʗʛ\x83¥ҼЂ',
                    'ԚĕƄ˽ʓ\u038dӺƤǇżŬJŜ\x9eһӞ\x80Ϛȣʻ¾ѪəԑήӢģŠɀ\u0383',
                    'ΨǆĎŦǠ·ӝϼÓˉɦҦxҳεϓƄҺɞøȥǙеVƭ ıѝƙǉ',
                    'ľćКԩ«БϖİӼ˅ʋƿCņʳѧӳϜǆƜѳƳҥæң\x82\x8eÅҗF',
                    'ʟ\x8aʘĄÒʆƷǢŵȒҒͻӒòɶͳǧͻİ]ҞҒžщiќЂǴìǏ',
                    'ȩЀіȝͲʒɠŴǠʩʀˑŨͰΌΤȅÚψЬԎʇʀ˯ŞŢŀ҉ӊ˹',
                    'ˉıCżїɿӘVːβ˒ΐ˫ӷȹʹ¦ƩғˁhǒŋӕѳΛƭɧĬŀ',
                ],
            },
            'configuration': 'VɷҴчάȵİÅ˔ӠђƤϒμюΦѥѿϼŏϺǍԟыˊғŲȒ4Ś',
            'permissions': [
                {
                    'action': 'ʸʜ\xa0ƘѺćÎѽҨɆ\x97҇ʁˁɨ%˂˟ЂόΕɃďďʁ\\еʥЇǻ',
                    'resources': [
                            'ľɗɑȡEʄȹx6ʋϿőЧԆěȹҵþɴɣÎҌŪ{ńŲKԐ¥Ҭ',
                            'Ė\x89αĴ˕ƭˉјƝӧġ\u0379хvɿɁƐηƁҝҧɏɫԘӗԑҸƝǀ΄',
                            'ӆΜÜϱΞϕͳƱΝԠҡĝɶӷњïƻùӈњƧŭĂҚͺ\u0378ǽɂУǼ',
                            '˖\x82˔ÄӝѦςυϯƉѶˉĕђзǅƹŗɄĦȈϙʇѹȏӽϩӋBϲ',
                            '}ŞԜɖһďεЂκǻӥӻ˹˷Єˬʓҹ\u03a2÷ԖɁάИǸц˾œҢӾ',
                            'ĚѨēӔǮӈȬͳÑ˦ȗϒʋ͵Ӝ˷Sʊɸ)ͽВԣˮϮȋș˔ͳҨ',
                            'ѲʸϩϻƭʢЉϺωμΧпѢбɶĪƥҭԓŋ{ӾƊіȶЪˏЈŰѤ',
                            'ͿƻǌԄğэ$ĳү\u0379ѹӡԘЫǔӔǩéҮЖǳĒðЯĒȼɱƐ0ӵ',
                            'ɮӪǣΉДʡĽŀԪѺмԋĂ\x97ɱŌѢϾ҄ÄςƉǄɗŌѬȃˎȇϫ',
                            'υÉĺԠЍϽѷˡҴҫɴϭҤԨɔϢ҈аʈΫҺϻӓʯϸ\u0383Ɇί϶Ť',
                        ],
                },
                {
                    'action': 'ȇƪʀĶşʜ³ѠȔԒʩҝһřӻ¯ǛČРΗɔύүĝυɂњ2θӪ',
                    'resources': [
                            'ǾĜÿͲŞ{ˍә¸Ӛ\u0382ЩǙĜľıҘʢ\x99ʮƚǃѠ_ŋɒ©όĐҨ',
                            "Èɳ\x91Ȁ1Ĕ\x93ÁǘáӑɸÌƿχșȧΔÛ˛\x81¯'ӍѡJ˓˨ѠЌ",
                            'сɽôґ\x89gȱȽ\u0379Ѫ±ʘqұα;άҵ҇ȌԢ\x97ĵŚȄ~˷Éûų',
                            '˦BâλҧNз_ϗśÞЛ˅ɽӛƄʒǫ¶҈Àf˳ǛγŷʩԥͲĵ',
                            'ǦǰϾȯĭϷϒĹȑǖ\u0381ҋ¯ʪƲɎŘWǵ˭#њóПė:ȏӓǈԁ',
                            'Żͺ4ӿӹƢĺƶʳԞɼĕ%˱ˬȬԇӐÖʻΖŘ\x89ԨŎΰǗЩďʔ',
                            'ś\u0378КλʢöŁʮԄȍ\u0380ЫϞԅşɏѠġӤȩɛЃѾ\x9aýӈțÁʪɤ',
                            'ˡͺőԎǐʤȍѯµҹȧГηϐԙňљͳӧȝϮТŏɨϞҀåaΦʀ',
                            'ϾMãƕǚӠΫȚξԬGu\x82зǨдĬГʹƙĈɐƆĭɀȤrʲɢʬ',
                            'ŀşήƱϬӍȬΤ<ьҲĈԔǕʥͿ҃ӃґǫȌƕÈİɢҰf}ƒ϶',
                        ],
                },
                {
                    'action': 'SǫҦƚҵϡϞȪщǣǂ(ҢҖТ4ΣҵƇҘĲĥąѥҬгѥҢӢɢ',
                    'resources': [
                            'ų~ζj%+',
                            'Ŷ^ѤӁѳьέǂƍ=ŤΙƲʆĦǙ¿ɦͺΰɵ£˗Æ5Ʒɼ\x99ŌĻ',
                            'ʈϨѽѐú˯ȝСȆǫѬœυɸҔõΎʚμԉ˾Ѳэ\u0380ΑϽ҅Ӄɷ˩',
                            'ÏƓ˂Ϻ+ϙԩǜĨąšǌӌɎͶϼɎ˳ϨǏПˍͿпĲϚ҇ÀΎ˙',
                            'ƵɃcY˕ƇƂҧѨИԬʇƋĻӦƥɤίԗǽԬĎɸʑÑĉ˖ξǪH',
                            'ʖdˣʤԨĎVӁǇȪ(ҳϪ˫ʵҼɛ!~ƨϐѹȑӱԤˬѨԝ6Ȱ',
                            'ҿȶӖϧĂ±Ӱɿ\x9cɃǴ¬ыʕ!\x8bĄхʀұ\x95ƽʭӒ϶҈íăŵԀ',
                            'ȘƈԖ¥5ӷÏ҆ȈˇӖãmˇЃщωѾ\x92ҐžНԝϤȾÎԞɃʪì',
                            'ǠӟϴǗǀαɈҍġ¨âѣљƎώ®ʰԈOΔѺӪţ~ӼȮĆčǺќ',
                            'ˆιȑԨǈYŹӍӆ÷þԛɁѻïӚúӫ ΥôҕϰɑÐЮΦƋχɲ',
                        ],
                },
                {
                    'action': 'ѰƴРĒϠũª\x94 3Ѳұʸ\u0383θǫƷрǖkǨ%ʥČƧɦтƤǢȫ',
                    'resources': [
                            'Ξ£ьʨ\xadҺȜԜǢNΆɀКĺ^єɽӋȘƕТ˙Ҭƹ˚ɝɶƟɾΠ',
                            'ǧ5ɬМȳєФҔІΦʩāɅʢǪțÒ·θğ˜ОбрϾ\x91ҸЏ˙\u0383',
                            '˷ƸŽѓŪӌ˺ɣҬ\x95ƈψʓɆԠφҿʻԓȥʼʹҌԎēңƼƋѡθ',
                            'ɷԋԣʔʫ]ǱyӳǮ?ȴśːǼʠ§ǋ˹ǺǜӫЬɏЙǼ˽ȬԩȎ',
                            '҆ŉÚЈͷηƟϧʂȗĂĨ\x96²ғϨŽԩªмƵǲʾ\x89ʊdΞԋё\u038d',
                            'ѿΤˋΛů\\ˑǮκ҈ŃǰƚҚʐǋ+ħѓ˪ÉxƌĝȿОEŎGH',
                            'ɣЈƨӬȼŅҦΚӺԚɖŜ˛λPǪɃшŴÕԐ\x96āηǻӃ\x8b\x94κЪ',
                            'ǤжԊɏ/ǄʧʭɎЭʛ2ƘǪ¶jHȃÃҝě˂ϣΆVԡ¤pҺќ',
                            'ȵξɔŲè\u0379ѾĻщ"đšӿȨɒњˇľԅőĉϹ¶˝ǝÕʈŮПà',
                            'ǆβǞҴ&ìêӴ˸ßàССψҧĿƨԬʲӵԌ,ɻɉʅǭΕΏϐѓ',
                        ],
                },
                {
                    'action': 'ǧԡωeӘȘϹѮӌԂԠбƬƭӖ§ũϧӓɏˠǧƃϑʰ\x81ԙРʡф',
                    'resources': [
                            'ӟ˽о\u038bɆ˞BaüȪѥƁń2ыΗͷЧҫͲĪѫ˥ԦȖȬɄŘҹź',
                            '6ҊђůGɌѧԨŲPԞϛΙЀʏżѯā\u0383ɂҿԢР/ǏԑǫƘĴ¶',
                            'Н=ΟèßЯƫ©˗¼ųǖƮŰ.˝ʬΗʖӔӔƝɇхVʔȎ\x9aң¢',
                            '\x9cŊʔɦςɋʟ#ЖǫŎӽϽԫвȴαÜѰϮĺħ\x89ϗƛʪ˟ӸЏϹ',
                            'ǢĜƥ\x9aɪʦǗ½ӝӂϧсêμөԬÀӝѮϚŭ\x8dԗɻύϟЯѥҶ˷',
                            'ҧ\u0380bɳҺÿʲ&ϣΈοАMŵƵФBɎʌĲș\x8fˇԄȨЃƐ҂¬b',
                            'ȟȦѐϜђͺ',
                            'Ԗȃӡ˼ɋǛ˂ǜԢӂƣɰŧʰʈ}Вɳȝ%zĦιӬӅԁӪăǴ£',
                            '\x91Έұ(\u038bҨѩǗѫ«¡ОÔȤǋýӫǥƋǌҀԇŕ\x94V\x8d\u0379ŗͼş',
                            '˛ӖЦΘĬԍѸíˀɔӭ%ӊɆhǿɔɌʨϒ\x8cuȥΤӶµЇ\x96ʠҕ',
                        ],
                },
                {
                    'action': '\x92ЯħìǧļÈď',
                    'resources': [
                            'YΚưȥǔu½Ł¸лӿǴё\xadʠӝͽХҺˡǾƛ6ũ\x9aҖɱ϶ƶώ',
                            '\xa0Î;\u038d3˫İȶƭʽɄŖþʖʗŔˠҢńӐΪʀĻΫĜƆҐĢǈҊ',
                            'ϖɎĆϞȩǻDшǹʸȫȅϻӦ÷ϋɼΙн\x8aϋŎûѲϕěǈԨsȍ',
                            'ѾŅɤӵДÿʁĂŷ˹ƂЏϪӃȩҜʴŭΙʋԬя҂ԭΈ˚ˎǯҩD',
                            'Ûƾн˜¿ӒǴPЖÖȼзҞѺрƢˣńеψξǊͱʧôċΩĴӍԁ',
                            'ȋͶŶȣĨ\x96âԡ\x93ŗƒχðҽųλ\u03a2ϢQĦŐҾƍ6Ҧˇ˖ԬƁǅ',
                            'ФӋαӀϦПј9џѐϼѢ˲ŒŹɒɜӊИʇƣΌʐʅӰɻƛуǊŻ',
                            'ǫԡχƭɋĽȕ>9ƖX4\x83џǸǑʦӗɑʑъȿ\u0381ЉҥĩѮʈǇϵ',
                            'ľéӪęϫч˾ǭΌ¿ϓӴΣԔдƹѕΫӖкʲΙѥ\x92ӜͰԤҹԘ±',
                            'ϴѡcҹΗɕòêʥŬЁhƉȳĤ΄ŬΘɃԦɂ҄ǻҏҼԘȯLҦͲ',
                        ],
                },
                {
                    'action': ':ʹ¨ʋԃǗͺ=7˒ɞɡԚЛšşĬXҦ҇ŰǪλȗΐϐǡю',
                    'resources': [
                            '!Ұ',
                            'ϤƄԭԢƵ΄ūϬѭ˫ū\x95ϜȠϬӯǕĲ˘҅ƔʹʆρгUԐӅңϙ',
                            '¶˙ΧľҕҸƮ˼ҢçΚɁϾǲ&ɆοҦϚǃ\u0381ƹрәδӱϢʌƬю',
                            'ɹϟиԃǯΩƼǆϤǧпũ˃\x84ѡбȤȇʑΡŒɻ˥ԜϏtƷԃ+Y',
                            'еʐŋǂȡɛЦąɞõн8ơǀӟҶҍҐϋŊß·',
                            "уǃƐѧҋŲƹÖӝǸ˸Ƣԏ΄6Ӈ\x95ǆ\x8d'˪ʕŅѢя˥ҶȰʈĨ",
                            'ÄʛВƏ\x9bѤԏҰƂĩҟѐǚȂΧ˸ȇ&ƮɍăΓтӿʚȡϼεžϩ',
                            'ţXӢîΐєɳάͷ\xadxǭĕȞǶѻÓҴ§ԬɛvoϷƬ\x98ǷÀѸϮ',
                            'QǧԢʕķȱΙϞ\x86Кв˱¨ӔϾТIΪˊ4Ä˰ѡЈӮȔΈЭĊ@',
                            'ʇЅ\u038bóšɒ˩EюԩԃvУʏȅлѽÂƱҮʍ\u03a2ϝʥȦдҫǀäǲ',
                        ],
                },
                {
                    'action': 'УӺ\x9bʅ\x96ȼǥΧԘÞԒ\x93ΘҪҲҮӴȓjʌϧɗ˼ѹɏ˓џ÷Ɏй',
                    'resources': [
                            'űɲҾɯŘȅƿǟ~Ăpвξȕ\u0380Ȩ=Ѧ©YԌҰʉ]˂ʉκǔȑś',
                            'Χ˚ŉźҾƿºОcƞ«ўԎӣҨΞɃƿОλӓǽʤāÓԆʝпЇӕ',
                            'ůԮcӦ҈˸ƸЃҞʀǐѡϣǁδÝ˾µɁū9ӫ҉ʪӱñǘϐғ',
                            'Ίd˹ϑƭòƒ˫ʏѫɇɃ˸ԞǏǠǴŒȽľӹ҇ʏѩƲʹѡ˹Ъˇ',
                            'ѶŘΔ҈ǜΟȜЛĸȥʹϞҦƨəЏſς˖\x7fуҮɥGŌЭҼӅĔӊ',
                            '.ıȘɣƪ¿¸ΖʿϟòeҚȰҘʚƱϺş\x94˽ʘ˵ԦƟƟ.әԒȟ',
                            'vćÙËĳϋțʿʅā˶ϻ˃ÀƑȭѶ\x85¤ΝԦŋѶ˖ҟÐԟǽŹʿ',
                            'ͼ҄ǓǼˉƒӁǪȵӻϝϕǃΒƒŶʺѷδϛŖРϙҹɄƐʭӚ\x90ͽ',
                            'řвɘ#ɸΣŰΩԅӜʅ˳ŗaŐÜˉŵʍʤēǋ}5ċĶ\x86ôЛ˽',
                            'ˣѱŬɿƘ~Ӛ*ϑԚǀǛ˪ƻ\x96ǝòӚҹ5ӿΊˢ\u0381vǡśϖҒ;',
                        ],
                },
                {
                    'action': 'łÊЊɼʸFè˼Ěƺ\u038bʻσċłÐϕ¹˲һŗ˄´ΕѪˈÊΫӥ2',
                    'resources': [
                            'ѠЇǍΐƲĲҲ;~ˌѪƠʞɽќИÆПБŚˡӼԫԜǅ·ųϰǕѥ',
                            'ȀÄãǊљɒ\x81ˊãĉЄƂȵŕėÃηǘ§ê\x9aӓwȠNƸӤ·\x87ʗ',
                            'ĻňŅ[ϚгӵтʮɆ8Ʒˍ´Ω³.ӝƀȢҙюњ@˄ňВ҂Ģб',
                            'Yå\x8fĥѥϷkϖЯŻ˒ЍÓɓίŅ˔ʾ˺&ӧɷȳƙѣǯΏɎҴǶ',
                            'ʛgƲҦȑʎîжáETÙΝШǦԑНΕϟġҒҠƓѪЄψĪԠȧɼ',
                            'Ԭľ>οѕǆǕȃӮǅӲéŌ|іƼWԃʉ˯ƒʚ\x90Ѿ^Ñ\u0382ф\u0381;',
                            'ѡǧǞ3ė¥Àϑϐ}ӆεʕΩˏ~óΫȑƞŋӲ¨ʢɆ˙΅šĻƋ',
                            'ǎĻ\x9cʂǕQ\x8c˗}ҩƁī˝¥ĒɺǋωǮίǊÖźϟƒΜĄРϟĘ',
                            'VϽƒnђÆ¾ͺϨŲOϡ$+ӿӚԍёoBԂгqƥҩԈѿԌʆB',
                            'ț˴εiӨΰ\u0381ğŒж\u038dðʡԓd˾ɕ˵ҵɷƔȐɁæԍȡğ«Уȇ',
                        ],
                },
                {
                    'action': 'ȜɁϢǂϕεҪȔqʧɞʱŅѫϋɘцǲɩ҉жϫˋӋņɕԑŇԆƎ',
                    'resources': [
                            'ηЍцѲѝϔΙӃQϺԗӯуÚΆӫɨ҅ϿɁħеǏƴȴŉԂɼΆΈ',
                            'τƎξǍ<ʀҜȆѱȪɒҬƨ˽-ʖԒǫuƨʺɅĹЫÍWДĺƳQ',
                            'pǁҦƊȎ4KЁZ҄ıҽ˷ǼǙȘωµЦćХĵĞʂӯFǱRӉҔ',
                            'ɣЛȌǮϸζˬʭńӎγѣяɬǈĖ\x7f',
                            'Βӽ҉×Ѵɂ˪ĘїӋ˒őŮɥ͵Ƨğʭǃ)ɴdͶэлYWļʎG',
                            'ƍЬĪǅʶRĵSŷÜκѹӸӲҾʢāϓҿ΅ġ˷YЏʠЇϡǜăŮ',
                            'ðİBѺÀӁ˂/ȗǐƾȓɲǍϝ¬ǸӊǼ˦ƭƫϤŦƯҀǧԃąƉ',
                            'ԟɽԑƼƢδƈȫďο_ǆȟΤӬΆʂơƔΨʧɇΑʜÞҾøɣӪŎ',
                            'ӡƲӓͼɬːΛЩӺ\x92ɀǆȹɝˆüƇϱƞˎКƿĚψ}ԓƛӴΩЕ',
                            'ǡpȮìýȯ˾yʯϡ]¨ёːϣȒүÞѪ ҂\x8fQǑǉȭÐƵȑЖ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Й[2',

            'version': [
                -7353061599422729036,
                -6021717167784029842,
                -4793989397813751531,
            ],

            'location': [
                '\x98',
            ],

            'runtime': 'ɶ',

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
            'name': 'PʼȏƈʠψԝЉʝƮĈѕȎӰƹǠƉԣΆƬɏƅʡž˩ҳĐOʋ²',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӊǞȯ',

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
            '$': 'ӸǰŜВԂǌƃƿˆӇӣϜɛόѱǫүƧУҪѰԤϛfӆԬКɘԎ4',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -214882492621024317,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 469435.45183963317,
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
            '$': '20210206:220916.795472:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '\x7fɫȖгɕʬwǄßþ\x8e˹ӫÎΨЇƊãʃɊτOΏԄƓ\x8eǹȞ\x93ɯ',
                'ӣÏǻ²ˋӣj҆ŦƩϣѪ\u038dўřΉϊä\x9eѼłʞĽЂћͱ4ɯwȍ',
                'Ѭûүŀ\x98Ҹǰ\x89ũѴ˽\x82ЄǄχғʭʭ˰íʵǌλƗƢɚҔþÿȺ',
                'ǼѹςѿÒʻҪǅъβЪȟęȰϐǙ¦Дǹ¼Ǩưʊąɐ˼ŪƃӤǗ',
                'ӳPϼʠ*.ЦҁӶӇ!VʀŋκϭʢӅԗÏnҴԔȟϚáϸƛ"ƽ',
                'ĤJƎưƆͿКÈŲǄ\xadӯѷ\x9aǆčΧǁƵ3gȝƻ\x9bӜéÁνčv',
                '˨ąѠńǺʷҀπϭ\x83\x91ǮǯɈѻсƹ°о\x8aѥêϪˁуʨƝӓϺź',
                'ϞØ\x97æƼӝИĺԍƪνȊĖԣџ$ϟ¬ˊŹĖʂv\x98ƓӰԅɟˠα',
                'ŜͿ;GɵʃΤΏʫ;#ÓȣƻvÞĽ\x85ҎÌG)ϘǪɋѕӡΉԆM',
                'ҚʼʩɈǄĪӋǖǛњ˜ȔʦàΆʶϨӾ\x87ѼAϗʽȕ¸ÑËέбћ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                502875598451807141,
                -3338923544459729963,
                8839696646563174625,
                -5112273828461759537,
                -4423412272557357343,
                -4650497782145733405,
                -7296412752187986271,
                6728231650490722052,
                -4860117680878127679,
                -2910534551696083136,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                499775.4261975812,
                422442.85299745767,
                694807.3801644063,
                794836.952862714,
                274746.7569882887,
                -37901.1634958807,
                624138.8015327515,
                951698.2920406531,
                323532.95934412046,
                39429.25374824167,
            ],
        },
    ),

    (
        'bool_list',
        {
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
                '20210206:220916.797498:+0000',
                '20210206:220916.797527:+0000',
                '20210206:220916.797541:+0000',
                '20210206:220916.797553:+0000',
                '20210206:220916.797563:+0000',
                '20210206:220916.797574:+0000',
                '20210206:220916.797588:+0000',
                '20210206:220916.797604:+0000',
                '20210206:220916.797616:+0000',
                '20210206:220916.797626:+0000',
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
            'name': 'џ\x97¤\x86YũҪƎšσiʺĮɯǘȕð<ɑǻˆРК',
            'value': {
                '^': 'datetime',
                '$': '20210206:220916.794959:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ԋ',

            'value': {
                '^': 'float',
                '$': 276548.6013752039,
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
            'catalog': 'G˟£\x8a˶ǾΊǘMӵǑǮǛkƐɧĢɠźӣEÈôĊɀõŭþѹӊ',
            'message': 'ŭΧ ҖĄÀi\x8dơӘέʅʾ҇ǡȅБɘҢΊŰ5ƛІҔ\u038dͶkЦȤ',
            'arguments': [
                {
                    'name': 'ԥŤѐǷФκtѰbëԁĿ\x81ГŴϱҗAʎʮўΞZ',
                    'value': {
                            '^': 'int',
                            '$': 3643108561376273950,
                        },
                },
                {
                    'name': 'ϑǓϮǔʆѴÙīӁǓ˩îӎѫòǄǰͿӄΒÔѧƞçʼϷʀƬȲɼ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'еˏ˒ŀŒǜҍÞ˙ТˡЌvȝˉt˂}ƴɸĻ˕ƭРҘˌîȁƷҩ',
                                        'ρòĪŦgЕƇѸҭ˩ѸŧζΧŎȯ˴UԒǌѦȪ˴\x8dӊѿāɉюį',
                                        'ҡĻɄәʈȆyόčнÉԢѧΐ˾ǶΐŦüԦϘѡƸҐӀϧİƵ҃Ƭ',
                                        'ǥ¦ĀѪ\x87ƻzĻʣӲϺƳыŬ\x88юӅͱźȌͷ˓ĜѓǠԞнĶӏκ',
                                        'Íƃ\x91ǲǦԠů«ӸVXůŢɺпǣɹɪǰ˘\x94ɟɩҿƇɚʲΗƌʨ',
                                        'ӈfԭԝēӯ4ӵƜǖˀ<ζӋO)ÍôƻȩΪѝЫСƛɲˢʋʍ҄',
                                        'Μʉәʚѱ¬өԙřgѶϑVϤĎj\x95\x86[ΆKɢ˯Ӡˌ6ԣ\xadȨӼ',
                                        '?УɾƕʼԑƖhǮɚżŨуȳϵΪҗ\u03a2ҚÆ϶ΏԗŅàGӭӓć«',
                                        '\x98ʝʫɌÃÏʣĥǑ\x89Ϣ҃çƹϯLλžŗғĚўύ°¢Ȧǰϗ\x8cū',
                                        'ʢрWЎσӋч҂ĞǪΈЭƑƽïšȍͿҭðЃȈʥȗûϮǔ4ğĸ',
                                    ],
                        },
                },
                {
                    'name': '˰ԒŎȺǄͲӚʯҪр\x9c',
                    'value': {
                            '^': 'float',
                            '$': -66790.45484580545,
                        },
                },
                {
                    'name': 'ΚīӦǈ\x93âmΫκōĽ',
                    'value': {
                            '^': 'string',
                            '$': 'ÒņӠ½#НɥɿїŔHàΒȂҺѤ\x8a¡šCÅӵӒϳʍ\\ӑϕӆο',
                        },
                },
                {
                    'name': 'Ʒ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ӫÑШҜQŁθĥǁǼε+ɳ˒©ȟЁԥɹ%ӝÍ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210206:220916.791964:+0000',
                                        '20210206:220916.791988:+0000',
                                        '20210206:220916.791995:+0000',
                                        '20210206:220916.792000:+0000',
                                        '20210206:220916.792005:+0000',
                                        '20210206:220916.792010:+0000',
                                        '20210206:220916.792015:+0000',
                                        '20210206:220916.792020:+0000',
                                        '20210206:220916.792025:+0000',
                                        '20210206:220916.792034:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ʁɱԡҽȳPʄb¶BˮАɗ˒',
                    'value': {
                            '^': 'float',
                            '$': 919847.5296862421,
                        },
                },
                {
                    'name': 'гǋǪʾĀÀȵӍӎђ\xa0ɫȷɔѭ-˻ӪĉԫƜҼ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210206:220916.792810:+0000',
                                        '20210206:220916.792834:+0000',
                                        '20210206:220916.792846:+0000',
                                        '20210206:220916.792858:+0000',
                                        '20210206:220916.792868:+0000',
                                        '20210206:220916.792879:+0000',
                                        '20210206:220916.792893:+0000',
                                        '20210206:220916.792907:+0000',
                                        '20210206:220916.792918:+0000',
                                        '20210206:220916.792929:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ʹƑˬLƆѣĦēġȖʎƺ·ƱщÅÛ¡ӨĦԁ˔ɼҴɊӠϣӨɄú',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        655537.3033122785,
                                        668643.8785101345,
                                        877861.1499512608,
                                        456510.65589018585,
                                        975874.0292665423,
                                        936135.2784351638,
                                        238420.89911753027,
                                        33143.65218291397,
                                        -41682.963210543254,
                                        688302.2140310706,
                                    ],
                        },
                },
                {
                    'name': 'ԧѸû',
                    'value': {
                            '^': 'float',
                            '$': -72810.41312739305,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ɼŹ',

            'message': 'ʾ',

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
            'identifier': ' ēϋRҞϥĜˌЮϟƝ)ʞʒąѥʕ\x90ƓӬ΅ɓҰΚԣћӲ1ɽȜ',
            'categories': [
                'network',
                'network',
                'internal',
                'file',
                'access-restriction',
                'invalid-user-action',
                'os',
                'invalid-user-action',
                'network',
                'configuration',
            ],
            'source': 'ʳӺјʭ˰Ǝ·ԇʽάĄņΡҽǒɟɫɬŁˀΛєβȼQ\x91ɒſß϶',
            'corrective_action': {
                'catalog': 'óӝ˦Æǆƾ\x9bȞɧȑ\x8bύȁǞİ˰ȬơƊş±ʹԄ,Ӥƻй²іɎ',
                'message': 'ѝ\xadŰǇќWҿϔǩ¿ΓɦцΒїͽΚʥɤ6çāz˰Ѿ¸ѯҞ\\Є',
                'arguments': [
                    {
                            'name': 'ơӌӖ˅',
                            'value': {
                                        '^': 'int',
                                        '$': -2218883140355378392,
                                    },
                        },
                    {
                            'name': 'ΆӌľƔɀȹʝЪǋǶȥͲμЂӣɢάŔȎ_p˗Ǟ˥юȆӖșӖˮ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -5214628744372175043,
                                                        2918400575555070883,
                                                        -3166837297908209294,
                                                        -7768875073669666645,
                                                        -7448021363812769515,
                                                        4297440698017868087,
                                                        -8450596499211594085,
                                                        149209337110904049,
                                                        -5967164730204918262,
                                                        5884111040729487959,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĄȽŠÊ-ȬʁΕ?',
                            'value': {
                                        '^': 'int',
                                        '$': -145504926616831484,
                                    },
                        },
                    {
                            'name': 'Ӈəȓr˳ЂɊюå΅ɞʘӔџԍʕӬʼӕҬдҙбǦƊɐTɂҐʃ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ǶЎΓ˝\x8fӽˠ¬ҶŃÈίŽ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
                                                        False,
                                                        True,
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
                            'name': 'ǭѯãԆ0',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -2537639895528830908,
                                                        6619516607478814410,
                                                        5583835756953917916,
                                                        4262797472742062884,
                                                        1508949861189102655,
                                                        856309840309378531,
                                                        -2471919982492386735,
                                                        -7435452301491511547,
                                                        -5153845626398782885,
                                                        -4152345293399020506,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӂҪǖÐĶƕˆϬпҭʇCFΐ0ϙˡĊ`§¶¶',
                            'value': {
                                        '^': 'string',
                                        '$': '¯Ȏ¯ǎœ˅˴ƙƦʦÛġϲŞƹ»ƢԂlͿʬϟύůo:нȲˍğ',
                                    },
                        },
                    {
                            'name': 'ЃȰɍǙπ˄ʱЈҷÂý҃ϳțίCdиŤҿ;ǳ\x90ΊÙŸǱɦ\x81ʺ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220916.787191:+0000',
                                                        '20210206:220916.787338:+0000',
                                                        '20210206:220916.787353:+0000',
                                                        '20210206:220916.787360:+0000',
                                                        '20210206:220916.787366:+0000',
                                                        '20210206:220916.787372:+0000',
                                                        '20210206:220916.787378:+0000',
                                                        '20210206:220916.787384:+0000',
                                                        '20210206:220916.787389:+0000',
                                                        '20210206:220916.787395:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҦоĤĬиѦ\x8a×ϻǀ§ɨЌʖȨϊŏőǐĎƪɀҖƪ϶',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220916.787824:+0000',
                                                        '20210206:220916.787973:+0000',
                                                        '20210206:220916.787995:+0000',
                                                        '20210206:220916.788002:+0000',
                                                        '20210206:220916.788007:+0000',
                                                        '20210206:220916.788012:+0000',
                                                        '20210206:220916.788017:+0000',
                                                        '20210206:220916.788021:+0000',
                                                        '20210206:220916.788026:+0000',
                                                        '20210206:220916.788031:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӂͰɗ~ѪƞЖ©ż±υưԟҾЯзӬȍÑΉюКŴӌĩϤɇ\u0382ƚ˥',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        104161.1096251834,
                                                        959743.5672238364,
                                                        162928.940251077,
                                                        88335.16066366184,
                                                        451262.6641579246,
                                                        788523.3359899307,
                                                        577718.7123788629,
                                                        449014.98583149107,
                                                        930823.7062178566,
                                                        510392.7093447965,
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'AЁёřčԚ³˝ϓϹǱѴȯaƛʯǝÞțŌ\x8eĄΦŏ4РӬѳɌ˽',
                'message': 'ϨϻȖҿŖ$ԊʳЪЗŲſʶ´ΒʝҘȽvԍ˛ѫrчёŬȠʪÛȼ',
                'arguments': [
                    {
                            'name': 'ǦӒΝýОϘˆµɿDʳӎ¡кɆ˅ʍʛґςϱҙ¿ȘЋŬƿőǅŊ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'çƃιӇӔĩԔȀķѪҔȾ͵Θõ\xadlΰʭŽ҈ʡ˾ɧɫɬӸĞ\x82õ',
                                                        'ӤǇҦ®ɼƕɷӐÕνӫϔƧwäʟЁ˜ƯȊuϷĲќΈȢƗҐԊã',
                                                        'ԙҦơɔԆÊdϛÀԞ×LìŁùƍϨЁąƤȽĚɥɛʅĂγ˪^Ʉ',
                                                        'â·ͶȊ\x93ы\x9e/ÈҔԬѯѱ\x80Ȑˉҳ˕ǽƗӬȅβӣǶΎƀԪӮń',
                                                        'ѠҐˢɪΞ©ǚιíÈƻƜˉÃϮɔȪѻÙ\x83¹\x91BhӷҎǹȳȶӻ',
                                                        '˔ӬŅ\u03a2ά¹˹òγЇĸďϻġȊö\u0383Ԛǅ4ǌ\u0378ȐłӷиˉсѰʨ',
                                                        'ĦѪrк;ʌŮԟ§1ӖļʽíӻΚ@ŎɝěƁ\x96а˻ɢȑɉЪɲȺ',
                                                        '¤ӠƐεӚħȐҩΈ@Ȥτ ͷÍѽΕЫϱǫ\x90ʋƫˠЋǜӫʆϘǯ',
                                                        'ΛɺӥӣψƽĖӿԛĝƭŏʡϦŷΫńƇʊɅҹ҅œp³dʥ҅ǾҲ',
                                                        '˰ӦУǸʴҔΔҽūȿϨΜЁ˩ЇˌǹɅПǹÂoҍЕȂΜӊȄ\x89Ƅ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Äˊįōĳϫʇˈ%ѵƑ½ŇÓÇɽ1Ѥ1ҲëѼѓΆşőτˣǎԓ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        9362.172371883076,
                                                        500473.28332599974,
                                                        566253.8278995838,
                                                        125694.10036584368,
                                                        202247.46838936378,
                                                        361135.09671785805,
                                                        233105.53232984687,
                                                        150243.99391288272,
                                                        346368.4336282648,
                                                        489957.09961403767,
                                                    ],
                                    },
                        },
                    {
                            'name': '\x94BāǄь˙ƿȎΪυȓ͵ѳŀ˯͵ԄΫжȗ҆ațƺ\x9eʵв',
                            'value': {
                                        '^': 'string',
                                        '$': 'ϼɝ˔\x91уΚӰɉ0ЗΧԃηһϛŇϼДÅȘÉɊÈҍМǗԠõçΝ',
                                    },
                        },
                    {
                            'name': 'þĺԕѡüņ˟ưƦԐȺɣŗȰҷØϧ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ȗБ`ĜŞ\x9aͷʛƙśɤƥğʖɸ+¸ӅS»ȺƷÃвÅЋɜĂиѩ',
                                    },
                        },
                    {
                            'name': 'ƇӖдʢƴÕ¡ң¯ǵʌЍĨЕüУʲ5Ԟȥ\x8fɦЕʞҾŜˀˎʸӂ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ϪϬұˏˌЦ}Ӱǀѯ¥ҀɸЧư_˺ȕѴЙƥΧҨľˡÊɐҸŹĺ',
                                                        '\xa0SĞƶɚ˵ʷɊƖƲÝԡǲŰđһӡӰ˰СЕħӈ¤ϡ\x83ˣ)ϣӄ',
                                                        'ˠǔcČѿԖ\u0381˰ºŲϩϊӽŭоԐԑϭѼĸÄɑQčˁǀ˭ϑϷȶ',
                                                        '˚ʏΑśVϋοкҝĕ˜GТɮ4ΘξºzбÙƽĺŝŢԣР˖˷Ò',
                                                        'ѻɤЛιєˌΌʾҙȽ,Ɛ˟¹ȴħΣԄɖƭ\x8dưǙưíуu?ɊЁ',
                                                        'ʵΓĥҋʰӜAѫԦw\x99Ɩ\x97śȆʭǛӾ\u03a2ʖī˙¨Ӛ΅ɷZɸϰĂ',
                                                        'ȣ×ƄP˧tƋԭӷ˷\x87β҉ќ˧ĲԊӴƂӚпȺɜиſʯȸϮÉ\x7f',
                                                        'ҹǵԂɖưʵҒй\x89ӦùԑŲөӘóƓѷ҈ӝĈȚ͵ěӮϹÎΨԞѺ',
                                                        'ȞɍЛˊƴ\u0382ǆΡäӟʝ\x95ùʕůюьěȿȲ\x82ʇńϤӚҖǮˢͲɝ',
                                                        'ҀѳLӃÆʹтȱ\u0379χʤһIѰˡģǊƑɈϝªìȻymԪºΨАϔ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǹȖĚϋȜ',
                            'value': {
                                        '^': 'int',
                                        '$': -3244827891725518979,
                                    },
                        },
                    {
                            'name': 'ϑЋ*һʗơƭſɩ6ҿЌWԟѓɁͳƨdϔѮȗԀͼʦŚˋ&ѵо',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'АψҪǇϤ\x89ӲжЧİƍŦǒćɌ\x92ʀʇ˨űƫѸŔŒϟ\x83ĴӖŦƒ',
                                                        'ɾȧǮʥӺƌ҈ћӄϓƲʑĽ\x80ϰҏΖëʪʨ§ԘԁќƠͱѰϠàӣ',
                                                        '҉Ƣ\u0381ҰpſѼѽџѤǈқкϝŠn!ĲϦX1ƑӤλӬYǘҡʹϟ',
                                                        'œƼ\x82ǝɩѫōȥӱφ˲#ҋʘŌϐԏƭʤԕϜşЏкϑąѺżѳш',
                                                        'ːԑюV`āØЎҳHǑεĔԘќÀЍ/ćX\x82оѢʝœƍӫϺѥς',
                                                        "Ȃŭґ˾ӡ\x8a˲ȽşīӮЭЌѺӀ'тÀԀʇԢƳɃѲК϶õɽлË",
                                                        'ѓɀӼ˾Ԭлϊ˶ҞԬ˪\x85MċЂŁԅVӘĶkǀѾȒҀ³ǖʿʮϟ',
                                                        'ǽђϹ[Uҿԉҩө^ȥǮǾӌ ȷϼWZāЄǮñɄéЋϨFάχ',
                                                        'ŻăŒǇΡjǐɕǓдЛӈЇ˩ʨ\xa0ƋЛљųƫӏöɊďìҋӋǹϩ',
                                                        'ĸ¸ȕ\x94θ˥ωðFѴǌĦўȹȊ҅ӵ·őӱ\x94\x914ɾBɃѳԤӊǿ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʑʱāЙ˭Ɠɔɪćƌǥӗˢτ\x9d˴чǌӢêіńđˬǶ\x94ġΰȲѽ',
                            'value': {
                                        '^': 'int',
                                        '$': 5275560668321169972,
                                    },
                        },
                    {
                            'name': '˴LԃƖʯΓ%ӡʫŅƙǾѷ>ǽƮЇ\x82ʧϯͱʪ˺YǵϱΘӠʾ-',
                            'value': {
                                        '^': 'int',
                                        '$': -8351812039700503244,
                                    },
                        },
                    {
                            'name': 'ӡЩ»ɤц˺˼вҨ˶ī\u0382OԂǦʋįЯǱ¦ù½ǶГ8ȇмŸҡD',
                            'value': {
                                        '^': 'string',
                                        '$': '˓ȷDԒ6Ӹќ=ё˯ĉΖĠҸǛ9дǛϥǍλÐÙǞяlΘŃӥʋ',
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': '˫ˍ·ҮŻ',

            'categories': [
                'internal',
            ],

            'error_message': {
                'catalog': 'ҞȤ',
                'message': 'ο',
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
            'name': 'цʸȂȂËǏҪͱԂ\x97ŦиΟɸɰђѺаƧę˸ѵЈѻțøƺɖwԪ',
            'error': {
                'identifier': 'rĄӲțӧȀʨj˜нӤэƇҒӴȈ*˓˲\u0383ʞϼŲӂʬʉěҧpү',
                'categories': [
                    'internal',
                    'network',
                    'access-restriction',
                    'configuration',
                    'configuration',
                    'access-restriction',
                    'access-restriction',
                    'os',
                    'file',
                    'invalid-user-action',
                ],
                'source': 'Ӳżр¯Ҷϯ¡ßʩŞĞȬԠǋɕɄâňWќϖɈ\x87˥ҡʌ˟ԐΥV',
                'corrective_action': {
                    'catalog': 'žʪҀϤӶƤżϞ\x85ɞÛ2ƙѯůǪȌԝ˭МόЪэϥƭʎŢŲ\x88Ϻ',
                    'message': 'ƨʟҊÃʕΫϙѹʖ¸˜Ӑ\x89Њ¦ǷªǋǽHĝʁȵŃһԃȱѹǬ\x9b',
                    'arguments': [
                            {
                                        'name': 'ÏÑегӌ¢ҡöԛ҈ňѐҮɴΠǤΓúƄȐƆҜˍЭ˯϶όϢΓ˦',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                    },
                            {
                                        'name': 'Ž¥жӪ\u038dͽ\x9fԩʚǆzϲţȧŐ2ϱѕԟЍК',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220916.772622:+0000',
                                                                            '20210206:220916.772661:+0000',
                                                                            '20210206:220916.772669:+0000',
                                                                            '20210206:220916.772674:+0000',
                                                                            '20210206:220916.772679:+0000',
                                                                            '20210206:220916.772684:+0000',
                                                                            '20210206:220916.772689:+0000',
                                                                            '20210206:220916.772696:+0000',
                                                                            '20210206:220916.772705:+0000',
                                                                            '20210206:220916.772714:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˈєѯ\u038bǡ\x94Ӷǻǣό#҆ě҇ΖӂÑҫҗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ƾӁ_ҷԍҧɑtӝτ'ͲŰǒά±ÓΘԠΓɀѥɰċȪŘӿЁʓÇ",
                                                                            'ƠӬκœ˼ŋJѢ\u038dѧ×҂\x8fĝԆѱĊжͰ[\x96ʫ.ԪƿêɬήVĶ',
                                                                            'qɁʆȒÎ҇\x9dâ˫ǔǋ˒ɐ\u03a2ţʒˑΕìӒþLƟѴŏЭBɫȹѯ',
                                                                            'κʍY\x81ЅBĳԬʷƽԇц˖ϛȊȣȀ;˴ҺуFиюÌÉ҉Н˧ě',
                                                                            'ԝĢӾ˵ŞʖƜšďȹϨǇ5Bγĉȫ\x8aΟɒ¥ӠʈʞѡѕэizԀ',
                                                                            'ч\x9fAÌqѴӾµŰÖ͵Ү¼ӤÒBψÂfЄūƃΌɠƇƠüǄɮǉ',
                                                                            'ǠǻԦҰZԣƕϽʀβıȉʞ@ɆʍɶϠ+ɮȻҶνɖ˸Ĝȷϱʰɦ',
                                                                            'ΡÕǄƮŘмśȈÛͲDņʹĸǼƕu.ɟѢƽʓ\xad˂¶ɏˋƵöʴ',
                                                                            'ϷƉ˘eɤ˅±ǪΓИΫǗƹς˼ӚˈҾΦüWДɅȠuα҆њˋÀ',
                                                                            'ˍ˙\u0381˩ΰküŽǜЩԢѲӖŮʄ1ϯνȳõҖǵƎʑĮȮӉ˲λФ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҹʅД\xadɌAūʐҗóΌƺͳиŸƯч',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʰƮωƣз ЍʖΡм\x96¼Œ»*ˡȡϪɔǤϕÜǛ;ƚЋϑζ¦ț',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            287644.0283425895,
                                                                            412033.2019218848,
                                                                            234823.81216184137,
                                                                            909412.6683018098,
                                                                            710196.3524513248,
                                                                            979401.7812466063,
                                                                            334165.8995391388,
                                                                            871514.9130323828,
                                                                            311238.36721013876,
                                                                            147255.2749378116,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˂њ*ÄɎҍ;ɛəœε\x84ŝƠͺυƊҧˠІ\x9dȢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8449797733259506852,
                                                                            -3662991019863879669,
                                                                            7020590590530842278,
                                                                            -6743810696146722452,
                                                                            7728858994602019068,
                                                                            -165563865919792287,
                                                                            5218064522996153976,
                                                                            -5879645435840508273,
                                                                            -7068417316534747590,
                                                                            3304441935556762751,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Җ˭ȭɦŽơȎӇTԜєĄɻЬҦˡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220916.775775:+0000',
                                                    },
                                    },
                            {
                                        'name': '˦ҽЇϤѪǂɺūʉȁӔѵгѰɧ\x80ʜɃ\\Έæl',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\u038bBȁҲǝöЈѠʾìbȲǈɪϵƟʄˇFλˡβ÷\x90ΠԈΤψÎϷ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'æӎƍѕǐӫͿģŉ҃ǖəќҖƜƷΤMιӭӧѩǊʳƆTɡԙÊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4965782946048553995,
                                                                            -5115389728761011366,
                                                                            -7851267780180782210,
                                                                            3886138846907426214,
                                                                            4695261149920668028,
                                                                            1672512669803248476,
                                                                            6259737577877535782,
                                                                            -2253667593024105222,
                                                                            -8352357228204737321,
                                                                            -5899542591407367201,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ÄԄŞӕƔяˈĠԇѨɘҌ23ȟĭϒзȆɕɝОЫʯ´ƺęšδǌ',
                    'message': 'ʎ˅ũԧŤƶǾЯƪȽΪƃţƎаџҖдѻЅΩƒ\x7fÝԅ`΅Ҙӓ+',
                    'arguments': [
                            {
                                        'name': 'ҫȴʂӕƄΤͶҘhȴÙˠ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8286829244822216393,
                                                                            -6434411051453628649,
                                                                            6461770971503446694,
                                                                            -8182774906791990582,
                                                                            -3944604335257199484,
                                                                            -7415434645192436061,
                                                                            7913478545697339977,
                                                                            8938918448994811467,
                                                                            4711445834753974792,
                                                                            -7359727106492448119,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˢӥȚΤǠԊцҡ\u0381Όҋ)ӮϳɹƑєѿѮɏЌƯϨͽņˑć',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŷнӿҚҢԖ£СϮԢҩέǰӔАϑаĀ˵/ˌŕϲΰΒŲҙȌͺ҄',
                                                                            'tƘÙτäϷҳJИя\x8eīȯϳΈǈш&ʵͽӧĲϫѼǾǓĤͼ҅Ʀ',
                                                                            'ѹϥƬʧϓҢPϤċԡżαrɋʖȋԓǤȹɬρӻ˜Άȓϱ҆ìƕ+',
                                                                            '˚Ҹ·uȭŰϥˀǼ˺ЋƯťǙĬ˭ѴƄԂһϚɮɽjǹ˒čȌ¸ӈ',
                                                                            "³ǜè'ўŒΗōˢҀ/ŐŧАҙϸҝ˾ɔĉԟǇХCɌӱɽԪťЮ",
                                                                            'ϛȘϜ\x94ІȵƻǈM«өгљԁͶZǅʲîʛˮƛӕʈĪ2ѪӴʶӪ',
                                                                            'ƺ˻ʠɭжú˂˜ĺŷ\x82ʑʧҺʼčжʍԭǕƽӣũϫϷŮǌBŨΈ',
                                                                            '\x83Ѹ\x91UȮƟ°ŊʫҴęxϚʓӕϭɒȅӭ^Ԗȏɝоłó˔ШȆѳ',
                                                                            '2ϋŲːƅѠȥFӵƮԛśčӬʻϴόLĭӰɁΚîǔ΅ɂњōßǚ',
                                                                            'ʈɬĿêőŤӿԋƚyċӰǥýƾϾ\x8dȯѓȷùǷОɧĊ\x95ѧƏϦô',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÍԥġȿƚҼζˉ҆жʰҕŢśǡɝë',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220916.779727:+0000',
                                                    },
                                    },
                            {
                                        'name': 'șҲΟЫϟӓʨŖʉŸ˻ŠʦǼ~$ρʍҌƾӚ\x88ŕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȒɜԊҦЌ˫ʢǰ\x83ί\u0378xԮѻΜŭԭЪϮÃ%ΙҬ˦ģ˝˨ԇұȿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 224125.2759232421,
                                                    },
                                    },
                            {
                                        'name': 'ӁїȌЀΰρʇǳԈҩΤϚǐЀ¨ǲӚϘƞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -129021801594396836,
                                                    },
                                    },
                            {
                                        'name': 'ɷЋƼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǆҋ\u0378ЇƯʧзĀIĂČІ͵qʹſʹȘԀԋΤŢ4ѕ˛Ѳ˾ъΒш',
                                                    },
                                    },
                            {
                                        'name': 'ˍпěƠƆ«ȌWǱúʋ·ȚşШϧźҙϕȷˑÖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 2380.3375969641493,
                                                    },
                                    },
                            {
                                        'name': 'ˌƍäϮЩ{ɿÊdˏʊJЛľΌţ!ӻӄРϜǸʅӸһґΘɫқɃ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΛɀûҶԘȭïӶʧҒϘŷˤŵƱϴ¯ʝ϶ŒҙƫΊȹȝIЗӿȟЧ',
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

            'name': 'Ήɕӳ',

            'error': {
                'identifier': 'ϡ\x93ӑЋҧ',
                'categories': [
                    'file',
                ],
                'error_message': {
                    'catalog': 'ɝĺ',
                    'message': '¼',
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
            'event_id': 'ŽĖӯ±ØЄȻɷЁ\x84ϨԬIǇÆХʀʞȃњӰ¦Í gΝ\x99ŕɗʈ',
            'target_id': 'ǣΊӐ˟ƥĝƪƹхЃƖĨҙǕ˖ˠѝѤņπŅѫƶ\u0381BԃɘĈћҰ',
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
                    'event_id': 'ǳŘ¹ːÛȟƭNɘҽ>ԋˉɋϠǐđͰΟĳыӄǌͶԮόʶԁғҭ',
                    'target_id': '\x8dưǻŏϞκρˬǖʕgѳ˯ȳҗоbĩűžZnʴˬRĜgǐǐĻ',
                },
                {
                    'event_id': 'αdЄŘҰˤȫgôȋƏз|ĿЎΤҞʟΗŐӴʨʸǌ҉ƵʯÓӴӢ',
                    'target_id': 'ЂѢȕчŅпӜͰȶǩβвˮӖԩԑvƇ҄ͿȒżԐɖ\x8fԆфʽɷȗ',
                },
                {
                    'event_id': 'ǝӣÑáˏϦɱеɊĞ҉Ӆ\x96˶ĵ{ɄϪоđҺТӦ˶ƤīώϻƐΟ',
                    'target_id': 'ҢɝңЪԆŧƬĚȩȦȁФöʙɤуȢϦɃüɘƄͷЕϛȼeҷίɼ',
                },
                {
                    'event_id': 'LΊȨ˼ȌEǡŖʈĈЧˈə\xa0˯Ƙ\x9c\x92LƯҴηӔʔŪȿɊŮĀЖ',
                    'target_id': 'ʹÊҠʨȾƶӔҚзςɲ´ɥʤƙӛв,²şĚǡѐѵʋX\x8bÊbÒ',
                },
                {
                    'event_id': 'ĘǴɒθȲԧʢȣƵ8ƥ҂қËƑԈɓЍ˖ɳńďRμȪťÐçÝ\u038b',
                    'target_id': 'ҚԀϟӌǑ҂ΝɺϦ',
                },
                {
                    'event_id': 'ʖǃĕξȕÄҀѝɚӧʁŰˢы˰˅ǧԗƯПοħқѱǎ˥ȃΩѻѮ',
                    'target_id': 'ΉȕƟҋƑʻ¨Ʊʆʎɥӂ®ΊǯЦЉҟÞϒџǳ%ʉǫґˉӒˈѥ',
                },
                {
                    'event_id': 'ÙƳҗÒɑЁÓŶëНƅTΣҔïϕƅ\x90Dл',
                    'target_id': 'ĢǷƴ˕қl\x87ѴżOҚƛ||ћǞТ@ŧԠёǁѩɖЛ\x80ƇĸҖӸ',
                },
                {
                    'event_id': 'Ү˶6ƈȌĻ±ɗԀŶř˫ęĺȀ˦ƚFԊưԉϹZЯςɉðƔèê',
                    'target_id': 'ǥÌӐțӶ˽иļʱȸӸǦCƐԍΓϔʯТʳҨĮӂӲʫǷǺƷΊѹ',
                },
                {
                    'event_id': 'x(íƽŸǚbԡɕҀ9ғͱԒІѻ˯Ӽ\x81ԔȅӶªdƾыδŃͿC',
                    'target_id': 'ɋ¨ԓU͵Ά;ǲȏëȲԛǒŀțЌ˙Ɯǂˌ˽hʣóωg˂Оȗɔ',
                },
                {
                    'event_id': 'čˑaЫρȞÐΒԅˤϾŉϚӍſюѺ\u038dȋԑʢpɨǷѳϬƗчԢύ',
                    'target_id': 'kʳʚŶˡϿÃĝJÿɢӥϟ˒žπƬѧćØ>шξñ˂Þˋą¶Ӌ',
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
                    'event_id': 'ɨʩɜ\x8cŅԑʏƷ\u038dѳƯӛɠΊɫұʡľʤӋϟˈԈȔɞ ƚҡŦ?',
                    'target_id': 'Πńˋ\u0381ҰèʾȂĭˊӻȞӫȕŠ;ƋğħʂѠ\u0382ԙʊì¦ŮǙΓȫ',
                },
                {
                    'event_id': 'ʅǄĮѾǌ\x89å҂ŕˈȂ˰ŅԥԚȧΥӫęƳÍҍϢȇјªψ¢ƌӮ',
                    'target_id': '͵ԝʨЇӺʘÆʨĿ\x87ӟųѢΆƜȠѪҠԘϊЃĂʅGӝƋʞʜìV',
                },
                {
                    'event_id': 'òʷ\x88ӿƂƛȘÓ¿ǸʗͲѥ҉ҧϼ\u0381˽чМôϣø8˚Ԛϔԝϙs',
                    'target_id': 'ʤѐ˃ʑƖÙХĀϏÇʆˡΤΒϧĻ\x9c\u0382ĐѷѡŜ§řοƅƲȚДʨ',
                },
                {
                    'event_id': 'ɽńӻˮɞÜΓɂʹ҆HȖԓΤßʵԄ©эͻÍҩÞѻ\x99/ɛS\x87Ι',
                    'target_id': '´п¡¿Ĕȑ÷;ӅƍǑÎʛȿПыʏĸґĄΥȳȨŵђĶŹÌȯĚ',
                },
                {
                    'event_id': 'íѱʕϦŗEВͱǳьҘΰ˯ƖИʁʅȎ®ɑϖˬΌζēӢ±ˇʢɱ',
                    'target_id': 'ƺйŜҳƓȥҟė',
                },
                {
                    'event_id': 'ѻϋ{ȠԢХĪËÛɚÀӤśʂΈ»ƝƟ_ϵίЇ;ɳ#Ƥӊɉˉԏ',
                    'target_id': 'ĝƈʻǐôʏȇǒ`ƓȪƨԦƘӍѴӜуӎƩÌϗӫ\x87ĒʷχźǗ\x86',
                },
                {
                    'event_id': 'bӰ®ЖûФαƄĩWɂʠϩ˲ΣŘϚçюοԡϙҀȊÐ!·ӹȈĂ',
                    'target_id': '\x98˟ӝlҟ¿ʳӟ|ӼȊѮӉ%ɇfɇϻҹńˠжňɲțӌŖƗĮƾ',
                },
                {
                    'event_id': 'ÙʀȉӴԨö\x81δҲυsД|Ӯĳʭńb\x9dѧɯԄɂŻv\x98Ԡ˲Ǟư',
                    'target_id': 'Ϧʴ˴ȂêѷîƓʁЄʨʹД˫Ǽǹԧǒϧ˥ŌЕϙɜȵŮɒqĹζ',
                },
                {
                    'event_id': 'Ԛ:ƠӼκԐÏѹЋЄʆюιЊÑƿʄʗ>ϲҞъȁğм҆ǹѻԕԊ',
                    'target_id': 'ΪĂIϔį{Ϯ\x9e+ӽ˖ʪɆϘαмϟǐӽҞʨͻƝѭҍĀŒōԌȒ',
                },
                {
                    'event_id': 'ԫǫÛʇǌЩЛЕǔʦӗŹˉQ˟ǌϦӟƱΔѥҺъŔӅǃӵͽƅΊ',
                    'target_id': 'ɺжŒȣÑǒϨȇԠ\x96Ǝ΄ԤӲĮȞ½ƁĮȣԞɧȗӼύԢˌ˖ʆҝ',
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
