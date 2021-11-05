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
            'key': 'ІƖʍіo˨ϾŇʩӝɯӤЬȜΞǥԧӮ·τ^»ҤсʋēxԁcͶ',
            'value': 'KMЛÁþïȹѴҸѫˬʻҔ¦ɈϷͿї˵ϵɨ?bŭÞЯɮɜæɗ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'щ',

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
            'target_id': 'Ëɱ«[бǍÍRīȪȩїϵʆϋȶǬĈǼĤͿԪǯЧԋцhȢҦǠ',
            'parameters': [
                {
                    'key': 'þ9\x97БΚÒϵțņƙʙȅԉԀдļǮѡǠɟȮƣԗʤɘѪYѝҔӜ',
                    'value': 'иΛҽ"Μë\x83ș҈ЫðɛҊӦ˓G2ĽƼČ±¦˅ѴȂċǕɻоÛ',
                },
                {
                    'key': 'ưˢұ/ɴόїхǗɽΓԧƆҥ(ɯϚвƤsγҹğäԄňǰΕĊҼ',
                    'value': '˲ʚiһƜ3\x82ˇǽӡӓͽǮȀʥƺÛ÷ɋқöοğя\xa0ǥɷõƪĺ',
                },
                {
                    'key': "ȧȪİАʱҶɝí˸Шʹɭ\x8aˆЭǶԡƁĿӧцƂǾzƃŠ'ӉԈЋ",
                    'value': 'ԚʉСҒϼÞ˛ʽư˚čÅԢԤ҆ΦҺɱϜ\x94±qӤ?ǬɶςԬйʤ',
                },
                {
                    'key': 'ŋҋ',
                    'value': 'ԡҔWŇȾiԁǉдǄҸҧŪԤοŒӐ¡PӑҫԈƍĢԠ(ǡǵ˲\x90',
                },
                {
                    'key': 'Ϗ\x87ǏɞʞʖԗԩȫÐțӈȨ6пЉfӶ\u0381ƔΚӕϡϔƦůӬѮUҰ',
                    'value': 'Ǽǂ˨±ʹJҢɥϢɭэǭʨʗҊ\x90ӐΠȒϨҺϡԖηʜӎ;ҏԉˢ',
                },
                {
                    'key': 'ΰǶ÷μŬɎȲԜӂ˓ҩʜϣѧҚһʣҿʖ\x9aԀ4\x8f§Јԏ҅\x92˻Ӯ',
                    'value': 'ϸ\u0382Ͼɼpɖćи,ơˉǾĢӭҸǗeҩұțϖǇ\x99б0ІʱŊQ˷',
                },
                {
                    'key': 'YÒёИç·Ũ˫ɇʍǥÀSĊęӀѝƀȌũÄӠþȥŸȈ}\u0379Ү´',
                    'value': 'ʯĀţԩɟƵÅΦBѾåѿʮɽӛԐҙƿ«ѵϦĳKԒîĀӋϒ˜h',
                },
                {
                    'key': 'ӏ\x98ǾԆʙɯҫWɔ΅Ǣǜƭ@ҿфŊεʘ¸ԗф¡ʅtԌϤǫҝЦ',
                    'value': 'ИɤǧɲԂǎҬΙϱԩɞ΄ȡџʳ\x98āɴĲĚΗʉτ',
                },
                {
                    'key': 'ɥBŮӷӱΟɥǖΕ!ƓƍŎŪ±ӯfǗи˒ȟƮԨϴˮăӆϦϺс',
                    'value': 'nԪğÀʐȨˬϩљ˚ɴƂXƀʆԁʑūҾŽҁûҗµĨÄvŌϧʺ',
                },
                {
                    'key': 'ƣʰõƑӑȭŢƏÇƑʫɪѹΊȱӼƝŜηŊΎƃӠ^ǰФНϥȾԠ',
                    'value': 'ԌȎɊłɝ\u038bщͳƋƫVƣ6ɶљ¼ҦŠ҇цgɥѽÜΓ͵Σĩʠό',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ȆE϶Ѱʉ',

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
                '_',
                'm.вƀņǏȿӗԤ\x97!ưϓŰ',
                'ύѨΛÿțӫƗйӲɉÑĞ҅ǘɢ\x81',
                'ԝɞӼϹŗҙ5ĦƔñ\u038dԕԏӛѦ',
            ],
            'event': {
                'target_id': 'ɉӆȹķЎǺ˖fb+ӣӠôӏ¸ǀұӒԋǌĶž,ƿϝηӦǼå¬',
                'parameters': [
                    {
                            'key': 'ſʒһvÔӤʙЋÝ˒Ǩ¹ˈUЁǯμŷȐ',
                            'value': 'ЌЕкƣ˦\u0383ÃƲУ˱1Ǚ˾ǡЍƈˁʼ\x96+ǧǉŻдċȉњȓǴÙ',
                        },
                    {
                            'key': 'ЛЙʳЂϗҙɞȻǲaƼϔΐɜͳϴǦӽ¢ӗȧӛƙŰDi!ǒϔˇ',
                            'value': 'ίĢƗƗϏ˸љƴҚҊϱМϼӢʉȸ¤ȱԔńJƼ[Ԉ\x95ΉĀțīƎ',
                        },
                    {
                            'key': 'NƒÓѯƹǷʛłνˍɥ%ĳŊӀλ9ќþҤȬξʎѳԍϮʓҒҌɷ',
                            'value': 'ϝêШҲӉƄӭ\x80˕ǓnФˑų\x9dʈˎ\x9fѫaщ˅ǍȌǅбԍω»Ǘ',
                        },
                    {
                            'key': 'ӯɤšǴʠƈőӶʧά$ƌʸYÊTƛƘѹӨϛȿʊâƊȷ\x87Ӈ˦Ƕ',
                            'value': 'ρcЎɃȩʶȶж˩иŌ\x85θ\x90Μь#ƋǽɦԙΤȊʏ\x94҉˧Ʌʹˤ',
                        },
                    {
                            'key': 'ħ?Đ\x8cʦΘȰóÿЫʷCЂĉͿƉǫщěŦӷũǬÿįȎȷj˳ӓ',
                            'value': 'ϠфѕĭíҕҏΘó\x8fåƉԊӰƆГѪΧǇэȰчψц¥ΈŊаʼӲ',
                        },
                    {
                            'key': 'ӳr0јǊñԚΣ.ňϯԜҎæƵԀӴĭûÃbΫтìøѸj\x98ǗȢ',
                            'value': 'ʨЩφ˫ϫ\x9cʏƂŤːȫēМΨɩʚЁɂ^ͷҺӜҴӯÅӹҢ˫ҫ¡',
                        },
                    {
                            'key': 'ѝǛʙμ˻ˉʾɔђҚр5ǬЮƴһѩ#ǧɟҴ',
                            'value': "¿Ƴ&з҇ҀȒƒWɨσɹ\x82˖\u0383ŋӥϾӔ˚҂ȻʒΌβΖӀ˄'Ȟ",
                        },
                    {
                            'key': 'ƳϗӟӻșäźƴɍĴvĆƹȺԁgҎοɾʶȘ\x8aаѷƲѧԢĪͳѓ',
                            'value': 'ɓЇʀ\x82ŶΊϾȣȨ³>ƣ\x9e\x7fΉƷͽĕʖˎƜƍŚÐʩуϝӫŢЋ',
                        },
                    {
                            'key': 'ȆĨƊҨͻϾдĩĸӦșԠʚҏҘ\x92үUɩȫ\u038d˕˙ђ\u0383˧ӌѱōΑ',
                            'value': '˾аѹӺkŻҖγѼβʶθѱӵûƶǶƯҞǈҶöєĮ˶ѽkĶ˨Ӯ',
                        },
                    {
                            'key': 'ŸѱҌÒʃɋΏ˶ЉӄĸȤęϨǘƸųˏӴ˅ʼЉӱȅϧӔЁǈEǣ',
                            'value': 'ǗϋɫĈ`ʛҀɦƚcƴƨΨjҢϵПΧ\xa0ʽŅπǹɦΫŖîDǢϐ',
                        },
                ],
            },
            'comment': 'ŽƖʝɒɤĳ:кЖʕιɌНϼŅόƫƇͳʁҺæϴ¢ȁėɋrα\u03a2',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ƻ',
            ],

            'event': {
                'target_id': '¹ǘЃͲƆ',
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
                'Ëч¯ԚƜˑκҏ',
                'Ⱦ˦ϭԆҨ˙,ΞÂéɋɐ',
                '\x93ĄǷMǀĚȨ˄˵Ƴ˦õ×ΑɶԊӂĝĿŻιϭɴϥú',
                'ǊƇӾҞ˚N§˩Ɣ˂',
                "dϽεˍΚc'Ј",
                'ÇϤ:Ѧ§Е;ҜӐƹфʍŇÎĎҮK¦ҎŨʸ\x96',
                '¹ŉkȆǻɊȿǹŜ',
                'ÍľƉэª*ƑþԛԉθŅПɓĈ',
                'ŲҴϪ\x8bҌ҆ѬΆƪɆԒÝǇϹϠƱȁԗ',
                'ȂϚ\xad\x7fӑʻ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ϘȚ>ǊʺχȩłÞƭȴjʉȆÓӫˡɨȹԟϪΎ',
                            'ʜvMԚϝǿŢ7Ԭ',
                            'ƨԂʅҁΆřРǔǓőÚџ˄',
                            'ɺ\x9cҢȽ˘ƾǙ\x86ŗƆźĢ\x82СҀĕ',
                        ],
                    'event': {
                            'target_id': 'Ʌ@ʵӯ½īΙƟӒ˔φ(ӭĦʾ¸Ţɲԇ\x8fѶâǙÜΉΆȐοиг',
                            'parameters': [
                                        {
                                                        'key': 'ʲ˱ǮηƎʜǤ®ыŪϯϢϭҔ3ͰюϺƥɜŀwԧСӀѝϒǓĒĜ',
                                                        'value': 'łʼ%Ԕ҉ϳ:ƔЩȚӸuƛɀÀȡđρÍѴɋɉǜǕӠŃԗҀȁǛ',
                                                    },
                                        {
                                                        'key': 'Ǧ¡ʒҐʷʔyX·Ö͵ǲѨӉƪΒʭŠŏǺԃȤЂƂÀȚɊΗƽˤ',
                                                        'value': '«\u0379ѩ0ҬŵҚě¨\x94ʨѳΎΪʴ\x8dÃѬȾҗӦήƔСҮ\x9aȿҿĬä',
                                                    },
                                        {
                                                        'key': 'Ͷþǲʒ\u0380ϳ\x99_ʖο\x8fȻŵϔŮƓć˚ɽЂȟƕʵφҼ%ʫ,ҞѠ',
                                                        'value': 'қȃɾώƤŢ¿ϑƲҒ8ƁҝΦεѓԃʖҬƳƇÃȃԉɱēɑ0ѹç',
                                                    },
                                        {
                                                        'key': 'Ӗ˩šӥpϊ҅НƸüϰÛкϰ˥ʰΟǓơ\x9bÖФ%ЁσӲʀєɺН',
                                                        'value': 'ȯƵρÞϙ˘ӎ\u0379ĻțϋYŀˎȡЃУȨƸĬҶɣи˕ǟӇφϥ7ś',
                                                    },
                                        {
                                                        'key': 'Ɍ˱õЮґҨȌӴэrɍi\u0381σĲÿƔΜɚη˗5aŬ¸ǣüɪ˲ï',
                                                        'value': 'Ɏɏ˰ΰƅɀ{ԜȚÐ1ɞϑ˗λͽˏΈǹƥңJΆJXɚʠΚȑΕ',
                                                    },
                                        {
                                                        'key': 'ӓ\x99ƳΫɎ˅ɚǣ\u03a2ʿ˷ȯ˶ƒȕųɯʇīˌƝϲpČŤʛƳҠЛЖ',
                                                        'value': 'ӧύγʼƛƨǢŦOƴ˰ȼßʀǃԈɟÒҌ\x87ˮŃɱ®Ԑϱ͵ΫxϜ',
                                                    },
                                        {
                                                        'key': 'ʤ»ϽяѤ',
                                                        'value': 'ʋҬ^Ǎϕø\x89ȊϠҟӇEȟƺřԂʷȇǏθz\x8eŹдҌŕñΪћǿ',
                                                    },
                                        {
                                                        'key': '@ӲɪҕŊϞxĴ\u0381ąӒϙ\x84ǫͽΉCʬǰ%bº?ÂѾƇŦŕӗ',
                                                        'value': 'ωɀşΠőԟţȶƳʄǔϥҧŧ˖jѯϴrĴȐǏɟʜҽԃӠå*ʩ',
                                                    },
                                        {
                                                        'key': '=Ӆ;ˀʻ˪μÐǚҔʈ',
                                                        'value': 'ϾƖʢɖˠωˊÐψɫ\u0383ӡʉĒŤů˯ɅΐŻŨ\x7fӖтĴқȓ=Đȇ',
                                                    },
                                        {
                                                        'key': 'ǰ1ЕʠҏĽѼĪ\x98\x92ȨŁ®ԉ˝ĜлƖҷ½¸ʖÀXȑ»ȒϞ',
                                                        'value': 'ȖɱԈУͳшŰш˶ѰʐǏϛƯҨˠĔԭЉŶҀƚ˰µСӔˡȠЀj',
                                                    },
                                    ],
                        },
                    'comment': 'ǺÃǓ\xadȹȂùƔŷ˖üͲŴȐуhʆŅɔ\x8bǜҮјϋҖϖΤ\x83Aӑ',
                },
                {
                    'keys': [
                            'sµɆ\x9cӊǥƯǰϐĄΪ}ηǴ˫ŻмʀӡƿVΓ)қдϠҿ',
                            'ϺǁԚ˧qԝƥγήͿf˧\x87ŭӦˠȣĖрŞОԥȑıѭѩʙD',
                            'ǴҀӡǅʹΡʊ~˰Ɨţǣðғƨ',
                            '҃ĺБƺćӂӠȊ˨\x91ґ',
                            'ЖŎǧϼǠ:?ĉʵрȥŊƁ¤pΠýԐΫцë',
                            'ЕžќƂʧǍM',
                            '˚ˈȉɛˣĩŐҴƧɘ˾ХԉԣȇȺˊĨѐ',
                            'ƪҖ',
                            'ʨǔЇēєѨяфϛn',
                            '˳ƶNčҨǢҿСϴĿˢ',
                        ],
                    'event': {
                            'target_id': 'ԃӡǿνőʎƻɵʷѵȈѴ>ǘÛШŁ˄#ӗиҿÂʃԊʓķ\u038dϽε',
                            'parameters': [
                                        {
                                                        'key': 'ʌȶ\x8aåеȊҵʤ7½ÉԢȖɨ|¿ΡʢӹЍ[ˡĄΈқυǇ',
                                                        'value': 'ŊѪσӖʈƍϤĞ\x92ʣźʎ0˝sзǳʱƸ\x9bɦ\x8dфјħwϪÞξѦ',
                                                    },
                                        {
                                                        'key': 'hɻʚũҜ0ѷ!dңŢˢʳæ˃ӱǩȬƎΪѴӲУϠҴâǬ!˧ʆ',
                                                        'value': 'ʥȢ˖ШӋѯȟƼѰǖΜȦ1ι¿ϲ\x9d(ĵԘԘћƖƗƬĺΣҝϧ¥',
                                                    },
                                        {
                                                        'key': 'ԖҌԅȧΆюѦÅÛӖʩϫӬ?ʮĜȷрęтРɾνõʭρҼϭч·',
                                                        'value': 'ȯКʮɹǼʮĥђ\x87ġʝĬԋϼĹɀԬǻΟ\x91ԕϴʈoӿɌюɞ˩á',
                                                    },
                                        {
                                                        'key': 'ʈq\x93҄Џ´.%эħΕӵÇȹɭʙ¥Β\\Șπȃ҃ʦɮ',
                                                        'value': 'Ǵ¤ĎЉưίˉЅɣҤϗŃ\x93͵ҏ˽ȑȠc˰˦ʈò@ҚʽȭƽSα',
                                                    },
                                        {
                                                        'key': '\x87оĖ˨\x9fġѶԘӀŁʮ\x8dȼϸÂ3r\x8eδá|ˑ-ȟϊьҾԐԉ˗',
                                                        'value': 'ŚhķǊZī˴ɲҿɔΑƢҐͺĭʙ«/äGɁӢȑȹӛЬƫЙ\u0379Ӱ',
                                                    },
                                        {
                                                        'key': 'ªͽʁζȺϝ˚ԃӺbX¹ʽËÚӼԚEʨ',
                                                        'value': 'νЩȢԖěƅǜ\x9eȜ҄\x94ϨʁÕЌƎŹŶƯѿ҆¦ÆȤǡȟŠӞ¿Ʃ',
                                                    },
                                        {
                                                        'key': 'ШĐΑІƳʿȾӟƉσɜ5Ѿң\x93ȹϛіŽͻϙʃȁ',
                                                        'value': 'JƤӭȓ\x93ʣμĈ¾ˑŷŏUϙɭɆįɯVϸϯɐӈüёīЮtΪš',
                                                    },
                                        {
                                                        'key': 'ҽӴǃԮƿyк͵ҾɊғȄǡΩѬΦ)řÊ~Řc¿ŅǊŹ~ɮĂχ',
                                                        'value': 'εȕԖǼ҇8ϡ\x9dӋǪО\x9e·ЍʑԊÃā΅hǝûŖeťȎƚҫŇҎ',
                                                    },
                                        {
                                                        'key': '˟Fбѻ',
                                                        'value': 'ÓöхWĵȄϵǔҼǻ\x95ΑӎĨǋԓțӔğȈѽύǁƾϣǐZОƛӞ',
                                                    },
                                        {
                                                        'key': '$˃ӫҬȥщѨɮԥΪϏƻʼʰˎхэϒӆι-ЙŒŚ˩Ͻ\u0381АȀģ',
                                                        'value': '%\x98Κ\x81ѠήϷ\x93ŅǙϔϋЉǁrԀӭǐGǝԪKʕϜԏǻȆЈˈȷ',
                                                    },
                                    ],
                        },
                    'comment': 'ϏОŗĉɶǹшD˹ʒԪÔƎƳƨȿĘŊʣȹ˴ѨʕʁʙѳĄ˥ĦԚ',
                },
                {
                    'keys': [
                            'ϨӣԀĚήfJξ?άђӂԎ\x87ѣʃȨ˯ȋëϤʐҺóкŪ',
                            'ZĆ¸Љŧǎ:ʬǞ',
                            'ͻе\x86ʜĳпԓɬЫӄϐȡêƻӖ,ȢŢџyƐÿ',
                            'DΚǰǂŮχѬӿEhƵτǩƷqұG\x91Єe',
                            'ʀ\xa0ɊĚˌӉq\x90¯ûϼ',
                            'ĎѾ\x87±\x8fďǗ\x8cлÁˡȯҲʨvЗʑ',
                            'ρьɈ˔ţ¼ǼҷGЕȢ˱ԘƋƆ¶ŞƖŊ¹Ȃр¾Èѡѐ\x9cҜǥ',
                            'әƩ\u0379VTԚҵfƐӦ;ʋϮѼɗҶȊŠɶāԐȳϹŬ˼',
                            'ɞ',
                            'ƝγЧ˝>ԁӺԄúɫáӘўтюӇɹýз',
                        ],
                    'event': {
                            'target_id': 'ϢԀФSɹ¼ЏšıӋӍ˕ġȈɖǃŒƬƵĺҙЖȷˉ\x9aѡϱʨÎӉ',
                            'parameters': [
                                        {
                                                        'key': 'ΐ\u0383˷ÓĻӮȹѰԍ˫ҡšӘԁ\xa0Ζ˝\x80Ů^оҗ҄vԔ˴ӶǶӔӤ',
                                                        'value': 'Ƕ\u0383Ԥ҇VӚ·ŔÌ;\x7fҩХƤÌ\x86ÎŧήϴӰϫіѯһʁҙӂеΑ',
                                                    },
                                        {
                                                        'key': 'ѵʜѓǀƅʀаĤҼɛ±JʲɬӺ\u0382ѶϹųʸ[ӥƥɢЧӱEӋµȶ',
                                                        'value': 'һϧĐϩǨǊʱÞʰњϾͶӢ²ϚЯƹȞǿǉԒŋέÙ˺ɐ˲˰ҋŘ',
                                                    },
                                        {
                                                        'key': '\x8aҡǢǸˣҘØԒɝƀ#β,ԩĦ.мƀƲØǈԊшŞʘҀhБÎƿ',
                                                        'value': 'ԉԉȓηÃŸƖâλɳЄ¯ѳȟшȫңǁĥțжʳϺЄēć³˝ĜĘ',
                                                    },
                                        {
                                                        'key': 'ǻǋ\x8a\x90ȋ;϶Уˊ4ԝÑGɦҝƙņЖ@ƦѢϭȨ¥ʫ·Ȕ',
                                                        'value': '#ҼҢȨǎ\x9fού\x81ƭџČԞͱϽŅώcаԀʊӞûɼϩĒғөȥЁ',
                                                    },
                                        {
                                                        'key': 'ΊӗοFԫɄ˽j',
                                                        'value': 'Ҝ;ːàΆêǼĠ˙ČӼˀϴĿȵǄɗͳъҹϢĖ˻ҷΝðӍѱеƣ',
                                                    },
                                        {
                                                        'key': 'ԏŏŴċ¬_ǓθɌȢÃāΣƐȚˌѸȒƃƚҴʿэРʹǯȓԗȭѐ',
                                                        'value': 'ƒ\x96ԎНŇŞɽȰӣƘΆǫǓˬőè˟ȪŕӈѐͰơЖĝίŦҷɀ҂',
                                                    },
                                        {
                                                        'key': 'МѨ»ǳѰ>\x94υģӑʟҙԌ*ʠʖƁϢ%ɞ΅ÂȪ\x97ȕĝԮŋŬГ',
                                                        'value': 'ƍӳ˜ϑȆéѯ,ǇǏє·Ϟԣų˨ϕº\x8cƎ(αS\x91ϲ\x91Ƥ$Ԥϼ',
                                                    },
                                        {
                                                        'key': 'ƈ¼χɡÛʓȆϤȾʄƙΚƎ˽9\x84˭Ν΄ͶȘǶΙӀΉȨрUĕ&',
                                                        'value': 'ӳ£Kσ\x93ǤЕ±Š˱ŠіЮЀүÌ}ЙǎŌ\x9cʶ#ãǗ\x8bЌӗrș',
                                                    },
                                        {
                                                        'key': 'Żʇ;ɐHΛɡ³ЏˊӓƐˏtгTϣ\u0378\x81ρϷχґüϨҴpņˏʈ',
                                                        'value': '҇OӛӠ˦ȮƩǠͱ˽ūӂɌ\x94ӵӹÔ)ӞɲɭƐ\x89ÿʾɁҞѫ¢ϸ',
                                                    },
                                        {
                                                        'key': '\x8fÃ@ʅ\u0383ǹϒҤjϋҏsɂǸ\x9eǃȿӮЕԓßӋΥϜҩΞҢ',
                                                        'value': 'ǗɻŭřʒħźƽҒŬȟсґǳκͰɺќȹYʐ˪ȢϖŞЇūɮѴҡ',
                                                    },
                                    ],
                        },
                    'comment': '˷ÛɃĄ\x9fh\x85ì˄ńѬŚ¯ģˣҺ¨ͳİ¡ÉÖNάǓŹ˜ƶԡŬ',
                },
                {
                    'keys': [
                            'ƼѾÞͰηИ5ɼ',
                            "'«^ȇŒҹʮŐШҺΦ,ӢŽ¾όѫȉϖϣȆΖјźľ¼",
                            'ΪҐɚŧŢ˚',
                            'ơɻҎľҝѭӸƏɜΗҎˀйО',
                            'Țǆ',
                            'ʪ˖ĦԩѸDϮ˱ŜԮЄԕҽ҉ϩ',
                            'RƕΐƯ',
                            'Ǫȸș',
                            'ƛҋӥʢŬ\u0379ɥĎȐεяԨǊΉԅlŚƔŲőďǹыǓ',
                            '˗ǇʷȑˮªÈѭΓЪřƒԌǵ?˔Ι҈Ȋӛѻƹϯѥ',
                        ],
                    'event': {
                            'target_id': 'Fӻĥʉ˾ҡćιʃ;ʂƐ×ːυσùǙӤÚѦб>ɦȏÎǯ±Ŕϊ',
                            'parameters': [
                                        {
                                                        'key': 'ӖДѠǥùÑ˫·ǍȭƅƫІʽФǽ\x9dèӈſ¸І\x9fмϬΪʹļԍι',
                                                        'value': 'ӰнȺˮȃԒҧĴÄһɇϡЪȓУrΨ˖ĳ˝ȫk˔åƶŀ\x8dūƤҏ',
                                                    },
                                        {
                                                        'key': 'ȁǝ¦ɦɒҦȴ',
                                                        'value': 'ȢT˟¤Рǎӫą˒ӟӊɕȳ\x83ɓƀƛʗǈƢӠrйD˞]ͺѫɻŌ',
                                                    },
                                        {
                                                        'key': "ϞҐҩτůҜӤ'ҦӈϽûƉIŊҿЗɠǶϯȄͲŚ£зӐŏɅӚɾ",
                                                        'value': '\u0379ԃПǓѝ8ˠ\x9fҎѲВƀļžęҩԗєгé˷юӘӪҦÙВӊ\x84¿',
                                                    },
                                        {
                                                        'key': 'ǒɢн«ŠǏʚ\x95θχ;ӷȰȋͽǩüЗÝXůȺȉ[\x83ȴЯ=͵Ԍ',
                                                        'value': 'ÂʾưɀƁPĈʣѿȽǒɖǆɼǼʸң:ĦĉИMăķФńѲǉҚҨ',
                                                    },
                                        {
                                                        'key': 'ԔѭȵȉҁȂДS(ȃ',
                                                        'value': 'ŗǗŦƦyчϾ¸ÐӡϼκȨǤǁɛљˢȱÞïϱϷ\x8aчΙʬʦĎ˻',
                                                    },
                                        {
                                                        'key': 'βśˆʢŻɐtǢɈʹͺϙɷ¾¯ԆҚƗЁÝǕȊȱ\x8bԇʭľȿėӕ',
                                                        'value': 'ѓʩțϻ%ιΫɰԄǺɈő\x82´ĎГĉԙćT\x91ІЧЩŌӕǾҡҀ\x8b',
                                                    },
                                        {
                                                        'key': 'ȪєԘ\x9b˼ɶΝӶǎƝϯӬԖŰӾώòĸüͲȟáĵʜɮǷ¶ɦμ',
                                                        'value': 'Ɉȿµɨȃ/țƗdσӇýБҫҢӣҞĐԗ.ԚɭéȾ\x83Ԥªď\x98ϟ',
                                                    },
                                        {
                                                        'key': 'ҤsЦȺȕѭǡϵȒǍ\x97БΥТſïȒǧpȟʄ҉ˌҷ=ʋõƿҮ˸',
                                                        'value': 'βȠŽƳԑϸǚϔл"ľǠӌƤьԣȐӳĦϧϦʹşӵφÚԐҗǹȋ',
                                                    },
                                        {
                                                        'key': 'ԅʩğδáʙҏѢϛƋЁрʐe˨˱΄ªƀŪѝŜǭяӷȢįϬӧȫ',
                                                        'value': 'H©ӭÛϥ8ÚƒƛНZǼɄÕ˞ˏČŇѭƇUǈ҇ƛΦɹǲɄĆC',
                                                    },
                                        {
                                                        'key': 'ʁԍĖƀӿ˳¾čɦŃԮǐ\u0382ҕʿȀ҂ҩćҨíýŪсІʢͰҔʢ1',
                                                        'value': '¹Ϸ¾ɡԝ|ȫΠБƂǩϞƸщȐϓЮ"ƵǈˑAŶ˼ЪŪǁš{ʥ',
                                                    },
                                    ],
                        },
                    'comment': 'Ť҅ԧԝɊ\\ĂȷĳѤҮјʷӾɧЮ|˛ԅˢ\x83ÚğǨÈӌʡʄ˯Ĉ',
                },
                {
                    'keys': [
                            'ˁ©ȧʪВ\u0383җœˆϟɊ¹IrǁŀӅʂ',
                            'īǙĔȼЯĭχŷӃРѹəțͼ',
                            'tʏĦӜ˯',
                            'ѽѮĭˣԝͼΰ҇мӷ',
                            'Āӱv˚Ѫä$ҠϿʣĘӟԊʠғ',
                            ';ыǔòҋϾƁőǖ\x83ĲӴĉģçЀ',
                            "ьʗk\x9bȀŖŅ'ĬιƄK½ĪDʮԡъǈԄϡџҿʄ",
                            'ɀ¤£ʫҬȀ\u0383ĦͶђÓŏȝѱûԚǾќσƋϱǫǶУƤ',
                            'ϠϢlļφʁάɒƼҕѩˋʌΐΝ˲šԟƶяĳȈӃŴȥ',
                            'ȿϠŮӢǙҋӑǐɫЗΪϰӇЃǯ=ѴԧKо½5ǷwϥɵŸ',
                        ],
                    'event': {
                            'target_id': '˚ԕ»ҕӃƠǻ˘ʕԓ,ÏȐŭɃƏѕъ[ƼȑɀƖŚ5˷īоȲХ',
                            'parameters': [
                                        {
                                                        'key': 'ҭēʨɯ˝\x90ĮɦǔƷ»ʜːYƊ\x80ÈŰžʣǣѣ\x80ë˯Ҩ˝ƕAο',
                                                        'value': 'ŒΧИÃvʷʪĶʧλЈυ;Ԉ¢ϒ\x9aӱԢӳ\x98πЉԡѩÑϝŦʥÊ',
                                                    },
                                        {
                                                        'key': 'ПŊöΫZнŹʯȠų^Ŋ§ҁƬДϔɠɢǋԥƏȖΔy=ӧӭÍӅ',
                                                        'value': '±ǢΒ³Ĳvɾ˩ɥ\x87ҺиѰʰɦΏòǳЋцφ¿ӀϡΗвǃF˭Τ',
                                                    },
                                        {
                                                        'key': 'į˥ӿŷč˼ѤωȎӈGϥȁǎ¨ɤЋ®ŇԂΥß˲Ž϶ŷԥӖЛɿ',
                                                        'value': 'mΤϐˀȨɀ\x90˭ɺΦŬȽϓѦ²¢ĥÎđãŹԕёɉҼhù»ǰȪ',
                                                    },
                                        {
                                                        'key': 'Ѣȓ҉ɖƿĐȭĎ',
                                                        'value': 'ͱ҇ѴĜΖŧĆXźԨ<ǇĿϠɉĵɋʙƍӯυԟǄˡGŒЍѴͺΡ',
                                                    },
                                        {
                                                        'key': 'ƆƴҌʮəҙҙŬΖҤȌòϧ\xa0ԮȲӻϝ¾łǢͰǏƛCԎ\u0382ϲȿͳ',
                                                        'value': 'ԥ˽ʱ͵ÜɄϿЋіǔńǮёƛőьȊƅǋƣҿҜқƅſƼƜ˨ǈʞ',
                                                    },
                                        {
                                                        'key': "őƷƫԑѰÈχŦȹʈǩɞʼФΓɨӾȆƘŤčҋƮέ\x9cҺ;.ӂ'",
                                                        'value': '<ÅʌĔНǸȑӉȮ˦Ơӧ]ϭġӷÐʰɖ(ƼéƓǄǶ9²öԙɝ',
                                                    },
                                        {
                                                        'key': 'ӿ´}ӦҬʪЁύɃӷNʢɀҐêŬÓƀѡӕγԩŭ',
                                                        'value': 'ўȀΏҁ˓ΝƾƤҲǷŨ@ˑĴãȅƚͻ9\x9dѰˈƱǁ˭ѢқϪͲã',
                                                    },
                                        {
                                                        'key': 'ö¸ԧǋƀϺ\x9c`ɾ$ϰƄφµԆöúљưʘűҟÔǱүԝωΐʾ¸',
                                                        'value': 'ɸ˰ʸɽӎŲЂƍΈŝэ7ɵԓūČȑΦɓǺɂ҃ĿϡѱʅɄĂʹď',
                                                    },
                                        {
                                                        'key': '҆οȞȐԉŪƄăҫҢƂȅΚљҌπ7ʭ˔ȄƐǔ\x88ɘʻĊАяþӜ',
                                                        'value': '2Ԏ҂Ě¼ӓǣŜʝȦ҇ΩўăΤȲĘҟ\xa0ʐοŸșƻѠҝǗπňö',
                                                    },
                                        {
                                                        'key': 'ǔя¦Ǥіşŀʹµĩχġˠ_ѬђáĽɌɕСˆ\x8bҼøԦӪуŞɁ',
                                                        'value': 'ɹǔĜľ\u0383ƪɦȠƷǍȈö\x82ЪҠиΠэϘΌƚůЕÎҩҖƚΰӍç',
                                                    },
                                    ],
                        },
                    'comment': 'ōӆԆȊȖҮҮɹңΈǠ¦źêÌƭ«ʸ§ЕMɧĴӸĒҷBËԣě',
                },
                {
                    'keys': [
                            'Ŷ\u03a2',
                            '¦ǵǷʋγĺѣҞԃл˻ǱͰȝƵRǴ',
                            'ȴѲϨTˈƵҧĭώÎÌˉ+ѣƿӸʆѕ9ΦȴӈɾŃƥ7',
                            'ǥѦğ˂Ʒɚӌê',
                            'ɜϐƏĎ<ґ¸Ӱ˷ȖʖŞƘъϛѕRΦхαɻѡ¨ȜǺ',
                            'Β˴҈ηĕbŞ\x7f¡ĂˑR҅ӉӤʭб¯dȧˈûǛÞҚΚćЇ',
                            'мΌϳɥțĒˌѦѡ`\x94ɭ}MÒΔϯԃǷH',
                            'БГĺ',
                            'XӏцÞ˲ϧДфÍǪž',
                            'ƳǺèƚĄǙʄǈÒà˜ųр˦Ĝ\x86þЇZīȦ˷ɭϻɸӛͽΡѕ',
                        ],
                    'event': {
                            'target_id': 'ӭϥҷr\u0378ʟȳ©\x9cдΌѬ',
                            'parameters': [
                                        {
                                                        'key': '1ΝϤЫɭÖþԞ\x95#HMϤǛʻǤʇҘΜńӔŮ\x8bÂ˥ėɌѝϙ\x9f',
                                                        'value': ']ԮѹZźҨƪӴÈȬЯӤҬƀˆo$ˁЏ˱Ϋӎͷ_ԙư\x80ӭėј',
                                                    },
                                        {
                                                        'key': '\x87MǠƘδґhͺ҉ǬѭӦǃȗ\u038bĀҒˀ¡ӾԑˊԓӸɴƐðŹѬ:',
                                                        'value': '~ĖƅÛɵ?ГЇτͺȄϒ@ƫЦҕƒʠϰÎʦѾϧƛϵӽƒǚϪѷ',
                                                    },
                                        {
                                                        'key': 'ɅΉЫҀΑ\x8fѿÊάĚΗ ȣ³˨ʇӡɠҧɲσʵȧкʘ÷ѨȤˋЮ',
                                                        'value': 'ɊɐŁɑƝҳӋĦɲΌ҇ϛƄ"ғ´ǆć\xadϮʝļʢшǭʪщΕЍw',
                                                    },
                                        {
                                                        'key': 'ΐҍӗʨт҅ǜӘ1Юά6ȸ˦ƷWҤ¢ͳΉɏ7ȏ\x8eӍ}ЈÂėԣ',
                                                        'value': 'ȫĀƉΞѴǫȀǭӮɿÚǴȄЩӐºɫВЧʖъ:ӾӅǦâʫʋӒ\x9d',
                                                    },
                                        {
                                                        'key': 'ϫѡО\x99ΕѷʶFӀҍΖƪ\x9cɢţΐƁύǀˆůȎˉŵ.ԕЯĉğʏ',
                                                        'value': "ϼШʱ·ϸǇєєЮǥǯӆƅÂʇļҎҊ\u0380ԉҞ'¾ɬȩԑʔϲ\x9dɔ",
                                                    },
                                        {
                                                        'key': 'ʈ\x9cQâ˷ҺȌƟгԩ+ӏǸΪԁҐ¶ЌӐģŧέҞΉ˪ŸͿŕǗά',
                                                        'value': 'āĺHϮӟŁϓΊΌ˧ӼěƧˉȥǮђҫM\x90˔ͺːŬ-ȢþΉĕā',
                                                    },
                                        {
                                                        'key': '@ӮƳʰ˂pĉïѿΉΣ˛ԁρΝĨтǔҖ˯ԣѭ¡)żƠqªæӪ',
                                                        'value': '\x97ĜfÎțƌĂÈʊӬɩц˾ŽĝÝ˼KһЋƹśτŭлɥʱďɢ.',
                                                    },
                                        {
                                                        'key': 'ňȮΥśȉˀoșʉʔÉҟҧˠ;ůƔʹʛĭʘƵ˨"ǮԘˣйǔĕ',
                                                        'value': 'ΖșǗ\x93ҠϽƂӔԩ˱ʷΓΥ҉˾ѕǝn¿ȁʋĞӼȦύēӬĬԅĔ',
                                                    },
                                        {
                                                        'key': 'ӀŐӬȼÞʹМ¹ˁË˷ԅҩ®ǉƮȉɢФΎɘ«æàÂʠҨŴºө',
                                                        'value': 'ˣϭΩˬĲӢ\x8cįǋѨʥÕ:ǥ"ĄƷ\u0379ʢƵȿǕѠ˜üÇԩàԩɫ',
                                                    },
                                        {
                                                        'key': 'ѩόӷăΏÔɒҾѭȴɸƶΔΕʨĺŨшąϯԁɫ˶ɩʢΟҾ\x90\u0380Ѣ',
                                                        'value': 'Ⱥ\x92ιыɨĊʹėƜ˖Ҁ:ɫɾɧ϶9ԙ\x86ūδİȞ>ǔѹѥͱѥx',
                                                    },
                                    ],
                        },
                    'comment': 'Ϛ\u038dɰʾQЧ£ǽӃѫҀϚ҃ûɁȆ4ϫҊːϐǓċήϏ\xa0Ɇ;ǒȡ',
                },
                {
                    'keys': [
                            'Ӕ4ȶɱŝѾЦ2˚ҖѨȱÔмþʗɇ&ǯNƭ˭\x84ċǟοʌ',
                            'ğʬȎƴǨɉǟŮĚµ¹Ӓ\x93kԜƍ',
                            'ҎƔӓ',
                            'ҘΤɑˑͱEM\x91˲ĵԌЍƲэdþɕʼϰϋłƌѬ·ͼҰ',
                            'KшǶàϓƔΥĨmʤfĥǫĹӀʑʫǣϤpΗʃƼÃǊƓԒýȞ',
                            'ѧȩӵ\x88ǣØӞķϵ',
                            'ϻʗѝɬÅʺ˝ύζĜҞ\x80TХ\x9fӁϛʊ',
                            '˻ȱҵȁǊΓɭԫCŢȃʌӌԡΰϭӾ²ʛԅԇФÃЖŋͺ҃ɄУ',
                            'ǫEƗϘʌɑʘ\x96î=ǰȺͷřѥŇǿ',
                            'ɓУŶ҉Ĭ',
                        ],
                    'event': {
                            'target_id': '҆γӑ˺çƃȩÓƳȸԙʖʎȩΙ¥ǔѧϩӾâƭŐԢʻÝӾЈыϜ',
                            'parameters': [
                                        {
                                                        'key': '^ƇŽҨƳӀHһêʉɱ ɲԈάʿ\x9dŅǭӢǫΦŶɉʕVɅÝɀԟ',
                                                        'value': '«ͻЌȰɆ¼ˇƭź\x849\\ˏȗϭ÷ϚɶÂʠƚ˯\x8cɾҺț;ҍ\x93r',
                                                    },
                                        {
                                                        'key': 'Јϳ˻ƆѬ¢ӶƜɖ$ˊä&ĔƱФӊҬȎͼβӑґȦÍԝƟ˅ǘȯ',
                                                        'value': '1ÃӽԃʡӲеʬȕʦ',
                                                    },
                                        {
                                                        'key': 'ǖdƻCѐҦʥʞУԊöˮƊʦŻˎŹÑέ˚ν˙ȓѠɓŖыčʡԉ',
                                                        'value': 'ҲΕԍđLԨʶ\xa0УóϳĒʉǍхǻŦйʹАƨǩȳǙÛƦѾɬӋ\xad',
                                                    },
                                        {
                                                        'key': 'Șοb@ĿʝѐȦΥƨԜѨǳ˂ӫțŌё_ӜӺƃŃʰğǀǥɇԅҎ',
                                                        'value': '˘T\x84Ԓұ\x86|ԖȋːůԂ¦ЖԬˑ϶Rċϴżʗ˸ʩΌ=šǲƆǉ',
                                                    },
                                    ],
                        },
                    'comment': 'ԖʌѤҎБƜВɿƥ§˙ȽЬԁũ\x87×˜ųŽÄͰÄuωmӉѺβӹ',
                },
                {
                    'keys': [
                            'ȬɆИǀƬLΪǬԜУťj',
                            '˓ÞƩƶ',
                            'Ӳɓӎïǜʡ·',
                            'ԝɃѡ[ŕ',
                            'ZŻЩƟƪ0ƛΩґÈÇ',
                            'ά˚Һнľѯ5ΎԍȽƤҲŨͻ',
                            'ЄԇНȒҐ',
                            '5ÌƿʚʊƆº7ӰҧÖȴ',
                            'ӎæĿИŰЌБǘΦ\\đԤQʷԏÒ˥ɺķūɷӏԁȮԣ\x94Ʋõ',
                            'ßϓΩŻĔ϶ҝˆθ˒X',
                        ],
                    'event': {
                            'target_id': 'ʳżбƿюƉѵ϶Сɷ\x95ЦȚфˆлΟ\x98ˍɺѳ˓ʹΗũΫƈȢʽʅ',
                            'parameters': [
                                        {
                                                        'key': 'Ҥʾ˛ѵӷƩþȏӣĐɔĤ\u0382ʖΒкÒF]ˈϼȤЊ×ˀÍҿ\x97˼F',
                                                        'value': 'ȇԬ˳¤ѰҾʾÈĿԊ³Ѝϱ˙CȉŘ҉ǯԝ/ӽȱƽǏVɦȣжј',
                                                    },
                                        {
                                                        'key': 'ŽƷΨЀιǘСҵѩώԞŗѭŷҎǧɚ͵ɎzuЎȯҒ»û7ȀѸģ',
                                                        'value': 'üƢҵaΔѴУ˳҃{¤ϲƼʥĊӯҎԜŹĒϔЎƱєʅͼʘлÎƭ',
                                                    },
                                        {
                                                        'key': 'ɉγ½µ',
                                                        'value': 'ōДǮȒäɋɌҿaΡõӼÔӕΖ3ǉ˔-ÌúӪɽʋ¥ʜ4ɭʤǾ',
                                                    },
                                        {
                                                        'key': 'łáȾӱgȵςƖ;żˆƙԆǨҌ\x99ˢǢƛ\x7fʖPԒ\x85Ļ<Ҍä҉Ϣ',
                                                        'value': 'ŁʖǥɈŮ·\x89Л\x98ԁʕҖ*ʚν{ӓΐcќȳѲѯǽћкȋ˝ʈӭ',
                                                    },
                                        {
                                                        'key': 'sϝǭŘҧсŏ\x91ʀ˥Ӵù˜ƍÕѤќ˫ҩˇźĥԮŃΫɠЭʺßӑ',
                                                        'value': 'ʜҦƂɂГɅҸӗҽ\x98Ѱɍļȑ)ӦAͽˑǻɀȗ˪ȧŨũƑÀœѨ',
                                                    },
                                        {
                                                        'key': 'ƇǕó\x8bƹƭƑȉɖћÃҍΩȒśӧĲʁҰĚąɚβπЛУӧӋӷ\u0383',
                                                        'value': 'ʗÙĕɛ\x85ĤǷКҋ\x8fʧ¾ǯ˙ӊΝΊ˲œɽ˥ηKðǧ»\x8d˕Ԣ˝',
                                                    },
                                        {
                                                        'key': 'ԈŲȁǶʪŘɌǆĜѨ}ț\x8eVԍѕƵǒŉ\x8aǊԘɛɮƄ\x86ȸϞłʝ',
                                                        'value': 'ďşϪψǦѽϘ.ӴƉȦIʍѵˮɆɪϣƍȬǐǷɡέ˅L\u0382ͼËӨ',
                                                    },
                                        {
                                                        'key': '\u0379',
                                                        'value': 'aşȨҢɌ"Іȋ5ȑ˼˧ǯĠǂʘŇęѵ\x81ŉ»šͱ¼ˑʏhϠ\u0378',
                                                    },
                                        {
                                                        'key': 'ԎˊŰӺɊϕӇʿ^łӺӂǣǰʂѲ͵AƭҎɾJ\x9aGɢ˝τğӣЊ',
                                                        'value': "ӸʲĶŐӛʉѩЫѕɀ~ưρǄȲşȢʝÎӴΞ҅˶ȉdΰʏɯ'ť",
                                                    },
                                        {
                                                        'key': 'ȷГ˻ӚÝЏӑԫʖ÷Ѝѡ+Вʏ¢ˬƠǷϬΨυÊΞю',
                                                        'value': 'ˇΑɯȑɪǅсЌ2ΑŦō:ȃҝ˸Ӏ\u0382ǇǌάЪȹȏÅι˝ʇȟȮ',
                                                    },
                                    ],
                        },
                    'comment': 'ȇŏвȥςцɄȈ˖ʩĎ϶ҏΜćˀҸҊàȍǍiȡԩǬπɇˏƩŖ',
                },
                {
                    'keys': [
                            'ŷƻ',
                            'ȨĿ\u03a2ϞѠйҡӏӶƜЕǐϜǁÆԐÁɭΤZѕ',
                            'ԇņзQ҂?\x7fűǮ\x9eÈJ>љ',
                            'ŨǘqҒЦӛſǇqθРƞǻŒО˞Ԛŉд5çɰ¬Łğ&ӣŲ',
                            '΅ԢʴNҟԗɃɎƵ#',
                            'ѭ\x9eɚɰN\u0378Í˛˟ɖàӅӖč|ŤШúĥԢӫj˳\x9fω0ʵϸԡ ',
                            'ƛэnįȆʑӪƽ\x90ʿѫόɸǐˢеѳõʏȞ˛eԆB',
                            'ћbȉǿĮЅъǾVĺѮЃŮЄͲҫ\x8dҕªɗ',
                            'ÿĊƪĩųԛD\x90ђ\xa0ҽƨх-;ρʟϞӣЖ~ұ;ˤΗŲ˰ҎϜ',
                            'ŠǈǨ˩öфL',
                        ],
                    'event': {
                            'target_id': 'ɌɗΚǭѷɘʮ˘ɑ·ӡΕϫãΚԬͰãɪʖοF΅\x8dԄӍГʚϪŽ',
                            'parameters': [
                                        {
                                                        'key': 'ԃƵ\xadȴɁЦƉˊε_ȭДǫΊ@wїɃʹΗԏԤӃɱîӂ˾қȮЄ',
                                                        'value': 'ǁæϪɻϦyȂ\x95ΰҺY\x8dЇѯԖʖ˸\u038bѦǪ®ВŢƷǶtħ5ÕϾ',
                                                    },
                                        {
                                                        'key': 'źȰсΑ\x94ҩϟȁƳϚʯЯӵϰŔǈŉМϘƅýψӍϻǸԉĪжůԁ',
                                                        'value': 'ŢňӕaƼԏƷ҄ġʔѺƮūśǔ\u0381ǅӴpҝƬǸɴ=ѠǏĨȍʄѫ',
                                                    },
                                        {
                                                        'key': 'Ȩϭқŕ=ÁĭΨԤРқўÈʚÆКϯ',
                                                        'value': 'ѧҗЬ±ԟɢњԢʮӛǄӶŔǢѺv8ƕͰʆЁĤ˵Ԣԁɶȟŵςψ',
                                                    },
                                        {
                                                        'key': 'ƓǍ±ĹȈ˷ѕ΄ʪśƀʝÂӔhʛИєŤɚӤ*СʪòЇúЇıœ',
                                                        'value': 'ͺΨÄρΜ;Ǣw\x9bc\x9cÎυӟʽmȨӾĻΊΰkŐͲiҖʐƪφϦ',
                                                    },
                                        {
                                                        'key': 'ͱȎɖʆğ{ϯҚ\x98ȡд˚ԨϪʜɴvԥρҴҙԣɔҞŢéхΐԈŷ',
                                                        'value': 'jͿʭ˧\\ƆũϾ˧ɩѼќɒ\x88ʛȫϢΑøҼȕ\x85Ę\x7fǵÈŀĨƝɛ',
                                                    },
                                        {
                                                        'key': 'ԁȂ˚ńɨӾˉëƨϬͼ\xa0ɟϷπж{øҤŝɑňȶR\u0381ҀŎƋԇ<',
                                                        'value': 'и¨ҝUȞӜϛĿԦ\x85КϘtȵӒe\x8dѻǱàğΉæϗȫιǳўѢǽ',
                                                    },
                                        {
                                                        'key': '\x9aćӢïԡѣ£ӎ¥Ӿ8ɂЊĝɣ$ȄvÆÀҤ\x9bɫƩԧːɓÛbЌ',
                                                        'value': 'ѪÈФŽЛԇшЮˡԐyγʮψҊʊȺӪʔЦƊ΅ÃӯÀ\x9cƛϘҺі',
                                                    },
                                        {
                                                        'key': 'ƶН҉ӒҳǓёǌϱҵ[ɝɅˍӀ\x9dЃԝ҈ЌЫʓƴƌʒԏɚфʹƙ',
                                                        'value': 'ԄĔeÇҼƧºˁӪгǅǋʪ!EŲ_ԇѣoɜͳӁʙѲ\x99ɴ˪ѣȁ',
                                                    },
                                        {
                                                        'key': 'άǑʲĂΠ',
                                                        'value': 'ʟȺǕӁŅѼͻʑĿdňǯǩӄXԉӮÁ˾œˮĔхЍ°ҢĂ˧ƍ˯',
                                                    },
                                        {
                                                        'key': '+ΣțʉŅЧ·0ϤŞѩ˝ʚʙÊ˘Сʓ˪ϥ?ŅıАҔƬ˙ӂȏä',
                                                        'value': 'ĒԚџЯ\x89ӧӢɈсlƷΣƩЌC\\Ɏż~ϭɭȡы¸ԪԎԭɸтЧ',
                                                    },
                                    ],
                        },
                    'comment': 'ήˋê˞ӏԥϱ҂Ѐßԩоʓт˦ŇgԢÂ%áØȡÈĊϞϮǓÑʏ',
                },
                {
                    'keys': [
                            'íӏ',
                            'ɵúĜƵʀαӻƾɨ҉įęЧɝ',
                            'ѣάϞԪХҏŔУ',
                            'ʒʩǐ0¿Ȳ8î>ѲɎΚ¿ΉǦоƥ',
                            'ϲΜҟϼɽĤ',
                            'Ɠʷ;ƴƵnϹѫӂͰЉҏ\u03a2Ӂ¶ΞŃ\x9d¼Ư]Ԩʣх',
                        ],
                    'event': {
                            'target_id': '\xa0ˎʚȹӤʆѩԎÕȃļ?ΛͺĸԃǣĭɅҮϾÏˁƝҽɝɭψǼÄ',
                            'parameters': [
                                        {
                                                        'key': 'XЩΆ΅ǉǏъƓ˃ϊ\x80ӭˢ#6ą8ɶƩƀËòû\x8eщѤЎ\x92ӡӰ',
                                                        'value': '¡Ť˦ͳΜʦһϠǜɭ$Ц°˘ŇɐҴ³˯ŕ\x82ʖƖи҃ǷeϨαȃ',
                                                    },
                                        {
                                                        'key': '\x82\u0382ѓ\x82Ŵ˵ţʄӇƫ\x85ÇˎԧƼàВͿТƏTтŪ%όоЦƽԜC',
                                                        'value': 'śΓΙ]ӊƗŶĘƱȮ¹ˉĢϘЩѻÏʻѝZȶҥ΄҃ӉцыƦӍѬ',
                                                    },
                                        {
                                                        'key': 'ѠÂӽԓ҄Ίʑʃbě˲ȅû҉}ӥµӻćcҿʮÏЂũЭ',
                                                        'value': '˖ҲԑĔ?\x9c±ʳƋƃ\x85ėҒӺӽϐúŷӲҜ˺ѼҗӗɃ˾Dϒʐ¯',
                                                    },
                                        {
                                                        'key': 'ЃȺɖƪǱ҄įìţʈ\x92ÙˢчԫӟŠѳҟГ@ŎӈȀТĘǠɫҷĈ',
                                                        'value': 'Ǜ0ːƹǯλЈΤΠʳüʍʎҚ˪ȽǐϔÞ\x83ǐϭǮđɊϬʛϺͶԚ',
                                                    },
                                        {
                                                        'key': 'ɻЍươƺʏ#ƑηѐΝҫԅ҇ϜWaëь$\x91|ɑ¤юȼĚϹЍͽ',
                                                        'value': 'G˷ԊÊЏªσ˪ʷɮɎϸӇͿ,ɾԥϙәĜѷǠΪǿΥȣǠ\x96ȴȅ',
                                                    },
                                        {
                                                        'key': 'ʏȻ\u038býϏʉȝ˺ʈԈȝјӶŜʛӱҜú<ĩǈƌψѯд',
                                                        'value': 'ŵЃ\x9eǜɈÑǎ®ΖɭâѤĬȽҪµʣʒȿÇ҈ĠƊϹŤţƹͻǍʏ',
                                                    },
                                        {
                                                        'key': 'Ҧυ҉ŐҜҬҵăԁÝȶԁΔ«ϒѾӓ\u0380р˪ƟƧΔǵγȮӪnǄɣ',
                                                        'value': 'ŬÿŊғùoһ[ӷϧϧ^®ȌˍĺԍԋɔŶҧˌʳ6Ӏ˦Ӵӧŉɿ',
                                                    },
                                        {
                                                        'key': 'ʾљŨʐΤӁšҺΠ\x99шɯӨ{ΔŌŝȺeϮϘŻӮΩбēҢɓˁʙ',
                                                        'value': 'нЋďТǶӢÞΜžϒćȃԚOКϪԝ6ԔéĬ˸ʅȷԠϓТÍʕӸ',
                                                    },
                                        {
                                                        'key': 'ŷƐԌƛА˯Ɔ˹ӳҢðԤſɞǱƓ҈ǥЙǵǓơȑЙŘҗǻ«ɃȲ',
                                                        'value': 'ąoѭƔγ˂²þǹԖʀϻǁԂϫɐˤŀúɁȲҝĵγ˄ȑƘЀƴū',
                                                    },
                                        {
                                                        'key': 'ԩФjТˋęóЪŉįΚʎϬxКҲƄԨ',
                                                        'value': 'Ԧч\x8dЖćҙ˯\x98ЯǉωƳсΎƛӡсʁкɹľʅ\u0378ЬʎÔԎˍ\u0379˜',
                                                    },
                                    ],
                        },
                    'comment': '˝ʚæũþȊςǀҪʽƑˇɨƲȋǇͿż2ˍҒKʢʴҵϖ҆ßǞɹ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'master_sequence': [
                'Ң',
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
                    'ȂƥѮԬ˂ϬҏĶҞЭóģͿρΘǁʈĮˬ',
                    'Ѩ˷ǾÍ{ϣȫȢѐϗ',
                    '҃џɕŦЦǗгǗҧƺ',
                    'ɉΎѴӒǢŗǱ×ʙY\xa0АǖʎɡΧ˔ҭ',
                    'РǔЀϵєȊś¸ķ±əҟӗϋư4Ӷ',
                    'ŕ}aЄƛԕ\x9dáɒđѤΫÞ\u038dǞ\x95Ϙȷ',
                    'ʭΦυӺϳЃ˨ǳƯˇϡΩù˲ʹѱКԇǞǩÍBǾɚĄƉŸʖϿ',
                    'Ĭ˘Ɂ\u0378˟\x9dƓʌŇΖψϭû',
                    'ѼƧӑԥĄӊƳȊ\x89ѬŽƓʓ\x8bţϞʢʝĴί¾ȹȴԩ',
                    'éſ\x93đǑɤηүʊԚ҃ɂDԉĔϳԡӾǐʺǉ',
                ],
                'bindings': [
                    {
                            'keys': [
                                        '¹ƆƔªΆǇЗ¾ŹǀpaĖȘǚʘ',
                                        'ƔņUW˯ѧЇ¼',
                                        'ȾĒȠŚɆͿǡ4ŋҢӐЦ˾',
                                        'ɕ',
                                        'ӈԩŅҬƠêƊȺƙcūʩ˔{\x87ʹȘύЙƠ˼ԊӬ',
                                        'ʄ˙ЕІǹϊҮԌϽϵƾӥÏЦɮˋäȿӥƺѣ]ķŒ',
                                        'uĭˀÐіӛ=\x97ѢŠӱèǼȄʉƫϤüҊƢеԟЃ',
                                        'КǨıǪʋđșĉȋӢ˵ўıÕȪʨԮIѓ',
                                        'ӃӒаˑȉ²cŽϹѢ¥"ѯÖŵq\x96ӄǂȬˈƯ',
                                        'яҹˢɝԏљÏȏŢǿĥѹӗąзřʤӥ\u038bǱΓǫĥïΑǆƍ',
                                    ],
                            'event': {
                                        'target_id': 'ʤeԝʲȯҡĐάѡŅһͿžŰ˔Ӭ\x8aLbˍΖŀƽʢʧ\x80ӱ¡ʰӪ',
                                        'parameters': [
                                                        {
                                                                            'key': '1zɅͷõɫǐ¦ɛǾНŎÏ˹˼ˁҷһʾƁōɗџӢùʪ=ˠ˸ѥ',
                                                                            'value': 'ʫѶʘˉҭэѡƤÃϊρ)ΊѢԩ?-ӯ˩9ΈѰϐ5ͲƎīëҠ\x8a',
                                                                        },
                                                        {
                                                                            'key': 'ғϴĜçʣĂӸʧɞĄΒӺћІ?Ш˸ԋŧєƺЮħ˪˺Ǌ',
                                                                            'value': 'dǘAɆћΥ\u0383łҘɥȡХ\x86ɄԧуόǾϷӲЙϧχǸԑ˷¢ɱΙɨ',
                                                                        },
                                                        {
                                                                            'key': 'ȓƳǑΕ§Ư#ΩΫӖɕΗüӓɸͼǥrʑįĽ',
                                                                            'value': 'ԑӏϏǳю8ȫά\u03a2q´ʠӦˆ\x83˥ŝʈɶOˏˁ4˶dƯͱǴи\x85',
                                                                        },
                                                        {
                                                                            'key': 'ǳȞ˲ɿɔƚȮФǫˇϕ¦ƵȐЭɆɥбğԐț΅\\ԅȓФŇ)гɑ',
                                                                            'value': 'ЧΑǫʺӘИϢāғҒǁ˰ԢɖιϩӸƕκɂƼɪİНƭǥ˒Ν϶Ή',
                                                                        },
                                                        {
                                                                            'key': 'Ȩ\x85J»жԕɥéƵе˱їͽƳɝ΄\x88ЋʒàӋ{ȪȐëηӀÍÆϋ',
                                                                            'value': 'ϟǋÖ\u03a2ȜƒȇÁԭҴĺɠѦLчъơΎҪHϢʾǹǄʘƵПÌƽԀ',
                                                                        },
                                                        {
                                                                            'key': 'ϫţŎȼ\x80ǉӢĒΏ½ԪêҎʂρŕҳɉPИĜƢț®ΙϹLЋøc',
                                                                            'value': '"ˬҸӎěĘ˫ƗwŐȚɉľ!źЀƱʛΊŕϠѤ¼˹ЉĻһĚҁу',
                                                                        },
                                                        {
                                                                            'key': '¡Ԣ(ĳϽϾªϼϸĢOůάԪǭƻωǾƒͶǝ¶ŏӛɅɶƄaɐԇ',
                                                                            'value': 'èǦŨǁƋ\x8cɯľ˳ҕŪ˧é\x88äӧѠǍΤҵȰŢӢ\x8dʎȴкȩͳǑ',
                                                                        },
                                                        {
                                                                            'key': 'ʑSˍϧǝτѡƗ\\ӑΉά+£ĝӻǀҤPĞπŒľӡӞŜƃƶԊȜ',
                                                                            'value': '\x88ΊƢҵȴƂȏəǦЂ\u0382Ѥ\u0382ΐǋѤϞӿȝɇʧыˋммѻ\x8aʃ˦Ď',
                                                                        },
                                                        {
                                                                            'key': '+Ҩˇ¯АRϴțɖʪɫƠʇɘÒϷҳѹƀƎˠɊ4ɄѕЩϠĠɈˆ',
                                                                            'value': ';˱ƵЄѧěσƜªΝ±ϨʪƦˇƬμŜЃ˓ѐϝԢʴǷ{łѺӧƼ',
                                                                        },
                                                        {
                                                                            'key': '˵ΗàϹɧ\x82ɃưqEɃŻώ',
                                                                            'value': 'ʲîҩʎnĔƂЉʼИê[˶ӄϝǧɌҀӭʙєįŁԚƂĉʢʕy©',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ӵϱԓԒγÙäӈЛɯÕ\x81Ȅ˷ňıԤÔAɵɦɢ~ԣĿ\x9b˾ƽԍќ',
                        },
                    {
                            'keys': [
                                        'ŹɃîȐΕ\u0381ǋ.ŢХјΎΧвϕͼďăƏʙƳȻΧӯϊˢ',
                                        'ÂɞȥÈ\x98ӉӲȷʖƹΊȂ',
                                        'Ȉȯ*ћΈԧϋҎĆφ \x90Țǹ˘',
                                        '%ɡ',
                                        'аƆʀ˜řӮǭεɋйƻԠA҈˴gҗќȡѭҤ\x92#іʡӃҤɀ',
                                        'ԇǥгԔʶԙԠƲӅњ1Ӟ\x83ʢъʗ»Џԛą7ƭɴЇζÖϋ',
                                        '¤ɃȺʨҋӎғΆŬʫҡӋΡǝĮõʙԁϤșѺϳʽ˶ǔ',
                                        '\u0382ТñжũʔjUҵEǺ',
                                        'ӄ',
                                        'ȇƗʷȸĚ<ĩϑĿǥΉѼYƚθѯȹËӆßІβįѾ\x7fȂ',
                                    ],
                            'event': {
                                        'target_id': 'KԍϴЦˁʶШРWŬūñļʠĄ˚ЬėƳƐ\x8c·Zn\u0383Ӭđʏǜ\u038d',
                                        'parameters': [
                                                        {
                                                                            'key': 'ͱˉŠîќέſƶȪȆơӽѠɢǺԮΨĪԂʳʂǝɑɛ\x9b˻ȻǹӋ}',
                                                                            'value': ')ԠʣơӧηˠäӁʑɣѼͽưΧƈǜҖˀǏ˫ƯǄюқɲȓӡ˸Í',
                                                                        },
                                                        {
                                                                            'key': 'ϬӵȀӛӼǅËӲǦҙeӕ\u0378ÆΟȤ\x91ȔԅŴúÔǀʌćԫүϠ',
                                                                            'value': 'Һ\x96аʽʆшԒAӁȞηń\x80ЮĢĉĠʁƊŠȭ®ʭҖèȽΟņҞ"',
                                                                        },
                                                        {
                                                                            'key': 'īҜЬeʸΠέёǑ΄óљ',
                                                                            'value': 'Ҷοʘ\x9cύĔŰÿ\u038bΒʄЏӾƹДƜ˓ɠӳʺɠəΒȭЂӹȓǈ\x8aˤ',
                                                                        },
                                                        {
                                                                            'key': '҃Ĥʧԕ\x95ӿɨϟ˟ƮǎγŻǃЁӸңƌçi\x84Л΅ĀĤ',
                                                                            'value': 'ȾCʴαʞŃҊǡԁ\x80ԉҷͶЍѽυхǭЃȔȗDǡѝԬüԈƥǽ\x9b',
                                                                        },
                                                        {
                                                                            'key': '\x99ƧƭŬ˺à\u038bìВѺǗɣǮX\x81ƳәĚӯȪѻԆԄˠƽдƚĄϭѸ',
                                                                            'value': 'ƍʢĊȿǂ$æƎ˝ҵǚϟ£ďyЧёԃӀԥԭŲlѳϩ҅чű˼ː',
                                                                        },
                                                        {
                                                                            'key': 'ĈІΝ˧ƈžҋҗ˧ʞЬɵʹǰȑąƌԥ\x93ԪºϤԙ<Ϟ˧ŀ\x84ʚ8',
                                                                            'value': 'Ӕʐ\x8f¿mΦÈΡßќυưúƱ˓ˏ¨Ӹl+МӴƺȑǿϬϪͿӜn',
                                                                        },
                                                        {
                                                                            'key': 'A¶ҡɒĤʨΪԣѮƐNƏɿɯЛʏςɶ\x94$Ёˍ\x94Ν\x8bѢН˽\x8c\x9d',
                                                                            'value': 'Ɔͳɍ҉\x88ΨҀѹħŕĉԎªıõʀӰRÅȺŨɃГяŰ\x85|ɋƞӵ',
                                                                        },
                                                        {
                                                                            'key': 'ʰѬłҡȎȫǍ϶ȸρŶ˯ѡʃ˾УЪђԝқjʆзƩƔpÿȫȄʹ',
                                                                            'value': 'ԓаӀԓҦìѕ\\p9^lϧʳѦӃȽϵϋПқϷҎҦŠ\x9c϶ĉƉͶ',
                                                                        },
                                                        {
                                                                            'key': 'ӖЖʆѵˬЂŭſIǦ¯ƔŢȻǛĀέɚч˹űͱԌǁӢАÄĚφɹ',
                                                                            'value': 'ƆɜƘȑqˮĶїȕɘίTЏV˔´ѵjϐɴʊȵŖҹƋƑǌ ϶w',
                                                                        },
                                                        {
                                                                            'key': 'ȸʕϟŶԥņвʂȤŭԪũ\u0383ÝΎ\x90ҌԜΒӱԣ^~ǉˆψЇЁӮѯ',
                                                                            'value': 'ϒϵǋ\x8fЎČμӇ˼ƙΘ˪ƙзʂіǃǝęǚìҒəơǗѨЂѧӺϊ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'Ϊ/ұԃфϠ˙Ѷ\x9d\x96Ԯ',
                        },
                    {
                            'keys': [
                                        'ÀʨϤóǴȪʹϝ˛ϙЦɇȫøˈΟ',
                                        'ϬЙƴӌRζʃϥŔŷαȬΔΏˢʅġÊѰİʹ˶Ӻɤ˶',
                                        "ɐԩƿӄ¶³ʖʖƿīŗϽØȕ\x88ӈΗ'ΛԐӜȽƜВőƶ\x91",
                                        'ȉcҶʾʔŶԇяϩÐůʡЖơŨϼΪ\u0379¡ĒĚʊӏƋǉ',
                                        'śùǝɆ\x8dĚʯҏɺǑ',
                                        'ϘӏȤʁ\\Ϳbр',
                                    ],
                            'event': {
                                        'target_id': '\x8aйЬԕ0ΤʍͶӑ҈ ŤҙȼʸƳѴԖӗҚǱԉʘ˛ʗӴĵɶҤĪ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ԇĀLΠν˽ΘŲőúƞ~\x97ѢԅǩԘď\u038dɕλɘӠŋԬЪĬϊсǌ',
                                                                            'value': 'к³Ӥ\x9aѢ˸ӂӒϑōԝіϋϬ7ʿӫϵΝӭΎȗӜĩ˾ԘҧԡÐː',
                                                                        },
                                                        {
                                                                            'key': 'ʩÃõϬϷƱ',
                                                                            'value': 'ƌɢѐƗÀſ\x7fϻ"ѹќƕrΕщˑī˒ȍ\x8aǲʀʭӀε˻яΙ˞ë',
                                                                        },
                                                        {
                                                                            'key': 'ŇɚÇĈFЈԉәӛ˩Ҹ\u0381ҢӉĔˢȸƍŨÇƒ',
                                                                            'value': 'қǋȊĞҹɞȭԧҞӎҹʓѪɖÉǩѸљ˩ы(ɓŊˤѷϬɩЙɩǟ',
                                                                        },
                                                        {
                                                                            'key': 'řόљÊŪϗȖ\\¿ǛɭʌҽМӤɍȴѼϒЋϐ˚ŁλӪʻҦδÌŇ',
                                                                            'value': 'ЪŘхŴ{\u03a2ӶϧìͽѪ˄ŵ\u0379˯ƞwϾӆ\u038dʖɳŮЉ;ưr\x90Ĳʱ',
                                                                        },
                                                        {
                                                                            'key': 'ƷŻ',
                                                                            'value': 'Źӑх˫ðѳ˫ɾȩɴоʌЄǌС\x90ʦɯҵǢΐԓ˦Ƴ҄ϤȵƷƈȒ',
                                                                        },
                                                        {
                                                                            'key': 'ДơeӜѪқȳîŜŁҨʐ',
                                                                            'value': "Ҵ`ьȜ\\ѯǅǮ'ɰɪǾɡŷğ4Ʋ®AˢʩѿȫʆƅшцҎʧΰ",
                                                                        },
                                                        {
                                                                            'key': 'ŧʞЯϪ˥ɖƙȋԎłиȌȓɎʦϛňɂӭĳGһĪʹïÏԤϞʣЌ',
                                                                            'value': 'εǳÄȇԓʯ;ŸҚӥ-āԤаҔӺȓԣѣЮŜҟӃЊϔVΝҒҷˈ',
                                                                        },
                                                        {
                                                                            'key': 'RǆŪ¸˥)ˮԪ«ЎʙӣԤȯ˦vĒÆȝŨ^џϫԑǤэ\u0382˒Fѷ',
                                                                            'value': 'ưλŨʯŀғԠ=ɤäˆΪɊԞǩѥԀǂǪ¸ǚ˫ȂĤрăԕӒϒ¦',
                                                                        },
                                                        {
                                                                            'key': 'ċQѩѽȦϯԙċ΅Ķ˟ϥћѪǦƲʹǞͳɊiǬ˶\u038bӐƸɃCΨѮ',
                                                                            'value': 'Q.ɁȥрőΆŧϸϊԭОԣŋ΅˄ɱʯ-@цµçѰѬĚdӳѨĦ',
                                                                        },
                                                        {
                                                                            'key': 'ŲƇ˄Ц^ϜˏĸьɣˮȲКʡΎʇ҈ѓŸҾЎѰρҦ',
                                                                            'value': 'ȅƽ«ĆԡϞûɘ˖ԤƓ¢˳˒ŨɦΤſΎƓӗРħċӨ\u0378Ȑ˶͵Ϥ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'кĪԬыɰśӀяɸļĬ\u0380ơɯzɹÁǪɦӕȣùǞșŃȐԜǄєȬ',
                        },
                    {
                            'keys': [
                                        'ʩǡΌөїαҚǸĦԣæϕ£',
                                        'ơК',
                                        'ńȈҙɿȣĖƮӓαӦåȚˮƂɄʼ{O˩',
                                        'Ǜȓϛǝ«ŝ҃ˍԭπōЀkΚʞɿ·ÎЩ©;Ʒ1ΗóǶŠĺ',
                                        'ШŲžΓȌ/ÂϮǴԖҗɵΦāΫɐɅȃƦɖ',
                                        'ӪʤΛЪ',
                                        'ΥɞƱʙ)ξӓ\x9aƒ\x82ǶǨҌЯ˲¹',
                                        'ƩYЛˀƤӘň)ʳʾ',
                                        'ʏƱÜĹƘ¼Î˹җѬͳʧʷӰӪўĽëυԢȁŤ',
                                        'ѼȨ<ȹΥɍԅ ă˗ЃӁŹѦжsҏδжҬˋӨ˱ƷȦР',
                                    ],
                            'event': {
                                        'target_id': 'Ʌʪ\u0378ÍɞʷҴɘ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ˀɓԪӠԊāÂǞжFƦ˻ʟҒĦƆɐ΅ͲưɤԝD˥Ěђˆũƍϭ',
                                                                            'value': '϶щƲĔόIУȕМϿ¤ЃïīƼʡњŗǥӂғȴwΝʫĩɨϒŨS',
                                                                        },
                                                        {
                                                                            'key': 'xƽʪӍǱ\x84ÐɝƀіͽФǨѫǨĔǾ\x94',
                                                                            'value': 'үң҉цҌǙƳŉԈʡԊΨɴΖԟЩӖΆҦǳԕʡʽɁƥÔʥɭº¼',
                                                                        },
                                                        {
                                                                            'key': 'áŞ͵ұƴʼѐɣЛȻǬ¥қҰϴÍƬɡ:İʗƉҼOЄuӯ˥\u0381ѱ',
                                                                            'value': "6'ŰԜǽ˳ȥ˲ǨǦҐȫøǭʩΈīРÉʸСʅʖӆΆúҗхǆȫ",
                                                                        },
                                                        {
                                                                            'key': 'ҘΆωǹǑԟԄȐåυţҰʮ~#ЅҦ˭ΎȗуɑēƙñһӞĞǃʂ',
                                                                            'value': 'Њҵ¯ÖˑӆМҙś¬ŕXќДϒɿ§ϼ˘ƶ\x8cӅƹίˤʘξԧ³î',
                                                                        },
                                                        {
                                                                            'key': 'ŋɩЇƝȞ˃ѩČƝȫǳ\x8fФɕԝ^ɶÕӧЄԃȧɩĸʫŹхǓØî',
                                                                            'value': 'ĜǵΣБҜʅΔĘ£ЉҊȢÒǮЅĪӎ>πгγƺɴäe×ˉ(љҒ',
                                                                        },
                                                        {
                                                                            'key': 'ПΣг³ҩ\x95ȢӚЪԝ"Κҝ˵ЫĥƅɏǼƏɉЏSúҒ',
                                                                            'value': 'ϲ˥Κȝг\x99ɜ\u038dЦôĂȈŌφöӬȾċϺ¨æĻӨЪǈ˯ϪͽƢt',
                                                                        },
                                                        {
                                                                            'key': 'ȩǓĘҜІϬ˶ʆΞїĸɡïҗɶЯŇ\x99ʩƼȰĈƗѿÉɭǼҍ΄½',
                                                                            'value': "žúǛǁʋǤ\x8d\x81ķ˲Ҽƒ'ÄʓéȄƱҰҢǅɿϓъȟˤ-Ҫ҂Ū",
                                                                        },
                                                        {
                                                                            'key': 'ӘϦ\x9dv҆ÅǌӗӞǌʃ҃kŸтʌϑ˜ĝ˸ԬɬŕİɱќӝӺɆɣ',
                                                                            'value': 'ƭ(ΖA\x92Ɓ/Ƒǅɏ·ÉõzMԋǥʹƛW˺ƶĎÎ΄ЎɈɷǗǇ',
                                                                        },
                                                        {
                                                                            'key': 'ɺ\x88ЮƐɲЊǓʑɨӏtƝćˁģƀӫȐ{Ә;ΤύϭʁˊƽûѴO',
                                                                            'value': 'ϟɲűȿƨϳѭԣƷӬҁ\x8c¬Ӂ²ɾʥ\u038bĬũТęϪӟϯΥ¸яƥА',
                                                                        },
                                                        {
                                                                            'key': 'ӎȃ\x82ĜҿϢЈ;ĎȍŏġʍÉĜ˱ǦǉӳU˸һҺˍɈĜѸѽ˚ϒ',
                                                                            'value': 'ӽϜ\x81;ˍУίВɾȤņʃөƷȓ<´ԌђƑʏŵˁ.Ćžp˓ǔǤ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'юƶĺʫ\x84˖oǕ6ʧˠЯӺȁҺɵƫɹʪІϺȾƈƏԌĔ\x95ϟȺƀ',
                        },
                    {
                            'keys': [
                                        'ӹɱĲæĂʲЍƱȐę\u0381ɓL',
                                        'Ѿˁ¡ίƽɹǳзȕ\x87RȠӞƊ',
                                        'Ԗ-ϣΡѹК\u038dʰôʔχƶiʬΤϟґèwΈӜ',
                                        '×ԐқɦϿòϑԗΒϯȿɘԥƫ',
                                        'Î',
                                        'ØŇǷҬ',
                                        'F',
                                        'Ҏ˽êΞδǝȂʔnͳèŵӨ',
                                        'ʹΏԊ\x8bҾЏӸ\x9bʿū.ϒƲ\x94ĹԈŗ˥ƂȊԤλ',
                                        'ЩţǫЯÌǹЕƛϔLΦ͵˟ȍͰˢҷ|ÔŔʘ',
                                    ],
                            'event': {
                                        'target_id': 'ǴѻЩǤĜ@Ä˞½ϋæƕŧ˯ιûVŒԏ˥ʇƺΠ®ýƄӾ\x8bԡŋ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ѠӌԦӰ-ԙ\u0383ўΖΝҨ˪z#˨ҷΖªѳή{қéˏƘҩʐя½η',
                                                                            'value': 'Ңŉҥ¸łӝʆФЂŝ҂ŢѺƙ϶ÔÔϦƐЪɮ҆Ț\u03a2šˍӋ\x99öӁ',
                                                                        },
                                                        {
                                                                            'key': 'ӳ',
                                                                            'value': '¸ӫԅ\x97ΔÙ<YːġҠǊqΣåʿmȿ˶ǰ\x9aɧʠcΈԍŲԅȔm',
                                                                        },
                                                        {
                                                                            'key': '˙ŤȦιď1ΘȊϡ=ќ˱ңĽЯƚǹəɾѨΤΧ˱\x92rԟϽdɡԏ',
                                                                            'value': "ӅΗ\\ѿҢӡ'»Ȳы˗Ч\x98˓ΒϴƷԧɘҼˊ«ÝmƔӛƂ\u03a2Ҭɓ",
                                                                        },
                                                        {
                                                                            'key': 'ęǠŴ΅Ԍӯ{Ɛӫϥоǯ\x87ЙԀ\x93ӴˬűʹéѼ90ѓȼƨɈ',
                                                                            'value': 'Ѽ˹ȧӽɘÒǱɈŢ<ĪψƞșMЁPԣŗӋʆω҉\u038dȉůɰ\x95Ϩԩ',
                                                                        },
                                                        {
                                                                            'key': 'ы',
                                                                            'value': 'ôЋɓҁľÐ^ǉúUҭɁǢчȒƂъ¨КЛқǕΓϘºӚӳҖԀұ',
                                                                        },
                                                        {
                                                                            'key': '©-˞ҰùʟʭAhоѨҜǛöàҼΎKԀȨ,Өț҉ӏηжΛ\u038d?',
                                                                            'value': 'đ˲˂ѾəCUσÑЂŭԛͻêŐȴjΦΩӶ=ΰ˘\x88ĠÉВϓ_Ǘ',
                                                                        },
                                                        {
                                                                            'key': 'Ҁǫīϗ+Σʐćш\x86Ґ«ɣĲҽȜȾåӍǞĦϳѸϯ\x94ɦAʹюҥ',
                                                                            'value': 'ȁjE»˜ˌʑýȖKɍɒʱʒѐȸ¥һȹŕƙűVǌәƂϨǡɯ˷',
                                                                        },
                                                        {
                                                                            'key': 'ɺq˜ľ˝ï˞πԢЄϥ$ɻʛċεŤϥʡķΏζɻˆ',
                                                                            'value': 'ƉȋʁЍŋ\x90άƔɵЗʫНΚʍё\x96ŚǸÀΒ˅ĪΗϙȄéǀŢ¨Ċ',
                                                                        },
                                                        {
                                                                            'key': 'wӞԫҔýƂҨ\x97ϹҵòҐǓƞȞԐʔúпʽjΛʕ˵Γβ˙ʜpJ',
                                                                            'value': '_ʆͰzЇʽȯɵ\x9c%Ȋӻʍ¹ʏɹȸӱȼǼÂΣʓŚęЊż˫ŋѹ',
                                                                        },
                                                        {
                                                                            'key': 'ǎƄʺɏȦŬQΡʹƬč*τΡǆԁƤϢԓɃǻƦĀɛЈżЀʪіξ',
                                                                            'value': 'GĤοӟӓƈǴňÿ´ЍӵΉŹӧɑцȎĘƢʽÁѴ\x99ÀӡКŇ-з',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ɶÝϚԆГЪѐɰ¬¨ȟ\x95ϝÅǜǌǡȵʷҤȢԐɭƿé#ɜԦɔm',
                        },
                    {
                            'keys': [
                                        'ŕ˳чǳȢ',
                                        'ɨʪǪ4ȓ±ѭźÅζdѷÃņЦІrЄңńȹƜūИԒȥǷʈӈ',
                                        'ǫϺͺҺҖχÀ',
                                        'jшɾƮкρΡϜ>ш]ͺǽʆɚɃЃԍФχнɦ´\x88k¿ȏƏċŇ',
                                        '\x99ÍГ˻ƼԬԛӹȲӸñpΏó\x8a',
                                    ],
                            'event': {
                                        'target_id': '²¤ЊǤӂoĆâǋƄΤȘK"ґӸŊɔŗҲǇ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ÁȁɣɘјĘӞχӐ˦ɲϣƏDÖʁȀ˽˜ͷÆƍӯŸѸĐǾD¡ԕ',
                                                                            'value': 'ʗıĖЂεÚΊԔҹ˼˭Ҋu®ϴЌŁϬУҨƢȢũÛѢʯŢʋѫΖ',
                                                                        },
                                                        {
                                                                            'key': ")è'Ĳ_ˉҵƛƷȏO\x8aǠ&ȦćǬω˱ԛʏˊ3\x85ė",
                                                                            'value': 'чˣϛԭǠƠҮēηϊіěƏČɒǬÃҸѕѨЍɑтĈŌǲЊ\x95мʘ',
                                                                        },
                                                        {
                                                                            'key': 'ǿ\x8fŴӗͽԍ˜ċȧWŒӣ¢ʸжSӹJσŞ˲˧ζҟǺ҂йÝψ/',
                                                                            'value': 'sȲÐÉρțȭʁĖǟҦƵѲȡҥMĖŰԎþӝӋʬ\x97ԤΫϰ\x9f\u0379Ʒ',
                                                                        },
                                                        {
                                                                            'key': 'gхћӳҍѶ҉"ӪĢҸ.!5Ȁʁ҆ƗΑПŝʮϦcŧӊΜɻІф',
                                                                            'value': 'ӴƿηŚĖЬ҄ʍ\x91ςǜÚôˬ[ʨőҶǞǴԖǮƂŁ˒çɭŇȥƹ',
                                                                        },
                                                        {
                                                                            'key': '\x9bƁƮǀǠŖŰϏȎԗĶϮҢҖȅȰϩѻŮќ»ƫԢĺ\x84ҜȩͲŒҕ',
                                                                            'value': '!Fǥų',
                                                                        },
                                                        {
                                                                            'key': 'ƀιƍ9ύΓ҈҉nЕϹʅ˞¿ϩԫӕΰԈɂѢϦǑɛЄ\x83ɱʿ˽ɐ',
                                                                            'value': '\u0381˼Ơĉ?ДЌŀ\x9eǁиŶÈǈОΕąʏÏԎȘΦʉţ˅ɐǗΥѺƹ',
                                                                        },
                                                        {
                                                                            'key': 'JĠάќ6ìɉĞŅŌɱΪԏǥʷьȨӍŉѩ˛ʍЬѴƷεКȉĕԢ',
                                                                            'value': 'ƣÔùŦȿǩϞȁлѰѱЖË´ɁӠ.ɰŞǚ˵ɂȇ\u0382ʼʧˁˢ3ˋ',
                                                                        },
                                                        {
                                                                            'key': '\x8eĽɉѢҾӊȢǧʢρя΄ǶЍĽҔȌʣЗƕɌûήѯ\x92¬ǖī#[',
                                                                            'value': 'ʎ(ΨΏÐÒʴԎM!ԍΆ\u038dęhǇΚxƼǣ/ɄȓƔ+КĞĐÏʷ',
                                                                        },
                                                        {
                                                                            'key': 'Ý\x94ĊȤƘyĄȶθpѩмg¤Ǐҗp\x84ˣÅĵҶŴrЩӲʟYʧ˧',
                                                                            'value': '˨ШČӃuЖˈΉѫǟɋЙKJΘЮÔ=ʤƨòQíԈό˪ѯ҆ǁԄ',
                                                                        },
                                                        {
                                                                            'key': 'ǼĐġ÷ʊҢЅrӆΝϿѳȅʯüП˜ȊȎƃIȖΩȽïɨâįPɂ',
                                                                            'value': 'ȖĉBĶ˾ϥжũàûÜȦǈxțϠҙĺĂȴΜРό¯š£фÀśˣ',
                                                                        },
                                                    ],
                                    },
                            'comment': '-ˇȅүŌрӹʩɆ\x93ÊԎҝӗϖʾӆȗˡϔӗъ˴ӉϵIɕƂɧĘ',
                        },
                    {
                            'keys': [
                                        'Ζ҂ĂǍ˦жżШˮɮΑǞ«ƝЍӤˁȥ',
                                        'ǩѲȱɫ°ϝĕ˪ЕԟϔĸľӟΖɗɓƢѬó',
                                        'νΩūї˔϶Ӈɝˋd5ɩɬȔōmʷЩyɨɘÏ',
                                        'r>Xpś˕ˠƴϊƖēғĖǺΟ¥ѪǬ',
                                        'ӄӾT3ǨұΕȁƔ\x9b¿ĽǴñϚŨnʎƅÚʮх',
                                        'čѿӅΰʴ\u0378ÚʊзͿƶнτсžƈӇĭǰŃȭ·ȥ',
                                        'ɥ˵Є{"ȲȤ2θɹӮ"ЮŲԁˡσҹMԣ<Оʆ\x8a',
                                        'ĢǉҝĮƅ£ʞʈЏæȠӳΧā/ƒӞͷŜѦӝÂΜΎЈΙЧ',
                                        'üǑ\x9eˎ¼|җĝÌ"ӋɼǍʹɢџВ҃Ó¨ģȲ.ÁКѥӘǮ\x8a',
                                        'ϹϯK7(ƔƎԮůʻǈŝ_ѐ',
                                    ],
                            'event': {
                                        'target_id': 'ÂȣҥԍıȇѤĬ\x8fѨƾæǼɁVӬя\x8dϗǚϟɾgбөέʂBѿϱ',
                                        'parameters': [
                                                        {
                                                                            'key': "ǵз\x9aΜψĴǧԧ'ԉΨҗ÷ǫΊҤ#Ĕ\u0378ŒŸіńщώΐĥUκ¢",
                                                                            'value': '¬ȪтΖɘоǡЊТ˯шˮĕɊ;ȥŉϔƾӛѡϛʑѹΤĒ¥ńķĖ',
                                                                        },
                                                        {
                                                                            'key': '¡ʭʵsʤqƪ\x8cȼ¶+ʎ\x96ҟƤϻʹФЋ\x8aͰД(ηӂ˕Ӡ͵Ƶr',
                                                                            'value': 'ΦƠϊÜӺϞȣ¢ΨϫьPȡʋѩ(ϭ ãìϷϒŸȹĜƁ˞ȄĎʸ',
                                                                        },
                                                        {
                                                                            'key': 'ҐqЅºùеxμϕʥxÁR=ʚя\x93ÉũʂԒӨӢǝхA\x9a҄ʔǸ',
                                                                            'value': 'ӏϻ˥εĕыχѲǲȋНӺþӰɮXƷ\x80ħϱϿŚ\x98aХϧƩňѥԠ',
                                                                        },
                                                        {
                                                                            'key': 'ǎƯӅŕäǳїϗТĔԙƭϓƔǀӅƺƱŋʗƬƗôѩЌʷѭҔҲр',
                                                                            'value': 'чOȧp\x88ΔЋɞґǝҐϋҦĂ˾ѰϪΥɉԋÕ˸ĎзʢoҦ5Çѹ',
                                                                        },
                                                        {
                                                                            'key': 'ɠʅÈʓ;#ħȽşӤpØўƈћ¦ϝ˚ƳɘЂŜʑʉѳѝ°īІΊ',
                                                                            'value': 'ϙЊʼµĀԗƌĝÑэʞƸōnɦłǔȂ\u03a2ЫɐðȂҀӱĊτҲpΛ',
                                                                        },
                                                        {
                                                                            'key': 'ʂ\x87ɿĞѪǏêơԇĲ˥БöӄĿW\x8fȂѮ:ƊƢČÛ1ёҽǇϛˊ',
                                                                            'value': 'ǛȺʞàәӇˊȞӚυSҢ£BΨŽ˨ʙǏѼɾѩƸ0ǫԞƚʨţʱ',
                                                                        },
                                                        {
                                                                            'key': 'ӏ˱ĿaƯȔ8Jɀģúŉʁ?ͳĉцˆʨGήʨÒȽĜЊόӾĞ',
                                                                            'value': 'Ӿ$ſԊбɧŤҧӭ˯¼ԘćѬԅӽĴʴұцǕȼʓïͿºɼɪӓџ',
                                                                        },
                                                        {
                                                                            'key': 'Ʀřҽq҃ʽCӖĪҌÛJңɄVn҇ЈүǮʘȹЂϋCʹʗĹλԅ',
                                                                            'value': 'ҩìӫлԈԧȱÂěʲʅkԤȸӧŖűʏ¹êлӠĔþɈӟёŴÈȿ',
                                                                        },
                                                        {
                                                                            'key': 'ȐǈҒīӠИŽҩĆɷʵ8ЎϔѼӕºķͻɞĚӭĢń\x88јĶбɮ`',
                                                                            'value': 'Ǫ¾ӒоżҢɨ\u0380ȁˌɘžũѥқʐΉįіӡϚмEζtҲťȀùκ',
                                                                        },
                                                        {
                                                                            'key': 'ӬļīҹӼǷÞ¸*\u0381ɇ·ȼý\u0380ъ',
                                                                            'value': '҂\x94ѩķɦЩʲÖƬҍԢӰϰˑȇ%čʔ\x9d/˷ŨŊȪƍЙɵ\x7fӗ˱',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ĬȝíˑЍȮˍҖ_ЭˊьИÈÙďГWΨӭĽ4ǈ\x9fŹʟь\x97ӑÃ',
                        },
                    {
                            'keys': [
                                        'ή˩ŁȉYҩBșԘЇϯǓÅ',
                                        '9-ҫ˙ӲԝƟԫԀԚ˯ΆӟќǩƉһϰǜÍ¦',
                                        'Ɖ[Ƽˉ\u038bǄϴǖ@ǘ҄С˄таӻ\x95(ǒ',
                                        '\x85Љȧ˹Ųԫ˄ԔƚġúҫˇӞѵѢǥ˛җǊť',
                                    ],
                            'event': {
                                        'target_id': 'Ȁ\x8cԊńǑћИѬǖѪǧć˫ӶʮȊęҖƭŖЪԋӵJ;Ӄ҇ͼɵυ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ͰIĿxʤˠvƻƴЌԪʰҰˎÆʷòήΎÝӭ',
                                                                            'value': 'ѸEĀʤшͽӑǦƄƟмωӠɇѮ2Ҥɤ"ă˵ң˄!ν˚ɣ˾ЂĜ',
                                                                        },
                                                        {
                                                                            'key': 'ӞѧɼͻĤğƐM\x9aΨȀĕӿԌвÈ_Ⱦ\x94ŝƤɕΐьˉӝ\u03a2λÞƶ',
                                                                            'value': '\x94έǱ˙ʰԁĄk9ԈЅ\u0379ȼŉȳԮƱΦx˽ͶõϺιҗΒϯҋhԄ',
                                                                        },
                                                        {
                                                                            'key': 'Οņɧ\x9aʸѱҜłҮЅÉŷǄƒǪƭˇиȱѪНЧNmȞ8Ԇ\u0379A',
                                                                            'value': 'ŔΕĐȽλSиψªˈWȌǭϰϸĆħƃόš΄ӡðѼ˻¶¹Ȫĵќ',
                                                                        },
                                                        {
                                                                            'key': 'ƼɨҲì҃ãϊĝёϘ',
                                                                            'value': 'ƳąʚǄϽɀȠΙҳ²ƸӔžϷŠϸ¥\x86ҹцȒĬƨċˤӰŪǓίǕ',
                                                                        },
                                                        {
                                                                            'key': 'ȚɁǘѠ\x85\x86ǑθòÆˌ\x8cȂͷЬУȊȐы`7ČǘʜѦάԘΨ˯ț',
                                                                            'value': 'ГѐӬӘҸѵįͲԉћĪӃԃÏöƊͳ;ѨѪмÍ\u0378ƷÈ˻ʈόɶɵ',
                                                                        },
                                                        {
                                                                            'key': '9͵¹˙ќȩȱмԀćÉΔʌǁ\x80ԆńkÜƪËԐǊʔ\x9aίЕОЉ\xad',
                                                                            'value': 'tƫƤ˙wĤ´ϝȻβѱҦǢà āҪÏˁțοӅȒѓӞ˕lıũΌ',
                                                                        },
                                                        {
                                                                            'key': 'H©\x86}ϿЄƍίχȸñνԀũĻȼ˔1!ưÉ\x96',
                                                                            'value': 'šÉáʥԂ\x8eβЏǡ\x99Һϸòˌ~LʔѼǙбŒФ^ťӾšѣӚϘж',
                                                                        },
                                                        {
                                                                            'key': 'ɖѨɚ6цɚР5ʾҀÇʞǏòͺЮԈѶ\x83Κʷ˭ĲɠĞRʷɒˉa',
                                                                            'value': '\x93ίʞĎĪėͶƺʰҽȎĘҪȟҾǗђϩɈάԎпˮЦˡԦɯĊəҪ',
                                                                        },
                                                        {
                                                                            'key': 'ęƔʅǐÈϖє;ȯBʸþ5ÔӭĪ',
                                                                            'value': 'ɔҳ\xadǨϊ˖ƸáİΜўŊΥӣϝԞŌǈȇɫĥğʘԩWƔύːоĒ',
                                                                        },
                                                        {
                                                                            'key': 'ʇϑ\u03a2ѠϗÏЄϖʒҮԋ·ǐ˟ѕӲ8ʲ˺˄¶ΔJŽʳǎʎȰҸÊ',
                                                                            'value': 'ӫʾӔƽŗˬϾɼϦяÑҒȚνч\\ïϵąƋθʥҟΎDëɐÖɘó',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ŝİЍ£ɝθӢʑϚȧӪſά\x8f˸ɱΑZҒԍ\x94ȎѤäΓÇ\x8dŐĊƐ',
                        },
                    {
                            'keys': [
                                        'ǀƦˊЭƅâѾǦˣ',
                                        'йҀɣԍǠΠԛŠнȡ',
                                        ',ŜѓϓίӚ',
                                        'ŔцѴԗʷѬѰ˶УˇѦʗƄƣÃԂŨµƪȖɃ¾˷',
                                        ';ăϛΘȕ',
                                        'ȵrˈҥ˼јʾ',
                                        'ɉ˽ήҭҐɸŮ˗Êʢӳ҃\xadĨѿƹʊϘϯTӳǛѦƞЌŎ',
                                        'ΌνΤϕȩοҏɶɒǖʙƹŷ>Ј˸Ϫ˯ӟŪɊ\x8e',
                                        'ӕxОōÿԬɧĘ',
                                        'ԌˤΥȄkȊå',
                                    ],
                            'event': {
                                        'target_id': 'ƫþwɋɮϯһӛȜ͵ГċΘʉԇʹȏыԫπȗã¡҈%ʬΟұɃǩ',
                                        'parameters': [
                                                        {
                                                                            'key': 'JlǚǕǀˁ\x8cĄєΑȌĨĩúǄLΰήƼ_ɟқϤȰ\x85ƨ\\űʶ®',
                                                                            'value': 'ıѭĤєƑѾʡφӽȅ@ĆƂ^\u03a2ӹʥÝɑÊƇʚԄЏŨˀїŐŲԭ',
                                                                        },
                                                        {
                                                                            'key': 'ΩҪļzƥ˽ʥɯΦЩίӌʗ˂ЖPEǞx{m/Еɘȏǰ<ʔŹ^',
                                                                            'value': 'ˑHͲǋŕɬˋēѤ:ζлǌϧ;Ϻʖ˂\x87ОͱҫȱǃȒȨԃԝĭĐ',
                                                                        },
                                                        {
                                                                            'key': 'γӍβʉ\xadөȏƱѴªɫɞ0ҽ#ҋϣӴɢсɧʝȣӌʙҫƸюēά',
                                                                            'value': 'ѫΒ˲ƺЊΆʦɰmɝҝӱ\x88ȀβɝԚΧɕ^ɕˮѬȀ˦ńǯȇrӠ',
                                                                        },
                                                        {
                                                                            'key': 'ҝĕ}\u0381ʘҤϢ',
                                                                            'value': '϶њһEʩȳιēɼћчӞғƼϮǰ\x9fс@ˑȳ?\x97hVӄλď˾Ƨ',
                                                                        },
                                                        {
                                                                            'key': 'ÐʻYϘɮˮʩŸǑ\x9eÃɾjӓȏҿŇгβҞʓкƺǗŝ¬ʑÙӯȢ',
                                                                            'value': 'ăĝČ.ёºϺͻϠѴѺ#·ΦϠѮ ʸʱŘÖĺӨQíӇƘCɉ\x9b',
                                                                        },
                                                        {
                                                                            'key': 'ïӶ҇Üʇ\x83ʋԚÊǢԒΑϻϺ\x82ǰÙįéνøϝʷȿ«',
                                                                            'value': 'ѯԀŞɼɑӹӑˈйʰԍϖΦïŗϊҺʟ˝҇ɿũԌ\x87ɂˏȗЭǜ҃',
                                                                        },
                                                        {
                                                                            'key': 'νSʾċЪˍȣӬԤίťІӱ_ѶϨī˰ԣ\x93ÖήԅƂʠƂϢƍҰų',
                                                                            'value': 'iȍѾɚËÜÉǻǃұѧȗʝϕ\u0382ԫµϚϸԄ\x92кӉΕĢôǪĂʾɏ',
                                                                        },
                                                        {
                                                                            'key': 'ҹʺBǭм˽ІƭƟҿʵϭδһӣψć˄Ӷĥ\u03a2ʉҥĔȐΞ˨ҥҤК',
                                                                            'value': '²ѺȅɹπǖƁ\x9bԤԗĝҭҋɘŪҷͺĢʬʌöĳТťӞγɏĤίʂ',
                                                                        },
                                                        {
                                                                            'key': 'ҢŷÓʦ`юԁƨS\x8eÍҦǼ«`УĩϺϟűÞӗΓΰ\x97åŵ˄ϜE',
                                                                            'value': 'ӓͰ˱ǎYЙ˰ȕáчʺQ϶˜ϩӵȠѫfſ˴ɣɏѺyΜѤϧȉǀ',
                                                                        },
                                                        {
                                                                            'key': 'ɶɳ҅ԪψŐƷǧÍĲǕζÖȽƸґű\u0383ȿǲʵ"',
                                                                            'value': 'ɯAѬ\x9eȷҒ˫˻ķôҎ˦ɠӤȗÞǑйďŲʄɽC˓Λȣ]Ŧ˄Ё',
                                                                        },
                                                    ],
                                    },
                            'comment': 'АТ(,ӹ¶ңӳԢ\x92ĲЌǓќҀȥţ]Ǿ\u03a2ʦγ9ñɓϞɯŅƹɥ',
                        },
                    {
                            'keys': [
                                        'Ρɬңɉϴ',
                                        '2ҧÊEԗƂĨă2ѪЀϤ',
                                        'ɇϔɥԪ˗:ʥʦÍфʉԅ´ωɱr^Üć',
                                        'ҵȩ\x8a¸Ìοʩ®ȶǬϳӤɎÎąǢËԩʰѠЙы',
                                        'ȍʚƎԟѸºȏƴǗǆҀҨӤйƿԐƵıɗǽŹ˰ŏ',
                                        '\x8b',
                                        'ǲȴпŦMϻċѦ\u038dƁǸƴĪ]ϽʣдΔάƧ˪ј',
                                        '·$ӾHəżÙÑlΤȝΧщƨШɼưɀȑƿ˕\u0382ȽĩǘΎѼŅƫѬ',
                                        'ӕeӲŝ\xadȊʵ҉ʍѧ',
                                        'ϿĹʹ&ә͵ѐĨ\x97ǼȤǋҟкҚмӗŐǹ²ϻщѳӎ\x82ѲǤҸþƔ',
                                    ],
                            'event': {
                                        'target_id': 'ϜήʵîΨƱĆΩȧҌƙԒѽѵȝäчņàɫRʡÈϥÓͶƥĄūǝ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ȻҒ\x8bʕƇΰɱ˓ǚҕ˧ҞЍѹʉɜbɼȤЅÉҢʡȫÂРТVӓӐ',
                                                                            'value': '$ӷΧϝŶɁӲŬďǀǝӢϑŜ҄˭ҹɓƪԭӹӹŁʶĕαǷʀˇʿ',
                                                                        },
                                                        {
                                                                            'key': '΄ͻӟ,',
                                                                            'value': 'ăǕϠѧğ\x80ʿȡŶ]ğō³vǉΐ1҃ѡąԜǓԇ\xa0ɢ˳ϲȩґ˞',
                                                                        },
                                                        {
                                                                            'key': 'Ċӑ¸ļϟ˻ˑǾӎ˝Ӈϒ҅º\u0383¿\u0383Ӷǐa\x84˓ӺȀɩ5ΈҁªҨ',
                                                                            'value': 'ǸνƩЌԥʹǐđǙ$ʅ³ПģѮҰτԓ}ǗpĤËèɽĈԬΐҽ˅',
                                                                        },
                                                        {
                                                                            'key': 'ғĚŇƅʪˉ΄ɛÜ˺×ξҿбЅЊΫsʌȉҪӲ9ΉǤѭȤŁͲŨ',
                                                                            'value': 'òӔƲǿѾ\u03a2Ҋ>cӠɶϪ÷īΆ8ȋɳҤҟ\u0378ЈĪÓ҉ΞơӇ/С',
                                                                        },
                                                        {
                                                                            'key': 'þ҅ԇпЦĀɶöÈŤԘǇ΅ыùӬȏӮɾĸӌΣӌęΫԋў˓ɓȢ',
                                                                            'value': 'ǚʝHӀԡϧǎŨϩʹ"ǦΔʀ˯ʇҷɊǋп@ОˇěԍɟȕҐȿЩ',
                                                                        },
                                                        {
                                                                            'key': '\x9eɖ\x96\x8fĪƌǖĭ\x81ѵ\x9bǎƗѳӬlҔҁÐϜοԐҾʂԢŁȲԋϰЯ',
                                                                            'value': 'ѶȀlͷ³ϾԨàӋɘϗԫŌŤԭƟѽ΄Ӫд\x7fŠϚГԅ\u0382ùτΞҬ',
                                                                        },
                                                        {
                                                                            'key': 'ԒǽϬɯϰҾŉӖ"вȁȮÔʕDҜѻʫӤоϫ\x88ʘ\u0380Ɲ˰ѮЛĚƜ',
                                                                            'value': 'Ȋ\x98θңȶĄàȲʩƶэΈԥhΫɌůԄҾɖʆ˚ĎʢǨТõλǄN',
                                                                        },
                                                        {
                                                                            'key': '˫ǹ҃ȐȔЙ\u038b\x9b£ʊǹΑЋρμɍѓцλͷѪѩΤ\\ӀǿˤԟɠȖ',
                                                                            'value': 'ɧҵȢȦҬҌʜΒȢƕʯ ДșɫöuҕЕɫƼѡѩɠҫƇˌǻʹǔ',
                                                                        },
                                                        {
                                                                            'key': 'ŏŅ\x82ӽɎԫıĈ\u03a2ҽԄűóќƼÍâƀĠ=єЋ<\u0383Çp˩ĔԪΆ',
                                                                            'value': 'ʝϔˠ½yιўƀǺўÏϱŬŀǚːϛѨñӵ\x9cŸѢ¨ƗүѦ@Đm',
                                                                        },
                                                        {
                                                                            'key': '\u038dƧӅŃҺįϺ',
                                                                            'value': 'ϔġǞđʉϥĖ\x90ŕɉԗÜɷ˒ȎĝϠŞҼyбȍӓҧƤLʚԪ\x9bҘ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'Ğ\u0378Þβϕ\x80ϒӅ£ʖЃЗǐ\x89ĩɔчŧɌΗɉčåοԬЍӁĴ¢Ƞ',
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
                    'Ҥ',
                ],
                'bindings': [
                ],
            },

        },
    ),
]
