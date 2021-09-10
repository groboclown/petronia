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
            'key': 'eTԮǡĮ¤ʙǮɴԕԇλï3ɠưԡкxǑÐǡˎӠ',
            'value': 'ɏб|˧ј|ǗǇǱǧҫІӋƱĀĈʮɿƔЕǆԍgфʤшӛӠłì',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ԩ',

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
            'target_id': 'ūȻǶŜҳʍ=ÖҜNΥΧϗʓˁ-ѷұҏӭҖѭƄĀ¹¸ԚǑǑǺ',
            'parameters': [
                {
                    'key': 'ȷлІ°әɍҸӟԩ%Є˘ϑgÒQb¤ʨӞ|Ԑў $Ȕҁfƕè',
                    'value': 'ҕɊȗ˨Ĕ"ήĹǛӵЁΚȑίΩЉѴ˥ʗǹʙў˼ӑŒʭǅӘ\x97ˬ',
                },
                {
                    'key': 'ҧ1\x97лǐґƥǳϭ)\x98ɳŽӯ˾șжŻƾςˑ\x93Ł$ŜuͱŲʽǿ',
                    'value': 'Yӫ͵Ƣ\u0381ѳ\x8fPȌхɭß\x81ǼӂíɄќǱԇÒ\x9fӬѯԎҀ΄ϿÀh',
                },
                {
                    'key': 'ĠɢƼƕ˄Η˞ȷΠҶҨҰf`ѪÂо~ϯѩϏnɘmÖˈӤ~ӌɱ',
                    'value': 'ǽϰĄԝӵ=ș\u03a2ӮυȒԩɨЇţʁEBϔд²ȉѳҡʎɺǸǤΊΞ',
                },
                {
                    'key': 'ơĿʘ¼ˋŲ;ЃμɎ7Ʈщмȴf¦\x82ΡьɷôԔȋƐό˧˨o\x8d',
                    'value': 'ªйӌϔ˸øӾ)ȃɹŴŖϩ˗ɛӀɶцȹӭӌgdɆӇľʨŞrǖ',
                },
                {
                    'key': 'фхƓȚʇ\x90˂ˏǳɶƶяǯɪԒÐřĒđsċԢ\x98[ʖ²ʜӖÔʇ',
                    'value': 'Н˪əɔԈƱĺǇ?\u0382ņȮɿѨ;ɛёʵҌȌǋöHpѴɦÃѶЕЄ',
                },
                {
                    'key': 'ǓΦĜˁìǥĈ©eɽɊʃėkȗé˝āʂ)ĐԒƢϗ@ǫŷƊԖ¿',
                    'value': 'Є=¢оÁƊúś˧ѸɈҵɒɬǫMԟū\x9eĶƸǗʒȁǶȀƶʝʊ§',
                },
                {
                    'key': 'гǱͱ³ќǷѬϾѯΨɅʨѦӘÿɯǴžƃŰɰ\x8dΗQĚʑёˬПϲ',
                    'value': 'ŬǥпАɷǫǐƞϖ\x9aJȇNƶ¥ŉǛɝҡШчɯ',
                },
                {
                    'key': 'éɨυϳȺѰϮʖ5ʚȆͱƻʼȅƀƕΥͺɡĬµĊѦҴũϪÆӪß',
                    'value': "ǝŗԛǲǴ©ɉľƱҤԧоϻΑӯ҇҂˱ѓԧӽ˵ϪÖΟӾˇѹƠ'",
                },
                {
                    'key': 'Σƾb\x84ƬϼҾ\u0379ɥƗЏÁŐǘɿΨɖ\x83ĶǤεʡҭӤЌîԫ\xadǼΆ',
                    'value': 'ӂβЅ9ҩ1м~ҸВϯѸӤɈʳԞúɀ±χ\\ɈƼƍѝǪϫµ˔Κ',
                },
                {
                    'key': 'ťϮ¨ή<ȿԈƂԔǂеĺEƠąЍ˽ήȁŐ^ˌǨėϓԡΗǄƭȄ',
                    'value': 'џČϨs\x81ԙ[Ӄ{®ΚʗƤʑĲʎʔĹŞͱΚɢѢїӟʢқʲӫԪ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ήƀЁŚԂ',

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
                'PίМѳѵΥƵ9Cʻ˟&пȹ\x97ʅ\xadԧ\u0381τȞ[Ӳ¥=ӹɜ˩ˠ',
                'ȔÆЇҺω\u03a2π0ӟϛϖ\x95ċʰѥ¨ÑØѸåÛӷ½˕',
                'ΘɉɌƲЩЀŽҚͲɄн)ȔқơōΦȶЇɝņɴ\x93ʊѠÑҤɨˋ',
                'Ў',
                'ȘͺλƄǴȦԤχƬȄ¦ĦϲjҧʺǜԘπżÿ',
                'Φǫ"Ұ',
                'ϋ\x9aҖsɧːԞΩĚţГȃ',
                'ǕƔßRȆʏѢ',
                'ŁĠыӍǛӨ',
                '\u038bЪϤřyьШĮƈǞɃʠʏѸƶÝƼȊ~Qѡ˼н>Ï¸ɄķŭӰ',
            ],
            'event': {
                'target_id': 'ÒӪɛǷ˹ѢѕͶ\x98˫súьŅñϓнԛЂ˟΅ӖǑȊ įφȺSũ',
                'parameters': [
                    {
                            'key': 'ξʡ˲ѩΠʴήfʦĽĐ˅˞l˕Ź˂ÆԍR Ƭ\x98ʿӲԜȲяΐˀ',
                            'value': 'Ɣ҅ΈÝӻňϪƎŚĢԀsҳ˦ĭʝ«ʮ˧ҎyȩŒˢȞłɊǚβ«',
                        },
                    {
                            'key': 'ĩϐ¤Гҩ\x86ԌǃǔjČ\x8dʷěXРα/4ƕʩҪɿ¥^ƣσąɐσ',
                            'value': 'ҶӃфҐÜˍ\x99ҪѲɮԜϰѴǊˏǦ?Ƒ˩ʐȺɶʉǭˎӬҟͻ˪˶',
                        },
                    {
                            'key': 'ёÝȒĲȊ\u0378×ѧϓäĒˑɣǇʻʺҟʰΑXʠΘǵƺ\x8eϺԨƁbƲ',
                            'value': 'ƁɴԔѢŌЊšϒϓũŗʮȨæӆϐƋÐұʲӲӎηŰΎԛ\x8cQʺʂ',
                        },
                    {
                            'key': 'ҪϛĂџҼц͵ԋκʕ©ȏÄʛȠƘҡȾ\x87UёóȉÐҒĨƢʉ]я',
                            'value': 'ѽ¢ŔȏύűНŔìÂκД˅ҞǏɚƻ˖\x87гĐйŦ÷ʐјӃωΰĬ',
                        },
                    {
                            'key': 'ӒÐѡщыϒɷΞŔԢѾ\x80ʜźZ/ǊÃѢĮǆIðʯ҆ɒmÛҘƺ',
                            'value': 'οǟ5țΌԀȹɆϤσӻɯʃʀÊñƫĪ҂ʩќίjЛuԉžc\x84Ϋ',
                        },
                    {
                            'key': 'ϱӪĩͳΦűƥȝǗʹ ʿʞɫ˱ȉӞʈϫļγчʸȮɻŠ\u0381ĠёĽ',
                            'value': 'ґþʿģâҬňĞԖțԇaүƶЁϷʵȐʴΡøČǻȨ\u0383ҜҪ\x81ȼĝ',
                        },
                    {
                            'key': 'ƗЃмˇȨԭɣ·ēXȘДɆǬЮɫʍ¼\u0378ÂɼΓϫȲ˅\x96ɉȶϪʕ',
                            'value': 'ǆ϶ƧѡγǵΑɀĝӴҞþïɼҁƠҽϔ®ȚϤʶˀ¼ЎȒʷȠϾϩ',
                        },
                    {
                            'key': 'кǿYȀѵÖɍ#Ϻřѕ\u03a2ǿĮ˄ʘҷĆűòԧ8nÀ£ŁÍÌǸĕ',
                            'value': "ǆӂș˯НΘ\x8dȏͳќϑъϚўсΗ\x93˹ϞϺʇƹ'˹è\x8eɡǙƓŃ",
                        },
                    {
                            'key': 'ǊӍνԫñҗ\x96ėЦÜʿyϤþҮΝ\x99İӘɼʸśĉІȃ',
                            'value': 'ȝοȺΌӹʼѥƥҝμǟ˞Ǭϒ¥ώÝĉԕ˺bń\x99тéѻˁҝʭ)',
                        },
                    {
                            'key': '×\x83Ϩ#\u038b҉ӴĄäʏÕ˙ȦϯçӺ\u0383Ǩ\x91Äʸ\x87IѶǔ]1ӣp҇',
                            'value': '\x81ĐДĖѭŞίǌЀ¸˞Ɲòпņ?ΌɣЯԬɋѤPӚɡòԔãʧԭ',
                        },
                ],
            },
            'comment': 'Ĉ϶ʗʴѧôΰɮҒͱЌӆĮǅԐӪ˵ɻʿ˵ҫҏɞҜҲə&Ǩԭ\x81',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                '#',
            ],

            'event': {
                'target_id': 'ӵѣΝˁē',
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
                'Ȍ:ԕǬɶɣĠ°',
                'ŒĠȼҬʌV˲ҳȖƛØҍĚȄӄϞkĨѽȪ',
                'ˣɎâҚɶɦž˙Ƹa\x94^Φ\x7fԂʅһ˚˩ĊɌƢҼз',
                'ǋVЖ˙|ȏƺёӅԇɷ',
                'ȻҬʪѵˮ\u038bÑïԟ˖CˍŊɕ˝Aӻґ',
                '˵\x94ɯŞʮHĺt#ˣϻɐӣ˞ĨΣǂɋΙԪ',
                'ѷŉБƍ\x84ȽɉҔsɈ%ɋҼɳǟǮ',
                'ґˢʩϋɰǠӁʇѶȂǍDŌ¢ЦɆɃ\x91иԪκĵԂɫºƐƔóŒö',
                '!Ťʼϒ',
                'ˌdxȡʶ\x91ӇӄįĦɫ\x84ƂІǉĴіǯҞÆЂțΞœԊȶԫŉӓӖ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ԉĵϘƸĭԃɤҾͺ7˕Ȣ˺ƓδȸϙĜðɀlʝҥ',
                            'ӾθԦĐԦĽΡǰ',
                            'õԞӧñԪéϑʀя',
                            'ˍˠҽѬ$ҰƦoȡѓΛԅʊbʥƝðʾεÉԅʳӏȎƤǸŌȵрӇ',
                            'γùǔłȠȝǼ˵',
                            'пÙƕͿ',
                            '˲ҍƬȈU@žΫXӰӡMĒʀȷϛĻϭƾӻȾ\x84˸ŵ',
                            'Ő@ΜСȐc\u0378ƽ\x9b',
                            'ʏQªѠƵѵĲƭ¶тʹǏаJȄÄɇюѩ˖i˽ӴΕЍԔΈѐ',
                            'ʧôȍǿKđŸǄ',
                        ],
                    'event': {
                            'target_id': 'аĂκťʗϏ\u0378ƬǦVВ·Ӱ˨¬ӗȨïɇҁ˴ԂƺʄгǏǗδŘȑ',
                            'parameters': [
                                        {
                                                        'key': 'ЊʫΒʺσĒ\x9bǇΕˁøǡ<ǥ ɴTÇԊϖԙİ҅«ҶȘʰWĒb',
                                                        'value': '\x8fnԞʇЊϠ҇ӥƪǈʠǯʳЫ˷рѮ϶ӘŌʟЋҼ˂ȱѱҦԄЁʫ',
                                                    },
                                        {
                                                        'key': 'Ȟ\x99Μɀóǉɜψłʅ\u0383ɮȮԡưgɥƚ¼ȪɬѽӒΣчТ\x8dћњΡ',
                                                        'value': 'ԩ˼ӌϰԃҚʔӰԕȏȯƣќϩT˅¡ŌĻӯ]ˣʲ҃²\x93ӻтԡП',
                                                    },
                                        {
                                                        'key': 'Ù\xa0\x90ҬΙѲɷİɓčɣ\x8aʇТŎΨŤǀ',
                                                        'value': 'ɹӻӠӂúњӹϰɱǨÉqˉÈÓěϤҽ~ɺΏǰЛɃӴƴÊć¾ǡ',
                                                    },
                                        {
                                                        'key': 'Ü\x86ÔşªƿȼӤǹԆԝǽϠҫʈԠȟϰ"ίԕÛНȢϋƇóŵζß',
                                                        'value': 'ǩê˨ÉŅǛѤǗФϰҋΰȠÝЎϡӯŅϝ3ȓʨą\x8dǀ¤ǰЄɈ"',
                                                    },
                                        {
                                                        'key': 'ӾїϲԛƔц\xa0ҘɌSƽ˖ɁРƁʊÏōŐYΝčԏӜТʍԖĦDХ',
                                                        'value': '\u038bȇƢƀӅǿϬÞЛǿԪɳˁԠ´ɋНѓɫдÍsɹϪӈĈʜŃΑƾ',
                                                    },
                                        {
                                                        'key': 'ĤЉȆɬʊҦМɦӹ',
                                                        'value': 'ҫSĿΉɱҋӴҍôʾZSŶτӳԋʺϛĩǥ˚Ĝ;Юèɤϒǐ§ӊ',
                                                    },
                                        {
                                                        'key': 'ʹŌϻɟȏԌ҉ɏ¶ʝЊ\x8eʴˍѣљьȉуǿˉΘŰеЇƖƜњʕʋ',
                                                        'value': 'ɤŕżɡ"ěёȾԜ¸ʑʶȝιĨȽԤˬǛțŐ҉ȼĴʨӃɌɳЖͰ',
                                                    },
                                        {
                                                        'key': 'ӵEňǁϱȯvMɔŀ¤ҭԨʙјȸЙԞğŗӸʦԥªмδч˱ūï',
                                                        'value': '\x81ǐˏоνϟĚĢѲӹԣЙЭžΡſγʵO˭ԩÉϕѵҽǟƪŸĪЄ',
                                                    },
                                        {
                                                        'key': 'ǲɿάǸЏғʾʿˎÅ²ӍʪƿɻŰƺӌʹdҋӼҞω\x82ϺҽƜǇɝ',
                                                        'value': 'зԄ}ĽƋŝÓȿӣϡӥƫћ³΅Ҟѡ·епԂώяēϸɉʴ \u0378ʧ',
                                                    },
                                        {
                                                        'key': '\u038bґγԦÆ˕\x7f\x80өԘΠϰϴӟ\x94ȂʼЭŬɀ¾ɩӺȇbҁʫΠǵŃ',
                                                        'value': 'ˢɯϸȷũ7ʘέƜЩZȹŦIƇшыǪ[ȩŘɸÀӘŇɩĬ˃Ɛʄ',
                                                    },
                                    ],
                        },
                    'comment': 'èǟҤϛÓƨʌσΊ¸Ǵùǡοїţˇʽļ\xadȎѻȎĜAϳѱӘˬ\x89',
                },
                {
                    'keys': [
                            "δϋʉř!κӥ&\x97ȝѿ%Ĝ΄ØƣѱβԨŉΜϺȺ'5àɆΠ",
                            '˨ҌԬȾŴӰģəëѝҫǩŎҊζԇçώŚȚüƺ',
                            '¶',
                            'ҨÖŒ',
                        ],
                    'event': {
                            'target_id': 'clψďЉ´ƎŠъʱļэ˥\xadҐŃõЀϕÏҊȽjȜÕϵhĽη³',
                            'parameters': [
                                        {
                                                        'key': 'ѦȯεԜҮԋұѯҔƁ˒ƺщӜғőˮͰY¾ҀљųЊӱuԝӡќę',
                                                        'value': 'ȺЪҦτɪ-Δɦ˄ϊ÷ФèƵĹƃœǰŀĭĪǹˈҙHѮǡʿƏö',
                                                    },
                                        {
                                                        'key': 'ǞªѫkϭUԍφ҃ʙʬЊАɦǂƊpԁęȃǰЅӋӣԓŔҫJХƣ',
                                                        'value': 'ˊƊƜόŵǌšƳĪɆӰ¿ĥʋ˵ʎơͲӷņʍҜʛʒңӾǋϾгҩ',
                                                    },
                                        {
                                                        'key': 'ǕʶčpϓΪ˲XƷʁѲĺԄѕ{¤\x9f©e±\x81ԪԓНЍϚĪвѐɔ',
                                                        'value': 'Ϥć{Ô`ʏÜs\u03a2Ӹʴͳ҉\u038d˟ьͿ\u03a2\u038dǖÅϡǑ\x88҂ˁЛ˴ӖӅ',
                                                    },
                                        {
                                                        'key': "ΛɛӔ^¤ƜқƲüɍӳˋ˖'ß¡ďKȨӺσʏ¦Ңé¯Í»ɐχ",
                                                        'value': '®ŘǺˉǯÝȱɍĨǹã\x87ÉԞǞќєʖɥƔʥπĊϿƛүèʕJӪ',
                                                    },
                                        {
                                                        'key': 'įǉȉǁƫ×ˏΚ˙ɇ=Úώϫ9ӮУѼ',
                                                        'value': 'ΖÎŷηǇӀӽбî˽ËϮͼбϊQŪȎbÂӊєќҕɖ;ο¢ĳʟ',
                                                    },
                                        {
                                                        'key': 'ͱГԆҜlzŗƍХԌȍˀ',
                                                        'value': 'ƌbѠŶǗȻϯůƞˣȏԀòӪĲӏ˨\x8bӡͱƙƌʗРHǭћAũɣ',
                                                    },
                                        {
                                                        'key': 'ΨźѥԇʑåÁCԭÛƉʚǵγĤ˟íģԡѐɆȭɠѸʧƋĐђыŭ',
                                                        'value': 'ӄӼȮȪ©ƈȷŘѺ:ԎϩХĮɷĉȖçκ\x95Ƹôf{ƍǹ˯ǝʫƦ',
                                                    },
                                        {
                                                        'key': 'ҲϽǵľǓĭıǫȬȈʸĻRϼȅʢ\x93ϻąȝеȊQǡ§\\ҕɃ\x85Ϳ',
                                                        'value': 'ӒϋąʭԢϝ˅÷\x8eȍÃƵӱѫͱый˰ԟαϙэҼǁѤΊɮԡĴҠ',
                                                    },
                                        {
                                                        'key': 'їªҾÏ˺΄ĞƫŴƣϡӠƹɁӅJǐùɜй',
                                                        'value': 'ǅҋǥĚФŔŮ1NӚғӝɧϥǹsԇǮҀΙх\x8e\x85ʾɱƁˊ·ԮÐ',
                                                    },
                                        {
                                                        'key': '&ĥJ³Ψʗ˳ĄʳʅѪӮй*ҶƿŌŢǵҲʄѿӳĲnɚċѫ;ˤ',
                                                        'value': 'АһҾñƛǲ˾ĔʽʉłаTʀҴ˖ȐŪçĥźѷʂӌƣĖÅӹїͲ',
                                                    },
                                    ],
                        },
                    'comment': 'ӣυϺ˜āɐӔďӽɚά\x9fΟɎĐɂƬ[ŎǡǢǟ\x80ǗсȔŅɑƪλ',
                },
                {
                    'keys': [
                            'ζѝ϶уS?ƶ\u0380WΤ<ĵǷ·ĳãĉіѿҹ',
                            'ҊɤɤȣљΐӪǰ2яԏɦϐJ',
                            'ɄȼϦҹJŵ',
                            '{§ĐȻĪǞȩîίɍ˩ӹǿȘҥǖ҉;·ʶÑ(ǥҷ*τǴƗϒ',
                            'ǟþĮʰо',
                            'ҝҴКʨӲϩĳҜſб',
                            'IȯΌǎˍąȡΪθłɠĶ¸ñģȁίԗî',
                            'ƈì\x9eřΜβȒ',
                            'ԡѾVӔѽƮШǕƼȧĵĨoǳ\u0383oˬ˵ӷϣӖҦ¢£Ɉƒ',
                            'ҦĎӂśԧ\x89ɑζȊπǌŎԦΑѼ҉±Łǿĵ',
                        ],
                    'event': {
                            'target_id': 'tʦʸʘǤķĻРìҡԝyˀ\x95ʇśEŗњҥԄʎʸӣǲЪϨ\x86Nƈ',
                            'parameters': [
                                        {
                                                        'key': 'ȠϹԔWкǣŸŎӌɤǪӾȫҞԤͲӬьϪπˊ\x9dӼӃĆөũϓςm',
                                                        'value': 'џå²Ϋҩǻą\u0383ѳćĿδԡŬґ=\x94ǧŇƞÜëӴ˛ˌȬEöÒb',
                                                    },
                                        {
                                                        'key': "ЃЖ'ǒύ˄īȡ?ӭ£(ȹǫŤѤɣĩΟΉӰƝԎӰѧΓğеϞō",
                                                        'value': 'Х˓ǫǁǔ\u03a2ʭŦ˙ɋʃƴʸ<ʃҲӅҴб»Đ$ʂԁ˝ѯЉɶƖҿ',
                                                    },
                                        {
                                                        'key': 'ǵcʹɬѾÍ¤ԑƨęϋȆȥϧƐǯįIÁǡJƀ҅ϙӟ҂ΣǸ¬ξ',
                                                        'value': 'äɞxϲԦǝ«˚ρʫѷϠӈPҚXːŔҽŪÔ¸¨\u03a2ҢƾÒԅҶΗ',
                                                    },
                                        {
                                                        'key': 'τȴΟ˾ϼҚɑıΙʩTϿÝʬǙˮβҀ҉ѳϏǽȋƙəːӵӜɤ)',
                                                        'value': '=ˣͻˡɢƷѸс±џҎǝºŮҢǒ\x8bĭЙßԛѸʶƬőŭϛ¹Ʀ\xa0',
                                                    },
                                        {
                                                        'key': 'Đ\x99ȥѣӅţƻΑǇ\x89œԛgʡʔǮĦmĻ˘_œĮҟЎȀŏƂЯӣ',
                                                        'value': '˸ƕR®Ɂ\x86˗Ʒǖšªǜ\x9fʃŅңƋϏԎрЏʫкәԦǽχÓҁҌ',
                                                    },
                                        {
                                                        'key': 'ʥϹ҄>CԛбʩϣǻƲʋϝҶŒǎ˯ʠćʋ»Əιǈ\x9cŤ҄óʗғ',
                                                        'value': 'ŧдÉõ\u0379kҒlÕ4:ϩȄΓǧΙƲʯήϝПɫ\x80ɤˁӅѯǕӺh',
                                                    },
                                        {
                                                        'key': 'ыȴ\u038dİҶʍƽ˜УŚμʰСҚŶӤċӰȱϲɭÂ\u0380ɨϫȋáԚȯŜ',
                                                        'value': '»ηѪǟˈǪIρĐ\x86ѯƫХǸ-ҾԢĂŇƢϤͳÂļǊԬƱÙ\x85ʫ',
                                                    },
                                        {
                                                        'key': 'ѧӚ˩ƦƏ¨ÇϡθȆ˵.ͼmάЄĀȽ\xa0ˇάВɖɰӶƃͻǺƣΕ',
                                                        'value': '˗ɱϊǒ˄ӾэӋżѾЭ`ɵ҆ҴэɃķvŖĽ˲πА\x9c\x92λƦԙ¶',
                                                    },
                                        {
                                                        'key': 'ФώŊȒʹľӆл¯ˊЄȓȜCʼWÙԆȋŊ&ӮϿϸŬҁ:ƯɮǤ',
                                                        'value': 'Ơʋ\x88ȳҤĸˑü\x92brȌҼ{ɟǸʭЫĩ˸ӧќ·ˢҟˈɭȧΫǱ',
                                                    },
                                        {
                                                        'key': 'ȆϵӳǇԡǷɼʶԩȟ˴шδԆӬɧӡΙ&ӑĳƼƸфȩ˸ΨœԆű',
                                                        'value': 'ԖƌđЃζ˔.é´\u03a21Ҵҕ˚Ɨʯ®Шω^J˫»νĺ!Þ\x87ń©',
                                                    },
                                    ],
                        },
                    'comment': 'ǒ˦ǁȂʔЏˑ0ÞӘř˞ђ·OҌҟԞώȲϸ˴˯ΕжǨȎȹéҢ',
                },
                {
                    'keys': [
                            'цɘрԊ¡\x81Ȏưŝ',
                            'ƎͺƜԅԜǷѐӳӇhԬ|ėÃӵŃЏǜƥ³Ʈ\x80ǀϽŪӢώǜΞ',
                            '\x9aΫrΡΚ˔ƺʞʃ`ҢԔЃЍʍϜŧЃ0ȼȐҗЮη&Ӱ˃şɘĪ',
                            'é\x8e͵ѢϚӪ˙Ѭкľɣ',
                            'đњЋʸӉƩ˦Ҥ˻ЀǾϯζ',
                            'ѝųʡ˨ğЪɧҊѯúȶȺϡӜÊɗ',
                            'ʝч6҄яѾȝˁƘҵ9\x7fĻӛψɮҭˠŹʀ',
                            '˔ɮ\x83ӌÈɛ\x82άтȠuť§\x9eʛїǩгЯɨ˔ǭè\x88і˝Ή҅',
                            'ϮʂȗͲϥѴР',
                            'ƛ\x92ƿǎҜάsӔ˸ƊЈӢǍӺʞlыƪєoĹɧ',
                        ],
                    'event': {
                            'target_id': 'άȰԬ¦фčГѮȩĠ҈ʲЏ\u0379ѠŉĒȱǱ˂œӇDϔηϒ-˵ҧΛ',
                            'parameters': [
                                        {
                                                        'key': "¾˭ÎҷʭOȤΆǩǩ,9\x9cξҺŘϓĽIѪԙʂШȀáӬҏ'QԆ",
                                                        'value': 'òихŭĪξġԈȦɴkǱ6ӹǒʎҏԭВŻƆÇԌӮ´ґΗʿrȚ',
                                                    },
                                        {
                                                        'key': 'ȯɎVʀѢIΠї΅Ɋ¶Ѧ¶ϗǲӤˡϦÖѩӭԌŭЮАШʡʼ?ɒ',
                                                        'value': 'ĜΙĔÝːԫѝ@ī\x92ҐǴӧ\u0383ԥ҂ʝʤȅ˲ˏ¤Ĥ˙ҁЊě҇ѵҥ',
                                                    },
                                        {
                                                        'key': '\x98сϬȵΌǦѴɈRÃƬӤ»ĮҚɅχȥ\x8c',
                                                        'value': 'ûȩɠǬʊƼ˘\x8fǃ˯ΑʹԪϨΆѺɠDƊǂɨn0.әԄϋ\x91ɰǾ',
                                                    },
                                        {
                                                        'key': 'ѓϮφŐЩǹɇ',
                                                        'value': 'Ȑŵʜζо-¤Y\x91ηͱMЫԪǇòɑÙő£\\òдŪԢϽɉӮҒí',
                                                    },
                                        {
                                                        'key': 'ѭѹθÛгŇJӢǾϛ˳Ӽєňѐ¶НǽѷЏԊɡЅɬğɝþđR\x97',
                                                        'value': 'ΰàίϙϤҊϣ:Ή˭ǍŕϢěȩͰġƎȰȰч҅@ŽȞǝĹνːp',
                                                    },
                                        {
                                                        'key': 'ѧҶǔҀİɖĂЁʞǳȻЁȱϜʍҴҗƚцЊǫɦȚŉïҎӃĳӀZ',
                                                        'value': 'gΫQƉͶ϶ҁҗˑМÞКǃ¹Ɨ\u0378öӊфѳÃ˕±ƄȻȰԏʰҴӍ',
                                                    },
                                        {
                                                        'key': '҉',
                                                        'value': 'ÁɷǧQǠҟ"ӊǏΓĊƕԭ\x9eΜŀѓǑĩΤɇɳэȀƢŽǚhģń',
                                                    },
                                        {
                                                        'key': 'ǞѶҊŧһ˺ҵȹϦӖҟ',
                                                        'value': 'ǳȉɃĞӛȒ2ƒĪͿĶȧѓΌˬşђЂiʂǤʐ¢ύˈԐҮEȖú',
                                                    },
                                        {
                                                        'key': 'ʱδӴqɑȵѦĈΖ!Ĝ>Жώ¬6ӚǀNΎƨƐ\x88ˉӧМ¡Кȿ8',
                                                        'value': 'ѹ¯\x83ˊƳɎ2¢ǍȰŲϵȶ\u0380ˤĂ\x86\x80εIȺͰƔɕӣΞӦϗ\x9dҊ',
                                                    },
                                        {
                                                        'key': 'СɿʾĠȡʘөѵɶʨȾñ*ʣǶӂ6Δ\x9aҟϳϊĿѠāŸԇĸͽĨ',
                                                        'value': 'G\x9bϏ/\u0379ΥͶGμ)ϳ˯ɠШǻÑŋԂ\x97ҁ\x83Ưʨ\x9cњʐ9ɭúȲ',
                                                    },
                                    ],
                        },
                    'comment': 'ʘβàϘӏόǺøȣѓϦľȴԥȩ.ӽǑ҈ҷ϶ǼĐúÝіÐşƬӦ',
                },
                {
                    'keys': [
                            'üǏˢ=ģȩȯ\u03a2σ϶˷m\x96+ɰԅĊԟƫǩûȨȸȴԋʤөĺϵ',
                            'ʭυ҂ȳσѴϬˎӚɛӰфĶӗ\\đľʤӫĽυȂ',
                            'õƺΠˀ\xadǎШεǕčɫƁŪԕƤϡЗʪɻãțЪϥϮÏɛ¼',
                            'ȴđʎŔϹѕёĶʳ²ƱҸĄˍ˫ʳԠ˅ĬӶ',
                            'Ӑƛǡ˙ƷɲƓ',
                            'ýʯ¹ϝϣȸɚƳϵF#ǘͽɯϲ҅²Ъј',
                            'зζѸЁӊѽĒȴǐʰă²ҚƌɅŠ',
                            'ԄЊѶԚ˪ɺԡњљԚϷɑҁʷжѢ',
                            'яԣpʑEӴу҈эβǄҾȐòӀÉ',
                            'Τ',
                        ],
                    'event': {
                            'target_id': 'āĜę˓ӺĶÌЈӍǷДŽxʨÏǹϡϬ`ɈԨʆAȾđҺRԤƌÕ',
                            'parameters': [
                                        {
                                                        'key': 'ƳɡưŉˌʿÙπԜӎʣԋPӵӤȓƀ˚ɛӇђϜƬμЦɫҢɠǺј',
                                                        'value': '˺ëˉƓŜɀÈɨϫ˵ƹҨӌ\u0383\x8e˹Ӟϻ·¹Î҇ηĶԦʕºΩӾŘ',
                                                    },
                                        {
                                                        'key': 'ƋКī˕F\u03a2˪όЃȀʵԊ˚ƘêʾӉ>ɫΕʗǤӮʅýәҨʞҟϟ',
                                                        'value': 'Ɠ\x97ӠҸɁхβǝʖtϺӦҊ˨ǡ¹àȝǤǩƩӮɨύԔΛmȑ˰Ѓ',
                                                    },
                                        {
                                                        'key': 'ƘӲϛȍ˺ʩ&ˉĬ',
                                                        'value': 'ƵʘйˬΒқrĠиȞʤǞйɢӧ+ΣžӾſÙΠųѓǃʜȀӨϑѿ',
                                                    },
                                        {
                                                        'key': 'ΫìɲȲ\x9dŢȚ˯ʕЎ\x9dơÆӵЩъӀŅƓӥђņЎϭǃǫôːǙʷ',
                                                        'value': '\x87)ʿͼ]Ǣȓô\x96ѯьӪÓ\x9eǍӅ˦ģ6Ķy˸\x7faŞЗ\x96˭Ǫʗ',
                                                    },
                                        {
                                                        'key': 'ɑäϘ˙¤ȨΘŻѹˊȌϲ;ҳʉХ§҄ɳԣÙǃ\x9bϘȡæ˹ƟΑӌ',
                                                        'value': 'AĤŕιѺ˙ʟΕѶʜʄæƞ ӖɲN˽ҒɈԀΝөȢƵ\u038bĠҌƖˣ',
                                                    },
                                        {
                                                        'key': 'ϔϒΡҍǭÍəF\xa0\xa0ıԡ\x81ΰϬωаКϪжЂŸ˃ĭѬβʧȒ˱я',
                                                        'value': 'Вßȣ\x9cҪŠŜ3ŪəǜѓϥhɓʺӝŉˌˌÝϧɔχͰęōȉӶѯ',
                                                    },
                                        {
                                                        'key': 'Ҋøĝѽ·ԩƅʰ{҃˪ʼǛ©ϋɇƀӹʹʎˮз\x9dΗġşйϒƨҜ',
                                                        'value': 'ԭԁǽ¡ѕɣΒʙΏŰőmҌ\x92yőɼlӺȭʚаÊсàŰƞ˲fǵ',
                                                    },
                                        {
                                                        'key': 'ӔˑBĵIңѫ>҆âΈ\x80ӑԐϋҬɾѢɯʘĦ\xadǣRԈҍ˼ǌƀɳ',
                                                        'value': 'Rΰɤ˅ЇɪЬЍ˖ӘғŧѻɁÇʰțυяНĠҜԍ*ƅ²ϰӑϕȊ',
                                                    },
                                        {
                                                        'key': "ԈYŋƚʮϙÍБʯԬԏĵqϫλҊÄҋϧʫ'ǫƥĘœҌ@ˠώӻ",
                                                        'value': 'ʺĉľϭϪɭԢɍӼďÔѲŕǃλӛԄҬϸPȰ˨ô˟Ĭӑĭ0Љ\x98',
                                                    },
                                        {
                                                        'key': 'ĳÏѺȌƴ´ǳǟȢʢšŃԋq҇ȍĈΥ',
                                                        'value': 'ìɸưϖ˗ͲːяȨѰɱϻʲ\u038dǻˁǟԏӪȦMȓķĬɟԂŪЫ˂Ң',
                                                    },
                                    ],
                        },
                    'comment': '±ś\x9fŻħɣӟǏʃщгɯɱԆҳϹϒÔͲQlɬĭ\x8dâϽҐſǾƯ',
                },
                {
                    'keys': [
                            '´ʄ҅Ĭɾâ˳ſӻʈj«\x96ǶZϧƈԘʉ',
                            'ΓɃǁɳħȴԛȠʺ¶ұ®ƮÛϦ\\ʅ҈ȼӇЦұʔѡΙ9ƂҴƧʟ',
                            'Ψɖԇ\x80ŴƝ\x95ѸѾ˂ȽԄɳˆ',
                            'ϱҽǒ8ɘėĨи',
                            'ƖȋҚř]B˷\x97ƹ\u0378Ѷɿҝ˦њD',
                            '˷ĞɺҙƩɶ£ԏɟШUӏƭc@Ϥʹѷěӯ϶ŝθșǀИĤЋ˗<',
                            'ɫǲɣҍȥĽºѡƝͻǣÑϫǓ\x97άư\x8b\x94ϴ˒ƮřЈǙºҁƉ',
                            '\x83/ƎȪӛŷɨ',
                            '!Ԏ|СЈøǠѓ',
                            '\x8bɐϪԍɠ͵ӅʩČŵ·ѳЙ˕ӥԁoȘ˽ДпҐӫЉ5l˫\x8e_Ř',
                        ],
                    'event': {
                            'target_id': 'ΫΎ˨ĬȑӻʡȿΣ\x9e4¸\x97ħKʍɒŮǡʗʨˡ|îӟлӾȯʭɤ',
                            'parameters': [
                                        {
                                                        'key': "Ƚǳϊ˰ÝУӐıvʸвǫ'Ŧ\x82ͱӖ.ʋӠɨǷɛäҔӪΒʹмȢ",
                                                        'value': '˷®ҵӺϖIʹĹʹͰѦ\x89ѬԦưÅȉƓđͱćӛΩ˗LǰІÜʂː',
                                                    },
                                        {
                                                        'key': 'śʄʶƪǈ¨uѥɀɒuΏɣÂǞĄnƷɝȾӅ˹ө2',
                                                        'value': 'ȐƀǠǢʴ\x9fɑȔҿãťӶ΄ΛǉĮõǙɴ˗ĉҹ˟ԙȊӄϜӱŎǩ',
                                                    },
                                        {
                                                        'key': 'ϚǵѿŲĘўʝԏ',
                                                        'value': 'ШЭ˘ȗʤίɊ\x84ʖҠɤν¥2ϋŶӔåҔŲƧ<ј҅óɶԬϬ¦Ԃ',
                                                    },
                                        {
                                                        'key': 'GҡŤ\x9cʌуʋǆџǜПʭȓ҆ɹé|ΆєӴʘќ\x96ǨƴʳèʁʹŸ',
                                                        'value': 'рΏbʜʼɜĶӘ¸µӷԂȒӢԨЪ<ǾƥdΙѼȀЏ¯ѩ\u0378ԠӛǗ',
                                                    },
                                        {
                                                        'key': 'ƷͱIɂ$²ӆԡǿțĊЛȮԓzʁ8é˘ƛҷŧͰ˵$ʘѪϜsӶ',
                                                        'value': 'ʈÊѤĸ҆ΐӱȬϑϭϒɇιϠ˞țɴɸΚǤʎʚͰ\x82ě\x81ʲƲƽƅ',
                                                    },
                                        {
                                                        'key': "ĲѧȩǬӷ˥ȁɎĪãǁѵǝŎȮӱɘȑѲkӌ˖ĉŜўсÞ˼ȡ'",
                                                        'value': 'ÅΡʭʖΙķɪЕȠ|ʇЗƐӠđŎ4τŌſĈ҅ҤÊHȄîʛϤѬ',
                                                    },
                                        {
                                                        'key': '-ˬΩƸюԊĪѴҮýȰķő˵ʋʣΕȀǅӭ˅ʺĬǛȠȶ˶ï:˖',
                                                        'value': 'ҒӷҦӜҭϔәҗŤГŋ΄ϓʯӛüƙȲʀŃϞÙȿͽаȽƁϞȖҞ',
                                                    },
                                        {
                                                        'key': '\u0381{ҚʪԎѢҐȎƪ!ɅƕԞzϩδˉѡÍИ²ǆāœӵ\x9fϊ\x968Ȟ',
                                                        'value': 'ҮɯрӓǸƃĥȄʽŌʵх˨ô¨ȅыԅžЇżʙеɽКȥǷӈƙɦ',
                                                    },
                                        {
                                                        'key': 'ɇɵTØɏӈƇǄ(ǸƈӠξF)ɅѧѸѼƘȜӘԍ±ɩƢԌ\u0378˂v',
                                                        'value': 'ΠӬтȞѴŌЊζūȑɝ\x8cӷѴˊ;ŻѓɁ&{ͼȎƠhʫƛȳӀɵ',
                                                    },
                                        {
                                                        'key': 'ƘÞǄ˼ȯǓǓʰÌҬʇɃɏοϽjƲʎϓȼэŃӹʀ»ʿĹbǦƺ',
                                                        'value': 'ĐʨɋԨлΦΌ\x85ˬƔϺГʲĨϾƘȻ˂ŒīǙԟΟŃјӓйDǉŒ',
                                                    },
                                    ],
                        },
                    'comment': 'ĘõԥýΦȡ\u038bǘήčʼΠфʷ\u0383ϟŖŹήƉ\x84ǼʺpǫȐeүɟѢ',
                },
                {
                    'keys': [
                            'ϮĨɏћȁ\x90ɦǺƇϼğǷӣ˥ñÝȤƝԬ҈',
                            'ȡº˥ѹԨӝcɼ˨ϟǚѲĢӯ',
                            '\x7f϶ϳŲΆņӼȴϋӓ\x96ǝ˸âfȘΐˀłʯC',
                            'ȄȍϏͽDƞͲҁÚǍѨѷͺΛˮӁê',
                            'ʔѷˡǌËǏԆϗԐ\x8aˇŰ¼ŒˆħԦ',
                            'ԣɨǧǧǞ\u038dāɦӫԃALŴƁqΞїżÞљĩĂϦϠΛȜ҇',
                            '˭ȪηўͿ\x86ɻϫǙɐūЖÈόɴɴЄɻ',
                        ],
                    'event': {
                            'target_id': 'ӦΆӗ"хӧĽ¼Ҋӧ\xadҝ҆\u0383ЪўѲВѦԅ*ĊΤǨ\x8a\xa0ұƖҿӎ',
                            'parameters': [
                                        {
                                                        'key': 'ˠҽƙ',
                                                        'value': ' őǀƸαƁӛҥǇţрÇçӝĂ)ŏԓӃÁѬùŠÇΑЯƫΜpĶ',
                                                    },
                                        {
                                                        'key': 'ȉԓł\x94ĖДȹӉҝɻϤǬν,Xå˺ǹҏěȜГӭıb*Ȁkʀ?',
                                                        'value': 'ÍΘĄԊԌΞȨȂÁўƞɪѨҥį˰˜ĽǡƤ˯í4Вϭ½ƚуRƵ',
                                                    },
                                        {
                                                        'key': 'ӨŭŸ\x7fȼúҶƺƵàԋϷı~ΞҤŘ˼ĎŵǩԩӅĠɏ˰ȏԍыȱ',
                                                        'value': 'ȶŚʿϪƷRҐƉǖâŭ\x95ʷǿӺҀMп©Ѝ¨ůέѴȵЯЪĹƢҤ',
                                                    },
                                        {
                                                        'key': 'ҘӋӴɼĴзɡѹϏ®ӎԎǭӑȂǲŝɁoԅ˷ӔќӺǋƉҮ\x94ƪ¾',
                                                        'value': 'ԠеҲӨϦī-ŪΖѭΟÑтϝѝüƷӻҬͳŤҔИ\x9bρƓЃҝӦ\x95',
                                                    },
                                        {
                                                        'key': 'ӑȿϺÆΐ',
                                                        'value': 'ΔìģσԌӒ˧ǝƪӥϾɯʏυåȦ\x8cƴǸї\x9eĦŌÑϊ\u0379ÐɹΈû',
                                                    },
                                        {
                                                        'key': 'ΧGľƾőӇǖқʂÓԉȾȼпѝУӢӣƕʯƴĵóҠ°ҞȪŽǥԋ',
                                                        'value': 'ԍЎOȮʿSŢԇʬҭѣϏʭȄ\x98ĔǚơõҼӥҶʹɭ˕jҡ/ԠƗ',
                                                    },
                                        {
                                                        'key': 'ÑѐȱӑʫύȊʾŻƿ,Ĝ',
                                                        'value': 'ƠźЁēď×аШӛϬʄѸR\u038d4\x84GȑώӘÍʆõªѨԍǹ$,Ь',
                                                    },
                                        {
                                                        'key': 'ƦĽԋӠϼΦŲƆɕыѥɖȠяͼΦдʬ\x92a˙˒ȟƗѺɖǅАɞǝ',
                                                        'value': 'ҪΥļ\x9aǁԙ\u0380ѾÖÇĵюЛ:ĤǾƌФМǋƻʢĈсѰǩчů΄Ҭ',
                                                    },
                                        {
                                                        'key': '˄ɮˠà÷ԞНԨщѱɝ϶ʈɤɦ\x88ǃ4ɐԃƅ\x9c1ʻǪƩô˂Ԭԙ',
                                                        'value': 'ĿǘҌŅĄԋƲǊѣȺκ\x7fˤΫçѐӝЏǴӃЏ˖ѶЕӕ\x87ԎӽȒʿ',
                                                    },
                                        {
                                                        'key': 'ЮʅłƇƂċɐãɧVԗǄWĲϛӓÜmӕŕӏʶӅãÓіӡѼįÈ',
                                                        'value': 'ƶ¨ϡƱ;ԧɯЊŃӥCҖkӪQąȭаÉͲŹ\xadǙϤŵlɴƠġģ',
                                                    },
                                    ],
                        },
                    'comment': '°ЯąξǑhSӥZȝЂѐҋgÚόЙǸӈǸψ¯ʓΓʷԦϖPM©',
                },
                {
                    'keys': [
                            'Ѫ',
                            'ĂԫWĉϒЊȣȰĝϥӚ\x89Ҥ',
                            'ϱaѢіїw',
                            'ϿҔǽжǽȑдҎ`ƫUαġ',
                            'ɹĖΏęӯƲ\x8bȃ:˚ԋʕÝӨ \u0378ʒGΗσȃù',
                            'Ч÷ɶŞɲƴ҂ТɲĂϕʅԨ\x9eǌʝ҃dq5ˣԗΛĄŤϫ',
                            'ěǢ$ȤȸƏԌ҉öʣǄĪÀ˥ψĺȷ',
                            'İƀƂ',
                            '˒ňԓӢőϞ',
                            'У',
                        ],
                    'event': {
                            'target_id': 'ɆԐϞİг҉ʗ˙Šhž˵ȐĐƼɔŹӆĭǟɇҪƃƯlʢХѺѱǟ',
                            'parameters': [
                                        {
                                                        'key': 'ȦǿԠˢүȥžЍҒÖXΒƬ˞ƬƨԥćԜŠ\x91ԃĺ°ύɾґ>Ǘ\x98',
                                                        'value': 'Ɖәϔˠ˟ɥƧж\x96\x7fðǈΙϋϢӢǚģ:ŉЬǏԅʡψїҷ\u0382ѹҽ',
                                                    },
                                        {
                                                        'key': 'ŞɅdϪи҆сӺ΅Љɥ¹ȰϞǄϮʏ˶ѼFƣ˯ǏŝФÌЀ2ʪĺ',
                                                        'value': '\x9aŜɡϽϒРŚɛΡȄʆԮǾłԎΫӞɐːϠȢҋϰԓJЈBŻͱ[',
                                                    },
                                        {
                                                        'key': 'ƁеѢɗЁ²ĶȲʉ´Ӭ?ҲûȖˎèĥЈҮ3ªɘűϭ˵ґǷƘ\xad',
                                                        'value': 'ƺÕѣǟÅȍ¿þƭ_uуȐɌΘʋԣʾ҅џoɱʻˢȁȊĵƻŪʥ',
                                                    },
                                        {
                                                        'key': 'ǙόÃѠʤýԍƴϔ\x88ǶȢӰ4Ǽ҄ʁѪӽĈʱPӄҪόf~ʱäЗ',
                                                        'value': 'İД˖ǯ;ԦàҖ҆ǲӹƣр\u0381ŷŎƧtPkМƷ¶ȀĨӐȪȆοt',
                                                    },
                                        {
                                                        'key': 'ϧƒŦʋϘ`ȥӶɛłйȏƩ\x9eĦҞiʫkÃӮҭʐǎĳǏŧʅɟʯ',
                                                        'value': 'ŝ\x8bķ@ǆrԀϟВǛƀđ³ŋΟǘ\u0383юͶ±ƛ¶ҘЯƎʷлƀӿǢ',
                                                    },
                                        {
                                                        'key': 'G¿ȞǣҎԝŖɀѶ',
                                                        'value': 'ϋȴĞԋΖɍҋӞɋǟτ[ÔɽәóοǖZӦҫDʌΛͼƁ˜ʛú»',
                                                    },
                                        {
                                                        'key': 'ψӐ\x8aǂͼʺәąѮȅˆЖǞĝӥȸТτáҲҴɘFέԜӣƆЇЁA',
                                                        'value': 'ί{рƒċȐưȯĵԗͱɧáӦɲӛƱԃӈǐJǰ҃њеӪӺ\x9bѷә',
                                                    },
                                        {
                                                        'key': 'ͽҪũ˪ǒƸ˃ыǥĸˑqĞЯĝΥ˙ʉѿˌҮɿεvї\x82ȶ,Ʋư',
                                                        'value': 'ɷԮšĸґɸˇϗȶ¼ѹĢĜîѳ\u0378ϲƬ\\ˈƟ˟ƙIl\xa0ȇЭБ\x8d',
                                                    },
                                        {
                                                        'key': 'tӴȃ˹ȰÑέϖˌˡƳΎď\x83ѨɲǷгσ\x87ǜѲ˄҂μКȗrΜČ',
                                                        'value': 'Ѹĳ\x9dȬǆƨȳӀş\x7fȩʲȱ¢<ʈԃϙƸΦԎťšάų\x8b\xa0όЫѥ',
                                                    },
                                        {
                                                        'key': 'ӼϲʓӯѲ\u0378ɺ҇ʴƳŴʤϞϰҝҨ϶ӔԉĺǰMдpŊĥԦβӑҽ',
                                                        'value': 'ЯОdƖ\u0379щӠԤӝ\u0382ÐӘѾӹˢΪŵЏǟϥɈǯѸFɾ\x97ӆɤ¼ǈ',
                                                    },
                                    ],
                        },
                    'comment': '˸ϓѱхĺOȷψþҨŦ>ư4Ϲ}$\xadԟӁЄϞγąīԪǠƄǻʱ',
                },
                {
                    'keys': [
                            'Λ˜ΚʎΏƞíƕʾʖnɀʩϾϟŅȁɲư\x8dĊёșŗѷʉƳĔӋ',
                            'ȝԘѭƻ',
                            'r¼ЮͱцʁƣɖУӠҹԞˎ',
                            'ñʳ ϑ',
                            'ϹѐŏџРȕҦ',
                            'XB¯Αȴ\x8fӂˬø×\x9bе\x81øˌȳȹр',
                            'ʌѷǏ',
                            'lȉ,ĴĄѣѿѦțʾ',
                            'à³ˈƕϥ%ϊōЌÀѹΉ|ӵ',
                            '˞Sȍ˽ĢАˠƉĉ\x94΄˴ʀϪ#ſB',
                        ],
                    'event': {
                            'target_id': '҇ѾϰW§\u0381t\x8dƲԃӒʹɍϨɂұǡĿNԉȑΫʤɂȿ˴~Ǫʉ~',
                            'parameters': [
                                        {
                                                        'key': 'ыͳҝƍʳЁŧǵɷą˦Ɩ˄ΤԌҡʵ¡"ͱͶù,ÃŇ΄ǢцнƮ',
                                                        'value': 'ϨĉʫԪѪǠɝӆ˰$цȖƊ˩ŷψy"ưÛƘ\x97ɘä.ǟŔƐӧҡ',
                                                    },
                                        {
                                                        'key': 'ЙĩïǞѮȉ˝TĭίŶhʁӽԗĊѵ|ѦʌƶɷӺȹ҄ѡŹ˖ɆΖ',
                                                        'value': '˜ĆſΈĺĥˇϪӀɚƣƹřķɃǽѿѓϧзӃÄɢÓSàҳʆѥʣ',
                                                    },
                                        {
                                                        'key': 'ʝϺˠcϗӖĊӠбŕϝǴ\x82%Ш\u0382ˍ\u038dϟÌSʤ˛ŕɛыɇʺ',
                                                        'value': 'Ѭūɪcҧˑѥɩäџ\x94āƸίӗħˍӣԑȻƘİ\u03a2ǙëãĝΎϫȰ',
                                                    },
                                        {
                                                        'key': 'ÖĤńȗΠÝƥƉӌŞίάҡJԀЧ.Ҙ\x7f˖üѯԜŽȖeʹŲρÓ',
                                                        'value': '˚ρǬϝһҮřH5ʬǹʙM˶ȺόmѧɡÂĤ˭ȓѥ\x85ϒґ˸ΥW',
                                                    },
                                        {
                                                        'key': 'ρҵȂŷʼǕαʱ҃ŀɎΑ@ΛȹÕϘȁӳпɁҽС',
                                                        'value': 'Ǟʲ®ҟŮøЮÙ6úȿĦζƦοįɔˁӦȕǲϦyωѷƙĈ\xa0ʧԙ',
                                                    },
                                        {
                                                        'key': "ŏÀĴӂʎ;Ć\x8cŇ˗ưˍƧϺМ'ɉϬҜfśУXˀÿÖӹ¡¹õ",
                                                        'value': 'ӬϬċdŖԥŦ˩ˬҟ\u0380ϭŵ¬ʆƘĳ\x88ǏσĜ%Э\x86ɜŝɄ%ӳë',
                                                    },
                                        {
                                                        'key': 'єmͱЙǝƴԙeɥ´˅ςĬŭ>͵1Ϛˢ¦Ĕvğɫ',
                                                        'value': 'ɚIɓˋ<ɣɫӽ˺ųȥ¶/ŊӌɫӏѼĶʌѫďѹȕƑМ ӆεӣ',
                                                    },
                                        {
                                                        'key': '˸¹ҟͲƁǝȬŋɷǟɿ\x98¡Â˰ͲӘ=żԄǷ˞SʻғʟʓӖǁ¿',
                                                        'value': 'ҙ»Kĺ.ěщѓʾȧζɍ0ǘŸ]щʘΧɶи7[ϓˊҭ¡Сɭǐ',
                                                    },
                                        {
                                                        'key': 'ўϣþƭʠʲӕǷƿźͺԅωțϾčʧɿДɦǣï»İɿ;ɽŊkƱ',
                                                        'value': 'ˈˠSʏзɠɋҲǩϪšˮҒ͵Ȭȑѽ\x91Υ\x88ҭιʵŀϫѕǝѬоӓ',
                                                    },
                                        {
                                                        'key': 'ӶÜΓτӺƊȧŝҭƄ˫OîƒˬбҼǹǝǹΚ΅ȨĪΗӗ}ы\x9bЌ',
                                                        'value': 'Ĉ¿șЀ´ÓӆǼĚǦѽʏЕ˵ԑǵŬʱϑʚϷÓǾʍǕ˕ŀˈӲŞ',
                                                    },
                                    ],
                        },
                    'comment': 'θˌήӹBϠǇѥѻťʕƞπȦҏƮȭӁL½ԠɿӘ҆СЀȓƮʇӢ',
                },
                {
                    'keys': [
                            'рŖʰӇ¬ҬΖˏӤöĀƊΝËȨЋύæÚ\u038dұԃďƉ',
                            'ʰ҄b_DơўɏůˬĆӥȑ7ʺ@Ҏ',
                            'ҩ%ΖÑķҦÀЉҎ˸Ѳ',
                            'ǌнҴ',
                            'Vß9źʸ\u038d',
                        ],
                    'event': {
                            'target_id': 'ʥԁâADқδϰ˭÷ä˽ӔÉǮ@ƂL_wǣΰԪΙȽĺ.ѓƻǄ',
                            'parameters': [
                                        {
                                                        'key': 'κξ˭Ȃư\x89ƳPȔǞҊO¤RҴǎɾėɦϫϭAЍ΅ͲʄɴҼÃʬ',
                                                        'value': 'ʖеÑѳʪŃ\x9dψȨĵȌӛ˅@¡ʭƝӡѰǪBӧӅϪ˻ҡąϔҐƈ',
                                                    },
                                        {
                                                        'key': 'ʒŽµѺxˌǸïΊžHȽÕ|Т\x92±ʩϹʕƐĹΏξ!πђͺÜи',
                                                        'value': "4ƆǾƲӌӾωËǁХ\x94˭0ʻ\x87ҘƐƲ\x8cӫïĨϩԤѼŞ'ßϡȀ",
                                                    },
                                        {
                                                        'key': 'ɐӏҘōʢąȾ8\x9f҇m[ҴJŒǠԥУƢԫÇ8ԂЁǊã\u0378ŕTЂ',
                                                        'value': "ȗԁϩzɦϯΚɑԃͱċŎсƋøùӇž'ӈƮǶԕѵĢЛϾт1ʏ",
                                                    },
                                        {
                                                        'key': 'ÂƯѓԈŚYɚԇΥЩȦlЙʄΣЧLĩІоjԠ\x90tѹΖŀѲŷʎ',
                                                        'value': 'ʩșѳÍȿEǆќȱΙʬÆʭѩșɘçʌц˫îŠʂΎÍїӦСʃȐ',
                                                    },
                                        {
                                                        'key': 'ʑƛĐќΎƍȚӱЍɁіȑӲϾ\x88\x86ĿΥʲÿ҈ʩȣɞɼ҇ʬɡʻӦ',
                                                        'value': 'ЬЉОʿyŤʋ-ƴϐðÜǥѥĀɶĮǀƺӂĘΡ\x81Ѧ/ѥŖȶаϐ',
                                                    },
                                        {
                                                        'key': 'ѝCѕϣƘωөĺɯȏρʩĩѳ˾Ҝȸų\x9fЈԗWîŁӉϹǩԦǐҧ',
                                                        'value': 'ƳɖƃЇȅñҧĜюʴʗÙDƐ¼Ň\x82ԉɣЯɨtǊaɇŝÂѐӮϿ',
                                                    },
                                        {
                                                        'key': 'ѰҾÊʠ\x95n½ϣҐͶԁ`ʡġŎƢΝҴŐ\x90Э\x9cŢԞȭʿô҉҈ԑ',
                                                        'value': 'ȍ˖ӰўˌǁЯʢû˼ȔϹƗʇɋϙɸGϣʹуԫɻÃOǉt\x80ǅ˵',
                                                    },
                                        {
                                                        'key': 'ĊѶơӊ\x95Ǩȃî"ԃɣɽϣų"ΩѴӪаϐфžĔɚΠˑÆøѢǚ',
                                                        'value': 'Ƭ¥ʎÿҪŠ΄ԉĲˮ҅ȲɒóΗ҈\x8e\xa0еҿЅʕӏǱҼĿʑϢʱҞ',
                                                    },
                                        {
                                                        'key': '\x9cнǃчѹÙЏӶèȰӀӓ\x8eƌǿŵmŏϱfɫĦŹʝ®˚ƉҭƘΡ',
                                                        'value': 'ļʠӥāǨѵϥґǑɅÙŪÉϑӃԧː¼ΞœɎŭωƶҧɸɻВͳІ',
                                                    },
                                        {
                                                        'key': 'ǚñ\x97Вμ˟ʥɃ¥˓ͽџn¿ϸɟǏƹƴɌΙШ5IԨǍ#ҿɚӫ',
                                                        'value': 'ӫѩ\x83¡¯wĜŵʴtĐӍԡÖҏƸȁˬƎɏѥĉɱɫθƌϐέÆϙ',
                                                    },
                                    ],
                        },
                    'comment': '˸йZьϢВҏυђȫŁ\x96ΠʌȚȲϽԠƭ˦ɊɫĢFʿЕ϶ŵǊҺ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'master_sequence': [
                'Ӡ',
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
                    'ҭä°ȀƣңȠƠȔЙǒπĉʚġϳ;ҴĹɒEЛD¼',
                    'ԣњ˨ƽǖ\x9e:ϬӢsɌϫϳ\xa0ЌѐϥͿö',
                    'ƐčTȄ˸ǑȺϐȵԀpðȾǃӿȗȂňfĚ',
                    '2ĘɒɻșˌѯűϞԄӤçϕŇ¯\x9aĭĆɔѕ!\x97',
                    'ȔęΖԐǵѐʯ1ɿϗA',
                    'Ѻ˹\u0381ӈɷрbʪ2_ψǩλŖΓѬѱɍԇǆəԜ',
                    'Іȇ\x99˔ʭӰÞʈǳ',
                    '¤űѸƲƥʽʹô˾˽',
                    'ΧϾjȰ¨ķЦͽΆϊ˳Ƥ˙ĪԛȵpӼɫnDŖ',
                    'ƍƪ\u038bΒɘʨӣư\u03a2˝ςѓжŵӀ',
                ],
                'bindings': [
                    {
                            'keys': [
                                        'ξΉ\x8b',
                                        'ˤũγɌĠ˖\x7f[ђėϜ4ƊLΟ',
                                        'ɅϾƕ˦ëťŦˆš\x9d\x94ǏԊгƦȈ',
                                        'ѽԧ˞`ұǂÜ˶ñïUǑпȅƋԦͻȊǂǀCĔсϝªɍӰ',
                                        'ҎƂϫΕ[ʑĽƅǂ',
                                        'ҲѸɻΛŨԢ¸ƥӋϣ˟˷ϑΨǭѽ',
                                        'Ëyԫϴһ',
                                        'ƐɉΕʄǩ',
                                        'ѰϸԉԎӌ϶˃ԞƎϖҹîÔɹԑϸʪ˛ɌȞĽ%zƵƾ',
                                        'HƻćŐźǲȃʩƘϒ',
                                    ],
                            'event': {
                                        'target_id': 'ƙԧКͱр\x95\x8aΊĆƮŞƓøºȊÖŭō3˂ĜɸŸςɦӃЈ\x87ƒʨ',
                                        'parameters': [
                                                        {
                                                                            'key': 'rƳk@«ϗc˽Ōт˼ӞÌҪЫυѓ©ɴѠϧã]ɢwԟӛ˱\x9aĀ',
                                                                            'value': 'ŰɆǖeҎϰΌϸǰ\x8bǴS¨ҐρƽѧŮ$ĺҎhҿʇȐΞí0\xadɼ',
                                                                        },
                                                        {
                                                                            'key': 'ʵ\x8aΧ˦ҕҞÄ˷ϹτƧżʹȡʹјöŶøѰӆʻҽăӺǧҜҫѷЀ',
                                                                            'value': 'ƺČÁʨԅǽʆЇʮɹǐȶɖȅǶǡĪ\x86ӬÕǒȈ˖>ԤЅưÙŅϼ',
                                                                        },
                                                        {
                                                                            'key': 'ϲљºҴŴpv˅Бэu´ĳ¡´˶ŉВѱԠͱýЊĤѴӵìAC×',
                                                                            'value': 'ԦϣдƯϞ\x93?þşùʃſϰǝԒgŅ҇ǌəʀÍhêǗоϓʗɝԆ',
                                                                        },
                                                        {
                                                                            'key': 'Òːʱ\x82ƜĪǍƦ\x84ȑȪόȏɒЛƉԈɻӎЊļÄĮЃBеʩ?ȷΫ',
                                                                            'value': 'Ìӷ˩ã˾ԇʔɉѹȶɏţǂˏ\x89ʑɌİӎѪƃԭѕÎҔшBҒӽӋ',
                                                                        },
                                                        {
                                                                            'key': 'Қ9ԂҳƮОÓÄPʫɆƘԫȚđ\x9fɚęαŘū(ĵȾÎ\x97ϳѾΠʒ',
                                                                            'value': 'ŘǶâʰҼӞϥ҈Ɓ}ɼŕɟӪɈĴȓɻҠIǐΈΓǽ\u0378\u0383ϓѫOφ',
                                                                        },
                                                        {
                                                                            'key': 'Π˔ÏôºÝԞ',
                                                                            'value': '\x8cȪȯ˫˶;ʮșÊÌɅӶǘЖΘѻӍɒʪǝªóΗґ˩ɁʞΌГϙ',
                                                                        },
                                                        {
                                                                            'key': 'Ɔόѱɴ\u03a2Έ϶JĮ˸˃Ǭ҃ϻ˚Υ8ЪºƨЂƻȜοуͶͱɊҍӅ',
                                                                            'value': '¤ƻǾˬǌԝΤԅ\x91Ч\x8bҾé\x89˞wʢϽԠŁªϨˠÂД˸ˁҲȔØ',
                                                                        },
                                                        {
                                                                            'key': "ų\x99·ſ'ѹΪˈ҂ԨƊƁɑϥϟΙȾˆĒϜҚȨЁΐʂ ȰǚȬ\x94",
                                                                            'value': 'ԬĿЬϏҫĄʽγǾʾƢ\x86Ǚĉĥа "ǲȾłϭґʺδʖΏìП_',
                                                                        },
                                                        {
                                                                            'key': 'ϕӹĦѥѲǙϊ\x9eӚõʖΕ˒ѽчѧƠɗĮ\x80Ҟˠþbǃɯʩӟϝ',
                                                                            'value': 'ϕèαȩʵǗСɦԩɦ\x97ǧѢʙ,ý\x8dɬɲńΉ\u0378Ο"ЏƃȖŠΘͿ',
                                                                        },
                                                        {
                                                                            'key': '˵âĕɻԀʸͻѡÄԭʱ',
                                                                            'value': 'ԚåƊ\x9eθƏқԣкϜ˭ҼƆӢyκƚТſŷ4Ǽć#ϮëĠT\x94ʺ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'Ūԙ)ӍǠ¼˖ԗԥԗČǘțɏ\x83ÞǮĴӉķ\x97˧¤\x90ɟƚӣЖȤӾ',
                        },
                    {
                            'keys': [
                                        '¤˼ӥѨ˽',
                                        'ʙqԢӷôˣӱӯ',
                                        '²ї\x96ѨͻÍѨ',
                                        '%ÿOǑňĪ»Ͻ',
                                        'ъõǎʷň',
                                        'ƛ3˺ΟŅRυɃğȴӑʈȜҘԕ',
                                        'ȶæЦɾțƢɯϗɷßĦқɢ҄»ŦЎΆЬϧ',
                                        'ǶǢѹʈœðϛ\x90ȗzĔ',
                                        'е˅ÜŻŒҏѺǟüҊѝѤĄ\x8a˻ӧȦǢ˱£ʗ',
                                        'Σ˥ԩ;4ɔʑϷøȼ˃',
                                    ],
                            'event': {
                                        'target_id': 'ȂʎȹӵÜƒǔЈΛg˽ȸʄЂе˔ƏҵѝѴΧӳОΥԔԧ¯đԕθ',
                                        'parameters': [
                                                        {
                                                                            'key': "6\x8e'īѲҠƼɼçˮ~ԓʻΖӫ2ДʿƘҍɶ§һȍЂŨˑɣҶȺ",
                                                                            'value': 'ȀYδнΉâɐǽȜƆW|ǞķĘͼdģѥŽúōìɺρhíΌƃʍ',
                                                                        },
                                                        {
                                                                            'key': 'ɂʺĄѼĪЧҍƱХ;Ћωʢ¬Ҧό',
                                                                            'value': 'ķ¡ӈХÆAӅӣʔǓƇʝºǝӅĔȚĀ˚Яż˟ Ýč˷Ϣˉԉˏ',
                                                                        },
                                                        {
                                                                            'key': 'íф°ϣǫҬ³\x90ԥӏ\x90ʖēǕ˪˝qНϽʛ;цєʾĥ\x95ȚëΨ\u0378',
                                                                            'value': 'Ѝ<ƓÏηʜɘҙǪ(ŞΖӠШkϲǹĹ\x91Šʽċΐ/ɡěυ®ćͰ',
                                                                        },
                                                        {
                                                                            'key': '˞ǔЭÞҺ',
                                                                            'value': '×èϱӑºӪͿjӻöԠӉţȟǩӦґЎɧʝƹĤɢnӖˏΘψʀɹ',
                                                                        },
                                                        {
                                                                            'key': 'ӠѧšТˊнĮə\x8aȑӚʄϵÇȵ˥ʐǬφ˰χұɼԔҙΠΤĜ\x7fә',
                                                                            'value': 'ȶ˗ЮΪɌҒӳќ·җ)Ϊçrԥ˻gƘΗΔ˧Ӡ[ЈҹӛːтԇE',
                                                                        },
                                                        {
                                                                            'key': '\u0383°Ӧ\u0383Κѭԟӹʫ҅\\ԑIɉӾśƆY˹Є',
                                                                            'value': 'θæУФƧѣɤÂȔνҌİϒЬԙěʉʘ½\x91ĳȮԨУɜҊԏɽƁԛ',
                                                                        },
                                                        {
                                                                            'key': 'ʊŨȾĽɬӞĖŶɒΓϋзĒóÈРĞӦƈĕЪȷэƈ˨ĠԬ˙ıМ',
                                                                            'value': 'Ԏӡ}\x99ΟÑЄѳѬǙӣɑԮńҎұF$ʐÉǞԫʁƿƛьƬȝĺƎ',
                                                                        },
                                                        {
                                                                            'key': 'ɌĴƐúЕӵМƂҫȡ\x98š 8\x94χŠ',
                                                                            'value': '\x86ͶΔӕ\x87ΘtŒͶϢĢҶҧɛώӳ\x87˯Ǯȧ<ɝдЗѧ\x94ɭԠӢͶ',
                                                                        },
                                                        {
                                                                            'key': 'EʮУˍȆ˱ɯƾЪ\x8bɮĮpӒϞǴÿÒɡɵǆԊΘɍáŽãðvΖ',
                                                                            'value': '\x99ӋϻѰ\x99ɔ˸ǘӷѡƥƄºʒuǛеĳ¦˭ˊ˄рȽм˳ʖӞɿ΄',
                                                                        },
                                                        {
                                                                            'key': 'ҝǂіŠʌʧѥԘɔԍȇФƾěј©',
                                                                            'value': 'ұƱԌӎƏ>ԓÑȁƚԥHȖǞʌӌŴ ӚêŁ@ȧð\x87Řýԛßң',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ȲЙқȨɵPȓǓÝʩȀԬʿ\x82ԝ\x88ƂѻƫЌǋЀΖβĠҿΡɰȴÑ',
                        },
                    {
                            'keys': [
                                        'ɊԖNǧйԢίύӷϴòÓͱ|ǔ',
                                        'ÜˆȕͶʿ®ȄнҜÅaѾϩѐ',
                                        '˂ŧĺʆȣï',
                                        'į\x8cȚʸӑϠжǱѮӗȊ˗ǔȄқӄǃ',
                                        'ˇω\x9aԘӢҀŊDӔĢùԖӿˮǡӘŞɜӺcӖӒÆÏɏԆӝ',
                                        'ɷȭό\x7fǉϱƯǖ',
                                        'ą·ϛʀǟƳҐRγЖƲѝƑŁʒ\x8fǪ҆ǦŎG',
                                        "'ƳӼ\x85ӞѼҁΒŇεɶțōѧвūǄ˚ψο\x92ˎ",
                                        ')ȍʉʄѥ\x9fćʠʼɝȎͰ',
                                        'ήŘˁÎ\u0378ӢүЙщΨЛĂϬиƿΚ',
                                    ],
                            'event': {
                                        'target_id': 'йĔғȘͱʸłŏҼҋfʡѕψĒȎȀŕѠőɊцLȰ\x91˷ˢʎћĖ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ɹҀȎʼʲnѬρǆĈěƙӥ¿ǇΠςł2ΜůЕȡ[ͶЕɱƓӂȨ',
                                                                            'value': 'Еʰ¶SƚɆγϷĘ\xa0щƈͿĪɗɷʼƖ\x83ėĄȝϡ;\x81ɁԃԊƚǰ',
                                                                        },
                                                        {
                                                                            'key': 'Ōқȃǐ˻ƅ˂\x82ȜƆɋÅˏӣӥҸ¤ʖƗǩԋυѧжˡШ\x95ɴǫʳ',
                                                                            'value': 'ǣЪź\x98ű¿ϛƴФɢǾӕģЅȣώǡʭąĐϊõƗΎͼʉДƲʒȯ',
                                                                        },
                                                        {
                                                                            'key': 'ˮͽƗβøſǾɱУѹ`ԗӘÆȗʟşӶԉ',
                                                                            'value': 'ȃÔoҺ\x98¹ʼ\x7fɴ\x99©ȩvѡƗӣXӇɴǜǩцVǬ϶ѫƲŕ½ғ',
                                                                        },
                                                        {
                                                                            'key': 'ӂΡģъǚǅʧ\x98ŝĮėāѽƜɏҽĄňʈԛ\x90Ѓ',
                                                                            'value': 'Ԍȯé˃ӧ҃ΕőďǅԊȽăάˋӮŷʮǞ;ƅӑϠ˭ĹԊȑ˳èˊ',
                                                                        },
                                                        {
                                                                            'key': 'Ïѫђʩlΐ\x87ÕϏƸʖł|àɑӆͳдΟқ\x94Í˄1РɀѦJϹ϶',
                                                                            'value': 'ƚʇőѝņÿιǢƀ\u0381Ň,ȯˤRɷɯŪЉҼьͶǉȻ\x9fҷԢɽώЁ',
                                                                        },
                                                        {
                                                                            'key': 'ƘϨӖͼүIƄĨ@ɲȲʵˮKМɷʤˮÐυÂԦʍʪêіɅώƭɢ',
                                                                            'value': 'ϙŎÆͶӅpŀӬδȀãʗҼǭͳЋ˯4ǻȪǷӰ\\ҍȋťΞĄԅ£',
                                                                        },
                                                        {
                                                                            'key': 'ȱɾƔʸʨжɞÂÞĊȩңԥǒīԎȁ§}]ĝňΫ˓«˘ӱʭϝ§',
                                                                            'value': 'ƛëԌÆԖˡσ˒˞ϳ\x8fɬΈȴ҂ǾϓʪͷԛÈŗƝԔĂŌΨǰ{ϵ',
                                                                        },
                                                        {
                                                                            'key': 'ƋģÍôҀɂûD',
                                                                            'value': 'ШƔҩɐƅϜ\x8bӧùԧӿԧŘӇˎ×ΪԜǰˀƭȕǲЁƣёԧьɷǬ',
                                                                        },
                                                        {
                                                                            'key': 'ÆǐÔӸė˼ɪԧ˞ДÜҒƙòøΜӂǄ$Ѩźҧȝ\x97ɋ˛ɞƳǋɵ',
                                                                            'value': 'nƫȢ=ʧѶȤcƜȳʽ҅ΡωӱGΏЪǻ¢jxǈēϝȉџƱʴǤ',
                                                                        },
                                                        {
                                                                            'key': '6ѣϼĨђĦҕc×ʺϲƽ>ќ˜\xa0\x81źнȈϪ˾ȔđŐ',
                                                                            'value': 'ƃӶƥ Ѱ5ƽԩҺóȩ]ӒЯ\u0379-ɇ¤ѐgΎśúʠȚƙǵǤϙĳ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'Ǚ]ЀˆȨўǷμȽӫȽԣRϜϗ\u03a2ʰȤǝÒÏѫȸbɘƀķуGκ',
                        },
                    {
                            'keys': [
                                        '·әЈԚȃДҲΡϴèԃǘЈϨʑҥї¡ȾɽǙѵɔҒӇŒ',
                                        '_N˖ȾhĥtЯxź҂ʉȍ˜ɔˀ',
                                        'OŠвʳ\x84ͿfЦȎ@ƍϺц¹ԉDʖŔưΨӀԬ˞',
                                        'ˌÙј˾ѣέ©ÒƟĆæyʁǴˤΐǸїĵçзЦˊƘÛϝġ',
                                        '\x8bюӟŨȹԋ\x8bϓ\x91ƙEуãѠѨȷzÛĜǘѽΨёJǏƉǾ',
                                        '\x89ѝȀĜӀʟʨ\x81œѮŧҬҳð˹SKќғθŭČϠɼΏǎì',
                                        'ɼԩЯԐIWӝŎԪԊȢ',
                                        'ϗʌˁ-»ҊȞаHӄΓƳϕ]ԍ',
                                        'ŵjȭ\x89³ϼĲ',
                                        'řǐǬЯģǦæ\u0380ɨɇÿӑҒӧįįřͻʛҫʇğGɀ§яɌэ',
                                    ],
                            'event': {
                                        'target_id': 'ԍĄӛΉɗǓƠԕҷˇǃŒċќȤʳͶʹñЪ÷=ӚΌİťɽˌjΌ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ĘîҳʠўǸ',
                                                                            'value': 'ƶ\u0383ДáǒԦҕΗѢԭāˏ\u0380\xadԤӿưƙǒЋӓŚęΩʚҘԈŉʓę',
                                                                        },
                                                        {
                                                                            'key': '\x97`Ŀ¤ώсñҔžѫ¹н|ǆ\x94͵ȎͽѣȄ\x9dë˧ӪļνӤΓŷû',
                                                                            'value': 'ʅԑёʆȡ\x84ƊϖɶƥԣĮӊϽɠµĎεГԉɃȽͱӾ\x82ˊĩƌĚ˼',
                                                                        },
                                                        {
                                                                            'key': '˗ʲŌΗȍϼеɾ˄μgЂŸρ˗˸;љҾҙΙϳʪԨ\x90ƭƖȧWW',
                                                                            'value': 'ҋǦӛŁѠ҆ŠӁɻɬˉyƴjԓȽϺγɩmҚ\x94Ǉλ\x93Љά¨ÛҨ',
                                                                        },
                                                        {
                                                                            'key': 'пÖJ6ɟѽZȇʛƴr˺ʿŎӄ\x81҉ēԕĔě\\ƇԜӐЭчfӊ´',
                                                                            'value': 'ԙɭĐ\u0378ˤɊǜԘyɺǔԏiÁҡİȴԇǆƅ\x89Ӄԑ˦ǯőʩkԟˁ',
                                                                        },
                                                        {
                                                                            'key': 'ӅˢʖʘӐӌ ӫ¯һýЊԄ˪øҴԢ\x9b2;ʧɴǔҨΤůǲЧÝŏ',
                                                                            'value': '\x9fтљҧpȽ\u0381ЎÛĶϸÁɶчÞʸӟϏΧ˸ˣʦOñƀĆЕ\x81ÙͶ',
                                                                        },
                                                        {
                                                                            'key': 'ŵɃ˨ˡǙЕԍӃɳWΫɷɜșӧɵɀ=¨¡ȏ\u0382ʆ\x8cá˓чΆɻʔ',
                                                                            'value': 'ƹʪ\x86ǹµʧřΤĮ|ĩÜɬΒȊȉʣŁИКκ\xadg×Ňǌ|Áż{',
                                                                        },
                                                        {
                                                                            'key': 'ѹԜɉ˔ДTǂȺɾ',
                                                                            'value': 'ϘәϠəġɉΑϣƌƱɥļĮˤϧòĕĚϘ;Ȕє\x89ϼЀЫѳ˸˥ʃ',
                                                                        },
                                                        {
                                                                            'key': '\x83ʛKƯțǵɰђŨfɾӥ\x9d˄ӎҚɤs§Ɛʘ˹Ѭσ\x8c¼nϼωƏ',
                                                                            'value': 'ƎưН\\μƥӉȚõȳѝ\x93ʸèд\x83ĚɫǁѶԋ˯ԔßҦ¥ΐȞҜϮ',
                                                                        },
                                                        {
                                                                            'key': '˵ҼӗǤȼˊƣΔ˦ӨǕȝǥɖд˛tȡˢϤő˙ĝĹӈВ\x98ԭ˒ќ',
                                                                            'value': 'ϭԠоψʮχǒͿԏsõɹө\x9cŹө˅кμȗ҆˳\x96ʡӮõӗȂǍƛ',
                                                                        },
                                                        {
                                                                            'key': 'ŭо\u0378\x8bƈϢΥɀŝȹѹӁѫҙnҐīǏЄȎəǩԢΉҘԪЫͲӜˌ',
                                                                            'value': 'ˍŀȡþǿʮǫ\x83ÔȡЄŁЬχ\x90˦ŧЪĝˀ2љԑґЈҗӿȭĞł',
                                                                        },
                                                    ],
                                    },
                            'comment': 'jˡΠÊ©ҝпѫьӟͻ˒ĳ\u03a2Сγ¾ƧûƾΘ˾Ƀ˭˹ѐӂԚÊ7',
                        },
                    {
                            'keys': [
                                        'Ӗҹ¢ΥʺňĩßЃȳǏˀɠπ',
                                        '˓gӕϔƥʢʄ',
                                        'х\x89ϛΗÀӲƽťƦѲɀâĵ?ŋіȁ\\Ѓ˒ώŋѷԋÖïĢѐ',
                                        'ʒ˄τˉƨ&®ѩ§ǠɀÖɑǏˡǦɖœAWķдВL',
                                        'ǃ',
                                        'yPԤԑ¶ɴϣΗʗÌ>yΣјϺcǍ.ѧBө\x80ΔΌ',
                                        'ϦўQãςʹƩǆ@ϔ½ȢɵŽYЬ˕pηП',
                                        'ϬÁ\x85ϛåǁŞPͲη˨ƏƽοΝ˩҇',
                                        'ʦʏьκ',
                                        'oʾ®ɛΐşγΟɵȿђhTĘ͵ɬӥʩʹν',
                                    ],
                            'event': {
                                        'target_id': 'ѫӏ˞ΎɱϊΏӯɄЁŁǢΞ˱\x94ӐбâYqĠʝǼŭćφǹˁΨÅ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ǅķMȮƑԏΒ#ѮԨϺJѥÈ϶Ќў',
                                                                            'value': 'ϬʕÑōҁňΣōǏѤƖǜɕġÆ+ӖʱʿʧǄěǆԉʽΈƂȳΨ´',
                                                                        },
                                                        {
                                                                            'key': 'ȸʑƛˬȳӇȎP9\x8f´øƨ˼őҘóǅ͵#øØºӌϏĝÕŊǩǤ',
                                                                            'value': 'ĝ˷ʹŮϮиbҶ҄ǞԃɻΐƠЯPɺţǈʓʓÌӏʯӇ%ǆҲѶɭ',
                                                                        },
                                                        {
                                                                            'key': 'ĥҿҳ˼#z\x81ɔ\x89ƤĸːΪʙɔŕ\\ӯԫйΆʮѵ´еæӮΡHD',
                                                                            'value': 'ϰϳįǐʴ{˥ԂΟӚ\x93ʨ-Қї\x88ԂȒȰӼϟñƛԃϫŲħĮ\x81O',
                                                                        },
                                                        {
                                                                            'key': "Ⱥɧʲӛ´ԩєÿȨŖЂâGӏƘш'ɌўҦǕǄvǤЭóԗ7ņɤ",
                                                                            'value': '\u0380v\x80ϋʬϙÛɍҰΦŕ\x9fÃȳwԃοԁ˗ǅŎҧɶįúʀǭɁξƹ',
                                                                        },
                                                        {
                                                                            'key': '²VΎț˩ʛӹʉȍpċ{ԨȉѐҫѳˬǆԠĵаȁʤάҙˤ˧mҀ',
                                                                            'value': 'е˩\x88ɝɍϡZЗ˘σ˲4ʥȩπ_ȟԈ=Θ\x91ÕςċœɦŘôΥʆ',
                                                                        },
                                                        {
                                                                            'key': 'ɑԒ˭âΝʬλnđÀЗŌtЌЈҖτϰŖªǇGǃ\u0381Ÿ"ϩΣǺ\u038b',
                                                                            'value': 'ҟʖϧȦѭßԦ¤˘φˌϺʒТȃӇϳǵäʫØǡ\x81ӎƌϭǉɂȘ1',
                                                                        },
                                                        {
                                                                            'key': 'WǑɋҷ˕ǛȜƒӒ\x8eŻ~ŁĳψŸƝŶ?Ǣˀ\u0379ӜшϹҏȶ1ȧϺ',
                                                                            'value': 'ĂȽʨ\x94ĘҦgƀίùʙȷӪɛɱɸͶīģ˘Ôϲї÷Ќ˩˵ѱԦζ',
                                                                        },
                                                        {
                                                                            'key': 'ƝȞϔ͵Ӓ˳ѲӉƖE³ɧ\x94ʭ\x98\xadәǩûǇӪȹƽuԙwğ˔śœ',
                                                                            'value': 'ƤϝŅѺgƵǰэ\xadωіʴǑϮ,ă½ĊŞҟԪλȓƼznˠîɉă',
                                                                        },
                                                        {
                                                                            'key': 'а_ʇҒҟ˼ȖӣǘǺʽ\x83ѣԢƙ',
                                                                            'value': "Ѕwόшīӛ/ǕЀĜЂʅ\x9bɜŧɰǗӠӥЀŲɨƯë0×ήЗ'ʾ",
                                                                        },
                                                        {
                                                                            'key': 'ίрДѡɈÇεȡņϺíǽҥϢβǀǴƍßťΆˬ΄ӺрͰжΐќĤ',
                                                                            'value': 'ĨӡĮíƚѴ3ГРΌƶхʽлԩÀğȆˡȝͳїɱǡЀÊɀԟԋҦ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ȎЮɘȵǛĿ²В˨ɂғѴɂχUŉˢӮԠќ3эˮӂǠ«đņłʸ',
                        },
                    {
                            'keys': [
                                        '~3ѶԆϛ¿ʫѽԘϩϙʏŖ˟ʊɱŀрѸӷҢŦȯӵĪ\xa0',
                                        'ȃ\u0383VʘɲƸˎ\u03a2ϛҿ',
                                        'ӶJɪ_pӠŹҔѢ\x95ϦLΨΛFŖ!',
                                        'ɤūʖ\x87Ŭ',
                                        'Ԋ\\{±Ѱ\x90ǮËž#ΒËӝƩҷ˞ǣ˙ӲǋƢ&Ӛѯ',
                                        'ƋζľȖĺ>ȴƎú\x97¶ȧƟOƏ˥Ӯϲ',
                                        '˧äj',
                                        'MєϪ¾ɡмДąΜςɔ˲Ʊ҆Ϥ',
                                        'ƼʵӇȵ˂σјmɷȟǖ_ʴȸϸαƷ^ȷҲÀƈ',
                                        'ŞӅз˚ƲςvҿĐǍƖŻҾȺʓ˗',
                                    ],
                            'event': {
                                        'target_id': 'хĉѩӗ˻бBǳʨȐчäĹ˯πˎЭŭѫĜѬʾm\x9a˙ыfΐƛȞ',
                                        'parameters': [
                                                        {
                                                                            'key': 'Ҹļ\u038d\x91´FίɡѽȚöҗǃpϐƄϭēΫЕźʛцσīȃͳˮ§ʙ',
                                                                            'value': 'ʱɖLϜˌ®ǣŰΛ˥σϋԒɗǤԋʚɤb',
                                                                        },
                                                        {
                                                                            'key': 'ŨȷĄϡʏ˽ТϚŮ\x8frŊǤ\u0378ɨá;ÀҩɶŖÝŲ÷^˄удŏŞ',
                                                                            'value': '»sӀҒԩϐϵ\x99ѲѿǢ+ЦɠȶǠуϲΖӯѕe§Вϊƛԙí8ĕ',
                                                                        },
                                                        {
                                                                            'key': 'ȿĖʠϝЧСÐʀΧѾѥļθ\x9cҸӒʡѧɰɠǈÉ\u03a2\u0381LɁěԮo¯',
                                                                            'value': '¤ɒĵЊŐǪҠҤğѳúŘȎϐNсȻӳŜǤ˛¸ǪĢѮĲӊϿΨΩ',
                                                                        },
                                                        {
                                                                            'key': '˸мөςϮϱƻ҉ơѾɾіȎǪɼʀŹѠʰǿħ',
                                                                            'value': 'ïϗɟȜǚˇʏIʐѶѲԛ7ΣίΝŌѤğĖҋԊҠΣ\x80éƥǊҤĿ',
                                                                        },
                                                        {
                                                                            'key': 'рԙ',
                                                                            'value': 'çóώÏӮț\u0381ҏ&ʈț\x9bˢςԄї\x82ѓӀƋϴҮҴƓШzʸϷȬĮ',
                                                                        },
                                                        {
                                                                            'key': 'кζϡɂɻ\x99"ŞȢʷɄѕƶǦΙȿΜӑƉϔԓГҏΗ˟ыїǀ҄ˇ',
                                                                            'value': 'K΅čˊŢ1ӖǏϴЌƱӁӪЬѭҿʘ·ϬϚȁ',
                                                                        },
                                                        {
                                                                            'key': 'ħ\x81ɤŵЧĂʻJ˱Əɳ"Êʳj˸(Ŋˡî¸ȊâΩʢнΙƿŹƳ',
                                                                            'value': 'πÒϰȭԣ\x85ŝ͵ĜǬÁƁlKɓ҇ΙυΆȞ©pǎɟãԩŎϥ҅Ѭ',
                                                                        },
                                                        {
                                                                            'key': 'ăΑȎҸďy1ϛȌѨ8ΩȀϙσF˃Ō˒ÄѓÝÒàĖ',
                                                                            'value': 'аψƎάôŰӋƄǺ%Ӽ\u0379˦ǡ˪θɨĪ˩єDҽƩςӀ±ĺұԋ\x89',
                                                                        },
                                                        {
                                                                            'key': 'ǺѩРмƶʤúԍѲ¸ɷˮ˯ƪԟȄҷăҫǏ:W˛ƊëƆ҈¨ǹϱ',
                                                                            'value': 'ІɁʞъˌѠȠϤȹТ϶ΥӯӋʪӐЃҐƽьЁԝȺѿóҞŁТłӀ',
                                                                        },
                                                        {
                                                                            'key': '\x95\x88¢\\ŜР\x8a\x92\x9fήԡΒ\u038dˇʓ}ΎƤˡƻӇÏϸ\x87ԌĩѬԨHԃ',
                                                                            'value': 'îɈƛΈϤ?ĥѰ\x83Ҳ҅Ɩʪ``БНʸͻΐˉҖɪǖʪһL[Ʉķ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ɺȩĮӥÊЃ)ԠϱŶƓʟЁҹ·ʨˋǥŉЭϲɖŕΖԣѡϼ\x82НŞ',
                        },
                    {
                            'keys': [
                                        'Ѓ',
                                        'ΕÚȏ˟ðŏȃƋԊэϒψƱҲԞƺʘƸԉʄԣ',
                                        'tƌәΝĞτƖǅ҆ƖîϙӘ\u038bʧфЃҽqė\u0380ѫӄԇǖʢĈ',
                                        'ӝˁʯΓ',
                                        '\x83H;ĺ1ΗїǂϋҫȇВҳ˄Ėш`ƏЗ',
                                        'Ӓ͵Ƥ\u0382ǰʾш¡ҚûϚǈҡҐǴˉ϶ѭǆԡÉ',
                                        'ΜʤˑʺʹʿôυÏ',
                                        'šƥÒӌΝѦ\x9aԈkȐʐʠѳ\u0380uҽϹҦӀ҄Δ.ԃҦöʊ\\Ӥ',
                                        'ʝʂԉ˽\xa0ȓ',
                                        'ЊʥΓǌЍə£yΕȚˇъ#riҲˆƔŠçβ˺',
                                    ],
                            'event': {
                                        'target_id': 'ѵȲϜҚɔϓȭëǱԉӠ΅ңѥБZśķƿł_ԚΔŔƼ\x83Ċ¬ԄN',
                                        'parameters': [
                                                        {
                                                                            'key': '\x98ӮΰđϮҷʹҤƻАӝҖ˫)ɃʸāʹŵҎƀЩǾӓgȖg҆ΕĤ',
                                                                            'value': 'ҟӡȾê®ԏəԝҸ³Ƹ˯ǠɼΌҁ¸ȦnԄ×¡ѕʖƁʅҪЎɐɐ',
                                                                        },
                                                        {
                                                                            'key': 'ǳԣѿϏŎӪĴКăȧԢ/ƞǐ\x86ȜēɯƛҝԞ\u038dʹpħѸȢƭɒ҄',
                                                                            'value': '¯ǲ¤ȈҌҠM(ӓ\u0381ρϻǗ˧ҊЌϠǔːĭƱȡʴ΅Śʵ\x85čðɯ',
                                                                        },
                                                        {
                                                                            'key': 'ɋҭͽǔCʛîԑѕ÷Ӹ˪ɛȴˇ§έɼʒ¨ԋνƣǫũæǭʉ˧ѝ',
                                                                            'value': 'ësɥƢԣǏŒηƗΙĭũı$ӊʧ¯ÂǷɖ¨įȣΦɃ\u0382ˇςӕԡ',
                                                                        },
                                                        {
                                                                            'key': 'Ѡƅԑ¦Ǌ\x91ȊϠИȾęЁɎɉȍȸһ>ѮλұҬ +ʯМӯʰǮԎ',
                                                                            'value': 'ŴŘΘóʵǌΔvƺdŚϿДԁƥĖʼҋϴǨʾӫкшŘǑϼ˨Ζą',
                                                                        },
                                                        {
                                                                            'key': '˘Ȋ˝Ьӄaȓɧ\x9cԞ˭5\x8bэťĊщʀҴҫʌȱӡͼöķɞ',
                                                                            'value': 'ʲ%ЪɓԦҨǱ6ϩnҺȡϵƿźʪȸĤǲΎƑɞмȳȭĽȄÕvԠ',
                                                                        },
                                                        {
                                                                            'key': 'ɚʵ8ȉı´ʓĒӁИɗȟě˥ЭпƳbwϚǈƝŦʐ\x9cɌ5Ԡȿů',
                                                                            'value': "\x84\x84ŕˠίɿáÌǗӺřťЙһäɗɡſʫ҄ίȲ'ˀЎЖӄŐÜʻ",
                                                                        },
                                                        {
                                                                            'key': 'ԅϞѫԧκ¿ҘНωƞϠѷԣŸ˃čŃϾ',
                                                                            'value': 'ӎ»ƖɑȢ˗\x9b¸\x8cŭ¿(ӯоԝƀųōëˀɌЌ ƙʝˋ\xa0Åɧҫ',
                                                                        },
                                                        {
                                                                            'key': 'ƎДɜɞ±ԉȂӸˤ˹Ӄзҥ˥Ȼ+ɝӟeҏÀ\u038dÅӇѓƗŧ¡Ԍƣ',
                                                                            'value': 'Ø҆ɘÆȎˋԡϚƨÝƊǂčнɴˎɁȞĴ@ŶƊψӳEƾͶԫҼԀ',
                                                                        },
                                                        {
                                                                            'key': 'Ӭĝӯȝ\x92ʙĦƀЀЉϋX˺ćɒv4ĲѱӜйʷǂԪĚөиȻԆʘ',
                                                                            'value': 'ƻСȗӨ\x85hԔĢИͲĄԚϒXšЮϒśˍrʫѠ',
                                                                        },
                                                        {
                                                                            'key': 'ƽƓΥΧҶ#ċɛǢԏѯƬǁĥ}ĮϕѹϫԟԡĂіéҵЃȚϊįÇ',
                                                                            'value': 'Ȧ|ÐɁĔ|ӒʌӑȊԢ>ӐbϒɏʊӨҍ˞×UȪԂгˌҿĲ϶ɭ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'KŶżΉƶиɛǰįȬüΊԮϢǥϯÚдȹ\xa0Śќŋʣ·ΣLϋѧ\u038b',
                        },
                    {
                            'keys': [
                                        'кǺȏɃ\x80кf\x8c˜ĎК˘UɗɷɧʚȠ',
                                    ],
                            'event': {
                                        'target_id': 'ȸn˂ϩɣŤgƇЈӀƇƍԚɺӥЏŏӻƚәРÈѺǿŪ˷ȼìӠɽ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ǣĊjāƳ8[ð\x92Ȁ³',
                                                                            'value': 'ҺƔѸҏӫǙòΰϨΐπċǉϭȍćĆńωȀΏÏө;ɻ\x83Ʋљԧh',
                                                                        },
                                                        {
                                                                            'key': 'ˠʵ˺ȴǕʏȅ\x9bë(ʐӅқԋ´ԤӠǭӷɯǗШiдʴ҇ίԡҪ@',
                                                                            'value': '}¢åΥ˻Ұ\\ФĢЕȒΏʅӿɵҭʭ˥ȶOԈÔɧɌʔȻϐɸʩ=',
                                                                        },
                                                        {
                                                                            'key': 'z|Ԃ\x86ȐÞж|ωJϦȟԙʻŁѤȥɶΧ£Ͷì˃đÔȞŵ',
                                                                            'value': 'ßŽƇѳюʘĞĨ³ŭЩsϿ\x97ӵˊԫҁ\xa0ǴѴΔΕűѰ\x8cҎʈңX',
                                                                        },
                                                        {
                                                                            'key': 'ˉ\x8eϽԅɘԭņӕĖШûНĹʁԉϯʶ·\x80',
                                                                            'value': 'ҢŀǣЕԩǬϷӠ҄ϺºćΜђͺǨΈĳ$ŗƮƴ\x86ӋȐҐ©ΏƑʜ',
                                                                        },
                                                        {
                                                                            'key': 'ϢԨ%άҝɈ\x8dĲҭοȵǪӫő%ÌÁ˩ơΘʭԠģƠмƛǬɣӡґ',
                                                                            'value': '˥Ԅ¨ ϔ˜gέԮѦ9ʋͿϢt3ȵȪ˚ўпĊ8ҏҭРŮŹΙԦ',
                                                                        },
                                                        {
                                                                            'key': 'ŒϚ$ΊСĽΰѺ·πȂ\x91ѷѤ»ϖӯӃįΏϴŅ҂ǉĨуƴѣƈҪ',
                                                                            'value': 'EХΤŲΪǑԭԦɞǆӱżӫȦУҰǍπМԆƵOʼєǓȤїж~ċ',
                                                                        },
                                                        {
                                                                            'key': 'ċ϶ƿŤВ˽ŧ\x9bȩœq˼¤ăĆэҔĢ˓',
                                                                            'value': '˰\x7fŐŘԕõČ˸ÎɵлȧƗ\u038bҝҜȲǷɋ҃ů҈ӠѢȫѹƤхˑĞ',
                                                                        },
                                                        {
                                                                            'key': 'Áӭ«ҌɅͰεκɻƗƯʗ˝ˌϷĖϤԜȡГ3ɏτʌєûʎєțǍ',
                                                                            'value': 'ɯ\x86жÆʩðʌїϮʨ|Ѻ҇ИďΰĿԙĖĬƵ\x95ϘҔEѬʹӯм\x92',
                                                                        },
                                                        {
                                                                            'key': 'Ż¶\x8f\u03a2ҝӡÊԛǖɲĥáҜѻ\x9eƨ҄ԁ',
                                                                            'value': 'ˀŚӆ҈ϥĨưӤv@ЗПƈ¶ЎP˝ӚĤ²šŏŐ\x93ҹэ\xa0чƑÝ',
                                                                        },
                                                        {
                                                                            'key': 'Ҭĝҫq\x86DԤɗ˵ѹĸQҭђƯ]ԁѳ\u038dͻŧǆI[ѦН\xa0ĕɵī',
                                                                            'value': 'ɝȯ\x93$9ӌӁ^˅ѳґѧЮˎ/ѡԢŽΟuòɰҨÚøȏԔɗκѮ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ʽЙĀ\x9fӟǝҀĿѨÏǫ˝Ӝ҉©Ԥ@ǹȨąêаϯʨӭIɠͼ9Ɠ',
                        },
                    {
                            'keys': [
                                        'ÔӼҘĻё',
                                        'θЯύ\x98_£ϷɴÐĐS˳ƣмӌˌ[ɉǌԥ',
                                        '\x85ԨҎ\u03a2καԇȺϣӼғĹɜʲȇǫƏӜͳʲʌ',
                                        'ûјҶΡǃ˯ѦЫӎͰϞ7ē\x88ęĝ\u0382äʶ˼΄o',
                                        'șÁ·Ӥʷǳӡ1oȖÎ\u038bȩТȚ',
                                        'ǛîèǱαȔʟϒɭŗ',
                                        'ҌяSҏƾȘ',
                                        'ЏʜԐÉǅѝСȗú\x86ɏѴīД¸úє҇У\x99ѾƣʬʤÆ¹åÃŤ͵',
                                        '2ѡöŅӿͲƃʔЋӫʷȝˍӵӽîИ\x86ѡ',
                                        'ԩŜà;ǽíԩƓŇ',
                                    ],
                            'event': {
                                        'target_id': 'ɖȢɚÀɠ>ŦͶӱƒȾЉȏɊвǐðǜѺdĬЩϙ<ȝ=īÕƻĘ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ԔИǬԫџȭћ\x83ԠύϪӍӃNȺƙѿηƎ',
                                                                            'value': 'Wпª,\x97ÄӤăɖƋʙțȤҊϾΣŐЭŷНȠųƧ˥4ӲĬ.ґɞ',
                                                                        },
                                                        {
                                                                            'key': 'ʩĬ\u03a2ӎʗʲƣìČͰЋŪʎśҖʜˍϴʔҘƟѭјMɦʋŊ˗ǖҗ',
                                                                            'value': 'ʔŢK\x85үѺƙǈŖTW\x9b˵ԖǦʹЛÜ³Ԟ¯sÝíƛĬϿТʧӠ',
                                                                        },
                                                        {
                                                                            'key': 'ǩ\x88ª"ѯπЄоз\x9aȣԆȠ¹ƾ\x9d',
                                                                            'value': 'ОǲɃȚɩȱƪ]ȽóĕÔˣϕȣԬПӪ˛ĎǷÿȟʤӼҷȑùÐί',
                                                                        },
                                                        {
                                                                            'key': 'Ƃ,ѫУӰĝÝӗƅюȲӼĪʱʴ<ΆĸћӨǮŝìñӀҺ¥ǖͰԅ',
                                                                            'value': '҇иҼ϶İҲХԝӹɬӟԎ=ӄŨã˶щ¿\x93цшǴѡЮĺӡьоā',
                                                                        },
                                                        {
                                                                            'key': 'ѷǵӧǈʋ|ÎӇ',
                                                                            'value': 'ћǬŁʪĻӣkԠυѬƶƴҞđìɄĎȕΏǆ\x80ѴVŚ<ңΖƟ˖ƃ',
                                                                        },
                                                        {
                                                                            'key': 'φԎɷɬǅшʳϷʨΝԜɊͽŝāԚ˩ǚԤ[ȅϺԭĠƥʟ\x83ΝŁѦ',
                                                                            'value': 'ɎϏƳǃȀһƙƄΫl\x8bƶʽŚƤĖƝЭ_˅Ϛ˺JҬǶџʱ-¿Ƌ',
                                                                        },
                                                        {
                                                                            'key': 'ђPшʈȻӕҸġʯ΄҅ĝɱƒČœŀэғΛ5>¹ĊΆCеʫϕˉ',
                                                                            'value': 'ȏΥ«ԞТ×ƘŘɨ˝˒ҽFÄcƋΙъŅѭ˕ƈѝɛΘϦȿʽҽі',
                                                                        },
                                                        {
                                                                            'key': 'ԠӠшØĐ¥ǭƷϘќʶ_Ă$í3?÷ǳћɷξǍҾƲʟăѿˌ\\',
                                                                            'value': 'īԤɠŘ×Јɔ˧ů҃l˗δƪɩȠЀʈӳĉˤæħҨԜίynϩǡ',
                                                                        },
                                                        {
                                                                            'key': 'ξȎϋ΅Ёï\u03a2ӱæѐƴҽȚþ',
                                                                            'value': 'ˈǈљqԔ\x86ӲLҲĥТЌħҼ\x8cʁɦɻˁɑɳ°¬ǧ¼ϗȎôԄí',
                                                                        },
                                                        {
                                                                            'key': 'v|˶ϜΆŲĶŹƚfқҫѡʬvƍʽ҄ě5ǕƁΚƃдϩЕʝ\x7fć',
                                                                            'value': 'ȬɔΕʹęŦΧʚυȩf˜ЕҸ˰äώλюĒľhμέэèϊȯωɂ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ЀΠѠһ˂\x8dρ΅ÑԙҾӏǥʫ÷ǷКɷʥƎӆ¶ƒ»Ϫ±ӾɘƔҾ',
                        },
                    {
                            'keys': [
                                        'ЀӊǞҶˣƽəǒ^mӏʃ.ǃӛίԋˑԩԑ\u0378ͽɅЇьǛС',
                                        'ҫʾǫЏɲ',
                                        'ъϔ\x99˃Ĉх˒]Ɵ\x8bϨωϵƕƍ˪ҿԟā',
                                        'Ⱦұ˛Хùɟκј',
                                        ']ώ\x84ʗшѲъ',
                                        '$\x94ǖƇȥόӕ\u0379ҝҪȰ"ŰИтťГkї',
                                        'ϓĳ\x86ύґѧτȭwSƁȜҞ',
                                        'ÿОԣϕχ\x9aЗ9βϚ˛гȵÖѳʇpƦŊŀɡ1ŦфˤƜ҇',
                                        'ϲ˄ΚΡǡɄμɐѱҘƸǳ\x8aМӔîĒʗ',
                                        '\x9dѡӌаʀϫɌ\x9dбŝ',
                                    ],
                            'event': {
                                        'target_id': 'ȃǖҹύRХӴΠƖшяϣ9˥ƑǈĨʷxİҖÒǁŎΜǦзķϸȿ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ϜŭBʏҤÒȨ¹ҾǻƷ˗Ӽ!ҍӁԮˬȂȅǡ-ķөȡҽΰʛԋӟ',
                                                                            'value': 'ğÌʄΓϿĢ\x81ȯȈȠаȾȆ|Ӵ\x92ΙJȑÔϼǱʏŐνԟčѷϤȚ',
                                                                        },
                                                        {
                                                                            'key': 'ӋºˊW҅ʩɐӫV½˶ƜѻѦΩƔǭѹŪÁÌÿҠϘұ²ŨċȐѷ',
                                                                            'value': 'ɲϯKȘӗǓȤsЃƠїÃ˷Ѽ:ԞJпʮԪÈӫʌòДӎψѰ',
                                                                        },
                                                        {
                                                                            'key': 'ǐōɁ*ȦёѯĵѢ˟άΙɨþˑӞǴ\x96ĪƚăȴƲˁ˼˥Ǿđ҂b',
                                                                            'value': 'ėӗĤЎæƹѝςԔɝʼƏѬϔѿɗuԍʘԇԡέϥ҆ЋǁŰ҂ϱј',
                                                                        },
                                                        {
                                                                            'key': 'ǷŎϯ˺¨¹ȜjħʲѥǫǙҸˎ˗Ҥ¥ÙҤʭŖǣĆ\\Ŕ˩ũǳ°',
                                                                            'value': 'ÌǸцzϓªǃԊуɄ¦ǜМɐ[ɊΚѡčӋǵƨёлǀʹоԈЖϋ',
                                                                        },
                                                        {
                                                                            'key': 'В˰Ĥ^Ѐ½ǵ\x99ǊǓҍͶ÷ӰѶȭɉʱϧŎΓȏϋʵÝǸӜҊόì',
                                                                            'value': 'ʚςÞӛȜӬ¹ѾʗůҝлщŠ®qŴŚΦĭƘȧ\x89ĒʗӺ\u0379ùӟԂ',
                                                                        },
                                                        {
                                                                            'key': 'ɗґȗңϩΨɨE\x87уœɄƭ¥\x90ͷʗ˖\x8aҴ',
                                                                            'value': 'ѹнĝʵΠĭԦͳԉԦǯӲɒŒ\x8dʶҶьęÓҀƵɭͲџɨʹѕӒѥ',
                                                                        },
                                                        {
                                                                            'key': '¼ʂӁYÍӀØѵȉȿɸvͻγ˅ԉѓɈɵǃƍʊʹϿǟÏ±ØA¦',
                                                                            'value': 'ыȮӅƌÖʵьΟŪ=ԖȝЅʀ~\u038dҺԐɝÑƮʣϵσрʲȪ~Ȝћ',
                                                                        },
                                                        {
                                                                            'key': 'ƐĀĔҐɌӶıƪɧЛжѱĒÅъӓȫͺ\x7f˷НӜʜšǜʢĎaÆӆ',
                                                                            'value': 'ÌǄCԢίPŇ6ѡίƧξƵӝͷEԑƅЁҧē˖УмӬûƱĨ©ɯ',
                                                                        },
                                                        {
                                                                            'key': 'Ͳš¼ӴʾǞÀ\u0381ʶ}Чя˰ȒԇjԩǸNŬϩҶϡΞțԞсɦJʛ',
                                                                            'value': 'Хɷíѡ|ʮ\x81ʈjɷɎ¡ŨÆȋʁǊҒΧӾѭńƹ˭řНə҉ħƲ',
                                                                        },
                                                        {
                                                                            'key': 'ȸѬҴϼżѧȅıŖÁρсƟЈ,gҧһýʚǨΘЄДŐЫ*ĝѳȝ',
                                                                            'value': "ǻύъ<úŷɑōƌȫ'Žа\x96˔ÑƆ*Ѡȕs²dɍʭƑŤȚȞƬ",
                                                                        },
                                                    ],
                                    },
                            'comment': 'ϣY|ӨÉƻưӝхϯ6ѹ|Йɠы\u0381ǉӸŅĹįŭƭŷϫӄЮđŎ',
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
                    'Ӊ',
                ],
                'bindings': [
                ],
            },

        },
    ),
]
