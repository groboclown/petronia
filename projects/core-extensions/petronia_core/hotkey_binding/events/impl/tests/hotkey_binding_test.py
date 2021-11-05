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
                'ȯҢɹѢ˸˷ҥǱȵCҐ',
                'ʪ',
                'А\x9dјѨҋέϏӜɌԈõ˨ɯȶǽІˋ҇͵˥=Ǟ',
            ],
            'comment': 'ùɖìѳхоѓӝĝ\u0382Φ\x94ØaʑϨʅȹȗǹ±Ý҄ǆϹέΫ˕RӘ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                'Ȯ',
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
            'key': 'ƈҾҬ˜чѧԅˢȯĴ[ĒɔȈOʪͲΔ˙ʕȨǋÕΎÒȞʵǚßǑ',
            'value': 'ѷƷәpҖʩщɕĀªV˝ȰŵȤҸσ\x83ȏпƥđƦӮʊƤŰ΅Ŗő',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ү',

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
            'target_id': '҅ҦҊГʯȭɘόѢˆʤгτчɺɁȗ҉ɮӏ~ϼіúӝȗǽǖ\u0382X',
            'parameters': [
                {
                    'key': 'ѧ:МǎӨō-«&å˪>ϮˋˑΟKŒáōĂʁǻ/ȆGюkԋě',
                    'value': '_ÑϡϋԖѦÀúȢЂ˫ğ\x84ɅȳϢ\x870ˤӏƉ',
                },
                {
                    'key': 'ʆÊˀѬϨɨϖǃǓƠʘŪhŴ\x94ҵʑŷѠѴʂȂ~ɞуť\x93ӿήК',
                    'value': 'Άϖ\x9fͲȼ\x93ǁɁȖŉϡŬʻĩΠÞEĉ\u0378wӚΕϨΟ,ѣîæŒů',
                },
                {
                    'key': 'Ƹ\x95ƨjһԣŗϛ~ӸĉԏϓɓԄ>ʪ;ÊƯņʊ{ѫɘУ',
                    'value': "ӻԆғιƸѺҥӝϑƚ7øǚ9˷ʅӻÈÓǴϫơō҃Ԑͻϒέӗ'",
                },
                {
                    'key': 'ʳȅɛѡϚϯıƗҨƷβȆØɽɨď҂ŮâȾñƓ<Ѿ˒Ь\x97˧&Ǖ',
                    'value': '\x84ƄƯʹǕăģԀϷͰāӕïɁ˙ɤȫӽԄ¾ϒӀ÷bLΑӹџåŐ',
                },
                {
                    'key': 'pϨƊȱЏЄ\x8cϾ˗ĮŗϑͶӷѳ',
                    'value': 'ãԒ«Ò\x8dԎϓȄOɬĉ˗Ǥөӭ˼ӂɖͱʭƠъĦɲφºˌн«O',
                },
                {
                    'key': 'ŴȞîѧӐͲĈǔȪĝӄӹϦƓԜѠϏǆӿԦРDĦԀÍɖҿŝΛұ',
                    'value': 'ӜőȰǊυ˽΄Ə§ҹʵΘǣ\x99Ź¡ǿŔ!Ӑԧ~ԟǴėŪҜǝҕϊ',
                },
                {
                    'key': '¼ˣӱӗ:rɳ\x88Ϩԅǟ0ȟū҉ƴϒČϠ;Ģ˾˸ԥȑ£âÙɤӊ',
                    'value': 'Ҏ¥ƥʈÈ#Ǝ%лȚ\u0380ǰȟЛĖʗϻэаʣƲС\x92ϚǊDҏĖɤġ',
                },
                {
                    'key': 'ĬŗEɳŝ˴ПʛԍҨÏƺԞxŮǲǔȅÑŰGřеƖΨǜѷıƐӅ',
                    'value': 'ʴKԪӽƦ´ɘ_Ӯɩҁɵ҆ЍȉaӴΓ˗8ʂЉʿ҃ͻˈʛϱɫ_',
                },
                {
                    'key': '¿ԃђɦʢĲsԂѪÂƆЇΜʴǒіʳYϗԤqҍɋƊɒ\xadȕƍi',
                    'value': 'ɸӈиЪčϨìǱѴĵĳΥʨàӅԖʪԣë˔ˁ\x8eϠθϦ¼Ҵ˴-ҙ',
                },
                {
                    'key': 'ϏÍūKǩԗӤȔĨǵж\\шÇĒʑҭԙųɃ4Ʈ0\x8bΗńБ\x9dÕφ',
                    'value': '¸ЊƈjȬćԟƼѾÐˋҎȀԨ цɋŒлϿϓ˕ԆΣTӐϟԇáԤ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ҩǙ»ӆư',

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
                'ϖ}dȒňƓ/ΤÉлŲҙ±',
                'ќљˎвžɀЏƣ϶ΘԨƝЏɩ',
                'Ȋʊ',
                'ƌӈ˳ԩğŸΓŠƾѓvˣЃċkƋŧǆˉԙɎ',
                'ùĢОӲ`ԇЮӌ Ҟ\x95ҤЙƂ\x95{ҀŖÊŁϲҾǠӣG',
                'ЗƀĻV¿ӬʨҕϰȩԉÔĀ\x8cʫŬfǬWԗȹΊʠňϿʟ˂ŜjF',
                'Ȉ˩ԫεĎӼєҵÝľèфĻҤƙǼӪŗɋԌɬ҃ǩ',
                '\x8aҲˌāʹ¾ΨѿȰĤëƿƟ',
                'ƟŞθĔҏ\x8dǢ)\x89ҺƳȿԂφψTvǔŌĄЃ˥;˽Ύ˄Ǣ',
                'ɽӝЊɺӾ¿iĴŐҮÈ',
            ],
            'comment': 'ˀʖȤЬƷ×ɼϣŰĢŵʤƁǚϧơмäԤМuKÛȪ=ɛάзοɻ',
            'event': {
                'target_id': 'ΑҴԪŹˤəǋˬКтɣӳӯɇĶʤϦѢɋίüƹ\x9cӥǰ˯u¬ȏϕ',
                'parameters': [
                    {
                            'key': 'ǟѢΊϾǹŵѸçȎӻķԤ\u0379ǆӆìõτĪɵʚуԕʶȍį%κ\x9fѹ',
                            'value': 'şƁȭӽјԔԫvӐ˄ĬϚʽԉΝȌҁRʖìȴкʿĖ\x98\\ΏºĤō',
                        },
                    {
                            'key': 'AŮ¸Ɣȓ0єÈ˜λȊѧƙĚʍ',
                            'value': 'ɐОñ3э\\%"ˈ\\?ŊţѺ\x88ƚыȱrȬѠϰˠȗłі£љѩч',
                        },
                    {
                            'key': 'UŦЅҘÃϹ3ʃǂΰǙѷчƙŦÌŋɌőјùƶƃǴ|Ω³ɳω`',
                            'value': 'ʹӂѲɹaБǓЄΩөǙţѻ°ζʫ¨ɰȨ\x94ҬǯƢŵțԄеØѕÊ',
                        },
                    {
                            'key': 'ʷŀ AҞɧʪӥпѯÊɪӼϡрϳҁȶß҄ǁÍʖԮϋÌƹÃŵξ',
                            'value': 'ŏȠͲɋwď-ǝΎ"˗Ƕʱѧʮ(ҸĞnɃЛϺɭ҂æӁҔȊϓĸ',
                        },
                    {
                            'key': '\u0379)єҵęЭŤν\u038dɫǼҪû˽bƩǂѠ',
                            'value': 'ĔїˋϲįѐҾԖΉŤƁʙķȖκƍéɎÖĿӽ҈υ\x85ʯǛԇ§ͻА',
                        },
                    {
                            'key': '0ũͶч\x86ĤʣдǸΔ\u0378ʔѢԧ˭\x82ƸμтҞ@ƗnǟƼкʝӊҴѢ',
                            'value': '˃Ԛ¸ˉԉƿgȫйƈξԀĆѹˬӸņɡH@ƴbǋă˟ƄδϏOЮ',
                        },
                    {
                            'key': 'ɳéȝϥ¦ȹõѹƪƾ´φɭΓǏ·å³ʶӡʙҴ§ˠȋϜ%ŭĚѓ',
                            'value': 'ёĒ\x8b ƅʥʿƠƚηǏг\x98ύĔ>ҽӬĔѬλΑ\u0378VɲɂƴϛϏҭ',
                        },
                    {
                            'key': 'ê\x8aʱӋȥϻƴӘ\x7fʍŦ\x97ѻŐ\x83ʿҮ',
                            'value': '\x80ɉĬЁ[ҡƟɫíɭқ§ҰŦͱҒŔɎŔɺӅŕəϕΔЩƥ ЕǊ',
                        },
                    {
                            'key': 'ŚΠ˕Σ˸ҹƩϴȠƫˎȭѱɄπЏѴΨӴшεǚȻɗѧƍǡƟӥϰ',
                            'value': 'ԂÕӭЦ*ǻұYΚǒʣƎϰʮSɔūΨϭҐƓȬɌǄīʢȠȄ\x95ˌ',
                        },
                    {
                            'key': 'ԣ¼b˳ҮėʳAˆŖĸӍȱЌβϴϘҥ?ӕƠΫтϩÖʞ',
                            'value': 'ɔwƓǫњÀЕƤΕõ\u0381ÓΫãӦŒʲCȅǾĤÛƄτÐřɼȲаʞ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ϛ',
            ],

            'event': {
                'target_id': '΄ɕǝѸǻ',
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
                'ҁ"ƇĦŒϺɻŘʂїϩɬ˅',
                'ѹч°ȦʧΘ',
                '\x7fБПˁЛ\u0381ϭрĪtƳżŚĈкϠ\x9e',
                'ǴϱȀÝʗĪ÷ɷӕҲʑνӼƻHХ',
                'ĨѵǬʧӰ¼ЌІѥŠ¹ÿԜΣ˫ϝҊŃ҃ѫǅ@ӊԧǠɮː',
                'юț',
                'ĀӟȫόǟŕʪɹʁʱǉȱȁɯѬ¤ˑļńˬ#ɣĭӕȬɓЋLƫʤ',
                'NВÑϨΪwѯӹ÷ǃҝдҏӪƘŽĦϓƜňƖp',
                "Ѐ\u0379ͷ'˛ǒ\x80ǟ",
                'ŭДϓЏȗ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ӿ',
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
            'key': 'ҏ²ô>\x99ȸҳϥřλϞáƽłŕĹѫǪ{Ғфǭ\x94ϧʹԕǤʰʕ˩',
            'description': '\\ΔԪŦȒğʯɺʎ»[ĢIƫӛʍҸ҆µOɒ¢ïƄ³}ƖЕˠŧ',
            'default_value': 'ѹȈҨҡԙ5ŹɴɪĔŦȮ\u038dϊƳԤơԆӽвʂϻ\x8fѠʧļɥɨɥŧ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Λ',

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
            'name': 'Τ<Ϫ\x88Ƽϴ0@ϽϧΘӄʳÊ\x89ɥDÚϷÄ~ɐxˑȽ',
            'description': 'G\u0381ƟϑĢǂƄɮϡɇØͿϝйɣËƾŇňϰÜ¸ŶđԃÇƘХʘH',
            'target_id': 'ķ¥ҦәźӾсА@ԘľҚǮĲԎěυΌŬ\x82ʯʁVӃԙБҽ˥əÝ',
            'parameters': [
                {
                    'key': 'ιĀҋĞεuѩɪκӗ˛\x9a\x8eЂːӭĀʮ_ϗȦΤƝǈȷhɅҰȕȣ',
                    'description': 'ӵЏ¦ͲĀˇǂżȟöҜűƎƖÏǒȻ#ЂĬũtŸѕʨӭ\x99ϟºӫ',
                    'default_value': 'ЭвΡƱϤЂʊˉ˴ЌËD5ӇʊŲ҈ïѾ1ΞЭšɍ˸ϧлƊʈÂ',
                },
                {
                    'key': 'ϡ¸ϠƿNϳǁІӟ˚ЇȎƫ¢ʕƄƁÖǥUĢϞξѣēӊċįƶΘ',
                    'description': '˟өϹДзѪlǐüƚÅǩ˧ѤўΖшŬþ°ĥӫϚЬ҃ǾͲûφӮ',
                    'default_value': '¦ʇηsȉɇːɡӃˡǸŴƽŠ΅VӚȯƕĴϦ˼ĨfҋђĈˋόa',
                },
                {
                    'key': 'ѴˑĬÿϿǯІƜíϽĬàʀͱƞАǕÒƷђѧ\x88AӺľɽћĦ',
                    'description': 'ӹԞƸɓϠ_ǾʇАŷΈҕǲœɦSȦĹȎͻѝ}ÇȘЕLϪԚʥÌ',
                    'default_value': 'ΧťʶόɐЊЦԝíƣƌƨżԋĘȿͷȜϙк\x86ȡҝŹƏ҂ԟНҲґ',
                },
                {
                    'key': 'тÕģǆПːʛҼ',
                    'description': 'ԒԒћ¦Ɵ˗¯ǘԉMµπҖш˽Ӭ˄ēИӒғу¢҅\x9a˥ґХʇǻ',
                    'default_value': '½ӵԦÜĳϷ{ԍ\u0379Ѿâ˒tư\x90űԮѣԬҽӷ˙ɱӟŭɷɾĹԩ\x8b',
                },
                {
                    'key': 'ǢЃʴŨ˵Ŕнg¥ĐƾņŁǂ˒əǑʸ°ǋ',
                    'description': 'ǀѼџʿұхтӺ>ƑʯҝΡͰŀԨˀÝƛȉƀəǊήɏҕɁϋ\u0383ʒ',
                    'default_value': 'ÈԉďƺςнÇ½ѹċӁ˒ƳżĘМǚǸˣѓǛ˺ϣϹ_\x83āѓ\x82"',
                },
                {
                    'key': 'ǀҧʍѲϩĹϋ˱ԜœΡˌф˔¦ӞßȆӅʄ)ǋҕ',
                    'description': '˴ϭԤȰѷϑŢϭưȬӰŖΒ˪Аőǭӄˀ\x93ə7Ŝ\x97\x99˒ʏϞ\u0382ε',
                    'default_value': 'ɫʏʨȐąȻŵʩļ҈ѲŏÒˈѝјӊŸԭʎíȾ˸5ʯӒѾ`ѵӗ',
                },
                {
                    'key': '˵Ϻәԁm#ԀTˎƍúǐśԟǸщpĨѐÍ\u0380ђWѕωǗӿȜwʵ',
                    'description': 'ǜʵчʀϫӥӲϤɕƀӋėďPȵǺǺĊҳķſђǚȼưѢҜƍDƸ',
                    'default_value': 'ʏŋѼȞҺҜͰŀαŊHɺ4ĵˤ¨ӨŭӧɚӇѻĖĈʉƨČÊȼ˾',
                },
                {
                    'key': 'ӭԌԁςȚѺгŘЧɧҠΞԓіĄjԖϛϊʾǑ°ԗȭǳҗ-Ԫώ\x9f',
                    'description': 'ƶϰ;ӡǞýȵӊӓ²ʯӅĉјnҍ҈Ʈ\x85ЀҹγήοϤŭЍΑ˝ ',
                    'default_value': 'ŚӗģеȄǦČϼǷɝʘȻ\x8dҧ˸ĈÓ\x98ǐЕӈӚĬΧɋ_ǝĭǌw',
                },
                {
                    'key': 'ӳλģќжKƳαɴ\u0379Ɖ\x95ŵϮхȃ;ήχѡƻǖoĢѵ˜ʁӭΏĉ',
                    'description': 'ϊŶÈδρǉȮɌƣȮËЉфɅʵJҬHɜӘӯ\u0383Ǐǰ\x99CËƍʑҊ',
                    'default_value': 'ƞȻɚɛŋ/Ǌҿ˽θήωYȂǗ˭qńÈЩә½ԭԢϊȣҁԢԎǘ',
                },
                {
                    'key': 'Ԭѹ¡Ɍϖʁӝ¶ \x89çǉóˬȴFΘϞɲʪӳɃЀɭ˧ƅǙχ%ԗ',
                    'description': 'ģҘЍԙc˨ǑҘиøÈӈӵõʔŊɷ΅ȻϺȲԛ<ɽҭʧQ\x97ԧ¿',
                    'default_value': 'Ϡ:ȸŝVӞϘª\x9bЅψЦδʘːҩχΫȲŏĞӪжʦԮхƏɌӦϫ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӰӀԖ',

            'target_id': 'ɻξӟѫ\x81',

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
                'target_id': 'ԅȉêZɌÌ7ԁŘˣĸΰӚϵšΫҋƸѠϤɦƺǄϖʚòĥ˜Ѭȱ',
                'parameters': [
                    {
                            'key': 'ԝҺѵ˘ÛńȉːģˏкӽԮҲί˲ǭƤԩɾƴҠ÷ǠͺȺĺʥϑ˫',
                            'value': 'ϏɰͳǋХТыԇÈҭĆϐήԙ˃СɰӍɌƦťπɿ\u0379ȡɁѨɉ²˝',
                        },
                    {
                            'key': 'ʖǍɻɪǎĹƬҦʸʕԏ˫rԩǯÀҳ[ƙΏƶʃΙ˙Ǖ%Ɨąȗʹ',
                            'value': 'ǔÚƠƴĦŅhӣÃˬūQԘ%¦ˍǨӒǖҸǞϓːӜÿɉӦιϮԨ',
                        },
                    {
                            'key': 'țfяϏԋ ѴiӋ Ԣʯǉ\x8b˗ϯȾȴǼTγȈԬѐfфɄэ\x94ů',
                            'value': 'ǒʒƣǋĺσΠԍûąϙΑȆ]θǛϙ\x95ʰYǔG>©ʯstӊЗѤ',
                        },
                    {
                            'key': '˥(\x8eԜ¦Ɩʸʦ¾ӆϗˀΘǐ\x87\u0378ЃѪ΅ҦԋîȤȅѻ*äԚͰĠ',
                            'value': 'ʁӖ®ƔјÃÇĨ<ƚ\x9cǍȥ;ƈ·ŁӈӽϙԖǬ\x81П˟ωԥƠ҂ǒ',
                        },
                    {
                            'key': 'ĽċͺʖϋХҁȞΘԖșƝȏʁҶ\u0383ȏĸÝśҒЯÖÞ7Eεe¢Ԥ',
                            'value': 'ǔ˵ɺ˦\x85ЁĸǿȎԎǊє˞ġMŨϝҤȿҸǼРыəҊmūͱģŉ',
                        },
                    {
                            'key': '$\xa0ĝ',
                            'value': 'ҍöĐԒҦʳє¦ŌǗöáҌ\u0379KˬʙQϬ\x99ÃʡɨȨ|ƄӺӄǘԎ',
                        },
                    {
                            'key': 'Ǻϗ«ʒӏʏHů¶àђӎ˰Â',
                            'value': '˄ĀȋϡƀΔƸΧƤĎȰ҇Ԑ(ϰΖУԈΥэƔԜ˴ȋșҖҸʸ«ю',
                        },
                    {
                            'key': 'Ǹ»ϵϸЉʈͱŽz·ԠбưƯԪÞ',
                            'value': 'řOØѽќ˭ӧʂɟȧ˔·\x99Ҹӈ҉ŪҥʕĺèЎԖŭơŮğǐȨɑ',
                        },
                    {
                            'key': '˯|ŢėÃԨɺäӪ\x90±·ϯΊƜǫƘғ҇҈çű',
                            'value': '҄ЬƂԁÆѮΣʢǛжǊѺųњҿ4aȋþǦ4Ðȣ˙ʀïŷlɫ\x87',
                        },
                    {
                            'key': 'Ŗɪϐɠ¢ů\x83ĈϲΞȅȼ˼ǣӌӸΜԈхЩĺǖʲԗȂmɉ\x81æL',
                            'value': 'ғÉŖӫԕǉąȷ×ӡÁЗӴƺƭ×тƿӕʹϠԐРѓlӷɟˉʛʙ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': '\x82ЏєƦ˦',
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
                'uȂΜǺȎϖŤʽ¿BǔƂԦŏύúƨ',
                "ѳȵ'˻ʬjҩưŊ˗ż˳μОΒҋ",
                'ʷҙ½ϤӢɿǱȒѺЮĂԛ1nʟΧӄǵӹzӂя҉ӓў˅Ŕ',
                'ɼµЪŇʬùЇԆˆҿԛӽҤӢ7}ҭÚ\u038b˖ȋƾɊίȎĎɁі',
                '?ȳƅƧӧӵҰ8½Ј\u038dÓĵɂДфŒ',
                'ӺѝǅΫΈ\x80&ϳԓԫВřƜ;ʖŋҹɨɚÀΓӾĞԁԍ]ʘӎˀʯ',
                'Ʋ§ǲȟŢyԎĔһYʠѡԨҮӡсǻěĢ\x9eԠMīȓǖҟ˰-ıμ',
                'Nƕϸ',
                'ʲeǇΎμūϖҺʍɉ\x81ʎεĭųȿ',
                'ӃɒѰĬȏ¯=ҽ:ԫҽȒ¶ň}˙ʳ|ˋǈʬӡё˖σê˨ϒðƭ',
            ],
            'event': {
                'target_id': 'ź΅ˣƒ˚\x8eԔӀЎӓǘϵ\x92ΥѡŒ˺Ƙ\x97ŭҠÅӚɼӺȉǑƕɁѻ',
                'parameters': [
                    {
                            'key': 'ĻѿːўȼͳγĘяѹХΞΜ2ɇ҈ԪӗǗѢĜ7ї˩ĘńǗӋħɮ',
                            'value': '҅хӞůſѓѫɴѻɡѸȣƯзÂǨ\u0381ΓУūˋϊϚӜΗų϶ҦЭƛ',
                        },
                    {
                            'key': 'ĠɈǄҚůԝўГ÷Ҟčѷ҇ЇȄɶǿ·КӇϲŜѫπЃԈʒˁǡд',
                            'value': 'ǌƎгӑөҰŸÆΗӪÏЪÓǪŵ!ČҝȽǍ,ɜjΫǨΉȏɉʙԄ',
                        },
                    {
                            'key': 'ƤMѷԃѕ[ųӱɸʸΥ',
                            'value': 'ƶ˜˗\x8eчǯŗȞПɴѧʘʦ(úєЦº\x9d\u0380˹\x8a¸ǋǑӜÀåϿĹ',
                        },
                    {
                            'key': 'Ƞɭ8πξή£ʬώèƬϠ7ȚȽěȈңb«ğďɼ0Sŗ~ϾȦŴ',
                            'value': 'Î\x9fΎ´ĺћßҳΟGΡԟʧӄӥԑȠАţȏˎўԝɜΠöDªƵπ',
                        },
                    {
                            'key': 'ĉ˛ѾӪ;˘ĠʡЮԠͳõSÏ!Ƕǻ}ЅƼĖĆͺ\x99˒#ôƳϫɄ',
                            'value': 'ѭȞʖeçȾ˶˱ҽ£ñȖ\xa0ѶӉɂѪ˱Ðƭɽζʟȷқвf}Хԫ',
                        },
                    {
                            'key': 'ÔяФСϦФκưɢѕőѕ\x96ʟǷ\x98ĽӀ1ĿӻʄǉêӣǯɜȫÉ7',
                            'value': 'ӎ˅ōφǜԙxϪɂВԨïǔӰäҖǖîĴɧµ\x97ĤȑȜ>żҕӶϟ',
                        },
                    {
                            'key': '˙Ǿ¼ŢȡĔ"\x8cҠǋͲʴҘӖ\x7fʧҬɜ\u038dӴћт©Тӎϡԁ½ĤÝ',
                            'value': 'ӹÃ\x87ӏƀϣҬĭɵɕˇźƃёpԬЅϴ҃ȂKӜȖīɗ<їɫ˄Ѳ',
                        },
                    {
                            'key': 'ȳ˃ѷˠĨvͼ',
                            'value': 'ϭ\x96ɢƀ_ЉƩєȵІΥȂƠ:\x82˄ȁтσѯÜУғ϶ŚѢγͶƦƽ',
                        },
                    {
                            'key': 'ӏƂϱӫ;Ȅˇõ\x84ɜ,јѴӧӯԥѸЅTѓƶҠшƛԮĒɾÂŁƁ',
                            'value': 'ȅȆçû˃ƋȝǟџyåĥĐƄÂиӡҏ0ˀέИэȅԑΐʧÜñӮ',
                        },
                    {
                            'key': '\x94ΝŮρϝłnѳƎ\u0378ҮɕΧóƷɈӄƲ\x93НеˢoűÈϕȍƭĿΠ',
                            'value': '\u03a2ҽĵыӀӁã2ªƯѴīуԒΈҌƾӈФԃŢϘ\u0383ŜďƔѕԥƣN',
                        },
                ],
            },
            'comment': 'bƵŰºҥΦϏȡ7ύє\x82:ϰԀϲǳɡԍ:!ǃÛ©ͰÇЁĀŮϚ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ŕ',
            ],

            'event': {
                'target_id': 'Īǽѡ±ϭ',
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
                'ҷʨϔǩH\x88ɠ(ӳ»řŝҵӋҜÃԝ˧ëƲӬ²ΚϞɊ',
                '~ƯȑħɀУΪRЅÎϏȚϘ',
                'μχȨɤҦԣ\x7fΈƾ',
                'ˡщʯΒΘˬèƖľƱӞԑ«ΥУċԏ\x9e҆ɦ',
                'Ě˷Ɏĥ',
                '_ήѡgϬӗƙԞȡԈǭыҼϷƕīњʠёſʱ',
                ',Ԉǆŭψ˅ȺЗ\x90Ķ%яſ',
                'ϷɄǻĀʋ˹ǤĖËǎƛŞȹЀϋŨȭ',
                'ӲςŚɢ˼Ɍ=˹ҥƥ',
                'wǥǶĦѿ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ȸȠǿǩ\x93ƸłıЫ\x93čπϪЇА;ӄѻΠϸtĄԖåùэӄͽĺ',
                            'ʃχeФC˼ѧ\x89ɪÙȚϖŹԌτĲɢ˖ĸ',
                            'dɎз\u038d\x91ĴȿÜĥΧ\x96ЕưRVуĪȃѽˈӧЀΩŤ¥ɠѢό',
                            'ǉʾǿЧʿǖ\xa0ů÷',
                            'ĘǞΏʓȅˍ.ÁļζѽөěGϳϣȑɁѩ˘Ģϯ',
                            'şʵÃˏçІėÑ˻ǋӍӂԆˢİлˋƓ·ԌζѪӁƎͻ¯ĖĜԚ',
                            'ɔΣŎҦιΥmʎ=āϔ',
                            'кЭЛʤїώΧɛǸǱʌϿԣƌ"',
                            'ȵðÿgƚϚˊљЇrƅWӤ˫ȨšʄôǳΉŧĊ˻Ȕ˹wќУ',
                        ],
                    'event': {
                            'target_id': 'ƭrɜȶ÷т2Ϻȱ\x81κƩОԡƃ^˓ҁɩѪ҅ćΛōԄԆǍМǜϗ',
                            'parameters': [
                                        {
                                                        'key': 'ìǼѽxO^ƺԞīƠДөĸ˻ÝǼԓʓћȾӿ˜ǡџzӸɂђͻʐ',
                                                        'value': 'ηнȤОҲɉȗʋԙϳ¾Ӿ*Ɍɳ˵ŧѮȩƞ҆śĤɣϘ(ϵЇԂČ',
                                                    },
                                        {
                                                        'key': '½ӓß§ǆƧӃÙѭԅԜŒnЄˊÈˆņζgĩУȪԅӾԨҧыȖϑ',
                                                        'value': 'ӵԂъσơːȁтΌϫƕˁ˲ϑÝ˸ʉÕɞ˸ĿӮеĝʒ҅þǥEҕ',
                                                    },
                                        {
                                                        'key': 'ˤз҄ȃІӻӴǎӗӀΣҲҝӄÐǋ\x9d-ǂкԙɻϨӢЦЕ϶ƕϴ҇',
                                                        'value': 'ЃȘ˻Á\x82ΕÎʮҜ\x9eʀыΜӡЂƕǣĻΟǟʲʓΙćɦЇþNǾƠ',
                                                    },
                                        {
                                                        'key': 'ŹōĊ\x84ɲ˃˚ӔгˀʲƣǄɷ\x9b\u0382ԆȡʇӽӘ\x86ĊІȀʝԓŬ+ʉ',
                                                        'value': 'ˡ_ɍӓ\x84ѥI¥ÜѳјҸ!ƷσʮӂαÎϊʄ\x9fғǔΎȓÑ#ŐX',
                                                    },
                                        {
                                                        'key': '˳Ϥ«ŰҹԚδÓˬ\x91kӔƇЙѥѭВԢČӠиŵ8ǄHϚ©ʣtǼ',
                                                        'value': 'ͻΔӫąҒåúˋѻÞã&ʛЃMӻƀϑƃЎɮЂˏѥÕĒƗʏ҉ȁ',
                                                    },
                                        {
                                                        'key': "ΪĊĈϛԠâЯҎɔ˚џ\u0382ӵĝʺԎҘԏӉĮɮɗҧыԙǹʆŖ;'",
                                                        'value': 'ϯiÓˑžӚRПĊǮ\u0381ԣƘQңņīϋɕóɸς>ИȵƅÚȅ0Ɨ',
                                                    },
                                        {
                                                        'key': 'ȏҊdԘʷζ¼\x98Ԩ·Ó©ƚϋӽԐ˳ʽϒɷΑͿɄǷÏʑ!5ϋË',
                                                        'value': 'ʦˌƍɑɉż˩жžІ΅˩ƆӷŪĎЗӥ\xadùƓǲԩùƵ˫âȨʌ<',
                                                    },
                                        {
                                                        'key': 'ɞȌȲĵǕѪÞɨ˔ҿσˏ\xa0˜ƣû΅҃ËǉѝʲΡ˹ˬˋԦύ¥ώ',
                                                        'value': 'ɮѿɸyňƬåӆМŹʀϔEϳгǥĪсɅ\x94Ȫķ+ʴǻȨДѮƟЧ',
                                                    },
                                        {
                                                        'key': 'Źƺɿ.˒ԤыĤ´Ǧ˱ΕʹČщɛ',
                                                        'value': 'ț҆§ɏUӞŗϲȬ3ѓʈĴUӍƉԦѦëĉµǨΔßˈԧǨ҇ҐΆ',
                                                    },
                                        {
                                                        'key': 'ʐΆӸҜʶӘтȸćƹ˔ź\xa0ϮŘӰɬï5ʐτ=ӪȥǨʀXʐƀɵ',
                                                        'value': 'ζȭȀʮǃŸҪϢ«ȪлͻʿΑƥxυҿ»ҷĂ)ƝņͶϬ8ɱƊ³',
                                                    },
                                    ],
                        },
                    'comment': 'ҙȹФϚӄʞλȳϦѱÅ˶ϿídGңȭɢŶʅӳŦĸ˘gԮˤ˯ˡ',
                },
                {
                    'keys': [
                            'Ѹц˩mǤʥàʙ\x7f',
                            'ȢơˈɄ˯Әã$ɂ',
                            'Æ҉ʳ\x7fŕνƕΨǳ˛ÉӭηˤӐΠԈͿƼĻ',
                            'ɧЂąŕǍϿÂɖ~\x93',
                            'ҦϨѴǁЧˢőӫʲЉȀ\x86',
                            '\x8eӜ',
                            'ЁԍщÌ.ʉ',
                            'ӠчÀUǢԇчȃƃ\x8cӷõ\x8aʖʿ>ҳψ¿ċɷVΗԏνA',
                            '˺˽ŅʇѓϹƨ#Ȁԇ\x9fҏ˶ĠȉɣӫƶRлɼύ¯Ȅ',
                            'Ĩȳόӷ҉Сӓ',
                        ],
                    'event': {
                            'target_id': 'ōМӬԤ˽BÙҭƛԩѡ7˩ЬӞų\u0378Ԡʹȗϥ\x90ƘӀϗҟӞĽÞõ',
                            'parameters': [
                                        {
                                                        'key': 'ҭVĲʌ\x8aːҙЖƀΘƩŁґƷωžʸǐɒǊʋԀȻЎȑӔѵ²ɖΤ',
                                                        'value': 'Ъ|ӆ˓ąΩϿΌ¦ŚыőøҋƉĬ\x94цΡŹЭЩ˙þЩ°3ƽRɍ',
                                                    },
                                        {
                                                        'key': '£Pʽиȃκɛ˙Ψ\xa0ÕεѻȺǥȏƃѬȞӍƗŰӪÜҢ˯јĄӷϾ',
                                                        'value': 'ǚϤԑǆăΝ\x7fʷиц\xa0ƚԝԛϟҙm˯ŦèηȬƧΧοeԊԒɱʠ',
                                                    },
                                        {
                                                        'key': 'ǻ¢ļɁӖԨδçӿuϻӘ>ԬϞ',
                                                        'value': 'ѳψҏ˸ӻӟѻſdȝȇϝǉ\x86ĉȖź҅ӋáȳÐƎёԣК˟YѠɠ',
                                                    },
                                        {
                                                        'key': 'ȭΊҥ:ΖΈ\x84˹ăΘęϳ\u0382ӥÛįԩÓɴÝʣɪɖ˲ɹȷȇѝÿÆ',
                                                        'value': 'ӵҏĶƍŐ\x8f\x84˭Ь˷ʹϔь:КbͼʓĬӢɈɤͶíʞτȑǸEτ',
                                                    },
                                        {
                                                        'key': 'ʁҿǂǟ±υϾȑɁҸÆ2ȔƻũƴҎъǯ¯ĻâħЙȩΕԣȥ\x9dԕ',
                                                        'value': '9ɭǅͿтƘ\x96АƋǐƛϚФгϻƆÖёȟϘͻӚŎì˓ҏӝäҰȈ',
                                                    },
                                        {
                                                        'key': 'ŒĔļ',
                                                        'value': 'ĕŃϦӟļƧϱТ»^ɾæԮԢÎɕЉ˗Ӡӑї˝Ϥ}үСɃȟπæ',
                                                    },
                                        {
                                                        'key': 'ˍξ˂Õ°Ĭ¾΅ǞȒȝöĳȧʥpȔøϿӱͷˏøТʃĔʓ\x8fąʈ',
                                                        'value': 'Ǌ˓ӛb\x81Йʧӂ}ХСϿ΄zɚȂϙӥǔżœҌʓĹǅǍeд\x8aȰ',
                                                    },
                                        {
                                                        'key': 'ЉňθӶʤӸŏǰӇϦЭ\x81ѵψäƀĘňʾŉǝĵӭѼƩɨ΅NʯФ',
                                                        'value': 'π˧\x83ǢůХҸáрҥʸΫѴʜКɤŔÒъÊ\\ӫȬӔюԖԤʟÂæ',
                                                    },
                                        {
                                                        'key': 'ʜҔʇӢԗƢɫҦԊғMɲȒӃȺӳʦθɓ@ǂɚȽӤΨʁÇԖѐ҅',
                                                        'value': 'εҪSʹʄJΌӗѪѦȐɶǵɌUŘŞҘȰκӌ]ǷԦ҇ǓƋKKǳ',
                                                    },
                                        {
                                                        'key': 'ҪɜȫōäʎѰө&¬VғŎǵϦͲӽȴϭĘӾÅ+рɞҤԇʊˠԫ',
                                                        'value': 'Њ\x8aԍјЯРöȡ]˻ƅÏċʴĵù˅\x7fϙýàӕҩϹøT/¥Љэ',
                                                    },
                                    ],
                        },
                    'comment': 'ƈǹҺͱϻɬί\\\x8aϺ¬љʄD¨\x97Ñϴ7ϬˠԪĨΉʸÆȏԣ-ԡ',
                },
                {
                    'keys': [
                            'ɍ\x82\x8fȨӢˋȒpѐɕɦŴҔ',
                            'QȤǏ҂Ͳ;ŸȎȬɪԟµӒҝСsȬǀƭÁÁӓ',
                            '\x8cȅĖŸӗ˕ƼѶҞҸUǆ˛ȺϚӕǷ¨tиуҢƿVǇЫѫ',
                            'ªÒſȱ',
                            'ĆˉÆӂɸѧǵąЋRҬ¤ӟ\u0382Ƌɲ.',
                            'ɁƐļǂԅ\u0383ȹρôˍԣ½ȮϖGƪʮʕ\x83ʣӎʼǯЗӧeҥЅψɠ',
                            '\x8aїǰϻ΅ѝȣШѢɽԪԑ',
                            'ƀǌһϊʔƁЛĬћіÀҌЋ҆·ј¬рӇϽ',
                            'ѿȵӅσżĩƚǴІŵřԠ',
                            'Ңƌѡɴ',
                        ],
                    'event': {
                            'target_id': 'ԩDԑțёѶs΄˭ɵŋӛЙРΗԛѵíˏ˂ŬӦŽ%ЁԒӼOϬȨ',
                            'parameters': [
                                        {
                                                        'key': 'Ҡ˛˺ӿʾЍNɢːǘҾ΅ůŐɝҜƷʌH7ġɉҴǚǧƢѨŢҍȁ',
                                                        'value': '˺әW¦џԬͳюЁǧϖÂo$\x83ǂƈȗŘƆˡÆĒȉϒϣOȬǍǽ',
                                                    },
                                        {
                                                        'key': 'șġ¥Ȑ¡qϦȂҊϛfˇГɎЀΡƽТЃӄзԃƫǸɦҡǈªΕΨ',
                                                        'value': 'Ǖ\x84˔҆ɹѾÐɪƻĲȻ˽ѮѐŞтѫҝǩӦʳȳõǏ¨ʱŗĪђđ',
                                                    },
                                        {
                                                        'key': 'ʶÛ ҾɢʠѠŝȿÍćԀҍȉ\x95ӆԚ[ӝѧLǷŐҶшǦ"Ƙ¹á',
                                                        'value': 'ԕӸɂϬʓƋфҢîȏǽɵɭǒȝˡĹ\x99юǪҰjԕȜʷӵͽvνß',
                                                    },
                                        {
                                                        'key': 'ћԚƂɁȠŪʀƋţԎʾѶξǮɁƘ§űωƜǎ\x83ˆ\x8aɮɳҦοѻ\x9b',
                                                        'value': 'ůºѧϸϜϧѱΰĉңI˰ʏδ#ėҵȴ˕ʥцҴbɥǿɀƒdƒҹ',
                                                    },
                                        {
                                                        'key': 'ɞѱóƇȎĠǃԇ\u03a2ǆŨȢˡҒʭΠƷıͰĎӠҍǮѱƬ"\x86οκÄ',
                                                        'value': 'ó«ŐŧƊӡ¿Ҫ\u03a2ҹкɜĦɰǐőӹ\u0383HӂЧЙε\x9dӦÂɶτǄʨ',
                                                    },
                                        {
                                                        'key': 'ρĿ·Ȧ\x80ЙӥcБѓԭӒԠѺ˩҇ѵŦΟϞɏÆǠy˞ƧĞӉԍΤ',
                                                        'value': 'δҫ"ԂёŷěTƺȌӁÿȕʻŮͷƯǺůӘұ¢qǵĝǹɊʂϋǊ',
                                                    },
                                        {
                                                        'key': 'Ҩ¾ǪȇиÃМxēƎнԊ\x92ˆ1ԖďɶлȹÇʗɞȜɣĲʻӖˀ˞',
                                                        'value': 'ͶѢϞюOǦм¶Ë\u038b\u0378ʇŁϞѮ˩ϝơ@țʨϘ\x98ӫȎüȡ:ёϋ',
                                                    },
                                        {
                                                        'key': 'Τʆ\x90Ϩ3ˡƳΫ˭ҝőԘĵϻƱƶVУʛќϚы˄ˋЇ.[·еγ',
                                                        'value': 'ʊЍ˂ŠǤwĖ«ĨǩӪϭђäΦʹŪќѱƪśɵέʓʭЀӘɲ²ҹ',
                                                    },
                                        {
                                                        'key': 'ІĊҸХΆˀеŵϝͳƷƂρήσюгаθ˄ÍžɑǣşѨƵˢZ¨',
                                                        'value': 'ҸԨ3ƪ˴ѓ\x9ašҭǐ˂ɹϤƭҍ΄ώѧïѢʐ˔ʈƪōѢÓϵŚԙ',
                                                    },
                                        {
                                                        'key': 'DuŭǹВǷ ǥ\x88ŨœάԌǰΩƲȪтȒǯčɾԑʩίĹɊƼ˱ͱ',
                                                        'value': '˓ǚԫ˱˒҉ѻΈɨĉȂҕ¯й×ɮωɲшҚ\u038dԘĪIΠ҂ӛɤťӴ',
                                                    },
                                    ],
                        },
                    'comment': 'сǬх҅ёΘədőȖȿЂвŠӨîνγ<˳ɹǐ¼ӼƛϚNǰcľ',
                },
                {
                    'keys': [
                            'źĿѷ\u0383\x8eѹͼƤѝӐ˞ȼӴР',
                            'ȋˎǚЉŹ\u0381\x9bɴÆͱɌƟƳȾɚ7±˵',
                            'ǂѳʘȤ',
                            'ȷЪäʺͽɯʴ҈р\u0378ѵˣҽ¨sĴʳƈҷδǾĤǘĞŧƑє',
                            'XпĐ˕˧ǑÍ ɱHȕҸ',
                            '\x90ƽ҉ȜΧOͽӃÅwϲҽĀӒÇЙԨ',
                            '\u038dΆåjѩԄęƂ',
                            'ЈţѫӺŉ\x96ӕóЌ¨ƢϢʿͷÅχϼһ҈ʶ3Üγɣϱ\u038bɧұӅ©',
                            'ɮ˳Ӽ÷ЬѬӑƁŕԂӡˈɼɒÅġҘɍeĭì\u038dȲʼ',
                            'ҞҲ҃ΝƉЩҚi~',
                        ],
                    'event': {
                            'target_id': 'ʳ/ʲĻƵԨɠ[ԢļƺҮȄбɾłѵʷύϽ˖ҊЧӗ\x8bǮ~ʸȡԖ',
                            'parameters': [
                                        {
                                                        'key': 'ˁѨ×ʌϲȋԎΏ¯ΡƩľӍW£2ǹӢѮӐ©pѰρɿɛӣɑЄ ',
                                                        'value': 'ǑƷÒʗˇėЖԉʩ˶\u03a2ѿԖҀĴЌҹϚłγϕ?˔з;ӕũɼ\u038dϋ',
                                                    },
                                        {
                                                        'key': 'ÈлԉǈƫɬӜĥЂʘʐĈ\x84ЅњǬöѰϒǹĊiƍѹ\x93ńπ!ϙӵ',
                                                        'value': 'ҢЈ\x97ΟȆ;FĘŻɏǐʤԫÀéȺǄʖԒǜƁŝͷĸĞȖХѸΑө',
                                                    },
                                        {
                                                        'key': 'qŋқf˔ſѣ˂Èæñȍԑŵ˗ˊ',
                                                        'value': 'μáŘȻΖGSʔ7\x8dԡԆłИǘóϤӰҺϝņʀҔmԒǣŝʥ\x81Ӱ',
                                                    },
                                        {
                                                        'key': 'ӌԂRԔȷӚȎ\x9eΆʂŃøȺӀϗĬϊƫȸӭ\\Ӿҋκ\x9fԏќѿȌӞ',
                                                        'value': 'ЅѡʭͺˎǙřů˩ŹʂǿĴ¦үƤƙƖ˦ǂ˂σιǊʽʎŴԖȆʅ',
                                                    },
                                        {
                                                        'key': 'ҾϤhȂǪѼқǞʛȹѻǰ±ŰÑpЌȏÍхŋΊEB(æǜҖѿӹ',
                                                        'value': 'ʊ*+ŭ҇ærЅŵТΰ¯·҈ԪΰԦȀª»ôǋοÀӗӽ\x98ӏȤФ',
                                                    },
                                        {
                                                        'key': 'ŌƉǲΣ',
                                                        'value': 'Бɶ{șͶЀф҃Œşз˸ȉΌͷ×¹xĤӯшӹƗąǈԟаȂʿţ',
                                                    },
                                        {
                                                        'key': 'ΖȯϷ ΏȃÖāӓЅІƮ˹Ů#Ǘ\xa0ЙʇȤÆʆɕє2Ȱ·ЁǸë',
                                                        'value': '\x85ǑÝĀȕ\x89ͷK)˜Ǳʅɰɳȴ^ҌǙĳ\u0378ɖͱϯɾˮѸҏɥФШ',
                                                    },
                                        {
                                                        'key': 'MӶяƉӬΧ˒ĳўӦǊԀΉÎWǺ˸%ɰǍψ\x96ʂè6ЄҋƬΈɉ',
                                                        'value': 'ɆƶѦ\x94²ʺάɮӲȻЀʧӧЁʰԃő˚·нʁϼĐǇįЍҮɉӲʺ',
                                                    },
                                        {
                                                        'key': 'Ȣѝ$ТΞ¤èƛ',
                                                        'value': 'ǸǋËµʢ˶§ԑȬ˕ĒҎʏκȌɳʖŃ\u0382Ǯ˧оğʕӵъǽӘǌ˫',
                                                    },
                                        {
                                                        'key': 'ģҸӏЕȟϟςʂOĄïӧҰǧˑȪ˗ҖбǬɄƲɯ',
                                                        'value': 'ѡѓяǑĮáӋú˜ҖԬєɽƗӼʱʳ{ѐǤÌʏԤʨģд\x91ɆΖ\x94',
                                                    },
                                    ],
                        },
                    'comment': 'ЪĂϮɂґԭÑеγӝȰӯƞ)ǪͳIĤԬǄͰɭʱĲЃӢю˨˥њ',
                },
                {
                    'keys': [
                            'ʇƣ#ǬŗʚҟǤMӓĸǲȿϨс|ɂγňɾòҲ·',
                            'ѿА˒ԭʰȥр¯-\x9e',
                            'ƠʎʲȂӟ҉ǗӯȦ\x9fгΚ\x8bğʉΒʨ?σӐ¾˒ЬЁˎβ',
                            '-ϛаˬȑȖÐžȱˡ',
                            'Ÿȹ˵ɱ\x7fάɴqŒǵ҅ʷ˝а',
                            ' ',
                            'ŪӑȓȾɰƓʶϯǔ҉ɘǌΏīʳ\x9e˔φșЄƯŘλ²9µɞҏ',
                            'ҪѫѾџúɷǽԞƕíơњ\x9fɬӕŊɒΔ',
                            '\x9eȪϕ´ϘËѲьßGгSҰÑȂȸк',
                            'ε˖\x89\u0383ЗσØ',
                        ],
                    'event': {
                            'target_id': 'ùͽԇȮΏҞΰQҜы\x8dǗǽʠ˺ǆҵBîӇGĊŏǛʗɪϩҤћǘ',
                            'parameters': [
                                        {
                                                        'key': 'ãӶǆϑŚ˂ΐšǡΥǩƃƾώӥͿǳsYTɓEǁ',
                                                        'value': '˷Ð¡tÇӤ͵ö´ȥĞŊ5ҩtȴ\x91˦˜ϡΏłɾǟɨɣÿʬӹӌ',
                                                    },
                                        {
                                                        'key': 'ϖʮ 9ūӶ˾ɥ0ӠўƱįʸàĳӇаa:ϒľ$6ĴȓKΩЅҺ',
                                                        'value': 'ƚҲɯzǛȲY\x88Öź&ȡηĒċӬΓmŪȀeŏ[ϹϱŘ.ѽҖ\x95',
                                                    },
                                        {
                                                        'key': 'Ƒ\x80ԈˏӑҲǽǃæӝѺҼӸҟƟƧӨƖȃĎϧʬǴӛσ&ɤȥöϔ',
                                                        'value': 'ɳԁǞԞǔǝαоʜƓχĶΎ¥ўƉúÉзô˨ҴƾǸɚ\x89ԞͰрĄ',
                                                    },
                                        {
                                                        'key': 'ËщԠ χƌX\x80kӫƦąҬƶøөǵΧɛ¬ȠŅŉ\x9f\x95',
                                                        'value': 'ΥΨdƼd\x95ȭϮdjdȳӁ9ʸԕʈĽҎĝχhû\x86ҕϯеӰƿѯ',
                                                    },
                                        {
                                                        'key': 'ӎŠũӷƟϚŷƛ\x84ҷӑҿӆҘC«ĢҤ\x9bӐϛƘβĕǙӶgЖӽΡ',
                                                        'value': 'Ӎǵ˴ƋǆЍ5\u038bɥțÓƛ³ԓυƂ<ӼŽRӁĘϟ×ӆjÑ\u0380ģԍ',
                                                    },
                                        {
                                                        'key': 'ɘψϱ',
                                                        'value': 'ĤƂɶөɨȩ˱ʢ\x8eʗӒǘŉǃŠſƽ˩Ʒʐʹα\x8cιGőԮĖͶϗ',
                                                    },
                                        {
                                                        'key': 'ʏӽÇͱлӴԔƑĽѧωʌъ\x90ǞαɭҙȭgчvЉуӏºѢҖnȍ',
                                                        'value': 'ŇʭƵXӯԤҌʺŮƹєтԟi˫˛ӣûϾ϶gӓ=ā3ςϣў¸ɐ',
                                                    },
                                        {
                                                        'key': 'ӝbωĬ˓£ǕÃmǪMљȵǿċ\x81\u0379˽¸ûğļZϳпÅ"˪ЁЩ',
                                                        'value': 'ҏŪķӲҁ˵rȠĪќТѾлɧÜҸѽԩÊˮɳģӗď\x9aӸ¾Ϋ˃ŝ',
                                                    },
                                        {
                                                        'key': 'ҌΓΚрӔԒ\x87\x87EĥӀσĊĒӈғəȢИʴơdŒϖζʹǭͶМɾ',
                                                        'value': 'ΫŚЙ϶ÙɰҋæʏʠƏțǕсЯ\x9eЭӠʿÿƑϖżʑЍіȃƘϑʛ',
                                                    },
                                        {
                                                        'key': 'ѤΥǭʸӅÄʕͶʚǘПԂԂæҍǩŏЬ`ě|¿ĽԒB\x87ƥΉh\x9c',
                                                        'value': 'pӰƓӵ\x80ʑ˱ÑǂҷƠ\x8aʇǀŒÄćķҳşһϓƕɕӪіЃʾǹ¼',
                                                    },
                                    ],
                        },
                    'comment': 'иǂӀÈрΓRɰΜĖӪɎϡŸԑʆǏǽfφˋŢЀ_˰ƐӻMѽā',
                },
                {
                    'keys': [
                            'ːʘŐŲӯƽΕ',
                            'ɠŪ\u03a2ӡǲȦѩ',
                            'șǎ5ѯѺǋʬ',
                            "\x8eƟ\x80ɚ\x89ů9Х'Лʘ\x82ѯЧȘѾìɿŞƪÉ",
                            'Ϊΰƴ˹ӾÙ¬ͻêþлǾ\x7fͺʦˇϦř҆',
                            'ǪνʲŁШΏљЂȺ\x8dôʾŎɊœ\x8cÏȳΙҔ\u038dRɠǧЊϊJЌƪ',
                            'ʠ˨yɻ',
                            'ΞʤӟʚГȇҚŢ7ѪȒėԜʨ˖Ɨ\x8fɶyƓяȏt˹\x96Ӏ',
                            '.õӅ·˻ԛњĘΗġѨΤ˄Ĥʲȼț',
                            'őÇˌΧžѹȾɈƊ\x84àЉъкRй/ҳ',
                        ],
                    'event': {
                            'target_id': 'ԖƾφǝÔØǃфǝÇ©Ůχјσʂe΄ԛτԧӷϘĿȆЫƹԐЎӖ',
                            'parameters': [
                                        {
                                                        'key': 'ªБŚưÁԜҿϰǘ3\x90ȞɗʂϿåǢңĽЄəӪȇʡƾТ\x8dƵĈę',
                                                        'value': 'Ǻɓң˸үʎЅȓŋǐØ¯Ћ˸ЉԆӌǻƠˌŀɒ˾ӘʁŸĤԊԀΡ',
                                                    },
                                        {
                                                        'key': 'ɾȫЯԅɚĵϾȷT˃ПǂĠƣçȩĻ\x8aƗ×ƯɊʟµÓǖvĴ>Ή',
                                                        'value': 'űƿƦј\x83ͷɁɊκɞýĉɯͳxĈȝŰʯǜқƴΉɇΚǷȽ&ѵŽ',
                                                    },
                                        {
                                                        'key': 'ǑwŜKƭɒ\x87ͼƇ\x92ȹҦʙNƟԊΏʊԨȫŐ<ьĨ',
                                                        'value': "έǴΜбǏѶȺΊƋʂЙӗ\u0383ĵȐ˾˾ȽÓ'WĘņГëΔķԈǵƮ",
                                                    },
                                        {
                                                        'key': '˹Ŀн^¯ЕюӜԮΒ[ʪÁԩȣˬÃɨϦϱӠԥҦŦԡțˆӋӑ\x95',
                                                        'value': 'О)ǘɯiԝ\x8aǴӆԛҙĭ҈Ȝőǻ}˩\x99\x8cĖч<Ü´čŬƵʷǊ',
                                                    },
                                        {
                                                        'key': 'ѵ\x8cΈĊĹ҉έԅƀĈ.˱AüȵӉЦ×ъħGĲń<ӻɭˁϋŁŨ',
                                                        'value': 'ɥЀϋҟԪӾϷγǶƛҹʐԭ˂шɀ϶ǸϊЗ҈+ŴΆсɑЕԔƂԅ',
                                                    },
                                        {
                                                        'key': '¾ıʺӉƼíõԌɇȿŰȪ˱ЕšŴ',
                                                        'value': 'ѫԔȆǊҮʯϣЀCҡʿʇΎύД˓ӅƢӣĺÍ˅҇ȸƙǒɧԀˠԜ',
                                                    },
                                        {
                                                        'key': 'ͺҦʲΓʩɉƎǱқŪŶьĢԙȠĸӑƫŨhҲȯӖ{ϘԡˆԌΏԬ',
                                                        'value': 'ƶ\x9dȋ˶ʳǻKư¡\x9eȕǎȚѪЀԥҢǤ΅ш[ǡӄҕѢͻ/ԦȟͿ',
                                                    },
                                        {
                                                        'key': "ȧϞǐ˚ȕѢɃƷӌӪȅΘҹԄ'ʬʱƨ˟0ÒǄǛ¹ɼʞųȃ",
                                                        'value': 'ԏͳӺѝɑĴƤlҘśȬϦķїӋϥԊͳјȒўèɯҷ\x7fʟΆíГº',
                                                    },
                                        {
                                                        'key': 'ȡԇϞǙюĦɌǈ\x83рψƔό·ƟÑÞҚƦįдŇȥҤʎыƱ¶ѳɅ',
                                                        'value': 'ȒΈ)ʹʇ½Υӻ\u03a2Ѳɇ˫ĺͻԓӉĢŦɑϊƖĺHΔӕӾͿѷhȧ',
                                                    },
                                        {
                                                        'key': 'ƎԘěϞΫԭşЫӱƬƪӦãʔ\x88',
                                                        'value': 'ȂԔΔŃў\u03a2ǜƗҵ\x98ѻӏ¾ɓ\x9a=ʋǲĲԡԌĈĨʃўǶƽìѿǐ',
                                                    },
                                    ],
                        },
                    'comment': 'ȚɎΰÑųэėҥũΆѱŬѲüԈӣƶʨƄϿчӺƄ\x98ʭΧқˁiŰ',
                },
                {
                    'keys': [
                            'ƪ',
                            'ӈŴџϳʛªǽğÿѰѪßfӰҜɤҤʙěσϱЖ',
                            'pҁЋǜƱŴԣƦ;ϗʀ',
                            'њƣŝ',
                            'Ӛͽ©đʻ±ϓӍԫˉѶƓ',
                            '²йҊѿѻцԚЅ',
                            'Ȋѥɒ2żĎͳˢɘͼ˧ƾϯӽi',
                            'Ȫ¶ĦÞб\x80ӌ҇хҵԃϘˇӨфЯʄƥè\x89Ԑ˷§ƸƢӎҹǶi8',
                            'ǈz\x9cǉýԮԇѹ',
                            'ƿɛ[~ʋ¼wŦŝĘг\x94Ψїƪòą:ҏӨS϶ϗѺŸ',
                        ],
                    'event': {
                            'target_id': 'Ȁp˷ǞƠӽмΉɱѓΊĎӖØğĵҧМӆϐƁĔȷͰЉšцÕƓ͵',
                            'parameters': [
                                        {
                                                        'key': 'ƐΏӑŇˋϖ\x95ѱϲҞˁ˚ĉ\u0381öȘɁΕԪʕð',
                                                        'value': 'ΪϝĿÞϥ˧˚ɳϾЃ\x8aɗΎŔIȞξƀҺͶŜʾфΏЗȵΕо\u0381Ҫ',
                                                    },
                                        {
                                                        'key': 'FůʻиɚºϒFƯÉīө²ψҩˬĮѫ\x8e˼ΪѧʅțҼȓѪҷͿ0',
                                                        'value': 'Ԗť˺˂ǢʺƗĐ@<ф-\x93ɽ\x8fбӚЁЬ҅ȦӜùʟǀĸʛåкǉ',
                                                    },
                                        {
                                                        'key': 'ĪļīԜƤϋӿř^ǀұπCҏϨδȒĩ]ǰϰŒǢȀφнŇϵ\x90\x84',
                                                        'value': 'Ñɍˮſ¬ЛËӰÓ6ТЪζȉʓ˴ԎҲɛȷѿŧÈôʿ˫¯\x88ӤԊ',
                                                    },
                                        {
                                                        'key': 'ԕ\x87ŻǏʟǊ˧ΡÚɦŰǄкĻgшɬσ˩7ѦԨɤӻɛ˸п!ˎŕ',
                                                        'value': 'ȚҞӺ˺·ÐȼˇɂȄœ\x9fϓκ˞ǪɧЯ±ȽňϊҚȬǥԦǑǏӢɚ',
                                                    },
                                        {
                                                        'key': 'Ԅ˱ɅяȯʚϪӽˎ\x82ԒЌËÜĢВÅȈϘʼҖ˾éǙ\x917ʗѡчʌ',
                                                        'value': 'ʅƈөԝϛθӣҜŢƵҳҬШřяέθʖтĴōðӰ_МкĎÕȆŘ',
                                                    },
                                        {
                                                        'key': '\u0382ʡ˕ԧÎͺѴľȪΧƄǵǆĐģ\x83˕ſ\u0379η¹6',
                                                        'value': 'tΰə\x80Γ˱Lҫҕˎ ɍ¢ͷɃʠúͲƀ\u0383ôʿǭӅχΐѓˋҀ¥',
                                                    },
                                        {
                                                        'key': '{ĖюҹрβȲÃĭɀƷηˤʢɅŒόɊG\x8aéůdπƬºΑėс˾',
                                                        'value': 'ъ>ҥϙͶ¬ĂҽʧΣϘŧȫͷɼŲʛҸˀŲҖЅsÈǞϨ\u0378L\x9bɃ',
                                                    },
                                        {
                                                        'key': 'ǹïȄƵdʔцґϺğȅƧѾϘԂΰ4Х\x80Ȃ¿Ä*ǘǖҰbȪ¶ː',
                                                        'value': 'Ǚь°ÿËЀǇƏɷåʵǡ\x97ǺŷŽƢəӂ;ůҝͱŰʝƅƱȮʂӘ',
                                                    },
                                        {
                                                        'key': 'Β\x96ҩȿD˲ȢϹ\u0378ʤ\x8fñ˚ͻӽАAȼɬӥҩž§',
                                                        'value': 'ǴϐʑΖʏпʹœ½Ҧͳ^ȘìЫ˞ˍϹźϓʏРɥԡ\x96ȡÿԛЦē',
                                                    },
                                        {
                                                        'key': 'ŕƇȎ',
                                                        'value': 'Ή\x8bѐ±ŉΨϦ˝ˏПҋʯƈҢʆb¤ņƊЫѫčЪρǁɖɭʄēѿ',
                                                    },
                                    ],
                        },
                    'comment': '»ǧˏǐӣʩ һұ˰˪ŅIôδҖǚǩ˒Β˨âѓͿњϴʯÙjŀ',
                },
                {
                    'keys': [
                            'ĈӌĨǙҬϴιҗԛΛрǏ\x90рǖʭŪþ',
                            'ǰɼΩͺн4Йƿ',
                            'Х˧Àº\\Ɠ',
                            'ªМӫrƿsҝʖӤȬś',
                            'ˀϭʢӖƧыŠЩԙʕоϡГͼƻʚЌԁƊ\x9fӊȗ',
                            'ҷѤēΔΆÜ΄@ЌқaΗÚ˂ѫњ',
                            'ĤʪæǾƿ',
                            'ǘ҅ũo\u0379ҚаŢʥƸ¸ɕķɉȘě˄Ïʭĵ²ɺ',
                            'ŕǼǠāĮШ',
                            'φϗtƕƵŝчpȈϥĶ\x96҆ȡʖӷΈ',
                        ],
                    'event': {
                            'target_id': 'ŧU˗ɪʠɩωǡϩÊİєңčŉˡҋşÖҲԎҳ?οΒƶɽЛŧd',
                            'parameters': [
                                        {
                                                        'key': 'ƏɶƞшϼĦĄʟǏґϼҩϟӒƗιŋс',
                                                        'value': 'ÍҏйӄŹԫɚϑԬp*ÕîБƓϭdƲǟ%#ңNϓźɩTˁӌǟ',
                                                    },
                                        {
                                                        'key': '×jƧҹ',
                                                        'value': 'ˤɕzӁӴɿѺϿʵ¸ĂқоȶƣÃǠǢͷӖϧѩ¾ťĲʫ*ѓФѭ',
                                                    },
                                        {
                                                        'key': 'ЇͿɲșгӹͱрЬȭƸɷҕвЩķӰͰͼιT˜',
                                                        'value': 'ҸΪƜ\u0383ɇɷƕd˄Éѐ˧ʻ˧ΦЛ˂ƢɤğĒ$ϛņҳΤǒЊǝ˝',
                                                    },
                                        {
                                                        'key': 'ƺȔIˎνε˯ǊÆh˰ԛͽϷиγ>ȄύȷƽǤ|ɮǴƳʞͼīi',
                                                        'value': '\u038bȋWǃǝȵϩ4ϊCˍˎšϰʬԊѷұśÔǌԔƽ,ʳӯȻɐƧZ',
                                                    },
                                        {
                                                        'key': 'ƌӇԖȡɘҟԏə҅\x91яϦͻϯ»˓ľʣӳʑƔôȵ/Ӽ\xadǥӤЛ½',
                                                        'value': '·ԍ˳±Ȅ˷ԜɭʹǜЄΰЇȴџԈ\x90ϰӓǾȡȬ҉ΥӦƻ\x87уĴЧ',
                                                    },
                                        {
                                                        'key': 'əʩʳĆɰѐ.ΚҫʠΖϠʥҗɔҖZȜƕˆͽ¸lĤ·æ¨˜\x93Ǣ',
                                                        'value': '8#ʪ\x9aԥɮŜМǯ{ψјΞ\x92άĪѐȱŨȊÏɵŧѨĿɳы©\x99\x97',
                                                    },
                                        {
                                                        'key': 'ά˞ƇАȻҏѝΡgĿåѮ\x96ǓɊƱҌС¯үƹΘѐčԔȷłɂϗè',
                                                        'value': '҆Ϙƙ&ĩȲѲыԏōɦǦӾԚǍĦɛɃĲȝŘӸκ\x80ȎΩ·ʛĄӬ',
                                                    },
                                        {
                                                        'key': 'ƐɏđɱЄĝÉϝrɪЮ˰ІъЛõʿ˜øʨтϲƣύіїҪȇʋȐ',
                                                        'value': 'ϡҾɅȘȂþңͽ˰³ԗѹσVҘ"ņʑӑ˳ԏÑѽʪ',
                                                    },
                                        {
                                                        'key': '˱ϹҕǦԧѴҵĈˠ#*eʛćϲˤʝēͻ\u038dҳƃЬ\x9b\xadɤ˄ǡΛŭ',
                                                        'value': 'ɽԕKʗ@ŅʹѮ2ԖϝӫӘ҈\u038dƱɤϐPɢʅĴÊƒȚ\x86ы¼ɋН',
                                                    },
                                        {
                                                        'key': 'ƍеЊ®"ЬҳäəɈŮǿƗ-˦ōʫ#\x9dZΕą',
                                                        'value': 'ʚÌȗʪċΉŐӾӸ¸ǙҫѡΈŜѐƵƎԩdTӶҷϬϏʜѢʮʠƥ',
                                                    },
                                    ],
                        },
                    'comment': 'Ȳѿ§ˣȑĳҭʫçv\x93ŤͿƖcʌˇ\x87Έҫӄɕ¸Ηɬ˒Ǩτ\x96ˤ',
                },
                {
                    'keys': [
                            'ÖҁΐʚұĕŋðņҐĞєƇΚĩԙɈʰθBřѤϞƨѠċɘķҫѿ',
                            'q#ǔħӕήȗԐĆȏȾɋтɜʦҮ',
                            'ȮÁƋː˔ɨrVˮρxɏƉҩ˒ҁɐϼŁĞ',
                            '҂ĚɍʲɀϵĖʝ\x8dÜЈɦӡҐrԖ\x9aԖɏŒƷӲѺӜ',
                            'ǉҙɰƉɮǈȋțȓͱΐǩÍӊÒҙ[ΔɡѤΏɱ˺\x9a\x84μȢԌ',
                            'ҩţЙχЂЉ¥6\x89Ô\x9cɧžҏȏŗĚȴΰθ',
                            'ӦÊ',
                            'ǜ',
                            'ϜϬ˻цƊªǕƨӇĞӹ6ǙÁжɅf',
                            '҂Ȫ-ˈ˲ȚĻǐХπŜɸҷɚǁȡ',
                        ],
                    'event': {
                            'target_id': 'ˆƎʚĀԠĳɧĴҵӢǪɣğşԝԔʤȗӯºӶɓ˭НHˑԀp«ԅ',
                            'parameters': [
                                        {
                                                        'key': 'ǁθӡεѓӍӾˁʜwȎҕ˻ʼуĘέŒÖЉ˃ȥ.ˎҮңˋɴȪн',
                                                        'value': 'pюĆȷԃ\u0381αʀËҒУӢŴ϶пӞɏʊǹöШȇϭɏΖԑτÃԮ˵',
                                                    },
                                        {
                                                        'key': 'ȍʺ\x98?ƅˍʕѹӭέƕǦʿԮĈÞ',
                                                        'value': 'Ќӫϱ˛ľƁžҷɂƤҗȰʰʅǬ`Д\x9e!ϚˈԪѤØǦŸ ԜĴɒ',
                                                    },
                                        {
                                                        'key': 'φΥǆǽѩś£ºɮʁɜȌёĈӦõYĬќѭӚ\x7fãʨ\x8cķÿ',
                                                        'value': 'Ө2ϫ}ŧϴҟƹƱΗԢԛВǊңʃҕ҇хӪԏǪɸʗólϴȥŲǀ',
                                                    },
                                        {
                                                        'key': 'đҖɚľŵҗʲƄϪˬȯǡΐʻΜŠ%Ы\x98ΦǵΉ ȴУ\u0379ԡӑǬɺ',
                                                        'value': 'ΞɝìНƇҐΚқϼįҕěÍщ˵ѷϢɸԃψəЈvЫѿɝҏȢȵЏ',
                                                    },
                                        {
                                                        'key': 'ϯČĊɏɏκғ˄ҺƎχ\x7fƞȎ\x9enȡȐˤˎːĒ<ԢģΞϬΐκϮ',
                                                        'value': 'о¯åҠӝǣˌ\x86g\x8fƣƏĬµÊƢǳԛǏƎӪϿҕǭʪĎľЀǚʫ',
                                                    },
                                        {
                                                        'key': 'ʃʠ«ΔS\x82Ǽ9ѝŹѥÂɐΝŕԀɡ\x9eŶɿΐЎҍωӅǥ˽ΒѥÕ',
                                                        'value': '1ŢӉĆёǚƆ˖\u0380ѭčјԏɬvΐЁɡƎJƟϰθѲ\u03a2α+ѻҙθ',
                                                    },
                                        {
                                                        'key': 'ÃԖĵ<f;ǓķçȈʚΔǄ×ɀÁӴːůɒˋǰϝƻ\x95\x8fƆӣÛͶ',
                                                        'value': 'ӁơɋҋʒÖԋʦΘðĚнKǨ˦öLǹΦʴѬʀƦ\x96ƳƂ[ȕԗʛ',
                                                    },
                                        {
                                                        'key': 'ı*ΓȃȂÌɷҴȉδ¦Λ\\\x9cĥиʣϺ¯ѧӸŭò˟˗ÒԀKҞʖ',
                                                        'value': 'úӸʸχѱʨԖɱνΗJƹȲ˷ԗЍ˱ƩӻӲƨɃĘÖϘӖ˦ϷơȾ',
                                                    },
                                        {
                                                        'key': 'ıƎ˜ΦËΔGʷǤ\x93ǪśΉӱԠǲƅ¦ҖšɌҽ˖ńęγӷƖŨˊ',
                                                        'value': 'ƂʩőʢɻϵӜϴͿùҀϯ˧ьѲӃԑèϘьːŮ0êΒɋ{ǰs;',
                                                    },
                                        {
                                                        'key': 'Ά¡йéҥϒњǬĿоλϸҫЍӫ\x94Ӽȣ%өДȗʜ>ƆԠ,Ŭʬι',
                                                        'value': 'ҪѿҁćŞԘ*Ź˙ɠȶҤƝƱȗӟαҭȶ˦ӹøѦƦĸíšӸҊѽ',
                                                    },
                                    ],
                        },
                    'comment': '˺ítʼʉΤуɷŋӑʆƔҕЯɟυȈӄȚŊȝЎAѸӃȑϪÀ\u038bë',
                },
                {
                    'keys': [
                            'ҜŔͱǼҍŪϬЧ4\x7fǁ',
                        ],
                    'event': {
                            'target_id': 'ĪĬȷʕҺ!ПʳгξßȩԍȃɐҳҬȎ¨sǔ˨ѡΒҏ˺Ĩΐ-ǟ',
                            'parameters': [
                                        {
                                                        'key': 'xϟі$Iцҗ½˧FОԦɉѭƮ˽ǖïιǘτϑТʢјҕVʻʔљ',
                                                        'value': 'ȼʈɯͰҫ\u0382Τ҉ΨӇїƤѣΉĠŠй|ˀпҽђҼˢѹ˾ķíŇӼ',
                                                    },
                                        {
                                                        'key': 'Âϗ\x83яуεȓɻцԂЅ¡ƸlĬʡˡю\x90ǽŉ˰MЩрNÄŁҔɼ',
                                                        'value': 'ѯQӉҶȠůɡѢϿǙʓtúĔ˖ҥǋҰʇЯȣϐάΩгʦӺ¿3ϔ',
                                                    },
                                        {
                                                        'key': 'ӣ',
                                                        'value': 'ʐÄβȵǪɊĿȓӫΘϋáΗ˷ɇԈкҬƺ@ʵЌȐħъђѰчKӳ',
                                                    },
                                        {
                                                        'key': 'ŠӞεĭÎ\x9fЫӛӑУrȰ£ɓ¯ҍN£¶',
                                                        'value': 'Єǳϳʚҵ\x90Ǩѝċ¨кїƘýшøƯ¡!ŝƳʆĉ϶ų҉Ԉѡ¾ɴ',
                                                    },
                                        {
                                                        'key': 'ýϲ4īũГеɆ˅ɭťɸȝŅɖ,\x8cñǶ\x82҄?%ȝÉԈҟȹ',
                                                        'value': '˹ƒŹɃԍƷːʗǰӝӀƣ\u0382ĳȓȎČöƤҧƌlĂǩҋѩδʊϒ΅',
                                                    },
                                        {
                                                        'key': '˕˸¯ΝӓʘȀϚfıȥŹUΩįȭÃ\x9cӠўҒ˭ӊÊӟɵƛǴƤѷ',
                                                        'value': 'ϸϕҊƬҾ=ҁћϠ΄΄qɿ\u038bϩҼƗÆsÒѰХƧYƏҼ±Ъщɳ',
                                                    },
                                        {
                                                        'key': 'ȎӥɦǛ\u038bɁ\x80ȥĄҝҽķ\u0381ÓҷѥʄӖԄЌǷ©рϒρ',
                                                        'value': 'ưӂԊѪͳуѕӧȺMɠ\x8eҸ\x92Εχ¤ŖЩрĦΫԈǄϏҺǵǁύѯ',
                                                    },
                                        {
                                                        'key': 'ú¸йÞ¥\u038b\x9f\x91Ĺ˞ˌΫðQȗļɎϑ\x8e¯ťЧʁϢӣӱąϛɣĉ',
                                                        'value': 'ƓʚēeʶƳIȉѾáϷѨɂГǻǱǑʋҾɯVǀў˗ʰɧѯҜÇӒ',
                                                    },
                                        {
                                                        'key': 'ĝōȚüӿƴ˶ʉÁҴǪȇ\u0380ıǟŝ½ê~çӰ\x99Ϛ˲ʺéҍԖϊƝ',
                                                        'value': '^șˋѸƗϥМßǝЗбʲđҘʌƱǞӱƃűɄ\x96\x80ҕÀͳÕɮΦԎ',
                                                    },
                                        {
                                                        'key': 'ұƹЃБǾȚӎҋǀǥҐӋήőҿİ\u038dғԛѱ\u038bӆĮϨ\\ȞЄƮMĢ',
                                                        'value': 'ˍϹЃ˷ӉɅӟӀȐƍ-ϖϖО˶ѤİΚˉтӕғѦɴɆ;˚ӬԐ˨',
                                                    },
                                    ],
                        },
                    'comment': 'ѲͽψɆ˧ǘŻǺʣΖԑǤ\u0379ú˹ǂɤʣˆƀɰҽЋǧɗӈƫϧPԟ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'ǚ',
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
            'name': '˚пϥɟ\x9c˚ŖȫÓȌÝϧӼʖљбȲɭʢZʽ\x92]\\ӢńӸȬ¥Э',
            'description': 'ԥϵԀЊδȡäё^δѹ0Ìlǜ\u038bì\x9bϳɔȘ\x99҇ԭϚ˒òЪĝ϶',
            'target_id': "˟òɷԃƙ'ңрͳ\x9bIiʸљ?aӚЍˈ˷ȭιɣѠǟƤhħĎȥ",
            'parameters': [
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԃĚȕ',

            'target_id': 'ɭͰǊɾΙ',

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
                    'name': 'ӪôОԇńҷȜǁ~xѶʲѵȶuʦľ§¨Ą\x8foǭ\u0380ԚƷϔħɛĤ',
                    'description': 'ȱňȄЎҎ4ͲĀźʻeȭ?ƀŌûͺ˦τђђɏǦǉϥǮҒʠƗϩ',
                    'target_id': 'ѱÜ\x93¿ƩFҽCƵțÊʿǑ˝ҋ˝ŷCȮVƑ¬ķбǇ˖ЎŇȭç',
                    'parameters': [
                            {
                                        'key': 'є',
                                        'description': 'ɷȒɳϔt©xˍɨ˧ϲѵмҰÝ˕ͺʡȸԖԞɸŽѶҩŸΧшиǴ',
                                        'default_value': 'ǣõYјҍʈʀɕ_ҜňǪԜʉ×mƮӍϲТϧύ±ѣɆ΄¦Ϯԍ\x99',
                                    },
                            {
                                        'key': 'kʝDɵ÷˳γӈɌȾ΄ÓbʉÙΩҖʦīʑIӼ×ɒϡʪˍNˋԧ',
                                        'description': 'ĆƯʈːԑŕŴάǝ8ƭҏόUďȐɒϗΒѭҊ҅˘āͳċæȤêº',
                                        'default_value': 'ɣ˯ӒЏӯɔҡҲϦάÍ˱ɀλOʀŚʷ˯\x82ήɅ\x98ʗĉPӚ^ɍ˙',
                                    },
                            {
                                        'key': 'ԡˑҦҟҭÅƛĲE҂ҍJĂԁƓԔ9Ԇ¹~ȍǣå!ԑ;ѶԉǺǾ',
                                        'description': 'ϝҼŝĄǮʒј$¶ψʹϨȑ\u0382ӓԕ2·ǃµÇƫîέʅϛ\\ϑѳȸ',
                                        'default_value': "ԫηʋ\u038dxƀɭŅ5ԓªŒʊ\x96ēұ\x9fōʖĚdɊїϬRϘ']\u0383Ƥ",
                                    },
                            {
                                        'key': 'Ţțǻ¢ёţ\u03a2ˢʐԑɽӎӈQǵŠǻҺũɃќ\x9coƣͼÏəȣήz',
                                        'description': '\x9eņҐԃʏѾΒӐǸʽuēǸ\u0380ëӻëÛƴҍÏҦ{Ǻ\x9eȩôQʣƘ',
                                        'default_value': 'РҀĕћʅοϴʭůQ|ΊϱӝşЍҏϐǮțȁʿѹϾǈ0\xa0*ЖÎ',
                                    },
                            {
                                        'key': '˾˼ιʛЉѝ3Ë˯δiԡʗgʺ7£øæӵˮħǨƫԊϑǷʤЅњ',
                                        'description': 'È¨àԩĺ"ȼǂ\xadπȟѯÌѸ;ÂɇʩɉʖʣмǐзƎҰÖϥС¡',
                                        'default_value': 'ͻИεʇǢPɾʷџϕɖжѼѦΧҨԇʖˁȥȯǭ¶ũɽǩΞɃɣľ',
                                    },
                            {
                                        'key': '\x80ϨöЙù³ԈǔѵӄɒƯѥҪĚȡƫɍşͶŀSŁԊѕě\x82ɳȐo',
                                        'description': 'ԆΒϲɤǝʴ˶ʨˊʹӜѭԋƖįÄøɦл\u038d\u0381ԫ×ӹϊġΡƻϤŹ',
                                        'default_value': '͵нӎʏȔŻҥÃŹ˶\x92ƽĴǳƺʦҠŮ˘˙ђԬɄǳӎοЀЀ.Ӕ',
                                    },
                            {
                                        'key': 'ǃѫΘú\x80Ļ',
                                        'description': 'ɨΣ_3ΗƞOɦ.;ȂȽˏӉʱ»ұъͱ˘ĤϑǍϩ\x83ϟ\x94џє*',
                                        'default_value': 'сȭ»ǐάʎ˗\x82äˁkƴ×ԗ¾ΎʫʀͰВǔGƏˬŞǘҴӃ?$',
                                    },
                            {
                                        'key': 'ҊŝÓăƏԒ˫\x80˔МɣòɀΒЌҰԞʹǜƟ˅ϓνƩα˖ʞŶԛ˟',
                                        'description': '˫ȥŰŵӌїɁЂǏőԅȃ.ɾҡѺ\x98мыťGҵđʫсĕţĂҩ˃',
                                        'default_value': 'ĠЛǌʶѲŦ\x8cхƄςÄʮsÈȣƙ¥Řǋā҈ВͽǐěҹƵƞřл',
                                    },
                            {
                                        'key': 'Ƨ˧ыΧaʞɈƉǼѬԎƝȀθĩΚΗĊ',
                                        'description': '\x8d¹ԟ\\ӦҼPƪ˪ɛцҡĎι\x8f΄ǅҠĩԏɞшѨѱ&ėŜԥ¥ŝ',
                                        'default_value': 'ЪʹNȾΥ҉Wˠ<ÿǤ|ΎΌŨȥȆȘ˒іȚǪŰԡƍƒҢ"җϖ',
                                    },
                            {
                                        'key': 'ƽūҨЋ',
                                        'description': '°ԘЌЙĺ+ʥǠͳ+λȔЍÉӳɎôǙԎҲɠѲӰҨΈsǍ\u0380ˁ²',
                                        'default_value': 'ĄѴ¹ѱЈ҅ζśυԂИJϏѫѐĭӒ{ȑͱЏǵɑʖ˙іÂUӅb',
                                    },
                        ],
                },
                {
                    'name': 'шɓSʾԡʶԆ¨V¢϶ɈɞЗǳϿĵ»ʠǐʓѧȿӞрȾŉÍ\u0382ū',
                    'description': 'Ł˱ԖҜЌȴƞrӫǣɢҔ҈њ#fϨӔğ҃Αƃ΅ҊðRѐь«ė',
                    'target_id': 'ЏƸπɰF¶ĿŹÞɲáƁƢƩƲ\xadԖϑįÜ˅ӞkӮʌΟӲЩѓ\x96',
                    'parameters': [
                            {
                                        'key': 'Ԃʨ\u0380§Ŧ҆RΩϝϼZðβɋΡºȤʫÔȑɌԠʪӘgSĘŜÓδ',
                                        'description': 'ͺԟnțĩҀ˫\u0383ȾЖтҺą\x8fľͳү\x81ӥϬҏŠБϓҭϼđӯәϓ',
                                        'default_value': 'ō˽\u038bÚӟϯΉĸbԣ͵ХӱѫȿȈƑƲВӔǸӌď˓ʖǿɷȦ Θ',
                                    },
                            {
                                        'key': 'əҴӟȝƆȲΪҊыϯNаΔϭҏ˥ҲƥÉƮПƸ΄Ҡ\x97\x8bŐӌŬȩ',
                                        'description': 'ΐĚĭψˤ¯ҟſ˷ϟƾĠ˱\u03a2ЪKƣŒğ9ƟτϾӉȳΧВɒ;҇',
                                        'default_value': 'Űѹ˞CǡƧĂӅҘӫԦёϞƀʡϋѣӋҵPӅŔǷƁƚѠɩɖӠп',
                                    },
                            {
                                        'key': '9ʔӲÌ\x84ʡͳɀŗÍɷ~ʘŜɀ҅iΡʶԤžϘåʟĀ!ɲѬɪR',
                                        'description': '£ʘϜyƿ²\x9bʧ˸ðÓͶæċɌѣǴ҇ƽń\x88șѴ\x95ɏĽRҵϼȎ',
                                        'default_value': '©Óϡ°ÛɿϹүŹʟϱБӸйɴʹäȹ˗ôê\u0383σ\u0379ƌºȨĦæʋ',
                                    },
                            {
                                        'key': 'éƅД¬ɫӳАѧǫʧӦϩ¬ӰρϐŷпΣϝҸüԔƔƷÁԮı¤Ҡ',
                                        'description': 'ͺӕҬ˽ǦЮgӗ͵҈Ϫɥ҂í½οͳ˄ӺͼɩƠϰÑɋѿM\x88ɇʦ',
                                        'default_value': 'Ͳ˝Њ\x86Ηà Ǭ!ӄ\x93ǥϑϑǐȆмȧí˒˅ƫέǮ6·ĶɝȐм',
                                    },
                            {
                                        'key': 'νąѵƿū',
                                        'description': 'ˡ\x8bȔҊ˾ƟȋÉɘӯĜſśӝǞыʒʞΔŏ·ǭǃſљʥß͵Ң˞',
                                        'default_value': 'ԛӻ·Ö҂λɣżȠƋɠĘzԥԛҗʎěѓG½ƽˢɃƗÆΒčʞȉ',
                                    },
                            {
                                        'key': 'ʻχBȫ$ŝƺĨǜÏȴҹʽǍvϱÀ\x9cɂЉɭύѡзÁǘќǞһĎ',
                                        'description': 'ҮɳгίǿϠǖ˓ͶÐͲ(ȘȦƧDȆҟ3µǑĿΓſϒʞƤĠËɷ',
                                        'default_value': 'ЙMʛ\u0378ɢɐԥҐůǬѦҜŢѝцȮԃɹЪϿҤҺɖř˳Ŵϧҿ[7',
                                    },
                            {
                                        'key': 'ʭϠт˪oβȤϰѵͰεǎѪÅƖƗ˓ĭ+ʱǡǟ',
                                        'description': 'Ȋ£ƵʔȉɯӾɭԪĂЖ0үҖ\x9fvӍ©Ԁ˷ЅΌѸŌĥȻY҄Ѻϓ',
                                        'default_value': 'ΊĤ\x93ʛǻřԌǜÛчҀԔ)ϐҌңDƯӈʻŭĽЏȸɟ čЉӺӞ',
                                    },
                            {
                                        'key': 'Įɦ ӓˠю¸ŸшƯĕɍҦĊˍˮˎȲ˄ǯɽӱtƈĖ$lӛaĞ',
                                        'description': 'ʼѤĴ,×Ԧ҇¯]½Ľ4ĵҕǠӷʮɓͰɊʊĿ϶čŹϢ҄ӉƝЮ',
                                        'default_value': 'éEȌϱǅĜ´Ҵƽ_ʟҹĂƖʘsˊÜҖѢўʫŤˉӺ˝Ƶɳσ|',
                                    },
                            {
                                        'key': 'yʞΝɣҜļϧϸİϯǙįѵʉʫƈĲðҲ¢ə',
                                        'description': '˻Ȣ\x86ԤňчǠ£ƍƭǩNĚÁʒƖѫīώ)ʉЌΘȊɏҳΜԞҦҜ',
                                        'default_value': '~ԍ3ӒϢˤѹʶ¥ɲѡêдϦĞƯfӸ<ӦêŰЊԇΩ\u0379ԎåɃʮ',
                                    },
                            {
                                        'key': "ѫɱӶҰƪJ|Eʬǃԩ\x8bɧČʞȊԖ'ϱǯơȁμϹơ",
                                        'description': 'ŪΆĊЗʹɜԕȃ\u0383ώƶJïѰǾŮȥǣΏĄ×˺ǬӡǊӨ҂ɼ҄ı',
                                        'default_value': '˄ãˢӳ)ç¼ŒЃˋƢFЧԆŪ˨ӸѐˮIӃΔÓʹkΚʥƥ˪p',
                                    },
                        ],
                },
                {
                    'name': 'ĄԁʂҁɶԕȟҪтà˛ʲƂĄ\x89ϺȲɍҘϺӽȔ\u038dԔκΩˇsĐ\\',
                    'description': 'ȞҌа#ЎӪҌӆȑƥķŜԣӐŊӵΝɶɼ!ĪǶƯҡơҟÍȠĈR',
                    'target_id': 'īȘǔąƄͱˑîмԩʰɣ·ӐÔĜȟēӥŪˈǈΗŦͲǥҴ\\ƄБ',
                    'parameters': [
                            {
                                        'key': 'ʂ£ԊȜȼʐӓΡʡªƈƈȨԍϱƎӓʤéїч\x9cϷǡԀԀЦŧ˚ʔ',
                                        'description': 'ӄөșԩѧѝȸ϶ËөƥʳŀʯԛğѤԓρ\x9bĆȶҁʑɡǓˌ\x87їĸ',
                                        'default_value': 'įȝ\x8eХĊƈʅĊҍΐɘƲżѰԎΒҨѼ,ȖȫΒȣ\x8d\x88ŹӝźǬʗ',
                                    },
                            {
                                        'key': 'ёԅϠØôдȂ˜ǭӋȗŝ!ɉóМȺʚäƲҖɡ϶Ԓ\x80ȊΚĉȋ`',
                                        'description': 'ѕįî`ʌŵͺŞȠRĚρЁ˭nάŸʠĴȞ`ȝǌ×ǋĳͿҴˋȈ',
                                        'default_value': 'ΈʽIǩƼ˦ɾÈ°ͻ^ǁǂŊHãǟŴηĜƲҷЈțǃҾǱӒˈɃ',
                                    },
                            {
                                        'key': 'ϼӠҧɬҢЇ˖ſ\x8eȬ˧КфɾҞӴǕÊĨѰϗɬûɣ\x99ċǈɁѱҝ',
                                        'description': 'űʁˀБҊð\x96ԅбϻұ\x94ΥʍƯɘ\xadΓџȅҷϋŨɳΊ˲YΞmʥ',
                                        'default_value': 'Ȇ»ȲΛ\x97ŝǸr\x92ȱҖĥǟɇͼȟɈΙʯȰŊҀĻÔǽɌԢ#Ȳ`',
                                    },
                            {
                                        'key': '@ыÕlкȉ3ӡȹԇʭȏ˟˯DȀũϋҤ~ѪʸČЃ\x99ШǌҍОԚ',
                                        'description': 'ԖŦ˟ȱǏΐŪÈЖƙс҉˼ԔŖǂљ҃ԢɌʅ\x83˩ϢÙϽњʘŵĨ',
                                        'default_value': 'ЅƁϤĊԓ\x9e\x93!´\x92юγǏLӠ|ҢȣϫʻдҟʖƷǢÍɏò\x98Ì',
                                    },
                            {
                                        'key': 'ӣʦÝƔ,ԗӸğϮëĢϟ˱Ûљ˵ɕʄ҃ɩˆɤ~źԀҔɋşƈɃ',
                                        'description': 'Ӝ\x97σÛΊÇѐԐƽȄāΚίӭӶϴЅĮ²ȈДȯлùЪʣϒʈÓԙ',
                                        'default_value': '\x93ď¡ɺ\x9eҙԔɀĂȒǐĕӾƑăЯ\x80ξĦ`Љ!΅ǍĴɉÝôƎɒ',
                                    },
                            {
                                        'key': 'ӥȐɇȿЋȾ\x88y&ýɣ\x85ŏӟīӊǘρͱеĄ\x8d4ѓЖǓɳ\\ѯѥ',
                                        'description': 'ˉҙ6ϻҒҥ<ŨǬŇ@ԤĈΜΰMʞƚβ\x89ʜƞѡήC§нȁåһ',
                                        'default_value': 'ŷŐâCѽϧƋKЉĿԜӋѹȟʊQҺΡÉˊʼӡÒǵ\u038bȱǱƓȖӺ',
                                    },
                            {
                                        'key': 'ÙƨŀͰÅĻƲŊǏ',
                                        'description': 'Ķ˟ӍȲʛΨӧѦӥÚƫҏơǇε˱ǺĈΈƫ˕ɐѴѵԇǇʳůѬɤ',
                                        'default_value': '½ьÝšϠƜ\x8bSŌýɒԐԫŤӄҼΰ˗ӱӼϿѰăŗȖVҜ\x84ϬЎ',
                                    },
                            {
                                        'key': 'ΜElĲԐʄҊè\x93вӺǥŹΏҟɸ>ɘҳƁЀÅ.',
                                        'description': 'ЂˏǎȲɬhΨьҹȏх&ҶϪbʔǯĖ˴\x8d˙τĴԮӚͷGˤ˲\x88',
                                        'default_value': '.ʬЂ·Ʋϟ§ŕӿһӹîӜҔʋƣϰԇũļċͲЌƀǖʿõɋбТ',
                                    },
                            {
                                        'key': 'ŽɳςªĽƨ9Г%ҌϮƸ˕ĕϹԏ˘Ү¯ªȑТʛȗԠʎӊԑԛǻ',
                                        'description': 'ŴŰњƥˡАŋʟy¯ѿԎК\x88ˇħĹǆϵ\x99φѿϦԪÕBȞҝϙɘ',
                                        'default_value': 'ΝŏγѠĸFѤĢ\x86ѧʑԨĕΊϲÍʝϖǘƲˠÙψɾҜС\x9eѿӴɀ',
                                    },
                            {
                                        'key': 'іȼҀвřχӪêļΠŝƩϩѲЎņůžøî˵nϟ˔ΘǮ*ɡҪϖ',
                                        'description': 'ϳȵªpΧиɅĻɅшťӽĒ}Ѕşѥ+˷ʚϮȦАҙĎGӒΑɇɋ',
                                        'default_value': 'Ŗ?ʃ˷ɝƕǦɥ¶ΣȆˠεŸґЌӸˁ¡ȠĕȵǀŖɘ˓˒ȒEò',
                                    },
                        ],
                },
                {
                    'name': 'ŌʢǯʠƁDm˷Ö˷SÑťφҒɵȼӭƱʠѴа˱šЬ˄ƈćҦȱ',
                    'description': 'ȺʔɖėˈϹʋЗӟΉңųԮĿмο·ɪԓӖσȥʃɼԡѴʞŲrʹ',
                    'target_id': 'Θϭ6ÆƃҾļžʷəĒ»МΠǮ\x9a΄ƆјӿіԚӡӺԄáˑԒžӊ',
                    'parameters': [
                            {
                                        'key': 'ɣÍɆÇӔρӉңʃҨə˧ӵɿʞԑˡϱʤЛ\u038dΏҬȘ£ÒʛŴҘǬ',
                                        'description': 'Ћĸ4ӓΧɻȼ͵ơȊͶǸԧȨӽĞƹʟgȫӵԎԃÁԋЏаʜϞѨ',
                                        'default_value': 'ŸĊʓԩģmӓŇùʨ\x80ǮʺUŨԫ\x99ύÒʄ\x93ͷӉɢȊɅϙƌѫУ',
                                    },
                            {
                                        'key': 'жʨ`Ǘ˘ĝϊѐŬǋˀƙƻоɃІǈ',
                                        'description': 'ӅɎϤĪӹ\x98ƭ˒ĨҩѹʍƵчʻȫŲʈЄϠ<ΝӰɤƃȳĿϵõЪ',
                                        'default_value': 'ӼȖЅƹѷóȪǯҧΛγŃӀʦЁϟʮwɷΣƕЬАΟƹф˻\u038d¤Ή',
                                    },
                            {
                                        'key': '˩ǫ×ΟЈфӨƧċҌŷǨЮpҸ˥ϖΖȠҎуϩӽɆˉūȁȽ=;',
                                        'description': 'Ο;Ů˭ȶ\x90ªÍƅFǙȏ¾PΧŖ^¹ҰΐҿӘƆāϫ/HĚƄx',
                                        'default_value': 'ϗɔԟȠ\u0381â\u0382ǓΠ\x81ǑΦӦԅʀщ˖ÀĴΨѪűҏ°ɓϤϗЀѢҿ',
                                    },
                            {
                                        'key': 'ʥќmѸԠě%\u0378čӋǌȃ˜˂ËƧ[ыɲ7·ͰĕșѢ?ǧ¸ΨX',
                                        'description': 'ԓōǔĄЋɜǧńЊſҼ¡üЈ$гǕщӦ`Żê]ǿҒѭҰ\x96Ƹı',
                                        'default_value': 'Ȃ[ƔľŪÜδ4Aα\u0380ʸτԦ\x8fǴ1oёѥʄȢ°ђϴʇÉԥŴШ',
                                    },
                            {
                                        'key': 'ŲѶҕƿќɿчрӓƀ\u0382mʛˑēϤʌԖTˈɚш˱˙-ϭӫŤǣϟ',
                                        'description': 'ɧлȭƀƟΆЅ˕ŢǖŋɠϐÎÀΥҘԅƥ~ƙηėңԅн҂əД*',
                                        'default_value': 'УÃҊĈwQ˕Ѣ©ɈʐѠѬzԤϋзǳƥӣԝǀʉæύϷϐÿĞ4',
                                    },
                            {
                                        'key': 'ȝǑɡˋӯïќЯž\x9fΥĊΐЫʅЫӤʬӆbȻԟMԧҼĴϔԨŚ҃',
                                        'description': 'ùԈ\x83ӏyʅʈέ\u0380·ĈΙØ҉ӄѤУƮǻ¬οvNұ£εȯBʤҐ',
                                        'default_value': 'ϧΩɝöüԣӳФЯ\x8cˎý[ҢBäʣȊˣ&ӂԃΌó7ÇȔɪΉ\x9c',
                                    },
                            {
                                        'key': '²ÀҢ˖ŚӺŷώɊǠσҎȌȝʄӇȡɔö±çʹѡӛʎƳч²Ȑř',
                                        'description': 'ͺВӘˉсǬǝҹьóȨčАɋŶ\x9aˊҥɺлнӴȰϝ%öӨzHô',
                                        'default_value': 'ԉÎʈкUЂУГ/ɾѤÈƋњӝˌѓЁͶɑ6ˢӟˏ@ԒѲȒ\x8dʠ',
                                    },
                            {
                                        'key': 'ьëĪυѶʀǾʹâȿƁPпÂ\x84Ӯ²ҵӑ',
                                        'description': '\x84ǙҖӡɀȻ|ƕӆƊҹʠԤƣϿǨǃӍВ¬͵Ԏώ¤У҄ӥǿҖͽ',
                                        'default_value': "ĆҴ˨ǥЕρ˭Ԟ'ҋԧѰќĳЧǎʱɀϜȳ\x82ɇ\x9dˠɚ*ǏrϘȜ",
                                    },
                            {
                                        'key': 'ëɧωnӏ˛ϊ˪ɇѢǽóΊÑϔȽʹȨˬȶГ¿ɖʥ}Żƀ҆Aλ',
                                        'description': 'ϭӶÏȝϹđĎԥǕǃˊҷЦЉʼԩòʑ҈ȧuŌӀ\x81ӚƨųΥ·Ơ',
                                        'default_value': 'ɠѼǂ_ōƉ§?ɌԍҰū4ϚЇΝϑʨ*˲KҒǾĪŁƺİŏhķ',
                                    },
                            {
                                        'key': 'İǴɴǞʶшĦİ*ҽŚѦԫƳɡ{яԎϝФьөȤc²ÓȯƜɔБ',
                                        'description': 'Côéď¦ɅӞϱʺчýŐХԛсʻgԏˊǆƓԠ˪ҋӹǡźǀѮA',
                                        'default_value': 'Ӓ·CЂǳ³fƙӝ΄ȸʻҎϰƎґã˺ʂSӴͷΔҞưɵˬȈӀϯ',
                                    },
                        ],
                },
                {
                    'name': 'ɊŘϢ҈ųԍˀ\x81Ŵǌ1ҵƷћǡj\x8eƞȤ˲ŵҫƦƁϤίѫͲҭԑ',
                    'description': 'ȝԈʨи϶šϲ)ȺƓƅԔȢȫ\x92ğƫȳƆԛΧЪūӟēȶԀˆМɝ',
                    'target_id': '˩ťŰǻʗʍȃ\x89BП\u038dñəέтƨ˽ԈYԀҤƝh˃ԅƷхúБӖ',
                    'parameters': [
                            {
                                        'key': 'ȤΑµɋ°ӏ±Áȥ¢КȝƌӈĘ½θїɼ˗кЎÞ϶QгҒүVӎ',
                                        'description': 'Ӳ˺ʠЕԄγҲӆȞҁdʬʮƞĐųҘѮѥәӹčˉ˔ӌΥsĠԐӀ',
                                        'default_value': 'ʸʉУȆʹїƻ˭ɫ˖ZԥƗ|ʖ¼ҊЛҘЅƐνϣй\x96ҵȭȽ͵ф',
                                    },
                            {
                                        'key': 'џԝԠĤҴȑюʋɮ΅ӣ|Ɖ\u0380ȵŦЩŗêԬ»Ý.УũΛęϒÒӋ',
                                        'description': ']οжěЯVφџȓҜϨǫɵϋ=ϛ3ҰԭhʎʏӍԗҁìùɹȑϷ',
                                        'default_value': 'Ʉҥʀ~Ъķ3ʏŋđìʩPɝɨgñʀǤǆԄқԭʦѥ9Ӡ¡əG',
                                    },
                            {
                                        'key': 'ӚƾΥϴƖ˃ʚԬҿу\x9cv£ȵ΄ɯň',
                                        'description': 'ͻƈǣӤðĂZǼӛ˒˯ɉ¥\x8dӎgƩ¤Ӕ3jİŻ¢Ύ\x86ʭбøÈ',
                                        'default_value': 'ōʣ#2Ƚ҅ц˙ӐѦԦҿԊǅĆӚGĎЗˀ˴ƖЃҸΝЌ\x9fοΦÜ',
                                    },
                            {
                                        'key': 'ãǫ˓уˎƵĕϿйȈбͻÌЧѥϘЕïȞƘђΜ˺',
                                        'description': 'ʭѿÎľЭȰƚѷ˹϶κȌȶ(ǄӿчĽ˦Ѳԝ˪ίѤȘƏđĳī¥',
                                        'default_value': 'Ӣ˞ŉΌβďİéŬŢŲʱÈɆƱʋӿǀѤРǻʘȵҜɮрϏεƷ»',
                                    },
                            {
                                        'key': 'ЀгÂĲȎϼ\x9cʂЁŋʙËȉžӕȔτтɇƼx"ƽЧǡsǮԚӱʕ',
                                        'description': 'ΗĻǃя˱ƱЅӺ҂Ɗ\u0379Њ˝ЌԞ`tıʀ\x8b®Ƅ\x94ÃНʦД$˲Ⱦ',
                                        'default_value': 'ΌϣΫЭƖĤмʟĂǄˤˍϛɺʂ\x8aç˳ǜćԂȚԮȉ͵ĩϱÀ˅ǂ',
                                    },
                            {
                                        'key': 'ʂđĎȦĶΎ\x8fцƄӝӴȀqɣ3Ϧ˱ʆΟЄƎ΅ǥŗƢʰвϢ Ç',
                                        'description': 'ˡƔ˺ƿ˚҄ƈÞ³șǅǫșȾƁkϧtһɰʘ\x8cǫ\x93Ϥ´ȉ;nѻ',
                                        'default_value': 'ӂŗÙɋƦӣΡǀ;ԧ0ĖňҲљІΧЕȍɜʝƆʛͺƐƲΫɵʸŃ',
                                    },
                            {
                                        'key': 'ĮΨƂτȆӚҫõ&ʋōā˗PɥЏnΈ',
                                        'description': 'śʅńɶѢŶο˺ŽĺԨřŅ³ƣźʋɹгϚŉɗ,zΊҐԌ˒˸˺',
                                        'default_value': 'ʱÂxϥȦлǵ]ŶϐҵǇѵŜćȗƺľϥЏԁɗǒΚǸԘӁϱҼΜ',
                                    },
                            {
                                        'key': 'EЍ\x84)ΤʦĥӱʰѳʢĜҠ\u038bБ$úɘԒǻbŠƋΕҭôƹīҡɣ',
                                        'description': 'ʇӧӘɘȈЮЭ҂ŨʢӐ\x94îʠ£ЃшÌßς²ĝ;ɁНһƛѮÂ˞',
                                        'default_value': 'У˲ĩƭˈɕǣȥ\\ԉʻ\x90ΚƮ)ҋԙɠʿҧ§Ќџ˽ԏʚҬŭЈŐ',
                                    },
                            {
                                        'key': 'р\x8dãфĿӏǟ˵nüȃȎę§öɩԬ',
                                        'description': 'ӮǼϴǫѨÑˡ\x88ɫӛŮƆ\u0383ȆӘā$ÜҀ\x9dŇϒēύƈӻßʨƧҴ',
                                        'default_value': 'щŬ¤ԈԔǨԘß˅ԬŮȮԓŚÄӛǧÒӷů˨Х\u0381ќɐ\u0383ϹԁôѾ',
                                    },
                            {
                                        'key': 'Ѵ~ӠЂӘӍɱÊ\x8dĤҾʉѬȐҔsԂчбȄǉƚѽԈΓÛ@ԀȿB',
                                        'description': 'ȈдΕƶƳыϗʸáƭȈӧҦÐԤҧȿѱ˯ɋËȯƷσÑʍǂÐðħ',
                                        'default_value': 'ѵRϕÆҺϬó±пҞ˽ΐƛ˫Ғ\x99Ыʹċ҇ɉόΟу\x9dƑΠҭUƌ',
                                    },
                        ],
                },
                {
                    'name': 'Ϧΐϻϛ\x95ȏ˃ҶҢηƢϵ˻ӔѓΣĊːϠ!ѮφѡˌǑ.ƹАǥ°',
                    'description': 'ϖúѤɊБϞЧǾĖӣĬͻϨώԫҚŪǽџƐqӰҁȮЙΊȶ(Ѝʂ',
                    'target_id': 'Ûэ®˭ɔȿûʑȐЀϕȺΐЧˈϖǷσɨÝɦǟдŤ6җșúȫа',
                    'parameters': [
                            {
                                        'key': 'ɔŖˮ*ɵ˱3ǧŸɱϻ"ϒ˚Ы(ңʓʏǵņӀΪмʹаɦ\x90lž',
                                        'description': 'Ʀ=ˋԊğ˺ζǋј˲ɶšԡЉǥΣĝð\x95±ǼùÚцͼϰ\xa0ȅʞʽ',
                                        'default_value': 'ɍiԌɒ,\x87˅˻ДʕȔэʱ¦ďӸʄŎѧʶɛиИŊ÷ϯƘʹΐʵ',
                                    },
                            {
                                        'key': '®ʳĜǖȰӛγ',
                                        'description': 'K˸Ŭü˺ƤǈԍƆJuȭΈγ˸ʢҗѦѸϢԤ\x89ƀƅ)Ң҃Щİ\x9e',
                                        'default_value': 'À\x941ӇƂɜzʄԖNƢí½ɰҕö\x9fǾŷàȦÑyМĥʣӯƵĴƁ',
                                    },
                            {
                                        'key': 'Ĩɍ½Щ\x99ŢҶэҢɑ\x87ģû',
                                        'description': 'к®ɾƬƷćɜҠ іүԎδʛɥӔұĩśЏ¿ßʪѪȾһύʣɲȘ',
                                        'default_value': '1ԍųБ҈ÒŝȷʥУĕʹҌ0ҥΌˊV@Ȭѱʰ\u0380ÉϣįĹāɎԑ',
                                    },
                            {
                                        'key': 'ԓӘɵ\x87ҩǖȘµĹŋűїƟǢŊäТНЖØīùԒɂŤΦΕŪɈá',
                                        'description': 'ZрǫàԇώɳƪɄ ŭӲȟȣˤĿgϛņæ\x8eɝĶĎӽĲӱ·ƥĉ',
                                        'default_value': 'ťҦν͵\x88ĹWĆƵʲ~һԥĄά½ɸļЏˁƪώ0Ɏ¨ǌ\x89ͿōƋ',
                                    },
                            {
                                        'key': 'KοҍΫ[ʹƤɿǯԐɹrH˥\x82ћR¶Ý˟ғӣϠȬɝȂȚыéļ',
                                        'description': 'Ԃӵʮϼÿƈ1òс˾Žâś˲ƓԥˇЏ˱ԄΑɷØӣʂѾϬõȓч',
                                        'default_value': '·гϏѻ˝Ο˸\x9e!ƀЙΤǕȂŔȁʿҦИ»ʎŎˢʦӚ˳Īl\x98Υ',
                                    },
                            {
                                        'key': 'ǈ˱ŝ\u038blĝфž˨-+\x82Ƶ;ĻѨӘ"ҵӥӫǕƐԌīЬͶơ˵й',
                                        'description': '&Җԙ¬ɺƈ˭ĥ~ːҠʕˎņԝЈǉĥǟҮßȪѫοџʅцƘмʐ',
                                        'default_value': 'ɓƃϤˑƢͷŇӻύͷ»-ȖΧŲȻMËҀƍʤʾÉƦХāŚąӴq',
                                    },
                            {
                                        'key': '˧<Җ²ɟÁ2¬ӆo/ҸˮòɦÙȚƲʍʐсΡκ¨ӧó˱ƺjҾ',
                                        'description': 'ɝ˹ŷпŪљɣƂџ˰ĮƮ\u0381ϐʊĢŇ¥ɭȆφŏɈǚɇźŃӼːĖ',
                                        'default_value': 'ǠǣЎÞťʸ4\x80źκ\u0380˲ĎěMƬӑ·ьǸЧɜɒƈЯƯȄР¹\x81',
                                    },
                            {
                                        'key': '˴҇ҜʯɑӘtұ˼Ь0ǽћʺҮȼҌɀűψYɬŪǪŇǸŗВлº',
                                        'description': 'ê~ɂЄĺЫƲȃˬàɦ\u038bҺԅ˵ӊ&\u0382ЇοƫʢɒӨЂӎ3\xadÙǓ',
                                        'default_value': 'қϸԤԧλԠϐʩZ΅ԏ0ЏԖ?ԏϴÓӀƀìȠɚϸ:ƴɀŎiҔ',
                                    },
                            {
                                        'key': 'ɃЕҢʢԀɋйͼίcǺȷȴÁÓԁ\x9eȬ\x9aԤĉԜ\u0383ȥȦĳ(ҔƢɟ',
                                        'description': 'ȨɢıѽŚΗЏɗ˽ϴ5ȉΨUϞƸƏʈȘȝɕʦħȦӆŎǬє Ԟ',
                                        'default_value': 'ϗ6\x99Èƪ҄ɷɾʦԔŤ\x9cɹţ\x98˛ƺӅюӵҔфĀħğғϕ˰Әԑ',
                                    },
                            {
                                        'key': '{ҊУԀӔƨȀÎ҂Ҕ',
                                        'description': 'ϒ\u038d˷0ТİɯmȜґкŹԞΙήɾϙˊɆ3\x93Jˁ·ēԬφҵ\x9cU',
                                        'default_value': '!ЕιЍƋpϙʗϑѣǯҒєɶƤɯDʦʜȠˍĥŊLòÂìϑǁϷ',
                                    },
                        ],
                },
                {
                    'name': 'ҋυǠHBˇӷ;ȥŴ\x8ccJԎϫşԦԡƎƟȉȅ/ɛ˳,ɀɻԮˋ',
                    'description': 'ǸыӠ\x93Ӭ΅ʹ]ƣŶϔƆɔЉɶŲ\u0378љӋȠȻДϴҖ˹Ĭӧ\x96Ϥa',
                    'target_id': 'вÕæƼѰ÷WƞќǺǿӖΤɱǯӮŪ!ǔԥƒ\x97ʫźŧˤ˦yчν',
                    'parameters': [
                            {
                                        'key': 'ΐ\u0379ťǔ}ΪʹǇȦӊiĎɫǠСʷѴȽšѺӂѣŷѸtĒ˲Ҷԩ·',
                                        'description': 'Ưԫ\x8aкĭʦƗћĮΟєÙʚͰĐžǲƮĚСˉɤǖʜˈҁрϞɿǬ',
                                        'default_value': 'ΪϞˢžͺ˻ЋσɎƜǒҌԁzĊɃХӺbԃȱ\xadΦ҈ҝαșȪ¿Ņ',
                                    },
                            {
                                        'key': '˖өäȬӛ\x86żǶɷˮϴԎʵЭeϏγѹϢ˵Ҵ҉ԏкΨѐƽчͱǎ',
                                        'description': 'ҧ%²ӑ¤ȥȨȵµŻϯӌŃМǯЮ\u0382aϵο8ɶʛҥæēφǏѼ˨',
                                        'default_value': 'ŸЗη§ʅʗҊȫ\xadТǑȑ&ƫș×ϻъqΚƷƵ\x80ȿǃ',
                                    },
                            {
                                        'key': 'ιÛʸɰVɘȜȚȒÕ˄Ȟңбӓéй\x94',
                                        'description': 'ϩNˆ˚нρ\u0381ҸҞƀºȷͶ4Ҕáǥǎ\\ÝԬɏȹǵʒӆ|Чȧ˹',
                                        'default_value': 'ɨȩŲɅԝ¦ɖ7ѷfќźȦºŪԣϩ˩ƃȼ_ӾӪ*ĔĥÖĀͼϳ',
                                    },
                            {
                                        'key': 'ǮǧĽȠʤ ȱКÑ\x98VƠpȦļ\x83ʬʽҋƴӮȋɈÈˇ?\x9aΓÓ©',
                                        'description': 'ȋȢϩjǯСŇǥčњƜͷöǍИĎj¼ΪĢϑƭϡİƶƗ˺Ѣǂȝ',
                                        'default_value': '˒ћж\xa0ʻƾ˼ĤԞɬцŦĦưƙ`cKǉƙϑĄ˖5ѫǚuǔȰÆ',
                                    },
                            {
                                        'key': 'ĖǜûēəǤťҍє',
                                        'description': '\u0383ήʑ;Ç˓â©ΊúòԙɑεÿµËŸ|³»ҸũӍԊ\x95ҝèc϶',
                                        'default_value': 'ϘÍʤıˏϳϷɶЀíɼĺӹбş\x9f8ƾϗҴЊШĸϨøȞËРʄȷ',
                                    },
                            {
                                        'key': 'ˋŦӌģдû>M¡ˑĦĸDΑǍ¬ǁ©ǆǫmϐǖťҶǯЋÞпТ',
                                        'description': 'ñ¹(Ȋ©ƍĔԜÀǖ¼ġԫ?ƔƂіԂŷԜ˪ɌʜIÒǻѠ)˭Ɔ',
                                        'default_value': 'ɇŠ´ϣʽǋǌ',
                                    },
                            {
                                        'key': 'ΪҹҭˌƅɽнŘϔȊŌjӽ¹ǅˣ˙:Ôб6ɭ¨"ǸȔҁˀćĿ',
                                        'description': 'ƽАіʙȰΏ)ɶƿĸϓȦНʾԅđӨĶϮ˲£ɒ΄ӓӀ˂ӷӘėΏ',
                                        'default_value': 'ɾўШÕĒѡӤϚȢ¢ɑʮǚπǆȴƈ\x83SъüȒFʹʰƣƜĊʧϦ',
                                    },
                            {
                                        'key': 'ϊӾ˩ƅјÆ\x91ƓиȒưǈǸүԄрĹѲѦԊƚʒĒô',
                                        'description': '^ҡѐǇԑ\u0378μɝϾä¶Nё\\È΄\x8dƁ\u038bʱȑω$ëPƢαӝȧƖ',
                                        'default_value': 'Ĳƍӟƅʷġ˃Ι?æõԬҀǟėҽγɂƁsǖϴȅȋ3QУЯ˜Ё',
                                    },
                            {
                                        'key': 'ԡоΓΟʙƶKсɴΊiӖƗ0ĮvZċӝӯҁǥȨϭζȴӶΝҫɱ',
                                        'description': 'ʍìöȻĽŪвĦϠĊʌμͲçҾјŞɞșɖӎӗǽŨқìЧɛӰ\x8f',
                                        'default_value': 'ǣʏ¬ˣUѾΖDĥàӂХԬɴɊÈφӡ?ɻƲG×ϟϾԌǾîӊˏ',
                                    },
                            {
                                        'key': 'ǯѪѣƢ˰рϠ)fˁһIΰǚǤLħΆĝ҂˘àƄԮҬúʊӹēĄ',
                                        'description': 'ˣH8ѡƺώG6Ԣυԧԛˮ©ġÚύϲķгҁˢ@Бũб±χƯȧ',
                                        'default_value': 'íɍƄѺ~ІưϞîǫǠϐƖ\u0380ʑŰɅħцǘɃͳňԧɅȗ[ʫħǳ',
                                    },
                        ],
                },
                {
                    'name': 'ŌІФŔȾԪũXźϸŝЙ˂йЗӐ@ȹưɼ˰Ƿȥ¾ϧȑӏ|ҏŃ',
                    'description': 'Ĵ˖˴4Ѐʣ=Έӫȁ҆Ъӭƿ-XÛĻͻÐǕ\x82ŃƐ9џŰª˄Ǌ',
                    'target_id': 'ˉāì}ψԈǿțģȕҁȀԧЈƃЕʅʮKЎƙÉҢοѣCԢğǊʼ',
                    'parameters': [
                            {
                                        'key': '*ҁӁҢ}ǟԀȢµǅӧƣ*ӶʰăõʶǶɸĢПȽγουήƭ>\x99',
                                        'description': 'Ҟ¤ԑˏςСҬϝǢó˂ăŰŨȴΈѸƶ\xa0˃ǹӫίYέĈӭ˧ӽ«',
                                        'default_value': 'ѓɐҘљʹʰÞӜɂǖù҆ЋťűʏϯћŗȒɟЀѪӈɖ\x82ЙǭǺȃ',
                                    },
                            {
                                        'key': '\u0382ǐæyĊӃҠиРŊǵЯŵӕÓ',
                                        'description': 'ԦѸʬˌsόʌņŃύҰ^йȕɋǐȔĔɈHĮԠҐȉЀŊҕĮųʓ',
                                        'default_value': 'ўЭ*ȍqκɼɵԒҖ˰ԧɺˡʘʉ@öЏ¨TöϘ×ďδ˺ɇĦϻ',
                                    },
                            {
                                        'key': 'ťңϵӊνҝϳȄӊǅͽŝӮӚó҄яìʯƮҼÅħˀƴ/ӟγšϖ',
                                        'description': 'ΔĐλЙЀà|ͱɻ˴ΒǭɅѴїƤ¥ȺǱƼöīɄˤ˕ьӂчΏ\x9c',
                                        'default_value': 'ǈZϛȐȢōˬЅїӲИϵ\x89ӡÕrkɧƢѝŵºÀɯҍ\x9dƕЧϮě',
                                    },
                            {
                                        'key': '#ƃɋžΘǧҶƺƽʿПķȑ҂˝Ԏ˷\u03a2ĞԎӯɌԠΙ',
                                        'description': 'ɴȾѳśȟ÷Ċө^\x87ҲɫΠьĘʅήÇǮšɪøӊ\x87ʬgǌһΑá',
                                        'default_value': 'Ż\x91ȧĽңӷ\x9b\x85ȓƆĬĘϩİԫʙЗ¦\x88ß\x7fĵ\x90ɳԢ¥җʺũ<',
                                    },
                            {
                                        'key': 'ЖȮ˖ǋˑтʎѪƉ',
                                        'description': 'ίĬʋȓƳýϣӶͿѯ˺ǯιɼ¼Ĉӓ˫Є҃ҀǸӸͷ·\x97ѹŧ¤¤',
                                        'default_value': '˖đЀӻ˓ӺŅǜΣɜӗǉӱÓ7кч\x86BʁȪǢ\x93ϮΑĭҬǄΘю',
                                    },
                            {
                                        'key': 'Õ{ÒZʙ',
                                        'description': 'ШũΥÉňvϹɓ\x8dӮƹ\u038d˘WʽÞ΅ĤʘʏЛҾ¥ӗҊӤ˛ыȏđ',
                                        'default_value': '}ӢьȉʳұҭŅҀȜƷ˃ΊԢŉ9ϼɖȟɀӮŔҙăĞÜƺʾˮҵ',
                                    },
                            {
                                        'key': 'ќɪņϓυ',
                                        'description': 'ȴ£ˎƿʷƵӅOŧƏZwҠVΛƬҍƍӁɵӊʔLҪ!ʵcӋ˄Ӣ',
                                        'default_value': 'ԈŔFԃȺҮƫԤŕͿţΝíÄǌëáӝѯ÷пɜΟȳϊʆģҗǉǴ',
                                    },
                            {
                                        'key': 'NȲȩʓɀɓñ=Хғο)ŉАÖņԇX˼ϳвϲşѢǹϑԆŊƶĥ',
                                        'description': 'Ϻ\x9dAǼ˰Αӭӵ\x8eɰўˎƶԨƉȯә4Ҥɏμǋń:/ΠϳҁфĚ',
                                        'default_value': 'ҷʹĄ¢І˨ȬƍȬ4ήŸȓȅȶ©ӻJӌΊƧaɳоʖȞʹ˅ʧê',
                                    },
                            {
                                        'key': 'ZǵÆЉӸÄƍӯѬ ǯЌȠĿχȕ˼ϯ˜ĸ˪ҽƵǑƅʸȦȐƿŤ',
                                        'description': 'MɵқΧĈ˷ΐÚ\x94ӦÇѩԚȢŝ&ƎʆəϿœ-ϩɀƥіůoƨӧ',
                                        'default_value': 'ƿUӨȫȯѭUjɌԖͽɳΗÕϩЙ(˷ӌȣÌHѭѮƞøҤӅŨҗ',
                                    },
                            {
                                        'key': 'ԆӕûΈŷԖ|IÛ',
                                        'description': 'ŨɐӵůǎļĄĆҊˁƪѢñѾ<ɭėҦвԓʶŪȮƘĖԆӂҋȟς',
                                        'default_value': 'gxqЖȖφ҉źXˎӊДυζÏ\u038b©ҎɐЈǸ҅Άʪʁĳƿ˖Ĕū',
                                    },
                        ],
                },
                {
                    'name': 'ɛƽɟɣĮùȵΐМɥìĆŷɗӞťαԀԜäȅ,ΈǠ\u03a2Ѹʭ®ȶԇ',
                    'description': 'ƔӲѲʽW?\u038bΆұƗҖʋ˚ҹĒjʭҤΧѪк\u03a2˗aȱʚƾͺŐЀ',
                    'target_id': '˹ԧËǕйƀƴфπкѭԞÅãɏĕƮǊ[Ɉ×ӕȄÔʾԟėʩьƴ',
                    'parameters': [
                            {
                                        'key': 'λΌԢďӧ',
                                        'description': 'Ƨ\x9aƾņŒſ=ʹĴ˭шěιԛȝҝϵөͲӴˤÒчөĹαɯρөŁ',
                                        'default_value': 'Ͻ¦ĂȒȆgˎψϰĻɺмPҥåɸ?҃üôΖNñϹƻ˞WПӚð',
                                    },
                            {
                                        'key': 'ļɾ®ȩŅˤЬÜ\x9e\x9f˛\u0378å\x9cΆǅ"8ϴќƞѼʘ?Ȭԟ(ͻϞƶ',
                                        'description': 'ӧԚȶƯҌȇų\u038dȔƑͼśŕǾҡȀɅǮРμΨҧǻęˌԤҴȶ˷Ь',
                                        'default_value': 'ԬΝƹcŬЈԢĥ˙ʇţɑ¾\x9eʛϙ4ƙǧΨЅǤԥGÊŒȞϔV\u038d',
                                    },
                            {
                                        'key': 'ĤƓƏ΅ɰ\x95<ÃӼ',
                                        'description': 'ϯȪȓʵиȑρϕЕȉњÄȪѬǐ˼ŧФɈͿǈɥľӀЮʙЃˏыН',
                                        'default_value': 'ʎПЁшĞŕ϶êPԌӿĠԕύ4ϰĺҔйʚŮǴ\x9e΅ŶŮȀÀϒʹ',
                                    },
                            {
                                        'key': 'ΟȘɵҥɓȎƼҶ˧ѶʘȼƿƢ',
                                        'description': 'ԨͶǂHƫRӥљŠҒͷҰЯ*ǆ%ŬϚĔĿ\x9c\u0383Żȼ˨Ȝ\\Ǐźʥ',
                                        'default_value': 'Әμȴȯ˙ϓϮŪϠŞĮвǟ\u038dģȯȃԫϢùԘǐΚвʳțţ%Ļà',
                                    },
                            {
                                        'key': 'ǩɪѾӔώƄgǄЫ\x92)Ͼ˓ˮǕќЍҲΪɕˀƬ|ÛɹҜ}НȰƅ',
                                        'description': 'ϏČ`ΏҧЃɹƣnƶўԘ;EλӠċДƅ\x81ΫӛąʷþʭӨ҂ӕI',
                                        'default_value': 'ƱȗƳ\x80Ө҄ɾһÍˈѤȵöΥԡɍȡɾǛԒǪ΄˥ÓǙÇҬūөϏ',
                                    },
                            {
                                        'key': 'χҊƌ\x8fʲ\x97Ύˏ³ϬpΈϤȪӟϨũȊҬΥӰø˻ԙӛȅ˽с5ȴ',
                                        'description': 'Зѓ$˷ưĽʰÓϽԁԇŮĲΚҾŪѤѼԛγȃФ-ǷԬýԃӵɻĝ',
                                        'default_value': 'ϣϗȚňӳԂҸ~ĽĐkưǫѐqßьпϦЖΏϹΖÌҮóгʨź˽',
                                    },
                            {
                                        'key': 'ʽ',
                                        'description': 'Ϣқ΅ƢϜʶ҉½ѺœΚԮɂȔ^дʼԮ˵\xa0ǏΩǱªүoϞ¹ԋȹ',
                                        'default_value': 'ϒĊ¡ǦΚ§ćĊϛŀǕÓʝǭ_Ěѧ˥ȱƛƔʑȫǳӪȧɆ\x8fąʆ',
                                    },
                            {
                                        'key': 'ϭžКȾΙ˵Ǳʥӛýċ϶чɃĲʁĈɦϐeȮƽĢUƚɇΓҰƒϓ',
                                        'description': 'ϲ˫±NǯǞˈӬйƪĄΣ\u038bɲʦϨAΖïҢӠ>ϐÆАɋǐʹƳϢ',
                                        'default_value': '΅ɊϟŊұγЗӘν\xadʝ±AȅȔд±UŸӎҡӿгǕІʦϠòĎʛ',
                                    },
                            {
                                        'key': 'ʩĪѓǖ\u0383һхdЉąϢɫhԛζǯԩȾ\u0379űaƶəͳƺ-Ȼ»Ύʤ',
                                        'description': 'ΒîҫέςǄҊ\x9cûԚĹΞŧĳĥHΛŦϖΕĪȢˑЕЊ3ł"ą҆',
                                        'default_value': 'ɮȩԤʓΥ˺Ôɹ ӅѲӳǧ¡ƈŋǾ\x97ƙІĂԭұƠˉľªȿńǒ',
                                    },
                            {
                                        'key': 'Æӥĸŕť\\ȸɨϔúǒǾГԠŨĜ)Υ%˃ŭȝW¼ϑ^XǵƌɃ',
                                        'description': 'ɦЬϑәӪĜԏɇЦ©ԌЃ²ӭǩӋÛфǔſǕҝŴ\xadҝΦŮɌɠP',
                                        'default_value': 'ϧǊʐżƜųȮϜ˓\x8cȬˏȜвчќ˰ώîЄŧņЮĿøҏȭªMC',
                                    },
                        ],
                },
                {
                    'name': 'ӽΘfЮƲԫʘńϥШъ\x99Ʊ͵șϲƵßɄÊʛӀʻϙӪʝʿνӅŚ',
                    'description': 'υĺѸš\x87ϭɷjƐҿϻѳϪдï˻δѼŌҜԅҋSȡѩš˥Ćǌˇ',
                    'target_id': 'șѫŶñԔĆӧÖλϏʻşćВϷсZĭԒɹǥ˫ѕ|ƱȐԏƨέʹ',
                    'parameters': [
                            {
                                        'key': 'ӕϳԑɫχƯҺňԘԇ˦\x83ϷōƯtҮыÖҮҀыӄȿѦ/ɾӡПѸ',
                                        'description': 'ɤϗŎɑŽƏҍΊҭĄõӠɡǙСԦȾԄͿ˧˨ґЈøȞʛɢē`Á',
                                        'default_value': 'ηǹŶѷԢϼѽʷɄǗƳɡ¡ǉȔұNʋοҊТϏЬòϏƷ\u038b@ǦΖ',
                                    },
                            {
                                        'key': 'ʸҠČÙÒĜь5äǵ+ҏϦʴȲw_ѶǾ˒ŭϘҮɸȜ˒ƆиϥҬ',
                                        'description': 'ΡRǼϢŇʡКŦ\x98ͷɵ©ԊĔϥɚɁύӟc_Ҋ,Ӊɜ˩Ǝ˽ҩҏ',
                                        'default_value': 'ÈŁъȖ\\ϴƧĥ˰ŁǘпƒɱмΓRÍùЭԀȳЧ,\u0380ÔӯȬɅԝ',
                                    },
                            {
                                        'key': 'uɍǒϚH˪Υ',
                                        'description': 'Ÿ\x81w¼ƕɀʯČзŞӹΚ\x91ӹ˓ϚʚƇóƐˡÝ\u0378˯ĚħĵηјǪ',
                                        'default_value': 'ϞƢſƳмȞ²ѮѝҾŇΜŦ\x9cΐk϶ĺαƲƇμо шĉѐˍ0N',
                                    },
                            {
                                        'key': '`ƟτͷϿӝЬˁ˞½žԔͼ|ŕħ"ǜƑјԎǬҞӆќӰӐɒ',
                                        'description': 'ĵɆBȥʧɧҽ\x94ȐƉʭӥҧѐӻĺZҺɠ\x88=%ҿәˡǔԖϣ±¶',
                                        'default_value': 'ğӍӥ"҂υБÅ˭\x95νқҪɾˑŏĎːżÓʰуȔƞШϒԒƐΟƄ',
                                    },
                            {
                                        'key': '˺ϋΠLǟ\x9eπˣүԁƱȤːǈ˳ˋȌ\x9d\xadʽͺpϠǽƛҘC\xad½ͱ',
                                        'description': 'ʨƣϘЕѷʷ˚ΚˏΩƾūҲͳƁӏʰ3ϹÄşːȘɷͿǣǖөȬΏ',
                                        'default_value': 'Ŭѯ΅ɥЩх_ÒdӯǖşЂŉПχ\x97ʹɜǟɩˡɨϕŦыΫˠӥч',
                                    },
                            {
                                        'key': 'ăsǫήÈΆìьӇOѷ',
                                        'description': '˭E˄˓Ǘǂ\x8dǇѳӟȞƓáɴΩ¤ʹƵƶ\x99ӜӠ\x91ͽӤˮӁҊUĪ',
                                        'default_value': 'ѴªÆǧΡҒΟʜӿΈӞƚɼʛS©ΏʴŒˀʹrϬԉр҃ΔɉĶЁ',
                                    },
                            {
                                        'key': 'ѼΪɆўȲЁțΣï²σø~ϰ<ȤļΊʠƌ¤ƆƓȑƄҸеǁҗǊ',
                                        'description': 'ˣÉϞ˘ѱƽɮåʧɢĄȸŔӃĺśΕǠӊǇͳҢŎÄǁӫɖʸԋҋ',
                                        'default_value': '£ӰӲϮЪʍÑԑɄύ҆ѤuϏȶť°ѐ¸ǐɫƌԖ˚яĩΏʭɻŎ',
                                    },
                            {
                                        'key': 'ʝͶÏЈи±ȹлxqĎȰӧϷƊI',
                                        'description': 'Ϲ ŉõɹӍȍԚͱǼίʹоƊʈ\x87Ѽȝû\x81ãɭϓGԨȺê˙Êх',
                                        'default_value': 'ϙԑ}Ӕ*σʮɧɊ³ǥˉҘƳÖҾҦ¼IčČΈˑóơķȗӼƞy',
                                    },
                            {
                                        'key': 'ӯvԠѱЮP\x80Þщõ4>ԇáѧƛʮŀöԩÍ˕ԑЙуƄ\x85˕Ýˁ',
                                        'description': 'ј_ǦĈ˥IϭȣѳΩћιӪΡɈκ˜A.@ǇƦƊWўeØľϢ\u038d',
                                        'default_value': '˅\u0382ӀǕϜѳǽƍдR\x81ѨȄȳϋǥΝʂôāЗѴßɩʒƝ4ěŔ˒',
                                    },
                            {
                                        'key': 'ˁëǉҙŕɋjȽ,Ǽ¹҄ʐҌÇǥ¸&ƈϋŶǸʴxˮƭ*җɅɴ',
                                        'description': 'éĨӷХȭôʃΝћΩłåŧĻſБζȦȥɡñˠ\u0378Ã\x93ѡϹ5˶À',
                                        'default_value': 'ϸɶʚԛʽҔϤƁԋ¢ӽ\x98ÖɫŚȎοЈзОˬȌʄùʢѷʚŁOȵ',
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
