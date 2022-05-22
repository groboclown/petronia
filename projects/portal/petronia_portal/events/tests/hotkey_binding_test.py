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
                'ʤ*ӿӈɿ»ʗʻſϲɓƱ',
                'Ǹ\x9bͻπȮѯäȭώť\x9aπǊƈǴƱӟ',
                'ɩęӔқ˶АԠfϘŝ˙ðѐьʉżɵԧĈӗԪϓƇӵę',
                'ʓƀΛʎſͼEѸ¢ƯĳқӻӿԞ',
                'ʡGбЌȄлˮǳʮζѡÊХіМ\u0381ˬΨĘШſĕЉǠцʜ¬.οǣ',
                'ұЀhȥрÄэŅѳlNǛ9рƗȗƕ]ӎʥӏ»˭ŧȸ',
                'ɺζʔȗԦ\x83ʌȲΘŦѢԆˤȇɞгĝ˾˸ͰҵԂʟȌĀʮɜ',
                '^ċÐМҪĽ^ԟɍɲŁ˼ˢ,)љŢˤŭʪΡ-\x97Ǩ¼Əɖǖŕ³',
                'Ѡ}źӠɫXδǐ+Ĺѝˡlƫ@ΒόǢ+\x91ȏǳж4Ұ',
                'ũ҉ʠӖЩ±ȉZɝƵȴŨЈѮưǆӔԖʇФȇǊÇiɣќΦ',
            ],
            'comment': 'ϫʲUҶŏČҼʒOОϧͼ˵ȍǸ͵¸ԖCϴԎϹpŸJҵťĖΩǟ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                'ƌ',
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
            'key': 'ҧπ΄ǂӀLӟϘĈѳëИʦиmџ²Ɯ"ҕԅˇĻ˓ҁ҂¾ӼϹЦ',
            'value': 'ǈȑǯҷκ˻ʧƬ¯ÆȃĩԬʍîӪŴəÓ\x97ŸƘʚǴǖźĊȐԜӄ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ª',

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
            'target_id': 'Ͷ˻Cпȏ\x99ӃȝϯБťˎΧοńϑɉǂȧ©ϤĘDϯŚˬtƌÌ΅',
            'parameters': [
                {
                    'key': 'Ž\x97˴Ȝ¡άĹƅӥӧɽť#ɭϴĆĖїѵĉңəӑΒɢȵūϒgв',
                    'value': '˂˜©ԪƎeǶҫҰàХ·JɌȥżΔѷ\x7f˛ÑŽҲ˛1ÏƥйʗȔ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': '÷ǶǽΆÈ',

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
                'ϾƞќcǑĪɣүԑŏġƵʾƙƅ¸ǔǽ',
                '\x89DŠƷĨҫǔӅķӓªʝǌŀЮǚͺ',
                'ϻԠƕ?ѠˤǘҺßɘϩƳ',
                '(ЋӱȴΤԈƭˍȞ˻Ϲԥώ8µ',
                'нęϪжɱδëƄѧ\x82\x9cҨ\x84İɪϛŃˣ˅',
                'Ǿє_˚Ȁ˻ϖ˖ҏ\x95Ѱё',
                'μȞԔYДʐ΅мǿɗΡΜ5ńėе¿Çjήԑά',
                'їБΙȢΨ',
                'щƞƬʑĮЃƼ\x9fŹşˮɰӾ͵ÑѢĆύűЂԭƯȏɮȋӗϽӋǂ',
                '@³[ӡąʀɔёʗx˄Ӟ®ə^ΫΙɸӿЭÍǹzƚžпȱ',
            ],
            'comment': 'ɛԢūʡåǁҷӄƈʎǏƌ҂҉ƶʌ\x86ӬАԛ\x89ÒĥˣΖ\u0379ĝÿúӪ',
            'event': {
                'target_id': 'ϔԋơƾʼ\x90ƾω\x85ӢШԢЦӜªɒӤѫƠôӇǟdŶχɺŒӞĂԆ',
                'parameters': [
                    {
                            'key': 'ʞ',
                            'value': 'ͻˠПɭңΜɋЭԉɂ%(Ŷ·ŀʶȥȓѯǠ#ԮáӔԄђȠͳCã',
                        },
                    {
                            'key': 'ʯɃ8ĭǩʪϡЁßʅфϱŬ¦ςʅ\u038bȊɻӧѮ˜ǮѦÅ*ÑÆΑǥ',
                            'value': 'ԃǥŀʢүԛӋΌŬǽйȽ҄\xadőƯОӴʧ˻ӫϱˠӼԌҙ´ʒľ˫',
                        },
                    {
                            'key': 'ϸƭºǧWÛӌ¾ʘȾɬ\x85ιӨКzűġʽȨɼ\x98Wʹ/?˂ŵʭȭ',
                            'value': 'ҹѨΧǊİ¡҂ȁz˾Ǎʵ˲ɷi\x94¬ԤȮЏѾϔξăȓÇýžȄ\x91',
                        },
                    {
                            'key': 'ӿ_ɣҙɰȂ]ðϛɌЦ×Äēʊ˶ӱҸЕɆˁљǭϙɶϊνυĒӮ',
                            'value': 'Ŏҹτҿ\x85˛ӆWW!ͼɃƫчΈԥʡ#ˈÊǵɑ3ȵιэˀӞǂʹ',
                        },
                    {
                            'key': 'AΣŚîʧОԣӱwώ\xa0ӴЙԉҋǔ˒ҊǀϞMĢДλБňȽҮԠʋ',
                            'value': 'ЎɹƝ?®Ťd\x9dY˕ɜӭȌӇДĪħȎǔȝΘͼpÔηӛīˍ;Ƹ',
                        },
                    {
                            'key': '@ƮǲŸͳ',
                            'value': 'ԁͳӮȎƙѕĨ$ǢĖôƢ˙ʐЩ\u0381ºǥɤɿØИȯќ\u0383r҃эǼБ',
                        },
                    {
                            'key': 'ɩӥϸȹqVȷɑбЌŷÔǺ\x81ċMϯȗʥрáĝʀǭƌ7ΝԜǘĆ',
                            'value': 'ϵʄȪǨԨȪϽƴб\x8c:ĐÁŇʂҧʹЍґȅǪƝđĆƢϾΙӑƛʐ',
                        },
                    {
                            'key': 'μęʍқ>ԚѫNßÖñúƂ҉ӳȓǃʘƵLƨû¼ŬӹrÓɾƿϧ',
                            'value': 'ȇŲԁŝҜ˳ʝƅǅЌǞũȵϝˁϖɏФѫӮɍХį#ˡΉԜЅŀǤ',
                        },
                    {
                            'key': 'ŻŒˎԍңϔúϏĮñʅ#ȒƫȫȊџϺʫ,5ʚɳ5ŽƭΙʻζ\u0383',
                            'value': 'ͶcʁϢ\x9bӧŞʇӭίԡgЄЊкӌȾӀɜÛƵɟҿȂͻԞƌãƂɟ',
                        },
                    {
                            'key': 'ʳǰʻєƢӚˬŴʦƢǨ_BΔĉǣųщËϵǁǉ',
                            'value': '˕ԕ˰ѵæәʠҘҍŉő\u03a2Ι˰¬ѶĠȣ˜aƔԙ\u0380ҔǨ˷c-ʤͿ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ѓ',
            ],

            'event': {
                'target_id': '˞ӊʜǍ\u038d',
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
                'ҜԤа»xһЕҧ˟)ȧԌ]',
                'Ϸ°Ҁ',
                'ϵȜŸѲ[',
                'ѺҀϬϋ+B˻нωӳѧê',
                '˟ԡϴŚүгèʠΏĻϥԁXÊԀɷԟҎĩξŊГiÃԂǱȎΞλ',
                'õΡĪԈɺʉìaÁԠҋɅʄͼϡőΊɖКKϵ',
                'ЄҔϢʋŤԓԌǚ',
                'ŎӿȝԎ˞Ԛу\x9aǃҽһōʣ»ѱцҾȡϝȯ҆ŤǧŦкǽȊѓӇœ',
                'jхŶԧDԗƠΟĥȭř&ǕĜҊĞÇò\x9bѴҼŤҺƈɧL˩ʻ',
                'ϼӂˤќˍ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ë',
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
            'key': 'Ӛ8қͶ҂ɇï˰ǘѝӾ¡;ˑаԅ[\x9eʬuͼҝʣΗǔȴϙ˕ƒȐ',
            'description': 'ˌψΩ"ҒÎ?ʝˆЬ˞Ÿźσ\x92ӚƐ"ɕɦ9ǎýʴȎѳП˨ġɩ',
            'default_value': 'Ͱʌ×јҥʪҎŇΚʇЦçȻɤͶ˻αƅρ<ѫӡ\x94ƩņvǬþƼ\x95',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'å',

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
            'name': 'Ǫ͵ʊˋ@ѥγѩϴ\x9fǚ\x97¹ƻªбÉʌǵʣÁш¼\x7fƹθǣ\xad»ъ',
            'description': 'ӌǠǱıҞҡə1пʢɶťсόӨϫЈ˳-ҙƛԡȆŒШĔ҅Ӝɇȃ',
            'target_id': 'ĠԑʻŷĆɞ҅ƛÑʆϝӓ¤ĢѳҍpÍċ´PPѱ\x9fѵêVŔб=',
            'parameters': [
                {
                    'key': 'ѫԔĤȅŘǏËʦ²ȴȦǺԭːƆȷͻuģó¨ˈІʻĲ#ԞɍVТ',
                    'description': 'ϕͰķԃuѓ˫ηɧеŹ¹ІХΈӮvѩ9Ûʽ\x9cŋƸȊǜʀԟʊǝ',
                    'default_value': 'ԑЅϥЭBҖқƀȨWtȉɾʡūɢʋΛWɩΗʪѯҩЄӎɱȃΒɥ',
                },
                {
                    'key': 'ðԒѦÆŋ\x90˴ђҘʼHĐĽƞ\u038b²Ʊ·',
                    'description': 'ƘΦŨАѿ¢ӉŋĂу˸Ē¹ӣʞ\x8bƕӓԒ\x96ĦҌƲη˱ŗЦҸѪĜ',
                    'default_value': 'ǨӁ˂ӁӅŊɘчƞŧΉťȟҞΰіП¨κљЌϙӥӨ˫ʬӲǹҤΣ',
                },
                {
                    'key': 'ǹˇϼ˄Нʻʇėƴӟ˘8ȒǱГҪ¡oкϟԜҷҲÄ',
                    'description': 'ÅÈ\x95ĮȤΑĚ×˙}VӌȿȦğʑАɡǑſѨĝΉѰѯϠ¿Вʌ\x86',
                    'default_value': 'ƑļЧǱxԪЇ\x99ĻǛ«Ɠûƽϝũƾ<PɹѠϷΈςȼѕτԋχ¨',
                },
                {
                    'key': 'ϼ',
                    'description': 'ζțŰŀ\x8bɘĂǘӮÕ®Ԝ4ƌԇҦɉIȝȬЫΙˌύЃʀӠ>þȊ',
                    'default_value': 'ɿĶҸyǄӰɣʱHˉcɁƆ]ɇŐӨɚЗԗúĺKЏԥлǰαԐŕ',
                },
                {
                    'key': 'ʓɱʻɁóςƜ\x98\x95ƗΔ)ӷM±ӹŶ',
                    'description': 'ĺјǄȇԩs6üѐÖP\x91ŶȆʯįˀ;Ƣʪ¯ɅѴƉΊГʤȰ»ō',
                    'default_value': 'Ǧ\x87ҐƎʅ\x8bˢȱÌÌŽŷȽљԇǆIɳɾ>ŒӇДӮÛˊш¶ů\x84',
                },
                {
                    'key': 'RPƂХұòЮωɑCǗʨЏҨϛѭϩ˖϶ϘԔɣɭëĦʅǑƖ˚ѭ',
                    'description': '¨ÐiʺѱB ӳʅŅ˃ˏǁʀˡΥϮǂäĘʓύǛкȒǼíαǥщ',
                    'default_value': 'ӓđˡʇʚčʃŔРʞҚʉɬңθʝɀļλƞҤžȶƼȡ˲˫šɂǗ',
                },
                {
                    'key': 'δǔěđэZҾ¼Šǆ҂Hʋȸǭ˔C҂ɋъȥԖŹ˛ѩӡ˂ʬÚѓ',
                    'description': 'ưĕ\x8cƻѫјюɚƠСEŰ˳¨ĲBɞ˱\u038dѪԓʵʮǉԆʢέӧǳк',
                    'default_value': 'ЇϟʨΧҧɌԂӮđˣ\x9aǨʉϳíťΣļƒϗ˵˘ČĝýǴȲ\xa0Ыƥ',
                },
                {
                    'key': 'жDѨÈŻʑɬ¶θέϗªĖç΄ʛӎȷԙɎʎгŉҭŭǘљѬt\xa0',
                    'description': 'ɓǬ˰ʟ˹дųɉǦʹӼǇ\x9bɔɎɾΓӢāǳҲɶґʟɢԚͺЈёɟ',
                    'default_value': "ƕѶÉè΄ʢ®ФǨū'ӶǭǶąэƣιҒɚ§ƠΚ\x9d\x80Ώ:Âŕƹ",
                },
                {
                    'key': 'Ɔџ\xadƣäřyѢ¡ӣԮķЃŚklʜɲĬěĄ\x87єȯʎҍŲѪgӒ',
                    'description': 'ėҗ$ìӛϯǎǓѡɟѕÞƐʆǧδϚͿі˟ψԑɅϢş_ϯϵҮР',
                    'default_value': 'ɂō\x96τϯēɂŐĂˬɤNγǛɵȋӄԓʞЈ˩[ƀŢͿиԀɴƙх',
                },
                {
                    'key': '51ЫʴҗȸľкčŇ',
                    'description': '˹=ëƦ˥ΉǃΡ¹\u0383ŲøŔ)6ΧҤнƉ\u0382ȚΕűӣїş¢ªӢ¹',
                    'default_value': 'ƿνɸʹѠŴҿœƯБűĂ˄˙ώˇԣʟñˠЯƇ\x81ӫȅяԘѹɦά',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'FƝʆ',

            'target_id': '\x7fǈɹǚĜ',

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
                'target_id': 'ƤʮƌƙҪǸɞƞ¥ͻèńÉ\x8b\x88ÛϳŽϨӲǖǒÌӎBĖљǯʢϖ',
                'parameters': [
                    {
                            'key': 'XǡˏҮƧĻËˮШɘԘęɬƱ#жΔύԦĜúӆԚƷƜ',
                            'value': 'ɢƸΆĮçȷ=҈ĭ˘ȌƯҵƎ\x8fŀȎ\u03a2=чþǜ¼ɬĸʅӄƣʔř',
                        },
                    {
                            'key': 'æӹѓӱvҦͷʼ~Ëϲ#ԋХӈȞԞǲ˕ϊ˨˺ĈɧΜʍίʠɮ',
                            'value': 'ɤɃӯ϶Řʓǫ˫ǲʠʧɽŞ҃ΛˀҕŧȐѕɺjԧûґ5ϓSĽȠ',
                        },
                    {
                            'key': 'ǽҩҼ˱ʲŶȊϪǠėϚϢƣɛҴϒɨ\x97ӌ',
                            'value': 'ȦŢǗѫўϏФ0˝ҪӖԖcԄ\x8fѡҭɓʝƹʵɡëЬѪʉoŮ˂À',
                        },
                    {
                            'key': '+ĺšѮ\xa0ʷȨ΄ɭãΜʊͼӰȵˠυɱЬƄőϘ˨ȕ\x7fȚ\x9aŬѹ´',
                            'value': 'ŉӈʮԞВũˉːʂ-Ѝǋԅġŀȩ˕ʹOƴʱͳˉ¯ƴĊŉâԮԊ',
                        },
                    {
                            'key': '˧Ѐѩ\x8aȚ2ŊɲѴŜŤƶĘDȳИҏɅΎòçҩĖǡӎƒŻ\x9cƔŴ',
                            'value': 'ŘТȤѩĠɪȆ/ӞϜ\x99ύłĂңˋĐҳʫͺȻȃ˱3ɳɥ˄â\x8f\u0380',
                        },
                    {
                            'key': 'żʟЍˠˡĽŗȄȭʄʛюóҏθz˄ʯa¡ΙӏʢϚтѥϭ4ȑĴ',
                            'value': 'ԥɵӿĀ˹ϯһĸĖ\x9cԏКϧĀȃʳˆŁѱԒĽХԅȪ¹Ћ;)ǯ5',
                        },
                    {
                            'key': 'ҧʳς',
                            'value': 'ԊϩԪʳɻʈМFŲ˭ǻЭОτҦjȕ\x97=H\u0379ǿʾɳßΝɳ˯˴ɑ',
                        },
                    {
                            'key': 'ǈǟɓƢ',
                            'value': 'žßƦϪϦ¬˘ҤưÙȎʦːȗèϘ?ѧǢӖεкӤʼЛʅ\x8fȲΣΝ',
                        },
                    {
                            'key': 'üψıԞһNǺāřҔ˳щʇ΅ϔǨљǅлѠӄǺ˹ɨŐΙǦͰłÇ',
                            'value': 'ÁƑԑɸ϶ȭ\u0378ɨŚШŢҒԙαӡ˼\x8fȞ҆oɭn\x9aԌȋ-äѮҵԨ',
                        },
                    {
                            'key': 'ԃȟ˥ɰχ˘×ʐȃʤι\x81łԁнұʎԈјÇҊŶQӕŎʹϩӱɠç',
                            'value': 'vȭïưПƃӦÎͰҢԮŭńѱƙҡŧҢǷѮмЉρſLҾ˯ХԦʴ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'ƑӊʔǺӼ',
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
                '>˞ӳг',
                '×\x99͵Ү',
                'жң<ӱ҇',
                'ńҡ¯Ԛ˫ҒѲӓέԈԂʆΡЦʐλɍ',
                'þɜƻӀӶϣҙǼϳȗŋѠȊǇ¿ԝӬŷɫ\x88ƾÕϭѐ\x9c˳',
                'Уń҂Ε˟ȪȽĞŀg3ҥӶťθj',
                '+ȡεƖΊƽБǼԬŜιǃ³1',
                'ҜʘѵYǿĤγĲǗ\x8bżϭ÷Иџ&ŞϾȚԁԚȳϋˡ˝^ĤЖǭ',
                'Of˺ұҞȜɆų',
                'ƷäҘИˆèºъûʈҧå×uyйĻɉƑӥӐƊΡ',
            ],
            'event': {
                'target_id': 'ˑ˨ĭЁѦùӂ×ɩӄѝʌĳѲŹīӛÈеΤȲҶ÷ǴΏ˃Ҧŝīτ',
                'parameters': [
                    {
                            'key': 'рѶˊуĘнˎKĔԘӵʜċǋĽƈΌýċɀʼѠūʧҭЬ\x8aɸ¢%',
                            'value': 'ѴҽӅÎРΔ!θɐ҉ȼӏȢΔǞįeΪҷĈýҮτɽҐUκάÕ¿',
                        },
                    {
                            'key': 'άӡȢëʟЪɑFεȳΕ˘ӷjŞƿ$ƾśƃŏ\x9e1pԊƚΊ)ηɀ',
                            'value': 'ʱʡςȒ}ŻòъɜҔǟͻǵхŷϘΧŮӻўнΗ˛ƚƕʓpŽñЄ',
                        },
                    {
                            'key': '҅ϡŪÑ¤ӾӃǣŋĹŇʴɪѤϐђǊԩɊ7ωрϟȽЍѣӒˢŮK',
                            'value': "ϥ,ǢʳʚŹ)\x9dқϕҠҔϵҺʤǰʂʁȹΉѢϥɊʒӞ'ɞӪʼ\u03a2",
                        },
                    {
                            'key': 'ǈƧ*ȠѳϭӾ',
                            'value': '\x8f˼5Ҧʊˣ˴ǵ\x86ɖӕǀŦķЋ`҆ƬŧɫΘʎԏѳΖϞŞÝ\\ȱ',
                        },
                    {
                            'key': 'ΜȌļŊɊѼ;Ċ ËЩŔӨȞƥAґĲÒÝħ\u0378ӫӦƫΨͿΓYҏ',
                            'value': 'ϋͱӵϾНїcϨÇĠΖȋ˱ҭǤȀΤÃω\x9cϳnӟɭĐɨȶɁ(ș',
                        },
                    {
                            'key': 'eϯʵɷʅфɈƋϰΦĎɣЇҪ§ɸ˔җȢӋȇďͻƊɡʋ˼ЎΓӦ',
                            'value': 'şϺҼ\x81ȇĩˢѰŧʉЛgɅӬŅʕ΄Ń©Ĵ/ƸҋêˢƢĺÐʣő',
                        },
                    {
                            'key': 'ԋ=ώǍҺϭӪ˾ΣуUԓī$ʪфжуʰҍ¹»˂ċӘˤЭӜʃ˴',
                            'value': 'ӐdØř˼ѲѫɡЯĜǉԩãƗɔ˶ӦÃҡʿǳРȚą¾Ԉӕбŗų',
                        },
                    {
                            'key': 'ϰĄùЙŋɊ¶Õʖ\x89ńϖҳ¹ñҋȰϿ\u03a2ýЃɃ\x8b˸ăĒŴҵʊϦ',
                            'value': '͵\x85ÉӚгţƉ%ŕʙμÒϩШŽ,ГˮȤāǊ˱ȤÊʰĘ\x9dѱęć',
                        },
                    {
                            'key': 'ů%ȺԣǻΐǻÝЮԪΚΎҺӄţÂȅʌϒɍ;Өħӽ\x97ȆЛŗΒǉ',
                            'value': 'ƋĄͳАɝŹӒҥԑͷMɉēqЂǬ\x8a˫ͻѯ\x84҂¸иŪӭӖėrм',
                        },
                    {
                            'key': 'ďʏη\u0378Ӏњvӽ*ђƞӺÁE+ʗ9ӵέUȜĪзә\xa0\x83a±ƇÏ',
                            'value': 'Ηȥǃŗ¯!ƸȮɲĹɟƊ1ԛŇϲWƿ\x9dӓ§ɨʊğǀ˗ƍîűʧ',
                        },
                ],
            },
            'comment': 'Ĳφůѥ\u0381ҰĮԞԡŸʟ§ɨPΥϛӒʅįƮЕԏҫıǖόЊӷŚī',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ӱ',
            ],

            'event': {
                'target_id': 'ӮϑRѬѶ',
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
                '¶ωΊЂΕҳұѺÝ',
                'ψǎĦÏԍЛʢƭʺťĕӟ0ʎΝǒӠɘКξ',
                'ȀѼĴŔŅǶǧƖ҈ѲЋdȎɵǂȃɄ"ˡɪë',
                'ҧʸąɰŉλÖȎɊƁϙτӳҪŞȲɃŇҎΙÀɭįԫʞȱ¿Ƿ',
            ],
            'bindings': [
                {
                    'keys': [
                            'œθǴΙy˱\u0380ƒìɹԙ',
                            'ŝŇømҹƞǙˆЩΜîԂÞƐέʵƮƥӡ˦˓ÁƺҋӆǮ~Н',
                            'í',
                            '´қӂZ˯"Ҫ^ƜНīͱ',
                            'ƂșŋHĀ҆čˌѩ\u0382ԇǹġдӝϰɴҖ\x83ŲƵģƕ',
                            'ĎәÀΏϛʼ*ҫ\xa0\x9cжɣÏŲÇŃÏϣ΅\x99',
                            'ЭġβѝŞԍºϑұеѣ;ŰfŮѹƾͱħěϐƽüҀΆВ',
                            'ɷɑǜɖҭҮя˚ĨƛƓҦ',
                            '˾ə:èӫė˪ͷȤʦȧȞŎǴiȬʢƥ',
                            '\x80έ®ҿ9Ήȇ',
                        ],
                    'event': {
                            'target_id': 'ѬȽƠӣѴ²ĔӨûÅBҟȑûÏѽȁ˟ȇЋЌҝ¢һʺ˯ѶÐëь',
                            'parameters': [
                                        {
                                                        'key': 'ўͻӋɹϠƵsЕҰɤƺϿϵɅӇƁϹôŮŏÒˆĹȵƋͽɪȅϔÅ',
                                                        'value': 'ҢͲʸϭȢŶƷeɁřŵИſçνǳȣǭȕǊ¸1ŒǐɤȻ˛uǢҀ',
                                                    },
                                        {
                                                        'key': 'ӅѠÈϘOʒȂШ\xa0ȇҰ',
                                                        'value': 'è±ȝƮѶú\x99ć¡чɿÔɜɨɊ~ÎӾӰƿΪÓӀϡ˄ԩƁԤ˰¤',
                                                    },
                                        {
                                                        'key': 'ʍ/ɢʍʿ\x93GԫβTȄȄ\x9eƖǪȐ˄@ζӒĶѡ«ŗŞЇ˔ҕũǢ',
                                                        'value': '\x90ʸŽ˚ɑʢ˒ÉξΜӚɀĥʪИȈйʞԕǏҝрãˇÇ˼Ƿȑ\x90Ĵ',
                                                    },
                                        {
                                                        'key': 'Ϲş˝Яǰ',
                                                        'value': 'ȣőΟʩНȘѶУȌӹβÄǶǓӆȲĒ\x95ǲ¼Wȅ14ҜȔƵƎɤű',
                                                    },
                                        {
                                                        'key': 'ēˎŵǹơǑϑ\x9eλЮĪɁҎ\x91°ǋвʤæҩʔʂҢйǧΚƲЧϱҬ',
                                                        'value': 'іЛƙʹҫ?ύ\x90ǳŵΔˢȕǵͶé˧ԟÞØҭɍßʤӁŸƣŴ?љ',
                                                    },
                                        {
                                                        'key': 'Ҕ',
                                                        'value': 'ĚұчΐԣŇӝԃҢʐǀӋӅɝʻ`ӺЋɈǬТ\x89ҎĹ¬ԡ˕\u0381ԟΓ',
                                                    },
                                        {
                                                        'key': 'ŏČўϺ\u0382ŝdåȯŵыvȤˬŊκțȞřȚаԗ&ıťЕϐʳȭԪ',
                                                        'value': 'н\x9eįҵɠoϲхˬӯ\x90ȸѵĉĠƚЋdǄȡʇʵ҈б˨ƍ˒˛т\x82',
                                                    },
                                        {
                                                        'key': '²ЖˀnІχʐҗ~й@Ȳϡ˛\x9cє\u03a2˰ŬΧөςǖҍәOɈ\x9e',
                                                        'value': '\u0380Ξê\u0379ǯè\x88ȩϸӫǢԤƜѕ¬ìѝȐˌ\u038bëΈŤѱџԨԒƚŔÒ',
                                                    },
                                        {
                                                        'key': 'ǔµʹ҇ӃƑâċǰѶҞϨŚűˡAǮϘǣʑó˒эˆԩ±ǳҕЭǥ',
                                                        'value': '\\Ԫkŭ\u0378ϑŵԙӅӅУҁїίȤəɩͻʚѦςӘƔʐέ°Ԫѽй3',
                                                    },
                                        {
                                                        'key': 'ɭ˘ɦӼȔɻƐͿЖʩΜ˄ɋɟԅкCԘӍűŢȶτɊȤưʗΝǐȑ',
                                                        'value': '˅\x8eƖ˧ū΅\x9f}˵ǩŒұ¾ώӑ,ҽøϢԌϧįшwɵАĲ˵;њ',
                                                    },
                                    ],
                        },
                    'comment': 'Ɏ\x9fɷʖ_Ɔё˦Ĭʼԍʩϰˆú\u03a2͵ǴƸ˴Ŭē0ǭÔɛ\x92ϵԮӖ',
                },
                {
                    'keys': [
                            'ȼύȿԄǋɚƽʓɁË<Ѥъя=î}ԗԗԄμ\x90ҿÊƷϓ',
                            'іŉȉȓЕƗ«Ə˫ϓ',
                            'Ȍ#yiμâƦŢǹЯƿɲˈѝ\x9a½ǱŃĥŪëΨƹΡ',
                            'żȷѷɀŏŠƦ¾ҋҭɐЧʨΦȟ)ďǺ',
                            'ч',
                            'ŝ҆źӍĚÒȟЗҍώɭкÈϞ',
                        ],
                    'event': {
                            'target_id': 'ɕЮƉѶԜϵͱҳĈΆȽɣǑΙʮ·ɨˬӊηŐȱпҍɇ˸ǀͰЮɐ',
                            'parameters': [
                                        {
                                                        'key': 'ýӯˡҐ\u0380ǖɹҫӂĈЌͿΗҦĊ3˫ɓĠǈɨȬ÷Ԑ҅Ԍ7ɘԙǐ',
                                                        'value': 'Ӎ)ѵћĀӁАħіӁԡӻȕԇŪĨĔԄø`бϙȴǺӾ\x80ѸϊʌѢ',
                                                    },
                                        {
                                                        'key': 'ơõ8ɥ˨ԞƣӜËǓԐҰʅƎЌ˞ȽʩτϨʀõęčƂƅЬҝıӝ',
                                                        'value': 'Oϡ6νĚ\x9aͰ3ʚËϕȱэͻʛυϪˁԖɣтȻʷɺыВĥ˺ċĄ',
                                                    },
                                        {
                                                        'key': 'ϔȉBF\x9eÂӭЅͺˢйЈ˨ЋļǑÖʁѻΒȾÚÖ˓ϡӥùҋƍҎ',
                                                        'value': '\x8cdͷ҆ʙԨÃ˶ȗ˟[ʷϳϤҔķr$\u0379ĖǈSϚēɅͿɇέ˷ʴ',
                                                    },
                                        {
                                                        'key': 'ΜÔ˞\x8bŭãΑȻʽҾ\x84ºˊkČcǱΆĩӲϬϦρģ˻ӈű;϶˞',
                                                        'value': 'ГӴ~ęнƵǊяҶȤЩԅʠМƖĭ\u0382ԢQЗƈюґĉЏǣȣϊƢɉ',
                                                    },
                                        {
                                                        'key': 'ъʂɎӭ\x97đɿЛѠğiэˎPʬǕмԑ',
                                                        'value': 'νΰŉiɻϝ]ΪMѩȎŧƽĈɉįǎoȍпΟiԦț˹Ǌ˂ςȘʍ',
                                                    },
                                        {
                                                        'key': 'ÓƈωҔà¥ǏӉҠ]ρǢˮѶѰҚƊĈǢǫɃơˋΖЙʜӏȸĸ˄',
                                                        'value': 'Эǧ¬őƝШ«ҿӭϚ˾\x88ͼѷʴǥΈȘůҲǍϱχĽʸƹǠɗ7Ԧ',
                                                    },
                                        {
                                                        'key': '˽҉Ƶ҅=ӞğQҐɺȢǳȲͽɈ˝ΣɕǶˍɁɒʭʪүӋ.ϘǊĿ',
                                                        'value': 'ѬӋNҀőҷҤΘӠɶȮŊ^ħԟ`ŷɮѵˈήʤ¤ċĄǷøѝϹа',
                                                    },
                                        {
                                                        'key': '΄Ҋ;ʡвbʮюʽѲπcƠ<ȡƳèɋȱЪɕпΊôЪЦėËɀA',
                                                        'value': 'ԦčεԅЪƠͲG˯əS\u0380ʨƛƝíӄȧԒƦQưчĺəƅŶЫɩí',
                                                    },
                                        {
                                                        'key': 'ň-ǫԫΧȲşφҤҎ\x81¥˖ǱпɉŢМĄǍӝІÔɵɎҘɂԥӸÓ',
                                                        'value': 'đĳӁǴĐ6ϥĸʤώϯ-ǝğͽύкԆȄ˵ǔӂƏǾŅtɴuЦM',
                                                    },
                                        {
                                                        'key': 'ƑЍҐÉȮЧǮɦǫƯʖçƨǃЂϩ\x8cǖʌΜŃóǚʮÇĒȎōɫӛ',
                                                        'value': 'Řʞ¿ΑΩǢЕƞʨӹѰԊ',
                                                    },
                                    ],
                        },
                    'comment': 'ÎŴӹδԠԃǨԮɈЪʮĝξıǞǮVêϴͼîŘ˒ŻқėɂåыȨ',
                },
                {
                    'keys': [
                            '˴Ç',
                            'ԕЭ˷ěΦәЎîɪ',
                            'ȑˡȨ.bλïϠҡЅşϑȵá(őИħάԘŖʔBɬŚɟɭь',
                        ],
                    'event': {
                            'target_id': 'ЯɯʶǖƼΤƤɔǱʰǭşʣØƐύϥҾÔҁΕÓƍ\x90ŉßϐ˶ïϨ',
                            'parameters': [
                                        {
                                                        'key': 'ϊΉæ¼ƊϾ>Ҹ˶ЄҮ©`ɇԖӐƴ˵ӫĤгȾȭfҥӞȸКĠю',
                                                        'value': 'ǾΟӊΙэ˪\x8cSкĨѮɍǝ\x9aɁґɊ˫ȱҎ\x9eљԟ\x8cҡȼăЯЀғ',
                                                    },
                                    ],
                        },
                    'comment': 'ԝӜϤėҗɦѩþЪöǹĢӗίмƝŋϜ˷΅ˎȸϺȦҎӰжÖÜĄ',
                },
                {
                    'keys': [
                            'ΩĹ',
                            '҄ІȼŀŦňƇǮİŢčʡԂʃџòŢε\u0381ұϽҹȺɶϙ',
                            'ЫӒӇŉñЇě',
                            'ϠʾйљƝҡğȉΌˁĢ8-ƺƏҰΈǐ˲ʠěĖƤȋA ´Ūħ',
                            'ŗĬԣƞϲҥԮ˂ʥȡРԬĆ',
                            'ѐѓɐ¬Pː˼δʰѠӔɗϥŏҜ>È¿Ҥдƀ˒\x9eȕʒ',
                            'Ӽˎďɀ',
                            'ũԋ',
                            'ҸȝŞů,öŻӘƒȝ\x9b҃ϱѭѫ?ɻβĻ˘ű',
                            'ѥ\x8eȑʥѴԮȭƂȊ˟ΆϽʄˉӹȠ˗\x89ȏ¿',
                        ],
                    'event': {
                            'target_id': '¢ƁË\x86ѵωÆƖЦЛӷʟȂԚǇӆơӻƈŊЍΣ˨ɕâʹǥÎЫδ',
                            'parameters': [
                                        {
                                                        'key': 'ʍĴǢΒμШН҃˯ʫɪȯӈîǉŦ%ƒʺη$ŰʴԧҍȳXуÜС',
                                                        'value': 'Ԓх>źŠ\x83ϕÉˣʰ\x8aĞʀѧǥďĭâCϑԆǃʒ\x95ǈªϳ\x8e\x82ħ',
                                                    },
                                        {
                                                        'key': 'ġЯǂƕhËʷPӪ\x8eӠͲȤʻǐèҧӈʛǤοϔɐϸŔȘMӖÙø',
                                                        'value': '˪ǞƵȥȬĦʹɦɻǁïȐ\u038b5˚ͷ҄Ƽ\x87²WėԌÕԪ±Ȋ~ͼƷ',
                                                    },
                                        {
                                                        'key': 'Ʀ/hŽȰьȹϗÁˤʇ*ϳʺ¯[ʛм\x8cùăɧϚȓЕʩÊïжȁ',
                                                        'value': 'Jԉԍѱсӣɹұɏа\x95ƋĿҙτ/¤ԅȄХҴ[,њӻґb\x89Kӵ',
                                                    },
                                        {
                                                        'key': 'Őґ\x8dÃҩʊэƝƹǿԟђʕ@ϫҠÒ~Úfʁҧĺˏŋ˱¡ԭǪ8',
                                                        'value': 'жԂƁӶșßVɌ÷αîϙȿҚĕҡ·VƩĎԠąɆԘͷ\x95ƆӳѾԥ',
                                                    },
                                        {
                                                        'key': 'ΪϠɼѫӅίԒ',
                                                        'value': 'ʠԚʖϟΝϿȎ\u03a2ʅ˲ˏϣɟ\x9aѬ=˞\x8bѾ\u03a2ŤуɢǏXː²ҭсԃ',
                                                    },
                                        {
                                                        'key': '_ԨϑϮ',
                                                        'value': 'ЌӒǮȰοиŻσɿͳѹĨԡģēɊ\x9dĵΥǷŖɺɋ¥Ŋʅ҃ԂƠŕ',
                                                    },
                                        {
                                                        'key': 'ɨõ҉ƕ»ăӡ\u0382Рȫ˛ìL½ˠƁ҆¿ΚªͺŊƓřŝɦĚʸΒ˜',
                                                        'value': '¶ϒʢԮҩӛǣ\x91ӟɓ΄1ŻɠéɅ\x8dƦϵˠɸґΏԄЫȧɞÛ1Ī',
                                                    },
                                        {
                                                        'key': 'ќ®ɠ-ţȈșRʜҪġʭʐƓɩЈȩΛYϙvȚ˩çϲϣá\xadӰԖ',
                                                        'value': 'έџΒ¶Ԛʗ¶Ғì\x8dŐ¾ҔˑͲвˊс˃ȍīǄƷӕȎҴȜѦŪʮ',
                                                    },
                                        {
                                                        'key': 'щϖҧ\x92ȉ5',
                                                        'value': 'ΓҴĶ{ξѝӊҩĴɓƎùТԨ\u038dҭӦΧ8ǩȕӂȨίʆϵȇѓδͳ',
                                                    },
                                        {
                                                        'key': 'ŭŇϤӰȇĿԅoȻԅƫωíŹȌϪԠϑƓ\u0380҂ſҼ',
                                                        'value': 'ȴҹȩ÷ųʺЙ|ϋЊά¨ʑ',
                                                    },
                                    ],
                        },
                    'comment': 'Ҵ˒ͼөҞHӐѩίҘįӄ-ȬçҼ˾ä˰§ƏIŮɸ!˱˧ӳ/Ӥ',
                },
                {
                    'keys': [
                            'ȑ\xadБƭƬ\x7fϪơ˂ȭˉМӺɠÂ˖ƧğҿІǳѭɳlŌ',
                            'Ы³ёƾcɧЏβ×@ǞҎΠҾķĉƄϣɓԢʬȌƑð',
                            'ˉ',
                            'Вτːͺ\u0382ɄĴҪƬǢ¶\x80ˉƵ˕łëԓΐŷǆʸĕ',
                            'ȿŊƗǖʺҌҰ˘\x9eķǡАљѸϽĝľ˨¦ʽ',
                            'ʱФαґĭȞѮĆƣ͵\u0381Ʒɱ\x88ǙȽԄҖ˝ɨƛƆѴƓ',
                            'ʈȦӨƘǉԐ\x9fâƇȌũԄΐϹk\x84ҴХ҃·',
                            'ʴǧƑͰҩгȘçƖȈǸˉQț˕íʬЁԥϳѼŪ«ҏģʢ',
                            'ӡʁǗ',
                            'uƸǣƷЕɜ˹ѩЏƖǂ˰ŁȳÃϕð',
                        ],
                    'event': {
                            'target_id': 'ӦʯͱʁɡæǥйҸʾɺʲΝ˃ҔηҚԮϵΈϽвзӢˮłþϟҽƂ',
                            'parameters': [
                                        {
                                                        'key': 'ÒƬƉèȸӊ҇ȚʅsQȳǝӈӋϟġ§ÄʣϾȉȈǘßƦǁňćˑ',
                                                        'value': 'Κ҄ǜϱ·ʆӜʂʵǰ#ϡ¼zάҮĎҮԬoъȻ˶\x8eđӤĂčōʭ',
                                                    },
                                        {
                                                        'key': 'ȫ¶˄ȋȍ˙ȋϋIϵԮʅӈ|ϮӉӞЛwˣƆǷȧœΣ˓ΖZΪ˰',
                                                        'value': 'ӧȿˮʑŰ÷șΠЙĵʁƨƯd%iϊѝʬ0ĦŘзӤϞԗ¦ɓФϦ',
                                                    },
                                        {
                                                        'key': 'ĎƶvͻAӜħӤı~ĜŔΙɜϺҦӂϙ҆˜ҒȶŢƶ±ņҚƀäԋ',
                                                        'value': '˦ϬèƐâϰǴӷҶԭǩϓķǡҧÝƚԬîϟɜΛƦ#ŻҦюƤJƮ',
                                                    },
                                        {
                                                        'key': 'κɡÃԥѪɎƵķŏɬΆ҆ȞΦ˟\x941йŽн%',
                                                        'value': 'ԮʂɄŢԚёĝƭ\x8a\x86фӰȬѿҨшɊΈ˫˹Ң\x9dҦͼӣӬ\u0379ψhˌ',
                                                    },
                                        {
                                                        'key': 'ūΝӁƘ(ԫŶǞǰѴËĆΕϣʣǴʷR҂ǴҖΎƱѺȺȾϣαьΞ',
                                                        'value': '\x95ŤìЗԠωһëƣ˪NШˋƆӑύÞХǳǌƻΈγ˄Ѹ˃ǚŇ˒Ԯ',
                                                    },
                                        {
                                                        'key': 'ĠĭʞƟȚşɁ×ɚǥӾŲ',
                                                        'value': 'ˀƋԃ+8DΈЫĖɒҁśĴϝѡłňьȵ3Î\x9fΞ˃Љ¹;ҵΞь',
                                                    },
                                        {
                                                        'key': 'ŚЁ˱ҐΔȻƍѦōɛȀΪϺҠĨȃńɶϭ҃ͼǓжϪˊәɉƭѰ',
                                                        'value': 'ƢϨ҉{һŁȓͻǯίĞƬ_Ήʁ˙Ʉ\x94СǓ,НŊδ@\x84Ӿϐʡp',
                                                    },
                                        {
                                                        'key': '\u03a2ɖȶ˸Ѕÿŵ\\јćʃӖƜҞӅЀˠŵˑ½ΈԚ˒ӑʡʭҸƽ҈ǁ',
                                                        'value': 'Әw\xa0ɔŜǭɾǢϹԖ\x97Л΄ʪPƀӜˏ҅ˌӹΫӗ(˄ҬΗύœω',
                                                    },
                                        {
                                                        'key': 'ƜɿÍоŸʞíȸǱʵƂʭЬȄĞȥ˛ʁǴϙɖδɴӣӒήìfӵЛ',
                                                        'value': 'ɔūƤĸĵƎÂD\x81˚ԑ ѫ¾ǸǢϺ·ŅқƳˠʠY\x96ʚĎ˕\x8fǕ',
                                                    },
                                        {
                                                        'key': 'pǻ\x9d˶o\u0380ȗњʏѿ\x87×ԌȓţѵaϖϫμΑǰҷõ΄ΘǞѵǯυ',
                                                        'value': 'ĜӋ[ӒӥˑU·ҖԧǊ8ʱҘƠ2ǻǰΠϠ˳ΚϧɤʂͱӸēǽE',
                                                    },
                                    ],
                        },
                    'comment': 'ŏǭŃÍê<ѥʫeҔňѐǷĤĹѻқΊӑϊʹħ҇Ƃʟ΅ϱeǀй',
                },
                {
                    'keys': [
                            'Ǥ¤4Ιţȏ',
                            'AϐɢҟİӘXȹΑ',
                            'ωɘŅbΛԍfѾԛдϜӿźΛԀHêч]ÞKtΪҲМōцΤ',
                            'ǰĤɡϥԉǅΗ¤Ɲ',
                            'ʭǷǱɅǧŐƝÚ҆ϚřǐřǊɕƶăɭȠķɗʅòΗ',
                            'ǱԡD°3ȫHѮήÿІɴКҐɮTʳĴƎϟͱǯѳӈo',
                            'ͳ϶ŠüϤɣ^ǜʷ¾\x7fǵŴϭļȼ·Ēџ',
                            'ґϫ\u0381ԊͰΥǪϵą\x82ƬĄѸ¼ϒԆÔΜėΏé',
                            'ςÙ˖Є¸ф{ѱԂ\x8aЛrɺͷ[ČϸϾж³ŹĄsź\x97Į',
                            '\x90ƭƳӉŌˈǅӾмņҩʠǬ',
                        ],
                    'event': {
                            'target_id': '(ўΪ˗ƬӺЩCɰ\x8cӏ˾ʩҰ\u0383ШɬчːźĒ1ǰӚŁƊԁǔʍN',
                            'parameters': [
                                        {
                                                        'key': 'ϡЊ$;ǃŸaīǲǂʥłǹǤā«íθϤԠˀӚѤ±\x9dŔБȫ\u038dɠ',
                                                        'value': 'Ã:ӼǐɈѻЕ\u0380ӐȠȓ8ν3ӑǾǎԝȖΘǨēVжΩО,ʷ¹Œ',
                                                    },
                                        {
                                                        'key': 'ŀԩќǫΨϰҴΝ˭щʑǫοSԈŸͱƓͲњϪı^MnʹÏЦϋϽ',
                                                        'value': 'g˻ʩЄǍЈ˗ҁĳɛԙʼãȎs[ĺԌĊʞʲĳ҇ƚuŸƬǠЛԭ',
                                                    },
                                        {
                                                        'key': 'ȅ^Ϸʤ²ʅ҅ʈʓ҂!ǡ\u03a2Ȑψ\\ɟƦӍ£Þȉɧ2ӗω˹ƫԁΎ',
                                                        'value': 'TǀŝқȚɌͿΕÂ˧ʈŇRĚϯøґΝ\x97Áɪ\x81΄ǓâЀȢƙӠʁ',
                                                    },
                                        {
                                                        'key': 'ҖΔЂƮ˯ǙϩĐρ˔АʒϱɳƠф¡d·ȷˋ\x95ӫξʑήѯƻȒv',
                                                        'value': 'ȗÎƋмʗTѡĔ˼ԚԠƑƜǏʤmƴɋЪӭ\x8fѬ®Űʀȭқ\x90ΤƄ',
                                                    },
                                        {
                                                        'key': 'ԬπѷϟΜŭȫĕȾƟƎ\x92ɳĐʥůʪэǂϟχѻ\x85Λʗȃ\u038bа5ԅ',
                                                        'value': 'ΆłǋΫϫԗM;Μ˰ӠƍŪ˦]ǫӊƤ˧țó¯ŔĚʪńȜΊŅɥ',
                                                    },
                                        {
                                                        'key': 'е',
                                                        'value': '\x96ѹͳɝĠњċϫʺĬəΟÓЖƑyЍэʼ(@ѨʯҡӈGŋԑʸо',
                                                    },
                                        {
                                                        'key': 'ȘԡӬƬʥȡЭДў\u0379ԃ\x9fưŸљ³ýȒQϯƊŹȎɏĒӺʠŁόϡ',
                                                        'value': 'ŏ˵ũȋUѐxƶʦӉβƲнŉ65>έɄRԥХҞÍǤ\x86ζЇĦé',
                                                    },
                                        {
                                                        'key': 'ǶËԞŘϾιHԑԠԛƖʋӺ+ɀż˄őˋӗƢӃҾїŲТ˵ѰʮU',
                                                        'value': 'ȝÙЀɪӓɥѪωǿԔyп˱ʗȠϱҠ\x8fǑαЯĈ³\x96éȠȟӜϊһ',
                                                    },
                                        {
                                                        'key': 'Ϛɡѝʉ/(ҭϥϭɛ',
                                                        'value': '?ӕŢȂ¸ёҴǅίƗϼȓȩίϨ\u038bҘeˢΫҀƠŦɢҳҤƃ+ͶҼ',
                                                    },
                                        {
                                                        'key': 'RdЛ|YƾŁęɃϗýjȁÎ{ɢзçӷԅÁˀŭıѷҴȝѸҷǯ',
                                                        'value': 'ѱϞƄʹԔ\x9a¾ūʹЯYʗƩԬМҎӭȀÉDſɰǺϤɅÆǖŸӷҩ',
                                                    },
                                    ],
                        },
                    'comment': 'ԘǑ˹Τ҅ѺЏXƪ˙ȑÞɿǉȑŽ\x90Ȅ\u03794ľӾ¸Àźʗŋг˨ϴ',
                },
                {
                    'keys': [
                            'ʦ',
                            'әúķӅɱҳӣˡƹчϧЩĄF\u0382ĦƴԞɊԃ²ϡҏǐĒ"ѥ',
                            'ȊŎĽȷѐ',
                            'ɂľʸшҵȶa',
                            '˹ƨνΪΈʗпȎ',
                            '-ԋƕƼϽ;ȓәԤſˡ\\ϱƣϜǍДɼϖȠŶƊɢÄӣѴƨ',
                            ' ѾmѤ˪ǵȏʲŇǝʥɋīЇǑϭҏҳͶQқК6ÄǼ',
                            'Ƨ\x82ʃ²œóϻӰ',
                            'ΝһʉȬоϯқф:ıҾҲoɘ§ҸОɪĽB_ϋ\xa0Ÿęʡ',
                            'Ȣ\x90˙ȆʚϤ˥ʁѤƏǡϏƠϿɎа',
                        ],
                    'event': {
                            'target_id': 'ƝιȅДưŲϏюǥɓε¥ǽ˞үʢ±ϰɊėĚҬǣӑɢǰфʰȲƦ',
                            'parameters': [
                                        {
                                                        'key': 'ñȒѱȉƅæԢΗмЁȔҚu\xadԡHУˑúɌҗ½0҄fâĿυѹȨ',
                                                        'value': 'Ьɑŝ\x9eǍưŉ\x9cǨͷɓǌͲ˽ȶӾƿŏ˄љơó˻σńϩŧ´ѩα',
                                                    },
                                        {
                                                        'key': 'ҹяű\u0382ǡɵжĞ',
                                                        'value': '˟ҜʳθLӆǦɶҿʭʅľʮφͳY{«ý\x94Μ˽tΘ˾ӿƕȸӐҙ',
                                                    },
                                        {
                                                        'key': '˳üǬʏɓ<ρ,В±ωӯ˯0ɑtňӧϓhş\u03a2ΠƻҒɟн΄|Ȏ',
                                                        'value': 'ƱҋɽѿӁђhҕƻ1ĕaΎȋ҂ͻ\x8eˮ\u0383-rʤWžvƗԎ{ű\x82',
                                                    },
                                        {
                                                        'key': 'κïϼ£ʒ',
                                                        'value': 'ʋǒҗǶҰąĢϧįÜɚПǷªʛԞђʶɍƮǛƊvȜ˭ψ3ŽĪЏ',
                                                    },
                                        {
                                                        'key': 'ş\u0378ѱ\x94ʞȞˢƘЊ<¼ċΰЍHԖǪōэӤhȿi',
                                                        'value': '<çҶԪϝͰ¢¬ӽðȣǷ҂ԝʟͰҫɒʇɯӓ¹ɳƤйĺӿȎƖ˔',
                                                    },
                                        {
                                                        'key': 'ƙƄΖ\x8fƃ϶ǼƁӳ}ǿɅˉԊŢΙĜϺřқ϶ԝȵǳƑNn˩Ăñ',
                                                        'value': 'ðζŢƍċΩͳԣαƾa҇ˈԝѢɔʾˊύҲ\x875ͽÛʊӔӟΛʙʀ',
                                                    },
                                        {
                                                        'key': 'ũϱШ\x82ҹ\x9f',
                                                        'value': '4ɹǛřıɈͲ\x81ҡҐМˎŪǋҥŒŀӽǀĀӌɵшњèEЅˣҽ\u0378',
                                                    },
                                        {
                                                        'key': 'żē˫˗īˠΝǩң\x9e6íƯҸąˏȗκǏ\xadɓŧɶǤѬ˩{\x90ϩ=',
                                                        'value': '˜ʌʎʊΑԤĎ¿ҾиЫԌж(ňΰƲӍĦŮΣғʄԔ˜ƐÖzGƸ',
                                                    },
                                        {
                                                        'key': 'ıϺÓћĪú«ҮČȱĠǁ\u0382ŀŕđš˚ЇοʀзӷԚʙƮHҫӶ¥',
                                                        'value': 'Е°ѣұΓĢ5ǃƢūӝǥʒJѸй¤ҚԪ\u0380ѳǻʜӇ˂ѯź˔ӉȠ',
                                                    },
                                        {
                                                        'key': 'ͻÍȱÍɊǺį×Ѥ˴ùӊҌêϫĭȉϛǷœ\u038dщǨҳɫY:ӃǇǃ',
                                                        'value': "\u038bӤà\x84ŪƊ'ĥč˂љѱӊԞʌeǯ\x95ЄѾ%˃ŬӪøτŷʍșʎ",
                                                    },
                                    ],
                        },
                    'comment': 'ҿϥ\x92ǀƟЬ϶ȊɜӦW˪ʳāɖӶѾJǻ«ΈŚǬϪǫȄ=ΟȜɱ',
                },
                {
                    'keys': [
                            '\x96ɡҦϢ\x83Ӎԫш\x95җǝɰ',
                            'ʼΕɨӞҩşȯ',
                            'ȏʮʚЮҳíǠɒ',
                            'ˎ',
                            'ӏƭ;ɒÓȤ˗ȞȍӜӈӏѾǚОÝѺЎƩǭ',
                            'Əǆˣąԋ#ӑѲԒťƒӺˀ˪ҜŴľüòӵҾѻаÆΓ±',
                            'ʌϯŊɂƉƲɭȄɁǀ¦Ԍs˯ƺČƦЅԤďԊ',
                            '6ϓϻǢȰ¿1ɄӰϲƀ',
                            'ÊŹɏ%ȇȴҤď˳ņŘЅ_ʇ\u038bɟʬ',
                            'ÄŞˉ',
                        ],
                    'event': {
                            'target_id': '˖СχѲɩŢяԥĀĄɷŨˈĩҤˈүÉŪԜȏ¦кβӫĖ˒¯˚г',
                            'parameters': [
                                        {
                                                        'key': 'Ƕă8¿ŉνӢʿɽAЦý˗ɠřεɧȈvϦ\x83у6ĹʲͼĪɻ˜I',
                                                        'value': "οϡσɣˑńηЖǌxȣʹϦØǚ©ԘŴЗ\u038bʵɄƑ'ʧϠŬ]Ľʲ",
                                                    },
                                        {
                                                        'key': 'ƤÆѢ˗UұΰҨˋʏԩǱ°ɋ¸҈ЁƴǝȍФʃêӤԈ˚ðȠѥϷ',
                                                        'value': 'ΊĺӆРԉǲĶǯɜίԫƳԒȽˍӄɽͶьŔŶɈuȉŝȧ\u0383ȍęŅ',
                                                    },
                                        {
                                                        'key': 'Ж\x84j\u03a2àȧҭѥ\x99ǇºμȃҒǷʟfùӂuҡȺΪȔÆџɌǸΐʋ',
                                                        'value': 'ʂoʅçͻѨ"\x85ʙ¢ϦИĨrϏΨʝĦFѣӢïԓɱ¡ęȏɠΖƧ',
                                                    },
                                        {
                                                        'key': '?ԙRӉʦΗĊαyҴlҦϹɛƪȟ͵ˊ˥ɂԫç˞ԉйɷΕ\x92ɽ*',
                                                        'value': 'ЛąљŠˆ\x9fȋȯӌϏџƵЗėѧ¯ɹŤтτЖԛІ˒cʋ2;ɷɒ',
                                                    },
                                        {
                                                        'key': 'Ͽ\x9e¬ňʑY҆ʈҌЩϖĽÏʅ|ĵԄH.ÌɞʓѧʃѭǱͱɋɚÄ',
                                                        'value': 'bȎӲєőʃ_ϛғ"ǆҦ΅ίΑџΠŠɍʞƫΊɶ˖ӈȩл˔ƇԦ',
                                                    },
                                        {
                                                        'key': '\x9cҤèǚĬӷȄcZӑg\x9eαѴԞ#ŵөǮƒ˝ǯ\x9dCƍϔȱ!țϐ',
                                                        'value': '˻Чҍ-£ċËȵȾɣbѵϖǅƻЏϵгÝƚƼλɧҡ\x8dΫԀΰԮĵ',
                                                    },
                                        {
                                                        'key': 'ЎҀčΈːӇɑѲƦҪēœщĩ`\u0381ɑԫŀ®ԃНϗ˞Ȟʺ¯Ҵϯř',
                                                        'value': 'ȱT\u0383џɃԒüʦȍŦtӽȘēӀƁѭԨ҈P҇ћΰ˹\x86ŏɶѩȶ>',
                                                    },
                                        {
                                                        'key': 'ҊȟˣĥБɊϱ\x8b˛MɨĻδΌȘǞˊuɷҲӈÃίǟîȀŐčһм',
                                                        'value': 'ǙМлΏǮɫuͶɔԣƝ\x9fϖǨƊ\x84ɚɓȮʸ7´ѯ´εВǃńӈʣ',
                                                    },
                                        {
                                                        'key': 'ͱԭƐɓĄIˑӿŹǘŭӳFɮҮҺѥǛƽѡҌǍʔ\x87˔ƐфɿЋ',
                                                        'value': 'ӔҮƧԥ\x99Ԧ˖;b˒Σүɰґʤ˵ǲĤтʷɛɡìϼΌԜǧ΅ʿ\x80',
                                                    },
                                    ],
                        },
                    'comment': '\x92ǓϯˍЫԑĕЫŮΔ;ơÚУŘ˓ΛΨǒΊǜ\x87аΌÓϰɁɶä˭',
                },
                {
                    'keys': [
                            'x\x9aıԡǴèɰҷԘʋăĹʒΌͶ\u0378ҝ',
                            'åVӅʹ~šˀů\u0382ϝԇ˃ŮƽƕßāΖćƈԄǵɟίϑԝ',
                            'кˠʢэKӵǩίʖȜ§ΪЛʹ',
                            '˙ŉ',
                            'ȥǼԁЂɂ',
                            'ҏȖʱɗƸɾ',
                            'Ϊ˜Ƀ¦NԈѸÙÇɟʲǎºЌΝĖԋʬǓѨɍǊʳ[ΗѦ',
                        ],
                    'event': {
                            'target_id': 'ЦßüãӬʇ¹ВŀʲBǽĨƌɚǤΖλsϔȩӥѤϺƶзćψƪΗ',
                            'parameters': [
                                        {
                                                        'key': 'Χ\u03a2ŀxŊɖ˂ǰСϼÔқԎʭ˾äjʡԁұǇѱѿƙ¿bКėťE',
                                                        'value': 'Ȧ˩ѣԍʞӃìЙґ˦iɺƔΫɋ{ϱȗ\x8fŭƑҊ˷ʇѺɐĮ½ĴǼ',
                                                    },
                                        {
                                                        'key': 'ZǚƘρћςϚjӜβ´ϔʎƫŦªƈЂϡƲьΈȟԝĔ1җfʘ;',
                                                        'value': 'ӊϺʁьʤëČ_ђыĖԢŶҩˎƔϓӴЧΝʫɶΝãöƸɯȐśŸ',
                                                    },
                                        {
                                                        'key': 'Үɽʵϙ\u0379ģɵ%ҭͳǩǍŤԘɈа_ЕӎĵԍMµÑϣ΄ɰʶ˅˕',
                                                        'value': 'ѫɑǳɁȯȮ=ÛȋɩǞˈЪǿėϰӢèÏʮңΠÛϐɁͶȭʵƟƻ',
                                                    },
                                        {
                                                        'key': 'ѻЅϷȓҮπˮЈ',
                                                        'value': 'ԟĝйТǨҰΉ\x7fРȶ·\x90˖Ų·φІπӥԅĞȥЏ\x87Ϥǡ*ʯƥŢ',
                                                    },
                                        {
                                                        'key': 'ѝʶ\x9cú˹ԈІͷ˲Ѻԛˋ6҈σǇƎÜƜ[γЩЫԁ;зʓêεǯ',
                                                        'value': 'ÊΔɁʉƷƗʹƶнðĝșôә\u03a2ëîʉӾ\x91lƋǝңԐΛԂ˾Ɇҩ',
                                                    },
                                        {
                                                        'key': 'þȽʧʒĪћҫNϖɥξĒӒԃF҈ɟѱŽɥƙΌŢʕҨ˰ĹпĮǑ',
                                                        'value': 'ΩэˀΈǮʐDáѹʘӀǱǥԤµĚË<ЬǻłКʸǍȈÂЫôˮȃ',
                                                    },
                                        {
                                                        'key': 'ôфȫ¨ԄРȌūЧ\u0381Əȑ®¿˷Ő\x96ҧ\x92ʗцȁӠɛ\x84ͷΨҚђρ',
                                                        'value': 'ҢñӶǟŦεĻИȸăԭΖ,\x9a\x91˪·ûТǢЈǜ!ʳʸ϶ƨǎðŇ',
                                                    },
                                        {
                                                        'key': 'ɮϏșӛӀ*ˮɽēǴ\x96фʶ¨ÌɠƺȍǇʳӎӛҖѕ˨ßɿǘЛå',
                                                        'value': 'ҒȠêbŕũǋӓšfȃ,ЫȪŻӮĲͲƔıïǁĎГM\x82Ύƶˋȵ',
                                                    },
                                        {
                                                        'key': 'ӮƊά¶ʘΉ˖ʹTĉIͽë\x8cΑŶTРŗǰςĸȼˍǤҚΆɸˡϔ',
                                                        'value': 'ēƝăǖǤЪϭТӈ\x8eùʹċϏ¶\u0379Ӗ˭ȴˢùѕǵš{\x83ϋȷϺ¢',
                                                    },
                                        {
                                                        'key': 'gȔƕԣɡĹΉƋɅВɰĔѭбЖȶQϒGϲˆ"ɖκʴ,ґÅʪԪ',
                                                        'value': 'Ǯхż¹ӦŵʣÍíΖԐƌe½C΅ŻĞΪҰˇȵûɐсȠɁȪίҬ',
                                                    },
                                    ],
                        },
                    'comment': 'ђѣȽÖ\x94˩\x8bǲ˾ȌϋЯuѦCѿάʤһǭ¾СƄ҉»ѻҐŲ˂í',
                },
                {
                    'keys': [
                            'ʞÊšί1ǬɁþƑŜǶϿй\u038dΘŀé˷â',
                            '\xad',
                            'Ζßbƣҁ',
                            'ǗӐ±ϷΔǙͱȱ\x9cеėρϞЩʬǸˆ·ǜʌɾĜ',
                            'ѺЫXüéόŌɧ',
                            'ιʆƞσrĶλȷɌźJ',
                            'ѢǢɷ',
                            'Ùơ\x9aɼҕĪǶԎˡé:щ\x99ͷȹβӞĜҎǶʡщЃҼɂ',
                            '}Ͽ\x89ȥƄ\x9f3ș£²ԍтĽǮ',
                            'ѩϝɡĩʃłчÉɞ',
                        ],
                    'event': {
                            'target_id': 'иӻΚΟƽɞ¼˟жМԐʅŲƵƚŏĠºϕǓ\x94ЧǶŃОȡƺҸԗҘ',
                            'parameters': [
                                        {
                                                        'key': 'ɔͰц҄ϫȪϴý\x91ʌϤӇɸǰƏ˛ʥү|ȡӚķΝ\x94ĉɌ\u0378șʴԐ',
                                                        'value': 'ωʁ҃!Ȗɡ¤õƱ$Ě˩;ĈâӈȉO^ǧ҄ґȐ\x94Πüс1ηѷ',
                                                    },
                                        {
                                                        'key': '§ȥȝμĸȅƓѺѾĕЮɯƜиХҩŻͿȏ\x96`Ĥԧ҈ԃԅȍХіϭ',
                                                        'value': 'ΔͲʫɔɉłϋΤΡÜӸγʘȚǼĶԡҁҒ¾Ǡ Ҳ&ò\x7fΫØ҂ŭ',
                                                    },
                                        {
                                                        'key': '˩ĪĤǨӗЯǵǢɥЫʫіìϐƚЖTϜɷΕĭӼ×ɁŎɼʇҷіæ',
                                                        'value': 'ǝɹÚ¬ǯ\x8eƭˢǡω϶ϩӬӭěʪêʌ°ΞЎҳΤ½ҷ^ȕɵ˦Ï',
                                                    },
                                        {
                                                        'key': 'Ɔ\x96гͻәùәǿɕӽХҋ\u0381ʃłӲ\u0378Қ˱ǅȃMΎʦԟɊʐ',
                                                        'value': 'áҕƤӈĵΔƀΩīÖĎż\u038bӸˬĈ϶ɚĥҖʻ°ɰ͵ȪĀĶΩΘΦ',
                                                    },
                                        {
                                                        'key': 'ɜʝԞŒ/ԩӔǯȲ`ʇϞɐԎӼȿЄԪ¿ŕŀŢˁĜă͵Αρϧɽ',
                                                        'value': 'ѢȉĮѓȧҚα®ɼԢɊȸїĿğ[ɊϼҼ\u038dԀŀȨĔʜГιλοΎ',
                                                    },
                                        {
                                                        'key': '&Įëbɛ˦»ñϺĔԬͳΖӬͷѯĲҭɎǼTéԞ½ӝć˹ɺBӀ',
                                                        'value': 'őЉŤЮh˂ƳȋçӂѣǓқɏʹĳБӅΝ·ɋ<ÕƞǸōˢÕÁ˗',
                                                    },
                                        {
                                                        'key': 'ɒЩɁёуdȆƚţɳƜΚ˯ƭϊƳpƆȤǓųӌgɒŝɲʛЫư+',
                                                        'value': 'ҊЫЉʇӈɇŊӔɦæƭφԩ\x8aϝΟǆ˱χƁŃӎ(ʼϠη\x88ιǯҽ',
                                                    },
                                        {
                                                        'key': 'Ʒ\x82ЪȮp',
                                                        'value': 'шӼδɗńʞћѵΦǇһ҉èԘԕ:ǴЫŅѫƚϝÖÖӐąÏĞԨҖ',
                                                    },
                                        {
                                                        'key': '\u0383ǘƿɒͷɝԙÜuβʤʪç@ƈβɚѬ\xadӃ˔¿ϋşƙχͱψũҦ',
                                                        'value': 'ƎӘӶĕ͵ê[Чɯє˱pÈԩҷӗ3ˤωºԩɇʚŀŒНҭȨĵͼ',
                                                    },
                                        {
                                                        'key': 'ĝǕƜΌ\u0380ǟǧĎƩηɷńŸĀЁԙЋ\x94μӺӀɡϖќȔӔӴҠ\x82Ä',
                                                        'value': 'þЫöȹЭҀфРƇбѱҋаΞbєҲԀϓƐѢ&ҳʆAӸɮǿ˜ˌ',
                                                    },
                                    ],
                        },
                    'comment': 'Ήҷø7ǑüĒθыș/ӥɌѿfėǿԔwӖˀ˽ϻĝϑęԐь>Е',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'ɘ',
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
            'name': 'ƊUвԒáţʇєфϿǩώʺ\\ҶlͰǨ',
            'description': 'ƇǹĂԝԓϩѿѴĮ-ʹʂԘκċĮΉ±ĩШʖҬȟҫөҦӼJȄϾ',
            'target_id': '\x80М²ɯǯɕҕψʻĐWǏƅÈκɊƭцÌȕɠҚiϙҙµ7[ʶͻ',
            'parameters': [
                {
                    'key': 'СƁǢӧѰΣԞˢ?ξŲĴø\x83¶ԣö/ȭЏӳқƝάҾxȥáŒ˄',
                    'description': 'ύԕʙơʭʶdĪϞʷӸӢͶñҼªҵή~ɒтƑҾΞłύþÿҗſ',
                    'default_value': "ɃǸˌɏĠʣȝЦɓԓ'ĄŰ\x94ɭћDй\x8aԬӮԡǊΡͶҢôʳ1Ѻ",
                },
                {
                    'key': 'ˮʌΥѭɽȋъ^ӡіǩ\x81ЪѲюԃϏʀӍɱ\x90ƚɻɌʟɅˀȸήb',
                    'description': 'Άȧ7Ŏσƒ˟҆ҡǎɦÄǹƇ¾ΌӎҪБ˔ӀМłʉJ¼ĨÅÛș',
                    'default_value': 'ПєƗҔϮҪ\x9cö½әϷғšßϮȪŶĎçʷûZӼČæү\x9f¨ӹҙ',
                },
                {
                    'key': '®Ȕʢ˳ʹ\x9fтÒӫúӽ\u0383˞ŰĳķÁԥˊçиѽƛ«Ɖͻ΄ΕÛª',
                    'description': 'ΡÐ·Ε÷ԐӍӢĢ*ԟƽ9Үуҭ¸ȑÔѶƐҖёүįбТЫ;Ԫ',
                    'default_value': 'УѲ½ѧǲʱDҚѼʧ]ƏΊÀԨʭ\x83ɄaΉɇбÓχБÜ\x8e˃ӣǦ',
                },
                {
                    'key': '\x86łƎζшΡί˸ϳӨÏͻhЮɷҡ&ЧÅφӊĔȄ',
                    'description': '҄Ϯə˽Ď˂\x90ҋχʨѣπӭɎˍѓ˪ѾʓвҜӦϢȻАͰ?ӈȺŔ',
                    'default_value': 'ό˵δӹӅ\x7fĖȝȏæԄΛҎƛŚO\x88ůЀɳȽѰǄѧҔ҅ӚƑƑď',
                },
                {
                    'key': 'ɧƶǟΗ˱ŁʏϢȟż˒іɫƜǜԞ˘ϋΝťă˟Ð\x8bùӰͱȓò\x87',
                    'description': 'ƜҭӴ2\u038bÉɤʛŒƉРɷȔ-ΎʮġśŭЄ¬ԧƮǍvɇĈ\x81ŅŒ',
                    'default_value': 'A#ґ˼ƶѻɰǉǩьȨƯ/˴ƈƑБқMͱЁϳǬȍɜλЄͿòХ',
                },
                {
                    'key': '˛вѮū¥ǀĴɱҕϖʎ¾ţŹÍЖӢɀÑРKĔǰ˖ϙɈlǏ^ơ',
                    'description': 'ӎŗȸÞròşʹŝzѭԑΛѹ®ΥˆÇɆxѰӞǻӎϋáҴԎƾ\u0379',
                    'default_value': 'ɆÏ϶×Оǜԇ|ϤцćŲщã˦ʤϺĿЭҚҎßɚŀʞѧʪ˗ˏĎ',
                },
                {
                    'key': '¶xQϹǣǏPӅĆ\x90ԙ˨Ѕɕ˓ΕŲϣй˶ǜ˵ˊ҉ǝ',
                    'description': 'ˮǍɹKЄ\x9bÊĉǄǠӠ˰ρ=U[РеÌ\x92ȘѨǗɖ˅Ɨюϖ{φ',
                    'default_value': 'ɿ2ɮɐ\x8cНȢˌUÄӻɇ˫ġ˝ġíϫcTÙͼɄǲɊɟѩϢӞ˚',
                },
                {
                    'key': 'ÙÄƘŧԃӿɍ˂İ\x8cĭ¨ѺϺү¼ƞēμ˷ʬǧèёǗԄЬ˾ϯı',
                    'description': 'ҿÌŝɧşʈȝǪ\x90мĄȽ϶\u0382ѝ"ξ´˄Ƞĭƭ\x9bYҘţɯϨĂ(',
                    'default_value': 'ϦЕѬȎċ\x89ǯoʬćʣѝžνǀˊĈӕԂӓāӟǭʾ\u038bˉ˙ϻòЁ',
                },
                {
                    'key': 'ҴëƵ{ȍFʋ˄7Ƭ˃πϋŸǎʖkÚİѵˀȃʹъŎĥɐύЦϵ',
                    'description': 'Ėѭdǈħ3ƋSȷΨ,ğ˓űΐŶɞŇűʔҤ\x88ΘơȖʒưıIÊ',
                    'default_value': 'ʲΎþуăΚÿnβǉĨɝ÷ʥȽӀԡϱtʗǐӗƊӵ>ȇȑƔѐø',
                },
                {
                    'key': 'ÒаƟԘxŹªüсǅß"ˑДɰ}ǧԂ#',
                    'description': "Ƞǉ!'ίӥǓЊͺϊćơ˼\x7fǽťӞ?ǮЧ3ϱIΒԈģгқŵŧ",
                    'default_value': 'ǟčӮß˷ϯˏ`(ϫԖ\x9bχҍʇÀ\x8bÈȺˣвӐ҈ҜΪӊǝɠюų',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x91қ҈',

            'target_id': 'ϿÆćҍϐ',

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
                    'name': 'ϢƣӖǸӝʏRɤҐЏϫШ˨ɖςrϞώƉˋҏӊͺɲÅԢϙ0Î˯',
                    'description': 'ȃȣ\x99Ӭū\x9dԉ?ЌȟЀ]ȭϰ\\Ӳ˻ƺ\x98ɗϣƣӷʑƲɻ˃\x96é7',
                    'target_id': 'ƒʅȵԦȸǀѳƹǀκ˵\x87ŖƶÀҌȆȥõʅ"Ӊ҆ǚѨђεͷӂİ',
                    'parameters': [
                            {
                                        'key': 'f¢ίǚЊ©Χ{ͿςҝԞИұ\x8eҳEӑƷɌŹΠǦӚ΅ǲʬXҁͷ',
                                        'description': 'ƉҜҶ%Ś¹ȡĠчӸǆό\x83ˈѾōv!ˇ˪ϖӅԇѦ҉Ț3ɊϊȬ',
                                        'default_value': 'үǹ%t\x8e·Уçđмƭ˫$&ĮЮϫ·АϰȅˡƧ˳ҸҫВďԒã',
                                    },
                            {
                                        'key': '\u0378$ӚҖσʿ˴ʾóȐͼ·ːƪ',
                                        'description': 'Рăƙыͻԥ³Ǿҵǡ˝{¡ƀ϶\x9eӥϝȞʀңӠǖαěãǽԏоĜ',
                                        'default_value': 'ȋȔԊƟԓÖȩȩǇӓδͱǚѦĚцΜ˜ʫkКɸѸп[БҕӀÜȖ',
                                    },
                            {
                                        'key': 'Ȟɑ˸ʦǶ҇ʮǓϊŞȫΐϴȨǂϪ\x80χź8·ǒ)Ğԥ¡δɘ\x8cϞ',
                                        'description': 'ĀЈҮϝП4ҏżϋʹԜѠŽWЁӼ҂˞+ɋȂyящҌӳ\u0382ȧˎǙ',
                                        'default_value': 'ʧƳʸ³ʉӊϤҾϳĲʉģɧǁҽҶÚʑ˾Ǆȿȍƞ,ǶŀӗȸӧϞ',
                                    },
                            {
                                        'key': 'ϕȪɻʘñҰ`ϩНҜÊѽǙ_ɥϘӾЭͼƦнȹӟǏҤ\x94ҡЛű¡',
                                        'description': 'Йʰπ˚ԤˎʦрşϗǑ\x9aΒӐaЁ¯\x9cȯŅɊҘñӶВγϞНƙʻ',
                                        'default_value': 'ǒ,\u0378ǽӁ½˕ҹԜϯȑӊƩӂԣΦǹѨ[ǷTƺōŰ&˛Ƅźƅº',
                                    },
                            {
                                        'key': 'ӳǥĥǒÖϧLԛƒɸÈѵΕ˚Ǣ³ǡȨŧïԢĲεƬȀϗĢԌτӥ',
                                        'description': 'ѫƅΟȪ˽Ӫ\x81еë˚»зτάԘ\x83ϢӳϓɊӌҽQʵȡÜЦϧτƸ',
                                        'default_value': 'ΪɢϱɼҪʛϹ\x8fʨʯ»ηύ˙\x90ƋǟʋPōȄȖćҠħǐԣɧ`Ɂ',
                                    },
                            {
                                        'key': 'ǘԆѯķuӀ¬ŭȀϻėԑǯϥǐȀöйҹϢԔëԛЇ',
                                        'description': 'вćøΙýύƩëʈƚȻљҶЂӾŀŭÒŵrӞщɑɶϰɕ°ɿςĝ',
                                        'default_value': 'ӁӹφχϞńӊů}ɮυ±ƈ˱ҠӴĔћħK!˜ɘǨʊЁςɐ×ͺ',
                                    },
                            {
                                        'key': 'ÇYʫĪɚѮȭϊМȀԐTҹčҧ\x83ϦΪWԐΆӻȍĐÕʎƮɃɍс',
                                        'description': '!ΪɊʻɈɦѻӒǝ@ɭʰ҄ͱěžĄˢΏǔŀыʝ˖ʆτϜԀ@Ϙ',
                                        'default_value': 'ψҬԢяδʤdԞɋJΫʲƔĐʬßǁӰȕ˔ĥªɐʒCʥTĵӷǹ',
                                    },
                            {
                                        'key': 'ђбх\x98ˆȝ,˵ӡυǛǲEӛѾoɒɒǳѪέÌҠƷŁıЫ˞Αӵ',
                                        'description': 'ҴÏNÎˎĖȒêєįƾµ½ІιО\x98ԍɑxŝ͵ÓǷˆαƕԘсƜ',
                                        'default_value': 'ȁ\x97ʡrN7рҚďӵĳӾԏńѮÅҙƲȈ-ʮҾǼǅЪԫϟ\x9fуʟ',
                                    },
                            {
                                        'key': 'ŬҊіʐ\u0380ȡ\x97ÄΚʉĒѺŌɕɂПǑ\x87þњ³ӰǅUǬ΄ǵҸ˃˼',
                                        'description': "ƁǯĕxЅƉŴʂӛ϶İ?ӐҾњњ(ÇМºʰôƸəΩ'ҭԑѰϹ",
                                        'default_value': 'һӭÖҭ˝èȈƅÐʒËʉȉ\x85\x94ÍƧâ\x9cӳʕɊУiY+Ŗ˳άԮ',
                                    },
                            {
                                        'key': 'ȄOƐԎõèǗґďŻʱңČϧĽƣ{²łҙəϸя¯ҔԩƑ°ȋɉ',
                                        'description': 'ԊӺԦŕǊύҬɰ|Řźϑp ȉŬԈυ˳\u03a2ʻˎʖɽӗԕΙÚòʝ',
                                        'default_value': 'ҸʟàȐҟѫϕοǯҌĒЕҿəВǂԒƊԊҦѧĩӖӚƞ5ŶƆƺέ',
                                    },
                        ],
                },
                {
                    'name': 'ԁЀ¥\u0378ęɓԗ´ĿƁùƿ7ɮ]ªΙμҙ˦®ϘŋԁоͿˋƫԝȢ',
                    'description': 'BӴˁѲǨƸÖυφŽ҉ʩԒĤțǑȺáѾҤĆ>_ǮΖyjԃ\x92å',
                    'target_id': 'ԓȤгœƗ\x8bŤɤƘӟƊƾǹĿΛwƄ˪\x87FʙƢąVͺĔӎЫˇΌ',
                    'parameters': [
                            {
                                        'key': 'ΚԨĄÌφ¿АƸ·\x97ɗ;ǫԄ´ѼťԎCĒɷӹɸ5ĸπѰʗ\x81İ',
                                        'description': 'ÿ\xadϢ\x9e;\x90т˫qǵ^һΚϯ˃ʆϦHʔЉ˼3Ǵ2\\Ø\x9aЂӹǀ',
                                        'default_value': 'ƳԥζİӞìςuͱǩȂŉŀŘ˩ҦԗSҭˁ˩*ϬВФԫΒƉȰƠ',
                                    },
                            {
                                        'key': 'ƚƅ',
                                        'description': 'ҖǀЍĮΫÓíԓҿȀЉȷѐӣĭгŌɪҲďýӎѹ\x94ƌŋοȃÔԋ',
                                        'default_value': 'ùC\x8aЧ˕ ƎЈƤ͵ûЫɟ\x8eŕɱ\xad˟ê˷ĮAԭ§ГӦ҅ЩЎȏ',
                                    },
                            {
                                        'key': 'Ӑ\x89èeЛƈľԋ§ϿĬ@ź˨ҾaăˍˏʽԬɀ\u03a2ͻ\x94ΥщʚΛƒ',
                                        'description': 'ɐºǻҌάȴϔld³цØš-¹ȟɄè+ǔŢȎҜԁӡfШѲ¤љ',
                                        'default_value': '҃ΩͼǥǡȚǌȃӕįхʖʟҠǔſǂύϴ¿ҡҲʷYžǻ\x95\\3ұ',
                                    },
                            {
                                        'key': 'ʍԂŵɪĞ˼ļӦKƮȋɹ§ÙЄuԏ˘ӨϫɁͻ[ԘϬ7Ҙɩƴž',
                                        'description': 'ʋ˚әѰҸȞǫɱǐ˵ΧΈɑҮ\x81ˏˮ\x85ÂʘʴϣӤφʒǲÕϛ\x81\x89',
                                        'default_value': 'ėʓƳɔԏόɞɜƃϪƐʡŹåҍӤʌΏˬɶłЄ?ĖʉƬѾ\x9dʓ,',
                                    },
                            {
                                        'key': 'ǊʗǾɎчѳŻԜȺʀŖÒӣΓ[ÝҌԕϫϢ҉ŚŃƉ¥˕',
                                        'description': 'JŦέϳԏяǴκԃԢӴ?ϓ¼ˤ˗щˏǪƛˆ¨ԠΈ½нõрƟӉ',
                                        'default_value': 'ԒӦЛĮɭKҟԜ¸ȿӖοϊÙʮѯ\x98ƐÜǵҀũԙζɤư5ȭƆ&',
                                    },
                            {
                                        'key': 'ēўΗʗΌνʓɁ\x8c{ţКŬǺӂɊӞiӱЕȏ©˥ƣĖ',
                                        'description': "ө˃ʽɽхŬ˝ɗŏ×ЧŉӦАʊ\x84ʈ³ºҧǅƻҧǙ'҅ĝʥӳ\x94",
                                        'default_value': "ǓɎˣ\u03a2ύ3ʨɒɲǓǈϥɈȤ'ͿǱëĊӊŋʔǋǎ-ǜȗĒXʂ",
                                    },
                            {
                                        'key': 'ҜcĈɬđ²˾ʆɴʌŘɘќіǢżӆьȁȮƞfʞʰӮƕБϫɩӏ',
                                        'description': 'oʧ>άªȬĨӕǍ˞šԥʍ¢÷҄ĬҔӐÂɮΌĨьƩ˜˸ҪΧ¶',
                                        'default_value': 'ɚϖƫ˭ԈͿʅЇ\x87ȼũƔʍɪѴӁ˪ǃŗʍʦБÆɉňˊѱʇмˋ',
                                    },
                            {
                                        'key': 'oįѢÚΞʺȑƈӞɬϑɘϜ)Ęϒ\x89',
                                        'description': 'ԏЖϑʗČǘŤӦӻè\u03a2Ƚáѕ˖ŭˊϹNԖƭ]˦~ѵ\x98l҈Ԇҿ',
                                        'default_value': 'ʁϢҘ6ÿѼӃΑɂӭӢǽ1ӾȲ©ԝÏǆɞҚkøѩϠˍğĄΛʺ',
                                    },
                            {
                                        'key': 'тˁЩPѩkpЦθε\u0380ѧλȲȈϘɐʼГ˸ŃԂԓӚҝèƒ0ҦƉ',
                                        'description': 'ЏołφҔǰĵЇАƳϺγ²ПҚOϱι\x88ŜƼӮΛʐӦӖ²kόâ',
                                        'default_value': 'ʩ˜Ϩʺ®ÐўȩҖͽ;ďǷϠ.ȝȃҕíșж˛˾ϸɺɒ\x96ˇρԁ',
                                    },
                            {
                                        'key': '\x9a§ȍȑĔèÕеϵĳӝΡ·ˮ\x9eҞƄįЧŇɵϟ\x9a\x98ϭȺԃĘЮ\x86',
                                        'description': 'ΨưŽƈɛҒŻʀϥÕ»Ӂ҆țє˓ӡϥ7ύӐ˷Ĕż¹ǲȒâǈӬ',
                                        'default_value': '˻ëҷѤӀ!Ĵ˓ӆZǖӛәÑŮͽƮșʌŤƊ#ɚd˷Ɂë\x84Ɇċ',
                                    },
                        ],
                },
                {
                    'name': "ԃǉʡϩӀԩʑȮӟĿϵɵʒƱͰ'ɌɆňӱӼʑӕ£ȠÄ)ԍɡʯ",
                    'description': 'fΎʃӂӣКWΡȓϺԪгÌȋŹƸϘяϘӟѧε{ʤҠǳ\u0379Δόɬ',
                    'target_id': "ǽӤǁюʀřʼŞ˄ӳ΅ŅˀєfËԍ˼ҡηӴ\u038dʢ'ÈȁwɼЗĺ",
                    'parameters': [
                            {
                                        'key': 'Ĝ¿ӡϏǘȃвȺӯѻϬŁŀќƍԥѬҖÜɣӤΏƍǖĭ',
                                        'description': 'ƦҗƧ¼˭ÎʦɊjϬƊɹҫԔӅʼƄҶӫ΄Ƨ\x85ȭ˞<ӫš\x8cԚЎ',
                                        'default_value': 'НΩ\x94ҰƵǦҗŖˮɉʀųƫϬĔđҴįȱΩțʖ;Ƹчć˝ũШΐ',
                                    },
                            {
                                        'key': 'ɭǧ\x87øѠӤүөŸjŶɃʽƘá\u038bưΈͶιŨǱtΈӻÙ҈Ǻ',
                                        'description': 'ϊ',
                                        'default_value': 'iʥǘǟʒҮžʧӌТc1ɏŅƩƋұɅųD;ЇȌфOĩÑz8Ӣ',
                                    },
                            {
                                        'key': 'ԒPώҀ˔NȠҒҌɁӠѻ',
                                        'description': 'Ҁɯ(ԔəƎϺʐČӶєɑÂńѣȑȪϻΊԛҊʍВŭѻûқōʬŌ',
                                        'default_value': 'ԜTϮʦӳǽȐïʳȧТŠŹҩϠʀ˥Ɔ«үϒŖɇ§ϚңԊǱSԂ',
                                    },
                            {
                                        'key': 'ϿȰ',
                                        'description': 'ҦмĮǄγƣʵ-ăϢ¼ëҽтʖԞňÄʬϡ҅ѧɌʛԗӗъԫ:ԡ',
                                        'default_value': 'ţϏƤɲǋƐь\x97ʨХʌǳґӴϯ\x90|ʺÙӸȱƋʘµ˗ǖФÐĶł',
                                    },
                            {
                                        'key': 'ϫŲӝƚ»ҶҢҫɘʳέµΒűњĝvĎ©ќƍĔљçѶ˚ҢˆоȚ',
                                        'description': 'ȸԒϨʌȰϫŅ˶9.κʼԏʳαŐΧŬѢŒȬлЙɶә8әӑϨԝ',
                                        'default_value': 'ȌѹĠȚϩɻʯÜ\u0378ʺʗЫԀҵu-ʤɂȯϱɉʄʸŬұϽâɖҲÂ',
                                    },
                            {
                                        'key': 'ʣęơəфһǭŘΕӛĄƔѾɊȭʫcһӧПǄɵčÌİă\x7fˇӬ˰',
                                        'description': 'ϩƱȧȔƞʎδӟӄҜԁȓεǈΗӢǉϡÎˡԄǵ҈ʞƝ˨»јҜĚ',
                                        'default_value': 'ӫʑԮʋӢ\x87҉ȘѾũҪϧĴИţʚƛ҃Љʠ\x8bɦ҆ǬϰҪЖąάā',
                                    },
                            {
                                        'key': 'ǋњ´ūÚ½ÇӺ··Īeļ8\x93ǦģΈdЛ¥Ұ˪ƒ',
                                        'description': 'nǗΘϗ$ħƛĢϺŌΰȈ˒ϣҀƃǀĩǠϽƉϙȢόɻοÙҔƣǚ',
                                        'default_value': 'pÌȔÞͲοnɐӽèСƝηҀàɖɽƙDοάÁjxȷМиȊϐơ',
                                    },
                            {
                                        'key': 'ΧȟȱӧҠɌωǄȼҁįЁЅ.ӐʉÓε4ςсȺɈ҉ɿɨȬˡň_',
                                        'description': '1ʍǞƺɦ˒Ш\x8bǌӵƊ+2ҟǞӷȾɲ˶ɞŦǻѱϕ\x8dкĨΖļч',
                                        'default_value': 'Ҩƺ?»ȒƭɾȯǬ',
                                    },
                            {
                                        'key': '҉Žƀ#ƽӌŽӿĤżɋŉԆȃŐԝÎҪ҉ϞҢaG·ѕѳʝeLΪ',
                                        'description': 'ʔМɤËŏ\x94ǧʹȓѵɵǳ¡BŃηȲҴǷ`ʽ\x88ӵйҋϗÒƑ¢˻',
                                        'default_value': 'ϣІ\x88ƮΒNԙʚÉɺеҪǃΥͿ¿ԘВӼťʳƒΜɌƙ\u0380ǐ^ɟŮ',
                                    },
                            {
                                        'key': 'ʇɈƦý˺ʣ˼ǩίѽΈÇĳԈƜƋȎ',
                                        'description': 'QҮҕѫȟ˓LŒέʁ\u0380Ϡ¸лһ`äƟӡȿ\u038bÛĳšɄȹӼǔıї',
                                        'default_value': ')āŷĥΰτwĀsq΅ѡɧЫЂˇÃ+ˢҚϤԈҩ΄αŽΏ¢ŪӞ',
                                    },
                        ],
                },
                {
                    'name': 'ʉđϨŌҜө2Ӵ\xadÔƒȐʏѐƎƁѯΆԢʰХ˂ƱҧːԡʫίOϫ',
                    'description': 'ĠʐԊԗҘQyŠеǾӘĂεӞčÝɩoˈǱqǺƈŊȖǫЮɹҿʅ',
                    'target_id': 'ɮ8ɢşϺΖӑȶӌʂӣѠɳƬëʃϦȊŠƞҰӆʠ΅˗ȗ"Ȥȸǜ',
                    'parameters': [
                            {
                                        'key': 'ĎʠʛdЁұFƇψ\u038dӷÕƵʼ˯ʹԌÞƶӾŨŞȌƍȐӒȠϏҋͰ',
                                        'description': '˼ƙȴщȝŧȆҟǋõԂƿªɐ.ɧŁѶͽʵƪ\x9bԜɼͺǳĊӳЬź',
                                        'default_value': 'ҙϵѥèʹƓ҅Ό\u0383щȧ¶ϓБÓҤΘσԡļϨ҆\u0382áЩƈƀģȀͳ',
                                    },
                            {
                                        'key': 'I϶ŴԫԂΜˮʬʱȉûϾ2ñь»´ȴˇ˘ώÄƜʵηƈѠƢʱʓ',
                                        'description': '˜\u0381ЋȠʶʔИПwү\x91Ɯɚ¾ʿʇŹƦƢʬˌVɜïŜΞ\u03a2LģС',
                                        'default_value': 'ƋǰʭзԖȺĥ˓њ\u0379ɩ˷Ȓ\x96ҕ^JȠͷǘŻ˺é¸ѥƩˀŮӆƂ',
                                    },
                            {
                                        'key': 'όӊӊǪǄԋʧJЃғ˵ŝ˩ÈǷϺˣΨĵLɏҰ͵ûϔʻĸ\x96\u0381ă',
                                        'description': 'ҕPÃŪėŮȹ˫ðσϏɓ˸=\x89ˊǞĐȱҫĢȟ\x92ǙЭӢʪPԇȦ',
                                        'default_value': 'ħ(ķώ\x9eɁʥˎҹĖƛ˻ϒӋʪԨĶɀʽ~ŎǗ9ԚɘnȒѐгH',
                                    },
                            {
                                        'key': 'ɕǯɯļѻIɊŪӢǜǜѮήΪеÓÚΐ˹Ԗʉү˼2|£ŖƊǤ\x8e',
                                        'description': 'ԧçɒΓԥ2čĤʸǐӇƐ\x95\x9aњÍӹĭ\x93ԓєěȯͶƦìĹŴѝr',
                                        'default_value': 'ǈÆҳȕ˼ʥÄȢ˷ÄAĮˡӁ҃Ð·ςţзǯͳɴˮƎǗǿ˥ÀƋ',
                                    },
                            {
                                        'key': 'îΚӊʥɠʀɶ¼Éӿ˳Ȟµǌ',
                                        'description': '˷ƀâԉͱ˙Ȟǉǟӈð«ϯѵ˴\x89ϿŨӈ˽ϋòҦπŁͲϙºɎі',
                                        'default_value': 'ȮQǫҋ÷оҶǼ\\źξÆԇƆЉĿȵʒʔЃƸϜэ\x89з˷ȃҁˑ³',
                                    },
                            {
                                        'key': 'Ӭˀȋӊω[?Ļg',
                                        'description': 'ƀȚȬiɔ˗Ϛϔ˂ȧѧǞĉԙҊ«УЎ®ʼĆӔƞé˛ϴĄһh\u0383',
                                        'default_value': 'ɢɄ˯ԂðѶЃʿėaɲѼóɂ.èϏΑϟҀʿʐԃѽÜԥɿřӣҨ',
                                    },
                            {
                                        'key': '<νΡοҌʚӱƏҏ',
                                        'description': 'Ҹ\x9dȻͰģЧǛȥǉ´ľ\x83ĔʺғҳɚϫXŀǓʨˊȰїѓҁɼɅˣ',
                                        'default_value': 'ǯɿʬҍϔˡîԟŃƺұƚӰɽÈǎƾ|әϒšѲҶϊǯȫȦ¾Ȱϒ',
                                    },
                            {
                                        'key': '¹ЄϟċĬс˄ԁĖ\x81Ԅ҆bǦʻʑɿЪʨÁ\x89ӁŃɬi7ɚДŅИ',
                                        'description': 'ȥћɕȑKťИȟѹОʔ͵НÅūª®ԄΐǤӸ͵ӿđԁɔɔ/ʽҎ',
                                        'default_value': 'ƨǊҎνɀ\x98ӼHǤʕ˟±ыƍӀi%®ˀЁŀХ_lţĨɄҾȱε',
                                    },
                            {
                                        'key': 'ĘþЬФӢȁˇψʕúųǤ\x8aɗǳļҪчÿǆӺƴ˹ĦԆ˸ΉЃ+ϵ',
                                        'description': ',FӟѩǀȀҢ,\x99NƞºìɀŀŧɆӼ\x85҄Ŵ^ʹӨƼЖрƴȝЈ',
                                        'default_value': 'çΥѬЀαɌШˤ\x80ÿđƷԧѤʑϱŤɚʒ_˗ȯɴǇқdʪòŪȂ',
                                    },
                            {
                                        'key': 'оȓʶϪѬɩЌϠ¾ͿҲњ0ѫȜЎҭœԁʺ\xadЯ˒ķʬΧ)ȷǏȒ',
                                        'description': 'ɉӴ|ɠİϪƉӶЎʤԕʢүȖǐpƼƤǄȡ-ǧ\x8cϬǌǏɁȓ´ӈ',
                                        'default_value': 'ǺųǄȏ\x9fƆöɲƖɏ\x94ŬҺҾѨʩˉÇЕyŒ/өҝŪÚ˒éȑБ',
                                    },
                        ],
                },
                {
                    'name': 'Áſ¥ƥЀc~ξKωΓʁʥҥгмǣŴӀʤ϶\x88ʵђ˴ɂ¤ĴǴŀ',
                    'description': 'ZÌåȦʁЋNΗǰϘȣϚõ°ԨӒϓԊѓ\x83«Ćєԃҫõ¸âɪb',
                    'target_id': 'öАαчҳԕȝǠčl˜Ϙˌȶҍ\x7fЎӼϔP¬ŒĉóτӪҗϣԌӽ',
                    'parameters': [
                            {
                                        'key': 'ɼƚέĊǬзϘξςʌϯϟɘӒΑЌΤȢʋƴΟÑãҭϋҟЃђϒˋ',
                                        'description': 'ɩɄźԧ˽¾ŭѓáνѦԋIҾȢ3ʌǌήʛҏ+ʉ΄ӋԦъδΘȜ',
                                        'default_value': '¿ǽԋȪɅ˷˸ĎʲтѪȧs¦Ƀ˷ƣϰП\x9eкäȴЂÚˈÈƪЪć',
                                    },
                            {
                                        'key': 'одƎʵȩԔş¥ďɿ˱ϠқĮƄґіє˪óШВжΖíŃʿѱȝЎ',
                                        'description': 'ҌuȿʣϗƅɏгԈʊο˯/ͽ.ȝ˪ӕĩ\x8bЛэƵNńңɥó×ǔ',
                                        'default_value': 'ԥǧǃΪűͳw7ɿȇĈʾ~ǊÖΒɩďӃŪƏXʦ҈ӮҗяϥȚȀ',
                                    },
                            {
                                        'key': 'ԁӧƫĎΣѐËƩƌȋĞUùǺ\x8bǔҡäɒƶͰĩϥӨкƷŧεşʚ',
                                        'description': '҄ƩѵѯĲkϞƼďƝүó®Э;ũĀeǽĲԬȞзȗɍąłӭǫѻ',
                                        'default_value': 'ʘ˛ƹƅЭЙЭӨˡΆΪɩˌıЎȇƤĝōǖϜKɊӂΜϋ͵σhԥ',
                                    },
                            {
                                        'key': 'ːѵɃϺğħ\x92҈žȴǡѦ˾&ЧþΆӷ',
                                        'description': '\u038dҳǌƍEÕϗϗǲįҵɌTƍ;ȋĽөИѬψĽ¢ǟӴˮ\x9b˓ӝǕ',
                                        'default_value': '˔ӥӝ¢`Ǔϧ˓´ӲθŢˀ҂ԨЉ$ʗӥĹĳʉ¶ӵŦſЬŧˮϽ',
                                    },
                            {
                                        'key': 'Ћ3˝ƒ˴ϾԨΩǧԑѐəΫĘН\u0381ȫ',
                                        'description': 'Îſ§ĥ¯CҙБ҃ԩq\x8d˻\x94œʁǟϯԢɸƻĘӕ˵óůOȣұǟ',
                                        'default_value': 'ˡƾҬ\x8bԐɴͷHˍ{ΠƉΖбˋ˺ΑɇДǢԘ\u0380ǲ^˦ѳï˫¿\x92',
                                    },
                            {
                                        'key': '<¶.¡\x97Ǉ',
                                        'description': 'ĦϙÏԃʎ˅кÚ:ǚѻγȆ:ŸѹӸˉҷʙϺšŬ\x85ǝˋмĭѤƐ',
                                        'default_value': 'ºЌЩøҰ6\x91ŮϷФǃЈźКӤҦȎʜǬ˫ǼȧƎŜΰ˜ȻǂҬϐ',
                                    },
                            {
                                        'key': 'іŧЁБаǯĆƢˀȶƼǲӂұӴʧÃȽȽʝпɫΞӲҚPƫԀˆƦ',
                                        'description': 'ϧĽĻԅˈϪҹņtҤӍʜbŠϪƽьōѢʶͼ˻ǾǆʶˡÔͿҢɺ',
                                        'default_value': 'ɈѡјΑЇǅɷЯʦӘ΄ˌ҆ΒŷÃцӺ½îΎň=ť˓ôƇì²Н',
                                    },
                            {
                                        'key': 'ăŃӟΜЃԦӿ|˾εäϋӧ϶˛ЭäθҙЩêĻǚέΤ\x9b\xa0Џʌβ',
                                        'description': 'ǤȃԃɆωГЧǐ\u0379ð˦cƸƣǥӭԝżǕҼӳń\x9bҋ˕ͽŒ˸˗\x8f',
                                        'default_value': 'ǰĄ˼ЇůΦԉαӗӚíТģyɷƬӝſМǩśƸ¯҈Ͽ\x85Ϸ=ˁѯ',
                                    },
                            {
                                        'key': 'öºѴǊȼϬƗoÓ²ɡѶƊӊøʼˈԄȻԑөϭԢaʓȮ²ΓŉÁ',
                                        'description': 'ΞaӚҹαѷò%ʸƑZΞжϳɰԦŵҥ\u038dȮý˗Ѷǂ]ƈΊʄ\x8cɓ',
                                        'default_value': 'ǫÅͰͻҹϞҠεǳBӠnԎeʰӯƇêҸЂίϽ\u03a2ӱɩʴńӪ˝ȩ',
                                    },
                            {
                                        'key': 'ьЦбģҋҿǲƠњĄȷʢȓЎʒŹƿԋΘȢШœȱԬ˶ԏĔ)ԩʉ',
                                        'description': '\x9bȍӪýȋϭīЮQƗІбЛ˯ɡʩŭŔЉ=ů¾ϮĄђȊϊĕӁƃ',
                                        'default_value': 'ћѧҮPѠѕϧŝӬĺ˭Аюө\x81ά˚ÆÊƮźбäʗϰ˰ƹ˩ǯǷ',
                                    },
                        ],
                },
                {
                    'name': 'rϼ(ӘÔʅ£ɉӋсÕĆѪɄżĢÞƋӂқӮѩũAԕ\xad˗¢ѳѤ',
                    'description': 'đФȷΔʫńѿˡϞԈŢϸѴʬ\x9eÛгŘčʱϲǵȐΠϵɀ®эϜÐ',
                    'target_id': 'ɺ¼Ğɞ˷І\x8bǑĬŇƫ6ŽȈ)҈Ͱѿ3ϠđǺąžңԚűгxɛ',
                    'parameters': [
                            {
                                        'key': 'Ѐ\u0382ɡõhϢńԙ?²ңӑΆπĮс',
                                        'description': 'ϭǑōΌг#ǗκЪόǢʊcʏΦǛЫ0\x8c\x92ŇȃČηϨʙȵ˰ԋŷ',
                                        'default_value': 'νЇ·ǵ=t˲ζƖԪbЭƐĝːļ+˃[ǕOƤCзҜÕƾϏ˻ω',
                                    },
                            {
                                        'key': 'ȏЁϜąŬФԨЄҹɦǅȟGxЎѠ˚ȺÏƸǦģǌĝ˷ɤШҺӴԖ',
                                        'description': 'ͱЖѮϛƜҒƩӴʸҹƚ\x94ű˨ĞţϷʔƢ\x97҃ͱІ;ǛԘȇπԣʡ',
                                        'default_value': 'ͶĚĞГǊҫȓԟǑÜӒʝ\x80ŒԉшҵΐɿÔέήˏєƙϵěӀӇц',
                                    },
                            {
                                        'key': 'ЦϖҗӧȖӏɩϔʘѢβϹĤȯɽ|s¬ǎЄɟϟҨШƵɰoӴε˫',
                                        'description': 'ԫɑқԖʦȥ"ʪСȂ3ŎÙuÈŷȫȔʇΣƎɎʮλєδĠβԞ҂',
                                        'default_value': 'ӡŅȵˌΌ\u0382\x81˨ӯǤƗíϑΪƭԀ&Ĵ˻ɴɚEȲēľçžЬԄǎ',
                                    },
                            {
                                        'key': 'zƬԨřўµυŚ\x81Йԙξôԋǋ·šŋHì҇:ƯэЊʘԤƍäƣ',
                                        'description': 'r˺˟ʳʈƹ\u0378Ʀ\x98)úʍԞǪȯîŮɣğ˂ňФϾ\x96ϛȲĨ\u0383ɥ§',
                                        'default_value': 'ҖȶÚόĹϠǍmÎГňŔɳ(ɰζV\x80ұϖŏԒʠɓǎşƻĴ˂Ñ',
                                    },
                            {
                                        'key': 'ԋэâ҅тĘƘĎƕíқϡžʄǿӊΦѿƘĈɲ҃Ԅ',
                                        'description': 'ʯʋΜö˅ȠȐϮϿɮНΗ@ϒɨӶǰŸʪԦԝť\x83ȐùɵДłјƛ',
                                        'default_value': 'Нϫιсʴїĕ\x94òŤ7\x99ǅԭȦкLԈȒļ~ԉäȵЀ,ĞюӸƲ',
                                    },
                            {
                                        'key': 'ȈĬӿѶǉΎǌǄƒɡȄԆˇаИËιʠ˧μŐϤӓǸЏӖŔƞЫϛ',
                                        'description': 'ˁǜÒaºӉҘðϙȹЪqƇяıҘώԇúȮɈÙƁɆǫǱʡʥԦɫ',
                                        'default_value': '\x942ǘȿàʓÙˋӂʒƏϣΐшӬVҝ\u038bΕӸǠ\x9bƚ´ўǔƉ\x90Ӯ˄',
                                    },
                            {
                                        'key': 'ȱŷшΪȝӉɭò;ԪȥȉʶЕǺØƅΉǉŵkɤǚҬÜˣη\x9eԔà',
                                        'description': 'Ўˈȗ˥ȩɀnѴԡƗϖѥëÛдºŊɖĒΖѕU¤æɓʉ˝ĺΏǠ',
                                        'default_value': 'ů¶ġǿзјsʥȓCȯºĠɐѩÔǢáϚηɎǸƆ҅ȶȑ¨ǆˊ\x87',
                                    },
                            {
                                        'key': "ƎǢß¥ƼʋӁɜÇ\x91юȞ˱ӚӝԛǒѥƗɮӾ¼ǁmѾѣԮ'ԑʱ",
                                        'description': 'ϞÖŞɀˏХΌѾ@Ԯ˾ɕPȽԤФШřáͱŘҋϊœƍҠƃ±Ϗɧ',
                                        'default_value': 'ʵΦȖʰħ\x8aǭÿβÝˤ×ͺџşɫʓȫ˰жϐÓƧ˘ϾVʁԕǔа',
                                    },
                            {
                                        'key': 'дӽǏНӛąкŖÀуӎѸ',
                                        'description': 'ÍQǨĽԝԥāїZǝǙӡџ+џʳ βʽϯɉǜӎơöӺԓΥĚ˛',
                                        'default_value': 'ԏǆęЙȦӽΑ}˯rͳǴƠПŁʌįЧ¡ʀ҇ӘπӺͰĘôѱ2ԛ',
                                    },
                            {
                                        'key': '\u0383ǊÀС',
                                        'description': 'ĳʚҺğȷʟ҇ʋΪ˃ǑǋüΫȲÉҜпäėϵųԈˢūΤΑĲˌ\x91',
                                        'default_value': '҈ʫĜɽÚŴѰʚõŮûϘȹɈԬǺǚýǄʹɍʊƶнǰmƒǄͲԊ',
                                    },
                        ],
                },
                {
                    'name': 'cщԜBϡ\x96ËĊԔȧ\x8b6;\u0379ġİ:˚ҩśCӸ϶Ϫƙ®˱NİΑ',
                    'description': 'ȹϯņŭĥȫŢŝ7āʼȥ\\ǩ˼ӠϮƩȀĝҲYӷYΣ\u038dʌũ\x99é',
                    'target_id': 'ϐϕʗŲ¤ΞÉɫ˪ϡԁ>ŧǃ¡ӺФƕ\u0378Lˮ¯ʑԮɀfīαȻȻ',
                    'parameters': [
                            {
                                        'key': 'ƖЊь*żĩԣɴÕıԉzŹĨɟȼѬȱϲӣêģҔ ҷɪͷÂı',
                                        'description': 'ǪͿČǬˮɮ2ϣΟš\x8eƞƸӇʌaωζɪҁЛѿǔϺЯØŵŮњȺ',
                                        'default_value': 'ςÝОмāԁǿӄӖѺʀ˽˝ϛǜǞʲĐÀ¬ŽϹҵCԚPψðԋ¼',
                                    },
                            {
                                        'key': 'ƌƯĻǃȐB®ŽãɲљĿˡԥȽӇĒȖ~Ƒm¥ʖơǄƙѶԁԪɣ',
                                        'description': 'φţɑӴ\x7fͲʗϚǺЄÍѩǾ\x8dӝчŅĀƓуkωҢɕ¶ύôʡƠӐ',
                                        'default_value': 'ǾͲёǼ2ӂϯѕҝɸʿ<ӴĚĒ2Ѹ˘ƉȀř\x7fĢȋ˚цӰĢ]ҙ',
                                    },
                            {
                                        'key': '¿ȦĲʼӠҥ@ʩғä¸',
                                        'description': 'ϓĪ҃ǀAϥ\x8fҩƪЪNщΌʊªӾƲƏԩжśƕТΘă¼ůâÚ+',
                                        'default_value': 'ʶǾѭɠӻĢ/иüʋȗĆѥǬȸʙšαšЧӝȿȒ\x90ʉϼ˗ˣǤv',
                                    },
                            {
                                        'key': '{ԋiο\x93ɅʊѬǣΰGTīƝûȾƆļϼΣΧΫʇΥ˗ωđүſю',
                                        'description': 'ĠʸĘǖҙ*љɘϵŨѠ\x8cԟƎɓǳӲʥӇĂ6ӐɽĎcӗàƣˇʥ',
                                        'default_value': 'ӛͿѥʲȻІΦΝ˸ΝЅȚ˼ԨȨɞΗēȺôх)ˉҩжgʔѕ˞Ɋ',
                                    },
                            {
                                        'key': 'ʅĤѩÈy\x95Ë˲ɺ\x87ӄфñ\x9fϋȐ@ǌ˪ƔʨӳÃΤÍbƴ˟őԑ',
                                        'description': 'ҫʤ˕ӶrČϳ\x96ԦҨәĲЙǩǠɝѢʂçĩſӃªțƉέжǫʱŭ',
                                        'default_value': 'ĄϪČ˲±ç³ǀ#ģϾnʅĬ@ɈԈԅŇϵƋΛԞΒӧҜ˨Oõԙ',
                                    },
                            {
                                        'key': 'ӧǝЂȃȝӦҠʍ¨ɚь˪ИċĖ\x89qÅȓȗĆϐºёҢѐªҫ˱˟',
                                        'description': 'şƔ_ҝ-ȈрĂԠѕȦĥѻҭɈ҈ƪҩϪęæēσ˒ӇôɌхŬŜ',
                                        'default_value': '÷IаȅљҫўǹҧԜɌʛѱҠ!Ƭ΄ИźΝң\\˩ΗϑñĪҷbċ',
                                    },
                            {
                                        'key': 'Ѵȑ¡ɄʍĘʢҭƏёǋ',
                                        'description': '˚ʰӔȷ¬ϷϱΰĠĕƏԈƷĔцм°I\u0383ϷʤӌГ}ʱʀԤʶӎț',
                                        'default_value': 'υӍό˱ăȠ˸ӕҲɯǩЬɜє[ήŶŸ˰єMƌƐүĵɲǘÚʛ»',
                                    },
                            {
                                        'key': '«͵ʉԪɞ˩ˮȟǦӠ\x8b²ӼЇ˫ɵɠKТ\x9aȹv˞ӱ\x84\x91Ȓ!б˃',
                                        'description': 'ɩӝҚιҒΧ˜Ҫ͵Ʊʗ¡˥ϪƬĈŞйƘ=ϛ4ԥѼΧͽʬϭүʿ',
                                        'default_value': 'ǘŇžΪҟǭԇɥ_ǐƫõǶ9ʊƇԅ~ôӕTӚ\x9bȠȃԫџŰĂÞ',
                                    },
                            {
                                        'key': 'ЊŇƋȯEѲúϝǨєʂ\xa0҅ƛȅȈMȩ',
                                        'description': 'ɜωŕӌ\u0382ԋӥːÈčΈƺϭҝ˵ƍɮƒѭќ¤ĉȹѡǝ»ȖīσŦ',
                                        'default_value': 'ҔӫŐŦБũáΰŹ˲Ѡ\u0383ͶϜ\\˶ǦȈˊŸό¡ȻŐԊȳѦΦĨC',
                                    },
                            {
                                        'key': 'ҿЋʟɬ˭ѺɯƢАèңƚɮȱǱȪԐсңϴĝ*жǛþȊƪāɉϢ',
                                        'description': 'ăĽʔ\x8eš#ҵԑɲɶ\x9fà¬ÛǠһÆĂɗ΅\x8eƭ*Θêȑ?ɟэÚ',
                                        'default_value': 'ѪҬüålʬɖѕьήӐoɘЀšђЛ˘ӭðƕҘĨŘ9ȊȄҞԫΫ',
                                    },
                        ],
                },
                {
                    'name': 'ĺЯȬtæ˙ħkԍ˭Ƞ˞Ɋ)ӒȼǛNӃԥΕӻķ˟\u03a2Óǵ\x91C\u0378',
                    'description': 'ǉřɾɱΎþФ\x90ЎŏˋƾěƜҾ',
                    'target_id': 'ʃǁáɐʇǒȳϹɢɦɷǁƇŢɗĨÄŧѐʯFԥϜÜŸ\x9cΤȭĔŒ',
                    'parameters': [
                            {
                                        'key': 'ÎȎŻɚɃˑӏѓўѭŚͱϏшϵSíƝŻӕʔԅƯ҂Ȁ˽jχԡĲ',
                                        'description': 'ǂǕǺƅҒϳҏƩƵØəƝʶϣƄћўЊʆȓʎǰѼфϐϗϼˬ¼ǃ',
                                        'default_value': 'ȟʋѠΜӱӆ6SƱԋɐʗƶʹſΩΡԔʕǱЭτǩǔ\x98ЪΚš˃e',
                                    },
                            {
                                        'key': 'ӕӌ\u03a2эŽψ"ԉǾEԤ ʨʮŝǇĤɠ^҆ˀƪ˫ǩɿòʨƖ;ʹ',
                                        'description': 'Nĩʪƛ"ԄɯŢКԣР˳Ҥ΄ɭȾԣЌŕ\x83øǲѱʶrшǤʸӎt',
                                        'default_value': 'υ@ѠƀӎŜҏϙЋЕȪǖκ˕ƞş˖ɗȮχɔzӶ¤Н˅ΘȷEÂ',
                                    },
                            {
                                        'key': 'ϳӲʬňΦЧÂůȶϏ΅ˠśǕȸ˳ӠȴƥȳӋҷҶɸǻʀϖѰΉʷ',
                                        'description': 'ђҡĄЖԢùΛЛ˂ϣªǸʡ\x91ӐȱѦ\x86εεɁșǔ\x96\x80ΌĲөДԂ',
                                        'default_value': '\x99ɼТӬͻÖͽӢļȭũˊǐԩɺΪʂΜŐĞ˦ɫƪƕԁʧΩŢлБ',
                                    },
                            {
                                        'key': 'ɂВŴ˛.ȥӨЩϩ\x88+˷ϺӮӒ',
                                        'description': 'ҪÐҙ<ӐӱŌЏʻ£҆ԓŷûƴͼcЛɁ',
                                        'default_value': 'ɑΕʒѬҋɩӑϤǚѼô˘ѱԑɛКиЙКԣǮʊѹҽȕϟȼqԛý',
                                    },
                            {
                                        'key': 'ɏºɒˎ:Ӄ·\x9aɛƍнCʙuĨƄΡɒϨǚƁԢ`њđˈ˗ɻɈВ',
                                        'description': 'dӝ\x94ȍаǖ3ԑɒλҖњʉϒѲ\x81ԤӮĥҌњəǝϯŦS¥(ȱɵ',
                                        'default_value': '©нң\x9cΆďĝԋϢтȮӅʢɖǀΒƚɉʋчǱɼˇбÆΎІƎQί',
                                    },
                            {
                                        'key': 'ҮīąƼӒĪ¶ϣʛҨұҸǑôĸȪc¸҉ӢӢӘʐЌƄΕƧϯ˒ɓ',
                                        'description': '³½ǅдӭ<Ӄʈ"eƭ\xa0ԨnʂΛſĻĻŋԥNʻèȜнjüʣɊ',
                                        'default_value': 'ǧǉҷ$Ԕʫǫ¶¾˝zЍɁήı#϶{ŉʃƁYҷΙʸɼӂĐӖÍ',
                                    },
                            {
                                        'key': 'ȚрƸȗџƛ҂ÉūɑʖͰχӃÙѴǗԄͲʠ÷ӟtӖʆŖ±ʷʭш',
                                        'description': 'ǛȽǶɧĠϡϾȷЉбǕřәŽƴɒұǶÖɊφʾԦϾԃϖϺфЗϝ',
                                        'default_value': 'ɒàŝ\x9cʿӅүЈ˙ɫԟĄҰ˳Ϟŵӽ',
                                    },
                            {
                                        'key': 'ŒӦɠϑɪ˦ʶћĭʠȞȪԀɲǄϜƞƩɧÞɐƋзǪӑөύħƳ}',
                                        'description': 'Z`ԆӜǝΩΊΔ˻҃?¶ӆ7ʼǜɎЈĥ¤ΌӭҧАƝ-ˡƱҜ϶',
                                        'default_value': 'ϳÎΉ\x84їO˹ДȅҴFϡŹ@ƐҠ\x98ńѶϲϔɇƋɾpƣО\x9fɪǄ',
                                    },
                            {
                                        'key': 'Ɗ\x82ЭÙ\x8d8ƏÔɰư\x9cɰζ\x86ѩSƔԤɮ;βɆ§ŬɉĉĵЗƐ½',
                                        'description': 'Λх˭¸ƷʳЌƽÛˢӲщͲĹ˯dmɬϢΗѿǒƂXШΙҢƪ½[',
                                        'default_value': 'ÛǪǷӜĢæĐĳ7°ə8ԛϤԖǜ\x9b×Їƥuxȹ˹ԕGѱ\x8eǐ҃',
                                    },
                            {
                                        'key': 'ɊłүѵƪĈĖa°½ǇβǲőқƝfҾ҄ʫӏð҉ͷĜƛ˦Ё-Ї',
                                        'description': 'ĵʟȖӐ4ĨǱȾӏӻВäĥϴԦыÐzϣ҄Ǔ²ҖӻˠɅ@\x88Яǀ',
                                        'default_value': 'ÐʚҊȕȄȭĨƽȴǡǫȂƃОѽDɔZ\x98¢^έàʯӟ',
                                    },
                        ],
                },
                {
                    'name': 'ΒºӺȒȊϫėN҉Ȼ\x9dшʍ',
                    'description': 'υ(ȬҤwцBĀɴҳҀԕ\x92ÄɪƕѮ˱әʓŜԨӳ(kΘΫѶØȜ',
                    'target_id': ';]ͷӡԂЮƢĮˊǐҀČ%ʬΈǢӰӳħüȏVƣǛ,ʮ$ГŹв',
                    'parameters': [
                            {
                                        'key': 'ӥЃӖІÉҫŰҩɀżʔПʡГ˕Ɖ.ŘωȴǥłRΕҋÝÕAȅ˭',
                                        'description': 'θН8҈ЗδŢûϜ˱ŉҫÏËƫQĆѾū˃ԮǪԔǟÏƒǍԮϤģ',
                                        'default_value': 'ˀȝсŜż\x98Ш&ʢƻѕћԞҐсŦʍќđҤ˺@ςшԇ˴чĤǧe',
                                    },
                            {
                                        'key': 'ɵ·ɗǃБΙġŤƚŸɖ͵żûǓŬϮ&ɮ³F΅ſϧWԌ˯ɿ˘ʔ',
                                        'description': 'ͲĔùŶǗÆȱ>.ǥʺԬð!ªѤțɵуīΈĆ\x8aʗ²ҼʛҐļЎ',
                                        'default_value': 'ƈɅŨԅыƔƚϔʮǺɋ\x84ҷx%η¾ЇǐŭӅɴ°ӪЎ_ӫȸˡð',
                                    },
                            {
                                        'key': 'ˈƅЗ\u0378ýŢAǡ3\x9fԗɌ',
                                        'description': 'И҉űŬ˝GҟƴѯŜ˨ìЎÃȈ£ǿλƲʨ;ƜЂŮбǾҶĴǸʫ',
                                        'default_value': 'ΒňʜÚwʌѐȳƂžӇϘțy\x98ȡ¬ґƉɁɜѹ>˸\xadƒӍԗāƨ',
                                    },
                            {
                                        'key': 'ϐʔƍěТΛϟӥ\x84êа˧ʗʟÖˀăǃͷѿɽӤɪѩǪПζѢǹ˶',
                                        'description': 'ƕĻȐʼaōǩУԣłʯӂәǠ´χǔÒҽ$ϊgǠ˷ӷΝȌĶϐԕ',
                                        'default_value': 'νΧӭ²\xa0ӚёǅЩȨ˃ÔгʖҸǠωĮ°\u038dϰҚҬÒȏvǗΧȠɀ',
                                    },
                            {
                                        'key': 'мüɤȸ\x91җŉÞl',
                                        'description': 'џә\x92˒ɊрŴȭɇηϵάѤǡƦbȩ°ǩӒȼȇĤ˒ːʏñΆţԮ',
                                        'default_value': 'Ǵ³ŞqǛΥáʝџ΄ĩʮϒɾӁfɮѯԊÒыΕʵϛҿѩĿ¾Ĝȯ',
                                    },
                            {
                                        'key': 'ҟʡԑǙ\x9aР\u0382ȓɃŀÔқʨƸǭǃ1˄ЃӄǯϼοʐѦ҃ǅϽԪʠ',
                                        'description': 'ÌϤɮ˛˰ġʍŕӪpǜʴњӿȮӢӜϿËƎ˟D˲ǞϤхҿȕŦɚ',
                                        'default_value': 'ƭƶ\x7f°ʚӯʨȕ°ӮѻƳӷҨʴŗ\x84ӷΎәҳ\x9fưπşӥbΆϴΰ',
                                    },
                            {
                                        'key': 'βÅɁβ\u0379ċÎρ3Ƿ:ѻҢƯԁȥƿ\x83ЇĐʈӶǐӻ\x94ɰİґӓ3',
                                        'description': 'ΡːпϯɹǊҍ˵˔Ә\x8e˼Ťɪ\x90ŕƦɮɛӾШҬʱm҆ҙƷŋʕǇ',
                                        'default_value': 'ɮΒĠȋLĎɈȢƐS˃ͳw°ӞɐVɪυίͼѦPѽԞĴϒʜщĉ',
                                    },
                            {
                                        'key': 'ȒӹøïК[ӮҩǘƧԢŜҽǮɏʺҔȌԇ\u038bƯнс¼Ѣ\x8fƽÕ˰˻',
                                        'description': '˅ðȜАҢ҉Ƽɚȡΰԕ˰ҽɣ¹ǼdɈӂΗєͰ˜ȹŌ˱ǸŸ˞Ø',
                                        'default_value': 'ӫEԄԘMϩӶƃȲҵʗɅӁìҵ\u0380Ƌ\u0380ʵωœțɮ˶ԑ½ǪвӒŖ',
                                    },
                            {
                                        'key': 'ȵHǈÃԈĘѣӆϲæǒʄɚĮȕӆȃďЀάÔӀҿÀκӹɝşɪɬ',
                                        'description': 'Řлύ½ǺАŷlͺřρʹКʿˉʸȑҰ˟ζɬªЇȒſӨӦ\x98ƑǴ',
                                        'default_value': 'ȰǝƮӕʔͳŎΈˬʎ¥MŜҴЉ;нȶԥЧχќͽʱԜʰΉ\x9aʯѯ',
                                    },
                            {
                                        'key': 'θ«\u038dђƣɂǈѕέ˦ˌўǨɝɶϷǱͳÎŴʾӅњɏˁġϏˑȑɳ',
                                        'description': 'ӆΈÖįɒȺʟѡ£ͶēѣǊ5ɝmϲƼЂϢ´ƽĶſyӄÜĝщѭ',
                                        'default_value': 'Ҵθ´ŝáXƬËnϰǞіÅ·ϚhɗЮђŹȏ|ЄşŲҹӛǹчɏ',
                                    },
                        ],
                },
                {
                    'name': 'ėʣÀʤ\x80ŹиθҰҪϧшƳȼĶ¤Жµвώ»¦ѦӈκгƐЧɚļ',
                    'description': 'ȐУίбЕȹƪŐʍϾƹɴ\x90άƀɂįбӋӫĎŴ3ŤӧѼ¶1еӓ',
                    'target_id': 'ƮFdǋ\u038dɘԐñ3xȺóȬʥӐłʧЌӱ\xa0ɊτĭΜǯÂѯȥԇǥ',
                    'parameters': [
                            {
                                        'key': 'ӵīԡхǳȦќɒɱɺ\x8eЕ\x97Ê',
                                        'description': 'ɝ҄˩λơˍєůѷʮŪǹŬԑĢ\x83Ŕǣʐ¼Ʀȫɂќ˂ɘtҏίГ',
                                        'default_value': 'ҪϧǔҵаЩлƟȟ)ӼŖЫҥȉҫϳĚǣʠ¶ĒѩÆϵɎӻ΄\x92ϕ',
                                    },
                            {
                                        'key': 'Ѱϛԭ¬˧ðǼҾ˞WɩǕͲԚөp³Ӛ¸ΌЮƬӁΈЪƎ£ҋҘЅ',
                                        'description': 'ƞ\x87ӻºҁўГįУќĦƎOӝϻϏ\xadνº¹ӵˍѬһǯˁԣɳϥė',
                                        'default_value': 'ԧωŠʬŏɿ2ӠСǁҴԤɎłʒɠʙǱЄ\x9dˡȘʞǪϤ\u038bЬӟǧù',
                                    },
                            {
                                        'key': 'ʶόśɏÛкͷБӏˇpԬ\x8bǠоӈϦ˟пП\x8f2˂ˏƒȑ\x84ŀ`ȝ',
                                        'description': 'ĢӮĬ·\x90˲ӞԐƚˆҲҟɰOЪϟǩȊÞмҀЯԁĀϫъǫʦ˵Ҿ',
                                        'default_value': ';ŗȉĵˣҠԞćԧҭйřϵȏΓȑĶѱѺԚψ\x80ӴƶˠηǤЁ*\x85',
                                    },
                            {
                                        'key': 'ӵÃƍФRˑːͻӄέ\x82=ƎҏкIŬÕ˷Þ$ЮцԞşĀɬ\x8dӅÝ',
                                        'description': 'ϨʞΩсŘϜĺˆƢPљĶφԬǧʰĐBɩшь҂GɻѪ$ԏäĬҶ',
                                        'default_value': 'ɌCӴкɉΖőȒΝĳ0Ͼ',
                                    },
                            {
                                        'key': 'ÝϬ°ҳLƝӶĞǋòȘ',
                                        'description': 'ĲΐϹĿɐóкдΊ˖ϩЄ\x97ИШDƖǆĨҵƮфɉnЈͱG˱Ϭ³',
                                        'default_value': 'ԒʏʕҺöɦƋàѿɳ£ǼɄώŘѠOҼχН˷Ӆˆ˾ӖӁͲˀʹӿ',
                                    },
                            {
                                        'key': 'ğЭω҄Ć»2',
                                        'description': 'ԄūkЇʆʔϖǣѬȺќӟԇʅӑˮҀϒγÍơǀŤΣoūΊÊÝÇ',
                                        'default_value': 'ғʲӠīͽсφîƙƠѱӽҴʒ\x8bԣӨlgŹԢ\x9dˬŨϭ4ʊҐǎΌ',
                                    },
                            {
                                        'key': 'ԜέТπѬ\x9dǠԜϪʆûѰ%ɐєɋ](˷҄ǆҒ\x9dƼԂͼϋǪӰÓ',
                                        'description': 'Ňɹџţ\x9c¯Ċºȉ·¹ң\x8dԧ˴ŔѺԡʽlìѸӚϷӶćԞԧƆɢ',
                                        'default_value': '7ɺѹūνУӦƉǝ ГΞŎıɂˉѢӘδҍ˃ʿӈ$ӑ˪ЗÅ¶Ԭ',
                                    },
                            {
                                        'key': 'úø\x95¸ʦ˴ÑəѠӾɚȚƴν;ΰţжϊ#ǵ\\ĐżHҳʇǟŝB',
                                        'description': 'ǎʔ°ƋƜϫӗËĭҞХȧЉԫºǾʏѫΧɄǞЋӇĴε\u038bӌԧÈԑ',
                                        'default_value': 'ůʌ˳Ө˃ѲѡƔżћйxƙӒΗ˷ŬԌJɹóԕƾ&ȈƼǾҫϖ\x89',
                                    },
                            {
                                        'key': 'ʪҝΞĸԄҏ˩ϙ˥ūªʼdӶјоԅԠɑӂmÀQӮǕОɜCҸƩ',
                                        'description': '\xa0ԅϨ˗ΏœͿяӳѓџłԡɨɡЗĒĪΩȒ˩ӻųʏʠŜ\x9aȤ#ϼ',
                                        'default_value': 'ЄƲԊĹ»ќ9ɠȍԂłƨν\x93уϷϹɟҿӧŮҕϦÿ˕ȲĳŐˍʋ',
                                    },
                            {
                                        'key': 'ҤȟӾš«ѢWЧӗ˼Ũ\u038bмҀ\x90ӔřөτMҺȞč¸Ӥč˶ӟѲϥ',
                                        'description': 'МСɴѴyʍɤҷΒŮΙǩŸ<ɅȰ`ʌЭƀҸĺ¦ҴӻʰΔϤʻǩ',
                                        'default_value': 'ɻΨȔ\x8cʁ˙мƿøЬ\x8fԙ7œőǇǂͰҭКҹʓLнԁʈǂ\u0383ҥˣ',
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
