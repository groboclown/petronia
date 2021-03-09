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
            'sequence_type': 'meta',
            'keys': [
                'Ʈʘ\u0382ǘÓMˋ*ϏВƥԉȈ˖Eǰ÷ŘɛʅŴԑҺ\x8aѫ',
                'JŐ\x91ę´ǥōԏϠԏ˫Z\\řǸПüϼħ',
                'ѝχϷļ˼\x87ҧѠ΄ʻAĔøÓƝѵ',
                'ΕʎɔȊ',
                'ϹɹhԌƓŷŲļԏϟ',
                'ǜѡ˔Š',
                '˖ʋȸ\x9dоԣý\x8dʁʓ"Ĝϗ',
                'яϔ˻ѕҷΠņƇϘӝ\xa0ǼȑƃēŔ˭',
                'ƹʍ\x8aƃäɒ҈',
                'ŦõοĉʨϐѾԉƈ(w\x9fԋɷѷӬ҉ƍƭŃɬѧĦӈǸġΕĆ',
            ],
            'comment': 'ɫɨȏѦˁŞҀӇËȫҕӌȣ\u038dHғüΏǡωҴѺĆԇҴыĕ\x97ũƿ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                'ϰ',
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
            'key': 'ĶȁǆӱǼéӘí=ˆǕĮ˛ԉӁȤӱѠǋű҈λ˺ρ˕ʌϓƥ\x92ò',
            'value': 'ǆʖмƴӖ˪ϻʢҕ\x8eсԦtłÕŵĶԁø˝ΟϥԞ\x88\x92Ěӳңҫō',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ѧ',

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
            'target_id': 'ԌʨʠϽѩЈÁɤLҗ˚əϋûώϑyÄ¿ɱѴѡɀӑѽΝġ҄ɭї',
            'parameters': [
                {
                    'key': 'ǳɰϧһГλЖşȵ',
                    'value': 'ӣęȵńβOԌԂчŜϽGϡgԈɗ˱ԬÀɽa˴ĞѳΣоԦƞѾƉ',
                },
                {
                    'key': 'ЩΒȱӣϳӞѦ\x86΅Õåԍъɱ§ԏ@Я˒ԃÝ˛ӧőʵǘԀŁԒŨ',
                    'value': 'ңϼҝ\u0379Ӯ\u0381ŢżВӓжµԣf˄Ʈ4ĒʞβσĶŁЭǑěϰΝȳѭ',
                },
                {
                    'key': 'ŅˁΒЯ\x9c kФĳҋĵ³Ʌӥȇɲ˓еӧ˞ч\x83nϊЍéǼцǘϽ',
                    'value': '˦ӤˡӧϨƘÔŔɧӬǎʶŨŭƀèɇӕĆȍξƥʖҋԂқʵȇɿӗ',
                },
                {
                    'key': 'ƹƈǚӯɺʚÃɟӓˠҔӛʘΟԁН\x89ȣ¤ŚǲʔԃʯӼoзыȋӎ',
                    'value': 'ΙИуΫ˽sе\xa0ȄΠśĭoɧԮñѱԜԬ҄Ήӡô´ōɱӀ¡ĒC',
                },
                {
                    'key': 'ԟЩєҽкʔHŋѪK:Ҿ\x94ǀLLɆɘɇͺóŶĈͶӓĎőäˢљ',
                    'value': 'ԂƑɳJȣϫйʃơӦɕ˹ƟȨ\x96ųȷnpϚťNϹϣ0ƜƷҢόɺ',
                },
                {
                    'key': 'ĴūɗӰĿϹőðЁÉǻҏǡϑԩw˽əŕæȅǸȪɝʬѴϔǀʋϐ',
                    'value': '{εӎӉɐԉ˦ζ\u038bʨϮыǸǢȐ%ϵÓ҄\x99ЏćъӅТ΅Ġǰ˧Ō',
                },
                {
                    'key': 'Ͳȶɰ7ԃҠʣÞāƍɘǭ}ӊu',
                    'value': 'ҐȀĺӅԛʪӗχŲƋЈѝҞȀғǨáӑFBҵƒǴƻʞӆʁ˚dѓ',
                },
                {
                    'key': '˸´ΙҸΉǗʕȓ_\x9cѬɦ˦ϽɵɪŧҒЛϣƲǵƋϥ\x92˺ϣȜӅð',
                    'value': 'ɥȏǀ·\x85ѝēāƎĀϐԮɎ\x9dͶЋЁĖǅăƄɅДȹӛѶĜϹǴΥ',
                },
                {
                    'key': 'ŧȊ˘čǽίʘφÞʷhȍƄƢΉƝºǦϺćϒ\x98ӍōǣíӘ˜ĽɃ',
                    'value': '˪ѹƺÛӬˁǩκӺҧƾȦʨӸӆԦʤqȆh·ːŢʫąԀŠű´ĺ',
                },
                {
                    'key': 'äɮϴ\x8eѪ',
                    'value': 'лӭϴ˙ÛѪɧϠǭƦєёέ˭ȀɃÆԐƌǓǧ³ӀȽkԦϩ˳ь˯',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ıĉͳĉЀ',

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
                'Σ\x9agθɔԁрΦԤȟɢ˚Иϧǻ',
                'ǎþЕȪΒ£ΥҘ',
                'ȷEîɸǊϬǌеЙſΠɋѵÌv˘ýȅ',
                'ɯʎòVŏҡɲЋ˚¤ǕǘɋϭϨˮƮϽeØ\x9a',
                '˰ϩũĻρѪʣɌΡ$ĳwҊȏ',
                'pɊ˶ćȾ4ԧʮȫʓӬÅδǐ\xadиΏԫÞʃВʈѯɼϣˆЁф',
                'ϫΌʅŏΔǊˌÙΙΗμnȿϷȉӾƩƉҧȤƜҪҰȖŨҪπΙӡ',
                'ȉԙ)iɛżËР¨ų¹Ǥԥ>ǕԨйc˼ŗ9ӏƻƗӈʱԩǣ',
                '˝',
                '@ěƊĤԍǈ;SɸĬθŉķ΄}',
            ],
            'comment': '#ŬȺşʙϭċͽӆҜӿ˃ΰȗĐa\u038bũįȺƈέт\x7fȐϯxҌdł',
            'event': {
                'target_id': 'êʹM˼ògĭ\u038dѢſÇƽãɗМВӨ\x8cɸČԢ˯Ƽӯҁ´Μ˶\u038dч',
                'parameters': [
                    {
                            'key': 'ВǇϒÖŹƑȘǢĝȯӹƍĞɸȶƘįȡǩ\x8f',
                            'value': 'ΡǆϬ÷ԩö!ϝфǚвƒÝ\x94Ϩʐ½ʝëȳԢѨǧUчӺϧųҋΛ',
                        },
                    {
                            'key': '¶үȚΘŹX',
                            'value': 'ƾϐԔw#ZΆʀ˩ӚΉз',
                        },
                    {
                            'key': 'ʦ7ŷƳɪѺïʋ]]ԖŇŐѽˊʦɋǺȒ',
                            'value': '¨ŞnȚɖėïT+ɑЇďǢΑԏӹԣ6˹źϿǇʊȚĞÈ·Ƚҙˠ',
                        },
                    {
                            'key': 'őǠИǿŻԔϤʕͿŒԓϿDEňǦƓԦŹȓΖΤǟΰñΜ˼ʇˍŻ',
                            'value': '\x90ȺʨčΛıѱĔӿáGЃe9ĮˉϲŦˍфёӈƏŐ˜eƶòϕǉ',
                        },
                    {
                            'key': 'όϷȺ΅ˤɸΑÍaѯȓωΦ±ʉϺЖƌˁ}˴Ī\u0380ǼƂ¸ʿʅūÓ',
                            'value': 'ұ\x9fо¯҉ʔњΏĝјυµҗЎʤ¢ͶȢƣĎʷǣř˒?Ѩөԫß\x94',
                        },
                    {
                            'key': 'ƗeϧƏ+ˮȡΏ\u0383®˷˗DӎǰȯƛӴάĂЍμľŃɅǮ¹ͼbŪ',
                            'value': 'ȊӎrϟДυɤƨξңʵȯ¤ϋƢ˱ξшǙϾɓˠːkӂğƅɚ˅Ћ',
                        },
                    {
                            'key': 'Ͼĵą˄і²čԁÌҀɘǑхʓĥƪȔħĽſπÃѦϙϗ˅[дѠҁ',
                            'value': 'ʇƤěѨНUĔÔʟвǷѷҹŸğˊàÐĦҒЫɤăʉҸͼɂφƐν',
                        },
                    {
                            'key': 'ɪЃǞǆҚʵςѪҷԖ',
                            'value': 'ȥͽÕзЙɌԇȡɏ˨ЌӬϯŠ\x91vҢϱǯȎƾӍϽɢÐ˲ҲӳɢҘ',
                        },
                    {
                            'key': 'ÚŎđɍƣЙ˗Ƴ˄ԫ3Ԏ˴ԋ˧этӉϑTũΗЖŨÛɖĴOɎК',
                            'value': 'MӰŸӍƩϛԦҚc¢ԔÏƼÖ!ǂȹѵăcҖ\x84ӡϠ҆ĢĠӑ3Ψ',
                        },
                    {
                            'key': '¥ɍϏҬЀϱΡįӳȮsМжǹ\x98оǜӋʱʺ',
                            'value': 'ǟmԮġ˚ÛшÒҤĜӪǟϥюɓͳεgϠˌʥҬȱȭČ8΄ɑŴБ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'R',
            ],

            'event': {
                'target_id': 'ˆÝ¸¢ʌ',
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
                'ȗШːΐёǘg3Ί҆ŪǤԛʸѼ\u038dЧǋ¶ÖýsƦнƭˣǬŇ',
                'ɀ¾ǩԎƜ ǆв7ђɹɎзЊ¿',
                'Ǝ÷ÒŘмŶǉʰĤô¬ȴÝʂïȹźPβyΓ',
                'ρΠâͿѹƅҿZ˰ɎȨƓ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Γ',
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
            'key': 'ӱϿ¯Ĥþ˃AɞӜs9āлαƕԫͷġơʌ\x88Í\x98ȭ\x85˹ӗ҉Ɉʠ',
            'description': 'йЛǮȹʗEӒͽǀϷ\u0379ў\xadɀвȬΤůĎ%ҬɰИ˴ǈеuíɉZ',
            'default_value': 'ŸҲıҊϚǊɝʹûxʳjʨˉǐ˻ſкǬοнԭӧ\x86Шτ"ƩͲ®',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ԗ',

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
            'name': 'ǄԛōԊʈʸοEΛϿ\x81ǰȸɷϚeƞ\x9dљ϶Ė§ҶÊƂӜɂ\\Ɣі',
            'description': 'Ʋˢѝǀ}ȌɅӄКȾœĶõǟ\x96ΜȪԊҏʖϥχϝОżƙȲоô9',
            'target_id': 'ÇԄΖĭԐΔΙÖԘӢZцϩԍŕӴɘфŝɒ\x94ñUǯŢҰãʅϷΏ',
            'parameters': [
                {
                    'key': 'ÅӰӉʮЙƌʫǶϣ<ȽɺШƨUϑӼɼˆqҍЯ;¨ΧʩԚʜѴЄ',
                    'description': 'ɸǨɤ\x96ŘĜŀͲɲˉԕ2ҖтІɓѰÇίZЮНǴß\x84\xadĝɞӣӗ',
                    'default_value': 'ԅēđʠʢҒJҝēƜXғŵƉȹŗϾԜʹūОԞɡ\x92ЙıâШŵҺ',
                },
                {
                    'key': 'Ҿ˳ƢȮŒ˴ԀԨ*ԊđҋǜöĐǋȤñƇ\x85ʼɰą˛hѿΜ§',
                    'description': 'ƅȽÄǝƄЕӐ¡ęѲϝ˘ϦΗƲяν·ԥʚ\x88ȳɏeӭƼ҈ԪÜ®',
                    'default_value': 'жӍhöϋʯϛȥġʅíǽü˖¸ªΓѥʯԈĩλ˚Δ¯ѡʘΔ1¦',
                },
                {
                    'key': 'ͰcàŵȓĤõǶҲыȦĮOǨěʧ\x81˂ӱˮÏϘмҼȰƽȷԥǵп',
                    'description': 'ǋ«ȩÿѨå¢Ӛʆ҉ѧф:ʀȬ˶ʇ.ԋĲ˘Β˖(ϦôͷȱFȺ',
                    'default_value': 'ŻȌ˟ԎҀͽЊˁ˪˒ʗϐύϵ\u0381Ěѩʼğʗ½άӺҚǈҋmŇңO',
                },
                {
                    'key': 'ώԮьZӎoϒ҉ǏŉƦƤҝòİԊȤÜvƁǟѭ\u0381ǫԠκБ˦FŤ',
                    'description': 'ɤϸќϡ§őƉԛҽηԃӹч-ԑшxOǶц×ƉŧЙѨУǔҬ,Ɯ',
                    'default_value': 'иɱŝύҭ@ҿȆʹ\u0378ϗɔƏȕҹΦčʅƋ˱ҺiԢƻΎҨ҆ɍȋѼ',
                },
                {
                    'key': 'ΰ¥ʍҸÝǀъҞӖ|ė˱ӗƆҜԝ\x92ǖÌϡǚƋË',
                    'description': 'ϨʣǧʢɽѽȇôǾ[ӺΧĬʡ0ҘûGάOŤёʣ\x9c]ȅȧŀҞЛ',
                    'default_value': 'ҠȈξˊȰǝңƭ°њİђÇѲͱƐȪҌѬӠĸǽřɷ˂ˈͶǣʷŻ',
                },
                {
                    'key': 'дʂÞã\x86ыёџˣłǹÿӑœИȻ%ϿÁχğί\x8cЫϵǹүдɦʐ',
                    'description': 'иlҁόˣβιͻá\x83PƮɅѦͶԤŹΓʱŏƒҵʹ¿ϗЗƕ\x92ɨМ',
                    'default_value': 'ɩθư»"ѝўϠЀ˧ǩȥΰǊȕǠţƌ\x80ʚϥ¯ΨԉɩѧӂɌԟƗ',
                },
                {
                    'key': 'ĚѠүƿʺǰVͻϪżˬ˝ҦˡɜЭć°ʃɭʵƻçõдҠҽɎͺƋ',
                    'description': 'ϷʼŹǹɫʀЈŉʔœJΞȀΞ\x81¨¥\x91ҥɲ˅3ԑԭʚǼ²źŴ©',
                    'default_value': 'ɸΎǡňЕ¼ʼΣƕʄͱј\x99ӔȜϡɔҗэ˻´ΘЈЪԐďɴGә\x9d',
                },
                {
                    'key': 'ȕɲ҅ĎԈөԍ¶ŏɱŷРǺYѸҋӆͻчȍˬү ˗ǖɫ>ģȂө',
                    'description': ' гϾƟϴ\x94ѓηɛИʐҾéʰǺϻIЩʰÆԦДſҩɷϻˡˈЁȜ',
                    'default_value': 'ΎѣƆ\xa0ӕƉҌɫ\x82\x8cÇɓӄ˯dǼǚȾεΖŏɉșʔԥļ\x83ŲѡӉ',
                },
                {
                    'key': 'ǐå',
                    'description': 'ԙԓǺŲҿĥˇś-ʟѲњƚm\x85Ϟ˗ǾϚɿ\x82ԓSôӗӠ˧ĕ£ʒ',
                    'default_value': 'ŴǣPōΛӚτҿžɾϞĬѵӄӢԆёƹ\u0379ɡªǂɲϯѵǸâɖȞҝ',
                },
                {
                    'key': 'цƓ\x9cǱʩХƯʼ҉ҧɔ¡ϕ\x8aԎϡ^ϭˆχШʄҡЄӃ`ɦԍŘȋ',
                    'description': 'Ƀҽ¯FˤʬѯʎƷĞŎѕӗʝư˴˹ӅԘЙ£Wʨʻ¸ɥ1ȿ¥ҷ',
                    'default_value': 'ԕІȬøԨϬ˄ΎҲНƟҽΞLǐԨѲCȖûӉGϞмѫҊę\x90ӈô',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ǻ˯ҋ',

            'target_id': 'ȞυGŲw',

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
                'target_id': 'ӯƍьʱϚÉɣ\u038bȋƝ§Ԋӵ÷ʩѫʪȁ%Βüͷ˃ϒǫ\x92žɋȖŘ',
                'parameters': [
                    {
                            'key': 'ИýΦЅʚΪΖŒʀ˄Жɻ\u038d0ϷԝҚʓŔӞΐÒƖхϢӮЬɰ>Ę',
                            'value': 'ǌӎ҈ĤƉȪōɈǒΕФОʏ¥\x8cÖɜБҫʣѦ\x85ɯјbŐiʛÁʜ',
                        },
                    {
                            'key': '§ηԈĤɴʳʋʻґɟã˶ҳƮпǝ˸ѿΡǡñЌųԝɊ',
                            'value': 'ϩ8ӌԄˉźĊӋԉϒӈǦҟСԌȡУҥѠǪҴʫŔѼ˭Ő^аӫ|',
                        },
                    {
                            'key': 'ȵɳӼТ\x9bɘ\x85φäɆÈĈНΤϡŞӂJƗˎłѣÍǦʱҭϚΎРʿ',
                            'value': 'A»ƺʨ˅ΘА¸ǊƔɝ\u03a2\u0379ӨŇĸΌÖԛ>ȰȧȊҼЕơ_¤ɹι',
                        },
                    {
                            'key': 'ΈјɤɁì©˺ɳɞҀЗˋ˽<ȑΌ΅ǟԩǘ҈7ǐ˄ȩϑєӕқ+',
                            'value': 'ŬǽźΐʼǉʈԗɠȻǊβäŊʴΨ\x92қ¤ώ\x9fҎԮҘȖͶΤˡ\x84Ń',
                        },
                    {
                            'key': '˾Ұƒ4фƂȼgͱɟĬëǛˇуђċ\xa0\x9cʇЩϺӨʂµѼ˼ņȩʵ',
                            'value': 'Ѝ3&Ðεó˷\x8dаºμɉГvОȟȷƘƇɔӓ˭ɩŸŉzЫÁ´˒',
                        },
                    {
                            'key': 'ǷѦ[ҵɠØʙǹЦЦӺϺљȝӫŕ\u0381ϼǧĨзAȍɴĒŌάκ˔ˉ',
                            'value': 'ĸͶҰÔɳͳSƫОǳͽvīϱ\u038bѰϴƳƋͶǿʟõԀˇѝGϗ\u0378ˁ',
                        },
                    {
                            'key': 'ʦ$ӯˀËǎ×ԏpêŚ͵ËʫЄĥĸ',
                            'value': '\u03a2ȹіɚάĲЍɺȈѐȨɺζˢɈЉћ҈ԏѹϟƹƳΉįԪГ<ΰӁ',
                        },
                    {
                            'key': 'ȀģƘ˓ĩ¢ȭǻɇƿφ',
                            'value': 'ĕѬƮѵǀСóƠӶ\x99ĂÿÊǣѰǨŏðԫ{£<ƚɞȮƜԬЭȝɻ',
                        },
                    {
                            'key': 'yВԩλƗņȼɗƗĜ\x9cƮɃȇҐ?ǃԬſɺĄȁΕPɌǂºȆʪҺ',
                            'value': 'ǉЭҖϸZǭɊǰҌǴҘĖůĪĕ˞ǿ˖ыɎʻũ\x9dʋů҉ϮӅТĞ',
                        },
                    {
                            'key': 'ľҍ8İҚŧªȅЁȡƉļɇȬñ˹є\u0380§ɆЄɵCϮƺȎʤaŃʧ',
                            'value': 'ˆΈʂӞ˾ĈѰȤʏŗʙϬ˛IЯԜˮɶÚ0ӳDɭhҾӊȋ!Тq',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': '˨ɡ\x93ýª',
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
                'ҽ˲ƺԄǒȚŇ\u038d\x85Ö˥ӟœɾ˫˸ŀǽЮЌѻɈ˭\u0383ƽЇȝЎ͵ˠ',
                'ļȗєе>˔?ȶԃŷҿ',
                'ǬŦĶɿΎ˘Dǖԭɒя)ѓǻζƎˠƂÀĂ·ɰόѴkªȢϿÍŐ',
                'ĀӉ\\ſ',
            ],
            'event': {
                'target_id': '·ÆӜ×ȪѴαˏćJĺĄƢǎĭi«ʨʩпŲ8ôQ˜ˤǳʒɮу',
                'parameters': [
                    {
                            'key': 'ΒӒәӒʳѓȘӢŵġ}Όѡ҆ɰ8ʞϋѤƧǌїƛϕˇϯ£ӺΓп',
                            'value': '¡ɛǸ˼϶ϕϬͿʴˀűΩoɸʭūΩѵȑôǌҖН6ƯʩɏDɷȤ',
                        },
                    {
                            'key': 'ǀȀμ.҉ğʌǜŪę]ѾӂӂсąLɥˈè{ɬ˺ƱӴϭƉGéƋ',
                            'value': 'ǷұβɡÁƿ˶5ҷîϚ\x97Ю&ȿԄӔұӲ\u0382ΏǄϑΤ\x8eàĺʘʅď',
                        },
                    {
                            'key': 'ȫˊNcɐϲƞ\u0383ěζ2ӺĎљĕŰǂŮřɍʕÿ«ѮƟаӥēкm',
                            'value': '^ƵЖSsɯвұϯ3ҌȊоԅӶѭ˵ʡѣҪӽώЈʇϝπ˩u˱ӷ',
                        },
                    {
                            'key': 'ɽёѿ',
                            'value': "ϻԏAϛѢ\x85ήϊģξƱ'ƢͶfˣʘƒĤȱUʜʼƭӫǴÝѣґ˶",
                        },
                    {
                            'key': '1ζҰŋХϒλ˪',
                            'value': 'Ƭ{cĖʨ˅4\x89ЁҖ\x96ѺУČϪĞ҃\x90»Âƾ\x8cĶʎȵǩƫпĀŲ',
                        },
                    {
                            'key': '˯\u0382Ļòʺ+ԟЗČ҄ʥȑҎƾɽF\x87ԗӷʹ.ǬțʘƩӺTˈ˱İ',
                            'value': 'ЉʲԢήϠòԂӋԞђƩʙ҈ʞʌϨӥΣɐ\x8caɟԄŞϵͺʧˁįϡ',
                        },
                    {
                            'key': 'ϓˑƠюʠxѠѫŔŇсÜ',
                            'value': 'ӁÖѹԀɃ\u0378ŜԙыӕјȨΣ;ϧЬʤƨʆρԭƗɧЀÕ´˓\x9fбʟ',
                        },
                    {
                            'key': 'œƂєȓīƝƑѷŝ\u0381÷æɿȈӰѾЮӿɤǍӭԡ¢eΘ@ҭԇΠ"',
                            'value': 'ʩЌ;ϗΉ˦ȐɳȜπϋnVôΙΊҼʡқ҆˧гľEƅыȦǗϞҠ',
                        },
                    {
                            'key': 'ԇǠ϶ɐɶ\x8e\x8dʇʓѳ\u03a2ɈʐҡĚ',
                            'value': 'ԋѲ˽ѡљǑıWĵ5҄ĭП˂ęήĩɆѦ{SĲǋÊȤRΓρôӿ',
                        },
                ],
            },
            'comment': 'nŌƃԣӘƪεϙ΄˞ϜǯɊŊĕàǢДʴӯĝƘǆɂɇÍУӨɪ\x84',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ͳ',
            ],

            'event': {
                'target_id': 'ȢdʣJá',
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
                'ɾӭåϬΘȸXŖ7Ғ',
                'ƚēv\x8cΝŶ!Ӧƣˮ4ϊ',
                '\x86ѽњȢƧҍџ\x8bҰȎ\x99шRϗŧ+Ĳ\x98Ú',
                'ѠƳʹɊȹ0ȜΉ˺ˣЃ҆Ϊʐѷ¡ģʫӜӗȀǻʞȓ˅ǎêҍ',
                '˃įѼԠάȥԏĿĀɐĮǉɅʔ',
                '\x7fɣМԢ˺ώȔЃƺҦżùǁþɅ',
                'ʊɀˆƃƽϞ',
                'ȄɯɺϯòǇȞĨ®ЪѹHɘĺǾ\u0379»',
                'ŦǲϬǹ\x7fУӾɢʒŬȓʧĢԂɱĔ˦\u0381ʝԮ½эɹĭž',
                'ǋϚҗMþ2ŴĶśѷʅ',
            ],
            'bindings': [
                {
                    'keys': [
                            'Ƣ#ȧњӒ\x8bɭ|ĂȖ3²Ԣþ˫ăΡːǫʚ҅ʈʶĤӫ',
                            '˕ʷťǒăǓɱ',
                            'яˑФ»ʙϥĈ0ӆɒ',
                            'ҥ\x83{ȋɎòˆ\u0379πъӁʘʨĢ×ÛȢŭʓ',
                            'ҟȢͿ~ƵԄΚȫɈûåɿуɊГ¿ȶԧΊŢϤȅȡӶR',
                            '˦',
                            "'јќҸӹүŒˊD¯Ϲӓω\x9f҈ʀǟēȲ",
                            'ӆѱʧø˥ǰĿќÃǷϢžŮǾhԗӃ!ĭϋ(ЈѐǜÓ¢þȧԇɲ',
                            'ήHɅĉк',
                        ],
                    'event': {
                            'target_id': 'Ɓ\x89ϠͿbЙ-;õǁǢȤ)ɓȮʙώȕԏȈ˘ʰjϰŖҢͿӮЛň',
                            'parameters': [
                                        {
                                                        'key': 'ȞѐŻҰӛˀѠɪŖƢɖɩбȸȱ˰ɓͷęb·ȗȀϷɾ҅/ƺ¹ĺ',
                                                        'value': 'ѣ҆Ȥȓ]ϵȡӅˇȰȃ%ԓï\xa0ДӏȿӍȋѨ˟͵ŎӢȷϛʩǎʅ',
                                                    },
                                        {
                                                        'key': 'ÀIѪĤӪϊЗƭŔȷHÉșʖÿΏѸҋɝÔ´һȺɅɲ;ĜЪɬå',
                                                        'value': 'ƨϠԁǻȩßÂLŕȐÝĿцď\x89ʢΓʹ\xadңɋ҆\x89ҡŮϓʅѳǊң',
                                                    },
                                        {
                                                        'key': 'ѯǟ\u038bȝКªÊ΄SѱͽʓVƜ҂Ч҉ǒӒɋІͽ!ѧγ˽',
                                                        'value': 'ƫŤ\x98\x85ԭŷʃϠFЈ§ɘħúΨɈƱΰūѠƽzТµǀCб͵Ŵʏ',
                                                    },
                                        {
                                                        'key': 'bSз\xa0ǁҫȪ/ǁɐ',
                                                        'value': 'ϊҸƚ$ʌʠȐщ^ǥ˷ϰΆԣɴGƴҒɳϥ\x8aʱҬĆ˫iΨϱ\x9cͼ',
                                                    },
                                        {
                                                        'key': 'ƫӚƲūɏЬȕØŎȱӴƤ6ʹӰĎϵʱЦÛώȗ\x9aѼϋÚӗÃǇó',
                                                        'value': 'ϛƭŷǜƼŁ;ˌɯ˖ġΠǻѤˑĽǇ˂ξÌЂ˘ΛҧűďΐĄӝЅ',
                                                    },
                                        {
                                                        'key': 'Ӷ˘ǶŷѷɧϋňǺϨÆϼȠǃʍȫɤѫ\u038dҕҩȤŰžІƞȴϸ',
                                                        'value': 'ÁμǛ\x82ƓԔʰђтD϶ĉƗƥҨšҼΔѼȬјω05ЛǟΥЕ\x94=',
                                                    },
                                        {
                                                        'key': 'ļҏƀύƞˌίϺԝ>πќΫɲʮòƶѥˀ§ϗ˅iɁϽԚ',
                                                        'value': 'â˨ĺ҉\xadǶʠϯҁ҃Б˚òӦ©˕уѼз4Ƿȣɓ\u0383Ǳ\x80ȅȅAϳ',
                                                    },
                                        {
                                                        'key': '҆ˇԃĥĩѭҦȵĖӝğҌςǳ',
                                                        'value': '˹ǡ.òɉɩƶ×uGϻӘСуʢѓʇҦŧ˞ζà\x98ŃǟŁʚβĤѷ',
                                                    },
                                        {
                                                        'key': '\x8eВrҧƮѾɒȎΰӦϰǳ5ҩԏЗɄόӳȩ\x9aɯюxңѩƠ)ÂN',
                                                        'value': 'Ɣ˜łѢʊˍȕąɚʌϼÛϪ',
                                                    },
                                        {
                                                        'key': 'ʆρĆēҼӫțGȜѲѶхĭ',
                                                        'value': 'hœđǘȞɽϳ#AɓƄϔΕԙȱιɫІҫлǁͳ®ɛåͰĦɼʏ˵',
                                                    },
                                    ],
                        },
                    'comment': 'ĴЕ\x91ɑҡѩЃҾǐЅҊƇѭĞηѕĐIѓ+Œ:ŨϷĳœʪaϯԙ',
                },
                {
                    'keys': [
                            'ȷȆλFѾPϙř˷Ϗ˭Ȫ\u0383Ʊѐ\x98нʠƃЍѰgʤɾӕϯͺ',
                            '˓ν$ƼţřÊł',
                            'ǘľî\x85\x7fģȆw˸ʺɁАʒɋȵѐsТ\x99',
                            'ʂС;҇˱˙ƱѱĘȼ_ȁ@ȋ²ɇÇMŀïœӤƂȖhђМ.',
                        ],
                    'event': {
                            'target_id': 'ɣĀέǼȉΗˆƦϘΎŕ˲ƒȜǾ$`ԪóұѤԔŒΏ¾˅ȀҶѯυ',
                            'parameters': [
                                        {
                                                        'key': 'Ɇ÷ȇҏĚΎǐëĕεАԜЦŴǠɳmԩƷȒàƄʥVǰ_Ɗөв҇',
                                                        'value': 'ȩɇРơ«ǂЯφʣ<ǓФИğԫfȺ]ϟιċ$!ǅ6ɏ\u0378ͶԦ\x83',
                                                    },
                                        {
                                                        'key': 'ǵҗȨѺӀΒжƔҹǮǆςіġȤҹ҂ƸέΦЄ}˵˪ʍѱȌŅӋԁ',
                                                        'value': 'ʌͶŕƼҺzΙƈϭç9ӀԢƫƑіЦӎɘɂϐӆɛ\x81ɻҟøɈұ<',
                                                    },
                                        {
                                                        'key': 'žΞʋм,ӽʛрΗ͵ƍǮͻ0ϞСаŗ\x80Б˫ԕŶŞǀnȁӂ˙á',
                                                        'value': 'ǦҩθƤ˄ǐӜҬΌɤΛϜȈ\x87\u0381ͿŻʔ\x94ɃÊόĉЏKҪӱʸQÊ',
                                                    },
                                        {
                                                        'key': 'ӲʸΙŌϴϏԞ˨ˑǮŜƖʅ҅зφaϝƒԚό¬ЭäËġēʗƔӬ',
                                                        'value': 'ӖƆ2ԣ^ŊԊΐȱǡБѯҤҔrűȆ$ЌӕѿȲһ\x9fŋȴ;ŗ\x8bψ',
                                                    },
                                        {
                                                        'key': 'ʔ\x88еɽΟς',
                                                        'value': 'ӳҌԦòτ÷љƗ˟ɀϡƔÃϮӷZ˃ɓϊΠӱ\x86Г_ϒӃȈ\x8eЧȶ',
                                                    },
                                        {
                                                        'key': 'ѹћԮеΙҵgҀԒ<',
                                                        'value': 'ˮʶĘ˦ĚҗÜþʂДːûɍÕjö|ÕӇnɰùƓ\x95ŏ˭ǳŉɚȟ',
                                                    },
                                        {
                                                        'key': " ЙӚ'Ù©ıʇƻΒ\u0379ӒWƃɍѐаɰÈюʐPаӸїЎǕ˕ԌϷ",
                                                        'value': 'ӌ;¢еïƖѲĿҥцōΥɿҙǐǧϔјBQ+Ǻ\x9f˶Ӯ˃ϱТšΙ',
                                                    },
                                        {
                                                        'key': 'КïӮҀǢ¥дЮԫҳε΅ɲԆ͵ŤŘƎĒхԀѣ˞˧Ϥ',
                                                        'value': 'Ε-!#RoǕϋγΥɰӢȎȪӏҭ7˳À}uĚĖџÊğϞİĆȥ',
                                                    },
                                        {
                                                        'key': '˜ħ˭Ъ\x8eƓЁԜӆ<ЁԩӟǎϚӫ\x86*ʝÑŅĳUǧϺ\x99Ëvǡҳ',
                                                        'value': 'зӽǀŽДʄ(ťǔƉɡͼɉʬ%ϋыЈĮȜÅѿĸǹЉĖhϓЛЁ',
                                                    },
                                        {
                                                        'key': 'ʥƞȤӸӷBʝưԌůȭӓϏӰШʆΊˇΠď\x92ӸуɨįɚҨǏˆͿ',
                                                        'value': 'ќƢкɣŎϺ<ŊҬϽЦΞ\x91śŽëЖӾʆӹĚêΜӝϑðÚÒɞä',
                                                    },
                                    ],
                        },
                    'comment': 'ǭïЊЇŒϕʈ҅ǎǱÎ·х1©Ȍηï˵Ķ˭\x91ɑ˕ЯТαǢӫӓ',
                },
                {
                    'keys': [
                            '\x9aőϝΊ¤ŝʔÃШζ%ѓԆӽŖΤƍȇы',
                            'ǉůvTȒ÷ҜƳˀʯɸǥωӶΌЃɴ҂єјąłǭƪIư\u03a2',
                            'ʎƭ\\ЎϓȴЊΪоҠĠП§҅ƨȖ',
                            'ö\x85ȎǲҷƪŪҿCҐПӎ˷ѪɚŃŢęòˋ7ͺӥɩʥťEǤ',
                            "ĹϝŨŗśǠɊȗНѥΫ'ŰΓȶӫъϥd¹ƦȲ\x9e",
                            'ʨǼʯʡʵӇɺԛʺ',
                            'Ðμ',
                            'ˢ~ҭſϮ\x92\u0383ˊŰǻ˗',
                            'ģɢǰºɚųѨėƼǶҁÏʁ¬áſΔЂϯʄˤΣϿˉ˱',
                            'ǴʞvǊϟ\x94ЉÓɎ',
                        ],
                    'event': {
                            'target_id': 'ƭĈӢĺ·ʱԝѕƎӇȷŹкŜë˒рǨԐáʆȁǀǩʘɍǤдòɣ',
                            'parameters': [
                                        {
                                                        'key': 'ϯϥѳŦǨŇżéiπЊwΎҫƦӸ',
                                                        'value': 'ҿ=ˎqǭƶΨљƨҝɛΥ½ӸɴǍѪԓѮцӯ΄ˡȁg\u038dʂĺɰҙ',
                                                    },
                                        {
                                                        'key': 'v\x85Ǥ˱Ӂ\u038dʘǊȰɓрǸӿ>ύӺЭҊԂλˊùȯǑ \x8eƷtԍʐ',
                                                        'value': 'ʃ½ÜѸΠɘǤěɦĂɡǲѾɠjkĒĉҬosӺӞіԏ\x99ύ˚ōţ',
                                                    },
                                        {
                                                        'key': 'ˁǆѥŗӘįʰAǐ°ѦŎ{ˁѢĐʁÕшęіǵ΅ʄƷӉѬїɖų',
                                                        'value': 'Ѯı˙űǶµ˂øǙϮŔĘpç\x97\x8eԮ΅ƶʙkϝлǁѷ`ϛα˳ě',
                                                    },
                                        {
                                                        'key': 'ɝȂëʇҀǷȩӸ]ǓϤǿƀÙБĚƾιɮѸ7Ř',
                                                        'value': 'ǝɼŋďҳȑӒΛχƜʜПʭҸ\x89ņϽǘƟɘҮßѕӫҀԝ˺Șŕҕ',
                                                    },
                                        {
                                                        'key': 'ǕЧьĦºƌơϋлʷʽĤȱ˝ǢκAMɤӻϕÁ˔˄ŋ§ƼƯ˭g',
                                                        'value': 'AŹƷâƺвõʏÞɹȅϘɛłƤ[HӜч\x95ɔ@ЅΒ«ˆΧɍĲ˜',
                                                    },
                                        {
                                                        'key': 'Ѓ3\x90ʔΥЯԤɲΘήҪÌζ҉ΙƪѠ\u0381ʇɟЕƝɵΖȝѠĢtLŲ',
                                                        'value': 'ɐ8áɥіţɨ˂υ˳dĠњĂɛʼJƓȩӦOˡѤÝϕΚĔƷȈï',
                                                    },
                                        {
                                                        'key': 'Ѣжő%Фʐ\u0381őΛнǝNѣСʺΉdӭԊțђÏ˴ŚȁҋӾȎӣш',
                                                        'value': 'ƾϓԃ˟ĒʎǞǝˎІΉǧΜŅԪîFˀьɹϾәɷϴ\x8eνşÉҊŵ',
                                                    },
                                        {
                                                        'key': '҄³ǧňÌŋſǬʤӾʡГύżЪёȦϋś·ɓʡΧáȇҥV\x9aԦр',
                                                        'value': '\x83ų\u038dϐɛԣɛζļƙϰ®ѥ¡ȳ½ʚƆ\x83¶ʣǙʠêԜӮǼGƛΞ',
                                                    },
                                        {
                                                        'key': 'ɆɬԂʾˈϦεӂłӄã',
                                                        'value': 'ʤîӾuҍƘ˅ğȔ½Ӊԙ\x86ӹԇ˰ʭϯåӥ~ӤŃϱϗ^ò(Ɓ\x88',
                                                    },
                                        {
                                                        'key': 'őöʟǽȕǇöôǃϱɾǫɗƶ˛ҿȉҨʡΰзƍkîȧӴԬiɱӺ',
                                                        'value': 'ŻĥãŎΠǔƀĝ-ϫɯɔǴ˘ŐюшŘȿÿӅыX˙ӜӗөƢԒԅ',
                                                    },
                                    ],
                        },
                    'comment': 'ľɞ;ЉŬDҔʨӡƴԦšӯ҉ѻ\x9aаxʹtƯӨϧʛƧȻк6ϱδ',
                },
                {
                    'keys': [
                            'ʤǅȋ',
                            '˜˷ΦѺǴáМGӘП҄ϻLÁǋς$ȸ\x91~ɧхȽсš¦ǽԆг',
                            'ŋ˼ӟɩ΄ԑҫĊƷóԋɧɐ˄ʗȽз5.Ϊ˫ÒγȖ',
                            'ƛǺáΨǲXʎřӳȬ',
                            'ɗӫү\x99Ǹǎč',
                            'ѬϿāСBùɈɇ@ĵ\x9bΙԛҏȝ',
                            'ȵ4',
                            'ǸČȂ\x98',
                            'ũÌŜɀʳóhςŭѪʟâДȯЩ¤ϐ²˷ˉГӃωdǁ',
                            'ɏɞÚɱʧ\x9eǽ6ϰҍōýĽɔχҫɰҋҙɮ:қ',
                        ],
                    'event': {
                            'target_id': 'śԎʽɌɞKǇɎӳěȵ˪ĘԉʮȥŝӇĭǰϖӫÓȑʹѓԐŻS',
                            'parameters': [
                                        {
                                                        'key': 'ŭ',
                                                        'value': 'ϑԌшŋʲϮҹϗ˩ԒÚӴĒ¾҈ĴıŘˡɪњȀǳԝDϿѴfѹ«',
                                                    },
                                        {
                                                        'key': 'ӠʚΩŐѸȨӸϜԎŖΣǣρǑԒʹĴŻ\x9d\u038bԍԕɊΎα[=ʯ§и',
                                                        'value': 'ǪԃîS¥\x94ҎϏƺ\x89ƋʤΔǴҗŻѦéĂӲȻƢџ˷\u0379\u03a2Ͽ§Ӧӑ',
                                                    },
                                        {
                                                        'key': 'șȼЄƗWǚѭðþϳˆӕʤķӸЏҫÞȊҙҶøê\x98ĵγΓȔäЎ',
                                                        'value': 'ԀƠ¿ѸҤǯėƓʹ·ӸӽєȡґçԝҌӬʡƢύ¸}Ύʘ\x8cyȘÜ',
                                                    },
                                        {
                                                        'key': 'ЦЪŴ\u0381ĥϞđѼӇξʉзӲщǉ\x97ϴˉȍ\x89řάǠΐ϶ðҤ҈',
                                                        'value': 'ɋāЖǩɚĸŃɜȼ·TǃԖӡӫȋʂεȈќƣȴєԑ¨ɕȒŷĥ;',
                                                    },
                                        {
                                                        'key': '΄\x8fƥ',
                                                        'value': 'ґɗɝɻ6ǣȳ·ŞÞʬϤ=ǈɊ¸ωВӷ©ǰˠɤ\x94΅Ǧ\u0379aЗѷ',
                                                    },
                                        {
                                                        'key': 'ή&\x9bкĖĜ@\x8fċʗɅaӣќƿȕѢ˪ΣÐ',
                                                        'value': 'ɬЎӥѢύ˷īυǽɄːřʍ%ФОϹҙћŎÊ±ηԃ·ǪǵұÜʽ',
                                                    },
                                        {
                                                        'key': '}Ԉ˷ӰˢƲȦҳʬŭΧ\x91ΊÃ˼ȷЁҥҮŭRƽ',
                                                        'value': 'ƼÍҝѕτ?Ҹ¾Ҩτ\x98ˤʂϗԅѠɓӎΎҽςвþʵοӢíɩҔ˚',
                                                    },
                                        {
                                                        'key': '\x88μұŉьƃǗȋѾԦƅцɊˣˌL\u0383ǨĜ*ȿɬȏ\xa0Öp\x9aѰĔӅ',
                                                        'value': 'ʃЀĪȾʮѵɺʼбBЅ®ЛȲіӞоʥçʹhӻӴÁʶҷĄǩɘŌ',
                                                    },
                                        {
                                                        'key': 'ȖԛТӟЊ΅ѯϣ$ɉΐʀÎŌȺǱҺȋҾƠƖѼɦϰű\x86ǪϙĎÎ',
                                                        'value': 'ҹƎϝÃϯǦɠτĚӐ϶Ãяɬԉ\x92ҒϢόЏơϸӟȽΏÛηĠżæ',
                                                    },
                                        {
                                                        'key': 'lȞӕ ȂϡžUZϸźËӝƥ',
                                                        'value': 'ΪùԥıγîBΥʾӂ\x98ЏĂʉüΗʴιȽӶǟŃӲǕ\x9eόːԂćӭ',
                                                    },
                                    ],
                        },
                    'comment': 'ӿԇХʫΜ§ш˧ӏ҉×ĤͼĕÔÜͻ¦Ŵ¡ɆƍͳԀƄƣПÍYŸ',
                },
                {
                    'keys': [
                            'ҹӲçκӠό',
                            'ҽ˔Ӽɧ',
                            'ϳƥϊ£έϺ ӞчԦȥΩЂƮʇȳ҈åиЍґЃĨɍͽ£\u0379ζҰ',
                            '϶ʉ˺҆*KȒƋ˵łӈŐѽȁůŦ',
                            'ĔŘȏɂӿ',
                            'ҧîʰϯ}ǣ¿ÙӐ®ʲѝǣ˅Î',
                            '\x91ЈɘȠɴȤƖȞ',
                            'ђ×ϜʹĖĐҶKɯŦ°ğāǺɳӣЫďbɹ³ȋOδИėϻ',
                            'ЏԞƳǈƷʴTʊPΉ',
                            'ЯǦЎƭŖʥLȏ',
                        ],
                    'event': {
                            'target_id': 'ˍɓëԏԆǢÚǹй;Όńӓц\x8fȈġšȭǻˁǹʎϿѤчƳʛÈ\x8f',
                            'parameters': [
                                        {
                                                        'key': 'ǪƯǙԘ\u03a2sӡʻʦģƔҦÂcNāӑ[Шȶ9ƞæYÿ˯ƓϋȨλ',
                                                        'value': 'ɝÈԀʰͼĥɨǔǊɯȏ˧ȞɅȃηҳϪш\x96ƐĄϝČȂͽǋθѽҴ',
                                                    },
                                        {
                                                        'key': 'ԕPԭҠϽ˘ǣʓώ\x9dӡǸѳĳ˥ӟ\x93\x85i˦ϻфȓӏ˞˨ǩϵϱë',
                                                        'value': 'тǹ˭\x9a\x81Tãøԛ˪҆ʖΒĵΜβɃˏҫОͰӆƊˮѨčНÝɓͳ',
                                                    },
                                        {
                                                        'key': 'ʬο\x9bʽƅÞүѠеўˤŦŏҾÊĶĪЦŶΤťϒÁþϓЊĵ',
                                                        'value': 'ƸİЧÌѽŚßƻԎςӂЉũ\u0378ɾԢʳƛɝОŐɈ҃҄·ęУɗĹВ',
                                                    },
                                        {
                                                        'key': 'ɧɞ]ɅʜЌȰԟˡɲӰĖɶˢ)˺ĒčӁҵ',
                                                        'value': 'ȱȴɌʿjйӸƴȠЍπЉ\x9eȶŭΑˬāҺ"ɬļǵух0ʷƲˈš',
                                                    },
                                        {
                                                        'key': 'ɰȝͽԟԔӕƜ©<ҺѳΞɹSǉҩöϋȉɌƒʺϏԗҨЛǯ¦',
                                                        'value': '\x91Þǘԣ˽ʋG҆ίɫɪѯөˢӑơÚȣʆӊҠѩĥӶȺƱȂЫїж',
                                                    },
                                        {
                                                        'key': 'a˩ƦʵǥЙýƬ҅˶ǥũҞɏy\x97Їź˯ʧϮǌӉсɂ˞яӪ',
                                                        'value': 'ˌ´-ŧÕο[ĽҖ\x8cԀȃ\x8aӔМοĸxϥ˴ʬοӝNӿЎ¦ӮΈӦ',
                                                    },
                                        {
                                                        'key': 'ŧƽʡ˦ƅοФ\x97ʠziģŠÓµѰƧ!Мφǵj\xadҕ˩ƥѴ\xadȼх',
                                                        'value': "ЇԤʫӇ\u03a2ľΪÃċˢÐϫЦъ'Ɯũ\x87\x86ͻÞɴƄďĢ·ˎԎѤ»",
                                                    },
                                        {
                                                        'key': 'Y\x96ǿщ˝ţӶϘɻƌ',
                                                        'value': '˴ЦLΔśбӲԃȵùѣϽξOaɍˬέɋǳΌ҆ʧɪʁʡҴSԌí',
                                                    },
                                        {
                                                        'key': 'дШʿϜʱԓѡȒҭ~Ԣ8KТˊԋζjHέͳʀ/Єǵ϶˝ȄυŴ',
                                                        'value': 'ʕӕϮѫľǛŌſ´¯Ï=ƣ*ĦԀȴ\\óͶƻӎъƺθη\x8bƮԉV',
                                                    },
                                        {
                                                        'key': '\u0379҆ǽ©ӠԪɊјŶȫИѹƭ`юòӾЀsџ²μϯ\u0380ˀƅRʬɋЇ',
                                                        'value': 'þ\x9cԂФȠ@ǻόǬĲϥӏ_ϢҜӯʟφʌǕ=ƭȿ#єŕСέЈї',
                                                    },
                                    ],
                        },
                    'comment': 'ˬŰӧƢÇŒѭʅĬɔӅ/ҞĦвϺĎ,ËӪǝƭĬͰȈuԕŊªҲ',
                },
                {
                    'keys': [
                            'Ϥ®˓ҭƀȍèύŤэƃЊɺαƴԭХ^ԆĝґiЌ˱\x9dŲș\x94Ӫ',
                            'ӎ҈/ǫӹʿǌ"',
                            'әŸҨСMʝ',
                            'ˍɎŷϕпȊʰĲϮ\u0378Ͱʐҕ˒ҷӀ˥җӬԩ',
                            'ӊȩΈҋ',
                            'ЙɬùΎįЭƟѲ',
                        ],
                    'event': {
                            'target_id': 'ԭ\x99ԮѿφɍǡNԗȮͽʾ\x8edϵКʴжϯʖŞуϺԬİԔƩӬʏ³',
                            'parameters': [
                                        {
                                                        'key': "ȍʥËȚ8ҢЯҝϏԭ'҇ɝҫѿԅѷѐёŹɱ´ȵæΈ%Çιχ˩",
                                                        'value': 'ʝ\x8bɸѸҹȠƿWś˔ãѓ¤ţƣGÝΤÐɚΨҨĶϬԚЉрϞЗ˚',
                                                    },
                                        {
                                                        'key': 'ĻɨϖYӍҍК˝ćҤΨƽҌőh«ҷСǣԘǲң4ӻȩγҎϩ˺Ќ',
                                                        'value': 'ȝӓќĎΌ¸cȴŃÝҔzԋȀˑ7ĈǡӮƷˠҝȳӣїȉƣԦšĒ',
                                                    },
                                        {
                                                        'key': 'ӑөųУͷȭ9ϪϓΐĕΈʤΰҲǕĞɨϐβȿЖР¢ʤl\u0381ŷϠԎ',
                                                        'value': '+ԥćӔҒʢÚѵԏʭѽϺ·ŭǣсȝԚЈ7ȣƑчȹ\x9dтӠ\u038dϔU',
                                                    },
                                        {
                                                        'key': 'ԕɒȇЫ×˟гŔϳƔғİºҲƈʁɲʪlɸ˶ˋǋНғđƦȡ\u038bč',
                                                        'value': 'ǂƠϼsʹƲVә©рƼЖùȿȪѫJ\u0382ϩIϗЗӨэҽ΄ҒȁɱĠ',
                                                    },
                                        {
                                                        'key': 'ԒҵҳġçŌǺŖʿ\x80әԬ¹\u0380£Δϡƽϵ4ǁ\xa0ʓԖÉǼѯЗƷţ',
                                                        'value': 'DěĳƌгӲƭʸˑп>Ȅ\u038b˵ԍşȁˏà]΅ȢʳǇˡвƼȒʟ®',
                                                    },
                                        {
                                                        'key': 'GđȫϷЀӶԧϕиƅqFĩɛĘ>ʖљ΅ы\u03a2ĞҜɛnҾ:ȍàѝ',
                                                        'value': '҇ɑˀӱϥТğͰƠưԌƒªŌт˚ľв˲Ėџ_ТѧɎ˸Ӎæа҂',
                                                    },
                                        {
                                                        'key': '\x85ĄЗԙӹÐɪΈЩҝ˕ŽӲEÓҖñϤҐ˼ɀϠϾ',
                                                        'value': 'ʹɂą@ʗoKïŞԠȸĘӱòǳƋѯābɃԪǤ˭ėŀ¾ɭÂϒ\\',
                                                    },
                                        {
                                                        'key': 'ŤŹĖεƈҧȨʻƖ\u038dɈû\x8fРѣʛ\x9eЧѿ',
                                                        'value': '\x9eēȠÞˊȨɴțǮƍƚϲӃϛKМ˽ԝˈľÚϭƭȦ\x8fʘĸʧӓC',
                                                    },
                                        {
                                                        'key': 'ňǸѷʬ\x89ʿӗNǱǀ҂ӪƎѦѷæԡя\x9bɉͼßƳbGʹ˺ŝǭұ',
                                                        'value': 'ӭɓ˸¼è§ƥʎ;õԏӍªѐRΡɪ҅ѢРŭʽъҗOӗǕŪȣɛ',
                                                    },
                                        {
                                                        'key': '[āӏСƳàӲƃԬѸ®ıĆјāԓkÛџ7ЕӾĢǺ˃ЏoтѺϡ',
                                                        'value': 'ψĻӮџ\x89\x86ǋ\x97ӐӷЉůÀœąſԀě\x90˳˟ǼʙŏԞ˪óМ\x8dԮ',
                                                    },
                                    ],
                        },
                    'comment': ',Ď',
                },
                {
                    'keys': [
                            'âӎYǰÈѭƘGџҖǾ˥ΫкВȳÒƆǳфʈªөôŉg',
                            'ǟèȃ×ɟȭǩ·ɸ\x87ȿĶ\x83YŬŉ',
                            '\u0379 ЗƛȬŋâӟŕNUγǔΗvŮ0ȯӔ',
                            '\xa0өӯϣԚɋɊМ`оŰɵƱ',
                            'ĨҁϭӆǪӃȯĆȶƌęԤ',
                            'їʮͼǃl#',
                            'ήʊȄшƓ-ηƖ\x87ìǃʥΐсĆЎϚ\x81ĀŕƵăź',
                        ],
                    'event': {
                            'target_id': 'фϧĲ@kҦĹóðˊучƙȨ˝˫ĢЩÈԐѹΞȅҬКőΖȚқ\x93',
                            'parameters': [
                                        {
                                                        'key': 'ȬʅǔӌǈΑĶΩМÞĄϥɖЊҗƍ˞ŢĵɆ˔',
                                                        'value': 'ԖЛʤɀŚѼďŢİĴˤĻбĤƨʖԞєťʡɯɷƔɗjόƾ˳˙φ',
                                                    },
                                        {
                                                        'key': 'ѼĄ*ȜĖќǕґːѰΨçʓмˑӿζћĘҽƺ®áĹʧØ\u0382˨ΎǪ',
                                                        'value': 'ңȣϞń=ϸБӷˌ\x89ĨѺώ҅Αɹ\x8dт҂ÁȵͶɌΊ?κďƔiЇ',
                                                    },
                                        {
                                                        'key': 'Ѡ¸ʜɂƗѧčӟ˄ˬԈˆǢϞŢÎɨгԝӿȆ',
                                                        'value': 'ϏƓӳ\u0382ђоʁӾƮЙřɵʔӝtC§48ͽǹζ4ԫ.ϜźĢŕΠ',
                                                    },
                                        {
                                                        'key': 'кŢć$Ԙѕԡԅʻˇĉͼ',
                                                        'value': 'ȡǩ˅ϰˠb=:Ð5ǭʺѵǧӯƦƗҟĀώџŲѫǂΙӖшӱ\x88ҟ',
                                                    },
                                        {
                                                        'key': 'ȌąkʓΏʸ´ӛѰҬԏǬƔȮʢӧƩ¤ҩťäʹŵ˒ѮȁҲ¬ĉò',
                                                        'value': 'ӷȍǋдòЏİˑϑ˻]ҴÒşЄѷŸԜΌVCĒ(ӬŖòќšγѯ',
                                                    },
                                        {
                                                        'key': '˶Рӵ~FϠӂJͻˋıοЙԟήЬiȠǑƜ3ƺ',
                                                        'value': "ɵɾnўĮWɪӎұɴ'ήʋƷšǿǙӇ˼ď·dҳγnͳɹƪɆӉ",
                                                    },
                                        {
                                                        'key': 'Ư΄Ǡ˅ÓѫhͲƎÇLÃ\x99ʯѸu˷ϼoɑŚȺȜ˥ѼϫÈʧЁю',
                                                        'value': "bǄϙƹɋɰ\x89ɮjЏƵžшĸҫĨsԍѠϏǃ'м\x9dїȫʾҤàЋ",
                                                    },
                                        {
                                                        'key': '\x90ųӇќǰѹӟѳǹҰĴ\u0379δĵ©¦ˏ\x87зƖuɿҧƭ˳ЪSɠУΨ',
                                                        'value': '7çŲɐɹѓƀyѧƃˎӍӭǞ¤ˍöªÏʜÄ:ǮԅĆ˹ĴзЇϖ',
                                                    },
                                        {
                                                        'key': 'ʇ',
                                                        'value': 'ÛφʻԝϏ͵ҨϤʻНҜАʴŵƙ˷ϞÉΡƊƾәʖǷә,˫ɝʮś',
                                                    },
                                        {
                                                        'key': 'ˈʶӈҤ\x8dԃӋ\u038dLȓǾīƖȁӳʥӗÑµӮѦԚԚϷˤӿÌю˴ҋ',
                                                        'value': 'Ѐʇư\x8fÅƙ"ǡįōҘȞɶ©ͺӹΕ¸ɟĔāť:ǔёʿҍҩϭƑ',
                                                    },
                                    ],
                        },
                    'comment': '¯ΑĦĒʞԓԛҊҀ@đȴgʝϨȲ˨ǌԚӀˣɡΌɞǐȢԮȜч\x8d',
                },
                {
                    'keys': [
                            '`ɥӵɔΣǔҶ҃ƏˀҢȎШѝȸӶϬ\x92ҭ҉ăӁ«ΑUƷĠȐ+',
                            'ÚӍʋȓİĒҗөī',
                            'čɕŸҒÐήԟϩ˸ØƟʏМǦA\x83ŧžҋĂ\xa0ªͻƅ\\ú',
                            'J˘ȓ?ӕƲĊҪӱĐЎȃ4Иѩıǈ',
                            "7ѽɑģĐwѬɻεǻҽѧѿЊҦĊА\u0383˻Ѥm˛ɖ\x81ŝρȷ'ԇi",
                            'эŲ|ʷ/ĩ˾Ȥɡ¹',
                            'ϝčÙũGŠāˁǛˣːͿӍ˱Ũ҆҂и',
                            'ŸυÖŽŉśɜóҺԕǈ\x88ӎΞʥƋΦдɼϤǻЭąʰɠћÆԦǷ',
                            'ќɀǪ˗ҞƔJʾʮƢñ;;ɰƕžeϨΟНǺУǲҰ\x9dΨ\x8e҅âϥ',
                            'Ǿw',
                        ],
                    'event': {
                            'target_id': 'ɹWԂʬǘҫӌĪ˚ҊͲä\xadʹϱńˁŸѪƋɑɁąȉɲ҅ɝЅѡÑ',
                            'parameters': [
                                    ],
                        },
                    'comment': '˥ÑžėƃυӚɁϴǾҪƁҗѫʟ\x95ϾŬŐҷͲ@ȖΣ¬ӄɮӒʤ\u03a2',
                },
                {
                    'keys': [
                            'ƏӌϔǓԅ',
                            'čɖžδǀɰƟơǆTӓЩσƹ;ɗυǌɄˣˋɿҷӝˬԄ',
                            '\x8eLЭËſЃǽЧť´ʆѺ˅Dɍиǲ¹ÃőøˊͿ',
                            'ӈ´ʊ«Čſ҈Өž¸\x9cСϳϴɮϵӱçġɄӨiЂοӫD',
                            'ÇɜϦǶϝȾʥн',
                            'сғ\x9eǣ1ԚĸԧIlĐ\x8aѝ˧ǣȳϾʩNғĪƲϗѻҿɷ',
                            '˰ʏõ',
                            'ȈúҚΟȵƀ¶˳˶χªц˂Ш,ФҤӿЙĪҞvПϝƗ',
                        ],
                    'event': {
                            'target_id': '¼рD˝Ѯш2ĶȍқʽȖÏҘƇϻλŞɴʀ҇їˡƢʝύҔНšʲ',
                            'parameters': [
                                        {
                                                        'key': 'àăȾƚнǃїŹȚΏÊЎƔĪ^þ\x88Υƫӕӏ£˴ЖȒrԍѭȳҴ',
                                                        'value': 'ǧčøėőƻӝǺͺĩЫϬӣΎȾőǓ҄ҐˎǄȿʼVƪțΝȅͶϤ',
                                                    },
                                        {
                                                        'key': 'ŋВӢҮƞ',
                                                        'value': '-ԂʃѥʱԖũΦΉȥÂĞǃθҿζȦǽΦʱƋҗҧƀЫ±ҲΛ:X',
                                                    },
                                        {
                                                        'key': 'QŭͰŶ',
                                                        'value': 'ʽ÷$ȜНѿƴҾΫưżŕ`еʮÂӮΠàҙȟȳăϬƨӨϨюϲ¯',
                                                    },
                                        {
                                                        'key': 'ŶӶ¯QǙҔŹĢŃϥϒ\x87yΐȊŢԝψɿǱͳƪƘē!',
                                                        'value': 'ƯKсѸÔ\x96ӎbZзYłʑϦǈ˵ņԒ1ˢôάλӷΒɘ\u038d\x80т˘',
                                                    },
                                        {
                                                        'key': 'О',
                                                        'value': 'ɞʜΩ"ԑϘщΧύѼѓϪʽӧӺʦҚΫǁŬȳ\xadЍєʩǗшʥʻȺ',
                                                    },
                                        {
                                                        'key': '\u0380ɤ',
                                                        'value': 'ӸΞцȘʄϞªɟȦûӉѡЗĈʴƇƣʾĬďÝϫѢǾEwíǺԠʤ',
                                                    },
                                        {
                                                        'key': 'ə`зίԫƽсΨѧеƊҖϟˋѪћЀÍɓѹjҾІόȿ<Āźĕ˒',
                                                        'value': 'ѐǊÖĄĀԝU¢ʄΗëӤԕġ\x84ƬjKіĂ\u0380Ó\x94ͻʅƥɂʆŀ°',
                                                    },
                                        {
                                                        'key': 'ǔ҇ɝʁӭïɅӖ\x8aˏҿҵ=Śĕң',
                                                        'value': 'Ȓ}ȼѣͽùˮӻ˙ɜȾϔ˼T\x80\x84ԍԀȇӽΘǙΫҽƫEsϒÐŒ',
                                                    },
                                        {
                                                        'key': 'ɄįƗəѾ˛ЫćʨȎҺƛų',
                                                        'value': 'q¥ͲЭϬҽȦŌɲɤÞ\u0382χȧΡǒõʯŨ«кazϋɔŃƆ\x84¹Ɲ',
                                                    },
                                        {
                                                        'key': '҄μѢ\x96¼Ҥ\x98Ɋb',
                                                        'value': 'þiƖeɤҋĸϞӱԟ\x99íʞWԖĐѼÚĵƷ\u038bϟƨ¢íèκ®ԑϬ',
                                                    },
                                    ],
                        },
                    'comment': 'ԑԠˆŨÍřȐĞģåɑϮǦΕҰ\xad˝ˍƎ˨\xa0ԮǄɵǌӏđө˩ǂ',
                },
                {
                    'keys': [
                            'ϸӁ¾ΈєŴ˻ûǶ\x85ɏŃ ūŜ',
                            'ǥʂ',
                            'ÌȫȷϴЫȟӮ˪ӗзԠɤıʅҎɃʯ˷ɱƠ˜ԓԉͱĲ',
                            '\xadҲ½ǗƧǵ\x8eоύÇɋȲЃάǄШӃ¶Ԕǁ}ЗʏŲUǀ',
                            'ҲȺqѯӦ',
                            'ϸʤ˔ÝJ',
                            'ȂθÃůҁƅÒɳрҭʧǭȪӘӹ¦ˠ6еДѯΤǗǥ',
                            'ɒĿΟͻјӃңȶˤԕľ\x9aӵ¥Ԧϻˢð',
                            'Î˱Ψʊ@˴щҢĻ!οжʸЗͻжń',
                            'ћԫĞƆˣҝŐƖĝ\x93ҜŌѝ¸Į',
                        ],
                    'event': {
                            'target_id': 'ǞӞȶӢӐəŉґ҈ɩċ\xadǠɿʏɴʧʻҞҪŖϱРșʤӕ\x9c˳bЌ',
                            'parameters': [
                                        {
                                                        'key': 'ûϲǽ\x81±ѨȬ\u038b˟ƞǭʬídɸƫâҐvЇɵыΘhΘ\x92#Ɨјϝ',
                                                        'value': 'ńѢϜ¨ŞǧíȫҟÂʔӇġĉΌȰď˰ƱǠȬßǷąʣѰӟƁԟġ',
                                                    },
                                        {
                                                        'key': 'ϗǕԃSϙǦӮ˺ЁӏαЯ=a?ÒňĉΉπ˩ѼЖbχϾ\x99Ӎȃα',
                                                        'value': 'ːϩѨαū\\Лƪ\x96ǯ]˛Ó:ɅtʵŲύȭŪ҈Ƴưē·ӠѾǽ#',
                                                    },
                                        {
                                                        'key': 'ʡˢ˸ώҭː\x84ԢͱЪá\x8cƆɼŦʑʧÃҀʬ¦ɝȣōʕӋԭʄХ˝',
                                                        'value': 'Є\u0378ǔĚʋҌӲө˯ҁª˂ѣϢV£:ƽŋϺͰǭßϩџʎϕЯ,Ž',
                                                    },
                                        {
                                                        'key': 'ϢŧЌзŕˇıͻЅìÉĒğǬmѩӳȗ=ήȉҝĪӖϬfӅȔ˭Ԟ',
                                                        'value': 'Ѐ҆ˬÇ˻Ħɖӝˆĩçą˲ĥȽİԂԙӢļ\xadèȪѯƇʐϨνҞʩ',
                                                    },
                                        {
                                                        'key': 'ЦЫ+ҭЍЇ¸ɕȒƧϖkàJ;ɏӏҶƲ¾ЗƉ=ğþŶxɿƷ¶',
                                                        'value': 'ȤƄ\x8fCģǊʽҒŌɬɧҷʤӁӁƄǵϹɻЗƎIʕΊƱˋπǷЦΐ',
                                                    },
                                        {
                                                        'key': 'с',
                                                        'value': '0ԜґɥŠϺ2YϩŜɘӠƩǼϢō¯\u03a2ňӼþĜÒēЯʤљʒųԊ',
                                                    },
                                        {
                                                        'key': "˻ě.đЎ҆dˋ\u0378ǹdJľSЦ¼Өӿҽ@ʙ˵ѧǺÝĜ'ϜĒ\x91",
                                                        'value': 'н˯ҀĲϘ$Ƕȏд\x8cŜǄʑʕïë˃εωҊǯÌԨü˳ȉ˵˔˖ʼ',
                                                    },
                                        {
                                                        'key': 'ӾӾ½mƯˇϲϙϽ[Ä4χȻҸӓˉΨёé?ʯōƔ\x8aǮƭƬɷ',
                                                        'value': 'nԖԊǺ©ĥĦѡƨϑʆ³ǒÏҕșĖѪƄϔʕˮ\x99ΟͳԤϕʡЗǤ',
                                                    },
                                        {
                                                        'key': 'ϘӥY҅ӛEнȰāƤƻЀϨ',
                                                        'value': '¨ӀÐZǏ~ǁԃäOϸɔ',
                                                    },
                                        {
                                                        'key': '\x96ǖϴŠԫҞƄӁɃ˟тѻӥ<ƣԝŲɕ˴ȘǷʵ©ɔ\u0381\x8aÑĹ,.',
                                                        'value': 'џԧyƧϑЦǀěӮѵԔêgтƓ-ІƟÐ¤ңɏƠ4JŨ˩ηŕʱ',
                                                    },
                                    ],
                        },
                    'comment': 'JƶɬʢѾӤȪ҈ѻΧƺŃǿXtşӠĠƃƀǔƋ˩kǶӜԉɽe˛',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'master_sequence': [
                'Ŵ',
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
            'name': 'ɇϤӰ˔ķѤҿ½ŞœΊżéҙȀŖǗƴʏӸǈ˪ДͿńІχԌƴʍ',
            'description': 'Ͽѓϫ]ʡӜſ˰ǖƯıdʷ\xa0\x97 ӃȿяɖЕлПǒǁΜ˷\x92ɶҪ',
            'target_id': 'φžԮŮȉ\x88\x8aҵàԚ҈тӼ#UΧ\x82ϛҕЅ˅CȾʠԢːГŰĵў',
            'parameters': [
                {
                    'key': 'Űѵɴʎ°ơWҮƳӜ\u03a2ɭƶ',
                    'description': 'ƴϖĘӳ˽ϚиʰЖpAϵӂ·ϛʿʁęѫϭ×ǤΤƱ¾ʈӁјӛĆ',
                    'default_value': 'ɑɛØ_\x85ԠЕmoħǕrƜΑѝҲ\x9ex͵КȑĎƤȘԬыφЫзŷ',
                },
                {
                    'key': '¼ӎʓ\x82ӤЈӡÿԖύјїɾю',
                    'description': 'ϋǯΰЊŹщӂŠ;ɷ˪σȪɆ˃ÊДė\x80ϞȐҀ˶ϝϤnƇӐńѥ',
                    'default_value': '\xa0ɳнө8Қԍԑɠԁүԙ˽ӱ˔ЉŇϨǐʌņɸƵȚ\x80Ԣǚѱɒȯ',
                },
                {
                    'key': 'Ϝ$Ƙ¶\x8eʚΠɻȅˍQĵ¾vӽϹKƃҴƙԏǷǗĮˣɈʞЁÅ\x86',
                    'description': 'ŬϷȌǥΉч˨Ȓ¿ĘɠΆҔçʄȝɩÙЭҝŒƉє5˨ҏƵҨɋԚ',
                    'default_value': 'Ә˽ԃΩǄ\u0383ΓμʙĢϤ\x89\x97|.хħɲԒɕИʱtҕԭϠԂˢӤσ',
                },
                {
                    'key': 'ʇпʭзш',
                    'description': 'ǾȈԚoшӜ>Đ`Þ/ɇhґͰԂk˯ӸΪԠЗˎɩЄѺšȺθԂ',
                    'default_value': 'ģԆАEϚӚͷőҠ˺Óͻ/¾Ť}ƶΗB|˕ɨǓӌϏҗÕʆ\x8eɷ',
                },
                {
                    'key': 'ȋ^ˍѦĵüþ˶ѲƊ˳ӅΧдģУíҥԠ&·ɘҌ#ˡȉԎ¬ɚҦ',
                    'description': 'τƙїÿѿʴVӷΝĤ×ȫǎèќ±ЈҌȰ\u03a2ǒȏӟΦϤҲӔ-˟Ό',
                    'default_value': '}ǌxΩĬҙHLѓPƳƹƐ7ΊrґǷҗư\x883ʗ\x95ƇѐѳċʕЎ',
                },
                {
                    'key': 'Ǔ˾˰ɦoȳҐΦЧ',
                    'description': 'ѐ҃Ӊg˜ʢƙƂưѡԜŶʣOQ˚ȥϺӨ\x7fÝ\xa0ōʐЪІƄхFΡ',
                    'default_value': 'αǸǍYӌӮΈЀӂɣː\x92ͽτ*ҨɝҳҪ\x81ȓƈґĝŉǚİǬsͰ',
                },
                {
                    'key': 'ʆs˗ŜƦъӘËkǜҔʉlĈɀκǘҐ҈Ǭ΄СǪʍüġşʛϜԐ',
                    'description': 'ǹҺҷɩuˢíX¸ѱƝƞͲ£ĜɅςȢʿćԦ©ʫʌЬɔσaɤ;',
                    'default_value': '«ϕӆǊöΔʨѡҎʑҡЎƼĚ6ƀ\x8dʗϋcϩƮ8ˤˉˑϗƬʦÒ',
                },
                {
                    'key': 'ǅʿ\x7fŏƺԥĨʭVӌǘǺѤȂӖNɂϾҨƶ',
                    'description': 'ʑԙΖҘϻˬÕӓҡàЯϵӫҸøĥɝɧΙЃϾ/ӿΘїТϡƯ²Ƴ',
                    'default_value': 'žǼ®˘ɏϒǴċ|ɂʢˮʅÞɺǷώο¬γÂìɡȆΣ\x89ĈśӒƷ',
                },
                {
                    'key': 'пȚčԍĽҹʝē\x92ϧѡȯŶԜǊƆœǯǚŚѤϥĳʨʲBɌƓԠˠ',
                    'description': 'ƏӁŒӦ\x7fϚǍƩҜƆϲƼɒ\x8dl/ōÜҩɥЂȣ˲Ƥ\x9fҒӝğ\x9eɳ',
                    'default_value': 'ϑÇʊCˍЅǋҍɎ×ˈƛːyn_ԠԤ˩ʽóǏӂӶɌѽ\x90ȴТӇ',
                },
                {
                    'key': 'źʿϡ,ӭĦƯɄȻuȂ_ȬʝƫϭӤǞУŕңʁΏɍǘǲ>ĈͲ\x8d',
                    'description': 'ū\x8fλǹŢӟӹǏǓΆʹƖțѳӾɰĻʩщЬхӲ©đńƿΟˣăє',
                    'default_value': '>Kћҍƿ²\x89ËǳɊΓøәɔӁŅɔĨ\u038dƵǆȃБőéwUÈxԏ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ϕӃ˓',

            'target_id': 'ʙйȇáō',

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
                    'name': 'ҪɎŷʔͰԩ*ο´ʄψƟð[Ũѹǿ¿ėϙ\x82ņ¾ͱԓȒӍҠʯŔ',
                    'description': 'ϗϯɡλ\x9eƳʨ@ƬɻɵԁʊӑǷʋȸɆʊʶ\u038d;΄ÔѧƓū\u0383ƻˇ',
                    'target_id': 'Ӹϓѐêһɩ¡Ļˎԋ5ǹˌЉɁ/ӢÔɍκΝ¶Ơ\x80ŉΨ´ԊΘͻ',
                    'parameters': [
                            {
                                        'key': 'ђѿ˃ȌԝťɵҢó\x9d;рѓѿ',
                                        'description': 'ʼҮ\xa0żҜmDƄȄtщԌϬЧ˰MáӠяƅǣƙȦλǪԀʳǯßӶ',
                                        'default_value': 'ѫũ΄ҒŧϺȼȳǊсӻ2ȶϓčƬ\u03a2\u038dĮ\x93ȇĢԕ!ɈʕЮ\x99P˝',
                                    },
                            {
                                        'key': 'ѝēǐʭmT',
                                        'description': 'ƩżϋZÎNƫӨԭ͵Ԉĺșˆ·čσҟɂİĉΕàλЌӺѺˬȮ`',
                                        'default_value': 'ͶɣưԅƄĻԗĄƞʋАҎ˴ʤGʶˬΌǋȏɨШ˒ɗ΄ɘɈȚɱ*',
                                    },
                            {
                                        'key': 'ǖɔȽʘ\x90ӀґǉˑƿȊQɷɮ$кŹуƛ#ҴǭьρËŻӍ0ʰΥ',
                                        'description': 'İ¥Ƕə˯˩ɳɔшѵɝ\x9cŰӧԩ%ʁĲ˙ɎϫȦάϺӺю˺сŭʒ',
                                        'default_value': 'ϴЁӄLâҴҳËͳѾǤǔѤϽƱʓʸԆ¬ɀȰɂƘӺâѾŲł ˭',
                                    },
                            {
                                        'key': 'ӖӀҡóʇȮȭȭřƧӤÎ\x89ǺЃâÇɷˎưĔӍ˧ЏƋǔň¿Ǆp',
                                        'description': ',ЖӴԢǙȭҝњʳăˊǥ+ƓΘӪҡПǇaИѡ˭ҠȐӽƨӟͳʥ',
                                        'default_value': '¶ϛďŉǋӾĂźˁʨʥһȤԩ-дʤԊƀҮ\u0382Į\x87ѽʐѥˋӥӞƭ',
                                    },
                            {
                                        'key': '=ӳùѢÞ˞ѦǕʜ9жĶŦWǚÃɶЦʧҹĹȵυǱƉХɿǧșӪ',
                                        'description': 'κ˙ćғΉțʜȝʋ»ϐн\x9eǵԁқРªќɭtEƫԮˆҜG+ʥȾ',
                                        'default_value': 'Ԥˬ)ɇЉìɪϞȬ8ќΧǌЮʩӃӔ¶ϖΠҧͿώ ƮĕɄҋ\u0380ȏ',
                                    },
                            {
                                        'key': 'ŻĈɞё)ţƾĥlвƂǛϪ°˥ίDξϭþ´ćǩeςҫϟʬ˪Έ',
                                        'description': 'ˊҰǭͷ\x7fʐѦʚҋǻȥŶů#ωӷѓ˦ԧǠ&ńǀЛʀĆ˶ŗǞÚ',
                                        'default_value': 'ǠƤʝӛƈΈќǓďϹȓԘɷˊԊΏąʳƉМƆӺͳϷĂІ҄ȝǰʲ',
                                    },
                            {
                                        'key': 'ƍʵǎĉƱΒϟ',
                                        'description': '˶ҐʩөÇʀǪϮӣǻԡӪȮǏ¶ȿ ҩƔͼËѨƇϐŢϗƞƂƼƨ',
                                        'default_value': 'ʸȵr·ƭΙȅĐϺɲ]ԩÊ˽СуÿҸĖɥǄҮÞϑéД˽ЈǢӻ',
                                    },
                            {
                                        'key': 'ϪÔРʔɂ\x97҃ӫdϝʰӇΚĽʕͺɵȃҊĪЋѥͻ\x8c¿ˠƯǊĴŸ',
                                        'description': "ʿhЈkΓťҼʻΔtŏǯɷIυΏʹ'¢ѱϝÊĳäӦ\x7faαљã",
                                        'default_value': 'Ҍ˫ǚҼś˴oӔҴǜʏРӋ7IӴӐǸҒȤ\x7fϜɸņνĘΕ\x98ɓĿ',
                                    },
                            {
                                        'key': 'ԣԟΫ\x7fğʣӺχŭɦ˺ȤʰЄ',
                                        'description': '΅ýЙИӴԩ9˙\x8aϺFóʟ«ħΏԏřѱƚɘÒͶǿ\x9bɭӷϟ\x8b¢',
                                        'default_value': "Ȱ'ϢϮȖ~ѨȄΘQƸ˦σG\u03a2ҳǓÊɲ\x9a˻ǒȑЮǱҸ˱ЇЅȼ",
                                    },
                            {
                                        'key': "ҒƬĐ'Àʄɇýƣǝî˕Ҟ½˃ħ˯b¸Ȍͳŕ/ЉǕЀҲ\x89Ɯҕ",
                                        'description': 'ƊӰΚ\\ƷưҭЈҡКѲȼЄÍƘ\\ɴӻӶmĝћԠѱƂҢƑӓЙѯ',
                                        'default_value': 'ƟʃҊb҉kȀşȼǨȨȩͿYϱƘҿп˹І¯`z˶ÅҀΠȃÍʩ',
                                    },
                        ],
                },
                {
                    'name': '¢ŇɆϻѹʦӫĊ§Ԯʒɍ9Ҫ',
                    'description': 'ԚΘȑДɦΓō,ȵ˦в#Ǘӯ˹;ԆҥԌȹɂbÉǬǞ˾уȸԎȕ',
                    'target_id': '^ˍӻŷϫЮãҗǙŽԓȮ-ȓŢ˔ǹϋЭƄҰʹɨЀÚԅɷц˙ȳ',
                    'parameters': [
                            {
                                        'key': 'ЙЗȚtɂѰνȖԥ΄ΤďʭєҕΈ×\u0381ǐôɈʻ.ȗѝӱ',
                                        'description': 'ε¼κЪƢʿ\x94ĳΞéЃҏǜѸÀĺҧ\x9c˺Ȣ8ϭ\x83ɮӄирʭжɓ',
                                        'default_value': 'ǘwӁϔɝԂƒΖ}ǡÂêѸfŁϟÕĶŮ˓ĊɱɞΘӱoəɵӋʲ',
                                    },
                            {
                                        'key': '»ǭЫńǱđȁƉäљϦ˞ʠԧt³ϢԌϾƌƥœҚÝưŷņȲӘě',
                                        'description': 'ЫʚŸǦǵҷºǾĔ¯˫ɱщYĉ\x99ӽÚ\x86ԔĴʽ·э\x92Ƅΰΰǯå',
                                        'default_value': 'ЈԧϸĐāҾȪ˭C\x83Įј¨αȦh\x9a¹μѾ˒½ҥˀԏԅ˶ȫá×',
                                    },
                            {
                                        'key': 'ȠƗɕɍ\x86ӕВϙьҠӣ\x90\x97ɀɈԐзҌȳ˸ҭʰϛǹӖЯϝơ˞ԏ',
                                        'description': 'ҔóėĻю}ѫΚʸ¶ʤӂʰǰΑӐѫλӜϧƩǆƆľǯЂӂƏȱǗ',
                                        'default_value': 'ɜǧƺιú˺oѯƲӦ ёǘėʃϼ˨ԑӮӬԅËɠǪƽĉgÚŬĘ',
                                    },
                            {
                                        'key': 'ӀэͲӀͿЛĳɰяˆҨǺďƏΠ&ʬ`ʉѨϫĄӎ0ҍОǠÁįӖ',
                                        'description': 'ΉɓȩҕĂϚ:ʨӔԌƬ\x97вĺԬϨҬɸҁЙźΒɓҰɀШĔԝϵƗ',
                                        'default_value': 'ȩҠ\x90,¼ΐԘȺ˔ǛəŁͳɝԁēǝӓЦ%ŤȂ>ǭǧҁ҉ǴΕγ',
                                    },
                            {
                                        'key': 'éԛÓɗɩFȖĥǹϮӾȈ',
                                        'description': 'Ņ˼ΛÖЛуɝśȅӀ3Ěˣ°ԆҠӨʶȍǴȅϐΎϷĳϕɬГğϑ',
                                        'default_value': 'ĹŜԒǑɅ',
                                    },
                            {
                                        'key': '\u0379jďƎȊϹȦǮȱϹΥӊ¦ƯԭΨÑƭÄҎ҇ɣ\x9b)ƥƍѴԔɨϰ',
                                        'description': '\x92р\x98φεǽEΆƭҡяŉȗ\x8fĦ˺¢ƨ˦ѻӌʽΑҔÂɶ3ǵȎѿ',
                                        'default_value': 'ȐȣϾ®ɐČ]ĞӍȣɘТʇľԍƽωʙѳӞςǸͿӅìЍȫɄ҃σ',
                                    },
                            {
                                        'key': 'ĚϨΦӣҘęɭ+˽ҺɠѵіhɳĠыӖǉƴ¾Ҿϋ˒ˢϜø\x97ˈϩ',
                                        'description': 'ɎȆ3-Û(ǍʡǈȲϩƕƎһΚƛҫ>åʺǦȖҖlȌÎxӷʫɔ',
                                        'default_value': 'ͼύǄȜҒцœäǫмaќњΝƙɣӍÊˠƗɢǠʜϊ˝ЖХĥЮƚ',
                                    },
                            {
                                        'key': 'ǊǳΗǿTĭȯȲȟȋ\x96ҘıӻŪˡΎ',
                                        'description': 'mɬ3ǵȠХźǲΌ\x97Ȧ×\x8bӛ˴˗ùÌɊſȗǗ\x92ÍлƧэǬFũ',
                                        'default_value': 'Ȅɥɉӗţ\u0380ȇіŔѐŚ˭ΎŵͽˬǬŭυƢ˂ÌѡƑґǾХZƈӴ',
                                    },
                            {
                                        'key': 'њƈǾ½sɿφe',
                                        'description': 'СŪ҆ééԘΪŇȤʞÊӐΣÂĊѕʹιƁŅσЎɍÄƌƖĖӱf¹',
                                        'default_value': 'ǔΉșFĒҦϏπϟŤΥ@ĳŠ˒=ȍªϸʃǗ϶ѪԡťϒΝɷkĬ',
                                    },
                            {
                                        'key': 'Vԥ҄șёαы\x9f\x9cĄ˱˶дċ)ъӈАΓ˄Ϙ¦үňÙƗőӃҚƹ',
                                        'description': 'ʚǒǀÒ!ґɨˉѬ\u0379эӁ˥ѴĈˀƶϷԘԋ`¬|Ǻӡ\x85ǓȭŃþ',
                                        'default_value': 'ӔЮѺǱШǾQˑԫʴ˫ȍ4ƚęɰŧϥмʱ7ӡ˛<ʔ˝ϏƐƀȁ',
                                    },
                        ],
                },
                {
                    'name': 'ȹϿԒƃŬÀќ˦ѻŲϴđӏɆÉƚаɗѻīɮɍ˴˦ʖ?ѯmŖҬ',
                    'description': 'ϑŋAǿȯΓʠò±ӎŁЌԣǼ҇\x8eŃ´ËE`ʩԬÆ˵ǦμʘƿҔ',
                    'target_id': 'ǹϣ\x8eʦpʟʷZʄμÅЩҠɾхjήÐϧpƞʚ9Ήҗȵ\x93ϝĜ˒',
                    'parameters': [
                            {
                                        'key': "ԟŰũѰχϊ/'żњλǸëv˲ҘƏ#ʣίşҾXʄӦkšǁĳκ",
                                        'description': 'ƜţϫŐΩġѝɷĨÔʕɽϼәJɁƠ˯ϸǫαɭӆǫҞÜȮǣЖĿ',
                                        'default_value': 'ϟͻģċΪƓêʂíƑпʍ\x83ċİďҟ\u0378ң¾ɏƙθ/ ϦǽԤțА',
                                    },
                            {
                                        'key': ';ȄɅӥǥɬɓχ˫hӠϐѹ/¢ӘԗlӡƷɢӷEх',
                                        'description': 'ȖҘϞΚſ´˄җԧ\x8aƭ˪čȄɅμ±Ғ˰ĒxƨćӇΓЗưΤ\x93Ӟ',
                                        'default_value': 'βјãӵ=ʷɾ\x92ɋњɜ?ҜΛԙŤZѐԝ˧ʁɾƼÇɮүΞȷӯɭ',
                                    },
                            {
                                        'key': '^Ϙӈ\u0382ԘǷа/ǸБȆɶʵˋиȈх#ίˠ',
                                        'description': 'ʭȯŕʈгS˒¡ӷʚЬɤ¾ЋÊʶ\x92ƪÖϛƨiƧΙʊĈӌȺËԔ',
                                        'default_value': 'ʚīνɼàȬӏ5Ζϧë\x8cԂŗßȟoӸРɦɥȰǦϵƞҏʴœ£ű',
                                    },
                            {
                                        'key': 'ϲґřŵґȧǕӆʸÄϻ+ԏӀӪЖȵfiӮɞçжӿϰбðΞӦԦ',
                                        'description': 'sɌ˥ǧÉΒσďǔԖɋ\xa0şŊĊϜGҿѴţÛ\x93¹\u0378ƫӑƔ\x9bωӝ',
                                        'default_value': 'ʔˍħ2ϒúӡͲȡˎďμȕϼʁȝŁŦӸŎІ˽СґťȲ˧Ȗďá',
                                    },
                            {
                                        'key': 'łϗђȔ',
                                        'description': '˝Əɠδ˯.$ɣƼɥнʇōǎ˘\x85ɍФͲËǊɓǔүПɋΑĚΝҴ',
                                        'default_value': 'ʌϯԇлͿaʤƋMƊŚƑԖ:ԣȊѺϑηʚŋȥОƊбΣĬˍ\x9fÿ',
                                    },
                            {
                                        'key': '+ϥútăĖИ×āǐњСʺдĺɁϿj˭%ʵUƵΦĶӫҷ|ǘʐ',
                                        'description': 'ʎԆȨӏĔʶӶӹʉŪʈѧƙȇżǍΞĊԨÎ?ŉϩˢ˨ĜӟӦϰɜ',
                                        'default_value': '3Ԛ˂Ӿӥ\x87ņʰñȅҪΛýxԈ¼Ӗ\x9fαɛҗF=ԮʴúȗϤ\x88Ҡ',
                                    },
                            {
                                        'key': '¢D}ƣɼǯʃѱƢĒƾɻʽ϶Ŵо\x9bȋΟЖCŴ҃νɋ҂ѢǨȅơ',
                                        'description': 'ƨȷή\x9dЙɲʃpяԑȴҀĥѠŔ˨ĠВňѳ\u0378ȸΞóìѬѿ˅MȖ',
                                        'default_value': 'Ǆƴ˭ҸήǆϛƉɕ%Ϣȟɡԋѹ½ïɭʒǩ҈ɋo΅ϴЈǶԡǆʛ',
                                    },
                            {
                                        'key': 'ϑɾɳȂˤώΨӎ÷ƄɲFȔȴ~кɬŶɞ˧ѵɬ×ǣ͵ʾɴҞ\x86ž',
                                        'description': 'ɽȋτͿ¿ЬԕȦ«ˈøɁĔҏɳяAͿ¸½ƔĿȡ˞ȐхрңЋ҆',
                                        'default_value': 'ņέˠ˴ӔH\x91ҩȟjӘ¤ŻzԥŔű\x82ңѼʦʸ/ƜӛĄđžЕά',
                                    },
                            {
                                        'key': 'ʔцŷ',
                                        'description': 'ƟǓ£{ȩЯÝ˜ı§цѼǂǾƦБЏÕԊȻàϦɵѭΈŘƜĞÕʆ',
                                        'default_value': '˯ӥҨ·ȤӒɓʘΤǒfӡҫźѤǜ»ӆˊÀª˟˃ԟͱʊΛØҏį',
                                    },
                            {
                                        'key': 'ɆԦϰǰпФВԨԭӰɂϬʟ\x95ԂРѣȬЇƖĺҴɕҘŵƿԡϻǦȖ',
                                        'description': 'śǫrČƽŀ,ӪÇԤϝ҂ΔǑȗǖļͺЛĲʁȶӔeӣ\x8eʙˣ˓Ӡ',
                                        'default_value': 'ΫŌʝфƤâϹΎΥˠӻљţē¤ȱ<ʊơϰнѻҋǱЂ\x95ӻĘ/ě',
                                    },
                        ],
                },
                {
                    'name': "˄ӾA˧Č\x93Τ,țʐÚʎϰġԍqҠ˫Éʆҍũ˸ɂΫ'ί#ƁӶ",
                    'description': 'ѝȵŀ\x99ʼΚҙƯЊϚϲЫφĖτ\x8eϺκԗţe˒ÎɦсǄȲɫbѠ',
                    'target_id': 'ɸϲѰγҴʛҁʜҡřϮӱæʿѳƴԉ\x7fУτƔçȍѺЖʜґjʶʾ',
                    'parameters': [
                            {
                                        'key': 'Ʃδē\x8bӿ',
                                        'description': 'ĪǦɈ˹ƆЂƅРЯЍƧƹK{ϏҎӐјȾɓǱÁƷԝ·Ψ&pȳȤ',
                                        'default_value': 'ӷԞϰЪѦЄȒɫē\u0383ЖǦч˳ȘϞЖǘrή҃лɦĠǰԇѸƒ;¡',
                                    },
                            {
                                        'key': 'ˢԩѥ˘ÏԞι½Ρӂˢʉÿ\x81\x8aɶĵΧlǒΆ\x90ϪӯʹЧʡΧʌϴ',
                                        'description': 'ê˻ǘϒľΝΧϴΥȱΖʌʤȃưӈϲVǻƟѳŌ¹Ншʞ6ĨОư',
                                        'default_value': 'ӨĊ\x92oј\x9fҫȩĀíŨƵԓȑ҇ȱӤkkҜĲл\u03a2ĸҼԨ\x85èɯΫ',
                                    },
                            {
                                        'key': 'ɨӠŉѲͻŧґƻɎø·οĬʒÚвŽnԌɅϦԛӍɈŘgїӫzɝ',
                                        'description': 'ɤԉёɣ˛ſщÛӏЌӠ#\u03a2Ԇ\x9cϰ9ȯҙǐ˼ʻƱ˂ǥИȢҙΗɐ',
                                        'default_value': 'пˆѱɸ˽ŮԇѿˇŻԞ\x89.ųϵДĽĐйǫ<˃у\x9fɻʩˢɤǉˑ',
                                    },
                            {
                                        'key': 'ҸʋʗпEӘƔҨȆŌƈ\x86ӝȞwʀ˳ąԢӆËӜ\x92Ӭũ˗˱МрƜ',
                                        'description': 'ОĥѾƇӍЬǯӄȟX«ƝBώȝƀ¿ùАıʯɏƦҀгŹӝƞTɅ',
                                        'default_value': 'Ŀǯōłɦϔʒ\x8bлЂ-\x8fʥѥ#ʶϚҧқƯΪϵ\u0382ƂӃƢÝdѾм',
                                    },
                            {
                                        'key': '͵҆ŁϵÔǗɱņ˪уǓІƓǠ\u0378ˈԚƛԆʘ¶ѼͳϓѼ4ӉΖϠ\x93',
                                        'description': 'ĦЧьʇԬyӢ>ϚϩʪӰώєǧCǜ*˥Ɛ˓ʨíӷĤӥȯƸϗӞ',
                                        'default_value': 'ƪН˟ŒΟLʌ´Ψ¢ЧӔǷȺΞëʘŀϊАkѾЧªǬʴÏњ{Ɲ',
                                    },
                            {
                                        'key': 'OɭɗˏҺӢнϛ˱=ĿϱǦöӰлӢƍδQƦΔÊīǒɰČʞĞҚ',
                                        'description': 'ΤҰƙƍ˻ɆѺʪϽɼԩϵŔʝ·¸ɒŶкԚɤΗ\x90ȽÊүĳQȪP',
                                        'default_value': '˫λїэЂȹ\x8dɅÃƍјɻ˗ҞԝВϯԡęҏţʹǳŴǚÝƬè҉ϊ',
                                    },
                            {
                                        'key': 'ΚKyĹӂϒӞŝӪύåЏĢӳɑ',
                                        'description': 'Ȑȩͽ]ʐʙ\x8dǿȤŴʑԁԑéͿѹΛɅҙЏӌҌ\x80ѧȝȅϝʖҀɸ',
                                        'default_value': 'ĊɱƆҸϴӛ!ňƇȊMƏ$ӪσЍáȩ˵ī§Ѥı¸Ϲ\x9c˘ȻˊѨ',
                                    },
                            {
                                        'key': 'Ͽʂԥ\x94ЩÎԥʋ',
                                        'description': 'ӳțƘϱ˒,ѕΪ\x9dӣɻȋĖ~ԜҖΔÿǃ*ԮƃϏӘǂԤʵЄМɟ',
                                        'default_value': "ЫǥÍҽ©Ѕρ'ãëęŽƛęύˈƀǛƈùǏƧ҆ʎƴʏӅѱ\x90Ċ",
                                    },
                            {
                                        'key': 'ʻļǩȅЗԩĶĦšѩԪӒȡϳˋƓĜӿLɠɢə¶ǿÞыВʾȮӱ',
                                        'description': 'vƆOªԫ˧ƔƇĲɧ£ҼƒӚşčͿҿĦǨσʈʎċãͿЅȨӂҬ',
                                        'default_value': 'ʚŞ\x7f©ʦϫΛƖŗÑțѥCǑѣĎ&ȓȐĶőКԄĔɑƅȼҰҲÁ',
                                    },
                            {
                                        'key': 'ѕѠЌo˗ыөĭˢѷ',
                                        'description': 'ϋϤ\x80ʠяƋџүϔȽɳҿԍȈȋӉИŸɂɟ#\x94ǌƉѱҵҌ\x8bХʣ',
                                        'default_value': '½λЅȜźSƚ\x87ƐÔΏǔɖɻр+ʎ\x83ʬǐ^řϏʞ˯£ŤȔʀ|',
                                    },
                        ],
                },
                {
                    'name': 'ҽӰϟRȥыȶБ^ʮшĉǵÚhĢ_үӆϿ6ƍŢÄΡŋȇҀаѿ',
                    'description': 'BǁԡƄΖ\x9cGϭ¿ņÉѫ¤Φ҄ΆɈњМÃǤáˮѯβĴŒÓчŗ',
                    'target_id': 'ƙ˕ũ˝ЦPͰŇĴ\u0383єɐ\x85ҽӂԬ҄ѵͻXӀɰàԏǘЌTοЎ6',
                    'parameters': [
                            {
                                        'key': '$ʥƹŽȵțƈӕӯˢь9\x9d˕\x8bͳ¿ÚІԚ¾ή_ʆͿˬŻĺǄӞ',
                                        'description': 'Ɗ§τμq[ƄԜĭҦȍțКΦҹųθƈЂq2Ӈ˃˽Ѝůqӓʜћ',
                                        'default_value': 'ӗѲ¦ӖƛϯʸʆǮϜÊ˝ʺȯҩѯ\x99ԡéđƸǇп\u0378ʧȵȭӾίȻ',
                                    },
                            {
                                        'key': 'ĽƓUƷ×ѮƢӦǒǻ˭ҊĬąфȻ|&ĴŖј¯МʤӍȷЛʡʝ ',
                                        'description': 'ԠÞʹΩ˘ʐÚӕƓμɂőʢѹ˃ҶƧ\x92ЩϾʶƄϭӠЫԟëŋ¸£',
                                        'default_value': 'ʽѩӭξ|\x91Òŋɞԉ҆ĜԢωŭ',
                                    },
                            {
                                        'key': '³ӸãϷ¢Çƒčȴ҈ĳѱӝѹϖ',
                                        'description': 'ǥβ·ҭӎ\x84Ϝ½ƻѫɊтȄԞʫήζʧKЙª˲ĻàԔҼ,ǬȽı',
                                        'default_value': 'ĳιƃқ×Ţίʦ˸К\x7f]eɅɔhɖХȃ\x95ƵϫʬȼθɖˢųѺĚ',
                                    },
                            {
                                        'key': 'ΥҾ³ͶӉàОЮİˑͰΰσνшɱƠuбÛƤȩŰǣĴ͵ʜȒԭȀ',
                                        'description': 'ӡ\x94ʓƟ\xadȏ˯ɌʄɢЁʕʗΰЭ\x81˘ȐǊӴΎ˖uÏŜҥɉԭeÔ',
                                        'default_value': '·Юӳ.ѴˢƽűžСǏԍƉΝѤ°ŪӱЕɲ;Òɓďɋҏԓɘԡȵ',
                                    },
                            {
                                        'key': 'ϫѺҁĩ˝ҢŲОů҉ϑϧ°΄ˣǳ˺',
                                        'description': 'Þèųьͽ6\xadÉóηԗƒӓXå\x91\x97ȕ˃ɷɛéǼǊҀϩÆӵυC',
                                        'default_value': 'ÒéȮӛĐ\x9bʦ˚ƹƠϱӇҲǈϝɫȧľþ˯ƂҎʾưͶƪA˘ǎ\x86',
                                    },
                            {
                                        'key': 'Ħϳҍǒ¬G<ʩÐ˄Ϡǭӡˏ^ϹжѲʥȝƺéњȵɤȯԊӳͻĝ',
                                        'description': 'Йɘʅ͵ĨŐϜǄˁ˔ʁǦЯңţʌюѷ\x92ԞеƖç7ǭђ҄[ɭԎ',
                                        'default_value': 'ҀșшȋəõīÑϪɩ§ȃƧԊʘ˨ԎFЅӻʗOłƛƨӌʰԂ-о',
                                    },
                            {
                                        'key': 'ŽǦѽ˲čĊҶ¾ΞӿѐǧőήʚɫҀħʕԍϚɷȓԢӰļ*Yvɢ',
                                        'description': 'ӮёщΖǕ҆ʄτːűϮψĸм¥ʅͼœѡӗ;Ԉʻ\x9dÇǪƐâөԊ',
                                        'default_value': ')ӖӛJĿǆ˨ЖƦˊƨԑŎͳɡ`ʭˠ\x9e\u0380ʨ\x93ǺˮȽvǇzjū',
                                    },
                            {
                                        'key': 'âѳӑǇҾȄ_ʿ҅ʻÀ3ɆȨǅҸĺ\x82ɃƴC˴ѓ',
                                        'description': 'ȁƥƘɃƅž%ƺȟӮԅĶŜӤĄʼмnɮϱΰǎʿϫɾғʎ˪ʏƋ',
                                        'default_value': 'ąʦƈΐΐϮ\x85ӹƧʐ Ѱ˄ʝ¥ӽżǐÿƷШєʄԎɽƣêʹ˂Ԉ',
                                    },
                            {
                                        'key': 'ǏȎʂӼūѯ˸ʱȣ±Άԭьċҝοϋ\x84ў©ˀ͵ȆóǔΫcʞТƞ',
                                        'description': 'ҴԔкqϻÌ\x8fȖĻ϶ĄԣďӇȍбƤѷ˯ӛǕǎԟхYҼȘǃΙÂ',
                                        'default_value': 'ЬȷʪϣьЀZӻ˙CǁǬ\x95ŌӥӭΚ˄Ķɧû(ª^ƊчуϳƟq',
                                    },
                            {
                                        'key': 'ǃƲн\xad˯ɩćδ˷ǺУȡǙ³ɋѧϑvԮ¹ϟȽŎɤǋϝȬ|Ɏй',
                                        'description': 'ƬOgΑŕЁ»Ȱǲʆȋ/ßǚӮдƕʬ,{ҀĈѦҍ҆ǅѩ\u03a2ŘȦ',
                                        'default_value': 'ΛǄІNϑÛğԛɒʯҖŪѷͽŬлҧҢƟď\x87ŖӷřЍѸłĦġǰ',
                                    },
                        ],
                },
                {
                    'name': 'ӼəńʀĐɬɂĸß˲ӳȇȪρµЙýʚҖbІƣѕѾȇӮĩ»·Ύ',
                    'description': '3ТѽWї+ʝӦϩgΊ˯Ȯębt`ǑʆκӰүƽiԕWΥʈˊʤ',
                    'target_id': 'ÐpæǺψĆĻɃƯƻùʐĖӤϻҧϡϲўΐǋʱřÀаˋϹΦŋÉ',
                    'parameters': [
                            {
                                        'key': '¥',
                                        'description': 'ЍȳàʗΠДˉȭҹҢēӅ҇\x9cҗȘԣŞΰȩєлӅ«Ͳʭϧ\x80ϏΠ',
                                        'default_value': 'įʭ.ѸȭӸúˑӖ˃ύ¿Іǻ¤ÜǜĤч˥ʓ˽цѿȎ˚ЊxЪǦ',
                                    },
                            {
                                        'key': 'ԔÉ˗һϲʞͰԇJƥԄʖʰϏɐԪρҹԊŃԟϜдхϾʼĩ¶[ԥ',
                                        'description': 'ы±)ԫɽͽæN\x96ΓŨsÌŻȱԇė\u038dŬǜӠԖwҬҢ˽ö˹Ã\u038d',
                                        'default_value': '_Ήʷԑ\x9eÕӴøʧ=ȧҒӷң¢ĕəɫ˘ԩ²ǅʀŹӎɴĻԚũл',
                                    },
                            {
                                        'key': 'ĮȲɌЦ²˚8!²ÉŃ',
                                        'description': 'ӲӥӂǶà˥9ˏșũłӦ϶ńҸɢӼ««ȱƢОΊоƷ\x97ˀ˻Ԫ˫',
                                        'default_value': 'ӡŜ\x94˜ȹˏ\x96ϵ\x98\x8aѳȲû¹͵Кѥ¢πҹӟψӌŲʻҁ˭h_ɀ',
                                    },
                            {
                                        'key': 'й§˹źҵʯʴ\x9cϘʡɱӘϖËϩœõȮˤˬǏƸԈǣ øӊƐŤƈ',
                                        'description': 'ǹ',
                                        'default_value': '͵ТÒÕҺǍȅ\x92ːØȐȪϵǔØфӛPżŃ\\νϋʶĔͱΤӋҨÂ',
                                    },
                            {
                                        'key': 'ſϔƄŐìÇŵ˭Ɋб×Ҏŗ˨Ŏ<νѼ±ÊDΗœâВюˌЬȌѬ',
                                        'description': 'ːʊɾȏ(âų1ȿ˴ԕœƕùīԕхΛ˚Éϸ\x83øώʼԑƃǱ¾˳',
                                        'default_value': 'ҍΜíΦƬȴΣ΄ɢ\x93ǓѼ\x87ӞÎĒŏȕѲɫ˲ƺ҅ɴɻ3ƌҫҿĮ',
                                    },
                            {
                                        'key': 'ńȹƬŪԨƈʮǖɓv',
                                        'description': 'бӺьWǯɂΖǬΜѓЫɜʛĔâüәΫ¨˭ǋ÷δȹȃ°4žСӁ',
                                        'default_value': 'ƢŰԘŤЙ˼řɄ\u038bŰĒʋu΅Γ\x92ɧ-<Ȇԛы±ôßƈӵԃȿŶ',
                                    },
                            {
                                        'key': '¥ϫƩǜˀ',
                                        'description': 'Ρǂ|ҢňïůƑѷńӔć\x88ҋѨҤ\u0382θȾԭ˶ǓҫӆдȌЙƐӥҕ',
                                        'default_value': 'ń\u038bŲƕ?ȧ{ΤƭÄXə˞Ϻ\x83АϔɞÌÚԃʾʕ]ˁΤзз/V',
                                    },
                            {
                                        'key': '\x9dΞδǜпɇĠKɖΘг˅?4ʊѮиӯҖўʸ\x9aø/ԤφҲÆũ˳',
                                        'description': 'ǧҥøϯǤcɪjԫāȋſʳΒĆÆ¼͵ĄʬʑȭZɕόuҼǙƸж',
                                        'default_value': 'ϭӿÏĠ^¤ǌºɇƱȑѧK¡ŚϴğϡǲƥɳˀÊʹ˹*ȋњɺ\x94',
                                    },
                            {
                                        'key': 'ш\x9cҹˠӣƼǛɠßeþãÚӱ?ŗȞ\x8dҹ«ɀǗ\x93ȐФɤϓɉăх',
                                        'description': 'қ|ǖȏ˰ԛŘɔ\u0382ΙˣǡмʠΕϋɽȒŽt\x82ȽФäĔм\x84н˃θ',
                                        'default_value': '҅ԉњ˞ĤӘͳǀʏǫˌӅ\x8bӖΉ¬ˬўƔǬƘɅϞƯЫ+ɬŵЭщ',
                                    },
                            {
                                        'key': 'ƴōĜɊυʶđʯ\x80Ušѝ Ƿ#ʾ)țȗύХɐΔďîʐĸȠȺҨ',
                                        'description': '҃\\ΒƗ¶(Ĩжз˶ʭӮДСɫŲΫRμĝԩȈѲǬӰˌâsԬ\x98',
                                        'default_value': 'ͰʄƨCǪӚΟнΉțҐʷɪǃģЧϕѧә˭МǘȾOʜǞ"Ƿ\x87ƃ',
                                    },
                        ],
                },
                {
                    'name': '˗(ϱ,Ύә˲ƖɋӠэδșïӇʬΫ^ԖwϨƴӕσƹŴ-Ϲžr',
                    'description': 'ČҢĪͿąƋЖɑИſ˖ƽ\u038bΐ4ƠʈȅɲcƔ&ŲŐƍϬʵԏЙж',
                    'target_id': 'ɮhǫ9КȶΜӗѼŤáǅʬϐщрýiʃđҞŦɗӳУɯǩчçз',
                    'parameters': [
                            {
                                        'key': 'ҫΈʂӡϑԥΘҘ5ҌœÊÇԣΛKǔӀѩυŵɨюԅиˇ҈ʵȉ',
                                        'description': '{\u0380|ņˎˍ\u0380˒Νˮӭӹ\u0380˗˜ƪŖĦԔɧòʹѝȯ\u0382şGѥɑÙ',
                                        'default_value': 'Ăƫ\x96ԋȶʕ\x84ÇɄ\u038bӶǒÂʿі͵҄УǻÇưѹZů_ҊԁāĔũ',
                                    },
                            {
                                        'key': '˚OȍĝόɺӭԐЭ/©ʉʀXñЗҫǉPϻϒʧƙÕȷϓAЪѷѲ',
                                        'description': 'ԁΨȊԭâӃǽĹҦªԄī.ǘŮƭËȸƦ3љΥƦűǋ*įνʾϲ',
                                        'default_value': '\x90аlЙǥѱ\u0382ъ¢Ɩӌћԛɋ˼åŭЗ˯ęŠʨϣΝĆɓǧԐʢɦ',
                                    },
                            {
                                        'key': 'ѬóŶͷϺҐН\x8bǲ¦ҤĵȥƱЀaöҕįƳˀ>ĵïϳ˾tĐԠƒ',
                                        'description': 'ʐɀŋǚǟԍjЋʇ¤Ñ\x87ѠƷė¾ϮʚȽȑĖӛkҍ0ǑɯŴҜė',
                                        'default_value': 'ҟĤĎ×ȁӈϠˌӨǓLӸѷЮÔάЗӖɠȈÎȔ`ҰҜƘɕ\x9bǡĐ',
                                    },
                            {
                                        'key': 'ɹƹ\u0381Ǐ²ȜϼǢĬΆ˛z0ēІʢ˄ЏǴǻѸʰΎҼµªįыÓǺ',
                                        'description': 'тћǐÏuӡɆΕľфБšǾҧҔÈДӧȿģԞȘ°ĘΙeǦΡξκ',
                                        'default_value': 'φƮuϱӗ͵áҶȽӣӏNфǸǴҗǴǧƱΞÍөʴÆƶϛӦэӥŀ',
                                    },
                            {
                                        'key': 'ΤГŭԋӀǤν˕\x84Ӈ\u0379ϋϊ˹ʙʑ˄ƼɉљӕiȪČŖʨέğƍɢ',
                                        'description': 'чȶÉ÷ҦВ\x81äĜɟ,ʩ´ӄȅdʻƅɲɜțњðӧÛƩΝõɘŹ',
                                        'default_value': 'ÀʌəňĂʚéԧ²đĲӑʒԄ˫ˢďèңóѡ¹˖Ǵ¥ƟeȖȨv',
                                    },
                            {
                                        'key': 'čȣƞ',
                                        'description': 'ŢӋˤӉ\x97іȅLĠ˴ԕєǫѲƎΜ4ҕѥ˾ȌåΠßʷҒpɰ±E',
                                        'default_value': 'ϨĵƣӍӞфȴӃ®¥ѵÀӷxΐӭΰ˱ωŴǬıyɄ·ӍǶŵΫЙ',
                                    },
                            {
                                        'key': '˘ǗӬ\x9dŋϠ;ǒͳϩʻӸǼӃΛƜνқ',
                                        'description': 'ѴƉǓĻƋ¥ɁĦκΒğЌɈʗǣjԚҴХӕКξɽ϶ȶ\u0382ԅèκʠ',
                                        'default_value': 'İˉȪҰӏҘōϏёȊƧԨƉұ˩ʈƐѝΏҌʄɋѡ"ҁӷєʔΨT',
                                    },
                            {
                                        'key': 'Ї¤\x84Ő˳ǺͷɈűǜӃÅɜȇ¸ĉX˒ʟӭѥ³ѧɠɨқәŬӊ\x86',
                                        'description': 'ǯ˾вσҌƇΙԥȨȣҠđΘʾҐäɵʔЦćЊґɶͰǌßɡҸ\x97ϡ',
                                        'default_value': 'ԌƎζǈČӅљ\x9bϋҤķʫԩӤķԮ©ҴʤPD˥½ʉĸÕΑӎʗǳ',
                                    },
                            {
                                        'key': 'ɓΜӖǴғļɟԞǻđ<ǡ',
                                        'description': 'ӳ[˽ǩàӥĸƇƠжЭäӡŸ·Љ\u0379ԛъŕӌȎĜςʯʔǧ®ʆ˖',
                                        'default_value': 'ӾŕÙƐIŖӲǍʎɬǦєʈԤΚŸʚ\x84˜ˊȻƛˑɃӾ<Ƶȥǚá',
                                    },
                            {
                                        'key': 'ЭƌǘβӶΎŉӕũ˷ίͱÀǴħMƐɳәƭǺӊο\x8eĺϛͱʮǚś',
                                        'description': 'ľУТҫǫϏхş\x83ȼȘЪ²ɲ_Ǣ<åʥқӠďǵϺǁҭJǊ¸ћ',
                                        'default_value': 'ʌ©ǴЖ˶ѾӔƝƕμ]ǻȅПпҺӗ\x8bрҝїѯfÄ\x96˝ɇІÓǪ',
                                    },
                        ],
                },
                {
                    'name': 'ԥ\x9aҙƩѰ҈ĒШɄǨăˎěԚƾǷʢ¨ѼјïюҶÌǹŦ\x8bǋКȵ',
                    'description': 'ƸɮŀÐþ¹Ȩ˗ΕʁʹˊÙʒ\x8eˠϋbĲɶõ¦\x84¬ӪԡӴ®×σ',
                    'target_id': 'ӳƸѭǁ˹ɷÿӧЦҤ҅҈ГЉˀӶʍҟ\x81ӶŵTɚßşԄsϮĎΐ',
                    'parameters': [
                            {
                                        'key': '_Ҝ\x8dýӆӖөҀύĺŭӡȠϠŀτOɍŦǄǤҬˍûɇ\x82ŷ',
                                        'description': "ӧ¸čɥχю'ζū˴ЄƫîΡ´]ŢҢƽЮđҲγǼЕ˻ҊѦϋô",
                                        'default_value': 'ɱȓЄyʳhґӲñѳÆǇúѳǤӡ\x96ďԦӅӌƛŬʀɍХCÙдæ',
                                    },
                            {
                                        'key': 'Ϫ:ΒXҾʖȁǓAѹӿһȝԘԣWƜVĀƿčҔʻĚΪ\x83ʱ˚ƹΧ',
                                        'description': 'ͿɴŚуĲ$ǤwғγƟ˸ƪȬ\x9fŽЬҌǃɹƥĬЅԂĐωʔÐɹė',
                                        'default_value': 'őӘƈӽƅ¤mǜtӝɣƈ҇ήȜτƮ˝сЃԡɻFȖƮϔΞУ\x80ʗ',
                                    },
                            {
                                        'key': 'ϗ¦ϮƩԡķ\x91ӇϔІɑÓԐɬ#įЮśлӷÖȹɐϊƄͼѭƵЏǹ',
                                        'description': 'ę¿ʧOǬǦʩϋ?˦ЋƼjґǭĮſ҈Ԡѥй\x95ĀГЂϗƷϫ}Ⱥ',
                                        'default_value': 'ϊЦΓҋԁ=Μɪ¶ƘχҔɇҎԗэΘêȆ\x93ЉƽaģÎ҂жǑӤÆ',
                                    },
                            {
                                        'key': 'ҌŧŞҡłăѾТØʄťмΒƩȸԙύЇ&űÑƭźҵ\u0383Йȗȗ˺r',
                                        'description': '˅æĀLƼɕˤŘ°g\x9fƕĞčтßΡǕʲʴΰFƩ¼ӞΉЉȒŊЧ',
                                        'default_value': 'Ӽɓƴǥųԃͷ;ĄǘŏɤҥϬɉɀˎʍȌіКrˬƯхӈгXԧΙ',
                                    },
                            {
                                        'key': '¯ßĭĤҍķ˲ϓǾ˺žɴŤÕΛԌɆҊ¯ΜŀŗǢõɝĞǕơӖĮ',
                                        'description': 'ºɘԙʉzо¾´ҲԖ±ƠѐŜ\x88ҫȸΆ^ɍv˄ϝĥǮíґɥӨ8',
                                        'default_value': 'ЃςԏЋŢȼ˾ϐ÷ɕͷŗǺ\x94ĪԕϕÆ_Җм/ѝǮЯӨәȷéǞ',
                                    },
                            {
                                        'key': '˲īáʙɠıĠˉɱ6ŇŎǊæυԂıÇŁҼь.ϠȥEaϖϻʤѓ',
                                        'description': 'ԣȽġʽƴɴʆ˷šȲэŇѻȐǓĬ\x9f3ȴŘŷʦþϸϭŶ˰Χ\u0378ʄ',
                                        'default_value': 'ϺwĬӨѡДЗƬʟхė/ȻŜΔˤӑξϨɰǪҭÁϗԖǴ˻ѠʭЩ',
                                    },
                            {
                                        'key': 'cʬ\x80ŢѹѨȋгбЫѸȳƮĲϣˇÓӚȷȐυĕĎɚăҞˎȡ˖ę',
                                        'description': 'ơȢͰѧΕҾƶрƵϻ˼Ţžïʘ©ȱͳ¼Ɏ¿*WƤЃԓѬԔрy',
                                        'default_value': 'юҜΩ¹@ʥ\x8eȪø\x84kҬҜʌȀϕӯϺМĝ˗ԡǖԗˬsҵ˫s˽',
                                    },
                            {
                                        'key': 'ЍԄÐέӁȸԙϜʶ§\xa0Сä\x8aӷØĥΨʤH\x97ͳ˳ԁжԚºӂňӃ',
                                        'description': 'ƴʺzļӌυɺʿƴ˷ӲɞǅƨАԟҲԆ\x80ŦѦŨ\x93ŎÄɯɾԒҴŏ',
                                        'default_value': 'ɚӳʓǕӵËȗñȡώȏʭυƭǰʈС$ôÉζƀƕΟɛԑ҇Ș±ö',
                                    },
                            {
                                        'key': 'ǦʂɦƘƔҴɩ¸ʷ¯ƹƦ§эȦȫŦļѯμ\x8fťюƔčĝķԦϋζ',
                                        'description': 'ҜĈӔĿȶƱ|ǝОo\u0383ýѻБѷȓȹΊғʋсȗѤɹżʄɉȄзѼ',
                                        'default_value': 'ϲʄÕĘǂ&Ǽ~҉BǺŧԖҕӒêͽĶɐÑʭƑΗԓɧƐUŷǽȷ',
                                    },
                            {
                                        'key': 'ҽ˶ƻϘиӥč҈\x85\x83˕ӌаˠ¹ӑ<ǦɱΈЗąӁćρѾԋʁћƉ',
                                        'description': 'ÕʡǣɥϽ\u0380һνŴͰОɴҳ¡Ėӎǁρǅ×YΦȂŲƘҳˌƙƔЯ',
                                        'default_value': 'ĪǧаТЁÔԬ˃üЇ.ԫ˳ʕȑǾӿϝӅΩǷ¶ɢˀʥƿӕϽˌƩ',
                                    },
                        ],
                },
                {
                    'name': 'ЬӺÇÕ&¾ΐćĻтЧͰҝЎʺѽȹÔϑ˧ʤřҮŪ\x8bɇŮȩǱĂ',
                    'description': 'φ҂ʜӦϰŋЪȲ4ɓ\x90ɃøͼuѯЫ\x84ƓÏȾΫӢĉѽ˨Ƿxău',
                    'target_id': '˙Ɋο\x8aЎԘÅȫѓĔѼϜϱȧьЯƙ[ԣZǜӱԄ˳oԈϺӢϳω',
                    'parameters': [
                            {
                                        'key': 'ȃ˦Άȥɒ;WŚsȓȵчϾjа΅ƿƇʇɳăYʹ@è5&ԁHŹ',
                                        'description': 'ѭЂľʩвϙǡ˽юÕŪ\u03a2їóʱӵђΪƫҾќČcʣӆѧщàƨʪ',
                                        'default_value': "ʞ҃ɨ³'ӰѬȶԁ˒о¿ѤþƬȣɶ}Ǽɦ¤ӓЌƈЖȉʟǍǩʳ",
                                    },
                            {
                                        'key': 'М¹ǢӷΡʽɗƶņżĉƨUԜӼ϶SřΨâϿҰфǁ*ɱƙƚCí',
                                        'description': 'ѱОŤ¢ѫ\x95҉¸ϺÙ\x8eÐӅДɴԨɱЉƮȤДξʱËȔ2\x9cŅtͰ',
                                        'default_value': 'оӜϙ\x8aӫӧѱǷŕ?ʢ΅ў˝ҔѴҶϨǓƣΩѲƒ-Ɛ~§)ùȚ',
                                    },
                            {
                                        'key': 'ÍƢ',
                                        'description': 'җΡ«ȸŧѱȰėѺ5\u0383ˣТéӶҖɋģ\x96\x95ɐFȶДāƉĩȃmХ',
                                        'default_value': 'öѯEͻ\x95˩<ҡК½>\x84ЈΎРЁ»ƛϱȥԥŗľѲˑáΦ˽\xadҩ',
                                    },
                            {
                                        'key': 'GǚϮңҰëџʷČ¯жӃӄàӇʇƔǦіɕ6Ũưʙԋ\u0382Ԅӳͱ\x9b',
                                        'description': '_ԊU_үӺƜΣԪӉЊņя\x87ˏΡSХ\x9eΗχʡǥԋҏ˜ԂǐԑБ',
                                        'default_value': 'ӗȱRî˶ÞŸͳ˜ȿԘʯԜǹӏ˟Ëľдӯ®ʝʋҸßэ¹\x8cŤ˯',
                                    },
                            {
                                        'key': 'ˉʧΌ¼ԟ4οÇʣƕ˒ĊȬԃӮ\u0381öƷΈ\u0378]ͻOđ\x8aҏОƗ\x81',
                                        'description': 'ӯҁ˱χϹǐҬӖưХ2Ѐυ˱üǱĉʶ"XǧτˋɱƚуΎ,Ǡ¡',
                                        'default_value': '_lȻ˗ӭҬӖâƑǒYдʛЂѸÃȕҷ»÷΄ΡϙԆʷ˃КЂ(ʝ',
                                    },
                            {
                                        'key': 'Ҭӆˌԥưʂāňǧϡ`\x9bΎҖĐ˫ÿʀӗϼҒǰ\xadȌгŅѼҾͺƀ',
                                        'description': 'ЛȸӟPЃϷԡzˎ˱Šˏ¬ːûʯªбȆѐćӊĞŚďë\x94Ʒĉф',
                                        'default_value': 'ʆʢĊ˛ǰĝ·śӺϳцǖ˳ʅƻӗТѷѫӋ|ԏӐѸэѾ\u0383İɢЇ',
                                    },
                            {
                                        'key': 'ȣϬɘϰ]ϜǎЦȪȼpΌ·3ǣúνϞǣ=ӋѣΏњЈɉ\x80ǍȭȤ',
                                        'description': 'ƶҤɺϡïŀҚM\x89ЏƔϗƽҟӕÐӼϓȑ2Ʋ"ԁȇțùìĸќł',
                                        'default_value': '҅ǈЬƱЛʑÎɪӱ\u038bƔơ\x94НΖ³ŦöÇŗĻÞ}Ҍ~҂ΕÇƒҼ',
                                    },
                            {
                                        'key': 'ˏ˨ΎΕŹ҄?ȺӿВˀ҅˧ŉvҭVҏҔхфЏßЃƿ\x85',
                                        'description': 'Ʈɤ~ÓЖ³ьŒwȕҋϜêɵȦҌΑѶӹӡȚǙӶԃɦ˺нԡ˒ͼ',
                                        'default_value': 'ΞƩǚ¶ƹ3¥ěзәҔĝҋ\x95*ɷcҹјҬԐϻҕЦáĨӹ˦%ȝ',
                                    },
                            {
                                        'key': 'ͱʨȓţÚŝϑƛźĆæGɃѧKŒʠ÷ҧƑҭȁ?ƀˁͿˊîçВ',
                                        'description': '˰¬ӯɉύāΨɠȢķңγþVěrҰȠƇĉÌ;VxǎϔʡΨĚС',
                                        'default_value': 'ͻҥȫǉʮϥϭԕљѓǔ7ΞɧÞӤρĐЀɵǷԤѲѱǖќėҏĻǅ',
                                    },
                            {
                                        'key': 'ВƆȢ˝ǎĳѥlϷï\x9bʖƄɘϼѬžğч¤ȓŘԑΫˏĤҞɢĈЫ',
                                        'description': 'ϚƋłВɻǪȚȉǑŗȅŗȬΤśē\x83QϚҪĨ˧ǕќʫАçԟӘȰ',
                                        'default_value': 'ɑȴöƬnɲĨŏǆ\x80Џţʂ\u038dϒǪѴɛѣøɎξϳkͻˤƽșƫԆ',
                                    },
                        ],
                },
                {
                    'name': 'Ϳ«ßԌʌͿ©ČщбѨưљȝҰaǍŢƒЦЇş,łǛȦѮʘɖȥ',
                    'description': 'ŢЬȕ^"ΝŨüʠƝ\u0380ҸӛΥ°rȞ\x96ǠǏĭʺʡtħПŁē˅Ό',
                    'target_id': 'ћxјѩύʑԢɧƸҰԍҰȞǚ҆ɵԛΰl÷ÝˠYЍ˒_o½Ç"',
                    'parameters': [
                            {
                                        'key': 'ȁɬɉīʬϼ϶ȱæλůʥļшĒѷşʡԅÀ\x96ʟϯ˵ƅűāȦȀХ',
                                        'description': 'ơɪ<˚ЖӌɉҫΠ*ÄĊʂљʹȜƔВюɹƙƼ˂ьƕүӨŷô²',
                                        'default_value': 'ɶƶȭiԙЖџҐǷÅǐӗƓˢuıѿϨɒ´ĖŷŽŘСтxѶϼį',
                                    },
                            {
                                        'key': 'ȃȵɓʚ¿ǷʖӌвǸ`\u0382ҧɑÙ˄ľēСԀÒφ£ҟЅӧŴÚϲ\x92',
                                        'description': '\x90ԎӭʍϝԁӭƃǕɢ\x93ͲīûǗЯυŶ2¹ƵÄɡ¸¾\u0383ƓĺɉǇ',
                                        'default_value': 'ˤØ˶ҝӽʋPȯϫ˰ƝǮ%˾ԭԢӞӼ´КʚUǔȆǑβϖǯϺѪ',
                                    },
                            {
                                        'key': 'ҷɄɏȔòУҗɠ2ӎΖλҴźɩȄƜӍäĥΏƖϹɂêʚɭюǘϚ',
                                        'description': '˰:ɠMȭ\xadɣɟ\x91ҖϱƷǎ˵NzЪʽ{ɎǏ}ÂƀӛˡΑÈΑM',
                                        'default_value': 'ΤʫЗɒЁʯԅŚҕҚҐKǘΖſ]ϖӌƿόѓҭÔђпсѓǂʤN',
                                    },
                            {
                                        'key': 'ӫԣĮʯƀð=ԥҫÚŬиϞyξζȵӫұžɧ΄ʍƾѦ¾ҧ\x93Ϟʢ',
                                        'description': 'ġΰƄӥ&Ëʧǥ_YԆƄϙԬĬԤ«ŁɮçĕϣÊˠŊȉÅþЈÀ',
                                        'default_value': 'ԆǖˆƮ;Өŝԣ·ìqƸŋ»Х¿ìңԟъϚҙİńĜǼqɆ˛Ǆ',
                                    },
                            {
                                        'key': '\x9bԕʰĦҟ˭ПʨӤ´ʑђƩSřΩӨѠʨĊŒѹѳʜҞҾҶ˒˳Ѫ',
                                        'description': 'ˈͽΊȼіǫԤ9ǚȞőУӘŹόɎӝѠҪɀԉɁɇǢϚƘ',
                                        'default_value': 'мèјˀȺũɬʻȨԔBϗǢД˚ȶqҎĮɵ·Ѿȏ\x8a˭҆оξŒЅ',
                                    },
                            {
                                        'key': '˩ѴԚ¶ͺʞƀʒǣʮҐŪŷϋЅӞƘǒͺȾǓsǖБÓȀƽӥвɑ',
                                        'description': 'ŕ*9Ĭýʿ˨ͼИϐȄ¤ЦíƎ!šéǥƵ÷іϋĈǛ҄ĜŏʇȞ',
                                        'default_value': '\x8aʮБdԮɶвЎ\x98ʕƺ¬ʎǿӖ˳ņԘǢŖ·Ѿǃǧф˺Дżˋӗ',
                                    },
                            {
                                        'key': 'ԕʋ˯ξ¡ƘҞƌ\x8eȘƲӀʓЏDŸȇƴě˞Ѳ_ŎƍҐ˞ϘMƍΫ',
                                        'description': '\u03a2ŲɡӶЍŘϓӍó˯ZԢųνx˸eƹʜɽĔʨÓĐҗ\u03a2ύ\x91ƜѰ',
                                        'default_value': 'ɋιĒλѿВόǻƉĩƕ˒Þϡ»ſŇƘȌƸԥѝқӨόǆÌԓΊˆ',
                                    },
                            {
                                        'key': '%΄ӏȏʠϔΉѪÕʩǿͼȵƑ˰͵ʆnıΨϫϼ:ѼӃΌӉǺĦө',
                                        'description': '͵ƀўαʣɠƈͷ˵ũʡ˟΄ʨįʟ˲˩ˎ(ÁȵқбёŔΟƽҖ>',
                                        'default_value': 'iϜˤƵӇǭĲǕ҉ӅɅêӅŠҳēźүϙƝËʠƶӋŰǮ˲ԛBɑ',
                                    },
                            {
                                        'key': 'îʽ\x9dͱҶȽƠþƫϜȥų˹бƳõƇ\xa0Ş˾˖Ǝ˗ĠʃӸǀ«țį',
                                        'description': '}ΛѼǟÖͰʮtVɌЛΥӞŹmϪθǺĚǑŦŞнƥҵćӌлŷԁ',
                                        'default_value': 'ʒʖӸѾȢѠѽ\x9bʱƚɓOҺƩ¸ѭźћyҶϨΘƾĠŶжΥү˦ŧ',
                                    },
                            {
                                        'key': 'Ҥˀßͷ˹ø¦ƌƳÐӵˎӜƓӶǦƩPî·ϯ¡ѸΨ',
                                        'description': 'ҎɒľκɄоƊĈҲˡԂmsʲĘεŏѼξҢńɔȥҥҭɹÛɕĽɭ',
                                        'default_value': '\u038dҶʋϡиȉ\x8fϨһΥǟҟ6ȽѡţȦҹАʉ\u03a2ȣĨZɦԙɣҀαԃ',
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
