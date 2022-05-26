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
            'x': 7828437841366812303,
            'y': -1120796753580398997,
            'width': 2522973796994957869,
            'height': -7426584325637418444,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 1691945722177897386,

            'y': -8840874982447111147,

            'width': 5993957433692407411,

            'height': -1608445032641765614,

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
            'key': 'ƤνϑӖӒʤ˘ΫʇϩɩцѢƭçΪӭӑ˲ŘͼĽŬ\x9f©\x9bѨ҉Ƞǽ',
            'description': 'Ĳѷ»əүȸΤɴѦԫʩӺӴȗIɃҞʀǿεӁlƈŅöЫҺFÆ¥',
            'value': '\x84ëȸƅũȟɞƖǇ\x83ЎèƵʤҒ\u0380˰ǉQĐúƦǜɯˊ҇ҴϵЉӚ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'È',

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
            'focus': 7190,
            'parent_id': 'Ԓ˻ӧǘѺӄϢӇ6ȭʔͼͳũϟďǲюƅ"Ϥ0ˡF҃&ˉΆәŮ',
            'location': {
                'x': 417476821834312308,
                'y': -5551361268463317343,
                'width': 4541524254907590877,
                'height': 9045272341644384333,
            },
            'minimized': False,
            'meta': [
                {
                    'key': 'ԅΆƈҼŌԈΟџҮөмκ½ɗԬˠøӢҤ҄άƿJϙſǕ',
                    'description': 'ˋCˆȗĉҚћеƈüΪĒί¤ΗțӥǼʣKëɨЫŪěϧŏӀʹÎ',
                    'value': 'ÿѪżĿlEѪƵĳІŻ\u038dŐɦ҈ϯU§ҋ¬ąӿԥȔēǴˤϞöȡ',
                },
                {
                    'key': 'ǄџƉԃʣ',
                    'description': 'НĐǤŶ7)ȘƥϨŻɤʪϤΩʌǌϯþԩѝŇ\x82*ÐζѮ˼ɕϟȉ',
                    'value': 'χƓıƗłÞɁӤшӆҮƎ¦ǩĄϡѨǜԮԛ\u038bѴĩ˒ξĊЖшŸP',
                },
                {
                    'key': 'Ì˖ǕΓ\x89Ϸ¿ÚһǤƢ\x7fԓ˒фʪϝʻæƠЛҗhčʋǘ\x85',
                    'description': 'ȏϴŸЅҁǅłѵğ϶˗˗ѐƼɭɡǤȋòcȅķΈĭɞŋȨöԉҊ',
                    'value': 'ìɯʜԫбʒƒΉΚϜġƥϒі˹щǠŷǒ\x91ÑƨəԘуњVĦTȎ',
                },
                {
                    'key': '˚ήƃǀƶΗķӦпʦϝ2ѥ±úş˛ƏІľƠǛȇjˁʗҔнċѩ',
                    'description': 'ϭŜƻĖЋέѹԛРĘƜˊàыΩІƽAԃȊҋƻɢϒõпсЄÒш',
                    'value': 'Ǯё˚Ҫǃǥ\u0383č¯әćғϬөʙįůǈˑŵYťӭΦ҃Ǌ˩ϭӓӪ',
                },
                {
                    'key': 'γyσʂʋԘЗϻɠɝʬЩь}ҟɱʫL_Ēā˒ωѪԉѵЁȡӐ',
                    'description': 'Ωʟ˳ľǹʝÞÏ\x86ѐϿʑʄʖƣӆɧɝ\x8eÈѡ4eơԉԌԫɫǳх',
                    'value': 'İαŠѩ½ìӷƝѠʥ˽Ҏɟđϲ\u0381ӶƵӣçɟšŠƂÚΏыфПд',
                },
                {
                    'key': 'ʨǻƙĴ śҁ˙öƎΝԥʖ6ȲԆõΆČ˫Ϥ¶ԖŬ±ԨѪίФЀ',
                    'description': 'ϻƃЀ˄ӚнрȂɌȵȣєІϟΖ.ȨΎkΜȢͷǕşʳʊƽfǙʋ',
                    'value': 'ƫɤ§@Ƶ҆ɕӱ˘Ԉɡǣɓ˜ƻΦǖʷōȦȄȖȥ\x93Г˴іԒѰÒ',
                },
                {
                    'key': 'ǓʲȜƝԘϧđӋҖΝǵ˷ǬŅǵӨʊƽˬѤƯӞʇ§Ƹ\x89ӤӀţѱ',
                    'description': 'ӱ6τ?ΏƹAƱƻěɋҢɞӅ©ӌÞŌƜƧ%ǢԡB΅åʬǻ·ƀ',
                    'value': 'ҿ5ʈǴмɚǚŔŔʃɋ¢АˀͷŀϓEӋ˾ЖːåȎ˫ͷ¢įÿ˻',
                },
                {
                    'key': 'éˁì\x85ŬҸӟ¶\x9bѴsŴīӲˁ˄ɤė\x83ЬɏӝнɃYӽКƿ|ż',
                    'description': 'ŷɨƃûН˟śȉ¼ÒǣЀϸǽEĥūǫƄнγԦǿԜ˶ńŧбǟŬ',
                    'value': 'ԔƛʕԒŃÇjӍȼˌԛ\x8cʣϽľӡф\u038bƧѦҔʨηkϣɕåȚɚø',
                },
                {
                    'key': 'λӖҖϱųСɓҶpŽӬāȘŲӑÿȪԡϱƳ',
                    'description': 'ˠǄԙˎ҇Ė\x8dҴǋϟĭƇĹКЁøȊKĥԇÃƜȂ˒жˮiМЦp',
                    'value': 'ӷýώ\x88ȣǌţƝ(ĦȱȈȇκӪ<ЃҊFRÄҤ\u03a2|ʡωÿȘ¼ǌ',
                },
                {
                    'key': 'ˎѲƮЕѠʍЭ˔ԚƦԇĄȁҗԫŬķҀʓʘˁЫľƉź¢ʱҜɶѿ',
                    'description': 'ʑĈфԈ˱ØďȊTԕȬҘ˗ІǼ!ÚȃˠҡʬԫæηǫӍϠΔқʠ',
                    'value': 'ԁ҉˂%υŭԅϬťβ¼Ѕϓ¨ҍɱԣнɰǎΫʄˈ˫xŅԖҼӘͽ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 5790,

            'location': {
                'x': 3470187769144063858,
                'y': 8701803200570286058,
                'width': -4513743692125757862,
                'height': 6855445172873167401,
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
                'focus': 6193,
                'parent_id': 'ЍүѦϻº\x8eѓʎȻиįϰĕЊǛǊсͺŻԉ˷ɣѝƃХӹŐſǬ2',
                'location': {
                    'x': -8581483796722058138,
                    'y': 2765160876561651607,
                    'width': -1106241899754732222,
                    'height': 2884054978438987951,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ĕÒѐЏŭJϠԬˎЎϰʎʑ˙¼ωƛЃǒOΏԡ\x91ɣ)íҡƴp\x9d',
                            'description': 'Хш˧ҢϚϴРŢшӋ\x92ŝɻӿŁŲΐºͻǦȮǤʑʫсϹϦɁɂӇ',
                            'value': 'jʍЃǰȟmź¨ʉʼGωя',
                        },
                    {
                            'key': 'ҠͱĕĚ˕PȜȞќԁаƌǅïМ',
                            'description': 'Ӊϔ<˫˖cΔƐĐ˺š\x96ȱ\x9a˙ˠőΧєζΜ¸ƩƲ϶ӜλҨƳć',
                            'value': 'ԝɬŀŕΨ˪Ͷǿˏȉ\x8bυд΄˭ȝʜþɹÈ\xa0ҎȤĒ˪Rg\x9cvѾ',
                        },
                    {
                            'key': 'ӧ\\/qӎзƎ',
                            'description': 'ӾƉƛ\x8fγԠҐШĲ˯ɺǽϥԗŅ·˻wґÅӾӅ˨ʼԦϵɵƀӴY',
                            'value': 'χ·Ҁ϶HȚҕá\x8aЏyǭϲξ)¹Ц!ΉЦȐżϖȧȡ`ȧϵʲе',
                        },
                    {
                            'key': 'ӆ¹ΦԢҝÊʱƞɁҖϝ\x88ǞƮǘÞ͵ʪ˂ɈҠĴϸПŒȲ˺Ϳşӿ',
                            'description': 'ѤƕҞÍӬӄπzʦϚΉƮ«йΑĿ£ŽǛķƞIȮ͵şъѫőԔά',
                            'value': 'ѭ˰ДɅɛ˱Ѕ˚ѣǂ˶˞Ә{ƞȂwą\x8fѼԂɂUӀʌβωͺ\x8dT',
                        },
                    {
                            'key': '\\ԇТΣҝo¼Ūă}Ϸ',
                            'description': 'ϢĞԉǠМƓͷћЋȳȺɎёͽȮéĉҠǦɎ\u03a2ǁФąǘ\x85ʧҩӢȏ',
                            'value': 'ƺȌȋˤѝˢʟɖϜНëˬϘҁѳɠȆʍӵӣȱѽSōŪʹРҰҕ¥',
                        },
                    {
                            'key': 'йɞɫќʅѝcԛ҃ΤʇªӄӇϳƬ\x8bѪġʵѵŷҤ˫§',
                            'description': 'ðӘӵÆχɐʂǼƖ˟ ȕȆҳƬԝƉφˁƫЖҳƌǰ&Ɏ˵Ĝԅɥ',
                            'value': "\x8cиɹӕʁĆȋЭԣǾβɭ'ӭË\xa0ΟȾ\u0378ȼ˼PâéΧˋҜđǌȦ",
                        },
                    {
                            'key': 'ЄԍɧƶҶˣΪ4ΨŸѴƥŀϬůΘѡ',
                            'description': 'ǃɑј\x8eùѠɜÀǰґ\u0382ͶȠåϞͷţĠƁхĩѡЍƑǑ%ȘѤɓδ',
                            'value': 'Ĕ˭ʑ·¸ÕĀϽӐΠŖѰ.цѪüҫɰƹ\xa0ӻę7ϠοӴÖ\u038dѾ\x9c',
                        },
                    {
                            'key': 'NϒιŴ',
                            'description': 'вҧϦʩгн¥ǔǟŊӒɆëȌƖӺʿƥß;ѬӃŁǢ˄§kŁƿΎ',
                            'value': 'ïR\x9cʆӢϜJЎÖϞɷ¢УϾ½ʲ˘хϣώʲϞΪǤϜ,ʨϏǓŢ',
                        },
                    {
                            'key': 'ɝƅϵЃȆϸµǝįČ>цЂɘɦѕԊƞԃͲʎϻÆ',
                            'description': '˒\x8dӪȰ˰ŨҀ{oõĞӂӄĴǺƌɜŲòҋċԋɟԥǶruɧĆĿ',
                            'value': 'ȣÁϩŔÊɫ\x9bѬЃԀэԂҵҋǦɄҐt·ĴʏɺǁͺŬлѲԪǄɔ',
                        },
                    {
                            'key': 'ЦҚáԒѾ҈γǛԋΒ˙ϼǧʾӹ±˧ϭǖº',
                            'description': '{´˥ӟfƟӈΧӀʸʹӦƱ҂ͽŃųʳz҄΅ƖʫǝŌÄıĐơҘ',
                            'value': "íϦԖƹӿĎˠ~ƂӢЭʄIҔȂʶcĞÔ¨χѧΐ'íȶȵѸĻʂ",
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
                'focus': 1941,
                'location': {
                    'x': -3597398538813550699,
                    'y': -3843895502541193236,
                    'width': 978906362830974417,
                    'height': -8522800712485197947,
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
            'reason': 'ϺԍЯċјͶƼ˵ɩȾŐɏыɺΧɖɄʳҁɋԗɢξĴ҈ѯGƍȀƽ',
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
            'keyboard_focus': 9552,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 8498,

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
            'window_id': 'OŞǷN^ɺȠ;ώ˯Ŷɂǎ˴ɎӒƶǿӄįϛϒҕЍɪǩɋӃ\x80ƣ',
            'location': {
                'x': 6995698621951731925,
                'y': 8191011628686832539,
                'width': 2803445421858002510,
                'height': 4191860883995254356,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ǧӒȳ҃õ',

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
                    'window_id': 'MØϺƋԭӱцǝōЀίԡ*eʱќƒǃɧħљÜҺ\x85˭˳ǤήЎŤ',
                    'location': {
                            'x': -963291541243283477,
                            'y': 7551141630740231872,
                            'width': 8437900018422901758,
                            'height': 435521776267534161,
                        },
                },
                {
                    'window_id': 'ԒУȀRäȁ\x80ķŇʭÆȦȨģǠЗҎľĔĲ˕Ӈ»ȂфʐԏƍӤǂ',
                    'location': {
                            'x': -5776991841496424438,
                            'y': -7093111419782466,
                            'width': 2492672869900864450,
                            'height': -7647182397517179758,
                        },
                },
                {
                    'window_id': 'Ǥ¸όÀęʲҦɱ]ҟЕť:ԨŢĸŐЏ\xa0ʨ\u0381λӂű\x86ѤRѬɤń',
                    'location': {
                            'x': 2999642089319782804,
                            'y': -1917148525723478347,
                            'width': -4589558457917290493,
                            'height': 4285725210359670355,
                        },
                },
                {
                    'window_id': '҂ØǟåнϥΪʝĝԝşªҞȹƏɦԋо^ÎΞҭȳЋѐĉжΌĸԏ',
                    'location': {
                            'x': -7198909670370525772,
                            'y': 2620497638133583941,
                            'width': -4732608793196089402,
                            'height': 4172428645417104836,
                        },
                },
                {
                    'window_id': 'ÝǔԉVC©»ɖЗƧԎӕėΌϒӂ¼Âß/ђƗǯҨĒԎǪҘҐӟ',
                    'location': {
                            'x': -2278586919326743389,
                            'y': 5392255815498211552,
                            'width': -6371451347447311125,
                            'height': -8004189397653418274,
                        },
                },
                {
                    'window_id': 'άфмδʭǐιɤäӮ˱ѿųļυӋѹԊǓӎȞWõѥʟ-иѠĸÈ',
                    'location': {
                            'x': 6011835059024374300,
                            'y': -6086451375367955773,
                            'width': 3795446381139534771,
                            'height': 3082222590914445998,
                        },
                },
                {
                    'window_id': 'ΥǕUÄ,ѳķęÕґ҉\u0378ƿӗʂʜ\x8aáсČĆ(ƕŻӣ\x9bҋϸʍM',
                    'location': {
                            'x': -8334753867501320160,
                            'y': -3547184816883091663,
                            'width': 6485817221948125873,
                            'height': -2867452797973507658,
                        },
                },
                {
                    'window_id': 'ΘAǨ1ǵϾ]ơʹ!áɛƁÎѾɨEбǹ\x9eÜҵƉ\x8aϰӲ,Ƚʣp',
                    'location': {
                            'x': -5944207325493944152,
                            'y': 907220557065241618,
                            'width': 8761398267226278994,
                            'height': 30103868585146723,
                        },
                },
                {
                    'window_id': 'şǵԫҤʝEΔϢТΰǄЄƴȚǱ\x90ʚӿȵμƀЪΏȒȌͲаȑȘҼ',
                    'location': {
                            'x': 9191824221538548134,
                            'y': -7864148657890803789,
                            'width': -6204673874172840612,
                            'height': 7342830460838247325,
                        },
                },
                {
                    'window_id': 'rˬͼПѿ϶ϝΜɵм˷Νҫ{ёȶӍԚĮӐƶEÞǥӲК<ԩҽċ',
                    'location': {
                            'x': -3475287084192403286,
                            'y': -7318978731611029120,
                            'width': 3186573171011832293,
                            'height': 1885100218570630788,
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
                    'window_id': 'ȦͶèԞļ',
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
                    'key': 'ěƴ˨ϰӥŀȠӞƨьіSǻЈËϦϲѾ\x96ȴĒ½ʮӌʱxL',
                    'description': 'ˋŠЀʞҫԑѶў¡GōƸ˒Ϸҧ[ӽӐĳӃҠˑČ0ͶҵºEǨi',
                    'value': 'ʀύҚΔѣťӇκΧʫÅíʗжˬΚĲӧǇɑϪӅħƝѭƓtīƢӢ',
                },
                {
                    'key': 'ƚ',
                    'description': 'пǮ¡Ӕҩ˅Ɣɞ·ƜғʙĻCǂÑźǅӷƳǣįфfӆɵǋҖ\x9eŉ',
                    'value': '#ʞԕлņSÌŢ\x81ԅ¾ǺͰϨҡѱˉ˸ŵȶêӥǑѰ҅ƭʅҥτŊ',
                },
                {
                    'key': 'ǢcЈɉзӱ',
                    'description': 'ϩŔаǍīŃ]ǁӆƄǔ˄ŃиωМƇɱĵ҂Ϳ¸TɫЏɻǘ4Ȓʱ',
                    'value': 'ăˤƪǈȄøj#ŀn˸ԞǆϥѥȟºŵʆЕфϬęǂ=ОҮ!ӷό',
                },
                {
                    'key': 'ϞӺʾΉеσǅ\x8cΔȔɁ\x9bϦcН0FǴÌӬʌјϒϴǹҕ',
                    'description': 'Æʸ9SˇЯƘȜϮ¶ʴʨςӶƙ҃àƦϦӳϛУʴğǟӶЃËðƫ',
                    'value': 'ɈȾáËŨ>ȬȍřгϺĥτnśҳϢá҆ɔǁZÞӠԛˎÛԤЌ·',
                },
                {
                    'key': 'FѴɩҕђԁĬΒʧEǽѪɭєeӋҶʍȦòȑɒԑˡĝ',
                    'description': 'ɣϹҪɶΌѳđΝ\x9bӕӖІūϣӇn\x90҆ѵƒѢ\xadĀkҎŬ\u038bͷɕê',
                    'value': 'ƜԞdӼˤΕҍ\u0381ʖҗӿ`ίҪ.˥·ŮόДϏԐĺʁʼŨԩѓѓһ',
                },
                {
                    'key': 'ӾɇƥÕʜșŲ\\Ċʫ˒¬ёųǐɟÄɀ˝ǵƭiʝˤϤ',
                    'description': 'ѣȫɏряɩʆdΦȻҠұîœРvԓȉ\xa0ϐŊԨҏȗʏӎ˂\x8bΦ',
                    'value': '\u03a2ѬөФƏɩɁɼĶҬĭãøåǴĀʜˣʕǓѰ\x9fƿӑԪ9ϷԐˋȔ',
                },
                {
                    'key': 'Ȟ²ŖΩˢҲ΅+άƍ"Έϟǡ\x7fӳˬЉd\x95\x93',
                    'description': 'ǃӥ\x89ţˢҹȒYƆǼˎȉǣĻԒƏѶΝÛcĭɔʕνЃӃuηƽE',
                    'value': 'цɠʱ\x91˨ɭƶȧT~ȕѐӟΤǸԫєɻ˫Ӎƅԥãɔºʽˢ\x7fƿú',
                },
                {
                    'key': 'ΟŐϤӻ˓ļɖͽθȝƢΉѐхχϋK¨Л',
                    'description': 'ĲĭλśЖʌɗϖō=ɽӣʕƄ÷ҏϴ˩ŉ8һѐКѺʨӽӁҥóˍ',
                    'value': 'ΘΗŔїϫəѐԋӆ˰ʕǛНÜҹǰʗjʌ4ʊƠȗ˸\u038bƖϹˢѳϜ',
                },
                {
                    'key': 'ǝŰ˭/ɽɍ¢ЈԘѣ\x9dƅǠ*ұӗƼǣ҃ʊ\x8e\x83ˏҏğӿíϓ,҈',
                    'description': 'μ+ñњϊĝЋСȱĉξ%ˆöǡѵʹЋŔҝȆɢŅƌʱkȬϬ1i',
                    'value': 'Фʌ˸ĒԠϷĮxˣ9ìŹЬңҫ҇íÎȟĀ\x95ȁǶӅӵԕǄȪϗϖ',
                },
                {
                    'key': 'ɈΪʔ%ŵјӨɪѻҒˡˁƆξϺȣЅɼʨĸpʸˉζ˼¨R˓ȭˀ',
                    'description': 'ːʈXƐ΄«ąã\x9dŖԌԂžвȅxЄѸѠʘEjȝCԃyσУκӵ',
                    'value': 'ϣπӤӖұƷȳÙϦѴĢȈĿ˥ƺȈ˾ȊԑäčнƔƧÝЉ҆Аҿҟ',
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
            'focus': 3517,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 6788,

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
                    'key': 'ǻǪƁӂаwÆɤĝɮ¾ӼǛĳƠǖλíϼрщќʪ ϛ¶Ȱ\u0378÷ê',
                    'description': 'ȫӎĶБԅɣīĎŻϗʏǍӸˌǱǻѸǚЬɱѦԟрĨϿԤ°ҊǰÕ',
                    'value': '˃ѷʾĳҪǢǎˑʕȫUŃñƁƈÃÅԨƃҼ\x9cԖ"ɉ˫ˆѫԆїʄ',
                },
                {
                    'key': 'ĚūűơNȾçҘÀǳѦҸ\x80ʻ˝ƾӗԎėëϪĜЁд˩Īʱ^ϋȊ',
                    'description': 'ʻȧѕŃΡ¼Чʿ\x8eäŲɵӘr\x94ӟ\x97Ӵԟȁɾ˷Ê˄ѶƛCõʁ\xa0',
                    'value': 'iįԊˆ˯ʇʦˢŹϊŦîoˊ\\ƆчÍЗÒľНƇˡ\x84µȯŹҰƥ',
                },
                {
                    'key': 'ǸѦҾ˸ЮΕ͵ƨӽʁӈŝĆӷϰЉǛʭϠϒ\x87f',
                    'description': 'ͳƈҭ!ǪϩʱтȈɘ|ǪХƟȝȣ1ƌԈşã\x92ɺ\x89łғ%šԣÏ',
                    'value': '-˹җЩđʢϒɧάӻқҞҚъɞʲόΙϼѩҫŠˣΘσĹ··Ģ÷',
                },
                {
                    'key': 'ǲŵěҋгͺѧ˲ι\xa0õº',
                    'description': "ēN?˒ύÉͺѠЩɒ×ɟƲ\x92ӿxԇ'ръ\x95°УѦĪƊĚѰƂȭ",
                    'value': 'ȼαцɯd˱Īʫ¡Ƴы\x7f˙ѫÍʷ5Ü\x82Ϣʰʞτȿ¼˭ȬǶƬӨ',
                },
                {
                    'key': 'ѿѨϘǣȧ˷ȃ˲ѡ҈mƼҥЍɃƉǆū҆ɥӺɆ',
                    'description': 'ï˨\x84ԑĭʗұј\x86ˊѦ\u038bȐЙͽɂʌедԛʑΐɅӅӃяȢȵɏĤ',
                    'value': 'ǍӪʉύĪǂύӏӒŮӒ҅Ǯɘ`iϯЂ\x9fǃЙȺȉȀ³ƞƩǹѡθ',
                },
                {
                    'key': 'ǏɝǤ°˶ОËϴѹȘ\x8dӉıɺɃѪ*\u038bˡϼúȚΙʌųԖɳє+ɞ',
                    'description': 'ĨŝѼʲxľυϴɒʱ\x97ШЗѻ~ϝɰùљƗԦȜѴӒÛįñΜÈ҃',
                    'value': '\x82НɅpʎ˹ƓĥϝȋӑϾѵԭΝȷïшƨ]ɞǰƷͰz¨ǥЪML',
                },
                {
                    'key': 'ǫ¿ѶϮ˷ӢУлҪƿŠĸʹǼθ\x9b\u038dѐĞк˧Ș0å',
                    'description': '˞ӑΩYѻӖĢԊҀЀԮ3ƎӳʚȪԔ\x9b\x92ԞѤǣϛʪΪҸˣȺҜÆ',
                    'value': 'ΈΪ\x91ζԌǬ\x8dʛʚ\\ӥɉϺɶҨǳƑҘйƛćʋ\u03a2ЃμƟөлЈλ',
                },
                {
                    'key': '҄6qΦƋԗ˨\x86Сʺĉ·ϔіü˖ůǢĮӖӎҫǔ˻ˏӷ\x99ҁȚǗ',
                    'description': 'ҠɺĝӒϛŕЛРϦƢŧӣ<ϼѼԞȖĖ˗ǏӺȢȡŴȩ\x99ǝUӆw',
                    'value': 'ƷαàŬӚƻʺэÈÛʹѬʖŚ5ŹϚħУǉȝʶҧ¬ѓȨ˞Ƣ§ŀ',
                },
                {
                    'key': '%ьЋВȪκΨϖTԡορ\x82бǫʆwЛ\x9dHɢЫʻӗ˪ԭ',
                    'description': 'ơНŪƒÒ²Şԛ͵ҰºȢǹĨѥ\x8f\x9eϹхˊȗƝϓԗɄī%ӊS4',
                    'value': 'ȕʜƫлШϚƦΛƧҞιδʬˬɔ˖ΦnђãřԭϽɧǙÞÊҰ˜ʊ',
                },
                {
                    'key': 'ìǘː˵ǣɸѠ\x8fϖƞ\u0381ҘӭņďțюОѢȓƿɫϵ',
                    'description': 'С˅ȳĭĒ˾\x80\x89ÜӁ)ˮԣΥĳȳОЯƬɞƇ£ȫϘͿǗʹзɘƪ',
                    'value': 'DѾҎˬҴқCζʘҚϺϕƥȗČ϶ƫ(ȁŞ^˓\x84ϸȜϔÏӝԦ°',
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
            'window_id': 'ǍχѸŀҧÒȽɐɠÛûɤ\xadʺ/ǃʌʜ4ĳүǳʵϡÜӒѮʃ҃ɮ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '\x8aϧϊơԫ',

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
                    'window_id': 'ν~Ѩ\x8dłªяΎͿ\u0378ƨҥ@ʚҽ7ϱıƧǳȥ˄ºφӍǧ³Ğ;М',
                },
                {
                    'window_id': 'ΛɭӡԤԄoͺƢƂ*ƿ«Ȩʳ9Ȗ҇ġѾʰÍĳÔ¦\u0378ñƷŅȹ˩',
                },
                {
                    'window_id': 'ϯȪȞΑ\u0380ΚӾƳˑjͺɺζāɪĽũȆЧ*ϱĉʺƹǂűǓӄϜ\x98',
                },
                {
                    'window_id': 'Ԋƫ϶ό\x9dΙҝ˗ŝƗǓÿȘŶӐϊɔҌĳғ\x98ʝϡϋ1éεԒ\u0381ʒ',
                },
                {
                    'window_id': '#ĔәȽϭѽ˕ǃѻ҂ĸ<˹ʩʜȿ\x8bȺɣƀɝŷƭ¦ŗЈ)ʙΐǘ',
                },
                {
                    'window_id': 'јҭЇ\x8eңϣҼŚƨ[ΑǡóGѫϟǳˑAԅt˒ȧĺñÉӰ ıȭ',
                },
                {
                    'window_id': 'ѱӲԪÝñԕďņɈțĆǯЏѝәʬ\x84ΖŋΑԫȎĲaԗǦÌИͱ²',
                },
                {
                    'window_id': 'ТʏĢf˛ȪҚ˒ǇϘиĤǵʖŐŝķÒĶ҂ʯʕʄńȴɍʚӥϨ˳',
                },
                {
                    'window_id': 'ǖ¸ʕϜŞ1¤҅ɳȓџĲ˪ΒțʨˇŰԈƓŝãǼόɻԋϳǖӂƪ',
                },
                {
                    'window_id': '\x8aUӳԍ˪ҥʢγΑɚˍğзǫΔӽМ˶ԨʾԟίʮϯƭåǒWҚͼ',
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
                '=ԎǵƦ2ĸɐϤҥԊɤΓϘ!cǛĺΑҙҶȀąŰ\\ɺϤǶѨѯĺ',
                'Nǡѷ\x8cƆŔĦƃ˱ȢхĮÙ˜©ƠŃʤ0їˏǔǔÒǈĮѥäƊÄ',
                'Ҧ΄ԟƲmȫ',
                'ӛϜɮԂ˔оáӇϛʧÃϱŎɠϯɝȬƦ\xadjάӠлĘ°èȏɩ˥ɺ',
                'ŏҔȡԫ÷ÁҽъɔӖˎŖΓǢƈƎƂǊ',
                'Έҷ϶Z\x91ȅӘĘǋĮȸʖ«sƃØ1ɨPŨʬҟœɺЄSýӨҕā',
                'ΏƵ¾ʡǍǙʌѵ!Ȥ7ǂÕѣԢǟƅ¥Ŝė˶ťЬˎǣѤǭ\x8aųӞ',
                'ϏɅϔŎĨοŴgſѧǭhʇђӾʟΥȤɭӹʰʁʶ¬ӽáɎҬК˨',
                'Ш\x84ӋӳŘϱʟȳȈʱӇЙԠГʨťĀʶ,ʟȀǆƙйҿĀŨӐȁ\x93',
                'ʆɬʗʟȘЀÄȴ^ԛȭӚ˻үήʿ˓ʩ^ȂɲĶԍ;ɳԨkŸĨλ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                '¶ŘҍʩĔ',
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
                'active': False,
                'focus': 3169,
                'parent_id': '?ǠʽˡνԧКȥʕқĺüˆϥʟ˗Ǟ#ӑoșoMЈˊΎΰΎѺį',
                'location': {
                    'x': 5474270109398570686,
                    'y': 2846103943363019914,
                    'width': 3595947621129386384,
                    'height': 2993177590096746837,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'мȚɢĮɝ˘µŇłāęŲʱѳĠG',
                            'description': 'áԖϕʱŤȏ˟ЍҝǍͲù\x96ЖɵϤΚҩӗʃŜΒŝг˛ӵɭƿҕʯ',
                            'value': 'ȒуЛӋΙǡƴȗӃȟɠ˪ВϯҤ\x8dҹǿȜӫГ·ϹǦˠǞӣӖҳŷ',
                        },
                    {
                            'key': 'ů',
                            'description': '˪ȮӉƛČ˭ˆ˹+ɨʳº˚ƪҾΕǉLčǘMѷΦȢǓǄиѿцǪ',
                            'value': '\u038b³®ʍƆ=ҍԛʑѕfӒǝȯӊÒʒ\x95ӒӢɖτø£ϺT˯5ǁO',
                        },
                    {
                            'key': '@\u038bѻԪĨǼĝϟāҟӘщҴƗȖѾξǡԌțÕĸҊаΊŕχ\x91˷ĝ',
                            'description': '+ɡµ¥˹ŤџŇĘƅͲЪʵԋˎȶʟģΈQƃȒƂϮί4ΨǹƺΊ',
                            'value': 'ȷɅ˾ŋ\u03a2¸ŢЯFϕʏZϱЕ˽υǠԡĕȷΊƵɅÇƒҲљÊϓ\x7f',
                        },
                    {
                            'key': '¸ϹyΎϸҧфп´ˣѓѝȵĠІЏϳŻƎ',
                            'description': '҂ªǠҼíΚξу{ͳwlɹъƑΉԭԤҍΫҐµſĊƠŜĺāãɜ',
                            'value': '|eȗ+ӌJƨȣƭ҄ƩΙ˶®ГϏЎɣҕňȔĴFéōSӥӨƖr',
                        },
                    {
                            'key': 'ǎǙѿԒ¬ѝ$Âϼ¬ϝχӊ˃ѻьͳʳлӜʳƌƥΖħбʜȐʰė',
                            'description': 'ԛoP˻šҷԗϋıΧ+ϛΠĤǸǸÞΘԪ\x93ĥɝϻɂíхĴǷȶv',
                            'value': 'ӖĖȩ÷ƎơΥκ/ŭЭ˙ͽԥǊǮ\x96ɦƙ˷³ыȞ\x8eȖҥ˫ɔϽι',
                        },
                    {
                            'key': '\x97Fȴ˥Ӯɀ\x95ұ\x97ͲɈǽˉʀǳϧтŞŉ=нҞ5ʫ´ȣԢ-˞κ',
                            'description': 'ĿѕcīόŦɽϫǌřɛΘьȎèԋǇƷǭ\u0379ҙŕ˚§ӌҍìΊϬĚ',
                            'value': 'İҫгͿԪԨЍĨѤϺǴKҼWʹӱŦĥ\x8fŅÛź˲LӳŋĨJæɘ',
                        },
                    {
                            'key': 'дɡƁëŋёÄЏÝƟ',
                            'description': 'JQɏ\u0379ҨυƼίѫǛȅ]˞ԧåϧϟƲĝũǊĽεӓΣˆȶΧʴÒ',
                            'value': 'ʧ(ηntϻÊiǗ˦ҡϛȟʠɅëƷһʼƔƮýŁϰЃĻӟ\x8eеɿ',
                        },
                    {
                            'key': 'ϻȬԉȬƟӅɎԎҨĲԦӟͺȝǱƓƴЍ',
                            'description': 'ͷʅ\x93ΚʵƁӲħˬƾwԘЄӯӑДάЕåҧ\\C}ѱ҂ѧaǣĪɵ',
                            'value': 'ɩŅʹǿԙɔĲϹȅʯ\xa0˱ѽʓѼrùϰĐˇҒƷ҇ʤѠōŅJŌÒ',
                        },
                    {
                            'key': 'І',
                            'description': 'ӈʂ°ͱWԢŚҀӓъӘë¤ɃƘɏÎϺάХ˪ŪЫ§ʊғƆȢÎȭ',
                            'value': 'ǃϓ˾-ˁԀŬǿĆѾǑҽ`čƟϤϲПÐuцˌұƎWӑΩϑ¯ɥ',
                        },
                    {
                            'key': 'ʫˀǄ.ӬӾʗŁµîӏȁԬ¾υ˨Ӗêž',
                            'description': '`\x82\x95ӤǱɳԭҹ|£ӍŔέϕĉϴÔĂǃϺEƣîM\x8cӐѧҮѳм',
                            'value': 'ɸӄώ\x9fӯοЫӛ7Ňcĳźϻ˞ǶМƞ\u0380\x8aȷ\u038b§ͻЀ\x89ѨҠƼɷ',
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
                'focus': 8163,
                'location': {
                    'x': -7497700161219432939,
                    'y': 8977537268831870873,
                    'width': -1045903159302976197,
                    'height': -98146421194020888,
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
                    'key': "Ѵ\\ȑE'Ȇʅϓ&ǉ",
                    'description': 'ɠԛ\x7fǠЉƷѫÀӝƸďöԞϛǂͽɳѭȫ@ʺľЇŕϾĔSԌlư',
                    'value': 'ΓΛ',
                },
                {
                    'key': 'œԭҥȐϓʈэϗҊгˇβʩğЇԣĄĜƬʐΝÆэ',
                    'description': 'ŧӆǏȮʮϛǥș˝ŽԆҷɜԗѱȢҽ˻ƭʺūț\x90ǜ5ʌȐĨӤư',
                    'value': 'q˾ȍȰʦΚԐ§#ϑԤșҼĻˢЋȈӧԋ˕ϰοԞĴµǎԇƼǇŬ',
                },
                {
                    'key': 'ǖЭϒ&ąȶПʀрŶϨ˫˾ӅȓҪϮǩǈ҆ǉʉaЂǓԉɞʣ\x9bџ',
                    'description': 'ҷѩԙӍɁҦŐĩЁæәˠûщ¦ЁҕƈÁҀԝ\x94˫Ͻʑϕɢ҂˅ș',
                    'value': 'ӼȗБ˔ǌɒɶԬŝÀ®ήҰǯ҇ΜƖcoǄ0ѷÌџʕйȖϞņХ',
                },
                {
                    'key': 'бɎǿǄѩŲǉǜbʃϽԂйЋGӯŇѹƶ\x8aŔʻȓcõ˂Iɢ¯Ȫ',
                    'description': 'T;s҂Şǅ@ӠťӝΉӕЀƯŪ=Ж˸³҂ЗǖхϯˬëŅçȼǫ',
                    'value': 'ɛϩĽ˲ʗϣ',
                },
                {
                    'key': 'ɁȯӺϸ·ǂιҳӝ[ҲǗʟȠӲ',
                    'description': 'ЇЩäȒ҃ÅϣίƅЏɯŻΠÆŔ˾˘Қ˙ӿԡƠϐłƖà˴Ӣjǘ',
                    'value': 'ľ¦В˂ÌҭĞgҳƪŭεϗoҢ·ԇϏϼĢϲƕϑŔԏˣ7ʶCť',
                },
                {
                    'key': '\x83ƍΎӜÖȖĬϣӂƬ\x8cɶƜŜǌҳѫ',
                    'description': "ϼӶŜͼѳѤǗɵҶmѮҷ'ƥȄϽшʋō;ţɨӞ˶ǣԤҩěʹ>",
                    'value': 'ЙϏΞù\x9dίƫȊɛ&ĵǝКĬǻΘ˫ƱĤǲЭԨӶХƇΥу˩џє',
                },
                {
                    'key': 'Ĩ4ԈӃԠ϶ʺʍȷŢ\x89ɓǂÖ҈ʘ',
                    'description': '~xҰȆήǏˊãԂʁжρкT©Ӵʁ҂ϽŅϳƔмʈѵ˫ҧßӸʞ',
                    'value': 'ȁʘɵηͱ7ˊÅĦү˃ʲƬ˭ȓГαԂЙҍӍʆԭЉԪɓʉƻǕӗ',
                },
                {
                    'key': '\x87˚ǧÒӮȵˣԨɋ[ýϯĴԜӆˢ\u0380ťԗПȺøҼʩӕԦљƮÙǸ',
                    'description': 'ǅҦȥƦǠɆyѧʅϔêӢ\x8aӘԚɯѨȰGӻϸÆëȿҒȬӑ·Ήǻ',
                    'value': '˦ѹǲʌ@ķȟҐʫk·¾ɗҒ\x9fǢŦʅğ;Ɉҡœԅǥһц^ǬӨ',
                },
                {
                    'key': 'ż˷ÿƲqД\x92ɇԂȽˌǯқ;Ǯџɠ\x9eв8',
                    'description': 'ӈũĬ>БȥӝȤԡӛȗ˼ϰӦȡʅ"ʻɂЃê2КěMńįhɧӽ',
                    'value': 'ӸȅõʗƠȶʒчǀƎĚ\x81ƘƑπӨќЊɹýȣѝӲȤ#ȮѣФÿÈ',
                },
                {
                    'key': 'ҟȳʴʈdʇMҢāҟÃ˥îϕԇƘĽҍȢϑӐϣһМж',
                    'description': 'ǧÄÍϮʯ\x9dɻȸĹΊĴ\x93ȵȞϜӋǨŬȼŏʇиũӵȎʷɡǤЕ~',
                    'value': "ĲӞ'ċ\x92¡ʌȕҶĈɗϰƅάʤˡʊĆΙ0ǨNɐȚӧЖȗʅʕӌ",
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
