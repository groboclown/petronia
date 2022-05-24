# GENERATED CODE - DO NOT MODIFY

"""
Tests for the hotkey_binding module.
Extension petronia_core.hotkey_binding, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import hotkey_binding


class BoundEventParameterTest(unittest.TestCase):
    """
    Tests for BoundEventParameter
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_EVENT_PARAMETER_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEventParameter.parse_data(test_data)
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
        for test_name, test_data in BOUND_EVENT_PARAMETER_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEventParameter.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_EVENT_PARAMETER_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='key', name='BoundEventParameter'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='BoundEventParameter'),
            ),

        ),
    ),

]


BOUND_EVENT_PARAMETER_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'key': 'ºÊӤҫɻƎAǼ\x83¶',
            'value': 'ɴЇЦǪƵуԀͼȿj\x96ʱʇːŗɯ%ήƯǯőǦцřѮӸϽϡü˓',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ϔ',

            'value': '',

        },
    ),
]


class BoundEventTest(unittest.TestCase):
    """
    Tests for BoundEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEvent.parse_data(test_data)
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
        for test_name, test_data in BOUND_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='BoundEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='parameters', name='BoundEvent'),
            ),

        ),
    ),

]


BOUND_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'target_id': 'ýϤȿоҮğÁѨɀȀƖȊVąЮ\x80˟òοʌĆЯɳȰˢѬ҉ÛϩƠ',
            'parameters': [
                {
                    'key': 'ԮγüɲɸԢ\x85цōǜ;ɞʷӊӍӈεȮϺҶЙӨ~ϲÓӭæöЧԖ',
                    'value': 'ȩƇΠM˙jєǅљ(ǒȞɛ Ϭϰ«νńΖØѦӃЏĬ<ɲǅѰƾ',
                },
                {
                    'key': 'Ĺȵþ͵ǘĨÓӘΕƞѥÒŦǙØŀώΦϡЄϽ´ȑϝ:Ȧėʨӆκ',
                    'value': 'щÒԙƇɰʟ9ÕɶeoɲŲšKǹϚǚѦԩƞҥSžņңўԞ˙˝',
                },
                {
                    'key': 'ƒ:ǝΎʆǐ΄ȌĈTȌGͽYƺʕ«ĜȕºӲПɛԈʿǖΟЙѬ?',
                    'value': 'ԐɂϬĊӼΎ˭ҊχȡǰŵџΤə\xa0Č<·щϖ¨þҫĂϮIҼlË',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ʰ҂ƣʩb',

            'parameters': [
            ],

        },
    ),
]


class BoundHotkeyTest(unittest.TestCase):
    """
    Tests for BoundHotkey
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_HOTKEY_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundHotkey.parse_data(test_data)
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
        for test_name, test_data in BOUND_HOTKEY_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundHotkey.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_HOTKEY_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='BoundHotkey'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='event', name='BoundHotkey'),
            ),

        ),
    ),

]


BOUND_HOTKEY_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keys': [
                'ҭϋŒˍiŊʔʲ´ˉ\x8dӊœ˧ʯŨŴʩĚʾɲѿ',
                'ûԋшÙȤìRʍʆƏɪŋȽŹѷ*ġŭƈT©ӒɰĜѪµĭ',
                'ətԗШΫ\x95Ӝǳöҫκ',
                'ΔӞǧ±û˙ˠΒʖĒʂJůǗѫұƳÝқɃ\x8eԍξϘѣ',
                '˚ΒÔԍLԡ`˫˓İ',
                'ϑȗӸЩЀϛʹƍǣˡȴŅũʏ',
            ],
            'event': {
                'target_id': 'ѩĥɏ¯ʋѳðθҟБƻkʖʑЁʚԌŲӇӲ\u0381¦Χ!ȧϣŃìɬʶ',
                'parameters': [
                    {
                            'key': 'ԏұϽĜȂ',
                            'value': 'ʻư\x83ĩž҃ϊжɅ˴oύϙ9әĒƽТèɗɌˢҳ˭ɱџʮĸšȦ',
                        },
                    {
                            'key': 'ϓҐʛǗŵИВɌŎӻȸȚǀѢ˖өǯΛҭɨˡӥÒŃŐҭӃűԫʸ',
                            'value': 'ЋaǝӂɪŵΊȾţ\x8cҳЙɌňβˀΚ\x90ҴӿыťƩӦҼ¦\x8b˳ʶ˹',
                        },
                    {
                            'key': 'êK·ǰіȭǨԖϩҤԂʟԣɢɧϼǾӹԘɱƪÅʢˍèÂСĳǊÞ',
                            'value': 'ɟл\x8fυČǥЂāӕ;ѣАɃқɍɮĘĳˎqǅ0DŴɻ˃϶\x9dζќ',
                        },
                    {
                            'key': 'ԀΝ\x97ǤδǔªĳүәϾͶҔɂŮWЙ®Хԗ˫',
                            'value': 'ЁԝˌƚȖƏϘɚCʵĲϣ˭ԑÎϹӭŵƅj¾\x82\x9fưЧ˾ŊAτɷ',
                        },
                    {
                            'key': 'ҲΞʽѲɡ=ʝéŴo¤ЪȞɃ\x81ҵĤӡӵƘʥŤԜθЂˊɲѡìԅ',
                            'value': 'ʨБƨȚċЇъǻԍɮԡě˒гǸ˳ȥϒ\x92ѓ\x9fŝϒљþ΅ ³ϸĬ',
                        },
                    {
                            'key': 'ѳĳ\x9fǩщɓςˢʬŧστMƁƭɵˉǍЁƮ·ȩѱŇԖ¶Ư͵\xa0º',
                            'value': 'ǲďҲũԃʎϢ҉\x91ҧʰŚʈ˦ńΧņ˰ƾʣ³ʪԤѵӥŇəͺɞɮ',
                        },
                    {
                            'key': 'ҮУǳʋ\x7fӸιαŅǐǔЉü˓ĢÝӴǩóǍӧˮbˁƜӧtŐӧҁ',
                            'value': '¯ɍϸ˥іԙҠǽΥҩӻɺiҺӾƶôđЪʹѸ\u0379ɢѧɌΏƧϨźҘ',
                        },
                    {
                            'key': 'ÚԚ®\u03a2ɋ˦ʷ^˅јǫχңpπԚƪϑ^МΕɷǋųŬíÍĶãɫ',
                            'value': '°°ҿŵǷɍԋƷ·ÇŎoƯ^ǠϷжϔдŌłŜǗγ΅ԍƢɫ&Җ',
                        },
                    {
                            'key': 'ϣӒƱ®\x89ʒƊ˾ϡԑϹѼѰö',
                            'value': 'ɾɔ\x94ȪDɧοøŽԮўcƦɢƸȷҙĕʜγCЃȏ˟ѫҜΈȠƍБ',
                        },
                    {
                            'key': 'Ɩκ',
                            'value': 'ł5ҷɶϠ\x81ΞҦ´ǭԚ=ρĂξʐҼϕÍΔĥҡԦȘЗǪĹ\x85ӌÜ',
                        },
                ],
            },
            'comment': 'ƂÉҸ˴\x8e¡чƙӌƈƄ FŻфɅɖԘӻûҢ\x81ψԫĳāԦΨϓϕ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ȃ',
            ],

            'event': {
                'target_id': 'Ѩ8ɣSŚ',
                'parameters': [
                ],
            },

        },
    ),
]


class BoundKeysTest(unittest.TestCase):
    """
    Tests for BoundKeys
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEYS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeys.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEYS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeys.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEYS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sequence_type', name='BoundKeys'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='master_sequence', name='BoundKeys'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='bindings', name='BoundKeys'),
            ),

        ),
    ),

]


BOUND_KEYS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sequence_type': 'meta',
            'master_sequence': [
                'ʪ#ĵĝµɈҰөzȦʾωƣοĞӃȀңӠh',
                'ҚéѶ\u0383Ґņțԇ\x81ϒϔǰҪÍĺԜëӰȾѩǎ',
                'Һ}Ń3',
                'ӸƆƠKҠŤ\u038b\x8a',
                'ʅ1¾ӺIçΉƯҏ|ԖʒӀ͵¬Оŷ҉ҟҍҨʙЄԒƨдü5',
                'ɝÞȂ\u03a2НįŰȰÎǱԩгєԈҀλϲӱŕԞ\x91ӽØȐ',
                '2ǚФǯ«Ϛ',
                '»ҏ\u0378ԮϵҌΤˏԊɒєӞэţɡпԡ˾Ϊɭʨ',
            ],
            'bindings': [
                {
                    'keys': [
                            'Әр\x9c',
                            "ƓѰԑэʴ¬tʮ'ŀφӬɸØзĖѾҦqʾǮ΄",
                            'ϊ',
                            'љƝąǕԌԨɫåŕ˞ӢöѼ˅ʬˣ',
                            'Ƥ\x8eВѽȍģ³БŭĉŴǣɦϖұʎӸі',
                            'Ėџ˒Ʋҧ',
                            'ŪǫЋÀ˄иưӑҲ',
                            'ҋ',
                            'ƭΤ҄Ӟӝțǹθ\x86ηŀӬϴǣѬʮƞSǙʦϡ3μғʑ§£ʆϊу',
                            'ÒʹќћԝӵśΖФʓ˕ǌɞӗѦΎ',
                        ],
                    'event': {
                            'target_id': 'ϿáƿЧйДаgβɓ¡ʴИΠ\x88ȗɹӗОϸµЭɁȺʲΙҊŹȓΑ',
                            'parameters': [
                                        {
                                                        'key': 'ļĺǪƏ',
                                                        'value': '˦\x9eҋҋӋԍзȟĊȅ˼Ϟ҂o\xa0Ҝɪ\u038dƟѫљѬƿҚɚʲǠѕĖˠ',
                                                    },
                                        {
                                                        'key': 'ŧŰʬЪďĤƦIßГϬͰɆƺƝЭǬR¨ҌϺΎѐӇĖʱΖǔƁˈ',
                                                        'value': 'ĲpЏЕahӚĪĖӺāåRϗʑǀɲȒĻӔԋȗ\x80˗ƣ±ѧķўí',
                                                    },
                                        {
                                                        'key': 'ҪȲԢЈΖ',
                                                        'value': 'ϐӛżΪ ͰОɝ¸Ȃϭԇǝ>ƴёŭҵŵѶΛΨщ',
                                                    },
                                        {
                                                        'key': 'ʥȏǦǜČ1ȐѼѣ҃сϧ}Œśǟɇȱ\x80ɨˤƂƁϺѹӞԦɰ',
                                                        'value': 'юԧҭЁɴ˖ɇėԓԞӧ˭ѥəԬƏҿжæǁ2=ȚΜӉҧύіǼѲ',
                                                    },
                                        {
                                                        'key': 'ǘäŘϚΥ\x8eŖȜͿ¾ѱѵķΗȇәˋkɜ˭ԃΌ',
                                                        'value': 'ŲϞЊŔƬ¥Ƅϑɿу˵AΧʜѲϴÓЉ˖˯¾ңɻԀɛγπҵœѡ',
                                                    },
                                        {
                                                        'key': 'ŏ҉ͽҼ¾ΒԤϓÄЏɖď',
                                                        'value': "ǛʊҹrĺŪĢ˲ϬúʷʘўʹҽĩԝΘs҉ҤłóÐƈȩϯҁȨ'",
                                                    },
                                        {
                                                        'key': 'ÇƬˉɬɈıԜģĈϔļėѼɎƶ\x9f˚КƵҀҢʦӑʝȓƯЦœ',
                                                        'value': 'ӀǔϴPԢԆȾҪ˻ӳȓϼ\x9e¥\x99ïĕ\x8eƩrѺĥΜÕȝɊȑκ҂ʱ',
                                                    },
                                        {
                                                        'key': '/ɿȨǁ˟Ƕƞ˂ȖϘѴΏ˞ō\x88v҈ɣϐɮӇĿŲƐҘѩȟЦҎɝ',
                                                        'value': 'ʰƕЬ(ŵûΒԡɞmǎƔϟǏɴ7ΘY0ĮŭʌťˇҋǶЪӚʑʒ',
                                                    },
                                        {
                                                        'key': 'ԠƲѨ[ъђʧӒџē\x90ĽϐԘ҄ƢÒͻѝϺ\x98ßЂʾyŎу´ѐЫ',
                                                        'value': 'ʡɭ˭ǕР8Ȼ΅ζƖѤƛ=Ķɿ˨˓ʎ\x91Ǜ½ɂхǫɡ˩Ъï\x8dʪ',
                                                    },
                                        {
                                                        'key': 'bįӵԛƵХŀĻɰȎùӆƂρ¬ҀȵςϻɿɭΓϠРǏηЧӪɱǖ',
                                                        'value': 'ņϽƶӥéơɣЅІˍȒsйǋ\x8eűӐɲʉśѐŭΤ;нŖϔϪĺӷ',
                                                    },
                                    ],
                        },
                    'comment': 'ɓȢɑȥƔљB¿DǞǲǞĽpȫҤпӮǩÜҗ%к\x8dʹΊɸǀƸ:',
                },
                {
                    'keys': [
                            'ЎȦĚ¥æԓ»:LυΈԄϤМǝɴѩNˎǠʋBUоˋ»ÙӀНҜ',
                            'ϤìΚɋȳϖпΝωѠɧϯғȮʡΰ',
                            'ͳ\xadѓŒ˫YƝňѩЦà4ϖ£ňηq҆ʦƣ',
                            'ǓȍɡΏӣ\x9b',
                            'Ѐ¬ŶɥŃϚŁPҔԫĝЍѽɫɱĭƜǟȒ˩ĸ',
                            'nɿлʾʼҞȌjˎʙŘѡ`\u0379ǿ',
                            'єĶɥêň·(ԎÊBж\x804æѥ',
                            '\x82Õ˭\x8cȉŇѨϧϊɘùkƨȣĐAŗǉʠ°',
                            'ʩɾđͱˋĕϾʛŤԭǰˑ',
                            'ßŎԕӱʫѮв',
                        ],
                    'event': {
                            'target_id': 'ϡК$ȇɌŗǿÀȎ|ƦɺυԚѠЗËяҥ˺ТғДȼ(Ӥ\\Ý|Ԕ',
                            'parameters': [
                                        {
                                                        'key': 'ƀĊЅТȁØҔ˄\x90\x8eïϮΥΕҢҔɨʢűԮўƤԂϟ˾˽ʋ',
                                                        'value': 'Ԓ@ĉӺ<ѣǴѶʶͶLãQϻӉâƅϗʯѦϠěƯɑӁ˔ԋǚĻʓ',
                                                    },
                                        {
                                                        'key': '˗ѻæ3ѾԥȸĮпЊťмűԥcӒʯĘǀĀʏЃʝŏĳϿʓČżС',
                                                        'value': 'Σӗҫҽъ£\x8fȚʁÆˊЩњγȰ˓ǦȶΗѾȊưƸɶ¦ԆѨƋˎ8',
                                                    },
                                        {
                                                        'key': 'ųȂǭûΗɗӹұѭŖðζѽǁԧãvɿǿƼϋ¦uþ˨ғÖѰӦЌ',
                                                        'value': 'ҾϲAɯԀǭԆƝӞ\x8cʕҌ\x97ʏɇǯѬϓ˱ͼШĵΑϐǫҁȦϲ_Ϗ',
                                                    },
                                        {
                                                        'key': 'Ś˼ҨǘǤįɰɁNʡ˖ӏȁȑKɼ˄ȉĞӿĸҷқ\x8a~ɗ\'"ȑǕ',
                                                        'value': 'ȴɲɭƆҘФǿϫƅӽ¯ĬϷԩǪύȡǪʎŭŻɍд˯ŝȴ\x8e҆˙Ϙ',
                                                    },
                                        {
                                                        'key': 'ҡǬưєλǒØŞŻ/ҘȆëˑБÖǥКcƓƮ\x7fȰGçɚˊΟǴͻ',
                                                        'value': 'ǏėԕѽοϨӫƵȮўeҮ ϧİϒ˪ӒÏ΅[ԑҳȀ҆Ӗô˙Řħ',
                                                    },
                                        {
                                                        'key': 'ɨƌʻ\x82ɧӂ¯ԋ³Ⱥѹīïþ˹б}ӷ͵ųȼ˾ƯӡҶĽѹƇƦǥ',
                                                        'value': 'ҿĦǠʏˌƂύĜúɓЭǹ˰ʽȑˌТҊΑέҕΘʕεӐѭԍ҈ŕV',
                                                    },
                                        {
                                                        'key': 'ԁЌeɔRΎƼӡŧŚǗ\x93ɕŘɩɾȉͺƯйҫ͵ϯÕ',
                                                        'value': 'ӳwƽɲ¨ϡϟƿȍ\x96Ź@ĔʸƄҢΔӊMӋW©ȎϠªŸӸѶ²ѵ',
                                                    },
                                        {
                                                        'key': 'Ϋԉƙaѽ8ŧϛҵđɿʷπԂ\x9dήɑˮӅɍɸ¦ԔťǏä÷ʖľĩ',
                                                        'value': 'ƔǀҜрϤʺÉɣőϓΏȌÑΠѧdMƄȺσɼωΙē\u0380{ʵĎ҈F',
                                                    },
                                        {
                                                        'key': 'ɤνiŮƥӱЉ3eыģӀß¶ę',
                                                        'value': 'ɜŔ\u0380ûđҲ϶ÌѶť\x8bԘуĔѯѳӡʲȅРϯ\x92~ѢĹȨϓӗџǛ',
                                                    },
                                        {
                                                        'key': 'ԬφяǊǮ',
                                                        'value': 'ӕҫɹĮiДïӔƷŚʅФıϠ,ЦˢƜ҈ʹɛζԒɕˈ˔ӈşЙЉ',
                                                    },
                                    ],
                        },
                    'comment': 'ĞǂқŎ\x82˒϶ʆԀɞ¸ϸ\u038båҘ²Vȉѱţ?қñĹɷ\u038bΡУΥˀ',
                },
                {
                    'keys': [
                            'Ψˋĝˊx·w\x8cVƔɂǚΜ~ˎŶƉ!҈',
                            'Ɓ×Gʊ.ϖ',
                            'ѰбɍʗӣĹơʊͽѧ&3ϟ',
                            'Ԇ',
                            'ŗѭƮϋԐД˜\x8b\x7fȠЂпч',
                            'ØȷСțғƑȿѠnӘҁÇɀԄЭ¾ɠ',
                            'ŗ˦ϿŌŭΗɌԗέčƃԋ\x7fÙǨÐőϱİ˭ɣŧЩ',
                            'ѓΚ?тŎǽѐ6ƃȺƮϏўӈŹ˱΅ӽ/\x9eґ\x9cϦ˫ԔŷŸǙΉ',
                            'ŲņϺɻʙˊ˯ԕʥĩ¯]ӉɖͿϼ',
                            'ͿʹɂNѤϟIϨȎ',
                        ],
                    'event': {
                            'target_id': 'ГΥùɠɫĹˏӥƝs\x87íϬѝϒeOǌЗʙǹ!ʢТɚӻʁ\x92ӈ\x9f',
                            'parameters': [
                                        {
                                                        'key': 'ƿȇϻаγ҃\u038b\u0379ŤͷƫɬξǳϩѸҹҹÀбφϨ3ӜҠϸԪёҼȦ',
                                                        'value': '˹Ɉ)ŴùϽʹӿ8ɭНɽ҅ҥԣĶÝÉ\u038bȄ%ʵӛʷɣȂНȥȞυ',
                                                    },
                                        {
                                                        'key': 'ϕʲԪǖˤʉŢԠƐšҀ¿ҞӏϱʈŧÇɸȺéм]ԥσҦΥҎӶȰ',
                                                        'value': 'Пӟül˲ЏðDĚÃǿȸњ+ˀ˟ϤȢVĸОϖɓћʳ|Ť9Ɇɑ',
                                                    },
                                        {
                                                        'key': 'Һ\x8eʃϲӃ¸Ӱɻ>ҜѨΗѥ',
                                                        'value': 'ĝƳƎη?ѫɎήǄӧП˲ͺaӑϭǉȾΠԟȍĖÌκ§υ\x95ǨȹȌ',
                                                    },
                                        {
                                                        'key': 'śΑĠ',
                                                        'value': 'ѶŲ(ǩҸԄHÑɫěǡʔѲҸӝȸӯҌŁĴΖȾҫϫ\u038dЪoɌʐз',
                                                    },
                                        {
                                                        'key': 'БɛȈ\xadĕ~',
                                                        'value': 'ʧџ¢ԞlƿĹǕӆĪġÉʹˈǄхȩĺΠưÕҾɷƿǯ ЉʲԮĴ',
                                                    },
                                        {
                                                        'key': '˽ɒıԀ˦ĺƇěтͶΏΫϑ²ȰλȒʍȯʽӵçοҬīˍǱĖ҄ç',
                                                        'value': 'ǄӼˑӽаƕΦŢ×ǧ²\x9dɈżΒӧƁЏ\x96Ʊcɟǐԇԙ¦ԉϿӉӹ',
                                                    },
                                        {
                                                        'key': 'ơƦҡϊˌȆȕȐόıÔɊԈιu\x83ɨ\x9eʪҤѨʑǛ',
                                                        'value': 'ǽ˨Ф\x91ƅǼËӗͰŎԍњѡ+¤ҽɂʫή,\x8bǍЇɿȇϟɆ¥đӽ',
                                                    },
                                        {
                                                        'key': 'ŗp"ŽϊάҒ¬LÈȪϓҁλǂԫͼˬȊϨГɼÉMԑ\x96ΑșĥϠ',
                                                        'value': 'ĸӺͺȄǺЈ˴ԕF\x80ћȦƿɍËÀԄҝó]ȉ¶ΘüȐƀϺѤӿƴ',
                                                    },
                                        {
                                                        'key': 'ҿчԤƪϿɍ¥ΩѕЩѡʿҦɷȡǠ}ўțǌж0У˘˒\x9cԎȩ˒ђ',
                                                        'value': "ѥτȮʙԭ©˫Ǻ¹Η¸ĺ#ȔѶ'тԬďńһĚǺ,Ӏˎ\x80œιʊ",
                                                    },
                                        {
                                                        'key': 'ҋǓщ',
                                                        'value': 'ΨЖĉʜeńԮǃώӲƱ˰ʸŨƑɍ\u03a2lȇƷÐìώҺD=5ѹ˺\x84',
                                                    },
                                    ],
                        },
                    'comment': '˓ƹʤȔËʢӚйîƙǼƜ÷ϨщʝЃƆğϞ9ĢǔǤЛmӗ\x99üȂ',
                },
                {
                    'keys': [
                            'ʞϰқӝрԑßÈ4ĭ\x91С#ȵȡςĊıʵǪǪ',
                            '\x7fξǜ',
                            'ђпʼрSъöȂѵψ˯ÙǬϿǏƃŴÂřԭ\x84',
                            'ԟӑоɷɡиjȶЮ¬9ŷąǩ˧Ȥƿν',
                            'ͱ·џѱǁ',
                            'Ɇ<Ԗ©CP҃Ӓ҄˔ǘ˂ǣӡ\x86ҮЇ\x85˧Ǳ~ѥΈŌΙ',
                            'ƇĢӞʬӷåҲtBҟȅCԡԉέMҮƭ҆',
                            'ʂ½ԡƛԫИ',
                            'ԓ˘ȩˏϜǿѻĴɽ®ʤĘ+ĄʱӤԪǝӽŤ',
                            '6ΙʪѧʦkßͰҖǟˀǼϳ\x94҃xƍʀ',
                        ],
                    'event': {
                            'target_id': 'ѫӦɭӥāǧȐţ',
                            'parameters': [
                                        {
                                                        'key': 'P\x87=ãȡƤǡ7ôńĖ',
                                                        'value': 'ŉʚɄĆƃԝ=ɗӂȏƪŸǃöÑʩМҬҋҤÚŗЛъłʇғԒƽҗ',
                                                    },
                                        {
                                                        'key': 'ϵʐυˑŃNӀ',
                                                        'value': 'ʉɆ\x80οǛGǛʟԩŔ˖҉ӗǽťȰӞΎҢɨҞÚǍчǒĐЎq\x95ț',
                                                    },
                                        {
                                                        'key': 'ʌԓİĂüźѴѥĿΰKf*6ƒоУîʻΒˆǣʬҚ1ЊŪǭʵ\x9c',
                                                        'value': '˟ɸĖť҇҆Ԗ¨ɽ҄ˆЯĲ˾ƍȪĥҙǔҤҞCžǘǅɓÿΞϕΌ',
                                                    },
                                    ],
                        },
                    'comment': 'θʃҾԣʂԐ±\u0383к˩ȿԪѴƘǗɴϮϼï˻ɘқϤǒɎȳʡҺ˚Ҋ',
                },
                {
                    'keys': [
                            'ȄBŀѐϔǔԮ/Ӭşĵж0ɘ',
                            'ɶԊĭŏıӭϘ}ŞԔ˳',
                            'ɹĄƛѿӞѺ¥ϼԅӠϹaԫԐΰʜԐʪĘѹɄȷǍŤԑɯѳи',
                            'Нɺěļ½ƘΗʀ˯Ƨ\x95Ƒʫ',
                            'мӳ\u0383ɦʁʫи÷ѕɵԝӲʴƨȑ˗|Þ',
                            '҅ĀƨӬuΛʡӔ϶',
                            '҉ΒɗȺBЯͲƪǸϓ˜ʮʵŸĜЍѹӻʟ÷ҞɒɉĠʈҢǇз',
                        ],
                    'event': {
                            'target_id': 'żѱƋ˘ǆɡâӴϩͺȱDӫ\x9aҷ˚ƹȂīƴ',
                            'parameters': [
                                        {
                                                        'key': 'ʠĄ',
                                                        'value': 'ӜԫϳӬÎЋƄʄΗҠ¦ԣЌɔĺΒʦ,ϡ§˾ƻұxѝǝγѝӰԃ',
                                                    },
                                        {
                                                        'key': 'ў҂ҲӐΗșǃαƞǢсȎˁ5&їʛҒǺњҙнԭøϥёɌԟƂ\x9f',
                                                        'value': 'ƝȄˊЖĢ˸Ɂ\\ʧԂQțºFΉâмиðΆԕķʛϨʥӦǉчєǈ',
                                                    },
                                        {
                                                        'key': 'ɷµԛĞǊͱР\u038bɣƐ\x98њǃõǚĢŬңӷϛϚ˙ШМáƁŽѰ¢Ѹ',
                                                        'value': 'уқƑȾĮ˖Ƚ(¸zŧȇӷƦzúAȁö7ǑїѳӒȑԮӀԡǧΏ',
                                                    },
                                        {
                                                        'key': 'щǅɥǍӲȬlԮťͽƝԍ\xadV˶ɚϖī˧ҬʜǀĻΙЀ\x9cȆôʟĕ',
                                                        'value': 'ϟƫͲ˛ҙȤѫƘÿ\x98<˧~ϊҕȐǶ\xad¸ӟɦŢÊz΅˳ԂɪϿÒ',
                                                    },
                                        {
                                                        'key': 'ŔʢǏʤķХſ¡',
                                                        'value': 'Ȇҁҧ˵ҤʭςjȼyɄĭҎƯϺęǈϾҋʻƬϳѢʾ\x9eӡqНĔ\x9b',
                                                    },
                                        {
                                                        'key': 'ηэЌOѺȁƎȨɁиӜȜƬHљεѬƿz/ЁѹģȃбćÒǏԋZ',
                                                        'value': 'ΗɰºǈήɯŊː%YΠèԒЙҶʿŖҒ˳źđѪӁ·Űďћ\x88ȫɵ',
                                                    },
                                        {
                                                        'key': 'ÅԓɢȽˈƃҿʅ@ŜˁэѴjОΪzˠǋɗƾȃԋĖİƘɅԚԪЖ',
                                                        'value': 'ę$ʘêɐȔȱȰcԦƝ\u0378ÜłɒǀθӷčɆϖˈɩÿ˝ԩ<Ɲ\x9d҉',
                                                    },
                                        {
                                                        'key': 'ƀBӵЦϝ҅šȴЃ\x95Śˈʏӷ±Ϗ˪Ұ®ǞǊɷӜƎ,ͿŲÛƹ˒',
                                                        'value': 'ćνѪ˰ŶŶȴūřͺɽͲƅ\u03a2ǷȭďơÀĐ\x80Ҏә϶°΄ǈЏͿ\u03a2',
                                                    },
                                        {
                                                        'key': 'ɭˍǡжԣʷқʅJĘȖ.ƭӈ',
                                                        'value': 'ʷWǓɳʕTέĎԬ\u038bϲЁRȈ˒Ⱥˀ˺ɘɊ˂ŠјɞΗŭ˸ϰӱӅ',
                                                    },
                                        {
                                                        'key': '+ƊʽV¨ҤϏŐˠ˚þÌʧК\x7f˵ԐðӠԖ<Jӥ\x99ӭȁĴǿӁʯ',
                                                        'value': 'ˁ˘ӋπӬ\x8cǵŘύо¾ȮЫ_Éζ]\x8aǦŔҷΐѬҎ\xa0ɃδΟԆ˖',
                                                    },
                                    ],
                        },
                    'comment': 'ˋƿ-³νϜ\u0382<˃ȟ˨\x8eřōӠлӦ_ʿƶŞäϴӘɫȱΑȸǶɭ',
                },
                {
                    'keys': [
                            'ǴŉԮѽčɖΏЪĿțϫщ=ˆǇ\x8bɂВξĺΚƊƸǿ3ӗ΄Ìɲɩ',
                            'ʣ',
                            'ȨȤ\x97čӵƽʾϩɝ)ȮˣҏǺɄԣȩūǛтεʬӍÎƖˢ',
                            'ԣϖ\x82\x8dƥα¯ˎюƂęÙϱƦ¡·Ӌΰξ',
                            '˩ВӂЯȏР\x80ԗԭԎϢʓǊƠŨҚɓɿʏɋ',
                            'pEƤãƜíлПϼЖ%ԂĈΞ·ɪ1ԏǋƨˋЄόΉ',
                            'ԭÇ',
                        ],
                    'event': {
                            'target_id': 'ˈкʘȈņΧĀÊ˥ѥΓ\x83϶Ϙų҈ŎѠİӒʣȄӉʻЅĔљηĜΧ',
                            'parameters': [
                                        {
                                                        'key': 'ѩ#ɨȉŭˍȴΰɅ\u0379ʹ×ȂwƨŖFӺмЖɤ',
                                                        'value': 'ҁŻʴΌîɐϾͻ\x8bðҨƇӜ|ǘԌƍћBҪ\x91ӎԥƤǾΣǻԏĠŜ',
                                                    },
                                        {
                                                        'key': "ŃǱƩƄ»ӠıÈ˃ϧˆvŐхưѩԡłґʨöɑ'ɎȒ>ԆuҬʴ",
                                                        'value': 'ǙɈʟӵőĨʔԤҔĬƇЅʧǬӔ˸ʎˋήķѮ\x9d¨ĈζϖĨΓ\u03a2ˌ',
                                                    },
                                        {
                                                        'key': 'ҿΨĞҺҏÕяΩδԓāUŉԑʡÏǨӅʯѪľΪüȹяȴΒѐїв',
                                                        'value': '\x9dɮfҍɂԞ^ƈŗ\xadȃНЁǰćĥЁЛ˥ľΚÚԊ\xa0ȗкɉÛűф',
                                                    },
                                        {
                                                        'key': 'ŮΙ;ʋӢʊȝšƖмΧƘԇĞԬʱùWļřϴǓ´űyӦǈԨͻԗ',
                                                        'value': 'ЕΰʦųƪƭΞǧŻǀũФѲʾǃĹ¯вɌͺĮӵˑ\x98òɣqɚũњ',
                                                    },
                                        {
                                                        'key': 'ȫҵԉͳҁǟΨēоћɃ˾Ȼй\x87σвƝʫʂϥӭӌƹԘ˧μĹƀŝ',
                                                        'value': 'ǭҸʫ\x8eƚӥǁŒɔƝн˜ˢȑǲĩ˞uŒε˞ϝІ\x8fȓU˭¥Ʊɻ',
                                                    },
                                        {
                                                        'key': 'Ą˾ЉѷѻмӶϜәɤӁϖμƯƲϢɴԎѡŖŠʐɭρȦ&ͱvͱҔ',
                                                        'value': '0E,KʩƭÂμƨұǦġǽγţɖɒѺҎťnǒҕÅӴҤŜй˳.',
                                                    },
                                        {
                                                        'key': 'ĩCƬ_ԙǍӪƪ˵W\x92Ͳ҇ʖ*jԄŨɳǨ',
                                                        'value': 'ǮӿҢσĢěЯѤӭ¬ʞщ¬άɣӟψшƞǲʥ˧УũЃѓғ´ªŭ',
                                                    },
                                        {
                                                        'key': 'Βұ\x8f',
                                                        'value': 'ǐĭĤɸŕäƲԕ˔ѕΓλМюÝșHЕЁ±Ͼâѝ\u0383åӫϹaG+',
                                                    },
                                    ],
                        },
                    'comment': 'ӋĺԧɁǩȡŻԧʇÛ?ǾˡǫuνʔĺЬҊˣʱԁƮɁκϩόʁĔ',
                },
                {
                    'keys': [
                            'ӕ˃ʥˉƃȞЈƇ',
                            'ɄΆ˽Ⱥˣȑ>ҺԘʢ¡FɪƩɡңήʈàщ',
                            'ĻÊC{νҘ˾',
                            '˵ƒӥԍEjμӍɂΒ\u0383˫ʭɕ',
                            'ƓƉӶϳ¹ŵÉҧӻЏŘӸ˥șЍѸʝĬʃÐʦ',
                            'лʦϝ҇ãƬĵȺÐͿηɘΖʖɖϸ',
                            '-ѹҝ\x9eƧȢŞȻÒӕŶԉƽǇ\u0383',
                            'ĕӕ΄ѢУЉɀŘĵǢ¶ѕΦӚдѲӔӉɧ',
                            'Ǣѵ·\u0378Ɍ΅ҫ',
                            'ҿΑʓˉƿ ŚԖԙï҈Ěʺî',
                        ],
                    'event': {
                            'target_id': 'ļш1ɼŰѵϟ˰ˆζɘʸЕʼƍɊШπıͿ\u0380å˧ǩʌτʹ4Żѧ',
                            'parameters': [
                                        {
                                                        'key': 'țӱĿԭ҅ԔΤӼæӘԣԒǍҐηĩŗӴӚƄŭ\x96љƆÌģƵƅнʪ',
                                                        'value': 'Ғǽˍą<Ѩԉˁʲɬĝԥ-ĀȖԑħγαӺƸɐҖЈΌĩΐЩ3Ӕ',
                                                    },
                                        {
                                                        'key': 'ǵΨ6ºұĹ¾ãԪШӧʊ˅LŔӵɞ#ɽ˄jˤʶǷĩͲƠͶĺӧ',
                                                        'value': 'Ǹǜ×ӕʁƉȕɽ\x91ġ˞ӀўЦŋҋɯΈԤώƲǝ˳АźƮǟʞɦ¶',
                                                    },
                                        {
                                                        'key': 'ҜòӛʖȝӬǾЧǃԠ-\x8dԄ uɳΟʚ\x9aŅ\x93ԐɩδÕ˳űъǕǸ',
                                                        'value': 'ǝΥѠЅ˴ϩĥʵӭ_¯ĥŰјɄɎǍÉōƹ϶ŔŲЇѹ-γóԞї',
                                                    },
                                        {
                                                        'key': 'ƣ>ŝŴɃ\x89ƲøӵɏњƛgνΛzʾÆ&Εѫʫ²ӕˉΜLʂOĴ',
                                                        'value': "αɊӏ˄ΎˠĽȤķNҖҷԆ'ѰʒȣʆӿӢӭԙԂƊų;ӥƞПƛ",
                                                    },
                                        {
                                                        'key': 'ѨÌóɝϸοӘ}¹{Ȍĩ',
                                                        'value': 'ϝӦÒѴāюҡȋĵſŻӰǑȇԊҘzζȉŻѴвŗØЖšƲǐXɟ',
                                                    },
                                        {
                                                        'key': 'ѣ',
                                                        'value': 'ˮġŁƌ;ǄϨ˩ǋЙáąʓ˶ǈэʟɰɵӗϽϽǣϜȼ˅*ɵѤk',
                                                    },
                                        {
                                                        'key': 'љΡͽʼ҉ģũĬσӻƘȅhӞɭіѼłӫ{ВȘаD',
                                                        'value': 'ʯςk0ɼѫŕӏӇĔҬŌ˷ɫϥȨęΕȒʬԥЬάвԙϯȿӔω˭',
                                                    },
                                        {
                                                        'key': 'ǹ»ŇӢĘƇЋҤʙÑƷėʲȘĺɳ¿bѱӴȂȽЁͷɔɒʋʻÂԄ',
                                                        'value': 'ҝʄЏ˜ϒʨц¡Ş˗юƨӑĔӗņρ/äџΓèɮΘțԓľǷơѳ',
                                                    },
                                        {
                                                        'key': 'Čš҇¦ѿ˓ђµʲΊҜȫïǪărʀɏ҈҈Ѩ}\x83ҮÍĒʠĴЈē',
                                                        'value': 'ʨΨԈĘƾɂǯƄ§҇ȔҚǡӸƼÖûƱƔ˳ӒƶǞϋџƶÝB\x92ɭ',
                                                    },
                                        {
                                                        'key': 'ŧͷΈƣԋӿĶǅӡɍȖϊϢʎȥƯʚȀÔs\\\x8eÛϾɱ_ɛÜƗȶ',
                                                        'value': 'юүʔʓÕʞŃԎǥΚИԓ˳ѿϮЂ¿ΜѷpŘӢʑΒπѻԡʫ!ϡ',
                                                    },
                                    ],
                        },
                    'comment': 'ŃҝΥӗ"ѿӳһǌ҇Ҝ\x84ЍϬҹԟϺąбǮȳȡɨ|ҦȶűʐÝȺ',
                },
                {
                    'keys': [
                            'ȲӊӝɹҸǬ',
                            '©ϜȫϚʡǇtцŤ϶ӁΔǾϐǗˋ',
                            'ǂäтΓɦԇµΊʇūȃОʽƮɍ˨Ȁ˝ɳ˟Ӭ\u0378ӷЊ',
                            'ɠǬбзĔŞΐӽɮƵӗӜħ',
                            'Џɾ',
                            'ŶШǍß͵йȩρʩÑҕǱѹ=ΊҍϐԕЩļżϫƖĒˮȅ',
                            'à˹\x8eβ˂',
                            'ʐŝʦǏķbĳǀíƖύίɰӇүÂԖã',
                            'ɼзһ҇ƭϦȅ,ӻâ\x97ȩ9ҏÂѰħРǁ',
                            'ɉ\x93ʠӠĮÔΧȍƔ¤ӲӔюǾƁрRҘҗм',
                        ],
                    'event': {
                            'target_id': 'Ϧ¢þŪ϶ΗˊŨąӋ_ÂĭҩӉ\x8dΉʅэZǁm4ʙњƳÖW^Ȗ',
                            'parameters': [
                                        {
                                                        'key': '\x87œ²Ɇҏɇ\x8bӀΜDåΉså8ӐƯàżҬʞǢŜӆĖʞыӃȵͲ',
                                                        'value': 'čϣԮʑʹˈĮӈǜä˧ϞԪńȬ˘úӿWŉǐȅќӶȲ?ϴΞһȋ',
                                                    },
                                        {
                                                        'key': 'Ѣ4ǤЉªі{ӟǺƶ˗ҪɐѰ\x88ӅЎňтįϏӒͷrʮhāŸ¾Ŵ',
                                                        'value': 'ьŖҢЕʟɗˏΐѮԓмǀËŀǚԟuӕɔЖ+ƇκˤʩʚÀ#IH',
                                                    },
                                        {
                                                        'key': 'ӮѤъРJŧԟ|˘ĩǍ¾ȡѲӕϸɑĨËίǖЧϲ\x7fɼUѮāŶȊ',
                                                        'value': 'ȏҩνԄȭȮҖюˁɆČǌͺи\x94ϖɭG\x97ѨҦɞʚȜ˼ЮΘ»зȰ',
                                                    },
                                        {
                                                        'key': 'ƜτȴǩûƫіͲϯцѧƊƮΉѺѓȚΨӜrϧϷɱϞͱ˄ɝ¶Өƿ',
                                                        'value': 'ӰʚΘÍҁʫsЯƑǄѲϜҷìӅӯӞϼϥθʧѭEøġȂйшǁӖ',
                                                    },
                                        {
                                                        'key': 'TǶюѥÄȃҍĻŲĀpҎɪ\x8cȐĻȎ]Һ£ΗŘƲѨÚНƂΡѣq',
                                                        'value': 'ĕуѰęӖӨμ#ӮɉɟŦʄěɋąҞĭǗѴɉщɕͰԢӑʇЩĉϿ',
                                                    },
                                        {
                                                        'key': 'ʖǫɺԒѐƁąўΈ=ÔƵǎЗґÂϰҾϑҽ ǖ',
                                                        'value': 'źʔűĞήŚǀȉȗʁϐ\x93҉ĝ˒Ή˷ӡӉʧʡƚǍŜ2ƽĆ\x93ŚȻ',
                                                    },
                                        {
                                                        'key': "ȏ˚ԔӽɎ'ˆÃәѨƥΘ8Ӊ\xadɞʘ\x91ˑ˂Ќ\x8bҰԨɀӖŨǺĴƦ",
                                                        'value': '¼ǓЖ`ɝҨсɚͼǴȪıо˒4ɥԋԒťǳӹɽԋǮÞÕ¯ӡ˪β',
                                                    },
                                        {
                                                        'key': 'ƵԮƒģЮȠҺĲ˱пƷɣ·dƗˋȡśԁϜ^ԫљӕ^\x99Мȇkѡ',
                                                        'value': 'ǹɑΠĻԄΚȋġӳƵϷП\x86šʞuGΉŜŘ҉КҠԙӌ˧¤ȕÎȶ',
                                                    },
                                        {
                                                        'key': 'ȵ˘',
                                                        'value': 'ԋ|ҖøэǻϥŃȘǭИηҀΥЄӽvɑ-я\x82ȿѣɎtàc56Ŧ',
                                                    },
                                        {
                                                        'key': 'ŒϦȳʈľӋ҂Ǽʞ˺NƑòδʦ¦ҍŊȵïʌςΎɟɡàөɝλɵ',
                                                        'value': 'ΜԁοƇŗΨԁϫΐʃ˨ʊʖӱ˘үPӢ±ˬʅѪъЄҮӅЍŃɃȹ',
                                                    },
                                    ],
                        },
                    'comment': 'ΌϏџѿρ˪Ȩ~ǹѭƍҀŌ@ԒѦαŁʃʚùτҰѠʿǓ|ŸԐҁ',
                },
                {
                    'keys': [
                            '˝ϰiʱ\x91û˒ŎȪǦZåľėª+ÕþǞȆІЬ6',
                            'Ϩ',
                            'пϗƀҚdPɼҥ˥°ӱԉƚɡɑǅǧ˹˃НȰҸӨɔδƐ˖\x9eFî',
                            'Х˯ĐƓӍ˶ңû˗Ǹ',
                            "ϝŤĵd·ϫ˥ĘɭͼȨĖ\x8cgː\u0382˚'tыƒҊ˖¥uˌӎԐУ",
                            'өʁԤθӓĥǓˈˮ˄ФйE2ƩǬʟ\x84ǂԆƙ\x80зƨϸ˓И˭ҥ',
                            'ԕƪΤʜ˓ýяѣǫ˦Е<ѲÀǰɕӾĂϠȴԛϨД',
                            'ËʟөʟҾIѦ.Ӣ¥щҌȀ¬Ǜ',
                            'ƯĴȒƹ',
                            'ɡўʚҕѢʝλţӡáЙǻͳǂ',
                        ],
                    'event': {
                            'target_id': 'ɜǱ˹]΄˙ӞкӚ҄Ēdøt-²ØɆύ5bîӋҭɐɧòǰǵŕ',
                            'parameters': [
                                        {
                                                        'key': 'Í˅ʋʂʧԙǦɄоB\x91ƴRƫӞ&ãӧϳ\x80śɵѮŃЖ»ƪȆƵҺ',
                                                        'value': 'ԡˌԧҊɲφȥĳҊȘɭȽJдɍȩ\x93¡ˢЅEĎȲ£˫Ѓȍə)ǩ',
                                                    },
                                        {
                                                        'key': 'Å',
                                                        'value': 'WĕҔӄȐðˍͻˮËұȏ˨ԞϻŶǴ\x92ԎƠӯɄ÷Пύчʂ˩ѓϏ',
                                                    },
                                        {
                                                        'key': 'ʀ˄{ÉƎȽɇӗͿƯÓшӉ',
                                                        'value': 'ʲȔĨ˽ӹˌ¶ϻҘϻλӣŨƟĹΆ\x9aȼҨWƄϫƕǆ\x9aИǃR҈Ү',
                                                    },
                                        {
                                                        'key': '\u038bŎЙʀýʤ˜¿ƻƳ\x87ƷʄΩӇʶГђϝьǴʈ·ˍʯȸrОǌΔ',
                                                        'value': 'ĠϋҜӶάuˠɯǃһÖ˽ҘΤѮϡðƋ\x9cʺIơÝʶŁĝԨ«δɷ',
                                                    },
                                        {
                                                        'key': 'ŽȮпǏҠκӃұ˾Ŀпˤ ЉαǗ˪ӣӇɇҺ6ļԐĢŦ3ƉßŶ',
                                                        'value': 'ԓб˃ȢϴӞŚƬĊʎьҟʊĜƧŀӀѾ˓Ξ¬«҆ǅǲʃĘƣşѽ',
                                                    },
                                        {
                                                        'key': 'ʛɖȾĢ˗Ѣ˨ӎҡʳЙϥ˺ʯыƉʊÎ)4ǺƟǣјĥωɷ\x82ԛć',
                                                        'value': 'Щ÷Ѵ\x7f҃ҕš˖ėĊγ˸ĜБ˝өяJɁɉχѿҗҸˏɱʦȥʶO',
                                                    },
                                        {
                                                        'key': 'ҭɻɘǶƀİͶѿo/PԟīǙьĭc\x8aŕҠΨ¯\u0382ÂÔǂΤϹҏǶ',
                                                        'value': 'ѼʁΉƈʉυƥòPɈºĭԘԌѠŠĿċɾéӣȵԫȇԉ˹òϹƉh',
                                                    },
                                        {
                                                        'key': 'ˎсÐǦϔȭɗÃ]qҢÓƵƱΨŬҰŗǫĺʊʷžӧɟƸɵиqe',
                                                        'value': 'āӢɹ΅ΕʣǡμɃFȲӶѓЧӡҦɩӵϼ˨Ӯǻνȃś<ͼ\x90ʮ҄',
                                                    },
                                        {
                                                        'key': 'Ӣбκ}\x9fʐɛȾ\x83D҃ңӪȩПpG®ҳïĦ²ƚΙƽʝēˤ\x8cӗ',
                                                        'value': '˞ЮĈ ˨μˠЂ²ȚѲʔҶƲǧ\xadǜǹA˙Ѱ#ͲµţԀBĳӰp',
                                                    },
                                        {
                                                        'key': 'ȒΠŦШ˻ςŎˎÍÛąχ˄ʔɒĶԌɩћ\x80Ńһ)ҹƬ˷ŹβȎΛ',
                                                        'value': 'dȴʇ˦бϿΎ',
                                                    },
                                    ],
                        },
                    'comment': 'ιĮϊIʿŗȳ¾ўҵëɗԣ˝\x85ƇNȡ˂=Вˮ\x98˔ƄвʊɈЋȿ',
                },
                {
                    'keys': [
                            'ЌɜŹԆҫԅѷҰɼ8åжҞСʇ',
                            'ŏÖƄȁЭϿ',
                            'ǰЍÞȳťҭʚ',
                            'ȯĀШΉűӐЛáЎÁϾ',
                            'ɡȋӍʭ}мɻɸԦǺǂԣƒЊαƦҤĝÜƛcȲф',
                            'ϩFŚĂɤҖ\x83ɚѫ˨%8ͳA˨Ӳ³ĕ҅ʽ;сӑƤt',
                            '¸ɰ²хҥϩʜRǫήƜ\x8dǂ',
                            'ɶηɗΈ',
                            '˳чUŌǯɂ\x9eȲҗ<И¬²Ԇ',
                            'ǌτɾǚψ§',
                        ],
                    'event': {
                            'target_id': 'ɎѝĹЈһ΄ĵѳԇҋϻ)ʮǫӾЂmʹχӠ\x8eΈÁσϺˎȾǤγ¦',
                            'parameters': [
                                        {
                                                        'key': 'ΪӹЄǮΣȿȀʺΆ\\ӺϭɊΓŋӑԫʦƬ3$ϚηӛƉȮƝŭĔĺ',
                                                        'value': 'ԞŲӂȧþńƷƓß˟ǌɱЬȏ²śPʸϽ·]ƪ\x8fñɦƏ\x9cdƫɣ',
                                                    },
                                        {
                                                        'key': "Ɖ\x95ɢŝÑĽˊӨ\\ӎτ˩¹ȭ϶'˕оː7źǖӶˤȾɚ ƍȰҳ",
                                                        'value': 'ʔgҟеˍҍëâţȼҩ¯11ЇƻǮA϶țǞȫ\u038dΧƎ.\x85ɰˇχ',
                                                    },
                                        {
                                                        'key': 'æёˉťǜКæ϶aĎŲ˕цΧɏƼұƨӟρĦʹ´Đ\x90ӍԝƢĵɓ',
                                                        'value': 'ÝNљĜȫ\x82ʃ\x97ģ¾\x98ɃƪˀÞѬΙˡ¦сђɐЕΆʽˠʙϺЏϴ',
                                                    },
                                        {
                                                        'key': 'RΘ˛ШƶØǘʑϺ\x9eǿǙ˙ιɊźѺ˯ɈЈrҾƟКĲǎҪ˅ķΝ',
                                                        'value': 'ȥѺmқЄӮǄ˾č\x9dƈҼ!ł˲ÖΦТƤџɣãƦѳϕhϰʮ¿˙',
                                                    },
                                        {
                                                        'key': 'ұΞӣύďĄ҄KĪ)"ǙȞҰƥǤˏ',
                                                        'value': 'ҁВʚàРƖ®ƍ\x94ɟӱǂưȀЅǐҮŌɎʘ\x8eӪǑͲЃǘĻыǻː',
                                                    },
                                        {
                                                        'key': 'āϙκʏΖōýγðĢoΞÙƉ<³Əŵœӻɷϥʤ˛ԖЇɜѠəƫ',
                                                        'value': 'ǣҞҿЧ¾¼ūӐǂƪϪƧ\x8dķȍœƎǬȋPλ3хɑ¢ПÞԔŖì',
                                                    },
                                        {
                                                        'key': 'ͼřɬbùАȲӕʆӡͿàνЅ¥ǨЛѬьȾҠ\x89ӂȥˣi¾βŦɳ',
                                                        'value': 'ҨԏƧ>νϲŊÊσυ˛φʼРӡŜȘҜΉҜɸÿŋȲ¯еӮϘʗÕ',
                                                    },
                                        {
                                                        'key': 'uӔҨѼҪƻӨ˵ǢȰз½<Ǭ½ǇǤϥвƦ>;λԡdƿЊɊɌѵ',
                                                        'value': 'ԝПзњ˞ϳӑѻΧԔϮŰǢģ$¥ȎȨѱϵЬѐњѩϾĂҊʤˏǐ',
                                                    },
                                        {
                                                        'key': 'ʜτǺeLҐɘǖ0ˮŵ˂ҏ¡мâәƧ˷Ο',
                                                        'value': 'ȫśIƱΟȰΈʚҍºҢŏҒӒ}ԕ÷õГѯԧ¨λƲ×ΧǴϱŘϙ',
                                                    },
                                        {
                                                        'key': 'ЁʡŘħƼTϲɤДдо',
                                                        'value': 'ͱ[ә˕İΤƧņ;ʔȃ˾ɓȎґǉӷûҴфɞъԫˇѮӓƘЩĢӐ',
                                                    },
                                    ],
                        },
                    'comment': 'ή˚.ƵҰӑ\u0383ÐЦïåɟɝιлȐѭѢфſϧˈ«\x8dϐś+ӝƫɖ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                '-',
            ],

            'bindings': [
            ],

        },
    ),
]


class ConfigurationStateTest(unittest.TestCase):
    """
    Tests for ConfigurationState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ConfigurationState.parse_data(test_data)
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
        for test_name, test_data in CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ConfigurationState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='bindings', name='ConfigurationState'),
            ),

        ),
    ),

]


CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'bindings': {
                'sequence_type': 'sequence',
                'master_sequence': [
                    'Ƭñɱǵ9ГЖӋԠϷһȶǱű҃ňʈd҆ɸ¼¥Ɖ³P˓мƶƂΠ',
                    'ϩʵ',
                    'ØeúϏëǢì©ɿ»şʺȠÒƪԊҊа˚',
                    'ɍɟǵbъȿό˺ζčOCɱϪȥȠԤZʕ',
                    'Ѯԗ/йԮθӵƢϾ\x85ŴԥѣɢȹØшѢ\x8aч',
                    'ѩǶpх˯ƷȴʇˠҌԈƮʼϫąϡˠшǈʙӸ',
                    'ǘ˙ÆӑԈΩʯȜѾʨɞѯɉӸ}Ϯ\x86ϋœӻУWǬzӘϩ',
                    'Ԋҝǃ®φϯɘЋҍǣћӒѡwǓ',
                    'ĉѯǝˠɋԤNͶîʵJԮέӒdļì',
                    'Ұº',
                ],
                'bindings': [
                    {
                            'keys': [
                                        'ά\x97#Ľ\xad<ԋʝɬ\x8eϘʇȯˁȾŸѺЭĆӥˉļɶ',
                                        'ȠΆӤƺƟѦƤ\x92ˋ\x83Ϻaì˨ʜ¡˪ƔșʞϘg¼ʸӨȣ6ɐ҅',
                                        'γ\x81ñ±ƍÅĶϸąǑӛɮşӹvύǒȚſөͿț˜п²J',
                                        'ȧˠěǱÆ#\x81ʅƅҟґ',
                                        '»ȴʛɗәΰѺɞì°˞ÍбɾeƗî\x83±ŉ˚ҬÌłώúӆ˭кƭ',
                                        'ιƶƌλˈβЀГњʏðʆÕ',
                                        'ȵȱƭƍΊӨĪӣ^\u038dΒȳТƣӫŴ',
                                        'ʵůЂɲžy',
                                    ],
                            'event': {
                                        'target_id': '_ȞЎŘԏĴ»ϯɃÁ\x9dӾ¯Á˛ʬҾԁ҈|Ξɫ¸tÅǪ]ӥѩɰ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ϟϸҕϯԀǛԉѠϳӳŧ˳Ӣϐ.\x81Β',
                                                                            'value': 'Ƒ˫ЮНċʮΆƘϲʔŃŴɢҴЖɛòӓºĖԪΠƴΰʟҏGψ^˓',
                                                                        },
                                                        {
                                                                            'key': 'ɮӲʛʔӜǼŅʷЮЬǚǶҹҥĊўɽӲпʜŸ+ŃS',
                                                                            'value': 'ˤįƥѩŤϫ¼ǮΓȸǆò0҇ȒФ\x8eϧ²ΨŴθƙĞӶԋĞԍƥ˃',
                                                                        },
                                                        {
                                                                            'key': 'ùPͶҶÕʂԀΖϣȝЗŪ½ŗŵпҝė',
                                                                            'value': 'ÕȲÍƎsg\x8eʮǢˆɍĬƘԕƸӥСƜʒɍœǑϦϔƂΐ«ĠƘʸ',
                                                                        },
                                                        {
                                                                            'key': 'ӔεӚԆ\x9dҮūŅμӪөĿϳ]Ԇ¾Óʃ_ɑ\u0381˒ò',
                                                                            'value': 'ҺǶӗōȆȢĠǤѥѩϿĜÍǘƜɠèˍиǬöƕҒɗȬąŬʾƲě',
                                                                        },
                                                        {
                                                                            'key': 'ˎ\x94ĺσǽkƧӠ˨ϷʗΡɵӤĖ\u0379ʺàѷǁˑÿ˃ЀК',
                                                                            'value': 'Ĉ¾ҵӦƙҴѻûКʦƇʹØтŬ£ŊŴ\x8fԁϷӵĘʆǡêʭƆϱ;',
                                                                        },
                                                        {
                                                                            'key': 'ɴɌtƞʲɨ˶ĵˑѝWĆƘ}ҤφȠҾҠњ˄WƄ˾ӒБӌC\u0379A',
                                                                            'value': 'ΐшΜқɏѩĲ҅љĶʵ^фϬʱưςӓÞʼʜȧǹϻόFƉӞ˗ν',
                                                                        },
                                                        {
                                                                            'key': 'ҿ|ҖϦʍϬƂЙΉţʄ¯˱Æ',
                                                                            'value': 'ϘǙѯͱȑʌ\x94ǀãИθL\x93ЇȝĄӬѧӼͿ\u0379Ĺƽƪˇлǚ.>Ɇ',
                                                                        },
                                                        {
                                                                            'key': 'æԎƖȺaŒ˃ˠДϲʥUãqKIĄѸǠѬɁŜӧō˒ɞЩӵǩë',
                                                                            'value': 'ƥҨAĦα÷ЛӯƸɤѯԓłţ\u038bњưМʝXýíή¢ȒſŹȸыɫ',
                                                                        },
                                                        {
                                                                            'key': 'Ӥ˄ǒϡƵƂËЎȉǫԟʅέўӇʸövДȝŻҕpǠŁƎήƼÚҏ',
                                                                            'value': 'ľȇĻƅγȒØʰǜȮӻȯϚňӨǠĘóżÈɕīǇ\x92ҕdОĵÎР',
                                                                        },
                                                        {
                                                                            'key': 'Ҁʽȑ{Ҿй¦ɝɇėΖӸŴӎкϑ:Ӫ\u03a2ЀĻñĐāӶϋľɑԏģ',
                                                                            'value': 'Ʊůɀ6ƾͻњ8Ӓɀ˓Źǚ·ЄӦӀņƣ˺ьǴǤóƮңΎһhʹ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ўϲЫű҃Ǵđń˱ʹˀßĊ{Ψρ˸ϖmEϑΟǋɦCłϳМσΧ',
                        },
                    {
                            'keys': [
                                        '&ӭ?УʿԪϹɻŘӆψКŀлһŌ',
                                        'ɭˡӈ>Ăň',
                                        'ІӌѦȈ',
                                        'ŉҥʞΜͱҘɔƣӝεХý>Ȣ¶ģÙƽǢ',
                                        'ϒʖƻюҴԗ=ϪO',
                                        'ΚżОŦӻЊŻ',
                                        'ú»ͿͶǳӰƘŞϠHĬ$ľґҾɻ]ɌÕӟэώɯӃ¨',
                                    ],
                            'event': {
                                        'target_id': 'Ƿ£ӵÈɂęӱ\x81ŤӹоɊәӱˍӉ˖Ќ΅ȁ\x93ʪңӳR',
                                        'parameters': [
                                                        {
                                                                            'key': 'ĳĨӾ\u038bКȶkЙ\x9aʂȖЊĤӸUÖǊϺòżòϠǄңŒαӃ·ήϕ',
                                                                            'value': 'ÜơθÖ͵³ɄÌǛŪ%ɮϞҿ˙χӭǇ¯Ɉʷηcϯήǲưƚ\x86Ʉ',
                                                                        },
                                                        {
                                                                            'key': 'ƹğ\x9fɜ+´tΧɽҖŵ´àіИΗɚɍɒ\u0380ҋΉƸу«ķĂѤʲҁ',
                                                                            'value': 'ƧӼʪɿÅЮҙƼČ\x95\x98ŒDKɳǅƕΨЕǊƻӒôˏz\x9bŶʔŜȯ',
                                                                        },
                                                        {
                                                                            'key': 'RιɁ˾ϸ¢˶',
                                                                            'value': 'Қ˸ɌƣÙԛűŇÄҒÀǥ·Ư\x8fϬѣt£ΔԔбþдɊÉԆВʐż',
                                                                        },
                                                        {
                                                                            'key': 'Ԭȗ\x99ϊƃŊԢ˟ζ˄ğѽ`ȫӯΠтĺřЃԪоƞԀԂȔσЏˑҸ',
                                                                            'value': '¸\x9då"aĝԡ\u038bƼȉƝȼԭËԬЋEȒɧ\x93Ļɔɹԩ҄ńюˌ\x80Ư',
                                                                        },
                                                        {
                                                                            'key': 'ԎÚʉƵАԧϿȳÝΜΓ˅ŊђԘŖԧѰŹΧӽǧ~ɋ°˘тϷĆǒ',
                                                                            'value': 'ʺԆĹӘŁ˲ÀėϏӴŪ³Ðˠх^ʑϹӾʮӫϸΚ˔ŌŴʗӭӸJ',
                                                                        },
                                                        {
                                                                            'key': 'ǊѰǖԡўŁˈˑʔ\x9f\u038bɌËƩ˝Ŭ;Ȇԗɲћϝðɝ\x8aë×Ϝ˨Ú',
                                                                            'value': 'ҮΤÕʠ҅ȪӫͽЊ\x8cNƵԊд˃ϖɊҠМģѸʈϱԃǞǑčάσʟ',
                                                                        },
                                                        {
                                                                            'key': '\x8dȇφĪҙO˰ѥԡЦѳȹĮϚŹԚʃҟѳϵɬZcшūϕёԢWǝ',
                                                                            'value': 'ĶӘӮȅȧԏԊΣʙϝнʗЕǯαχҲʼɅʳХȱGόρҽţԇҵƛ',
                                                                        },
                                                        {
                                                                            'key': 'a«-úӎϽʷȐ#lfyԞ³ûУƯ\x8dҩEӸ˵qǏŉԁ67Ȗʴ',
                                                                            'value': '«ßѻŴȪЁϨйŸ\u038dΡԥŕˉŢŲǥ˟ĒqҋϽ¯ȸƻĳ˞әЬę',
                                                                        },
                                                        {
                                                                            'key': 'Ģϊн\u0379ю+²áӝĿKҨȒʈПǅƚɒßӼǤґʎХοтăZɃĦ',
                                                                            'value': 'ǛɭͽŌƜҫƉӄŊӃFӯLŏ˹iЄήɝԉԘ8˔Υԣ҈êӋΖİ',
                                                                        },
                                                        {
                                                                            'key': 'ɈħƬlȱȼ˫]҆ɚЁǦ˙ʺʅƖ<һҹâáԪƑǰϐЌ,ԨκϨ',
                                                                            'value': 'ʲ\x95ӄæƘѬʹ҉ҮǤӝƭȽȅ\\ɟшϵΥԀQӄԀυ7ƼԌӝҎŰ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ǞύȬ˸ӲċÇ÷ě\u03a2Üȹ˫ιńÙӼİÃζӵпҔϵŒɓß£ħn',
                        },
                    {
                            'keys': [
                                        ']ìΟ',
                                        'řâǉԌäÖȴɉ\xa0΅ͽēͲɿ',
                                        'ąƔ§ґȬ˛ӋāБ\x82ә\u0380ϏѼЖҮ˷° ',
                                        '\x9eϣď˒mҮƌЖϐϏҿÂʉ',
                                    ],
                            'event': {
                                        'target_id': 'ŅϳŴŕ\x89\x8dӚϧǺßǧѦȃȯCΠǊǉ-ʵ҈Υԁ˩âѯė¸Ԕ1',
                                        'parameters': [
                                                        {
                                                                            'key': 'ÄǾЪхoĲ',
                                                                            'value': 'ʢùǫтƩįȫČǣϤ<˫ПϬɆҶӡͶHwąˁБ¾ǳ·(ˏϫɡ',
                                                                        },
                                                        {
                                                                            'key': 'ЀĝͰҗ¨ŞЕYϸЏĤиĨΞĨԅDҶŮƜ¬lӏįÔˏ',
                                                                            'value': 'Ƌ(ʐ6ƹӉӍӈ¯ϛӐȃäȾΎȩǪȋӃφɗūɐӗȝǄ·˝¼ê',
                                                                        },
                                                        {
                                                                            'key': 'ȵű\\И¹ҳӷνσѿѻųNȟμCˉqԔеɅİƽϑˎŨ\u03a2ӆϘд',
                                                                            'value': 'ѥXƸѡӹε-ǿϟяsəòϢʱ\x7fϛˈШіͱūƌǬβуéͺǁѴ',
                                                                        },
                                                        {
                                                                            'key': 'Ӫ',
                                                                            'value': 'Ɔ£wĜřѻ҇ƸԞÄΦΗȸ,ţӵvќʔĤҩǚƉɎԭƮ;ЂϤй',
                                                                        },
                                                        {
                                                                            'key': 'ӊʏгОȍļˋ«µсĥƭ]ǇѓƞóϐҊʃͿȈ3дɬӰ˹Ğáͱ',
                                                                            'value': 'ѝϗũɐ\x93ǙϿѫϵ΅ŃeʓœYҥϤPҗȬƺϢcԥʺɇƎўÉÄ',
                                                                        },
                                                        {
                                                                            'key': 'ґǳɣ˳ѹvϧéÌҝʒѱțӧʝЯӛĺǙмĴϜȨѿʒҴΓѾͼĹ',
                                                                            'value': 'ƉːǫÊÛчН^ǚ҃ŝáG˰ʜ҇\x7f#рӵŪÊё\x86ūȘ˶\x94ěʽ',
                                                                        },
                                                        {
                                                                            'key': 'ȑѶϤ¤ǴƊÔ҇ϤŖǖϲʥαҐǜƖ/ӤЀŰǱΣͶȤԥ˛ǹ\x94і',
                                                                            'value': 'ˈJΗÃȕΝʎοŒªÝˍ˚БʜХeԓĥÕŋ˂ˢϒшĐǐȂӼ4',
                                                                        },
                                                        {
                                                                            'key': 'ѪɋɤĐŪƖҊʘȂєҹуĝӘř',
                                                                            'value': 'ϐμ;\xa0ПǴ\x8eΆѢǎԗôĒɋԏƥªȋò\x86ˠȌà\x80ĳϚ\x7fε0¢',
                                                                        },
                                                        {
                                                                            'key': 'ƱʧÔhľҭŃοϼ\u03a2ʨӬӍѦŏƬЕ',
                                                                            'value': 'Ý˛ƳʴǰſʦɧɆԘʪ:ʅ¶ӺªУϪVсΏЮԤžӾsņŔͻσ',
                                                                        },
                                                        {
                                                                            'key': '©ȦʅįѭƝΐǌ',
                                                                            'value': 'ÊӆäѪӑȜʻǉɔПϵȳÅζȶGΫ9јŏʂǂäʆӻʏƊѿŚŔ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'Ɍeɷ\x96ԉç˚ǡɋÅ7ΰкàBÐɍϨӳШϊӋȵɪȢÛèȶϸη',
                        },
                    {
                            'keys': [
                                        'Œ˟ZԣƦȽzВŀɠÄŭЀȑ\x8dȗɺƲɻҦјϗǄ\x7fдϗ',
                                        'ȞɮԀ¢ÒҙЖ¦ȑϩFҥíӃʆʜy¹ΝҪʑҢ',
                                        'Ϻːɨȏ@ɬGѷǖ\u0383ѧˆƷʦ˻\\σӽ\x89Ԏ',
                                        'Ә\x9aеͲjƧɏřϐűͿєԞΒɻÊǻŠ\x8cκīĎ',
                                        'cÕfʻŰYӖ',
                                        'ȕ˻\x98ǪʱңÆȽɯğ-ėÕ',
                                        'Ǖ',
                                        'ȌϠ!³ĩʖ˗ċÒǘưϨjʈԍìlÅΎψΑҌЛ\u0381Ϛє',
                                        'Ȭ˾<ƨωӹëЄƜzѓԉ˭ıҞưұȥǞѽƫϷиʢʼ',
                                        'ǟΉBÛȹȷĵҮҒ҉ąlԕЍԋɥРűƱȶǊǢuļ×ϡ˚э§',
                                    ],
                            'event': {
                                        'target_id': 'ӉǲȃѤ[ǦƝ˫ӫɳЏ<ӤÉ!@4u˴ȍýІɜ˩ËŒǤǛ+Ȥ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ҢȟÕ\x9dΖłԚďБΤŉ\x9bϒƐϴÆ\x89Ǘȓ¢Δш\x9eμҁϜМĽʵӐ',
                                                                            'value': "˪Ŧg\x96ɿÜψ,ѿǅǪΖ\x97ǍŰəϬԣϐÁͼѷĂĹы'ӁϗӔɆ",
                                                                        },
                                                        {
                                                                            'key': 'ѬҋkʓǛȫɍñϗԅŕжͿȡɔǲӂҭǩ<ÝԙɢĢҌ҉ϗ϶ċ',
                                                                            'value': 'řȾɇʴHǽąΆҗìҘȶϚ¤4ȮΧǽ˰ρǈ\x9a9҈ʤ\x86Δɍǌϟ',
                                                                        },
                                                        {
                                                                            'key': 'ҦϫɌˆԈԓӾЌɫϓҭȶƮϾĭҒ˲ѿϾçʁгɮƹ\x9dΰÒ0˸Ê',
                                                                            'value': '¦˞ǪԣʫϑŴyʝÂ¿Ąɲ˕эԄΫ®ƣӵˏȩСѳʠ(ºǪЋȓ',
                                                                        },
                                                        {
                                                                            'key': 'ϺˤȉŕįɉĀόϗǄӚͳ˺ѯЅ¯ƛɒ÷ˁ˴ҽϤǍŀϚҌϬfӁ',
                                                                            'value': "ŭҭ\x93ѧʹҒǮΝíƲЬĲ\x99ɾǂ:ҟˤĩλȐ'Ӹ¬ӤʙĀʜΑï",
                                                                        },
                                                        {
                                                                            'key': 'Ī`=ʪҰøӆ\x84ŵҔԍѕаčӬɋΔӔӅ²˵ΔʧǙν҃Ȫɻԧξ',
                                                                            'value': 'ԧ˧þȼЋϝ҈ɣѲдЪ˶Áҽͱ{ÀѺωѓʫĜŀȗкˌșÎŽȺ',
                                                                        },
                                                        {
                                                                            'key': 'İѹŞΰɗє$/ȨƲΗκƆрĂ·A˱ŝȸ=ĎӞӇlȓŚԡʙā',
                                                                            'value': 'ĎǃԀǧðӲǳԗĔʸˀȄƫorԩҵϪϾʊЌӅ˥ˮɆXԊȗ˚ɸ',
                                                                        },
                                                        {
                                                                            'key': 'ſɪ',
                                                                            'value': 'ȝȷӉƑ\x88ёŰƺǍ˛͵ԐAЪΤöԃНɄηĵČΠӞͷЪƋӐĜȵ',
                                                                        },
                                                        {
                                                                            'key': "˝øѬ&ǕǱ\u0378ŝˈɍnˋʘўţј¯вϱªѭǐ'˶ėӻοʂ$ǜ",
                                                                            'value': 'љЊϟǙ\x9eƫӏЩѵ9ԁńȅҩҞÒ˔ɗJ=ʁǠƵȁϪƾӁŭкβ',
                                                                        },
                                                        {
                                                                            'key': 'ȊӔɏ͵ѮQƓǬтΖӱ\x9c˄ӿбͿ&͵Ѽşоąʑі«t˚Ѕϔɯ',
                                                                            'value': 'Ȩq҆ƶҡ8¯ƀОѢQɡѵəѷLȗ\x87ŏ˯ÁʗͰӹʌʻҒqrѱ',
                                                                        },
                                                        {
                                                                            'key': 'ӭцњ\x99ωȅȆҰЍɟҪɍQЉĪӈɱΩʴƇө¹\u03a2¹ԥ1ǼġЭИ',
                                                                            'value': 'ɔκ]ˢζʿ\x89ԮLЫЅȪˡǌk˹ӡҫ\x8aȖļԂ\u0380ЧÛ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'űλŋ«ʜԓϻ|ӅĹһĈʕċſԤÑΌʚСϚƢǭʀ·ƿüŭ-ơ',
                        },
                    {
                            'keys': [
                                        'ѬǰȚҵýɰТϚԥφƓϴȄкʢƦӂ0',
                                        'ɄѯƅμҵԭŸʆӴȞð\x87ЈǟѽʍÞјʱ!λΊԬ-ϭΗɔʵ˓ͺ',
                                        'ĪíˮʽȺѸșҭ\x8bҝӲԈ´*',
                                        'ʦЋө\x93ƴĞĜŞúˏ',
                                        '˪ϟ\u03a2ϫ\u0379ҭ˵ԐȦȐšxɫȧӌǥǁĨ',
                                        'ΖђьɫŠ',
                                        'ӭφѦЈӃΨE\u0383˵˫ĊǑӁūÌċѷ',
                                        '˝',
                                        'ΐƷÄ¦ίŖцуɘМƆƆԝŢŦʸɌύˀȿ',
                                    ],
                            'event': {
                                        'target_id': "\\Ѧβ_KŹŵĺχюэ¬Ҍ¶ěш'ԅDҪŜ\x91ΦǅсϴÑѨ5Ŕ",
                                        'parameters': [
                                                        {
                                                                            'key': 'ҫϓ',
                                                                            'value': 'ǢŤ·\x8aӱĹÎʔ҃sȷʕǵðÇΠƭ3ĐΆОќǔ$ҳȮϔԓΊʎ',
                                                                        },
                                                        {
                                                                            'key': 'Ăӌŷ\x98ЍѭƠχ>ȂКňΚѼĸɮҩύПϟŠň˻ȽʪԆ˨ȓҤ\x8c',
                                                                            'value': 'úʮȵ!¬ҶŏԀ\u038bə˕ŁȺıƥдѡЪϯЄD˯҆Ў¨˰ǅÖмΈ',
                                                                        },
                                                        {
                                                                            'key': 'ѰGø£ϢϣÎȺǟɑʊ\u0383ЦΟ,Ȱʯ',
                                                                            'value': 'ƑʁѩàŃҎ¨ȬǽϘȣѣҼкé{гęɵ˔\x7f&Ǻ\u0382ӶԦӑNĴҾ',
                                                                        },
                                                        {
                                                                            'key': 'ɬϧİʧȫӳЫҗŤǅč\x8fҭҩǅǑȒ҈ȡƙԎ¹8˯&ŉ',
                                                                            'value': 'ϣӉϰâъŶ҅EӗɈ˂ǘҐ%ȘƺʼԜӧԟӜϡɪϚЈӬȜЪǪƝ',
                                                                        },
                                                        {
                                                                            'key': 'Ҁǐ˜ʹġƷӱʃКίҦǈԟb3νеǨӗøĺ\x87ѸȜҧʜțʡЂɝ',
                                                                            'value': 'ВαǂˁǋƍԚҔƉэōǧŵͰˍҋŹз\x8fΆӘ˚ԞʙΐψʪnΦ˸',
                                                                        },
                                                        {
                                                                            'key': 'ΎȭȨ7Ԩ¾ȵ)ӏɝζVˮ4ȉ',
                                                                            'value': 'ǽќJłƀҶԂӸǳ˜Ǣʓ(ΦƚӗѷșåīɸѐǫȫˀΔͷŅύ¾',
                                                                        },
                                                        {
                                                                            'key': 'ßҟϥЎǕώ҉ĵБҰĆȃƎϏҏÐƦƭӡАӳуɅú',
                                                                            'value': 'ωƎʟϘԎăȹƑŸӅ҂˘ѐҭӼʾ˺ʑţˆVͲɦʭĕθ\x89ȡ˦ҷ',
                                                                        },
                                                        {
                                                                            'key': 'ΠϝȖΫ',
                                                                            'value': 'ӠơƾɃ[Уƪ¤æԠʝƔЛ\x966ʄӍԈʷ\x86ϸ¨҆ЇӚҙƪʙʒƩ',
                                                                        },
                                                        {
                                                                            'key': 'ЫŬӅɠ®ƍЗJNΏÿ>ɹʉƼϩǼŴų҃ȴύȐ',
                                                                            'value': 'ѢőȾϟϷԢÙδ#ԫØɍĚϜ˰ǵǘɻ\x9bȁcŮʗſİÝ҉ѢРè',
                                                                        },
                                                        {
                                                                            'key': '°\x88\x88cҀёʻjŤ˟ŰÁԄԣƜɳȎ˽˖ϘϛˈҵƔȒtĂʐӫϥ',
                                                                            'value': 'Ĝˤ˶ħШ\x7fӔ˛ȯ˻ŔѿАȫ˫ɿƪǵǱŴȫҜƻ/ћ^ɍʃОƶ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ИʤȄȳӞӻŢĠͺʹ\x80ÖɡЁyÕĮɪyʛBӘδ\x97Ԏ½Ȣ+¤Э',
                        },
                    {
                            'keys': [
                                        ';DɑFʄʊȚϱȐ˾ԌɫƘχƐхѬϴШˀӺÙԜ',
                                        'þκȥâБΚȅόНψɪʿЯɢǱȹm\x96ɄӶƄˠ',
                                        'ӕ˅',
                                        'ȮŰҖηöҺҌƗͶƉȅϤAƭѸǼͰ°˞«аðӪƍЌ\xa0¾ʑ',
                                        'ͶŻǂϸĂL҂ĸ!ԕ\x874ȤŤĿĐϚUԋđˋѓӳҔǶеЌӚ\x81Œ',
                                        '×ҩҢŢȚƢґ˙ԩȄͶ϶/ȼʚˁĆƎŸΈɜΞ',
                                        'ȨʃU˂ʘÃѮ˺ɤ\u0381ǌƯ˄ԕ\x9aъΒҧάѶÇё',
                                        'ʎùЂǸİΡϙȋŌѷņӱ',
                                        'ҾșǑѶӵӎқп¾ýј',
                                        'ŋεҷʫÌеԧʗѰ)ÔȀʌƺƮ\x82ȦʺǬěqӞǰЅǧ',
                                    ],
                            'event': {
                                        'target_id': 'ˋοшɢ9҈ϋΗəƮҷЙÝʭūĎνπƇɋǑ\x84ҙđӄ/ԜĢȽƒ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ʣɾнɾ˲\x8bɜӡЦϹ_ Ċ\u038dÙǧɚƾǒΡ÷˱ǲːłɀ\x90ɇÜθ',
                                                                            'value': 'þɬNʵ˕`Āɭśȥȇ˼Ӳ"ӢӍΰÏ\x7fȡ\u0379ɟҤ҆ӥӷЃÛíʂ',
                                                                        },
                                                        {
                                                                            'key': '×ҽĵΪԐȍϦʾ\x9eÆĭkRґћɶƖύˏҹπĦƣƊÑЍȃȎАϰ',
                                                                            'value': 'ϬŗҶęѺĶ%ϥǝĵ#ʴţGFĦØŦԛ˔ȣúƷԁǏq҆йӨǂ',
                                                                        },
                                                        {
                                                                            'key': 'ǪӲŮŻÖĜҦƙÞӄІBʀιҒъФЪǙȑƝƫ˵úťγʤĸªŝ',
                                                                            'value': 'ͿϑӸ˫ӁҫŮЭƳʆʍɋģИǦ_ɑѦͼ΅řƀ\x91Ȏ»\x94ʌӟҶc',
                                                                        },
                                                        {
                                                                            'key': 'įȢ˃ť҈ε}΅Ȇɑӵ\x9d˃ύϓϚÝҾҘʼȴҎԦ˂ʼȱϼЁҎ"',
                                                                            'value': '3gЙƼ÷ЩӖғĽЁрςԊѬ˝ɱθɮɆԣǓŦǷcϓН\xadǦʟO',
                                                                        },
                                                        {
                                                                            'key': 'Зȶˊzź~ÿɀΗǉàϥģĽҿɦ˦˫ĵҺȟмԎƢԏɫԥԐĮѿ',
                                                                            'value': 'ƇXѿˬ\u0382ЊѹФίӈ4h˻Κ˾ʚ˄ķͻMĐQΈȔðϐӞǞ\x8eƞ',
                                                                        },
                                                        {
                                                                            'key': 'ŊΑӕӜ˵Ǩ',
                                                                            'value': '9>ϩϠĳɧχӎρѠѥʕζʼȔ\x9aÈĵɁӧƀЄʎ$ʛˏҕȔϦå',
                                                                        },
                                                        {
                                                                            'key': 'ČԞ˯ŤίŴԂOwɱøʬˈѲçΏeӶɪˠԋŀŎЗȗӭΈ6@ǌ',
                                                                            'value': 'нɦЌҧρ˜οýsѿå˥ӸάϿΒ˲ʻƶ\x9b҅ԩƋƂӊӕȩƬ˙ő',
                                                                        },
                                                        {
                                                                            'key': 'ӮȓҐŶŘƲԨɆ˖Ŕ',
                                                                            'value': 'ԙɽÀˉӴҔϡКҫҕɠϤɮƀŨƖқЯ\u0379ͿĤĀœĀЇm˔ǐ҈Ё',
                                                                        },
                                                        {
                                                                            'key': 'âЙ\u038dЄ\x8dƿӼӮԃΒЫ)ʻҟˇю6϶ˠ¨ԚϥҜƉͼˆķϝŦʯ',
                                                                            'value': '˾ҋ.˙ӤȒϘȏìóԥҿŧ\x85\x82¯uʠˁ:ɻ¦Iơϝŀãʂˌ)',
                                                                        },
                                                        {
                                                                            'key': 'ƌsīΟѰűҁѾ¾ǂǫѣƹо˰ɩԥ\x83ƬéȨC\x8bơѹRˬ\x88ǜɪ',
                                                                            'value': 'SѐɦȴˎӀӬͿїŉːӖ˒ӢȂqƩʣäʬԆϑΰȣʴƈ˸ƓŴθ',
                                                                        },
                                                    ],
                                    },
                            'comment': '˸\x89ј}ˏÿʇ\x81įȒɮФεɟԘđҏţ\u0380Ҫ¶ӱȍǣĒƳС\x9eԉЌ',
                        },
                    {
                            'keys': [
                                        '¨ˬƙ',
                                        'ӋƳԑĀǧƣϕjɋѺğ\x92ϷфƭĂԎζƅ',
                                        'ЭѮнԍȧȥҪԘªҁͷ˯ШѦӀΝϙ\x9bǯϧƅ!ĭɧĽҪр҈ѱň',
                                        'nòќӟȞҥ',
                                        'Ѭ¥ʟэʑԬŷΩǾŬ¥wɪɟŮӣǰҶ°ƺ\x8e',
                                        'ӳ\x99χϓʕӇVĆǌæāҩ˭;\xa0',
                                        '/ʶǯϐhҲӮФԚɟǼŷTİǣ½ҁυɩŽДжʫф',
                                        'ϱęΒΎȩΤςìć˲ȸ϶ƒԥ@ƫЎëɉʿɻҖĔȻ˱ȏϫ',
                                    ],
                            'event': {
                                        'target_id': ';ɻХɦ@Ħ`ÙжƲӄlԐàӜͽʒѷʌԖϝϐěɃӑϑ˵ѣ2ư',
                                        'parameters': [
                                                        {
                                                                            'key': 'ʱϤñМԑͼ ŭǩħӫȥѺòƛžΪɏΗ^ҝԫʿȟ˳ƀɡҐԕ˰',
                                                                            'value': 'ǣĤϝƃҼŢǼ¦ԧ<ȕ\x7fĺҮ˂źѴӨͺȼҠ҂γΘȴ_ˊΉЫȼ',
                                                                        },
                                                        {
                                                                            'key': 'ɡŎϫŷƍrҭȮԭΩҞˬԠɼфŉҭӫΖɤ\u0378ΜɄ˪ЇÉҀΠ',
                                                                            'value': 'Īг®Κԝˎj˚ú˵ŴСƏҡ`ˀAԈɿѴɀĎ§ɤƩȼȱɤϲϏ',
                                                                        },
                                                        {
                                                                            'key': 'ɢʎқ\u038bʵήˑǵʗ¿ь˸ͰJ˫ʇłωƸԖҀļ¸ɓΚÞShΛɜ',
                                                                            'value': '\u0383ɇұĴȊѼԁòǴĔo˞ŌIԝԉƅΨ`˝ëɔȋβԨ6φIΤp',
                                                                        },
                                                        {
                                                                            'key': 'ǒ\x90ǊͱпǗÚфÛҡǢƨҔͲčѦԎ0ēԇΦȇíąȃϻ¡ͽøӕ',
                                                                            'value': 'ĢŪЊԕķŸԍÝÅѮɞ¿ŁίĤɎπƅ,ǮƁϛǀѴìѥҗˢǌ0',
                                                                        },
                                                        {
                                                                            'key': 'ƈԇˑʾѨϺĸƳԦԧńŞȬʛϳђζĪӑʿɵDǽяʙхѷjӧζ',
                                                                            'value': 'Ӊ\x8d\x9dʢȰ\x89ΰűϺӿêѱѕ҄В¤zС\x90ԑ¼§Чɛӗԇ¯Ȟäϛ',
                                                                        },
                                                        {
                                                                            'key': 'ǝяђӢˏλʏѬǞ80ӓě\u03a2Ыԡ΅D\x9fʙĦѫ\x90',
                                                                            'value': 'л+ƞɇ\x98ɕӓ¬ĘԙǙȤȒ:\x99Α1ҮӍѱФżҴƒɩūԅʯʜӲ',
                                                                        },
                                                        {
                                                                            'key': '҄ɬŕðöƳ\x85ӠʵõԖӅΫƝ\x84ʺБļӔiԐΔƩǖȑúΦƩҠƣ',
                                                                            'value': 'Agɧλ_ϫхŘԁѬ˅ԞƵǰΊѰȋϜӭǃϩÆн΅ΩԅξȬҡΛ',
                                                                        },
                                                        {
                                                                            'key': '\x8fǦƥТűӲԘһԘϮœҖҮƭқűȪϱyȊâʉϘďˊӜğ,ӖϪ',
                                                                            'value': 'Ӯǈ\x93ŷŭǊUФϩѯйȎЁӴȤϠɶǠԂМʫÖΙƎʱȐϢʚхБ',
                                                                        },
                                                        {
                                                                            'key': 'Ìίrýҹғ÷ǐɖŇYѐoпʜїԘi˱ϐǥͿˤˊëԓΛҡϯ˳',
                                                                            'value': 'ϽБϻƤϮÈӭåVϱєYô0˖ҥ×ԆƙѯqԑǀŐȬȁÈѴʌІ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ΕԒЩɤξ8Е¬Ѝǌ˛ЃҥǀɤŝҗʝǞûUѡ+ɺȐ\u0381ēȍǣѱ',
                        },
                    {
                            'keys': [
                                        'ϡΔ+ǦӋǟɿsӲȸѠé',
                                    ],
                            'event': {
                                        'target_id': 'ƓнǉJԋϕŮώвȆǯЛɤzĄеwЗǺӸÞʫ˒Ңɵ5˱ҩѨͼ',
                                        'parameters': [
                                                        {
                                                                            'key': '˝ҝȤʁʊϥɟӎ\x89КĻ«ÈɶЙǐąƱǱĪ\u0383ŃĝɆɤϞ#ҮΖŭ',
                                                                            'value': 'b\x8eƶӞҪЦĆǕБȑсŹҭ҃ѰȟÒ\x84ҼҰȷϹԈ~ÑÊ_ȔʬӠ',
                                                                        },
                                                        {
                                                                            'key': '¦ϽǇÈʭšϬΛƈÙ҇ɂЄĂɓÂŶúǐӈ?Ɣò\\ϐʗпӏι+',
                                                                            'value': 'ӽɾȷӥˢƜʛɐ`СʑΒWĄ˥ļΡҳɤӝϓȦʮǞΘɞƔϧҡϧ',
                                                                        },
                                                        {
                                                                            'key': 'íXɺУ\x9d\x93˗έqʱЃa˼ЫǍr3ŭԀьǣǕɄƟƴǩˇǉЇ˟',
                                                                            'value': 'ƘҶτȠȦɂsčӑ«ʟј҉Λ^«ŲиȠ˟ƕǼŎύҐά\x85ćтҶ',
                                                                        },
                                                        {
                                                                            'key': 'ЅԢϢΪȝüγӸԋƘȜˮΒѻΕǱi¾њӌϲ\x9dχǲʤ',
                                                                            'value': 'ӕ/ĵ˪ɋёhVοǷР϶ÕвҖĄ¹БɥȓʤƧǆҖă#ŃɃѧŏ',
                                                                        },
                                                        {
                                                                            'key': 'ԧϲČȶ',
                                                                            'value': 'ǱɬьΉǩ\x92\u0381ѵÂҁőӝΦǕǖΓӴҳџϨǛʾɒĎǥԀŨƀэϝ',
                                                                        },
                                                        {
                                                                            'key': 'K˺æºяьӳƾ˰ÉɹЫ~Ō\x89ŁȅȈѻӷǢǇľz',
                                                                            'value': 'ǻƲ҈QͰǦҋЊųƷȘΓѬҝҵ}Ȯā7\x84ǎˈ£nʭȹɹłψȦ',
                                                                        },
                                                        {
                                                                            'key': 'ȅԔɛƗԈϺѥuɌ?ΖĞ(ƌλ"ĒΈѱ\xadӰҟɓƃʻT§ӥȲƅ',
                                                                            'value': 'ӯǹȃɋśϞΑ«ŹæžϢȾԖŀɋ©ԊǞ҈ĹȝϗϰˈȴLЧӍ·',
                                                                        },
                                                        {
                                                                            'key': 'ІӜˁӋʾȱʴҠҔԇèǼӧǞ\x8aƴԀʜӇÔʟҹɹ˭ƾԝʭɆФі',
                                                                            'value': 'ԤΏ)ɘΈ\u038dԞЋˇÕʻĈľԁΕǈ{ʴђϞʶ\x80Γ»ӏȱŹ;ӝŸ',
                                                                        },
                                                        {
                                                                            'key': 'ҲĔӓ@Ϧƾ!ӀĢȢ\x8d~шħĨѪŎǘϐӧƩΚǇSŧZǥõҰѮ',
                                                                            'value': 'ԝ×ìMѴȸ\x9cϳԣѨӬ˱\x96ҏ\u0380˰ӈÐũȩԎsƁƘĻԘÙ҈ҽɟ',
                                                                        },
                                                        {
                                                                            'key': '˯ҠèΫΆ§ΐǆÍЋԩҳǣ',
                                                                            'value': 'ӵϳ%ȩһҟӯǷʌÁҠԅԄȫΑÜɃOӛĜМɑВʺŖхƈƶ˪ˍ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'zЋ@ȌД8\x95ԝƼиѹĿȲɄɺӹӲоȽQƙΓɻЪ:ʁЉ˞ШȜ',
                        },
                    {
                            'keys': [
                                        'țÛɄПʺʭΚԥ΅эҀϞʖʲƱԊѰ˼˰Ԭ˧ϙΉ',
                                        'ԋɫϭτӾƢĀĽΧǨ\u0379Ӱӥm\x93μѫ\x8a˶˥ɘɧʱЂМ',
                                        'ʚҿǍҪŮˌЕŤƷ',
                                        'ӽ˴϶2ʜ',
                                        'ʦϠȰʈМӑȃΐцї',
                                        'ɓԊҰҍΑŴИǃ',
                                        'ԩјÝѲĤΞϊƍŹùŇ',
                                        'ͻѓuĕӫӛҺƳŦʷԄӉԒеψˎú',
                                        'ȘÙ҄Ąŏѳυ»ɋԊ>ԕӒɷMŢʄӎ²Ωѥ',
                                        'Ԯþƞ,ǓɁËé\u0378ЩȲğӬȹȨԮϺǰƇ',
                                    ],
                            'event': {
                                        'target_id': 'ȒɔfLʄƋҎUͱϗȸʩȼįɈ\x8eʴъΛƚŶɾлЁЖFĸˆӫҁ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ȣ¤ΌǲʢǩŎ\u038dTŏƁǴ҃ʴȨėkѹʋʩθǶòžʞŗȂԬҸǆ',
                                                                            'value': '_ɽѹͻâӕßΡ˺Ӎ˰¸ϴŚƘ÷Ư˳ºԙћͲ˪ǸȌѪɅӸ˽đ',
                                                                        },
                                                        {
                                                                            'key': 'ü\x96ǣłҙǟƭ˴ĤϼΗŒԖұөəͿѢȈʎǿéȊAƋƫƊι\x8cʚ',
                                                                            'value': '¬ЈĎÔʃɠǾȆȦǼ˜ЉІŞύĐɭƨƞƐϜɛΥϢҜƂмӒűϿ',
                                                                        },
                                                        {
                                                                            'key': 'ŰΆ÷ȫЩӅŴvЭƄŒXɫŢј¶ϪʍʰªԠ\u0379xȨǿ˵ōдȻΕ',
                                                                            'value': 'ӻҢȿм<ʌюѬƃǜɺʝԆĽŇ0ŬķÍЅ¬w\x7fԙģɁ~żԬѷ',
                                                                        },
                                                        {
                                                                            'key': 'ӹӪβmæľȊȯΣϋö϶ȩǿοӏѿɄʁɷϑđɈёъҁ΄ǁӗӗ',
                                                                            'value': 'ӨҭϙɸЗĮ\x88ɃēʴGѧÞ\x99ώ4ƻφŗęɐȣŠ<ӌͿ´ȫɭÉ',
                                                                        },
                                                        {
                                                                            'key': 'ĉԤǬǏqԈЋƔˬȦΉԂɀώϔYļɊéĳŕˍʿΪ¾èēxʹѝ',
                                                                            'value': 'ȂҩҦłԕ´ȱďԬԢ8ơ\x82\x94\u0379әƄUҾņǿОїƽϰѢʔǠԏ˼',
                                                                        },
                                                        {
                                                                            'key': 'ψüďγ`ӌөӤϣϯ\x8dË˫łþƘ\x83Ǖʹ\x81É¯ǪҘ\x8aʉŇƚƮԦ',
                                                                            'value': 'ΪҁȣɃɪòǒφʓ˜ҘʮрÕϐĈԏґƉɿ:ǪÉ\x99rΦ=ʨӤԐ',
                                                                        },
                                                        {
                                                                            'key': 'ӆӞĕ',
                                                                            'value': 'ҤӤǌWҘѻόҤ©«īĦkǯͼыŠң҇ĭˌǝϠĪʩϷyĎǁȓ',
                                                                        },
                                                        {
                                                                            'key': 'ϊPƩ½ҌȄŃχҢƅŪ˳xǦûzɭɫЉɸÃǎĺҺІϋӚƨķѠ',
                                                                            'value': 'ľƆӵ\u0381Ѽ\u0379ǫʌӾģĤϕϴɣˋҕϧƐș˛ɚUơˎáͷӇρ\u0383ο',
                                                                        },
                                                        {
                                                                            'key': 'ШҴȀ˓ŔǎуžǶΖ°ȱхʽ§Âίӑʒƍά?ēaЃʙxӬϛo',
                                                                            'value': 'жɆ3ҡҕ:тчҫŊԌԦͶjÃѫ\u0378ǜЂϪқ´Υ҄ĺɳǷǿΟw',
                                                                        },
                                                        {
                                                                            'key': 'ůÒɂӫĐşҨϲɕΖȉ\x99ϘӒѲў<ѱȩ\x83Σԑ\x9aČbȩƅЧΑɯ',
                                                                            'value': 'ӖЫǶƇΆάўwӹ\x8fʫӖɘ!ШǳǐōτхɤӯԃɤʒƊԣ\x81űƳ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'üɅÇİҕƧ\x94ʩσƊǯˈû¨Ǚ}°ŵǭс¯ʠŇ¦ѤӹƪԎϘʶ',
                        },
                    {
                            'keys': [
                                        'ԤŏǻʰT\x8cĵΟϿ\x92ʜțʘ!ǆ&˸',
                                        'ӋʄΌėĚϥʀǦǐΎУɰĽшɿ·ňҌĽѣȻǒƦŷρʣӝѸӝx',
                                    ],
                            'event': {
                                        'target_id': 'ğɴ\u0379ȼϛАʏʢÉǷҶň˒˄ȩԀ˂ҺŒÑϏϑԊǂѦĵƍҁʩĖ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ζŏұ)Β҆BʀʧơԃҵŚϽӁʐӡĄ1ȍǊЇȲɎǞ{ýʭǑӑ',
                                                                            'value': 'ȶŔ\u038bКûþĩЮФ¼ˉØʍЏȞΘӎŢчǴ$1ԫͲʕŹɌŗic',
                                                                        },
                                                        {
                                                                            'key': 'вǁЬӮҳԡǷ]®ЏűŦªӟÌ@ɊύĴĆʬƻƸʡfÁć',
                                                                            'value': 'ÑŇ\x94ɁЯĞɟǙǷÙ-ƇӜǩ÷ŐɔјȅġĔʶҼƫĀϺǽѭӹǷ',
                                                                        },
                                                        {
                                                                            'key': 'П«ʽɖɂʰǓќaқѕ҈Ѵξ˘ʗȉŎ>Ӯɽ+ϥԭɵğϲ˷Àб',
                                                                            'value': 'ġŲΑӍʹԢęʄτſĤ˛¯ĩ-ѸӾμǧ˩ΝϼоЍĩŹ4εĊг',
                                                                        },
                                                        {
                                                                            'key': 'ӑȡȲϓήȸ\x9bƃΔ˦ȈȕÏυяĘèš\x96ԩȎҎԎ',
                                                                            'value': 'ů˒ŕpǀж\x84ӄFĺӪçȱƫϻʟÅԇТВSԀ˥ǵҐȗȈѪɫҿ',
                                                                        },
                                                        {
                                                                            'key': 'ӄǶǵϤͷǁɕ҄ЛȧԒŕѾíȕԥƼӧʕďǬ\x8dĻǙӃ\x8aˀDˡґ',
                                                                            'value': 'Ǩūʢ\x81σԧԕθːϣҩӫӴԬā\u0380ÕўϽɺ§ƿѡǱJ\u0379ØԘ=^',
                                                                        },
                                                        {
                                                                            'key': '\u0380ˀɖЅџ¦˸ԇ{ӣφԫΧ-ęηÒÄЮˣĭ&ǰԨюцřĩӳұ',
                                                                            'value': 'ԭƛ#˼ʶӆϜɹӀϊ\x84ʰɷϲ8{¤ǌɦʮζТҖ,˔ҍ˩\x8cΕд',
                                                                        },
                                                        {
                                                                            'key': '\x9eίϏĸóѢ˴ȝŝ҉ƶ~ʹ\x96çԇ˃\x95˥ʮϪÑƛʟCĀŇӧͶҏ',
                                                                            'value': '¿Ȭѽĸњȉ"ɮ¡ʫԏțſŘћƅԝԐüOfȊΙǑ\x8aǑӚ\x96ȉɃ',
                                                                        },
                                                        {
                                                                            'key': 'Рϐʝΰ\x98ȢңѺ\x8c˃ѬΘýɳΊ\u0382ĀяѴΕήȢԂǆɍʚЖϘȵё',
                                                                            'value': 'įȬ˭ЕǦȄĘϼԐƶ¡Ǳ\xadσǾɻϺčԍ˓Їʥƅҷ{ѕÉǔ\\ɍ',
                                                                        },
                                                        {
                                                                            'key': 'ѤӂΏѨϘґƏҤaȲЃ§˖ϯʘ:Ǽĭ\x812ʙϵѳѪӦˢßɸƫҁ',
                                                                            'value': 'čƨ¦ʤʓŽ˛ʦXӵиʈ˱ɡ˖DQïѪϰǳǹǉEĳƓԦŔәϪ',
                                                                        },
                                                        {
                                                                            'key': 'ɓϟңѤРˮ˖ǰšЊԑȏӣʴίӲʝȦ˝γϰȇЏćέӂǵÏԠÔ',
                                                                            'value': 'ϩȉд˔ϱȆŸuˏÖňɱȭ\x9cʊĩʖԈǧ˕ȗôŇҾĒºɜΌGǸ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ƀќѮƪѣĬǵҬƿӽč\x9eͻӸǤ¤Ȫˋ҄ĳ\u038dԞƞĤяԤŉȫǗҴ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'bindings': {
                'sequence_type': 'sequence',
                'master_sequence': [
                    'ҽ',
                ],
                'bindings': [
                ],
            },

        },
    ),
]
