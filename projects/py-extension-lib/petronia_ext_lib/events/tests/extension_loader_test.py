# GENERATED CODE - DO NOT MODIFY

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import extension_loader

class LoadExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequestEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionRequestEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ǢɓЛөǫΗǖҖȚΰˤɠƎ҃Ű¼ÐǈϢǝкȍȠʂǑќʇɒшѳ',
            'minimum_version': [
                -6872606400332300808,
                -5140421267402304176,
                -2989120175459572591,
            ],
            'below_version': [
                -1208923355562830403,
                -6498025190943951923,
                -6994999731548089355,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʶɕŁ',

        },
    ),
]

class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.MessageArgumentValue.parse_data(test_data)
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
        for test_name, test_data in MESSAGE_ARGUMENT_VALUE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.MessageArgumentValue.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [


]


MESSAGE_ARGUMENT_VALUE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    (
        'string',
        {
            '^': 'string',
            '$': 'ŝˊȲºǧҾǚǝʲiqϧƹ¹ЏŒŭɝ\x99ʢȈ˓ÆЯθҶƆȌλӆ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -2914355035894891954,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 317924.20306978346,
        },
    ),

    (
        'bool',
        {
            '^': 'bool',
            '$': False,
        },
    ),

    (
        'datetime',
        {
            '^': 'datetime',
            '$': '20210309:040336.973337:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ǲ\u0381әҦeӐĔӖůĿҖԁʥ\u038dƄϩPȳʊԝΚӹѸŶώȬİӜŔĖ',
                'ƿƉбЖǭ\x9aԣȽɎȲ\x82Ǌй˦ҜËʬΤѼȎ~ȁĒ\x81ЂΓӍîɴҦ',
                '}˛ÎП\x82ƤkʏʆAȝ\x96ɈƷǾϔпąԅԄöӎÛЏ\x8fÄ_Ҋӱı',
                'РȧÕϧƏǠʽËԢʷ˒2ðɱѬǔŀɉƺңƥ·ΓгҸȟͶɋѼү',
                'ɸɡӧɧЁѼc\x81ɉįӨǰԎʋѓԧɧġѼϓπТѥ¼ȼǯʈн˚Ʉ',
                'ҼǯЃ¦ҬшŨǠУѺɜ˨û\x9cƳ#˔Ѵѡ)Ϟ|ͳ˦Qġ´Äɘ΅',
                'GʆІ˷ƂϭàȉȘҦЙìΟǬȰϳˠǟȎҷӓԌ´ůŜĊÚ/Ǥʪ',
                'Ҁťɡͳ˙ɷΰԄҋɔ<ѝƛɯ˕ӫӚðӻĦĉ˂ź0ɅҤƯǒǹ%',
                '҄ªЀ˝Ȭ8üĆɩʜǓчψȕȐ˼Ŭų¥ɣҳɲӱʆɫȩθ˄ĵԜ',
                'ͿДϳԁƦ҈ПæĥԨÜɹ¡ˮΎ;ӹђϬíҔˤʈɘѾԨʩ¾Əʍ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -5149819075369917186,
                8080607189003900525,
                7508593292719984003,
                -367284478312942578,
                5790669744252413000,
                2174863042935804178,
                -3558144392029783987,
                -5881701159476089324,
                7527877410759945260,
                9155332619944714142,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                120436.03691845943,
                117327.19491152337,
                320221.06621080096,
                544446.43521336,
                683637.2300202121,
                -35251.04575690614,
                634110.268911028,
                239270.3587375412,
                -42946.76051961765,
                384488.25335972116,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                True,
                True,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210309:040338.355238:+0000',
                '20210309:040338.375041:+0000',
                '20210309:040338.394709:+0000',
                '20210309:040338.416227:+0000',
                '20210309:040338.437254:+0000',
                '20210309:040338.456379:+0000',
                '20210309:040338.475781:+0000',
                '20210309:040338.496114:+0000',
                '20210309:040338.515358:+0000',
                '20210309:040338.534083:+0000',
            ],
        },
    ),
]

class MessageArgumentTest(unittest.TestCase):
    """
    Tests for MessageArgument
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.MessageArgument.parse_data(test_data)
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
        for test_name, test_data in MESSAGE_ARGUMENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.MessageArgument.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MESSAGE_ARGUMENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='MessageArgument'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='MessageArgument'),
            ),

        ),
    ),

]


MESSAGE_ARGUMENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': '#ЫyțЫШȔΞԐƥϠӠк\x8fĮFҚʚ҉',
            'value': {
                '^': 'bool_list',
                '$': [
                    False,
                    False,
                    True,
                    True,
                    True,
                    False,
                    True,
                    False,
                    False,
                    True,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ü',

            'value': {
                '^': 'datetime_list',
                '$': [
                ],
            },

        },
    ),
]

class LocalizableMessageTest(unittest.TestCase):
    """
    Tests for LocalizableMessage
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALIZABLE_MESSAGE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LocalizableMessage.parse_data(test_data)
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
        for test_name, test_data in LOCALIZABLE_MESSAGE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LocalizableMessage.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALIZABLE_MESSAGE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog', name='LocalizableMessage'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message', name='LocalizableMessage'),
            ),

        ),
    ),

]


LOCALIZABLE_MESSAGE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalog': 'ˆ˷ù΄ǇđĉјçМӠγωɔԓҮ^˖вÆӐсӢīȿơhĒǚɢ',
            'message': 'ҎŀͱʊҏßɥʺūļǞȐчZɳԭŕЧю\u0379ę¼˫ԟҊʀµƫ·ҹ',
            'arguments': [
                {
                    'name': 'ԨǘÚЩȨ¤\u0378ѓǭ҃ŠԓϮǯӓӹƧїДùԙvЫśǅһјȀȃԌ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ϰưэ҇ҹqőǘG]ӷ˘)DҗÙwϮgҁěðǋĩǉ\x9eX\x99ΓЭ',
                                        'Ƽhˍ\x9cʱмёȁëīҎшȕǮƳΨ\x93ƾϴ9Ƒ*χāрˉԈĂӊſ',
                                        'Ű\u038bąϏϻϸʬ',
                                        'ƭʇĿÆІVɱűԄˀѓ\x85˗νɎ҈ʗΊϤȒŌǇĿԁЏõ\x9cέūƛ',
                                        'Í\x81ԮǮȣ˻и=ĤȾЩϮŽȟϞưǎțϓԗŁȯfóǲбŢͽӇϞ',
                                        'Ӵл҅ӷȺӶԠ©ӈÞȶéΐʧΈѼ˵˻\x86ϛüʽĿhĝўɺŬʂǁ',
                                        'ƚɻжόϡӤxΒӒҒȽ.ҥӋ˜ÞǉƛҘǾŃ˹яʍÎǅƢ×Ήϱ',
                                        'ʲƏǆ\x96ͳJçЏҌ˦ԤÏɋbąί҉ԤԮīЮǵςTƧȟ£Ϟ·*',
                                        'ϋӓƞӠӭȧďҾ˶#ӲȴϓÅ÷ǟƳԇӲ½ϠŉƁă\x85ɴΓĜԭЦ',
                                        'ÏŻӲɻ»úɗæʎƵčĴΎҥιˍѽԬ}ƮǄΙƩƬǖƋƈЭʦƆ',
                                    ],
                        },
                },
                {
                    'name': 'ЀƺʆğɣŭӆӵǍЀ\x97ȳԞфѓϟϒ3ÎºѢ\x8bΠǒϘ\x88ϒ ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -1253588685595716329,
                                        -2470793499764684595,
                                        530519179509679671,
                                        -220579442434298168,
                                        606184926973706543,
                                        5078336222176699629,
                                    ],
                        },
                },
                {
                    'name': 'ŦЌć',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        777152.9787871225,
                                        550632.3265778157,
                                        619343.7407289725,
                                        -58362.22852995849,
                                        323083.68256277655,
                                        128208.27399355566,
                                        625333.3264265346,
                                        675729.8711727483,
                                        801939.8207459255,
                                        682647.9762835313,
                                    ],
                        },
                },
                {
                    'name': 'Ñ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210309:040334.771540:+0000',
                                        '20210309:040334.792809:+0000',
                                        '20210309:040334.815150:+0000',
                                        '20210309:040334.836373:+0000',
                                        '20210309:040334.859360:+0000',
                                        '20210309:040334.882855:+0000',
                                        '20210309:040334.908000:+0000',
                                        '20210309:040334.931063:+0000',
                                        '20210309:040334.954438:+0000',
                                        '20210309:040334.977606:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ȒҖȕͲȗɺpʜÒ˙οʯӀßΉ˩ŹΫɺı',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ĊɻˍˆƑȾ҈ɲŎɑӵLȜѫόϛ˪Á˕ҽɍБˑФɫ\x81ȶтΟɃ',
                                        'ȧŒʻ˳ΒЅº\x82Ѣӄţє Ԭλ˩ɫÛƀˣ˴БɽśɐȎ¬Ŝ°<',
                                        '҉ʢԮɚ˛@ëŽӪϡşƀţXĊѫˡĪ΅ηԀòӽВźaӧʯʀÄ',
                                        'hÊɳˈԁ\x83lϊˌһҽħĔѯԅӃˎѰUʳѠxuʫŏӲȟûӭǭ',
                                        'ϖͽͺĞѱuӦҒģҝҏ˭ψɬѺӓԨϯɯȱßǷ\u038dɆĶļýʷӯ˰',
                                        'ǽôĉʰБσƹѦΘ˅ŞŻ?ȿѤ_WĎȜˏƉĂɤϦƎəаƯâӶ',
                                        '$Ĕµ˲ҼπOη3ρĪĪΑɥèƏyːћǴҏŬȱƚθϷʩȴ\x99Ӟ',
                                        'ϵЌÉʹͳѡԬ˱ԢϨ9QЃϘˉȌџҘÿưїƕЛǠƷœƵrћɫ',
                                        'ΥĀêʁ¿Ĕɒʄɋуʶԭȶ&ϻұÁɀĸ{җ΄ʱȴщσƞ˂ƏЛ',
                                        'ӎČΩʓȒïН{$Ѐ±aèʡ\x98ɻgǭXϞȭɯΔƩĆʆŉUťˣ',
                                    ],
                        },
                },
                {
                    'name': '9ıƌȼԌġ\x90ϿЅ\x92',
                    'value': {
                            '^': 'string',
                            '$': 'Ô)ĎΟˬ˽ԊĎ¤]ҖΩççГ˻лʟɬӋӤɈєɕԗƙʿʦǎѰ',
                        },
                },
                {
                    'name': 'ɪŇСƂðϧʀҿдԎϹԛґĿEσǌΓȭ®ДÈ·ԃĿ',
                    'value': {
                            '^': 'int',
                            '$': -965610760622731480,
                        },
                },
                {
                    'name': 'ӄ҆ǅЮ˷',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                        True,
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'Ȓԧƹäˇ(ĭËϝ«ì\u038bıȕũЮȔϙǄ4ȑˣmӼԕõǊЖԒΖ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ҍԞ˥ʮϑȨЯѾҚϚâ¤Χ΄åĞĠùa˲òθ҃\u0379żʲΔ˾űǦ',
                                        '¤Ǐ҇ǆʍ\x968ǌԄʋоȸÊϑĢ\x8eѥǓͽÌ>җƖǠΘк˩ӐЊ^',
                                        'ϨϒŜ\x97ǩϕΆÄĀщҤҌһƵƕȋĺƱĔͼњ\'ӧ"ӮĤЅӬùԆ',
                                        'ΗʗɐǻGǈЮӉ˨{ѰĢїlƂɃƍʸƩ\u038bCϨɵȰмϩѺРғʟ',
                                        'ǏТԗɅ˨©҃ҾŲƂƹŤшШƨĀЕßɐßɺΰΦҽԎ¢ЏĂѐӴ',
                                        'ɴå\xadƶУϿU˸9ɣƲĤʹωĹ˘ӆʁКόǼ\x95ǗʩӚɘzŇūŁ',
                                        'ԀƠ\x95ŤúϘ8ϬɀҵHɩˁőԟ¢Ȗ#\u0382ȥþ6ǻǠʅȲŊηĨԜ',
                                        'ǯΡſ<оƂԦʘЀȘŉюſȭԠɷҬʝǧpϼȧȬЅʟĦԠ?ǺӍ',
                                        'ңМʺҚҀԩ˹ʖӄdҏԒΕʵӭϗϝǤüƽŁЛієȶ\x97ȑȐê˯',
                                        'ȑư¹Ȳ×ˁӘѓ\x9c/Ɵκ©ǼуǏώˑƓԖђľҿ\u038bȍϯÀӢ§ǋ',
                                    ],
                        },
                },
                {
                    'name': 'RȢҡŚҹџǽ×ɆãыˠýѾɀĴȤ+ԗԧӲ¸Ǫ˨ϵφ\x9eӅɗ£',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ýН',

            'message': 'Ƕ',

        },
    ),
]

class ErrorTest(unittest.TestCase):
    """
    Tests for Error
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ERROR_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Error.parse_data(test_data)
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
        for test_name, test_data in ERROR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Error.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ERROR_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='categories', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='messages', name='Error'),
            ),

        ),
    ),

]


ERROR_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 'mľÜΞƁțʢΥɺΟƍҗϫ˸Ķ}µŠΝΗǻԖ˓ɔ\x9dÊΘЏʗʡ',
            'categories': [
                'file',
                'network',
                'access-restriction',
                'invalid-user-action',
                'access-restriction',
                'network',
                'file',
                'configuration',
                'invalid-user-action',
                'file',
            ],
            'source': '¸К҉ɷΧɏ˴ΗƒɃӀ:\\ʸÔȕWӁϩӶ˦МîҖk˸vÈӄĆ',
            'messages': [
                {
                    'catalog': 'ѐҘɆľǅыŏʓќÈƠƗ~ˀүӜҜӢ˄ʟӂòɲɍϊƲ¨ѰʱΞ',
                    'message': '{ԉţƐԫ˓μӍȶ˯˖ŲΟСʪЎɚˤE´Ъǟʭη\x8cčэɩòӯ',
                    'arguments': [
                            {
                                        'name': 'ԃЧҡPԞȺæȞԦ©\u0382ΞϥǫŤΈɧʌ\u038dƠʢԒʢίƗĆØ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȥј',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            327997.15853066754,
                                                                            430083.8687177154,
                                                                            292151.6036702527,
                                                                            956670.7751804006,
                                                                            660619.067935708,
                                                                            983991.3982863943,
                                                                            320919.5594232884,
                                                                            576331.7535653308,
                                                                            310002.5975554356,
                                                                            338989.1660167433,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΙЍϪҡǂɡΕǍĹĔφÍHЇbǑҊȕӯʆȣħŧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'цˌϕǖΟ1δԥƂƟͰӐÂ3ԔΓͻī\x7f.˶\x95ĕIƌӗƿѲɴ\u038d',
                                                                            'ӼƖКɁȚĞǖȅϝŅѭғξźȜ¹ϋԌɆƂɆɧСOЛĢ\x90ϚώÔ',
                                                                            'кЕԏǮʖȺƝĳӖͳѼѽŒƖÂ<ΝĮEǷ˰ЖнΈLĻȃÁǴʶ',
                                                                            'ԏȒϤѝΜЄȈ#х³§ԡϑˁԒѲƈŹ,1ғ@ɐűjвƞüŗѲ',
                                                                            "ĨʅҐǚұŖÕ©ŜʁɛӄϾ˕ŔԪĥӣϓƕΏʛζΗŸŐ'˙Ƅ_",
                                                                            'rͱʫ˔ЦǰωʓʩɌ\xa0gԣФǓɰъԧҎӃʅØǿǙRԂˈn2Ï',
                                                                            'ǐƨǎЈȝƿΊʍƕªԟϓӜцƄƮƾcō҈ʝȮ)ԭ(ϜͳɁǒř',
                                                                            'ЃȀӋƬμ\u03a2ØЩӧӴâŘÜ\\іşҮЈ˕˘ʬѠũƦ"Ќ\x9fΕɱ|',
                                                                            'ƶŐπӳǀJƽƁą[҇\x9dΆXɫιʙϒϒɕũȑʄ˙\xadςϋΈÖĘ',
                                                                            'ɈƶӋėαŻƷȃюԝI%кʕƥĘũʞҒţ¬ящųǆȆȅĂάʅ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƔіȜϤϛԬƳ"Á˻˙ȭßГѼͰÚΉǐфɇɁЛƵķŕƟӨÝϏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 899951.0734606847,
                                                    },
                                    },
                            {
                                        'name': 'Ƚȱɪǅ\u0378ҴƜӵωΤ\x95ƙǕɡеƎȏǉҽɢȨF',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040315.455092:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŌʇLЫńԃŭÏ°ȦƁљɰ¶¦Ҡu',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            583398.4976027801,
                                                                            210555.06753912184,
                                                                            337001.65212809993,
                                                                            545630.1403773704,
                                                                            231023.0362301477,
                                                                            -35670.59423992028,
                                                                            465426.71871967486,
                                                                            426666.6256775198,
                                                                            726272.9875482938,
                                                                            867427.2947751504,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϒҤэΌ/\\єɆŷǟЙƍΩyӴɵPǿ÷ʚѾEΆÐÚǝѣǡԣζ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8289592252849740739,
                                                    },
                                    },
                            {
                                        'name': 'ʊǨǁ"\x7fýȋÝɃ\x8fѴÉΨ˯˨ʌƧʓҷ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĒӠîĖõřȱóвɣͱ¤ĻʕƣӦɗҁӤȸӍɀͺſ˫ҽ\x92Ң',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5449565635267659846,
                                                    },
                                    },
                            {
                                        'name': 'ԝȗʧѺ΅ĵƚҳҜ˼ˑǜїԕDƎƔȟŃǓùͿ\u038b¢ԩȒ¯Ţƾӌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ͷ1˱ϦÛǏÑǟЛȫ˸ӂÃˍǡ×ŬӺȌ˵ɰȰNǂѰԑ\x9cťʠӎ',
                    'message': 'ȮèɔÊǺӴʼЈȯƣђӧо)ΥԍǼľņƨэƢ®ӎӉΧʻÝХǚ',
                    'arguments': [
                            {
                                        'name': '¸Ĭҽялϝċё˟ƐȥʷɸѬ\x9cԡµəʽMШ=ӉԡuɇɓôĨɭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040316.809876:+0000',
                                                                            '20210309:040316.830661:+0000',
                                                                            '20210309:040316.852082:+0000',
                                                                            '20210309:040316.873474:+0000',
                                                                            '20210309:040316.893468:+0000',
                                                                            '20210309:040316.913861:+0000',
                                                                            '20210309:040316.936386:+0000',
                                                                            '20210309:040316.958118:+0000',
                                                                            '20210309:040316.981383:+0000',
                                                                            '20210309:040317.002255:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Pƺ˴˱ĦȪȚχхҎτǅ#ǤԤ°ИӿŸǘβЧЙŶәϮ˪lRŋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 18677.619523861562,
                                                    },
                                    },
                            {
                                        'name': '¶ɄӔȊ˦сҩӋӏєаʦǍҪҽΰԦШУ˻҆ЈĊθјɤɕȢ\xadĿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ƙȓ\\ˌĶáɲÜũ2ѨПǦŢěξǸȍɷςɈ\x87ˁʑUɓʦ\x89ʉԘ',
                                                    },
                                    },
                            {
                                        'name': '*BȕˊĄˣ\x8cȥУɚˑ»˺ĵҳЇѕÕŀдΜӕɹ˘ӨŃvψζϞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5992849282723970315,
                                                                            -90090371379158281,
                                                                            722901054329720241,
                                                                            -2787820954760799308,
                                                                            -4886643003911259584,
                                                                            -839222471986089579,
                                                                            6798819855995669936,
                                                                            -3019442671936521932,
                                                                            -6815450304025970993,
                                                                            7809933115516515036,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˗ҦkБԥûҏȬηS',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            178181.14646972367,
                                                                            978899.2348566118,
                                                                            211051.35056037398,
                                                                            350898.277805593,
                                                                            6728.431254291063,
                                                                            798420.8574604059,
                                                                            175600.8465445774,
                                                                            874647.1539902014,
                                                                            975345.2073624271,
                                                                            177600.21006991318,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԅӽŢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŚŵƗǗɿˏĹȏӦǗʒˣȿΧhϦҡ#ŮήŃƓΉèΆЉɣϪĢˊ',
                                                                            'ГÑĩȣΩђĠĕҰÃæσŬϼȎϡ˗Ӵλ\\Îƨű\x96ŷ˹đˈԙɪ',
                                                                            'δ˥ǊÞÊǑɸ\x86цҙ\\ќ˶˥Ͻü*\x9d¬ɸVƗ\x87ƕƟ¤\x89wȘğ',
                                                                            'Ý˷ɺІƶԊčһϣӞùёЌƆѿҖѳңOѽǢ˹ǳӾǷԇĄԃҸͳ',
                                                                            '˰ΓyʮϝӑȭԨϩŠΈcǫǇŇʨĜҶчЪώȆȬӘū\x98ϲȊа\x9e',
                                                                            'D\x93ўɻʹԝȅΔŀБť\u0381ѓΖΎˣϜ˕ȁœҚӜ˓Ңσºʱ\x91Ȼh',
                                                                            '΅ǰȷŘǌƱΞΈCҖǤĚөȺͷò´ŘƯҊΉˁϦ҈ʦǪЁ[҆Ԁ',
                                                                            'ԃԮϑ_ɽӊҧ¸ɢлƾЙҔ¶ӠY¼\x9fԗƓΟΎǆѫūƺ˖ɗǮʆ',
                                                                            'ĸОǤɌϸҙԔӦӱсĒʇ`ʸËőȏɝȌӧįЁēīΖɹˬŀΏЇ',
                                                                            '\x80РʆğҀв˟Ңν\u0383ӢЃÎӰЀ\u0380ɺ²ɠͷÈƋұωÈӛӯɞ¨ɱ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƷýΏæΓɑПʿЯѪʗԒɑʀΡԄ«˓Ɩ˹ĬƚԋӃԈфĵċƭ&',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040318.117714:+0000',
                                                    },
                                    },
                            {
                                        'name': '҄¬ϒȸԂүƺʹ2ԤυˤԩNĿɭʎǼŶлŕŀӾ˚ʙÛѶҴvЃ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            624880.4220207467,
                                                                            624973.6952929167,
                                                                            913934.2724512342,
                                                                            331464.17054888594,
                                                                            43287.98511566769,
                                                                            200745.26391193032,
                                                                            310357.03722193406,
                                                                            878198.2939111447,
                                                                            342218.3448967756,
                                                                            519687.81291011476,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'xϧ\x91ȗÚӔː<Ȣσ˂˸ӾΣIԠŋȧĲѝʚŬȗʦǫȷΗӮБĄ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5278511512500630854,
                                                    },
                                    },
                            {
                                        'name': 'ýвʘĐƊϜǁIɅ˖ΛԢ;Ȇ\x96ēȤԑσӑԪȴώϸƛщŬOӕÖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 252810.47488421143,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ңɤԃŗϻ\x96sǘȉuҰĈρÕȔ(Ȑϰ˙υ#ʍëɃӮˋ;˱Ԇ˒',
                    'message': 'Ŗш\x9dәǒƁԪ\x9fǷήĬĶȧ϶ɷ\x8bɌԎ55ôΡд%ЗŽϰŭŔȔ',
                    'arguments': [
                            {
                                        'name': 'ǆˮʞBŧϋ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -748946448181275989,
                                                                            3951934893910250011,
                                                                            34425084031158732,
                                                                            -6457531713130861138,
                                                                            862684292702149842,
                                                                            2869193233184556610,
                                                                            -7701130883560838952,
                                                                            -5601980571618288101,
                                                                            -1110847839551652790,
                                                                            -8991421954893679174,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͻΒӖӺԀˮĥΞɂǽɮɷΎϧӶȒąS',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 112375.29124753096,
                                                    },
                                    },
                            {
                                        'name': 'πȲАʚ`лӜӽϼǟϏÛ³ʖƞŋВӹʶŘǟɡӐ\x91ȚSʰψȥԍ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040319.083352:+0000',
                                                                            '20210309:040319.105361:+0000',
                                                                            '20210309:040319.127283:+0000',
                                                                            '20210309:040319.149814:+0000',
                                                                            '20210309:040319.173278:+0000',
                                                                            '20210309:040319.193953:+0000',
                                                                            '20210309:040319.214652:+0000',
                                                                            '20210309:040319.234948:+0000',
                                                                            '20210309:040319.256877:+0000',
                                                                            '20210309:040319.278590:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΉҸ0ˎ¬ϣ˓ĕʢĕ\x83Ɓ\x95ĨЯíǝƢġ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040319.388206:+0000',
                                                                            '20210309:040319.409602:+0000',
                                                                            '20210309:040319.430760:+0000',
                                                                            '20210309:040319.453608:+0000',
                                                                            '20210309:040319.478479:+0000',
                                                                            '20210309:040319.507197:+0000',
                                                                            '20210309:040319.534046:+0000',
                                                                            '20210309:040319.556716:+0000',
                                                                            '20210309:040319.612520:+0000',
                                                                            '20210309:040319.641737:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɺˢеǉ2ơƭɤǫGɼФԙõÞѝҵЋžЃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1488587910742342790,
                                                    },
                                    },
                            {
                                        'name': "ǨƾѧȦ'ȳҶįʵƳĻǟмӁȲ¤Ϯ˦ҳȟϢˈžpыńÞ>\x83Ɇ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4148270628912264996,
                                                    },
                                    },
                            {
                                        'name': 'ō²ƵЖʕґʩϱǑ,ʭë',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            382981.3828995201,
                                                                            -31166.49653525208,
                                                                            374472.6791907141,
                                                                            780297.357048219,
                                                                            232803.37716266327,
                                                                            696723.196147073,
                                                                            830277.3864101943,
                                                                            4988.3506986953,
                                                                            795558.2800933174,
                                                                            639268.5245332419,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЍҲ#ʰëБĺɞ҄μӧΥԜǡϪŕΣʉ"ɱæŉÔі\x90öɣЃĭЎ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040320.122045:+0000',
                                                                            '20210309:040320.138423:+0000',
                                                                            '20210309:040320.155828:+0000',
                                                                            '20210309:040320.171970:+0000',
                                                                            '20210309:040320.188461:+0000',
                                                                            '20210309:040320.204959:+0000',
                                                                            '20210309:040320.221356:+0000',
                                                                            '20210309:040320.237554:+0000',
                                                                            '20210309:040320.254433:+0000',
                                                                            '20210309:040320.271801:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˗\x8cԧԝǀ\x83ϥŏҦ\x97ȰʥŤбȅȧàҎʛɜŲǓԗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7766817918169037931,
                                                                            -1045253615919292089,
                                                                            -3825082521974682379,
                                                                            2848902327212531247,
                                                                            4177360634514701028,
                                                                            -390054589582850600,
                                                                            -8587538386947917806,
                                                                            -908045136892151148,
                                                                            8453045945272378614,
                                                                            7393265765483626157,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȅ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʦĪҟžĂǏJ¹ѲҔĎ·ȏщƤƻв²°ʏΠӖѪɄĸϏ˲ědѭ',
                    'message': 'ǄîãƟԁΌǃŋˢ˷εɦʸſȂϒɆʽΩӻ\\ϩиɚ͵ĿӣӒѶΈ',
                    'arguments': [
                            {
                                        'name': 'ԛ§ΊřȲ\xa0ǸʘЙɭȿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 880138.4156986704,
                                                    },
                                    },
                            {
                                        'name': 'o\x83ɊĀȅ˚ǧɒКΓŃӳǍĶĽŽЂȎӑɗҼƋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040321.176805:+0000',
                                                    },
                                    },
                            {
                                        'name': '6sǊԀw',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040321.257282:+0000',
                                                                            '20210309:040321.273523:+0000',
                                                                            '20210309:040321.292828:+0000',
                                                                            '20210309:040321.317193:+0000',
                                                                            '20210309:040321.339157:+0000',
                                                                            '20210309:040321.362165:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Т˗ȎҎƓ¸Ȅ¿΄ȉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2465304899036301633,
                                                                            -317331808035581281,
                                                                            -142608205056636716,
                                                                            8897289547047165021,
                                                                            6717965152911857483,
                                                                            2515228473689465300,
                                                                            2499312214718643206,
                                                                            -5003340780951977926,
                                                                            57663592466701278,
                                                                            8789518708960978622,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ù˩ӞwŌʡ"ŉθҚȱ\x9fȚǥԔɯϒӍʟ΅ĝƱ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 964703.4961979743,
                                                    },
                                    },
                            {
                                        'name': 'ɢĝ˝WĐĩ{ÝҍƦǂУȿρ£XӆǞʼσӲǧ6фѢȃцʀ°Ϊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5179782347159591657,
                                                    },
                                    },
                            {
                                        'name': 'Ίκ?РΕӪИóԧӴǘ[ӕB.˂ȇœϘѓӨѾҬ\u03a2ǔдп/Ȉч',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040321.947003:+0000',
                                                    },
                                    },
                            {
                                        'name': '\u03a2ЦȣѐΐϕвĲρҸǽИƳκϨɥ-ȋԅ:\\ӁҠʎƯɰ\x8d?˚ѳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1171040850700444968,
                                                    },
                                    },
                            {
                                        'name': 'εҳˉӚ΄ӛƵӜϘ;ɢ9Zҏ9\u03a2ЭƐΝ͵Iˀ\x9cɝɼσʫǪĀъ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            441896.4986187556,
                                                                            745969.6461530328,
                                                                            979727.3346679071,
                                                                            580004.0488277007,
                                                                            961916.4017371486,
                                                                            947089.4632371991,
                                                                            444422.7741573872,
                                                                            738167.223906385,
                                                                            744119.8394989753,
                                                                            286748.0220831681,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÇҶHʲʣðΑҍЕ.щϊŲ]:ƢѥĮˎƟ˱ƟĬo˘ȗǃϙ_\x9e',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 374141.79391574493,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '½ɿɝ˄ӅАŐΘʧQʗǴ˧±ʣ\x7fδѷѷώƘˑ',
                    'message': 'Ɉ}˧éΚ˔ԓeɅǏѯѣƹύԠΌϏӐʄăÚƮ\x80ɇƗЕɀȭыǜ',
                    'arguments': [
                            {
                                        'name': "HȸǾǞ\x89ҼǑӺëȑ\x82ȀȍϒȶτɎÁӕŪΥӖ'ɟʛʜŻԕ/ģ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040322.635091:+0000',
                                                                            '20210309:040322.658232:+0000',
                                                                            '20210309:040322.681027:+0000',
                                                                            '20210309:040322.709110:+0000',
                                                                            '20210309:040322.740511:+0000',
                                                                            '20210309:040322.774353:+0000',
                                                                            '20210309:040322.805647:+0000',
                                                                            '20210309:040322.835912:+0000',
                                                                            '20210309:040322.860824:+0000',
                                                                            '20210309:040322.890037:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʓɖǘŃиȟҨҺͿƗɿуϒ$V҇ϣϓÐΌXƢĪŐԦμ·ѹô¬',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƾ#ЉɊƣÈŷЬΦ|ǺϜʨԛҸГ͵Ƥ;Юϟϖˈ҉ƯƎӏ΄ĺǳ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040323.341580:+0000',
                                                    },
                                    },
                            {
                                        'name': 'åԫȚ˒)С˯Ξǎo\x82ӦʆƻҠǆłԦԚɾˀȖʐqШάӍǟvŴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӷΓ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            911968.509677886,
                                                                            695317.2477551623,
                                                                            -92602.35666592336,
                                                                            373109.009227675,
                                                                            914949.981790431,
                                                                            938270.5286430145,
                                                                            755315.0487525497,
                                                                            74627.74344206229,
                                                                            272630.2928630421,
                                                                            71297.5534565748,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '%ѭ\x81ʭΣɣĒʹҪҳűψ˅ɓҸĜI·ėΉɟϔҝ˷ǾβǇɣȃϬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8399516482090746937,
                                                                            8050872160303316031,
                                                                            3917494640401932697,
                                                                            6346167825668900694,
                                                                            5673786975239634244,
                                                                            6788076074417936077,
                                                                            9025593779439101535,
                                                                            -5411855270671395089,
                                                                            -8807123550919231916,
                                                                            3418558597050477008,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҘʢҫԑҋҎ¬ҺȯêƸ˭ɶȞ_ѽĞӷϼʼҿǾʄӎңťğ.ή',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040324.144113:+0000',
                                                                            '20210309:040324.171531:+0000',
                                                                            '20210309:040324.238732:+0000',
                                                                            '20210309:040324.324854:+0000',
                                                                            '20210309:040324.348643:+0000',
                                                                            '20210309:040324.369347:+0000',
                                                                            '20210309:040324.392465:+0000',
                                                                            '20210309:040324.413380:+0000',
                                                                            '20210309:040324.435694:+0000',
                                                                            '20210309:040324.454850:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȓӧͲԨȌǼ3ɆˁӾȿǌȼ÷',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 65125.87796459699,
                                                    },
                                    },
                            {
                                        'name': 'ҞЏȈϣ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040324.643565:+0000',
                                                                            '20210309:040324.667266:+0000',
                                                                            '20210309:040324.689356:+0000',
                                                                            '20210309:040324.711623:+0000',
                                                                            '20210309:040324.733901:+0000',
                                                                            '20210309:040324.755460:+0000',
                                                                            '20210309:040324.775476:+0000',
                                                                            '20210309:040324.794972:+0000',
                                                                            '20210309:040324.817898:+0000',
                                                                            '20210309:040324.845271:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȉɸνӖǳ˛wџμˀǳʌ\x90˸οϞrɘøŊĎʟȨ҈ƽͷ«Ěĵǚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ηƒò®һȏŒɗӀΦ˹,Ϭō\x7fԋ=Hk͵kҜҡӀ]ġʎźɨϷ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŗԦĬɜ^Ѫ\x84ƿƛϱ˲ΐ²ԕ\x80ћƭԚļȌ}ǈɺ>ɟѾɒˁͻ[',
                    'message': 'ȗP$ȭѬǰЫԜг˖ғԏԌȶğѯ\x85JԙŴīÙǥʝñǯǺϻԅȚ',
                    'arguments': [
                            {
                                        'name': 'ζԈÌū=Ӑήȍòϓˬſѹ\u038bѱǇnǳÙ,õө´\x86҈ӡÉͱǬv',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            814086.0857733404,
                                                                            982602.2401417713,
                                                                            -50405.29503217152,
                                                                            77701.5886192933,
                                                                            458523.7175267553,
                                                                            676309.0756427674,
                                                                            590748.9905536884,
                                                                            36348.255440205336,
                                                                            47357.674541914486,
                                                                            321870.143229429,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ļ˱ʅФԏхϋÇґӂtп',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4224179002499670242,
                                                                            -8135621675451917726,
                                                                            -8345365790389190716,
                                                                            7129502334118866477,
                                                                            -3823430919660653682,
                                                                            8244514998059049578,
                                                                            -4978732614906896525,
                                                                            179095021898985658,
                                                                            -3833886805284352306,
                                                                            3254952169844946076,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'îЫƼ˟ƔˬхïɺßХŒýΏҒʤҬӣЊǆşӰŶщӬԊӷԎ˱қ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԅƾȵџɤg]ϱȥˢɿϟPҴһнʥʣɑe\x97ӔÊÉËѿǳÊϚӓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҾĤӳǵϋŕƳѪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            13444.25797287446,
                                                                            904722.54429726,
                                                                            41860.74869080805,
                                                                            269225.99489381304,
                                                                            424627.5699745504,
                                                                            -11040.545896276337,
                                                                            379448.0337041323,
                                                                            266076.7195482617,
                                                                            803034.8265499556,
                                                                            668927.3036782582,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x95ZŲ1ИǼȰюāϟąԂѧɏӴ˵Ϡ4ɀɚʌ҃\x94ʸӇӷäT',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϼsÓCĿуȄǞǰԀŕϼïƃ˷Ž˸тǏɝÉĨʹΰȁӁҾХcƞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040326.432914:+0000',
                                                                            '20210309:040326.450094:+0000',
                                                                            '20210309:040326.472017:+0000',
                                                                            '20210309:040326.494144:+0000',
                                                                            '20210309:040326.516076:+0000',
                                                                            '20210309:040326.537734:+0000',
                                                                            '20210309:040326.559017:+0000',
                                                                            '20210309:040326.581043:+0000',
                                                                            '20210309:040326.604534:+0000',
                                                                            '20210309:040326.630195:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɌѾ҄ϥʈ^ӫ²ȇ\x82É4ǜϗȣР\x93ʔþϫʂϛĲËȥԬΧBȣІ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -38935.5209498612,
                                                                            943687.2414070824,
                                                                            497737.0611034967,
                                                                            161465.53309653315,
                                                                            256974.90213587426,
                                                                            889804.6823430457,
                                                                            124654.39400894873,
                                                                            750379.6097024125,
                                                                            357851.0326277876,
                                                                            564283.6452025381,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɈʀǢƋ\x87\x9aѨʠŉɔӺ\x95ɅòɳѧǯЯÇĹҜҲӆϫĥѓϕӇ#æ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'P\x85˂ϳЊОƌȿӷϫɎ+*ȈԃʑϊЄ\x89ԐӀƓϐÔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 311974.52058314736,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ɓƣʔ\x9aӟуĎѶǩʢƵʝԗƦUжWIͷŃȄԞӂȫ˕`ʋǒ҃þ',
                    'message': 'Ӂńмoɍ\x9cwƮΦӞŰˌԓʝ΄ʱˇӷĵӪԆvɨɼϣӄŨήƾȈ',
                    'arguments': [
                            {
                                        'name': '˴ĥԫϼҳàÙˋɾĒǞѝƪϼǼϦҗˑӟɝβϴԐɃϤ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -764505447690911007,
                                                    },
                                    },
                            {
                                        'name': 'ӆžÌ˅Ώąƒ¸ƪˋhͽЏ´ζǄ¼ɑɣϞ¤Ēú',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            144924.24471456,
                                                                            358198.72022465715,
                                                                            600508.9302330097,
                                                                            -30222.897144547736,
                                                                            -421.9669117987796,
                                                                            601152.2554589841,
                                                                            364679.05050131213,
                                                                            -97768.30534406265,
                                                                            147287.45622341667,
                                                                            287190.1301803034,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѱʠɏĹːƁŧǏ\x99ЋŒˢγτјәàϥϔ΄\u0383҉ђ\u0380ŖҬȺɝŹʏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040327.737948:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˡų˪ȴǾ˵ȓȝнԥŇ;ӠǓ\u0380ӃԦǹ\x85',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040327.819087:+0000',
                                                                            '20210309:040327.842713:+0000',
                                                                            '20210309:040327.865028:+0000',
                                                                            '20210309:040327.889480:+0000',
                                                                            '20210309:040327.917122:+0000',
                                                                            '20210309:040327.942195:+0000',
                                                                            '20210309:040327.965069:+0000',
                                                                            '20210309:040327.988046:+0000',
                                                                            '20210309:040328.010762:+0000',
                                                                            '20210309:040328.033785:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʪϩɴǤˇτŻƨk\x84ě˞',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2786747822262081832,
                                                    },
                                    },
                            {
                                        'name': 'Ϟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ðϔȦËɦԃѝ˯ОĊɠ+ώ\x8f\x8bŦƽȧrвĘǬȳőϧĎ\u0378ԏƐa',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8434134014168349117,
                                                    },
                                    },
                            {
                                        'name': 'ʩƓѣИПȤқġϦ҆\x8b\x9eҐЊŋˍ\u038d\x8dł˰\x92ɈɻԡДΜ˾Ό',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            161285.68988875087,
                                                                            335819.75145884516,
                                                                            641497.1925777782,
                                                                            681378.0784923548,
                                                                            574443.9679842533,
                                                                            653251.2844535663,
                                                                            -32418.260944496054,
                                                                            218987.2720323152,
                                                                            630030.70754462,
                                                                            859282.2811152413,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĺћ\x8cϭ˘ͼԁӞŜĉúϘϋΠšҫɇӴӦÖʙѰ\x81«ɮʗƚʺνԤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040328.813328:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ýř˄ҵģѕЂ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '×ºѺлʑćλҭ˯ϳȉk\x98ԠăγȃsſŨɗõѕ˙ӳƗҴϓnӰ',
                    'message': 'éƔűʔϤǭƔhɃҚϳȡɮɮ\x99юԧЦŕŔѵǸ\x81ПĬ˃ɅӵЕŇ',
                    'arguments': [
                            {
                                        'name': 'ϹɑϚАѧϋfôѵɱϘʛцĎϜŇų',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '&ҹҽDԀtԚŗӨƜ9ѠѬ˲',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040329.356833:+0000',
                                                                            '20210309:040329.376563:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '͵ǿιʁͱɄˤkáė%Γ³XǪϽǔĨЕ·ěeč\u03a2ɠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǯӖҪöƓȞ0ѝĴiԘԩϳƒˎōÉяԨνɻFӿěэΝƞǑǵȌ',
                                                    },
                                    },
                            {
                                        'name': 'ȥƃʘΠƁʈuū˒ƱēȅTİÿϦLȽˈŚŘăѧдѕӷѪɎΔȥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040329.559842:+0000',
                                                                            '20210309:040329.583914:+0000',
                                                                            '20210309:040329.606302:+0000',
                                                                            '20210309:040329.629771:+0000',
                                                                            '20210309:040329.655194:+0000',
                                                                            '20210309:040329.678215:+0000',
                                                                            '20210309:040329.697972:+0000',
                                                                            '20210309:040329.718498:+0000',
                                                                            '20210309:040329.737915:+0000',
                                                                            '20210309:040329.757717:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɉžϑŧȯńҨӌԎƱϺ¢ĐăȗǇqˮѫϓνȳͻҞƂ@ӹҌЅɟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'πŹθƋ$\x8bĩƼ\x8aôɢΙ3ƅǥýϘʩýƥƮҺпҊɎЇ҂ҍȣз',
                                                    },
                                    },
                            {
                                        'name': 'ĻĂьϪԋÙμїϮ]јϰȎ˪ǨjŊŞǬŃљԫЧӝȯūȪΚ®ĸ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'İWΌŝƩÀƼˏϻԧЏҬʭʯĨ\x9fϤʣƐʥɵӢʻϵӃǀĩƇѲя',
                                                    },
                                    },
                            {
                                        'name': '˪ԟԎĿƷ0ǅȃä.ǥԠӻ$ωu)ĜАǒƷλɲƚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6777095948269501871,
                                                    },
                                    },
                            {
                                        'name': 'Űz˔Иˊ-ěȑӫɇ6Ƹǯ;žižƸѮ6ҲÈѴԀ°Ω',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÒȵǀaӮȾűŴȵɸͲɾЬ˞Ħ§\x91ԌơʘnvџΥ/ǎŊK˘Ҿ',
                                                                            'ÁɚȂԏĿÛ¥ѠҞЅхΌ\x8bͲԐ³ИшӴпmʻϒώЯӼѨʯʁ]',
                                                                            '=ЁɡлˍԇѱhÇĠȟÇБѣїԡӈƨλǴ§ÐëϨîřѯɥоĤ',
                                                                            "ɗǺэȔ=ŲΦ5ӐΛǗӞѶȘϊΨY1'ЁϨН˩\xadɸƪSŴѠå",
                                                                            'Ҙ˝ҁq¸ǪƂԡØРͺ?рȋҴĞǫқ8Ǻ˯ĩ\x87ĶӉāїθΆƬ',
                                                                            'Ɉ\x85ʹϹȨрȇǟѕҤѮ~ΧФӥԗɠУˋΩʬύʑXƬ\x8cȱːϝτ',
                                                                            'ǧҚλ˯ũϲƞҖĩӴɤʇϋРёĴǤȦωŠƜɯʖ¨Ҩ8\u0378ЎΞҋ',
                                                                            'ƪѯӊŘȧжʾȂΣƩрӿªƑØƵЏƵΒ\x88¨¦ԑњȍ¶Ӝ3Яӟ',
                                                                            'ʛδk½ĺПÝͲƞ\x8e˜V¢ĻʅˊȦǟȁ¤҄˳ǞƦ`YӠų`\x81',
                                                                            'ɖŔǳԒ҃ɦҹf˺Кǖmɽ˳ȽчЄù>ϠϪԏΤ~ȁΡΆьáe',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˧šʣŗӼʞҕ˖ʞҋɯӳΊ»ȄĉůǶʫ\x7fǅ˾ĄԦԖòӬԛʩ϶',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4746627035081955407,
                                                                            -2373080949756507547,
                                                                            5988976030699033464,
                                                                            6570194747819984986,
                                                                            -1782328826114651487,
                                                                            -962051037059348380,
                                                                            3917044662583768847,
                                                                            -5187886555401027334,
                                                                            6786421120003675595,
                                                                            -2425453183911394323,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɏʀ§˯мҲëжZѪӧӨџДРŔЖoύѷ\x9bґɯίƃν÷',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040330.753138:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ţɶ1ЏѳӮʭÖȨǘʣLCĮ˷)\x8fŗ˂ǍɵёʼɬãЕиʂƍʢ',
                    'message': 'ĢӍԏɣÕ"ϿȮXˣªҳԩ\x80Ǡȡƾ¤ǹйӄȹſцĮ#ӜčϬΫ',
                    'arguments': [
                            {
                                        'name': '2ʒlҺλЈуȍ˱ΘʬʗǶҮ˯åԭΙΕʚ÷җȼԉҏϥȨȢ\u0379§',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            928761.4025169578,
                                                                            804939.2860136227,
                                                                            868117.3403996666,
                                                                            -40035.47482562356,
                                                                            756267.4112896645,
                                                                            273961.27169524523,
                                                                            233449.9099530485,
                                                                            692099.361962167,
                                                                            347610.3916858441,
                                                                            660146.9985600112,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӫ\u03a2ʺҴ϶£ƢȾҌìЉʦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040331.181777:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '©±6ИҥƸіȨΐĳз¨NяƳßӣėѵāԭјÈɤơΟ¹˘ĥɚ',
                    'message': 'ӆѽΥʊƱҟό°\x83 ԦУǐGµžӎƼΙƉʊӆˈДƤ˫πɛϞџ',
                    'arguments': [
                            {
                                        'name': '\x85ҶƸҺЂSÔϡĽоӆʹҲȄȷҼӥтԌɓзƲʌƳB#Ď6Č{',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 662349.6351530997,
                                                    },
                                    },
                            {
                                        'name': 'ǈӊѣʎȽ˫ѲŔҢѽʻҲ{a\x8fɟªˆƅˇƅ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4453787442135071866,
                                                    },
                                    },
                            {
                                        'name': 'ʫǶΊ҆Ϭʒ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            97141.46123145509,
                                                                            62168.48765604221,
                                                                            418747.89294607006,
                                                                            209568.43867686653,
                                                                            693037.8583435041,
                                                                            418640.62642251246,
                                                                            44063.43129063092,
                                                                            312065.0630075034,
                                                                            379208.2761924039,
                                                                            36278.27547573377,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԃŬϴҤʏʐ˖гԤˈǞ\u038bĮƂɨЙųƥ\x9eĠűϋƖӮĎӮēΧюӇ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'įHşɺЫΨˆѩȂȜiȜɝȋ}ąɝԦʤӲƚ\x93',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            376686.66048383754,
                                                                            880974.8605118043,
                                                                            790157.7243574992,
                                                                            226977.52487327746,
                                                                            345495.8542408978,
                                                                            -28780.093824236275,
                                                                            567445.088592142,
                                                                            367205.46129422286,
                                                                            246848.09144885256,
                                                                            809662.5457017764,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ř',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040332.458603:+0000',
                                                    },
                                    },
                            {
                                        'name': 'πɖ\x8dɳ˗ΨɅdzŰԛɾďXƋɴƷΓ¹Јʷʴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040332.547670:+0000',
                                                                            '20210309:040332.569187:+0000',
                                                                            '20210309:040332.591825:+0000',
                                                                            '20210309:040332.614794:+0000',
                                                                            '20210309:040332.635959:+0000',
                                                                            '20210309:040332.663133:+0000',
                                                                            '20210309:040332.686908:+0000',
                                                                            '20210309:040332.711310:+0000',
                                                                            '20210309:040332.737323:+0000',
                                                                            '20210309:040332.761676:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԡǗ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040332.878505:+0000',
                                                    },
                                    },
                            {
                                        'name': 'řӡѽȥʭSʇҨЂɝ\x89ņ҆ЭυǿӿПwɑƣǄʣġҜö˖1Ү҆',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȠýĹ.ĵŕʗŠͱʲҊńδэ2ŐǱŸǻǮʬԞſȍȥ\xa0²ПȰѧ',
                                                                            'qĈȸʏϱƃƌЩ҉νβ)ԔѓѓǔǀʥćϪЙ»ŻwɌѶΫҷЍ\x80',
                                                                            '\x80ȒïӻƑȗƐʈǄFҴϑªĐΘÌўӒǭɧʛ˭ŷɡwϧԍҽˈǼ',
                                                                            'ɻԆĵΖƋЁŤǯοϽòʔŬȦӬĳƼˬҸƟʌӷЈʕɪНɳǟΌǅ',
                                                                            '\x93Ѫ1ΊҍРпȃΰȎ"uͿĹЪŧТ¾ŽȅÄȫǉȺѯΑ1Ȅhj',
                                                                            'ǔˤʇЏ˯ϳŔƂɼŀљͽȩΛġҵlҽʰ0ͰǻʷͳþЌƔ\x90ûǏ',
                                                                            'ΖҞɐÄƔҶǌΩȣjҺҵӅƈӾɞǂҟӘäƉγɧÂãŎ ǏҒΚ',
                                                                            'ϔЄωΰºĔБϜÍǥʡʾϟϫŸɈг\u0381ɊAͺǦǲˮȋϷŬԜЊҎ',
                                                                            'ȫŶćûƘ˃ʂêƽɿ¿ðԜњ\u03a2ЏåӚƉЎǩ7ZҜ\x84жЩȟ¦U',
                                                                            'ʨɠɡǈEuӈҭͳˠӈƱʺˬǓѶϓ˵©ǆÊäĀʌΙʊˇ±Ҭζ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'оѭ>Żθǧ\x9aҧ\x9fÉ»ii',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9110378710399436107,
                                                                            -1722862396019405183,
                                                                            -6984911171717217910,
                                                                            7395636619259965335,
                                                                            -3244222086680984670,
                                                                            7279944911305960727,
                                                                            -8371466753239939126,
                                                                            -4922751457140262479,
                                                                            6286046836851524200,
                                                                            -6703794311423493359,
                                                                        ],
                                                    },
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ԃÒ°Ϣ϶',

            'categories': [
                'os',
            ],

            'messages': [
                {
                    'catalog': 'ҽӷ',
                    'message': 'ɬ',
                },
            ],

        },
    ),
]

class LoadExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailedEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='LoadExtensionFailedEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ʿҧϏ˯ԣė`ɮ_ԉҺǡСЛ˜¿ŏɷéɱϔń\\Ԅʏƥģзгĳ',
            'error': {
                'identifier': 'ǙƛԘѣԥфǁӫPˉБӣҳӦкԊŢɝҏɼʬѕҪÖƓӢÌВżʿ',
                'categories': [
                    'file',
                    'configuration',
                    'network',
                    'configuration',
                    'internal',
                    'os',
                    'invalid-user-action',
                    'internal',
                    'internal',
                    'network',
                ],
                'source': 'Á\x89ż˄͵Sͷ˯×ƃҳʴĚʡ1Ϩ}ԗɄÎ\u0383ǻN|ƭõǛKдȵ',
                'messages': [
                    {
                            'catalog': 'ǡʢƣw˕ͲѵӞưϩ=˞Ȟ҇ƿʙҌӝҵĵıÊā5ԊMɽуĝԬ',
                            'message': 'ǛƄϤċшх\x7fdϬƃ˵ηԤ\u0382éˌǳЄĝѺ|ԎĬƪɛÞƭҰɭC',
                            'arguments': [
                                        {
                                                        'name': 'ҲďĴŉŹҫӉŲi\u0378īÁɷŢԕϩɡϔ˺ŶѠѕƨҵʄŕˎĝɎǰ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ź\x87ĔƉӐʆӆԩ˰φȱÖʴԊӓƮʲĤǃȍ¡јʜªÅųΥӬƑQ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯ"',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƃ˶ǷȠҡӹԫǌѻӞ<˻ȌŅӺҺáσĢyЂȷҡЕǰγŚƊ҆Η',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƩʜŶƳ®kӆʹƄɋśȿÒԝǘȤƵ˫ǑΘʣԋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5950506189084683943,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӢΫfΎĞҰɋ˫΄ƸţǵbѺͰʔΚɜҬѿ˜ąӦҺʛƟЏ§Ɠ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '´ҡŗӗ¿ңєŮŨ´ϑɤƁʡѬƅʵˣүǕΠԚíϺΰˢ¶Қǂǥ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӓÅӾİʱέōђˁоYҳ˗Ȁˊѵʐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3355044087331665076,
                                                                        },
                                                    },
                                        {
                                                        'name': '˧зǁК',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӕƇѴ7ÃćƱʦĤӗľÉƖӋΌӡȈԙ\x81ΞӳĹŤʡдӲƹƻ:ģ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'rÂͷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 651131.8322181267,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '҆ƴөŵÑñģĩÊ,ɱ҄ĥ\x9dˍĳƏʧˎ0ӚɓЕҁΙōǚһЏп',
                            'message': 'ĽÁЫƸʹ³þ\u0379ˉȾЭϠϝǰɘˀ˔¦ȾŸ\x83űʆįTȊПчƭ\x92',
                            'arguments': [
                                        {
                                                        'name': 'ǒɯ˾aӊЍŝ*ǙғЏϟŘʃ\x8d',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƧûɱȔ"ǗӕŎɞˑоаЦǺůīҌϑŦƗӨȸĞìPѺ˄ӻ\x95C',
                                                                        },
                                                    },
                                        {
                                                        'name': '-5ӽсϑϰϣc³ԤϝūλӟҢŇ˛ƈŀȘĈѬɏQ+ӥB˭¾>',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Zϲԝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ΐQǁΙʽ\x81ԎǓɁϤјԀ%ƑƫϘκϼ'RŜʑfƤ¾ǈŇ΅Uϙ",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɗϊʝʂı҂ŜЛǳƚнԃŊſѡ°ɰʷ6ʃƚϓѹƀɧʍʟͽˍЎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4123018595032489399,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƳͲǅˡΕƤѳԛơɂӯʇҤȴʱăӺΫɀН=μ V¾˾Ϗȹhӳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '6ʱγɽ¸ԮЄѪˡƗɌʿŭŁХϰ¦ɪŦǁǷʉӼƞǠ\x98½є\u038bҏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǞȌɶԏҁìħċΜЉԑƹˍѸƊϬʵԦřńćŸ˗҇Įӝ\u0380Јĕ3',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫSѲȁ˪3ԆҞȥϝɍ/ŤLł\u0382YϢɦЇɆһÅõûÐ҉ȕфЅ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʄ&φӂĲľÒ\x8eɃXіљ˥ͻǝWΙȁȃƦϯԢʮӅԤΡʯ¡ЯӜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɰʥΒλʊҪǎǫϻƫ½?ОÑ˥Ȗɨ˝˜ʻьŹņ҄gΰԐ˻Īh',
                            'message': 'Эȍΰԛө Ǔǟȭ˭ӝƜԋ˯\u038b2ġȔ·˸ōϷӓʓȿԫΆ˟ĒϜ',
                            'arguments': [
                                        {
                                                        'name': 'ćĥԉсӥЫ[ϟțӞ<РŐѾɮίƂϠøϋѲ˩\x97ʼĖ҅ǞöζØ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3760031779435972935,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑFʍЏʺҡƂΏѰҢДУԡύбЊԢӣӊ\x8eԧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΈӪҝОʑđʤU˖Ϳ5ʘΑʷ¹ԜʴқҭʘƏĜg»\x93«˦ԕƺƔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͽ\x9eϋԋ\x84ÒϥԩӈҹąͱцҜÝɭәĝѼȦƑȰѳýɹƅȟ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѡ¡ҽŠˌǜ˗ȱҵңѐӓԧ˘À',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040306.986064:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "˕ɧĪl\x97ȸ˽ūç'ԧǳѻԅȤċˮȃĵȶӌÜvǌɑÙÚӉЦh",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '1ŭżҊśʿԄϏЏÉƥЬѴɈӫŒĐϿǯͼķ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǍÄѶʂԜƳÚƅğʦĚʜīҨьή8-ҽͻԣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ВÐјĉŎà˂ѨýƽέћԗȼʳęMкǱ\x9fqÈģΌʡƃƔҪ˾Ԩ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'È˰ƗίɄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΉЖʁԁȘ҂sʫʂҽʎϙюέ҆ĀқΥˋϒ˭ƔδЋϔб˰ƥĚȞ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʿȼєǡȱГӍˁԍǉīƩ¾(˷ԖÀѬʹŒЮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '`ϸöʄϐӟϖÉϛҤЊʙԌϔŁѕхʏŕ',
                            'message': '¢ɷѦrèƗρƻ·Ā\x8bKÕĳ˞Ѓʸɂɷ\xadӥǂέӗĜĢŶyΝá',
                            'arguments': [
                                        {
                                                        'name': 'ъӂÓƄ˖Ԍ҂ϺġӺļĲҼƘДԀϚǊӆú°ӈȃƑ\x87ҋXǡʈ˾',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4506672035273579720,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĠЅŅʪʮļZɥɖπЎȁѬʧɠӰЇёЃƔшǻҒŊǊɺѽыÌŉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѣˊ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'dǒɨǳķˮʗҥĊɘŹƒ\x90',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 38248.10072173734,
                                                                        },
                                                    },
                                        {
                                                        'name': '²ċÒӪʚèƛ˰Ť҂ǕîĀƽǻ5ıҮΛΑΨ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˳ƷȦԞȄɞ÷ѵţ˩ùϥUǼ\\',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'κBΐƠӐʯύǼy1{ȚѼԧÅэˤ@ƭΨÅ˚˨Ԧ\x8eɮєѽ\x9aĩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЯҜ˹¾ǫΠҙϙű˒Î˻ҍFԆȋǶђЛ8ŶŠȤϨĴͺΎΝªϪ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɝͲǀµĝαơЪƧӉıɡȃCʈЌ΅ґʦ\x88А¡ǫШŮƧxƙ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1051506497542363690,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯĸÄĲ\x95ǏˍǜˁҟĿ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ƞ×ÙƽäΎĞħ˱ɻǷˣ7ŧмѐ˕ɇӂôͻx=üɬƷɍ\x97ːͺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʾтҳçşԔ\x88˾ӆЯΞСƒǩʊƫƆ.ΰήEˤФɥʸœүЧƄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԭǋ\x96ĕïȁųӾʢӀμΊȝńƸԡˢȓЛϡz\x95ȋ³ĮbϤѰťѓ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'v|ӸҬÙύȶĞ;˼ϰȗőW˹ΩəԆʇǥńʳΤƹɴ\x80ʪʦµԥ',
                            'message': '¨¿ȘңǁȀ\xadΗԉ¦ҍȖЬưӽϾ\x9fѥưԎɈɗҟʈǠŠɞĮǣŐ',
                            'arguments': [
                                        {
                                                        'name': 'ɗЦ˝˻ʴѾVŀʽӉԏ\x89ŧâӎѳɉǸŨðĽӑ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʙˣϐ˳Ȩ\x8dƵ[ĞΈǤӞˈ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЋɌŗѢԃĶ«ϴǹȰҬϳǴʼгĪӻҵ\x90\x82ҧƽȳӹӶȨŎ\x91қ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2951571822248555406,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϲů§ȴέаЉԎԊеЁzɽŭԈJǺÐӒɹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϸϽɬҦԈQ\x9cåŉύŧЏƠ²Ɩ¤ɗͼνƿȿӧҀÓѶѡʒĖ\x86ȵ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȇLУӾǚʘȺDΤƑβΞҚ˾ßвВ˄Ǉ˸ƤчĜѶҐќӐИѢҜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¡ǾűΜ½бčНҴ\x8bƍö\x80ʹӁӵȑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6533929371094496117,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʌ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040309.281881:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǠоƘž΄ǭɝǨĉ~ӵûŒŗ҅ȡëľł˻ѳԉŋҼƝӮɞWɆä',
                            'message': 'Ǩŕ*ƍʳũӹŦɪɏӒЩÄľƲԔӭʠöϦԎʓѺ˛¿ǀ\x93˜ɡņ',
                            'arguments': [
                                        {
                                                        'name': 'ɡ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ęʈ>ӺòÉϹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ЉЏŔʼԗȥӻǨЁʭŋңʢ\x9cΫѮԚÄɜ'ēXȤѴħɛσy²ŕ",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 378280897065517057,
                                                                        },
                                                    },
                                        {
                                                        'name': '˕˕ηЦŏЛӊɗƕΓͷ:ȱȆͲԢ%Ҏş˝',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0381ȯœȐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӬЙ\xa0',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'χ˼җɝ¦ʛ¨KÜ2ɲҙƔÙӗҙӢũǺɖʁћɇӖʷ҄χҋθʂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1059064976374558872,
                                                                        },
                                                    },
                                        {
                                                        'name': '˹\u038bԚǔĤPŵã˪ʨͿæǥ|ʐʌ\xadO',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÉˇɈӌӨŎ˗ʯ¡ɱ×әйşàϐʋƧɹҮǈаχΪʏ\u038bɔѿz/',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǑAɖΐϬűϕɛêȫ\x80˲æ$GƼϖИϯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҪϧËƙӉɒǩƔ˺ɨЖƑ҄˟ͷʓԗȆǨӝ$ȟͿσьѳяҙϢȓ',
                            'message': 'ґ˪ ČɨˀѽâαT\xadӖˢӮʐѯɗɃ¨\x94ŎŗүҢҗъҌ»Ҙʏ',
                            'arguments': [
                                        {
                                                        'name': "Ͳ'θȔʇԞʝïϭСԠȔÔӃĝ.ӽŗϬŵѐѨȝʹρɑĖ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'žҭϝΠЦƾӮϠөηіŽћHԌȈϺƃǕƵƎӲēЭƚɸ˙]w˨',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˭ʅ\x84ӇúҶΈ"ЫÅӤ¨юλΜ҅ҌdaϽʍɱȬȁÜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɕȷΊҪǎƈƖƞ\x86ԛΥӹ(=Ͽ˜ӓȚÇʜňѫƺ7ÊÈθξȎ˒',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȍϺԊūҗȳɼ\u0379ȗΐƞŸΠԆ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'bҜʗϼϛєǱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÖǾ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲ&ė\u0379ӣżΑ\u0380Ĵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8018787133359799794,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӞЗųŌđҢѝ¦bʡ˅ǿЯĈÖԑ6ѯȜ¿ǲȔ\x8cџåЪӔǳĳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x90ҙQ&іӝʟѭºҚѧļϺЕΡΓĲӸůʏĀɼѹԀȥɖЃЯǽŶ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'өyҿǁɴӱ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 337283.7941446893,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ғʞYǼƸǅ\x9ciθϾϗкΆƬƲʦҤŏŦƗƌ˓ӌѬԮĚЅȓØŅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'iȱʺǗ±ǬӤԁÐҶʤĝȦþ¿Ѧ£ȗƟΑǂψЅÉӪЏǞӟ\u0382ɹ',
                            'message': 'ԅɚ¼ɳİżˋүVŘͻƐšӸӇϰɌϧȌфҔʐWϢɋ\u0379ȻӯԓϮ',
                            'arguments': [
                                        {
                                                        'name': 'Ȱ×˻E˲ԢˆD˛έѕɌîўѿìӾÕϱƕѓ˓ԙɫäȻжɰːϏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ŵț¹ɇÚjсȿѦA·ɱǞ=ĢƝˈͳţƬ˅UɤʢƖԖľԘǱή',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȭ\x9eŖϢѩŧǝ,žΔŋòÄЫȿԟǯөɚҞғ[ǌαŰς',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǝ҇ōǋЃǫӅћ|ĐЁК*ʇΊΰŐҷЄА«Ŕǉώǲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2085171495934240728,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ń¸Ħ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dîlșԃȜ=ӡwұʕZӌˬ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 250216.64589063532,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƴâЄξ˙\x96Ǖ]ґƉҷ˙ĥȌƾϳӪϢіͼśӧȴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040311.717410:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŃǏǛ\u0380ŤϞМĘ³Ӭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6174189008264546124,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǘӺΊȏϒіҡʽӌľëȎѧӎ˔ӴƔȻ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӤђԗʰŅŕūŸԠɕ˶ǧȳƸɵǐNʙ¶łɿƒ\x9cŁӪʆȡ¥ˉɺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѼΠȗƈ˟°ΪΗS0Ҩ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040311.993018:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʮ˔&ļ=ѯǼԨʓ\x8fҿʾȿ˶\x83ǑҊԛɡÙƥƥǈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 945178.0421286741,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȯѸƇюЇÄѶwĦƱFɶΰŰϲ\x88ɜҼɺҋȀϙzƥѝÇԄϾαϩ',
                            'message': 'тȡіʇȭҺĉȢӣΔϯ˹\x84\u0379Ϥɳφʐ>ΰSʘżƭǤ\x9fʥ\x93ɑо',
                            'arguments': [
                                        {
                                                        'name': 'τй˷6ƞ\x9cӚɟŹ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x93ȾƍüǱ\u0383ϭώϿɘ˘ĞÍ*˨џǮŜνнėȌʻĿϰoɡː҇ļ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŖўʖӝҦn',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɋеϏ\x7fʋĦǨΤ˃ƕԦʇωΉLѭvưǰ\x98ɪʹŎĤɲ˗Θѷθђ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040312.559986:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϋô³ȁyңˍ\x86ВΕŅɦ\x88\x8e#ӕάΜϯ҇ёõ\x99ãӧ\u0380ԀүƵҘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8730251752879824654,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͶǶΑóЦԖϔςŚɛԙΥƾɣԍơӮҙ4Џ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '¼ŬΪʖτӹӔӹɭ§IӮˉ҈ƘƃХȆɖӌwӵťõԚΦ¨]æ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ФðѽΔы\x80ФĿѲð¤8ЬɾȡьԞǧӁӲɖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 437175.3260624767,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ÿ\u0378Ÿd\x8cƆͽɆʥʯϡШӎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʢ҂ɚӉɪʫ"ԓͱ|α˩Ԏǈʙ˚ŋεÏ\x98ЅϐÜyȏ<áȎĘĄ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȡԈȚѷăÐӯԞłҾĚģμґӌ\x8dǳŘˈʎĻŞÖΊĎŞˑχʉһ',
                            'message': 'ӑЩϑѿØ%ɐ;ҬTԣӸ˖ϴϔʭεșɀ\x9cʇǖ\x98ϪǅǴȎΩɛϨ',
                            'arguments': [
                                        {
                                                        'name': '\x8b˲~ҷǆĿ\x84ЖΓɚųӸǖͱ΅ĞȱЯͻͲӇƹ˔Ϙƞə\x84Ģ#ř',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 908017.7404157039,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǜɭɦʢ«ǫíιɟÖΨ·ФПτӲΡƸ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ':ǳПΟ\x83',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ώʑɘJѬĞÝЅѧԓϜ;ɹʅҥúϵζȹөҨ˦',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŚӔЎΎ\u0383±ϿʶƹƕóUр±ƤPJŵқх˘Ѭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'řƧŚʶ˸ǂҲVŹЁŃȠύņ\xadɓԪғҡŻ<ҁǪɘԚȢāɹ>ȅ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ðҶєͻϒфъņȨƕ]ǌȑȄӢѻɍɩίĆΪӼɣʥҒêϼ¤Oπ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖШϼd(Ù\x86ǖ§ԫϽDlԥӉζƠȳƭǦԅzƀɠі˯\u0380ɭŭǌ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĆѧŬ˦ͶʧƒŨǃ{ЌТѴҔɝÜƓþ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÀʆТҦǞˆǎ\x88ВǝśģȞǉʺ҃ĮӃǺ\x8bϒʵd<ÊáčǻԮġ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѦϣÄʺ˅˴ʭË\u03a2+ţɦӼήΫƫĻфĊӟιαȽτjϧʪщľӿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ġ.Υ',

            'error': {
                'identifier': 'ĺƒӝɿƊ',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': '\u03a2Ѣ',
                            'message': ' ',
                        },
                ],
            },

        },
    ),
]

class LoadExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccessEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionSuccessEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LoadExtensionSuccessEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'Ϙ.ʥӼ»ЪÖ˖ԀΔȪ¢İ ͳĂæίϹǆѠǡ·ΟŌ˘жфƷò',
            'version': [
                -4837534308461708164,
                -7718484744358730865,
                -7399066619515403469,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ѣʿԃ',

            'version': [
                -7956910007665872985,
                -4871251390120195096,
                -5024810299890931240,
            ],

        },
    ),
]

class EventListenerTest(unittest.TestCase):
    """
    Tests for EventListener
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENT_LISTENER_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.EventListener.parse_data(test_data)
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
        for test_name, test_data in EVENT_LISTENER_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.EventListener.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENT_LISTENER_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


EVENT_LISTENER_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'ɉ1ƓȕʔѨ$ƆŷǸάȤӏЋʠ˪İȭƧͺ˝ĺɩʳŇȵğnıċ',
            'target_id': 'ȲӃʪ~ðӜρŏʒç©ɲ^ĻBоƉҐ(ɅCŢʩˉϓfþĐȼ˰',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

        },
    ),
]

class RegisterExtensionListenersEventTest(unittest.TestCase):
    """
    Tests for RegisterExtensionListenersEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RegisterExtensionListenersEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RegisterExtensionListenersEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='RegisterExtensionListenersEvent'),
            ),

        ),
    ),

]


REGISTER_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'event_id': 'ƣτ£ѐŇ҃κυʚĐɃDҽůӢŊëӰƕʧԣԒӲԇȂȀϞő\x89Ƌ',
                    'target_id': 'čɊǲ}ä\x8eɀӣРˇʜϯǗȍӈ\x82ςɤȼϒǮ1ÝɠϯϹяAjщ',
                },
                {
                    'event_id': 'ԌίӅϵӯǸȿDşVÎŷΈťÃķGϔɨŇƻВǓ˛ȯȁʿğ3Ŷ',
                    'target_id': "Ǘė˩\u0381ƠɴĘ5NԎǝϔХĘϠȩ'iƬȗȩ~6ŖɆ\x9eô,ɏЯ",
                },
                {
                    'event_id': 'ǶƹƙŐȱĦȋωʆˮǞġϽǲǍȮĀŖɾ˙ŖͶËϡʈƥϔ˸ǈӅ',
                    'target_id': '˱ǆɕĪǕԜǊӫǋЗƱ_ӗ˨ͿЕҖđ\x95ЖƁƂưǫƍ˯Ӏ¹ХѶ',
                },
                {
                    'event_id': 'Ί\u0383ФƫŒԞEĂìԅ¯ȅҡȮ"ϣԀϖдĩƋƣĔǌʸ˺ųíόɛ',
                    'target_id': 'ǣӏøʊҔǔʆɺÅńĵЯǻҬˁʦѕԨȘEЕ˰ŀoǠ\x85ȚѶȊ|',
                },
                {
                    'event_id': 'ѝѰńԎɩ\x91α\x99ѱΌĈ\x88ǛÛϢȝȾĴʰχjѮƑΆɐԣ\x9aùȂŀ',
                    'target_id': 'Ķҫ\x85ĠВӥЅҧʗȝ˂ȼǣɷǐǉɅ͵Ӑºʭԭɩʰő5Ӫ!´Ί',
                },
                {
                    'event_id': 'źŸӨóǕԇѸ˘ӜΌŸǒȪÖϵȠ ǹľԣŦЅ\\00ӮĥUŏã',
                    'target_id': '\x93\x95ǡӐ$ÞʪşʿĈџT҃ʴͼήϗцҹé$ӭ˩Жєʋ˧?аԣ',
                },
                {
                    'event_id': 'ŔȆʤÝ.\x82Ҥĩɦԃƕå\u038dǗĦkˊėЩǏѢԬυȹӕ÷˂јʘä',
                    'target_id': "˘ωŁлɣѦŷrӻΌвƗȟϖ4ŜӓȎ'żúэѭ©CľӘ¶ơ{",
                },
                {
                    'event_id': 'ҽЄӠƛK³\u038dɯԭ˟ӍĞЅӾяԄȟ³Б.ԧƙÏʪĹǥCʳӫÔ',
                    'target_id': '˝\x94ЫƁˠOŰσĶАȫK҉ѪωӓҗȗҪ\\͵ҩĳӎɡӭhĈόз',
                },
                {
                    'event_id': 'Å҆Ż.\x97ϵŻȣĳȸȩ$ɶ\x8b\u0378ǩĄŷɆсԮȱϵF˝ʒǵȤϭϴ',
                    'target_id': 'Wƥ˵\u03a2ȣҒЕ˴ɦɉҙӖͼӬ\x9cҖӐƫҐӁˌźWĬԄȤȌˀȽȭ',
                },
                {
                    'event_id': 'ϩȒȪʆϔǗЬǍɛ҂ʶϨҚĈīˆūíʃśў˭ʭĴӺ˴ƾӸđΌ',
                    'target_id': 'Ƶ˾ǊɄĢ\u038dʘЧκƍӄҊϲτłǂɆûƱ=ʡË\x86ΟȽĨюȏΊȡ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
                {
                },
            ],

        },
    ),
]

class RemoveExtensionListenersEventTest(unittest.TestCase):
    """
    Tests for RemoveExtensionListenersEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REMOVE_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RemoveExtensionListenersEvent.parse_data(test_data)
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
        for test_name, test_data in REMOVE_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RemoveExtensionListenersEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REMOVE_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='RemoveExtensionListenersEvent'),
            ),

        ),
    ),

]


REMOVE_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'event_id': 'Ⱦèɸӛ£ЬɕϩҲůǼөʘӧϚгuгʇȎʗɁz±ǮˠÀĊӦƂ',
                    'target_id': 'ǊщԈåѴŧΎȅxˇË"Ήά\x89.γ˶ɧ÷ҷǍQ¼¯ДűХлӭ',
                },
                {
                    'event_id': 'ăʩжɪĘЖƮ}ŃΆǊѫǆŹϏģ\x91ƾҳιsӋчť\u0380ϓɁѬͶǴ',
                    'target_id': 'ǩɶϡӾ!ϣщŹ#Ŕƭʻɉ\x86ϷŬ1ņƏΨƧýʭĳ˅ǯъĆÍɜ',
                },
                {
                    'event_id': 'ʒƷĿͼ@ўҙ˔ˌҊ\x8eʶĨѡŅŪ Dο˪)˳Ҩ\x80өĴΥîσÀ',
                    'target_id': '@\u0379Jѿ$˵УȠðſS\x8eӿȩƀː\x98;фˀɊчζԌ\x90ʪȭҷǭӖ',
                },
                {
                    'event_id': 'ԝȌƾԤƃɅƏг«ЀѮ9ϠŜϗԋˡѵ΅ĞćĻȐѻŔů¶ʆ˻Җ',
                    'target_id': 'Ƙ˚Η\x9dϏуÕǿаFǧřÏɊƲÏʫΆͽǪlӆĩŢƭâҔPȿ"',
                },
                {
                    'event_id': 'ҳНз\x86ӕMòěÜЗԙҁӸĩ\u03a2ȷѦ\x88Ŧ:ĊͶ˅Ĕѹˇ\u03a2ӵˬɚ',
                    'target_id': 'ĈʌРӮξǩÃA¸Ԙ˹ǅӊBUϼ>yҭřɖǀþԔʥŷǮЇѼΚ',
                },
                {
                    'event_id': 'ɓрƧ\x9e\u0378ϕ˲ȢжȰжɭĂҳŚüЌϒ˵ҷŃÐàԚ9ӁοѱΉn',
                    'target_id': 'ȒκʊĖĝΜƛҜâŨρЪSˆчТЧԑůƕΝӖƠЁʑԋѪɂj¹',
                },
                {
                    'event_id': 'Ǧȼ-΄ˍϞŌвǠ\u038bɲѿў)ǲӄӁˤŦcɇґÔŖԮüƼʏ˨ѻ',
                    'target_id': 'ȗPӄРĩǬʭϾёĜČҪο҆ǨѭϞȕӢԟΤοѯϤӓ\u03a2ЕÜȖŬ',
                },
                {
                    'event_id': "мʜ\x80ΟԡĄʲ¦ԜϣѐԀʟɃҟ'ǵċ\x91î>ЦȚѮεɮáӠƶʘ",
                    'target_id': 'ýϏρȲƧ>Ӵ,ԇȷНʴҢШԘЭӗ˳ӀϐÉӭǼȚĲáόӕǫŷ',
                },
                {
                    'event_id': 'Ӏű˔ȗϹұѦƬ\x9aԄÄʒϙŮԮАԐɪĘϡѮǅȓӎ\x802ʹеʝь',
                    'target_id': 'ѰèӒɣϺŢȡϟɪOԅęДŗƽd¬ƛȐЊ{#ġҠǂ&Έ\x86ѹӁ',
                },
                {
                    'event_id': 'ԜəȍǳԤ\x93СͿΨ,ҳә2Ѹʼ\x99ȣǃłʸÆδЌ|ļAϾɎʕΝ',
                    'target_id': '"ˀбԬ©ŊƂȭƭİ§ԖĭɔɟԔóǝŊɣӸÉǧшψhʁ·ʹM',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
                {
                },
            ],

        },
    ),
]

class SystemStartedEventTest(unittest.TestCase):
    """
    Tests for SystemStartedEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in SYSTEM_STARTED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.SystemStartedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SYSTEM_STARTED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]
