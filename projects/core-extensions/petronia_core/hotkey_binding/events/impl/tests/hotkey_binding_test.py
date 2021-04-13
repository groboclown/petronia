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
                'Ƥ\x92Ϫщιʟ\x92ĆýԩӸԒҩζVɄԠɧÙϢσƻѬҽ',
                'ƧɡХϓҴˀЋҍǕŉʹǔēҩɽȘӻůδЭɊŴ˽Ɣ˴Ҩ',
                'εӂȎ˸ɶʶɷΤƄʄ',
                'ӱūѩˌΘ³ÁΨ\x9eʱʱЁĞˣ΅ƺ¸',
                '\u0381ðŐȂ×ŉ\x8aȱξϼԗ˽ѝȃŪҊ˄8ҁ',
                'ˢhŠ',
                'ˌǎ¬ЙγӚԋƴʝƞӳŨ\u0382[ǥЉϼ',
                'rc\x8fҵ-\x91',
                '©ˠ˱͵ҧ/ÁКǼ1',
                'ǛВϵ\x85ǻČŌώ\xa0ǥФ˕Ͷн͵οОÂƲͷ˃',
            ],
            'comment': 'ҳ҇ǙΙȩ\u0381ǧų\x83ȃˎӷԭϐāĄɸƚǰҰχƉİƊͱ\u038dӍà[Ŝ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                'ǿ',
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
            'key': 'ƻéʞҕ\u0382ѩǜІҢǑйѡҫÆʵϔѠȻГѐɔǢδöиr',
            'value': 'ϭγσȦȣdҿϾȍżʫǀʥƻԙåӾβģ7K`ѐӍhəÀ4\x90ˣ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': ']',

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
            'target_id': 'šʸѨԊśңȢĜőɮǨӧзǝϢԮɡƘӺ˦wҔѡԧȠғɰƍԭ˸',
            'parameters': [
                {
                    'key': 'ԝ)ǩƥȦѭǌǺўΏ\x9bƍȚǕ˹ċϺƺâ',
                    'value': 'ʿт˛ү-ӕ\u0379лџʥƈҨӝӳ\u038dЅӻ|ſϧŗèŢϐɆ\\ʠӹґӑ',
                },
                {
                    'key': 'ӗҟӰ˸ѺʪæʹŜѾƗЋ˓āЎƣʑƲƉҼη˾ȏѻԒҠӀΰmƙ',
                    'value': '˅ʈǑƑˑ÷źϠоȾϤf\x8aӽJͲňƔϙҷҲӱʍQηϑȮƷԫǺ',
                },
                {
                    'key': 'ĝǦƏё\x8dΫӾӋǈȐʡҵԋȸʠtƺπˮxŮ×Ѭŧő',
                    'value': 'ƀтϿʵЋʒѹäβе˴şʄԒȥƹΑԑκǇͽ\x9b#$ӉɏͶŠӎĜ',
                },
                {
                    'key': 'шҧæϮơʷЉĞǶΦѽӳșҎßˁ\u038dʵňǸΣҊϐǩ\x9bʱŻƓjʃ',
                    'value': '\x99ŤбÑȇϳƜ\xadҀȠvɯˋŜѬ?ˋҾ²˖ʑ˷ʽˏYɰɝĂĖϷ',
                },
                {
                    'key': 'ѐȷ0Ĭ˲c\x7fʒҨƧҘсȤȉʤĉʻЬȞɓŻҔҾͲСȰǷҽҋø',
                    'value': 'вŭϋtуÛǈԂˍѱªÈţͶϛɧɺƻϕВԫͶʔңïȉȕӛ˩ѧ',
                },
                {
                    'key': '¹΄Қ$mǄѿѝ\x92Ç҈ɞȒŇЭǈ{ſҺԦӅшѽͺыȀǺ˵ƫG',
                    'value': 'љčȿ\x89ӱҁӾYǖ˼ϊPŠѣ˶ǗҢёƸΫӎЏÞɶ@ӎ£ԓūУ',
                },
                {
                    'key': 'ƁɃө§Ȱƪ"Ɉϸƫς¥ȮѾѨӶʙƂĢѴӟǽϐЁѐχ@эǟз',
                    'value': 'ŽĀJÄȠǇӗ§¨ŝэƔ\x8bÏʑĕӛͷӦТҧӈӘĖɜCî҆Ĥ=',
                },
                {
                    'key': 'ԘƮèèȟөҮˬŕʲіǔɨșȨɏ¹®ĚǧЍΫʉЪУ˶Ѐ',
                    'value': '\u0383bцǌĚ\x9bӧȕâĠˠӭ}Ʊ~ǂԉ˨ĬƔƀƤďÒϫʜҨˎрҿ',
                },
                {
                    'key': 'Ӈ2ɀĔӺЅ˓ϖΉƾϭØԠȎÈƅҷïн˹ϗҁ©ʉĘʶʫʓƟʎ',
                    'value': 'ĤɅϸǂ˘ΔǞѫÙŋˊϳřǱʬС¾ŋΌEĿÅȳΛʲҪΊĹðл',
                },
                {
                    'key': 'Í¯;ΕҧĩŒǍ҄ͻƎǄĬp©ÆԗԂɨÉųȑЎΌÍѬƁ¦\x84Ӂ',
                    'value': 'oӁǍ҇ƳǂӾȪʁĜИŃǩčˈΟ˾ΟɌʈƢϬµ§ð@ѹΥɍд',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ȕʶȗǮҤ',

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
                "˕˟ŏЋȈ8ƽɁĹ!ˬǉĶʈϛӷҒˬǦ_кąō˨Ƥ'Ҵ",
                'Ѓ҇Ӂ˖ѬÅėҌ˴ȹɾҸ÷\u0380ъƅź-þжѼʊʂԄӑ',
                '@ʸ°ҠÿԝÃƎġђ=ӁӇʷ\x97ʡ҂ķť',
                'ƙНѬǨǮ\x80ȵѫ\u03a2˹ɖÐξ',
                'Λӧ.Ғȸ',
                'ʂ˯ӳȕςԐÙȈлǜеǂʹĔӐǊѫÝ҅аƛύў',
                'ˑ˫Ĥ\x97тӿԙąľȧǳĻʫėˎĢʠɔ±ŜԩĿȇͿҨӉѿ',
                'ԑϻҴЊӡǜœѻν˷\u0383\x87ɴԨΣ˳¯ʵѦ',
                'ʃwАƊ@ǮȥƄʨԉǂ±ŁƉΟĜ5ńȕʀÃʖǼȡȀŁCĻȌ',
                'ˤħǝôӆʔ\x90ĉƛԏϢÞʓҘ',
            ],
            'comment': 'оԛ±˧ɰʁѢč\x9dӏԩʆQϬSˠ`ÜѪɱҷ6ԄƧϕΙɷˬӋФ',
            'event': {
                'target_id': 'хс˚зЯϰȱȘȓǪÇɦ\u038dɼϺÕȎϫĉͷŅӍȑșDϱɾҾŶͲ',
                'parameters': [
                    {
                            'key': 'ʑȩμOɇΈԭǽɴcΪѠ|ϤƬşǱўŽPϫãʀʅȨ>˂Ъӟά',
                            'value': 'ϛЭNԏZǁϜȼɗƩѨǧϕ\u0382ƺԍŌΚϠԊԮ\x82ȐźţSYǭˠ˨',
                        },
                    {
                            'key': 'ȃ*D',
                            'value': 'ǻØԑϬѴgλԂ¯ӣȶϪÍНӇԟ˾υҊљȣÂ8тϏΊʒд\x99ő',
                        },
                    {
                            'key': 'ʞĠ\x82ЮˣüҿЬʘҾ·ԫȩ҄˺ΈûĞЭӘΌƓļҾҒĖ9Ђμӻ',
                            'value': 'ьў1ϊϮʐʽ\x86Vĸћш\x8f\u0381ӍɡŐƼˀɎНǽʌԎҋеɱиļƃ',
                        },
                    {
                            'key': '҂Û|ɖҷͶʅыĩ\u03a2ļȺɱϽѝԂČ<ӘƽčѓĶ˥ʿĕԛɴƯƼ',
                            'value': 'πǍďȥŒзϵńϭʽԇȇƅ©ϫFδԏʣʜĞʍԀӽɢυ\x81ǰ˞Ȃ',
                        },
                    {
                            'key': '\u038bР@ϑҦѧҙецрӅϝҡr\x82ŗʩͿѫȑǝVʄÁщԦĚ\x85ň×',
                            'value': 'ˑ6Ҥȳį-τƛ҆ӴĊɪ4˫wÅҮӶйΡcҾȸњӺԘҳdʵä',
                        },
                    {
                            'key': 'Ð·ǘ¤Ӊı\u038dҶbӠȎҠƞҁğ˴uԢMԗ',
                            'value': 'ңʦӣȉ1ѨПεИńԭÑ°ƀƴͶǼƸя˱Βи,ˍϑΙѝҪҍƶ',
                        },
                    {
                            'key': 'юƬŦϨѩԇÏɔȓԗÊҳȯŮúԌѧɉLşǣʵЋȒɅǾүƶɤѝ',
                            'value': 'ʷ¨˲ǅŻ\x8bæōn˝Ͼ§ŧʝņΟƿ\x90ԅĦʙĭͱʎɖӯʅԙƹƔ',
                        },
                    {
                            'key': '\u0382˟ȷư˃ī\x9fΚβѩєοԛķыʎЦˆŌcїЦͽ\x95ЬͶeÞ',
                            'value': 'ӡͻцµ;ˇПɀʧȲѪӘϩ\x91Ż\x85ѤʄԏɊҨӫͻʾЗԊѻω¥ĸ',
                        },
                    {
                            'key': 'ϻ˄˅ӐɊԅѩ\x84εѧΤʜΩİřƙʾèŴŤЮӑѷʋĆ=ǢϪŠҕ',
                            'value': ',ºϷƻ>ɥϠԨЀөɇɆү=ƓǫăʷѼĐŋǺ˦Ҙ,ԚβҼàҌ',
                        },
                    {
                            'key': 'ÇĸºɩԎȘˡƌłԣҥțʾЩƕҊıФӵŅҼӤОʻϚūͻG\x91þ',
                            'value': 'ȉφ\u0382\x8dʅǃŗźӴόʻȵŌǺǇI¢Ӥ\\пĽΌέȐжÖҐȑưЎ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ǁ',
            ],

            'event': {
                'target_id': 'өsǭøu',
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
                'Ͽ|ŀÂѾ\x82Њѝʣòԩ{',
                'Ŭӷɉʤŝ\u03a2TƲFк\x83ӀӅ˻ƺҔ·ǋSȎЙ',
                'ƶϮ',
                '·ίϓoϒҦâ',
                'Ԁȴ^ŦИѳʯƗƪ\x80¢ѴυȍȖƄћƟ˚ӑÓϘʚǂа',
                'ζĚÁIʑŸӢÜҳ',
                '˵ҘŰҍҴ¸\u0380Ʒ¨ӵҳäԡđ',
                'ȥ҅ӂɄţҩǪĬρĢƐңϡǒΝѲ;',
                'ʢîɒύ\x91ƵĸɧѣЛӉҍ˶¨ԄϾÃ',
                '\x88ć',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ӈ',
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
            'key': 'ƴҊƃȮìơĈȚӅƇʙũҿĀŏőԑɂ8ς˲ʠҧȉѦÍϥ\u0379Ї',
            'description': 'ҫɭ˚ȋљğɓԂɣϑȰɘϷǏΗǲƭҢОğϖӒʧCҘĴ?ҚǒҪ',
            'default_value': 'ƷǨТ9˶¡ӢͶɻ˦˓σɉȃjσǌưš·ͱ.ɵҝÏń҃Эʜf',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ĵ',

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
            'name': 'ģ2ʚ\x89ǼƗʎǉčăвǀВуˏućѸ\x8bēόЌɟňȶӥɸYɨȄ',
            'description': 'ŧɗșʳЕˑӟǰĝ&eĕǾƌˇ_ԇđʣƧħsӅѭūgЏǂď҇',
            'target_id': 'ȆȟκΥȘɏ\\ŸзӬƘɐȇԟӔҏɧ(ҿ5ʮ˛ʤˏπĎӔǱèͳ',
            'parameters': [
                {
                    'key': 'Ĩă~ϵɯ4MӕɋӒÈǏ˰ҏ˻ƏλδБƶǐǻӫ®ƓӠϕ²¨Ҡ',
                    'description': 'ķɅГώОXϦǢƋԡΖ˝ӻ~Ғȯ¥ǾÝśÌӅcО˪ĜíҝЕƂ',
                    'default_value': 'ʑ«ÝĽаÚмħƨ3ͶɤZ˅|çҀŴЦӐԅЉӤĚ(ΙԢ˓ɳʡ',
                },
                {
                    'key': 'ӈãÑћЄюҿ\x9a˝dǬͷµō\x93ʛÈѰ¨ƐҵʶŻ\x81ȔP)ԖϠί',
                    'description': 'ЄħƽТҔĞǛщĶґŢͼĂԒQлӨ˷ӄ˻ϞŋӌɦŇҰưėϩӊ',
                    'default_value': 'ͳԕɬϻiϬѶjāҨˢȜΛȪɊǅɧѢjНɠʙʦɝÅΪġȹÖā',
                },
                {
                    'key': 'ʉǆŊƓā}čƧƙΑȲěВωȜψˈ',
                    'description': 'ѥѦКѩȇȥԤǣ7ǈʣäύɒiɍĹÂëǭɬӽΡcʫ˨Ɖʀ\x89Ō',
                    'default_value': 'Љͷσķ˨ˢSȟУǨɕȌђˎОӽВΊz˒ѼϏҲЄ\\ðĕā\x82Ã',
                },
                {
                    'key': 'һūϬƟ×ӱ\x92¨¬ШԀƹȇQˁȍˎŀҥÈŹЌǠp˞˩ɘ\x7fɠ\x8a',
                    'description': 'ˈцҴԦԖU҄ƳΉ˒ɨʖӧŲѥĔƃҀǠԭǱѬ»ВȄˑƦҫӱä',
                    'default_value': 'ǴǕÅш\u038dʔwˠЎ\x91ΰҜҌΜКѶԑϋпϵnǛõɮѤҞ5Ǯ¼Ҷ',
                },
                {
                    'key': 'ƘϘŒΡ˼ψƯˋȋѬ\x83ʴȰöǢЀ6дљȲ\x90',
                    'description': 'Ϝˆӵ҇õԂΙǤœѝ˯ϮǳǊͻϗāԜǦɁӓ˩ƴɱЈʡɂφɩ˘',
                    'default_value': 'џԔǇӴљʥԚƞÃЕÄjмvƘʹ:×\x89Жä\x9aԂǥϱdѻĒ\x98ǹ',
                },
                {
                    'key': 'ŬǨþ»ρԀƺω\x83ӳЄíҌ',
                    'description': 'ƒƿʢŊŒΘƼԭôˣԫwҟΡԜϷϒӊ\u03a2ƌϭӥŹčкƥĪМμǖ',
                    'default_value': 'Ń˷Úӌϻ;ĶˏΗđ϶ĨҩҘčɹiįɺŠĀ˃Ǌӽӽ&ǛôКɟ',
                },
                {
                    'key': 'ʖʗǭȗ˨ÚȖȠĸĉ\x97ƼĲЦәЖŀɾÂ]\\ѭɄ˱˝˭кѦԇȄ',
                    'description': 'ơŽ\xadЋ~žыĳɐ®ȈÂʥΓˬ˩ʽˣéԖϏîãʓќЂΉц˗˛',
                    'default_value': 'ҏ=+ȉȌǡΟӧGüɬ°\x8bɱЀ\u038bΧÎǎȝ.ђ҄ÜŬɬ"Ɯϴɵ',
                },
                {
                    'key': 'ßʲȫÛǜщԘӽřώ\xa0@',
                    'description': 'Ɛ ȶƣŀȫҏɿ4ĮƵưδwĞķΊƇѬӱѝϲF¸\x86ƆīʙЋЅ',
                    'default_value': 'ʸĤѤГȮϯ\x9cŔʃ҃ʼƐδHԢ¹i˥ͰǷƵйќɆҚԫɃBĻϯ',
                },
                {
                    'key': 'ʶΕ϶ѵĝŇěWͰɈƇԑθʜɍɇ8kǸ\x92ψӸïͼjҋ϶ƍҲӎ',
                    'description': "yGªOϏ\xadäɮͻΎӃʟχΆӱɔKʭ'Ѵә\x9dӳʠѹɡӣη\x83~",
                    'default_value': 'ӣəōgϾη|Lλ.ȈѧſɊԥ\u0382ůɾ,ÖӧźԀЫɯȱЁˍ¶Ԕ',
                },
                {
                    'key': 'ʽѺϜŮԚƝӹ^ԜɻӲΫĩʾ\x9eʡǯɩЦνŧӥˊò\x80vҏ\u038bŀʣ',
                    'description': 'ʒӇѼғ?Ѱӝϵ¶\x92ӘƚªѭEïƗǫиƍԚDҵΆуʯ҈Ķ˼Ѱ',
                    'default_value': '+ńкҠǂĽϭ7ɯ¾ƜĂ·űĲďî®ζƝəʿϤȽѓ~ƿ\x88cȁ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ҋ¬[',

            'target_id': '\x8fЀԗǼά',

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
                'target_id': '&ηΕƮǽ¡Ԁ˖ƀĻǝψѫ»ƁϹƯЊҝĆџ\x9dƂUƵȦʛϙӒɫ',
                'parameters': [
                    {
                            'key': 'ƳǫΐтƺgпѷЏΫһϼԖǰWϷ$Ƴѹ\x89˄ɼѲԂǝƒɇɭρӏ',
                            'value': '!ĮˉΠԂғɤҢϞǚќΕȸҕјʚÉ\x95ԊǰҊłƟˋ-ɢĮƁˋÄ',
                        },
                    {
                            'key': 'ӞŐ¯ʥԀŒͺǥҚ˽ǃӛķΚǒҔ\x9bʗņŎq\x9a{ЉҫʝQżʎǡ',
                            'value': 'ӹĭŶЀŲɳӦ\x8dȿԛ*ҖņҴУԈӆѻЎτҦȨɟȭȸϛŭ˾Ά°',
                        },
                    {
                            'key': 'δӑҨ',
                            'value': 'ǋƅ˔зº\x9c҆ȁNƝêδŭøȹƹЯħ\x8dʠӍÊȐĦԭѸИͷԬɼ',
                        },
                    {
                            'key': 'ƋžƢŬ5ԋɇƑǙиțgʢ϶;ьӋӲӥ·ь\x81ś˶ǇǺŝƈɊɶ',
                            'value': 'ȃƊɌƽȹæĖƉ·ǆҸ·λΖďrȽè˫ǶʎİϳǠŒˆΕJοʹ',
                        },
                    {
                            'key': 'ƛ΅ÃƟӏ4Ơ±ҐƜɌϩˊ\x9fɺЂòȱӼӪȷĦĞҝѡȚƫĆƭВ',
                            'value': '˂ɰ±_İĢ˥ďŃˏſȒêȥʴ2õѣͶ>ԘǼРƉѹΖŖЄɤȎ',
                        },
                    {
                            'key': '˝҂țŠκͼϝёɞ£ʊĵĕϋ΅ƌȜԢǯsҾ\x93ĊͲ5µύӾʄΙ',
                            'value': 'ΉkǜÖ*ϵȡʠνɼ¯Ƥӡ?҂ѺєԋƉӼЕ8ΧΘ>Ҋϐёǻƣ',
                        },
                    {
                            'key': 'ϸЕ\x8aƕǞȵďϯғơҖȽжҴǁѯѵ;°ƒӗɸЕŜ\x89ʹͼЛźџ',
                            'value': "¼ЮқҁȦԟȐϫЬƳ=ſӑÅѵӓCїɨʦѱǜ'ωӒöēӇЪ˼",
                        },
                    {
                            'key': 'ǆ\x81ŮįԉȓŚнiĹʇʄˈɍʲZǞoѼƏǟԧϘȮөUlĄǯν',
                            'value': 'ˡĞǊм\x86ŵǅѰ\x86üҺįЃųŝŗ\xa0ļьǺjïϦͱŴΚĜ_ưғ',
                        },
                    {
                            'key': 'үƉӘʥĈũÆǙ\x93±Ҧб°ǨԜčǽ\xa0ǚʐ˸ʳ˹įϚʬͰÀʤƥ',
                            'value': "ÅгŷŻƀ\u0381Ѩ\x97Œ҆ŤHеӫЯŕӬҾΜӊˁԫ'Ө˔ɯȒƅÜ\x86",
                        },
                    {
                            'key': 'ǥ.ҪӥЭŘĔȨнϕǛƽȼŖϧË»ȼƤƣÙôѨWưε',
                            'value': 'Ý3оĻԐΘŏàūҀУǭхϧţΘƣƴȹλĬΩǃƵϚìÞʺ˱Ԫ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': '҆éҮȽÉ',
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
                'ÐӲ˙҉\x96ˊ',
                'źԐӷϳƼŒҕƟþ',
                'Ӓτ\xa0zӟѶĜůЏɆԛ҇нӽёəЄԔ3ʱǪξ\x90ЍĺЯѳˁ\x88',
                'Ǹʈ',
            ],
            'event': {
                'target_id': '(.~ƒ`ǵPѬŁǡxͰυӡĐžòΦʝaɖäϦƚΣȖˆˈБ˔',
                'parameters': [
                    {
                            'key': 'ҴѵĹŞ\u0381Еİəǁ¿ѐ',
                            'value': 'ÞР˥ѬȵɯʰĢǺўѴ\x88ɰϴDɊʽɑŵćԧПUчѢ7½ΙŮĆ',
                        },
                    {
                            'key': 'ʼç3˲ɶJϓ\x82KɶҨК\u038bt˰ϭbŇÌЗȃϲ\x81ҷ`ŻδΝȷˎ',
                            'value': 'ӓŘ\x8bŖƛʊeҧɸƿÁ¡ȃ\u0378ǀbǊ3ѺǅӸ˙ǅ7ʎÐԧÍȗѷ',
                        },
                    {
                            'key': 'đǭӉȢј҉Ę˶æ>\x93хCŃ',
                            'value': 'р!Ö£ѸΪˀƬӜɣĤɆ\x96ΪʼfςĈ\xa0³żіżʭȫ\x83ŵƦǼφ',
                        },
                    {
                            'key': 'ҋʱƴĹìČǠÐ',
                            'value': 'ԣ˥љȉΜƐǕĹǍԅӆ϶ÎơМźҟ<аΞ7ÚΆƐ®ҰʺȌԀЋ',
                        },
                    {
                            'key': ';©ӊӢӋłPÆĀԑƼȫ4Ι\x9bԗCѭ˞ɟʷѲôŖȐɯ\u03a2Д˦ҧ',
                            'value': 'ʞʙĜӑØŵǷǷ,ӷDƵӔ˫Ѣ¯ӚȷčϛĸϐȊ˒ȼЈʓԊǩ#',
                        },
                    {
                            'key': 'зυłҪ\u038b˵ԮӞÐŮAɥ\x91фήƙ\x85ӘɹXìіͻөԐǎ=șԁ+',
                            'value': 'ɡϚ˧ǞǇҪƻӏˡѵ[ƣKËŮӑыӖ˾ƲĒˎϊÕ҇αҘv҃Ɔ',
                        },
                    {
                            'key': 'ýĈ<ņЎЕж8Вαy΅Л',
                            'value': 'ɦӥϛoÂɶǱƸӤʰǤ,ǺϝåǎцǮ\x8aѰɃΞɶӃǄ˯īˇ\x9aв',
                        },
                    {
                            'key': 'ɳĲ\\Ґԗтÿ΄Ϻˑ˵+ĝɠ±ӥʴϗŮʘкӁΥԔҵΝ˃Уһƶ',
                            'value': 'ȱΏʼXÜvģěϣуӌΣϹ\u0383mzĹư˷Ǵ¿ˤɗļ˝ǿÜ6ԇӅ',
                        },
                    {
                            'key': 'Ƃɉӭ7eŋЄ˷џǰ˼ԨʁӓϢ\x9c/ϵɭԢҘωgȪʀŐӰʬŢŹ',
                            'value': 'ț\x95ȇɖƍӊƞǏΣ˕Ǩ˟ΈǮԩʯБԓӑȹҗȞ\xa0ΊŧΆԃҠƲǩ',
                        },
                    {
                            'key': 'ΌъºǊҎͰǚĵʹɡэǋΌӯ£ɾРɀáЍÞԕŮҭϼҒȇȭγF',
                            'value': 'ʟԖΟõŒſŨЇ\x8bģŰɝĈΡТҬYǛĲĒ_ʌȎ\x9bġǲɽԩ˜Ɓ',
                        },
                ],
            },
            'comment': 'ƬеҎȕѬǲ\u0378œșҒĆ¦Β˩ɚɪXƝϠǜ˟ΗĬ˔ǷºҜϮ¨\x85',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'φ',
            ],

            'event': {
                'target_id': '˾ǈɺǎǈ',
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
                'ԗœƶҝԫʤΉΰtƠ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ɔʒƯѓɿ7ϗ\xadϘӟɗ°ɬũҫˤ˳ƍϺĆӝү\x8cҨơύ',
                            'Ϊ˲j\x8bȦʖʦōĭͳЍӲɖѳǇĢăÄ\x93ˣϼΆϜά\u0382(ˉ',
                            'ʷѓƜʅɤПɗ¡ɮ\u0382·ϢʗǺЌßϫĨ˂οȱ\x8cȱѮȁǬӷ',
                            'Ҥ˙ȿҍĦͷºҔŏɲ,ҰƖ*ӦǒяҐ\x94mͿŤɶŸǥɵёbk',
                            'ԗǳӥɭп˓ɠŊ',
                            'nҌқωɑïéƎŢȚǐӱɜȣΉ҆ɲ',
                            'ʛŧ\x8eҤɀƳШѱǸyɥǪӊԋ·ǈ',
                            'ԝǎǠҲȕ\x98',
                            'Аʪҗƽ',
                            'êȞαιӊγǒ¬жɴ',
                        ],
                    'event': {
                            'target_id': '\x8dҴͿÛϚğϩ\u03a2ƇСΏѮƷŀ*ˋÞ\x94\x91љ²҈·ҍӢʁӜД·ɐ',
                            'parameters': [
                                        {
                                                        'key': 'юнІsɖʑēȦѠ˾Ѝ ƇϴƉɥǥһǰҿʌ˘Üėϰŗµ\u0381ԭ·',
                                                        'value': 'ЧÂϧҸѻŭɃŃԁӮªɵö´ʷҙЯϒÉfӐɥ\x90ҨǾʿƎ҃Ʀғ',
                                                    },
                                        {
                                                        'key': '¡ƛѤʐĔǌĤσȵ',
                                                        'value': 'ėҸuΎήʭǏϋÕίȺΥϮ˵çͼ)ΐϻÝ҄Д\x96ϲө\x94җҡʮm',
                                                    },
                                        {
                                                        'key': 'ʂ˞Ӟ',
                                                        'value': '˳ȟʻӦ~дʥƶ^Ⱦǽ_èҍ˞ӹҞĽʩӍԭǞɲěψǎ°Ϥȭȝ',
                                                    },
                                        {
                                                        'key': 'ʅÝʻ\u0380ЌФɻӞȂǔʚ¯ŭ',
                                                        'value': 'ǟɛѰгŘ\x90ύҥ¡ћʍϒȵ\x99ɦĵǌŊǶǒɉɬϖř˴ѺȵÈʲҲ',
                                                    },
                                        {
                                                        'key': 'ϝʟϗʫôεúӣɯǺ',
                                                        'value': 'ΡǎǢύѴӫƟƅԈτ˞ΘîͼϽіǿˋω\x81˽Ǔϰiϧҍʵ\x8fьҹ',
                                                    },
                                        {
                                                        'key': 'ɔӻ˧ΆΩȣƸũÁ`ԐiͱȻҔїԅpГІҊХψθđ',
                                                        'value': 'ǟҳǦ΄ÞЮԘЌĿǓҏǳкӣΑϓ>ɫğȶʥ\x94ҕʋѪʆʀҨōѮ',
                                                    },
                                        {
                                                        'key': '¿ı\x82Ƥ[рӪϗδƑљϊĕáНʠǼϯ',
                                                        'value': 'ѣƕµӏ³ЉѯęϨͻϩέԅȺȤ˱҇ʥԇ˦\u0380ϫЂƨɕπʺҤȦ,',
                                                    },
                                        {
                                                        'key': 'ýʏӠʸț\x95÷ȷѥɔſƾǁźɟłȩȪȲЊŤyXʾ\x9bǕǦ˒җǭ',
                                                        'value': 'ıȀȲԏҭϨȶʤʍ\x8bӺШYFɿZŽěʢÈɽӂˈ\u0380ӘƞŴ¡×Ι',
                                                    },
                                        {
                                                        'key': '˷ԃȹʔԆĂɕgɹɍˏͺƾԃĚНȅȡ\x8fÝÛ&Љ§ˈҶҙ3Ӥˣ',
                                                        'value': 'гqԘӷɐǸíĻôфǺε"ŤŞòѨĮєƼчI\x82ԋʃŅҌйđS',
                                                    },
                                        {
                                                        'key': 'ƱόРìћɟ£ʸӍĉɻȢǇà˄ȻЍɕô˔ƆŜԝșӮÁԜƔͳŋ',
                                                        'value': 'ҚԎǒӜē¥ΙƣưʄłŖȄƦԜȵҘƱǭԗŞȴΉȉĆ\u0383ǪĈѨ;',
                                                    },
                                    ],
                        },
                    'comment': 'ν˽ĶӡÆɠѲˤƂƌʵ#wзȟѡ#Ǥη=Ԗ҂ȆӂЪŎ¬Ͳʸɘ',
                },
                {
                    'keys': [
                            'ȭĵ҉ŵɱŘԛ@Ɇ',
                            'ȣЪԩνɻʵҤ\x86\xadϕ',
                            'ŕʅӗǽҸ˙қƋřťʯǅĨӪԏI',
                            'жěΛ҂ҷʸϑɸȐwҕʉԓâԑəХø˺\xa0ƉƐΧŷǅѝĚ',
                            'ӄШ,юʹǟ\x96ЖņxƕԊЉсǻ_ԓyԕӚül',
                            'HЃ"ɓuƠȱɲǚ',
                            '¹ăâD҆ͱǓrˣŘºţʰɒĴҒҾ_ɣϘ',
                            'Ѫ»ɿHǶǡ',
                            '\x8bӸǜŜρĜӭǁҟԫČȶҷȥȿƆ˃ĳԘͳϏαő˩',
                            'Џюƾ˦ƺқǓӅɝԌ*ȔӋ£!',
                        ],
                    'event': {
                            'target_id': '\x8cıɬǎμLӮ1ːмуӪıʿƢƕ\x91ЊΘ\u0380ȭӍśûUķ˪ƱȆȭ',
                            'parameters': [
                                        {
                                                        'key': '\u03a2Mɭ˵ԊХáʄíΚýǢŰ4ʺ˂ӄΥʔ·ӶΟĒҥȐώӍĉĖˉ',
                                                        'value': 'QЌ\u0378Â\x9eϷƊΌĆÈ˛ӾtRѝ˪ʵǘŽү˭оӾwƥˁǈѕʰÿ',
                                                    },
                                        {
                                                        'key': 'ϗʙ˷ƷŘƤŚ©£',
                                                        'value': 'Ŀɇ,ҰĉNJηĳҙýaҍ\\ˎκƸǤʥΫÕéžȳф"εнʰP',
                                                    },
                                        {
                                                        'key': 'ѯȨϴҾ˫ь;ύǑЦMд\x80˵ȳΰΕѵ\x98ĠųΦνXԍɓΤƶɴҏ',
                                                        'value': 'НǯЙзӜŘCРKϛɶɪȸȥӌʤʢŒ\x97yґͲӦĻŜ§ѫ˕ƴҕ',
                                                    },
                                        {
                                                        'key': 'ЏνťłƝрȰɘɈ˯ӓҡϠ˟ŏσοԥı\x89\xadŝ\x84Ӯ·ь2ȿÂΨ',
                                                        'value': 'ʊԑΑ˴®γüűӦԬµTĝϒˬʄйԭ\x92ÄĎϤϙ\x97Ƹҋʗͽӯƙ',
                                                    },
                                        {
                                                        'key': '\x92ɘĄΛєƺƌӱГғţžǗîŋͲůҘİƌѧ·',
                                                        'value': 'ɮȠͻ˲ӻϠϥǊѦɖ¾ԎƲƺǟӷ\x8eɖÉ˂Ŋ·ΣϢӜʛƔàɺˑ',
                                                    },
                                        {
                                                        'key': 'ƌѷѢŖɔ#Ά<ƦʹРŵҵĶNǹΜQϝЮ¯ƥý\x90ʂͳǠԅԮ˚',
                                                        'value': 'Ǖŝ˳Ĺӗ:ӟɇʞϟͳ\u03a2ĠҝɫƇЋȻ\x9d\x80τǧŖ˓ʇźȲǠΆӂ',
                                                    },
                                        {
                                                        'key': 'ʥĀȡԋɔǮћƋҢΎq¥д\u0379˺˵ҧƖʪϛʞčɻπƒ\x93ɑΆ\x9aԜ',
                                                        'value': 'ǛīЃơӦ˭ӋdĴӑBҭѢӼŠĲ²Р˛qχǪ\xad˅ʹʟǮеλθ',
                                                    },
                                        {
                                                        'key': 'öĿ˨ʱ«ȿҴȾ/ΰπԙ`ΚƫˢфϠҝʥʑƮÍОδϾяʕâǬ',
                                                        'value': 'Ώѷƥ\x9fŗŶƺσǶ\x98ҕ=ӮƤjʷ\xa0ƕʔˍƀ¿˦ΫχǏǛҼ\x88Ɣ',
                                                    },
                                        {
                                                        'key': 'ʭΥ\x89εεφ³ƸŮΌȐþŪuɖÂʓřɹʌǛɩǉɵƱ|ȚˡɌɱ',
                                                        'value': 'ʺԥșʹŨȲɱхʋѱǃѩŏEěҾԃˌǼÚǨʧҩҧåВϗΎȸI',
                                                    },
                                        {
                                                        'key': 'ȅÌơͶήιӔƴϖ˄ϼΟĮѭҟĹõƜ¦aȈћ҉Ǩ]җӯѩĭ˶',
                                                        'value': 'ќ.ԑNнȹȵĎҲÙρʌӲµō',
                                                    },
                                    ],
                        },
                    'comment': '{ñӕ҆ѹ±ȇ҈uҝOДŢЗǞȯɁ/ϻƷΝȒ҄ȶʩʳîăŏ±',
                },
                {
                    'keys': [
                            'Ȟ\x8dĹҙ\x98ȀӍͷʸЌƕtѲƓCҖп\u0379ôʭßÝą',
                            'ѭŴѾѧĲǃ\x9dLѶ\x99îѝ¤',
                            'ʇ¡Оϴɭ҆δӫʘƘʫ\u0383ϡ»ÅÃÇ',
                            'ˇ˺ŕÝѤҖŞ\u0381ԢĥƏǟƍƮЕӧČͶϝň',
                            'їÖӮ',
                            'ЭʧӋΗԀȯ\x82ȭʴӨȞ1æΊœΊȝ˼A\x8cǡǬЉòȓ',
                            'ƅƷŠūǖÛщТbԇρˏĽԒôɫцӂӅ˹\x9eʚÒҞƬШǨ',
                            'ʟԖ˅ƊԫɧѝʛĖȃJEȣ¯ǔΟĚлР˦ȎaԇōɪθĀ',
                            'ͽƲѝѭѹӂ\x8eÆЊМ¡ĀʳӇαϷ[яƊɈƪЩȵˮԌʗѭ5',
                            'ΑҐ\x92ɉŉ',
                        ],
                    'event': {
                            'target_id': 'Ћԍ҃ƘȠұѬȒ<ÿɁcаŇȥbEΓBԆŚиŏͼԫXSӂɑʟ',
                            'parameters': [
                                        {
                                                        'key': 'ΰĒʿ˱ɪàÔΊЉ^$ҐņϴЕ˭ѧј´ˇE\u038bТЯƆΛ§ɮ҈˅',
                                                        'value': 'фʜǟť\x99ʰ\x84ǢƂφʂ\x90Ƿʗʕ˲к˘ώӭѮрфɷϏԨʨ\x903т',
                                                    },
                                        {
                                                        'key': 'Ȓʐũ˾ƈɪԈBű®ʗŬŉҒŞôɦƓ£ľ÷\x8fȋžǴȘϘöʂƉ',
                                                        'value': 'ĪȘɭҁɐÏƇԤ϶ƄƃãCӽȭӟǬżȡȱ°,йˉӭΐŌ˔Ўƃ',
                                                    },
                                        {
                                                        'key': 'Φι϶ʈЧ\x84ƞΔӪǘÉǳǒѫȲƍ¬ɾǏð£ӧȪƟϛd\x83Ġʖσ',
                                                        'value': '\xadˇËҨѰȳЦЩȆΦȥDɸƕЫPwũʵĀЕɪΈҗдѠ\u0383ɈӯR',
                                                    },
                                        {
                                                        'key': 'ϿʂƢӀѥѭâLԀǞԖŚƽԤɪӯ˔ˁŢиĲӱǞǸəƙЄ/Ƕ˾',
                                                        'value': 'ӒӫĜя˓˾ҊǝˆуǊâҪΛ£3wʁɵƠҍҷɎ\x8aҥƛ"Ǩt:',
                                                    },
                                        {
                                                        'key': 'ŧRΙĂфԁгϛ˹νRέōƷȔ¯ˀъ¾Âȗʕǃɓɔʿǃęӯǩ',
                                                        'value': 'ӶɓΡȤЗÐ)ĕ҃ˮʚŵɧĞûѱʬʉӍ6ćӬ˵ø\x8cƧ*/ǋʞ',
                                                    },
                                        {
                                                        'key': 'āҾĤ¹ЪŞɍ˥ŃɱƟԮр˭ ϐTɜ¸ùϫǬŶȣǅĘϪɿ0Ӥ',
                                                        'value': 'ËkȬЗ]˴ǢɑҰҊҷġȿʼ˛ʗąŞΤưĔɼûɽκũɕцȅŬ',
                                                    },
                                        {
                                                        'key': 'ɣ~ŞĜąзëÀƄͶѳӉԧȅѮBѬѨ¥ЎÂΛӒƽЮтŎöќƟ',
                                                        'value': '¹2;ȘƑƘ˺τ°ҵʎӇӘ·ųĴҳƽΑˬϹ¾ìÚГʺŜőͻĐ',
                                                    },
                                        {
                                                        'key': 'җҋǁ˘ɘśҳ\x95ǣńɸàȠƳÃ;ӥġßϝEɹӤЅҊÎ҂Qŋ\x9e',
                                                        'value': 'Ś\x9dųʙʷσž\x8aҔūǥ˰ĳƇ:ȸ¼Ǘӿҍѡ7`˛ˊΪSc°˄',
                                                    },
                                        {
                                                        'key': 'ƺ\x91šяȁҠѦ\x95ɛïϷËӒƜȴ$ĒêξͺɯÂȿӋǞíȕ¥ԫί',
                                                        'value': '%љÃǆʅȺϧѼŋ|\x81\x8fϰÐ΄èȓʽӔӅʢι\x97ÿȅɑƽҧñĻ',
                                                    },
                                        {
                                                        'key': 'Ϋ+ďΣɮȆүƁ|ǟYŊ˙íҐ˕ßϧˬʷăïʀ˛',
                                                        'value': "ҫ1.ĔŌƊĢ'Ɛ\x84йӤӚϸȠ\x8bсȜћʮΰ˰˹ü~ƨǾιџƨ",
                                                    },
                                    ],
                        },
                    'comment': '·ΔǅњΛѬȜƁӂʅċϺ¾ĕ\x83ʺɴMìǞĦ3ªǟĥХgĻSЙ',
                },
                {
                    'keys': [
                            'ӡάη¸ÐǴσȇ',
                            '\u0382Ϲ',
                            'ž',
                            '˥£ҦɀϴаϓĹµӹŤΊΙǬǐӜtЊȘĂǴÇҖŇ\x84ϗ',
                            'ҞϙðΊ¾ˮҀŶ',
                            'ӤчŮƩʬĶĶǉöƫNǷһƕˇҾȢəүφśȟƙʯʘȌȄ',
                            'Ǟɾˎѻ˵Ļ˟Ɗѥ¿ɢŮͱ',
                            'ɡɍҏ',
                        ],
                    'event': {
                            'target_id': 'өŐӼԏeƻơѫʃɂ·НwΆϺİƳԒнɴȄύǌŦπˬӖӶԦʆ',
                            'parameters': [
                                        {
                                                        'key': 'űϽӿѦϫӭ',
                                                        'value': 'ͶƵѥҴcƜɅӆОô\x91с}ɑŌʓҢlϲнÑҒӿђӞ_ҙϨZɏ',
                                                    },
                                        {
                                                        'key': 'ϣсɽÁ<ȨӪσlô\x89ǤǉӪǜǱɛЇʽƳ¥µ',
                                                        'value': 'ɷҲ_ёӟưŊнҨϟłÌфӜąΥƹОȐħңϢĥȸǻ\x9bԜű¶ɱ',
                                                    },
                                        {
                                                        'key': 'ĕµŐȘƐҘɕŚʡԃʿĽ˷Ѕ÷фыɲ+ΪȍҒı&ƛCѰѐӖ\xad',
                                                        'value': 'ΑǜүΠΘɍγɚжƆћӴҌӱʷͶ҅ӶƣęѶϸ*:āŀɕġĊɹ',
                                                    },
                                        {
                                                        'key': 'ΜԙɅϚÏəƘxľıʫћЬѾΒ˾Ɍ\x87ŴĔɣ~ťʪŪėƑEǟͳ',
                                                        'value': 'ƀŚϼƉˇΗiſ϶ǧǦ³ŮʾɯѲ˭\x85RΨԀƔˏŹШϓϺʐŶħ',
                                                    },
                                        {
                                                        'key': '²ɴȽҎȼѪàÏʤĝǞóūͷËΔʪɿƳǺų',
                                                        'value': '\x8fωίȕƍûʢбƕ\x9dЮïƸԑϫ˳ҔӄԀ§çĪòQϥфi\x89Ġv',
                                                    },
                                        {
                                                        'key': 'ӘĵѦŭτǵʃфϔG9ʉўǌϿѹь\x9e\x82°ʯĕӆԏѿ)´әIȐ',
                                                        'value': 'Π˟ӓȺɷYԨǞȭ|.ҦĿŉǯЍŀÑӉҿ\x84ǏͿͿϦƘáĒҮT',
                                                    },
                                        {
                                                        'key': 'ļɌǄфũΞɣςͺУфϳ<ʇ\u0381ѧΣ˕\u0381Ы¨XІÀǰӝàÓӠҤ',
                                                        'value': '/úҚ¢ώʜ_,ӓăŸ´ϛāƯɛӓԭSĆʜďôґŞĭΦǡʊɛ',
                                                    },
                                        {
                                                        'key': 'ϒΤʵǺĐ(ѩǥөǫȾ˅PuĩȟԑŨÍnɮrήыƓ@ėԢʖǎ',
                                                        'value': 'ĉìʝԕʭЩώӀ˛ƧɬЍR¥ғ\x89·Ǜϥã9ϓŔʇʊ\x85ì\x99ʌʴ',
                                                    },
                                        {
                                                        'key': 'ԥН˚ѳЈďƦ˦Βѩ˄ɗɥėfӆŉ҂¡ԇȋ³ƒө\x97ЊǀŮĔ˻',
                                                        'value': 'ϾΐɸϿ˴ЌΛŶҞԇ3ϦΚʗÀʠȂƘ=ĥɻÁ\x84ԙыҾ˛Ũ҉A',
                                                    },
                                        {
                                                        'key': 'ԐΒҖüǎĔʺŹєΐĵîҟξѽȜқЭ',
                                                        'value': 'ŦѦśɣИȓϵķӮȒОӞӫ˹ơȾʳDƺӰʜϑƢӆόʱŻџM˛',
                                                    },
                                    ],
                        },
                    'comment': '\x8aȋď\x90șȧŅϤǲбƮӊІòҬ+ƷΔƙ҄ŹҧӬͳ\\\x85Ûҕӊ˃',
                },
                {
                    'keys': [
                            'ȍÄƪΦҠԋĄϡ\x9bȻͿƩ',
                            'ŧÓ~½ԫǳˏӇǝУҵҬǘōԈ9ˋâdԖӓϽсª·Ŕ',
                            'з\x9fΟҁʸǳѫɇƖʂш»ͺϦŧӯϋʭɬǃѴвƧ˴«°ήȺ',
                            'ˬÆŐɄҋ',
                            'ЅѠKƛ%ʛҠġԪƋƧ',
                            'ƀkʖҊŋɓƅ`иĻÁҶɭΰЛҸ',
                            'ԘƑ\x89ŧȘҧʐʗľŚơ¼õόȻ\x95ωԂǥǨƺˡ',
                            'ǒ˫μқˇВӓҊѰѻȢ\x95Ԯ\x85ϼʟΑӅ¤Œ˴˹0ԝӟРϻȪҰɕ',
                            'ëŶǞ\u0383\x7f1ɸύѮҺĶɸϕ¡ұȕʰ[Š',
                            '҆˜ʞŪiП\x94ĄĸěɑƑœɏ>ƕЫ\x87ƿиʯϫɺѰÿÀӚğ',
                        ],
                    'event': {
                            'target_id': 'қ`Ĕͼǖтѱӵǭερͷ\u0383ϰŽїŉǘƓНϰΚ1ΤƶͰһҨŚ˳',
                            'parameters': [
                                        {
                                                        'key': 'ƽӶ',
                                                        'value': '˒ΙģҼˊȄҟγ]ʝ½ԇȩʤʵɊғŶŃƜ×UëƷģϡԝԜӊЛ',
                                                    },
                                        {
                                                        'key': 'ӥÆЏŽıęҊ˜˦Ѧɕ',
                                                        'value': 'ơɄјͼɵҊԈɭɒʒԗɲэШȓԏӦ\x98QĎʷMŻɍСϨϧιĉÂ',
                                                    },
                                        {
                                                        'key': 'ӝͶӨ¿ͷő҆FѯʙĿѶψǈƸįԠϼϮǷ,ϋζԔÂȓĆŬǧӰ',
                                                        'value': 'óͻ\x99\xadƷɮ©ĝШɞĥѾӶĐ˕7ΫʔСΟʾνԡŢǡ҅Ƨʆɀɥ',
                                                    },
                                        {
                                                        'key': 'ԡ˄ÓԇĖÆį\x96ԈːϓŨ҈Őӂ҉˱r«\x99',
                                                        'value': 'ȩϦúÊƢX\\˃ĜvӭĲʃƴ˰ԟщΨ\x99ćѲĪ˗_öȲѠϟƹŹ',
                                                    },
                                        {
                                                        'key': 'ɷѳ>ɶ{4ǫËʕˡЂ¢ǟЀ\x96ɣёɢđκωɛ?υϔǽǦ±Ƭҳ',
                                                        'value': 'KәӲĚĵ\x98ŃҥƊȯüɤd˛ƨǺÒԥ¥Ġ҄ӌ\x8bԇåɨſЌǱһ',
                                                    },
                                        {
                                                        'key': ';ғɻДĿǍҪǧƷŴԛӚϺΌyʞǅʲӸȯϡѩŐɫ\x8chþˊԔȴ',
                                                        'value': 'Ŋӻ\x8eő·ɵѲŐĎрƆɂɁÙǹŁǇӗƜěŗԣēʁΟUʾ¸¥\x8c',
                                                    },
                                        {
                                                        'key': '˯]ԮòǍɋǌ\u0381ӱȕ³\x88ŘιȊΦÌç ɉǸˠ͵ӂәВăΖɝҫ',
                                                        'value': 'ʷЙҘǊĎ\x80 ȊМƑϋҭтԊƼҗɺӁǶɉȄяqÍˀɍΰєГĮ',
                                                    },
                                        {
                                                        'key': 'ǵɁƋӒϜȩ\xadӠˉÚǋҜЏvČƣЕɼǅʼϣɰԟҋę$҄',
                                                        'value': 'иǒp˃΅Ϳ˙ӈǒȟɅÂηίɥѩñÏʱҜɤϯѮɮЙӱȓƂɱһ',
                                                    },
                                        {
                                                        'key': '҄Җƶ\\',
                                                        'value': 'ɶȬғZĔЎˏΤƥɡǩͲԑŊƠ˲ǜήԖ·\x8eԮҗˡķҝņɹΏ ',
                                                    },
                                        {
                                                        'key': 'ӔJèŜŵá;Њ\x86˺Κʾ¾ģ˦ӌˆơҗƵÄүΎРâǅЗ˹Ѻ',
                                                        'value': '˦ɀ\x87ɁӁəȌŋc˰µʲɛɑˉΏБʢɇɫӗʟԜͶў\x8fʫʦЇB',
                                                    },
                                    ],
                        },
                    'comment': 'ԏĚʊʇʗ\x92θҧʄâӘљȑω˻ѯԆƉςʙԛˈa\x8eԮɦɽѹøѠ',
                },
                {
                    'keys': [
                            '˃\x81Ȗ\u0378·ƉȅÒŢˇ϶\x8fá',
                            'ʞӋʑ˕ӋÔĚϔǣ?ҀʕǒȒԈдѩèĥ΅xĵƭ\x86ҢĦʻ©ɶǷ',
                            'ʪӢŽ¶ɌдơnțɒÈĬƢѥшȸҞ˅Ͳ¼',
                            'Γ',
                            'π\u0380»&҈Βʈ϶ʸ˜$ʫЎтɅΫʝǘʆӀϠƈŸЉѫ',
                            'ӪДȇԋΣǆФ',
                            'ÎʜʙɤĠϥЊŽӽêĆˍ҉ѡСԜzɒŶвЗӑƱҐűϖȻ',
                        ],
                    'event': {
                            'target_id': 'Ȃ҂¬ƞюǕʧ6´ԙɴ\x84ĻǊƛđŸэɉǉѼϭϭQōˁ҅ǉɆƷ',
                            'parameters': [
                                        {
                                                        'key': 'ǂǎõýϚʊ¬ːԉťӢ/Ȏ˜ġɔąȕѷϐϧʹʬ!ЫӫӦƑ÷ʧ',
                                                        'value': 'ȵяϚ˂ÏȒϠʺ¡ԠƇϧҾ˼ќƒTģħjΥ˒ћğ\x926ɟԊ˹ɘ',
                                                    },
                                    ],
                        },
                    'comment': 'ĦϪǅĊάʑŰǴłŖ7j\xa0Ωɀ˱ŻˋНΚ΄Λн˚ͿʀӘɜОĻ',
                },
                {
                    'keys': [
                            'ԃɱļǐҼǺĭȣӞҍŬÐӽύӷ«ǅ',
                            'țˈΑ>ҩmѠĶÂ',
                            'ҜÇƶԩȽŻʋ˷ËԞƄɦҞ}иyǣҤΓʾҟȘӧѹƤ[ċ҃өѽ',
                        ],
                    'event': {
                            'target_id': 'ȟʾ\x9d˵ϝʘ¶Ԣ˰Ɉɜχӭ\u0382ѰėAPɘ»ƨӞΟԊԧǃ²ƕЃż',
                            'parameters': [
                                        {
                                                        'key': 'СˎʔϜǚȒǂĳϱ',
                                                        'value': 'τтӝͱɤф°ŹκЙƳ\x9eҷÌæϤƊɴɢʯϦƕӕԞӾ˳ӤТʱŋ',
                                                    },
                                        {
                                                        'key': 'ľҢŚħĩХЏͼӻӞСʷå\x96ȷ\xadŐŷɰѺÌϴԜȪʀŎņуʯϴ',
                                                        'value': 'Ǖө\x9fΛҶɼϒό\x9eĞΜƤϧΒˁōҞ˰ʂƉOŭ˶ÞǆǹPЌΕǊ',
                                                    },
                                        {
                                                        'key': 'ķќϞŕƒŽΜȉɎĠˠʐƌͼΉԙ\x86ӍłïŉӱȼĈӊ7Ыbψy',
                                                        'value': 'ѣpпџçvȤԍԪɨɫʾˀ\x99ЏŗȦŧӤѼNξƻπψуVȽGЦ',
                                                    },
                                        {
                                                        'key': 'ΩʏȘʎЉÔв°ɲɝɮBÐԈҞòҲǪȧϏƺ\x9fäϔÄǟŊčѺɯ',
                                                        'value': 'Ā²ŜgίĺӒȝFҿȶҹȭŽн\x96ЁɇҧàǓșԠҊфǦтϘdɀ',
                                                    },
                                        {
                                                        'key': "Ŧ÷'ǟŜ\x94ϧȐδ¨ɉĮ\x97ȶӭŜϰѳɍ˚ŔРӊʠӤƪʡԊҎZ",
                                                        'value': 'ɮ\x88ԫ{aȦuƘӄӮ¼ǯ҆ŖӇ˩ӴRҭʉɱΖњӘ϶ˤíýΑɛ',
                                                    },
                                        {
                                                        'key': 'ɕȂΫȀҖҵӰʨΑōˊơýѥwţʱʮȀӧʽҘÆĻâ°ȽŅʤϾ',
                                                        'value': 'ҖĽ@ɸňʇƥɞǀԭǗŮ·ƤĘσͼ\x94ГЌΛЫ\xadƣ.\x89^ʣɔѐ',
                                                    },
                                        {
                                                        'key': 'ιȊõĝϱΙɁ˱^ѬͱǂåƎʮɏњŃŋҢvȐdіЄʵʭÀŦŉ',
                                                        'value': 'ĺˢӑɴҒΆъ˒Ǎ\u0382ͽɤУ:ĂĹʱʁÜÞɃѫӄòĤÛȣԪĲʺ',
                                                    },
                                        {
                                                        'key': 'ĩωŔƹȏłԢѩη˵',
                                                        'value': 'ơԛǣȱɘVѦƛӦʘΐˆˀǃ\x9fЗǃ\x83\x9eԫ˂ʈɚЕ˔ȩьà\x9fќ',
                                                    },
                                        {
                                                        'key': 'ĔǩтɼȪRǩлΑȗƛҔcˋ5·ǈħюʢ˽;ƢVƕЉȭӵɎʒ',
                                                        'value': '\x96ΗƇǲԝɩԎωèʬÎ˺vΒ×ūԏȞĻƀυ"ҋØˀńöʒʫ\x99',
                                                    },
                                        {
                                                        'key': 'ԓ©шȇĪŕьψƯʓϧąǸƦ˘Ѡ*ǗŊыQΏѨľɞħǐĿŧǺ',
                                                        'value': 'пtɓĴʲԠ½tƠͰÿɢņНnԌņNɣ!ΣЦРЏʊȦɗûǲȵ',
                                                    },
                                    ],
                        },
                    'comment': 'ҢʔǡюҳʜʮΐĮjЇǚԜκ҈ʹǐʹΆÉѳȇȧӿӓʙȖ\x92Шґ',
                },
                {
                    'keys': [
                            '(Ɨ˓ɹʸƁȷɪÁȀȿʍŗ\x91Ψ_',
                            'ơҀȇϦӣπŲȌяѩӅȏӲ',
                            'ȣȧйǀҹмӨзŇө[ȋ',
                            'ûϽуɛŨƀːңÃßұҽϒЭËĩÛØɣЎB\x9fГ',
                            'ѫ˜ɹҮҭϲ\\ϖÔȓĒ»',
                            'ϛǯ8;˻ǩwʢϵˑ',
                            '\x9dӠӪĻ˽÷śͳ',
                            'ʮZƟǑŹԭіʶƯωħóÉӯϸ\x9fɗ˛Ά˔Čĉђɡҝ',
                            'ѤϿÖʕʜǆԊ',
                            'ˇТӧíӓԧŬѱ!',
                        ],
                    'event': {
                            'target_id': 'ѫȤĭţћӏĞñқïϓγAғʡҨĂǰǯ|Ϙûɸ¿щĒԮNѺŃ',
                            'parameters': [
                                        {
                                                        'key': 'ѷˑͰҳAʆʀФȟĐķǮL˄љÊŶϐPͽӭψЈѲɜű',
                                                        'value': 'ÜŇѓƃԈć҅ʭŢΕэ˲ɘɪϊȰ˟ɩ±\x86ΞѪȟǬɥσԩ˯,ʨ',
                                                    },
                                        {
                                                        'key': '£өѕРʗϻг3ľό',
                                                        'value': 'ĐӽħҀŚøŇιуͶαӂҔ#S\x96Ԭqʐë4ÍȗnıԨĭБωӕ',
                                                    },
                                        {
                                                        'key': 'ЭĤpɸøǴЯФĞ˫ǎӚɉе˛ҠŲİ²ɼŠ)ȋŬӌģRǆɠя',
                                                        'value': 'Ė¦^ɐϏ\x95ɍЄYќ\x9dλȽθīřʑʷϬǼЛ˸҈Ӈ',
                                                    },
                                        {
                                                        'key': '\x9eӆʺп\u0381ќ˛ЏοɵɒʐԂ3đ',
                                                        'value': 'αȀӼğҔӠҘҤęљľĕɿҲӸ1ѥ˖ȔӝφҶѪӸǛϤú\x81ȩӺ',
                                                    },
                                        {
                                                        'key': 'Ҧp!яϨѲŃ°ùñ҈Ϻ¦Ͱ˹5Ң˳˛ɏɪǼ',
                                                        'value': 'ˎˀəϟʠ·҇ŕсģӂδ1δԧŞğċª\x9bĻ\x9cɑϳȇМЯäˉԗ',
                                                    },
                                        {
                                                        'key': 'Ӄϳ\x94ͼ˥ǔų\x88Ϩuɾ\u0383ƛѬ\x98ү\x92϶ý˶ҫԤжŚҘԇӤѸ6Ѵ',
                                                        'value': 'Ğ҅zžāŰ%ͼр\u0382ӳȞ«ǃа\x81Ѷȥƍɍȇŵћ_ɒΔˀ¨\x91 ',
                                                    },
                                        {
                                                        'key': 'ӠȝȏƪӧƈѲɨĆļƯʂ',
                                                        'value': 'ΘД|JţɎǬҸƔö~WŸǋǣДá҉ҞżˮâϻДǚѤӔԥÞî',
                                                    },
                                        {
                                                        'key': 'ʎϟ',
                                                        'value': 'ŭҥÜÚҊwʀñήF ѺƳҰĒʘʤĂɅѤнϠ?ĵͲ˵>Ϻн6',
                                                    },
                                        {
                                                        'key': 'ųȴΕ҂ƙɟҏќрĔϛǌѼжǣϩлĤșŋҞ\xa0¸˽ξаʧϰǠĀ',
                                                        'value': 'ǶҨӆҟӌȎлԔѤӅԥΏӉĔŇǅšʱԔЊʊqμ˛ɛ>ȻȲŵǍ',
                                                    },
                                        {
                                                        'key': 'ɿԊШΤųŎʔԛӄƨŊԨȦǌ½ԕϠѲŶӲ¹ʩɫyр\u0378ľȯэŷ',
                                                        'value': 'Ĩț',
                                                    },
                                    ],
                        },
                    'comment': 'ʰÀ˴ŤӱÐǘũ˕ǋ®ГɆǸҀɝȟȜзΐQѻҎɊԏʐƏ\x9eңď',
                },
                {
                    'keys': [
                            'ϚӰƍíҷǂԂ˻2ыϠÓΘɘżǀүɢâǴȔȜӴĨҁǗ',
                            'ђӮЃӠ϶',
                            'ĊÉ϶J˯ŒԎœйѽԛΓù2ƞĴŝӃϦ',
                            '҅ΰȬʕǉɌӼ˅ĥ£ϔƇ×ѳʗɷ',
                            '˰Ӛԕɕ¯ӟӛŲϗʎȳŵҝ˪ӷˆ˴',
                            'oїԀ_ѲԚ^ӍɥȎɧɛȠʕſť\x9eɉԄĀǮðēǏԩОȻ',
                            'ӵҗɼ',
                            'Ԃʼ2ōÜ˦Ә&ŅμȨӵÈ«ӹАƯ¨ðŊԌӋ΄ԡд',
                            'Ư.˶|Δ҉',
                            'īϾǩŎΝȟԛ\x97',
                        ],
                    'event': {
                            'target_id': 'ĈŘŝӍřƏǡ˜Ƭ çӓɞǥхƭҵԓƌĕҏƃπ«ϭtС_ÌΖ',
                            'parameters': [
                                        {
                                                        'key': '^\u038dČШҫd;ʶņǁԋǠˈΨɑ\x93ԡҧĨԧÚŎϿŏϷBĜԡԘю',
                                                        'value': 'ĻƠѡȊ϶Ų¿ң˼кӤ˄ЪbƅoӚԁ:сŤЗΗkɎǎǊăɂg',
                                                    },
                                        {
                                                        'key': 'Ë%ǳͺЧίЗȁ\u0381ԀƒЙɫ[ɽÙѫЋΈҵhǮuѲˇƛПÒҙʠ',
                                                        'value': 'ΤЉďɿҗƇѰӮϥʃ˔ҊȢ˭ǚҐm\x92ɋԫСϼ˝ĭ˨ŪԒӘƘ«',
                                                    },
                                        {
                                                        'key': 'Ɯ-ƺuӿңûǷПɂŮ4šӒ¾ƹϱȓѴwɭԜǇӼɓƦȤʏƙЊ',
                                                        'value': 'ʓəƈƱҏЉȃҙНȱœʖΤшĂηɉ˜ȱӆϥȔʮɏБ0ΫãËǠ',
                                                    },
                                        {
                                                        'key': 'ý«ϪƎ˴\u0383Ʋɥ3ȭɪԘnΤҡȡǋНQĹӈŭѓɛƭ\u0379ƑɂʛԄ',
                                                        'value': '˚ΧƠƹϥ"ҲƷʙˡɛɖґęŢɠþɳƠеҍʹʈ˥\x98Ʌȩ.Z˕',
                                                    },
                                        {
                                                        'key': 'ϓԕɣą0',
                                                        'value': '҅²\x8fВʑнéҁѹaίѩȈˮƹƄȕђͼǜѽѕӴΰĢãϫœȿũ',
                                                    },
                                        {
                                                        'key': 'ɣ3Ğф\x8aεҼ˩Ҋҧŋ¼ӝĚǖďԁɘɇԜwԢ©ĠˮʥĶԜȥɀ',
                                                        'value': 'ҠĝѯŪʧγEɭǨßƸϧʟӭǞ9Ł҆ǛˢǰͲȬ³ȧ˺ӒѾǝϕ',
                                                    },
                                        {
                                                        'key': 'ЙīβԪíɸԮηϪɇȂÇӲƚ$ѠżǌŜԘу˘ʗӵćɠӸԞȝŏ',
                                                        'value': 'ƲѷɾУƬӗșˎжВǡűiěӶȼԁôÇΆŽ˝ϡԈЧqќˉȴĕ',
                                                    },
                                        {
                                                        'key': 'ʆȑǩˋԟЊƖ\x9cԍҺӄ]¢ôŷѤÀ"ЏыwŚóњлξԃ˖Ѷӎ',
                                                        'value': 'Δñ¡§ǾƍӉǼπΝПѹѯҪȽ¢ҡŗ\x97ӶҮӅ\u0382ɴҘ ʖ%ŶB',
                                                    },
                                        {
                                                        'key': 'ģƼʞѧǹ\x8dН\x8bđƫ{ͱŖηʴ\x8fǅ"ɑǼѼ\u0383ʹȘȬȒԜőдƺ',
                                                        'value': 'ƞǿήԜũ\x8dùçùϡ\x87¯ʠκȝ©ͶƉȽʇɒÌμˆӕӄžΙЧĔ',
                                                    },
                                        {
                                                        'key': 'ШĩОǟпȦ˄ű¯¹>ЇĭĠаҜ˙ԗĨјӺǷӤ҉ƶҶĹόYџ',
                                                        'value': 'ϊƤė˹ҀÎ˵ȨưгΉXYĈ\x87ɂͽš¶4ǘϰҖʃӐƋʈšrӅ',
                                                    },
                                    ],
                        },
                    'comment': 'ýԪϊǭ÷;ɚИѓҗгԐȝ¨Ԑ҈ҖËϏѕŝˢԇҹ˝Ŝƽбԣƌ',
                },
                {
                    'keys': [
                            'ƷԤͼӝ΄ҵǮȚʒɴӑ',
                            '1Щ^șJ¸ʤтЪİʗɶ',
                            'ǘȗ˞ʎˆј˓\x86ÙˁҦΐЅĆſҾԁӹȃԖԘ\x8bŏ',
                            'd\u0379A',
                            'ԃʷµѺɲơFŴ\x9cǻӝ˴ΦʺΛ§ҖћсΠŪ\x9aӱ',
                            'ůΣƦӠªҹŧĐԈυɺͱӆ˭ϲˈċҎ2',
                            'ƞȚёЃ\x8eơÞҪӊɒȔϽͰâåӱ',
                            'ľͱϏϝИԀδʱϿλʅ',
                            'ьʮǱ¤ЀŬӰ',
                            'ǡӛȞǋɚģΗsЊѾϕĵŲbǴ',
                        ],
                    'event': {
                            'target_id': 'ù˾Ӏӫˆԍ*ФϢɋʸӵӷý˗ϛÝİ˃nӅĖȅһхˁ*ϐȆʆ',
                            'parameters': [
                                        {
                                                        'key': 'KǖȴҟǵŮŬϩİ˷6űȇʸşԠťӁ\u0382ʯŒ\x81˼ȾԓŵʡϑщȄ',
                                                        'value': 'πκ˂ХʦʨʅΐĮΫң²ſʌ]EʐɅŤͽɧ~˄ʰɵʍĆӊӑʭ',
                                                    },
                                        {
                                                        'key': '`Ϭ°ǂеԥvΛŐӴɑ˪ɨǛϚ]ӈԇȢŤг`ϚŀԛÆ\x7f¢Ā\x7f',
                                                        'value': 'Ɨƶ#әƲ\x93ƋӺųƺʫÁņĿOÛ¦ʤȻ×ʯȅ×ĝŷƹ¾Ѻιӟ',
                                                    },
                                        {
                                                        'key': '˦ѧ˸Ȧ³ýÆɾʶ3ʨҞȡϸēХ,ϞӳґΘѕ˥ɯ.ĦɶˆΤƌ',
                                                        'value': 'Ē˄:ҽΐĢхÀГ\u0381ʨǙŰƠѴuӅǿȵTљƴŃЗʦü\x86Ȍ:О',
                                                    },
                                        {
                                                        'key': 'ͽzԬɴȎȶϗҵԛҡɒѡUѠĬfӅ»ˮ¡ŔШĶǄ(ĠЖ\x90jI',
                                                        'value': '¼҈ӈħԭ˷ȴƻӂĪѢǷǴҷăӰ\x89ϩЙƖчƂ\u0379țӧ\x94Ƙȓ˭4',
                                                    },
                                        {
                                                        'key': 'кƨƝϚŕ\x84ȼƯǦƵǿІò˭ŧӴ˰ǿ_˯˅\x9dǨҖƕ\xa0į˜ĺĚ',
                                                        'value': '\x84)˛íºҊԚГϣåԭļĜξˀЉʃŚƓɏϽƃȶǝȯþȨͱˇʬ',
                                                    },
                                        {
                                                        'key': 'xРӿǵԤʘɏƢοΦPSӵȨɌМ˜ΐˬҞ\x91Ăη8ҫɭӵĄǥ˩',
                                                        'value': 'яϽt\u0378ʸнęJπӊ@ЯƳψŸïˀʛˑңӴʔү\x91ŤɽӝƗ©ɘ',
                                                    },
                                        {
                                                        'key': 'ӒͿ¶ʎ\x9cӷɂȴӋǬˀ',
                                                        'value': 'ɡƞѣӄюϿéİɩӅΧ\x89[Χ{\x80ɿǺӘǉȃʯĢԌǴЍѳoɪ^',
                                                    },
                                        {
                                                        'key': 'ΛʿÃџǉʌԙх¢ɎœɡŠŅƯԨϜԀȅȂ"øҍɺ:Ԯ\x9dӋˁѴ',
                                                        'value': 'ӅЭÂрѐҰιɲΌӭΚŰơ[Ț3įƿϓũԤƩƋʽɻҗБѝϿ˩',
                                                    },
                                        {
                                                        'key': 'ΨҙΈ\x94÷ғҸӴϢăʴȤНÒϒѝΞɘƚ\x8bȗϟмĝƞӰǯÉ6Ȇ',
                                                        'value': 'pǆɞйƛŢԅӛ˅¾ϴ˦ˬκ\x95гʎžƧɝYƱѳҏ,ĺѝĉόғ',
                                                    },
                                        {
                                                        'key': 'ʽȎѷӭѥɼś;ɬ±˷ɀĤüʸћƧǟøŽΒ\x80ΕŲĹѬ¬ӕʢώ',
                                                        'value': 'ɘɍŀȊΥȈŶ ѨĜƭʈɧҦŎӋʔƬљÅћҋåТԖБҪжĥӲ',
                                                    },
                                    ],
                        },
                    'comment': 'Ʒ˒ēˡӖēÜƔĮ_бԣϟȪɴӒ¼ǛƇȵӀ\x91˗ӌͶǂέӷCɻ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'master_sequence': [
                'q',
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
            'name': 'ǑƕɣϔÖéǌдѨʮĥͻȨʥåԟjѾўԕБˎώӹd˟ʴЄ9р',
            'description': 'ŹōӞĦТ]¸ʨѱʦǶҗƈ¹ƳRȩZы˦ğɱȖűŖȀȄӍ\x95Ο',
            'target_id': 'ǥs\x96ЊӠȦΚ´ïŏ˫ǇОӶȚĒ0\x9cәҔαԬƊ¸ΉȡЬ\x84ɕɁ',
            'parameters': [
                {
                    'key': 'ΦɝÒȨϸ\x9dиƷˤņ«ÃȉˑÊïԨ˕Tê1φJɓr·ƏїъЇ',
                    'description': 'τʻSƞȧѤ˭ŅÁΏѮLǖԭǪшϺȦІʡ\x8eǗªʈ}ӱʌϳɈƁ',
                    'default_value': 'ʡԂЃİˎzɩŴĚǏʑ©Ŧǡ˙ƭѷ\u0378ǥÓͼєɕҔ΅˝īǫàϺ',
                },
                {
                    'key': 'ǈˊϩҒɋaŏƖˡӘχl2tY',
                    'description': 'ҙƨ¥Ϳwŝaņƞ˧ӺѤџˉӾȘϣӳ½ɝ˫ƩkȌǡĩɨɴԒ²',
                    'default_value': 'ȎΜĐŉΉÃΫǆѶƈμ˸ҳƐ°ǈɉxҮFʂȺeΜɚ\u038dÅ˜½ɶ',
                },
                {
                    'key': 'Ɵ˔¢ЬϕǗíЀǰϡѮȅқôˑͷίʁĩȠĺӒΎÏϖǏˬԞˇϹ',
                    'description': 'ϰІƮЧƜşXϰʯϩϫɲƨÈԆȔƞΘȀԄϒeļ«ʠҪаʞǥǀ',
                    'default_value': 'υȗ˖ƍũΧȿ¯ûÐƯκԋёԠҒȃKˮx˨ƪӫwɆϊ¾6Ņʢ',
                },
                {
                    'key': 'Яғϱ˩öҪ˨ѨĹһŜŽКʠƩǩ>оĦӘͿӮӽkӨ³˧ɼЗƇ',
                    'description': "ŌЉƻ\x87ΰ8+Ȩĥҽė\x9dӇɅÜÅä¢'Ҍ\x89»ȴĀǇȲΓԮʩή",
                    'default_value': 'ƢˡÕʸʙσ˻Ŋі˛ɶԕǒ8Ԙ˧ӯƧЙӑÑǹзʲёʵөΖҢӶ',
                },
                {
                    'key': 'ɿҾþˈŠƧȸЎʰÉȲƷӕΈљđȏǴѐɮǴǭˋ˚γ¬Ԃęǹѽ',
                    'description': 'śιǒ"Р ǩŌҖđəÿǌӋŃƁѯˋɧìӮыˠԬʐԄҫӷEĀ',
                    'default_value': 'ѿ¯ŋԙԑǹɡǈ\u0382ѵљҫƼѩęP!ǊΖǗ˽ҝ#˽˪ѯŧƖþɭ',
                },
                {
                    'key': 'ƓÃŪà҆çЪϦʼ\x80ƘɝǰƝûȇz¿ƁåȰМӻƥΐOɐǭҔӳ',
                    'description': 'ҫϕù˟˳Šıǰ҅ΒuǝúʫԑȾ\x89UŬζ¥;ʹzĎϧΝƍ\u038b\x85',
                    'default_value': "ӿӬҡFȜ\x98ǍͰȯʮўϽкљѩɑӝɼÐƻЈԡЕɊ'ϊнǂϢҪ",
                },
                {
                    'key': 'ӹäʯ˓ɹ˨É¦`˞ŢоĜŹɌ˴ʎƹЂǵ˯ÁŔ¨ƢƒʥΣĸ»',
                    'description': 'νЉʓʅԬ΄Ǧěǳ˳ԐʌŽʛҰЖТfƷпŒЍ˻ıťǶȍˬͰǉ',
                    'default_value': 'óH?ǳ˰ˌ˯Љҽÿʶǅ¦œɉԝȆѧʼɱńжɉ˭\x7fзQԌŨɨ',
                },
                {
                    'key': 'Ë\x85āϙ҂һңïωÝ7ÌȢ\x80ƚƜҸʐ˩ŕЧ¿Ԫç¸бɍ\x7fԞȗ',
                    'description': 'ʂΙSćӪɕгΈYǆ&QˁНËÙĆȼ&ǂңǖˑ˓ļȣϟРʻɪ',
                    'default_value': 'ҩȀÊъİϊъʐɗЍԢӭ;ӤĢwĸʫң˂\x91\x8c˲ʺƑԪβӣțϨ',
                },
                {
                    'key': 'цÈҍ#Ě\u0379P<ҮC]ƺʮѱ˄Ϲ˄Ʋ\x95AɇǡέΒԨ˽Ưτȷŉ',
                    'description': '©ϬgҡÐЄң«ìĖϒϵűĒȕςɹѢ\x83ɂĐʛȆ',
                    'default_value': '˪eϾӯǺΗќɯҳ±<ɇǐѹӸˢαșԧˏ҉ìŲ"ʿˀүűЯŋ',
                },
                {
                    'key': 'φıŁzőɌѿǝǪ%',
                    'description': 'лâψҰɦʵå\x81ӧǈɽдүΪĖқӏϲ˃ДήĆӁϤ\x9fҡɞͼΧƇ',
                    'default_value': 'ʟӳЗΛļˊɻPŠȷQӾѨԞϯηӱǂсƗīƓˣҌfͺϗʮ˺Ԫ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӊ҆ӡ',

            'target_id': 'ӮȉȔýυ',

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
                    'name': 'ÉɧƼɦõƲǝӰŏ˳˜У\u0381ǌıʇ\u0382ʮʞȅûTӎʡԎ\u038dôòʨЫ',
                    'description': 'æ\x8fЁȐԞ§ϵЖӰƑɨȧh3πȽ˕ԪŁËƬŹ˃҉Ȃà\x85ԋʛŒ',
                    'target_id': 'ˇʘԌ¿Ʉдʾĉчөф%ÏͿĖl\u038dǁМӎѠϵ§ȧ˵ΎĳŠ˹ɿ',
                    'parameters': [
                            {
                                        'key': 'ԮǮǾуεό«ҚûΨΏЁʢҹȵдưȸǅҋƵɿȄǴˊ/ˉGɑǮ',
                                        'description': 'ȁɡȗɨʮ©Ÿԕ§өǃѐǦ˪ƑԬГУªķǖΠȒ\x7fӮӢŦĠˣͼ',
                                        'default_value': 'ȹӍīχӔĨҳȏԂѱѽиλϯϷѺϏɴƸӟѸɃйŅ˔ɳŁ\x93Ȇǅ',
                                    },
                            {
                                        'key': 'GĹьƍ%ÙтϢͺӽ&ЎҭԘȿ˪ɽŗӬęŲηOǀOˠ',
                                        'description': 'ԗtƞ(šѳѠҡNЏǧΛQɰϭɁ҆Ӌƽvʶ˝+ώ͵ϰΗϼѥω',
                                        'default_value': 'ѐΦǮЉρƸҚʦӂɪҭƗӀĮӵңԖÆύǹӘԚƹϒŻê҅Jǝђ',
                                    },
                            {
                                        'key': 'γ',
                                        'description': 'ʄъʊ.ƿŀʀʸĕÁÞęÆʹȳťǺˮłœ\x96ĊλԅϭŶĖαќԩ',
                                        'default_value': 'ΈΡʕͿȩЌBҰȚƜƾȏтǩɫÌ¸ʳіȝ˛ĕȑǮ3ɴΊɫѹŝ',
                                    },
                            {
                                        'key': 'ԊƶjԬňӾòȉǦŬΞԬЀҾéʹĽМ\x9cчѐưԜβњgфψĈд',
                                        'description': 'Ϡ\x87ҜˬĨ+ЏăɚȵȒЗčʈ\x8fϑҦЅҁ>˾Ĺςѕѕċǿǵɐª',
                                        'default_value': 'ʢƬΏХŐѝɸЪȝŦ.ӆ˓˟ɔȒҐ5ɂŊѢĹКǹʆŉҩƦНö',
                                    },
                            {
                                        'key': 'ӤɽԩȄǄʵkéϙ\x93ѧҹÕԟņҋϼůӰ¤lɁŅzЋӢɔ͵Ӻˢ',
                                        'description': 'χ\xa0ìӬѷѪOÙöќҠǺȋӬ\u0382ǢǈìӎȦѮȟǳЧĞ;¶ʖŜȋ',
                                        'default_value': 'њ#ŴǸɚʄаŌǆɷɤƸ.ʋЯ¢ԭԇɍѐƍМγɳѷǗlƣӣʂ',
                                    },
                            {
                                        'key': 'ϡmҤЉѵ˸ƈ\x9dѣˠµӥήҘOʁΐεǿʋʥɭѬǀÎκă\x8b\x83\x9f',
                                        'description': 'ʨɶĐōʌáѾƛɥдШоŗΗǬɹ«Łτѹɕ΄ȡιœÖɯӆұƛ',
                                        'default_value': 'źżʢ$ɲȭϣɟ;ҪԘϺѫӣ҈ɇ˱ҝ҃ƙЇһбƭƦԏ?ξSŻ',
                                    },
                            {
                                        'key': 'Ω˄япӈϳ.ưğ»ӡƳ\x9cԦӹϮȋęɜƤӦļȦɻęҙ\xadϟˇ`',
                                        'description': '"Ο\x8a-Ȉ¹ϹǸ\x9dɉMҦÍĝ¥åϚаϜҶɣǛ҈ʲόƢØ҄ʒb',
                                        'default_value': '÷\xa0ύɸȖϤεъƸˊϲȷĪνԔŴϢ¸ũÇČäѽĹ΅ϖǩ˪ʬ\x83',
                                    },
                            {
                                        'key': 'șËӺϥΡŐԢӱҀĈȡģ˪ΙȯƧіɄӽǐԠȏŭ ҂Êʥɋіſ',
                                        'description': 'ϞοʣˤŔgȢȸЀƭҍЄÙЊгҙďӟοϨӂÐ˱ơŊϽгˇɒʯ',
                                        'default_value': 'ĩԑĬȽȧǚѣưαſϛgƧԒɋȄҞщӱǯŹ£ǃεɌ\u038b˃ƈ\\ґ',
                                    },
                            {
                                        'key': 'ĄűщɊǿ˂оˏϕ2ŔŉɝБɅѢ~ё',
                                        'description': "'ǝ\x9eɖѲƽéʍӤĠ\x96¢ƷƿˍŲΪġΪĬɖ҄ʬ҈ӌɘFȿϻɮ",
                                        'default_value': 'Қ2ԔԔϦʼɿɊϋȢɼοʢӁŽҊǖǾΰөԪ˯СԟΑÐř΄¶Ӽ',
                                    },
                            {
                                        'key': 'ͽĒΎǞ¬§ȓБӡÀԢϼŴ\x9fĤ¾ʼѫńΰчϿΗ\x9aKЄУӟϥʧ',
                                        'description': 'ǠҤϖÍѸßΔÞδ\x9bÞɭȰƟ\x84ϧԓԑ}ɬȱ˒žϒԛӟϷɖʵǻ',
                                        'default_value': 'ҩTϿɶȵйԁƯÅԟÊ×й\x98őфϵȹыĦƩ\u038bƃƽ[Ƴщν˹Ø',
                                    },
                        ],
                },
                {
                    'name': 'Ф½҉ԎļäÐΦѰ',
                    'description': 'ǲļüϛ\x93˷Ρ˂ΘɠȤVƀԞ¹õʺ\x83ѵџЖ˄â˪˥ӳĸϱǔҷ',
                    'target_id': 'ɤӓɺŭœ˩ȽЂmŝŨӳӋü΄ńţПк϶ʼɡђͺĐѸɈԤПɧ',
                    'parameters': [
                            {
                                        'key': 'úˀӫӝӂ&ʿʣїСâȔȩ\x99ȁĩҟɩŰҘΤOФԗ',
                                        'description': 'ĵ;љȍ\u0379êτͳ¡ŊξUΉύщӳýϿƦ˒ūďтȈKԠˌʤóԃ',
                                        'default_value': 'ːȠҡΜ©`JӊσĂûįņǚØɬϮԒ\x7fŧġŔѲϏхȸԓŷÄǄ',
                                    },
                            {
                                        'key': 'ΐțӌЉʺ\x95đÉѼΓӔ\u0379ǺόŮǕĹ\u0383/ĨȏĺϸΣǥĀʥơΒт',
                                        'description': 'őόӁʊǅĊ"ƎęҁԈȋŕӵS¬¸ǿікΡԊѨǍʄ˶ҽψȵǀ',
                                        'default_value': 'XȣνНȤĖŗƀϾ-ϓʆcȒŖŶǯȨӴȬŻɞʋÆäƶКԇǞҥ',
                                    },
                            {
                                        'key': 'ЭǣçɮƙϺȔƚѣʵúmɔӔʯ¼Ǐ=Юԥ˝HƆβɭ˷\x82ГǭȤ',
                                        'description': 'ԪĐcłɒϑnĨԛøʏҕάŌΤȏɡ˨ӸcџӋӡ\x9cưίŊʤτŬ',
                                        'default_value': 'ŋʾȠЯ¶ҫǣɰɽʹԂǉƓĚЃϐˡÜϭƙůĐãӗˡ˦ɜҠΪҽ',
                                    },
                            {
                                        'key': 'ʆо%ПώщҳŒŇªұʁǲљɍˇʑ˒бәĞÈÑȜБѡʧ\u03805Ů',
                                        'description': 'ǅ|ŁɯӀŽ҆ʥԅ\x8fŸҫ˽Ƀpũφ˼ƚƽɔѫҟƤƪ˴ȐЪtӡ',
                                        'default_value': 'ÃȳůЕӸĠΐҼĮşӲӞɃė\u0380РɃЎσÑÂʬͱϿʚÅǡɼҪВ',
                                    },
                            {
                                        'key': 'ĐӷԬ¢ӓ',
                                        'description': 'ԫΤż҆Ζ\x97ſʁЂġŁǛʠˇӃǴʞӳɭ˚įĸýϖϸ˺αԤ`ъ',
                                        'default_value': 'ΣŨʂϿёǕˑŇқǜQӈѧŽэF¯ɼƥЄӁŇļԓǖϏŌέɭў',
                                    },
                            {
                                        'key': 'ȩδéÊ͵ϹéǆƪǒѿӨǒʹ«őεԡƸĖ˔Ҁ½Шԫ\u0381âʤǊƣ',
                                        'description': 'ʴFɉԗTʣѪ˲8ʎȷҦѩA҄НѽƾĖÊѥÎ{ǄҐaԞϲœӺ',
                                        'default_value': 'ӭл˄äǂȲʉ9ЪѠΎɺϵƢƚpύӶƆĦˁȗłћӯžȍĹӬɷ',
                                    },
                        ],
                },
                {
                    'name': 'ӡļǯӀӆ˘Ƃϻ_үÆϿȥŨѮŏїƮʚұƕĞ˰ϠʪǽȃŀŕЗ',
                    'description': 'П\x8dԑЬԂʷѭ\u0382ĩΰȂģȔα˲дԘƒӦĴͺҧϹÈǰĀɫӡƔΑ',
                    'target_id': '˹ǸӅǇɰÖAĥ"Бʊ5Ѝ\x95ώсþϺϙòӦѲä#ңӐ˟ЋӪӈ',
                    'parameters': [
                            {
                                        'key': 'ӄзД',
                                        'description': 'ҷЋŻǓԄfÊЪLĞΧDϩ\x99˗ǕӼǼūʜЫã÷șφӏΓϷǯŠ',
                                        'default_value': '˺ťȜ˧ҕςϚʧƶԚԞʗЌ×ʘȴÊǹӏɢӰĮǬѲµùľżȒ]',
                                    },
                            {
                                        'key': 'ӗΣŷȭ/RǮƠɉȰѸ',
                                        'description': 'шɼ˩˹ԨϿϸʉĚƥɩӭϳQÉѸŊɼ˹ĜΎʡӴЄӱӐ˟\x89Ѷϑ',
                                        'default_value': 'ǤȒŒΕʵŊͷņіˆͷѻѤÙơƬġȸɑõĩɬζ{Ѧ\x83ƎȖΓӲ',
                                    },
                            {
                                        'key': 'ɳϕΗʧԃԇ\x8bΩ\u038bƴˊ˾ɋ«ԃеЃĄ\u0382Ȏ',
                                        'description': 'ǊҶԈĿƐ˧ԙʣϛđwʮȉǾɹвɁУϖ\x80ʄӑхˬɅ0˱ӗӉɢ',
                                        'default_value': '˨ЅѡȊ¨ŧҮϡ˳ĪϏë\x91ºѳˌʋʆƁǸ\u038bƸѹˇ\u038dӡӐšАǿ',
                                    },
                            {
                                        'key': 'Ù«ϕʗ¸ǆDǱŚ҅ɿ˷ԑƳ~ʍ˅cǅśԔŋǛǙ:B]ц˥Ɇ',
                                        'description': 'ǒȃӃŀƇ˰ʉƿˎH\u0378ϲлȴȷ.ΠƵyʳâMãǥыӗӤʝ|Ú',
                                        'default_value': 'ƲŴ\x7fКeӻÂ04ÂʰŖΎÀī¡LπʍєƟ_\u0381ƪӜ˜\x9aΉɮð',
                                    },
                            {
                                        'key': 'è\x87ɲȐàŧЫŀ©ķѣͻЦϥĔЮͳĝ~ɂǙɪƕ˩Ίɑʍ\x80lԄ',
                                        'description': 'ʿȌɃō\x9eĨ˽˵ȄƛЂĜĹáуǵ¨лΔҦҘċԨӒŇήȺįħƏ',
                                        'default_value': 'џЏˈˢӃχьҊʾPǛӹ\x81ǯәĖԚ\x8dǎƬѥњϙǹ¨ƶǠүͺʻ',
                                    },
                            {
                                        'key': '\x88Қ>ƼfRƶȓҒӆ*Ǩϥ^ĄӧҮ˷îӞȴĵʡēëӖƄʭϊҸ',
                                        'description': 'ı^ёÍҖŤʤѧǏΚǍΛOŔȦlΘ8˳ϑҍŃĐʃԗHΜƖϽz',
                                        'default_value': 'úͱʩθĖҒɾˑԍ\u0379ʄÆɈӷђԉӹPΩ\x9eРҭφ\x8aƳħљΎǕa',
                                    },
                            {
                                        'key': 'рÎɾĐˌȰĽњÁɇԐʞӛ"οƴʒϬ˖ŐƴұtӘɦ\x98ʔϨϠL',
                                        'description': '×ǖ*ѠɴԚҞeʧѿKЛІźΨȜöȲʻŐʵЋĸŶƤċʷ\x9aЍҘ',
                                        'default_value': 'ėȓϐϓǔӮǅϞЂӍėƊ\x80iÁį҇ӏӐЯҍĎʲ˅{Éφҷӊh',
                                    },
                            {
                                        'key': 'АϫʈØ\x97ԮԖǜʘҮҁ\\ƦjˍMӸѼwƀ҉ЦтǻѤķɜɔӪʹ',
                                        'description': 'ѭЇͽѰMƢɩɔğʘɽүĢ˽ҞǑΛGɛ˳ɗ˶·˩ѧ΄Ȝɝʾɀ',
                                        'default_value': 'ο˜ǫűXȶŲҔѫЧӮɽɴȹÕƿǦľЛ\x84Ğ\x8fřҡ\x7fԨȜӄƦ\u0382',
                                    },
                            {
                                        'key': 'ɫōХƆÞȶ¡Ԋʵưʃԕ',
                                        'description': 'ɇŦ\x9eǩǎļʟґѫΖϊҴȿǄԪԀʹͳҟѐ®¼ɋΘɫӢˁǵεж',
                                        'default_value': 'ƒƓБǌɐɊȊԜDŠǋӽǎêǳȒÃƷɖʶǍǣ¢ѩЎȂƌΪЬó',
                                    },
                            {
                                        'key': 'Ӧɺ¾ѽȧШ¯ȜˌŠ\x7fОġӄƷè˘ǜ¿ǝ϶ʃvdFʂÃϷÑĚ',
                                        'description': ')ҜŨŗϲϳƽӾǝƂίɺԉǫ\u038bZǊҐƽЇªǀΛѳѰӲӬɍǫś',
                                        'default_value': 'ʖ˝ġɒb#ϊΘ!Ͽ˗ȂɇǛОÚˢƌˊΕĔЖ˹2ŵǑȔєáҬ',
                                    },
                        ],
                },
                {
                    'name': 'ηФѴƲνӔΌΚdĳӤŜοȭ"чˁЅΗɀÅʝӚѩ҉Ȏ˄ԤǏ:',
                    'description': '˒˫ԣӵσȡʵі¦ԑҗ§ӆЎΜǔÈŬɾƵʧɎGъǬɪѸʦĪƖ',
                    'target_id': 'ȔȋЗˊОǿW.!ҸёΉҞ˘Ű\x96ƩМȂ÷lmϢɯȻӴɲҌԟɪ',
                    'parameters': [
                            {
                                        'key': '»ʚǤӇԟ\x9dˆΔʺ\u0383ӪʖˉʉÉԋκҕҲҊψ˫΄ŸȩɝӼѨӾ\x84',
                                        'description': 'ѯɚӂІˇɑǺѝKƾ\x9aϫ҅Ȓѽԡԩ\x96ǬŜʘҼѩÙʯТĠϰˆС',
                                        'default_value': 'ˇԋΌϻĲ±ȗҴƓϼ;Ôö]Ŏ҄ǟԜɸΞЙˍӶүΪ´őˣҊ0',
                                    },
                            {
                                        'key': '\u03a2Њİŭʖ',
                                        'description': 'ÈԈŹ˶bΕǅûʃ˲ǢбIɭƢ˂ģǠҫϙɂȆäсǍϿț\u0383ʯơ',
                                        'default_value': 'ѥʀîʊΎɥˀҐʧăơҔˊļДԃθΈŭūɛĵĤӧӡʸ>ӘȰЩ',
                                    },
                            {
                                        'key': 'ŁNϱǠЁʇĠƊԮǄ?ÄҶŀөԥη˾ŋτ҈˷ǲңо\x9fӸǙĦϮ',
                                        'description': '˅ÆΤϒŸ\xadъŷжΌ<ˁӻðΦÖЖԘСĥŭƕŅѬ`Ðʇ8+Ò',
                                        'default_value': 'җ',
                                    },
                            {
                                        'key': 'ͱԉѽċϻêϿÆBɧ\x8aЭ;ìǼϜϝĥʴ\u0378Ųӥѿҵď˳uȒԆʝ',
                                        'description': 'њĠȝϴƦӌĭǐϟтɰ^ɀγϢǓǣǷњɪʽµϭɫЩş\xadɳƦƯ',
                                        'default_value': 'ҿčρ\x8cʭ˨ˤɋƬҷҪϧӣ҂ïӶŇ˭ĽÑźƨ˾\u0381Ĵ\u03a2Ğнӹ͵',
                                    },
                            {
                                        'key': 'БɣǾΘҗɖʽʉҊΨ\x81ΐЅ',
                                        'description': 'ѓӫƈԪňίϾĚϕΉȈǏӍЦΚϣэƌώ˓Ԙϩɗʊǥϐ\x930ΤԤ',
                                        'default_value': 'ШǏУdŠпğ\x97ΤǁNԂӣƦԆƻüԔЎΗεXǢ\x88čī\\хԘ\xad',
                                    },
                            {
                                        'key': 'ǪϭҀ{ʤПƐ;\x8aάΆĭȬtҼ˸Ϊħʙ\u038dϱŷLƈИǈƼõΨƎ',
                                        'description': 'ò`ҐɶÌҶȠǿǕяqѭʫΔǨԔϛҠ|ЖgӇèƓҖ˃\x96Ƀʝͱ',
                                        'default_value': '3ɉ"ӢˬKǄ\x99τˏрϻkńˇӮҭғǜηĠϢľҰԤ\u03a2џƧʭȣ',
                                    },
                            {
                                        'key': '҇λͶԕҹӬåѥ/ԚƌòȲʜԝżƪǴщåʥТŲ²ΌĜѱҀŝϩ',
                                        'description': 'ċ&ãɍ¤ȪϽćӨʂӏҪԬȿҬñgҡxɟО«8ѽăRҋϿҌΕ',
                                        'default_value': 'ҒƦĉЂҠǰʦҊӺ\x91Î\x91\x81ʕ҉\u03a2ƿˌÀƥm\u0378ͰhЁν\xa0ѼͱГ',
                                    },
                            {
                                        'key': 'ʰˬȊhАÂ_Щˇ',
                                        'description': 'BˑĠԔӥΠͱӗАǼӎ\x90ȕʱǽǽǔȯȲʢҀȨǗž\u0380ªήӈ¸ħ',
                                        'default_value': '×\x95Ïǎǘ\x9cʕĊȁШŚФɗĮō\x8aЭ½ŨǳΙ¥ǛһɖСΈƠΔ$',
                                    },
                            {
                                        'key': '҉ƂøUƅѤÁçϤή\u0381Е8˗ҕΝ£ʢǸĶǲƧ¿ĉQϳԦʥȾҘ',
                                        'description': 'ҴǬ-!Ыʕӣ˱ɘõςQө2ѫ\x96ȚФ½·ĢÂҥϟĮɶƐ½ïԦ',
                                        'default_value': 'yǳј¦Ώ˃¸ȵʧE×ɡɻÙͲҏĺǶɍǚϐɘǆԤΪзPʩќԊ',
                                    },
                            {
                                        'key': 'ɖôѐΙȎИđƇ˙ј\u0383ɻŶƣӁεǄ·ǧԘȹÆΣӞӅлŁνų˸',
                                        'description': "иʾûéǒĜÞҗǦƬʐCǥН˝ԝѴϨǱ'ƕɲȬŋ·\x7fԖΥΔА",
                                        'default_value': 'ƎĳȕĭϱțǑ\x9bԠʏʿҠƬЛ*ǵҋʜԙqˤҳΰǢԠЧу˔ϛ͵',
                                    },
                        ],
                },
                {
                    'name': 'w;éɀųεɼ@ԨưΞ˥ӍЈ\u03a2ιÜʒŵǔдϨūĽŭҹϘǠç{',
                    'description': 'ϷͲāα˲ƤʯɩǬȼΞΞʘϸȿ&ƑӢŻÓȇľjĘ2\u0379[]ҏØ',
                    'target_id': 'hƶΏԙМűЍĬЉԗǼғһεϭȲƁϨѰҼ_ƁΨӌ@ˍԃĈƙŜ',
                    'parameters': [
                            {
                                        'key': 'ξӟƘɸƮOԆԒт¢Оȍ1ƩѰҬǬƱƾȇåԜĄɗƞӪԚЍʉͲ',
                                        'description': 'нʟɎ²*ǋͱ;ƷÊϯѵÞƧѨЎű/ԀЄԨɚoәњТţªɛӛ',
                                        'default_value': 'jϐȺ.vȄȌ\x88Ńиҗ\x9dДάĂМСɼƆҎɛŸǕǲѮȦ0˜ȦǛ',
                                    },
                            {
                                        'key': "ϸöӦʞŠń\u0381±ʅȫʗŁ¨Ȗ\x85ɓ#ѵWʻ'ĐƶȮϰÙзӱƒЮ",
                                        'description': 'đӹͰʲӓƐСσ;қβҎǙсԋˌϡæâώŒяˊ͵ӊĽ҅ʹŅα',
                                        'default_value': 'φ\x82ѾɫſҤ;ęȤϐƪ\u038bӫūǇ\u0378ėӎЕЌHŮ\xa0bϹҒƨǫτρ',
                                    },
                            {
                                        'key': 'ŭ˱ѿ¹ԫêҖу˫ӱǋ˗ŠέԘ\x8bΠϡϳ%Zԓɋʰĵ˪ʡƊӌƳ',
                                        'description': 'ҼѧЪɨµá\u03a2ZµƂɣԞ°Эƫ˴ɞκWɪӵЌЗɍŵҜŸģӄν',
                                        'default_value': 'ƆͳƞϨƧ˩ϽȺΡyΦ÷Ҙ\x8cȝɠДīӊɧg\x870·ҳ\u038dƸʘǫț',
                                    },
                            {
                                        'key': 'ϙȘʤt',
                                        'description': 'ͶШPɅȽ¼ԤǺ§¡ԌϟΖӫ¥Ɔ\u038dԄÌȞå_ƻMǧƯcóμȾ',
                                        'default_value': '˔ŅɵʋƋФҊ>¤Ԡ\x9e˶Ȼщãƺƚ˽ĊіЂǎJ΅ʋʑӰӫǛӒ',
                                    },
                            {
                                        'key': 'ɤjϣȅʾʇφΧӾʫ\x9bĻİʶϱҖϞ8ĭѝʛϸɎҩ46ƷĖĎƄ',
                                        'description': 'Ӗӄʬ±\x9aǍҁùԮĆ\x9eХý]҅OˈıԙΈβŲɄĞҤϔԂþƲ˃',
                                        'default_value': 'фԤԬҖÄłĒƎӷʕƱɛ˺ЄʇȞ¿ɭȉÛŦÐJӞeĕPɴдʉ',
                                    },
                            {
                                        'key': 'ѺУXѵĘ4ʬêЎɂÉԋɒ\x95ԗͱҺўƕÉ´аĉĿͰµɯƞƼȬ',
                                        'description': 'ìҷʗԬń҄\x89ˍ˒ėͿΌ϶ҼϚŔŐǸҶȪʼCƪЬӝʞʽļƌū',
                                        'default_value': 'ȞɤԄǥɐˏώȊОźӛÜѲ\u0382\x99ЈΟ˭ĈʘԂƔ¦ӪÓʸњÏʇĝ',
                                    },
                            {
                                        'key': 'ǐʐӘÎ\x91ǚЀͺfęé˦ѐĤӸÞЮcƀԜǃʵʄ\x85Ŏ',
                                        'description': 'hλԞ«NǈЗǼÍÇ*/ϡƑ͵ҹ˕ˠʐɟ×Ō7ӕ΅ăŧÀӮǾ',
                                        'default_value': 'UӲΟҠŁѼ˴кɸɁĚωɳēӱԙ˼ӴРƄњVÌԠϓʽҪΆMʦ',
                                    },
                            {
                                        'key': '˙ȢϑϨǽʙм7ƁǬԊǹРÀҺӼ\x89ӲӉϯɅ?҅¯ԉӈȍҡƀǅ',
                                        'description': 'ĔɥѵÔƒĎɼѤԈöǧοΑȄε\x90ǷҊ\x8dƏԠʡδÉЬ˜ӱϨʊ8',
                                        'default_value': 'DÚԤʖˤŻʒÅΊҀыȿѧɜԆΖ~°хʺԥŷPӄϧ\x97īĲВ:',
                                    },
                            {
                                        'key': 'ШZԎ˯Čљίʬʥŵӣˠѭā¶ΚǠĮҞɫĄƴ¯Μӌǝï\x8e˙Α',
                                        'description': '˾˕òѴ¢ѵȿ\xad˲ΆЎ8ӗԃϊMƾӟñɧñ˾ЂĐϸӎԜħńŹ',
                                        'default_value': '%Û˶ŵGɤƖЕŃǥӪf˩©Ăɘ\u038d˨7ʮϕ˻öҡєʃŉǛͺɞ',
                                    },
                            {
                                        'key': 'ćӆђɘͿkѩÙъɖ\u038bŬύ˞Ȭ˹ƅǱҏʅaȵмћĮŀġ˻оǶ',
                                        'description': 'Ǫ\x94ϠÂ\u0383(¢ßӾΛɰ˂ʞΤɤҞǽ˘ñіŏƻȕΎȞλЎξʲΟ',
                                        'default_value': 'ŭГ\x94ƢžGӃпƂӖңĜҁƵ~Ǘ˜Q\x98Ǡ\x8eƘƸАÕʸǟŔԛΞ',
                                    },
                        ],
                },
                {
                    'name': 'ĥKǦԋa5.ȣʊӃԋӷБɚ~Пϓ\u0378ҝƵ҃ȉКЯƞ˺ӏœː\x82',
                    'description': 'ϯƔĽŝryјАgĀǑфȊüϥΒЭҽaƤĞÃ°ɊɋƇˏʁҀV',
                    'target_id': 'ɠҋǯ\u0383ЧWŕȩɯÀРΛϹɣȢʦϜΗŘɅǛQĸûԑАyЬĹэ',
                    'parameters': [
                            {
                                        'key': 'ȷɖŎҧƦ˹ʾǻԜǈǌőԬɷƂĪˍƾѶіЦ˽ҭϲΔŞ˻ӵ˦ŉ',
                                        'description': '\x8dӠʶˈĎΐ\x91,ʽʮ!ʦҬЭԓřԣѭɾӮӃΠǕӉ"òˋю\x9ađ',
                                        'default_value': 'Ȍģzćɹɮơ҆^&Дť]ӏң˻ϑԬʣЃ˄ŒřΥ+ςΧаCӖ',
                                    },
                            {
                                        'key': '3ƱАϊмёΣ¼ʗʑѹ¤УɁ˷ϲŘ$γʙƕ}ɑ\x88ԩХÃņęʔ',
                                        'description': 'ǼϭȗϳѪȏЗŝ>\u038bĳʇ\x9cѐP҉ŒȐ¢ßԕȹƌƘˠҲТˣʹӭ',
                                        'default_value': 'ө\x84Ѹõç¥ЬeƄ¸ȀƀѧΠ-ƏºȅȖʈ\x8bқßǲȁԀҔ˄7˼',
                                    },
                            {
                                        'key': 'ȓɄГʴɁàЗǦƮʚ˗iɞÛѠđŌˀ҄ϑɽ<dҟżŒԕύТц',
                                        'description': 'ʂȎӒЗǿǳыӻƘƐǔω\u0383ȹ7êԔϯƼХĢ\u038dЗèΊɍŌĀ>ƽ',
                                        'default_value': "ІƧ\u0381ʙК˲'ѽȵ®Ǔ˚ųĤʧūƸȓƸѧϾ˛ʭӱę҅ӭԌ\x84Ξ",
                                    },
                            {
                                        'key': 'ªöϳƨԇӍϻԤҙʚӹ фӁϨʩÿȆѬĊӄǵ',
                                        'description': 'ˋǄƕЫԗЪuƭÖӚʾġϸҬY˵ѕӳ\x99"ƩΜΕ5ØЃæTȌѿ',
                                        'default_value': 'РƟɻр³Əɶơɠɺ\x8b-д²)ӏȑŒӛȫǱ·Ɓū3qЬћƥϟ',
                                    },
                            {
                                        'key': 'Ɯ\x95ϥυϞξѝq²҉ӒɐːңҍЫԟͻÕѺ\x8b\xa0ӀЈԥǴıԝƎ;',
                                        'description': '˯>ˮƣβ҇ĵĔŎѬǟÚŌ¡ĪэҚɪÊϒ˚{άʫїőϾòѸ˘',
                                        'default_value': 'ЃβXѰˣÝŜҟ˙_ĠБqǆϽͷPųīģƴϑѴ"NȜ\x94ӵÐʵ',
                                    },
                            {
                                        'key': '˧ȧMѾ˅ҚČ\x94Ú7ͺЀÚƂ5ϩȪŉ¼ЌӵΊȴΣƨʻӁŖӼ>',
                                        'description': 'ˇH˾ԬѰ\x97ʃdπɍˑĜƳӈҁAØĎ~ǅӳαԮѴԦӞǋĘʇƸ',
                                        'default_value': 'ǻƊ\x84ɍКѕ˧ªȮѸǢԀʨȎͰȢѝЏΔΚÒϛяĒȯƵθ˥ŭÂ',
                                    },
                            {
                                        'key': 'ǕĂɧ˪Э҅Ӕʰǫ\x86êĻԓɕ<Ӻɕæè(Θ',
                                        'description': '&ӖðΘņɦ˷ԗрˠɝŦΛʹӫȄϔɖϲŦ\x9dĂ˪Äɮγǂ˽ғύ',
                                        'default_value': "ΜșʕʠâǘőÜ'Ƙɶ˖\x97£ǴӺʌ\x82ðjȧώΈƹѠɁһӯǾʦ",
                                    },
                            {
                                        'key': 'ΜĖÄƩМȬѵǳÂšΪBϗӖǵÈӭҦȞ',
                                        'description': 'éˌϴЉȕӈćѮȕľȗßˮÍɊҋĭƌ$Ίϰҗîөś×ɢҊÅæ',
                                        'default_value': 'ԩҶӉΐиҁ΄4ωʢ \u0382ʉД\u0381ȴԎʱĔ҇ƊНϑNҡɜʡȮͽƪ',
                                    },
                            {
                                        'key': 'åʛԞӖȁćʎӡȖűόҫЊӠˢбԢ\\ѭ҅sʑΉÒЦͱĮɟˎʄ',
                                        'description': 'WԍŲïОǙЃ˚ƫΗҁ˸Ôƒêʖ[ѶϲҚԌϲԬǉȳκ˝Òҳԇ',
                                        'default_value': 'ƒЗΊҁѰΗТʧĘҡӹǺЯңȋǾϩĳeǖãԎĉЖͽ˰˨Ϟвˀ',
                                    },
                            {
                                        'key': 'ɒʍӧΌȲɋԅ\u03a2ƂƀԌЏЗÉӢрӥѼÔěċԩƫȰǑéϹʁ҄Ȉ',
                                        'description': 'ѥƨԝ}ѱœ<9ʺ҄ń˅εǁҲʌƫȰɄȹjˮσәҴ6ęʛʇŞ',
                                        'default_value': 'Ҟґγ\x82ȝЍƻȉȝԣƅǳчΪǺѽƉ¸ʓ¶Ȱ˜˝;Ӷ\x89\x99ϟѵӽ',
                                    },
                        ],
                },
                {
                    'name': 'ѕӧѶũʉƻϐ<°ȓʅ',
                    'description': 'ǇΑΑȐ ĨўňԈ˾ȈЛ/СʮѫɴƙÞԘϝΧȔǃƼƈ.˥˹Ȯ',
                    'target_id': 'ɹɋʉǨơѨљɪʎaҏĐӾÊҸƞӥŚͿʒʵ\x93ͷ3АȈӹĒύ7',
                    'parameters': [
                            {
                                        'key': 'ƩsъǹÇǅÊ˲\x8a',
                                        'description': 'ŤӦԃɽϱ/ӽüÏ\x8bƦ˺žľ˗ŕΡΚ~ʹЀӒӌЉÂǏΦΒԣƧ',
                                        'default_value': 'ʑǩщŐʴҲ8˲҆ɟϾΘƮMҲǅžЁƘÐԚӺӼaƚ\x80фђϟѰ',
                                    },
                            {
                                        'key': 'ÎѓÜѴ˚ΓƚԚȂɁͷōġѧԠǆȜ˙\x98ӾφaĉĹЮΏϦ\x7fŏѦ',
                                        'description': 'ӒʛАϒɘϾőθԒҸˡʸȽϞǚÞηņƴϮɤȢĔЀ\u0380ĊӄͰǪ\x9d',
                                        'default_value': '\u0380ϢÝƬDǍҾʀӦϬԬϗñʻȉҾ˽ϐΉĕϢɔʀчĈŖˢztı',
                                    },
                            {
                                        'key': 'BÿΨdʹҎżɥѤúƃɁԃ\x81ǏĔӥ(βƱюȔĴȔDǵΜͻȴΐ',
                                        'description': '¼νЕțcŹˏӟѮǑʩ͵ѲƎjɤѻӎǜɨí)ί˙˺ѠЧϳͺɃ',
                                        'default_value': 'σɩ˟0ҝǫxɚӼҪҕΧȫºřϸýγЧаҘǚԀɽËƂѴ˴Wө',
                                    },
                            {
                                        'key': 'ġΊǔѷԤͶĹŵEɖŅ',
                                        'description': 'ͳǢΰȶǤӚҸˡ˼˥ƆʊԄѨ͵҂ԆϨöű\x8a˫ĤϸͿӗмҙͿƤ',
                                        'default_value': 'Ͻβӵ·ѐĤˉɖʰΓԇũW҆҅ЦңqƉӺʴfԆԪ#Ԇсԓѝ\u0381',
                                    },
                            {
                                        'key': 'үоȭŢԮԐҤßőŕȴϦIЩkѐ҈ҢǀϵSǒRԕǁòыԝѺn',
                                        'description': '!ZȞԬ(ͷӞʂдЩқŲʕ¤5ɡԕƶҗ¢ÖԖȿҮɹдʰ˰ҐΗ',
                                        'default_value': 'ӭɞйΩΓɸҕ҃%\x8eЅѪРВҶΜZԀƑɐʹǈíГĤЩČҐ\x9b\x86',
                                    },
                            {
                                        'key': 'їkīˮȫˇʶſȭΦ\x9b\u0383°ˑѭʂ\x8cӞDϝʖǼΗɄϪʼʵ°ƎӍ',
                                        'description': 'ӄϝҫĸѨòĬzмÛηüȤϽIƙϰǮѴώҡĎΖʢÑƱɆɭϺҮ',
                                        'default_value': 'ĚЦԛλº\x8bы·ǓΙџ˶Ǧ˦ӿ\u0380Ļҟ}Ť҈Λ\x9f\x88uǄӨǾƁc',
                                    },
                            {
                                        'key': '\x97ȊȔɆůҲ˸˛`˔\x8dԡˊ4ηĔҷ÷ƃ\x82+ƐЭǢƺƖĉŋҖž',
                                        'description': 'ΤͳѬ¤śβɎάSЉȉ\u0383ФЙƛ\x9aˡΡˉɈѻʭkјϵʦ\x9d\x96åÜ',
                                        'default_value': 'ʴ\x88ЯɄɇ˾UôҎӪҴʳ»ǮҟҨщҪʭґϤχԒȣÑŋȚ˕¼ʳ',
                                    },
                            {
                                        'key': 'Ƣ˧ȫ˛Ý',
                                        'description': 'ɪ˲еŠώъ³јʷőôĳЄiŅɛRϋʖǉЬjζЄōϟO`ϱʦ',
                                        'default_value': 'Œϥʗ(ʖфӛɤϻƟѨ НɭԖȉºǖѷƼǀΕѲÛʑȊΰ\u0382~\x85',
                                    },
                            {
                                        'key': 'ÍҴΠȱĉȢŕ(ĠǓĩýӷʠƔӕʖğİȳɋиҀʵѵɛƫ\xadθϷ',
                                        'description': 'ԊԕӴȠҀ˰ǖԧԒ҅5ɟǰРБӂÖŌεʾÜʟϷҢԕ\x9c҇κ\u0383ϻ',
                                        'default_value': 'βԆʵȜǵлÂčο»҅ĻFàʧɢӮ˩ΦɈǵsʇ6ΖŚѵԘФĵ',
                                    },
                            {
                                        'key': 'ˢ˄',
                                        'description': 'ɼҲѶё0ʈҪˢϹѓÎ˘Ëť҉йžzˍΥŘҎЫҡƙŖ?\u0379Ťɵ',
                                        'default_value': 'УͻȹѭԐ\x86ӛɵ<ρɍЋҪҒӟfϐҫϫ¤Ԯć\x90ӔíƼѕԓ˦Ȕ',
                                    },
                        ],
                },
                {
                    'name': 'ӔӮԗҽԥūƥʿВυКԞһ4ъѪŒԉQÂϳ˫ƵΥμìΞӳŞƳ',
                    'description': 'Җc&҄ɶɜ˘ӂĹOõʅɒЅˑԈљżÜиǑǪ҂ƩĿˈ\x86ĉgǋ',
                    'target_id': 'ƌϵ\u0380ƙίԨӼʎ˒Æӯъ;ǪϣĲĐϣӵɬλͽʯ_ʲƦϨмΞ6',
                    'parameters': [
                            {
                                        'key': 'қԋ°˾ӾϑцǕАîЏȩϔþӁȚ\x8eίӔƥ³˨˥ƮɝƄʕĘΜƁ',
                                        'description': 'ϏРѶɑȒίӺϿζê¦ǆʧ˹Î˄Ļːэ˄ɻЍưéԜǴŞ!ΫӨ',
                                        'default_value': 'ĐҬƩӱµAҏϹÖΆǉÂМǬȋϗƐѫиԑƜϖĔҽȨϻΫƒƲ\x8b',
                                    },
                            {
                                        'key': 'Ŋ',
                                        'description': 'ƽ\x93ȺÄȍȳė˸ΣԘӤӒĸĜȘӔƨ\u0381φҵσ҅řӔпƇлȪϐå',
                                        'default_value': 'ӓéТǨȞƿDGЕµә˝ЍӒӎŏŔ˜Őʍ˶ŷȿϤgԩʁҏƭ\x98',
                                    },
                            {
                                        'key': '/эЅġˠƋdɲȳΐįȷČĮɯɛҪʉұȖҩˮƐͿmƅŻΰʴ£',
                                        'description': 'ԑΑŶÝŃϥɣӚƊпѱŏȇԦ¸ԬӰ˘ʥӼŜãЗϱŴӢƿɯρƄ',
                                        'default_value': '΅ƶЏǾƴӣԧƋƄǗӜɤ3˱Пn\x95ĳɚοϦŐ\\ϡŲˤȷϚіË',
                                    },
                            {
                                        'key': 'Ϫӽ˥;ҁ¦łaѻԠлƇҨđȬ҄ɽ0ÝϽɠǪ҆ӒҬǕӺέȸӅ',
                                        'description': 'ʍӏϗ\xa0ӔK˚ǂɐˬȏȷʄsʁǲîҲƒƴȶ±ˌӠӃфԬ\\%Ɉ',
                                        'default_value': 'қƤÂғȈԟɛʨʰŘƀȓΐʶѝәɁȥ/Ɍ\x98ԋƝԘÞĳҥȂ\u038bљ',
                                    },
                            {
                                        'key': 'ŴґɗJ˦Ȗ6µƻ˵ǞļɼǣÓǋɋǫ\x96¬ńý˵ө¨àûȎÿȬ',
                                        'description': 'ѷO)˟ɉӔŋŵԢ\x9bʗƦƌĀϿ˪\x7fľҔ\x9cƄ2Ώȴʐ|ύǽΕȩ',
                                        'default_value': 'ɥ\u0379\x87ϭEҜhҎϞʔĸʘцɺφҀȟ\x90Α҆ÀƆɤӈЇԨǸӺӅĩ',
                                    },
                            {
                                        'key': 'ĳӦ\x97ԋͺОˊǲЯþƭ\x8fǠŪ҂ҮʤʕɐϮΠԖƙɉŕПŁԒƙŁ',
                                        'description': 'λˠƭŚƩ_ѣǳˈɂźʅϧԀӈěӕϛϭ˥ԇѴȈϵǶǗң¡ǌҶ',
                                        'default_value': '¯ʁ\x8d˷ίаÑGʃёȹѪеˢíėΓǋĮŗɩХŤǄȀʧҋǊӭŊ',
                                    },
                            {
                                        'key': 'ѨÅшԂ˞ƁǾҏèʵНǽӱԣӷԈҔ˖Ҭåɖő',
                                        'description': 'ϦӨѬ\\ЉɿĉϷіǙȳŐLѫԤƀǹϊǠЩēΟɖ$ѯÇΣ²ϻɪ',
                                        'default_value': "ϑ\x9dʽyĠӒXʋYѯ'ÇħΝ:FʒKìԉĄƗnʹŖҐˡ҃Ƶȅ",
                                    },
                            {
                                        'key': 'ˡӷҏϽʅͰÖ{ʔƖǆǸĂĚȂЭÖλűȊƨÎԙįŬ\xa0ϊϓҩÌ',
                                        'description': 'ƺ\u0382ǩАƃñ҄ƴ(ȞǊŖCǝȫɶ˙Â˒ϠһʲʱǐАǗʤЮšʨ',
                                        'default_value': 'ȔˑGќʷɼƬтœŢ˱ɿēІ\xa0η\x8căǿĹѐĀƏӚÀʛƟФυһ',
                                    },
                            {
                                        'key': 'ìˑ¢˭įÇкÇʯ|ΆɒěϔñУ_ĜҖ\x9b»ӿŞǮȳƽšԘҽӈ',
                                        'description': 'ӨҌҳŴíɘҹíԏĻøÿǬ҇ȩЯВĩ»ĆͿǷвɒçÖӓѨʨį',
                                        'default_value': 'Ŗɲǩ\u0379ȒǦɸEӪʲŜУ˲\x8dԋ2ǖčƮѯч\x93ң\u0380<ǭ°ʞԭТ',
                                    },
                            {
                                        'key': 'ѳНϖɞȩΓӉǯЖϢƓˡɄӬϼ˽PŵǖƚȽοǅʧѼͿъѺМá',
                                        'description': 'ȹǇ΅πҕьȡʑƷ˷ʫțǑҨϮ҅ӳ˱ȽʈwĥШˡŰӞψŉ˙ђ',
                                        'default_value': 'æèҷѢʘŪϛΨОоąοɍħѵıεԣÂȕӤӋˊěȼ˜ʥ[ɰv',
                                    },
                        ],
                },
                {
                    'name': 'ѮˠӅȘюBƥτ³ҭѢɩĄŤÿĕɝ`ϼ7²ȚȅɄЄȅV˟Ƿђ',
                    'description': "ĝϘӥɖϽ/\x96ϛǆΦŗŔ\u038dЯĀńҍ'ǿҧȼ((Ѓɼ\x82Ȏʠƾˡ",
                    'target_id': '\x91ͳǩ˺ЀĀƬӍ¶\x9b)ϱ6ƚʜˬ¢ɂ\u0379ѻϣσșùђĶҀщХѷ',
                    'parameters': [
                            {
                                        'key': 'τЀgãěƽʮЈƲ˗΅·\x99ɔϞǤѡŁĳ\u03a2ļɯӘȗǶȁ©м\u038dư',
                                        'description': 'ȤҼҸÊHˌҖ˲ïɎљÈēӁҗώRªȪʧȿҷδƆӗǕϚĖφǂ',
                                        'default_value': 'ȾΈʿӗǁƾ˓ȱԓύʎԇӟĻȫśʤԅϬsƚκҏЃȅŒĜǌ\u038dƄ',
                                    },
                            {
                                        'key': '\u0379ʁǫӊ˸ ҸӼϑőʖӯǾDɽҴϬ×éПцӭðǀßɋĘε;ϛ',
                                        'description': "'ĒфҺҾʃƊƔɸӱХĘ@ӅʐȯÞNνѣžɽѧĤȇѩŅËθĺ",
                                        'default_value': '\x86¬\u0381¥%ѵϢԄ\x81ЎσˋˏǜʂҏӸͶɿ˰ʨωΏΘЕĻВfÒӲ',
                                    },
                            {
                                        'key': 'ԕPԇ´ѻƱĀ˼ҏ*¦ƴ˗|ҶϽėǥˋūƳƓԙԥɱӸǏ҅Ӎƀ',
                                        'description': 'ԇNåϟǕÕĄϊķԊ\x96ʥʡѮǅˣ\x86҈îӲ0ŗąƟξ¤ĩԇұX',
                                        'default_value': 'ŜюßΘѠѶʆѧʊԔΒяϿ1y]ɩǄӣ˧èϗ/ӿƎӹԕҴлǬ',
                                    },
                            {
                                        'key': 'ǌŵăǸ\x9eȋҙԗвİƸʘëӚɊœWÛӵȋ˧ϓ',
                                        'description': 'ԥŗΫˊŧΖɜȽѪг\x9aʁӮêǰеǺӳѦǾĞǪˑйĊĪϱυȨ˘',
                                        'default_value': 'ŶµʻéԙʟӇˉѳƱώpĥýͽ6ӡŰϸċ˼ϷόѬԙĖɩʯӉǁ',
                                    },
                            {
                                        'key': 'ˎfҐ;ϸľ\x8c Ȳɺ˵ѥƁ¶βȗåǸȯѮoƖĚҁ˺Î¡ȀŘʽ',
                                        'description': 'ŭίǕ\x84ƨνѳǍƳ±ö˽ȣ\x97ǂ\u0379NѱʶҕȡʊʷǶҊҿë7ȒȰ',
                                        'default_value': 'Ȭҥԧħƻ[Ëѳѩ΅ПƼÛäǃcԀ0˲ԇÇӛĲÈƀЦʕćɞх',
                                    },
                            {
                                        'key': 'ϒѣĭҒҳУýΡ\u0381bȩʋѡ{z\x84ǎЬǙ\x88бɓΓŕī\x9aιƜТ0',
                                        'description': '\x8aũ˺ąе·Ŗяɭ\u03a2Φ¡ǥ˂ΠϥĲЏĀƓѸƍ<εâў˓˽ȜǊ',
                                        'default_value': 'Ȳм}ϵȢϮӮđơѣјˈΤɮқŴj\x8aƼʕԛžɼÁåџ˴ӉˉԚ',
                                    },
                            {
                                        'key': 'ӮӠƎҌ˩\x95ļˏmԩ\x94ƣǾƉĴǻϓʏƝǿR/˖πүѱźԂӿʂ',
                                        'description': 'ҽǤӌЀƏŞōрÒĒʑϴĆĬʖҧů\x94˽5ϳԔƔĉǔ˴Ź˶οσ',
                                        'default_value': 'Ѓ˲șӾυɗҭŪǢâwċǹѰĀˈűʉɢӤôҨĺϜŻŇçкŊԞ',
                                    },
                            {
                                        'key': 'ѤҜʶƅƈ2ɈǮӌЖeɚȐɒ\u0382\x91˃oһÙƦˌΥŴϨǓϏē3ʟ',
                                        'description': '\x94ɸӕϖ˅ЄƉңѴаĸ£Țv>҃ưΥɮǟԃЯɚĉҿІЎԔ\x92œ',
                                        'default_value': 'ĨѺŔģҶѪШ@ʜ˶uĬӟƷϓŘǲɧ\x88ɣϜIȣʜuм˨ˉÙŌ',
                                    },
                        ],
                },
                {
                    'name': 'ȍҭɩȦԚԒ\x98ˤġΌCҾңµͲýҗŕ\x9dАήɦyńЎąŠQҥ\x94',
                    'description': 'ѯʍηĢҞ*C-ʈӞѾɯħΚKƞƊϡʂԁѰҵΣӲӲԌлЭʦ\x8a',
                    'target_id': '÷ȸҼӭѺOԨѰĶŀӷΟʻЮŔҰ\u038bĄҬĬÕъԤɴԒr˻ШŤӃ',
                    'parameters': [
                            {
                                        'key': 'ϿǛɣOʍɬÓԑɬɋVmɹӸɘ',
                                        'description': 'ҞʅϲɯԄ×ЋԊĐɬŻźĝPѪΜʞˑˀǏÈ\x87ƘʠбҢb#ã¥',
                                        'default_value': 'ȩΫөάҶϔѳӔīάвЇҷŷȸŧЬɼӍ)ĐΰґѼƨҥÛôěɆ',
                                    },
                            {
                                        'key': 'Ɇп½ӌƍлβōʜ§ѻүƹϵόˣ˱Зѹɯ_Yǟј˝ϟҸÍƈ¹',
                                        'description': 'ŊѣҒ4ԍȓΐˍĴȮɁȣƯɿæ`ɷʍ¦OǣӎԭљSȊƈӒǰθ',
                                        'default_value': 'ƐҘ˘ӕδŶѐўжƇáΤ»Δƅ˭ôǃ¼]ïĉˈãȮʴǙҌ ~',
                                    },
                            {
                                        'key': '+ͶōƴʰҴѨŷŅëКɈТƊïѬVǚϝЪѢΫҬkǟYϜȒѝƒ',
                                        'description': 'ΐàǑɬ\x87Тƀӈͱΰɑҽŭ˕ԗԊȣ,ѪɼͳΣśѨһĿӵ2Łı',
                                        'default_value': 'юԍȁæ\x82ʁ\x94ǨҷRЗИƪҜǠƍӂķvFǦƅόɩşɓɘɖòϲ',
                                    },
                            {
                                        'key': 'ЂԭϩïÎОѻЉŗȵŏƎɗßʋ҈ĜъϨ¶ĂĮĒòҴY®ȧɔĎ',
                                        'description': 'фÕӓjBŭǺHӞȆ\x98ƆÌлǒȅə˘ȪȯѪСɬɳǷǩǦҋҘK',
                                        'default_value': '˺ϡϞӡϚʷѤԌƋшΙɵ½|ӟϲНИēɎϝϿ©{ѣǲҋĢψҎ',
                                    },
                            {
                                        'key': 'ЎɄ6ӾŘӗB\x91ƤΘxʾŜ>ȤčłΥѻÛƝˁЕǯԖêʝͼЌ\x94',
                                        'description': 'ǔƒ{ѽϭДԏ½ūҾȣȤ[ʻϿ»!ˠʌŗї9ʣȅКӄůϴǩĖ',
                                        'default_value': 'ӥĺ·ӦʒŨ˟ҟó˵җђΕЗӒÐȀŴωԮϭɚСЉțμŎ˰çΆ',
                                    },
                            {
                                        'key': 'ӫƨΗȣvϜћԮˇę\x89яҞÐ8µƧrӐȾύńԎơ\\ň˻ϐпО',
                                        'description': 'ϫɑƱQʹȬdԑZҴϕę¼ɍ£҉\x94˲ΑÜAæɤà;ͿЃȖΈŸ',
                                        'default_value': 'J\x8d¼1\x80Ϝmѵŉ\u0378ВπśͼΣƐԚҋҢъŖȻčªІŴ',
                                    },
                            {
                                        'key': 'ɲ=ėӠǥ\x8cȞǂɷϾȢѐɠѱ˭ƫɿȪԎɸΉʄϼřԂѢƒ˷yƃ',
                                        'description': 'Ł˞ςЕĭԒ*ƤιŖˏƥ',
                                        'default_value': 'ȺȠʵȤ·ӳʮΓųϝǇӉƫ҉ήҟ͵їЅ˖ˎįŰhʀƵΟӶƣ\x99',
                                    },
                            {
                                        'key': 'ҷÉÏÜǳӸʅ¢Ћɵ˱Фѷɖ˟˂\x8bѴƴЌşζėȮĈǦУѼ@ħ',
                                        'description': 'ÃǅċƮϞɋŻϴȹӧӐԝŝІɧ,ƢΝCнпƍГԛǃӂȇτҚʹ',
                                        'default_value': 'ԘʯʂǓɇώΟʽńǵеŨʄƖƹĲŰmԉѬãĭ ѷ©ÉȐӀ¿Ε',
                                    },
                            {
                                        'key': 'vХʿȘʺɚԄί"ʋѪȒȠȷľ˃\\ȲϻĔ6ΙgOʒƖzЍȭΜ',
                                        'description': '\x9e¤ƵӾ\x90ҿōΑƗǯаċƟԕŤëɎåѐ˲l +Ķʜ{ΛΎêÑ',
                                        'default_value': 'xŉɘƪШ~Ϫ+ǜθŁǜábǨɄĶ%ƔҋǛθǏжˇɒӇѷӝҧ',
                                    },
                            {
                                        'key': 'œ¬ʯɹŵˈƕǌ˼ĊȆҕϷÊˢȱÄфŋˠʾϣɶɞѬûÜͱсÁ',
                                        'description': '˧ȎµŒýFȾěȩ˦ЕƴˌǺğV҆Ѯǹ\u0382ũӏĈԡȈѯǤ˷\x8b\x95',
                                        'default_value': 'ȽɸѭӣȊΦƐβSӻ\u0378Ũɲɧ˶Ӑ\x7fɹξĻӨΓĩ<ͻǖЀđϬE',
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
