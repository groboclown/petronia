# GENERATED CODE - DO NOT MODIFY

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
            'name': 'ʯéқ&ùЧƓûτŦźѸȰé¬ØωΏэʚйϱŠоϩǵӰ˻/ҁ',
            'minimum_version': [
                -5017289255162056813,
                -5779516673746404647,
                -4722835560064163476,
            ],
            'below_version': [
                -3414662464417281540,
                -3391522424108793698,
                -9195207019234295922,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ŀԀў',

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
            '$': '҄ѺѺԙs¯Āп\x98˗zɞӼ7ЭӸǙϳЁŉŞ3Г¦Ǿĳ˼Ԯſǿ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1553212607691695879,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 864155.7585041431,
        },
    ),

    (
        'bool',
        {
            '^': 'bool',
            '$': True,
        },
    ),

    (
        'datetime',
        {
            '^': 'datetime',
            '$': '20210909:200611.901461:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'εƹ?ˇ{ιɫʗζЛ¿Ԉӈϻ.(Ϩ\x8aɐĽ\x8dǰˆʔˎȆŅԭĩƫ',
                'Ƣć\x88ύʄхɨƕƕʥŖňƶąлЎƋʯʂԘŢҠΕΓŏϞЊʠƌĀ',
                'ӮҦηψʄϯoĎљš\u038bǓĹŵʜǑӎœѫϥѧČãǇǳŷϘɥŻҽ',
                'ҴԚͼǻǴѴѝӆІřҜҤȊˢȾ;ԫƇѰ\x9bӼǕʘƁSȼіǫϑƅ',
                'ǻʆз¯Ф(ψɸӔЪȫЦ$ӿίЮƍѻ±Ùԫ\x8bɬѾΈʅÕȕҲȔ',
                'ƌϸϟˮɫƕ˓ǌŚϷĽ[ąѹá¡ҽƙҸHÐҘƾɃӼĖɕҦӘȶ',
                'ɼϋюΜʒγɄƋ˘ӫǞǰ҄ǵθŃʤâÞř®˾҃ρǎЪΛȿԢƶ',
                'ΐƎ˔`эʲӇ\x84ҾϿԠӞʭӕͶϽЈÕЪȮԫςѾЩ¥ƺӾƾҝy',
                'ѿ/ĥє\x95ԏţΈƮͶȮѬˋǘƤΟč˄è3дϗ%ȣӛѕϪ~и~',
                'ȶ\x98ʽdӶӨʧʗԗDɘԑŠҪПʅЄ7ͽɅмТʩõУʴ¤~@ң',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2557724669783728566,
                3567982313805342636,
                -2210962280292208072,
                -7320067950370880175,
                -7450253954162257822,
                -7410168035048351526,
                1731911557267305222,
                -5019983803666102906,
                -7296943601615021083,
                1021351300499257069,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -37559.66133103982,
                586633.9489741279,
                295145.81140630326,
                -21442.545182099842,
                69140.60975456313,
                577520.0269307924,
                606408.7243316134,
                -93186.50091395125,
                317226.18512017257,
                180384.54888932244,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210909:200612.675831:+0000',
                '20210909:200612.692531:+0000',
                '20210909:200612.709398:+0000',
                '20210909:200612.726108:+0000',
                '20210909:200612.746656:+0000',
                '20210909:200612.768370:+0000',
                '20210909:200612.785361:+0000',
                '20210909:200612.801226:+0000',
                '20210909:200612.817641:+0000',
                '20210909:200612.833729:+0000',
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
            'name': 'ȖϷмԀԖıāͶΤȍOΒEҢЍ˞љɩ\x90ʴʸĪăgʂЅǩу~Ȃ',
            'value': {
                '^': 'bool_list',
                '$': [
                    True,
                    False,
                    True,
                    True,
                    False,
                    False,
                    False,
                    False,
                    True,
                    True,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '7',

            'value': {
                '^': 'bool_list',
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
            'catalog': 'ŸтʔѴÖѾӉĩVӗӘ´ˌȫԊӔčԧĜÐƼɧŖКʘȋŗȕ˶ƺ',
            'message': 'ʩǟʛƋы˹ďħѣđȥİßåЦƐӷĤ҅ʩƷаŢςśͿЫ\x91Ѝʵ',
            'arguments': [
                {
                    'name': 'Ѿɇ\x8f\x94c6ʮӄ,ȻòΧҘǾ;άʞԆ˭\u0380ΝÅкҔ˚˟σɵƠп',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ŪґˏҬвϞ\x9aХÊʒҦ͵ǽ4ǋЉљ·ԈʡΚñĂѐ,ƪ]ŸĨǏ',
                                        'ǤʋŚŶzΤĽҞ±ƌȮ]ǛΌǑ\x80ŲŬɝȆƐԏбǔʬȒȣΧ\x8dȫ',
                                        'ǔâҹġЫƠԧśĽҁ҉\x9aʢȚH˦Αɂðшţ¥ZǄǣ\x9bԡMQǂ',
                                        'ΤǛʼ£ĆČҷǐηcʾɡЇҘǏλɍҤŔЋҺΤĖԨӧIɋĉɡɼ',
                                        '˂Ʃę˒Gɪ˃˯ŉΊϐ˖,ǌˎǄМƈĀİÓϜҸΚȿĊθě˱?',
                                        'ţû҇\x82ɜң!ļџģЫЕǞ˹Иǻ\x91ʮȒʄԭʺȍύöǈʰӘīԇ',
                                        'ΠȬ)ŏñξʎ¦ɼŀēʓΚηȅҍӈϔҵШӢÆȈ¤фģ\x8fͺϐϒ',
                                        "ěƩƥѷӵԐŁčϭö\x97ˇęЋƻȌ¸Ƣψӥ˲'ƻˠpǢ\x89ʛƜƦ",
                                        'ʥȪƕƍȅ\x8eǙYϻҟлĉԃϽΔ˳Ȱɬ˟ʺƧYȣȰǅӨ\u0380ȂȃǠ',
                                    ],
                        },
                },
                {
                    'name': 'ȅĊƞˮǏȽαǼŦԢʚ¯ҳˍχǮʼóx\u0383ҿηԋřđΈӍѾԪʭ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210909:200610.247421:+0000',
                                        '20210909:200610.263338:+0000',
                                        '20210909:200610.279934:+0000',
                                        '20210909:200610.299809:+0000',
                                        '20210909:200610.321069:+0000',
                                        '20210909:200610.337801:+0000',
                                        '20210909:200610.354898:+0000',
                                        '20210909:200610.371670:+0000',
                                        '20210909:200610.388339:+0000',
                                        '20210909:200610.405089:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ØrВWȈē-',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ĥª¢ɨԟԘҊtzΏ˅]ΡϐӸɱǺΰϺμɅф]=ӬǙņeЫŵ',
                    'value': {
                            '^': 'float',
                            '$': 428767.6615589572,
                        },
                },
                {
                    'name': 'νʬ\x98ǊĥԊЍϿȡϓŕŸŢÕΕɊĤʭƵ\x86к.ϷʩҙА\x95įƱӇ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:200610.624213:+0000',
                        },
                },
                {
                    'name': '@ǓƎϙǦѮȂҟԤĬ',
                    'value': {
                            '^': 'string',
                            '$': 'ЎñĆˍĴȊǩ¶ƭ\u0380șǦӌŷ˱ӐΨăȐϢǕÑ^ʠɁϪԢėҗϝ',
                        },
                },
                {
                    'name': 'ʳĻӿϽѮɲȺXȬʾλ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ԔѤʭvȋЛϬΟςǧѦӉ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ʥǢśʬѵɼǝͺȘȰĮюπЭbƎȀŪįİ×ɨγʳΊϽϹԦҖǸ',
                                        'єŪ˹Ѵ·ưǇˁʭ#ŧёĻҏҏĨѴʈԩϤȠЕı¹ÝԔëӦ҂Ϋ',
                                        'Ԇԗτ5śȗą΄ѕӊʕE^ȱΓͳэҸϲǶʪĨí\x8aӢͱȶϡɅд',
                                        'ơˏʋȬИƛÿɳӘђšҔˍЊБ˯҉ҎИӣȡБΘҌƶȯɩƿÈâ',
                                        '^ɇΈȌҭǶϾǩ\x9bãҦz×ˆƷҮǗǙϕ{ȠԦƕdƶêǁɇŮŧ',
                                        'ŬÖϟ\x8dϯлȖӦłƈ?ĥő\x82кƯЕиμƉ:ŋǌ\x913ʂҖøœЛ',
                                        'ͷɻlĦ˝ΈўϔɀаұƟɅǋùϕ\x81ɛɉϻ³Жę\u03a2ġĭȌ²ϳŨ',
                                        'ƜҙØĿ˪ѺѓúƓ˘ύŗΤϗˑϩ\x8aȹɭΎхlϾЕƂѰђϿӲє',
                                        '¡ȾƭǶōΫǊųȻ˭ѱ˽Ͽ9˽ǓҩǠɱ(ȭUƽĨɂǪȐщʫä',
                                        'ǘÃǥɦчӂͶǧҘvƠʭϕɍ`ϐȐ\x87ϛ\x92ËѵǚцĆųԊѼҖÚ',
                                    ],
                        },
                },
                {
                    'name': '\u03a2яyNҰԄΓ͵ԣ/ˡ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ơ˵é˦ƹɀĄƗ®µϷѨ\\ǰѓʃÃˆԍZӇ¦ŃɣЍĬξȖȪƔ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210909:200611.158963:+0000',
                                        '20210909:200611.175710:+0000',
                                        '20210909:200611.191905:+0000',
                                        '20210909:200611.211922:+0000',
                                        '20210909:200611.228371:+0000',
                                        '20210909:200611.244941:+0000',
                                        '20210909:200611.260867:+0000',
                                        '20210909:200611.277257:+0000',
                                        '20210909:200611.293211:+0000',
                                        '20210909:200611.308829:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ҥɢ',

            'message': 'Θ',

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
            'identifier': 'ʯɃŤȊȄƼԆΓιŧsɪŀ',
            'categories': [
                'configuration',
                'os',
                'configuration',
                'file',
                'invalid-user-action',
                'file',
                'invalid-user-action',
                'access-restriction',
                'invalid-user-action',
                'network',
            ],
            'source': 'ɻ\x95ĒĐɖŭňɌ¹ƳħŚȸGѝӷǌɺ\x98ǷŲӿˎsĐcŸƇИ´',
            'messages': [
                {
                    'catalog': 'ð˱ђ˅)Ȅ}ԦƾĲҹɲÜyːɈŜԆ´˲ӔԒЮӶ½ϓϊ\u0383¢\x96',
                    'message': 'ɬ¼ҀϿˋʞS\x90ӺǆиɷɊʲʱͻ˦ɖțғͻϏԣˌҀӌì$ʱÿ',
                    'arguments': [
                            {
                                        'name': 'ʀ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200553.455374:+0000',
                                                                            '20210909:200553.471799:+0000',
                                                                            '20210909:200553.488489:+0000',
                                                                            '20210909:200553.504586:+0000',
                                                                            '20210909:200553.522923:+0000',
                                                                            '20210909:200553.539036:+0000',
                                                                            '20210909:200553.557574:+0000',
                                                                            '20210909:200553.581050:+0000',
                                                                            '20210909:200553.597286:+0000',
                                                                            '20210909:200553.614576:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŰʯԕԕўØYЛÞƵɚÞчʗĺˣҾƘӆΞmɬ\x84ԆŝƭļĶӆѻ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3419714442111840966,
                                                    },
                                    },
                            {
                                        'name': 'ǅƲϠĽɎƩˌЊŖ9ЊʴѵѾɎYԨÌĊɈʳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƫқȑӁɉ®Ƽ˴ǳΑ2·ώĲˡɘǢԡ˴ЖŴɊȞнēҳͷРƻɪ',
                                                    },
                                    },
                            {
                                        'name': '˟κϴЖɧˏ?ӊƺĹΰǃʃɺ˝\u0378ѮȨΏͷҺҹɭЁ҂mҕŵѧѮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2940211614077155526,
                                                    },
                                    },
                            {
                                        'name': 'ƃÙŹԂѢǽԎђ\x93Ѓ\u0381ӪԒȩ\x87ƝŒϣϔʢйҝΕ˱đԍX΄Ϊų',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȧHԏϱǒԞΑΓɵЏέ˛ϋ¯ԧǇԙΊӓцLҽ\u038bЛƷˌʴȥ˟Į',
                                                    },
                                    },
                            {
                                        'name': 'ѢŜүǅŧˎƠϿѶ\u0378˽ƾϺИaұŧηЉҶϹϯľƝΐˎ˗¶ҩП',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200553.980363:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҬФϹуӜÔƎӫȦčłą΄ȥϠҤ¬\x84Ưɥ˽',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'oϳŁ\x98Ө\u0383ψ\x9cƀɤӧ0ʲҺİãιɢΌʇӉɾċѥүʕÊĎ˼ǥ',
                                                                            'ԮˡȽέ#˃ʋ˂ϿWɵƙÍξԆӟÓϓΕºКƻȁșϷǁɄʺɊ˽',
                                                                            'ѷþŴУнѲƮϦÂɳʆʭkɢ˦Ϝώ϶µиӆ˨B˳\u03a2ʹΖЋЂȡ',
                                                                            'ЩøцʆӉϧǳĞӱΠĞi\x84ϨÑԖӟȘp˫ɯʙЬ8ˤˀҭǟѭϩ',
                                                                            ' ѥɈϡЕѺƍϺǉжЇŠҐЧʷ\u0380ɪŭďѮϖΜͶÈґЃѣԗɡǖ',
                                                                            'οʖѶӱѤҠ¶TΪçĿѻǬԫɀuȻͼĬӥϙˇæԏԡŷΌFΫӿ',
                                                                            'ŐȥϛҒˡƇĂҡʎ\x8biŰĊƿʌƏ˼ĴјԢЌϓƂʇêԙ|ƘŰğ',
                                                                            'ӶӹӘԕЎŰǙκY˺ůʷ#ԝԠş¸ԩøƬʤŅРǄźϪŕÙǇĬ',
                                                                            'ɥQӧʨtͿ¸ĴȮԀ˥ɰ˚ŹĬϖ\u03a2ǃӤҼкдØ³Ӗ˲ӲӜƴё',
                                                                            'ȫɴъΑǲύƝʀӜҾːπкλѿШΫҋЫɓЗÂςŦȒŷЇȀŻя',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'vĚǤŃǝлJΊӝ5ǚѩŏϛÂˣѥĨҕʘϼͽж³ˏΖԟǑâÁ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϭ˪&ŸӭЧɋӎǧсřΨоԢʝ,µѫɽҀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 729342.73318555,
                                                    },
                                    },
                            {
                                        'name': 'БιTAƦÏ@ΝѸvǅ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '~ß҉ʏЊʞӲñǞϘҩЄЕRоНv˘ǣºгӋɂ´ǡʰǶϐɎр',
                    'message': 'șΊͿŗŶÈ]ґΦӨдQπĸ´ķɒѻŊРЄɘǳvʍȺŘMʨӥ',
                    'arguments': [
                            {
                                        'name': 'ˑ\x93ϪŬ˔ýȮɧő\u03a2±˗ĩѻˡ%ŒҷԬɕ\x99rʆ\u03802ɝ˫щĀϪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1421575137813731186,
                                                                            -6875958297649696226,
                                                                            -5103063227531130752,
                                                                            5719954339872567246,
                                                                            -8049761317248169154,
                                                                            -3714680567818220928,
                                                                            1997141921797947157,
                                                                            7818257975340589336,
                                                                            -726913382697135728,
                                                                            -4778605653934519166,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'AϙьºĕƋƐԟϊğɎΑ´ѯ͵',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200555.140100:+0000',
                                                                            '20210909:200555.158562:+0000',
                                                                            '20210909:200555.178429:+0000',
                                                                            '20210909:200555.198672:+0000',
                                                                            '20210909:200555.215360:+0000',
                                                                            '20210909:200555.232936:+0000',
                                                                            '20210909:200555.250256:+0000',
                                                                            '20210909:200555.269665:+0000',
                                                                            '20210909:200555.287802:+0000',
                                                                            '20210909:200555.305245:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɰė/ʂĵƄиȅǲϓн¾ú',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҟйҼɜɳ/ń!ǥҎԂʄ¡ƀ˫Þ¥ҧї¡\x8fɊćЋBƄӺɽ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4343593046252340831,
                                                    },
                                    },
                            {
                                        'name': '˺Ԑʒ϶ҬρĭƐѻ\x98Ɂǯѐԛȅ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200555.551974:+0000',
                                                                            '20210909:200555.569776:+0000',
                                                                            '20210909:200555.586501:+0000',
                                                                            '20210909:200555.603858:+0000',
                                                                            '20210909:200555.623695:+0000',
                                                                            '20210909:200555.640858:+0000',
                                                                            '20210909:200555.656959:+0000',
                                                                            '20210909:200555.672727:+0000',
                                                                            '20210909:200555.688937:+0000',
                                                                            '20210909:200555.704687:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѾϮΉҳąĂЅѦҗȯƙˮǏ҉ѡɩϪьÝʂʑϩУԇϺˎԐНĄϾ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҅ǄЎ:ˍзҹďł}ΜӂҚԊƽќ\x8dӫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200556.050690:+0000',
                                                                            '20210909:200556.067866:+0000',
                                                                            '20210909:200556.085356:+0000',
                                                                            '20210909:200556.102430:+0000',
                                                                            '20210909:200556.120429:+0000',
                                                                            '20210909:200556.137540:+0000',
                                                                            '20210909:200556.154137:+0000',
                                                                            '20210909:200556.170504:+0000',
                                                                            '20210909:200556.188200:+0000',
                                                                            '20210909:200556.206185:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˌЭÕɮ˰Ʋ[ҌƉ)ŷʚȮ˲ǝ8ΜҏƃɞϩԮɆƐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -50882.91471217965,
                                                    },
                                    },
                            {
                                        'name': 'ƆǬӎʟʺÃB|\x81\x93ѥЏcАŭȲȇˊįˆυөʉӣн\u038dӰ҅Ƈ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'љѐӏϱʼѭϔ÷ϤыHӭφĕƱ°uɛџϑͰȬҞȚȒɮϰƓ\x80®',
                                                                            'Ӕϡ˸źêǗʗӀ˸ŻҧОīƞŘӂƦƘɦÚӺ\u0382þԚК˶Ȥқ®Ϫ',
                                                                            'Ϳйƿ\x8e7ÏĦӀўƣƹ~NȃÀф|Ϟ@ɢ:Ω>\x83\x84ԃǖǈǗȿ',
                                                                            'ӲπȩΝӣϽȵěșʦҥĉˢԌȘáвĞЂʘ˝˵ļԗ\x8bĶĬZµ|',
                                                                            'ϬǸΌʅȂx\x95˵ОǞͲɓ\xad~ɣӱԋʙӸϑԨҊ÷ťϯҩЕϏ#ȿ',
                                                                            '½Т҇ΙҹͷӯӰȲaǒǂȣʸҶѾѶɕϹϟ҄ҢȾДˣšжæğσ',
                                                                            '҉ӒҔФ҄ťɻɦɑƄƟƚЦŨϋԌ;Ũьġ˖ǣ9àӾƴƵǜΆШ',
                                                                            'nȹǿΟϽҢ˷ǯʯɁ˔Ӗ¥ҪгƄȑӧɢƽőǚƏ\u0378ÅʦħƮԕ\u0379',
                                                                            'Ҫэİĉȹ˷ӝўˉԫЅ҄ͶɷȫǬΚʱĴŚĂџjϭǲ\x82mƋ2ΐ',
                                                                            'Ӿƚŧ²ѭȧĲ҉ЖɔԑȠёđȸҎ\x86ƵԟΤˮЦpүѪԁžǜǱĘ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǊԐÃƛ®ҡ˄ФĳМDҦΓ\x7fŞŏʠυ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԙѼΉʷǎɁϘБˈôłΒ\x97ÄϝġƉȓѳδɾӸԅƸʚ\x90Ɍ·Ǜɬ',
                                                                            'ÿĶыϜѫұщτ\x8cӹģӓʑϽɲҕ×ўƭîˆĴƢξvľʀɣϬĵ',
                                                                            'ŠŃ҂ĺæӷŐǒƎtƕȫѠ38ɯ҃ʶĽɱʱΫКđ:œςŀǽ«',
                                                                            '˨åǃüɦįˮÐǥ1ɢѪͰύ˭ʽƑńɯóɣ\x88ǃͻˈƶ¨ӯʷ\x94',
                                                                            'ȭŰҽԑƕϺžVщϢѢŉΌȆҜʳʫχ3ΪíÊĸԇÛǳ\u0383ʅηɨ',
                                                                            'ŶȈ"²\x9bŜыӏŸԓχĀšԜϓƆӅѤȟȣɊцȒȢˏ\x95ЏΑϋʃ',
                                                                            'Ɯë\u038bʇэнŌӐͰҷӞδʓbf×ˊΗɋң˽èƊǂ\x85ЯЬƦԡŋ',
                                                                            'яͶưËĠƇӚʎ{ʩƝǹӍʼфɶɞčʟӽǰƗ¡ˈIϖѝɅþҰ',
                                                                            'ӖȣҽШÙ\u0381ǱҗĊȾźКÔɛΔԠŜ±яЎȊɍԨËƆƤ\x84ɮʹ\x93',
                                                                            'ǿѽÈԑϵ5ªѮŹϺʟ!ʊϲҚ˞Ԥ]ŃųҩŘù\u038bυʜ\x97ǟЬǠ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɠ$@ЈӐɔ˶àԩǐϪĻφǢÿĔ3ԊňīÊ^ϋýÏǷĜȁȠ\x8f',
                    'message': 'ɈƠ.ɟwΐʞëțǄĻǲǠŘȚͳEҔǃȜϿǮ҃óʋʆѬӹ˻Æ',
                    'arguments': [
                            {
                                        'name': 'ʝʺŲÓШ\u03a2ͲāͺŎˉºжÓәĊҢԍƹɯԅȽс\x7fȎϘ¸¥ĸѫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200556.920759:+0000',
                                                                            '20210909:200556.937994:+0000',
                                                                            '20210909:200556.954849:+0000',
                                                                            '20210909:200556.972312:+0000',
                                                                            '20210909:200556.989197:+0000',
                                                                            '20210909:200557.005403:+0000',
                                                                            '20210909:200557.021698:+0000',
                                                                            '20210909:200557.038027:+0000',
                                                                            '20210909:200557.053876:+0000',
                                                                            '20210909:200557.070423:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'κĬȓ¿ƇϛЋԛͼϿҿэȥíıϤįΤЯŶć',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7650303605268794637,
                                                    },
                                    },
                            {
                                        'name': 'ϔƄ\x9d҇ǹɚͲ΅ŢǠӗҳˇеƭ¨ҹǆͲΩԂŕе\x88ÏƀӏӢĪí',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2963003125222799952,
                                                                            -7459414249797410740,
                                                                            -3778217295116752042,
                                                                            3474614809142657952,
                                                                            -4492856826897545629,
                                                                            -3912341643865751376,
                                                                            -5111575353001928725,
                                                                            -7504668234245490638,
                                                                            2369108835608102334,
                                                                            -8537979733876023241,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'vÍơБ·ƺUЇҗ$\u0379ӷк%eʺ1ȂӦŹŀͳӛöАɗʇ˟ȝ]',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȵǑǗȬɉˠԆқŝĵ\xa0ζɿӵ6ıԝĜŘǬƨȑЎʉȼнfϺʣԮ',
                                                    },
                                    },
                            {
                                        'name': 'ωɠˆƀȴǗÄɞϕ\u0380ӻɢѡŖǑŅҁƻŹѧƎȳδȭҀΊЦӤ˔ō',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƈžçşôЂəĹͰ˩ʗѰԙȞǟʴÊȢʨûΕ>ίΎиǊɹȮѪú',
                                                    },
                                    },
                            {
                                        'name': 'ΣӾţԙƔƕ/ǬεиÓɔђĩыíŤΛӪ˔ȢαǼΓǗɌ\x85ϛґϰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˱Ԟaʄ¹ŪҦцЫōĩeýŕʺȻɳŵњԩśʙȼȻЈ\x8bдϫɱΦ',
                                                    },
                                    },
                            {
                                        'name': '¿ȫƜɑ\x98ԠoɸXΙɸǙӔϹϱьɫʄ˛Ĭ+ʱʀȬʷӸӮ˫WӲ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7097319289082942861,
                                                                            -6265359243371818090,
                                                                            -3894478754834505301,
                                                                            -2810922420626325601,
                                                                            2190157972256340101,
                                                                            -985541348460087378,
                                                                            -2937686013043982259,
                                                                            -8547641205760887225,
                                                                            2285358222731859053,
                                                                            8457955325423901196,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9eϜȦœθűʧƄԉґĐɃǇeñӂѸ¿ҵӑĲ\x90ʣţɈƜ\u0383Ҫǯ˱',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200557.957582:+0000',
                                                                            '20210909:200557.975074:+0000',
                                                                            '20210909:200557.991085:+0000',
                                                                            '20210909:200558.007279:+0000',
                                                                            '20210909:200558.024332:+0000',
                                                                            '20210909:200558.041523:+0000',
                                                                            '20210909:200558.057637:+0000',
                                                                            '20210909:200558.074215:+0000',
                                                                            '20210909:200558.090776:+0000',
                                                                            '20210909:200558.107794:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǨӎƱˠˬɑ\x98ʸÅƧΡłāӨĪ\u038bʵӹƸЛȕОǳĦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 810136.2446649623,
                                                    },
                                    },
                            {
                                        'name': 'ɕŵƳŇ{ӑʏĕȨԒʔгȐԚƁµʈŊƏӹȦƧɽЇΨϖЋʽĢϊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĺʎƋĲÿʸâíɊ6кϺCšжʡŭɷ#ԌԏǣϱѼϋȁÿρĬˍ',
                                                                            'ͻӈԧǩҘɓϧΈǏËΆģUӍЙʤȿǼ\x9aǨсҀψоҌхϡtѡM',
                                                                            '~ϓ1ԙѪɜԠĻEÅƣψЎҒƚӰ=ħ\u0381ӡЊŚkʯš҈ӖŚːˎ',
                                                                            'Ѱī˦\x83WFìҿе҆ȾȨĲȪɹƟ\x98śҥųкúԃ`ѭʊʺʞѽȫ',
                                                                            'Ρ7ńȞƸɕʎӽĦœǋɡ÷ѴƝ³БɹȋÓŅĭџөƖĐśč˙Ā',
                                                                            'Ϻˉ³ЂдǶӐî˭ҭ?ɲϠĹѭγˑ9ûéӇȴѲѥſҋқΟ҄Ѵ',
                                                                            'ȬЁìȕYΓɿ\u038bʻ@ƏƁҧʂ£ʅØдπĖĽυd˷ҵlɔxʛƜ',
                                                                            '\x95ǗҨǿҿ\u0382ГɢČĮƾʖ\x80ѰΐΤƕyŢǗƬ~ԅǞ\x9fЦǺԟ϶ԏ',
                                                                            '\x88Н˕ύӢqΒˉ\x90Ār͵ѪǛбÃ\x89ƝӢòÛ\x98Ũȏ`ҳЅυ˽Ʀ',
                                                                            'ғћˁɡ\x87ǬͻӬïŜǌ˃҉ɖĨӤµӔћҟ\x9dӽɷǩƐŇà˒Ɓρ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ťĻĺЪøċʛƷΐӱψȥȳʬϬAǦŀɋƨŬчӘŭ˶¨ӒхҬƠ',
                    'message': "ɰÕpɄǙǭоҲ'ΡЪǩϐԚŒTӌНGźˋ҈ōȁԪβοѐ3ҧ",
                    'arguments': [
                            {
                                        'name': '·ӡΡҥÄúǲŔŰΈ\x92ĞΑ\x80ÖȞƧɸԘ¡ԊīʘĖƯƘʳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200558.571175:+0000',
                                                                            '20210909:200558.586979:+0000',
                                                                            '20210909:200558.602860:+0000',
                                                                            '20210909:200558.619888:+0000',
                                                                            '20210909:200558.635641:+0000',
                                                                            '20210909:200558.652672:+0000',
                                                                            '20210909:200558.668476:+0000',
                                                                            '20210909:200558.684292:+0000',
                                                                            '20210909:200558.700574:+0000',
                                                                            '20210909:200558.723259:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'λȨïҡĽ˜ůÙȣҔŊȜgȞȳʠǰҪԒɕԃϬЮ\u03a2αɝƻщιҹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ň˯%&įʈɜǚʟԅΪĬƷ˱ėӀʍӺӱґΙъͷƌϴњϧ6Àƞ',
                                                    },
                                    },
                            {
                                        'name': 'ƮѫʵҺѴɔʂíŁѲϓӌӻҹɋӒϊЖůԚɯƟɱö"ɤӹҧΨ\x84',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѡÎśćӗҷ@Ԡɷζɇ˧ӅəKѓƌ<ԢύԩҼʳόΈНȴƯŕќ',
                                                                            'ʸԘȅԭǚĸҾ˻ʙƣӺ¿ɌΉȑΉhοǵQƚсϺĆĖƌҚΟγŕ',
                                                                            'Ĝɮ¦ŐȴЖЕԌIl˝οΟȰƭɖӊҊ¦Жҫϑ^ĴÏͷ҇ωˑҳ',
                                                                            'Ąк˩ΔĀǣǴòÇϴЯ}ԂƐȁƸџǷĹĪǱБӆ\x89ƹДƀƹшǥ',
                                                                            '҉ůΈǫϝɇƷ˔˅ʙԟɺҦʏʒ˕ƔʓϯäŖϴӵτȲË"İv˅',
                                                                            'пƮбȓɁΙzК\x90ϋųűԮƮ$˅ӎϵĶßȾΣӚáȺөãѓӰa',
                                                                            'Ó!ЭϖόΑǱ>ȩʹǪȏƷЃĿƅ҆ԮĭˋͲВɷшѩKͶșƺĻ',
                                                                            '7ÿǅîλԆБƫýȹŉɝ҆έ¥\u0382ѴΒŧӴқQӞǖ~ƬӴҀɣƸ',
                                                                            'ԃ>˷ѝʞнςҋʷ҈ɫǨѴo?ĜVϔöŹǸUó˓`QȵǅɆ΄',
                                                                            'ż\xadĕʁөśɴιѡɸ%ķȀˈϢЬǛëɸŉϿωɵӿƲæеѯʃȳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȗϋ¸ɵɚ҈ĴӮÓҡa\u03a2ӣ˪\x9eƏŮȬÏǸүƞ¯Îʩŕˊ˄ɚÿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200559.143269:+0000',
                                                                            '20210909:200559.162574:+0000',
                                                                            '20210909:200559.179985:+0000',
                                                                            '20210909:200559.196249:+0000',
                                                                            '20210909:200559.212490:+0000',
                                                                            '20210909:200559.228981:+0000',
                                                                            '20210909:200559.247483:+0000',
                                                                            '20210909:200559.271077:+0000',
                                                                            '20210909:200559.287818:+0000',
                                                                            '20210909:200559.304192:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŝɣƒ²ҭЛήіľǭƮȦЬɜӄə',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200559.387299:+0000',
                                                    },
                                    },
                            {
                                        'name': 'įǮͶäŸ͵ɒҍʟƴҀɡʿNБĎϘΨҵԐůӱɏŴ˺Q\u0383ʵҳ%',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200559.451364:+0000',
                                                                            '20210909:200559.468424:+0000',
                                                                            '20210909:200559.484554:+0000',
                                                                            '20210909:200559.501306:+0000',
                                                                            '20210909:200559.520069:+0000',
                                                                            '20210909:200559.542297:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'nɹҫГ,ҕŶӱЗʟԎο²Œɂɦ:ɸÓϾďÚ;ɷЧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƳҀԛʥ\x8fī˙ПϞәϾǉͱшŒԮӴɂӿәʺȹPѧ·дǪеў˟',
                                                                            'ˇѮϐҍʛéʡȎėǏ˶ĄɊƃϙŐÜϊԔҔНŗƱҒБÊңɦÓ҃',
                                                                            'Ð¦ăʽΞʬΔҢáԮʃӴŒƓîώÁƲ\x94ӭӍ҇ØЋЎƾþɕǖǯ',
                                                                            'ʇˇƞɑýÕɖHɜQŞϡѐʭԉƎǪȚԙÈϞҎȘжҬǣʮӅѧЌ',
                                                                            'ѡь\x8c\x86yӻĤÏǮɤπԝɼÒы.ӤȥІȃÉĥҲѿ˞ΡǸƽәҬ',
                                                                            'ɫêĝйʀĈïҫӏ\x8fɖѤκʻҹҒĎʇĦrÅǚƒʾΩǺӴͲ.\x88',
                                                                            'vРԬҿ˛ɼёοɖƚҦɪɥŀƹȀƢӈӃ\x91ʻӊ\x8bƍʉȓ˔sƮǜ',
                                                                            ' ĩҪŚ\x82ȸóİưƺƕÝǶѨŒњϟ¯ӏЫŹҧƩƗɇҝΝɺǦѰ',
                                                                            'ƴΜʚ3ʼǐ¹ʪȶԐʝӑǪԊӖ Ιҩy˨Ӑ\x7fӝϾŅεÊӓҷĭ',
                                                                            'āњЭͶӅQɱŖʷǕӫ҅ΫπɝӅϜэŇԤтԅŲƻчЎЖЈӿЩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '÷',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200559.880660:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŪӊʕӓſǕϜиʏȯѢsҩϷɌș¨ćďOöˆ҉øȰԥPϤ˧đ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200559.947003:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x99ʼ>ҝΝϹʶpӓ÷ʺɥÖԮҽψɫäϤʾÑѦĥӈÃ×ƴψӭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200600.013592:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': ' ДkѨΪҼɹɜɔņϖƐϪŀɮХԒ˰МʦˌǈҴlǗʣЦ',
                    'message': 'Ԁ\x9fǞтʤ҄ԙϴϷƲTʭƻˌǑɩŚ¬ԐΘ҂M\x82\x94ǏĤӺ+őé',
                    'arguments': [
                            {
                                        'name': 'ҚãІǲʃӴˍ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200600.150695:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҖӝÒȢϚŇQǀ\x9cƧʣȡҬѿӏÜ\x83áϐ\xadFΚ˰ǈ:ȝҝɰµ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4630611518051008474,
                                                    },
                                    },
                            {
                                        'name': 'ô',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200600.283613:+0000',
                                                                            '20210909:200600.299817:+0000',
                                                                            '20210909:200600.320000:+0000',
                                                                            '20210909:200600.338713:+0000',
                                                                            '20210909:200600.354498:+0000',
                                                                            '20210909:200600.371277:+0000',
                                                                            '20210909:200600.388220:+0000',
                                                                            '20210909:200600.404413:+0000',
                                                                            '20210909:200600.421032:+0000',
                                                                            '20210909:200600.438237:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˏBЉǯǧúѥʂǣ\u038bƏҸӃǊûɥΜΪͻԘΟΛãȥ\x97ƭƙŷͱӮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѪӈθƁСõɂţɀƖɳԀş\x8bԔЍʣ˶ԒФą\u038bҗȀº˪łѭάԂ',
                                                                            'ǗĪҢϭͶάǬǳώʉɓӋÂԠӧ{"зƜ\x8aӖϳeϐ)ȎÇʶ҃ҝ',
                                                                            'μвϜәъʯ˫ƆНƿЀΐϟĭҦЏƚЫȡÕűţζǯŏLʤӎғκ',
                                                                            'ƴ҃ŮˌԠȁҿǐӷʂӥŴǙ\x9fёԊşïƾέѰʾĸԖˮӨˣӤ҅ƃ',
                                                                            'ɌʷЅǃңɑ(>\x9fθĆʰť#éûӂțҜIĿ;͵Ǩ1θŞƱѽ\x8a',
                                                                            'ƝǒΌĵ\x90˔ԫɗĮȸʲƫĪҭ9ɞǚßӖȟζʝģĈ˕ͳіԍͳΊ',
                                                                            'ǪȌЪÎЂɾǫȯÁҲԍʽҍě\x9aĻϹâͶŻԁÄˑˉђϽƵ¤ŃѸ',
                                                                            'ŝ\u03a2ëѻòӕËϒҦÍϯǱ÷θϚÈǣ˽ˀƆȫäӈ\x9cѸ÷?˽Ͻ˒',
                                                                            'μԫԢеϏȊHȘǐςвÊňşȢԮÈʗ¼ԬŲčāsɕÞƀŞȝӼ',
                                                                            "źͺ¬ȗԖѠʪʗ҈ÜɮҶГǨϛâ'΅ҫȵ˩ʥÎƱɰȭԛЕ˸\x8a",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '«үҰԝԖíωǞ\x82\x91Ȁȉԛѵу«ϴ²ЛǊɺTҸХɖÜф˩=˗',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʖΏԉȎƢƷђ¼βːʊϱ˟BʹƾʘȄ҆ȴύ¹ʹαă¤\u0379ƄϫЩ',
                                                                            'ǺѱȽ˳ӳɤΤЭіӸľʵҚ˶ԇΠЋΖҼȨӱͺїѵϹǨǼћɈӐ',
                                                                            'ҒȽϗŚóŃĕɍ\x9dЗτļԂ˚ǷfȇѹCËÕԒȜʹĶΚĭɌϗǤ',
                                                                            'ġʧЛ¾őԩ\xadLΈPӼϚϴ\x8aʺĐԣо=',
                                                                            'ȵƉǡȜĥб\u0383ȧӴ`ɒҿЖԩ!ƾ\x83ĉ\x8aǞόƷ,ȝė˶Ķʛ\x87ɹ',
                                                                            'ԁɒšǖˀĊ*ńʑ&\xadϭцƨøʅўӥǘɳçý¾ʢ\x86фÌ\x80Ƞˎ',
                                                                            'ɻτsϷǉïN˼\x91ʆ;ĸ˲ƒҸėɿ\x92ɣķќΐǥ×ԜϦϏǒԢǓ',
                                                                            "ԩԮƛԏϐҝϪęμώσÉԪ\xad˗ϞѨӵˮ3ӓ¢΅mʍeK'ϴԑ",
                                                                            'ȶ`ӤåŤĩѷҼŤȭҗÁÆϥÐ˞цʭɃΣйʻӥӘ°]ÿȣɀԨ',
                                                                            'ǳҤʔЀ´ɉЂʬȧĥɲӠĜȪǠ¨>ԛЦԇҏщvŽţԠӂƫҖu',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¾ФŜʄɉĀýʤiԭΥţƣ\x8c҂˼ȥ\x9eϛϯʵϙ½ӶɼЕZɔϩ˸',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 269752979283365968,
                                                    },
                                    },
                            {
                                        'name': 'Ϩÿԑѧɐϊĝ9ŕǜϔǦȿ¶ɞëºƸǦʱȥӖѩȾԝgŞɶτ¾',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200601.084187:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΘǈŜʣĩǲϘӒ5ñNČϒŊϘĳ\x9aǗ΅ʊɝɱΧŔʳѵĐåKğ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҅YÀǉϮŵ˕.ӡЋ˄ɅƲí¼FÐӐƟɄʼȌ\x9eҞĚÙéӫZƻ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200601.418467:+0000',
                                                                            '20210909:200601.435691:+0000',
                                                                            '20210909:200601.452505:+0000',
                                                                            '20210909:200601.468891:+0000',
                                                                            '20210909:200601.486768:+0000',
                                                                            '20210909:200601.505381:+0000',
                                                                            '20210909:200601.521353:+0000',
                                                                            '20210909:200601.540611:+0000',
                                                                            '20210909:200601.556464:+0000',
                                                                            '20210909:200601.572888:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϧб',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200601.657158:+0000',
                                                                            '20210909:200601.682340:+0000',
                                                                            '20210909:200601.702982:+0000',
                                                                            '20210909:200601.721762:+0000',
                                                                            '20210909:200601.738745:+0000',
                                                                            '20210909:200601.755206:+0000',
                                                                            '20210909:200601.771063:+0000',
                                                                            '20210909:200601.788461:+0000',
                                                                            '20210909:200601.805246:+0000',
                                                                            '20210909:200601.822821:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'áӠŔƁŦɲҤǶǢɊԢʦ\u0381ï·Ɏſ\u0382ΗʄʈѢӔсƞНҸϡлӛ',
                    'message': 'ЙćˡƸʷäҍɟʸ\x9fā)ˉԜ˥·;×ȥ\x9f˯ƸӬɧɾҶȌ˛ɔҏ',
                    'arguments': [
                            {
                                        'name': 'ςҳΩȄɍ\x8aÇƆԜӘȊǇӖҞƛЄҪЎҤÌĶҨǨđθӮjÀɧ˝',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 791560.9197911936,
                                                    },
                                    },
                            {
                                        'name': '˂ТōȚǋԨщ°Ҟ\u038bÃ_ΞϜ¡ӠʂΕʹʗ>ԡԟЬƱȉϾƏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'љѫȗЋËn´\x8fͶʑȘȩRѶ˽Ȁ˄ӠҐ\u0378҉˶ЬʾSɹҟÜş´',
                                                                            'ψǴӽԨǯKʙжμ>N³ҿǋɴɽџϛň¦ҡ8˩ԈԐ˷˯Ήęѵ',
                                                                            'ȼ(ǋłʑϕʕӲȝѻĪͼʷʈ¶ςĻ\x93чÕԦѧÑȁҬʣƁ7ǇƼ',
                                                                            '0XѲʭφŃʠӍEņҵƱцͿÒʓϮğʝʠȗϣУĪҞËçōͲɦ',
                                                                            '˛ԛ#\x9cvϞɲťűЗǳņªϨɭӠџӲ?uЌ\x88gљҍʨʑ˞ãз',
                                                                            'ɨɐōăҡmҟвxԐҷΒюȾÏ·ɵ\u0380ȑ˫ϔϿѡϞŕҭȴʢРҟ',
                                                                            'țǋɦ˽ƒȧϋ˕ʯʟɚҤɛτʮʴӅȁѿ\x92\x87ö\x9aɸ-ϯҊǎϰƮ',
                                                                            '\xa0ҵWͶūƋˇƥˉ˅ɤ\u0378ηӅϬô0ӃʽшĲƐұʀˆȗҽÄНѣ',
                                                                            'ԠĤХψϼҞÝʶ\u0382ƒϿɑӛęĔʸ\x92°Ф\x81ĊχͳIϢ˂ŲȲìŎ',
                                                                            'ӳƲԑАαӧӟǊΜűĮԓǌћťҧ˖Ɂʈπί\x8aӓΰνъɶǓƱʮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǥӮѲǰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8962432200510349971,
                                                                            7084315830293176126,
                                                                            -8062606202993749287,
                                                                            6995443550161917847,
                                                                            -3047376107691975260,
                                                                            7180370815207908642,
                                                                            -6909368747466178237,
                                                                            -159216374104936895,
                                                                            -6221834937295722052,
                                                                            1960957556927467706,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8eȄ2ѼЁ2ǲÒ$ʂʫƦЋȪӢźԃ˴ϤÊӪȮQϿȯɌCȴЊǗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8991691038573564190,
                                                                            -3652930696341157790,
                                                                            -5992769226252243843,
                                                                            -4816205284126675711,
                                                                            -8171232374569741303,
                                                                            -5267334305868629310,
                                                                            9065757167449106640,
                                                                            -1127143938012599312,
                                                                            7373960878304552784,
                                                                            8962296186294699103,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˖џʗȀěȁŕҊϖ[ԏώҗɎ˒ˌ\u0379ΗӼūОõtНӌÞҌǀĆӸ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ѓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1348816779262014865,
                                                    },
                                    },
                            {
                                        'name': '\x8d2ɌïΨ\x9bʃƎƮɢ˂ğȭͼƥɣ£ʸӂӀ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200602.894536:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΎʤɛӨяȿˑƛ¶ƘԉúΖȔǖΗԌԛˀ?ĴҴϢƥ,ǋ˻Г¶ɦ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɶǼԎѺȤӿÎ¼˃ũŢȦжʚʤèǿ5ǥʄΡɏԖŊϒ˳4ȇʝů',
                                                                            'żтӅŸȹϗɨƩҋѣȀιϲģɝɑ\x9eƓϽȽȔŎԬǍ~͵ϟұŢӔ',
                                                                            'ҁÝ½ͳ>ɮÅϓηɼтʇoӤĬɲЌԥͰĦ,цΚЉČГϣ˗éϖ',
                                                                            '҇Ãӆ˾ʊÍЄìӟÑąŸ\x8dưŇγʍ.©Ϧħʉ\x8dҫΰǙΌÅ¤ѓ',
                                                                            '˔ßÃѥƟҋķǠʦѨK\x99uƄʴџĉ϶ʿѝˤ˂Ѩɼ˻·ԭԓǉΫ',
                                                                            '\u0383ϹŝǮćĀɂȈįϿԐцſúǯϙȬѳ\x9e@ȟǺ)Ϻϙśȇӓӿԙ',
                                                                            'θњȢӤɯωҐ¢ļ¼ǩϚ˰Ι¶ƎÉъÉʿ$ƦЏpԨκԎőǻϨ',
                                                                            'Ǎ+ίзΔ\x83Ѻĵͱ҉ʾ¶;ĝ\x87ʽʿȺ\x9dԍӱĝʘÝÍɮÂĈţ<',
                                                                            'ſҭʜ\x82ƒğɕéĉϐš˜ΉўЭźҬγɕŬϘҫƽǒɲͻǙȭнû',
                                                                            'ϭӚ,ϻȱΒ˴ǥɧɊ˹@ʃîɎİˉdҏǕӜƣ[ƻɥѧ\xadҎp¯',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӾѱƱpɕ҆҆ñїςΫ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɡƮƍː³щʼʑΛ˕ʮÝˬ˂ǡыͼíŌïЏɶβ§ˑ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʌƳ;\x9dͺ#\x8dҲŉɞɯ7ǆÈɡnͲèʲ^вũƸǠʨ\x8eƭȺѺƽ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŦĂɄĆѰΠØϷˎЌbþӄǨȟԭҟĪÄӤŭғ˯ƱϨѝˉGι:',
                    'message': 'ϩǘöʯӼɵɆϤƟҌȇ\u0378ΔҥĖˊϓђµǟŀ\x9c*Ƹ҈ЯƬϒоҌ',
                    'arguments': [
                            {
                                        'name': '\x82Óȡϰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1123279729760237685,
                                                                            9031090091649674265,
                                                                            -3480792113516071190,
                                                                            -156854848443267280,
                                                                            9177830016527635064,
                                                                            3319839558739406775,
                                                                            677121788564797404,
                                                                            -3158740174548143390,
                                                                            -2301210557244125365,
                                                                            3948402163391311149,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x87ʨĿӠͰåƀ˺ƻƮ˧*ŀЭƫˀ˵lĘ\x8dȌĤbɅӅӷĴIԊʟ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200603.759222:+0000',
                                                                            '20210909:200603.784224:+0000',
                                                                            '20210909:200603.827972:+0000',
                                                                            '20210909:200603.852374:+0000',
                                                                            '20210909:200603.869584:+0000',
                                                                            '20210909:200603.889152:+0000',
                                                                            '20210909:200603.906028:+0000',
                                                                            '20210909:200603.923557:+0000',
                                                                            '20210909:200603.942222:+0000',
                                                                            '20210909:200603.959130:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƼϷsːÿ\x7f˳K',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            840996.0276205202,
                                                                            868680.314124453,
                                                                            82655.79002113044,
                                                                            389077.86137656326,
                                                                            268007.10793558945,
                                                                            280165.04414328694,
                                                                            359664.5803941574,
                                                                            912220.1858820503,
                                                                            655024.3707550816,
                                                                            677727.1425920039,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǫɢ)ȕБԊªΣǯҢҎƗԣĢƹ%ʵϽŁdˈËϺљΗʖώxϊ1',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200604.289895:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˋμo\x8föʗȎż¨zѥǤʇˮőƦʀϸ˵ӄϓї˝iҪƷÙˮӖΔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Щώh˰ÐӀˌϬ\x84ŮĽϢїǵϠYӚϥχˑҚƲʆɖŵǄӘͷˇȮ',
                                                    },
                                    },
                            {
                                        'name': 'ϪԃʮɄӶ\x87¬Ý¢ɵϣ}¤ǆ¢җÒǨҐёӾȒģ§ɎƅƣϔЩԩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɜǨЩƄEѬþſÉο;˓ЮŵpńѺ8\x82ʊƞÛexЋϐǔӞћŶ',
                                                    },
                                    },
                            {
                                        'name': 'ӡȬĸɯҺ3ͷ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200604.507307:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĐͱɭˎʤȶѣѐŽɴ҂ÌΥk',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 649733.6691256495,
                                                    },
                                    },
                            {
                                        'name': 'ʢΘtŗЯĉȖˆʟɇBµж˫Ҙ˴ҒѝξџϏǢļқPƥƕ¶ӯѡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -312128263542943315,
                                                    },
                                    },
                            {
                                        'name': 'ɺŌŚĴԎgƛȭϫȆƲéŊφзңǨʻį¾\x96кƌӘƭˆϙʧϷƂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            400435.71665549645,
                                                                            676777.2996784193,
                                                                            103011.06094562385,
                                                                            934487.4594764699,
                                                                            623906.6282388073,
                                                                            186212.36064009432,
                                                                            235008.76298896846,
                                                                            755218.9287152005,
                                                                            23007.64634517004,
                                                                            -18176.306457001934,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƕʫŸǾǈԂ\u0383\x88қ¢˝\x97ʞΥŏԪƾΒ҂ѬήɠːéϏĹǍê`˷',
                    'message': 'śϙΠͲǒ¼ΒÖξÔІƭ˕үƗЛïǘƠ9ê?ȉϙÏźϩτȑ}',
                    'arguments': [
                            {
                                        'name': 'ɕΚěҩ\x82ԢǚЫѲҾЖєÔγŰƝϔʠƭŨŕÿɮҊϢʛêԀ˔¨',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200605.034146:+0000',
                                                                            '20210909:200605.050614:+0000',
                                                                            '20210909:200605.067611:+0000',
                                                                            '20210909:200605.084617:+0000',
                                                                            '20210909:200605.100898:+0000',
                                                                            '20210909:200605.117833:+0000',
                                                                            '20210909:200605.134283:+0000',
                                                                            '20210909:200605.155617:+0000',
                                                                            '20210909:200605.176574:+0000',
                                                                            '20210909:200605.193209:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԂҀƽ}Ҿǃȃξ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200605.277288:+0000',
                                                                            '20210909:200605.294214:+0000',
                                                                            '20210909:200605.310855:+0000',
                                                                            '20210909:200605.330888:+0000',
                                                                            '20210909:200605.347750:+0000',
                                                                            '20210909:200605.364448:+0000',
                                                                            '20210909:200605.380659:+0000',
                                                                            '20210909:200605.396307:+0000',
                                                                            '20210909:200605.413572:+0000',
                                                                            '20210909:200605.434965:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҈\u038d°ƋҜѰзrâʏïχ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8140956896693163412,
                                                    },
                                    },
                            {
                                        'name': 'ԅáF',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӣ\x92ҒǲϽԉɤ˕ǇйЦǆ¡¥ǜƙwŮǍ;CҠiʩŌfŞӆ!ˀ',
                                                    },
                                    },
                            {
                                        'name': 'Χ_ƘҙĊ&ӰƖšҗȀȤωӸǝÔͰĀP\x9dƙ\x99ҳʛҳ·тÅ\x91ϫ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 840431.9429864307,
                                                    },
                                    },
                            {
                                        'name': "ζĦДÈƴ'ǋ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200605.738709:+0000',
                                                    },
                                    },
                            {
                                        'name': 'фԘƍӎȰʊӁ<\u03a2ҜЖĳɻ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\u0381ėІ}ԎԒĒ˽ťĒƖ\x98ϋЕŎ.ȁɓ×ȮŻĸѧƿʝVўʻҜƕ',
                                                                            'ȮǄ¢ʪĹЏƚѨԣиҟUҗ}ǣÀéф#ЏƤȟз\x93ʇ*ɬ¯а\x7f',
                                                                            '˒ʺҴΒчӋϫɑΌϕ\x83ǇɹԚӎҡόɒͳ\x85ˀʴ¹ƻϿ˳EĜŶ`',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˔Мjȇ\u0379ƼєĝҪē',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȤŊήƅͲ\x82ΰ\x83ȗъӮΊìӵ\x81ӷïɔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200606.035219:+0000',
                                                                            '20210909:200606.052068:+0000',
                                                                            '20210909:200606.070501:+0000',
                                                                            '20210909:200606.088615:+0000',
                                                                            '20210909:200606.105041:+0000',
                                                                            '20210909:200606.121310:+0000',
                                                                            '20210909:200606.137214:+0000',
                                                                            '20210909:200606.154765:+0000',
                                                                            '20210909:200606.172698:+0000',
                                                                            '20210909:200606.188813:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ň˂ϜӋԙϠΉƜŶʃҝąˁЉɔϢΘďŘӌ˼¢ɐҍЛĨĂŝƆT',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7313407889642382096,
                                                                            6075793062851274610,
                                                                            8039720986692507598,
                                                                            2301556200847323823,
                                                                            -5440614204694148509,
                                                                            -579680222389021753,
                                                                            4734139424705133900,
                                                                            371192205218586681,
                                                                            1899980226835577963,
                                                                            1385561861282423717,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '±ŏнÜȠ[йʿɁΣй,ь˓ĔкѮÂGϬ',
                    'message': '\u038dƨӏѮϲҷÕ÷ΚкƿeǺ\x96ϒχFÑϩ³ȳϒƍҀδĉˉ9ϤБ',
                    'arguments': [
                            {
                                        'name': 'ϷƫɂćɔӪƭǪӇ_ЄБǸºǳϫӒʷʁŏҋǔΔпĂžȩǎęɣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9083773355498070962,
                                                    },
                                    },
                            {
                                        'name': 'Иʟŕ~ƟǵśԈƸʠӄѓњɩŏŧӒФĎ;вΝӼԚ\x8aOǦΨӢŮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȣѭѐͳ˰ΰͼǜРǉЎ?ԊВŖɀõ˞ʘýӯнǎs\u03a2ϖƮғîш',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200606.908866:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŪȖ)øʼ\u0382ѵԦȽѸʋЭĤǾlƽȇϤǂȊ φƟȖ\x9cпҝʼƵ҃',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -37602.4495331688,
                                                    },
                                    },
                            {
                                        'name': '˂ԜӞɩ\x93ŷχ˧ȶǞȰήʊǘȑéɨѻͶu˰фίӛ˃ɮēˢҞʳ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200607.050987:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҡžВÇǹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ķΗΝɲǗԭҍ҇əùȴӰÆvƴ;ԇАƐєҾͼƨҽӚɑΒʞʰģ',
                                                    },
                                    },
                            {
                                        'name': 'ҰǜɃϑˡΡɡѼƳѭУѽtºŉûƝͺƼ"A9ɱͳ\x9eɥƶŔјИ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7382925242833863390,
                                                                            3485052733709535494,
                                                                            -8580169669768820038,
                                                                            9069174984853553356,
                                                                            -7603060344440339168,
                                                                            -3381100523595302510,
                                                                            1093995814837708554,
                                                                            2662116668368552401,
                                                                            1136569949922105866,
                                                                            3891597912421732712,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͿοȷÉÃҽà+ϪÒ\u038dŦčνŸ0ΎAĄбƷɅӉ\x92Ħɵӱϯǘ˶',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200607.430665:+0000',
                                                                            '20210909:200607.448539:+0000',
                                                                            '20210909:200607.465315:+0000',
                                                                            '20210909:200607.481613:+0000',
                                                                            '20210909:200607.498271:+0000',
                                                                            '20210909:200607.515547:+0000',
                                                                            '20210909:200607.533187:+0000',
                                                                            '20210909:200607.551617:+0000',
                                                                            '20210909:200607.568629:+0000',
                                                                            '20210909:200607.585354:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԍҽɏ~ʬ\x98ʷǊƙȧƸηϱrGʆȡϔ˶γѝĥћŽӠɱȝϽľǅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            673377.7934178552,
                                                                            978346.5717715314,
                                                                            487139.3183236442,
                                                                            148725.2036706679,
                                                                            548215.2556437026,
                                                                            60366.74230747708,
                                                                            905368.5432392391,
                                                                            710087.8567748608,
                                                                            162391.65925238625,
                                                                            848997.8649099485,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʷӽӚȼҮλ\x9aǏΟİǻȰEΧԀнÁŏɘԫϻЖğϰȏϻT:ШѼ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7990208192897933396,
                                                                            -5301479092578426513,
                                                                            3489602098714876156,
                                                                            4545286709440706392,
                                                                            -4990470761139920850,
                                                                            5414120086651847015,
                                                                            -2089924656493914568,
                                                                            5252928865204309118,
                                                                            762787133083877232,
                                                                            5988014263495497624,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x8cԁϤ\x9bħӢL˹ɤʑȅËƺҧƴ\x99рк\x8aƳĢ\u0382ƸȇҨʪyƧˡǘ',
                    'message': 'Ż҅ɍƭĜғΘɯɦ¦ӿɋӉҋ˪ùɍˊZǁӽЮ˙ІѰĺ˺ϑ^ɜ',
                    'arguments': [
                            {
                                        'name': 'ӏǠȆäʀӷҠ]ԩ\x97џѿĔĭYȮρģʿƚ¨ǓɠӕǠÂР\x91ζП',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5826371609498769101,
                                                                            7806436465000808505,
                                                                            7425542224650785851,
                                                                            -7571094839520269629,
                                                                            964075289580606281,
                                                                            4763925276352746403,
                                                                            1688984764022951730,
                                                                            5726193115943177178,
                                                                            7611841427887756600,
                                                                            -7176016564305617846,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'mΆӭԝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8290075842496094717,
                                                                            2929976839259156956,
                                                                            5616283231071327325,
                                                                            6147610623322574667,
                                                                            558642933048011563,
                                                                            -959840649383339989,
                                                                            5944465574932357654,
                                                                            4561932460331756059,
                                                                            3214074927684068860,
                                                                            -2180551814099890940,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȡɞŇлΡ"bΌȑԌ£зƥѬƦrrˇѪǏΨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8015798924811019940,
                                                                            3298366336566526289,
                                                                            -6838478652982973858,
                                                                            -3284603546328900339,
                                                                            9214271738814558175,
                                                                            -7860212159279341588,
                                                                            -3067783836307216666,
                                                                            8543096698733617030,
                                                                            -1834019402998641510,
                                                                            -8220577902111871548,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȮљÊŇА/ͽʊâɏӡрӳƲǐ³˲ҡϐûÅӛ˸ÉʢǍ¦ʘҼЄ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1065056510764293410,
                                                                            563276324793891001,
                                                                            3952668594997659903,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӁȌŌǸЃƣ\u0381ϝǢ\x8aѪɬԅgŚԦ±ӪϢʬʑɧпɠԊwȦӰòÌ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200609.071968:+0000',
                                                                            '20210909:200609.087301:+0000',
                                                                            '20210909:200609.104044:+0000',
                                                                            '20210909:200609.119491:+0000',
                                                                            '20210909:200609.135204:+0000',
                                                                            '20210909:200609.150518:+0000',
                                                                            '20210909:200609.166102:+0000',
                                                                            '20210909:200609.183535:+0000',
                                                                            '20210909:200609.198912:+0000',
                                                                            '20210909:200609.214529:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'õ&ԗʁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΓζҨѓˌΠËĞʚİ´ȿƦ˚ˡωǨĕҎ¾ʢȲ˂āǸ¸ĠқˡŃ',
                                                    },
                                    },
                            {
                                        'name': '\u038dϾԖ¸ӴǡȽԈ«ФʅЫȄƴұoԣÃĴϓЧǠʪнǑѦȤΘǡŊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƤƱÛӴѡƯϝĩʓ,Ϊoɍʧ˶ɧӓзѻϕиδ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѺȧƱүÝïчόˀ·¨ĦʩǄɞƲʾ~ѵùMŲǀùʃʹǯ˛ʂū',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200609.663418:+0000',
                                                    },
                                    },
                            {
                                        'name': '˗ƈǍ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 253284.18278521713,
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

            'identifier': 'ȓȯ˳ƴѕ',

            'categories': [
                'os',
            ],

            'messages': [
                {
                    'catalog': 'уѮ',
                    'message': 'Ƅ',
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
            'name': 'ОȜžEԪʇπÐҜЊͶ˻¯§ΧћҸħŝÏƲɵф8ӥҁU҉ϖˌ',
            'error': {
                'identifier': 'ǴȿȍԕɞȴŏΜӊŻλɓς·ǟ\x82ѷМƪ\x9dҺѫ³aǳ˝ˋƟфɭ',
                'categories': [
                    'configuration',
                    'file',
                    'invalid-user-action',
                ],
                'source': 'ũȔӎӉwə4ԠǛ5Ɋǿ˞ϲϷҽчÔ\x8fŜɪȖȈɉӃρԍƛɣЋ',
                'messages': [
                    {
                            'catalog': 'ƚëúȢяпÏЛ҃Üħ-4ŕІɀҼƱǴŕǈǧΑҡĮ҅òԘҺЮ',
                            'message': 'Ԏ˔Ğʳɩң:Ǔ\x8aɅÙǯǚƄ±ȀĿªЏЃǓԙѵԠˠź2ιҰɊ',
                            'arguments': [
                                        {
                                                        'name': 'Ӹ҄ŴӨҨƚсǥ·',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "¦ΎǂӟЉģȜͿƇП}ƹԕъ²ά;ЖͶƜ'öÝчƇˌÐɉ.˛",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 843121.164654512,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ρ\x8cʏӢҹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȫԍ!TȘm¦ǮʩѫʵƋƱӏūʠĞǈ+ʦəϦñ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'β\x96ƼӳϽӟȞӛΣҋƼşʶЫԅӈԊƧǢĺGΉͿǜхhYƖŝü',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŇӌԊĩˉÿϊ˵×ğέɬƽ(ÕϙХĩԧű*Ƶ϶ϴ˟ˡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӄӣ(ϩϥ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 182505.4573532662,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8e҈vфǃҖ\xa0\x81Ϫӓ²Й\x9bʁСԀɘҞʵɱū;fЦʘLϺΟө-',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȬʗЈϭɋ˦ҢʟηƋгÛ˪ѴӰиũκcњϩˈҬȑƭѢǎɘɧϱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɖԭ\x9a\x99νƻˮ\x91ǼҀ+ӷƮȧӹ\x80ϯȆæĝҵǩɃ½ыÔԭǷӳǴ',
                            'message': 'ȁ҃ѹïʀmZ£ƸжŮĴÅâˬѢζΟӻϞ4ų҇ǩMɈŝɪhԨ',
                            'arguments': [
                                        {
                                                        'name': 'ǯԀήЬʻʌǢŞåȗʀχǯɁıǳώĂ˞ŞсŝҭȀ\x8dȘǩ+ӗӴ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǃɠˤƎƶʴġӻˁĵ˾ӸɣPĭϑϪɟÊѝ£fΏϐƢ@ʥʶĬƹ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳͺġƷ·ɼѶɝχɨ˵бЮϐъĜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200545.874961:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϳи\x98˽č˟ĨǋυÏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6602405965175233046,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʐ˫Н',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԭλǹȋ>ϾŪлÄќсÞ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȘжіãrҌO;ƍК6ʮȗƠʑ~Ӯƕѻăшƹ8ΏΙиŝǼɻϚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƂЏҧєǭΓϭ\x90ʡǋ*ѹαɥСҬɜ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǏȸøϔĢԧѨȁϺì˄ǑƌˌӭçӁƗãÅņЩϖǑʡʡǚ:Ǉ:',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ȼ©ͷʊǼҠ\x93ѳƿʤΏŦȖŢӕΝӹԨ\x9cϫŨȢѐ҉ϹCҜȥťɟ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÆѐҦžчͷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÏeҼӾƷƐFćŕΒЯȜVĿӳԤéʥѵ˳ÆДŃȠĶöθΗԉ.',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʼʻϊȷŬ',
                            'message': 'ʅӚ¿˦ƥʗӬāтʢƻѥɫԗĲÒҿЏň¹ӉТĪӵɆ!\x8cҕëÝ',
                            'arguments': [
                                        {
                                                        'name': 'wʺϒѸϼ҂ǑѬɮ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¢ЙԟεǪŉд˞ӽțJǯrӐй\x88ιԋέȝαźѓʸӐίǥЙѦƨ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ү¶ĠёɹъM`ҩɌˣ΄žбЇ-˨ʭŧ\xadƗ/]Яą˾³ӏѠI',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'џǒŲӫ¿ǅȔŢԂӔƪóΪȭŵ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'гʦУƼƆЂ˯ģѳѢϐȼ˧1ȑƊӠʚԝɃĪfĲƟ\u0382ɨϡìЃȟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'әȥϏɥɛèҡ#Ǘџԛˑ\x7fʗɷ҈ŝëƒɟ˭Ã˭ę˹ʡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÉӒʭ[ϳʜȤ¨ɄɁƽԩȋÿǣDϫ>ȰӸӺ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͶȸmŜʃѩņɚјğɘжȮɥDïǝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ';Э',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u0379Éǔɷ:ǅѫЉӠӼïԋȆ˻҅\u0379mӥΧ\x91ФηϽÝp˟ǱϩɏɁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐΦЬġԆйȞɔÃчБ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽϑðΉȪӈЪŬˎǡϏȑӀȥýćĔ\x8cҝ\x81ԠAƱ¬ӭǁǊӐÏҒ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ВʸμͳЪљуũęɷ˚С(ͶȒ˯ȃ{Ҷӊ×ԦӎǤɦѧҭŉϗ´',
                            'message': 'ɎʰҴ`xëǹǁĨȶѓȬԧōԍ\x88Đŭ˴Ӫ˰ŢǿȡͱЧѨˊËĂ',
                            'arguments': [
                                        {
                                                        'name': '\x9dԍĽ\x9fя\x89ԧӷϥ0҆ʧ5ϻµ\u0378ȞǨі»ʕӷЅU',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "Ɨέ\u038dʍ´'ʂ˯μģʇ\x8f˻-ν!гϫɭī˨ÐŊΫАȟӁϞѦ˪",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ИʆӶ\x90Ǻƍ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 72333.53849581428,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϓ\u038dʓʼĪЅ¹ŪƓԃдŝŌԌηāèяΘȃŬʷăԚђ1ҚɾЄ²',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΦϴßʍƤH\x8cϞƴ½њӨʧћ\x81ƁφʛәƎËĳВ\xadƈȍƂЮĦɟ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŧɘʌΡˑʊҖγѲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '-Ȧ\x92ҐΖԋˮƠΐ\x8dȒɊ½Βƣ΄ȜˣӀҳΥȈѷԞŁ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3086553881402472034,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʅӀϥН\x94Éšѯϸνĩ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƽҶ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'čȶԁǯȃǘɘВ°ԂņƼΕɨ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 344434.447205881,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҼӊσȁǶŃˏσˁ\u0379TŊH',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƻƾȱĭƤшwϫȩ\x8eOЛӣ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѾϷͰ$҈ùӵҚѴʵ¢Ǒǌ˒ѹƫѹϓÝØԎЃˆĶԁªƣÖūʞ',
                            'message': '9УΤɟЋҏ\x89Ǜƾ ÏЙcΟƲώѷγрȚ7qǎС=ЮΧąˈĥ',
                            'arguments': [
                                        {
                                                        'name': 'ń[ƂБ\x83Ğ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200548.070098:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'μƞfÈǭѨԧſü\x86ϨÆʿǿηӪсƲňĺɯЫӛĚ·ηξԮƝκ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÉʻƿϿǺͰγŝψїřŦȩͲʼȇƖǜźϲɹĉΗťЦɢǜáʀă',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'õƟʿØ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -55783.66865004016,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǍʦҝĎԩҾҰӒ!ю\x84ϯ\x86\u0378Úӷ´ʉѮԒģȹ\x88ěyÜӹÞǪì',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 479602.75678446307,
                                                                        },
                                                    },
                                        {
                                                        'name': 'őѿ҇ƂµўѦľѭԋϫҺ˯ϮԘ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯĿǀВԪΊѻϋЖĥǖǅĴȸүӳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '·ҵ҃ͰʇОϤǰЁɆ\x95ІâÞɈNš\x96³țǔǕ×}Ι=ԥȮʜƫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8cŬҵy˝ßʻзÒɐƂҬөȃϳʨ/ÚnΞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ćǐΤŌɄǶǅϧӞ\x8eɈ^ǽХĉĵ\x9cBυ¢Ӗ\x9bѭӈѢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҽѽҹЀЊɋǴƖϰȤѾʁȔӕɰÇԣʺɂØŠŚǿѵϱХâƠÊ.',
                            'message': 'ЄˈɶƼʍӯʐ¶Çĝӆ˙_ŽϏȀˣѯҀ҅¸ҼČӓŀӴȝ\x8aɦ\x9a',
                            'arguments': [
                                        {
                                                        'name': 'ưΓсɲȳ\x87ŶǠԌÕǎѝơ\x8eҔѕО¤\x9aρʊϸƛʹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'λ«ĭəɫǷȧĲӖʠʆŃáȦɼ҇ɒʨǭӈғЙ͵ЪӀшąАґb',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȳѶɬШĿľюôȖɘзёіjčeȎʦИқѨˀť\x82˲ѐȦѮçǪ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ūΘĪˬ!ʚхƊΊRͿƎŠҽ\x9dLѲɆƄӂ±ÐΤϨȤNʇXуɑ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '[а˻ȫƸϒ˻ͶѽƞšĐ\x8aϬʜ\x80åԡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 232970.62629623484,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϫǆʓѺˌѮҺéюӐǳУɻÜƟÿкUȼġҸĤƙˠɫ9ȲʱӨǛ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '÷щǍΕЪҽĻӊԑWɌˑӘρѹ3@ҖĹθ(QĈΫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЍoʳҋԈȟĠjÍρˡйϝHҴҡ¶ԪŶ.ĄŹÃηɫԙ;ҶÓö',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ːĉǚĢſßȄ¦ёrӲʸʐҗ¥',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'E8˳ôѽӊ[ʂύüŅһχ҄ƭʂʱȖВǁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ß%ŬéûӓѵǎѰΐŽΙӨ҇zɍыцªːŦ\xadҀԦΓϢģİʲª',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6606898319726483769,
                                                                        },
                                                    },
                                        {
                                                        'name': 'dӌиϲǦӜΣξȏӸϤ+\x83ýČӎшͽϕŗ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĸкɷ9ɄпӢͿеΎӶȌ6°ċҪȍʏ\x84п΄ʲƑǞўǀϴ¡Қǔ',
                            'message': 'ʚEÕͱҸǝόɁĐʊǌCЂКδκƗʜǛϜҏːȖő\x97ΓƊʳӰƀ',
                            'arguments': [
                                        {
                                                        'name': 'Яү˅ǰ@ȓσšԗβiƉ\\ѣpҤȵƲiˁʞʴөȹԤƜ¸ӿʱƋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': ':ˤАĩӍêȷøϘįƺϰӹĪǺЊԎҘ˱ĂЅ¨ɇίcʒ)ðѤθ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʂŞvҠпʬʧԧΤʸľęɊƝиϫɦˠԀěͺĥɊcӯӧ\u0381ӎÑ4',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĕªюӘɎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3008853713526954740,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϿҔϰĪ>ˈ·ĵΦύřӉ\x86θҵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫуʮȯϊҬԎѤP',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҷӖҪɺЊПʂϐǲĜԄӖɡǃʌӇ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƝűȘèҐɍӡ*ҹόРƂ\x93ҳӝϗͺ͵ǣҿΛϭϒ\x95ŦӲŐѦɎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'MѿȋyӼϒƽǷȟʸɾӑłҀӾǻԫƇʽӣԞԘʪʠĚʷӗγѱƀ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ėϷΤȣъ҅ɻƓ+Н΄˭όԦʻΜˤïφɻэHΩшǲìŔӭm\x82',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϔЫВŕѳҙŠȟŨӱĮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1435502395813824683,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЁrɠԬʥӷҿԑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '÷ϘѨҥ',
                            'message': 'ȐɘґΛ\x83ӻłʢҗԊȽɘ½ĔğFɇ!\x8eѬөӑŶÔƦӀӞĭȱΣ',
                            'arguments': [
                                        {
                                                        'name': '\x87ʥʯȡľϬϯˈӊЩɫѵЇȽѷοё',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǞҒȏϯ˸Жв.ǜϫǆѴř',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ơҋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 52959313601893105,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȱɌѪӌưҶ˺\u0379řŔІņéˤяɎǰǅвʦù',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʵӇʑЮɵ\x88ϕԁӕӛ\u0382\x88ϲГȟʟ˯ˌêűвѷνӘœ¾ƣčȀɑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǅīϚәʙʅĮʥԘҕrνǓƴ\u03a2ҤȵӼ³ȿӌʨċϺϴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӫʴ®Ə\x8bϮΩрЄъCӒΔмŵԖΛκ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200550.944147:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'КԐφčŖŪɝĤȏǲʯӒċӵĜ1уʳĹàГΧЁɛӰƎę˂Χʳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6252124741888526792,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŇÜĊҮѺφϪVʑԓϤīʆӇ҈īБȘŝѾцǋęӬϴύǁϾϰѴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'åѼ\x84ѽѯήԌϊÒĕϏɎȫlɋβʦҿԛʲʆ\x98ŧǊϱˑԤʿǋъ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÖĸeȾԆ%ҰͶʵҿõȘԛ½ȲΞǧʸцȹã\x96ГėʸŃ˼Ӽƹí',
                            'message': '¶ˎçőmҝΏϏϋƼƵß҉ϛ˧ҪɈԊФ˾.ұϻ˺˒ƥ϶ģôӂ',
                            'arguments': [
                                        {
                                                        'name': 'ϨιʺƼǮ҆)âѰЄ[ŷkӋИɓďȆƚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ò\x84Ƕѽʚϟԝ˭ńʙ"\x88ɖϷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 904066.0501475575,
                                                                        },
                                                    },
                                        {
                                                        'name': '˩хќҝЫșļθ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200551.520203:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʆΊѷƟ˰Ӟ˼ĝAĺ\x81',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɎĝαȗfӻǳҗҖҪςҍŏǏϺŶԚǿѺԟкӽ\x9fԝaөÇЈӘӸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԭŘϕ\x9eԘǸ϶',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЗƼȃ\x91ϱˣҙйʈǓ϶с¦ѺӃüϰĽѩȜ\xad҉ͶԀɸ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'цѬǖӢ"',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˢϒÐOϷѓЛĻҦʧҌӋҘņ\u0380ëѿ͵ɦȾϛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӊԇlü´˨ǡąʂƕǉɦȉþţȬӕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8747558442830826187,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȱѫ©ʷǋŞζȤ0hɍσӦčϖȋĔǋǧĻԀȌӨĵԖɑľźuş',
                            'message': 'ϴӓԇǙĶƾǽŎШѕ÷ŇȘǌ˂ɡĤvѷΑƐʔ\x9cɡЃʻFЖΤˬ',
                            'arguments': [
                                        {
                                                        'name': 'dʸʃVѝҲɤ¥υƪ+ԚēŬʉȹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǇһѹƆéɩɮђ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 286244.2762928066,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʥҺ\u0382ʚβ²Ќǫкθϳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʝOwìчFϮӎЕʱʁĆΑёɏӟǏĪͼԂӷsWЊˢƁСѼØϙ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'нΘҮƗЊːɀȣϗÈҽРBѠǩ~ϫӂĚˌϱ˝Ҥ˷ɛMɻДϿȪ',
                                                                        },
                                                    },
                                        {
                                                        'name': '¤ŐƫɏѻɖǲѽԣƁΠҘщùӀȐб\x8dŪϨіÖ^ν}ɴȺ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˃',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 841819.418170908,
                                                                        },
                                                    },
                                        {
                                                        'name': 'οӍȪȅкƆԠҼϷ\x8aƍÓs҄\u0382ӢÍмëƩUʱ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƣС1Ө˦ҘǶΞοʥʞҼ;®ΫѝàԛčχȞΚӡʜԘY¯ǌӳΛ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '*φӍÐҘӵɕҖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Çɮȏ6҇¢ұϣɕŧРҒ˄=ȈҨǾʡȿľϜІʑŅʔϩĘǉɷ˞',
                                                        'value': {
                                                                            '^': 'string_list',
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

            'name': 'Ūϖј',

            'error': {
                'identifier': "Ű'ûʭ)",
                'categories': [
                    'internal',
                ],
                'messages': [
                    {
                            'catalog': '<\x90',
                            'message': '§',
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
            'name': 'ƚϏGпŇĿĞǈЏǪόұɡ˄тԮǰÙӶ\x9dĄǬƟʣџɊĒ`Ǧú',
            'version': [
                -2446993802191787228,
                -3012303103476558331,
                -769361537732691974,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'W\x89и',

            'version': [
                -2896195950507846756,
                -1358904272868990925,
                -1252585654175400073,
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
            'event_id': '\x9cҬŒȇҌϴͽʏdѷxĿňŃзĳΘηбҢèƠнˋȉǁԚˉƼɗ',
            'target_id': 'ӹʿуʘňϓɷλłДÔEΓǩĻеΈÞθđƢѪƮώʈŕѦ¶˼ӗ',
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
                    'event_id': 'ƠФоȌċɘτͶԌ\x7fˈǆΞˈ˓ȞȯˈӀԨİȋˣӑԔ҉ѽд˪ȅ',
                    'target_id': '˺҆Ң˧чīƚΣǏʗʰLʅʷрЊϷʞѧZԖ˪ʹԮȯʃƶЫȈĤ',
                },
                {
                    'event_id': 'Ɏψʕˎ΅ѰˠĝѶҦɠȈľĒ!ōFs˕҅ӣб<eóyRҕʸП',
                    'target_id': 'ȏˏb+іԅ˭˼ʎЗԘľӵӮr˳҂ѐ×ȇßӚȀЂΘȤǕŋФʛ',
                },
                {
                    'event_id': 'ϑΌƐˁ\x82\u03a2þ',
                    'target_id': 'ћΏĐҾƸÅ$ƴҝˉЀɝèЊмƸɒȬȆЩŞ4ǀϛÑˠΘ\x99Ӟα',
                },
                {
                    'event_id': 'ӓҳӾč¯ъɈŠͶ\u0380\u0381ͶSǪӧȽΒ-éǘKÙҚѻѶҼ}϶ҶЫ',
                    'target_id': 'ԊϙJµ(!Ƌʰ5ʞɂʕ@ÚŚѭǽǓϘɉѵʴpľȘЇё\x85Ē/',
                },
                {
                    'event_id': 'ѷκ˰ȻQʝҊτӴҖĈŞԩƭт\x9fǤŔǰˤҠȼƲ˪ƕӤ\x87ǀϢŧ',
                    'target_id': 'ӰİʢѬȿʿ¯Ǚƺʸ`ǺĒRaʏ®ϐөŚʀұ·ԤƋɮ²ԭF˕',
                },
                {
                    'event_id': 'ԘÅΤǕɡĿɖQmèƁϘϠǔ͵ȐƖԂɧϧ\u038b\x98Ѯϩ¾ǒѾѱӞԔ',
                    'target_id': '#?Ôƒȶȋ\x9bpҜǙTűыӶʅƣȊӽÍІǺaʟΑӉpǄӾӻѴ',
                },
                {
                    'event_id': 'ӍʰÞÊÏΎҸРãϴæǭÙɬԡѶҠƚɫ͵Űó\x8f§ȉвǾˍäʹ',
                    'target_id': 'ŪԫÎђѺɦϹϴųɆМЇәƊŵʤɺʀəӲѡ<YǦӣȫū\x8dΠѠ',
                },
                {
                    'event_id': '˝ԞΑĐӀΏƱe\u03a2ʅ˘˘үщДӓԧϤƦȆǑɤӚƛ˳љʂ;ŹҺ',
                    'target_id': 'ƙԡϥӒƴ',
                },
                {
                    'event_id': '˪ɳµʠʚ»ʶ¦Ũ҈ĪӱЪ˼°ȎȸΊӝϱǰȦԋpƝǛλǄƬʞ',
                    'target_id': 'ЎӸ¢ϥφ_ưƬȃɩЊΪ{з1ƌʯоˏѓĘƩŨ4δǗϴŢҩѠ',
                },
                {
                    'event_id': 'ɆɆæьĐʪßȞžϱήƗǝ:ĠɤɵƚԪ\u0378ӚͽȗŏTøʳ¯ÚƂ',
                    'target_id': 'ř\x8f҂ФӆϰíǘSNϐŬΐҕȴ<ԥʯ\u038dÆǇѾŨʠ¡Ϳ>ҧѭà',
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
                    'event_id': 'ЍӾǜ˞юʵϦѐŶĩǮǾ˪ѭԝĚԞϔΖˇ§ß~ØєϑѧʆʮЫ',
                    'target_id': 'Ӂ˙ɢԕ˩ԠҋɲʕǥΞЏȿăʓаԬȥĢ˭Ďǫ·ӕѮɦĂԪŵʒ',
                },
                {
                    'event_id': 'ïϭĪºôѺÿЉҺϑTԛÒȧŪ@Ɯ\x96ǔ+ʠĐħ Ԁͷ<NƆȷ',
                    'target_id': 'Ӗ%ȥǑʃŽИƾҳӸʟǛЖͳϠșÒͳӜЩӔӸ˂đ¼ǛȎЛϜ$',
                },
                {
                    'event_id': '6ѵĔĆƄȈҭŢɧ\x91ɆϴPĠŶįСȇɛғӃϙ˒eʎΠѓҥͺʘ',
                    'target_id': 'ÌԞҩǾЃ¨Щŭ˜ǞѺѤ',
                },
                {
                    'event_id': 'ƊŌø\x96ʾǼͳųӛЩӭӧǚлćЖӀϥҶρèõͽȝϛԚIĎŭɄ',
                    'target_id': '\u0383Ҕ϶ЃɎџĬЛʅϜŹԉǅʞɄ\x8bЅСßêћȃϙʚХȋʰÈ\xa0ƻ',
                },
                {
                    'event_id': 'ёŒ¤ƧxŢÆɫǣ\x85ȳǔåǧɃìʭӑҘԀ¤ӪϝҢѸÇžȚаΦ',
                    'target_id': 'ћÎϧ¤ҸцŗˠƫǹЕŢӓɀþ\x99Ǵ\x99ɞѪԋ˘ìWϷʔŐȳǦҝ',
                },
                {
                    'event_id': 'ĄҀǸϏʓѰ¿\x8eĐʠеɗʢθɶ\u0381Σ9ĿӃǛӹĽʢѡ΄ĨŹă*',
                    'target_id': 'ϳ˦ˀɏ\x87ţёԐёʤĵ^ζƄ^εѓӈңҺѓC',
                },
                {
                    'event_id': 'ѩīСЅ˶ȼêѕʴśϏʥ\x8bĕԈƏʱԅƠιϹўǆδѭŜȖƃƮэ',
                    'target_id': 'əɠŧҢЯȦĢģҷƧӲ˱ʺɠΎ˩ĵңдэàƪ˚ƊβćҮψƮˌ',
                },
                {
                    'event_id': 'ŦPӾʃȖΰ¥ʯцХҪƁmŵҞͺюșάʉϓƎΨƍҮ˳Ԇĭȵб',
                    'target_id': 'ǣΜŁθƇƭӨģҌZҔäƛΪʖĨ¤ȭɿϕėӕ˲ДǌӉſ·˫S',
                },
                {
                    'event_id': 'ɕ˧,ϭ˱ŗǉɀШƄĲǉԮϰϮÃД\\ȳҺ˪?xÚԝʾǱʺяƾ',
                    'target_id': 'вɢ2ƾђʋĂϝƣѪùȾИЉ¹Ɗ_șĦż\x8aĬҨȻϚΤǋŅΔ§',
                },
                {
                    'event_id': 'ȈɪϒģϠƊӹȠԮԄƶɷτПͺ˓ɋϺɽҊбӻʌɈːÁ¡ԑѸΪ',
                    'target_id': 'ďԕĕЏ˞έǺǜǆҚщȫ҅ǛùáξӠƤġˬΊ4тfҏѡʃȖĂ',
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


class ExtensionInfoTest(unittest.TestCase):
    """
    Tests for ExtensionInfo
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_INFO_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ExtensionInfo.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_INFO_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ExtensionInfo.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_INFO_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='about', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='authors', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='licenses', name='ExtensionInfo'),
            ),

        ),
    ),

]


EXTENSION_INFO_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ĚČɾďȖŸҟvЩˆқĉ\x9aqÛӡҽȷυǣҁɚӿȠη˚ŹƔ\u0382Ԧ',
            'version': [
                -1683579616380890853,
                -322673059159586923,
                -5820756336900825723,
            ],
            'about': 'ї',
            'description': 'Ťɂƪ\x7fëοɑĿΧЁLŸΙƔŬԞĐ´ņŝӑǵӸҡɿ0ƗˢИĿ',
            'authors': [
                'JȜʏ\\ӫǣАÜªʝѪƃǊӁ{,ȭѲÖAȺWMÇÛAʂ\x7f\x83љ',
                'ΌĵHůӘȽŇԨϐðӨҀғʦϜσԭɀ=ȽǏǹӲĩǢłНКˊн',
                'ΔĽԦӢҘǑ\xa0\xadzā\x8eɻȸԤďыʩϙΆʭӏξĕϧɗƜԦγʑƲ',
                'ɨ\x89ҽ˭}ϾƊķӇƳϑ\u0379ę˸ʣɻÎӈƞ҃ʚԝĦǝ¯ЎѧҾƷʤ',
                'ţƸ˺ԭˌҾ`˚œԭÔЋʣʎșЀˁѷ\x9fσйͻӨŲʧ\x91ſ\\ǓŠ',
                '˩ĝҪÚƬʚΟİǿεɆˌϼѧǪ1\u0378ǳОenѧϾ\x87ˊӮȟиǳù',
                'ŭ7òŔӬĩԌĆǦĊҟǎήǕɏqњѵѮˮƘO҄S΅8ІАө\x9e',
                'MɍƢӈ³ӌΘҙԒådҕԂʺ(ӘҫÓtʷƣӲˠљƢWǍσƎȋ',
                'YéķǅҨͳɘÐČ|\x92ѫźȺ\x94ҝŠƞԁўjQҠãą}ŨĐ˾ŧ',
                '\xa0ʑȽËʱʱĨÿFʚȀӚЋϮǏϿä\x88΄ãж\x9bϬÎňȓɚƕϔƂ',
            ],
            'licenses': [
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ԁԫ\x92',

            'version': [
                -8674183469036146966,
                -8632057765927585405,
                -4693162582766562109,
            ],

            'about': '',

            'description': '',

            'authors': [
            ],

            'licenses': [
            ],

        },
    ),
]


class ActiveExtensionsStateTest(unittest.TestCase):
    """
    Tests for ActiveExtensionsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_EXTENSIONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ActiveExtensionsState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_EXTENSIONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ActiveExtensionsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_EXTENSIONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='extensions', name='ActiveExtensionsState'),
            ),

        ),
    ),

]


ACTIVE_EXTENSIONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'extensions': [
                {
                    'name': 'ӃγϜӮǩȘȦ^ʪˣ÷ҒîѰƄǞϮϟѽġųНŐԉˆÖԛŏWƂ',
                    'version': [
                            -6604344235236306951,
                            -1413842954116784023,
                            -5334089870799407814,
                        ],
                    'about': '·ЙɄȏʣѠÔӺϹhˏɡ˓ӝȁɊǔϯэӍ¡ɲ˷ЛӾÑÓӡƝі',
                    'description': '϶ǮҮСuʑϝӜӁϻʍȽȮÛЬєȯԗŹʃȅϕһһ˾ñƶƲюŬ',
                    'authors': [
                            'ɾáēŷ^ȎϲvÅӡʄ¥ĒɚƝƣwŽĺͷ2',
                            'ɚrʘIиӴıϐϫř\x9d˚\x87ѱʖұƵӅӣ2ȿӑZ·ьíƙʒū˽',
                            'RłR=ϋџЊ?ҭηӗЉɃωԋƃɉϕɹǩĂÝԚˉȐϵ˵ȡѾϦ',
                            'ϛćĭÆʣН,нȾɯюЗСǡɍěʘԔͼħâѕδѣпπЇѭ˖ɸ',
                            "ӐĠѱѶǾ¸ьӷŅñϋ¡ЍԄˎɐзͱȚϛʸ'ɦ0чŧȔͽӬ˫",
                            'ʩѴҏ§nĿϽɞʝ˹ɖƝǃЇưɥʀǋƺэǸ\x85ǜ`ø\x99˦ӞČƧ',
                            'ƣԤ\x96ΚʔҎԈǔ2ʯѻԚΰͲǄʧƲ\x9dѶmĽǁΚШĹЃΞπԤ\u0383',
                            'ӆҦМoҘҁӀˇŲӰAѠϢюěˀɔƢǡɚσǵɊѤ˲ɿϣïƣʈ',
                            'ïУɠȵʐԀЌŭˠġɃχȝҵȪ҆Ѥȧ\xadǭƮÖ\x88˘˞àĐϹȁŜ',
                            'Ͱϑaӝϧ\xa0Ωɗ_îВƢɒwưκYÍ8*҄ҺȞ\x8cǓэԑЅо϶',
                        ],
                    'licenses': [
                            'КģГºšΫ΅ӏѦԤΤʹƏĀͽĥŢʲ\u038d¾\x91ʠӢѵʋΓƑϑȗϠ',
                            'ЖюPƘрÛ',
                            'ʾʠЍʳˢώʡϕόǪɍȠӕÀͻǘƫǎ˪ʦˬѻŲ\u0378ɎǬíƢǧ¨',
                            "Ȱk'ԕԊį·ƲŤӻЃѦ˻ʁǿòҢùӉțʙæǭʭŧ\x85Ӵɨɒӈ",
                            'Ͼč҅dҟzͼȱ\x80ӖʿçϥĿ˔ßgϲȢ϶ѤîыÈƤΉЙzЪœ',
                            'ƧнϿĐƸóӻшŒpɲ¼ǬƭѠҸĚǂȠΘǢс·ώбԉӖțɧш',
                            'ɡӦgʚʳУúѻɯǡiҏȓRʜ²ÄȇԌȯȝцӲǼ@ήĠɑͱ¡',
                        ],
                },
                {
                    'name': 'Ĝœξ1Ǧ3я˼ҺύȾŇҡƁłЯΩƊЙŚżGćΓмЊ¿КΐȰ',
                    'version': [
                            -1630900502151679068,
                            -847698045778431869,
                            -38862085513464819,
                        ],
                    'about': 'Ȧˑʕ\x85Ѷ ӒtǺȥƑĩËãȭɒȉԈŝԠδҍϤɟȨБV˄ƎǏ',
                    'description': '\x86ǊФ?ͶˮѸϨĀә\xa0ԁ˰ƚ\x9c\x80ļͳőOſfѦɱɣƾШȓΜň',
                    'authors': [
                            'ˣǁԓʸĖӍĒǩόŵԘ°\x9aӌǨѰԠөǖԫǦ˪ıkƘдӬ\x82;ȗ',
                            'ҢɈ\\ŬћӖ҈ʓϗPИ[κɞûǲƋɔϷñθԤиFқǕȘ1ǌҽ',
                            'яǊԡǠ\xa0ŇͶҤɺTʩщʞɱņӪʶȻԫˢˠԚԤʄӪǡλƯϪ\x9b',
                            'ɛ˧\x7fԃ¹ӷϝǚǋʓʁƻɰˌʋķĆЎϕ\x9dҳԢвѲŚѳĺɘˎε',
                            'ˍϒƷċĴļȁʎÚϢ£¿ùΝʜʽtʚʍɶȤ,ʋщįɬȣǌǶȝ',
                            'М#ʂĒϳǂÎƑ¹ͳʧ<Ҳ®ɦġԇԇǖч#ӍɖӮŖωҜȣЙm',
                            'ɥ2ϽȽƽǞȩĶԆÄϹ˪ϜƄǽϊĽɥ½åūɉŇҡƧЫџʀŻ¬',
                            'q˙¿ά\xa0Kk˞͵Ȗ˗ԌЫĭɳǏӰíҁŞĐ\x8b\x9bˀͻ',
                            "ѐѓϾ˜'ѣӮΙΏμ@ЧȁƑΝĬК$ЌϑͺΌϺʨĺȑų\xadŢѡ",
                            'ŭ5kʟˈ\\3˔ʛВʈŵӗЬҨµȧþǩȭҚюʵӥč˽ȂˁÇǠ',
                        ],
                    'licenses': [
                            'h\x8fǸѐŐĖӻ˖ц˂;˼ɞӞƾµǑ>ǫЇϊўӷɟӊԆµ˙ʈѝ',
                        ],
                },
                {
                    'name': 'ȟ\x8fƇ,éVШd)\x84νԃӔǥɓԢІȀԨғϸȌӆÇɆӞƝòɢґ',
                    'version': [
                            -3850262524436958210,
                            -3136634687036359224,
                            -8031094117253945728,
                        ],
                    'about': 'ï',
                    'description': '½ˠF\x9bљͽeӻǴ˩ΣôŖӽх®Ϲ҃ŬФϑ˹ǒʶÕ\x8d?ґȇт',
                    'authors': [
                            '҄ԪΦƻҮ\u038dÒ£_Ŝĝ\x89ĮԋоʡИʌȊȽÉ¨ɥԜԆÍƿ˟}й',
                            'ЀʻϮǛЫèûӀɟΪťǌ¼˛ôȧ˱ŽƀñUεͽͶɅ}ʌˆǾˌ',
                            'ЁɮҎЉȼľԦŌƝáξɟƢʊΕ\x8cΘǿȢrŶȘ±ʲӅζĢZaτ',
                            'ˊŵǡǜαчøӔƶԟƤѺίѮǽȢ\u0378ъѷΠǉÐ"ӤȰθƢΩůх',
                            'ūǣƼėŁҹ\x8bȉǧ\x89˼ǴϪƼǅŚƔЎԆǹԥΔ»$ѺӖЪȨƤʉ',
                            'ъФþǘʔŋâћ\u0379ɕșěԊОǰŊͶюíѼЪζηɁõҒƷĞȸȄ',
                            'Ҿɏ\u038bʋūιŉ҂˩ʟˡԁÐђǅņʿŤǚèʄKȚ\x8cČҸƈǗÌĦ',
                            'ǼȧŢɗʢɰŜμƌԄĬȄϳ6ҸɅ˓ʣƵɈӰƀłúĐÐѲɧǹ\x9a',
                            'ԃ1NlԘɋԏǦƇƅтѬʍϷμōĬȇЇѲȉӎĠ>[˷nѱȚϛ',
                            'ƛȻΰЊȀÖŁбԊżIȿʂԉӬøƺʶ\x81μRй(ϙͶʶ²˙˞Ʒ',
                        ],
                    'licenses': [
                            'Ѧ\u0381Ђˁċ´ĐǙàǇȀř\x9bŜ˞ǭÞȰ¤Ь<ąЃÑʮŉ;Ԅʀ҄',
                        ],
                },
                {
                    'name': 'мŘƛnēDőϩБӸś˺ɚǛЀѣŢдķѻӏ҂ƗǪдҥ\x9dȜά«',
                    'version': [
                            -5590887825072106317,
                            -2830834537039553915,
                            -1533369554971349845,
                        ],
                    'about': '\u038dͼΧğљ²ɘӣʲʂʶĕϚϦϵŠԢϴЃӡ\x9cҽȥέшLѶâȦȢ',
                    'description': 'ΖȀϾϛøĈɇϣΏ˙ǙѱчКµtʀHϫρrĻĖĬϕҭǙȘǝ˟',
                    'authors': [
                            'ŖƂÊȾŲȬºҙBԡǕàҷƽӶҨҺ϶ǟȰΕӯʨȰ¦ȳΣƠ˕΅',
                            'ĥӍϪʲ˟ƸԦѴȎˉɟŝɥϷγ\x8eɷ\u0379ǡ,˥ɡƸ Ԅ3ԜϤӍ¶',
                            'çӒľѼ˞Ģ1ʸӧ¾êԁǛϤͿźΊϧґ˚ԉыŒ˦ʴҰʻњɻν',
                            'Ý\u0381ΔʤϏ\xa0b´ъϷόƇЧѥǽӃƐ`\x88έӏǮ)θѕɆtΨʆȡ',
                            'ƈʘ7ҵäť\x9aͳЯĘE~4¯¹ϕΣpÕ˄іϲ0Ԣ³ą_βѤȗ',
                            'ŠΠ\u0381ȇʵȃηΤɈǫřˎȲђǕůȅķCƳǤƯѵŢƛˣʇǇ"ǀ',
                            'ƿOɟЂв8\x80ѡĢЀԬɎƔƦѱӞ¿ϫ҉ӵʳˌ÷ÄªͲ ʧҧć',
                            'ȹȉʸǕĻӦˉƭįʗ\x8bʌ\x8a\xadń¨ŻƔMǃɺљз',
                            'ƀƊҠǯö¤ÑǨ³ĄЋ˹ǛʏƑҼ<ȴӥфȤͲȼTИϔҝƂʹӸ',
                            'ϖ˟ɞЂʵǮÓЉΖҠʆğǣÅҧJϊԞʕ·ŬӤηŻԠPƾį*˻',
                        ],
                    'licenses': [
                            'ΡӑӍʫкȲĵѴҞƜĨʘѻ;¼ϑѵСîѲƮçƾ˟ɫˈ˲șўɴ',
                            'HѿíИӚЅɲЧʳѰαӏчξȗ\x96ÄęԢŘсtΉЎƖώŻπʲʧ',
                            '҅ЋøÓǼϒ˃µEɚŋĵƃҾ϶ԏϫёŵѩ˨ѭ±ѕ\u0380Ȗ\x83Гɪӧ',
                        ],
                },
                {
                    'name': 'UȎǵԈͼ\x8fɇǒìӘÕ\x86ǶoӼ×òĞҏĪͱϑ',
                    'version': [
                            -340979097002016487,
                            -5222292051163442481,
                            -4673303423965647835,
                        ],
                    'about': 'ˈхЍсУƠҒүŞ',
                    'description': 'ϙʼǒɥ\x81ȟUºҪмăȒȯɑӏŹӵģҖʚðS\x82\x97ŔʫΎʙłҟ',
                    'authors': [
                            'ɀϒĹа²\u038dҏĨĆΒҁθԑџɄӧțˬȴѭċìƹѧŨŜћіяќ',
                            'nκ>ĽѦʵ\\ĬlöҗʊȯƴӦѳ¹ǁ҃áӻԋʜƑ*ÎǛҒɠĵ',
                            'Сʥ˄ϢƱùҒҗԥԄдƀÀ¯Õ´ŅӋƒλ5ӮȯȑʭҠѡʄһ9',
                            '\u0380ОΎŴi&ԃǞƗØńôƺǩь\x85зҍҦөҋɞ7ʹYƬӻѴ҈ɫ',
                            '¼cŔё˨ЄöqȾđԍʃӳυɺГƔxbΫ®;Ԯ',
                            '˰ʨϬɞƪҤƾüĎǲӍɣȵЎ˯\\Čѯ˯Ĭòľа ϸѕʍĶͷƥ',
                            '\x88ʡÅ½ɣƾΌ[8ƅӨӲ\x9dÜЙ-ΎŰoŨÛѦΗŕϥЙӖӸɡȓ',
                            '϶ΕƬ˞ɮPïũӼǝ\x99ȚɜɇżϽÚϩƍ³ԮҗǬʈҳɲǃ˫ЬΑ',
                            'ǗǻɠͱȐ˓ƀʗʒЦŔӱѧѻʈ˯ǁǔˀʱIΤ˜ÅСЙӸǧӤӕ',
                            'ƷĤԊҹӅ.˒ұƱW\u0382êƹ΄ǾΣЫ.ԚδдsÁɎϟǒЅɠŊ+',
                        ],
                    'licenses': [
                            'ϋӾΜɱЬåÂd˧ǙοӄͶҌҍǛӥ©\x9c¤\u0381љˮ¢šԄţɡ¯Ƀ',
                            'å˸ϳĢԆɉˑɽʽπήP>ĳΝȱ,˼ǼξϕƜЩȗӝǯиʩɚϝ',
                            'оȋΘΎʄʍɏжƇʒмҨȷǬ˽ѢʙҁHʥÕӷԎ\x9cǫьсȺЉϢ',
                            'ϰŀ³оλƀ\x8aϖЇÒҿӥöȯƱпҙԍ/ȹîԟӳҝҬякˍηİ',
                            'ȸƴϷÄ˝FВǓѺ·ĬǋҁǣΚCǱʅ_ș~ϭψЩåĀŉʜƏǸ',
                            'ȱ˻Ѹč҄ĎȢīǘƝǵťǂˍȌҍĤЫşūкĴҼŵˬĈʶIǡҼ',
                            'ɳ2\xa0ƤѸйʱӖ\u0379ǧ˟Ô[СӛɲӴ\x82ȢɼďǀƿȦÅћ˞$ƗH',
                            'ЂɦõΖʽ»ҧŭ\u038dϖɳȫŕ@˓ѸҝäѓɰϟНɖ5˦γƉ˲Ŧɟ',
                        ],
                },
                {
                    'name': '\x89ȪýɧԬҤČ¥ÆɘʾLǺϧ<ҤИĘɬȸˌôȉüˍԃǁϮӼқ',
                    'version': [
                            -8756401455314395577,
                            -2397150842479639197,
                            -3999971479727520472,
                        ],
                    'about': 'һԆǊцjзɹЦӮҝƙ˜ŷѪ˻κԃħоä˵ћұΉѩɔw¹§Ƕ',
                    'description': 'ѵġаЈñÐВӬʡ1ǸˑŹ҅ΐѼԪћћʷϕěļɥJ®ˤȾ\x99ҡ',
                    'authors': [
                            ')đQϥɰμѺ\x8dȃà¤ĵԖζňʅµ\x91ƐɻѫʲӵhǈƔԐ\u0380Ő\x84',
                            'Ǒ±ԦАҦ9Ƭˡ9бɠԦÓͼĳǒӀÿÄӽˢѴÿԡœ˹ӣ˾\\Ǝ',
                            'ϡĩ/ÛԃlԎtЛ\x91ÝȕԔȵӵƀǢƥҴжɓƘǿ҆\x9crΜԩӴӵ',
                            'пÌәŊгǫƸŕӹӤΗ',
                            'ӒЫҸҽǀşŪčȌΐЫѕϱĲ\x90ӭҫ®ƾÙѶѡ5ǀ´ҙҐǰķȗ',
                            'ԇſéφҿНǌЋŖѮɰΐҨҩ˛ƺɓȀȾbĚ¸Ʒy˥ȘǏ˲жȋ',
                            ';ӉöǾĨȂ©ȈӨȈ΅ҜȑϵԒÀȾþįɀȋ҉ˎ҆˳ʧǘę˓ø',
                            '\x8eʸεМґ˚=ӊėȴBƌΥћуΚЦҔεȁц³ϻѪǆ#ϹЉŜĩ',
                            'Ȳ|Ȼʕ',
                            'Ƴǐ\x8bӶӠȄϡљɯҩćɩφΑŋҶhgͷqÕìжbϻȲλƒԧˑ',
                        ],
                    'licenses': [
                            'йǍɝҼӰȝƊѲ§ϰÞþӺƄвʰƜȸʙωƨѰӱϔƀ·ϔОǋӊ',
                            'ҁŰϪӸÎÃˍŮΊiҒ%îĩδΚι1Ƞ1ȉЇȝwԨȂýʩȮƒ',
                            'ϭӿńƔӰбƚùFȟԅǡǖЗâҎИϊ;ҹαʳșƿʙţεԍ·\xa0',
                            'цñΚΰцɿ¡ȒϽƼњŁȂӳ҈ГƬɋɦÜЋҡˇŜȭЋњũĈԥ',
                            'ĦɅȑҰˋλˤɏϽӵƮȰʬ҉©ϵ\x88ˑΪǸŦįÞН\x80ȓ[ԁӘĚ',
                            'ԫ\x93ʵńȬżКǕΗћѷьDʎĻǃƸȌЗɟʲԖņŢΐҜҺδƔÊ',
                            '`\u0382Ę9ǁοj\x8aˏďǵ˘ˇʓǔŗЦ˕ΞзjЉƚƥіɥ\x8fƭLѿ',
                            'ѬʡʏoђӼӢѕ\u0378ҁīӱěʏñ¶Ȃŷіϓƺʊä¡ʨчǊUνĭ',
                        ],
                },
                {
                    'name': 'äДǿʛʪ˵Eˡȿ®ɽÖ˓ӴѽǵӏӤȻϖ\x83οӧѭҿыµƘǑɺ',
                    'version': [
                            -5980352524657628965,
                            -3917413291448335590,
                            -2561541979355200982,
                        ],
                    'about': 'ɶϫō"X˯ɝǝ҇ɸʹ\x90Ï΅ϓSŃίăƍͺϩ¨Ķѭ<ʩ',
                    'description': 'ЯδӧĆӤҠȗ;)ӇюϞДуҠ\x9aĘӢ\x9aʉˇгцRЦʴљĀǒʖ',
                    'authors': [
                            'Ҳ˲ԔҦʬ\x9e´џūɃōӹˋ+\x9eʢԈϴϪϩɮPϋϤïҫͷ΄Ȥɺ',
                            'ȍɗҮϲȮĺ϶ɪԘԉ˩Țâ\x92ʉőΓʵÒǻˊ҉˟ŲȕϥǩǨӮϪ',
                            'ôєˏџȹѯfΗʜĖ˼˧ʾΒʭǰɧǁьŧłұԕʺȾǆâȻƽŬ',
                            'éϚ˛ԢӷɍƮ҂Щʁ÷ʸİίΙȡͼӤŷӚ҈аԖϞпôԎˈҟԧ',
                            'KʛӕѲȾ\u0379ΛҬɻȀΏӸΥЕԄФľƿ˜ԎSƦƯʸûȴʐUǸĲ',
                        ],
                    'licenses': [
                            'ͻǛǖԅωȑǯɁvȼӐïoĴĂѰЄĮӘ©ȰƢƊʏʺűѝtϫȢ',
                            'τɞʲǗʔŒҙӯϲӀӵƲŰloů\x8aЊв¨ůҪϋî?ǣɈʹǕė',
                            'ÜƣĨˇɩǩĴ0ԃáéPǍéiӓȓ',
                            'уɏė\x81Wˉѹҟέɩ\xadɺĦҸϡԎ¨ЪҮˌ\u03a2Ώө˽ͶȮұɇ]҂',
                            '҇ʱǵ˃ƕïȣpӏɵ`τâĞˁҎǤɭԧʐӫύƊɶʆɬŤȀМɚ',
                            'кҌϣδǞӂщɎȅϞѣÆˏƯѬӽƫłIƜ}ŰȹћԙхΞҀӻΤ',
                            "ƐҿγƒϸFěǦɈͼ?'əŤŢƚҕ\x91¤ǍΈɄͲωƂїĠ\x9aӪʖ",
                            'ȥƉʞʃ˗ЗʩɜÙƩɂɗԖɆǢƍ˄уԏԎȰЀŝǛʲԉȸъԍą',
                            'ѵѐȇȖZηԜƠ\x9bɈīҰțʦugŐ˗ĀùϐȨxӷϫʹӏÛȿƍ',
                        ],
                },
                {
                    'name': 'ȮɅ˶+҂ʪœӕӚгĨǓáɠӃЍǨк0ӻʗËҽȐӚ\x8aʀĬјƪ',
                    'version': [
                            -4907073601251804306,
                            -1877118898207740773,
                            -1782033473377948133,
                        ],
                    'about': 'ʙǧʱɴӞХюɕϖƽƗҽѯʐńŀξméɃɼɞǗʰųϭ˰qƂԒ',
                    'description': '\x9a\x80ŧɟ4ϋύͺǉ÷ÉʳĿʵӌxάҕʋиƞԣŁƮ˕ѿϋԣÓџ',
                    'authors': [
                            'ϩӧΟȐәӭtʰω?Ыл£Ȍϰlƺίѡˤкɂӆ&Ñ7˙ʻǷˑ',
                            'ūу˂Ʉ',
                            'тѰϸʪΞŇųʝÓ\x8bȰԜΰǡαǁä5ӺȸԜńȧЄʓdżђԟϜ',
                            'ѠəȢʚǆҖ1ѲÜéǱǡǶӴҒԛηʞʴкĲӇʻώƷΎξVЁĔ',
                            'ˁƻ©ĭщȤēӣӶŠԆʥӡЙԥƄЮϻԖȜ¹kͱĭΕȋ˵όјƬ',
                            'ӊ\u0383Β\x8eʫѝ˘ɫ҉ͷϘĠвɿʂɦġêɏÄʪР}ʥƈȹӭΈѓʤ',
                            'Ƥԇ«ҫѕȘɳɅӱјӚȧ҅ϓ,ɢжFɐʍ˙YĎРȘȒԒӗЉɰ',
                            'ɤƀЯzɤɉԣĜѻÒ%ƢЭȑǭĀ˦Ũжſϋɦēǀȱϰ&ʒũʥ',
                            'ЖӮԋϖǗЩǍΌųɯчңӴәOǷˊqэʞыǶѫєĸƓü²Ρȼ',
                            'þ҇ҫɅѐĮӇfҚҸƏɪ˘ģşԧʋʲɁӂF÷Ѷ·Ѓѿϭѽ\u0378ǥ',
                        ],
                    'licenses': [
                            'ƚƤѳСϯ$Ĩ¬ȢΚԁҢ\x9bʾ˒ФšѐƃϨŻ÷đ\u0383ѸȚ·͵-ɲ',
                        ],
                },
                {
                    'name': 'ƺİ\x89ȽϾǰѢλҸˑӷƺ2ʟȅЌΚ˽ӶĲˍƕ¡ʀĔ҉ԭ\x91˷t',
                    'version': [
                            -9208328581332260387,
                            -2907716478812845479,
                            -3642862919311780577,
                        ],
                    'about': 'ɆѨʧëҰʧϥë\u038dĝͻѺȪƟ;iСΓϳԅЌɃɕΕϔ·ϹǜǾo',
                    'description': 'ԋ҄\x9dǽԎĎlЗНɉΉΐЭ\x9cϩɯȀѤ#ɿIĜљúćԭ\x8eƽѳʮ',
                    'authors': [
                            'ҢïôƷÝo\u0380ӹӦώ³ԚϬŹǋԓʚϪȁ\x7fʋĕҕPūȃƎϟȭʩ',
                            '·кʁÜŁĖ˞QӶ˧ϕ·ΛЗԢšɁkļүΣƮ1ўĆҝƻϊͲǻ',
                            'ǘƇɢÚεΘӛΠʾĀԁʿȨӋϮŕĬŊ{ҵң\x9aԐчųЍķȉŗȓ',
                            'ɿĎȕԖϿ&јɮԊɷͿȢÉԑΏǥʕҢïϻѧBą\x91ŏį˰\x87[Ѐ',
                            '\x9bñǐδøÀҧϐԞьΪѳ\x7fª\x95˷į˫αʑΜ,Ûвΰ˼ϼϓŶǪ',
                            'ˌ\u038dӀȝӠτǶɟ\x9fиԉȟ\x94\u0378ɢԘX\x85ЏʝЦĩјΦǧԃǟǯƗя',
                            'ŌΓɪȻ˓gӷ˒¶\x9eȗAΎӌŀ®Β<ҞƽӸΰ\x8dϩΩɺÑӶЉќ',
                            'j÷͵҉ŅѿgʩҾҀQ\x7f',
                            'Ɏʼ ɄǻҼěЊѷƣyļӰĖ\x9eǬËƷƒ@ЅӀêįˌ˫ų΅ϓӛ',
                            'ÝØǆ\x89ϫˀǍĊˀѡЗДˏͰҌӓɟҙǶīåǬ}\x9eϲʱɚҠ˧Ԇ',
                        ],
                    'licenses': [
                            'î˴Х/ƙǸҤŒ~ɧР\x85ȲÆȰ҇ιFǭǶĊłӸёȓÀӰa\x88ƛ',
                            'ʠ>ƓΟƂӶϽԝʩåǸŨĊԐ˟\x8fςұ˦\x8eƧН°бγ҄ˈԠɩķ',
                            '\x7fԈůӞҶÊыАĐ҉òğԔïʉϢɼӿҘжĘИǵÃwÅѣ˅ɟ҃',
                            'ϣɩԋŹзǃ4Ɵɨå´ƙƮȅÔǘϾеЮɖԤɟήϕȅāӐ*ӵ,',
                            'ҿɁ\x91ѼҵϐĹГϤ',
                            'ϦGƛΑ˴ǯĠˆþĲƩŦˮÖ\x9eʮǔÛ҇\u0380ӡ˵+ʱȇĔ#ƲΗƘ',
                            'ȵǅԩĿөŪɅFÄѲȹ˽ɰǞўƓGҁĤǭѣӛʣϱĠˌΤ7Ћ®',
                            '\x88cгʱλӒзƎ¶§уǊͷρȲјЪнӛ¨ÐҰϬĘϔҾԦʡŽĒ',
                            'ұЬʔÿ˛ҽvʰΤȇҵħƙĮƥŧϡĆϗУȦҡѴ©љĐƥΫΦǠ',
                        ],
                },
                {
                    'name': 'ūѥ:иĸÓŴFªҕǓͰɛԬˬ\x83üǟӜ˽ɫĘԢŘțěφǳäӎ',
                    'version': [
                            -4558777683699595253,
                            -6911979445483537693,
                            -5810414463943134050,
                        ],
                    'about': 'юðÌԞǐ»оˮԀѾ[ѕΠìεHМ\x85Ԏŷµҋ˅*»ʃԅɦѰ)',
                    'description': 'ƥµВɟОΔȾÁďɏ¶ʇɃ˥ьȤĶ]ǈǴˌ˸VʳɹӧԔʫˢԑ',
                    'authors': [
                            'ȭǯφˢӕÍƾˁ˘ƯąыʩőôȱАӻУƃӐ҈ÇSǌ×˄ǰĀα',
                            'ð&ƥhXȝԧΫԐэ(ŵʩЄϤͻ¡nӐɦѠҹН˱hǠxҩʌϾ',
                            'ǴԗГДąҖҚÆȦӦӗēЯǣͶñɹʈĺż\x88ӡԗʽќƇӽ9Ǚҷ',
                            '˙~ȊǡԝʗЃȈаǼŸЛέǔљ˲ҡˢʀşşԮǛ˰ČĘýǪ÷Т',
                            'Ϳ}ʔЄӖ',
                            'ʵϏҾӇʣЕɀːЂһԋČΌƑԖ®ŮĆ\x95Рʊ҆9ӥ˯9ΌƻоŪ',
                            '\x81\x89ʪ)ȕΕĜ\x9fӥԫłǄÍӏɥďɝЌӖƓϛ˒ϕӾǙÊŏŞ\x81ɾ',
                            'қÍǱ΅\x95ͻÄɾєΣԄdΥӐʎа\x96ѰХȬ˪/ĉύȪӣ˅úʰȾ',
                            'ϣĉǗϮÏǌǛɾұxnĜǴ\x94ǀýΒȇɪˆʌұχȉґНèӋ҇ʒ',
                            'ҺƢΡЕkȵŁɼӄƢе\u0383ūӟ\x9bƞBΗk³ϐ\xad϶',
                        ],
                    'licenses': [
                            "ÒѷǥƳĭ'Ëęԝ˹ÔȦǺЄѳǈˏȮғ˾ʪƁƪїөŇ°łБT",
                            'àÌҵźμӹ%¯ǳɛ# ǐ³ƈĤƙ\u0379ҨѓʃҀưuӿǲʕ\x83ʊа',
                            'ҊŽΏŜӼ7ҭȧļԃưɿϿԫԠɒǗȔӗȞƦǮІĖěѵ"мϭÌ',
                            "ӈɤÂ9ԞǴ|ɮʅˡͱѶq'ƒтƀɐɒǹŷʓҕ˭MԪӔʰ\x87џ",
                            'ʗÑÒźҨȄǇʇԘБƛёԩː˾Ηʶ˧ыȽӜ˰ȬќнʌȅǙ\x91ť',
                            'ӯìҡǊμςшǂǖ-\x88ӏĖɰSњхϸȐɶ˞³гɽθðʃȑļϾ',
                            'ΔƧ|ΨτӕǸҲǑʛʎ˅ҤҋƴҼèǄΊɁέjpЇ˰Ғ6ԕӞȕ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extensions': [
                {
                    'name': '¾эľ',
                    'version': [
                            -3069545865911932754,
                            -1100600754948773076,
                            -2389268962457807489,
                        ],
                    'about': '',
                    'description': '',
                    'authors': [
                        ],
                    'licenses': [
                        ],
                },
            ],

        },
    ),
]
