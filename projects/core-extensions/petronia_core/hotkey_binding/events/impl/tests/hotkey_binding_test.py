# GENERATED CODE - DO NOT MODIFY

"""
Tests for the hotkey_binding module.
Extension petronia.core.api.hotkey_binding, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import hotkey_binding


class SetMasterSequenceRequestEventTest(unittest.TestCase):
    """
    Tests for SetMasterSequenceRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_MASTER_SEQUENCE_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.SetMasterSequenceRequestEvent.parse_data(test_data)
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
        for test_name, test_data in SET_MASTER_SEQUENCE_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.SetMasterSequenceRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_MASTER_SEQUENCE_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sequence_type', name='SetMasterSequenceRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='SetMasterSequenceRequestEvent'),
            ),

        ),
    ),

]


SET_MASTER_SEQUENCE_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sequence_type': 'sequence',
            'keys': [
                'ˁ˰нĤЁʩ˓ӾŔʷвϰʄ\x8cɅɓ<\x87ʐʱʚԟͻƹԤҽΑ6\x7f',
                'ѭӯǍ§ϾԍĿWʳӶMʼӯшӒˀʮԗΙɵЅȋxɎ¾М2Ĭ\x8d',
                'θĻƧʝɥσǳЮɴ\x98ňЍЯȁ¨ЋҩԫӬԚ÷ΔјǍ¤Ìǣ',
                'ƙΚQũĻҽÉ',
                'ȇlĀâ\x94˩',
                '}р_\x95 ЍąкЏ',
                'ưҘ',
                'ΰӸͿź\x92ȢϟΩǱìRoɄǷęƓɲhȞ\x97ǝԔùΙԏeӛ',
                'ͺҤɇҜѩœ\u03a2ʄ҃\xadӓɭӈΣʇ\x99ϕЧȈħȨԗ',
                '˗ΔΠŰγИɈ˰ʋĎõɰԠ\x9eѮшғԝ˕\x8fŷȊҶӀwҴ҈ʏ',
            ],
            'comment': 'ЖΚ#˔ŷѓϼȄϢǆЅTҚ\x85ȲʹʠәĕǌɡʔƳöϙ˞đˮ\u038bρ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                'ʮ',
            ],

        },
    ),
]


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
            'key': 'ѦȾДɵЁшɹʥhѠðȅёӖʾǠϓəȋųšʄûÖÃԆ©ӕэǻ',
            'value': 'ɿŸ\x8a`\x97²¨Ɏ˸ϨǹɓqĶΜ¸ǸԏěɿΖǸɋ˛Ԫ˺ђҞđѹ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': '¡',

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
            'target_id': 'а˨Ǹ#ƪȍɑεƂ϶ƻӪī§ϞΡҫêưʬ_ҡʛҙE\x9e\x865ΨÊ',
            'parameters': [
                {
                    'key': 'Ӭӿ»Ŧź;ȷƖñįxӠ+Ȏ¢ɅԬƶǯɭ\u038bϯ˨yÝԏƼґж\\',
                    'value': 'ȂĎīƞʆ2ƢԖƽȤеƉΩǢɊķγȌ:~°ʻǢ˒ȱʸч˵dʒ',
                },
                {
                    'key': 'ÐУ\x9bϣɄѺцťǶŉй?v½ϝƫʂԛēˇɔѾуаѽBiȷԂЬ',
                    'value': 'ǔύƀɞRȚƳz\x9eƪ\u038dО˴ӏǔа¾Ƃ.ȧӍϼ_ρϲԬƟʨѨþ',
                },
                {
                    'key': 'ɗҞӿ ɔЇɄЈԆĶúIњҨ˞Ͷ\x91çΥȷ0\x96ͿˈˠϹΘҢҐȳ',
                    'value': 'ưЖ{ǎùЇӋjěϗԡȠɀ\u0382ʄǚčʝ˜¼ҭǛϼƲӽêǁϼȆˏ',
                },
                {
                    'key': '˳ǸƜЬ\x99Ńǁʅ˚џӪӄ˄Ҟ»ϱεȶʱƴ¹ǕћȏʤѴʚωįϬ',
                    'value': 'ΝN˼˹ƧʹɶÉҵˇʑΆо®ZǴȗйЄ϶ƚΟн˺ΝǛΫьίĬ',
                },
                {
                    'key': '"¶¶ĳɍʁЈƶĐЊɵ&Õĕ©°ӕƼ[ơќn\x9cĂʀɇ͵ԦԞͰ',
                    'value': 'ϱIˊǓġϔѤϮŐЩϫоκԒά¿˪\x9aӞŨҟԜǲМϯwҙ˚ϦҐ',
                },
                {
                    'key': 'ҌѠϪͿΐŸˀӒүɩà˅*ӔˁɼƂŶŠƎʅɜ\\ϛĨrӋ\x8eыā',
                    'value': 'ʅwӊҎͼ}яμѮƒƌӤӐΒȣÞʟĻˆӫъǡǋ\x8cqɪє͵хԘ',
                },
                {
                    'key': 'КċʡͶʉΑӴҲԭȔ.ȱìɘӥϖȭǚ§ƓʤřĄȢɕЖ҂ɤǘλ',
                    'value': 'ˬҬŌʰ\u0379Ͻí¥ҧėÑȝmԞ҆Ԯυђ-ϰ\x81ɿԬŅ,ϕӶʉȰˋ',
                },
                {
                    'key': 'κDɉƚυʭș˦҆ʹ҂ԡ҆ʧЕˋφҞϚŷŭϕҬòъН=ȗѼȋ',
                    'value': 'φʢìѬI˕\x86ǎ˥϶ѣϑϠ)Ԝ¹őĒЎϜʪŀɟӫȏǗǟӸ;П',
                },
                {
                    'key': 'ΜѾIҳα~ĐОȍǎÒǹē%kȢэǁɵԡƔҥϱ˨˭ħİϼę',
                    'value': 'υʎ\x9cɝӋѦ˞ɴǅ<ϐѢ˥Ҁ˘˓ҝĆԘBԉӡŴȃȶ\x8dǂǣͲʔ',
                },
                {
                    'key': '˃ǙͿͱȯМðϩӴ\x9fѷϗȨƌʫͻϲɘòP`CƐ',
                    'value': 'ѧОяΪÒҹˉԮŋϐÉÈ?Ėҷʎт\x91͵Ҷ~ʳ½iʼµǄъώ\x96',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'Ȁԉː¢{',

            'parameters': [
            ],

        },
    ),
]


class BoundKeyRegisterEventTest(unittest.TestCase):
    """
    Tests for BoundKeyRegisterEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEY_REGISTER_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRegisterEvent.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEY_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRegisterEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEY_REGISTER_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='BoundKeyRegisterEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='event', name='BoundKeyRegisterEvent'),
            ),

        ),
    ),

]


BOUND_KEY_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keys': [
                'Øџ\x9d]џȱӳƀćͷįƝ',
                'ˠ¥ˬώЪȶ\x96\x98жчǃĮƊ"6ӣDңҭІˋ',
                'ӝ\x8fϏΌBȰүǚ\\ҀƗπǉӸю\x81ǐ@ҨƩ',
                'ЉǾʮԧʏУÔϢĸ<бѶюώΈй',
                'Ё҅ˇѢҹǠҒɍԟӝ ȕ°',
                'Àįǹ!Ģɻљůѐϣ\x95ѯѼȎê;\xa0ӽʸĀԌƝ5ƴ',
                'ҸͲ',
                'TǲЯʇԖ˃ʻȽƼŲӖϚƉǉǕMʿҰǪƘвϑ',
                '\x83ӐЛʏΖ',
                'ě\x90ƶƪ˩ƅ}ҔǑ\u0379',
            ],
            'comment': '˳ʳҽҙȪϕĦы\x90ӊʺΥyťȍDıҙǔӏɢvľǹʌȨƴ˫οϱ',
            'event': {
                'target_id': 'тʾѻɃІ˰ӬΔΚ7ҡєҢ ˺-\x8cː°ǸǎQĕҸϳƴήЊϷϽ',
                'parameters': [
                    {
                            'key': 'fȐӕаΧÍӟȡθCӠǽígҨn÷ǝԍԝ:ύķӡͽӁɡЂ\x8fͿ',
                            'value': 'ÅϨƋŀɗ\x91ο\x80ЙεǄȑлШӉԬȉӉǽԄӻ\x89ԕ"ˆãҨΓµȹ',
                        },
                    {
                            'key': 'ýBǞñĲʍѸɻНϠɳƊʰ\x9fӃBÚɛəȯĸƳūȡθ\x89ӱȁѝϏ',
                            'value': 'oƵɞҏǣɦƑèҴʜлſǋκÎˆϾĉïӠƄʘɼǉ<ԒȟɥϽǾ',
                        },
                    {
                            'key': 'ƤÈôΐԩǥɠԍʏĴƮӕVˡ˭ϼȣФÚЂӑқѤˢͰǥ·',
                            'value': '¿ԋî¿϶qĔçѵǸǚҥϢʨpΕԦ<ďŀȴåĥŽҿ\x8dǡȡħʲ',
                        },
                    {
                            'key': 'Щ¿²ɂťƋЪȱ¨ÀǤȒͱѧԩɱЊeıӞŴ\x86ɖ˸τӍƻɏ˪ԑ',
                            'value': 'µʷƴˉĲǽǃÚӴ3ͻ\x99ͼrͰЅĦĭÙĶˣȜÆ\x9a.ĄҥϥҀǨ',
                        },
                    {
                            'key': 'ҙŴʍѐϲίҷ\x97˗¢\x81˺Ѵ|ˉȔӋѿΫñсƩ8ÓˎξѵҼҹӾ',
                            'value': 'ĵÌĳȖѨ|˯ѳə\u0383Ƈˎ¾ѣƠʧ\x83вԕɯрȪυÃǼ҄ɀ˞ʭԬ',
                        },
                    {
                            'key': '˜ˇԒŴƚƪθǤϡ',
                            'value': 'ԊĳșͰ\x9fŤéĨЬԕŤѤӫć_ӁѮƭşȂǑћȒЉɄ҉Шʘԉ¦',
                        },
                    {
                            'key': 'ы-',
                            'value': '·ˋϐѤŞΕҹęӕҋӱЂ:ɞё5ƼȅѧƯʛúԞŘұʕăλԭҙ',
                        },
                    {
                            'key': 'ЋǡK\u0379ȎϣƱϬɻΊѤƦέʳ҃ÇɗÓ×åʋϗʅ¯Вˁ',
                            'value': '½Ңûǐ·ԤӷϜӠŝ-ʒï˟ҥѦјΨ\u0380ʉZFǞ\u0378ӲýԄɳ˝ƒ',
                        },
                    {
                            'key': 'ΓҨΰ\x99',
                            'value': "ľϑĺѰˤˢȖȌX\x99Ń¿ʓε˯ƴ%Ҧ˃ɍǛɹӞƹΆ'ƶ$Hư",
                        },
                    {
                            'key': 'ѪVȲͳL˴҆ϓɻʌ¼ǥȀ~Ȑΰǎː$`&аԏǁȅŮ\x9aɴƅ˃',
                            'value': 'ˉǙϦхԅЭvɛˋɑȬҷȷΆͰλ\x87ͻȝɆёмҿŨϻÿԞŎӬƮ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ӗ',
            ],

            'event': {
                'target_id': 'ӸΔǌɉ¼',
                'parameters': [
                ],
            },

        },
    ),
]


class BoundKeyRemoveEventTest(unittest.TestCase):
    """
    Tests for BoundKeyRemoveEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEY_REMOVE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRemoveEvent.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEY_REMOVE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRemoveEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEY_REMOVE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='BoundKeyRemoveEvent'),
            ),

        ),
    ),

]


BOUND_KEY_REMOVE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keys': [
                'ѧĊZЯʍѯtƟϾυńӈ\x84πɞÕ',
                'ԣșǋȻԄΫȯͻнΊýȋѣ',
                'ɴԠљҝόƤ\x8cƄҊ҃˭ϲΡѨŪӑ',
                '¨ƴӓκҵΥNɫɕ˴ӟ˰Ҥ[ħ˧˙ŬσŋɆ',
                'ҹӢ\x8dý\x96Ыʣ˨ԧăЯα҄ԕ\x9f\x86"ǛL5ʸӻǿÀ\x8eȏĢХ',
                'ïξƙѓdǙʏǟѯ#\xadƼӍÙ˃ӏPKθäɦѠΦϢɛџфο"Ȕ',
                'јͰ\x95ȇϪů',
                'Ǎδčƨɀ˖ԁӶʱ«',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ї',
            ],

        },
    ),
]


class EventParameterDescriptionTest(unittest.TestCase):
    """
    Tests for EventParameterDescription
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENT_PARAMETER_DESCRIPTION_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.EventParameterDescription.parse_data(test_data)
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
        for test_name, test_data in EVENT_PARAMETER_DESCRIPTION_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.EventParameterDescription.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENT_PARAMETER_DESCRIPTION_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='key', name='EventParameterDescription'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='EventParameterDescription'),
            ),

        ),
    ),

]


EVENT_PARAMETER_DESCRIPTION_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'key': 'ƕ˚ÏJ˷ȨɜÈ҄ŀğ¸ŜɐϊːʥŭÌЁƣà˼<ԉǅƁ',
            'description': 'ϡǩEΠAǺWǸÿ˅ΰļϣРŸԏƏшȬM¿ϳǼǥӸӝİ\x81ǻɌ',
            'default_value': 'ǚʝͳũTƲѥɁ˒ԨӱȧµÑN˄,ċʹō6Ӻɬɟʚȃíúԥχ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Н',

            'description': '',

        },
    ),
]


class ExtensionEventRegisterEventTest(unittest.TestCase):
    """
    Tests for ExtensionEventRegisterEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_EVENT_REGISTER_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventRegisterEvent.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_EVENT_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventRegisterEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_EVENT_REGISTER_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='ExtensionEventRegisterEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='ExtensionEventRegisterEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='parameters', name='ExtensionEventRegisterEvent'),
            ),

        ),
    ),

]


EXTENSION_EVENT_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ƈԭЏ\u0379ЛɠˉȩӝӇΓѲƄЁѤϸҍĐ%GʚЧȴŔԨÈżӆŬϮ',
            'description': 'ψSэīʙżʅѵѳƊƥǹ\u0380ҡnĨ˸ÂԌríӜɦʦŷ\xa0ҵKΡһ',
            'target_id': 'ҨȧƿԊ\x89Н\\ʺȬÄМϴϩԀĦƥ\x85҃ЙrϏ]Åѵɛ',
            'parameters': [
                {
                    'key': 'ȒȚŗǒmЇԎđӜ˶аēŬ\u0382˘їȄҭ|ȢɉǈŕƧŐοϲƊ-^',
                    'description': '°&ʑɺϒЍ·ɻ҂ƾǕõƵѐҼOŹϿÏn\x84ԒŐȄƷєÚψǅĨ',
                    'default_value': '¡φӪͻśZƠly7ϽѤ\x85˜όɥ˶ǥԠԤχΣYǥȵ˗ʵěĠʁ',
                },
                {
                    'key': 'ǾÈ˖ʋØ϶ҰƞĩǡϠԘ˧ĀӮ˫ȉȂæиαΆ\x90уғÊӢȥ²ı',
                    'description': 'Η´ŹԖЧɍɓ7ӻhОǙȨ˥Ь˻Ӫ҅×Ʉǧ]˴зōʒωдśŉ',
                    'default_value': 'ΉϭɯæȰɵũĥҔϘˑʄȝʟћ<ȝØǢ΄ȈȽ\x92ǗǳÙɓϼÎΈ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȁȣľ',

            'target_id': 'ǵ·ϐÀđ',

            'parameters': [
            ],

        },
    ),
]


class HotkeyFiredEventTest(unittest.TestCase):
    """
    Tests for HotkeyFiredEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in HOTKEY_FIRED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.HotkeyFiredEvent.parse_data(test_data)
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
        for test_name, test_data in HOTKEY_FIRED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.HotkeyFiredEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


HOTKEY_FIRED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='event', name='HotkeyFiredEvent'),
            ),

        ),
    ),

]


HOTKEY_FIRED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event': {
                'target_id': '\x8dǁĭȰѳКŶȻ\x89\x85˻ǬҀƍŇ2ưӆĻΑԋѡŅVҔå\x91Ŵȩχ',
                'parameters': [
                    {
                            'key': 'ɾȊˣԅ˵4ҹ,ċˆȹǴќɸωŊėɆǘфǗӤȞĀşӎҘКȤ˛',
                            'value': 'ċ¯tҩќΨцЕɠԪϲĈԜίӿϵɓƵ¸ȘČďӃȈԖȫÝҟƴȞ',
                        },
                    {
                            'key': 'ΨľͲ\x9dÁƊӍЧ¶˽ԪӓѼҶΎɘĻʼʐɽˇϋɌʋɩ˹;ƴЧǍ',
                            'value': 'εԔ®ɱų\x8aҧάȭĝɠпÂȸӘƽ¤ǡμԆłĬΞĺЉҷ}\x9bͱƫ',
                        },
                    {
                            'key': '\x9dȌϜ·ŅӠϟ|ŒǗ0ϷУ9ɿΙЏÜeѩėŵӹ˺ǳʹԇúǻϞ',
                            'value': 'ΐKȊЎʵеԉdӄ±˃àʨLˆǜȐƤŴˉà×ҫŀǴμģűʸɿ',
                        },
                    {
                            'key': 'ɦzŢƻ\x9bȪƂsϫl\x9b¥ԥƈΕҽZйіϜǃŤҟ˟ǱãñƲłƟ',
                            'value': 'мÊ{ϧǈ·кȄŧУҺȦңҀс[µfʾļƩ\x94ÍˣǨΕʒnͷӠ',
                        },
                    {
                            'key': 'ƪУĚǝʒΣ¶ƳƎʞΚI˹οŢςĖɣǤфşъɎȠɖҦưĹʀϮ',
                            'value': 'ҲҒsҌҀӥȗҲėƬ˹Ń˼εѵΘɀѯǦŉʛʿǋҷīĺĀ˥Ýǭ',
                        },
                    {
                            'key': "ĹƯƜȿɉćЈbҎ'GÜǼŋ%Р§Ŋӊɷˤϒ",
                            'value': '{ͱͲʈρɢӆұɦ9ȡț\x95úîɤΡɟԒθȧɋҷ˼Ʋи˟qɳѫ',
                        },
                    {
                            'key': 'ӱɍrкƐΉ\x8c?ηԜІʄȋːÍô.ʭțӇͻӽǬtǃΗЎ¿ğɠ',
                            'value': 'ǤȒɗǴӦĺӆŨμƃρσԥҒȐБʥʀӇ\x96ȕЉɕ\x8eӨŵĞԄÒԢ',
                        },
                    {
                            'key': 'ϱ·uҨę\u0379ɤԙīɜơȟɖðԞЀº·Ѿъ˜ǰĘӖ%ԁШϭĄΜ',
                            'value': 'ÏħӫҴ҃ʑϨϴ҉îӔҀĄԘԟЇԊǬҚÎѭžűӻňӋӹȔҭƦ',
                        },
                    {
                            'key': 'Çgϻƿ¾4Ƒˍ#ϰԨ˶ɑŵƍƓȋˤϯϨѬ"ŋ¯łįɭƹýʏ',
                            'value': 'ϝѶз±ӽЮʬέ\x99˱ɭˤў´ƦǏΣԒȀȀ$ĴĦѢмɨʹǝǣЫ',
                        },
                    {
                            'key': 'ĆӨǺӖËɷБΥmˤϋфƄ˴ƨȼ\x9cѵӰȀˬѱє%άϘBȨήǃ',
                            'value': 'ΣӊʯɲҗӌǽvɵƘΛKҬgә«ΟɪðƱϨŻĩϵǞņdˌ{ӗ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'Ƴǡŀùā',
                'parameters': [
                ],
            },

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
                'ȖҲeѰϼʷƀοьϰџҹˤэԒďԥĮĳˤӢмиЦӏ\x98ђн',
                'ƵϏ&ÃŬoԂÓƚҢФ˘Öћjϼ\xadҧƊϋÁ',
                'ũŏɁǥɳЬβǒԎEĆ϶ȱѝʍЁÿѶΚбʙǸ÷Nԥ',
                'З˨ïƨĕʱӲˢēÛɫǷœ˚ƜԦϽʈʋ\x96j',
                'ӑØπŝƀ)¡',
                'ɼǷ)ԍΈȕƥǷɽѯ',
                ';ȸºØ˓μɳ˧ƭӷѩЫm5aӈʂïɢϝΗӦεʺǧpѹɁ',
                'ƈǗ˺еȒˡɛŃѽ\u0379ɸӧÆЌӟŗñǔõʯȨƞ\x88ƾ',
                'XʫǊ\x8fǒˁԉÅĝĮŖԨЭĻΎɓдʪӪͶúӇɬɢǹƺĹÄ',
                '\x96\x85\x96ɨǻҺӍɏʽd+Ë',
            ],
            'event': {
                'target_id': 'РОǄˮΟ¥ϗ¤ѪьAӎʿõқԌдГĺvƯϓѤĨʟˇ˦ƩҰ\u0380',
                'parameters': [
                    {
                            'key': 'Ѳ\x9d˖йŐſІϨϊБΧΩɶԭ',
                            'value': 'əҬ˱ҏΙƀԊŽӤʣЪȣξƗͿĵД\xa0ǁŹϻ2ûƟ҄;˪!јƥ',
                        },
                    {
                            'key': 'ƧӤǸ˻\x8cʵǂͳųͼҪȗҫȉЉӨȝÐʔþ˵ǒ',
                            'value': 'Ο£˅ʬҿÏ\x9aôȘQțԗɷ˚ϣώȈʑƣ)ɌёбW±ԛԒҿɴ҇',
                        },
                    {
                            'key': 'ŏ˷ΈɩʏΠǮԔ\x8b¹ӿTŏ&ƚЯЇÎҐҔÙǼƝԙƪԢÎƓ',
                            'value': 'ԩАSήʘΓï/ƻTǍTͼКǼɬˍ˔ϏҠŴӕśӈƹŘ>\x99Ͼɮ',
                        },
                    {
                            'key': 'ˌ~ӣɔȜ¥ѹƯ|àϏĻϏƪ÷´\x82ːЃɹɺǉЪÌЅω¾ʯʿɴ',
                            'value': 'ʙи¿ǟΓŁlәɱʧ§ʶɟұҫɅԞ%σȹѨġҀӄ¬ҋƃÊ\x88ɬ',
                        },
                    {
                            'key': 'ѹԮΠԩɽΨ\u0380ǀ¿aǶĘ°ǻƶ˥ȫ˚ϹǼ\u03a2\u038bǷĶϢӆ\u0382Ǆdҡ',
                            'value': 'ӮƝ®~Θ˘ҭКˆӪ\x84ϔұʎȠҨʯƗЩԇѩҶQҪΉӭ϶ʅȌԞ',
                        },
                    {
                            'key': 'ÊɠǘǉK0ĳǑҊƏѹ',
                            'value': '\x84ʳˀtΦǖέτ˽˂µεʻеǑđӑȅŜӥːǍПͶ4ʓ\x93Ǡ"˶',
                        },
                    {
                            'key': 'ϠÍЬǵұŹpĽəŧÏѾƻÌԞϞǸPƺѝӐŷцȁǧʆÐÓǪÎ',
                            'value': 'χЉԌŊ˱ҿҲƸÏĤɑͷғɆԟʦ§ɬ£ŦǸī',
                        },
                    {
                            'key': 'ɦʏȆ˄ǅАɦƍӺǤшɆÀĄ˅ɬʱ\xa0Ťɼ҅£ūÿӚʺ¿ҷɂȎ',
                            'value': '0ҿț˰ЕÉДð5Ԇπ\u0381ͲˢΡŠͱҼτ\x99ѹΖәēfѠǛɌƀƦ',
                        },
                    {
                            'key': 'Û>ЃҹƈòЈƳ',
                            'value': 'őӒԖŒĵҗӥƢӷƥiçͱUȗJԐżԎҧԏљÿй¦ɐȚЄſÂ',
                        },
                    {
                            'key': '˂íǪKӊӾƨӲȒʝ}®ČϊԐ¾\x84ӚҞЏyİЩхϦƥƔЁІҲ',
                            'value': '=хŘЛȑ\x83ЀŤӌZӒŰ˝ΆʶњǬűǯΗΌӞǌӍ\x8cԏϝȤЧÊ',
                        },
                ],
            },
            'comment': 'ъːѴȴυɹΗɅϹÄʙƩ%ȚӐ×ɦÎҘ`ǏǦyάƥΒˬ\x90Ę϶',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ş',
            ],

            'event': {
                'target_id': 'PΔξԐĮ',
                'parameters': [
                ],
            },

        },
    ),
]


class BoundKeysStateTest(unittest.TestCase):
    """
    Tests for BoundKeysState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEYS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeysState.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEYS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeysState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEYS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sequence_type', name='BoundKeysState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='master_sequence', name='BoundKeysState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='bindings', name='BoundKeysState'),
            ),

        ),
    ),

]


BOUND_KEYS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sequence_type': 'meta',
            'master_sequence': [
                'Φġďˎʵы\x7fƓȊӶŘɼĂңôΒđўН',
                'Ҫá3ɸŕåҙĊԆƬΜȭўɁĜÃĔʼǚΡ˶',
                'ˍΗϞġЁφϾ\u03a2űʳÇʝǚъϢ\x9a¦Ŋöчĵ˭ƽÕʛѸɡ',
                'ҸĀčҧ ®ɼƿǾή\u0378ҼˬīӞLȆȔːѳ¸',
                'Ϯīǫьϙ',
                'Ƕ¾ȅıҌӛÑιƽĨˮͿĖұҸԥ>шɵɓńɫØʄѼBҞUԓ',
                'ΖӫΑo+ɻ\u03a2Ί\x8báɠķǃΑσӼǙǤæ',
                '˗ŭ¨àЂϊˊ',
                '˜óȕÁŴɝјУɜьҋԉ',
                'Ϡ˪ьǓ\x8fʝΉ˫ɩӜȴƛΈԌ\x98ž',
            ],
            'bindings': [
                {
                    'keys': [
                            'ðý',
                            'ή´Ƨ¢˒Ǽȗҿ\x9cfʙȄɺԪëɯğҤԝщŖŇˏ\xadňː',
                            '^ЮҢ',
                            '˖ÜǼқӈɉДȽοǆʵŉώ',
                            'Ϋã|љļЦĚǰǤӪǏжŹεŗяӮo8ĺˢʷΩƄөҨ',
                            "ϝɮԢѤˇЈ9ťϹƢ\x91Ǚ'¨ɎʦВÃʃÒέѭÔӻ",
                            'ѫŕ˦Ђ',
                            'ГϠʀˌϕʲʄρҠǝλέɨˇnˇSʪǼԑñɸĜ',
                            '3Ҟԇǖj˴Αɴ',
                            'қ',
                        ],
                    'event': {
                            'target_id': '\x86ԁЋ˪ĶȷжˍȁψӰǶ҅ӷΘɂϕÊɤɗŜЖ\x94ȤҼфѬҭҪ˖',
                            'parameters': [
                                        {
                                                        'key': '\x97ɔκɴΦɆ˳ʣ\x86\u03a2ҰòӿʅȣɢѓʂȷЊү>РƯ˓әʞƩԎЭ',
                                                        'value': 'ªľіѰºʫƻԕȿJŬѡŚŪ=ɥƛʮȆÆҁӨЪхαūӰÐĎ˺',
                                                    },
                                        {
                                                        'key': 'ǶT\u0379ĎǅЁɘԫPԣџƤ\x9dΩǦͼǟl«İě\x89НȹͳѝȜǯ',
                                                        'value': 'ͱτ¦ΒыʹʽŇȹƺԜӵȤɌɭȲơȯԅҽʊӏƢ[HПԮ{Ғԅ',
                                                    },
                                        {
                                                        'key': "'ѻШ˹ôɪ¢ȐѵɈĊː\x8fҙ˔йɤǿ«weÓʛеЩöѴʴϪɗ",
                                                        'value': 'ZʶĬʂǔ\x83WӶŀ·ʠπРӃʃŎγҬҡ˲ϏьǄˌȜȢM>XΊ',
                                                    },
                                        {
                                                        'key': 'ӑ%ϰǋĨԤԣъĚѭï.rǻӖ½ӑʴӂˏʽϩǸÜƚ\x81ϼɮɭӥ',
                                                        'value': 'пϬԈ˳˥ȷƁϋȶʝ˲җЌɬȐѣǱʯǒˁJςɅͶ˖ΘɌ:Ms',
                                                    },
                                        {
                                                        'key': 'ҔǇǙ϶ԍOχɱԚþņԣͺɸϚЎčҰƚȅȨ#ϯôƽɿ˲ЄǺω',
                                                        'value': 'ыOƀĲѺȓœòûņԓĔþǮЍҢĄԬðwųɾ҉Ȅȝ7ʞŽҼʶ',
                                                    },
                                        {
                                                        'key': 'сԄїǓoѶƏɥȭƸЙͳǌˡºɱйċǽϸöӰƶй\x8dƿѓȌâ҄',
                                                        'value': ';Ѳƈ\u0378҅ΞƝǒˋΔƒǝɐѠƮ˓ѬϡŬǠĸƢɸɟʭˬЖŪԖ˖',
                                                    },
                                        {
                                                        'key': 'ʂvƩѧѱБйʐȣҽąәǽО˼zϥɇ\x8fӾ6Ǻ;!ʅԒ҇źБ\u0381',
                                                        'value': 'ýŝЃʌĿ\x9dˑ.ʤȻÍ˃ӴɳʀӸŪзλȖũȖԢхвìѢ_;ʛ',
                                                    },
                                        {
                                                        'key': 'ȷʖ]',
                                                        'value': '\x8dțʻ;ч˳Уɗѧ¨șēǥʷˠƁзʋÉ΄ŉĿӍι\x80ĥɤʋɸǆ',
                                                    },
                                        {
                                                        'key': 'ΊǸɖҺǥȮ§%Ӌ\x8c°кˁɿˇҞƝӾμȢcԕƃŇÛȆԎȤǟӖ',
                                                        'value': 'ъǫÑTˠyĔɋSxȣ\x9cnēÐɃŢțӿҕˢưǞϡȔюIԪΌǾ',
                                                    },
                                        {
                                                        'key': '\x95¾Ρ{³ÿ\x8eƣόɯĚƂ',
                                                        'value': '˻Ʒ;у!9ɒҢ«#фǢ˲òӬȧӚќʐƤʛηҔŬƜιǅќȢŃ',
                                                    },
                                    ],
                        },
                    'comment': 'οόŊ˅#\x83ē0LϮtǡÄʈŽШǩ]ԩĥɆԮʭϰÎʒÌέAȤ',
                },
                {
                    'keys': [
                            'ѣԔ҄ћϐϡ',
                            '¥ѠΆϺ\u0379ʺȯ',
                            'ȅӄŝ',
                            'ϗϘԭŦa(fԁǕϖҫĎ',
                            '˗5ГԝēǓзƺҗӪǏѭҫϛ\u0382iǹͱʙȋӺā˵Ԏ\x83ƴ8ԝ',
                            'ƷЧԐϵʎѻЏЕƫ',
                            'ƅƄЕ\x9eʄϧƬˠì',
                            '\u0382ƞϗҾҒŰvȪԍĄϙŐϛ"ȆɅoùΐpDˇҘ',
                            '˓˚И҂ζšϴԍǯȓӧƈʎνσȃsӃƒɸͷБî',
                            'ӯ¬Ůʮ\u03a2ʭɩӎ3Ё',
                        ],
                    'event': {
                            'target_id': 'ĒжŠƖϫĭӟ˓ˀĂДωJȓʥЬͷ¥ΠĥЦұΜƎŇʴȘ˪ӭɶ',
                            'parameters': [
                                        {
                                                        'key': 'ØжӕʘҩԁɘˮŨ\u03a2\x97ӟЃÝϨĞϰRώЕoԝӺɲŎϐȐр',
                                                        'value': 'TŌłΨ˶Ě¹иƁŨēƈƪiмȶüЅϴΡԉҐĽoӭĊƛ~фк',
                                                    },
                                        {
                                                        'key': '¨яҹдφ',
                                                        'value': 'ȿӷɺâԑζʶɱӖġԩƘ¿łüВǅ°ѺāҭʄƭQҝˊoȆƷ˦',
                                                    },
                                        {
                                                        'key': 'ķϤŊāǲϹëѶŲϺǤ',
                                                        'value': "ѵӉǹҲOɳ'ˎǋʆϾĻҶÇłʩĄͳɉӵ{wҒ³˸ԩˤǵԬĂ",
                                                    },
                                        {
                                                        'key': 'ǁұŸŔԖ\x93О',
                                                        'value': 'нͻӞƂѢѯɞş{ԜʮǴˎ<ѸδʮȓơiѰïԚȚЯͼǬHҋԙ',
                                                    },
                                        {
                                                        'key': 'ƏÞ¡hЖɫҎƞĝѐǔș´ņʑ4ϖƃpȾɀƬϞӆͱϸƪŒơϯ',
                                                        'value': 'ҁ±ѣʞȱ˺ĝĥЍˇϔŊӞkÚˎѡӆҤҚǥÞ˳Ҥȥʹмcoˣ',
                                                    },
                                        {
                                                        'key': 'ѷϸʫЊĆͿϐƾʌŕǐ˘Ғ\x94Āü˦ƠӸЊɰ\x82¶ōӝͶȔͷƮȬ',
                                                        'value': 'ǷϔҭǊŞØϤ\x9aя҃Ώ`ʛǼЄ˸ħÊǚ˶5ęǠŉțԠӗ\x8aȚХ',
                                                    },
                                        {
                                                        'key': '¨\xa0Νº+ӽӬƶȆÞɌŉ.ĶЖ˹ЧλӻƎύśƑFρİҹǜɿʧ',
                                                        'value': 'еǳƻɊÔѽ¹ОҐЏƌԧɽӈϗώΦȈͺѐɅҷɮɿńŋҰȚд҆',
                                                    },
                                        {
                                                        'key': 'ɊʖĸϢˤͰЮĊɐνĊϷӴϝûИ!ЃĽˬ%Ҳ϶˽ɪûʁɚɸđ',
                                                        'value': 'ǫүǡ2cƿģҹͱÆuϏˆ\x93.ēΙʢƤɱʫ7ˌԫԒΙĕȪYѩ',
                                                    },
                                        {
                                                        'key': 'ɉLóӓĳØʼʓʅǤδҤȥӖºƸϷԃɬωϜ\x8dʆԔґ\u038dıȤ÷\x85',
                                                        'value': 'ȜӘÜԄĊҲƑşƺ¹ȃͲʃ˘ųҁѰн˨øѠΧǰҍЧδĥïԙų',
                                                    },
                                        {
                                                        'key': 'Ҹ\x9b¸Źӧþȡ¥ηӫ\x87ǹĦΧɹƆȉΞθōʊϼҦČмƾϦ\x84\x85ș',
                                                        'value': 'ʫŤȮƚĮšɛīɒΔYԙSϡʷNФŢϖʽάқ˩ЂӆǭԡμԖȅ',
                                                    },
                                    ],
                        },
                    'comment': '\x8cψư»:ѺĴѳ΅ӚĖЄ×ѧƫʮʐřѠӎʝ4ʌʻЄңӴɧƥς',
                },
                {
                    'keys': [
                            'ӿϓ˵ɉ',
                            'ćύƣH˥\u0381æșӬƽͳ˖ʗƍˆŉϨхмԎɷф',
                            '˽ʤƽүσÎԢÙπN¯ϖǱӔѯç¸ҦʨǟӁÖǍŦ˃ϛȈŐώɊ',
                            'ҎĔ\x8fľɑ\x9bƇUƳ',
                            '{',
                            'ωʬɏÖ',
                        ],
                    'event': {
                            'target_id': 'ҷЀέΓ˃tӽԖǗԑpĩ˟ѼϖГԮ\x82˭υɗpo˧ρȾȣ\x8dӆƉ',
                            'parameters': [
                                        {
                                                        'key': 'ӁкΧIΛ˓ţʯˆѻ˃ҙʝмȕϘϓĸӶΐiӁɞӲƇĖ÷ƻȅȥ',
                                                        'value': 'xЄUбϕǼčĞɒϙҲËуϏ&¿Ԉ҄˯ůЏ¥ϴХАӠŃѳ¨Ӂ',
                                                    },
                                        {
                                                        'key': 'ŽĄőΌϟƏƢŎΞƂј',
                                                        'value': 'ѵӤ ˄ǖƸϫĺȫAΣϷjƱśӊ]ӘʙƄȤд(ʌˇ£ЎόǜɁ',
                                                    },
                                        {
                                                        'key': '¡t˥ŎĜÁbŔφʟ˯ҁ"ͺƙʒϯĳѬ×ɷϓ_ǨĠϜӉ˴ϷȈ',
                                                        'value': 'ѭțɇλǃɬΆʪ@ͺ(eTȵǜǹҟѣʌ\x84ѷãǐʉӇãǴҭğԕ',
                                                    },
                                        {
                                                        'key': "ǸåѥNϷԊŃ¶ʓκȹғɑѲ˴ѬȪϏОd§'íȁƐ\x9adɮ\u0378Һ",
                                                        'value': 'Ҵ',
                                                    },
                                        {
                                                        'key': 'ϊΟ{ǚÁ\x9eϱКƺӛȺǵã\x89ČȍǉӻrőϰԠȴϧIÓнϑҪγ',
                                                        'value': 'ǝƞɨЯИŬ˟ƖRΔȓm¤\x88ЃɌϊͷÍʈg%ȓȀϸϩGʾҝɇ',
                                                    },
                                        {
                                                        'key': 'ƣѸƼʎÉƋěѤˌ',
                                                        'value': 'ǆíOȱʑǴ\x82ˈÄƓҬŕğđǞЍμĢƝɖʢƏɲƌΝˆθƯý҆',
                                                    },
                                        {
                                                        'key': 'ńĈΓQcƈЙȈҐ',
                                                        'value': 'Ì:ϭŒΚȞİɚʔñǻɈ\x87{ƚŀШӧӲȪνɻȤƵƲ\x98ѓſƮÑ',
                                                    },
                                        {
                                                        'key': '\xad˼ɭƍŸзĜӎ',
                                                        'value': 'OϋƽϜϡ˹ɡӊЌȧФȒ\x85¨ȻÊɃǜʵǕѴùΠû΄ɉˉͺńә',
                                                    },
                                        {
                                                        'key': 'ϗŷӔθƥǥѺӅѭɈƟʪţʲŀǐŞɵ˚ʡŜøдʫȸӭ\x96Ŏˈȁ',
                                                        'value': 'ͽưҊ)ƵϐcʾȧƜ\x7fҨǞĆɻӾӻƑӠŮŰǇƚϷƿ`ȟ¡þ\x97',
                                                    },
                                        {
                                                        'key': 'ʣЉѰҟȭҠѾҎŞʹζ\x90ΐԐĳώӱǘϕʧ˚ɼѢӇ˻đԮ˞ԩn',
                                                        'value': 'җɇŠöԇźǹɈөʉÃҍtˣΥΜεǫɥƾηɻ˦ѳӦǙhĚԡӽ',
                                                    },
                                    ],
                        },
                    'comment': '¼ҭŹrϷҝJҖϧǙˏɏ$сʎŸ\x88ͼҢɱ\x96ΙĹʤɇŨ.җƿȐ',
                },
                {
                    'keys': [
                            'l\x97ԫШ`ƷʆʶǄ¨ȸӄԔûЎщȠδʣʂȋɺĞāȨϦǇ',
                            'ɈǎƬfRԗ©EԖĶаʝʶğ',
                            '.ɽѻ˕ɼЉŎgƌQМқоȳ\x8aº˜·ƫІѡ',
                            'ŉĆǉƓcĻ\x83ĉ<\x8dȣj',
                            'ĦĔϜƬиŌϾϯϢfѰqϫϊ˰ҁdʅɭɊҕƝ',
                            'ҭɇҜˎĀҌźʙƕъз»πӲɓĳЮǂÆͽҶŀȞɛТˇÛϷ',
                            '9ɗѸԜѥʚȭҨӨĹИ',
                            'Ǡ΄эӵϲȂӘɄƪΗȄę\x9aϴЅϏΝȋ<Χ\xa0ɓǪ',
                            'Ϭé',
                            'ͰҍϥЖJϪǋɌɝήҸ҈ȏˁŖȽЙЫ',
                        ],
                    'event': {
                            'target_id': 'ȑԠĞǁƆϟЂϛFjïϮŊҽɩģȴ!άôοƋʉžToϹƥ\u0382Ԏ',
                            'parameters': [
                                        {
                                                        'key': 'ƊĎġďЪ5ƙ3ӫ ďѾʻɅŃҹɏďʷǖˏζq¢ǃƟ³ČЯа',
                                                        'value': 'ϧ»ɻɊ°оҶӄG_èʜδɴr{ʂşеўʭWίϒˎȗҵ҅ƝΎ',
                                                    },
                                        {
                                                        'key': '6ʫɋ`Ӱ˳ŜѺͶҡ¶ǎɛҀͰѓĆҠѽwǃɓͶvΏƏҔ\x7fҋԉ',
                                                        'value': '˞ҍǴШҒƦç²ŃŀȆ}ԓæРԊ¦Ĕ˥ˆϘo÷Ӿӻ\x8dʖǅԆǓ',
                                                    },
                                        {
                                                        'key': 'ѠǷþԚƆÑӟɤѲrӃʄɈŤӹ҈"ȔԔ˩Ħ˖ĺγɡҠƩȌʘз',
                                                        'value': '[ϕËҜhÌҨɔϕЮϽð\x96γŞĹĖąĆПǊʁ˽ѩʯдӐœ˹ԗ',
                                                    },
                                        {
                                                        'key': ']ȞŊ)wԔЀϮʪȗǙMΜӥǬŸ\x85ӦΎ¨Ɋϥ΄ԝˊˇ˄Ӌʭη',
                                                        'value': 'ŌѮӔÄ˳Ǹ¶ЇȅшУìҷďǛяǮsσÿȎǋѽиÊϕȉёÛȫ',
                                                    },
                                        {
                                                        'key': 'ҦԒӔ˂ӕǉЅȟсҽԑNҭӺ0ΰ\xadĻǹѴϷʦȴéғź\x8fɇɁƕ',
                                                        'value': 'ӣŵ˔ԥ¼ȨȊǺčϟʔǌàɣѢҊɭmʠԟÁʓǹƎǭҏʤԠÁǌ',
                                                    },
                                        {
                                                        'key': 'ʽȭôʎΞнäңԚĐϩϳϘťτҒĀƆʇҘ)ԘƒҙʚƐцδŗ\x98',
                                                        'value': 'ÒɮȨ\x91ӵʣõ{MrҾ˞Ȯ,OƺϙśРȉǴŉƲǜҪӺƖǪǤ\x89',
                                                    },
                                        {
                                                        'key': 'Ғ˂тƛ^ǺɒЍ×\u038b¼βŜ˥ѾЂʄʶθΔӒʝǒҖέɣВϞĪǍ',
                                                        'value': 'ВɗµȈϐΉȢέƸɟўŌǇvɓřѻ˜ҥŐΐƫӰŶӠÈǂ|ʘŕ',
                                                    },
                                        {
                                                        'key': 'ƫѼŜBÔӺ[ϟыϜuғĲƜˮ҆ɐҙͰѐƳʡŠɤa2ɗ',
                                                        'value': 'ԄȾ҆ԡ\x9așЯѠNӥŧԨѰŮ҂КΥЩύǨTТ˪ŖΑŉΕͷӯ¿',
                                                    },
                                        {
                                                        'key': 'JԪ\x99DƩϯΞ˫ҙ0оŭԎϿʜӌū$ѵêðŎϜſ¼ј˛ŜƯϯ',
                                                        'value': "ӯʘńԦЍͲƔiϬǃЬɇĚԬӺ'\u0382/ԫԨҦpʟʔѶд˧ȧʆό",
                                                    },
                                        {
                                                        'key': 'Bð˶è˗ѫίϵˌт\x7fӭØȠöL˫;Ђ˙˒ЏɫΘћƎK˺ʐѬ',
                                                        'value': 'ùҥȲ-ЉҐţˀ˳ªӬ\x98ʏ:űҟŌÿ°|÷\x91ĄZӽϤɇ\x99ѭ\x7f',
                                                    },
                                    ],
                        },
                    'comment': 'fȤҞηӍԭҏҷǤЗԫȍЕʷԕxӖѷв϶ϚϙЮҧϴѐxżӋώ',
                },
                {
                    'keys': [
                            'ʢʥ(҃ԓĬғǐěыϪɷȩ',
                            'Јϑϭ\x9aұȬŖįʇ·ĕ®ѓщĩҝԗɹz',
                            'ɞϊŁɫˆżӼӛ˭xԈ϶Ɠɴ',
                            'Ɲ',
                            'ȆɮԢ˒šΜƥͲ\x95Ѓϙ@ύɥŅєīĵӢԊӧЙɟӶ',
                            'ї\x96ɰŻ˼ЖƧƝ×´ΡȱԊ¶Þ˒ӢχωҵX˞ǨҬ',
                            'χќ!ҫĄūЙҜ%ʝдҨÁԇҩέĭaɲΠˀʆqЌđ¨\x7f\x8ff',
                            'ŭ҆ӞΑ·˻ʈƺԛʾǧ%ŔʺǬƗӤӀȬÈ',
                            '˟ŧӍЪWѹϰ\x80κŹ\x81ДϪ˹ʏ҅ИśӀчӁʱɿɾŮƹ',
                            '\x85YĽ\x8fȲΓy˓ӭŁʯÑɦҪŖ¾ˁϓ]Ԫ˗ĶμҎ',
                        ],
                    'event': {
                            'target_id': 'ӰÑŅЗʬŜӊԔÉȬʜψŠ÷ȓ˺ȋŬȌƟ:ŦǦπʽĒΐѩΉЌ',
                            'parameters': [
                                        {
                                                        'key': 'ʱƸ˻Ω2ŤÎҋ7KҦѲăʐҴϸԣ˳cҚǜήӷ\xad*үκλ8њ',
                                                        'value': 'ѲӷϬȆˋâƐƳА\x8cǼēǢЅψǱԛчʹ\x9bHˀ½®ѫúqŋĔѓ',
                                                    },
                                        {
                                                        'key': "ˑɘǹчԠ˓őӥҏ˛å\x83ΕɚȁȀɧʶ·Ġϧξ=ȭǖϮ°=ɟ'",
                                                        'value': 'Ɛ=ҶĮʹӂWʾȹҜơϑʁ˼Ҟӟĭ\x82fˎĸÿǹSRyȢȽΩΉ',
                                                    },
                                        {
                                                        'key': 'ÉїŏԠɂǨʯʸҺʙΡʒŲÊ`ɦŢԡðѥÆǾͱǳ&ǯЎɝѾØ',
                                                        'value': 'ƿқԦlɴˀȣЯĴȑԎrǹʼɿгǲͰсҁ\x83ǓњȪЫю\x9bmюʹ',
                                                    },
                                        {
                                                        'key': 'Ԡх\x9dȰȭΑĒȪτȅЃȯȎfɜϡ˘іԦòȶɩΜвЏÓЋґҎѥ',
                                                        'value': 'Ϫ\x7fƎ҃¡ȌԢňάÒʆόϦĕϣϐҚϸȈƒбŕˁŅ\x8e\x9dƼ\\ҙş',
                                                    },
                                        {
                                                        'key': 'ӽN˕˱ƅ(ţϯЇӱºͼϊ',
                                                        'value': 'йŇ҉ѸʯǥρēʌuǜҨɤ˵ӔƞɷфӢʊяɈɥоʚ΄Ǳӽ˼ǖ',
                                                    },
                                        {
                                                        'key': 'ǫӒҋȦǢӼϟήϞѣ˱ϓА\x7fȽȞ˽ʏͶtűƀϥѨиϠÂҸǢӶ',
                                                        'value': 'ÒѫϦǇɾȒō\x8bʋǠ\x99ͺ˶ǴöęŹѣ\x80ǘkЧȱΘπJŖΰщŖ',
                                                    },
                                        {
                                                        'key': '\u0381ȲÇ\\ǘĩƦҤǗПŇΪƖΜa˞\x8a@ǥӯεһΘ',
                                                        'value': 'ñѰ҉ūʁƍΌ\x9cηɏӜʂǌČђƒӢћ϶ȴ\x8dǃϰЕ¶ы»а\x89І',
                                                    },
                                        {
                                                        'key': 'ёѦӬȪƢѳĖ\x96ҺÎÏҾɅǯĶpћԛ\x86өǉɻ°˅Їȣ҄\x85ҳҀ',
                                                        'value': 'ΏєӌēЍģʱƟϣ˳|îȉŠȫžюёΌWńŅŦƛǍ\x8bϐԪđѺ',
                                                    },
                                        {
                                                        'key': 'АϧМϙXАΆÓӘɴ\x9e\x9cŻңϜĥӤƙѶǉгМҮƞ϶nƮŉoÆ',
                                                        'value': 'ƃǦɑ²\u0380ǢΨŁÙraʅhCƥ\x8cĵǐɽӔưіʻҬѾŤYԈϖщ',
                                                    },
                                        {
                                                        'key': 'ŷɼƶҭŘ\x8eЀѨ\u038bԩӬnÄ\x95ЛtҲ',
                                                        'value': 'ΒГ£\x83ȘЂǳ¿Ƿɘr˙ȍŋͼșоǏǬȿ˶ЫϻЅ˪ѳąƊˎæ',
                                                    },
                                    ],
                        },
                    'comment': 'ǸԧԡʕԮԒǌ"ȘkΪȴƚҎʳ¬ġӲ\x81LМłӔГӈƷҤҝȧњ',
                },
                {
                    'keys': [
                            'Ș˒ȉѱχгÝƂĢȴ˳ĒŎ',
                            'ĴɕÌɡ њɠ',
                            'Ǘɋǔ҃ώÞԬ҈ӓə˴oˏϱӺϥϓͱ\xa0;LԬ',
                            'ƥҕԟΆӥȯΐ',
                            'U',
                            'ԉ$њʹȊʕҵc\x8eɐȋͻʻѰŜǰ',
                            'ţÏΎ\x90Φœ',
                            'ƀūɋДÕƴӄΔǺӽ˜ǯϑҥ˔«Ŝ˵ԒɻΩ"^ÝҐʲȎ ҡ',
                            'Ȋ-\x8aʌŞʁԁ7˖IϹ',
                            'ĀұƞӦă\x9aș¾Ʊ҂éѼ',
                        ],
                    'event': {
                            'target_id': 'ƈĵþ°ĔвʜƼ]¹ʓ˾Ȅ˹ą\u038dȷĻèŝγĄƽϬι˓шӃ8Ⱦ',
                            'parameters': [
                                        {
                                                        'key': 'Ơȳʩ\u0383ԑңȄ˽ӾɖεɏѭԞλaǆƳȈźģ҈ĈͼҞƻώҁΥȎ',
                                                        'value': '˂ƈԬъǳǘҥVôɑԤό͵ŵӠʹϼϞѥˊȄΟǞЇǌѰƼ˚ұÝ',
                                                    },
                                        {
                                                        'key': 'ѬvшǣˡĹúȵӋ 6',
                                                        'value': 'ҸҔ~˄ЂŒҤˢĥԆʓ0\x96ɖŭÒԇĜЁǼɟΆåфϐȵҙ\x88ЙɃ',
                                                    },
                                    ],
                        },
                    'comment': 'ήӴ|ÝɻȂγɂӽǐǺˎƱǏҞˉЗҼĚҏȩΗºȑοɇʁʷЧγ',
                },
                {
                    'keys': [
                            'Εɋԩ',
                            'ɊрўǞҋĤǭҫΞ#ǋɱŇѓȊүаӆǳżҎȽ',
                            'єҝ±ΧΡ',
                            '˂:èƘͰŸƭƤΟίьү',
                            'ÁԋҖԚӍϑ',
                            'ɷÐԔ.эˍ',
                            'ҸʏӸÓξπĄφ҈>ϗНϡSΤǭҔԂ',
                            'ǲãʗŌûЕԤѫЫяϡƅҊ',
                            '\x949Ӷ˹÷ж\u0382ÖɻŷšˌϿƼɣ',
                            'Ԥ',
                        ],
                    'event': {
                            'target_id': '\x8eɎҙӕщáŪŰ҂ƩΦɍђĊψќ\x94Vƕ҈Ҙʰžµ˳ǄӯыɲŞ',
                            'parameters': [
                                        {
                                                        'key': 'ˤШĝȉ"ýǑʬђɴѩÖ\x8eѶʵȿԛԉϒԁͶ½ͼρѦƅǨűӮǫ',
                                                        'value': '[ǱpȐáµ˵ŋǧŪʕǆ·ѨҽϢȬʣФҜˁБwēƧͶĖφǼɣ',
                                                    },
                                        {
                                                        'key': 'ΩɯÉ¥ҥĀÑӢϮÿ˳ӽ±ʜɁ2ЌūHŸӻČȓӽǫʈǹyӅϓ',
                                                        'value': 'ʬ,?ºǳșǪҘʯ[uȫҌͼҌȄĢĉɒƓ@ʋƈȮÔКҽԣАʰ',
                                                    },
                                        {
                                                        'key': 'ʓɔ˽\x86˱ūʳʳх\x96',
                                                        'value': 'ĳ½-\x98rɭЮĚǅӼѳӠ¹ĳӊȐ8ˋǒŃθ\x96ӌɽӤӠŵŌýɏ',
                                                    },
                                        {
                                                        'key': 'ԥ^ǭĴƓς«đѰƵЬμƪĚѡ',
                                                        'value': '¼ʞѳϬԤİѽӛȑԧɟѻϻŒПύpȅÈӕ×ɫ\x9cĳμόƯЋЀQ',
                                                    },
                                        {
                                                        'key': 'ЪӟħÌΝЉơӏĭ',
                                                        'value': '}ɠΡϪӥxʀчφӌȖ\x7fȗšHź˶Ζϳ¥ȹơ˙ǥ˔ԃˬсɰί',
                                                    },
                                        {
                                                        'key': 'Άӑρ©ɃȔϫԦϥͽɬƯˎˑĤ¶ƂǈЪĔͷŰǛЀɄēʊŹʏʔ',
                                                        'value': 'ƞδі˔îͽȍҖĚБȁ\x82\x96ˏҚΊ҂˳ǀƋҊŬWǒҏӏSщȽҮ',
                                                    },
                                        {
                                                        'key': 'ˉήÁωϴǻѫʀ\u03a2ңԗϫ\x8fԌƫǽƻʭÜ@Ìǭ˻˂\x83Ǟ_Ҝʟе',
                                                        'value': 'ѝοҲǣ[©ŶΰӕȇΉÖЍͷԀѢөӎЛǣɜʉ}ЬrȡūGҘË',
                                                    },
                                        {
                                                        'key': 'ŸʦϬ\x97ļȺ¿Ľ\u0379\x82ʂΕɭΫҠХþΰҥ{I˘ǜЂ·Ζǋ¦ʌĀ',
                                                        'value': 'ɋĘɾjǣμǔKǽʽԒʁ\x92¯Ȏŋ\xa0ЭђοʸkϤкѥЉҴŸΐĔ',
                                                    },
                                        {
                                                        'key': 'Ԭ\u0383оНħɿˏ\x89ȹΌԎҦѶбcª¶φƟԂÅȑͽώνźΔŝΦ@',
                                                        'value': 'ŦТǿ8ǤžǀүɊį¿ІВş*ǕȜԤ\x9c˺ԭƚзϡɢȢėЦ×ƅ',
                                                    },
                                        {
                                                        'key': 'ұĢѲ!ï/Ƚ³ψƪýџţŢǘȫ\x9dԚξƚʞ϶Яў\u038dǍ\x93ĚԁЂ',
                                                        'value': 'άԏхϭǧȆ@ŻʚɓĲ\x88ӨΪʂ¨\x85ªƉΒҠ\x83Ͳϥл˼ϣъŌ˵',
                                                    },
                                    ],
                        },
                    'comment': 'Ň˛\x88ˮӏØҤӯӿēˋϛƒɉïԤŲT!ΚǌƓĞЫűSKǍԤϽ',
                },
                {
                    'keys': [
                            'ŏûʉþDʟÌ·ТѬҗˊɒÈǎCϥЭȴяѮυƣѱǝͲ¢ß',
                            'ǐѽЮϚƣȾŘˠŠ˒\u0381',
                        ],
                    'event': {
                            'target_id': 'ҝкǸͼʲǧƻӕȒğȵҳɖʧѰʓȐįƈΪҾʬϙˉДΆƹК`Æ',
                            'parameters': [
                                        {
                                                        'key': 'ЏβɋôʳΛŌԫɶϡ54žȢϷΜѦ\x9bǧϩЄԗϋԏϢѧɗԛҷе',
                                                        'value': 'ЄΐщЕâҟCµǽҦº³IĲҢˏ˫ͻɠș˸ʛӲsщЃTщÎ7',
                                                    },
                                        {
                                                        'key': '\x84ȚðΌĂΧĆˠφʧθЩƙĠȎԂĐPȚɨҐɁĠɱ\u038b\x84ˉӇɆ\x84',
                                                        'value': 'қ ƷӫμùˮЉǋȬė%Ȕ<ΰõR˂ΰáġӡǌýʱҸ\x85ɖҿɝ',
                                                    },
                                        {
                                                        'key': 'ûǮӭǧѢϯԑɶĿЉԉȫϭӑØĺī\u0380ˑƑɁƧМåȇ˳Ёԃԉ®',
                                                        'value': '϶Ϡžʦnŏʻӄȟɧɖʨј\u03a2ʉ}kϾӻӝϕêŔȭΎÂǩҐͷҀ',
                                                    },
                                        {
                                                        'key': 'ǌӕĊƙϗ\x9fÊµ',
                                                        'value': 'ӤӇĈŬʝƵϤȓÕ¦Ɨ¢ȓƽǪ[zċrвҫʱϕƘɈǶhӾǲӑ',
                                                    },
                                        {
                                                        'key': '6ÕýҷҖԃ«КȤ¶ɳӍΧЄČ¶Ҽˇ˔ιРőɶω\x7fƨïʰҋ˫',
                                                        'value': "ВӁԣȄnȴžЬÁȹҎʍЌӟǺҷԅǙŪ'ͻËoˊĆĺɓɐțǩ",
                                                    },
                                        {
                                                        'key': '´ÏɚĒÜ҅ϔǓƓʫфėʞCЦӛČҬÚáɕǅǒĐȿŃɟžOǮ',
                                                        'value': 'υӛϠǄʱӀΛŢɽ\x97ӠѐҨâeýĉͷԫüʾƃ½˖ȇÌɓΫӎϠ',
                                                    },
                                        {
                                                        'key': 'ȹǕ3ʞŠӗ\x8deЀ.ɇ%ƬɡУȯЖȜҁœǔѷļ}ˑӟũɳȨɸ',
                                                        'value': 'ͼЎ%ȁΖŷʞǼǯ˘wǊŖӞ:кӨɹʁŒцπЀɲΑʝrͰԊҭ',
                                                    },
                                        {
                                                        'key': 'Ĺӑ9Ĭ˥\x86ϢʄǦʃϧɴӍЈԠŨвΣÏɬʔԮŻӆfѳtυԖĳ',
                                                        'value': 'ƂşþЃтϊϙϓĵªϷÓʃλЕƘ&Ҟ½ùԀˡȐɿˉԓԀƎ3¾',
                                                    },
                                        {
                                                        'key': 'dͳȟ',
                                                        'value': 'ϰRΏВѪӦɈӃʙϴžƱІȢӟʩƾʑүҋČԫUЏǨѓϗԇɴƄ',
                                                    },
                                        {
                                                        'key': 'ĻĠ˪ɚ˓҃ÍϢĶыӎӃȣҘTҕϕǔˏқǡˆѮvп¨{ŰëΌ',
                                                        'value': 'α΅ǂŰɮЈҔһɺŨԊͻƠ°¡ſdˊЗϳ¬Êӷűªſʼəɧԗ',
                                                    },
                                    ],
                        },
                    'comment': 'щӻQЊÇĒκȸź´6ԭ¸ōѴόГЕ˟ʿо\xa0ŐÒȆ´ĖĽǆø',
                },
                {
                    'keys': [
                            'ӣĥ˳ѡӮǱɲΏˈ«ҁҤǹѵʊʏ\x9cӸĠ',
                            'ň\u0381\x9dxÄǐUҫ8˫хȨϿ5ѰǼТˌ˽҄\u03a2Ԅ¦Ҽǵ',
                            'ԗ¤ĖО¦ԜĶˉ',
                            'ĠԄԍˡѩĲˍЄ\x82ƀʶӼҕƑφʇ1ƦÉ4ϫ',
                            'ƦϺςǼɄśκӿҀʌΣ\x83˼ТɜԪͽЏʳʫÏԠѹϽȈ',
                            'ϘĞʙɖƶЦϐ2˻sϰҋÉɐЋ\x9bǺʀøɉΥȫ͵ӆǕЯ',
                            'ÓӔɻИə×ÉԕɆʸŤĸoćʌ',
                            'ҾƀФŭϱȖҩĊŉcǌпԀЈʔʘͿЈӇ0΄ўϵԊϳ',
                            'ХқǟĶɅӸЍͷȒǳťɶȻҬǇȗăēʑʁɣџȔǕ',
                            'ŨȞżџԍ¯ΗEҧϖ2ɪюɎƽқңȕ¾ĥFвӣŷśĨȀї',
                        ],
                    'event': {
                            'target_id': 'ʶʪ\u038bҶϢʍÒɲ\x8dƘƼƂҕvd˹dȽ\x98ЮƱ¼bǟϺоϷƒϫ',
                            'parameters': [
                                        {
                                                        'key': 'sȮɲϘ@ŁÐɉϢԇӢŨƮƲΌ¡\u0383ŚЎƞǆǘ\u03a2ăāҠŰΕ\x8aď',
                                                        'value': 'ΔҶѾɺϒǃЏƛġԤĵ\x8d˲ƼÏјҟ˕Ȇ©ĩωȔЯMˁΌ*ƒ˹',
                                                    },
                                        {
                                                        'key': '£πϱþʘǈ¹ӵˆԊǻйɆ(УĎ/ê\x83ȄƟԍ\x81^ŤʲÆ\x8dϝҦ',
                                                        'value': '˄ĨӬӰӱǂȦʡĞŏЋĚ˙ȣτвə˃Ȁɵ˽ÉύȪȹĈǎğ\x93¥',
                                                    },
                                        {
                                                        'key': 'ĖвϥƧъ\\ʩƈіωɅΕôƮÆŵϢԒжӜʬM3ń˒Ǜ#ȽŌǡ',
                                                        'value': 'еɱʎϫϦÆͶЉЌ¡¿¯ƶųʫ:ӐƦɩϾ§ǖ´Ӡåýʷ\u0383ɞЕ',
                                                    },
                                        {
                                                        'key': 'τй˗\x8fШʱνǨ\x97Ӻ\x9eȋŏ§vɱϋӽОpÄʀɺĭ\x80Ԏ΄˲Ԭˁ',
                                                        'value': 'ҤсӅϧ\u0379ɬзĝ˓Ǧıԏ¢ŏĖŜΚIПŤƥљφѼɏƠδÑŰǲ',
                                                    },
                                        {
                                                        'key': '˒[ȩ\u0381΅˳ϲΗŚҵӀƠѝҊĝғŀ?Ν+¥ƒqΌʄЗ1϶ɆǦ',
                                                        'value': 'ʑȡɾĂҵǵɪ·ӱӧӜӻ\u0382ӛϐԝӇģɐλʶɂԓϭǸȷǃĎҘK',
                                                    },
                                        {
                                                        'key': 'ȑȥ΄΅ÚτύŃ϶Ǟϙӎûʞ\x95^Ĕʘî҇ȓƲǜƏʐѨСӞϓͱ',
                                                        'value': '΄ıӛ\u0383Ӆ\x92οȟAӇǘІҎ˥ѣÕˊ\x95ţņþȊ\x8d҉ŀϕŇƝɕϿ',
                                                    },
                                        {
                                                        'key': 'ʿˮѧфĵʡŞ&еυƿӈȑÍӥ&қˤɢĄϴΌGӯ\x95³Ѣ˖Ўň',
                                                        'value': '5Ϣ³Ʌ\x87΄ȡƨçÔѱŷȗϹӡяϽиðǄȮvĦūŏʕѕзŃЄ',
                                                    },
                                        {
                                                        'key': 'Ƀ»ѲҚϳΥŴāӐϐ˰Ăҷӻ.ˢѝɡԐΤӆ¸ƙŝęϹԢϜӋµ',
                                                        'value': '+ÆвΖƿǦʺƃǭάЀǚš\x98ƝȴΨӜдĭ˅ÆŬӪɱμѤßƗË',
                                                    },
                                        {
                                                        'key': '\x9cΒϓҹβ?\x94ÊŗøŽĚǮ\x83ϳˑɁĦë',
                                                        'value': 'ÄɣѐȮπϋïǆȁϸӕ˂êǘ˜źǦȧŢʏ\x8fДϖɲҾҸδш˙ø',
                                                    },
                                        {
                                                        'key': 'ϙäɏԧaDİʿʵÅҎĻmοÏ¬ОwŃ',
                                                        'value': 'ǂеÑı(3вȰѽƄMƄǖ3ΪƱɨ˫ë΅˖˃ɘџƥʆпҖӁɠ',
                                                    },
                                    ],
                        },
                    'comment': 'čϟĉʽчˣƾ¢ɩƜͳōҕʡƑVƠÄїѯл',
                },
                {
                    'keys': [
                            'ǼʱǕмŚϾˮѐüƺǢϝɪϜl˘ӉӴN˒ΌƋɺŮҩǘӹʁ ',
                            'ʋŵǄͰĮɉĝӋΙЌΞθ҉ϤŽʲ\u0381IÙ*Ǡ',
                            'Ġԟşˠà nϔAʃǣŜõõrɶҳǩðӦĖ˂ҁɲǃӭƵ',
                            'G˓ŴϱÉƉҦ҉яʑ',
                            'ɵ˚ѰɆȈƻ\x86Ǳ',
                            '!Ӯ\x80ǾŤЛª',
                            '¤ңҡrԒМǆʴ\x89ѭѣʢєƘɎǋŮɷÅҟȄíg',
                            'ȝʆӰàӡк҇½',
                            'Ǚ÷РЉɴśĲ$ҬũÅѹǐъƠӚΏ\x8bΘĖϺȜʠǾӆѡѮΠÝ',
                            'ɉёÌ~әÛBʐ«ѵϠѿźʇ»ҼÊΪӞєЂȳ',
                        ],
                    'event': {
                            'target_id': 'ΌӜƎņϪ\u03a2BБҦʠ˘Ǹ\x95Кčϐ¡Λҿʌѽʷǈ-ưҡ°˓ąƜ',
                            'parameters': [
                                        {
                                                        'key': 'V÷ôѧʣǎ¼˹ƛӇɇōȑ͵Ƚϧ˟ƀƆ΄ǜňԆɕĉҜńҮ\u0383ĩ',
                                                        'value': '¶јϲɀΖыëЊϨʂҒ\x8aΟΟԚӿоΓˮΨӰɱ˪ϋԃϺͻĤǷԎ',
                                                    },
                                        {
                                                        'key': 'ɗВҵӁ˝Ш\x88һΫȘϴǶ˞',
                                                        'value': 'ҕøɸҸœȫƸeϙÏÆˡɺɃϼВÑ®\x92ԓȾԋȔʨӕдӔàȓА',
                                                    },
                                        {
                                                        'key': 'ːʓǏԚϞʬʙÂȣǮ¸ɘϑŕμѤ·ʤ|rʲήԆяҶuѾi1Ƹ',
                                                        'value': 'ʧċ×ˌҊѳ³\x85ͽОɯʉLìqԪĈ\x85ȑʎƗƷχ\x8dʞ+ƞȑ<Å',
                                                    },
                                        {
                                                        'key': 'ʣ\u0383ԕżӮ\x86ʱñČьϝ;ŕYŭȡƓɼ˷Ô\x9cȫȵѣʑďДѷš\x98',
                                                        'value': 'rĒF£ǐҪʰҳʎļ.ȏKƈƊˈɔєǠƢ˽Μ\x91ӶҿʬŵϟԂӐ',
                                                    },
                                        {
                                                        'key': 'şėɸʻӚøu\x89ĤÚҀɸӃӵǁȾɞƚĬΜƌҩưé1і°ӯ_ĕ',
                                                        'value': 'ˑŁˊűϗbԕ˷Ѫȳ˼ɵȴɖʢЉʨнņ$їˌʊɵŏȐѦȣі˻',
                                                    },
                                        {
                                                        'key': 'ļȑѧѠ<ϣАǴЮɭӱ˗žӺŰ\x83ɏӷȊтƳʋΨсfŊ0Ԍ>Ċ',
                                                        'value': 'ƐƀpŌɳȝȴȸĜɁʻʺƃԛ\x89ǈΟΩӌɤdŞȄԡŃJđʏжʖ',
                                                    },
                                        {
                                                        'key': 'ȸʿъԜЁΕжȍIΟӁˑì.ЃҀʮԒԭ',
                                                        'value': 'QʃǐғÿǚȪԥϽӥXӉ@èЖƹѳǂҐѬƱљϓӃ<ҠǬŷ˞ɷ',
                                                    },
                                        {
                                                        'key': 'ԃ',
                                                        'value': 'ώŊǴɐŭƴ\x8fҪŊ\x88ѕȮԋˇεђƿ\x8aХϙ\u0383Ђ]šƲ\x97ϓӖƌÝ',
                                                    },
                                        {
                                                        'key': 'Ĵϭʒʮ\x9aÑөƯïѓaѴƱƀʲ\u0379ȸԕrÆҥĚƿʤ³Ò',
                                                        'value': 'ΡƸȱͺ¨˗Ȭȇȼ˞lԀʱɏВȡϪϷĳϰʬǫȂ˨¿ҸκΘģè',
                                                    },
                                        {
                                                        'key': 'лѝ#ѤŒ?$Ιɑƿ£ĈĊ\u0378ɹϕғοW˾єʤȆШȻîјѴԃƦ',
                                                        'value': 'ӣсðσŁǱ˗Åѯ\x829ɘʉƸŷ˗ғӻˉŨʡ©ӉUюԝƕǂƈӧ',
                                                    },
                                    ],
                        },
                    'comment': 'Ӓй϶ĵϽӐ*Ԛ®ɁѣͿÇќϔЏӦӻɂԦˀɱɟƊǿȻЇǚʴΥ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                '˸',
            ],

            'bindings': [
            ],

        },
    ),
]


class EventsTest(unittest.TestCase):
    """
    Tests for Events
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENTS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.Events.parse_data(test_data)
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
        for test_name, test_data in EVENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.Events.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENTS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='Events'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='Events'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='parameters', name='Events'),
            ),

        ),
    ),

]


EVENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ӌɁ!ӷǙУԋҝѾΓЉӁIgԘȜȒ\x8duKŚʶùúѾϫΊƙŏĪ',
            'description': 'ӌ˹˒ӔäƣʍȝɦͷНЗöї\x7fҙҥɘТdӏ1Ϡ=Ňˌʆ¯Ƶ\x9e',
            'target_id': 'яɑŁΨɽϱȶѡʿ˟ɮσРƷ\x9bþңÙşÏΊҴСǲ7ċҽŏɘř',
            'parameters': [
                {
                    'key': 'ĠкҨǶԦǦěыP˞ĀΫҪŅ҉ǔĲÎξƦǋþƻŚсѼʄДŌʐ',
                    'description': 'οaý˜ƽԀΌ΄˞ǋɵΌďĠŐɕЬ\x89ԍɲӾʃӳŢŴҼȣɭRԈ',
                    'default_value': 'ӪªŬɿl˖˘ˏ×ɶхͺyԬɭкơɩǵʻψIҤ˕ɣѮԚϮѻЄ',
                },
                {
                    'key': 'ǲ\x9bӞİќWі|αҹǃͽľʕӞ=ɪϹƚřƿҍѠхÍ·&ŚȈϐ',
                    'description': 'ƛǟɦ˙ҨEʪα\\0ώαϜыΩɅƈ;ϩӀѫЁϽƠɮf҅{ԛ_',
                    'default_value': 'EщЧÈ¨BwțϖFƱŚȣ:Ӈ;ōΓĬЙω¹PЦӴӢ,ӈȖә',
                },
                {
                    'key': 'ǱїǼϤŜрԠˤ\u0380ΥӼҽÿŞƶЛ\xadԩȔ"sˋ\x84ЗǇąѕǁ@˅',
                    'description': 'Ϩ[өɓӺiѯœ\x95ƃϙ\x94ŭӧӅʎʦƳɠĬҰXƄͱшĪƵӑ;ʟ',
                    'default_value': 'ǒϨşїƣАԕĄʜѧŨ˞˳ѭÐʎĿWIĳҐϧϓŶɍҙIƆҬϐ',
                },
                {
                    'key': 'ɋĸӖŻˬǪ3ďɬɇ#ЪŃʆɎ˗Ľƪņ҄ӴЭǔΞŻǸϣȐƨϻ',
                    'description': 'ϊˢҋԎǷFĂ}ôϴӧÕΈǷǢɏƈаƙϩˎǓˮơɛŗоϜʺӁ',
                    'default_value': 'қӊψɹƷɨȻʮѤ\u0382ѫҌƺíǅ͵ȑ\x9cˏϧΉüӫŝɓ˪ː\xa0Әη',
                },
                {
                    'key': 'Ŭȫʡʮǰ¢ȽδӎȮ˪ΉÀёѤȬ®C˫ÓϘԠƶϭțɭũѰǥɩ',
                    'description': '(ĢʨƒýϙӅЗȭάȢǍҋûДŦӥ΄ŸƨAȋ°ɡ\x8aŨЋĊƺɰ',
                    'default_value': 'ĵҚ¨ԋJӣsÜϱғϵ˒σŜĮˉӮΘŅbϔ\\ȄѓҦʯRӵѶЯ',
                },
                {
                    'key': 'ŲˬɻίǞɓѨɸӍҙøԞҳϵ˻ϚƐęʚɒξхǒҖϑΝǜҤ˧Ԡ',
                    'description': '~ɋåͿǏǅʦʹşŌţ0\x80ҖϢʯ\u0381ƋҩCԊĜĶ´˒ƚΓǷƽ͵',
                    'default_value': 'ˏõ\x8aSŭʢΧ˻ԡŦľѣѷĴИӅͱkǂάӄ"Ȗbϖ&ΝęӯȤ',
                },
                {
                    'key': 'ȚŏÎ˺ͲѝԨҝķӁŹŠȑϊșÛųҩ\u0380ȉɈ$ѕƪȅʵĤƫőʔ',
                    'description': 'Ӹ҄ԏȜɇʥǲºŶ\u038bȠƿťɤɄӱԅȿÌʒiǱԃԮ\x92ĞɹԁÚj',
                    'default_value': 'ǒZʜ(ġҥƒϭΗƆɆΚȊĵ¦БLӶԟĪƧӉ`ΫÏɷơϸїå',
                },
                {
                    'key': 'ǛЎ\x98ӍѤǈÓˬrǜжɶʀȌӧ|êǊȏѽΉ˝¤Н\x80ρ+Áϫѕ',
                    'description': 'ӴӐɂѴŦɪҮҰяŮđbǆ*ʯ˸æЍ\u038düĖĆϥ¹ȵӲʘθĠĭ',
                    'default_value': 'ȓҏ˶.ƣǯƠОɈ/xǰɣƌŌѬ\x87Ӣ˯ˣǴɟZƏȊaϘɤвΧ',
                },
                {
                    'key': "\u0379ğƃѮƆŏéњЎʬƒӞƞʝͼ!ʹˠΟɐ\x8dѯĲҺɮģψȷ'ʶ",
                    'description': 'ŧʏÑӓϹȷҥńĖÚưˇȭОəŽÝ)ԃԩԡɐˏ˳ĸҝыəіɩ',
                    'default_value': 'ȼåÝʇлϺæ˗Ӣѿ˨-ǸƯηȖԬàϝĝʀΊïђϭҊϦԘʎӚ',
                },
                {
                    'key': 'ȔǬÈð\u038bęûƜхȇ',
                    'description': 'ĖƄŤĶ½ϸɶԖҸĎmǤɹħΧ3еˋҢѭ˔®çȲăÎ\x86ªB˄',
                    'default_value': 'ҵϬʧЌϼˋΨИ\x93$ԡΑʃ\x9bȫ҂ɥȼǺIɼҥ˵ѸӄɈĨ´ÑӢ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ҝīϥ',

            'target_id': 'ͿτӠƭô',

            'parameters': [
            ],

        },
    ),
]


class ExtensionEventsStateTest(unittest.TestCase):
    """
    Tests for ExtensionEventsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_EVENTS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventsState.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_EVENTS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_EVENTS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='ExtensionEventsState'),
            ),

        ),
    ),

]


EXTENSION_EVENTS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'name': '¥ӪΞľȡʪЖθŪŹΠӷʔтѽƆÕЙ\x80ҹ.-ɡχƳѮʬʀǐƚ',
                    'description': 'ҋЂĽϜżŲѢ<Oҡҧ˖ЕϏˢӔыћѓΈ˰ʹüӤƲSʄßKϨ',
                    'target_id': 'ԗίɥѩ҈Ē\xadίЉ\x85ȻşήўВԛΒŹΑҵҟĩҞƗųTÃʛȣΑ',
                    'parameters': [
                            {
                                        'key': '¥ѓȍːъˉԭĈqĐ',
                                        'description': 'ʁöӸƫҲƳǃɿˈπʈЮňɭǱĚʳ¸\x80ϜѼʏĄʐΝͶЪƧøĭ',
                                        'default_value': 'ļoΨǂÁϽùғʁ$§ɚҽȤ϶ШϕǪoǭƓӆː˻0\x98ҝÝƱĞ',
                                    },
                            {
                                        'key': 'ƇҾƺ-Ωҗ`˼ӘĹ˫ϚʍɾќȋɾʽЖĮŷǅƶbɈQņͺģa',
                                        'description': 'î2ҷНˠψμҜТáМͶ¨ԭpàÑˁƁȤa\x96ʻ3Ҏſ²ȾÏҲ',
                                        'default_value': "+ϴΗɧİΟϿ'ɹ҇ȑƙӧȎЪӣΣƸΙοϲȢӵ˩ʱ;éƑşώ",
                                    },
                            {
                                        'key': 'ϧʈɓƔ\x8bȈ˵ʨκԇͳӴʎɗјХƟСɼНʐ\x83в\x96ԛΧӷԖʗ˹',
                                        'description': 'Ӟ˩ɓӊЄʀ˺л\x80ξǘFα˯ȁi½ͺѪҿʫY&\x9fʚɪϮʷŠę',
                                        'default_value': 'ǂɂɡǄҎÑνŖŲЙζҷʊƦǿčӒӼǡĖ˻ǂDǴɥǈѠУ¶Ч',
                                    },
                            {
                                        'key': '¹І\x98SԗӤŔ]1·ʁɄȆ\xa0ˈǂ\u038bʩȏϔдДƠ˓ȀőԅǨϦŚ',
                                        'description': 'êˁßˈµŔşɋőĊϙ˵ӯ҆ɅԙȶĎʅҳʳBĘϊ©ъʦŞƍϯ',
                                        'default_value': 'ԏȏїҙ(4ϒ˹ʟɨ\x8cȊ\x8dĉΖӵЉԠѫɀĬедřɳǞѺñ\x9a\x82',
                                    },
                            {
                                        'key': 'ϏνСȂƐǉǬ\x9bͻǃ"άԍϖ5àӻČМȠЅҟӼHː9ÐҊƉɳ',
                                        'description': 'ď˦jʹǈЖĸưϮʅĲmAϻŷӗλҖeѝż±Ӌ\u0380Ѐ\x95E˳Ʋǯ',
                                        'default_value': 'ŕˏҎѰΰɣˠѠМſϱôрǱъzƠf\x8a˔ªȤэɥсǚǑǶlɥ',
                                    },
                            {
                                        'key': 'ԘǙƘƘĂǼѴΉŠЗ=ʳǽŮёvϒĔϲӄ\x87Ƌʄ˽ӶÏˡ\x9bɨǪ',
                                        'description': 'ʇшƘДʽ®Ԧϭ¿\x8c)҈ϡҖØӃο¼ԝɍϠψºġRтƺÒǫɦ',
                                        'default_value': 'ȪʨѭşɨɶvŠϺ´ʅǳǩ\x7fͼźҼϞΈɒ˰҄ѠӓʍŚȾұѴ0',
                                    },
                            {
                                        'key': '˃*Ԑƭ˅Ȃ\x8dЯЧøĂҀΏŅ·¿»§Вҵ,ҼӃƢ\x95ěӃŏўã',
                                        'description': '{ϝƳ;Ύ˽ѨӱҊ\x8aͰÚҊΈƖҢȯʽǮ\u038byϭϐѝ6ϳ¥ˉЦƒ',
                                        'default_value': '?¶ԂĂʺԫϽiȴπɃӃʂчʦŁӶǮűΌ\u038bӚŘɳţʦҿęɡƜ',
                                    },
                            {
                                        'key': 'Ȃȵҷ\x9eӎƴXίѻˈѳʔʜ2È0ѩΠʜǦ0#/\x83ϸǟǮΔιŔ',
                                        'description': 'ÚϮѸʑ;ӔÅɃə˃Ĥª^έɍɝϿɅɵНjмѷѪïÜȬʭˇҦ',
                                        'default_value': 'ÑƜÛƲԋͼώøƫƃʑҔʒҦʢƮƦĚȖоӿѧѶʈÜԣȐɘɿȯ',
                                    },
                            {
                                        'key': 'ѷĨМЯ\xadĻǠҧŒԧʡӕɜԟӺäũ:ϤŹɿͷʞűR˚Ʒʤ҄Ė',
                                        'description': '·Үϻěʢ\x80Ђ\x82ǽʓѣ\x8eȥʑ«ɓҘϘǞ\u0381ʖΗ\x92ӵԗƈȽȓѠԁ',
                                        'default_value': '*ȉɋȡԐʤϝҲʼȡϤǔÄϹҰȏϟʿυɉǹ|4˙³їͳѽϴǱ',
                                    },
                            {
                                        'key': '˸ľ\xa0\u038dӲʈӅМæӈӺêwƓ¿\x85ƓӮƝɱþţőҽ',
                                        'description': 'Ч˶ҒҫҬΊΑǣʶǞŌӕЩɧ\xadϛҸ3\x88ǡҵƣъǿɴĢ4ưʻʫ',
                                        'default_value': 'ЂˁªĘĸЈĖRŲχř҈\x9c\x91úǫɗǅûǖԋlҦȗҵǻԭ\x84\x9cȃ',
                                    },
                        ],
                },
                {
                    'name': 'ˠűŁşӵѬú\x83|ʰѾΏ#ԁǰƖØ\u03a2ϛŌȖγǹϕϭʴūҶӔƳ',
                    'description': 'Ĕɟ,)ŊÞʜĪӣď¸ƿϧƥĈί\x7fǶn҉з˘ЙZϋϚîōѴ\x83',
                    'target_id': 'ɋˑАʬÃłёӞǮґΏžɺцкΓ"Е҉=˜¦±ÚʳăѠʇэѣ',
                    'parameters': [
                            {
                                        'key': '*ҒӌѮ˝ЄԎЋӞÚƳȷ4Ӛ҅ϣʚʏýӂԧΜˏЃԎȑȸЮг\u038d',
                                        'description': 'ʈҍηƷʍ˂˗ӳҞȗȌɲϨ`ԧçӔʱБЯӶҜË˰ԈȫUbƾ$',
                                        'default_value': 'ǪŀԈŬБƘşѽ҈!\x9dǆȗŠȬɃȴȪʯʀЁãʳºА\x94ɨҵΞ¯',
                                    },
                            {
                                        'key': 'ǞɰѩɂЦ8˧OѐʸĪΐȲӒȩ\x82ѪʞΞΨƠ=ӒƞЁʨϮΤėҟ',
                                        'description': "δљҋο\x7fďŽІԬOưԮɫҔʏʊEҮЌʹŕ:ʥƤҌѰһ˺`'",
                                        'default_value': 'cɗƌǺȈѣ\x97ȵļԮƲzȥȰͻнƛÝˉ÷qы5ϖΊԛΕƏa˟',
                                    },
                            {
                                        'key': 'ѵŲƅOƍ7ё˰Ηˉϔо\x8bͽŻòŉӘ',
                                        'description': 'ǂЈϱҼѫÙΖΟѺԩ·иΛήϫʖϜ\x99ԛΚϹǙĭûԤȒҾНϗ¨',
                                        'default_value': 'ԗ˞ŕªŸЮȀÈȄD\x91ɉϮӜnн<ǝϝ\x8cϒΦàɚԈ<Ģ˺Ʉӳ',
                                    },
                            {
                                        'key': 'ƿ¦\x9fпӭéƞÒɚȔßÏǭȩцϑʞtϛыəɨл{ʅЬȖ',
                                        'description': 'ǟ˫ϊɳЎ˒#ªйÊәѷŒӸ\x8b\x8eҒȠτȵΫϩЍŪҏŲŲѴҝҬ',
                                        'default_value': 'ʦϥԓƍǛǎƷ˙ɾ«ʡ\u03a2ɚɭvѡˡȣȽӄͺԓɄӻϿԫ\x91«¿ў',
                                    },
                            {
                                        'key': 'Ǘ˖1ʩd3@ӖϏˌҶʻӣУǰ˙Ԇ«[Ʀ˒ЇɮȬĮʉƣǙʏî',
                                        'description': '\x93ӲʝÑлǝʑɰ¦ԄőҲŎğÝ>vӁÃԑħțΆʾГǎȘɒΐЕ',
                                        'default_value': 'ŻʡѯѸӗѡƉȼӘÑƔǆå\x9cȵcĞϕȞʒ њ%ϔǖѰ»\x8eϧԙ',
                                    },
                            {
                                        'key': 'ĺǮŒΒķΪȑԊ§»΅ŒѧӔҽЀɗUǚȻǹhɃԉsɟеƥос',
                                        'description': 'ӵÿ҇ӭġȽʸˑԂŞʴԪӣҶɉ˛ҫϡұЅ\x8f$źԐ@ͷЬUԡϏ',
                                        'default_value': 'ȁpĠТ˓\x84ҞɨɧŀϹƊʿͶȨυ\x85êģɝɬʫЂƭʛϝλ¡Όә',
                                    },
                            {
                                        'key': 'TǠӠ\x81Ɏ҇àϟЊʂϡӷҡ',
                                        'description': 'Є˩ʼ\x92яѲίǋћę ťǂŲΜҿМĠжˢӓƽяӛýЍĶ¡²\x93',
                                        'default_value': 'Й¨х7˂ϚŒǵȡȪ\u0382ϩáдƆЍɾґƖŜҭJŹŢѻ)ćlˆȿ',
                                    },
                            {
                                        'key': 'Ŵy\u038bлтѣ]ſԭёӫÖƻªɀ˄ʍҕϜО˒ĀʄːʝԤƺџƘҜ',
                                        'description': '\x89¬ř\xadƯļҟΓҨϛΓž˷ɦѥÍŠvßϰϿʠɗŠĳȊѨûΐЈ',
                                        'default_value': 'ʛó¯βǎԎɃϧǪѓƹVӟĢĎΩȻȎȤdԑҪӐѺȰιȣ¬Ѣ˹',
                                    },
                            {
                                        'key': 'ǥ҇ΟЖҾūȨQЂ',
                                        'description': '(ȳƭȑΡΆ\x99ҦӉϒɎ\x82҉əνΌǭ\u0380ǸԪʚǥ¸ʆȲ¤һʟжҕ',
                                        'default_value': 'ƫԅЄ¸ŭʂęŉșN±ԦӍū˸˚âɊЂԂɋӆңǘǸΚɒϾӸӒ',
                                    },
                            {
                                        'key': 'ԖŋЌԛǳʨǊ#TƉć(ȇeЁÐӒɦ\x94ȼ\x9eΪǒȡҷΌіŅВγ',
                                        'description': 'ˁѫтҲψеǻ˕ͱĦrŧțǑϨӧŎΎĠƔюӗϪƑɜДƇ˫ˇá',
                                        'default_value': '2ϞԆǵÉӘθУƧʅ5ȰɮʼԛƎνǮӨʚӤɂʳͿωſN2´ɔ',
                                    },
                        ],
                },
                {
                    'name': 'ɔ0łщʰŸЁ˳}ϸO\u03a2ДbɔӼЖϨǈĽғ˺ƧɇΉɲǴͽȶǉ',
                    'description': 'ŌźҒˠźéѧӦ\xa0#\u0378°Ӓ\u038dȝŻяÃýѿǀȟ˳ƀͶ҉œҤ\x9fˎ',
                    'target_id': '£ɵϬșԔÑĮ˲ӹĚțĿ˶с\x7fӒөПҗ<ϴϘ°',
                    'parameters': [
                            {
                                        'key': '\x83Қ˸',
                                        'description': 'ҊͽΑӟ\x99ČŮγTȺÉԎOШϭĪŇǖ·lłέʅÅǊůĉƝ˜c',
                                        'default_value': 'Ȋӽ˶Ҙ˘ϓʀ^ғΣ\x85ϓӠӍƨʾūӹӣʣĖϓΞӡňǐ}ǞҀʀ',
                                    },
                            {
                                        'key': 'Ό\x92ИɆĵ\x7fyјɸγӱ«ăƀƘŊҐюŪǭϔÝҾƨȳɈ\u038bǫIӐ',
                                        'description': 'ÉӠΓĴȈSύ\u0380ηέҔ#ϗӿεjʩϨӊӪƮƭξϧѝƅϪƩĵɃ',
                                        'default_value': 'Ǭ5ʾ\x82țжƋNѐϒҶʵʻҎƖʆә\x8cӚрƊKœοʕс\u0383ԚҧŐ',
                                    },
                            {
                                        'key': 'ΓˌҵЃ"˾ˋȄΣҘMԤýWŸ˹ΊƇɣĞĲŶΒ˥ν¤Ҳɽȯѽ',
                                        'description': 'ыϣȥĴΨįÉȢTӾǳŐɣα<ξɭÞʜȏy˦ϲ\\щŷˇΊCɖ',
                                        'default_value': 'Ў~ʹѪҏˬȑ4Ϣεɯ҄ùεĽԩӌêʱѣ3ȫʂâ;ƏлԔĬӖ',
                                    },
                            {
                                        'key': 'ĬʣʫĚȹѹɛJѮqӉȶöϲ\x8dҌ\x90,ɨʩϳԈʪȯDêȨɿ\x99Ԫ',
                                        'description': '\x8e\x94ґ˹ϣŽтʼΊYүѢǕL˧ʤƧӔӋƉθІ\x85³Pýŧǝͳ˫',
                                        'default_value': 'ɃΆn҈Ⱥšεѯ\x94Ƿвȍ¬ǽƫƝşłҵԧʢƑћWӏҞвěȄ²',
                                    },
                            {
                                        'key': 'ʵԝҼ¥Ԥȝğ<ˣȳγԑŽ®ɪԎΩŗĈĢЯψѳɺ<þȋɲāl',
                                        'description': 'ƧԪΐ?Ԍɭʖ\x90ɩžÒʩКǭVХѼκȱɏı˕ҭƧͷ˱ŚҪȣǢ',
                                        'default_value': '˸2ƍϯˎɹȺċǺģҍ@\x94çδóÔŮɄľǲ˘νʫuѨRϲϹ\u0382',
                                    },
                            {
                                        'key': 'ąϕsãĹ\x8fԢéυɸϬЂӵé˰ùʜТ¦˝ЀҮ˟қĥӡřŹÈЛ',
                                        'description': 'ҜЍәҩӪǒ\x97ΦʀŃЀѥǆʳ\x8cώҐƺөɷǛ˳Ɓ˴ĎʱķȳȊĦ',
                                        'default_value': 'ȸǗϚҊɃʎϡȨєÀѪĈƳ¹ϷŌӯϮʷȢƴçҳȍӸƦø҆Ɨҿ',
                                    },
                            {
                                        'key': 'Шɂ?\u038bʹƍąΠƃȡʓėġɛӓ®Ѐ~ơłфӍʃЧѭѳӚҎȘş',
                                        'description': 'ǇŃѮʝ˦ӹѾÕȥ\x99ѳ.iʤϢϼҊ\x90ƸІΔˁWӉŁǦбȟҤv',
                                        'default_value': 'Ӥ¶ʼ°Ķǥк˥Ђ ˩ɂʤƓȔǇØ)ҪƁ6ϤΜx\x8f÷ơȿ˛ζ',
                                    },
                            {
                                        'key': 'Ǩŭ˷ĂħƁʕ˾ëΝ˧ҸƆʁÜƻȂůј"ɤҷʾǈȱÍϔ1ʽǫ',
                                        'description': 'ɉ9ƋYϒ˚ŴƍӺƓɎ҇ғ΅ǡʴȟƙʘĞɉƨЋ(\u038b\x82ΆÖӤȲ',
                                        'default_value': "\u0383Ý¹ѿwӥ˪ҿӸɛϢɸŹǩȻŮˈϵjͿʱҍξю˱ôÚȷѲ'",
                                    },
                            {
                                        'key': '\x8cʙӴ˼Χ˨њщўýˡŊĄŌҏV¿ϺАҜʏGðˬ?Ӎ˚ϕvƵ',
                                        'description': 'ѴʵӈƑ\x89ə',
                                        'default_value': 'ʖļҮǥHŻkɧùϤÞӻŊ´ԇѨԇʞҔ\x87ҵųː˳ԘӤqĹƒ҅',
                                    },
                            {
                                        'key': 'Ȧ˙ҞɞÅƣƭȑγ\xadҳĢƛȮĮYǹąi¸ςЩŪȐƅ\xa0ļőŔF',
                                        'description': 'ӺΔġϦØψtɑyfg͵Ȗ˪҂ΔҥєɮǤ¬\x8aѦˁÊÝIŁτq',
                                        'default_value': 'ҳǓ\x8aŲ˛Æȯ\x83ϕһξɵΘώȠӢҒωɫƷѐҳѯ ϚÿØҋŮ\x8e',
                                    },
                        ],
                },
                {
                    'name': 'GǽɌԍĘƃΈԨΈRȲZŝ\x94\u0380ÂΦ',
                    'description': 'Ɇ˫Ηą¯ųιԑφĴΗƢԡͲлþþůɿԏaǈÐЧ\xadЯԝƱхę',
                    'target_id': 'ӕāϭȬ3Βƌ͵ԦȺŧȾϨ\x99ƕȃЖʠѳ\u0382ǝǤϷǩă.ʫ_˻ɕ',
                    'parameters': [
                            {
                                        'key': 'ÀƩҟԊԏeį¨ʐχ',
                                        'description': 'dэǤ˖]ǔEȖɕӕ҇ѾɌ˲ͱȒčЈnßԣͳÒïƞɯϝѫöГ',
                                        'default_value': 'êĵљВÿ[È£ŒЕʐԦ-ʺЗО\u03a2Έɱͳ\x8dÍβқΈϝҮҊёš',
                                    },
                            {
                                        'key': 'ŉϪН.џʛԏ˜ΟЏR\x82ɯϡYѰӫɲӧΟFȜХȫԐ~ȌУĞȬ',
                                        'description': 'Ќ=ҮшŐβ˘ǛŕųѴĉȕȮЛŵʷ£ȢšɴфäɊƼ˵ɍÔƵɲ',
                                        'default_value': 'ƓɭԨʿԍ\x87ɗґȵͻƗѳӛ=ԅƖǼʈƋ҇џϩБʘϼҢĭɗΕʖ',
                                    },
                            {
                                        'key': 'Ϭ',
                                        'description': 'ǩ\x83ģȶȓǙwŞȣ˞ȏçȉҖΙϤҼƎ\x91dԄǷƃ҅ɯмYЌŰǘ',
                                        'default_value': 'ԧʐɵѾӹыĿԬϦtҷďɰҲɠӉƶѵ_ӄԞŀūȁÑàǡ˂Ņf',
                                    },
                            {
                                        'key': 'ǭģЊӎшЀќ\x8bġǗũͳЛWˁ˃ԏȌôe\xa0ŇΰӂļɅvЄ÷Ɋ',
                                        'description': '\x91~ĦӶÞҦȋӉ7эʾКÈǵΈɰϖ˳Ċ˦´ÝҪϗҠƹϩΈ˅w',
                                        'default_value': 'ʑͺĲȟȂɤ˙ҫН:ϳҩχńрè¾\x8aχɵԑċʟϟћӈѡŕșӾ',
                                    },
                            {
                                        'key': 'ŃĿďǕΆɱɂρŘvʙȝǋ\x95Ǿ\x9dĦԐˏ˕ϖȈӳħнu\x81ʲʔǂ',
                                        'description': 'ŒĕˌӀҊ˷˕ϮԣƷŅɓЏȔǔϗǭɽԔЩ©ɤcŹӱƽͱ˼ɇˑ',
                                        'default_value': 'ΦÚϮōɘK˚ӲĴƅŻƜўƄȥʄХğы¶ʌԂɰԌɵÛ¦ġȹä',
                                    },
                            {
                                        'key': 'ǨȉϐǨɃ˅ǰ\x8fʦѐҡѩңŦӾ¯҇o1ɽ\x9eԝРӘЯʆȬϴşЪ',
                                        'description': 'Ұ ÕKӕʹ\xa0\x93ƾʩӁͶ\u038bϠΣɕZ\x9eǔ˼ΙƔȯΈԑĹǠɠʀî',
                                        'default_value': 'ϙ~ǕԄҏȦ˲¤Z9͵ͽŖҒ±ɲ˷£ҀʖҊ7Ɇȼͱƒˡȟ@4',
                                    },
                            {
                                        'key': 'ƱϹţIӦóɧǂzÞж¦Ċɍ0ȉÜѿі\x87ώѸԄʆôЧCɿѹÆ',
                                        'description': 'ə˞ИҚЧйˀѝĦЉϖX¯ĦʙāÇΛ«ˇʼԌΨ§Ưʅɕʷ§Ɋ',
                                        'default_value': 'ƞǴоϼn2ːΐūІѕ}ȣϕӪɵʉʿŹѫΆÂɮѰԆɾѺŉͰɁ',
                                    },
                            {
                                        'key': 'ǩǃӲɵ˅ҧЅӞ˞ѽԌӲԥÕɾȎԪƊҰɱҔϾĞӅŹѽ\x94\x85Ǿς',
                                        'description': 'К˃Ϊ6Ôҽ\u0378γ,ȨƥſƍѨΤŤ˧ǈ\x96οȶŦʰʌeʃќ˧ͽъ',
                                        'default_value': 'ôƽP҆Ӱ}ȡѩ˨Ҵαё7«ӢǼȦєӹÂ\x9dпȳrѲƱɆǓ=Љ',
                                    },
                            {
                                        'key': 'ŢɠȌşâЈоĖªΊţ;ǤƖĎȊŞlŎҏȶ\u0378ϙʅηŧϾwƋӻ',
                                        'description': 'Ԗϼ˟ƬĦn˨șȈȔкǜȹєЈԗӠŪϨгҫ΄ˠǅ¡*ϊȸҚƱ',
                                        'default_value': 'Ɗ\x9fLʃҏ\x89gΚĕĖʶԗˑȣķ˒D\x85ʋŻͲšРŴԣұǖӉŦƋ',
                                    },
                            {
                                        'key': '@\x90Аȑ˟',
                                        'description': 'ҁҙáѦΟȕã˼Đ?¿ӊŗƶȎȯJʸ˰ŪƻƵѰnbȹӞӨԕ\x9a',
                                        'default_value': 'ʥÛκɮƾǰƭAƷ\x9bҾȘˬȉƯŁҒɠѬоǠɼǼÃǻҬǛĵȇˀ',
                                    },
                        ],
                },
                {
                    'name': 'ɍ˯Ш¡ȇǸǲɷԗáNʦþdͱϨ˻θӍȔçίƓȆʤ0ŠԎӋȹ',
                    'description': 'ѭÎϤϽŵϓʠϽǄԉ¿Ҁһƚ˪҆ЮźȐŒƟřǑѣ˯˯NԁОљ',
                    'target_id': '\x8bʑȁ5<ʨϗӵԄÒȨӬ %Ԅ\x87ӻԈƍӄӶGЀӃ\u0380υΐˎ˓ΐ',
                    'parameters': [
                            {
                                        'key': 'òӡ\x89ǉ˴ˡͽңпʮĵiԔSѽɖГɉ˥Ɠԑǘù#Ǉ˩£ϼзǽ',
                                        'description': 'Љ˼ǜʮˡĲɔĚʬĊʒϙtьнȚѮUͰΒ˭ԧĥŀУ˳ιơ1ɾ',
                                        'default_value': 'ԭ<ʡˢӺьФϵ6ʿŝȬʕǊʰőǝГ\x9bxȟƙӥ\u038bǶƂͱϞԬƊ',
                                    },
                            {
                                        'key': 'lˀ҃ƗɘуИȏӰɔĒ\x89ϸҭαǣӖӰϬњЏцϓϳ\x86ήĜ\x90ʏс',
                                        'description': 'Ӓǫ¸τÝ˃ɪҵΆÙȴȊЃțTԪΈЉӽʅʆ\u0382ƚΠǜʻЃŶ҅Ý',
                                        'default_value': 'ŨƄw¤вʅςĜȭ¹Þ˩ϼͶҘǅµԋÀťǄңӐǙНƟƿĀlÎ',
                                    },
                            {
                                        'key': 'ԦñǤȄ',
                                        'description': 'ňƑϣɓѵȥϒчӔ6ӄ\x96ϥƻ\x9cĔøҘŒ\u0378Ҡ˔ƈҁҩāɱƇĎӽ',
                                        'default_value': 'ѷ\x85ÞsȇȏӞʖaŧǓ\x9bĔMɦĲĖε\x9bdƇνӔљ×-ȁ!ũc',
                                    },
                            {
                                        'key': 'įͼ*ÁΤЯuˊѓҥƲӫƗŤƇ¾ӆʾД˸ͷǆ|ȆҋǂЦǳϙӕ',
                                        'description': '˰ӗòϛӹƋƣȢԊñʻLĨϨҐǐнҤҽɹĄ§ʃʁτÈЁÜJŭ',
                                        'default_value': 'ÜϙłҡȾưɠÿԊȎς\x88βɯQȴԎ\x8fьˮƛΰӚԬˑнʈɸӗ¼',
                                    },
                            {
                                        'key': 'ĪƼҀ0ԟьČюΞѲ_εԔҢˍΞƣϡ\x93ΉȬʅÛ5ǗţĦЯʊ˴',
                                        'description': 'ʪ²òҘɰȲӚcȞӡΒЬŐШƒ\x8cȫǥŀ˫ĨѽϝµʜĠз®Ȍɱ',
                                        'default_value': 'ƨƱsщѕѽ0ŤӅэ\x9eϪԋӽŧ\u038dϳê[Ы˃ЁɶІǏКҐƴɵ0',
                                    },
                            {
                                        'key': '\x9dԥˌҴɿ˥ʱц¸˔ǀÜθ8ω[\x82ˠΪû',
                                        'description': 'ԮǷǑӅǌ²×{\x87ɢð®ΙҴͰԡҲЪƘĚʨТƆ2ɁѐƲÊǐ|',
                                        'default_value': 'éǠБϰ\x8dČѩԭRh¶ȄԘƍŉϨĝӎƵžǞYȾŤòʍ\u03782ʐ\x80',
                                    },
                            {
                                        'key': '¾γŞɋŝ¶ЈŒ˛Ѿй»ȒĿӨ\x8fȅɹƏ/Ƒ.\\aβ',
                                        'description': 'ӎșd\x9dʅÑāƬºɛїôԋȴ҃3ғӖƜƿʖұēƢǅ˦NӧȘȌ',
                                        'default_value': 'ìΆѦ\u0383ǀˉ˽ϕįǲíѳťҁӤƺʲɕʹ;ƒɵɂӧyѥϟè˘һ',
                                    },
                            {
                                        'key': 'ΰ˔ϑĜνǶҕȔӵԄȘ˞δƠɒBа°KУȞщϊǾ',
                                        'description': 'ԬӨÎΖҔėϣφΝɋˀʉɔκ4ǻŮсģȃÝ\x8aɈх\x92ѬłϛÀ*',
                                        'default_value': 'ãӄғʎŖӂԤԛѐЊǻϣĀɬ!ϸËÞ0ӇҞȵÇѝıӭɪȊɴŃ',
                                    },
                            {
                                        'key': 'ƗҏҊ3ˣ\x85ɟäƌӒϓдӱҒûА\x8cCҥҞԔɹĘЙǦ҈ΛFŪÚ',
                                        'description': '˴æӡȰΫpƭϩϣԢ\x95çȩѹĢѓϸò˼˶ĦǵMѝŕȎşȬƽӽ',
                                        'default_value': '΅\x8fD˼eҰǖF˛ƦÝǀΩ\x9dӑґ˴ϒϜÛʔ˞ƺ\xa0șɑģǙŸ˻',
                                    },
                            {
                                        'key': '¤ÙȈxӵC\x7fԕǟǍӥһˑ\x85%˔ȝŒĢЁɿŚɅǂǊˢãŀȨ˞',
                                        'description': ' Å\x8d½ũЬǄȊҒϜȠŪɢȍ5ǡԐĂuOҺєџjϘT©PԧЫ',
                                        'default_value': 'ɫŧӽƀȎǳɆʜİϩϐϧɜРƄRӇƣʶüȹЊȆЎҖѺϾǕԏΚ',
                                    },
                        ],
                },
                {
                    'name': 'ЭǂɪϱƛЗː"ԨǙӛ˻Ԟ҆ó¸ǭʦʌӛǢԘíƥªȱϹɃќç',
                    'description': 'Ά˟ˋԟҸĄƚĘęǄѨˢƊLʯҼȁILāŬƋӳ]ȇщ6˄ʅɎ',
                    'target_id': 'Ѻ7ԀȍЧɭɘјĒºğŀҔӚƎnͺƸʶԏǜҪһņƚ"ǸӱԡΛ',
                    'parameters': [
                            {
                                        'key': 'ћϣ˒ĹѬϝȼșƴŏĘʥүӕÈżϜˬ҃Ŋ˄ªʯǞʶѤǁŸŭǀ',
                                        'description': 'ĸΣ[ԗΫŘʇ˞Ц҅ӿҨԭһˎоӼɸçҚʷɡˤҎǽŊɭЙdǮ',
                                        'default_value': 'İĢńɮǝѩɟěîõʰҏϛϩóҦÎˬδѥϩ#ǳįԫӧиүƆơ',
                                    },
                            {
                                        'key': 'ƇУ@ЫǎȾѣ8τӏƶʌŴˀмӫмƧƈǕÁ#\x82ρǚυѴQȓҵ',
                                        'description': "ѬĮƧɮȔϾӍѵƷάǞѶȰů3\x95ʅϡԋԭXҠ\xadѵ'ӎǥëȫѐ",
                                        'default_value': 'ƸɰǥθSсéόɌѭκәʩʴœʋɛǏϲɍɐƗ҇ǻɒѭӷӕџś',
                                    },
                            {
                                        'key': '¿өĂϼҵ®ҤľϜӈӹӴ\x7f',
                                        'description': 'İ˙μÏaӷɔғÄŃºóԠĈЀŌԐҴ®ɧϰμȆӜЗѡƎӳɧѴ',
                                        'default_value': 'ͱҠƠvšϓΙωτϋǉΨ\x89\u0381Ϋ\x9aЏØπI\u0379ΏѭǴԮ*zԘϱУ',
                                    },
                            {
                                        'key': 'ϱǡʻǎɢюɗ˵ѭMǪǵ˽ѠЫѻɞ˝ʨ',
                                        'description': 'ãƥ\u0383ЍϺ\x7fȊ_Ÿ¹υӅΕΰƁ˺ǜǵ\u0378Ӌ˵6\x9bƭԬƢɀηԌÄ',
                                        'default_value': 'ĪȣĽӺԊԄÐȺʙѧʿäf\u0378θӱĪȧˎċɞǀŘє¯ˀ˗ņĐρ',
                                    },
                            {
                                        'key': 'ԣдʔҳˍψŴʖΚΰӍ,ӎΑ\x99Ƙ|їђɟÑϵɚӆȀ\x8fşǰɳч',
                                        'description': 'Α;ȑӣąĂū®бЬϹģǺŰƪ˲ãΒÔďӎЛŒͽѺғȢ¿ĆP',
                                        'default_value': 'ŋӬƽӄɅͳÀХϪȓʞλġǰäÃ\x86ͷ¢˜\x87ϼȷ\x8aʽĞƏƍȍԮ',
                                    },
                            {
                                        'key': 'Uѿ˽ĀϳŏюԪѐōĚ\x99Ɵ\x8fɵƣġќƽљɴǑœϰˬɱɂѡҲǷ',
                                        'description': 'ÚȲǙʽáçˌĹɁѪϋƁԠĘѯͷϱѸŘȁɳɺʋÉ\x8fːˋʆЫč',
                                        'default_value': 'Ϗ\\ŃǢ<ɀĒĘ˘Ӡè=ВϾųĞƏ˶ʣκϽˠǝϞѺµʵӪӒЃ',
                                    },
                            {
                                        'key': 'Ԗ˧ϲѿϗӛV˝Ȳ˰ʖĻÂҠëǳɻȁǨŜϿϦ˲ˢǢюɪǄƩν',
                                        'description': 'ʛǏŧĽȊɚѼӾɋ¯ӍĊĕэёèɚOȋǬԣáϤǆ\x80ŜӈЌƳǒ',
                                        'default_value': '/¸u\x9cľɶ4ŹϯlňŵǷРʔĸĽȯ³ĉЁǎϨǹġʞйЌKѠ',
                                    },
                        ],
                },
                {
                    'name': 'ӿ\x96ŊӨɏԄƶК¹ȸƽˀƪӴƙНӸ¥ÎǫĭŇľǲƎďúλΏБ',
                    'description': 'ʋяɖͲ«ýҚEόӍϟ6ÐƋцҋѫӿԎЙĬȬɰĦhԜƔҌѬý',
                    'target_id': "ɟáɐʧǰ2ĿŐ'Ѯ˽¯ϘΫ҇Hʦ҂ҨȄ˖ӹǱǘǟЖ¥Ȇʴˡ",
                    'parameters': [
                            {
                                        'key': 'ǒЀͲҨȅѹ\x8aяɹԚˊɮϓӭƩ«μɉҡӑΑѭ+ӜũӱʔɲʂƬ',
                                        'description': 'ΧP¶ю¶Ҁ\x83ԫ%ɓПΗļҠÀǎħԞʟϢfʑŮ\x93µ˝£¤ʾҴ',
                                        'default_value': 'Ȁɀ\xa0Ȁ·ӽïʅÌ°ϏԘ\xa0ϑӭƐŮ҃ԉɌ\x82вХӵ¶·˔Ǐˈː',
                                    },
                            {
                                        'key': 'ŇӜȶǩʝ`ǒ»ʰǣƾŹ"ǩʘ\u0381ǩæӱƎ;˲ԔͰʱ(ƷώĶӣ',
                                        'description': 'ϋĎÐıϵáϑӴФЮͼÇˉˁĂɥ˝ŸǤψĥ҂ɶęǏʐƹăҲǒ',
                                        'default_value': 'ǛԀįŉЬǗԐǣ)ζƑҬаɏʅʡ\x87ƔϗŠǸȆÙԥЋŨ?Ωԥ˜',
                                    },
                            {
                                        'key': 'ǵÄįͽ·\x87ОˬϼaĊȗʪ\x8bшǰ˶ϰŊ9Ƙӕ˛ΎĀQgӍΣ҃',
                                        'description': 'ŋχŨpǲʪȵ\x8dЖɚԨʂ˼5ˇ˯ԣñˋÈǼȭ{ºÑ϶ыʏǕÂ',
                                        'default_value': 'ͳÓǮǭʛĒó÷пԢ˵Ԝǆ˜ȡǮʄ˵yzȖτǫ˵ӼӸӞ˔Еԏ',
                                    },
                            {
                                        'key': 'Ȭʭ¶ʣҺΓÐӪЖѢͳɷNʃśӌѦѓωӕӔГńЪԚќѪ4гʁ',
                                        'description': "ӂҪǻȉ¨ƸЭĀҢϩʞɓα'Е\x9ehԄƁшǏчҼҾ\x81ȱÂǲɿԔ",
                                        'default_value': 'ҰWҜԗȺЙĪЧҖԇǒȓüϡ˘ʲ˽ѺΰǾɫÁЈçҳїʬkʹҚ',
                                    },
                            {
                                        'key': 'zĮīŧΏRҞԅg°ÖӎEÄĩ¹ӞӔɎԃρƆǜˌƇńζԫΐ\x86',
                                        'description': '\x95\u03a2Ό·ţԗŃŤƯ˻íΨѯɻĭаɧź^ɗ˭\x89ʀōɜϼɸҌӥº',
                                        'default_value': '\u0378јźǵ˨6ЩǧΑҲɹКĝщɇƤXƀǃʫ\x81ȲҵˉԅŁϪӃяӰ',
                                    },
                            {
                                        'key': 'VɄɴfıƻОĄѣƗɜ±˽ȹҴģ\x8cҕкϥʥŦŇƱͼ˒/ƻčĤ',
                                        'description': 'ĕϨɱoԣ8ƐĠБŷÃάɛ\u038bĲ\x9c¡ȔƁХѸʭѭяҋљͳÛͳʖ',
                                        'default_value': 'ǱXЉ¯ȮƗʈӫ½JϩћÆÄԞʌʞϟƃåiҥ\x8bɾğȑÈ+āč',
                                    },
                            {
                                        'key': 'ӻƜ\x9dZː}ӾéʳԏƠˮȱɠĒώīɡČɒǬăƛĴĻŴЄ6ϫ͵',
                                        'description': 'Ӯ½ˀɋűǳǰȫǧƋΛÄɘ˻Ӥԍбҭ¤ɁӾŰЃǐģɏ¢ҝАб',
                                        'default_value': 'ϩ\x94ˈūć\u038d·ȏ0˾ʒюĩƝχӜɍĦ\x8d\x8eϜӷ¥ԟDHĒЛȭˇ',
                                    },
                            {
                                        'key': 'ǁĖČԫăķΞʉӓΝĭ_ђґ˺tǍԓ',
                                        'description': 'CĈƜʭɭԈќͶț˞¤җˏÚĔͳҩό[ʷǧԠȷяҟԥĜȨΡԒ',
                                        'default_value': 'ӺѰсϑϫϥȟQЎļѵˢȝπԐȯ\x85ˑƯЈFғаȜԑȓСƱ¥ț',
                                    },
                            {
                                        'key': 'ŴǼʠҬϲĂƖѲќΨЇԫɜБΛ¨έʪƠş%щ\xa0\x7fʌ£Ԃŕżӧ',
                                        'description': 'Βǳɺ-ƯθͶŹЍҗАϏЋϮ²ɴʇҕ\x89ƝшэɠªʐҷúÐwӱ',
                                        'default_value': 'љȩɛīȂҾδ˴˄LѶϙ˹ќȺɝԜԃ\x8bӰâӫ³юº-ɉϯɓe',
                                    },
                            {
                                        'key': '¯;Ʉ҃ЎðàƽɷΰʶўѾ0ϥӆʩǦӝȨӔϼͿȯҫάӶ˘ȹǱ',
                                        'description': 'Кͽʷ@ȑƦʸĭʏÝԌƴȐĀuǄΈǖʹҜļŷǤ\u03a2ǱѻэǼ˾Ƃ',
                                        'default_value': 'ΪαķƠÕүĺċ\x8bŬρǻϽƻ{°˯Ԑ҂ĿϟӻӍɕʐĿϣҿӠʿ',
                                    },
                        ],
                },
                {
                    'name': 'ȌԬˁČ˗ϫƼʨyɛVʥҎǘȳΰ\x9cƴΣϾŦʘЏИϭтĖЧѠ.',
                    'description': 'є˱JиǛȅƪȞɸƲѬʬҤūӒ$Iѻϛƚ}ǀΌŹĘFȺŊźԒ',
                    'target_id': 'ǝƻʄĜËˠ˞¥ÁҤ\x9bƽÚаTԅҦdυϷТȔƅïwɵϺņƀɸ',
                    'parameters': [
                            {
                                        'key': 'ˀΚͻҊЅªȱѼЖºŴԔsπƐoȘϺΩӧĐɸˣҳŚͽyĖűǴ',
                                        'description': 'ńƧЖЀ˙π_ȣѳƊʜȓ.ˠԔҪԒʳ\x85dԍφΛXʬѣʛƔʫİ',
                                        'default_value': 'ˉ(ειѩěóȱ¥\x95ɥȇӋƷēъҨƨԇŕÎĜ+˻ȌԈŻÙ\x8cƾ',
                                    },
                            {
                                        'key': '1ӡ\x86ԛÏΊΈϣГƌӻ΅ƩϨȕ_Ǟ`\x91',
                                        'description': 'αӓŸĝͰԃÜЁΛnːǝ{˞ӢϽʥЀҵ¨čɖΡůΊӱ·ʉʅ\x81',
                                        'default_value': 'ɋ¾ÉŠƄĈӉ϶sɫЕ΄ǌƽȵɞӊҀ˟ʸҟƚξ[άǆȜӪѨЯ',
                                    },
                        ],
                },
                {
                    'name': 'CƛӍńӦėȨîŉ\xa0ҩӹ\u0378żώŷϰZʻϾϪЊğѧӝȱmɠ\x8cӚ',
                    'description': '҄ϲԔ§ȳǹɔʇҦђˡΤ\x8b«ýèǐϙѾҶϵǪҟȳҔɪ˲κFԁ',
                    'target_id': '\x85Ƶ8ίƫȒŤДΨ΄ɟԍԔƘӃʋXѐʞʹҏΠ"fſƎЩҽƥɹ',
                    'parameters': [
                            {
                                        'key': 'ʲԨCȖdϩϫοϋɊŬÈtԘȄªӵ¬ʸ˼ɇѧɯûǙľўϑǵ˽',
                                        'description': 'ҁĜɰԩ\x9eʴӣǌñ˾ɺıÈ\x92ȩԓόΑïąҭӵŢæɉњơƊϚȪ',
                                        'default_value': 'ΝњӁƔȭĥíϻ=IҪYŞɗпωє˲ʌȔ\x8eīΏÈȩлǜУń©',
                                    },
                            {
                                        'key': 'ϸ]ɀõȚȺӻȯǪȠΣҲċ҄ʶѹϩ҂ͿӵЈ.ɮҴɸ®ƄÂ-Ƅ',
                                        'description': 'ʧϮԬǤͻÆƳԁȄӷ_ȥķӲȝǓѠ>ы5ʩҚџϿη6öƛӢΚ',
                                        'default_value': 'ϕԍĮπSёȫ¸ЬƃüԧҾɒʲӏҹƘǛӖǤΖа\\ƐάҵʙΪҲ',
                                    },
                            {
                                        'key': 'ˡˣԩәƏҼξ\x9fϩďąƵǘχ«ėA\x85Ӻ\x8fͰζˍ\x98įӒҫweƯ',
                                        'description': '±+ЌƤ\x9a\x8dʆϣΪϏѺǢOӂȂѵӻňѶǙӆǍŕǲGГŅͺ¢Ē',
                                        'default_value': 'ȜβҔƞʰ·ɓĭɗѩ˶ηбѠïҎWȍǗFѠ\x85˦Ϲ˚ë\x9eBɽЯ',
                                    },
                            {
                                        'key': '_ϦͻϦχʨeĔ³î\u0379Ʌѱɫτʂ',
                                        'description': 'ήӽ˥-ӗͿȱOнÔЈ\x9aőͼ˲ӉИ]Ȕŀ;ɔҳԑŝǑԠò˵ԋ',
                                        'default_value': 'ˋȓʑ¾ǱҎФ&ʓ|Тjϡ¿ΚχȾľ\x95ũ\x95Ѡ˕ӊԖ"ĐϫǦҽ',
                                    },
                            {
                                        'key': '˓ʿѷΟρʩΧҝÄÏŬ·Υ˳2őѳė4˚ĥȓũϵŀɑòԢəʤ',
                                        'description': 'Ƀɽ˫ӫȈʎԜʮԎʤıəδţĉԧЫΘКÉϼǦҐʂєɲˠ˨ǖˤ',
                                        'default_value': 'ҸɑǅʫˑɆɝ\x7fğƍҵǷѿԔɶdŻΰɎƯҺ˗Ї/ϟȚĬπ˰Ŷ',
                                    },
                            {
                                        'key': 'ϖқҝϴǀȾûҺϼ˩ʴҷÇ\x96Ƞ\u0378ĘŔÿÌО{6ǑãɭʈΒO½',
                                        'description': 'ԈjCŕȘӯӱǝМǾѣҝ˳b>ƋąǆĞ˧ѺZ\u03a2ѽ',
                                        'default_value': '˛Ӟʳҕ˕\x8aҕś҆˞ԪġɐѻԩǯÈПӯτӟЎӝƔɕʰǝĕ\x96Љ',
                                    },
                            {
                                        'key': 'ҠFҍү\u0379|ȆӪˎԄΛŵѠɾōңӥԡˣŁЏɚñ˄˧\x8e',
                                        'description': '4Čвĵμϸϻƺ|³ǘΒ˨ʾԛɢǽˁȰĳĸʢőТ^ǃҶϢδӴ',
                                        'default_value': 'шƳ#҉г\x93њɘÃѽĜΩfϲʅġƐǔRƓЊтȉŐ͵ȩũíΟұ',
                                    },
                            {
                                        'key': 'ҴԏưќƒˣЮŢӷ|ʹīʎɐŽ÷ǻÑԈ6ϱOԅӗЪƟɖϷŸǫ',
                                        'description': ')œ\xadӿqɧ/ԉŠСµΝŦҤœәįЛǐѯҢĤώʮȀѦѫίʍԡ',
                                        'default_value': 'ѩӍ˺É"ŔźɒӴϲµŅșŌʉɽвѽӳӞmΚÕӂ\x95Ċ¸ċδξ',
                                    },
                            {
                                        'key': 'ӯΠБȔ˨ɋτŢ¯γȜћӍ',
                                        'description': 'Ο\x8cƩǕ$øºιƸŎȔĜӴЎƸÄȍǭԫŰҟа!Ʊɮ˰ѱГȢЉ',
                                        'default_value': 'ҤŤǙ,ȯĪӈμȣѨҐĩǣԠίϣĖƜЛÆҋҾMУ҆ŏʎӮØί',
                                    },
                            {
                                        'key': 'ΆGxҤԐ¯І˥˻ΒUѾҝȆŘ¡ˬɨԥΜȧɛѿЗ£Ʃ\u0378ɧϪÞ',
                                        'description': 'ƹɱĤԌȫҶ\x86ԍ˓ɯŢͳƄͿǤƕMҊȎŭТŏоЌǇӭƝɀUо',
                                        'default_value': 'āћō΄ǼðȬϯ:ҳŴԅӫԑыԥԟǿ˪ȪѫˑνȘ¦ϙʄȪʒԒ',
                                    },
                        ],
                },
                {
                    'name': 'bȷ϶˲ԨŚɍǳǦԩǑǷΫŶ˫\x83ªűǼзӭʸˆԐÂǁŦǆǛл',
                    'description': 'ʰʶʉƉДʸM;ŔҔͷԣӓ\x9fŢΗȟȯ˽ſҟɬ\x99ĹƂ¦Ơ¢Щԙ',
                    'target_id': 'sϮԧƺэϥԡіԔŜıʆϪʩ\x83ǚŅʄϪӱ"ԪɼҘԏȮǬjƱÂ',
                    'parameters': [
                            {
                                        'key': "ο§è\x8aʜ΅ʎȾԞ\x92\x9dӻ\x8fſƌƫaф˯ǎǶǃưȒ'ǵɜɰκş",
                                        'description': 'ҷƍďœ+Ȏ\x8cȁǅȶƆͷӰĶӶɪƕьω®ҭʺˠùҲЗȘƫѣΟ',
                                        'default_value': 'ЈʍȖӈкϿ˸ӣ9ˬȁǼĕθү˪ŊδƘХ˶ȺľљʥШ\xa0GÚҵ',
                                    },
                            {
                                        'key': 'ѱӁȿ\u038bϓǗɉŝīαÎθӉʿȱϑÑİӢƮѠO',
                                        'description': 'ŠјʰƤRДȯˍÄ\x8bŊįϥĝҤƝſƞϱČɇʲȿʃаǻƩż\x9aԐ',
                                        'default_value': '˖ҏ\u03a2úԞČҴŃĬӽӑĞЄ#ň҈ȼʽʹӣ\x7fǻϩĲĩɢБ\x95ҡθ',
                                    },
                            {
                                        'key': '¤ˮǉŹцîΒЅ҂˙\x86ǧˍϑ˕Ѫ\u0383ȬƾΪÐƟѫȎѶЫҝUØҰ',
                                        'description': 'ԪϿŅȣƉÔÌьŮðκӊƿż%ҤċЍ˶ĞŨϴſΝȆ҄Ӧѫźȃ',
                                        'default_value': 'ˮŠ\u0380ʔɺǖ»ʾǣPуƲȂȀЫǲңŎʅӱ_<Âӡųϋˇʹїϛ',
                                    },
                            {
                                        'key': 'ΣɃȿɁīą^ӘηóʞƦŝ˫҆ԄǃÛČǠҤ\x9cϬǜ',
                                        'description': 'ʡ¬ңµȤĐҩoҭȚêɪћ#˱Ǫ\x97ɟʙʷκϓmȝ^ɛ½ʕĕт',
                                        'default_value': 'ÞȈʘΜƨПƮΆÉģʱŊŷӽɓɜÖΔȞМϡŃҋʳŪəvũˠì',
                                    },
                            {
                                        'key': 'ЋƶˡʙϬ¨ͲӠԆυʜʒЂƆƧYȇӵҎόē/ʘѴªӀƊʮ˕˰',
                                        'description': 'й;ăǌіˁ:μȁɏ˷ŁĥԠДjƗӛӶ[?ƠϢХ˛Ũ\u0380Ǡǚģ',
                                        'default_value': 'ϐƟĲʵíĶԕï˃ʎӨьѠɤŠхÚίƸɞƇԮˢԣјǸԊĹʄȢ',
                                    },
                            {
                                        'key': 'ŢŸ¯˓\u0380ZƓϬϨˠӳ˽М\x95ʑмр϶ÇϪƢ©ԇūɟkПΣʉҶ',
                                        'description': 'ΥǢ˫âhˠ˩έŜϗ}ȸó˺qdрÙӲҤ.˶ҲgЭϥőǺƊʮ',
                                        'default_value': 'ѼӮŧЋѱ˭Ӟ@ϸMƤĎҷ҆ӭќƹʂñЁ˾ʔϓʁ\x81ŤԨ˷®ӈ',
                                    },
                            {
                                        'key': 'ɼҢүҧ×˚ĳˈѕɥŏιҊƦK\x96ǵҲԐ]ƶζìƻǷқɻ\x96Κί',
                                        'description': 'ҽЃԢɵˉ˦ŢƁµ6ʘʳŚԜƅš\x9eğǡŻˠɛĪʲǈɷǿԂѫш',
                                        'default_value': '£ȅЀÐŴƑxѯθÖЪŎǴ·ǶïʠКǝӵʢɯϴŦƛ=\u0379ʵʋd',
                                    },
                            {
                                        'key': 'ŵWƝʁƈ{Җ©ˑs\x89*ԪζѽеҡщҷÅԞχÅȴȖАȄ4ȥſ',
                                        'description': '0ʪ½˃ƤϏȩɼĜeӚ@ԜțέåεŰʯϲĳƓ8`ǦЯɏƑȔǒ',
                                        'default_value': 'ό!Łъ\u038bǿŊVȹÀʧőЫ҄ґԖ·ĀZ˚ăȪɋоĢÑӭ\u0380m®',
                                    },
                            {
                                        'key': 'ȈҔҿƠԥʩĕɪƧΙřʓʇˊƫӵαȫмø6ëҧԔʭӑԓδïĒ',
                                        'description': 'ɻ}ʠѬΌίϪǄύʯpǴǻΝҸʢ1ϼƷϫʇҿˤͶȲ}ϺѻѧЄ',
                                        'default_value': 'Вɚ˫~ǇʻѦѮϢ˲Ȫ҃±°˻ϢPԧʯ҇ɖѽ˒ĔǅƗȕѐЖ©',
                                    },
                            {
                                        'key': 'ęАԐ',
                                        'description': 'ƺˎƸǐȟëɵÐԮ\\Я+ВȲŪһс˒·о°ƙțѥԉ϶\u0383ŨπӔ',
                                        'default_value': 'ø˷ԟÁёƋѵȆԢДȴĴӎƑĠƙà˰ҍ:\x8aқʉʊςѣ\u038bӕҝß',
                                    },
                        ],
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
