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
            'sequence_type': 'meta',
            'keys': [
                'Ȥ',
                'Ҋ©ȋϗ{ĉǑʾɐŅ]ģʐЉ',
                'Gʎԍʬү˥ǾǩVLĤˈǔȉǔiŹǚӊϛӸѬ',
                'ʞʺҗŠŞаͲԄЫ£ɘƱÙ',
                'ĜʉҳρӷȺԙƳί*ÕɵΏ˫·ҵĖəə.ѓϷ-ţǵӝ',
                'ȶÒíҴʬÔNҮԫơżӐҾԍ\x98ĽЁ҃ÄέԚȡ\x80ž',
                'лŉʛ1ț?IΤԅɤϣͱϟωƩҁч˯ɗ',
                'ēÆǉƚxȭ\u038bӤè@ӇţêІƨ§ƳЖґԂďŐíɿгͽφ\x97ɆȨ',
                'Ēl',
                'ėāØϕƠɛǩĀɊӣӔȣϻȘЯ\u0380Ʃҹʥw',
            ],
            'comment': '3ɯȠæѩӦǺ.ȎƂȵ˃ǟgзԮӂĹcɨʠ5Éϙɳ¦ˬþÃĖ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'keys': [
                'ŗ',
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
            'key': 'ɿϕľȦȻķʈ',
            'value': 'ŹɧƕϢưΈӃҸ|Ё_Ϣ҅wʬҧϻёǚǲБʙĬөɅ\u0378ȔԉӰʽ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ѱ',

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
            'target_id': 'ӱȮɶ҄XπȱǻҎԜȜҩӯЄʫǒѵΝΛƸŸŉчæ\x9cӭԓϤŋϒ',
            'parameters': [
                {
                    'key': '͵ǆԍƠEӫÈʬʨvʲŚђ¹лҩҔȐƜєЇЗɍҋ\x9bĜĤʲɀȗ',
                    'value': '҆ʁµ\x8aȤ\x81ŞũːЂƢх\x89ʃ˰ΧÉɾѶˁÍ˩Ͳ˥Ͻѱ\x92ӅԄÖ',
                },
                {
                    'key': 'ьΎĺ$ΈƟЫԗ@ϗ',
                    'value': 'É˶RƸӦșþҖȐ˃ĸŸsҲӮψӏǇʆǚĦѨϚƄ\u03a2ӻͿĘúJ',
                },
                {
                    'key': 'ǲʥǡǻѴäGхɦŉśӋПЯåRΘǋүfƎŞҳÍ',
                    'value': 'ыѠ˕ĥî|џɵɽώȸӗaɑ˟˸ΔĹӿҵЋϧ~ҜДJΊʜԫɖ',
                },
                {
                    'key': 'ԕȾѽŞн˲ϡҒėĮơŀχԈƇќɫўθȡǺʥʊԒ\x97ϲĥɠɄȂ',
                    'value': '\x7fȲ\x8aãҌΒҜʴφʈԋʹУÏˁš©˦ÍËưˠЎòĳůȏьɌԇ',
                },
                {
                    'key': '\x89\x9dɕ˼ȌѕȢЌԨϻŃЪΕæžʕϠç˻ш˨ĎEĝƏΜϺƥŊΤ',
                    'value': 'ЩčϼȎ·ѨɤԘ¯ʠĜʦ˥§ϵɉɽХНϓȽÂȁӽȼҞɴǺɅω',
                },
                {
                    'key': 'ЯøďɤӶԛǸѝŉćƍƭQЧjϳńɓǣȔ\x8d˔ĞӿґNОξ˵Ȉ',
                    'value': 'œҁŦѷĴʞĲŴȊȡȉ\x9b×РѣĿĒҟϹПǃŎЍnԜЯ\x8cɶȈɻ',
                },
                {
                    'key': 'Й҃ʯЌҗʱʱ˵',
                    'value': '\x97ӖǎҡԇқʳƋƞҭȄ5ФϬǄőɗγӻȾȉʄцԤʯ;ϐȪЁ\\',
                },
                {
                    'key': 'ɘȟΧˋʈӭӹқα˫ҲšԚȔӂ·ҀȫѴˬɎŮJ҄ʊ)ǐ¢Ұӽ',
                    'value': '\u0381˺ԡѭȤ΅ˏãFaӻΊũΙΰΞєƺȨȝË^±ǁwΓǕϐԀ˹',
                },
                {
                    'key': 'ԣԄЇн3љӥĖŘτ®ӲЇӊП˯ϰ¸˂uҢƼӴŧŁNȍɳӃӿ',
                    'value': 'cǓǨóʩƽôNЃŃđПϔǖ\x8cѶȬҊϞҸĪ\x9bNӑĹÇŠΓѰè',
                },
                {
                    'key': 'ȧʼðĒЃёSӸȥ˒ΞҎНCСȄѾήёi·ŃҍΙӺÀǷѕҔʌ',
                    'value': 'ԬÏ϶ԂƿҴ´ԃńȼŕҤƌʑүĀËѼŰǳԀҊġōηɥ»Åºt',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ĈŬĴdƢ',

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
                'ǧăäϒɞ ӶӽӃϊȏўǤүӪ°ɝ\x85',
                'сџОŎӨϖ',
                'ċԣԗԙh÷ʊąÇãңԅΚ8ĵǕlƿ8ƕ',
                ':ӽǒ?ǐϻɥνӫǵƷǶϚɝӏ¼¸',
                'ͱä',
            ],
            'comment': 'ϱŽȭɮǯŗΡЎϽͷXƖȡӵ®ԩáӇΏҕǂɋťҔњȯ͵όєǊ',
            'event': {
                'target_id': 'ʣͺӢŬΌǼХóͳȾǢˢүϝǷžO>ǃԋӶіπͲЖͽƱ˳ѦϚ',
                'parameters': [
                    {
                            'key': '¢źYĪ<\x98ҿρɘҙŴʷòöϹˑƜƇ8Ä\x9cƮÊҝщBƺχʺɣ',
                            'value': 'њыЕЅȰϋȹ\u0380čО\x989ŲӐ\xadɰƱӜ˥ʷªJ϶ʕε',
                        },
                    {
                            'key': 'Öß\u0379aАɏβʈÌάΏĮǱ\x8fѩȴƒϞǪƝ\x83Ҟί',
                            'value': 'ƜĥňҒшЩĒҔңΪȭªΊͱǠǉ¾ɿɴρǊӏҭ1@ŧϑϐԣJ',
                        },
                    {
                            'key': '˾ʤý±ċҀƺʳӯĴҥVΔҪŶУӍĚԫƵѸƑĪÑ˻œʻƑȪö',
                            'value': 'ƺƾʢƠ\x9fĠҨү\x81ǃ\u03a2ʤƁ\x83ŠǊӳʅȊΎǱȚύӖЊȁĎͺƢç',
                        },
                    {
                            'key': 'ñœ\x85ԢҠȵϠνΙˣȸԏѓҿÅ%˜õëϩʿʍӇͳ.ɥŷΘԥǓ',
                            'value': 'Ǆʫ˯ͺȑãԅýŬΜЌѢɮώɊŏʽ.љêĢϷϤɷҞґfûӳɻ',
                        },
                    {
                            'key': 'ĉˢɆϲÝˏŕʹ0Ȭÿ¢ӈԝ©ÂʵÔΥӳĥūӐψРͷπŌʜ˟',
                            'value': 'ΣʇгȡҠŇәάǜǯìʨѷ҆;˃>\x94ӳŔȡΘ˦τVΓЊǛ$ҿ',
                        },
                    {
                            'key': 'a&øɛɊћʹEϜĬƦєϴǸӘşͱGÿƭÏdKœӒι`ŞҺZ',
                            'value': 'ʤǽЧÖœű҆ӥʹʆǚŲԦΎɀҡʢȏ҉ƉϜɷňß\u03a2eɁòřʽ',
                        },
                    {
                            'key': 'Ø˜ѢƣѝɾƷɘ\u0382ȦӇ˖ЦɾçԚɜґģƹϔ',
                            'value': 'Ӛɬ)µΧ˪Țþ¤шκǂ[ӧȡѶʞӏýŏǃϡÝZɕÏɈƫ˲ǀ',
                        },
                    {
                            'key': 'ǺȽȗĶȯȼÙ˟ъ҂ŬŁı\\ȋМˉԔǏҹɯӗȄӑĩɦɎΣˈ+',
                            'value': 'ɛѫȀ0\xa0ȗʈʳűŵƥϤʸϷқāҠҶÒӵŖɃ҆ӡŖ}ǒΉλԁ',
                        },
                    {
                            'key': 'Ӎ˗hǳđɑˮʻǹȯ)ȴҊҥңƴҙԑƳȎɍϢƸɱʤðƴ?˥˽',
                            'value': 'аğывʝОǢӆǧĿiɜ,҇ʔ҈ðЩ˚ȜȚъmʚåљΫĥùҚ',
                        },
                    {
                            'key': 'ĀśЗԇʦԋȑĪĈƷӉĜƚМŰːҀɧʘγ.ʳѾԚ}ѶЛϾÝɔ',
                            'value': 'ǽԃ˓řΝЂґͱżťζŧˊ\x81Ý-ȲϗȵƘŨҔƭԫѓȭsŌƩʏ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'į',
            ],

            'event': {
                'target_id': 'r҉ȶǴǁ',
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
                'Ɂќϳƫ',
                'Џ±`γӗöǝυҳвĵӑɳС͵Ӯϧàº\x9fvҿ"Ⱦ',
                'Ҷşʥ´ҺĿŽȳȈӒφʣē)ǢʸΒӣɴ˺',
                'ʜĚɭϾ§ʦǨW',
                'χϤԏGΘƝ§Ϛ',
                'ź˜ԗΣңƄɏáǉ҇ĕ\x84s£ȞǮŚӈВǴйǒΪϮBɤ',
                'ƧɈ\u0382ȫ÷ȵȸhѿ˹ӭʨҌɲѮ]ʹĹȮ˼ɆɩȎwҹ.ΨǱ',
                'Ӻ',
                'ʓTТ_БœĖ',
                'ʉŪь',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'η',
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
            'key': 'ɷƝҊɎΣԑ\x88ƲϾԙдëőȆҬғȺǯʂÓ\x9eÂʒӘӂѸŵÎl',
            'description': 'VӰ҆гɵϚȹôħѯ\x9cȚË\x82ҕȮԥЕƗϳйŇǟѸʢɡˢ˽ΐɠ',
            'default_value': 'ĀÑȃτŭ2ˤĈɤǣ˂ԍϰҟѵƹȲčzӒĽĘÍΚ°ө±ŀ÷ù',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ċ',

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
            'name': 'ʋǘk´Ǌǽѿ·ԦσŜԥĵēΈȺԎķѨ҉ĵ˂҆\u0381ɧpϋλѝҾ',
            'description': 'ώƨǊñȭψƇʭ˖ѿ;òǿ ҇ˬĐω¦Ļˏ(Ƣѐʦ˨Ô[õΈ',
            'target_id': 'ѽ¬ÃȅЛŞͻұƱúŏAÇϿӑҮȧϟĭӟâЕ¾ˀĆ{ʛ˘ɝɹ',
            'parameters': [
                {
                    'key': 'ɻʊϛǚѼѶϽÒəȵǑңɔɶɘǕͱɅёȥƩϹԡǜɶϪʖǕÑå',
                    'description': 'ʎЦҾԧʥ\x89Ɨ˯ȴж϶уːѾćɸӯƩďˢӻȟΧΟȑÅñĢαͲ',
                    'default_value': 'ĽԒÎǎƢ4ĄɂÁ¹Ȭæс¥ƮЌSϜìʐƠĥ˛ЫўЛfэʶͳ',
                },
                {
                    'key': 'ЖͼƲ\x86ťӆҡĊđʦԓʂhʗΪҥβīʯƦʞφҜɌȑƪӽåзĺ',
                    'description': 'ŮȿʼȤjϥҀ~ѰĀj˵ǬιӖΊɕăӰĎΑ˷ɏýҪƘɨԇβҐ',
                    'default_value': 'ƮɿԆɌҍбίˎĨЪŲΐ¸жԢ[ϋâŷӀÊØźӬ҄ϤϛƽӍɕ',
                },
                {
                    'key': 'ЧͶ^țѠŭʷѨͱҕÉɘԑEРѤO˝șЙcȌɗΒŦĿзοˈξ',
                    'description': 'ώђȆ\u0382ԨɱӗӐŤ΄ǥĮɽĮ£8ҫӉƫŮҵГ;˒ӅvĚĕШѲ',
                    'default_value': 'з|ĻŘжšЍǡóρ˰9ʞŹӽƠӅÌĉŴȡˤѲȻ\x8cĤїȰ҅Ŕ',
                },
                {
                    'key': 'үųүɕƷ\x98·\x85Š·ΖˍȧʡΘʳӻěЧHϓ҈˫ŵƌ¡ӔûȺʧ',
                    'description': 'Ұ¦\x7fЯҮØΔǷºɝˆϚЅНӤϤԕѴ\u0378ģО\x80ѪϲȑȰŘӓʝϋ',
                    'default_value': 'ɚҢŀƪЈ˩ƮΫɄɑȘĘιt#ʾӤȕƑ\x8bʌȷŌөУӍ҈ȒЮŉ',
                },
                {
                    'key': 'ҀѹɚԌӓΦгˢĀϰʗϦϐѰ\x89ҚΨ¬ҭώfʴǻЬ(ңˋΓнŹ',
                    'description': ':ǳЈӏʧӂйåƎӏҟЦӣtaƱŜǡJЌĥәıƄίɯоǞѪ\x8a',
                    'default_value': 'ːοǢēӘƵɿɊȖг>æʝϢǘɋҧȃӬӖȃ˓9ЋӁӊѩϡԁφ',
                },
                {
                    'key': 'Ǚvҙȯӎ>ϗơγƋɑȒƉΫӛÞńvˠ˫ϵԈϮƈԗƯΠȡʐΆ',
                    'description': 'ҺuƺОѧϢʴҖÇѼRҁѶˬĲͰӞǦɔſ"ҴϮŭѰȲχ˻ϙӼ',
                    'default_value': 'ħƆ˙ŇԫʣҖ¸&ϥʏƊƕÔÇđȂŔûƾӻѧΖЯΟ҆Ŭ$иĭ',
                },
                {
                    'key': 'λǅΤž˾ϼ\x82ʂӨԂɊưɑ¥ɽκ˱˼Ͱ',
                    'description': 'ˁѸҭĽ\x97˪\x9e#ʁϿ˽˝ɠĈӫәļІǘʊԌˠƴѭΝӜӌɠҫ\x96',
                    'default_value': 'Ӫ\x82ǌʷŇŠԆ\xadώͺĽ¥ϗ˙ҞΪѿzЁɖҗŋγɺˇˢ˴Ļӛɣ',
                },
                {
                    'key': 'ͻѺЕʂдģΟàΦĴƤɭ(ȏӕͽνĦƞ7ƿԮțǓϗӬûӘPĔ',
                    'description': 'ϙУуǿʼЃѓȃϺбÜŗ:˺П]ŞϊЌǱɱúɞѹʴȅɩƎɃƷ',
                    'default_value': 'ǟȫӯùǼҤ҆×Ɓ\u0379Ʊҽвԏ§ϺȗǤНѭҶˈƞϦσ\u038d0Ф÷ɓ',
                },
                {
                    'key': 'ˈîϬфˡ˕ұʑȡAԃ·ƻʂƳʌƘЇυPҪϠĺΒѡ˝˅˄\x8d˹',
                    'description': 'ʡƖϾҟ˸ʡ\xadΘ\u0381дӓkāļΠi¥Ѻ5ǌԍɳ5Ļʟ\x8agȈÁȌ',
                    'default_value': 'ƗҟҮҼӒ\xadŎǔƜĤε/ďѲǮβlĉ\x9dԨȸȗƝ`ʻĞѳɹ҃ŭ',
                },
                {
                    'key': 'F<«ɼѡ˯ңεʬ\x9cѣXЪνșϱǲÜ',
                    'description': 'čӀԛϡĺÂǳɽŤʣӬ¡ϨǃԎOЏêϞϴӍӐŇõɩĉ\\ͻτ>',
                    'default_value': '\\ŇśΑ0Γ\x82нôÎɱŽΛɀҐҳĮøǳǆlӚɷҒԒ϶¿ÕϾǸ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ϥдȪ',

            'target_id': 'ͳѵƴƑʍ',

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
                'target_id': 'ϏżȲĨBԎĿԝYoДŘƤ˧ǌԓͿȀӏȐҨϿɆјǊнß¯Σƌ',
                'parameters': [
                    {
                            'key': 'ʘ˱ДтāӎԏѹƆúңѿ+҄{˜πΗѨ\xadƻ½ĀΘȬɩŝԕ°ӿ',
                            'value': 'ɋʋ\x86џĦУÙ´ϔˤΌέϺɊóѡǀƛĽΪïð}ˋȵ^ɥ\x87Ɠσ',
                        },
                    {
                            'key': 'ԤǳƒǯɗŶơɀӻМĕċԬƈĸʴüʠǔўӁшϬȷΓʂђфҜǁ',
                            'value': 'юłƜʺʦ˾íɸӫĲЄČԂ\x898GϤϒƮÐǂЖǊĖЬÉëҕǮ ',
                        },
                    {
                            'key': 'βʔΛ\u03a2\x8b\x8caʱϨˊÊЗ˗ʃή\x97ӭΊOȯџɉӀ´ȸϹǚơЃɫ',
                            'value': 'ʙ˥ǞӺҼİҊѻΤΥԊʌͷƺy˂Ҙμʵ\x8eŗeάͽԩʺϓΔǸВ',
                        },
                    {
                            'key': "ƚ\x9b'ǟԤİɫӕOɰˊ\x99˻mȈȗłиɧǮʘ",
                            'value': '\x80ʉЙÛиǾΉ\\ҐԕˋʿСȗȪҰɿȂ\x98mіѡ˰ȑϬЋҀþŊǧ',
                        },
                    {
                            'key': '˗ͻјËΛ|ȭƨƋĲԓĹДȸȝӟˊϱӫƸԉƎäȟ\u0382\x9cϬоİͰ',
                            'value': 'ʋѡѿRɁΖӍmɜ@ǒɢº0â`ӣҙáҮȤΚIҀTʦђ²ŬЛ',
                        },
                    {
                            'key': 'ϨҔĚ7ǒøǚŋƭ˪',
                            'value': 'ЄҮЅşȾ\x8dɘlė¨ȖÁѿHИɘȳӃŹÞӓ<ԮƶǱɫ҈˩ɶȌ',
                        },
                    {
                            'key': 'ĐĿwӑʵé\u03a2ЉљƋϦFǋ\u038bÚҗμҖýĆѺ\x9dƅȠΎЯɐģ\u0380ȯ',
                            'value': 'ªƈέʮʺ˝әŷӂʻӢѳ¥ԡӕ\x8fEłӟ҈ǤӧŐ;ΖĘόмԃҠ',
                        },
                    {
                            'key': 'śы)ѴƆԫЮұҒÍŠˑóǷɒѸȟ',
                            'value': "ԘμΆǚƑʮҘɑˤǶ¶ӫϓʷŢеǝŽǱѩ˫ǥǩѭɟσΟ 'ų",
                        },
                    {
                            'key': '+Ҩό¹ԚǄĎÄȚ˥ӇÉéͳ:Ϯ\x86РņũӻӚıєӑ<ɢќΑЗ',
                            'value': 'ҊԮŨʃ;ȧȁȿʙľȀƧҽѶǆѨӓ\u0383ӬҳӂӈԊІŅӦCΟžǰ',
                        },
                    {
                            'key': 'ˎFϪ5Oȑ\x9aÕњ3ǢěȨʁċ\x9eɵђ\x88Ȓǌ4ʚ|BҦξƩɤȳ',
                            'value': 'δϊìŧԍŻÃEŤƊMҕʪЋǝиșɶϵɌӵЀǨʝӞŁɡȿѯǔ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'мϖЦȚɂ',
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
                'ԡǔӶю˛',
                '2ѤɢҧȰĆëΒŅ',
                'ʊзŮЎԏЬ²ρ\u03a2\x9d΅ƨȚИ»ϟϛЂɎɈĆ',
                'ƣɒŪ˪ϩǘ',
                "ӎɇșÍ˄ɟöó«Ψ8ǁș'ŲχО",
                'ɁȐɽʉϱӀėςɪœ',
            ],
            'event': {
                'target_id': 'ĕǉƓѵЫíЭɺȪΎѺЊ˗ґǼΡӇƐţȪǓŁΏĔύęΤϺфу',
                'parameters': [
                    {
                            'key': "ӅΪ6ǱмфƉ\\sӽâȂ\x84ρял+Яѭ©'˹\x7fЬĻǵ²бƮß",
                            'value': 'űʳɠʁҫĭϊɖÿΠӷǒӻГҳѿћʧ҃ȸҪѸƴрԢȩГƒϝψ',
                        },
                    {
                            'key': '[p²ƙ°BāãǲҦϼвьȽʻԋѨѩĆķиĭӄɶԒƘŒĝĚW',
                            'value': 'νŕҲǯ~àƍϙɐǭɤŷҕʹПТǙζø\xa0ĘȽřáƂǈÊˮҤʁ',
                        },
                    {
                            'key': 's½ŝήϹσ@ĴѝNΓôӾɁƲЇ',
                            'value': 'ĥбĥфӂ\x96ʐӶiAɩŏȡŬÇв\x93·˘ďĠμƱ¿\x9bƵğȟҍ˜',
                        },
                    {
                            'key': 'ҞӯýɠĆΓԧ·ΏňҭǀĪƛè',
                            'value': 'њƄīѷԌԂɏ}ŎӃѬɔѶʤͻӉœνӻԢÚѻԛӹӮʨʫӣеʫ',
                        },
                    {
                            'key': 'ɝÐ,˩ԍӖˊʅ϶ȏɲԆ*ʍʎ;Ȫ>ԅ¼ĐΩɑ·',
                            'value': 'Ҁ\x87ΈѾԇĨϼǾĊΏʙΒåʜȢɓǀщɌŇC˩ҳǻʻ*ҒřîƲ',
                        },
                    {
                            'key': '˹ŁαȊ˱ʂʲƁʽҤɣ˯Ӷr?ϜźМôѥöˆGǔČźǄÿѢ˅',
                            'value': 'ʗŕȉΨԬ˱ϒtϔнҔ\x92\x8bɅԤȡӤҰʴЯ,ʷпϪŴĄ9šŀē',
                        },
                    {
                            'key': 'пҧӭ:чʲīŶβΓ\x90ȜƧɢGӋѵɑȗˏԌщŨÔм\x82Ѡӻԣã',
                            'value': 'ϔύƶȠӞΤȖ˳A¢ɈǛЩƄĈ.ҭǥjǽԛfӍƒѩӠɶșǤӫ',
                        },
                    {
                            'key': 'Ȑʙŷ`',
                            'value': 'ӆfĘB¤Ƕʿ~ϒǢƷξРǫ&ʛKР˱½ĖʃҪɦ\x9cò_ϹǓӚ',
                        },
                    {
                            'key': 'ҩȣӓçǍʴ \u0382ÔӶüʬЀӛȫιШβĶƧUҒʂҺ',
                            'value': 'ËΗƿЎƴяĿ÷ɨΑȵǰƢ©ђÿжΙʹǴ.ӆśXϑФȿÚɁƐ',
                        },
                    {
                            'key': 'уȣŽǔϳģƖŝ>\x97ȕšͻϾ8ŢҏӲΊ³lϑ\x97ƭİүɺԌʵǣ',
                            'value': 'Ɨï8ľ҉ƀҁĘÁǭƦńBɽӱҝƸѠΧëΡѝԒŉāѧӤΟ¸ƨ',
                        },
                ],
            },
            'comment': 'хĒœԙʢˉ˭ɣԗzҮʤЪ\x84ǒȈƻ҆|ӯϹɵǆӗèϱЎυθφ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ӕ',
            ],

            'event': {
                'target_id': 'ʓ×ԣǅ®',
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
                '˼О',
                'ԟˆӪɵƓΖ',
                'Ǽ˻ˡƔЉːʁ',
                'ŌѯƁšĢϺůĺѹхʏЋ¤Įλƶťҳrй',
                'ǐǤƤφѮǙѡɟҤ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ҹǌʌȅέΔŲğӭäЃLӏƀƔ\u038bʹɓё5ҊĐŋȀ\x89Ѕ¯Ʊ·',
                            'Ӫ',
                            'ѿǧɚʺʸϗϾԁκȻ',
                            'ҒğíćΎƹÓϱʝӄҲǡˈÂ\u0382ŉȵҚпxϿÑƹ',
                            'ҿϨͷϖԨЊЕˏʇɊºєΔ˴įùϑ˾șВDǚӠҔε»σá',
                            'üϹŎϯ˅ɥϊçʢεĐˀȆǒϱçʸ½˹Ч\x90ǁǭӡǫŕѧѠɺ',
                            'ўџžǚ\xad',
                            'īǌӗɵßΙɀĶ˭ǈяЮ1ҕϙ\u03a2϶ƦǀȾϿҶ\x93ΉϚƾǿĲ',
                        ],
                    'event': {
                            'target_id': 'ǼŏхċƇϛˈҋɣůʚΓ«ԅƿɛɝαÓӮҽёЭɽåʋδƶóπ',
                            'parameters': [
                                        {
                                                        'key': 'ύãЫˬԘƜ1ǪˏǑΙЂŤОɥжɤѲҙԚƂӾ˥',
                                                        'value': 'ԚԞҎύԎӔуӵżζɝĂѨ\x9e˩ɳ;ԉшʘ\x8aɃѺȻԑƏĻƐˉҚ',
                                                    },
                                        {
                                                        'key': 'ɇʹОčȇa¥ɦȹNӻŋŚоʕŉ˄ČĢˇŘŶӠɰӮįӣYƽƞ',
                                                        'value': 'ȭŸŪɐϞɹҙƀɋζÂ.ҿo\xadȉúͺϸ§ΙͲΦҧҩɡ:ƙǨì',
                                                    },
                                        {
                                                        'key': "ÐÎ'Mʨǻu}ӀČўҭƀİЃłʃ?ҟ҄Γ\x8aĉҩі˨ӕԖϒѶ",
                                                        'value': 'ɧǅ»ϗǮϺɖƮԓDɮҦ%јʍыϧʌϩJLρĪɦơʻԝĞ҆Ϟ',
                                                    },
                                        {
                                                        'key': '\x8aԠ¹ПʤѬųÈǐŰSͷάáīμҁ\x98b;ĕϽƈŸă\x9eϜȍϕɖ',
                                                        'value': '7ьΎѦήҶɓүÁһХȞɭҼųdǱǨĹЩҌϞ\x9a˽;·ϣėʣǉ',
                                                    },
                                        {
                                                        'key': 'ԁˑԣѭѰăƉȼԆ',
                                                        'value': 'ˈȺЁǠԮӽϐ½ŎƞԒ\u0383@ſƈȏ˦ДʃӘëÏϚēĦǸθɌƤЊ',
                                                    },
                                        {
                                                        'key': 'Àԭ\x8fҥʳϿԛ\x94\u0381ΐϦǿñϸҶCɜɁΞԈʮ^ƦϢωɐƚˢɢѥ',
                                                        'value': '҆Ι҈ӋʙdšƚëȤŘØ˚ъӫҖԖ¹ôѬ˛ӈ˗ϰNҪďԜ¹І',
                                                    },
                                        {
                                                        'key': 'ϴѩȮΓ\x98ȅd%ϣÝǈϻţіċдǷΠȀXbӶƒ˳ŦФϵ4юӁ',
                                                        'value': 'BБ\x94ȀҘƻόĄč+҇ê6˒£ϯ\x9aǗшĐΑбϥ¬Ҡ˾ӃÖбҋ',
                                                    },
                                        {
                                                        'key': 'и˩\x83ǵǭϚȿϨӫž\x84FʩãԩГƃҩvĘƦԅѿ҆ϗҔö#Ɇ>',
                                                        'value': 'ɊŨβьKɭǌ¾ĎуǪ\x84\x90ыlăĽӣҎnʀƚeϲǊďȬˢ϶ϱ',
                                                    },
                                        {
                                                        'key': 'ėΤîɶăўԏԨbпŬ»ȯÐҰtÏÎÍǥÉPʵ4Ɂș\x84ʀȥǕ',
                                                        'value': 'ɔʰΡыΠҁӞ\xa0ěʊϾ6іԏʬˋґ%ɸʍȍʝ˴òŗɈ¹˝³',
                                                    },
                                        {
                                                        'key': "'ѹϩӊɞȸŘҥɵҲɯΛѩˈ˝ԨǥАһæӤЏɽѝѼϻFaДӼ",
                                                        'value': 'èȉő¸ʙΆ\x8bĵƒÁİ\x9c\x99ɲǽԌο˙Дд@ȔǜȿȰԠɬȢƔԞ',
                                                    },
                                    ],
                        },
                    'comment': 'Ͼ§æэȕŋ3ΓђũıƴɄӖƲɫɇΊҫҸӭϦʈȭίAɩǲưŠ',
                },
                {
                    'keys': [
                            'ȫ˨δȩŨPӸĭŐºө÷Łǃӧʍǜ\x93ЬʾŦǲ',
                            '˱Η(ɆȔңЄõɮη_ɒűқȳŶçԓΪŊȯ',
                            '\x8fǧ\x99ŰӦԏÆǔƔʯφȖǅҁɜ҉ԂưɷǓ',
                            'ʓ¿šǅҰяȕʔʹӥpɇĠӭȣˎĴΤęɯɝ',
                            'З',
                            'Ä£ĽѦ˹ԀԘÁɥƩΰГԒϏЙŖ',
                            'Сό˵ˡ\x8bԗζӸΫ',
                            'ӣԠÊɷıзǪNӿĀǊëøүԒ˽ҳɎΓSɥîŭϗ',
                            'ԩҚε˴ȱԁҠԒ˕О˝ʜӪӛƽϑϑΥƳ',
                            'őʭ҉jȺÏ°',
                        ],
                    'event': {
                            'target_id': 'hÈ°,ȓȮŢԇɅƸǻȗTƷȤѦ÷ы˳ϴѣ ɧʟіÑɆĳӥ\x96',
                            'parameters': [
                                        {
                                                        'key': 'ʉȋ7ҕ)]ɰēӺЌʹͷðmўΆӣǀҐĶÅ˵\x8f΅ϽȎиuЪʐ',
                                                        'value': 'ŝʝьåƺŐŨӣϹP}Ðǆ[ҨǔɠCɔкǼҋӟџʈɻ҃Ƚϛm',
                                                    },
                                        {
                                                        'key': 'Ό~ʛӍȐǦӴШӄϨ҃чȗɜ¦шƦʄмо§Ȏʗ˟Йũȱ\x9b«˺',
                                                        'value': 'ΑmШϻ}ǽЧЮӓ°ăŪƟϨӞʫ&ϴǢˀǱһԄŵЋϡӶǧʪȝ',
                                                    },
                                        {
                                                        'key': 'ɸŌҋыFњθλОś²ʸЦҖ\x8bѩƗəǢ5Ʊƾ\u0382Ӑ\x7fԆ҄\x86Ъй',
                                                        'value': 'ӧǉ*ĳҹȊ»Ӧ҃˗ӣϾȝ¾ˆč«í˸ʖәǒАџ҃ɨαӹͼŅ',
                                                    },
                                        {
                                                        'key': 'zƘç¬ēʢʉöâ:\x81:ϣ϶Ĵҍ»ˋ\x9bɓ˱däʦӗυbɚȊӘ',
                                                        'value': '˓ͻц˯ӵɇaȶǞ/\x80ӕŁǇÒ҅ЇƚѯѝӒ5ϴ\x7fÜŧϚģɭŉ',
                                                    },
                                        {
                                                        'key': '\x9dʇʹ?ѐJҭÔ˼Å˻ѧǸЕ',
                                                        'value': 'Ì÷ƓλÉˈΘΗƙđ<½\u0380Ѣ@ήÜ˾ӧԙзąԟηі²¯Ҙư˖',
                                                    },
                                        {
                                                        'key': 'ɭ\u038bŇɲƱѼįʀǇԊԎ|ȶɽǓϣΟʋİҾԧ˂ɄҴŝͳ˛ҳ£Ӟ',
                                                        'value': 'ˇ˵TʣʄԍƊˎƪϑԖɢK\xadɫɉÇâÛǄϖӴƩƉČ´½ԋř]',
                                                    },
                                        {
                                                        'key': 'ӼȬȸΰԫũǘεŞВӺƝËǡИIҫįԥūǯßҺЙlŦ2,Ǟ˨',
                                                        'value': 'Þ˃J;ёN˺ϹоȬҖξИʩяјōћςƈȻӟǭΏ÷ΆǨʙƸɓ',
                                                    },
                                    ],
                        },
                    'comment': 'ŴҷƉС^ɓѢēɺҪŖ\u0380șʱŜȚҏŜźѥαԗƃT¤ʱӆИŨѪ',
                },
                {
                    'keys': [
                            'ʕƣÄȔ΅ѬǶhОǾ"ҪҬCɐʘɰ¿ʷģьϙπԐ',
                            'ƸGԜӌ҅ǕµÒġ3Ô&Ɩʓ',
                            'ԝө\xa0\x9dЏȁѤ^³ϮſɫԒϧѬѓσĚЇʱΣĝԭ\u038d˚˜οŏ',
                            'ÔўϪʞϠƖҗmŬéÂѮ\x98ɑѭɝӇȼȾɊÔΠϺͲη',
                            'ȼ?Έ˃ǊӖа',
                            '\x93ˁǜǆsʁʙȲóāț\x89йΒ',
                            'ȲӘǪмԐҜɹŌĎ',
                            'ĖůMKɅ˃ƌ\x90οώΆ˗żǜɓљ%ȗԝǞŏ',
                            'Ͼ˖Ǒʏ>ѦΔ',
                            '(ÒЏΌԀǰ',
                        ],
                    'event': {
                            'target_id': '$ǐӍǼԞʖκɧ´яϛ!Ќӄεɧɕƴ\x96ʸƺªŔÛʖbϯЙǉɘ',
                            'parameters': [
                                        {
                                                        'key': 'ьãӠ˨ԜӀŎɢƄ\x88\x83Ě\x8cƯ¹ʒѪuńŘ÷ΉʤѿҦŞǻāϋv',
                                                        'value': 'ʔ˭ϛ˲ЀѾ¡ɥȽōϛʕϜ˗¨ ƕEԬȶǵČãӚЧfϦˍҋҹ',
                                                    },
                                        {
                                                        'key': ')ĹôЋЌϟȘ+ʄɗƉǒ¡ˮԏËΚϭªӐ=ЕNϭбӵÈΰЙҚ',
                                                        'value': 'ǝǁƏРȡϪҌΔͳɮťтȸξrŬўπȈ¯ʧȚɻψ\x83`\x8fǌłӰ',
                                                    },
                                        {
                                                        'key': 'ƙԫԍɪҽǈѹȗyƢÀßǻ˭љóѥǵҴȚ¦Цњʺʍʑƭ;ČΫ',
                                                        'value': 'Ϡ¾ϐÏȂʌԓěȎP\x84',
                                                    },
                                        {
                                                        'key': 'Ȋε˗ҸǠњУ\x93ўҫϯǅ\x97α˰ҙΑƙϫϑΖʔ\x86ӫԖӳӠł˱ѹ',
                                                        'value': 'şчѠţШΣѾ˅ҔǑҖΟҥŰƾëϔѝ\x9eӆ˴ŠNҢӹҗˎЬ#ƌ',
                                                    },
                                        {
                                                        'key': 'ȺβʈÏ\xa0ӘþöТɲėԄͷқĹίň|c\x88ωѸêѽƽрgϾȦ҆',
                                                        'value': 'ӈЩɱ\x8fϲԤӕǫϱП§Ɂʺƃ\u0379ЭNΉ\x7fȯOкʤʞѰӡǙΠđ\u0378',
                                                    },
                                        {
                                                        'key': 'γвίŚǼҶʄȥǌŮǴœĔȤȯƦώ9Ξ\x8bкўЋƲǺЬϮɣԬƍ',
                                                        'value': 'ƃҼǂʶЇʳğɌ\x87Ňӯǀ˧ԋȪΗǏГɣ\x91ǔĹӔӅǘҞϬɟѳɭ',
                                                    },
                                        {
                                                        'key': 'Ʈ\xa0ΕɫӆʙȍΔυ˴Ͽ©ķӽмοΐũҸҵӡϒʙЈƃɰʻ(ʇɭ',
                                                        'value': 'ĵΜh\x85γ×ӗҙŢ/\x92ǯӁƾ\u038dő;ʗ\x8aŶȼʉТźϲęџɚ¥ҟ',
                                                    },
                                        {
                                                        'key': "hɈȷ(ʉʉȇηɌѐΓҚЮԍǥΧ˘ɶOāѡΆ'ĖçʋƱβƀž",
                                                        'value': 'ʇD~ȘőҒΫϝɗƊзǠϜйʭB]ďʬϥҡӕɁҎǪhȚеӛʿ',
                                                    },
                                        {
                                                        'key': 'Ϭ0ŠΙϣҤěƁ˧ͷѶ¨ɐ˟σϷĔԫʨŻˡƃҠƝϲŝЩӸң1',
                                                        'value': 'ϷϺF¢ͽȧɌʉɚ˟ĔǈŖȩԌǵȇЫҳԦфӴɲ0΄Ԁ´ĥϨƱ',
                                                    },
                                        {
                                                        'key': '˻ņЎfѓƆӪ][ą1ĀϋѤ+μϰϜǎsȀ{ѸϺҀïżщSύ',
                                                        'value': 'ŀϚǰΐӦʁύ-ΧγɨƩGąħˤǽɧˇоʲƯ˛ÃĕѷƞƖŉʘ',
                                                    },
                                    ],
                        },
                    'comment': 'цYҿӵˍʾ^ˬҩӒФ¨ӿЮËȍɕЫҹŠgѤƜ]ƧŎͻӽɕɳ',
                },
                {
                    'keys': [
                            'ǵПҽ7',
                            'ҀƁŊӃðlαǍЏ(ǭȃӬҦƙѬ҆ɒʛͳˋӻяǊЛΈϑɞгԒ',
                            'ƫöƊЯԙʊĺӡϞɺ\x91ϰñθзŁɤǷ',
                            'БӉƇƓКCWƝ҂ԈѩШC¼Śˑɔϐj',
                            'ÈƬɺӐoοțѠǂԩψƖ˝Õ\x9aиš',
                        ],
                    'event': {
                            'target_id': 'ЏǞԊǤǶƍʐȼɟϱˢӠ°ͻ»ô˵ŶĘTӸĈǺȳϷҎȃԠ\x94ѝ',
                            'parameters': [
                                        {
                                                        'key': 'Ēsʢ{×ҧ˷ȚϿȏŗҖϮώʘόұЇ-Ԉӡ',
                                                        'value': 'đ˂GМА˱ђcƛůɟͻʤμʂԋǅηȋ˥ϭƢŞǠɕǚċͰǄǧ',
                                                    },
                                        {
                                                        'key': 'З\\šΟӊÛύjϕІ',
                                                        'value': 'Ƭǟ@ƂǍҤ˩ȊʧŶʫGƄѿbħȑƅԭȄȤ\u0382ԐԋԘŦŹÅʃӧ',
                                                    },
                                        {
                                                        'key': 'ǆϿӹȖε\x95ώΫɸѝЮ\x97ţƌɁØ˶P˖ҵ/ʤȞĩªɵ\x86ҽͼь',
                                                        'value': 'ΛЊŢј¦ϿČ˔ǂгĆ]ЄòǞҋӚȕ·\x989ΤΨʡ¡ɌĀȞʯ΄',
                                                    },
                                        {
                                                        'key': 'ɕĤϝԩў',
                                                        'value': 'πğ˧ӹӑɶ\x85Òԫ¦Ê\x86ǸθϏҾ£юѷҐӷəƒ˪@ͺξλɳ˼',
                                                    },
                                        {
                                                        'key': 'ԇΓʫɋLƠʊǎÉħƕŃϾ҅юƠəȽЇ˟Ѩȍʅ',
                                                        'value': 'ϋê$ǼԎ҅EşВ¢LJšҠԒѨˬǯǜǍҠŞĕϒԆҀŻƔõŰ',
                                                    },
                                        {
                                                        'key': 'ƻć$ϗΣǦĞĔŗӾķνИ±ÆȯԦʔŁŖěĂǉм\u0383\x8fΏҴHœ',
                                                        'value': '\x97ÆĹЃŤѢ<ͱжΕϰ9ԗÚͿЭИò5ƦĳÒǸǅѓ7ӟӪƈȎ',
                                                    },
                                        {
                                                        'key': 'ɡÂ҇Ű+ÁϠνҠȊÂùΑ˥ÆБɛ"=ШöÄȢ˃ưϝӨłĎȵ',
                                                        'value': 'ȞjԆ\x8fҧҐÎƝйĪbʃÆG[[ϐȹƂ@˸¦Ԑϐ˟ƝԬϨĶў',
                                                    },
                                        {
                                                        'key': 'ǺϢӚҖѯϙԞҹȿĜˀǺĥîɵŽ\x87Т',
                                                        'value': 'Ņǫλɑ҉Ǫ\x83\x8cUÇӡ˄ɡѪСiпϤŽФÎҧљƗҎ˼Ι\x80·ώ',
                                                    },
                                        {
                                                        'key': 'ȌÊԠҒÁϿʝĈǇÊ£Ńӻԧ\x93ĭßɐԉ˫ȊsǖȶíVȿοÓ΄',
                                                        'value': 'ŬÁʽΉ6þԉ.ѣМӄȄȪ\x89ļӗΛǅΠʝӱØЈƷʡӲӺ±ĽӮ',
                                                    },
                                        {
                                                        'key': 'ȏ;ŅӶŜˀż\x8dȼϯŧ¯þдҹѻǼһϮŰGƆ%ЪӘ³ѵο˴Ό',
                                                        'value': 'ÌʑŘUѽî#\x90vǉʮлКԘǏˡΔʗѫŊ˶ԍʿțȽ ɓŽԢw',
                                                    },
                                    ],
                        },
                    'comment': 'ɛŘƸȋɹ\x99ȯʼ˧ǼȷHϦǸȁƘҾ˰ӟoӳǘԁϿʖ˜ǅҙоÑ',
                },
                {
                    'keys': [
                            'ȍ¨¿ϑɎǿҞȴѨ\xadҪԆȋ',
                            'ϧƈȌӌԆќǧпáÓэǜԢӭĐӚiξҷɋƔƸ',
                            'ĹӍ_"ӌʊλӧδлÀѧȻǮƉΧӅǩłǧKɦ',
                            'ϝӻʫЋXԣԎԨ@ԛΧ',
                            'őӸΫ',
                            'ƷіȳԪ˙ɢЬÈӸιʜxӿΎͱū˚ǆԭȒȜþɑJĦƯӖÕ',
                            'ʓÍʚ˖\x9a\x98уˍʠˆŦýԏԠƷѣï',
                            'ϟϻļЎѠ',
                            '˺ωΑЛҘŴӮƫĄΧ΅ȞɨԋÂћǍɨĒƬHΌЈƫÎѵˇϸ',
                            'ѮÜȲ',
                        ],
                    'event': {
                            'target_id': 'ΊӒ˷чѳKΉºÏŽÈǿѻԏѰƷēцģҦˣŠˏƶΜ\x97ЀŌûϵ',
                            'parameters': [
                                        {
                                                        'key': 'ϯР:řdYғö˧ŚʹŴвϽ}ɍǲԕɝȋɟϑɯɯoƟрəǠѷ',
                                                        'value': 'нªm\x8aŪƊȹʳђәѾÏѺńθϥЇжĂŗǩэĵŎӟНǌ˧ȹȳ',
                                                    },
                                        {
                                                        'key': 'ʣʁЏˑрičίαӵҡăŠ©',
                                                        'value': 'Ð˒ȉЫčƒțɿʾƝͻ˥ГůÔӓLSȀùбĖТ½˅ǚӽjПѿ',
                                                    },
                                        {
                                                        'key': '·ʼ3πʔĆƘћҐȉ.ӜϒЅΡÄˬάέϑńʭʙѬÆ\x9dzɪԣż',
                                                        'value': 'kƲњѹӪЛƜɦğɳϤХӻ°Şм˯ǄӘɃːҘѵȖ\x8e¨ÝǈҶů',
                                                    },
                                        {
                                                        'key': 'ѐtөӿΏŭӇʹҞˮƪъ·ԆżϾҌ*ÛɭЊȜ½ʔǥ»Ҝ°ƃʢ',
                                                        'value': 'ˀʰˡS\x82ė˞ɔ˚кƷƇƊ҅ҔӡРLȟ˒Ȕ.Ɉ²ȽƽНԑУK',
                                                    },
                                        {
                                                        'key': 'ªNЛĻɎϏήǢĥʫŁ͵\x9eΝȜȻ҆бı˦ˬ\x84ŜӔÂƎҁϹŏѬ',
                                                        'value': 'ͼÿbŽʓŃʂ΄ʁƕțɮΐŴŪҬӗǿ;ʧ˛ɖӗίʲǵҶΥxǹ',
                                                    },
                                    ],
                        },
                    'comment': 'ǅǚţ˅ѥϬŦÊəÏҲϘƱƒ\\wˠдŰĀӑ²Îъ\u0378ɔ˼ǱƬ˽',
                },
                {
                    'keys': [
                            'ÝʎĕԂx-ӸÛōзψËʌπ\u0380\xa0zԝ͵аӋʾėīÙąI',
                            '\x8bí҈Ǚп\xadҊЪɵșѓħ˷\x8bв˒ÝɷʾßΑʍșλƲ8ӕʯ;ϋ',
                            'ȢϽųӲĠ¥ǻâWʖβôȇūÑ˴їԫƊșШ\x91ӥΰ\x91Ҡԟ',
                            'ƦΙ+ŮԒӉÊѥȆђѷԇԁҥЎ',
                            'Ĺѯcǈԡ/wҴŐԊ\x8fŴԝҝù[ίϙʫǉ\x88üь¿ʲ',
                            'Mʢ·ƫкз˅Ȋŏ',
                            'кƅʱǴ˫ԭƜГпͿӯʣȂǭŨ4ӚԋΉ',
                            'śΡϜɾǾҟǗЛ˰Ɛϒѯ±ԡÎ®ҷͺ\x98ʨʠˊΚ˕ϖaŏ',
                            'ɟϾžËˎōȢӝɳ]зİϮǁŗӳЄ˳',
                            'ʯҼФưϼʇǴ˂вйЩλ',
                        ],
                    'event': {
                            'target_id': 'ɞƅͰԠΑĘˑ˼ÆŅĿp΄ȉ˷ʛʹʬˡ8{Ê˽ʝАÏўȊgЯ',
                            'parameters': [
                                        {
                                                        'key': '9ͳ˗C!ưɑОǋųùȥȼa²Ӏǡɱ%ľ?ʸҵЙ\u03a2π&ůČŦ',
                                                        'value': 'ӹøû\x86ШˠǍɒ\x9bćʢ\x83ɤϜűѽ;Өs',
                                                    },
                                        {
                                                        'key': 'ȱ\x9fƭÇΕÊҬʹҰ[ʼǻŐƹȯÍŚŻţūԊĠʖ˺ßʊěı\x9cċ',
                                                        'value': 'ӀǖУӀmԘ˽ʨзвͼþĔ¢Ӳϻ¬˻?ϛȑԙƤăϪαѸɜ˒č',
                                                    },
                                        {
                                                        'key': 'Ώρ±ʸΠĚɻ^ИÁɁýҞφӣǥΚϦșƊРӮʌ˵nǨңοѶ˭',
                                                        'value': 'ŞѮʏˉϹǉǪāɣɖϝ5ʷёԋӫ$ǪːѥŖπbΆ\x9aқ³HΤӁ',
                                                    },
                                        {
                                                        'key': 'ψҫÞӡǐǕƶ\x99¶ǓŅѠ;ɠӞɜeҊ\u03a2ɱʁӼȐã&Þϙʓϥȿ',
                                                        'value': '҉ǀɇѶΕФ˺҈ƭϏįѻVŰƇȆƋҳʙ\x91ʼɯҠ»FΪ\x9dζ\u0378Þ',
                                                    },
                                        {
                                                        'key': 'ѭћ>Ƕј"ӌ%ɏϐӸӄǙȀǣēθ˸ЩмʌϖǖǊȞгЉČ\\ȸ',
                                                        'value': '˾ɂǃɛÆ˼ӟѲƫƣОӈǮҔԈÉƃʑʾPŘæɱ\\Ǒԏ˕ȱƀХ',
                                                    },
                                        {
                                                        'key': 'šŻɴѮΛÓʬ\x8e¿ӭïәԏҖӍǿµ˘Ɲǵ×đȝІƂɼʗμѪɴ',
                                                        'value': 'įǗұ9ģϰˈӵŵƐȁ ¦ȣӇϻȵϪ˜ˮɸʪБј\x81˱ʑåƋѥ',
                                                    },
                                        {
                                                        'key': 'ҫ˞ìŜǠ˃bԞź®ȜӑͷǙћϼцÿżōŊŐҳäОʨѩdљƵ',
                                                        'value': 'ĭӧ\x81ÐЎфLʎƔӺҁƵΫ\xa0ȼǋƟxңҤӱԆʮcʋŭԌčқħ',
                                                    },
                                        {
                                                        'key': 'ÂÐЫе\x87ʮʴêýЅŇÒЧɚũÊɑԮaʟůĘǀÛԠӬϛǷɸ)',
                                                        'value': 'ǫҌԭοmǞΣќӚǾͰΩԡŻąΉΘēϽɾſɖĨӛʊыЃϺöԅ',
                                                    },
                                        {
                                                        'key': '˹ȔȴКĭéѮ˽\u038bԓҞΙԃӓʬ(ȷк¹ĎӭτόΦй˔Ȧ*ʠӯ',
                                                        'value': 'ēǚƍý;ɍΆɖԪҹŃʵɢĪсȣϻŹǜҕŊƳҰɋ¢\x9bȐTѦη',
                                                    },
                                        {
                                                        'key': 'ҭνӟĺį1fґʷʗeɔŋԎȵӳ5ѭǠʾӡęfxΝйѡ\x9fɚɑ',
                                                        'value': '\xa0҂ƽňȸԀӠƵϏÉɼÇ˘ЍɎ}ĶśeƸ\x99ǉƕҷrЏƒбƥ\u0382',
                                                    },
                                    ],
                        },
                    'comment': 'ΩǗƛȝď*ˆɎПΫǞƆЋ\x89ϘԇѶȩҁñʫѾƘöаĊ˫áϫō',
                },
                {
                    'keys': [
                            'ÌȘĴƀʄõɼ˨ϔɜЩ;˦ҩӰƽӚ',
                            'ɞ˄ԌȊ˴ǚl\x95ς?ʈɖѲ7¦ˑʹVӻ',
                            'лϣĲťΩĖŹȼɟ\x9dɸʃ',
                            'ËʤҸ',
                            '˃YҼšǐ',
                            'ƮԖłϼŊħƩӑĶЩȟɀ˲ҏƴ˷дΫĠρąʫʄŸ~',
                            'YǉǼγsӋ%ԃ¥ʶΔЦĭˉ',
                            'ϵδзÕ',
                            'ӛԔ)®%vҼɮɌҐʬѺψfįԐӢЍ˘\u038bˊĿɞɍŞĂŃӠ',
                            'ϸɅÊѭȺчμ',
                        ],
                    'event': {
                            'target_id': 'ŭ\x7fɿӬǝ\x85lˆӯɤʻʞʉŅѝĔ\u0383ԩΧѹƬίɹπsϗҤȒǚĈ',
                            'parameters': [
                                        {
                                                        'key': 'ʹҟȮΎiǷǚŮ˃Ӭ¥ĕ\x81 ŠψɺщϳӆèѠĄ*ǢǄӜԩƠƯ',
                                                        'value': 'ǸïѱɿŦƐ!ī\x8eЮ\x81ЩȂҋ-ǮӱƝћðύɋѓ\u0383gű5ɿ\x98Ɛ',
                                                    },
                                        {
                                                        'key': 'üȌhÀɔ\x9fӳѯӈʻӀγНɪ˚¾ĳЛδC\x84ʜвȚˡǐѧʎúŊ',
                                                        'value': '<Ȑ\u0383ќǊȩϔΠҲ˃ӮŷćԀԪʇ°ӂδԒ-ƝKĘ¾ϭҘɘ4-',
                                                    },
                                        {
                                                        'key': 'ζεŐÐbӽеȆƜɽҌ}ѫƘɝ\x92϶ɤF',
                                                        'value': 'ʾ*ÐϴԮNĘӿƪ}ӺӡΑҬϮoӂǏ˜ȶǅGʒ3ÊƸpɯѰʲ',
                                                    },
                                        {
                                                        'key': 'ϙéÃ\x8b\u0383ȇ£ʰԃȞčåœѪ³õΐǒİԠϟҁȔԃӹ΄ê\x85ÌƳ',
                                                        'value': '˽ҚϡˬÞ\x9bŻʤȧoьҘōκʓƦџҸ¤ʿȦȮNьVǊѴʔ½æ',
                                                    },
                                        {
                                                        'key': 'ӥʅ',
                                                        'value': 'óԆǩDϫĩХѳѰʘΞ~éƯƳԠϗԌӟs°тӧͽGȥyӭϫÃ',
                                                    },
                                        {
                                                        'key': 'ϱıɶσԀŉϺϐͶħŹ\x97ϐīήžĜȭųѿ˵Ɋǧӝˌԇqҍʨ¾',
                                                        'value': 'ΥУДĀ@kѐƫɹζğёIФԮŵӰɨ=ʖèƹѮóРҜĨЧҩǃ',
                                                    },
                                        {
                                                        'key': 'ϟǴʊǧ¨ʒz',
                                                        'value': 'ÜƶҌ¢Fτ\x91ε¯Ц˳RƿщǧӱˤӊĐϑV˘ưǺʉÜѬƽŞϫ',
                                                    },
                                        {
                                                        'key': 'Ƃ\x99ϝϰȻЉŻîäā\x9a-ЭӡȒʧȋĴυҡҿѴ©έȶψʉ\x9f˜ϒ',
                                                        'value': 'è˹ŒʼƴÕҳ\x9dʫɚԆûɟęҬщѸЎ:¨ѣХȥɰƅϯƜԌƅĐ',
                                                    },
                                        {
                                                        'key': 'µǣӞĒǑpȸǡǿƙɛ&ǷϑϭѩûΧÅѕwʢϯɘƿHԘҀǯȲ',
                                                        'value': 'ͽԍϔҝϮȼŇӝʒuòÃљňʧų˲ГΨĵȣďIпʻԚjɢцЇ',
                                                    },
                                        {
                                                        'key': 'ʫʕԙ˾ʠǦһǛџӾѳϢҴϾ[ØΛÊЊǴ\x86Î˖ӄȲӶ˫ɑŎƗ',
                                                        'value': 'όŨƐÁΕZʒѠȽϷĥ3ϭÔԑӳӎÏЀ(ŀϢĂȥʠѹѝ¢ͷ͵',
                                                    },
                                    ],
                        },
                    'comment': 'ԫӭȋŅŤΆíϴȜр˴ħˆɤɜʶɞʙӮYˏƚǗɒºϗǮŎӰК',
                },
                {
                    'keys': [
                            'ʉĆцҌě-\x94ёμ',
                            'ϭͶǏӢ¥ʦʏɭȱ¯ЎʁŉϳġĻNÉɮѣ',
                            'ӊηӑ҇Ѕʱ~',
                            'ʥxˇ',
                            'ΝǣʷϘ.Ϝð˝ԍˇӾ˔ҍǡΆӣғÏҤǔĮªÁʰѲ=',
                            'Ș¿Ѱ?Ȫ\u0383˯óҙƦˣ zí7;ѪlξɷĎȮ',
                            '҇һȌôϵƥǹӁ\x88\x94ΏͽÑǬΩĄĸȀƀƨԔǛɕё˘ΛɓέΟ',
                            'ϔʂyƇМ\xadʾúǊӒ\x9dʲȰĠΆřöӱ',
                            '=aĄԊˡНԠПȮҥ\x85',
                            'ʱ»èÇ΅ˌˇʜ',
                        ],
                    'event': {
                            'target_id': 'ʝΈÜÕӪɴ&П',
                            'parameters': [
                                        {
                                                        'key': 'ȯӷҴ',
                                                        'value': '8ӓБşȈϤ³ʴ\x8aŌɃϔл\u038b¨ĚУ{ʜƐϸԒˡҔќλǚ§Ȣ͵',
                                                    },
                                        {
                                                        'key': 'Ì<ѥѨŵϒˎǠØРɐɳŚΙѰ˸·Ӧ˕ƑȫǤΓʻŽƇ>˚ƦȆ',
                                                        'value': 'ŴϩŕȹŁҚӻ҃ÛϏĈԘЄH¶ҥӺʊүƶϩПTεǓѭҨȖǱӟ',
                                                    },
                                        {
                                                        'key': 'ңӉĲ˥ÀԪǞǞĨ2ƽȈϓӿӲҾΒKũºԖΗӹνрȚ˻Ҟήҭ',
                                                        'value': 'ϪҬȵįºɨΫȦϘ<ѝмƛѦЈҁĸ6Μµ]οоäɫ\x9fÒĩȓł',
                                                    },
                                        {
                                                        'key': 'ƩӚ\x8b)ϪěüƠȷʑ3ıķ˒ϔßǱěxƀĥʬԐǊΜXȨΰѠѵ',
                                                        'value': 'ϡԖҥƵVʸȕɆó˭ʅұǽǎӻӸѦɮϟ\x80ÀКʼ°ɕԣw4ŸȲ',
                                                    },
                                        {
                                                        'key': 'ѕ¹ËšȓǻƏѬ',
                                                        'value': 'ƤҠŇǠɼ\x97˩Ɨ\u0382˝3҉Ʒ¯ѹӓKʉцȼҌÑÕȻÌǯԥĈňԎ',
                                                    },
                                        {
                                                        'key': '¹˵Ҟħɿtϑ\u0382ǗÊūƧЁİщɟįǘÚΠΧӢǂϱǻћíƗƉԞ',
                                                        'value': 'ѭ5РƵÝèϽԤӦ\x9aªĆʀϿZʶΩʕ˃ϧ\x9eɢɳƆҤΧǮϠĻÞ',
                                                    },
                                        {
                                                        'key': 'ǯӃνƥ-ŤԨһŁșɤǨΦщČǚŨϑΘуҞɫӴѾϹӇ҄Уɍ\x9f',
                                                        'value': '˓ųɈm3ωӅӥԓѱӕϳuǚ/ҠŨ\x97˔ƲÖ˯Γɳ˂ΓȁжTԎ',
                                                    },
                                        {
                                                        'key': 'ζЅ,ӱɳ!ȋɳæ[γҚİǧиǸ©ɎΤӴˈȑƊ)ҐӿтҊϼӘ',
                                                        'value': 'ѪӂģρcőѓμʇˮѼҡɠŵĺɢϳė8҂"²ƢȼØͲÎӎ3ĥ',
                                                    },
                                        {
                                                        'key': 'йӺFлʌ\x9aѳǺӻɰ',
                                                        'value': '˟˾\u03a2é\x84ϬњѦѝF\x89ʝÐϹěœˌ\x92ǇЩMӃРηʷȭΡͻőҡ',
                                                    },
                                        {
                                                        'key': 'Ώ]Ϥɸ˗ҿЯĜƹΊҼϻBƐǓƆ)ǀňʇ¡ɏͼӾĒĉѭϪüƗ',
                                                        'value': 'ԞїǮԝȊβÊӶƂԨΐȤʺФɄηҹɪЪԆɀʺǮȢуцÛǯѻԢ',
                                                    },
                                    ],
                        },
                    'comment': 'ˬƀʪϺ×ҼǹʈҫτϸјĠʇӡĿŇ;ÿϏϕŷʤ\x97ӃĽűƕɾˤ',
                },
                {
                    'keys': [
                            'Ӛ¶',
                            'ЎҜoɬƤЉг·˦вˤЫ',
                            'ǜÅjӟƅΥӎԄǿ\x8aóøҜ˚Nżт½҄˖ɚʏҐ˚ƉςԒʕ',
                            'ĴҭӀǑ˪|-ʿԎ',
                            'ЎɟãĪüĕ҈Бȕ˶bȍ˹',
                            '¬ąƽǙǂˡʍӢÙ\x91ϧВɕθYӔφԪжǡÍ',
                            'βѼІaǿϘĉ˪ǢɡΧˌϋȲƼϋΘР·ʮƱĖ˄ˏŞҮ',
                            '\u0381țŶǤe:ʸԃїσ<ÇǐΦ˸ɶѨȽß<ƆƖʹ˼\x85',
                        ],
                    'event': {
                            'target_id': 'ԎÏȑӂӺӜɰ"ÔµșʽҚǇ҉Ҥț.Æ\x8a\u03a2ȏʋÕðӤˤÀʝÅ',
                            'parameters': [
                                        {
                                                        'key': 'ҔвȻјłyӓ\x87ʏӶŨӣ|бƶœΌ\u038bӋЃĄ\x8dˎфǼʏ҇ϐ¸Ҷ',
                                                        'value': 'ӡǄǌψɿӌ]ӭЗɞȬũάʉӍņĸɇԥȅԎǉЖљǐζφʸӌГ',
                                                    },
                                        {
                                                        'key': 'Ǌ\x8cњǪ£Γи£ˇϮʷӼɈȣƹ\x83ĩɳȖ2µӪͱϤʨҒĆΡĔҋ',
                                                        'value': 'ǛƇ~źƕøѧMVԦ˗ΜƒѠĤȾ\u0381ɚƍыѵˏѝȞӔŬыӌƵ˛',
                                                    },
                                        {
                                                        'key': 'Ȳїżύ',
                                                        'value': 'ªеŧHŞ˫PаʠРȽʡӶєΌ-Ə:ėǶѴɉïΈƝΆλЗ~w',
                                                    },
                                        {
                                                        'key': 'М^\x97őǊ»ǝ˖Ρ§ľǠ¿˨ßɛӑҥjӛά',
                                                        'value': 'ԦĒ\u038bǶӬˀǍіƉƵп½ÝљĨҖӦʦГȇĸÙˣ,$Ͳŧ8ҾR',
                                                    },
                                        {
                                                        'key': 'ǲʢ¾ԬˉĂ\x90ǄʓΉȜɕʴΑѪƵԁϼŻË˃˦ÎɫĖŊHɭŦŶ',
                                                        'value': 'ϱźŔIɤ\x80ʀaӜŮjŌƶ±ӦΊҬɃƥTɻǩӰȜȡΞʋɝҝҚ',
                                                    },
                                        {
                                                        'key': 'ĤɳЏ˯¼Šʕ҂ɂƊɉΉ\u0383\x94ţӰӟŢҞ\x91ɸĹɠ\x90ӛɽКԈȎË',
                                                        'value': 'кĈ·\x92\x8dTίíҰԆˣĻPů¦ʚȼӔƛǸʸѴӷŀɲĂƏ˅џʔ',
                                                    },
                                        {
                                                        'key': 'ӿǆ\x90ʠȎÇԙЯΕŁҩʤѰȣĮ ԟʁ\x9aʺ˔шϒϠÈĊːƜÎď',
                                                        'value': '˗ӜвзCɤŢÌǶɞӘžƇ˲ӀωϪȦеʁŲҔñ\u038dȚԑϣ\x9a\x96\x84',
                                                    },
                                        {
                                                        'key': 'ҘӏɺπЀɬǝȡ©ɼzŕƄјЦƜÊÂ',
                                                        'value': 'ʠō~КњĴѹӬԖοӎkӬϗʶUǜΤǣΞɬ£²ŭѱˎЎҼˁ(',
                                                    },
                                        {
                                                        'key': 'Ýʎϊ˲Ϯʄ¨ĩȿʴǄčǔБ2ӈԍǯΡĪÇοϝΜɎɼ9҅ŭȢ',
                                                        'value': ')ӍҹǦƣҰ\x9e#śΌä҉ԝŃЁȞҦԓɩήҵҪîƲԧŵΜ>ГH',
                                                    },
                                        {
                                                        'key': 'Ɠˬg˨ӉөǓ~ωξϏԃӃҍǃԎƒ¯\x958˨ԕȵΆɠӗӖţӦʹ',
                                                        'value': 'ӰӨ˴ˍӇ·ɃӍˆʠɕдӢǇŸϥʵɃԨΈԒƷǞ\x98ê\u0381ˎѽǒҁ',
                                                    },
                                    ],
                        },
                    'comment': 'Ũҳĕƨʬсĉ˂¢ȔɒȢ¬ɽ҇ԄςΖ\u038bɠҙȮɮĮ˛RͶϹʯҀ',
                },
                {
                    'keys': [
                            'ʳϫˊƥοйǩәÇЩHƇ©ҬĐԩ;rΖΌЁњʏJʉ7щЃłˏ',
                            '\x87ƜʶʘԔɕɨюЫŝǔŠѹҰӁˉgȣЏ˙иĄҁҰƆħƶӥ',
                            'ɢΠ',
                            'ϘϷͲлʏȻ\u0379˩0χǳφ',
                            'Ż\u0381Ӻѡђҽƍќˉ',
                            'ӉÁʷÃ˺Ύ˟Ć ӹFğʵΡӒ',
                            'ԚĖǨуư\x8cжʡʸϚϽìùɏʟǷͲʪôҋɍȗДϳ',
                            'pҴʽӖÙʮӒĝʾʛԞѻİ\x82ǴάÝņȸΘ',
                        ],
                    'event': {
                            'target_id': 'IŪʇîɲ\x80ϗӉҬŊԇЩʫǇˤҢȾ~ƺoѻӓ˨\u0378ϦΝȊҐҦǰ',
                            'parameters': [
                                        {
                                                        'key': 'ĮҞţčũĤҲ¿ѦĄƞәǐ˯ԧԢ҆ѭėË¸ӈԩӅȘk\x8aǸȹU',
                                                        'value': 'ʳѪе¬ҘġӽѿȌҌԄԇZԮĐάˁxÛȚ\u0379ʄɈƽɹĵƻMʎƔ',
                                                    },
                                        {
                                                        'key': 'ѷăȺ\x8aѯЌʝϛšȖҧ˨÷ƜɝʎɃ˕·Ū#ȸūӟɳԝĖůɚӤ',
                                                        'value': 'ǲδɖ@ʆӴќȰʳŰѓĳǴǠԄ\x90Ӊ\u0381˯ԜѱÍӭ\x8cì°ȭϭˁо',
                                                    },
                                        {
                                                        'key': 'ɍhω\u038bsǎŪ\x81Ѳƞ\x88ļӿӻЃЇўʩӤĩіѕǧΡўʫí&Ӥϡ',
                                                        'value': '˦ӚUʕԌýƝ4ɥʺԓϓɇȕʅŘϬ3҈ǒĨ\x83ѪʘʖʌӡбɖH',
                                                    },
                                        {
                                                        'key': '˩łϤ\x8aǃʣӁɬνіъʉĜʎКȸð~ӧśҊEιҸàĉҀæÏǼ',
                                                        'value': 'Sʝ\x90\xa0ĆƬhɡàƳѰ\x99ҺkɴȅчŁƲӶ\u0382ŃǃƴÐηƒÕ~!',
                                                    },
                                        {
                                                        'key': 'ǚњѹěӅƤŉ|ӆɄìĘӬӝÁԈĜǐΡáŀļ˖ʺɵȥɀҶˮó',
                                                        'value': 'ĭśӬ&ĭģ>ҘȗЇ\x8d˜ҸîĞƣӊҩгаЙ\x8bϏҁ/ǴʯɑGƔ',
                                                    },
                                        {
                                                        'key': 'ǳ',
                                                        'value': 'ʊ΄ģzѓӯ\x97lɮӛɞƘα|¹ƮȾʙҰɚȳ3ĨȪԨ³ʉǣӶɬ',
                                                    },
                                        {
                                                        'key': "ƏǊ³ɍ˛ȬεƅѷK'ßÒβӘ»ϺΫøǍöԛѿєʱ:Ԁ}˘¶",
                                                        'value': 'ЋȸŞҦͲu]Æνǈ҆ȜҜ!ÍЬ΅ήÛЯďƼԐğ·FăΧʺǿ',
                                                    },
                                        {
                                                        'key': 'ȠāйϒΠÇɏһ˧\xadɒ҅»рNǍ5ϖ˵ƗҬ˫ǵŔMȌȋŢЭN',
                                                        'value': 'Ӳþ»ԦΨſ˺úěδʪԚɩŲ˗ɈʰуɱɄ!\x7fӹ¹X҂ԟгԆΩ',
                                                    },
                                        {
                                                        'key': 'κ(ȣѴſjɾˌȉĢӮͱÔȳήǇħƃóиыЌĮԁ˕ӦƔyЖ\x90',
                                                        'value': 'Яԑ_\x91ƹưǚѴ\x8eγĔgÀǲӾŷѢʱŽбˉѵ\x8d\x8eşόɒƹXύ',
                                                    },
                                        {
                                                        'key': 'ΒȓðƼ\\ѓԃ\x92\\ѫ÷ǂƴͻΰԣтдŖҁԫԈϺġ_єξ˨pЬ',
                                                        'value': 'ÑԢɞðˎϼŧƞȗαƈʭOǵcσÎӅƦĔǇϓǬɖӶ_)-ŭҢ',
                                                    },
                                    ],
                        },
                    'comment': 'ɇɁɀѯ\u0378ĨȧҥѺÃudӟƾΞÚǐхѲĽą\x95ÔƤϽʙŹjϴͱ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'ӧ',
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
            'name': 'ӮӵХʶћȓƪрʷċΎ·%[ΥýʷҖǛƦӦƠƍϥÊҪҪǚŖӪ',
            'description': 'ÎˠIșnϹ\x80ԊΥgɴҘŸԆϦ7ɈͳɘɅѽɐГɄʖǇˇˉƁ?',
            'target_id': '5Vå½ƫӔзÐȣ½āǐΆǂǆњˇÒ×őȢʟ˖Ӌɰ˂ɼĘyf',
            'parameters': [
                {
                    'key': 'ęԜԁͼʣ\x88ҦȄɚƹԏƞ',
                    'description': 'ǶåѧˊʱӯҞPĭ\x88pȓɧ˙Ƚ\x9e\x85ʞùҾʔ˟ҬΜʋʜǆжVϼ',
                    'default_value': '}\x90лéʥļȔҠ«ÿъĮѱȡҽϷđ\x8dǅɸѤΨɥφйԢǭʭʧF',
                },
                {
                    'key': 'ҦȫρȚɋ³ǉʶ҅ƽΗȗԌƕȼË\x83Ϲ\x83;ƈ˚ƳıÇNҬá1ý',
                    'description': 'ğЇ\u0382ƂηͰӑϥƨҸ\x88ҴЇƆɦ\x83Áӷӹ˧ͻԅӆЖʹлʶѕϊʯ',
                    'default_value': 'ƞЏõè\\Әʝ˨ŞʡɽÅ˳ʉҿγцΦ҆ġʴQKԕІ~Mǚŵˈ',
                },
                {
                    'key': 'ɴ£ӷДáȱ®ƈƢƧͿǻIȃ҈ҘԙƨjÕȾŵʚВ\\ʇȐҫƁ`',
                    'description': 'ǟҿºÍǕϪÊ²ŉ\x93ɡӻɾД®mǻ\x8fȋӁͰҰȉƞɕǝάȵĔɡ',
                    'default_value': 'ѧǞrĪĚԄǊΖϭҨϢ˖ΫăÏŹЂ\x8eұЏұϳԅБтĩΤҤɻѡ',
                },
                {
                    'key': 'цϳǎʇ˞ТÙ~ϧŚY\u0381ʾǄƋԭЩятƶoʹȟξ˾vʠФʮǧ',
                    'description': 'ЫĒӏϪȄЅ1˞°ȸĵzϟŰǆδÊшћɢʎΤHѶҫ˜ŅBɧΈ',
                    'default_value': 'ŋȺїƞϠȆǹlƩδʧÐɭǇcƲǁҕǘϩŀŭӦҊƝө%*ĺǨ',
                },
                {
                    'key': 'ҐǝȡȐΌ˴˷ʝҨϐɓɘ˳\x9b<ɨúƙǈŽӇϢʖΌɆґϝÜ[ԓ',
                    'description': '@ќǁΑ\x8aкӏŽҡʡЅ҇ĪѶȵĚ\x8bӧŦԮëҋåʀС˄ːǢĥū',
                    'default_value': '½ɩ˃ωôĄќŝ;EˏǎĕďˉͺūΣĚʪ¿ӒŶԛΚϴçΪɅ',
                },
                {
                    'key': 'ˋ`\x9d!ȘñȃżˢſhеǗǷʩɄÓϪǖӅȻʷà³ҽͽӧƄΡŽ',
                    'description': 'ŃˉŋӀˈƽ¬Ԉ¯Ԭ2ʟОƕϊφJïѹĆӢĥ,ˑΙŗƤΒӛͻ',
                    'default_value': 'Ŋ×ɝïҋɯĀǧŸȴбǳƱҞɱӬһЇŗɛEΩʫõĨǊӿrģĎ',
                },
                {
                    'key': '˂șΘϊʿВҰӮŐŧϤNΰ\u0381χƹϪƴĻ\x8aўϩeƆ˺ɱŷФʩw',
                    'description': 'ƞȒĸͻҴ¾τÚЗЯʸĩɆʁČß¨½ɊѸˀő³&cК˱Ԑгƕ',
                    'default_value': 'Ǖ˵ѰĤq˩ҶӛҖüɐʧľӋӮ˧ʁѽɴӻ҅˓ȷҵ\x93)ƴǸƶӡ',
                },
                {
                    'key': 'Џ',
                    'description': 'ˀňÿ\x81ªѽƷħςĮɹŋȶʺΪӫʩ&ΚͲӇԣұвӯĵɪƸBō',
                    'default_value': 'ғʰÃĳ˝ǥѱͳѵȬӝƫŲƀ\u0383ԪɠԆhƟәұįιԦԪњ\xadԥ¬',
                },
                {
                    'key': "ȰӍɌκцøǐ'ξŔĶ¨îǿ",
                    'description': 'ÒħϳШІɁϻƃҲɧŔpрqǎЩ$JĜʍҒʊϽБŃпǃyȧϫ',
                    'default_value': 'Ą˚ӕÚʜЯ˷ʅÒέЌРƓŧăěń¥MԜ\x80ɎǠİϣӏĮɑβύ',
                },
                {
                    'key': 'àVԊюҔɂƠгƯӒήˁɋ\x8cцƯԘÝʮĹ˝ȊӣϧћȎȽȌǿԃ',
                    'description': 'JҶԡǕė.ä˓ƕǢĺƦŦʹĭǃ\x9dґɼҐŜÃF§ԬǻĐЖȋđ',
                    'default_value': '\x7fΡŦČнԘά˂йʥˏźJʵӛǠǯԦȎoǃȬЌĩùɩҌǦĬ\u0381',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ѦʜԬ',

            'target_id': 'ϏÉɸÙ¥',

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
                    'name': 'ΔΣɯԨɠфˆǥɂfĿ˵ӸȍʑԀУѷ¨ǂψозî\x92ţұǰǯö',
                    'description': 'ғƚːľГŔ˖ƛҽƝтɲӾОΛɖγҷІü˽ΔÚčǋӐÔÏpκ',
                    'target_id': 'Ѡ#üoȕʃÁЏȎϿˆ\x9aVɴÒèˠӡӨȃʈћϷФ˛ƼɽҲΖɘ',
                    'parameters': [
                            {
                                        'key': 'ʐʘΓȸì˟ΒϟͶžÙΒȁϑԃīſьћƣ»Ƽ÷ςƓ',
                                        'description': 'ʾƣ˾ѱxԦė2͵ÃϕūK\u0380ӨˬкԌ˔θşĞMƑƸɈǎɁŎÞ',
                                        'default_value': 'ԏĞɦƤӝΟŇŕĺ\x95ƺǨʹȌθDȆƹĥэȋСŭӓқɯˋ³ң҇',
                                    },
                            {
                                        'key': 'ȃρ!ƮƸϙÒgå\x98ДšÂ!ԩ˝˂çӾΠчɒԏǥԪԗƨʅǈ6',
                                        'description': 'ўΤõϷūԋƜɓ²ǰɮиˀ¶ϣьͰѮϛΎÜδ¾|ŁԞń Ϲ˅',
                                        'default_value': '˂ʖɎ\x88ʔťӟŦƈ0Ɲƒɦ²ʝȣѰƭθɵΪáмyȇŗҁ\x83ʋŭ',
                                    },
                            {
                                        'key': 'ġÈíŦǳӊ\u0378ӆŊjыѽɫßê˞ыīʴjԄ²ƎƝӏѱˊΗ',
                                        'description': 'ѨaÛŗѯȸӃɛӄω\x90ѪΦʗƧʉĭ˼ЄҥƩƟѬȩăɿѣ˭ԉʦ',
                                        'default_value': 'ҊɒъɡōśђƏӑҖΧ¬ǧ˂\x86\u038d+ӫйÍЖӦІ˂Җ˻ǈ\x91\u0383ҙ',
                                    },
                            {
                                        'key': '˧ΦҫɂҪϢЎĸӂ\x90˕˕ЙϤҬԉǟĊϽӆ˗ư\x8d',
                                        'description': 'ØєǗ/ƋɚӆĤJiʇϡь\x8cœвҁӝП˴ĦƽȢŶ˰;o҂\u038dу',
                                        'default_value': 'ƮĄϪHQöĤǜĭǏЫìóϻӆƐϰƭŅϣЄɑςŁįǂɯЕˍć',
                                    },
                            {
                                        'key': 'ŌɎяƟѴȴǷͲКҭҠқųŁǸ˞ɃˇΎˮӵŌD«ϖПɠ°îѷ',
                                        'description': 'ѧ˘ѰΨÕǐфƀџſњĄѢ&ÁǰЩΑϘ\x9eǴèòʐҩҹЖɜ˹ȷ',
                                        'default_value': 'ϧ˷ʹҕȗÜσñ\x84ɦʄϑ\x99ķДԗϕԉĪӟġғWɞл´čɏӏΏ',
                                    },
                            {
                                        'key': 'Ή¨¨żǷʿϐǔҚȀʮgȏгǖƽŸ˓Ԑ\x92вВĆδʦǑOʵƾԀ',
                                        'description': 'œþѵ\u038bqΏΰԋҟΞƢ˨ýƇКͷпhΏόϾЯӒǭ\x92ĳ]ýѠȭ',
                                        'default_value': 'ȥĈŐԓѠĂȠ˔Ӂ,>ëāːϫ\xa0Θ¹ίπăǝǝѲӾţͶť,Ȣ',
                                    },
                            {
                                        'key': 'ţʟ`еɌνǆэɺʚƷѾпͽÖKȡȬƑăЈ«ÌӸҊʞð?\x90Ӆ',
                                        'description': 'ġžÐ6¨Ԏ\x97˸\x84ɏ$ǀďЫƍŸǁ˦cöĜɳӄVŃȊɲǁТњ',
                                        'default_value': 'İɫȔȍ҃˧ùſʢřlǀ˞û҅CӇǹǙƑʜĞ˘ϦƤĠӚҪȱ±',
                                    },
                            {
                                        'key': '¯˶ҎԫЂɛąӌҞǻƚ|ѡ',
                                        'description': 'ʑзÙψͼƃrҠÙ҆ȫȴšҠԪ˧ʷїΎΑ¤żЙғzɾҰоҝϣ',
                                        'default_value': 'ӗÛʉӑ\x95Бļ˳тȜɐѨǜγ{âǷҞЂćõËϠ³ʁĕǔȎѻɴ',
                                    },
                            {
                                        'key': 'їˊШρӶɫ\x87ceϼǰʏˑ˞ӕПʌ÷\x95ԈщȂŃ¶ˑƈΊѻ˗ƃ',
                                        'description': 'ˉεĤ\xa0цɷÁËȬEʇȋƭɈʑʜ·дʅүǭԮùΘҌͷªĝġˁ',
                                        'default_value': '¯ʒƻӅbƯʷϕŉ¤ДÄѩ\x91·ѴĚęĽΗëɸǬҕz˞ĆȉΐǞ',
                                    },
                            {
                                        'key': 'öŦӡѿǷӬȽĩšTúÓɄƣϓ˟Фϡ\u0382\u0379шнɕš΅\u0381\x99Ԛ œ',
                                        'description': 'Ή˸ªӭǟЂɎҖȶшӼӦҾK\x9bƕŬέҥϞľʌ|іsҁĶʣѡ\x93',
                                        'default_value': '˒ʯŤʗʷ4ήČԢʶă)ӄ~ĤZȞŇÆBҩϳèў«ìĬǫͶȚ',
                                    },
                        ],
                },
                {
                    'name': 'ļѨμΊɗπʋνʔȩөӒӹƋȱŵòɾхЮiҚˮ˫\x8bƒӽѬ˕Ю',
                    'description': 'ėŀӴm҆ӷҞĴłƃĊDſšȣϷȟʽƂˬɾʚʌř˝ˤΕ2ʽ)',
                    'target_id': 'ΖuģϜИȧѲÁΦΩ¥ȕͶF:Ǩˢϐńʏ˙×c͵\u038d¥êӍìϮ',
                    'parameters': [
                            {
                                        'key': 'Έǭ˥ԗцӍƺίҕϏʉȝŞɞҵ«ľͱˏ\x9cȊ҈ūœОԡӜÚҸН',
                                        'description': 'ӗғǟƮНѩΘ˒ŖêѲˈ҈ϒϐÍȇ˽ΤűÜӛƱːӆȧǻȀҶɩ',
                                        'default_value': 'ҫ˹ZҡˊɦƭъĸɸЛȾɭ4¼ΪҼʊЯӄʋ¬YҊ>НʪυʑϠ',
                                    },
                            {
                                        'key': 'ӽϱǦEȑΩ˘wŢɶAжί7ǭшҐҎƊū\x8dĺԆ$ɀ\x94Ʀɵɋŀ',
                                        'description': '@ͳȪãΔʎ:ê˯ѠΧҒѥšȍϬșZ&ŬϯşΈǕʄɅ҅ΒóҨ',
                                        'default_value': 'ѾψŽļ˳nҜĪØѷҩЋΜȑͽƿƻ_ШȬË@мǔ϶ɽԦį\x82ǖ',
                                    },
                            {
                                        'key': 'ʙʼʓԥΞĭ˞ʨĽԑÒȏҪΆ~ΣǪԠȨÌԗАʇӚҽ-ҒӽͰ˺',
                                        'description': 'ʙ͵ŎǺϼЌɲҒһƵѵˀΎʤŊ"ǥʿ@¢íӿӢϳʔ\x80ʙʥӋW',
                                        'default_value': '˙ǁʅɄrσЅεĕӦƩϪϤϸҗǒҧӾǺÁǷƬğǺҶʠҷŮњ˂',
                                    },
                            {
                                        'key': 'gĺŚťƺӇˠčǚ\x96Ӻ\x8eʉ¸ɚҧºдѮϫžơӑɣɲŀqɂǪɼ',
                                        'description': 'ԘŮɮīѺŖ\x99МƤIʁϲťÃƶɌžŌ˲ηҵŬƷǿkʲTжҦĜ',
                                        'default_value': 'ɈǮˈǂ_ŌҪŀǑϛӡΎƅó¸¨ΊϠЄљΗӷџѕґǰУƩ;Α',
                                    },
                            {
                                        'key': 'ŤïgϨԟұʗĨ\u0380ҩҬǡʿƼķõ˖ƫƲɇԀÃ\x99Zŀʓ¤Оʁɓ',
                                        'description': 'ʆc¡ŒƜÅȊҥşȓɓӐԦԕȼƒŮĸȴʢѨҋӛƹӸӞ\x8fΚƨĕ',
                                        'default_value': 'Ͽ¸ʡҚÝϝʾЉ\x95¤Ȗψ§Ѡf$όƱИΊӖΕ>Øƌ·ʹȣŨ`',
                                    },
                            {
                                        'key': 'ԃ',
                                        'description': '˹δ\x84ЧԑϲÀıµͶϱ\u0383ҭŮΏũəФǾϚɺʕʖϪťȈΖļȐɒ',
                                        'default_value': 'сɇ˕ÅƱѢβчîϕПƮȱÉʹŤҒʲәϛǚ˃ɷΟͱ¿ùʈ0Ʋ',
                                    },
                            {
                                        'key': 'ŲʙǹÃΛʠҾͽѳɿʛɾΣWѭѮìіȿηJĚӔŵӬΏšIŴÌ',
                                        'description': 'ËѶƾǀ϶˂Ǔ\u038d\x9dѕÚˀҼƞO˴εφʢбĬ9ӷϕѸϧӹ\u0378)¢',
                                        'default_value': 'Қά+\x86ΊʜԙδШ\u0378Ĺ˻ҊçЙ±ʼ˵ѵЎѮƊĽԅиАŻƺȺ£',
                                    },
                            {
                                        'key': 'ʳ·ҩʔ˴\x9fϵ!ȩφʁlӞŽúʄгǳοǉŖɛǑΚӫѮĸΜɼē',
                                        'description': 'ȟӧʀҊҦΫЁМ\x8b¿ʙȨ˃ѨaρȢɣʂ°nƠӥ˶ωÇΧ˳ԏӆ',
                                        'default_value': 'ƿƠҢɿ˜#ƒΕԝƷ»\x9bYɅů\x95Þ\x92ΜQџ˾ιľѬWΖȦuΧ',
                                    },
                            {
                                        'key': "PǆĴįƐʩ˵ԃѷԒώζ'ʔΘΓҭkģӃä´ͻˣФөҽσɚ>",
                                        'description': 'ωńģfӆƸО˛ԡӂŧфί˟ʌʱлЕƀBūǓύɈӅԈđӹјҊ',
                                        'default_value': 'ӡΓ˴]мɯ˚ӻƺЉr¯ȝүȽďξH\x85\u0382ȅϡӧҽȕɤˏŬæɘ',
                                    },
                            {
                                        'key': "҃³Ě'ĚҲɤҤ˯ħνʮ˳ˬɞĿɅàéх+Ȫśϫʰ˸Ɨұ҈Ѕ",
                                        'description': 'ŁɁξƥíƾ\x8cԂˮѫþǝ˼ÑȺϝʎ\x84ʠъ˳ѳŁчȋôͳҶ<I',
                                        'default_value': 'ɥĺԃʢϳј¸ѷ\u038d+ŌɤдċУҨӬϣʒԤҷԮǶѩʼХӑ¬˷\xa0',
                                    },
                        ],
                },
                {
                    'name': 'зѮğ˝ĒÛѳʏӬϳʺȚ҈ťV˦!ǝǵұ˓ŉΎɉѓʢˍɐюК',
                    'description': 'ʱϻ¸мɎȟϠǣ\x96ԍʹȜμҟªɰΪϲƤНϾǃȥЕ\x88ąӵýΠѹ',
                    'target_id': '˞ϐǃƸ\x88ОpҦʯΊͲЗϕ˜áƿƲƫɣ\x9aŤǋăɉɮ͵ɒўƯL',
                    'parameters': [
                            {
                                        'key': 'DʷҐ7ɤӀȽʞЁѻȠѿ^)҅˲\x91ǅΠ\x7fǞɖM¤Ȁ{×˒еӗ',
                                        'description': 'Ή°Ϧӓþʤéьàȷ\u0379±ѶǅËʋ\u0382Ē˪҇ƙƥΨҫέėǼéνɟ',
                                        'default_value': 'ȫȭŲѤßЩɦǛːɽϚƖǞ ȌıεӇƻž«ƈϨ¼ϧʈώ҃ԍâ',
                                    },
                            {
                                        'key': 'Ą',
                                        'description': 'ϴmԑħɁą҉ǾΞ;ʩāƐ˟ɦǈăфϷ˼ʑȕѰЇϡƵ˫ϷȉÒ',
                                        'default_value': 'ɉʌķĉXɞǋħĸƆËɚτҴ\u0382ѷ˘Ї4ҴƉ˚ÂĚИԨ¨ɻǇ·',
                                    },
                            {
                                        'key': 'ˁ8ʁʍЭĦćӢŞ',
                                        'description': 'ưͰӤΆҸď^ԃʯ˫ǿԋƠ\x94ªÁɳΣƙМԋĤŵǔӱʿ\x8bÅšЩ',
                                        'default_value': 'ȈĀϾ˯ӊԍ˫ȥҡŰáʁ\x8bϽӑèНƘҺҩ,ԉїеʣϕɆƵφӂ',
                                    },
                            {
                                        'key': 'ЇɣњdɽԆÑԢǳԄδǬӾњþʮƕɘȗ+',
                                        'description': 'ƗƯҝʱҦȧȖӸĩϓоƵϱXй҅åϛǒ¿˳ЫƒŽ˄ŧӝǝųÀ',
                                        'default_value': 'ЋӰù˔е\x80ϷТȐ˅üīŋǦ¯Кς\x87ΣѧŇìɱƵλ¸Ųϔ\u0381Һ',
                                    },
                            {
                                        'key': 'ɐШƤLӞȞѧӑԟδǄʟǇϳñǡ\x92ɴɽŊȆΙӨȠɂ˾ӃфǨЂ',
                                        'description': 'Ӑaıţ˴ωšÕʺϰȬΰįƞMԑ\u0379Ùҳ\xadəáȔЫЦaȣԜ\x8aϮ',
                                        'default_value': 'ƶȥѳmʻǲ¢ϿşƾԊ҇þɍʖ!ǓƴǃҌӍĿЧ˒нѦԠ˹ԍǃ',
                                    },
                            {
                                        'key': 'ņȂ\xa0ɧӤɺǦ&\x81×ΉŨÆ˰ÏҞȤŶ#ҴȇϠҵҘ{҅ѼƼɠҵ',
                                        'description': 'ΘӐсѵԘʬˎ¯ϫҷǱҡҠҠʈɸƷƛԕȬ¹ЃăţȪҹ\u0380ǧԅƏ',
                                        'default_value': 'ϟʠʃùҏέËƛŗɡП˟\x8bȷȘʱ"ľʇЄÒϷ˭ÆӒʲӅɪǨң',
                                    },
                            {
                                        'key': 'ľ˄\x9d˸\x8aʩ˧ͿЫϮ',
                                        'description': 'œƙοɽɞįɽӹҐvȯŃԜŐϨΓϡɑʵЈӯ\x980ϢΖΗӪ\u038bRЪ',
                                        'default_value': 'ªɬʖөùͼʽѽ\x86ͶЋ͵ǝвϳλӌí˥ȆPϴϓþ¦ʎʹǘЭˊ',
                                    },
                            {
                                        'key': '\x8fßϥĦԟДƗ\u0380Ű\x9aǗɭϫɐ˹ΧȾ\x82ȺЖ`˪ΰ¢ЍϔҶсǞƕ',
                                        'description': 'ʳЉåΌӋοˍäǬȷĩу҃Īţe҈\u0379ǒZ\x88ʙƘǆƻƁˣԠȝǖ',
                                        'default_value': 'kɒĽǃ:Ö¹юƏĲƉΥҩťņҭŊƣӶԢŏ\x9bːȷǛьɜÑɺ5',
                                    },
                            {
                                        'key': 'ǺƾҶΪĩƣ\x9cƕ{ҋъɶʤˡРǫѭ`ĭˀʭЁМЗξǑиɹͶϖ',
                                        'description': 'Ȳ˘Ͻūϖɼ\x89\x8bәjmūҏʌ\u0383Β˘ŋȵŐсΓ\x85ǱЀӧÊυϼΚ',
                                        'default_value': 'ҺñѲĻҎ˲ɧԨѝҋΪʰԛ˛lǑθҘňǥȧԌɢăÑļȷɷ¬Π',
                                    },
                            {
                                        'key': 'ą˟ɇÏ³ПŃàάχҊϵϢƄɚŁŎ',
                                        'description': 'ʒ¥\x8dСƶơ-˳6YŻҌ\u0378RȤ¿Ώ&ύѐϴ¦æaǋԌǂϲȭ\x8c',
                                        'default_value': 'ЉăÇҩӄ\x90ļʤė¬ʡʣʫBѠΛǖØȫ+ȂвŇѼɏ˛ÃӽÆà',
                                    },
                        ],
                },
                {
                    'name': 'ǁӰ\x9fȶѫЙƻԐ%ѯkźѣвǭэ˜Ϛ§\x7fІҵӛơˬЎƺвӚ\x95',
                    'description': "ӿыƯΑ˧ʇ'ΗԐƑԕϣϘ«ʪѮǥɺӝϘ\u0379ʅЀԫÊɳɠуθү",
                    'target_id': 'ĻùЗӐόđt«ĵʱ#ŇѾЀԩ˰ɖˆ\x9cвќÈԖʫѺ˵¹Ɛ§ӥ',
                    'parameters': [
                            {
                                        'key': 'ƿǾ˖ɫя',
                                        'description': 'ҽԝùɹʈƜƗрɈԝ\x99ωΣэŶӋ˶ϧʠʲѧǥӟԕɣχţ¨ʸŏ',
                                        'default_value': 'Ĭ¯ˤ˹ә¾ēҐ˦үǡƣƃɣϯҝɡάӭԅǆпȃĶτʣІÎϨ˯',
                                    },
                            {
                                        'key': 'ȲƱȶЈϬùǶς˭ƈћʗӱƥЇÅδѽĚȨțƇǠ\x97Ź¶Уˠӷɧ',
                                        'description': 'ȫ϶ʹ\u0379νɬʬӇԘǮ҄ˢТѥИғ˦\x84%ʂ˗ńԬŋԆϷžçĳΞ',
                                        'default_value': 'Ұ{ɃūІК:ǗʾǓѺһȂłЭǸīҕԂ˯эѢєʆ?ЅЦǨ˫n',
                                    },
                            {
                                        'key': "ĸ˨Śԑũȓξ\u03a2èȦѯ'\u0382Јȣ˜Ǌʲȴ\x93ȕэĻųɎƝ½±˺ȱ",
                                        'description': 'žσ\x9bӖɃƙӬáфԘЀʭπˈͷϳȶѳǫËɇщԒ\x95ƒMɇӋȱÌ',
                                        'default_value': 'ΫïŵȦɍİĦӵ"ƩГѭʫϷѶťґσƦǏȱȁʓ҅ǸӋԌЧǔҍ',
                                    },
                            {
                                        'key': 'Ŗđ',
                                        'description': 'Ћм×ѱԓǙϳЉƋȌȵːȗÕӖӞϞʦ\x82СʵњρŻôѤΊˤ?Ό',
                                        'default_value': 'yg\x9dЗˋƠӻԅƢƢħѷȸжÓ¦ǏИ˨ҘіԚʐųӲʏȈˍâѻ',
                                    },
                            {
                                        'key': 'ʼʗʹΐďʤʵ9ƍǗ´ʩ(ƱŗҒɧǊǣưŢʙŞȠǄ\x8aɃ\x8dȕɽ',
                                        'description': 'ø&ȤÄΚ`Ǣ¾±Їҩϭӓ˴Ё\x9dьԘѫҬҋɱȪ³ćӁƯÔиI',
                                        'default_value': 'ƙɻҞЃz´Ų\x8fԬŶƱĊϰӜȗтҠƫǨρƉÐи¬\x7fCȨȤԢ<',
                                    },
                            {
                                        'key': 'ƒǪ¨˞Ϲäʓ˥ΏЏ',
                                        'description': '\u0379раҥСƫԁµ±ЁωĂ\x99ҿΌȄбʉɨѩƳҡунɠɢԗɻ˼ȼ',
                                        'default_value': "ȍ˖ƟůҎlÛʦ\x87ÈǶȵʼǈʫ҇ɀȴѵʷѻßɅχґ'бѧĻB",
                                    },
                            {
                                        'key': 'ӣдʳ\x9dЄɇ\x89ӠȌԦȫˢ¸˚ʁҘТ˰͵йɆ:ѱϴęɢξħƬл',
                                        'description': 'ЎĒ)ȗϢȾɄɥЋƇԌЇϚKĐiӮΠƂɺɗAÑĪΜƲҌԌɎʬ',
                                        'default_value': 'ү\x8b)Ґ ΊɜЪӱУǩȵϋӌйƾѫғʂӨѲЮˣɘűúŧǨԏŉ',
                                    },
                            {
                                        'key': 'ĠӀÏz×ƭ5ZЂƸѹáҳōɜŁƺ\x8dˉϟȟɹˈʦӋӕҦӁŞƖ',
                                        'description': 'ԍȒĹ\x9aΪǕџȈэƀ\x91ΚҏϮv1ƫ?ˎҨԔLП˵ˆΰ\x9cʃāH',
                                        'default_value': 'ʕ0WΝȀОҍãƂˠΗČӜtŐ˄ЍǦҸŒӁſÊȉǠÖѢȵɺ%',
                                    },
                            {
                                        'key': 'hNʦżġǿŊȿÄǷŨҐЂɎϝ҆σгˉыѾНʸϫɒʌȘǪиɿ',
                                        'description': 'þŮȬІǄŻDčȐɢȎîԬϡ',
                                        'default_value': 'Ǣ¬˃ƨ7Ϻʱѣ¹ϺǏ˟AѻƾӰĻϟ˗ˍТ˻Ѡнƚ˺ǋŹĳV',
                                    },
                            {
                                        'key': 'ЅȜǅѦύԗϬҢɲÆŇʎɘϙԇĳΛȾī¬ǺΠЃвӗOϪʘɯω',
                                        'description': 'ӆȑʿмιҼƖʶÑāЀЭĐΎGȒ΅ùĖǌɣȔȷŞŸʃƗKЌʎ',
                                        'default_value': 'Ⱥ\x7fβӯāϭɣɶCˬӳқŕɕſŕқϷҍΆӯǯDƝЇ΄ÿˉİҫ',
                                    },
                        ],
                },
                {
                    'name': 'ӎŖҫοzʽ0ԭЍΘĆԪ^ѿʽ',
                    'description': '.ʳΈÐù˚Ѩ˴ǃƠҬʭʝŷςӯϸČ¯\x97ɃɆ]řϤ\x99ԗШŔÃ',
                    'target_id': 'ЃҤǊѺƃĎČуфŗʓϻ³\xadφ˵²Î϶ÎȆт˺ɱƼрňȶţ±',
                    'parameters': [
                            {
                                        'key': '˱¥Ȁ¤CЇЧŻԘѢ¹ËӯԎиҐØƠԨǢƩкɬɘ¢lĠȿQƵ',
                                        'description': 'Ÿ\x8d}Ӡ˫ϸлɴӚ˅vӁˆćԕϜӫĿЪЉɶƒˁήӤ\x86ǯԝАѫ',
                                        'default_value': 'ˇƨӽΰяӞʃĤ\x85γќ©;Ǝʲө\x97˥HġˉǹҙÍθ˦˽°ϵǚ',
                                    },
                            {
                                        'key': 'ΫҘϖġҘĖȕ$ʽӽȮҰ$ǐԝŲȰΜҨцўŲȲV',
                                        'description': 'ӆϴΈԃÉgǽ˩ʼȽĤĉҤΙÇ΄ȪōүðҤąʕІсûѷϱǔ˔',
                                        'default_value': 'ҡϝЂ҆ҥϦʴƣї\x82˒тĮſҙĉ\u0379À',
                                    },
                            {
                                        'key': 'ԔǪʭɍ҇ȘЋҮʴͰǒϢǚұԋіRǧoҤǶ',
                                        'description': 'ɪ˰ìˋưљYǈǂ\xa0ҐżLͽZˡɸǿ Іϸ\u0380ԐӤȳŮӕeӾӎ',
                                        'default_value': 'ƳğӈʎX\x96ȏɍӴͱ҇οӛɥ\u038bĮΏHӫӺ\x7fζӓҘ҈ћΩԄãǣ',
                                    },
                            {
                                        'key': 'ӓź҃,ҬÇǟͷǒԚƟЦԔŔŅϬΧćHЈФ',
                                        'description': 'ǪԙΔӺΦԥŁõѪ\x83ǅΨɧÂ\x805,ȩͺӠҾÉ˅Ɩ˥\xadԊĞϓ\x85',
                                        'default_value': '^ЯкŰ˚Ƶƣ¥˾ЅƖɝűɍɊɝeŅƆбȐiʧӧӗŭˎѠϮĺ',
                                    },
                            {
                                        'key': 'ǥȘ/IԤÜϷѯǋÓΓ\u0383ӊҚʹľ΅ˡЩĬž',
                                        'description': 'ϓ7ɟßĩɠŝҡЃSF6(ӋĘò˾\u0378ʗΫϡԛÕíȚϾϷ¾ɍӝ',
                                        'default_value': '\x82˫йӹҺh\u0383ɮҼôԒҾɨǽʪҀ\x8e}\x9f*\x85IɼEѸ˄ĕγĤ¯',
                                    },
                            {
                                        'key': '·ʲȃb˙ȑԝв&ĈƓļ\x80ЫʫҲѮŻπҤąĺΰçȳîˮЁӆĚ',
                                        'description': 'ś҅ƯԎ˨˓ϖǷ\u0380ŋҮƽɚŰԌ6˃*ΦӞǴ҉˂ĘԔŐǦη˥у',
                                        'default_value': 'ԧЭ&ѱŰ.\x87ŞϻŬΡ˃Ʃ˶Ŗɪ=Ɣ\x9aƷ9°ԃ;˓ЮͲƑҿǛ',
                                    },
                            {
                                        'key': 'ƺѴǜЕʃŉËиԉɥѩϒӓîӑѓťԗɂǿђȬȯǮ©Ɂ\x8dӕӱϦ',
                                        'description': 'ѤϾǐ¨ӅŕŨқɄ2Īǡӆ˧Κԙ˝˻cоҨɚÙʿДƶƤԤIɵ',
                                        'default_value': 'ϝɑӵɺƬԫåёɷŚȲxÁŬϏӻс=ŸàÆӽω\x83ʣZːϪϒɓ',
                                    },
                            {
                                        'key': 'ˆOё˝΄ˡҳњƯӆ˳Š&ŸˊãöEʀėÊЩҖ\x92˚ȻӐŴ',
                                        'description': 'ÄŜУԮʢŮШϠČ\u0380Ԝʕ8ŶɻƥŮ˺Үŧє6ѳѶ\x93Ķɳʕʇˁ',
                                        'default_value': 'Ԑ:@',
                                    },
                            {
                                        'key': 'ɀѾЎȶ&ǻȸΖѷ\x9bȀ(˚ԟĕǀǇԤǝΒǢˀЖ˳ȩłҀ]ўϹ',
                                        'description': 'ʝϮŗΏÍǎ«еȠʷԚƥɜʴϞŞĀήȾʜπюσƚȷПȾèıӽ',
                                        'default_value': 'ØƶјĢԘ ϸâҁԉӯύЯɐ˄ϒĳˁΐɆшЀĦ½хҴĜʘĔϬ',
                                    },
                            {
                                        'key': 'ѬϵʉʱͲЋȝĨďԌԍá"ʞѵĠŝƶ',
                                        'description': 'ǖҜ҈аɄɥɋϢȳЧ҅ѢʮɛƱҶ:ķÈϴʠƤȧìԋ˫ȎȊϷΖ',
                                        'default_value': 'ԢgƍTƘ÷ɏϖӶ͵Ĕќ˓DϦWNÛˬΘƨɱ§ƿſɰˆЄʔԙ',
                                    },
                        ],
                },
                {
                    'name': 'úӘ˥χʼœĦÏϐΧɗɦέ˄¶Ƅ[ɩΦљDRŌŷĻņΡŮɓu',
                    'description': 'қɗШЛʍʥ˲ӶңϛʫsʾŀĚɐƯǂ\x80ôкӞӛѡ˸¶ǥΨ҅Ԥ',
                    'target_id': 'ŋàʵRɤƃȈƇɡӐȈЃåǐnĹуΩ·ȕ\x9eĞʙǶʜ\x9aҨόʮB',
                    'parameters': [
                            {
                                        'key': 'ϪʊӠÒʨяӳYϿϣžɚ®ȫɟʥПџҭɩBˣˆԥЧśǅ\x88łƁ',
                                        'description': 'Р˯PƏǠғѾÚ:πšƒЕҬ\u03a2ʪʚѵÿȇʄɝŤÒųɏӟɏ˵ԏ',
                                        'default_value': 'żӪѺǍdȥƻ¾ϹШÒȧơĭԟЩŸŝ¿ίɊàʒǌƗƩ\u0381ΝƔƵ',
                                    },
                            {
                                        'key': 'θϡѢʳДǱєÿϹͻȩ\x88тë\x82ҲʛΌƼϒŘĳЩȯԬϮҼΎЭǏ',
                                        'description': 'κѷмͺɥӺ˺ơҜ\u038bÆǙȰ˦ϛПѿďӰёϠИȶƻåЕӴńє!',
                                        'default_value': 'ɕîҧͷαњΩʷɼӳ҅xƀˤƪąÿьȩчØɕҫ<˫Еʇ\x97Ӷƙ',
                                    },
                            {
                                        'key': 'жʹχØ±ʬ\x98цɼѸPɎѕҎ@ѻĘΙЯ\u0380ĬӚʰòŎʆӻłċ¢',
                                        'description': 'żȗȟƆ\x9aґʦТӤÐ3ӑѫǜϺ˃jǤƧŹÿ¦ȝԃļҹƎҙɅɅ',
                                        'default_value': 'ǺЌӄǕвІ\x9fϴȜį¶гѝńȢ˖ħ˱¤Ţҗ҂ҷʇ\u0378әлƉÜɎ',
                                    },
                            {
                                        'key': 'ԥΎćѫɲb˹',
                                        'description': 'ƥϤɭӊε¹ÚВĊϞѾнƂӷУԝȻȓҜҭèЅɽˊӛɺͱȨз\x88',
                                        'default_value': 'Й0ѨƏѐԮϧ˓ʒţϮǤҺƏҢ˭êɯɱːѭȎ˓ċԏa,ӘÙ]',
                                    },
                            {
                                        'key': 'ԄѐÀȋг>ɞƮаƫӥ\u0378ҎҐҕɓϹ˖ԒUȨ',
                                        'description': 'Bȓ?ßǄ˂ԄҕƆԮ\x7f\x9bӜɻOÝȽϣɈ҃ԝɝь0ϠƟРʇ˕χ',
                                        'default_value': 'ҦӚԧƵӹЉ˴ȢpԪѥԀɍˏƶϗǧˆÍʋҳµӋȾōҳǓȴ3˰',
                                    },
                            {
                                        'key': 'ԄĎХXҹǂȰǪуŘϯӼһǏȳřςШȓÊ4lλѹ+ø҈ӠҲG',
                                        'description': 'ň÷ɼǤΦ˼cÕĹ˕ǨǸȃʍӷÖўŚҗ»ʳΣ\x90\xadКǷȫԋѱŠ',
                                        'default_value': '˻ŲШʀǀ΄ʼ˨ĨљҪa!ѡѵԆˋșɵуĒȱ\x93ĬȯΒ*ǪƐȍ',
                                    },
                            {
                                        'key': 'Α~\x8dňњąǹƹӏҍЍљӍ\u0379ǕԢ:\x99θĚŢüɐŭ\x8aɗѭƀǷ\x8d',
                                        'description': '\x94ѹԧӘʅҌƔύħėPПơѻѕԁϭϭʹȓǹԪɡʝӹȥxΚӚѰ',
                                        'default_value': 'ԎÀ\xad\u0380ɌɘǞΣˈ˳ӢŅвϾ«ͽҳMҔѯǽĶѫɎȹıЅұӏ)',
                                    },
                            {
                                        'key': 'ąԓѕʥϦʍӨÝԙҸԂΠ¨ÑѰҥѹˣdÝ*ͺãĉĲ¯',
                                        'description': 'иҽˊҵԚɀĬÅέȣɄӡпɦïβ\u0381ɞf˰Ѹ\x91лδɟʸ%ïʄЧ',
                                        'default_value': 'Ɨ҅ӥώyƭƜJǊΞЖүӂɏӭ]Ϳ[®«ìȜηłɔɐԕʡ˱ӷ',
                                    },
                            {
                                        'key': 'OƗОɘ÷ƃĩõҞρѠєЛɘ4Ű҅ϭĨƤǹȻɉʄƟĽ\u0379ũøҞ',
                                        'description': 'ξӺO¸ǂӳӍӀљκȠƯYΌЁ΄ƩìʹȰЅѲƙԢһóү˨ʤÆ',
                                        'default_value': 'ȞӃύʕԘąДΖľ\x86\x81ҫ\x82ϰɏζҌĄǓЊПцLȃθϏɗƽeŎ',
                                    },
                            {
                                        'key': 'ăѴͻΏͼʄʄʢҜȭDИəȎϦŎҝЈСсǋ',
                                        'description': 'ФϥДņČɑŌѩŅԘʞȎǦӪґÆ˫ҳĐɗɧȥɳ®ЪΆħƭЖа',
                                        'default_value': '˄ԣЄƇӆƠı˂\x80ИǊɂϟӫȫɤˡȼl\x86ӝŴŦèԏƨНЛKо',
                                    },
                        ],
                },
                {
                    'name': 'ΧȿŴ҇ƸЗөҙͲ˨ʑҁÃjİ0ʆ\x81ХÆΫ΄Ҧ˧ӞԄĺ˶OѺ',
                    'description': 'ˊ\x99`ǓʶŃ\x9aҡŌȊфΚÏíԩЩϜӓƾ¦ӵ˛ǇǑΛʬӐ·Ͷԃ',
                    'target_id': "ˑņÎǔԅϩǂʽŉʜ9ʤØĵĉϚé'",
                    'parameters': [
                            {
                                        'key': 'Mԣ\x9fәҰtξÐȐȲʋ',
                                        'description': '?ѷЅȃѰӐɤϧʟŁͻђFċª2ƚχȷНĆǽȗҨΈҮϙˀȸŮ',
                                        'default_value': 'ɻžşӁʥά4ӊԢùЏƦuǥ˚ƩǠӾѩˁ|҄ǎʮñ1Ӝȕ\x8eɗ',
                                    },
                            {
                                        'key': '+ȓSȿиÚӅĤȩ҈Ϫņüи\x91řú˱íÛŲѩÛ\x92ÃΓ\x99οɞϝ',
                                        'description': '\x82ЁӶΔ\u0382ӌʗӂIŴ·\u0383Рõ·˖ͳÀζƨ¶ӆ\u0383ȸəȓӿήåƳ',
                                        'default_value': 'ƤʱσǺϽԄˈ҆ȤӳСΓ҈ŉNɔѨ\x93è³ơґӬcȞǑХǨŷȦ',
                                    },
                            {
                                        'key': 'Ō˕ȣіŃ±ɛʋĥǒɲǅşéìǵϜķʪλ΄ńäІ\x91ƮΎΖǶ˺',
                                        'description': 'ĔŻаДŋԋǣ=\x92ΧѕʯÕňķƸӏͰɳ˃ÛÊĠүŤWŋŵ˼V',
                                        'default_value': 'ʗǌԅ-ÆϝƁȹιǸҀțΏΐ4ԂҺʡʥɵГųЎѮͼ˞ĝҴǫʊ',
                                    },
                            {
                                        'key': '˫˰Ӗƕϔ\x91ȉЗЁƴƻȔΚ@ʹӘ\u0379Ң',
                                        'description': 'ͺǾКβƇҍŮʓ\u038dċĠǋƪΪͿЫʱʇkžʯӹFРƓɁφž±£',
                                        'default_value': 'ǌǱĉůЙΡǔƗўяŃ\x99ѺӥЇă\x8aǉĝňɕЗϪɿ¢фԓʞίϯ',
                                    },
                            {
                                        'key': 'ǉ',
                                        'description': "|σ\x8bӰ˛ʾЂſɤ˼ξţӨˌстʻ\x95ӌ'ʖ͵ĒӕPÔԜɕϓѷ",
                                        'default_value': 'ϰʸѨƈҲ˸ѽҴΈÌŌɲ˵ŮԛЬӷͰϓіȷôʆ\x82ǉӗяhȱϯ',
                                    },
                            {
                                        'key': 'ΚȾԩĥɏɤŢΒ˴Ęԏ;<¼\x90ŧ\x96ŗǨԛˣɢӷГŲӃžƿѢɃ',
                                        'description': ';˦ӼԞǎ´ɎĎǃʤӛ\x92ȜȌɟ¶ŭƃҎÓҩÙìӸҐǻЅҏνє',
                                        'default_value': 'ɷ͵ʌƯǮϿЖϋЦʷßҤʓѐÚљȢӌfԥëѯɑȺǀӳˤÕщв',
                                    },
                            {
                                        'key': '¬ǘə',
                                        'description': 'öΰ˞Ǣ\x92ŕĶʷuѡµɔ\u0379҃Ω\x87ſɇt{΄ԌрÓʦ<ȴϞ\xadр',
                                        'default_value': 'ǚĴʴƏNŞӖщϷԒMԗƳŊ¼ѺɲΊΔʅ2ȉıфԓʦЉǎЃ\x92',
                                    },
                            {
                                        'key': 'ɩ\x97Ϩ\x9b˚ϵʾƗ͵ĳŴɏưϰǾӤhϢТѼrɌʠӤǫ\x95ρ¦Ƙь',
                                        'description': 'ȁșǨӖŝǦɄ҄ӧìãсӇпÝǘǣҦӀȥƝЖżҭЪҰѨ\u0383ǄӠ',
                                        'default_value': '\u0378ԘĄԆǝɃΕѿƱҹҟƙϐЗyȌŭŉ5ȽǼӻѺȭǦKBɯҚí',
                                    },
                            {
                                        'key': 'ɪžϰȐΖÉƜҍшŢ˩˾ȸˤ\x98˫˵ƑàǝɹðҸп˾',
                                        'description': 'ιɼİțĔӔ\x99çĶЙԄΫӏКҏ\x9a=®ԟҦǠĵӛǷ=qˮҮǈȃ',
                                        'default_value': '¦ѢӉİ\x81á¯ˍĒΤ^Űԕ«Ǝɟѩцɰ\u0379ȤδʜрhШëʜˠǒ',
                                    },
                            {
                                        'key': 'ư˩hʴƁʹЎΞӈϩȷԐζ˝єȉћ-´\x9fʍĎӫʲŋĀ{ŀԬǺ',
                                        'description': 'ΟϺ5ħǪñƨҩɕʬǫʄɒЦѫʫӋŅǅѨĈԣɌƿʌȑ#ԝʌφ',
                                        'default_value': 'ԇéH\x9bƒVƟðя˧ӕӟ\x84Є|ǐԛʹʕʐöðĪtŏüΠɗѿζ',
                                    },
                        ],
                },
                {
                    'name': 'ӥĄȬˆπˊrќČƒӳXΌȂϭȢϚ\\ǻɣĐʆŅʪȍ{Ȁʻмſ',
                    'description': "ġ'ϰЛΠɚζĢűȱŜʫŵÕRʢΓ»¿ԥϋʒhʴßϾѓZɄϤ",
                    'target_id': "ѿ'ΣƸз°ԤǽÝчĳѪǊΔ£ʞӻԈ\x7fɢL²˘Ě˰¿Ԍ˻Ўř",
                    'parameters': [
                            {
                                        'key': 'ȄŢ\x8aľąǂ҃Ʊ[ʵƘϢ·ϳNӀūΩʁЅȁΝ|¨ԬũѰв\x86Ӻ',
                                        'description': '\u0378УнхaŦαǣǞŪͿɶԔ\u0379ŉ\x8dŪ[ˍҸϭǤϮѹƘӌˏԄƁȮ',
                                        'default_value': 'ϏˊԟċϤǏϢ˟˴ɯʗ®ӒǉWÇƎҰ\x92ѻʥħϑ\x7fǶзȊ/ØÃ',
                                    },
                            {
                                        'key': 'ҋ˭Ġ\u03a2ǹT΅ԇǴʰļ\x83ѴгŀмyO%Ͽ˔ţқɥγƗњӂÑш',
                                        'description': 'ѳˢȡӇʼŰʴʁéɕùȕόɑŴˤɘВцkѱԌȾť3ǘǛχ\u038d(',
                                        'default_value': 'ӼΟӬ¿ȓʤ҇ǄČ»\x9bз¼ӗГ\x8fEҺԚȐFѮžǏŻűӟńҮˉ',
                                    },
                            {
                                        'key': '½ΈЧ]ΟÕȁ˒ŸєȆŵǝŜάΩśΟ÷ρśʐΌʁÌͽԬ#Ɔв',
                                        'description': '˚ӎ҆TƭқϞƑӓӝĺҒӨHxӘГНӧ`ѼȈјӧӑƥˀӈÁƴ',
                                        'default_value': ':ðԗ\u0383˹ϕЕ҄ԏyҾȢĕ\x82ΣѰľȅ«ΡįƧĳӰȒǢƑ˲Ԡҍ',
                                    },
                            {
                                        'key': '_ěʬчʆǇҰˬλʉƉϬ˾ȳñƦƠζЏкɣśлжüȸȳɼҰϼ',
                                        'description': 'ŔBɽвӘԋƭʮƄōɝ˼ĘЉƻæҦ\x8e¤Ԃѩ,ÿȵүЬȪҽ¤ѭ',
                                        'default_value': 'ΐѐӎǹĄРрϢƻԪ~ӎň˄ӃǶȘŕҤǔұπ\x9cʴǣĽʥқȁÜ',
                                    },
                            {
                                        'key': '\x8fͰŘƩ\u0380ȿПԀӥ:',
                                        'description': 'ƶéҶÈʒԖȤˌϹˊΚ\x96ҰʎҾʄѥ\x94ѱŪƪƊȬŮƼ˦Ϝҽԫw',
                                        'default_value': 'ϑ¿\u038bҌѴΎГύѾŰ`ϟǷƬϳUԀ\x8aГʌùӄΚƓѴ˅ϷɀȄЏ',
                                    },
                            {
                                        'key': 'ҥàʭǄŐϯɆП\x93Є˚ŀȃɎƈ\x96SĸŌԞȚЈɫļÝƖӽěҎɰ',
                                        'description': 'ˏĺo˥^ϸХƲʭ',
                                        'default_value': '҉\x9cЃfĈĖƆõѠȿ0ŀ`ǗͱГҔŦȬċBϿӞſ´ǶϰɭѸƓ',
                                    },
                            {
                                        'key': 'њďҲÙû\xa0ѷƱǏÀ˄ӕÒȐńԟĿ\u0379\x9clȋƅӲƺʉҽʘǚÑэ',
                                        'description': 'аυÄȲǷŕɩʪԫίҕķŅMôƚ\xadƒţPӯӂӔΚИӑāѾϏa',
                                        'default_value': 'ÂïɯɆά˝ɉÙǝ\x98¥ѱ¶˝üϹ˺Ϫҕ\x94фώͻσʁǯɘңΦƦ',
                                    },
                            {
                                        'key': 'ēK_ˮ\x9dǆgȪ\x99ʚσʶčƏҎ˧¾UǘтяΕ%˖үӜĸn;Х',
                                        'description': '˞»Ѡō\xa0ʃcҪȘ\x88\x9d\x9cJκύЯˈҔΗĂŮԐѓšͺԃԛΕǄȱ',
                                        'default_value': 'cҚϴǬ\u0379ұρκǧãѹɀĕÃХӁ¶æéЇφʒǹɤϣ\x8aϘɪtΨ',
                                    },
                            {
                                        'key': 'ӏřyΏſӲŭÊьŚȱиĜÌƀԅѩǏԖӹ˪ҜʝƢҿ±ʯЪːǬ',
                                        'description': 'ǗрлЎĦǆʘǃΆĽ\x80ȱҳȏӦΑMː\x86ҔԙnǺɼωɚĲĜƓΠ',
                                        'default_value': 'ýƐɬӪɷƅ˷Ȁ˟˕ŉîΐȹŬ¤\xadPĺɪɷʫşΝʸ^ѯȟӠԠ',
                                    },
                            {
                                        'key': 'źǟԔƲƑх˖ȐȓϾӮ˅ȦԦŃƭɎӣϸƤƘ|ҼθԖҕЙ˂žХ',
                                        'description': 'ϿȇѼÖ[ưȸǵӳΜ\x82VԖӶҒZҡ²DµŜǀȗŪɭ˦hˣˈГ',
                                        'default_value': 'ўйĳƑʌѳƈϷςɒϯЖǜȥUˠǢԠӋvɩˡȣԚNПқĸӫӔ',
                                    },
                        ],
                },
                {
                    'name': 'Ҝ˧ʩĥʂĹ҂ʍͿҷԔ\x9aĒɒԧʜ´*ǾťϏáÕѰЈԇϡҪҚŀ',
                    'description': 'Ӓˈ¤ȽЯîԩγЙŹɈÒώЪȄűÕΏǚȗȒΜ˃ӭΎɬŐӡ[ʟ',
                    'target_id': 'Ȋɐˁƨͷς½ѽːАŨҍİǳĪ,ҨƉ´ėȣȍ˵ВΊǵќ#ʒȽ',
                    'parameters': [
                            {
                                        'key': 'ƼLXŖԓѺ\x90¹ЂҍҡΜӊƄģЎЙӻδɃΠãƑÆĔʴȔÍHԫ',
                                        'description': 'ĒͷйæĩšʆӡPҌæԖҊЕКϣ˔ɳʄʔxþͺōȍҬħίļԆ',
                                        'default_value': 'Ѐ\x95ʼȫRǃҕƮӳӶŨĶӐ˔8ƢǋӛÄԓʗǠȘʒɅϵɽҚʲΔ',
                                    },
                            {
                                        'key': '%ʣǆÿәΦ΅ѨҪЮŲɝҽʿԮҀўЙϩǊûўYÞӇаÈĿ˂Ɖ',
                                        'description': 'Ӧѻ#ԌζқÖџüɿӂωŨъʷ©ϴѵ϶ȨѐêǦι&ΤŪѡŀ\x84',
                                        'default_value': '4ϔΥ\x94ȖӱӝҸȲΥθΪ\x9eҁϊĦȊȆ«ǅҬƎϠʶÏɵѧǳʑƲ',
                                    },
                            {
                                        'key': 'ÝҶʀӃƟș\x9aϰ҃ɹҐɴƠӓԠȠ˥xİҁĤȱ\x9aɧéͽʠâș˚',
                                        'description': 'ˏ˫˜εN϶\x9dʏ<j˩Ƽsɓ%Ɣ¬МωӕϤӭ˼ѪĠɶƓpƨɝ',
                                        'default_value': '¸ӟјԡűѩÝϦƋp¬ӪԧÞʺΧβˣ˞ϽĚ:ǋϫϿЃɸϫ\u0382ù',
                                    },
                            {
                                        'key': 'ÒǭqɼŻ¦ǫƳкϦԅѨςˢԬԔʻӁɎĕщǲėǏӵТҝМEа',
                                        'description': 'Ѫ={ǩ\xa0˜ϞӈԤТȨξɮ=ʳΑɧЈǆμűћ\x9fӰіɀ˘щÐŻ',
                                        'default_value': 'ɁȷóǁкцðɄɚ˸ϩ\x86ȓϑӼ\x85Ͱř¥ĬƓļнԚԣʑӆǘǑã',
                                    },
                            {
                                        'key': 'Ґȴ:ĳőѲҍћзɌ¿ΛƃĉǻʳʳѢҔşϯăȭʲ˩Ȁƽˢ҆ʁ',
                                        'description': 'ɠʔӛŰϓț6JԜ҆ʟŠӍĹԬЀėfȐžԔ]\x84ϑϋǨҒӠ˭ʞ',
                                        'default_value': 'aӉČʮϣƧǹҟŎҵҎЅŔʈԀɀÙҏːңϕǪė(8\x98Ȥ¶şą',
                                    },
                            {
                                        'key': '¸әDΐÚcȻѺˊǔĴK',
                                        'description': 'ȰМ\x9aŹϜöΆҦТ\u0381ɒБēԆǔϩìĲТв˾ŪƋƴȏG˴Ԅˊƴ',
                                        'default_value': 'RƢǬ˩ЫԡԖϠϞԕæԇТΡЫǵԈ˔ơҙÇĐɄϻϖГJҗɥ_',
                                    },
                            {
                                        'key': 'ƅϥюԊшͷԚʝcєЖŭԂȣͶʢо',
                                        'description': 'Ѭф\x8bЫϟÒϘĎӁǙиГùȊÅÞǍÜʫ5F,t;ɰͰƐԟǕȰ',
                                        'default_value': 'wČţԇȰлíυˤƦО\x90ʰèėƷ9ΐȒȶЄρXƆ;ʦΥˣĹѧ',
                                    },
                            {
                                        'key': 'ï.ҽʲǝćǿĺ',
                                        'description': 'ǼυȽƶʟŐʲ҇ȯІТҀ]\x88ʄʬʰˠŨƩŮѢҹȩгɒČșAǵ',
                                        'default_value': 'ˎěͽϫя³ȭ°ʃʽОȐǴίɩƃXåBʎ7ъƋϭΒЫ҄YКė',
                                    },
                            {
                                        'key': '¥ýȗ8\x86҈ԡìΨăƌˌɒʿŎ~ǘǙɨȰӚƠҒ˸ϢеĥƮ˺\x8a',
                                        'description': 'ԥԏҢʷÏȶЮˍїɗ˚еĥǄҝ\u038bɧͶćΠǇσќǪϳԮԓƱҪӾ',
                                        'default_value': 'ԁɬşҳŁ\x8bΏYǽԄTþѢ˓ġĵқˮҾЦȧǲӟͻΉ×QҜƣd',
                                    },
                            {
                                        'key': 'ơ˰\x9aːƧҚĠĔcǎ˜ɠѾƯʼɗѦɆļԨʱ«шúΞ%тϞͼĺ',
                                        'description': 'εЫƗɲ˨ǴԤхƀҚǂЉҧӚÎŠɤφɡÂ\x9fѠ\u038dhҒȈӯmΘƝ',
                                        'default_value': '˘ƴCƧƟͷξўÞПôǞҏҩŤƵ\x98Ӷźʁû\u0381ǋž°˒ƛЖɍЈ',
                                    },
                        ],
                },
                {
                    'name': 'ε͵ȬΩϩ˦ÉβұǳйÔ\x90',
                    'description': 'ǉɕ~˶ǚƋΦɑ˶řԦȉŖǰ\x8d³ИU\x88πǧƝШԌĶñúƲn7',
                    'target_id': '\x86ѝþ\x9a×ǧб-ǰԚ0ӑ˦țӔҷЩGɋԐiǟѻƔʕǮȨˡǉӍ',
                    'parameters': [
                            {
                                        'key': 'Ϳlð\x9cыӬӻ',
                                        'description': 'ԊÎτ˾ǣĵ\x89Ѣ˕ɲʊc\u0381ӑȧǨŨϛΩсѣɿХ=ǕēåӅοˣ',
                                        'default_value': 'ŷӛԈҦǜ\xa0҃ľɋЈ\x98ѥğҫɼМƟћθϖȓbƆҜɍʻɘύҨʴ',
                                    },
                            {
                                        'key': 'ТԭʁȣԏķіéшŲöȇђЃƏɾ¾néɩѲƉҢʺȦΕЈϯɩÐ',
                                        'description': 'ЂkϋǼ\u0378ŬăƿП˔íӼǍˌµΖıŌԋӤǍď˰Ҧu\x91үҒQљ',
                                        'default_value': 'КˋɾȒϨұʪĳԅ¾ӃÓƥɑƯЂӿʮӂƣԣ$ǈʷĿOѯΧԩŉ',
                                    },
                            {
                                        'key': 'ԄҥōԨÚˋŰÒřҳYôƝȞʪȱɁ(Ĩά\u0380ΰˠжʷĶΆԂʰŞ',
                                        'description': 'жҤ҅ǉ¡ ίНϒθϗлͼŶҌʝĵѽԗƽϜƈҒҿҜˬɩ҈Ń˓',
                                        'default_value': 'ЅҶΎΤԋЙҁǁԄјğĲϦǩ\u0381\x93˱ˠǜ\x85ԑԑɴЍȭʳRѢͽҴ',
                                    },
                            {
                                        'key': 'εĿѱƉԪĆȡ\xadǷƾǁ˖űu\x8aԥêȵäӏ˞ʃ˵ķ\x9bҥңˇӝΑ',
                                        'description': 'ƨ<ø7ŀӕхłҭïǹ˪AƍïЂsĐ˽ЇˢǶʄӂъж?ůȇ˶',
                                        'default_value': 'ƄсȰŰʦӕΤˤї\x88ŲѰŴξȏОæ7ćϼ\x88ԙčǃ\x88«њхҊШ',
                                    },
                            {
                                        'key': 'þԡ˦ОǦɉͲţŻϲ¥ŊҐӍɇ§àκȲĚѲïŇеҫɂ{Āƒϱ',
                                        'description': 'ŵ;ӞųϜżȂаΙn2ƈЭƳǜӞȸÁԘЖѕӱҞLʮӨϮÀӀǴ',
                                        'default_value': 'è\x85ɘ×ÎɒϹһ]_Ș˃ɯѷаɋʉԞäҰѕȲȇǧ©ʲůɯŃӱ',
                                    },
                            {
                                        'key': 'ʴǚҢŸшʪĬіȄțɺƹ\xa0ϬǞρѬȕ¾϶ʡĸѰ·ȕʳ\x7fƪμӃ',
                                        'description': 'ϾʗȘЅƭΌђˤk%ͺòҭʊд0П ӖßЄŔоʬɘ³ňśҘЈ',
                                        'default_value': 'ϡгϛҾϕѮʒ3ŮˏљǳǍ\x8d˂ëϩζ¦ԚӉ˸ȗҜɊҾҖԝɅɘ',
                                    },
                            {
                                        'key': '҄ѯώԥθӣȼ\x8bуϴƫWӲɂń˱\u0379ӅɭťϨ³ԝʪӘГз4ƾ\u0380',
                                        'description': 'üгʬɘЉЦˋȏŨCʿѕƖ¡ҫӗȅŵÚÚʟ҆¼Ʊ@ǤķΨ\x85ù',
                                        'default_value': '˘˯ĠǭѰǁˌЦιѶĀӶģÎʟήԟӨɹКũƻѱŹСȨгѶȉ9',
                                    },
                            {
                                        'key': 'ĦԨ8\x8cҕ\u0380\x87Ř@ӝŎƗ\x8cԔ&ɬʶӊˀΖεȹƌҙԕӑІ˹ǪԔ',
                                        'description': 'ƪS\x8fȍΘŌƅļŨȨβƧíҚϧǧsЋ˜Úʋ\u038bɝѕȧМҍʑ.ћ',
                                        'default_value': 'əƃɃȫ½пӓϭūĘӹīЁ}ɣ˷ƚɆȡӮËӂğͰͱeѲѪϱҕ',
                                    },
                            {
                                        'key': 'ýΚȕ\x82҇¾ȱŰΒΫǠǙÌ.ǴҰɩ\x95ӸӐ¿PɐǥΝÖôm',
                                        'description': 'ƮԈǦʡϤΰ~ΏƉ´řЌßϿŔʹїZƥӤϏƗôѢκƭкεΜŐ',
                                        'default_value': 'йJɍmӿϋƑлɑˤόɓɋǹ҈ʅ\x9f˵ʕȂŭ=Ţɺйыn\x89Щƍ',
                                    },
                            {
                                        'key': 'Nφȇ2Ԗԟ$Р',
                                        'description': 'ÍɆĠȔӅī¬ˉӷͺҮ\x95ɚƛķѺɘĂϜΉɩ\x9bƯδ\x83џɭóʭɧ',
                                        'default_value': 'ÔČӿȶÜ˗ȨīяЫ,\u0382ЕȲ',
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
