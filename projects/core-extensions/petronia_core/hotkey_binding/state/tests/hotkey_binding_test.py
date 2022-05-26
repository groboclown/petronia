# GENERATED CODE - DO NOT MODIFY

"""
Tests for the hotkey_binding module.
Extension petronia_core.hotkey_binding, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
            'key': "V²ǈѝˠ-¤ǢʹϏZɉѠêūŲ˺ĕΌ'ǳŧҵϒԨ\x84ĎǻѾĠ",
            'value': 'ѫț˕xÞlɏєƞΜƘγˁΘȺńˀ°ɆEO˶ӋʢжĥϝɦΫČ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ϡ',

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
            'target_id': 'Ǽϻ˲MƂhΩƳŊИƪȅɓњЪÜҲȲʼȀиѮɺЕųªÁŐЏŃ',
            'parameters': [
                {
                    'key': 'ǡʨ\x80ѐршÉƫӘ²Gчÿ҆Γų´\u0383Ӆˊ\x80κˢӏǼɶÅ)gφ',
                    'value': 'ӦćɟКЭрǊɫӚÆӉҥ\x96ĦҖŇ¾Ğй§ΤÎȦtÈΰďŔΠк',
                },
                {
                    'key': 'Ȋ\x9fü˨ӹÔΗìç+Ĳ˲ʒӼѦǫӁĈȂϵĪ˦ȊҼͿɩ˩ȟˌǐ',
                    'value': 'ʕ|ҡΉŌ˔ɌϷΜıѻАɁ?Ԣԑ3ćԮťʇфέΒ˖θҶҞҡҘ',
                },
                {
                    'key': 'ӹɦѪ=1ɰƶΥɶȳӮ˫ŷ£ϥԫԚЗϴҼʹͳ¸ǺƀǥŸ˄Ө\x87',
                    'value': 'ԣͲĒϜˀĶŁŁМ\x9fТкŉś˭ԍÀĆѻÊяǞŕЛϛʛĢʥȽґ',
                },
                {
                    'key': 'Ƅ˭Ā\x94ǞɓΘȱĜǂҝ\x91ÒìŸ˔Μ4ԄLȜŲǸΚҫҠȪ¹4ɜ',
                    'value': 'ĚɰНĨӲh˒åӭӺńΰ¹\x8dðŚϪтƻ\x8d-ҚɁлӧɄnʗ\x93Ĥ',
                },
                {
                    'key': '˦ɱ˵ˡɃȠsëȻƯɸʹȿ\x83ЁØКɧǳο',
                    'value': 'Ь˭ŋʖaԇќӹӼɳŸǠȅƐʗфĶъЖΌÎΞȋρē"οӖLŏ',
                },
                {
                    'key': '˺åʲӤ&ēŗɰЇʭƘȖʜǑнʳJƋĭԀʠԒρɛјҒEʀȕϏ',
                    'value': 'òƧƜΩ\x81ǉɭƜȧƋĈǻϰϾÉȭΜӹοɣҧпʓЎɟҠԥăЪt',
                },
                {
                    'key': 'ːǦ-зÌЫΌÀȲƛҵȓʂşǟүбÉǩ',
                    'value': 'ΏΞϵĔϟȈΧïѿΞͶ˽҂ƀˍ\x9aд҆ɥƼHʐƁξ>ҁԋðdʎ',
                },
                {
                    'key': 'ϸɑĵ˂ŗԈ',
                    'value': 'ŎÔӚ¿ȑŨ{ʅ˸ȐԙȠΩ\x81ȳӋǕȯːӨѪԓʑĔƢ"ԣîӻɷ',
                },
                {
                    'key': 'ѱÎƴϹГì˽ȍҪԉËξǨ˒ŋȓ[ɆeгũǍҒԊԓβȃԑςǸ',
                    'value': 'žϗ˂ѣģ\x98åŪŌ÷þϻҚǢµԌѫοыӒūɻ*сµӔҼƥ˔Ǆ',
                },
                {
                    'key': 'ҩщǫ˩ŔǒƇǎԞǓɘѼôcÊҸΊаˉј¹˅х˓ƁΙūX\x99.',
                    'value': 'Ӻ\x87µÉȵϙѝSҌP]ƴёЁ϶ΰШӮǂÅťћ\u0381ԨǕҊȒŢS҅',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ÍϒłӰ˽',

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
                'ŅºʷɈыȐðŔͱĝŧǢƷΙƼԞƠҴϬѴΩΨϱƊƺ˾ҵˁӣų',
                'ЏIҲƂԁÓʃӪāϸĕҐǉ',
                'Ȱɪįͳӈӥ΅Ơѡʃʰ,áƳȰƖҵǢԢӃþΨɠʠȔʲϋΡĒ',
                'Ӕµԟ˵ӏ_ŔőˬǪǩͱƴŲӍϩʗӄҺ¹Ϯ',
                'ѝĂϗËĲӪŦϚîΗÖ¹ƊSȥʼ$',
                'ќѴÃĀɥ˹',
                'ѢɫҜɘ˹ϚÇǣϸÚŮƋ˭ԫҒѝ"ƃ\x8aϦÜҠȊ',
                '˥ŮʲξқˢÌ©ʦîù',
                "ˤɼŅßπǢƚƔȰ'Ԉĕ\x9bӃǇŢϞҊ\x86ЫȏāѲңэυ\x8aûԬЗ",
                'ǖПɋƩ',
            ],
            'event': {
                'target_id': 'ŞϋɗӦɚǂųȉ\u0379ɵϯїŤƽͼɈ\x83ɩӼ˙ʎѝцЩÿ;ƣȇшƲ',
                'parameters': [
                    {
                            'key': 'Ɖ˚ȏ4\x97ƺʖXѾĻŦǑħэŘԠұȪ4˓Ǫ˰¼ƺĦԆԀŘCʐ',
                            'value': 'ç/ǚ҆ĢΩĭӪЅ˳ΜƔǪбùʵÅĄňʿҳΈўϸǸrħѶŶҳ',
                        },
                    {
                            'key': 'ʬƐʅɆŮʯ˃ƐǺԑĉĠĤӻȈȣƟÆǌːӿĄЬpϻȻɍȖзĕ',
                            'value': 'ǂżŚчɒς҅\u038bϡԠӁÏʨ\x89ʊƷ\x91ϡŖҞԟûƯτǏȻҗ}ƿÒ',
                        },
                    {
                            'key': 'ʹhcɣСȿ',
                            'value': 'ұĊǝ\x8fxԤӽ\u038bɧѧҵ˓Ѽaĉƫĵü\x7fзӞȇwÖΠГӼșѐʲ',
                        },
                    {
                            'key': '\x92ąϞͳËɁɒҴӟвӰѲç\x85ԕĖàҧϵˌ¼ƟӶрԜk',
                            'value': '_͵ћȠ`\x97ņҼϺ˚Ԧџ/ĴρѹвҲѯȭϴ\x9eÁi\u0378ěƒԝȁǧ',
                        },
                    {
                            'key': 'åˑ%Кɞŉǟ\u0378ŹǉҚҡɝ\x9dÉÚѲ-ˬҾȌɶŋŜɵȅO÷ȃņ',
                            'value': 'ÅτčƓĕƹĽáӹɢÒè͵ĺϦ҅ŞКӮʽϱµʒĔ^љĳĘˑã',
                        },
                    {
                            'key': 'ϒˤ\x91ʣηĊʴwаĎϯʊĮʻұ҅ʣĹ',
                            'value': 'ͺˌŗņǄӏż3 ÌoɉȔʫȲϧИȴĭȵҐȲȷЃԢ\u038dҲљӽj',
                        },
                    {
                            'key': 'i϶ϲGʇҬěΟªʘ7ФµӥŮаСŢǎтνҥΠ¬φНʍΧȼĠ',
                            'value': 'Čʃ<ҖÉEԕӨҬȧǋ·ΟӇӔ˔ʤӸǓiΒŝUņϧȦ˅ʙϣɴ',
                        },
                    {
                            'key': 'ŕTғȂƅƁοȆϺЋĘяʯҙţʨʢóǫǏм',
                            'value': 'ȇԈӓȤԦȨҒΐōÁБԃӜИ˴ϱ3ƒɾΞαĈ\u0379Ӳԟʾ|ЋɬŞ',
                        },
                    {
                            'key': 'ĚԤϱŔЛAÖɭ\x97Ǻι',
                            'value': '½ʲ\x88âСǫĘзˠƫĒʲƇӬђƿИѩϔћȺEɝɿśӜǘԩǖP',
                        },
                    {
                            'key': 'ʐҺΏрш\xa0ɟχʟʀщ¶еΐwǌùӀ\x8dƗӧ$Ѕƹӎҕφ҉ӕȃ',
                            'value': '¼ƏбŏҠƶŶ\u0380®ɀԨIщϡʩѡȹĆӇņïЕȰ<żȓμεЫƌ',
                        },
                ],
            },
            'comment': 'ʷУɪӦԇ Ο˳ĬȰӞұѮ˓ưϹɿҨˮύɖ˚4ʭΌ[НϿƈƒ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ʖ',
            ],

            'event': {
                'target_id': 'ĕƣҒǳϕ',
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
                'ʳÁ\x96ſʾʩϖϥͷ϶ˡԣ\x80jʲXъӘ\x81Ƃ§Ͷ˅ŘЋŢеăГ',
                'ЖĪͻұǗѮʙӵΑƱǫ¬УǥàΜʎɩïZɞзғ/',
                'ʦ˱ğоYΓҡȆǇǗ',
                '#ʙюʷћė\x9fхƓ"ӵԁưςϞЎγŖѸ',
                'ӄ\xa0тąûΊʡΑζͺåìͶƎĝp\x8eȘaѵ',
                'ƌʙÏ˼Ŗƌ\x8dϢ\x82Џ',
                'ʭƌͲҟцœc',
                "·ğЦʔӸɣɤ]'ʺӞӡǞQʇƂSÿϜϼЄī¿àſӯ;Ǫ\u0382Ť",
                'Ʌ&ŀǕŚȷҬ',
                'лʘ`ƕş?ЈŖ˱ˉǍԊǁMƵ\x98ƃҦӭΌmӣԆƴǛԃĹҖ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ƤњūçÒҐďȌʻЉϴʗ',
                            'Ѷӎ¿ӾӢҤȺԫ',
                            "ǊҠʁҀÂѭMӪȘμ:Ϩ'ɤԭϏјӑҀǓѱϳ˾у|ЬϜʌ",
                            'ħȗˀЕȒǽʝǤĸǩѕѨ´ʰш',
                            'ЯáϲʷͰǍӝˑθ\x9fωʁȌ\u0378ȃљ\x9aҌӌЅ',
                            'ёшϫҐϹѦſ',
                            'ϰ»ɽ˜ϒęƏԫá4Ɉԝαȵ:ɶӍ˻Ʃ˯',
                            'eөӣȃƇƭǁ',
                            'ơ\x9fϑĤɿ',
                            'ʃŎеҙʭԖȭмщӣӒпӔ`ϔx',
                        ],
                    'event': {
                            'target_id': 'ϊƁϼЗύƶχļ(ԙ¨Я\x87αӌƀϜĎĭBѡѓԏŰҖDɅȾͰ\x9e',
                            'parameters': [
                                        {
                                                        'key': 'ĀϘѾόӺȒÞƑ҅SΜ;ӒʤϘͿмŲ\x9aǣҵĺԂ˩ɸɚӓǕɀi',
                                                        'value': 'Ş?Ɩ·ЍϣȤʑΟҒϋӠȴԋςҽǼԝʂӊԎҪʝϺ6Ʒ\x8eԂ˖ʡ',
                                                    },
                                        {
                                                        'key': 'įƉԃѮϬͰŠȮ\x87тӕʞğÏɨҌҲ\x9cѣÏϣλȅӸȺȃŇ)ҥϘ',
                                                        'value': 'ϵЉRëԛҩЈ#ʿʃаӗʄ*ŹƄĜɃ)і1ʠĩ˺ͼѐҌ˶{Ҟ',
                                                    },
                                        {
                                                        'key': 'ȏԦcȍΫȎƓ¦ψžХŘӺÙ˼ӰȾ˨ɔĐ(љҴϟԑʞɕҬŷ\u0379',
                                                        'value': 'тƕ˦п˂Ë\u0383ãbůϳƂԉCΗ"ɢӀ½ħ;ưĂϗĸǥç¸>Ϣ',
                                                    },
                                        {
                                                        'key': '\u0380ΗΦϗҙ§IɹӉS\u03a2\x85ˈҝtſ\x80xБvŷũ\x9cʩˈHǳƥȵϸ',
                                                        'value': 'ɯǆǳыŶÛºĈјĐŤρю˓ƱɕǊрȠÚʭĎƂԟϖěŷƘƚˈ',
                                                    },
                                        {
                                                        'key': 'ӦȰȫąç¾¼#ϚėΫͿǇͽ¶ˠӽɡёȒǧ/ӊȥČʊĈϳ˯Ī',
                                                        'value': 'ӌǅǊŹʃQěЭ˹ɒҷӌɕ¾ª\u0381ͶʰƳԮѝãКϱЋӐӄPęʙ',
                                                    },
                                        {
                                                        'key': '˸Ěʼφa˵φѽÚė',
                                                        'value': 'ͽɚɽƱӹ¾ķ˝ğӻˋʢҠѦŷβƒŔƏÄśχùÂʆSƦԢİʿ',
                                                    },
                                        {
                                                        'key': '5Ӧ˽ŏʚΣѢĕŴзƂёǄǂȪĈԪύ\x89ԭƱ˧ӁԌˢƥƾȫºҿ',
                                                        'value': 'ǁ\x9făԉĂрƦҁǱПʅРĈ˩ѴëŸþхΜȆżӈLgџůZɎϘ',
                                                    },
                                        {
                                                        'key': 'Ԃs\x97ûґTәō?˛ююƸʄnӎԫȪƒˍʯƻ˟ѽơӓħ϶Ңɰ',
                                                        'value': 'ӺόνʚĘɃңøСeÐĲ˷ƯʇХѷïЬőҞ΄-ŪԝӿĹŁͳʡ',
                                                    },
                                        {
                                                        'key': 'ӸɮϦƧGţљ\x90ѥҶԉǺȇʞӼɪĶ˗ĀǌŚČγЧˎҷÌȸȸ¶',
                                                        'value': '%ӭҴэͳƠӂ´ĴҙɮнÁȾŅDʱĺ˔Ďӊϓ¬ɊЂԐΎŪ÷ϱ',
                                                    },
                                        {
                                                        'key': 'ԃΐǡǞÊΝǭҚǷǯɰčǠˁΠȡ¾т',
                                                        'value': 'ΪGӣƊÆȁ҂Ú1ğǭԞԔˋҩZã¯ƄFлҴ ʕ\x92\x95ʓà\x99Ӑ',
                                                    },
                                    ],
                        },
                    'comment': 'ƴôθƌѯ®ήЈл~àŒӃˏυϘċ}ȜЃƽÊҰƪłӴҎӑӌː',
                },
                {
                    'keys': [
                            'үшӺЃ(ƯơξΛιUʂ¡ϞϠƈO',
                            'ʞѮ',
                            'ŬӪ˨Ĺ\u0382ӏȰ,ØѤr',
                            'ʟѳYюԧ\x98\x92ϫ7ɻÓэ«ΒӼbɫŖ2ӽΟµǯϽхеЀ˝Ȏʬ',
                            'ѨЦƵ\x88әÕǷсʔ',
                            'ÐƶæǇα\x88ϐԆԙјӎƪ',
                            'ͺϋΩνǨÙʲǷqӂ',
                            'ŲƦϰbŜßԥǷ',
                            'өÅЕƊŘ\x85ъÌ˜ɇŁƒσɮđÍЭĨ\x96ŹʖьŦӦʭ',
                            'ǐςɿáĨҪƒðBÂEϡƗƴԕ',
                        ],
                    'event': {
                            'target_id': 'ʨɷƨɴѫįԝЫԍţŽǾʐ\xa0΅ŰƷʐĂĄϹȱ\x91҄˖ƃЉáOҮ',
                            'parameters': [
                                        {
                                                        'key': '˶ҐӹÄɜĘ9ŪʑȉĻҏ?˪½ȼƶԛӳÀ˗;Þ',
                                                        'value': 'Ҙ±ѱïõʎϙ~ӝŻжïÑˏς҃Ȋ®÷ʉĪKǢѦч˓Åδӄӹ',
                                                    },
                                        {
                                                        'key': 'ˋӌњΨJg\u03a2ɚ\x9eБҤƑİŐŶvџќƅԩĮÕƗd˩Щǚǚӈӿ',
                                                        'value': 'Φ9ӕЎϗ\x8cĉ\x8cƀЗƉǶʥĢͽǒQ·ӅɩԣϐɷĘĀÖ҉˩ʎǭ',
                                                    },
                                        {
                                                        'key': 'ƿŁsʦňр',
                                                        'value': 'ĻĈԛSşѪϿ6ϏǉӠˍìĢʘͷɨ\x84ПӫϖаDõ\u038dƥ\u03a2Ǘͽʕ',
                                                    },
                                        {
                                                        'key': 'ŉ`ďηȋň˙ҙά\x97ӾèĿʶФæҷϩʏ˔ҞӭΒĘҶɁȩɍͲȋ',
                                                        'value': 'чżώĒχҧЏŞüӟɦҢƷȵύΰӎ\x99ԗŭa#ξ½\x93˜ǣƾӋȾ',
                                                    },
                                        {
                                                        'key': '˨Ԃ\x84җЎϱńʵ˄ǿPņƙȣSԚӬ^\x80Ҙ υͰûƸθϗʣɫυ',
                                                        'value': 'ˊкmӂн¢ŔұӲĖ*ЯǠũñЂȫÐΒˁ\u0382уʟěxѷ˲ńǲΙ',
                                                    },
                                        {
                                                        'key': 'ʴ˺əƨЊǘЬҩиȐ',
                                                        'value': 'ǧмӈάƮԮ˔ƙǭɌŤѭːХѢѭӇ°ϠśӥλĸȀȠȥȮқǷɱ',
                                                    },
                                        {
                                                        'key': 'ŶɐԧЕѣśƴѺįƕĜпěϴƨƻ҆ԨdȼǏӣÑÐˈԃнάŊԘ',
                                                        'value': 'Ϝӂǿ˰3ϽfĜuˌl\x86˂ʤɻӪǖ{ѩҫӘɨЦȦ҈ıÂ\x82ȗ˵',
                                                    },
                                        {
                                                        'key': 'Υ҇Ȕ\x9cΆӸŨȆǨǀŉŇKωȊӳȔȫѲJӴѰŢɗ˙ɯҥЎ<ӱ',
                                                        'value': 'ͼӾôŎɴԣϡAǧËǶƢȫΩϴϣϒҐUβȷǇІŅô˻ƣщ˜ƾ',
                                                    },
                                        {
                                                        'key': 'Ҋ<5ƞ',
                                                        'value': 'ґңρ¾ӻÎʒӎϴӉӴѱқ½ýЎƇȑӪH˕ҕŹʱɁ®ѭĿłƶ',
                                                    },
                                        {
                                                        'key': 'ɫ7ѫѠӿĲӇӷӆdŊɓ\u0379Ǫˁ`ӅeԑěΊ˯ПƈƘƩˌêî҉',
                                                        'value': '>þTѭӰ¤ˍ}\u038bШѨҦҨʔďԂ¯ϵ]b©ԭϏɖƀɛ"ωªs',
                                                    },
                                    ],
                        },
                    'comment': 'ЋöѭŢǙʌɛИԡÇӂȳ\x81ҹˑѥƸ҄ÄҒÝˏˡȗȦΡʊŃъʏ',
                },
                {
                    'keys': [
                            'ȃԉŨ\x8bϻ\x95Ϻ',
                            'ӽ-Π1сϽÒ',
                            'ȹ˺ԟUʊΜ\xa0ɰηһԏҎқѕм¥ç',
                            'ƆΚͿ',
                            'đeΪǤ)ǷӃ΄œĕҷûɛЈɳΰKҳˬЀƼϛïˉН',
                            'Ãѿ¨ѳȐ',
                            'ıΜФɧñˊ²ËЍх˗ǉ',
                            'īԠgɪǃűȯʒρ\x85ѕѝμͽǿϲҦ¤Ӝʠ\u0379ԦÈƍЩ\u038d',
                            'ǾɀƅͰ˔ɫҍç\x86óλʿӼЖ҅',
                            'ŞӳҚҼѝŠӼͼɤͷ«ȩ\x8f˂\x9dɌЭд\x85Ыǰˡбˑƴʇȅ',
                        ],
                    'event': {
                            'target_id': 'юɡϬҜПĮΘʽɽЊ[\x9eΝϵʬʲ˰þѮ/\xadҷÄƊyʁĲʕτӝ',
                            'parameters': [
                                        {
                                                        'key': 'Ͳіğ°ΦмVѳȁÂƘǦ¥ǹʳȨɄ4 ӐгɲǊfłīҥʀųӋ',
                                                        'value': 'цιёʬҗ˞ĴĀ®ϛɢΉŬͳ·ЕНçƠҟʛʐԅ˓ǐЯӌІ%ş',
                                                    },
                                        {
                                                        'key': '\x9b\x9azĔ˽¸SΈ[Ìʘ\\ʲȴˆΛͺңҙԧΑԉÓǑʽŋʔǕǡQ',
                                                        'value': 'ӯʅKƣĉĪɵѳŠҢоʿҠʷý\x9dДЮ³ʜйҕрǙĥÛѮсƗÍ',
                                                    },
                                        {
                                                        'key': 'ķΰ',
                                                        'value': "дl\x98(ƤǫƼϞ£ƶ!˧ĥɿ'ʝͻʬх\u0383ɹȟǑѷĳϯʧџńͿ",
                                                    },
                                        {
                                                        'key': '˭ͱ×ѩѠĀ',
                                                        'value': '\x8c²ɧϷVӚΑǿʅfǷТЪ˞1ȻϭĨΨ¹Ƙ˜˒·Øȇїīɬŧ',
                                                    },
                                        {
                                                        'key': 'Ы˔ŰђȦoǚΤȟί!ʠ¸²Ϙ˫ǆˉӝIЧΊŚ˻Ʈɰɵʠʭ/',
                                                        'value': 'Ҫ\u0378ҀłЅӌ\x9dƥԠԥȜѠӋ\x89ʑȣʑ\u038b©ű¿ŴɕvʄYĘŜɲô',
                                                    },
                                        {
                                                        'key': '˾КȻƚņӾΎȈ«×ȵұȐӓʔțϑɏҲƄѲŌȖʧěŏѬ҃ћɂ',
                                                        'value': 'MΈԝƔɤԦÏτν˅а{ΔeňȔόűʂƿЮɮοȌŘĘȋ˸ʴƏ',
                                                    },
                                    ],
                        },
                    'comment': '˲hʋϵʓ>ŃπԨЃąсδ \x8cԟÞ˖˝ͰȺ¼ӵ<˾҇М҆ɻҵ',
                },
                {
                    'keys': [
                            'ʭΉÔӤûͽƦùnƜЪҁ˧ӕʉбӊɮŎѝʜǃǓӡЬˉϵÐ×',
                            'ĨӑǄыƋÄyĂ˙ζœLŭӽɵŨ',
                            'ͺ',
                            '8ЎǙ˼Ȝȷʘ§\x82ӊ\x91ˏҠģ˻аϛϦÖόÀćӹb',
                            'ҩ\x8cϾ©Ιÿ ѭЗÃ',
                            'ǘʅͳƕ',
                            'Ǔ˶ȶưĤȊɔuvȨǓƾ`ǒʑΨҒҞϐËĖĎ$ǇԂǗg@°ҩ',
                            'ϊϔóҍÎͰƠ˟JѽƩ]˹Н.ĐɦʅƇb҂ƃԭʾӬ˾',
                            'ÌԬΜЯʆŶʴΕ',
                            'ŭұωЬɳԑƶǤґГӨͲυÏǏǾ',
                        ],
                    'event': {
                            'target_id': '×Νԛ˲\x81fҘƇϊӋΊЊŉƽсȃĆӻEǟәͻʴт{Ҧѳɫļʂ',
                            'parameters': [
                                        {
                                                        'key': 'ʩϗȀČ\x97Pʂ\x9eϟ\x91ϗȰINүɝѯƄϭźоǐȅВɝƛԤϨ W',
                                                        'value': 'ОɅʟːвȽǀŚƒВͲƘşČҭ]°ј4ȩӷ˦ΟҵҒʢË#ӥʝ',
                                                    },
                                        {
                                                        'key': 'ȴэҾ:˰˷;΅ťǻϼǵΥǷhͳ˦Ҿý©ӅĊϽʹǪϢŧӺʹҪ',
                                                        'value': 'Ѫǽ³ԧѥҨȼЧΐɲВƽ˙ªçд½ɲԐψëʙŠɧʞ\xa0xЅ4ĥ',
                                                    },
                                        {
                                                        'key': 'Ү',
                                                        'value': 'ѸЖҮɶ§ĽĸͿÇřƞ\u038dЩɢɦƨѯ±ĺЀƔӒӸҸʵ˛˲ÜģȦ',
                                                    },
                                        {
                                                        'key': 'ЀѣѐєŗɠʌȬ6ԐӍȏŠҌØȤȌҍԟȸѳ˜ҷŎƵϡˉѠНѰ',
                                                        'value': 'ʗŷHʄЕ©ԟǒЗȏǪҖӷӫо¹ɜԂńҐ\x8eȾQɢɻȣʿ˸ǧŜ',
                                                    },
                                        {
                                                        'key': 'нҠѨȾԭĻχ\u038dǁԇ҈ǽ˶Ͱɟȫɇȡɾσ\x8eԪǫǍƽԡͼ\x91¯ý',
                                                        'value': 'Р³\u03a2ϒ\xa0ȽϾɾӏɷ\x7fҪÕǔȐΧҤʀӞ\u03a2ÜΟԝӀɕͰˉŮżľ',
                                                    },
                                        {
                                                        'key': 'ҫ',
                                                        'value': 'Ѧş\u0381χȲŭėʔĈĖ\x99ŀԠƲ{ĶҬӢшʕʦȵƂРψӇ8ѥˊӈ',
                                                    },
                                        {
                                                        'key': 'ЅŗҢȔѺеϼцϓéΘҰº˽Ԓе´λ˹ʹɯɥЗԬ˨ȜȁͳÕƜ',
                                                        'value': '`ǳɑƐŶóЈpǄӀ^äʻӥѾșϱ\x99Ū¤ýǦӰӍӕôħʿͼ˚',
                                                    },
                                        {
                                                        'key': 'ƈÌϴn¿ϞϗŦ˧ȟЩ\x91ż\x9cĀиθʓ~\x93ȎξȢəľ˕~˚čю',
                                                        'value': 'ϠϼɍǔӮǌѵƠˑғɵ¶ԕǚåӅŊĥĩɢΉϟ͵Àѓӝε.ĕƊ',
                                                    },
                                        {
                                                        'key': '\x98{űԢΖҺÒŒʀқȍɬԎȷĒǕʤ˂Ϭ˰ѱǞΛȸҝȼŨΡƄȱ',
                                                        'value': 'ӊŽȖğmɼÿzļǅЛЇǕϝŻϣΝԍ]ā˯ȰǧZLӳĬˁǭȮ',
                                                    },
                                        {
                                                        'key': 'ƦΠυ\x9cѫˣτљǼŠŧҝ\x8fʗʷƇôřԄĩƂ',
                                                        'value': 'ą˭бʒбТǯȀЁтЂŶϤǺh§Ѓ\x97iώɶƙԂÏ϶ΘpӬȗԔ',
                                                    },
                                    ],
                        },
                    'comment': 'ÈΓ@ӗӷϪǴҹɇǍʊ˂ɗÚ\x8b˒ˤԨċɴѫƳL8ѣϻţWčʓ',
                },
                {
                    'keys': [
                            'ӤžˋǦМɂƆ',
                            '\x91',
                            '<ΨнӖϗ˙ɷХѕ[ùѵҽŹ\x88ӳФӸԦοȻƖŰ˧ʝ',
                        ],
                    'event': {
                            'target_id': 'ϒĚƙӘʳɋӵƵϱȕѢžҐϥόʒɶӪMςJƗӖĺʰϑĤӂőĈ',
                            'parameters': [
                                        {
                                                        'key': '6Ы҃Ԋ¤ƝѰǃ;ˋĺѭȜЩBŨӀяӺͼ©cӂƩʷŵ/',
                                                        'value': '\x8bҀĠ(ʜȈҽ$˰ǈĊÌ¬ɢ˅¢ԨʬǯʫτϱѣμɱԦ¹ɇǳԗ',
                                                    },
                                        {
                                                        'key': 'ЭȚͱǠХɺʼҘţ˪˖ÂԜƳĚčɉȂ˥ѤϓЍȴĚˠìОŋˌ\x8a',
                                                        'value': 'νɠħӺĕʹʲӒƘʀŠŜĠԂҝΑ˰őǺ˟˝ҽĢɷţƅ®ѸΦǘ',
                                                    },
                                        {
                                                        'key': 'оӴż\u0381ƸԞǣΑȑˍ[ηЍϼBԓAСνĂȪԬѪ˰ҲʝӎǱӐЪ',
                                                        'value': 'Ҷ¸˒Ɋ.r_ȡƿϛńʊưƬƻϸȆӟûʵǃPˬĜҖѾˠ/\u038bМ',
                                                    },
                                        {
                                                        'key': 'ßUίѵАȍûͰЂιPʁΐΞќ΄Ƿ\x98åLƇn҃\x97ʋƻÇŨȖө',
                                                        'value': '˛¢ʀ\x85βȒѲÜĚƖ˻ĐɿűǮŤ˟˙ȎʬўǃЖϞƟӕŢ˞Ϗȑ',
                                                    },
                                        {
                                                        'key': 'ўРǐɰшѲф',
                                                        'value': 'ˌĭĢьҵӌƦuÊ5ơǒХʷӰŘхƱɠ!ǚ҇Č˘ɊʁͻÔϤҳ',
                                                    },
                                        {
                                                        'key': 'ʇωōrˡzǑ',
                                                        'value': 'vњ£2ΛҧðĽϮȇżƆӓÖɵqХ\xadÊQĢЎͱҔßÖcϴͱ\x8e',
                                                    },
                                        {
                                                        'key': 'рȅˉЪĈőɏĬa\x8bȲӟƠÒɂЦι ԬUɒŕˡЗȡÆϻʜJҦ',
                                                        'value': 'ғʳǡƭӷіʠΠԗʃǑĂӀêąːņѪÌȪǤѯŝǖǷФŧҵƒǽ',
                                                    },
                                        {
                                                        'key': "ӡ'Ӫœƅŉ\x7f±ùϮӖԭƼѠХYЪƴ\x93ʛӣî\x8fzĳʮɨӟÕ7",
                                                        'value': 'ç\x9bӵȜΡɌʰǿȡԋ˞˼ƬʨŐȑɭ/˞ɟΝɲҡҥɋϨųƥȃª',
                                                    },
                                        {
                                                        'key': 'ƿȑɎúʙŹZĊųԚƏȤĭҪӚîŧŉßӲϦӇМȠˣӐқʎуŌ',
                                                        'value': 'ЅÖ\u038d\x9fӃˡԨǄçʡϜȂџʘȍQϘʿÀӗȔҳʯӇεǲӟŎϞԋ',
                                                    },
                                        {
                                                        'key': 'ơ¦ϺnĹǲ˓϶҂Ĝ¨RҬК˩Ϟгǧ\x7fɦˎϘхφш5ϏͳʺΓ',
                                                        'value': 'aʾƑжҠάŧҁϚˏÛ\x99ҿԏӄʩ°\u0380ԄĄ˝ХϕѠѓϠÚTʱɩ',
                                                    },
                                    ],
                        },
                    'comment': 'ϜġҀƷӣœЁʭѰʰԤĶԫƳϙǸľǍӯӛɀϗъӼϩұЅ˕БŻ',
                },
                {
                    'keys': [
                            'ƠǱ&ҽƣĴĚːȝѣϔӧЧ˞ϩ&Ɉ',
                            'ѐѸñʶǸƲçϽΛӬ˩ŧ',
                            'ƽϼ҇ɗ\x8aŶМϡŬȽБbσıӝЮГ˅˖ϨʠěӳǓμƛŋǈäϿ',
                            'ʪ¾əюϸΦғƺȨ\x7fΜ҈ƶ]ėσđҤQ',
                            'Ӌʴӧóüɐ҉ǩΚЊҽXΞL˶ŗɅԛ',
                            'ʹ',
                            'Һb\x95ԕDƁÀēϣĴʌϵɧ',
                            'ʗƏʴHʚҼĽӶ',
                            'ѡ\x90ԗӃŉʒҒϟ1эЈьӿ',
                            'ѥǤӿӺȺĎj',
                        ],
                    'event': {
                            'target_id': 'ßԡˉәɊѼưĒȗԞӗ#ȒrϹЊWϪÆǆȇїϦDГɔҭԛnѫ',
                            'parameters': [
                                        {
                                                        'key': '·ӖѻμĽǭŖӦ¤Ң`\x98˨MħAʮñȎòǇĖͷчÄʧď˞ӗÙ',
                                                        'value': 'лό£ȇyĩѭеĊZЏӋβ҉ǝ3й\u038d˛qӅΒȽůȄǜ\x83˅Ůʯ',
                                                    },
                                        {
                                                        'key': 'ǼґɧЁ·҆®DιèʨѼǕ¿αѽѿ͵Ɩ¿ԄǀèƗʶɫ˃ȋĺҝ',
                                                        'value': 'ɣЌҷ:Ͷ¸Ԕž΄Ļ\x9a\x86ĥқˠŰɻßiηʛȓʳʰʘ˛ǻÈͷ;',
                                                    },
                                        {
                                                        'key': 'ƉқԈжÚȬ!ɪŵԣéɻɯΕũƓ\x7fś˜',
                                                        'value': 'Ԛĝǹ˼ΰǲǡƒԪŉˍîȑʑŸлӟԖΊĥҐ²ļɕƧ©ԖŤԩӀ',
                                                    },
                                        {
                                                        'key': '©ʣӶēʘɻӓëҽǫωŤϪMɾ\x93eƢΟȂɍ`ƸӗhГ4\x8eęǩ',
                                                        'value': 'ɡȴТСίŋ%ϮЯVʨPԙӣǫĵʹгь҃ªɍнĄȠΔbӔŗ˜',
                                                    },
                                        {
                                                        'key': 'ћɠ¬ȪĠϽҭ˄ӗĂŻңϼӠ\u0382xƔ\x90ѱơͰϿɀ\x9cϊǜśѭɳĉ',
                                                        'value': 'ǧӕĞɳϩԥȺʪCĻġμɑ¹ɪϝӣǩ˻ҐϪԟϒϻ\x93ʇȝ$ϝʔ',
                                                    },
                                        {
                                                        'key': 'ʑξҖĿƎǫʒÒ˳ȁȘŗΦīsқ¶ÿԥƿłǼˁȭɣɶό҆Ӭȉ',
                                                        'value': 'ƙ˗йΈѳƭʝǣ,ʪ/ӎƜȣεŊǤȀсƁΖμ˭ǇѯqƇ·ŨĨ',
                                                    },
                                        {
                                                        'key': 'rѹȪɐυČҹ\x97ґØȿɧŤƜΫɭȀľϢrӟÈɨЯ\x80ɌA\x9a"ŗ',
                                                        'value': 'ŀӪɣўʞĐҖæϐӆԄҹȔMҦʿŘπǲΌʹЦǻbя\x91ҧŉ\x83ѹ',
                                                    },
                                        {
                                                        'key': 'vП\x9bĒВŏƩżКËɯҡVˁ]ºΪ\x86ѭȶîkē\xa0ʛqԍπǠ°',
                                                        'value': 'ņԂnāˇǠľͶϐѯ҃ҴɧÊ˥Eú\x99ДϤϰƜԞΏɛԛиˈπІ',
                                                    },
                                        {
                                                        'key': 'ŌXϐø¦cҷɋơԑдʞˇĊŨʽŠΰНѾǗǍKţʰԉ',
                                                        'value': 'Řǿвԟˮ·ѿÝǰҊŀʲӠӒȢσ˃ñϦǝƃЧ÷ÏԂˍҴҾҝș',
                                                    },
                                        {
                                                        'key': 'мɗɎ҄ϻȾǉ\x81ӣoҼʱʅԔϪÐȄҭ˰ѥƎоˆԝɠϵâЭŪà',
                                                        'value': 'Ɣɹ\x8fΣLϾ˱ʇȮϖͿȮϺ{ҿ˞P*аҔėčҗъҽҼӇ<ǘȢ',
                                                    },
                                    ],
                        },
                    'comment': 'ƫɎųιãљȹξńrϊԨхĤÔӮǳҳРÌԣí\x95ɞҨMǊӧΡԀ',
                },
                {
                    'keys': [
                            'ɍа҂ɪϞĤϭˢüǡŘÁÔЮИţ,ʕǝƟĉʜӾθһФƫʃŎ',
                            'ȾԩĚǕЬϼC҆Ђ҄҄΄Dɺ',
                            'ʊ(ѽȬĄľʊ˗ľƜτˑʂɷʩǚ',
                            'ԋȅɃӐӌъ\u0380˦ǋͳϗӕҠϻαĘȣ',
                            '\x9cϲεƮҚǲȗ˥Ƭσ-ēĮ¬Ѝ-aωгɜɞ҃ԇƣ',
                            'тƍęԮŧӆȗƍΐÜш+ǨћʅɮϘǖќΛьɘǥˡоӣÇſӀ',
                            'Ūӓ˥ѦғȀǅș(ï?hŤʔǃӒΏ',
                            'b$ģ˓ƭҖÙΟΔưÛʠÜL\u038bԞɠ',
                            'э',
                            'Χ қԪү',
                        ],
                    'event': {
                            'target_id': 'ѕӇΟӭˏЬ]¡\u038djɣӧƝǇſ˨ΕҀ\x8aŬ@VŁжŲǃ#Ǚёϸ',
                            'parameters': [
                                        {
                                                        'key': 'хҁʗȂĝѳҝюƹ\x91ǣ˚^˓ӽ˳ȟ',
                                                        'value': 'bѭƁǫѶǨϳ¾ӟǎüԭÉӍϕɮĆȢƹ¤˗ΊϛԡӧγȊȨªĆ',
                                                    },
                                        {
                                                        'key': "ШѯƷƿǛΡψӃȿʷψŎÞΚ_ÈόѦÀϫԗˑ'ӚМӼƾ§Ņœ",
                                                        'value': 'ЊɑǦŬɼɅːͻɹƬȫʎƔā\x81ӛЪȰɦȮŢɭ\x82ͽ·dҘϿӅƨ',
                                                    },
                                        {
                                                        'key': 'Ԝý´ԄϤǅѳǙξҶԪӞ',
                                                        'value': 'ȈιȾȿwĶ҇Ďɍǲo˝ӳɃԁ&ԇǩǶƞ˃#Ϙѓ˄ĢŬѭûʐ',
                                                    },
                                        {
                                                        'key': 'Βѣý\x9fΪϑǮ˙еʂƊӲĭ\\"ȧēГӐfĵɱԍÜ\x9bȔɽƠɠΝ',
                                                        'value': 'бyƌ\x9f˖öË\x99ƟąķϱΞΆΦ ɛɏӇѢƼЇѡґ˸Ч˟˄γ¸',
                                                    },
                                        {
                                                        'key': 'ʆȃƺˎˎ˨ˎюũϽʹŹҰ҄ѷƩԢкϽ˳ǪÓԂȥɾÂŵ˅љX',
                                                        'value': '¡ĝϻ\u0378şϥlϳӭӚÑ,аǯ˜βDΕgԡ҇\u0382ȠϺäҁ\u0381_ı1',
                                                    },
                                        {
                                                        'key': 'ñҼÕƬPy\x9c',
                                                        'value': 'ˆ=ŊΑɆҶĨԇƖÝϣϳЌɜȚɁЄнP\x91ɤԀÉӑϰɉŝʝӭӧ',
                                                    },
                                        {
                                                        'key': '˲ȏ¡ȀǙQђƇˈȷѺӺѩѥԏԑ\u0379ɂˀɱƍͷ#ȎΫ4Ҙƴύ\x9e',
                                                        'value': 'ӃϙƴИŒҴѯɯkϊʖĈʼàɇЛѳ`ӛАˡП#ЭԢϪǤ˸ƻw',
                                                    },
                                        {
                                                        'key': 'ʈҗźҫӖɊЯΞ\\ήҽa|ηt·ĒϝYϯ<ŷƏ',
                                                        'value': '҂æςҙˍͲБÝӊsϿr\x81ВƊıưӯ±ƀƀüŚũȢѧώ5жŁ',
                                                    },
                                        {
                                                        'key': 'ԚάǾѯЂƸˢĉ\u03a2җ)Ԅ\xa0',
                                                        'value': '¾ϲĝȴԖǝƚΧԋԞɌȫɫ\u0380ЛǌȃǻŅöÌÆç{ʁҳЭӅǙƞ',
                                                    },
                                        {
                                                        'key': 'Ӹ«ʪІÉʥƴɈŝҲЕ˔ҺК¥ϳчƢι\u0378˯\x96ўƍҨӵʎӀÌǜ',
                                                        'value': 'ӀȤϳ}ĄԄȚA!ӴȡŬƺƚƅʯǡĩǖυүŐЏаѲѣ˳ȟǁȕ',
                                                    },
                                    ],
                        },
                    'comment': 'ǱŞǀòΉÕȌÛΌǌŘɉƉӘϨ×ϞңӟŐPŢěвЂԃɑҨo;',
                },
                {
                    'keys': [
                            'ӎˮѱŲ»ϑҚЂԉ?ҧ',
                            'ʹŵϝԛīΨǡҤӥԅÆȟ~ūτƭқùΥԎ.ƷЧҥΝþχҡ',
                            'ĤƙˊúӢ¿ϵУ΅ОȨȠ$ȫɯȔĸsƊΩɞԥԗɯ˾χΐϾ',
                            'ȀŁɺǡȦŝФԟȾӨŃƥÒ˔',
                            'ȦͱĲʘVÑ¢ŇƒεŦǪȨơԭǟΐѽΉćȇû˙Iӎˠ!xѥ\u038b',
                            'ů¨үƏ',
                            'ʥɏ҂$ǀʍƺȟαɣАÖ˱ҩӡ',
                            'Жɟ\x9eƬНǣӻΆ;ƾħ[ԨĚCĻԬĒҒǶΦ\x7f',
                            '·ʷĒѵ8ŨεҦƞ\x807,ϬɭҐЩǞБυȱƜԩͼ',
                            'Fнˁ',
                        ],
                    'event': {
                            'target_id': 'ӞäҨ\x94ʒЈˌѣTĵȜΚȋͱ~τɴӧtҪҺΞΎЉэĊȞÊϱs',
                            'parameters': [
                                        {
                                                        'key': "ʁ0ǚÞêМʁȴêӠӊЁ˹\u0381уȷċȥīѤɽ'ҼιǂӉʃʃϤΫ",
                                                        'value': '\x96аҧʮӠȫȼԚĚҁʩвҸӽԮĚ^ҹĶҡǯǝʰ˹ʥȡΝҬƐȂ',
                                                    },
                                        {
                                                        'key': 'Ư\x93Ĭù\x89Ͼ',
                                                        'value': 'Ӧȍˢқʂ˱ǪΊǏŗӮƜŞùЉńˏï҃Əǰʽ\x89îƿʤˉʅѫ4',
                                                    },
                                        {
                                                        'key': 'Ҁɕ',
                                                        'value': 'ҭmԜ˭Y·ӻƎȲӗ˚6ƻҮ\x8f˳ùʨӧ%\x9b(ƀəίцǱðrɾ',
                                                    },
                                        {
                                                        'key': '¹Ω΅ȔÌϫŤİƊӒɖҐ\u0379ƹ¹Eѳʘɉʸ[PJĳѦӹіʴÊǪ',
                                                        'value': 'ĠԐȰ²}ɅԬԣǀŀϯȄƃɣΦʩVΏąȅЋǹĽԣґƧôʴÌр',
                                                    },
                                        {
                                                        'key': 'ÄÍ˪ЬЏѩӤɁ\x8aƬǱǆӕğǖѩƩũԕĒԮҍԅÐԐЖӡˤÂ¬',
                                                        'value': 'ӣýƃǛĸԐӪžϺǣФҧЯĻ˦ŎΊ\x99ѐԅГӠ˗Ѻϔʻӱ!Ʉӳ',
                                                    },
                                        {
                                                        'key': 'Є¨\u0380аŚЩѪ¸ҏԊͻ\u0379',
                                                        'value': 'ѲҷɍΩT¹˗ͳÊЮ\x85¦ԖSÖпҩĊʸȀȣö\x9fɟ»ɿȌÁǧҰ',
                                                    },
                                        {
                                                        'key': 'ΌǷӚųϫшͷȧӵƽҀ\x8bĉpѰϲTѸλӤ΅jȍ×ħǅǰʦ',
                                                        'value': 'Ʊʲӝ·ŚŻҏΛӎԮԮʉԭ˾łʔ˽ǂàÆΕaе0ҞÀ.үɗʖ',
                                                    },
                                        {
                                                        'key': 'ˋ\x8c',
                                                        'value': 'ŷʣѶŻˎǮЧϐƌкũƍ\x87ũԜƶϩѾϊ\x9dϫjpĸʼҝIˎԖˆ',
                                                    },
                                        {
                                                        'key': 'Ӷό\x8avˊȧˋ',
                                                        'value': 'ΏϫȐϓвûȹbЙǬɚ˹!ѧ˴ɗǁΒɌґº¯ϧыÿȯϱλʂÔ',
                                                    },
                                        {
                                                        'key': 'ӕQуʭĀȊâ',
                                                        'value': 'ӶƸ ãÿŞǍӭʖŠɰƱϧ˟NÀŏІƥѸĻ@ԖҏΐђÁˉϗ˻',
                                                    },
                                    ],
                        },
                    'comment': 'Ì҃ơϰͺƜŴǙŕԅ\x93Ќʔ}ҒЯͼĕљ\x9eɖжȕ;ʲʹǢʁˈԣ',
                },
                {
                    'keys': [
                            'ϵϬ¶ɮ!ћ',
                            'ǌӭȺôȐȆиĪŨĦOҴýĞϬ˼ě',
                            'ӎÑȑӱ',
                            'ԎӞҐŎДӛ}Ó',
                            'Ɉ˘ƬђΣįĔш',
                            'ЇёæϑĕǾ˾',
                            '˛\x98ƃɉϮɄҩФӨї˧ѸΔΰʛƓԦÓΦЌÉő',
                            '˷ƻȴƻĽҒmԣyЁɠĆȺ',
                            'ǾɤϳӜԅ.иϵáʋӂǍƉȗЂŪƋȝĤЧκ\x98ԜҭɔӁĳ',
                            'ʿ˻ӗΖӡχ`˷ĥԌm',
                        ],
                    'event': {
                            'target_id': 'ӰΨ@цȆàƎʆӕ\x82ҩģ\xa0ʹҁяĈэʠ˧Ň\x87ЇӳƘƅJýӉŞ',
                            'parameters': [
                                        {
                                                        'key': 'ԫ˚ЏʼǐԢȆЈʚӥϗΕɬӖˈ',
                                                        'value': '=ȟųͼ˱ӝóόǬѸƲŹНԫ\x96ȗŦ\x99ǆԊԅ҈ΣʉӰ/˯ʆԢ\x85',
                                                    },
                                        {
                                                        'key': 'ǆҭɂˍѠ,Ľʧɱ˗ûǮɨȩƐňžІќ˦ʬПӒ·҆Я˜Ԡ÷Ԁ',
                                                        'value': 'ɼКɐҠәѾÚ\x8bɵˡРªĮҮɐο˒Žљ˳ɮѯΚŔҷǖ\x95Ĭцӆ',
                                                    },
                                        {
                                                        'key': 'ȈǤ1ϷPϽżďўƚ˛ʯҵɍ˝ūWƱǙ(ɶԞνØOɲǪɁĂp',
                                                        'value': 'źɳÛɜкβɂͽѣǏЖȫɤȶ˻ҨǪƲħβқǔȾҚƀɏΘԙǤϬ',
                                                    },
                                        {
                                                        'key': ' ˤuʜčȾҗǠ\x93ТƅmƽǏǵÅ҉ǧƷ¡Ȉȍĭ˽ӕęǣԝƼɨ',
                                                        'value': 'ĴJȗЯ҂мŧѿûʴѳNĽĵłζӵ\x95Ŝ˓˯БНʨɐԡϠ3ԏv',
                                                    },
                                        {
                                                        'key': 'ρдʏʰʊӐʎ˜ǼЀ\x90ʟӞÎƿȃȮԞˏӁϚȟ˚Šʡɀҟǜƥʽ',
                                                        'value': 'ĴİǕҏâťǧɒҳƖϡɌɫрɗτʽ˪Ы\xa0ĬǴђĭǃпjƁ¸Ŕ',
                                                    },
                                        {
                                                        'key': 'њЅӅƙҁžʡЎħʪ\x99˞ɔfƻͿшȖ҅ͷɹưѰǆʝˆΐ˼љ˳',
                                                        'value': 'ϗ»¬ƥґS÷ԡĦϞӽńäíȕԮɩαԭǫ£ǂ<҇ƍͰƋқˤ*',
                                                    },
                                        {
                                                        'key': 'ʹгxƽʏ\x9aΏüԥŬӭƖέɮƓʻӸҗɚ+xґˬʿĉʁԔΘмҪ',
                                                        'value': 'ҮǢǦԘʇǉϴnҽƷ@ϏπԓÄƿÍȺѦĆΪɆƶĿRɫѦǎɁˤ',
                                                    },
                                        {
                                                        'key': '\x96\x99ѕЌˆŧԭȭĒ˄ƃѣ',
                                                        'value': 'җϩωƛһµΞϓƲ\u0379ͼȅʚҠɶԓ/ǂъʁƊ΄ǣʼBőϑP.Ÿ',
                                                    },
                                        {
                                                        'key': 'ƆηºɾģȮ',
                                                        'value': 'γϺЋ7ɟԈѮ}ϷƃΞʁ˔ʁ\x7fɥѮӆ˹\x91ŔɦØкΆPѫ҉Xˀ',
                                                    },
                                        {
                                                        'key': 'ͶӯsԠkԚġǯВ÷ˎfȃɣЗѢǩɟüϫȆ˰ðкȪƂ҅ЏҚи',
                                                        'value': 'ʷ\u038dѠνŵůϜԉΗC<Żɽɖ˺ȕѮˌɕÅǅыʆ¾ģeɕκ˺ӥ',
                                                    },
                                    ],
                        },
                    'comment': 'Ќȉʃћýр\u0379³·iĶãђӎԖ\xadЍĤĮѲӛăϯNψʙδϝĠѷ',
                },
                {
                    'keys': [
                            'ԤđŐȱϩʃѤʟ\x82ĪҝÂþ3ˢɓɫгŮİʆůйԍʀЛԮåʉӾ',
                            '&ҭ˂ʝѼҐÑйΠǷÖʟňĵѹԨƯ',
                            'ҧ;ώ¨Ј˧ψԋΈυѐ˱ʝмī',
                            'ίԒȐƒǀЦßΗΕо×\u0380ҋκ',
                            'ӪʻǬʕſ˜ϑԄϠяŧ½ҿ˓ϰάӕɶԫнσȯѱ/ϋ',
                            'ҠӠɌˤҞƒʴϸζ',
                            '\x98ɐτǿʪԜˣˊȆȫa',
                            'È\u03a2˸ҧ',
                            'ϿƵĵŧͷ',
                            'ƾǧþʹ#ϓ',
                        ],
                    'event': {
                            'target_id': 'ЊÍ}ʄϥʅѵԉшīҼɹγΒϟ˶ɄƄˤΗc˒Ǽ˟ҳɞ˩ȓŪӲ',
                            'parameters': [
                                        {
                                                        'key': 'ʋɽƠŞƴƕэџϩŔͺęΟ҇(ϞИѨΞ\xadƑ͵љƵҎƍǇԘǦ',
                                                        'value': 'ʷó\x90ˎÿǠȼ˅ϗВ(эϧҞ¢ěÅɝϩŋǗˑŜЌ®ѵȇӟѪЀ',
                                                    },
                                        {
                                                        'key': 'ŋәŴѡӶ\x86ʛˇϗÚӮEČЖҌЃϊҥ\u0380ǥРΉĲҌѫűɎѮŃǱ',
                                                        'value': 'ұǽưӨɻҼǞМ×ž4žǲĨϑϭǒͷәȵßсιÆϙæȚШ˱ҷ',
                                                    },
                                        {
                                                        'key': 'ɰČąԮǍȟΫ&ϥуЭƨȝ\x97ʤŐƷϋӷИƹɜӚЧӬвϸΎхӑ',
                                                        'value': '˃Ϫ\x8fƟԣѼ|ǟȸņΌѨȿФɾƘŜʂ˄ɛѼԧԅǿϳVѧÿΰh',
                                                    },
                                        {
                                                        'key': 'мѭĠϭϿǰǿƳԋωѺϚ˒ɄŒŠϣѧȬʐѓѠƸѴˋŵΈҬǬɿ',
                                                        'value': 'ŗπ¥ĥӬɴҮ}ЪϦФǍŨ҃ȥЫʣżɘȪΤȗƥ˶ŹrřαӳӦ',
                                                    },
                                        {
                                                        'key': 'ʗϘaϏ\x8eѸ¼Ҙţ®ʚÉ²Ôѻêҽˏ3˭ѮԞ\x9fΖΜϴ¸ŊӖĵ',
                                                        'value': 'Ͼɪίͽ.ȜҖͼѽǎӿцĆȊНǉʌњΣǱӟӸƯјѻӬϑĒͺң',
                                                    },
                                        {
                                                        'key': 'ǳĐƐϫ҄ΦɄȘʐ|ҍfϨӿʠBϪϙ\x96ѝ˔Ц\u0383ˆ˗ȝњύɗƭ',
                                                        'value': 'ӻȮҌ˫ћşђͿөƲƲ±нөԑКѫ]њŭɶ6ѷγƭǠԋίϞЂ',
                                                    },
                                        {
                                                        'key': 'ʊхʾīƆƑΔȁ\x82ȞnʖӬķŉ\x90ПƲѵΨɋċø\xadҷβʦǻǹ¸',
                                                        'value': 'ʕCĺǽg\x86ҙȴɱЊŀψǺˁжʴәʠ¹Ԭѐҋҫ˭ԀӓӱĕǸ;',
                                                    },
                                        {
                                                        'key': 'дːȷШŧȭɀ\xadČΝːĦϦȩќǰ\x83ıʬ\x9a˕_ѕϴРƯТѫǋ҅',
                                                        'value': 'ӒêƌќϥĦǼҟƈρɷвȨÑǪtϰή\x8fkТƘVŏΛɥĐÌӐ[',
                                                    },
                                        {
                                                        'key': 'Щ\x96ΙʏĭƎҔƍɺÆƍΩȵY˴д\x8fӎОΖ>ʘϋʘ˅',
                                                        'value': '_ŐÈÄŵϤѼԨɑûӝĲѧϿÄǷӯʋҴђʉɠʴǏ˷\u0380ʋƖĤɎ',
                                                    },
                                        {
                                                        'key': 'ǩͷ˞ºϋɡȭϽƒέүԪ͵;ϸɲԫāȐοóрԜȎѷƈаŷΣȴ',
                                                        'value': 'ΏŰľѸ\x85ҬʙʡѮƍѽӒΌƛ˙\x9eĒʖˤvԘYП\x89łȬƜ˫Үɯ',
                                                    },
                                    ],
                        },
                    'comment': '~ʹ0΄ɱӣ˓ϗŨѾʂѯʕ˟ЂĶЖЇʺĹƊҹÌȸßÛ϶ШĞʱ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'Ԁ',
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
                'sequence_type': 'sequence',
                'master_sequence': [
                    '?юǊƽϱĳ\x9eƙ',
                    '˞ÐΚȖΖФ/ԙȢмӒˤͳàі\x98ҚμɢƾχkҎӎʘŔ',
                    'Ϸ',
                    'дӕԁюÌΕʃԌҰʞХμ\x86ơц\u0382ΐȾшƓ',
                    'MҩӟҗɡҟϒъӹƜĊҶ\x9fӕɏзϒə',
                    'Vŀ\x81ƈƭĩ²\x8eʿмǒҀκіɔ˫UѓԥѲŤ8ѫ˓уκp',
                    '҅єĞІҏů΄ĔěɈɞȈÚCҽҜӚ',
                    'Ōû˽ʘ',
                    '¤ҋˠɯή˥UʩkΜϵƓʓѵºςԣϊřҴ',
                    '˛ЭӔӾԍӷ˂æ6βчȩŃϦǺɫǗʳ³Α\x84¿',
                ],
                'bindings': [
                    {
                            'keys': [
                                        'ѹΊ˶ͳЬЯǺʂȞɩʬ˹đʃτфЛ',
                                        'ÊȞǟƣdŒŋǀ',
                                        'ǝϨͳǛ@CҶǩò˽ŧ\x8aʦʖ',
                                        'ϸѡǻ˫ΛѺĮԛRțĠ϶8ɳ˓ԜǭTÏӅΓԈi«\\ňяüΫ',
                                        'ѹϏŢȕѐ˷ǂƩ˘ԕԥ¹ҹƚʲҝ',
                                        'ҊȓԪǸǼϮσƃ',
                                        'ǯĀT½ν©ˆω\x8fӊуɒʉ',
                                        'ӞΥąĊŖɽӚɵˊɴϠªʸĬɟΜ8ϼԢͰҗҟ',
                                    ],
                            'event': {
                                        'target_id': 'Û@ҟтɵϳËˎиųϛtϡӪÔŇ×ҽɭ˨§ϗűϯťęiƲЁː',
                                        'parameters': [
                                                        {
                                                                            'key': 'ŨˤͰȩтEşƍԈɧMpŬǏϽЋЌ=ѷżKӐŽɸǠÄѐЂW¡',
                                                                            'value': 'ſÇϣ϶ԥԮ˦ɘȱLʢ˞ʞ\x9aѕɸԫδ\xa0XȖøӫùѿҋ/˰\x87ƨ',
                                                                        },
                                                        {
                                                                            'key': 'ƎÑŤʊЙΦϙŢƉɗìгњЬǓΞŚŃԑȃӇ\x8bĽγ϶ūǽǃҙԓ',
                                                                            'value': 'ϪŻƏϓ¶Ԟ\x99âϐҜʂϑƼӲЛѺʧзͳǭɒӶԇŎӜϔȊЦЈǃ',
                                                                        },
                                                        {
                                                                            'key': 'Δ0ҮҢǣÊåѽДӼԤĩ\x97ÉбϪŅM°˂ƍǷ˲ţ˂ΝɐСèК',
                                                                            'value': 'ŀҥK˦êιǞƫ;ѾþĦʭαфDй˩æëƖχСãаƪŭőԢӧ',
                                                                        },
                                                        {
                                                                            'key': 'ˉЗԕʶaԧ~\u03a2ĝpҚǑ˶Ϛ˩ԈШ\x86ҾΫсϰ~ƟӂQÍö1Έ',
                                                                            'value': "ɧхɯɜѤǵFʴíћ'ʯQúƈ¢ԓƶ˝`ΐɷǡìҙĆɿԮɌ˗",
                                                                        },
                                                        {
                                                                            'key': '˴ǹўЬυʮÀȀʆʓφќєѷϜʊœȖƈУǌʿ˖Bĉdйе²˼',
                                                                            'value': '˜ϫËș¹döɦεӔȥϥ._ǡƩˣƀȻԅΠɘqӏăҌЖϼǿԛ',
                                                                        },
                                                        {
                                                                            'key': 'ϣ\x95Äʳ',
                                                                            'value': ')ώУπя2ɮǭʿ[ʟћу˻тқôЖƻȐťηςшqԍČӭnӗ',
                                                                        },
                                                        {
                                                                            'key': 'Ιȴ',
                                                                            'value': 'Ē˓ƦРԔȆƆҎ£Ɉϗ?ԧÜÝǽ?ҡϏã~ϵω\x9fɅȯϛƶķѲ',
                                                                        },
                                                        {
                                                                            'key': 'Ғʜ%ӭЃǃӛѳƛӖʮȍѮ\x8cӡʅ˚ŏ\x86ћӍи',
                                                                            'value': 'Ϸҋ˹Ԕʾѕԑɞ}ѣYȨΏ}Вŕϋԃśкɲ΄Ԏˑ˟dɏǶԈс',
                                                                        },
                                                        {
                                                                            'key': 'Mϊʶȡϰ\x8dͿʠϹ҆ˁʲ²Щ',
                                                                            'value': 'нÈϕů½ó)ʭƹΦ˭Ƙ˜ ɪЏÎ˶ʰE˾ԊŽǐˡÊȡ\x9dұϭ',
                                                                        },
                                                        {
                                                                            'key': 'ΊǉιʗŽҬǬҦқÜàȉʻňß\x88ЌFĴƠ*ƊԜɧǆΣόȩƓӭ',
                                                                            'value': 'Ȝξ·вҀ¤Њɐɾȋӝ\x85ÐňìJ˳Ѩ\x91\x88ӜǄėπĲ]Ĕ;ǚΟ',
                                                                        },
                                                    ],
                                    },
                            'comment': '¡ɭŎώ]Dʋ΅ȾĳΘɸŨŌÍƺЖɦOȤʌ×ɇ˟ʺdŭƨЉ҃',
                        },
                    {
                            'keys': [
                                        'Η\x86%bѫ\\Ξ5\x82ƨқȐľӅŲ÷',
                                        'ŸґԊФԣԂǕVϻ',
                                        'Ú³Ɂʽ˛ԟѠԈэ×Θ\x8f˸ƧNƟ»еɻ5ëQʔӵ',
                                        '˸jőдʬԉӘƑöǨύϪ÷ǁˁ2ǗԇбÚЭϊʀƇȝȀ',
                                        'ϞȆ',
                                        '˨ҚʟЦȧɼ\u0382цÀμǁνšͿ˵ҐĨ',
                                        'șҭ',
                                        'ҽʃ\x83ϟ@ԌƙϝėɢѭĦčҥγһ',
                                        '±ŭĩѺ¥÷ЗҗAZɜýұΜ˧ҮѶϏӳІë',
                                        'ĭҾ\x7fԕŪ˻өҍʫŠЇԨǣɕʟВҩʳ˚Ώѿ',
                                    ],
                            'event': {
                                        'target_id': 'ҬŁʄʔӰϵӺΎȻĽϰ\x91ѾДğѵșԍγĞ˓ЇǐƐ҅ѥSıѡŇ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ѯǄͱӯȜɽθЅņκϯǴÆŨ˻΅ǄȞʸ',
                                                                            'value': 'iȔѾ\u0381ʯÐ͵ά+ωǧӦГΛҔÛʵǩӵђ\x87đсȖÛӐſѝƽ҆',
                                                                        },
                                                        {
                                                                            'key': 'А1ΫшKʘȫѐһͼƷŧäӻÕѶƆUϑфBΛӋԬϗ˵Ơˈ˝Ё',
                                                                            'value': 'ƗҁӈɸjъʽŖʓαGХӒÖӪʟȅϤѬьʸХɖʝѬңϛưƭɊ',
                                                                        },
                                                        {
                                                                            'key': 'óвŮ\u0378ƑϱƐԓ¬ҬȓɈ¾ìÜĮԂŎǙɥsǧӣҠҚ˦¥ʔËɥ',
                                                                            'value': '¼˚ɬǅԩ\x8bĐ\x98ǈԫ\xa0ČȔτ¦˪ƞʠχǷρǕC"РúŵѿϞĦ',
                                                                        },
                                                        {
                                                                            'key': 'ЦȆϧɫʈʼԒGƶͻäѼǞƐԧʹ5ϋΥƢɭˣҢȻɃϠŢ\x86İÕ',
                                                                            'value': '˦ŲʱѴ\xad·ǣ˛ϰϔҐИƻΑɱąʇ˳ƜԇȞӨȥȒĊШ˰ΙαÌ',
                                                                        },
                                                        {
                                                                            'key': 'ˠʃҞҁȦˈԊşŕŜÝԝѬЯȺǩƝœǌӦѓ;ȲԃƊɉƜǚΑŔ',
                                                                            'value': 'ХѯäѹҢϜɐԅAġƦǳȿЮԁɸƼŧƁʴτȕ\x94ĎɡңɦϛǙԅ',
                                                                        },
                                                        {
                                                                            'key': 'ШҚȩҡӗҒԀǋԆϷԊ\x8a˫Ɇԧӗ·ƝÑӔ2ϸМιԘǉʙȭ:Я',
                                                                            'value': 'ҩӠѽäӯõ҇ùɂѴƨϛӺǶyϚƲȀ\u0380Ĥљ5ӿR˱ЭБǐʺx',
                                                                        },
                                                        {
                                                                            'key': "əǲΔϪ˖ԨŨbɗ\u0383ƝȚ\x9cÂϤҴҾ'ŷʪ΄ŨҵЯ\x98ӧϡҲљӀ",
                                                                            'value': '%ɿϙβyƿσԈːǵɎdγвɏȩ\x87Z\u0378đĊҳͳɵЧ\x90ȞŕԤȘ',
                                                                        },
                                                        {
                                                                            'key': '˄¿ΞϫӑǾȩɷȖƐĒʙ\xa0Ʈҷϱ˔ɲ˃ɨҸӹʭʵώҞȷʑȌ˟',
                                                                            'value': 'ǫԑөӌʘʡ˺ͷƗ·ĹÀʯТʗή¥įˆΗˌұϺɜ¦ͼĽԂüœ',
                                                                        },
                                                        {
                                                                            'key': 'ǘĦȚаȮJƋǫӱˁπʠą\u0382ПмʀƄϨOêȧɞȟƃÂӄ΄£ʼ',
                                                                            'value': '˛ÅԎȢӉˌǍөГɻҳ\x99ǈƶʤƌ\x81\x9cѶӥ\u0382ǩɳƘʇɣņæӃǇ',
                                                                        },
                                                        {
                                                                            'key': 'έΈǃɴˬ´\x9dτʶӴϚäԭŭЅԝʚċȉЄ\x9dҢԬӹϮ\x93è˛ĄǞ',
                                                                            'value': 'Ƌ:ƀ«ˆŒ\x9aǔѷԢΪԛȆТ·\u038bȖϓrϠ¬ΏˡŸůHHɗw¬',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ˀӍǧΏΠӊӲɤЅǁȱſkŝȗ^zϖ8(νʔsαƪúњǮҫЪ',
                        },
                    {
                            'keys': [
                                        'ςԪɺoԁԢ',
                                        'љ·Çԁ9ιē5Ȱcӈĭ',
                                        'ωȎ',
                                        'ū\x94ΩБƂι\u038bɷûуҫ\x84Ƀɔ·È',
                                        'ǗȰӴ¡È\u038bǓǦǄ\x8e˝φǴ\u038bđϿ?ΘԬҙ',
                                        'ӴӨӢÒϸϖÞӪˆљƶƟЫ²',
                                        ',б˃ˤсRҕÖΒ',
                                        'ν\\Ä4ϛˏƅǫĨСů҉ӻ\u038b\x8fʘʝӌˊғҚǈİː\u03a2Ôņ0',
                                        'ǺΰϝŔ˥ϵӞЭH˔Гҽ\x8aҚ',
                                        'ȵƄϮґϓǾơ\x8cE\x87ϊЯĆ¸ÚЛӭŭωȯӴȌģ',
                                    ],
                            'event': {
                                        'target_id': 'IȩШ:иȔɞʩ±ɂЈɱзӂҺҺwƉ*ҕҋƐΈѩņƋãƻǓӃ',
                                        'parameters': [
                                                        {
                                                                            'key': '҅¢ϰϥФ´ɵԭeVŚҧ˰\x9aĐƹh\u0379ͲѡҖΞJĒ˟σɤϯŬԣ',
                                                                            'value': 'ǕϋȑФƍѡҟЏ½ƋºϨʨȜʝȺҨiÒĈû\x8cºԤɞrȼą҇ҿ',
                                                                        },
                                                        {
                                                                            'key': "ȅáʽԔ΅ϞFɈɑ'ĚĨ\u0383ϱ˄ɮ9ӘmʺͷĉŽŽӤϊԅǫ5ɚ",
                                                                            'value': 'ϐćӣԃ°ɝ[¡ĺԚΤβџРʻƵІŞƟПơƅȫˑͳĔºƙʀʯ',
                                                                        },
                                                        {
                                                                            'key': "ɥ˻6ũƃΝȩѻ'˾Н΄ҢϮĤȯʫŕϝ}ɎϫɂМǓɗҳԑƑЯ",
                                                                            'value': 'ͿŕǢѰ(ΧŹ˙hŰĦΑνϵȺŅгǗɘșÍҘīϭӢ͵сϜŹǵ',
                                                                        },
                                                        {
                                                                            'key': '[˲ɨʢʕʱλɸçΣ5ӫ˃ϒȭ6ÂüvҊχĭʕԂ',
                                                                            'value': 'ɿӗũʁɴnԖĿĢïʌ\x97ʋɞˎϙǍÌʗͶK\u0378μаѻΎǲɼԦ˩',
                                                                        },
                                                        {
                                                                            'key': 'ԜȉԏϣȲĞʵӌ\x83ˇɨ[ƁƚĘ/ξɎȋğƘƗđʫ@Ǯˠ¾Śð',
                                                                            'value': 'ƖċÌҜЂ\x99ҭɹ?ɑДɜ\x91ʏͰƼǔ˶ӴДԉɖԄǫ\x93ԇɑȓ˪Ω',
                                                                        },
                                                        {
                                                                            'key': 'ԖΟРȼК\x8e',
                                                                            'value': 'ʡĳǞÍȗѷôҕǞӨјőӞΐЌϹ²ќ˾6ƌӚΑŰ\u038bȕ2ԟԟЇ',
                                                                        },
                                                        {
                                                                            'key': 'ȣԣȲӱ\x8dʗͱȖњɊɅϴ˱ψĹ\x9ff`ƔʹŧԀєӍѝKӲϤOû',
                                                                            'value': 'ːѡǶɑ;ǎʘĘЧ˞Ӎ˹AӮƁәψ˱ɝȆԚ4ϨƛюѕΕҬʿб',
                                                                        },
                                                        {
                                                                            'key': 'ӺſˡļѦӣӧԓû\x80ǙΝ\xadӜКӎƒКѹЕˮ˝Ԛ\x96ɉɁƩѻǙϟ',
                                                                            'value': '͵wĦ2˾ǙεˇлʄȁǫǽҪˆʅ\x87ӻӜˬȍǄȷjʋƄǬƖ\xa0Ԗ',
                                                                        },
                                                        {
                                                                            'key': 'ԅʪĆϧvúŏϯы\x96ʂǿõ˱*ÉТʳҒ\x9dɧǧƋȔeԋfTЛɨ',
                                                                            'value': '!ӬÄ˵ѭ˅ӷɝŪѮфӤɕΰǁҐ˔ʘЊhɯΩǙˣ·Ƶ˯ǮʱГ',
                                                                        },
                                                        {
                                                                            'key': 'ƎmϭСѴɚΨϨϧӯȻ',
                                                                            'value': 'ǊˍВĲ˩Ωƾ»˰ʸɡ¼æś¿ϼѕNqӅİɩӕ¤φwԡζȠƀ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ĖŚ\x8fßǴРżǲ9ҕ\u0381ƃΪҢGӜĄϣ\x81ӅеǨΊ˔Ì¡˯ȤɚĴ',
                        },
                    {
                            'keys': [
                                        'ϋвЃ¼зÏŌŒĖĎǟЪːíɋӢͱMȜϣ7˗ǞʜƱ',
                                        'ҳ˚ϧғцІþ',
                                    ],
                            'event': {
                                        'target_id': 'ÈƕȌ˲ðľҡҥƣοʺͻ«¡\x88ϖɧkǰʚԠѮÀчβϙTюùÅ',
                                        'parameters': [
                                                        {
                                                                            'key': 'W\x90/ͺ˚ɪ\x95˂PςŮΣӅɸЀʨЙĴƎǍӼųʎӜġŋЊΈԨA',
                                                                            'value': 'ĀãŇӂӠɂÑŗǉЉÐʧǆˤΎϵĴҶƞϴǱãƏ¶$Ł˳Ψþķ',
                                                                        },
                                                        {
                                                                            'key': 'Tδ˓ʹ\u0383ĴѩǯҼшġҞɮǺЌ\x9b·Ŀ˫ґӷƌϘYԟ3 ɕ˓Ƅ',
                                                                            'value': "˒¿\x95˱¶ʡӕǥE'ԢˤjГŧƶԛØʵϞȳφӳУıБȶѝŌƒ",
                                                                        },
                                                        {
                                                                            'key': '˷ɢɨҾŘɬÄ˹ˊšˀʇĳΥĉɖɲ\x85ӬәbϚЍï<ӦʢǪŊҢ',
                                                                            'value': 'ǧЃȲÖʴбʑӫſǘϝѳğˈΑɧŋʆƃӣȪӻʗĒ\x96ЈΚӞϮů',
                                                                        },
                                                        {
                                                                            'key': 'әŜĜΝěȍÃԏҼϛЌĜҘƞǰƆ:ĪƮuƛɴʬÙѧΩӇƽʔϕ',
                                                                            'value': 'Ԕę^ǐƍϮŬëԖѱћȎӽÍѱϝҼƖžȬ\x99"tʕǐºȥìś\x9a',
                                                                        },
                                                        {
                                                                            'key': "Ѯ.ϖ'ԕϧțЖ",
                                                                            'value': 'ǥŵԭҽѐ)ѷ˸\xa0\x99ȏЎȬƓȯǑϛj8ĨǢ´ȮēЃШɄʋ˘ԡ',
                                                                        },
                                                        {
                                                                            'key': '˨ӧȺ´PǃȈςӓӌʀϾõĥʻϭʴŃԬŠ҇',
                                                                            'value': 'ЬňûűɄϺЍțΊƛ϶ьR\u038bǘúȩʲ\x8c҆ǝЄǬFɹњʫϯʇԚ',
                                                                        },
                                                        {
                                                                            'key': '£Ҩԋƻ4ʦɰeǂˇúČʲȪҕȖǿʽҳҥǩˑʦǑӾӅҞ=Ãʲ',
                                                                            'value': 'ƞ]ǋ£ӊΖ«ӻĐdHȉŖӸêcvϚЪӁˌψħ˗ħnȞjfϏ',
                                                                        },
                                                        {
                                                                            'key': ',ā\u038dƃ˷ƮҦøƵȁʪƬƈǣ}əëȵɰɪƥԛäҸϡήӑΈ˶Ɇ',
                                                                            'value': 'ȤƁθ˄ӷĥÔȫĺȉž\u03a2җ˕Ǖ˵λ/ǶжˬƆЅƵΠіі:ļɠ',
                                                                        },
                                                        {
                                                                            'key': '˲ӺўŦÚƀ˼σŸŷȼʌĳŞҰσřÂǟҗĂνů',
                                                                            'value': 'АǪѡǫɾ˸ӣȫƲҭȺʛ\u03a2Ԟ¨҃ǮŖ´Ʌɷʑ҆ɓˁ9',
                                                                        },
                                                        {
                                                                            'key': 'įǘҿěςӢкɉɡ΄ШϝșU±ԛAҐȗɾɉɰӯҧʋ',
                                                                            'value': 'ʦ˔ʁω\x90ʒФɼǽ˓çç\x99ȫ\u038dŮнʏRąӇŌNтЕҠǷêňǹ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'Ưƽ\x9bȑѓ(ЃԚśɳèзǗȬĞҜ˜ЈΩ˝Þ?ͳʨБƩȆÛβ\x9a',
                        },
                    {
                            'keys': [
                                        'ϲƐɥŪʟǅŲƢɸ¹ȡôɌђ',
                                        'гѬϑӮƞю',
                                        'ӃЙːǫͻŖԁѫϣΛjȓk¶ӮÉ϶IԟƿɜʣˮЭȡƎӣ',
                                        'ӼԡѯœΊ',
                                        'ǍϱŏĵҿɄϞn˼ʬѢ,Ӕ',
                                        'а¹Īˬȣ',
                                        'һ˳ˎѦʼ¯ӷÞĕȕͺʜӈ',
                                        'ҔſДʌӮ³ͺԥӵɏӹëА\x85ɹǈĔѿӜȎ\xa0',
                                        'вǏȃŬʓ',
                                        'Τʨȉǥы\x95ȑҎĤ6ǅIoƯ\x85¢ƽȃԡ˖\x8bũҪȬ',
                                    ],
                            'event': {
                                        'target_id': 'ԞȎʫɻӽϵ˽ӊŢσȴӹǺνHυӞрӰӆɡȗ¯Ȧ˶ɤӦҕʂǚ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ĵƷҲщŃƟǅɿ\u0380ÖƣСοƨӴ¬ϳÁϋҭ\x99ǧԈÞӮő£ӛ¼Ȩ',
                                                                            'value': 'ƕƫIЊɇɒĞüԜѣȲäŞԞ\x7fɼǭɰÕßԖϗƀȲɮСƄźɼƪ',
                                                                        },
                                                        {
                                                                            'key': 'ɜгѰ˝KKѪј ǹȗƃΎƚѯˣжŕѾhͷ¤νѤӋԛň«ѢҔ',
                                                                            'value': 'ɥсΏъxѐʫKЁϨǉ½åΆѹΒҁ˞ò½ʯРҿζǃр$ŸˉВ',
                                                                        },
                                                        {
                                                                            'key': 'ŧɲƇҥĺeд',
                                                                            'value': '\u038b;Ϩė´ʇȲӓʊԖŮҨĖSŤ¡ӂϧԭԥҫЦϟхǹ˞ҐÏ÷ԅ',
                                                                        },
                                                        {
                                                                            'key': 'ӶƦԄιǪϥpîζΏңǻМĸϭ\x85ιʢѫ½īȋɧм(ӕ\u03a2ϥΏͱ',
                                                                            'value': 'ѷ˓ƨȧƏʀȩѝԁѮ»,ԑĞЙɘΉӶǩɢǧӧЩϱa}ȳÅѥʶ',
                                                                        },
                                                        {
                                                                            'key': 'ȳ6ǃø\x8bǮґƕĮȍÜÔĒяκԎԢ°ǲɼРԓчьӮʨžÖЀ;',
                                                                            'value': 'ƔΐԔѾШɶ˧ʁȰèҍ˝ŎÌГɞȺɮКSӫŸǄψƏȈ҉Ԑ¦˦',
                                                                        },
                                                        {
                                                                            'key': 'ˢǊnĐϖĿӺжɝ\x9aǋȊˋӤǷʣԅgȐ˩ƠǦԂɀҀΗɖɶ\u0381ϒ',
                                                                            'value': 'х=ĄȨфÝĶ{ҔǷĥƏͰлʬęʖΠǜ\u03a2ǁÓĬXBˠĔӏҔџ',
                                                                        },
                                                        {
                                                                            'key': 'ӓҊԧǓ˽ʳɳǴǢЏцƁҵүђ˒¯ʦňɆеΘ«Ţɧƕň½ǐǑ',
                                                                            'value': 'нÞэƅǿ˲Ԫɾ\x84{Ɯŵ/Ӆґ%ŀˬɾϓǘQʍėĥà҆\x89ҥʫ',
                                                                        },
                                                        {
                                                                            'key': 'βϰҬĞӔ¿üƣǬȐDʾыѥȡӉ¯ɮӺ҂ԉųʘů\u0380ԃȀѝȣj',
                                                                            'value': 'Ҍ\x90ȼðΊ;Ǔ]ȣξŜõξϴ˾Ѹ\u0382њGöɩʧģΈȠǵʆ#Ѡ6',
                                                                        },
                                                        {
                                                                            'key': 'Ό»ǛԪvʖʌѸӗǺþɨӂġͺēŖɣŬċ=Ŕ!ÖjΣÉ҆Ŵʣ',
                                                                            'value': 'ø\x8aŀǿԠцŬӳΊƍƿǃξő˵ѿӼҼȱǖ˪ˤĊΑ2іРķɶ˅',
                                                                        },
                                                        {
                                                                            'key': '¸ʹɐӈԙǘ˙ЈҘ©ʋϻʽүаȬʼѼˬɑʥхǸӶ˅ԡÁ˷ƷϚ',
                                                                            'value': 'Θaԋ~ÛҹʇéˤȒԑϜϫҥѱҝɡǢԑȟȾȹɭøoĪ˾Ů\x8cΦ',
                                                                        },
                                                    ],
                                    },
                            'comment': '`ϯǉŅѐВԓƖϘʕaĵӯ\x8cБĢƝ´ʑԅϺԭ8ƧԢ²ŵʋόΧ',
                        },
                    {
                            'keys': [
                                        'Ғȕϧŧ6',
                                        'ɚˇ#Ȗ\\ěі;Ă\x82҆Ďы=ѣ®ҘψƂӿ',
                                        'ЅˎИɶŝэæ\x9bȄ\x95˫ʽ\x80ɝz',
                                    ],
                            'event': {
                                        'target_id': 'ƓΗ˗ǠǂȤǎƭήʫŉşӛґ\\ɘcĘпǖѻŪЦƻʖŌoÝӠ˗',
                                        'parameters': [
                                                        {
                                                                            'key': ',ȟԋѝӱ˘JɈΓǾʮҩƖ\u0378@\x82ˮżyΈъΕ\x82ГüS©эǄϷ',
                                                                            'value': 'Ϣѯɽ~ŸјʥĬԖ˯ØĶI\x9eΙĬȠˢϟɟɁĜÖɓ"ŵʯȟæЛ',
                                                                        },
                                                        {
                                                                            'key': '˦ҶĢӸ\x87ȰΚ˽ŎϏтƥƮŕжӈT$ϖΧҨŹδ°êąп÷Ϥ˕',
                                                                            'value': 'ȤUÜ˼˾ԠӷȇҾ˳Ƃʱӽĥɇӡ³΄ҭҀV\x9aήˆŶ§ӳȚϸʼ',
                                                                        },
                                                        {
                                                                            'key': 'ӑԮΎȹò²«őʰЦ\x91ÏȫқǵLƐȞÁԐʝϗĭ˻ů˄ұӝÍԩ',
                                                                            'value': 'ãȑȆĺϋэΨu\x92ҴӐƸвΈʚƔʶǿRƢ҆ÈόҰ˚Ęc¡ĳ\x9c',
                                                                        },
                                                        {
                                                                            'key': 'ùԡϾӨɾԂĕϧЖғÿčɰʵԚġ˃ͲδȈҋɾњʭΠǠҪνɹ`',
                                                                            'value': 'ŢŹʅɳǺӯЏѶŋЃ\x87·ʯ#ɚåʤʃͻµlΟģÅʘǊϲлƫґ',
                                                                        },
                                                        {
                                                                            'key': 'ɝӾ˗ѻÂѩʷϾKΙөѦˏϝɝˑ˙ѽ`ӆǠөΔѓԇg\u0380ˮƟΞ',
                                                                            'value': 'ȫľĦҬģӡШ\x87˶ʂDʴӿɜɘРèHЩСąҀ°bȏ0ЗĥʽҜ',
                                                                        },
                                                        {
                                                                            'key': 'ÀѵɩƐςŀżúΒƁЛqȗϑϢĩӷΥӔҧѼԇȚäңҍǺĈʨЁ',
                                                                            'value': 'ǱϓīɆ³ϩ!ʝǋUȵɂԓ×ĕҏτѪѦѹŐȭƓɸ¬ɈǪчȥȲ',
                                                                        },
                                                        {
                                                                            'key': 'ӂʭ\x9dƕʇӫѩ¶үŨͼʖĎˉӤѧȔԦɗҫŏġʞ\x8fŋǨҭԮλԑ',
                                                                            'value': '¾ˊĮłǜ˛ѡѸŀȵ°ĘӉЋ{ϧȷάŹ΄ύԅƳ˺{ϩ˯ǻƭҰ',
                                                                        },
                                                        {
                                                                            'key': 'ϚЄЌϏ˥ȳуϊΛǊǨB˛χƴЈɛéʲʔʹɘҐŰɥËĝɹԎи',
                                                                            'value': 'хфȥȂЦ϶ïm8Ѻ˼ɀːĈҏɴʖҠt˭ƹɦ¢ŗǓκήҫҰȳ',
                                                                        },
                                                        {
                                                                            'key': 'Vƞɇɏ',
                                                                            'value': 'Ѳeљ\x80ɭ˘ǎǌҰϊȴҚÿѼŦϴǂˋϺѤŰÊģʏϖƽXÒđ˔',
                                                                        },
                                                        {
                                                                            'key': 'ȺŽƃҥ¤ŁӜˡľāѭϣ˧ԮӝePȆ ѨҹЬ¸ϜίȏȌ˒˨Ԥ',
                                                                            'value': 'чɈʭǫ6ŤΠˡʅҍ¯óєÞɉȅ˱Βėή£ʥԍˬɐǑɅς-Ѽ',
                                                                        },
                                                    ],
                                    },
                            'comment': '#ζS\x7f¸ʩƠŽҹʢϤɏяаΓʘǞɘӉҺϢʽŬєŎƈƲƵ¸ǆ',
                        },
                    {
                            'keys': [
                                        'æȵ',
                                        '҆ŬǹӗʾӃ',
                                        'πґЫƖϕψë',
                                        'ʲԆӳԡÝɃЫϦľȌӃǻsԤϟ×˙ǌΚҌ΅Đ«Ŗ҂θāÚ2ʋ',
                                        'Ąƌ\x9c˒άŬӺ\u038d¤Ƴʹ˘ҷɄϞƞò0ŤƜ˄',
                                        'ȟч˽ǝgщ\x7fɭȆ\x91ȮҁʃôĠǩŶОϾѤ',
                                        'ӈƒӨѤɶɔςƮɹôƌ',
                                    ],
                            'event': {
                                        'target_id': 'Ɓ¼ӡʷ¾źԎǍ;Ⱥʑ\x94ǯԎNӱӻ\x80ɟtԈԏǂɯ˓İǌПȰԇ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ǢŀΰЦЦςљΡ÷ʌÍµΉʲgʡģņˤЀӀӰȫɀ\u0381οĉʓ\x83|',
                                                                            'value': '\x8eѶҜîƅAӎʃȈ¥Ƥ\u03a2ǻľӬɆóΜ\u0383ѵʚkɩǢϡ˩Ǖ\x98ºɐ',
                                                                        },
                                                        {
                                                                            'key': 'ǘН\x97ĠˌϾĸĄ\x8fȨƀԞҏȥʔτωºҳȉ#ƪΰ¤Ⱦiӕύ\x90ʌ',
                                                                            'value': 'ʾ˖вˈԪԨǴΠԋȊВhқþʻϞɀŮ\x85ͿˮÕΗLáӗӳѾуȷ',
                                                                        },
                                                        {
                                                                            'key': 'ʾӷ«ѓǨøѷѮ1ΝƙКRɌŀФЬēP˷GϹɐƿȤ-ΑԒϘʿ',
                                                                            'value': '!ƺ÷ӵÇ\u038dīΞʦ˾ʢљǃɨȘвy&ţӜÿɩjȒԈ\x7fϮȨηǰ',
                                                                        },
                                                        {
                                                                            'key': 'ЈҹԣʫœʏŽ\x99И',
                                                                            'value': 'ϑѽɎȍqÁȀʸιɨnlȩȳ*ʯ%țɳѡ΅ЅҰӰӖʊƦϵȥȆ',
                                                                        },
                                                        {
                                                                            'key': 'ӎˋĲ®EƟΣǣɟǗɠұĹː˭ͿɥÉϯźб\x89ЏВҸтȆʀǌӐ',
                                                                            'value': '˞ɫƟϯѼҁɌʰòҮЛӒЮtŰ\u0378ӍӘѭӾǑ\u0380Ӂ˄ŢʍĒ\x90ΠƖ',
                                                                        },
                                                        {
                                                                            'key': 'ʅsšˢ«ӠОЗұϔԩ',
                                                                            'value': '˲ͺOʖƮŲȩRΫϢϣï˶ɍˀМ˵ԟѿӯʱŅ\x8bяНԪԣψΠϙ',
                                                                        },
                                                        {
                                                                            'key': 'ВȹȲѸӢѰʛКêʱ\x90ҺҐ\u0382\x9e?ʌʱń)ĲʾЁϡÕϊ^ҚUҰ',
                                                                            'value': 'ґѶҭγ҉a®Ѐӷ`7áʴFѬŉӶӂ+҇&ǩhЕɺĉƕҒӉΗ',
                                                                        },
                                                        {
                                                                            'key': 'Ȇ˼˯вȬȊŽȮWԮˍǓґ°ΥƦČρүԧȐŗ&αĝʉƄѡÖǇ',
                                                                            'value': '»ѷ\u038dΌϹ¶τǁԇЮѐӂӞ˘ʛъɉҟ¶ϔ\x9eȸŃþ¥ãĦϔхc',
                                                                        },
                                                        {
                                                                            'key': 'Ωʑ˨ЋѵыŹηʍҫЉĖυ&Ɠ;Ɉ',
                                                                            'value': 'цѢȿѦќɤĜt1ˎεшҮŚїˇĬѠИҳςȯҩéǪ˨ς˰ˆY',
                                                                        },
                                                        {
                                                                            'key': 'ǢȣȟɑυÍɷî˚ѰȘžƸ\x9cśѼWϖƹĖ\x90çȈԋҊϡģźǸȁ',
                                                                            'value': 'ӄҳϠ˧.Ɉĭɖʹ\x88Уϱӗǋ9ĔʟȶFȰΒŠκуʈYœχʸҷ',
                                                                        },
                                                    ],
                                    },
                            'comment': '6˾ҷƐɯҊüįaԤɉґѦԌςŎ·ƍ˞ǚʿӖԬVш×ЩӔb˒',
                        },
                    {
                            'keys': [
                                        'ľӷ¢(Ƚń»ғɃēҖ˨ў¶ΐɟʈ\u0383ȭҚ',
                                        'ÜΪіɫɌȃԫБ>ɚŽʁ»[ӛŹӺΚîƻ˳xĂʷǕŖϹ˳',
                                        'ɫęɌϡασҒӰξϧıѶŎǱъͿϜ\x83%εл',
                                        '˻ǾʬǌɷȂҮńƂӽĲоɭˮŵи҅p-˥',
                                        'ǯyǪ',
                                    ],
                            'event': {
                                        'target_id': 'ɒȩsg£ˠŒĽzɭЎȉεƊʴ˰ÆƽĉJ˸Ʈόː\x9d\x83ǅǴԮƘ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ӌмхɿ\u038bʇʜʩѢƶΌˏѽϊӘĤ˼ʜƞҬӻЇÀӪԒ±ȹÑЄǘ',
                                                                            'value': 'ҳÈуŌþԈȮǣ҅ЅĄˌŇǷΑƄÖМƆ\u038dΒȃìƢΤɋԉѬәϡ',
                                                                        },
                                                        {
                                                                            'key': 'ԢȉɌÇɫʉÈûϜǻЎɺΦĻӃɑÈ\\)ϑǈŸ˔ÀʚЌĲʖȀϕ',
                                                                            'value': 'ϒƮÅϰžɝЍϱ\u0378˝,\x9fľ»ΆŤԁИǛѾ\x88ϟ\x84%\\ʔƒŏ˝Ϛ',
                                                                        },
                                                        {
                                                                            'key': 'ĈǻөћΛαʠ˝İυɽȿĀћҰˎ\x8cҞιѴſǎάǙʦşőÆϷğ',
                                                                            'value': 'Uʿ˝íśƱ¡Ϯs˪Т¿ɓǳʒɁúдȫόҬ`Ħ|Ӵɽøѩ~Ǻ',
                                                                        },
                                                        {
                                                                            'key': "ǲ^δɝмgKȸĮǽʄƳʶ΄óѣȌӳȚͿ'ȍһʜǘҕˠ§vŅ",
                                                                            'value': 'үӓʴ\x81ӒОĝ\x8b͵ɉ\x85\x8aѽɜФɎūĬƩȟҔӹÛUŻ°гƧ\u0378є',
                                                                        },
                                                        {
                                                                            'key': '\x93',
                                                                            'value': 'ΥêΗҭǂʾɛǝϾƳĔ\x95ĄƛȫɄȄ[ϖĖɥg¸ÈÝȤƢӵʯ¨',
                                                                        },
                                                        {
                                                                            'key': 'ТÒǰ\x8aϯŲ\x88Ώ˲ʇÓϨŻǀ7ˇҀЫ½νĈʬJЫҙˬɳџʀȟ',
                                                                            'value': 'ĭ!ЅϬˇԤ÷ÎяƲӫȍęȠϓσļŐ\x9fšҸȒȖһ҅ϗņ˰ʋŌ',
                                                                        },
                                                        {
                                                                            'key': 'ʸϳ\x9dǉ˽ŐԑҝƙʓѠßŻ',
                                                                            'value': 'Ԁƫɳéδҽʤ\u0380^ħǺȮkПƺđʙƢԑʗΟȫƇѴƥϠVΦϳɵ',
                                                                        },
                                                        {
                                                                            'key': 'ʟҏȇ\x88ǒϗ¦ҒȰÞƷρȵͱʎĚʒεCґȅǔôȘȍōϮ&Ϣ',
                                                                            'value': 'ŏЌѢɺɟɫȵӀ\u0383ŇɖːƄtʵʇӠҞŏҹ˵ìʂϚ¥˱ɷʸƪҏ',
                                                                        },
                                                        {
                                                                            'key': 'ȾϤʹҢŲƇŹʆͱғѸ˽GƟΗұ˓ɔѯyƮѷЩgԧ҂\\ʒͳ·',
                                                                            'value': 'ğϲˍšϾľƻɻOǻ²-ƷϜʙԉɯʒњҒ?ɰѝдÕȼёɣǏΫ',
                                                                        },
                                                        {
                                                                            'key': 'ǲáǣǵ˟ҖŶZҿӛǞʐѺОρŕÇҞ˾ΪE˕ŨѵÓȢ«¦ԁț',
                                                                            'value': 'Ɖϑ@ԌЕʊԐ£:ǵǢn·҈ԔԋϘѸҠźͶNȮ˦ѧıќ˞Ԣę',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ʶӹӝѲňôɺҊӪmѻBĺЮѤȡԢβģǤѷłʳÍĬʕъӜҰù',
                        },
                    {
                            'keys': [
                                        'Ϟ',
                                        '\x88ōüńȡ0ιŮë҈ɗʰΦԤєƪѱ27κþϳϨţԞǧƳʽϞ\x94',
                                        'Ϊњ`ȹ&ŶӣӷѨͷŃ҂Iŵ˶ƻnЬѧ˭ӊʌ\x84҉Ӑ\x91˻ӟԆ',
                                        'ͺȐ¬бΨ',
                                        'ӋϿыȱȺζȎ´\x98ƣȹìϿЇӘȹ',
                                    ],
                            'event': {
                                        'target_id': 'ŬϏ΅ȠĎΣ\x9b˾´Ρϖǆӂǹюɵǋ=є϶\u0380ȟд˵ѤÐƎ˄ҙѲ',
                                        'parameters': [
                                                        {
                                                                            'key': 'їʤԁĤŅ˙ƚƿϿҎÊͱřеӳҫԃӡȫžʗŐϯшɞѝ£ΉԐņ',
                                                                            'value': 'ɄэѳĽƼˌ§\x95ѣéӾǟɠd˝įēɂѼľȼʤԣİćŧĩʺʵ\u0379',
                                                                        },
                                                        {
                                                                            'key': 'ÉƟƸǴʍϲƍêǣЌǨΆԙΩӂӌƗ\u0380ǚ(UΌԀÂ¥Ŧ»˝ʄʛ',
                                                                            'value': 'ʢĖǱʲŨ˲ÿȮѱόкϛŨjƏŐĝhӜǢƘиϪņƓȁŬϰʝ|',
                                                                        },
                                                        {
                                                                            'key': 'Ł˅ДȠѺŇ{ǒƾ"˷ѓīƉɫъѲʜðԃЛŉƾ˚ɰ7ɕPԍŤ',
                                                                            'value': '\x8e"ʔɮԧгʟʚwѥͺƛŉљĜʟϾKwӶŨīϑÿєŔƠʒʆř',
                                                                        },
                                                        {
                                                                            'key': 'ŗԠƖː!˻Ѝx˖ŋǐɒˈë',
                                                                            'value': '\x81фɰ˴ѮчĶŤυЅ\x83ǃПʲĶѩUӈʒԪΨǍ]\x7fR˲Ԍĭ.w',
                                                                        },
                                                        {
                                                                            'key': 'Ӎģy¥~ʾ\x89bƷëȪ°ѩǑͲЬʰĎȌД˸ҢКϐы',
                                                                            'value': 'ζ\xadĂԒȻń\x93ϹƙЍǙȘƻҰ˵ҜѝҋӛҪǰʠόЕĨʌԃӡҗT',
                                                                        },
                                                        {
                                                                            'key': 'ùԙƫїĿάº˷.ԨÅĚνĶάԪɒ\x9fì\x92¿ɲ\x94Aȍ\u038bЇȋӔ',
                                                                            'value': 'ŗǧǉў΅ʩ϶įҪ˅˨˅ȶ΄иɄǏzРЛ҅\x9bɫßєɺyӤ9Ŋ',
                                                                        },
                                                        {
                                                                            'key': 'ŶѮȰ1ϻӏвҘʵĥϞēԁЦÚɁӡΉ',
                                                                            'value': "ƤȱӯžLɡ˕ƥɲɁȆbϨҥÄБФԬ'Ђ4Фѳâ\x83ԠƮкГϧ",
                                                                        },
                                                        {
                                                                            'key': 'űӇ˔ϾæōŖӮГӈɓZʼѕČȕ=ѹxӬǒˈʕЎ\u0379ċǧbśǓ',
                                                                            'value': 'ŕӍǀĺѠӅÝƢȰаBτΨǮԒƗќЋӮƅȂԬxǘĨȋèůȕ@',
                                                                        },
                                                        {
                                                                            'key': 'ԝǫ\x8cΎ˻ƛȗυƯŚȒÁŮŐԂθЀщįȌx҈ƻϖ$ĜˎŨΧ',
                                                                            'value': '҈ԝőԔӬɊΆȇÔŘ9ŹҢԄφL˼g\u038bƞDяǅӂĔӈѫǡ\x9fϤ',
                                                                        },
                                                        {
                                                                            'key': 'ίпԗdъǉ\\Ǫ\x9cђԄRŁɄ',
                                                                            'value': 'ɠɸǀzчΉȒȽÚʍĿLϴ@ƢƷ7ƸǱµÏŰËʮʃҷ\u0381˝˷N',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ˠʙїĀ\x99ƕХĆАΝȥшfӐΗÎȃ\x97Ȍѻˊ|ȿԂÃԩҡ˘EĒ',
                        },
                    {
                            'keys': [
                                        'ѨǀšʢɧԇǻπЌʔɗҦťĩДɕƑaӽƯ',
                                        'ѧÕϸÆ^',
                                        'ĐˈԊhqЕğԪғǟ!ʷÝˀˑ,Ɖ',
                                        'Γȩӂӟ·ʶŪξϧɏ˄ȴϱņҮ6УkÔĵΦ\\Ӑ^ѫ',
                                        'άŬęϳϔˉ',
                                        'ϠυńķĄƯēЯş',
                                        'ҳfюӆžѧμϩɸҭҞЉӠ©\x81Ԅс',
                                        'êҷʺΠˢφǿΔ˱ӧĦ?ϠСŭ˨ɭ',
                                        'ˁʑōӂȝɜ=ˢƆ',
                                        '˪ʇȬӰʎ˴ȔЖϜϵԦԡ-',
                                    ],
                            'event': {
                                        'target_id': 'ΓɹƤ˶RQίȮΗɶȪ˄ʕȭâҌ9Ż.ÂʹǨ˞әƊч¯Ԯƽϵ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ƢϿƪǂЁƿĕʈԠϱŗŌˎɲϜſ\u0382ǐŲ5\x9eʞ\x9cˁ2ʕǾǕ\x89ʄ',
                                                                            'value': 'ǻʰӈ»ЍĀΣϲϬ[ȌϹӹ˹҆\u0383Ǝŷ\u0380ɶϫȏϖƟһǼԕΓ˚Ö',
                                                                        },
                                                        {
                                                                            'key': 'Ϯ\x90˰ĝԈԄɫϲǣԅƮèҬѡȺ˽ԗРϾ˰ӷ÷ĉӳŴԟÙƼКϕ',
                                                                            'value': 'ͲөωɕƹţαЩҁ&˴-ľŀԭɪϪҹɟª҉ϴȿ«ԏʏЌѰƩƠ',
                                                                        },
                                                        {
                                                                            'key': 'ơҾÿԦŵØȒӹüұČȱfǪɯģϾË˩Ɯ+ѮʧѠ¸ąДīǥˠ',
                                                                            'value': 'Θϔ˷ʾΧȂШѼǛƂЍʾɷЧǔӀлϙ\xadљЁʡ҆ĮȠƦʁԣM\xad',
                                                                        },
                                                        {
                                                                            'key': 'οȘÒļê\x8a',
                                                                            'value': 'ЂˡZē\x82ҐȀВĳ\u0380ʄӶӈћЯŦɘˬeƢȰфǬÑԊʠÖњчŭ',
                                                                        },
                                                        {
                                                                            'key': 'ԞŽѽȄÒϯ-Ӏʙì˔Š÷ɊυœήʑǝӐˎǒΤѻǻɃУƗƌʔ',
                                                                            'value': 'Ĥ¦ӊ˄\x98ўµɌº˪ĵĴ]ȈʃƨȵаÅȢΓʠӰāßʕΟѫǨІ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'Ȣ9ΤÂƭȪԮćԋ±ʒĶȠϸНC˴ӈōƲƜ\x8aӱʭOõàŁʄϱ',
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
                    'Ǌ',
                ],
                'bindings': [
                ],
            },

        },
    ),
]
