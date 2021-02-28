# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-28T02:46:04.357333+00:00

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
                '˻ӟӽΜӠϾ˕ûƶѕѽÌҀԍƈǟ˭Ɖ¢í\x9eMʋōǳϊMΖҔҎ',
                'ҳȻφϰƷʀǐǇθÀPλӲƙȼ\x7fѐƚҘҶ˧ηқčǫkħұ˓Ϭ',
                'ʐhȯĜżԇŉɽőЉćÅѱsȽȶˍȨҶʻәʩϋŢǡ˽бҟͺȕ',
                ':˩Ȑԇɤϰ"΄ğĐƪЊαӤİΚAΨ3ŠȑǞĞӲДƸʆ$ͳӮ',
                "ЧvǆЭϗҟÉӮЭơ'șżƭ^ÎƌͱҙһʲԦѓ'ɏҟȞǾżġ",
                'ά˴ӕԒѳχί-ԋЈɪłéɬϒ¦ĉҾΗӂşтѼ 3ȆҮёɞ˗',
                'ˍôԇΤͷЄ˶еԗΌĉŌˠӷʴіɫ҅ȒҠș˳ʚӋȩɔ˘\x7fӉư',
                'ɎƈҭKźчмѦ¾īψʮȴćĽ҂ҕıЁώϔƦ\x82ԉΑĒǯԊ˭ʰ',
                'eªǫϾżĺ\u0383Ϣ˥ŗԋԖúҿУĩƃȹǐѹԅǩƐϨԑĂˠѨ¶Ґ',
                'ԞԡɊƚƟɧʠǔШɩ³Г|¯ТˤҷӭǖɃȳūˡǕЇŠƈѸïã',
            ],
            'source_id_prefixes': [
                'ƍMѢɄʢΣĭŻƤϏ·Ïəъρʍɻĺ`ԤЇѹШƏҵѕΜГ˔Ԟ',
                'ɘџƼÆÓȮʡӣ\u0380½Ҧƥ*ǟѹИSӼÜИԒΖ˺ъԘȢ˒˕\x99Ӥ',
                'ӆ¸ʇȥЭϐğe¼ƷҏӵĔ΄ŢΗȅΤ\x86çΪƪӅp}ΖȅӥǾʩ',
                'ƌТӢϩԅJх"¿њvɯӈάſæs÷\xadʄɡϏŰɊǳG¾Ȭкξ',
                'Ѐ˦˟jЈ\u0381Øϒɰ!ǩʒҴӄŦǻƽό\u0378ġѨԌŏΗԞ˖ǺŪƀǿ',
                't\x86ϾĒʥ\u0380҃ȭΑĀ\xa0ˑǋέ˭¿җɚÄÒƐĸŤίűВοʙӆʛ',
                'Нј҉ύѸӡǠ\x9eӪĿ\x8aЧĢĜΧŶМӾʐФˏžØǖɀԃƗԠſϽ',
                'ӮȟѣʭjԂˏƂύʄʮԃҏѸюȵˮǿņͱ#ӵӵ7²ĉ˾ƽZĩ',
                'ǡЖ°ưтʌʖШ\x9cˬʊӀӖʹʼІÈŧí$΄ҭȄɩǍϮʎҘ\u038dĨ',
                'ŜʆòȕʚhŽĚԐñϲSšŗϽÁɅÈÉ\x84Ԉ,ӏ҂њ?ΜɿƱӫ',
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
            'action': 'ǔΗД˸ӧʶԬǼӅĦϩҝƉԮОτ(ϋωӇϗŢ]iėĠƠǄѸŨ',
            'resources': [
                'ɴ0РԙӰˤʰҠ¡Цҭ˞ʖϊЩ¡϶ζˡ\x83ιß҆^čӔϸ¿ýӵ',
                'a7ɥӍ˫ο\x8bȪħӀʚѸҒщǯʋʨϸôѯͺĴð˕ƧтЩȴЁ҂',
                'ŎƯëҙɝftȦƐȱϋɆɐйβȪԂӓƘʡȈ\x97ɟ˟ɳѝӶͻĩ\x8c',
                'ǤӖθó˂ԅÚϷɿԗжdȋ%ºӺ!ǳІÏӎͻÈĤȝBËN0ǂ',
                'Ԃ˧ǪΨŃD`ЅωFӳȕͰʹɯ϶όщŗɮӨɯϹƴȢ·ǈӁЀ\u0380',
                'ȍBȵғ-ѮǬͷ\x87ҁӎďʷӧ΅ԓҶȓʔɼgýǸǅӰˤϙʑķw',
                'ӍϸơΔДӒȝ"]ħҸͼɜǅưɵԘ(žƄ˕ғϤȫΨǆˋ\x9aʿΧ',
                '¬ȍʝіǠΒĦԂԘɫɜũ®\x8aɸŴӱХåƙ˪ӷІĻ\u0382ҪӂӉѥļ',
                'ò϶ʏ\x83ғƓĝƄŰƂǰψːҪ£ģ˧¦ôԋ:дż+˼ϖʉ˘оΘ',
                'Ԟó˸ʢ˂ǩĶȔϤMҙĺ҃ÿˆԐƘ#/ɡԁÔ6ɵЍҀJχĹξ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ӕ',

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
            'name': 'ӳҫƐȬʨǫʰƏФʣѷӎ˼т¶ǁτϑˌƄǰˡƖƷȜ¼ƾßħҦ',
            'version': [
                -4527410859145603164,
                -9115482064116141421,
                -7592911798439313057,
            ],
            'location': [
                'ǂӢ©ͰζƸƊƮǨμʑĖԭŉ˻ҹӱӯŵŗɱзүƣӀ¿Ӌ҆\x9aӌ',
                '\x9bѢӋʶϱϓӭοȤo\x8cʹ¨ƩцìԤԉÜƦͳϾÀȕǝLɀИϲԛ',
                'ɺʃųΐǧɍ´ӗǫBӡ˚жƈȨҩԎÎԩҸҝƣʙǄν+уʄ˲Ԣ',
                'ɩͻ_ƙżϜǫɋʭǭëƱư_ǀǒ˂ЬkɩĻɆ˔:Wɕ˘жʜ\x8d',
                'Ź˨Ƙ±>ΎˉɃǱҩѷӆёЁЀϦНӵԪϦăʂʚŀ˫ήfҡģɐ',
                'OɠĘɵӳɬŭȪŕѭԠȻďɇΊƈ˭ң÷ȡ£ҔĳɐʡǅҖƒǯĄ',
                'ʙ˟ΙӫϹƨTńԞǄ˶ДӢΗʺϾİŖĭ4¼\x89gÙˡ\x8aЊҐӊϴ',
                'XӰԬǛƸƨӊΜԈ\x9aŊĻϺѐԄșҺʊ˩џԌȆʤɬұrфłϯ×',
                'ϭ˯\x8fR\u0378͵ʔˏɍʡZ¢ˏʊ%ϷӚɹϰȸ&˷DǏDѭεВѭɑ',
                'ļƂӿ¯ίˈħдɘĄȷÍ˘ΰІԪжԨɧ˪κ˟\x9ațοԝϪǮӑɵ',
            ],
            'runtime': 'ӋɒǯʍӼӄʌ˴ʶeԓ˻ȬҘż£ҵıƫ7ZôһËиκҶѶԣn',
            'send_access': {
                'event_ids': [
                    'әщɖ:ğĥэфƊſѱΐǔÙǮűʛЂжϥ˝ùԣtОȴґʭŔǐ',
                    'ɴԜīҫ\x8dϿѴƐ',
                    'Ξº˰ϋŒƿƩ\x9e˟ϥȺϢǒ',
                    'ȪĸБҹÑӄцЎԬѵѣg˓Їԡ¡˒ǀǺЛëҍԅŽІƠ˒џɞʺ',
                    'ʆѯҒôɫԈYΔ˝΅˽ǃ\x84ҴЯΰлǢˏѦ<ҢČǵЎ ǐūŴ®',
                    'ͻǚҔĈƂŧȷE˖ȒǏξŨŊ¦өüЍΐӇ\x90ǃψѦŐ\x81ϨÿƝſ',
                    'Ǔ$ԖӪ:ӂЊƒǵϘÏȮʛĂ*ѴҿЕӑҩβčgŢɢŽԅӀʹĭ',
                    'ĪФθá5ѳȅ\x9dԄҟ\x90ƓHɇhџƛHĀɺ˄ϟҐӢɯÈҪҍҲΒ',
                    'с"ʤΈǴѷлі˻ĸ˧ӘīȞƼǼǸѷчáȜ҇ʻʛ3ҰʑʎКȡ',
                    'Ìѐ¡ɘīɚҺ¯\u0383ĘÞɭӹϥ¬іĸȆˣiεŪĊɃȐ@ғаR˴',
                ],
                'source_id_prefixes': [
                    'řÒΐǌϩȞȫ҂˺ЬψϟùmɸҿȞʙͺʁɨЬԐ\x80ҐȣUсѲȑ',
                    '˂˚ӰÙ(#²ԘJʦ\x8aʞˀ}ЫҦǳˎʔшŷлхĘ;ŠƲ·ƎƤ',
                    'rϪ\x8aϗˆȏ\u0383¤ʳ˜óИюǗ*һĘϭϚǐȒҼƷǜLϽԭсϐӂ',
                    '~ˇ˗λ΄ĖĮӻҪӥԂɜīўŵпӇÞŔÓ',
                    'Ͳ9˅˟¨ʛmˈʳζŽǯѡˢϚνԩƷCʫ˱ƄȘӧвϒѶȭԘĵ',
                    'āϙˁ\x98ͻԛäɳĵˈˏ\x9cԁУĐȟοɩ«ΥҞȜɓƖȣ\x8aı¶ŏȦ',
                    'ΎͶǭϸӉŚшʎĆǰÿӍͽϲɜŐȐ˒ȞʶЉϫ¾ϰȓĬ˷Ǣˀɑ',
                    'ˀƏ!ˊҮӪ˪ʨˊ˛šȪҖeϑƑƵŬwЧАԨϪȖňҍzҔλ\x87',
                    'ɜƐΘĝϲҎ\xa0ϮȶȮɇĸƄƍғÊDѫѥӢȌчҴƌǞaЌύǣǴ',
                    '*~ρǶƠӬˤ\x9c½ĒéȶӮɌӿC˺ŉȝbцΨώ\u03a2νӶҽӏ\x92q',
                ],
            },
            'configuration': 'ĽͶѤѵɈɴ҈ϤbӑʹӲǄöҗ%I\x81Ĺ˪ɛΥŴѮξ¹ý˺Ʒå',
            'permissions': [
                {
                    'action': 'ԏãӕɷгǡ˫҅ѰӰśӛȋàƩԟΤƍγӛƇǏͱΐϚɿ8ΤҔǧ',
                    'resources': [
                            'ЪԪģɘѡԀÄgȣĻ%ϦҭʞʸČĺƴɐđҩƺєϿȓǳәɵ\xa0ӝ',
                            'ЊɭϼʘеЯĠʋ\x85ňǼƚƇ{Ǜˋ˦²ȫӺʨΎΔЬ\x94}ьʌYΛ',
                            'Èǝɔȷ_·ωƟƦȑ\x8fȭǢħyǝςˋˮϳĕӞÍӜʮVřЙȀҡ',
                            'ЃMїȌƅґԩєȳʓҥQѰzʨ\x90ӵɪҲƄȈˊѰҩƮνѾ˳ʢʄ',
                            'а6ƒʥĭǊùΦȩɾТUґQöËƣоҖϻʻSňǖθϳǊĀҥϖ',
                            'ήȎϕ˼ϪΛ\x87@˳SЄũÚƘřʟˏϤϜϯʩGԏƨԡŜ\x85ȰҼÖ',
                            'ξďСΉˣӧhӚzԝûΣíýԦ\x81Ɩ¨ƴԓ-µοèǕџљӤØτ',
                            '˽щŹʍ\x85ӼĦƬǖȂŶČПѳȁȈʓȄҘǅ[ÝԛVɱʧ˱²Ԃɛ',
                            'ϱȱȬˀ\x95ÒX\x91ʫΏĽҨĕɢУЅŅʹˀ˽˂ǣlʌҹʙŜƊǇѿ',
                            '@үєИǂƊҩĆʨʍʪȍɀ\x9cЃϒ;ϽwļԞҴƑ\x81фʇԡpdϒ',
                        ],
                },
                {
                    'action': '~ȘǄзҬӂϩ÷7њ˟ɼϗ¢ƹǝʯƃҺʦ¸\x91ЧϡӈԨȜΒĬŇ',
                    'resources': [
                            "ʕ3ʪwԛήҏσŲǧџIȜǅbѬƌ\u038děmÄ$ȪΞӉȩЂ'ėѬ",
                            '˝ԐþӄöfƪӎӎӵүȈɏңǔŕ×ѫəʆʦÿҋȲԣǺƮИԏѱ',
                            'ŹθĤuÏÚơˬɖщ4ʗçͱΦ\x92ӡӞΣw\x81ҕѡɻľĜҸӷ˯Ӷ',
                            '˛ŧȒϔμΛӟʹFҙұϱʠɃӽćoԣǋƺΙѹɋǛӊθˏƎәǱ',
                            'ñТ˯ƋӊќϠŖGȨŻ\x9dΑˈк*ͱpӿςΆɝ\u03a2Ě˹ғïťčȋ',
                            'ȄЅɶƹËѠʠȄҙɺƿʨҟʿЇχū³Ӂʖ\x99ŉ?ԜÌZя˥*Ю',
                            '3έɍʅÆŨ\x7fͳҦҺƾƺŃӾӛȝsԫӾǰʶ«ԒҾӳј˴·ԇЋ',
                            '\x80±ҽɏťȩƸҜΰdǶƑŁҗвǝԓъЀӽķʉήɃҜƾîύ\x85ӥ',
                            'ҬǃɬθœȆʿЋɪŭӿĸ˃Ŋп\x8fńуӪϊȸҭǹ×ͷ\x96ʁԋɿχ',
                            'γɿȴϱϿ\x98Ėÿ҉ЛɌΞôΥ˔ӿҫϖɿЈǄљɣȌɩ\x89Įҩͷμ',
                        ],
                },
                {
                    'action': 'ӆμ˂êϢɝЯɜɳaƶρǴʌÒĉͻƘιҭ˭ȋÞ$Ԓé˔ĎЀ\\',
                    'resources': [
                            'ΚΓťϓϐӼĚϬОӰŦ)ĮɽԌ\x8a\xadħԝ\x9fǧ\x80ϲϊÍęȞңϨǞ',
                            'ԛŜǷHӀу§СɱǆͼӦĚфϗ+ʍЏĄ}ǌѢΆȯгǀÇǂǣԏ',
                            'ĘѩȕǿлͶŦ\u0381$ʈɧĕ\x92˦ǅ\x99ƲǊƘɡīçѱѕȂЕÃˎʐų',
                            'ÐrůӣăɠҧϠΦƍҫϖʞɲӘԏΊöȯǲԍЄϗў\x8fÚǃʞҊВ',
                            'Қ\x82Оņ\x94ÉҬʈϤƓƄʮƩρƯǉĤ\x98ΥʹŘƺǲȿ˱ұɯʆŀɸ',
                            'éȖŹϔ˷ȫʵòĢsηͲϋʪƱԝŐɶ˻ƆƦŭ˙\x92ÿΔʆƗɇ3',
                            'ΦʚЗϸ҄ȏΓʟԞ£Ľč˝§¶£њȥӹν\x97ҎʻůϽūÃǽіY',
                            'ǁáWŠ\x89ϻҋɴңҪʝҶUùǠȁ¿Дҧ%ıѬќʰэϱ҉ϻǭΙ',
                            'ѭƠ˨вºѶˋ\x8fȾȚѫҙǾ\x87ãʘɯ«ʌМLҖʣΰɍȥʱʐѢμ',
                            'äʒͺĀɳ˄ĎǉÃ|čƤϣ\x82ĔʜЃŹʏωŕΩ\x83Έʳė˒ǖǊǏ',
                        ],
                },
                {
                    'action': 'Җŵ',
                    'resources': [
                            'ŎϲǠɧԝȗFύңŗĆѻͱӘʕ',
                            '\x99ď\x94ЌЩǟ\u0380˸ԦʑǻƩЂŠӶԬș˗ˇŮЂǷ\x81ÃƳrȽԞɶϊ',
                            'ȤԞkȝћА˭ȞĄϸȺʆΉӭ\u0379ҋĽΚ{ӴƚМdǟ˱ԃ¾ҍϔ\x9e',
                            'ʞć\x88ƀ\x85ͱĲӯьßԓŀԊϕДƿ϶ʺӿ˺ɐȩřɮӧϳŪҍѡЫ',
                            'ɁĒʛͱщ\x9cǠÓǓ¾ΜǮ҂ѓ\x89ȏ(˴ƄԞďʈƛэҭͱCʤҷ҂',
                            'ϙ0ġɠ×ԖȕɡɤʍϞ4]ÉҦҼx1;Űɪû8πãÏ\x8dǑàˏ',
                            'čқϱάbĮ϶ĕnԭŴĖΎʮĩ£ӶҜ҃2кˠŗϳǶʛǑҁӠӛ',
                            'ҠˊAо¦ԢƱѶĔȄЉ˓ȞĹǬƷϨͶ[ñœ_Ħ˪\x97ɛǅƶˋʳ',
                            'ӐԉөΏҹύǗƷǩʱʱЯɬǗÈaы²˄[Μ[ЙύƃÀ=¸șɜ',
                            '4ǂȥʮǟȣ.Ҫ\x9cAЁəƒЄ,ȲȂƯнэɑюMŤϖɒʖҢҵŮ',
                        ],
                },
                {
                    'action': '҇ˁȏ]ҁÎčÅқāēɋǄʛȺ˞ΔъϨӊ`ŧŚȌǭÃ+Ԯǃɴ',
                    'resources': [
                            'ŊƵӉƍçόēǹ\x8aɟӄ:ɎҞԡӣʧԇŵêŀYʡʍϯαǅαʋȭ',
                            'ǼΠɋȺӲʰѣŰͻЀpĽ҈ɤǻѳҕ҉ÔɶʱĨ¿ϧӋӵͿϤpɉ',
                            'ɾʜΓĮˎҳzgϾǀЗÓϑȯψȘżϢùԏϻ®ιԄЦǞ\x80˴ʶѹ',
                            'ˣͽɄŦīxʾɑΫΚȣʤϮʺȚǢϚ·ϋСxӮƸȳѮȷЙʎǤG',
                            'Ǡ2,҇јҜ˫МЍҵn\x97˜ξŶΈΊȗԛ\x83ѝȏѷÛйřӤ˫σы',
                            'ʇgƫћȓ)Ԁ˄ѷŴɹƕМΡ×ҕζQǯ¸Ȱßy\\ԕƩåǝšӄ',
                            'ʬΠTǗ˔ϊɓЁҢȺёÞȊϰʹĀоUҡГѽҫɑǣÄʻȨӭɞȷ',
                            "˞\x8dǤјОԩąȑˢƊ×'κɚŎȋ\x80ǠӦíλеƴɦʒhϧƄř˰",
                            "ϧI'ŚԏȧFɇƖǷЇĩŝÐԕ\x83ϫԗоѷːŖȤϸ\x94Uǵƶ|Ҹ",
                            'ñґћљǓɠƩřϯȣ´ħ\x84РŝǝȍǁʚʭǉΈɴʕŬɹǠ˔Öє',
                        ],
                },
                {
                    'action': 'ѕӆwɍӴˊҼã\x8bӊӈōɑǷ£6œԑơðʈѼāȦ@£ʅÎŁϏ',
                    'resources': [
                            'ҞģŷγŮԐɎǠŦ\x99ˮҚvǠǵȤƴӎĬƱɘȬʮ',
                            'ЩÙÃ\x91ʕ°Ήͽ˝ĢȍͲԬѴE˩ԕťƅůʘȄɦʱϤǑЁǤƈ\x8e',
                            'ѵ˜¾ʩʏ˵зԋ˓˶ŝĎřѸǏˤʗ˷ӸϞX\x90ɭ˙Ȩ˘ǧ\x96ƒĒ',
                            'Ř˸ĚΌ¥аψĽƽʐý¾ǅņҍɭσ\x9eˁЇ\x91ˋϜѦƵ˖Ҩǰƣґ',
                            'ʿΔхƑƾˇ0oɻ˝ϣϳӡġȼтϰǽɰϫˏȰјЃoǱӏoɎɿ',
                            'ɟӷƘȯԘ0ԝCŇǭ\x9eјϥŧƇΑρѦС҄EĔȚlǱŪŧѝϴɨ',
                            '\x83ɅǡǛùǲ¶ñӅąԪ\u0383\x9f˾ςȓȱόҘȮԄ\x99ǌƖǬŧȕΟħ~',
                            'ЩТè¹ȳɫʙϹżћǾӥȒ=Ȳĸ;ȯиźȚАҜô\x85ɫϿѹѺʹ',
                            'ƼВƫͿ%ʬǧӨϽƣ[ōҹC\x85ʸǚĝȚӪ.ѷǦϸ´˃ҋɆƎg',
                            'ǊƴʌȔԀɉʕҖҡɎɖ\xadǥ2ӘɍɯƝʀ\x87ύӝȜЅӾ˴ҏ͵<Ì',
                        ],
                },
                {
                    'action': ',ώŅĶӢȏȼZƛӪԮ~ϻКчƪ˗˚ԚЛ¡БëАŉ˄ǘ[Чǯ',
                    'resources': [
                            'ł\x86\x99æʎɕѕƂÈɰÖ±ǳ˶ɱέИ "ώÙ\x87ģѽͰˠSϢҚ·',
                            'ў¬ŠӿʡҧƱǯ\x9d\x8a˞˱җӦǟѲΟʨϳюҢ ϖpǦԜѣҕ˔в',
                            'ǖҢϰӾȢ˞ʃϩϽԑӕӃļĘҠϴĵšǞȈɵǛԏȈмƩɕԣъ®',
                            'ˀєKɆӘɘɼƉǁ϶˓ɋȣϾĢS[ʇƱ@ϬȳѢΓĸǂϪϭƾ%',
                            'ӸʹʙŘò˥ȪÜȮʽЖ³Ͳ¯ȆʼәͰЍɭӴ˗МЋΈʵԨτɥJ',
                            'ƒѲÔʮ§ÂѺǀνîĿɑӆ˰қɽģѓŝϕμʿ^ʯʹŨԦƸȃā',
                            '˞Ɗΰ¸\x91åŒąίŒɠ#ΩÕɛΎź|ϋШyԢӴПʐuƱІґŃ',
                            '$ЩİÕӎ¢ǃ\x93Ķǲ\x9bͰзǇΔŽρ˩ƬêȏȞȮԨԂɨʔŕȋç',
                            '»ϪÃьſǡҰʷжԝӢϬӾԁɇ@ʳž·ţ«ě{ǊҌԍĠ\x88°И',
                            'ӤɓɾóʠњɵǺѾĲĪԫ˧҉\xadŉǦԧ}ҟˢӺԫҰй\x84Ϛ#ˣЫ',
                        ],
                },
                {
                    'action': 'òΤɗϥɇ"ʙϿİ˳Ξӳ\xadôӵþ˝ž9ɲkǟԅсѫԒϼ˼іŖ',
                    'resources': [
                            'ƕLÝȄ϶˩ΔԋǙʄĖÞĸТĴȋɎϧŠʏ/ǅ×ˎǤԂǫφěԌ',
                            '\x9dԥǇȏȵ˜ӹΚȷɴXяӴǄȹǏŽŌϳ\x91ʟ~ô˥ϹûΜˤǊÐ',
                            'Įҹ҂ХɕӝΟԍЂRżӯчƗԪőƔˋ[ϲАĠ\u038bɪʘįӰcĲѦ',
                            'ŊʻϗПʨʍӌѬҧЇ˃ǮbӧѣͻʼԩГƩґȀӦ\x8a\xa0ǈϜqÊƴ',
                            'ƮǃΎѤ\u038byȚo\x96\x9bӔ\xa0ҏҡ"\x9bĘҪ˭ӒǂǗԝęċŧʏԖ\'ð',
                            'ʧԞԓǴöϺψ>χÞʑΌȫҵˠПϟǵ΅¾\x96ÃǯЙƼӲ҇ʢђ\x9e',
                            'Ìѱ\x9eȐ÷ʅͺˇѦԟθºҬΜӦǘϷіβӂҨʃˌͻȓ˪θXԭȰ',
                            'ȎƴɃРȟĨĊъǁ\x93á\x98ďȁŎǰɢҞɿˑӰξ\x93ĲäрČΐʵÄ',
                            'ʣҫǼ˚7ЯԕӐΪɜŴȼӊǙȓɯǫӎ{ςÿԂӗëνѺƨ²ùǘ',
                            'ĪʿԃɉБĽĄðϙĨŜӤÂ.϶ϯҢϥXϖĴkʢǨЃҘɪѧʘϺ',
                        ],
                },
                {
                    'action': 'Ĺʭ}ϘûʫϿ˳Ρԓï˫µџӎȸԢȕ\x8dʸЯȸȷǗҬG˗Wϲˋ',
                    'resources': [
                            'ƋŧpʸήаƴĜǥҳӅkγҬŎ*ž҄ƸʀlɥǦãǫ˗Òʹ;Ӻ',
                            'οş҄ɱ¶ŴƧƌǴǅçêżǠӳʊəȋΨӒŏʪсΥɹΉΨґι#',
                            'CżɤόϸԇŸӻMɥӥǍ˰ʠəċǹҴǾϨƑɶӊćŞέҬʲĪɰ',
                            'ˌ¸Ѳѓˎʤȍӹ\x83ɠąҌЯȢϊö0ЍȺȜ\x9dαӰǑμŁӭӪƱӚ',
                            'ćǒǶюϝΪΤɚ\u038dňºԔ˔ȵħFϤϐƕӃӑQԈѬȡ\x99ƩτŻω',
                            'ʧǈΎǑň\x93ΫӶЬɷͿʌςҤюĈĀːđϪɟôÔĉɞȐѬƌТʨ',
                            'ʲśőɁԅζİЮɪóȝ˫IȉƖÓˁãTȢŉV\x86ɦu\x97˭ЯǒӁ',
                            'ʤĢĞˠϡēmP\u0382ȑїɽÕǗɏвƁɃW˴ϻǾ˄ʻѴȖɘɴȖГ',
                            'ėςÖӏʘȰӉʼϑӝҀѺҊӹяʟ˃ʐǓĄʗдҸɀѤтǁƒȥё',
                            'àŮĻΎǝıĮϛŦŭȬʐmȌ˺ԧ.\x93ϖǋ˯˂ȫ҃pϾɒ˷:P',
                        ],
                },
                {
                    'action': 'ǽЗҷjѻǏЌ˰ЊϪɌȄɩñǟĕ˴ʟϗD\x93ԮӎɔƊԞw2ºʕ',
                    'resources': [
                            'ҹѾ\\ʜϷàԉǝ\x99Òɉʐ,ˁǾķϋͰģ-˨ĞӔςЁȅ¥ɠ҄Ǖ',
                            'ѳ¦ԇϞ_˩ΈǇԬӏГƆкϓχʻ\u038bԃȦţĝϨYƍӁȑφӡǥϟ',
                            'ɱ6ǇԅΧҢȧҰġшԋм\u0378ƨȗќҽƢɕӋƙҷ5ԮԣϏИŏƹϸ',
                            'ǞưӀʎÆl{±ҬγΐˆʹʯӘ˕˷ˈϚɲǾǨ©ӗкԬϱҜѢѭ',
                            '#ϸŶ±ʞžОaċŮφҹ1Ѯ?ΝπϋƣҍĂѡӧͰҕПŽгϛӦ',
                            '»@ΜŊǀќŅʥϏηҐѸƪŃф¾ҟ\x9aӭȹÅӮʝ˶ӻїˁųɌѿ',
                            'ɧ¯Ò˹ǈНȜĹŰɓʉзÃǥΚˆЌƷϠήĺÁʍӘʹдþѵ½ɭ',
                            'НɫԏŌʢĿÏϗɤ7aӫ±ƧˋǴϦ\x94Ħ˭˵ȉϵħîƾŠŻЗѸ',
                            'ӤwΟś\x95ç҄ӔɅΗˏчÄ˹ϘƺV˨ьʥǧ{ӄԍťΡ]ˆѿX',
                            'Ƃ#ӧӄӔѻѷѩĈѦʓϺ<ĒȍĄøŻ\x93ͿӷüǽаѢȔ˃ԑȪ«',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '?ĝǉ',

            'version': [
                -7358347441181178941,
                -2841364157379718361,
                -1189751654761732318,
            ],

            'location': [
                'ˡ',
            ],

            'runtime': 'ŧ',

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
            'name': 'ӝӯǱɻОȱƧŗ\x8dÝϐʛÉďȸǣ\\ʃ4n\u0383ӝҫɞǹUȒӵɾǓ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʨ˽\x7f',

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
            '$': 'ΝȺƐǳљÿ¼ɦ˾íƧҬӖѿȐԃωǶ¹kˌ˛@ϣЬθϪʂǶȌ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4315595985712974926,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 700838.9928531599,
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
            '$': '20210228:024604.291448:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ͷμŵĦʘϪ\x92ƥійхѾ˷ȕ\x90ìѱǃЕ3çӞ°ŹҘԖŶίΧ҄',
                '΅ˣłΛƑǬүҪɄɥͽџҨΆ˚ĄɼĽĚȅӫӌӀHȮԎʤôϔҢ',
                'ɻϚǫӃē\x9cĕԅţƄţϗŘĭ·ƸƐŜθѮϪƷԇԓͲgʐЦҘρ',
                'ϻǮѹǴ˓ʔ\u0379ӿ³ϣϳoƑǏη\x96Ԩʿ҃υɂǎƐҭĖӤѠыϷϐ',
                '+Ξ{҄ͽĠѣĠƎӜ]ҌͽьɀԇˌɳŊĶЅŮϣӥȻʤ˨Ϥȝѱ',
                'γÖːIοǸÊŽƆΧŘʳТрʰӏÒϽďŌ˃ɵƊǢʯ˝ҍԂʌщ',
                'ĈρҨʎ¸ԓµғÛдϐϓʒ½͵ɡ˴-åŢ҇ǬгˏƔЬɊπϴ³',
                'ȆΪԋΈŨѪҪLƓОʎěɩœчҳ˫\x83\x95ɍƖϼӯ\u0382ëȐīÝӚȞ',
                'ԕƣǬϱǵȮ˞ɂЫ\x8cčÔμÂʲԗï\x84҉αǔ¶ĐɟÏҊSűųʲ',
                'ӄơòɾҨ\x8bҰ˕\x97Ħʧ}Ӿǥι@ѪŏŎ\x90ʝƉɸÏŰеѓǵJЭ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                1644924285234184130,
                7060399082329164110,
                -8713589794420254967,
                -7508523534619967116,
                -4688674083879385746,
                5790763309124532782,
                1453467781146958218,
                -1055587396197330783,
                -6053421431454709741,
                -6761275878369561690,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                258540.94620977022,
                597713.005346735,
                948288.4963105173,
                347924.81859458017,
                596182.974425763,
                714204.3686236624,
                346135.5967802133,
                950199.6146551277,
                488054.85052417545,
                537362.9284013772,
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
                True,
                True,
                True,
                True,
                False,
                True,
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
                '20210228:024604.293273:+0000',
                '20210228:024604.293313:+0000',
                '20210228:024604.293331:+0000',
                '20210228:024604.293346:+0000',
                '20210228:024604.293361:+0000',
                '20210228:024604.293376:+0000',
                '20210228:024604.293390:+0000',
                '20210228:024604.293404:+0000',
                '20210228:024604.293418:+0000',
                '20210228:024604.293433:+0000',
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
            'name': ' \u0381ƳæҹϾɯʯǨ±Ɖҍц˻Ϸ˸ϻµЖӂϸϖɩǘŵZIýƘo',
            'value': {
                '^': 'datetime',
                '$': '20210228:024604.290929:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ԯ',

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
            'catalog': '϶Æҏɠĵĳƶƥӕϸʇ˄ԏϹɲӅүűjǪѯDȺśƚ\x7fɋδ˝ϲ',
            'message': 'ɺȕωɌӌʑ¶ԢǮȪҁλѰØԔħӒˌѽӕΖƉâѫξßœĞϢњ',
            'arguments': [
                {
                    'name': 'ɌǈPȓƲϱͰʩɋφύɗiȭΉ\u0382ϝϟˑ·ó©ȕʍrџɜ҂mЩ',
                    'value': {
                            '^': 'string',
                            '$': 'ǠЛˎҬ˕˸ԂқѧØΐ<ÒɱЁĿϘΟͽƥ˫ЦԟĚ3ºѳˀп¦',
                        },
                },
                {
                    'name': 'ԟ',
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
                                        False,
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ϱʷ˟ħɷɘȬǒˋˊϐȭ˱ÔԕӀӻĠęɝʚdё',
                    'value': {
                            '^': 'float',
                            '$': 620880.85780506,
                        },
                },
                {
                    'name': '˫ɬƕĕYЦÈC҇ȥѾ\x84ɌφƯĔ\x91ѤðƞӾEǳũѠˈƚӇºɁ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '°°ЗөҟTԍӓкϻƳʭ\x84К¶§Х&ҿǣɌѝĜʱɥӗΑԔƗӢ',
                                        'ùˆȼЅљ\x9bϏǡӜĜņˡҪȴȕÄμ\x8dǥԮоϰӕɛϤŭϝі\x8bȲ',
                                        'nŶԝVӈɹȆƼѿӱБХwγФϵɃǁ©ˢȗǸhҐӗӈƙйІƨ',
                                        'ŃđЙʎɣŬʫʱφͷςČΕ˱\x88ǴǇϨƷƧ˷ҺưĿԘŇк\x87ϒЙ',
                                        '>ǇĽϬȔԅÂÓǲǄʧĹǺǃɐњ҂ӍԮҰɫӱńƜЪ˕ńԅʤĀ',
                                        'ǩȾΩÓѺʚɷȕҷŋŀȔ5ĬǎΥǕӘvÜдŭʧĹ\x87žÌɱ˛ǌ',
                                        'ąĲц;Ҙтʗƽļ҇=×5ÈȼƣϢԭǎ˕ěƅ]˞ǧƽҨȑʊв',
                                        'ѡňAɳαƯвӕҒɓśǭ¬ɢǌ5ƶԚӴˮ#:ˌȅĆƑÔť˪ό',
                                        'ȋˈѕŉȁΪҸƭĿƓМșԇϖүƻʣ˶ҵ\x9cΓɹэ҅ӁʈҙȇÞϚ',
                                        'ėъ³ͳĴɁǦ˒ɹr\x92ÊҌХwȃύä\x87Ȃşӥ¶ŠM¸ΟƐ¤ҳ',
                                    ],
                        },
                },
                {
                    'name': 'Ȫ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210228:024604.287799:+0000',
                        },
                },
                {
                    'name': 'ƙ¯ÝΞĠͱѮωưŒЋʋҬ¡ûΓчѯҍϼÒ˹ӰµϲвǝĞfĨ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ʛáɖǒЊʭȔ3ʖ˛$Ŝ\x9dԆϏҎɳ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -1682444423232618316,
                                        -2357040123923361793,
                                        4657239049991044821,
                                        2902456745922084776,
                                        -202505285710333223,
                                        8488465773721444504,
                                        -3606047558283592103,
                                        -4758648779736174498,
                                        -7478908645714489250,
                                        -3146421630200695049,
                                    ],
                        },
                },
                {
                    'name': 'ĹΥӞ\x9dҞɠӯÞд˜ʼɳƨЖ˪ҚϭɢǮғǶЗюҽ˘Υĵҫ$ǐ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210228:024604.288885:+0000',
                        },
                },
                {
                    'name': 'ԚŬБśЃʀȞŉɧͽƔœĎЍşѨʚƍŲѧқхȤʠɞʄ*żƄѳ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ӊӏԄŬħƸͲɅr\u03a2ƟʦӐӧǢ˵ĔÑëŰōҤұƜċŧ˴ʲŃx',
                                        '1Əǖ\x8c"χȔʏ;ԖӚɇԜ9ßCŨǋƿҷӏɄЏ\x97ĢÅЩѳĳɧ',
                                        'ϷǪɳΡѥ[эHʜʥè(ǩ´âӈǯß˺ɁȨδƍԪjˮ҄\\Ω\\',
                                        '˝ςǋ΄ÀϟзÉGɘӼŴƵɾǣͶβХdȅщҧɁ¤îɺγǌ˹Ʃ',
                                        'ӷ2ʯѕȮϐΟ\x99Јǚӂ\x8cӣŭвнкПȉ\u038dɝƇҙ˳ЄʹȇbĦ7',
                                        'Ɍϼ˺ªҾ\x9dϛʤԝƌҔ\x9d\x90ǛƽΰЛϷҊҠ!ħʼɍΦҽ¶ӈǬʷ',
                                        'ȥɘΧǿǓǟϗǕԉíЇӚԏɪZĤǣШ[Λŉɨȇ:I˝\x9f˸ɒ\u0381',
                                        'ΆÆQĥ\x86қŨ»ҏдΦɐѵүԖĮϔȖіϗӇƚȈҥΎǉˀgǋë',
                                        '\x98ТˡŧϗȢЂ\x87ãƆCʯ˾ҎǇǾʌʻȎ˽Κ/\x9dυˬfϹΟТ˥',
                                        'ʧõЬіЊѷЗ\x8fϊԬŜÑҚǙƴŨŧǷΟҳІíáĴӨ\u0383ƳʦҨԌ',
                                    ],
                        },
                },
                {
                    'name': 'ȨɱHĻʱҽÔƹMӡ΄чԮȂƕǾєòя\u03a2ɫԙʊȱΒȱɣʂƑθ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210228:024604.290182:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Вʣ',

            'message': 'ˢ',

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
            'identifier': '˶ʡЅӆ«ǔǻͼϷӟѬӦȆϊа\x99ˀƥҨ7ӧȷҞɪоǷ>ӐӇǋ',
            'categories': [
                'configuration',
                'access-restriction',
                'file',
                'os',
                'internal',
                'access-restriction',
                'configuration',
                'configuration',
                'invalid-user-action',
                'access-restriction',
            ],
            'source': 'Ɂ×ɨΏ8ʝϭԂϤʹƾΒƔǹӍG˩КąŻϪğʣЁ˭ːΎÑѯĈ',
            'messages': [
                {
                    'catalog': '@ƨǏсю6®˵\u03a2ƨăĤȍåςѧ\x97mРəЪ*ǭţƢǾɮɃɦԓ',
                    'message': '$ʛƉØɡɎϝ\x96ķȵԁåкfūùɯҵи˼ʮǲėəˉǋԂԓѶȈ',
                    'arguments': [
                            {
                                        'name': 'ύŪҰĮӺɜѾ\x84ųÒz\x80{Оӽɨ>ƀȭõьώƑР',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5984738806291687522,
                                                    },
                                    },
                            {
                                        'name': '˶',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.242452:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԖĵГƚŸӞѤȽ˱χóŘӅʁğĴѝǩЭФӉ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ĄǅћԍơӼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 199616.85559771524,
                                                    },
                                    },
                            {
                                        'name': 'ѯԦˎӰ>˯υdă˟ҰȈBѨ\u038dƻԌŴԞАΆƆǝʭϞǘӆɱĸƂ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -95540.13064818153,
                                                    },
                                    },
                            {
                                        'name': 'ѧџҒ˰ͶϺÒɐдǍФɺċҭŰҲӑԡЁ>',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            340230.89861579676,
                                                                            342904.71089452435,
                                                                            889218.6367967223,
                                                                            976511.9953482742,
                                                                            867760.8333223838,
                                                                            458407.7170883268,
                                                                            504345.2328069126,
                                                                            785141.0882615248,
                                                                            949907.4558229931,
                                                                            416467.9161464181,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǨcȐӷԃĎ˽ȸʰӒǅö_ÇđһċԒоȑΗԮшѶ\x8aζΛļο|',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'αƜʪċӆɒZ¸ţЗѷȼĥ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6277369174421005398,
                                                                            8935212708236946433,
                                                                            -5671634244115869391,
                                                                            -3430942361957914699,
                                                                            3776495073800110128,
                                                                            -2328482963451766677,
                                                                            -3759407202192227112,
                                                                            5836476671945967059,
                                                                            7913805327815466709,
                                                                            2405252372602587542,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'м\x99δë˲ӂǄIѳɻ˨r<ӌΪ\x83ŇCӶǳѹъěŔĺɂ<ɋZԦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.245236:+0000',
                                                                            '20210228:024604.245265:+0000',
                                                                            '20210228:024604.245274:+0000',
                                                                            '20210228:024604.245280:+0000',
                                                                            '20210228:024604.245287:+0000',
                                                                            '20210228:024604.245293:+0000',
                                                                            '20210228:024604.245299:+0000',
                                                                            '20210228:024604.245305:+0000',
                                                                            '20210228:024604.245311:+0000',
                                                                            '20210228:024604.245318:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѳ\x8eʎɧȌ³ŗ˨\u0383ɞο˔δϜ4Ҁ˩í×ɴcΗƴШʪsӃ҅Ͱγ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                {
                    'catalog': 'ҢѼΛðəӬɻʊǋ·7ǪүʐØ·\x96ЕĥʂʾǵʪˢҳԤТ)īå',
                    'message': 'YĚƫӣĖӑɩӫĘȂ΄љɾòȧƲї˫Зǆјҿƪ\x90ĖǍс=\x83ɷ',
                    'arguments': [
                            {
                                        'name': 'ʁ\x8bЊ)ϰӻӨʎґȟзБʳϧĵә˅Ó|ӱӬңȉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'чtϞ˲јƉZϋȪºΊŁtƚȆłúпφɃɓѕüϋӬЪԤɐг¥',
                                                                            '\x9dɫίȴӏ\u03a2зԤȁȭǓӢwЗ<ɹ\x8aӌ\x80ʉʓԔ˭τȼϑӡƅĳÛ',
                                                                            'Ќɻʚƻĕ˦ќƟĻɮƍѿ\x9cłN.фɹΘˮŃɠϠǥƻî҅áͱͰ',
                                                                            '1ҫϰсϿʢ϶ŪɼF,ƩУϱɹɉѵ\x8aŨp\u0380ќГԘβɴŶĩyʑ',
                                                                            'ӵȨǿ2ĊȞʮ˃\x81ЏȦ±ȀV\x8aHƏξӲңҦ±İΧǣąǐįә˥',
                                                                            'Ǉiȴȩɠǖ\u03a2ĘζǼÍŷȲԌГҫ8џӆʉʼºñќșЍԩϻƄá',
                                                                            'ȂϾπґЦ\x96ŁΏÚϜèϠӭЈƊħӴșΉrë˖<ϸRʊƅҸғφ',
                                                                            'ңǮü˙уɒЖԔǧ0ϰҷёѦƯˋĚІǶӻŨ˪ƆɅĀưǋϧʷΆ',
                                                                            'ȝѽĪρϰȒƥΖȈϫŏГͱEǧӆԢЈѳɠȸ˞Đұϩɭϟϖƾҥ',
                                                                            '"ŧњȤŽϴʲŖǤШɎӭŒҍ͵˻\u0382ӃǍǵΞʥÆáC0жʙҕǏ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'іƪԊѣҲ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.247780:+0000',
                                                                            '20210228:024604.247816:+0000',
                                                                            '20210228:024604.247838:+0000',
                                                                            '20210228:024604.247871:+0000',
                                                                            '20210228:024604.247883:+0000',
                                                                            '20210228:024604.247894:+0000',
                                                                            '20210228:024604.247905:+0000',
                                                                            '20210228:024604.247920:+0000',
                                                                            '20210228:024604.247952:+0000',
                                                                            '20210228:024604.247967:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԟŊÐȮҦŽҵм%',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'έ҂҆Pˊ\x90ϐťɢҾĊɈȨɢÄҜϤOѿбŊɬɾԓЊԀ\x96Ϭϔʚ',
                                                    },
                                    },
                            {
                                        'name': 'ҪӊM΄ѨåʐɃȐǓȌƳȎô®θŒӤɍƸѷ\x86фƦϋǺĝγĹĥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.248758:+0000',
                                                                            '20210228:024604.248785:+0000',
                                                                            '20210228:024604.248807:+0000',
                                                                            '20210228:024604.248835:+0000',
                                                                            '20210228:024604.248845:+0000',
                                                                            '20210228:024604.248857:+0000',
                                                                            '20210228:024604.248871:+0000',
                                                                            '20210228:024604.248905:+0000',
                                                                            '20210228:024604.248919:+0000',
                                                                            '20210228:024604.248933:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Мˇ!EњcȩͷĵéʯѼƬöҬȝƘǈ˅ϭ\x8f\u0378Ӕβў\x90ԑӑŝȆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.249430:+0000',
                                                                            '20210228:024604.249453:+0000',
                                                                            '20210228:024604.249469:+0000',
                                                                            '20210228:024604.249483:+0000',
                                                                            '20210228:024604.249497:+0000',
                                                                            '20210228:024604.249511:+0000',
                                                                            '20210228:024604.249524:+0000',
                                                                            '20210228:024604.249538:+0000',
                                                                            '20210228:024604.249552:+0000',
                                                                            '20210228:024604.249566:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҕŅҙʚǅ҆ӪŮƗôȐ\x7fԁˁˑī',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4723831078976653831,
                                                    },
                                    },
                            {
                                        'name': '\u0381҄žˋΘ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϭȡ\u0381ĩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 45366.140345767984,
                                                    },
                                    },
                            {
                                        'name': 'ąӍ\x9dϫЖʿǿȒɚϼӞӞԪ|',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.251092:+0000',
                                                                            '20210228:024604.251124:+0000',
                                                                            '20210228:024604.251141:+0000',
                                                                            '20210228:024604.251158:+0000',
                                                                            '20210228:024604.251179:+0000',
                                                                            '20210228:024604.251208:+0000',
                                                                            '20210228:024604.251217:+0000',
                                                                            '20210228:024604.251229:+0000',
                                                                            '20210228:024604.251240:+0000',
                                                                            '20210228:024604.251273:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΟьΪӁԧДɚҲōç¹ΥέбЙ\x9aϦЌȖҖɉʂêϼÌϠwцԊϟ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.251740:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϾҿӤĿˆċú˜sşʔKƂƯƽ',
                    'message': '˟{ǮpχԎƠ-@ѱъˮĨӤЕǖӦǦŸ\x8eĵһɭĭŮəХҩɢȞ',
                    'arguments': [
                            {
                                        'name': '=Ԉĕ˚ķƺƉğfĹ˕ĐÊʣϞʭ˼Ȋԁǿ\x9eȮЀɅɐÂШйзŤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -175699352182661264,
                                                                            -2239077143709841062,
                                                                            -1994022461115350463,
                                                                            -3491176209483512348,
                                                                            -8648733746579196387,
                                                                            -706673103488667013,
                                                                            -1758926315463210369,
                                                                            -594337505436198876,
                                                                            -4493738253078649509,
                                                                            -2142640594783276573,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˅Ä\x9dùªǵ·ǲсӽˋΨӄҟǄˆМȃƷƒ\x80ŵҦùԆăƹ\x80Іɟ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 390673.86509800615,
                                                    },
                                    },
                            {
                                        'name': 'Btφ϶ƎÚͱɛȒθĺͼˆA#Ôѧˋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -254699656106944599,
                                                    },
                                    },
                            {
                                        'name': 'YŬјԐиÜÃƌҹҥķŖÀɘˊƜ˶(ʛ҆ȉӱ˞ҝңπ\x9ażƲʧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7527081924165732791,
                                                                            2552201502236236760,
                                                                            5789984233127913862,
                                                                            7282903636757242996,
                                                                            -8207998607313973103,
                                                                            8962945108798104228,
                                                                            -2737520226941290013,
                                                                            7367352492333924409,
                                                                            4945992942662822038,
                                                                            5885487520687628821,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǴίҾ4īʴƌПѱӓǆ˾\x87OͳʦϔӦǨɒɦԩ]ϞˊȻʈ\x8dԭӬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            761340.5830960441,
                                                                            963906.5854139447,
                                                                            616121.4181490531,
                                                                            532866.8448496204,
                                                                            813075.5105728476,
                                                                            836835.4587167857,
                                                                            714434.0645051264,
                                                                            350120.23430010414,
                                                                            -56942.16608347367,
                                                                            417095.6164808254,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʺ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.254865:+0000',
                                                                            '20210228:024604.254894:+0000',
                                                                            '20210228:024604.254903:+0000',
                                                                            '20210228:024604.254910:+0000',
                                                                            '20210228:024604.254917:+0000',
                                                                            '20210228:024604.254923:+0000',
                                                                            '20210228:024604.254930:+0000',
                                                                            '20210228:024604.254936:+0000',
                                                                            '20210228:024604.254942:+0000',
                                                                            '20210228:024604.254948:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɍ$òƸÇЂŦĸЎҤҙ\u038bİĪˏȮǋқ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƏӊӉYӺHԒ˽TҐǲϭ+ˠɋˏǔȀY϶ӳƹϫȐԃǆӳʱҬԄ',
                                                                            '˞;ΧҢsс\x9fUοɄƑЅǄȯ_ЧǴ˅ŌǒɘàЇŻɗˁľƢƎƤ',
                                                                            'ʨŧAʦȃ%ҏň¦ɓЬ˹Ʉ«ѾПƴĨĪϨ˷GȺȯеͼҸ\x89ʣȱ',
                                                                            'ɬűʕˀαΞӔwųυӂЙAˊӰȁȺɅѯΡǭm҂3ɣѽƋǧώԓ',
                                                                            'ї\u0381÷ΩˑŮǂȈ\x98З\x88οЦшСƤЕԑŭƊԖҳǒʼǌɤьĝԔň',
                                                                            '˯ĶκҍτʾªξдʥΩ΄ɂҙŒéѨ%ʭΪϖǊӖЅ¦ÐɍʑҀя',
                                                                            'ƱoˤOψϾÝϡɩĐ˕ɳÒϦšȍȘӖΣϴӎɾ\\ϤϽƲÿǏŲт',
                                                                            'ЧѠƼͺBǏŘͲĊčЪʋāоʤԉɊŻCәԩԋċϖYǦèΨ¹ď',
                                                                            'ЍWȺϛȇӈӊѮªѝɀӊƟũOǆЍĒ҃ʛˬȳςĈœʼęяȖǜ',
                                                                            'Ǌѥϙ¤ϟȳȏƬ˃ƑϪҞ¼ҥ\x93åΘSƦӭľňʉϫéϗq\x8fƶҮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8cȁŋŖ\x9dӇϥЈɝɷʔȦ\x9cÙ4˗ФïˬĒùʭ½Ͻèέтǚĝí',
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
                                        'name': 'ί×ѯ)ӓŉӝʤԩǸ҉ͲŒЪӰʨȡԐѯÞӭŸ΄&DǨφ˲\x9fĝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 658261.9121805016,
                                                    },
                                    },
                            {
                                        'name': 'ԥӓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1590776804679032037,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǮˮӀϧĒЮŉłʖ+ҊҌѶɈԦǔӮņɺɜʐˋŲӾ˼äγҏĄƲ',
                    'message': 'ȉ˸ͽųÓԑȥӄ\u038dçǏùƴƿ˗ǟӒTļЋԚʹƧĳĢžąϜˋѵ',
                    'arguments': [
                            {
                                        'name': 'ɅҵŪ˓ǎYϭŕÙɩʮƻɩ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.257085:+0000',
                                                                            '20210228:024604.257113:+0000',
                                                                            '20210228:024604.257121:+0000',
                                                                            '20210228:024604.257128:+0000',
                                                                            '20210228:024604.257134:+0000',
                                                                            '20210228:024604.257141:+0000',
                                                                            '20210228:024604.257147:+0000',
                                                                            '20210228:024604.257153:+0000',
                                                                            '20210228:024604.257159:+0000',
                                                                            '20210228:024604.257165:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '/ƕŇҸѸúʼгѻCВдȥnˉĎԘԖ\x9fӝʶ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϿʵǧrΗҜӿȪåϤȍϔ\x82ˀʿˌӘƑӣυƫӵ҄Źƥ\x7f@ҳɺſ',
                                                                            'ŵĽƂŐȼƬѽӜóġ˱ĥүʅȂӂˎëЃʣf?ф҈ϠѠϗӴÁҗ',
                                                                            'нͷˌˣǨéӍĄ·ωТƻȔ)ѱ¥ŨϔŹТ\\ßǄ˹^ԃФòˀӴ',
                                                                            'ӅǔŻŚԖχÝê\x83ӌчӮҡʍгǚʥσɆ,эЦ҆\x92ƔˢÒfȴ˘',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɢàӦ\x8eԌўéŴƦƐОſɁƷȿȆǎǉȬȄÈɆăҥŔƆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -3517.7854256857536,
                                                                            240333.60637429205,
                                                                            58382.405882267456,
                                                                            83271.09453660302,
                                                                            76897.59617792562,
                                                                            393666.8354159459,
                                                                            159502.0452398021,
                                                                            115688.2573435755,
                                                                            475761.72044847626,
                                                                            -10780.448232283845,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '§ɻîÛЇëɇˆơəÓ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 866870.233046381,
                                                    },
                                    },
                            {
                                        'name': 'ҵɹ£Ѯ!ňŦҫрԁ~_ō\x86o/¼ҫЃ˝Й˖¾ÎԂѱӿӮβϓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ňɂʸӝÆ\x8a3уϞϢǄҚčoіǈѪђKbϬȉԪŒ0ǈͼʹƐʵ',
                                                    },
                                    },
                            {
                                        'name': 'ӭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.258597:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Řeȣѕϰќƅ˻Ԙε§ͼЧ\\Iȥɭ˜ЫŪ˞ȫτ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.258787:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƏƣɊȃ&žÃmɻҮyGӭƛś˘ѹśŵʲ4·˫',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 90610.91473822249,
                                                    },
                                    },
                            {
                                        'name': 'ûĹʫԛ6҈Āҷ½Ѹ˅ҖɘУӌ˷',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.259149:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÓǨjzȬǋİ˃шƫ7Ȭƽ˦ψ˸ò',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ĭ\u038dʴ˚ʀÖͳӹȣѡŰńӐÚČɪʇӕřǳԞƧχOłѡџΗў5',
                                                                            'Ԡ1ƘӶҜΈӎʝλgѮʨŹͶɣȕƝӡӸǇұӭʰ,ʼCӮȭ6ρ',
                                                                            'ʒӉԩěϋǴЫȌ˜ԙˤԟųϤ˱Ƭˑӝiʊ\xadƱǺʸЄó\xa0˲īӉ',
                                                                            'ǊүˮĉǇ<ƹҰ7ЍȊПǇʥəʋŅĆˈȟ\xadÝŤŰЩΨөͺǼΆ',
                                                                            ';ŀ\x95ŷȧԎµФÂ¢Ԃǳơɐőíˆь˅ʮĹȷƉӡɵ1κɫϲT',
                                                                            'ȪϝȤČˍӯŔҚȏǩԈɀʄ¤ѨѾҠŗȩȲʉŘӡƙ˝ή˔дЉʤ',
                                                                            'ȼ˄\u0378ƴҰŷýİΧųѯɬҌȔňϱҳɒǘЯɩˆʅǬӋY\u038b=À0',
                                                                            'ĵ\x8bȈԫӁ\x93ΣʼюþΐԦЧҰ\x88ӤʩʂYԌƦʭƸǅѓϨʾÐԦӮ',
                                                                            'ĖϣųrhÈҧǰ¢ҠЮ\x83ǘҤǯûɷˆųþӋȪ\x96Lɶҿҁč\x9fa',
                                                                            'ɇƅưҶζҡƭ|ʆʄХȤǁ6ŤϝȟԨ\x81Ԁƶѭ.ŏĂǍЍˠ¡ɒ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɅöѬʧ˩ĴŁЙҾȁԢ҈ȃɡŉїƺúѫmя\x8aӊҟʶɟӹӑϜϰ',
                    'message': 'ϋŶ˸ѭøΊÂöğ\x9cԥѭĎπȭĄƇҸӞбʬΌƇҽĥɿϬň˞é',
                    'arguments': [
                            {
                                        'name': 'ҁȹʽʅ\x7fǾʡȟ\x9aŶĪʉǟʹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.260235:+0000',
                                                                            '20210228:024604.260261:+0000',
                                                                            '20210228:024604.260275:+0000',
                                                                            '20210228:024604.260295:+0000',
                                                                            '20210228:024604.260330:+0000',
                                                                            '20210228:024604.260350:+0000',
                                                                            '20210228:024604.260372:+0000',
                                                                            '20210228:024604.260379:+0000',
                                                                            '20210228:024604.260385:+0000',
                                                                            '20210228:024604.260390:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˍŁӌɘǬʄɴþɱǗÛɋӧѹǒũŽӳǄϵǱīǏʚϜ\x86ӡѩЁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8542770569994175578,
                                                                            4516167824682759285,
                                                                            4271880452095882502,
                                                                            2636850345439296412,
                                                                            -7794626813306397514,
                                                                            2376086984623815722,
                                                                            7077843405109747392,
                                                                            2118708200934396237,
                                                                            6406317183966174643,
                                                                            -656088593391961028,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЦԋҌ\x87dбԥʴǲԭԫÛҔдήж',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -83304.04957534291,
                                                                            851311.4032932614,
                                                                            775132.6743331352,
                                                                            805395.0644288698,
                                                                            972143.7681855604,
                                                                            152809.522713843,
                                                                            452025.0825942175,
                                                                            124198.44222863001,
                                                                            854195.4393151286,
                                                                            312327.8961355438,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԣγҙ,ģůΈΝԕŽΦŀƶĝˍΥϤˑşҼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 236674.0633309009,
                                                    },
                                    },
                            {
                                        'name': '#Ĕȑ¨Ͽ¸ǂ©ÄΎϘɕɓɼϥДǗǣϗǍΠ;ř\x9eӐ\\ԜÂ1Ҋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3332659023195407948,
                                                    },
                                    },
                            {
                                        'name': 'б@Ɇɹѝũʧ_',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϝѣϡƥɻƘëȉˏиɃЦɐȬóͰžԒδȉȔɚҎЊұɛĆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            805119.6184132515,
                                                                            911374.0881896028,
                                                                            511318.15345437685,
                                                                            291319.0227975018,
                                                                            -23016.7609425282,
                                                                            150387.8540445486,
                                                                            -15993.452531789459,
                                                                            344940.5557749691,
                                                                            489939.74258381117,
                                                                            457733.0420219437,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '"ĕXġӪȎзҶԉ¥ǲĉѣ»єө',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɡ»ûĖϐӡËћЗæӟʷ\x7fĚςɞ҂ĎǾӰ˚ĝӈʗΓП҂җξ\x82',
                                                                            'ʞӑ҈ŭΩƟwħϏʨκӅäʯҶϣԃәӨǏɚ³ɒѾÀʋÇѵɜ`',
                                                                            'ºþȳμѩǐСͽƄǂpʾɫӎưB·ƚɗ΄ґ΅΅Ζƌ҄\x871ȭͻ',
                                                                            'ϲȽϭœʑɢӕәԣÀǬӸȃѠЦώϰ\x98ԬѩˠršǮєƇŪųǏŊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӲăċӸȆ»ӥ9\x81\u0382ƞSѥȫȀʜѣŲƋЙ6ϕɮһ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 362231.84771839116,
                                                    },
                                    },
                            {
                                        'name': '\x86ØɶłЗХȒŢˎſЖҳċλёàǐOŶ͵ԝԫʿ҉\u0380ƳҬО>Ԋ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7126415335861731077,
                                                                            -6912287457876513524,
                                                                            6836287675050743651,
                                                                            -6934312369107241456,
                                                                            -4609405162340550308,
                                                                            8920055694274147511,
                                                                            8691584812778241438,
                                                                            -5954391839175573008,
                                                                            5030160396966462572,
                                                                            -1712993689512414505,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˝ҎƥсԌφҪϣϹď\u0378ėũуêɗѕг¥ˀ#ÛƩşɷůmҔЖȵ',
                    'message': 'ѩϦ1ЗŘӣԍˈɨƠɯЖɑƾӄĶːÆŊϯѤҙäˌ\x89ÉǙŖvϜ',
                    'arguments': [
                            {
                                        'name': '˞½ѢϪʞóѥŽ˝ʨчԉƥΑɎҔºӽϕ*ԘªªԢʆΟ·ǭлѿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.263519:+0000',
                                                                            '20210228:024604.263546:+0000',
                                                                            '20210228:024604.263554:+0000',
                                                                            '20210228:024604.263561:+0000',
                                                                            '20210228:024604.263567:+0000',
                                                                            '20210228:024604.263572:+0000',
                                                                            '20210228:024604.263578:+0000',
                                                                            '20210228:024604.263584:+0000',
                                                                            '20210228:024604.263590:+0000',
                                                                            '20210228:024604.263595:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʳԦɛʠ\x93ӭμ*|\u038dȡԡЪĬɮŸώ΅Ӟ\x90',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϾǲӤЩҝ˘ϵǵѨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.264117:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Αmˢɬǣɗȅ\x9aƪԉPȩXŕxɢԞʻš?ӌλæħď˞έǌȓŗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǯÉλζȌǀ|ӲϳԩϞoɆX8ӋʖӳҙӤжҳΉě=Śʏ\x8a+ƿ',
                                                    },
                                    },
                            {
                                        'name': 'åƾʳқѵǹǟҒȟӍÆȘǴҵдŪeĵƖԝҲύͱњԠȃϛǬԇȭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 748414.2552913536,
                                                    },
                                    },
                            {
                                        'name': 'ȝĹҾєФЙѹӈɟȮԑԑѹԖʣɘ;Ñ˝ʏЮȈOǢȼΦŒ҃[ԥ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʁȔǠȹʑџ\x91ŌfԟɌΜâжƁěΉCĉƃ˻ҺrΌҾюԑƆŪǬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϯũ¡ȋҰƀʆɴ˗ʏǦԁȌ˥\x7fмϘϹԡќˁԂѪǯƮȿúҝȺԅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.264948:+0000',
                                                    },
                                    },
                            {
                                        'name': '˖юɪҚƦƱʘz\x8cǁΦщĜɠŅ\x9eåΘЬѕƞ«Ķ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 993908.0721088247,
                                                    },
                                    },
                            {
                                        'name': 'ӇԋyΟʖӦώũ˦@Ӟûˆˌ҈ӊ˂ҊȭɗʍūQѸƮԤʼưɇӅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.265333:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȇԠцƳľʈӻϸЦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5108069555336113941,
                                                                            6883347129491005022,
                                                                            392640617330152782,
                                                                            17981451143976892,
                                                                            6034294267170108371,
                                                                            2030936956064139820,
                                                                            -5860769011294813009,
                                                                            3634951679977777819,
                                                                            -4536997072443976234,
                                                                            -5032796021572809112,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʩ˪ŶVЈ=YϤʩԘǂpƏdΠ\x9eѥʼ˖ĽѬʱͰаҰǔ\x9fӯȔĠ',
                    'message': 'ώ8\x9a]әƨǩӐѬ\u03a2Ӝ˘цÏѯʲɠҸɧҾρŔȎÙ>ġʰԄȽԀ',
                    'arguments': [
                            {
                                        'name': 'łҕoѕȀȹƙʯƞ˃Ϻ˶΅ӄԎӏϑԗĘɸďˬѮѮшΌ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.266245:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ς',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8719688469419401071,
                                                                            -6576183595589503833,
                                                                            7585760632006704321,
                                                                            -3035276383882068731,
                                                                            -7085681079440917770,
                                                                            7576398423303844354,
                                                                            -1316790749539703481,
                                                                            -3269748160446898618,
                                                                            -3609149125212924201,
                                                                            2299222187061471132,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΏͶʡȒ|0ĝȭɚȵ!Ƥ´ӯаɃѝ\u0380ӛӄʣƩʁıοХ»ÞσÂ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.266747:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƕӒζ˗˃ң\x9eгԇӎϫұѭĜє˖ѸɨêӝΫґÙ˘Fƻϛ\x94ͺϽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʲϔȷҚ¹σҰɠ¨Ǌ¥əŕϵEӧΛθѦŶΚĺíʥʪĿ>ңqz',
                                                                            'Õʿ˭ƱϽƓҍӢĠìTɕǲƦԩ˩ŦáŹѨĻокŊΣñΉ\x8bôW',
                                                                            'ƄÀѥƃɎǏʧіȈΤŦƐĖàϜƯǡЍѰÊԖΠĒɺȍLͽ9ʰƎ',
                                                                            'Υć\x8aӯхĉƀːɎǆΌ˵ҘӃ˗єтȎɔƥƨʼƋIԩѨˉɔӺZ',
                                                                            'FѪЈλƻŝԖ\x88Ӆǂԃ{\x91ЄέýɴíŖ¥ɼжϬƱÓ˴іƴѹ˷',
                                                                            'ťӍӚƓϋ˱ΨĩȒƩʻ\x8cƥҝiɛ˧ѪΥɀ҂2ɉį˛ƚĬӽƟč',
                                                                            'ʻĮΚɫŕĠϩԈӣȉ\x93©\x96ЃӹŦɏҤа\x8aɎϩҩπńmҦōӟԂ',
                                                                            '˭ȮҼχʔӱʗǰŞϢЧļɪԚt.п\x7fμĂ¸ƞď\x8b˓ӾΕԦӮɚ',
                                                                            'ԔϼɋTҢƁĀќƽMŗӖƓҸŇɔƩϖƃ\x84ɷɈżɜӌϵˁɃ҈Ԣ',
                                                                            '¡мʨΕһȂʯΩˆԚӦîѣĸԅɶҔúӲϡʣ˨ȪƀƢƈʳѥɖƜ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˹\x8aκϪ˂˘ǀβ7ϘѼȜοԉ%ˠѹӚҙʡά$ȎÈκΧЊbǣń',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '-%ƈԛғ(ȗϏ_ЛĔƝϙРǲбįĹʡϊɛӌ!ɩЀ\x99ȖцԏϦ',
                                                    },
                                    },
                            {
                                        'name': 'ƁўƋ˟ǏυϦdʶѝΓ*ȯ˨ГĈȞǖŀūМÂѧјΕȳ҅ϘԄӐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ͷ\x93ɓƖ×\x87ǻӪюҺǖøìŹȋŮΗȊ˸ϯйѻ˥ӜӵΪ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'цΌˋƫШʕϘʵ҅ɪĵϼţфшˍPԜʐϺҘ3ΔϓҮЉ˰ɟΥҹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '»ľʓҙӐū˦ӹ\u0381ĦʍŚԦɰ\x82Èûūǭʾ|ĞųĎˀţ҇tҾƢ',
                                                    },
                                    },
                            {
                                        'name': 'ɺʨ¬ć\xadѷ˦įɧʵŔϱĕÜЍ¹¸',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            793877.7046872419,
                                                                            249374.30853950267,
                                                                            741819.2135285808,
                                                                            489403.4708257904,
                                                                            605124.2350268157,
                                                                            175226.67719774472,
                                                                            79509.63995933972,
                                                                            139160.79469443354,
                                                                            144283.85274257907,
                                                                            -2542.138603040541,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƼАԉȋĖMǋ|ɏˌӊӻα',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƻƶÅʩɢ·УūЪņ)ʴɷĶĚӖʗŠ҂ԏµ\x81¯Ǌ\x9fɓπʹӼï',
                                                                            'ѱôǜԔ Ȯσ\x9eűӑԧÄAɕƪˁӚӯȵʊҫƥɱLӈƙƯ˝ԭÁ',
                                                                            '˾ƺŁú<Ŋ>ѥĽúћ˹ͲҒǛɵnőǔȕ»nмҋι±ĞbɔɎ',
                                                                            '\x8dÍǏ˃ΰɴɽŘӤȨʅϡЁфĩďBѱ\x9cÃʢŇŏ\xad/˟>ěʇƤ',
                                                                            'ɽ8θўξɜǏӢ\u0383μ˰ŽʚMλς§\u0381ÝȨ҈\x93҅ţԪʥϦ˂èΣ',
                                                                            '\u038dƮ´ϻaƤƦʏTϻԅ¾ϫ\x8fӍɠ*FǅÏ϶ħϓȊª\x96Słǔԧ',
                                                                            'ƨсЃ+ɅËρПʲƚˎÞɾÒϱòОӏһЏП˖ЊȠΒʓРϵɽɂ',
                                                                            'Ǔɏ˽˗тΡϦǔΞǷ\x9aˆ9άӳҙĒʈȊ\x8a҅ѫʆҹӥøǳɳŖÒ',
                                                                            '<ͺʵkǯĸͿ˧ŧêЛ\x7fÎƏˮƊßҟƽϧиШƗĆƧԅŸͺʯҰ',
                                                                            'ӛ\x8fϭʶѩ˲ˍŦʋd\x7fԖ#θԅžɀ@ƌӊŻδѴǾБǗˎ˝Ȁϫ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƷҤϬѤѫȓƻμрTѤї¸ƚǝʐśäĐѤӇӼӵ҂ȇśģ\x83Éē',
                    'message': 'Л\x87ύUӣŸæťӎ˪ˀԛзвC˷6ζԡλ\x9bȕŅȗ;ЂԒҝ+Ƃ',
                    'arguments': [
                            {
                                        'name': 'Ȓ͵Ûʹɩʓ\x8cʩҸɶ\x96ȧþäωԒ¯ҵϲɑәҕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'UƀȚɀѐбyϖɮų\x96Ϝ҇Ńñêв-ϬqȑīĸëѼɋ³Ӛӱe',
                                                    },
                                    },
                            {
                                        'name': 'Ѱ˸ҶʵТňŒʦˮ£ҖюˤЦҔɱЃìȮԭǗŘңeͱ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԩʻÐě?њ¢ҏƮ8ǡͿƸϯÊβҌŵÿ˟ɑϲґʜЬɁĝêϜӕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.271587:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ȩ+ĥ~\x8aєθәȆɞӺȋÅԢğϟĀΪƨAĤˆԡ1Ŀԅ˒ǘŉ\x83',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƝČŷм3εΟϱƺíäғөŏə+ĠÖȒϵи¹ϠҦê\x80ʚңǑТ',
                                                    },
                                    },
                            {
                                        'name': 'Ԧʳ½ӤoόS˛}ʭӑН˪Ӫ\u0378Ҫ˅ɞƳϧx\u038bǁɥȫȡɚɞǩπ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 260643.9684601486,
                                                    },
                                    },
                            {
                                        'name': '\x81ФĄõ˯ԛʢöȣʧҚŀ\xa0ĄяΦ˹Ӟɺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԒΦǷǱб˘ʎѭӋЙӿʒԋѹ»ҹ˅ѧѱdԇԇ×ѱrƃõáʣɢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1187684096857546708,
                                                    },
                                    },
                            {
                                        'name': '9Ź˻πƠƎ',
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
                                        'name': 'Ҝ÷ģĜȑýϰ¬ђƇɁʛԥņ=LxĳŊ˵ԫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.273068:+0000',
                                                                            '20210228:024604.273095:+0000',
                                                                            '20210228:024604.273104:+0000',
                                                                            '20210228:024604.273110:+0000',
                                                                            '20210228:024604.273117:+0000',
                                                                            '20210228:024604.273123:+0000',
                                                                            '20210228:024604.273129:+0000',
                                                                            '20210228:024604.273135:+0000',
                                                                            '20210228:024604.273141:+0000',
                                                                            '20210228:024604.273147:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x88.ʋ\\',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.273457:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': ',ɎɢԌɊ/ŹȣΦKѬâϞʽtĘTƈˎԊяҥLӔԛǬĚӤƎĤ',
                    'message': 'ө϶ȼçх˺ΛŊƀŹȳNÚǊ҉ɣуэʓеɣȮōӿ\u038d¹ԑȚǵŝ',
                    'arguments': [
                            {
                                        'name': 'ΌȡӗǦĴÿҞϐ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԍϑÞęĮɖѿҍЂԭˢȃԘėƳ"ŇʙƮєͿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.274292:+0000',
                                                    },
                                    },
                            {
                                        'name': '1ϧƐĂ\u0382˸ÅРʣġ/$\x8cӨƯˮɫ*ԡSьɳ\x81ƪ˶ǜя',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ѩɵɛƒɋƛ\x93υĸˡϖșƻӾɝҸŲƎƸҜʦjȌ˩ƂҕɏѿŠȎ',
                                                                            'čҮͱ˼ɀĖƸȕ˽ȘǌΕңιìˁϹȵǢɪђȭ×Ӏσ˻ŠΌ»˓',
                                                                            'ЗȕТɄɈθʣ_\x99ʹȻ<ҖʌyqͳǗ˫ǎũІȋ˞ˠЮ\x90ƋПı',
                                                                            '¹ϦӉEӹԀғƫǗ|ѯnŤɂѐҒE\x87Ʒȥħ\x85ǲ˜ўxʃƜŚǦ',
                                                                            'ҩˆķϾ1ķϔǮĂɆęńāƘõVҘѥCҩƮϥɁӐ1GїŐ°Ç',
                                                                            '&˳ʥĤɏ\x81ôч\u038d>҄ЀȆҨɽȬ\x90ΝљͽЌԨΘǚԅΎ҆ȇˁӸ',
                                                                            'σ\u03a2ƛúĘȶԅ¿ӷɫç΅҂˜˚ҖȏǝʯǗ|\u038dǡҤčˡŒ˗Ќ$',
                                                                            'Ƅʒѥ΄®\x8aˌΰ҆tʫԑzͰƾҋ\x96ŴqϼƅPɗəäŨğ¡ĭʧ',
                                                                            'vͼѦƄԔ\x83\x81ļʬͼȎǈɇʚԄńЌҙŻ҅ŋӹȇЋʄʎϙĔ\u0378ɱ',
                                                                            "ш\x94ɾtԅƴűʙӦWĻ\x9f'ʳʕȭЩҷ\xadЯҩЮRŚˀԛЮĹįӇ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ќŦŔˇí˷ËϊÇƛ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.275226:+0000',
                                                                            '20210228:024604.275248:+0000',
                                                                            '20210228:024604.275256:+0000',
                                                                            '20210228:024604.275262:+0000',
                                                                            '20210228:024604.275269:+0000',
                                                                            '20210228:024604.275275:+0000',
                                                                            '20210228:024604.275281:+0000',
                                                                            '20210228:024604.275287:+0000',
                                                                            '20210228:024604.275293:+0000',
                                                                            '20210228:024604.275302:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ηϨǿӢΩΑӕЊӌUCӶҫmɇˈ˳\x8e˷Ź3ȷ\x8aͱɞȼя',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            740454.494606341,
                                                                            743699.0456310674,
                                                                            935535.5902195254,
                                                                            885331.4072777372,
                                                                            678084.0243684769,
                                                                            477664.9546702736,
                                                                            653852.0318148688,
                                                                            658311.650140637,
                                                                            799449.7301475712,
                                                                            10466.636615822892,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Αµ\x85',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -95293.0612342985,
                                                    },
                                    },
                            {
                                        'name': 'г²ǏѼSÆRc҄НВüĞǧʒҐхqČʪƩҬԂǷҼΠúЮhΟ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.277191:+0000',
                                                                            '20210228:024604.277239:+0000',
                                                                            '20210228:024604.277260:+0000',
                                                                            '20210228:024604.277279:+0000',
                                                                            '20210228:024604.277299:+0000',
                                                                            '20210228:024604.277320:+0000',
                                                                            '20210228:024604.277339:+0000',
                                                                            '20210228:024604.277356:+0000',
                                                                            '20210228:024604.277379:+0000',
                                                                            '20210228:024604.277400:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'дҒɽѽиП·öůΏӯŁíҧ\x90ήÿˬĆέƝuůңÇĮĶʟÞԅ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5919152217892567523,
                                                    },
                                    },
                            {
                                        'name': 'ΥϠƌǸËĈҪЗҡιϕò',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'чȪϝŷǘĜĺ\x86Ұ½ŶȯҴÆӬΡΛɘҍˆ˅ЧSјȣȎҡˌƗԠ',
                                                    },
                                    },
                            {
                                        'name': 'ͻǷĞÜʾ{Ӟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -818539828141679482,
                                                                            8867197673472935542,
                                                                            4668012957789422500,
                                                                            7436909230504984746,
                                                                            6084746289243699336,
                                                                            -2638109880135890667,
                                                                            -9057470281117579702,
                                                                            7603598162343133434,
                                                                            -2586985230214115709,
                                                                            169297814235907730,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǮЊʰ>ÒȉΊʈȡї\x827ș2ÖʕŶѭŅȴʛƫÛȟҞǢ\x8dȗдӇ',
                    'message': 'ўXɖː\x83\x87ίÃΊɸϖȌåǟˀ$ԂǻĊſƩŕӘ\x9dӻGʂϙгԂ',
                    'arguments': [
                            {
                                        'name': 'ΒͱӭҊɩѨˈ\u0380ŚΚ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2369622307579067524,
                                                                            3323868186770516146,
                                                                            -5570314130704265356,
                                                                            4079866782338735065,
                                                                            -6870632835831137292,
                                                                            6432618520012938570,
                                                                            4490003937438725289,
                                                                            6854581522925318350,
                                                                            -9197320307322875481,
                                                                            7891628153803228584,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǲ\x85кϱĉҢɏ²ƧӨ*ŨɇʼɧӉќŎ}ʏͻ^0OҘΩƣšӘ¬',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.279705:+0000',
                                                                            '20210228:024604.279734:+0000',
                                                                            '20210228:024604.279746:+0000',
                                                                            '20210228:024604.279757:+0000',
                                                                            '20210228:024604.279769:+0000',
                                                                            '20210228:024604.279787:+0000',
                                                                            '20210228:024604.279810:+0000',
                                                                            '20210228:024604.279858:+0000',
                                                                            '20210228:024604.279867:+0000',
                                                                            '20210228:024604.279873:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'αҜɶѹҿEȈÑƵΎҲćλBѺȴ`r\x8fǜĘӟŕό¨ŲҷƯƀÜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.280186:+0000',
                                                                            '20210228:024604.280222:+0000',
                                                                            '20210228:024604.280231:+0000',
                                                                            '20210228:024604.280237:+0000',
                                                                            '20210228:024604.280243:+0000',
                                                                            '20210228:024604.280249:+0000',
                                                                            '20210228:024604.280255:+0000',
                                                                            '20210228:024604.280261:+0000',
                                                                            '20210228:024604.280267:+0000',
                                                                            '20210228:024604.280273:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˇȝӋŽҸBˑɨˋǤüĲƨÕǖʣǦеƩȄͶμ\u038dťҀʦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǿЄWДƢƘˉľˍǎñƩԜϼȟɳӜũӥʾŦŇЛB\\ȩӷ×ʀ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЪƒɫҝȜȆłÁȓϖώόɇʶ˦˧ƥԟӍђ˛˶ӱ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'М) ɿЗĿÙʻԄ˯ԜEӽίңğī·ӉȖʓҏɢϦƖΐĪeÎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            357151.5161634503,
                                                                            627403.1198849003,
                                                                            590470.1966765139,
                                                                            448085.85682942346,
                                                                            -75037.80106057395,
                                                                            -9876.059831566672,
                                                                            430914.6944853428,
                                                                            45953.627610294236,
                                                                            555364.4588695875,
                                                                            247248.84803722607,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʤӅï҂ϫƂŽɛxƓâʑƮʩҴ\x98ЩōȝӣĖȢɢǜΥҀԗƫǥ˙',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ËŵΠOƄ\x8eӻɠʑ(ϢʼƷȮˆǳŴȈ|ӐǻčӁɶǊəǸ0ΨĨ',
                                                                            'Ӱʲ¿ӗ˝ȪÏ¹ѲʿZ˰Ҋ˓ğђʻɖѳѰϒ˺çԮvәƚϊōε',
                                                                            'ΌÎˍ΅ďΗȴǮʺϢōɕơʵҗѓŰ9ҁʫ˵˩ɇɕ\x7fĢªӑǂү',
                                                                            'ȬͰһҝŻcǁ˨ʡҋПʀΊԮĸЏǠγӈяҊÉԇ9ԩʴŁRâř',
                                                                            '*´Ƴȵԫÿɴųɞʵǧő\x7fʙΈǎ҆ѶƭѕɮʱʊŅðґčȑҷϢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'РĐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.281993:+0000',
                                                                            '20210228:024604.282028:+0000',
                                                                            '20210228:024604.282036:+0000',
                                                                            '20210228:024604.282043:+0000',
                                                                            '20210228:024604.282049:+0000',
                                                                            '20210228:024604.282056:+0000',
                                                                            '20210228:024604.282062:+0000',
                                                                            '20210228:024604.282068:+0000',
                                                                            '20210228:024604.282074:+0000',
                                                                            '20210228:024604.282080:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѫĺʐ˭-ӶӠЂЬϪӫԜ%ºȺҁѡԥɥǘȑǸMϱБä˵ϖƕ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ĸЫѓšД',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ΥҶ',
                    'message': 'ӓ',
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
            'name': 'țOɤˇҁԘľƛʹћɂӌ2ԠëąȌы˜ɪȃєӯԊ#ƹΕį7ĳ',
            'error': {
                'identifier': 'ȨHҦȳҽ@ӓƱŅńŢѳ`ȟѭӋˬϚĺԦȣŇǞ(ÈϺʈȂ»Ή',
                'categories': [
                    'file',
                    'configuration',
                    'invalid-user-action',
                    'file',
                    'file',
                    'invalid-user-action',
                    'network',
                    'access-restriction',
                    'network',
                    'invalid-user-action',
                ],
                'source': 'ʎɔ·³ŷo)ϩĸˉҮҨλĂҹфӤɀǞƽ˾Oɂϕшȩљχşρ',
                'messages': [
                    {
                            'catalog': 'Ϛͻ·éԭЕ§˪ɳƻʋǐЃҍӦčǷы˥ќ%Њϱ÷ŜȞÃԔїχ',
                            'message': 'КА\u0380DŘȗıϱГӿĸˈӦƙч<ǖřԚöјƶűŬɔ½ȔˁПч',
                            'arguments': [
                                        {
                                                        'name': 'ǉЍ¸ƯťHɐ\x86ʶόŅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǆϏ\u0382ĸȚƑәɄʎқȔłɻθȀƂː\u0378ˌɫϴ]Ъ΅ɒª\x9cƀʊɳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'α²Ưπʼӭ˰ʃȴĆԖӶ˴Н˦ËѱʾԉǐҤ\x82Ř{ǥäϗȤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЂԔĄ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӱ˦Ў˄ÖԅŞȅϒҰϮʏˤͿԑƇ\x9aȣÖȲҵȘмШҦ¨/ԑĽ¸',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'q˃ȀĝƓȋÍqγÕȎѸaфǃȕʴĒǕҔòφɸϻΒӣЇΧ½ѣ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 108534.8036334673,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӶǩɕԧʠǵÐȟԐºЊΔƓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΌȠӣƵΖύ$ΔКϢǶʔˤ҂БԄɗЄҏʼɖɠȻˀоúĳ҆ųʵ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Őӳː,¥҅`»йƐϢӛΒ˖ÃΦʗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'й"ŶҨǃӆxžďҋ\x8eðʈʢ±Ç',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ģΟӇŐѿʂΡ¶EȠùѵŘϳʰĠҘĎӞΊʕť4єҦԉȰóǊƜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5333357756647499322,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҀƫǩYӲʢiēɾɿϓ˯ųě˒ǘɪжϽnƗͳ\u0383Ԇɖĺ\x99óӌȿ',
                            'message': 'Ȥ˪ÄϻΘүӝX»ɚϬϣS$ˮŊŌɒӡ\x86Ŗԥʣʹʸ\x9dƌGɥƧ',
                            'arguments': [
                                        {
                                                        'name': 'ҞӤʻœѻΆ°ҭӥXīʚ«ǥʖǃ¸ˏÃhïҟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӂҚȰȷɂʯʚ²ҎҼԣѾʏɒùĀ>ˬнӓØӒˣɾĩϖ\x83',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ȼΓԢЫ/ѓǐ'țŸÍӊLӏϺΣyϵɎȧûХOĥφ4Өʿ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'yЃοο˨ƖˇγєƗЏѱΙȧ˔Рζɧɾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŧȲÙГ§ΎҝђŮ\x88П\\ɝНΏəʨ`ԃǗѩŌʚV#Ȏΐ҅ʥǒ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ěʺȕ\x9eӄϫʙҕҏȆЯԡ\xad\x89ǳА2ů҉âŁĵЫhƴ\x83}ǎƨ\x91',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7365639441199383627,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ήǧȰ~ђɽѴӁ\x8cĜ·ȡs˝Ñĭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.212949:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍӗ=ɾɞϓʓɝωĊȝċíɉʪЩʔϛêӡųǶ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǿŅϨԨǏąǖģүϙŎ3Ъ\\ĂIиˤͲӘ"oЌŻ+ӆϺȟӁd',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ˇ\x87ҚǊϵŵȋѢəҚ7Ű˔ϳƉӌźѰϸ\u0378ћӕ҃ͶǙȘҲ'Ĩ\x90",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӤƌјǓ˫ҁ ĵѠǏËŢϺʕŗǹ¤ԓҥԐőƉWЎķɕϔïє¹',
                            'message': 'áƪ_àčѢ˚ʻȕȕԏƤшϮҞσ˷ӈ=ĎӵҘΰCӵϚ\x9eлɗß',
                            'arguments': [
                                        {
                                                        'name': 'ҹ}Ѻŋɔʸ\x98ӱƘөԃӡ¤ȏ϶ɔȉyŻ΅ҏǩǷЃҾԭŅαӀú',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐу\x8aFӬʟ¤ǦTԠʨҜρϨѾmĹ1\\ʆʧô',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.214472:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѰơűБĜЯΪĜɣҭǶԂ˵ԒǐǃWȢʹȴūԧ˲ƺēì\x88ƞŴſ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '҈ϓuĵ˹ɝǩ\xa0ËŭȶʓŇϹ˽\x98ǺĠíȳɿɞǀƠңЋàɩҦҒ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŝŷǪ\x8b\x88ξŃâ¢ϩԎȋǨӓΗʲҲɥһǐΌɍϲԉĺ\u0378Žǥ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -654779840597423134,
                                                                        },
                                                    },
                                        {
                                                        'name': '΄ÆȮÃУѾϤμ¡ȽŉіÏӣÙŊШê˝Ц\xa0Αņù˧Ý҂ιƝm',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.215094:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӇөkӃ#ƣ¶ʴÝ6ŹǋӓѸхh\x94yȰπСɑ˃κŃ˪ȸ\x9d',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǒҖɔ҃Ʉǒ˜ʘǱӅϸƔƹӔЦҏįûЇеƂǥˤāγ\x85ȋjÊ°',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'OQķȟİĤ҄ԁѝɳӗǦЊϷǱԫǀʹXҎĕå°Ƃԝ»҅ǠуϦ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑĒkѼш\x89Òǯ,Ǜ˷Ȏӭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɆŁȭ\u0381ѝӒ#Α˸ӝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ҡʮ\x93ǼʙÎʮƠͺǷʖӑȊȔ\x8b\x84¹éЕ\x84ыȵǕҬиӭӾƗļʩ',
                            'message': 'ʇ\x98ʿǴζʝ˧˪Ɠĩ¬įԟʃƵСǟ˘ґԗƤƑіŅɑ\x8cƈŸмɞ',
                            'arguments': [
                                        {
                                                        'name': 'ȭëƏЭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'áàмӟ\\ѷȧȃΫķɥѲ"ϕɚ&ʍʴѶƋƷРą¥ÞXĈѫðк',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԇʣũӈȒ\u0382Y\x8aī˦qɄ:ǫɢǏňȘɡЕ<Ļǉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŋpӭĈȜԥþҩdӌʒʻ\x8bȃѺǥǥā\xa0Ò`ǠҏԂϦhѓÀ|æ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛʶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.217340:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳT]ϲȄÃΖ´ҊɭƂɇӿ˛ԡʆWѾйə³Ư%гʆ˽ϻґΗǜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ķǻ¯\x89ҭȒµĤɈ8ϱҘŴйƃѶЬɴ^˞ƇǮ5äҒ+ƍȋ¢ѓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҺȠǦŜЌϺΛϪїϋщҎɩd0\x96ʪɻÈţƮѕƥДӻЦΏԛBӟ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 754173.0624073287,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϙʹЯЃ9œʹÎÖэʤÍūljҡӨĵ\x80ӋʘƢԬώϠƐɪÑƘӗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫλԎƓЇŁ|Ѥ©¾żʈŔǁǵΐəƽҙʂАƅҦɩȊNͽµǠѱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑӑˇȃ\x8d\x86ǾęȿƮΏζҡŐɶӡ˺ßϛŪȻζ\x889',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϮˡʨѾǞΠȂăʧũӤȫÀҙŻσ˺˄Ƒ҅ɝε˔ǀА@¶ĩ\x9cŇ',
                            'message': 'dÆσȅтŜɁɵÊǛϻ*ɜƞƢҼϘÓ¼ȘƈϪĞҏӉЦȞˤǴķ',
                            'arguments': [
                                        {
                                                        'name': 'ƇƗʐӸʯƍáȟԬÿ}=˼ӃȄ¬ɹѓÏƕҏʭɋǍėʝũӺʡѸ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9162633328665461418,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŘśǃƧˑˀʀǦʥҙʩπԒġßÛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.219353:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϬҷÃѦſʦ\x82ȅƞGŬʐЅЃӸĴ@ȳӈ҈ѨӫɌġΟŇȯũВʍ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -461936089335154074,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ZʪµѰ¥ӋЕ΄ħūèӦƮњЬųàÑ4ƚһϬΩR¢¾Tӏϸȸ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʻёΚŲϲ\x9d¿ɉEǿȪɄƿǹŶ{ʔиё˽ǣF˵ÄŐӴϬƏɣÝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΙαǩΛȔҭ?ơ=ʊʊɓӣϛȕːɯΔǼАțԖΙ˴ǞȞԁVӌЏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'aжҀԡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'όđō6ɌƊињÆιфƷŠĊѣǺ·҄Ȧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 603791.4139679262,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dϽŠзгѡήЧҙûɍˉĨǓȕŦϕǏǺǁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ơӪɈͲ϶ЀȹǋЦϾ'ƑƥƦķzʴǵȻԛȆЊρôӊβ\x99Į\x9eû",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϡÔθ*ˇĒӴǝϭϑºȷ(ҒԎæʹˮʂBœԡϱʉN˺ſӀ˖Һ',
                            'message': 'ƯҜӇɕͷԌþ0ƜӜ(ӔгίǞԒɷȺɮЋƷ{ҍ˙Ǒɘſ Ϭʒ',
                            'arguments': [
                                        {
                                                        'name': ';fƸńӚ\x9aŋ*Ȃԙfҝ҄áϪϳʛΧŪ×ѓȽϛ΄ċ3҇ŧɽΏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.223003:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌȮ:ϫÑčīĺŅ;\x9dĹсĘҳӊ(ć ɣǮƑ\x8dҭƤľȪӳқӛ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ż',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÑʭȷиѻϡϭĸʊӎNȇͲu®',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ςѥɕäxв\u03a21ĒƶϻΙ\x95ύű³KЉϛAЧŻɻŵѦˣɻǒħҮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 403667.9257577576,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ť£ӭǣȚPƊKѕăҥǾǿî¬Ǝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8985188143157915587,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂ¶ȭŇŗˉ έ҅ǎÿ¶ͳϡ¾ȳńʱ\x8cɢʃϝˀǧʪǥŊϿɉ\x80',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑŨΜȕQȷҵϲʡȢƲƃҐʁɖԍϼ˪\x8cĬ˩PșȣѺϮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 56608.282785733696,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΘӠÇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƔuÞ:ӈѶwͱǙưŬҖƊ\u0379ƮUԥπũʿȷѻ\x89ŃŠǙѸș\u038dý',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϤÌŹƩїÚԦɘHєƵЛ˗ҒɕΡҨԢǥԛŔŇҾμƾԮȲ\x82Ѽȏ',
                            'message': 'Ŝʨ˺´ЛƎÙәўŢ\x8aҌǝǀȧƝ§πҥ˥+Пԑ˭˚ˌʁˠ*Ј',
                            'arguments': [
                                        {
                                                        'name': 'Ȧțh=ɥŇȓ˖ɽѐːÑ˲ЯɇɁƂ»җʿΫˁќиξϋВӖȒƶ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'źШƔɟ˖ŕПУɄɼ]ŒԒ˾˧ȅѧΐř',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -367336848882384006,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƀćņΕΖсƘÍѮρ"ӐȌɑéFΉЧ2Eχьх\x96ϿȖЏ]Ί\u0378',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԔÁЁҶ˔Ӆ\u0381ÂϓϿßǹɫĉ«ȬͺE\x81θӠԄԌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Җ\x8aŷˣӒЦԝźɬŏÇÔʷî¡ӸԢŪYϡɥĶӮГVĈѶЫ˥λ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻČŋϭҿʡ\u038b²Ѿ§ʯĝÁƟȿa¤ϖЯư΅ЎáʃøЧƯԞ^ā',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѤĀȅɹӷ¢Аŵ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹȾɪʟҏ\u0379ҞЏũҺµԥȂΪñιɥġÚʌԚ҆҈ľ±ɀ\x8eҮƢʟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǷƛαÎƮȉǪҢойһ¤ԉȷZȫҪ\u0381\xadӋ҃ϫʃǗҳЖӣŧpΗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҒѿɐӒǀ@ҭ÷ď\x90ҙŲҤĲǱȸUƤQқɽŊȆӁ¢',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '4ŏШǒɸԑԔɏϢȟŁ\x9dĲ\x9fєəûҺPϐ\x91À˃ϿδčƬʙĴԙ',
                            'message': 'Ǿгʞ0ЈԒÍȧаɂԋӶ\x82\x8bңԋТȀҟӕя~ĶƒԦȦȯЄªʼ',
                            'arguments': [
                                        {
                                                        'name': 'ʠ¢',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņŲ£ƥҵzΨ\x88ςӮ&ʗΏ2',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ɍʝϝİѓ¼χÌˀȞƛĥІɜҌ>ϝƶԢԝkƖɢ˥V˃ў˥ѐȨ',
                            'message': 'иƹǿı˧ɁǎhǴDϵє\xa0Ӧĵ˚Bϵ˼ĂȘƜͶȴrѝƚԇέ&',
                            'arguments': [
                                        {
                                                        'name': 'ηд\x81Љ˂ƮőȎАјƖsӲ˂ǋθˉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '"ȶ˧ɐѰĀ҆ʕŰΈ\x9bʫЖӃʻɎɣҷӣΓҖʴЀŝǕ\\¥ҏћ8',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΤзϔДЊ҅ƓԡʸϣπĴĉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĞŨѬ΅ʹʯͷ\xa0',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 186980.95905263117,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ũ˰ŀӭ\x80ʹʻԛӼǧƢįϏβθίó<уĦķňӪĝϽЕӬΒЏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3624556019821332589,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĢʘыƸθ°ɐΦĮԬӰΥø\\ëЋɠƷĥҝЬһɱέɅ\x8d6эѴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЯҜƯ˳ʩǘĸʣɽǾŠӉӻǉɑȿōʳĺƒԘĩÁѵф҇zɌʦʡ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŗÌ\x88ͼmΥʚ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѦѥӸɒбʬVѫӕҨĥͶ\x93ʞʓʌʓёҙ˰ͼǝȷǮʬ\u0383ƱͼȤǊ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҽ¹\x96ЭɸʕơǊOƏȹżɂΐϖĿɦɁǍǫƅΣÇǚȝʥŬмʑѯ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 48300.918459017266,
                                                                        },
                                                    },
                                        {
                                                        'name': '²ȊʘȮГƊǕʘԙ¼Ǵn˃һϸɉŮÇɭԤΘеɡȃÄұɋӖȜȳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 507271.0535477578,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '¤¢ǅŮƜĔʒżΌδƎӱϭҵҿјĺƼϽѶӳǒ˅ћǤ9ˈŲʇN',
                            'message': 'ɱ˩Űʭ˧ÏЫǍƉʽ(:ԦφƃнȤ˃Ⱦɂюǵѐӆ҅ƷΙα˖ɏ',
                            'arguments': [
                                        {
                                                        'name': 'ɺН',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'à',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 393070.4126609176,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻΉąĒϽϏԌͳ΄IËΐϻѻȅ\x8aгϢρІʪӏ\x81ј@ɥx%ϓ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4845044571466934528,
                                                                        },
                                                    },
                                        {
                                                        'name': 'тŅ±²ʶīϟҺ\u03a2ʈ»ԁDȯѵƣɗзƆ˻ȝPԪɦƇҫѾȒчǤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˶{ҟȐɵҏʳ\u0379GР(\x9eαȧ˚ǗʸҙԀȍЋ\x84ƸӉф³ĊX',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '÷ƱʏɭҢˋǏŜң˱ő²eʏȊ҂µјϽ˕ƽŉ˕ɔӦEɟԋb',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Λ҃šԂęԂǁķďƾNˋ˹ʢә\x92λȢʙčϢǴԓÊӋȱҔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƾvѓ\u038d˻',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȵśĝɗԗˇˎљĞxȇ\x95ͽҨ\x80ҤÜƘĬÅУβ\x86мˇëŧԦ\x82ă',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϖƚӬǴ?μЫ\xa0úύҝЮeĆ˵Ԫǚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԖԆΰ҉мέʧmŬȷ',
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

            'name': 'Ӹϗϙ',

            'error': {
                'identifier': 'ļ˩ǨɪŘ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'åԈ',
                            'message': 'ӥ',
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
            'event_id': 'ԓѤ˨\x88õǤŘƯľҋȎёԆĉԪǷОԒ҃ҕЩ¨ʯЌTӺ\u038bȆѣԃ',
            'target_id': '\x9bӫÔҬ\x9cԂŻӖʴƷЅƜːƹƿĽʅҊ%ԑĿæɑƧɹǃśϫϳҹ',
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
                    'event_id': '˓ӍӀԞӾ͵ĶíǑcʿˏƇŞñЫğƶπԔĹϴŒӜƕć˶ĥČǰ',
                    'target_id': 'ˇ\xa0ѲŷΞƜȷ@\x88UÌԄЋԞӐƕѡǜԝќȷWѽɏóԖѲӵŶČ',
                },
                {
                    'event_id': 'Ń˙\x9bɯ:tȎĹѻ҄ĶѵғC˟ćȱΰģ˻ѭÀ§ŔӋ˲ʦƐшĮ',
                    'target_id': '˾ɜȕƫĕΤfǴЋҷľӴЎƭӰ˓ɠŦɻbƊǖǧӥÓ˜ө˲țǎ',
                },
                {
                    'event_id': 'ɿı*ʾѨȑ\x93óҾɅǢXǛ¶ǵţҲƓ˚3˘ЭËάˀØĽΗҡʟ',
                    'target_id': 'ϐɼƛζțοïԫuʏ3Ͻз×ȄĻɱѺĂƼҭҴtιϘ\u0383ȅȾЃɵ',
                },
                {
                    'event_id': 'ŚӊԤ}яȼxЯΩ$Љˍɡəʰǉ\x9bɧɋÞӨ@ƌƝ˹ӋΏÚË!',
                    'target_id': 'ˀʅ\x87\x92ѐƵĉ$ѽɏѫ©҉ϐԩǡұʪļτɚƗ!ѮǲƜԑǣ2T',
                },
                {
                    'event_id': 'ɸӣαfҩŅȏԃȢϖ|ҔȜ˸ɷӡћĳ\x9cԣƻÂƒ«ȏϊɦ;ȽŎ',
                    'target_id': 'tǡȺԏεŵǻŨοƦҟɰÑÛǖº\x9fƘ%¾ȔɗѹȃϱЛËVӓΈ',
                },
                {
                    'event_id': 'ʥШӓЪԌϱҺФϙàǙ\u0383ĶьŲӗԂ\u0379ӰκН˱ʋŉŹǋɳʂˍɜ',
                    'target_id': '"ʀ\x96űÿÀƣ(ĉɔҏɬ',
                },
                {
                    'event_id': 'vϏӇΉǡłŜΚЃʫΨφ¸»ΕČПƋѭƥɬӮǺʢӍȉқǞѩ͵',
                    'target_id': 'ǓˬɿÿͲʯȗ,ө-ѮѥӻѻϕТӛӖƓðȓԆgɡȶȠT\x81ɀĘ',
                },
                {
                    'event_id': 'ӾΉʭʜŞӝӋ¶ΜɽϠđƭǻоżƕөcȡȷ½˸5ӍБĺӌӤʧ',
                    'target_id': 'ԠǛЩ;љЏԪӢɂǫҔӳŎɧö˔ŁȸÂȞšɲ΄əȠǙĐƎ,ż',
                },
                {
                    'event_id': '¯vͺӀʕŲζ«ȯǁʶàɰЩԃĄɃüȌŴɦʹťϳfҞψ҄Ӱ҉',
                    'target_id': 'Ҥ\x8eӖКͽȋƺӢUͽ˄ϒ҄ЮѠϭɾɄČȞÙѩƕƽǖɢѪ˥ŞЄ',
                },
                {
                    'event_id': 'ѥԗϘĵQљŐɵӹʢΩԪӜʡζǖșǐѷ\x94Ťª®ԉȗɽѕσЎɓ',
                    'target_id': 'ϱŗԤӼѼƊҴѩ¤ʎΥpϐÈȠDИҏӥ˶ȡÏǀ_у_ИϥȚ҂',
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
                    'event_id': 'ʿыɅίη\x86Ιӵeҿ˩ʟϬɍ\x98®\x86ŔÉϣąҹ1XiϾӺVΉǀ',
                    'target_id': '«ӭ\x8cľȇџӥϘƴ\u0381ƽϢʣ˸ͳƑԈǛ\x84ΨȜΜ\x996ƉƳɷŴпǠ',
                },
                {
                    'event_id': 'Ͳ\u038bΟqϫƗEайʥԐΉΦΤəР\x99÷oĈЩψʼԉřϨdϛʆі',
                    'target_id': 'ˣ\u0383ųҶԜВSͽ·ĢұīĴđƦʦʣϻӆχҶӗȇÞͰӎέˌƽΏ',
                },
                {
                    'event_id': 'ːχɪͺɣϏȴ@ƯҖҕШ͵хѦѡЧϨˆĴŐ;gƽӃԔȌ\x98ǅƳ',
                    'target_id': 'рǰdϼԇԦКҢϳ_ȄːЦ҆Ż£qΰȁʱѩϔÉЕϞƔҒ˃ƦϢ',
                },
                {
                    'event_id': 'ķӿ0ξǧɬ4όӁǏӏ]Řʨ˥ӫˍӸŅͲƚ¿FӝȜͼÒфԃĸ',
                    'target_id': 'ӬχѲб8ͷбǧΘΓшΨғðĪÐ8Ҝ}ŉʱЁ҂ͱҴǖҲŋĉˤ',
                },
                {
                    'event_id': 'ԚǰϺƒŅҝϸŨɽʜԞͺßЃЩ(Õőǽȴ·ɟɺǊӀβҲʇҐĹ',
                    'target_id': 'ԓtgԠϢƋγ˹ȫˑȬQӻĈǼȼԙùkӗϓϋ΅\x84МʂԩȡԤю',
                },
                {
                    'event_id': 'Ĺ\x9cʂϤķԋӷЧӫȼœƞ~ŢɣƇʭҟˋĥǼ8ɏȨøͶŸ7Π\x83',
                    'target_id': 'fʫҳɈƀǦµҸ,ˉƺŹɤɹÂѫOŁШȑԛęʍÂȀŤóʇȷơ',
                },
                {
                    'event_id': 'ɸ΄Y¯ǎɦ˒ƗӼĢȄӿҹΠmƴƇДʞƛɏƽз±Ĝо˴řĠҿ',
                    'target_id': '˭ōԀͺқӠфƖϮˊҿ1˒ҊţσvӠӚɔѐͿǲ¶ԩǅΎ҃˾К',
                },
                {
                    'event_id': 'Ӷ¼˙%҇МëĦȢďѵİԍȑʆŻӳѦȒΑȠƞƋԊИԓɈǙѴǦ',
                    'target_id': 'Ɇ\x97ԚӤǸϳîưϽˢÈǖǸſɿ_ӦǕOӢ\x96ΨɌ˧ēԖƸȻyƲ',
                },
                {
                    'event_id': 'ɗpͺӳŰҦ¤ёǑƔˁμʚ\x81ήƢм˵ƲѯжčЍăМΥÚϷɼŤ',
                    'target_id': 'ʚĐβɇύƨԨWG"ԭĹˁàˠ³ԅƼЊȨӬͳ.ӭčȏ@ĻȌġ',
                },
                {
                    'event_id': 'pµʚóŨ¥ΜǌѿǡʓƚǚðпʆˊǃԝþˈƑŵŧӒĵƲɗŉԣ',
                    'target_id': 'ȐħƻȡPЕœɮMˋɕeĬƓ6ČϥΒʞњѩłъxе*Bхɜӯ',
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
