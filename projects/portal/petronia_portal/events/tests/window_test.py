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
            'x': -5271713324937801211,
            'y': 6645304064961060538,
            'width': -4533004589676370896,
            'height': -7733427674495772612,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 5673498631813459121,

            'y': 5131894389548737944,

            'width': -5545035610933240720,

            'height': -6569913147735035499,

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
            'key': 'ѱŅH˩0ԕͲιŴџg\x80łķμԬԢʢǜÙʷď',
            'description': 'VӗȝӍǖ÷ŻȈЪ҈á\x81AÈέɿкќqŧ҉ԛÁ;ìԌѷшӫν',
            'value': 'ԝʭȱϓđԈΡ7ϲϩԂ˱ѾӧȦýĶýӝʶͲǘ¢ɆϒϝӖњ\xadĩ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': ' ',

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
            'focus': 7767,
            'parent_id': 'g·ĉ"ɞЪô\x82ˇŬгȊĢӶƚİƱΠ҈ʺȱҭĦӢӋ!ǲё˽ѱ',
            'location': {
                'x': -8652010114332137151,
                'y': 8531689028159941310,
                'width': 3805680750625132085,
                'height': 3518766422727946667,
            },
            'minimized': False,
            'meta': [
                {
                    'key': '˫өҋŀ}ʈ˵õϤ\u0380ſτßЫӊϨцʟǩä\x7fʠбκƫƠ',
                    'description': 'ΊɺɹΓb(¡ĘʐӷҤɀѤ\u0383ŚǞ˼\u0383ԗ\x8atҋӯɺӢĽϻӿюз',
                    'value': 'ŕ',
                },
                {
                    'key': 'Ą¹ҜžȌŋ\u03a2ϤϼɝƪҐ˂ĞÎ4ÞЕɤĴ˯;ΉӧŅĳcӒ;Ƶ',
                    'description': 'ȀɝYˆ˲șŒʰιưʩԅџMώԦȝȓɱͽј˗Ӓƥ\x9cѫȧìǴː',
                    'value': 'zVϕǡɶƪÁԨͽəFԠ~ŖƟƼІXєӶĮǹiҖýƖDҾɷΤ',
                },
                {
                    'key': 'Ė:ҭŪXБўŀȫ/ˤК,ŲȵѿÒɻѡїÌͻƸĒǖȬɗϦʠά',
                    'description': 'ϮћI\x87ζ˱ҼɜύAѶ\x7fơӔσͱǫǐ˵æ˱ȵɽ΅йö¾Ɵʎʬ',
                    'value': 'a4ȲƁǗǔȟіϹӌΤɞό¦ǌԋάßϓҞôî\x86\x8aǍʫˀȯɌ{',
                },
                {
                    'key': '҆+Ț°ļłƷȀƵŖСɺѿô\x90ЖǭԦȦȃҸȁȄƚSӐғÕҨ£',
                    'description': 'ˋожʱ\x92ԠŋӧɏğįяșҞ¸чŠЗǑɖDǳǳƉEͽдǲɋϥ',
                    'value': 'λϽýͳҰэǛʹЋiɈ]Ξǟ',
                },
                {
                    'key': '\x94ȆЩýӡ˕ˈȭԂр',
                    'description': 'Ȥҭɣɘʭ8ʂԍӊ\x97ϒǶМҷɊɘɱħЌѦǭϠеΊхɩǅƪӏԕ',
                    'value': '²DŁЩɏҒƹЃѩƠÞV\u0383ψҹˈЍѣƪӛƥɎϓ\u038dӁѧ2ȪƢĦ',
                },
                {
                    'key': 'ϟ˜яŞ˕΅ӡǰĪн«ƂѕԓäªƧ÷ҏœɲɃ˄ͼȇˠΟʮÏϼ',
                    'description': "ĽĬΥĒστɉԙū'ӫѷ҂Ϲïƛϔτhԋ\x92ǈƢ҃Ö҄ѭҝфų",
                    'value': 'ŒbҺǧҁˑӓ˱Δ<ŭˢǉǿvѢôɶѭƦȳŰċ˗ӭШƥѸϪɖ',
                },
                {
                    'key': '\x96ǘŋщŏíԨϸζʩє',
                    'description': 'ΙfґΙԝͲÒɽ3ÑɲƾǗ\x86Φĸ\x90˶ʆˣžїǦҫĐвΕ¢Ǭʼ',
                    'value': 'Ю$цӮʸˢϬôϬӜŧŦĊǮČ)Γƀλγ˨e<ȾƻȗɞΐĭȪ',
                },
                {
                    'key': '\x91ӀвʴϥіˡтӒҚƖӗƼǣʇӵɛȵȏкҥľӿҏɥʏƨĂӈϠ',
                    'description': 'ȢæÒɮɭЫ\x81éк]\x9eєȐѳɃƢşƩÖЋΪЕΌͰɥʍǨʑ˥ƴ',
                    'value': '%¥υ3¸ȎќЎхÓ\x99ϴäĺđȿ"ĳҥ7ҲȀX\x9e«\x8bήЪбè',
                },
                {
                    'key': 'αϢĊKɖ˂ΏɢΡĎдҟĭƌ\x88Oӓб҇ƾύњЎԠƊ',
                    'description': 'VЉγѩɈ˵ɵ!ϟʄˆѹƮǸɞӏƶ<ԇȱж҇ǇϢЅɐћ˦ӷϹ',
                    'value': 'pāгƴʐѓ¾ǏѐϾгʮŔƔȐɤѥФǍˇ҆\x97cÞˠϓ\x7f\u0383ɉĩ',
                },
                {
                    'key': 'ƙСΡ˴ÓƄǚԒ.\x94ƛ',
                    'description': 'ʭѤǢɓȹʜԌќѷ;ӯǜιÃΗȘѽрТͲ\u0380ԌƖτЄ˶ÍҮɏɬ',
                    'value': '{ƐƙɀΡ\u0378З҈˽ҬĽƭԆǳʴԛӷȴŴъɂά΅҈ϩӞӝҾăʤ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 4529,

            'location': {
                'x': 1587873478360882036,
                'y': -2967176921833765282,
                'width': -2622088206822023804,
                'height': -2276987875364938466,
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
                'active': False,
                'focus': 1362,
                'parent_id': 'ǐÁɆҭ®ѰÌΔȿϻŻƼŽКӁƅήțGγΆ8ƬȉХƐȎƿҰƸ',
                'location': {
                    'x': 4468047319618581347,
                    'y': -6638667376297066818,
                    'width': 6223836452659257965,
                    'height': -4147078382984979535,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'ИÓϒƔƒdΦſɥȲԮώˍĜƔɬӌʹЗ˟ĠþŇƲãǛόЩØT',
                            'description': 'κβ¸МϠOҕҟ\u038dÆ?ЂХĀвЯɉҟӪǆŝԮθ³Ǭ˴ť\u03a2ϘӞ',
                            'value': 'ϰ5ƶˣĸλ\u0380ƶʷȴ*',
                        },
                    {
                            'key': 'ɀĐ˙',
                            'description': '²q˥ӝǧǏ·\x90Ǔ˟ԡŇʽ¹ĤǛDʱʶǂԪňP\u03a2ţӱuĄʒЀ',
                            'value': 'ǵƐѿЈԔƷʪƶʭɤԦµˣƔϱЧ҈ʬʧȝҐԩǜѧɡґ',
                        },
                    {
                            'key': 'ѬˢǯωҼԨŒýҚyӸħхЈk҄i\x9fҥʘʐ\u0378ʋʺԉş\x8eȣӣȋ',
                            'description': 'р҇ϟ\u03a2īϤĖŪɶɮѝƏˡǲ\u0380ʷɹѯ\x8aȁɐŶӾHҡӦʧΕϴӘ',
                            'value': '-ɄΞ·FŁtԞȅ\xa0ҢɡɜʝĦZѡȭǙʗrо!ǁыƇŽϬțƫ',
                        },
                    {
                            'key': 'ӪʔĸсһӬ˗јаҿʫʥ\x85ӧ>ΪƂ҅р¦ԉԄƻJҁĻԗ¦ņȧ',
                            'description': 'ȥА-˩ҙƿʇ˗ɱ¨˥ɒįäνüŒĩČІȺϞ˪ɸɅºȌӯǆΗ',
                            'value': 'ØŜë҅ԒЄ\x94ŕňȎȜȓȇǪ1Ĩ÷ԁΑ\x95ӳӦѾмŪv΄JΎ{',
                        },
                    {
                            'key': 'άц˭;£пҳRΛƓĴŀһʎąЯԈ',
                            'description': 'ɹȊϹѴ˹ǿ˻ǅϻƚɋj˗ң#š,҄oÛҮǭʜ\u03a2ʚƍʿěĉЍ',
                            'value': 'ώh˴ұљjØČÞȴ˟QѱѰϪȝŨλhǲƔЬ)ʈԍâʲʘǳԪ',
                        },
                    {
                            'key': '˓¿ˊƩ˔ƻƨҁӐ',
                            'description': 'ʨϘԧċǾʌȣƫĈϻ\x99ϮϴƪƗßÊ~¬ÎΎ\x95ΗԨ˒ТӢúòϡ',
                            'value': 'ȃƛSMģũ:ˤ\x89ƆƂԀȷʕʟǛĎːΎ+ƟȖÌŢӃȧ˥ŕѓȇ',
                        },
                    {
                            'key': 'ɏȤɖεԟҶΓѺѢǣԧ-.ƘǵƷѥщʽάѨÐŦHͺÒǐŉ#˲',
                            'description': '\x8dІμəϬӬáDǸƀρηΊͱȃӧή³ґ\x7fM¶ўίӆʂҫԝƏҮ',
                            'value': 'ѾŖЌҬƍʘĺǞϞԂԭùӼˤώϤΟƳLϠƆȾfӃƪɹ¹)ʊɊ',
                        },
                    {
                            'key': 'ǊѝǩǞġ\u0380ɹƭѪ\u0381ɀˀϻғĆ˘>ғȓȩѤғɅːɘNˇĎĨV',
                            'description': 'ȋъщеɔӦ˼ƐҬэϤԟʾӘʠӧѝŮӟ¤ϥķ˵żұ˩ʇΫʢs',
                            'value': 'Ƅnȗ²ҸԖŮǂƩ\u0382īĳÑйαʹш҆Ѿ@ΑҳVҽ`ԝJɁʑ˖',
                        },
                    {
                            'key': 'QĊŻȆƚԟǃļé',
                            'description': 'Ǣʅɲ˻ҏʇǚЖù϶ӏȚЩˍʾƜЖĔʿʮǁЗũɟĨ\x87ǘǙəǸ',
                            'value': 'ƚӨǪВцҨӫÔҮΙșӌиų¬ƘřӓǸϰʻҋƂɓȃŁZŇӞň',
                        },
                    {
                            'key': 'ȎôļŃūűύ',
                            'description': 'Ҿǧ˗Ηĉǃ.ЍϵŁуɭҠΤӿǆĴ҅șӋÝYǋœλ3ǠùÆ[',
                            'value': 'ǯЁζʂӓɳϾӫǖ@ʹцҽǓΫˑƔñɺ˽ňͳİełϐœɴΤϣ',
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
                'focus': 9884,
                'location': {
                    'x': 1194545647175269799,
                    'y': 375325569234192068,
                    'width': -3891671316082060453,
                    'height': -6535381113902602560,
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
            'reason': 'ιʖ˸Ѱù϶ȆɸłϵŻʁɡĻäZȁ҅ıέːű',
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
            'keyboard_focus': 8075,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 1535,

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
            'window_id': '҃ǥƵȺÂуԝΔőßʡĬŰ£ӷԫ\x8e]ҦϪɵĳӲҴ÷εСдʾ˜',
            'location': {
                'x': 1326595196966519002,
                'y': 4147517852819701823,
                'width': -3301038686279577011,
                'height': -3286592233843198088,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'еӻǞùK',

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
                    'window_id': 'ςǬęѬоĐи˼ͳ˨˨Ӡү\u0383ҒBΚ¥Ҥf\u038džɏ\x95ӫԩÊ\x89ͻî',
                    'location': {
                            'x': 6014288821530020526,
                            'y': 9002625267251743623,
                            'width': 7536578340136218139,
                            'height': -7867393966658480122,
                        },
                },
                {
                    'window_id': 'γŢρӘˮѻʾǭϜRʲʿoӢŃƀʁ%ԀϲźƆſǛНʢͽǽöĔ',
                    'location': {
                            'x': 5231394274390663227,
                            'y': 8194288548547376147,
                            'width': -6242213207571728851,
                            'height': -1408492974592442765,
                        },
                },
                {
                    'window_id': 'fûʖӜӂǢƛӪ҅Зç˹әßϵƌȉ~ÏĦĭĀԠΡ\x88Ϻĝƾm҆',
                    'location': {
                            'x': -7843743986993094924,
                            'y': 6033091712763583114,
                            'width': 5963630568194680708,
                            'height': 1391295236982059987,
                        },
                },
                {
                    'window_id': "ѡșƔϧʿ\x85҆˷ҧhөӫµҡԓȿψҽȑзıʚҖɞʢӇѕ'ʃƙ",
                    'location': {
                            'x': -1698225199215396929,
                            'y': 5291134889064201606,
                            'width': 1777361686113844796,
                            'height': 2446668057737404718,
                        },
                },
                {
                    'window_id': 'ӁЮϒхȴӞӍjɀӓ*ΈØɒӝƯӑȜǇɞZʝҴυÖưЧĞŐӱ',
                    'location': {
                            'x': 8002688861922236617,
                            'y': 8699701721238349036,
                            'width': 12095786887343997,
                            'height': -8179753778731414001,
                        },
                },
                {
                    'window_id': 'ǋƩͽЃʊxя\x91ѓƄԑ\x9eCѠВƋȮà\x8b˙κǹσƁӪʩÛǵì\x97',
                    'location': {
                            'x': -1460449464837693962,
                            'y': 3733326622411927048,
                            'width': 8588641929273565267,
                            'height': -1957543143141409158,
                        },
                },
                {
                    'window_id': 'ǥ1ʆ"ðҤԟʷȖοɮAʯԖѣʠˏèǕα˙ʸ\x8eƐ¿˘Ǹ=ʀƖ',
                    'location': {
                            'x': -5895934891653638337,
                            'y': -3922826576094721722,
                            'width': -6965555323924526323,
                            'height': 3127475452917528023,
                        },
                },
                {
                    'window_id': '>āâϕʋÝȉIԜ]ˠӽԂӮľСlӑԛɤХåԜҞ˺Ȑ\x98ʶɱӽ',
                    'location': {
                            'x': -6259744953419811254,
                            'y': 5266541280465470275,
                            'width': 4775300892310665837,
                            'height': 4494420461105055291,
                        },
                },
                {
                    'window_id': '˙ЛϨɢŃӟҟŃιFƴАр\x87ԧҹɍϬёƋ\x88»Ӣ®śϯtԇд«',
                    'location': {
                            'x': 4631452335916651803,
                            'y': -6687351579270624549,
                            'width': 1225833754049687014,
                            'height': -1829587102140867925,
                        },
                },
                {
                    'window_id': 'ʢӸ˝ƹƏ˝ΕЦ¿ÉŎЂЊБāˏШÈɔӴ',
                    'location': {
                            'x': 6657157615324330751,
                            'y': -5865459624066184880,
                            'width': -6290961854989483691,
                            'height': 8840776962589382928,
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
                    'window_id': '7ğϮŇɶ',
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
                    'key': '҇Íȩ³ԂǗиȴҨʅÔĴ\x80əȄΞΝϞΠӌϲÉÅνӂ',
                    'description': 'žбʃүҲȖɗШЁӃӐςϟΫŐȇө\x8bфǂtɣžћ³ωΔΫ˰˾',
                    'value': 'δVŅÐCЍŰҖҔʤŧÜΥҝӵӰёҧǤʴƯӫ9αϷǯԛMм\\',
                },
                {
                    'key': 'ʒʡɴԘҔʹԀňȧШȪ˛ӀҰӈƱìĮ²ӑ',
                    'description': 'ίƛßȤåηѦғˏƌ˪Ċ;ΪͰǉȀђ¼͵҇ĂĦɄҏʙȿЉϐʠ',
                    'value': 'ѠŠˬûΥŃƌБŽəÈϟӚ˰ϭüÑȌĴȚ΅ȯɎ@ɺŝҧ˱Ϫғ',
                },
                {
                    'key': 'ԞȤӎήƿӋǨğūˌȯԞҮɔʣʤĞε·ӠέЊԉǯVԑȥП˺Ȋ',
                    'description': 'ɤ¹Ɔ|\x9eыX\x9dĪΧĩƿҚаȂүÄώőǑǉɜѦ҈ӆЪ?Ҍң\u0381',
                    'value': 'Ĕ\x8aԓdѾɨɉśɗɜѳ³ЮǍЋZǢӨtŷʮʒӣӗșòͼɢǇŁ',
                },
                {
                    'key': 'ӸʀƢ\u0382ˬҩӷłχ^һʠѴԮ\u0380ďǖϜҡ',
                    'description': 'ԗƐǑ҆ӝҾҿǻŹȡ×ӎ\x84ɽԕҙ˄˚ʉҵ}ăӓŧϹϘ¡¿ɰˀ',
                    'value': 'UюƧɻΌωǵØˌ\u038bŽϢѮ\x8fЇƦ˺rɎѴƜԁáάɋЩȃҴƦӏ',
                },
                {
                    'key': 'ýԡfĜқá*ԘѧsƯѯϧ!ʰѸ',
                    'description': 'ɸņíĵǉſĥȈҍ\u0379ѷӒ\u0378ԛƫµ¬"\x94Ўѵ¹¯зªщʯ˥Ԅʍ',
                    'value': 'ӮǢςƥƃ§-ĝҎʢхŞӐ˷ǊŪ^ǖɉ\x9cʊǏѰϺԤ(;ѻĄ',
                },
                {
                    'key': 'ЀйԕΣä˦χ\x8aǴGǨśĥҵӇҢȿ£Ҟ~ƆĄcOɣŔb:˱Ǧ',
                    'description': 'Ĳӊ˘Ɏ2Ѧ¬ԛǝˁϯȗԇƇĴʠÈɀɛ˱ˬȟІȥϪ:Ď|Ϝπ',
                    'value': 'ͷļҳżƻƯ¤Ușԓϫȥ˧\x94ȔӭΚƒ˕ɲĲϴǬ×ҊģŁɊPԅ',
                },
                {
                    'key': 'ŉ-κƟǊгǖΉҾîÆͷʥêǏē\xa0ȩRĺɵÏЌŝɗԉԥȪɂɦ',
                    'description': '\xa0ȸóíþˋˣԪȈÑÂǵЭӝаԡǟһԑӌѻЏɑʩŤӮїѓԉƪ',
                    'value': 'ɛǫͿҎOǭ˂ѓȮƗËΘǂϰһǛĖʍҢ¿ИʞȚӷĘˉ·Ȣɑ½',
                },
                {
                    'key': 'ò˒´ΨĔΆùѵҥǎ1äŎɕ҃\u0382âr;ήѺŶɮӼӅĬ',
                    'description': 'ҖӜǳðѥĿ҂ΕəάϕǆëĕʦŶϸǩӳѴʐQĳϰп҉ώϰʩҙ',
                    'value': 'Ͽѻτ×ӗòǆԓёλɶǈȓѻӨ"ҚѢϣңɔмƇĉ÷ʗŦΏ\x8c\x9d',
                },
                {
                    'key': 'ҫJȠ˰рХ',
                    'description': ">μ,ʨğʈˊȯδ$ʜҔʗԀƴʄԈЧɁʳ³ӣӯǳƈ'ΔϬ\x9a)",
                    'value': "[\x9bȘɵ'ҵŝƾќĩŰ˝īºǜāӚϋϠǳρʹ˹Ǯɴ˜ǴҔǵʯ",
                },
                {
                    'key': '¨хɊ˜οiКǭƺ˗ǒLǼľФϜ\x8fԂɕǣ)ӇǉĶĂȝӮĖǇӺ',
                    'description': 'ŹsŦ>ұѽҪƞс¡Ȍ\x93˞RǝρԡЙѪɧҴƛώk\u03a2',
                    'value': 'ʑӶÂπЊÒСʗȽǋʪĬķQʇÖЙʇЭ˘ǰӢͳʏωѧɛoԪϠ',
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
            'focus': 6733,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 6260,

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
                    'key': 'Ī˕<œОƠøОүΠ˚ͽF=ƊŹɳȕ΅ѝБëȥƕTľѷпЩԆ',
                    'description': 'ʕű!ɣŃǤPȕȂӳƃԧ˃ҶƃƔÆԅɰʵҮʠI\x94ŀö˖ҡ/ʄ',
                    'value': 'iҹ',
                },
                {
                    'key': 'ӮуԆČÞЫŰBϡǬΧȂҼ«ã˽˩ɎÓˇǳďʋǦɥЩƯϓæϸ',
                    'description': 'ҏɣ˚ѳzʻˮɿūӹѧҁЯǩΒӄЦʧƑԥ\x9cĢʦϳȄδÖãʂø',
                    'value': 'ϢƞѣƤӖɪҶŁƃӎJЃMԃјƭϗњԮӎ¦ȍ%ɿтɠԄоӀʅ',
                },
                {
                    'key': "ΔΎ\xa0ƵŨóϫʔ\x9c˫\x9eȶͶëØǟ˸Ѻ'ӐʃΓƹѓӐ}ȬͰ\x99ѕ",
                    'description': 'ÉΎ\x96˰ʒĪʫиàҧĺȔϤɋϨ¾ѢԛԆkЎĜ˗ԕϒˊӫɢřˢ',
                    'value': 'ΟŽƌїÌ½¢Ôȕԃ(ВɓʶбιĈÀЂȢ~Ԑ˼kҖȴ\u0379ƪǅˏ',
                },
                {
                    'key': '˃ʶǋKɫӞΔɲϟȨɀРʌŖĭɽɾÂ,ѡ˶:',
                    'description': 'ðĢΖİϬəЏѹʵHÅ˻TΨɺÎɮɭӌŲMϘψǗϠï]ϝгϲ',
                    'value': 'ƛͽʒǨǂҜèɟԅІͻԛƞҪʠʴʙȽÀTҠӲ¹\x94ϛфϔćǄȠ',
                },
                {
                    'key': 'ʮǵĳʺф˼ɦұӛ\x9fȃǥӻƦԡŔ¥ϩҪе',
                    'description': 'ÆúśʉŹӡʉчˎĐˁѲϐ˞Ӣ2ΰЎͽÑĦȀ3Ҽ˶ѹәğǿӓ',
                    'value': 'ʰûƨԪԐƕʤǍʺɯÅоіϼӋÁ˼ȠØŀȹЌҲ\u0381үǠӈɖʨ\x8d',
                },
                {
                    'key': '˲ƾҚʜ',
                    'description': '˻\\ӭƅ¾ȕ\x8a҉ǭϮǶȬНŕΣІéėϢъҝĔ˵Ѐ˭,ǐлȊҚ',
                    'value': 'ӭłąΐ˖ќȨɵͻʬ\x91\u0382ǒΠӖѠмBωϞƑǙΞǐqSŲӗ˾҆',
                },
                {
                    'key': 'ÑԏҥӋǬˣ˱tиVˍyԧɌԁƱÛǹĲ˖ʖƽ',
                    'description': 'ȩ΄sȎƀǎʔЭӯʏѝοфΧɍѤʩӤÛ\x97ǷΖЀ·ӪШ˶ΡȒҗ',
                    'value': 'Ýʐǈƛ³Ɣɦ ǰщʕLȇ5ȠĥĀӦџяͳΟϕùͷρӡɟʜґ',
                },
                {
                    'key': 'ϡȺҔËҙƣ·дšҔ5ԚΣ»ΘΥѶʼҎƮЈ¯ȣƅVɯǻ',
                    'description': "KĵΧɚΑʙџɠÿʸѥҬйĞ'ɣǂӘΈXǬӀӿōКƵ˘ϘЧø",
                    'value': 'ӻӕÌιsоЌЈЯϩǋ',
                },
                {
                    'key': 'ÂˣěҴӯȎȦΟ+\u03a2БϴӜұӁʡҝҒvӊŮMԍϬu',
                    'description': 'ΘƩϘƁϡʜŜΖԮ*иzЛ˵ΡȀƎí˲Ĳ\x84ŠԀЧԨ¶ɖɶǓƒ',
                    'value': 'Ŏ×øſÈśʔˁȶѰǓɽ·ԃď¨ұǈӉĠӆ¨э?őĊɏʭ©«',
                },
                {
                    'key': 'žȅǾ˅ÊΗǱȥțȠſͿҋҏ\u0380΄ĿџɟǵĨ\x88ъɒſϴȔıϻм',
                    'description': 'ϜҺȐЧӲИʖÂΞ\x84)*ŇлˤǯčԔŧ҃ǢsǆΡһʹʺJ\x84¤',
                    'value': 'ɦƛƴËԡҖёȉŧ_υˉȎǍІȭȺȑͶώ·ƖĤ«ŮЂίҌ˸ғ',
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
            'window_id': 'ƁӏϿ»ŴΙĞȅϏҫ\x88\x80ʁ.ɲŜůхǢVĹѰΥ˙Ą;Ì"iʴ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ԌϾѯgӁ',

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
                    'window_id': '¸ҫ¦Ë\x83ŀ\u038b´ȕÌӀMѯî¼ȇԃԊԞóϊЙɁɍŗǚЃŢӞŐ',
                },
                {
                    'window_id': '˅ǛǒʮŎƊΤЧˋөŚȿͶϕŷ5эǍ-LҹEɐƺƪÃȝЯ±Ĉ',
                },
                {
                    'window_id': 'ř]ªdжqƢНɛȚхϏĎȅį\u0383ʈȲύƽτȗɿҾΐ¨ю£χÙ',
                },
                {
                    'window_id': 'ƍĔδ˷\u0379ԛşв˔RœжƝҸȁˆЇϩњƻŻûțÍ˭ӢͱɁ+Ҽ',
                },
                {
                    'window_id': 'ťČȦӞ҃ʾҵŘϜȍΗȈʶȪʆǞΔŪǚ$ʃčӦ[ǈĈřχˍϏ',
                },
                {
                    'window_id': 'Ϟ˹ĀѯüÍM+ѦѠҞɣґŅўă˪Жʦǫ˧\x95ԣkƹď˵ʫϘԙ',
                },
                {
                    'window_id': 'ҫжɫϝˆƥŷLҳҌӊΟǳԒѼɇɇ;ëò\x93ЈӫƶĲЪĿамǊ',
                },
                {
                    'window_id': 'џԛ˒Ľ˱ĪӮ!\xa0ɷɨˋTΆgөĨԬԡΘǺϦƗŜƦɇĸÍ˼ѩ',
                },
                {
                    'window_id': 'Ϸ˻эөʅưdΗƞҦźȕǍű¡$ҴŽÿʌɷȣ/ȳԫ+ә˩ϊĔ',
                },
                {
                    'window_id': 'āšǄ\x8dġȒ-ʯĚӻɰϫЉǏϤΐ\u0378 ɹԮ%hƃϚēʹԚѭ\u038bʈ',
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
                'ɫЭ\u038dвȁǏӫЖ҇ӎӞΚǅЛłê\x7fіҤϢћéĝʓҮ±ȑŎěɮ',
                "Ə҂í\u038bʩĩ'\x7fÅŵǗȟȨЁΓ\x84ɍǬȏϵĳ<пΩЅѥИđǒ҇",
                'Ҍąɏøɽ\u038b´ΤħʅȚқȇģзÑТÙԁҗЧΖѻ¼ԞνУ\x8bəҶ',
                'óő˸ǻҠZïėȸʨaϩҊȖѸųӂʗś҅ȞȍϙԌÛʣӠäџԜ',
                'Ӌ/\x86įԌϝΈЪĎǊͻƅ+äϚXɄѧ¿$Ж¼ÉĨŲԚѩԟȔŏ',
                'ǋ҃-Όνɛ˧ʒγxяĲΛȁȜɰӁʺǵɯʥέ°ųòž\u0378s£ш',
                'Ӓů˟ǇЭƼ\x98ƩţɞӤȻŀɭˡҿӇБĝǛѵVʃѧԦƹɤωɎǢ',
                'ϗȤȭĸ\xadԌù¡ǔĽάÐӄkϲлɱǱʴË»ĲҪҕêϿɪõ˲Ӯ',
                'ӯȒɤħЧŗǩƙȭϜӼßϵǃĎԩӾІÚˊыЇ˺ѽǴǿԗǩУɈ',
                'ƺɥϙѣ\x92¬ĺЭřŖÔŶ\x82ʳυЁ5҈ҀƮďӀųÕԈԩѢЊόΣ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ƆԙǻĦɌ',
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
                'focus': 2076,
                'parent_id': 'ѥÕηӤќ\x97ĸ\x9bŧê˩\x87ˤɪɍӌͻԩԡԅēȐɬùľų\x91ÃɬЙ',
                'location': {
                    'x': 2493620159476019623,
                    'y': -2717043871509147557,
                    'width': 8925483194201696947,
                    'height': -16562198779890912,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'åŐі>\x88ӬӼƣ˖ɲȊǏº\u038dĪҧCɂɋНòЎƦҷęƊȹȝºő',
                            'description': 'ȭԪˎǬҢҔԡ˫ƽʭ˱ĸӧ҈˼ӊϵѿҋΨԋӨǘƂɷЂЁɴ!˼',
                            'value': 'ǦҡϢΨɉԜ®ŢμЩˁѳʜƕӲνɉ˳Ϯӽŏ\x9eqԅЭφƌсҲԑ',
                        },
                    {
                            'key': '˜',
                            'description': 'eӑ^҃ǋӇЙƮgӼԁϟʃǐȊŠǡ˵ĄԙԖȺΰ_AũψǥςƉ',
                            'value': 'ΰјŷĕƉ\x8aɻȭʟ{ƅƇĞƕГAɼЀɣĳʳ\u0379ÏɸΤӴ˱үԈӬ',
                        },
                    {
                            'key': 'ξӷĖÌѬůΉǪʿҭҜζƒʪ±ȗɵЖ˓ɍѯĭǰϐʶΦŦΉǰǑ',
                            'description': 'ķӣǷǒǬɉРΔÑȒǫϧĀέēȖǢΡ[зȪѱʎ\x8dΘȜΚǀȑƢ',
                            'value': 'ƙνŧϳʨ·ƃǢŘJҳźƘϗЛWΘɨǜˌнҨľ\x93ǮӍ`ǮКӯ',
                        },
                    {
                            'key': '\x86ʊȈЯΞκ˥Ҡ˦ÜԫƎϱлҨǜШҰ',
                            'description': 'ȳɬʖǀsŃʉцƪХϣȿй\x99ƽұӓÍĴľԭуњËʄɸʫɼG¢',
                            'value': 'Sɗԉ\u03a2ћΆ\x8cƙ-ÌɤɆǇ\x92ǷdŢƭˬKǩєȠÏҝ˓ǏΥƘʷ',
                        },
                    {
                            'key': 'уɯóŶɷδ{´ůӱӱβIŠãŜԫ˪Ǆȹéʎ«ʹΜƬ;ʡԐҀ',
                            'description': 'ģʃǺ\x90-ˊЁ˸ыДĪíΚĐÊŨİŅɣӭȘԊϛɑáâʢȤǨǫ',
                            'value': 'ǻěůϡƞʧɽʸɯʀƖɻɐɹɎԈԘϮþǮɱδɣĽѦЀɗΠѼ?',
                        },
                    {
                            'key': 'έŗӋӘ\x95@ƧϐѺȅǪ\x7fң˔ӸƖǶ',
                            'description': 'ǎ\x96ƙҦԊԃǢŠκлɊǀΖӐĩɋ˟ų® ʥè\x8fĩŎ˺˳Ʌїч',
                            'value': 'şɘðÚ¹ĿФǞȕɑgԁπФӒ/ω\u0383ϲóƟԮӖ\x91ɥЇħ\x98ɐs',
                        },
                    {
                            'key': 'ĳӯŽǐÏΩīƱ³ƌϴĨдϘʢ°ѻNыɻʂǊˉ',
                            'description': 'ƗԋȢүäɠПN\x95âΓϱpӫɀԨŏƘ2åʍԅΦɑΪE\x8f\x8cӗ6',
                            'value': 'ȀдʘԧҕʵӠҢϐǖ',
                        },
                    {
                            'key': '3сŊsɗ\x89ŖˬȅȀƔ\x85нӃԂŝѼӵɑԂMŸҜěʦ\x98ѿĹӨ҂',
                            'description': '²ԦM[Ҕ\x85˶Ǔĕ2˼čǓīĹҷμϞ˄ŋ¦Ȫ\xadҀěŠ4ӣнĦ',
                            'value': 'ŷĉéȈҏBŻEoƺӗ˃ȺћîĜɾҶӰʚΤȼɩԇǌľӌТԌѮ',
                        },
                    {
                            'key': 'źӰèӑĕɎĀöҿĎԠȲʇƁѬÈìȗİѿÕ,ҍËƼɳϮҚχĥ',
                            'description': '8¨¶έҞͰ¹ɂɿ¬ˣҩ.іƷʦӮjʐœԕȻԙңԃԢԒθеÚ',
                            'value': 'ĂʯДKķǄ\x80Ǳʕ¦ɋȏʺˌΐАΠөʭԭФË;ўśa)з\x94ƛ',
                        },
                    {
                            'key': 'ЪΰĈԞƠЖɘCρчJϡȶȒεҥѲ\x87ƏǲşŖ',
                            'description': 'ěɬ\x89КȵȒˠҋ)eĸcÒǙʗѰˇ\x89˴ө˼ɲɇЦӑлӥ_\x93ʐ',
                            'value': '˵ĻЈӝ¨ͿƼȋ',
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
                'focus': 959,
                'location': {
                    'x': -3065329569015653142,
                    'y': 1915762023730020814,
                    'width': 6125698062596405254,
                    'height': 3419550720442285355,
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
                    'key': '˫ǳӐLȾϽ',
                    'description': 'ɛͷ\u0383ϗ\x8e˅ШȨˋîҴөrlѱΉŪҧκûҩ˕ȋĕԫ\x7fnʙӇЉ',
                    'value': 'ŉȧƦҤȯγƧɍʀ¼\x85ŒǫгJҽԒϸȍɬҦ\x87İ',
                },
                {
                    'key': 'ȰʩĎΌԁ»ψҍǄӷύʊјƘɝɑӁ˺Ԫӄ:ơťɣșξȽԗǹŮ',
                    'description': 'ÏǵǮɢİĔǵέA˾Ϲş×ŘVʖŏØƭfǞ\x89ώʵËʚѹӷԞҢ',
                    'value': 'iҥÂ\u038b,Ѱ˨«?Ҟ>ɻαЗ\u038bŁƎ\x80ԑɣʕӞЧƐζԛɘϘӬö',
                },
                {
                    'key': 'ȟƚѤί5ŅˮÃ;¯ˬЌǱˁȎϜt˭ƈ˫Ӵ:˞ʵҾƏҝ\x84ΜВ',
                    'description': 'Əťǐ˻ӌKԗ<ǻǱʭʾԥȕѠαǡԧŃϓ˘Ϫ˯>ʷϸ/ĝўӣ',
                    'value': 'ӎ¦ОøòͷxӟɾѼӦţҷϧŢςêы\x80ӏªǔЌɬʛͺYɢɀϊ',
                },
                {
                    'key': 'ϓįő\x90ӊͲˍȊҿɍ˘^ԓ%ƧȆ\u0381',
                    'description': 'ӓƙӵąόșΠҘμ·ΊԨĝˊʾ°ƂщǝѐʳŗďÓԜƧ\x8cƢК˲',
                    'value': 'ҕȿȤşćӳΏԂΞψǁǔ¶ћ˛ԥë\x9dɣŵԂȞŠʕͻƼČϵŊΕ',
                },
                {
                    'key': 'Ѡƪ¢\x8cЎ´Ѿ',
                    'description': 'ѹҭ˚RυˡϳǠĻцЏJĒʹҰӮɬˌǧˏ\x8cKӽŏ\x85ǓιӱѱƑ',
                    'value': '˄\x89ƟɔƎЅčʂ˔ƬӵƳʆρʵfԇҶǇ˼ȋǯԆԭӱ\x9aĥƷȼμ',
                },
                {
                    'key': 'Ľĝľ\x86',
                    'description': "ȟƷ¢˝ӁȑȌ'ȓÒ˘˱ͶǇÊ҄¦ŭɀӯѠƢōɐʉ˽ӽƵVY",
                    'value': 'ȧƳȑŲȵÂ*ӎʇĹӂǏʗїDҵɵӲӻГzʐàčѺόӲɶȉŌ',
                },
                {
                    'key': 'ӂõżЏŗ˃5ɮҷ˺āʿҞyʨ',
                    'description': 'ЬǐʓϓԤ\u038bԈ\u0380Ʋʢšӭзԙԙèйќҵδ\x7fʱ£ŧԈ˓ѱȠΐï',
                    'value': 'ɊƋŲ\x89ΎįȿÞǶϊЍƺĩ\x84оԣKņǁΓԫρ¨ΐ£ӡÌćȕҍ',
                },
                {
                    'key': 'ȮҮΔǐ˻\x93ςÇ\x95§ξϨǞӒҭóτŝĉVαӪɮʿɹĸɻԉ',
                    'description': 'ańμǀΤɪμʦќӰВΛҩǸŧȰĉ˹Ɗĥ\x92ʓɯИ˙ʁʼăɺɲ',
                    'value': '˱ÔоÊoѣś\u0383Ң\x93˥җәĴΈѰӳʌHı˚˄Ʃσƾ£z¬ɕɳ',
                },
                {
                    'key': 'ƧʣʝŽåĔЅ',
                    'description': 'ΐȫɣǝϛ\x9aΙ*ĮӕѶʰӼþыĴıȨϫɪǗúƿʉǓӟǡŀѓ)',
                    'value': 'ˮäωȑяОƏĸɓǇǨƅǍŁOѪыԏȳԓˊʝԇԘƙʮĳԫÝʃ',
                },
                {
                    'key': 'Ƽǅ ҢҊƟ',
                    'description': '҃ʭSɨæӰƭΡаȹŌēMΑІЮňɌШЃɻɼʯ¢Óǐ\x9eȚΜϬ',
                    'value': 'ӱȮ\u038dΆӡӕʹťӞӂǔˆВBȋϯѬѹʋшǬС Η˝γÿџĥė',
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
