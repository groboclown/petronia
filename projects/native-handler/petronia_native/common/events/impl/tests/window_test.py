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
            'x': 51441701065774088,
            'y': -7960271652281668942,
            'width': -8778224519938091769,
            'height': 2203936801616652796,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': -572553783418312178,

            'y': -576074213537654172,

            'width': 6809586602448717618,

            'height': 5739049055703911991,

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
            'key': 'ҝԋтѲӈǦÏ˹ĈƸΔoҡͳ',
            'description': 'ĕŔ\x85ĜǋѵԎÜ\\ԐςԏδĥzɇĆЂǛCѹ˥ɝԎξĚїŎŹƆ',
            'value': 'Ț˱ϕĩGjυɧȘѢǧĠ\x84Ϊԏ]҈VϭϞҞçǍ°ŏҥŇ˔ɒŋ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ç',

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
            'focus': 5514,
            'parent_id': 'рϒ\u0379ɵ\u0383ŘʌӱϐЄɓϸĆϻϥň\x9d\x8aԫ¸ƉɪȱҖőȱ?ǲϏ\x87',
            'location': {
                'x': -5964133135333326972,
                'y': 805395425301398528,
                'width': 1549700271912202865,
                'height': -7994009975015056440,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ĿӤĢɶΣӒҔӎΣɭɛƿύ\x9aʚÝϸԪōŴҥВԓ˞мԘ˨ĥØӆ',
                    'description': 'ÎĳМǊɰԜҒǙ\x84ƇѪϧʽͳЧԎșɀ%ʮ»DШϭϴŨ^ɐɂƯ',
                    'value': 'ӛȵɤʽdǃϱąϊ˖ʹgԘӼσğJѦŅ0ӁʂԥѠҸˈɂϪºď',
                },
                {
                    'key': 'ÕǗĠƷІѱСЀԐȡγǲӓȣƎǽȳϥ#ʒȵūɵ§ưʡłāӨǌ',
                    'description': 'ѭƼǊҫĝȪɸ´ɏäɓȉdȪΒƱȥǴɈvΡǖ\x84ƌ¸њTʨҕŢ',
                    'value': '·ԝ»{\x89˔\xa0ìĒfғ`\x9fЇѹǩʡ¸ȏ/ʟΪϰęԆƈіБĀЀ',
                },
                {
                    'key': 'ΨŉȁӓTӽ˭ĈЁԭҌQР÷Í²ӄŭùƝƤҔùΦ',
                    'description': 'РҀɑp¹ΔƩӄɗʛ&ǚʤÜӑԑЯθϣȞϝθЖʰӱύƻдӚѾ',
                    'value': '¹ӮϞΊ¢ϓϬϦȦĀƋƤ¹ɹǮҥιǜĳЄ9ǘǑԫȓ=˅·Õм',
                },
                {
                    'key': 'ĈԄˆǨƸż˜äʬ!ƥҌʓϤ\u0382ȩ\x9càɁʐӲ\x86ˬÓԚԒŴ\x9aЧ˗',
                    'description': 'ϵҸԔфċÕȄų\x85Ԙ1ͿӬήɻ¶ȔȂęƉȧ²ŅŇΗςŦƑѾɨ',
                    'value': 'ϖŹk˷σƌуɄСӏ\u0379ϊíģ\x92ˊǘÓɿ˙ϾζçΣňӳįˣʍӠ',
                },
                {
                    'key': 'ɓˏώє˛',
                    'description': '§´ˑѢӷɝӫƄǊŅӹƚ\x98ҒӺɵȄҖČƑҧȒ˜ōĿɚ)áƮ\x80',
                    'value': 'Ӄѭƽ²ԡљŘҨƟįɃŅơԭрҩӎ{щЙӓӄĤŝӐ˾ӌ2ŇȀ',
                },
                {
                    'key': '¾ǾñðʫàƪԖƳşҵƾ˵Ɋɇ˾óԝҼǎǼӫМЅƨЏԝ',
                    'description': 'ƒτжŒstԏҙӨхШƻʌƫ҃јєѴ\x8e\x9bʵMwЖѩ£ŞӹŇϭ',
                    'value': '˚ǵģÅηĒú˥ϺƷЮƩѹ´βΫϧҥʭͲĔѦЂɠʎҔɬbΐ\x8f',
                },
                {
                    'key': 'ϿǪ ϧѵЍΕ%əÒ¨kиӉ\x90ˁšȖëɕΑѝΩoʲƍҫʹǾԛ',
                    'description': 'ԏηђɷΨЯʼЉ҉ПаϪľͽŒñЮéҧ\x85δƿӢʅԩƞɝǚʈӹ',
                    'value': 'ȴɖϙÛȇȂԧњɦчíԈRϹǋҷʡӺ\u0381ҮÿҎ¸ʄƯÉƲɿ×\x8a',
                },
                {
                    'key': '\u0383ўƿƄǰ˹ÙѢɰƿҿǫǯĉҌĲϕԌ',
                    'description': 'Ͱαǩ\x97ľĚҠʽƲŴϫϧϒĂΦϷũϗǋҁǍț˦óĆӣàω¶Ҟ',
                    'value': 'Ӌˉaп˱ѝ˻\u0382ʌĶďfɦiӂφУƑȶǚ\x8cɜЍͱÛΘӺˎϢƜ',
                },
                {
                    'key': 'ХÆѨԍҺϹΤҴϰȗьѭАʔѰԅtρʣϭÏȪȽɅɥȚĉ>šќ',
                    'description': 'СĄҢԆFș\x96˟ǽ)î\x90ȁɕ\x82Ԏǉ\u0381Ɛ\u0383ӕ{.҆Ɣ҉ȖȪěʰ',
                    'value': 'ͳŋȗКĒәȪǏӏƥԌ\\ħ¼ǒʡ\u0380ĪΤÿģ˜rԛѨĂɱɉͿÌ',
                },
                {
                    'key': 'êʻÀԑˁͲЀɀӶmяŢūҊв',
                    'description': 'ќyĞŶΛӜɯȽͳǿőǚǭмʯ?öёрǈʋτΆȕЋђɝɻ͵Ϲ',
                    'value': 'ʆǱ¸гϴΎȃ¥Ѹ҇ЍϩϏԓǷ\u0379)\x90ʝʹɂŦ˾qʑʯҧʄΉЧ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 4900,

            'location': {
                'x': 6889596553040022390,
                'y': -4476674811150817070,
                'width': -7386531414233200623,
                'height': -4582529767750364182,
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
                'focus': 6669,
                'parent_id': 'Ȼ2ѷΤ˲˓ҿŇϷϻ@ɚԧί\u0379ňӁЮэşÃlѠľOʎČĀĤЀ',
                'location': {
                    'x': 7328186934085536700,
                    'y': 6285619965425867725,
                    'width': 6089831476692297087,
                    'height': -1426666873763525533,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'ʵŭыԩ¨ʇ;ɝʑ\x9dЦέӳңǩʠ\x9dҊΗȿϜȿǒЏƁɈДˢāę',
                            'description': '·ǰӟu\x92ˁԂЀҸʟoӆ}ɀнóʇȎЙïѽǗȝƼŝŪɕ&e¦',
                            'value': '\x91тˇҖԘ˒Syʟ8ϒûӛȇqȜɴӷżŇ\x84ɲΈ=ǘǷƌ˭Ų¼',
                        },
                    {
                            'key': 'ФҌȟѨƷŁҴ1ѸѴ\x87ńɤЇFēӎś',
                            'description': 'ϧ\u0382Ƃȸūэα²\u0379ʥϏĊġқʗҬЯұЁЁԖӵ=ѵ сҔӬMΡ',
                            'value': 'ũӊѐ}Јў\x95ŢÏǓ\x92`Ԙ³ǶǣɽԣȔǘòӤÕӺтҹɔњΓ±',
                        },
                    {
                            'key': 'ņΐĲȂͻѠʮÿÖƢ',
                            'description': 'ϾɬӀʪĹºʢӎ2ʿkЗЎWɁ\x96:тʕɨŮ³Ľ`ǒΌ$ǚYī',
                            'value': 'Ɍ\x8fǔҾԔĎ)ЈĝϵϿɠʂ\x9cǊμ\x82ĉǨɛȤӍӺȀÃĆҿąǷϱ',
                        },
                    {
                            'key': 'ĪȼʣԈΎԆɿϐŠșǵʂЀˏѱʘӳǓ\x8eÇĥŽʖЗϫĮQŊϪʗ',
                            'description': 'ʦΌТ\u0383ГʌɝΪ˲Ā\x89/ƁĜϖġђ\u0382&\x8eΈͿμŜΗҰΰέҡǳ',
                            'value': 'Ƙѓԓ˺΅ѻǠUĄϙɗӠÓʝƐăϒԈȳÎѸӝΆŔÑБԄѭʊ˯',
                        },
                    {
                            'key': 'ҲÉĩЙǉ˟\x89ϝԂĮӿņѝʄmªԉƅƾǈ\x93ЩšǒĲ',
                            'description': 'ҰѓÓυͻϸɓ˴ϚҗWǻ\x8cÂΕƌȿŚςȽϾÝʌȅӒƫΈԩз¡',
                            'value': 'єгѧĕƫҕ\x9bƁӴϐɆɡĀĈӗΞƺǧ¼ӗF3ԭʧİӦđӯƸĬ',
                        },
                    {
                            'key': 'ӏɆβɋвkѦŐѿʼæƭӳ˶ŗʌûèѷɜ',
                            'description': 'ąɫOéǺȻΖԖɯҦ`ƮžщǾϏȼȜҍɍƺůʒ&ЯГɢϩǤŰ',
                            'value': '?Ʉ˰ȇӌ5ˑӶȷƤǎĪсđËҼҔȥȹйҾĀ',
                        },
                    {
                            'key': 'ɥœοŐͿɷ8ϝ΅\x92ɄѵΎĉÅǭαϱΔ',
                            'description': '5ҥƨɒΘϊP9ϢԪЃӤѻ¡¢ïƢȾʀФ8ŕDýĚŞƆʍǲã',
                            'value': 'Ͽ-Ⱥ¦ùɁʮҞҏɡ7n¹ʖɁүӲӃÐԁʽȃӗǫģśγҴʨʪ',
                        },
                    {
                            'key': 'ǗŽΕɅƖCī',
                            'description': 'Ǔ˯ʅȨ¤˞˙ˉѯ\u038bÈУӰƄѝ˹ҜæʺȣXшGkƿξ˛˫Ũ&',
                            'value': 'Ȗʨ[ԝ6ɺŴϕРƉӫνԪ\x81\u0379ιɏȮ\x98ѭǹРԫňʨɾтηĨG',
                        },
                    {
                            'key': 'Өԍӳ!Βѷ\x9fАʛqÿ˷ʺƞʹЩŇ¬ËʑЅÁүаǆà\x9fǩ#Ǐ',
                            'description': 'ĀŚδϭØɶʊõγėќŎҭ?ѐžϹя\u0380ӏӺ\u038dĕŒѕŹŧʻʦƨ',
                            'value': '˩ԍƟңҪiǰϯ¢Ü΅@ʕЃӻԄμƒʸˠȐΜʯǺɺŃˋƜˠϱ',
                        },
                    {
                            'key': 'ȬС\x83BʒƯĔˮԕͷºŷȏƲÓ\x88ɗӿԊŠӮԦϜω$ͳӶάФƭ',
                            'description': 'ŮƀɣӍˣϟҩΈҺӆ_҄ǒwѹ\x7f²ˁϽӎЦЕҤщȦɱ˙ȚϱФ',
                            'value': 'ÔʗƪҾʘӳЙ\x89ć\x80ɰāǖĴđū˲āʠ\x8fɵǪɽԉʍğфĤƬƀ',
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
                'focus': 4867,
                'location': {
                    'x': -5963912019005076538,
                    'y': 1537873011079974463,
                    'width': 3133486992375206464,
                    'height': -4558524992175267968,
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
            'reason': 'ʂϘÕǷȃюѿ¢īӍϿ±zҷԄƆȤʢъϛП×ђƁÍ͵ͿӿȋΙ',
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
            'keyboard_focus': 1836,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 5372,

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
            'window_id': 'ĞώϡTɚÓėČèē·ϩĀѐҖϲԓĺЖþӓǯΙÑҝrκ["¶',
            'location': {
                'x': -7474049695490917597,
                'y': -5070132155274679998,
                'width': 424244527872854423,
                'height': -1233999984223445244,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ЕќѧǗΟ',

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
                    'window_id': 'Ę˳Ƞ\x9aҎʩ˽ɊxҏӶŏˎӥҘȚϏˈóџоѼЫΏ΄ŇȇȐƄɵ',
                    'location': {
                            'x': -365263781951794114,
                            'y': 5638369310300722981,
                            'width': -2691874445292652066,
                            'height': 3828994499995532975,
                        },
                },
                {
                    'window_id': 'ʼqѹɢšѲґŤŽѱƏÈÕǒҾřуlėΒƳĩǠӣĬäβ˰ԏЈ',
                    'location': {
                            'x': -6131857356174781809,
                            'y': -5720288985974701564,
                            'width': -7807826716519030880,
                            'height': 3691734772469235261,
                        },
                },
                {
                    'window_id': 'iӚȸЇ\\&Ԡ\u038dμMχŁüУƛĞPǇ%ȣјώSʧǆ˂/ŤԪƕ',
                    'location': {
                            'x': 2505239166320253227,
                            'y': -8423934985560236605,
                            'width': -6278405477491815042,
                            'height': 3845296608600036229,
                        },
                },
                {
                    'window_id': 'Ӈϲ<КđƪΉЍԛȷѡʼπĈɬѓɞȭΑ\u0379ҋҥ\x88ƏԙƆƊȲΒł',
                    'location': {
                            'x': -11007037083424047,
                            'y': -2614845458466002234,
                            'width': 2465586703865018295,
                            'height': 8908355194566533501,
                        },
                },
                {
                    'window_id': '˱Λöдʋě\x90IǂΦÐɓ\x8dǧɘӑ^˔Ù²ʏéώɎʲ˪˝9ȱԂ',
                    'location': {
                            'x': 6013639524449839796,
                            'y': 6279198643833673683,
                            'width': 200046087212557350,
                            'height': -4739655367152506877,
                        },
                },
                {
                    'window_id': 'ПƻҊӭќȖǂҒťȸø#\x8eĆӠʬϨ˼ǩήʂƉҥР\u0378˹х©ѭ\x91',
                    'location': {
                            'x': 1479834551244642288,
                            'y': 1446939283722073412,
                            'width': 6054698150291198662,
                            'height': -2651987665204058919,
                        },
                },
                {
                    'window_id': 'ʩɂ\x90ǔˋОΚ\x8aҌ˥ȜѲƁӒ!ŦXз¬ʏϔΫÿŘ˙ӅȤʀťƞ',
                    'location': {
                            'x': 2440860129371211567,
                            'y': 2241182311776589183,
                            'width': 2815152217072079552,
                            'height': -7940224557555832739,
                        },
                },
                {
                    'window_id': 'èө˒\xadɈƨɗс\\ėšČȀȐΉР\x98\x99ϥ\x9cɇɬǺ\x92FĄѓԮĲД',
                    'location': {
                            'x': 504023996436888656,
                            'y': 2738564873949482271,
                            'width': 7158016688966961613,
                            'height': -1040965502353392865,
                        },
                },
                {
                    'window_id': 'Ηы˥Əėɀ\x88όӃ~ВǾϑR\x8bԮ˕\x9eƴҫɄɸԥʸn˸љ\x82ǼӞ',
                    'location': {
                            'x': 238959519168681242,
                            'y': 3905803655225874198,
                            'width': 3225899710067956693,
                            'height': 1968541868782733489,
                        },
                },
                {
                    'window_id': 'оʅӓϔЉͲ˲άΖƞĿïøĬӃЮΑh½¬:\x94ѶSķ˰ӭ\u038dθſ',
                    'location': {
                            'x': -8147385427695577960,
                            'y': -7698525985653227610,
                            'width': -7947764897525650347,
                            'height': 5784368205159511016,
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
                    'window_id': 'ƥʋĸʐҁ',
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
                    'key': 'ε§ɀ˚\x9eϗȷ\x8eӽșč˶ļϷҔǧμԭ¶Ҁϋ\x85эһάѓҢ',
                    'description': 'іӸ˟χҊɺǨǋ˨;ҀҒʓѺ\x89ӽ˱Ȩ4ӝɩяȄèʊˤ΄Ȃ\x8c\x8c',
                    'value': '1Ԡ#˵čˋʲɖZΰC϶\x8cɋýӁÅʪZƀȉΚʢЛԛřҟ˾Ӥ\x90',
                },
                {
                    'key': 'ŹπΟsԝΓҴʮԝѹÎԏϚĠ',
                    'description': 'ԃШ˭ĴœRЯѥy\x8bһͳʈϘκÊ҇§ƿɺˌ8ѝԨϥγ;ϔʑ˲',
                    'value': 'ʁ¨ʓƌ΅ѩǽåɤ\\ß҈ЍѯĝŶϹǲ҂ӧťŵϩ˅ƧғΊtVϏ',
                },
                {
                    'key': 'ÓĴАdɢүιĮҥʹŔʅҮǤǔԈȵιҦňӌҩҡȵǃͷΰşɷö',
                    'description': '5ĹĂȊԤϽǼϾӖ˽ȱӄƎδV\x9dĐҮςԕÎтΆh\x91ҪϖsԂέ',
                    'value': 'έҎʄȩ_ǠȾͺЦΗ4ˮɭч\x97ƾЩiϨHҽţʀͽȑĔɟ:kԕ',
                },
                {
                    'key': 'ѓǔūĔWxİiЌȎÏϋрӯĘƀ',
                    'description': '*÷ɑ\x99QǿČȪ\x83ԓϦѭ¤²ЦƩΩϰʗƨԑҀɢy¦ӌѪτҘĳ',
                    'value': 'ϗ˘ǽԛЀǖãġ\x85ɮѽ+ùˏИńґÕɽŠFFÏ·ӧɳөƴĕ<',
                },
                {
                    'key': '\u03a2Ų҈ɘΠϤϩʂԊÈѓɺώӂǇͽˣѮцĻŝöЇĊ',
                    'description': 'ЪҪҦţƂcɜзȚĲͶȉǁʢΚЉѥÀÁʅν\x96ěҟϼƷӵπ\x94ǫ',
                    'value': '΅ӛѷȓϐηӼǹѤÔËļɜБ\x94ǂԂƚǊɆԖɻNʘƹҟEιЈƕ',
                },
                {
                    'key': 'ƣҢɗʧЍҽƋĐGϒ¡ČшƵǥϯјǮMĐĭ9Ԝӡшӂ',
                    'description': 'ʦӴˢËĨΎøҋ·҂ӹɦԪĝɤŽԉбϢΈ',
                    'value': 'ѸξʰιɆ¢ƜģþʕҥăӳϣϠKʇ×ɬůÞςƾ\x98ΉԫHӐƟõ',
                },
                {
                    'key': 'ĻЩΝԣʻ\x9cфǁɥîԫuε\x90ÎԦʨ˹ʽχĭȞӬү˂¦ЖҶԊ\x99',
                    'description': 'ї\xadǠ"˕ƾԤˈɾȗɻӶĞϰͿɫʬЧϪÕӮ\x82bŀ\x85ɅOȽɵ\u0378',
                    'value': 'ǺΎlςłԂɗɨсƌ®ÒĶë\x97ÞЗDǽЩӌς·Υԫ¦ÿʽNƦ',
                },
                {
                    'key': '»Śˉ˻ңхĖʻƦ˖KŕӔ&υʂʃ²Ɠ˲Z\u0378d£ҷλǝÃЀʨ',
                    'description': 'ʟʒ¶Ř˰ПɿλVǤIʧɞӁǣЛξƍíԎǚ¦ϚкǂэɈÀД˫',
                    'value': 'V/ĦЖΈ&ϦĽҍÌϝҎԘЫKĬΦѾʥѼɰQÕő¹ˀԛŲϩʻ',
                },
                {
                    'key': 'ˡϊЏΪЇƂ',
                    'description': 'ΧrϷƸȬGīӳƜγǄкêӏʋěТˤÑԐQˤ΅ѤQаˁԣϞž',
                    'value': '\u03800ҝ*íƶǿǻƬÇĦЕȾΛˍƑӌd¦ĬΐИʤҀÖЛɚԛԕĕ',
                },
                {
                    'key': '\x91ѧ\x91ș΅Вǩ7Ӭpˆ',
                    'description': 'эƪɊȂƼЕ)дȱħɦʚÁǝΦѬ˘ʵǖβ\\ơ˦ыýĜӝġø\x99',
                    'value': 'ҎʩВΦËǃʍ¬«\u0380ǦńԉĊҭҴӐуƪǿӭʮǲɉŷжğ˒ɾУ',
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
            'focus': 9355,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 7848,

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
                    'key': 'ωɓӣγ»XĶŒƑǃҳȃҞ',
                    'description': 'Ď\u038bӸěcȓэϱs\x89ʛ΅˒ȑȄƁυɩ\x84žҭ\x81ϡH˴ϵЄ˅Ʒԝ',
                    'value': 'ȓʳżϩ!ϧʛϳ½ĳҊ\x85ɤϾ[ȚöͳsiɩʂԬŚŻԈӐӧȜѰ',
                },
                {
                    'key': 'ӐҬЭȼ˓ŚԥǼ*җ',
                    'description': 'Ԩ;и\x7fԕÅϢзλϜȣrϠ@ĔЊӎџ˨\x87Ȋɒεŭ\u0379ӈЁъJÿ',
                    'value': '҃ɦ`ӃǤÓÿ˗ȪÃąΧ\x83ԟʪԎа\xa0ǁȠDʂиːǢȽǎğȵ˪',
                },
                {
                    'key': 'âЂʅΰùȅͷŋXƆȴӿщɏ\x9aҹяΨˢTүЕʞgԅв˲',
                    'description': 'ǟ0ӕϲÜ0\x97љԋΞɗΈĝҽΎɞΉьȂʡҶͻʇԩξǧӶ˰яɮ',
                    'value': 'ȇͻөԇ²ǚΉԠĺ\u0380ԔЍ\u0378ѳɌӅƂȏ҉ˌřžлʳΤǆɣҽďG',
                },
                {
                    'key': 'āЊ=ӆΆȿ×YâŤҦñǉ\x9ağӽʹϹʦʶȓǉҬ˷',
                    'description': 'ǒ҄«ˆΟɩ҄ͰùіěӞԔȎľğBĖƻȟɊʭv·ҽ˅ӊΤ1Ǹ',
                    'value': 'ЈÙχȴѱɬɾͻͲƕϧӲĒ2ΫΙʍĨɡµұЗWҁϥƤяԝŪˌ',
                },
                {
                    'key': ';ǇŞŪUB҅ňìʝMѰҁ˵ƧnʰāɲþˬϾŝŊÖӖʅGΩм',
                    'description': 'ӶαɖÿʝƈԪҠ"ɒ+ʧd>[АɦðЃΊҍʥϽɆӏӬǻ˓µ\x9c',
                    'value': 'ƅ˔бªēǥƷʗϋƎɳОŔǓŻɛӻNѐ',
                },
                {
                    'key': '^˛ΦɁĒΊĆzκÂ',
                    'description': 'ϘɭʋϴǬȯӧζϞѨţǡŃчj×hiκϮǢ,˥Ӡ˭ϗѐƊˠԭ',
                    'value': 'ͰŌОEΩǯʖȀԃ\x8cЖƼʹǹŵПǏƝΤ^ðãѩǼѨԧ6Ǻʬ\u0380',
                },
                {
                    'key': 'cp˱',
                    'description': 'ƨǂӠΡɼŭːґɄȣʁ\x93ҖˋӅŰ˃QɩȤӭԝѴʽϷŽԟ,˂Ю',
                    'value': '`\u0380ϐɶԞǣíôɴЌϙɠł˩ȣʀϔ³зЀmásŒŮСǉΚƛF',
                },
                {
                    'key': 'Îĩȇ˥\x94ɎÖĽƞˬɵҔԫҿ˳ԪɍσƕȌő?SѴϦԋ.°§˜',
                    'description': '°äŸƵɵǶѿΐÁˀI§ǵ҃ʩ˄ȜƆɠζӠ¸ʂįλýҁυȊͲ',
                    'value': 'ʗƏрѮţ1ò\u03a2˩ǝΥǫ˄ʤϤŌҶ³ͺʉȦʁƤǓŘǋŔЩɀǴ',
                },
                {
                    'key': '3яRVϖҢɉP%ӜѸĔ¤ƺˤЫåRƺϳÀѼǹΥϮkdǦу\\',
                    'description': 'ϰЍBҾ¬ҺT˕ͶŏԞϧĻʊōʖȲɈͷӤѕЛȏӒͶ!ĔӈӜ£',
                    'value': 'γҊɯYЪ˱οŲғƉ(əѸƋУԥӥ\x8cʝЛ˫{ǌρΡϣӞʜϕϼ',
                },
                {
                    'key': 'Ċȵµŕĸš\x89ʥΗȂѲ÷RтЖ',
                    'description': 'Ɂ\u03a2\xadБX\x99χƙ\x8cϷtѕɩάΑ\x9cέщυөӓʃʇ҃ĳΙÅo÷ƺ',
                    'value': 'ӆӕŜ6ԊΜĽӔŪԝMĉәȴБǳЉȍÅɢāӅǓм˷˖ЄƎҩУ',
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
            'window_id': 'ѪƂΉӰʎӔͲҖәάϫјϣŶˇŅȫӒǛȏιϒø˃ƣ\x9fȚǺǅă',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'Ȫѝϋʫӂ',

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
                    'window_id': 'ƷʬʝʂԭʮʍȲˆ\x9bˍ´ƢȊоӠʆԨԐʛǐƏǓ˱Ȣ\xa0ĈЉΜҶ',
                },
                {
                    'window_id': '˃ѶǚƭƯǼΤYҷӍĉǡRѦԌɊеӳˎʻЦ͵ñƢˍ\x98ǩǳÙѶ',
                },
                {
                    'window_id': 'ЩӢ³ȽƸ\x7fɹύĊßȨȎŅǁЫϦǖϚȽħ˘¯҂ʒˆјĒϷĴҶ',
                },
                {
                    'window_id': 'ΗԌіѷҶšԖïä^șːśМqkӘøԣВǮЍȔȵмԂɢʕćҭ',
                },
                {
                    'window_id': 'ǰЋҐɅŭǨùȏɐΞƄIƧʬκ˔ԗΨȰԙΔƏ\x87ɮҗƀҗ¾˙X',
                },
                {
                    'window_id': 'ŖδǝƫѯƵӴĤжɵЯˌƏӘ˙ʙԒȼΦӹźԩԄ/˔υҎǯϿĲ',
                },
                {
                    'window_id': 'ΑǢʱ#ʁеϞƇӴȕȵϐɇŐ@ѐ?ԃПƝưÂ\u0382ѠùӭϻƎ*ŷ',
                },
                {
                    'window_id': 'Ӹ\u03a2r\x7faƚф\x90ČӧǚаԁʌIzШͶ˕ğɠƨȫͳËĖӊq¸ˡ',
                },
                {
                    'window_id': 'qĽêʰŊʍȟ\x91åŬԝҸ҈љ¢kлżʷʟ£ǵƈфĩƜӀ¼шƿ',
                },
                {
                    'window_id': 'ƽȝȥε7áʘƪȓ˳ȼ˚ǻLЬΠɢІ¼®ȺȜÔёӎ©ȠƗ(ϋ',
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
                'їȑҹéŜʴĹԍу\x82ѷρЗȳɏӲͼiԋĚиɞʾ´ĺΓǊŊӊӮ',
                'ČΪ\xa0ǨǬUǕ·ǕȌr·hс³ЃԬͻ\x9bǴԁŁЌϒº˹ʲ$ȉö',
                'Р҈șӥtyԡɼɣȂ˙ϲħеˋ\x8eʮÙëbƌĹŷӔ\x88ѩѬͲɣ\xad',
                'ʱ˪ıѩƣņПͽĆtFʱӒμæʘɃķɄϸœ_\x8fӜЈʤ]Ćϑϓ',
                'й˕ϽөҽϷs҄ёǫȔŽǥԠԇɦĕɟţԆȬͷȈǸśӦŻгҏΗ',
                'ɫҒΣpԏ3àƓƃő\u0378ł)Ԁˢ¾ӳɯΧϩ\x98ӕϑӞ·ǁқɹƼS',
                'ƨʶ±Śӌѻɰ˵Ťӫ&ȭÒʮøŴɚӏÝΤ˂ĩƄʛɏŎɥÝåΜ',
                'ǹ·ǔН˲ɭƢ?ɺƚ°ĕʟˢ˺ԤФӂėԆңǴ˵φҠƣѨϫȒʪ',
                '÷ZӪȥԨǿl^ӉoʥɜƮùҮɤÔLƣφˤ@ȌʪƭɷӾЦԒŐ',
                'ßñ˶Ö?ћҩпŦњԫʋԔēϪ˚ɞʨˤ\x80϶\u0382ɝͼέʤĉJȡȩ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ҳˇĉ«E',
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
                'focus': 3873,
                'parent_id': '˽ˈОǙҼŕҶμƀůɐδɓîЗԐҖǡǭɏÞǤˢӂÃͺΌѕˢĺ',
                'location': {
                    'x': -4919807724794398099,
                    'y': -7139072891166739296,
                    'width': -3302469294155035928,
                    'height': 8441508434525967991,
                },
                'minimized': True,
                'meta': [
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': False,
                'focus': 7521,
                'location': {
                    'x': -5924060896830724841,
                    'y': -4520441218935266048,
                    'width': 5049434368791221910,
                    'height': -7204643471401906246,
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
                    'key': 'ΩиϐȽǟņ"˟Ԋ.ŉˈƷԒƲɺӃýǇԦʉǏϧĘΣԅӼȽɂ\x96',
                    'description': 'ǺΩɾoΞуԐŔCĵɮºʆÊʖ\x7fĹ\x8e˅˴Ǒʐ\u03824ŶPˌ\u038b/ǀ',
                    'value': 'ϽїèȑФҬŞǎÌɁɭрхψЀǳɇЖɽҧьӮάĝȌɀϑҢЁҳ',
                },
                {
                    'key': '˔ʮͶϖҵҟɣè¦Ҫȷ\u0379άơʳŶѕŃĮ`ΩѦŲİƺŖˤӴƊm',
                    'description': '҉ǹӹϭȃxҦ˷ϔӳįȢ|ԚŻҞѕƚƭðԍʇªңґǁЊцӢȳ',
                    'value': 'ˤѼѓŹϓҋԎͷ{ԜΕƐǭñʣrŌϧ˟ƪ=λWƺԆ]ԀøƎÇ',
                },
                {
                    'key': 'Ѹʜ\x93ƅČυϽͽʏű\\_Ď\x92ѷȤïf¨ʢÁχɚΕԁŷµԭѩА',
                    'description': 'ʂ\x92Κы˹óɼƓƿѬıшŽˤ\x90\u0380\x9eÚїŋƺźśϠ˂ȦőɔȒ΄',
                    'value': 'Έ',
                },
                {
                    'key': 'ѴϼžʂҜƓԗšƸЍǨńъƺϱԃ«ŧҵҞÀѣҮë',
                    'description': 'ɏƤȭόӞœƜTƏ˗ȪˑпƻӪĽ˜Δ\xadăɦӠ;uҟƗ+ҕ˹ʑ',
                    'value': '\x88\x83ҐʔĤ\x9bνΝġԅвϽǬѝń˘Ԓ×ϒžǢîϨćȲӃ[ɜćѶ',
                },
                {
                    'key': 'ζʇӶ²ȡŌёĭŀh\u0379ӋίżƧ˄ǭʿͱǑɚÝ˻°ŘӺ҂˒źƪ',
                    'description': 'ъąŉΚÄ˷҈«ËŒѤưӀYкƞʸώMťĶϚƪіȨű\u0382º˱ѩ',
                    'value': 'χɒǼȜԃŘϛņΆІ\x81ǋикйĂӡНųˠɁåɾ}ӭǰМɂɃњ',
                },
                {
                    'key': 'ԉ',
                    'description': 'ӸΖ\u0378ѵÐЃąƕǠҪԁсï´ƭǿ\x86ьӗĚ\u0380$ɯ"ư\x96T\x96ƫч',
                    'value': '˯ҥӽԣʘѭïqӣŔ¤ϥЙгГkȀZØυ\x8bҝ˟ӭȆ±Ăͷчě',
                },
                {
                    'key': 'ʕ˹ŰУҜәEӔҊəɲýºgξƱЊӀЌMҥΠΨʈǋ[\x80',
                    'description': 'WʯɆϮȱʧ²wѹa\x9aҁvҶÑˈϙмƠʂзԘҖɲǰʨ\\ʪ˅@',
                    'value': ' âЗưԄУùԕΏβΩȥҍ¯Ϫ\x96ЈʧZ&ѾԧΉҥΞŽӋ\x90bǲ',
                },
                {
                    'key': 'ĩ\x8b7rËÚɗɖi˲ȓǏŷ\x83ӤҊzÿũ\x97ąяӋνǫίƧ',
                    'description': 'ƙƔȨӻȉϞʍϕśƬӭӇʃ«ӝӨʰϦƱͽěЂϢϠю҄ΑĜгˤ',
                    'value': '\x96ӂũƠΌaԆȢͺѿȤŰʜʮщΰɝϚP˛ВʲόЁıҭЅҪʾȹ',
                },
                {
                    'key': 'ъȼ˾˶Ͳķ',
                    'description': 'ѡè\x84˽ÃѠӃрԌϮɉǣťЌҥӬ\x9dˡʕш˺^ėѿ͵ѠĎɟ\x8d˓',
                    'value': '\x8aͲԐѼЁǡΪ°´ȡ˵ƤҺɮäӧòӔŔ¾ÖƖɵɦĈȌ\u03a2үŌϢ',
                },
                {
                    'key': '˯',
                    'description': 'ɏΕϝƺɥiǅϟЉΓˏQńÅ®ʹʶ˪ӼӔ_δË¶ԮƴɻЀԫ>',
                    'value': 'ˬѓ ʸʦŰ9ȹʐźωδҦе\x8eˊ^ƒӰȗΣväɖŎ\x9b×ѨĔ½',
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
