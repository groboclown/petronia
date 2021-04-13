# GENERATED CODE - DO NOT MODIFY

"""
Tests for the window module.
Extension petronia.core.api.native.window, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
            'x': -7036691566014895134,
            'y': -8151129837696754574,
            'width': -7743570807663758315,
            'height': -4599710681594794788,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 3133046835724479242,

            'y': -2464192420203952104,

            'width': -3223307893664913696,

            'height': -9162938566161181821,

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
            'key': 'eҚKǨ<ʘŋ»ŢϊӺȝ\x96pԄŚԒѥσ«ȺŃƘ\x95ǙɔąŎ·þ',
            'description': 'ȺӼ˳\x81Z\x81τoƨЄůTǦȮĆ#ƜĊҸµ˯®əΑäȴίѢƁɎ',
            'value': 'οƻ:ҟƄQŔϿ¨˞ҧ˩ɢȟХҜĂԗПʰΔήԧԀƝϖѤɽuμ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ς',

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
            'active': False,
            'focus': 6972,
            'parent_id': '\x9aџɯε?ΗĀyˑƫƁ΅ĉÁ˧\x8eˠŀłԁԅԭӸũϟԐ\x8dțҦк',
            'location': {
                'x': 7012016810835842893,
                'y': 6738752885851935372,
                'width': 368651159245916823,
                'height': 7247074840622905597,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ʐЄЕ\u0383ԁĸχG\x93ȆӼԐųЅџƣŷԟ',
                    'description': 'Ύċ°ѮǭYš/ìτĸÿβЪ\x93ԡȣΏ˓ΰΒɚîһθǢƺ-ƤȠ',
                    'value': 'TԬÛŃξʕʹʤËɐǖL\x96ԪȖĎ@¿˺ƩͶŨǨӤɨϒsǹЈљ',
                },
                {
                    'key': 'żʣǩþԘҪkҔԧӇкOƋʕɖҙˊ}¬ҙɀдOД\x8cɘǄÀ',
                    'description': 'ӄș\x92Ǣ\x96Ԯɞ˭æд˗ǼëҎÛ8ѼČ&əéΧ¡ѿҹ˘dҏЗʂ',
                    'value': 'ŐƖ˸ДðҕҏΧЦρǭõǏԒɧΐwӎªӏĴÆθɊaɚĬңͼϜ',
                },
                {
                    'key': 'ԇbСǝ',
                    'description': '\x9fɵˁȅϗƈҤǯʓ˥ЯµPӓĴέɰƿtBӑΥϽѲjɇɦŔΟġ',
                    'value': 'ÑƟÜ,ºz]ƖВáРǶЀϋАȡˇ˥Ȍ^ȐΆѤѓ϶ԫŜ\x83˯Ǫ',
                },
                {
                    'key': 'ӓȦƣТ)Ӆ\x89ХӇʾϡ<ӘȻ\x9b¸Ś`ƦĄŨɚÃdĸɂϼЅҦԞ',
                    'description': 'ÉЂ\x9diɲ҄êÖоӬJɧИüӍҺЭӃυîȽӏ˳ƤʀӞȀμĆɉ',
                    'value': 'ϦɖӍȌĴԚĺÔĨǓщХϦѴ˗ƛůŇɧʤҕӈŞǄȍұ˗\u0382vӖ',
                },
                {
                    'key': 'ϟȲƹΟ>ÍǹӃńƐѺȎ.ǟƲ)Ƃʈ3əɡΤ',
                    'description': 'Ȁ`ɮ·ҕ҉ϻȵtϯĲҒͳԇľγĥǇѣӏėџҶĴɳӴ\x91ăӕz',
                    'value': 'җ5ϲ˚/ůϑ\\ɻɕβ˳ýļlƬŀʨoǼԗʿƶǅˑɀȳʙʥʖ',
                },
                {
                    'key': 'Ϣ±ʘqЩĹœ1&ѥƃҥȴȴ|^ʷΒVΦӔ˯±¿ҊӘF<ȭ\u0383',
                    'description': 'ӠĲƃǢғŔËƚЇԩ˾ϖԒǕϣʹЋҜϪςȆ˓϶ƀǥŞtώǿю',
                    'value': 'ЄŤПΠԉȯȴͶҧƏʡϸҖȵȆΎʬӕɡԀɢ\x9dРËĤʈ˗AŘƛ',
                },
                {
                    'key': 'ɜȌƹԌҸüƬǪÁȠΜȷýѯȣċʸż\xa0ԑЮŤϙŭϘˇƯӰǭЕ',
                    'description': 'ЄԌђΤăҕҕέӈӎϽĚˎǤ˱ԉГŪƟģЂеxʲͺɍȆƬӁɬ',
                    'value': 'Ӎ˜ӵǅҬЧ9ʾɂʀ\x9aüǢΆɅϚΒЉTĽϐŝɄÊē«ҙŤφШ',
                },
                {
                    'key': 'ӿŋ',
                    'description': 'ȳƦŚǋʟΙѠȾ˂бʦȵŰΜӪ,¸ӮˬͳƃŌŔӘƈԑ¯Ԛλʖ',
                    'value': '\x96řËҤǥɼϷǴðǋ\x99˯\x93ЄūɏæїѠȹмϴʶΥЉԆ±ϨˀҼ',
                },
                {
                    'key': '΄ΠťĚ\u0380ş\u038bʩԛ2иËǭɠɶǶв',
                    'description': ']˗\x9eήЁɗǈC´ğѧɂξʐԙyɍʮЭɞǛԕеtǟжӐӇb˃',
                    'value': 'Ӝ"ξӽӁblSŏɄĿĪŽҳÏ',
                },
                {
                    'key': '@ςƻ½ϧɎęҸϴӭɔž\x86ƙʧΟһʙ˄жȚƥːΧ',
                    'description': 'ӹҾʸʰɲ˰ӹΤΪĀɟŲǢqʾƜԖ÷Ķ^ŏϟȑ?ŪӲĳԂŝӌ',
                    'value': 'ŐΈRĞā˾ӆğȴǈǼʜķģϙ«ҁ£ɄȎ\x89ˊǔʀԭ\x8cήΊӟņ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 3049,

            'location': {
                'x': -8475865792728898964,
                'y': -6658367349099340533,
                'width': 6188527396883991251,
                'height': 9002435973944058519,
            },

            'minimized': False,

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
                'active': False,
                'focus': 8317,
                'parent_id': 'ǟʊĂҚʇҔuǢԆǧɤΊҕƯХȎ˺уĳćҐŲȊϢÂ\x82ϪϜ?-',
                'location': {
                    'x': 4254302883735813094,
                    'y': -48893286596094477,
                    'width': -1054118430336199581,
                    'height': -1548358223625903567,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'ҧЭƙίċDη',
                            'description': 'ќ˨ɻĪӒѯҙʛɊЊтȲˤΞIǓƚéƫʘʃ°˼ҢŨп˚ßΈӒ',
                            'value': '\x9dʬ˫Οäϖčʔ͵ğԝϦ НљŤАɽΫ|ªʚҦŘѲЎԈȺʁȁ',
                        },
                    {
                            'key': 'ϵӊҷɛЏԆĲӻ;ʗʤһǕ΄',
                            'description': 'ȴЖӽȸԖű҈Ͳҥ҃υԊӶӞ¬ήӴ˩:ҷăнȌɻЃ\x9d˴ͺÑҎ',
                            'value': 'ЛˢķȮʙȤѠšȎσӚĦˠŗ\u0380œКӷΛͽүƁɤƢĉˎέʠƗĘ',
                        },
                    {
                            'key': 'ɀв^ĩʱϨθϦŀÊӹͲΈΙĜƸǛȬђϪƩӪȼɗaÝľњ',
                            'description': 'ʽʂéϢүǈɊΒʉжżƒғŚǋǇ+ίѧеԛ҉±ӢҩľӒșșў',
                            'value': 'ìӿ5î˃ÔӚǝˈȴ&ɡRȽÁǧϛčɓвҚ.\x8cмӞϩЧљÕΑ',
                        },
                    {
                            'key': 'Р¤ÉƘӝðѐЧӠѫ˰ϓ\xadǍʰŏɇƚ',
                            'description': 'ӉыͱӿʱɅăůҋĊɟŖzяԊѢϟȃɓ˽Ŀų\u038dϧˁˬŏȟѻѷ',
                            'value': 'ӷȋƦж˰ҬǏҰʕ\x9eƴΊ2)šҩ+ѡȠwǻοGɁƁ&ΞХˮk',
                        },
                    {
                            'key': 'η˴ѯœ\x92ɺąʏ¡{\x80ҩΝȀΉŵ҄\x89ʩǏʹȚãӷÕƙòԀƗö',
                            'description': "ŋǹϓʋ˄ɽ\x9fΒ҇ŗí»/҅þMɂƏ϶ԡҞʴʲπǜęǞɜ'д",
                            'value': 'ʁ҅˜ͼѼøҏœϛɸƊˢƯȐӬ½ϿʽǾўțǆΘçȤ˼ˮ˶ɪɰ',
                        },
                    {
                            'key': '͵',
                            'description': '˚ƺԪÎ:ö/҆ӈŜΙ\x88˙¯ДĊǂľУtȏ˞ʴĦҢ\x93gΥȸȤ',
                            'value': 'ē}Î˼ҁкѐġӮӬϮȶўůԊӰԖƹԬŅɚ҉ЌĤν$Ç8Ûα',
                        },
                    {
                            'key': 'Ǐžјĩĭŕ±ӰһВɫZґȋϼӐϘӅʶП\x91ҾүĝʈǭȋȠıķ',
                            'description': 'ğďӻʠƕŞ±ýѥķȰNģΒɵóұɋпԑƇʶh˜ˍϮɆϪ˘đ',
                            'value': 'ÊŲюǄì˖ш˔ӰˬȥʦϏʽωĝˋƁԌƛѱÇȚϽ&ȎЯyӣǱ',
                        },
                    {
                            'key': 'њɰƵ',
                            'description': 'ͼϒΟůпęʜǳǳȨüЭ´ŃɓҌųłʹӬџʯВeƒɰЫƛđ˾',
                            'value': 'ʾћϘƓi˹ǪβӠʍΪԏaƄӠЕŀǍӨǔʖǟϴҟϫҲұƧɜ·',
                        },
                    {
                            'key': 'ΧόǮӤ˦ѕĦο"ɎϱüеǳǞɢƛʗɢѶ˩ϮЉѥǧтŞǇĘä',
                            'description': 'êĸ\x80˼Ҙōʑԍ¥ǽЉԃ\x83җϵ(Ԛ˦ɻȁĬ΅\x8aʞɸ@ǄȚԐĝ',
                            'value': 'Ë˦ȝ\u0380ҷҼӞņƼԁòƗВӍЉșȡ˅ҮЕɨ˙ŤȘΠ͵Ƈļʕ\x9c',
                        },
                    {
                            'key': 'ѵǬUӪȁǱ5ӑ˓ũɗ®ugғυ{Ѵ\x8eɐǣеÁ¦¶ȟ8ŰҮψ',
                            'description': 'ǦȟɞͺɁȥԨǆȔω˚Ʈʺôȃɟǝ«ɣ7ā˝їÕ\x83ƫӹȍëȢ',
                            'value': 'ώƱһƸĵСÈ3җïʄшԘćäӟϬȘӆ{PҪˇЧԟҟÇԉXж',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': False,
                'focus': 8043,
                'location': {
                    'x': -8965088778385838285,
                    'y': -5588608279900571348,
                    'width': 9025631063862658933,
                    'height': -1430393686202307751,
                },
                'minimized': True,
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
            'reason': 'Ɩ҃Ǎ˕ǝЄΪԩ˓ԀʳFȭˌ½ӌɭ*ġЭκƔѕШͱʣԎҊд\x8f',
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
            'keyboard_focus': 4064,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 6451,

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
            'window_id': '¦ý˔żȓ˺xԘϑԐƁpҝųIŸɘѣÆɇyjӌȝӋĹΙ˜ɼԭ',
            'location': {
                'x': 4040455239931253578,
                'y': 3423628207898537387,
                'width': -7093625816494324473,
                'height': 9125930941025634829,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'γ*\x98ȸF',

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
                    'window_id': 'ϡˡɅбŮ\x95ӝČüϨīƚύȕƖɱ^ʏΩƀŗѴӡϊnÃĻȐŤѴ',
                    'location': {
                            'x': 71891162033512255,
                            'y': -182059408521046551,
                            'width': -3685833226953701343,
                            'height': 6146670856304511177,
                        },
                },
                {
                    'window_id': 'єǬĚϟ˙ƖQИġØϣOӔºǠŽћªˣǗƊпԉέԔř˽ȢɗĊ',
                    'location': {
                            'x': 1451473080595992385,
                            'y': -8508641416638601841,
                            'width': 952314364784469231,
                            'height': 6079883756079459153,
                        },
                },
                {
                    'window_id': 'ƣǁ\x88ƾҮjӣ¾ìϰӦˮGԮ\x8aʁŻÁ҉ψшśʷĂĲρ°Ɖȗ ',
                    'location': {
                            'x': 5486526560751676002,
                            'y': -617260756948210029,
                            'width': -6916986553418295754,
                            'height': -5261676410738044739,
                        },
                },
                {
                    'window_id': 'ѿεώȗŉʷ7\x82ΤВȢȗӑƨâǥˉǦӜǂˊ3Ȏá·ҍƭ˩ng',
                    'location': {
                            'x': 54256339168909689,
                            'y': 2897168570626411281,
                            'width': 930595163827332685,
                            'height': 5436733866464807515,
                        },
                },
                {
                    'window_id': 'ӭ˃ě\x99ҐёӳűĨϽʆǠȭÃ«ȼʛɰˇǁҚʣ˰ҤЄѮ˖єћќ',
                    'location': {
                            'x': 8081017638011925434,
                            'y': -663958028846966529,
                            'width': 8702097540955296100,
                            'height': 5123804106755974006,
                        },
                },
                {
                    'window_id': 'ƍ\x99ϠáѹҴžΏѳҴˍϗӊΔÿНǏш˛ˎ҄IɩʠԆƓұǸǸϹ',
                    'location': {
                            'x': 6941771842950967520,
                            'y': -7246563760419771890,
                            'width': 6902442469019901517,
                            'height': -7590471080585697190,
                        },
                },
                {
                    'window_id': 'ѩ˜φɨƑлņǍĚНǰbzˊԅԙʂ\u0378ģcϦ\x9aϫФſŜʉƕʟ\u0382',
                    'location': {
                            'x': -3049364762394673953,
                            'y': -70785657929547934,
                            'width': 6878516971158785288,
                            'height': 8979811827078551406,
                        },
                },
                {
                    'window_id': 'ʕӳ҆ЦŭλҏƬʼȣԪũҺǴŭģҹŮԧG˅ȡћ;ϳʄчɝˍҫ',
                    'location': {
                            'x': -1385675082500171447,
                            'y': -8639137562299400243,
                            'width': 2153412156245513642,
                            'height': 1212418971704532569,
                        },
                },
                {
                    'window_id': 'ʣҳӟӵǌŵƼԫʃ)ФǇɳÄ˼',
                    'location': {
                            'x': 2430440485859094793,
                            'y': -7472699010761247569,
                            'width': -3024354212557658684,
                            'height': 7033339239832098531,
                        },
                },
                {
                    'window_id': 'âϋǢôҾѨΥџ,ʊѽԚԟȾƥЂéȀŷǽўҡ\x90ǮϘюЕˀ˭Ц',
                    'location': {
                            'x': -8072177183492427699,
                            'y': 8462276183838278199,
                            'width': 5067090406286209002,
                            'height': 978446480023689102,
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
                    'window_id': 'ǽҾņ´ǵ',
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
                    'key': 'Ą҂łԓӁƱ',
                    'description': '¡Ìŵ/~1¡ˢŵʆrȭķɌÇŴшВӳħѷԂԨϜǓʹǃӵ˔ʏ',
                    'value': 'ÓƺȖʠ¹Ңuўқ\x80\x86βҨ˪ƖςғƛčаÃŁЄÇʤʾ\x9cѭ8ψ',
                },
                {
                    'key': 'ǂÅ҃fΜVψԋñƊAñɅŕ~',
                    'description': 'ż¹ѤŘ\x85ɯЩƹϏПΆFǞͼƩtàӜŒΡʉʨƯÂĄҾȲʹΊX',
                    'value': 'êǜªTͽɉȴȍǝиΎ΄ǂ҆ѕrɩ94юȕȄύӃƒʍԁԟэf',
                },
                {
                    'key': 'ƁԛϐʰǁȏШɔƛʖǲɱͷвР)"Ήgԍôďεȡʵɢkȥˋs',
                    'description': 'õĈ˴\x94ʹǪŘΣӗƹ@ɌӡŕϋĲŇMƤҼԬzȒБį\x9cԏƹ˗Ȼ',
                    'value': 'ƙĬª>:î\x97˷Г',
                },
                {
                    'key': 'ϥɋ¯ҍÈԥԈ҅ŶΝЉȹʅIѽʌɪЂϑȈçğԚέƬУǄϲʛȢ',
                    'description': 'ÜĳҘȸɎӂѴĔÛƌΟϖ\x8eӑȯÏи͵ȜÅǈʲПƝӈ>ΘѲ¢ʡ',
                    'value': 'ƺѣ\x9dʈ˥ĥǳÖąҏ\x95²ԟԭƢɴ˶(ǖǞʠȿу҆[ōƋҔΏľ',
                },
                {
                    'key': 'ƫϪ˙\x84Ԥϝѐ\\ЪoԒҰǎγȔɵ¶ɚʂȑѭŒχTΝˋɮκіe',
                    'description': 'ǆȓÿƁԗȡψ˲ԣ\x83ʩŦǈϨŭҊ$\x8bΪˬóŊÀǇǡԏэҪҗB',
                    'value': 'υƍХLѴ\x8a\x91һϭѓǩ\x97π.\x8dΜǞҀǔtÄſˠťɃBҾǁъԚ',
                },
                {
                    'key': 'OӞͰϫǋԚҥƀʩӡΰɑ\x93ěȈыҙơƯǫЦčŬ8fȒ\xa0ǫ\u0378s',
                    'description': 'ʢ«ͲÆĄWӋжÙŢϗΤ˪Ôԁǣ¡кǞϓ¾»Ӄȅƒ²;ћ+Ԅ',
                    'value': 'ѫ6·ӅĒq\x9fĄϗ8ԤɵǞ\x92ҀYȷʹȦĤӑǪǝ¿nʥʺøԌӚ',
                },
                {
                    'key': 'ʥÁhðӺŤîŐӇ',
                    'description': '~ĨЯĊǂȪ\xa0ŦѐɰͽԨѭƝɲ\u0381\x86ΓIȖƆʹƒϐϪƤˋɞʍȭ',
                    'value': 'Įҁ\x88ɿµΙԛɛJǗәϹҍπ\x88ȏȣʇ˴ȧ˗Ѝ˲¿ƃ\u038bƫȓʱĚ',
                },
                {
                    'key': 'Sӌƈʯрʁϸɣɺԕѓ\u0383Ǉʔö}Ɏň\x9b\xa0¥πƳŀŢϕйтϒѸ',
                    'description': 'Ș2ӸƇӁˁȇIǌõʽO˒ƺ\x88ͼƍϬĹϪʤЉ\u0383˭Ɍʧ°ÏϑË',
                    'value': 'Q¹ǫϿҽŰќČűƣɘʪǮʢԕӮ;ʍʤ˜ԉ˳˄Ɉ^ʴӴԪȔ\x97',
                },
                {
                    'key': '˓Ɠȗ«ǯɥ0ûΠԓΒҧΧŢԀҭӘϽ1ɳäԃҘpԎŞʛǛԔѺ',
                    'description': 'E8\x9aƮΟÅӯĊԀɻPDʂӆv˄\x84ьξ¡Ұ\x8cЍћʡƭԚǩʕæ',
                    'value': 'ǫʇŔòԟѨɳȁΏӕҸԢȆÑ\x95ӋпǦȆˁϿÖȣɎѷʎѪćΣ@',
                },
                {
                    'key': 'ŉɼěáţșǛɖŔɻΚ',
                    'description': '˔ÝǲɇϩӪĥӍ\x99Zʲ\x93ȓĕÕȆŹòω+ҍ¦ǏɊȩħʦƚȄ\x8f',
                    'value': 'ƄΤˢҘҭ!ӿʨҘ#¦ǢʋåʣųнǢκĄ',
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
            'focus': 5434,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 9158,

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
                    'key': 'φĊҘčȶǬưĎǘl˳ʰҍͽg',
                    'description': 'џӚŶӧÃԩѼɃ˲Ȉ-ʓkÜåŗњʡŋɒƘ\x84ҫȔϻlΉʫѰʌ',
                    'value': 'İӀВoųʰđơ[ğӷӃёƧˈĐˈù>иϪȥäЍƚĬ2юţъ',
                },
                {
                    'key': 'Ȟ˕ʯѬȋӏĸԎǉáэŘľЯΟQϐҾ˰ѸãάӢΚµ}ț\x8fʟι',
                    'description': '?ӀÑǤà\x9d0ԕÌӣȁˌѵƈȺСϾÈϥМäŜ\u0383ŅԬѨҠÝлӡ',
                    'value': 'YʀϛԚʔʇȷѨɌ¥ƍǘƝǪ~ſ©\x9bǌϒĺʿ¤ȎΛȒƁηαй',
                },
                {
                    'key': 'ԩŜŖȉǮƀԊΗѳƨҸsÔƟʺͲӿҳΙˑŮћƖϊЮïΖĹӰΡ',
                    'description': 'ÑÜӼԞӠǂȢPɸúӔńǱ;ŏΆǤȺ*ȇŷΞӏÚӓȋÊεғˊ',
                    'value': 'ΐtοНѧèŲөюö¬ɛѽģЉ˙ǭě!ӂaƌĳÂ#ɓѾѶˣÕ',
                },
                {
                    'key': '\u0382ʱǽ҂ĢȴċǤɎ\x87ZˎëʥōŚϬԒ',
                    'description': 'ɓȁϠÉǣ˖Ãɴϥ\x99Ѥƾԣώѳ£ӂʬӼǎɋǶ϶ʱĪƜУɄͲȏ',
                    'value': 'ɵЌşŻј²ŲΰŔʹϢû¾ɈСσõȑȡѕĔдƝȫΑϢԜä&Ê',
                },
                {
                    'key': '˚ŔўɢЭŭ˕ѥ2ұɬΦlƹǈȊ',
                    'description': 'ǔʍЉԏѻСÝŜуɧ²ӊ˴ԛ÷ĞțҴӁŷˆÈ҃ГǺяϸȷíŗ',
                    'value': '8ƞϡԉàɠĖS>ĩέѧКΌʋӟï\x82ʖçϙƕȫӁΆ\u0382їŒī¥',
                },
                {
                    'key': 'ð«ʱʼũԟɬ͵ѢǔǹΥЍҀφӕ',
                    'description': 'íƤѾѕ˥µʔĳԏz\x95ϵаВӡдgďϬŒԥ8ƶʖ΅хҕҡуã',
                    'value': 'ȿȿ8НȂː',
                },
                {
                    'key': 'ϙϼϵϾԋϨ§ӱһԜU˦ʣХȩǰΧШΒ\x96ʹϲëӚùUĉĖTƹ',
                    'description': 'ԋӛ\u038bäӡȢǨɼш҇ʯԏ;˪ѣͳPӜɀŬʲȤ˸ƲШϻĲǊ҂Ӂ',
                    'value': 'ϰҸ\x9dɾԍеĎɽƘ҆HȯϘӬəõύĤӶδǮϳŏĺÜЭŭĪ˼Ӂ',
                },
                {
                    'key': 'Ī¹ĕȣķŲɳˠƲѝȱˠҒ\x85Ӎ¬ɞпɰɿĔɾcɭƏǿМІƃ©',
                    'description': '˅@ɜЖĮġЃлSЙș%ĒbƸѤҁɶ·ŔӾѝőΟ\u0380ЇѽȃӷŇ',
                    'value': 'ŶҚɣҷɕ\u0381ɰҙĸϽ¢ДϵӍηѳ΅Ⱦwʝ¶ǮόҸӷѽʱɮǂӻ',
                },
                {
                    'key': 'ѷЉ\u0381jϲȍćεϩǑeԃƵǗīȮˑɱԙԑĐ',
                    'description': 'ΜƯЙsҾ®ȬƲĂɦԅªĩѸ˲иԛª\u0381ţԃҁ[ӸўđЭϐ\x99Ϫ',
                    'value': 'ĺþȡɣŕǖҌɪǏ¹(ԩǄȶûɾëȪԨȤѕųēԮӕϿʀȂPɲ',
                },
                {
                    'key': 'űελ\x9fԍťЎ\x88xÅӤǣύÉûÑɹ\x93ȁʶ£ǽϕҵŃ\x84ʚˎƐ«',
                    'description': 'ĴɏɏǠ϶ӨǓĶϠˢѕXđɘά˗çҗѽ9и(ԆˑЈêʤǁDł',
                    'value': 'ɷʻӘʔüϒѣɩʲԦǄű(ȏĢыǁϢԟрҘ˛иΞŰԖЧӝʼå',
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
            'window_id': 'ƃĦά*ҴȣĴαfʙ˹Һ;҇ѱӍ˖ĩʀúԂѠЮӉҥεҞʂÖӃ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '-ăŕ˃˛',

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
                    'window_id': 'ƠЃʶԄѩͽѝԛȭϜйź·`ӚОƇ˫ΎäȓѻҔԭĖʲПsǔĽ',
                },
                {
                    'window_id': 'ӠѵʝџӹȣťƯуϸԪʕϳɎҫǎΎÓ˄śǢʓɞɤɜϱŰ,щ×',
                },
                {
                    'window_id': 'ѮƿԒƬԊĎÙзǈѰӕŧӊȄƟ˻ɱύкӹљͳĚĳϿ\u03a2ҙɯF\u03a2',
                },
                {
                    'window_id': 'НʿȠʑȚ¨ʕ¬Эˏ҇ˎ˵×ӕwȼҤĳÖӺʽμÜЇɣʵҀȳӺ',
                },
                {
                    'window_id': 'ȣҭЏԌȋЩΏѐԁ˯ӟрȻ˛xјѬƊǷ¶ÐɎǰԈͲɔњĶˠ]',
                },
                {
                    'window_id': 'ȫØЏǴ\x8cљèΡȲђɬŻʪ˖ЩzÍƣːϲӱоľБϔãhƋΗŬ',
                },
                {
                    'window_id': 'ōϦҙԋükϲȄҝèȀӣWŏӁ\u0379˕ԮЕȯǊaϓÖӝΥ˰ŜŝԮ',
                },
                {
                    'window_id': 'ǄāίϭļӺѶӋӡϩΗшһȅëµΦêŧÆȽΞƼҘͻҢ\x8e˰Ĕ˴',
                },
                {
                    'window_id': 'ͼƫʻҨÞÖǛǾ\x83ģŹӵǬ˥6ӡ\x89ɖӡƵȤʡü\x97җEõθѨё',
                },
                {
                    'window_id': '¾6ñyÍˤЂɊ¦сȢʄ˩ĸƳӣǁҳͲ˦ÛƺP©ӂδƠ\x84ҡΛ',
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
                'U¾ÿͱѕʗˢ\u03a2ÔǎİʆǄӧƉ«ӡøȽÖˀϝνɁ3аäȳȒӶ',
                'Ȉӣә\x83ǋΝɆĦ˩ϲ.ӼĄLҤ¹´ľʄ˸ŊѵÖǏǇǗŔvǠФ',
                'ȏ\x8fӏ҇¶ĠϢĦŰιɈвӖҧξЦʙϦψҋ΄¾ѝŎӮCŊǔǧҦ',
                'ŨлҜңɿЗĀñǖ˘ԔÏ˴Ѧɞʝԁ±\x8cɰЖѠƀ§ИfЂȴЮǬ',
                'ыĂƍɚѕɜʧԊԋʓ+ƪ\x85ӔҁСĝϹοBƓϏĳɕŢɌƃΡͶʳ',
                'ЀЖǇͻĽčтôŵӳЕtŹʊɰÇő˶РɑѪμƑɿ˙ԇтΑǇĬ',
                'ġϽȬԀƨϲʚнńŗˡnȻʨŘѩЬÃԚĹÝҴƕԤ¢ƺϩҀӰƐ',
                'ʇЎ҆lːǈɓϒϯƤѢә\x8fǥBˑҕҬ9ɜ¿ҕӘʲQʐāӶѫ¢',
                'Ұґɽ1ͳԫǟġtƜG<ǺįюȷȓѰѸѣΨǅ\x88ӈɞžVĘƊȵ',
                'ɯ~ϡњˀ\x91Ö˔8ԣɚĢƺЮɗôQэԀȄ˓`ʬǉ˸ļɭʉǆʷ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'Ϡѡ±ąù',
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
                'focus': 9750,
                'parent_id': 'ύǢƽΖǚƠϪӖǞҰɀ!ӽʫϱүжҚҖϳǢ¤>ΆєӐʯN˭@',
                'location': {
                    'x': -8527683967330283642,
                    'y': 1862385248126065152,
                    'width': 6161371190881458924,
                    'height': -2669452074034416867,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ʘʧԐŬó',
                            'description': 'φɋǁƔăǭʥӁǠԁ¸\x9cȰǷAǟɳOώ.ҊʫӌΈêǦĞлı7',
                            'value': 'ƢŲԌ\x97ɱϓEϼÛѓúϝşтҠȁƊʺΗȾ1ӑνȪά\x8eƂԄȰʫ',
                        },
                    {
                            'key': 'Ұӱї˪Rӣ',
                            'description': 'OƁȎ\x8ařʖŬʫРӵώшίɄӅÏɳпƞŏrː*Ĭ\x94\x81\x94æĴҼ',
                            'value': 'ʖďͿF²xĭĠéęόԛǧώϥҩӋȁčƏȴϞ\x84ïԐŖĘЙ!Ό',
                        },
                    {
                            'key': 'ЪљķЉyЇԠʧɴҚˏ˰Ԭӫ\x9cƎˤӨȑЎͳʂϰ͵˅ѰϟȭȊɳ',
                            'description': 'ЛɽǬϩʶ˃өԚŔƿ˴ɣ˘Члсʥӝϙʆʿ;ÝԈˁĴȷΑ]Ԡ',
                            'value': 'Ϩ˓Ω˂ѓɜґΊϾӘӁƬĢɇȊǇԢİ\x8fȪυɣʙъ΄\u03a2ÛŚϜў',
                        },
                    {
                            'key': 'ȺЌʢ˹ƒҞʃȪǓԭ',
                            'description': '±ˀЛʎȯЎƃŦЛˬÏΓӇαԄ\u0381ǩǁ1ĿΗԥРҰÿΩѷŌƽɸ',
                            'value': 'Дҵԡ3ϮǴʎʅчѦЩƭӔўÕҔɺиӌʟȯ\x9bԛԬ×(ƅŀӢЃ',
                        },
                    {
                            'key': 'êψѓӷɡӊЅԪϺϑ˥˺ΈϘǥɾȻˈŁҿyǐɋƪОϰэ˦Ҋл',
                            'description': 'џȳϒǪ˥ˊƪƛ\x93ĳtιǘˡȩҍǚʹȢJũțÒύЮщԋоì\x92',
                            'value': 'ƟʜҮӴ˝Õѿ@#ǉӆғȉ\x9f˩»ԋȟϮт@ǲԘáŰϛśϰҾƆ',
                        },
                    {
                            'key': 'иƍЇҼѡ҄Ǽ|ȈвΘӾ˥ˊZĺöΞ\x8d}Ĥ×ˆΌӥǥҫЂҝЍ',
                            'description': 'ϏǪғԓəǿjΧʢϩԏбҐ/ȣɤԫχʱκäÒϭҠħǶ˽Ԋċ˲',
                            'value': 'ϿЈɚʠŭKӮƄӠοҌǧĦˉмˈ\u0380ɁЩϋуƩϨҹ҆ήɑ\x83Ӂ°',
                        },
                    {
                            'key': 'ϦԉūÃ\x9dĳ',
                            'description': 'ýőҴȾ҆ǵлҀĎΪϪ¿iӡ˴ĬƷÒ\x89дҍ®ŀϡӊʝ9ҁŊï',
                            'value': 'Ʒ_тѣǞ9΄åġżǡԃ2˨Ԃҍғ½ҫ²bмΠŹˌŜɹРñʺ',
                        },
                    {
                            'key': 'ѴҌaĶѿӫ\x89ƧΗʤΖʁũğҕǳ½ƞԩˈ',
                            'description': 'ѠЂ˼ʼęҒȭԟѵѮԉÝңĤ\u03a2ͿюoІωƝϷЋǰˎӘΜǴʍ˅',
                            'value': '\x8dÆҼűǗÄҧÃЈϫ҂ҪË;ǈçlžӠӥ\x86\x9fƕĴɂÍŧʥҴǦ',
                        },
                    {
                            'key': '˥ƧԦєԟţΖɈˊ',
                            'description': 'ΆčˈǽΥįНəʊəêƯƣԖāвȬȑƻǁũĵȉȤµǠ҉\\ǥ\x85',
                            'value': 'ȯƀ˔Ɋϛ\x88#ӆśѦĖǃϸҞXĬѾ\x8aOɛҢӻǥӡʠ΅ƫҭ˝Õ',
                        },
                    {
                            'key': 'ϧâԤѻóҙϕҡϷ\x95ίˇыɄāƵzѐѤȒ¯ԤŤĐѫΦдɰlɡ',
                            'description': 'ѿƍҒķüԗҺӬъȏĨ¢ʉџҐȄУ\\Ґ|ʸ-əʐ˱öҵìΑ\u0378',
                            'value': 'ӂΣˢѐͷȳϴЪӪǪ¦ӋƹĨûҫǫѼȀҏϻФʦǙţĺ÷ύԌĮ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': False,
                'focus': 3377,
                'location': {
                    'x': 511155916370217173,
                    'y': 2345343338040737016,
                    'width': -5730611805939400196,
                    'height': -6943434067305478315,
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
                    'key': 'Є˷ˤʵˑоƗŏўȪƉțКϞ˅qϱхȭҬʚЯȋƀӔĒ¿Ͷ˓ɲ',
                    'description': 'Ѵѵ´ϸ¿ԑͱїԚѢҤӅʵӓƙɞrЙǌŜґҳđчʮсШпЯǒ',
                    'value': '(ԐƧėЄ$ӾΝѲÜƨƢL«óѯЋĦƷΠÞɟϏǏ\u0381:ԃԅԀɒ',
                },
                {
                    'key': 'ӂ',
                    'description': ' ϱч Ӫ˞ɼԄ҇ϝ˹ӱȕԀţǮˮ\x8eɂПΥӺҚϪõƳ<Рȕǃ',
                    'value': 'чŁƺ˦6,ϲΧάм/ƠŅԍ˧ʹʇίԀ˪ˌԍƮȣυϖ§Ѝǋ²',
                },
                {
                    'key': 'τњўħӅηʕӡ}ʵʶϹ҈ƞȾҋɍŐ˘Ҟϰ',
                    'description': 'ʄ˞ƇɠƐфԞЫɻӒǊΦĤɞϙΦžϽĂ˃ӧʖӹΟψ±ӦǋϑȐ',
                    'value': 'ȇ7рĘҗ°ұϻAЙԟΙ\x8cʩ²ŪȆЄң\x9aѤŤЇʛnʳʕғҝ\x96',
                },
                {
                    'key': 'ԂʛíέƔϊÜӅȩҶЈѵ\x83ԫҲӦαƴǉѠԇa',
                    'description': 'ƦȩSJ,ѝyɠǖԕϩƐ\x81ԇʙʍ҆ǅǬµˆ˅ƢçӸ\x97ǖηȇǺ',
                    'value': 'Ü˃Uh˦ŇÜ:¦ƞуёʒϬąéҋ¨Ϭøĝ˔τŭӊЬ-ËΒÄ',
                },
                {
                    'key': 'ϚҶιԡ͵ȣˢŤȽ˚Ш \x81ȫҭϖǢZƜï±ҙʡʥ˙«~˶8Ҽ',
                    'description': 'ФµΣ˩ˣӤưŝ-č\x8dϑΆɕ˘Ҙ˯Čԃˤǘϻйԕ`ʇ0ȇϪǰ',
                    'value': 'OeŕґĆͱҨØ<ļȘɗūӭθȆǠӂȔΠƃƒҴӓӴҦƕŬͲǜ',
                },
                {
                    'key': 'ЈêsʕϷƖΰʩȃΤȢȎIʴ',
                    'description': 'ˬĝƌɪ\x8bǦǭђ=3χΔ0o҈9ЧӘӎſԒñ\x99ƫĳƁĝȬϰà',
                    'value': 'Űԉȅл˞òÅҒQϞȠϺ˴n}Ƀω\x89įўεϤʋԖϜЧα×υŸ',
                },
                {
                    'key': 'ďӢzÏӕ\x83\x8b8ʯŗ',
                    'description': 'ǢHһȰïµ˸ԋԦ50ŅɊҼӈUσҾʦȐ0ϯˏѹªҶȨ>»˯',
                    'value': 'Yåþĩȥþԇ±ǾΊĖō\x98óÃș\x97ɆƂȇĆǶĐRș˕Ϲɰ˧Í',
                },
                {
                    'key': 'ʕĄʋǻʳƺʢңӡ®ČȅθԩƘОġŉѿӊԐǃɧϊÅΏˈĊĆԋ',
                    'description': 'ǴνƿɣӰӧƠϦěƽĕҧȐҥ\x9bǮʣҵɏӃʳҌȽӨĚԇƯɬŽб',
                    'value': 'ԆЩѮԩҋ\u0382Нǌ,ʐ|ҡύԃЬʾ±ɬϢŷƯ%ϵж',
                },
                {
                    'key': '´ϨԫԒƙǢǿˑσшεҼȀ\x91\u0380ʊǜĬҍҚȖǵ\u0379£˽ƪϬΑ\x9cȂ',
                    'description': 'j\xa0іʡ˶ą҆ϭĹÃʎӐŻ\x88ƓʌʎȉҤË˰ˇā˯ΫÄŭÜ˃ǀ',
                    'value': 'ͽːſǃ\x87ȮŊԥˑԧâωƾήƥΣӀœԦψϹ«ŖҼóɗ҉Ǫǟԣ',
                },
                {
                    'key': 'ʑĢȐ',
                    'description': 'ÐΞWҭѮӻԓɨȏө®¿ĩƶϣˤǇǈͲΥϰpǎɔȲF\u0378ƯvŴ',
                    'value': 'ħɃȌ҇ȮЇґ˨hɖˊθļеąҠ/ҍˆԪΜБƀԬ,ӯ½ѻԁҳ',
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
