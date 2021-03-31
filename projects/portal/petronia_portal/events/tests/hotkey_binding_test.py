# GENERATED CODE - DO NOT MODIFY

"""
Tests for the hotkey_binding module.
Extension petronia.core.api.hotkey_binding, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
                '˹ɡē',
                'ʹʣѰƇ˙\u0382ŉѓΰɼDDɨ',
                'ЄȦΡƄͳљĶтҟςˍ',
                'ӴϚĐØƖӻѭҫԔɕȟӉʮͰӼɄƼƟωĬЛƛǓ',
                'ˮÍпήϊҬİϾÓ',
                'ȢӨÿ\x7fʌĲżȢǷҚүvˁϑƣӆ ѡК϶ΑƲԖ\\ˏ¹Н˓\x89',
                'ñ8¼°ӗ˚)ůϬǵ˒ǻĺ\x95ƪδԠɌИӯ˞ŭԣ',
                'ӏǂκӐҒѶԥȬі',
                'ўˬʼԧԍ/ҠƒʧåϤϊȊ/іϘʎӣɽѻŏһʓȮҤØ',
                'ıŔŇȻԞȯ҇˗оŎːǃƮƛѦԣǁƀğβДϗǑ',
            ],
            'comment': 'ȅçԄʺŬŜ¯˂χĹʌƶςǂΉąԓĽόНϻԖǿĚ˔Қϣ\x9aˣӦ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'keys': [
                'ɭ',
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
            'key': 'ҝƷάѴіŜѯдԇԫ©ǰɉʲԚӊ˸Ҷūʠ\x86Xμȓʖ¡Ćөҝ6',
            'value': 'ĄūƅϚÞőӚÁɮ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ɰ',

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
            'target_id': 'ɂ\u038dÚʧ\x8bΏѷŵȱѱāƆɅ¢\u038dǢИҠȤԊđϥϥǸĢŻè\x89ζɘ',
            'parameters': [
                {
                    'key': 'ҪȮǪѥůurǢѬ<ŧͼqǯЁ',
                    'value': 'ŻţʐːˀΑ¦ƭȆ˞ǰŌʖWaȁ˼фw˽nшĮҍѶȦŊљȰӚ',
                },
                {
                    'key': 'Ϻų˙Í¡ʃĦéơʡϊОúƎΓΏXϮӣ3ǈɋfcвʒёȆ΅E',
                    'value': 'ζ˝A\x8c¨œ+¢˹ҍɤƢĜ¥Ɋ\x9cǡjŵȧͰҵҋѾӐщіЎύϥ',
                },
                {
                    'key': 'ґÊāћ˄ţЅϣӝαÝˡø\x85ҮċǤǼ\x80ɉƒͿɤʉüŐ΄ăƜї',
                    'value': 'ɩU´ӹЖϛΛѰʬǉǜŚҡϵʋŏЁÀĺɲʂˣĈҐѿø˂Õºʝ',
                },
                {
                    'key': 'ȦϼѲ˄ҺӑƭΫӴʁɼøıɪȮαҪԟАȤҌčʸАІǕÒ˽ɨα',
                    'value': '¤Ӝʈԫǵ˂¯ΝǼҋÈԜҿϸ8ӎ«·ĐΛà·έѻš)ȵԨVĘ',
                },
                {
                    'key': 'ɥƱϮʔкɛ˼ˡ\u0380ȟЪěȴԟ˜0ʨǍªÉМѥԓϐĠƆƘ\x84\x88Φ',
                    'value': 'ȑȯɱԢҐ¶ƓſӅɍ©ƶΰʀяԬʹğҘʄ˦Ҕʍņ4Ĕʚ҃½t',
                },
                {
                    'key': 'ϐʎԩзԟÙ˥ǩπоưϨĹʨβµĳë',
                    'value': 'ʁѧĭɓ\x83ǩǏѪЈӼƛ˺ҖŷʶÍʉͺɿϻӿçżȀӡ˶ɡˮѽщ',
                },
                {
                    'key': 'σƋűȼǁӂĢ&ƴόȃǟɼæ÷σӢʈǆ\x9dѼĮĺќ¶μ˲0ƁͶ',
                    'value': 'ԊDπ_Ø˗ϸƬɻĨθìÑϴ\x99ƚˎĬѸʐуԦɽҲŁƭͰӞԟ¨',
                },
                {
                    'key': 'ԌŮԥ<ΞɞɯѐɕʪƦɄҵƆƐ?ˏɬřĚǿʦӚǛє\x8cЬ˖ұŊ',
                    'value': 'ȒЧȻёұů\xadbϯǆˢȁΚųȇαͷˣӬÞuϾǁ©KȑŝЕÁŐ',
                },
                {
                    'key': '?«ǇҸѕī˔ʢɦ+uѮȚϟʍɐĿΒȉũӎǓҿѯѸčKҤҋB',
                    'value': "ʻϕÞƻŹvøɉƶˬxřƨѯ'ƯȧҞƸԐúǬў\x91¼ѧʯɎŝ΅",
                },
                {
                    'key': '˃ƬƧțӤɘұŎĥԋ·ǗĎɎΕʍİЇǼȃǎɰуȴβɶʏõ~Ƅ',
                    'value': 'ΐͲҫĘ\x95jŇ˞ӀӝĤҞҹʸԢӖAǣФƆйõƞʌΰVƴĝςӝ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': '=Jљǔƽ',

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
                'ѠϽѮĤӁϦȮҠĂϕčǮɘƆ',
                'ʐǔˢ¹ƑșМԝӷǚɾȝΦïӃɐћƱ±ĩ˟ǭ',
                'ȇ:ϔ;ρǡԑӉ\u0379żΙԖŤŹȺԮΕˁκ¤ģϙƏз',
                'ԧϙʸűƣʒМJÑнǞǫː',
                'əÚκɊҔϋȀľ˚Н˙ЕĕƮзǽďȎΜ',
                'Ĕϕ\u038dҍSпǅĤŃɄȺǱѤѕύώҋɎ',
                'ǁӮΔˈӤƉȪȝ·',
                'ĤǄΗËªåʎɗȰ\u0379\u0379ſϔrʝƀʮØοg',
                'ͺђ˝ФǙƽĸ',
                'ǻ£˔UаʃÄŇҚ',
            ],
            'comment': 'ƦÏҝȾǆũǏʚǄóˤтϭъƕ;ǊЊǣȵ҅ʁz\x93ѷĘΔӘːϡ',
            'event': {
                'target_id': 'ǇǴįΰѰ҄ŨӿѴӝѹĕɤ¿³àƮśԩйД\x83ʾŜ2βʦãƅӥ',
                'parameters': [
                    {
                            'key': 'ʞȣØĐćąʄʦϙуʳǋϺʭԋ\xadλȖǩʆɣcɺ\x93Ђȩԩϩ¹Π',
                            'value': 'ʓғӳǬπЙ*˼ˁĚΪԎɧҦȳèń˛Ź˟ˡǎ϶/ˋΩϴƮĈԘ',
                        },
                    {
                            'key': 'ʲ˔aȴԟ϶ȀϢŇnѠ˒вȗԗȓȭҼsxьȨї×ɗʼҒƸ',
                            'value': '\x99ǋ\x8eЉƽŠɜîǆǸϓЅХǁǆӹͶʹÆȭǂȇЛθҶϚŲʯƆê',
                        },
                    {
                            'key': 'ё<ĈʹƶǕôȲĳµДfЫRӻϰľƷıʰπĂVԡȉĨòήϞ6',
                            'value': 'ƪџѢͱԌxʙӀ҄ϟ£ɒϫʤӐðƐċ϶Ԝԇô2ťӯϟčſΖʖ',
                        },
                    {
                            'key': 'ȤΩѺɧÈȐɳ˺ŦȋǧȓC ΑŤԅcίӂӡɪͷԬ1ŒɎˍѾΝ',
                            'value': 'ŦӛΤҘп҈šˀАαȝʐŒøŠҕƷҟɵ+ѪҪźӛφŮљ|ǁƽ',
                        },
                    {
                            'key': 'ҵȘϡɱĎ˂ϲςϣ[ȹԕǵ`ӃǓÁWűêю˞ϩưЄΡƏҋƄȧ',
                            'value': 'Ԣӹӳ`АɝÌԭ\x95ʬș˞ƸԟQDӉɖ˲ÖҘǉŅҴÞĴő˂ˣΙ',
                        },
                    {
                            'key': 'ɮƠȿŷ˻ҴЈŇ҆qқϊԏGċ?¤óԂҏȓɋĊц˵˴ŃÕÍƑ',
                            'value': 'ϐʻɓӊѐƶԞʪ«ȪŷʸrЌӦ˛҂Ѿ°ġ˖ǖҎ\x8c҆ʈǭľÆӱ',
                        },
                    {
                            'key': 'ԩòԝӓƅѺ˃͵ăɺĲɵ®ʈǤúӋȠƁрӔǊǟˢŐԕӓʹΫӺ',
                            'value': '҂ğɩKӔǒԗѻӋřϭÄ\x8bѾǡƁúѕӘˇƖʰ§ϽӍʥҗŀӏƊ',
                        },
                    {
                            'key': 'ɼʟȣ\x80ԔƝѣЇɨΧӰӁƖ¨ΗËӨʇԟѴƬ˃âƪ-\u0382ώ`ѽȎ',
                            'value': 'ԉĀ΄OơǄѭϒτƀIӾԊ\x96ĖÞҬϖμŢ¹0ϖͳſĊµĞӾԊ',
                        },
                    {
                            'key': 'êȞљюρ\x93.ˡ\x8fĵϭƽЁĜɺʘзĬǻĜÞĎϕΏ{ϬюҨЙϑ',
                            'value': 'ΣıMӢԛҥʑǩƟüҢĬЌʉ£ȒǜУʐJжǮΏϴŵʰʯŬ\x99҂',
                        },
                    {
                            'key': 'ɏΗǷή˧ŧΜêŐǠÛб\x9cӿυŏϾҢǚѡҴŞ\x9dƟŽŷӄ\x9cƪ(',
                            'value': '˗ˀѩ\x9d',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ȴ',
            ],

            'event': {
                'target_id': 'ͲKԔŬб',
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
                'ɷӆӵιӓɆʀUΘԐҘʃĆɎʹʞȥϤȶɺ',
                'űϴёЋъ',
                'aԥÝʔ˒ӧˣʨϥʉ΅',
                'ͺӢʳƭƗ',
                'Яǡ\x84Ĭǲ\x9dĮöԤ~ȾԜχ',
                'ҍԛ\x84ŀņńĀȡɛƔрɄӣ',
                '˧ίǆʓ(ɻʓЍѦɭ¡ϡ\x92ɣʷπ',
                'ͰОȈǘŪŠӰ˛æ҂',
                'Э',
                'ƺɧɍтͶɇũѣȺưĄŔ¢дϙ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'à',
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
            'key': 'ɈĨɻѵτэˆέwοǵ˜ԡԣÊǺɺɐďӺΑɿˉɐÓɆѱɛ{ʝ',
            'description': 'ңс\x80ʑͻЈ˂ԩԖŕѨҐDɞΌͱΊCˣſ˫ɢΞŮƸ*ԟѺѩǮ',
            'default_value': 'ƚȨɝʷŷӳĬȕǃŹЄЪ/Wғɰ*ƴұҺ¤кĒƏĀ87ԝƂż',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ā',

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
            'name': '˥н^ǟЖІ!ĪҪӥʡȿɞȲˆ`ҝöȐǖǾέПüвҧǊ¡Ɇ\x83',
            'description': '˟ÓίȰǘĹʂŴóήǴOӋÅԩш[ԓ˵ǕɸҒϙ˟ʦTџ²Ӗ\x91',
            'target_id': 'ϻӷʡѳϽOҾĘʓ˛"˭ʫƈћŜɕҳ\x90ª\x7fʏҶǎцїƓѣŅɭ',
            'parameters': [
                {
                    'key': 'ΦщȯɃԒŭŗѦѱжƬͱƁȴKԍǺ',
                    'description': '\x9daЭȈƍʼ\x9aōůǓĠtϾ\x9dόΖɻőӾξіԅЋȺԛϣ4ьÅ\x92',
                    'default_value': 'ƿԚşŉʊȀӟӧƈϺӄѼυԪȇUȨÙrƝƛϕȇƑÆÝºćĆϧ',
                },
                {
                    'key': 'ËðȤĻ¹МϊÍƲůMĢǷ|½Вί1\x8dɊ]ЖÕîһ˖ѽӳØй',
                    'description': 'p˽ακԁ˝ŮƸ¤ξЮɸ3χΚȑϢƸȑ`νʡìƺҕбԥ3Ԝɦ',
                    'default_value': 'șƳΏǞǓΞ϶ЛˌӡéәŬӽԒ\x8eʂA\x9bɿˀǥɷʚѻdˌǥȭΖ',
                },
                {
                    'key': 'ćЌîӇĻţԔȒèǂǑʔюxˑ©ӱɸÐŸfʏԊǫԫ˹ʳ/Ӕ҂',
                    'description': 'Ԉ\u0383њ ОΔKʙӡИ®ȺĆɽċѱωĵöʍƴӫŵÇʂʁҴűӺō',
                    'default_value': 'Ѿ}ӑѝјȆ®ӆp\x97ӨrЊȽxКҬλƞőǒюšʽˑǮɇƤЍ\x86',
                },
                {
                    'key': 'јϯĝФǳǿ¬Ō҈Xԥɶоˍș\x80ͷЍú˨Ƌҵ',
                    'description': 'ëĳÂ½ğÈѩɪóϵԑâűȤσп\x93åjtΒ1Ќ\x89ԗѯŦBϷɊ',
                    'default_value': 'ԤҨϊԬљǺğźлԧźŴʌºɒьŞϥ¯ЀǴМїȌ˯ƽƓѵʵϲ',
                },
                {
                    'key': '\x87Æ\x82ŘаĢӰǌǔϋҰǱǆшҶΜęǙΙǊӘ¸L˂ɍ˂ѣƇԚҁ',
                    'description': 'ОłˡѥԚʇІɌůВȪӏЫ\u038bΩӬїϼ˓ķÖ˙ʈԟӈŕ¼ɵͻ½',
                    'default_value': 'fк˝ӣ\xa0ԓҷԦɽʙξχԞįЦ¾ɀѪʫιЫυǨȒύэƣϫçΎ',
                },
                {
                    'key': '˹ȓmgӼʼĄ˲ɳ;ќȴȦƨьȏŘқя°ǣδӶϙɢĵ÷ѿɭɖ',
                    'description': 'ƉҗӦˡ[ǅеšмӼΘ^Щò£ԥƺȦǬǉǊЕлƴ˒ǈǀ0ԩԪ',
                    'default_value': 'τ£\x7fŌ\x82ǭƻŠԂχтӴƀϵ\u0380ɰҎȞʮßǰZŊɬɈӄʐ˭\u03a2ə',
                },
                {
                    'key': 'ˎďÌѦѦʣʮЎЧЈҸ®ғϭþФHԚŢʥ!ɠ\x92',
                    'description': 'Ǻʽɟӟ˪åοǌ\u038díθȢԂІʚ¾˷˽ԁá\\ȽѤÔħұ\x94ƧʩϘ',
                    'default_value': 'ˡƪǩ(ÞӤϢ҄҃ϦʰǗѬʔİгȤĹǉəϙ´ıYƋʰˬ˽Ѕ\x9b',
                },
                {
                    'key': 'ϳźϑ',
                    'description': 'CѠОîωǷXơԛǡлɨ.қʸԆҀʹ]eϑӭǊǷȱ\x91җөȦѠ',
                    'default_value': 'ƈüχƺÍ3\u038bѴʔSÌΉ\x9dϡċ˴\u0383ǝѿwβΫҘҥѹς\x97şȖŽ',
                },
                {
                    'key': 'ђǽȢ»΅ԀsɆȢǻʟÂȕFô[ŦʮɞʂӖ$ĩаĐíˌ÷ˋɳ',
                    'description': 'Ǳ#şɺľŶ˟¡ʋʚȧĝŦȧ҇ӟˌғƿǃ˲ǖńʑΎƊĲƶѴǾ',
                    'default_value': 'ŶРđ˼ĴʙåӉÏ˾ѻŷҦПчȀmɾ˗ɾϽŦvԬƫХȾюƏЫ',
                },
                {
                    'key': 'ϿЛЄʡȦc³цĄůԉѝ¹ˠÀμѯŦȊɇƹĪйʡșˇғӂȳϞ',
                    'description': 'ȰƱιÂӪņԤʛиԑΧѧâOŷϾæaԀǣΥƬΙЕŘ˰Ԛy2\x9d',
                    'default_value': 'иȊǤUΣпˎÄ˂υюĸǸžΌ/ԨԝзЊвÙҧȌƯĭȕǊɲˍ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'PљE',

            'target_id': 'nϧĩƤǛ',

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
                'target_id': 'ǢΠЋʥ҄қŧ˦˞ǵºńұӨАɪ˞ɑùӍТʢμԋѫŁʾơγͲ',
                'parameters': [
                    {
                            'key': 'ӓЎ˰\u038b\x9fјȶУɘ˧ўƂĠš«ŎÝ»РҢБҕǯɞӇąĮκ͵З',
                            'value': "ϒƉƞOҕƗȘˀȠпkϪʏŔΩΧŔϟĬԌŦBО'ƆɛğϷԋ/",
                        },
                    {
                            'key': 'Дʆªɓњɣԩϑԑ7ԥƽĂ)\u0380Ԩɦ}\x80хөďτž¤*ξԅѩǹ',
                            'value': 'ȱſɂɽԋǻŁϊƇsYӣBȡԁƶҼʔӒɈ<Ѝ˛аɂ˱ΑƋ˦ӵ',
                        },
                    {
                            'key': 'ͳʢҶȪ˓ʊЎҩοҏËɌεҋƁ¹χ˓¨\x8aщӍyҢ/ſΥ-ѷм',
                            'value': 'ϵȨѲĻԥәηԥzåӣʺάъϨκӦ˅Ð}Ҙ˃ȡɷ±ʹȈʶͺŉ',
                        },
                    {
                            'key': 'ϮıĔÉџǌӶѨÞǘÑЫѱЌ¸ɋ\x8bȵ҇bŠƮӚ´Σİ˞QIƙ',
                            'value': 'ǽÝɸʵ\x97ԘĶθ˫жѵѽǌϰ˺ǂìŘˋηфЌάŭЂÂϳӉʓă',
                        },
                    {
                            'key': 'ΒгƇȋ¬ļԏɣȲԎԍ˕\x8cƎӎʹŀȫ',
                            'value': 'į΄ɶӓɮѱΣя˞şνƵҖÁǃĘԉʨˑȲ+͵bƽƞĔʍǤҖĐ',
                        },
                    {
                            'key': 'ƣӈ\x8dĽѝҐYǶZ¤Ҍƶȸ˔ćɏяƍϺ˫Ӝјæȫϰ',
                            'value': 'Ȫ˃ǯ\u0381κɛһŬҴӄȿ¶ø\x83āЁĸцԪԨ\x89ϟȞv¯ȍ΄ǛȌƿ',
                        },
                    {
                            'key': 'ɑ˧ʺƷʌMƭău˟ĂЖϢƇʶқ²Ĕ\u03a2ÈƚмϿѾŵѧȢřƵý',
                            'value': 'ĆќʲèʊзŘҗ҇ȯoȱ˓ҧ÷ĳʔJΰѶŊŮŏĕ3Ί|ùɑҕ',
                        },
                    {
                            'key': 'K\xa0πůÔǫ҈ЧōķҪТғǴԆ˳ώėҩKӋЫԨ9ЯϷĎˌʯΕ',
                            'value': 'кΞґЂJı¨ƮƶŸǺѧ5ԁȤң¿ғȡԑǒ´ǊÂęƕƯƇМx',
                        },
                    {
                            'key': 'αGÓȽǢ',
                            'value': 'Ӭжȧ\x88Ӣd˭ӮЀҦϳ&ӿԃѡԌʆĐǯПҡɟҼѩұʔԬ҉zӼ',
                        },
                    {
                            'key': 'ǲ)yďƥ+ћʲͲʯҧƼʚԜЅҳ#ǇĖ4ĨҴ ɪ0¨ϖƒԦÊ',
                            'value': 'ǯğɽӷԟŪ!Ϸ6ΫȂŤԏƣ˹ȸèoǎɔƉ˖·˥řǲ˒ύˣk',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'ҿԉʯȾȏ',
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
                'řѨϳȄЦ˪ɝˮұƌԉҒƥɸî˃ԚϭӢ\x9d˓þʩȲˎ',
                'ҞҟȒƗȢųȩȼɤҷφȋʗɟÖшϷēѩΞӍӵӘ¯=ɛĺ',
                'ѝϺÏ',
                'ǯӜӁvұҿϟǂɖ=uĢɴǚ©\x88\u03a2҇@ҫ',
                'ІȶҧԛdΚɺ',
                'Й\x9bйɜƌƞ',
                'ǣ¾jЯˤ\xa0ƩĀħжК',
                '˗Ǹ\x9fӏˊ\x9bğ3ʲԋ¸,˥dƉǖʇϋǏԣOҜ',
                'ƺѴŞñųʕҰƫσ½ĺĬ4ΉʔАRǎϜœΨnϦďԛ',
                'ԠƁX×ӈҡȲΟϖȋjөˠҎΜф\x8fг',
            ],
            'event': {
                'target_id': 'ɣΡȆ΄ʣȒс˯αǋпǽˡ˯ѕqӍϹӀƹʟcìϋľ~ƯÝԨђ',
                'parameters': [
                    {
                            'key': 'ƵΔѺ',
                            'value': 'ȂŉǵƋÆʌʪ~ZǃĉʠƓƐƔԬÞȓґYΛźǎˁČСҙ˲ҿȆ',
                        },
                    {
                            'key': '˒¤ĽȗΓȣ@üʫʾˠҖľф×ѰöӓϐÁȶƞΤʄ˗Ά\x88ŝƏɒ',
                            'value': 'өÍɅΗ Ϫ˻ԝҝЋęɡƍˉѩăɄ˞ąϥɫяĚÅ\\ƅÒӆźΓ',
                        },
                    {
                            'key': 'ԇҤʹԇ˗\xa0ƄҙЇҰŞ¢Ͳɫ¹˗àЙĝҪǟӔйÏīӨҖ˰Ĉй',
                            'value': 'ȺˑēƟµȠ÷Ԑ\x9aéPʿӧīd÷p΅ʒӧčδӹ\u0380σĬ=ǗĺƊ',
                        },
                    {
                            'key': '3d»ĥЁϓѼɍ{\x8c˷¡ʦĚƚʀљМŐʇ˲ǒРГĨӽȢԊVƾ',
                            'value': 'UóäŒϘ÷ϋʕ\x8bχЀДʥŷ\u0379ˮчόļҙѵ\x96ΞŶԌч¬ʻѯЪ',
                        },
                    {
                            'key': 'ёfԅŻϮčɾɕŉ¼ҌҿԢÑ΅\x94ƀXӾɒЊ\x95ʐԓҟŻ%ͻ«Ť',
                            'value': 'îËХ+5ÓˁԈΧðȺɘ\x83ӫƐıĠŀɳϴѭǹɏ҂ъŮɢːРЌ',
                        },
                    {
                            'key': 'ǧӏɂӈφξ9ÜѿɔƈԬýӯҴϽɃȾǷĮ\u038b-ԫɥЯĪ\x93Ř¨Ԣ',
                            'value': 'Σ¥ϧýҤ½ҸjΌϴ\xadϫŸŪǝΝŭ-ӈƺȰĬ]ƞ˰ǌπҟʂˠ',
                        },
                    {
                            'key': 'zϒ\x93ӘҸЙÆʒ\x92ϲǿÇǹ҇ŉРԉˡ',
                            'value': 'ŦΚϡƄϮÃŦӏĤɟțʋɮӆǔр¿ŸÆ>˾ԭө΄љџʅѹѥƉ',
                        },
                    {
                            'key': 'Ԕж˶ԢȚ\x89ǔѫǛĴӸс·NȋƐ˴hΗÈ>ϸʍ#ԤĄɪąӏϹ',
                            'value': 'ΝȸҘ^ɀлbɜҘąҌȰɒјdŸ`ӊΩźϟәƗчôӕ\x8e˼ťʥ',
                        },
                    {
                            'key': '®ԓɵКƿ>ŰŮѺ}ӏδНúϘǮϪ7ǽȳӚҴˇѶЊÉӏʾҌʜ',
                            'value': 'ʂʟԏŚиΡԮѡdΑ\x82ѴǮϛҢҟʄ~Ž¦ҰΜƛѤͱѩӝʝƀǜ',
                        },
                    {
                            'key': 'ϸ~҃ʏǅɵǎóưàėɑÉǚâtȿ\x87ӆҽϷεĹЂę·ҊѭŐǻ',
                            'value': 'ҁЕ\x85ʹЛ˅Ӵԍˉ˛˵ŉҸϧ˖ÈʿΉʎӫӀФԞѨʒ]ΈӎСǡ',
                        },
                ],
            },
            'comment': 'g˛úȟЛΒѮ·ˎЏς˞ёφԀqίėǡvÁӀɄƬңҷέĵ?ɋ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ő',
            ],

            'event': {
                'target_id': 'êƶɽjâ',
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
                'ʙIƇğƸԊ҈ʒ˓ҐѱOƜ',
                'ʀƀ¥ѫӻ\x8dćĜǺͳƨ',
                'ϷѣſôһЩƿŶƶҦ\x82ăşÓ˹Ĉ',
                'ǱϽϙ\x99Ԩΐ',
                'Ԇӈ;ӚĶѡŐY)ТɝԫԏЄŅѤƛЪњѺɤ',
                'j°þ˴§ӫͻɡŢĭӶĠǍєʉ',
                'ɕɦӲ',
                'ƈ\xa0ɍȘʠ˰Ϸ',
                'ҌьWϞәŲŉdѠȖ',
                'ͼ˅Ģ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ӨāЫэԊύǸ',
                            'ÙðĵӆɹÀȡ$ƁϏч˟ϟÍӭ¥ɝǗŰͰΗÊ¬ȒҜцˤ',
                            'ń×țM*ҎԬÏʅŠʲGǼӈӶХȠԈʩǦмʝԭ',
                            'ȼDӁãӯĬâoˤßуҸķřУΚйԒ®Ӯ7ŃȷʜíҖφ',
                            'Ї',
                            'ǃҜΥ>ѲȿȊa˔Äǖ˞ƺȭãyГóśëԧєVϑƚ',
                            'Ͻ҇ρԐėѦЉΗɸԖȋũģЁʛ',
                        ],
                    'event': {
                            'target_id': 'Ŏ˦хҨԊqĪçͷҕʘйʝӮϣkEаˡ\x84ҦǜʪҌĂԀϘοȾÈ',
                            'parameters': [
                                        {
                                                        'key': 'ŝõćҞџiпȷѱƓ˛bʫɀĞȈҪҖѸċǿȰέ\x9c˅MјȄѥu',
                                                        'value': 'cʌǥɩźҖЂ\x8fǡɌӡϝю»ӅϣԀɈåǬэΩȄȅӁNϷIďʽ',
                                                    },
                                        {
                                                        'key': 'ƣuƥèŕԮŔîϜÔ¼ǲӼϧʽћɮɢЁȭǟ˦ÂԮϮӝ¢Дɲк',
                                                        'value': 'νΙÄǫ(ŋĞ\x8eʝН3Ϙ\u0381ǺĦ\x84ӮҤɢԄ˰\x8aҭ$ʹȰxіҟÃ',
                                                    },
                                        {
                                                        'key': 'ǹϬ',
                                                        'value': 'ˁХƛҾʌΥǅ҇χıˮɳ~ѻĘӜȢ¢ǰ\x85\x99ѪȠӂÃ/ØЬnʉ',
                                                    },
                                        {
                                                        'key': 'єǁȒԘ¤з˂YÏĐʹΕӴҏʺЇƝɎ_Ȣԑ\x9c©һς\u0381ΏЖæʡ',
                                                        'value': '\xa0ӼɎͽˣ¯όƞҷÕҒŊŠ\x8dqɟą˹ƐӑΤϮȫlǩӆ»å7ʧ',
                                                    },
                                        {
                                                        'key': "Ǥ'ǿ˘һҺР˽МȳǭлŲȯЋѭʫӂɵƢʵӍɤ»ûјΘ",
                                                        'value': 'ʅăԫ´Ҍå\xadșº˗ќԡҕÉ\x8bЄӔÐԅ˨ÁǉȞɌѵӛȜ˾ǉӱ',
                                                    },
                                        {
                                                        'key': 'ɢ"°çѼȨϒŮɣʰрˆPǈԇӏѳʴϟʩ·ъ±·\u0383´Əʁɲ)',
                                                        'value': 'iѶĨHͻDļѤӥˢӡȟčɯԆȼԝыϩ¬ЧУʗǨϴě˯Ъˡð',
                                                    },
                                        {
                                                        'key': 'åЄǙӷӆ˰ȿӍǺˢѲӅǏŽԢȣǛЏȒzӬȢŸ˧ѴɕĕÎΚń',
                                                        'value': 'üԛΗ˼ɣ˅3κɰ˰ԑßµȁǝϠнȃɚȐη˹µҬϡȀһŅ˞҂',
                                                    },
                                        {
                                                        'key': 'ʓͽЂΠƣ\x89ŰӝăЇɪКѩɋɉ\x82ӨϷ',
                                                        'value': '·đ<˃ǯÉ˽ƃ˄˒¿˼;ǹưӌθˎŮћɻʹȔʧˍ\u038d¢èȄa',
                                                    },
                                        {
                                                        'key': 'ȄǲѮӃ<Ƒɪ´˝ӼɼƱ+ǥΑʼ±ԬǒdфѤЯĎѨԞԀҗ¿˧',
                                                        'value': 'ɅƓuŉĆJηųʛ˷×҄ȉʣӬуɩ\x91ɧШ&ͿϮӒ»ȂͿӏöɦ',
                                                    },
                                        {
                                                        'key': 'ҴԊ\x82Њ',
                                                        'value': '>aǎлñљѶˁҴʄƕņɖıӂƹȺʷƕȀȢѦħhĜÓ\x96Ԑˋȵ',
                                                    },
                                    ],
                        },
                    'comment': 'ѨͳԭªșԩҎƈ˅ȩѷšϴƨɅɮˏІΡ\x95\x91ҡƚЪʂƀԊ˛īȱ',
                },
                {
                    'keys': [
                            '£ˤԇɼɳƝцԃȄėϋѦçXkϼWƝԌ\x9eĔЍȫϿЙēӑʫƨш',
                            'ϷӺЩԈˉȌ¹-ͲǲѦ',
                            'ƂП{җƉфȬņϨ\x98ɬѸɾŎȒȹ',
                            'μӑѵͿÖʹЖůHӢ',
                            'һԨζЗΠ҇φɞ\x86ιϓȁЙʨдǔХ&ȳªлĴҖмC˭Ʌ\x9f',
                            'rΪƦΈүΩӠȰ˖ӁϓȠƌfїͽ\x99ϩМùƮεѧӓяȵΗ',
                            '˸ʣεƳoϗԏÔѰĚ\x9bϏŉɄӶĪ\x8fĹİǟӥİųЫ˧Ϡ˻ʸУr',
                            'wΞӦˁɉhŁRēţмƊųȊҶĆ]Ɗ ǔѰ',
                            'ēғ4ǻȏĖсЌҀβψΣʛʆƂʗʀԫēϓKƃΏ',
                            'νqɭ˓ƖŔùjςǁβʑčǱѹ',
                        ],
                    'event': {
                            'target_id': 'Ǭƾ§ȂѬđ˽ԢŜ΅ͰȭжϚԋԜžґĮыӽeŔɇaіˆɫûʉ',
                            'parameters': [
                                        {
                                                        'key': 'Ү˺ҢžˍK=ɶɑ\x87ǽǎІǒ[ʱǁү\x89O҆ƽʼɊсp"\u0378ȹτ',
                                                        'value': 'єΜ˙ҡǔșЮɦƍŁіԌ˒pːÑӦѢƚ$Ĵ\x8fŮRΫ\xa0ɝ\x9eǜю',
                                                    },
                                        {
                                                        'key': 'ҢDӷ¯!\\ӉӞƆԙʹʔρҾΙȞȇv"ŖɧЗĥŃǹм҇ѭʴǑ',
                                                        'value': 'өЉȏʺѰЄůѿϬςƋҝțʑŢǡ\u0383ȡЮєԧ͵GӢMʺΖѱЕҋ',
                                                    },
                                        {
                                                        'key': 'Åԓѓ\x98ʱåľÏɎǳǊʆͿ˝țȂІǕʢǕЅŀȞǍǚǚÜѢ\u0379ƪ',
                                                        'value': 'ҜɓȨÍͶНĄEĈȈȞΪϤǳəćšȌӋɥƓ_Ǌ҂Ӯ9ǗćӔN',
                                                    },
                                        {
                                                        'key': 'ʍɅŴЩщ\x87ſԏӵӤԩÄʈҺʝϏÅWЙ˃ѯ«Ĭ˸ȽV\x82ҋ®˒',
                                                        'value': 'ԅЛʘЋCδ˙\x98ԦгȵѽиԩҸØˮԦ.ЏӈԅǒV£ʆȥȢȤǒ',
                                                    },
                                        {
                                                        'key': 'Ʀȯ^Ț˸ѪʫʌǒӪʓкƣmпƠӹʵȾʛÛ¼ĩΓ}џČoʭÞ',
                                                        'value': 'ĹǢΞФ˵ϥˡˤŷȞӑAƲÁđ\u0380ѽϘŎɭѳҪтЫĈ˱ӼԎξΙ',
                                                    },
                                        {
                                                        'key': 'QƴUԭΔ˟ȅϝɰȯʂʌȦωѳӸÇ˸˴ҠӺÅ˃ñ\xadϗÞӢˀʯ',
                                                        'value': 'nȔӌýԭѯ"ˎҲƎę¯ȓªгoˋĪ÷ȓЄʕŔԝνȂͱô:S',
                                                    },
                                        {
                                                        'key': 'ƙͼӱϡҿ˹˥ēýʏӜtÿкÑҨĂÅ9Ύӻǈԗӗ˹ƁѓѨюԩ',
                                                        'value': 'ĹŎԟ˒ǋөԉƞϨǁ§ҼкńψɠĒʜɹśˊcϵЃâƨήgͳԥ',
                                                    },
                                        {
                                                        'key': 'ɴ?²ӶƪҽŝīІİʤ\x84ιЕēӗǔƀʱƓΒɮȞˡŔ϶ɗɆĝ҃',
                                                        'value': 'Ȯɿ&ЉԠʗςΕӱŁТȗÅПħΖɓʁɨӫżˇ¿Ʌüđќ\x90¤Ѥ',
                                                    },
                                        {
                                                        'key': 'ҿĴɒʍĔơɂ˽ʸʯƸҫΏ\x8eƧäϠȱПѶΠ',
                                                        'value': "ғÙʘȟ\x99нʞũϷ'|Ԇ Ƹ\x861ͿŤВʌ\x8fϘσ˘ЋƼâȿǽ^",
                                                    },
                                        {
                                                        'key': 'ʔӖгŸƨ\x9aʡ&»ђ͵МĲҟƟ½ʩàӾƇƋŻԨƚI҇Ӌʒ\xadФ',
                                                        'value': '˴ӿʮԕʆŀӝԃҪLԊ˛ʵĝ³ҶÍâ˯ӝЗđħĢѹѬҒ7áҺ',
                                                    },
                                    ],
                        },
                    'comment': 'ūɅԌȿeΚӢϭͿĒȘіЬŒ\u038dα˼ȇǊқԛ;ǢяIϋÀƇ9ő',
                },
                {
                    'keys': [
                            'Ϯ+Ѯυ˛;\u03a2ǎМ',
                            'АɱɘǽҔĎϼɇЛЅƞӡŭӀϱ0ˑϭ',
                            'ȶԭƢɣѯn\x83Ż',
                            'ýҭҹ',
                            '&έnѧҍΦ˫Ιä',
                            '˖ˎԚή˭\u0382Ђɘ',
                            'o\x8eˬ',
                            'ɫŸЖ+ʴ\x91˾',
                            'iĭǁ\x96Ũ|Ƶϓ¶ˌѿТөљ˅͵Ѥà}Σ¶ɟĸƼõɾŖȽ',
                            'ӱcZԌӻˆҵȩļͱЫċd\x85ȑϯʴѰҧ',
                        ],
                    'event': {
                            'target_id': '˧¶ԁ\x96·ЫȳnNӛȜǊһɷƓÒˊ¤ʴЭư+ÕʭɪƛԐȽǜӒ',
                            'parameters': [
                                        {
                                                        'key': '¨ƟmäĀâʹїʞŮȻĈФӲǕɶÑ.ʿB˫Ө\x9fШɥзη¯ɗʁ',
                                                        'value': 'ӝ%ʱ-ӻї&ÃźǶғɵğȘӕγжăѷΑҷUæöˠōšǆŻʞ',
                                                    },
                                        {
                                                        'key': 'ɨʽӭӶ\u038dВƨŐşπęˌȫӬѸƆaмņŊŊĹкϱȤ',
                                                        'value': 'ʗŲßʜϷíȿȭϼ>ЦțͼԭϷ\x95ŕýѡȗɫŇѶДėıƯȩŅѮ',
                                                    },
                                        {
                                                        'key': '˾ҒϥŇĢ:ɍʩǋd\x86υƘѲӲЊȴƲΒƧ6ԥɳǨǻƳº˹SŁ',
                                                        'value': 'ǻɻɚ¨ĘUхҋƝмϔųżȆǻƟɯǵǻ©ԡ2ʆͿϘ~ʆöɣȻ',
                                                    },
                                        {
                                                        'key': '·϶ԃ/ˍéӐѳơĦɠ\u0379ҺͼϻǨǺϙȈR;ӝЁÐԆӈĺӑƨԀ',
                                                        'value': 'ϘŽ·ÈſŚΝQɨːʕˤҶѰӽҥ³®ΥɦƆуб¦ѪФȾїȺ!',
                                                    },
                                        {
                                                        'key': 'ĒҹоϠν©ѭνԝȣ@ʓŴ',
                                                        'value': 'ŗȸѝϬǤŀӧŊƠɃķ[ΪǞӂĺšЛӂяɂ\x9a˛)еҧȯôǒ9',
                                                    },
                                        {
                                                        'key': 'ѾΞσĨɦѽȊɶĩžǑɡgǞкɏĶѿУΧӿʌĜ)@ЪȂţӈ\x95',
                                                        'value': 'q\u0379ϮІӺʖʾpήұʠүɤȬ\x8aˠˌҙʖɸϧɌǥ\u0378ŀν͵j`Ȣ',
                                                    },
                                        {
                                                        'key': 'D,]ͱіԮΏ\u038bΉԗɰфśӜÁ¾˚ˢȪƎԖ\x88ёąÿϷȸęÚn',
                                                        'value': 'ʑϖʽɏԁɉ<џʍıŨӅ\x89όԗ\x80ţ˛ƽń\xa0ԓˎ\x95юѻћ=ʎɻ',
                                                    },
                                        {
                                                        'key': 'ǧʺƋPϿ˽ηǁԛˀ',
                                                        'value': '˶ðʞӵѲńҝԕʂǴϚэƫĲӋȬʈλÿβҤɆѠрӷƹǀ˭ӫҍ',
                                                    },
                                        {
                                                        'key': 'ţìӒųѦˍԞ5ʢӬС˽Ć',
                                                        'value': 'ŷάcǯǝѼƎèӃȵǪŵÓҌԘμһíǻӀŀſ҆ǃÚϥϜЉȣˣ',
                                                    },
                                        {
                                                        'key': 'ͱҾÇÀбΨеɃ\x9aǡ\u038dН',
                                                        'value': 'ąsϸӐҐҥ˷øRˮ˅µǾȈ×ϜЏƺȵ˝ӳÜǀčϰÎϓʎŐɷ',
                                                    },
                                    ],
                        },
                    'comment': 'ƴɓбԓEĶȰʗϞ˯ϏЁɃɉϑǲȤɡѲΥɁĲȇϸҘŶàȵҺũ',
                },
                {
                    'keys': [
                            'Ӗ\x9e.Ǵˉ_ӟϽǱ4ҲҭΝÏόŸɘЉ',
                            'ƤϠϘÛȑЋҺǊđȽ',
                            'ƍ\x9bûϚʗʔ·ҀÒʈӁɦ±ҋѡ',
                            'ŌшϚњΩӦƼȺ°у˂ɛ',
                            'Ǩ˽ЃӴ!ǽӪ',
                            'Ώ\x8f\xa0ԛƚʭ҅ˌǵӄÂԩ¸ĮѲ˳Ґв҂ҹª\x7fł҆ƸαÝ\x95',
                            'ƧǭϪЁИĒɶŪѝŗµȉɯƷŌļĈŔΛҘ',
                            '¶I',
                            'ȧЇˋ§Ӊ',
                            'ҢĬ\u0380ԓλɬͰ½',
                        ],
                    'event': {
                            'target_id': ')ɹǧ¨ʤЉ\x8fԖ¯ɻʊɾDŏҞ˃Ʒ¯\u0380Ǩ˚˶ӭϽʳȓǳ¿Ϻʦ',
                            'parameters': [
                                        {
                                                        'key': 'ӻԫіĩԥӟìÆђˁʭ9ЂʭƤ',
                                                        'value': 'ӌЎ\x8eςĞѭǿ7ʥ˾Ϥ\u0381ʯ÷Ƕ˔AΝʫgʾ{ǣħDńĎ£ʱ\u0380',
                                                    },
                                        {
                                                        'key': 'ĦԚȪɴϵʫϟ\\ϞӯϱΚʅԎ˩ƦҜŪʔPƴ˓ôUʐӏҢӴÌŠ',
                                                        'value': 'ˏɋÞŽʤІħԌÿÐďZηϙıǋқɒʸҶºɼФĵȵĔʈΉͱǶ',
                                                    },
                                        {
                                                        'key': 'ƳɓȄȕ¿ЃǠ3ҹ4ƿ/ĩġӔ҉\x81ҮӒС ¢˖ƱȜŠɗϕʸӴ',
                                                        'value': 'џϞʮ\x98ѹ%ʡÌɂōvɚΦĄ˅ƮҖÏɕϠ~ǢϞҼƇҜ҆Ӻ˽ҙ',
                                                    },
                                        {
                                                        'key': 'ϖ³ҸǮȵ\x86ӂɘӂKŔɅΆ˥ϸ¼¢ЎѦЂˉ˦ƌǈӘ·ғȰȗӽ',
                                                        'value': 'ϹЪҫόê˷ɪҞѐϻȁҐZãä\x8aƋǴĄɋČȆӫG˫ʯŐλɲ\xa0',
                                                    },
                                        {
                                                        'key': '\u0383ɡмȹɣΰǾɢәʈÿϵˁҜP\x90ʚԂҶɇŠȡɰPƍԮ˾σʴĭ',
                                                        'value': 'тɅǽԦˮƻԛхДˏ¹˰ӚҬΣǖ\x90ϲǲɼҤ˧Ҟĺȷ˩>ʩʻˊ',
                                                    },
                                        {
                                                        'key': 'ЪȴӬčȲ(ĕʔыýƄЍŸȭˍ\x9dǬUɻԮ´Ƞ\x90ȅԫǓ\x9dӛǓԨ',
                                                        'value': '"ıŏЋZԛνȦгžϏ\u0380\x8aǺʅüѺɵЌjĠƞфŝȈľĶӃӥm',
                                                    },
                                        {
                                                        'key': 'ŲĉϲɍʧýʠîϙͽӣјĞİΙǘҤ\u0382ɱ+Л\u038bќѣ?ʗźo>Ӡ',
                                                        'value': '\x86žǁʓÓRѐпǭѠɒôɝЫѯϳ;[ңƉтЕʼǯșУƯςƐѰ',
                                                    },
                                        {
                                                        'key': "ήʦҏΐ\x8bϖɰЮȽЅιш'Ġ·ĀԀɾЯ˽˼͵§ș˯ʓÀЫȉù",
                                                        'value': 'ɷğéЯΌµ{ˤęèɲļɑѯóĆӁɆјЍњΌӒċĞǸµŲδƅ',
                                                    },
                                        {
                                                        'key': 'Ť³ҸαȭPѦϱȩƝśέȸūaä˨ÜϕӘĪZ«ѡˢԈΞʕ˺И',
                                                        'value': 'Έ˂\x97őĦҁƝŸː²ÎrӄʳƽͽʱƖȵǉ\x9cӱЭǚ˦ʑѿФǓƇ',
                                                    },
                                        {
                                                        'key': '˾ȍϋ^ʠȹÖԚЃϹԌϼť˗ŖÁˆφʨǹƕǪ˒ȘŭʌɧҜfǬ',
                                                        'value': 'ЛπƻŪȩ=ĞȀ¢ƾұМʞԦƔҬĢӜƧӭДϾԇ΅ńșЩƲBҴ',
                                                    },
                                    ],
                        },
                    'comment': 'ѳȵЧfŒЁρȸИӬώѥǙˋɫü˴ѪɈгѽɂ˂MʎɍǾHƱƺ',
                },
                {
                    'keys': [
                            '£ˣжÍҷǟšĵӵʾϠ',
                            'Ŋ˛ԨƢКΡҔΘЀƠ\x8ez˴ԘΖѳƓɮҕȽҵąϚJ',
                            'ǹőȝӔºѨʑxƾϑҪҹ¬\u03a2kʴ;\x83ƒ',
                            'ѼKԟɑƷʝNǼ\u0378\x9bӈ¤ӬŕȵĭԞē˰ːȿԖǮχ\x8f!Řūǿ',
                            '&ãƭ˯ңDηʖ;ʫɢҀӉèɛ˫ŎΛƂɤþǮƠɂ',
                            'υȑǭbʜŴӢǶśŻ\x99Øˌ\x80ƴȷǲÐйɍϽВɕ˕ʿť',
                            'ѱɇýƣҐʼÇӫӘȩρ',
                            'īČϔĘΌǉЃͶԂҨȻӫǖȣοɌ\u0378ǥǻǩЮϪćˋå',
                            'ʿЅѭŞҠǩ\x83ӀȬǶ˅ғɄĲŹŦφŚ',
                            'ӯǻGҢɊƬ',
                        ],
                    'event': {
                            'target_id': '\u038bΫ\x9dÀÁ˰´Η½ȣ©½їǁğУƀ\u0378Ƌ\x9bӳΗʠ÷ФĖφʦѲю',
                            'parameters': [
                                        {
                                                        'key': 'ɢƎc8ҍгɟÞǌЈƶΣƒȕϳɾʕʠɄ\x91ʻzϿӳ\x8dЏ\u0383Κӗɭ',
                                                        'value': "ɩ\u0381ѲξǐsϢťѫsΣƍ\u0378ďѽt΄ЗҟšЦ'ŀʷɰɑпѧΦΕ",
                                                    },
                                        {
                                                        'key': 'ЧҪϧX\x89ԡҜȤƑԧɷ˺ȝȪ',
                                                        'value': '\x84ȄɳMńã;8Ė8,˥ӐĶˁʀӥ&ɛԥĒƦý˚ԛɵδˍÀω',
                                                    },
                                        {
                                                        'key': 'ĒħʻeƯǃȦȬӕȷҫШ8ʩѹȟˁϋԢCʁӿҰЅȕɱřȩǛǱ',
                                                        'value': 'Ɉ\u0383ӜъƲԪУ%ňΒȋʑǠŨЫ҇ȡеѸƋҔyԄѾϽöγȀĔƳ',
                                                    },
                                        {
                                                        'key': 'НШ\u0379ӵδʞ×Ȩɑ?ͲʀЂϕѾˉēĻƻΚӜȧŵʖЇɹΛьԬ˜',
                                                        'value': 'ҼϠĵ˪ȟźʳ\\kŃԟȯ϶пɰƻҸӚӰŧĲkȂȥ\x87NǪÞÆѪ',
                                                    },
                                        {
                                                        'key': '\x98ˆΚȋюΦΊѫɭČħʱʭgӍӍљҳƺԥǦĤŨІұˏˠԆŐĸ',
                                                        'value': 'έĽǵ\x8fҒԬԖǣqȘ˙ǖ˧ҔːĹʏɕţҦǟˠŀÙȿҶqȕĘɤ',
                                                    },
                                        {
                                                        'key': 'ʸͺØŸk×ӼƁƁκǚ$ǕӏűѫǝԤΥșиǍʹńʫƣŃӑɽɴ',
                                                        'value': '·˒ˡÐһяĸͱȌΤζ˟ǳҐŢВĸӽ\x88ɅԐǙʝġĝԒȠʪȿú',
                                                    },
                                        {
                                                        'key': 'ǾГÈˬȌÀΠҝԗΐʥϐɪѢŀǘ\x9bҵͻ˛Ͳ˔oщËϽͷµХȣ',
                                                        'value': 'ʜ\u0379ѡǄЌґƂ¾\u0379fčɿ²ÊУ\x8c²öƾʴŧжxĐҥŹɃҊʃа',
                                                    },
                                        {
                                                        'key': 'ӞΤƨϟƻɣƗѕΛѶάϕqŔ',
                                                        'value': 'αú\x82ƖǤԍĦ\x93ŅɡFIгȂÿȆɢъǃВѬ±ǾȒԁ\x8aǉқЉǇ',
                                                    },
                                        {
                                                        'key': 'ЂúЮ΅Ğяǥк4ƅӧ˜ӊЎýҩƹā§Ϣϓʀԙөˆ\x92ƔƷϝԐ',
                                                        'value': "ȴӚʗǟȎ3ЪκѬԥ΄үţt˦ƌ'&BƧ\x8dɖĈ~1ɇ(\x91ʫҶ",
                                                    },
                                        {
                                                        'key': 'αҴûӗɗȉŃȸӌаѝβµʹXĎԖǴƧҖϣњ\x86іǅʟʭ϶Ƚӏ',
                                                        'value': 'Ď\x94ßЯӄӻʛɴӿʖűψŊϣșǱʋOӑƤњŜЌӻшѮϷѬʜƿ',
                                                    },
                                    ],
                        },
                    'comment': 'ѳђÎ!є-ЩãŅ\x8cƧђƹя˽Ơʱ˱ƴŕ1āƐȴʻҒҗǛ\u0378Ɵ',
                },
                {
                    'keys': [
                            '˖ÀҐӓϙѰҾġϮ˷щ˾éџ',
                            '×Çʃ\x94Ŝϯưԋ³ҼqǞȄƤӇЈȲʨǀϨԖφяo',
                            '_ñäзîǄoВϓǢѶ',
                            'ǆͽçѕӺЗЊǽ,м¥ӶlҼwӗ˶(ӊϠ\u0383˶ŚԉƇ',
                            'Óɕ҅ĸΙſ5ϥҶ˅ӢŊѼǣŐɽÍƴŕ¡ȀȓʾìӄF',
                            'OUqŀЅΗǓπ\u038bǦâԇȟѪ˜ĢrɾÔԇɣĶőuЭͼȶtњϊ',
                            'ʘÉųͱʊC@=ûwҳ\x80ĉӭʍајƹ',
                            'ǲӵʝƶу[ўΛȑЙŷΊЁǴ ԣǍeǓϣ',
                            'ŞѓʊΔԉQ>WӭӁǗȐΐөъĪδŮËbȚŰӺͼХћΔ˃Ȟɽ',
                            'ŬȈňɲŊȇʨ҂υİůdѭE\x805рФʍɺÆϋÉԄŭӱīƨɹǳ',
                        ],
                    'event': {
                            'target_id': 'ϬѪ\u038bʒȪF˛ǰҀôɠĦ\x9fƝɏˢФѝмȺʶ0ȷ`Ʊʕѹԗѕˎ',
                            'parameters': [
                                        {
                                                        'key': 'ώåÒСӘϚqǢў×ɁҞº\x8cĹ˜ϋʦО<Ӿ˽őăДʵɀǧѐП',
                                                        'value': 'ƾɸσǘҞϢϝ²ҙӛӅ˛Ɏ¿ˊѤ҆ůԔαˮ\x9cԋďʪҐ#βҿͶ',
                                                    },
                                    ],
                        },
                    'comment': 'ˢƩğɓÍŕƵӻƞ§ҏˬƢǔҟ4ǔɷӿ.Y҃Ӳ\x95Јӛɪ˅ɇƘ',
                },
                {
                    'keys': [
                            'ϸ\x8dȰ\x8bȥ\x8dϠÁɗȇƳҧƋԜƱʼѴʼĤϯī',
                            'ӻǣȖӢʿɷiԟėʅȽǨʢɫƘ',
                            'ЛѹҹƙíӮӼƐ,ҰҩȲ˄ϵĀі»ΘȾĈцңϨ)ϏЧɛȿ',
                            'ȵ¹ɁıƃȏυΒFQɁˤ',
                            'Ľ˾ДŨǮǉɑƳΛϊ',
                        ],
                    'event': {
                            'target_id': 'ťԔӟůȂƾЍӄɿ«ɬӚà\x8cԛȣȗԈӚʫśβ5βҁ;ʅĤȧѓ',
                            'parameters': [
                                        {
                                                        'key': 'ϼ¯Ɋ\x92ĬѕĶԡΎғϙèԩʼƧˤЅӄѥÑѿКӃԈVɧϙɊ=ƶ',
                                                        'value': 'ŨȫӮ,ҐĄҽʉΊȥAχёǣ~ȇƞœτʨÚƩŔĢ-Ɉƞҕȧƿ',
                                                    },
                                        {
                                                        'key': 'Vјʜё',
                                                        'value': 'ȡÝɲÆûƟηǔϖԒԣŖЎѣ˫ɞƞ\x8cӔΣɛϐ˧ʇϺɱ|ѷy«',
                                                    },
                                        {
                                                        'key': 'әǵƗɨ\x9fČ[Ԙ˚\x89ΐѡȀμɷǴbϓ\x97ȿĻa³ƜýҜáϔƋ9',
                                                        'value': 'ÊĆƢÏВȟԜԘ\x92ʰкāɽĴϦȶŇІĈĆԏɾ®ǡǌ@˲ Ʒӭ',
                                                    },
                                        {
                                                        'key': 'јӿҧӮǢßҬ¦ʞϼþ҉ʭ¶ZâˮϾӿ\x81ˈȣ˥ψÛs˞ȾĻŞ',
                                                        'value': 'Î}ПɥĺěǔŶшɉ\x82τЭIOѠжΏĈиǵԏνĨāœuȆΊП',
                                                    },
                                        {
                                                        'key': 'ķÊʛƾŃӓѽԉƮˉ\x96ӊčJº(9àїx´ʠ°ʑԗѣѬѥĒɃ',
                                                        'value': 'ǯҾŋqԒΌƥƷɵčЏΠƳɽɬǜıҠȓʾєĒĖɟϜѩŀԋ~ȯ',
                                                    },
                                        {
                                                        'key': "GΌƃ®ƾίm¨ӟˈѠҴʆɔρěhǽƮ'ԁʕǇůʎɶǷȶǡ!",
                                                        'value': 'Ҍ^Ɇϝ˪ίсӱȅЌρNлːϢёQӝůЃɖϝĘȭЍ˕¬ʳŔΞ',
                                                    },
                                        {
                                                        'key': 'ӻζ˅ӐɱÙ˰´˝ΆϺӪҦҫĳaȰ\x89ΙƦǵ-ʳʇАʁĚúҰǩ',
                                                        'value': 'ǅѧèʜ¼ѠςԟӧФŖÙǹΆ˯]ĹϙˇҗΓӇ\u038dЙǷˈ\x91ɩɖî',
                                                    },
                                        {
                                                        'key': 'ˎĜΚʟнаɜGȮЃåӶΒԂʑƳοˮÔ',
                                                        'value': 'ș±cƳ\x80λ%њҼ\x96Өá˟Ŏӥͺӷ˔~ҒϊѱўĤɂĤʢѾԜҏ',
                                                    },
                                        {
                                                        'key': 'ԒŜпȬԥ\x96ƋЁŵɗȆǏƜӮʺҝҙƇďǎʾˋЭȯύŊ¡`ċƔ',
                                                        'value': 'ǪȰϱԊȔŲŔЌԭϱЀ\x95ΐϟ3ϕ˭ѵɽϮɋšϻъРгƏ2ӏŹ',
                                                    },
                                        {
                                                        'key': '\x92˚йÍӟҶ',
                                                        'value': 'ɡοϯƜ˛\u038dΓ˖σЇѝºԒӕâҹɺàΦңpcѡљΟќЄȨʪŮ',
                                                    },
                                    ],
                        },
                    'comment': 'ʧȹϟɁљĊŚαŃɻȹ҅ФЫҤԁԚ¥ŒțΨўѱӻB\xa0ĚҙίŐ',
                },
                {
                    'keys': [
                            '\x93ѹҵϘAЋѺəĴjȸԖ˥ÛȴϳȈÂÔĸɑˑMԙѹ+',
                            '\x90ÎǤñǥчȓ\u0382ĲЩɏ˸Ӵ',
                            '\u0381Ѥ˸',
                            'ɝϢƧƞȶĐϤХǁƾ9ђӬβʎ[БʖZŋǉŏʂƗˆѱɖŌ',
                            'ԧŒ҄ͽԑΖ҃ԙˈΎϓǎҝϠȠŢɏ<\u0379',
                            'ïɪƔ\x89пå°ǬʑЋ\xadʂȀӣñÕЈˎıυĎԜѠǶůбϷ',
                            'σ',
                            'ӅãɡʗƪĴϭ³ӋӌКáϬ`Ŏɀ3уҜ%ϯ',
                            'ÐӞпԎĚхѓɔɟɒΈϝŊяʄŋҵǤ{ȼɳ',
                            'ӠĜ!ӎϋˈτCɬŭȒ6ӨѪ«˰ǃҞξϹӫΰŖѻӪǒԣ\xa0ӧ',
                        ],
                    'event': {
                            'target_id': 'ÏΪΠő҆ǫ˗ǙĶϷˌƇƦȒƹЀǜ\xa0ҫɟĒңÖǇș\u0380\x8eŠϒd',
                            'parameters': [
                                        {
                                                        'key': 'ȏǤȴҊҊȰŕ^ӟԢǘϨӽɾʬңІuˤϪÙ˙јǘF\x90ʆπΎ9',
                                                        'value': 'еtѢ7ßԓƧė˟ǎȋԘˣφʶƅˡрŷÁȏĬңñɫѨӑǞъǊ',
                                                    },
                                        {
                                                        'key': 'лʥɠǋҹ\u03a2ƾϪƚlEƫҁſћXλΔĭɫӂɊŨɗ˴ȡĹʇǪȩ',
                                                        'value': 'ӢϻӑӦĐϲʐЇԆư҃ʫřΆһſwǨRǃ˦ÈʾɾĔľɧƂϳņ',
                                                    },
                                        {
                                                        'key': '˺Ɵʪb˒ãhŵύǁëρȠӔZԧʽԦӅӹƄ˭фȺʴōĐňǨ',
                                                        'value': 'ЃǫØ\x92õɓȋƴȬŒυӲϞɳАзhԀɫѯ˻ѿAӈԏǦӺQÍҖ',
                                                    },
                                        {
                                                        'key': 'ΘȴţӿΫ½ǅίӹћυʧУѓˁͼ\x9cϦʦ+ҘϼɐŨӉĦӏ]\x85H',
                                                        'value': 'К˯¤ĶˁԈмȎ9&K˗ϚʵȅЮýŦɮϠȞ¦ʺÍӪӘЍΌɾƢ',
                                                    },
                                        {
                                                        'key': '˙÷ǀӑѢĲɫϘԥщӫą˒ϏʼΐŽȩĭұƷȆɂĮϱӒƊӛȂ=',
                                                        'value': 'ϖҗɏͽʌ7ϩ\x9aǶΓĸðĞϞΘ÷˛ϏЧʬЋɲɻĢĜϜǀϧñŧ',
                                                    },
                                        {
                                                        'key': 'jѬ˟Ӗʴzǟ\xadϦхϞGɗǙŷƹǺ˨ГXМ¶ƫѤκʽӽҙѪβ',
                                                        'value': '-ҜЃѩȩʃӂŬſͼɾ>ˍŧAш£ЫѥɵуΕÇƄήɁm\x94\x9fό',
                                                    },
                                        {
                                                        'key': 'ΣҖû\x83ƌҖΆ\x8b4\x9aɼƐȵѰƩɆʦʇњá¼ãӲ˙ǈИԔԘѕѬ',
                                                        'value': 'æӌΊ;ӘĜŒѴθĪɟQӼѩѐUÇȵ\x9fŇŜIɟèҪǇÿǅԩѴ',
                                                    },
                                        {
                                                        'key': 'В\x90ҒǤŖĻˇȧĺ\x86ęԖԛЛӟƎɚD_ɏ·ŤĠɪ¹ˀšПЎɲ',
                                                        'value': 'ȈYчцϻхlĜ4ǵŚљҊˣЙFуǵ\x97ʺüƸɒě¯ƈϰ˕϶d',
                                                    },
                                        {
                                                        'key': 'ӆŜ˱ŵoӘ¹£ӣӭԗǕơȻѿȣЗɊǧҟӶʏ`ϪθĖ:îЉʟ',
                                                        'value': '*ѲЕοԔˊŇϖŋлˇыұǤſîEϴӯ\x91ҝʂ\x8aƧδǽɛѽ~ɱ',
                                                    },
                                        {
                                                        'key': 'ôğʍЩЏȲ҂Ԃ·Ԃǚ˼ţʹҜӷǨ˓Uі/ԕїЁȔɤЛȬΥϋ',
                                                        'value': '˙ʘϜ®ʞӆvԃŭͰ΄ҙмѹӜЈѽīʯʜʐá¾ȼӰ\u0380қÕĿɱ',
                                                    },
                                    ],
                        },
                    'comment': 'ΨǗʆÑǰôUӜńѴЇʗȠҭƘҽΊЎǾΌɔˡΏʜóϿƦʠѡǐ',
                },
                {
                    'keys': [
                            'ƉМıȽԮ]ѵ҆',
                            'įǬдѐʑӾʷԞ',
                            'βѾ˼',
                            '¸ӼʈаˤūҊїʨӿʌt',
                            '¢ΌӄĻӚ˹ҧӆIƐ˲˲ԕ·uɿςпҳ\x93ђѻ˪ɝǌŷȗʛŔ',
                            'ˤØӅӱ\x82',
                            'ÛɌ7ǫϤΜΘƢXŠʬǯηǫſɯ\x83ǶȓȬɠɶģҵ\u0379',
                            'ԆŤҷиŲ˓îѦӤɫϴǆʇȶʢ',
                            'CƬӅ',
                            '\x93ҁӼ',
                        ],
                    'event': {
                            'target_id': 'jѐåϲԘǁ\x99ªϝΜ҃Ѩ˒ϪʑeíǦŋn҂ĝбĊоȉǮȟˇͼ',
                            'parameters': [
                                        {
                                                        'key': 'ĶŒȿʆŬ˸ӁνČưǇƋõ$Ҙ\x8dΑʦқńɴ ϗȷӓ¬ǎˠДӯ',
                                                        'value': 'ҊԎсϰ˗įŨƭŽŹӿǯЁÕǰďҞGƓαőԈ˴)ŊɱpҧΨj',
                                                    },
                                        {
                                                        'key': 'ȀłγМˆ\xadґƫɼΙҦ˒',
                                                        'value': 'ǩVśԜȇȠƎʶĜȢˑ¥νѾŹӹЗ˾ƻӚԩԗѐԭҎϴ˳ϮĎԥ',
                                                    },
                                        {
                                                        'key': 'чʀΌԣďΰ1',
                                                        'value': 'Ӂ\x88ƦɫʨεДҩӄυt\x8fGȁǤdӣΨNƼԏͲƯҴɰΨϠĪ6\x81',
                                                    },
                                        {
                                                        'key': 'yϖɱ҇Ũŧ\xa0ÁǫɩӋЌњѿȏƐ\xa01ǾɸΌѫЦƕΆʦʦ΄ϯԘ',
                                                        'value': '|ԦɠςԎѷҶQȩϼѵĒ:\x8dϠüӲ ҌŲÈȯ\x80ЬύĸǪsҍψ',
                                                    },
                                        {
                                                        'key': 'ɳ{˥ƞ˼ɿ',
                                                        'value': 'ԒǗƼɲd˾\x9eӺκǃ¹ǲεǫӈүԈůȍżˀƄʿƞƔϮҺɩԗF',
                                                    },
                                        {
                                                        'key': 'r͵˻ȀÒķƻǿѿśƺ0ıq\\)¶ʧі˻)ʪʉҎ1˅ѠƧ˙ρ',
                                                        'value': 'ǗӼtƉ˹ƶ.ȥԣɝ\x9dțЕ΅üїѻԊͿÜϰǶǝHψWǵ=ҽƦ',
                                                    },
                                        {
                                                        'key': 'ӟˣáɌȠ9˯Ҵù¸ѳϤʐҺȉɂ\x95ʺǾȭ͵Şĭќҡǧϸ{Ѵƅ',
                                                        'value': '/ƑʔԏӼƛͺʇ\u0380Éʀ¯ǯĈʵĊϊŎƴ4ϞȖϹťψЗҍɡǬѬ',
                                                    },
                                        {
                                                        'key': 'ϽеBЭԐϠȀʌфȐιȨʎʩǼʗÝ:зƲЕM˖ʋ¢ȳзѰӟŕ',
                                                        'value': '»ӫЍ]¼ўƼЪœŕΩïд˅ˇЃԁZ!R¢ӗĺƿǭгʄƈϿԣ',
                                                    },
                                        {
                                                        'key': 'oҬÚұǥǯʑ.ӱåҲҰҦǛcүϑΗцˬΞʁ\u0378ʃȾʫƣʞȮ\xad',
                                                        'value': '\x96Ρ"Ǧΐѷ³ΕөӥʬϭǖӷÿǾÉЉƢƏ\x80ԧȧƲƯҰʩǺϝӒ',
                                                    },
                                        {
                                                        'key': 'ǊϬʖ¨ҼΞЂǬɗʂĢOН\x82ϮɅʍƉѳƆp2ȥϘŌΗÔζĮP',
                                                        'value': ',ʇгʑƩqɦƾÿҀî\x80ñƄɜƂѯΉ˼ðϫƺŊɺʩ˹ƨÕԂϤ',
                                                    },
                                    ],
                        },
                    'comment': 'αƯÕ\x87ȬϱԚ͵ʃϯʽγȚӹťƍ½ӴΎӭ\x81ǆГӏĨ\u0383Ϳƫ·/',
                },
                {
                    'keys': [
                            'żьŝ\x97Y',
                            'ӠӓŚҤ˓έ\x92ŧŎöȝƓ˪ҁϝϪɫǴ',
                            'ͷӅ(ӽϷĀҬѲІ\x85ȧrƽƛ_τʭĹҨͺŨӃȺǼǗ/8҃',
                            'ǿđρɎǁ\x86ȡ¶ɨǦǢλƍɼγɘʤǾΫфˁĞ',
                            'ϘȇЯцiӽċ˞ӺΒȮʄʄČƃ',
                            'сŭϓ˦҄',
                            'ƼΒ¾ŀϤЇ*҂ƀxԘϐǑΚΔİĤŤьԑɦ',
                            'ЪõƸϱѼѸɐʞ÷q΅ӰԊȺӋȟğ',
                            'Ѷ\x94ɷÓtҲˏÁ9ҹ',
                            '\x91Ж',
                        ],
                    'event': {
                            'target_id': 'ïĹД>ȩϧѳżǞıƸԛԅŌŔʊˈƑпˮŬԢ`βӵаİɫьŁ',
                            'parameters': [
                                        {
                                                        'key': 'Ѵ˝ȩӯĸҧēФҒԭρ',
                                                        'value': 'Ưȩ˅ɃƜÅmƤЄȪΟˣѧă9ўѳ҇ҤŜĒYΊɪэgϢŌȲʀ',
                                                    },
                                        {
                                                        'key': 'Åҿ҄TǆЬѵѴƂĕ ŪΦːľɾЩШˍƾѵӫĤnҕϪțĀBʓ',
                                                        'value': 'ӎřɜ˻ϾʨӟЭ®ǤʱǂĕԎԪήǺͱŒъτț%\x83/ҼԞƢSȪ',
                                                    },
                                        {
                                                        'key': '«ԋӉƕƎȄʔҘʱϸѴɁɰ¾ƇрʼϾ ҩӳΐ÷ϨÎ˺ˋƟ3љ',
                                                        'value': 'ɓ¡ʼſĬǞԧæϞӼùϨÏTƔτ)ҧђ˄ԝłΜ¨єƾÉ҅ȫμ',
                                                    },
                                        {
                                                        'key': 'ĔϛЧʻȉæϰʕҢќs¾şπsǆ^ϟѻɤšɳªÊǟҗҀЉϓΙ',
                                                        'value': 'ȚȾ˟¨бҖРӎοˮĞȄǯQļʃ\x95˒ԫvčщΦŖѹɽӱǕʤ˼',
                                                    },
                                        {
                                                        'key': 'ѣѬϩ~ұbҵi҄ӦϒʹśԍʲȖ¹Ғңα˜ʫˑӡǿҨҠӨӌƧ',
                                                        'value': 'ĽžȱӴŻ҆ΏYӜ',
                                                    },
                                        {
                                                        'key': 'Ԫ϶ͻϹ˜«ӏƌˏєɒ\x8făʭāņ΅мÒȽ\u0381ȷɜԬƭ϶ơєŬѿ',
                                                        'value': 'ѣǦɊqǚТǩˁ\x88\x7fλҾtą˃ɗӈ>ðњΟ˳ȿндҶϫRҠц',
                                                    },
                                        {
                                                        'key': '\x9dbѫʬ\x92',
                                                        'value': 'ҟɢИɾҡӳ0ȷψͱƅѮÝˋҸȘFɶŎɆRŃГҾԑíʇӞɋΧ',
                                                    },
                                        {
                                                        'key': 'ϢȿUǼŉкҏԖϐϟʆƌª~1',
                                                        'value': 'їWѪƮ«·ÜҜұЕ_sĨȈԖ˪ӔϞĆ|ζϣмýƧтǍ¶Έɪ',
                                                    },
                                        {
                                                        'key': 'd×ĕʈɼΥԐȳΆMɛ¬ԕЖӈ\\ȴʩφɞρĎ˙',
                                                        'value': 'Ξ\u0378ƂӦxȲƮάȺѧҰĬɅÀҠ\x88Ί҉ϘƇőģЪʻƫʅκϽ¨ʯ',
                                                    },
                                        {
                                                        'key': 'ȗŤ,ϮĨс\x8a',
                                                        'value': 'ԃЉȭ8(Ȅlűˏԭ¨ϖŉφBӸʠʽǦų˦SҐ\x98ьѢ҄˼ʵӷ',
                                                    },
                                    ],
                        },
                    'comment': 'ԅȆҊѾɢЉǊѶɮˎϬƵѺî\u03a2θÐǘ˖ұАbˮϷǄɀɛҿɯЦ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'Ѱ',
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
            'name': 'εsˮɸӎƋAˣŗÇЍΜΰǋŽяʖуſӤŁeÐWǫϋ0ĶʜÍ',
            'description': 'ʷ˱ĨБđƺƻǂ\x9eÁӖ˖Š"ŐÕΗêŘǦɨЁOkŮϯƱƢ¼А',
            'target_id': 'ǓȕȂҴƊƩƩťϻȜTƙӿ˄Ʈ˓ƣвÝɿŌФƽʬÞŽʜόӱз',
            'parameters': [
                {
                    'key': 'ȜƚǶǞӀĆĎõTҖбŷԎØоЩ',
                    'description': 'Ďȱ)ƉŷȇѣͲҊЧȓFǓѹȺƴӭ\x95ԅɦғǪө`ύлGȪ5Ԏ',
                    'default_value': 'ʳċƄΜΡ¡gӇ˙Ӗ\x95ƃ¯ȮԜԕ˚ɄŇЎˌԜΫӱϪρЎ͵άˑ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȩНř',

            'target_id': 'ʶȥǃҞʄ',

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
                    'name': '7c¼ӝԗǴѶɠlǔѡťâχ҃ԩuʀԓϒλʄɤŮʇˢԋ?Ёӫ',
                    'description': 'v[ĝʻ˔ғÅ}Ʊ˅êӦqvʶθūǣŀwǱōӵǬſďѷӸEѕ',
                    'target_id': 'ªͽ_Қ҆ԉƺ\x94H\x8cĀ˝ѸȜ\x8eÊȩa#Ǎ<Ιўɑѥż-θʏʶ',
                    'parameters': [
                            {
                                        'key': '°˅Ǥʛʢ\x93Рӏɫ\x82\x94ğԛɳķʏϗѷ5ķβ\u0382ӻíȷǠά\x94I¹',
                                        'description': 'ƀĈӀɓҗʟʙϽїҁƍʍƋ\x8dӄλԌʓћ˕˦ǱΪБƹXǄЎoŏ',
                                        'default_value': 'ѐɲ˃ҞĪʱͷkҶӊҵƺӫ˺ȒnɺӐRϬʁДɴ˸ǒEiȿΥǢ',
                                    },
                            {
                                        'key': 'ƩԛӞ˺ɄȓԟӰȷȖ°įhJö˺šȡɛʉіÅY҇ӗ¾˥ԠȰĹ',
                                        'description': 'ȣ˝ĵȦǊʘΎLĎƓɕƮ˛ԇď˒ƋŷǼҟҶсξ\u038dơ¿ƆĢ)ă',
                                        'default_value': 'ðčȋтś[\x86ȟ˶ŦӅǚĕ˥Ǟԝ\u0380˄ӚŢΣǗ\x9dϢȆ{ʯĒӸї',
                                    },
                            {
                                        'key': 'жѿҗĐˈ˔ɑβƫԄ$ѸȢπԆƲҀȍɒʳűОƊǧÿĔ͵\x88ͺǫ',
                                        'description': 'ʋþΙҁԩǄԡñʸĖʦϒϒϩŘΗɛƃȨɼԑʓȽҒɖɵǡҷ3Ǜ',
                                        'default_value': 'Ԕİӌȝ®ʇąÖå;ԜϘȼѥ\u03a2Јȡӡȉǩэф½Ǟɍɍέϗ˳ϥ',
                                    },
                            {
                                        'key': 'ʡǵąʕŮ©Ȃ³ěȠЫο¨ӀƲҟŢƦʑέ\x95Ũ8ȧŏ\x87âԜͼѴ',
                                        'description': '҃ѕʰʓ¤Áö҅ƍƘȀүξÜӮ˦λŋϫаƞǌёѳːӺԥıɃϞ',
                                        'default_value': 'Εǜ\x99ƬҳȥŚKŬцїҺÃƔϮCQ҇ĩǾщĤőѷǏ3ʾǘƠ6',
                                    },
                            {
                                        'key': 'ΩȻŖŔNǻāSɐӅϋƈ˜˘©Ԍ[Ц1ĔӲȺǷĦάҥЊǓФΗ',
                                        'description': '\x8eϦ±ȘìǤΗǹ',
                                        'default_value': '˛ІГĠ\x83ҍοǀˤǚҨϯoӄӂòИжԜӵʺǱǑҊƣӅЕӲˑ\u0382',
                                    },
                            {
                                        'key': "ϽѾǖˉàЗ;\x8bыǵvȘ\u0379Ƅ\x87϶ģϐˊļƍΕǜϋǄ'˵ɼʔ\u038d",
                                        'description': 'Ȍůζ˛˔΄ɵȬȿiήԢƱԓЅȂҀԡʹ҃ӜǕˠҐÌəȲŁɌ±',
                                        'default_value': '˴ȨƙċӇʠ҇ӕʮȒņɄΙҦІʌϯϛϖЌϻƾhƳåȴҞĶȠǀ',
                                    },
                            {
                                        'key': 'Ţļȼӂˢů£ҮЀōɕҵǺ˶Ƨϗ{\u0383ҮǧøҮ´§ˁºйͽƫκ',
                                        'description': 'ˣpԎfİƥ¹ȡǜƠϳԊŧӷΩĶʤƄѪѴγqǋӯоƸϥΟΙm',
                                        'default_value': 'ƈțơ-Ǽʇԅĺ3ŹҁѮτƬЌԍθтʸϒӬķʖ҈ſІǎѝħǚ',
                                    },
                            {
                                        'key': 'ʯʶåУєVǬÐϼǆ˅θљ\u0380ɅΒΑԪŭ\x9dťĝȳ?ҭëɤҩ¼č',
                                        'description': 'Ǉ\u0378śĸăɶаηҐ˞ӉŚЧӟ,ɈǭԟωƎώϢДƅϩԊɬ˴ƂƑ',
                                        'default_value': 'ťϮǀҿѦӀƢkҭǋʦҧΧ\u03a2îʊŎȁģ#ѕɺȆЧӹԊРʃ˻ƌ',
                                    },
                            {
                                        'key': 'ȰɑȶX\x91ҾïԜŗˋѾҪ?ɒʉɎȃʾқ˘ǺaˢҢ§ʅǵϒǖӇ',
                                        'description': 'ҔĳGŐʗÜΆԛŴɤҴΝ½Ǣǳąʳ҄ʟѰϏŉҿǵƜМ\x80§ŦC',
                                        'default_value': 'ϩĒƠ\x8a$ƐʊϫˣâÍĪЋӥˋΩưɑɡɟǬƦXÒţŠ\x9bӐӞͰ',
                                    },
                            {
                                        'key': 'ʇƿõӊǁњҟ˖ԏɶȧʛŦƱϻ˵ċʤҧϪ˂ΙőϜ˺\xa0ƗÏΙ3',
                                        'description': 'ɚѦЏԨʧғʎиҍʤѽоřƓӲ[\x99ǪŤƠΓʛѓ$ĢӋ?ҟОƇ',
                                        'default_value': 'ҀӤі°nƫʹʮƕѠě\u03a2ŘӜɯβƕїωϠΦɭĹìҝà·˾Ǣѹ',
                                    },
                        ],
                },
                {
                    'name': 'ѐΖɠӟĻ"Œ˅ȅɱӠŒŚ҅ӒƕɁЗŋѨ\x8a\x91Ʌ\xadƗмɭÍԡ®',
                    'description': 'įƗŖЃ6ȔǸÀӸ˶\x90ԑΆΪťʙƩ¿Ő®ˆĐ˧ӫƑƏјІг҃',
                    'target_id': 'ÏɦĘяʥӟӭȼ\x98ǷŜƾΓčœʌΠɀåÝΌϷ\x9eǍƦғÞ˛ѝǊ',
                    'parameters': [
                            {
                                        'key': 'ōɑ8pӅɌіӯ\x90ǕμƾãĠКαƻ\x7fЮˀɠӰ\x84ďǲЙ´ϩϐˑ',
                                        'description': 'ƔşΕʋҊ;ρʓ]\x92ĉѣě\x80ÚѹÐĐӏˬґѰĠïτ\x90ϯǒƧ[',
                                        'default_value': 'ƀϘĬƛʅêåÍӱǡǮψнđƠ\x81ȍʦνεʴƿŃЯͰЎӮɐЋȉ',
                                    },
                            {
                                        'key': "îңÌyșŵÐїҾҜĂΚϕЋɻ\xa0ӫ˃ʄưŲǔ'ǴҨξŪÄϮʓ",
                                        'description': 'κüӹÐӭǝѣɀɛɑˆҰʼȺǜQìǝA\x85ϑO˅Ǣ\x81ȵЛŝĐҌ',
                                        'default_value': 'ªÑƅˉυʐӏӪʇƂĘәЛÜɤ҉ѣmǑöͷMǈˉϕɃЖǨҰʀ',
                                    },
                            {
                                        'key': 'ІѽȧɄȍ;έҫϋ\u0383ĮůJКÞ¶Bɐŗ˫ŊҀѾ˯˾вЩÜ2~',
                                        'description': 'ϨǤĶұˡƟƲĻςǩcѰϳä=Oʬƫ\x80\x98˂ƓόŖĥβƎԡȠ\x83',
                                        'default_value': 'ЬˉϹˊӫȏ¼AʄҢҋɛƽµЏɓҤӘ·ķɆȵ˳жԇģ?ġиϙ',
                                    },
                            {
                                        'key': 'ɍАɃǭл',
                                        'description': 'ѯȈ¼˭ʕԌWҪҤϑȿă\u0379ϦĒmȾɺIЫòԊ\x8eЛӢяÕVƂĎ',
                                        'default_value': 'ήѣӀͼѦȯιҚƆköѦжǶҥ΄ȌжžˀʭбʋΟǷȊӱʸӿľ',
                                    },
                            {
                                        'key': 'Ͷ±вύҚȅԉ',
                                        'description': 'ИŢŏϒɩΡ˩ɪ9uЗɞϗѢοƯƒˑҌ!ðω\x8cӘƸҒ˜ȎœϞ',
                                        'default_value': 'Гò:Γǅԕg1ȵĈm\u0380ϔґȱȩϩӕɃЙҩȹάάӘɚʮʐǏɚ',
                                    },
                            {
                                        'key': 'ѳѵÕοv·ӑæБȋǒǩΒ1ѮЇѕ´\x85Ƌˎŭɣɜ˕зˣƣƩΩ',
                                        'description': 'ϫ8ÙÃК²¼ԒӦĉёԩүċŭͶԣėÇϸȥhˌĭʇľӵƍǱʰ',
                                        'default_value': 'ЦX˞ȿԎǣVÊÉƼǀɞԏǎҋ{ѸЌЎҤд¨Ĳ˅ŷʌũϼɵԬ',
                                    },
                            {
                                        'key': 'ȐɁҰЭшļӍϡȊИ¯ԢїЅŅƚαƀƮ',
                                        'description': '˶ÔԂŨŪύѪˏƋĉѵŪ\u0381İюá˒ί£ȁőǗɈʅƋɼбЖȶɊ',
                                        'default_value': 'ÏΒΊ¡Ŀ\x9bˋірƠϭύѥϬɓѪτͲĸ˼óхΗĒѨǲ\u038bϩϒϛ',
                                    },
                            {
                                        'key': 'åãƏɘͱӲ8ҢӵҥpТԏïҭӄƙǞȧɫĦ˥ǏѱƇщԟʎͼ\x9a',
                                        'description': 'š\x7fѷӕöƃӐ\x7f\u038bцѬņzȕĝΣōȊzŬǤ¢͵ʇ˃ǜΩȞË˔',
                                        'default_value': 'ЏӜӾ¹ʿɶә0¢иϡmͱғ08҆ėЗÂɼ\x9bЈϧßwĎӟѵǿ',
                                    },
                            {
                                        'key': 'lɼѦхдȶˀӤǐʹϟѳͽԪʱϹȷӧWɅˤď3ˀÙ˙ìĲψΔ',
                                        'description': 'ǋьӮ;ĩЂԉ\x9ftԬӿNҮƜԜԅ\x81ħԅƏѥȘŕϸƇåđŵˎΫ',
                                        'default_value': 'ԢαԂƝʱӼɉĎƲοŋ4ʹԫļʸϽԗҴДŎм\xa0ӑщʢĥŭΆƓ',
                                    },
                            {
                                        'key': 'JЕǮΉҀԀȈʿǮԘҘ¿ϿӞ\x93ґЪáѧāΗvŶԎưʘƜÎɗ°',
                                        'description': '¢˭ɠΎČÇ˻ЎϪˊ\x96˖\x9cĔİΡƕǯϚ\xadʐԔü˳\x97 ǗeǋĨ',
                                        'default_value': '§ӅÇӢΓУæ~ʜĈÈƍѾίʡП·\u038dɹǾɪϊŸƻʽӢŀƽ~į',
                                    },
                        ],
                },
                {
                    'name': 'KŵMϙàж¹˃\x8dѣǹēҁȾζΑϰћӚάoä\x9cǒĂˋǁǰÑѺ',
                    'description': 'ùƆЌBǝ\x85ÖɢϪʱРȤӰĮӞӈ\x87ͿʾуĈάЁýĳʇөɣSÃ',
                    'target_id': 'ƽ˚¿ҐԥЍΙˀшǞǈƋƷRĐ\xadȅıԡȴЪϩŋǛĀɋͽÞӓĄ',
                    'parameters': [
                            {
                                        'key': 'ΌʺҝwuȣOɈǉҧȑvО¯1ĿԆķǇØ¶˥ɬè˥ѱvƕˉæ',
                                        'description': 'Ʈƺø1æȝːӡŊǬΡӗȠıě҇ƞľϥďūŇӫʖȹ]a,1п',
                                        'default_value': 'ơđïҤˎσЏʇı®хŤӺ¤ӵǁǈ×Ѿʃш҂Π΄˵ɾѥ΄Țɱ',
                                    },
                            {
                                        'key': 'ƿɳĔСϠŖͿĩɒʅǼͺӻϑMζҕйȵƀĵʀΊŒƐϝlВƌʅ',
                                        'description': '£ύúɄԖӄˋϭ¯ǚ[ɯêͽƕȧ\x9eªӘоtΏė¸ʡȝŅˏùѲ',
                                        'default_value': 'ÝӌǗªƹwԑҾϧYɊY˦ΗyoУǆȺӪȫΓµ\x9c~ȭÚġ˒Ҟ',
                                    },
                            {
                                        'key': 'ğe³HΚͽӰǺϥpΨǾµщ9ʊƲ҂\x9bƿŕξ˨Wƿɑ\x7fbɌȈ',
                                        'description': 'ÏɜƔԏюŻЖɢԛĠҀԛʖΊȇήϮДРӲ:1Ƥȅ¯ɳ\x95еUƻ',
                                        'default_value': 'ӍЌԠʴčуέτʫҲў:ѬɻŀӫȳЌǯ{hήšʿĪɦȶцǉ˰',
                                    },
                            {
                                        'key': '\x8bԌˎӁ¯XưѺїĚsҟŪͲȑű˻ʟΣ+ƫЇҷ×ěƼВWζÂ',
                                        'description': 'ǘüӮ\x8eԍ˓ԚΓǓ\x9d¾ƫѽ\xa0\x90ЃĹűƈǐǙ0˶ʭǡԕԎɉϠ˛',
                                        'default_value': "Ҝ\x9cӘԨʟƩʝűӛԖã\x8aҰϬȽ`Ϳӯ˶ǛƳwŒ\x9dĊ'ĈЛȐȴ",
                                    },
                            {
                                        'key': 'ˍҪλӭȲĮΘŸΠ:ÁȰԨɢʖ²ȞΓǞцӴƨĩ\x8aJļӳȑϢP',
                                        'description': 'ƓŻ²Ѧ3Ũɡ\x90҇ҵZřнɔϢϒ\x83ɿˣaģωɹ΄Оӓ˛ϔɃӗ',
                                        'default_value': 'ǈҬǪɞЋӥ§ɝơ¶ʔԤԒſɰΟŁϖíѓ\x8eɅʕѪŹ˪ɣʧ!Ƕ',
                                    },
                            {
                                        'key': 'ӣǌӮĔŧŤΤúˋȁ\u0378Ǣ½ϑԗЁȎěʓБiφ\x9cƗȭѭҐǧʓө',
                                        'description': 'ҁˋOƓѩΦѿԝÑȅȂɂʻԗӯ&ĻèɛΓ¾ԑɵ\xa0ǳˣȄԩ҅ĵ',
                                        'default_value': 'ҍϣоѳ©\x94˯ѻŮÓ)\x96ԇɠʮ25ˍʂѡ\x99ǙϗЉʣӣȧư6\x97',
                                    },
                            {
                                        'key': 'ȊĿΜȎʘԗɍˊԥ˼ѧрПÂΏ\x84þWϰʬƢǽқȝȃĶʔ˙!ҫ',
                                        'description': '!ɐƋӦ\x99Ѣ΄Ӂ\x97Ńџ5˝Ѱѷǎϰzԋ\u0380ςȤѦΡŬɟϮʘɬɁ',
                                        'default_value': "Ɂā½К;ωɇѼǹ?ʍRʀşȸȲƶ'ƬΖãĩ\x8dòZĤȻÑþҡ",
                                    },
                            {
                                        'key': 'Ж˪ūԎґѶʙ+ǹĹΞ҅vǸΎЎ˨ŉĩqɼǷc¯ΠϒѬҎʥŭ',
                                        'description': 'ŴЪ˼\x83ϯÄȟ;øњĩōȘźɨ³ŴЬЛŢΤҢθќɣɿʟӽʫψ',
                                        'default_value': 'ϫӝχĄʨԊġԞōԄȄ\x9eΚƈĖ\x81ϣŬ¥ԗͽʿҁɞҢǂ,ûРο',
                                    },
                            {
                                        'key': "ƛƒЮɩɽӬˊҸƥŁѻǍĸԛ'МëɧȚ|ȭǬ",
                                        'description': 'Û]ƉģˏԜШƝԤƙТˈȀʻ\x93ȗӝɐĚɡ¿ԑ5ϴ¬Ì.ʸĜk',
                                        'default_value': 'аƟͼźƙˋȻZгТOҚǛʲĐөϦԚӉ҄B»\x7fșжˍІӀ4ˍ',
                                    },
                            {
                                        'key': '˖6ľӮɃӱԛӰȲǗ˾ӄRUӫ˖ʯĹ\u0378ňҪфǲ ǹшˤ<Ċ&',
                                        'description': 'ϕ˅Σ*ԩҤɝˠȝõƶƦФΕĚǳҨƢ΅ҙ\u038dԠĻ\u0383ӅžʂѰȬĀ',
                                        'default_value': 'Oĵ*ψɉ˳źϓŅªǭθ·мɋĿгӐԗΙȌŸĻˍŽǖ×\x8aȋƲ',
                                    },
                        ],
                },
                {
                    'name': '˘ҟѣϥˇӕīȒȞǐӭ°čOƦăɻϣƌ˳ЙћϐЇǷn҆ǅǍ˝',
                    'description': "ū§\x8c'ȹʬʠ˜ΖȮѓҶ¸\x86ƴй¾гǛǛƭʠέÂèӦӬΖ˸ʩ",
                    'target_id': 'ʼăÉψӀΧ×ԑӯɶҿВǪԭͲѺǨ¶ĹäͲЄʖʔʹн4éщġ',
                    'parameters': [
                            {
                                        'key': 'ÄoҁKǇɶΜҜĮĦĥМ&ɥɎҏʥ˳ȵѺƖёѼϳϙʷϔӕǂq',
                                        'description': 'ɩÙεӥŉʫԇҒѸĢԟ1ѣ҈і°ɂљÍԑƐˡҝǖÍѾѲk3ԁ',
                                        'default_value': '϶Ǔш©¹Ŷʷ§ȧ³ϹŧӜɵƀқƳʂӧϴԈ˚`ĺȱҩϳɼҵǚ',
                                    },
                            {
                                        'key': 'Єʴϰĳðĩ˘°Ɏ˞˅ŲђӠϴſԏɄηΥĈƫŨ\u0380ПnԒӑűʘ',
                                        'description': 'ĘA˭\x9dԭ\x89ǁҾ»Дϫ˙ƓW\x91νʜķǶäϐƗǣѲʁԄѷfȁΡ',
                                        'default_value': '·ӀɜΛӷԘȺзWçҮˣ<ϟǇћƌҥцŒҊάϔüμʓȴϕɪǫ',
                                    },
                            {
                                        'key': '҅ʁӖҙфƙäǢ˽˵ʽӒԛŇg\x83ќřӚÊvȱĳ°϶у/ɥҀе',
                                        'description': 'ϫтӒϾƢ±щǾШЯ˧ı˳Ӊ\x82ϪҨh<ʯǕԎͻӨȲÄĲ͵ǔ\xad',
                                        'default_value': 'һ¿˳ΰΠИƨʝɘԬКѺ9ɣɢϽƺϬҫļ(˗ϢШҼþтŋΒß',
                                    },
                            {
                                        'key': 'ƞ\x9eȻhпԪӈɕơʛƻǌƇѥɽΣԤҫӗȈ:ˌԆwȅюѓ˲ԂÆ',
                                        'description': 'љÆÇąѥ^ʭͳĉ6ÍԚŦäŃŕƆʚˋŊδĆӒ+ʘЉǐʨÞΫ',
                                        'default_value': 'ϜĻǾƙňɮʥϻ]БȰɐɓϩԦɆοпчʧȴШˣѳȇ\x8aĎǮƓœ',
                                    },
                            {
                                        'key': 'ϞȡҷѸDȺɊͼmĥє˂ǾȪʫ˫œӫ(үбȕŚΎ<œԃ}ǍȻ',
                                        'description': 'ҔÇЮԁлϪĺʠԇgͲɘҍӛ˖Rțѱ\x82Ͻӌ҈ιKǅė˵ΪͳϬ',
                                        'default_value': 'ƝҶɇȗȥǬː\x92҂ѳƧ˓ŦǦɦɄÂjɾŊҖƦê҈Ɨ΅ʕͳ;Ҳ',
                                    },
                            {
                                        'key': 'нȎʑʶǊȎȾ\x9b´Rʺ\x9cуɩҬɀϼƋԁƺДԂю\x96Ҩ^Ȏҽҿć',
                                        'description': 'ˣϓӘŧøбȇÔÖdǬȿʣDҐV¶ɈOӭɗˍηОȚ`L¯ˬҬ',
                                        'default_value': 'ԑύĭѸЙԥÍΔƑӧʕΧ˨Ϗư˾ȝɔįɹǾŠÕϿҨþȋѸģþ',
                                    },
                            {
                                        'key': '®ӭȺԛ`ȑєĽȱɖʯкбɿ΄ŷƾċӄîбđǢŬҸZӢÒίѮ',
                                        'description': 'ʩnɘԎȟ\x7fňҽƭǤ\x99\xa0ϭьҮ#Ñ8ƴψΆˍԆˆƦǣɜ҅ƻ҅',
                                        'default_value': 'ʖʅĆȾоŚõȇѡʖÈӤӖσԆ¿ɮȢҧșͳpĖˠŖ',
                                    },
                            {
                                        'key': 'xDΞá',
                                        'description': '˂ʱвɫșԡĻǮǷƐŋſǙ]ӛŃϾĹ\x92ҳɟёΐѢĘέŵԂɧǻ',
                                        'default_value': 'oȸ\x98ЫçũŌ.ʏ ɬɖҧϦϪCːπƱƆȾҤ҆½\xa0˭ƣȲƩ\x8a',
                                    },
                            {
                                        'key': 'ĉҿϢϖ2˓ϴΎƹ°ɦʍɔ҅=Łь%-˽ʸηąӸȒ:Ӯ}αѠ',
                                        'description': 'șgȢҳёʖƴє˕ĊǖƍʱЁȟ}ӛБȘύ;Ǫі9έɎЊԭæѵ',
                                        'default_value': 'Ľƴ\x84ȓ³ҭΥκ\x9eΗőôхơŻĂϏÐͽҜ?ΤƘÂӞіХԤ҈Ⱥ',
                                    },
                            {
                                        'key': 'ӫѝΊӍѷӈҖ҄ǺӍĿûЙȖ¶ϚӲˠφɄƬĽ«ӘȾӂeġҬԙ',
                                        'description': 'ȍȑǇΰŮϦ҂ƹΥʰԬ˱\x9dåˋǇ\x8d5ϦŰūȏ\xa0ǙϓǋȹȊҟϒ',
                                        'default_value': 'ǘǒƐɤ˸śűǨɥ£ЛƹҕǧÈfϔχzř\x8fӭǟԑȿљѥӱӴE',
                                    },
                        ],
                },
                {
                    'name': 'ƁӠѐϾBƽ\x9dԉ¶ȡè¦ѶȜϥϛЍћɮˆѦÀʄƆНǞ<ӹǸҊ',
                    'description': 'Ԟƌ҂л7҆ëӝҷɷӛҧҫͲП¥ĔŐϕѨĉ˗łвĚƗ˭ʪɶϡ',
                    'target_id': '˥ɋɍ\x84ηǓǟĚ@ϽѴ˗ǿ˵ϊȚͲɰŃКΣ\xadɝŀеŞұį˽Ŋ',
                    'parameters': [
                            {
                                        'key': 'ˣɁѲɅҷυԕɄȂӻσƥǆʜŗөЩ¨єАѦ*Үàƒ²ǡÇΈ˭',
                                        'description': 'ԕȄсъšìԦȀ\x94ԃ˥\u03a2ѰÂƵЇȵŋӠͼf˂ҕőŧ˜ʿʧԂʚ',
                                        'default_value': 'ӣDîěȯżϨ˙ӚԊƪԁ\x8e҇θţɗʭȻϟńФͱˊҡlҴͶΓM',
                                    },
                            {
                                        'key': 'EѣʄǀɄWƴƇ;ѼȤǶƗŵҒ+ɢϥɮ˜˟ΛӔԕӎ/·ȿƅ;',
                                        'description': 'ͶȠѭɂǱïeхλѾɈ"ЅőɸYѰşϚƗĒ_*Ƀ·ӛЎƾ\u0382Ц',
                                        'default_value': 'ψt\x9aƺƹxʮёĹĶқϝɏ6ӻ\x9căԋϊɛǹβмԏюKȟȠS˾',
                                    },
                            {
                                        'key': 'ҡū\x9bдӊȕBʊԭqϸƎ\x95˻ɨŶȃŬҝρшӹӲт]ʶϔĬňԩ',
                                        'description': 'сĀӅżəĵƃԫO˸ΈŦΥƧӿˮǩ˴ѢĒƻËдӢжʥèXаɎ',
                                        'default_value': 'ȪΜɣǁҷ}°ˬhάχ\x9e˺ĘҺNʧɋҧK\x88Ȑɰԉ\x9fŌЏʗǨƴ',
                                    },
                            {
                                        'key': 'ΊźÎͰԒʗİ\u0379Ł',
                                        'description': 'Ԥɭ˲´ѱɎĬѕULĬϖӻéЂǑЮԕǥφǻїұԨʭԣωʦǞǒ',
                                        'default_value': 'Șϴȕ҂ѣŕΟȱНƃҵӲʒҳăϐƔåʋ˄ѻҿϥƘη˫ˆӗИѵ',
                                    },
                            {
                                        'key': 'ӖźҧƻΨĹҏǅˤёҸ\x88ӧÈȣѭҿ',
                                        'description': 'ƅʪӊάÀЂ"ƪ˧ΪɷŪϯÓEI\x94ŏzˣʇ҂ɄǧЧ´ýɥӡʺ',
                                        'default_value': 'Īһ\x82ǃǙǆÄМʦφĸΞ;ˈ®ƌҜǒҪęȎfA\x99ǫìgɭóʁ',
                                    },
                            {
                                        'key': 'Υȅȭөъ˷ϴāȳɨъŌŏőĖƤĳг˶ɻBŨƻɓӜӼĉUĀΨ',
                                        'description': 'ȢȽǍƼҫЃʍƝӾΝ0ҒƓΎ˭ӱΝФͿʓҵ\xad\x8aoϫƍƄɠɽƳ',
                                        'default_value': 'ðӴӌӁɫҜѫΊЎʏ\u0378ƠЭÌǬĦƀ˼ԧ˘ͻхΨʓǕ˓ԬDҔļ',
                                    },
                            {
                                        'key': 'ҔӋĩˢʌȂ@ÈѼВô\x9cϋ6ȰшɒɴŤȥзǓԉЗ˕ŭ˫ȒҀͰ',
                                        'description': '\x86μFԨЅϫšØJǁˆǅѾѭǋˁҧƄŠǏЕӓɱəԖϧљ"İϚ',
                                        'default_value': 'Ȍñɤ\x82˶\u0382\x96ЩŐǔƂӊΈϨǜĭѕҒϕӌƽǽђÀͿàъĂŰΚ',
                                    },
                            {
                                        'key': 'ԖȈ*ԑȽæжҫ҂ı˴ÙӜӗ˖ϮɸĔƪʫЩƶӲ§',
                                        'description': 'ɜ˚Ȕԙ@А·½tԃźВȖŬɟ˙Őӓőċ\x88ōɇҹ<ϐlʵ\x92Ϲ',
                                        'default_value': 'đŃӪнɬ˪ӨɆɤАҲǒϗɚоùɐŻĚӟӰ˟ʘɭþƲцǹԑɡ',
                                    },
                            {
                                        'key': 'ƗϒӅʀǷԪLɆιȍĥϛǕʁĵûËȍːɫԂӡѯѦ?ÆΪϡ·Ѭ',
                                        'description': 'ψßӍƤѠʎ\x8eƄ\x90eē=żӎzѕӲʗȖʜθêɎĥȠпGɅϮ҅',
                                        'default_value': 'ΝBϙŚɾҶԝЕҕƲČ½ԌӊɷӓÀƹĉȄжԧТPðƁǈϋЉҳ',
                                    },
                            {
                                        'key': 'ƩƪϥРяӝǚҶ\x88yҐʰεт?ҭǢԩūƒ˫ʿĲћˀϟҢ¼ɰЁ',
                                        'description': 'ñЁұѾӴ}ӫѭϖǶŨϑ˲½ҟшѝÚhɄȵ3ʦǯ(ԄʄŠĳҮ',
                                        'default_value': 'ϤɏΣ\x85χљʊЄџ\x83ɔҫǩȭԒҨԛ[ѵӼ˼ƣҖňƨ¡ȢĴνғ',
                                    },
                        ],
                },
                {
                    'name': 'ҼʉЄӜÕĩ˒ҸʣЌąʴҼ^ıΌΝ\x9dӦħ\u0383жɮΆ\u03a2ˠêʱǣΒ',
                    'description': 'È˼ɻӄΒ˨ЧԎћʌϭӫɲΤȫ҄Ԛ"ˢ҅ȐňÓϿãԁȭѴµ˽',
                    'target_id': 'ӬƳλĀɃǘƳģǫ˥АΟЪӻϗʆ$ȓЁčɌuǞ҃\x87ΞƬ×ԣͷ',
                    'parameters': [
                            {
                                        'key': 'lŐϔԌȽΚÎУԋ\u0378{ӟҼǡčħąȎĴȕ˃ŉȩͳə',
                                        'description': 'ɮѸĹŚнʔɹɀиŬȂжͼºͺųŔЗȈғěӮѝҍӈ҈\x86æ\u038dΧ',
                                        'default_value': "pŨǪĿςȼ\xa0ҋӤΩ˕Φѵ§ĞZӗ˥˙ƏͰɋϺӆ'\x91ŵΧϋԭ",
                                    },
                            {
                                        'key': 'ƸĤȰĩȐÂʌƢϾһƖ\x8cƗȤ\u0380˷ːΧŏƭƼԑ˧˒xƯРˈǊĭ',
                                        'description': 'ɯé\u038dʚΨҍǂϒòè<ˀӔŧȹeӋǐҋҲϯͷ#ȿ@҂эԥˑИ',
                                        'default_value': '²ĩϋԗɵǕ+˾%ɋӊҷћǐѮͳ2ԗ',
                                    },
                            {
                                        'key': 'Ѷű҇ΏˈžBôϛƣ˅λ\x9aĵȖƔ˗ƙľǖʚwàʕȺѢЖäΓǿ',
                                        'description': 'ãȆҊ\x81҈˜ԥɖƁȤИηǫŶõЊ=вÌŹĹҁɐϓҠěĖɅüð',
                                        'default_value': 'ԇķíƻ0÷ȦΎɧΈOԄˍόĽȪЋŨфƎςϽû˃ΕʱЦ=цш',
                                    },
                            {
                                        'key': 'ŬжθŴć\x9c˓ʹȤx¸ѹԏˮɚ˺ƭÎɾ¦ñʋԪɸԓȾɯȼųҞ',
                                        'description': 'ʪeŔϕʿҾőˆ7ĴЙɲҊ\x99ưξ²ϊѺцȮϝƵЎћɀÕˑЎ\u0378',
                                        'default_value': 'ɏɫ>ɝȀӿɧą±ʚӤӃưȐǹБЧȻԧʕȣϜЉҤǐőԩ&ɽϙ',
                                    },
                            {
                                        'key': 'ˁŶ˖ΈƼŕϨÁϬԨϦ²ϭʭS¼ȧíԓ',
                                        'description': "¡Ϟ9ʾSҗОϦǥ'\x84ӚHÍƱ҄ӐƔӸȓɫҨÿрĳԜӍʩƒɫ",
                                        'default_value': 'İ҉ĊɖΛµĔ\x9cʴºǰēȋqÅěɢŲǣÐɍŞϺȩϪ{˅˫¯Ä',
                                    },
                            {
                                        'key': 'ȥ\x91ʜ\xadNȪJѴOıѨϖеƌĜӜŊúύ˔Śыҕǐƛ\x95ϱҽϯŶ',
                                        'description': 'Ė\x87ʖӻˑК˓Ы]ЛήȝҠѭѡ\x9bȳʟь˥вϱ˝κȏѢ¸ьϮä',
                                        'default_value': '˩ǅʬϋǾǏWҚҤŀΑśɐ\x90өιӲԗŹȬԁзŖċʙ-ǳ\x86ƴШ',
                                    },
                            {
                                        'key': 'ȩӪɺʹѹґÖ˴ћźĢ˞ȺŷˬșāɃȭͰȟ˃ҘHɗԔʤә\x99Ԛ',
                                        'description': 'ʁѫюҁqƎԀƚӦIԓ!ªʋūˡϋϊӒҪºƮνɅʣјϩUјŕ',
                                        'default_value': 'ƕъʥĀΈȊźРƟӫŉƲϐ\xadɢȂԑ˔ɏΠӒ¸Ύϋύ',
                                    },
                            {
                                        'key': 'Ζ¸ɜƫµʇÕśgҗʵɘѧư˭ˀÅƌǧɸ\x83ҀƑωЍѾĳȢ\x82ф',
                                        'description': "ʡ˯ć¢ҋĺ҆ŲҭĲʴɦҞ\x84\x87ԧœԞßˌΝȟ'ԍϝʫǥҩUЂ",
                                        'default_value': 'Ȉâ˙ǃҖȰˋӤʼΤˠϭÉώЕƹ͵ţѵѨЍħĎ®ǦÝϓԤά*',
                                    },
                            {
                                        'key': 'ͿƛʫɃɌ§·ʴ÷ϱҦAāϟƴȷŔƈƆƣŬ¢ӕĜ¤8ұҵԨɥ',
                                        'description': 'ӟҶƋҲӒÅ\x87/ʦФ¾ʣʅǔȾϾѮʞђȹшĨŵӖӭľϗϋ˄ɠ',
                                        'default_value': 'ϪƉӋЫΘOϊПЮґѴčũҵʧýңœʙͶŀɬȒЏ˓əѦ҉Òʡ',
                                    },
                            {
                                        'key': '/\x9b\x9fɡУɼЍbȫӄϢфѦȋԕʞӹZzŢųâȑėĴǌѭ]Ήϣ',
                                        'description': 'ƞӮҿ\x8dÄ˽ʅӆĿȘȎƁȞãƇөнpҲʸʻήǘƏФȰɀԌѴ˨',
                                        'default_value': 'yɗ˴ϲϝɎǽɝ\x8c+ȬļϧѯПԑͷӒëζʢϵţӃԟ\x93\x81Ⱦŗǚ',
                                    },
                        ],
                },
                {
                    'name': 'ҺӉǀȕü΄ơĤ«ҤǂԒŪ/ůʏȄǏ҂˃ſïԆşɋ\x7fĘȥ˝Ɓ',
                    'description': 'ѩêΘ\x85Ӆ΄ǆԠŴɝΒŦϠĴȑФØîɟȵƶҵϩĶɯǹy]£В',
                    'target_id': 'Ǯǵù+rгʷΡǡɰѫÖǶѵ˙δʽ×ĶǌʁpƻɒϺÚĝҜɣƈ',
                    'parameters': [
                            {
                                        'key': 'ʊǚДʏτȽƹɐ«ԭƃƒѐɿÉĚї\x94ǣϐĂęєĢϏуPЕxȴ',
                                        'description': 'ĬǙÃӗĘ΄Ԩӱʼ\x9dѕ\x8a·ǃѣϐůȤӸӂǹʝΎyԅ¡ұƮϾ˞',
                                        'default_value': 'ɣŖȡε˫жƙʤϻš2Џ˜ҋɪǯǽʰЯҘȧϣ\x81ŻΘƼăʌ˪Ͷ',
                                    },
                            {
                                        'key': 'ȿϛʫΉȟɳųʐјӄʈԐĄԫ˜AҥéΖϼΊ]ίȁѳĆӔҹ\u03a2ǉ',
                                        'description': 'NɗǵХɞʚҁsψřȀЂʚ\x8cˆ\u0381ү£ȶњùʌ˝ҨȮɄɐŷԫӒ',
                                        'default_value': 'ЈǟϺϡŖȹ\x84ҺfÒѰѕɹϙϟͰЭˤӄĄǅE¶ђ÷ɱͽťɚĺ',
                                    },
                            {
                                        'key': 'ϸȦƿУĐýϙ',
                                        'description': '\x88ˡˈ\x90/ȋlĎĈǩ½ɘԍ1ӌƒKИĀІӠԅĭˆɥϽǔ{Țџ',
                                        'default_value': '2ʞ³ĽƨǼуÆ²˗ĜɣȪŶǘϩXÁȅкʾ\x8fAȆƶԛʙЍʌӑ',
                                    },
                            {
                                        'key': 'ѓЊɟ5ԒƷЈЬӿ²ŊʩϥѰǢҌҕˇәĵˈ=ҙÓҍ>Ԛɜҵϔ',
                                        'description': 'ɾ˷ĕźƓɤĥȐƂһ˻ŒɡήǪΜʜȻІԗЏӆaѽѪ\x9aӾҏʴʊ',
                                        'default_value': 'P:ó¹ǡȑѱƳñҍʍÇԜЫЋɗɣǸΤɲхΤɭȉČ]ƠяпҺ',
                                    },
                            {
                                        'key': 'ӗĲԍ$Ǽeџ˔˯ŗǆ\x8eψΜ±ϛɟÂҤĥ҃ʜɶüñȔϾżœӡ',
                                        'description': '\u0379˷ԪӃɣѧҾЮƗʄϾҷɶ\x80Vàвˡѿ˴ƘƵ7Ū·÷˥СЊѨ',
                                        'default_value': 'Ĥţ\x8bˍ3ŻˋЍˬùГƽʸѤ<Yϯөğ-ǈ@ĶюѤӡǐΗžӯ',
                                    },
                            {
                                        'key': 'њ@үǯƂˡǯōʙ˾эǤӀҏWāÿԮɞƒԡʞÁ\x96ЇυĻaȫͺ',
                                        'description': 'ӒΚʹɑӸƀɍǓ\u0383·ϜƱԝˤͱҌΚӗ²äҶȳԣŧřӺǬ҄˻Ĭ',
                                        'default_value': '°ŐҌĺ΅Śǟǵђ҈nЖƋ\x7fǂȊљƄȂƅα6Ӗҹ\u038bҊϿĖɈӳ',
                                    },
                            {
                                        'key': '\x9eĿ½ΰǱȐΩϘηɴʰ:˂Àӊ҅Ϥžɳ¡ũѹȮɰҦΐАϝϐќ',
                                        'description': 'ȸȾӐŋЕƣɏuåHԛʟ|Ɂ\x80ɚґЧȗĕŇΣϖэϔϖʝΌѾǹ',
                                        'default_value': '˕ĝĖȞнʸɨ˟ԍ^˩ʠĶX\u0379Žʚ©ŗΖϗЁӵєȬ˛ʺ\x7fѺÈ',
                                    },
                            {
                                        'key': 'æʀȋɳħsǼ\x9bçӿƫŀƄƍ\x86ϝƖV˲ȊϻƱʡcʨӺaВьҍ',
                                        'description': 'ȔȂƒωȅІńʱХǈͺ˭Ŏ˥úԖѳş\x82ǐŰЯϛ?çϢ\x87Ԟ&ŉ',
                                        'default_value': 'ǘҝȶȩºжηYƉϹɂǡι˖ǀƅ`ѭ@\x84´ԑ\x95žăʚƩ\u03a2ÀH',
                                    },
                            {
                                        'key': 'ʹϧВʈÇӗņƘȳΠËě˶\x8e˝Ƅ҆ҶľˏͽȚƻΞȟ˽ӕԓǸД',
                                        'description': 'ϳĔӓȮʷˍÛ˄ίŲŦђнīDȟďŭȣ·\x91ǑФńΜӷˢӀҥĦ',
                                        'default_value': 'ǓԨһѐʻȕĐаZǦȯѿɱʻŝîĶƕʇîВ\xa0НěӳԬ÷М˺ұ',
                                    },
                            {
                                        'key': 'ҍ:ϷϷѓΗёФ\x8boť˥˩ΥϵʧȪļμʞƍƂӗĻÐѥĕʘȖ˜',
                                        'description': '+ÄѷșӇɓȏGʻwҸʼĄΌɃȹʔ&ӒȔυσǔ˒ȫȅɾϮԃɛ',
                                        'default_value': 'ȇɢĄӘɼɷđфҎʑҼǙӄöȓłʯ*ÔĮɀ¸ҋégĠǲk¼į',
                                    },
                        ],
                },
                {
                    'name': 'ԓ\x83ǋʹЮ˦ӑ\x8dåŚʯϿӧиӰ',
                    'description': 'žľϪƲŗbƸɖĊĥƼϟЅ\u038dfσĹҧ˷\x86ýӉu¡ƪԬИȕñų',
                    'target_id': 'ˁȷȍ\x9aäθͿȊϸĆҥӭ˽ԇƆΠξNJҿϩ͵ňιƶÛςâςı',
                    'parameters': [
                            {
                                        'key': 'ПϹҺУƳӬyɹǹ\x81ȳǌͿɸƹҍ ǌ',
                                        'description': 'њ,ȬȁӄɽӆͱҖӘǶ9ŷӚκҶ®ѿäӠԕƠ˯Á˨ȪëЪ³ĕ',
                                        'default_value': 'ǧįҡƁԣĄҷԏϾĚ\x80ěʇѺΔӣѺλϙ˃ȉ¸\x8aƁӥɈʭKѤȢ',
                                    },
                            {
                                        'key': 'ɳęΔЗИęϕı˅\u038b',
                                        'description': '\u0383³ɭ)ŃĆϔсǗɘǧǊȅŉϨФǮӜ\x80ɫЬȞƟĮǯҁ˜ϮŪι',
                                        'default_value': 'Ҿx|ӑɡȤ\u038dʌһȾ˔ǽӉԅΡeĕ˦τʊŒ)\x8eЧѥ˵ʺΘӎǿ',
                                    },
                            {
                                        'key': 'ԋǛɏǁʿɕαРӶcϖҏӪҳȕďéӄȚӮ',
                                        'description': 'òԠƨǧѼ@ɩЊҎ¾ȔǚԅʩϗʑʅȈț)ȆμðˣąЛǺVĲ˲',
                                        'default_value': 'ǚ²þʀǀɫ\u0380fưǵvʵҮŇӋ6ˡυʷΨŌʤâƘǐ\u03a2àӷ\x93ϸ',
                                    },
                            {
                                        'key': 'Ƈґĭ¦SŘ«ëƴУʰɬϤđє',
                                        'description': 'ȶç?ӤɮŹԅ"ЏӽѻϊĹĆʇԫǥϠӑźɘͽ˒λҮŃŉЉʿ°',
                                        'default_value': 'ɇˬŮʻёϤҋʤсҗȏȳƮжҹҾ\x8eŽͰӳʧѻҒ\x9eģͿƠΎҷ͵',
                                    },
                            {
                                        'key': '˰ϥɡАəϟǣ>˔ȩҳ҄,Һҭ,ɽǂɁʊ"2®ϬȘ\x8eȶǁæ¾',
                                        'description': '\x86Ѝ˳ôчϋŨȔŻØԥźȤθҲкӰ\x96WЧҁųѠɖϯьƁǰψи',
                                        'default_value': 'ӵɼƂýĩһчǵɣ\u03a2ӈԓұçцϓϠΘȥм_ĐϳèҷΪǷε²ʥ',
                                    },
                            {
                                        'key': 'гэˮѳұ˩ӱҍ',
                                        'description': 'ϗɘѐѯ',
                                        'default_value': 'ģ\x86¯ΉȑuǬvʽΨɢʟüҬˇԊҿ\x90ҖɃʜ\x80ǥңíȘɒʋХò',
                                    },
                            {
                                        'key': 'ǦŞQ3ȿњ\x94Ӑѓ ɵӲҬĮäɕȣǒǟeǳĦǜ¼ʍč',
                                        'description': 'ԛmʸȪʒԕɬǅ˽ȥǬ\u038bѺД҄щϭFZˇĈÏÍƲƩǏίƘĮ²',
                                        'default_value': 'јɊˎƢѵ˽ȟТ\x8eϒŸ6řбʪԂь^ӷКΞŗIƫƯɄФƅьŒ',
                                    },
                            {
                                        'key': 'wӈʌǭÝɉҸШeøƾЅϪŢ',
                                        'description': '§ΡԖԮųpă\x9eȫȶȜbgπϥʓ«ĵˎHó!O˥ǠȕRĚ˂п',
                                        'default_value': 'ƙ˵Ӡ·ϟƖԞεԣʺѼǽüԒģΑ˲ҵƛηÉϾČҾɄΙǩǆʄɐ',
                                    },
                            {
                                        'key': "Ȁ'yνƞĀʫȱөԤ",
                                        'description': 'Ĕ\x82ыϲʘȞѹ\x9fҍԇǝȉŕŇβŬÃÜКΆĸ˶ȑ\x83ҿԛȴΏɒѲ',
                                        'default_value': 'ӚΦ\x93ʸƑԟЍϊɬϒϡĢɕǊ²ÁϙήȒŉЎӧƯūоёԖѸ`ʵ',
                                    },
                            {
                                        'key': 'ȩāҧ#ҨiΣʮʩ\x88ɥω\x9bϳӺțҒʢá˯ƬģӇ>ȏɢƠŷķϰ',
                                        'description': "\x9e?łɴʍԚ˟îȑƭǠɊʸ'ϔ\x82ǕўȑЎȺǏǛTǹӍл˘ȶq",
                                        'default_value': 'ƳˬӹӤØǔ΅Ԯ\x8b£ǈμϐńŉȉҸлԕ¤ҫž\u0378ʋʦϋ˽ңѫ9',
                                    },
                        ],
                },
                {
                    'name': 'ȜοďɄͱɘžĵѧЗͳóѮˬʿǋɲϸƶĐý˥Ԝá\x98ĚÝ\x9bċʄ',
                    'description': '҃ƶѓщŒиşɎӡțѫ&φ҇үВɋƊҊ\x7fœӴŵ¤lJŚҤΡό',
                    'target_id': 'ėӵҦŨΨƻɡƱЄѾSVȸӇѣʆӵӡȜǮŞќΔɔ\u0378Ԙŋʐʾ\x81',
                    'parameters': [
                            {
                                        'key': 'ƑĩȕʌƉRÖǐϠőĭѽɖ\x91ԫ\x8bAҤªƬґҔӂìϗЊ΅ǝөʟ',
                                        'description': 'ƿҗԍŃʎħȳ\x9eв\x91µůǟĭʷ)ҦýԏϕřˆͱΈӷѿ˓`ƿǐ',
                                        'default_value': 'ϭоĿҖӞLѹщʵΧҩҴѕЏӆȁԇŨ҇ȈˏȪӒȻϝȡͲƩȅϚ',
                                    },
                            {
                                        'key': 'ЈƆѦyä҅\x8bЗɖåҴNUéӑ',
                                        'description': 'ºǵýɿΏǣcq\x9fΨþΣɗƫϙӳПȭͼЋǉθʏħǂëрǪ¿Ѫ',
                                        'default_value': '>ȏĝə͵ϢЛѱԖөΩΨƝǇвZȤҽЊTˎҠ\u038bɏ¹ѓȌǞİɭ',
                                    },
                            {
                                        'key': '˜ȹ,',
                                        'description': 'ÏƿҒˌʹԅЇ˂ÖkˡƂȪʖϯʃ1ÜʺҞʱdN˵ȶЦǾҫȕƤ',
                                        'default_value': 'ȍU҅ĭDӈӇӎŹϕņѫÒʽ˴ʠ˫ϪŤéαŞ\x80ҙӨĭĵμŜ¬',
                                    },
                            {
                                        'key': 'ЄƏӼʟ',
                                        'description': 'ΨɃŠǦ\xadɃ\x86Ƚ3\u038bɇͲͱȫӥҤkӀ\u038dȯПȾŗˋDăԜӘə\x92',
                                        'default_value': 'ŵ¿ûӂ\x83ŤɰԐЯğ¹ѴӐʪͻӭĆ\x96ǻČ¦ʚӎϴԦȗʤ>ȘƬ',
                                    },
                            {
                                        'key': 'tbӾīҌŲɡԞȌʇȀАΖyԢơ¸Ѐ',
                                        'description': 'ηİʟўǌɑǭԤӴ(ӹɆλ\u0379įø˧ѹфȮɎɅіƂŧˇјEӻӁ',
                                        'default_value': 'ĳ\xadϰΐȾtɲҁȈȢǈӡδČƼȵ£SѳĉԠ˶ъQΣ&Ӓƅªɭ',
                                    },
                            {
                                        'key': 'ѼЂӧŎŉiͲ;ϗVіʋӹѰåҳҳү˽ΊМԮӋʓĞҖ\x92ƆXЯ',
                                        'description': 'Ɏ\x88ʛаЗѰĎˊŪfԬǶӍǓЛҗӜИыѵϸĪĜНņ»pЗťҠ',
                                        'default_value': 'FˊÔǲƺʔΣϙΌѰʑŻӏшˉїϜȅԃɏԁͿÉɲ˒ȄȆ½ʠN',
                                    },
                            {
                                        'key': 'ǎ®ȂЬǲӝˏŹʄǦӱ',
                                        'description': 'МʿѴȱѳȉ϶ïɭϯȂϷ˺ӧaȻΥʈ(ȽƵǊɌ\x8eǚȄԜɆß~',
                                        'default_value': '£ғˍ·¦ǼŷŸӭўĴЧ҃ſԉɰ\x96ɰɩùń˘\xadϐƗҫԡȦǢȄ',
                                    },
                            {
                                        'key': ',ÎӇ6ӹǝУӷ®Ұ¤ëԦɿǙƴȏǳ;ʕΔøЙƹυSӡȕΫ8',
                                        'description': 'фԟǆɢʁϽOΡϚÆΚΦΚӻnȐǋǧЌƥǞ;ӜϠŭƯ·`Тʙ',
                                        'default_value': 'ǚɃɾӻɈК\x85еΎЃț)Ɛҋ\x90XÅєˬeūϯ±YԎÒ˔Ѯu˺',
                                    },
                            {
                                        'key': 'ԪѓƂДѸģ˴ʪ²υ˻Ů',
                                        'description': "ǡɲҖ'X˦ű\x9doԥIЧǦ=ƻɂyˍ҉ˀ\x85Ʀ;\x8e3ǋŨǙЗԋ",
                                        'default_value': 'ұzԨυǼêЋΆеҀ\x9fҊτɕԋχÔЫķƁӤҥǓ҂ϝϛӦZϘʞ',
                                    },
                            {
                                        'key': 'ĀϥíȈҳςѴɦАʸ\x8fʪɽΚÊƐőɒΔχ˚½Ƕ±˨ҽУ¾Öη',
                                        'description': 'Ӵǁ«З҄ˊɅԨʔwҵѺʴИǪЫχ£е˲еϝιьʕӶʫӧ,μ',
                                        'default_value': 'Ô\u038bИ͵ǫҵǎũǼҼЛϏЈӻďCȚöˮӜуı\xa0ӣßǥŔˡſМ',
                                    },
                        ],
                },
                {
                    'name': 'Ɏ&ԆřӝԓΗЯΐƮҏҾ˭˰ІΦØŽєɰǘԙΣΖΔѼǏѡĿȢ',
                    'description': 'ύWƔĴԈˠӾɚÇǃƏɻŤtҵзӞŃĹ¤э;ƽɹӬŁϤȱ˶Ѯ',
                    'target_id': '҃ˤҫɩΒəŢԟңmД\xa0ͱѼ˛ҵ3SҦҹʙѹ˸ȣ¿҉ů˸ѕ\x90',
                    'parameters': [
                            {
                                        'key': 'ԀʤȗĔѤƻѮӞ\u03a2ҐͳƳԖȑÓԆ\x82©˺¢dʂǁǴƏ΅ȾeͲҭ',
                                        'description': 'ɲǈΑ¡ś)ϝνĢҝƹԍŐ;ȝZ¾\u0381ԗȊĕԈϐÏɗéэӵĚҝ',
                                        'default_value': 'ßϋɿЯӣˁԟчx˜ѫĽăǆǻԀĭԧąǘТǿЧýυǂӜЈǸȋ',
                                    },
                            {
                                        'key': 'ʟʷ\x8aǽȹ\x84ɛϰƙjǙþ}ӏӫy҃ʟђŬĬŘ\x9fčÈͼмƣ˖Ȫ',
                                        'description': 'ţEԆɽɓɹΐʼͳȰŗ!ƀҋџωϧɻȳƆŶǖЗ}ҤƹɄԔÐϿ',
                                        'default_value': 'Ìʦʛ@ǄӦνιЬʱ;ϟǮҒƮʠ]ʨĵǷ҇ùʍŝ˫ѺϖҹƉɗ',
                                    },
                            {
                                        'key': '\\ϕsϫí\u03a2яŽùƬtţԩðʠѹ\x94jҖԩюΑʯӑƃ',
                                        'description': '>ԢίĚɷʗқɓ\u038bĐVӖȢҐɄˣ΄λùёҤϚѡʱҞΔԀsϻӲ',
                                        'default_value': '4ɀȹȭͷ×Ɋ0ѳʿɬӿʍвQщαǕıлѪћƽƀOǖćßӢğ',
                                    },
                            {
                                        'key': 'ҢǝŇӤɀѭϤʳǢĴƄˍˁΜ',
                                        'description': 'ȕɧƸƍĀΛ˞ПÐɶшвȟʥêίºƼ\x9d¾хÙΩ\x8aԊ҉Ӻʻԍǉ',
                                        'default_value': 'ЖȆЇŻΣѻʯЌȗƑΰҾӗԀȓǐ<ԍΌɂȑƤɣQťИӂļʈϯ',
                                    },
                            {
                                        'key': 'ʸĽЗĉα˲Ʈӵԋ',
                                        'description': '\x92ӆӘ)ʃΣΛkъӆˮҬĚȘЉУɁѴƠ5чӀГǇӪɥǚǱЕИ',
                                        'default_value': 'ȕɸǏШ҃\x83ЯƌіdʑӎϖƦцϿǰΉǕŊê\x94ʝ9ƭЁ\x9fɈмȍ',
                                    },
                            {
                                        'key': "țЇΉɔĨˇӺАί˰Ѐ˛ʖԧŨ[ʭaˈ'ƩԌɪǂʺ\xa0ȟԐĤɘ",
                                        'description': 'Ԏčǵǫb3ª°ƕѩ˅ѤKɰԝǲ¶ΞǢϙP\x83_лÚ"͵ǏԊƛ',
                                        'default_value': 'śҲȿχĢɌAӳύƲаƼҌĈ²ӹɀ)ƈł#ХБ˨ӵŕȨШӿt',
                                    },
                            {
                                        'key': 'Ŝ(ьwУťńà˝ʯЂâʷӷ\u0383ѰʒЫũƐΞύɴҨšƣЋã\\Κ',
                                        'description': 'çõǑǆӒɁХӤŋĀѨӦƉлǺӝǂ\x95ςɌÙ;æµӴlϿ\x8bβ\x8b',
                                        'default_value': 'ԭӓyÕƬʋъƥўǌ˧ŢԗÆԎǄĭьãШƎ~΅Ӳԃuёʵԟǲ',
                                    },
                            {
                                        'key': 'ΔѱˍщжҀŤɅƂʁwӫȩӀqωѵ#^\x88Ѓ\u0382\x9aȺҼԮӂϿUд',
                                        'description': 'ԛƛŃǺǔʛѝƌř˕ŌˆїέġŹ\u0383¸ԭøӏσ·ʆ˹ґʣҿҌˡ',
                                        'default_value': 'Ԙ¿ɚ˹zʝɳԨɿ(ΙϤʁҗѺ¢ǓɯԈҼmИϚʊӺŋԪ\x9d\u03a2ź',
                                    },
                            {
                                        'key': 'єӉƟӟưSϋĝҚәýӐΕɔΘǫøΡ\x95ƈś˲ҧϹĺЇ˶ÈƵ˞',
                                        'description': '\x9aɘόΜ^ǔŭȾŗϜǐϢҏ«èºȸϦȋļƫð-ǮäʄΪӪǴĈ',
                                        'default_value': '\x96ӓ½ҜӲƒȱTƖȱʽԭʛȋˡRǱФâςɪѩԘĚ=\x8d0Ũ˰ҳ',
                                    },
                            {
                                        'key': 'ʈ',
                                        'description': 'ɛѢɣӪǪЈˍǐžϷîYǉѸəƇϬɇʁʿЅӑôĵɔΝŲmʌĥ',
                                        'default_value': '5ƠȚʱԠϥȱαĖуϓЁһӫĩȷќƒϕƃǇʿ=ȑ\x8eôт{˧˛',
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
