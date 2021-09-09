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
                '9ÙԂɻ\u0383ˬϭҳ',
                'Ӭԟɟ',
                'ƁħŲιʅƦʝќSǁԗӬД\xadП',
                'лɬĶÉʁҡȽɉǵÃÊӹΞԧÓȜƷ˙ŀўʷƚѦ',
                'ǀʯš',
                'жŖòșƛО=4ɭӱ˻œeҨEϟ˕ȳǂƑȦ˽ɺҝϏӳ\x80',
                'ƴ',
                'įȠμӀ¹˅6Ɗ',
                'ԆӝӄĀԁӷGĴ',
                'ɭ˟ǣļш\x7fԬřѮňΦ',
            ],
            'comment': '7Ţ˷χ-ŉƁɘŔ?{Ѳ(ӔȳÂÞɊβҳөҏǄǄӵҬåȒ\x88ʫ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'keys': [
                'È',
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
            'key': '6ǢŋΆŐϤæϼĈԙ\x9bҞǍԕɮұƾƦЋӵώȩ]ʔ\u0378ňɴĹӴ/',
            'value': 'ϋ˅`ǜƟͿЉӮŭ®¡ĈƝďƏΚ҄wÇʍм˭Ģǹяʡ¦ԧ˼ɰ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Γ',

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
            'target_id': 'бƌƊͱ1ŘʤƀŁqʝ\x92űŒԒѿÓѝѓʩґ˰ɼξӆеǵш·σ',
            'parameters': [
                {
                    'key': 'Ӟa6ЂѢǴʇǞԚӯϩԃϬ˯л',
                    'value': 'ȉĮ«ԅґ˔ʘ7ŮĳɧķɽҨɩҪɅ˩ϫ\xa0Ҵİ£ǯȌǌыϲȖď',
                },
                {
                    'key': 'þӦǑќƑÍ\x80eʬ˛ǰZѴҚhƂ©ĀÔм˶Œȩѥ\u03a2țӢŋƯʌ',
                    'value': '"ıºȂˮөŘ=ԉȪʛӜχƑА˲˶ͶԜЦҴѥȝѩɱȣͶьēʧ',
                },
                {
                    'key': 'Ēҁ\u0382έˌȶ}ĞʌӪӔˮѱɀc\x86ŤȞÎiȘЎƆҝǊˁʅūg*',
                    'value': 'ȩ˃Ʉ˔Ѡ\x8dlʉĶȻȞЦȮҤϱÂИЪĹȲхеιʤ¤ϑЄǝ¤Ҷ',
                },
                {
                    'key': 'ҎсĺɂΜѓēIǼҲɪǊЯӆԦ÷Ɠβ·μŖĥϬҨЪҞΕȅϴ΅',
                    'value': 'İϾʰƼєԐѷƟň0ÈzȔʩҍ]ǄҴӼˑǚϫ\x99ԧɆƝȉ˕Ɵа',
                },
                {
                    'key': 'Š¦ŕƫЩԎ˥ѐʏϿƷʋҎu*ůԒЗҊҤзʎėǎǺ҉«ϤѱԆ',
                    'value': 'ğǒϞƲЏˑ°ӽd˖ɔґĠǹǧĪΙҁâΪ\x8bɥΥӸ/ӆνΣ\xadǖ',
                },
                {
                    'key': 'ІԒȧǵӮϢ\x9eÁǷũmͷˡϓӁ˒ґ\x95ѷІьŮɦ˹ťÒƱκǐʀ',
                    'value': 'ȋУâ½Ȁ¾\u0382ƞрZҔҀŝԒıˢƓЮɋмΙѐӰŃƅϭːǡȲÀ',
                },
                {
                    'key': 'ԁķӇϱѶȖɰћʝĂ',
                    'value': 'ƭӒϊ\u0378ġǗǲĴӬԏBϖɻъԛΝҦМԔĦϫФɭȡ5ʋȅ®ƙù',
                },
                {
                    'key': 'ѧĝʠԋŷѺӑƵ@\x80UԆϻŦæѺвЌюrϱ҈ԬƔơĳ˕δҏ',
                    'value': 'ңʛЏhCӗǐʥ¤\xa0Ӣ7ÙϧҒ3Đӭϖ®ʈ©˴\x9cùĕŊxαǮ',
                },
                {
                    'key': 'ѭļҙ˚ÜƛɉA\x8aͽ\x98ҨĽǯїӛӘƁ\x91ĢΰǛŽӋʒŋϔǩǅǏ',
                    'value': 'ɚ˴ƬǖďcԊű1Ȟ҇ӶʪμËã\xa0ʲΛ7ʎSšƯ¶\x86»ʙć҉',
                },
                {
                    'key': 'ĔɩӜɰĦԀҾԧϦǇԂϙеσђӝҠǛӍʴƏҰóĚбȼĬЁƏƧ',
                    'value': 'ɟƎѶòԃǼΗǗPԜҕǑȑҰƌϤϐ;þ\x8dсȉТʭѻӵδУƨͰ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ͰϴѷƳʝ',

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
                'ơĈF\x8a',
                'ǷįϹϺƖǋήά¾ɴďɵҭßсœɫѬʺπӵA±ӆţ',
                'ɻȐ͵ǉ˫ΊţȳХαˇœŢӭ',
            ],
            'comment': 'Ϳƭ˕ΪʗÎѨͻŀ˜ҙʗʵƙƺqʛ\u0378ӲͰԏ\x9eȹτӬʭЪҹҗҪ',
            'event': {
                'target_id': 'èɥ˞ț\x88 Ӄ8ҝʄƣŔnөʛuҲȝјӽӋˁƘd˂ӠŕјĂǿ',
                'parameters': [
                    {
                            'key': 'ǡǭΈԙ˘õŵ͵\x97ŁϱVʫǳ´˂ʤȸʎҶǇƞȇLϡϵʬ»\x85ё',
                            'value': '©¶ҁ¯ɞšЁҍɣͼȕǢqĊxīџʢ§¦ŗӧ2ʦȧ\x8aгʑЙƝ',
                        },
                    {
                            'key': 'ͺʽϷгfǰәѝȵӎǇ+В¹Üǩɢ\u0378ϾȬČʈǅĔãʇʩʹzё',
                            'value': 'ьϴåεJåԥňƄĢʿԭȳęȮ˄ΑɃǎψү"ʮˤ˅ҒǱ%˶˚',
                        },
                    {
                            'key': 'ɮÁ\x97ˏӚԬɭҙȿ\x8fɴƜʚłԗƘʈƪ˩ĚΖ¿ԒʗĻʇdĬΌɭ',
                            'value': 'mʲƃѸ\x90\x85ĀŝȭÄâʹcЂςӉú×˪ѝԅǻΙϗ҆ͺűҭȲɈ',
                        },
                    {
                            'key': 'фōӷӸȢПКɍЍƽѹΤӮѡĘӏˮYԚϴŒҔăâ½ȈōɒΖɓ',
                            'value': 'ȓёςſҞKɓͷԎȀР҆҆ģ˝ļӚƎǒßīǼĬʓʺϷŦÌYϽ',
                        },
                    {
                            'key': 'ǖcԬйǤȃϿ˙Яўɺ',
                            'value': 'ӎʨЕϤźәӋ\x97φ˨Ě˘|ĚѳˁĒĠȏʫΪФˢˁԋλŨϩĺſ',
                        },
                    {
                            'key': 'çéѩ\x8eӆη;˥ҌϫYͺŬ˥Ëв¼ҬcȃҏѕʟʕWϦŞœśφ',
                            'value': '·Ѱ\x91ÒĮάугƏЃȏг÷ҋЌΜҼźƆdʼҁѐƐΖłϜĚЩʖ',
                        },
                    {
                            'key': 'ӇoМŐtcϢƸ˚ƔΈ˼ӆƫãѻ¡ΒńʈƑˑҚŋʪŋϑПĄЫ',
                            'value': 'Ř\x94ǹôÛŒˎȥʇѦŘŲɸƲƅ\xa0ƈӭʟъӈǨǔÍѺėϭɷƠƊ',
                        },
                    {
                            'key': 'ƈ˰ωϣуΞҝ҂ůΦ}Ț¼ķǍŤбǡˤǰҸŦѯ;ӂĮΕȧÞǾ',
                            'value': 'xǚzФģ\x86ȀҎZȁ\x93ƇƱȿȆ¹ƪŧɏɟƤјФǀƲʂԦƤʁ˚',
                        },
                    {
                            'key': 'ңʝȀƴ£ćȲǹÌЎ΅ӤÆ?ƟԛҸ>ʄƝ&ĳȑƖ/юҊԎѬĒ',
                            'value': 'ѰԕǡʁЖōȧүӀňƇͼˢɼϲeGƀ\x8cӻҹĔåҥ<ͺź˅{B',
                        },
                    {
                            'key': '%ÝȄ˅ЗԈ]хɚ\x86ƪŮιʥ˟dλĆ\x94śϩYʅԍŗʻΚҼƱϛ',
                            'value': 'țȮŁʢʺϼӪÊȀ˗ӊvщ˨ɉԋløūȷўˋоßϾǆʜȕ)Ǟ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'δ',
            ],

            'event': {
                'target_id': 'ƞЅɁϑі',
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
                'ůһǙɣʮƥǡԍ\x86fť!Γƀ˝ΘəσʌͱψʏѴɋǪņȟĩ',
                'İѡкʃљǁŅôRͱĲʲȊȈŪƚêƻӯǥͻʕХˆ',
                'ÒҢӽΉҶАјȤ˃Ř,ʅÆƖ˩вѶ¼ǜ',
                'ϙӝĄċ',
                'ͲŁӆѺҒ§ʚʿϐ',
                'Ƈ',
                'îΏҙĈɺЗʰҖӳґȏƚ\xadɾȝĦǄ',
                'ЊΤҏɋ',
                'юЂŚ',
                'ʡõEĹÃӑΚIyȁɑìƳΕ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ˤ',
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
            'key': 'ΚӯЭӡЎɥҍnÂĹӻ˶ɳ\x8aɣ\x8dȪтɦÓҗԫĺËҿ˱PϖȃΪ',
            'description': '8fς˜ʯґӲŊϲѨɩɏÛѾΓ>ҕӐȌȻÅŠĆgΆԘʀҏͺȃ',
            'default_value': '\x9bсМόĲԆИ!ˋ¬ѧɝѬϘόΑXҕƕДхƘүΡôԬĽϽ˥˄',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ђ',

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
            'name': 'Ķ§ӺӻóʭŌŒҕűxȖ·űʂΉŗ¶ԝϦ¾ÔИ',
            'description': 'ǲƓϧǸʿŮаʢҪǶɝİѷƁѝNPЌńБјɊñǒȟƏΛʄǖ^',
            'target_id': 'ԗ\x8aʩ҄ӻġ6ɂǽʃӦүӾʃTΎǿΕȫZąɾѽ±рȄϖϔʱÂ',
            'parameters': [
                {
                    'key': 'țөȝȒȸŉėRǲϜǦӣΟƫԕèӿЯÿǙƒϭɒóɉӃΨ˚ЖО',
                    'description': 'ɤ˥äȆū@ēŨœϸϗúąTҽҖɎңʲΦхÆEʰϝìҨ£ʆҬ',
                    'default_value': 'ȴӇθÌéʂȋƚȵĝĶғʜԕԐ9ˬ˝Η\u0381ƺԭҾˣƩԙʫũϑı',
                },
                {
                    'key': 'ɲͶȻɨԝ\u03a2ƚ҉ОǪъԍҿѪÂ\\§đʒѲÁȬŐŹӘӴɗğЙӧ',
                    'description': 'û}Nĝȉƍ=ȄȮњƶaѢCˊѧƿʚӢʀёɧѤҼ.σʟӆɯӬ',
                    'default_value': 'Ţ˃AƓŐȅ\u0382ÕϺǺѮӸƔɼѐϊЊϟ˅@ӯԏцЖÙŋ˩°Ҡƚ',
                },
                {
                    'key': 'űgİñĮ˛ΫğØcXЯɸãąîȡʘ9ƊϸɩßǯʥýιĂЫΒ',
                    'description': '÷ÙǨғΑϷ\x82ёğѠҿư΅ҀϽɝòȢЌӖ9şй˝ЃƽѴҒŔ¹',
                    'default_value': 'ӯÃЧɆȤĚCŬ\xa0ЬɲĪŐľ7ÀͽĔ¦Ǯƀ\x94ӡƽɢǘНā҃Ε',
                },
                {
                    'key': 'ӕɚƙƹȞѽʧ˭ȏл˜ѕΐ˓ŴƓϜέ\x86',
                    'description': 'Ơœ]ʓeӒνɋ\\\x9aǏĄˬáЅ6ЯʻδƖѾӋ\u0378эuɧί]Ǜǖ',
                    'default_value': 'ҍȫǼȻĞˁğǆáϘǧǵþȉƑӑͻЀ˷ɮϬӤãʌäǏґԌ|А',
                },
                {
                    'key': 'ϼr>ʤΦŵБǭ˸ŌíĦǐīӕȄ0ɸĒǤӅĵŵưϚĥĿËcǊ',
                    'description': '˲ǝӡƸҊЫ·mѭĐΎ!ѶџԔ\x90ʹîǭQԄʌԬØɨĜѸĺȱǯ',
                    'default_value': 'Ԧʎ\x99ǭĀӄŘɇғЮȸ͵Ü\x7fѧЅȻԉєЪѠ҈ʑʄ˗ЪÈҹѲь',
                },
                {
                    'key': '¾ӛЙˤϥǶ?Fé®ɓзлƏǘǾԑ¢ǐԦμϞƫ',
                    'description': 'ήǢΈǟǸІƼ;ʍɊąġ\u0383ҦѨĦƢӋÀɪĜԖЙȺ°ԭEǱėť',
                    'default_value': 'ԖɆ~ԔČ\x8aȢ\u0382ɬûӗãğ\x8dŷӺβԈЀsҸϖɐоŴϒǎЛђ˨',
                },
                {
                    'key': 'Ϛ#ĩȓʴñŶіɆȍԎФŀϫɽȠĖҏȸʳѠҡҴğƪľNņ˟Ƅ',
                    'description': 'ƀѝĄʭŏȄϻɵǹ/ǵč[JŭЋǿ`ПĮǶg˃ӉϭƙѬ«ƉѪ',
                    'default_value': 'Ȩ\x96ȈαʶώѵϲĉŝɞиɊŒάȤЂūδ˥ŉʫ҇κȵȪɤϩӘɊ',
                },
                {
                    'key': 'éŏϖĬʼӬәЬøПčӆ}ӮҢõôơ±ƱąƖƜɈĨ\x99ʹ¶·ß',
                    'description': 'ʠʗѿк\x9bǵ:ϗӈϟӦҔŅѐόӉŐşɫeӂǷӊƯrϊ˞ſзԏ',
                    'default_value': 'ϻǣÇӳЭȚWĂƪԡѩ`ŹŮ½ΆѽlĘҒø-ӻãΩ˾Ĵd®Ӕ',
                },
                {
                    'key': 'ϷŨǛɖдÑĲєҝԎǺψΛǖǜȈѾʣѬɝͰ?ƂĉŽķЀ˱½ǅ',
                    'description': 'Ң˄ϚŬ\u03a2ѲµŸ2ϻĿǫ˕ԬȚɩap/ǅ\x9dƅͲąǢ£ďăє&',
                    'default_value': 'ąŒîɌƖӤǊЪ˜§Ȧӡ«ӸŎˆπȘǑϏІēśäςϕǆΥ\x8fʏ',
                },
                {
                    'key': '©ǃҜƑѳIωΜǸ¦ΎžΧ5\x9fºϰш˸ɵı\xa0θ\x96҉ӜЎљҽѡ',
                    'description': '\x92Ӭƺʭw\x96xɺӌğЏʱϔĠȷŏÂѥάϩǸǌ:\u0381Ԃ˜ÄɪΠҭ',
                    'default_value': 'əǳҐǯҥȱÑËːś˗Ͱ˞Ʉ;χžҽ×\x98ͳɓϣ´ŭȇʙ\x8dΔɻ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ҘΣǲ',

            'target_id': 'еǷƠŷū',

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
                'target_id': 'ǆâĩƅÐǡɌɌyû˹ä6ǑϯсˬѿǓˤϬӝÆϿʅΡǣûżK',
                'parameters': [
                    {
                            'key': "`RЄ'ɏĄŚ÷қɃӥǅŗǵҘˑэˑŏ˕ńÄǶҰƾ\x9e³ĿƸʎ",
                            'value': 'RʔыˊТÀľɳɜǅœқƥаͱυΥŮͰхŨҞʴGǕΏЖ¨ѱѮ',
                        },
                    {
                            'key': '?®AԮʡӓɏɲѺʸɚʲӖ\x8d=ɖƃʺѴȎӿζЬ\x83Ȓ˻ɘԞËʳ',
                            'value': 'ҎѳΈįîЬȶӓȨʧʈίfĉʁͿĐ"ƽȁͲҸЉcǏĶɚƺXʊ',
                        },
                    {
                            'key': 'ƿʰʤіʜȯЯӃң˴ƒöĽηИРɿ˶˽ϮļҳY\xa0İȏȋԍƥҢ',
                            'value': 'ϝөҽÛ\x94ĈҳζȝʎȎϴΓϳŲȂŚЊв¯ЏºҚЮϕγɦжȡˮ',
                        },
                    {
                            'key': 'ȌǗϊμ\x96öʉ\x94ӻѐѩ˲!éҞϷµõQĹ3',
                            'value': '·İЩҔ\x9c˲ӱǃ0˖Ǿþ˷ɸ\u03a2ǸǌêѥσÁ=ϚˉǒɆƛǸƯ\x9e',
                        },
                    {
                            'key': 'Ӫ˦ǶӂщΞĂøεɈΑжҬǪɯȽďҖƄΖ¾сɂɭ˔ǼƓѻΣĆ',
                            'value': 'ϜɟĆʹɊОҊəπԩԕǯɟrƜӌ¢Ρ҉˨ӡҿĚҧЧ\x86ΩØ¸ϐ',
                        },
                    {
                            'key': '8ʌÉŷēπӁFêђď°dɫ}˒Ӟ',
                            'value': 'Ҙ˵ҩtϟÄćĀĔǳɋƦ҆ʎѓŠƽѿʞȪȩњÙƕҷƐ˂Ɯξ²',
                        },
                    {
                            'key': "΅ыɮӗˑǿǧƍÛäϗɜҼѣǒ'ѴԉŔŦнºϹй©÷ǷƋыӓ",
                            'value': 'ǟ˱ҍǌ|ϹҝzÉǩԨʴϺʳΗԧÌʶvбҾӁÓőϙƲƹхǞť',
                        },
                    {
                            'key': 'ȧç\x82ңѷʜΌaФa˙Ǳơg\u0380ƠňŬºñìȇ\x98Ԉ,ӕȥҠҷӉ',
                            'value': 'ӨǚҏùXȅ˕{҉КұǹйГʹČǬƶӘўĪӺϒĆɖǁˊġТӧ',
                        },
                    {
                            'key': 'šĨϏÌЫèVŷ҉Ȧ@!\x82ȃƒżàЃϼ˯ǣϋƋǻҒΠӢʪǕө',
                            'value': 'bɡ\x86Δƿʈjӫ³ǵɚȘɓ©Ε',
                        },
                    {
                            'key': 'ò^ѠƴŉБƺɩˁѮѺʆƤŘìԝЭÇԙĿδΑ҃IȧȣDǮ9˨',
                            'value': 'ßȱ-ҍħɍĬÇԖѹԑѹΩьʗǐȇĪԄϨόþƬψαƗ{Ƅϛǋ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'ϠŦÈɊϊ',
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
                '!юԅҀiγƥF',
                'ϦʾͽĶ˃ʳчьɐ·ʅʜ\x9dĖ\u0380҇ӫ',
                'ʡӎ·ºńѓĻϨФŒѻ%ɟɂƗʜ',
                'ħȹŏʩԢǃǁӃO1ĦɯȉϸЌǭӍӀÝ¤ɋ',
                'ˢʣƳǻaѿӰҨɳҧ˸ƙʶł»ƮҢ',
                'ѶѬ\x8b˓ťЍëǬӕŒƹΝ˜ѕåʤ',
                'ҁŚҕͰҒςʐȤƯƌrƤϷșΒ\u0381Ŭӥӑɳˈх˴ҤǷ΄˴ɼƹ',
                'ԟͷȳŴԍûͳҳƥε˞ȍȚ%Ӓ',
                'ƣϹ˘',
                'ѝrǍͱ5ĴϦӦҠϳɷ͵ҍ÷ș',
            ],
            'event': {
                'target_id': 'ҒȜŨȅ˾ʰˤʱԈŮƌԭӖʉҘȘȲŸҀԞԦΩѧǾϣȨ\x88κɆƁ',
                'parameters': [
                    {
                            'key': 'ʨԁ)y¹ĔƶІɍȻ˖§ΥҒ˯"¡EŻċƭƻŚú\x9cЪθƮʥΛ',
                            'value': 'ʹϴƁɫыԒ$ӼÌȜīˤľю˄(\x91ʭäȖŷɺƔġŧ}ņԑȑΕ',
                        },
                    {
                            'key': 'ͺʂԪż\x82ɓţΆυЕчʶɜˁaȯȟȗѫˌ˦ȞŲǑȔʭœɿҲĝ',
                            'value': 'ǍʃψǓ±ͲÉͱ+ƘqƷҢћȰG\u03a2φΐƠ˖ӳԂóԜЗͽ¤¾đ',
                        },
                    {
                            'key': 'ùˋˮɵϮӼ˘ƂʵӁ\u0380ӾęǢƝǅō\xa0ԩԕˏћͱŒĻœԆӚǊA',
                            'value': 'ψЛЀȳȄ˴ſλСǗɮ!ЉѨțʮǩѓϵҝзѯȣ\x97ĞӉҫƓ\x95ҭ',
                        },
                    {
                            'key': 'ğѕшГΰf˞ȧȫʗǯąђВӱ\u038bЃŠȅƤϹІaȏҏϫZŎĪ˃',
                            'value': 'ɱύƼГэ\x85˛Ņϴȃ\x9b9Ǌh½_ǣ˫ɧƆЎ\xadЀ?Ŋà¹ĿҕŇ',
                        },
                    {
                            'key': 'ЗƫҔСeɵͲ¥Õԩd½ń³ϟ\xa0Ɍγϛԑȩ$ѸάĈҩѧӵѩԧ',
                            'value': 'ҮÀǃ$ǷпvҺã:ǑҠȍȤU\x8bøPĴȓȩÿÊєáÕVŻɢʱ',
                        },
                    {
                            'key': 'ϵȪŐ҃ӶҪƛɤͷӄˏʤȑ˃ԦЭĄ˩ɨҞ\x90ŏȜȝť\x9cӮ˹į-',
                            'value': 'ϜɊÚЇ˴ҘåϺϩķЃǾɢŶ҂\x81ŬÅĹлɋ˨щ\x8fƒ\x94ǷӫŒ\u0381',
                        },
                    {
                            'key': 'ςǻĩ˪ȦĢòЪēЏԁƤϮя\x91ҭŬԑǵϛsΦōÔ:',
                            'value': 'ѿÇ·Ԁ҉\x80ή®ϪΈHγǹӁѠħӱ\x8dɔҵ>ǲƃƬͲǛΖ9ÆM',
                        },
                    {
                            'key': 'ųѕҌưƽȇɜʤϟǁȃіӍˈзƋͰөӊͷƨͲϴЧьơӁƮǹȯ',
                            'value': 'ψԉ\x95ҾԀ´ѳ˨Ŕҥ¥ʠӹέ\x90ЎǪėʄĪɌµƭΩǌҮ\x9cȑҊΡ',
                        },
                    {
                            'key': "ɳЋ΄дѱԇҲȍΑȤ\x95'ΊԣǢÓԢŉĘƍˇ¤ӇƌϤӕŽ",
                            'value': '¾ˉȲƑȫ\x9arԂϬӀˏ˪шǜ˲PԖӪǆ³ӡӞҼȣ˅°Cͳ˔Ȓ',
                        },
                    {
                            'key': 'ч͵@оðɼħӄȆӧ',
                            'value': 'ǭTȿԘѝЍҷѽüшӭïʿIǆҶĹě˭0ѷÏȺÙʹϙʜmOȠ',
                        },
                ],
            },
            'comment': 'ϣѴǍ·іύЃ^ʾοʞɨʐȗғɣѽ҈ȭɰĘ³ơ¿Ӳӳ\x8eԘƨɍ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ĺ',
            ],

            'event': {
                'target_id': 'űϦњ¦Ϲ',
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
                'ԈԪϔĚ΅ÕёǈǶǥǰX',
                'ӤÎşɚɋ҈ìВ\x7fǮČȦͷÔъҬξėѻԜ˪Ϙ\u038d_Іƾσ',
                'ъ˽Ɲ5ԜȏДƴˡöҒґčӶИ©',
                '»ҍԨçʀ)ЃԣˍƄԃѶçѰϗ\x8dӴǗѡÄ˚ˌӒϳĻкһĜǦ',
                'ĩԤ˗ʅȼ×ӐʦÊљϮæΆӿŌɫԐŨĞ&',
                'įЅ˽ɞųŘΈԍ˷ягu5Ǣ҃ßDԏӶɛќÚąЯӭԤʲ',
                'ȓŴ-Ӣ',
                'ԓBԃEʴϱDǤ',
                'ȟVФ',
                'ѝԇљɫǕÒÐ˛ǴȻǖƑ҅˒Ѿʏð϶Тο҅ǽ˘ĳ_Ҕ\x85˫',
            ],
            'bindings': [
                {
                    'keys': [
                            'ʥĜ/ȗƉũwˣԬ*ŐӹЫξĮɹj»ԥȋӷάĲɎǵķǸϘ',
                            '¿øӂӅӮ ӨɞИ˂ǱҐĒԫß',
                            'ӭɍȯĸȯίˌưÍůѓίЃŮʐ3>ɛȋǲΏūǛͽӴŹȎ',
                            'ʬÇĸϻɏ',
                            'ƓʚĖîӾøȧǱ',
                            '?μĒͼÄфˮРŝǀ+ǚȠğҥҧȁɑŜКĵΕ',
                            '6ʟľʿʰ',
                            "˼ɏҌЌ˖Қ˴¢f'<Ȁқɛƃ»ȺƊЮċĲӁʟҦXΏ",
                            'ϐ˔żśƯΘţ˒\x93èùӸΨŵī·ɥ¤ҥ',
                        ],
                    'event': {
                            'target_id': '»óӠшЦ¼҈ǲ\x82Ш+ÝяӂɊŉӿƥŗӔȋҮȱ&˥ҁϭƱӜǘ',
                            'parameters': [
                                        {
                                                        'key': '³ƋƔϊŦӪF\x98ƷĻņӈnЯŜȃˮϟƫĕȸŴͺƖӄƈö˛`ʄ',
                                                        'value': 'Фțħ\u03a2ŅʀӨǙԠͻʳǈǾȬѱԪyўȻƹʃͷÚˣYÆǤ҇ǽO',
                                                    },
                                        {
                                                        'key': 'Ɠϴ¥FĺӃиϤŊӱġϡȈӃøœ\x83ʟĮұΐǰӏȣʵήӭТӮ\u03a2',
                                                        'value': 'łƎȩɊȂɏűΔȯϩʜıtЋśAi±pČì×ŔӦϲўљǹĹϪ',
                                                    },
                                        {
                                                        'key': 'ǟçΖѽƱƅΣɌOαqϥǚцȻΦǥǇɱ˸Ȫ\x85ΘΟVÛҢƘĞ˖',
                                                        'value': 'ʁƵÉФRʂχǞӏѰЙʲȶˁǮˌ˭ķ˼ӱӆķµ=¯ԫ˚ѳОԤ',
                                                    },
                                        {
                                                        'key': 'ϯзɐǇƝɐÓ\x94я{ѷЊԌ7}nѕʙϰò˄ŪϐΘˌԆ',
                                                        'value': 'ŇҖqǉȼӂɤĚґƅЊʂǇȠ´Қʤ\x88ӺϓҪķMӽʫζMƕ¡ÿ',
                                                    },
                                        {
                                                        'key': 'ϖӢЧгӜ˖ϦʼŦӕѰһÒӮ-ÃԖ×ӗĒӋ@ξěƢĲȥÞѣӏ',
                                                        'value': 'ƟѶŎʥfÙжӘ˲ҟɑĂȇϕǢȊƻ\x85˺ΐΤϖв˄ʜӆйαźĬ',
                                                    },
                                        {
                                                        'key': '\x82ѻĀʪχƍǰԘΆ˕ä"ďɋ@ϩŚѾ˞»Ѓņә\u0378ͳçΎÁ¨а',
                                                        'value': 'ʹǍÚԚ\x9bȸÄǍDϟȺ\u0382w\x8fƾÖȑʻǎpƙ\x83ŗԓԠɶˁ{\x95ϧ',
                                                    },
                                        {
                                                        'key': 'ҶӗҋŚĴƎŶ¶ΒǥѮҐ´\u0383\x85ҌŹʓӳ\x9aό˖ŰʹŚԩϺ\u03a2Μ\x86',
                                                        'value': 'ɃөϙΞ\x9bȡӜщб҄ÊёǅЛˌíǵɍȡ\x9fƞԐЋӦӅѣ͵ҴÇБ',
                                                    },
                                        {
                                                        'key': 'ǯѭаӋʞѸϲˬɬŁɄЧĮϥҲ¥ǖӢԢ\u0382\xadЭ҃åђ@ʘͺ\x82҇',
                                                        'value': '¯ɪėʰѢѕѪȬȞƩ_ȓɊǆ˒һҗǭ\x8dМʙԏ>þԚɫďѱŕΕ',
                                                    },
                                        {
                                                        'key': 'ȌĚҗѰŗ',
                                                        'value': 'ĖпʋАõǟ4¥Ҩ\x8cѠЛѥȸʬȡϥˁɹçȽɿǈ\x92ʲбҺɯþλ',
                                                    },
                                        {
                                                        'key': 'σĘϺȾʥ\x83ЫϝźáςϽɳ˹Ţ˼ĉĹԪ˝\x93ԫЖġ-ԀƉМ¤ɱ',
                                                        'value': 'ӍʐԉʟҺƴJғµŕӞнǇǤ\x89Ğ;Ԕ˪ӠΚӊƼʸ>Δ\x8eǒ9˦',
                                                    },
                                    ],
                        },
                    'comment': '҇ӢČXΞ<ҀͼǸΰМԋǭčÁѠĥҁЋûɌϧΥӱԭˆϳƕщȮ',
                },
                {
                    'keys': [
                            'ùñԪ1ҿ',
                            "ҙ\x9dLǕŠ˝ù§ӠǕˌеŸʫǷ'®ȓȽΰJü",
                            'ѡǶÏt˝{Ҡāкƫ˃ƿ',
                            '\x82kДǎЕ\xadƒȎУĳӝĿ\x93ӕѰ',
                            '˫Á1ŖҰƋǍΘ^ЈƌԉǠːŐĐ˪ɵ\x91˦«rĤԡjΧʘʼ',
                            '\x85ӂǋ5ɕnυƥʄ',
                            'Ǧ¶зӫɈά˥ª',
                            'Л҃ĲҜˉƔϿ\x9dķʰĎΒK',
                            'љɝfÁ¶¥ύıě®ĆbƘӹ~ùΛԉ\u038bʚԍ',
                            'Њ΅ʂ˻´ȅԥҹ',
                        ],
                    'event': {
                            'target_id': 'Ҿ¿ϨϪʍɊˉǝλǅňōȥțʐʟ˘ζİӠxɴѳφƇzќ:ϋ"',
                            'parameters': [
                                        {
                                                        'key': 'ʷҟǵИӌ҈ʻˀЩőҽɴ¦ïЫʉǍεƅыѷИм}ԑŅ\u0383°ӷ\x97',
                                                        'value': 'ǪȟƉԢǓĕȃȰӺјǬƘÂЮːǐϘķǩʑҒVΙҙ҈ƨѰҠãԥ',
                                                    },
                                        {
                                                        'key': 'шű\x9dέ+аȓİĒ+>ǷçʰŭҼҔԈȧҲøɵѢ?gÅīΣØ',
                                                        'value': 'VàªÃψˉĚɐѨ\u038b\x8dǝүϔˮȇӢ˦qȆ\x8dάňͿφԇɣӌÃͶ',
                                                    },
                                        {
                                                        'key': 'ӟәΛĐ·ȑķЩŤëȾɱȮϓ|ΌĜȊ\x8bӏģ¢҄ńԫ¾ȵԙôӺ',
                                                        'value': 'ɥąʜĬˣĊρԐʗеάůō\x82ŕŬВƥ\x90Û΄%ÚɵДқǥмȄď',
                                                    },
                                        {
                                                        'key': 'ã϶вͲҔԫɚƁ{ÊͶ\x80ѴЌӼǨӁ§Ƀʩ˯DƹɓϭυŚȇ¥ϋ',
                                                        'value': 'ÃƬÈdҏĨü³ˠΦƀѣIĒҠŪüƶϠƺғǇȌӪƕƳӣёȄҠ',
                                                    },
                                        {
                                                        'key': 'ΧěϕǴҊ"ɌԈƓѵοƒ0ɑѬϩϹÏзж\x81ŊšʻϿέñԅͶn',
                                                        'value': 'БώѐЃƍJŦˋˡƺ\u038dūɜѠʏҜЀɴх+ʽȣѧͻάƛҍl¿Г',
                                                    },
                                        {
                                                        'key': 'TuSͳұūͱʤØӈ·ĚɃϲĖ\u0382<ԥÖӐЁҶѽCŻЋˆҰțA',
                                                        'value': 'ѰтѳψŊƽɈʎŗТɏѪόǨҖǲǖǫƛ)Ð\x85ЀЇ˂ąƒǻƺɬ',
                                                    },
                                        {
                                                        'key': '˘ȄŘԦ˟зѤӤęʃфБŔăAԊˇаѫįӷȭǟҿҌҁɤӏƁƺ',
                                                        'value': '@ʣɜʋȉƧв\x9a\x9fɨMЗȹȍJËüλɻ˴Ɋœ|ʢЪƓчΝƤː',
                                                    },
                                        {
                                                        'key': 'ΕŠϗҽȺǤԛŶĒƖϬђʜΨȬϽυԋҀ˺Ѵ°ºȓΗӊѝɣņͰ',
                                                        'value': 'ǷvQƤʪάϛïêŎġX§˭ǳҳPϬҩЏʏ=¢Ė¹īʻāǺÉ',
                                                    },
                                        {
                                                        'key': 'ʾśӭ8ˢ)˾Ŭ\x88ɲѿˇѫh\u03a2ҵ|Ǩ¦ҷ¶|\xadŇ˯Ό³ÜēϘ',
                                                        'value': 'ѰʭˌšԢàӞԜķƭœƙƲԡəҁ˱ëŊӰεςΛ˸ÄyçÝɓϓ',
                                                    },
                                        {
                                                        'key': 'ЖƽҥѤӂЅȖƷuǻќƭӈŐΰĔ˛˷ǥ',
                                                        'value': 'јПƫ҇ǡ¨ђǞǐқÌ8Ҹƭ`RVˢU\x89ƨϵ¸ϋъǣHԌƦЈ',
                                                    },
                                    ],
                        },
                    'comment': 'ōƲď!ǟőΥυԣǙϛĹĨɻȑʫӧ¸ĠԬħɼ|ьĪЈ©ˁҚ\x94',
                },
                {
                    'keys': [
                            '\x85ϞõƴJΥϝΉɴĵǡˊҕɍʢιwΔϳ~Ȟ\x84Ҡ',
                            'Ǉρ¸ŧθ˕ϴѵϦƱӾӤʍŐʞ5œ!ʦқ]ʃƖ',
                        ],
                    'event': {
                            'target_id': 'Ȑſàύ¥ΕҠƨҢоԟ˼?ΥѼǻкϢǜƔĘʈҜÕΖӵӑȺԏ¼',
                            'parameters': [
                                        {
                                                        'key': 'ΪΛȬƵΨɧUȀɵĔŭ¥T7ģҥǈԙЂҗҿƿԫҲώCχâȳű',
                                                        'value': 'γ®Ԅ@ϞЁ\x9aўƪǷŽǈēŻɆɆϭĞɐƇȭ˃ЭϰǟЎѧƟӹϘ',
                                                    },
                                        {
                                                        'key': '\xa0íȵľǷŶϛ˔ƴд',
                                                        'value': "ɆȜѾЂ˳ç\x9dЪ'ѰҎϽќԣΐѓϙЦɔϸÍƀa\x98˛ƴƪ˵˵г",
                                                    },
                                        {
                                                        'key': 'ТɴҒЅѲ\x8eҪƫϱȦǭʻȧ',
                                                        'value': 'þˠǖ´ʒȜʳ!ЯĞßӕĢҟҵǜҐӕɭѶʀȜК˚Я¢\x92ңΉȀ',
                                                    },
                                        {
                                                        'key': ';ɮǐ×Ҥȹ˳ʣ,ɪǹëȜӜiɻ',
                                                        'value': 'ƵǂӛрşʇʷİëŅ;ȓЂТƳңӒʖǯӠƩѶΥƼǯПӛdҟƶ',
                                                    },
                                        {
                                                        'key': 'W2р\u0378ͽӳʢäɋϪȓthɏԑ\x8aƯÜ°НӫϟӵҨέ÷ƌnЄʅ',
                                                        'value': 'ѪʓƏ\x9fǖФєĴϛӵҷӾçωΣŨĽǮ˺ӑũѝƻӽƜȎ\x92˹˙ư',
                                                    },
                                        {
                                                        'key': 'ǛȗͻƼӀÑǲ1Ɲ ˚ʐѠˑƖӖȲŋˑçȷȩǇƝν\u0378ǬôΨм',
                                                        'value': 'ǹŘâϱ^ԏş˧Тŵ˝ɵEȨįsʖʐíԉԀǑԔϊkʜӛǶѻҿ',
                                                    },
                                        {
                                                        'key': 'θΰҘӰŃ\x87ƈ÷ΌτǚҠĭąұԟɣЇ{èʴ҉ɴİĳʮǱCóÜ',
                                                        'value': 'ѯʱΕʬŮιˆɇŨɸǛ·рҀɢȾӬͳɼ˶ΩǬˆѪ3ǬП~ķԀ',
                                                    },
                                        {
                                                        'key': 'ѪԖaăÉҽŴ˧ʇŹ=ȇɁŦЙwԘü˟ˬѠ¾ɇÇσӲȹЬɻȝ',
                                                        'value': '¡ƘЛ˒ȉԣʵéƦХѮʖτаͷҗġǽѬ˙ˬɔņǳƷǑҲƦΏȗ',
                                                    },
                                        {
                                                        'key': 'ǮϡӃƨӾ\x9a\x8eҌӴŇŭǯкǡʯȉ=Ϝ˱ћԋЅѰ',
                                                        'value': 'ƪӊʗwȹ ʁįҌλФÆɨȋɢȠҶĔθHҚˠǙ΄˦ǡcϻȪć',
                                                    },
                                        {
                                                        'key': 'љEʻɒЦ\x93¥ɀ҆ǭό҅ЉϑĵһéԂѶϔϻ϶Ӱщʧšп`ńʞ',
                                                        'value': 'Ҕ\x9aΑҐưɩϒԭ\x901ƽɦƾΧԌгюʘп˂Ӓ\x8dJϷϵϩаξҶ¤',
                                                    },
                                    ],
                        },
                    'comment': 'ӑo@ʺʕˍͱԆѶ҂ԮˊӰĝǍǉůă҉ɜB\x7ftÅɨϐm˚ͻĺ',
                },
                {
                    'keys': [
                            'Ƙʯ\x9dȪģВõ"Ҭͷ\u0383Ǣ˔ưǛʡȣ',
                            'Η˔cƝ',
                            'ːέ\xad˛ďτƞʅȊǴ˽\u0380ΥłÄɭ',
                            'ɫȧăїDŨƐÍӍãɼӑÆǥҴӛǯ',
                            'ŎЃåҗîҜЂ',
                            'Ϫń˵įű',
                            'ȗѯӝԑæљʴŬϖ˻Ȱκȥˈ\x96MRҁ\x9dƘ',
                            'ӏ2',
                            'ЬʉȒɻÖ',
                            'ȓЈ©гфѻȸңÜӁ\x8c',
                        ],
                    'event': {
                            'target_id': 'ɓҡйѹ΅ĜʊȕМϐÍĘ˗ÙƭӻʮɋЍόƒTҫȡʝŐ§Ӵƃж',
                            'parameters': [
                                        {
                                                        'key': 'ѫȮǎǨкӜEδȶƥƲҺÆҾǩ¬ϷÏӺҵ,ĳӥ˰¯Ԉ-ƧϫА',
                                                        'value': 'ʓȃͽĲΊƠˬȂɕÜȰˍ«ЩкÍυôƝ\x80Ǖ·öҀƭΉ\x81Ӗʱԋ',
                                                    },
                                        {
                                                        'key': 'u˹ŃtüѠÌaΧӷҽˠíǇ˄Ȑ',
                                                        'value': 'ˎӛʥƪ$ϪĪҰԍˮ˫p˖ЂӍőƱ˕dϑȂŐŷѝўŤϜԢˢӔ',
                                                    },
                                        {
                                                        'key': 'Ԁҽ\u0381ȵҾ`ʷ(=ǹΈŪҰʗЛϏυ\x98ǉъɭΘӒǨμļЙʝͲŮ',
                                                        'value': 'ѽӝϖҬęӏĚУҜѼ\x8eʐǋTΌQşƿzϰǞˍЅ(ŕˤϦӟŊ¯',
                                                    },
                                        {
                                                        'key': '¬gȉőѾԒĝңˋҡȴʣÏPЛǧƺԘλȞРρ\x8c\x85%jˢɫŋҘ',
                                                        'value': 'ǢҴΟ.τм˄¦#\x83ơǨΣƨ;žĉƌƟ\x82Й^ƲǕǥșӉǫ\u038bҳ',
                                                    },
                                        {
                                                        'key': '\\Ɠ˂ОԩŞʭǾѠ´NӚgӏʹǑˆȧԇˣÆŪȡƝȁ9ǁϓǳӼ',
                                                        'value': 'ԝíyʭ+¸BźİЁӐ¶ɡ¸˷ԃɔΛCµ`οɗɩ7Ξ˰\x88ùѰ',
                                                    },
                                        {
                                                        'key': 'Ѝ^Ӊ¼ ҹ\x9dɫï|ǂԃЦ҇ѪѮɥн·ӞѯèWӫˑνę˝ӌα',
                                                        'value': 'ʭвɐδφĐэHУŲŴťWұqȲѨǿҸѶҙrЬ\x7fǕŸĺȃΚȆ',
                                                    },
                                        {
                                                        'key': 'ƨǾʓɂӭҦđѻԃԪ7ŨӘ&өŐŕύȺɻπõ]¾ѵʴѪƿʯɅ',
                                                        'value': 'Nɿ˚«ΑјҺƾĘ˂ɤ·ǹɔӞňƚһҡXξʁЮǿ\u0378˜ćŤĽ\x91',
                                                    },
                                        {
                                                        'key': 'qŎxƘ˘ȸyǜʫчļ\x9a҇ǥțͲΘҙ=$˦ʰɀҖȣġЁǷӶӊ',
                                                        'value': 'iģϭİʉȐЅ(ăǝҷϋ`ŅɶьΣĮԜÊӼʦȚѝȞŁ\x9bʥ\x8b®',
                                                    },
                                        {
                                                        'key': 'ŞԮǆ¡ĘӧԌ˙FǎȆҹȈϘͽЦлΣӌҪǪǄʽӄȍђʣ(ҶЖ',
                                                        'value': 'ŌΔʋ\u0381_ƥĲʾҦтέʋӄх\u0381ɊһǧǧǋѠĆԍʣNԕįǕȘÿ',
                                                    },
                                        {
                                                        'key': 'ȭ\x98nȾ#ĶȈħȩØƹəшȈƤϜɗ§\x84ɛë\xa0½ԓăŹǊ\x8aˀй',
                                                        'value': 'ʵϱϠčòұœȮΜʌ\x88θ\xadҭԌó˕Ҳʓ§˜ǰŲșŶɇŚψ·Û',
                                                    },
                                    ],
                        },
                    'comment': 'ҵɭƐыκZӓŜʿұʠȱKЌҞΆďÏӧǔԭȆÔ¯ΘÓҫȽĸǏ',
                },
                {
                    'keys': [
                            'ӂԝЮȰǕǨ\x83ÄϕͺPҳ+¤ЃfȬ\u038bϾ˃',
                            'ʱĀ®ƨѨ҃ȇŷƓÊӁʐš',
                            'ӣѲɛǈĹҋĦ.ϮʰӇdԥѾ',
                            'ʤϱȫŸµ¿\x90βʎƹʔͿ',
                            'ǧêˎЌͱӷ§ѺǁŐƓĞχzǎƽM+ːЋʳhъʏ\xa0ς¾',
                            'љuƗˈԚ\x91΅īʉƳĭƏưʗȔɳѷ˶ұǨƥǅ£˙',
                            'Żѓʗˈʍĺ"ԟÄѾďɆěƂӜ',
                            'ͽι',
                            'Ь#ƯíʔЦż҉ůЙӤοώԉъƳ\x9fǒӉѝԍϙʔ',
                            'ĬʧʢҾю¤ħɒδÖӉәїҀҷYТÊř\x94˟ӔΈ˺',
                        ],
                    'event': {
                            'target_id': 'ҢӼȌ~ЙσЫJьĳǕωȩˏɶУȡƍɺ\x94\x84ŇŔÀŶϡʃȶƚį',
                            'parameters': [
                                        {
                                                        'key': 'čΰȴƢƆѲǘGԝ\u03a2ʅ(ҖҺʔƮӭϿDƪӟϕǷӎ\xa0˦šόбˬ',
                                                        'value': 'җЪпùǑԢÄƒɃϭĂхӮѝȢ\x80ģ҂ōӐǇǃʙʜƷѓ±жˁo',
                                                    },
                                        {
                                                        'key': 'јǌªǜƠ\xa0˵áÇҼ7ɢŐҼ˟ΥİʧԎαϐÛŌ¤żͻԀҬ\u0380Ԛ',
                                                        'value': 'ϬѡҼƢЫέňӞӳΉƺɨ\x91ĲԁҬфМβįƱԥӿǑҳȧΞӝǾs',
                                                    },
                                        {
                                                        'key': 'ϐòøҭɭѪϳ:ɕϨĆɿÇ\x81ǉáP#ƚɧƦǫҫҟҭòΊϦƧv',
                                                        'value': 'ĲȽэȳɓņF\u038b\x8eƘϸǋǵΖ²ѱò˗ӡħѰѹ˄\xa0γϹ\x90áкǉ',
                                                    },
                                        {
                                                        'key': 'õӳŷ\x83ѾņȜʳȲҰцǳȄɂΔZӉΑӾǾљǘԆ\x903ϬŸцǌѼ',
                                                        'value': "hѵȸ',ĭσʀϛ~jϮʞϫ?˻ǋԂϰƲ\x9ađđʇȲ˷Rǘӡș",
                                                    },
                                        {
                                                        'key': 'ÑµӼƂˎȅ',
                                                        'value': 'ƽĲʥɐIҢԙϐӾȞʧӇϔʜ·mɰљ=αãÚ·ѕȜђϳĐǾɘ',
                                                    },
                                        {
                                                        'key': "ȬβhĽʩ\x9bЁ\x82Ń˖Ч%ˌ˟ʱ¼͵ÐĠξ\x9c'Ǧ˟þȺΧэԞҭ",
                                                        'value': 'CЭȪȭɭНǗьЮɿӱˆȐʛ϶ȗĽєөȫìς³ΡЬY',
                                                    },
                                        {
                                                        'key': 'ԌƾȾ*ÜҌяǴő',
                                                        'value': 'ȽɊӹʥĹԖˬԊěϚ¯ӹˠ£ʩÙɖźȿȳ\x9fNԫЕЏ˖ãŵɖÞ',
                                                    },
                                        {
                                                        'key': 'ԆԎŻǷɷ',
                                                        'value': 'ԛÇȏʬМʎɩÚς˫ņєǟӻӘĜɆҥȢ˻¸ԗƻə(ɠĸȢΣɶ',
                                                    },
                                        {
                                                        'key': 'ƗԅӜ˪Ҏșɭſ',
                                                        'value': '¥ӁњзӆſўqϏѠυÆͼáӊӵӯːӫ\u0383ĵӱ§ҢҐӯǝƘяƝ',
                                                    },
                                        {
                                                        'key': '΅\xa0ҲďѸԎŗȧϚƟψǬ΄ӆɤª˟7ϩ\x95ӥêϦӃǰȷʫŭќ҂',
                                                        'value': '҇ʦSưӉ\x89¨ɹ˲ԈιӇ҅ȅϳǄȶЀѧӷƬ\x8aг×Ɋϣªͺʦɬ',
                                                    },
                                    ],
                        },
                    'comment': 'ϮŉϝºŧJk Ӆǘ\x96ń\x92ɰƬǿȿýÄрђɁBϼ7ёӜ˾ɹ\x94',
                },
                {
                    'keys': [
                            'ѾJƳɣҒԀǅʏ¾ƻƛìʊΞŗэŋFµ=ǒԚӏȓĭ©Ѭˆ',
                            'ʰԞ',
                            'ĳɪʆɊ',
                            "ƻȪ҂ʃ\x94Ҋ˰˺ÄÈv'ҢVԔϪ",
                            'ʑŨĖƤϲμʓʬĜK',
                            'ΤȺʲѦ҆ȿ¶Ц×ЯȊϓʹĂǈ',
                            'ͽȝϑЗЖŢΑ˺Ҽ',
                            'ҌӈѺƎ\x81<ŕзȅҬзӔöњIĒѷʮ˟ɴΧPˠҐͽȴхƿ',
                            'ȑВҲдơ¨ЎʎİƖ2=ϝ˄ûͺŁԩrʲˡъÀЙ',
                            'ƤƏЁ\x7fӛuĜĈϋèѭПіĈǨҜ',
                        ],
                    'event': {
                            'target_id': 'ϠΙŷςөÿĝˁяҸǔL',
                            'parameters': [
                                        {
                                                        'key': 'ΌҞġԂɎ%Ɯ˵iłЫԚƴɻŏѾΨ\u0378ǜʈÕϑƷȥ¢ΔЫƨďÔ',
                                                        'value': 'ǭ6ӯ\x95ұԋˮӁΣƙʕĚɑ¼ʧàӚ˩Ӛ˗ԇӏŜ\x85сϟɵȦнѥ',
                                                    },
                                        {
                                                        'key': 'ϚlţÂźӎӏįdϒµ\x85ѹąΆӹfʶȧð˼˚Ƅƃԙɿ˥ǂ˳Š',
                                                        'value': 'ɆƐġҹċƷÄԪԮҒÚƛˊОïαÝÚȾĄѢĆŧńҏ\x9a¤+ȷ5',
                                                    },
                                        {
                                                        'key': 'КЛͳ.Ԍŕ\x92Aӳɺɞ\x82ȯɞ˶\xadӠɮ˭»ˌӔй˖ϩő\x99Õ\u0378Ň',
                                                        'value': '¬Ԟ\x91Ǟ\x93\x96ѡӦѹɞǿ\x9aÙΕϖĐыʕӞΨκłňƱНԟǬǙǃĕ',
                                                    },
                                        {
                                                        'key': 'ƫȉǯ',
                                                        'value': 'ʧOӻťɚ҅ǷKҷ˽ĪѢϑѷçȥ˙яBөƬƓßʽKόӺʨɂŞ',
                                                    },
                                        {
                                                        'key': 'ԥҹԦɨɼɥǋиĻƆ˹ѷпɓ{λ',
                                                        'value': 'ԝΫҷʳƜ\xadςѹùȧģρòҽʱ\x8aΘ˝ԧƾəҎkĶʢʓԒŏԆΕ',
                                                    },
                                        {
                                                        'key': 'ҚϽȋ\x89ö³ʬѤԃ6ԊкɩʍΊ4ŦΏˢҧIskťȹѝǅԬŖ(',
                                                        'value': 'ã\u0378ЪЁK˛ƆԫɄƬʧɐóҴȁ˃ԢύũȑӵCþǵӠ@ϡǦĹб',
                                                    },
                                        {
                                                        'key': 'ųĿˑѕĐŊχӅĴɰǐȝδπSʧқΙÙƋÍŸƆǡҌǗŃԅ«\x9e',
                                                        'value': 'ɏMϬқӇɹΞϕÌԂŮſǠȷɫʒƽҫҙҺѓȴʔ\x8bǍу2ŀ\x95Þ',
                                                    },
                                        {
                                                        'key': 'ϹӢǶѢЍďǊĭȟуδ\x91ŤõŤӎȥuK\u038d\xadƶØ',
                                                        'value': 'ТɿʡμĉɜòԘԮΕӧΙЭŢνӧʄуɃȻÕѵз_Ԭɜƅîю\x93',
                                                    },
                                        {
                                                        'key': 'λЕ\u038dȵƑҪьƤǻ°ĒƒΫɤͻΩĿ©ԌѰĬǹέÙ\x96Śω',
                                                        'value': 'wǬǖǛԍ*ϬςԈÊb©ɥуɞ˚XћɀΰћŻǹɍʖΑʆЭǐҦ',
                                                    },
                                        {
                                                        'key': 'ѡζŔǯŷˆȳɟӒ\x98ǕƾϺь\x8aĚѝĂ¨ʎʹӪѥԢβѢΖЗѫä',
                                                        'value': '(ʠѴϩ@ԍѻӚˇҳƮˈʖϵѤñēƨғɳǔɧǸdżȱ·˸Ǆǲ',
                                                    },
                                    ],
                        },
                    'comment': 'şҥőӫӊǓ+ǣþcЙԘŠƵ1ɟȆƊšŁыŞҸͱʡԭȳӢŘɌ',
                },
                {
                    'keys': [
                            '\x95Ӽ\u0380Φ',
                            'ѐлƺϚȩ',
                            'źӒŐÑ˳ɫėİԂԤ˓ѥP˳Ҫϣo',
                            'Ěœŏҟԋ¹˼êN',
                            'ζχҟ¬ΏɌѧÖэÌϴȇҢ%ŗ˦Šȥ҇ƹȼʑ˵(Ӊ',
                            'ɦèŷžϓӹќȗʏʲǲҚθωӧʤ˖źԛtҟ˖ԋÅɜ',
                            '΅uʓӁϳԌŎЈȌӚοϩЇ',
                            'Ǌ˲ҜŏɧòIѰƠʰТQаȕ˜Ɯ˺юÔυԬŬmŃ·^ʮԬҲ',
                            'Ӵ˥ьðɋˋfЌѱΏ\u0378\x9bÁèҤǭÛӨҬĵМŒиãϯŅ',
                            'İĄȡĻ£҆òȮяӡӶÑϘʻʧʄȳô<âΣʣˈˏ',
                        ],
                    'event': {
                            'target_id': 'ì[ǤșӮĩήǥѹȤӽī0ҴǂӘ\u0378ηhΉѣ9˲Ɋ˥î\x87ӎӶȹ',
                            'parameters': [
                                        {
                                                        'key': 'ԦԩΏϨPԓ]ǹÏʔǭ\x81ΐӿʟԄҊīªƘζёʭΜˇԉ¢Ȉìµ',
                                                        'value': 'rо2Ž\x9eŅğǔΆҟƋ0ƒͷѐȉЂϱ¾ÇНГˈ0ϒҢĆȂњϽ',
                                                    },
                                        {
                                                        'key': 'ŬČʖʻȂўҏůПϬгąʃԃ˰,8Ηǉɯ.ǉæƚϐĥϕɦŦϢ',
                                                        'value': 'ҵыÅӡ¾ӘːƸɴŅϐʧʑ³:ˬϦÂïzϧҲ¾#ѨŲ\xadʎΉΙ',
                                                    },
                                        {
                                                        'key': 'ǳҶ˳н@ͳRäӱ¾λ(Г×ʵѫђўǱԮǴҏȌǶŝ˃ȢŢęŹ',
                                                        'value': 'űrйlԚѺBҙ¦άǑʚӯԫ˥nѫ#ФÑĥȉPкʗʍӾёϭӬ',
                                                    },
                                        {
                                                        'key': 'Š5їΑЍÙ¿Żʦʜ&ŇԂƽţŞӧѵЗУǽʯ\x9cўſґԋ§ĝ҈',
                                                        'value': 'ҲѲʋқíҳ÷ʦ\u0380Ā˔ʈɅ˖ºϯ΄Ƭʾ¶eʎɬуЃѶ˾ίɣΉ',
                                                    },
                                        {
                                                        'key': 'ªÍǒб;ɛΪЂΰɸĿɤϴК4ԇ҃њǋ¡\x9dƐʼɳԝęɹwĲ÷',
                                                        'value': 'ȅȃƲЌø\u0383ԄʂԆΝғɀЙȶЯѦѹȚҩ¨ǁ¼ŒԈˬѝžɿǸѲ',
                                                    },
                                        {
                                                        'key': 'ǟȊɴԧϸ҂ĈĆӝȨӳϓʱ϶ԆŃɏÙԙҘƭò\x87ϤΙӜŷȨɮІ',
                                                        'value': 'KǪņȸԑÜʸǰќԫ,ӈˏʉǆјΔΔҋŘȑӓ˄мɭ˟ĮŋбӬ',
                                                    },
                                        {
                                                        'key': 'μ\xadƟŊϺӤГ˓ű2ԜӅ¾',
                                                        'value': 'ѢҏԄÌĔήƂѹҦøɪϜђΡŦϾ˻Ҭ˼ԨρŅΟҟҺÍɦ$èǢ',
                                                    },
                                        {
                                                        'key': '˓ÍͻΑūǦPίʁЂÝBǓóӮèӜĖ\x83ͿʍŖԔǏʒŉ',
                                                        'value': 'ØνʋΡԛ˖ϿҢǽˍʞÙϡѦ\u0381϶˥Ѵɹĸ\x84ʝńМҦήύý˺Â',
                                                    },
                                        {
                                                        'key': 'шoŌСɰOӉәɡȳªӥΨfӓǻ)ԅȎήҢюʉĿˌѤϾеȭŨ',
                                                        'value': 'ɀѻþˉч˟ԨʺҺРđÞԖÏɃԦϺ)ʎҪӚǕĩѵȖȰϲźȡŒ',
                                                    },
                                        {
                                                        'key': 'ʿϕԜȿǲĝƷϪӜÐϫΚӠȯȸѭƐʲӈ¬҅˧ɺǯȥЄӠȻ˨ѵ',
                                                        'value': 'ĄˁƖӉʰ˅ĥŬɠԎ\x99żƵĈķƢ˔˗ưõ\x84τΘȋԚ˸ȆƉϛq',
                                                    },
                                    ],
                        },
                    'comment': 'ʹѕʒƹΈ+ӊȚЊє´ňȰҲ÷ŌʏϼѦԙΏ\x85đá°Ω#ͻѵΡ',
                },
                {
                    'keys': [
                            'ɨǴӧвǸs¼ϭ*ΠȻȧӻ',
                            'Ӊбǔ҇σ\x83ѰҴ¸ǊőГЭдɆƟſɰòъ҄ҵǱłǢč',
                            'RӼȺ\x85њÍНęНԠЭźȏȼt҄т˦ҜÕˢ\u0381ɲҲ]SԬɿ',
                            'ʐɕĀԣǜѠϳΰʵȣËɍŦŋǘǀԂЅҲ6ƊсӞ',
                            'гԇȤɹѠæ·ТƎϔӖ\x8e',
                            'ηHǇ',
                        ],
                    'event': {
                            'target_id': 'õ˫ȼѾȲí~ǱȒβϺΊʃðɦ\u0381ѰYʓΐɈӣɲǴή«ļΎÌԅ',
                            'parameters': [
                                        {
                                                        'key': 'ƧƴʉƵ&ɣΩӣ&ǌҝáĲ^y\x81ȞÔÖƥʟųһЊθǤїhɗƍ',
                                                        'value': 'ҏѯƍҰɋЎАѢÙĩ;\x96ПаÚɶţſȹĎʢ˟ͳӏȫͳєŇéŘ',
                                                    },
                                        {
                                                        'key': 'ӅƉɊίǸѷ3ɣāтж\u038bŌɂ˭£ϜɐBrѕҧέғǲεVǄϒʆ',
                                                        'value': 'Яˀ\\˽ʭ"ұЊʭұы¯?ȜðȩªЕΦĔbcțƄæΒӰŧĿɡ',
                                                    },
                                        {
                                                        'key': 'Ğ5øƭӇʋжΥҀˌǚɭˈȴсǊǇR´ϛσξΕʗïėğӃŗ͵',
                                                        'value': 'ˑӠƙɫʦɨϛƨŽҡЯ¿Яh˂ʳįШΖйƐĢӏʢмeɝДɺԏ',
                                                    },
                                        {
                                                        'key': 'ļόίΛϤќwƏ˼«˹ϮǧƺƇńŚūƊ\x96ˎƐǔɦЀΥɟϮϔΙ',
                                                        'value': 'јŮȬˌ¸ǚӃɊˊϒԤɰ:ҐĨłɤϻҒҺůΨťӒDͺƏҿȇϕ',
                                                    },
                                        {
                                                        'key': 'Ϙ\u0381¨ҴԓȿҨǥ.ӡȊҵԉŦƣǮΒȸͺƗʺ˂ӋўŮӾƛ±6',
                                                        'value': 'ŷʰ7ɫ÷ŤŨƔʱϡȻĮjЛƽƖ¶ıŤŧòͷȰԓ°Ô˄ƷŹҺ',
                                                    },
                                        {
                                                        'key': '¸ǈęŋͺǟȜʳƿ҉Ρºѩ¼ɅϻĴӕǩѢ˳ӊɵϧʪ¾ҪϙōΩ',
                                                        'value': 'ːԏƜˉԧΛˏŬ|ʸ˷KϋѹҷƩȰ˟.ХÔχʶ\x96˷˧ћѦϔǥ',
                                                    },
                                        {
                                                        'key': 'Ԛˇ·Ǹͳó',
                                                        'value': 'ΪӍɮҵКņ\x9fȉЗʴ˚Đ\x87Ηџů˼ʿӚУҌªСƅďѵΐԢʾҡ',
                                                    },
                                        {
                                                        'key': 'ʚðυӭɄ\x94ɀȻӣѵćҖʶТҐμā˷ɿǠǑў#πǣƌϚA\u0381˱',
                                                        'value': "QΈʮɁ\x93ƿͳӼġƕҖˉЛ!ȦǫƄ,ьťʘȡͷҔΗ'ʨ\x96ЭĜ",
                                                    },
                                        {
                                                        'key': 'ӞΖӨ ŦŖԮρǳƑӪƏǏŻøМԟ\x97ǒúҡĥˁΥɳ¡ѸƗ˕ʐ',
                                                        'value': '«ΗˢTîȆ\u0382ɚЋƓΉǹıƵĀɞˮǂ¿әȮ<ЂѡØjʓæȥӃ',
                                                    },
                                        {
                                                        'key': '\x8eҊ˽τϝȿŌnŠǏыѪΥϣ,ƷϮҹҹǭʆŴɼŻЮ҄ɯΠΊʖ',
                                                        'value': 'ǐӇÕ;ċΝŪÃĎr¾ѸˈǃЄʢ:Ӥҋ϶Ɣxƫ¯ȄÈϪsʹɜ',
                                                    },
                                    ],
                        },
                    'comment': 'ƒōӄͿ;щƻыʈӚʘŃΥÞǻЍ\x8aǺҎȜ¯ϝΡëAԋϥȝćç',
                },
                {
                    'keys': [
                            'ǻCԓќӻVϯӬ˥ѧʹψϣԝӫΟԠΘ˲ѝϡԧƘȩ˙ћǺ',
                            'ɻͰѬǙЭɄŵөϺņƵΡȴ',
                            'ƭӹů+ʰѸЪҘǰʒƦɚĚϿӒЭНW\x92ƣͲʻŕ*ʸơʍDϑò',
                            'ŅʀÅ±_ҿȓȰѼƐˮŷβШŗҩ',
                            'ϫʝƺ҅ğϣξҭǭŻ/ћ˕ϱ˩ϪŅǛɮвȆĠŅϝʭŲʧ҈ӊҘ',
                        ],
                    'event': {
                            'target_id': 'ˁϛÙϯԌЅУƼKĽȸǓм͵ȁ[τЄͽҮʍĆЃÎȣӍђӰŽĺ',
                            'parameters': [
                                        {
                                                        'key': '˞ͰûĬ5ɊjϪR\x80ƭϲŤМº/Ȩɓ',
                                                        'value': 'Ȓʸǅůʇԣ˾ϊ¾ϠϨҷĞгԎ[åƂ¦Ǌѧȁ[αϑ:ĕĸɥɷ',
                                                    },
                                        {
                                                        'key': 'ʀˤǒǎϾĭÓǂ˯ʈĨҨЫȌˁ\u038dʌƽнˀǬIΔǡÂѻɛщЫӠ',
                                                        'value': 'ϕХƾˉƿЧŵɩˌɞϿćӥȁnmЮԒˈȜ˵ί\u0382BœӢ\u0383ɩʹʃ',
                                                    },
                                        {
                                                        'key': 'ϦΒ˕ЧÑԃӴȚŁiͿӞĵаѦ»>ԊҮʀˊϪĉԅȮήu˯ÕA',
                                                        'value': 'ºǀЬ;ͳϛʁˑĞԞԓϭ\x82ӬνŭТ\x7f?\x96pǝȩҔÈŽЛÞɬ½',
                                                    },
                                        {
                                                        'key': 'δêɏԎҁ˄ȿ~ңÈӗɡʶŷLţĩċʍǖ£ΰƒӕԦɨ\x83ҼЃК',
                                                        'value': 'ҷϰǔȁʝϏǣύͻBӦÊĭ{ƿ\u0378ԤÊ®ѵ\x8eʚɇ)҆Ҟǜ¨4в',
                                                    },
                                        {
                                                        'key': 'YɏӴʮʩȂȶƍΤЂƚ0ԪƼ×ѩǱ˲όȹ\x8eǔӲGӂ\x8aSƋӆĥ',
                                                        'value': ';\u0379ʵΛʑ˅;ґĜ\u03a2űľԢҹȢvӷĴӡŬόŒə˴ɯϺΉѧѝ÷',
                                                    },
                                        {
                                                        'key': 'ԡŞɰԄˢψҎӄӦҨЌƕɥɞhҕϩяέλΨÊǩƘœ',
                                                        'value': 'Ʋ˟Ӥ\xa0ψg˕\x95ʠ½ѥԝԒ΅ʇǺԋϒԭɁΜϜҽϹνϭ¤Ĉѹ\\',
                                                    },
                                        {
                                                        'key': '\x8eзķƳϟҼң&\x90ɂŁʒ΄ŃѨҬ\x90ԛDʼʍԤНҽԗϏӯɅıΠ',
                                                        'value': 'σǬ*ВηɜɁӵѷʋн\x9bõϻҎ¦ѹByȶýԫwÚϾѭʿ³ѫӖ',
                                                    },
                                        {
                                                        'key': 'ʇʹűšĶƦ',
                                                        'value': 'ЁлʯєȋԬ\x94\x87Ƞ\x83ˍſ\x81QǙͰǧͽuȟyʁÅӝˉӻǗ˓Ԭȭ',
                                                    },
                                        {
                                                        'key': 'ԛɜӛԫƛø˅ĤɄɪ\x8bĔʲʛǲ\x90ϏǸą!ʳƥ˖ӟԗдӾȵŞ\x85',
                                                        'value': 'uĶϒ˧ϔĂɓȸЀτЪŌÏĢȀɍɮчĦMˁƈΟҒԉЊαæ[ǅ',
                                                    },
                                        {
                                                        'key': '˟ΈαȺ\u038dТƟҩŧǘβҨ6ǷѿҥЅԆԉЛ\\ʁ҆ΡНԊPÓɌΞ',
                                                        'value': 'ԮɵKǳОrЊƅâҧȡRо˛Ƹ˰ӹӗǴŋҖχмʈόǝ.Ҕʤþ',
                                                    },
                                    ],
                        },
                    'comment': 'Ӓýϊӟ˹ĤѱѪғԉɐƑԓϋԪҦʑʘԊ\x9d϶ȍєɺΫɨӨϚiɂ',
                },
                {
                    'keys': [
                            'ż˭ӞҔśʹ²\x9aĂÏӘΕĚ',
                            'ΣðƪŦʎʑòɣҧ.˜ÀƓǽ¸ђɿ¶Ʊɓ\x85)ϞöæëѨ',
                            'ҿӸ҃ȱÜ҂ƈǭæϙŅɽ¯ʛѽʹ΄',
                            'ôИÚÓǱӄ',
                            'ӫʴħèʦ\x98˧VȏÍʯıʅԍʦЍӳÌ',
                            '§4ɺӚ˞ШɉɉɭƎԇӣʘɔÂĞͻÌŜѐԟˬȝъͽÇȷÌԡ',
                            'Я\x98æϹˮзŒȂȀŮ²\x99Ŀ˪ϒĎΨӓÍ[ɑƚǏǧ',
                            'ʍ',
                            '¥Ͷǻњýćξʙ;ɂϷù',
                            'ȎУ˷ƎлȩȷȪϻйĠӵŮĸѐ˥ҐňϼĩИІȁțη˫ɬԬ',
                        ],
                    'event': {
                            'target_id': 'ϳƲԑͻВˣƮПò˯ɬĦΗˏȘƹȣưӳ\u03a2Ϊª˵ʸ;âӅӒ*Ⱥ',
                            'parameters': [
                                        {
                                                        'key': 'ſɌ\x89øȲōĈ',
                                                        'value': 'û\x98ҜƆ:Е¾ƀŵԅȽ҆ԫƁʥѠĭƭZǟѢĎҗŪɇхǓTˤԓ',
                                                    },
                                        {
                                                        'key': 'Ԇ϶eҏϡГ',
                                                        'value': 'ϞЛǺЀӁКȽɷɐƢǥБǑɉƯţƧѩ˸ɒԥǸbRƔΓʿˏĭӭ',
                                                    },
                                        {
                                                        'key': 'шɱXωʢǐŚUΗ<ʘȋȓƵҚύÆ\x8fфǌŕσϘǬ\x99ТПѨϕŝ',
                                                        'value': '>ÅӄɶРК_ǄŘtа\x85½ӐƕĄѦ\u0380ϟɡȍʺăȞň¨˸Ɂ˾=',
                                                    },
                                        {
                                                        'key': 'Їȗŕ ǺПƲΛȳſaýȌӲΦưƛίƃɱЌБĂӬ¢˸т\xadì¸',
                                                        'value': 'ǖ3ӮͱӍӞǪȯǕүѣΣԩϋϦdԈϕӶɲ҇ѿь³ʂŀCϹӳщ',
                                                    },
                                        {
                                                        'key': 'ӎɗѢâҦǂZ\x9f»ȹχKRҖʴд\x8bɣɡfǣɝƤԦ£ϔιΪ˸d',
                                                        'value': 'ĞӲҝ\x9bΙήǷ\xadԫҲҪӚǓÒǰ:ӤˑЭҋ˓ϜύǦʦƪϛ6űȃ',
                                                    },
                                        {
                                                        'key': 'ʓµʇeΨӞ\u0381˥ӨŒΗȠƏŀԓӺßa҇nŌιçΟj^і\x9cŀô',
                                                        'value': 'ˤƟë0˴¥љҠƂъ1ĂϓʈĂʯŖΨϗʲҴԋҢȐ÷ƪÎŉ˙Ǻ',
                                                    },
                                        {
                                                        'key': 'Ɋӿϗ\x9blʔ¤a˓ЕӥƩ',
                                                        'value': 'ÇѨǹԙʃūɱȁҔԡŸʙԬԚɍēҼɇěȅʙƾłбk§ϖȈ,˞',
                                                    },
                                        {
                                                        'key': '®\x9bɖѧɏϐјХ',
                                                        'value': 'ψáԐҠΥ^Ă҉Љ\x8cԛƛɒѸ\x92G\x8fЌ\x98,ńӅһә\x9aǲ˜ԑǆĊ',
                                                    },
                                        {
                                                        'key': 'ʇӛʵІĆҭЙ HѭǕǡ>ȁ˕ЁÿҷԫбǁϩӟҨЯªʢĥƤė',
                                                        'value': 'ŀ˞ʏǧ«ɶ\x9dЧѩЃ\x90ǬɬӨĈȪŵģcԭɰҸȱН\x94ŽФʂεҗ',
                                                    },
                                        {
                                                        'key': '΅ƯȵҺӇp\x8dŌĹƷȸőǥȐÜιчԨ˃ȀľǲHŦ˪ßϰϥƼĒ',
                                                        'value': ',À\u0381ҕȾƋԝ²ŚȇúȌѐŃʳƇѴĮǦѠѯèʠСѪφЦѺɸ\x7f',
                                                    },
                                    ],
                        },
                    'comment': 'ͰðǁˏҾ0ũɊйХѥϳǅǓȂºǋи4ĬÂԑό˂ŦҷэԈ¸ѯ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'ϼ',
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
            'name': 'E¬ƘӀГ\x91ʑŎ˒Ʃьɉ²ҳʻӡԦͷ©ѴΝĕӾȟдĪƲϴåō',
            'description': 'ǇЀЂɭˋξ)ΑʶOİ˂Ƌ\x95Ǡγɔȴнç_;dСєϙuԥ\x82Ĵ',
            'target_id': 'VԏЮǫҰǌğӘͻґʈ˛ѯȚϩ\x7fʆ¡ҴêӯŚψ¨UɕƇĥƮǸ',
            'parameters': [
                {
                    'key': 'ҫiǞΞĩӲōρɋҨŴșӈτĚԛñǲô)ҘʖǤԣâù\x90u˦Ҟ',
                    'description': 'η\x8dɎǒ˧ӮɄŏǶͳҳǣФɟԟɎˣ\u0379ɐŠ·ԉСƜĖāԟȥȔ˗',
                    'default_value': 'zΈċӓǬˬȲҚŨǤ?ɆϞsΜǯÙůĥͷːʺрұȵͳˉӵѮˁ',
                },
                {
                    'key': 'ȃЏԦPƉԟԆė;wϵϥɊǚ=ҸÀǸƮ\x8f˩£\x91Ŀлçӽ¸Өȭ',
                    'description': 'δǮѝˁāȂͳƀǓЕȵʲĥŭÓӢӍȌǭσǄÿϑϓǒÈ˙˹oʗ',
                    'default_value': 'ʢŁÐɱбʛÝôҊƿΛţӻƬɦӾ<\x83ӶĠǏǖ\x97ŤvǬрД˱ķ',
                },
                {
                    'key': 'ˠQƢϑʺLȞŊeΟвÈҬԚЗ˘ÓжΙǓΜά\u0383ƜɢPӮϑɆb',
                    'description': 'ƄҚʑρƗƝǧȵŏŅȘҖԏǓŐäϩċѥȍ΅ȘɵԣƆáҹȒәˮ',
                    'default_value': 'å:қɚŢj\u0382Ӵ˞HҖȨһSͰĝԝͻѿÐŻӭ\x8bŶ˺ɥÀ±ʬȿ',
                },
                {
                    'key': 'ɂ¾ґΛɬβ\u038dǓёȡ˛Ԉϻћ-Lɕ\x99ѹѮŞ_ƩϜяƳĴȭĐʹ',
                    'description': 'ΠʯȨ˦bĎӛԠíԠ:˚pĿɏϠZʳ\\ÄЧъWƠσϨĂԊʋѶ',
                    'default_value': '˱\u0380ȼȝЌћЯ˧ȸҖūŷѢyŮʚʸǼӲʛϋȣɖÚǽҥɩ¦Ӟʫ',
                },
                {
                    'key': 'ǅç˯Ō«ʐŃч¿Ή±Ѿ˩MĜҿΧˤƕ\x81ĖʑӅ˜Ó0ЇŤ}ӱ',
                    'description': 'Ԓ\u038bδ©ɍɯҕлjǈžƀнԁȭʟ®ăӬǎзȍMʄɉʞʸΎӫη',
                    'default_value': '@êȾŻКȺΡͽCΙӨƂUɦķîǎø¥cŸΈˊ\x9eӭіѐұ˨B',
                },
                {
                    'key': 'ĞО˴ǩɌѰӂԃȀɖӜҨȶӔʼË£šĺ?Ҩϝ?mќΈÊǥōϏ',
                    'description': 'øĽɁó\x97ԃŽцųԡϮǚĿʧξɎĺϼѢ\x92+ӁİǄɴyӭ҄3ɜ',
                    'default_value': 'ϏўɌԪsҸӢŔûâȱǭǐˢãАýHԈΉbΟǜ˞ɳǱ\x8cԗȅp',
                },
                {
                    'key': 'ŉɪЕĞƻǁĬҵLѰ',
                    'description': 'ɣŀˡˎ2ԃfjЦΧÙƋȊƻ\u03a2ЫәʔЯƼˬΉHãϭҬӑʰҦǡ',
                    'default_value': 'ӿ҉ýҞɨǇԌŀ˖Ϟˉ]ηäɍМrĆɢŨȔǪњЭEԖʣԑ¤Ҫ',
                },
                {
                    'key': 'КϠȸ',
                    'description': 'ӔϢЗĸ{ϥaǏšļĜĴӹηӳԉϐƤÛƦϕΕì^Ēŗ\u0382ɯӥÁ',
                    'default_value': '2ӾˋȝƃԖǢȑ´čèӤǻȮŃD϶ԉďħ¬ĲʓǥɞǶӠ´ˈ҃',
                },
                {
                    'key': 'ǣ˄\x8fȮϙïÄ',
                    'description': 'Ѐʊ\x8fț˗è\x91˯˲ЃˍǢʝȈ\x9cŚƯхȁƩΨɍ\x99ІҌĕœеeƴ',
                    'default_value': 'ӶˈΎǪɄɦѕįŖ\x8a_ԀӐԥı-ǞìҙZɨɛЊΔӗœӷȶ©t',
                },
                {
                    'key': 'ĠРǁȫ҈˷Ŵ˹ɪǌɁԜʘˡϑ®Ēʩʹ¶ŅʘζèӇΟƈÛѬ˔',
                    'description': 'ҲԖ®ʃМĹȥΑ˯ЮӦ´ʘ\x83Ӭ҄ƿ+ǾΧȅΩʋеΦрҊ˰ʲѪ',
                    'default_value': 'ѢѕВʨƤƮϤɦԍ]»ҲѧʢшуɆФϥťxī\x93ʽáѯ§ĵԞɄ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x99Δȡ',

            'target_id': '0ʵ£žδ',

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
                    'name': 'ӄVȗʥʊ½ĝ˖ƻȉд҃Ó\x82ȁн\x83ЦӬϤɔӗØӔ\x88Ӊɉɐ*Ř',
                    'description': 'RĖ\u0381ìŸːƁѫʞĬʷÔȥ˴ɌʬЧɅƱƤѝ§иcŧf,Ӵƀe',
                    'target_id': 'ӗԑʈéӥ(«ςƠȌϙɹªԭZǁёкѨ ΓӹзѩȽȈТϕҳϜ',
                    'parameters': [
                            {
                                        'key': "Ǿpї\u0379ƴўƓ³ԙŪοƲϙíˀ!ÍАϱҳȺɛӪӵς'·ѵƣϗ",
                                        'description': 'ԭÔʍĥԡʞĎǍĊѡιҙъ(ɷ~ŞнŚЩńˠҜʥîΓʴ\u0378ʣΊ',
                                        'default_value': 'βĒӈƕȀʭԕíщ\x9bҷǸϟ˽ǅʕȨ"ԗȱɁʕǇХӇȋ¾ϚϦȢ',
                                    },
                            {
                                        'key': 'ůδΦȖРXļŖω½ħĪʋϕņ7\x9eĴąŢҸŧʧöτˊҭĊʲʿ',
                                        'description': 'ǸȒĠˋЌˍˏŒ¼зľԣʯĝг\u038bɁƺѳĥЯħнЦћ¸KϖȢv',
                                        'default_value': 'қY\u03a2΅ЎƔϢқƍÊάɺԂθĢˤǧɪ˵Ӂ>ƊеőȺĜɲûԕƯ',
                                    },
                            {
                                        'key': '¥˯ƈФǳС˪Ƽ˔ɇͲƛӸЌÉƵѮӴÂȌϥǹԊĢӛԞLĿғ`',
                                        'description': '×ƕȽȡĞӑǛÄȏǷҼƧˣ3Ĝϐ]TРĻĲĠȔ=˺ˈƈș_ѣ',
                                        'default_value': 'ыʈΎŜѲƊ\x86ï2Ĉӫ˟ѪʳĿЍϓŃԄҎǷ\x9eŊτӥĵԟȠŋЭ',
                                    },
                            {
                                        'key': 'oϵǾрԢ\xa0\x87ЯӲЁ\u0381OfɽǻǞʸ\u038bİÇŮļЏîԑŌǤĴśѐ',
                                        'description': 'ÅyΡӎɱǺĵʔĺɔ˭ι\x91D϶ԃʾҥÙή˯\x94œӮӰʚӜ˟ϱų',
                                        'default_value': 'ћŋʬΌ˩ŻǧJϺ¬ɍχåѳûBˈϜʀɔЍԣҮȰʘɵӬʂǂɄ',
                                    },
                            {
                                        'key': "ȽѝѧèϯϚ'ёǟԆ~ĲɁvà˦ȒêӜĉ\x8aӋλԊƑʖҡϒʵˍ",
                                        'description': 'ĴҐ÷ŦҎÜϘѝўҥɃӦЭƟ$ђɏKӧ˘ԡˀŇԇĢɿáƜѐɜ',
                                        'default_value': 'ċʷĈҘĮȋƻŝéȼϿϺ\x87$ǉƎƅfˏʉɦϪύdĝŸŜκ?Σ',
                                    },
                            {
                                        'key': 'ğƻбʒȵƾԧˋϦå\x9dŭȿҢ',
                                        'description': 'Ŕƨц\x99;uӵЄԢҽƞ\x95ѣщԡ\x84˳џΝ\u03a2Кѹû\x81¦ԃʬǫ˗$',
                                        'default_value': 'ԉρįȋɳђɳѦʑɉԥřΥσŊľçԊӸH§ӵцГ7ъƄ\x9fįʟ',
                                    },
                            {
                                        'key': 'ʉϒӅʁδ±ΏȻОŦĩ½ηӺ=ҽ˙ԉǥϔ͵©ƟЉȱ\x9dζƃӷ*',
                                        'description': '\u038dʳ҂ɵȕʛΗǪUҖҫх¤ȊǨ¤\x89˜īĝǌƴÊ\x83Ӷȏί϶ȡǔ',
                                        'default_value': 'ɧŝΑСаơΠČɾÁӺȸ҆ʹҪˆӄ˰ʏ\x96ϞȉΥȾӡ˰¡ĎȚɎ',
                                    },
                            {
                                        'key': "˓ʔԙĢŬɜȇȝǭԃùԝƺŻ'",
                                        'description': '!ũìɭ҅ӘʪϚЭ϶ƹBηƍ®Ӻ\x96\u0382ӔƀϕϼǴŔ¦ŗΎЂҷũ',
                                        'default_value': 'ȍƁЦҞęƱɤĮʍΉɁΙѸʋӿӏȘǹǈύƳÂŇѴɞ-ϵσ\x86«',
                                    },
                            {
                                        'key': 'ƘȁȶäŹͼԚ˾ά˨ϤƼѵîѦЗӽϲìGŌȝÖµΫґ×ɰ',
                                        'description': 'ˎÎԟƊͼNƕɪҤ»ńҿңƧӤϲʣÌʉȃƒԠŚǊŒқÊe˙ҿ',
                                        'default_value': 'ѻɷЌɻǠΡŏ˓ʊĬáƄԫtҀ9˚¨ƇƝ϶ƭєǷλς6mĭ´',
                                    },
                            {
                                        'key': 'KϐӤΑϳƵЪ\x85\u038dəГ\x94#ԚáίǷҦƢǸҘ\x8c\x84Ɵ҈ЇŢүȗ¨',
                                        'description': 'шԕϐĉӫň~ȀȍǞӌūÀɕйЫØȑʨŏ\x91˛ˁ%prDҴϋӟ',
                                        'default_value': 'γх\u038bƃ<ΏȌɵÓ˳ǿԪƊʆ1οƳŞ·ϐӁѠрԇҼ#ǄЀӻȖ',
                                    },
                        ],
                },
                {
                    'name': 'Ǝ\x81ԮШϊ҈҂ǝų\x96¾έѥĠɽʖœ\x8aįȤũсѓ:²Ȟ˨ɝѪφ',
                    'description': 'σςўƥĀ3ԨơǲĔɃ˖ǝƀÍЈƟ˓0ĲÄӌãЄӳȿʤ\x83ьź',
                    'target_id': 'ήҐѵщ91\x91ӥjʓȳƃТƨ°mʥӺ0ӷ³ÍʟŎ͵ȯȞѦˤɵ',
                    'parameters': [
                            {
                                        'key': 'ǙΓ^ЀѐΧă\x88ΗɩǓ´\x9bʳǨҦŬοʟʑƙɢһƮЄΠϾӊ½Æ',
                                        'description': 'ēԪʏ\u03a2ԬŒӂ˨H\x89ʾȼǜȣӢɰM)³ŲǁɽFƦǳӬsЂǊī',
                                        'default_value': 'pʷ\x85Ϗ\\˸ӐKȜϏǎǗϊĹǙǤɄѬ˺ϵʅĕϏ\x84pȵӀÈàp',
                                    },
                            {
                                        'key': 'хЕʛ',
                                        'description': 'ѩúԈʛĘɩʸĕͶʭΓȝǺˈҥӀŬЂǿǖˍΝϨƓӟĞǰӤÀИ',
                                        'default_value': '¹қћҽcɎŲƒřº˩ʹʉκԃ˃ŏφˋš[ʜж˥DЧԫАȍĄ',
                                    },
                            {
                                        'key': 'ЅĭÆЊȽÜȿ҈ԌǷŰӧІǭÃªʆԧѶҨςќѴСҦҥԦɩǭð',
                                        'description': 'ʤŬ\u0382\x82ɿɎѵ\xadϒȸǀӅЗԖhÄҍɯҰËйƷϛ;ʬԛyӥĢԫ',
                                        'default_value': 'ħєƸȔîɟѿŵԥνǉ[ӀɆˁɱήɩ«ȤǼǣƇĉшѡӪëšО',
                                    },
                            {
                                        'key': '˥ӖXκɚɤȲӘҁĔӦʳԉιыʊĽŃҝg˲ϻŤѴΚĜvόƜð',
                                        'description': '˗]ÔȦҕÂӄуƒͳʌНʥƦsKǜԚĶθBȺƛԐɞз|˅ʑɍ',
                                        'default_value': 'ĭɪІʪǪ\x9aŻNƍ˟ԁŎʾƛȼȍöȐ˾ҁǾƺǅɬϡyƺ˴Ţɒ',
                                    },
                            {
                                        'key': 'ȧГÈͼӠn\xadȖʷΐ¶ǓǗʺȊƓǱԠJ\x95ƢDŀʹϙѐɴԣƯӇ',
                                        'description': 'çųµƅĲԥ΄ȯԂƄÏϵǌǝр²\x9fҾӳӪČΌʓ\x8f˽Ԇӑɲȫb',
                                        'default_value': 'ΜʾȟɠҙʀΓѧńЫ\u03a2ɁǁĞғϏӕĨŶΦ±©\x9aǴ҉;ɴj˄Ҳ',
                                    },
                            {
                                        'key': 'ЌԦǨˇѿԌ%ɷҪοҨƄĊПҮƕÓԉȢІ˥дˆϳʊĠ[ŋχϦ',
                                        'description': "lŋ½ƁѫÞőíЎȹѢĵАĩΎΠ'ԬɋϻɟȱԔԮӉӟŚ|Є¯",
                                        'default_value': 'љϋԏϰĭ˚ȁ҇ǐíԛɹIǞυǢҠлʃʋϗĢӢӊЁӝƏÂˆœ',
                                    },
                            {
                                        'key': 'ȸƒǕьȴˡɑȠͷŤƊ¸TԛԁýЩŊЖåȷnģǺˤǟǁȷʓ«',
                                        'description': 'ûŜѻƦƯϊǴb\x97ԀҐʰÁØŋ<ǿӌȲ\x8bśÜǺφɌӓhÌд-',
                                        'default_value': "ԋɵѼǣͺȘĉӶӭ4ºǌҪȮƓ˄ЋϦқҳңђǠXĒ'ʲļ˜у",
                                    },
                            {
                                        'key': 'ĳĉюαӕuȥȰñŷƶùQӬύɶѝʜ<',
                                        'description': "÷ЯgНħϵʠԞgӔϢϪĥ¾ӳǎͱυԟХăº÷Ȯîp'Ƞύѿ",
                                        'default_value': 'ʘȀԁȀҽƕÁѨÔǊ;ŮŻƟͻȯҔǔρȶЬ\x92ŅǎΈɖәПӛ:',
                                    },
                            {
                                        'key': 'ģˀǘӳɭ\x81\x8eӻɖȢȞæӴƀ2ԧųGìҶўӤiƻ¨¨ǩŖҿʧ',
                                        'description': 'ѨΎ˴ː\x92ҁŭõʕɵГťɌȀCɋǥľҾŢȉļ˦еîњʠǥʄʖ',
                                        'default_value': '0ϡӤˁ˙˥ϛЂϦͳɽŲӅ¿ŰͳӟӡδǵӲȵJɝ϶ōˌќȁŘ',
                                    },
                            {
                                        'key': 'ϞЃǪɨɧ\u0382ȋοŧT˝\x86ȩĀ\x84ѐЩ˂ƸҴЩȧ¸ÝМ¿ɺÀ-Ȇ',
                                        'description': 'ãӭԪщÒǤˁёӊѲʥԑīӕɭŷ±ŉʩɮŋƢʽѨHϨҙэiυ',
                                        'default_value': 'ˬŎ´ԒԝŻγϱӞ˞ŪѪȷĺʚћŔƿȴɑʞϓàÍӀҡŸͳʯt',
                                    },
                        ],
                },
                {
                    'name': "\x9dδ҅%zЬ\xa0ӑԝТЉЪ\x7fɝЃѥ\x81ú&ȷ'ʋԐƟʱbʎ˵Ӽʫ",
                    'description': 'Ùǎ]ɖӪ¡ǣʃùšʠʐԛ\x8c\xa0ҩǒИѢːѓѶӞǇԃȆμͲȢʍ',
                    'target_id': 'ɛɥӦɩӴДπɖлΡ\u038bːђҘˋѝǿâCɧӁ\x9aѭ˵˥µr˩ȿԟ',
                    'parameters': [
                            {
                                        'key': 'śГĢƠѪӧϛӴ`˶ӷɎɡOҟ˃DǽΠҦЫϴƗ½СźŻΡǇџ',
                                        'description': 'ξʃƞΒŖΕ¤ҧИԅЗȮ0ϯѵϘ°ҽǔԄXЉŎ˜ʌɰÆůΓɭ',
                                        'default_value': 'gʙĈȎZhԌW\xa0ƚύΩφəьԁ҃ŁĀԋϡȑȹŪ\x96˕ȂˍҒӕ',
                                    },
                            {
                                        'key': 'Ίгèҥ˒ƴɢƝŭɆ҆˽ʒƸÔǡϖǶɣЪΟԟͻʧœԩɣ´ɺʵ',
                                        'description': 'ʢΑӄȺ\x98ˈȭ˗ȣàвĤλЭĈͶƊДƶɆȒ˵ÞĂǔǟʍѱ҈Ѝ',
                                        'default_value': '\x9fΐŽůğDʡ(ȜĔАνǲҞʰK\x87ǊΊԏtͲʘҊ˴ԙǙʴ˖Ƹ',
                                    },
                            {
                                        'key': 'ȺT;łȎ҆îʱŁÑбԢ¿˱ŭˉÑҴɦɝʾѭ',
                                        'description': 'ξÞÿʔɼхFÐ\u0383åʨîɎѮ+ФʟϜ·йϭʪħϏ\x91ȕɫŎӐǭ',
                                        'default_value': 'ʚҳ˞Ҋg!HΈǂλϨԨԎҬkЊʑҊţϬӨȥѽ˸ɀȾŶƦˊҩ',
                                    },
                            {
                                        'key': 'ĩřĺһVҔЪԑи˺ɺ˘ǶɿŴΛɱғΈUŽöѯ\u038bοӄ҆Ɠӷl',
                                        'description': 'Ā\u038bЊԡԑƧɮnǸ˫ŮȎĲӞǄӇ/ʟɢӮҏԅĂΐɉŐЁĦӮӟ',
                                        'default_value': 'ԑǚǥԔ9ϵĨƓԈϯı£ʟÒЌĲӥùҖԐŉαǭƈԜμmÝ˧x',
                                    },
                            {
                                        'key': 'ϛțŗҤʍΉԐƸӭɹˏ£ğǓń%ćӪ(ԊĶȅѰ;k˫ǋЬүŶ',
                                        'description': 'ɠнҢȖӶz˖ͻďϋžπKʙþƙȡǆƙƪǐʅѦӨéƼʜ`ԃȰ',
                                        'default_value': 'ƨЋҖ{ƝȫѳӌǫκҫЫҢσϐǎȮҫǍŎoΔŗɤ\xadĜƔ\x99>[',
                                    },
                            {
                                        'key': 'Ư2ç^҈гĽϿХ',
                                        'description': 'ɣs¨Ω5ʬҎıʧˎВαωуϚŅĉ\x96ƛυġçʶӒӹѓǳƞ(ċ',
                                        'default_value': '*ǻ͵ɡʱɡɹǆȽϦÍˌҶlȎңʷĎϒƮР\xadũǑƝǷŮҧǸȱ',
                                    },
                            {
                                        'key': 'ȇƭ_ʊɱ˩ŤЩ\x96G®ͺ\x9cȭԓѤ҂Ȧ',
                                        'description': 'ĀԈԥǻŊ˰Ǿǂƌϱɣ\x81ȌüӀǚǺЬђ¶˥тԂʔǧϞԦʹϮ˷',
                                        'default_value': '¼\x9eqѬªґÇʷсȘû˓ʑčѱXԗαKɎГЕ4ǜƙ£ʢˆ\x94Û',
                                    },
                            {
                                        'key': 'ЀԚιрӦŉŉǪԂ)ҶцʬŤѐÈԕșËô΄ŪϐųϣԛȘЧ¤Ҝ',
                                        'description': 'w6\x98Ǘ˓ʴǥμƟǗҮ+ҬEќЩӧȆšϏӥɱ&ʀͿωΩԮʧԗ',
                                        'default_value': 'ǞªƉϽŒýͽǇƨȹчϨɲĢĩťɹЁøҖР˱ˠԝ¾ˡГɣʣԘ',
                                    },
                            {
                                        'key': 'λ˚ѥͰ¬ΟҲЋ˨ɥķʐçǾӅǇŹȼ,ǨЬǘʒɁÍμnŭӓ¶',
                                        'description': '<ȦBɄI˭ԐϔÇ¶XѧȹɕşКǗЄ˔Ѵ\u03a2҄˨ȢɛǝΐҜЌұ',
                                        'default_value': 'ДѨôˍˎʙ»ύ\x89ЧǉEƯǜƘχçξƓԖǾƄȏɜƵğ\x86\\ʧϭ',
                                    },
                            {
                                        'key': 'ʐś¥ŬϧȾˇʂԈǚkŌȵEƅųȿŞӡPʳȉ˫ƈϡ¬ãƻ҂Ą',
                                        'description': 'ӱϜԙɝΩƐ¦ıηɤXxЁмӼʫԂʇЪҮΔ\x9bҚűӼӀҗÿɬǨ',
                                        'default_value': 'ȮҌ҈(ҋΈǇ\x9bĞưщƟŷхζсӯʏΣý<Ϥϗˋɬúʣȓć˧',
                                    },
                        ],
                },
                {
                    'name': 'ŀңçωȆұϔөȩиȳӑдʓӝːɃʍɺĊ˙ѝ7ºƒԝȯ˷ȵΩ',
                    'description': 'ΛɋЩ|ϡſϙ\u0382ѧńËˉ÷üϋєΚΑ\x88æÇΈ3´vȎĻʹқͿ',
                    'target_id': 'Ƥǡ4\x86ƊЭͶýbyк¸˥ɅƉžϤιЬǸ˄¡ԀČȤРėΛɗǕ',
                    'parameters': [
                            {
                                        'key': 'ȉʭЬ>ѯΣʀХʀɾӗƸȖӟĕЫԐɝԇЃlʓľƮĽѧȒˊˤͱ',
                                        'description': '=îл˼ØˮʥԫɾђҽԉʝΙȐĩћ ǱΝӦҰӲ\x82ļ ɶȨҁƲ',
                                        'default_value': 'țĆëЮÊȿĮԢΌѤɬЙа,\x84ɞҩӉѵɉˬәμǈTÄа©\x8fƺ',
                                    },
                            {
                                        'key': 'āȚuɇӨX>ƚԊ϶\x9fTľΘɮΠɯΚơ0ЪwǗ˩ĒϷƊӯǀҋ',
                                        'description': 'ȊĵtѬǤ\x9fÇƵӐЊŘĵ|ЎͷӃһѪƫγżѦƬүѨʝǙlƃ»',
                                        'default_value': 'ҥŃϨň9Љ˒ǔҙԦPҼқ˝҃ӡų\x9cǗϦ¼зҤӮé˭˛ԙ\x82Ĵ',
                                    },
                            {
                                        'key': 'ĵԓɼʏˁ˙ȹԤĨɱԊƔɮvȹϔƯ*ϴѿ',
                                        'description': '\x91ɶ#\x81жԗɜҕъˤ˶òǱʑь´ͻUǔԢXĒԙʹϻĳΰͳżä',
                                        'default_value': 'ǈʳӯ{ȡѲӀԎεĽŎˤ˕к>ЇҮίƬΚƗӪÿӍÅê\x9fϡХԝ',
                                    },
                            {
                                        'key': 'ϧ',
                                        'description': 'ϖӤДґkŹҥВĦ>ɸ˒ɐ%PŗҫгȜώ˰ΣʊŝҼӣԐĀԭȱ',
                                        'default_value': 'ʻǕəӿĹ4ǎӌԭǗŝѓɵCΔĦǹөåԟAл+\x93Ηą\u038bǚǰŲ',
                                    },
                            {
                                        'key': 'Ϊшί«ɽǋйǨЖϭǚцқœʴɈt\x80ɝ¥ØϴǊǌƐlϵɌˍΜ',
                                        'description': 'Qƕφǀ»Ʀɷȃ;υӓϕɴЯԫ˽уĘʻҒŢϡӢ¤ǻɯ\u038d(ϝ\u0381',
                                        'default_value': 'ǹʿ˃ˌmƕɚǋѻһƢʡӸԞΓďԐқӍҲŦѼұЪǿѲHʚȫɵ',
                                    },
                            {
                                        'key': 'ɫ˸ǜǈėҙЛӃԗδӐϢÃӛǱʏʹȲr`yÛґңʵʯɜɝù0',
                                        'description': 'δèŪȂńŰМ®{γ<ɷĭΖ±шϾαŀ\x8aȈλȶh\x98:ȂҎԚ˄',
                                        'default_value': 'ЛŹѰԖΰѪҐϤ˱ǧ$ҐÉњԑɀƆƘɱǝԁѦƅɨυһģӐӎѶ',
                                    },
                            {
                                        'key': 'ȚҫŝîǈӷșѭĔϩ',
                                        'description': 'Ȃɨơ΅ϸ҉}ҫŧƪ͵ӤżƐˊˮƏ9ňȗ\x8fȼǔ\x80ɡʯƠƛřɻ',
                                        'default_value': 'ϣё˘ҋ˾ҵŘēμĺƦȯ\x87ϣğ˪íʸ',
                                    },
                            {
                                        'key': 'ɸÔӰ\x83ʄԨ_ɌҎʫř+ȣǁІɒѸǌǊЗʷyȡDĞƜĬδԜi',
                                        'description': 'ɡ\x88ΥǘѕȓȫшǀƍЃȟ³ƖòͺοӰϴȺԈОńˑԣýǻŷ½Т',
                                        'default_value': '<ӑӬ[ԃÄđђĢӗȟ˩҃ʉ¦ӊчďϸǈɬkŒʱʛʆŇˬӬŕ',
                                    },
                            {
                                        'key': '®·Рkǽ˗əίɔũ\x8dμȊˮΰЩшд¢ϯҀĬ҈ӧҰńʀʒұ\x9e',
                                        'description': 'ҕɳԅ˸҅Ú`Ţłʽ»ʹŪTσˊY^ЩţȽķǅǜ»ÊȡӃ\x85\xa0',
                                        'default_value': 'āoȱȃŁ˹ӍʿЋ˞ʣ,è҂Ύԁц·ѦϢӫT:\x8bÏºγ6\x83ȑ',
                                    },
                            {
                                        'key': '˧}χɎÔˣǣѥфӭθѦɇŗʟϪȼƳéӚӑȿͻƁ',
                                        'description': 'ȭӮϴ\x96Ķӵ]\x82ķĚҺJkŋӏԣƫƨӐҖӈλǡU2҈ŷȀ\xadē',
                                        'default_value': 'ԡʚƱāƠ\x8eɆ²ƎʨҎƈӻμǌҿưδԭėʕƕΙҹµˍĿǿԄӉ',
                                    },
                        ],
                },
                {
                    'name': 'ˡ<ɖȡҰғҔ҅Ӌ\x9cӲԘʍȚėĳЊȥXчʑ҉ӺǠ\x9dËǳħΛΠ',
                    'description': 'ȹΔɞήgūʨєŔΛʐ½ϤȽϞͻ°ҚˠCīҖÐȜĐɭҐ˥Ȯω',
                    'target_id': 'MȁԁШɼĜϻϝӅ´҉ғԐʉӄҝЬƋɿȊђжƖɪáιŃ2ţК',
                    'parameters': [
                            {
                                        'key': 'éζǇ-҇ɲ҃ΞǤԚӼϝɪøӣʟбӆƌ˩ϯˬƊҊХɏ^Ώ¨˃',
                                        'description': 'Ő÷ɝʥѓɷѿѼҩǑƀån΅\x8eǹĉ`ȲϕбǿѤʉVșƥБӒώ',
                                        'default_value': 'ЖɠбҭʬТŌЃâϐԭÆ҃ѢΗƠиӚфǢºĵϤϵYӝ£ƪȵͺ',
                                    },
                            {
                                        'key': 'ĦҸðӑšɐ?ŞāƾϹȮҋјБƨҩȣӜύӿǷ˗ҭԉǝѽȤѺn',
                                        'description': 'ʕЖіɞԫβʪѽ϶ʱ\x9aƻőзрʼƓӏĨÛЙĶʥԆԉZō\x8eŶЀ',
                                        'default_value': 'Ԥ\x84šĔRăʺӊŻбŌƪǯљϋ¡ƈbЌeԨƂĪê҄ĽӷҖǼƁ',
                                    },
                            {
                                        'key': 'oҬŮʩǽ¦ƤżҼЁaɱӅ\x9aʗȊƻȽØéŮĿӨΔТНԚɓĲÑ',
                                        'description': '\x7f˄˂įҔÞҊϑȽföƆьΘʤϹȘϴӖÚѽǲĪkҎȠʝ¿Γť',
                                        'default_value': 'ӺчğЪѩŠĦμϮêзǌʥþӚ*ԐˆӧӾɪđŃƼҎʹҖț\x9c°',
                                    },
                            {
                                        'key': 'ĘӔǁљӲƝȡ˵ҖʫͶ@Ӯ7¶ѺԈāМ\x81αń2њʲƖ!\x81Ưʖ',
                                        'description': 'ǅĔғǿ\x8bâ\x99ϦѠк͵ԐţФȱțѧЅЭ˱]ƢʝɒѦԣxŷŜӡ',
                                        'default_value': 'Ȃ6œʿɁéɴͳTˏÝ«lтЇiƳ~ƂƒШӚϪќȓĚ2ӲԌŁ',
                                    },
                            {
                                        'key': 'ҫѐ˵Ҽ·ļǖҠ\x83ΓƔgǛˈΟӻӴÕŞiԐӰÐΔąǈ3јIĸ',
                                        'description': 'ĩɰЖ҄ӀȤԧӒҫ$Ɠ˛¿nʮӗӂДŴҒƜıЍѥ\x89Єʽѱ£ҭ',
                                        'default_value': 'šԖ*ȞͰ\x9f\u038bŐʼɌǅϖʬ¹\x8fɡΤýƥťѪoϾĄԫŁУΧƶǾ',
                                    },
                            {
                                        'key': 'ƾϜʓóô\u0379Хʞюԫ\x9dϑ҉әȍɔƝG\xadòϗӗCͱŕ\x8fϲʤʯȁ',
                                        'description': 'ȼĬ˝˷Ѿȍs\xadHeˤŶҝĜВ\x9cΣӱʫȕʫ{ǱɀǞǿϊюѪЈ',
                                        'default_value': 'ϜʐǢέǁ¹ѣёŽзʡкΪʋ{ðӨĥԐĈǔӼǫҒӰϲɧЗӶҰ',
                                    },
                            {
                                        'key': 'ǟΐɁm\u038bēұȩŔʍȭŃŅµɉԄĤϿİƵλ.Êùђoӎ<ϴͶ',
                                        'description': 'ҋ\x8fŸӬѬĪ´Ԙϕљ\x91ħѵŵȊЉEηΣΈҡϓJʎȽѨеȜγӳ',
                                        'default_value': 'ȏѹԬĢ˺бқԭδ҇ԚʔѲòȲҳȦǉ˜ɗҞ˸ϺɥӭŤхǾĕҀ',
                                    },
                            {
                                        'key': "ɀҦ\x92χü҂ѾӞȈӶūΧɹ'Ŭʬ˯ѕήƑɃǴθϤзЦˁъǷŌ",
                                        'description': 'ʘ2ϴĲ\x9cɥˡ°ǝȇɦnүʧЃȝПʒTОԭaÜǑѶӐԠЏŎʳ',
                                        'default_value': 'ĉʄЄξ.ƻΒӾŴƀȨǄ%ԓȿȏȆŔȆȽ˗ИϖĒρцȿӣͲъ',
                                    },
                            {
                                        'key': 'ӿʷ˘ӖȽϲXǪſлɩťɷɏϵҬуˑȒД˂ҝyŀɄƸɅǶ ȿ',
                                        'description': 'êíΕǡûϊĢƖĩˠϊˢȪśѵәʹ˼ųͽҪğώǵѺӶqʥȗҸ',
                                        'default_value': 'ɎŗТɲϡȹѥ\x8c˟ͳԑѾʲȒʀČϷĤѱԕЄŪљƗ\x93ΈӇ¬ҍӧ',
                                    },
                            {
                                        'key': 'ϪЉʳ¬đʘʾŞɎӌɘπʑŝá"ƐǝӆϚĥǨ\u0378˂ǋBԈĥʟď',
                                        'description': 'ɌİǂÃϊЙӺʡ3ȤΤƞԉЙϼ\x9cðӼˮϹőßöϖʞϮũӕ\x80Ӿ',
                                        'default_value': 'ȩĦǗΗΰƥ\x84ĠȼвʭƺƐЕȞпŐ\x99ϥďȐ҇ӧΪɊϦ÷әƏЋ',
                                    },
                        ],
                },
                {
                    'name': 'ӒÎŨÿɨɡǵȿŗǫªęĆýǙͶͼһτŰçȭȎ˼ӌũʹʭɴӱ',
                    'description': 'ΗԎċϺåҳЕ҇ϾÄÕǵśʦ)ԄŹ\x94ƟŁýɡɂʀĩϒϻӼϽʠ',
                    'target_id': 'Øдԋ¦\x83ǜǯįőġʎ4ϹìūƯҲȉѽӄѽүÎ˚ҞπˤӧʣԚ',
                    'parameters': [
                            {
                                        'key': 'ϖħТºZĸ˓ïθҚÓҵōɋŋӻøŒΝΚZƦĭÅɖ˾ǮԓӰϲ',
                                        'description': '˔˻\x91іȸҚ*μҕĪӻЍӊӹТɞǲʕμǘÎ|ϔё·ҡǋ2ҙ˾',
                                        'default_value': 'ϪӀŖƨjǕԒɲ,ʯÏсŪЎёϮKƩŘȼ\x80ûŬԆɲĭӄЋҩĞ',
                                    },
                            {
                                        'key': 'Ҩ˨οɦ˛ҐͱŝdѻԬȯ˗ƢӐɷчаŵɹӳП˗ȚѾɓ˴Ђƒo',
                                        'description': 'ƾŋϫÝʅSӐĩNνåЭBЁ¼ʮԍčӜ1nəźā7ŵȂ\x8cҎX',
                                        'default_value': 'ѽТʩҴԃԂοÝƿȓԣǐʤǪǸūԜŽӺЀɚψĢ\x90˧Ԫ˫Ņƾϰ',
                                    },
                            {
                                        'key': 'ĉΩʑɺӲŪÌĲǃПќΣɔǻ˗®ŉ\x96щÃȾÞǢШǪɟ§Ӗåú',
                                        'description': 'ΜϹзԎǶʄȮԏяšʎӸ\x95ʼѷØǅ\u0381ȴŀʈԨðɋ϶œ_PǯЬ',
                                        'default_value': 'īƢӔƆɱōӷŠŧќêІʳѐÚɻζɖţғʨ\u0379ЖʶϽԗZʳ˻ɗ',
                                    },
                            {
                                        'key': ';^˩lЛb˃Ƶӓ\x9dÆðŁʓĴŘʷϿӽТťȨξǅϙˁΪ·ɖƻ',
                                        'description': 'кΨφЂ¥ˎȑǏĽɡѡȼүʭǻIŗB_ψ\x88ōʲӧȇғ΄΅ԍа',
                                        'default_value': '£ɧƙλʬ\x85ϧȰĩӡ˺ʭCŮӄѕďɢϷŏɆʝŌĘʸ˻τ×ϝȅ',
                                    },
                            {
                                        'key': 'ЕжԓǚѓÒɓӁĿ"ȧȼҟȪѻ\x98қȺŰǶϭ\x87ŕćʩлӊӲҿ¹',
                                        'description': 'țȰā!\x85ʳғϚŇ\x83Ҕс\x7fǓќȉrѭ/ɋС§КԍʸϪͻƫI.',
                                        'default_value': 'ȄɽƩϜɫԬƭԇҹę¾˩ıȈДСθʂҗˈѩEσʭњΰʈ\x8cɦҘ',
                                    },
                            {
                                        'key': 'ºҮҨƘ\x9aϸƬӦɭЧlȟ\x9bϗƨʤ',
                                        'description': 'ԡӿƚƤĀԟ˂Ӿυɭϙʈō҂˺ΖɿƼϼǲΆηвΖĬΰőĚ\u0381Ѐ',
                                        'default_value': 'ɿԓ¸ԐжɬÎʒIҷþƶͻǁҽӑǥȳЂˣȮžŻŸԘ+жЄƖү',
                                    },
                            {
                                        'key': 'π1ñǱ}ΨΨÛΊ1ƉԞͿϜҞӽӯƹɗǮ˭Ъѕɏ·Ӵ\\źѸМ',
                                        'description': 'ĸҥŌƁƨĭϳӝŠчȩͷȖϖЗ\xa0ˇːƆԜʮӋŐ˷ԕӰȀŻӹŝ',
                                        'default_value': 'ОӼˆʏĹųŘЋņɬ΄ǚĤҴϒĿЋҥȟÌҔԪѫϙ\x96ȶAfƙԊ',
                                    },
                            {
                                        'key': '˹ӣүҐĤäŜƍʵδşˬҀl%˙Ħǟ!ɫǆOё7ϺäˮЈƝʘ',
                                        'description': 'ēћϊe*Ȝɲ˴ŴƫӲǏǺͼӸԅҧǶ¡ǉüƈûǐÇţПƳȷȺ',
                                        'default_value': 'ĠŰȼßƢǵǪͰŚ˸ĊȫѤ§\x8cΉíԓ˾îΘΠДˍˉѧqʍɣØ',
                                    },
                            {
                                        'key': 'żЈ\\ƁϑǃΘϥȋȣɊ_ЯΪʝ',
                                        'description': 'Ⱦ˽ІϸæˌїяʊȂтɞ\u0380\xa0ѸCхƂ\x9fӧЀϩ7Ì¡ŉʐ˼Йǫ',
                                        'default_value': 'ŕҨŃѭƈɗѠȶ ұˏȵԏ<Ƣϗ˯Ғѫȭ\x8aӵ\u0380ЃϠȅ\x84їÑ\x89',
                                    },
                            {
                                        'key': "ǐМҴ'ώDθȘԓёϙƽ͵ΐį΄Ԅ8ӑǮҒ˛ƌ¦ÃåĵЩžç",
                                        'description': 'ԚƱϢƻƌ²œʏųзԖǤӼžÍɇ`ϠȟňēûɐɅЯřЉǅϘԄ',
                                        'default_value': "Žϱ˔İŏr҇ӣӛǛţőőԖ'ŗ£ɵͽҹȞˮ˶ŋ\x9bҮИϏɞѺ",
                                    },
                        ],
                },
                {
                    'name': 'Ƹʔԕȳ;ǋɂžąȨ_äʏЈѣǞϔƙÔаɰԞʿ»hѧԄρ˕Θ',
                    'description': 'ʌμăŨ˥\u0383ЀˌƌßƶЅНς9´ʠǟŧñK˽Ź\u0378ôѸƿ/ω˩',
                    'target_id': 'ҵ|\x90ʈԙŞŠŽĲÔȧӼĄȜƸȜŅГӎβφҖǡǥ',
                    'parameters': [
                            {
                                        'key': 'ğȊűʼőÊċʫѣńț|BҺЈ\x81ϛîȳα¨҉ǼȟҪʰмѫÉŉ',
                                        'description': 'ʾ}ɭŝӀőχи]οӄʋњщԒњsƭӅʼƼĖЦ\x7fȡΙȓʇIԢ',
                                        'default_value': 'Ȕ)ϏƹĵұВ˜Ю҄"ǓҔΔƋʬγЎ_ˢ\'ɔʖŸȖȽǯѓjƞ',
                                    },
                            {
                                        'key': 'Ȝš\u0378ǐҰņƎ\x95ȬΠ[Ӳi\u0382ĺw҆ȕƊWԝȭʬǊÊġПYӐѼ',
                                        'description': 'ċȺǁΩҖĵȾƅ\x8bĪюǰ˞ӇŻψÇ˾àЫɨ{Ģҵü˙дʝŇ@',
                                        'default_value': '\x92ҀΝĈɣƎǋӯæыoɼŋìϘƶΞϩFƓ:ɚѷГɀˈ¾ӕЙk',
                                    },
                            {
                                        'key': 'кĤŽͱґØęϖʷş\x83Ȳԭʣʁɧ0ӃƸ',
                                        'description': '\u0381ϱӬЏħ6[4оüɟщԀˀѹȦ2А˕ԊƤǕ¹kфˎʍ\x94ΥΘ',
                                        'default_value': 'ҹλѭĢŵ¶ѶͺъÅʯǊɞ\x9e5ӑǤaΛѪѡȃϛȼÄñĵţǠÃ',
                                    },
                            {
                                        'key': 'ǮźǝӹҼɴмĂψƩǁĞʏΧˊɒϫŨЯȩϹʧĥчԨɇō˼Ңԣ',
                                        'description': 'ӊЇ˾0ǥǶӂбЍʞƺ¾ҷȏɏ%hǺФƍϢ{ũΐɨ˔ˣȒѓʹ',
                                        'default_value': 'ŶѫλΔČǉɄȚıǷ\x98ԞзǽØӺjƟŽ\x80Ԅѕˇɘʏŷyɼmώ',
                                    },
                            {
                                        'key': 'Ą^ҥʙ˔уΡѤΦȅǯς$ή҄҈ГͽмȓƼЙʁӹĈвӸυŘҀ',
                                        'description': '}ĄӻϽrĊŷƆʟӪӆġВȜǛo˛ǋ˹\x8f¦ѴÈǀΐϽіúİӛ',
                                        'default_value': 'ʲ"ZӷϫɋӭǰΥϩŦgőşΚłʪʶІ\xa0fȕƕŧύ\x9f˫хPЧ',
                                    },
                            {
                                        'key': 'ˤĢӜĘȚȟӀΑ\u03a2Ͽʠ&ƌ6˘ɓɣȺԬͶuӡʀɖѲǣԨŉTʵ',
                                        'description': 'ïԉƟśʝǣЙǭԝҭéуũҝɋΗӃĪdĔҤәңѶі8Ũԕɛϒ',
                                        'default_value': 'πƍҳ҈QӠТƯ˘ʦΛ˟ѹӽīv¨Ŝ\\ӔţŴѕȲ(ǿҾѕˁw',
                                    },
                            {
                                        'key': 'ʶĖʣȻΏϙϭΧÆ]ƽξӾĞҚİBƔӉѯѳƥХ˩:Ʋӷ˦Ƞʢ',
                                        'description': 'ΕſԓѹʂĝԝɁǎҌъӲÉτʼӇăҤȗȻĞȖ;Ӻ\x85҆ɮҋĦҮ',
                                        'default_value': 'ЌŧЮÇȉˢȯԎȖРͿӃ˶ƼψͲĎȮƃȪɯϥǴÑӾũΑӠɇΛ',
                                    },
                            {
                                        'key': '˵ƺɄ΄ԁ˾ģαѨ&Őį˯Л×ԋǩљɏŵнˤΊǅɽÔԜKҪϪ',
                                        'description': 'ȈϣЙǣΥɗсȩ˴Ҝ³ɧ΅ǸˀҘԧˑПŽĩêэʸķК¹ÅAӫ',
                                        'default_value': 'έǍҾӽϒƟĥːͻϭƄΙȎ˨ϣʻƪħɽâΰņѫȭȘĕȧԢˇē',
                                    },
                            {
                                        'key': 'ϡ\x95ǅҍрҝMҁǾҝӑЁɩƿǖ¸ˎӽє',
                                        'description': 'xЭɠз˽ĒȵіΘώ˲ɂҷǔɴeƔºŉћ¼ƱüȔӆφεȅӎȅ',
                                        'default_value': 'кξΔοĖͱñȪɃǉyy.ϱ˚^vԩåÞüԞģϵѶБøĚ:\x87',
                                    },
                            {
                                        'key': 'æϙŽƼъÑ\x94ŬźԧνӽЇȕїȷ˃´ãěѵìӶħƵчɚÙ˓Ҝ',
                                        'description': 'ӑəϦЪ\x88ϲǫη½ȊìˌʱǀȌЧƦпlӎΆЀΕӭǱҸŕ˝Ǡɑ',
                                        'default_value': '˙ģīʨǂӿ˘ѩƼġãƶȥϚҫ\u0381ɽɕʃòċ1ʙjƉʯôʫ©ǳ',
                                    },
                        ],
                },
                {
                    'name': 'φҦƚΧĝɫɛѼ҂ÓςоɁ=ԜХ&әήȭǇʷˌæ8˥ҘͰӵĶ',
                    'description': 'Э\x8fdƱȠǢӨ\x9bǬΛ¶љ\x87ʙ\xa0LȼǳԙɵӖʋɤɐԑÑƚĸņ?',
                    'target_id': 'ȶӒȹŁãԄ\\ƍԪԃçƕņί¬ԡʞΈŝÏǡЍфFƭȸī˺ƦП',
                    'parameters': [
                            {
                                        'key': 'Q´ŽȹǙȡǖȇʸǨӋƗҒ\u038dɲҋʚ+ξ˱µÉ1ΏƎҩʠİ$ʾ',
                                        'description': 'ț\u0383ʠʶӣʕΉάЄȫŋżăў\x80ͱ\x9fԈ˱ӵΙҰǣȣĚԨùҊɆѬ',
                                        'default_value': 'ȧ0ЇʰƃȦ#ϧAɘɬǧҝʿʲĐ³6ģ˰ҊǳɆ\x99˰ŁͱАͶϽ',
                                    },
                            {
                                        'key': 'ÓĢԮшЩԀrʦƾʬūŋŞµ˒ƖĜѵǔɔӱϖĂͱ\x88ƨɃƐӭʖ',
                                        'description': "ɕӌƅ$ǕпȳͲцӑƫ҅ӎÂ'4țɐ´ĩFӝƟʠvҋԓŅͿ͵",
                                        'default_value': 'ÊȈ҆ĄɁΠćĠ¶ˁȃʅˤéW¸Ϸʲ÷ѧȗʸϼӗÚϴɫωӰB',
                                    },
                            {
                                        'key': 'ʎ\x8aҳДƷνҔҔæΠ',
                                        'description': 'ǉϥɺŅ&ұɀõƒхɅƜРɪL\x97˜Ɔ(ͻ#ÉМ6Ϝ»ҟȼΥҒ',
                                        'default_value': 'ŦΔŤʂǮɣ=Șě(ӬЪ˂ʅ¥˟ùβЯӎ˅ʚѷ\u038bΦáý˄˥ø',
                                    },
                            {
                                        'key': 'ĘІԪųĈcџ\x84КѣѮŠΎ-ЀϾĻћTлXį-ΙѬǭüųȹΨ',
                                        'description': 'чbİ®ͽpƄĉчɕǧ\x8cȭˊʟ҈ȎΓѐųӤҶƗǹͳœȳƅ^ſ',
                                        'default_value': 'Дgƕu˪ϑύЮҶԈʧ\x8fɳϒvˤæǞÖȸϽƂϜϭϱƥÓ\x9dѺ˅',
                                    },
                            {
                                        'key': 'κϨŖаȇ\x89\u0378Ǘ\u0378ϦæҘԤɥџJƪʈϕɽϯʉȴʞ¯Ͼѹ',
                                        'description': 'ɉӻ1Ӷ˦ƨ\x8cɾEɊϭМzҟĪ¿ʥƥұǑ.nɞ\u0378˫ΙС¿˞Ϥ',
                                        'default_value': ' ҖÚǸIȟѹΈb˷ЩѡØ*ɢʃɔҕ΅ǬĖȉɏȟϠʺͼǣňϏ',
                                    },
                            {
                                        'key': 'ʓɑɓåҟʜĲ˽mĚ\u03a2χр¨?ěźʓüXŐŭʷ҇ΖɸǂɈĐǆ',
                                        'description': 'Ȕɝ_ʺ˰ĹƇ˴ΐǵʃѭŰ{ʔ˟ɛȲϏЁѝƳżǩԬОǙʬƛˇ',
                                        'default_value': '',
                                    },
                            {
                                        'key': '\x8a\x8dȠʇӹƂȈŞԏӔȆʑ]',
                                        'description': 'ӥ·Ӈü±ñҚϚǚ˘м\x95Ǫ҆ĶǎʾȡȜеƠ˩\x8dļȦŭ˃Yғƛ',
                                        'default_value': 'ÆЕ\x96$īΈԀɋß^ȌɀνɁӂŤº÷Ğyɏ¼ЄҮƅгŌɞǰş',
                                    },
                            {
                                        'key': 'ӗ\x85ǵɰwəӯ',
                                        'description': 'ђßȕҞЭɎŅԛÞŜŊ\x89μӅĬºʞ#ЗȆȷŬƛŅİƣ˩ŻĽ¾',
                                        'default_value': 'ȣ˚ěÊʂ¾˹ΩϿԩʅĿʨ9ɋŁӚӿʓ҈ӗҀǂŦӆ;ɻǁƪˡ',
                                    },
                            {
                                        'key': 'ӼĂϡӫʊ\x9cЌξͼӞ',
                                        'description': '×OҠôșƹþʳ͵Ұ\x89˧ȰŐÊčˡƉȬŗa\x8eГȝχK\x89Хщχ',
                                        'default_value': 'ԊӕǷΏXȌӯȼΡĀǟă\u0382˽[ǜ˩¹άģӓĵЕØûʫɺæϭĖ',
                                    },
                            {
                                        'key': '£´ɜőϩüˉǰӽīɕӜʥǪѡӦɠ҇Ǌˋ2ѳu΅˱˹Üʞ\xa0ō',
                                        'description': 'гʄRүҽʣÿɚЀG»ж\x81í÷@ĒÔŃː§ǋзѿïГӂІ҆Ƽ',
                                        'default_value': 'ǦĖ9ϱěѓϗҶɢϵη˸ԐɛɊϒЊƻ«ȈʛҬǍǈů\x9dӨ϶Ӹŗ',
                                    },
                        ],
                },
                {
                    'name': 'ϽRҞʔɊǀӕҟА͵ƍүԐĆѷƑϿƌˠ\x81˺ϙkƅǜϞϤǻϊš',
                    'description': 'ҟŚǨİԈɜТŨqɬÖ¦șī˓ΧŏԌͼīwɥΆHӿĊύ˙ʫƲ',
                    'target_id': '{ԇ\x86Әŕ¾éɛȗǚЍg҆ǖʦǍ^ŰϱΊIɱƠȟĄҜҹǕӑҔ',
                    'parameters': [
                            {
                                        'key': ')ѤŚαǹÛɦºȉÜϴғƗҳū\x85êӊпǔIҫӃňȞϾɮϪèʍ',
                                        'description': 'ϿBěȊƓӵϟъȶĂĂϘƴѨE˹\x95ƿʴɿ˚ǩ϶Б¿ӧӓͷӦД',
                                        'default_value': 'ҕɝƴ˙өȿŊμӹ˕7ϭќϮȰ\x9cŰƧ;ʩ\x7fΞ¸ǧӛÚώȵɉĠ',
                                    },
                            {
                                        'key': 'ЁЪɤ:ϿɱǭӘŢҫCǝфǖŪыƭŐ͵ʳōӲԩ˧ʳȩӏƇo!',
                                        'description': 'Ǫ¼Ǿň·Ѻ\x9fǐćē|ĲɍǣΣƕΘѼũӻɰǝ\x81ԃѶ\u0380ǯ7ǩй',
                                        'default_value': '˷Η˷ǷŨɒË\x99\x8bʹĳáԧƸ¢ΌƖіӧȔѧʳýňşȲ¼ɧҾ˰',
                                    },
                            {
                                        'key': 'ķʞ˔Хμζv,Âϯӗąѩ»ĎΜ҂ɱɕ˰ɅӞԦϴȕżÛɓȓ¤',
                                        'description': 'РҢШ®ѵº҆ǥҙĐņҚsπĲƇғĺҕʲȦԇԟӮƀUӻ˟ɺł',
                                        'default_value': 'ʜ҄ˈȤϋˋkёӺӉH¢ͻϣÔіŹĮˤʈȦÎњҾғźПϒːˡ',
                                    },
                            {
                                        'key': 'ɓÑÑƦ˒Ӽ˻g\u038bHđɮ#Ԛ§ӁĒ\x86%ɗԑĖ<ф± ӌʻЪѕ',
                                        'description': 'Ӆŭɻ8ȐӞύʶͶÌȈǛ˥ŜųƠQϋƛǀԥҬ\u03a2ǪӂƼľрӁı',
                                        'default_value': 'Ǒˁ˾ϤˆмÍƩΘѻȨбίѣĜĂΧцƑɝӿʅȺʹuĀѬØǮФ',
                                    },
                            {
                                        'key': ')ҏӫˉžѹRĸfԪКЎЬƷǣƷԐӃřį²єӎˬԬ×ьsŚc',
                                        'description': 'ӂыsɬĶЭ\x83ʝзήэϏƴɌ͵ƸȽβҐήΖȜŝKǭӃѭԔǬ˃',
                                        'default_value': 'ǄРζ˽ȵț҈ťƩɜзХɜQҪăƛƃҶ³ɿMК:УƧ_ŹrϺ',
                                    },
                            {
                                        'key': 'Ԡ.',
                                        'description': 'ǝʮ˞ƑѨ\x99ʘͲЖЗSŵɆÛԣѯϴȞЦ΅ěβɲȏωɘ»˳\x9bϣ',
                                        'default_value': 'ˡԆ˺ӘȱэфһǮϙψǺʧҊ§}ɨĨйԜț˂ǿ\xa0ɷfОúΕƥ',
                                    },
                            {
                                        'key': 'ħӊɨOЁӘȝAņѭήЙ\u03a2аσÈ˂З®ƚΎɇǁxф\u0382ǒЛɱɲ',
                                        'description': "ǉíхѻΡ˖'!лԙϔˎВӊǅ^βѕҟȹÑҶà˧˟ыѥȇȣʡ",
                                        'default_value': ';ǦɱēɽŮ\u0380ϜƓȰԑ˭żΈУ˫ŭԬʔǠӵ3ȗǼϱʯСѢϥӯ',
                                    },
                            {
                                        'key': '˷ȃƭŷſňζńɢɟэɲϡΥϐŶәʟ',
                                        'description': 'īúΡGġȪͶќAĝϕƢʧ҈Ƅ\x93ӁΕъǆҷ`ƀœďԑȃВȸX',
                                        'default_value': 'Πѵˆ5ΠәʝԙƬˀ˞пéÓΒǯġѱƎʅƗťƩмЖӱ\u0379¢ȅƪ',
                                    },
                            {
                                        'key': 'Ο)ǰȸӞL×ÊѤKΏʻѱvʴpӮkŋҾEȰƣǅЪͿƟ˺ӘԠ',
                                        'description': 'ÐōǊµ¦ԍʩưѓʀҖ\x9eȫΎ£ȈȉŋŭǫŉÈ»ȕӀʠԭȈʟķ',
                                        'default_value': '˘ӧɍшäΒё¯ŷʽήˈυǂЖмАԆ˛ҍϭ\x91ˠԈʗžѳ˚ŀ;',
                                    },
                            {
                                        'key': 'Ȣ¨͵˟¼χʅ˽ÙΙøˏ˹ŦΙԣ˨ŀѝԡÓ´ΊȩǭÐáȊÑɁ',
                                        'description': 'ʫшĬԅМӏѥēӄȋүʹͺǧʦĕŽ\x89\x81ʇʹюҊȠȦѻίʟǚ\x91',
                                        'default_value': "ǞÿɢȆȝĂ'КȝëĭíFȞΕɴԓɧƙĜІëԊɹȹΆϩϿūù",
                                    },
                        ],
                },
                {
                    'name': 'ƇǾ§ʜĮȓИȌȟʷͶƵCȥӟѰѩɾĔϣсЀғҳςӹ¹чҋш',
                    'description': 'ѣȐњί°ӅȌҫϴȰ҅ɻˤ΅ʽƼƁʫȒȡȨɞōƮȉɷКΦʝ%',
                    'target_id': '˺хǿ˕\x97ЎˤŢӽ8ЋҲåΨˋ`Ǯʆďпо\x84ŠѯǕˊЀҐрƊ',
                    'parameters': [
                            {
                                        'key': 'ē',
                                        'description': 'ȱXĺÞéÎhŢǋɼʼƛљ˜ʗϢčǃҧӾԘzȥ˱\x9bσ˖ϼɤӶ',
                                        'default_value': 'ǌʌүϧƣƐԑȫԬʂ΄ӽЋ˪ӂʅяɊj˸ãʧɻ\\\u038bɗBѪӣϸ',
                                    },
                            {
                                        'key': 'ǊǸ¶ýʈҜǡғђԑƾҬǍѪќíΏъЌØ˷ƑϧˁВ¼ǰћӎQ',
                                        'description': '!ғЂƢ±\x89Ѫӷ˨˰\x99ǙʏwӲΛҐ\x90ɫçϯ\x80fK\x9c@Ԕw1Ȧ',
                                        'default_value': 'θ*ªĎͺҀЂɣИѩЌkϪƄǤ¼ʤȑҟȥԃȮԪƓȱƻѴӴҫP',
                                    },
                            {
                                        'key': 'ɛ°ũʍũȾêЙˋȨѳԬũýŕĄюơˁʍƌԧÿȄƆŁɃΈώĮ',
                                        'description': 'ɛNȩԙԚƴˍӝ\x94ȾĪʋ\x9cĨʱĹƗʉ\xadʆɬѯ´Ÿ\x7fыȢªǓǅ',
                                        'default_value': 'ƨ/\x9cйС°˃ѕǵĄǀԎƿПȖ˳ûçțʆŜӌ>ȭлɻÌ\xa0\x99Ű',
                                    },
                            {
                                        'key': '\x95ʧœЩ>ÞѤ˾Б˯ĞɺȎ˳Ћэџϧцď˸àˮΥͻÇԆ@шȦ',
                                        'description': 'ЦȖϪǾ˟ʮάȲɡßăɟƅɁŰĺѯǱ\xadȩӦʫϹȹӜkǾѦȲ´',
                                        'default_value': 'ҐȽϰ˯6ȍҾ¯UͿϟǉˉϛȟΣɤEлÔwË«ѹ',
                                    },
                            {
                                        'key': '¼¤ĉԀŷ°кϬ§ȭÆ\u03a2ӮPѼǰăѩÇ¼ŉȥʈґ2ʽŔǣ5Ә',
                                        'description': 'ПΒQɅӾȪԪʆĈφƞɃŘÚȴƎùвɇʌҴƦŻǰ%Ч¸Ҏκǂ',
                                        'default_value': 'ƃƖ\x88DɴҦļԉȼƾη\x8f¹¯϶ˑԕÈǈιϋ{XȜԖԕȥĠПͶ',
                                    },
                            {
                                        'key': '\u038dåФŜӋTǷԕƀϟčΝǩǶюȒÀĪүҢԣѝəĀȇхʣ¸ԡȠ',
                                        'description': 'ҁãÆͱҪɢƖǊǶƥǱρ\x9bǾӠМΡΐҠȂµƧў҂ΙԥɧƷǲŞ',
                                        'default_value': 'οωƭХ´ӝɪɚѯЀϝœƟ)ʶôΪ\x80ʧ˝ԒӺ˟ҊZ\x85҇ʲĚÒ',
                                    },
                            {
                                        'key': 'ҍªȁɛϾνɸӔȑΈKԢаЖpԫЀӥΐ\x88ү҂ȦӐʅ\x85ůŭȆµ',
                                        'description': 'ԙŝɢчåÓŗƺ˅Iœ҆ȍÜҨҔԝʬãϪ˻ý˒ȡԦĠӘчǱȀ',
                                        'default_value': 'ΣƃЁYPϽϔȀӃɬȋԨƭǔèâўʤΙ\x8dҦ˓р˧ȟˌaƝƈҾ',
                                    },
                            {
                                        'key': 'ƩǾϸʅȇҥԌȈ',
                                        'description': 'ҕľVЭӫыɞɣԛʦҙҪԜ˕\x8dĂӥ˹ѫʮҋɕȯ˗Xөǧmǫ͵',
                                        'default_value': '\x8dRͱĘКś¼щ!}ǙхӱѪӃҤȟ˯ŋÔaȜԎѐȤĤʲиǨɝ',
                                    },
                            {
                                        'key': 'ŵɯ˻ШΌʤ˙ӦʐĖkƔƢξ',
                                        'description': 'ˉŒĳːѬƯΊΎВšϴɹԛǋГʵϐɓѲҒ,ț\x89ÚȥϩǉʈɩΊ',
                                        'default_value': 'ΐƐ˱żџLҪğÍǴŮĖȖё¬Χҋʗ˔йeŁ ӿɧϏÎáϦƣ',
                                    },
                            {
                                        'key': 'Zɣɳҽ҈εЙœƘƏҤԡǖǼdȮŇɏ/ńȰҝñϿźǜͱ¨ˈł',
                                        'description': 'ЛʺÂɣȰӼ˓ƏѮҪΒÙԙĒŲļʈΈϿ+ԞзΓԬϳŠ˱Ĝ¶º',
                                        'default_value': '/ǈУǳékńԁԒÈĠͰȘӮғɐ˪ƩҒ\x8cЌσˮ˾іµɼǅƉĶ',
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
