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
            'name': 'ĂСO²ϪҒűĽNʵψ\x8a˥вȞԣҜύơȰ"ƜКҌŔWʇǄĠɺ',
            'minimum_version': [
                -7191614374255874002,
                -711284232467549050,
                -7681395222881244208,
            ],
            'below_version': [
                -5627557574945484286,
                -416390379511035967,
                -3410457619643298148,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ͻϛԙ',

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
            '$': 'ӖǮҌ˟ʱмѦѓĺЅ-ˠűŖҲţ\x81ӿʪʒԥɡŦpȠǚÎcŜÇ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 6500356843650965092,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 409501.7987293626,
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
            '$': '20220523:220032.046188:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ЛǯԜҷƀȵŲÄʤ¬ˢʠ҄ŒďoӝưɔTŠʩ˳ɍŚǬŲҀĕ°',
                'ԃЫτǞ(Ƨ҆ơˤĮҹÏQƵďǜˣ˅Ӑӊɐǯ˥\x88ԏԌůðĊm',
                'ˣˏ$ͲʘΊȳ=x\x95WҫȀdƠȷ\x93чƽ<ƼЙĲƜϾˬĢȢ^Ч',
                'œɳϻѕϼϥŌϽĕЕ҅żʮɠȞɥŴӧРşРĠҲG˅ƹŉСүż',
                'ů˜ƉȍğǛсĒΐûƩϚŅƉЈµɴԕĊѧłʄƱ\x8eиξ#Ӵ˃ȡ',
                'ʫϒɡа\x97łɭǫ˖ˏƋ˺\x96КƈʉċѲԨȝ|ƪʚĄˌδґˇΟϘ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -3000500926440304370,
                4159697959334867383,
                -1599227559040632143,
                2950517878728724156,
                8657801137911051590,
                -8544058133020868584,
                264017792550764563,
                9062167479208780917,
                -3901266150811095384,
                4452019083374996619,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                982420.0417886397,
                953633.3028935825,
                890972.6136751296,
                -69069.25209834789,
                39820.89247977626,
                229104.95493662363,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20220523:220032.050525:+0000',
                '20220523:220032.050617:+0000',
                '20220523:220032.050706:+0000',
                '20220523:220032.050795:+0000',
                '20220523:220032.050883:+0000',
                '20220523:220032.050971:+0000',
                '20220523:220032.051058:+0000',
                '20220523:220032.051146:+0000',
                '20220523:220032.051233:+0000',
                '20220523:220032.051320:+0000',
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
            'name': 'ΤŁʽКƝû2ʾŗǶЀԍѶή#σ\x83Ӭ(ɅŲҚ\x92ҮʄШ҃ǜƿӿ',
            'value': {
                '^': 'bool_list',
                '$': [
                    True,
                    True,
                    False,
                    False,
                    True,
                    False,
                    True,
                    False,
                    False,
                    False,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ԇ',

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
            'catalog': 'ŖʥːĺЫĘϬǃ˥£\x99əӟñͻОÞŊȆҖң\x91âӷԦҠǸнĿғ',
            'message': 'иϹŻϢ\xa0őԕÓά\u0380ȮΫɎ˝ёÃÓȠɘѵ˔ŀѤȑѸӢť³rħ',
            'arguments': [
                {
                    'name': 'чƉɭΩˤ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220523:220032.034922:+0000',
                                        '20220523:220032.035010:+0000',
                                        '20220523:220032.035094:+0000',
                                        '20220523:220032.035177:+0000',
                                        '20220523:220032.035260:+0000',
                                        '20220523:220032.035342:+0000',
                                        '20220523:220032.035424:+0000',
                                        '20220523:220032.035506:+0000',
                                        '20220523:220032.035588:+0000',
                                        '20220523:220032.035669:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ѨΈҹ©ӧϑ@ҤеŴŀŞԁұŎ9˛œоƷƋɑȄφİǴȚŮ˨һ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ҷâƤм\xa0ɸƱ\u0382ǻοȿä\x99ˮ΄ǀҕ#Ʊ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ʍśѣƭ\x99\x8bɫ͵ȃŽŹ˞ő˸ВЌɃƟҠƟÆ҇ƟÇΌɾʞɥӲ\x81',
                                        'ԋϸδѫūӿƫӄ˥ԈĵІŠɾǣʉŊчЭʒƩƥ¸SųӜɈɀėΥ',
                                        'Ԅ˚ʤǩԒǜ˞ЍΈʂ\u038dЩ¾ӌϹӜη˨Ӹ\x87ΟʰȚӬǷ\x9aǍùӤϪ',
                                        'ԔпЪҹѝʬëȩΜϩʍƂΡƧќɌŐǴĻҖǃФҞ!ӴΤϾϙ\x8eи',
                                        'ȧˬԏȂ ķѱØѥʃ+ȕǰéĆӋĿÝȮǆɣвԝӏԒәɬѹĨϸ',
                                        '\x94ĲǏ˥ӡă$Ӎ\u0381ӈ˂vΩȈPƬԣѐǧЋʔGɈġnťЕФʾϿ',
                                        'ŤǪYҌƐıЃѤǚþӋεӝ\x8d\x8d²ɟšǱŹІɈѣůϔҝ\x9eʿΊԮ',
                                        'ǋΚʼӍɮɾΩуԘ\x86ΊŏԮŢĈ>ЗǽΦŁїƲӈӦčŅŏɈƎӎ',
                                        "\x99ªѸӟâǀ'ĴEșƁƟуӜ\x9aѢȗ¿ʉŗŴɏęпɶҭʍ\x9dĥŞ",
                                        'ǽŷ˓ɅʈЄƌƕИӯμɳÅԀɩϢϚʌQBȔˁkȖȷѐЊȌӷɵ',
                                    ],
                        },
                },
                {
                    'name': 'ɡԑϻŌBӈўÆЍ9%Äþ\x96ȝ\u0382\u0379"ΕĢÃЏҎƪɎΞӒʮԖ\x8a',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        144819.01459720213,
                                        913752.3552221662,
                                        -9630.419238086906,
                                        337840.94951148477,
                                        168147.7650343033,
                                        1411.9901187011274,
                                        61676.08439920997,
                                        751030.0988279813,
                                        365944.58193706913,
                                        732501.197223145,
                                    ],
                        },
                },
                {
                    'name': '¯',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'Ć6(ȔҹђȨɜԦʧCĠЙʦӹ',
                    'value': {
                            '^': 'float',
                            '$': 563639.3212374301,
                        },
                },
                {
                    'name': 'ϒ\x9cʄȘ|ȨӷΧȘҕΠҫʩǓēżȡуӟʤɪѷЬƨ4ԆſБFȫ',
                    'value': {
                            '^': 'int',
                            '$': 3860623252208044835,
                        },
                },
                {
                    'name': '·Ƀб_ӽѾ˜\x90ºˡġŲċȋιʹǢĐ˨ѓ\x90ЮЄӮƂnGÚo^',
                    'value': {
                            '^': 'string',
                            '$': 'ŝЂӱɜϻΗSĲȏňԤԍƷуĈҠǚAТЌОƏѧСũEИLʹԝ',
                        },
                },
                {
                    'name': 'ɻѹѺÜä˦',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -7211831371630391282,
                                        -2575784773738717304,
                                        -3242947459308757369,
                                        8021583934770583230,
                                        3418221647678300833,
                                        -5334609361211694231,
                                        -4638692272365076116,
                                        -8904570728454260440,
                                        -7801300728802328099,
                                        -8553863138362947027,
                                    ],
                        },
                },
                {
                    'name': 'XԜ',
                    'value': {
                            '^': 'string',
                            '$': 'ҺΓɋЛŮȥ¬п˺ϠŰ˜ʶɉɵРyǋVȎĉϺΒҫɡɜËԛѽŭ',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '˒ǳ',

            'message': 'ĕ',

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
            'identifier': "ŹʗŔΨ'ȱȦӺѿƅԛ\x8fȝˊϱϏ»ŦĹҌъѠЭԑǊԋÕӬǍɍ",
            'categories': [
                'internal',
            ],
            'source': '¡Iʫƍрćė˶E',
            'messages': [
                {
                    'catalog': 'Ņ˸KѮԤѠǃĆҰóȽĢΓąџ˚ʁЎҩF',
                    'message': 'ĒÇҦǨγȐƁQϸԃӠ\x88ҺʬӷƅȰȻͳʼзгƧʙǓϏҞƏɸȹ',
                    'arguments': [
                            {
                                        'name': 'ĥɾʉ҅^īԭéɑȁƜϡ˕ǀҬǑʄyсӫԘļŰԢĚɚŸϨүΤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -92543.94674135295,
                                                                            200591.6336555308,
                                                                            465030.86983116646,
                                                                            754595.6400273913,
                                                                            153338.64459230023,
                                                                            252151.36819138506,
                                                                            55605.61017717782,
                                                                            83670.40745057527,
                                                                            656710.0582954342,
                                                                            79065.52409203743,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ê',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǨҎӡϾϘȠėгϵĹŪ˴æϓÉЋ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӱ¡χɦςȊҪ%Ɠ\x86',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.953322:+0000',
                                                                            '20220523:220031.953406:+0000',
                                                                            '20220523:220031.953487:+0000',
                                                                            '20220523:220031.953568:+0000',
                                                                            '20220523:220031.953649:+0000',
                                                                            '20220523:220031.953729:+0000',
                                                                            '20220523:220031.953809:+0000',
                                                                            '20220523:220031.953888:+0000',
                                                                            '20220523:220031.953968:+0000',
                                                                            '20220523:220031.954047:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƑHğ˅˯˓οН',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'YӰҡGʟԊҕɒ\x8d)äŊēϑөжƾċxȮƞЁɽ¼7ΒͲę)ŗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĴāɆ˽ǑҥȫɀĪȦ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӨƄˈȮƘÐ\x9bѴeŷDӀÄǹҊœцȩUʨЅɴǪџŎʛ\x85ʿӋʑ',
                                                                            'ǎ˫ʳҡϸÖεГʰυň¹ȊƟʾьˆɲаƊˀ:ǖʅėźôʿʸ˞',
                                                                            'ӵҍ˓Ő³\x80͵ҋŇΈяč\x92 Ѹ˷ƜĚțΟӟʩНԠӼƑТμy·',
                                                                            '>ɣĄԣȻlǴϽРŇҽȿҁ\u0383ˤԐʁʁŇĒӞӪʺԗĦԇvƛψˇ',
                                                                            'ėҩɪҼDƾӴɊ˩ԘЩÚř\x9aƍȑďýˑɼĈ˯ňҟƑҩĜ×ƺƨ',
                                                                            '¯ΙƸȝʳЀęƐäȯԑè\x9aå˾ǜſҧ˖ɻΡˁÄ¾Ʀ˱ˌhίɻ',
                                                                            'ɜɮɾҙʦʋ\x81Ƈʹ\x97Ȍʛ˶eҔԫǲ¢КҕhÜƫŧӦÕԠɚƏѤ',
                                                                            '҆\x88ƪԩђœІȑѣҔЍƜӒȪŬː#ӂҗǅѼf҅уЁŘ\x87ũлҍ',
                                                                            'dǗÍ˵\x95ˆшӛп\x82ȹИж˯àϋɃω\x91©пǚĖxӮɷЇŜһŝ',
                                                                            '\u0378ĵŷěŇɆӮӎ҇Ǟȑɽ˂ԪɶԞͳ¸ɩ©ϒ\x9eξŜAΫʇrƧһ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ł×ƪƀĒҮ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҜўȺƪƎɢӬʮʯɘǄÐʞ˳ϢΣйҔƶϪJΩʆɲѪşĜŋʬɟ',
                                                    },
                                    },
                            {
                                        'name': '˴Ψƻç8ÿfϟçƵͲΉΥġΞɋɼЪdйиȭÆжǷԠЬ¦ӹɅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĴƩȑ£=ǎŦ»ɞӑʄȾǥҖŴ˂ӿŜ϶˅ғSӅýΠ\u03a2ʪӘϔҨ',
                                                    },
                                    },
                            {
                                        'name': 'Ѡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.958568:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'śЂϗ˷Ǎԓɸ҉еґόAԝƦŰśΠIӫ·њéӔѥѰʽĘԄȷ҈',
                    'message': 'ѭԩέЕƍǕЧ\x92ˑȘ˒ɴ·Īеĉʱ\u038dԄҳɇіќŇþUɄ˥ӿҷ',
                    'arguments': [
                            {
                                        'name': 'Ɉ\x95B˷ȩȺ\x93Ē',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȴԔǁӱӞƭƞÊϓͱʖɥϋӥРžΜϺ®',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 28376.94766864294,
                                                    },
                                    },
                            {
                                        'name': 'ѵҋʿԮұϨĔFЩϽϐŃƣ§щӕ\u038bҡǭɠНϏʦχԘģȃȕɪȝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'АԠľΦԁȭЬҁʀÇԍÑҷ9ϚғˤЅɖÅѤȚ÷ȺƿɦǨĤЦϓ',
                                                    },
                                    },
                            {
                                        'name': 'ҫ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8156225887633376393,
                                                                            8666144952319859839,
                                                                            6407945719783061414,
                                                                            5348654961659802250,
                                                                            -4109010795006601270,
                                                                            -7845979946876537058,
                                                                            8208067083876722912,
                                                                            2025800066284411616,
                                                                            547646957422262636,
                                                                            2759273362663678832,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʒщǠɽ˞ҢӆјԖİȒǪУơɋϢͰƈŅıўҷѶ˓ùМƨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3673178410829058887,
                                                                            1217432135509066164,
                                                                            2813072581285748460,
                                                                            4003610624373273565,
                                                                            -1883301360969468116,
                                                                            4248379168837399365,
                                                                            -7302758972593617449,
                                                                            7533182844963336774,
                                                                            5857605161583637489,
                                                                            -7796787677198836516,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԇгҲɴI·ŚĜӧфҭѷҡʜŔλΒШΞԠͲʸʢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.963234:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.963762:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ØΦȴІĽϋU;ϞȚ¹χǤǝжˉ ҠԆΧǄϸƶϨԥѧõѤɣӚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'țԁʞFӧ[ȫԊãϔñҌˊʵһˢҁӹϼĞϏ˳еǕѠäȷQƾÕ',
                                                                            'ŬȬɖЄŧő\xa0;ӛϒSwϣȌƨʛГrƻÜӲŦŧÏ˅ɃʄƕЈΗ',
                                                                            'Ν|¢ũЗҎΕƞů_ǷШ΅ΧҕϩșâσʜƲŅ˷ƃ@ҹϮӾΤȸ',
                                                                            '˛ʡȢеӷϑřŧ\x86ήĮŢȏĔɒǹЏŜкԓſЪȥCԕ\x81ĝƪʱӧ',
                                                                            'ьɭӠΖÌεϯN϶ȓӦƿɡҺʙƷҙƌιɩ\u038dǄҾҺǭżҷ\x90H˳',
                                                                            'ή³Ɍĝ˽ʷ҇ɸџȄһǿFĭΟhяҏԞӎǢͳφӍÞˤϢҖÕù',
                                                                            'чӉ\x8dŜɀвЇԅ·îʡЙɮ\x86ΧӲ˳ɏļ˰ŽàeЯʅƭн˯Ɏˍ',
                                                                            'ϘŚȑ\u0379ǀôʉѧʫǱǣǾÐφњ!жƉɝ˻ÛàҔîЫȅӷȭ¡ƻ',
                                                                            'ť\x97žøЮҕfԀҜƹЄϳ΅7Ǯmƴˮљπ˖ÈϪӶɣYäЗ˟Ш',
                                                                            'ҥȼΗȅƿéҧïΙԨӦçҦȡЕąӐɉʺ½ŀҡшĝҫЌϹɖ½˟',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '±υǜϱҕˤ˳ŗӀжѤӖŜʾϪ\x89ū/',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˓ǗǖʏÄЃțĔÆΏȡΦðĔȅΙƾыÜʑ[˒Ѵ˲Ȉ\x83§Ǚë\x87',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'мϽìʑǈ½ԢĐÃѢɑűǫǄǿÍԇӕʽΖƏƔЌ˹ԗƢĆ˴Ӄ\x84',
                    'message': 'ɼßĶҮΈĭxƂϐӵϠŢʹŇ˱ĪƶӀǎɱϙҒvɵȨȁԓ\u0381әy',
                    'arguments': [
                            {
                                        'name': 'Qƺ˺γӧɛ΅ΜȪÆȰ˩ПGÆѠhϺĈЯnӵ҆į§ѕŒϴʄÜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8526249618471594849,
                                                    },
                                    },
                            {
                                        'name': 'ѼAι¹ʶȧȺĶѥҺ\x82-ɏļӺĎѬŷɄ\u0379Ԥ\x87ɞϣͻԑ˙ǗǡŞ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            623069.1598493546,
                                                                            -9919.036862423425,
                                                                            730046.9412006313,
                                                                            -49005.61096866146,
                                                                            566975.7179916395,
                                                                            849459.5588476384,
                                                                            978170.442306679,
                                                                            535871.3859207552,
                                                                            828367.5880919107,
                                                                            448819.72444338945,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˩ťÉмhчҔи\u0378ĞԍӋоɘ\x9fγȥѢѥeмԫŒîМԞº|Ĝ˨',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҩƸªҼčͿLÌтĸ\x90īǦВ(\x80ˌӲͺԋ´ʹʎŷ˾ʙȆǷэ\u0383',
                                                    },
                                    },
                            {
                                        'name': 'ҔҘӹә҂ĂȳѝӆTԭɤƃ˚0',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'йǫѶÔƘʈ)ϒӨɊƥωʒNΦΧʭҽƷƄηΗʫіǫ˗һ»ƀԡ',
                                                    },
                                    },
                            {
                                        'name': 'ȀʳɀûӕѨǠǴ\x89ƷÑ¶ŠŊ\x7fΒƤDƋ\x9d҅Ӗӂư¿ҷǜĹƾώ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҏΉщŻΌӸMľĕɾĭԢþβȱƪ\x97Ͽґˆƈ\x8aԮćҭîԫƫųθ',
                                                    },
                                    },
                            {
                                        'name': 'ҺʧʜɠЖʶΛŴέ҂.đҍ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ҮŶ\x87aȮɐԦӻʝˀͼh˪Ԋƀ˽άŖɐǎŃɑȫȻиǹѷ҂ъл',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӨΛ\u038dìʌzƓ[ӶÂƾƼπҧ˜ˑΨɕЇЃ\xadəʗʜşɥɺŹĭҼ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.973172:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӄɯǰʥ˝Λ˚ŶДшƅrŰ\x81ðЍϹȫ˚Àɜ°ĨɈǪʘƊίԋɕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 451504.5264778414,
                                                    },
                                    },
                            {
                                        'name': 'Ʋ\x92ҕ$ʚϼkÙɨϐ5ȢΙӔǡӾ½ԫПӲČǭʺɾӹ¿ˑƁѧ\x9e',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7936130840520655167,
                                                                            -1580663087075225680,
                                                                            6289655239687495435,
                                                                            7579268593413800316,
                                                                            -7292422020727175731,
                                                                            5077962229218854195,
                                                                            -9117084042429701418,
                                                                            -1146064842691918295,
                                                                            -8535535886607286909,
                                                                            1279497171469107063,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'лíʹȆƑĕԆΓǁEĖ¯ƛ%ƺԠϩĖѶʨӔ^ԩǝģͿѹƩ҂ϭ',
                    'message': 'ŖΊϥѷěǲƗѺȎʘΙɔΧ_ZӷОǼɝ(εȁЏŁÛǎƅј\u038dU',
                    'arguments': [
                            {
                                        'name': 'АϛÖӛʳƎΌӹԢӺÑʥʩϳǋeÇÅȈeŖƼǦφѾȖѥϝϴÈ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.975809:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԇʳѼşǈÐҴĶџÎʍ\x9cν¸εͼά',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.976257:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǰ˔ԪӧѹσSĘкϤʺӱϔҨԟ\x89ǨnǙɐγ4ƮɍȶӀĨɾĆŐ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            888574.9508005191,
                                                                            633802.9238855573,
                                                                            292814.66396366584,
                                                                            281897.12114162504,
                                                                            179922.14840183203,
                                                                            998755.5166693903,
                                                                            917340.7693155677,
                                                                            71500.4906251606,
                                                                            7963.510973588665,
                                                                            619272.0753647581,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x85Ƿů˶ÙЋ¡\u038b\x7fРýŜȶәΪʔͿӬӨёčҐ¾ɍůİкĕӶȾ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҢĒѓ˒ÀʨǕс;\xadѼłÐΎſαɖМ´ӃʻǇъâϽҍƚѠω]',
                                                                            'ӕΑəΊԑЖƒȮǼи\x95ϰҝзЉЎŋʄ҃Ōϣͳ"ƄRȊǺҞļĬ',
                                                                            'ŵ·\x88ɝѴѼ6ɵѲϦӘĶɕbϬj@҈\u0383ěϐɌЩξԮеѦȪʓΏ',
                                                                            "ӗмūԪҥºӌ3ЦɏԤȠϰSǱЎƯLŋөƚҏûɫЙ¼\x83Őc'",
                                                                            'ѯºʜʭѨ˄вŃδŝNʟÒҋ}·ӼÍѵʐ˴ʁɌќƒŕƲҫ϶Ǩ',
                                                                            'ʷȟÿӴ\x88ϜʎȭѺŷƀ\x83ΧʤħӜҫʚѰɉ-ӍʾǦ˲ʌϡѭЯƬ',
                                                                            'ӗƣМʶƫ\xa0з\x9a҂gϤčлӍßƯáƵȈɠ\u0378ˀ§Ę5ɡӚҊŐÑ',
                                                                            '0ѝȷöcǢӡȻĀ;¼ĻѺӼҖɩͺӲ\x9eґӒåԌĕӕђ´ǽϨў',
                                                                            'ԭμĽѽɥ\x81ǦѸ\xa0ѭӓӆə\xa0ʀ˴Ɏҿϲ҆ˊÕ\x80ɑåĄDҪkɈ',
                                                                            'Ԫӄ)АѺЊKϲχʶӘǮ\x91ҩ[ԘɴЫ°ӶNюΕł\x94OэŉФ˹',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'η£Ϧέę¬ƀǞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4497499812869251622,
                                                                            2634155039851011874,
                                                                            -1535948671629397308,
                                                                            -6973273755780598679,
                                                                            -2257693193067363177,
                                                                            5033901149712094358,
                                                                            -1386256089843165302,
                                                                            -6560049818116413982,
                                                                            4845947935924746620,
                                                                            -3850476317113768692,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɜԕ](˫ȿ\x91©˦ѽpƮċȈǈŲԃįвҬʘеЗA*қϬѓʲΚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʀӓ\x86',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ήӴʹԟ%ǹҞʕȴԤxyȕƇƣŐ˴ƊӇȝӂº\x9eˁļèFʆҤŏ',
                                                    },
                                    },
                            {
                                        'name': 'ӵđāϚą9Θ\u0382˶ƯǲҢеɚƋ˥ҁтǎҎBϋϝη©',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.982110:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŗкɌӸђƜƯ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2522957308887105368,
                                                    },
                                    },
                            {
                                        'name': 'ʗЋԢÝ҇öԇԛҮďӤɠǱϘӿŶ¤ɬςǧƶIғ]ΩȗһɛӜˬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.982928:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '»\xadЍˎÃП\x8aƽŅҿΉƺƇŔ]ɋƯʈЖΟΕȅƳńɍȩԠȅ\x9aϭ',
                    'message': 'ōĶԦ\x83τǼďӎƣӈτΘʕǂҴҾ,˧уѹğӝԮ˲вʸˬèâϧ',
                    'arguments': [
                            {
                                        'name': 'ĲžɑәҌ·ҟĞǈĺ˱Ԁϝ×σӹªӤį\xad˂˱a\u0378ͽ\x98ЀӤƫО',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5872889777907574668,
                                                                            -3735845869835872439,
                                                                            -8247024960199088261,
                                                                            -3934962890124734022,
                                                                            -4934073851378346909,
                                                                            -8231365926197139550,
                                                                            7901029946309633124,
                                                                            5846708861299010276,
                                                                            3070524680796094479,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʧҳгȬ¶ÛŠ\x8aȵѼϚίь',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.985027:+0000',
                                                                            '20220523:220031.985112:+0000',
                                                                            '20220523:220031.985193:+0000',
                                                                            '20220523:220031.985274:+0000',
                                                                            '20220523:220031.985354:+0000',
                                                                            '20220523:220031.985434:+0000',
                                                                            '20220523:220031.985514:+0000',
                                                                            '20220523:220031.985593:+0000',
                                                                            '20220523:220031.985673:+0000',
                                                                            '20220523:220031.985752:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ёƂΩMΈ˘ö',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ưϗĞƃĄõñʺтȡɴÕ҃үˁÌρɺxΑюʹəĵĿ.ρčϾ^',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6208716998026344278,
                                                    },
                                    },
                            {
                                        'name': '˙ʱ҉Ǯ|ʴǔӝé',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 429118.14146343805,
                                                    },
                                    },
                            {
                                        'name': 'ŨșȢЄÓ˝ҙЉ˙ӀЙ҂ˮϥ˛ŷǟɹ,ƚƲҗʻċԁĊäƼӶ˷',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƕφ¼ӐȽѩ\u0381ǟóЭųԅƩюʉęжӹȏ¦ЃȂɯź',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȯ\x90҉ǆàʀĝԄт\\\x8bԫȃӹ\x7f\x9dǱȱ˴ҎЖσϓ\x9dƅҶʁӭƬʥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǙНȾȈΪϛҬ˼Ѝɠ҅àĈϜĂчоpӌˈΏǪԝĽʗȠϕ˰ɯȒ',
                                                    },
                                    },
                            {
                                        'name': 'ČЁӴŚ#кҪǻҏwƶϳǾϏѶ»ʱŃZɉΧĠ\x8b˰ӓэţϠɢΒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ɓƹӹ\x82҄ʹĶӎĮӻȟӎϦ$Ôȩ:ʦɳѝ}ѵƀЪЄΖŵȉι\u038d',
                                                    },
                                    },
                            {
                                        'name': 'Ȃʷǆԑ\u0379ϾʆwǁĦĚҎ˼ĮСԮîϰgцԏӔϹǾɀ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ѷ·ĻÏħŔш˘ϩɓSɽȆϦãͳğӋÞʿѹˎËȼӊƁΖ\x85δν',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӧÃԟɌÚιǘ~Ǆ\x95Œ¿ΙӱĽ˯ȵLǞʓʍɘãԋæϫҤԇʇȢ',
                    'message': 'C=ȽĕĶҁЋɧͺĈɣƮ!ҐȖѐυ@4ɅѤԞǼӃȶӥʹΓŘ˨',
                    'arguments': [
                            {
                                        'name': 'ГӵȞɺɿƾŐ9ӖԜҥȴʇ»',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.991753:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÿŉλſҽñїκɐɴǫ1ʾÀ?ĝěĊϯǉʞęЦɺ%',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.992181:+0000',
                                                                            '20220523:220031.992265:+0000',
                                                                            '20220523:220031.992346:+0000',
                                                                            '20220523:220031.992426:+0000',
                                                                            '20220523:220031.992506:+0000',
                                                                            '20220523:220031.992586:+0000',
                                                                            '20220523:220031.992670:+0000',
                                                                            '20220523:220031.992750:+0000',
                                                                            '20220523:220031.992831:+0000',
                                                                            '20220523:220031.992911:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƗnψԨѷbƼ˾ԌßзŐȂɸҔɪˋ<ɁǏ˨ǾŕΫýʋԣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            137236.8501270756,
                                                                            262017.6348264545,
                                                                            635460.1412227263,
                                                                            978670.9178017471,
                                                                            607083.8523299425,
                                                                            492633.55595963425,
                                                                            526006.4124610354,
                                                                            293330.88201144483,
                                                                            980857.8947835579,
                                                                            381880.51227751974,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¯ȰӕѦ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'џŗʗˆæϚÈҕ~ΚåλyвΜɣǐƯɜǢ϶&ʆˆòԈǍòŅΠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҢʖɢƖŸȤÈ\x9fȆӾÈƀΞіѾʊ\u03a2ѨʣҩԖ7ԍӾўģ˔ªʼa',
                                                    },
                                    },
                            {
                                        'name': 'ʽԕЛӻǷΎҮ\u0381γЙƨӥ!ύ˘ҨH\u038bǼҁѶšΤѦƄĠʩˁӈɯ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȼϢӦġ҉É¤ʪç\x9c?ҩΑҜυʂ\x98Ó˥ɡȍҔљӺҭMǏϙ¶ǉ',
                                                    },
                                    },
                            {
                                        'name': 'ҭŅǬȧш',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            60875.88618028382,
                                                                            205813.6612852016,
                                                                            152236.31264214683,
                                                                            528497.4297550333,
                                                                            -32660.463169557566,
                                                                            724440.927089004,
                                                                            10636.22036203729,
                                                                            118409.755040319,
                                                                            490951.48498953553,
                                                                            668498.3262094891,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'o˙ȑЏЁԠȹȄpƒОǰŻˤ(ҪÇ¿ӤgϴχǧÅчȠŞžâԌ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǿɠԦγ^\\чÖЦ®ʗѴӻҸÜUĊSъ\x8dȁ˃ѹŌӰďƵŒӰы',
                                                    },
                                    },
                            {
                                        'name': 'ąʋҸ˲ɽ˙keƃ҈ҬʂĸͶɶPКɊƽҫѫ"ҴɫӏїĶǘɮ3',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5377107855976432740,
                                                                            3357756924037406370,
                                                                            -8029597776960122182,
                                                                            -5693340714764159348,
                                                                            -2584613500065980810,
                                                                            -1804452396734252514,
                                                                            -8009598231472041526,
                                                                            -1835079717692236984,
                                                                            7375282096714007268,
                                                                            -8036057190568270449,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҢǏnƌƤ\x85ɏ¿ӀªɪʰОķӫ÷ŷóȲŉˁȃ˄ԠƴðЯƣγɇ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3500198049348339580,
                                                                            -4438406704296725167,
                                                                            237563678280113947,
                                                                            3250515827166359934,
                                                                            1723190801491269208,
                                                                            8967179661995885679,
                                                                            -6103496757516632095,
                                                                            -4852893466994835085,
                                                                            161436924596914522,
                                                                            -1229861364290793552,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'λ\u0381ҍɬǵɞϝӮԍȁĽΤԠϙͼ˵ÃиǬ5҆ĔҼǔĬ˜ͼǐˈƵ',
                    'message': 'В?¬ŌϹˠťƈ¬áК΄ƺˣ˅ļɂƭɨŹʑĮ϶˧˙ƌƦϢҹȏ',
                    'arguments': [
                            {
                                        'name': 'Ȝ6тð',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220032.001346:+0000',
                                                                            '20220523:220032.001431:+0000',
                                                                            '20220523:220032.001513:+0000',
                                                                            '20220523:220032.001594:+0000',
                                                                            '20220523:220032.001674:+0000',
                                                                            '20220523:220032.001754:+0000',
                                                                            '20220523:220032.001834:+0000',
                                                                            '20220523:220032.001913:+0000',
                                                                            '20220523:220032.001993:+0000',
                                                                            '20220523:220032.002072:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'к;ī\x8fɸё:ģҙӳʱγƫùџ×\u0378ѯʮʼǝɺӟˤԭȣλҷʛ˹',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʲˈãǾԚɊUδЩВіȃʩKǬѧǑӉȷǫӴËӷɎͶ¼ԥсʁӂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            308118.8282155849,
                                                                            403777.65754188184,
                                                                            556302.4853501652,
                                                                            788577.6481994152,
                                                                            223801.14480163046,
                                                                            747074.1596785806,
                                                                            -31277.914359186994,
                                                                            824776.1044551401,
                                                                            805063.5445600324,
                                                                            754181.1270634462,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˽ϙĶȾĬɰUȎӻԝ\u03a2=ɯӗϦҙ˙ʸ˵ԔБΎҹȃēƇΚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5740630772504993741,
                                                    },
                                    },
                            {
                                        'name': 'Њӯĝąе',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220032.004677:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ł6шƍ³ΑҰƃΎНѷȯҟʦx?äűϬŋ\u0381җǂв\x9aǐ˱ZŧӠ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 785865.2848194011,
                                                    },
                                    },
                            {
                                        'name': 'ȻLŕƺϕЁxҀʎґm˧҃ӗѲʙ˯Ҕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220032.005496:+0000',
                                                    },
                                    },
                            {
                                        'name': '#GƁƜӬIΰ=сtş',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 228680.62688233174,
                                                    },
                                    },
                            {
                                        'name': '˒Ӭʘ.\u0379щºϛ\x93',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƚӢҏŧƜŪҏϸɁÚ˃ƛˉͶ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220032.006692:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӉƥȡŻŗϘɀҪԨȄЄWЗЏŋԁŊúÕƳʻĬ°NѣϸͽϗʦЯ',
                    'message': 'Эʻ\x8d͵ƻɂȉѮήʵԟЊҵȗƟƯǲƇÿҨˉ\u0378ȬңDŕҰ1ĩæ',
                    'arguments': [
                            {
                                        'name': 'ΑʌƼǊ\u0381ԞȷƸ\x8aż¶ОŊȒϒxƱϰļςÆԕūĸ\x9dЏѩ˲ϔҢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220032.007634:+0000',
                                                                            '20220523:220032.007719:+0000',
                                                                            '20220523:220032.007801:+0000',
                                                                            '20220523:220032.007882:+0000',
                                                                            '20220523:220032.007962:+0000',
                                                                            '20220523:220032.008042:+0000',
                                                                            '20220523:220032.008122:+0000',
                                                                            '20220523:220032.008202:+0000',
                                                                            '20220523:220032.008282:+0000',
                                                                            '20220523:220032.008362:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѷ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĉȇǮԈԩ*\u03a2ΙȸƊξ\x92ĔЗӃΩʳϘiJĝģ\u0378cǝШҴ|ćЮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -619259263368077472,
                                                    },
                                    },
                            {
                                        'name': 'ËϿzN҂',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '²ӒѻČƗΧµѧɞ˟ʵ×ƖʄҒЛѹԎāҠDƤУφİƗƝѕдx',
                                                                            'ζĕӗӛ˻˫ǝǰʖφΒÛѳҐͿ©ǥҐϠχɌЭ˅ȷǃʉH;ȹƄ',
                                                                            '×қѺĬύɓʢIґԨΌˮȏ΄ɐөĥÙůѼъіÆ϶ƞϮҞɃџ¥',
                                                                            'îːjΑȋϿшͳԦƛ«\u0380\x91\x85аʼϗΙ\x80Ε˕XʎѰ˗ȻЧˮ ɦ',
                                                                            'āʖӫѸǕͻˢăȏρ\x97UĨǴɩϧƐÏԣ˳żѰ/ˆԓʌΏҧêн',
                                                                            'ǪѺƐƕЃљǟ(ɺ˩ЈѹŞÎЫÐő&¼ˍɝӃљк˳3ЯӸ4ӑ',
                                                                            'ǒʰԎȞҲöƊǮɌ\x84˭ӈҋœɿԁщ˲w<ƫŢӃͶ˘oϫɅʸē',
                                                                            'ԬƉ\x89Ѻ\x7fӾʿ˛ΑđҁȺΩɃʹғ\u038bˉ\u0381ѧϣΌҀɭǦΪ\\ϼĄS',
                                                                            "\x864ӕïɷӯûǜȚ˼Ǆʀ΅ȃ/ԧ!τʜȂ'\x89ƷǬϩѶȯб/Ǫ",
                                                                            'ϜȘ±ϟ˕ɈǊĄ˱ҷɶʃďǝǡѕЙӝϸӺԓǸɵϹSƋх¥ЉѢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ðŸаӹΗʟŲɏϏԤƌɫȟ¯ÞƭɺZÐзƯɒˋħô',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220032.011938:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɤԃĂɛéҳҞϒΆ\u0383ɚųĊŦ˭sóԫ°',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2212373663988107875,
                                                                            -3796422686306842997,
                                                                            4001362538728274542,
                                                                            2198962183729028251,
                                                                            4291606927199425043,
                                                                            1125480788395971462,
                                                                            6178812775299563014,
                                                                            -3771104132381178446,
                                                                            8045864992413924498,
                                                                            1931072462277597457,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʽǔ>Íèɍ˔˪Ѩ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7995374791792019605,
                                                    },
                                    },
                            {
                                        'name': 'ȿ˳δ3ƆǴšѢПЙˑnϻВ`ɌζÛ¤ŠϗȴÚ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2010851343256433550,
                                                                            -7220771711527041634,
                                                                            -2011437334417218777,
                                                                            -6823806202417547974,
                                                                            6069631377481083793,
                                                                            -6672142527870290959,
                                                                            -7653237103262195177,
                                                                            -3919589783976147910,
                                                                            2252772883001240502,
                                                                            -6898828767143232449,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĵƗ¢ˆϚöҝƸǄͺҎԮĉǫÄGȅіѱƣ˵Ůԉˈ¥ѩɒϹ_Ҁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÆĠɨЛͶʅǇʙ˜ò>kƃ`ύϛτB˨ɦ¨ʵÂÎ˙ʬdϩ·ν',
                                                    },
                                    },
                            {
                                        'name': 'ѷļÄгњІpӷ²ʤбӖʽʺɶЄЎѭĂІ©ėʬȉщŲӻΡʂ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'őʂдΧњƅŅҠƺ¿ƙ!ƤӪаȵԉƹļȖȗ!лxʶγβȟ\x92ѳ',
                    'message': 'ʆɟ\x94g®Υ ˝ɳ҇Ԓͷȏ˝Ŋ˾Ўȇ˞\x7fƀŸԝқŔɕ¨ѽͺɆ',
                    'arguments': [
                            {
                                        'name': 'ɤҢÚсԖȩљʧҥӤvʆҡIϐз<ƹ\x88ϊļʎΐ˽',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 625579.1408934002,
                                                    },
                                    },
                            {
                                        'name': 'ПϤǅЋĉϑũʋɘŒүiˀü\xa0Ӥò\x92NҀ\\ƊqɊɑɞǔėţҿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220032.016946:+0000',
                                                    },
                                    },
                            {
                                        'name': 'λȯsɏàӜś!ĖžӡǴɴ˷ЊșӞȡΫЂįíɧhĭɐǨèìӬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˍӉ˴оƉҧÕˋʿˠƀGÅÈґʡǊøɄπ˔õΊǶκɼǟ˂Cɶ',
                                                    },
                                    },
                            {
                                        'name': 'ԨſʼԭɘŰ˒Ͳ7О\x88ʱǨҡơĻ¿ʒ˻ČиѦȀħɏodϬ\x83ˮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220032.017792:+0000',
                                                                            '20220523:220032.017876:+0000',
                                                                            '20220523:220032.017958:+0000',
                                                                            '20220523:220032.018038:+0000',
                                                                            '20220523:220032.018118:+0000',
                                                                            '20220523:220032.018198:+0000',
                                                                            '20220523:220032.018277:+0000',
                                                                            '20220523:220032.018356:+0000',
                                                                            '20220523:220032.018435:+0000',
                                                                            '20220523:220032.018515:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ϽέǤûŊrũʕ4ԟħǹ'ϩɽłǹΆ?ΤъΣÁӇўъӯʎҖ?",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            355170.1294211162,
                                                                            30611.755433090017,
                                                                            96093.92199395152,
                                                                            -84641.315677462,
                                                                            419218.9979717917,
                                                                            240310.79053464328,
                                                                            172019.41312736843,
                                                                            199987.93542386062,
                                                                            459377.9797797634,
                                                                            -4080.7428255231353,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȃҵӅqˆϴȓ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʥęăӣȍвҝ\x91ԐҦТΊť"oʧкҏҁųʩiŽc',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            939347.6385304217,
                                                                            604178.5662097489,
                                                                            826024.4642204108,
                                                                            486137.6958454035,
                                                                            322453.31270717917,
                                                                            347050.7949387283,
                                                                            371700.79950013064,
                                                                            -16988.4611507386,
                                                                            504836.39002485725,
                                                                            516162.63654924266,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΑʺǍæϢ¸\u03a2Ȧ\x91ÈȻǗHȈŔŰуθǁv˦ϜƜцѩΉǢϢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1859378788470793414,
                                                                            7107392810058477308,
                                                                            9203393176659739803,
                                                                            -3794079639715125018,
                                                                            1464460913733138825,
                                                                            -6447579794674035829,
                                                                            -6686325321223778859,
                                                                            -2724427835609627704,
                                                                            2405537075922796537,
                                                                            -2424467764636819185,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'XʩȻŸɺa΄ѵǹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'όҢʆĕėӃѝƄɱκϗśƍƫЀ ah½ѵŏʾϵԠƏ\x99ƪˑɦì',
                                                    },
                                    },
                            {
                                        'name': 'ҧ¹UʇҊҩǡʏɕҦ˳ѼЕŚGĎưǽ0ӝ)ԉŸяƔѫ˛ǾǻӺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѧҟиɉӟϦҌƩǄPõǉ\x98ѕžǒzӠʅǘҜə\xa0ӪʸƗĉΘƭ҉',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǻΖĔźũĲϡѲҿȥϡƭэǓʑΉŖˢĊ®ȍ\u0378\x91ɬ˓ʐƫўīĀ',
                    'message': 'ЎˣҲʒӌ¶\x80ϙʶђφ˪Ƀΐ˹љŸǕҡЊ\x92seѶҦӀҡəЅ˺',
                    'arguments': [
                            {
                                        'name': 'ǺǬӛ˺ҀӚέ˥ǧϤkȈԝeҌѾϖďķÿìÅЦѫѧƘBǢˈž',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220032.025324:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɾΐâɿǍ\x82ѕŞ«ªιˎɇƦϳŻˌѧΗϻɶΐӯʨφʞ·βƳÛ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'àyńϥƝΰӱϨċ¿ʣƎĦ˹ӧÙɩŨ˃YŘΔ˫ˉøѱšɄĐү',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220032.026167:+0000',
                                                                            '20220523:220032.026252:+0000',
                                                                            '20220523:220032.026333:+0000',
                                                                            '20220523:220032.026415:+0000',
                                                                            '20220523:220032.026494:+0000',
                                                                            '20220523:220032.026575:+0000',
                                                                            '20220523:220032.026654:+0000',
                                                                            '20220523:220032.026734:+0000',
                                                                            '20220523:220032.026814:+0000',
                                                                            '20220523:220032.026893:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ư.ȿӢˡ΅$ɛʶПτΚĤӵѠîȨ˩Ëļ\x9eΪɉӈѥɹΛ3',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӦΊĥɥLɣūΖʢҤĜѸӏɠЧī˶șʟ&ˎϸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            881175.9909299486,
                                                                            273540.4341664372,
                                                                            312295.47538216383,
                                                                            11816.28355108219,
                                                                            772353.9987300512,
                                                                            815885.844090104,
                                                                            901415.9921980471,
                                                                            -257.42604416247923,
                                                                            682099.7616874747,
                                                                            930844.0312905702,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƫ(˲Čŧӵçz^ʧМРƸˈЛRÅĤͼ\x9eәÈϛʮ\x89ӿƺĀϭϢ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220032.029135:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȗҲӷΧȰϩƻϊϳŎӨ&ѣǺэӮǦÃ˕ԤƑ´΄ƞēÑӜɻźй',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220032.029567:+0000',
                                                                            '20220523:220032.029651:+0000',
                                                                            '20220523:220032.029732:+0000',
                                                                            '20220523:220032.029813:+0000',
                                                                            '20220523:220032.029893:+0000',
                                                                            '20220523:220032.029972:+0000',
                                                                            '20220523:220032.030052:+0000',
                                                                            '20220523:220032.030131:+0000',
                                                                            '20220523:220032.030210:+0000',
                                                                            '20220523:220032.030290:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҠÇȷ\u038bɚƫҐ&Ɲ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'uԫξsѨÏ҂ˎĚʞҁѠǉЃưνҌГǗȶυăɗ;Ɨʬ_Ћǅ\x8b',
                                                    },
                                    },
                            {
                                        'name': '\u0378гϦәȎǭȝƴYțĎȹĄʐǙЊŸͼΚӝԓƧϪƲˉϷÞπDҟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɗНνԨϿNΙʤƇ\x8b<ӝ&˫áѰσèѺȻʩɚўԔ¤ԛ&ðȜʉ',
                                                    },
                                    },
                            {
                                        'name': 'IϙǗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͰǏЉƈϝӍȰΓƪԑѯʫӪɹѠťǍПǋӾŋ=ӱȗɩϚΜǨƑÜ',
                                                                            'ҀɳīЬÉԌӟĘƬ,ŏǭȪͽɉԎͲîɾҴ·\x7fΕ\x85Ɓ˖ůʹж˧',
                                                                            'ǜėʓ˫µĵӏΟΡĜ\xa0\x86Ѿː˟6ӹʓχγ˯҄ÌƓθŲÖÕҕƦ',
                                                                            '¬ǬðůѩɳʸåÿĝсϮȯҸȁƅTŗ˱ҍʼğҽҨśðӼЭήЎ',
                                                                            'җ\u038dnΨӻƘҗ°Ғǜ)ʙэŐǀµÁԝǆсȊĿȼūе5ΌѰĤβ',
                                                                            '±ɠ˹ҼӓĆԒϟʖʚǀȎƐƹ÷}\x9d»¨Εɤȗ=ńѭ˚"ŗ~Ѐ',
                                                                            'ϴħͺʅҋkѐώăȜҨơ3¦ҳӖơǙő\x86EŢкɨƑϩԕsʌʯ',
                                                                            'қɥРĔ9ϐɄˏǩˇӣΟǈč¢ƼӏpǛˌԎɡп\\ȐҼĠөΎϫ',
                                                                            'ĽX#ǆǑr_ƌӰˈǤѧɉςӸһңǐƉƠu˳9kŉӤҭìʣҏ',
                                                                            'ˇʷїѧϺèűȨǯѠР>ѳІƾxǤͲʹҾЛЖΒȵőљ˞ВĻϻ',
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

            'identifier': 'ӟÈů]Z',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': '\x8et',
                    'message': 'ð',
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
            'name': 'ĭΒǛǑӕΐӮƮЊɠİуцːϱŽȷɊˉ˷˶HϛɹɬΣĂčћɏ',
            'error': {
                'identifier': 'ϨLĺϠԕʒˡʯƛȐKł\x87ŴΠѯȐ\x84ў\x8boʔԪԎԐԥˁϙɸƞ',
                'categories': [
                    'network',
                    'os',
                    'internal',
                    'access-restriction',
                    'internal',
                    'invalid-user-action',
                    'configuration',
                    'invalid-user-action',
                    'os',
                    'invalid-user-action',
                ],
                'source': 'ÝqюÔ\u038bɂƽȁ˻ɘƟИĻ©ɫßԩƶ˾ěĒʑͿ\xad҆ӕʘCӻə',
                'messages': [
                    {
                            'catalog': 'âШĜĨɒÏÛþˣ\x9bƫÖfĹǮųжr=ԁƸѼŤĞҧΝπɼΕ"',
                            'message': 'Ѳϧӝӭő®#÷SӇˬΫμ˕MǶɏÜŔΠ\x83ά\u0378ԊøŉȼЛāç',
                            'arguments': [
                                        {
                                                        'name': '˫ЉɈŊ]ѨŸϰŚϹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĹӦҟϙKȄЗȖʄǧԚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͽԍѫǹʺͷȅ϶ӜҊΪд',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5081797526883761143,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈʳȵƋȲƐɿŬ˼ȘʒҲТã±ʄγɘБƹҡȤψȝҨӸξŔȿв',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2547656221341862775,
                                                                        },
                                                    },
                                        {
                                                        'name': 'дvŧȤěϓ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.903965:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝȵϿΊƇϑǘŏɿ»',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΎʤɁŐԙʹѻʑжŐNQъѱbϹ\u038dѹƭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĠϭηĪēѬ~"ƒ}ČŭÿEқҝњˋǡrĞĬԠƋƲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.904759:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŬϷˡγ˥ЊŢԎӄєǒȭȂƫтʑ>ªĔÙĳØѓΖʛЊԍʲнϣ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Є{ӴƮΛŠƯԬîŤŤǾԦȅʂϘÏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠңԛĂ;ˈə·ĖυǷѰǵɡǴʈҌ¥șԖ\x9a÷ÃљŪԗė',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 157086.45453240912,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'BςóĠńʬȤ²ĈҧŶÿƎȘήîǉţӛʋˋзĒͳӜș˃\x89βą',
                            'message': '˶ӪƴǷԚEΑɸƫ\x98ËΙҳ˚ˁŋŭό<ȿŕ˒ԋɦŊЩ\x89Ѻǻͼ',
                            'arguments': [
                                        {
                                                        'name': '\x9cƙҶġɃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÿЖӦƒȧż³\x95ґҴɊʵɁ\x92ƎϳʰюţҐ1ӲҚğɡȭԤĵβѴ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠˁɇĥýɽӼɯʏОѬȼɽаίˁǞӟƱǪ\x87Fů˕Ύ»ƅNРě',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -520267946853430094,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǎāɒ\x87ĴȣƄɼгӗǙС8`Ѭ\x87˝ΪʀīTΊůÆϛʠβ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7106431195724555461,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ұөӂƱƚɧǆϼкʗ\u03a2\x82ĈÑȠϻʹͿ҇ȝ\x91ɋԬȔˤ˙ъһÔȚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϱɞΎʁӂəɟɶҘŴ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 619778771756544095,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ъ_ӈңКҥҽĕӨ\x8døΥΦȹɘЕӌƪɛάҋХΓе',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƿƭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ǻӑǙ'ǯÂɹɆÛɜʞƓġίτϘϋԇϭċ\x9fϋƝƹ;\x84ʝ˂ʇщ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.909683:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŎģRǽȓʓ˾ЫǹĈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 688000.7928628302,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЗӔИ˯ȖʚΕLԣ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 64710.18930048705,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΝʠǙʹĳʢ{ÅòŕӍǃȫW+үѭĶzɚ\u0379˺ԙѨʜș\x8bȡȉÚ',
                            'message': 'ÙӚ?ʖġȼѶӺŚԋȂЏωȷɭΐȓɆь˝Үǳ΅ҳŜ\x7fȬӊ ӗ',
                            'arguments': [
                                        {
                                                        'name': 'ȄЄʞĥ˕êӷϧ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑХԔ\x85ŔʩυѝȦΛƉSҶҜ˂əӥʘ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 986957.2063428443,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦљ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 483952.00860909186,
                                                                        },
                                                    },
                                        {
                                                        'name': "ǬіǔYϔɦŘЬ˵ђɘ'ü\x95ЭЭˑʣмӟɏǁ˲ѱºʿƎŋűԦ",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1444538258188304578,
                                                                        },
                                                    },
                                        {
                                                        'name': '¯ѴɖҡЧgфϒoȊ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.912891:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƲȡɂԖϑчӹʪɀɫŇɭ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'J҆ϥ\x85ŜȨȺäҷϡŻчЩ^ɼȫҲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌҶƀϼŅȳDŸēɿʚ\x86ά_iӒǖ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӰЭЖʕćŹȶŧ;ȩ˕ѨƩòǊɖŖǚʸӟĨЉϠġmǟɅ\u038dӶҞ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1359908696071893496,
                                                                        },
                                                    },
                                        {
                                                        'name': 'æΖ˱ӊӔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1326435693514137164,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˣhԖŚӺͶʬҔđҥŊƲÈѼȅơlζѕÀª\x92ϨĥȒů\x9eδκͰ',
                            'message': 'Ȗɤѣ\x8fǚǴΐɘԋѤ1ʆɐΑ˼šҍÕƔÔɱѰɰғ˝чϵȯ½δ',
                            'arguments': [
                                        {
                                                        'name': 'ӆˣȀȀɪͲϲυɅņҍāŗҨϡ1ԈǈđǪβǛŉɸŴΚ)ȣʤЄ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.915808:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӉʴǪѥ±$ĜϨхϗýʘÞӎ*ѓɵӦɋΊӧӛŐѹϛ»ʸ¿ǁĽ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Э',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -19906705603314392,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʵмɉʡïϱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'n˟źԘːĪ˼0?ϔɤҰĦÎĿÇřΖșӂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2872586034647547800,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѡφïƹϥʛɝҘԈӭɓȗȡӏѸԔÉɒÞ\x86\x8fұïƯɡş˕ϸǰШ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ů',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.918195:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "ΖŰƍ˞ňΐƛжŀ'еАЅԝіʃĒжԮӹƮʀǝŷĳҸǢЦѐȂ",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƗɈУɤΜɚÔ¬ȫƿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϫǈʼƄʝɑşԝϦZЦҐΝÑӑϴ\x90ȿΏӣ9\x8fЊĕƇō2ɒϨȎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.919448:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӻʓ¬Ǩϖ®čʆƖŢWżʻҖɆ´\x8fŏ\x86ɡ%ƲѾԏʥҵМҷΈǩ',
                            'message': 'ϤρгĎΛ\u0383ҠSǜƚϧԌӾbǡˆɵR˯ӮҚԢƜѮƣÕʯЎгʎ',
                            'arguments': [
                                        {
                                                        'name': 'ѕƯϤЏԐØ/ȎÁƠɩ"ʸϵŒÎʭŘȮлѸÁǴõ˛Ǯ¦ѤʤĎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 908580.3004053769,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ц',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӿřϲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϕϾԬ˔ǶșЋǽ\\hϼЕ˕*;\x90ǓԫʜϏӵ\x83Χпʩӣӧә<˭',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'мЊҕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.922351:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˆϵΈɶƱҥȔɤȵÑɋǧΉW%ӜϝǄѭÊÂäSďɰnә\x91ȺW',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 827212.6343417394,
                                                                        },
                                                    },
                                        {
                                                        'name': 'дÖŪίŘӢ_\x90Ѡɹßʖ#ǎϘķƳǄΨΗѬќ\x92ǝѰǣŧιʉÄ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ďƎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƠĞʿю`ȸѸʞ\x9aΦͻŜϳ÷ʡϮàЌ½ďų§ƖԭӇϜƩӛϢт',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 110338274880400638,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƄʹŨ\x9cѤȴ˛ɒ˘уǘʂΖԈӵȔǥZӪϛь¯ϛǸÝΆfӡԗȴ',
                            'message': 'ġʵ\u0379ǧ¸ʊљЦ˝ԑĪɳǠĆ˘ʍǮǋʢ˹Y÷¯ǜƀȱωǬŌĤ',
                            'arguments': [
                                        {
                                                        'name': 'ȝΩӄąáżȎ˲ȠĻұÄîǘ¥ĻÙSϯόŋÁǖμ΅ėɔŶԎϊ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҷҽƠҫúхƤҦӕТȳȤÄˎ\x88ԞƢʹĖςǴԦҺ·˳ȭÐy˕Ӡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȹƙʱɵχϱνĘ˱ưŖԭ\x8dҘÇӭσМѰϢώŎWāɄҴ\x93ғԧҝ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˺ëЋί1ÖƦϟĐɓÐɓҩӌҽƜʵзКԍͿǾӨϬĐЇњҊ9<',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϜŁӫȗɜ¹ŀҊҮԬŦԙЦʵѢĲʩԌΔɏɑɥҳǛɒ¢ǐAăǖ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԝұғǌʄ¹ŀȘ҆Ғԕd',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 761544.3005036019,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƴǉЧɆηÊƽCЕàÝϷȜҞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧĶʎҧȐɐx³иЊγǏюtŘͰ͵ǾĿѡ˞žƋǛ҃Áƪ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮњВƸџҫϮԔԁΓɌůΑĔªϦμ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҢčzΎңǏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƞѭětД˳ϐ¡ϞɄɘӊѻӺͻ˙ɉԮԐŇώɊÈȊʨҵƊʨіρ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґ҆ΠɨӢőύԞƟԞϼƓԬƟŏʾ˭Č˷Α˾',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ңĵĐŒҹñ2Ηǫν{pɌƜɠюɡŵŅâÿΟӉü\x8aԖÉȸ_я',
                            'message': 'ȍTр½OƹƵΩѮγѲ\xa0ƛΟǦϐύÔÈȊӠŬǧɒЈĸцљѧĊ',
                            'arguments': [
                                        {
                                                        'name': 'φƊʴԟ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7242717935096075664,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÒĘĳ½Ȕжԛ¹ȶŻˮ˝ơƢμϣҸҞ΄ąĨʮơɶɝӭȍԛĴб',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԪĢȀĮҌ\x80ԨћͶьȄԤӮӯɚ˸ĕЍġʃğӤϷЏζ&˃\x92ӕć',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŵĉÌҏƫǰӍƲƼҎ¶ΟΡґϺϼʅƨΫƙЃүlϑФÀ҉˶҈ē',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382ɈӚŗĠ{ӌţʹӌǸȚ\x95\x83ϑʡć\x8cǦћƥɢʖјʿH\x85CϬӒ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ыgǥɳ1ĹσМʽ\x8dɶχЙͲŽѐІ˽âő\xadԖèƣˠʷáϘ\u0380\x9f',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΝSīͼĻʴʉ˙ʕǒͽĚԥʿ˞ȟԋÒɪДƮėɫġԮÇ˅Άԫđ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɞѯjƶʟŦɀÆХ¡ҠBÚϹ˶§%ǝВчϾťј$ѷǓŐ˄ѓϵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4528051380248174034,
                                                                        },
                                                    },
                                        {
                                                        'name': 'яȎ:âηxѪGʔɀɩϖș҄FΤļİ\x82ĝǎȗίҾ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÜŝɵĻұʱȫ˃ңԜΪɂȜϮѣľžĎҶƚƘћѓîʗņғɽɀҡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '=ȸî҂˩ƛa\xadɵf#ŊƒɧӿŅ$ɒȔԊԖľɉĳęӘaԙŖɒ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 926446.5706965863,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϏɞƮÍʨǘȭ8ѢèЃǍƠҋиѴԣŤĥŶʌI˕ÆӔˀ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '§±ҡȲ˃ȈʭƺʑԋύԔ¢ѮϯÁԦΥðǦĿ\x92ƏЅĒđ\x92ԝбà',
                            'message': 'ͺǱВ϶ÕƢEiHć\x9aŇѕįǶʈ˩ΰѿśǕǮɨѸʲ×ҷϲǯϾ',
                            'arguments': [
                                        {
                                                        'name': 'ƦТǝԃɹϘƤ\x96ˬåЪǐʑӻƭǷˣ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -55682.80073617079,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ыŅҫøӠѣѬϸ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ç÷ŴԪYBјχΊΓŭɈɿϛЃѶΔҏДȪȰǪǏԎӛ{µ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȜĬǿűεťʙ\x8eɶ˱łͼ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5856838775822544789,
                                                                        },
                                                    },
                                        {
                                                        'name': '˸',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ǉпɤͷϝʶ\x8c϶ȸ\x96ЅřfԮģ˥шȩĸųϹ˻љӟȖĂґÂʢȧ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӡȮ˳ɑɼŻҘҾÌŉЯБʞ˻ҭϮǲ×ӮѝŹʀБÖϘǥǽҩ¤˖',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʢԈĳƵУÓΐMŮƮȬýʂјҦάΣƶȻѱҔBХƍʤɯǛ1wҼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 413749.6625561672,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϪӚÚ\x83Ԗ"šðЫƣƶѪ;ȳɯöɣӌǠǁēқϚġɯŷƉӻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.937610:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӓǆH²GԝȪƛVИ҄',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԔȊ°оŨѴԆԝǰʘ˚Ԩʈ;Ȕɱϯ˘ǰʿħŦìϵ\u038diaЩǧҖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7787187430543071813,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҔΤ\u0382ČàҊӯѹҧȊʙөųԒԬʛƍӝƊÑȂÞ\x8eҎΗZz{ƯУ',
                            'message': 'җλ˽ʜÓʐάҎɣȇ˃ƻϥԧԉv¹ϩΫӜŹGʅѩŻѐαʮ¡Ö',
                            'arguments': [
                                        {
                                                        'name': 'ƵŕěК',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -164315360140456568,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԝ\x96ƽͳɍҹȅпЉЋʵ(ғҋʈӞǃʼԞʲѐϾc\\ǅȼȖŠҬ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 348306.79041524825,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǣʨǫ˔æӆйǇȹԠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2963136655112500384,
                                                                        },
                                                    },
                                        {
                                                        'name': '҉Ċ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǯҚԆƀѾ˓ŝ\x8f˰ȼǃʘđ«Ķ\u038b#ǭıũЩ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -82904738456184081,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӘŊҫʑȰқȥΒȶŗ(Ȯ\x80ĕĪƘŞтҿɘίѡǾɩmϼПɇѵˢ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻǅȟȞǠȭӦόťˀѦĳȹδϢԉ\x83єȿ\x86ɽĆ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϠÓԐĞʫnѴπӝǶahκø˥/ѡԤŅț\x99ҽѳĿ˻ʝΛɘYӧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɁԫӳƔҫƹĀθɤƥБśїǇ1',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͶEРÜwʐ\x86Ģνωȡʁ_ΐ˽ɏjŮTΔʀѧΥZpкΑžǩđ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '^ġ\u038bɁ\x8dω˶èǞĞŉ`ЦȍŮĀǀΰáŅţTɫƐǈˑɇʯЄη',
                            'message': 'ȚǻǶѯѬ{ȥ˵ŬɭÓǤŜѽϫԨЊ˂˝øϜҋԔлÏˢγʥОǹ',
                            'arguments': [
                                        {
                                                        'name': 'ϰĠ{\x9dοХĘĐƟǢ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӍϠԒŤУѨɶМǍҴʓŠϮǊѠíԏɠ˘®ğʑТğƀϋą\x99æԆ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 277493.5002887443,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԚϦ˴ӌĻʷŞȑ}ɚӻ˝ǵůƹɓ\x8dȀnҊύʃͻȴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƪzӕԄϬːʵЕġèϺҀȆƣƪѕɹb',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԛŢ˗',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 835652.3192391028,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӬȃɎΘԙǒʝѓʔ\x9bΡęSϨžæ\x96ӛûψҙѣɍˬӲʔȉ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Пρɼԃïʁя',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϢŦǺɓԇг˾ǮРĲ)ӖâĉʗѤǻ\u0382ԝӛĪʼ˴ѥρŹʂԅʂʑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƏǺɍѕ\x81ƛɟͶɝɩϫԥʡơēϕŌзҞʔÜȚ˙ɃҿГѵÿ·Ӿ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҟƛˡ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԁξ4Ϧǌą',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.947784:+0000',
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

            'name': '·\u0381Ί',

            'error': {
                'identifier': 'ȚтҳХȮ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'Ɍӧ',
                            'message': 'и',
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
            'name': '·ѷɕХζ}Ž˂ȎФïҊʊɶʳāƻµ$Ƞ\x8d¸Ś\u038dСЁΒê\x8f\x8c',
            'version': [
                -3729500791515913868,
                -2622251636749428089,
                -4891089681031756704,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x83Ôϡ',

            'version': [
                -1298858672245608230,
                -3318598819903459003,
                -8747899904364652100,
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
            'event_id': 'ӡ£ŧ\u0378śҩVʈӦˑ?Ԉɮ\x8eǒ;ѬÀíɰӐԦǪƨЖӮöε\x9dȤ',
            'target_id': 'ʌ\\ŘÅԙЪÎĉϤ9zʃǹʶ$$åѹѽȊоӱŒ(РăϑHәÌ',
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
                    'event_id': 'ѦĎÝԠνΡӑБǞʨĉǟʲɝӂȟϿϾȣͶϹђ˶˯ҋȆʃҝôǟ',
                    'target_id': 'ȈѓťӜę\x88˕͵Ąӫưǁɖ;\x95ʸɪʮΠˢԧĴǍ҅ΆɳƇѻǼp',
                },
                {
                    'event_id': 'ˆĵԆ°ƽʟ¦\xadɋü\xadί҇ͰνύçʑӠćƴƚȥƐ±ʘєҟ©ơ',
                    'target_id': 'ЇďȵĜŨϡaɐӪ+Ƀӻ¤,ϾhˁϾǝ¢вɗǷįҡɃŅÙӹǀ',
                },
                {
                    'event_id': 'ȣsЧςůǇϱϮÂ˫Ӱ϶\x81τ\x9fԃȠºΠȍȽʪŀϲѷ\x9dǌ»ǃ\xa0',
                    'target_id': 'ʓţƬ^ӌГҮYӠɧҒ9ƏΑɋ\x9bԏ\x81ȉGΤϡ\x9eTɁӑƚ¸\x92Ґ',
                },
                {
                    'event_id': 'ĂÎĿʶèбå\x9eµ¼҅оəĝЌȲǸťæʗЈ˕ɗνĚĞťљɾҚ',
                    'target_id': 'Ŧ\x9dĒǅơ)ːҙÚЖǆħϿƯΨǠӇюȄдɲz˕ɫ\x9cëȠēɪɞ',
                },
                {
                    'event_id': 'ғ\xadʯӓ\x87ķёˮ4ϸцэ\x82ѡɕϟ²΅ȯʳ˝íёÄɾԆԝĔϿF',
                    'target_id': 'ÖҟǳɺѩǼϰҜ˶σ7Ɂȱ¿ʐϷͺżќӰĎҽӢt´Ҏʌſɂе',
                },
                {
                    'event_id': '˻ҙҕӓҵυΉǐō\x8fŨũϢÈȡΜͳѹ\x94ˈўśгĸƤòλͰȷË',
                    'target_id': 'ƈƼĈ·ϊˡΐSӐ˜rϰͶχǨƞ\x98ǢƽԖϞˋć·ϘÉӂϊӀħ',
                },
                {
                    'event_id': 'ȑȲϓéĘґȳ¡Ǚ\u0382ӊ=΅иԈѾə:϶˝Vƾǅϋћҽªҋʨʡ',
                    'target_id': 'Зʂԑˤǈͱ¢ɩǥĿЍςÛìԐЗΤɝÅҗӔʭmÄРǀŕ˄\x82Ȍ',
                },
                {
                    'event_id': 'ҨӶĴ}νăǃщ˖ˤάЇˢɾѰĢіԮŪӱɳνxϠǣσџɽϦɏ',
                    'target_id': 'ΚВӻӸѳЌø\u0383ʓ˦ЯϕʠȚоƐӮɨʫʒŚάƅ\x83ϰɻҞƳɐӈ',
                },
                {
                    'event_id': 'ǾƊțѶҪΈӇƶѡϻСӿɳ\x92ɮȯŔԞèɾξ҂˱ͿЍɩƢнƇΔ',
                    'target_id': 'ƕΩŜѵЁ',
                },
                {
                    'event_id': '`ɮ\x86m©ĬϜ\x81Ǫл,ņφɤŉ&ǑΨ϶ЎǩΛÇЀˊӍĨϏ"Υ',
                    'target_id': 'ǝϲўӆҮѻҿ˯ԉɷϋÈ}ѺӔƦϖˈЈȀˇєҪņғɫ£ɬöԆ',
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
                    'event_id': 'ðȊ҃δȧϛџә¢ɱ~҅ďё»ѡŎȒşȁВ϶άЏΚͳԙҴŏȣ',
                    'target_id': 'ɲˡ2ӔϾʷ;ɤчΆԥɁėĽ-ьȆΒȰŵėлҠŰťȽͻԄȱ\u0378',
                },
                {
                    'event_id': 'TʩҰӋΈԇѾƠӦȝďʪӒɺìǍ3',
                    'target_id': 'еʘM¼˞\x9fˋҲǫɕ΅ǊĪеɿѦƳѬſҰӬɃƥǇҭѯԓӯӾȽ',
                },
                {
                    'event_id': '=ȉԮĨϭˁÖȃσΌљȣ}ĤҗŚgϲāǿІк¸½йǈfǘȻ9',
                    'target_id': '7ԖʔɄқ±ӔŸ\x8aǵŮȲ˸ʶƎìƶƠǸԧӐӬÃɑƓMˀѢȄÒ',
                },
                {
                    'event_id': 'жǿǗΝҴʌ}ԋΚʕēœ¸ŕɲΜɳ1Ƈӯ¸\u0380ȸѷːǓȃmĥǸ',
                    'target_id': 'ҬϒȄƷʢķɲɃӔˣƴϣʎǙԍϺПʨÀǔȕαǇĥėωĎČԦɊ',
                },
                {
                    'event_id': 'ǣUÍˑˣ¬ʋ\x8cĮɞ*ȉчΜТĮЀŖФӐτϸͽҋȹɻӝáͷΝ',
                    'target_id': 'ʗdʚzʦ˱Ʌ.ϼ˰σԈЭКΌƉӽʲȟ`¶ƇѵBώƏ¾ʇҽƴ',
                },
                {
                    'event_id': "Ӫљȷƛ>ĳþѭŏ҈õԀǘ'Ѩ¯EњBşþѱǘϏ˗Κ©оҴ˞",
                    'target_id': 'ʣίӆʄȈΌӬ\x90·ǰшăҥ.ĮļSĖ˄ȜƫԭѸËθƁѴʊӁE',
                },
                {
                    'event_id': 'ŉvƟ\x8cԅѕī!ԊДҲɓļǧ1ϪŽ˦ҟЙ˺ǳİõқΞǫΫĿʧ',
                    'target_id': 'υ»ӰȻȚĘ·Æ%ѽωΊҐǿÎјɂȀӭĢ\u03a2ŸΊʡԗöĞшяƋ',
                },
                {
                    'event_id': '§?УµĘΘžʦeҹҪiǽʹñɽҀ\x87ёžҼˇCéŤД\xa0ҏ˽Ψ',
                    'target_id': '¥ѓɿЩÝȬ\u03a2ǤјŢǍ҈ѼҧÓʡѣȌeɞӨΜø\x82ԋɀˍĝϼƊ',
                },
                {
                    'event_id': '˫šĺКʫћŧʜпǉ˘ơ\u038dҌǨ˼ƴϒ;ӼÏϬӞÊʡѿϨӔѧư',
                    'target_id': 'ǬΎɚ\x8fżʖчԇǡөʌ-ɗˤδу\x83ѡ҉ï8\u0380ɞÈηԠȀШøѪ',
                },
                {
                    'event_id': '~ǉΈɆÍȨƣ¸θȰɟơǏӽɋd%ƃʓ˰ҾЎ϶ʴΘǇţǨƁʶ',
                    'target_id': '\x8bԒœłvĠτЏȖԚĈԟȬԚѢ\x81ā|ǉԋǆѱϡɨȺ8ϩһСĜ',
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
            'name': 'ƧӴʟȌζ@\x7fңɈӖϴāě)ͷʷɕ˰Ŧơ³ʸɢȄÇϨΠШb',
            'version': [
                -6482885519771174318,
                -8561122840908292370,
                -5977901106247476622,
            ],
            'about': 'ύƟ˴OÓǕѡϿȢʘɵŦȒƞĽҗΜ·РĔӠÆΏҜɻñӽʂӭȟ',
            'description': 'ʋʞԪ\x8eaр\x8fӑчԫÃѥķ\x96˺ƸǻӁҁӑ|ͽ\x97\x92ÍāĈ¹Ӯӏ',
            'authors': [
                '\x85ȚαæθѰҪĹǎ$čҺϭGѤRĩǦĉÀ|łŌʭά\u038bʼŤΗʻ',
                'żƪµɨпɨ³ϳĄӔǴȑ˅5ȗнȤΉӍԇӮ\xa0sŌÊJǱ\x82ǡí',
                'ϷІϗԐͻôʧƄӹĻǹĄЦ˼цȉǍđȜŒʲɊʁˋʈÀЁʅȥƤ',
                '\x95ºê\x7fŦőǜ¶ʿϡƞŕͼYЮÛл͵Ĝ˟ɋӿȑђ·ԉЃ+ɎƆ',
                'Ξɮ\x9dԬýϘѥȤҘÁǾӑʑɝ(ǜѥΡЭиӆĹҗɇ',
                'Ʉ\x92ŗЛƹǢˣκΩʯ˼ƺO\x81ǖͶ«ɶԪ%ČҶѿҋŒãȈőбű',
                'ɇӁĶҭȷɳǥʠәЀʲʷĞϖ¥ƕɬ˫ʇʢρңʠΑƳƯh˽įǤ',
                'ȖɠπǻġŶό\u03a2ĺªɧĪ\x9b˩ϾЏÅӋNη\u0378}ɋΥПŒˤŘѰҎ',
                '˚ʕɆŐɗ˱ɲˌХɄđWүƀή\x9dǟƌʯ˒èө^ɹ\x8dĨìțҬţ',
                'јɅȺ\x9bǀɽҷˋʣΜӣŊԟİҬƎʤɦһʪҐҮėЭ%éДσƞɣ',
            ],
            'licenses': [
                'ʖόӟШĊϭ«Үҫŉη҂гȟӬȥŤŭˏӥ˓ʫӯтXſф҉ýз',
                'ʣƩλ_ìѢĹОşŷϔϞAΕѭͼҪϮʰǧӏɓbҿΛʰd«Ɓ/',
                'ùƠ\x90;~ʀ*ÙɻƃТԋWӾҷǇӋͺύȁҿÁєѵƏ\x8fнʀźǋ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ѝyѱ',

            'version': [
                -3875754386703486349,
                -2919744524912849709,
                -6502834706268181781,
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
                    'name': 'ϐǘ҂φȘƥǭ˦ƷхӍʆɸŪĀЎʄЭӅ˛ïɢĊǪϰєʿ\x96ŸƠ',
                    'version': [
                            -4923391880050292999,
                            -8145030800320641153,
                            -2195358985271715744,
                        ],
                    'about': 'sԧʍ/ӽˮôӟ\xadǩҲǕǫ7ƯäȕƎӒĩ`āӯȠŢЏ^ΘƁ¡',
                    'description': 'ʋКӏʎ¼ӻÙǦ¾Ό҇ŻӣͶ˳ӀƦȬлŌԚВѨпҟα3҉ʶʄ',
                    'authors': [
                            'Ҫʒϟȭȑγ˫ɍӔΟĴȏѶ$ƎεңªԖ˦ŌΕǞM7ӬҍǄϖ\x9e',
                            'ӶWϓ\u0378ʦѓuϧ\u0378͵ªѬćȏ\x95ȄӦɇ˦Ɔ˻bѵМ\x82ɱǫ\x9bˣҠ',
                            'ƔɹȵъƀȤ˴ΌɊϫΡȠǄː˘ΟĽŷѡƟˌ˫Χ©',
                            'Lëɽ8лǔǮ˙Ê˜áҰҿĮ¾Ӫʳ¸Ԡ_˻ķūѱӿ΅ǩϡήʥ',
                            'һԓ\x8bȋǳõϳ\x90ľѼ˔´ΟƮm_μҗƨĪŒĭɁӸѕԚƃõӺƢ',
                            'ԆφǦҊӰғ˱ğ§&ȝΣʭ¨RŌӀǴҩњΧԃӢȁǓΞԊ˘ҍю',
                            'ΔҠÆĎżГŜӞǔȤiӐϙЛŬˉИјɠȠȈQ˲åӗǥͷ¬˓Ϝ',
                            'ņǌĄȗȬĮʱɱÑfӚɬʳ~ϰƘҶˡƜƨ#\x89ԢǕ®\x85ӔѼӾǐ',
                            'Čźʚ/ȽɄӄʥҞĸλӓVѝͱíҍėԗ\x82ȤΎɾĉűϑҲǶƹĂ',
                            'ѨVƷ\x8bİ[CУȔɔʒʘ\x9fɻѺúԩˀ~Ѭ^Ϙ^ÜEʞşΞǠ\x86',
                        ],
                    'licenses': [
                            '҄р¢ǧȂȶ-ǒĳˁΧóȝ7ӻ͵ӘпɸǻѭȁȋŌȍ\x8dѯЩĂԖ',
                            'ƭ\x85ľʝӜɑɳ¾ϕ˽τ˼ƅМ%ΒƱñʍŞЯ[ƞʴӞԝб\x9eӻэ',
                            'wŠɬʖ҆ŏϥĳƃƬѢfǢȝȜʽǿЌίԫ]àͷ\x91ɿβɻёϐċ',
                            'Îɕōɫӱϟлć˔ŌʈԊUΥƍʗ˦ň¸ľě\x9cϠҫΤŖѨӐǉ?',
                            'ɵɎŇ\u0380ОҐ\x8fʋҔϨ\x96tĪ˅ʚ\x8b|ϧψиЌҿΕǢÌӍS:Ȓʋ',
                        ],
                },
                {
                    'name': 'ɐǗωşüнÚӦӬƛʁdʏÌɸKГÍԁɐʺѶõШҍԅƘ$!ɏ',
                    'version': [
                            -5300568021201352830,
                            -6544422274100761343,
                            -8835145145113929340,
                        ],
                    'about': 'ԫǒιǖǊ³ÀǀϐƺɟƼдӃXǓȭӸҗφƊГԦ\x9b\x8fϹǖĎԦł',
                    'description': 'ɯŘфĕĉ\x90ã˵ϖŗ˂ӬԂѢåԡԇʽ\x9e¥ÐЄǐhtʀмˑīͽ',
                    'authors': [
                            'ʓԌΝҾČӁԆLɥЁȣŹӈԑ\x7fȦȼ2w)ˏΖ҂ƞΚĲʞÖ˂4',
                            'ǠԆƋѸΏˉ\\ҀʞżѷÇӁ',
                            'ұŎȺșҰ͵ņӪрɴ˘ĒϼəӰӣZ\x97ѥ÷˔ıш}Þ˕hҹҊƧ',
                            'ҥĸϝđƎÅ˙\u0378óHíŤɸѵÕțʵӝϭ˶ϻ҄ÝÏҪƛoұԠѐ',
                            'ƅǼɓʌгȰнǁɊҭЛČ˄ÛǛȤǴǕҵ4ʧÙƼɐɌ7ȵ\x9cʹϨ',
                            'ԔŴĴņǭ˺\x84ʊȅKɥϡΖԌ¥cDơǶǢӹʀҡЁҬ˓ȸϳӥΓ',
                            '\x8fćϬμпɭɚȺԓҮЗσɄϬҺЌÄĢŇЗȯƪùɂżēӧӃОÔ',
                            'Ȭǽȅ1æЗ˔ӷŝҢôĉŒȮØ8\x99ĠЕϬˏˇӌӜ\x83јҮȃΗє',
                            'ǝϔϒ˻νq϶ȊɼϫʪʣɽÓԬNʻɽÚɰ[ҸҹҸǕѦ',
                            '˦ζѳǸʩˍʱΜȓǭȵ¢ŪӰŲ2δƾҁɱΤǩïɅТВԤþˋԔ',
                        ],
                    'licenses': [
                            'ȕȪˋŚҫµ\x91ȱ\x88ȲƹͿн˾Ƽ·ϱӁ)ǴōϏ\x8eЬ˹ӥӇ\x7fҖł',
                            '˳Ȱ÷gʶѡǉæčəſӱȣɉуšϜȫ\u0379ÈɡџИʔƾЃҎśМ\x94',
                            '×ĩӑԞԪͳШåͳųЁνęҎ\x9bʓΌӎÃɺЀȱБњʞºĿɥƬħ',
                            'ȣлм',
                            '͵Жǁǽºѩĕëɂ˨\\ԈˆϓːʫӽǓɽūсμϭò˅˘ĔНɸŶ',
                        ],
                },
                {
                    'name': 'Ϫ{ҚԊѭνŮ҃ŘʄҼʙ¾ȘԤǵ(ʮϷǦъԓӬ½ζѪŕӽƾЧ',
                    'version': [
                            -8786488015370283184,
                            -2406589241445387655,
                            -8417555290484319427,
                        ],
                    'about': 'ǏͿƝʆɖȲ<њʝʿ¤»Ã»рӉ¹ѸƍΗШƠҁÒţdӫҩҿǼ',
                    'description': 'ϱʒZāԐÍ˞ȐͿâǙԨЪɘИƌ\x91Ɵҕũċѣ+ғГʰȢԐҸҠ',
                    'authors': [
                            'ѭΟ"ǳ_˜Ľ\u03a2ȃԆ;ǩμӻĊƮРƿѴȿӠθFӜňˤʮ\x86ɻ˳',
                            'ҞùΔXԫɝ|ӨˣʋƎƌúɶ«ʕϱ˧ԞǵҠÛĢɻ˕хȣѴӆĲ',
                            'ʜ҉Ѱ҃ƉƞśË\x9bВʬʾΖǝϘƚƊɇͼ8ľɒáƥҹϙȺĆѬš',
                        ],
                    'licenses': [
                            'ѝAГɂЃФΚŁϬҔľːƻӵρΙǏìǨѣț>ǆȽԏAӢӵξƓ',
                            'ѵ\\Ǹ˦ѮҙԦčÞΩσͲÛҴņԐ)ȎҷŇwѯƕЊ',
                            '¯ūԁњĊƩʕƘԏnЄOѵƓɗïώʼцϟϺˉƨӼʥӍѨΈ˄Ѳ',
                            'ȒǓȇĞșʶȂƙÏ΄ƌȿόηӉӚψԍʍÉʸgŻϭЛgϠǓǜˈ',
                            'ȱɻ?ϲéʜѧɼļіӦԞяΙѠӮȨŲѲÎԁ%Ѩ˧Ъʛπлһƹ',
                            'ȌзɪӛȼÐ\x81ΒЌϰ+ȆΔȘ¤Ќȸε6ζíӞѻ¸ȄѮ\x85Ǆƨ˷',
                            'śГĚkċĵǢдҼĝeРʞÜƷáƄђĞc\xadυʎʭϸʿћ˃ȑș',
                        ],
                },
                {
                    'name': 'рҩо$ӦĥѾˈbƁςΣͰɪ͵ǚǯǖРȒƺӭɵħɳŝРʴӏz',
                    'version': [
                            -6015910705161052757,
                            -7436216889794362540,
                            -9007148326363325030,
                        ],
                    'about': "(śX'ԩѶеˋ;Ԫ\x92ȢԁÝǺʅў\x9fďdћηҼԜƞȇNǲ\x98Ћ",
                    'description': 'nˌ·Ӯj\x95ǄħŭΎƗзѢҺŧȑβɍ1īüɎ\u0378ԋΔˬõәĴÓ',
                    'authors': [
                            'ҠÃǹʇԭԘϔϿ˩w÷Ƣ[/Ҵ}қҲDnǫӤΡƮʣψӜͶƸӓ',
                            'ŀĻԅҋΫ\u0383ƾ˚\x9eɻÓ\x90ʌЫВ˘пͻӑ\u038dǸˠЯeԪķΓГΖŨ',
                            'Ӌ·ϹɋÊvŅ×ȃKЄ+ԍ1vºÿіŒɐȝǷ˘ǓрϬʌ`Ԥŭ',
                            'ҨӲȞΈĉǌӑЇƠӋѪȀӟǎÁҔ΅\x8eńĵÞʶȽȡΆЏŋԩuƖ',
                            'ΐȐɋɎɘȥӪʍԝǰϨŬÚ\u038dΌ\x90ωԌƏuΕ+ʅӏɅɛɽĳԘϱ',
                            'Ʀşɹϻʯ$Ǧɼϸȅ5"p\x8aąŋӠĔӴȊ:řşǨŚȼģéҼȆ',
                            '˸nё_ϕΛ;Η\x98Þҗф˔ȇȺĒÓɤǎÏó1ƁηӐӛüϊˢϥ',
                            'Ǘ+҆˚ї§Ыɻ˻ɲͰŉȳǳϊ§Ѓ[ˆҽϿУҳӴˀӌƹɛȚҹ',
                            'ǳ',
                            'ǡƱ˙˼ǨƨҏХȪȾX˶δѓʰԣƧơΆ\u03a2кθҥԑӎ«ДģΤò',
                        ],
                    'licenses': [
                            'ΑςȓҲɋ~\u0380ҰâǵȯйƫЅџѕƝ҇ƓдνŒй3êɺƇаɴӰ',
                            'ϗұț³ȕ\x92ˢΜȉɿΩØȩԥЖžнĴǂԠҨǳÞǑnƪˍʀӨȽ',
                        ],
                },
                {
                    'name': 'ͽӧԝdԟҭзȫōěзԋȡwаǮ˲ѿҠ\x7fſńœΫʃʄӚȗŪԔ',
                    'version': [
                            -8733504431783232658,
                            -6771857698496659433,
                            -7593016444802304158,
                        ],
                    'about': 'ЪƽDȢɪɠάɗ9ľÿȬʊǲφѕ˞¯\x9aÜʬі4Ԩy\x9a҂ˮΉʗ',
                    'description': "ɜæʐҙç'ǄƩΡԙʐȉɉфHˌЊʔшЁȇɲԠмÂǊϽƛŹǐ",
                    'authors': [
                            'ȭэõӚ\x95þćȿŰ\u038dȯ0Ǝǯ',
                            '˜ʌ¾Н',
                            'ĝ˻ƅàͼԩьâњЗ`ϳȦşϹҜĖɸˠˇŴÅȭ\x94ǎ@ӇŠȩѓ',
                            '¼˺ƶǽɳőÝҠ҃ϺȍχΑԖφçɆҥĚЃЗͺΫѲľÊпҔȖȭ',
                            '[ϟ͵ˡȕшҸԕΎĬ\x94ŉϧŀï"͵ѵңǚĘˎХЮҶ\x90¦Ӡńo',
                            'Ԟ\x92GTʸЫȌ\x97ҲҟЬϚʓ\x98ĥˮ~ΕuЭĘνԃƘŠϙԥƝTž',
                            'ϩƚȚϞĭЖҭОԗŏТӴϟ:ɲɛ˶:ÓʭτπƠԓÒʐҡ/ѲL',
                            'ӍОSҫǹńβ$ǂȞȏɎʲȖ×?īψE®ΎѺФMʫɫʹǳˢұ',
                        ],
                    'licenses': [
                            'ӇњňÉƟä`Ë³қΤԄáýУςѿĵp\x95ˬʐΣǵþʘ½Σu!',
                            'ŲӕʜЏʰѐːӂƚǸЩƪQÜÓɎĩ˜κçtˉӟԢъѿΈɰĎɸ',
                            '©ҴµǴЭѧ&ųɭԛʪ=¼ϫӱ\x96ȣǾӲƦϪÄ\x8aɡ\u038bԑ˄ԣъú',
                            'ԍрԟѾɤǳ\x80ĔͳίǔӼЀǬzǒɖчԁβΈ˔ϼ<ſƭØдԇГ',
                            "џԂ˫ïЭЦ΅îʤǽ'ΡƙΏ¤ɚŲӖԚƥД\x9aɫӋѣ\x8a˻1ɬM",
                            'жбΫϫnɰƸǸȔþѝ\u038dǖǁшέĠˬÄѧЦư˨ѵˆʷƥȽӆé',
                        ],
                },
                {
                    'name': 'ȉƣɊԣ\x84ˣӴϸπ΅ϒϸуǾũϴҥПªƟ҆OˬɉrѾѮӾӑř',
                    'version': [
                            -5428111384743151571,
                            -1204263793361164967,
                            -2645036888075741814,
                        ],
                    'about': 'ʾɠ΅ŽL˂ƈɄèϵϜŌǾϻpƨÖwϼŮ¤șѣрʽзŏ\x9c҃Д',
                    'description': 'ŝĚЕɒǴ\x9fИȅŃǎ;ϙΐ\x97ɟɤЋ\x90SȎǷʱû1ɿţ\x81\u0382цӿ',
                    'authors': [
                            'мɽǞı',
                            'ȝŭӮƦΤϦϱʹɡ\x870¥Ŏԏ˗ůyӧƕƬáНӵҏ˩ѥѥЮƵĻ',
                            '\x82şĩƽčϔȿΣВħӽӳ&яҧɲ`WлâѵɱԘÓWϊӇ҃Ƀί',
                            'θȥƵҔƒϕǜӛƭĚΥ\x8bɓӍĖ¶ÒњĞԓьҾ¯ƢΑĜˀЊ«ʁ',
                            '˵È\x87ԍӄň_ƐĶʺӽ\x8cԠ\x9c6ȎƆŸфШʬϾɹ҂[ϺłǪĳγ',
                            'Ӄ҉Ĩƛ\u0379ҪƧ˦ԨɓҧǭϵƥÏ¸pɠbȆƶsƸǩˁǴɔŌěѕ',
                            'їůλԀӢĐ%;щψϣnо҃ЎǥѵӧđȜϥӼ;ӛԞȹq˹\x90Ŕ',
                            'źϤǧ\x88ͷǎϣϰ\x9fŢθÃϪƈ«ăȓ˜ù\x93Я҉Έ\x90Әș˼\x8b˲ɠ',
                            'ѮƝʕĔɨӭӞѪȣɁϛ˩ҝɍɊ7ǻ1˂ЅǮИѵǃƅˏς˩#ћ',
                            'ΙϓБԜƵ\x9dßIģƌυqŅɗӘͼˇĬʃɶҐ˂ѵ˒˻ʢqԭʔ¹',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': '\x80ƧɾѓΒшʴвуāÐԬϛǩǪΛϿC˓ѡęDȓҬÐɅ\u0380ţ˨Ě',
                    'version': [
                            -2223108684081907847,
                            -3054720091354162683,
                            -3341242046430919272,
                        ],
                    'about': 'ɴӯǧʙЗʶɸбЏԈNЧΞӀɢ˳ȌОсрĎѲďƞ˼ÉɟƵΩў',
                    'description': '\x91ϣ¢ǔäϕ˃ͽØŏӁтġǂƵɂ˛οӰǘɳΏHл˯Ԟ\u0381\x99Ҟɥ',
                    'authors': [
                            'ҤιԍĦҵʌӌͽĩӈϛɰƛȡΔÎԘ¯Μ˪ȇɱΥԙrϐҾҜƪ?',
                            'ҶǓÈʒÑŰѴǻϊƌӹ@¯ÌAʀїӧǯѾ\x8bі2ϳѝǋυȫюϰ',
                            ')ˍH\u0383ǖҡǽľИͷɓȡԣФΜОϚǔʠß?ôđӡ\x99ІуǲЙǗ',
                            'Ƒ¢ń\x87ɷǄДϡΡĘ[Ǧ¹ѰſӬƪˤʓѩÔԩ;јʭʹσˆ˜ώ',
                            'áʛĨvͰϦdɎҮиӐǰ˜ʞǠxϟ\u03a2\x90ĠŀÿӑSʅÓ\u038bāǱŌ',
                            'ћʋŌáѠΏΟ§ĸҡĴƹȊȌ\x93Ơ',
                            'ƀϑȏ҉пźяƭæ˹ЛǼłү˙Ə\x93«ʡȀ·ȭϑҰ҂ˤΧʯòȧ',
                            '҅ȗƪВӤҥƷӻǯȣǷŐ$тOʥЈ?ēǼ˘ԉɵīЉʋƕɃҐƵ',
                            'Ƞȇo\x81ʋѡʄŞ\x89ҎƒўһGϿʴȟζÎӐɢ˱1IӫÏҷѹȮҟ',
                            'Ԧ|ɼńȦÆȣІ˓ӉħſЋΛǽʤӷʁ',
                        ],
                    'licenses': [
                            'Ř\u0379˯åǃƌΔЕŞlǥñΜʾĕˀуҎԌŵԈǂɮÀӯˡШжƱŠ',
                        ],
                },
                {
                    'name': '˞Ύϩѿʾəιǎ7~ʓȉåĶĄɪӔ\x9cřǴŢμ҇Ҝǘ\x9fȄғЏϼ',
                    'version': [
                            -3490228714428315793,
                            -5278884334806642748,
                            -4907645412320754486,
                        ],
                    'about': 'ҷ²ʔZʪ˔Ѧ°ÂĘԠ6ĳĬǖǭҨűϑʪȬȕϖV5\x86єǐ˸Ŭ',
                    'description': 'уԪϫӕ\xa0¼ȵцҸ˟ȅ\x80йѿѾвɦ҇˜ʛ¶Έ¯Ӹ˴Ѫ÷ȳһЇ',
                    'authors': [
                            'ѕӁɄϜҡɥɅϷϷϧǈŝ\x9f\x82ɤʿҗ¾ˊЧσǀɺăȑƅԋ²ѰΠ',
                            'ĢҗŝԘrȺԢѾЌϻīʩϒʄӬ\x7fӭвώҏ\x84ÐƚũƗŨǰїѤɀ',
                            '´ȼԩΓíɚƚÂȲɰƊцѝÀĊφҀѯʯѵϑe˻Ӆ˂үЉ\x90ӳƥ',
                            'ƤЫǠҨɃƶƤαmƒʱ=ƓйgҡŜɖҵԗЧǒĐ±ӰˋφƩβɠ',
                            'оˠWÖΎѐӂҕΩÃѼ˟ĳҩ\x93ɩȵΎ˕ȷ˖ΖӘ˩ÅɪѲSFӧ',
                            'ɋǞөΪʹέʶèϠˈέΚҰǪͳƅ҆\u0383ϫěЫҊˑΦDԦ҉ӣOΖ',
                            "ǻÙ҈Ҟµǅǈ'ͲbҌӕ%ħйЖѝ\x82ԪƯ5ӍǋʡͰƴΡîǋΒ",
                            'ϠĺϊŭԘϛŒɶƸӡſĜU˕ĘĊџ˺ІȘǟӘНˠõǗǐȯȽ\x80',
                            'ƃʗЀ˦ˌҮøңŌӉĲ\x91˨ȄǇɅȚБ@ѯɥϒʘɃВŹǚэ˦Ҩ',
                            'Һ0ŔƀǡԠȠʽǂјɌƨß»Ӱϴ?^\x8bƅşПϊш¸mo_ŦI',
                        ],
                    'licenses': [
                            'ɀ`Т©ʵѝǽʪԦԏѕ',
                            '4ăĠɎ˦ІƢɲӴîӆƴԡŰƛΛҲвӏʧϮԢ^ƫķуԀ±Φȸ',
                        ],
                },
                {
                    'name': 'Ì¦ɫϸɽώНҤŸʐžŞѼӒʏʲԪӢOēõƿϵѯΨ}Ϙāωƫ',
                    'version': [
                            -6616185788311540195,
                            -1950339208338802551,
                            -41985341608883435,
                        ],
                    'about': 'ǐҲƃĠ\x86ҍƬӸϞΜѳѡʖǍϜРÎӓĲ\x86ӟ\u0383Κ^ÚԦ-϶ԁҧ',
                    'description': '\u0379ӶҚſ¨ːωʾнτҍɏГšß\x8bƠΏаſȞӸ7Ϫʵ\x93ҵǘʖс',
                    'authors': [
                            'ӰҨȮӗƔÏЅˠʹάʖĪɀğӯЦͽk\x8b\x9dϒĪţģXԞӸÄͽ¹',
                            'ŜΏůѶÐΆȌī˖\u0382ȢϛɩǚԁőŻӶˤĹ£ө˼Nƚʳǥ(ķә',
                            'ÌΚѳџΔŏЋ8oȦϡϋĭȄϒȐȽ,ʷЇ¢ҔŸЂÒлԊ˖χԢ',
                            'ɑВŔΖƀʿ\x87Ϭˆ\u0381ƨǩŉΔɀĞӽΘŤǣІęЎ\u0382Ȣѵ}Ȝԥį',
                            'өϯͱ\u0382ˬч¬ӕǮЍͲԇǖưȃÆͽŐPιřҬ¡ӃÒǞȟðʘʿ',
                            'ɠýѳÑНӷɅ;ì,ȱФłʑΆǆ+δҋòˏӾМǃ;С\x94Ζğѯ',
                            'ͽбϻΜԙʳÆϯΡ\\įϨɕŬөȣȤ˭f³ɰҊɹǹƹԙeҏεѡ',
                            'źȈƘjŁȟ\x8fԎ¹ƳÑɿ˒ƕƂǀκªƟŸáÔɢʯӐΓЕČΨԫ',
                            'ĂǡƳѬÌқʾƜϾҧÑѽѱђΜø˧Ҟ\x91ǘ*ˬÃʝУǿϩļ£ĕ',
                            'Ӭƹҫ˂;\x97Бʤɜųȟǝˤђę˲ϼȴξΫɍ\x8cʌ\x8cʶ˹ĀēͲ\x97',
                        ],
                    'licenses': [
                            'ž;ʉѵƿѯƈnʜµġԠб\x85ːϸŽӺʵʛƗţǑšϓИĶëЏљ',
                            'Ʋˏǜ\x92ǲǗťÇԊʖϡȺ\u0382îńυƺҤƨʇТ\x9eͻӛɯ˲θѪщã',
                            'ΘtǎӶϡӏ\x88ԛӜĮÍԫӮΈßòɖөϟɋҠԅÄïѿӍϓǳӀȶ',
                            'ǻɭȱЏǩ}ζŴʖ=ɇİÚԍƸҕ˵ƄѾ¿UԒ\x9f×ȶҪŒϝǺʹ',
                        ],
                },
                {
                    'name': '!ƚЙѷ]ϞʠǉӄӨɸåɗ!őϏʖĖ˟ýȩÍȯԦϰЗϕѩυÙ',
                    'version': [
                            -1639889717975802132,
                            -1164090577244401293,
                            -5662081783987109964,
                        ],
                    'about': 'ќѶtŪ<ǐîǼĳҬƈϢä\u0381ӫ\u03a2ĤԑѣϨАͰħɁЈǎџ}Ǜԇ',
                    'description': 'βӔÛБǻyǌѪǥ¢Ъɨ˶ũʯãȚˣĴ)ϹƴƋӥ\x9b^ǁĻǉý',
                    'authors': [
                            'ѫĮūȸԈIЯҠҋԙĸѯѺľԀҴˋEÊҦˮԐ4ȹ°}ČӮƾ',
                            'ƕ;ʶ´҄ƐŲß˞ԈЗɿӈΪԏʙѿǕÎјнӗϋΘӦą|Áѩˋ',
                            'dɕğéŶ\x91ɿ1ΞәȼϜŞ~ԣÛʼľmµѰȮ˦˱ĜÉґɡѭȉ',
                            'ˍԗҢҀҵ҃ȺԇʣƎӜʛǓҎƪȋňAƒΈȉXQū!ǘɞǗŕ¨',
                        ],
                    'licenses': [
                            'ϜʟθӕИƵΠԥŪĕÆ·ɎԨӂϫͱǏƸżŏÛɃȨХԔχѐ/Ԇ',
                            '³ĘƟʆΏþқӲȚļ^ԮƓÜ§Ƃ\u0379ɲÍ\xadҐǅҼԞƧӁɿµȖɅ',
                            'ӊʉŸԟÔȝЯОѧѿɛчȿNψ!ǽΙ\x9c˖ӧыωƴƵΒʱΤҝG',
                            'ҩИΜεҲžѪƊƶρΤИΗƥ\u0382XәÔ\u0380ϬȅɡЋșǮȷѮӒѴǠ',
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
                    'name': 'Ҙšĉ',
                    'version': [
                            -5034855372129758857,
                            -3729974714620485017,
                            -3476491877386072409,
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
