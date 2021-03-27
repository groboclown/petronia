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
                'өԅԭϏ\x96əʔȸ\x82ǦόβҧĺԃѸԔɀ',
                'NÏŽÜɘӸ˪ҝϯľлͿcʋōԂȩŚȈԡ±ΐɟ',
                'ȶǔһȿҚɉη6ʫǍ%Ǯ˝ęx\u0380˵JÅėɡ҄ɶѯƽǌ',
                'ɵμƼŞǺ˴Ԡĩ\u0380ǫŝҌВĹĢāΜ',
                'ό¡\x7fӡ\x88ţ\x99\x90һ',
                'ҖәΖŘŔЈʩŸҮТϒ\u0383³ҽɼΧ\u038dѶ~ͻťɮ',
            ],
            'comment': 'ēҢǉέ˽ýæԚJɃűί{ʦŒňЊʷɛāˀʦȰѠϢƻáϒŷӁ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                '\x93',
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
            'key': 'ғТʫҳԈĎβù[ʤВ»ǫ\u0382ɘʯÝ~Ǧξӄτȑџėä#æɔ7',
            'value': 'ʂ˴\x96ģƄδ=ЉȢjгŪϱΟ=ф ƺҧБәΚ&öfȋȆȁ\u038dϠ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'a',

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
            'target_id': 'ͺR®ÃǭʐԘɗ¦ʆƪǦˤī<ǣӎ҂ɟĄӠΤԥâќѿÃāΧӚ',
            'parameters': [
                {
                    'key': 'ĐįыGȩ)ɟǋ|ǡK˓ˣoƜɨɼɇĨүɤǬЂӡ=ɕѠŀ\x91Ƒ',
                    'value': '\x9eŢHÝǤѰɊŢкɰʩõΦˠyѰјĢùͷȮʘcлӱȀģɑůˊ',
                },
                {
                    'key': 'Ωĸύ\x86ѭӟ÷dƼӋǋΛǶǈԂѸȠƻˊħĵ{ȣʈ\x8bʅϚ\x96˃Ѱ',
                    'value': 'ńϚƇЧҫӞSԃӽˤËʠ%OҿʚɔȌûʖǖÛїΊ)ʪǨɳˈƌ',
                },
                {
                    'key': 'ђĚƮhɦȵіҏѥʹҬѷȞ&ʥэ¯ǲĚϔҕƢԈĨΨĉãӋɋ\x9c',
                    'value': 'Ƶԭmӫϳ}ÍÕӹ\x81ʏРѲ˳κeǐӎΡɲκьЉòÆе³Ϗʆщ',
                },
                {
                    'key': 'ґßʡѽкȏӂнƬƷɶҨŖχȚ7ÃӶƞ',
                    'value': 'ВŔ2ȑӪȁЁ¸Ь\x81ĆѤÂȄȎ·ȖҽÜӧŠœaӾǬkĦŰʳМ',
                },
                {
                    'key': 'ϽƃϒϤǶӻŞҹʗȡǫƅѳӫɠɭιʁʩЁхќŇ\x97ѫϜԘϚҋ',
                    'value': 'ʃγȄǬѭǮοöˬÐȣЄɾʌў˄ιʜ!ɄҫŏȐŚԆСʣ˹ƊҘ',
                },
                {
                    'key': '΅ԝ=ѽӰλԑϼȢʢεĥλˠ\u0381˦ηӥŕ˭ǺǓсΣхӄʕʆTƖ',
                    'value': '½óόjèтӡЏʼʱ\x91Ҙͻґĕ½ǜÕͳĝʣʱıОqļŜжĳ±',
                },
                {
                    'key': 'ǅǌLҸɗŗ˥҂ӿϒϑқĚ\x8fãʚ.ΘɈӎ',
                    'value': 'ѕȆ³ҮӤ=¯Ѩ¾ˆϸ\x8eњіɳżƤСУǊҐϖĬԂƀςы˪ҹω',
                },
                {
                    'key': 'Ҧл͵bˡñßΎŕŭʩŭыԡǝƩƅǤжʻεƯԞǼҰňӜ©ʱƚ',
                    'value': 'ӻˇӠ_ΟЍƚĸΧ˩ҏȑņǤѼ˧Ə]Ħ}Йʞ4γѥƦ˔¢®έ',
                },
                {
                    'key': 'čҵƃʖԣIӹ˛әČūљЏŻώŖº\u038bΜΡӾ\x9bгӏLжѐʱʪы',
                    'value': 'КϕӘǅԑϮƱ_˪ӛԆВĳӹдҼϒư˹ώȢяȚ¡ɄΡöҦŚρ',
                },
                {
                    'key': 'ņ]ȉʥǂȳęӀǫǃȧʰ¬R',
                    'value': 'ÏӬԗȹѺʤȒϛ˘ȧӊћӐǆýԈÖCΦǈфѳԃаͽɖĝΫͱ¡',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ѹØɻχˀ',

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
                'ʽφ҃Ƭ˞ƬѢˤȪ=љЕŉÕƵζĄͷĸɚҢÞƦɦӷӥˋԫ',
                '«ŘÞԩ°ʽĄɺǾ_x½ΕԧЦȂǦѯ\x88ѕųыԩͺǕȌəƪҙ',
                '\x9aҨѮȌɧùƫƸΕҿ΅Ρђ¹ρӗǢŮ˼ĝʱIЁÚ^ϋ',
                'ҔŏȂʦҋĳǩɭƾѦщԣуäǾϭТȚ?ɧǡȟÝОɌ',
                'ŬƐɲ˙äλƟÉN˳ǘӑΟƯϻҜĒи&®ĸϛҙȩŝ´ʒC',
                '*ȡъӃйҘˁбφ,ӨOԛҗεȂˍѻґҡŦҚɑũυȏɨbΦЦ',
                'ҲɑĊF',
                'аƵҿɰϭЯ˭ɎȄбľѫrϳг\x7fɓȯԖЧÍL$Ԫśʘ',
                'FҐą`ʍΒ\x8eQҒƓʿs',
                'ƑϱӜTЋ\x9aΤĩϳǻǢӰ\x9aŦɆǀԧ¾ώ^Ѐʸ¨оӅʷϤʜ',
            ],
            'comment': 'ɞ˫Ј˕ΗǶƢϺÓŨʖĨ^ӴȢǭҌӑːǫȮҾ\u038dқϝbʴӂȎǁ',
            'event': {
                'target_id': '˟ƻɂ\x8eÝșӅȫǅ҇Ɂӷ҃ȥɧʹɠđΟρ˚ɏɥτЍȀƳġɨř',
                'parameters': [
                    {
                            'key': 'п',
                            'value': 'ΗџΫʘɫѻŰӮʂó«ǪT]\x95ӂƕŚҿĒŢʳʧȇӝȰˤԦρΪ',
                        },
                    {
                            'key': 'ѐіǷJɒγҟ0ǙȓΧMϿƈ|ɺɔgǧ˫ыưɃġ\x8dΑҍВҦƆ',
                            'value': 'RҒνǖƏŘђǤХÉϽɀπ¯ýʿ҄ɥˮΙԠlљʺĖë8;М\x8f',
                        },
                    {
                            'key': 'ƻõkʉʠÂ"ĲН҉\x94ϮʰÒ¹Ԡ˸µüϮӯ\x86ÖǸʅÐȈȜʜȹ',
                            'value': 'ђǏɄƧȬɀɼ˲ʝʍϠˠĮæǃ+˛țŋѲK˹ÊϢҚџΣȈǫ^',
                        },
                    {
                            'key': 'ŻɅҋp\u0381ɈtţþľϺ҆҄ϭɉfУЖμϗɋǊѼ°˅ýƵjφҳ',
                            'value': 'ϟδˎ҇҂ɩѷʝМ΅ƃʼȢѬbΌǊĮ^ΦԈǡԇЗ®ѧӟɝƲϏ',
                        },
                    {
                            'key': 'έŪȾѿˬKϲΝŅӢЕόʀjΛƯОɨҴƜԎ·ˀŹéŨ~ÕԩΜ',
                            'value': 'ǞčҀǩòɑ ɒӗԘ{=ȷƟB\x97͵ÉΫȳ˧ϔ˪҅ӣϾԭĖ$ɇ',
                        },
                    {
                            'key': 'ηҡ\u03a2ʒҢą,ϜȯїØѲɟѽ>ҧŔġЅЙӝкϻȞӕӖķЯ\u038dĀ',
                            'value': '°.ɷƻӯżƌ˴ƎԇΏҰԩƅΰҷ͵ħ˦äτΓҙΤÔӷɟÔӆЗ',
                        },
                    {
                            'key': 'ϗŝĔϿȖԄӍÔǽŅǀҨcӽ#˶ԧǧÜŸЍˌmɿБѱԩū˜ѓ',
                            'value': '˖\x8cýɶΠ¸ӿŏƱ\\ͱ\u0383ȿĵȗϭш˞Ԑү˰ˀ/ΑɉũȄXi\x80',
                        },
                    {
                            'key': "ѬŹʌı'Ì¯ȇć\x85ZϚΓѲǚұǡɘӴƂԧ҇ѭyŞœПКɋ\x95",
                            'value': 'ϯӘƍԏ΄цΈ_˟ªͷΘϝ\x8cŤѯ+\x8dњϩvуYŇĬɈСʀ\x8eЧ',
                        },
                    {
                            'key': 'PŭаƁτЂośǋǁԠ҈ԭÿΰϭƉǉʰӣ=ͻęÀÛҒͺԞaύ',
                            'value': 'ț\x87\x81ЕьеͿʍзǆ\x85ʻӻʾ7˻ʸȤɤӛȇďˤïțӆ2ɫԀћ',
                        },
                    {
                            'key': 'Ώ-ήТǎЧѣºǏïЭuѠ\x99§ȋ',
                            'value': 'ʃ˧ϩǻš˵ǣԀǋ<сҭFПČˍΏrɉÈґԬƧԊǶďͰ\u03a2ˋ\xad',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Μ',
            ],

            'event': {
                'target_id': 'ӆI\x8dƱҪ',
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
                'ͱƭÝͿÖć˦',
                'Ў\x9eŉӦbŞҀС҉',
                'ϫǝĦɹƎЗϊ˗ӣδ0œO˳ҍ҈º',
                'ͶȫĄ4Ȍ=ЏԛǬҀқșɟǌйłϢљʃΕ˴ԊεΈӪ',
                'ңЎ˝ȂțђԕūUӜӄƽƻԗ҃ǹγ',
                'ʩȁӁыˑ\x89ԖҎǧɭӑό\u0379҆Ƃė\x9cϳӏǐ¼ɍҗYҾrњɎцѝ',
                '˾ɒɔ¨šɨͱ¦ĢɆʊɦ+ʌi/ȴhϣ',
                'ȩΉϤ>',
                'ѐύ',
                '4ӟċM¡ɿ΅ҝŃ\x84ψKĬǶ®ϡȣҽrǦёɶЗȜԄ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ȹ',
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
            'key': "ӴκɝǵʂşџöãӶƷǰƊʔǌǓ'ł",
            'description': "ҺǇʲҭÂψ'ҎӒʕȍȮͺɮ\x92ʨȶɩбǄöЭӲƼµUˢ҂.ë",
            'default_value': 'ҹѠ΄ʈȤ\x90\x99Į˥ßʇā\xadнϒÀ¸z\u0378¿ˊȝԔƣŋҝŖǷϞɤ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': '.',

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
            'name': 'ĺŏΈšȻ',
            'description': 'ϡųðŚļǳЇΥͿí˪śŤ`бҘҨͽɁƷó:ӡʑ\x8bǇĚӜԁȨ',
            'target_id': 'ǐоþЎȴąѹϻĀƔaӅиġӻѭŀǵϯԄŬӞЃΒҟҷϩʦˡʧ',
            'parameters': [
                {
                    'key': 'φǯхǛѭзȫԡʲˇþ',
                    'description': 'ǪύʊƜʝǪӉиʔʖʶÑʊϪѮǾˑϑΫǥԊɎǋēӋѸÁSɸ¢',
                    'default_value': '҈ԐЂҸʦэMʸɎ"ˌҪӎАӪϷЯʿɏíȉǘżƎԩMɫάϰщ',
                },
                {
                    'key': 'ӯǿÓyɤĒn\x9cț˗ӾʩҭƱȄŰӈȍϾҟȘˈѐԟϖ ǞTҌĉ',
                    'description': 'ĔŭʦȫŴÉϠÐƛɻϠ\x9dˁ×ůʺԍјýʞЯΰҾӶʾFÍә˓l',
                    'default_value': '¸ĝҘ˂\x89ʔù\xa0ĘҢâ˺ΈzĶίɹ\xadȀΜәɳ˓ѯȔ\x97˷˞Æȇ',
                },
                {
                    'key': 'ԂэС˒ƦҷϸĕӽчɵмɝΎщѨɦŶ˥ɗǴЗŠŸ^Ϩʗкͱ\x84',
                    'description': 'ȫ\x9eЗċKҏѺʞǽϛɻǿԒȿĊΩȨŹѫԖЪϞцŷӎƥÙфëХ',
                    'default_value': 'ńѽГķʯэӷɷϵԦÒԓѡŇ\x94ʵʍӟЧƔ˨ȓȩưǉӎҏӴԓ\x9c',
                },
                {
                    'key': 'λнĕʹĈçҀðӳƄ«Ƀы΄]҂ӛØҹԧӦ˓ѽʨȣƟʉԜǣǆ',
                    'description': 'ҞŲɾǾɑɌ˔ďѢˮƛζǧӏӠȦθԡĉˆŲϨ˽ɾžĉџė\x89н',
                    'default_value': 'В+˩ÃÏŶ½ђ΅˗ʲԠĶ¢ȜϻЎϔСʑ+ĮUϪΖˤәеɛȪ',
                },
                {
                    'key': 'Ņǰ˛ȳûȎūУˤQ˰ȉΎБԐĻöӍϗȫȳȶėҌԤϰȲєȈƀ',
                    'description': ':ɟӐƅȈƕīơґ\x82ҀŦÿӺˀτ¸\x96ȼΊ!ʳɓѰ³ƾʓƈ®ɨ',
                    'default_value': 'όʽ\u0379ʈʹcȱDŀȈɉǾΪɚͽɩԦΏċʿӅ\x940ǿEԪё}\u0379Ǒ',
                },
                {
                    'key': '˔ĳʤǊѢԥǡȅĩԁǰԄƏɳƎНǅnȒҎˏ˙ĴƠ\u0378Ȓ´Ǹ\u0379Ʊ',
                    'description': '˱ɿӀŶĉȎˌюҗ˃ҦдВхģ)ЯƷŸɷŢ?ãĵΐĕ˭ʍϔH',
                    'default_value': 'Ďҏ>ʮқΚΚΦIʌĮˏчȳˈǃÿĺĺ\x90ѯġ¦˂ˆӥ\x91ˇҌċ',
                },
                {
                    'key': 'ɋ\x8cɮńˢƞѷɃΧ\x90˙ˠҚԢǊɦѣƢ5Ȼȋϛʒϗ͵ƳǖĪʘԗ',
                    'description': 'ɾϬҫHΣ҇ŞЖѬҲΡQˎŪʸʔjÅûьÞɼʎıД©[ǌě˱',
                    'default_value': 'ɽɹćӋŹȶԬƲȉӷȬʯӻϺͳԙ\x83ŖҞÌ˱ϯϚ¸ĵԭŐ)ˍϱ',
                },
                {
                    'key': '˥π',
                    'description': 'ćȴCʗΞӮŃгſŭþԌĳӣΞԦ˗Ϭ˓šίǈғĽѥǡÓȲɗӌ',
                    'default_value': 'ѽŀΌ$ʐƱԆǆ\x81Ʀ҃üʱ\x99ϏұӭłàM\x8aȃ˹¡Ěû)ǞӃƐ',
                },
                {
                    'key': 'ΨӇɓʪ·ǦԠɉɬάɱʟԐŤƩħÇƮҚӳ\u0383ʟɜϳΕϨĖʵƏǔ',
                    'description': 'ˁƣųĤǅģϷGCɚЛӏȃΘ\x9aӟΊʗȅɸ˲Фȝ˯ȪөȭԈȡ;',
                    'default_value': 'ӁǂŎƬҳϊÑæūӮȓǻϖɽáѺưЍȜŜǩÜͷҲϛÑГãˇá',
                },
                {
                    'key': 'Ь˄ҢѮΓǈǳɓ˹ƩΈѱǗяLρҫSÙɸӎа˞ǲ҈щ\u038dԆǡ',
                    'description': 'ԝѻ˞ˑәĭȌˀʾ¹ԧҐːȀɒǏƠɑɬń˵ȡǚϝĵȂлΏʧ4',
                    'default_value': 'ЕĭѱϥǓЛŚʠʜϤʫǕϝɓƝŃʌƲPħҸϝтĦʾ4ŽǰxӞ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ѓȾÂ',

            'target_id': 'ѢԕſħГ',

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
                'target_id': 'ĄҹļżāҿϩӒfδЈԙԪ±½\x92ŃɍʁƦ҈ȵ\xadŃΤάřΑяţ',
                'parameters': [
                    {
                            'key': 'ĿӬ\x87ԪςʂŚ\x84аΏšǄȲˏɷɧ',
                            'value': "ûԕ\u0378ӡǩї˕хÏɶ˩ӛЭɱüʻҰʘʯѢŗǎ\x86:\x82ɿ'Ρйé",
                        },
                    {
                            'key': 'ħΰǻԁɽNӔŎǚ˴',
                            'value': 'ϰ»ϸŶĜ\x8aѾԆŃЛ˰ԀҘѡƹ˶жԉЧ9ЅŲȡƖ҅ċȪјЎō',
                        },
                    {
                            'key': 'Ǜ$ҀКОńɔˤғ]Ÿв0ҵĩ˸ΗдʱϏɭѾƅ}ӾɿʚӨɡǷ',
                            'value': '˦ҡłҽϝȮˈʲôÉĪÍʃɇřČÓìšşҲѪЃˌ˵˽оˇ¾ʖ',
                        },
                    {
                            'key': 'ʔɛЃϢȇˣƖȁХ^љͱ\x82ϯЏɐǏɫ˴˞ѨҿiΠȓcԑȍюҚ',
                            'value': 'ƑšĴӚΜЈҼϚ¥ªÐӡǨӢǵϟʾĊӟȽУȊӥuɖЈȐ˽%ņ',
                        },
                    {
                            'key': 'фϽƚӶŷ[ʞ˷ȩӸ˜ɷ\u03a2ŒĄ˒ΝɵкϐԜťîʼΆǲöԙʵ»',
                            'value': 'eȯƒ΄\x96ËӄѼ^ȚͼʧȯǢɺȬģԢԜЉˉȏÌʛɬҀ\x86ǫлȋ',
                        },
                    {
                            'key': 'ǚӅϰøӜ&ДӝɽżϻНʾϫƨ7ɪWØ×ɥЛӶԔɄ¬ʽʶTͰ',
                            'value': 'ƖȫМʹȤ\u0378ȎαŊͰЎѻȰƹɰБȬɘԏϧӆϲĜʭӣœǿƫҙф',
                        },
                    {
                            'key': 'ԋˉʲѹ§ӵ¦ȜӭӥƣŠҔРü#ϻGΒϗͷӊѴÃǼůԕĎΤŁ',
                            'value': 'ȚЪƖҨȭԊʢɱǘɶʲԈͶЋĊӹˌ\x9dÅʪʱǐѾΐƴҟˉŸʢĪ',
                        },
                    {
                            'key': 'ÜɩΝͳưқāǋ¸ˋѦΪĿѻӓѡхϘÃϑ6Ͻөǟ=ĸΡµ',
                            'value': 'Ԗ`ȡƉǣԤĲЂÓȒО˯ƄρӲԕΓÊƻÊ×,ûѾԡϫѝʉÆ҅',
                        },
                    {
                            'key': 'ԎZɝΚΒ¢\x80ҟ\x97óӱŦʝѭ Ǯ+ӃϻǱǊƵ®ȿӌƨĎ£ϢǗ',
                            'value': 'ƉĈΡ@ďǀӦӶӦɐș\x82ȷѬ\xadzΧʤŜʀϵʄ¬µƼςҎƛѣͻ',
                        },
                    {
                            'key': 'Ά´ðĐѸ˕ήΜƋŪŗʠʷɦŵхÍ·ɶӤǴƩю&Ԁ¢ѿxĢė',
                            'value': 'ȏɋď\x8fÜ+ë\x8bľħҍœŁĮ¼ʹŉǹŊʩ\x8a\\ǄʰT\x8fԛƚҵҢ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'ǳáȾӗӮ',
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
                'ћõϙӾǡƠãÖ˶ŅșӨ',
                'ͼŗԨ',
                'ŨƢӦʫԖƬӓ˲ʘɘgРҀ',
                'ΓροҶɠҍÈӝüʯ҇Ϩϵʸїƚʮʌ«πГʩƔЦ',
                'ʐ˥Ҫ\u038dԥҨвҗɘφτԔƶԬɑѲ]ǹrƑ',
                'ӏʜɩƦѥҠԒ<΄ÓďϻLѨăԬώȄbxёȖɗ',
                '\x87\x9c',
                'ŐƹĳĴ',
                'ΗϟЋ˖џtș0úҁĀƚƤĚҿıɗȈʡи',
                'ĿȵaȒͺЀȲ6ѨľҋХ˲ξѦŭ\x88Ѻŉάϔi˯',
            ],
            'event': {
                'target_id': 'ǥ¹ҪĉʇИҎӇ~ʐȆƁhƖƐʍӃĒˋΗÚ\x9fƲŀҵζ\x94ëӵʒ',
                'parameters': [
                    {
                            'key': 'ʃǑԐԥȶ˒ϭͳ\\ЄϗӘɕˌԥ˚aӢǌĺɭϻȬW¤ӈ2ȯÄȄ',
                            'value': 'ΆϾƖQυғέέʛҭӼøŕßѤԧчǂӣɔӏ´τǾΓƓҨƱΘΣ',
                        },
                    {
                            'key': '˒\x87Ķ¨ŒͶÜ£Ê.ԓºяӵŅłϦҽƻ\x92LύӪŦԎшιÎɞǬ',
                            'value': 'ʮИ_ȬΠԃũţɾ˟¬ҌҬҿȨðʁʺѲ"ӑľv\x99ԫϺњʫʣƢ',
                        },
                    {
                            'key': 'čАӵn˞MȄˑȇӼηȇĩɇ9ӟʽοĤҽ˚V{ʏj\x81ν˪ˊƟ',
                            'value': 'Ϭ˭ʍÚAMӝȇɶþ/ĜÎ\x8bɨĉЙΖ\x98Ѱ¡ӦȽɮĔ˻ȳǴ\x9cǓ',
                        },
                    {
                            'key': 'ҷϏɟŲÎҮȴ\x8cĩ\x91ɜΔƓɿɻǻƩ',
                            'value': 'ÇtҚΞ×НɔƇαȺƥƵǲǬƬīńϬKƎČĴzъ˽Ώԛûρʓ',
                        },
                    {
                            'key': 'ƔƎԔԡЌQ\x87ǆˎԈϙѤśЙ¢ɢҹҩк',
                            'value': '˛ǜƕřѫ8ƈЋÇάҏϒmѷĂΧ\x9bɠэǇҎφњćқ\x93ϙǜŇҡ',
                        },
                    {
                            'key': 'ƥ¨јҷ]ш˸ºʋćЀΚϓҵƥȗ˻ԝȕԮҬѽɞŬbqlў˸ß',
                            'value': 'ˀɈКйҋѢ΄Ͻǋ˚ҮʶΝӇĆôԀѨ}HҋĦɖƉ±ΔŬȌƤŸ',
                        },
                    {
                            'key': 'ӐÃ',
                            'value': 'ŐƩӟэb˦ҙȕүЂŎēԨԚȞ˰ӑƬʣ¢\x9eҴҍǐŒÿēσûë',
                        },
                    {
                            'key': "ĖƷ£\x9dȹYƺѓ\x8dЄɇҼŲˑƁǶdłɳʹΥÂǌʱΕβӺƳǎ'",
                            'value': 'ʉѣΫʓӳ\x95ѡĎƬѸ\x94тɢý8ьӘ\x8ezӟ˙\x9eɎʹñЧǌ˾Ѧѥ',
                        },
                    {
                            'key': 'ͷ\x9fŃδҾԟńϿûǷ˕lɍ',
                            'value': 'дBĠ\\ʹ!бҏɭɚɭ˖ô^ҢƜßvεĐȑĩґԮ{Ɔ\x81Ԅɧˢ',
                        },
                    {
                            'key': 'Ȕ',
                            'value': 'ɒÐʃƤȅÙ/ĪįáɟβÐEɺƣɂíȳ\u0383ƢЉ\x8eK,ӨǋŠÉċ',
                        },
                ],
            },
            'comment': 'ļoѷ®ĭʆŘʾӱҪТėĎœc³ʩуŅҌëϨȓԃϹѿϫΡ?Ӡ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ɐ',
            ],

            'event': {
                'target_id': 'ѮɝЊƛȿ',
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
            'sequence_type': 'sequence',
            'master_sequence': [
                'Β\\љǜʁü˥óÀήʙΚҸŐþп\x90Ϲѭι',
                'ѰΓӂӞìҾµѦ˃июȔ',
                'ïȃʬϐKÙҕZͼƮє)ʝЩÑυτƮҘȽзʠ҄×ˣĔя',
                'ʃԔԁɏϐǡá',
                '˰¦ƭт\x80˩ӢȘʺĄуȉЮ\x95¹ǜФˁ',
                'ѩ˥˳ǻ˂њңųДƇԟčMĻ',
            ],
            'bindings': [
                {
                    'keys': [
                            '\x89Т˧ƭϽаÙҗ×жԙ\x85ʝӶőÎ»\u0380',
                            'Ǩ\x9b',
                            'Ѹʃ˹ȠƳø',
                        ],
                    'event': {
                            'target_id': 'їįαӳ҂ċһĉƚх\u0382ϷǻӖdʂԏ˓·ђЉŰƿƻӶˏ+уΚБ',
                            'parameters': [
                                        {
                                                        'key': 'hÜΟЋΔ\x89ϵҡϠЗѦçϡϔȅĔʑ\x93Oʰ5',
                                                        'value': 'ҕȨŘԇЋªxɰɌ˳ÿǇѾЁʸѷѯ"ШӼIfȳҦΆĳʑȬĶ²',
                                                    },
                                        {
                                                        'key': '\u03a2ΨřǊҧ\x7fюZ[űƼӰyӭʆ\x8eǏнёˏԭŴҰ\x9bŦωſĵԈγ',
                                                        'value': 'ȡ˫ƩϳǇɞƹďҥлѿǡҳӷčӆǍϊҬǍeʘ\x98ЎR¯ŧʗш˞',
                                                    },
                                        {
                                                        'key': 'ƶԍҶөłʔӱϜĽȝöε¢ΤнћđñɴǃéӱċʞǨЍČ¹ƠΏ',
                                                        'value': 'ʯ\x8d«˒ɌȿȤɖӐεԝԋ·Ԝȃӟ\x92ӫ΅ЎñѯǳϴñҔԮΐŗЧ',
                                                    },
                                        {
                                                        'key': 'ԃQԦʃЀʴŇϨŹ5ȥӈ,ԏѠóɏ§ËƏėAÖԑɭZЦŋ˜ˋ',
                                                        'value': 'ТʷɖȬʑЕǂήǢǲǙӟȘӣǷɧ˼Ňȗҵș[ԒȄ·ɬʧźһŹ',
                                                    },
                                        {
                                                        'key': 'чЫь´ŇǯӿҍәͰϣĜĐԭԦ˦ŗhŰґКǄƕӇǲïȞĈ-Ψ',
                                                        'value': 'ǜǹƣ҆·ȁɷ˜ˠƯϝɽ˚ƘϫԠƱęʞ\x80Ӥԗgţţ#ǢÆԗ¶',
                                                    },
                                        {
                                                        'key': 'ԡǮĶŘİғȇƍ?ǥ͵ѾƲҴь',
                                                        'value': 'ΙʻßkRяȉўӈìӨΌÿƊ°ΠĭˮΕϥm.Ķ\x87ӄƈČѠЪa',
                                                    },
                                        {
                                                        'key': 'û7Ê҆%źʛӚԉҹǓξķǱÇ1ƑΡͽѱҤfȤ°Ϥ$ƚș˸Ē',
                                                        'value': 'ːĽҟŶƕ˯ŻԉΉÒҙМ˥HÖ˗Ӎ˕хӺrķiӡǬN$ɱԘɒ',
                                                    },
                                        {
                                                        'key': 'Ƀӗ϶ǔӂҾǓ˒ҍơ¢ȶΚ~/ā\x7fҊĐӫōrʁ\x86ЩԧȉΑƞɒ',
                                                        'value': 'ОƵź˶ʁҙǚιȬǛíŷЌҪϵąԇ\u03a2ˮƱξƋlŵӲĨнϖȾҡ',
                                                    },
                                        {
                                                        'key': 'Ӕ¯ƌ½ĚǺӦʯêˀǶU˥ǹғ\xa0ԜːƎǧϒ:аӤƙɱѥȖƃϓ',
                                                        'value': 'ϑķƴжμŜɘѯBÒŬѡÛ"Ѱòӡ\u03a2ǧ˔˞ȱ?eљӷNʅσʗ',
                                                    },
                                        {
                                                        'key': 'Ы¥ѴƲѝ΄ӻ˩ǚϭ϶ҸԔĀËǡҤ\x85ԙҍëԩӧfʃџɄʞлͺ',
                                                        'value': 'NaЖÌŋҜĚʶҥʨȯԫǗӘÀɇʀʼˉҹҷШ}ӫǽīǂą_˳',
                                                    },
                                    ],
                        },
                    'comment': 'ˮʆUwПуʁǯŸŽƣUǜmΦΦήʙƛɟȫΙЌjς˻\u0380Ƹ¶Ɵ',
                },
                {
                    'keys': [
                            'łŃӭϲϴ\x92Ӥõ',
                            'βǜѱÄѹȄҰǠЦԡʒΎ\x9cϗƇѴӧʢŦ¿ɭ',
                            "ƫҜηƆƞϭϓ¡ОɁ˟ЅĤÞEӉ'ɕϐѝӮ·ʹҍÃĔ'J",
                            'œĹʻ',
                            'ǜ\x98ԝǾ',
                            '҃',
                            'ǒƗѣ/Гˬ\x86ĚȻЇǘҕʸϵ!Ʀ',
                            'ƽɸњЩЋ\x86ʤҬ¤ŅДҼӕŃǋ',
                            'ˋ˘ËȟĖŐŏИлěÉȭʸǥϼɸҎâƩѧ_њɳƄȡ',
                            'õƙƬϸȘсǬ˹ÙȲÑЎӽ»ŘҪЃŢԅɋȍу\x8fΟǫΐ\x9c',
                        ],
                    'event': {
                            'target_id': 'ŰѻҙңʚςʤӤWňΦʊл\u038dƍϫʑԕƸԐɟήėΛԜđřЄɬћ',
                            'parameters': [
                                        {
                                                        'key': 'Зģ\u0380Ӗ&˫ŋɕ,Ǒ,ξÄϮʟКƝɨԣĳÑƯΠθųʩЎfϾɮ',
                                                        'value': 'ʺƊθԊuҋmҗˣŇǯǚΘħÃτ˻bԆʌȥΜԁǰȴ.©ɧ ɡ',
                                                    },
                                        {
                                                        'key': "ŮŪ\x9fäƤ\x9cԫǳŶŏƓUѪȰèз'ˡ`",
                                                        'value': 'ē˄ƚãȲҞȿǗ6wӈԭǸДȞæIӏӅĮЛʐʁӚ\x92ǯΏԠƆž',
                                                    },
                                        {
                                                        'key': '҅ͱεшαѸϘ\x92ɌśɍKϨԬĕȿȫ\u0380ҹйʹƖҾӽğ¥ȘКλ',
                                                        'value': 'ʫ\u03a2ʉȐҡ\x9cǫΟеŨӫϞѱ˙Ȑĥ\x86ҒϝĜjĀ§`ɗȽɛΦɼԊ',
                                                    },
                                        {
                                                        'key': 'ƣĪ35ȜxǪҰƳǭÚˌ\x83\x85gюԜ˵ɝ˾΅Üãu1æӍОϰF',
                                                        'value': 'ѹѺӤҊğ@ÝȘӫ\x9bȧϊĮǹƯĵАˇόƘȲģˑĤƑǘçΪƜ˵',
                                                    },
                                        {
                                                        'key': 'ҌŞӭŜƶƛwǐУΆԂYʀJЙɹӠǢÏ¾ȌҞƀУΥ˽ȃԔʵĀ',
                                                        'value': 'ƵӢgΚśƊƂƓũӚрąϵѨŁɯҖȯЂǉϝɂМɢsҧƢ˝ӊӁ',
                                                    },
                                        {
                                                        'key': '\x97',
                                                        'value': 'ȕƓēѷŃϻƳ±Ėөѱ[ǻѯȨϪ\u0381ȩнɻ=ϗȧȢťЦɩƋеf',
                                                    },
                                        {
                                                        'key': "ƃʣȚҞΊғ˰ʬȘƂҪíҰϗŋ˨ȊϽ\x88фӖů˭ѫЕ%Ņѫ'",
                                                        'value': 'ҮĄӬĝԃɆɄиϦƴӵԬɰѿżҜǆҠΖŰŘҢGұϯťǣʾͶΌ',
                                                    },
                                        {
                                                        'key': "˹ӾӢʢɯ˰ϞʒɆĄɻΎ#Ä]ŅͰǗÃĎĨӨϿSѡ'ɣ>άȋ",
                                                        'value': 'ѯ˲Ѧɏ˃ªΛИ÷ĆӴȭ˃ÔԅŌĲКϬψƢЙiЖȪМȵäǠȱ',
                                                    },
                                        {
                                                        'key': 'Βȝ˭e6ώӭӵȸҬˢϓ9',
                                                        'value': 'ЭɪħěҌʹ\x89ŚǗƽǰŇҢ,ĔԃȕƢФÒҋŽ\x87ȜԮ҄ÝīáВ',
                                                    },
                                        {
                                                        'key': 'ĶрŔ+ϊм˃ɻRäЯƶʶŕжœĸɹơɹǰƆɠ@ʦ\x93ΛńРù',
                                                        'value': 'Ɛàɲ:ȗĿԔАɴˁӐϥíƦҵЎǙ\u0379ʖ\x96ЦĞ˵ϙҜџȃǝʶ˯',
                                                    },
                                    ],
                        },
                    'comment': '3ЄЙQʷӤĢΊƭЖΎԨʙǞǻǁťĦ˥χȕːчɓǈаянԢԈ',
                },
                {
                    'keys': [
                            '˸ƞÞŲę',
                            'Ǝ΅Ў\x86ű)Ԓ\u038bЗƥˇ',
                            'ʺ҇ºţ\u038dИ\x99%ȇΉЪԤɦÄcӶŢϞ˱ʤūзšǔ',
                            '˒ğӴ+!fήԭѬοџџ',
                            'ķѐӫыФʿϬ¿\x85҉d',
                            'ϲʱϗȏWюʤюĔ˥ԪŴ\x98ͰνĥGjТɒ®ɧͺɤƳͽвǁʽ',
                            '˲r°qˌcǅÞǇϡҗΟĤ;Ąѫ˳˖ӝӃћȯȀ',
                            'γȁ}ɼǲɠΑς\x85ɭʆãȶͿ',
                            'ǤӇԙµǑÏːѥKȓӡʆϳűҡś',
                            'Ңăƿçτ¼ŎĠņƏƢϖɤΧíªԃ',
                        ],
                    'event': {
                            'target_id': '³ғĐӸјâŜȼӆȣƞԊįŌ©Ĺə\x8fɏʼcɨǽцŲαқуŉʐ',
                            'parameters': [
                                        {
                                                        'key': 'фщԍYӜɵiѧ\x81³Ûȝ/ƓɄ\x94ԏāɞϪā˅ɢʓÄ>ŹĩƐ*',
                                                        'value': 'ǫєϓ:ЖҎҼʣѢ}ч\x81×\u0379Ο\x8e\x88ёTԬĦǣҎѤÇҒԛwНŐ',
                                                    },
                                        {
                                                        'key': 'ңǤ\x9aʓȸÛѾɣϱVÇѯ˂ǲ˧ǍӐ½ǭǙҦÿÜQżŽѐûʾϔ',
                                                        'value': 'ѐąј*,ŬɊψȖʖ¨ӳÝ²ѨӅʹΡ¤ϗӹϘ˴ΙȹӒ˥°Ԡĭ',
                                                    },
                                        {
                                                        'key': 'ɠҥʃӥӯЁҿϙöɖɅќԨĕʃǩŗȐǫȱК"ԁҍʰїкƛƸӒ',
                                                        'value': 'ʫƬȀѧɫȜӽĘђϥҲΠГыǁԋʵǘɰԍˬÂӺәҜҷųɾƝҧ',
                                                    },
                                        {
                                                        'key': 'е§°VɰЯ7q˧ђǡŨƙʬˋҰŐ{Õ»ΆӮīĲȬJEϾǰҧ',
                                                        'value': 'ɽώÅ˶ϱ§Ц\x80ѯʹцFѓōÑɒΘӏžӪӵӞqŬ\x96Џԇ\x98ȎЄ',
                                                    },
                                        {
                                                        'key': 'ȱùęӝñͰώȤÖ\x9f1ӅĈȑ\x81ȼ$˵]ԭʟÂ=´πʸơǺўÊ',
                                                        'value': 'ʵіǮ(˄ςїϮńˮÆɞϢіɡſΪГĬƒњ\u038bƪќϰ˅Ȋy˨Ϥ',
                                                    },
                                        {
                                                        'key': '0SùтưŘҒ?ӼԂ˫¶ʁ\x9eǻlƅӲĮÓͷǘό$ҶˌзƯԞЛ',
                                                        'value': 'űɧУ\x80ѸԮ\x84ɍҰŵҧĕǉțϑ˻ϤˊŵǖѹΨɓ\x9eCŲ\u0380\u0381ī\x91',
                                                    },
                                        {
                                                        'key': 'ԔɻßˍƃӥЉӖǄΒäԊɺ\x92ō˗ҳǾ°ń˧ϰғǑɱ2ʆƳ˚v',
                                                        'value': 'Øΰň˱§Iˬ\x9fʬΛͷșĚǔӕӞӳàąÁҨϳŸҪԐųȀȱǜπ',
                                                    },
                                        {
                                                        'key': 'Goύɫ®ȼĔɽĨ\x83ŝ`ΝԤʼĊϴѴ\x93}ҦӢ`BӔǢƯwϒĩ',
                                                        'value': 'åђöΪɫ·ʬʋЎѝӖиρɂ˰ѦZԄəźƷϜЁԑŹʷƣςɑȚ',
                                                    },
                                        {
                                                        'key': 'ɼЪɊͼɞʤАĤÓӍˑϷςŻɭ',
                                                        'value': 'ǩӌɈɍǸʉŅȶǢǠξΟɶƚϻϔn\u0381ύɘЛ}еVƜϩʈΑƣ\x96',
                                                    },
                                        {
                                                        'key': 'Ԟѩoє҉ŧѬҷϕԪ¸σ·\x84ȍ˪ԋǀΝ ħ)όƥːťΊ%ΙÇ',
                                                        'value': 'ӡǤЈƼʹƻ˙ǒžpƤхȄĘǑςѐή\x9dśӤȼɽóУӮǜɟøԞ',
                                                    },
                                    ],
                        },
                    'comment': 'Ǉ£*ɑʭϏžҊ˪\x85ίđǉƍθ0Ɲͷgʕ´ʻϖӟȂüҶQЍC',
                },
                {
                    'keys': [
                            'ёƄɑ΄ɣϜΚƃϪˡȨÏʲʯԜĭêѲ¼',
                            'ϭΐӭΒ¸ӂΕĉ®ȲӑӞȎԕ¾ԖȝŉϔӎɀZƦє',
                            'ϣ҉ʐ¤ŎǮІѡӣƋ6Ǽ\x8cúӬӅ¿˨',
                            'ʍÙǛӏѬəӵ|',
                            'Ο϶Υʪҫ{ȃɄƗæŘ\x88=ɺÓΎˉϡÖǩҮ',
                        ],
                    'event': {
                            'target_id': 'ȇ=ХќӟȔρ\u038dʶԏӴԂɥˠ}ɗ0қͼɎГőûaqĬĵϨέ2',
                            'parameters': [
                                        {
                                                        'key': '˼ѝѭĮgʸʚƘŹ˻ӗϠʦƅˇʦҟӰԜԒ@(Îԡ\x8aȻĸʒ;҇',
                                                        'value': 'æоԏnƤüξϢƶģƉκƄϐӐʖ±ӫϗȪΉʀīҩҳˏʎŬ²ƃ',
                                                    },
                                        {
                                                        'key': 'ɩõϪϳȷϼǤΙŵΈÅԊӢJ8/ƝЈЧȳĒǏѝčĐʎɴĀƛʽ',
                                                        'value': 'ТÈǋʎȥ\x95ÁķŲȬӔŤńǏxŔ<ʭΫԨȤы&ɆǎщhβŚӖ',
                                                    },
                                        {
                                                        'key': 'ӐҍЧŊmʔŔЬӋŢǅӂϓȿǊѯ;˞ŚbƭǢКΣϡԌ++ʹÈ',
                                                        'value': 'ϹɼԅʮɪϹʥШʜѦˏˡ[éϋ΅ǺɣəȳŜƬ˰"Àж´˓řǎ',
                                                    },
                                        {
                                                        'key': 'ȏͰËҍɟĠìӋȾeîȥХÉӁȱ,ԀĄԈϦ\x96ˆ҆ϧϵʠÝȜӵ',
                                                        'value': 'ØIҽ\x96УԡȜͻϝéƬGԐǿʹѪʌ\x9cȷɪȉɺκLĜӹɓáȉ÷',
                                                    },
                                        {
                                                        'key': 'ʭʢ˾ªӣ\x84áˏŪɜҍÇҶӏ',
                                                        'value': 'ľǨɖŗӹà¡ϢǳŋĨɗƘӏƫƶɪÆƦ;ĊȯÝä҈ȎTΙ\x8b\x89',
                                                    },
                                        {
                                                        'key': 'ËѸӹƲĴ_ϧ\x81ФƧWćȫă˯ʌµҳȻ\x96ɚ1˨Ѩ\x8eѱǔ9˂Ͻ',
                                                        'value': 'Ԇáβ§ҊўʂpВ\\˒ơǹɰŶӠ\u0382иÿʡ',
                                                    },
                                        {
                                                        'key': 'ÏǮϷ¢ϷkɘĮȱŧӇȇƟ҆ȬѵϩҊ˕ǞȱuтĄфɀԂǠȤ˵',
                                                        'value': 'ɹӪɟĵфӏЗ¬Ñǻɧ~ѕʠЖ҄uҲԙӇ˻ððʿʣȭȽɡͶď',
                                                    },
                                        {
                                                        'key': '¢űǾè×ǥÙÄğǬɝҢƼ˭ȽдɩŎͽlӇƏ҄\x8fңѧԦԖ¸ԍ',
                                                        'value': 'ǡźӕɖХξҹȂ\u0381\u0381ƿǏɅξʓÆϊΎǑʯɢӤщ>¬\x8fƧϔέȊ',
                                                    },
                                        {
                                                        'key': 'Ƃúżӊ\x93е£ɡʲħCǴǿȺЗԘGͿвɨˉϦƒ',
                                                        'value': 'ӐǍwϙΊŌɅЍԇʘǔǺʁ˂ʒȨиϏéƶǭӟѥԈíͿҵsȫψ',
                                                    },
                                        {
                                                        'key': 'СɫϢ®ʏʯƃ˅%ˇAíǴôч¼вʳʧnϨЗƷ\x920$сԕS˃',
                                                        'value': 'ϡ|ҜӕҢ\x87ĬĮΆːªҞʛŪõΡɖ\x8aȸ)Ĭ¨ҵѐҌƪĴ\x8fѵØ',
                                                    },
                                    ],
                        },
                    'comment': 'Î\x98η½ˈʈΝόσӖ҉˔ȥƪåƒʄӾȼƐΛӺϭԓԚ\u03a2ѯϮ%˰',
                },
                {
                    'keys': [
                            'Ȗ\x83ž-_ƳϵǾuɦГȿϥɔѪoө|üxƉŎƧϵ',
                            'ɢԝΞ˴æʖƎȄғʤρ!ÑҸǬОUѲр˖ǔʏ',
                        ],
                    'event': {
                            'target_id': 'ʂӥŜԕЁӰȏ\x89ƲТƼȓҏ\x9dҊƻ\x89ëĢƅ\x8cǇĭӺʋГκќ]Ġ',
                            'parameters': [
                                        {
                                                        'key': 'ґӼˎăҠwAȁӢȤӡƿΦѽхûƿʳˠíϓŊцԘæȂ˕ȷӅƐ',
                                                        'value': 'ЅʚΙÐ˟ʘʸɕñΈ˪ƹ\x87ЃįWǑʟѼa--ҶѯiŹϩŴʔ¹',
                                                    },
                                        {
                                                        'key': 'ŔǱӈ-μԃ͵ˏ\x98θӈ:\x8eӠСªʛ;JϜƧӤԜǣɵÜǶƩȃϢ',
                                                        'value': 'ƞʴϦəϘ˹żЃʺ˸âʀF_ѻȊЈýćΟ(ͰѵʊԦ³ӲëΕģ',
                                                    },
                                        {
                                                        'key': 'ӫǯđӼ',
                                                        'value': '\x99ʕҖūȬÀƲдТ˷ϐюБυǰįͰξżӦçŖ#ƞȯӉѦuÝÀ',
                                                    },
                                        {
                                                        'key': 'ҿӶúªϹϪɪ\x8cЯӡēȴ\u03a2\x8f\u0378ɓäǵϸϙηìƳҰ˧ёνƴ',
                                                        'value': 'ŝFɶΝѐӨ҅ΓÍЩҏΏѓ\x93ɓаŇыӆϛ!ƄăңӄƜZ\x99˪À',
                                                    },
                                        {
                                                        'key': 'ʁǘҘӃҺѠѸʡ"ƛξāϕƋРϜґĥĀǼèԇ҈īЎ\u038bũ',
                                                        'value': 'ƜʝҰҫÌǼɉԀұ´ԅđҲҩ\x8f\x85ϞШ_˟˸jȑ«Bӛϩ\x8aL8',
                                                    },
                                        {
                                                        'key': 'ǓĞҩԝħϯӀˤǹÐóѵƚȜԙņǵӧľč\x87\xa0ӠȰρ\\',
                                                        'value': 'ЂƏϽҹȠÔϾҬÒŏϮνƱѫ\x8dғʪЗʼźτ\u038bΎϡӧŭѼǡÈʕ',
                                                    },
                                        {
                                                        'key': 'ӨԡǓÿĩǞа\x95ȭ\x9eγԊÊӰ\x8eͻ˭ӖƖʢžЍХ\x99ΚǠƛϊνɯ',
                                                        'value': 'ɧųϛ¤ϓԛѳƬҁƩţ˓ə,ȳϗϥ¡ċёǃȈƒɑѨѐť΄Ǿǵ',
                                                    },
                                        {
                                                        'key': '\u0382Ǫԍ\x91ВӳǔŠгӐș-ϼĪ¨Ӂѐɇ˶ѬϱʆſĔ(ϖҿƵԠȮ',
                                                        'value': 'ŃϳͱȏέѠΈǳ8ĂΟè˔²ħÓϛƐҼĖцǃηȨĦiǸǽћɺ',
                                                    },
                                        {
                                                        'key': 'ƞҬȼ˫ЊȄǣɎďeʭ˛Ȝ˩·åƦ¿Ś',
                                                        'value': 'Ȕ˱ʇcÌԞ]ĉ³ˋжŁȐфӷӅǬǷԀǟ/ӾӤ=ĹʘϠɜǑг',
                                                    },
                                        {
                                                        'key': '҅ǛæɓÅӘčɔĪΣӗ˝ʔçѩɣκЁɷͼ>ԭƻ˹ˮԋ£ъƗε',
                                                        'value': 'ƑπáȽϔɗʨǨЈгĶԗĥѴқԗҲоƟӗѯҐ\x8aɯĕʝɧ˩v˟',
                                                    },
                                    ],
                        },
                    'comment': '§ҠРɋŽ÷΅ʐӰ5Ƴ˧˅FɖÉęС½ё^ȍԖĖГŢÜуˋď',
                },
                {
                    'keys': [
                            'ɀȂɿɏBƛȍȎŮΩ\x92гʨǯΡϕŚ҉+ʷɖËЎˠ\x93җoϦгȡ',
                            'ȟĂ\u038dŦĆҞԍ˃еǲԈ˂бԁƺҰЕ',
                            'ɲÔң0ɓŦȿņəҠǝt!e',
                            'Òқż',
                            'έýŤԙѠΑĴÿèļнԗɨӁ',
                            'ʜϏěʣʔҴɮѮƴǑ˨\x8bðāåД˚ΥʳƝ',
                            'Ⱥ\x7fðÇǦƈγ¸˨ЊСҖ˗šɮɾӷ˳ͱɰьψ',
                            'ʃӆӁ҂ˍаӽɤԕÖҾ\u038bķʳI',
                            'ӾҠΤШЮԄәӀўϪƌаąþ\x90êǴȾh±˝ɜ',
                            'ԇŕ¿ġ˘ǻŔÖ˯ԂӶôʥAŎЧӐ˫ȴ×Ū˕nʋ\xa0',
                        ],
                    'event': {
                            'target_id': 'ЍAςғƹõ˙άϤɻæ¹ƚɦӑtʹҀƢöƔјϑʵ',
                            'parameters': [
                                        {
                                                        'key': 'ȺϭҼ$ѓŁϷύΊŭ',
                                                        'value': 'ɹǡȍqέŗɴƠѢȃϪҨ©ĶҍͺŅѢͻȥΕ·Ƿϊ˩ʊ\x9dʠϺʏ',
                                                    },
                                        {
                                                        'key': '˪ΝҬĹҕƨ§ӠϐԨ\x8dλψÐǅƊĆͳәˣġū˰ϝϢș\x81ȔVǜ',
                                                        'value': 'ιɻŊǼǖҧӹԔӆϲǿәǡŅѫΑʂҟǗʨљɺ\x9e˘ӪчȽļƬĳ',
                                                    },
                                        {
                                                        'key': 'Îĵ/ϺЙʤǆɡēƌΗɡɩ˸˭ζƉʝ1)ʌȘǃϗԝéΫʚҾȷ',
                                                        'value': '҃ƱųԜԉӔҼĔӒƠ\x8eŊêǈȪÉϷɖķҊѺРˁѱԤ˅ϺƪЩ,',
                                                    },
                                        {
                                                        'key': 'ɤɎƩƽΪԩϪɯʘѧӚ\x8fɳȏΔ\x87ςɫɺΦæËЎ˅ɖhƚʰTЈ',
                                                        'value': '˪әŏĲŠ\x82Й\x81ʽɐ4þƬˌ~šĮŪѼΡ=ƚˁ˭ѺЎǝ0˻ʶ',
                                                    },
                                        {
                                                        'key': 'ˁ˒Ρ҆ĄѰǧғлÈŐƕӧˢщƃƓēӐËǚŞǰtǀĲȑ˻ɫș',
                                                        'value': '>ĮЎ˪$ȘΛѻԃʕƠZɢľҖĲȬȑʧɰʥЍԈѕюɈɨӒSƄ',
                                                    },
                                        {
                                                        'key': '˥ɬƊǎϱΦ\x97˲πͲĂҸǳҥ˜ŻʏҦȎ\x89ХĐϓΐƏ҈ɟȴ\x93Ƹ',
                                                        'value': 'ƻѯҳѳЗʏϔ˓ԢʸƘЮηɥÜ҅ѴґѽǓʷ˝ƄǋϝΌЇҙņǨ',
                                                    },
                                        {
                                                        'key': 'ŋɠӁӣőν\x90ԤЭÜ¨ʨˎϘˮнӘ ˽ΚѰũßβы υïΗͲ',
                                                        'value': 'ǌϘƠɿȃԝǺԝϿΐżąΏƥρҦȒһ˼ң6îҦЕΞѹ\xadȀƚγ',
                                                    },
                                        {
                                                        'key': 'ӏŨƠǧӎƤMƭ˃ӧ`ȦɒӚϺƝ4ʎǅ˺Ȍğ¦ϾѢɂɓÒӻƍ',
                                                        'value': 'ŮȗѼͱȒϥʾ˟\x94пԒlӆɛ˜ӸaƵӕǫļϬюɾҺХ3ğιȈ',
                                                    },
                                        {
                                                        'key': '\x95˄ǢзƘÀǯў#ϋџHȥζϰӠÞƯԤыҞ˅ƳľƃE\x83º\xa0ę',
                                                        'value': 'ϜƽΉƋȯȣā\x98ɮˀι\x83ϚǽКЃ˗ϗÒϏ\x82ƚęʗǏԮ҈Æ˸˺',
                                                    },
                                        {
                                                        'key': 'ŰȏġͱʬƘϥΉщÿғXͱ˻ΩΏѶЍɋRБύlʻʷ@àѠϚӴ',
                                                        'value': 'ĂĐˈԣЄÂк>ӯǱ΅ə˺ǐψȰX˓ԉԚëàǭ>ȲσǛú˫ʶ',
                                                    },
                                    ],
                        },
                    'comment': 'ζĥΧČđʲʏԄò\u0382\x7f\xadӏ6ˇͻʹӧӲɤı\x89§ʾӄ\x9aΖЃΗ<',
                },
                {
                    'keys': [
                            '˪Ћ\x93',
                            'ːħǦÑʆ',
                            'ӇǶ\x90ŜԫȭϐvϬƶŤő¦ȢϣƬϠϋƾ',
                            'ðӀ¶˟ŉƻʹȥѶǋŵӔ',
                            '\x8cǂ',
                            'šӂʍәԢʪ]ʕΉЧКԫǏԄ',
                            'ϥȆǷȧώЦ4ƹƨΥ\x9cœяМЍԨ;ǸӗςÃͿȝˣ',
                            '҅Ő:T҆ʂĉţ',
                            'Є·ȱɏʾʟ',
                            'ξ˜ϼɻӱ·Ҩʫя\u0382ҰΔ˻ȳЇҘϥй\x88Ԯψʗ',
                        ],
                    'event': {
                            'target_id': '˟ɭΜȳӟȗХǇԒ˷Ȭʌԗzίϊеº[˨`ͽ~ϓĀÔӢ¶¦ε',
                            'parameters': [
                                        {
                                                        'key': 'Ř%àɦѺΑòҫԜŶ±ɮ+ÓЍϨʢ˸Ҟʕǉ+ȱıҷѯ1\u0380ſҥ',
                                                        'value': 'ȝΠԖƯfΝʪЗ¿ćŰļɍЏƂ˫щѾ\x8c˛Ї\x9d˓˰й\x7f,˥Ɂı',
                                                    },
                                        {
                                                        'key': 'ӶŠ\x84ĢǓƧϞɄ',
                                                        'value': 'ϞҬнȱΠùчſƄŉ˓Ҁ˶ӧϚӈǽɏĄҐԔԡЫϸΠԅõ˫ʱ΄',
                                                    },
                                        {
                                                        'key': 'ϟ¶ǄԔŭƵ=ϲ¡ԞӪ˲sħςʒʡҝˍȻƃϡԫ˫ŷǸĝ˄ӎČ',
                                                        'value': 'ѰӿȗʠĭȺ¦ĸƿѢşȫӂǮ¥ǜɜ\x93,¤%˻ΔȢϩ\x9fνȔкԕ',
                                                    },
                                        {
                                                        'key': 'ʟʅϧćɨϒɦʙĬʼƝӚĊЂϸȀҾɾԃɩ.όʾmɤ͵ȲВѳҨ',
                                                        'value': 'ɺ\u0383ƠϻϬџӸǊŁҮʃӺӘʞǇЧÂԨĝѠφ˧ȠǇҔƚŮθdҭ',
                                                    },
                                        {
                                                        'key': 'VbɻҶŽǎ˘ƠȨҬɿÃĲҹɵŭѳϤӣʊȿΆĲŜȮŤԊÿɉӣ',
                                                        'value': 'щѕʵ\u0380ŀƉ',
                                                    },
                                        {
                                                        'key': 'ҴʼͰ҅ƯͳИх˓аƒ҅ȉ˲ȩĶНοʟєɰѐʣǂʡхӣŴǆO',
                                                        'value': 'ŪŽϥѧċĝŎǔĄì©Ѐ¿ëʏѓįƞ¡|ƿɤˡįԍÈʆӭSԐ',
                                                    },
                                        {
                                                        'key': 'ǩǜӖâ2Ƒ¹ҚÓӴε%ƄдηԖǩёθĪŧτѩɇŻǘMϐ˅ϴ',
                                                        'value': 'ʎԇŌ&ɚМаɣҼΏэɐœԕū¨ԂѢ!ȭ\x92ï5ЫÐΘRφϗŻ',
                                                    },
                                        {
                                                        'key': 'ȶÚМԐƞ;ŪȕŒЮӚƶňҋЂԡҌΐȜГŁņƶ\x97ưӜĚĠԚ4',
                                                        'value': 'ſα6ӓ¹ӭЛԧǟÈɁƮƪƔӇīǀ.ӰʽҕKƊΡƛɋĝȦ¿ʖ',
                                                    },
                                        {
                                                        'key': 'ʱˤȔȥҰϤк{ƥƾ˝\x8c˝ϮųЃzϡăƓϟξʺϐ¦кҿнҡО',
                                                        'value': 'ʤј&Ҧυ˜ɏϞɨЗ˼²ҥƃͻĨǃϽǠϓ҈źϷIҵĬʢƨȇ˾',
                                                    },
                                        {
                                                        'key': 'ϲԤƠÜ2ɅӨƀàǅß;ҒNžť%ʄԞÉӖƉŋɁұƁɀƜ,ʲ',
                                                        'value': 'ӬԩȯϼΊȑ±ά2ςԢǯkŀ;÷Ҫƞ\u0380δ\x8eȲΉ˽ʾȿʛɑ\x99ӂ',
                                                    },
                                    ],
                        },
                    'comment': 'ѕřгѵΪćDiǂӌȻҵİɬȅƄ\x96ϒӌӉҊƏēЄϺӔʇpδϗ',
                },
                {
                    'keys': [
                            '[ϢĪϲîӽӟʌԙǖŚњԖ\x87ʩĔȡʬͳbӆ`ѸǍƅʦκ\x9d\u038dή',
                            'гĠȯƱЫŭˬϘcЖћϥʜɹ',
                            'тDˠ˶',
                            '˵ƈùψӡȝĔïϓėĻƲүÓԛϮλȁƉƴʹȌ¨ȱʏϥŷƻӸɀ',
                            'ΖŮӉӋT˵ŌќӠ҄Ȅǫȭ@ϑʎΒѡaŎԩ]ʹˈѻ',
                            'ʜkȔȳ',
                            'жνƕūӀǖ˼ƚΠʗʤɇɟ;ƆΟʗ˟DēǯğҬ',
                            'ǶǸ\xadжĂʻ',
                            'ʞԐoӇʶВĜҿ\x9aĴʑ\x9aͷ\u0381ΏƠˉ\u0379',
                            'Ȓ~ВӯȟŜеǔʍϺːТΡϱŚπʱңǽΡǴſŵȟɇ£Ф',
                        ],
                    'event': {
                            'target_id': 'ȍΗԝϽǔUыКȫrӟʣЬѬ˞ӻҝ(úԂҸ҃Ζͻ»ԓЮǑǞʸ',
                            'parameters': [
                                        {
                                                        'key': 'ѥ˙ΨmҾԣҁŃҚƿҦãиȪҖΙļƷȾϝɔĲȎÙĘ\x89Uϫѹѽ',
                                                        'value': 'ʦҤǄҢȪԚҶņЮɧʋ˱˵ԈɥҡҐƭǯɐʾͻΆԩƇƓµǔйʧ',
                                                    },
                                        {
                                                        'key': 'ӌԝҖĜƕ\x92ǾϓѴŅ%ʱ3Ŷ¢ϽГĊȕ.ƕͲŶ҆ӟƚӂŻǱҟ',
                                                        'value': 'ȁʋǤˌķȪȧʚˇˣąƕŢƟӉҬ¼ӱϗ΅ɬα˗ʁγʹȲӥǴĦ',
                                                    },
                                        {
                                                        'key': 'ԖҪ ϕʀˋӳʁяɹŰўԕψˎ\\ǍôԢʇˢ͵Фǀȶкϕsşԉ',
                                                        'value': 'ʆȟˍӐˍѫƴҟǶеæǞňԄΥȢŝ8ԮðғҨǞơȐοĦƳƟӥ',
                                                    },
                                        {
                                                        'key': 'ŻȟJĤӚǛ\x8bñ°õйԏ˕**ˎhӈϭБϥb\x93ҩͶȧǎūˌμ',
                                                        'value': 'ʾҠԫĸɰԮЎώϧ˘ĶЀˤ҄Ěɠ\x8cĈѡϐňˢƂłď\x9eDɺɲ˞',
                                                    },
                                        {
                                                        'key': 'SȿƄʱWмʝшþƫéªТ3ХˁѻҘԩɳԌ˶',
                                                        'value': '±ʬΑȒΟкɟ=¢Ϗĥ˼,ԫҾɚΚĒyÌ\x9e\x9dЄʡԘȄ;êзÌ',
                                                    },
                                        {
                                                        'key': 'Ãħƕ]ύƷӲʄƞɿӘ|!ѐǙ',
                                                        'value': 'ұ\u0379ЇԚʂЭ˗ǹ˺ņ(ƉҫKƍȌɳѷKʜԐƛҮϗԈԍӚԭˣɁ',
                                                    },
                                        {
                                                        'key': 'ǫǅÅӯʖҾӕ_ĎXâ˟ѪɏÅʕΔǵ͵ϭͰĭͻ',
                                                        'value': '\u03a2ďτɧƀˇͷL˧ԬĶϕĺĴǡђŤѣͼ*f˒ƵґҭÙȜ7ҙʵ',
                                                    },
                                        {
                                                        'key': '&ˢʫΏҸuşÀŮ',
                                                        'value': 'ѯϬӑǻɞЗÊĉƑį\x8eĂ.Ėƽԅ˒ӯҙʽͻͽÿȲŤȓȞJæq',
                                                    },
                                        {
                                                        'key': 'Ǆ˂RȊѦƌťНӞӿ²ŹȗɮԋѮԖ?ǬщĞԘ%Ē/ыʢїȞż',
                                                        'value': '\u0382ĀǣdʹΖԤhӃэ҆ÂʽØ\x8fΧОΗǑҀΠ½ЉљβƘ^Ϟ§É',
                                                    },
                                        {
                                                        'key': 'ЖćǡƧ\u0383ώƜȗʑŸӏџǚ҈ϓţȂηϚѦӘΛ',
                                                        'value': 'ҟ\x98ϽǨ˕ґĺԮȈȏ\x8fϘµÃþϒʠСΊĭț҇¼ǇûȝϭʠȳX',
                                                    },
                                    ],
                        },
                    'comment': 'ĢұϚʌăĔɑéǃɚăӥĻЊˡƾρЄԘęʅ҄ЎȊǁҺzѣӗһ',
                },
                {
                    'keys': [
                            'cӧѡˣϯǽқŬіʞͼƒǉǶʺӇџѨŸ&ǒȁӎ\x83҇ɰ',
                            'ɋԞϫŕϼŚƑҋȷɅʺǉϳҫθÓǃЊͶňҔư\\ϭг\xad',
                            'ȎШӳӍØɂNÿȅʚӤӾƽ\x81ȧɌ\x90Įҍ˸\\ÐΘʯ',
                            'ß\\Ѽʾϙ',
                            'ǐʖԂȎλżͲɆ-Қϼ\x94ђҫȲǹKȅŞɢ',
                            'И˛АʯҎ˒Żɵόȝ҅цŬДӫşƶµÝԄϩ÷Łƞ\\\x83ɫ&ϑԢ',
                            'ɌǺʄϏԒЬĦӭЮ_ſȨëņѼΏ',
                            'ӺɳϥΈïҾҬʗɺґγTʢϽƻʼНƼǬяӇӽ',
                            'ԋˣѕ\x83Ų9ǯԆŮÛʾäʅzƸ',
                            'Ø',
                        ],
                    'event': {
                            'target_id': 'ʫǥΓς#әшǿʒϬʫċɎʻƩóȧǊŏŜԥȸԅʞ9Йȹʓŀƿ',
                            'parameters': [
                                        {
                                                        'key': 'sƧҋӆ+ƃпɄʷńӥӣ',
                                                        'value': '©ӎ\x875ɾɩϪʕϦǴѻˮϴǍË˯ȰƄϨƣÍԝǉĔҝҜб˱ȡ-',
                                                    },
                                        {
                                                        'key': 'ˑƪɿ;ħСӏƺҟƳƞѓϒų\u038dӥˤíȥϘ\u0380ŻэԦÎБōϥӭb',
                                                        'value': '+BåţCǞ҉ѭ9\x8fȧ˺Ðҷ)і¿˳ъƣѺх}πȇŴÖ-Ȁΐ',
                                                    },
                                        {
                                                        'key': 'ğŉͺΌĲǂqџ/˨ǅσЅЁ7Θ-=ŦĳԬ~ЌNԏԫάƟɐѥ',
                                                        'value': 'ΩўΆŘЍȊ[ȐÖϱҫжΌȸХʱԉũϮӰжԐʱɔJŔФ¥˨Ҋ',
                                                    },
                                        {
                                                        'key': 'ЙɏĴϫƻұtȰĒ\x8a˙ǿưѷſĠuͽǺɕȥɂԍƧǾ¢ļДӰz',
                                                        'value': 'ÅɔиȴӧŔ¬Ñ¿˜ɉ>ƔŽӎΖƥȵх{ƲĢȹъϊSϽҐеԮ',
                                                    },
                                        {
                                                        'key': 'ϻ"',
                                                        'value': 'ѪѴƁң˩\u0379˥әƫŽҐ^ӮҹҳѰҿɴÏ\x9a)ϸǵȂӖ^ЈӉ!Ł',
                                                    },
                                        {
                                                        'key': '<ΡЄΕ˭ʶˮǿЅɭǗεԜδʍѕȿƭƶĵԎ¾еƙ\u0380iƃԤ҇¿',
                                                        'value': '˱Ȭţƣ˷шmǡǝǝ˖ö÷ҟɽѸńȵŭfѻӎƧŒŎŮÇŘĉӣ',
                                                    },
                                        {
                                                        'key': 'ПZʣКɝҵϳǮҙбӚЗуǊӑ˱ĸȇƴӝɺŜԇbŘԑĆÓĳɒ',
                                                        'value': 'Ʈσňsß˩ęļΌBЭĴϤʼƳԛӗӄzˉĽɈÜ˺ЗŮӇΞΕȯ',
                                                    },
                                        {
                                                        'key': 'ɩʽϩǼʈΉƐɥʧã˱£ŎǻƦɰҚӅϺFϠљӔ',
                                                        'value': 'ԥƇð\x92ԏώȊĀлʔ˪ϥбʧxȏӲϾПÚɰ3ȏԫǨɰͻâ˦ʃ',
                                                    },
                                        {
                                                        'key': '\x81ƹЇԖȯҍʀɡԀҺΛĀԫӗ¢ÁԣҰȈʸc',
                                                        'value': 'ϛXɴϖϭÙ\xadDϜϥǊːʼ\\ΓĝѕӬġӏɳǪäΐɂȏ(Я\x9c.',
                                                    },
                                        {
                                                        'key': 'ǏuɆйʢь©ҋԗĈʝ҄Ԣ҈ƺʨ=ҋd',
                                                        'value': 'ЪѐɣҬѐÛĉԥ\x97ӺǩӂŒʑ«ҞƘҞӍϷҳӀҳ˺Ӽˁ\x7fgɴǾ',
                                                    },
                                    ],
                        },
                    'comment': '\x8dǪĒɘҲθǔĥʞι˯ȍaњȓИ˃ӯHҔǚϬǂŠɱƘƱSĔŪ',
                },
                {
                    'keys': [
                            'ѹǘʆ\x9dˈĞĺɌýǡԇüч÷Ϲá˂ȫɪÑȣг',
                            'ЅÛɽȓ҉ϳĸ˶ʮǬǷǲтȏшȨ/aЯ˖χώ',
                            'ŊϪθǄϻѕ',
                            'ԋţϲ',
                            'ǧԂœ½ŹӑmčŸԀ',
                            'Үќ',
                            'ХÍЧќ\x8fʧƸºǭǼ`öѝˤȅʏǗͿƉǅƇßĦ',
                            'ĝа£Xчҷ˨њϠǔŤ҄ġmдϸ`ѨϾ5\x96\xa0ѧ',
                            'ԊѤFиǴ\u038bΘíé\x85ǄŁĻĿ}ýȷ%ӅӻА¢фı˼',
                            'ύǂѥʬűӤ\x86f˅щҋεʢŮŦӨ¨ǽͳſќBȉú',
                        ],
                    'event': {
                            'target_id': 'ωĉȳrƨĺΒǫƏÆǞ]кÀrʽÃӋñȚ4ǑėƑūӦʐ¶µΚ',
                            'parameters': [
                                        {
                                                        'key': ' φνҪˏʬѮɪϽȗз°Ƒ҈ΣʪĮѬ\x97ćȶͳ˅Ɣŀ ӿΠƅɨ',
                                                        'value': 'ĸԠ\x94äɓČ\x87ϚʹЀş\x97ŒDgUϹuͻǁ˻{$˴ȶӱOґŷ\u0381',
                                                    },
                                        {
                                                        'key': 'әɾǿƙʃ7ǒ×ȓԕçЋϡ˫ŝѸjƎɪ˕ЂņõƤ\x9dηЩƯѽˏ',
                                                        'value': 'ɭɇ\u0378˒ҍҳоĕκĚʇπ÷нįЙУ»ͽϽ[ïǬaΫԠƩŬψÏ',
                                                    },
                                        {
                                                        'key': 'ėА\u03789vȗȫɷԦЯŞǐ\u038dЂźѨʴńљͽӝżȠԠņҨϔȫĨӺ',
                                                        'value': 'ǭǥíÞŤпν@ʮӐțӗҺƤӽӄϰɴȐѾӻϭϠ¨ǓΗɼȌΨѡ',
                                                    },
                                        {
                                                        'key': '\x96ĐҥɽԌɶфҹΪυдϝӾԒƩӟĔȩ˜ȈªЫɔКÊѩ©qӽя',
                                                        'value': '\x8eȻɛѿƚϦҌʥ\x8aǳȩӌʠ˩ΟѱϜǃіǝЛðäŋςʉϷФʗϧ',
                                                    },
                                        {
                                                        'key': 'ǄǒΥϖήЋҧѴЗƯɫXĢНǡĒјƴӷ"˰ǸŰɄƿ\x9dӳƖӽ\x9b',
                                                        'value': 'ӯ¦ćŴ˂Ǜɫȓ«Ƙɇă\x8bѢл˴ԓVųŪүΆɥƣοʹĈѸ[ī',
                                                    },
                                        {
                                                        'key': 'ʎɧȤҨƻõνԓĎÔǢӟɗнĨɫĜƓΖıùčŕŇѣҾэагȯ',
                                                        'value': 'ǟˋ\u0379ɕӀɾƩȶÇҘʐѤϫȮˌïǪʢн\x9dҳØkʩͷϳұѿΒϑ',
                                                    },
                                        {
                                                        'key': '®ȗАѪŧЏĖƓȓʸѬ\x93ѝöɓҞöËϕş\x98ԇ¤òӞƫĳΖɑ;',
                                                        'value': "ʅɎϚʹ\u0383λӳҦŎġ£ʟǋĠ£6Ȣɮ'ϛǈρȳŌ\x81|ҫԄȅʫ",
                                                    },
                                        {
                                                        'key': '$Ħ\x95ǾüĚĂʜѼүл£ϰӘćÇЏƮȾиљWɈкşʇÓԮKɫ',
                                                        'value': 'πġʹӳϷϵťϼѥ¯ҵТŹ\x87ȸİшԇÒʀΨόŖЖиǶǖˎЁҘ',
                                                    },
                                        {
                                                        'key': ',ɧЗ\x86\x8bʘѝȄӇΆӥʉКϊӽǪԣjоӧYș¡İŞяӶİУѐ',
                                                        'value': 'ðɡȸϣϕ¦ŗĭ;¯Ж\x9fѿǟϨŅκŐxƶοԞϒҎŽҁ7ǐPǵ',
                                                    },
                                        {
                                                        'key': '҅Ø´ƁĽȜʙôȁ˘ǫУʏ˸ƌ',
                                                        'value': 'ѵϙГЌͻȠĥĉԣɛ\x9bҶӧλΪї5Z`zЪє²ЊЇӮȉХʁE',
                                                    },
                                    ],
                        },
                    'comment': 'ЗLТϬƍʬϧȼΩγӎŇΆԗǳϤăƋϠķ\x88\x88˽њƼǐ¾ȅ˯ŋ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'master_sequence': [
                'Ҳ',
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
            'name': 'ȰʇЀρƪKєʃФˁÅԙŐ3ϑΗːȁDLťˏ½ĵέǠƆŮ\x90Ĕ',
            'description': 'ĕĲɻɊд÷ǈġé\u0381Μʞ\x9eŔȔȏı˺ƩʚˮԟǽŝƿŭπμӦŭ',
            'target_id': '˟ʥ×ήѓȈјβɮϺɿҧŻŊŉпʜѡԦÖӐǭӍ÷ö\x82ѕ·YҨ',
            'parameters': [
                {
                    'key': 'ӂԮ©ҏӌі˂дʵŘ΄ΗÔþǧПd¡҇иϐϬŵҜЪ˓ԧŖʶp',
                    'description': 'ŻɳӷƜӋӰąͳdȩ҂ЌԛѩġôѾϛƘϜ˴ϲɃͿєíӏ3όΖ',
                    'default_value': 'ԢńЩşȡňƸԮԬͲѐƹЗūɯĴȐƵšħ\x81ԐĿИëœåȰäɜ',
                },
                {
                    'key': '<ɕHĘӞѶϋӷõϓкCɕԭ\xa0ϣҦɦѢʈE˜ԠѡρţӸǬūѝ',
                    'description': 'ЛҜæȠѽʏ΅ɲӘΗϭƉˡӜ"ҘðƶΙºΣɍ\x8eȳȘʕѯӱǉϙ',
                    'default_value': 'ƧǣuϐӸǠʢѿˇԭиƩʢͰǹѿҮŪ˧҃ЎҏйӪІ¾қÆÆń',
                },
                {
                    'key': 'ɜԕҤϖɌ$ʈӱƏϚɈƬd˾ϔ\x82ˑɎɡςʭџőüϙš',
                    'description': 'ɧ˾ʺÍG҅\x81ԡ˲ÚʫɫȻ͵ŮʩƂ˝\x99ѦɾʾɢȖɩХϴʘe ',
                    'default_value': '˧ДȚˌ҃mІġˊɶɪӄӀӌҚʕîǄͽПɃȱҿЉӢȶҀŗĒl',
                },
                {
                    'key': 'ȇҴσÓň˚ҍƐĠ\x80ǊӫѕȢϠČэȌĥЊԊƿҨËԇԪɜîĞ˥',
                    'description': 'Ҫ\x94\x88Ԃ¤ʐâČәӵӪʚқѱʱӏFӮþ7ϪȖҲƞϞϱ]ΜеƊ',
                    'default_value': 'ȈјˁȧhңѴѠѼǵԪ\u0378ñQ)ɰԔι?ѱʼƸ¨ƅϫȹʼȔΈʏ',
                },
                {
                    'key': 'å¬ƣŕŤ\x9eϟȞʱӆõƼˀęįЛӲƊԅŚͷƓưpěԬωʘɲʏ',
                    'description': 'ȻЖƵƂƚ(˂Įn\u0383ѡцʨͱ\x85ßƺǓǆϥǳϖҥŚô9Zɭβy',
                    'default_value': 'ƁʗΰŭΌȴȔҁ˫ϩͿѩϪíÕ\x9aӺжĢЇϸňюĐ˵ӴЈŻšČ',
                },
                {
                    'key': 'ҐʾæƬĘӛӉƚÜѲӬԃ/\x95ØҒéďɷɩēńҗͰΔűӛ\x8fˌԟ',
                    'description': 'ɘңҎНДƫƕШ¡щþϚ˖ϮӰ"ѳʦβƉKˮõ\x87ɷ\x97ϱÞŌӤ',
                    'default_value': 'ĽĒԤˏÙϳrʋЎұ\x82Τȼʟ?ϡƼŢƑѼsɋ˙ȹԍԃϦϧþξ',
                },
                {
                    'key': 'ϓЬϷʠѽϿɽȺґņώҰÍá±Ѯĺ¨QġƊžʝФфęÔ\x86ǐÞ',
                    'description': 'łԮʨӾѶ\x9aǖȽæǊѕǾΙͽoʧеѦ°ɓƘЅʁË˞Ǖϭ\u0381ʛÖ',
                    'default_value': 'Žøӵſ©ŉͿ\x81ƕåʩҘǢε©ʖЛϦЂΛ#ΣâƴÓϳάˏέӖ',
                },
                {
                    'key': 'ıлԇӣӑœΟϬИŗбӄϘΝɕ҈ëțɒuȟĔĭ\\Û˓\u0378',
                    'description': 'ӋſƽȃҕĽӺʠȶˬƞКƦ˾ԉsDËȡ`\x80ҮѳүôȊшΡŘL',
                    'default_value': 'êįέXɡ0ȖҪӾ\x85\xadlϼȼΓ\u038dǗѰʅǂǋƝԟϦɗpDĺǔҘ',
                },
                {
                    'key': 'Ưӱ¡Рˍ',
                    'description': 'ΆħϿ,³ǉP˧ƚǰŴЕѨψүǗ¯ϻKȏ!Ŵ§ƩҰРώьľ\x90',
                    'default_value': 'ӈѐ¾ɇĚʦ#Qƃʳ¾Ƌɽĭ±ЍϞĽŕӳõǝʞʉ)Ӡ)ʖŏ˦',
                },
                {
                    'key': 'ç5',
                    'description': 'ȋƏδҒN»òԕƖЎˀǔǪ~ǯɓwȶǊȕêą\u03a2šΫĂżЪʟ\x8f',
                    'default_value': 'ǳЪuȀ˰ƀϓɾҜѰyӏϚ\x86\x95ȧ\x9bǘҶ˩ґ$ëѺο˟ϹȦҺғ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȁЋˊ',

            'target_id': 'ǣʿѯŰӔ',

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
                    'name': 'Gǹ`ĉ˫®ҁ˻άʖѺǕѾ',
                    'description': 'ʺϧάӱċХŁϢǽӯ2´ί ШɱңǩAс\x92ğϧ϶ѐʔѮŗňҕ',
                    'target_id': 'δɧǲ&ǚπƩȮĸƪƕʜ˛ÙʽĐ·ӊΎʡϯ\x80ʮɫɵ\x99-ƶăϞ',
                    'parameters': [
                            {
                                        'key': 'ûLΔˑϺVӈԒőƍόe',
                                        'description': 'ȔԫĴ˱ȚЅΔγѴʑcĠ¯ȸ\x8fƕ¶ːʪҳ}Л˯ҫŌԪәͷĩǥ',
                                        'default_value': ']ҮҍƞрԔƛRƫńAÛƲˆŏΝ˴ϋ}\x8eÜėˠőɞӻΘȅԦЉ',
                                    },
                            {
                                        'key': 'Ӿ˲ÍǞɻѴƐɀƚǇѤʎиÁʣͳǼԞÅZπʿŝɊӼґЇªϣŬ',
                                        'description': 'ͱpϏĉŲƀȘъV¨~mʖϡęƬåίơԗϡϡ\x8eñwԣɨ¦Şn',
                                        'default_value': '·ɡї@ʅȠŸɯľ\x9aӬƙԖġőǱԤ4ĿÄѯƒ\x99ÌŦгʹ҈Ƕɴ',
                                    },
                            {
                                        'key': 'ĜˋȖϺȀÙʴѭɓŝҕˏɹʂ\x95У\u0380þѺǿԢҘфѬɚа:Ī"ł',
                                        'description': 'Фѫc)ƬRӥҥ\x99ɳ\x87ƒȟ¢üðɘσϺȻɗφ˅ǫǆԫÈι!ԉ',
                                        'default_value': 'țhϪϭөǿҁȕγӁП6ƲѤʑî˕[ŧ˾ϔɖäů\x7fʋ¬Ә\x95g',
                                    },
                            {
                                        'key': 'ЅҕȧԖӳϦΟўʴΜѳ˫˾źѪ:ɔΌĲŬМξӪҖƙĈ҂κÕʑ',
                                        'description': 'ӚЃɧåњͶǲςϑĊʺ\x80ƅŅL˲ɗԥҡһÒƎͲƇ\x97ʫөʧįʂ',
                                        'default_value': 'ʜ÷ȱӑůȧІɘȶ˶ƶƦԒȰǯkͳӸˠƌ˻ȷq·δƉˀ\x95ħƙ',
                                    },
                            {
                                        'key': 'Μ\x98ԩҏΧ\x8aȶ_ӈƪ`τθˇŏ¾ȥƏω·ưӇO',
                                        'description': '˥өưϡɔǚĿƒKԢƆҁŀÞҾҀԫʿ;ӈϯ϶ΦɶҘёuӗƽӺ',
                                        'default_value': 'ԄМΠòȒӀ˗ВυʯŴӥʃʶɾõЃӹVчѺȘԆɨϥβѤÝʟŃ',
                                    },
                            {
                                        'key': 'ʊ\x89FÂ˖ʹ˓ȃƫВʾHǟɄ©ʽ˃ҭΨ=ƋÈɌѸӲɤ҇ѳǌϋ',
                                        'description': 'ƯfƿΛ÷Ȁ˔ԩɸԎǡĲ^ƱҨŖʚ¢\x85ƟӶɗԠʤƘăǌ\x80ėǠ',
                                        'default_value': 'ƷņȬοɾ˓ԁЁ¯ƠƝŵµː²˞ɉӋӨΘɨѸǾɛԙvƝȜʂʳ',
                                    },
                            {
                                        'key': '$ПҞñΈӢͲĺϭѿГϔԠ`ǬǟόǪ^ԈіƹÇµb˕ӹҔʱĠ',
                                        'description': 'ʍ˗ȫɲν%ѺԜuĐҊ҈\x81҄9rŇǎȨӋКÚ˨вКЗԖͶðʰ',
                                        'default_value': 'ϷИӴɗѸƝͻȨ΄ϟβŸʾ˖ĔТRԧƗɡǂɽɽÜȑ\x94\x88\x98ͻƄ',
                                    },
                            {
                                        'key': '·Īœ½ВΕ˴ʹňǈНЭʞSƧ3ЋӸаȧϿѸԃ˕ţǃ&ƷƧ',
                                        'description': 'ɍƲӏЪóĹíīıүӤЮŪj\x9cȝʈūȅĢӛӔԄеҒɥʪӍĂ͵',
                                        'default_value': 'ӖwϱО\x8b÷О~ԋР\x8bΐкɂŐʂæĉÈ\xa0ґ˝Ӊ½ҹǣ\x9bρ˽π',
                                    },
                            {
                                        'key': 'ˀ·ʮкźѝ ʏӁʎόԓҙүӛԡѮwƈgÃϵӈӸĘѕћКҘЋ',
                                        'description': 'Ȥ˰сҞЈƒ˹ŷͳēŜÓô\x93ά҆ΆǗтɧ\u03a2Ì҇.ĢӉҨԌĐƫ',
                                        'default_value': '~ҩҢԓʟW\x84ơ˟ґǐƓЛξļĬԈƭȏŒ˱˻ѻĹſƌ´\u0379εĢ',
                                    },
                            {
                                        'key': 'ăʪώŪСԌу˕ӎƇ˱',
                                        'description': 'ǝÀƊǦ\x9fӞĿ|ЊλǂӛԟĻBϤ\x86ĦǍƦŐæoϚ4ƶԆľǩ\x83',
                                        'default_value': 'IĘlǆΦǪȘʺή+ˏϒϐϦ6ԚɫƬЌǄ}ƓџńɽƑV2\x83Ϣ',
                                    },
                        ],
                },
                {
                    'name': 'ǵ²ƳϭϪϳԜҼԉ\x98ρΌeYë\x95;ĢƋɝ˧ѠҠ\xa0ӱǙ\x99đӆԝ',
                    'description': '˧ʹȲʣǗĠЏȣΘѽϺϗÞҋ²ȫǊаˬɋˮŬ˧ЀŨѱÅɁƣ}',
                    'target_id': 'èĪͱïˡƗϘ\u0383ˤҞTΡǂÑʕ¥ЊђѥιʑЗƠΰǙØñÛпŔ',
                    'parameters': [
                            {
                                        'key': 'ȳǼĎϋ\x95УԔѶ\x9cҜǜρŵʨžŧпɡλЂϢ˺ȼɠӾáѓĜȪĈ',
                                        'description': 'Ч\x85ЪŐʧҼΔˡȆélΔʿˬ(úϞǔŲ1ʡϕɱƘϋѡцЪϧƿ',
                                        'default_value': '¸vαҺǹǘɏԐɮʻ\x8f\x812ǊгѵйΗǶǭǾшƞҷԎѐʫη˹Ӵ',
                                    },
                            {
                                        'key': 'ЄрÜӖ˅bĬԁѡĢēřɍѭPҿÝÊ#ӗѥӯ7kŚŏў½ŋ\x8e',
                                        'description': 'ŴHÐӔƗѨΨѡùȣL-ʳͻΔȶaƗϹ˸˳sȝx˓ǈϱüΪ¯',
                                        'default_value': '÷҃ûф#ȐǛ˖ǄşД˒\u0382<ԞɝΨάƭҬ˼;ŉȋѽҳӐ:ȵȳ',
                                    },
                            {
                                        'key': 'ђ«ιǡ[˩Ӧ˯ïѰŅ˶\x92ƂғÙхѲΚ\x9eƢ˪\x8fǦǓ\x9aȯҠɄʒ',
                                        'description': 'Șːhώs\x97ǳĸΰųǈӇƱәÚc˴ƊɫЄѣČӑǵЫрIȸÚƆ',
                                        'default_value': 'ӈёǒЬǇ/ŜUĕĠс\x96ˌöҐA\x81ȐԒϱŊȾȍʔƱ+¤Όʜ',
                                    },
                            {
                                        'key': 'ӠԛRЧ«ΰɫ¦űДӇҿԭ\x9e¨Ǘ\x87\x8cϚӝÂѾѮҾŚǁδǪ+Д',
                                        'description': 'ҥбӿÚǦ äˀЏϝҩȈÐҦt˧ԏoļʓԛ˾˦Ƥȗд˘ƪУȧ',
                                        'default_value': 'ũПΔΕʉˉĶʋːńӏӥ\u0382ƍƺРʢҀğҋnњǣςʼѴÖһПЕ',
                                    },
                            {
                                        'key': 'ȼϠӭš²ˆ˂ԩʺԪɳһδԎȫíӗʒЃòƄƫϠǣζſǥþТω',
                                        'description': 'ҫʩʺʊͽѦйȜӊѓȰˮӎEƌo\x9eЋƫƝӒЍӆˡΤ»ˤƋˈ¥',
                                        'default_value': 'ɫūƣӭɉѴ\x93ʌ\u0380˖϶ӠȪÈðƙгǦϸӑѧҵɁƇŮȲȭʚ˗Ϊ',
                                    },
                            {
                                        'key': 'Ҍ˼ʽ˚ԦϗҚɮȅǦǱΣÛǼҿƢ¨ӖўωҖҙþӋȀΣRԃ×˚',
                                        'description': 'ʳjϵ7κȹ¶ǠČsŲȟίƆЄЇԫłȒΊνǏē¨ǅȐСŝϳ\x86',
                                        'default_value': '±3ŝԃ~ĪĥǉȀфđȀ}˚ßΰńȊµҧӲțĽϻĮĳϯ˥¬\x81',
                                    },
                            {
                                        'key': 'Äй˻ԛɳ˦Đ\x94ʩĖ¡ӒƧԘάŽɐ;ΖȯҵȻӔӽľή;Шǟʊ',
                                        'description': 'ƘҢȕªǔа\x8eÖ¡å²ĤþҽϴҍĀŪêɈĆ©ќϰ[ПɇǮÑɵ',
                                        'default_value': 'κRȋȭ˩ΜʹèбƖΗϡʽҘŁЦƷ҇ťǤȑкȫĈĬňƸѣé\x7f',
                                    },
                            {
                                        'key': '·ťМp}',
                                        'description': 'ǟȔȵȘ\x84ΟʤŷơϞQǬҨ˭ͷːҮǯɾɨӤΡȷӶÏʴΘλӢԉ',
                                        'default_value': 'ЩȥʽLϫJЦӷʨ˕Ͽ҃ŀԜʘʛ>ǋĜӆcНƵÓ҉ʺιėµҕ',
                                    },
                            {
                                        'key': 'ǻԑĊИBԅӼҀÀėӪҧъԣǮɁïʊиȶίǮĢžā͵\x9aȁřơ',
                                        'description': '\x85ĩƦԪяƻҔпßћЃ1\x87łƟҳϬıťҜȃϒßЮĒ\x95ƌүRƽ',
                                        'default_value': '˯ǺɩƘӠ[ЀԣͽĮƩƢɝԜȷԐˁ˧PϟʆͼӠËŜǧϲˠφß',
                                    },
                            {
                                        'key': 'ҫΦÛϹԬԐŠ·Ƨԍǋϧ³ӄǆ˯γơʬˊҙƧāХЍ\x7fԬнȑѪ',
                                        'description': 'җԀф΅ŪӅЍȞƄƳƺѥъί˛Ҷŀê\x8fŊǻԫɞΆŌԓ\u0380·ȋР',
                                        'default_value': 'ǅ\x92ȸôҧηʵюŻҬΙİђ˪ÂӷЏƐĉH|˺ӛσҔҙȑаĢҩ',
                                    },
                        ],
                },
                {
                    'name': 'ѨɀуŞӶÕƤѣG˥˨ĿʁӍƵЎȤѵ\x7fƶǔѢɃεĤ>ǷӺɵƞ',
                    'description': 'Ƙʤ[±ȜҟԒӳƂēüǱĐoȪѽĵËԗȳɾѤ˜ǮɎ˔ԅʎкǒ',
                    'target_id': 'Ѳ/ЩΗƁȗÉЍώȱê÷ĥϏǙѥчжҼ\\Ъ˱ЬϾ¸ӮѰͷƶԧ',
                    'parameters': [
                            {
                                        'key': 'Μʫ΄ƆʺγɌɞŏ',
                                        'description': 'øƦʥƎɞ ʧϰϽԫǎĢi҈өɊ^ŸDwXӄàѳѩŐϒĴԝ"',
                                        'default_value': 'Ñ;ȏhΔԛ¥ģӿЕнϯBϖѤƅĖϹӚңȑԝƦΜԚНǆћ˗ԟ',
                                    },
                            {
                                        'key': 'ʩ˩ÍҲɻİÒĘŁȕȱȎѴǝϞËϽúФЭĜͽɧƒӭǁҎ¢ԗӡ',
                                        'description': 'РͰοǇθǎǾѯŀ˱εʄ˵ƺͷϢ6ʲōƥҗ(`ťŶǵӊ϶ϣЮ',
                                        'default_value': 'ȱȣ\x7f\x97ˎdˀӽŋƶ¥έŃčgѨϤԨpǥϑϊȂɿñɹјʪǽȃ',
                                    },
                            {
                                        'key': 'Іēȟ˓ϰϼΈ.ɑΤψʤɩƩwӭͻŻ˥ģsǼØԄϒѵԨƪ-ʖ',
                                        'description': 'ǟđΝ&U"ǅѐĔνyЗűѓƅԃҞ҅иҬlɠPϠ˳şԖƖҦǱ',
                                        'default_value': "μѨǛӮʳșэҩ҉'}ÄÒcɩŶǘЩȕпȰ¤\x96ϩѳηǬӁɵ¡",
                                    },
                            {
                                        'key': 'Ͼ\x95\x8eІӺИDԬǇ°}ËҪăwǖԬͻȤȴʘ2ƼԡӶӄȦȘǆt',
                                        'description': 'ѰϫǪΘмүĳȮ˻ɘҒҘϗǳҋѢΊWJұԇ·űŉǽѠϦǴcԣ',
                                        'default_value': "ͻwł˭Ԕɋ϶ґɠѸzԟюƦ\x87żƨëԔͽż-ɨϑ'ɋ\x96ɳӥˉ",
                                    },
                            {
                                        'key': 'ȈџƆm»УӉλÌϠϪƝŤ˶ǋTσƊ@ž*ÚɊɶ;ĭ6',
                                        'description': 'ѿƶ|ǄLўϺɔΗƅʑϱʱb\x8dʒ;ɓӔǡіәϵΆʀƵŵſӎϣ',
                                        'default_value': 'Čб\x95ǾɓɤɬӉҤѢΟѪВЅӒ\x8d\x8bχǸÍНҼæzȫѝʃǨЍΐ',
                                    },
                            {
                                        'key': 'ςѤJUˍӭΗ\u0378ѾģώȂV%QïͷЙʦƲǁǏΤπÎҎŬǿЗØ',
                                        'description': 'ÝҪ\x84ȅy]ɬɕčξȶϯʁƚΰÝɸҙƑТǕқ\u0382ʖȤӶǉȅōԒ',
                                        'default_value': 'mñːәȗłӻʁЕЩDΧűśǥΈӥΏʬĶĔΌXίȯЏɹҗҡƸ',
                                    },
                            {
                                        'key': 'ΓӘ˶ǥɕӭȥϸ˭ˤĀǳȥ˧әõӬȘƁħӄӺϸЪȌÃҒ¦ǅѺ',
                                        'description': 'ǶǦѓÀ»ȋϰɹʂǤɅʲӆͼѷ\x99үϹˆLĤEǽϋԋɭБЂԪ¯',
                                        'default_value': 'ӴΤǀǍŁdϤҾËӜǀЅ͵ ѼԒKё¬Ԭ½ƚƢʹԡҚԤϬӰѫ',
                                    },
                            {
                                        'key': 'ɶ(Īǯ6ȴȅΫΞЅѱгПͰ',
                                        'description': '˵ʓ҈ϗēҺυÏăƄÂɋdĚЧԥȻÔàҼϩԛĞ\x9aʗнϥҾxƓ',
                                        'default_value': "ʓԎȋ\u038dʲ'ƣƽΪӰʪîíшΎ˽\x8c˄юԬșƽˊЋΥĳ\x92ǔїɿ",
                                    },
                            {
                                        'key': 'ǣԡ\x8eЏӍΑѰѩбRƻ˻ŪʋОϥΕҽȆɭƼҴԙį\x9a҇ƄДos',
                                        'description': 'FɱϾŊ¬˫˦ҸǕŔѫȫáĺы˚ªĩόåɍϹ҉^ĸԮơçǑÿ',
                                        'default_value': 'Ӂ|ǠʫƏ@OȑɣӨĪǼǇɧǫĶɎʟҰůʰ³Ԉ˵Ɓ"ƴǤ˵Ѝ',
                                    },
                            {
                                        'key': '¥αʒɦ\x7fϨȢΪϱ:ΗЍŵ\x8fưеЩƯʰίɒ˝ͷʃĐӕĄϬӺ_',
                                        'description': '3ϼϔ,MĒ}ͺǦêҐԫĲϞŽǎθǏĄżȷǖÒŁ˻*Қ˛ʙё',
                                        'default_value': 'ǌίǧĜ˃;ʮĎѹηÅì\x9fUǳϰѬԐԩĖɓԓmŸωɉҟώҖΤ',
                                    },
                        ],
                },
                {
                    'name': 'ČўȃɎȹϮQʘѫĲ©Ҡ°ʅˠªǆɜӋԃӰσĘϛĠωǯȦǝɎ',
                    'description': 'Ј\x82Ʀ¥\x85ϒçӚȏɥ\x9aƀҒ\u03a2ҒˬӴ˓ǨͿÜϓӘ\x94ȅ{ӏÐǷŕ',
                    'target_id': 'ķ\u0382ԈǁˣɃʣӭĻӴѿ%ЩԙƋÐЩȤџ®ɫːˍ҄ȎϊķѸʈƎ',
                    'parameters': [
                            {
                                        'key': 'ÚԠǧӪѢȰĿǸŨԌǤ\x8eяͶÎŞTuʝѻ˞\x93˾ѫ\x84҈ѤĒƓȭ',
                                        'description': '\x7fȃŇϕ3хӐȑвƍθ˱ɥʋĖ\x81ĬҙĒƴäŜԀӴµkɏ»4ʜ',
                                        'default_value': 'ӜӃƒƂχ˂ŐЕÊӁ˼ӄέʞŚđӞƓƩѾǾÆëʹ\x9fҍϠҳκЩ',
                                    },
                            {
                                        'key': 'żкƜƢ',
                                        'description': '¢ԩϸӛ˲ɌɐɭЙԘ˕śӲʮӖȞɃâйƳʁǗřϽҶ¦½ɦŻϟ',
                                        'default_value': 'ϣ¯ňҢӗΈņʕэèҥˏȗьŁĨєMҫµҮԕʷǣҶȻϭʪҍƿ',
                                    },
                            {
                                        'key': 'ųÝľ˜ŅĄԬAŬĥ\\ɵÞҍӇʢ˲ɃŮhÔИЦɥӅ8ИҕʩĈ',
                                        'description': "ȣͲʌǰ'ЬșҦɨΤÅɯŏ®ВɦҒʎ˦ŕѬҺŤĆцсÛ3ԡ˘",
                                        'default_value': 'ьӗƠŉy˂ʨϫɒʌȅƃŤ7Õѻ˄\u03a2ԎəıЩȪƢӥȶþ',
                                    },
                            {
                                        'key': 'ƅĜǃ4ҐγҵǿĠÃ˯рԚӾǇѴ÷ԕԠҌ',
                                        'description': '\x8bɭѨǶȞßKƘ˘ԩȉӃуКϖӨѻϻΗΟǋ3\x83ǭͼˑȳƐɈС',
                                        'default_value': 'ϠţʰɓʞξѫǞҋƐˬɜълӠŭЗĔѓȽ]\x95ɦӞѻÐɲɛʃэ',
                                    },
                            {
                                        'key': 'Ʋ',
                                        'description': 'ѨǓ\x9dòşƓȭƧǪòԟ˚ЈòѫUқɲû»ӐÞĆ˵ȉ˽ǔΝɋĘ',
                                        'default_value': '˟ԗ˭ƥ\u0382ғӆӢϾЯӆȒĂʖĭΈI\x89͵ɁĵϳõϱɞѢɹJȘǒ',
                                    },
                            {
                                        'key': 'ҮZƱŐ\x8dхɸǶ˜ˣӖűѸƠ',
                                        'description': "YŨŌƗ\x87ÙʈU˄ь±Щa\x8eĢ˙һеÞǣνŧ'hªӾĔ˧ˆμ",
                                        'default_value': 'ǬɈʹζˮuȲҐ!ϊӵҿҡȏϜϧ¸ӖO3ӭ\x86ԗǈѩĕø]ƐӃ',
                                    },
                            {
                                        'key': 'ĠԒϷjӍҩžǫnǑŨӨʡҽѪɜ҆ҩxŵбɰӽͳƐǜԧǚљǹ',
                                        'description': 'эſċ˹@ɜÈÄƈϰϛƀʹҎӕɗŀ¿ŦšǙƄдǑƪ\x90pǛƦ\x99',
                                        'default_value': 'ͶïԫӼѶаδҥаc\x84ǦȣЍϜāПʼπŔǢϖ+ơrǳҺ˜ƞӨ',
                                    },
                            {
                                        'key': 'ƼФʧʙӔӊЃķƥӄԀˑғɜƩʛΏ\x86ğҶͲ˹ʝΥ',
                                        'description': 'ϫ*ǕЦĶ˰ǝ¡ѮǲüǶų˥ĀȦΫɼɑ¬ҶфVŖьǫдɽҸɺ',
                                        'default_value': 'ʻ\x99ĿϲʞΑŨHėɲɜѦŏµÐˢ7ʑҔљҖϒӦԓƇÖϩƚΜȴ',
                                    },
                            {
                                        'key': 'я˧λŭȾh\x95ЭѲ¦ԢӉˑɩиuèȰԄ¸ɵϴӰȢÒˆî',
                                        'description': 'ʮэфłўɫХӍ\xad6ѭ΅Ү¦ƛč҉ѩΊkϭͷԬЁŖǈ˕wǻ\u0378',
                                        'default_value': '\x90Áƍ҅ϒԮEҭ˼\x8bѰȾőѰԡs˕ΈuÜJѩåԧ¾ӅœљɅ˛',
                                    },
                            {
                                        'key': 'ɁńΡ˴Ŝ',
                                        'description': 'ħĪҐǷöɧɋȥ»ʛђɺϲʳúȀɄÁԕĺΡ×őŭǒФӂώйȡ',
                                        'default_value': 'ɛĵԓkɘʩûˢĤҽʳѬϑЦӌҕєSɣ¨ӍĒGɷɨθ¤ɱԧơ',
                                    },
                        ],
                },
                {
                    'name': 'ё\x9aˉØ˒ғʙɿòϤBSɾˠΌyɍŒƿ˱ǣŭŅýƈ+ȰΌѤυ',
                    'description': 'ѣȧӱҔԇɿ¶½ҥɛǃáĐɝȭ˜ϝjy҅ϗİǾƁӯǬΔѢǞž',
                    'target_id': 'ɕяІĥұĲĮºфӁΏ?ʗφƄ˥ǤКϗСĿԌŚƞϡɤ2ƹ˷Е',
                    'parameters': [
                            {
                                        'key': '\x83äËϧͻԧnΔЩÞя\x90ќ±Ѕчɶə',
                                        'description': 'UѨԋáǊɃЪϢǶɗϟ;šіԛˋΐˆɼǇͲüʬA˻хȅԚ',
                                        'default_value': 'ҀҸӃ˛һуϤƨ\x95ŤԎʰõò.ĽѴƍǬƝԅjАDӲȨӠƦԩʡ',
                                    },
                            {
                                        'key': '˅ѾЌҼӺǵ:ȬǥqͿÍħE˭d\x81ʂΞ\u038bЇƅǶЩњԖң\x93Źп',
                                        'description': 'ǯb»ú\\ǚʸɀ΅ˀ>¹ʹŹԗˀOŬБýʩũ˟ƐƮ˛ҏáʌʜ',
                                        'default_value': 'Δȓʘҭ˼Ȓ3ͱOнȄʇȿƵʍЕȆѧƀǾѹǾɏkҾбǷϗ˱ɬ',
                                    },
                            {
                                        'key': '˟ϙŝӞƲ',
                                        'description': 'ˉУˈЁ\xa0ʕÉ9μʶȊƎƥƋǑѓɀҝԋɹǑiέɻ,ȉԉ¿Ѧ˲',
                                        'default_value': 'ΣʲҋґЬΐϘÆɱΊůэƇәſй͵ɴwÛrX\x94Jǉ«ǫӍèО',
                                    },
                            {
                                        'key': 'ƶ<мӘ·эÒȋʱԂӣȀȋ\x7fИӎƑƀǟӌ',
                                        'description': 'ǋѣŶ®θ˷ӨʵƥːǂԓϩϚƔέʭǠȟǽǼ\x9fȸƝjÝԧoӵʫ',
                                        'default_value': 'ɺƱÁÐï˃цΑѨоŠÍĳĝӢИȡ˗ӦαϋϧЪCĿĵȖķ˃\x8b',
                                    },
                            {
                                        'key': 'ӘǰĜт',
                                        'description': 'ІɃшĕȬƸƸ˼ßĬ/ƘЍЄĒžг\x8aΐ?D˅˵ȔѶĨłʖŀӬ',
                                        'default_value': '´ϴƃĉіѱQżˣǏǳӇЩÔɭŚ÷ƪФĒ҇Ґ҃˸ǭƲǔȄҗǜ',
                                    },
                            {
                                        'key': 'ʻ¸Ǩv˃ɃӥųԁŶatĐ*\x89ƹįѰ\x98ƌDҾԟДȢҲȿΝĤԢ',
                                        'description': 'ӪVЭӭǨ˸ƺˀ+õҞӣOŜϩēÕʁɈʶӦҫ˴ʓӸǱśƈ΄ʹ',
                                        'default_value': '£¾ɬ ǣWӉǮҩϹʳµȍ˼ΊǗ\u03a2ƝÐ˄Ț˯ɨŦ:°èŅԭӗ',
                                    },
                            {
                                        'key': 'żίĢÇӿǙĂĚʿ˦Ό\x8bƿнʍɂŴɧѹƪ϶ƎÛ9αɃːҘϏʵ',
                                        'description': 'γ¸ȉцΦӋǚӦûǲҵƩċȦȵɾƜ\x9c¥ҶƁεǔ˜ɉӼhɻϬb',
                                        'default_value': 'ӂΣпз˲ǈʓΆˌуԆǉēvŠ˘\u0379˓лЦİҤϪ˒ȩґѤˇйĝ',
                                    },
                            {
                                        'key': 'ǋҁ',
                                        'description': 'ӡӣōĄÙɄɆŖʅΚ²ųˍ\x8dοϮԍԞľıԬ',
                                        'default_value': '\x88Ѱ˺ԩ˽\xadǜʁϹɱӍøѣRdɲ)ѶɷΒΡǜǴœˮā\x85Ҧǡҏ',
                                    },
                            {
                                        'key': 'ҡаȎЃщ\x86ƁʅɶzОӂґŪҝǅuǭ¶åŇҔЩľƵϭƷť-В',
                                        'description': 'űxϽϵ\u038dǻԠɕƎðҵɤŤ·ʹѱķϰǰČάϹGĭҪĭιϏЎʣ',
                                        'default_value': 'ƖȾҀĲĸДȇŰȔ˟ŧϚŬŅˀlʜϘӔѩ\x9fñ-ҧĬYƟӐӸȗ',
                                    },
                            {
                                        'key': 'ӇǈÀ\x98ȅЏ\x9eΨ\u0378ԚѵÔӤМЕΧʀŔϷïѐдːΕƈɏ҆þĽ˹',
                                        'description': 'ҀυлʉȈͷԒ§ЃӃʳÛ\x8aȐƆƦҍ˱ɴҵ«ѹшЇϨмϤԁ\x97Ü',
                                        'default_value': 'ĚˣŔ˯ϩѕφƅŃɻТԈΧǴʝќˬ¡Ҁǩ\x85ɠөĨԔſԏҝ½Ҥ',
                                    },
                        ],
                },
                {
                    'name': 'вϲȯəҺåʎ҂ʮ\x8bҲԋƾAƜΌʙƎǌүĐÒŤŪрǣůԮZ2',
                    'description': 'ƜӑʪˡϹВԙ·ÔЫӷȧѮũŠӀљâҘǕɭζɾ҆мˁѳŜhЧ',
                    'target_id': '˗iԈŲĨҲǮҚȀ¿ԔAԋ¼˅ȤҩԔѵҊǐԪ¿ŨƘύѬѲҧȻ',
                    'parameters': [
                            {
                                        'key': 'ȸˊÎȆɏƓѴɀ\x9d\x8cƘǩԍƑьѵɃπ˹ǋ´ϡȔȺƕҢFȁȧұ',
                                        'description': 'ԮЌңʓȚωȏЕα\x9dΜȍǂќԇȞ\u0379ӰǃˠѫόѢӣЮƶʆϑĭҘ',
                                        'default_value': 'ʗĊΡ²İ¤ţʦΌJϮӔΪŏχȿΔ*ҧʠӜdȥ\x90Χȉϵǃ҄Ԏ',
                                    },
                            {
                                        'key': '(AȺБïɩƶоƃβϞƺ¿Ƃ@κӍβȆӠѐѽӐŒ҅ȏΪß',
                                        'description': 'ԟʜԩɑƃɏ\x90Ƚҝȧ4ƈЌƎIԒΒ˽\u0381Ʒžԋ˸ńԕʀ˾θ¥Ϗ',
                                        'default_value': 'ǐɴɆҜƪʥʂĦǻУǶųɕŎżΆȡƞĖԓ\x95\u038bȻ\x8cЂȬvéʔ˘',
                                    },
                            {
                                        'key': 'ҮƑϩ˦*\x8aЬϋΝ\x8fHієԑӍİђʭƈϫǱŕ¹ԖβĎʪԦ\x9aЍ',
                                        'description': 'ΑëŗăǛʹ˴ãż\u0382ПφʺËΠϲȱɎĕÿĀȯϋ\x99т\x8fȌô)˴',
                                        'default_value': 'ԠѰǪȨÞӜŁɷԓwұΠɠ\x8aĺňIѼ˄ΝȚЅń=GĐԏΚƟM',
                                    },
                            {
                                        'key': 'ʝʢßhǂĳĲҙ8ҞǵɓƵŕȚϯGԈʸҞȅдĢҸҬô-ǖӢM',
                                        'description': 'ɦ\u0383ԂàɁӥcǏΩ҉ԕ\x83ѫЊƁѵƔԋȴʼҝːűūϊͻѻǏj\x90',
                                        'default_value': 'ЌˁƼƸȐρδҪЃ\u0379ϋͻʘФĭ˦ŷːȮǕӌʿ#ǽϤźĖԚԝѕ',
                                    },
                            {
                                        'key': 'ʓα˷ʛӟћķ˛ҥÈòԒą\xa0ī\x92ɞɨ/ҦњԨ˃Лɝ˵κšҠѫ',
                                        'description': 'dʪρӻȻeʈˊǅʹɑѯӥϮȸŲМB\x9dˏƉǖɥ6ŭǴҿόэʛ',
                                        'default_value': "'ÅЀˀɛŞϕҺɆˏɇ\x9bƽ®ȈȬśԕԍåÕəʩƆì(÷ӷ®È",
                                    },
                            {
                                        'key': 'ҦʰǘȕŘ(ǺȈƐ\u038bʳǆÞϿċ¼Ǹ',
                                        'description': 'Ĕяșʜģɠ\x90Ŭд\u0378ѿňɈǎ®ÕκȘҴΨǞ˨ҊĻўѓԖΛЮΨ',
                                        'default_value': 'ǈ˶Ϭ\u03a2ʮʓQ)ô\x92ϴӂƚʯ¤\x85ğ˹љʸƺ7ıα\x9dĴˇ˜Hӣ',
                                    },
                            {
                                        'key': '^ƀΌƂ\x97\x84ĔњшЯҏӍӵ˪ǘ{ԮѪӡɓʈ<ӬӜș˄ϬšǕƪ',
                                        'description': 'ŹԏϗǙƗЌҒâεǟҐǞ³ʃҨ¬Ƒ\x91ǸĲĉΊĖԣɱ\x99ҬłƘŘ',
                                        'default_value': 'ȮӪЊnӸӄӽũįŻ\x91ҔϭƄ-ϸчԢѭΘ9˼OӅĥYШǗҰΜ',
                                    },
                            {
                                        'key': 'ҳԤǝďϗҷĐ÷ˠɾǖïŞӑʎùǉkЉɪŋˠǱͽĠ˯иǣ҂Џ',
                                        'description': 'ԉ˖ʋȀĬѓdęť΅φ¿ΠζƐ҄т°ȇǉӀŴф\x95ʷĻӺǍŒҵ',
                                        'default_value': 'ƑΓҍ\x98ʖśːЌŦҤǍĵʡœԍЦ\u038bοЌȭʹΠƣӞƐӔȫ;ɂ³',
                                    },
                            {
                                        'key': 'îγȶĝʏŦҡU˺Ѣr˾',
                                        'description': 'ȄƗʏӎ\x87Ӽçąʁ˫Þƫ«ƹǊļӺƬɈɰǯҾσȵŷӀ,ǫŝć',
                                        'default_value': '˥Źaϣ}¾ԫҼ˴\x9c҃ĸʍǨǦɧ{өӆƟȟӓԞřɵȸj϶ɚҿ',
                                    },
                            {
                                        'key': 'βX\x87ȨǇǾѱΥƳДԃċ˹1ōԥζϨЯÖǃԘԕȗʞƕ.ҏХų',
                                        'description': 'ͷѶϚϽƢ>ҏ`ԪҦ½|/ȲҝǉġȄѮˊ.ǸȤ˹ŬҷŭǬǵԜ',
                                        'default_value': 'ҨίǼ¬іҞʊĉͳÈΆɅ«ЕĹёЊӬԄǭňԓƩ҂ҬЧĖˍΎ˯',
                                    },
                        ],
                },
                {
                    'name': 'ϣ˴ƪѸԈԎϡȀғƑɁʣǴǳНΊɺΫǛƯЈϯӸÜҞɛƛͱѭǭ',
                    'description': 'ΑԘώĄ\x88Ãƍɤмģ˙Ͱʿ\u0379ʡҏӠO˂ȟɳĬΗς˯όȦҶ\x91Û',
                    'target_id': '˞ʏĖʑԓ˷öƈ3ĉʤšɦǐӶәԌűєɼɼȷƁk\x8aÛд\x8cïқ',
                    'parameters': [
                            {
                                        'key': '\u038dΌσȢӲǳћΓêԘ\x97ӷͻļʳƍ1ͳŧЃț;ȥӉƩȽԨǄҫ˗',
                                        'description': 'ǂѶóȇĕóȵƈϔȸ¨Ҽt\x98gĥưԧ¦ɩϦöƮǃuÊѧʒɃȑ',
                                        'default_value': 'ȯxƢ,ïĳ ϧҋi\x91ė˹Һâ,ƕιѻκĒƊ\x9fǈɊƶĉűɶǍ',
                                    },
                            {
                                        'key': 'Ç<ԙђҝŸэ\x89ļȥƸ˘ĵӥΞÊˬňϊ@ěLϢǓųӜ',
                                        'description': 'ӕӠ˚"ѐ˫8цҫŧĞОѩΔԖΤ@ͻϙԪ\x92xƮ\x8dǟКŋÙYͷ',
                                        'default_value': 'șÓԫЅΠőÎcІөӊԨɧG\x8cșαɚɰŠȊʕ\x9dɩȮŷɞԉԮǝ',
                                    },
                            {
                                        'key': 'ҷL\u03a24ɍЌǍòČƗʍǯљϝlΆӿїŮӕɚ,ʝƤҐ:Ӫǰ Ȇ',
                                        'description': 'ѡǊWʓԅӮԤđ\xa0PȕɌeǟćԙ҆ӢԢƯʘԣǮРȅǵʾHǙΰ',
                                        'default_value': 'ԧƶуȻƇҁqõǪӾǡҽҦ΄ǵϲʜӐBjʾёϜб±ƀΫОŘѰ',
                                    },
                            {
                                        'key': "Ԕζě¹ʗǝƖ˞Ϡνəҽ²ԨŊAѫюɔұčӊɐƓ\x8aЍƨ'ΓW",
                                        'description': '΅ҨƉѦǋʇ˘ɿǖχɡÄ˖˱ʡ\u0383Ҳɍ˟ҀӶ=ĥȆκ\u03a2Ҥȅˬę',
                                        'default_value': 'ԅĔѓχтҾŁϜГʸƭАЌɕǄқα\x91ēɠӕҏĳÙӊǈԏҖўɉ',
                                    },
                            {
                                        'key': 'ƴÇ\x93ŭϝ˵ƺɭ¤\x7fİĐ.LɄΏˈƿŔ3\u038dϼԨЕpʳZԒƤԄ',
                                        'description': 'Ƿ\x8bɨu"ʃΕkɃӕˀ˗ǉ\x94ϊɚ¼˨þǳŅ\x83ÑωΎǭ¾ӂьö',
                                        'default_value': 'ӔлҒ-ƄΧɻͷˠ\\ҫƭĩғ\x87ȔìĆіΙͰĀԬƯǁȩжҽϐΊ',
                                    },
                            {
                                        'key': 'TɓüôΦ҆3ц¼ІȑӰβųɐҬѾǔïɰș˟ůÌ˽ïʦkϛФ',
                                        'description': 'ȑ҆ϮЪÈǝΝԨőɿ×ϴ˕дĆ΄Ѫˡɋ˪PѥĵҢŲŞһƦÊɟ',
                                        'default_value': 'ʝΘӢξγ҆ɶͺȴƍąōԙъ¾_ϥҔ˂˙ЀšľȍʢОĂêЀҗ',
                                    },
                            {
                                        'key': 'ːųǵ\u0379\\ηΫʨʣǚ',
                                        'description': 'ʛѧʣʶԣƗϣçҚùVӑ˗ǅ˽ԫ\x89ӳϜ\u038dɐY\x84hƂȺǴÛǈɒ',
                                        'default_value': 'ƇҖƫʏγNˠѥæΊe£¿ƫYƅˬϒʷюɧаĽĮΖґělʙ҉',
                                    },
                            {
                                        'key': '}ӥrǛԉѦʫÉ\x9cӷġѿǗ\x7fÿʯP\x9bԦƲĤοϷoªЫɼηðɱ',
                                        'description': 'Ԥȷeĩԅ\u0378ӇÚ҅ŷԍԁÀƯҥŗ5Ʒƥб΅īԈȓzÁƜ˘ϥѮ',
                                        'default_value': 'ɕɔʵρĮěũľ·ÂЕƽԢθΐҽѡƵŪˆΊʁƫǹƣʄөpеʡ',
                                    },
                            {
                                        'key': 'ʑϵӬɥ£ǜҥЂ9ǕƵȩ]Қη˩\x80ƭ˶ęΜŇ!αʴΘĵˬɟɞ',
                                        'description': 'кʂ\x9eʶˇҼƬĪɭˊӁªȫɱşÏɄѕǶǸ\u0378eȷҟіĩ\x9fӘʒϫ',
                                        'default_value': 'σЬʂƲÙȮ¦ЩɊ«ЦʤįϹǫҎ˩Ňԃѹș\x84Ϊ\x9bŝίүɆɯП',
                                    },
                            {
                                        'key': 'Őҿȏ±ʫŃ˨ÐԋКӹǘ\x84ХͼЍβ˄pҜΪʺ°ʞĕԪȮҕшʡ',
                                        'description': 'Ѕșѥѷһɝ˂ΗɽʑуЛъĢ҅ɥɟжĩ˦g\x88ŗҐɳƗȸǜûǔ',
                                        'default_value': 'ʹпѾ\x94϶ƿÈӃĂҒӼоӱͽҹЎVәыŇʉȠςNɝѪϪѫƯǁ',
                                    },
                        ],
                },
                {
                    'name': 'YȘΠ\x83ӱLœӇԇǭ\u0380şΑùş\x9bщΊʓϴđɡĳӗа\\ȃԦӶλ',
                    'description': '7ȮĠЀȩp-иō϶bЙ\x99ş½\x80ͱаɗϜɰЫϮ{Ɇԍҟ`ӌȎ',
                    'target_id': 'ƎӓɴaΨѱ;Ӄc+ǐĚΙʰÅºſĿǤŉҘǣǊ˱˝ǪλѴшǋ',
                    'parameters': [
                            {
                                        'key': '˔pıʭǄȐəˌʫһɈѴh\x88ä\x81ϊȂϻʨòƾϣӻί\x96ӶπϬ˙',
                                        'description': 'ʼ\x95ĜϺáӚ¾Ҽ=ƷǧEоʍėȆǄ7ƙ\x9fѳʯ4žԖMϕ.ÈЅ',
                                        'default_value': 'ѓʇÓȱϞйǭӸӾҔѹǷӔʒӡȂΑҋÇæ®ԭéȤƨϴϧǋϬʱ',
                                    },
                            {
                                        'key': 'ÐЊêӻ\u038dҠƌɤċD',
                                        'description': '/ʃɞк\x8cӒƍŦһǍӚɳӠͶȄtлтʞ÷ǭҒԅƜčξƷɸǕȔ',
                                        'default_value': 'ͷʹÊŭûɈɧшѕǙʆҦŇлƦŘǻԒŉ҅ϙċȡőͱ҅&ω\x7fΞ',
                                    },
                            {
                                        'key': 'ȺΞȉҒΔ˳ʯΗԔĴήЃі\x80\x80ϐʙɷɟƶԚӧ\x8fªϔԣ˅Ԝ7ϕ',
                                        'description': 'ɏʺ+ԦцÄɶˠχʛɍNӶŦÉҝԩԛԔŮДʂƺԔUʗªŋŊӰ',
                                        'default_value': 'ː\x8ci÷łϢϜАϾɅɊώǀ϶x°ҀӾĐȻԌηюʠɇǉЗƦBŜ',
                                    },
                        ],
                },
                {
                    'name': 'ɠôΑӯ˰Ìɀˊ˘÷IͻđňΩӋˣ1ÀǵˣĴ\x84зӜңѺϸЭǬ',
                    'description': 'ҳČ]ƗОΆ΅˔FʡЃЫϺʿǙǆ\x9aǌӝΕʨԌʈŸ˹Ҭ˷ΎҾŶ',
                    'target_id': 'ʋԚМκ˄ӀȾ»ЉͰȪЈђƕĥ>ϲÓɪ·=Ʊ˴ЈǈɒдǇʧÑ',
                    'parameters': [
                            {
                                        'key': 'ϫϾ\u0378ƚͱƮċːgǬϚxԮȓʛ',
                                        'description': 'ҝȔȴ©ԇӰɰϑ˕Ӧ@kӆvʅɷʁȲɟϓ÷(5k8ƢĕҺǾñ',
                                        'default_value': 'ƴ§лƋǺʂΒĕЦȉӺ\\ӿĈĆӉӎаҩѼ҆è°\u0382ôB˛£͵Ā',
                                    },
                            {
                                        'key': 'ƢǄðǓɭn΅ȍʣΧȀ\\ɳήŋ¯ËЉňʊƐԥɻĪȩ\x99ƅҲȎƝ',
                                        'description': 'MiӜ˧όϮʯҿдȖǹ³ɬ³ԊJĂϑӮȊŉȈŻ˦ǓȾJDɯѭ',
                                        'default_value': 'ә˞ıˈϝʵϾ҂ƺЊѯͶȄӝhȌɆǍϥϼƛƗj˺ҹ\x9eƊɩ2ҕ',
                                    },
                            {
                                        'key': ';Кïʗ˂ăўԔҹ0ɴԈѯΥōҶ¶҈ѣŧĶŎ5Ͷ҅ԏͶС˕Ď',
                                        'description': 'ΟƀЁˏƝDӠӜӤŲӨƍĄΌǈӵҁ\x98ÏʳȠǾʯ)ȺɳɠΔәæ',
                                        'default_value': 'ϫӶϵыUԩƴι҄_˫ǸЦ͵6gˤËƴĻёҰҰAąϿэ˳Ҭƺ',
                                    },
                            {
                                        'key': 'Ηɜϣǁ˕Ўƞɾ˰àżîTʈ˛ĢԃœѻΕʸӺ\x93ɜϟȼѫіȻҿ',
                                        'description': '˥Ȇ¡ɩÁșɓ˻ľȂҟΩ¿ƃч|ǵǑ\x95ԕҋʽɧȍ\x98ƕҵАԔӚ',
                                        'default_value': 'ϚїȶΝ:ˀĄć&ƼǠӉFȸӌӷŸƢԓȞĭčƙIʡϣ"C<ȿ',
                                    },
                            {
                                        'key': 'ɡúEǴ¶ƏѓԞŁƎʘɶÙʱ\x9aϴǶÎЋԜäХΎɋ"ӶÈàȾ҃',
                                        'description': 'ɑɍ\xa0ĵӊŒŒ®¦ͻâϥΠŒȪӲĠťĄǉáęƖͱñ˕Ů·ǞΖ',
                                        'default_value': 'φҚδƫ˗ζɮԋˇėƊҟ#ěBǛƭːȧKӑűwǴvÝǏ,ëӼ',
                                    },
                            {
                                        'key': 'Ȅʶɀϳϻϛ˃óȚѬҏˉұԛͿԋaÕȺʕхі\x8fŎƣȝƠŧʛͼ',
                                        'description': '©ԉá҅ɸƇӏ˵˛ĠMŬƅʈƦɵѰԄԘ²ԬсBʽʦƶźȬŰî',
                                        'default_value': 'ϊ#ǍʅýȟһǽҭŃĠҩŽ϶ˤ˫яȫ˅Ƶ\x80ɟȿоιǢǁ҅Ƕʭ',
                                    },
                            {
                                        'key': 'лìŨƁf$Ǧɫ;Ƶ±}ӾőѕɝȿìǎԁΧ˝òģȿɬ',
                                        'description': 'ı\x8eǸιлÆɁűâ˜ǛǊŶÞʅѕ҅ЃйγɩĳįӜ˷ѕƒʍ\x8bϿ',
                                        'default_value': 'yȳʹŷƄԥŹǼo-ήМʧOžԭľѷτĥĥTѐ¸Ӵ\x88@íŒ˽',
                                    },
                            {
                                        'key': 'ЎсϙɢКǋ\x8cӘˊӍ\u038dͽӦšсҤ(șNϥǆ«ɑĆƨӹfäũҳ',
                                        'description': 'ѮΙŶɠƙȑ˖ʾӪǀH%ƥʻ¶ƉъĨǕ\u0380ȞƒŠȓӇ»ϐҥШx',
                                        'default_value': 'ªԖο˰ɀԨɦıҘȫɠ:ʍ\x92щʚȜǉӏšƷťƚи|ʔƋʸͽϽ',
                                    },
                            {
                                        'key': 'ƫýϞӤӦ\x7f¿˶ʴАʓǪ\x97җəǝѷҰϒ',
                                        'description': 'ӈķųĒȍÛ˔ǦˁЩҺƇˊҜ˗ΕӟʠŘ÷ɋƎ¼ԓ\xa0үɞL\x96/',
                                        'default_value': 'ɠ˩йѪǲũȝȠɷуȹ\x9fώ˸Ļʅ˴ψƵȲҭΪǜԧçˇfюҢѡ',
                                    },
                            {
                                        'key': 'ĀрǒӪɵƦ\x90',
                                        'description': 'ōÈ2ʺŮ\u038bƢAӬҺòèнλƟđɞȱÓ\x90Ӷτ\xadϬµ΄ȸΓĘԗ',
                                        'default_value': '/ŁHZЙĝƓЁɾ˯ʖ\x81Ұдœҷҩ\u038dжʿӮӵЩŋ!ɰϼҽUʩ',
                                    },
                        ],
                },
                {
                    'name': 'ʾԆϥǬҍ\u0381ϗӦɗԧȲԗξȿƷȕGΔɧλtəԦEŢľ²Ӏɟϟ',
                    'description': 'ʂĻƥǝѻζȧŜԤ˒ǥɳÉə\x9d҇8ǅǶwξɮҬДΪԦˀкиǖ',
                    'target_id': 'ʰ¢`ЄːNӛӉўğӳǂәӎǗ!ҒŪʵ\x88ɚӜʱ\x7fjĀĭ/\x9dȵ',
                    'parameters': [
                            {
                                        'key': 'ԄӤʤҨԤ˩\x94ӽWŐơƺƲНҭĖιɀŧʒĶüԅę˒ԈȖĊϻӔ',
                                        'description': 'ә"ҍ.ϐƈҗƱћȦӟӗȨǆŇ˹Б\x83ӃɥǚɪĈҀ§ʉӛЌNт',
                                        'default_value': 'е4EϠӰΫĳŅƚŘʥϿȀтʇūǩ_mǻͰҖǧʥԭĬƹɛȲҲ',
                                    },
                            {
                                        'key': 'ӇpǦӸƏʛ·ʦԖòѕ%ɻǣєԇˬɗѸƘηŒɭԃЉӒԋnǇʽ',
                                        'description': '˷эǪʩɶéȄĚτȝʸÛъҥāńǀɺȬĥԭÞŀӣ˷\x92}ʫɚѕ',
                                        'default_value': '¡ѳmɢԏ¸ƒӸҰ˞ΚmǝŮ]ϱſ˥\x8dƭʒÔˤjӶќԀ˪К˳',
                                    },
                            {
                                        'key': 'ъƕΨƉ˂˄ˆʫˉɩiѧϷϑƛğĖ¦ӦːΜȄõȂѕкʘƅєБ',
                                        'description': 'жѫɑϵ˭ʧΓˢυɼҮϨΘӢ҅˧ǂҺǅʥjɊƍԭәԈɬχӚɆ',
                                        'default_value': 'ԅ¬ɳˉΙŭ˺ͳˢҝȳť\x9aӪoόƛͷγƖĿҕɁѕƯйV\x9f\x8cà',
                                    },
                            {
                                        'key': 'ĪД˙Ơǥʸ8ԤđϵюʧҺъ,ƣѠʄmϺȖˈŇӍԘȴ\x9aġɐԜ',
                                        'description': 'Ҏӗҟ{Jȝԁ\x83ѲŝϹʠЃƓТԎ˫ԒВņFǩÁͻ\x93TɏÛÅү',
                                        'default_value': 'ʇϦɴӴəÍϕНԏǏŧҳƱʷѶӚ˃ϧљMƈqÄɥɩøҷÑAҕ',
                                    },
                            {
                                        'key': 'ĐϞγӫȽϻWӷ1ҷљċ',
                                        'description': 'ˇʃżıОӡѭċϞǾǞԐ\x9fξӱѣϱ˒ǴΕƩˤɖďΙԛϼѣĴ˪',
                                        'default_value': 'ԭϔʺƏũ\x84ƱGDωį·GĆȪŻ*ϭʾ˂µ ɤҷjҤԑÏʳξ',
                                    },
                            {
                                        'key': 'ӄ.ΎȜƲȪҏǲСвαƺƇǂ¥ǃǴдӔƋͽǩǡ(ĪӢ',
                                        'description': 'ØυѸƏʝȎτ˒ń~ĕϤŁ˾ОҤљɄ\x87ҫѬȝ*Ư˪ʬξʻԕӅ',
                                        'default_value': 'ўԘѽξŧ˄έкĄũȭǕ+ѵЪҾҾɌνȭăǌŉTЭˮӉͶƵƆ',
                                    },
                            {
                                        'key': 'ѳɌѯưEƂҸǳ\x80ōǿϢ',
                                        'description': 'ƛЛЊӕ¿ĘԕӳƪҪЂћɖʅËɗvǢїЄƟʖцˀɈŻČѧϵɯ',
                                        'default_value': '˳Ɲ\x9cʏǜƹo\x8dFʇƮȫ˛>ǧЋɥ\x89ҊԘфƮîӅ:Ƨрłĸų',
                                    },
                            {
                                        'key': 'Һ;ʶϻͰŖɞ\u038bϪɻĚ҂kѵȄЊɅҺӸŮ҈ʭΚwҟÝǕǑŜ¿',
                                        'description': 'ǣLͼԋĈҬũ˼Бˏý˘͵ΙϴΠƐș҅ȵцˍfʱӤНϯоӠμ',
                                        'default_value': 'Ģɏʞʣ\x88Ĺξϗſ8ʗĤrQ\x96ҌŢ®ˍʢӽ΅Ã¬ˆХåǡҥҬ',
                                    },
                            {
                                        'key': 'ʇĐ^Cԋ͵ǸpƻɜӤXƻγͻН\xa0ĖJʎ\x8aһȨΤΉƱѩŻĈɴ',
                                        'description': 'ʀǋѡОǮϡʢ5cЯЏԔ˥еͿȱԙʯŴɄҚҸãӘ|ǋwφúȌ',
                                        'default_value': '}"ϟôєԨҍƪgȕƾƂϤŲϮϢȤpĪưԑɵˣҫȄҡҋЫųβ',
                                    },
                            {
                                        'key': 'γɓɜ\x96ŒɇѧёѸɩéəÉϵö|Ѩơ\x84\x80҃ԘҎɐс ʱȁǵљ',
                                        'description': 'ʝȠѿԌˌĸѼ¸ӷȳŝӻȔˮ%У\x92Ūμ¾ƥǏϵӐχһ˙êˍĄ',
                                        'default_value': 'Κ!ҀĤӪňɢ˦ѳqžJȁ϶ØТƶįҐVǺԋь¯ʀ\x90ȼе˅Ӗ',
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
