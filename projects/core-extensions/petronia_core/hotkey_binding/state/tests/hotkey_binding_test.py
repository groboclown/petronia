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
            'key': 'Ԋ>Ӈ\x94*ԋXɋèMĄĥʦˏȴlřwҺδяǌιlɴʩϭ˛V;',
            'value': 'ȯțѦoқÒǲБȩːВЫǘ\x88ƙƻϡϖҩ¤ԊŰ\x8c\u038dӹJʥÁǫӣ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ϡ',

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
            'target_id': 'ҺήҒһї˩Ǿ˘ÈɲрØʭīԔY³\x9bˢʒÇŏʄȧԜДӑåƂ6',
            'parameters': [
                {
                    'key': 'ȃҕнчÉіǐ\x84ΌҠˌϓɳχɯκʧ\x8býΤ˵ΣǅӍ\x97ϢɢʒvԌ',
                    'value': 'ҝȧ(ƞШӦ˫үòàȎɟβǢԢӓжϋ*˼ƸаʣƞϏǸ˄ɱԊȏ',
                },
                {
                    'key': 'Ƌʟçʍӆǀ¨ЄoҬ±ǌmƫ\x90\x94£\u0382ѫɿXҞΠҋʅҺƨLòƨ',
                    'value': 'ɽ˲ŏÒĂІĥƳʍǊˋĴф!ɑǆʄ÷ʬ˗ƇˋƔΎԅѨϓƣԜʳ',
                },
                {
                    'key': '҂ňǎŎũϛ,Κ>ƹ҃ɳԢʈƨjϩΜʏƯÝŅȤˏǿϡP\xa0ɢʤ',
                    'value': 'ÏĐǲӕƼÅҚŞċ\x8bɓѦˍѮȲԃłϔƮˇʷпЂΥҰ˵Ӗɚҷ°',
                },
                {
                    'key': '\x8bѯƥПŐɵɪǔӹѿ\u038dǹҗŦχlƶΕқӞžѵ˓Ơªʹį[ҝҸ',
                    'value': 'iŲѢű\x83ǛȓӦƑнƛ˷Ѹʯѧқ7ʐŵǜȀӀʉҵŎPѭ§ĎӾ',
                },
                {
                    'key': '˃Ҽқƿҷ\u038b˘ǳϴˀɁҿƣȰļȉɝȴнɿȑÝіαmǹȌϾhÄ',
                    'value': '˰ĜӪʧρАɘєQřήŽǶMÍƋɑʯ§ȴʳνԮʮϐӵΈġ\x9aԔ',
                },
                {
                    'key': 'ϨɷɿŷɊÐԛ',
                    'value': 'ΏŞ»ŉΣˁʙÂuœϏ÷ԅѡđwǺˡҠʢ1Ҋ>ȩаÿȏ\u0380ͽˆ',
                },
                {
                    'key': 'ʒɽɛʈèɕӓχҖлIгΪCΒ',
                    'value': 'ātǄԀ³¿îӗҸƥЌόӛϩō˸ŠɒǃΔˁǢǬƣ˶Гȷƌħĸ',
                },
                {
                    'key': 'νý˒Ϝ˞ĨӺřƨ¶£ԀǬ\x8c˻Ѓӆ±җɈƚ˗ΓɆ6ϢԨɹϷʤ',
                    'value': 'ʻʔĘˈ˟ǻèǨÖɧψ҇ȪЬʯɠӆЅԍäӅԔʄę˧ŌBȻƣζ',
                },
                {
                    'key': 'ξΔћΤò§ȺW·ĜǤťˌӶɏԃаϰη˾',
                    'value': 'ӻͱÒЋĹ:ƅ\x8eġżѠԫϽ#;˃͵ǑűD.źϵƺœϴƇǓәʈ',
                },
                {
                    'key': 'Łџˉ˧ɒϧЈҺɜ*Ұԫċʮҩ?,ŀ˓ŘӲÃΎȾϷ˟ʠȚϟҤ',
                    'value': 'ǋ»¬ǽǡ´ŧӍѳЊ5Ԫϼ¬ϽɔӾbќçĝҬϣÅɇŃӤǖҿŘ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ɍƃшƽӿ',

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
                'ĎӑϓôϣТ\x8aϥɅ^˂]{Ü',
                '\x95īŤԧρƠķԉʘ7ʫԞ',
                'ϔќVɃѯ͵ÜŹɆäWӐ\u0379˴ëõǣKͼλԜǯњ§ĺüԕƈɳ',
                '·ųԚ˟ȱȹӝ',
                'Ԫɉõ϶Ů\x80ƥɭԎвѴąMѢҨ˳ɓҢΘqБϯˌё',
                'Ԣ',
                'Ɔƴɍ҂ɫ˨ˊԀԑ\u038dбѽÚŁʧȃӽaԜƀϿ˔ХŠ',
                'ԔԒƷ҂ŰǁƣѫϩёϣϡȯÞυ¾¼ϮыʚƅϣrɶШƴ',
                'ϲҦԀźʋϙš',
                'ɩǧϜȁϧԑʷɱҼЫʪɱҊ˚ȿ6ԉҬӿ˗ԝ.',
            ],
            'event': {
                'target_id': '$ǸǦƽʜƞ;ӧǻǋ·qƨ˘Ӎҁʇůŝ˷ɇƁĉÜчҽѲӡ;Æ',
                'parameters': [
                    {
                            'key': 'ɑÊБĹʾЩįҦƉӖҬˠE˚=\x8eҎʶ.Ƹɝ¥П\x8dҌω˃Ȝȓк',
                            'value': 'ȰӓъђЦŻʽȎťЁˉą\x87ĿǘƓƘмǺӨԪǹӄĒ6ƈ˅ϤƁő',
                        },
                    {
                            'key': 'ԝ,ƲҵɢӊҤǙ',
                            'value': 'ƇȌ`ҡűąǗμҍeÃǮѮɭήӫвезàĪŤӁ\x8eʿЉ\\îˍˡ',
                        },
                    {
                            'key': 'љ¹bϞˏĒʮѓї0\x9dǅtȱЋӵŨŉϩɴЅƅ½ȴŌӛÝǷ˂ų',
                            'value': 'ǈȣіʃ\x80άjȈάÉɬϝʅIƸԤȅξˑťÉҎҫĲιčУÅϡǮ',
                        },
                    {
                            'key': 'ŤƩ²ЭӛʪåƱ',
                            'value': 'ȼӋΘŌɚʺqˏÆˡĿϡ\x9coƌӍ-Ȩƌđ˚ʲǦҥʠɡѸ\x92ɒm',
                        },
                    {
                            'key': 'ʄјǾРϰ{ԅӭƯɶɎбοҺːΖ0ԒҝѨїѷӻԏƞѩýØ˖?',
                            'value': 'ɸdÒɕѯůΈ˺xǆȅӜҔΎ@\x83fǤļЯ\u038bÀnηJΟQŏӏʂ',
                        },
                    {
                            'key': 'ӅʸΞÝѨӖԦŦƧљBǈÆ',
                            'value': '˳k1ɧ\x99jʁϨѯŤрɦ˯ӚΤĵûpЌɸѸȟ¸ҿˎѠӪԆǥӕ',
                        },
                    {
                            'key': 'ɒʯɋ¬ƈȭÀŭӍ\x94˹ÐϳӇ҂ӶƫęĜи.ƹ',
                            'value': '\xa0ƊȢǾӲњӖ¥ӃsΑЮ΅ǒÇϯԥӽÐϊąԣƵƒеǣǩˈȱΗ',
                        },
                    {
                            'key': 'ϒɃˣƢ}ӂӘħɊόΉ\x81YԤɛ\x94ȴÉĦÀΫŇƭǇŠ˾РӘˑr',
                            'value': 'һφǍ´ȡðϠīǸӠϓӼɉɆ\x9cΌ\x7fЖ\u0383ΩфʇɟɤɅӗÛѣҁȻ',
                        },
                    {
                            'key': '\u038bƥ%ŧʵ%',
                            'value': 'ưεOɖÝέ`ѭʳҶʱϿĝːъǉªĦӨȓʰкˀѵʆ\x89ːǇѯю',
                        },
                    {
                            'key': 'ԮҩјƑїȟÿʡǒԅšȽψ¶ªǷÀԘȮưȮʽüʭλ΅ʦ',
                            'value': 'ԢԫȂΒǣCϚσɠÍʳˣӀЬϓŎřҎӛğˬɢĠˣ¾¤ҋƽ;ķ',
                        },
                ],
            },
            'comment': 'υωƙ˱ӷŐƙ\u038bǂкǔš_ԞǏѿ%\u0382č&ǖɟƼ\x8eČʭĮӵϸǜ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Є',
            ],

            'event': {
                'target_id': 'ЋΞɇʂˌ',
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
            'sequence_type': 'sequence',
            'master_sequence': [
                'Ϸȡ\x8bŌϿ˅\x93',
                '˖ҚОӲ҄ȏΖĸΣÁɊʴϿυƷĉõ',
                'ƔӺíѺјҋӔ',
                '*ǖğʿѲ¦ɤһPȿ4˲îBƤ',
                '\u0382ɑɽѱŧǤѷѱǜҌ',
                'Ӗэªìƾ',
                'ƩæѠǟāУʌ˶ȻѦƋͿ\x9bǆϜˢ~Tϴ',
                'ŏ˗϶ǲȬÛŤдԧȣĚǊȚҤgӵӑȴәȼͳ\x97äƑǕϺЕӲ',
                'ʺ˂KҌ',
                'ӼʩƾĎhʧ\x98ҳ΅ϬӶŬ3ÞʜπΟʺΏˣрńƬҊ',
            ],
            'bindings': [
                {
                    'keys': [
                            '8ʖŸ\x7fãɧΫ\x84ԝЊϨɪӶ\x99ϗf',
                            'ϻΜ',
                            'ԗћѩ\x96u˔_AӡңЊγÙȃ¿ĎζӾŨʜƄƚǾӒӾέȧǷШę',
                            '\x90Aα\u0379ԧѽϦқ',
                            'óԖƘ',
                            'ÊȽӘɌёϲҭƛBҶú΄î¬ԗХԁÄÈϡ@',
                            'ęҖƊΥƯgȘȏŁӣËͷ©ϘȩǊǉġǨХҏԞx·XŘ¹x',
                            'ʂбĎɤеǄ9ŹФÎıѴƷ±ɹǝɫɳԩ',
                            'Ʈ¬ƦˑӺϰŋɞϕͲʣZl¯ψɺҙζˑ',
                            '˵ЊȒ:ϜǍ˲Ʃŏцˤͱ\x8b',
                        ],
                    'event': {
                            'target_id': '˦ɼɶԚѓ»ɐӧȨΆÊê\x94ĵĐÇɲʾɻɇʇdȯ\x88σò¨+÷Ε',
                            'parameters': [
                                        {
                                                        'key': 'å˶ҩϔ\x9eчĶʄˑGAӅȻαϡƊϳѮʘǧƈĮЗӼġĊÃҪƂȫ',
                                                        'value': 'ƻȐĒ\x89˅ˤDӻϪ¡͵\x97Ѭ˻Ԕː²˳зέξ˻ĀĜȏӌĜѰҭɛ',
                                                    },
                                    ],
                        },
                    'comment': 'ʎƊө\x8eП¡˪ġģǚ°ØğӰĔȘͶӲӾәӺвqtYϜҚúжѯ',
                },
                {
                    'keys': [
                            'Ű˰\x8fȰĄǎŤǡɹŝӠŜǧ',
                            'ǖӑ\x83ʒȰƳɪtȄ',
                            '\x87ϭǷϫυӤƌөĳɐҟʩʲÛǇьԋYŉĮϔ',
                            'ψ\x9cҿҘȫεƹΪƬʩėќϬǍɬŁŕϰ\x7fƽј',
                            'мɂԜϾāÞі˙šØΘʫ&ǩˤӐΠɈϼƢЅң\x91',
                            'ěҘ\u0382ӮțΓş',
                            "\x93ΜŻίʣɰӤЭҏĔÅſĞùЭ'tАɑ¤ӵΕУ",
                            '˷Åǅ#ȑӐʽԑ˃Ϻfӧɼ\x9bǐ',
                            'ĵ\x8dϩÇˋĮϖφɌƩƗȃʠʻӘɂœʉʧϧԓQ¹ѸÙѦ',
                            'ЪˀͲũȭΜɉԊέ',
                        ],
                    'event': {
                            'target_id': 'ԫŮƓ\x8dĨԋqЕ\x84\x8cԪȬŌÔΝ}γ˽ŒˁћƉˠЪȖЁŌ¹пÿ',
                            'parameters': [
                                        {
                                                        'key': 'ĆŴәΓ˔ǆɟǭ˘ΉλˎИԠυ',
                                                        'value': 'ВϪơќʸΌǺ¨ΝЁήѢӎʹǴn\x9aīȃȁȚ΅үÐ*üѧĖѹį',
                                                    },
                                        {
                                                        'key': '+ͱи',
                                                        'value': 'EӍͶќԠƚΎˎӚǉԝü˥ЖԭΎ\x8dοÙĞрdɃǢ˃#ʞ\x95ɴҔ',
                                                    },
                                        {
                                                        'key': 'ӳҤȡѮӟƳɂĤ\\',
                                                        'value': 'ʫĎϳƚͶĆқĒӜʓŎɟҚʺǘʐΤθŻȌɢɾїϪˍɒʙҡ˵ν',
                                                    },
                                        {
                                                        'key': 'Әō¬ϒФάΙĢǱ',
                                                        'value': 'ÊɆŀӕ\x7fϗзȒƈϳлȄ¦ɮӨΖƎàцÜǳˉɦƍŜѐc\x91XǞ',
                                                    },
                                        {
                                                        'key': 'Ŵѱ\x98ŭӇğŽ,SрFѐ\x9aѧрԪ!ԂҧӑǚƬŹ\\ћö;ιȪŋ',
                                                        'value': 'ǏˢvЪ¡ȅЊл+ŤǲĦŵāаlʊ1҅ԕԁ4εžŁ|ҩѱЄő',
                                                    },
                                        {
                                                        'key': 'ϷҾʆʕuņ˕ɐ',
                                                        'value': 'Ѓԙ\x85ҋğхă\u038b{ѹʟʉƇғ\u038bǭ˥ÀӅȢђø\x83ƪрҜԗϯɿ:',
                                                    },
                                        {
                                                        'key': 'Ɔ\x97\x85Ӵ,ϫӖƋʲųʊĂКҜȱҔÄ}΄',
                                                        'value': 'ѾȗЄˍGƱ\x90\u0378҉ǢtԑLƅȘʬţӵƉˀоÝÒˌъƱƦԆϘƽ',
                                                    },
                                        {
                                                        'key': 'ǝӂ+ʃeмɹӈŌǵʓѿÂčǯċ§T0ȖԮЮ?åǱX\x9fƯą;',
                                                        'value': '˩ƷG¶ǃɓ9ѕßƩԆŭ͵λň˴ƂϡԥҪ˺ŹΏ)Ķ;ʎŵ\u03a2Ƹ',
                                                    },
                                        {
                                                        'key': 'ԩȯΖϽAː^ƄоvÍġӡωϠӗƮHІș>Ĕӌ',
                                                        'value': '/ԅˎЂϩС±ΕŭԇҘɌŰӖˤϻ˟ʵ`Ь¸ҸŭƿT˾ԘϷѭŻ',
                                                    },
                                        {
                                                        'key': ' ʲһcʘ˪ùVЄǅWÀӯЎЈҸĒ',
                                                        'value': 'aԈ^õ\x85ʂ˖ҽ\u0380 ƋΨ¬ˏνǛâѢȕ˱Щͼǚ\x8bѴŬѺ˘άȉ',
                                                    },
                                    ],
                        },
                    'comment': 'ɘǐΐзƜÃǦ˃ϫʧӶΞӞÕԆʯϾҀӶƏЛ~ШIłϏӇ˒ʨҙ',
                },
                {
                    'keys': [
                            'αџӵӋљÑ_ӷɝ˴βǇʰњ˚Ư\u038dԛˏȯρ»ŽΏьԘϲq',
                            'ѺηȀÍîԬŀÏςàƤ·ԫԎňʀӺǀѝ5ҝϜ˰Ƚ',
                            'ШϴɘȪɨ˭[ЀԇâȅωѐЏʭɳãƽʦԎΣʓԌƿаĳɯѬӰ',
                            'ўŹƞΩɜвѴ',
                            'ȳуˆ¶ˏϚʩʻӊŽhoзǓ˱ˏɡ',
                            'ӟҾμˠÍѕțҨ',
                            'ԮūÌʹĝҖ\x88\x83ʮù¶ȣђ>ҫГԡǝřΩĄʎˀ\u0378Ŧ2Ǔǽ',
                            '\x91ΗҽĖʒȲÒʺǱȊ6ӥ\x81ȅːƆʃ',
                            'ǫƣɗɘНΈԭщŔΗ˪ǟŭӰȰүr®ӬˆŷӁǻѼ¸źĀ~İǤ',
                            '˔ȺђĔƋ',
                        ],
                    'event': {
                            'target_id': 'ǣчŰҧµҹҚԏɲΐΠρŊϷώ°ǘźɊʒԊ˟Ų/ԋΔįЗYϞ',
                            'parameters': [
                                        {
                                                        'key': 'ϽϴЪԩщΠшÔϯͷ=ɨʠΘ\x8eÃҙɥӫ',
                                                        'value': "Нԝċʌˌ_һѕĽØƸǈŲͲȃӍʊүɦŁίƻŬǻ'ЁУy¾ʛ",
                                                    },
                                        {
                                                        'key': 'ÖhғδϏʍБɴ˂ǷǮȕ9КǨˢʌōϨЍБǢưƧτˊšйд\x99',
                                                        'value': '\x8dŞӊљǻƜ˓īɌΒ¤/Књɝ`ɛǸÕӠǺѿŕФɃӶιͲƃŊ',
                                                    },
                                        {
                                                        'key': 'ʴĬ\x88\x97҆öϖǬ˄»ѡľÇ˼ϖ΅өӁƐүӸ˼ӝȶŐϖźʻīΟ',
                                                        'value': 'ǻ\x81ӖZѫɻΙєȖɛʾǐɕąЪγǉϓșӰ´Ӝ\u038dɺˀŤΝǾѮќ',
                                                    },
                                        {
                                                        'key': 'ɷ©˶Иʋ\x8dЇʘӵăʲҮȀҒ\u0382\x8fJʁȻɡˡˇә¢ȽԀî;Ƀу',
                                                        'value': 'ōɔ\u038dΖѡЯ"ʅǼҠʂȇǑúΠƍɮƪģ˾ƦàƖԧ*øŇâͲz',
                                                    },
                                        {
                                                        'key': 'ķɃNNƽ϶ήЌʼѫϼqɦ;˩ЙN˥Ǻ2ӾЀԙYòФѧ˄ÁҐ',
                                                        'value': 'Ӧ˜˰ӽ˫ŮôԦѣǧô˧6ѲȦƬBԩːǔʍýŖȭȷȇĠƶ*Å',
                                                    },
                                        {
                                                        'key': 'ӠȂƿƧç΄\xa0Ɔɂ\x81æäıƍʟȶɃʬ˥¯ŨpǎȑҳөЧȍƉȡ',
                                                        'value': 'ƑÉͼҶЙƧƥҖ˖ЊŝǆaɜƱŀďˈğώšцøΊȈцľȺvҠ',
                                                    },
                                        {
                                                        'key': 'ƁƷѭÜІÙǐ*ˊȣ˫ь·ȓǨύЯХƞԙRĹӛϏɪ¿ȸ',
                                                        'value': 'щЋҷĉϖºŗ˜ɇҢбгԣ}ѢЕìˇÐϏϽӯGԤ\x81ĴȪϞũʃ',
                                                    },
                                        {
                                                        'key': 'ҽµǎΊϚŒǈèťʣǼ˺ЉĸÀǝȵѣϷ·љɇ\x90ӛԩ!ҬʤҌ>',
                                                        'value': 'ÁʊΕҖɦ\x7fśȭξтαːĵȷǟφFÎţL˫èŢ2\u03a2ɶϋĺŝt',
                                                    },
                                        {
                                                        'key': 'ӸаȦȻķўȑӄğlҚŭȾĆćǢӁƾΏӍǔфҫɑ,ǈĪˁΜɎ',
                                                        'value': 'M҉ҎƐǢňȐń¶ԫҭtԀҽȀ\x9cʂ͵Ԏʶˍŋ\x98øǳʚɡɻʒɁ',
                                                    },
                                        {
                                                        'key': 'ɫƏ\x93ҩ˟ŅѩӢťИҪӤʀǽɇɑ\u0379й˫÷ӮƖǔԏ\x83ȏҿʹҢӲ',
                                                        'value': 'qĔ{ҿƂбηɼΆҼϨȿˆəϤɝӖϪțǶɃҏ¢ĳƞǒѐ\x9bʞȢ',
                                                    },
                                    ],
                        },
                    'comment': 'ӹͺiƶԣÇĉdŁȬη΅ˬƒȀӂʸԠȈӈϼҗ!ґԡǢ˝\x80\x83ғ',
                },
                {
                    'keys': [
                            'ʒǧ5ǵœȖ˅ӻ:ӢԩėΞnɞɆϯƪБН˥Ҩƾ',
                            'ɬHŞҕŀ;ӥЛ',
                            ';ʲŖÎ?kӬư\u038błȩĵϗδȰИ',
                            'ƨЬʄӲļ¼˙©ӗñȝ˰,˒˔ˬе',
                            'ҽ˙',
                            'Ͱ~¹ԟνŹЛ˂џ˒Ǫ±ХɢӫǍԛѕ˳ЗŜȁǂoȂʺƎ\x81ҩ',
                            'ȦΑǤήκƾGӝτ¾ǖʅϢѹѣũ¢\u0382ɧŪ~',
                            'ҼѼϡ±ɱeˍїѴũ˳Ő1ƫßƇ¬ІʹȻԑїÒıȋ\x9dŌřўί',
                            '\xa08Tķ,ȵ',
                            'Ӵ·ǭԛ',
                        ],
                    'event': {
                            'target_id': 'ƊԛϲϋɣȌѪŞӪěHӟƦʞ˾;NϺȽѱËXӄεɟұΝύЮɮ',
                            'parameters': [
                                        {
                                                        'key': '\x95ң˂Ѱȴ\xa0ǳ˻ňй§ʈŶˈńԛǧδƒҹųԋΛΪϩǈć˷ư³',
                                                        'value': 'ўfԍϟFɜ8ŻёѽŊ\x96ԌһƸɞƙҦǘϋw¥ҢŅӠƝȏ˫ψϏ',
                                                    },
                                        {
                                                        'key': 'ȞӃвϞ',
                                                        'value': 'ҬsѮμҺӏ¢ǀŞϔEϲϔ˗ÀӲLѠ\x81ӇǑĞƉÓÄ\u0379ЯҜȦD',
                                                    },
                                        {
                                                        'key': 'ԦƜԎSǈŴϠѤʌ˥ŃɔΦjђͻȘĨЯƕϪΠɧӰpĆӦŝʸă',
                                                        'value': '˜үPӿˁԒłćϸʪҏˮљ˲ɠ˃ҁǓƨÈŒŔǿĳя\xadmϳмȟ',
                                                    },
                                        {
                                                        'key': 'ǐˑɅɱɼ҄ț÷ʄӐσәМҗKԅ˷ǡəɩϧӴА҆ȳ©cťǾř',
                                                        'value': 'кѢƑ¹jԝѰӼʚҽ˞öҝŏ˔§ʵΨηŠбѱМœ\x88ϡ˺ãɖԖ',
                                                    },
                                        {
                                                        'key': 'ǝаϢуɛçѢ¬ĀƇҒԍÍj\x82˥҉ǍęΙ˜ŎȯɧґŬ(ԉ#Ǒ',
                                                        'value': 'ÐԝΑĀӉÉΣʕĦʤΏɛ\x96Ψы˽Ғʚʣ\x80ӮˁұѕĘǊ-ѾÖȯ',
                                                    },
                                        {
                                                        'key': 'ÍѰģˆкϰþķgѽϵȺcɻǔņӜĮʖw\x7fŃȧҙ;\u038dυ|˳ă',
                                                        'value': 'ÜӛɕХӾ¿ǄҤȑ҉˄φɀɜȗОȶɐÿӧ҃þȑƂ˞ҏҋϐũǼ',
                                                    },
                                        {
                                                        'key': 'Ľơзғԏ\x93Őˮ(uӄqЕɌɷȞΉǃԫȪʼяɓ]',
                                                        'value': 'ŜŻƀͺҡԆǭєĵәåʊɮȠҿΣżĀǷ=ԦʉӴʇԁǍáʫƯѥ',
                                                    },
                                        {
                                                        'key': 'Ň_ϝƂɚÙưɨԌв7Ě:αƙǴʖƦʳ\u03a2ԥˁǟрсѧΜчϲ¼',
                                                        'value': 'ɱF*ʿķȪԘ\x8dƮ˪ЭȲ\x88ʳňKċϐϣВҐʵԤһç˹ΦĦο\x91',
                                                    },
                                        {
                                                        'key': 'Їʠɵɠȕʪ,ųӘ0ƛ»',
                                                        'value': 'xăДˇѨũĄΒБǩøҳǣɣâ|ɎΥŖȂ\x90ϧ\x87űƥȱǖȴʨǟ',
                                                    },
                                        {
                                                        'key': 'ΚȘÌĞsӫƣǤĨǩǁήÏȼ\u0379ǬȟäAǤКɌӓυ˝ɃɑƩ˃č',
                                                        'value': 'ĞӂȃԒǱұȇʶϼʭȀˇűƅǺʆϑˏƔѲƸϒѯɄũȆήĴχҵ',
                                                    },
                                    ],
                        },
                    'comment': '©Ʋ\x89ԕˣÃˎʆĞ҇ę¥òӀ˂ŬʦОɽÖ˙gư5ȧ~Ъśӈν',
                },
                {
                    'keys': [
                            'ԕ˂Ϗʘ!ҏŃCě϶ǐħʭjǙ|ԓ',
                            'aTˠŁćî^İd`ԣɱӄÔʣȑƞʙъǪɰ½йӵɒɃƼƕȆ',
                            '˯τԪĢ\x7f-ӃȋEȟÀϺ˄āγ¾ϝòȴбΑȈ\x8eԛ±˶ї',
                            '˨ďʴʚʓӟğ1ҾγıǧϠŸǽўӛήђԛЮҴ]fͳò',
                            '·ɭӎϣѐгɤҚŌԗ˼Ɠүϩ΄kŒ',
                            'ĤǺpȨϔөʕŠ',
                            'оǚ±ĖȝӘǘ\x84Ԡ_ɸɔϥˁԧЈӠщӎÈeʛf¿Ӹ΄ƨґ',
                            'АĽʁ',
                            'ҿƁкƇ\x88ɎʫωØ}=˦Ԅ\x9cNŮ\u0380ȇ',
                        ],
                    'event': {
                            'target_id': 'ńHÔѹγˊŖȋlBȝǱ\x81ɔ\x99oϵϡћφϺƑεĆƞǔԔkлÍ',
                            'parameters': [
                                        {
                                                        'key': 'ɉƢā˾ΦиTЖҖӣzӳΒʑӏǜēƦӊ3ѦĮ\x9aaŷ˔ċҴ҃Ѭ',
                                                        'value': 'γƙÓӝϷ\u038dįcϜА»ͼʶө³ϭ˽Ӈɷʦ\u0383jĊлÄΰ\u0383ƶѡɻ',
                                                    },
                                        {
                                                        'key': 'ǠԏʒŐЭӭϽ\x8f,lʠсƒΏř\xadФǰѹҮƼЦĠѣӧƌ˰÷Ǽ\x92',
                                                        'value': 'ǹԝǝDğҭʘǐ϶Җ˩ӨԥƐЂϋȌ˨ӁėƫϮϟŒīŐƺҴ϶Ŵ',
                                                    },
                                        {
                                                        'key': 'ł',
                                                        'value': '˾ԐɲĎΪӚԎήБȴRēєˑŨȻːѽωɠ+ΞıΦѭʒϸӋƨǥ',
                                                    },
                                        {
                                                        'key': '·H]¤ÉͶҊζ˳ԠíәqǜůȂ˴˜\u0379ƨ\u0383ԋԦ-',
                                                        'value': 'ѹ©',
                                                    },
                                        {
                                                        'key': '\\˄ȎƕϴΞќƊÅˌþŽƫvЦǤʾ˟ϏоŗјɣǀςϞÎ\x8bƫ<',
                                                        'value': 'ˈӈ}Ų?ҕÀԄϰ˅mǻǪƑĴĝʋŨǅʓ¹ƕźӀǨϋК*@Ԍ',
                                                    },
                                        {
                                                        'key': 'ΕеɳFиƥ±щϚĬӿň½˗ΑæӑɦӅӳčΈҩȼͰÝΠӼѲԃ',
                                                        'value': 'ӟєǕǻĶƲƻιɔĉÚǪ3lγώаY0ӴѡȒºΎÝԮ˄K˒Ϭ',
                                                    },
                                        {
                                                        'key': 'ή\x93ƳƲӵːҠʙӨ_\xadƠɏçǸďԬȸʱĐӤþæЕǎȩԗʹʊϻ',
                                                        'value': 'HƽLǘ½ѬʨʗχԮǅ˼ɑWЖōˋϟɦϏԦɰΆҭɸѼǺßY\x9f',
                                                    },
                                        {
                                                        'key': 'ȜcЅâȥέÑƧjįΤҏӇĳɭ\u0381ƞÓòƎŐżӲ¨Ґlԣˤxƣ',
                                                        'value': 'ȫƣϬ£ҡǏƮ[ZÞ\u038bņŐȸˈɉʺˬɘМӫҸVэΑʶĦȉӞˌ',
                                                    },
                                        {
                                                        'key': 'Ƹѱǅg<ț\u038dˎɤʺʓʐǉĨ\x86',
                                                        'value': 'ŀΡʙӪȪɔХʣ҈ĶƩXřƜłNţǣӚͿĄ˰ưɇɓţɩɗɡą',
                                                    },
                                        {
                                                        'key': 'ȫѾҎԘПӵLƲġȠ$ϱǋӘʣКԮmаîǻĜŠϬɅƍǌδĸÓ',
                                                        'value': '4ҟԤ˪ʎ ʹάʣ·³ȡЎ˳ϙΛƾŷϠȏӨƫӸĽªȩñѻ ε',
                                                    },
                                    ],
                        },
                    'comment': 'ʎӢнΘ¡ҚѩǥόƞѼӌʏǓӻ&ə\u0382șǍɝ.Өʊ˔ѵȊǜԆҘ',
                },
                {
                    'keys': [
                            "ƝŖĮʥϷ˩ÏÇė/;ɵūІÜʯɎȩɁʮͱ'һÁ",
                            'ƪņӎΰϖӼÔƵǛԐk',
                            'ďķfĭɦ˒ɳəʤǊðʻð',
                            '\u03a2ϓƘӄɣЫƛԠȀԑƅҙ®ǇąφǒĔƟ҃μԚÏƓ',
                            '¥_ϓʽњҶ]ɂʩβˣǫșĉ҇ǔ˲ƕrԆМ',
                            'ÍԔԙ§\x91#ÑОȭʶĳʷӑƓѻə®ȜɘΑōʥƈɶоʣɌǝɦ',
                            'ǟā',
                            '³\x8bǘȆ\x9eʼèхXԪǊǜ*ôD˪α\u0383сӇȉƄɨӰƦąŵ',
                            'ʗƑ*Ͻ˷Ęʴ҅τПŨЃƵÜЁʇÞƾƺ%˲ˈȔρҽː',
                            '΅Щŏ$ӒȇƷγ5ПĈ˻ýqҁĜϯƤόƅͳВ',
                        ],
                    'event': {
                            'target_id': 'ĔŁ˂ˏˊӏ˺ŔÊͽyҞɉǲҐ˒6ŨʪŔůćĳȷǱĉęԀý6',
                            'parameters': [
                                        {
                                                        'key': 'ѽˑвͽǨ˫Ѐř1ķԢȜν΅~ĝ',
                                                        'value': 'Ӹ¤ϻԕ˰҉ԖЫӬϚҴŁ\x86āϼ½EԝaìҬЖiԩОӞ<ȗ҄ϒ',
                                                    },
                                        {
                                                        'key': '¶ƇŃҸɘ˧Ǿţ³ǨɢѓÉə',
                                                        'value': 'дɆÃÍʿЪͼπƆӇŰǝϏ\x91ϷϙȅǷɞѼíҊ¶¸ˤϭˍѯ˸ƚ',
                                                    },
                                        {
                                                        'key': 'ţ҅϶ĂĖúǔϣҲÙɐϮԥаrʇҽĹȆʋýӼŞŰǿҚˍӡΊc',
                                                        'value': 'ԅ˾ЙҢϠΈȶɏ!ҫƨ\x8cʤˋύʵͷӡĤǺˊƄè*ƃԀʜɥæӱ',
                                                    },
                                        {
                                                        'key': 'ÉϑԇԓҘʂРҺʓŁ\x83·ƊұʫȈˌ·˹ŰÅMӛϮǙɂ\x94ˆǝ\x90',
                                                        'value': 'ʯƔ˫ɺʟ˷уǶhǦMúłЗĎӘɭɧІɰǄ\u0383ŁΤң+ʑ˛rǼ',
                                                    },
                                        {
                                                        'key': '\x82ԙѺӓMяȉԉŽˬĆɚhЂȘХ˙ӥϡlǌʣϷƟË˦ρԓҺ\x94',
                                                        'value': 'ѮłʁʝƂ ēσŃ©Ȍϣ[ƜɼƮkȈġȝʽԬҥϜԖ\x91ϜÇӀɓ',
                                                    },
                                        {
                                                        'key': 'ȒӗȇˡʸѨЧĎˇͻ˞Ұȯ>ȰƘ$ʞӚĞҤȄéȥǷɵŖЕĻğ',
                                                        'value': 'υӡǧԖŶʃʦŋöĴkӀÛʈ\x81ʙ\xa0ҬͻГаîѩӶͽȾΈςʻї',
                                                    },
                                        {
                                                        'key': 'ϕȤӞŷъ9\x84Ƥ³V˶ʁĜƷñЩȴԧȠʌҹˇʰ\x86\x9dɠǨƂ˦Ǟ',
                                                        'value': '\x8aǶΫяōƴŜҕëӚɾҍͺџΉӡӍÙΞƚԇƥμǑΞư0=Άҏ',
                                                    },
                                        {
                                                        'key': '\x96\x89ʭ#юƲΨ',
                                                        'value': 'ʒԤrĢ(ΫԎÒԄϐԛąшΣɏǅɸǉ\u0378ĻЁqĩ©ĥΩͿӯоӉ',
                                                    },
                                        {
                                                        'key': 'ŖŪқƵǽvӾÊϰĎǈɻЩԧҁˑfӖƣDƣцҾâ$ѪͼХqӍ',
                                                        'value': 'ǨʘɺºТōʛ¦ʶӏʉԇƒеϲ^ȔHŵђŚ\x87σϜɖзÑ˶ʾˡ',
                                                    },
                                        {
                                                        'key': 'Ƚʆºɳԅ˵fEʙşÞĠѩĪǴэΎÂíҭΕʙΪҽ\x83ûʘƁϽƂ',
                                                        'value': 'ѦÔƯҐ˖ͼÆҥ\x91юϒӌҘ˞ҾŸƙКԘѩƔѧƆΉäʚԢΚƼї',
                                                    },
                                    ],
                        },
                    'comment': 'ǳǅɲЙǪΝ\x90ȼҪʥ\u0378\u038bƇǜIl¢ƠˤԀɰҍȪњκԑŒΔ\x83Ѕ',
                },
                {
                    'keys': [
                            'ƝρˡĄӣɷƋø˙ҁ˙ӡԩĪäǚϷɀ',
                            'ӍĢͽʽƮEҳŉ҇Ƥˮ\x88ǨѫϰĔaƦ«ϖ',
                            'ӸѲȍϔƤԇ˂ҥ҈ɜƀҙťˆTŦŞЀøÇZǥƈ\x96ʌПÑ(',
                            'ӹƨƐϑGԢÞҟ˜˒ȶԊЗӓÊʼϸ˫ȜŉȼVūȭ\u0382',
                            'φкþǋπɔҏ5ӦӖ¯Ɂ˫ùзPĦ\x9fτʺʥv',
                            'ϯĄǟӃūȚІ˶ϱǮǷӬ%ÙƓǗĺŏŰȠř\x8bʶɛρ',
                            'яяϹɳȳŴΰ¦ŨǴέȽΌʚ2ǕȰɈɢƮʟҩԋӏ;ƅťűå',
                            'Ŷ9Ґ',
                            'ǳҹԝ\x89ЏҖӽüɵϥ',
                            'ɝÓ\x84Ԏ³¨ɻ',
                        ],
                    'event': {
                            'target_id': 'ƕqɼӌƉеоԉŋϱŅƈ&6ǎҴŐˁгȂȫ\x86Ź7ƿβǶț\xa0ɸ',
                            'parameters': [
                                        {
                                                        'key': 'ϻϯïĮҰ\x92ƉѪş\x86ѳzŜǽŇĚeLĚλӵ\x9bΣUȻϽʲВǨƐ',
                                                        'value': 'БƴhȬϒŰôˎfȷə×ġ\x98˲ӓýӻԓŧÖÐӐʢńɄłҸϪ˞',
                                                    },
                                        {
                                                        'key': 'ԒϚ\x99',
                                                        'value': 'ĄżzȓϻǙɪFɮÞƴɠ\x8as Ⱥ˻ҝėˁȶĄƾyͱǤɹŧŭƙ',
                                                    },
                                        {
                                                        'key': 'öƍĔҗȜӋʪʯɖɾˠςӨӇȱӟξԋƐщ\x8bˌͱɼõӬëȋćώ',
                                                        'value': '΄ХǱÎșѼΧσ²˴ƳʬΤ\x8eʈδûзˋԙǦƤωmíɇÏ˘Ԋě',
                                                    },
                                        {
                                                        'key': ';»ΥӵԙԅȁȀӼƎȌƾιȴěƕӪБҘԦŐџβԂІԑēЂѾȨ',
                                                        'value': 'ƗȗȔůҩʭѵɟӘōƂƍѻÕgƌœʹϑȉkҮϨʭɯɭμҞ]ā',
                                                    },
                                        {
                                                        'key': 'Ǉȵ',
                                                        'value': 'ԂĽēӧŝѯўΖĹ˜Ҡ˧ЍŹˈ=ʌь˭ɘĆǵζØЅӢʏƒ˼ê',
                                                    },
                                        {
                                                        'key': 'пҾɫΗcƃҟǅƹϞÏԙ^ȁЖ˅ƑǇ˳EϘδӭÀӾŨʷ¾>Ӭ',
                                                        'value': 'Ԕѯ:ЍӑŃБϜǮɠӭƮɻρĠrшҼKѷ҉ϕӒʡ ǓĽūÿđ',
                                                    },
                                        {
                                                        'key': 'ϘæǈϟǸӉ˅łʹ?˺ƼӿįȌŚʉɲαƳ˃ʛÝ^ϛƖόҴÇŨ',
                                                        'value': 'ϻòϫʆ4lɩĵħӖЗĢфƽʱΰĔˮΩ²ғƢӀlӌň˙ƨķ˞',
                                                    },
                                        {
                                                        'key': 'Φ˔ĲҟÛ¿(҆ϋšgЀĸŀΙĐЅ\u0380ʒɰбԟ˯9\x9e\u0379ΫϷȐŐ',
                                                        'value': '¯ӊ˳Ӛƌϗѯб˹˴ǀиԮыŇèәδȮԅȻȰĵʝʫǕϷː˩Ԗ',
                                                    },
                                        {
                                                        'key': 'ʃЌϱ(ҊƸεωèˬʥӌȈαϾϦѫǣɊĕ²ЃǴĖҕҼøʹ',
                                                        'value': 'лԪğҹȁΆШÔɏȝʬԛЬƜĻã\x96âȋŐȖШɶĆҝ˴Żԁ´ʟ',
                                                    },
                                        {
                                                        'key': 'ɥțΕъ҂˔ɓˎюɼa»',
                                                        'value': 'ēĞфţʹ\x90ÀĠģÍ\u0383ĺʥɡǩϸǂĶư҇ɀΟƸΣʒʎΕпːż',
                                                    },
                                    ],
                        },
                    'comment': 'ȾϫĲ0ϷžüǕɐмĄǩĐԗɎͰҗϪȇÒǚȟw\x9fҌœĠƸōǣ',
                },
                {
                    'keys': [
                            'ʞÃķ÷ǔɦҝ-өο\x8dǙ˕ƪу[;ȸ\x81T',
                            'Ўrȉʬʥĵнͳ¿ľē\u03a2\u0380ǩʓφūϨ',
                            'ɺ^ʺǠ2öˬ˝ΣF',
                            'Òŉĭƈ͵¹˳ѝʀхόĭК',
                            '·ʂ\x9cСȹΪŐɧψ/_«ƼГθ\u0383˙ŕǰȣ',
                            'ȮǐϕԅѐƉ',
                            'ŞҬÊşԩˣѰƱҖΆҦѿ1\x92¸μƍIʃĔЏќ',
                            'ΗƑɬʑŬҷʉӂҺˇəʿǳϚГʧ\x9eĬʈԀ',
                            'Ə3ƲвŲTԟÉӴϚfŴЙ@сԠēǩ˒Ϩƪ',
                        ],
                    'event': {
                            'target_id': 'ˏ˂ЅԉȂөðӟώȅРŏԮЗŽұɋ\x89ˣ/hʃӫ˄˙-όùчϧ',
                            'parameters': [
                                        {
                                                        'key': 'Ѫɺ҅ħƙӃ˥°ȘŧƯѬәʁϐ϶ʞʤu˧ɏÕϢƈӳĶϷ',
                                                        'value': 'BϤПFдιԨúLʳôǖɄ5ҏɛƀуɋʮɪЊɍʩƜυůAӣV',
                                                    },
                                        {
                                                        'key': 'ϭŗϏʯ3ԨϯϛŁĽųЌϵ<Ϭ нȇƌȾӁϑʟҹƨʓs˺νˊ',
                                                        'value': 'Ɇ\x9bĽ˄˼-У˂Ƴɛ@ϹÝēʴɭǺƶōͳԮӭŴӀþƥԕӄȜƹ',
                                                    },
                                        {
                                                        'key': 'ЭĬΥʱѴŪӴʛ˱Ћ½KˑӂĩΦˁȲӢƑȟԑŬusҭ8ǌȃӡ',
                                                        'value': 'υх+ëҙÆțϔɜľCěöфӴǶ\x7fи2ǿƧ¶ˍÊɪɞӍǷҜȭ',
                                                    },
                                        {
                                                        'key': "ҩ»xҹƍ˷¨˔ơ'ýɥőұϟƶɑƱƯ˶\x82ʬ\x8f˂ĄcͻȕƎİ",
                                                        'value': 'х;ӢØŶϋӅīϐǺω$ı)°ʳЉМĤΘhʌ8ӄŻĉλίŷĨ',
                                                    },
                                        {
                                                        'key': 'ӣ|ȅ¾ŻĵîʿϞè«ʶƀÿмȈǿǤʖŶΈɧŜ\x9fύӔиμ҇)',
                                                        'value': 'ɉԘɨШØɧʹLҗɏӰ˪ГӘξŊlʨΨԤӊZäơ˹˻ԖвƓơ',
                                                    },
                                        {
                                                        'key': 'ǡøϱ\x86ӨĪǓÁΆѣӔζȤӃ϶ЅˉјƚȡӷϴʚČŏԭŪƌǖϊ',
                                                        'value': 'þӼВĐѩˎӘҗFȷǘ\x8aƪȿǒҽϧϲ%ˡӷƢĄʡАƺæϵȋψ',
                                                    },
                                        {
                                                        'key': 'Fˢ˛ĈŠԞϞǣ˒ΙŽŶˀ˝ҒӎӏˀЉɻįҌрʕͶ҆',
                                                        'value': '0ƼǋΏ˥ɀϴԣȶӆā»˃¨Ϭ§ǇðЬľȶэҝŖ§тѝÅǰƊ',
                                                    },
                                        {
                                                        'key': '\u0380˲нť§ѻӱĦϞӞxҠ@˹ȭĶǮɤ\x8bǀíȴɇ\u0383ә˅ɰΪʱӚ',
                                                        'value': 'ȓԖbрρͽĒɹ˞·ŖӁÔȻҜóďԊǘŗҌȮźӰ²ªҨzӓД',
                                                    },
                                        {
                                                        'key': 'ˌˮǿǨʗңҡѐǣŲһĨơĤǚϸI\u0381Ɩ.ɐƾѰѵȌǗǮԦɼӝ',
                                                        'value': 'Ҋȼð~ˑԠɢŌҠΥˡĸԀûɦ¬ƗԦĝϕǇǇɰȦʒY®3ɬӭ',
                                                    },
                                        {
                                                        'key': 'ЩҏǺɮϟөńēˎǒņɴĥЭʉ˯ǷҔƷɑѸì\u0382οГđ¬ӋӔɎ',
                                                        'value': 'ČͺvΟˏƥϴПpƼϿ4ȼèɶʁʙʧԌ˴ĉŭο˝Ȥ˅ùȂЂɮ',
                                                    },
                                    ],
                        },
                    'comment': 'рɩжЁЪNȋˏˋΰ÷ʓÑсʷĢʅԬƆÏG҆і0©2ȴƔä˸',
                },
                {
                    'keys': [
                            'Ԇ°ǡ`Ԝː\u038bҋʥӣƣEƽʱŖӈӞ\x8bӒĉé˩ӻùĊƨċςеж',
                            'Д~˃÷ӣΖƜϴΐňdY',
                            'ÊĆPƁʳ҆ωȎ}',
                            'ȷϚ§Õ\\җȋάφХП',
                            'ӺҾϡЉƞΌҞδθġżўϗϳǏɭ&áÿ˚Ī\x9c',
                            'ĀӵĩŽ˷ԡň҈ΠȒɔÇɤºgÇѦϼŗƩ>¤˻ϙϿz',
                            'ɍұǘЪǣ҆ʥ',
                            '\x9eʼӓҢÁȳǤͱҏ',
                            'Ǐƨľǽƶœɖͽ\x96',
                            '҇ŷн',
                        ],
                    'event': {
                            'target_id': 'öҙX"\x8dɿИӱǢ"ĳȯ\xad΄ΰŘɔгƅ\x87§ЀԐǜ½ԗѩШĽӤ',
                            'parameters': [
                                        {
                                                        'key': 'ǊӦĪӓԭ҇ĄЩɱƉÿŦԘЈԋǾˏ˔à϶ÚԪ',
                                                        'value': 'ȏΨʱӼυғѣƓǖǲtɧʡӤ˫ċ˲ɷďVԡυЏѩ˸ϑȍʭÁų',
                                                    },
                                        {
                                                        'key': 'ΐ\x9bǿҷ~ЄʥėӲ\x8eʕҝŝӥȏZ҅ЗЍΝǲӂӟҎ#Ȃϗĺόɾ',
                                                        'value': '\x85bʁßʘƻXúĐίɭĦж\x8d\x9fłʬДs\u0380ҥϵƓ\x86ƽиĶДӃϬ',
                                                    },
                                        {
                                                        'key': 'ȇƨƂАӔŻîÂѝϙÊŉ˱ȝĠэґƙǉǷɤϿɟŐ˒чĨ΅Ĺҋ',
                                                        'value': 'һѫĝĴ˪φƅȦËBҏ˾ÄҽҌˆƣÚь;ŢηӍѶȪхƠ/щҪ',
                                                    },
                                        {
                                                        'key': '-\x85Ҽˇ˄ӣҕǞƏȋʭʀԢˏ\u038b˱Γѝvş˞ɄϟΌǝĥÅƝԄΉ',
                                                        'value': 'ˇɴЃàФƙΚʪôùЌgȞеƌʟµʒr¥ɣӁɳŻӮSĂťTǱ',
                                                    },
                                        {
                                                        'key': 'ǸăěƎǁ[ŵèǣ\x9bˇҹҍͳ¤\u038bʯҴ§ν:íŭǑD©ŪɶθŶ',
                                                        'value': '¼øĻȖǗєƽÍҠʩϜќ\x97Ƶϥg\x9fρѷǃŀ#ƋŎџҰƖđŖϑ',
                                                    },
                                        {
                                                        'key': 'ȳv',
                                                        'value': '˭ȜÁ&ТӃ˭Ϣ+eӲΫʉ΄ңĦ\x96ҘӧūÌΞ\x99ǻǒԑɃХ"ƍ',
                                                    },
                                        {
                                                        'key': 'ƁǅǽŰ1ӌȋȆ¹ыÿrҐϲƱśфёƙ',
                                                        'value': 'Âи¿ƍΞ΄ԮɜžŸ¡ŋȏ\x85λϝǯˮҤNҥԂ¬Ԓɺ˰ɦȼȦҦ',
                                                    },
                                        {
                                                        'key': 'ŇιЌƇΪХԨǭ\u0379ϳɕɮǛɕҬʩȷ˒ˈΩźìԜʉǸ\x80ʶĊӕш',
                                                        'value': '҉ŀɾԜŐ²ӥԤъ˵ϪũҔşƍǾȭŢTϠӻļѶȾ®ʿŊƝɘϺ',
                                                    },
                                        {
                                                        'key': 'ОǛɢο\x92ǭǣ·ǋАďЪΤ҅',
                                                        'value': 'ɥӲӲпΰѹÄžǎǆóѷëWҜƧͷќϘŢjӢ˦ȣђŐǏµ;ł',
                                                    },
                                        {
                                                        'key': 'әʯoҩȝU˓ЌϕȑȕоǰκͷǖͽΉʄə7Ȕ',
                                                        'value': 'ŻǐδəŲ°ɰäєы\x8eӯ\x88ɜÿ˺ÓπϻȔӅԈȠāˮʀˍ\x8dȝш',
                                                    },
                                    ],
                        },
                    'comment': 'ǿԙʤ϶îӿҿ~ʕ7ŅĦQͽͳɡʄԧĹϛēԠWοœѭȳȺİҴ',
                },
                {
                    'keys': [
                            'ӷ³ƾśĩϴβΒǃòҨ',
                            'ʞ˅bȔƠόȖ¨ЬџȋӭŐƑη',
                            'Ӭŋœӷ¸μŝнΰ¼ΔΫ˦ЊõÅ\x88ЗѨϲΗО˧',
                            'ȃŖ˝ȧіѿd',
                            'ƙǌѷ˙ɪİǚӴƬȤӸ¢ΛVһәƍѲʃƌѭҿξýиԒӂ˺×Ԓ',
                            'ξƿҭċɌТњӨЕɣѴ˖ʇʤ',
                            'ËьiɘҵҊӢķϥɣвҩқһĥӝ˚\x85ȾµϟɝϤΘ\u0379Ⱥ˩ӁǿĖ',
                            'ɤϏ',
                            "ϜƲŎǿԝΈҩеºӺnoӑɦ(Ŀ'ǸͿ°ƄЈӀϰ˲Ð\u0378",
                            'űқȉ˱Ǳƈ',
                        ],
                    'event': {
                            'target_id': 'ŽʆȌҕOԏöťȴpyύ˓ʛhUɧȷϐÞųұѐǖӞŊƳэɶĨ',
                            'parameters': [
                                        {
                                                        'key': 'ҒҞФͿҏƜǝЊЦŲŐɄӌӠ¶ʹˌ<Ѻáhtώ',
                                                        'value': '˗ǀϓŝæǦϢЙ˾ΞԤ©ҢƍԪʔȲ=ԓԕťĎбϻĵÜŐͽ˗É',
                                                    },
                                        {
                                                        'key': '\u0381ËfѺԀюǲwΌѤӾāƏӽ',
                                                        'value': 'ǵԒЮУŎȡ˪"Ϗ²ˋɖ,\u0380\xadΏĲȏӝϭ[ƬљˍͿŷ8ʪǿƘ',
                                                    },
                                        {
                                                        'key': 'κΤWƳƊĵȂ\x8c',
                                                        'value': 'ϖδďϢ)ϊєʒJȊɊ\x99ǯ˼\x96ĈӧԣҟѶċΟӧбҦȃǳʯͼӃ',
                                                    },
                                        {
                                                        'key': 'Ɉ5ґƢӽҎρԍįpȎђͲȁϔū҆ϷӆǨƴ˵\x8fąӶũ˨Āηӈ',
                                                        'value': 'éɋψȡʺ\x96Ә*Ѫʝϟˉҗθ\x97\x87ϕӳ ǹ˒˨ǰďj`ʌѹҢǔ',
                                                    },
                                        {
                                                        'key': "ÀӀɡуӿ˱ӚГ˽ƩӜ[Ⱥð¥ǒǷ'ӵġ¶ǛǒȃǦMӌϼӦŻ",
                                                        'value': 'ԣŦѷǟˏŧɞΊJԎȗϴjĿǈƻ˽ǫъɛѹĄӖćɇĕѓԃĩ\x8a',
                                                    },
                                        {
                                                        'key': 'Y˅Xˠ\u0380æǍԄʔ',
                                                        'value': 'ϕʚĂȸŉΣ\x9eѦѷ\x8cȮîũŨȚćԦʔɢȜѶοDαʥƂpѽˤ¸',
                                                    },
                                        {
                                                        'key': '˟9ɫĦķәïФƸȖѠʻѕƘȈҢ®\x93ԟʴԡ/ʣԈ˶ʏҥǐɳ¬',
                                                        'value': 'ȟ҄\x8aʸÈʍѩŁáԪ$ĪʓňòΫͰѵ\x93Ӂ\x8fѶёІȱċǩġІҀ',
                                                    },
                                        {
                                                        'key': 'ӥҳҾFʪǹĪҠлԄҸ"ӻª˭ĭҢƹ\u0381ҡ¯}ҊǯДėȢϰшǙ',
                                                        'value': "ҤϳιяnƺȏĤˣƭŊ'ŋäԐ҉§үǤƦȻԘŦǆ˱ҞɭȞҦѥ",
                                                    },
                                        {
                                                        'key': 'πԝ¡ŷÃϱƖɠɲӽҡĮʉƓϥēĒēʺԚǣɢțѡdÚɤζɴt',
                                                        'value': 'ǇПɶ˂ƚʦ˲µ*ҜӭАņʗқǩĔϺʗҢrʏùӫҶΥŻyʩǒ',
                                                    },
                                        {
                                                        'key': 'üĤŹɋϳ<Ԍ&ċψɣμɂʭŻ;ļӇЁȄɷ˟ΤФʾǔ',
                                                        'value': 'ΌΜѩƽÅ\x8dłӌ(ǼˠɆªķȇÇІиʢɟ҅Ћ6ȱÚӕĿàŖɯ',
                                                    },
                                    ],
                        },
                    'comment': 'hӓ˧ζĀƎɍӸƜȶm\u03a2Фĵ¥ƹЏŒkѾŇԣхĔʒɟƲʄϻʰ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'master_sequence': [
                'Ʊ',
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
                'sequence_type': 'meta',
                'master_sequence': [
                    '\x8dÆĦȮͷρ·Ь˦Ь²\x83öΆÞ˜Ӆ=ӯӹ¬\x94҇',
                    'ǩϛѳɐӅԔɝƪő',
                    'ćϘīǀʙȜ\x8cɞǀԙԀǙԄƮѼZӓůăŞΕΟϠŽʄĜ\u038d9',
                    'ҙϛЁƦƝƗӀѧԆ',
                    'ԝѕɦˍϊ\u0383өȰƠœƱԌÄЭπ\x95«ЦǺƎ',
                    'àҡiƪˁдўeï±ŦΐɭǺϘȁɃѻʈӨĞŶӏҠ',
                    'ƹFˉ\x98ΌϊΪlԕ§ЏӁη8ȥϋƕŪ',
                    'ҔѳCӸ\x82ʂƿĕºǭѯʩĳτƈŪѵǬö',
                    'ɗԕƬԝʪʕ\x9aIŪӎĚӾȱҢӪғΡԣģұөĸ˙Ϋʹʯ',
                    'ȰϠƀ˗Ԫ\x89ў;ϝäҏЅϒɞЦ',
                ],
                'bindings': [
                    {
                            'keys': [
                                        '\u0379ʾFӖǔŋ',
                                        'ǆƀ',
                                        '\x8dĠɧЅű_ȝψǯ¨÷x\x8fªqϨӪɝҟǷђȑ',
                                        'Ċҥ˴ëгПѥҸѼȐɪѯϝγƻİǃ}Ŗҡҝ}ȣιÁǕ',
                                        'ҪҬ\u0382Ƽԋ˪ȚҹĥӫɒɖЁπ%ƻɻΌ\x95˸ϐѼãßуқùũ',
                                        'ăǘďēЮ3ʪȺгįʥǶӎϔҿšӼ¯őȀSΉλʂӆ҈',
                                        'ɞ#Ů°ӵҘŷсǇưʢҵÀǏŪƏȋɼÁѮ҇ɫϚЃřĵąƹ',
                                        'ƲѶ¤ЕŇΈđµѡǑϋ¿ЄȻ͵ҏӪǨ˲ɞδƞĘЧ',
                                        'Ϛ\u03a2ƐůƮ\x8eǱǩҶǿѨʾѾϰ',
                                        'ƖҙλįHmʐ³ʢρѓҐΞӗˮȠǨÐ',
                                    ],
                            'event': {
                                        'target_id': 'ΏȨ҃ˎԆǞNҥɓӣЍĴΈ˝ˈǘ\x84ɃԝҙӴˍǡƈѴŬņǤѽȇ',
                                        'parameters': [
                                                        {
                                                                            'key': 'qкΝΚ˨ƦE˗ŲΖ´ĠεӁЍ¯ˣѯ˝όhɜƸȁѢпӫќњă',
                                                                            'value': 'ϩМçБӧʣʆΞҟсӤɐӵ\xadÙƁDǣѧŗƀ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ĬЧ4ЅЀЙʱɄżʋҁ',
                        },
                    {
                            'keys': [
                                        'ƪ',
                                        'ȻÇҤӸÇȂÆӅӸ4ȂëΡ',
                                        'ñҤӢ',
                                        'ňĉӒʋҧƆĠҥʞȳѹǌɫѠϙȓɈ:ҷԒƩǔɾҊʻԗѳɁ',
                                        'ůŴҟбǹaōĐ\x82ӥώˍҘ˻ŰǶȹ҃šϸσҏēӆȸȐѝȼ',
                                        'ҶŲэǋԚªԪԔ;Ζγȉʏ',
                                        'ǔxҠɬƃĸ',
                                        'ʂÐө˨ƇΊɎéϊöƌƱÖɨЉ',
                                        'Ϋ˧ǜϢĒŵɕÍũœнǷ¯ήȳƯɅԐŪÑ',
                                        '-Ƙԏ\u0379Ӥ',
                                    ],
                            'event': {
                                        'target_id': 'ĒҿΒíȌŵʈ0җѱ˴wİ2ҐƪΧɝ˻Ʈҹē#ũÔ>ęԢĚǣ',
                                        'parameters': [
                                                        {
                                                                            'key': 'Ӝʟœ\x96ǳԡӾԄȉӺУȭʠƲáΰŲӦ˨ǌóӫļĹφуƂЀŮɆ',
                                                                            'value': 'ЅҦʽϩҸ˄ϮɮлʥɜɏêмŸ+ԓ˰ƵʏûũԣԡÑѺ_ɛҭѾ',
                                                                        },
                                                        {
                                                                            'key': 'ĺĸ˔b¢Бǘԟ˨\x92НĆϧʍρǿˇїԛǉӁϡǘģԮԇØβжӾ',
                                                                            'value': 'Ȟ\x86ɗλÊͽϥвϵ\x9cҲΛǉЦоɜȱҔҨϳ\xa0ӕǎцԫϐϸΉOҒ',
                                                                        },
                                                        {
                                                                            'key': 'ɛϼkɡ˓˼PĮŖξĉʗYЖѰű0]ЦҟԐʴˀӸǳˬԔȄƷǜ',
                                                                            'value': 'ȑ\x98ůWċƠɦþĄËɿԀ\u0381ɢŠѕԩҲǿ\\ԭӀѴӺʼҺ_фÙƑ',
                                                                        },
                                                        {
                                                                            'key': 'VԓӨ\u03a2ŪͿ˱ȺӼжūˆíϖһʬǧǷØ΅ʾľŢːʵɫљ',
                                                                            'value': 'ĚѲǑ΅οÑțҜǪι˒{ӘҏѬåƆ˚ήǸΦѫҤͲΛßѯ˕Ôɼ',
                                                                        },
                                                        {
                                                                            'key': 'ǻaԑɆ˛ŋӂίžmǸ¹ƪLŴ϶ǖŠ˜ŏƾȼˎӾ³џŨɫЌϺ',
                                                                            'value': 'MǦԝѐzø%ԩƁˌӟȃ¯ȱƣɉ\x9fŁΕ˜ʙɞїŉTôǵʇċȞ',
                                                                        },
                                                        {
                                                                            'key': 'βŋΈҸОƫҳіҎӞ=\x84Ķ',
                                                                            'value': 'Ţ˯˲ɀăҒʐЪėϡˬΕʻǮȜ8ѯɖśȞԤԛƺԄőʻǇϬ@ϙ',
                                                                        },
                                                        {
                                                                            'key': 'ˁΗ/Ҥκʊ˪×Ǚ˧ЋťӃȄrȗҀǦθˁ\x95ԝũҫǯʘΆнĮǌ',
                                                                            'value': 'ŴɶВјřѺʋǅˎɄѿҿϓĲǴӆɊѮ˧ĵѩŘ˧ƪʽƁϙȼԈҩ',
                                                                        },
                                                        {
                                                                            'key': 'vоʼũˌěʾӏёѦЛъ˨ЃӘνͽƠә˕ҹúζ\u0383ϝ\x8aҵїȉԋ',
                                                                            'value': 'd ЃǘʩƼϻf\x90ˡ˭ǜҡóθӘєΈƬiƁŶӤʇӔƞ¼]Ζ˴',
                                                                        },
                                                        {
                                                                            'key': 'Üӑ',
                                                                            'value': 'ԑЎ/Ѓ/ˣPӨί˖҃ƭßїыȅЇĊǘʅĢĸϪŕѷƾƵʤДи',
                                                                        },
                                                        {
                                                                            'key': 'ˇ_ЄĆƮͼԪʩŮÅéԉWXѷ×ôϲԢѼԕ\x92ĉȰȶшŘÅƶЋ',
                                                                            'value': 'ҢǂәFϵˎьĩԫƴɠҢέηԔʥʎɢȦҦӇˣΟ˟ӞӧѰѓ˸р',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ǭΦЋˡj²ëʹԙÎSύϥŀҿΆƕӚģƽЙ\u0379ϵЯʕſ˷ΆÊǧ',
                        },
                    {
                            'keys': [
                                        'ьŸнͷĊ\x98ͷˋ°ȸЮψαǁіʕƚʫѴöѭƷñūѢѷąʹҺҲ',
                                    ],
                            'event': {
                                        'target_id': 'ƯҪ\x92ѯ=ʌƳɺȯΦǣҵȎûș!ϖȆτZɀʼһS˨ĻιĕҡF',
                                        'parameters': [
                                                        {
                                                                            'key': 'ŢŏӦŹåѡɁηȑʺŻӠÉǣΑƇʖ˙ҞÜŕԥϗӓƸŸ·˲ϑ}',
                                                                            'value': 'ŝʷƈÕɶӕǻ;˹Ұƌǧѭҝſĭ\x87зϕǧŏƶŦʥɸʗϛ\x9cҼӽ',
                                                                        },
                                                        {
                                                                            'key': 'Ȱ\x9dÒʱÏϙɭǞdѺƻŎ¼Ӽͺ/ҨԫƄҐӱîҺÊѸɘþĉҢŎ',
                                                                            'value': 'ϙϙˆɚӭǰȟvwвtіƊƋʿҤŔԁ+ÚϔĐӗϡΣӠѦңЙӠ',
                                                                        },
                                                        {
                                                                            'key': 'ѡ˻ȃŴҌĮˌԑ\x96tøÈÎȼƫ"ϔǭaЉԣ\x9eȅȭʥÇǺĐԬÓ',
                                                                            'value': 'ЈԖԎЖ˔ʇ\x97ԠǅƊμ\x96ѓ\x8dƋа¿ӂԘ\x82»˴ðȭSƔµÊѳĈ',
                                                                        },
                                                        {
                                                                            'key': 'ʲϲί',
                                                                            'value': ';q÷љӖǳŖŔҬͳӆȲП\u0378ɘƪȊϡή˒Ӄɨɰ\x98½ǏUӰƹƧ',
                                                                        },
                                                        {
                                                                            'key': 'ӄПԮӕǁÐЂĥ\u0379ќğӔǎÏzӬäѝѕʄ)\x98Ƕ˶ȈĐɨҐνЇ',
                                                                            'value': 'ԋȖ˨ξн¼}Ɵʧ5Ήδӳ\xadΙЩʿ˫ǎӜß3ƔҰΣȼҹͱѕǑ',
                                                                        },
                                                        {
                                                                            'key': 'ˉϯїǧѤĨ\x8c\x90ŶҊ\x8aҙ˩ɑӀĽГɁgo\x87Ż\x85бƼїƐЃɲѷ',
                                                                            'value': 'øӁϰȼ˻ǰɵǌН&ͳ¥ԓˑԞ^Ѹȇʝԑρѡ˴ÎӓѶȖԠȄѓ',
                                                                        },
                                                        {
                                                                            'key': 'ĢΌMēĳƸȪΚȩӁȈˈƵɛӴŎňӹѤϰ˶ξŷʹǎ˸łŕѴp',
                                                                            'value': 'ԗѢί˟НiʏϊuǋÑ\u0381ǲȴǹ[ϻА\u0382ƲɓͳуˍӳŸ\x83Ŋdћ',
                                                                        },
                                                        {
                                                                            'key': 'ǌ͵ˎЕЋŽӰšǔ¡ďʢǰѴ\x9aɎӒËĳ\x85ĩđAèͺ˥Һ~ԇɓ',
                                                                            'value': 'ǝӫԇƬřƻ#Ћчċҙ\x8b;\x9eаԌαƂ4å\x83Ӄĭκб=ůʔʵЖ',
                                                                        },
                                                        {
                                                                            'key': 'ȓʱȿвǜƈϥƑҲҜˣԗJǦʾ×ҭ0ʎǯĹϧɤiɋԆǧх˖ʎ',
                                                                            'value': 'ԠŞãӦӷӏгĒƯȿǪȨȔMԕòɆѸǚԙąҀҡǵcϞϊɴЪϞ',
                                                                        },
                                                        {
                                                                            'key': 'ɚѷϼĆ¢ơĤơɉԦa\x88әǾǑϽ˃Ȭ\x82ýƋŕˈțүÌŮϰгЙ',
                                                                            'value': 'ˢ[\x9aɗ/ðΘ°ØӨ\x82ҪȂҽ0\x94ΎȑQΝʤѡCԝӺȲʤιȀǝ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'yԎʯȮҨӳȵДʰȕ\u0381ɈXл˻ǃβɹЎŘИВԓȻĭϙπϲѣn',
                        },
                    {
                            'keys': [
                                        'ƓfԓЭǩŁҞъ',
                                        'ʭЖ]ȕҢ',
                                        'ȵѡΉ',
                                        '\x83Ŋͳɲ˙',
                                        'ŎŨŝ\xadΘҧλ`ȒҪΏǙµԜӰͰ1±ПԧʊԕԔĽɊӹйЖ%ͺ',
                                    ],
                            'event': {
                                        'target_id': 'ȪǻҤ¥ɔͰҠЁȐƇŢƌƱkĐɏ҃¸çʅŏʍYʋZʥϱŽЪͱ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ȏ˯ɉƗІΣͼ',
                                                                            'value': 'Ŝ;ĊӖľȓҞͷͱҩHƫɧ˷Ǯ\\цӇđͽ+ćӈ»Ѹ¿ɭІľʐ',
                                                                        },
                                                        {
                                                                            'key': 'ЦѪƆΈƍ\x7fµʆ\x86ύʸȼƒˆШ˝ц˗ȴӓǓɻǟˊǬʮ£ѽŁĳ',
                                                                            'value': 'ў²īƵȴԊĝðΘЃϕùɈ\x90҉ƈҵȴȴɌӻɥΝϚɼΆɼѾөÀ',
                                                                        },
                                                        {
                                                                            'key': 'ɕϰƙŔǴҞԊΠĥη;ѺȂɟ_˛\x92ΛІɻͼĤQҋ¤˝ӄȑԮH',
                                                                            'value': 'ė҄ƒʄDƂKԧɝΘįҝчԢǽÚԅϸǐԐɺǊΘǷϯˮҺɥ˯\x97',
                                                                        },
                                                        {
                                                                            'key': 'ȭчǅъÄӔҿˆȮѓэӳwМΛïƂĚƱвī>S˪ˈʡƘɅ¡Ή',
                                                                            'value': "ԝͺϦũħԕ6ņɺӖ'ɥŹʉϋ\x80ɐϽͶӝ\x81СψÇϔ×ŻѡѵЉ",
                                                                        },
                                                        {
                                                                            'key': 'ÊԒƽͳʪљŋЖȔȩԭ×ͽ˦ϼɧэϮЅщȧѻĤԕę˷ǸЄėȥ',
                                                                            'value': 'Τ@ʿԓʂҫɄȔ˨ВѩȶцˣАЪχ¿ȫԄ¤˛Ž˲Ǽ\xadˍÜOӍ',
                                                                        },
                                                        {
                                                                            'key': '˄tӶǆǔǇʆԙәϝ0Γ\x9bĹΞLҾǓ±϶ҮȺīo϶ѿϊӫɹƥ',
                                                                            'value': 'ĮҔɋΦ·ҹƇǚʢ#ͱǣÑȮΜơԆʇŷƧӓƩЖӽоΕ˱\x9bөԛ',
                                                                        },
                                                        {
                                                                            'key': 'õӳėǵýɬȕϽȘʄѣǥřƆӻԨµũёɹ˖ýԨҚѧ',
                                                                            'value': 'ΌƵģň~ɿѮʯӆGόÁǼʐΪǊԌϦхͶŔ\x8aҐĝ\x92ѪĂȋ_0',
                                                                        },
                                                        {
                                                                            'key': 'ĕԬǗԖ˾ʯԮŇ҈ʑҥTЉϰԒÛ˞ұф;ȳİ',
                                                                            'value': 'ȀûƒŨåŋıŏ\x83łčΓ˜^ÞƄӂɥ+жӫ˷\x95ό¨Ӹ˧βƾѠ',
                                                                        },
                                                        {
                                                                            'key': 'ЄɔæƟӦȽªӄ!ĿÃУĔǷǇņΠТęΙѐý',
                                                                            'value': 'ȍѱђҵ*ʽÙ҉ұËчҕ»ƃtƬΏ·ђ\x87ϫѳ«ƹԚҸѦĻŕҖ',
                                                                        },
                                                        {
                                                                            'key': 'ǗȤґťжĲBѹɘ¼\x853қͺӥ\x86ѭеɈԗȑҫƂѸӽ˘ρѹҟě',
                                                                            'value': 'Ј;ʿřńƆΖϗđ˲ϿťǪƃņаЅĈǔƬIɂÎƢȡQȼƶɆň',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ǥɱόΫʰRԍĄýԘѶʞҪʕӎɏŶЍć\u0378Ɵ¦ʧɣÆ,ϒīВĬ',
                        },
                    {
                            'keys': [
                                        'Ż\x8f',
                                        'ɜΥ҅ͰԦЂǷҙӰɞˤОҿрΜϯȴɰӆ\x9dφɬТȭĲʶҾŞ',
                                        'ѢԒĬϲԎ8ɺȍʜɓ҂\x8bΨ¥Ó˹ο\x85φċƥ',
                                        'ĎϲǽԬȌʋƥϐҁϵ',
                                        'ίŀʆϚČÏʒŧԗEƽHϐЍϞųΰԐѥϨƖЇ¥Dȇѡ',
                                        'ǀȥъƖÖϛ',
                                        'ƦϯӔϋϋÇԘΞǇЩȄµӾȹ',
                                        'ρáӯΣ',
                                        "J'\x94ȲǣмԎαѬȕҾƚèƈΰԒӥʟԔ`лǬԝ",
                                        '>\x96ȧВdцÝɺҒЧԦǵЬɰЖĘΘJîӬ\u0378Ő',
                                    ],
                            'event': {
                                        'target_id': 'iϺ3ǛјĥƀǂįǒάӋǻӺƞӎиʢɉǥΓǐԪØĔԐɢѱĿҋ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ɭҺƭЖ0}ԭӖ',
                                                                            'value': '8šʅϣŔѻɂÄϱƦ½аτǸ*ƘÉɎʤҟӰӖҽƎSŔȄˁғ_',
                                                                        },
                                                        {
                                                                            'key': "Иŵ'ʨϨJďӟ\x80ӤѩňőԩĐÑ",
                                                                            'value': 'ЌшƷП³ƋçͺʤɇǝȥπӷӠΐʾʮ˯ЫŇǀȱњԁ|ʭѷψ϶',
                                                                        },
                                                        {
                                                                            'key': 'Ƙӌч^ҙͳϓη΄ϛӤȸ˅Ϋ~[ƥӽĮσӇҵĜˑǤƠͿʽȇ˴',
                                                                            'value': 'ĊӾ˹ЗóǵСϾvЯϠqϛΔÃɲϋĤȲҭȆїζÿсΛʇÝЇˇ',
                                                                        },
                                                        {
                                                                            'key': 'Ű˸ϕŲϜşȓӌpʈ\xad]ÚɷѺϛŚ\x84ʍ<\xa0ґɏԐԁ_ӔĎҴԛ',
                                                                            'value': '˲gЌʌȇ±Ӑ-ϹªΰɏҀςϻ˃УѶξҖǄԟЊUƒѴͱȏӮЩ',
                                                                        },
                                                        {
                                                                            'key': 'ũȌӱѿϽсǨ\u038dԜɵĉzŊǳȴɟǈюԎӵņÉ\x95K˼Ĩȡħǵҧ',
                                                                            'value': 'ԀǇю˃Ƚӏ˶nηΊʹЙe\u0382ɧƅҹѳƀůcѴѭ˸Гԃ\u0381ЂǠӇ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ьÌ˄«%fӲʑȫOzďʁӦҁyÕ¢čǪͷ°ҝƭiǖÚȠπȏ',
                        },
                    {
                            'keys': [
                                        'ÁŰԁ\x9fʥæɻXĉÝΥԦÙȘŦβJ',
                                        'ÏeѣΗЭϺɧӺ˪Ë\x9eԓǤρKϑÅʧφ°ӓ9ɓlԎεŔ',
                                        'ʆθǤͿ',
                                        '\x83πƶсdʡ¶ê\x80\x92\u0378˸ƿцĘÂПtɨӁҵȊM\x9dѯ',
                                        'Ɩ1ӫѧÕɆБψɶƊ˱ǅƿХҪѤƍɝʷԦAΖɫĭȘ',
                                        'ŗδKўȊƵєҦˌʰϺ1Œ_ωΑҷ˶ιxƆˈɭ',
                                        'ĔкƄϻ\x85ÄΣʮŢЕ',
                                        'ѡʉɸҫӝ~ʈƒŚҭǂɅ',
                                        '҈ώâț˩ǠŴʕǸҍƠїɜҹҨɴ\x88±ýɃʼġǎ¤ĿРƹ',
                                        'Π¼Ѹƭ¢ɓȚЧȭҖ\\҄Ȧ',
                                    ],
                            'event': {
                                        'target_id': '˘Θù˟qлǿǤ˱Ѹȡłз0¬ƼmćвǐSаӀİÈӆS˯Țк',
                                        'parameters': [
                                                        {
                                                                            'key': 'ʺ:òԬʜʙÎƕѲęʲҒӭȢЃţ',
                                                                            'value': 'ȮiţʊўvǃǊé\u038bҩƧöđǃм˖ʙъҵϹĴĥ˅Ø\u038bʺӃBΙ',
                                                                        },
                                                        {
                                                                            'key': 'Ώ\x9e£є˽ĎāɼǄΏЄ\x85ă_ǩІ˓ƗΊсƢԕéѺĐȁʮȕĥԘ',
                                                                            'value': 'ʜÚċƱБɳԏ\x89ӯԟЪ\x8c1ǝŕµĿhΞӺʥGÐ,Ԍҥ±cåȤ',
                                                                        },
                                                        {
                                                                            'key': 'ɄȞţȵĒρtƱǟϽƳypr.ǀÞċ\u0380ЛáÈ҇ӤώҢҗJŵō',
                                                                            'value': 'ҹǛӰɽ',
                                                                        },
                                                        {
                                                                            'key': 'ЉҚIʉʅҌ4ҝʐòӑŰdԉģqǵĺφҪƾƴʵԦ',
                                                                            'value': 'ƈJÚқɢѳʧxʤ҂ЅȭβЏʀǙqϔǳÞQÿѭƾˌүқƅì§',
                                                                        },
                                                        {
                                                                            'key': 'ӐǠӔȽ\u0380ĈӳȁȢzԑԜϨʉ҉ʜŴ\x9aΧӪ˻ӓčȘʰǨӛү˳ʄ',
                                                                            'value': 'ŴŌтӛ§ҫýʓŁſKȧ\x9cǱ2ѾҰâʹǨΨ˃D£шȨY˄ϋԜ',
                                                                        },
                                                        {
                                                                            'key': 'ɣė҂Ϝţş\x92ҁʡѮGӓȯ¤ǘԃЄӚŜ˃Įшт!,đòȴҾĒ',
                                                                            'value': "ΑʟЬԗȐɬ'ˋÆŷŒ҇˂ǒˆҚЉЗθƺưȑȏȎɑaɣҷƏΥ",
                                                                        },
                                                        {
                                                                            'key': 'G˪',
                                                                            'value': 'íѯŏυǀӆˠʹĖ͵ΏњYņƶςkѢАșʁpгы÷ԊiʘĜȈ',
                                                                        },
                                                        {
                                                                            'key': 'Ԣn©ƖŰêпӏƘŒƌȜѕŏϰ-ɮӆҢʦҪȵĉԘȮα\x8aʤ\x96Û',
                                                                            'value': 'φƜʸвχȩӁƛŴʱЁӤΩøƉʪȞЭиέǌДϿĐǭCҼɧӸĢ',
                                                                        },
                                                        {
                                                                            'key': '¨ʔŢĖūɒʠ4GϬΜΒπ˖πϊː;ȜІ¥ґ} ύiўƺPϠ',
                                                                            'value': 'ɖʷʁəšǑ²\x88\u0379ĝ0Ǩʏʊŗλԛ§ϙȑƶǈҿϷЗǴɧ³Ӽӝ',
                                                                        },
                                                        {
                                                                            'key': 'ԕқюʙʅǭÔ҂Ε¨ƽȜȠĻʔ&϶èЩĿCwdĥǃòΟE˩Ӭ',
                                                                            'value': 'ʦ-íHϠўYӂǺùύͷǏФцƒҀÎԌ3ҲãĄӿĢϼӛ&ɩΚ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ЧǌɊÔȐȩǳŀБӡɕЌϊɋԨo\\ÝǝǊɲҽƽΘЈӜҥҒΣџ',
                        },
                    {
                            'keys': [
                                        'ȶМѣ`\u0380',
                                        'RʦԔӱ',
                                        'ǏӹǘϪɏå',
                                        'њÂėƺ\x9cƿђσėŢӄ',
                                        '<ˈҵϧö\xadњÚӯğlϕŮOǩǜsс',
                                        'ǙxŖʞˤιΘШ¯ľ\x90\x8bǟ˯ҝɮϠēǥVɂҞ«Кԇ',
                                        "ĽǛǛ.ĨĞÑȑЋʗ˥єuϳ˴Ϥ7ȜIȶm7'",
                                        'ƠϿîΊ0Ҫӫǳ˃)ҐԩӢJȅɹ',
                                        'õϦѳ«2şÂɔщБ',
                                        'ÌƠȕч',
                                    ],
                            'event': {
                                        'target_id': 'ÃжĺҘқӶ΄ѯěѵĦɝ0Ġ´ΔƣЃȜħɇԝэˑAН¥ЊLǢ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ůEĕǜqňȢʻǩȹԊþFōԣљοâĽ9ӱÈ\x91ʹƑăǦěʨå',
                                                                            'value': 'ȤȶнӜ]ҢҔȑҽʱҺͶÕԒʦȝ×˪ѼѴʹȏΘɓΦҷ&§ьǡ',
                                                                        },
                                                        {
                                                                            'key': 'ѿҙӽǞǔΨЕϩɮˮѹĢʦӓɚϚ˷Ԉͽө҆ϵĲŜ҄ɫ˞ʍΝƝ',
                                                                            'value': 'ΐсŸͼҪªˆAƜЙÊȨŐÃϱӺȨ\x80҉ˡǻʖšԤʹoѣɜőʜ',
                                                                        },
                                                        {
                                                                            'key': 'Ԡ7ÍЏЗǍɄȘѥSɠĻԈƈФ˂ЮĹӄԈ˲ӬʒȨæɴȣɈǭͻ',
                                                                            'value': '2ζԭÂȌӣљԂƉʾ¢ɏѲƆǗŚ÷Ԍϕ˾҄ÇƟ,ļśġӦҋ˩',
                                                                        },
                                                        {
                                                                            'key': 'úԂүЮ\u0381ɘԒÒɫǣŔќӵɋӠҕ˜ԚˣĂ˹ίϱʍŰʪңөԅɏ',
                                                                            'value': 'ȥȒŹΟь˃&фȷҸИϋɐЏӀőƷɢ˖}ϤЇ\x94\x8aЊĂžƾȤµ',
                                                                        },
                                                        {
                                                                            'key': 'ȠßѠȶŚĭΑÜ÷ԝŴĘÖ',
                                                                            'value': '×ԎƬćˈʓů\u03a2Ƿԣ^ʆӧũ˚ɖ˧ŹŎѹ5˷ğʺ˅/Ҁϝĥ7',
                                                                        },
                                                        {
                                                                            'key': 'ȸǉɄԝʓӑĮɕƙtҪȅˑŃҭ\u0380)˂ǈǲʈɍƦǊҒϺν˯϶ѫ',
                                                                            'value': 'ưƑŘȦҜǆǴŴҨrϮǊӕӕӆĜҊ§ϛGÿӉϿɵ6ΕЏňźÜ',
                                                                        },
                                                        {
                                                                            'key': 'ǚoÁ¾QñÇѶÈ˸҃ŨѸʵĂϔůʠÐԫΤȾȁƖɎǶʳШãɛ',
                                                                            'value': 'ѧ˼9Ӡ^ɠȤϜԦȑÙíǅʰʀ(ã˰ƮɖřƌҝȸɲƚұȜƄǾ',
                                                                        },
                                                        {
                                                                            'key': 'щҴʆԡΒǒǷǓʤȑӝīԢíʃԠΐξƚąÐͳӈϝϳȆȼȔ(Ð',
                                                                            'value': 'ĚʆԮɕϚǻБƐŇwЮʸѬĴŏ§ΚûǇÌɼ\x86ýƷӂ˯ͽԖԉǠ',
                                                                        },
                                                        {
                                                                            'key': 'ҖͶӷϓȳ҆KȥĐ',
                                                                            'value': 'ď˃ШӈǇӯȥəȻ³ƇӻϹӭȱ ŎŠǌɤʽϦYТӼϯā҃Υҩ',
                                                                        },
                                                        {
                                                                            'key': 'ʇ\u0381ù˭ӸϻШѝϷфǿҦǳќßʄɚʚæφаǱDZ',
                                                                            'value': 'Ģƾtŏˀ´εϗʵǎʡϯ¥˴\xadȓ±π"ɣцÈϦǤĖ@шǃŮϤ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ďҀˣʖåǿIɭýάʇȾЊɃaʻϑКԁӗƪōǍШʝČɂИҍĕ',
                        },
                    {
                            'keys': [
                                        'Bź',
                                        "θԟćѩΓʬ'лʮҼ^ЙÒɝȐѥƩʥˀ",
                                        '˙¥\x8fˣˀÖɮǢéɩϥɚΦ',
                                        'ȕô҆ɂåƧ\x8eɻПʐӅξɸɕҸӁԣĨÅɭƠȩEҐͱáѾʭ',
                                        '˴Ŗ§ѯ#ҏˤȐêɉ',
                                        'ͳͻ˳ѻāҚ˭ԗҮǤҡʙ',
                                        'ɭʠϰdԧьҍǱȫǂλҙӵŻĐσȚ',
                                        'ÄmʂбĂ£¤Țҭ5ӭҔȯҫс',
                                        'Ŋζɑͷӓ\x89˂ѐʺ',
                                        'ɟȹ҇į˨ȻȷģŎɾх1҆sĐ\x7fŢѨŏȢżgΔİ˗ćǬƢ',
                                    ],
                            'event': {
                                        'target_id': 'ԘͽȧҕҷЎƺȤôԂơƗīҽW˱ʮɧͻfɬƋƮęVûïƎ˄ʾ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ǗÔüTϝʼҖïĬjpҍҵŨǡæƒʻΌ÷ϮӈĊȊӏˡ\u0382ԕϤӹ',
                                                                            'value': 'Śҿ¼ȦĶή҈ǬŀԎϨ[ŗzҤЅȕӮǼґżЇÇˋŚǃȟŵ˾҆',
                                                                        },
                                                        {
                                                                            'key': 'ʃƃƱÀ ԫѨŧ:òŀҟӇVӔāėʄτƔΉйζĵʗƵ¿ιғϺ',
                                                                            'value': 'ûǞˤļǄɡБ@ԣȁџʠȟƓǐӗKĄƀìȑ¤ĹϙȡſɚɌ´Ц',
                                                                        },
                                                        {
                                                                            'key': 'ȀɪÁқ˸Ι˫Ġ҈ѥЄ',
                                                                            'value': 'ŗƫϑƆ˄ſʷƑЕԭɬǴĈÿŭļК\x96˵ͳȢЩ@ǓÜдҡͼԆ¡',
                                                                        },
                                                        {
                                                                            'key': 'şŷȤϹɳҦҧѮƏӊŪȔϥπĈȾȹłɌǒҦΌкʍұіԖǜŹʑ',
                                                                            'value': '7ʰʺĶρÃћ\x93ӼŰΈю\x91¤ɣĻҚɕș´ʚȐǮT˺dԍɌ˵ʼ',
                                                                        },
                                                        {
                                                                            'key': 'ϲlƽŞʹƉɓɗŪͻͳѐϼŧƒ"ʘɋбҙϞĴʆҰāѱˤ¨Ԕψ',
                                                                            'value': 'ӍůѼҙþƿ\x97жϠˎ˯ģŤɝҙŇӹǁ\x88ǈǒ°ԬҨÿȰҪĻƻя',
                                                                        },
                                                        {
                                                                            'key': 'ʮϐÐɚέԖԔΎϨΒѡ\u038bÁşʠĂʉӥŲƴʈҥ˛5φѷÔǎҽs',
                                                                            'value': 'ÌӌѯɶȈґĔȌƀɻȄҞ˂ϔͿͶʙЇҥá\x7fԐΆȮνжȬÉмѣ',
                                                                        },
                                                        {
                                                                            'key': 'Ѐɺq\x88ïǼ-rǪâ\x85EɤéʑǕΰØǾРДӝѳŎĭƲč´Ȓ',
                                                                            'value': 'ҡ\x9d˻ӞĝőĽ\u0383Ͻ²ȹ˶ȣжȰΖÒηŢԃҲƔřԛΰ;ӈƋгv',
                                                                        },
                                                        {
                                                                            'key': "ʯʹӞӴDΐуʄϴ<ϨɕЏǹġЗқҷ˖ѸɷɺȍˠԖ'ȭˉύȯ",
                                                                            'value': 'ëΑĀϯϯѿʀԋǙɊƟhїҨ\x85ƐтʸÉŏ\x9dӖƃ+˺\x9eʓÚǓх',
                                                                        },
                                                        {
                                                                            'key': 'ӊȮÞ\x8fȶP>ΚˑǶчʬʻŖǛǁ˰/^ґúη҃ӕʤƕ˄T҈ƫ',
                                                                            'value': 'ʢϩƟϽʖʣØȱɎÅәѭƙȱβdtϲãɴѦѭͶsСʡɠɓȆɓ',
                                                                        },
                                                        {
                                                                            'key': 'ӦԊ7ΐΘ',
                                                                            'value': '\x94\x8dǷӭҪѿǩã3Ń˜φˎʉŬ&Ìԛ\x86ԏɭˢˮĳҤҳȂɕΫɶ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'əѬӛ8Ķʜϔϡ,ӪԤͰсɌ\x9fϏǢǄάӚŭϩıȸюǈΧĊɵЛ',
                        },
                    {
                            'keys': [
                                        '˓ҁϲ\x8bӾ҉ħѼʼПʝƿªŰȟlǹ',
                                        'țƏҐԣɛåųǷӠϪ˺Ƈɡ',
                                        'X¶ϒѭқȈ˟óΫfɤϔĶȔΓȍԛƹҩΠˠǺʔЧ[NʟϚ¿',
                                        'Ԅ\x9aҎėӇcƞϱ9ÏŅɾ^ȼİ',
                                        '`ҊάȶƉԪʥ"~ӱммѩўӤĨȓ˟',
                                        'ǰΎӔȹȈʲЃǌɪ¡ŮȬΛIgæԉԒ',
                                        'ԃЕ/\x8fƦƖϲì˅ίȎ-',
                                        '\x8cЬΤìϭҟΌϥ',
                                        'φ8ʏĺǕɷ˹ǁдӇoλĹ\x86˃Ӄ~ċĵΖƈ',
                                        '+ЖǧСʜϋї*ƴđǈĮ',
                                    ],
                            'event': {
                                        'target_id': '\x98ϹȠuǃҷԬƬйέ\u03a2ИŶ³ʏ҉¬]ÑҧϑѮŠƐ²ĒӫϳΒМ',
                                        'parameters': [
                                                        {
                                                                            'key': ')XԕР¸ΖҌˍȹϛŜʢċƍл§ȋξȡÿԔ\x83ɡˌĻɶƤʣǩY',
                                                                            'value': 'ŕ҄\x99qɌǛΌϙɷұªsҊ\x9ebԦœn˞ȡρüўéjŦcϾǼæ',
                                                                        },
                                                        {
                                                                            'key': '˝϶Ǐȅʕǁ¿Ο˲Ġʗ\x8fǲЄӤɖοʮЄҹЫɵԘV˝$ыȨĢČ',
                                                                            'value': 'ȖȮɆϞξKӜхӠЗɮгѓͷÀϵĖӖVȍʔЎԘ˜ɠƞʰԥҎҊ',
                                                                        },
                                                        {
                                                                            'key': 'ì\x81ȻԭшˮϟƎФԘӻѧƣ;ΨƌӐЂөćҷ ŸýѶʤҍĎȆǮ',
                                                                            'value': '˵ĤщҾłҦ˧ΈΜʜŞȻԒ\x8aȯҀ,ϹЀӭњћϒӡ\u0379Ȕҡɜ÷v',
                                                                        },
                                                        {
                                                                            'key': 'ǣίŜήưͱƐǨцJ^ˋԣţſк©ǶȾËÌϪĐÛǰ˻íнȝЦ',
                                                                            'value': ':ϊ҈jΖԄρƟşʑ˘\x9bӡ\\űƄƕΎǙ[ЄoØʢӳŇБĠúZ',
                                                                        },
                                                        {
                                                                            'key': 'νȒЭ\x89ΨƂԝЄˋȥȋњŀ2\x8aÚ\\ϴЦӵҧðρȸ',
                                                                            'value': 'ǀÍĀԟˣǃӰѪϔfϥʯʟ\u0378ĥԪѦҧˤǠҼѐǠàϚʟŻʮӓń',
                                                                        },
                                                        {
                                                                            'key': 'GɹјʒԄγŦέŔӢФːĔǆSәӧʥ҉˭[яѤӺ',
                                                                            'value': 'șҘ˅ˌϡӴǍɈǓҶɀʓ¡ÏηìҌƩԛ˫ˁҲ+ŚɼϾǊƒĀî',
                                                                        },
                                                        {
                                                                            'key': 'ƣӞçgƳЭңƂΰȂʎϿ=ѱщȯōŐȁԝҶҺ',
                                                                            'value': 'ϧӬϣΠǥΒȌƝ·˄єPңӒʴӎҮиĀƥҏ͵ϔҬăРɋɀĲӑ',
                                                                        },
                                                        {
                                                                            'key': '\x9eԃȉƙʹŨǘɉŻ˦Ҿ²ȃќBvȗʦΦϔӞϑгҾǸ',
                                                                            'value': 'ʰсʬʴдΐӬԘҷļbѲž˶ӓôεƵ$ŵЏƍɯ˩хȢɋ˗҄ɔ',
                                                                        },
                                                        {
                                                                            'key': '˔\x8cӅȿҌЖʎԝЬ͵ðғǩίӤčɆţŔϠ¤Ϣń.Ýӎ°Ю˜ɀ',
                                                                            'value': 'ŢԋƋ˘лɧή˖нʂˋѠĻƔƚԘдĚĔ\x98\x8a5ǎГϻƽϖƥÚȵ',
                                                                        },
                                                        {
                                                                            'key': '¢ˏЧԤ\u0383ƹŘѨ±ϒ˶ņƹŪŨɍ˨ӔΦjҀ1ǆΐªΈӈʰƚт',
                                                                            'value': 'αšʳϴśѷԙʨсzĠɳϏPƈȃKɨȋğĴϛԬӀʽԗȽɕҏĎ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ƥêJюӵϯÓӯņ\x89MŞ˸ØӌŶПbÍǞӘƒʹÖӫ¸Ǉñëə',
                        },
                    {
                            'keys': [
                                        'ʜ\x85ĚϖÌǔҕǂȡӔˁǿĕˣëǞʛкÓvİ˹\x94˜Ȱ4Ϗхƭ',
                                        'ѿȡėʹƪτĹ',
                                        'ʧΊώŮ͵лШп',
                                        'ΩԓҀŠҌ\x98ċ',
                                        'ŧΗÝȋҋȵ˗һїͿŢѽĻ\x99',
                                        'ŊӕʛκͺƳÑȇΨǇÖаˍμȼԒ',
                                        'ɂӛҺϮԦӺΖϞş˅ƨlӬ˝\x93ú҂ԡ',
                                        'Ҷ˚˥£ӑʎʂȢҋӟϗaǤ¿ʝԀԇ˄ɿƻUϨСє',
                                        'ȑƔƯŘ',
                                    ],
                            'event': {
                                        'target_id': 'ç\x9a¡ҤƒЉȂɎȴԎÒԀӟϛЧGɕŞˈ\x9bԮ˝ԇ^ԐәΊ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ȽεͳΊҁČӬˢɅϚƠī)ėЕˣΦҔОӷĉ˟ЦčLǤЃђżƂ',
                                                                            'value': '^МұώӆϸàrşҨΝŇǊő\x8bͼ΅ǳ˂ѐtĥ\u0381¶ĳ)¢\x8a҆ɴ',
                                                                        },
                                                        {
                                                                            'key': 'ԩíǘ\x8aўƵǇӎĴĺĲȭʒƨҕӣ˯ѬɒƱϟˡŵσĄŗϊҽæп',
                                                                            'value': 'ɉłśİƐJŒіЅ¸ĹǮƁɥĀҢÆŬǳ_Ǹрȷǜƌˤø9ҖŻ',
                                                                        },
                                                        {
                                                                            'key': 'âŦ\x96Ѐ¹ǙѲĘеŶχɃƜ\x9dԕlǞʶ·ϽŠʓĤ\x8cÇʨ\x98ģȄҙ',
                                                                            'value': "ѻӛƄΏԗőCҎбͺʤˑˮˣɊûðʅ˜ӂҏçѳѥ'ё\x8eƖƱӵ",
                                                                        },
                                                        {
                                                                            'key': 'Ђʔš\x8e@çщɱŏԚʃé¯ŗī2ҵψρƆQпɮăɀЬҐǗ\u0379ȗ',
                                                                            'value': 'ɏÑʐ®Π˺ϫӍǜҕʻ´ĒʕЌ±Ш҂ҹʂřÛϙˁӝŌł®тǓ',
                                                                        },
                                                        {
                                                                            'key': 'ʦȎʮԋȘɚҪʖʗөД\x8fϾȜʙтƆԨŁũɄЫЈʯ¹ρнƱϣɯ',
                                                                            'value': 'lëʦˆȒӞıѨĘяЌʜςŬ˪ԌÅЪЖЉĬǢǜ\x9cɡɉҥƻсԉ',
                                                                        },
                                                        {
                                                                            'key': 'ʑȡķđҁҝӊӷԗĽОLнҙøǮш\x92Ԅ8ȄѾǍ*ӖϮѬҿŨ',
                                                                            'value': '҆ŬɜQMєҲȻǗŔԙҎʳѽœʚÖб˞Æʗǉə7ʉȷɍЋőΝ',
                                                                        },
                                                        {
                                                                            'key': 'ԛҰԓӋ·ǵˎҺ˙ʳЊ˯ҳȠĥԭǧҙ>ҏ˜γ¹ͶӸĠ«ɲçƣ',
                                                                            'value': 'ɱȌƢxļ\xadėŹϱǕʑξżǓ$\x8cҧˏѓђ\x85ƋЃґНЗƌе<ч',
                                                                        },
                                                        {
                                                                            'key': 'łJϲиԌ',
                                                                            'value': 'ӣǷӿӝǟϯщǎˤ\x9aŅˬΩ3ξԧɻĜâРSőҮčƃĈԎƝĊѻ',
                                                                        },
                                                        {
                                                                            'key': "ѓɨÛŵԡŃǠ'ſMɔϒҍÒ΄ӯԄ\x89ыѡĸԅΛǳʁĢҰǅũҤ",
                                                                            'value': 'Ĝö\x93ω`ИΗǹƻӦ°µµПˑЍ§ǚОɠԘӶʊʠ\x96Ӡ˞ɈɟԐ',
                                                                        },
                                                        {
                                                                            'key': '˞7Ψ6ҾǃΧϧ˒\xadǄҽ˄ψЧäȆģβøϖƶҖʩʵɱȝҖðû',
                                                                            'value': 'ȦяàǑAɯиЂγζѲ[ɷȥЎůϳϟЋ˧ʭŚĖʕʭƺGң\x8eļ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ҁɬȵʱʭӰwΰлѨȽ\x8a˓ȎϾƖɧʁʏԩϔԩûǣӨʏnԕƜ+',
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
                    'â',
                ],
                'bindings': [
                ],
            },

        },
    ),
]
