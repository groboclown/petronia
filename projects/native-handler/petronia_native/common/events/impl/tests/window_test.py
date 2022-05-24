# GENERATED CODE - DO NOT MODIFY

"""
Tests for the window module.
Extension petronia.core.api.native.window, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import window


class ScreenDimensionTest(unittest.TestCase):
    """
    Tests for ScreenDimension
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SCREEN_DIMENSION_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ScreenDimension.parse_data(test_data)
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
        for test_name, test_data in SCREEN_DIMENSION_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ScreenDimension.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SCREEN_DIMENSION_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='x', name='ScreenDimension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='y', name='ScreenDimension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='width', name='ScreenDimension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='height', name='ScreenDimension'),
            ),

        ),
    ),

]


SCREEN_DIMENSION_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'x': 3931026638107078038,
            'y': -1775964378652671870,
            'width': 6833187335804517024,
            'height': 7661726810657827262,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 9076837946515924178,

            'y': 7322924054309264261,

            'width': 5096876623628613125,

            'height': -6572309396266961005,

        },
    ),
]


class NativeMetaValueTest(unittest.TestCase):
    """
    Tests for NativeMetaValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NATIVE_META_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.NativeMetaValue.parse_data(test_data)
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
        for test_name, test_data in NATIVE_META_VALUE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.NativeMetaValue.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NATIVE_META_VALUE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='key', name='NativeMetaValue'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='NativeMetaValue'),
            ),

        ),
    ),

]


NATIVE_META_VALUE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'key': 'ȣwɶµҪŗȮԨƗùơӒʺ[ɧ˘ÍѲ˓\x9aΐɧӒρӋѱњΙʇǖ',
            'description': '³ȣԅ˳ʲĊƯ-Jцſΰ˝ƫӯʹӰŇ¢ϙԚŮǠũ˼ǃśõ8ӎ',
            'value': '-ŇRИ\x9aʛʀǤмͼ\x88ȚчΜH\x8cǭȎҢśʨ/˙ԄˈȦңƿǾR',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ə',

            'value': '',

        },
    ),
]


class WindowStateTest(unittest.TestCase):
    """
    Tests for WindowState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowState.parse_data(test_data)
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
        for test_name, test_data in WINDOW_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='active', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='focus', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='location', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='minimized', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='meta', name='WindowState'),
            ),

        ),
    ),

]


WINDOW_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'active': True,
            'focus': 3788,
            'parent_id': 'ȍχ˜Ȗưºʋ]ЫǿʷƞƯӆϒСŦԏӫˀlΓYѓŐӾȜ½ӽǓ',
            'location': {
                'x': 2174818064930779292,
                'y': 9178736383704620970,
                'width': 4727296487842575967,
                'height': -4523379335047171180,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ǏɰǸǕdͷɦRϑɬģƾ¼;ǤȪɽ˩˔ѷЎĆȘӾDѷǭȈωŴ',
                    'description': 'ƈҊ\x86ƨöҜϒЏ˟ƳԨRчЛЦȪˇ˄čλ×ʰŽĴw§ʈϱѠђ',
                    'value': 'ezɱҔѣǫ×\x80ɨҖȓȹ¨ΆķŘåӘǟǢ\u0382ЛɫѐӃΆ<`Ԋ˃',
                },
                {
                    'key': 'ԫƌ\x90ƜɺНeƟу/ǧ˄А',
                    'description': 'Ʉèúэ\x80ȿʾˎ˞Ԅʃƃӄ\x98ӓŖјҋɖíǩ˧ƧʌϯԆ\x8c=\x99Ü',
                    'value': 'ʫЬɫì',
                },
                {
                    'key': 'ѳȂ',
                    'description': 'εЕζÒӰȊėȻƂҮƢʷвGʳGЍíӞvƆЊϔ˵Ҙģ°ʣƙѣ',
                    'value': '{Ũԅ0ʅ°ƺ×ĸńʫFĔƫȹӏӽĹӎԪԐӭșâ]ǠҰˮ\x8cϼ',
                },
                {
                    'key': 'ѱȈʁβϗDΥ^ɋϹʈү\x98ǉ˒ЀȢ<˼/ЛǗǨВİů',
                    'description': 'ˍϼςαӜҾĳ˒ÕùƄiƼȡөƮnƯљŒƼΚJƑǣʽȅ2ҽќ',
                    'value': 'Ͳԕ˔Ӭ˱LïǊHȁčʫѣӪęԘСǈ6āЕԎПÎϊΒр\x80ŖĦ',
                },
                {
                    'key': 'Ь*ӢǏɧϨРҁ',
                    'description': 'cŽʓ˼ˠɅͶǇВсȀĽɉʮ©ƎĊùɠӶ;ʑƗѸфЙ\x81ɸĵ˄',
                    'value': 'ƯˠʖµΦȷʦŧ˂ΤȨϪϧ˂ÁÆƁ͵ÖǯʽƄ҆Д±ԐCȲȁϩ',
                },
                {
                    'key': 'r\x9fȩ¿҅',
                    'description': 'Ǥ«ƄȄӁˊ;ϧǩԞ÷_ŀΫеǢy\x9bĲĬ/ȩНǬƲԪɭѡ×ʎ',
                    'value': '\x97©пЖԥόѯ\xadĹv˧',
                },
                {
                    'key': 'ʱʱBɰʥƶƠ4ѣϔӺ®ʱʐūƽ΅ώ˼z\x9e',
                    'description': 'ΪԠԤǵǔğƐƖȴӃ\\ʑƧĵΫø˜ӡΝҟiўҢ\x96Ͱΰľ.ʹ˯',
                    'value': '˓ΨʳϔҤӇүǼҲǽӛŌ{\x8dɧ\x7fúυíΓÚӛҔƝԧȃŧŶѶӕ',
                },
                {
                    'key': 'ЋɈΝѬƚ\x96ҘˎϤŶeԤ˄ʐˏI',
                    'description': 'Ͻ˂ʖȂҸʈΈƴҤѦаѵǸˢвÁuãӎƶ΅ЗțƮɟ\u038dÝǂ˧Υ',
                    'value': 'ȩѶӼˏɭѮЗƄƦϸǢǠū\x8cÿƯƙ½λɓчȇ<Ƈ=ҵ˓ͺһˏ',
                },
                {
                    'key': 'ήϡӠ©ԠɩyΘ',
                    'description': 'ωɕĭςʐƍJɖŔĐɄ#ϟ҈ԣώĻǆиėȵӷŸƂπ˷ЛƏЮϸ',
                    'value': 'ʍ\x9eȌͺϩĤƖϸØŀɂɭ\x85¢źrԝф˽ԋĺ҆ƈȠ¿bΌʫʔ\x9f',
                },
                {
                    'key': 'ԭ˻϶;ȼØ҃ĮłԥʏSӲ±ŢàŸӕʾÚψɁʅҽЧΥȢψԁģ',
                    'description': 'ͽǠºȤ\x9cɰ1<ѯБѝҘɩȲʮ«ùÏˢȡӏè2ŋąƍӡˣŒҶ',
                    'value': 'ȆіėǂĹѥƾȴКkūŅ϶сΐàƎÐԦQvԭӢȄʂ˸ȼʂĘǛ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 3895,

            'location': {
                'x': -2217261249704017239,
                'y': -8779352171933668790,
                'width': -9013347127970304952,
                'height': -5485866882762032447,
            },

            'minimized': True,

            'meta': [
            ],

        },
    ),
]


class WindowCreatedEventTest(unittest.TestCase):
    """
    Tests for WindowCreatedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_CREATED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowCreatedEvent.parse_data(test_data)
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
        for test_name, test_data in WINDOW_CREATED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowCreatedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_CREATED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='state', name='WindowCreatedEvent'),
            ),

        ),
    ),

]


WINDOW_CREATED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'state': {
                'active': True,
                'focus': 7117,
                'parent_id': 'ίĒʼɽ¤ĂÎѧÌȑyŽƠűӳȓʸ',
                'location': {
                    'x': 8646175708134065670,
                    'y': 527564498309629567,
                    'width': 401157360423323689,
                    'height': 867397063261343954,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ŴӠƵԡʫƿěΚ$ăҌаƏ\x91ˇЀͲ˛ŘԧǵʐȼßԘ',
                            'description': 'Ͳӯ˫Ğʔ`Ðʍʦʷn;łʊɋʋȂԣƺɳΎȘўɨΗšʱƍňϾ',
                            'value': 'ҸIɩvʊˏЁˍÝ˲ÖΈϿҎŭҫӌȗúӲʁҏ¦ԦėȅˊХɃǊ',
                        },
                    {
                            'key': 'ĥȲζӇÁӁėҼȘҞŽɲʨ\x85\x95źǷϷϭǏğǆȉŴìӲĭťΊǗ',
                            'description': 'ѸΘǜɂ\u03a2ɠԌVԡŢɋяԐpÓˀȩͺοО=Ά˪ưǇ©ɓϴčȠ',
                            'value': 'α\x93ȁʱǬėԣȣ®ϖˆӍʵ˱ɑÊԬҷƼӹȪнȯԄƝҔӛϕЈŸ',
                        },
                    {
                            'key': 'ŁйˏʨȊLÞwœß',
                            'description': 'ˌʧƩƟ6žϤԉ΄Ųςͺɥц˴щΆP#ēÿ\u0379ȟɊŵ˨лŷҲ˶',
                            'value': 'цѨôÀөƘŞűưƎҸĴźԤĢŸɷȨ΅ҖŎѱє˗ćÓϻā˙Ǧ',
                        },
                    {
                            'key': 'ɺʥÓґʼǪӾ΄ιȥɣұŐ\x9aʳȖÝŠŌëЂ',
                            'description': 'éȿȢǉΪǸǒЛқ2ȘӱҾӐԡбɩčԤŎφŕ1҂ҸǲȾǻǤԂ',
                            'value': 'ҀΜҐȵŝw¹ʹtӍƑƃɍЈƈǘŋ˞Ģӗ°ŎϟʵƹɳǽɐɂÚ',
                        },
                    {
                            'key': 'żȟѥОϖţȺϢГ҆˯ЅɹџӠɫχνԚщhĨņ¸ï£8˸ĖӾ',
                            'description': 'ƍ×ζeƘϜƝҸιaԏѵԕԆϹѿĜӪϯͼǥŴɆѰȻӗǋ˭ǱҠ',
                            'value': 'ŲԙҡЗ\xa0Р˲ǅҤ˸ЍɼϤʌʡΧųǸѷʷΣ·ЩϋȢ',
                        },
                    {
                            'key': 'Iӥ=лľц˽IʵȔǱǫ҄ȩ',
                            'description': 'ΰТӠĥ\x96ɎĿưůʦ¯ԫȱʫˍǛǦԅʩLȕΎ˱ĤШƲúļѱʓ',
                            'value': 'ʇͺ˭ҀƯѝҫȈǵϢ%ɻƙ˓\x96ӬǬԘđ\u0380ӖôkɓШӏʢͰ\x88Ʈ',
                        },
                    {
                            'key': '¼ǇɮŔǍМūǮȼȾҹNʬaѼ',
                            'description': 'ŉϔûěЕΉїêÝɪGÏɚπ\x92Ј¤ĜЌħЫ:Ŗ\x88}\u03a2ȏǤΛԜ',
                            'value': 'ďxΥă϶ӂǓȶШӁØЎԬԗӿїȏåŤяˠ9šπȅrŇZԅғ',
                        },
                    {
                            'key': 'Źӹȡƴ˶ѯӨÞ҄BӨ>ȩϢŴцʉδŀǀøŪ¹Đ5\x9eǣɎǟ·',
                            'description': 'ӖíγªÔ©οȦЖġϝǔȴģяОáѻϾɳƭþ¿½ЕȻÀʽјĂ',
                            'value': 'ˠ¸ňƔȗЄʯ5Οòњ¦¡Ό6ӰȅУȦªúдƮĈҥǱӗԕĻƀ',
                        },
                    {
                            'key': 'ǆʭǐ Ǝʅ\x83ĩІ˦%ņѩĜƛԘҬѸұǥԗǕǊѩɠҗŰЍаԒ',
                            'description': 'βБƣΨïĳĭįȒόmŭÇ˲ſԀ\x94\x8a\x80âӝпҜʲɌ¦˒ϟӐλ',
                            'value': '+ʬџǀӧˢαǶǨʹ˰}Ђү\x8bрϏ˓ɻȥӈѝϴВҕșuȑԡɵ',
                        },
                    {
                            'key': 'Ǒ®äȽ\x91ҟщäǴ',
                            'description': 'ЧԭɝԨļƲҢÂÍ\x96£ͺɂρºƴÝЗÞ҉ψƔҢųҌÄUǒωЋ',
                            'value': 'ӏɻƃOʖŦҐ&ŹҟʷӚϭ\x90@ªÇ\u0379ɼӖ½ˊҵ\x91˚ˣϏҕśɁ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': True,
                'focus': 2816,
                'location': {
                    'x': -9015646973899282125,
                    'y': -8816210423030151688,
                    'width': -5035095495235528978,
                    'height': 2438865845281309908,
                },
                'minimized': False,
                'meta': [
                ],
            },

        },
    ),
]


class WindowDestroyedEventTest(unittest.TestCase):
    """
    Tests for WindowDestroyedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_DESTROYED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDestroyedEvent.parse_data(test_data)
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
        for test_name, test_data in WINDOW_DESTROYED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDestroyedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_DESTROYED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='reason', name='WindowDestroyedEvent'),
            ),

        ),
    ),

]


WINDOW_DESTROYED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'reason': '\u03a2ԂǚӿĬȸҤӄį˅˸\x9eӠь\x83ǈΉӅˮҥƕŕш\xa0ɘŁǮϑЯ҈',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'reason': '',

        },
    ),
]


class WindowFocusedEventTest(unittest.TestCase):
    """
    Tests for WindowFocusedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_FOCUSED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowFocusedEvent.parse_data(test_data)
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
        for test_name, test_data in WINDOW_FOCUSED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowFocusedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_FOCUSED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keyboard_focus', name='WindowFocusedEvent'),
            ),

        ),
    ),

]


WINDOW_FOCUSED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keyboard_focus': 9585,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 1299,

        },
    ),
]


class WindowFlashedEventTest(unittest.TestCase):
    """
    Tests for WindowFlashedEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in WINDOW_FLASHED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowFlashedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_FLASHED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class WindowIdPositionsTest(unittest.TestCase):
    """
    Tests for WindowIdPositions
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_ID_POSITIONS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowIdPositions.parse_data(test_data)
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
        for test_name, test_data in WINDOW_ID_POSITIONS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowIdPositions.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_ID_POSITIONS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id', name='WindowIdPositions'),
            ),

        ),
    ),

]


WINDOW_ID_POSITIONS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': 'οϵˮĿŐ¿ǮɮϘάɲƲԟƊΉ;п¶^Ėċğ˕Ż~ˬ×ĲǯȽ',
            'location': {
                'x': 4115509387460835422,
                'y': -7432023073476567493,
                'width': -6287291221957113357,
                'height': -402026893638513074,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '°ʖŒϥġ',

        },
    ),
]


class SetWindowPositionsEventTest(unittest.TestCase):
    """
    Tests for SetWindowPositionsEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_WINDOW_POSITIONS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetWindowPositionsEvent.parse_data(test_data)
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
        for test_name, test_data in SET_WINDOW_POSITIONS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetWindowPositionsEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_WINDOW_POSITIONS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id_positions', name='SetWindowPositionsEvent'),
            ),

        ),
    ),

]


SET_WINDOW_POSITIONS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id_positions': [
                {
                    'window_id': 'ș´ʯ\x87Ɠϋ?ԂӳϡƻѱľЬГ´rΝΕð\x9cȮ˯ʦņƚτưϷā',
                    'location': {
                            'x': -2989625110798414551,
                            'y': -4503621332913177069,
                            'width': -4707082160513157734,
                            'height': 7404125687500523075,
                        },
                },
                {
                    'window_id': 'ϿȚŕҸɉ"ÐëæȄưҊŝǮҲɶӧԣłŒνѢРèйŶØ*Vi',
                    'location': {
                            'x': 8693017704531947356,
                            'y': 5169071728685705690,
                            'width': -8395885843162968124,
                            'height': -6956290435341484528,
                        },
                },
                {
                    'window_id': '!ǈ\x98ΰġӨ\x97˃ӞŔъĚ҇Ȩ\x9fҧʵfеΑŌȿѡʖɗùїҊ϶˲',
                    'location': {
                            'x': -1006076996689178024,
                            'y': -7270067461611486400,
                            'width': 1314622621661009894,
                            'height': -4957137139613420680,
                        },
                },
                {
                    'window_id': 'ț˹nˮϛуŸĿūҡүΔɣŹÄ\x89ҠǋѪʠɳԗӢĤȓԒȩҾĥӜ',
                    'location': {
                            'x': -6361318979000508515,
                            'y': -2091801016139981201,
                            'width': 8105081636193848929,
                            'height': 2316024578550131137,
                        },
                },
                {
                    'window_id': 'ʶŖӟѬғԟħŏǻϕȏ\x82ͼҺ˒ɲ\u0381Ǣɫȫɂ˚QȲêӔύҼɍӃ',
                    'location': {
                            'x': -7101513784251695023,
                            'y': 2947337812171448036,
                            'width': 6343398959948944829,
                            'height': -2411814971794238675,
                        },
                },
                {
                    'window_id': 'ã1ʴŬ˫ǳƆ)ʝɲɘάӜ¢ȦǡʝǎIŝŹԫѹнҕ¡ΚїȬȟ',
                    'location': {
                            'x': 1682336290294115074,
                            'y': -9128489470077223144,
                            'width': -2673749177348680902,
                            'height': -4988961756806093500,
                        },
                },
                {
                    'window_id': 'ʢϲˮʩºü\x99Сʦµ\x8añȹȜȐКâ˃ŬʱÞ\\ɒǱJы¦Ļ\x94Ԑ',
                    'location': {
                            'x': 7027934781830380022,
                            'y': -5719749968211158398,
                            'width': 4617818450974128693,
                            'height': -5339514662932626375,
                        },
                },
                {
                    'window_id': 'ӷȴǗӒ˦Ӗԑ&ŪƆřǉĹħɌϔǍԬүѺʡ¬BɋΝÝĕϵūȼ',
                    'location': {
                            'x': -4432464684621941546,
                            'y': -5397552280823258611,
                            'width': 2068267945991583535,
                            'height': 3898959219843842590,
                        },
                },
                {
                    'window_id': '\x93Űǯɦ˅©ÚΑȥžǬçʷѩБɬїХˑĠƄɐðӶҜ¿ɉΠыӹ',
                    'location': {
                            'x': 3596050012698887506,
                            'y': 1498081003840037353,
                            'width': -8176518169991333401,
                            'height': 341459331945783078,
                        },
                },
                {
                    'window_id': 'ԜԇɠĐЎďŨԤęӝϔȦɈҩƽҀ¿ɭˁʁҒЂȅ˟ʓ/ĶĺŐț',
                    'location': {
                            'x': 229616595985843433,
                            'y': 6703608669421955653,
                            'width': -2658012018376528757,
                            'height': 1331516846042630357,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id_positions': [
                {
                    'window_id': '˪њ˫ĹǏ',
                },
            ],

        },
    ),
]


class CloseWindowRequestEventTest(unittest.TestCase):
    """
    Tests for CloseWindowRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in CLOSE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.CloseWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


CLOSE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class MinimizeWindowRequestEventTest(unittest.TestCase):
    """
    Tests for MinimizeWindowRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in MINIMIZE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.MinimizeWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MINIMIZE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class MaximizeWindowRequestEventTest(unittest.TestCase):
    """
    Tests for MaximizeWindowRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in MAXIMIZE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.MaximizeWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MAXIMIZE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class RestoreWindowRequestEventTest(unittest.TestCase):
    """
    Tests for RestoreWindowRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in RESTORE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.RestoreWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


RESTORE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class SetWindowSettingsEventTest(unittest.TestCase):
    """
    Tests for SetWindowSettingsEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_WINDOW_SETTINGS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetWindowSettingsEvent.parse_data(test_data)
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
        for test_name, test_data in SET_WINDOW_SETTINGS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetWindowSettingsEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_WINDOW_SETTINGS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='settings', name='SetWindowSettingsEvent'),
            ),

        ),
    ),

]


SET_WINDOW_SETTINGS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'settings': [
                {
                    'key': 'vȑŵłԁƨ˩ʖ˂ϴө¢Ǖԗέ˦ϐȮԐĚђѱϥ\x8bÏȚ}ԫΣѦ',
                    'description': 'ӕĂϳɜФќћѰƻÔӼЀЮťԣͱ˘ǘћҡрѦӻ.В²÷˼/à',
                    'value': '\u038bʀџȑeӇ˾đ˱ºӿQЄΏˁ\x9aԉĂŊƎCƋƲˢӰǎjȵďϯ',
                },
                {
                    'key': 'ӸǉΖҁǢ_іǎҎǣЦǪԛǴǨɊϾΈVӐϊеʯʨʭ\x8fπƂȟӘ',
                    'description': 'њɾ\x85ǀϐȦƥȴŪqɫæȨήψӘØϪȜʌF˗ӡȾƦѲ҈ʷԕф',
                    'value': 'ļGЍУĒԩͰɺΝњ˵лÇwƊĒτĚȯΥΏҌǽҤ\u0378ԟ\u038dơƙ\x99',
                },
                {
                    'key': '\x80ҟθɳȒ',
                    'description': 'ŵǾšɹ҉ӔӵАƚĺȭoǘёȤÛŨĉƻӻɮƼɺɩʏ£ªɛĚҳ',
                    'value': 'ʜv҉ĬTX˨GÉŜʪкљɾȦдɊ\x9aеɺΚϯЁΎƼFң¥Ƒɾ',
                },
                {
                    'key': 'ϛΗƞѕƩК\x9aǼб˩Ą˃ȧ',
                    'description': 'ʾѱΡÑ˸ȻƗŴȀЌƸϸҒϘ\x8bӑғ\x88ҦΊȏ¸Ҭӕ˨ƠzíŜƛ',
                    'value': '\x83ǜɵϓaұɛжā˵o\x85ʪԨԂɳҚɑǧѴ˳˓ſɨ¯ȤDɚĭқ',
                },
                {
                    'key': '¸ȧ\x91şã',
                    'description': 'ȨʻѷȭȆҧĴrѯԖѲīмǄN³¥э1ĉÀ˰ԤFǹ˃Ńú҄\x85',
                    'value': 'ўˇѢѾЍƬĪʤǭǥлϜɇċŔӘ˺ğê˧ѓƝѭǾӾӟ-ыQΆ',
                },
                {
                    'key': 'ϱԏӑÙҫėHŦϹίʙďηyĎєɷ',
                    'description': '˶¥ŠǭĒ˧\x9aťҊҿ\x87ӶUƸŒ\x8d˗ĎʻǤ²ӯƨ£ͽȿ˼ώԄx',
                    'value': 'ȂƹďˋЇĐϊĤύϟɃ×ѫʼԊoɳ˞ƬȪΖɑчʮ\xad\x9aϽBŒ΅',
                },
                {
                    'key': 'ς҅ʂǪбưŤŜõҮϙ˹əҊψľÎŞ3˅ϋϐɫƍ',
                    'description': 'ŨԟŜǏҎ¡ƲƣˉÊӆ˗ӨʿĜɠNƯNǘȧδ)ҖӅ˦ćѨ:Ŕ',
                    'value': 'ƖϊǪțίьʚÁ˻а\x9bьѪΫǶųԧ|ɭXΰJЀϸҦУԜΑѸN',
                },
                {
                    'key': 'ǨħтŦɌŝɎЭjɁʵ',
                    'description': 'ǷbϨӹѺªЖ\x95Ԗʪĵ±ЀԫǩȡğϝҚΎҚåÓȵӲƨ˞Yǿȏ',
                    'value': 'ώȰɃĄÀрdΫ%ƋƖʭϞκ΄È˕çÙ(ӆ¨Οʹ)ӟԈVĸ?',
                },
                {
                    'key': 'ȜƀЏOѩӵ˄Є\x8bǐɭΥīåĮ»қÜӚ',
                    'description': 'ƦƶϙŀҦǕΔŅȚxĸȻФʛnоӊǃ}ɑϗӺԛȩÊŎӸʧt1',
                    'value': '*њê\x99ȎáŴǤ\u038dӢƦĮǟÝQƺНҽІˆωʍѹϝ=ʲǎсЌŇ',
                },
                {
                    'key': 'ŜƏ',
                    'description': 'ɾЎπɔҝ±ԬɤϒӗϵώĒӅ\\Ȍ˸ҵҦǠǞͲŠǄªʍØҩǿϱ',
                    'value': 'ʣł®ŵÀǺĨѰUßƸϷƔǠɞåʵӺςѹƥǵΞϻӘԄʏϪƏǲ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'settings': [
            ],

        },
    ),
]


class SetFocusedWindowEventTest(unittest.TestCase):
    """
    Tests for SetFocusedWindowEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_FOCUSED_WINDOW_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetFocusedWindowEvent.parse_data(test_data)
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
        for test_name, test_data in SET_FOCUSED_WINDOW_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetFocusedWindowEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_FOCUSED_WINDOW_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='focus', name='SetFocusedWindowEvent'),
            ),

        ),
    ),

]


SET_FOCUSED_WINDOW_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'focus': 8259,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 1518,

        },
    ),
]


class SetGlobalSettingsEventTest(unittest.TestCase):
    """
    Tests for SetGlobalSettingsEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_GLOBAL_SETTINGS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetGlobalSettingsEvent.parse_data(test_data)
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
        for test_name, test_data in SET_GLOBAL_SETTINGS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetGlobalSettingsEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_GLOBAL_SETTINGS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='settings', name='SetGlobalSettingsEvent'),
            ),

        ),
    ),

]


SET_GLOBAL_SETTINGS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'settings': [
                {
                    'key': 'Ϯ҇Ȅѭjư]ңÇӽӫӸԒ¼`ǉ˻њЍЗԫ~ѣMŇҖΞēԮϔ',
                    'description': 'PзΛ\x80ŖњЦ\u0381\xa0Мп˘ûԑϚ΄1˒ҟÉϪ_ćǴɩʛӲÉęь',
                    'value': '@ʂĕͽΠɡɒ·ϟʞʽΰʧэ˗Ȗ',
                },
                {
                    'key': 'ɪ',
                    'description': 'ЗЩη˒ĸѕɊ·ɒȘ°˥ǂƅǰǴӅиſğƖυϓ˭ԡΰԬҔȧļ',
                    'value': '©ɹԮГƢСѰȿ˭ʷ7ӆӫӊΕNu҈ǎGɈ҉I҉ʒ˰@ϖτϤ',
                },
                {
                    'key': 'ŁҬɆǢӯiǙґȌɶâŋϢдˬɛˇƹҘģς½þҁüϋ\x91ɹȓʦ',
                    'description': 'ŧĹɌɼСǕԈ7Њθ˸şԕϔėʙǜμ϶ΏΙˈѺњƓҽώѳɅû',
                    'value': 'ƘӯϴЪΙʎƱɔˏѽąȋȲ\x91¶ϳĸԞH%čɅǈ5\x91ɉϛΜLǅ',
                },
                {
                    'key': 'ѥмɶĚÒˊ{ȪӼͺ_ѩ',
                    'description': 'ƿΜʫl҂ǸәмƣЊƣЂҏǳĞљƟÉтéʇǉʈȑƩÝ\x86TНʻ',
                    'value': 'ȁĿӫλяӞɩÌБɔԅɫˤѕӦΏ҆ŖʐǄ˷ļG|˸Ԏ¢Ӻ\x83·',
                },
                {
                    'key': 'ҞɹͰĉɯψиˬӔŷГЀÿЯÎϬɐϏԥŲӐÙóҙʘʧƣÇƽ>',
                    'description': 'ѢǯȴƩ0ɔɻŭƚĢƢӵϜˬӌ\u0379ǚƎĲʓИ҃άƴƓϊ/Żω"',
                    'value': 'ʰ\x7fĶĎЕӖэǈȶȓԇϞɉϋ҈Γ',
                },
                {
                    'key': 'ν<Χ',
                    'description': 'ΣΙѢǂȊǛǾÅVɎҫĹuÁͺμΎЀʵӦ7ѸŰΙƧ˛ЭЌ˝ύ',
                    'value': 'ʁɥőź\x9a˻ӊΜŭ҈ѐȔ¨҅ǵƕԍʫŲΏұϗɯɼ\x80ȸʽаũĐ',
                },
                {
                    'key': 'vӛƳҭˉ\x82ΟˑϧϚү}ƳΤģnԩ¶Ϧοˊ÷ȹG\x8bɑӪnȔy',
                    'description': "\u0383ȻӫƹϷҖʀǆłÍȴдћΚԮѦãćΉ'ŗϻė:ƜĽЂѸĬ˩",
                    'value': 'ĞɅŋƻǝǒbў0\u038dиԜȏ)ºĶȴõ|άˈȈƴԭǦңɉҲŀӕ',
                },
                {
                    'key': 'ȞӹƌӐ˱ҵҾõˀԦӇ˂ΟƵ˽ԉȟʂčсʉͻ\x8fɕjħÂϦЇ\x9d',
                    'description': 'ƛȱϸɶЮéƏϳ!ЍѰ˹ҨɬǑȖԥʈśÂʠ;øЕНʑˏ<ԭÀ',
                    'value': 'ϪǅQӊШª63ȠʁӰȊơʎǾͶ8\x85ƇŌӔɰˈřȗ,',
                },
                {
                    'key': '\x85A\x85˦Pʪ\x98ǀƉ\x9a˚ɪ®Ϗԛҙĵúԣ§',
                    'description': 'ƿȼȵњǶʥŴҐƹΛʊ˝ư\x90ӔҪɅүǀ˽˞ƳǦĀԩʉЛ%ҧ£',
                    'value': '˙ŨσѦҕȁҗϞѫϼǧˊxŕŞЋɡʏǋșѪǶΪ\u038bѲҷĎЏǣǒ',
                },
                {
                    'key': 'PȊәēΤËŃ0˻ƄĻÌʛ;ĊöӨɇȴԤ',
                    'description': 'ҥ:ӉˍԄ0ΕɿнϒƷÌŽǗ˹ѕˊəѮҕθЪүĲʬGрÿ¯ҍ',
                    'value': 'EɃ˭ŎͽŖēΦѠ\x8f«ӀȉёϘːÎҼ¸ȐƉ\x85Ұ˻ɲͽεz}Ђ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'settings': [
            ],

        },
    ),
]


class ActiveIdsTest(unittest.TestCase):
    """
    Tests for ActiveIds
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_IDS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveIds.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_IDS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveIds.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_IDS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id', name='ActiveIds'),
            ),

        ),
    ),

]


ACTIVE_IDS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': 'Ʀ˳üʹ*',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ŊɳϕЩΠ',

        },
    ),
]


class ActiveWindowsStateTest(unittest.TestCase):
    """
    Tests for ActiveWindowsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_WINDOWS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveWindowsState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveWindowsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_WINDOWS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='active_ids', name='ActiveWindowsState'),
            ),

        ),
    ),

]


ACTIVE_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'active_ids': [
                {
                    'window_id': 'ıÇϓRƖѽĻѷƭЕɠү\x93\u0380ЖӛÉͰʬɝÿ´Ġι\x9d˞ɖӰәӻ',
                },
                {
                    'window_id': 'ԦԄ˨´ŮшˇѢʑ¤ЭÖȔ¾ɍǨĔøӁɺčěф\x88˝ĹĦɌ\u038dӳ',
                },
                {
                    'window_id': 'ÙӁɗʐϜďӟԔԞƵɻǴӛηɋɮΩĨќӹʌȝϐ\x82ąҺОǺѻ~',
                },
                {
                    'window_id': 'хʿ\x9dϑɻĉҬͿŬ,~ҪŰʃро˜ǃ˳\x92ǏŃțĠλ$ȅȋɉÀ',
                },
                {
                    'window_id': 'ѹЭǀʱ\x8c\x94ȝſѴϋƬ҅ЁČВəˌĤʻȥЍÔ®ŁѡΉǌӂќӜ',
                },
                {
                    'window_id': '·ǶЅfԈМś¾aÀӵ\x88\x8a˺бԮЯӾОԕϺХϘĜ ˬʼǼɑʊ',
                },
                {
                    'window_id': 'φʆvөƊβ¬ˢƎȮŀԀЌ˼ʓӍ´~ҎҲϠʖʻʼ˧ȰѺ÷ϸʥ',
                },
                {
                    'window_id': ':ďŦ"ʯĈɇˈϲȃ&ϴɜϱлřѮӝ˵В\x95ˍǋьІЉ˛˭Ɲʅ',
                },
                {
                    'window_id': 'ԛ,ϒ,Ƞˊ˰ɒŹ\x8aϟԦͷυʯ\x8c\x90цɂΫʼóѦ#ƧľӁėùǎ',
                },
                {
                    'window_id': 'ÄӜͻҲũĉɟàάƩǧώȄʜí#lҠşɰΧʥƹzԄӐɀǣӔӝ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active_ids': [
            ],

        },
    ),
]


class FocusedWindowsStateTest(unittest.TestCase):
    """
    Tests for FocusedWindowsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in FOCUSED_WINDOWS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.FocusedWindowsState.parse_data(test_data)
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
        for test_name, test_data in FOCUSED_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.FocusedWindowsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


FOCUSED_WINDOWS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='focused', name='FocusedWindowsState'),
            ),

        ),
    ),

]


FOCUSED_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'focused': [
                'җҩԪΩҲыʷɚXϙԅ\x9c\x85ˊ!ƶmȰċêŜǛĻ˷\x86ѯˇԍќȐ',
                'шϼԦѦʁƃŤͿ\\\x8eшѼ\\ǔųͽԞȖǔζȄЃөȓњƇфkЧą',
                'ѼμȵʐƚŭөüŁťȍǒɑЧğɃɮҿƛƄ҄˼\x95Цѷ\u038bȤԬɺɼ',
                'Ȅ\x80Ƌţ,ˮ¥ɞżiɗҁРʐˌkϰ\u0380ƕĆ®\x97\x84\u0381Ŏɍ҂һŒͳ',
                'ѩ9џƚoʝġȏ´ϷԩˇǱăʁ˳˦ΚĸэXϵЪ¢ɺ±Ǹ\u03a2ҲÍ',
                'ΒëʿʋхӸԏƝÿЇ±ãÍɧɖɆΚƨǕХɛǐΣΰпǶˀυÙǛ',
                'ӰȒ\u0379·\x90ʾӅĂϤΌԇǆĠÕк˜Ͻ˴ųʌɇNԀαһľӀхɽԫ',
                'ҌҘɤƆȊÝƃÍͰѮ¿Ñ\x92\x92\x83ʋ\x8fԣ½ҰʗÀķйѡР˹ԣҫ\x89',
                '˄Eĵ˸˩Џ҂\x88\u0383ǵn+щɉĿáϥԓɅbǋ\x8b\u03a2î»˨ȜʠДΊ',
                '\x95ўεǄѺŵӨѵɴʡʥώ\x8cƪȹ\x86ӬϗƻҎΞˀЌѰƂǮ˭Ɯʮ\x9e',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ӚʂΞˊԮ',
            ],

        },
    ),
]


class WindowDetailsStateTest(unittest.TestCase):
    """
    Tests for WindowDetailsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_DETAILS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDetailsState.parse_data(test_data)
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
        for test_name, test_data in WINDOW_DETAILS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDetailsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_DETAILS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='state', name='WindowDetailsState'),
            ),

        ),
    ),

]


WINDOW_DETAILS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'state': {
                'active': True,
                'focus': 1627,
                'parent_id': '?Ð>іΡ\x93ӤʼҖŵ¨ǻɋѬE϶ϧҋĠ\x9e\x8cѫǼˆǥЉȸѓҰ˼',
                'location': {
                    'x': 4964913659518775444,
                    'y': 4116997057742189007,
                    'width': -5562020069153440518,
                    'height': 3681344481386033810,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'ƠƄãҼǑϰǯˋѴќ\u03a2ʰ{Đ\x8dϑ ˚ъĵǑǀ',
                            'description': 'ϓŭǦŃ˖ҀɜσΐƳσ®ϲșΪƆԏǾЪ¾ďԥʐ[ʉāPUЃ˝',
                            'value': '/ˡȐCǻмрӺͽ8ȴťИъ\x8cЌԤίüȓЗњҬ\x9c˅ŢȚǋίλ',
                        },
                    {
                            'key': 'ɜӕƮŮʳ¶āШŀюͺŹԭȬˣɌΝǫȼфŬɞ\x92ʁđþíԛȦW',
                            'description': 'еǙɘΔΖɼȬҫύρώ_¯҃ŏɼȞϤͲȒ2ӊłѷƭʌШΝʋі',
                            'value': '4?\u03a2˷ЬĂĴ ңӸƲǼˉҎӈȠ.ғӧɢѢǾRľЉʙȎƧӔɻ',
                        },
                    {
                            'key': 'Ω}қΨ\u0383ïĮ˯ĄĊʑǂʚ΅ҵȼ',
                            'description': 'ҴϯėѵѯRŌ\x98ǣČÍӏøQҕŞϹƶ\x91ΧѢÇԤžԘʧˬ҆²ϴ',
                            'value': 'σÚώȡɪӲĺųǿŴӌҽǉЮґԎȉћϠё®ĈΥ-ΎDʉì.Ӥ',
                        },
                    {
                            'key': 'œơŰбԋүÂʼΘſъ ҅ϝϲ×ȞΜԙŴ\x96Љūȭʝ˜˜Ґʤƣ',
                            'description': 'JїH\x9cӳȋÑΖɑˊа\\õĐɵѣԬęϭȊƼÂΗ¸оҨWЂηŝ',
                            'value': 'џ˵ԗІѣ$BҌұϟӗ\x8bţȶϢȧ\u0383Αʴűō!ѢЌɱɟƭąƸź',
                        },
                    {
                            'key': 'ɃӋŇҍ΅˟ȌōϢɌt\x81ʧ˫ʻ',
                            'description': 'ȼӴʓćąƯǧQӜ\x92ųȏӕǮʃĜӤЭƅ\x90ӧȹӉŝԭɠǃԩѲ˨',
                            'value': 'ǈњΫϣǥʓ˙˹ǓΫ]Ѽǡ˗ȪÎ˒Ħʞ=ͷüԏԒƢˮ˪Nɖ»',
                        },
                    {
                            'key': 'ѤĥǃʶЃžɐя\x9dʘʏǮ',
                            'description': 'Ҝʡļǟ`ö˲ӤҹӾɈŗΙΕmêӽΛȟEҤзĀŲЕѦɖwfǴ',
                            'value': 'Һ˺ȹʜżŶʹƅѱμɄσEőǋȵƁ&Ҏ˝ʧԪƃǮďȿɟʌҺ¤',
                        },
                    {
                            'key': 'Ϩʇ3ҫ',
                            'description': 'ύƔθϩȏшŤϼѯЌΩѭʬυMϹĴЩȷëȂΪ˯ÕАʟĨʕYä',
                            'value': 'ȡʦVʒǰʹԫǡȮ÷ѴӀʭʝ{ȚȥҜǘбԙӻԦсţŦ˅Ԥ\\Ԡ',
                        },
                    {
                            'key': 'ƯǫÄôϲe˃ΒͽŋŠ\x84',
                            'description': 'ӆĦ\x9cϏÉɝɑӥ҈˪˦ʖɁΓoҺήԙľ\u0381ΪɕѽҋȂ;ʐ¥Ę˼',
                            'value': 'ċȗΫǻËϕҖɕюýŃ˾ǙÔpПͻáϳPƞŲŨbɅƂͶ±ƅѕ',
                        },
                    {
                            'key': 'ΰ΅|ĹҢ˱ĜΖ!¼ҟǒҘ҃ҹćшÀǁͽıҙXЈʭ¥ǇŅ˸ɚ',
                            'description': 'ʝ\x87ԦƌԠˣϴÕɓԘʕÙËϡ\x90˯϶ǚ\x9fˌΒĕυ΄Ǎ«Ӄ˓%û',
                            'value': 'ʎӈѸϵςӚ\u0379ƨmɼɳƌο¡öǟĶʸÍҍɡŨ"ƴ5iƶӔϤį',
                        },
                    {
                            'key': 'ЄkɗҰӵҷѝƞПѮәūͷЉОҋ˨əқ©иÄǊƢ˱Ī\x8aӗԟҐ',
                            'description': 'ɡëłѻЍǇʒыǠүϨҝԙǘʵȕĴ\x9fȎΥэѲϗʱɒϐĳȞϘџ',
                            'value': 'ɻΊöaə£ˎı˩Ľ)Ĳ8&Ǐ\x9fԀʣǮ[Ȓ˘OƬӚӚАИ˙Ӧ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': True,
                'focus': 5127,
                'location': {
                    'x': 3224381761960302954,
                    'y': 7245255399499412511,
                    'width': 1172896101062340303,
                    'height': 3987177310811524684,
                },
                'minimized': True,
                'meta': [
                ],
            },

        },
    ),
]


class GlobalSettingsStateTest(unittest.TestCase):
    """
    Tests for GlobalSettingsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in GLOBAL_SETTINGS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.GlobalSettingsState.parse_data(test_data)
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
        for test_name, test_data in GLOBAL_SETTINGS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.GlobalSettingsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


GLOBAL_SETTINGS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='settings', name='GlobalSettingsState'),
            ),

        ),
    ),

]


GLOBAL_SETTINGS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'settings': [
                {
                    'key': 'yˈΦ\x8eƻ \x87ɡĸʐĝӇäɃɠÞӾʀġӞ\u0380ȿҵ"Ɓʹf÷',
                    'description': '{cµǎ©ʂǄƓ\x8bƦԢŽӉƓӔԚȄć¬ȏÁjˈ\x8aѽΐјʻҼĀ',
                    'value': 'ԅʊҲԩǧóȒϛńɲǥ\x8bλ.ŚɅΘҷγψȸƜ˰ǚѸUˣăуӋ',
                },
                {
                    'key': 'ɥǙ˵ӊſť\x8cɾXƏɁԮӖǩǤϤö;ǧȻϑɸǭЪϐÓѳoʉ˭',
                    'description': 'îДυŪδįҪǄĦ˘ýǩȁ˕Ј;ҙˌʀĺɩTΰҼɪ©VʌÇ˩',
                    'value': 'ҲͳҶуȩӈȫĩǼүf³Є°ʈȌŘ´ȟìřŚѠ}ɾϴ˄śӟB',
                },
                {
                    'key': '˔ÚЭϘíZЬ',
                    'description': 'Сƫ-Õ<ԋ\x9eӿҚЕƀˢ)åˣΒ¡ҠӤƤˁʇJƗ¬ӮǪ˼ϡǨ',
                    'value': 'ʏǨ\x96πϖsɜõљтԆƨˢƗӶβňˢӰ%di<Ĉ˽ÉùҖĲȾ',
                },
                {
                    'key': 'zWÛ˴ӭȁњэýѐb\x94ȡɱƷҠŊӖˌmҁ',
                    'description': 'ӕЋȠҧǑRǛσι³ȉλǑġӢƞHМŗąɣЭȏfǈяʊʈŁƹ',
                    'value': 'ʗĘŎƖРå˄íǺϬɋϙԝÿȹƏ/Ŗĵʂˈɲю\u0379\xadƖϫҹɒf',
                },
                {
                    'key': 'ƀԩʉƋѺУǢY\x94ȲԀ¥ƆɃЬ^½ЀЙɋư\x86ф÷ɋħшҫҼδ',
                    'description': 'ɅñĮњǩӒЗǮɶ\xad΅vǫƖ1ԊŞZОȼŠдƅϪʻɟԍҀϋˍ',
                    'value': 'ʎ\xadѸҗѺʍȉ!ȅѸ\x81ÝƃȆ˵ĚԪϊөϦNГƦҪҙĴǴyo¤',
                },
                {
                    'key': 'ǤђíҚȍӌȲ?҃śʰ\x86ѫlšʚȣļÔ¿ÙĬ¿9ëȡÙʏϒ˓',
                    'description': '\x98ƎǪyįȑ;ÂʭΉɲɺѰʯŚΏʡɥӭӔÍͳхјҥѐΛЦДå',
                    'value': 'ɗ˧ƣŘӸŢģζϬȝŰô¶úřίĸȘ\xadhϣғҊʡ\xadκфŀх\x99',
                },
                {
                    'key': 'ҙ˙Ϸ˒K2ԑǒȯϚϊНЯϰʿʌ\x87\x80ʠÒԓʴ\u0380ŕуϾŊÍēЙ',
                    'description': 'ǽр,ҨҲĻϕĳƻɖͳӐəǓԛ\x93ɮņȓ°Вӏ҇ĳˮȍԋÊƩӂ',
                    'value': '˰ӶǛ\x98ʒ˥ϣj²żǡУDΛ¬Ͱǡҹ˟ǀɠΪʕѭŀfºмёЈ',
                },
                {
                    'key': 'ӚBʏHËĐΪőә$ѩϚȪԔӤ˙ƨǜȒԇ҅ƪùȺ',
                    'description': 'їτ˚˫ЗʯÙƪVӥыԬƛѲ)ȃ\x84оғάĕÔӐѲîėˁҬȵǛ',
                    'value': 'ˑΦӥʲȧÅˏӧЀĤǥӖә¥ņӮѸ҃ӅÆ¦φɾŏ§˾ʟЇѺϡ',
                },
                {
                    'key': 'ϤԌʴԈȑŔĠ҂όŷΪ«\x98ɎϻʐхśʼѫӦȚʻaϘˢưͲɿ«',
                    'description': 'ЦǷßČėƢɖӟёĔƿӑ҄ɂ˚Č˵ĥԛɬчúkĘGƇɯ\x9eӢх',
                    'value': 'ĩӬǉԔ҃ΪŗѯɡŊԒҲԧԐɻƾοŽʌæ҃нʻԧţҶȜϘʰ1',
                },
                {
                    'key': "ȨɮиϾɎϽΆȝƋϥмŗǛŠʁGΠГåѵĵԛ'ÃuІʇɠȿƧ",
                    'description': 'ӝͶ͵ÃԮʻNӏʺǺĐȁǐȐ˪œʻW\u0383Ј¢СʧʻΠɟʡШϞа',
                    'value': 'ҁ1ȅěψϑόҳКƣӎӇδAѤԃЩːÇԏүĄĿ\\¿μѳ˟&Ū',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'settings': [
            ],

        },
    ),
]
