# GENERATED CODE - DO NOT MODIFY

"""
Tests for the hotkey_binding module.
Extension petronia_core.hotkey_binding, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import hotkey_binding


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
            'key': 'ҎɣŋVĴšΖǜрӂϒpʧɒȹЄΐ\u03a2Ξ[n(ɋʷԢΝҩǻĳѦ',
            'value': 'НFеӇˇȱĞŨǚϱӪí\x84ҞÚɫƸͲĴ˞ɗǂΆвѭрɌ+ȸþ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'к',

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
            'target_id': 'хԪӓРŦɿήżʓФӌȆɳ¬ǩƦ\u0378ƻWǻŨϚԡ}ϾÄÖɥɺă',
            'parameters': [
                {
                    'key': 'ɨѵӑӟǟйūƾέQ\x94Я½',
                    'value': 'ԙҴRϊ×öђӲȬȼĂƞ͵ʠô˻ҳΠɊϖÑϡÜοɛΙ˧ІĤӱ',
                },
                {
                    'key': 'ˆԤċƐƴȫ\xa0҈аˈÑҷΊŴɽΘǡҠĮԕЛљĮʞȦŋ',
                    'value': 'ϔĳʛʳyɂӔŷ\u0383˸FʈӀčӑϿ9ĆӀǶЪüȨʴđǾsԅġ+',
                },
                {
                    'key': 'ԧēʚԒҙ',
                    'value': 'ʪǳÎɚʔqĉśΟ˹҉ȵ҅\x8fīɥѓԇ\x84ʙˢėэįϱśǰКϫ\u0383',
                },
                {
                    'key': 'ѕԈéȭƤӽƺʀȆѫϧÀưхԉ;ˉɃϫ¬ơoɴ',
                    'value': 'Qǖˎ\x91҉϶ҠԎԢǿˢƂ˅~ôƴɮÞӠî\x90įБΕĥӵУҙЮɑ',
                },
                {
                    'key': 'ѱŔǲӪЂΦѹűɅ҉ǜʾ˹ɷ;Ĵϫ˭ʉĎɇ҆àćӄǼНTd\x80',
                    'value': 'ʡдèFÕԪҹʋȼ\xa0ԟʈӧǊďɧӻbɔȇʹϤӺȤқɺΪɇқM',
                },
                {
                    'key': 'ʠ)Βǿ',
                    'value': 'ϫ©ŕԅӍόʅˌB{Ƙ#ǅґʼ҆ŎҥѝGĜɢЙɺƹCɜȥŚţ',
                },
                {
                    'key': 'св»ʳOʭɺɷȱ;èҌϔğÏʭɑzͻԏѰ\x85ȼʥ\x81ȊЮ,Όҁ',
                    'value': 'ŇΫSϓȚҩ"ȺήǍȇJάʖÛʖȎԊ\x7fǧԜÁΗΕԔ˄ȿҰ<ҫ',
                },
                {
                    'key': 'ʺƸϬӻʒњ;ƈԮĽѝҥ˩\u038bʾ©ȻǨĠʸϴ|ΗѼҽÆШ\u0380Ǹʅ',
                    'value': 'ȺˣԩPƍԩÄT˻ƵJ;ԉĿ\x95ß¥ȸͷ҈ȵ«"ʯɴԫϛр+ɨ',
                },
                {
                    'key': 'XÕχúëû7ơдǵ\u0379ϙѿȻƁĕӪɀдÚyUҬԅҎӖȪȴтŝ',
                    'value': 'ȣӴĉɺźŧōκϧlϢɵȤҋԁǋпѣџʩĶҤµŬȈÇѓȚͽˑ',
                },
                {
                    'key': 'WβΝνˁӹϧΛ\x8fŴůҹǥ˪ˆ<\u0378ȤcŲ¹ĠδYμĈЛżƟҟ',
                    'value': 'ǐʫϨˍЧġϤѽƑïԮК˙\x97ũҬĝ˶ţʫʧËǝŦђκΆƋѽҵ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ԦǡɼԐ϶',

            'parameters': [
            ],

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
                'ƦЋɚԃΘЕɓЅœ˦ČȼűηďɢȏҊЉůˌ{ҀɸҫЍΖ¢Ìс',
                '.!ʏԥÚԙ*҄ąϋř',
                'ƙϡ¨İȑʞÛ',
                'ºˉ*ӡŃǛȼΝѬɘӓӖ',
                'εΗϏμ`ɡ',
                'ȐƛυŴ˨ʸʜȺŌ,§',
                'ƒϨґ˱ȀÌr',
                '+ϝÝƹÁϩЉŚԪϊȭϞӉћǌжΙǸήϏЛϗêΦМ',
                'ЗĴ\u038dLҲЧƿ͵Чˑ',
                'ɱ0ΡʴţɆ',
            ],
            'event': {
                'target_id': 'Å°ΩȧԑʈɚӔǄЍʀεҔżέ΅ϮӧʤȌʵǡѣѱȁΧιӁ\x98\u0379',
                'parameters': [
                    {
                            'key': 'ʓʶ˘ƠƥѝŧʜƛқͽԀɚ\x8cǼĜµΖļeϦУΈϩԩ˶ҫð_ʨ',
                            'value': 'ϹЬʛȃԘΘɟLɱ˲\x8bŚÉÖʐpǷÍӤˇŢбʏ\u0379ȄсƝʩěÐ',
                        },
                    {
                            'key': 'ɟɴ\x81ēϣӺɣЧƽ·j\u0381ԡ:ɂ϶ÔтęĦȥϛԨ\x8fċ˰ʢă°Ҵ',
                            'value': 'ɧȀĢТĔʩ\x88ӌ¡ԭ˸Ălΰ_}Ԏ«A9ϐʠȗȭǋʣʢҘHΡ',
                        },
                    {
                            'key': 'TϿǡƺҨϡӰӉκͱѩ}ěҳ͵Ӡįșʄ\x83ĠΝɺǵƑĴЬΖхǊ',
                            'value': '?ŶԣʒqΫϹЧΎɰƺеɜКĝÞΝԋˡŶΈҧ\x96ωԑŻ¶\x93ȖȦ',
                        },
                    {
                            'key': 'ѓʿfķ˺äɪŽҌʐ˲ʍdʩƋƐԔэʖӥϗ˦\x8aɤƅŌ',
                            'value': '͵ˁʇЏѼшǜôʦn˖Ʉʄ"ПҿìǮĵνșƬFƱēӖ˟ѤȈƻ',
                        },
                    {
                            'key': 'фϔ`СͼjԑԑԅϬӴɬМϢʳȚUâʨӘΧʈʂԢ\x92ԪҨ',
                            'value': '˯˦ΡЀӟÝȧEƱǴυ҉мгʟOöƔoҎkϲȂ˟ƈʹњɄѭԘ',
                        },
                    {
                            'key': '½jĎÀΧԔ°ƐƎƜ{рůϗˋĨӢćǎȃ«ƝŚћ˝Ӛãνǃǭ',
                            'value': 'ΞӃэнǁÃÍʶĚϠʝòԘϽɰɯȸʢãИӵ¾˭ɀǦž˵ʡӆʦ',
                        },
                    {
                            'key': 'ʷӁȥłGʓmG\x9bЛѲȬŋ˂\x84{ӒԥԍģƃҍΣφĳ*БѺēʴ',
                            'value': 'ƬśSȬΨƉʊĶԌӈёһӏӡϢǅУʗԑŉԛԣŮҽͻћņŌȃǀ',
                        },
                    {
                            'key': 'ȭjɘÔ\u0383ʀӒѰжӳǳ·ʚђ˃ÈΏƫcʳ»ǯøTԨї©˦ŜJ',
                            'value': 'ϔ/ʾŀȂƢȥŪǋĶþԊҏɟȯ¤ǮЊƪϳԭſNÞǿʔņѠԀύ',
                        },
                    {
                            'key': '&8\x8cưŋϗN{8үӌŜ\u03a2ʜƍαZжȢƊˊԀw\u038bжėЧmĝϛ',
                            'value': 'ǜҠСȼÁԍĺЖ˒ǚӪҺɱјŀӔѥʟӦΠȉ-ȝОŒØǉА)ƌ',
                        },
                    {
                            'key': '°ǭϟƂΐάίƔŒєdԔжų\x90ʴǡʒҊŦӹΦǽʃʪÛɩѶūɮ',
                            'value': 'ǏƇϐӘЃ2ҡζƲΟǬEʃuˊԙʯ¯˨ΤƋ\x90лЃȞĩȄūӂ˳',
                        },
                ],
            },
            'comment': 'ƽɸĥĽǂd£ђαèǈѯȚɒƞTѸ˸ćОRƁ΄ˑԕĽ¯ЎȜƢ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ũ',
            ],

            'event': {
                'target_id': 'bĲӠįB',
                'parameters': [
                ],
            },

        },
    ),
]


class BoundKeysTest(unittest.TestCase):
    """
    Tests for BoundKeys
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEYS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeys.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEYS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeys.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEYS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sequence_type', name='BoundKeys'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='master_sequence', name='BoundKeys'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='bindings', name='BoundKeys'),
            ),

        ),
    ),

]


BOUND_KEYS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sequence_type': 'sequence',
            'master_sequence': [
                'ǛʳĳĔе˪ǽÆʓÍ˖ѵͺǾǙhɓŰȍȏˁҪɋȆʘ',
                'ӡҒǄʥǠЉěҫвþԐ҄қΑ°âjχͶû',
                'íϧƳŗȋӢȶƸ"ˇ',
                'êÄРǼΈˁ\u0378ƙÖͽǥ\u038dǇϬǸȊȸʂȕԫɮϺbüιά#ɜϴ',
                '{',
                'ˤɴ',
                'ʓŎÝІƩǗƢˊӞԥӊȭǙ:ŮϺʾɻʃʊ,ԉȣҤǁѤƶʑ',
                'ưԂÉØѠǇԈʢȨóӼ\x89ĀʣΤѸʣѫʷÇÚϽ',
                'ƣøǃ³ȇǭÄ¼ƥбŃƋxʁŢŶĶԇǶҗ˹cɲÅϮδ',
                'Ĵ¹ÙƕӼɪƌņŵΓƠĞĹ¯ùºƥ\x9aɣšʍƳӲ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ʨЛl§ԪƱӍƃ_ȉτ',
                            'ȞAɣ\u0382üſˢӫβϻĹӊŀ´ҥӎɀѹȞJ',
                            'ɜĩŬΧЎA',
                            'ԎҨȢ˟ҲԄќƍɴηҝӅΧӌεɊʠ\x8fǦ',
                        ],
                    'event': {
                            'target_id': 'ӹϪӅ}ρʷȅĚˉҞáƼСªoȰԠϗӤǤxŶƉǬ҅ĺʲІʄà',
                            'parameters': [
                                        {
                                                        'key': 'Ίԝ˼ӶҤͼȏíЯΜŖː˭п϶˪ι_ϗӧӜˎпƏɡфʎԦĻÊ',
                                                        'value': 'ӸÁ;Έɭ˪ΣυѮΎǀ.ƶӪҍȣȲĺɾƳЃѧθ>ӝĉċФԐ0',
                                                    },
                                        {
                                                        'key': '\x93ЕӳҼįwɁӹĭѢАѲ?ΕŻÕӦӊϪɥҜӪаӝПĳσ˘˷ә',
                                                        'value': 'ʅɛǁϏe˺ĤʷĦЂsȚҧŬƜÈ˴ӀƉ;ơȩ}ŴԙɖɸĢӅʤ',
                                                    },
                                        {
                                                        'key': 'ҡҳҕѬȜЁѿ%',
                                                        'value': 'ȵˑɪɑӫө.Ԝńνѷǰɧˢˣăʥ®΅ŗнӃΎуӒԣĂ˜ӓß',
                                                    },
                                        {
                                                        'key': 'ȧ2VǒɭΉȹΠЮʯѻɸȵΚϘʿČǩԮѻԊȅ6ɫҮɔǕʢɗԇ',
                                                        'value': 'ӟʛˏϧрʉǰǔ<ԫſ}ӬǚЭӬcʯЯėάčΦӲɏНɏʰɍο',
                                                    },
                                        {
                                                        'key': 'ɿý1j϶ŃҩӀùӎ<',
                                                        'value': '7jɘƵӆηȤӏɉѱϖuӌлҌўĿϧАԖԛ˅Ӯ;ϧƙʝˏͼˇ',
                                                    },
                                        {
                                                        'key': 'ʌћiͿˣͺƪfŨчˤĒœΪ¹ðƶţɆɌҒүƛ˴6ɜјćҍˑ',
                                                        'value': 'ğϥӮЄŻ\x8aχŢͿͼʣĭԭɽİũȽʶūɩȖʄіŇŏļƟʲԖũ',
                                                    },
                                        {
                                                        'key': 'eɖɺ',
                                                        'value': 'ҐϔΆΞΟЇǥΙϓӐùӗҌӳȒ\x94]˦ӺСˇѝЦГЩǪƥӸˬԑ',
                                                    },
                                        {
                                                        'key': 'ƹԒ҃ҸîƢȮřўмԅѡʱҒ˦Ϥɤȶȍ\x8a\x81ӽˊɀʫ"Wϻ_ę',
                                                        'value': 'ɰǴĺMçTÙÞчƸɉƼʎĦóԤɝÕƱʹ\x85ωЬaʱ!˟Ͳy\x88',
                                                    },
                                        {
                                                        'key': 'ƨĐΕÄæʏ\u03a2Ӭ>ӄΧƽόǆ/ЩΚÛЏΨɅɶƓэŋʌɰœȫ\x83',
                                                        'value': 'ΖʧϢǣǅә4ɸ&Òϯȟ˄żʹǆÎ҅\x94ȼȖʈĩëČŰϮÚ˜Ҟ',
                                                    },
                                        {
                                                        'key': 'ÏѤΣƆǧϭҥ\x8a%ʹѧÞƶȦхĚƍ0ӼɢѥÝϽȤˠУίРʗХ',
                                                        'value': 'АˢϓʴΥPѨÙɆÕԑÅÌÜŁȑʱúċԠǳΠʂ˹ȏҵǲÄơѻ',
                                                    },
                                    ],
                        },
                    'comment': 'ĩŊӡԊȋєȫÍϷȔQƀÐϨ?ҧΝӔǴɚɡYϞЫ»ʘʢӷƑӺ',
                },
                {
                    'keys': [
                            'ҬʲIҀʼĵԫțԀɝǘѝїӵ',
                            'Ϊњȟ˷ίƸϰÏOȭŌʭΌɤιŭÕ?ϭǰŏɒźɠ',
                            'Ъ',
                            'Ĉӄ\x96ЩψüóЇСФϢъҢΟŎЭ˙ʉ',
                            ' ЉɱˮCȝƅԉȕϯĭƧƁ2ǕÞƻ҂˒ҍхμ',
                            '˜ˌƞЄUцƴуFɦPAҶ',
                            'όЂϪӖϞӏЧɩкϩƌΌƆ&ùǅΧìԭĦɤåƪ®',
                            'βε˽ԛѧǥŌçΡ',
                            'ƣɲôҐΡ\x85˘żͰÑӅΓĽ\x94ʿӔĕ',
                            'МW¦ȋɵӝˌ@',
                        ],
                    'event': {
                            'target_id': '»ɤӂӘѸѕΧӝҏϷ˞ŇұƩʒōӓԅҁˇƑѪİӍĜӢǟЏӸϥ',
                            'parameters': [
                                        {
                                                        'key': 'ҡɞϗåѧҚƙҗϕƠȀ[їɂŤǫˀҎĸŃūľƖŃȩƂҕlǡǻ',
                                                        'value': 'ˉʳ\x81ɮ0ĊЍðԑШȣŚrǺƮƸеѺŃğ҄ӖѾđKӰăӇA¥',
                                                    },
                                    ],
                        },
                    'comment': 'ҳʬΊфӒЀIǨрŀƍӮÂȑ\x8eԤɀ3ЈѨΞҶϜT¼Ҕмµ|ȭ',
                },
                {
                    'keys': [
                            'ʓϵȼӆƙˉ@ӬǧӣêьȆWΎťĖ¡Ҩ\u0383ųјƚЦÔԞԁ',
                            'ӰФ˹qʊˬΓµZϓλVŌξ\xadν҈ÿԎҭ˺ĶϦAƈҸʱ˖Ǖ\x8a',
                            'ͱǱΡȸȢӈʏkǔѲԃĶȃýƅÅ˽˸Ǵ\xadœԥǱĭ§Ѵҏ',
                            'ҀϙC\\ϼƩʌĒɾɓɍƌԢ\x90ҀϘvʖ',
                            'ɦ˓ӹŴҔҺҏ˪Ơ\x8d',
                            'ƶO*¸ҰȻĵíʄԊż~ǭÓȎķȐ˭űԞӊҍ',
                            'ӕВӭˮŪ6ǗAʈΗȼřȳßЧ´ϡєΏųӇӼ',
                            'ˑһȅԫϑԧ¶ĂÎåԍӸŔ˰ɴĠҗџŝҹÿǻ',
                            'ľȑ+&¤ɋ',
                            'ϓ`ŔŲµҳôÖҘҲʹüÁÝǃ',
                        ],
                    'event': {
                            'target_id': 'ŢΙĜǢξϯАȂ҅ŭӣΒ\x8bɒ\x90¢ΊӮāӜv2ѧʰļμґ×ǻǰ',
                            'parameters': [
                                        {
                                                        'key': 'ϏӱҶ¢ǿӈ˅',
                                                        'value': 'σĞʿВӵFад\x9d^ŬͷѺ˧ĊēîƨϝɪȔɱ.ȤǂĮŽХȂѧ',
                                                    },
                                        {
                                                        'key': 'ӳʌԡҔĢȃЉјǦɽџƲрqÛ\x82ZəЬŻŤƤɂ\x8cĦĽ¨ɷʹɜ',
                                                        'value': 'ȩǏŴϚсāѝΩҫԢΗҖӞƓԖφϕįƟžˆңъгGǕǧ\u0379ɬќ',
                                                    },
                                        {
                                                        'key': 'ӫɬϝΓ%ƃͷ\u0381҂ϞĚρʏɆȕżϹц\x98ΞҀԫԐĤ+ѦÌůϡō',
                                                        'value': 'mψ˾ŵƥĒɄŢӁĺȔЍ\x93Ҡŝӽĉ',
                                                    },
                                        {
                                                        'key': 'ƃϡÍ',
                                                        'value': 'ΫѨ\\Ǌ\x9dΉ˛\\ƅҥýԁӀϻȉͰԃȷđUƢéɃӸô{сζɩӜ',
                                                    },
                                        {
                                                        'key': 'ƸԧƸŗJʬӻë˄ŝӅʨǑēɢϻϨSʇёȁ;ГƷǹˣΏǦΠƀ',
                                                        'value': 'ŠŖČǮȊǁǙ Оų\x84Аǧȁȋ\x91ÔζŖĥÆЯ˾ʏ ϖИЙʇΕ',
                                                    },
                                        {
                                                        'key': ':Ѫ\x8fҾӃɰʩͳɊʍԜҪˣӱҊӜϳ¡ǥаԒӶȵъɣɓĠɝϾК',
                                                        'value': 'əЬ\x93ÎˣĖӑĿтÓΧҴɅѲ/TMġőɬǖӱπҦӊѕҋʯҎǢ',
                                                    },
                                        {
                                                        'key': 'ƩϧҢƜŹǴɿ\u0379ӭӲԪϿGӂԄҕƴ\x9eĮȜ\x89ƘҎёș+¯ȱӁԃ',
                                                        'value': 'ϠǋŘѷFЄƉE\x9cӋΦЅ»ɭƇʌȱˌ\xa0ĢӊʳİƘƌbĴęҩƬ',
                                                    },
                                        {
                                                        'key': 'źψłщӏɏҙʖǫИŚˆő«҄Θ\x8f¨ң˕ȄưʯƠȗԙ˭ÒƄʒ',
                                                        'value': 'ӚˈʺҲ\x88ǖ˃Ėδǆέ·щҮωtbCИиɃԈ\x89Ǫ˸ƹһÈʭʰ',
                                                    },
                                        {
                                                        'key': 'ϟˋɾԌýʛ}ΥώȊϝ',
                                                        'value': 'ˉˊ˓ȁŬƿĳˈǂæŭĵѤҥҦ\u038dǪȲӉЪǩвЏƤβĥή[ĥƎ',
                                                    },
                                        {
                                                        'key': 'ϩɹҡɛҢųÈ-7ƽÝр7p}ƢRˊԠĘЛдśɣˎωҘˏ',
                                                        'value': 'ЃҐũͷˁȖѥҞùʹѦғǍV\x81ȩǟ=Ғή;ЂϝԇҪũDɤÍ˕',
                                                    },
                                    ],
                        },
                    'comment': 'ĵ˶ÇɻɋӬ°Ο҆˼ʻ˧ʪƱ¸җӑĠǥХÃƹſбhƚ˞͵{C',
                },
                {
                    'keys': [
                            'ԏǍĮϪZȪԃ˒ǩ',
                            "ȯѼжЯΨ'Ұˣ",
                            'ʏ\x9aԛ',
                            'Ĥł˹õ',
                            'ĭʡˇĪÙ˛ʀμ¥јˤ˜Â',
                            'ȇ',
                            '\x90қ±ĦȺι¬ǶȌĦRĪϔԝɩҶá§«ŎӘ˻҃',
                        ],
                    'event': {
                            'target_id': 'ΦъЪȼʒİҐɽģщʱζм҄ҪʲО\x9fƨȁȜυØµĤʺ/űλӅ',
                            'parameters': [
                                        {
                                                        'key': 'ҵ;УŋӑσIԮҷ\x8dʨǮƮЃ\x9fāɹϠƒȡƮϭwςұŜҡњƭ˕',
                                                        'value': 't˅āÈҾ»IԨȷϦ\x8e#˾Җúy¢ӜˍҎώƃόƉЉļʄŜʩĸ',
                                                    },
                                        {
                                                        'key': 'ÈəԈŰϴƗ²ĊӄBͰ|ў6\x8cńΆĊĬź·ɬȩ·ΏʟӣҼЖε',
                                                        'value': 'fѫȧƁʱӿš\x98˨\x9bƷϣΫЭìȕɽȝ\x82űϏӔŪϴ˲φКԅJʀ',
                                                    },
                                        {
                                                        'key': 'ӧѣ˓ȶßȈԗɲӔ#ȚȟӾҹͿʘtÍԬɊɆуΑɻȆÿÒʿΧϯ',
                                                        'value': 'şĘљƝÏϹƕҾȆ;\x88íЦÿβȃɖˆâĘǗʑɓцĬóҼ¾ƉӉ',
                                                    },
                                        {
                                                        'key': 'ҩĜӀǀ6ʌˊʻҝϛƚ|ť\x80ʀ˭ĘÀӦ\u0380úя΅Ӹƿʧ·Ǖšҷ',
                                                        'value': '<μʂʺӶʉεƓÌƊƲԄɶ\x8cӎȊӬʰҽFЩÚȪǟ÷ƺ˕ȆҲƧ',
                                                    },
                                        {
                                                        'key': 'ЌΫЇԗ¯O҇ϮʙτΏȆŠʚʹʃσĘίԫƑłXҸʆĮΤ\u038dºħ',
                                                        'value': 'È˨[ӜŊΓʣŹƥ˶ÜĳŰȄǕ§ƤьƔ˜ǶԧϦ˦ΌąʑʄĤĚ',
                                                    },
                                        {
                                                        'key': 'ϐQϩǀ;ҤјŒƹʑȑ\x99ԔҒ\x86ŠłLȃƜуЇ˛ԓɈŽͷԧKȉ',
                                                        'value': '҂Ҽ\x8fϖ˖ҜԕŠϷχˊÅϞϣԗŋˁѓaʿèlǉȒсpѝœ\x87ƽ',
                                                    },
                                        {
                                                        'key': 'ѯҤДѓȄШсЅόЕѿ·ЊЯȨ¤ѠǓόǗϢƍGҢʙήЬϜԠɲ',
                                                        'value': 'ΧүÀçBɥȨ˜Ӑ˜ѡӏЄ#âЏɅʗǦҜʍоӬεĖΟȹÃaŊ',
                                                    },
                                        {
                                                        'key': 'ԡʏǓσŚ\xa0ϥÇ˵ćѥԌƙӠƈ3ɘ˩ɟɱˮƑsĞОQœēϤf',
                                                        'value': 'ϠϘ´ĤKǣс-QԀęĔóЀЊȰқԁ҂ΞPԢǇšĸϡϫӥ\x8aҰ',
                                                    },
                                        {
                                                        'key': 'ƧєЪŐtȂӲӢWɫƤЅγѓԡ˚Âπг%ҏƼИƀ΄J˟Ȩǈā',
                                                        'value': 'ɚĉʽʨи¢²ĂΥј\u0380ɠƉ½ɧ>ʎÏĝƱöʗΏǾ˘ӱ˶ÎҦ˵',
                                                    },
                                        {
                                                        'key': 'ӿÄӌĄßўŔѰĵΧԥƟʛџӴčʼӞÅЯԛϢ%ѷΛɆɑѶq0',
                                                        'value': 'ѰȪĹβύĚ˨ǉƀưňƓΔȘuǔŬǖŖЋ7Ԙч×ӑәҕʲӽɑ',
                                                    },
                                    ],
                        },
                    'comment': 'ϔƟİŐˉѰɚɛſР3\x80˼ґώПΚԔҏϱӢɖĹΫɝȢϞФȱə',
                },
                {
                    'keys': [
                            'ΎƬέʐ',
                            'ϓŲȫӨ¼ȳȀzǽ\u0380ϰҍӇHċ\x89¤ЖǼˑ˙ҽɡ˷ȷ÷',
                            'ѡǱ˧JӃϡǐOԉΪЩȰŔǢϺ',
                            'ʒӫ҇ҾɥΟѽΟĖɖʭ£ęțΆҜϝĠĻ',
                            'ϲūȮԇвǭ?ǋʠgͺȽ',
                            'ԫ͵ºƻÆʁˡ΅¦3ҍƛˇĺåЀǩǬͻ×ЎɾќƘƖʂԚ',
                            '˨ԅγȈҿŗ˒ԙѩ\u0382ÇΆə\x9bÕӧπßҪĜʹѐԙιӺÁʓͽѬ',
                            'ŧɤȏɼɈТаʿʈʓʾĄӇȿƻО;˼Ԧ˔ѨUΰ«͵Üǥȇӭ\x99',
                            'ɱʓӖɥƖǧ˰ĝБ˰ϨёˈҶҌѸ˄˞ԁҰʼåiѬѰœl6',
                            'ȼĥªЙĤfÒҞ',
                        ],
                    'event': {
                            'target_id': 'ϫЏŰҠζ¨ʎ`Ȱ5ĤԕӿͻƣХƸˀШϰӀˡ4ʙůĔ˦Ū҈\x96',
                            'parameters': [
                                        {
                                                        'key': 'ȀǤџfӼ²ϼҘЁυʁɎЬȝχʤү\xadǮ=җˡ˅',
                                                        'value': 'E͵ʭǓͷƍԏϡǂ˲UØ˙ơͼō˦ĹhƟԖ˞ɓěӎ҉қǏƜĻ',
                                                    },
                                        {
                                                        'key': 'ɵı1ȊʐԤſĝQɽɨ¾ƾ˲Ũ\x89ȿ\u038bҏϿϤ˧7&ğ[Mϑτļ',
                                                        'value': '~ĴǙƄΣȮĐқʚϩǠ΅ОγƃǔâȔƙ˩\x84:ºįőЁřԣ\x9bν',
                                                    },
                                        {
                                                        'key': 'ɪдº',
                                                        'value': 'ɊƴȇəůǒȈϳʰæӳȤ˽\x7fäƙÓˁӪӑѠɕџмöЁɴѳǖZ',
                                                    },
                                        {
                                                        'key': 'ҿʠƫͷɬ0ˍkɻŤ}ӟͱ%Kƨ¨ȱ˷ΌƣхԊÃрѵͷЂҰȨ',
                                                        'value': 'φ$Ƈƥ\x8c*˾р\x91&İÇƘǩωҒ\x99ɽŲ˭Ұ&˚}ǄÖуǡɂ',
                                                    },
                                        {
                                                        'key': 'ŁƱ\x83}ŎОIϢԈԄʛɯř˥ÖƼјƜǀ%Ӽćȯł˓ϚҪâμϣ',
                                                        'value': 'íƣƂɧӂ%ƙˤϹɷj˳\u0379˄Ƃңɠяɩ˃Ѯ4ўŎũʑ˘Ӊ>ъ',
                                                    },
                                        {
                                                        'key': 'ФԠˁƽϽ\x9bρАйђҙɪɹы͵àΚİϒǛŀԮӨˁ˺ȌȨˇȥU',
                                                        'value': '˃\x92ҥƱˁӢ\xad\x89ƋɣâўȬ˴˄Öʓ\x91ÔÃʸÕ)ԌȈ\x88ӕЫ?҉',
                                                    },
                                        {
                                                        'key': 'Ѝ÷Ϭ¹ìȖϓԋqʸʰΗ¾ПȹʇƄҾˊΫӲ\\ыҙƤÞœ>Ɛ˄',
                                                        'value': 'ӶоЏě˗ZԎԃҜɎǙʅҴϦëɑѿ˦җϘǗĴǬěʀϹƄǕɠİ',
                                                    },
                                        {
                                                        'key': 'ʹФƏǲѯϿơҩѯǏēԆǄ˭ӋÏҹѡ¦ːԮȔԅвǁ~ҕ\\ϔУ',
                                                        'value': 'ɅϖU!tΨеqҬĞ.ƹԬĥ˥ΜуοҨЬҜÌ˃Īþǯ\u03a2ΑӀx',
                                                    },
                                        {
                                                        'key': 'ϖ\u0379\u038d˰ͺŽ΄ŔΞѪӻӒ\x8dǤïбҽ\x81ɣӑCЁȒȩИÓƸҺмɳ',
                                                        'value': 'ĩĵɎåƅΕƚ`ÖѳϗбɑʎѡȜюˑšԘǓƯ\x8dΧЀ\x82ʌʅʼѝ',
                                                    },
                                        {
                                                        'key': '˅ɠöĮĉÑßțҴ˲ɕ,ҚǑɗǼǣѵӫɰLßʊɞЍȠ˘Ӵ˝Ε',
                                                        'value': 'îƺ҈ˋԇԐԪЖŲЖȭРˉӘ÷ú¼ӞŹΟϏҷƑºțϊœͷ§|',
                                                    },
                                    ],
                        },
                    'comment': 'ԇЧв˅ĊǛŴɾʛϕǤƉϾȨӵÌҰćȅЂʘϫWÍйPʁԇʚΘ',
                },
                {
                    'keys': [
                            'ĖόaУσ¾ˎɺyӫӮôǔһgϮĜԩļYˬƌüǤѐ˯ѝ',
                            'bʚ',
                            'уΕ',
                            'Ƀ5Ź\x8dǯ÷ԖǧƊ΅',
                            'Ǹĥ˛ßӛ\x96ƪĽˉȫӫ˨ÈȂҎȴʒў\u0378şҒԬŵ',
                            'ʁ_ȾҹәɖНʄżˀþĴɅͳ\x7fԀǎ4³ʝʌы[ӼƆ;ȶ',
                            'ɨţäыӨ©ӑнʀŠѪ×Ξʐ',
                            'ɡƁϵòӸˍДҾǥ˛ƝԩŁĳ¬ªǱɅҮϤ˳ɄöȄɎáάƃņ',
                            'ҕɧĶёňIũԨȝǁ\x96ʃΩʐÂЦѣʞη',
                            'ҽНЄʦƖһблΙҥεγƺϬĐåǦϋ˄&Ǉ',
                        ],
                    'event': {
                            'target_id': 'ϵɱӲђɄ}Ëų|ɞάȿƳĮȜƕЬRĆ˕ΆnʄƭbƦөãΈɘ',
                            'parameters': [
                                        {
                                                        'key': 'Ζƻ҆Wbϱ҉ʣzͿϴϝ˻ơѬʑĪʝ\x90ǚºʥѕҁћȑ\u0382ͺ\u0378ԍ',
                                                        'value': 'ƈ³҆ҷгТXάʱ½όΘѨϵҵuȮЙҤƲ\x86ΧΪ\x8cӸƘĿϪҊŊ',
                                                    },
                                        {
                                                        'key': 'þƶǜþ',
                                                        'value': 'ɬDȍпÊϤǉǔȼϯӣ˥ԢѲ¬œͷбя!іˏyɲľяĽЏԞӚ',
                                                    },
                                        {
                                                        'key': '!˰ΛǋǸ˒ԝ4ўŻϿб˛ҡоӼ˹VԎҿҖđǣʒàȃаԈ˯ʷ',
                                                        'value': 'ŕЛ\x83lΤƣѭƕȈ§ΰȘ˱ɰɎԒÀκ˗MǲrȮǶȇǅºǕ\u03a2Ď',
                                                    },
                                        {
                                                        'key': 'ӜưȕFƤšSӟÝ˴\x8eųϓ\u038bɚŹǊӖ\x94vȭΡԝԄԃѨɦȒ\x85Κ',
                                                        'value': 'ԠѭЪџҨìӶñOĠӑΡυ«ώѮуҲľ҅ǧɍ½Ĵ˘ҁ=ǻƹӼ',
                                                    },
                                        {
                                                        'key': 'hхƋǨĴȜ˃ƸſҴѢԣwϞ˷}ҏ~ƧΎϊȕĠĳӅԤѮЦ"y',
                                                        'value': 'ĽʏɡԒҷѼͰЬǳ¿áώYѪ\x89ȓЊҶϵīԦџüуâ˨7\u0378űȕ',
                                                    },
                                        {
                                                        'key': 'ԋӤЫŦӶѤŒʼɐӬԌ',
                                                        'value': 'ĤƱ\x9cЍ\u0381ÃҼȎѻΊːЄőʜɹљͺԇǭǔӠȦѿťʞӍȑȏԭВ',
                                                    },
                                        {
                                                        'key': 'ɉ˱ŐŞÄƍŷɑѝ˥ŜѐʺʍƼʵoξѹϤȨȪΙҒϨǬ\x80˄˴Φ',
                                                        'value': 'шЀƄȲťɠϝͱɌɗʁьɦȃҰϡÜ˖ǻӃǗϷФQ˶kǐӾˁԑ',
                                                    },
                                        {
                                                        'key': 'Ҍ\x88æđɘ',
                                                        'value': '÷±ÌùǁлǒѝĢVǍӹѠр5Џ˲ҽƆ\x83ќіɥ\xadʘѾǊȯϠź',
                                                    },
                                        {
                                                        'key': 'Ѩ˳ʗʮѢŇбȧԣ·ʹӈħЯҴʠнȴËĶĦ˝ԂЯ',
                                                        'value': 'ҞÚȾҒкĳĲ»ƲʼĳϗЍӕĞĉ˞јƿʐҘΤȿ˜ƿҵр˾ġӡ',
                                                    },
                                        {
                                                        'key': 'ΧëėҚōѦҊԣԫ¶',
                                                        'value': 'à]εԧȁǩõĩԕΠϏ%ƅЯΰ˽ùœяŪƒͺȹϥΚӬЗȚӴ\x88',
                                                    },
                                    ],
                        },
                    'comment': 'ΖQsҘԅқȄϭ΄њ»ґïΐһ\u0379őЮô˞\x87ЛƺÕȱÍȨǐĜԭ',
                },
                {
                    'keys': [
                            '˫ŉ˙ΪƻΣđǎĕэƺ҄ўяφŕʈ\x8còʋΟ҂',
                            'ǣʂĽԩԎȤԐˡĔ·ʖ\x8cЭ˲ÝŤԅѦωΈͿήŖИ!Ê',
                            'ǧƥćʛӲQϾüwǴȄŉӻʔ4VҲġԢΑʷ',
                            "ʗKͷʞ ӑtԃǡɀkҰˠûƎv'әќǋ",
                            'ӽȒǙ\x9eM˒ԈěÇxΩĭɊúЅȝѐԡˇʂýy',
                            'ҕåКҖ',
                            'Ŀ҆ϑ',
                            'ϣźʯhɓ',
                            'ϊOĞөҎęĀʑţϝȾ҉on_ȤĨƍɴÅӲ',
                            'ԢƷŠФɱ\x93\x85ǻІѐΆ\x9a`ŃġӡӁk',
                        ],
                    'event': {
                            'target_id': 'ԁ˳јӤ˗ƐǸϸҪɔ#Σȁéĩ»ʡĿȢ\x80jǵϧơŦ\x82ɮƚ0Ҩ',
                            'parameters': [
                                        {
                                                        'key': '\x8dȋīɣĥʓЊƓXƏѲ3ƪіã[ġԪǖ˭ЯӻͱU',
                                                        'value': 'ӿĲÚӎŤӎǻҝѠϪǂȺɇƟĴȚ\x8eƵҸÊûЗ˝дRӯ˨Еτˤ',
                                                    },
                                        {
                                                        'key': 'ȻˣӠøΰͷzКɶЖФӍȂÉñ',
                                                        'value': 'ʒƉ\x92ͻÆϮɏ˙ČȽΌȌИƨʋ.ɤΉƲǲĒĵԞϏīçǾţΧ¡',
                                                    },
                                        {
                                                        'key': 'ȟǄʭ¢ͷŗҳ˵ıѽ\x87ʋГCéϠəԩ',
                                                        'value': 'ɛЋϸKɒ˘ԙľäˮіˮÇƵÞ\x9eбɍӑqԅķԦʵͻʖйËƙɽ',
                                                    },
                                        {
                                                        'key': 'κӚśτǤ',
                                                        'value': 'ΠÚÔäԫ\x82ǂÉҩ\x8fҙϋȐͺȄԗЭϭѶƊǹ¢ЋǗǼȟя«ƙѯ',
                                                    },
                                        {
                                                        'key': '±˷Όɵж˚Ȥƍ²\\VÉÞ,WψĴǟɐȏáТƊˬɜΧԉʤƜ|',
                                                        'value': '\x99ӂԪL]ȁ»ƾɈìĀҍÊų\x93҉ğӿ\xadÞƞЅĐǂȨͰĤ˻Єż',
                                                    },
                                        {
                                                        'key': 'ʣΐPǔEȆ1Ӵцί˖·иťɭ˨þѹzɔϑσəɇӝʯZҰЍσ',
                                                        'value': 'NϰÛќуƩΘ˘ѬˊςȳɀďŇěƫʭPЍʂBŲѥãVȋɌѿ×',
                                                    },
                                    ],
                        },
                    'comment': 'ΧӠ¸ƸӔ«ǼƃͽɵʺʕФ_˃ԅxˣҤɉϾˑӊšņвɟďͻы',
                },
                {
                    'keys': [
                            'ΧfЌȢҼŲţŗПȉ\x8dţǏˉȨ\x9fӟŃΠӖĭӭzԢğϏö',
                            'Ѓй',
                            'ԑԤϔӯ\x84',
                            'ϩҵԜƋĿ ΰǌċŻW',
                            'ú҄ƒӅĄ҈ǡǣ΅ʤѫǔʳМǔѝӅʄˍİʿ¡ğ\u0380ɘ',
                            'ňˁφǩ˨ʛͻи',
                            'ίɓˠgүǹcŠНҵ',
                            'ȇůԥĒҝҖкʫƱЇ\x99ʩȓƽŭňсШҲŃΡ"ǥϪtŘƄԥȁ½',
                            'ɽʱĜʸ\u038dΈȦјʦǌEȵǗÝӗŷ\xadЯƈΣŽЋʨҙ',
                            'ː˸Х',
                        ],
                    'event': {
                            'target_id': '˄ϿӯѯœϺԞřѶŤϤΦΙҡǞϪҿɘԃȆŋȩ+°ζЫϢʾʰı',
                            'parameters': [
                                        {
                                                        'key': 'êӶÈƛәΓͰǟůƪƠΣJĢǊҡưĆǗţхԋсɖҜưɍӡęȲ',
                                                        'value': 'ӝŠЯҘĊΥɤɚҌŏ˻їŸѝȐxҺǹΟƕʱмӪԩҽŜ˜ԝ϶#',
                                                    },
                                        {
                                                        'key': 'ƱŸļȹĄΙҲіƞπƸƃǘĀȂsɭƶϱωϨԣ\u0379sȎњhúηƾ',
                                                        'value': 'gcЏӬʑҶӌŗŁƞ\x89јЖӻŝԩԟů5ǥȓԦѰǻƑ£ǵğĂǷ',
                                                    },
                                        {
                                                        'key': 'ʱϻͰι\x86)қȃĖɉ˪ĩԆʑăʥГЁ³â҈ϖͲƑÌȝ¸ԇԉƙ',
                                                        'value': 'ȾtEoĮѮęҙď3˰\x81ӤƲЂђˮȼ¢Ұ˙҃ўѥ¼ԓΘơŁҪ',
                                                    },
                                        {
                                                        'key': '\x7fӢҴЬѳΥIєZāʉΎăӊġɼ\x82ƀìМ£ģ\x90ңPʮǐźâЏ',
                                                        'value': 'ӀūɶҬŃǮŀȓɛɗϪĘ°´ұˆkº_\xa0қĳğǶǩԅɫɈƲb',
                                                    },
                                        {
                                                        'key': 'ͻӎғ\x91ӶBϰà^чǛäћΥΥʀΫǆњςҳ;ЍҋǕŠŲѕʅǻ',
                                                        'value': 'ôgġМǏҞӰȘ\x87ÿʃРѫǅхʢŊȫҵԘгҿɬЀ°Ϙѕo]Ƅ',
                                                    },
                                        {
                                                        'key': 'ҁăͰΛ˹ȒƷˍʞӛ\x88ɬĈķӮ\x80ӂçѤȕʓԅǳƪȌҝԞyΛƍ',
                                                        'value': 'ѽҜǭґώљπѢӋǈˆѪҢϿƁϟӣҌǠªuƂĉӌœÁ¿˰ƤҰ',
                                                    },
                                        {
                                                        'key': 'ԥõ`Ǔ<',
                                                        'value': 'ËӠѣĸϹ¬ӦĉЯȭρӐ?ˍǏȮԙӊȈԖȫɝϼƗΙΫB˺қˏ',
                                                    },
                                        {
                                                        'key': 'ϚʽɊʝҖ!ƠЗѢÏ˹ӝǈο\x95ˆyĮ϶ЭȂɑɉѩˣ҄ӦȰĒЌ',
                                                        'value': 'ϭ\x80ƸǖЕØȢђΧȀϊˀǇɩE-œљΫöɶӒҴˎɂŨȲɻǽ϶',
                                                    },
                                        {
                                                        'key': '\x98ϨʌvɩѡһǁΊȦ©ЬʀʃŉɈΗÿ6ʁʹʕɃ˳ɜΉɵǙ¶ώ',
                                                        'value': 'ӯ˲ƾɠǼξ˕ʭҋʮíӠҌîч\u038bûΪЇυщċĺΌ6Δçɭϸà',
                                                    },
                                        {
                                                        'key': 'ѶӀͳɎмТЍ&îʌɥӦӺʼƠǘ\x85řϑɡѼ·ōŊƬһ[ǢĝӢ',
                                                        'value': '\x99ӢϊÕєȓȷкɱңƱһͽҫŌŕ\u0378ɟѵʂǚˋЌѭ\x9aĭųϸƐĥ',
                                                    },
                                    ],
                        },
                    'comment': '˨!ςӑɘǼǉģɽȬԉŞ\u0378RĿэºƥM҈Ăſ\x8f/ёŎɡPǽé',
                },
                {
                    'keys': [
                            'ĤȦϞŹȔѮŧЍѺ\u03a2Ŀ˶÷ϩԛuįӪʙ',
                            'ϫǨĭӤȾѬˎĽɩȌѸӣ',
                            'ӊҰϊɌǪш',
                            'ɘκ7ɫЗĬǼEǤϲĜψӞκÇʵνӰďǳǲǋӋÙ',
                            'Ԕϻʤεс;Ȑԣ\x98"ǓǅȐӗԀˊƙªБ',
                        ],
                    'event': {
                            'target_id': 'ŒǠӏɩҸГɡЧFʟӻҕʿʚћĺ˱˯ȓņɜƴŨҮӏʤʒĜΆѼ',
                            'parameters': [
                                    ],
                        },
                    'comment': 'Ŝ\x88Ԭ4џЌŤҐĦŷβϊҌˀʆˌô\x83ЄμȗХËԤöȻѩÙʀɉ',
                },
                {
                    'keys': [
                            'úùŜ;',
                            'ԚzµӑƫјшTɚ˱',
                            '¥эΉĊʿuͳȿԉƊƜ˻dˏvǽӕѰǺϮӧǸP[Óӄҽ˖ʞ',
                            '~ǜҎćŇƅ',
                            '\u0378ϡºʥԇԃњԨ˷¼fÇһþјƪɨɋҔәѵɼ',
                            'ȃɸ˺ӟѮΔúƅƜҳМɖ҆Ԣζʹ',
                            'ϙέ˚%ͺǃԙ˕Β\x8aǸǮ҃İϨҫø',
                            'ӳWӹ\x89HћgƮϸҲАnȜ',
                            'ħӚϨƖàʝк҄˱ԥӕƧϻˋπǅ',
                            '˭ƭһıɳ«Яâ£\x89Ȍӳ˞ÂĔӢĉЂo',
                        ],
                    'event': {
                            'target_id': 'ӆÙƗЇЦŸ\x9eɆ^ёӘğӉΆ]ДƉπʭύϻƬȴҦúͽԧ˄ɳ˲',
                            'parameters': [
                                        {
                                                        'key': 'ɋ`ΗɒӓȉÈ˜ƘԍʚΫƴǭϚ¸μϿԦƃԂЇǣϴұȋɅϸʎү',
                                                        'value': '_ƸðѓѱXԈΕѩĢʈ:Ӑӛ¿ơΪΗάЋϣϱ\x9f˳дÔΖȬɛʸ',
                                                    },
                                        {
                                                        'key': 'ϖȸҚϝſǀ@Áʋ\x91ĈÖƷ˫Ё\x8eөѬϹЎǫѴǀ¦ϔƝŶÀòӫ',
                                                        'value': 'ȠъВѩʳćγǋȺ˴ɠŋƁɎ˄ȓǗƸƦ\x90ʂɦфʹŜϭ%ØˣΠ',
                                                    },
                                        {
                                                        'key': 'ͳЉȨuĐНΒ˩ʷbĹͱӳβ˦ęйӌÝʹƅʐ҄л¦ϽжԜӶż',
                                                        'value': 'ӗέАSъËɎπλ+Ӊ\x9fёɊǳУG´˕ʢΐӸΆХԆцӹԩÙő',
                                                    },
                                        {
                                                        'key': 'ƹĹͶąôҏƘ\u0383ŬØƺ´Њ²˻ǆɎ˃ʳ±ȟЮǱĔˊ˕˞úȗ˰',
                                                        'value': "ȿϛľÑҹƉνӀԤӮ˭ӛĬÎǱԦқŔˆČòèɻԚӵѯҭ'ҧз",
                                                    },
                                        {
                                                        'key': 'ɾԢƵʣȆtҰȻɎԭǎПťàǍÂȣLҞȵҜɨǄѢϵȄӼÑӔҗ',
                                                        'value': 'О\x99ʡʠѡʨĿӔʝïԗƭϊЌüƟĵļÎˢԎ˒έҔӚͰ°Ԣ"ҍ',
                                                    },
                                        {
                                                        'key': 'ƪȑӕĔżйϐRăӮƕěğȅiђμ!ôÙʚʯϡŌβȌГĠ\x84ԩ',
                                                        'value': '˺\u0381Ԉ®уUϚγΗNԭЭΦ˱DȿȐ˶ɗȜǧ˭ԟȽÈƿeЙϵȤ',
                                                    },
                                        {
                                                        'key': 'МŸJȵ\x87ѽʙÙȗ©óгηӛ\u038bӴɋƤŀƪǽǥʵȌКƬť$ΚŸ',
                                                        'value': 'ĖÍŀǆΖɈǏӴÏ}ĒϑȦȊʢҼζiʭл˰âЁƧʅχǥżĨʷ',
                                                    },
                                        {
                                                        'key': 'Ȳ\x9aŌēύυ"ҹԉԐӟΣŠӑĠҬ\x8eúȈҢŰљыϫĭFҹˍĸϬ',
                                                        'value': '\x9cԩάɄϏԨԦŲ·ԍβʊΌĂӤы\x9cǶɈӿEȅʌ\x99ΔǙËǵˈ_',
                                                    },
                                        {
                                                        'key': 'Ҋѵѵɿ˻ϣԨĆӏɾw΅űqÅɤңǝԡŃnΣāψÅ0ϟ½ŠA',
                                                        'value': 'Λѓ\u038bѯψPʫʮʏjǈëԀʐӞʐΒÒƩáєǞˊΜǲǖҎѺǀ¦',
                                                    },
                                        {
                                                        'key': '˨Ʌʘ\x94ʊɹʚȧӔŮѧÇϺ\x90Χȭaǧҕɥ˭²Ȏӹϑűʐ\x84ЙИ',
                                                        'value': 'м˄ҪÕûЗϝѴƉԍӍѲĽÂȆĿ[`њÜπʞǲΚÀćԮѩјЭ',
                                                    },
                                    ],
                        },
                    'comment': '˸ЍΔĽέԐˉϭtԁ}ǅ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'master_sequence': [
                'Щ',
            ],

            'bindings': [
            ],

        },
    ),
]


class ConfigurationStateTest(unittest.TestCase):
    """
    Tests for ConfigurationState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ConfigurationState.parse_data(test_data)
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
        for test_name, test_data in CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ConfigurationState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='bindings', name='ConfigurationState'),
            ),

        ),
    ),

]


CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'bindings': {
                'sequence_type': 'meta',
                'master_sequence': [
                    'îԢȘȪ:¬бȚɋíԑӗБϻƈΐ',
                    'ҵӯӪȎȺɧ©к',
                    'ԨìҝƽΘ',
                    'ȖŞˏ˃ǶËă˦ϡǺβʐ˹ɖǥʺĻǾʳƲ\x83ȓҤłӢʌ`Şԩ8',
                ],
                'bindings': [
                    {
                            'keys': [
                                        '\x9fʕ\x8aԨνqŤħΜǢ',
                                        'ǮԟĸЖ',
                                        'ØĘsѤȝȞНͷӣƼɹ>ϘԪǐƠ*ŨҮҏ\x83ĀÛ=Ҧў',
                                        'ʖŕ',
                                        'ƢXǙ\x9aЗͼ͵2ˆζ\u038b§ςʤʐǘƢЮӍȁȜԞǺҢȷØɅʻ',
                                        'ʖäOӿțҵŘ\u038bɐɱʻǆʅɠȫЬƉӳĤ*ǀє',
                                        'ńϏĢ\xadˏ',
                                        'ȟ',
                                        'ӠǖϽ˶+Äʟ:ӫËѺŃ¾ʾŘɃʙД¥ҢЇ\x9aȸ',
                                        '\u0379ϏЈxķÏʡǻҔʛ_ъ\u0381ϻ˭ѹʟЦɌaщ',
                                    ],
                            'event': {
                                        'target_id': 'Һãӓ˷\x81ūǸǙμǊȬ\x9aә\x83ҷҾƙȘӮӡτ|ʡӎƴcŦѮHś',
                                        'parameters': [
                                                        {
                                                                            'key': 'ħ˲Ҽӝ\x8bǹΩԃϔř˷Ç',
                                                                            'value': 'ĳɶòʏ\x99ΨӕʑŕϙE\x85ɠĢӨƗȨβ/ʏǆ\x9bǌ҃\x98˶}*ǂĲ',
                                                                        },
                                                        {
                                                                            'key': 'йĄ¨ҨƻɝӫÑ\x92ȡͽĖъăʑˍǼнǐνƚǝӁԟşӴɲ¤Õʙ',
                                                                            'value': 'ЗқɚʦǱԏ¯ҨԬαÃĩк*¯ɞȵƾКɵ¼ӍҦ˼ŻĎƋ{ϟʀ',
                                                                        },
                                                        {
                                                                            'key': 'vͿʺӃ˷Ô˅ӇӤԚȣɯōţǉǎӐʃѐӴĝТǟȌҧxœӌӨċ',
                                                                            'value': 'ȑǽιӱ\x8eӷǮ¨˘őЗȡńыԦı\x82ɶӒë÷β\x9fđȞͳƿЋ˫Ѥ',
                                                                        },
                                                        {
                                                                            'key': 'ѵŎʗǘϕоʄӇѐҔĈǎ˫ʠʙŵϨς4',
                                                                            'value': 'Ȁ>ˈдӖƲ%ҰØҖΆƢͶԉǯ£Ԑ\x8c\x9cӁŹҽҌѺ\x90šǵёȽɗ',
                                                                        },
                                                        {
                                                                            'key': 'ѿШʘɑɄŸΘĝěȔηϏѾјԞĖӔɈеì˸\x81Ӥľȱϸ҃ηϕȌ',
                                                                            'value': 'ˇӍӮÜŬϖЫʁÊˏ҂҅ƹԟ|˯фΧ¥ӐȄȷњӑˡĘϖȸ˷º',
                                                                        },
                                                        {
                                                                            'key': 'ԦÖБ˥ǚňʟʏɨȆѬǛʽŽȑCˀïƬʳŢϽƪѡɢȚϒ>Ăˉ',
                                                                            'value': 'Ҏ˰{ΪǿȁηªŻw½ӹņɓ˂ɧȆ,ρƬ©ҧıď ĝǈ\x9dΤĉ',
                                                                        },
                                                        {
                                                                            'key': 'Ғјӻѣɠĭѕϫǈҝĕő',
                                                                            'value': 'ɔŽőłπҊǃµҡŸʌΙǴϾѼŐƘƑǏʮ[&¯$ǯ\x8bØϒsS',
                                                                        },
                                                        {
                                                                            'key': 'ȥΏū\x84τƃВɛsӼԤŦ˖ĳҔҮӭѯӫAљ©ӸLƑҝϫľήä',
                                                                            'value': 'tόɅҤΣôΟˮҹ\x89ІӮĹƅČУȌƋ?řWʞ˛ēϴ˖ϥZѽȏ',
                                                                        },
                                                        {
                                                                            'key': 'ӄʶ',
                                                                            'value': 'ҲǛҸӕWɡҕYӄćқǵŹƍ9eȸƲѣѰóĔϷӟϳЏҿƒ|ñ',
                                                                        },
                                                        {
                                                                            'key': 'řԂ2ԙdǱčƟȊSίˁЈ§ӄ\x89ĝ¯Ĳ\x80ԞжфФƬͻ҆ĘԂα',
                                                                            'value': 'þDԋńϨɁ˲ͷŮҴïǾż5\x9eԤ˫Υáόǈ×ż°ϵħøѭʓҗ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ÌųѐУƑɍǝԘԚѧΚԖɌʆĒȭƃ˼aΎɐƶĬϴzǤƱѭєŨ',
                        },
                    {
                            'keys': [
                                        'ÓњȋԨб˩xƍүКȐƩ¥˻ǆȪ',
                                        'ȥɓ&ʹǪӔ',
                                        'dʓѼôƆǬː~ǜɲ^Ȥ\x85˺ΕƳӍͲ·Ɇ΅˙ԛ',
                                        'јȎ!Ţ6ЦͲŭ',
                                        'ɞϫ',
                                        '˨ǥ\x9fԀĆӫˀѶȍěАȞӵ7',
                                        'Ïσï˓UœѼƓÃϯʭ҅¤įʞМ',
                                        "ɠƥ\\m҄÷үƱȓ\x9dìŴԬ'ˮңϳώȠηЙɑԞŲԨɧ",
                                        'ԁ',
                                        'ȾƥʖƂȐIƻŽȅ½ω',
                                    ],
                            'event': {
                                        'target_id': 'ѳҥϜ\x93϶ѝѿǧÒ)˼˴ǩïКʐƲųȯʆ¬ÅɻöÓÁцũ˰Ҟ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ӑǻĐрŊʈ\x95˞ȱңŞϩџҝƒˎʱˮǄϪȓ\u038bÝʰȹ%ћÁҡЫ',
                                                                            'value': "ǎ(Ǒż˺҃ëΙ³ȽŒ\x969˗ʜӿƟǿˊ\x82ИҬλ'ЖВЎюȑȝ",
                                                                        },
                                                        {
                                                                            'key': 'vѩƪўҿ˫ɚÙѮγɓЉѥɠƼ˽ȠȣĈҰѤϴ˙ƕ˚˭ǂcΗԉ',
                                                                            'value': 'ʃυǃʖ\\ʿǞɜ(ˏƄƦwӘĦ®ѹԪҷˡѝΉӢ¶ħȠΑÊѱз',
                                                                        },
                                                        {
                                                                            'key': 'ӑ5ƬŜǦσŹű˺Ӻ²ӦɄøͻ ʠω¦ĳ\x85\u0378\x91đƊМЫɇˑɯ',
                                                                            'value': 'ӀǿԟõͲǓѾѹԢÅΚΗ\x8e\xadɣ¿ɮʳѫǌϝфçËùșϷñѥϴ',
                                                                        },
                                                        {
                                                                            'key': 'ӇǌƩыȽȿ`РӍсиȕ҄ǇԏϔԓϚӳқӯШЌΧҼęȜЗԄԞ',
                                                                            'value': 'μѨʮԕʩʬìҷ҉ѬНϕǌǇH%ԮɓǊ˹˱ҾΖϲƻҪѤζϳĝ',
                                                                        },
                                                        {
                                                                            'key': '˗Фɵgŏ˯ƣ*ʧɑZΓĶ\\ʟ',
                                                                            'value': 'ϹʈŽάԨēĒ>ƴԐɫƵьӯљгϕȃʞʒ³ζǞȞƜɡɄºӖҞ',
                                                                        },
                                                        {
                                                                            'key': 'ɄљʧƭǁŦҗæԑэʃğWęɚʑʿӗƓϘѶʣ;nų\x91ԫϹ',
                                                                            'value': 'Φ˄љ8ƽƲԆAԕÜp.˛ŗǛ҉˓ǽͳ;ˈƓϹӎǛ·b˭ÝΨ',
                                                                        },
                                                        {
                                                                            'key': '\x83Ы˵ɣ˰Ŧε¹Ȁǈʹţ\xadӅƳҵЗӛҦnϭ\u0379˒ǽÁa\x88ĭƚҴ',
                                                                            'value': 'ʈҾȨǽҤȩӯǯưċβ˰ȆΨҥ¡˯ϫú¶Ú˄ѾЦ2҉Ǹ\xadŁѳ',
                                                                        },
                                                        {
                                                                            'key': '^Ǡϴʍľsʮӳ¶ɀѬɾ9˱ʹѮέȿЖВԐĒԦ\x91ʩĞлѲуϡ',
                                                                            'value': '·ţˍҤõ ¯ųʪŖ]ȼВǚʑ˂ѹʀӉɅΟӤųʄљŀǯĝƮ¯',
                                                                        },
                                                        {
                                                                            'key': 'Ѷ\u0383˄ҴoЛЍњƉÕιƜÕŹѾɸЌ\x80ɄǼŀĆŇϮ\u0378ĳįĴԩӰ',
                                                                            'value': 'ʪΗԐāĲ¯з ϔɹƽвŚʏѼǥѶѢ˄ǧаɢǊ|ǶЧ˦˴Țң',
                                                                        },
                                                        {
                                                                            'key': 'ɖǛгȟИҥƽƤ}ԫǗʦǫ\x90řͽƤ\u0378ĖэØц¶ƀWюǒА"ŭ',
                                                                            'value': '/ΘҪʠşˡτҕҘϩѾɶ͵¬ҥǹɽΰҊӾΏЉϋӷŨ˼ˑωњϱ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ϼ£ЂżΞνжҚЫĮǋŜϜʋǐɔӬãȚЂȢÙȯͿ3Ϩɸвĥѣ',
                        },
                    {
                            'keys': [
                                        'ȏϟΦϤɐνƝЛԜҹӊ\x86ԑɸɈУǉɼѳћпɓƔŹ,єͱĂĜ',
                                        'ϬțZҾҡɽǀƓȣ˷ɸфƲ',
                                        'іΖɣҒҖԄǂцԪȻƒćԄ˄шƂʇэ҃œȃíȘͽæiӽƞǶť',
                                        'Ϥ{UɎΝɚ¼gƁǻŉɦӌR˲ΨÑŊeϕ',
                                        'қТ-˺˯łή%ĲƁ҃ƲΌ\x83ҟċϙԣӤĥʧ\xadЕ',
                                        'Ԡ\u0380αл-ńMë˱ē',
                                        'ɊҘ\x9dȁԂȠȖϭʴʴǳìʃǫԄϛǸǚь¡Ν2ƸƕÂŋч',
                                        'Ӿώȍӭ\x8aѐǔɑӁҮĢ\x9eϓў¸ŽԜȂǱέʣСъӾѻΔО',
                                        'Ѹ3ЋtNřƌŌ˻γĐϽÿʎҒͱԃȼ»\x88ʱЫĦҊËР',
                                        '·ϿρEŸʲʤŸƸ˂ӗĹεҊѓкɂpɰȡʭ@ŝȖăԖȶ˦ȵ',
                                    ],
                            'event': {
                                        'target_id': 'ĂɊӆԙ\\ʚƘԡħϔ˧¹ɄƺΔŚΚˀϧý\x82Ī\u0382ԕӜЮȫΓÿã',
                                        'parameters': [
                                                        {
                                                                            'key': 'ϝʤӔӑ.ǾŚ˕ĸηƄfƾϡіžőϟ͵®íӵʔtεíԑʰɰο',
                                                                            'value': 'ԏРҔϓϻȖҧ\u038bШɗþѦɅ˨ǚþüǍǥŴ®ñ˓ϡύ¨ǁʘˢј',
                                                                        },
                                                        {
                                                                            'key': 'ÙҊċ\x88Ԣɫǻϥio÷k£ñϔŐĵѰʄ˂ԞǗ¦рëɜӆӐ\x8eˋ',
                                                                            'value': 'ƨRɖԝ\x9eʩx#ɂӑԇº҆ӮҡԎԙΗǱǅ¸ЊҲԠӦњΠʩÝĈ',
                                                                        },
                                                        {
                                                                            'key': 'îȫȳəȑӴҞҸÉɟӞˍӚˮǻˏρCҔį\x91ǃZƨɀñрȪũԒ',
                                                                            'value': 'ɠŦUϽϫʾ¿ŖТȧЮÞͿıƎ҅ǻөђʿҤĿϷǗʎȹȾ³М®',
                                                                        },
                                                        {
                                                                            'key': 'ƸǛĔӈ×"ѭΆɢÆĢ҈ʪƅǓĕʛΙԗˊԀϕ=ˊ',
                                                                            'value': ':ΣǷʼОʳ\x98GϥԋѴȟXӠ\u03a2ҿԕϜȩȎƍҖѷ¶ėěJ§ƾş',
                                                                        },
                                                        {
                                                                            'key': 'ßȎԉƑҌϻˬeѫēԉӦɌυЃіĖƏƇǞ\x86Ҵšơşʷęǁѡԡ',
                                                                            'value': 'о/ρ;\x86þѯЪÕGμȴȻǿʋӦȐȺҘΚǐӠȩӍˬδÇςǡĐ',
                                                                        },
                                                        {
                                                                            'key': 'Ŷѿ3ōɀˏҐMЁƫÂƷ_ђϊПѣ˜ԆɐѶϪӶĝѠČÛ>ӂ\x7f',
                                                                            'value': 'ÙɄÚёҨуѦԫǐжĲŌԓīӣǌ>ԈЫƘ mɶÆȼ˗6ƪΤѿ',
                                                                        },
                                                        {
                                                                            'key': 'ÐцǗɶ˷ѨČϭ°ԅиʖÎӧʒɫɝк\x80ƄΪӸɘДÔəҀ\x84¤ǐ',
                                                                            'value': 'ϧɖӧ\u0380Ҝ¾ѐğʚԬΕGѥ ˢTόkƃІǍΩ΅вŎЗʖғĳЧ',
                                                                        },
                                                        {
                                                                            'key': 'ӣɫԗŞΩѮƒ˭>ӛ|ƸƹȱϔȆѸǻíϙɤˣҹӥѫʄʲ',
                                                                            'value': 'Ґl˒цѵʯύԥʈѦǿӞЂŨʹɫӟҽЊѭҵҷɆәЈ\x8eқ[Áʧ',
                                                                        },
                                                        {
                                                                            'key': 'Ǝ4ͺņnщÔЄ\x9eɩőʛėá\u03a2¨ȅǧǣ;ɝӕýȦaȇ˄ņӪү',
                                                                            'value': 'ԌԠŎѯȩɵľјȤИʪҨɖȶϕϊÓӽόñ˖Ӟ\u0381æηʰɗƱϗҕ',
                                                                        },
                                                        {
                                                                            'key': 'Ǉȸώ˾ȦЯЈхƗőұƦӡ§ƅѣß¹˥ʭ\u0378¶ԉƧ',
                                                                            'value': 'Ɔćɯʑ\x90ǏϺӣǝύΙǒˆΘЋƂƶЈΤĴϣ҇ȠϘӷ;҉Tňʑ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ӝЫїʶ÷ʧƈȷʰς˯ҒʏƊƴǣГĘϝʇѰӪҎҝχϹǤӸ,Ʒ',
                        },
                    {
                            'keys': [
                                        'Ùï',
                                        'ĕĦҕƴŝҚʚϿǛ\x97ҿӼ',
                                        'ДѻӪЌóɡȔǟ',
                                        'ƣϻϨȜľУӎыǽêͷɣʓĨѾ+Ҕ',
                                        'Ń҂ѴΡȎɷѤөО\x86äϫʩЅζIǌđѾţƢʖԔѦ\x94\x96',
                                        'ґɦwʩȠҰǪѧӹӁȥϻѣ˽εϓИŽƭʮJ\x96˰ºʉŎòɓ',
                                        '7\x9bȷϬȝöӼȽȈϷпέǅ·ӥʕϨϙ',
                                        'ŻЈЙuѓĻԅ˩ȥȟɞȲ˪ȯŧʢƣȫ',
                                    ],
                            'event': {
                                        'target_id': 'Ł<iЉÓɈυýѴĈĠəʌȚ˛\x96ʫɦ˦ёLɽȓҊùǕϷˉϣΤ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ďӋьǼSƁҲŻ\x97˔ʃӅΞʊɞӯņ˨°=͵ȳӅȈČϪӧ˚fȗ',
                                                                            'value': 'ƐГåԛЮìӭΉĒƴϒσϳƹŪǪɻ\x9cȖɈŎӵЂŠщ\x94ĽƦʔω',
                                                                        },
                                                        {
                                                                            'key': 'țΰŖĿføҤ',
                                                                            'value': 'ĎӮ\u0383ĵΎҢ\x95\u0379ϊˑPԋȄȪɗͺιӚёЪɸв˚ɄԊõʥďłʒ',
                                                                        },
                                                        {
                                                                            'key': 'ȉѣѐΥϺаҙɷ˕¶Ҙ¸s\x8eȔЖѪдρƯԇǿ',
                                                                            'value': 'Ďʙɦɹʁ\x86Ą˭Ǽʦĳʉ~ȓҨʺЬʱƤ҇ɋβԩНÈ\u0378ǎîȜĮ',
                                                                        },
                                                        {
                                                                            'key': 'жўɣВϐӨϭʎϺҪƣƦѧ\x89ѹщ',
                                                                            'value': '҉ӌoѴѸ\x8c¤εӮġɈΖʈl˖Ăͽwԣɶ®ŖЋԆΧˠЂɃ˻ƙ',
                                                                        },
                                                        {
                                                                            'key': '1ά˂ȊµâҁǘҳҢε˹˓ӗ˨ʳȏҷȒŜƿŮŗˢąҢ*ƜюЩ',
                                                                            'value': 'Ӊ\x9fƽpƤϘɤVÅЃBƻӅ˕ҨғӋƷɞϲχвҧƐͰGͰ²ßˢ',
                                                                        },
                                                        {
                                                                            'key': 'ˑʄν"Өǈ˘Ȳɲ',
                                                                            'value': 'ι˻ĨҚҠʻͷϼ҃ɠҩǽŌǷƢԝӆnɩϟ\x9fȚŌΈɮй˒\x9aёӳ',
                                                                        },
                                                        {
                                                                            'key': 'õ\x89Ĥͺ˰ȵ/ϱЛҰΓǀʟͲ°ʇƣɈçĠΉɰ¢+ъҲƳʦėz',
                                                                            'value': 'ɀЂŭԓҋťóɃԪ˗¥Ċ˷ȨӪèӳǾȟӻԜªЖɽӪƝˡàϢȈ',
                                                                        },
                                                        {
                                                                            'key': 'ÜˀͼŖĸη]ÒQìЈΓЪϒƖĉ\x7fȁԚҘҳЅѬȧ˟ҏįЎ;ŷ',
                                                                            'value': 'DɃДÚ\x82ʣʃ»tšŻĪϯǱlȟŽȻҰėΎ(ϔƇÁӘǡЭѮӛ',
                                                                        },
                                                        {
                                                                            'key': 'ΧèƻêҤˎΠԋıʊȺДʣԚѥΜE;ϫӔѷӏα˰ȅ͵ОȖʟʈ',
                                                                            'value': 'ɄǑϗƧЍɹҝψǤӔőЧ!ȥ˥ƚ@ĵʴ+ҊǓѸɵϪӯƴŌɨ3',
                                                                        },
                                                        {
                                                                            'key': '2ȢȸϞ\x8fĬϗ',
                                                                            'value': 'ӞƯƈƚĈĂΐɮǳŘʍƧІЩʚђȒ\x94\x88zɎԈʏƸѨþ~ɡđл',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ӷѳUƮűƝǮҕůҦœƿЯғƎǎΙϾӳӈàҜʐ˙Иʕ˝ӝƖƸ',
                        },
                    {
                            'keys': [
                                        'ƤʛЮ',
                                        'ɒӨЊ=\x94ԟŅɗ',
                                    ],
                            'event': {
                                        'target_id': 'ʗϿƩӜώƖ˙ɏĭѮј҉ĳǰưʇЀɴȝʿʳƿÕԄɔмŇ˦μϟ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ҮѰɀŹ',
                                                                            'value': '\u0383ɬҨOǛh8ǴŒͽǯɠȰǾҾ´ƍҥƵˊүʧұ˛˒IŬǤяŒ',
                                                                        },
                                                        {
                                                                            'key': 'ŉѦСĦŽÚùɶ˕MΖɓúԑ\x9bėΥï˩ЊҹȨμŶЗƷ+τςѧ',
                                                                            'value': '-ƵћТǏͰƍѾˇȜЕğͰKЈʺÅƖƓE1ѝϻеȢТɸØȉˈ',
                                                                        },
                                                        {
                                                                            'key': 'ȿ҉ϰˮǐͱðȥӃŨѹԟ·ȦЀŵӵӏƠӄĤӅĺϨђҴ˝ªюё',
                                                                            'value': ']øčľΡȺȨӎȂȵ»ӽǮǮϤсΥ\u0381Ʊԉʨ\x95ħӘʱȕӟуɣȏ',
                                                                        },
                                                        {
                                                                            'key': "ӚӌΜХȇ'ˣŻÂӜúĺЁҳҡįãкʷΆ Ŗ",
                                                                            'value': 'ǽϼƭˠаԂıĺϝʖūϾǜ\u0379͵ʶзʄĿʤiȬĕͺҘͽʋΚΉˌ',
                                                                        },
                                                        {
                                                                            'key': 'ʌȉӃҦҵɱǥѿȶȦčѶҠԚӚɵĲůĝȘ˼ǯY\x9eɲы@ĭӉ\x8c',
                                                                            'value': 'ˊñǥǁϱ˚«ȃļşԩҞʶҰҪєɗ¾ȕʞʵĉ·ЊӠ,øƹaį',
                                                                        },
                                                        {
                                                                            'key': 'щǚèJŹўƎɺįрİԨîӧjҖǿͱơǆіѱ˾Ɖʕӄμ\x9fԡԧ',
                                                                            'value': 'ȁħȜȭÝ˭ʔͻñĂа´ɷȲҐƵþÄ˯ӃõøͽNЂӒçӁԆҽ',
                                                                        },
                                                        {
                                                                            'key': 'ъғȈȿĢsӁεň˓ŀϭϗʮƈV*řĤΡʞĲƳŎˍ©²ʇ\u0381ȃ',
                                                                            'value': 'ȜƻɧĐR¸ċŞɫǯǙʀӉȐěŽåȩ ì҄ǂǢɠԞԪŖȰʬҿ',
                                                                        },
                                                        {
                                                                            'key': 'ϤɰЋ[ŅώǠÊȐӊɆ˘ς˨χþϕΎКŬєΕ˒^ŘύТ˛ξØ',
                                                                            'value': 'ѕú҂ӤãȬíǷɩӿū˨Г·ǲŉʜԨʄƸŎżĒμȢ˽ϑѻȼʨ',
                                                                        },
                                                        {
                                                                            'key': 'ÂXǋĥɣJԡ2AГȉƗǹɇˬԠªfSьԮȑ[ȋ͵Шƙϸò',
                                                                            'value': 'σýАųL˾ΪϿǚӾǟиǓŃóɁɮ;\u0380ÝііǴžһχШηΕȳ',
                                                                        },
                                                        {
                                                                            'key': '7ΆϳԞƮ˖űyǽѣЖ%Ήǟǚ¹ѻԙǎǕɣɟ\x94ԃӌſԮɜr{',
                                                                            'value': 'ďҷҘӺϭȈҳǹƀӜÍǛºǬǲŭŷͳŤˋɃΠԟΕ\u0379ԕ˦ҜæĘ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ӲɷҹϗʙӂǱ\x9eȫфʘҰӍ:ѪԡǈӋşΫϸðȈӂđҜȸǰ\x9cӪ',
                        },
                    {
                            'keys': [
                                        '˸Є,\x82MϠУfʏ\u0383˷ ӁŃʌŠ¡ɽ',
                                        'ɯDӹƌƵғ=ʊĒɝʙǍÄВ',
                                        'Њuͷ',
                                        'ӓӮ^ζˢ',
                                        '΄ƬћŚӢ&ӓ\\ϣ˲θΓüсǠΰтүОɆΥþşfʈąćҀʣӴ',
                                        '³ӥȱú˘ÕВыȇѡǂҁȵϴӁØԝ',
                                        'юÑąϧŔȀ˦\x7fƙкʟ˓8҅Ǩ\x9e˟Ύъˊ˄\u0381ξгӺ\x95',
                                        'ǚПȧǰȮĩɳԏќ˵ӔԋҎƼԍȌbϵǾǽҬҧĺҴ÷èƫД',
                                        'Ԃζ:fŜҪɻϻ˨\u0381ȅЮэӖġбӯũǄì',
                                        'ԓĭʸǰȐѺӁʶзɰÏ˹ͿĜΜ',
                                    ],
                            'event': {
                                        'target_id': 'ǎȈбȱӇϭΙдҵXҮȀƷǎƊɲϘŀ\x9eĽȒѯµñҐӃ·ŏũӾ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ğďҜУșΜÝ&ЯΛƮω\x92МӖθŦΑʇ÷ĥіƙӉҲҭǨhҋӘ',
                                                                            'value': 'ɴӃҩҡ4§ҦƸϤɲәˁ@ТΛӦƃЉ6ђƅtԏҊƗιŰTРκ',
                                                                        },
                                                        {
                                                                            'key': 'ҎѳʵǋûďӱӾӡɾʘƎԉ\x83ӂҒԩλԢҁȣˉкϭөŁųrˢ·',
                                                                            'value': 'ԌЬѮɐШЀϹIвȁѰɬ¹Ō\x96ȵĭΩх¾șŧɤÈǦǣϽѷҝШ',
                                                                        },
                                                        {
                                                                            'key': 'ΩѢѯбǰʼŋзXĳǂȴѶǆўɇɖſƿʴĤʗϊѥҬ%ķˣʣ˄',
                                                                            'value': 'ÁЧʧΕˠǖϐȧǦDӚӻЁψԌĵńƑɺȦӯ;\x7fSљƮŲ[юȗ',
                                                                        },
                                                        {
                                                                            'key': 'Øӭ.ȯǭǦéϘѻþҠ\x8dūĦƥϊ#О',
                                                                            'value': 'ҵ\x9aƳΏȢˢÈÄ¶҂©×\x96ѩŃŶцƅ¦ϡƾχԆǵ0Ȼʢ²Īŵ',
                                                                        },
                                                        {
                                                                            'key': 'ɤžȔ˛þʗϖ}ʢ˜ʣҠµȼ',
                                                                            'value': 'ţ(ɺъÅɑɱЩθԪ°ЬӾ;˨˯ҜɉbÃ˲ǈɴƱƦuЮʍĕU',
                                                                        },
                                                        {
                                                                            'key': 'ΈÑƥѧƼ˟ԣҭʙԬѤ\x85ĲȝƢƸzˈ·Ǣ˖ɢΡñɀȌ΄ŗňʡ',
                                                                            'value': 'ōӄηɴƾv¯ʯgˇȤŷ˫СҴέʭøFˢҫĢϫʟѷў;ѷƉʇ',
                                                                        },
                                                        {
                                                                            'key': 'èӔƞƃȩº\x97яÖŗЖј/ĒӾɔƜэÝʢԞ˫\x81ђϤƄ<ҳ˼Э',
                                                                            'value': 'Ԗ˰ʐeЋӀѩÓҎҎϑˬћɉɒǏϛɈ6κJИѰӶǛӺӕˬ÷ΰ',
                                                                        },
                                                        {
                                                                            'key': 'ϒŁŐЄ˞҇ԒåȃƒÆѡʋқӾnɯΖщӻɇєƖҩ0ɎǤ˷˨Γ',
                                                                            'value': 'ӁũǼėȍЉČǷǁɽŗğČԏӝѺӍěѫҿvĀõ3ƒӎ\u0380ϷDÙ',
                                                                        },
                                                        {
                                                                            'key': 'ŖǍĬȥ¤ʢċǋ¦ŝ#ƵΐΝАƅ˧wɗΖӧÃɡ˥ѬȚӣǐъː',
                                                                            'value': '˴ũȁĖĎϩɊƿǢМļӦǚIcʹǿ)Я˒¹ŜĚѱÜəʻˡΪϴ',
                                                                        },
                                                        {
                                                                            'key': 'ԎŽƯȰɴȧ˦ςɓҢƾ҈ŜʊιάαГ£ĵВ\x8eΛˁӓɺɼɽюɟ',
                                                                            'value': 'ҢYЎɐ»нŦϐЦԕҥtѭ˚ЮƴԞƾϺʦêɖ\u0379ЮȽљӠȐҊŃ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ɭ\x90ύʤķϩƉϛǺЬуʚˡϓŷѣӞЪƽҿҪԒĳ\x9cȫ\x7fȦǶÇɻ',
                        },
                    {
                            'keys': [
                                        'ϟΝ\x80ї\u03a2ҙӁχΨώЌх',
                                        'ι˕δЉĭϐ',
                                        'ѳƬ˾ι˞˼äÛ\\ӑӮrãÓI\x94ѳɆEҖ',
                                        '»ʬԧ҆ś½ЈϢԭ\x96ŗ§Ȇ\x95ȟÝMÞőǨԫӕGφϘчÎ˕',
                                        'ÜǜτƊΠĥƖӉĎϧҞѸ&ȝάͶfϔXdɥ',
                                        'ŋǇIԜƆĜ°ǇΠӒŜĩˊɻůʴ',
                                        'ɧҦĤ&ȬҟȘ˧ƾЎʳËÑǹj',
                                        '·\u0382Ƣ\x94ӆġӄƣԢːɱɎ˲ʆσa',
                                        'Љό\u0382ŅľˤЋŮҩьѓέЎôЧǾώѩơǌӌøĈǭѲlјƥ',
                                        '˗ȶ˔UȚ',
                                    ],
                            'event': {
                                        'target_id': 'ҫϜ͵ӶAƬĉϡÌɵƣВӽӪ\xa0ŚїЫͱķЧŪɒƖ^ʎΟ\x8dϳј',
                                        'parameters': [
                                                        {
                                                                            'key': 'ǹϋ˽НѡҬѲǴȺȏӂĕԍʥ˜Ȗ·Χ\x81ªɼǕȀpń\x91źΪǅȌ',
                                                                            'value': 'ˤԌȐȇ\x9bϧΖȒVҩɘΥѠӄó˫ͲƥȐӽҹϘʂԭҒӣÕśΫε',
                                                                        },
                                                        {
                                                                            'key': 'ԧИHá\x9bΘÂ¯SāΠĎȚ˙˾Ƣɫōfͱ˾ǒηʕсӊоűƒŒ',
                                                                            'value': 'ˬӱɮͶ2ДĖȉĐϩ:ӨȠѿєuʕʮ҃gķѸйƔҕKûΨį\x81',
                                                                        },
                                                        {
                                                                            'key': 'ƭϚĹИΆʔˬ˝ýеӢƐӏΰäЧŖ ǋϮи}ж˸ºνƊÞаŀ',
                                                                            'value': 'ôҏǙBǒ˶ǤȁȂ˅˂ƱҜМ˵ѦŁɋћͽȓ©ǜɓїÐҋɉÄɫ',
                                                                        },
                                                        {
                                                                            'key': 'ԟϯ\u038b',
                                                                            'value': 'ŔмҴ4¼ёЇϱ΅ͽİ+ÃλϓԡИ˹ԟƍǥѯͰȼťОˉɥ҉Ҍ',
                                                                        },
                                                        {
                                                                            'key': ' Θ±σͺŲƄiˡǔԔɻ',
                                                                            'value': 'έӨԚɥҽǄǙΟɪàԦ\x8bəΘѡǍï˧ϟYѸsҺǆɗѬϯNԜ¼',
                                                                        },
                                                        {
                                                                            'key': 'жͼ.ΜΒĺψSĎдȥѯæρЩұȂ\\À.ȌϗцɄŭ҄Кȍa)',
                                                                            'value': 'Ĥо\x99)ĵƟҌԔ˒ºΘиŉџɁʉɧŹҲҝΰҚȍ˾Ϊάϡś¹Ѿ',
                                                                        },
                                                        {
                                                                            'key': 'ɍЀ¯Ж\u0381ĞǠшƙ\x9bͰŻ\x89yɔ',
                                                                            'value': 'ʳԎĻĤΌƩ®mϐ·ƇљӧȹƐȂаγǨȲzǝӦčϋǼ9ӶǗĉ',
                                                                        },
                                                        {
                                                                            'key': '¤ѢКȹ',
                                                                            'value': 'ɓγʠƅɗʜƕ˫ÐˎɯɥѧͶЭπÁŻͿŲrŻÕŅК&ǞԔǇȼ',
                                                                        },
                                                        {
                                                                            'key': 'ʬЇԏԁӞŢ>\x8fУҕӉĎɡKĳӖ',
                                                                            'value': 'ύƍǭ¸ʱÅJkͷЈʄɵąϺӶˆюϡͶǩʤņĢŎŗɉQΐԛП',
                                                                        },
                                                    ],
                                    },
                            'comment': "θҶӮÿԡԮΨ*ΦΕʾō'ʤŤąεǨУҰŹʞĪԈΎԖĿёƫě",
                        },
                    {
                            'keys': [
                                        '&ˍ±őˆ(˂ҕ¦ȉź1Ҩɿʽ»Ԑ',
                                        'ũȈŉʧǐţƯȮ',
                                        'ʞҧͶɕѻӒ',
                                        'ЇӵƤɎҳěÞЄȼǘˣZŽ¢8і',
                                        '¢Ώκ\u03a2ŕ',
                                        'ȃjͲɌßƁJ˗Ʒˍ˥ѪŢōơΡǡύƢ˥ПͳΏ',
                                        'ӿҩĬӢ·',
                                        '\x9aŶЍĦkηΡɕŧЋqA\u0383Ԏ',
                                        'ʐʇƉӱ҄ҒüʕԀΓͱ҉)ϞѥǗѭŕҬΔʨó˼Ͽ˓ԬƼ',
                                        'ȫкɶѵ>ӦӄŤҙˠūɉ',
                                    ],
                            'event': {
                                        'target_id': 'ɐǔűԅ"ƐɤȹςқɟιʛɚӣzІўΎɢг\xa0η˟ˠϿ϶Ɏʨʇ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ƑФɇ\x82ʵϡʽ;ΙΰĭŠʊǬҔʒϞƘύԗӆɂɺqʮŚюӟšԈ',
                                                                            'value': 'ӕԢǹĽʦ˲ȶӋӝĬЂʷʷҘҠƔɆĮ)ʍԌńЧπŚѺƥ\x96ŲЄ',
                                                                        },
                                                        {
                                                                            'key': 'ɇƘԢțÕ\x8dжů˙σƝӷ/Өȝ\x8dԎҧɘɯѫˢԪэźʜԢͲΑǚ',
                                                                            'value': 'ȝţйӅԞűȼȹƠ<җѢϏˢϳԦ¿ԬͼõǓ\x8eǏôøѷȠįşϠ',
                                                                        },
                                                        {
                                                                            'key': 'ŗԝˁŗSƱʓξϏҘєǪҹ',
                                                                            'value': 'ǛϏ¶4ƃФφÙĈ˕ÇɀɷŊʪƾєàɟΎ\x93ĸÉȔĶƔˠȘåԫ',
                                                                        },
                                                        {
                                                                            'key': 'şĶRђȵώɀɌЪ(ȐҊаȐĨ҇șή\x85ëԫȍďȱτ˞эŔ˯«',
                                                                            'value': "җàɋ҂\x86ΩҾϮϙϭÊ{ǅ˻ѪżĢԭêŒ)©ɫ΄ӏ˺Øҟ's",
                                                                        },
                                                        {
                                                                            'key': 'ŴԎɌ\x91ӶŚǤʹ\xadõʲ(ɭưɞίŦ\x82Ԯ˵ѭϷΔƾȢ\u0381ʞ',
                                                                            'value': 'ӇɨЙfԥҠѕӻШ\x8eԀʿҗě2Ԟ˂Ψ¯Ӯ#ƶ¢Ƶ\u0382ӿюӉÚƬ',
                                                                        },
                                                        {
                                                                            'key': 'ñқłʇΦƎʳӘ',
                                                                            'value': 'āȕ¦ԌҠ-ɳɠƈы\x81ǮҰԖǼҁ9ʫЮΩǬҨс÷ЌȳɴƼҼÍ',
                                                                        },
                                                        {
                                                                            'key': 'ҮN\x97ԨţŚΉǤɵД±Ɠ½Ӳƛ\x8bΙ\x95Е\x9aǮŝҷôΥ\u0378ɫÓǥʴ',
                                                                            'value': 'ǟЯщ+ƪʲіҡƨŉԚôϥPʠʶǮѽҾ\x90ȬƇǦԨƟʊ¦ВȊÔ',
                                                                        },
                                                        {
                                                                            'key': 'ǾШ\xa0ǺԞѵʲŋĜԋʹѯΘțȷϝӳ£ϟǳɏӓŽίǁȯȲ',
                                                                            'value': 'Úéз˅ĊɫƆũ\x94ŁаƕԗƦԦ˞Зԛ҇ЎƮȴφĤ\x80Ӎ˖јϚΠ',
                                                                        },
                                                        {
                                                                            'key': 'Ҩ϶шŨȢȉԜΕώπԛɸǝǗɗȠ!¸´ŮȚΘ²ȚÿΑҸ˺όƦ',
                                                                            'value': ']ЅλȁxπȮīoƬ¾εȚБЫɺęӤÓƢ˃|òƇȗʏÞґÚД',
                                                                        },
                                                        {
                                                                            'key': 'ZôʚƆѲ˲Αe.ǋиȡėΚҭUԗ\x8aͲ9Ĭ¡ҟωțԠΙɆ˕Ԟ',
                                                                            'value': 'äиΑɓŽɷҺɗ¦éɚҠҺэѸȬû˕ǲ8ʴnƋӦÓʗ»bĝƷ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'þΐѦŁĹʇ˭Ąʖ°5ěęɢ\x80ϜԞаӹΏŧҥǦӣP;ÔȨȹΖ',
                        },
                    {
                            'keys': [
                                        'Ƶ˦ŇԗĮԐ˵Ħћг\x99ǑƇΨÈϿщο&',
                                        'ʛƶЯɘįˋȃoͼȶΨ',
                                        'xć˧ƅΎŨVЗиĨ˾Ȕŵԭǧұîԧ˯',
                                        'ʏͽҨԄ˹Ѽȝ҃',
                                        'ĕŃΪӺƓѴͳӽҟΝСƻǫӓѤӗʝɛŤ˚ԍ¿ɈɃЏ7Ǌ',
                                        '˴˜âɯƬɠÛȽàŹϲDØϯī×кǤĩùż',
                                        '˽{ś¢Ъ\x98ǩĦĳҌԭѵҨɾ¬ȤĠx\x98ӺǝҔԄȧþҵˠєƎ',
                                        '\x88ԂЋ¡ȮÖΞ˄ʔϏȟŹӇє˺',
                                        'ԧ¼ϒӺúǝŀӟ\x82ӰɒˮƤ',
                                        'ɏӘŬȀϳ϶ϩҨԈʠӷĥƞϑƜʾŦǟԫ',
                                    ],
                            'event': {
                                        'target_id': 'Ɨŭʥ\x91ňӇԗԆӠƁŝΊǳĭƸˍx3ԣƇӯƞћќ¾ϱƭԀȪϘ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ɉҩɓЃdϱҌ҅ĿӾКɟƴԎӓǽÌǵςĤѭѫԒϼȎħƇ˵ƇӨ',
                                                                            'value': 'ԕʣʰ҃\x95ӳ\x97ˎȭύŹāœXǺһDј\x93πƇ˱ɿƗ³¸U\x8bÿд',
                                                                        },
                                                        {
                                                                            'key': 'ҿĀʇˌүŶǤ',
                                                                            'value': 'ϼ˛kԕВŷÊ²ʗʡςáЃƴˤʠŭħ|Ьѕ5Џ˦Æˆ\x88ωǧȩ',
                                                                        },
                                                        {
                                                                            'key': '7ȮƧ¡˗Ř϶ƨӉ˾ŌTŊÉοιдɒ\x9aɼЧ\x85ҕĔDХ˻ɯ',
                                                                            'value': 'ȷȆҎЅϟ,ȶƃƋѠŎ˼ďΆЄУƇƝԫ҃ƻμʵ>~ďώ©ȧɭ',
                                                                        },
                                                        {
                                                                            'key': 'Ȏ\x91ϑǵԫĿ˟ԬɓӳЃȇȵɄãǌϗ\x8dŬȣԞ0ˈѣԟоԠſƖʾ',
                                                                            'value': 'ȠУ\x9aeӄӪҩóȈƴϪƻȸƣҠϹÛóҕҦ7żɫɕԈ²ÔԡГѧ',
                                                                        },
                                                        {
                                                                            'key': 'ūҭ˙ԤӻС\x8aƫҬǶŲэ\x9fφɄͱǞ«.ɀ~ÏƹԈķұѳǤҴǏ',
                                                                            'value': 'ğɃį¿ԃ˴gҒƕЀĖҥ˚κҒҞƬdĢˉƘ\x87ͻԙʯљҬƇӌ°',
                                                                        },
                                                        {
                                                                            'key': 'ĩ±ÿҠКΘӧʠĩЬ¦Ɠͻӳǥ:=хєәɻR\x93eϙçΙ\x9bà\x8f',
                                                                            'value': 'Ɣ˥m\x9cɛǎƜǰҙöюíǭАɅǞǸєÜÃƝÁȣpɀѶˍͲȎ\u0383',
                                                                        },
                                                        {
                                                                            'key': 'ʫѢ˞ҝXʉȫƒΈɮ+ӸǚâƿґȤеÖʽŦӢ\x9fʂγѼǪŗσɘ',
                                                                            'value': 'ˤŕǦ^Lāωʙª«åAŰĢʏΧɬ\u038bќȲӊ\u0380ҞҋȂɇҊ»;Ƹ',
                                                                        },
                                                        {
                                                                            'key': 'Ɵž*˵ČΌӒϤαҙƤ˳ǜҡӢĄԟȅÚȨҮ·CҼӲˁ\u0380Ԇ±Ć',
                                                                            'value': 'ԜŻªԨ¨ɄȝûΣPƶøάǩʊÊ\x97ȁңɝяȨМ9ү8ćξЅκ',
                                                                        },
                                                        {
                                                                            'key': '\u0379Ŭϡ¶ŤƎǋaƛҖǂĄʸԛȬӢψiԒhʝУōśǙŊƠԈ¯Ȍ',
                                                                            'value': 'ʅҐŤԂċȎҍЎӧРƌŕt˸ʸѳʳwȯκɜεҝ£ϣ˙ʆɬ\u0382ˊ',
                                                                        },
                                                        {
                                                                            'key': "Ҳ¦ǠΰʱȪМZ ԡ'ăΗϡȎƎЄШȕʷȦϚǦʖɣ˱˹ʏΚ˼",
                                                                            'value': 'ĖĲϼѡҷɟӾʔǉx{ɿϗƵӺѹÂњрƺˑ˽ǕϙĒǶҐԝԩѤ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'Ѱ(ѰúʃȾĕΐŊĘǯ\xa0ӃƗȚѯćԫαʺʮƷɐȵϓżŐɬѕ&',
                        },
                    {
                            'keys': [
                                        'ʈ¦өǔ\x89Ќ҅4˷ŏĉĭCƨƶ\x8cϿи҄ɹ',
                                        'ǦȜ\xa0Ҍ\x89ьδɐЄŤķćŧ',
                                        'Ӈҡ\x8b×͵tðɷʜ}ϳ\u0380MȟЫġpϺҟǮǏȾԡԓŃ',
                                        'ͿӥЊĉϨÐСɧȷɊӆɡb',
                                        'ϒǆɥɡŞǪΎ¶`ÿԭ*ӈ',
                                        'ϤԒʒ«ЌZΡ\x92Ͼȿ',
                                        '·ҙȃĢӂɊ@įΨЊԌľӶҳƝđLƆőšєӹȒЀņmǖ',
                                        'Ӑ',
                                        'ɣΞɠģϯӸΊԎΛĵ',
                                        'ΆϡчĨ\x9c\x8fЄŸ҆Ǎ<ȍȪœ˄ΓćɜɋϥưşдǑоϦ˲Ý˵',
                                    ],
                            'event': {
                                        'target_id': 'ʋϼʽǧ\x8bΏǋǷǈϟγóώϟ,ęˍϬ\x8fπϾə\u0381êЎӝĕͻßҲ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ӠӜέKǞƟ',
                                                                            'value': 'ƧYРɌƁŅӸΘаΞΎϧӼų°ӄú%Ԅ˜жƑԢψƐ¹ϊ\x82ҡˏ',
                                                                        },
                                                        {
                                                                            'key': 'ȜɄĞԩѓӲƃěƹҦ',
                                                                            'value': 'Џ²ƯϽψЙѕ\u0381ɶǞҞƑƴҽŚįӄ/Ƴ)Ū҅ҳĤҼWƼ˰˓Ⱦ',
                                                                        },
                                                        {
                                                                            'key': 'Ӟƪ0ɺѝνƢǉ˚ʀчюӝˊ',
                                                                            'value': '.ͳǫǁҲŝђʩѯВùƁǢϧʸǟ˳ȔԓƚԠ˔ǡɳЍŌӳГ7ϗ',
                                                                        },
                                                        {
                                                                            'key': "ʺʡ\xa0ц'Ǜ˅ҒΑͺѷԄƥ\x8fɯȽпҾı±әƿʹҦҎʦňwЙћ",
                                                                            'value': 'Ũ΅ӽŏɷķkʂ\x96ÂƷӣƂņ˻˕γδͿRǎҊ,ãӲεӋχ\xa0ɂ',
                                                                        },
                                                        {
                                                                            'key': 'ſÆ$ÂŤӒӀСŖУЅʂȭӞXJϽӊǎZɺϸȁЎğːȪ;ʫƃ',
                                                                            'value': '˲ТЫƾŊǂċÝҾ҄źν˂œƚ˽ĘŞԬэɩ²ДƛѱȾ˃Ѱϵ\xa0',
                                                                        },
                                                        {
                                                                            'key': 'îҧ»˫Ǚ`üҦǒκƸҺȄӳЃƕƅɪĨҔƊѭϡ"κʰΔƭłΕ',
                                                                            'value': 'ғхрέǎˊÈЏɯӻȯʳʷΉƅΈχИҾ\x9dƋʨåԬѢ¾ί\x8aǥ/',
                                                                        },
                                                        {
                                                                            'key': 'ԘͽԉЮϷǁȂдєƹǞҎǾʖɚѾќӘЮ əǹ',
                                                                            'value': 'ўŀ˯ǨʑΉðΈғĊĜчĕΊфɎ!Ŏ^˞şɃǰȂȋďɶѫɺǖ',
                                                                        },
                                                        {
                                                                            'key': 'OŜΥњ',
                                                                            'value': 'цљĝϩϩΣƾēɸӗѐȃʠæȚ|ØĐğcϼƏŹŻβё\x93ʹϺƌ',
                                                                        },
                                                        {
                                                                            'key': 'ʠ%ǩҨΓԓԖʔѫɑƢËÖϢΉũŀƬȨӃņ\x88ɛƴу\x9fԫЬ½ʣ',
                                                                            'value': '҈˳σҡԂӟĖΙǺҒǑǟùǨӯ1ŗϢĺǙҊɕɗ®ɒɍ³ƽѤȥ',
                                                                        },
                                                        {
                                                                            'key': 'ιиǕżʀƦԜ]ЍÚȢǓ˱ÏӄūӳʻӔȈҺԚ¯ӏҦ҅ʅ\u0381ˍŭ',
                                                                            'value': 'kʮůΜˣŪρƻͽëΖӷӭŎЏӿĂaƣɬΘˑеӿԉ˛ԘσЕϵ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'UɈӀэ˫˥ͺė_ȘJ˶ЅǘȽÜ^ő˂ɱɅǹ\u0382ǰɇ×ԬǸƦѭ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'bindings': {
                'sequence_type': 'sequence',
                'master_sequence': [
                    'Л',
                ],
                'bindings': [
                ],
            },

        },
    ),
]
