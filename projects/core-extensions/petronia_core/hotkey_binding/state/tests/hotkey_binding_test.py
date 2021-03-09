# GENERATED CODE - DO NOT MODIFY

"""
Tests for the hotkey_binding module.
Extension petronia_core.hotkey_binding, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
            'key': 'Ϧ(ʲЪӎҭŠщӼ҄ýϪċ\x9eUҍǧX\x85ʈɠ\x83ӥ-OӱX$ʓʈ',
            'value': 'ҦǝЉɮ҄ƠϱȊԝɡӸÒÒҙö)ԛ˨ǍĢʯʫʎpāē҉°ŹQ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ԛ',

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
            'target_id': 'ӽĶƄĀͼˉˑԁŘƅƌ¸єӎʔ\xadјĎƃҺôВ\u038dƮԙơԃ¢оɛ',
            'parameters': [
                {
                    'key': 'ϛnƷʱµ˟ɾʼΒĸҪɪÞɢԖϐËʜʧĚύ³ƤɬǛҌǇѠӤΆ',
                    'value': 'ϞƿƳњΗɀ?˒ʿÄ:˩ƖΦӮbɡǫ$,ŨʫǹİτŊ˶Ȇϻѐ',
                },
                {
                    'key': 'ӅǡӓϿΉɝϻĈx\x9așʵĖΏҼϑzǗԀɳЃЗ\x90Ǘ',
                    'value': 'ȥÂʂВǔƁʽďӐÆºĒÄʒ¶ĄƖȊ¶ªёļ\x85р®г½ǈųī',
                },
                {
                    'key': 'ͼŌɪǃćOɇ϶Ļҫҿ\x97άδϛGɒķo§÷ĭġŘː)ѲTǞͳ',
                    'value': '˘ɠјԠɵԤϔʄӏѿɹ\u038dϐҵѐˬҡͿ\x88чɃʊңͽѸӼ\x8aΣuŇ',
                },
                {
                    'key': 'À˯Ⱦͽ\x83cΟɐ\x87ӔʜǟˉȆԠдZфҙɊQɈѷńѿȽѳМĬǃ',
                    'value': 'ǮɈӡƬȀŹʃƞŊͶɭйǯêԠ˄§ӏoͲǢϝ\u0378ͻӪłòyǝѼ',
                },
                {
                    'key': '\x82ňśϮ£ɪΤЊżäÐȔȴĔΙǎФЊƠƆόƍʮ\x89ĳȶû˵ȘƑ',
                    'value': '\u0378ȟȰЗ±ϋ˃ȴҲƦê£oơǏŻ;ēӱĚŭɔΎƏµxƵƳϺҕ',
                },
                {
                    'key': 'ɸɦɘ ɋK˥ǨÜ,ƐȗўϥƟɠʘ˔¥ȫşąɂϟ˻¥æ˂Ҩӳ',
                    'value': 'ŭĦˣ˭ͳпԜ%ͺˆāͿLǗƣ˜\xa0ԒŅ\x85ӉͲұ\u038b}ò˹űɼČ',
                },
                {
                    'key': '\x8eɌ˳ʚ&ƨȮĕÊˤǾLòçȰӶǾcіȤ˸ЗGϝʮ\x9eԓВĵə',
                    'value': "ɱčРƋǃˌUԌӺξɶЉkɤәɲɤȃԙʝQWǬ'OȮĤBʊ+",
                },
                {
                    'key': 'ΚɹȩѺ\x8cčΛʪ˕ΦʻĻѶʩƘǋˆŶ¯',
                    'value': '¡ʄƄίϰБʏϫ_Š·ɯǦϐVӝСʵÊеʜӸĘɯƄԮϊυϽĒ',
                },
                {
                    'key': 'ˋăѻĚҞ;ˋæěSʌȞ',
                    'value': 'Ԗϫ˶ϗ}\x8cȯԘŝǭŃӧӇùżȏѽóЅüǻǡѢfʑύ˩·ɂҭ',
                },
                {
                    'key': 'ӍωǲȌԭͽӆҶѴʪʳŚҡʪƂǐҐÉҸÝϙӫ\x8aԚħ"ƆɁéɭ',
                    'value': 'ȃƌȱԀȸд§/҆ÂҦƅ,5ėʘфȘ\x8aɥŧŚAʡǬƲϱҵсµ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'Ăƒ\x98Ǉȧ',

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
                ']£ɉɰѬ¯\x98\xa0ǗĊ',
                'ѹĜӱʞƈ±ɃǨιċʖƀЃΆǂʃǙ҈Уĺ',
                'ҍǷƍǧʵűĄϯѳԧũŐɔ˖ĶӂȶԍϵӔҚX',
                'бʁøЪ͵˥řƷϩʼɇʅ˃Κìќ~ιʢԣ\x9b\x83',
                'ȅȶ',
                'RгԘĴŖȵΌđύ_=Łʬ˾²A\u0383p',
                'ǝ',
                '¯ԍΪ',
                'лӖƨRΠɸȽɲ',
                'NͱΓ|;ϷћҶ',
            ],
            'event': {
                'target_id': 'ѺȽɗȀЦƎЬĄɘϵғʽ϶Вϝeцҡ˳ˎɹϩʉҀЖԜȬhϏÚ',
                'parameters': [
                    {
                            'key': 'ыȇ˲ɻϓ˒HԀХґҪ\x9cƜgѐwʨΫӰȣαɆқӏȱ\u03a2ʹǆҩè',
                            'value': 'єȨӴύпʹȱΫѹҨηƴСҦϪƚ¦Ǟ6ñʃͲѺo˰ЛѬҍÉˋ',
                        },
                    {
                            'key': '¼|ӘŹϋǜҎӅɺȷƳ˞˓Д\u0379ɼʫѰɈʱƲ\x8dďΠȻιĠє\u0380',
                            'value': 'ǹΓɪɉОѱԁ˵ŶԝӻS\x7f=ƟǱ&ЦɵҬɛIӬǧҙŬœƎȤ#',
                        },
                    {
                            'key': 'πԝϧΝЎΦɵß˥аÂӂʁ˼ķō\x9aØdɏ²ˢ\x86ȯęEȋҸɖô',
                            'value': '˃ͺğʲΉɿĩʢґĪѠӅϱϵȻДЇƪĠЮ/ɏάэɧӣγӆОɸ',
                        },
                    {
                            'key': 'ϧo§Д~ȚʽÌҾĞĚϖҶrƩϹǜúоɢҺrğѮϳԛį',
                            'value': 'ΘǞӳ\x97ʸҊϠѶЮϩΗǅяåȱƣЊŁlÇЎȫӈʴƅӏ\u0382ţͼŁ',
                        },
                    {
                            'key': 'ǻԞɵɸҗΗԫ¦ΏɿaX˨ӚǍƊƎȠ',
                            'value': 'ҭɹɲƉ˖ɟɳʶfJԮȋķԫƀζʤƨ˻\x8bЀϓʑɵөȾω\x93ȭB',
                        },
                    {
                            'key': "ȿʛüǂ\x83Œ҄ҙҞӻ\u0382ƱƟʬЉҊѥ\x87ȃʛχȳΒƔÇ'ū·ʅÂ",
                            'value': 'ѲЂǨūѽȇˌԗȦāɳɛÀ-ԣӗ,Ҽʡφҟ¾§ȅΙŠį\x8eӝЀ',
                        },
                    {
                            'key': 'ƵǟϫʖѧётƃΡ',
                            'value': 'ǻϳ\x9fɚ˲ʔȂԞǿǖίԏƻЙŗîҿǚġ˦ǾψΥŝҩгȏÜӍ˒',
                        },
                    {
                            'key': 'бŝͿЖûL\x9eУɁ˟ʭɆƸȦϣ҈ƵȀ˛ʆΪ\x83ęҏКћʴԣ[',
                            'value': 'χ;ǮʻЊҏɌǭԂʢҙэҥϯƑ?ɃȖƼŹΐɏΧΠӤ¥4ɺ¡3',
                        },
                ],
            },
            'comment': "Йϔ'ІÀԊƬYјľϷȶͻȫͼͲɮҎ\x83ĺ|Ǚ˸ίʲЖЅˉŽǂ",
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ϧ',
            ],

            'event': {
                'target_id': 'ʹÉ:ł.',
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
                '"гŧȌ',
                'аӘĔуиƪϙʋϴƦӆϞҼȝǥɭʟѭģƞŻĞԎjƚ$',
                'ͱǨѷ`Оèӎ˽φХҺϥź',
                'ʯ',
                'ƴ΄ȉ$ʖ$ˮΞî˓ŤҭЙνßɐϹҚ',
                'ǉÛҁƔԮȓѯɚɖԕВШbӐҴ!ҨʰӐѭξ\x84ˀҼ»\u0381юʕɾƭ',
                '<\xadȄǬģǃˬн˝',
                'дkˠʚǜȟKԨԎƂe$`ǔġȭƒiϔ',
                'ɺȇ',
                '\x99҃ņƈгǘɕǭʅҍșǡС\x8fӱԨ\x93ÍʹǇÄχ+ȴҁʉĲ4ŝɃ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ǚˆԟĦΜ',
                            'ҰʛơƔʡϫɟˀȴȇѼҫtł',
                            'Κ\x92ʗɜî\x9aԁҼѺҿρ]ĐӬэưĒŹƓԕŬ˛Ȅф',
                            'Ѧ<īпńԫ˖ԢΌo',
                        ],
                    'event': {
                            'target_id': 'ʸԝǦĶ˒ȅ\x7fӺűӯ~Ōϓƶ\x94Ǹ·ȰОԤĘÙƴ\x80Δʤαӥ\x86ý',
                            'parameters': [
                                        {
                                                        'key': 'оÈяȍßʵʛӗѼ;ϢϣΊǆʉʢŲěɯǔЏɘΐΡϗ˭ҺγʯΪ',
                                                        'value': 'ǼÑΟƤťˈǿԡʮɝшҰϋÉđϞ˻ʆψɰЄȧƕǁЇ҇ʇϋÀǷ',
                                                    },
                                        {
                                                        'key': 'ΘìƫúƤД\x99àӗŋȅŌζˈԇÝΞ2ǎˀϜòѫϏï÷ĺ҈Kӿ',
                                                        'value': 'ȵϛДĈӢϦ`\x87ǺòНͺƎèíŹ,Ӿğhϼʠ±ɀӏΗ6ŒƱӣ',
                                                    },
                                        {
                                                        'key': 'Μɭ7õТǔǦ',
                                                        'value': 'ʤȻÁɸйĘtƻеԌɠο˯˹ɖʳԫŽƭɁХψӘ%Ɓԁ˵Сфӣ',
                                                    },
                                        {
                                                        'key': 'ʦҁʾМˍʿǨʳ\x81Ąђ\x85ÓQ\x82ƠԠ',
                                                        'value': 'ǐΩΫ˔ǟʝӁʂǞƆ;ώʣͽΓˏѶȌђɃӟşģȼșЛӼãʁĶ',
                                                    },
                                        {
                                                        'key': 'oɻ\x8a',
                                                        'value': 'ȝ^ǦŠœАˈӡдаɘíʓ˵йȉ˭ϮӬȽϤєƗԖĮӔȍČʹ\u0379',
                                                    },
                                        {
                                                        'key': "ÛξȔǑϊҕԃ'ЋŎȟΞʚԪʩ\x9bCÛϮчƓө°ҘʉYӀ.ςӢ",
                                                        'value': 'ȍƐƭκ\x94ξɺŝӮԝȪιFľ ˕ɽèιšҽҐӑҡĩ҃ʎʝʓġ',
                                                    },
                                        {
                                                        'key': 'ӂԣ£ėé»ľƄҎϺӃŪșɎӑĘĚѺ$ώʞýЉӱВҽӸʣϽƟ',
                                                        'value': 'ЭΖƬ¢ҷÃd΅ĒɺñZɏʎÅĂɔў Əо¸˭ŘƓȱlЁˇʩ',
                                                    },
                                        {
                                                        'key': '˩ɫƼƈ͵ǋΔӴžˮ§đјƱGǿѤЏҌѨžѹʡʇőƬɬҡѼϠ',
                                                        'value': 'Ԁ\x85ԇǭˎӟүƉȯѕŸ\x82щɆɆӤƦЗΩɷ˜ԟ¾ƲƱ\x8cǴмȷƷ',
                                                    },
                                        {
                                                        'key': 'ύ;ѸĩҡU³˱ȝPϓ\x90^ΉÃӹӽВ˭ίªƱſиþƣǛԒͿͰ',
                                                        'value': '3ћĕʅ¥ƋǦπԕÏ˽ЙЙӝ\x9eԥήřʡԭҪÎÄӘΦ˅ƪӃζ\u0382',
                                                    },
                                        {
                                                        'key': 'RƑěǿÙʌθʃ¦ǠŏƟʎҸīĠђ\x83ͶǗȥɴІOeÄðρȴϠ',
                                                        'value': 'ӔʾļѢˈΛԏƠʿóӗѬϖΤԍ\x82҉ƼЫҶÞϴɕĽś˺˦ŋĔǶ',
                                                    },
                                    ],
                        },
                    'comment': 'ӣϮΖ(ɁȀwpªјīı\x90\x92Ϥ\x86ȝ1*ӵƫ#ûÊžŗ¹ƿR\u0382',
                },
                {
                    'keys': [
                            'ʘэ²ԆîɄЕϢǛǱԍԮţ}ͱĒȜ·v˕ҊӂB',
                            'ԞĔhΡфϊɴҍȈҁǡͲĔҁЎˆǶҡˎƐѤý˒ͽåđ',
                            '\u038bəĺɵЩPƟșx',
                            'Įďğ',
                            'ήʶwЭ¸ƔҩӲȺҕĚșӫȨÞʝçğϕЮɀӰӊ',
                            'ƄŃȇǖĉПŒ',
                            'ђǒФʓǰŠżӠʍҀϷЈǵŗѭǖѳѦǡ»θӱӦϟӸȉȧÅң',
                            'Ͼ§ӐǋϮӍŲ(',
                            'Ўԭԫю˨ҭҚвɴɨʵľǙʤΘ%ƴкӶДҪѳʀ˦Ě>ȷ˭',
                            "ԈŧӯÕԕϟʕ'Αљж\x92ιȂ\x82ƢķȮīҮ",
                        ],
                    'event': {
                            'target_id': 'ӋңϛͶҬԉdĉːпΣǶȫΈƦùԩђˉȚØќϷԊ¶ȩȦѢ«ŭ',
                            'parameters': [
                                        {
                                                        'key': '[Ęʙ·ǵ˙',
                                                        'value': '×\u038bʌџƋɉ·ҚĸJӾǘϝѼʁƚƶƁӉĦ˦Ӥω\u0379ҰόÍˇǫЎ',
                                                    },
                                        {
                                                        'key': 'ҬӀɘ΄\u038dѶϏʣϲʋʱĈ^ϗʪƃж+˳ʮÆӲƓĨȢ¼ņԏқν',
                                                        'value': 'ΓЇʖɦЈ4Ƽў©ìк2ˑϷÒΞÒ\x80Ψ&ƢЕѾģ~ξÛʃ˳Ő',
                                                    },
                                        {
                                                        'key': 'mƃӑ˱ϤȒćЙ:ƒćϙȖοԎƦх˸ͻ\x96ԝƈѷϓĐŦĖʶΒЮ',
                                                        'value': '\x9fĨҡɏʜӆӔӭī;ΧĒƐǷΡ9ȱӧѣǳЦȤʠB3÷ƔȠ҃Ԏ',
                                                    },
                                        {
                                                        'key': 'ΣũŽαɟ',
                                                        'value': 'ȳPÀŇΌͷÉцʽçɍÂ\x8d\x81ʃ\x91ӴϼԀâ~ʟ°\x95ȊԖ¢ɵӾƪ',
                                                    },
                                        {
                                                        'key': 'ɡ˪Ɯɡӭż,,ŴӺқǃƍŋUδτϧźʍȇҦαǸҳӖΕѐλĨ',
                                                        'value': 'ƂċʆƨϘԙԗѤ{Ʌ»фʑ',
                                                    },
                                        {
                                                        'key': 'ίěҔΛʅőɯ\x84αϿϻʨǮϹȥƥЮɿŘ',
                                                        'value': "ЈĨңШϙϊҶŀ'ўɲƜȲы҇ϓԃɓҦǧСǈԭČɛ«ŌȬΓɏ",
                                                    },
                                        {
                                                        'key': 'ĦѕМÄȟîʑƏɄѹīȩʽÃѕϾȆȥŸџƕҢĬ6ȌǇʾѦӍԙ',
                                                        'value': '?+¥ѾӠʭԣĐЦƠʮ0ӑȪœKƋҳӼƾϊĠǱʟΚˏЭʼӹԒ',
                                                    },
                                        {
                                                        'key': '\x91ɜʏҭэʦƅȦĉѩΌʷԟ˓ҬѕҼХϞδ˞',
                                                        'value': 'ӨѧƏԦӆ\u0382ʮf´ɃƾˬƻʐěďĊвĲQĕŗǓÎļ¡ɌȢХҀ',
                                                    },
                                        {
                                                        'key': 'ûңӜàӅΛ˸˸\u038bęoӼЄȢȨȏɏʍʀϬºˎ˭\x89N\x9eǵøρÞ',
                                                        'value': 'ĔƽûAЍӅøőŢƯĂŠФʷɞζȄɒƭřÅӞВʙʑ˒hİŀ¸',
                                                    },
                                        {
                                                        'key': 'ûȤӞɑљȦьɃԓʙɑȘӗǘƷɫϋÉƨϽ\u0382˂ɝԒG΄ѓѷɩщ',
                                                        'value': 'әƨ{ҥʘτǆiĤιɄȇʢɌĹŴϝ\x8fˁʫ\x9e\\\x9bΡӘťΩɛԛӧ',
                                                    },
                                    ],
                        },
                    'comment': 'ʗϑȾŊƄϖϖÍ\u0383ƴԇӡɄˇρʥŕǰĘӝeԁ"\x7feȅ\u0380ӒǨӦ',
                },
                {
                    'keys': [
                            'ĩԘɡϢΎňȞĆ',
                            'μϸЅ',
                            'õѼƊ\x82',
                            'ǪөϷь',
                            'ȴȝϐϧϏήќƁPˢ\x83ѯΡƘǕҌȖΏǙʐ',
                            'ͻïԕʛʈÃMҦЄŒʇӗϝɠ\u0381Ǻҡüǭ¼ӸЅР2Ȕ',
                            'Жi@ƨ\u038dŭҪҔǚ\u0383҃\x90ԋıǂ¨ӿ˘"ўа%³ǌԬдЍ',
                            'оГŨԡΑ˞˭ƛŪͱΞ',
                            'ˀʈӈӌ»ѿȫζґʜŖϕΦ·ҢΟ',
                            'ω\x9eǈҧЯɹèȏ҂ʞÀ',
                        ],
                    'event': {
                            'target_id': '4ӿƥ\x9b¸ƬɉЃҜś|ѰɽԛćСɽΆƆɛϺwʰδԠπŀω>ɏ',
                            'parameters': [
                                        {
                                                        'key': 'Ϧƞʁ˚ɗͷǋ´ͱòґЅʉʿÂƕoÂҹШLǧПʍƁˏǍȦʥҜ',
                                                        'value': 'ΊËʝɮťǱОɏȄϋƛԌˋƁЇʊɺɒƞԓ°ǿΌ\x9fɇǧϼəԤ˵',
                                                    },
                                        {
                                                        'key': 'Ҏ\x9bQӹҘɞșѴҟĠˏƑžèѷƷåͿÌĔV\x92ŅǚĵpҐ9ӱȣ',
                                                        'value': '©ÖȏȯäʢϼӤĴŔΐˊPşɖ@ҏԥʐѥб\x81Ҳį\x88ϩ"ϖй;',
                                                    },
                                        {
                                                        'key': '¥ȁΛӥΨȏЭŴŰÖͲźŏžпӐĹҠÜƦҟ\x88ńӨʷӮСĠ»і',
                                                        'value': 'ɆͿ¯ǐʞɷȥϸ\u0380ĽΆ*ӜЗ˺œӕâĮΫԊɅșΗїŊҷӟ\x9dӐ',
                                                    },
                                        {
                                                        'key': '҈Ύ˨Ξ\x98Χșѓ',
                                                        'value': 'εԄ«ĝƼưΪ\x8aĽÖëγǲԦYǍ\xad҃Ƴ\x92ЖѨ#Ɋ½ɐəʧϢÔ',
                                                    },
                                        {
                                                        'key': 'ϳЬ',
                                                        'value': 'ΔɍўÙéХʱѴ¤͵ɫˇҥÛ±˚\x9bǚ\xadŘѱμ͵ѵȮǫÇǺӎɾ',
                                                    },
                                        {
                                                        'key': 'Ħ˘ϬżϠê',
                                                        'value': 'ӧɒпҋǓξƞˏɣɻǐ\x84Ȟ˯ȽӽĮӦNÍƲқ\x7fŭҤȊԃȀŉǪ',
                                                    },
                                        {
                                                        'key': 'ϸόǸрКԝόѲƹÍ9ƴɀˇӰѾˤ>ɞřВǍλԐӐ϶ü˖°И',
                                                        'value': '˘ˆɃйnĿЋʌϟˤɨ҈ǀǧ˗ҤԥŘŤƚǊɟ¿ЩϞÀҷ\u038bοҀ',
                                                    },
                                        {
                                                        'key': 'Iűɬ+ˍŃʡѵ\u0379ĉɝȁШǣψϡҌʶδɃгĐȅŝƼìӽǓϏӴ',
                                                        'value': 'Ԅô;bӎȩӋҎґԚʹƝсɶүɆŲǽĢ9ǡW\x7fnШϚӳōҁȚ',
                                                    },
                                        {
                                                        'key': 'ɨ˵Ɖˬťʲ)ҥ9ұ˭\u0381ҝ',
                                                        'value': 'į˚ǽѨϿŕʽɦƬ×ʪ˂ЕĴΪѪǤʞ\u0378ǎѰȸʋѥĪÃзԮ˟Ɣ',
                                                    },
                                        {
                                                        'key': ')ӞżҨҾȯ˶ϧƓ\x9cϏ\x89ȖʮғƤψ',
                                                        'value': 'ĊʆτŇƨ˄ďЙ\u0380țʯԫӫƹhԦǨˉѺȄӞЯǮӀӰɁӇЃ]ę',
                                                    },
                                    ],
                        },
                    'comment': 'ҡƩџϲƐα2ѢɋŴυǭ˺ӛ{ʊԣͱÌёȰű҆ĹƢƉҟԎѨЉ',
                },
                {
                    'keys': [
                            'ǫѢŷ˜ӑΡԉԩЦӾ0ƀвΑш\x90Ԛ˶ƹ',
                            'ʓѿk˳ǛʐϮȡҖϏHȺҡӿ˓\x9c\x9bŌˍπ£ʏȤ',
                            'Öhԇɀϧ',
                            '\x99Сʊǩҧҷë˟Еǲ˕',
                            'ӌ˗8ϜԂďĽѫø˻ǩσθĽġŦ',
                            'ƺÅνġЩɷә\x88Ɨ',
                            'Ƴĸƺʙ҂ȊçЃΝ҆ÒѝѬӔ×ƬƏ]Þҁm&ǿҶɞҝνщ',
                            'ǩӭ\x9bэDɎҕʺ\x84ˠœ˴ÄƖɤˢӛhδʣxȰҀɗ',
                            'ѫ˜ɉ¬ώΐEgˉԐӋĦ˅ŗƎįǹԕԭϏϠȱӱ<˚wΆπ',
                            'ӳѰYǗϢјɊâʐɍɆ˛ģˌϰ«ȫ',
                        ],
                    'event': {
                            'target_id': 'ķÚď˾ȨηÞόæǪӆҺŵ0Ǆ҉ϩΞ˂Ӌ{·įĜiҙɥšɄ˷',
                            'parameters': [
                                        {
                                                        'key': 'ǝǼОѱɱʪԋĒ҆ɕƐÇщˇŤƀȎ¸±ŮɨзOƱȀӶƿőǮĮ',
                                                        'value': 'ҀŲ!шӤжȬԗάяҊîàȻÍȰ˱ɜϴƸ;ҵϢϜҧǣö_ˣʴ',
                                                    },
                                        {
                                                        'key': 'ǣƩŦ˖/ŬԏϕžŐǎ˙ñωӍϙ҈ВČһȆϵ\u0383х˟\u03a2ЧɝЮϥ',
                                                        'value': 'ŦǒӒΤЛġǭûȠȸζĆԃ\u0379ΏŊΞºç˕ÀҪ·Œǳțʟ\x7fqԫ',
                                                    },
                                        {
                                                        'key': 'ɩɪϑQӢЛŁΕйʹŻȤŋʙɑԜɤрʰіÃÁĢЙŏŮўԍǚΩ',
                                                        'value': 'Ҕ˖ȗϙƞҒƅȇҥϖϧȯщҷɹԀɚǰʹІήɮңąӭưȚŸ`η',
                                                    },
                                        {
                                                        'key': 'yÆɺϟҟБ\u0378ēMGsЩĥПśð¬ƆВІɚƁҐϬЪƀԔЋÂȂ',
                                                        'value': 'ňϾʉŻÈԜԪɫįÂÍюӪʂȐ/³ӛъј\xadҰϦʝΠɡȗϋȰŻ',
                                                    },
                                        {
                                                        'key': 'ϷұТԖ\x95ɑǏіdǒІȔŇΏ',
                                                        'value': '«ҙåРʈǝƜʻŬĂѶĹҨӣӞФɊȚЂm˶ѤπȰΩŗұŬԬˏ',
                                                    },
                                        {
                                                        'key': 'ӤˠƃƦӹ;ԢȇơŭǞǗͰвʖԕɏ\x88Ϛ\x89ƈ7ǆώҹϙ\xadԫŷɯ',
                                                        'value': 'ҫ¼҃ҢƔΪ_φˉɁѐђҞdɣCǴԡ½ǧĩʨѷJʀГʑͼÕ͵',
                                                    },
                                        {
                                                        'key': 'ĞɯѦ½ĶΛŠķҧ\u03a2ƃԖĎȂΜџʱʤƎЮ˳ȴҀϜəƠʥǤɛĜ',
                                                        'value': 'ëɪø<ĀӤңϺϡӗϯƫëΜԌʦ\x9cŕϾʽƮ˜ВªͲѪϐԝӷς',
                                                    },
                                        {
                                                        'key': 'rãӮҗ[ӯԛEÒъ~:ӡϨɊ',
                                                        'value': 'fƺ\x95ɞГΝǔ\x8aԝʻƑʞ\x8dņԙԧϰøĴԧ˸ͱɚʹћҙʒ\x95Úš',
                                                    },
                                        {
                                                        'key': 'ɻĨƒ¥ȡɱӨӭʐͽԙșÎ8ļŢèŊ',
                                                        'value': 'GѮƴεʍӁӀԝƬʼȩ9ғ+\u0382˲ӽĥĮϙǳȤͻҬʖǷԡʼЦʯ',
                                                    },
                                        {
                                                        'key': 'ŊƻѠ:ÃӝӘЃƐϾĠӉ\x80ȱ²λʓɒǤı˅˞ϲя˨āˁŀȩʖ',
                                                        'value': 'ȐK\x89ȡӘÐǗΐ˂ĚӣȑǼäɁǅʗϨühӃșͷŁӝϢˏĈҥϬ',
                                                    },
                                    ],
                        },
                    'comment': 'ŬĎÆ·ŗsɆӫȚ\x9aƎjCԒƚχҿŇͲϠϧͶŐј)ӀţĎќĖ',
                },
                {
                    'keys': [
                            'ħʒŷŀΞӳε£ɦÆ\x8cʪό',
                            'ӏ»γ\x86ŏ',
                            '§ҿӅԇӼӖÝǏƍˮĠÝɡљF1',
                            'ϒʰâ\x8f˰¯ǄɛѼ˪ÍΧύԩƩӧӋƜ',
                            'ƕΌńƀӇѬƮɚƂRϥԙĦƏķÐÅɅńЫыΗӷ\x94ȘòФ˻Ǯ',
                            'ҟŸ',
                            'ҴċÞ҇АǃӯЌӢōtİÖ"œɢ',
                            'Ί˪\x90ÐҠÒϨƤȳłѵБȡ\u0381ғȾǡԐɵǄ˃ǯΰКЊ',
                            '´ĊнÊЈŖήįƳȘƸӢˌßʭʲћCǄŅc%Š',
                            'ƷŇ5ŠƠV˙жȆȧѷԗқ',
                        ],
                    'event': {
                            'target_id': 'ȱЙѣȥÄҰϵƱʘЭ©ǻƊ5ȳTǅѐġƺĈǑθÛΓǰ\x8eΪÆϑ',
                            'parameters': [
                                        {
                                                        'key': 'ӛƂɶôΣԃнȕϹʤ\x83\x82ς:ǦǧҖŚɑȀǹʠ8ф',
                                                        'value': 'ҋОŵǣBФ1ŸƓӝȻɾ˽ϬŦíҚƤʡԚϻʝУϸŕňǶЛεÖ',
                                                    },
                                        {
                                                        'key': 'МѮƬÒǰɫӒĄ¦şѻĪĸȀSϮwéТÂ§Ӫ2ãȝ\u0382ΈЗɟĨ',
                                                        'value': 'ΑŤϓɴ²ЮԈǿϡҰȅúЎɡӆϩģ\x8cȉӧʘɒŴªҌĈ®βƆώ',
                                                    },
                                        {
                                                        'key': 'ҫϿӅʁӷ×ϬѶȃԃŷʎƙ\x82ӬϬȌ˨ľȑŽӕĹ˖ʀόǔӰʿχ',
                                                        'value': 'ӁȠʌg½\u0382\x93ўǵĶǋӜΖɏªԀƢӀЄƕǠх˙Ʀο˷ýƄ˽ȝ',
                                                    },
                                        {
                                                        'key': 'ɧθvѱĩæ\x92ʵϓĈԄŎЧ˨ˡ-rǺļÊԘҥϧ\x8dǲāɜș§Ş',
                                                        'value': 'ʎӷЇ!ȁǌ\u0379ɌƧϷȔ˕ѧѦ\u03a2ӛȇΞҝӬ\x80°ҺĩˤaԔĢѵȾ',
                                                    },
                                        {
                                                        'key': 'Ɂ\x92ȎŰɯЙ·ІFĖѽƧѹɡśϟӭSȨ´wʗ˔οЁӘnѝȲу',
                                                        'value': '\u038drƀŷķψȵŋƆ\\LȮ˔ȭȊŀϦ>ϵЅǂ¼ҳÚZǮɋİϺ˶',
                                                    },
                                        {
                                                        'key': 'ʸ\x85ʜӟƣōɜ©ÂϽʃɂБѐȿҺˆʮŰɲńÝΦԏÂɊɣҀ',
                                                        'value': 'ҴɼŽh˸ˑОϦƃ˙˹ӈˑжΘ\u0380ȴʘˁE\x83ѿ£\x95¡|ɋˇſŤ',
                                                    },
                                        {
                                                        'key': '\x8c˪ˣОњфѫÏŧc˙ɅӤĥϞɣĚȶĹÎѐʎ"ύƝԓϦǸέӜ',
                                                        'value': '-ʐųʌԀΫϾϷjˡĦ˲ҰΓӱι+ĞЮЈʞӘӣΞǶΪӗСїΉ',
                                                    },
                                        {
                                                        'key': 'īɰǆŒǜØҤқ˟żԤÒŝЃφƜ\x89ƛҾʈŮϛԑƹӓŞдȄE*',
                                                        'value': 'ȢȺǴȽŅęӋáË«ôχǎKьǇMЂԃγƫђǜĸϫЀ°ǽ\x81ɐ',
                                                    },
                                        {
                                                        'key': 'ӧчǀҌ0ϡĠЃ©ϲѽ҈bД·ƁўŊөɴϿҐ˶ԪԚτʪǞFɛ',
                                                        'value': '?ԥԢϧŊΎԇŵόǆʶԑɄƏ˟ɢƬѐƆϩĆχƮʹοƩɤȨ˛¨',
                                                    },
                                        {
                                                        'key': 'ƳЃŅˌǕL\x81ӿ±ͰdϬ0ВÝΰ©óӾȌˌīǎ˕ϸʿÓќƃѮ',
                                                        'value': 'ɪʱҎӬ˴SЇcʮÆӷхΡϳԛĂέΪο˹}JƲ\u0380ɑʽӗ\x9aϰn',
                                                    },
                                    ],
                        },
                    'comment': '\x8eȖΛԪПӅµȕȠďǈĻтóüŗм-ȑʿǢĢę\\ԑĄŚӸÖȺ',
                },
                {
                    'keys': [
                            'ŒӚƋČФîƣҖȐ',
                            'ŚƃɄɴӥˮÀĲ˗ɞǷǨѲΚʃΞ[ϳѻ}',
                            '˲˭ƈӢԓ',
                            '\x86ӫЂҊťįɼɞǋѼsưŒŀ«҂Ԛ\x81ҿӲҨŎǀЕѧǫΌƀ',
                            "§Ϥү'бӗΝќρЂfè3˟˨˅Ɋ¾ӕơҿӓȽ",
                            'FbцŬÂȻƩίҠɝԪĂ',
                            'җЈʁьȷđǊū×ƩÉ+ԁҬЮԔ˴5½ԩ¯ЬÑAԃKăˀ\x9aɥ',
                            'ҍϵħ\x8eR',
                            'Ττԇƫã˸ǞԦʕԒʨəѼӈǲ҄ȝ˕тĎ\x94Ӯ',
                            'Ê\x90Đ˚ϯW҂ťԛ',
                        ],
                    'event': {
                            'target_id': 'ʇſԤņɭɎǼǈѿϒǜʡʲѻʕ˥œˑʑуƚĢǗ˗ӝҥǓǺÆ',
                            'parameters': [
                                        {
                                                        'key': 'ȗqΏϸŤӐĴϵťŤԞѳɠȿҷϽҝÎʼ*ǱʮϯʳɣѠŀƹπʟ',
                                                        'value': 'ɍŉǱѫǟĚ΄aԪϞ>\x9ałѶДďӉӹ϶ϪҩˊδíƐ˪ΤǠϕȷ',
                                                    },
                                        {
                                                        'key': 'ԈϵÓGҖƤѡʋғøȲq®ҲȈχ\x97Ϣ\x8fĒҩɳ͵ƓIЙ',
                                                        'value': '҆ҐёǪWӎӷiŋԩŒǏđϟѶːȅX\x9dÀӷBģƌùЕ°ǝľɸ',
                                                    },
                                        {
                                                        'key': 'ΚɕҿύjΪʍĀǯŇîӬǩzΘЭžȨ˗ǋԭБ˪ű˩ӯU7\xa0Қ',
                                                        'value': '\\ЭM¥ΊʒӚǲϊǄĘĴѯɻ˵āxИķǒ\x98љûȪ˓Ʒ¾ʬ˞}',
                                                    },
                                        {
                                                        'key': 'ÔɫƘϬψԦE;ԈǇѱsӺҎΚóʏɢƻˑHтҤʙʵӗȳ҆Ǡc',
                                                        'value': '˽}ǊȦ҈ͽũʾÁɔ½ϓӪÆґȤҏėŃ>ǙԄ\u038bʰyԞĆʗӉӷ',
                                                    },
                                        {
                                                        'key': 'ɶūīǾɘĴ11ϤĞЄҭˈҐͰѸşԣơӦЍǽȫǒUčЏҪҁǏ',
                                                        'value': 'ƊɘšІПЕėāɀѯΝИķʹʿʲ\x94ϤƴѽƔ҉ѵѫ·ĥ˂ăŪŨ',
                                                    },
                                        {
                                                        'key': '&°)ɪʒϛЖř\x9aҬѭӏ>ȔάˆĐӎήѱϤň˄ǃуļҕz˯ϑ',
                                                        'value': 'ɶӎ˒óѩ8ƊҫΌġ˖Ϣß«ԈȐnӡŝҭϟϩʌҮʧϪƐȡϡѨ',
                                                    },
                                        {
                                                        'key': 'Ӹ\u0378Ʌɟʄǒ˻Uōé\u0381ǦҜǻÅɇ¦ԐŬ˶ҝӧЖǼӿ\x9dϡ\x86ӥ%',
                                                        'value': 'ϥϙʁˑ΄uϳűЭШѡЫˌǚԀ#Ȇ\u0380OʞĽ҈żȴ˻¿м\x80Ⱦҏ',
                                                    },
                                        {
                                                        'key': 'ҊğαͺƙŔɫƴǢE7ϛӗѿˤ',
                                                        'value': 'ȐɳЩ˳ͻԑ\x83ѳ˄ÚÎԄʪʛ/Ϙ˥ȢΊрӚηψȿήȊԝ¿҉Ҕ',
                                                    },
                                        {
                                                        'key': 'ßxµɆ½ĮѱǒļēϥřȼÜԜҬ\xa0ѽDιМЦІİԀǪӮ9?ɞ',
                                                        'value': 'Μ[τ˔ʔȳШҎıǴԠâœdˎˈͳѼǥӘŭȽʡȘҢđͿáνǤ',
                                                    },
                                        {
                                                        'key': 'ÐÉȐģӤR˧ÁЪѨце¹ԑБȺӌěԩȠϋ·ԕ\x87уĈɦŏҮƷ',
                                                        'value': 'ҒϬӂʶěϠѨȨѩńȱǮɦ\x8bű+śC¶ÉǶƹƕÃˈԍ҇˄ƟL',
                                                    },
                                    ],
                        },
                    'comment': 'ǋ˞ԭʞyȓʭxʹĦɻѳԚˏУƞʄˉŞЍҔϕƀNѼOĻΐȋԑ',
                },
                {
                    'keys': [
                            '˴Ȱ\x84Ԡ˹,pȿōϩʯϴňʨı',
                            'ÔøϏğ˅ʧÇұDυƯϑɘ\x94ȠǥѹĬ҉ʷüɼ\x9bюčҥ',
                        ],
                    'event': {
                            'target_id': 'ӁʥłʰӡȿΆˍɯʋƧɿĴɔƄ7}śӝō\x8fXƸɵϷʇŝШҮ\x8b',
                            'parameters': [
                                        {
                                                        'key': 'ò˜ΞŚǖĵŚ9Ϝ\u0383ѝϠƩƪ\x87',
                                                        'value': 'ɞ\x84æƥHðsʹӎ\x82өƬҔ+ǋˉÍɴӣǧҵǩɨ*bϖ¯OϬʠ',
                                                    },
                                        {
                                                        'key': 'їτĵƹęȸҤ1ԥɷϤȳɨǥӥvԞ9ϸĂêɥ\x8bԚyӟȭȿǥɳ',
                                                        'value': '\u0380ʅӠίхĻԞɧʉƚхПԏƳђǽǶь#Í\u0382\\ĈǨЫ2ïãcɏ',
                                                    },
                                        {
                                                        'key': '\u038dEșůǮϟȐѡЪԋѸțɜɽъδӝѫʰéҎԌˋτơ˜7ѣȪB',
                                                        'value': 'ǽǛmɥЖҐ7ǝ҉ЧƗzĿϣjӱ-Ņñ&˻ќұʼԎ`C˱Ϭc',
                                                    },
                                        {
                                                        'key': 'ӽǡԕbVæĀƠŬѭ',
                                                        'value': 'ҫӸΠļωλȪƕΊʋОŽњԁϰϙɵϣӧУAƥΕȖȯĺčΡȐѮ',
                                                    },
                                        {
                                                        'key': '˖˶Оǭ˸ʺɠŸ˧щԗćȞčöЙĚӈМłțҋŎӝЛѯˁԄυˑ',
                                                        'value': '_ҐȌΞμơȪcїϊ҉ǓʳÁ\u0378ɞǼ\x91ӎ°ǴσǢ=ұͳ˷¨őʡ',
                                                    },
                                        {
                                                        'key': 'Ɖ\x91ǛǹΥī',
                                                        'value': 'ЪGǯˈŹĉǊœђЀ\x91м\x8eӼѫĨ|ˊƖ\x9cӝƎ\u0378ȯκɉаҺОȜ',
                                                    },
                                        {
                                                        'key': 'ԀʺʥúǲҀ¯ͺũĵ{Ƙаλ˥ǦǺæХƿƺ\x8eǵРæɂ˄ЁϿt',
                                                        'value': 'МӶʩĿǮ˹óȗƭǇχҼҔǐģŇeҵħХÒЋƉÇϨͿΝ\x8eŴ¸',
                                                    },
                                        {
                                                        'key': 'юϮϔ\\ʶƖ˽ѢʨӐшʏϿȹʾǑͲßéђ-Ԟ˗ҵЕĞƍҮʡϠ',
                                                        'value': 'ϓɦʽɯ¯β҇ń;ɆӘ˼©ʇʠ\x89ӤʔҗɝgȨŖЩЌύӸɲԍͰ',
                                                    },
                                        {
                                                        'key': 'ūǓʙȡɵоƠ',
                                                        'value': 'Ƕôș>ɚмĹǃƨǣƲýʞʕΔrӛѫÈN9ƋfЭ·ɏҚˡ˝Ζ',
                                                    },
                                        {
                                                        'key': 'ĤͷĢĿъԬȮҬҤӁRƵѫԒsȃȦѰψɽƉćΡƂοUĴ\x9fӁê',
                                                        'value': 'ǣúͽȲҡʌƊϼȳÔ±ɯԚԀȐϦɥʤªÐҐʵțʪƍ}ɘψпx',
                                                    },
                                    ],
                        },
                    'comment': 'Ӫɠ\x96ӊ\x94ιЃÑϛ¹ӪӨʁԚΐҴęmϩ˺ΌáȠɲʼɾòŦΖӯ',
                },
                {
                    'keys': [
                            'о$ŝʇ\x97ѤƫҢ³ȣҁƍх\x89ʷѓЈѴ|ˏǪ˞ɞǀËӾɾ¸ë΅',
                            '˯ĩғԈRϪƆǉЫДӾʏ5үũ',
                            'ȋԂҽѧ.ƒ',
                            'ʽԗѦǧɄǁåςϓϿşԂÉŉϺĨ6дЖBӴӗėćǺӃ',
                            'ËːƄԀͽӢÃёԟkÎʒϲĤαӣȉԧĬƼ',
                            'šŎΥ\x9a˝ԮȚбɴȲĔǪŨ\x91ҦƭʍӋɴЀϱҌƊƇǦϱ',
                            'ǜφǘώŵƞƵ;ǴӥҢR¨ƫ',
                            'ǖԟԆдȺөρƷқ~șƬӘoȳӊKˏŞĻ\x9cɎΌ#gӓҩӑ\x8b',
                            'G',
                            'ΤʹŖɃĲЮϱԬ1$ɮǯȈĎʬςėÏҜśԨȏ\xa0ДØpƉ',
                        ],
                    'event': {
                            'target_id': 'ӕЬӒƖɞƷĕҾȋʔʭБρűчÇŋʉqӔԞԐξϛɯ\x97ȥҕͷƶ',
                            'parameters': [
                                        {
                                                        'key': 'Ҙ˧п',
                                                        'value': 'Ε\x82έɀҍѿИǥå\u0378мĲӗáИԎȭ?~ԫɆµ΄ã˞˞ӓ\u0378ɑĚ',
                                                    },
                                        {
                                                        'key': 'ϟ\x88ƳʦKρ\x82úǊɆŃ˳Ӕº\x8eΎǠӕ˸ĿÒţȉ\u03a2eǯŦʷԋӢ',
                                                        'value': 'ЯƟȊԂįϙ\x9bԁӵϱ¾ҝȰɁљɎ˹ȿшŧүëҴїϲͱȵӏѧó',
                                                    },
                                        {
                                                        'key': 'Ѳѭ(ȈӪ˰Ȣ˘єʈŖ΅ɺ¬ӟ|Uɉ@ӚΖȈϸɂїѧӇнҩŚ',
                                                        'value': 'k¨Йʲ҉éʻɶ+΄Ǧ$Ӫ\\E1ӎΐ\x93µӂɈ˗ψѸ\xadѿyǓĔ',
                                                    },
                                        {
                                                        'key': 'ԄҘщғ˛ӯ?Űѹ"õҎѓϊϫȥƑĬÏ\u0382ȇПƟӱPʐҸ',
                                                        'value': '\x94Ĭŕ/ĮοL1˜ĲԘȸ˜Ɨ\u0382ƨʻҨīҍĂŊȀÄћԀϋʿΪƂ',
                                                    },
                                        {
                                                        'key': 'ìˋ˷Ϙͻǒϱ\x90\u038dʜyÑ˼ˋ4ΒƘЉ\x86',
                                                        'value': 'ĝи\x92ͱ=κĳǣĶң˓ɴѭѾǂWˑԛӯƁųϳÚϝȳ϶ïϣƷί',
                                                    },
                                        {
                                                        'key': 'ʏDȿɿǿƜÓBő{ѣҍŋĮзɚϧƟ˦κʡѯĺŒϢήj',
                                                        'value': 'ʋӑҖȿ\x89ɯȠИώԩҎ˨ӋȻˇΘ\xadϖϤʘ˲ӵɰԑ¬ҞѲҍɝǹ',
                                                    },
                                        {
                                                        'key': 'ÌΒӪţ˝ȷк\x82ĚǬȸЉʍuÜӦđƹ',
                                                        'value': '£Ԭ¿§ȼʦȳvѹҦәϘπŔƒŤα«Ɣÿ¯ƹ˦`˻ʆŷĠҺɎ',
                                                    },
                                        {
                                                        'key': 'ӺѸˬøğ˰¥è\u0379ҌǷȉЗԁ!ɟρԌʽɿǰχҕϹƥЪ˳Ȃƈι',
                                                        'value': 'Ǖ҈ɝԡ\xa0ϥĒŶȒǲЧĎͷѷ˵ҢŋӠĩ¢\x9bɵǵѿ˥ΟƄÚ`Μ',
                                                    },
                                        {
                                                        'key': 'ʸɯ\x99Ǔюɴî\u03a2ǪӘяΏӔ\x98tÖЬ7ҤфθŖύªȇХřêȿȘ',
                                                        'value': '?ǁѐƬɮҷϏïԇҔχhėƙȭőĪǠɊŔ%˞ƒОŨΥ\x84ǰ\u0382ͳ',
                                                    },
                                        {
                                                        'key': 'Ӫ\x93ǚЩ;ʎϳʱɼħέіʇϙд҇Ъǣȫ˓Ѣșƚϻ!ĳҙoϳÕ',
                                                        'value': "'ё\x92ёƜʕ³ʖˑΗӻGƎҥНļȱѸġǕǇŘÿ\x9eҮҝĎѨ˩,",
                                                    },
                                    ],
                        },
                    'comment': 'Ýӣǋ|\xad҈&Ϧʤĺãӽњ¬ӐĉƑПȖӱІӀӛ\x87ΡʷĬдǐв',
                },
                {
                    'keys': [
                            'ʧ˙žѳ˴ҸЍҡTˀ˛ȣͳğԛʭǟЂȌS\x9cʁʡ',
                            '˞ßŒ$<ξØҋԈcĖΩXʼϏӬҬÕ1έьƼѵҙ',
                            'ɀkѬÂϟ˽àͻСɽϸ#˔Ȗʫ˓˃ѿʗ',
                            'èŊƋãΝҲѡϳ\xad',
                            'įưɃӟÀňΎ',
                            '"і˗ĦļǃƓȐȘĕ˄ʮŷӁφűɋÇƨɪԔɵØ0υї',
                            'сǭŁ3˧ƅ¬ƚѴϚʧѡ',
                            'bĀˇыϊϖƝηģϋӫХӴŴȖ',
                            '\x86κˈчƗ\x82ОЯ˭¶¦"˼ѕƛ)',
                            'ŗэдƢˬѮ;ƔĭʧİǇѽώ÷ӵƬn\x8fŌǝķҌȦĤΕ¦ɧ',
                        ],
                    'event': {
                            'target_id': 'ӴtӆǄȧ^ɜЕE:ԄѐϾɺҖɆ£ƄòǑʎѯӌĻȝʭƛкlк',
                            'parameters': [
                                        {
                                                        'key': 'ʸůÝǌ\u0382¨ʗ¬Ɂr\x9c-ͿȽβȍɂĢωɗ2éȕϻ9ԣǫÜŭƽ',
                                                        'value': 'ʉʳ',
                                                    },
                                        {
                                                        'key': 'ʙ͵ŎƚƐɮɔǿθѳҌőҋԦ\x88ԇ\x8bΰЕѲȔ|ɦˋSǥӏåҗϻ',
                                                        'value': 'Ӵӌğ\x89ҭԜ¤ǖѽɔɇņGӴĔͼʿΝϘłɬҦІΌjНΆѝԕŔ',
                                                    },
                                        {
                                                        'key': 'ԁɻŧʶɿԥŅżҤρͱѾԇkʻˣЧƺʫYϦɈɓѕЅɱϋ^ϫǖ',
                                                        'value': '7ϱǈ¾ÜͱÈѫѴӧǈ\x83ķǇ_ʞК˗ǯȾ҆ȊUˋ\u03a2¥ӥiӡ\x88',
                                                    },
                                        {
                                                        'key': '˄Қˈ©ԭķǿФэ˰Ƿт҆ÊϽ6ΌˠеƜś\x82ͽɴΈϠўΖуȥ',
                                                        'value': 'ÎÚ¸ђίÔЯčĻΘŤòȂƔΎԐʶϯɁųŵɇτХƿ˩ʺ\u038bĎʮ',
                                                    },
                                        {
                                                        'key': ']ĀȍșȹӘT˷҃ʗ˚ƶϖҢɇɆϐŹǈҥͰӻĂÆƋǁ',
                                                        'value': 'ұ\x8aȺѿӱшԭѽδċϏЈˬůš~ԀƛɘӚψΈ\xadѮȑΗԫǙˠȏ',
                                                    },
                                        {
                                                        'key': 'γȦˢϽЍΜ¡\x9fAΆϚ',
                                                        'value': 'г#ʾ^ƖέęƵɈƥϩʭΏʖϫ@\x86ǚǃɀɌɾƹƘӧŦˎ\x90Эη',
                                                    },
                                        {
                                                        'key': 'ĲÜCǷљîҡÊȈЅªþӯĎԃϲ',
                                                        'value': 'ӱԊzɃ\x96ŭʃΥ±>Ԟѿ\u0379ЍǵάŀƃĐŸʬ{ΣÞө\x7fɬзȘÂ',
                                                    },
                                        {
                                                        'key': 'GΔǰЛϹ˰³ǁΕѸ',
                                                        'value': 'ѿɡ8ȬΫǉɬƃεȃȉΌØșʇɧȢʡ±ōʟŹϥκ¸ȩěLƥǰ',
                                                    },
                                        {
                                                        'key': 'ž˔ʱǦ-˸ϹěлˤʢϱԣT˄ˡΆȦÚåΑζŖūеäӥɊԞә',
                                                        'value': 'żӶ\u0382˝Ҭ˙Ǜӽ\u0379Ҥѧ9ǉ\x7fҒѠԩ˸ιͷʉƝҥԠъІš˶õΧ',
                                                    },
                                        {
                                                        'key': 'ЦʋEò\u0383\x9fɊԏƶO˪ŹнĪȒ˧ȜǉϬΗưɣ;ƈõªǫϑǊɶ',
                                                        'value': ',ɡ\u0381ŨʱŗΔοɒ˫ǙөšȖє˳ЏВȌӝǗԠХ˰νʿѰĬΊӞ',
                                                    },
                                    ],
                        },
                    'comment': 'ʖǄˋœфӅ΅&ȬԪΟпäψ҈ɄƓХ§˚Ϩû˻ΖɫЯӜԖԓŎ',
                },
                {
                    'keys': [
                            'ÉĿЩēˤŭ',
                            'Ɩ',
                            'ɋҠ}іŽʟÑ',
                            'бΐŻǝſϪƠѧʴԈʰ',
                            'Ђҡҕ[ęεÆԌҾӗШЗŠ^éĊҶ\u038d9',
                            'εqŶrɠɦσȡbԤӗȴʞϾʦӝ ˗ʗɢ',
                            'ƫ£чΗɷJӔ\x89ǸRѷ˜Ԍ˝αɏѻ˦Ђӵō]υȁ',
                            'ԖĠ_эĲϖϮдџĵȸ¹A',
                            'ȱYӰ',
                            'ʢśïȌǃāöСӥªѲŞԐɰҪԑǕВʟʧ',
                        ],
                    'event': {
                            'target_id': 'ѫĩíԜЩʛΠϘƀȄƛͷφȝψǖȐɎ\x9c˳ҰϣϽ\xa0ʙѤ\x9aƶȠϦ',
                            'parameters': [
                                        {
                                                        'key': 'ɷmĠ`Çl˒ɶғȘ˕IǿӻΌƭŉūȱЃſ\u038bɒ˸ԏӗϻŮӓԟ',
                                                        'value': 'Jѱ\u038bԩˑȥ¦ȊɀĺͲţӝǈɅǐπϜϑԧNӁϋƊbΥ8хИ\x7f',
                                                    },
                                        {
                                                        'key': 'ƝԡȕƇбéт\u0380ǗҔрŕǱȓQˠТҰœ\u0381ɇͶлEϬè˗ԋǳʙ',
                                                        'value': 'ҮEԟ\x9dʽĠәpԓ®ȎóґXɎӠŭă8ήҕΨңȀƔŬЁ˼\x96ʣ',
                                                    },
                                        {
                                                        'key': 'Ņθɝó\x8eҀΣĈż>ηɃԄ',
                                                        'value': 'ºќπ\x9dϽkћԡƌЄʬӞҲjǪҊȘӪΔɠΟĨʅНϺҴ~ŮяЩ',
                                                    },
                                        {
                                                        'key': 'ьϽÌ\x95\x94ȼȣŰǬˊÅʎ.IɢϼϰԦвɨƖúӠӭȐҁȯȫ`Ƒ',
                                                        'value': '%ĨɨȒ?tƪǛçΧ΅дѵϝѶуĦԎʙƵнŋ\x93ώEċԄőѱÞ',
                                                    },
                                        {
                                                        'key': 'ϺƒҔΡΟѨāâŧȳ·ǨÖƨIǸͼнčʹӂ^ӬȏǷѽԚҙ(Х',
                                                        'value': "ĆҲїάИʣϹϽЯЄÅ²'λȼĈΚ\u0382Η4Ґɱø˩ǃԥȖšÑԘ",
                                                    },
                                        {
                                                        'key': 'ʧЫ\u0381ŔʎʼįϙˍϱҗÞЗӬƄˏȞɌҌԍԧȪ³ѣßƴ$Ǉƻŀ',
                                                        'value': 'ûЖĤ\u0380ŸǪōÂƾСpҮǮЀϋȨŠţȘs\u038dψƔ¬AβƨʻÌƣ',
                                                    },
                                        {
                                                        'key': 'ԆȅĊȩğϖʉǲˑľԞ>ґ¢',
                                                        'value': 'Ȧέ҅έƵ˼ȉɾȷLҵʞңϠģѷƮѦėԀѫԙ˄ɗwҼwŹΰȉ',
                                                    },
                                        {
                                                        'key': 'ϸхџϤ҃ˋєΫSҬҪσǣ\x80ԤXʞȥÉϊϐҪϜx˵ʛéȴΡő',
                                                        'value': 'ðтɬӯËе˅ƂҠŅɇ;ΌʆьѾʦӔʵ',
                                                    },
                                        {
                                                        'key': 'ǫӋćɎўӐВνεī;ɬќеƂą{˔ģqſϜȌ\x90\x95шÏбπŉ',
                                                        'value': 'ΤˎѩɒйŖĞǿЂςљųʦϕқ>îɓϢұʋɒϱǨĽ˽ЀǙ/ӆ',
                                                    },
                                        {
                                                        'key': "Ѳɿ÷'Üǂũ,нͿϔɫȞ¡ҿª˺ԏΥϏÞҗҽӋ",
                                                        'value': 'ϥȴӪƥǻŤʦʈƼʆōҹȗњěԑԍЎѧщϮɷɎɹʎŰАӲǢɩ',
                                                    },
                                    ],
                        },
                    'comment': '\\Ʀ?ȭȌдŔӢΎoӤ˪оĵŇɾȷȉîѫJԀӎȡ\x97ȔȖӺƲ·',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'master_sequence': [
                'ɣ',
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
                    'ÞƆāǰӬԮ˼çӧȘɷǸԭ˝ʢ˙Ȑ;φ\xa0ӈǯʻĵ\u0380',
                    'ǨǅМ҈Ó˦ƤҋȅőЯԃгĐʏ',
                    '˲ΛćKʯ½æΪΫʙŝƔǵѰ˞Ĥ˗ҷH\u0379ʕʸǌη?&ǭ',
                    'ΧМlŎɟʮǤ\x8bŐŅΰүԏŔï\u03a2τͻ{ʩҍЗӀČз·ѩ',
                    'ҙԈoΘZјҸ;',
                    'ͽǍҿ?ɭӭҨŢɁ´Ĭ\u0378*Ñʃ\xa0SŢԏЙƊϨǗƐ',
                    'ţȮʉȵΗƳǲFҽӓ\x93"ΞσϒɰíϦԡɒҵĩ\x8cЙИΖˉϲѦΰ',
                    '~ЇєӾԚŷɔ˚иȯā',
                    'Ғș',
                    'ŔѫƖұȂ\x81шĺfÿ8źÙєϸӃǍѸ<ˎøÕöϫǌ˘',
                ],
                'bindings': [
                    {
                            'keys': [
                                        'ÜԉϮƯƺРŊʇȶúϵйRĩхÎ¡Е6ҟзөԮ/с',
                                        'ǹȱǱƅʩѯķӘҫβȼgʓˋ6·ʰ',
                                        'ʻƽԖʴ¹â˩Ȣőǭ˴',
                                        '˾ēѿƁϒƪȻȨ¿',
                                        'ѥǑǾʙϘǯϓʨˌØӼřӦƜÿʵӋėΒӥʰοŅВæҡ˕',
                                        'џķȜɨ\x9aʝƜůđ',
                                        'Ƅʥ\x91ƶБ\x85ĔĈԣ²ǬƝɰҗşʛԝƕŉӚϗˑǞ',
                                        'ѷәЏ',
                                        'Ј',
                                        'ԢʳҎӧѭʚѮȟšЛ#ȂăӺŸˤΡ',
                                    ],
                            'event': {
                                        'target_id': 'ɤŖŧԦ˩űɠØÎϨʫʩŞȖϹɈӱJmvΙΆҴΎƼčǁˀǲɺ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ɌѵƺäʑʹѢûȕӉƨ|ŇϤɮɭϨͶʂǧНӈ\x87ӁϜЬηňӕέ',
                                                                            'value': '\xadιȆПĐԏ˵ʥΔȈʨȰ҄ӈҝԑд˯ЈψˎХȑØ¾ɻԭ+ĝΆ',
                                                                        },
                                                        {
                                                                            'key': 'ƻĀƓωÑŝϞŧʃʍĖĂѳԧЫĉɀɎϓ\xadˤΟԥɀȸ¢θ˭tΙ',
                                                                            'value': 'вӖĦԩɞԌȾƉԘ©ҵ\x7fҠΛҠԁҮQϙѦɈ˹ǄͻɨǅȁĢČΊ',
                                                                        },
                                                        {
                                                                            'key': 'ԪΙ\x87Љǃƞ_ҤQοϒƂÆĕœԂЌȊ¢Åȟćʖѐ˨ƩТʃIɘ',
                                                                            'value': 'ŠƳѺ҂ӳ\x84ϕàУѯԥƢǒӋЮɂҋ϶Ǝ˵äԦˏȺüѤęƁӦό',
                                                                        },
                                                        {
                                                                            'key': 'Ν£³ЉγԒӿ˖Ƭ\x89±\x98ҭ¸Ģą\x82ɛϨǐɃȺÒʔʣMƐůӼЎ',
                                                                            'value': 'ȌĖČ~˫ć˃ҳθԧƗ{ПιŧĿȑԦϋΗӱƈlĳϣɹя¡ȅƸ',
                                                                        },
                                                        {
                                                                            'key': 'Ҷͳ[ҴӽЀѶѦ\x9dˁɰȿþɍˠНϢԤɆȍĸʾǯɻӵĪжº\u038bL',
                                                                            'value': 'ЄĽŤӜŹċвʪ˰оƒ\x90ŝæƅѽƉÊûƻүvҸϵ\x87đɇȍɅŚ',
                                                                        },
                                                        {
                                                                            'key': "ǥїµłяӫɃɳȭÅſ\u0379ѠҳʖưɮįǌҦӑŜŭ©¿Ï'ʟũé",
                                                                            'value': 'ЗƀϝƈųgѦɛҢҍʎӛǚњҖĐĠɁć0¬ʾ|\x93ɖȞͰjЕǯ',
                                                                        },
                                                        {
                                                                            'key': 'ɈщƟƃRѫ˧νϫϞÙɜ˽ƃӹδǗƓƩòˌ\x8eΊФƱʰ',
                                                                            'value': 'ý¿ŎԗҔȾĚӌĞѩԗӗ¥AćĚӲTȡѺфԝĽǄ]cҭΠΑɹ',
                                                                        },
                                                        {
                                                                            'key': 'ӏļaα÷ǗϴΖЋҌʑˋeȂԗѕȞć@ŗȕ@Ǣκ˫ѵɋжəԓ',
                                                                            'value': 'СΨˡϰБπ\xa0(ɳΚŨ˻2ѽ\x9e\x87˗ϑӤϡǇӲҝ6ǡΤѥǌǃĠ',
                                                                        },
                                                        {
                                                                            'key': 'iʅӗ˩žԧZΕʲХБþɉŉ¤ÄʠΚѬ·әĔÃѺġεǼӘ1ʀ',
                                                                            'value': 'ϾÀČɛΈҗɷТΟƊſԬǴɨžMԊӓǈӳʜwлå˝ȮƭĝŢǡ',
                                                                        },
                                                        {
                                                                            'key': 'Άè˟CƭğǻġʙϘǦФʕ°ȭHΛǧGæɾαҪĢƩ4ϴĂԎð',
                                                                            'value': 'ԉˑŶȬ\\ƞ¿ΧɨϸʞϾnʵ}4ИƗИǇ\x96{њҩӈяӻӷƕÇ',
                                                                        },
                                                    ],
                                    },
                            'comment': '\x99ʿйʀ$Ĭ˙ȍɃɷԢҜɤòŰҹӭİњ×ЅԉБáĒвѨÀςΐ',
                        },
                    {
                            'keys': [
                                        'Ȉӷĵσ˼',
                                        'ӉҞɨсìϣEĨʫҕȪɋӮσŲɊȴԕÖʊĚεӍ',
                                        'йӄӖяЦǨѪķ\u0381±ĺÕƾ͵ҿɀӴ\u038bŸрÉŞщȬц\u0378ȪͲ',
                                        'ɥȌãϢɠеǉͶȻȂÀ˖QƘiÌɡČĳĽ²ͻ',
                                        'ϬŒʶ¬ȩĕÉʉΚѴ˪ӟʑǻȔӿčʌɍҢъ',
                                        'ʎʆԛäѽґͰʀӫģӜˡɪ',
                                        'ˉѲѦũ\u0378ԇԗ\x97ʣƮӇ˽Ͼȕ.ķɇŇͿãŸϿ',
                                        'ǠłԡƱµЌ\x81FПä¦ɽеƠӓԁԡÈԢʻwѦȮ\x9bƫǉ',
                                        'ɰΣ0ӶǍΛŒʊ',
                                        'ҾέδҡăϹɟӘľҡƞ\x8f¤`ѝ\x94˾Κҷ¶ҝ!VҳЈH',
                                    ],
                            'event': {
                                        'target_id': 'ҭǹɫϽйВźę¬Ȱ^ǃƣˢƿŊȺ@Ûȓ\x85%Ң¾Йϰԛ͵\x93ª',
                                        'parameters': [
                                                        {
                                                                            'key': 'ŝĝëЮƀǴ\x9cƛҔʬ҇%½ǎӏїȳ\x84',
                                                                            'value': '½ãЯŭŤǜ\x85öşcІFăǲƙ\u0381ΉϿԪɧqΰiˎǝȏʣķΩƅ',
                                                                        },
                                                        {
                                                                            'key': '9ǮQƞȜ\x86pȇǙҾδȰ"ȢϜƈЊПUћnЅ˼Ɋԡäśȣ¬ơ',
                                                                            'value': 'ɨɐ\x81ЪōˤԩŜφɹҸҥʯȥÊӇǊϫƎӜėϖȍǿȚȯǐɥƼҌ',
                                                                        },
                                                        {
                                                                            'key': 'ʦ.\x8eȜȠȭӖ˭ӲӿƂҰǏ\x92{ΚҚІΌԅϤνфÂŵØӝ˱Ƥā',
                                                                            'value': 'ɹŗώˡįӖӿ¿ΓȰƥtӄţEʼˁϛЯҾϺӦƣãƚξʹҟӈð',
                                                                        },
                                                        {
                                                                            'key': 'ӜȽςѤӷ˻ԓƟ\x82}Ͷɵнð\x8aôǝȴaœЬҵǘϮЭԈӨĽũТ',
                                                                            'value': 'ȎÕΡҰγѱ`ȲƽТǢɂʪ\xadŨTԣϭȳSØßԘҐP¯yһӁ\x98',
                                                                        },
                                                        {
                                                                            'key': 'ΈӛсΎĊјӏɝ˕ƃƬϼƲ§Șș\u0380ĽL3J˰ԝƾħ˪ƞӾőȮ',
                                                                            'value': 'Kўͱ˕kғɶӺīѿΌĊ҆ƚŘĞɗIÉϔ8ҹΧњ\x99Ƒçŵʾτ',
                                                                        },
                                                        {
                                                                            'key': 'ϼòȬƼϗӶ˵ΫʝНҧˡȋ˞ϙѐЯƳȉƧΞƅȸϹƠҦҍȿ\xa0о',
                                                                            'value': 'ҦϊӫЃδТҵ\x88OΒʜќðȉvǶϰԟYȷŮʤĿƅäǘŌ˖ǚӰ',
                                                                        },
                                                        {
                                                                            'key': 'ÓƷԬϭϿİĵңËƹȣĜͲ˄Ʉƒ6˟Һ҆έ\x99Ș\x9d§˱ŁĞԦԌ',
                                                                            'value': 'Ɣxω\x89 ǿсǧЯ˜ДùέrûƏЮ\u038bϑѝɬčȴØʕˠҵʺӚҗ',
                                                                        },
                                                        {
                                                                            'key': 'МҡĉԎΑĳԋğVȾūŕɏ2ʻĔŪĉ\u0383ȟӼɪ',
                                                                            'value': ']҈ī˝ЕҸyϠŕԢȁқäĖɕ\x8fɔŠж´ʂ,ˊΏÈʎ´ʹԐԤ',
                                                                        },
                                                        {
                                                                            'key': 'ŶшϐѡϭǛjѳĀčѾґӔŜ҆ǼɢȦŵϥʐǕй\\Ңόǃ˳˹ʺ',
                                                                            'value': '\x94ɴƉѧ\x94ӇʢǈȎȐπŠώϯʹ˝ѐͲԢÕƽƊxϷԫţʏѭҚƇ',
                                                                        },
                                                        {
                                                                            'key': 'ƒӻέҩξǘɼϕâԜǯ\u0383ѯ©´ėȅźђØԎŨöŮӪƵŧ*ΠɃ',
                                                                            'value': 'iҘΰ\x80ћː˻ȞǅģȠȝӑQɒη\x80ɩƸ\x95ˀʅ˝ĦʓǍтʍϸӥ',
                                                                        },
                                                    ],
                                    },
                            'comment': '\x95ѲȴƌѢñЉ˸ɷӫҲ¥ńǅ\xadʜ˙өdMӸʷϖʯгȁ˦ĒҴѕ',
                        },
                    {
                            'keys': [
                                        'ǌҝϪӲ\x8eԗÀҺРƮƄѐѼʧю҅ҎʚϪýɺωΖɘ\u038bǤά',
                                        'jΐɩ˘D',
                                        'ķ»ѝŏɧaʩϻƠÖƏƒ',
                                        '¹ƤɬČ˗ƉѿϘgѦͰϊ\x92ѐ',
                                    ],
                            'event': {
                                        'target_id': 'Ω¬ŗǅϡзѥЕяɈŝ΄¥҃d҅Ӥ\x89ũƪʱˈϊŪЯƆʰʗXѝ',
                                        'parameters': [
                                                        {
                                                                            'key': '\x96˚ϦҬΚБлʍƋ',
                                                                            'value': 'ɾʺʀϹ8ӐXӂ²ƱƞӫǯĬкŚϻϮӛϳǿɰ҇ǆ MыŃдѣ',
                                                                        },
                                                        {
                                                                            'key': 'ӏ3˻ɜЋϛԧѷ\u0382єĒâ',
                                                                            'value': 'Қȶǹʈε\u0383ӍӠ\x9eҭåŜʐ(ӧɺЈӃʪԟĔ)êȪУģ˼ҕſ\x93',
                                                                        },
                                                        {
                                                                            'key': 'Іɒ\u0382OҏαUѫӷń\u0383ήҷАԥʠˁǰĜ¦¥ʯґɾÍʹŜv\x84Į',
                                                                            'value': '©ԒȈǬ\x8dďǇ˽ƀȧ÷²ɷŔ\x85ԉʒҋʄҺšӶñ˾˛τ˟Èƴ¯',
                                                                        },
                                                        {
                                                                            'key': 'чҠѢҧw\x97Ӌ{ЌбϏȚƆӚɔѢ',
                                                                            'value': 'ğǘϜԧȭǽ˗аˁʾԚ\x9aӂ\u0378ԒԣӥƩêЮBˏƔΞҊý`Ə·ʮ',
                                                                        },
                                                        {
                                                                            'key': 'EԀуԓźƎȥК΅ɈřɲӣŝǆԛԭcΝԕƉѺğįəˏ\x8aԀǋԕ',
                                                                            'value': 'Иͷ\x87іȟɕӢˣɽцϗ',
                                                                        },
                                                        {
                                                                            'key': 'ŀƋһƽƈţȿɨƔԮҵӣѲ²ӅÍϕʙkǴҜԆ|+\x90ǝȦ.ɿɳ',
                                                                            'value': 'ˀŉǊуǂĔǴúʽͰǐːϠϕѶÄƮèçΑęʺԏWɬСӓϞȚҼ',
                                                                        },
                                                        {
                                                                            'key': 'ψdϙƀƖ΄ӲǙɜɚčvˇе\x88ɐ\u03a2JϻљƵԧɾˎΜλ}ƛрҜ',
                                                                            'value': 'ԃ\x85πǅ˟ӊѭɊ˱ε˥ƒӿԗ¬ӿѾˉЂʳϑөΞҏҟʠ¸μъύ',
                                                                        },
                                                        {
                                                                            'key': 'ŰІΆԒȡǌȘӳƸdаȝśôŝԋͺcȡPҲΦъξϟǊºԑ\x82ƒ',
                                                                            'value': 'ԟͺRάљЁɭԚԏɄƄąĸǽIĆĻȋХȢƛĶ,WϾҜЦУɉә',
                                                                        },
                                                        {
                                                                            'key': 'IsƠǭҒ\x80âŰƤƩ˘ӖǍjΪӘ˞ίӖQͻ\x86¾',
                                                                            'value': 'ЪxûəσхɚŠҾјΆΩӖ΄ńѳɤǩȚhŪãĿˠ˄Ȭқ¼ΰӚ',
                                                                        },
                                                        {
                                                                            'key': 'Ώjã!ѢƮϳ҃Ҍâη϶CɞԜșϚйщѲ',
                                                                            'value': 'ɆøŹĜ\x8fʐƔ\u0380ԥΘƤԞǊMWԕІӐϵŲȵ˘\x88ӜΆҢŽPÄԭ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ǲŇιҖԕƕұƗȉK6\u0380Ӕ˨˰ҳѴq˾˵ҝȯǧíԎ5ɉǯîϊ',
                        },
                    {
                            'keys': [
                                        '\u03a2ЖȳˇϳԖ',
                                    ],
                            'event': {
                                        'target_id': 'ÖȘƽӻʪШŔǶҁѦԍǿȱ=ӬνɴĢОˀȈş¦ԥĢÞϊӱӮ¶',
                                        'parameters': [
                                                        {
                                                                            'key': '\u038b÷ƉӡдɴßӊȰǛɜŅӠōvȞGŃǼ˷Ëз¤ϛωѾʞ',
                                                                            'value': 'юɎϓɤʔʭЌʪáǕͱ\xa0ĥΙ\x84ĉǎёĸѦĻɀɘɞlʌ\x8eөʐϏ',
                                                                        },
                                                        {
                                                                            'key': 'ОώĘÔˬƻ',
                                                                            'value': '^ӲҝѦ<ŕϲWЬɚDƁыԌ҆\x94ƓhнĊˈ/ĺіjÒσʕΏɽ',
                                                                        },
                                                        {
                                                                            'key': 'ʶүԦ\x7f\x97ϳŢɢeĢӁťщF^ĴβŰǔӱ4ɭɟѬRƝҳɪ\x8cй',
                                                                            'value': '\xadQÂʾŴǿ¨Ӊ˙Ŏʦ»пҮŽӋȝǆ҉ԛԑɰ"đͱƊК˚ʢɰ',
                                                                        },
                                                        {
                                                                            'key': 'ϒԒǐӞȤӹ\x84¹ųӗԞˤˋ\x97ͺҠӻӄ\x9eñД\u0381šs˨ˑɯțӸʕ',
                                                                            'value': '˝ʏϼƝĒӑə҇®ԧǴ\x9cƞʃɚÀϫΘӹƯɴƷÜÎ²ȴȕҡʔȾ',
                                                                        },
                                                        {
                                                                            'key': '˫ŏӹ$ĕĥíЄσĽȰɺҨҗǺ,|ʽЗϘ',
                                                                            'value': '~Ύ\x9aòѣϡħΥжƃʋĢŢ\u0380Ȳ˻zӊ\x816ҜЪїΌtӦ\u038dȫɅщ',
                                                                        },
                                                        {
                                                                            'key': 'ÀζɻΒ\x85Ԉ\x9bʺúѝ«Ėξ÷¯ºΏ3ҮÙѻђѮ\u0382ȍͱҎĭѕȕ',
                                                                            'value': '\x9e÷ƶѓʁΥóɐkмͽtҽА˔ɩŮǩĈ˞ȁ¢ʔҌƍѕȤ{ѕɫ',
                                                                        },
                                                        {
                                                                            'key': 'ҊćɉȆ˭ȻɌȧ\x9aғцɕ',
                                                                            'value': 'ĊǛˮʽВɺZ§ќÔɇЅʑâӡҔÛŮԊïηϬuƞӰҴkʹ˱Ǡ',
                                                                        },
                                                        {
                                                                            'key': 'Ҹǽ˜ǉΏƴίȌΒưϵӀАκ#ȧʟ(˙ļȮn]ǦϒǘɰǭЀҵ',
                                                                            'value': '<ƷϑƤŲɛɑҘz˹Ӌ§lʃľȏƛԑŝJѯ)ӄвŨήԒ˷ʄƚ',
                                                                        },
                                                        {
                                                                            'key': 'ԅӺʨÊɝʮɓ˯ԚӶɏ\u0379ƓƵâcgƍΐс}ˤˮȕҌƕIȷņÇ',
                                                                            'value': 'үԈ&Ϝʯӽİǋ\u0379ǍɽœžԞѻǛѧιÞʪʀчʆMҡÉ\x8dƗӞЍ',
                                                                        },
                                                        {
                                                                            'key': 'fʃ˶ŕΕ[ŷϟњ\x84AƕѾŦԗ',
                                                                            'value': '5ϧuȈʋűϬΛЊəӚΙƛ;ʿҏàӣҽ\x81ќʅˑʕ²',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ƻқ"чɛҾčˀҴǗùʠИÄƼ˂ΟΡõ\x90ӎ&ёѵΤПĆϠʱӞ',
                        },
                    {
                            'keys': [
                                        'Ϧˏͳεʡɋő',
                                        'Еķ˜ǩŽʙɺɌ¶ǚƜщ5˕ČÍ0ǒȱɸt×нСџҝħ҇ԍ',
                                        'ɱ˧ӓùΐ\u0380ɜʇ˅ԐKђћͷϷǐʭ',
                                        'Ʃǻā}«ȳĐ5Ӻĉҡǲɚżƹʥеӄб¼ˁ˻ă',
                                        'ˢāҰЮϯӧȂљҡʅĠU',
                                        'ĿʻԡƓeƀŉԈ#ŉψ',
                                        '˃ˣӿΔʇԘ\x8fΪ˹иÆºоȥЏӣ5˛Ԏ´ӑʛлÁȯ',
                                        'єƮаƽξĐ)ˎvҩnϯԨžʠĂbԊɿɎǤЙÝ ҚɈ°Z',
                                        'čǟԙвŕǤžȟ˹ZĴԠҥзĀӕΉђ˄į`iҠL',
                                        'ˢͿ˱Ьtƺǜʶ6ΖԗrĘǙ΄ϻ',
                                    ],
                            'event': {
                                        'target_id': 'Ǒ5\x9fĕƷź;Ńȗ˲ѬǨԋҧъϼȰԒɺӈѺ\x81ʤĵӼŽ˕ʳǆą',
                                        'parameters': [
                                                        {
                                                                            'key': 'Ñ-ӨîɸҍͷŽĉ\x99ʢΨ6ɴ%ņ\x8eJȘԧϏưԪȊ÷жΧƅɶρ',
                                                                            'value': 'оǄɱɶҿ9Š\x95ҹϷ˝ɥȂωʣ§Ďԏģɐ ǩáʅr˘ѝȸèŲ',
                                                                        },
                                                        {
                                                                            'key': 'ұȼԥҩҶĚЉӧĽRͳϿ˞ȼʡʲöеҙΙȞϖεȰȳVGɨĨЫ',
                                                                            'value': '¹иʿͻÄÊ˵ΆŻɪЂȃșÕȒˎĘȎƈÖυȥǢʲĘԔ^Υvԏ',
                                                                        },
                                                        {
                                                                            'key': 'ːŨƬԧΗɈӒЛ-ϘʎњH}ȑ²ΧΥΑ#\x8aӲРɤɑϝˌ\x85ƿԣ',
                                                                            'value': 'ҍӦ˱ƯίιѮҫȷѮˉ®čԮҔ"ŊћʗϦϦΆΈÆҤɶҽЈĠѺ',
                                                                        },
                                                        {
                                                                            'key': 'ЪJƉЁԆΩȨжˇюR\x83ҹþùԥβuϗЁ\x90>·ҦлνɣȆү5',
                                                                            'value': 'ʂǲ°ΔǈԎ¸îɨ\x9aŌϫǊÉʹҨCͲӵѸśÚĞΤԝýQʟWǅ',
                                                                        },
                                                        {
                                                                            'key': 'ƥԔOМˆ6ͽǡθɗеҜƞ\u0382ӎȥBЗБ±˲ŬЯ˅đĴW»\x8dÓ',
                                                                            'value': 'ԩɰÆ˦ɸȅӾ\u0381ƙ>Ȗϫԧ˥ВҏΑгӹΠʫǝЖɭѨƘҘƓÈϞ',
                                                                        },
                                                        {
                                                                            'key': 'ҤɁüèι\x9aԬǾƴЃԅǨԒǜѱįѬáǵ\x98âμ˨¼ПǤóѧ§Ʌ',
                                                                            'value': '\x86¤РӾʒʅ¯Ƣʷ˲Ǿԧͷ͵œŨʽǂƒĜĈƿç\x82϶ÂżƩϵu',
                                                                        },
                                                        {
                                                                            'key': 'ϧÝϒņ\u03a2\x84ЕſʽԓɂтҜ\x88ϯŲÙӀǺī˯ѻįϚӁ˫',
                                                                            'value': 'ΩҍӅəѵºŅIѶmԬÛΌ°ʄǂÒӨþǵԜÊą˫\x88\x8bƱʾԠ,',
                                                                        },
                                                        {
                                                                            'key': 'ԅ\u0380ӪϮZˠrӆƐіΑИӘķԔpΛԆʿƷ9ǢŹ˥ƩϛǧgȭҨ',
                                                                            'value': 'ˣɞόŻϏϒͿΆǵȱˁƹċĮɀӿǊǆ˹ˎʉǚϒįϢӃɝԘԕ\x99',
                                                                        },
                                                        {
                                                                            'key': 'ɉˋŇÝȜɐӤȉҮϢѝÈκŽBӽʀЇԅįӕʃг҃ϛһɜĐϠ˓',
                                                                            'value': 'ƆʈɀDİИ[ӢſĉӅ\u0382ΦǥɷγЫɍͼϝÀđˬЃϺіʚȁʛϿ',
                                                                        },
                                                        {
                                                                            'key': '˳,ȂɞԁӸңѻĉǥƷ˒ǉќЦΏ¶пƶў[ηɒĖЌˤ^ђÐԣ',
                                                                            'value': 'ɶƺ¾²ȯǒȁѷγѤǛԤ¢ʷĝɿԋYĹɇÄω϶Àҷ¶ѱɯŽё',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ȄӹŔǖʼýǊ+ϐĎMSѳӃʿʕêЙҁĻōПҚ҈мɿуʹМΉ',
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
                    'ƽ',
                ],
                'bindings': [
                ],
            },

        },
    ),
]
