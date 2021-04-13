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
            'key': 'ГӃĕŜǸ˱FϐҁĝЦҨ¾ƜϋļӹӝbƮВѻԓúˤȐӯɇюĂ',
            'value': 'ѶʌǲǄʗȍŎͿĩʳÛƬĒвŃϓĺх˛ŠèĶұɧ&Ӽ+Њүü',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Η',

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
            'target_id': 'ʾʈśͺӔԇfµѨǘp\x80WԭĤȺˮǝʰŶǎƍ˕ȦAҠӲѝRϚ',
            'parameters': [
                {
                    'key': 'ДԨξ¸\x8b°ĜƃɴЁϯΈѥ#ǧЮƢ˽ýƵʜԪђκӗԅԠƯҵв',
                    'value': 'ƚОӋrƯ¬ĥѢΗӢ˟ÕԈƮ²ǾΖҴїíԫŸ%ӕϯԎԕ×\x99\u03a2',
                },
                {
                    'key': 'ό:ДԩҬԥ\u0381şέλþǎҬƊ\u0380ζĮӇµĂщ¬Іȟ`ÅЄΊȌʲ',
                    'value': '˙ΈǬˍǼΏʧiѾƆi¦Ӯv͵ûZȰӌ;ю˲Ѐ˰˳ǪŸʚεó',
                },
                {
                    'key': '˶ӲȈɷʲͰɷȮҴТΔ ȼԣȯϸæиɄϋȰЇ\x87ŭňȩϻә\x84Ŋ',
                    'value': 'ϨF«ȩȠǂΚ˷ĻѣƅŒӏ²Ѽεɝü\u038d҄ðΩϑӦòҍƉ\x9c˙ԭ',
                },
                {
                    'key': 'ǟϓȝʵMDóʡÅ²»Ӣ»ʐЅ6ҹӈˢĿÃɕщčԩƲ\xa0ԧčҦ',
                    'value': 'ҳϸΊƣŮ϶ǗxƕĳȋwʗƢϭ\x90ϰúƺˊԀ·ɫҀϋ\x9b¯ӵšя',
                },
                {
                    'key': 'ϛβƚөѺ¹ˣԊ˖ĭq\u0381\x8d˶ηǣїЀǴȬŲĭ§\u038bΦ\x80Ы±ßѴ',
                    'value': 'ѧàʫƒρÏϨƻűʬũʯΝξԥīǵʭˣ˚÷\u03a2ňʒò˾ΡґǨ£',
                },
                {
                    'key': 'PͽS&ϜҋԠ˨L}ΥʨҝȀΥm˳ÒʕʝѪÐʱЪҟәvņʎ\x82',
                    'value': 'ҏɥɕǳʒЉƳӇĎØӴʣɦĿ˃ҎφʜǔǇԖŜ\x91щʘʔɐдѶī',
                },
                {
                    'key': 'ѓĨӆƨʱԇ*ϯDШÄ˕МʾƊĉ\x9fȅåμȁłĕʆ˙ХQɦ˼Ƽ',
                    'value': 'ˣō˔҅ѪѺ6ώȰɹ=дÇ\u038dČёҮѮʽыϮUɬѺĝχ7ĵ˻ʆ',
                },
                {
                    'key': 'ьѬϜОÇʜӑΩŒç\x89ƺИ϶˖ԊˢΕңǭĭϖwϗɴНǍӁůȇ',
                    'value': 'Ư˾ӦÒE˪ԅеƅҡʹǐȂùBŢӹ(Œȡѕ˩¶ʜƯŌʐ˩ɷ\x9d',
                },
                {
                    'key': '˖ӝϰ\x9dԀɼɘǑĞˠūĽɂǳϬȝrԇʱʀҺӵǗˈ¬ǶĬ:Ŕĥ',
                    'value': 'ȁŘšÐ\x8cʴȞ˾ϽƿȘҍѝѹŲҐȀӖΉ\x8dčĦǅžɌɪÂª˄Ǖ',
                },
                {
                    'key': 'аȣńҥψˀɿ1ˁȣύƖˇ·=\x83ҊʤɬΉʫЌѣӦМŋӄҤӎϚ',
                    'value': '˱ÃӊŮ˘\x7f\x7fˮ\x9bҒȫȪУ!œѾɫ\x97´\x86Ò˗ɥȶ\x9e˙VʀС+',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'Ŏ\x9b©ÛԮ',

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
                '\u0382Ђ˵Ɏ\x9bġKƓ',
                'ѪȐѩțΓ\x8bµÉϨÞɚĥƽξ\x81ΐɗ\x8f˜Áԥ',
                'ɤĕӸȭˊӑkΡɊBɨȱҁÛŎжʋɭ',
                'χČ˪ǫƵȜĿº˥ɜɀ',
                'ʘǄȑЗĄ˂ɮӣǻӬɴǮϚъҚʆʡҹ',
                'ϔʀŇ˛',
                'ʢɭϾήӗё\x88\x86ȏ;ԙǤŶoų˳ԏͺś"Ԝ4ӷ',
                'ҢΝŒu',
                '҃Ϯ˷һ',
                'ȩʙŀƓ£\x92ζ',
            ],
            'event': {
                'target_id': 'ѤѿɮʄӐļǤɉûлΥĜQ°Ũґǎ˓ѝ˯NӶżŗӝAƎȬdϏ',
                'parameters': [
                    {
                            'key': 'ѐҽĴÛӖŲӤ¬҄×ĜњKʐȎϜŠ\x80˚ӠɺÊùѨÔŴϱЯфȄ',
                            'value': '>FŊ\u0379ĉʱԇ\x8aŪШ˵νмʘɸ˺ÂГϔņя%ÇҺδɚӺТŃό',
                        },
                    {
                            'key': 'ӂӘĩûѸíӅεԧʯҦʍЄšƑȣϭƚǊє˽ҾљǠĬõ',
                            'value': '˟ǳѯѼ\u0378KϖώϵȺҌηɆŃĩёŬHǱ\u0379Ż\x8dӜǵ˭ЃΥӗȐõ',
                        },
                    {
                            'key': 'èėɖҗϵ\u0380Ć΅ɕ¸ǬѿôlþɔŹǨɼʞƊ',
                            'value': 'ʵ˺ē_ıg6țƘǆюҏǝѫͻàɞҢƙЅȄЃ{ȾȗмȚ˘JƑ',
                        },
                    {
                            'key': 'ǳ҅\x93ǉ=˨ǣțνȼ/ѰΪwϻĆВǕȦ˻˩Ɲɱщƣʎ&Ү',
                            'value': 'ųӵ\x9bҹƕȎͱϠYґŴԋ˞ʩϫҡƙǚx²žĹЀԥŧњӣʘǻͲ',
                        },
                    {
                            'key': 'ѿ˘ŒʺúɤƥjOǺ͵!uŎļЮΒЂұNē',
                            'value': '˳ȞŚùÄc˧Ľȱ\x9eTѻп˔ϷԁӍ:нƕζȕ)ȦԟΐрǙȟƲ',
                        },
                    {
                            'key': '(Ƴī˫ƬЩǰØ>ԎҎхԠь\u03a2ŸϕЭŇҡҰ\x875ͶǢŞ˻¾Ňl',
                            'value': 'JѽʬuőǌόҬҭԋɋτ8҈ĈϥƄĺȁɤ½ďыƖɿÿјμōӥ',
                        },
                    {
                            'key': 'ԂťȖƉȸő¿ǀ]ѺɱǉʳǍ\u038bϻȾªӃƭ£ĕƆˑSƛŧБтƫ',
                            'value': 'ǹůǚТçǫӦιҼԚ±{\x9bďȶҡɄΉʦϖǭʾKψԘŷΣ\x82Ͱѐ',
                        },
                    {
                            'key': 'ɱ\u038bÞǳƸЯҘƱƆǏѕðϸeӛ@ԣŁЯŉԑŐ˼Йɽӫ\u0382ҲҏҾ',
                            'value': '\x83ǕNѤŁȡ=фiƄʥƳʌ·ĎɛԀ×ѵҷ\x87ȹԕŻҢщ҃Îǅԏ',
                        },
                    {
                            'key': 'ӷǺ˱ȘέƳÂԎƔøԂĥϿ¤ƻ\x99ĨʤѭԨЈƵͼČɉCϖԭƈU',
                            'value': 'ɋɀʾ˾ŭȆєг4ɤĪʑƄбÇˈƶdҼΛфĥЦ*Tԣ¢ȸ\x9dʓ',
                        },
                    {
                            'key': '¾\x8fʤ)γҦ',
                            'value': 'ȿԚʮǊΚРәӫȹҠ\x91ѨŌ(˩ýƺΣĈϒΑÃäåǚâ(eӊõ',
                        },
                ],
            },
            'comment': 'ΎԡІZT\x87ˍɐȚʍυԢͽƵǉǋϯԌԎӁDҁ˹˴Μėƈ\x83ԓԂ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ū',
            ],

            'event': {
                'target_id': 'Ȋęκäѻ',
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
                'Ȓϣ˸ŎɧĤ\x9a˺Dӣ´Ġџ^ƩϰǂҶ˪ʈ',
                'ÖțʑӷŌɢUϙTιҖԑ\u0382џ&ΆӤƌġɓɸʼӃǎЋŷҨ¯ʑ',
                '8N¼бŻĴԜ',
                'ɗѺԍǻѧÖĿǄċ¹ŘĭɽӾ˂Ɨś\x9cǪȻɒȘ§åѻəϔüї',
                '¡ϸ\u038dƋӴsʮǴԖӨӁϑəxƅґNҚΤԃөμˣƉʌƨ',
                'ҷӱɡėе8ώ˔ʔЀ',
                '°ѾҼȻůñ\x80ɤɗ/ǒϲſLË˒чҳжđЪ"ћ˒aң',
                '˫ʯąıƦоȿҵ£',
                'ȼêƓŨŋқŖŋӊψđƹǀãώúƞoͽÄȄЁǷ¾ġЅ˽ʂ',
                '˩JƏǀȏΚԣάɩǳƵЪ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ɡťŦҨƏV',
                            '?ѪɮƿθìȭŀȾȠͰƬώ\x95Ϲ1ӝ7ϡʀΕƸ˲ԫs',
                            'Ý\x8eɽ:¶˫ÙĚ',
                            'ǬӸϳϩ\x98Ɯʦ҅ЌӉĎƃęʶƫȫȏ',
                            '\x9bрϼЦ¨ӳüӈӝ6ԠȗӅȥфǢԘӂIԦεPíɎóϸÅ3',
                            'νѬǔa\\ԧ˄įϋȏ·ő',
                            'ͻǋŏŶΨδĜҿɳ',
                            'ȂéĩˈƘɾíˉӒ˺º˻τчƁƔԫŻѡĪϱÔљ҅',
                            'ʾƆȚȡҟЕɾǃɥϣFК˜ŌƤʑѫԤ',
                            '\x88ŝ˄ӡ¤HɩʐӀȞę҇ȒɏŦԘҼƸΎЊɉ',
                        ],
                    'event': {
                            'target_id': 'ɤΪɿʌťҴҹΑЧγЩɒ¼цƐѷǉЮʣŊŪȫˢgǺϜʽÖɜƐ',
                            'parameters': [
                                        {
                                                        'key': 'WӿŌȧԉŸßǝШoˡѭсDŘеϜślӮ˴ɌǺϝɂӊʚ˟Ǒo',
                                                        'value': 'ǊΣÓǴ+ӧNȸγƀѓĦϱҗӽѤɳˏƏԡΑњƝҹԣȜνɓԝɪ',
                                                    },
                                        {
                                                        'key': 'ĥМԗВɝbԊ¡Eʒ\x97\\ΰԛΑΌϤФnƳΛŵȕfΌǘ[ü[Ȋ',
                                                        'value': 'ŅƦ´=Ɏҽ\x90ԜƙʠŌΘ҆ςĞʰѮdŪƒыѰŽǫϣΥȁǔϼ\x86',
                                                    },
                                        {
                                                        'key': 'PΉ·ΞҡӒϟɋЛƇҤĭ\x8eŴ\x93',
                                                        'value': "ă\x98˽ºȩƥ'ԩɭгʐǘÅȐǆӽǯš˸йӌˤΒѠΊǈʈȱ΅ʈ",
                                                    },
                                        {
                                                        'key': '\u0378ǣсРȫϹ\x83ԘӆΐМƙӁǺΔʼɋǚSĊӛĪЙŰȚɹΆę+ư',
                                                        'value': '͵ӛϵѦКҨI˩ЁƉʻ%ƑЂеҖŷĠŭɯȝĕсƋӒӷŪʇ\x80Ԃ',
                                                    },
                                        {
                                                        'key': '®Ԭϊ΄Ӟ[ˮϔqʬɑ6ǑӯȖĔͷºŬʀ ŎҪ×ӷ\u038dñҿȅʗ',
                                                        'value': 'ô҆ÌƼɛĊАԠ¦ĦҘɈӡūˊЊƩΨϯ¤ǿʵzǟҗϩҬňѱӵ',
                                                    },
                                        {
                                                        'key': '˛˻ФʤĩǱȴɗλќвǙć\x93ЃϜ҅ѓǯßŴѷϗÄ˩',
                                                        'value': 'еϦЂϘřËĤɬʑęҮϭҤѯÎӔнґҪǯƫ˦oś˫ϟэfԀƥ',
                                                    },
                                        {
                                                        'key': 'éсǯŃ_ƥʋ',
                                                        'value': 'Ȃҫʘ½ӏĖЬƢҋʄ˞è\x9c°ӾθéАϷԉŀ\u03a2äёӛʹȀƍËҼ',
                                                    },
                                        {
                                                        'key': 'ˊ&ǑƗԆÖΡτƬÅЍų{ʹ6ΕҍёҰѶԍJȞԞɞҢѭˍǏ˪',
                                                        'value': '¶¶ȸӄƲөǃзəɬƑһʘȇ\u03a2ˀҞӦ²Ҭ\x9aāͽ?ʩϺ\x7f˴ӃȦ',
                                                    },
                                        {
                                                        'key': 'Ɗ˕ÎŻ\x9fγɅΖȓ\u0382ɼƥ\u03a2вʖʛ]ʭǮɯʇ¹Ϩ˙иѫ«ԋÌˉ',
                                                        'value': "öȴŐӴљǻ҇ʙȐ ñmɚЕҺǖҽ'ôÒTѻ°ѲēԒѳNӽ(",
                                                    },
                                        {
                                                        'key': 'ï\x96"\x9eҹ˾ɤ0ŊҹʸԡɜОǒаҕʻЗѓȗғȘԭɈԊɘ¹ϧς',
                                                        'value': '˱ΑMЁÎ˛ŲƷ+Ͻӈʝʀ˲ʺгüӘƗϗӭhɫЮƉĂȸɫʄԜ',
                                                    },
                                    ],
                        },
                    'comment': 'ʠʡҦɰϨ2\x91АǗӕ҅ƙӰzÊʮѫƝҤǻҌȔΙtɜҘɷϾɽȝ',
                },
                {
                    'keys': [
                            'ĀôţѥјϴŴгħůЮŴΒ*ϑȣPԤ',
                            'ȿȊɢε',
                            'ŏϕҸȎѐćŒӲ¾ҙ~',
                            'ȄƶȠąqΐ&ZʯĆϹȹƦѼşԖǳъ\x99',
                            'ˇțԏδЕǮǵȁʫȿÕŋӔΘǒЫ\x7f',
                            'ЃˑѻΧǤьюΖĜdѥ?',
                            'ʸĩŀ˕ѪňʤëÉΓ˄ӪĹԃњЭҪӮàΨş\x96ȉȡ$}ӛϓ',
                            ';b˓¾ӸѣӸ\x96ҟë҇҇5ϧˍƞԐ˧ʍ\x85Ͻ',
                            'ȈĐ',
                            'ҧԨʚ\x8eŊяԎúöв˽ǁì§ςiŊҏʴςǡȎôɽ',
                        ],
                    'event': {
                            'target_id': 'өϾӜtҰι3ŋΦīѩ˰śҿ;еĢ{Å\x9aϼƺ£HŋƯWÆӳ˓',
                            'parameters': [
                                        {
                                                        'key': 'ӣȮЛ#āǯɳԭŊȳэЬĠ(КӵϣņɆ˦ʍÊʖӰΰө˔ŀɋǥ',
                                                        'value': 'ǲϊӗơȨԞöȤҹƱҖҍѰΒɒ;ϖbΌ˨ƥҵӗìϛϛɵʌτȝ',
                                                    },
                                        {
                                                        'key': 'ɢŰƬʘζřŝԘ\x94ɀ»ɰԇġТϝ˱ê\x9eŢҽэɛϡɤА9Ķxȭ',
                                                        'value': 'Ӝ΅ʎҌъȺƃȜƁԂҔΎØиpԘǐĠԩƙɨӳƎӺσѝɯҗöø',
                                                    },
                                        {
                                                        'key': 'ѩƷɪ˼˶ԝ\u0382ęɐʺəȩϨƈŧ\x99ʙʥȪµʡŜԌÜ§ȟʂȲòƓ',
                                                        'value': ';аʥӷϲйːƚęЉѭŚҔƻөҽО8uɔɪȈʑӒǏÑG:ȏš',
                                                    },
                                        {
                                                        'key': 'Ǯѳ\x94Ѯ{\u0378ԝʆѫȒ\x9dˣŗʍɎӼӎǣšѳίŤгњȣȒȆæ·Ϸ',
                                                        'value': 'ӨƇɸʜʸǦӖ½ͽĻҠЂΉӆȢĬΤчʕBĨҞʁoҷψʣΖѪĆ',
                                                    },
                                        {
                                                        'key': 'ʹʠɲЏQŘϮʋ',
                                                        'value': 'áɜϩѭɝσʑӹɏˀщŖ˩ŧ˫ŉŒπwƅ4³\u038bϋő@ÈҀΦȆ',
                                                    },
                                        {
                                                        'key': 'ҳȊĩȞƳΉŪюĦ"ňΕĴR˨Ӡ\x86ԅϏĞǣȎѹӺϦſʚɈĀʟ',
                                                        'value': 'ӇύΪҚɞˉfӰӰàŵŤ˟ɆΡΓʴ϶ΧǬıʎϋӪ"ưĎΦÐѝ',
                                                    },
                                        {
                                                        'key': 'ƃӍɏЎӘǝΣ\x85ԧџð8ȥ˛ӿΐAɠӉƵÄҘƋύȇ\x8bķͷϢʱ',
                                                        'value': 'ϽЈϩĔԅюɊƏУ-ȅ\x83ѾϮíiһǀ\x83c͵ȝBоӼĐΏҚ$Ư',
                                                    },
                                        {
                                                        'key': 'Ƃ˝ѺǧǀĥÇĿŰŻůɅĢѥßʤǂрĺɝŔǋ\xad\x93ŀcÙŷƅ<',
                                                        'value': '=Ė_˔ȤџǻǪʹ҅ǯşȩ^ąΧњҲɗӨȌȎˊɼѪ]Т϶űΖ',
                                                    },
                                        {
                                                        'key': 'ŪȌɹžăĥüЅȘҫŶήѰŻƪƟď',
                                                        'value': 'ɼƣ]\xadǒѡˊÝʪқȡǤ˻ԓȢͽѯхuϩƞƲŷΠӌѱӖǺŉN',
                                                    },
                                        {
                                                        'key': 'ȓƟʼʞȅǽπłҗǇѹīԉφżȥҮÔĚϿ6ȇʾ΄%şÙõǁà',
                                                        'value': 'Јӹǽɹǟ;Ԭίϲ\x8dĐóωԂӍόȱ˩ҹJʨ,ÉʇҩTǜɞǮӉ',
                                                    },
                                    ],
                        },
                    'comment': 'òğʣdîÎǺÅȧȘӈȘƝƛö˺ώˊԨζҧ5\x85£ȓҷŜӶԇѩ',
                },
                {
                    'keys': [
                            'ŹÒЉɯΘϚȪ҆ƿĺȨ\u0380ӄƦˌвό\x8dɢϭΝ¢ʭ˯',
                            'ŽһƖäůɕĂϕӈӥφ\u038bӣϮ\x9eҲ˰ˬƑϬǉ',
                            'ӕѨǇ#˯òҩàα5ѰԉęοҦȹԁПҵ£ĝҶʐĞ',
                            '˘\x84Ιɯzˀϧ˕ӕ\x8afȡҁǻļĩȒŽκӻ¼â',
                            '>ȷνmзĹϫ˯¼ȘŖ',
                            'ʇЋŁД\x99',
                            'ɜκαЫřүǆʳOʴÍƭƐϚșĻÒóλþÅñȜԕ',
                            '҇ǏǮ\x85(ħλϖbѝǏŬϫƼӪ\x8bϟȊѯqŉǑƣ+ˣ',
                            'ǅǵώˬÅÃƭʟӖ',
                            'ˇR\x8eҦԔƭß%Ш˛đұҠԉſԒ\x9dˏʘĸ',
                        ],
                    'event': {
                            'target_id': 'ĪγĚ³ԣɡѾѯ\x9eѫǊЛǉϛԅԖɃɬһăƋǏǋɮ8ԉӃĪҘɌ',
                            'parameters': [
                                        {
                                                        'key': 'ԄĩğϘѼ˔ɝǧˬɑӦ',
                                                        'value': 'ņȹ˕ʀͺŭ˗ʏuÓǝȵҒÎћƯϣïĝѨѻϢ\x99ЙϼǼԔùϽǉ',
                                                    },
                                        {
                                                        'key': 'æŊԃɢѿBȼɤƄǻʾȧPϛ{ϊцӆΥϜǝΧǗșˌ˱ћЌж҇',
                                                        'value': 'ƿń˒fԟˋɴʒǵŚΌѬГʒȆǬФ˼˥ÞѭӯŲΐʨ8$ƥȝĳ',
                                                    },
                                        {
                                                        'key': 'ӌγưɡΏÆӖωǋ»ԡïХ΅6µŇҜӯԅѩɲŝȦ¯¯ҏøҚʚ',
                                                        'value': '\x9bǹ˜иǯӡòТrZԇʚ^ȇ\x96ǧȑП#Ȁ\x92г˓§ƾËҺЪ\u0381ъ',
                                                    },
                                        {
                                                        'key': 'ԢɥҀϫѮ½ɱɧqʥ«_ʺəѰԆҶſʮ7ΛѨ}Ҥ@˰Ő0˗ш',
                                                        'value': 'УÜ¤\x9fӸʿƄ˄ʎәӐĜ`Gϙ˵ғƶɣȮɣ\x9dӚ8ĩӟȧȌΆϠ',
                                                    },
                                        {
                                                        'key': 'ύ[ʫ´ИҶʜƻȦɞԀɏγҭÏɕGȟЫѠĳè\x9cѡɆϥΙUнә',
                                                        'value': 'ʜüƘď¡ǔʎ¥˂\x85ˢɻЋЎ˕\x90ǌȽįұƿŞìηiˢʭψõӟ',
                                                    },
                                        {
                                                        'key': 'ǔвĊŹϓμуl΄ϊ˵κԓ˻ЌϤ҇їǻ',
                                                        'value': 'ƅǣǕøҔďȢɺɳ ÝʗşȈώƾɵνœҙĎʚΡÖˇƭԚ˂\u038dʅ',
                                                    },
                                        {
                                                        'key': 'ԑԔÔ҆ӵВɨћ¼ɇƇˑ¡ƒԭͶɰΠΥ©ѷԘӽċ˚Ȉ\u0380Лʸң',
                                                        'value': 'ű϶ΣʎәϙÐӭѺ',
                                                    },
                                        {
                                                        'key': '\u038dĒԜȉʗӳP˔ϜԞǈħ:ӆƾοŖŔ2ƾŮgό҉ΎӲɄѭМ4',
                                                        'value': 'ΫƫҊҏɓöȲƈεŒӯ҄ƎǣӺѤӯΖŨǞǔԠ΄ʴ˜\x97\x94ȣʕn',
                                                    },
                                        {
                                                        'key': 'Ԡ\x98ԡΦѰмЗӒćǔΒ҆óÀ¡\x9aʷϪѵÌɐƯǿEЋ$Ħ˙ÂΧ',
                                                        'value': 'ӂȹŢÙȮˏ×6аÍӖя˅țЧлȗѨzǖƄѲʭƐČµŊч˥ь',
                                                    },
                                        {
                                                        'key': 'ʥԜéɟ2ˋтƤБɗ/SńзкӌǓ˯)ɜЮѓΐp҅҆kņʢǁ',
                                                        'value': 'ҜOįē¾Ӷ\x9fϰұsΧ_ͳȡԟÇ΅LëŠҷƴЋȐҔϰɣƇǴϘ',
                                                    },
                                    ],
                        },
                    'comment': 'ΫʪUҽυÔAÇͶIĩӞcκɮ8ΒҭɆѱϦȔϒƏΆǫϒǻdˁ',
                },
                {
                    'keys': [
                            'ӆѲҹÓÈϩ',
                            'їΙϢҘŅӃόȲΣҖȤğΪ\x98ūɩǎ\u0382ɷЈЖ',
                            'Θɐ\u03a2ǋȾԊҟ1',
                            'ƠaɯqÐɼ®ɅĞ¡£ӷοО0˸ѐċ',
                            'ҘеʍЙēЈąùpϚ',
                            'ϧЛͺѤғϟЀԢǍǤ',
                            'ġ\u0381õĶҀ\x92ЪÇęѮţӀ˻΄ΠƘȬδӲћӫѸ',
                            'ƗĿfŎ˙ӯȗɓ·ѝӝҢԈȝţˢϦ϶ʀȇÌ˽Όɥϴơâ0ʨ',
                            'ű\x86ϹµTЙԚ\x81ιβþɱƙ˲ϱŕˈӒ1ɨªʛ',
                            'ʊόŇĀ',
                        ],
                    'event': {
                            'target_id': 'ǀ<<ЈӣlƌǛȹůЌԈÂȟҊȅмƬϘѫВ\xa0ɉtдϗӫϽӕϢ',
                            'parameters': [
                                        {
                                                        'key': 'һˇǎƃɾÀǄøØμʄϞƮĊϠ\x80ԚȠӑ-è\u0383ϖʕԠϦэ˃ˋҸ',
                                                        'value': '҄ӏMǼ\x99#ÚӢθīӧȤȬʻâИ˵ҙĹǨүЬӰÅǕԜɽˡǵǠ',
                                                    },
                                        {
                                                        'key': 'ӓTÃ÷ˉȏ\x7fϕʻɋ\xa0ˊʡ«\u03a2ӂƓίKȘ˃ʛΏȺA˄ȒtϔԢ',
                                                        'value': 'ѬӻÜɌԒΡGˠȅҸČɈ͵ҊԪЂɍКrËæӢǥӊƧí˶ǿΌŪ',
                                                    },
                                        {
                                                        'key': 'ҧӂːȗԪʮсӉʘʳÓ¼ȊϒԜ;ϟϠэ»ɎʱΧȠˮЭ˲ӅɎЋ',
                                                        'value': 'Ęĝˠ&гѽɄԖ\x86ƯǴ_+҉ʀҗφʬÏǈȢpϩŵҊʄσŹƗԋ',
                                                    },
                                        {
                                                        'key': 'ѼģȌmȡ',
                                                        'value': 'ӑбѳи˜ăϘԬ®Ҳ6ћ\x95ΥύМϑÏ\x99άŕϨǉÉ˺ǜѳĦÏӴ',
                                                    },
                                        {
                                                        'key': 'ȔαˈԟѦĦ\u0379ĽҚň*ˮ҄˲вŝдƸϪǣҟȺεƹ˄ĐϯµTȟ',
                                                        'value': '\x91ŴǫȺҤǲԖМmβ^§ǶΓѧÑ˞ÄÓŖԒ˃Їόӑѳʹϣԁi',
                                                    },
                                    ],
                        },
                    'comment': 'ĘФŴʽʏϥɢ:ќŸ»\x98ћΪˣʭөϣϾŁȳĹiΜөԠũГǶ˾',
                },
                {
                    'keys': [
                            'Ҋƒ÷Ƌ½ӌcԊŰȳǼûŗӏˆ¦αΗǛ',
                            'ӉƧԋ҅ǤМĭeɘˏϻӖčѠĄӤφϧƣϡ',
                            'Ӻ˘έǆӱńϰÚ\x80ҥЊ',
                            'Ƌ\x9cȸӐ\x95ʺ\x91',
                            'ˬɞȃҀƃĈÃÎΟȮ°ԣ',
                            'ӡǢ',
                            'ЋƎ¼Ђш˽ңӭĽėŚĂӂ\u0381ӿƦІьô.ζȊß',
                            'ϘҚůКѢʺǯѻҹˉ˕ҺǋғʯԥtιӏκӞ\x84ƴϟͰ',
                            'ýǋϘҨϦӽ',
                            '7ƺŁ9ƉӣĦʈƪԢ)ýΰà',
                        ],
                    'event': {
                            'target_id': 'ΗҍъĂуԋ˶\x8aʿȰ;ɵΔƴkҫ҆˜NƈųǇ˯ąԍ´ҁ\x9f\x9fӋ',
                            'parameters': [
                                        {
                                                        'key': 'ɗʴ®E§ƎҞÄɘЈԓÏҾ',
                                                        'value': 'ҤƁпӡА`ЏΛѯŷΑʸԎƤϑXƂͶĄїʳĠӍʨRÓԙ»Юɵ',
                                                    },
                                        {
                                                        'key': 'ͺоúΐԀЉƩʢĽɌӌԙ7ΎЕĳҐÝˍѧ$˩ģΫ4Dşmơ˛',
                                                        'value': 'ȖȖѭљыЗ~Ǖ\x94ѫʊӯӺΓҗȂºӜƢƧHȖʏϏ·ТƁʹӯê',
                                                    },
                                        {
                                                        'key': 'Ѫ_Ҟōн¡øПcʄɪӷÉAΕԧŹőZ&ʡȥǘɶìʀӸү',
                                                        'value': 'Ԕǖ!ʙѳӸǶҬʋɣƕϾ7ɊʭɉʩAӨ\x81ʇљ²кПƫϦˇԉ˭',
                                                    },
                                        {
                                                        'key': 'ȩΠȫȪϓɁO˕}Ԑ',
                                                        'value': '\x96ρ\x90Ѭϑǉ˵ªķԛt҆ŝҖӋ˾ǑČΫҦ˼ҷˏҷɗœрӭ\u0380ƿ',
                                                    },
                                        {
                                                        'key': 'ɝñӟƱʹŖìғÌ˨fŀ',
                                                        'value': 'ΜȁĮӘ`\x89ġ˼ǤØ˃ϋҶφǭKһȋ\u0380ҸҢѕԫЎϔӁԏԠï҅',
                                                    },
                                        {
                                                        'key': 'ƜìɽMϊ4çӢη˜ǒɢόҬŦ9Ρ\u0382dλHӳōӮˬƮ\u0379ʓӑʥ',
                                                        'value': 'ΩќԩΘχ-ʒѼđίZņӢɌӶΚАɵç»\u0381ɲʻɣ\x99$CmνǑ',
                                                    },
                                        {
                                                        'key': 'lǑǌƠƅѴ\x95ɽӈҨҙӯг',
                                                        'value': 'ӱƒ¥ϸЛˤìɇ]ƙ΄ΦĔκͲˎĐрșȟɪ',
                                                    },
                                        {
                                                        'key': 'ŧɁƘӠțӄƀ"ƞѱϫшʇҦʎƴ»һÞԭīwυ£ŘѲ(\x7f\x8cʚ',
                                                        'value': '¨ɀŇЀΪŅќȠ-ɄǙӱοΞ҈ƾuǮђ\x96ūτ\x99Řϧ˝ɒнѦ˯',
                                                    },
                                        {
                                                        'key': 'ǖǼϔʔҊwǻǥɮҚѵƺƌȂѼſ1ӎĥҸǇȺͲҤҳʄмŦǭɦ',
                                                        'value': 'ùђS±ʛɣԫƬĥГɓǥͰξҙӁȡsĠȂÈmԕήԬΥ˾Ûťφ',
                                                    },
                                        {
                                                        'key': 'ӱҩ·˞ĕέЎӻŤrԡǮņlҔǣůƵƈжńӋƐǁŋψҥĔԀГ',
                                                        'value': 'ηԁÑΔAĞƿЄķ\x9aȷVʼ\x9eƼЩѓФщ҂ƦԚӆȎґ˴˸Άƫʖ',
                                                    },
                                    ],
                        },
                    'comment': '\u0379ûȒїȡЋŕԭǵɗÆӿʱϔҰҏɺİȃɱƥӲǟ҅ȾȩгʿŃ\x83',
                },
                {
                    'keys': [
                            'Ņνˀ',
                            'Ϧ\u038d½u',
                            'ΘΠǙƋˏ,ҷ^žЦĨêͽɰЗҶ˗ʿԈɃÔԇҰƩ',
                            'Υ\x93ӷƗ˨ҡĄß˓ԏɥ4яŮ<ӥϲ˷ʄäȭ\x91ԤȶƒnϒʘĖȜ',
                        ],
                    'event': {
                            'target_id': 'ӭҲƌ\x80àӈǦЌφΊҕƾĄҿǶѸŅƢԉьƛƴӝԫϕˍĤщ&ȕ',
                            'parameters': [
                                        {
                                                        'key': 'ˡ\xa0ɥʼ(\x95ȗЉȘƞæĆÑѼԃʵɞkϷϸԔ×ŞȹȭĎЄ¡Ѹ˚',
                                                        'value': 'öËәáũЊУŧÞ˛ѩǫe\x97˰яø@ıӏӖ\x84ЗўǊñуԫ˚ϴ',
                                                    },
                                        {
                                                        'key': "ƅӂǝŰѦŢʧŻηċӚCϤWЖƝĊѸŷ%ˤШɗϟϤʬԜ¾Ƴ'",
                                                        'value': 'bįʶɈқǼȓҒśΤǬĨõǮʠʭ9ϦȅQϣő²ϬˉΊБ¾хͿ',
                                                    },
                                        {
                                                        'key': 'ˈҸίѝAӘ*ŬһčέΈżʕӷ©ҒȱΈ\x8b\x984ɪćλġǄʑȠр',
                                                        'value': 'ƂǼƎƣƔ\u0380˝Ȗ\u0378ɓ҈ʩěə\x99ÊπĪϠЋϐlȥȁԎɦȬ\x7fίɧ',
                                                    },
                                        {
                                                        'key': '\x97ИљƺϢ',
                                                        'value': 'Ӭ˃ʲãԠaʣϕЦɱȘъǆĂƦŲόӒѕрºʦԞǉҳϡѰĭŮȉ',
                                                    },
                                        {
                                                        'key': 'èƿ9ɭĬҲV±5ηԞΎĸǺǣΘ\x9c˞ɔƏäɔϽŝĐſҳυѩŏ',
                                                        'value': '˶ȉǚҬʭƫƭјȟ\u0381ѺіɛѶЪɨʕΫȔЌėĳнЎћÁΥ˨ҕG',
                                                    },
                                        {
                                                        'key': 'ȫȀрɌϥΦɍϐ΅2ТɱНξ¢ιfӾƂŐЈͶŵќϘƢǢЧöɂ',
                                                        'value': 'ȗøȜŧŇдМƪӂИ˟ϪņŘK\x92ʍӆēΜҼbԤ˫ƬYɳ˪íŒ',
                                                    },
                                        {
                                                        'key': 'ǁɔ\u0382ǹҵўԐұƓ˝ā>ƣˈҞђԂ\x89nǧϣYʜîȠėΛɳɹÔ',
                                                        'value': 'ρǎ\x89ƮʪʹѨӝӋŗξɗΡŹńðϑ¿ɜǂѺ\x92ѱΥϲʛȮϴѽˀ',
                                                    },
                                        {
                                                        'key': 'ȚԡύˮɊÝбȬĸþɆҘєϫ˅¿ĭAϟ˱ŮԎ΅áđǒɊɩȺ\x8d',
                                                        'value': 'Ёʞϖ˦ʞ˜ʘƛđŀĽ\x9e¡ž¿Ľ®ʬϵɖȿȟԧфу˒ГŎѽƸ',
                                                    },
                                        {
                                                        'key': 'Ҿ\x96GɻдӫāʹƜċКĿƹ³żȿτеЅĔʭÎҊƕΝӅёҠА΄',
                                                        'value': 'δϱΖŉӹʝƨѧɗύԟŔåȬӷЦʳɭϼϮϲŹɴѮʟѮξȳ˸B',
                                                    },
                                        {
                                                        'key': 'ҙɈŀЉң҉Ɂ\x8fʦҎҰċʛ§ώτìӓʇȂ·¶ιǋ˽ˑɋɜеĊ',
                                                        'value': '°ǭ΅өХʵƶ\x88ƞӘЙ ǱȩЌŀƉкΨʤƑƯЊҗƢѝÇѹ˗Ċ',
                                                    },
                                    ],
                        },
                    'comment': 'ƷӿíП+ɲЋˏƂϪoћƴͳʐγԎёlǁѯsǴ\x81˴Ĥ_ќοф',
                },
                {
                    'keys': [
                            'ΩĲ(ϒɱĉş\x81έµāмХ§˾0ΫȽūǶÊΫҌɨ\u0381ėʁύФҙ',
                            'DǭΟɏŘ2ÙƓhӜƆȫҞʬώɯįʹ',
                            'ϺМŏǱɾѱƯ˙ŽϴеpǞʙƕ',
                            'ɝϺΞЭλӼΎӉЇԨ¯b',
                            '(ÎϲƑƬʛӭǯΘȗƅļ˻ţ¬˚ʋô\xa0âϒЦ˥ӿ\x7fˆ',
                            'Ԙñƽ˕JдŖ',
                            'ѢȀ\x96ǸÁƻģѡ_ɡ',
                            'řҀǋə΄P˜ӚɎщδzµ',
                            'άӀӛ',
                            'γÅψΌԣʠԕ\x8bŨΛ˨ǀ\u038bȋ3˫ȍ',
                        ],
                    'event': {
                            'target_id': '«ƣ˝êʗ\x90¯ȜŦӼGŮΖ!ԉɕŖҼȟǪFπғҢ\\ώʸǔRʹ',
                            'parameters': [
                                        {
                                                        'key': 'ʽʀȒƇÑɉ˂ǳйΣȺƞßŠă΅ˤҲȲʸӾΛрОI˚lsO\x81',
                                                        'value': 'ǤԇϿǵɧƅѣɉӭƄϋɾƭҿ˟ȾΣҐӎ\x94θǹʫɆĄНȨŜԃΤ',
                                                    },
                                    ],
                        },
                    'comment': '˶Ȓǒҥ&ʎӄҬǐǁǷşΫ=Ǉ\x80Ϫԝ˃¼ж\x8eɖӀϓi{ҹWȔ',
                },
                {
                    'keys': [
                            'ðκͽėϧӻ',
                            'ΗțǢɜ҄ȧ\x8aϬɺͱɵ¿;ӿԫӴ§',
                            'ǎŕɡʒŭě$\\ˊɐɀƅĦқ',
                            'ȖƱ',
                            'ҦГtÏӧϲ',
                            'ǼӱȕҡÉҖӖÙøµǇͻτŽҢŒЂ',
                            'ӬƉҨʕέ\x7fʯ',
                            '\x90qǤĨԠӂʊԡ',
                        ],
                    'event': {
                            'target_id': 'KϐҟɗĨϡƙƹӂŷӞƢ\xad\x7fҹʡkǨԤǃȻ˓ĔȊ\u0378ҒȞЇĎ\x99',
                            'parameters': [
                                        {
                                                        'key': 'ƛɌoůƷ©˟ϟΠϚͰϊ£ԥɂǤˀԜÐƤéŸȖƓɅĈlːѮҐ',
                                                        'value': 'ƀ˭_СжІŤɗӽ}љӓ=ʹӺ^˃ѱƉʆ҄ʜσ¿IОȝҚѽʁ',
                                                    },
                                        {
                                                        'key': 'è$ɉеУʬӓӀΐͰϨĴĵǔʉȗӼϯŝ¨ɆĮůӭϫòŧʁɪƏ',
                                                        'value': 'ԌɓƀɿѬĞʍ+oȒџɸѷˤҖȩ&ˑǌę˴ƅɵhȹ\x94\xa0ȃҵɈ',
                                                    },
                                        {
                                                        'key': 'ˡŐ<Ϋә·ȝѻȭĳöʻϸʬƀΡÏҮˀƪķşһяȖȊЗ1ʂ¶',
                                                        'value': 'ĠѺѓĵȦWɽgӈǨ»\u0383\u0379ĘœʮҩѼǗ*ЮԂ¤΄ɁԦ-ʃɄ§',
                                                    },
                                        {
                                                        'key': 'ĤҋŪBûǾӣҿӞʶ;όƷєɀ¹ƁƐɩǥ;ǨѣɻǵƘɵ҆',
                                                        'value': 'ƞǍӥԖҦ\x81Ʉ\x83ВԐȆĶǪƨƃ\u0382ĆôЋɉýԘЪūʡƩOěӾɾ',
                                                    },
                                        {
                                                        'key': "ΨΪϨqȮŸΪ'ћДǗɤőΘ΄˧ϵťŇɔȎaҽÈʷ¨ˣˆʹä",
                                                        'value': 'ӉѷŞ~FǋΰҕΠъȁb˲˯ȪĒɉљͷεşҴɎĩ2ɐ¹ʯәӥ',
                                                    },
                                        {
                                                        'key': 'ҫǛǏ¢íƓŲõӀΫǂśо',
                                                        'value': 'ǾáϯϞԟԘɇŃfÃƯ£ǱÓǵ\x8bчåʗǘΖ\x9eÒҖҩǅ6ʏϊ¿',
                                                    },
                                        {
                                                        'key': 'ӯƧǜǶȝӹήҏţ˛ŋB×IѿȉόżЀȾӒâͿƃӪɴĞк\x99ќ',
                                                        'value': '-AʛņӔMӇĖкȋИ˞Ǖƫ˕ΟӃʾśͳŔʝ˰ŭԁүȞʮǋЩ',
                                                    },
                                        {
                                                        'key': 'ѠİåÔӭ˪ϟ˝Ȑ˩ϻʎϭŌǥӷęʁĲÈ÷˸*ŒӓěԬķƬ˽',
                                                        'value': 'ӠӆyʚЫ9èҚɜ³|ʙӢ҆½˔ƁΘ˷Š\x873ƞȪãлҶżɬщ',
                                                    },
                                        {
                                                        'key': '\x85ŉѺ\x99ɧþμѮúɒϦҼËүѮ·ѽƪȬǃƆ0ҋЕͷŹǫɄʉћ',
                                                        'value': 'ˣ˃ɳҹξǅãƊǰìƾR\x8eζ҇ɽƬȫȉΛϿ<åαϓԘ҉½҅΅',
                                                    },
                                        {
                                                        'key': 'ԭ¦ʳ\x87ŊΆӮӜʼÓƩ˖ЯʺǠфͱΗĮŔ\x97ӋǵȫÀбɤɄcˤ',
                                                        'value': 'ÒԦǀѹ˙ȱƧŬшʑəӊЧǼǴ¥ЪϦјӈ҅ҪβŸΟɐȶǯǻɴ',
                                                    },
                                    ],
                        },
                    'comment': 'ǨзƸԇ˶УԢʏ`ĨˆѤ\xa0ÈͰƐýЋԊʠӞʪîɵ<ӡ¦\x8còҡ',
                },
                {
                    'keys': [
                            'ЯLԄӦӨ˕ҲȠ˥҆ҀѐΰͿиҥ',
                            'ǈӮɄ\x83ԃūǱßŶƭɞҘ\x9eH÷ƈɤǄ.\x96zǞ»ϛ³ѰʤҒǩ',
                            'ČϞАѕȈЖЬʂàǉБÇŇˏϨγŨ\x86҈ΆˆӘΫ÷ҭӄɃԓǫʧ',
                            'ˠƈŦɩȋӬӆӯʸɕ\x96ҭǽϭȗΦƺèȔΛԛҊψзƯm˲ͼ¾ƌ',
                            'ϣɢɯФЀȟíЦԂϝʊҕǪĻϙҩʞ',
                            '˝҉ȸϫȜӧȼ˅ȢΨΩȸķLҷєāzɤξΥȂȴÓÌ',
                            'ϡϾɩÅԞ\x93Υʺϣҡθͷӈ˳Ξ',
                            'ȦЃąºЍʺԗŰҧԠƢ',
                            'яΔșQРԒʵ˘ЍџŗoʨǜɃӢԒɫƧʖŗӃ˩Жʋ˖2ϰƌ',
                            '\x8eʒ·ςϦы˕Ң',
                        ],
                    'event': {
                            'target_id': 'ɭxѫΊ˘ĥƇÈ˅ԣЫѲȫļҊʽƨŬĜɥWōũԩŹѱϩêѽi',
                            'parameters': [
                                        {
                                                        'key': '¾ɱЄ^ƀԬȋӒђ˽ϖ\x8aȫȫԁǤƫђɷЬ҈ӫèÈɅω*cNȕ',
                                                        'value': 'śJ˒ȥɗϵƕɼѺˣԜђm˕Ԯz?˛ӼѣѓĴ\xa0ǱŲ҉ρәʾќ',
                                                    },
                                        {
                                                        'key': 'üÕӨɣȮŒŅұǱ҆ƏЮуѮ×VʢɔϘǳҏԝ\u038bȓȲƶ^¡ʪũ',
                                                        'value': "ͽђǨãӟ:\u03a2CşƊшн\x89Ķˎԟȳԍӂъ'ύϠŦËÕĻԢǛԃ",
                                                    },
                                        {
                                                        'key': '\x99ȊѲ£Ю.ƑΚӉȴʁǆУӊƺΌ˧ɀӓÄϢ˥û3ɀѥτưψЗ',
                                                        'value': 'ʏБϼğÖԭäҕĕˆɈɘhČœØƞԫ]ҷŢ\u0380ĔЕòǢϐʀӹ{',
                                                    },
                                        {
                                                        'key': '˵¦ѽ',
                                                        'value': 'ű΄ĚӍ͵ÉӲȓŉ.ӒȤãʆӏϟҺŤʺҟĦϟԏùԫзМҪʠ4',
                                                    },
                                        {
                                                        'key': 'ɱ³ѫӚRǦ_ΓÐİȥЗŀ\x86\x84ȹʽȎƈǤŗԥȼJ',
                                                        'value': '¬ҹʲϡήżϾӤѓɔĝ¥΅рsU˳ˡǶӤ˫IʟҘԙϏ¡җΐ\x8b',
                                                    },
                                        {
                                                        'key': 'ΝÕƴҷгˬ',
                                                        'value': 'ԞѝýΎȨȌɞcɅśӟϊчӐβԤƧǤȪӐß\u0383Њ?\u0379ү\u0381˄ƒâ',
                                                    },
                                        {
                                                        'key': 'ȪǙś\x95ǻЇӸÒϤƌĸ?˳\x99Ίӝȗќҙ\u03a2ФǹÅǻ',
                                                        'value': 'ΗҀ.ŸĈęǡǎˌpÃҖąxȝȰɚНԓʇŰɊ\u0383τҞȎԜӜxң',
                                                    },
                                        {
                                                        'key': 'ΠЯǕЋ:ͼiĤăȸ¹ϮˏŃgфÿ˰ɐġˤ·\u0380ăǉ˖ʭԝъɾ',
                                                        'value': 'ҼҡɖȠˀłĽϦΠƳԫ˖pЅ˳˻SoŢ5íĖьӣЯȷxÌ,ϛ',
                                                    },
                                        {
                                                        'key': '˺Ҕ',
                                                        'value': 'Ȼԁ\x95ǫuδɓªсҴцʥŸļѡƸ#˛ԢņӵQˣȻ\x8fıε\x8cȻ.',
                                                    },
                                        {
                                                        'key': 'ÆËĴѫҊˬʞȄÉєɟʖƞʸȌοГďĴ',
                                                        'value': 'ϿϮǀɺτ#ΔЪԙϭ˭ԉŬɀԅϥҕΗƧпѨ͵ҽŚȶåɅϞīɟ',
                                                    },
                                    ],
                        },
                    'comment': "ο˶ÃВӦǙĽÔ\xadҩg'ϭIˤɖˋƨ˱ʭ÷ʔЇH\x85ÞԟȢʉŦ",
                },
                {
                    'keys': [
                            'ŮƟɔŭĘʪȚʈʤπ˛σ',
                            'Ǵ҄İǲӇǑ#ˌӥȳĕфıŢɼ\x88ѓȟԭτ',
                            'ď_ʜŗѯιϚ',
                            'Ùыɵξγӗ4ȹj˦ԏԪҬyЄŧЄ¶ƒ`\x9c{өß˅˯Ϫ',
                            'Łǉө¸мɒʇҒΩǗŦЭɗ',
                            'Ƣӷ\x85Ŀ\x96ȇƫɎ',
                            'ʏȅĶ\x9dưò',
                            'TīқĳĠŹϨĳ>§˨ǀʴԦțȮɇӨŴÝӫјǇøŀлԠŒĹ',
                            'Ʊľ¯˒5ʞ',
                        ],
                    'event': {
                            'target_id': 'ЍɡʛƲ\x88´ҏʱӿȈІӄʣŌOћ¦¥ԀΓď[ǐə˸ƩkhЪǒ',
                            'parameters': [
                                        {
                                                        'key': 'ŉʀʙŰʧƞȣő',
                                                        'value': 'ѫίι\x83ʁѵāӱəЭӪȆƓԨȾӺϞƅÙӱɿģϖΑҍəɉɀ.ϓ',
                                                    },
                                        {
                                                        'key': 'Ͷ\x97ɂǹͺ˷ȶIČџԙξƃʺϬϢɱ\x9cŃÚΆ΅ǫĂ_λ\xad˰=˔',
                                                        'value': 'ȢĜųӼң×ɯǀɺ_.ЫưǤäͽΊЩ˛˶θӴхɺχ˝%һϽҖ',
                                                    },
                                        {
                                                        'key': 'Ў˚ǳЙİъҶÞ',
                                                        'value': '¯ԚɀҟĲƾԗȸĸɆKνȞʴȷAƼԖāҐРϸƃʲӄ\x9d\x91Ơӊ#',
                                                    },
                                        {
                                                        'key': 'э˟ŐɘĠȜĚ&ԀņǿӲʜŤЫɩӢɞάǡҎȯ\u0381рϳж\x95ʠѱƟ',
                                                        'value': '˨țʼʶĈё2Ǭϲ|ҬҨþÙʲҎΪвΌӠ¯ҀѰ¸ŘφŸɰ\u0378Å',
                                                    },
                                        {
                                                        'key': 'ƯœyƍŬÙ\x9aԒźѹĎͿͶɿ˻ӕʹ»ˑȼÉȻ˩ʱϩΦқЇΗŵ',
                                                        'value': "Ǖ˟ѳΘԑœāǇ'ĘνрƕɏĂǋÊ;İƝХӗŌԌ©¡ʯԠӻƸ",
                                                    },
                                        {
                                                        'key': 'ίľ΄ÔѪԨБȐɚʏŝȎКÁчыdϠ¤ʼȅқfƞɆλƭyђɈ',
                                                        'value': 'ʦIǓZQҬ¬ӘǎʤȾѫ˅ʱőʂŜàӟƶδ\x85Ўȏɳ˔΅ʲɧ\x89',
                                                    },
                                        {
                                                        'key': 'ğ=ZȊ˭ԜƖɺҕΠВ¹жԋÇǓǷƟ\x9fћNɳÊˈԑӫӷ\x8aԈˮ',
                                                        'value': "țҌҔȔ˥ΨöʿʃΘ#{ʷːƶԗ'¹Ǥʰ÷cø©ȼлІӂɮļ",
                                                    },
                                        {
                                                        'key': 'ɨȝƹƜɣƷЍ¢ǥҋŨĢӢΧҫ\x92˧ϊȚʿёϾҷЦˉ\x9dΊԭwɼ',
                                                        'value': 'χмCƘήϚdέȁʬƟûȼӓχ˖ѐƖɽӾӪξƚĸǧԒћϔǊɈ',
                                                    },
                                        {
                                                        'key': 'ТȱïοǓǲƩʓ˧ӋθӴνȴԅùīмҩЏ˂ԂõŤΛӝԪ·ιԐ',
                                                        'value': 'ǇĸФҢŔщԔϰ\u0383о\u0381Ů˧[ÿΦԍȘú˽ŁŊүԫˏěĆрɉƱ',
                                                    },
                                        {
                                                        'key': 'ғҏӣdԘԜЅȓͷ˟Ӭˀ½',
                                                        'value': 'αʥҭŵǍЅǈӜËвǩ\x95\x9bӳŹĎpһ˻ЯʯӦϭaЀĮƄюćͼ',
                                                    },
                                    ],
                        },
                    'comment': 'ŘǨK\x8a3±ӕЙę҆\x8fvȠƎɡʧφǹǙҍƛ@\x99ƬӎΐӖƳˌ&',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                '҅',
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
                    'һƋǖƚ5ȊDʗσèЛҶ\xa0ѐЛɖ',
                    'A/ЫŃӌӯ®ԣРɳэȥӍҶȐԥǂ',
                    'Ï\x8bęȕʀ\u0382ӰƶĄѩ҅ʵԥӒӼǻʅ·Џɻӫɾ´ʫҚТ',
                    'ĊΔơԆɫƋԜƌ\x9aˡƵӤ',
                    'Ιɍ`Ňʓ]ǷĳʖɀϟȞҋ',
                    '˸îǷƭÓԑȽ®ӖиˇӝҝуϊѨӨ`',
                ],
                'bindings': [
                    {
                            'keys': [
                                        '°',
                                        'Ǫƴ_ȪҒėѲ',
                                        'Џ˸`ц\x7f',
                                        'ƶΧч7ɊǋҡԬѾ³ғԒӀ¬ҮȴáϥүρѺʠˉ͵',
                                        'Ȩ',
                                        '˹ʩ˕¤ѵȂΐȜ',
                                        'ȖԪҭнǹэāµŭųԗ1',
                                        'ԜőлȸȿѢTŞ',
                                        'ɝҨɡ',
                                        'Łƻɶ´ҮƼɛ΄ȳ˔ԆÆ',
                                    ],
                            'event': {
                                        'target_id': 'ƺѽ˨2ˬĸ©ѣЇƂѫ<ʶ\x88r˱кɚȖʕМЋǬ˝ʁɶԪҽĒ΄',
                                        'parameters': [
                                                        {
                                                                            'key': 'ˤĘƫǧæˌ˻ӦƟĈǞȘӇŷnɋƃιʥƭѿņȠ˰',
                                                                            'value': "ˈҌѼôÑθƒƮ¬ǱђĴ$ϙʊӜȏϺiĢ'÷ƭrҗʔȵΏvҞ",
                                                                        },
                                                        {
                                                                            'key': '˗˨ѲƼцΩ҃xȹϲàĉԒƠǧғк˙ӄϨȍҁɘϿƉǍƼǨЗĚ',
                                                                            'value': 'ǬɧƍíНοϱϸЭӎϫJŮԡ%\x9b\x82\u038bӎɗόµ\x80˵ч\x89ҫ¦ѡ\xad',
                                                                        },
                                                        {
                                                                            'key': 'ϗgɓW˃\x81Ѡ\x92ϳɣӶO\u0383ɺȽɩԥςŖϟʟUЋȏОΥĭϖÂѻ',
                                                                            'value': 'XЗϚаƬȷĜěѝÐ+ăө¯μȂϴʌ˔ĹȚ·ԕә\x8a¬ɪ˗ԗ$',
                                                                        },
                                                        {
                                                                            'key': 'ɱȊÆ³ȇϵȽȨʃȋƳoҴӬȎʢϘ_\xadԮҤ˖Ԑ{ȯӸƙ҅ǰƷ',
                                                                            'value': 'Ϯ҆Āμƣ˯Ҥҗ˓Oƚοԁȯ¶˗èěЩκ˨ĿÈÕ',
                                                                        },
                                                        {
                                                                            'key': 'ˁ\u038bĀв\x99ŗ¹ȓĲɨΗӫІӕƹʂȜʙІЊѼˋǹԙŲϙȃÑ˅Һ',
                                                                            'value': 'ц/үϞkҲ˔ЖҔҩť\x90ɒҽЄӧЇԡǛиԔБЅωǄĔЧ|ŮC',
                                                                        },
                                                        {
                                                                            'key': 'ǐ£Ҡ\u038bѦϭԓЭʢƨӸǘ˙ʺʰ××ӯҝԠù',
                                                                            'value': 'Ɠ˔{ҲʎѕҷnТqьͽӇ)đŝ+ǋɽȊʹҭyǄ CоѠϸɘ',
                                                                        },
                                                        {
                                                                            'key': 'ȿà4ȶȍwϓаƅɜɣòŭ\x89Ơƫȣ˫μ¬ӪЛǅѐįʵө\x86á϶',
                                                                            'value': '¯ɮȤҩ˼ζη}ÖƐĠʼǧǪ\u0378ƌԍΝɗȣĩŦԊȼ¯ɲДүҵƫ',
                                                                        },
                                                        {
                                                                            'key': 'UԮ˼ѺщǚÔµǍʂ',
                                                                            'value': 'ĦˣćԒǓӂяçqɺʝίùåǍϜɹÄ҂ǖͷęɰ˼ς˾ˏҋϾ҈',
                                                                        },
                                                        {
                                                                            'key': 'ŨòӪϷӠ\x80',
                                                                            'value': 'ƙģæӝ²Ã˃ƵxбΌшņɲʁŧԆѨΈҲɀȩȗcдSΙңɁ,',
                                                                        },
                                                        {
                                                                            'key': 'дɹԕԖµӡ~ƠƧʷʆς˲\x82tɗǊțԃǭĪбҤǣΫфǾˬʐƆ',
                                                                            'value': 'ƏѮ¬ԡɕєʉ˫Ǟ\x91ɯŦӵӐ#lΨϦӭӥϹƥǠŐ@Ð˶ş҇ʛ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ĚĒƺΰYćėҤӡг"ʗͽˬħÏŖŗѾǲ\x8bҞʵҞҜʤgͿγ´',
                        },
                    {
                            'keys': [
                                        'ђʿŇrлƝ¶\\ьʰКӸƵȢ',
                                        'Һŏ',
                                        '҂¦Ҷ¥˻Ь',
                                        '˼PɂЧϽȅ',
                                        'ĤďɮӦ',
                                        'ƴǯһ\x96ҁƭҩȉЖλË',
                                        'Ӌļ˚ĶȺŪѮŭѷ7яû·Ȥ˶ʔď6ǂ',
                                        'ʗuʄ+ЖƗƏƽНç˝ü\x95ϊѥ˷ʺŖťӫǂ\u0380ƅϔ',
                                        'њĭĉˣώӺіŴ9ȯ',
                                        'ǪТ.ҶŸёö\x9dǭɼμ˱Š',
                                    ],
                            'event': {
                                        'target_id': 'ȨƸãƙӁΐɞşĩśƠλǥǆƢ¡ЌҲԍņƌɶдҫǤҨǈȬɨŔ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ʩϚy',
                                                                            'value': 'Ъ˰ϛѢӴΗƖΦӀЄɦɑʠǋƞŌǴϪһʳɝƬβӋǕҳ´Ǝdɿ',
                                                                        },
                                                        {
                                                                            'key': 'қ',
                                                                            'value': 'ØȐǾƨϒԆȣӳ>ɓµƩάуѸјχɍԇϤӡϯҝǐЈҕ<Ǉě˺',
                                                                        },
                                                        {
                                                                            'key': 'еɃгԪѪƇūŗσͷсͱçèūҘĕɭǘ\x85ˆǏĭɍ',
                                                                            'value': 'AєδЌïЁǍȜċǫ˞ťɫ¹ϖĊȿƳ͵Ȟ\u03a2ƙԛ\x88ԠǽҸ>ɠğ',
                                                                        },
                                                        {
                                                                            'key': '\x8eȽʶšŝӎӤԡҏяϞȍϕʂŚ¤ÅΧ¸ƔʸԞЭД<ΫϥÒƘĔ',
                                                                            'value': 'ŭϟ¥ӧvЁ˒ӽѷǥʧҥǁʋϢƸϟλ\x86ҨύİŻÅƞȕԙ˛ϷĀ',
                                                                        },
                                                        {
                                                                            'key': 'ɸԅ\x8aȗȗҵIŞ΅ɭӍǉӫǲɀψǧ¢\x94ɪԥĆġŷ',
                                                                            'value': 'δȟÁƀҾԋЅȧӹÊʷȞWЬЪĐнʽЖʰʩѵVʥң¸ϪɁʞ˷',
                                                                        },
                                                        {
                                                                            'key': 'ԍη¡KǈԜжԉԕʛ*ȔŇŅƛƴКκʉϬ¸KϨξɟQȿÂҠҪ',
                                                                            'value': 'ĜĒɸȗȢŝ\x9bӹkΐӋͷʙϊȃɋŹђĻѣӷѽҳԈȇ',
                                                                        },
                                                        {
                                                                            'key': 'ʿӉљқˢұӈĂӞúФѻɋ\x99',
                                                                            'value': 'ȆȤϾ\x83MđǔˮŜÙơǁǭΚΖǦŸȣΠԞЩӭȖİɊ˥βē¡л',
                                                                        },
                                                        {
                                                                            'key': 'цΚɶ҅˻ªԓ¬ԗ\x96ɰϚίϼƽЦҧ\x8aɍ:ʗȊʳӻĮϗ\u0379˦Ϛʖ',
                                                                            'value': 'ҺϐϤЙŒˊ·ʕЅ¡ЖƁmӜμЀ˼ϐȧΪȑñʹʘʢŠʍЧçń',
                                                                        },
                                                        {
                                                                            'key': 'ӎɽʬƍˮҌʈʯуДůȨɅLĔĸԦǷʈoȆѵ{ȒѓŧʛˡͲˤ',
                                                                            'value': 'тĨĞˊŶɹŘǢ҈b]þĸɋƕϣKǂϯ˓ҭȬʗԊǎ\x8cӤȟɦɕ',
                                                                        },
                                                        {
                                                                            'key': 'вŶһƵǷďҐɊϡʹԉƢԆԉҲҦNҬiҚȐȰѮʏӌӥψфˆѷ',
                                                                            'value': 'φхǃԢ]Ҵ˧ΩɎҿ\x9dѝѽɺĆïЮ·Юн\u0383ҍАӂɖˣ\x9c˩ȼԬ',
                                                                        },
                                                    ],
                                    },
                            'comment': '¯φȡȓԥԌűĊҗβ\u0378ŻƝЭОÔĖ;\u038bˇϧ˨\x84ÒГХĦ4®đ',
                        },
                    {
                            'keys': [
                                        'uʴLөϢ\xad',
                                    ],
                            'event': {
                                        'target_id': 'ʏÔlËΓ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ΥŸӉϯ/Ǣ˗ǞЄά˩ʷ:L҉Ɉë',
                                                                            'value': 'ʹӣŃʓƞѓΑΜîŏʚ«ѐƬԑ˚ȖϘǼç¨ӏ?ΰś҄χĺʛϠ',
                                                                        },
                                                        {
                                                                            'key': 'Ȕʍ2ӧӛƨʰ˚Ӝò\x8bϪDӌ҇ġҝЖ˼ȦŌҗȻİү&@ѝκѲ',
                                                                            'value': 'ǩÿ˫ƬʞЏƯщ˂ЙƊƳӝұԟδſXӥÊȏѭƇƌМЗƥӞȬд',
                                                                        },
                                                        {
                                                                            'key': '˝žƋƊθʐǹƟÄâɌҾÅ˨ȏƳ\u0379ÝÎÎϻZˈ˾ѿĥТ\u0380>ȱ',
                                                                            'value': 'Ć\u03a2Ӓ҃ԤʩɀǵhЖÍɤҔˮķʲѼӌΆбʹɧ½ǮʹÉ\x7f_±\x89',
                                                                        },
                                                        {
                                                                            'key': 'ɴɋÜ\u038bԫƚÔ˖]я\x83л˖ѲћѸҽʸĆԓԀƍϢӿ·Ǟçʄӆʶ',
                                                                            'value': "yЮκͰǮжƔrГƟĽҖ4б'ŀȁRÃ˕ɩϺȁ£ҞθкOµʚ",
                                                                        },
                                                        {
                                                                            'key': 'ԒҌƟɞÝљԛϹŠţԃҩΚʃѕΦûĸɁɎӅɜ¦ɢŢɬ\xadƃƤʼ',
                                                                            'value': '˛ÓӋ"|\x85ȗêɘȮƺЊǔϛ˒ϯҒҿŷΠ҈aԐȘƕȼԎªѵ¤',
                                                                        },
                                                        {
                                                                            'key': 'ǴÁĜϻÛřȏʌҽҧmŹ8\u0379ƋñɜӰ#ѪʖɣĴèȄЊ\x97OŕӀ',
                                                                            'value': 'đü҄Ȥ\x86ýτɿÀѐіßʤːӞƹňӝӰʒНҊțΚ¯đQΘǤ¸',
                                                                        },
                                                        {
                                                                            'key': 'ȷԄȨнˮƶñʫːҨőӷЇɰɇӟјĹſŞ¨ȜǗ"ǸǍĉħҙ6',
                                                                            'value': 'Íʱˤʢӿ΅ϑήӐʊpǘÚŃʐ·\u0381ʸǥ҅ƺ\x8cȓ\x89҃ɼύӔԍɪ',
                                                                        },
                                                        {
                                                                            'key': 'ЬiºʍĬƃ\x7fǡŻ´õƟҞ\\Ǳſĉѕ\\İZεӘӜϼЬǻƎϐʨ',
                                                                            'value': 'Ԋ˴ĒJџÓ\x96ϒΉΤԩǍſ˞ѱҖ˝Ⱦ¹ĔºÍͲ˾GƜĹèΙ˖',
                                                                        },
                                                        {
                                                                            'key': "҉\x95ūļ\x84Ўϕ\u0380'ʅЙńѮű\x82Ƹ˫ѝÇӳǳцŊϟσџАëźϷ",
                                                                            'value': 'Ζўȍ-\x8eƓхǭ\x97bǙŠҷӐRŖƹáŶӝŧȉΉ˵ͺ҈śJ҇â',
                                                                        },
                                                        {
                                                                            'key': '϶',
                                                                            'value': '7³Σϥǌȯ\x88ȍӪFԁҧċҒϡʟѷģхɟЏʉΔѕƎbЎqŷʹ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ƃ\u0380ǃʟ\x9fӲƘȹЌƍŉԄȞɫҊ¾ƙТİŎȐӃý\x82ʐīÿĩ\u038bҏ',
                        },
                    {
                            'keys': [
                                        'þȕä',
                                        'ȮȲȆǤǗǋʇH',
                                        'ŤC',
                                        "ȕhȃ\x87˗VǦˣĉ]ѫɎ'Ğ˄ɹѝVǄ\x8eҘĖʌȁϥ˰",
                                        'ϞЙ',
                                        'Тƫ/ϨһĈ©Ψˡ\xadȬӡÁǓӂґϡвŃƫŞɌбŉˬϻӷ',
                                        'ŧ>ӣ',
                                        "S'ȑǋԖͽaФƉŀԦȀȹêÙǴÎɝ#ΫUуɲ",
                                        'ҏӀÝô5ĩԤǫ҂ɔDğ¶ѡȻƕŪÐԖ',
                                        'ѨƍˆѶcΪʭ\u0378ΑK',
                                    ],
                            'event': {
                                        'target_id': 'ˑƦҲϨɥĎԩŹӵKԝΦҦňȱˉ^¤Ǎȣ\u0379ɑΈǛιщǕϭĢè',
                                        'parameters': [
                                                        {
                                                                            'key': 'áа\x9fµШιβŮʝYεȧāΪ˺˭Қ´҂ůeɮŹк¾ԡɲÝқß',
                                                                            'value': 'bŇЇʕŒ˕ɠŞǆϓɼɊыɉȵӒϑũ¯ŜӔǼΤʖЇǓɃͻ˂r',
                                                                        },
                                                        {
                                                                            'key': 'ē\u0381юȿ´Ӳi±ŉǊ3ˤԮЁҼȀҿˠË˲ȯӘΜйμԆƿˎȂˊ',
                                                                            'value': '\x80=Ҁ<ѱηēȎłԚКЎӴӥϢƦΩ˦ԇϗѴǼӦģԈҌͰӄʑϑ',
                                                                        },
                                                        {
                                                                            'key': 'Rp˙ʆƑɮŹȊ.ˌԚǳIǌǐğŝǤʣǼʍɐˠ\x9dŕҐϺԗĝȺ',
                                                                            'value': 'ůҷƠzĸʄʷāl¶ԤШȟJ£ӴΤΚOјȪςҹѽʼĻћ\x87ґѲ',
                                                                        },
                                                        {
                                                                            'key': 'ѤĢ¾',
                                                                            'value': 'GÓε\x97\x84ŊҰΡ¯λӠĺѸɠʴҔ.ϋԈǫ\x8e˘Һ\u038b˺˺СĩͲ ',
                                                                        },
                                                        {
                                                                            'key': 'ˣǆϑǨƎӠέҦǫˁ˗xćӹřяҵλѱϗԑˊćӅ˹ǎҰӎˀɓ',
                                                                            'value': 'ұƍҕ˨РХǓʶƐԕǈĜ¦Wİδˎȁė˖ĳҙÜԃϋ!ӂǮ˙È',
                                                                        },
                                                        {
                                                                            'key': 'ӆԡ˲ƷϫʄяɅːҳƺoǦΉћs·϶ҁ`\x8eñǕԊōǒƹƹ˭ϻ',
                                                                            'value': 'ŴҭЇJʡҗǠƞƧɠҼɁ\x9bÄ΅ψеɩʞйʲɥͼғƸӢӬ\x8c\u0381w',
                                                                        },
                                                        {
                                                                            'key': 'ș:©¶Άа\x96Ӥɇɶ/ҩȚ&ԍTɮǽŢ˩$7ʗʛǖϜƅԁʄü',
                                                                            'value': '\x9fȜǶ\x8bҩѾ\x93ХƗӪžӖѓAϩȞҷʦζ{ȜďηȯéӏƊ\x9bԥӎ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'çLѺѿƫĤƷԝΜȻʍťΏōӳȇӄτ|ǉǢϿ\x9cзϛӕȁɖɫ˳',
                        },
                    {
                            'keys': [
                                        'ƮÕ°ƗΙӟʊϰ҅ƄʰeӆˈҲоʠ',
                                        'ɐŤêѺÃӋЂҼԡpε\x97Œƨņ?Ì\x9f',
                                        'Ӡȭ',
                                        '҄Ċ',
                                        'ӆ\u0381ʓ',
                                        'ÔʤŪȟGяҜǽǠοɁɚ',
                                        'ѶƭȂͻ±Łԕ\x8eǓńЙԭљӉ˸Ś7\u038dȎӶÆʗѽóƝϻïłԝо',
                                        'Ϥǭ\u0378',
                                        'ӨӈÊίňӳъχԏǅwȓ˴ǪЪˇ\x9c\x9e',
                                    ],
                            'event': {
                                        'target_id': 'ǬΔѝѠňɘͻbŖϯʒ>"ƳŠǾÛчѕѼκ\u0380ʐҞđȇÒˏęϺ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ˣŧɨћČ\x81ȷȱϳжƭƠˉƱͳȲΩӭԞ¯LϴÒyʐɁ¢DζF',
                                                                            'value': 'ƦϖŝĶҽӢ˜Ȏƪª˚âà?ˣæϱUӈă˟ʡăѳȇӴĸěɪг',
                                                                        },
                                                        {
                                                                            'key': 'ѝͶӸ',
                                                                            'value': 'Ьƪɯ7РȫĥΕӼ¥ɜԀ4οŁl\x88ÁƠ˞\xadÉюɞ/ęǆѲʗØ',
                                                                        },
                                                        {
                                                                            'key': 'ɂь:ˤбƒ8uӷȮџO\x7f½˛ќɲƲŬ҅ľȠ;ğHŢΦ»ʢ8',
                                                                            'value': 'ˎΗǅρρEЍЛ½ʻÄПɷŠƘƍʦÉϻз°ǂρƽːʥҖŁΫÇ',
                                                                        },
                                                        {
                                                                            'key': 'ΗВӸʱʖɐȻԓÁ¬Ĕ\x87˝ɐЊѶёӦʋұϸǫ҄]њ\x95ǃіǱÙ',
                                                                            'value': 'Ԑ¹ьƂŧś˕\u0380ɰϚɌǏӃƒиǍʜЂПeʏәԌķӴǅÌӭҨϢ',
                                                                        },
                                                        {
                                                                            'key': 'ї(īęȐ\x92Дў¸ĥȭ¿ƥǙůǹɼƗбГ\xa0ˎǲüɦŗ˵ưԋ͵',
                                                                            'value': 'дƅ\x9fўмʘӌǙ҂ЇѿÒʎǸϱÅɂ3ηƶǂķЅГқѷǿɷĽќ',
                                                                        },
                                                        {
                                                                            'key': 'ɩƉ\u0379ƒ\u0382>ЋWԠȕ2Ӫҧ˻ԐҊʤʃԡʷ4ҬʀɁɎ˰71Ԧ¸',
                                                                            'value': 'țƐɳΛѿЃ˩\x95ĄĂЉρŉ*ӄφʮÚΟʕu˦ԕЦ\x8aσƗŞƓ҅',
                                                                        },
                                                        {
                                                                            'key': '˱ʧÊһɳʣѵɶȹӠ\xa0Χʥãһ¡Ҡǖ\x99ʽѤƁʹυԊɉ\u0382Ìąù',
                                                                            'value': 'μħӾβıȷÐcϱϙƾҾԔіɧϘЄӵТ\x82ϕÔÁԀƅκӭNțë',
                                                                        },
                                                        {
                                                                            'key': 'ЂȵǈЎÂƝӲ',
                                                                            'value': 'ҚԩȝȻȁŭǖÓ\xa0ΏӽɞǊюŘŃç]Š˪þpDsЮҌηӡg\u0379',
                                                                        },
                                                        {
                                                                            'key': 'ӅѷҩћӃьӼҚúƨѤЈӍΟʗΖ¸ŭǀѱͳƊʏоҰöϥϢnÃ',
                                                                            'value': 'îˊΈЕȂǚǦ5ÎȲͻ҇ǁǃΪȉВƻƛѺҙƓĦƑҝQПãÅʲ',
                                                                        },
                                                        {
                                                                            'key': 'ȸΫưťɊҲ£ϺɺìkųϪ2ąЄ\x7fɖ˛εļДӱÄĕӪԣԢҹз',
                                                                            'value': 'ɣβӒΣЭϷͱӌNЧŢ;˃Яӕɠǥƕ×ǦɫɠɧѰ҄ӢȚНӢȄ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ŵļӺźǩъˆŰȝ˹\x81ťԏƅѺ\\ďœӲЂçΪÁ΄˟ԇȏѶıĂ',
                        },
                    {
                            'keys': [
                                        'ʏĆʨοŐ{ƫϕZʓӁ¯ǂ΄ˣԫԈϥϛžѵ\x94ĭҎŎ\x99ΛΊ',
                                        'ӐёЩЀή˶ǽʷЮԌƵѫӰ§Ǹ˕҆ϑgˋ°',
                                        'ˠӳԬƽƇűэuðҷу˰Ƴ\x8dȮȃ³γƧπͼ',
                                        'Ԥ',
                                        'Kş\x85īǼҕόҒƻŵπΞʏĿīǋͽĉƂ\x9b˃ʯʑʍθ!ԈΗʈȍ',
                                        'ûζɲɯ',
                                        '©șѴϬ\x90Č',
                                        'ͼīzɌϔԑԍΝÆǨџԔҤȨʿͰȲɅ\u0378ɴWYĽmʠϚÈʙҳ',
                                        'ʸǇґҚσ\x83{ӶӓÐʂӥƶӀ˼Ҝ',
                                        'ƶ¶ѫɡӘÕ',
                                    ],
                            'event': {
                                        'target_id': '˫ӓ\u0381ϼмɚ\x9aЖ҆ʇΑΖ/ɨȵÑЕѮ\x8aɮͺǵ˗ˁԏϷͼȷ~˥',
                                        'parameters': [
                                                        {
                                                                            'key': 'ԩΗѿϰϦҾҖ΄ΞŽɴƈʧƪѓǏȁǯʬκƪüϵŵʄ˻˨\xadϸ',
                                                                            'value': 'ѣȓαũ\x82ѧӱȣ˝ȴΚɾҎBūĮǥхԭƴҡ\x86ʫΓʰίɰǶʦЌ',
                                                                        },
                                                        {
                                                                            'key': 'ǱзȴԑŢԃƮǝӊƄȚʽ\x94˗ǟтѪƬ˝ѻЊɄԫ˖jÞˮϩӿć',
                                                                            'value': '˙ԩƃǷ~ԦҏԝЖŀơ"ȶȐɛсƇԀȇø¿ʶĉʎѱĤũϻ$Τ',
                                                                        },
                                                        {
                                                                            'key': 'ĲțҐԇϤŌϭҸР\x97ǃiԀ¥ϡƶҷÎƽ¶lЯƬɰҮјԌĦ0˱',
                                                                            'value': 'ĤǺʒĖӢӟ˟ϡäȯȁºĦˑфĠšäƃˆҵӓđʝοѭȲq˳Ɠ',
                                                                        },
                                                        {
                                                                            'key': 'Tԏ`)ҝ˚Н\u038dƋƌˤγjӤƐ\u038dѕчǩŚŢɆͳǃ΅ҰʃƦҼϐ',
                                                                            'value': 'ǔɖɹҚŇºѤ˺ǝ҈ı:ӷωĈʣҚǸОυȊϠ˄rѫ·μTəφ',
                                                                        },
                                                        {
                                                                            'key': 'ӺŅя҃¤ãкФ˵јwϛ\x98өĸƥʰӭȜǙʽ',
                                                                            'value': 'ѱËĸԃЈ^ƿ´ȖӄϟӽʌΙҩÔ6ӿδɷȀ˻\xa0юɝˏǸщ˛Ѧ',
                                                                        },
                                                        {
                                                                            'key': 'Ǌϰш¬ǰʞ˶ӅůНѐéw',
                                                                            'value': '˩ҩ_ӟO\x8bӪɗјʕѡԂXøȳ%ʋƍRϐƀҙʹįʧҐƢ0ӦǑ',
                                                                        },
                                                        {
                                                                            'key': 'EʜЎͶȻvĦЀһűɭΗЪķǹǾĵѶΜԀгŬƌȇΖƻŢȩȳѝ',
                                                                            'value': 'ϾŻǉЊǳ¦ӁΜӷÎƶΰфћȠνÁőɻϗ1ԬźOƍę@NͿǦ',
                                                                        },
                                                        {
                                                                            'key': '˾%XƽǈɻȭӤĄ˂ÇӪΫȟcǆӮʙ\x97ʼ|ǼђО\x93ǅĴ\x94ĝʀ',
                                                                            'value': 'ѕ҄ϧҀzǖӟ\x7fƹӂГȣĳ$ňȻϡÈԎңƬȑʿǚƶжęjwҹ',
                                                                        },
                                                        {
                                                                            'key': 'ʮӪʘ\x9bҹ\x9bԚäʖЛǚƐЙϰˤԘΌǫĪ÷ǛƙȦӳƧϚɴ[ӷм',
                                                                            'value': '5ʲÝĊԗƶhʍrnʻѕҀćδËѪąǣ(Ũ7ĄғϽϔƇƁ\x8eď',
                                                                        },
                                                        {
                                                                            'key': 'jӑϼҚԅűǭǅ²ϪƤʡҦҼŌǭə',
                                                                            'value': 'tÍʹЎ\x92ӉΒ6ʕ˳ÅкϦ/ΘɅŋʪž˹νϤүĿ-ѪѺ~ӭɁ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ԏȓЭпўҗӔŧϱеЌѢϒԓ\x92ʷ\x98ͺЭҿDѿϷ#Ȭ8ЋOΊϞ',
                        },
                    {
                            'keys': [
                                        'ɨИ§\x9fˠČɗϯČȤΞîӜ#ǋ˙ҚЎҪʇȎˍ¦ȑӎŅ8',
                                        'ЍÀāѠҵƖǄĮȬЎǻŮʓŨϸŪřȑZɼ}1ʇˇƳ\x8c',
                                        'љҩȡƚιň',
                                        '2^ҰţԎԊô',
                                        'Ϋκ˧C\x94ʃӃ½',
                                        'ÝʍвВƩҟñɡҋЛ\\ĠєʁEͳyΉѻ',
                                        'Ĭ{ʧŲȾǭӴѡХʔķΝȶɢԪĎƷι*ȺčĒŚÑӴϡĒǑ',
                                        'ЭƦԐȣΤ\x85ѫĿɜВųɴѭӲǂcʍɲ;ʢʕ',
                                        'ϕ',
                                        'Ӆΰʾzΐ˴čž҂ȑŀˊƒҍˉƚʟˀ˹ȇÆɂӼ',
                                    ],
                            'event': {
                                        'target_id': 'ŝΔΎӇĂðǲȌHԒoҿϔ˫5τ\x86ĮlԂēƕѼʏϛξϳȼϵŻ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ǋˀ¾ƪϿĥƏǋǇӟē˯\x928ƲҦºȺȦˆâʂԞèȧìxĝʽι',
                                                                            'value': 'ӲǜũȦωʋʧơJŊ\x8dʠԮҾɲɏϹVȵѮĥ¸©τԥɁҋκҤƲ',
                                                                        },
                                                        {
                                                                            'key': 'èŠʕϗħӟª˲ʰҨϼƸ¶ÄМ\x97и˟ŐξŎɋèҊĕŬǌ˓\u0378Є',
                                                                            'value': 'јԍŎϗЮȄͽƃʎѼǡŒҤÔʜϢȷȭ½\x91Ƒł˱ǂȄƵυ˴Һ&',
                                                                        },
                                                        {
                                                                            'key': 'ƢʺǦәѣˈЫ˜ӎ_҂ƺǱϵɖͳʺĴĂ҅ȌȴņĖɚƙťԙâ\x87',
                                                                            'value': 'ƷśĚўԁ½Ċ\u0378\x7fĄ\x8b\x87ͳȮγ¿ʈĩʥǐФɍØҶWƸˀƓƖK',
                                                                        },
                                                        {
                                                                            'key': 'ѧ³ǘ҅gгǀʨψҴ˗ӊĚϔӜJǔϯҲб\x9cȃşѯiʏƽɔЊȗ',
                                                                            'value': 'Емє\u038bˬθэ>ŗ*ÜȟԤƵ¾ͺŶΉ}ȀçƬʎͺΈŌ˜ɿ¡ɨ',
                                                                        },
                                                        {
                                                                            'key': 'ëˠҺíԀӵÄϏʹӆǾĆ\x98˓ӁɾӵϞȫĄζ(ҏþǭЄϭƳ',
                                                                            'value': '϶ćѰв˫нóʓɠέϩΡá\x88ȰĉûȆДĨĞɌєӱΏӣѻƽñā',
                                                                        },
                                                        {
                                                                            'key': 'Ѕ?˜ʙԑϤ˅ãɓ',
                                                                            'value': 'ķ¬ʹdӵɾʰ҃~éжįѰɳҩҶǛԎ÷ОϬǙŐϱԓңǫ\x8a\u0381Ӳ',
                                                                        },
                                                        {
                                                                            'key': 'ǯΣҜγе˱ʫİ˾ʐÙϠÙŤ\xadΠȋɀϓȀåѻУʲȇɴюȄʚғ',
                                                                            'value': '҇[ŔЗÄ˼ʘўѦ\x97вϒƈżɯΫ\x99ʾɼƷʍϽǖʫΒɪĄʪŕȪ',
                                                                        },
                                                        {
                                                                            'key': 'TˌѡŌέ\xa0úԐѴиȣъƄш\xa0ŢҒȿŏϓяSȈɴЎӨÝӤ5Ѥ',
                                                                            'value': 'ʉIït ɬԔ~˞ΟɊүoǶʿG9!ÆƨλʱӌėͲ΅ȽĎ҄ç',
                                                                        },
                                                        {
                                                                            'key': '\u03816Ѱĥ¿δˆϑ¾\x8cŅĐͲʑðԬΝâч˔)ʟȅʉЉԍƠԎӁҠ',
                                                                            'value': 'чϫԁүŊŴ¸˙\x87ȘΦŚżĢǥ˷\x95ĻӬȠДуѻĤɀϰϨʨӳӎ',
                                                                        },
                                                        {
                                                                            'key': 'ɀɰǮӰГϟҰЖ@ɂ3ʆī',
                                                                            'value': '\x85җбƂ˃Ӟ6ϥʥ͵ƱƣіvмœǛɗʖʆԅɏŠʮѵkłDϷє',
                                                                        },
                                                    ],
                                    },
                            'comment': 'Ň½vɷȌơӐ.¢ͼ\x8aı¦ύҭʴȨǬ\u038dÒǑ\x8fɄΉѤԝƶӟǇƼ',
                        },
                    {
                            'keys': [
                                        'ΝϵԋʕҡǠ§Ƨ 7¾Φ\x9aõЌƙ˸эӿɘΈҭ',
                                        'ĝʒΧΏԆҩӱąDÞ¹Ùē\u038d˨˨Ʀ',
                                        'ň˶\xadʝԛ҂ԙńÞć',
                                        'ĘƬɃȖɥ7ωћŠȑɯӄcӐĻȽŢʯҳĴɉĻϮǽɅƚŊ.',
                                        'eʡėįKѢ',
                                    ],
                            'event': {
                                        'target_id': 'ΠԗǌϞΊʡȖgʄ˻ĉÉұg·΄ʅ\x8cϔ\x8eίӵԊ\x85ȽʹʸΈƞυ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ʫȆįϾÈҭ˱ɹɑŚЦKȒÕҬʺĬƮÖƺΡ\x9cѦŹϔǊӀĸ<ϧ',
                                                                            'value': 'üζ|ǚŒɱśƉĄɉɹŅƌҹȪȉÅШ\x90\x8dĆñêťЄƑԫЛѽԤ',
                                                                        },
                                                        {
                                                                            'key': 'ӌŨÞαȋƞҥĐϴΈȓĊĿɫ\u038bʯҡˡʫԮǟu3ċӨ*\x9bΓ¥D',
                                                                            'value': 'ǉʑ\xadOiϹƀΕÖƸāQǀâɭ©ѤӛϽӨɉ\xadζӣ˻ƀ\x9a҆ɠÐ',
                                                                        },
                                                        {
                                                                            'key': 'ѽΠҔͰŗïӪʈΣŒϙñ\x8dřɍ7ԤʣǡɴҼǄкÔԐџFИ΅æ',
                                                                            'value': 'çҜ˧˧Ǹѝϸ˳ʹǫРǀɍӂŧ\xa0ÑʷNĈƉϛʧ˟τ˃öɐ4к',
                                                                        },
                                                        {
                                                                            'key': 'ȸöēΧƐ˽ʁιʵϘżǣįʚҬͼŗ\xa0ϡԅϝīѹҸΑŔɅ',
                                                                            'value': "'ıʉȱĚ˘πʍÞ@тјӏҕ\x84ɗœ\x90яѸʊźҠӶɬwʘ*ˎƜ",
                                                                        },
                                                        {
                                                                            'key': 'ƂѵǎɅԏ´Ӳ\x9aɰ\u0383aϪЬҐƦƜюѥǃēȗȴŧ\x7fǶԕıë:~',
                                                                            'value': 'Έ*æѥȌԝǒ˳ÜßɮĢĕшƟӱ\x9eχƠĩӚūȃѧɱМΗİɜE',
                                                                        },
                                                        {
                                                                            'key': '!ʿǡʒ˨ύÏƧ2Бí²ʌϡî\x81Ûʾʼǥ¬ȏɞ',
                                                                            'value': 'pҾîɶõǉԧӗӝƱșӪЩĆǫnɳ҉ȆƋ»˨˚ЊѐǣуƔѕÅ',
                                                                        },
                                                        {
                                                                            'key': 'ϪЫyyɳ˖ǟXʢӫÿĕѢǿҲЀǽӞʇӸêƖМU˚ˆΏсͿ\x98',
                                                                            'value': 'Ӕ\u0379ӘɔȚӚ]˾¥iy£©âƗ\x95ʜ=˜ҩȔΘȋсðʰŊӟèΩ',
                                                                        },
                                                        {
                                                                            'key': 'ϏėӅ0ԒԫǅfȤγ˷zsӽȂǴŉĶËȋɳʆÊĿ˵˖ìƆ˩˃',
                                                                            'value': 'ɶӘśêŀʌƼÖȹЄƠѧΫ\x9dϠι\x83ŜǢΔĸέŝc{2ВӧŕĤ',
                                                                        },
                                                        {
                                                                            'key': 'ΠǥҿsîȆˬɣËˋŋ˼ɑŊɾ˷¢ѻƃȥ\x91ӶÙϘȃĢȹ\u0382ɤԅ',
                                                                            'value': 'ΗЁɦɺӎнÁԞůԊƯԂʋʢƅӉȍɀɬȋʵȝȥ\x95ӎ\x92^ϮжҢ',
                                                                        },
                                                        {
                                                                            'key': 'ȳɐʛӆ±Ä?Ǭɴ\x92ƾyˣʐϪĩ©ͶǀȔРŦɽЇZňȮѐѓΝ',
                                                                            'value': 'ѴōȸȹΝΆȌ_ƓҨǯ>ůȍŪѢ°ĜА\u0379eЇǂč×ʋдɤ˄Ϸ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ˮҰ˒K˜ǆԅϳΤɿ\x92˪ӠÕȺˀҀӌѱ6ǚ˵Ұ˗ƯÒ\u038dȪȠȬ',
                        },
                    {
                            'keys': [
                                        'èԇ\x93ZàcōӨʋÂöŷӻʧӍϥϸj\x98юȌʅӚČłϹ',
                                        'úǑҀŨˌҝŘˡ',
                                        'śÉЫϕУľîϱƀϽѨүãƠΒўгϣΠʋΰШȶŇĬɆŻĆƓâ',
                                        'ΩͳʃɬΖҗΊôyЀ˕Ɲ',
                                        'ĹɏӖzϖѯǫɔУ',
                                        'ɿ',
                                        '˘˝ҪÏʂϊѱi',
                                        'ԆƏŬӉÓуӍǢúnҘʠǠíˬƽԕƺӨζwӛҠԕ',
                                        'œ&',
                                    ],
                            'event': {
                                        'target_id': 'ѯϙϸϷoĎȕýWЛԢƢЕϐĵ\x96Ş\u0379ӨĽÔĿζºƻţɻ\x93ʻё',
                                        'parameters': [
                                                        {
                                                                            'key': 'ͼ\x93гѱҽʃƶİìĜʷŭĽǿЩêƇĭǭѕ¬Ʊή³ØѓϧӣҶɈ',
                                                                            'value': 'ƈȴūɲęʟǜс|ȿӬӈʉƸəīǮę\x96ȂŁȼБӟʇǝȥöƐţ',
                                                                        },
                                                        {
                                                                            'key': "ɤѼǛӹίʸҧæn\x89\x9d;žϱΖºʭӤ\xa0ē'бý˃ƶÞÅӈŊΫ",
                                                                            'value': "ʑӿ;ðQʛÏĚϪѯέ'\x8c˦¼ʬĕӕ\x95ȠŨѼƻϰĭǖ±αΚĊ",
                                                                        },
                                                        {
                                                                            'key': 'ΧȝιУΡΦӎΈԕǢƘŒȧίɀҦљȾЁȞǅύɭȹЦĲQȌuё',
                                                                            'value': 'ԉɝȀχϼÎ\\ЎǯŨÅЗӄӃҙŜʸҐćƼȵ˭ĊΔӳϧԋűѿƅ',
                                                                        },
                                                        {
                                                                            'key': 'ōѰίЦâ\u0380ıïшïȲǅǑЗƙƢӚʗȸˎԔΈ˳ìҁѤʞĈЌ]',
                                                                            'value': 'ʋԔҼŊеǃƧ˗ØδҏѕҼϟȠɤQ7ȅͰͶųȊϕ9\x96ƊƻëȖ',
                                                                        },
                                                        {
                                                                            'key': '\x82úѲԑНǪɄƐǢТȜƧʗϖӻҦÉÖԉ',
                                                                            'value': 'ǕҫΕώЃӖ\x9eØϊȿŜдÉԅӱʕŭФӱëɬѶwwǗɮЛΐĭJ',
                                                                        },
                                                        {
                                                                            'key': 'ȷŊ\u0379ԥ΄ŞŔǲǱļΥԡΗϏβǬҭβOΒǄԅ΄ȩiѪк}΅Ƣ',
                                                                            'value': 'ЋțŲȖľʬїįѥҁţ¯ԒԄʔЫњǄȖ½Ӎ\u0382ȖхŮӏїҕȥӲ',
                                                                        },
                                                        {
                                                                            'key': 'ԁӝҲԚӑ҄ʨ¼Ԯđ',
                                                                            'value': 'ӟɿĘƳʠ΅ХˬϦ³\x94ȣ҉ƽԚŅƄĩӌҤƛх7ȳ|ȩњɺŀԑ',
                                                                        },
                                                        {
                                                                            'key': 'čŚ\x94ψһϢӌɯàѸφҮԋɿœϫcҊПЛ\x9fɭʐĨ˞ȪҤ$ʒź',
                                                                            'value': 'ъκΛͿĢʸˠŸɄMРҭĸ}ʖϧΡϗ>ȸї»žҹĒѤȏӱ˚ζ',
                                                                        },
                                                        {
                                                                            'key': 'ϷӄƷ',
                                                                            'value': 'Ϩѫɼˮ˨ĚǸʠʇ˝¯ƨˎºϞϤЯ JǇ5ΦİĝÈ˩Ǔ\xa0Ęҭ',
                                                                        },
                                                        {
                                                                            'key': 'ҭńѭԬūѧϠёēɰɏÀƅ±ƎҺƄуԈAŬƹ҆ʣ,śʎϸ\x8cĺ',
                                                                            'value': 'Ő\u0381КԬӐѕѵӗ¨ʗɯˊчȻ]΄ÕИÂ\x90ɲOäǑ\u0383ӘЬҭǰЎ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'өӸ\u03a2ƢѷԒӹżϘƒːӤҲϹŻ˯ɯāKõ\u0380ǈӳӯȱʱĊůȮˠ',
                        },
                    {
                            'keys': [
                                        'ΜůͰӦ8ʜЭ\x91ӔòѨŘ\x96ɃЂʦɆѻ¯yµ',
                                        'Ҍ´Ɔɷɦԙ҆ԣņ+ſr×ѻȔ\u0383Х£ʚʖҢҰ',
                                    ],
                            'event': {
                                        'target_id': 'ȹΊĢØĻѹŢϦӥάʭɢԉˎŜǡƇ\x82ŜɱPzPЭыϟ҆Ԩɗ=',
                                        'parameters': [
                                                        {
                                                                            'key': 'ϜӸÍ\x93ɶ҉ȵDıLϤґбӧíԢǧçϓԦÊǤԡяĔѼƪȜŧӎ',
                                                                            'value': 'ɌКшɚ΄їӫ\xa0\x8cȊѧʔͱǊŎͽʫӇʿҎфζɱоˢ×\x8aДʭ\x9f',
                                                                        },
                                                        {
                                                                            'key': 'ԕžłɒԗǪʚ',
                                                                            'value': 'ƦǼȫН˼҄ĈъǋԏӢҋZ˸\x8fŭԥuЉϺ¶ƋИӱϯӔ»ȕ<Җ',
                                                                        },
                                                        {
                                                                            'key': '΅ǟśDϖΩŌɒŒ¬ǕǫǾ҅ØHɾʜ\x92ϦǾԖŵɦʮʹƙèӞȥ',
                                                                            'value': 'Ǿ˛ǭӗ$άƹσǹ$¤jɶ˭\u0382ɊԮѱóƥԦɖ˟҈ѢǩÂʂè\x85',
                                                                        },
                                                        {
                                                                            'key': 'ĉрćԃű8Ƃăǁӧѭ®#ɫƹ\x86ҺâΙшɰӃ˟Ӌƣƫɂe',
                                                                            'value': 'ӶơɢӤƐnȾпÆȨԍЙΣϯȌЫбÑµ¾ϗʗѱÛ;ɲÃMŽȴ',
                                                                        },
                                                        {
                                                                            'key': 'ζƭˋéʷũȟЭʯǲӶϘϕёˏ\x8cӹҐԠӥɛÏ˕əǡ"ѹϋtŜ',
                                                                            'value': 'gɃ˰ϫԘȖϑƥŖԫёʙ˷ǛяhƓΛǨӹɦЛŤѝ}ˬӹΉˌʰ',
                                                                        },
                                                        {
                                                                            'key': 'ηϻʊұæ-ϜŢԡЃŤ\u0382Ӂǥĉϳ«Ř',
                                                                            'value': 'άәқ˒_ȤѳɇȭԚƹ͵ţŋҽĊʛÐČ"φŌѵөuєΑɔҾĄ',
                                                                        },
                                                        {
                                                                            'key': 'fǡъaɢÈƼdЭӅZы˝ÊкPϜԍtʟЏ҈˟ӬТёϜɉΫų',
                                                                            'value': 'ɼчщÈϣ¯ǅû_ԐǬ\x8dŘƤ¸ȕѭvūͻ\u0383ĎԬȹɱЗʉКεў',
                                                                        },
                                                        {
                                                                            'key': 'ǟƋɃŃχО´ʒχőΊɑˣÛʛ˽ɞΨϾśînϓϥŜȸɶ΅ю»',
                                                                            'value': 'Ϣr=Ɵ\u0380ζƬϨˆԌӺʊǕҹʗȜƙέҲɸΡǗƫǼϖŭĹ҉\xadȀ',
                                                                        },
                                                        {
                                                                            'key': 'ÜĻŗћԧӒ÷Ϥфӟą×ЮǠʃ˷Фѽӈ\x91ӘʖűɓйΧŖɒ\\ǻ',
                                                                            'value': 'ҳϭuӏϜğХТƣť\u0383ŵ"λӳ\u038bЕ\x81ϡĩuŻȄŚƃ)Ӡ҇ÆÅ',
                                                                        },
                                                        {
                                                                            'key': '²ȏ˕ԉŋϩî¬*ΗȸČǴåҢƉĎIүƬӶ',
                                                                            'value': 'ҢƪʜώϰúџƇʇΆƈлпŦҐΊ\x9aо"\x9aԡΡ˖î¤ȼȚKŽ½',
                                                                        },
                                                    ],
                                    },
                            'comment': 'RΞęӗĘȔ§¹ʞϭŻĈθ\u0383ѣƐ]ηȪʂҦ\x82ȯN¸ʖɓΏϱ¸',
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
                    'ӹ',
                ],
                'bindings': [
                ],
            },

        },
    ),
]
