# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-11T17:55:36.525619+00:00

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
                'ǡɺ§£®ÍˤʷʚϤȤԉŉПԧ~ǥϞаҨԎΣ:Я˝ϪԭĂǋѨ',
                '\x80ïūДŉ҄ϥΖǌ҆ʈGϼȓɎТĤơǃ{νʿʚ\x7fƤΝőĻϪͳ',
                'rεҹɬǜԢɋҟʈІɽƆһӻ˥ˋRıӡКԄψɗ˕ǆ΅҄ρӂc',
                'ØŃάBǇǺДϪѿĩʪ\x84ȵOĕѥʐͱ϶ʴÐďϐͻŢѶЈʑΜĩ',
                'œʼĭƔȫɷЙ˪ȏ˗ǏԚӃєσѿȏСŜԋ˨ҏϿӦԌӦˆҖÙԟ',
                'ЎȂɛ΅ԆΚȟʪ6ęҮœĆѲҴǂÐѮ˶ēԓɔѓŖȻǑϥэƎԒ',
                '×ήѷ¡Ϙɩ˪ԣԂ¸IѐƀҴȱѰȟƲҫǏα¨Ǘ2ǳƞԬŎϸӒ',
                'ȍˢƢ)ЛÓϷт˜ƨĳŀƍÂƤðрϩʌȶľĠαѴҩɯǼŸʩŃ',
                'ïлƼящǌϭťÒǄȠЕҒÍ˱ˆфȣƛȏѧżŠʁԗcжķзѡ',
                'ӴƴԜƳĚ\x89ÏʊȻģʋ\x96Ŋù?Ԣĝӗ|ӺŘOIӪϵӆƫŃ҉у',
            ],
            'source_id_prefixes': [
                'ɰȴí<ǠΧǀƏы·ӕʌμÆĂǨϘјСϾǷȆҺÙƭɬȥƊmȂ',
                'еԣԭˋЀĂЦԝÿ\x91<ˊʌ˝ӾԙϲŉҳȘƨžͼʮǈҒŷ˱ɛԢ',
                'НρӪǒʂțǜΝϘɽȾʢӓ˟Ƒʚӿ˘ˮŏӋѿÚNϵӏͺnŋШ',
                'Дѭ\x87tȻρʢԥɗčҾɥҹƐƍϩǒȯͳЮД\x97ĝĨư0ҝɏІɗ',
                'ƉQʰ˘ҕϛхŕѽѥҘ\x85 āӰΣȊԦƸǻеéЋ±ī˥ίɳ',
                'ǹɹғϤȒϢIʊAōǀΈ¨Ƭʸ\u0380ҖϘ-ЛƎńѯŏ˚ʲȞʩʩ\x87',
                'ŌÎɑƙΗŉHзɫȈǴϳϻΦǪДЯԊЛϓͶíϋ˟Ǒů\x8aɮǊΏ',
                'ωĩӨ+ѮʍԦԏæѵ\x87ʠ\u0382ąЃƌǟíǢƇЁ\u038b<ʀ\x97ϳпПǺǟ',
                'Ϧ˳Ë˵ļĞҗŠȇˁԑϯȧȩĞԓƳùαΏӷѦΩĲƒȥϝʆϺ9',
                'ӺȜΕԆ҃{ΎˢӁȶϠҾɕƁωѧȺƊǧǉʘԄƾɍγϢԗƳЇЀ',
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
            'action': '©ˌÂ\x82ǫӄοʲЭDɥу`ŻƎʭ˅Ȉɯɫƺ\x9cʺ҈ϋɓɗ;шԜ',
            'resources': [
                'ʲѐƲӬƙԛ\u038bӫƙrōŻÆ\u0381ȫȐɒԘӋƲεԪҎʟԁԢƴΪмȊ',
                'æЀÖҢЊFʬĳϰγӖͶύͿǢѱ˞ŎʚĊȁ=ƑǣОШȍ\x9džӷ',
                'Ѫš.ǩĐʋ˪q\x80ZĻşǜґˏŎζΏӞʝƋɾǩƍ\x94êĵжˆ;',
                'мϑ҆ԏʲȯѯϩɀЕѸ˘Ŵ˓ńϲɭ{àъ\x92ʺŃӭЃǸҎ;\x83ɜ',
                '\u03a2ǈжӹ\x9cѾ˝ӺѾȱЫƶƉl˖fԐĘǺů?ËȥUƠûϪ҂ȳϋ',
                'MƒϱύâŜŌɓɥɂэɞʒаҀəԙԮƧǘѪѶʅ4kқǫΩЄ˽',
                '£đӘ\x9fÎΒөʤъhнЗҕѐϴΈÅϪˈӂςЅˮ(ӯ¦ӫíҔp',
                'ν½чҌҎʀƪʯƾŋʽ\x93ʮԝyкʓȥŤϷ;Ќ·ʋԖЍűбǫԕ',
                'ӲeΜȮňÚԤвƒû\x8c»ѲğļΥɶв\x84ǣƅäƎˀƧϴÿ\x9dŗƆ',
                'ɟщѕҟщɛÿȰɔĖŨĒЪѯǧϼӭŠɁΈɘʴɑ\x84Vjî҈ȓЄ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ϝ',

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
            'name': "ƫźȗȩɆ:ӓǺƑvS˾rίɿ²ƭԘȹ˯ƩɒīSТƫŇȯâ'",
            'version': [
                -6735187839743884122,
                -4062285833635516617,
                -2896106668082210714,
            ],
            'location': [
                '˜ĢҚȅũїƻćǛμk҅\u0383ЙϱԑΆʅѧӝ҂ƋľĪɸʵÏЇ˒˪',
                'ŷϲϩӟʛЄ\u03a2Ϻӄ\x9dƼϬūӺ˥ʉӘƚЩʸV5ԏɂ÷ç϶vęĞ',
                'Ϝ¼ɟρҤƗΈʐγɶȾӝ\x9bԖƚϿƾʃºɖǱԥ¯ņ¡ѭΫ¹ΜƖ',
                'ɐŃɹ˕ӖӭѺǵЉˬsȷ9|ЬѼЇϿĴнѶ˟ѺԮǟ]ɚĎԥĈ',
                'ӟ ĥŦ&ÐҊƽúиɀƏЗњ˩ӖÚЭˀʮΧňwĉхҪ·ŭƖę',
                'ėå\u0379æÞʉƱΏ¬¼ǾʹȬ҉įӿȣÅ{\u0383ԑэӤқʪŢӯÕѤѣ',
                'ĜĐǈĥъӺĸ˫΅љ$;˔ϪˍҗNТĂϻɣƺϻɊƑŽϨ{Ѷ\x86',
                'ž«ƶԂƗȺʠѫǫпǑ~¼ѬƵ\x9aљ¡ѪĘΖӨӱħѡрŜĀɳ˂',
                'ɈȋѻХȎ҆ˡΈӽҴųԖԚԞÞđǂíƬhφʵƪÓҖ\u0382пǯÆʃ',
                'VʎюʔԤĕƵ,ѹϟ\u0382ɧϐяҺǲҽϼɭPlї\x9fаƣԈɫȌҴӊ',
            ],
            'runtime': '\x97ʨϼԐɘҊϑȍѻŢЭŃȡΛĺ',
            'send_access': {
                'event_ids': [
                    'ΕпҿȘĊ\x83ɡԞԚǿŔԫKìŏȤ\x9dδϴΣǳǗÅ˝ѱǮƲФԊԩ',
                    'ˬΙĂЯƪψӥ~ɨȬΜӉԂðǐ˾ʫː`ǾÒʄÇэɘʼȦʫЛ˩',
                    'ˊĵķą˫đǩѦŜƹӝћſӪ\x7fɨψÇʆσl˗ƗΏ҄Ƨ\u0380¹һ¦',
                    '¥ш4\x83ҵЪҧǸƧ˾ʖάҥȀMĀΞίˏԇԊēŜҲӨǁ*Џǻ\x94',
                    'ƿĀČ\x8fȞBώԀӻĥȧǲɋςƹѪƎ\x9eɯȶϱ«ę\x8aȑȿȝʁь҅',
                    'ûԣο,āϒƣӔEʓҺЙʚʣ`іƉѽԭˤӾ¯ŒԅϣϡǢλԐȹ',
                    'ƳɺІǄυʾӂ˒\x8aɖEьɦе͵ĠȆʠϢӳѧïîӅК˼ƊȧǭϦ',
                    'ЇԛǑˢϥ\\ėùɕҾÚҧɔѠOҍѤƗӮȀ\u0383яѤǋƅǛʸzƆɤ',
                    'ΔӳŉСҥÆʮ˰φƭҝǹʷɞĉҚԪº-ѱŎǪʂŕϧԈԃœҌҀ',
                    'ӛқѓҥӒѺԃ¢ѦȎ¹ƍũğΛȽƂχ˜ѺɅԋÔ\x8dͱϐšЮϤѠ',
                ],
                'source_id_prefixes': [
                    'ԩѵĪȺǧʥ҉Ю˭нƅǧĞѫʍѢĕʑjйʄHʊϴɮĐėȟŤƥ',
                    'ҔɅνìүHDЩГƈ%˧ɆξŐ¥ԙϟĜȿȣѐÉČӹ\\ӽӽӕҫ',
                    'ӔқǯʜұzŷD\x99×ϬčʩßʉËЏVƂʴИƺ˭É˹\x90ưίȆĸ',
                    'ʡӜӐчœĞ\x96lćëĉ\x92ȢӑǑүƏɲŻƻɐǶ˾\x98іΰԫҋɠѓ',
                    'ЂÞԧћĖǷƸңЛҝѼȮŌŕɔϧØϭʫúƑȟӆľӗˮ˱ɸǜǼ',
                    'ӷÔçƆZˏ˂tГϝӿxŐɷ!Ȁԗ¿ɢ&ʏàӕɭŸїķͳϐŬ',
                    'ĩÿԛЯǫǁԉ=ɾðɮΪМɗтöō˚ʟϏ\x89ӠҸ˻˲Јƻ˒ʹŐ',
                    'ԐɼҢџȏԎϙƿ˯˳˝1ƮӾ˺ѐҹï05ӒȢǝ±¥\xadȲɼƬ(',
                    'ɢЅ·ҽԎгҝǖЗѨsԨŗŉȚ\x7f¢Ǒŗȕ\x9aɶšϗƕɭѤ6ȳ\x9d',
                    'ĔԒŀɆĤӹǍ˭²ʗɕȪķñǅʩщΘʚƙԐϗ͵Ѻũ˫˚ƔϑȔ',
                ],
            },
            'configuration': 'ơμзԠɷҔЕªӴҏƃіϟPȝәŮOȡƗlм҆ʌΗԗ\x80ɥNɳ',
            'permissions': [
                {
                    'action': 'Ӹ˻ŌԆЪӱό\x7fɃӨƺȌҢӛ˺ÊőрҹϬɌíʫÒƲÚÊΐ\u0381Í',
                    'resources': [
                            'õѠȢӔΗΙεŝɐƋτ\x85\x9acͺӸӋЏˤćӷύĢƉҗƃϧˌͺɎ',
                            'ɮÏӄӘɦ3ăɚƶƁďӬϦȾïˁϠȁƫԮɏɜӆКҦʝǦƋ-ӷ',
                            'ŮĴũҫ˺җѦσϐϡκƄǁѴźϘȟcʐұŤҙǥċĀ¢ϺǜԊr',
                            'úҌ\x8fȭǕӹĭ˸ӂÂˤɤˇƣ',
                            'ŏǅȞѤƺψВϴȎ_ķê%ǭɋũъҔǣȳ\x95óƔψѯʮЋϛ©ĺ',
                            'ȊƘŮҨƕțѥ<ίҕńɤқҶɓŽɶǕpȬȘЦ¤˅&öԐɪŞſ',
                            'ӂzнɕёʎʰƷϦǤȢϟ ɚΏȡĐȕjZļҌѴNŘɍũζҏÛ',
                            '˭ȭȳЅŤĳʪǡ)ǜ\x8c®ɶʾ¬ϗÐӋЀкĒĵώËœΕ\x87ԭЃΑ',
                            'ï²AņįӍȡӬė˄¬ƴǍuΒÝӳǧ˾ɞɸÊƤc¤ǹϢҪӠƍ',
                            'ҼЦӊʙɓŬ҂ǗǍӱǶҽԤʬñΥѽЊђϺҙϵΫԗȗκ',
                        ],
                },
                {
                    'action': "ȇ˧КЬѻӼ;ΏŃΪůϮʅϸĐ'ѣĺαʂԁϧдԒñ;ƺ˘ˡĄ",
                    'resources': [
                            'ɐőÚg!ҪӌǄӤɚӉ¡у\u0380\u0380΅ƕΞ˯ӇϱɔҴmԂȐșԮɉɴ',
                            'ǮʭӀə\x94ŐӘΜɌȩ\x93Ycϒ*Ѣѐ8\x85ХҎųƯǸãĭĹ¦|е',
                            'Ҝӊрcҁů\u0381ɟSƘȞdӚ:Ƿǩ˱ӯƎ)ʽτfżÜγŃǧӱш',
                            'ψƠӷɕ˂Tɶəк΅ЮƉʞԢɃʥԥIөВÐˢԔğϹȍ¼ņλэ',
                            'ǊͳЁдƁͺĭҼɖԅԬӁϐЧƇҼҧXĦӶŔρӫĕʘƏӃLĖŒ',
                            'ѲϾÀ˂϶Ͷ³¼ƽЕȨҔƏԧϏȥĈɇȺԜ˧ϓȦLЂlѶЛʢú',
                            'ΕϛԉǙ˞ƀƭЃǺ\u0378ǐzȞȖŅʅŹäΠϫʎ£ʡхä>ȖǫʯѺ',
                            'ȋг΅ʫŜѧԩċǇǌω҂FǿʥɄ\u03a2ѸfћòҭʦuʀǾŻƧíħ',
                            'ŒÖκȱɅͱÅYįӥИƝӘҳĹͷѤƏ=\x89ɑΏǒΊѐ5źȫƉĆ',
                            'ԎԑȬӼЄ˥\x93ťzβxŴ(ӕKщŨč\x9cƷũѢ\x8a\x84Žö\u03a2ŧNԙ',
                        ],
                },
                {
                    'action': 'чԃƢa©юϘÌƻĝϧąɼËԦЖҔͲōøoϩ¥ĻȾžǊŇϿƠ',
                    'resources': [
                            'Ԧƻe\x92ǑƥңˏсƗȃЋ«ǅźБèǣŷпƔœ;ƀȈdњҽŃæ',
                            'yȠɬǹŎіǜǙĴźf\xad\x7fˏĔƒ˞њŤĪΛÏЖԪ΄šİΤ»Ǽ',
                            "ŒϸżдΥӭќÒĸѻǔƧ'ϟɃàϾΗǳɬĻ¼ϟҞɛ°ι\x88ͽƛ",
                            'ԜGɕ˂ĜƀԌȳҹëϟȒĲœȄāȓќӢΟη˜(^ţӇϳт¿Ƭ',
                            'lĬǰǤƲ\u0380ǐɔԧҿν4ȣ_ǏʍǧѡkΉԇcӳͺŠӼϤʡ³Ϡ',
                            'Ѕҗ˖ːøǁԄȅψʨƑe)ƇБ˧ʦʋώɘ·Ϳ,\x8fʊΖʎǕŠɸ',
                            'ɿÊ\x92MҬ\x93ЖðЁӠɿ¾єʙ˷ΏĜ¥ԏԂǮ0ˇċf\x7f˂ãц;',
                            'Ƞ_ʘƉѢ\x92¯ȳɉҥǶʫѬͶhǄƾ҅Äʾ;ҷΤǷӺþJƿƳä',
                            '˃ǸǪҴĊɛԗI҆ѪŢ˳£ad҉ѣÊɊЊ\x9b\x97ń˭ǸȝÝψҍƮ',
                            'ґѣȏ;ШÇȴϋÄЬĉȚӯӥҹϓӪ÷ԔјǂÇƾҏƧԚ²\x7fЩ\x8b',
                        ],
                },
                {
                    'action': 'ͶǜȍΑξϽɜİÚӬƗЮΦжʖ$šLƮ\x8fҩ҄ɻǤùˁ\x97àǮΠ',
                    'resources': [
                            'ʃǮѓ҆ʘļȌѤ>ɒ:ˎұÉĬ!уƔ`Ǐƿ¯Ū˟Ё\\˶ƥŏɑ',
                            'ɺήЅˊĕŕĈģŨ.ɺţǗbʱƓvʊюȿɈ}ф˙Ƀż~ԫÎӎ',
                            'ˊÿºjԭšԂ˂uԐѨ˷ȆϖɑÇӅϽ\x8aѝȓӔϽΗÖҧɼԁƮ\x81',
                            'ϯѝ\x9a\x89ϻϸ ǇСĴȕƙăφƶҕǦTĹœǡ\x93\x96¤0φ¿ƀĥё',
                            'ϒӂϦöşҍȴɐƦ˪ĎӰ¼OзҽӄŴԅӸҬӪŗӷϖÍĵԮϹѭ',
                            'įѵЪәɝȉĩɽǙΘñ\x93ƇÛ¾ĬǔĉӾƇ¹ƣģ(ĤǔѩƮôɏ',
                            'M˓ŞУ˶ąɤƷΆΟÕGǺ˱ӍϐìɞζǲѯʕͶŋŅȿÝӟϸέ',
                            '˘˰ӿиӷЍМςėʔȖӥД|ƼŕϊЌ<ԆԬļϘʁ˟ҧřϹϾƸ',
                            'ĪҾµɝƛԥƻʟϗΤƗƙ³ϫȉǾО|ȅґҰƤʖĠǼ0ͷĒȖφ',
                            'ʟlťÚøĺ͵ұϬ=˩˗ТԠȲ˾\x7fŴ/πԏȆИˤɟѬЇϥҡѽ',
                        ],
                },
                {
                    'action': 'ʊŏώӂҼ7ќǡɞÙҾɡďʿĢЋ¯ѬΝͶ5ӒόҘ˲Ҁǻɽ3Ќ',
                    'resources': [
                            'ƞԋѾǽƨ˖¡ʽΠƕͳĶĽˉɂˊӮ҉τлģӨ»Ά´ƞˍ˩IЕ',
                            'Ġɒúԩĸɷ\x82ŵνϳ˱ĺhʪҞɭŭ7iɎĂƦǓ¦ҊҜųѓɨΚ',
                            'ґŘɊƌүʅ˽Ùm!!Ԓ˓Ӭ\x7f\x92+ɒѾʹĈεҝ\x9fОρÃb¡І',
                            'ûҹúɬϑǿˈЭgȼͺơ˯ɿĳԍúƦ¦Щ²ԊҐëˌ¹²łǵ\x83',
                            '\x9eƨ˼ΥǱɠҟO\x8dʞӱĹɍSˏÆʮȴMþŘÄʧѤɊʲүԂŲԨ',
                            'ɎдƶɢΜǏӝƝɡ\x9bʨШЁǲͺÀɷżӯƑӄĴ˯òӷӴǹш˂ȍ',
                            'Ʌ˚МŻ©ǶʳņXưǷɁȺ,kʐɜQЙφҎƖĞõνϔκϢ%Ě',
                            '°ϜƣīȕġƫɄ#ɶǒ»ӷЮĚƹǢǴ˖у',
                            '˳ȟ΄ëJĪԭȀӶ҇˴ШљĈàĝďdðˬ\x7fȃϛȳϕϝƐͻrĆ',
                            'Ɍς\x85șȖĖȩ˩m!ɇĹ\x83ԙʲă˲ϲӔɻϴқƤηǛϬfӀʟ²',
                        ],
                },
                {
                    'action': 'ȜÝ1ʇԩԑŤѲҟɤdӼƁԜHȻЕРή˖ə˂ɥǺԐА(ҽƞȕ',
                    'resources': [
                            'έӒ˂ƙɤӄɔϻăˏÔϰƚħГȿȰϕƎŖ·ҵïʡäҽ͵ƸϖϾ',
                            'ӀǍƞŅӝƣŊЯв˟ɞƴϽԩ˥җѶʋҮϰ\x86Эώӎɍʬȟ\x88ƮǷ',
                            'ǴŉүΏѶÖ3ԏӖАʾŏԉ҃ŗĐˎѠԚĕ\xa0њС\u038b¿ȱΒƴ\x99Ǿ',
                            'ԀɕӑȹɭʡÇҷρϘ¸ӈƮ!ԣҶҗʂƫџдƘ`\x91ЀʎʴǒΜϗ',
                            'jҏȓȈʧΧõμ\x8d˫\xadǯjȍȌ\x87Ʉȿ˻ӜǳƞƇӔȾΠɶɗʚϨ',
                            'әϼȊϩϧԄǨÖє\x87ʎʶŭʲԩҎ`ԉǂȷӁ˺θħʞЪωСԚш',
                            '%в^öҊɒcӰҶŒǷČǒ\x9eӸȜб˶ƮȏǿƕѕЃeÖĿ*Ђ¬',
                            'ūơΗԈɆĹѤĀýҬȑɼơ#TΝˬĤσĽ˸ɠ³\x99ҧAγμʡƞ',
                            'Ε\xa0ƛǷʒļ˰ϋϩԪĂƨͶŅ\x8cĘģÊĖǇˠAԑϔӦϏԃŇǌН',
                            'Υɪ&ΐoƀԎ»ˋ˸҈Ĕ§ǉһҘмщәӀϩФ˂˝˵ԋ˲ţМ*',
                        ],
                },
                {
                    'action': 'ͼљӯĨͼӅиáĊŕФӈʚʠĪǫҵƖғɘǯfͼ\x8bƈĩƞ˅˯Ǔ',
                    'resources': [
                            'үL;ŔςвɺDΜͷĒѬѕƭđǓДǘƠήјЭʐɇƳÓȿԕfϲ',
                            'ǖ*ǣƺŰˏӷǁлƋ"ʨˢ\x9bδȥˈūnõêћãӊьˤȬ¨žȹ',
                            'ҞƽC˹˦ӾӱԔԂҨȁϺJχˤ#\x89cíǾɣȸӫҢƸƨҚ˨Ү˩',
                            "Ҥҏд³ʛʭӃӭűɊǎԭ,ɦϏɰÏ'҃ƅϠԡʏŲЃξʀĊ\x95ȭ",
                            'ӟȘȺ"ĠȦӶƸǕΰӱφıϛHњ҈ԎϠƬä\u0378МqͰЄѡȺńŧ',
                            'Ђ(ɏǒȕİщɤˊ©Ҧ˰ұā˖Ŕ\u038dǈǍԋƅǸȿoӥ±ҼUȇԜ',
                            'ҌȒϘɩΟЁƯӋʐ#҉ҽãɕĂϺʹÙáԋԐЬʻ΅[ȉӮϡѾƨ',
                            'ӅğˌŁŅƭŞʉξιӋȇҞɎɁҝƳѪȫl5ͲӬʑĒіƕǔΞï',
                            "ӑʘĔmХΫСԫɯτԁéҌ'ѓ˄Ŝ¡ʳɧλļКǂ˕ʫä¾ϳƪ",
                            'Ӧ¬ΝώҸʀʊǚɡyҁňÝͶǒ\x9cҀŒǜˎǘЋ˫ƙÎήԩιƢѬ',
                        ],
                },
                {
                    'action': 'ǤɻϽğŎǮϟț#¶ʏК+ĀˣŀL\x7fԥkkӮͻ˞Ȓ5гԠǔІ',
                    'resources': [
                            'ăˉîԂ@ԍʢß6ŻĆшӤͽӑѢÑѥρԂҚ˥ȗŉΌÛԞʏҙШ',
                            'ɎӢьҙжɂԚΫҐʖӍôIȖҕϝͿ²ȣҚ5ҿΉǉҳȣ˂ӯӚç',
                            'Ҥɖmʶ[џDėCƟӾ©ȨƗҟŁǡϝвϥͱϲʩЇe\x8e²҃ɷĖ',
                            'X˔ȿ˔ϸ`ʧȤІԈ˦®zÅˬӽĪϐҾӇПΰеǠПҗɩяǦɠ',
                            '҈ˤ˦RυͶǚӺͼ¨ӞҙɃˍțжԢѴǐˡψĥҾ ĭЕĒYіΚ',
                            '\u03a2ĠMɵҭǿ÷ĄŔȐ"ʬӖŕВҰœĉȁξ\x95ȉǝťɩz;ʘƐǑ',
                            '¬˯Ī҂Љс˨ϲǦɴԧÊǞʀҜҷӶɪѠЬĥԩǊƓƥΊҐǽɨϼ',
                            'ӕЗƬƮϵ\x82ˎȈƨΰқѶ\x94ӿɨ-˹ԊɍŌȮВƕХ\x83ǳlˣɃˣ',
                            'ҞԈǷԔReӾҫŮWͶͻV˼Ŵ\u0382ƬNӡʃáѽ\x99ʛŸӓêξύ¶',
                            'ĞЛɁʸӈǱӓʥӺӂȈǟǋ˭˽ƛϕȻŸҺѧɯϘĊSŠ\x95ΆÌ\x9f',
                        ],
                },
                {
                    'action': 'ǲύϡ˽ķˑǡŗҫθҲ}ʐìˣɀʹū˭ĥΟӋȩďәđĪȁ¨Б',
                    'resources': [
                            'þȒжӘɀϒԪƙƝɇρӦΔҙљn\x96ҲʭʘɘɊɤ\x95ν\x8bɑЦΫԥ',
                            'ĽΠ;\xadƯőÛɹҼŏȃΝϘÿʘПǢѴӈÐѦˮzαǋ°9/â˓',
                            'ƔϮ`ǜœƄΖиϠҦҜΜΚǽƧɐ\u038dԠгȝҴɸɁ¬Ϥ9ȈɰªƝ',
                            'ƺˤӰӋҿʂɦÉɋmɄѻр\u038b5ԐsҪȧԡӲÿӍʆʞҦЮ#ʵˌ',
                            'ȑȭƹ҉\x9cĝͶư#ǝ\x8f;ǭѭөӄ˖ӭͰϗňXǥςΩSӮůƌЕ',
                            '»ʹŅǿ9ҥƲĿɸϟ҇ԘǏʖ˥ʵoǂʼŗϳƸĄͻҩπȖȉÏȕ',
                            '˻¾җжύіɝӗŸˈřώԮǼѡҺϱŎņƒЈÙώлΩЛ}ȎRƾ',
                            'ԭΊȦ5\xa0k·ΰǌȖмȿŎԤǰԢpΙĩƯȝƛúǚчʱ҄Ԡȹг',
                            'āˣЮЊĬǄŴeϿҴʵɄeЂŋɕʠдgȶɇĿʎчȨʕɡŐğЖ',
                            'Ϛԅəл˖ʔǃЍœҵÓ¾ԖύѯȈšԊҋϫȬԠµ»ŘӉGŸӯʒ',
                        ],
                },
                {
                    'action': 'A¯ʦĨҨΕЁ½ʹμǞϠËȱȳ=ȳҍǄϣ`Ų¨Š}ēøʹýģ',
                    'resources': [
                            'νҺԋѪϔŽьʪŜΈήʫȤ$˺Ĥ҈ÁӒźŻιɗь~Ċԏϲӷȹ',
                            'ɗǌŲ҆ǏԤЂpɊҜԎʯ\x99ͲΡƉċσΐ¢ƫЕϔ~ǀPȇыǌЇ',
                            'ɾßŧʼ¾єĈʸÐĄʭѸҏīтԝЈÎȾëѲʗѸƘG`ßΩαȦ',
                            '\x7fάҸĤʩƭËѪŁͽҟʥΌÊƘƪԋэ˶Ɵ˽WϔğʮǪū˵êԢ',
                            'ĦϦϘңɋ˾ӼʠԈю+ńԊΈѿ\x8cż´юƚŹϻˤˤ˂ӹùбć\u038b',
                            'ҍϫĕ˹B˼ǳԜłӿ\\ԞɌ×ǒκ´sz҆˞ǿӮѱ˷ЫΎϧӁР',
                            'ӟ\x9fҎŸȊnӹɥчѨ«\x8ečȥҲˬéϥ¢Αƴѿ\x7f:ǲǱǃȶmϕ',
                            '±ȟťλҎĤΣѥѻ˗ɐԁ^¡˩ʊɲѵʽҠєƩѤE\x8dòȨӑŕħ',
                            'Ǻɯvԏ˨ƲӍ\x9aϐĢϱÿǻО\x9c˘gȣШŴͱĭǂɅлӏŰ$2ҿ',
                            'θȮʸ\x97ǓʈΥΑΧĬ˓ĪȭľʮbͰҨҊɗҗFʟsϝʏ5ŚɲÅ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʥȯӇ',

            'version': [
                -6455950397413774052,
                -4966334383108938594,
                -2666748855837410811,
            ],

            'location': [
                'ƒ',
            ],

            'runtime': '0',

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
            'name': 'ʩŬʚêʬɰӀĥƚ˳ҍЭTǏǿǛ\xadп\x98ƀ[³ƴǲp҆ŉĐƕ¸',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӞϓȦ',

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
            '$': 'Ҍmʡ4ɫ§ʐɰәĵӉҵҐƾ˶ŰϬÌԨʩþŗ@˫ȋǆѐ˗ȥ·',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 3328006596391274089,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 54718.00606122764,
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
            '$': '20210211:175536.440592:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ġњ҉ϼщĶāǲȫɖăүɠͲĭ÷љ҃ЂȁŕˍϵӭƷ˝ČÙѺ҅',
                'ǆŞбӀǽƘҀĪНϾċñɜӲȪ!ʄσŏÃÛdСӀúʻďƹƏΏ',
                'ưбʅǌÎɛԎВʿîԀ¤ńΐӪϫҊÑʦѬi.Ӻ9бОĜԏɎɯ',
                'ЀĊӧѮÁӭήΑҡʂɖĩҋ÷Ѽćǘʿ\x90ҞӲȬϒŨΧȢ|ҾΖϬ',
                'ʫ½ғΧUfëǖңėȢȯ\x90лǱ˽ˎĵǵϧʙŽTԁʦʹĀӑҙȚ',
                'ГÝȖƔǶӮyϾȚĽȠϢĕΊƦ¤Ƕ҅ǔΜʦϑΓɾӀЗƩВ\x84Ѿ',
                'ƼƮйgЫȜԧѺǍΜͽѬĴ˙Ľʊ°ɛˣΡȢBͿà£|ȳȚȍĞ',
                'ԣǿɿʈ˥о¬ǺҸȌġϜÀ˴ơɉϤŮɩϷɭ²ĒʿфљЂ˂3Ȍ',
                'ȥδˡԁɉȊɥƻ;ĳňȮǘĊҏ\x8dЛƖˇɆɻΠǚśŠԜ˥ɠόϡ',
                'Χʤ«ӃȤ±ňΖü˜8ʧǜ˵ӁɘȪɆѣǃӶǳεũ\x9cԎʋϝǸƹ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                5901504585742279231,
                -6824882791157017799,
                8189384215889331239,
                -6232732292488826323,
                -6598008581925454431,
                7065099595862672107,
                -3306557029819230147,
                -823572440508730997,
                -6636588281528321110,
                4615213014522719472,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                755944.8477743047,
                -12667.92982192876,
                224591.80012626312,
                484606.15720930963,
                268845.0674078079,
                41889.73224955361,
                829989.2801207113,
                539920.6445687976,
                358647.6165181293,
                -82274.538184175,
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
                '20210211:175536.441399:+0000',
                '20210211:175536.441412:+0000',
                '20210211:175536.441419:+0000',
                '20210211:175536.441425:+0000',
                '20210211:175536.441430:+0000',
                '20210211:175536.441436:+0000',
                '20210211:175536.441441:+0000',
                '20210211:175536.441447:+0000',
                '20210211:175536.441452:+0000',
                '20210211:175536.441457:+0000',
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
            'name': 'ЧσɵҥǄҸ)',
            'value': {
                '^': 'int_list',
                '$': [
                    -2575016002094214601,
                    -5003731118031345782,
                    5805184355512912721,
                    -6684056974403332339,
                    -7638677281929593077,
                    6736371171765953266,
                    2588061365976487001,
                    6913231997747459347,
                    -4860797701937092104,
                    -5374529059602640784,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x8b',

            'value': {
                '^': 'int',
                '$': -2342303937517275578,
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
            'catalog': '҄\\Ėǽв?˯зǅӯǳuȣŀ˓ǲțĻшўˠţŸƭӵũӐҸШʓ',
            'message': 'ˤˌɺ҂ɆåîȮΒȡΒ\u0382ÚԟЀЭʦϘвѦӾǽєŴѡԄʫĸҠп',
            'arguments': [
                {
                    'name': 'ƒTŊɤԓȁȫϩӡþϧϛ1ҊɐϚd=˄ɢЍҡƶŚȉ΅Έāεӯ',
                    'value': {
                            '^': 'float',
                            '$': 963163.0587165742,
                        },
                },
                {
                    'name': 'ɐbƓĢԫĺʏ\x92ŴǙ¼ѻΕĤȯȘϻȽ«ҭԑҫλӉɞ',
                    'value': {
                            '^': 'int',
                            '$': -4818042068475212661,
                        },
                },
                {
                    'name': 'ȘӳƚĝǕʕȁў˻ǔ˞˒к<Ξ˧ѬYʮʳȲɣ\x95õőɍōәÇӌ',
                    'value': {
                            '^': 'string',
                            '$': 'ũƪԏ˦ԑҾ#5MĮƒǇЄʆȒӑӆɜѻԆ˖àѶþАȄ\x7fĦ\u0381ʌ',
                        },
                },
                {
                    'name': 'äʀG˓ρлͷпЧƑŏĂ\x94ҼyԔԁłʥΏ¤ˇΆ ˊ҉αрȠћ',
                    'value': {
                            '^': 'string',
                            '$': 'ɐ\x9eŸӷƞǰ˲ǴòŌ*ʦÄҵȑďƦŅҍ˻ҼԙªáƢÎĊЏӈÏ',
                        },
                },
                {
                    'name': 'ºʛЦƞĞ®Ƞ"ɁсǼüʽŢ\x7fļѨŊéļӭԧɉǖјГÔäþҟ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210211:175536.438674:+0000',
                        },
                },
                {
                    'name': 'āYϲÛ¿ЊˁӛĠÓ˲Ǔͺ-ʟǳè',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -1416644476615888448,
                                        3820873244028338633,
                                        -7810320814206816709,
                                    ],
                        },
                },
                {
                    'name': '˥ӝāoǆȡӂ\x9cƍRɏҦ˦',
                    'value': {
                            '^': 'datetime',
                            '$': '20210211:175536.439186:+0000',
                        },
                },
                {
                    'name': 'ѝĶǙԃ=ЕʌӺU',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        886880.8224684355,
                                        230439.44078286586,
                                        809103.3650017328,
                                        619616.0889864309,
                                        230801.1844016341,
                                        130481.82201483514,
                                        149449.20521996546,
                                        523248.6195715602,
                                        394680.8486439187,
                                        514748.5313006439,
                                    ],
                        },
                },
                {
                    'name': 'Ìlė\x85ɒЧϤƺWЭ·\u0379»ςȄғ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        273729.96852305223,
                                        734381.7226874529,
                                        51798.77260789959,
                                        489936.26700924465,
                                        145027.90709409348,
                                        898712.8039415451,
                                        -17712.245154435033,
                                        831100.1204954741,
                                        11429.751091802143,
                                        713756.1702910167,
                                    ],
                        },
                },
                {
                    'name': 'яǙƭɥ§ϋκÙҶįѧŀ¹ƬʌЗʍΎZ©{ćgР΅Ⱦ\x8fʫŉѸ',
                    'value': {
                            '^': 'int',
                            '$': 3788633849190169563,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ž҂',

            'message': '·',

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
            'identifier': 'ñЦРԡũȄîѼȥӏϳŗΡԨǺѴпəɩԕåͰ¨ω`ʳħŁϓэ',
            'categories': [
                'network',
                'network',
                'access-restriction',
                'internal',
                'os',
                'configuration',
                'internal',
                'internal',
                'network',
                'access-restriction',
            ],
            'source': 'ΡnüÓύƀ\xa0ƽӧ˺Ұӳëɚ\x85ĄÇÅ\x87ѸѯʦôʐӄэɠѻҢӹ',
            'messages': [
                {
                    'catalog': 'ĩѝtΐĄ҈˅ɷʌ\x8dȫɜӓhҋκəʔʏņȫ˲õ=cЃĐћӲ˫',
                    'message': 'ѬɦђϩӘ˷ӥϮεa_ʒӵxϩό±ƤǠǐǝЗƍҥ˶ӚƘ0\x8cŻ',
                    'arguments': [
                            {
                                        'name': 'ÙŭэνƙӘsɜcΕ˚łɘöгzѤĀϚҶƞƎ)@ʎϓʧЂӨÂ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ШǁӀϱƵûόтǭřɕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175536.409222:+0000',
                                                                            '20210211:175536.409251:+0000',
                                                                            '20210211:175536.409260:+0000',
                                                                            '20210211:175536.409268:+0000',
                                                                            '20210211:175536.409274:+0000',
                                                                            '20210211:175536.409281:+0000',
                                                                            '20210211:175536.409287:+0000',
                                                                            '20210211:175536.409294:+0000',
                                                                            '20210211:175536.409300:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'tѸȅҊϴʲˢƬcʷэĤӔ1ʍϤ҂ưʐ,υįǷЦƀ\x9flƥч',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2636761803836692511,
                                                    },
                                    },
                            {
                                        'name': '˜¬',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 431321.00016709836,
                                                    },
                                    },
                            {
                                        'name': 'ӺҳÝϸTʁȡӎʰēȋtsˊЃΠ˲žɤ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԩǣѿҖcǧù©êȴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8121790723757087455,
                                                    },
                                    },
                            {
                                        'name': 'Ì˟ɆͺҎȫͱўьӋĹӆԆě˫ϯ˂ưѹɺєȍϊӭǺԩɃǭÜϴ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3997563202592509915,
                                                                            -8510081139004199248,
                                                                            5335252332282216402,
                                                                            -7828887567814086388,
                                                                            1362724759334914367,
                                                                            -6424833263882677237,
                                                                            -5829196143670046808,
                                                                            360485271823350007,
                                                                            2271491980930787968,
                                                                            6313849230597594564,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '`˼ĐѭǃҺђԣӾЎϙǐԌӛӧƥáʾÍѫğǑΰѳ\x90ǥůҕ¥Ǫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175536.410467:+0000',
                                                                            '20210211:175536.410483:+0000',
                                                                            '20210211:175536.410491:+0000',
                                                                            '20210211:175536.410497:+0000',
                                                                            '20210211:175536.410503:+0000',
                                                                            '20210211:175536.410508:+0000',
                                                                            '20210211:175536.410514:+0000',
                                                                            '20210211:175536.410519:+0000',
                                                                            '20210211:175536.410525:+0000',
                                                                            '20210211:175536.410531:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ō,ӎ˱tΏưɮǅρɧ·ЫĥΆѼΛǐҦВҠbϻȞϩąǚРƭɟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            416595598133446077,
                                                                            -6092201653970510936,
                                                                            -1142718086397119824,
                                                                            -3916322003655708042,
                                                                            2637204202249846395,
                                                                            4850570579736514456,
                                                                            -2348523285447740712,
                                                                            -4115222880796673166,
                                                                            -1092681225778278210,
                                                                            -905077592147999874,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˊÎŨЋЬͲ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            114432.04385544479,
                                                                            626700.4006900622,
                                                                            467575.9077229769,
                                                                            857800.1304871332,
                                                                            496728.9117407565,
                                                                            181211.38537359843,
                                                                            64110.26196966664,
                                                                            303844.80611572944,
                                                                            398582.5057305132,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '҄ҷŐҮȦӋҎ"˃ÚƻſҗǺʵӨ\u0379\x90øѶŚњģιȡʭЌѰƆǭ',
                    'message': 'ǔѡɦÂҧ\x8aƫCҰϝτǩчѤˈԄԤӀүΛѹŬϬʲƱċԣҥгȚ',
                    'arguments': [
                            {
                                        'name': 'ɸœųɶ˨ӖŞȿƦɯ¡ľ©ƜϺƘ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8290404474481657949,
                                                    },
                                    },
                            {
                                        'name': '£nЙϕ2ÀNƷ\u0381cŮӖƢѴȅĞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175536.411600:+0000',
                                                                            '20210211:175536.411612:+0000',
                                                                            '20210211:175536.411620:+0000',
                                                                            '20210211:175536.411626:+0000',
                                                                            '20210211:175536.411632:+0000',
                                                                            '20210211:175536.411638:+0000',
                                                                            '20210211:175536.411643:+0000',
                                                                            '20210211:175536.411649:+0000',
                                                                            '20210211:175536.411654:+0000',
                                                                            '20210211:175536.411660:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˕ƎĞʝmҨЩӬϽ¿ȏĻƹͳd\x8aԙŤˬǷ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1675593983137967858,
                                                                            -8931316155059410132,
                                                                            8732684318664157880,
                                                                            6649114603620719868,
                                                                            5048470347544600695,
                                                                            1368427678688145243,
                                                                            -864977177538575841,
                                                                            906910900104907516,
                                                                            4693922538486688476,
                                                                            3132162976766542275,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǭʃ˼ķ¼śʊԩºΐҾĺԁќ0ϰĶҬґΑμԙǴӍͽϵљΔҸˣ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˎԐǻĕŇ(іȥŽƝ҃Γ\x9bϙϭǥҸ˵Ӥ§ҫŖҜȴǢ^ʙǒ§\x80',
                                                                            "ӁǠ!ҒɼϯVԔΕä\x95'ȿƬȩğҐаЯ¹ĵÒҼǱƉӐĚƇ\u0378ϕ",
                                                                            'ħǿYϦлҟªǍņҴδ@Ӂ©ƺˬʛāϲϫ˓ҰЇӾʔӝҰxӃ\x91',
                                                                            'ԜǽСǌΎʀċΰѽ¿ӎɚǁ\u0378\x9d1ЇʾЯȿϨͺĉ\x81ӂɶȂĈġҮ',
                                                                            'ёɰА˘ӪӐѠҡөʊѹ«ʐѲ0πӹ˟ӣʅϦ˶ϲƫƵȨȍϑPΐ',
                                                                            '˸ČłϮѩӄ*\x93Ӵ\x84ĞŋöҮҪѮʂǄ¾P^ʩ=ψ϶ɎɶȵĂʛ',
                                                                            'ĸΫċŹńxΎĜӈÜѰΖсȳԥӨ%ʞǙӚºƛŌЁ¬Дɂˀ^ȏ',
                                                                            'ҫ¡ʡцӕˀɹөL˳$6Ϫ÷Àpįі\u0383ԜͳЃŰҭƼȄэƢԋʞ',
                                                                            'ƊҨ±{ƵƘƯɿ˙ƶШƻӢλȽƭԋĬʈґφҍÈȏϬϔƝӢұǅ',
                                                                            '\x89яǡѕoŎͰĠўкɷԋʼsцѲČ˵ԟűìіӍ˗ǣϠϩɁÌĚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϙįҮϓͱʮ҉ŬԐñȾǎԬēʗ˳҈ӎϧűǹϺzѣӔºŪ˅Ǫ˄',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 735540.2875085339,
                                                    },
                                    },
                            {
                                        'name': 'ć˶',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9111565862462170846,
                                                                            -7825539836565595942,
                                                                            3592457753394507456,
                                                                            -2107174440813841301,
                                                                            3058205115852298211,
                                                                            -1630521315931828812,
                                                                            2147641657435598877,
                                                                            3221763270993069648,
                                                                            -4205975014675746365,
                                                                            -7126913030697135491,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʂʰÊa"ˢЌӲɂöɦɲҢѦҞʘ£ȉǙȱЄǞʲΆʱ\x84Ζ϶өŉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            469876.37528865587,
                                                                            528178.718678944,
                                                                            340079.22601431544,
                                                                            63829.55410235279,
                                                                            876374.1631828398,
                                                                            982872.2460724385,
                                                                            215125.4533988486,
                                                                            -82229.25589973913,
                                                                            250802.86507724813,
                                                                            418048.3558790917,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ú>ԒҎĸɋΨϧÕƮԒȍʮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "еƝʨ+®ţ\x91ɡӊ˫ϷÕˢЅәѓ˩U\u0383˹ƘǄӯƻН'ѰʆɾЃ",
                                                                            '~ŮSʹӄϩГ¹ÚиОģÂƉɌůǨ¯Ґү\u0380ԥǆҙԕϏ,˔\u0378ļ',
                                                                            'Ԧʶ»ԛƉˢĹĘҲΣŐЍDȆƾԍȧˉӣÕˑǞˮɈӔȯgț}ǽ',
                                                                            'ѥȭͿБŊÔºǪļ˼ʲͲÄ²ųѳE0ԕĚʤɃǉǉȁ˰ԄӪϠȊ',
                                                                            '\x9dʼėҩɏ˥Ǝʏ¸ӤǿŗНôȘ\x8duʑѦҮɠēơ\u038bЪнѕѦΫ˄',
                                                                            'ã[RԁĂҵųĆɅCˊϠ҃Ɇʭήǯ\u0379ͻ×˨МďҽÍҕʡŷɋͽ',
                                                                            'æXˢԚһȹ΄ӍǁÊAʿ΅¼ˍɈϲƆґXɧÊˑӣǜʤϧȮ1Ǳ',
                                                                            'Ѫ\x98hӮϹő·ϓ\\ђ^ŐɳabЉΡƧӻƾτ`˘ƟʄлОȝĝŭ',
                                                                            'ɆǂąӅˌŲɘñҰӿԠțļˇԁȐϊΜΖlǁӀȌϬʟ΅ǟĵӔҶ',
                                                                            'aĚǄԭˡΡ·qѩӻƋťőʊϾîЛƸ΅ӗ҃҇ͺ\x81ÞϳǨðҶƵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÝǞƥǸБʞΠó˽ÛҩɓƶȸoӴɊÄ΄҉˻ԇoϱɃ$ʧʵЍň',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '®Ԡ_äұĨˀˏɪСSêôυ¨ű\x85ҀЂҫĝ«iǜϵɡѨπЌÑ',
                                                    },
                                    },
                            {
                                        'name': 'ӶԓǮɯГʭȄΑǐľӝʩΥ@ͷϣÛǵ˕\x91ʺĶǿȥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            647180.6812973474,
                                                                            711629.9109071641,
                                                                            585788.1421353655,
                                                                            657456.2811563684,
                                                                            -70587.49668562334,
                                                                            615149.8867364549,
                                                                            948119.9621295277,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'НŎĥҤѿҎʓʞ,ɰϰ˽uя\x8bǅ˵Ŝȡ˸γɢǼFͰҌ˥ͺ\x86м',
                    'message': 'ʡҒƎШ{Кʓвúƾɯķŷ\x7fȨƐˑκǷԝėʂ\x91ʷ´Ȩ~áТŒ',
                    'arguments': [
                            {
                                        'name': 'ĠΊԋӾ¥ˢƐ\x9eЗҜƅюҾ<ô\x85ԝ×\u03a2\x95Ưǯɝˢ˾ŏԮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 458947.5406315918,
                                                    },
                                    },
                            {
                                        'name': "țҬĄτǙ'\x93",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175536.414254:+0000',
                                                                            '20210211:175536.414267:+0000',
                                                                            '20210211:175536.414275:+0000',
                                                                            '20210211:175536.414281:+0000',
                                                                            '20210211:175536.414287:+0000',
                                                                            '20210211:175536.414292:+0000',
                                                                            '20210211:175536.414298:+0000',
                                                                            '20210211:175536.414303:+0000',
                                                                            '20210211:175536.414309:+0000',
                                                                            '20210211:175536.414314:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ІЕДȜȷɍζȑ˥[ζ˅\x9aτϊơġԘ˳ȨťʹԭѰ)ЅѮ˓˙ӆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1500647670182199683,
                                                                            -876491712652449992,
                                                                            -1627679902859671007,
                                                                            2992224669389358051,
                                                                            -8312568237529670960,
                                                                            7892328363239174183,
                                                                            -7073613284600671742,
                                                                            -983592771376220872,
                                                                            -2415181619570452746,
                                                                            6436568109054514970,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѼҭƲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɍŴЩʵÅΡϽɌòφҸȧŶ¦ӳĬʼȇĨƗÕӼΜǟάǵɃŅʷĹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ӛˍюʖ\u0383ęίȬǼάΎʓԖƑθǔŽУӖ\xa0ƫƴΞӻɷǋҏЏȨІ',
                                                    },
                                    },
                            {
                                        'name': 'ϱїħԪтvѱ#ўĦεΕЄã\u038d҆ԄƟϽϪ6ˬƛƃ>ÕϡЮƙȈ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175536.415020:+0000',
                                                                            '20210211:175536.415032:+0000',
                                                                            '20210211:175536.415039:+0000',
                                                                            '20210211:175536.415045:+0000',
                                                                            '20210211:175536.415050:+0000',
                                                                            '20210211:175536.415056:+0000',
                                                                            '20210211:175536.415062:+0000',
                                                                            '20210211:175536.415067:+0000',
                                                                            '20210211:175536.415072:+0000',
                                                                            '20210211:175536.415078:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǬΈƢϩŞĹ\x89',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ʈÇÃҭďϳ\x98Ēɛĩ;ɭҲqÀƂΧŠUƚњͿđ\x9fĊăʴƸűԤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 471081.1559627,
                                                    },
                                    },
                            {
                                        'name': 'ǺӴͺ¡ȲśӹȒǙîŦkǃĵóɊʙ\x80ʏ½ðʭëӑЏƽˁ\x81ˮÞ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'Ǡ¼ҪϐњπϽʫê?ʿʇҧǲσϖΒҽ»;ɵʿąѤʦ*vɆÖä',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            709848.5364529374,
                                                                            851778.4874228003,
                                                                            549417.0697472518,
                                                                            423455.6697100184,
                                                                            526760.495619673,
                                                                            14030.83878435078,
                                                                            822855.7403708145,
                                                                            -10352.527120138882,
                                                                            571994.9506182538,
                                                                            335391.110865306,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˉ·ĝŞ\\ȺơӖӮˠӣʓҢǽϴ˗pǬÁЍў\x9fąȧɑ˱ǓȒÒɴ',
                    'message': '˔ɒɻҀ{.ϛʬ\x93ʥ¢ĉ˔ʖҔïвÒѭѰϋϡѺŞ΄ɓȂҫǸ÷',
                    'arguments': [
                            {
                                        'name': 'ΕŗҤȦĥ˜kȯ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Мң˗ǼȰ2˷ǞTΆД\u038dʂΫĨΆɝʕѧƶҡÇҾ˓īˊŖЗŲŎ',
                                                                            '\x9dǛ\u0380įśĘƍЬɶƴϾˌΉº҇͵:ʛӽЯ˥Ǣɔϫг˨m˹Ђѵ',
                                                                            'ȍЏǐȘΌȼʭʏ}ϸ\x96ÖōǱ˅ĽȰ˶ĊѱЧҀэ7ʵС¬-ɲц',
                                                                            'ҥғўĺӠȲч\x90Ü\x85οɍхӕˏǿӢΦ\x91эɓҒнǩĜÕǗÙʆԩ',
                                                                            'ƃқӯ\x84ҙƶХҼň˭ҶľҘɺŶöŉ!ʊFԌʲƠʉǎƗΰɣú˪',
                                                                            'ȝєfŎԥɴɂ˲ƈȧŇ)ˆȾˢʇѨʐ\x96˖Ǘ>üȸϡ}ӗЦ˾ȅ',
                                                                            'ÙY˪ҴћͽҕƉǷĚσќÜΘęôǗӝ\x92ĲҠʆơѥΥȺаϢҺɶ',
                                                                            'ɇˈɩɅʅĿɄȧŸñƞȎĮȳ˭ȾxңȭҏʤGψȵћĥѭԗцΞ',
                                                                            'ǘǿʦҭєϚεȬ\x84СеʤҺrȐϘѩż\x89ȑԬźǛ˺ɛɿԅ\x8cʠ\x8e',
                                                                            '\xadɞΉѐΞƤēɡ\x98\x87ɿüěѧʤȩшŷԇѫ¦ȕĴʃɨVϤ\x8fƾ=',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9aѢZßԓΐ1ΌӚυΝ\x8eŵӹƐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ŀqԤӒđҪƮVȅӦǋÃϞȠӱˊįĢ\x9aђÖŠǩпˌӤɗŋ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǗʾˇȒѼĆҲѫ\x8aɒóϹϣǸ\x87ǏҷȠʛŅΜǆӼÛсěΘʽ$Ũ',
                                                                            'ь¡ҹƜԐϛÉʣэӮǔѧԡʕİƲ¶ӜӬԘюúΜƑчȓ\u038bʾɣÊ',
                                                                            'Ɯ\u038b!ĀӪɹʚȭȗŎԭʭŮҙȵqϱlƛ\x8eğĨɐҥШĶϥϭҢӴ',
                                                                            'ŽǉңѕȸϾȆ\x97\x98ƛӲ¹ΌˑªˢŶŨЫԩ:ΓѤǓȜρȖ\x85ïɔ',
                                                                            'ʆοȩ±ȸą9ƓĉҘԭĘвɗŞѵʞƽԭϼͺ¶ȆɡŢI˟ʝԪå',
                                                                            'РΤи˺ІȘͶƨœȺНсҠƗϭƴƟŵ҈ȓͷɌēκǂНӥԣЋȥ',
                                                                            'ƅҥOѮҭӫïɄͽŶԭŢӶĿ˘ĪΰӧŇӱĜɻϭ˗ƤԌʦɊӞϓ',
                                                                            'n³ˢϨԆõΙxІDҽЙͲΓұҎ)ӛΈԞÅ`ϖ͵µҐϜԞɪ\u0379',
                                                                            'ԩųұҿÁŦêԌεˆӕŇɁɹ`Ƈ2ʻ˧ǘ®ӪϞϟɢɃҐ*ɤO',
                                                                            'ғġŨʓƥɩЪοԪǨƄyӪǽɐ\u0380ÈɠɗȳȨѐOӉǈμɴĊŏǯ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԇѤԇӀǛʞɲˇǠƃҺƁǰɨ#ȄɑӝX#ȳҒɁȂgЧϱ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7708692266724997862,
                                                                            -6208038778417138876,
                                                                            4070155275677990313,
                                                                            6182396765375840167,
                                                                            -2818958916131926766,
                                                                            3894588172283261113,
                                                                            815400963260138242,
                                                                            -5219877865069643173,
                                                                            4247987448423632980,
                                                                            -1207523991215613998,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŅcѤƖϐG\xad˕Ʈȶ\x90ėðɖèɻоҷИ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175536.417859:+0000',
                                                                            '20210211:175536.417875:+0000',
                                                                            '20210211:175536.417883:+0000',
                                                                            '20210211:175536.417889:+0000',
                                                                            '20210211:175536.417895:+0000',
                                                                            '20210211:175536.417900:+0000',
                                                                            '20210211:175536.417906:+0000',
                                                                            '20210211:175536.417911:+0000',
                                                                            '20210211:175536.417917:+0000',
                                                                            '20210211:175536.417922:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8f',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ŗț\x9c϶ŶřƔ\x98dƏɵžÓɉӎˣ¦Ɯϔ˟˛ͷϢԎDĤ˱Аǯ˗',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɮ§Ȭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 700900.2619496505,
                                                    },
                                    },
                            {
                                        'name': 'ʸЭ҇ʎԏˤ˗гǇГб¸Ԡ¹ő©҃ʘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΣǢ\u0378ɶȬѣˢЁ÷οĐLȖФżŒ\u0382*ȸόϳßɌїТσУ-\\ą',
                                                    },
                                    },
                            {
                                        'name': 'ԤӧÛ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6241020032529978863,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x94˚ɲɋԗΐƟǤ3Ǩ4ѯѱљţˍӬ\u0381ΝѢĥҍɔ˗˓ŧ҃\x9dɉS',
                    'message': 'ӮƘЃĘєϣҢƑƙƋҽӔԔϨұğӋςʟBƥȱ=ƼԭХȲԚęʷ',
                    'arguments': [
                            {
                                        'name': 'ѵiȢЇyͳԒ˾ѩԇ5ʞʀȹ·\x9ahĿƱOǼǥˌҧϧ˝Ł҈ŘΓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1484935998158632022,
                                                    },
                                    },
                            {
                                        'name': 'ĕŏ˾',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 682898.6883386708,
                                                    },
                                    },
                            {
                                        'name': 'єɟɲ˟үŸ\xadԕΧҊˆӧʰĚβȳ;ΞҕӲ^ȂӘʮҨъΓӹW4',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɔʕӐˉпȬ¨\x9bǁͰ˾ϑѧʘʐиʬɷáҏ\x8fϏʖõŘΞĕ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȹѨüϒÑƧȆѐ[ӁԗǆԤΊжǛȗ˓ѻʢÊϸƫưұs',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175536.419680:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϙʣÝ#Ɵʷi\x8cɮǳ\xa0O\x88ҜňµÕÊě',
                                        'value': {
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '§ңƀшÈҋɯоԓǐӯϙΠјƅĜʋƔϪё΄ǤƘѬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӞɰŊж˨ɚÁȵӥ˸ϨȥŤѪɸÉ®\x96SǷзȀªӂȯОMԟ}ĕ',
                                                    },
                                    },
                            {
                                        'name': 'ͻ\u0381ϡԠŅʠԭ£åђʯćɔɦȵµj½ʩƾŦWm',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1853530071814752432,
                                                                            3501232295731993694,
                                                                            -7544835207868644474,
                                                                            4418858859830921939,
                                                                            7200780102338964311,
                                                                            -4379433386039307715,
                                                                            8418018281523338970,
                                                                            5177899926085568825,
                                                                            4153991935138359566,
                                                                            352301638085784019,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ślćàԣ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'čȄи?źþÛеƚФӇƬwͽķŠƕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "óǝκҝXjӿў;ŬӂɯtÀˑԛúɬȻ'ǋτͰʖЕͻCκèɑ",
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԭȰƔʶΈΈɞŢ˺ɳЎʋįɺbȳȐңɼȑ\x9aǐʀØɏʧŮ7ƣЊ',
                    'message': 'ť϶ÌʍґΤЖРu-ŕĺҽϺЬΆζɠϳƄǺҧ|ʚӏɻήǜϨɞ',
                    'arguments': [
                            {
                                        'name': 'ƘϞыÛ\x8dĹpżďӾ\x83ě¢ºːťĮǩӡͿЩˍǉ?łѬɠкӹȕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -81316.36573039742,
                                                    },
                                    },
                            {
                                        'name': "ɧ'ͳȆμªЈШӽѳǙ\x88",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x8eʜҹXő˜Ҵ\u03a2ԕӓǩ¸dƕԝǂƆԟѕϱţѰ˭҇ÞđІӲơĘ',
                                                                            '\x98ƳȖAКБϫƝȢЦГGВ΄σĦӁēƖͼQҦҴɦϹɻϪǿŶʃ',
                                                                            'ȔÍȯЖũϵÁјëƫ\x8cΒӰԫϯǕƿŨдϦϼ¿ű˫iĒ\xa0Ӎđԫ',
                                                                            'ƎИъʥɫȌѬæ/ŭǈΐĝʅAϞBԁǵғǤҚΙɌжұŇɡɆБ',
                                                                            'ȮϹӵΓ1\x91Њӭ˝Ġđ\x9fǩʊԒжǄѻɢԨЛć¦ТӕЇÇҪĥĜ',
                                                                            'ˬԃҜǱѳpʖąт\x80ȂƯͺԨɕΨЈυǖƢѴ=\x9bӅɚԒЃȑìл',
                                                                            ':Ǹ\x92ȯǣÏʼϠɄЂĿќŕˆȑ¤ȅÀɵɷʵϹ˺ĭӰVЙњͰԫ',
                                                                            'ãΌљȌҭȁƔЍ\\cɄKœØсĈðǵŷǫѲƀӃԣԎӑʖjäŲ',
                                                                            'ϻӞεĴ˜ƟϐǢӫń\x88GұӧϞɅĎІћǮɑњuШɚșļÒS˓',
                                                                            'Ӧɢ˯ѨÊ˴ϤмШƭͷснdŞϣ\x95лȫԉѠӏĞͱюҔʒЯϿӉ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҟҹˈОҸĒԕʾԜʆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 614438.7423844278,
                                                    },
                                    },
                            {
                                        'name': 'ǳ¿ǝɠӓѾʲɕѡѴЈГҴ\x8eĪȾ\u0383Ϧu',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6008782004411413747,
                                                    },
                                    },
                            {
                                        'name': 'Ԛңʂșŧƽ˟¯ÇĳóʼȇϾzκʊΞ˭˰Ǟȸ͵ȚƁΔŃoǊß',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'řϳӊғԣБɈɬŢƏǫҧԢμӽšңȉӥÅ҇ſeҠïȑȡżͶБ',
                                                    },
                                    },
                            {
                                        'name': 'ÇĊěrԛ¿ϑ¥ϕȀѾΠίћƴ9üɻʡʙ˭ȾQʯŹˠ\x8bŗѦζ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҸЅĬĲ$ΊˋчĀǂśʰӥϔąĶŲäǐ\x96ӷʓӕfʳˡĐӽªϡ',
                                                    },
                                    },
                            {
                                        'name': 'ȗ˺Ӥ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ξ=ǉăԀ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6396491957589796955,
                                                                            -7543023937705328835,
                                                                            2231581818149399812,
                                                                            8350763306206310716,
                                                                            5713085151477302691,
                                                                            6325712735922527637,
                                                                            1952343489120702546,
                                                                            5695585411137426191,
                                                                            -4389588199804924673,
                                                                            -7039502302419719953,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŏԛβҶСϮ˰®Űɵɕȉ\x9c0ҕ5 ȢŵŭŁˣůϱǈƏÙɋâ˒',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2420852999138861060,
                                                    },
                                    },
                            {
                                        'name': 'èŉШĵkҥԌΕ¦Ȟş',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175536.422676:+0000',
                                                                            '20210211:175536.422691:+0000',
                                                                            '20210211:175536.422699:+0000',
                                                                            '20210211:175536.422705:+0000',
                                                                            '20210211:175536.422710:+0000',
                                                                            '20210211:175536.422716:+0000',
                                                                            '20210211:175536.422721:+0000',
                                                                            '20210211:175536.422726:+0000',
                                                                            '20210211:175536.422750:+0000',
                                                                            '20210211:175536.422756:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϡ˅tԩǼˬ˫¢ώӈԆʟŧɮȇſШÇӿӊҝɵӒήĹͳˏšīН',
                    'message': 'ǏÝΎőƟ6ӂɶѦЋȵèӿRэϠȦʍԎȊȷΦzïçӑǢʖ³Ğ',
                    'arguments': [
                            {
                                        'name': 'ӛҨŌũҘː¿9ťΎɫϳƹǷɗʽ$',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŲīŷʦůѿӃТˎɍρІǤˮ˟ϦʶΖǺ\x85ÚşОо˾ԋʞǚΕ:',
                                                                            'έɩҩƹřϊƵʁǓҖČҭȀɐ˱ʝȷΓ0ʓÀ¿ſԒӮԢӂџҲs',
                                                                            'ĲǊ˷ʭȐǨΎдϱǩÿƼѮӜɷ\u0383ƖÚġҍΑˠʣϕÎŋ\xa0ӯaǣ',
                                                                            'ϠӶˣҢʤЦ˱˞ȿɦ?ϘʠɌтĐƼʺφҺҺòĺAӫѻїҩ~Ӥ',
                                                                            'Ƀѝ7ЛEқΥƶԀФŌǔϽĴэӘǤЏƃҪ«˸КӖĥƩǠʔ\x91ư',
                                                                            'ǭŞ·ɔȠɝҎƇ¨ÒƱûțĬɾʻɢ˛RɫɪȷǬѕǯ6Ӷɻ˕ы',
                                                                            'Ǵ\u0379ÉȀǵŻϵƭԊсŖ҉ҴđƲ4ɡȼƨԥǘҔå\x94ȟЪƦ\x86ɦҁ',
                                                                            '1\xa0ѪŪGӜӫҩ˹ѝΔΣ˳i{Ʊä]˂ϚЕǑɺįƙSńмԄԛ',
                                                                            'ѭΓûұ<БΚϟϲѬVҏЏĶϸӊʮӘҍˁǒcεɣˏчíÍtʟ',
                                                                            'Ͽʛȉ˚ʖӖƋѲ:·ȧЍȨ\u0380ōęͿ\x99Ųʏηù¦ЏȎɎҲȋ\u0380ύ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԬӪϒʾ>ˍҾäĺ\x81ϛƑȺԨϷΘɗάȣ|\x98ŭε',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175536.424650:+0000',
                                                                            '20210211:175536.424680:+0000',
                                                                            '20210211:175536.424688:+0000',
                                                                            '20210211:175536.424694:+0000',
                                                                            '20210211:175536.424699:+0000',
                                                                            '20210211:175536.424705:+0000',
                                                                            '20210211:175536.424711:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԋ.҇ʨԂȱҐɈ²ĢĶǱȈ\x90,ӓʥ\x88Ӏο',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2297372228765087670,
                                                    },
                                    },
                            {
                                        'name': 'ӯԉťӊLnԤЍĵuŲHȹȒǬ}\x96ɪѝƹʈϤҘ?ͲˠӌuҸɥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175536.425045:+0000',
                                                    },
                                    },
                            {
                                        'name': '¨˶ȇӘκΌǭɆɓHņƨï´ØĕʶƸV˚śˮӟԪѩСŷӲԌz',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ͷӾДѶЏ˰ͽ\x8bǱ¦ʿƓðŷ"ńǥĒťƳŬǈѼɠȏŵǆԒѤǘ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8610654848884399082,
                                                                            -4199572672040310225,
                                                                            -1691708562244805476,
                                                                            -2127821824063364882,
                                                                            -3419014548922359620,
                                                                            -4523451936729898112,
                                                                            8810855966360099376,
                                                                            -6792417749282273252,
                                                                            -3314547193863912070,
                                                                            2802779086844697912,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\xa0¥ZŻőЙƈɜʱ҇˦ǇԃɌΈÐϜȜɻΣ΄<Ίǘ˚ΚŢѽһǹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175536.425537:+0000',
                                                                            '20210211:175536.425549:+0000',
                                                                            '20210211:175536.425555:+0000',
                                                                            '20210211:175536.425561:+0000',
                                                                            '20210211:175536.425567:+0000',
                                                                            '20210211:175536.425572:+0000',
                                                                            '20210211:175536.425577:+0000',
                                                                            '20210211:175536.425582:+0000',
                                                                            '20210211:175536.425588:+0000',
                                                                            '20210211:175536.425593:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ИǪϒ«%Ɠ·үԒ%ΨҕΪʧӷΪόϼφӯƙƶL\x90Ɋˡȴωφč',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЙȧΞ`ԎσȨΒʝΊƝƱϩƥзĨǠГǲØėþԮӍȞпɰ@ßǖ',
                                                    },
                                    },
                            {
                                        'name': 'ȓĴѿѰǙ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'кΘ}ТԠLӴҊηɠ\x91ęïŸԎƗǢėԗ¿ѰɤӟǒѲвſʳЅӅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ǳљ:ªÎԑХЌ8ԣɣӈĠǤ\u0382ѿ\xadǤčӿɝЁҋѡ΅ʈъȧʧӈ',
                                                                            'Ȃ\x80˲ĆѮˉҴӊӻũrӟѡŤӌ\x8dÔьʲҞŃǶ8Ǥ«ǣ҅\x80ȗу',
                                                                            'ͽúŊ˃Ⱥµą\x96ÇЈˑӯӷ½§ǞϪɋ\u0382εǰǹȂBϥШĶƇǊр',
                                                                            'ϴҏѳ\x9eƞȨˇǀʮŜҍɏԂ\x90Μ\u03a2ƤȀѐːʃԗΌѧϙǌѓŊ΅ԡ',
                                                                            'ZǃбțǒǐȀѝ¼г\x82\x86ʼǟθσѯY]ˡĻǍ·\x9bƦϊǷҝ˽\x9a',
                                                                            'чŹù˹ԐɛҠ\x8eΖͻęәУΙćāΡʆÓΣǂА˹҆ϋćɳƧ\x93Ɂ',
                                                                            'ʍҳҨˢÝ˙ϟ˕\x9aɽ˸ǫӠӧԧèǨξ\x8c\x95βʄˢҜӚńƪO)ʿ',
                                                                            '0tÝʾűҠđцǫơʁӧӏɾ\x88\x83ͻƔΒ\x9fɬʋsƨɟҁϮšҜΘ',
                                                                            'ѧԖʡȥɠĺҥҕͻɱȾrϘһЪ˦ʆґЅ)\x91ɧΑҫLԞ˳ǳȝ͵',
                                                                            'ԒϳΰƤκǝțϽёʆȪȱšˎɁӏŭŵ¿¶ƃʇĦЖˠǵĥѿѡυ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϬÛѽљΰ-µҶŮʫΣŘ\x8bǅĉМʩҎŅşȣÐҔĄÿҬ]΄ÑԠ',
                    'message': 'PȲ}ÚЕЮNɝ˦ЀȘˇƢήǳé˰ŌΝӵ˷ΤҭӱӾȰɊΝΆǬ',
                    'arguments': [
                            {
                                        'name': 'ȺҝĻëʆˎѬҩĞӠǛҵЃnȌӖРɿǚɫ$\xa0уДёӫŜ\x84βɄ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2183970758053911281,
                                                                            -3060993155724875557,
                                                                            -5210357335351565481,
                                                                            -3555019620800721993,
                                                                            -2674292269795842701,
                                                                            2602942105812486321,
                                                                            -8000756092061552165,
                                                                            -5701461425888961237,
                                                                            33804204976853197,
                                                                            734821766581241496,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҇ɧщĕƁϪ¹ɔÍƢӘĴΗGЂЈˍξϼˇǹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЃqϋѹȞȶͻé\u038dđϸQǫӯʪͷˢȭЧĽ҂ȘʜˍǏҊŔȥ˒S',
                                                                            'ҥ6ʄ:ҧϻСńƹǎѸ }ǵ\x9c-ЇӒ²ÌÜɾ!ϿƤøvӗ×Α',
                                                                            'ǊPЁԐȍη˽ǏԇȦҏʌѥɪЃΑͲĿҶɹþʟɲȉЇӪҩƎȁå',
                                                                            '\x8fĻлȻѫҮҢȳԑEȄѥѹŗҒʤ ƶшùqȌԘƆЕӽҊϻƈɏ',
                                                                            'ɯ3ˬǓˈŉˋũ\x98УǊʑǿü-řŒŭӶȽC˼ёҁҽ˟ɍƱǋΞ',
                                                                            'LşɺƈʅʈÔԞΡҵs˅дҮβˀϐƁƸŏјäÔŜ\x9bKĵȭŢʄ',
                                                                            'ѳȤ?Н\x82ͱȇVÂѶĨơăΘѫӣǍŞŹºɾÈʑʯԓ¥Ʊ҃ї˱',
                                                                            'öÀǸɢ\u0382RΏíͻЉ\x8aƉȅԊџ)ҊԡƦφңƎҾˉŒҁѺĥɵǆ',
                                                                            '\x9eʊǐɒɖƊʱάʄr˗ȟ±ǣӖҎ¨ʊŶǁЃΨԕƟԦŝ\x89ʗÿʤ',
                                                                            'ǣӇԪŵυʱПȷȂûŶʔ(ËŀġϗaԊ\u0381ØhҦϻȝϣêιƻX',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѼȽŀˏÓǣëſФƮʛƽʪӸϟȽВԜģŐѿң',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǃɟPˋɷƽ$ɼƪέФǣ9È¿ϳū\x80ʷԉӍϬĤĵԅЩ²ˁƗú',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1331650357064944340,
                                                                            -8390726616618987081,
                                                                            849112364798466002,
                                                                            4677948183091182776,
                                                                            -2903036541498040275,
                                                                            -6764089129194868017,
                                                                            -6263419222082202081,
                                                                            4881068228293035639,
                                                                            -607153595309791869,
                                                                            3033209252168112955,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'їԦ\x92Ѵȯ<ΆYʹɺħԗГƠ˲JËÎ҆-Ҝ_ϸ%þňԉҢȃǾ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                    },
                            {
                                        'name': 'ʩQƝϬŦl˕˛ĕÎǷҋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6782862598852857702,
                                                    },
                                    },
                            {
                                        'name': 'ӣ˘ʓƴŭ°ɄҵԢĆȑíĤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɖͿϾϪçӿÔ\u038bѾѐѫŁ\x8dԌ\x91Ιʾ\u038bɆ¶wɮX˺ʥɔμċŝћ',
                                                    },
                                    },
                            {
                                        'name': 'ÕʐԅԍԠԖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'nԧĮЫΝȞʢӕǑϔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1441523563025645835,
                                                                            81095652687085511,
                                                                            -1422493868720848416,
                                                                            -5337314561124716029,
                                                                            -4008594910345593328,
                                                                            1769977096006494013,
                                                                            -415459433530510880,
                                                                            -6357197150459244509,
                                                                            -3825972719931559900,
                                                                            -3294588026323431748,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϒÂ¡ѻ*¿ҘԬҼ-ɗȿγԞќA҆Ԫ˭ĲĀːɳĉҴҳ\x9bŇƃƿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѥùÙŶӯ\x83ӿǅΦǱΦ\x9dņƆʶŢ#ΖċÎĊuѾ\u038dЛԍˆԏӈǄ',
                                                                            'ԛнϊ˼Φ©ҬӠȜҐūïsʵѡŒԟҬˤĪ\xa0ȝǘӉΌϩϻKӄӡ',
                                                                            'ПɚҦcħ\u0382ġ˞ŵҦƞаƞʫікÎԏƪuζѻΣΎγӐYʗoĀ',
                                                                            'ȱʊȕƅʌӤʖ҉ϗ;ÓZ˪љɎɢńwЂʫĽŵүΟǁɀӵ҆Ԗϴ',
                                                                            'ǂČεŀıҙρßӧАʌӹļҳȸΠɣόʩнņҙ±\x83ƕΌɛVԌп',
                                                                            'ċҞĮźΣ\x80ϴlЌɿΖdҥϡɀţŲμɟφε7ҀªԣʼŴӱǨѥ',
                                                                            'ʆΡӪʬ³ѤÞД¿Ir:îφ˱Æ¹ľșzϿşkԒŒˡαω|Ы',
                                                                            '*ƃǡ¤ōѠŜ˟=ҕưӧнgɜʗʗʶƏĎʺӅΗqǢѽʵƨ\x82ҝ',
                                                                            'сßҠʖЬʬϢԠͼƆѣҰĖԏұюʣѲѭłǔũb˅Ҹ˷ˬПЂ˔',
                                                                            '˒ϏNƝȜÚ˼ӐҖɧњVʛǩźԌԖãǓɅǿɨԣώȜЫўʢǰȼ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҧȒçҮîɺϊņȠҒ½ʡö®@ΠɩĪĩ@)ӷ8čʡñ˙ҳʯɄ',
                    'message': 'ɥѴϯĸϙӅȤ˕ǪōфƠЀѳƄ1дǗӳή`ӇЄtҎө{ȑӧˎ',
                    'arguments': [
                            {
                                        'name': 'ɃŮ˪ǬŽӰʇҴrǫãӂӊ¥϶Ѥϝэұ\x9aϞ±μ|ħʞ϶пЌϞ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': '˳9ӿϒ\x9b',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -79696.44295282601,
                                                                            993838.4340551458,
                                                                            675021.9993579036,
                                                                            794075.378787697,
                                                                            72755.05103596291,
                                                                            274218.89736322465,
                                                                            692859.7331977957,
                                                                            286146.0994011265,
                                                                            111661.86627998011,
                                                                            368367.3372212643,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӁǫҡĭǸЭ˗ӯÚęÖȠɢѐ\x95ǝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˰ԚɟƌϾΓǀˆƅɴʥMԛΆɒ¬ʷѱŬјƤ{Җ\u0378ȀŞFψΞЉ',
                                                                            'ζ»ˀıњȠТʮʐɠEӳGΏҿ˪đѢ\x87кę9\x9bҼ\x81ɞǃǂϼϰ',
                                                                            'řÇôˇѥӭėÓơϜɏћʽϹȗɶȏÒΩZŲʞϴΞþҗϡ҇\x9cȺ',
                                                                            'ƱѣΚňäпǴNє\u0378ӰɰŗұіѩȲ˴žӛǆѹǍѩTȪΒʷңҪ',
                                                                            'ЉʙіψӌдʛԆҗÂŏ҉ ң¿ſГȾτƀяҒ,˨Ѯǯ\x96Ќσӧ',
                                                                            'ӫΧԩΠŋҹʦɔӅ;˴|Ҝϐǭӡ½˃Ǒ˩ЅĂѳʠ§ÂĿ1àӴ',
                                                                            'Ă£ŜʰŲЯӍϵʆȌ˓ɒƠďǤοϔƅ˫ϽάъӃӹΏ=ҝÍ§ˆ',
                                                                            'ϿɎɰĴԚʱ\u0379đŒ§ČÊҩɆ˥ΓɬѲµłȷХԒлƛȯŷѳǪŽ',
                                                                            'ˋ·ɶŌƃƧŎįƪɷʱĨѤɝ˩Ȕ\x90ѷǎѕʑѓ~ӆΜ\x80Ƶǽ|}',
                                                                            'ϗϥѯɹ+ӰɪǓ"ȫҞʍг҇ǐșȒ/Ӄɔ҅ɱɢȼԛǓг6Łʌ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϸώǼЂěӅſɗ\u03a2(ƜԍɴѮsѝàϑΎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4532293327192925062,
                                                    },
                                    },
                            {
                                        'name': 'mρŇԃʯÛw˃ԆԒʅȦ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
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
                        ],
                },
                {
                    'catalog': 'Џƾ\x9cɆӌίǴɜ?Ϊɿwӧľĭ˒Ċύ½ɲ{ԙ:ƚ\x93˳ЖǹϠǅ',
                    'message': '˯=ʄőĸŗȮԂǋʺĳØʚͿăɦEʲ±²\xad΄˕űϕɯzΣδǨ',
                    'arguments': [
                            {
                                        'name': 'Ģѵ-˾\u0378ԜȿșǣӧlсP\x87ΒӨƥөƜȥʆιʞӌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'þӬӥ¢ѥҮÃɒтͿЇҁϛҨԜ¬ČϒȲĉǔôϳƚҥUԣѦΦш',
                                                                            'љƎȕXǔ˯ʺϓɞɭOԒ"˕\x8dʡ҇\x9fɌжėˎΌÌʭѰжϡȇԏ',
                                                                            'ѡ\x81ɊȜϝ6\u0383ʣӐɥǚΆΆȯїǌњɄTҋΉˠυңĝƦτԞȳϡ',
                                                                            'ãʆe΄ϲŗåƈɑɭѲϩɪԋҴˍ\x8c\x90ҨЂʶɡ˽ƥҞ\x9cǄюЋÌ',
                                                                            '(ą\x92ŒѦԚѷÇȖԬηĐζѼʗʧʿͻæӶҿҼʌˋԚȈŀǩǨӋ',
                                                                            '\u0382Ӱ΅ҤƌøĘюΉőЙ˅ћưʉğ»ȍ\x85Ϟ͵ǯӧϮƊNʶԓжѝ',
                                                                            'νįȵəAƙʱђƘʛі˩˳ƥΰɄƖC҇Ҧӈè¯ʡÎŕΘҭђΧ',
                                                                            'ȚǒʊɄȬƷǕ5ԆҴWȌΌ-ѷťθɐơfǓ¿ɋѣǌνɆȿͷѢ',
                                                                            '²ϖÍϋȊģǽ\x99ΘTίҤ9Ԛ4ˊĒ˧Ё\x84ѻђӦӟѝʡWMԘ>',
                                                                            '˽ΪԫҦľϯɠœΘҟȝӛȃżф˺˧ƚ\u0381ǯɎЈʽщ½ȕˣԅǂΜ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƭŉΐɁġʹΨĎԅҗϨ\x9bȷӦʷҌ҂ȭǱ\x9fɇ³ƗȦʌԠҭƪżϱ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175536.431989:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˇóҤрǀʢɷԏͱȶŽďŖƕƷǉˠŁnѺѺҍʟ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            621043.1324830013,
                                                                            674901.0657790361,
                                                                            404038.14078967454,
                                                                            -27401.021191059,
                                                                            158448.40758013562,
                                                                            694623.8406289428,
                                                                            797228.2463206314,
                                                                            788831.2590445715,
                                                                            17005.774320165,
                                                                            929021.290522467,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ѣʤòğβ'ВԥЀ",
                                        'value': {
                                                        '^': 'string',
                                                        '$': ',ƨɒȄ.tȶȞŬǣʴƧʶѪµƔƬɟ\x8cϯҮ΄ĽѽŇгƉѰΞŘ',
                                                    },
                                    },
                            {
                                        'name': 'ҙӖЯЎ˹ӣƢĊ˵\x9b=N΅Ɯ\u0379ǥӍǞ˪ѣɩǪŵ\u0381',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2704524844774575536,
                                                                            2233874145289374425,
                                                                            -2068005536037893143,
                                                                            -68714953647863503,
                                                                            1264843434234267299,
                                                                            -4082636929061965918,
                                                                            4088992792830870571,
                                                                            7361675968224392020,
                                                                            -3698742432293179680,
                                                                            -3571339736924044022,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˩ѓ\u0383ɵшʝ¡Ԗ/ɍÛПȆҥїȷɴɻɃδɖԐϝÐŖӔŵ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x96ÕΚξгҖѳȊҿәх¬ʦˬѾ§ŭԐѐɸſƤŵʆǘϔЏbΪΠ',
                                                    },
                                    },
                            {
                                        'name': 'ΔΏĔӳ~±ȚƛŒĠˣΏMȠԣ\u0382\u0383˴Шҡ҂ηπȔӥƩԉǎҴˤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8069727697939415159,
                                                                            -1592124512458896882,
                                                                            -3077305265660748607,
                                                                            231607862301831489,
                                                                            -4536341528349529573,
                                                                            8189071326354424427,
                                                                            994405364846901957,
                                                                            7841472668936864000,
                                                                            382715058826371970,
                                                                            -7083806588490473622,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '±ϢіƴЉª',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -9200085315256440552,
                                                    },
                                    },
                            {
                                        'name': 'ǯBӬԏ˹ҽõѩ˽ʬɵjπԧӉ·˦Ӑ˹я<ϖȃáԓŴċȣЅ*',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '͵ʬ\x96øȰһѓÀ˰AǵВӠʫΏȍŠώǃŋΗĢ˙ĭξ˻ȉɶșӅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƓĪЮÖΉ#Ą˴ǤΑɿĬǐ0ϾѠΧȿƻłԖӳҤчʥȶÏħ˳ζ',
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

            'identifier': 'Θ-m˚л',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'ҏW',
                    'message': 'Ӟ',
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
            'name': '˃ƋȒ@μʍѢǁTǏԈĞǓ~ȪǐҁİԣȪΪиʐӉЏӢːʝǈʝ',
            'error': {
                'identifier': '˻ʙǻӿƞɃɕ˥îΐȍѥӰӵɋɇ5ÈɷЉήБɤƿžе³ǢЮª',
                'categories': [
                    'invalid-user-action',
                    'network',
                    'access-restriction',
                    'os',
                    'os',
                    'os',
                    'file',
                    'file',
                    'internal',
                    'configuration',
                ],
                'source': "οԬѝʺː'ήϡȪЊ˰\x97å]ҵɵԟǬÎԫԧʐѾԤ0\x8bVԛʄŊ",
                'messages': [
                    {
                            'catalog': 'ЫʭӨȐ9´ʎőģŷҌЉƚѬÿɲӡęȍÊâԮĦӿqŴΎſʖϯ',
                            'message': 'ԑK˴ƚǏӳřѩӷ˚фćŠЮ\x8bx$°ύvÿyϢ9ЀÎǧ½Į;',
                            'arguments': [
                                        {
                                                        'name': 'ʎƃŒͷҧϽY>ʀ\x84˭}ɵ\x90ĨÁĠԧӥΨý',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'şпѐҋқĤƗɜˈӌ°ȤҸñϱҍǀ\x8fʞů\u0378āљEӰǠȕʨʶ*',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȳɵǕȂҜӑƺFҥ4ûŏƵġӇăԨƃѥȶēԬόҞ\x9aϠķˤƻ˯',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x84ʲǌˢŤҷĂҒϡЗƁȈλΏɴȳǨʖ\x9c\x90ϗ\xadǂ\x82ƶˉłԎѿɬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӂȾǒѷӣ.ϬԝƟҩʓ*ȚǂԛϰЭŗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 354017.2857634251,
                                                                        },
                                                    },
                                        {
                                                        'name': '{ȺΟʾů',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8344610777432899072,
                                                                        },
                                                    },
                                        {
                                                        'name': '˧юҾĆƾЫԄǮɊČāӠA',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 329667.8080489022,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ķɒ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȜԟӍƙ,γcãǅʿþіҵҊȃ\x86ό',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'CҁнƘƘȸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 729881.812163409,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'οǡ˶ƟѫʚЯѢŤĺФәҮЃѕ3ˉϴŮnŜ\x95ĳÓ=Ȩ˜ʌʱo',
                            'message': 'ʠȑѼŅƐҌ×ƫǓԟϩǂǕΠ8ü˖ϠâοǖȎ˵ͼƮҐīЛɡѺ',
                            'arguments': [
                                        {
                                                        'name': 'ӞѴƷŜԤΐѺНӌŁl҇»·Ӑе\u0380ςǩʖȞӤЪƥȇ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'yǦ¼ɝϹĪʓԃϑ\xa0ϊŸБʱϕ(ʇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˏĳȶӥ\x9cʶї˫Ԩȋ˖ÿѬʳǯɪʬÿɘɐҖόɗӉˏÛϩ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǒʇπŶĘЊӆлљӣ҂ƓЀЗʔρў˘һĨМŚɔÀɊҊ\x84ΈËϮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '«ĆΠɨöӥγԄԈåѻ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¹ӶˡȪϯΓӝʊƨəϸi˛˒ѵnѫļΰȮőǬыƦԜхPȷҥɖ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѓƦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˍШȳŔ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 781693.4391616664,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x83ůŇʄưϙMђџȟԈƜȜӎÑǥѵǪɿАҖνƣ˨JԩӨ\x92I`',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '?ұʤΒȢКːáНғ\u038dVҷҤ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ӻѝį\u0382ʡӦ\x81ȶԍÍʢҹ\x84ÝàЬѣ\x9fʻĪʱƓĸӑЏžϞ˫ũΤ',
                            'message': ';\x93ɢЃǂĜӢȀŨԃʿ˘ȮΝӞĞɑʶҷƎАÿ¸ӢϰĄѣԌѵϚ',
                            'arguments': [
                                        {
                                                        'name': 'Ĭː<ɩРж',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɳǦѮΒzȢʊǷǮδϽ˾ӟsǐѬХɋ.˚Ҏ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -32362.492428701196,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Άˋɷъӯɒźʡ˲ŹČ˅Ȳ¦åџƗҩҢŲЗóƼ°ʘ˽ȷɐÑ\x91',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ФϘѿ˾ɲĺ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǉɯУƑ˯АαǵÜˈȮʡˈ˃ɳϰȼƦҐϼӤȭҽÎϳњRʍȱï',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŶѽãɇʮÑɼҌȖЙӍȓˮеˡϏ\x88ˊş÷бӣȑҢʥɑЌҜžʻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 513628311381618480,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԁťȒќĩǷɑɍƷʨŭɃŷǛˊ҆ŶƹʖһȿŨΈȐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '#ÚɃԧMˉɋщ\u0378.ф0ЙˑН˂/ԙwъ\x98ȽðϹԠβґӧɸӈ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǜеʅÔӽѧԁĊͺΉʆКpѾҿϧШwԥJзʶCąй',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѦȜЉΑԖúʺʻӕҽ˧ŉ¨',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175536.394727:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Μɋ3˔Яɗœ;˹ϳt\xadͽť˕їΦДǐԎēԖҒпù:Șҿʘǂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʥĭʲΝ҃QǺƇęȠƮʅԅҐðöǝˡ®ŇΆχτ_\x92ьΧχВƶ',
                            'message': '˥ɰΆɈΓ±Ҕ\x95/ȈӂtɧҵѳϭĜ\x84ӰнҍʋуӳɜӼҀőƞɽ',
                            'arguments': [
                                        {
                                                        'name': 'ˠʒ0×ΎЧ˹Ԃ5ԬǃŭŗϿ˸¸\x8eƓȁĠȮ˲ǡЅĥŤĿ\x84ѰҶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175536.395933:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Χҗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѹ¨ОȠЀȂŖÏÑϤ˪ѽǧʺ§ѓλĥǪҟɶԁЁυǘɔʈ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͻ˾ϛқɋǜˍЮ·ҀфǞτѾǣѐүŰԐƅΨӑӫ\x83$Hiȕνѱ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -366100273753366123,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9fΕӫé\x97үΣϕәˠЫӶ¼å¾ӑȓԔӸČĶ5ԆĊԫɷϣħʿǹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175536.396551:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҲԎãɀ\x9aĴȑƇƴӳңЧʟʣʤ\x9aɽʳҋƊſȔ[ζΧƨƮηЋк',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175536.396703:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˭ԡ¿ïɍŧΛҿϲҨӌɑŘǅҪƕϪ(ğ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ó~ĽǂťԅЩþƽͶĬϠƪÎȡȼњ¾˼ʁɲǇţğѰӕƇÊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'gΠəұǹјň΅˽\x98ɉБΉϛťâ΄ņʶ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1458346465974948635,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӂċфƼɻʇʢț\u03a2QҖӽêΨʴ\u0378АȋˤӭæМӒʕӢˌ˦ђďǭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȼƅǓ˔ǡхԁw¨ԅƂќĄҤ',
                            'message': 'ĦԞёǼǗ˴ʜљϦӟʏˑρɥҞ_ԌȴιĦ.ǬȰɸѶӆĥÚʄӵ',
                            'arguments': [
                                        {
                                                        'name': 'ϖˈŊ˹ӧČΗσÃ¯2ƽ±ΓƟúƨǏχŴȶmƵҭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'РΎųжʉŋӷМΦì',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2265488255155088699,
                                                                        },
                                                    },
                                        {
                                                        'name': 'җΚǱΔϋʑ˳Óµ҆űÖŵ\x8b!ʷğáѼǳĳŌȂ®ӌΚȠΓǦϓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¥пҦǝϧŀΙӬͳЈЅјѫѦȫĝǣĸ\x99ξϦʪĵĕʚ\x82ΣǱѷŹ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϜΟðǢ±ҭûȉәѢҖʞ/ϛӻÑίɇˆɌcƐхþǒsԤƷΊɼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175536.398540:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽÜ˭',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 714716.9174104888,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϘʮψǑҰÓʕĿ:˭0ȿӦң1Ο\x9aԑ˞Ź\u038bƔҭʰ\x9dӵҡӺgӡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175536.398824:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝ ʍҳ\x95ώʹԍƫƕɦғ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '5ǬƫʪɰƢÐӠζЂ¥ƀʛƚӳҬξмѼǕ$țdЏ>ŅʏPԥ¹',
                            'message': 'й˪ΙǖɵèѺ!ϭσu$ґ\x98ш¨ѲǍѤ\x80ήȊτђŭ҆qˌσ\x81',
                            'arguments': [
                                        {
                                                        'name': 'н»ʕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȭRȠ˅',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'įˆ_',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЯǕЃϳʟJ҅ɽȮϹгƐӆϥɺӜԁʓQӦÁƷŬđvͷƿί%Ɣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8592385078920370613,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƭѸȃҊ˭',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1931891753466651630,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԄӶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'įǇ\xa0˯зΒɤǻ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҊЏӽʃһ\x8cƶԈɘ҂ǪԎƒȝϻŁCȘJȎĩ҇αԂƖOѴǠĀӉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -689671013859051496,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҿҪƞĩŷðԤ¼Ţ¦Ŏ\x8fǏÜÃȤȯǃżǝȋÆϷɛ\x8eа',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ҋ˩æΎǗīɕʙƿԓΠҤūҖӥɣǓѷӺšȕʏ\x825ӽιʲɗӏЍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЁōƫʕĈƒƖͼ°ͱЁƕ˓ĩɅӼҊԁҢίƣəɺКΆʍǶŽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'åķρr¥ɚ6ҋŇHˢϝżƿ\u0378ӡϋћϻˉñохĽƈȬΙ˗\xadĞ',
                            'message': 'ʫΚΚʲ¨ґș\x84ŏ\u0379ԉĪ\x92ӣ¶ÙӹҢã\x92ɹθŭеvʪȦУǡͳ',
                            'arguments': [
                                        {
                                                        'name': 'àυӏʫēЛΉѨԛɖďÝѳÒǹɋӲɊўϽ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'і\xa0Жɼĳϛ;ưʭƊҠϓ4ʺ#ˆїɛҴҪƅЉɲēԢ³ϏȼϴȄ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĠΖÅňϤʣƬWϟǫӉʯʥӆјђǓʨ҈\x9cʜϑΛЖƁȥȵчɎ҂',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҟЀӝц˅ɿ²ЂӱҖΚҘӰҍȗsͺӝƞϋҟ˪ʷ7ÒȇϜČӬá',
                                                                        },
                                                    },
                                        {
                                                        'name': 'cΖsӭюŰǲҘǊƲ˜ǜʉ\x92ƒ\\ЕЍɻĜńˉҙǮȔԕɁʽʕӎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŌoÿƂtίԜʻɩ˔ǐµΡǠІ¨ĈƹΖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '(ԭſœә҉ͺоƦŰ˘\x9dԔěŻÉэ˵ϯƶъѹPΫĀŗΰ\x97ʦĂ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӋЦ\x92¬\\ɾ³дʸʔŰЭóĎŒŮѳ˖ԭԇӷʋ\x9dӱȢӼϣńȟҏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖӡːώŘҎԠȽΜ\xa0ΉȍʷѷЋϬȨÊÞǄҥˢŠѸӽĕˣ¦лǎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6170704441635498817,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҋϒɦ҆тгȂ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǽƊż',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʹɎǦȟʡɃƞЊWķѴ˛ĀȱЀɠ.еͲϻӗɠҟҤŠѥDȇżĞ',
                            'message': 'ȕɜ\\ҮӼӧҳĽ?ŌϺÜųŷ]ĉ^ɲ@ğıȳ˧ӮЫžҙȐӥǣ',
                            'arguments': [
                                        {
                                                        'name': 'ЃɝŊλϩҖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175536.403455:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥŸϒŴ"ΉɁЀǎѧΫǟӃνĬq˖ǺĢɋħěӳćΕ˭Űȷυϰ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʍӶôɏ˰ϐЬӬйōӝĐԎǰ\x8eӺɊЄǢl·ѺөǂČê¾ЦҞ7',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'VєűУơǆǱȋ˩ǚæǥҲΠг',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '"ßЈšɟАŧӣÂŷӈ\x9bɿC&_ɻщ\x9dғΛʮӲǭѩɧѡϵĪL',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǘɵŃԙ\x91ʮ@ςĚáų˺\x80·ɱӊƊʊåɰāɿѩжҝóš\x95Ƥī',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175536.404132:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Å·ӉςŇ&ǚүǁǥ\x87ýȇŐ҂ʰ˩ɧ4ƍԄ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8007609915849900392,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x7fҾɞÇfÕơƏϹёЌђԡÉԂɎĚΜΰ¹ϤшʫԓˈυѦǂѭ\x8a',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӒģχΔҢҁAǱàůŗъгӔҋ˨Ͻ˹ǭӽł҉űſʀǁ˴ĝԔά',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ǵ\x89ќʼ÷ѲʌŴˋѪş˳kƭϢʏϒˁƷǳȁΫʫӶӒ˲ɲҀϾł',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǎGǽDǎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4980333410283809900,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɗΜʨƘʓʎǠ¢ÑΓÇƚͱУЬːȆˣ\x974ȾȨѰӈȳƛдuƚǦ',
                                                        'value': {
                                                                            '^': 'float_list',
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

            'name': 'ːьӟ',

            'error': {
                'identifier': 'ϫÏʴϝӁ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ãӛ',
                            'message': 'ſ',
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
            'event_id': 'ΟÒзϰǶƣѯŋśԋɥЏѦÅXíӟʉûɁџ˩cÏƾͼʔ˙Ǿԥ',
            'target_id': 'Ǎ˦\x87ƉƗȊȓ҃ӽĹϮh\x84ǉ˭ϋӕɒŽǤǁͰԈɋŘЋ΄ιяø',
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
                    'event_id': 'ΗϤÜІ2ŻϟϚʣɘe>\x94£ӟāĈЫΪύЁɨǦҖʥđ˾іϔџ',
                    'target_id': 'ΈŜҞTпÎˤÞҍң{О',
                },
                {
                    'event_id': '@îӾĢӉĘɧӖʅ˰ĻŝԮюc4AɑýԓӑлEԢ`ЈXϣŰѝ',
                    'target_id': 'ȯɼL_˴è˱ɲўΏҖӟ4]ýāҿͳƕΟѡ°āҭƁӌӪȱѬ"',
                },
                {
                    'event_id': 'Ӧӹť\x9eƨǱρŷϢҲŇЦƊȵџѤ˚¯˨ИȼӍĮΫʴʞǜİԎӞ',
                    'target_id': 'ɷdŗƣȄȀVȞNϙѨȽΈϮƢœЯɐӎт҂чʚsYҾé\x9aȭO',
                },
                {
                    'event_id': 'ЅĢʸƿʉȓϙƈҶҢȸ˃ĳЉϖӿӤŽ\x8fӺμˏԋѼО\x97ū˴эѰ',
                    'target_id': 'ň\x9c5&ɨɜ҂\x86ӋΡöəȿɻɴ˔˶ʵȍšýyʇÇɳЗżұ\u0383Ӑ',
                },
                {
                    'event_id': 'ŎҲоП˵ôƐĿ΄Ϫ>ҧӌαșÀĦҿżqAӌӱŞȜӓӁûлг',
                    'target_id': 'ˍиưoňΜŲʓϔԎƌZ˯ͻϹҸşȱѡӵƐǡάŝʲŋȉΈȔŁ',
                },
                {
                    'event_id': '>ƙǭǨȟјuȋҨȷҩӴ&ÆÚϴƔǠľʱ\x80ДΖԄѼ0ž¬Ƭ˔',
                    'target_id': 'ĢşӽюХǷВǤӑɜЦџɲҲǇĸŗÞԞЃΙZХȱą#ŶӤʑŶ',
                },
                {
                    'event_id': 'ыǆ\x9fԘˊ\x98əϒʹ(<ȵ΄Ә°φțɲҢΈФɼԭĄҭӗǏӐЅ\x98',
                    'target_id': 'øԛғΐʺԅѷӁӃØήʻːHӋȭΪӍœ\u0381ȼӘϟĤ§ҭƳ\x7fĵɴ',
                },
                {
                    'event_id': 'ϡɇżβФĔ',
                    'target_id': '¹ĘƦΥ˓ƠԇѨу\u0383ïМͿыѦƹsοȵǇѫô˂ƝnïĽȤϑʤ',
                },
                {
                    'event_id': 'xänʦǴɦŖȭҨκɥlЏαѲԋȎɎÅđїӡϰʗƱϾтϯǿĸ',
                    'target_id': 'ԋƹδʓЭƙΖ\u0381҅ͳĪЇÕ˃ģǗȮȇɲȅ΅ɠMȲȵΙ`ӼŴԨ',
                },
                {
                    'event_id': 'τ_ӱØƌȲ;δ˩ӐʼȰȡƼh˒ʂуÄ&ŕΆҘѰ|ăҵA\x92ѭ',
                    'target_id': 'Ӻ\u038bϚˋѡȣӈŵЉƽ',
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
                    'event_id': 'ӁɡПqвĭyƊɟ\x8cɌ7ϔƻυǊ˓ŜԨʿӢǕИҮȩġƪƫɜԀ',
                    'target_id': "ȱΆɒ\x97ͷƛ˟Ҵ¥ӏԜŲґŁưǘōȅӋÆ'îȦ²ȥѪУǲ\u0379ϩ",
                },
                {
                    'event_id': 'ԇϦʎŇɹА˥ϿƺČӲÿϧȈ˵đŧМȄцņPî҈ťǏ¯ϝ\x87˙',
                    'target_id': 'ԗǭÇхŤԏuğäΤʆ҅ɁÛûӓɱz[ţƉŨêkÆǀϩ\x92ҹ˰',
                },
                {
                    'event_id': 'ψλɕƑ^ͼчŜЌĮõҲϗӵǨĽҠԊё\x96\x8bıßĿιƍPȓµŻ',
                    'target_id': 'ϋ҅ÞӸϘ>ѩsϝƈÂȾҐ.@РǗżЏκҹҺĜũʦ\x9dʜԏʾƽ',
                },
                {
                    'event_id': 'zĨ2ϨɂЋϴˋɭёϘͷĮ$ΫҐӽŐӃҏα҇ϿŮƷμѤɂgǥ',
                    'target_id': 'БԍύϰЯ°ͷӹƈƅƴʃҵ½ĳŠԬΧѶ˜Ф<¤ŹʒʁĵΚǓӉ',
                },
                {
                    'event_id': 'ΪŗχëɯF¸ӛȳǁԙɂZ҈ȏ˂çɑàʅĒÛҼȃ˲\x9a§˫Ӻ\u0381',
                    'target_id': 'ӡĠҼƥ®ÎѸî˟˞фγ\x7fĭkćУƳǩқЙǱʙŀҗӚäÃNǵ',
                },
                {
                    'event_id': 'АΘȆΝ~ʤƖ-˥ҝʏѝʶƲ\x9aԛȥƞW˫˥йğ9λǷϖϼ˰\x8e',
                    'target_id': '\x94Ԑĺɣώ¾ЯѰƛҾǭПҗɬˁώĽCШŏНŴʄέ²ίѵŅǕő',
                },
                {
                    'event_id': 'ԚM\x93ӂûģǿĦƾЁĪˆ·!LűɩìЦŝǴƂČƥʍʏωË5l',
                    'target_id': 'ȵ\u0382ʝɖӻǵȴϸѧͺƱƸɱӭƂEʧζͽԦѶǉCӀӡéżѐƍĜ',
                },
                {
                    'event_id': 'ӸsӝҰƊӮΉʹϠȓʸԋʐ6ƩçʕɪЎ˷ϑφçКҽԣӪԍ!ç',
                    'target_id': '¿ʾŬɛϊӐϤ˕Ȩ˚ҕťÞȪɓсГǄɽǪϜҎŕãɕЪѹɹŅҲ',
                },
                {
                    'event_id': 'ʋǇǎƯĠ~ѐξǠԉůϓ×ǳӭɾMƏą˃˶^ҫ\x82Јȴŉʴӷӛ',
                    'target_id': 'Ϗɣʣk2Й\x81ÁȐӱ΄',
                },
                {
                    'event_id': 'ͻɪ\x86ˮЛǻЬӊСĄ0ƿȘɪ¸ˁ¯ɼ\x9fǅΊ\u0380ɜ˔ӅʼΘҬ*ѷ',
                    'target_id': 'ӫ϶ӎŬмǌ2Йpʋԡ҄ȗҥɫY©ӒѶҔ;ԨҊƶĩʗӣкԢĉ',
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
