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
                'υȥϬЯŌŭСȢ÷ѥ',
                'ǬŴ´ɷΙç',
                'ˍ',
                'ʎТϚ_ɾċ1Ǖ\x85\x86mʬƆMΙǼӑĞ˭ñӣŬш{ԆďӨ',
                'ϖњжΔ"Ƶй\u03a2ϪυƆ',
                'ҾнŰ\x9cw҄ÏƪƁҋęgǍěЭɌыȖȮВǅ',
                'Ӛ\x8aʲґɡќˍƋ¢ҵŉнөЍ',
            ],
            'comment': 'ȜūǞ˥ǴɆԪûԊëͻқӃѵ\x8ehӥΑƧнɈɅҬȪåԆѦuĚď',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                'К',
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
            'key': 'ȦАĪŭδʆˆǧ˫ĸÑ\u0378şǜ6ʀŃņҰǤ˒;_Ý)ԥȷǊҢȋ',
            'value': 'җΛŘɡØʹ˸ѡŸ0˾ȿҚɛuȲÚơӔŬΪԆЉɃʱ\u0378ϣƣГć',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'þ',

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
            'target_id': 'iѲʒӘі˾ƫı®ɨōԜȱƒѾԫϿɨãБΝϙѶǶǰѶ΄\x9fԉǣ',
            'parameters': [
                {
                    'key': 'ȯƾЎɴ˦ȎːŢӵbĐүҽΥ˥ɾӽd[ƃfȠɍɖĜѢȭЂ˟ˬ',
                    'value': 'ƑƪƭʳԌƣɎǠϮȺəˣӡΝΤǉŇъАȜΗΈҙҩQŎͲГǛв',
                },
                {
                    'key': 'ÈҭjȻΤāˉĈͼŅpΉ¨ԀѯɪĽӍ\u0381\u0379ľƌϯwĤ\x9dѢӝ',
                    'value': 'ǟǑǩſŹ˂ҩєсóҵʎӹЙϊ~SԢ҄ƪʓξǋȽÂɁƮЂšѭ',
                },
                {
                    'key': 'ҼЩΖӀ±һϫβȅА\x86ĄǁҸʨmмžɕŧϜҐŗˁԜ˂˷ʴΒː',
                    'value': 'ѱ\u0382ҨҧIщǔöʦgҚЙŵѣϵYŌíίǠϑ˴ũӚƬΰ·łфԉ',
                },
                {
                    'key': '&ϓΠτ\x8c{Ʊз\x82ʚϗʜҦÛЫƯ˳ğаӄщßђӖȐdȦ\x93ӓɂ',
                    'value': 'Ҹ҂ʜȗϛӎũ¦ïƹƓéƵÒѽƧ˰ѵȶʾȷͳÇȟǾЦƐŊǸ_',
                },
                {
                    'key': 'Oa͵ҺľʛȊЁԜǯAΦǕÓʛќфԒ&ķɇAҠʻʙʏwΔǍĚ',
                    'value': 'Ӳ\u0378ʶüԢɉУҺMӓǥ>ϹсΐɗȶѵǦʡԇ˗ʋёEøŐНќԤ',
                },
                {
                    'key': 'ɩϏЊȅ9ϫ˨ӤȂˋԚ~ȏȐƵĕǲʺǏЄѽƴȪÜ\x8b˛ɇϝȽʭ',
                    'value': '\x90ȕ¯ʰ\x82ϫɓ\x85ȲΦɫɿβţθӟȁDυϪQϜВҟȟӚ\u0380ϲʌǡ',
                },
                {
                    'key': 'юПЭΝμƾʉɼĂůȖ˰ҲЂ˪ѵĒ\x96ϟũΔӤ\x82ekϖΞÈѾԜ',
                    'value': 'ϺбœΥѦƼȡ҈ȗѭĸӟΤңӅèÆòΟΨϪͻvҙʂâƄȏYӤ',
                },
                {
                    'key': 'ŝϕǤ©Ťԩƀ˗жDͶϼʧόҿѺȎҘ\x89ʍΘ4ўʧƿ\u0378ԐŦŁΘ',
                    'value': 'čŘɠȸȃɄϘȏΦЗȲ\x9d¶ћһéÂѪǋí·¥ЄѫXvȴȝӪѸ',
                },
                {
                    'key': 'ʠӀϜцșӻ\x9eϺǙǄ0˲ИÔȪ4˶ѐҝŔ\u0379Ѯ5ȴӞɳįƪ',
                    'value': "ϥςɼďǟәӢÏ'ǚΩȿǝʻ˰ª˙Ǫ¡~\xad-Ƕ˾ΗǌÇϚǏ\x84",
                },
                {
                    'key': 'ѭҝЏМѾёӐĮ(Ӂжʋѫ ԓĘ£ū˝ѸѬʄƼ\x90ȅνЂˡǭʣ',
                    'value': 'ʨ\x86ȐΖԍżЁȉӟ0ƱöʭȪεѨ[ѡҡ҅\x84ѡƐ˝ʙʋƅѭ\x89|',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ϞDρĝс',

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
                'ȘʾĜ@ƊǉԔё˟ǦƷĘг9ë^˼',
            ],
            'comment': 'ɱGсѿǠɚǝҮЦǁˋơӶɘԒџ˽Ϯ˰ƢпΞ"\u038bόȒʓǋŁȴ',
            'event': {
                'target_id': 'ϾπɕΕn$aПîǏғ7Óǥͺ\x9fϟӯˎ\x8fҰΏVυΎҝȒƁʂӯ',
                'parameters': [
                    {
                            'key': '+˰Ѧȩª\x7fȔʧȭј˹ΞҀͲӓҕӽϲѕQȑӐŻŅ',
                            'value': 'ĤΑǽĄdϬ҅ŅƉΌͽÚY˹bӮ{VΟΩώӐΞǠȔ',
                        },
                    {
                            'key': 'ʲūϽјƔӵΰԂџ}ʀηʈЉʎһÔðǠŚ˓Õɫ×ƨÊΏ¬dѕ',
                            'value': 'ˑ7ƂǟԕʶoόˌϡȏϚҾϺɨȚǚҍYќӤˋ^\x91϶ŝΡʡdϠ',
                        },
                    {
                            'key': 'ѧðÙѺжğѥŴƏƈƱµ>ˡĄơȴ˧uΘЊˈ\\7ȥĨәҕʔĒ',
                            'value': 'ɍҶүƖɉƻ¸oŕӺәұȳ˄ǞƴʬEļ˩Ƥ\x95ЯɎȹйaĲѩ\x8c',
                        },
                    {
                            'key': 'Šʪӗɩԡ˩˽ĒӛϵҼԔЁӡОʞŸʩ˄¦ȐȱтцðĖλǸ\x9fÚ',
                            'value': 'ˍȨĬ҂͵ȓȵþяӵÎŀvіҐμĦɏΛɄaҦϬĥҀϛϏÃɹț',
                        },
                    {
                            'key': '¦ɳɗƫӴӽҩ˼ʀψɃ"ĄӅȉϦσĹɩЏ˘AvǮϷȺ˧ҸϾЋ',
                            'value': 'ӁіÂģ\x84ɨƍӭŎҮѺʭɲƜ\x81Bԝάɏ˜Ģˮǚ\u0382Іűʳŕϯ˹',
                        },
                    {
                            'key': 'ǟîːҧԥʣʹɾ;âťǓɍΥÄҦł,тśȖŅ\x95ʔŕœȪƤѬǦ',
                            'value': 'Ǩ˻˖шŇӂʀɫɮʳȾ҇ұɖӀʺʜ.ʠϳӪӔǦʦŨϰϱӍȼD',
                        },
                    {
                            'key': 'ƚÈƅʘЂʏ#ԓlŬȯɗ·ԑԟƩ^Mīȕ»ʔͳԀˋWʩ',
                            'value': 'ƢȊѫ\u0380HǮʴҀŻѻãɃƖȪȂȜʡӳӌƀƖeӯ¼ňĸǗԄǙӊ',
                        },
                    {
                            'key': 'ΐȓψҙʳтЗяЛҩåѭȑ5Өζ\\ɘϲэɪAʇЫ\u0378ɓѤȬz\x8f',
                            'value': 'ƜƯĎЧǞΧ\xa0µϼж7Ԥ˝ɶ˙˵҂ӅƿÙƖȧVĞ\x8fÓͲÄǖΦ',
                        },
                    {
                            'key': '˝Ȝ',
                            'value': '\u0380®ȽŃͼ,ď¢ȺΒ\x85ѯЊͿώ¯ʋϙͰĖ\xa0ʡϔ\u0381łȅ¶ƘŅʁ',
                        },
                    {
                            'key': "ӣņ϶ǥʔɿƆɟ?юʞ'Ȓʨґī\u0383ϕˏųǱĒ\x8fӎԓӵΑҪƅī",
                            'value': 'ƍԄ΅ǞѬϠԜƌ?ŹǈďˀɢɵѹƭӭǚZѓTû©ȣѶ˓ʨхƵ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ԥ',
            ],

            'event': {
                'target_id': 'ġЄЖʟˏ',
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
                'ƓϠxґҔϽ«°ƈǻоҴҩӄç˱ę',
                'ǕМĔ\u038d²ɗƯɵӍĀŶAԙԆňЬ0¨àʴϷɆњË',
                '3ȮԘ',
                'ċЈœϝũ\x89ĭ',
                '\xadβƫЁçʊ¶ʸȀͱĜҥЈдҀц\x81ʹе',
                'Ʀš<hΠϰд˶Рʣх2ȮΙϰ\u0379Οȼ',
                'ѠʻӓİҥдҺўȭƩŇ˃ƏЌҩ',
                'Ɯ¶ʴÍϗƕːт¡',
                'ӏВӀЧe',
                'ȫƀàΟЎ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                '\x92',
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
            'key': 'Ѵ»ÙӁɯÁрŋȼ^ȯэ±ӈůȯϨcʍ˴řȓĒȗ0óõÆҋʷ',
            'description': 'Jȏ\x82ϿɓŦǦџ\x98\x81\x84ϾҹҰɂ{ȿ¼Ǯ?HưŪ˽ǧ˺ӥЙÙŘ',
            'default_value': 'Ȁȓ˩ʋųȰíԥZȸĨ˺ҶƠĨѝēƊӦƾζĀлĽȥ=ԋˡTz',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'x',

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
            'name': 'нΔŪÓ\x97ɩ\x93ȲȀˎ\x9e]˰Ӛӓąȋӟ=ÆϞ1:ɴЛ<ӷԔˌҜ',
            'description': 'ωҶ^ϾԎǠʀĻЂɺƌikʏԃɈăѩŝˁ҇ȋÙΜҊКŬʧ˜Ҍ',
            'target_id': 'ЏËÞUb&ƈ\x87˕vȵ(Ҝζ3ԑĬĮϮK˨ϭyƳѧЗľǱǪŘ',
            'parameters': [
                {
                    'key': 'ĲwǦϳƆōͱОƭΞêιĎњɩ˶ĆʰБÑΦ7УъѺ\x91Ɲǣ9W',
                    'description': 'ǸĎ&\x9eγŵʹӅʛɋøƓΙĂ}ЀǙȼīʢ',
                    'default_value': '¼ϖЁÇɁʢҕʈŕˆ˨LΛâ1çǻѹѢϪÇþϰЕˌвӤǾпϹ',
                },
                {
                    'key': 'ɧyɞҿӯėΊʐнìӑŌƽƵƹWʄѹȍҗ|žăĂVɷÅΉҀΜ',
                    'description': 'ΞÒæǁӇѡûӁþӴƣ-ԈƠˢ£ǩªʜöˁñŗ©ɣрčǧǥϊ',
                    'default_value': 'ͿaԒq˜З?ҵųJLԢɴȱŻΩFӋƽƕӵʎƎ»ɄҙѲ§Șљ',
                },
                {
                    'key': 'ˍ϶ŲŅίȏыϻϙӾЄԚ\x8e҈M˳ŞV"НѠӽŁãӖ',
                    'description': 'һȉʓíΧĶɐӪ}ǇĺͳЪƱůҜ˳ѽˈԝДТοɧɝТȅºδΦ',
                    'default_value': 'Āʿԭİ×ÀÊǮȽȘÑӈϩȸˮ˷ӟȚǊOɓбҼǶ»лԓҌǻϱ',
                },
                {
                    'key': '˸ʯˆÄΚëţϒƮĠòǧвӓːǄϽƋӳτÖˋσӁңƇʍԪвĕ',
                    'description': 'ŬӊǏΓ7ʟҏѦͼΑгȄӅƶΫҊĉԏʷǈǒϥVŐŌύҸfѳø',
                    'default_value': '\x92ȤГǙʊ˙BήɻęXɁǼÚѝ˽ʈϬѝ\x98˞ѾNȩǏʪ|cÞő',
                },
                {
                    'key': '\x87#ӻėŴƪȠ˵ѭ\x8e¨фϭ\x89ѠɱΦǋϵÑ˳Ć`NʰŮͿϗėǨ',
                    'description': 'з$ǙӲђ¡òœ»Ћαǯӄѝ;ЧʢˏǗƳҋŋҒDɅφɬġĊш',
                    'default_value': 'ʴȓƖЈHûÿƷŒĪˮɎκnƍyҚϔԢÍʄ\u0379Ģ˳ͱϚȕϋFҖ',
                },
                {
                    'key': 'ӀÕƀƾњȫӑȐoHΣҠƹӶͶŕΨʵӑ×ϫαԬӛшЖͼϯѹʰ',
                    'description': '\x80ǖ΄ɼťҹÿǊńǛǑϦˣɁʟɒз϶¹ѸӃğɗѳ)γΙɃӏˉ',
                    'default_value': 'ìϵ\x9aư˾ǓɆțǦö0˽ɔȍǪɵˮ˾мԦʸĂǁҋĭǃ˱ԅ˴\xa0',
                },
                {
                    'key': '\x98ԮzіӛҺұ5ȍïӑ\x82Ȟ¥Îϖˡ#ǶźĩƉ',
                    'description': 'ΚԁʍдŹԌϐ^Ӏƕҭӳ˔ЀĩüûϙáΎȰÉʓ\x80ԣԇȠ<^˃',
                    'default_value': '\u03a2ǹíǛΐзmʋĈςĎҒɢӬɚˤӛҭ3ɱѧЁǈʅʙїϳĔǬͺ',
                },
                {
                    'key': '҈ŗȫԕˡàίƐԘӶ<їŹ˥ĬφŮơϰèˁҟ˂ӌ\x87Ӫϝþsǐ',
                    'description': 'gí\x9cɩϜÄǱ˭ˮӶÖƠŝӃ˩ʟϧɘəϮмǍ¼ʧԆҚĎʗҽș',
                    'default_value': '\x82ɉЫӭϽ˓ĭМЋι˨Ŋǘɤɮșԡ˝ӹþ´ľҭИĮŉδƸǕԭ',
                },
                {
                    'key': 'ðɴƤϮЙɀć·ƢȺҍƹȜćƱѫԆԪƾǻ˘ʴС÷ϞЉê\x9bӍɨ',
                    'description': 'Ô˅\x93θGϺgυ.łŐƺӤ×\u0382|ҀŚΕҹŪɹЃǉȜŦҠӹɎȘ',
                    'default_value': '¦ΉʍŧʎӰȭӗƥ|Ɠ·ҖѤơɹȏ~ǗɣҊĀԥӒнпɇÍњL',
                },
                {
                    'key': 'ÃƿèТӎԠ\x8a',
                    'description': 'σʟҋ\xadƸѧªƥƧϖеӧ¡ԮȈȳ\x88ӯņȒɹΗʔӪūƽʟ\x86νǽ',
                    'default_value': "éԓʲǮɧƿԬΐŠͶʷԐԟƢΗЃүΒʬŬ4Јŕ£Ȯúѯ˰b'",
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӼԬŀ',

            'target_id': 'ĮǺþȄȗ',

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
                'target_id': 'ˑȧʉǥȞɳЍӵʹǼȡ|Ʊʟ½ɦȣτҾɋxȞųĝω±}ƷÚÂ',
                'parameters': [
                    {
                            'key': 'ĬʌĵμeЙėΫΤƽúZβĆ\x89^ȕơϭԄӴʄ"Ȋ˹ªǉǎ9ĥ',
                            'value': 'ɠÀҮӮȇ˚\x8bϿ\x93ǇĘθцʯӇĸѰϧʌǔȗҤʊǢ\x98ԡȗӒÚƙ',
                        },
                    {
                            'key': '҂ŦҤȄԔʇÙҷԗū˰ίƀѕƿÎʗ˃Ú§ψ˚ɖкϺǰ\x98чԎ#',
                            'value': 'ӖͿ+ÛԝȕЂӅ÷ѥÿʍěӨϻTԎΡɱЕʀǰ˅ԋȜŤϭ"\u0383ϗ',
                        },
                    {
                            'key': 'ȟ˂Ƨјʙ;ɐԟΒΆ',
                            'value': 'ƌɔʒˎɇdôɦˇˬòƸăɆӃЉŔȡΕġйϟΰƎҀƛӁҐΠф',
                        },
                    {
                            'key': '\x7fδдϸԍΣ˛&\u0380ЄŹ?ϠɼʅĶΤέӆѷé˭ʌśIĀΖ˖ʴĂ',
                            'value': 'mөʥĺ~Щҟ$ԧ˔ϫǃƷwȷĭΟŅĄŃӻeԖ¥Ŗôɷ&ϵσ',
                        },
                    {
                            'key': "ŧϨɞǄԍ'ӀǁĐБŴˣKɑҢȓ˔ғ]˵ZɅ˄ΉԆ\u038b\x8eĻħΰ",
                            'value': 'Ŋďȟ\x86Ϫ£ϊϾlrƗȟѩɒʍ\xadʑ˅˩nѡf¨ѭ¶ӦǆǃȳȤ',
                        },
                    {
                            'key': 'Лϙу$ÔҚг?θΡѓͲԜ',
                            'value': 'Ɣԧ˫ѰŻɮ˾Ƅԇü\x92«θ͵İӥΌ˒ƻяԆʓƃ\x82ϱ%ƝнѰÔ',
                        },
                    {
                            'key': '˝ӋɭοàΨɧė˞ȝϻӜӉȶГĿɸʖԮϪԍǺǹȢξpξѯϏɬ',
                            'value': 'ӄһϓţс˟Ӂ\x8d]rʺҳŵ˒Ӏɩ,ёˌҧԭ}˪δƏʳȴ)ʷӒ',
                        },
                    {
                            'key': 'ðtЊö',
                            'value': 'ʲҠǶʊȲϟɾɱмжҊ˺ϲԫůÁȎ FʮÓΚȣκ.·\xa0ȎԪю',
                        },
                    {
                            'key': 'I#ҭОӸѤԂӱϹāϮȎЗϼģӿɊӇǴŤÈВХTҀӽȩʗʁJ',
                            'value': 'ѤƇſɼҬΔȅǁҙ\\ҀħԇÓ6қū±ʆȏ\x80ӾĀЎʁұӥр˂K',
                        },
                    {
                            'key': 'ǹmɎҞńԔҠâЈɝƜʫ÷ˍӆųϹͶkѨʄġɸƲ\u038dʠɚ˶ϖԦ',
                            'value': '¢ɦʹ˾ͲΖΡʃԡиǂȏчɜMжʕҍȠҏXѹáѨůEɢѭŴĀ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'ƃΈŪϤǶ',
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
                'Ħϻê ҢȌ\x8f΄ϑǱёӆīǜđςȉϳ',
                'ӭӥ',
                'ʚşӡĨЪ\x89ĵvʮȹȏԤ',
                'ȵɳЌѷȤϐĤˍRɖr',
                'ѺπœɉԖ&ľϠ˶ɅǤѲĎīʄ˝ĕʇÙȧΝ',
                'Ӟ҈ͱρƎɥҭѐÒīØɹԧӝ΄\u0378ŘˀĆȒȖɺ',
                'ĚκǤΓŽŗ҃Ʈˑ˓Ѷ˼ġӐƙ\x9a\x9aԔϕԣ',
                'Ϩ˲ũҟӠʠӏϴͽȜǺӐԊŔĒʊҐ',
                'ˡoĚ(ǟȌϯӐČ²¶Ţ˶\x84ǛjĲѻӢʢϡҧƉ#ȭ\x8aȽǴ',
                'β4Ťˣ҉ƶɜ˷âƑӴήǹRϕΦ\u038b',
            ],
            'event': {
                'target_id': 'Ѩ"ԈӆϣͽеʡKűóʀͽɘ˶þžϧ?ξăϭȘҤƯųӲӛӑȼ',
                'parameters': [
                    {
                            'key': '҉ąИӸƈȫ΄нɱѵğ\x87ЩGԣʰÏєжюҿ\x7fƅҢΔҢǎ΄ǙŁ',
                            'value': 'TÀвǥŗ\u0382ͿҼӰԈƧS˜ϧσ˶GĲǃďübФʏΠ;ðΨ§ʛ',
                        },
                    {
                            'key': 'Ҿә\x8fCФưӗʟ˭Ч҂¿ȗʖLѷƪŪΪў˺ȧLӊ˻ˊˡųԍʧ',
                            'value': 'ĝɖ)ʠϧɳƭŮȞǽMїÈҨӻѓø\x94ʿ\x98ϞѓʖsʝɕԚԔӴӔ',
                        },
                    {
                            'key': 'ӏ²\x94ȈʓŶñǔʒǟ϶λˋÃĩЊˏĮЏèԂáΥêŭł˔҄Đе',
                            'value': 'ȮʯвАįɌԔ¾ǰʐЧѳS˫ӈŚȭ\u038dȢ͵ZхΩӹƘʌ˯\u0380\x8bЌ',
                        },
                    {
                            'key': 'æГӽѾɀѫйÌùÛğʌʮɐΓƧɎаї˞˳ΞěϖƳЂɌȱαɦ',
                            'value': 'ύ\x87҃ùОӦ҄ӧ˨ʮȔѤŘJФҩÔУύЌЮ˝ÆęҶʍǍƪƎж',
                        },
                    {
                            'key': 'ЮͷԃϬ˶ЦȂɴǥǌѓҬȝʊÜtϞŶҏƴ\x83ŋɗ×νǙԐưÔӱ',
                            'value': 'ÃāРŎɄҠάԅ\u038d\x92șпӧĵ°i҉˛Aƅϕ+ˉʍè˴Ɏ±ŧμ',
                        },
                    {
                            'key': 'ɶЁΣӎ˾юƈɆ¢ȒŜʟǦВdΡүƢДӒçńϘөæŉ\x82ɘϱG',
                            'value': 'NȈȐıőȰʕѩ˱ʯˑ-éɅʞґƉeɄăΫňÀҾü\u038bˀѼrϔ',
                        },
                    {
                            'key': 'ƽЏԧȹԆӥΫл˜y\\ȥҠԋϏԙӴʹŶyƭԟ/ȂɭˮЯȎàΞ',
                            'value': 'ƝƓˀƔԙԐʂȳǌgӜýеƌлІʗ˄ʦʲӘβӖeCӱĔҁǞξ',
                        },
                    {
                            'key': 'ãƻŉņҵ~:ȖȷmΰùԞԞÙ',
                            'value': '´ɇұοãæŝϯfӲÍ˛Ӈ3ˉǑǳªʠ÷çғҬЩΟƷƛӳȘ\x9d',
                        },
                    {
                            'key': 'ʆԠ\x94əϑǙД',
                            'value': 'О\u03a2γÀńÏtͶҒŭĄӀȡΑįɦýǶԤɏ±è§țӈԒ¸jĦԋ',
                        },
                    {
                            'key': '˺ÅŤϙʧāЎ˚ѤҒƪöeϤοͺѹԍȊ\x83',
                            'value': '˗ӔѼɷıś{БŴǓQÛȱψˠĐчԔǃԂαЖӞӯÉdɿӺФϻ',
                        },
                ],
            },
            'comment': 'Ơ˖',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                '\x95',
            ],

            'event': {
                'target_id': 'ӃӨѻj˻',
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
                'ԛɤʠ˯ӱÕɝǊħӛҮщʯ',
                'öэίŌҎĴȺɽњɐґT˴϶˴ΉҦǂ',
                'ʤ´ȍǴъϚŵ˪',
                'ˊʖϜȐɓԜȗŬ',
                'ŚŋǤΎ',
                'ҩÍƖ\u0383ҍuOľԗӼ',
                'ǆĀřļӌȔΑЍǉό',
                'ӂ[ǩɽ҅қҟˈΊйӦԏҫZ',
                'ƔѲįʱ\x80$ȥǺǪ\x84ƤƂӕӮ',
                'ςÓɠˇԓSōέϯΛʿzĵɗsҕаüžŘɔ*WŖҟ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ǷӈȜϕGϊϦɥκԭ˳ίɃ',
                            'ŖԠʓéǂƭɬϸuǫȷ',
                            'ƙ\x8dΕєғ',
                            'űȷƦȲ˶¡ϸƁɝѾ\x8aЉІѶʝ(ҞžƈȦбĎεІˆζϛ\x8bԣά',
                            'Εņ',
                            'ˀ҅«ȿ\x8dţņŪŬӏЛËʻń',
                            'ԦʕǿзӺƣ\x96ʼϷʚĜ',
                            'йтƚҟę/',
                            '§˕¬ĖѶѴȭĈWį\x9cñ˷ԏð"}ȮɑĈŎ¯Ÿ',
                            'Ń²ƗϰÃͿrїµИĕҚ',
                        ],
                    'event': {
                            'target_id': 'aҨѤ<\x99њ˨\xadŁƗƴȨҸƱŘәó=ԧӊнΈėӦ·àȒţ/ϐ',
                            'parameters': [
                                        {
                                                        'key': 'ǈèiňХĉќřƁϘԨҮ\x83ӫ\x8bʭǛ˜ǑҰŻ)ŤӏѝҭͺϏѼ«',
                                                        'value': 'ϷȾљЯ½²ħȳÏҪēƱúгɍüѱĆФɆΖĖ\x87ӐĸŴǗѫǥȄ',
                                                    },
                                        {
                                                        'key': 'ԗƺΞȀͼóȝθЪхŞϰƥԥӴɀϣ˯ƆĳſǓŹӣo\x9cϚʁĺԄ',
                                                        'value': 'ʀ\u0379®ҧʵΡҌӂʽϠŐBҩʫɝ+ԈԚɴѬӌȯЛӥ*Үѿԙηǳ',
                                                    },
                                        {
                                                        'key': 'ǏÚʫϩюƩѲkÅĖ\x80ͲkɦȒ°Ęǜлҷ\u0381˺$υ˧ǥӖȒͷп',
                                                        'value': '^ɶΌԮȐˉʏ/ŖӴԧƜʙǭ˛҃ȣɒǙԡԆȹˣˤȉ˴ñϧКl',
                                                    },
                                        {
                                                        'key': 'ȠӤ¥đ1ȣӢ\u0379ѥӗϬƥѐɏϏĲƨъ',
                                                        'value': 'i˦ҎƢϟΆƹīю',
                                                    },
                                        {
                                                        'key': '˩ѧȠƛáκē\u0378ĽԞƃϳȼӍȫθ9jȊȣRpĆϽüЗѡ¡ϑd',
                                                        'value': 'ұľïE»Ԡ±Őʲάӡ˻ÎNŽaЖњŇƞұӣȕҧɹƄϿʘǈԓ',
                                                    },
                                        {
                                                        'key': 'ȖlŸҺΧӵѴŵЊψÅ6һ\x8a§ӸΚɮϢ\x8dНӉɴўőǜ\x98z˹Ν',
                                                        'value': '«Ż\x8cəÄӠ˱ŭЯŒÚȇÝŌȟԤ`ˤѵʘz˪ԬɄǑɨңʠѽƙ',
                                                    },
                                        {
                                                        'key': 'ɗҰa',
                                                        'value': 'Ӈ\x84ǀ\x99)æӺ˻ˤ¸ƜЙ«ǣΌčÈԮ\xadƖ˩ȀӵΚҋ·ʯšʮʪ',
                                                    },
                                        {
                                                        'key': '˔}ÕˉӎǎӀѥѕʒ¸ϞдɴϚʌͱǌŢԗwԎzɌΓĞiϲҶѷ',
                                                        'value': 'ʘ҆ҒЙƘȒƦϑ¢\u0382˘˔ІЎҁѡ}ĔĲʳҁӹɶԉµΞЍ˖ʍӁ',
                                                    },
                                        {
                                                        'key': 'ʍūɍԞǇӬģv~Ĕw҈ҰɖѽӈηΰγɴT(ȞF\x93лϲ^\u0382ԡ',
                                                        'value': '?α¯μʸϞıːЁǼŉʟхζɚҟʤ\x8cőӴӂί˸ΚʭđПΗλϐ',
                                                    },
                                        {
                                                        'key': 'Ȣ˷D\x82ȹăŗVԇʬ£\x7f`NԪӔ˕Ȟǌʒw˭дΞΩ',
                                                        'value': 'fˇЎƁXҐŏāӗҫʄŷԫƭ¦ʩņҢұĎΧҪȖι˲±ůķMӇ',
                                                    },
                                    ],
                        },
                    'comment': 'ȚǵӹȰƠ\xadŕӔçÇίϚ}ɰś˔ƁèʢʊЙНϕɲϕȳĴc˗\x84',
                },
                {
                    'keys': [
                            'ǠɉʎƙӐϼj',
                            'ĵɌÐϙѲŀĿҦҖ0ӫ',
                            'ɟҟ;дϿӎČ_ѾȧЌҾ˄\x9eǗҽȱ',
                            '\x83ȶ',
                            'LкҠ»ƨѪԧΑτȽ҈àǳÛ\u0378ǘ˫ì',
                            'ћëӺԒПхƺaÉӿn\x8c#ȝZ',
                            'kVѨCԦʻÆ˥ĐǑƎƭ',
                        ],
                    'event': {
                            'target_id': 'ΟɞȐЌơɰΖԆΛǹίßѺȍ\x8a\x84ѐÆφȵɦ˃ԃhɹĸǿгәľ',
                            'parameters': [
                                        {
                                                        'key': 'ĵзϕǱ_!ϡĻ¹YΆˀŨǇŸԈɄǲŮʘϩĄĵκ¹ɿaȁТʠ',
                                                        'value': 'ɭƛǃ˨ѽӶѧϢѬΧʻѸƽȵǔFʗȥąƻтʱҫ˄ӉǠȯsШŲ',
                                                    },
                                        {
                                                        'key': 'ʔ\x80Ѿϳ$Ĩ\x81˗рӚÖʓз@ʛŻŒʟāΎ҂ъ',
                                                        'value': 'ʄǍŤѹ҈ԉʜѳǾzтȰ҅ÈŬȱӲҲƥÍҪʀξʜŗԄͶϠьΈ',
                                                    },
                                        {
                                                        'key': 'İƎȜĀ<ǘЏӒ\x85Ϳ(ӪԬʣpҺʼӽÆ"E\u0382Ŗ\x92oÊǨρTԓ',
                                                        'value': 'ƽӇԐōϟüŻ°г{ɟτҁѢƄγȫˬoγǞʇҊŔ²ΩɼҏŸЃ',
                                                    },
                                        {
                                                        'key': 'aóƂ¯Ǜ МAɬϴɊşɌѿȑ)ѫʚįΪԚԗӀʅӞoɏԔǽǩ',
                                                        'value': 'ЦrȜͳҒ\x85ǣɾӝʙȕԝтӄŶ\x84ǺˑĐTԐWČʺźř˚ǌΙƞ',
                                                    },
                                        {
                                                        'key': "$+Ɩz˧ʵҽˀ'ɟͿʒǼ ϹѩȲD¾Ýƈ½\x97ԤȜŔʈɡѡľ",
                                                        'value': 'ŲþϫΐÛǨ˂Ǚ˔ΐ\x8a°η3ѡҹ˛šԞļӛėâŭʢϷɫƂ¿Ԟ',
                                                    },
                                        {
                                                        'key': 'ӪƠӿȱy1ѡ+Ԃ¹AƘʹ.ɟòʩϫӋŶѣƭ%Ӏ²Ǌĩ\u0381ӵ3',
                                                        'value': 'ИĖŔˣ˾ȖžĉΘ\u0379зòŸѯ˼ς\x83æɖтӵ\u0383ȝǨʠ΄϶ɴĉċ',
                                                    },
                                        {
                                                        'key': '_ɴ)Ԇόô5ЏĪ˞КOɍ¤ŋēʈʑ\x92ʔ˛Młӎϫ\u0378§ʅ¨ŝ',
                                                        'value': 'ŏȬӞśѯîҕ˝ͷԜˠŤ\x9a5ΩÿļčԝӞӾǇÐ˘Ӌż϶чØ#',
                                                    },
                                        {
                                                        'key': 'Μ˘Ӓ˞ʭʢ˨ͺńɍ;¹ԕq¬ϾƏwҗ˞ҬǷъ¬ӻ',
                                                        'value': 'Î҂ѓÚə˳ұ=PЭưpʙɩ˒˖ʞWӟżɐƍɌӚǮϫϻѿѠ҅',
                                                    },
                                        {
                                                        'key': 'ǧ\xa0ĤΰϵǪƁЎзƟιʳȺоźи˳ʰƋѭͶżѺӂδƦ.ʅӇј',
                                                        'value': 'Й˭ηbϐªÆːԉƩˣƥƴͷγːԔ˵ҼņȔΠҼɥ4ɹѦԍΏÑ',
                                                    },
                                    ],
                        },
                    'comment': '˵ǋɄԜѦҡėǄ˶QΏìδӦüȫлԫÖ2˽ŇӻȘʰΣ´ʊώG',
                },
                {
                    'keys': [
                            'AbȆɯſѷȻ϶ӹȮɃńӤŒɅÉŤǳϑԬӥ',
                        ],
                    'event': {
                            'target_id': '¿Ǧɗ˄ӭΗԊɰrϜƺ`ˀÙӿʸӮƍʄ\x81ЃԧΰöÇƶʟ]˳Ӭ',
                            'parameters': [
                                        {
                                                        'key': '\x96˧øÂЂďБʁHºҹҹąĘʶľ°ɕñşˈҒԘrАПǇӒИʆ',
                                                        'value': '\x81ӡҼΉ˚zɒp˧i˺ϵä\x82ȌΕ÷ԫ\u0383҆ж˨ȋÕƅŎnÕȾʴ',
                                                    },
                                        {
                                                        'key': 'ɞӁÇԎĨɗȟǱʒæЃĜҍ\x85ӖȠȞŜ',
                                                        'value': 'Ͱʇψıƭ˳ăƑԦҾ\x93"ѬɎͶδҲώѐƶĔ˹ϚϪċȤ˳˟Ӂˁ',
                                                    },
                                        {
                                                        'key': 'ԋŬпʯ7ͷȘ˱0ѵǛ*şǨ:ʥϕyаǢWʁBĩɗ_МԦΩь',
                                                        'value': 'ϔįĺțШˍŝ\x9et¦хǔВŁΘЪϽԕѡ®ρ˳°νĎĜŃʉѕǢ',
                                                    },
                                        {
                                                        'key': 'ƮѺϰĤÇύIҺüϣʑƜҲΓˑͽǂӔɥħʢКǀБ\x84˶ƦӸȀǝ',
                                                        'value': '»ʴ`ŰʹΈĎũˎƗҮґƖǦʒŹɪѸЄʏιЄҸԇέҤgÞϤȢ',
                                                    },
                                        {
                                                        'key': 'Ʈ\xa0¶ƃԡɏ®ҡŃӋVɉʫ[˃Ȭ˄Æ˗Ȫ˅,ȴԤϤҾſȦϋ҂',
                                                        'value': 'ĜһðÍϐӁ×ӹɻ҄jÇͷҕ;ȎΞґʻĉπЬϺµɧËԙϯƴȞ',
                                                    },
                                        {
                                                        'key': 'ə6ԚňҌŊЖĔәέДԂʍιӁ¥ǄҜɀԤϥВbƉά-',
                                                        'value': 'Ǩ͵Ł¬ЛȮƪˎҽǱĂǡʪ·˱uӈȂȋʷħϋ˛ϷĨăбψӓȖ',
                                                    },
                                        {
                                                        'key': '҇°Рƾȿ',
                                                        'value': 'ЗЮGҾoǫĻЈɤӵί˳¶ҹѓÆИӔ\x9dƳʇƄҶɄϽщɅyӎҰ',
                                                    },
                                        {
                                                        'key': "ђ'ȯЀǝњнҖʕ˞ч·ĴӬӅƹǮЉˏν\x80ÄЉʫǣņųԈǍԣ",
                                                        'value': '\x8eϚtƁ$ˌүĶɚюύԉмȾƩìǫҙԓˀΒӘȨɮ@ȘĶǩϕҭ',
                                                    },
                                        {
                                                        'key': 'Ӄ',
                                                        'value': '\x9dԌůМɛχȂİǒЯЗˈïǍҖĢΐŰΛǀҶ˻яѕ\x97ωGʘʘʤ',
                                                    },
                                        {
                                                        'key': '҈úϩҮʜ',
                                                        'value': 'ϮͽèõȂuʷҡȇɃȡΉǛθÉʉŷƾӚІЗΏƱǆɞҁӁύџҊ',
                                                    },
                                    ],
                        },
                    'comment': '²īɝќǄǲŗЙȇHƻŤќϝϷʇϧ"Hб9¸ҕͽҖό˜˭ņ/',
                },
                {
                    'keys': [
                            'ȽȜȐϒŠ',
                            'Ĵʡŋ\x84Κƫɶȶ',
                            'ɔƪӳρčШÝͼѓ',
                            'Ыώ',
                            'Ƕ×Bѵ\x99\u0380ʸҦƤȢ˙ǫҽӴǄ½ϳȠΨӗ9ȏʹ',
                            'ʺǰˁҫϐžϏȇԥǓ',
                            'Ɨӟfɳ',
                            'ϻĥӾȪxшǽһѵӨǭ\xa0',
                            '¸ѹҳ3ŶʓΚƮуҸ˳˲˶˅Ԝ',
                            'ЖΪĈǀ#ɶυȒΏΠ',
                        ],
                    'event': {
                            'target_id': "RȾɒɃĉǆ'ҮǏӳˠҀʚЌ˘ǺƠѰ:/İϛƅ0тƒҎӔΥʘ",
                            'parameters': [
                                        {
                                                        'key': 'ҧ\x9aӪΞ\x86ӢÌ҃ʅȀϪɞѳ\u038dԢӯЧΥ¼İΐȅʘʔү˯Үɡő\x98',
                                                        'value': 'ЉƳũ\x96ȄͻʄŜѧπΊɆԕƟƅǈɖ;ӉԄͿǔ\x93ΣˣǺ˱ʅǖ\u0383',
                                                    },
                                        {
                                                        'key': 'ȣɀԨԄǥΰ1ӴËӰ˶ԝ)ɹțȍ¦ҵɪӐԞʷĢȉƪԙƮɅȋɯ',
                                                        'value': 'ƽԄ˕ÏΤҁӅˋǱôûӤРʿŖÐȱàίƹŪ',
                                                    },
                                        {
                                                        'key': 'ǨΌ\x8eΫɳѮƨϘʣhEΦÉ҂Ӡʹ¯Ð\u03a2ǩЬӟȝæNЌѾƚ\x84ȍ',
                                                        'value': 'Ö\\JԦԨˆńӢӟҁАǚmóѿɘʡíϐҭƳʵʈȵҌ+ ʱϢÀ',
                                                    },
                                        {
                                                        'key': 'ǕӕˏŜĕËЧҸȖΖгɄҴ΄ҏƢȧqȥ/\u0382ʺȣđøêĲȔјԐ',
                                                        'value': '&«ƷѦӱɻ°ºʋͷĥϑļǜȻƱϘΕ<ΚŅǝ)ˍ\x9fëŅƮθѽ',
                                                    },
                                        {
                                                        'key': 'ƩɀҀэĤęʩӇŗҏȭÐêѽѣʠэų9ϿХ0ưŜȌĻ{ьʎČ',
                                                        'value': 'ьèͺЫҏĊĻӓϭȃԈd˜ʱʉ΄¬ȬҭˁƑѽĥϷəϙžĘϫЫ',
                                                    },
                                        {
                                                        'key': 'ͼȰʈýuƂʗ\x8dԬνÌɌҭǝāυżЈҵ҇ϱϝǀʔ\x9bЗйж+Ӵ',
                                                        'value': 'ǆҗ×ùĝσΰɰÇȬӝϙωϑЍ3ϢƋӕ@ҢҽКʷͰȀЫKǦʔ',
                                                    },
                                        {
                                                        'key': 'ҤƭŉζѲҦ\x91ǖŲȀĖŖ',
                                                        'value': 'ǃǶ¬ϵąѩÌӬъ%жӞŊĒМЋƓԩϩǨe5ɱŒìŮ9öƆ:',
                                                    },
                                        {
                                                        'key': 'ų¹˒ѐɼȏΝôόӜʹ˅ʏ\x9bÛ\x90ʻωIÖŭɳŅƲ˙ι¶ȡ±ź',
                                                        'value': 'ӶԍŌćϞӨΚŹХ\x97˼v5ͳɰǿӒɀ)ő{Jʗˌ\x93ɁњɿҤɁ',
                                                    },
                                        {
                                                        'key': '˕Ȑ˷Ō3`Ɇo\x84ɹâΰʶ\x88',
                                                        'value': 'ЗҦ\x8aÀʴʦĳOˑɠÊ|ђǝʈϜŖƩϘĶ\x87ϵŎ?ϩ˥ЙиРʵ',
                                                    },
                                        {
                                                        'key': 'ÂʼȽͷʃȒ\x83ȩƣЕΪӽЮ\x95ŃϗΞǿ{ώєΘӪύ\x9fԌԏΉ`ɿ',
                                                        'value': '¢ќǺžƘÊʐәɳȃ´ɌɈсɁϜʤǿѲ˄ΣԊӬњ\u03a2җ\x85оɰΛ',
                                                    },
                                    ],
                        },
                    'comment': 'ʹςģǊaϊ}ϿӓԌÝЉƙԂÒԂśйļϊ˙ȤԐəñņӅʕǊG',
                },
                {
                    'keys': [
                            'ʮŇ.˲ΆŞ\x96ˁȁӣˆ5ѺY»ɮʥ',
                            'ĉʗϙȏü\x8d',
                            'ʍÈ˛ʧƖűȂсěԔƇ˫ҳ0σʭĦ',
                            'п҂ƙʜ',
                            'ɛЊНӏ\x8f',
                            'Űřïλ',
                            'ǄɻġɽҀϢŔȃɤʈũΤЕ',
                            'ǏÒÒˣʊȇɲŏ˒Ϛʯĳʨ\x84',
                        ],
                    'event': {
                            'target_id': 'ϝåŃѣӧǤĦȘĔӿƱώ\x9cːÜςίșűҲɲзͷˠʖͳˌɬ®U',
                            'parameters': [
                                        {
                                                        'key': 'ǖҺʈǋПĖYҜŤƎʰǻɼƼƤѪ҈ǝĝǌǦʋѶǷʂ\xa0ԧʡјƎ',
                                                        'value': 'ʏѮʽûǸʩ\x8bťńYʼâ§ӎƧʰҲЅΝɑ×Ѳңöŕ\x91ʯӘ|Ѳ',
                                                    },
                                        {
                                                        'key': 'Ԝσȣo\x8cυϼħώŒńġѿөҋɇǦφʘü˥ŰȼĶ@ɨƫϦǃÓ',
                                                        'value': 'ѯӡԓøɺTƀțyΗ˒ΤΧϫɠЀԔ˕jƽĄȳӖÝˑҝǨϮɛˆ',
                                                    },
                                        {
                                                        'key': 'ĢϧιЊȄˍμΣӃҎɾɚēυħ~ǝÀƊ+Ǽԇ˶ŗήýȄэȍԇ',
                                                        'value': 'ӶέΡÐўɦϺ҅ԙЖƁЛяӢƛƪʽŃŅҨӐѷʻ˪KĹе\x97Ѿ\x99',
                                                    },
                                        {
                                                        'key': 'ƾдϛӧ',
                                                        'value': "ǱȾΩ\x8eЧǵ*(əÇĬǽмѣƎɁâüʴԚ'ʦ:lϼɌνɜœѓ",
                                                    },
                                        {
                                                        'key': '©ѭŜ\x83®ҸŶκìҭĉŠƇǝаЙӧЇӣѱԜİȺ"Ѡʤӑ6\x86Ȭ',
                                                        'value': 'Ҙ5ʹЋeτϳǏԥӄœǒϠϯƖԤʈΔËӚŇϗ˰ʆͳʹůә2Ȥ',
                                                    },
                                        {
                                                        'key': 'ćÚ¡0пɘųɪΝʵюϛǶ\x92ɶԄĴƏǌ҇ɸźēΖĳӄĢο°Ѩ',
                                                        'value': 'ДšŁ¹ǬǞÆœ\xa0Ѽԅƞ\x85%ͽΦɍXȳ\x8a\x8b˫\x9d\x98ǧǾȥŘœѷ',
                                                    },
                                        {
                                                        'key': 'Ģ',
                                                        'value': '\u0383ͿɖԍЕӠƝʤȇǗͿʗѲ˩ŤТΉɚүï҆ԐǉԊ\x9fοŁ˞Ѳɵ',
                                                    },
                                        {
                                                        'key': 'ͶɈӀΙáҝѣÅϽϬҼԨлNƴǺĦƐK',
                                                        'value': 'ȗŠӋӅл\xa0ƵŦdÆǮϚ˗ȇϬi\x91ǒʠÙο˫ӥӍ˧÷ѤΘŤ\x8c',
                                                    },
                                        {
                                                        'key': 'ӤρЖƇҡФѾ¨łюƬĪǖӹ!Į¨jӼȘʣǣͽ"&¥ьŠÅΌ',
                                                        'value': 'Ĉ\u038dŻǑ϶ȗЎͶТüϢȧɱ\x95ĢǵÒмÉ\x91ŀĖϋϱәһȘԎȴC',
                                                    },
                                        {
                                                        'key': 'ŹŗƆϣtƋҼʶȢДҬ¥Ƒ9Ӛǲȋźʮ҄ϮƷЛɐģԆĒēkɃ',
                                                        'value': 'ӵӅԙʬњ\x89óɗȻÝό°œ˄ШӬÙҰβˣӐҨɔ\x91ȆʇɢȠŨЊ',
                                                    },
                                    ],
                        },
                    'comment': '¼ȌЃѺŒȅяàʹУ1ŕˣċŦŔţɹҳʄǻӨȪMɺ\x9b"˒љӪ',
                },
                {
                    'keys': [
                            'ґʫԑ.јɞgǈĄһ˪ʵZҭʷӷưѾӻŊʺǷõ',
                            'ŨӻϥͳčǱˏъζоΌьЖԦÕÂʜϖZУ\x99ȷǫҎ',
                            'ʗ´¹ĚϙƄӂҏgɕɸǩżƥԓɊɦĬϊĐγɬҝ7ϯԭɞ',
                            'TԐ˅љưΠӞξÆìʨƌӵѯ',
                            '´г\u0381TъщϳҒΚǜO',
                            'ΟΒЬgӔˑǻŽϙӰҽҔҒЁŰЭ\x9füɫ˖Ő{±ʢϖ',
                            'ƻЂҘűΌάőʅШΣïѓŴ÷ҥÁӉŢҶġ]ȕѺң\x8eeȆҷ',
                            'ϟčȔ\x89ĮұЏϭӬ',
                            'ńǿŸυɭšǓƄŧ',
                            'σϜ[ϟʾȫԔëҚʓо\u0383Ҋˢ\x80Бųŋ²ĥ˓ΓƱҦ·ԄӉЎя',
                        ],
                    'event': {
                            'target_id': 'ɜ΄кŽМOЭ;ƟíǣΞɉɳ˄ʙқѮɛȾӣ\x87ĩ\u038d˷ȩʬ҃\x84͵',
                            'parameters': [
                                        {
                                                        'key': 'ǯΊӳśŊӿӹЬɿԘśǡˬSϹѶӦΙ\x9dǗŹұǁΈˑeƶ¾ʂʹ',
                                                        'value': 'ɶȻԞŞϗǢӢʬЈππİƺ\u0379ӵÄˆΫȅƬҹʋĄӯԛҠ˰ӽѴǂ',
                                                    },
                                        {
                                                        'key': 'ǜʩƪȅӂέʉ˃ͺɼ\xa0PԞ<œȃΡ',
                                                        'value': 'ˉƱ˶ǥКɹȑЬ¥ΚƺϷѺȑӻ˂Oř[#дŗΩƅѱЪɤ˩Ԍź',
                                                    },
                                        {
                                                        'key': 'ʆφӊΩˡұ\x88ӀнȹǏĠʆȠƇ˔ӤȪKǨʱў)ƳϡɩΉѺˉz',
                                                        'value': 'ϞԎϱӈ˫ɖĮĶԡǧŊҥѴӷҢgĨцŮѬÐЅ\u0378ǫ{ȢʿȾ\x8eԉ',
                                                    },
                                        {
                                                        'key': 'Óǋ\u038bѝмõ©ĳ',
                                                        'value': 'ëƦåű%4ļǋ¶ͳʼʟϚѸϑőƿЦëѯĹӈԎǆӪ˙ŗʩɳа',
                                                    },
                                        {
                                                        'key': 'Ŀó˚ďОҚΘųƣƢ҉Ɂƚͻƅ\x88ȽĜɲӊɢƪТǐɆh\u0378Ё\u0379˺',
                                                        'value': 'ĺŉ§ěÉƅƘĲʵԍҩȺг˱ǩƽůôǤєƙĞ\x9aғĪџ\u0383ą³ĭ',
                                                    },
                                        {
                                                        'key': 'ͳӥ¯ű)ʄӝϧʙШӘɀƬ\x88һ]ČӲÇǚԊʫȼѫǕԅƲ\x98¦Ȳ',
                                                        'value': 'ΖŗƷƲΞҏ8юϏϣƽӹԀϩԨǜƕǃˮ˔ȯα{Ǯˬұ˙\x8eóҎ',
                                                    },
                                        {
                                                        'key': 'ѪυɤРÈϴшΊ(ɄöȁƏɚӎȿɸħоӋǨԥȩ˃όɁǳãԫЬ',
                                                        'value': 'ɱоΎԑӥȖӨ˗ΗϰЉ˓ΐ\x9fAʇӸɈˍĸƓТĞӦϔƮˏΖԈҹ',
                                                    },
                                        {
                                                        'key': 'ˉʱ˪«',
                                                        'value': '˔ҨÇƩû˯˦ʎ¨КӁɎ?\u0381˕ʩ\x8dѭăǯă\x99νƲŤВӲıʂӖ',
                                                    },
                                        {
                                                        'key': 'Ȩ®ĘƤ;ôǺӲǀƸ/ǤȾǹЊϪˈÔɡȮӅΚұ˞љP\x8dĽԏǱ',
                                                        'value': 'ʹЮ^ϷЇѫxγНˬɠʌˍǽĲľČ\x9aϠӌӾƨĶƐϱҊѽŠцΈ',
                                                    },
                                        {
                                                        'key': 'ҶúӯӖŀʌ˭ĴyŰʯȔºƉԄοхʒȏԥӰеşѼͽȁɑʹ',
                                                        'value': 'ƈԉҟ\x9fͻάΞΨȶŒÐѬΆψǗӃ»i¬Ҥы®ʣρŶϸϧīCҸ',
                                                    },
                                    ],
                        },
                    'comment': 'ˡɐȼƜgʹәƟ)ÈϽˉǤʨŧш&ńɛԔʫ\x80҆Ɏǵγȡ\x9eԜõ',
                },
                {
                    'keys': [
                            'пӣүɠӤƪƗɿѠȹʆØʥԑѿ˧ŅˑȪWƭȦϸ¢ưɷҼ<',
                            'ˑӾýɵцȳΞǖԄʞɮӦʘӒˊʕΉΤūΤÆǊȊϠ¡ ƐΣ',
                            'pБǤʓ',
                            'r\x87vʽϘ˝ԚѐYʪ',
                            'Ȕ5Ʒ˨ϛ\u03a2ӿĞȨɊ˳ÛRŚĖɘȥӦɜďȍƘѺCç',
                            'ɈőЪΛɮгЯ7ЃβԡҶΪȋԩƄΛԪƔęƷɭ˵',
                            ';ӎӐǻȮϛҚïжӪ{ôģp°ΦĹ',
                            'ȈʱʼИXё',
                            'ǕßȋɭЉɇ',
                            'ǒҿɄӳƇĶӰ\x95҆o¢ŕΒ',
                        ],
                    'event': {
                            'target_id': 'ѱƣΥˍВ˂ƧŞ\x81<ϘǎĉїˁȳԥǾњ\u0380ãΙǔđ\u0378÷šҤʡí',
                            'parameters': [
                                        {
                                                        'key': 'ԒҤʒ˚JҋЍƦaƑǁƓǮɜƔȗӷ\x80˂¦č˩#ȪԝîӄӅÜϯ',
                                                        'value': 'ƃł˞ǱѢϒω˘ΩɆɌƮƛƼƾͺү5\x8fЛrϝ˂ɢԣͰÂΥѶѫ',
                                                    },
                                        {
                                                        'key': 'ӐźӴæȭėÜɅÃ!ӕʾMɯ҇ʘ˲ΠǐӛӮĦˮ΄҆Ӿƾ©\x99Ǹ',
                                                        'value': 'úҺŇȔ\x96¸ԮωŔ\\ϳńʡȃˬĽԮ/ΛШƦЭ҈ΛǔǞΰ΅ѲӾ',
                                                    },
                                        {
                                                        'key': '˻ʵԌȟ҅ԭǳɕʬċǉЭȄɛӁɒ΅RDƋ\x92ωʖԧƔҗæƹňE',
                                                        'value': 'ѿңӝ·ϔˋЈӛʶǎԁŌϊʣŦϳÂҧëΘʄgӅ6ȽԦ4łĄž',
                                                    },
                                        {
                                                        'key': 'Ȃԍľƽһљӥ¹ɋҍ}ˊ˛ť5нӝӪѨԬ˺ҤĩԚӏƚnʮÝǰ',
                                                        'value': 'ʘΗÔфĬːђʵˑΊȩAʳƎÀ©4ƨˏХӴĉÜɹÊkǍƅƶð',
                                                    },
                                        {
                                                        'key': 'ǧΚÉx˄їčŕυЖǤЪӼҵ˕*ſʈ˛èΞ\u0379ʼʚʰΣ˗ĹĆш',
                                                        'value': 'ŖȂ\x83хЋЭёѵϪéҁϔʻČȚѦψďʎϺĺ\x9dƀPνѱϪ¹õǪ',
                                                    },
                                        {
                                                        'key': '½MЂЏßɱȐͽ\x85ϸʏγӐȖ҈¹ĊǋɮӖƠϪȞϨ$ӺήtҖǗ',
                                                        'value': '˒θƫӒīgϋˈǽ˄ѡʽȌЮƮɎԃҳ£ĠƹδkʼιϚʤӹ:Щ',
                                                    },
                                        {
                                                        'key': 'ӕΦ\x81ҋрɢі˂ŀΎˁҒÉčәԄΌİ\x90ԥʌÞƫμҒÝ´ӵɓº',
                                                        'value': 'ɦ҃˭ҹǺɔӏρͻӲʱҤωʈѤNԉͽэƸ҇WΰΘʹăγV˾ȋ',
                                                    },
                                        {
                                                        'key': 'ȦϪǴɡëȡҷǮѠμ¸Ó&ǞΖÅʋ˒ůȿ8^ӽʖзśѤƶԒϢ',
                                                        'value': 'ҍ\x96ȷʂѾƣμͻʶϹĎ@*ʺÇѧѢ×£ȅϾIȷȠƉđȶǾ˒Ҁ',
                                                    },
                                        {
                                                        'key': 'ѳԧŜʻʂ¢ѩǤсLҎӧηŀɭĂϕɭωʃ˛\x9cЫţƍӷҭˍюɟ',
                                                        'value': '¨˫£äԀĎύҚǺǒƷɀнV\x88ϧΝбεŁӰǒȷĤ\u0378ˈ#ĊӦƝ',
                                                    },
                                        {
                                                        'key': 'Èʂ',
                                                        'value': 'ƢȼˏɥНĤЪδŗхҷȰΥɅКЩήɄɞ˥˻ʨ²ѣӸƏĹΏȚϲ',
                                                    },
                                    ],
                        },
                    'comment': 'ĮзԌӷϵǏӂ?ďʭϝ\u0379^ϹƚǧєӐ˺dƘzͿӣʕQϭɸǜԬ',
                },
                {
                    'keys': [
                            '\x81',
                            'Žćά(\u0378\u0383ӁØĒ˴ϗǤǃÑӮǣȴĖʍʭɛ',
                            'гȱÜųӮϙȪ¬Ͱ\x97ɻўʸѭǴʒӐǩ',
                            'ĥΎȐ;',
                            'ώưтο*@ϯˉŰiˢʉ<ýƠӰơ\u038bɖѤ',
                            'Ԛ¨ӹɮ\x88qӅơЀˑĩϸƱźήѨŗˊ',
                            'ЏͰԇʽϏϮˤǙɣӄƹȹ',
                            'ŐÐ¹ǇÏȯϧέԠɤɝƸpɛҢϙʯɡÐ\x95Â˩Ϝҹ',
                            'ԣ˅ȳ˽ȏÐ',
                            'DvѵӞƫϽˍͰăıÈлӹ',
                        ],
                    'event': {
                            'target_id': 'ĖʶЇѺԫʳЄʏγʕѮn`ɣЃşĥФǘѐƛìɢѕʜѸȒαˈŏ',
                            'parameters': [
                                        {
                                                        'key': 'ʜкĤ\x9dɰÔԦѷŶȔҟ©[\x8fPoȹ(˛фҾ΅ЈԝĺɋϠʄÒϤ',
                                                        'value': 'ϠˉƏÀʨϟ\x9fϵѡ¥ɹȶҺĹ/ɅŅκӛ(÷Ϫ|ȱD˜Қγʢ¤',
                                                    },
                                        {
                                                        'key': 'ԚиԓϟҊϳРÉʑƀʥНѼˇkēˬь&ͿТ\x9d',
                                                        'value': 'έΌŞ\x88ȗ\u03a2Ω\x9f\x8a\x99ȧș\\ɼèҪԍ˓ϕԄӲԊǯ^īΖϳԜʆИ',
                                                    },
                                        {
                                                        'key': 'ȭεěʧΒȬтÂʰˆѦ[\u0382ЄȉɯҤĩŸҿ\x9cǲѼӷρʗʽѧҌϯ',
                                                        'value': 'ԒȲèԟξȥBѮóɍĜƲÊǼřīӇˑˢɹѻ\x93ʸыЎĒğԖʨЁ',
                                                    },
                                        {
                                                        'key': 'Ѯӥ˯GƺωĿʹʂϪΆƋќSőщ',
                                                        'value': 'ԩȔЀ҇ƏЀ\x99Кц=ӕ¢ԧԮʞнŇΉcˣȺˡңҋԄXҮͶ\x80а',
                                                    },
                                        {
                                                        'key': 'ίʤǖӂûɺѼϽШǣɢśʯҐқȃ˥ХǐιρƷ',
                                                        'value': 'ʩϿũ\x88η`ºΆɜѮ\u0383Ǔ˒FŇȣˆGäʄĆǔĖʜŖЊǙύϒn',
                                                    },
                                        {
                                                        'key': 'ȼӄʺӓÛƇkcϽFАΌ΅ЭħÕ7ˎπŕĒʁŀˉĬ&Ǭ(ċ$',
                                                        'value': '͵)џӱϟРӖƅѻΥϔЕǿĖȍЃϖʘҊϐ\xa0ēδͷҊ˦ŸǐĿԦ',
                                                    },
                                        {
                                                        'key': 'ɛʕ£ĔŝϕΔKÀŝǜʮʢǴNӽ\x91ɃҴə',
                                                        'value': 'őδӳ˾ϣê!ΠͱӱŪʋÛӳ҇á,Ď˝·ýɴy˻ƫр¬ʿľǣ',
                                                    },
                                        {
                                                        'key': 'ťњʹςɬȊʖȸʷϏƪѠҘƭȊś,ˊƹҡ¶ӜӄNǟӔ»ѭñ˗',
                                                        'value': 'ҷ_ҍ9ԡΪЪȇЀɵŷȞҴýƽȄɨǹʰɕҳoӈËkҦԭǕ´ȗ',
                                                    },
                                        {
                                                        'key': 'ѺѓüɅǍ͵·Ԇ\x92ʁ\x91Ŀʎ΅юɅҚʩȔÚ8ŤйɏĞ¦Ɵӥȹʡ',
                                                        'value': 'ł\x98Į$ȎϡɈ҈ʒ+ҥĶəѶÄ\xa0ԬӋɖζʑÖΛmǄŻЀʁВƲ',
                                                    },
                                        {
                                                        'key': 'ѿǶԍǊѳʶŶȢԙȘӅǖ9ӇſƀĊā',
                                                        'value': 'ʥѓő"ƛĒԪ\x90ŤɺȣƤʡαðķķϙǵԘǕĢġіȗŁԞΞȭɣ',
                                                    },
                                    ],
                        },
                    'comment': 'ɔɅԕȺӲ!ЦԮҴƁѨҟķІ˧ŵǼѦqβΘБŭŪ°ΣΦġÔ÷',
                },
                {
                    'keys': [
                            'ÆžÊ',
                            'ӏϻlҌƒƺåӵëȕʿǲǵҋ±Эɍϣӏ\x94m\x93',
                            '¯ЋʺН\u0383ɐƱ',
                            'ʺщǂЉ0ȧHƾƿѐǙʝӁԀȪЬƦÛѐӰӳҶĂԁԧiɗƾƯ',
                            'ķъaɿ',
                            'ФĈʋΛӰǜňˈǦ˓υ°ŝѦͿƎ',
                            't',
                            'нԌƦѶʌӀ҆ӒŠˍĘѵυθʸΠԏǆЧƕ',
                            'Яѭƀ¥ѤÜҽɡӽʋÑÁѨ\x95ŌĄϛȎΆįɦŌ5',
                            "'ŞɼÕĴԕDҦ¬ɇ˽Þϧ\x9bƂƳŚѱ\xa0ŭӑʑɕ",
                        ],
                    'event': {
                            'target_id': 'ʹĠўɇСЩƚҲİŷ{\x9aɕйΆȦěпȟ(ԛÛųa\xadȔƨɑӶɎ',
                            'parameters': [
                                        {
                                                        'key': 'Ҏx¿ÄŤƑŬȳ˱µŕeӆϷƈρѳ=ʾӀѬÈѾӘңӝҩÍƹʰ',
                                                        'value': 'У˔ϟĖ϶ϚżÐϞƕUϯαѿsĉřʣ\x84бmoɥɠŋӻ·Ǵ\x83ω',
                                                    },
                                        {
                                                        'key': 'þЀԇҬ҅ЎϑϵѴ˂ĎʙƜӘÂ',
                                                        'value': '<ӧӎƕӗӛÉʃȅҕʣFȯҵԃʍҍŋ7ÕpʫГ6ɲɐƫ¦ЇҦ',
                                                    },
                                        {
                                                        'key': 'ˮ\x95ӹĨƾм\u03a2Ʌԣ<ϪiϙȱΔſȌϋˊԧáқʃɰɡèʕϝҮ\u0380',
                                                        'value': 'ƉпѥòǱϣдλĬŢÄƑqҷŅʨаAƗ²Ș`ѬȧƪŴaˑŴď',
                                                    },
                                        {
                                                        'key': 'ʗʃȣǓțф˷ʣΑϯƤǬʡåԁϓˍƫԌÞ4ʯɿщҹЩӓƛ\x81Ҫ',
                                                        'value': 'ɌǗǋˊ}ϵˈˍшȦŤɶʔдÌСŕϵ)įӪžưŶőӼбɛϷȦ',
                                                    },
                                        {
                                                        'key': 'ĦΏɖš~tɒ>ѩ\x98ҎɚĺЀөЪЅш±ԝқщÇƦĶљҍȸˢĎ',
                                                        'value': "ӱԗǖņńüŻˏȾ˹˩Ƴ{ʹɍϏƏƒ\x82'ϓǭӠѱ˚įӜ˚Ӭφ",
                                                    },
                                        {
                                                        'key': 'KƟZӣǓ˱ɩ:Ý˵Ң\x97Ɂӊȱ{ѫ\x81ŧӋ7˙¶1XŜ˱ƈѵȝ',
                                                        'value': 'ЁϼöļYéɒі,җ,ҾӏɕȰ`ʓƁΫʶƪǌЖɉŅ\x93ǐ\u038dļˢ',
                                                    },
                                        {
                                                        'key': 'Ӂ\x93ϣ˯ƋĦɄȶƲͽΉ!ˣρĠgИîϻʌɄȪπДŬ±\x99ʊ^ȕ',
                                                        'value': 'ԃɀНǒXЦÌȭӱʒÐ˹ËÔў˄˩ӇӿŐϿԝĆŤʁǋˁфϳ\x93',
                                                    },
                                        {
                                                        'key': 'яҦɽϾ»ӤÜTƲЯɩөгϰгǓхʕbӂ΅ʹ®ӆɸύϙөҩĺ',
                                                        'value': 'ʚѵcϬŸƭʔұӉǩ˽\x98ƽДȴʟˌΫŃ\\ѥϜϲ˻Ȣŋ1Ӭŭſ',
                                                    },
                                        {
                                                        'key': 'Ы¦ƅҜҌȰ˰ԌьǮˊ\x9bϚÒ¥ԙ{',
                                                        'value': 'ɂÃāЙγɳƇ÷ɩψǚĽǸÄ˸ÅҰLƉϵĚ\x89ÙŉɆUƎ\u0379ȧν',
                                                    },
                                        {
                                                        'key': 'ƨƑð¹ƌҲpƓXεǥīơΐȮɝÅҿĥǢșӻѴʶtþɨƠѓд',
                                                        'value': 'ÙκӾ˲ȌǻȾʃΜΩѿԂӝӧҲȷѳÊɶόƖȖҫťҟŘѹŷȶч',
                                                    },
                                    ],
                        },
                    'comment': 'ƢĽb;İæϋˢȯиʫ\x82Ȉ˃è˽ΞшʝԮʦ҅Ȥ\x94×Ӯȿˊtȹ',
                },
                {
                    'keys': [
                            '\x92',
                            '«ŎËȘȉƽͶԈҮԝ˩ǲY\u038dÞPɮɲgēǫ',
                            '°ίƊӐԮҮ',
                            '°ý\x92ȊΩ÷æӻɐȶ',
                            '\x89˙©ч"΄˽σӧʷˢОXћTԌ\u0383¾',
                            'ċǴ΅Á$»Òԩr',
                            'Ǿ',
                            'ϲѣџȤɷɄînγʙĞрʙ',
                            'ԋӂɟçʘΨϦϋĞǃ˳ҋĐĖâȸӰ%',
                            'ėǢȧԁȞүЕÍΈқԞŦӍWXԆеϷ',
                        ],
                    'event': {
                            'target_id': '˄Ϙ\x80˼ʕŶzϡʌȚԂɕÇ°ƽʷHԆïoԌѻѢȋƲκĩȊǦ£',
                            'parameters': [
                                        {
                                                        'key': 'Ϊ\xad҅ǭˍōƄ˘¯ɚż˕Ѻϴʘ,QȹύŹǌȸōΌ˞ΩøΌԌљ',
                                                        'value': 'ҭћuϭ˩°ȆϊƐ\x82ƭʧө3˥ЖяέļӐОɕlŁҚʿƳӄȊĢ',
                                                    },
                                        {
                                                        'key': 'ŚΧ¬ÏË',
                                                        'value': 'ҴγƩ\x83èeǮӽȫȤɠƸêЏɻãӂÿŦЧҊӰPɺϖҒǖːԬ˻',
                                                    },
                                        {
                                                        'key': 'Ŧӥˀˮ\x84Ф',
                                                        'value': 'jVʊҔĿԮ¸ɴȴĢūҝņͲʪѠɎθĳ¤ȑĮɂ˻IÕʬmх^',
                                                    },
                                        {
                                                        'key': 'ŏЕŕԗϔʹΙʭɃώӉʜɕҽ$ŀ',
                                                        'value': 'ϬӞɌԉė˺ЗʵО@ЈΜɤʡȮəѕˡ%Åǩ2ΙЮŅM˼ŉɀɇ',
                                                    },
                                        {
                                                        'key': 'ϮƘǇ΅ȡФȝÀяʫʢ˟=ƧӞƖ²ӻǆӇҘиӉȀȐӈНӀшʑ',
                                                        'value': '\x92ĺņыƧԣȵłԁӓȰǽǠȁȣΫ˃ÓԘǷӛɩdƦѥ.Ɂѱ¨\u0382',
                                                    },
                                        {
                                                        'key': 'řǂɘȻ',
                                                        'value': 'ŮǎȔŬԤɸҹŻʃʊ˲ʖƾǈȮƆƟԛҷЏ5ԑȵǊĀɩƠЎŤ{',
                                                    },
                                        {
                                                        'key': 'ϺӂȰ ȣʹŮ˷ЧǰϫśπǴϮ×ɇΣžϑɟȠӲȔǉͿϺͳƆк',
                                                        'value': 'ԇϙɵΗéƸɅʸßЗɒRƅ˦Ό˕ŘȨ¢ȎÎčѸǫоĳ\x92\x8aӡ˧',
                                                    },
                                        {
                                                        'key': 'óҽɰŽwѝǓÌɄ ӎɖˏǟһpϪƬӏʷόœσϜӐΚŇ\x94,Ƴ',
                                                        'value': 'ÁǗɵɢƹЦ¸ʒǶŋрħΣ3ɣˡʾYͼɐǬ×\x95ƟȟЃƀϻîЍ',
                                                    },
                                        {
                                                        'key': '˃ЙԦŵŹˎÝϪ~ŲԒɪƷёśĭŧњŔ~Ȣ˕ƢѧǇ҆цЖŽϮ',
                                                        'value': 'Ь6ιӄĹGƪēӵFə˪ЁɒϻśΧźðί±ӑçϟȪˍƭρΚ{',
                                                    },
                                        {
                                                        'key': 'ʹęƆкҊʪϬέƊʀԒƱьӅɀƟŃʢÌǔʒʼ\u038bζӧǘɢӊƊ±',
                                                        'value': 'ҫѨϩԀŁìʿƥѼʚƟϱɀϧǘȪˌʕτͼʇ²ϥӘ҂ÀԩȏɴŰ',
                                                    },
                                    ],
                        },
                    'comment': 'ӧáȃӀŧ[˙OʝǏӨĺӪӟЗɲÀȷǟǴ\x86Юʖĩż\x80iIȾ\x86',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'Ű',
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
            'name': 'øřԠĳûĿȻҚȀɆυ˄`ȗǺĆÁ¤ǺȣÿϺϘӬâѷƤĢΧ҃',
            'description': 'σΆТә¿ϞιÃˡǝØӕǺ҄ЉЈŲǜľΰ&҇Ы³dΧĤЇ˒ǎ',
            'target_id': 'ϓ˒ɐú=эǆҟùŷµµtӻ)ǪɤȨÿѥ*+Þʡ)ɫí˘<в',
            'parameters': [
                {
                    'key': 'Ʒҧѷζȸ~υ\x9bұпǨȥʌf~ġîѝȑʋÆ£эͺӔŚ\x98˄øˤ',
                    'description': '«£UɔѠҗ˚ӍϗмňʋƪǅϜƐдǆ\x8cʦȜϕǋ˾ȒˌũɟιϷ',
                    'default_value': 'KļΥhҞԦЊыƘxŎĳʗ˘ăεʱĪ;ͷΚĐqǫԀŭϨeʔƏ',
                },
                {
                    'key': 'ηóȻlͼȂZķɡѸʶǖƴɚύ',
                    'description': 'ͺҌάŻҖƟđ΅őԣĄҼƠϡɪ˔ƅͿԤΡϧщϝĔԞEȟҊЛĦ',
                    'default_value': 'ЉʭĺȀҧӿӇė-řͺďЗ$ǍЫĽԋԢыŜƉĠӯĜҒƁɧĮΉ',
                },
                {
                    'key': 'нǓɟ҄ξ\u038bȫjҫʸɾÂĖǯǑƥӇʹҥУΙǘʮΞ[әћ\x8cņʡ',
                    'description': 'ӈůŅ˂ӌБ\x96ƞɞҙdϜЀnvɊ8ǇȣҜ¯ͺΑȃΕúʟҊĭҹ',
                    'default_value': 'ӱΰұŗҔǾîΔȌʯΓĥǷԩ\x87ǉΊƉʈś\x83ˍ<ʥɻ:ĹЖӘԉ',
                },
                {
                    'key': 'Ҋëś\x7fԓǶŷ`ȕŗIŖƪɮȈǅ¯ɚ_ǋɄӼƔәЍ0[ёŶђ',
                    'description': 'ǜ\x80ʸȪʺŻęғzӭò\u0381ңхиɀϏ\x98ɹґæʛȻȋͻƓöûіſ',
                    'default_value': 'єѠɇ5Ӛ·SŅӨϤәУâԡĕŦɁєʑԩwìѦˡØњӇ˝ǷД',
                },
                {
                    'key': 'ΡĨ©ȭƎ',
                    'description': 'ϺĘϞǴϮ˞ԑҫȴϭ҄˭˯ȉӈȑţΙȺԝśϾ\x9cǘΐͶОМѺѐ',
                    'default_value': '˨ʨˡЊΦƺҒд\x89ΥѸԗĽ˩ŪɝġГѕʞҙʡΌʃ\x8eэ~Άӫӂ',
                },
                {
                    'key': '˚ǙԄԩɤķлѽͷeԩɎƘӋʼΪяȆҒаƱyȴqȨҜПӯϸâ',
                    'description': 'kȯŸë¬ǻӃɆʫЦ˨şӞϔҞˇǹ\u0383ŢѐӷίԙͿ\x7fӍĹ˃@Ѭ',
                    'default_value': '˴ӼĶНщγ5ҁΞάʾӵŕҮĊѽśǨʢȐîŐğȘŨϛĩĪ;Ή',
                },
                {
                    'key': 'ӥǰƿ,ʦ҂ȇάΖ\xa0ɰӡǐӽԝ¹ђȨѧƯőƲƞϱŁΔaËĆÀ',
                    'description': 'ÄчҚ|ͽǠӲӋ˺кԌƅǦι°˟àˀƱ#ˆԢʽĕЦMȰϾĚԇ',
                    'default_value': 'uѯϸ=ʙқьӭÚӳƝɢÇ/чˠΧɝȀ\x8dʝƗͼћÛ˺ӫ˂˱Ɍ',
                },
                {
                    'key': '˰ʙ',
                    'description': 'ҙǅԉϻŬáʓk҅ҲϗѾǘŻɎŧɎȡɜѐ˸сʭÛŲăУҩȬs',
                    'default_value': 'ġʃθԞЖʷȕϚѾĪźn҇ǋͶɨ\u0378¡\x9dΝҖȷѢΔˍӫ?˫έɅ',
                },
                {
                    'key': 'Ѯƙ˲ˤԏʃȤ\x91hĮȨǚDϯȝ\x7fƸӲƇϭҗΎʽІĐŃÉłÆϪ',
                    'description': 'öϚǯāŵѠâЀXυϨ\x84ØρςЉbòǼѝӊɕſʭțżĳԔɗƢ',
                    'default_value': '˼Ȅ\x81\x9fϊѩʏgʭ\u038dԇ˙φηЌɄ[δƃϒį}<ӫΗ,ǫǝϵÙ',
                },
                {
                    'key': 'ĮÈïȍɥʒ',
                    'description': 'іÒќ˒`ġЎҵѪƾ΅œÍēʟ˥ϰQƢϪұǤäʞcɑ&υʽȫ',
                    'default_value': '¶¯Ǿÿхԣʪċρ1ƀʛѦǿɡȞɪӚ˩ŸԟĴюˮɯ6ƶϪȞʫ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȏҁѴ',

            'target_id': 'ɍʧȓʅȶ',

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
                    'name': 'ŇϏԇŻˉưȝΊιңuΥȜϪӴǸѪǬòƉӤÉɽʧº˦ƗπƆǐ',
                    'description': 'ˢ±ɶӅӵʉιåøρϽɝç/ϔǦǭĬƨƋҷ6MAŉϠȬƧ҆t',
                    'target_id': 'өґЧҔJïŨ,ѰԨҁҝ\x92ыѕCƊQ;ζʾȒǗ:ϲİʉДÎQ',
                    'parameters': [
                            {
                                        'key': 'ʹӱʂȰ',
                                        'description': 'ƞҲǏń˄ć҃hЕ˕ĂÔ\u0378сϧƛʼǐӰϱβӃƭȯǯƖӪбbϢ',
                                        'default_value': 'ðϔǐˠƌҽ҃ƮǄʰғӇӯәǈӜFӅ^ǀƸҁЖƿϰǤǺɰ*3',
                                    },
                            {
                                        'key': 'ĠɧȸɖЪˏҲɈԙ¬şĳЉнЛ˟¾ҥѯ\x82üΦȢěΧŐѷОȱς',
                                        'description': 'ƆΐӗӸɋǒɺˆϮşҒΗȬԁȣϨȒsş\u0382ŉȈĭĿʸ˕τǷųѝ',
                                        'default_value': '-ŪǟǎӰdǰʮԗͻфȌˀƛЌ»ԑ҅ΏƉ\x85ğћÈϙ!Ә¦ćʟ',
                                    },
                            {
                                        'key': '\x85üүǡŅáЅːӄɑŜƆʹñʌϙёԓĄƞWӭĒŏ¯˩ƣӂș-',
                                        'description': 'ʱӊѩĆ+\x94ЧɐřҷǈĠҞ\x9fzǽьGºѠâϑΤø{˸8ѩϖà',
                                        'default_value': 'Ȇӈȍ7ϰ˫ƗϺϰɠØ\x8dǹƠϐÆөZә\u0383Á\x8d6ɞͷʎǧć&{',
                                    },
                            {
                                        'key': 'B\x8bΥʑΙ϶FȱʧȌƋ/ϱǩ\u038dƸÑʉӜӸӺ«ňҬ;ωÎŲӭ\x88',
                                        'description': 'ӶƑϫӁÏʐΖϯçőʁЫǐɇԟĤ\x84˚īʵʛ҈Β¿¿\x8cƛīъԦ',
                                        'default_value': 'ʍˋǷϓ\xadȷˁ~ƿЁЛ)х҈\x8bŘ\u0379őǫÈɛŻҳĢǈǖѝ´ЈǨ',
                                    },
                            {
                                        'key': 'ɢɢPűɓζǈŷȓҳǾ9ҡϨəƍrӓѽŽɆҾҭĿƆΞĳûѾҮ',
                                        'description': 'Усcŏ]ˆ=4<¤ƖǾΪǤʗĻԨūnĳʳÓӚ\x87ӴʮĚә Ύ',
                                        'default_value': 'ϫǞ\x87½jўȖƅҘɩέ»òǫĩʜԔ#γȪϻȭɀҵŊ¶άȕĞӻ',
                                    },
                            {
                                        'key': 'ƜӟЁЯ͵Ȕɺχ\x98Żɨƙɶƕ˂͵˳ȔĿȮʎдРèѬлʩəӥƁ',
                                        'description': 'ԤŀɣʐɥӔ˷ɒԎќƫҵťʼɄπԖʍȲ)ԮSǱӄÊεȤƀÈҭ',
                                        'default_value': ' =ȇѐʎoÑԡ\x90DΚώΠGϿɊԬǢŢӭİŵvưϵƈǥʾɼԤ',
                                    },
                            {
                                        'key': '/qŽĈȀȚǭãøǇȋ',
                                        'description': 'ϬĞ(1ĚӃƚѲȪϕ\x90цſ¬ɗǻҩԥ˛ƞΡȰÛʚʤķӿҟ\x7fȝ',
                                        'default_value': 'ʽϩʖěɡ˄ĮǏøĖìѩęĈĚ\u038bȩҧ¸ȠԭϳÓȈһsʬԡӐā',
                                    },
                            {
                                        'key': 'ţ',
                                        'description': 'ǡ|ЊБѮ\\ЬƠm\u038dԮ¤ƖΪѰɩŬȹɗϛҍЭ˂ŪӟбĴԦΥ&',
                                        'default_value': 'ƖʞʬħƏĥȰȆɦɟθ\x83ȶǚϲњ#҃ƠǗƃҫӐҥʙͱ&Fc˳',
                                    },
                            {
                                        'key': '\u038dƈƏͻѧiÉȇԃǃưɍÔ²ӿİƓżΎӬԟΪŌюϛÏɈɎͻĒ',
                                        'description': 'ǥļǂŢςӗ@ԐŒʞ@əɰ-ϝĈӜ˝ѰӠ҄ѯԡͿҜôԟКęǮ',
                                        'default_value': 'ϻЫjϰŎk\u0383ŚӫƯгƃҫѱҶԊʍΰ˗ҕ\x81ήӺˏć\x7fӋïɱ\x9f',
                                    },
                            {
                                        'key': 'ргƠ˫ǟл¥ǷȍðКȘ΄ϐʍč/ȕʮìǯȅ˔ȠůѴНԈŦ\x8b',
                                        'description': ']ɱʤԀZԥɁũŮзȹшҒӴԋ~ʹӜǂÅʔ˛ȌÏ%ʱȔÌȤӃ',
                                        'default_value': '\u0379ɗïǌȸцȇѲ`ƠI©ҲŁ϶ϥҥ¹ʺˠɠȘʰȰӌӬͻûĞŃ',
                                    },
                        ],
                },
                {
                    'name': 'ǣѩԀǦńψ\x80ͿlͽЈҍҎǀ/зµɿƥӇӱÈιͱ\x9aŢƬҧцȁ',
                    'description': 'ˡйҋɡѧжɐƩĆҺņӒZϒԨʝāΧʚИӍNǊĖȳʸ\u0378\xadɦé',
                    'target_id': 'ӎi\x9fҎƥФǊϟŌ\u0379åΔӪƩҌ˫ԨßɕԠʀҟŻϚҔӣӍòʥK',
                    'parameters': [
                            {
                                        'key': 'ƥǲsαĐlǥԓʽŚûСˇюđɵԀͲȘкѨȻŸƱ<Ѷ;ѠԢι',
                                        'description': 'ӤnȺѣĭȐƶ\x87ӆȃɀȴύ^ӁʌјˍĊȘσƕϦӨCƢŏȫАԈ',
                                        'default_value': 'ƌМjKʹМξƚƹȆ\u03a2ɾ²ɢЂԝǪǱԫĭ®ѱ\x8d2ǨBʏTȊĽ',
                                    },
                            {
                                        'key': "ˁ<яѓơŷѢ'ЌɮуϟҦ΄ʽпϡќȣő˲tȄkș",
                                        'description': 'ӃȎϋ\x93ØαѪΣͷΧ˩ԎǞҵȰԔΉĵźηҳʰǴĔǽυˏʴͷȏ',
                                        'default_value': 'Ųǎӹ1ǂÈԁѡ¼ӧûϾӂηҙѲѴǪëǒȺëήЫǂǾŏʄ\x84\x93',
                                    },
                            {
                                        'key': 'ѳSĜѽһȍßȦԨuθȢњϡӟҼȎũɇϢӍ\xa0СǲΓôԬΥŤì',
                                        'description': 'Êʨ¨ƍϋ\x9fɫáȝśʩͰëúРҹԛƭʹƇωӜȂɜÛ\x94ŪЃӱS',
                                        'default_value': 'ͺĉʝЯǝȮ\u03a2΅ê¾ǗϮ*ȁʆғɮƎƳŕӊƵ˙¶ĽӉǰɖѶƓ',
                                    },
                            {
                                        'key': 'øԢĎҦƙßіʃђбϪԝŦ.Вӣɽƭ\x8eϧǝæϺƈȩ\x7fЀϹƇǚ',
                                        'description': '\x94Η˭u]ӁǍѢʂƀɈԚҶμԐŨŹưҶК҇ʤӡɨȆˁӑԆÈn',
                                        'default_value': 'íɶ\x89ɮȐтө\x84Єŉȡ\x8eŀ\x98ƛρ\x84ЅϽԙ«ΨԊŕѫƻΰȺɢĞ',
                                    },
                            {
                                        'key': 'ҏиſȸŞ˝έș\x8dӧӡýHЗȤ7ϪҬ˕ėʻϔˢȝǖɋȣʱƷw',
                                        'description': 'şƖӺ˖ЧÖɁʔҩǹʲРLªĔҶɜϕөҕӤʄŀæПʣ\x9f҅ːƢ',
                                        'default_value': 'ó\u0383sǔȺ\x98φƘзīɎӷʩƴίƛʯċơÉҪьЯӿţĨƛΫʼ\x8d',
                                    },
                            {
                                        'key': 'ЄЄ\x8cʤ˙˫ɨӠήǰɤҒѣ҉Ӛ͵ӘӪ)ӢʛǬƌʟŕ2ȾЊʤʌ',
                                        'description': 'ĹǟӯĖiЅӭ¨\x9eҨƧӪʛ²ɒԮВƋ¼ћķßț\x94Η¦ȃƽĶƀ',
                                        'default_value': 'ҺѪҁӱсǱΏȫӖQ˒҇÷Ž@҇ïɼɑʧϘcȲǇ\x84ДҜȊLķ',
                                    },
                            {
                                        'key': 'ЄѼİђСˑɵŝʉϮ˔ʰ\u0380bʮĨ˶ԏkϋӫʭťкԤDӆ\x9cʴӡ',
                                        'description': '˄ѤӬů҆ψơÜĄΊϵϳԧˤʟˮ˜˙ԫˍǺΛЙϼʿƔˑя%Ά',
                                        'default_value': '˶Μ\x8f·ǯԡzÍѳєäŕҐōҢ£ӭʿȖəаΓχșʞȜϱȥŀҊ',
                                    },
                            {
                                        'key': 'ԋҚԏ\x9bʆӈȒȩǓÎΟсƔŰҗ\x8aʊɾμ\x9eɭŊĮЄѕ˗ʣ×ŵ*',
                                        'description': 'ɺеѸӶӴǬЍϾѹõʂŰÂȂȮΧ΄ɔ»˥ŖHѶˉ§\x9cƖΤпҁ',
                                        'default_value': 'Ԝ}еåǖŔѬƙ¥ϿƴϦқ\x8fǌ<\x8dȺˮĒûƧӇ:ЎĚйb\xa0ԓ',
                                    },
                            {
                                        'key': 'Єĵ\x8aəΉʮ~ŖԡĚƶɁ˯',
                                        'description': 'ЏӿǴǦҝϽΏfɩӀҩɁɜʻяϰƂɥD7ҬԋϾǴýϝo˦ԗԪ',
                                        'default_value': '#ЏӜюАϪӜӘÏŭζʩҷ%ϴȖǡǅʀȗˍÑĕũPʄǵÎ˽>',
                                    },
                            {
                                        'key': 'ņƑǉѸ\x9aĬʩȯСӚßʌμĆ\u0382ɼϫԫɺɾӞεſѹΊ\u0380ЖӪņĺ',
                                        'description': 'ʾɅʒ˘ԎΉFŅC\x89#ΝŸ˻ͳśȹöBʉΊˊĤ˗ŎƟѷǣƮφ',
                                        'default_value': 'ǷǰʻӖŦˍВÑѭĽƜĭǯθϋӶй®\x99ȱԌ»ƘҠϯƺГ;Ȭǟ',
                                    },
                        ],
                },
                {
                    'name': 'ǧ˃SĢӊĠʟȡйό\xadϛ\x83|ɝϢǧʅ˴qƹԘΟʀӚǀşǜҍ\x8f',
                    'description': 'ɀ˥ӈӭ¡ԑЗӫV˩\u0380ō\x9aѤTF˂äʉȋĐǈΜ&ɩʄũȺБ˭',
                    'target_id': 'ƾyȎөʐΫźʵˮϦɻ˻ˏІ\x88\xa0Ԛ¾˘ѫюɧҰäґяPˍцȾ',
                    'parameters': [
                            {
                                        'key': 'W\u038b',
                                        'description': 'ǖ¢ʩϣκĞ\u038dВƌԘΫј´ŇЄĘͺȥ\x86ԭλǒԋƣϑԐ²ːȻΓ',
                                        'default_value': '˵ΏԬǑ1úöĸɌɑȿΆ˯ǋʬʘ|GԕĦɦǏҞϓęȔԆYԘЉ',
                                    },
                            {
                                        'key': 'ӉҞѶ˘mϾTЏOȚɣȗƚϮÊɁȝѹcҟɚ3ұѡǶϺҜʗƂƜ',
                                        'description': 'ίәÉƘɮȕԦ҈Ӎňҭsɥ˦ɥTϼľεȼʴͽőРЉϛө˝Ϧӥ',
                                        'default_value': "ԏƇӌǾ\x85˫҃ō˳\u03a2ϽϦʒȾŉÐŘ$ȑŚѴЌΤӝҀ'ġ\x83ʬӾ",
                                    },
                            {
                                        'key': 'ƬЍĠɟ*ȾɄҺӺ´ɀœҜԩǈΠáͲƞӷʉñжЖԗвϥϿí˕',
                                        'description': 'ňķȯ\x89ҜО҉Ê˾n\x8fgCϑɏǕǹ\u0380ÞԙƥώʢƍџΠϷѪԬ˧',
                                        'default_value': 'ԧŃŋÊ`äǠ˕Gʖ˻¬ΨȈчǶЫʖӽҶČҪӧΥȱĕŦpϪų',
                                    },
                            {
                                        'key': 'ұ˅ԞőӜ§ӌr˦\x90MĎʾ\x8dʅǱѯԒäԝ¨јȥѽџȼҟĭ\x88ʖ',
                                        'description': 'ηǟӪǼȷĥǜƥͶ\x8cЉƓƃнɲʫжǿ˔ɓωҵs\x9dƔ\u0381æ6ƻӺ',
                                        'default_value': '_Ǎɍ\x90\x8fǹÉ\x84шǎϣľ˯Ƅ\x9dΛβˣùЉƝǾŽфòńЕ҂εǈ',
                                    },
                            {
                                        'key': 'ͻǐњӢöӸʹοXέмtɭӡҬȇđ\x8fФưJċȚ˔Ȋӥ7\x87¡л',
                                        'description': 'ȑd>(ƆȆǟƽ˳μǪã1Ӽѫ;ȂʪəFбҭ+çƚȭҞČΌΨ',
                                        'default_value': 'ΐ\x85ǈɈ΄Ʃԙ6˓ȭâÌŝ7иҁÄŖ.ӀǖʜĄӆBҦњѢ)ԭ',
                                    },
                            {
                                        'key': 'ʽƪͼ\u0383Πϛn·НŽʈ\x98˂ɨкӶůыˆ^ƻҪVŀƘL\x93Ҷ\x8fѣ',
                                        'description': '½ЂΚʚÉӍ([\x8fҥԨ˝ėԋϐʇʢȈȥӌ˫Ȯ҂ғρĖ˾Үʀԗ',
                                        'default_value': 'љʷǘˍҧ\u0381ƣɴɊӵ[įcťēȺ\x87\x9dĬϩҁĄ\\\u0383ϑʘPÈЭŘ',
                                    },
                            {
                                        'key': 'ȐġЇӷǸ˟ĪžĨϚ˨҉Ԫĩ{ŸɖԍԑΟɼˬǴŗӝѧˋЂÝʩ',
                                        'description': 'ϠĘēȵqŁ\x9a-ÝщзшʵģѥkɭÐĪâUʐ˷ϼƜѸϳԣÀʫ',
                                        'default_value': '\x85ЅȯӤ¤ƥ˖ѮȦҗϙќÏȟʅėʞȻҾώƖĴмĶɽ˰Ҷȣʀб',
                                    },
                            {
                                        'key': 'ʏȮŁЎhʚɲǛ',
                                        'description': 'ΘХɰԕʷĥ\x87ԡƞɤЄ3ƜʏŮђЁĚ˘Ч˄źȭ҃ώĈĢԆԒƛ',
                                        'default_value': 'Ӭ^˽аӹВФ˫Ъ҈бάµ\x85ӊâǋҧ˃ʽўēșǹԥԞӶƬ\u0381Ҹ',
                                    },
                            {
                                        'key': 'ȭԩʱÄĸ',
                                        'description': 'Ѷ*ÞĆϺśϹϪͺƙHѯ˦˸ǐёωŻĝ˯\xa04ɈԉŻĬќҼиĸ',
                                        'default_value': 'ƆѣnΣʔΛԨ[ˆǲñҰȜʳʘӬŬςѥƳȦPηǑѼͷёǷǣÓ',
                                    },
                            {
                                        'key': 'ŠůŵĿҘĢӝҍͰūƈvɬɰ˳ѨӪƺŕĢԀ',
                                        'description': 'Є҆ʆѱ\u03a2΄ԞƟʫɬĒƙŤӊĩӂӂʯιř˱ɬÑҡзʘ\x97Łӂӏ',
                                        'default_value': '\x85Ňѽ~¶ȵ\x82ɍȽ¿\x8aȺѮЍ˫ȝŜϜƎϥʋɩҠƬϱļǩԓ˅Ω',
                                    },
                        ],
                },
                {
                    'name': 'ͶϓԜĩϠƪӎŽрɪ\u038d˪ƨѼÌaˊЩδӲҼâӱŏ¦ŵɩмʠ|',
                    'description': 'иҾ3ķŤюɋșўшˈǧˮЋ6ѴˮéÐĊĮ¥µJƶɕƊʊǔƏ',
                    'target_id': '\x92\x9dЀδõïͶñɪĠҀϠǯ\x7fѦÚŦЂÚȆұȫġpêϭӨü˪ξ',
                    'parameters': [
                            {
                                        'key': 'їÐƙƞҒѯêͷpϷЎƾȜóńџˢõqƐϗ\x9eȐĭӧŠԗ\u0383ʹό',
                                        'description': 'ú\x86ǫћʺ\x9bžƥĿɆІϭѵ͵ʐӃмѤΗŮΘ+ѳ@ȧӟ,ǋǗŨ',
                                        'default_value': 'ЈιiϜɸ\x9fЫҸˋҐϼɄƫ\x90ЀЭƅяΠҥВħɰɆƴЮŮȝԄŉ',
                                    },
                            {
                                        'key': 'ʖҤЙǬ®ǙрɜîɜǊϛԫғҖЯ˓гӪľɖЀΉuǶ˧ɾ²ςҙ',
                                        'description': 'Ǡ˗Һ˭ӧ7џҰtċ\x95ŚҗˌĄΜЊƂͲ\u0380ÆɇʤԒΓϑєè\x93ː',
                                        'default_value': 'ͻ¦Â¸ȫ·Œπƺć$\x94УюЙͶʌ˟ѧǤɓѶѨΰҧǔƀŇΫΛ',
                                    },
                            {
                                        'key': 'º˴ԫĔγ#Ɩˁȃ\x8dӔǲʙǏ҂Ǒ!ӢĒǸўQĎґϭҥͺӆȗĩ',
                                        'description': 'YԧΝЧ[ÃʙȆǎǥÂɌДʕȣΜԡьìƘ\x91үʆʒƥͽύϋȷΨ',
                                        'default_value': 'ʃŋʯЭӵˡǁϳ]ēñÁėΜρāʑɠʘԐūêʰǵŽӉ,ϓȁĮ',
                                    },
                            {
                                        'key': 'ɜ\x80ЧҞҘƫîө˽ӵ˫»ʆǩϖ˃ԟ\x94ʺҳǺӟ«',
                                        'description': 'ƑʈɉǔÐʳШӰӬˤҙҙɜǼҠÑzуҍǇӈԈз³Ñ=Ӥàƶ\x88',
                                        'default_value': "ҎÀG\x97ƀßȲѲԡѝϔ҃Ǎˉȉʗ\x87ƔĩȎƅҝʎǒÃІǸµ'ӗ",
                                    },
                            {
                                        'key': '˖ӜΑΩˁτùұƑéŠҤȗǀŻǟˈ½ϨǥǶɿu\u0383ϖуӰʀȮæ',
                                        'description': 'έ˼˷ŏΪŶЄӽ\x86ĳҋyѰȹѬϮú]ƿӋϵʔŵβЋ˦ӧĖ\x93Ȩ',
                                        'default_value': 'Ӏ+ӔƌÆԆїͿiɿțÈӟԇƮ҄Ə',
                                    },
                            {
                                        'key': 'ȮeʇɘĆ\x9cϰȹʠɽ>ѠϿѴAŇ\xa0˒СɕҊ΄ƖÁИϮϑƅŢ·',
                                        'description': 'о˸ĉġϗíСʉ\x9dγTдûȁɮ˅šŨq%ȔΟбчхɎѬ˙ҸX',
                                        'default_value': 'άӃȳ˭ǂүoʬǭΕѢęûԚƉèЈ!ţԤԝɡ҂ĀŶŭɮ˽Pͳ',
                                    },
                            {
                                        'key': '\x99¤[Ӿө]ʢГō¦џĸԏǠȌʷ\u038dʳŗƙЌȧƖԥKɆΜԅѬ>',
                                        'description': 'ЄҦ˻ЯѯνӛΓ¾ȿǶûƛҾ7МήˏþαʫζԝɍёȚQ\x99Ȉ2',
                                        'default_value': 'ţȜʸȁɗÒ͵ȭś˛ӘͺΤɕɇʫʄȈɯϥΥϗʙωЦķǸ;Ҋʦ',
                                    },
                            {
                                        'key': 'Ė˻ŐʗӨȥòőƻŹȿƹϊ%ȊыƿԣˑǈԇӠψKúɉ\x80º˼ɑ',
                                        'description': '¿Å˚ЦŴβӡӍˮϏɍ£˄ѮϷúǬԋȢěđʾԣН\x8b±ЂŵƨӖ',
                                        'default_value': 'ͽǋΘΨǭȂĵуϨΒǵʝϭȘȱu˒ůǹЫ\x90˘ȧԥϤάϱ\x91˩Ű',
                                    },
                            {
                                        'key': 'ѠϗҩɊɢȉсʕѶ&ЎÀSȬӱʧМԑϤπΉGͷ\x8bʒûͶҕ˗ə',
                                        'description': 'ɖ˞\x8bĂҐʳ\x8eǵ\x91ąёхēÙɾɜҹӌ»Ȅ$χѯʽøʞxώɆů',
                                        'default_value': 'ùȫƴГĮŗ\x9eɂ#ҧɢ\x8eσĮЎLӀίЏпѭñ˅ŏèͰѪҵFΟ',
                                    },
                            {
                                        'key': 'ĳɱ<ͻҎȊǱӘŢͶĺȉμҴѾƖҐĲȬĦӴ;ќƭǆÏàӋŇ',
                                        'description': 'ȦǬѽȼλOĕɧ҆ɳȖ\\Ņ˦ïª˽\x88ň\x93ΥǸΘàƈTΌФ«É',
                                        'default_value': 'ԧǶѵΏӎŧőɩғʄ<О{ƒĈ͵ҘóÙŪџϴǊґ˂ӜʮѲЩɷ',
                                    },
                        ],
                },
                {
                    'name': 'ϪȇсʈɎнφ3ЩˊϻʥξӳљњÊΔĭʟw\x89Cˉ˺εɴŷ˟ҙ',
                    'description': 'ƄэȌѤĆˁǆɄːчӫFRÀĚŁώʷ3ơȂˋĉҔɰˌL\x86¢˲',
                    'target_id': 'ɗʖҮӬ>҉Ҟ\u038dCǨEîƓŎʛÌȦћʘǢҲǾѣтʐģӥ7ɻſ',
                    'parameters': [
                            {
                                        'key': 'ɺрŽ!\x8aīæϲNʧ"Ь˟ʧ˹ʂśŕöԒǗн¸ÀХâ9ԏΆƾ',
                                        'description': 'ȽФϬ͵ņÂǓ\xad͵ӻ\x83ҥԥԤԚʲ϶҆ĮɾƍʦƾÅȌʤgŝŏԙ',
                                        'default_value': 'ΤϸɂӠʚɟȚ͵ƖɠԘäġ˗7ʶȚĄɛı˅ÄŴТˁҎП±ɗΨ',
                                    },
                            {
                                        'key': 'оН<ǙơˑÏ˜ƭîӹ\u0383ί2ςƧԐϲ',
                                        'description': 'Ԅɮ҃δχӪіʝȆʅԫ˨ν\x8cʏӕ\xad΄ΩŜιɣŤχӍȶ˄6\x8cŔ',
                                        'default_value': '¯ǑоѰ˅ȌБĮ˗¸Ή˫ϤFе7ĪӯвԊĲԒФ/wƝƩҦͽK',
                                    },
                            {
                                        'key': 'ΗĻȆˌ9˷Ҕŋѝ\x92ϷǻΠɿüȄ˔żӃҼ1¥ΛȚԭʐɳЫɯ˼',
                                        'description': 'Ϛ\x9fѤǰ)úˢҔʏȔԢșͲԅ_șѰȟÜЊDqΰΪ\x86ˆс˚ȋɡ',
                                        'default_value': 'ƧϩɭϢùʽуҭϐǕҞ˸ԛ+ģ\x81Ѷιӄ˴ʈm\u0379пùΤΩӜϤ҂',
                                    },
                            {
                                        'key': 'ņɧɈć°ȍņìʰ½Ϭϯ\x87ҬФҺԙΟ˼ßɤ΄ϋʫ\xa0ǨɞԨ˸\x87',
                                        'description': 'Кғΐԥұ(˓ӪӟʉdǐƯĞơɴњӓȖōƦƫүœГ\x96ОԖėɨ',
                                        'default_value': ':ǥɺǛ͵Ħ;ԦMԟśЪďӕÓȅɢ¼ŶцǧϳʱƤӥӠéӝnΌ',
                                    },
                            {
                                        'key': 'ǞґǒѐʩǓ҈ȈȾӂԚђϊ¡2ȨԔ\x80ϣвԨʊĮѠëƣ\x86ЦŘҗ',
                                        'description': 'ȃɜŇЃOĘǩƮǇɘҸÄǳ;ʂґ9ҜșˇƻƁϽǟsµ(ѧˮÁ',
                                        'default_value': 'ӲƧǖŁĺbǣïǶѱʎ\x86ԝәɺĠ£7ČԮʹӗ\u0381¾ʀЄčӦӞӋ',
                                    },
                            {
                                        'key': '˗ҩƘǖƁàǆoʷ҆\x8bђȺ\\',
                                        'description': 'бћþȷ҄˙ɑƱщ§ŷƏżҞøţϴΙǬʮʋΤҭʉͷˊȊȋΏ˜',
                                        'default_value': '\x95ƽÊǩȬΆψƳī҅˥Ŋђ/ͺϔȗɻ\x91ӬĴƔшƝʛʚwϾýʢ',
                                    },
                            {
                                        'key': 'Ʋӊ\u038bǷŤǔæӭųϜԠìԐwß©όЕ\x8aŨ˹\x8aɄζӐǍÏҩƭƾ',
                                        'description': '=ƑŏĜϷ϶ŧŮ\u0380ǋʲ¹ϮӫԡæȳÉzɓăªÐ\x8bъӳ;[ϯв',
                                        'default_value': 'ͶɬŹҠÁˮŖћaѷǑɮӣŽϷ\x93Ǒ9ϫˑưϢɿЦɵŕƘïǾ\x7f',
                                    },
                            {
                                        'key': 'ӦʡнéɛіλĦǀĚΊʘġʪɏҭҔǟ',
                                        'description': 'ˡÕϬ˸Ƌ˴ȷ˸âʖŉ\u03830ȸRȸЉӅөџ˂ԡňП>áӴϔŽʷ',
                                        'default_value': 'ώĐƂ°Ӵş^ǟСԨ\x98Βς˞·ǌϛмʵɼīͲŐ,юРɽͷΓѤ',
                                    },
                            {
                                        'key': 'ɣˋ϶ΡèҞͷƛ$bţ·ťʌҸǺɸюЍˬΚЩӖӑȇǌ\x8c\x94ҺΣ',
                                        'description': 'ľԉϩȉтǡԌӔɟԄɠǯȧƣ\x93ԞƈԩԋӑНԅ Ѵɰ˸ĪɦҾʡ',
                                        'default_value': 'ԂӁŪΚơƺԜԚ',
                                    },
                            {
                                        'key': 'ϡĢӶ\\ğгɑ»\x9dМԞұēĖğčʭɢǐǙѪYԔ\x85Β˅ʬ΅ˁ£',
                                        'description': 'ԉɵ3\x89ǧzϔ²ǝǋѣԕÏãǻќäEϚΤ˴ɐɹДǟŪҕ¥¥ӳ',
                                        'default_value': 'ÂΔɢO˂ɉĶðÄƤђóþҗЯĠxҷȻȓʾƢÓˆFˮˊƪˤØ',
                                    },
                        ],
                },
                {
                    'name': 'ӧȊѥāΣËʇЭĠλŌʚǃЂȅμÝΠɸҠѹİΖҧҮÆëеϐȥ',
                    'description': 'х\x86\x92®ҤȂҿcʣѫщɢĆȇ҅ƦǩÀЊԃѼԨԚáϔˊŚΜ¨ь',
                    'target_id': 'mXӮңΆƃáγД\u0378ĿʜͻΰŰȇoұɧҥ˄ɇìư˻Ʌł\u0378Ѵ\x8d',
                    'parameters': [
                            {
                                        'key': 'ÔęԄҟȔ³',
                                        'description': 'ΞύƪҺĊҵҖӃПs\x90ϛŜŬƦØńȬąũVƐ˒ΏŊ˒ԆǁÙϾ',
                                        'default_value': 'ɯїΔϩФÝӁȦ77Ϲɑ¡;ϳɚʋΐëϾϬɫӚҘȦΖіƠрɷ',
                                    },
                            {
                                        'key': 'HŗΗϕɧɟӶƑ˓Ԗųʲ\x94νɥхǿ˦\u0381ћΖȝҮΨӎϑҡ\x8fB±',
                                        'description': 'ƜΔʕҮχ˯ƄӝΤǻĪ}ǯЖ\x9bQӮʧΛĕΫӳЕɓԓȻҝ˃®\x89',
                                        'default_value': 'ěщѼ}ǝΞіʆҔ¹ȁϥîκʏҰ\x88ӈɳʟ#ϹÛӚśǱҚεǰµ',
                                    },
                            {
                                        'key': 'ѿÍǙ ˼FQƨя&ҁͰȽĚˏ˥ƂX~Þȵ',
                                        'description': 'ĉĄɮαĞʚ\xadȄӔӅʈÆϼÊžх˕ДӉʲѵɝ±ζԗθȊӒ˗ɦ',
                                        'default_value': 'ҟ_àЅÑҾˍ0ŕŖɸԡϣѯΛ\x93ĕƁʕӆРŌАĜΏȠϾƐѭͿ',
                                    },
                            {
                                        'key': 'ӥLʸ94ҪΗ_ɹNҘ\x86ʙќµЋҳϿ˸ƒǯʧϐˇĨƎНϻ Ѧ',
                                        'description': 'ŌWɺҒ҄˹ǧΣǂҊBóԬDáǫmțΡ˗ɕ°ҳǕ˃ɽʚƵɎ×',
                                        'default_value': 'ψ˽ҪϯУɠƭɘƬšфOԖƩԬɬ\u0379šʙȆфlюɒ9ɖΘΟƍѲ',
                                    },
                            {
                                        'key': '˸ЮԈ\x83+ɏFҎɿŅʗЌӋƨʊêȾŚ£ıҋǖûωԌʁˌɤĘШ',
                                        'description': 'ӯҪрħВͷʃȨ˸ДϊɳɝÁȃҟ©ɔсħԑǋq\x97ι}ɂхД,',
                                        'default_value': 'ƧOԁӇӺɶσWУ&jBѳӊӝŞ\x8c˪ņǈžȊȘ«EœȫѨӞ{',
                                    },
                            {
                                        'key': 'áȦȥǓǌRĊϱЯȱЌǯȑÖǻщ¢ˎѣÄˣȪ҄ѯәɖ΅ԀњɌ',
                                        'description': '³ΈԚƚҗϥśʎ:Ӊ˱ЅԥѸˤæƞѽͰϫǻΝԫкҶωʆʨŐҎ',
                                        'default_value': 'ӿɁȜѯȡӱҫʒԫУÆԟÞȘѕ҃ҌοҗǇǆӫǔʴүǩ˽ϺȲǗ',
                                    },
                            {
                                        'key': 'ӞuʾƀИҺ?È\u0378ͻɽϱԝɧȋȴ=ѮΣȮͺͼ˶˚ǛƼѨѪҎй',
                                        'description': 'Сċ\x8fӵfÉYҭ®ϷЦƆԁ˩јӎɴҞ\x92ƝǨʗ˹еɃԠʠңâ˨',
                                        'default_value': 'Üе¦ΌѕʤʺƦÛЈˊѽμwQʨԮţǵϜʷӕɶȨʘƍčЀәΧ',
                                    },
                            {
                                        'key': 'ƂćʼĖɀѭ¨`Ȓί˞ԈȤ6äŮҠſдўoҫύҹϧѽҁɉҞΰ',
                                        'description': '%ȃԭӯΤƇȏŉǶŶЬǌȵ\u0380ӉʢČöǥӬčж˙gŶ»҆јˎӍ',
                                        'default_value': '˗ƛǺǣ\x92Ԩǩ¹ȪтɚϹŁύϮΐű1ΰɢƐ5Aǁ΄±ΙŶШҍ',
                                    },
                            {
                                        'key': 'Ɛ¤j°|ƥӆC\x82ſŎɍ"ї˰\u038b͵ĝřɍĻϼBɡΓŻӇŧĻȭ',
                                        'description': 'ĽȀɷɃĥȯҦǵͷĆȬͺ˕ȡǟϘңӶ϶ųԛԂɈfѫƉm0ВƸ',
                                        'default_value': 'åȆʐȬιԂϖɡąʹΔҰύŃѥΧɧ¹ԈӲɌņŰƉĴԋІɆŋł',
                                    },
                            {
                                        'key': 'ʪѕԕ¤\x99',
                                        'description': 'ϟȡ*ƒӿήκӲŧˏɹÆιǮěӵˍÔȔ5¨˨ӆБ˦ЬӒŋǥɘ',
                                        'default_value': 'ΞǭǔпϜҎ˸σĊɑ<˨ƶϕƂȄȩAѻøϒѦǘӏ2¬ÝϤӻҤ',
                                    },
                        ],
                },
                {
                    'name': 'ƲҏɻʲҕĜĺ˜φĚΑʇΒŠѲТʸӁԈ˶ǟĹҳǓϙнҸәԕ˯',
                    'description': '¿ƨΗŊȸǟvйËĴ8ӨǞжŗ¦ґĞʧ\x94ΖǗɠƏРϫγöưē',
                    'target_id': "źцϧƌͻÙʎͻԥ@ɋӞÕΧtЦԣҰӚџҕ«â'Гϥϥń\\Я",
                    'parameters': [
                            {
                                        'key': 'Ϝs\x8aӍəƤʄЉηҹƘɴФӼ˽ьӆԩȯřԢÃ¿ϟŞĻҗƝ\x93ʘ',
                                        'description': 'Ƭx˘īҠǆÌѼϕӽpȶӏȎғ¼Λ˶˱ηƂʹǎҥӖЃȿ»Xư',
                                        'default_value': 'ԋԌĄˈ˅ҮԁƳ\x8aƂЀxϢSƈȦłԬɀњ҆Ʌ%ɀοÏШӅÿť',
                                    },
                            {
                                        'key': 'ζќ˗Ԡ2˾AӍʲəѫɾˋǬǨɑԋ:ӓƨ˧йƔʇɔÊƓ΄ҪQ',
                                        'description': "ҥˋλΕǽŵΕϠŀҁρȆɬ'ǷαϼҨƚ\xadԞϩϞрŪĐʷýԨ\u038d",
                                        'default_value': 'ԖőƂİȠ\x90ŢΞЋʏāԃΔæú«ȇЪщȜΗνʓѻťÀ҆әȱǞ',
                                    },
                            {
                                        'key': 'ԍϠſϲyʒŎ\x8aМɽȮЭǿϧ¢ĠͱʒşƪŖˉ\u0379ѓ©Řƾ[0т',
                                        'description': 'ňĘ\x94ɸųҟϮnӒƘѯǌгϛЛюƂȲÖϭňǩŞӛҍ \x8b˺ȜŒ',
                                        'default_value': 'I',
                                    },
                            {
                                        'key': '˅ҶďƻπŝϏ˕ĊˁБ҈ϐɐӺřȴǄȁɰ',
                                        'description': 'ӒѿÇnҩ$Ʋ\x9e\u0383ƬƑԡ\x9dĆχы]μɱҩԫ\x80ƵϿ҃ҲʪКϨƬ',
                                        'default_value': "люŎ÷°˘ϘǡǄǦз6'òǥʱˇԗѺĩǘ\\Ůʼʁ˰ԘѵƷѷ",
                                    },
                            {
                                        'key': 'ɼÄʌӥҝ\x9dԬɌЁǢ×ęЅѴɹ®ďƃӉcǄѮǐƆˌƶςЗðŘ',
                                        'description': 'Άʵǫ˻Ѹɪǝʥ˯ɔ\\ǎ"ӃŶƱ˒Бđ˄îɊԎΚ҅ѭƑӡтѪ',
                                        'default_value': 'Ĝ˱ǔŗçɾăάƄʪӒХѲǉRȃȺԏǩпʢӄŒŤƥћġκʱ!',
                                    },
                            {
                                        'key': 'Ŵ˚ƔЊÅ²ԓώԏȔ˚ǂ:êƝɵѳɴЦFɭŦœg˨ˌƹəѹѪ',
                                        'description': 'ŃȠӿĜʭîҞўҢʸ˼ͳԡкņʉǮȋьxʏђ\x98¦ԍ{ԙөΧҝ',
                                        'default_value': 'åъөϯĔĺҒȋǃɩҡŤ˙^\u0381ůŮǸƋĪĄθӿӞͲƮƢϴĵԚ',
                                    },
                            {
                                        'key': 'Ғ\xa0ƩPǃÌ\x82˓0ȰįҴȪò҈й³_ǨӒǤԣȤϒ҈˶ΐфζʞ',
                                        'description': 'ǜB˱ɛӬ»ԇϺуΪǼȓбјʥԇʀ\x80ŋЖȪȀˊǗǰm\x97ƖĴЏ',
                                        'default_value': 'ԄŨ\x8c\xa0џîͼӦƉɊŮǻȍǲ\x96ĹӬȓћ\x93\x7f˞ưԤΓΤ·ÁĈŊ',
                                    },
                            {
                                        'key': 'ƽëɝӎZɠвƮƢΥơ8ǢѦЖĖϐҰƉaщϼãͽ',
                                        'description': 'ÕΝǍãΠԔѽҡ˃Ҵ\u0380ӚʮʜђɎȐѨǇйȒÓъßϋΚϢѩÄѧ',
                                        'default_value': 'qҏ·Îáʥԝ¸c¢ɒÃӓå\x8cέıÛΕ\x92ђТӸѫǳʞƤ«ϛ¨',
                                    },
                            {
                                        'key': 'éƈdſWΫўˬϔȪ',
                                        'description': 'ƣҢĸψѢĐŢȗӰ\u0379ѝɎ@VѢͰђлȘ³ƾϰ˨ũʲķԌYŢ\x9b',
                                        'default_value': 'ѾƺʚҬɳʊчŷҥΛԔ\x93оӆĨȖɏʰ¢ǤʿћұϰΖΒ˧ˀǷǉ',
                                    },
                            {
                                        'key': 'gϼȚǆä¾ʰ³ЍʤоɖϓÞԖӪ˨ǉɶfΖΆɻήͽɻЭ9Ԃю',
                                        'description': 'ųǞ¿ïҐÖœѴϱǱτҜ͵ȶĎһϋсʇ¢\u038bϚұîҗƋǭǗņң',
                                        'default_value': '˕ʜӹӷͺΊhɗΧˁÝɦƯ˺ӞĊ\x85&ǥĕґķҽԏðȺяȳΧА',
                                    },
                        ],
                },
                {
                    'name': 'ƅͰӳҺŊɄǔÖGӚÚƘәʸEϡӼřѬþzȥȇˮɽϬèҋԉ˹',
                    'description': 'ǶˢʗѢɩӆЈύϪŤèőƋЅϺдĻʾώÐ`АˡƪьŨĭťǊϹ',
                    'target_id': 'ϺɫȘΙ¢,ϝїȍǐїˮȋщþҧӝ³џ˻ˏΒņзΚѥ¡˞ӏ²',
                    'parameters': [
                            {
                                        'key': 'HǬɷ˄˃˃ı',
                                        'description': 'ӷƯƘÁһшİ9ĈT҂ΕˈĮɩͽƢɃʦŶƴӼҡŋϙѱśȸ˗ɟ',
                                        'default_value': 'Ϙϻȑρ˖ϫƿЋȌȔƖ7ǁïaԗѴ˻ВƇӡӹƄĈOʂˆ/ēχ',
                                    },
                            {
                                        'key': 'ҺʭȄǎ/îǻΗҧʻϷӠˬˀхχӤűΓεΗāyŃЯ\x81˒ʪЍ',
                                        'description': "ԜЎѿɁ\x92ɄӋ˳ȡӉϛ\x8aΰĖщ\x87³ø'ąъчǄ;ĒɳùϠíѶ",
                                        'default_value': 'ΈϾ˜ԋ·Í¿ҷΣIĭќ%όЍıƁ\u0382ÕŚŭɈȒѭξ\x94ӒįˌC',
                                    },
                            {
                                        'key': 'ĺǼГɘʀϲϔėþІрDğ˜ʱЫ',
                                        'description': 'ƮЊʄǑ\x8dҮɂʉƐʵú]ΡƜ\x8cƷǪ?ŅƘ[ȅȚňßˠȁ9āѴ',
                                        'default_value': '¡ïѣЖύƉŞЈξÃǏŲƙаƏȸǕюÃ3əëŨĉ҉Ƞ°ɍ˧ƞ',
                                    },
                            {
                                        'key': 'ɺԑđʵLˏԃҕěΚѡˡ˶ǭǢ&ҮƈʷѵԅμȨγθūʵҢ;Ё',
                                        'description': 'í\x9bѥұȋѭi˳ǔԫB\u0383[ʑƿΌΣ\x94ӥɸ\u0378ԫ҄ϼŶèӓɐчɗ',
                                        'default_value': 'ϭňtƽňΫӇɬϚˁΙϢԈӯʯҌŜӿȕČŗŮŇ¯ĳʔсpĥЭ',
                                    },
                            {
                                        'key': 'ǲ҄єʎύi˙Ѷ;ԔѴ§ȘƯͱͷɘͻ\\άſѱәѰǄΪŕ҈Ʀb',
                                        'description': 'ӹсʱЯԚĢà¡£ÆѷиȟϐƴăӥåĹųΊΧǩүԩʆюӯđҍ',
                                        'default_value': 'uƵԃ¨лУħɍˎHӭҗyüʣ˕ҎȠɋ˝ϦѯĨwɰғňʐәѪ',
                                    },
                            {
                                        'key': 'ѰёūȜԮϯŚȧȔʠŭ ϡËҼѴ(ӃԋĥjЪɟξPғ\xad¨Ωȭ',
                                        'description': 'ӠǶТăԊǉŇŅӔЧǝĤϛĶƊų2\x89ɂÉԌƱΒΑǖǶӧʋtʌ',
                                        'default_value': 'ѡgɠďӍf²ϪÔʕɎñȪҟƵĚћԭxϼƱўĒŰ˶ȼӶύλĆ',
                                    },
                            {
                                        'key': 'ͼЖεǚԨȥȘĵрԉ]ņɘҏйȻ҅Ě«˙Ƀσɺί:ʀЫ',
                                        'description': 'ӓӡ\xadЉ҈ǃΔҸȊҹϜʇ¶ƽθΉЪƼ\x9f\x9e2˔ΚóАЬʩCəɶ',
                                        'default_value': 'Εχ¦ҒRɒ\u0380ɀθϖЊǶԥɦЙñƍǰ=Ш\xadԏϤȭƃþ<ҧľԠ',
                                    },
                            {
                                        'key': 'ĢƋĨɅΗƣƦƣsӃҍԧχ&ŃȑԭϼпєɈxďΉʰQѺϹӓ˒',
                                        'description': 'ͼÊԀНӖέƪҲmǬPЮђΕ˥ЏõƆɍưњʋЂɗӺğϚű\x8aΕ',
                                        'default_value': 'Ǒ¿?ԙ˃ĦȴȄ³Ѐ8ђϳɵЮԪΉàśǍĠǼRŢ)ˌјʴɭӶ',
                                    },
                            {
                                        'key': 'ήӚԢԊѶŝşԛqÍǡҊ˭ѨƺŠîmƤɠːӰǭΘɯűȜΜƚʧ',
                                        'description': 'ʄ7ӼҒӷΣçҦ#\x8cyηɋɫu¸ļƮўʉjζÚɍăŉ¢īӕȷ',
                                        'default_value': 'ʜеʚƿαͼВć=ө˅˅ˤ˸ˠІȸ¦¾ˡMNɻЉʴŋƃ]ƪҍ',
                                    },
                            {
                                        'key': 'Ʀӹκ\u038bǺǡ&ŏΠЭʵɅ¨ʕ҆ӄVЮĨ˘ζѧ×ǚ:њȳèΚӖ',
                                        'description': '҆ģªǈґŀćǪЈʒĄԁӅǡʠ;|ȵĜϙΥɎǥŸЌȵ¨ÅBǓ',
                                        'default_value': 'ӂԇaʛˢў¤1ɐԐ.ʹΚÌӢǈʦÒҭ˫;ԣȚřѲϽʗϞʷv',
                                    },
                        ],
                },
                {
                    'name': '©ŀʟȢÍǐǊʻӳǋSŻʇãțļӜĩγĻƁĵáҰÕ˔ϙϑ¨\u0382',
                    'description': 'TɇʂĀƣ˂ӥȼʭГƽȷăϹϭϹЮюԨ×ҋРƎǁǔÇ\x7fʲǽ˚',
                    'target_id': '˓ӿ\x83ŝʐϏԌñ҂ǝų"\x9dʓǾ\x86ƽȤưȸǸθëԞŘɩԭp\u0381А',
                    'parameters': [
                            {
                                        'key': '5ʃЂзԅȱ½ËüҰȀϺÛʡ˛źǑȎʋ\x86Ĝϝ˻ӡķԡѲĺ\x8d˞',
                                        'description': 'ŽеƂĎˉǥȤCǊzʃ\x9fǌ\xa0ȤЩҔԇЀӻȝǚҋѿҼӨҁϗӳʸ',
                                        'default_value': '`ʜüLÕӁɅəŘʟԜJиψЕìǚɊΤ҂>ǁƨɺXƎȧǯńɒ',
                                    },
                            {
                                        'key': 'ȘЁƺĜΟ\x9ePĕǩ:ԎЩƬСŀЂԥԀИŅǐӌ˧νϟɜ?3ƿÄ',
                                        'description': 'Əðì\x9f˧è њʃƥΙÇϜƅɻǔêʬΠňÇ|HͻƑҫϴɾɬǽ',
                                        'default_value': 'Ǒʫӱ҄Ѫ\x8aэԚАǰɠ4ӉeƋʒȏ-ҩüǄĤˀǊKÝѯ\x93äx',
                                    },
                            {
                                        'key': "'ïΑɢÜӊ˪ʧǑҬґ·",
                                        'description': 'ѶʢҐдūҚǕί÷ÀʴύđęϯȊҐĥ\x87Ӝ˰Ԯ1Ό\\ԁҴѩĬԞ',
                                        'default_value': 'ǥˑƕƫ˻AʐɥŶǛǲΆˊŚėѦ˘ǰƏĩϥǤΒӁы;żĆɝʩ',
                                    },
                            {
                                        'key': 'ŔÆӥ{)ѲzʤЫ',
                                        'description': 'ȱíΝƩѿѐӰЌ\u03a2ʺˇȽ0ҋ%˼ЂĐ&bŴʦƞ\x9aТȽњȇȅю',
                                        'default_value': 'ˡ>ŝǝѓʸԈ~Ƣ/ϘɬФȤ°οЃvȗʮ\x83Ұʽҏ˪Ǔϼφ\u0378ł',
                                    },
                            {
                                        'key': 'Џ«ñȾɄųœ˶ԦԩʪаɆϼ˵}ńËƓ|(ėȄǯǢѭ˔ԁЩɧ',
                                        'description': 'ԌŃвʼȓɜтϩϵȷ:ѺʽȦϻAǹɢÇİ,ɅҙлŀƵŖѻһ˵',
                                        'default_value': 'ǆƎПёѕwԢ\x93Ēčʤfβƅӓ\x9fѿѪKɔĖƠǁŕɜĒǿ΅Ϲă',
                                    },
                            {
                                        'key': 'ÚĖÞXɄЖ҈ſĨĢОǡóůɞːԁԋǎüΪɫjӃҰcφǒƄĮ',
                                        'description': 'Ɠ¡_βэÏjɱnˮ;ϴõҭ,ˤͺ\x99ˏ7ѹІҘ5ìźđ\\\x90ѫ',
                                        'default_value': 'Ƶ\x93ĝГҎċƔˌʜɮю\x87ϹԒƂϥđљȋϟӶŒ˻Ƴ˹ӯēѿҐƶ',
                                    },
                            {
                                        'key': 'ӇǐǪɐЍřȿ',
                                        'description': 'Ȫ˓Ϫzţ¯μʧнķġ΅ƏԛѪìǛΏѯԉʱҭԘ˂ʺɧŢгϠӓ',
                                        'default_value': '\x80ӄÍ+ǡ¦ԋĚȉƳзĸͰƞǗπδĳdUǤ@ňɭ˰ͶϓϓыΉ',
                                    },
                            {
                                        'key': 'йÕØΪӾŔMnԁ\x90ˌó\xadăƞɻͱӶрщә˴Ş˦ҧƎǏ¥OɈ',
                                        'description': 'ô\u0383Ģǎy˼ŎřΦƮӲĊѐp˹˭ŅÛ˚Ч½ҍųҕǔçʦĵӦϳ',
                                        'default_value': 'ΑϝʯèбΓĊŀâ.Ҡșѷǲ˖&ƗӶοĎ\xa0QйΠԇł\x9eəӊĩ',
                                    },
                            {
                                        'key': '\x83ƋVƹȅȗɊŇŵgӮҜɶȍё\x7fΡч;Ѿ˴ҜŢ\x9cůűǚѬϼŢ',
                                        'description': 'шϵŲɅäɞԧÇеҙƼƆɸƮ˾ˠȎYšɑBŁȽДƗϡĒʹҔͻ',
                                        'default_value': 'ŴǮTөċѣ¸ɕ®åСw˨łɚѸџϛԣЊƑŽ҆ǿ·¬Δεĭӂ',
                                    },
                            {
                                        'key': 'бɃFԁԗqӺǟʶUʉĦƁAӈ\\Җӹʞ҄ǳУȔçҌŏӄΊɅR',
                                        'description': 'ˢѩǉϼҧƘҚʚËИQʱʜȓϙѢЧцӔΝ&ĵ˜Ԃ\x8bƐŕλ\xa0ƌ',
                                        'default_value': '¼ʥύǓȟϨԜжρҡҾɒćЪҜȲ\x93ƿқóʑ²˦PĥĮ\x90ƗӧȘ',
                                    },
                        ],
                },
                {
                    'name': 'ʨǸȢǛˇ´ɹʮҵłÔǂS³šϷ˄Ω',
                    'description': '҇Ĵåŋ¯ǑϾРӷ˪ǬӚ\x87\x87ѪƑʑҡԜϘɚѣɲЪɵӕҌκʱˢ',
                    'target_id': 'Бƴӽұƚ˶=',
                    'parameters': [
                            {
                                        'key': '¶ҪхӅАȌȟыŒȁ\x8eʩɣȪȃѭҩoͶɭ?Ʉ©ɦƵ˯˧\x87ѧŲ',
                                        'description': 'ĢÈXԁѻǜmɋƚĈөԣŵʮ\xa0?ӖǒƫΘȶƽӀ҅ˠέӺÓ2Đ',
                                        'default_value': '˄ʜϲҌlďƅоūљüƧ\x85ǋíʄmĬɉƷ˓˂đ˱ŀșƲϮĞʖ',
                                    },
                            {
                                        'key': 'ґаϜѺϫӼѱϟӅӜӀűäӻҧѿȾęϾǷʼʼvєȆɃ\x98=ϽϾ',
                                        'description': 'Ңȕ%ѺȮӂͳ҄ƚʿưд×ӵƢ\\ʇԬÚӳˡǻӺŰ\x9bʋҫͰ\u0379Ŧ',
                                        'default_value': 'Ԡ\xa0¢ƲƮ\x9bʓѺʅϝÿϱϣώǚŌѣƇί˱ԇͺʷőӧӀИùзţ',
                                    },
                            {
                                        'key': '\x85ʯÐÿǤƄӝ˅Ӽ',
                                        'description': 'Ґ\x92ƈŨқʡɹˎɓԩǮНΉŉȘǯƖ͵ҜҿɤȔȢdӅҠ\x80ӻӺ[',
                                        'default_value': 'ɥ[ΝйɸƟƨʏȈǳҐÖчӨŻʔd@ŚЀĮЖшőŃŃƶȜ.K',
                                    },
                            {
                                        'key': 'ЭʡӞĻȖѝоŽˮ҅ψӨͺ[ˆx˃ЕÊȂ(ɥʄƾǨƦӧ҄Ćύ',
                                        'description': "ͿϰƭŅśξ_ȕǚǲԗқ˓ĠöԨŃϕʹοϒ'ǒÏ®ȪӞŗДɸ",
                                        'default_value': 'ҥϵÜ\x8bӼϬϋĀʔǉЙԠ˭шƪѰʵЦFΣѵ8З<Ҁ\x9fѮΟȦį',
                                    },
                            {
                                        'key': 'ӲԡіšҴ¢ʗЭӏс˅ӮϔчӬŸǮʎӭ˗ʲƢW\x9cο\x94hʥĄ˷',
                                        'description': '˞¢ғ\u03a2ȩ˫ԝĻч·х\u0379˶ԓǔʐȤʿѧCɐǷĸӶSςӮҖͰв',
                                        'default_value': 'ԭʫЁīƱƩѼϠЪʙƎ1ԩџʙѭͱѵğĐӁ\x9eǵӲϩ\u038bГŞɿй',
                                    },
                            {
                                        'key': 'āȨˬþƔùƍ"¨˼ƦҁñHϥΒɅԒӰɩ/ͻȆŧҵ¬Pϧ9҅',
                                        'description': 'όґΪǠÝԦØ¼ǾâƮͶŹɹͻŖЃϾìˎӁҩΌʁţŰytƛȋ',
                                        'default_value': 'ɼǡƛϩǝǮνɕРêĲ×øɋʶʪɫüϊ҉цŗ҉ÖǧѤԆ·\x85Ů',
                                    },
                            {
                                        'key': 'Οӹ˴Ќŗ)ʵƣª˞ұӮeŃǇҴħс0˗рŔɶɞ§҄ӆıѩ-',
                                        'description': 'ǙѡлÅτƺɛgʸёƥũƓ΅\x7fś:КǲȔ\x95ρƢȇȆӾÒУϸҦ',
                                        'default_value': 'ʳѦʫӏɹƎϺѮ\xa0ĵƌӬ.Ƚǘ˫Ӣʤ҇șȕ¾ϴс¾\x8aѽŧ\x9cʇ',
                                    },
                            {
                                        'key': 'ӋĢԔ\u0380ʰʿŨ\x8dнϢļĎÀ҇@ûǪȡȗ.ƫϲŊˇωˎ˻ЕҫѺ',
                                        'description': 'ńǝːΦϊşǇÓď\x96ʕƗφԠ¢RƮψϲΠӕEХňГӪҎҘÑ˒',
                                        'default_value': 'FΨîǧ»³ȫνǄЀӟƟίԎі\u0380ԔɠͲŲҰѤȤbŁцϝкîÎ',
                                    },
                            {
                                        'key': 'ǘÏʏʴÜ\x81БӘǘƔʾϧ˩',
                                        'description': 'ԝ˓зʲǈÊ<Ŕśϕŕʩİ˩ҩŒА˜НӳÌӯԘҡӆ¹ʹ¹Ėā',
                                        'default_value': 'ӷȁƚӾ\x934ѸƳțҳԛȁȚϚҥɐɐѡ˲ͷӒƪäɩȊѬçȫǹу',
                                    },
                            {
                                        'key': 'āȓ\x83ҊҮӻVʧʜ\x9bқΰŹʕΦīǠԐпЕŋmÎӁ{ŲȀԗҹ(',
                                        'description': 'ʦjμǃɡŔΈĩϹËİңӳԙĩʐĮђŞİśϖǅǃϭԃǩхEќ',
                                        'default_value': '\x88ӉņθàÂҺӑƈϣҴ¦ɇȞçƩ}ZȉΘʡõǁ¤ҹȀöΐɇȳ',
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
