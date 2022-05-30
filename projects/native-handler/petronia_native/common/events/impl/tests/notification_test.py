# GENERATED CODE - DO NOT MODIFY

"""
Tests for the notification module.
Extension petronia.core.api.native.notification, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import notification


class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.MessageArgumentValue.parse_data(test_data)
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
                res = notification.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ʖɜλçҠŏқͰґʷҒÓˀĹʉɂ°ɀͰфǐ\x91ǭ΅҂ϺÈϡȻǋ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 8078873850042932872,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 675997.865756002,
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
            '$': '20220530:170407.260144:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Ͽ\x92ȇεʱƄĝӟӋăәǂΔ³ӏΩĵҐɣУϰłŨ҂Ψʲƪɪʛ[',
                'вȕʐʤҼϗ½}ϳѾˮδɫ˖ʂӰҹƆǽɑĜ\x9e!ŒǐʥЊίũ˹',
                'άϋӾđǯЖʱ@ȏùķͷÎŴ5Ӥ~Ҝø˟ŉɟƨѱ_wʬ9ïñ',
                '˟ā§ňɷӗЁÅɉʝ\xa0ȵ˃ҤïˀҎOЇ¥ԟȵπǅİӱϥѧӳ\x82',
                'ӓԋ˱űϙЅАԑųқżВ°ĝ˗ʐѻИ\x8f\u03a2ƫӏӽιΔʣɫҫϒȖ',
                '\u0383ҏȟ\x8fˀƘkƚȘlЛʉɡŵ҄ÉǞđǖªѩ;ÈΎ9ʕϖȪȱƍ',
                '\x88џÐɡˈԈMԖɑӀҺȎқʓĆӻ¨\x89ȿɺ#ġϗΝȪԐʉΝɨŜ',
                'ш\u0378ſŃÄíхˈRҳҒӕÝ!҃ЪƕɢԓԈλ¨ϚˊȤxǨҭµх',
                'M:Ȑ҉ҨºőӫƲСҎљ҆ȀǾӿƩư҈ĬȤԅȨÉЭҊҋАп\x8b',
                'ø,ǱȉϙƒΦԕɾȓ\x8eӎҶΝѯǜĲǗѡùƥÆŅçʋ$)ƐŵЫ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                1742537745302188130,
                -2113916764931911335,
                -5127572497667467424,
                1211976533069830772,
                -5637935426908893036,
                7013912358590533811,
                -2889628143803166639,
                -936314252988075945,
                -7159863698009745846,
                8674488298006935876,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                428020.59625909827,
                24635.142734760433,
                287324.95145237463,
                856216.7057974539,
                478062.6656749492,
                903831.5333743049,
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
                False,
                True,
                False,
                False,
                True,
                False,
                True,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20220530:170407.264649:+0000',
                '20220530:170407.264736:+0000',
                '20220530:170407.264820:+0000',
                '20220530:170407.264903:+0000',
                '20220530:170407.264986:+0000',
                '20220530:170407.265068:+0000',
                '20220530:170407.265151:+0000',
                '20220530:170407.265233:+0000',
                '20220530:170407.265321:+0000',
                '20220530:170407.265404:+0000',
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
                res = notification.MessageArgument.parse_data(test_data)
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
                res = notification.MessageArgument.parse_data(test_data)
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
            'name': 'ƪȉͽĆ]ǑǠ\u0379ЗǖҍÕӆëҊÕԎϵęзˑbЕѮϫ\x7f˾Fłʧ',
            'value': {
                '^': 'bool',
                '$': False,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '҃',

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
                res = notification.LocalizableMessage.parse_data(test_data)
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
                res = notification.LocalizableMessage.parse_data(test_data)
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
            'catalog': '?ɦʲȮȹƩ.¡Hи˛ÖŇ\u038bɌǟƄϑӜŧʭѯŋόϘaʂ˯˾Ϛ',
            'message': 'ʵАˡ\\ˆĈЋ҅Ǔіǀ:ЖgʁưҡМpіɌ¢ԧųͼҒ®Iŗɍ',
            'arguments': [
                {
                    'name': 'ϺѾüӪҚǸƶ',
                    'value': {
                            '^': 'int',
                            '$': 7403214016358156917,
                        },
                },
                {
                    'name': 'őԁ<ˍƬǥŁĘƺʢϯƉ˂Ԯ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        696942.6916483442,
                                        227575.5448609647,
                                        480366.3262717234,
                                        526117.1409438673,
                                        909160.3173837982,
                                        181475.8156350518,
                                        569845.4021184293,
                                        791449.3092702675,
                                        242887.39232102426,
                                        145470.80999741764,
                                    ],
                        },
                },
                {
                    'name': 'ΧȀˎ\x80ȻL7ϷǬĢϾ\x9aˣɟԩʞŎˎ=ϐá^УӵŘˊ¥ȻßƦ',
                    'value': {
                            '^': 'string',
                            '$': 'Ùƶʧȹ°¦˩ҟ2йԉΡŸþgĺ˾ψȍʤƎϸѾǡǄũöңέʖ',
                        },
                },
                {
                    'name': 'Ħ\u03a2ǔмϿԒΐΆ˃ϹрϏƧɎ',
                    'value': {
                            '^': 'float',
                            '$': 370048.40631212556,
                        },
                },
                {
                    'name': 'ǆĠԬԛ\x8eͼ',
                    'value': {
                            '^': 'float',
                            '$': 264252.4247755813,
                        },
                },
                {
                    'name': 'ɤǄȅϲΌėӞЀYˀмεĉӌġăАӸȃMΏ4ιɑ˃ëĕЮҶȤ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220530:170407.253706:+0000',
                                        '20220530:170407.253789:+0000',
                                        '20220530:170407.253868:+0000',
                                        '20220530:170407.253946:+0000',
                                        '20220530:170407.254023:+0000',
                                        '20220530:170407.254101:+0000',
                                        '20220530:170407.254178:+0000',
                                        '20220530:170407.254255:+0000',
                                        '20220530:170407.254333:+0000',
                                        '20220530:170407.254410:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ѽĺȅӸ\x8eӹѐԖíDėӠΠāŪϲſæ@ѰɍìɍàkӮĲƴСӔ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
                                        True,
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
                    'name': '&ѓѧÖҙ',
                    'value': {
                            '^': 'string',
                            '$': 'т˙0Ζ¬ŬrН¼ΰӓΝϐXĳƪªҕƩnțжʷ˓ŖћǸҫ˺=',
                        },
                },
                {
                    'name': 'ҊΈ\x94ŀѽĤɃǃғ-ȡʜ˰ÎАêϿ¤ΏӵғˎǾ\x8eoƃɑһʄԜ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ͺʬèǐʥŬſĂ\x83ǸɚĔϼԋ6Ƣωρ˷VĽ˅æɒč!˕Ļжț',
                                        'áǼϢВÍABĤȫӒ˔\u0378\x86ҤѢԏŔΙůл\x93Ŋε˸ѯʎͽɰзˆ',
                                        'ԘҊȖųƄЃͲû˝OѲύϨȝоѠЀŠн\x9aаҒҪȭȻȕҭƶȜť',
                                        '\x91D˶\x9fѪɴ´МǃȁӆЭΓʋǃƷҢΦʜƇȀƮ˛²JĹÁԌѕʗ',
                                        'óċļµɣäҸʬďJņϫΡϪҫѺġŁƁυͺхаȪƥů\x9dδ+ʱ',
                                        'Ѓ±ѦϯƷͺƈ2\xadѓӧȟīfЇѰþɒŌʬԂӹϝϸLȯоԝԦӧ',
                                        'þēɀͰï\x95eȬ!˔ʤˇȁͼ˚ΘɀǮ·ǒΝËǿϖӸ\u0379PѥӓƢ',
                                        '÷ɂсŦϗƻÎғҪʕӡƉϿĒӷʱɈŌļġŢȔҭ˅ƿÉĘϳBɭ',
                                        'ɚѲ\x8cďľƢшЯ\x90ʌî҅ҿӘӥ¶ҾȋЉҭӏÉƕĀʐƀɡѷŶá',
                                        '×ŐчɐΔ=эǈȅǬ>ǋԟӤ˺ɻ¹ԂϜŠϻǉ¤ȴіƒˈǥːǯ',
                                    ],
                        },
                },
                {
                    'name': 'ΉҙȽǀŹз·',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ҡѵ',

            'message': 'Ơ',

        },
    ),
]


class NotificationTextCreatedEventTest(unittest.TestCase):
    """
    Tests for NotificationTextCreatedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NOTIFICATION_TEXT_CREATED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationTextCreatedEvent.parse_data(test_data)
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
        for test_name, test_data in NOTIFICATION_TEXT_CREATED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationTextCreatedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NOTIFICATION_TEXT_CREATED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='text', name='NotificationTextCreatedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='title', name='NotificationTextCreatedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='icon_id', name='NotificationTextCreatedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='sound_id', name='NotificationTextCreatedEvent'),
            ),

        ),
    ),

]


NOTIFICATION_TEXT_CREATED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'text': {
                'catalog': 'ͰӊχѺ\x81ӞøЎƧԄӴԞά¶ԭΨ˘\x8cɐl˶ϧġʴˇғNņӫ9',
                'message': 'ƍÞԕȤåˋƶùȺºôǜǅǢ9ΤтѫÞƷȭЃƇΟȒǢɕ˰ȹŨ',
                'arguments': [
                    {
                            'name': 'ή\u0378ʄϼǧ\u0378ϓԘĒĦԍϓѕКӧѬ҆НȍʂӅǯŴ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'дгӣĸǭѱӋѬǙύԎĎђϟǮҜȗϷφPΞћԥĂȟԄƎӢϾ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '\x83ăΜ¬иΈ<JԐȎÓșʋ\x8bǁżаǦƎҔУԄѐƏέǙ͵˄ҥ˜',
                                                        'Ĩ҄Е˴ʀӠĮ.ÔƆRԁϐćɦ˞ÇǫΧĳ¤ԦȽˬ\x7f\x9cѢю8ǰ',
                                                        '\xad\x8dʪԡʰҋԣδǭƴȹʝʤ҆ŹɱɈМϡˍÂǫԃżʑØ=ΪӒ˪',
                                                        '\x8f7żњFȡԐЯԦĮ!ÑиŞҰĀкӅɂпÓŴĲůȿĝÍɜúԢ',
                                                        'ϙ[ūͿΰȡԧʴmґȨƑǚǇ҈¦\x94ҕԣҐҠaӈƒīıфŢĈԓ',
                                                        'LǥæĵǴѳԩϺѿӷ¨ŋɮАϛŪĨūϥҌœɂ,ԮáӾϖӪşg',
                                                        'ʹǥǓ˭Άʬ¾ŪʖҊϔBȌӚÃΗˋι+ǩǆǒʢɅĝЀƇǒʚ˫',
                                                        'ȓúӞȴʶƁMǹҸQӵάМÑ`ɪђОζ\u0382˙ƞǠѓЄ$ϋΨӎȧ',
                                                        "ђ\x89Ҍ˓Њ£ҿϰȼǖ'ɶY=ȂҰǰѠΎ˟\u0381ɭΜɣԟϠʾ)Ѭð",
                                                        '˶νԃɂΈìɊѠƶӖѱáͷ¯ƅƚʨҐɃЧ\x87ɬԂϕÖ¡ə˰ĉҜ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'іʀŢώпѿƢ\u0378ĺĲŐԫǗ6ӄχ\x9bу\x88ĉџɷȡ(яȉǤӒʥу',
                            'value': {
                                        '^': 'float',
                                        '$': 134194.86112829216,
                                    },
                        },
                    {
                            'name': 'ΦƦϟҰąы=έǱƧɠΝDɴз?ϴѻԇΟ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220530:170407.242989:+0000',
                                                        '20220530:170407.243076:+0000',
                                                        '20220530:170407.243153:+0000',
                                                        '20220530:170407.243238:+0000',
                                                        '20220530:170407.243311:+0000',
                                                        '20220530:170407.243385:+0000',
                                                        '20220530:170407.243458:+0000',
                                                        '20220530:170407.243531:+0000',
                                                        '20220530:170407.243603:+0000',
                                                        '20220530:170407.243676:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ϞϥǷϰ×ҪϺǥ,ΥԅǾçǲ\u0381ÜҚǓʸÓƪΚ)ϜȕԖџ˔ʟɳ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ь҈ȡѥĆĮƕ\x93lˢԋʝӯÁõąĊΡѷ÷ԍτ˭АMǢƙŢÞĎ',
                                                        'ȌƳʆ)ǾԏÈůԍԆѮҊΐњGʷɐѫKê?ςĤ˕ȥͱʒʻ6ě',
                                                        '҉ʸȆƼїϮΥɭГӼҿ\\˝ʋϿʖęˊĵvʝ\u03a2ϛЙͿӤԈсϬ˺',
                                                        'bїϞ\x8aøɏѬɯçҙϠɐӥ˧Ĳ˕ȚԩϪ4ȖʹлʀüӃ.ɵ\x86¸',
                                                        'ɝΤӱkˆΐĞ\x82Р҆\u038dɸƤПiАΓ?ÈϵȵХ#Ϲˀѽ:âǙÂ',
                                                        'ŞʩVƹưßɏâïʘRħȵЂƛ\x9dћē%çεġnѸИHɅʓЩŗ',
                                                        'ȭӖΘųϤԎϏАɕӷѵ;ώĞ˵ĖƲã\x94ƹcYβɨЋŊЉťǰИ',
                                                        'ӢɕOԜðƍСɞЈ6÷ƐԫԗηɹoҜùԩğŀɬƬYӡФ϶ӝˀ',
                                                        'Ƙń$ͷʍƬʍFԡӅȦřʉкǒЄԩӟ:ÃŴŲŘúҫŔĚȅðʵ',
                                                        'ŗӖʚɃ\x8bѨ\\δǵёϣǾЄϠ\x92˜тʺȣ\x97ΡҞ\u0379ʭéС)ĎȀ¯',
                                                    ],
                                    },
                        },
                    {
                            'name': '҇ÑѹƇ˶)ĳȆńmҊҊθOĚ˲ÿɹА҇ǚőҿңћӃŚˑϐМ',
                            'value': {
                                        '^': 'float',
                                        '$': 746087.6601455569,
                                    },
                        },
                    {
                            'name': 'ƔЭɣ|ЇżϑЯɺɃс˂ͻǺԝűĩʣăêѣĈҁˇƐΟɧĶόҔ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ˎȵáʡēƎǕʬ\xadˡX\x89ϑЁŻР϶ӚзzсҲĔϦ҅ҋ˧ԙϞɈ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        216576.29184203985,
                                                        856632.2871136972,
                                                        535381.4571452977,
                                                        799710.743424726,
                                                        95605.12935593483,
                                                        118234.0086970466,
                                                        911187.8072279809,
                                                        -40484.83495365242,
                                                        775638.014478602,
                                                        891811.4570749103,
                                                    ],
                                    },
                        },
                    {
                            'name': 'œʷ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ȥʣǴĂāˣӨЎԒώ^ÒŸͶ\x91ЮнԐҤҜϋˇэ\x8cĒĤИ˂Ѡԏ',
                                                        'ӍʲϊŭǍг\x99Ԥ˕\x96ɖμӍƁƞǈʈùVɐʆ}ԆАZȕҏɨʛY',
                                                        'ӻóϋсжŐˈԮԃȖƐɒÂԔҸ˥\x93Ђ\x8dŃ\x99Ȼȋǵ΄9ΨʹԆw',
                                                        'ƛBҫ˽ЈԣʦνӐœƢҝӂԔԎϨŀΌƭʥӂȚΊЦԪůȄίƼȀ',
                                                        'ėŴʢˠŅm\x83\x8eϖЁԍͻ·ɌˎԈԚʬԔǁԛІͽĸ©ƘŴŽƆʼ',
                                                        'уеʁʶҿϹƨÔДaԝƢ\x9b\x8fțêʘ˖˄љɟ_ɻѩȇʖϟ\x95жÿ',
                                                        'EDΪȒ¤νÓўł\x9e˾mԧɉй©ԉί³ԝф˺єƄҔӵϫæӣ˼',
                                                        'ӿˌªюnюŲº˻Ļ%е´ҮƵēɬĖŇˠǤɒ©ύʹǔƑǝʱι',
                                                        'ͱɬƞ\x92ГѶЈģѠÐdсѶ§`ӄŞ˽˛\u0380ǩrȌ`ӣ4Ǉԅɓг',
                                                        '\x9aӢɖüθфǧD҆¾l˅Ɓʑ¢áѐ[\x97ʌdvÅЪʈʈūʟƅ˝',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ѳTêδNë:ǷĪ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ˊ¿Ǔ6ʌǽƀӨʊΉєĠʷ¥Xϣęɛ˾ţдĒ\x93ӃǘɨȶǿǾҷ',
                                    },
                        },
                ],
            },
            'title': {
                'catalog': 'ȢƾąǟΊүЦΆԐѕ.ϑԆȝɆǹŸɗ»\x9aДɂÌЄѵȨȪ҇ԑŽ',
                'message': 'ӮѕǒҧϖǦÚőɗӈҀ҆Ůπɸ\x8dȪǣԅƿԤλ\x86ϬѝŎǒʞоƓ',
                'arguments': [
                    {
                            'name': 'Ѫ@\x84ŴʪѕĭŃŋΛѹȥȋѯˊĨʶ°ѐǵ\u03a2ƩæƁɮ×?˰ʅó',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'Ɩϑ|ѡӚǍϽóøʓ',
                            'value': {
                                        '^': 'int',
                                        '$': -5628034074659938460,
                                    },
                        },
                    {
                            'name': 'ҸƾĠΠđoȳϣʒϏĹƷԅ˅1»ͲſŜ\x87уuɄħÃǭĉ¥ђź',
                            'value': {
                                        '^': 'float',
                                        '$': 574150.9110915657,
                                    },
                        },
                    {
                            'name': 'ÖŞ҉ǯªϓҲĭЂΰЅĉŘʞɈĜ\x80',
                            'value': {
                                        '^': 'float',
                                        '$': 851631.1308282197,
                                    },
                        },
                    {
                            'name': 'ԨęĴҍѰѯˊmŇѐûĥЁϺʟE\x92nŌwқǫɮȼеƽǔ\x9aƙń',
                            'value': {
                                        '^': 'int',
                                        '$': -1122920253417904973,
                                    },
                        },
                    {
                            'name': 'Xȡ\u0379нΙʈуǪϤɝ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ψ\x94ɍ³ϜǺтțˉѝѦюǡŷӁȍЪѭQȄƘѿ˘ұɌԤҺΦ°˘',
                                                        'Ų4tmɿǽɾèǷаͰȜϖRĐǍ*ʸ¦Ĩϖӄ˥#ҷȍBьɢǳ',
                                                        'ҕӯěˠЖҞȒȻԮȁҪ˵ĊƬ˂ɛʳǀӕ˱Ȕ\x867sĥѢ¿ŭӆȝ',
                                                        'Ψʶ˖G¶,ávƸјǳˍtǪŹѱӼʫѫƏȻбα҄ʓ˦Çǖȥɬ',
                                                        'ҴӖ\x7fè˝ˣʭҸʑ9ФӶƿ\x8cFoυϿɨʨǰɚͱ˃(РѵØɝǢ',
                                                        'Ä·ͷJƱēȨ;ӑς\x98ϾñψСӏхɠīɇăҠ\x80Ǆ¤γӺϟʪǦ',
                                                        'ΨҧƩγÅXʭŉÅ¶ČɵҲ`ҾάźӡН;ŏɏXđѠ\x82İĖe\x8b',
                                                        'Ɩnѩ\u038d\u0383Ɣþ!ɗʀʈìδϤ҆ȯ]҉ΘͲǑÝ\x97ц҈āƬˣĤʒ',
                                                        'ʍōĆÅ©ΗόͳƘǛѠG\x94ΪìвŇӘɁšǏŁˬԦĘĪҲӴʵǶ',
                                                        'TԨȼ\x80ƴϗΜϙτ\x92ѓëЪϿ/ұԖňŦÂ\x84æŗѰӨԬΛҐČš',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƍ',
                            'value': {
                                        '^': 'int',
                                        '$': 4282982905056591123,
                                    },
                        },
                    {
                            'name': 'ӈ³ˍ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ѣШӂκϛͱӆʙԚǺ\x95ǵΔӛʶϗˤơ˵\x86ѕ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ǌȧӏ\u0380ѵÃėΎɖЭĮʬҗԗjɂѷ%ԄΖ˶HȆϰϬ«Ńìщ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ЅˉLɽ\x84Ҹśǀ˱ǣΩHєɪʯ\x97˺ðŽ\x8dÞӺɇПЁ7ɹƋi`',
                                                        'ĠīмƂuŇϹ+ҹӾǳɘŕǧʜ\u0381о±ЈѬҹĶϋЀ˃ԃӿćӌħ',
                                                        'ɯρͶĤҸ˜ɦΫϧǛAѥҦ˴³Љʛěοċ÷ˉχſɠȲɬҜлǣ',
                                                        'ǪϞͷʘèʩˍĬːѵԠөϠñόѵ˄ÉǣёЅϧȸķʆɖѝԄƺÁ',
                                                        'îѐĵс°ɈĜόψĹһӒӅһңˆȁɛƗƫ˸ΧǁѨϕͺÎǌƓҒ',
                                                        'ʠŤԟs\x8fśΨȄ|ʻЪıƻ\x91ƳƍĚπґƂӷѼЭϏί˳VƻƸE',
                                                        'Η3өǧjɫşȍɃ§ưӛąΙƔҬӶѻʁˀØǠÇ˹ȝа˲ҙɇǏ',
                                                        'ˆ\x8dѠƍȩʀҴśԢƉӖƊρŦɘȴºѬΰ@ϑԎӞγĸɕҝҚgѣ',
                                                        'йÆŰņǢӔЯ|êϿƆʞƚ{θρYϿÆ¡ʳУέȓĕӓSƑѢ&',
                                                        'μϭѡǈďçϽΫɉʬŭ´ÙέĺҸ˔İƺӳūȇшˀёԫҏǛϽċ',
                                                    ],
                                    },
                        },
                ],
            },
            'icon_id': 'ѥƔlӅÂ#ѳҳɉƈѝǢϓŋǦфʷҙԤЖƇǝѯʁǕґψĲÇı',
            'sound_id': 'Ølǔ®ϧP˛Ѝє¹`öƉВɈ»\x91ƢíǛǸ\x98\u0382YJӀȒñԝÚ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'text': {
                'catalog': 'ʆԇ',
                'message': 'Ƀ',
            },

            'title': {
                'catalog': 'Ɯӻ',
                'message': 'ǁ',
            },

            'icon_id': 'ϝφʮƯԊ',

            'sound_id': 'ƅˠôɦȬ',

        },
    ),
]


class NotificationIconTest(unittest.TestCase):
    """
    Tests for NotificationIcon
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NOTIFICATION_ICON_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIcon.parse_data(test_data)
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
        for test_name, test_data in NOTIFICATION_ICON_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIcon.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NOTIFICATION_ICON_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='icon_id', name='NotificationIcon'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='title', name='NotificationIcon'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='hint', name='NotificationIcon'),
            ),

        ),
    ),

]


NOTIFICATION_ICON_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'icon_id': '·ȏ\x7fϣ¯ԭг\x8e^ƸϩҒѾʜєΩĝΧķŽőʱcaǆҶӠО¹ў',
            'image_id': 'ʧŮŅԕśaҭƼПЯ˶\x85Ϗ0ˁĔҏˮ¢grʴϾǤҖùɽӿʞˑ',
            'title': {
                'catalog': 'мʲʀԈē+ʗÖБѬĦЩҊźˢ˂ʝ³ţžѷɂ˵Ѹ|ě6Ǐɩʺ',
                'message': 'ƖƙŮɇNǦϙCЂˋl˺йӖýȕқеө>ƺҔʐdŧ҆ϖȉɤđ',
                'arguments': [
                    {
                            'name': 'ʑÂ\x85ÛĐǟ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        679136.8211229229,
                                                        111049.82505547881,
                                                        541905.2049554047,
                                                        348841.056967014,
                                                        968333.0054485435,
                                                        662025.7505530205,
                                                        636943.0831308134,
                                                        673867.5976851904,
                                                        844719.3613590284,
                                                        911968.5875486183,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ǟ˺ӲȪпeďÒθ³şѴÄʡӄԑzHâƥθIЪQӣȖ?ТϣЩ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220530:170407.372211:+0000',
                                    },
                        },
                    {
                            'name': 'J<җʿӁȀИԦ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -265912918930239069,
                                                        8256947305602219780,
                                                        -3925641301346550611,
                                                        6850748332041065016,
                                                        -4830028562587305515,
                                                        -5344484875438584820,
                                                        7013056683601751535,
                                                        -8604301557704701122,
                                                        2452815376310693639,
                                                        -4844749128476152794,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԍťŨˋʐȬΘǸδĥѝ\\ɕɱȇÄǠZ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ʈ¤ϣϬŢБơųIÕʨµˑɻкҽŃϔĕ˝ȈļӪϋǿ|ʕȸºǮ',
                                                        '\xadϔϩ˯4ѽó\x95ŵ\x97ͶʃϳȘͷɕҥ°ʹɹęġƫҞǎõƳҔΜˠ',
                                                        'ĭ΅љάɓÓȻюЕʁ\x97éƮ҇όʙćѢ˜Å¬LʏϡÚϥҕͽ˭Η',
                                                        'ˊÏǎÈƴΦуΏçҺϰƢϡ\u038dҔщɁɃƕρĎöч>Úħ%ȋѷƕ',
                                                        'ɄʜҡĹʼǪǪƵéµɪiϸ3Ǒ˙ӌězӃʕŏóǵϼӂȨԤǉҞ',
                                                        'ʋˡ¸˕ӾԫϗуʞǨέƗшRȵʊˢиЌ\x8eũҌϬĆǀʪ\u0383ºˡ[',
                                                        'ĹĘЎƜµĈШºү²сεưƼ~ʅ\x8eĽˆ˥ÑƼȗʧЍЌʊҕʽÈ',
                                                        'uĺƽņТ\x7fÉζҁ˙ϛƯӟШØ¨ЯΗƗҞɌκĜgӆɹԮϿЃѯ',
                                                        'ьʞ\x8eÓӸȩӰTӃԂƠѹӚʌ~ŵǣĮѿϽơӓ˧ˑ\x98ƵΚƑ7ҟ',
                                                        'ԈϴӹOʈʣʞ¬Ԡԡ˕ĺƣџӓǌӂқӂ\x98ƈҊӭӷ¿ÌМ\x9aíЭ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'qϊɹƺĤż%ʴɍ<Hϔ»ˏ©',
                            'value': {
                                        '^': 'float',
                                        '$': 82108.12593621295,
                                    },
                        },
                    {
                            'name': 'Ɣʁϛÿ˳ҧūmӆ)čϝэϡӓƸʓϼL4ԤưȸβΕˡҎŒɀӆ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ЬǾӯɃʻсZŪϺ\x9aЃɍΈʒˣïʕ˸òĩ\x80Ӥ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -6805939855145481344,
                                                        -6095844592062901037,
                                                        -7605537977285741295,
                                                        -962871567857870349,
                                                        6688715339172360355,
                                                        -2372858829491184648,
                                                        -2296430558925457810,
                                                        -8812676991069279069,
                                                        4682184489631096441,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɆȘʵǕʵϙǿƲƟӬȒȵʀȵҥȟ˵рθġӘfлЯ',
                            'value': {
                                        '^': 'int',
                                        '$': 8780422890520218845,
                                    },
                        },
                    {
                            'name': 'O\u0378ӈ˚ʘȰԘʛѹӸҽú˨Ý˲ΥȚҫϾ¶ˊɚ%щBўĒ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220530:170407.378267:+0000',
                                    },
                        },
                    {
                            'name': 'ˊєˑŉCpҍɢЂþӨǲǍβʦĭ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                ],
            },
            'hint': {
                'catalog': 'ə\u0381ӅлѴ<љԥĖȕԓζĔËϗ\x9bӍǖӦ\x80ȮŶƍǈ˳ÌѢѮͰǦ',
                'message': 'ʷԑɞρΰʉ´Ӿˑ{ҽ\x9e\x88ҙΖƹƝËҭƞRǙлΊ¤\u0380ʮŰqѯ',
                'arguments': [
                    {
                            'name': 'ƵƝȚԘ˱Ǭ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'пKǔΘҙΑĘǐÃԮюέԄҡԝȍȜwƸ,ˁɕͶʃȒһƝxÁφ',
                                                        'ʍϒҡңѵʹЋǫ˥ǔūѝƴԟǚ˚ɻЫȱԍʑ]нșȐҐƾȎфſ',
                                                        'Ǥ҈Ш\x9aԦÁАhԬɌƒăǾÙҶʋԃ\x97χǪǲˍOˋǍŪԑԩϲǓ',
                                                        'qŊŁȪҎѾʘΟѥѴƕȘӓ϶ЧȱØɦρĨ\x96Ӣ҃Ëϋѿϔ˸ӽȿ',
                                                        'χΔ˘ǯσSӖЀϸ±νƳäȦӕђӿÜ҂ӖϪ˗ΤӯIʩӭӟ[ȫ',
                                                        'ą(˥Л-љ¢ΏѼɵԚ˘ˁǨθŽЉϥźĶ|ýԧƸˁѠȓЊωх',
                                                        'ŷʻӈʘӌʉʞƬǇΩ(ӑǀԫiҞʡǌɚйԌĭ\x8dêƿˈ˰ϙɭт',
                                                        'ΪķǼˇɱћԕˆƙõÊò(ϮǇũϸʒЦͼµļ&НϩΊƌϧʡŮ',
                                                        'ȁØЯƜΆ˫ǄƓͶȿϷfʏδŞȬԎ\x83ӣҮɃh?šʒбπµƙɻ',
                                                        '҂ˑғŅğšʢáӛ˝ΟԨԥ˦l!λХс©ĺѹNǶ÷ӮǏ\u0378\x98ϡ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȱ\x8fԣʫ҈r˲ěӌƼȂŷѝφӓìҶƕț˺ǔ2фʈÁϞȍÂĐÙ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220530:170407.382202:+0000',
                                    },
                        },
                    {
                            'name': 'ŬͿʤєƨїұƾΜ˭ϒűр\x8dӠʙԞƬ˙ҀӦȮ±ԫΦЅӏЌȲζ',
                            'value': {
                                        '^': 'int',
                                        '$': 4172983717952341839,
                                    },
                        },
                    {
                            'name': 'ȦȬĹǍЂƅ˹5ԓόԌǾƤѨΘǕƢèΑ¸ŕγȡɟѫ?ƚȄӍμ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'Ϸa˒ȱГԥ˾ԥ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
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
                            'name': 'Ⱥǫˎ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220530:170407.384570:+0000',
                                    },
                        },
                    {
                            'name': '˺ѦQɉƢȇѿҳʖрʳǸǒ[',
                            'value': {
                                        '^': 'string',
                                        '$': 'ģ\x97Ѿ\x8dȶŭԞƿɢ϶ʉmŪną3ӵ҉ηȊӴIΣε£ĵӞōĊȢ',
                                    },
                        },
                    {
                            'name': 'ɺ9ûЂɰʗΦ\x89ҞƼѸ',
                            'value': {
                                        '^': 'string',
                                        '$': 'άɱѝˎƌȅƸѢÇƖȌξϽѱƄŐсƸϙӽ˨юԡǧԘӒӣdӌѷ',
                                    },
                        },
                    {
                            'name': 'ϲ%МЦʊƻľðҐåпѺѪϼЍǆĝȍʪԦǾҝLӧҞ',
                            'value': {
                                        '^': 'float',
                                        '$': -86853.94824519646,
                                    },
                        },
                    {
                            'name': 'ƄѶɳǇēǧʘǏ\x9fFκɱ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220530:170407.386181:+0000',
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'icon_id': 'ƺӉĳçɛ',

            'title': {
                'catalog': 'ҳЕ',
                'message': 'A',
            },

            'hint': {
                'catalog': 'ưҧ',
                'message': 'ǋ',
            },

        },
    ),
]


class NotificationIconsStateTest(unittest.TestCase):
    """
    Tests for NotificationIconsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NOTIFICATION_ICONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIconsState.parse_data(test_data)
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
        for test_name, test_data in NOTIFICATION_ICONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIconsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NOTIFICATION_ICONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='icons', name='NotificationIconsState'),
            ),

        ),
    ),

]


NOTIFICATION_ICONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'icons': [
                {
                    'icon_id': 'Ϭ˃ǭŻÙmШćϢ˦>Ƙȡ\x8aҏõʨ7˽ҦϋБΉƋΉÝǏiӗӄ',
                    'image_id': '˒ͻӞ²ıɣńєàSΊѠêъЁùę¾ҹϛˑˈǽϾŇԇŎҘӸË',
                    'title': {
                            'catalog': 'KͺÕǣʞʣӸȎϽjːǬӉʹʨɈϑϡȽAԟʓˎƾПǺѴҰ#Ö',
                            'message': 'ϳ˗ʨǡҷ~ʫ=ėŉԌΫИ6ѸΉΖȭǔ\x9eǣʴĊęɅˉ/ɭΆΌ',
                            'arguments': [
                                        {
                                                        'name': 'ʹϩ(ˏҖǞǤƾÂŢ϶ƝǚuɶҝȺǱƑǗđ\x9fƸɲԖ˔ņŝԚϧ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '²ōƧŧýѭ$eϒѴЗәÑϷčҏǑʭιϣӅƮ%i˪ЯȢх',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЧŘțԣǵӤ¶ɹƅ©Ѷ˚ϡɍ˩ŐĆϠΎѵҡеЦɻȝԪщÂяϷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ДɄԈbбӻώR\x99ЋƳÑɧϰ]ȖΠƄтĈɬ£˽ʳoЯȬƓʕÂ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'єˎˑғóϺ±ΗùƙȾΞγ˜ЕɁ˳ǔűǙƸʿĪoЊγҨ0\x97ū',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.275579:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȧЎȁ9ьƉкϰͲфЯʸ¥ӸҹÂǻȜҞϴȋa>ƱĹЂ[ʼЋ~',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɴìďJŰʭʨӘӭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѥ³ĩвͿӮɧń\x8eϰɥ}',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 677094.13003611,
                                                                        },
                                                    },
                                        {
                                                        'name': 'хҙ˰èеɆ\x8aȒΖŅыΧÜɺΡyɄȘ\x9bȨ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 404926.7984857793,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ӆèȯâы"Ю\x8dԣӳñĕ[ѿȁɖǍƢvΏπȽɀʵӽƻʳYªϙ',
                            'message': '΅ʪĖδĥэΚ\u0379ϥИǏˤŅԢϒ?ԗΊýθɜӆ¶ρғ&υȏðҞ',
                            'arguments': [
                                        {
                                                        'name': 'ϬѾ΅ԫҁԤʍɪŮ+˳ɉćˑԗĝͶ˟КƿƙʡǹƳӲϹϳǫʉ/',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԋіԝһʱϛ3',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˝ÜĞSāԣƊǰɵĖªǑƩЕȴϊй\u0380¢и\x9fӕÑҷƽϗŃҫäņ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɸ-"ƽ]ӶŞΩ\x86\x8aȷдȍϔ\x9bÂȅ˒҄҉ɓҞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.279843:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ôɄÚҷˏ\x86ӵƧӦ˹ʝ¢|ԥēϗʹƹƏӃҌӥȬ˟ɿΧĞϏřł',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 295863.98834311153,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĶҢӡ\u03a2ɺε',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.280622:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'үԟњfŎɑTÿ\x83ș0ɞΟ,Ҭȶӛώĭ˙ʪ\x98\x87έЕʺǟԣёƐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˗ćпkŐԢø¬ӒԛɉÏũԦɛʚѦϐȲ³ƭү˰ҬP^ӪPәŐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȖЖǘΤԜНғ>SŻʄőǪʢѲԩʞӜäɡ$×ʷǇ˝$ƞɚ˫Ő',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '[Ĵ˴ӐΕҰҖʛ=ОƅȮ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ƐGƚʨ\x96ϯYаȼǭºãїÛɑT\u0383čӁȞόтʒѲі\u0378\x85ƑªĒ',
                    'image_id': 'Q±ӇǖʹɰÌɅѯϡҁ9ԇɕʙJʃǺšґ§΅рӁňӆǼӖǿԏ',
                    'title': {
                            'catalog': 'ɩѰ\x8fϚ҃Ԡ\x86ʾĔēҋȏʒӱ9ƏϻӖɿԙoΟŀ¿ѳŌˊԃȌ˩',
                            'message': 'Ś˷бǉ«ӨĈйʌPрѰѽÚʰѿúZӰŸȿɟЊƓЏKʁĻ®˨',
                            'arguments': [
                                        {
                                                        'name': 'ȎëċřΏɒʰ¢ѲſʊϻԥҐǱɹlʃĶпʣʃƨϕԩӤƑЃǒũ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĽEƿөҭǤʑϨԆͰʷʀų˭¶˻W)ԟęţBҀāÌŷ\x99ąŎƯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊǰŦѼʗħȷüʄì\x94țɵʝȺʰθȲӑҽ˴\x9b˼ǙϾˍ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԗɤŠɜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8337574670638768523,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀӗТҐʳfƵơÔӪ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɭϾӮƩƈsԜʢУǴÒrľ)\x87ȪȂвƿоэҝѴșƒӀŢɔѮЌ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 914366.4741288867,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԠμͳӖԘǓҙǸӝņҌӀŭљ0Ċùϥ˅6ΰӌɈЉȮɃѹɹŋЩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8d˨Ѻ˙͵ȕӶX˥ÂƮʯĵѢģCʻĆϛȀέεͶ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϲɥǽʉрȀȶԘ;ɒʠӶǩ˪ªҶ˱ӪҰ¿ǃɜŘΖ7ԉŜԣƒ0',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŷɭέ\x97Ŷϓ˪Ɣ΅®ńƤǑ®\x87ҳˏ4ŦǺͿφЦħˏĪȸûÚț',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ԐлԞ˓\x8cѩʶrđǆӅ΅НşȎΜЇÃφǧ\x85ʖɽ҆T}\x9aүè6',
                            'message': 'è\x9f\x98ʲшű¦\x8cϹȼʈӈͿΑ҄βҝȭOÖӎΎǞơΚm˖ģÀȹ',
                            'arguments': [
                                        {
                                                        'name': 'ʢĕѯŅɖϭɘӮDbϑFʹäҀÚԉƎʜȀǜӾļŻӧoǵ^Ő\x9d',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϹЋѐǮԆŲŇӚÅ\x8fǨǩĥ;һѠҀǀ˵ŵʔȻϬļԤаǷԁρϲ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѭZɹ6ȰǺťƩɆŚӣPÂΜʖʇʟεɄȾ\xa0BӾҼ\u0383ĩоĞ˔Ɔ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 71719.71790542614,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Кԃ{·ҚɣϯēӇŴŔέŲΥéɤɀɛă®bԒǣǭʲ\u038bʇ²ЦҼ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8872472417106401222,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϋĂǑ>ΰӢƕıĘϢΙìхĩԚақϵԜʲЊKҠ˺Όɕʔ\x9dƁɗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƀŸȌʤ©ƳλχΗ\x9cĺîİ˜Ѣәȵŭщˍ˓ȧǅӵƴΌԂʵɑʜ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ãȩTҎ¢˭ѐѽӅԐԨԧҢͿ\x8aǠԈʒǈ6сԂɰҔǾӞϏĞҬч',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'zҭĩ҃Э)XѰӧƾҏϐӐrěҵâ\x9dȤƑċ¦ӷл\u0381Чʩsͳņ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 86689.6803797216,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɇ˰',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣĬŚʋ\x8eʚЯ˄5±ʅʑҥćŋҘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӶĪǹ҉řĞŞӯȗ˘ɂMɝƕͷȄØ°ȣɞРȏϔαΝŬљä',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'қeƳPÒŧÛԓȧХĂòˊԄȃң˓ȉӱʞ\u0378\x96ʷўԞȅɀΌƷ\x7f',
                    'image_id': 'qӶÇЊȅǍˆƥʮЈђμЬȕǃʙеԍʁ',
                    'title': {
                            'catalog': 'ӗ`Ů`ϼɓѰ\u0381ɔɴτǍ¢?˖xϳȻăMʞ˚ʾԦÌǅǵҳЩӽ',
                            'message': 'НϏ¡ѹƳȈǪ\u038bЮʼɷòԈƤvVԢͺŗ\x85\x92ї˗Ѷǚƈ´ɴϸå',
                            'arguments': [
                                        {
                                                        'name': 'I˔ўǍtȻԆӤ˃ȽɱȺҷΓΛˣӔíĊѭĿђ˸ȏÌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӭԀӏӽΖӽѭȦϮ\x9dηωΊЌϕϕńʍˤŨˉȒǷϲʄz˚Rʜҿ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǸVƘƝ˻ǫήҋԞҐÎҺѨϛͱѽ˼ÁĀÒΤȜѨԣǱєā\x99ӊş',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7169983969777434347,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ї*ѫâӯ±оԐ˕',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˥ʋď˃ԃƾǾɲƋΆɖўƂԢβͶjχХǓǄȨËŋӑӞѱӎèå',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҳȆɵƎo7џfĞҤҁΞМýùœҤӘҊѧʌǇ҉Ȼ҂ƮУԕļȧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.294388:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƪΩxӯɮҿΊӱƀðεʳɞѰʸωiȵҞàƟǳԀĘϻ\x86Ç4Ȝ>',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˾΅ȩļĳԛŉж\x82ˁöȧԈΉlπʅνÞ¼Gŝ\u0380И',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦѦÊӡQԗǡԬǜŗơӐȾӄʓŔϳă˫ϐԦǝŐɉƼѦϚŏKʝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'īŖήÂҧԄѿˁ҂ʰĿ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "ЦĬƗ=љӧѴ¶Ţ˸ÜʗǙʧԘǹƪˠ˱&bȊȒȅ'ȝ\x87ǻѯŷ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǁˎΪĵˎͳў\x82ğǝ^ԂŪәԫлƹԚ˖ԘʄʯĚ\x89ӦԭöҖΜп',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ǫˤǚ-ƹγjūυË5ŭƮǯҦӮgϕȼѝѹ¬щȪԃǯƫŽʛʚ',
                            'message': 'ҮӇМɀΐ1ǣťȺҜ;±ϕǠϖйÌϋХ2ʹɕþɒˉƣ6ǞӒҌ',
                            'arguments': [
                                        {
                                                        'name': 'ɌƪД/\u0380˃\x9e˼ŬÈĔƾӥļҒ\x81§ǐǢɈC\x80ԦʧЫĻTΏģ\x80',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.297821:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӎcԫФǍӓƻшԓ\x98ÉʕөӓõґαĩΡϼӶӴ҄҅',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 454329.7018366888,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηъȕЈ(\x92ӥȽÆl',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 246779.14460720326,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽŀʽˍŘ΄ψџȟӍÕʈӤϴΘbѺˀϒ#ħԁȧΊ˅¼ʄ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԃ҅Ҷѣɵǌұ±\x99ҢŇşʞϽңԁĸ҉ȑ\u0381',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄ˊԕΏvΞ¯ŢɥԎίxϒΈǂԂΗԒÑñȅżºԜѷ˰ԢġƋ\x84',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'TûλҺƄɽɚɑǙԭЉ;ęĳΖľʵПρѳƷÛвΆĎΆôlřt',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÚǵϪώħŁʖШӥ҈ʥʅɳӆʒӣӭԗĎˍɻůʃųUΚӞɖĦÏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '%ӯĺψδ·\u0381ǙˢүêϡҘЄɼҙƊԜȧǙ\u0382£ʛɆɇԓû˛ϙ)',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.301132:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'êˀɧЫƵҰͶ\x82ςƃĆ\x8cѻʀΑƋƬԒЄɴĂɚѭƊНªңϸɘǪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 286208.88283903094,
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ǣњƹÉǂ¿\x92Шǅ[ª˰еƸǦųʁӹȟώ˒ҥϕ\x8cń\x95ԥůӍŇ',
                    'image_id': "ïԬͲƇɘȠəûΤǹά'ĎǬǅϠɄɠԊ˞ȘФUlǿŪлIђ\x94",
                    'title': {
                            'catalog': 'í\x91ԍҁϺģǕҭԍΪˣ\u0380ţξΡ˦ҿͶʂЦŋлÔɈǐƜЁíɇӝ',
                            'message': 'Ў҃ƝШѾəŔĆƨ\x80ѡԌѶімьТȜЭʧÚèïÂƫȫŴϚů˟',
                            'arguments': [
                                        {
                                                        'name': 'ѬӻȺǠʌ\x9bšӊı',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8487386331400457279,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЄϾŎЙ\x81ʬ˘ϮǦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȦµȶӟȎґˊĴȽǶť3',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.303600:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɯʅųɻǚм½ɍǵʟӋkŃԧŤϥУǻɵȧѻʂ˥ўȢ҂БϹÄӈ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǿϻʟхЎЄźӯԘӈɿƇçНȪǙȮϲ&ɎƭƅW|҂сєØӒǘ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȁ¹',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǌÕΈâɗ¡ÃE"ʆʨҜĦʣƗŪǕŔ¯ŧÔʠĆǝҌǺ\x89/ҔÂ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĬЫЉөљBϷɢȓɨԭǕÇÇҔ·ԌҒgϘ©Ȏňҥĉѥ˂ʬ˟ԗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8004580678753632932,
                                                                        },
                                                    },
                                        {
                                                        'name': 'RώʪwѰд.Ȥ΄ϷǏͶВɇʞ\u0380ɍÒԭѨɓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ú»ѱӺϙЋǸф³ťͺѧȤ˫ßïʹ\x93уƜԃҰΏǛÇȋ˞ȸѣȦ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƥc>ԨƛD5ǶƁϺ+ҚѯѼ\x8aɋȖҷƹ\x97ΡжӷӬҦȵǇ¼щў',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 419030.5616862715,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŕңɪ\x90ôŲϷƝìІҥȍђӵ¡ƔɚǠѪĭǰȦҚ±ʆɮ˼ΪȾ˚',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 189350.26485850388,
                                                                        },
                                                    },
                                        {
                                                        'name': ' ȫаϺəпĬȧúґћԖөŴȣŸǬé0ìҦȠĞͿɘϨҭʖϲҺ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9042751317702954728,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'тϺBŢĩϞҀϳԢǚ]ǌƶŗ²pԪҟ',
                            'message': 'ЙŅ\u0380ɵǋɢ;ЩéŒ\u0378ķ˭ʢѝǎә˞ϤȽӚYӧДϘԜΑХԘŗ',
                            'arguments': [
                                        {
                                                        'name': 'Ԇ1ӫɽҚɏƝԮΗȒȘȘӣċţБϛνˬΨϖǍĹǝįƸɕÉˤː',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϨĮÙԗȈʧ{ϧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҷӁϖˠԨ˄ԟªª*ǎлˬϢɷ¤ɧÄƽ΅ǻǎΚӽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĕ˘Ƨʝňėŝˤ\u0380ǹӾӲ\x85ˇɼΔбѯʱԔѓʹЋųɃɌsǼʔӘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1018199435035106737,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥ˫ҕҰɠ˚ÃţšĕӉHӹȯҕϹʔĳΑѻ½ġ\x7f¶UΐġK@ƫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺºĻӹӨȈưӹ$˺ɻ˜PηĬ¯ʺ¨@όдƂ˰)͵Ɉų\x95',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĀΛĸӗ˼Нс˳Υć¡ҦȕыǈȔɔӞѿкǚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ªɱɛɭȠɁЌуȳȳųëʀȋbͽǓȎˆKȬą\x93ԟĺXӕЪӊӞ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'О',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 962535.9576657244,
                                                                        },
                                                    },
                                        {
                                                        'name': 'üҎѧʣŒҩҏʜӐãӤÂƐъ˱ҮδџGϪҎӵ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.310795:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '.ō҉˕FŖѕìЭʴХǤПӎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3011776158697351187,
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': '\x92ϹǪӞ\x81Ϫɭ˂рЩȖҬΓêǪɅϘ͵ƶ΅ɰʣϪīɅήƋʈȪd',
                    'image_id': 'РҽȼӀĂǖɘԔɄǥԉaԢx˘Φ϶ӁȍƓǦщϏӂ4˖ΓĹg\x90',
                    'title': {
                            'catalog': 'ȴԚʊςϘϊʹĔԪϨфĦΨȂSԏЅʉ\x90ϊ˻ӭϕɨϻŵΔˣӶč',
                            'message': 'ĉȑė\x83ϽVǎȦҌ=қѴѶӋΟГüɔңʌѷʆdˈâĊǝ\u038b\x88Ŷ',
                            'arguments': [
                                        {
                                                        'name': 'ʕӁǜӹƮȢЍňƠŅĺA©ğϱΟʧǯ\xa0åв\x81ӂӳdʕҮȥǣƣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ъɃ˗ҘĨɋξŔʆGΟÍƠѴϚʩп',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͽєȥʪˬʘҪ\x86ϞOӈѩ7ʆϱŚϻÔǁΏɞѳѿԑ˙ŕ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȗкѩћϰ$ʺőњӲϩӁ×¦σБˁΜũӡĄíÕQθӊ·ĶӸ\x93',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǨɗZͷɢĩϬǜǄξ҂cî',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8557105989558527174,
                                                                        },
                                                    },
                                        {
                                                        'name': '¤Ҥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǅǢɆaľўºϼ˅ϡȲӤɜ\x9cƪү˹ʂōͶԤƅȲ\\ӱΑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɴŊ ԆЖϦ˨ŽŘϲțӄùǛ\u03a2ЂǋçҜ¾ΓǃҢƳȅpʸQɊˉ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƊȧѝϾпńҿɁ҄YНӧÈЃǀÚΊƏŖθɾÛƆūҧЉĹǿm|',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĺh\x95mǴΕşɓkʷԁɜNėΫʹͲΉō¹˔\x92ҶЛĠҵwϩŞӧ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǽ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ţ΅ʠD˘ƙƭȮѸӛӽ\x99ͷ˒ƍӁЖΌǓǚϵȷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ӅȨϮĭѳѠӫЃơJҨӲԢϑʇʸĐÔ.śTӲѤʦ\u0383ӿ20Cė',
                            'message': 'ΐt˟ȹzԞҺƅúͼTʶұ΅āʇӝˠƮӼŽйǈɳß˒ǱƖƳϹ',
                            'arguments': [
                                        {
                                                        'name': 'ƣҥХƙŠˬŴЍŧÐϹĸŉĠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǮƪѼř˞ŞǚǄY\x94_ΏъҟƉɏpĚǜ"ɥƻΜӲȄΪəӒƸԖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.317516:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͽʏțňʶͰɱȨҩǊɊǎрɃɨś҅·ҘƝǙ҅ȢɽȄԚԨȂѽ-',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ģȢû³НǛҶ´',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȕ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҎuƖў\x82Úԃ\u03a2ơЍпɩΌĊõʓɎӥǤoӮĻ˴҃ƤʀNŊбӔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱGμԥԬҸǜĲȎҬ˸ǋɩÑҔщ©ͷȶ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҶɂЏǐ\x9cŹǪțfªɈӀұЫӪҷŖ΄ѺςĘƻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˭',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\xadѼčһǋ[Ūѿӊ˂ȡɞ²ϡӛϙŵĕɆɋİ9ʐԫ\x88ӑɫȿҖÞ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Κ˷˴ɾǴė҄ŤǤƕȮƱЌԫǃʃϳǗҔđѼŪ˘ΠӲԈϺ\x82˼ʔ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѩϗϠŭɇʺӘӺϩȮςȰɓћɤǉˋΒbҿ-',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'kϯŢ}ʠκӫØ¸ƻĆŒpΦύҕǏüȋǿǆӱmŕ\x84ĻʯѝϱΚ',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'z˶Ԉɥ»ώ\u038d*ħ¼ƠÓL\x8cƬď\x8eʁӲɐѡԁԁΓѶɒʈŨȱ˺',
                    'image_id': 'ӜМαȠӝϯѢeƋѓМǳғ;yя¦˷ǎȄϐǥǯƒˋ@Ѡɻщα',
                    'title': {
                            'catalog': 'ˡЎłŪһǅʛҢʖԎˑвϥƒìřôƌįȥɦʺY\x9cħέŞȫčМ',
                            'message': 'ԌηĐ҇Øġԫ«ËϜˉ¾ȧӐҞʹžƊϩˋʄќϴѿǩ˸ɲøoŤ',
                            'arguments': [
                                        {
                                                        'name': 'ЮԍƛÌϧԤȞԚÌό',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 26810.038899338528,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϱҴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӓгЋ\x8fö?ɎĒν϶щ% Эǣ\x97',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0379xІƔȎϧ:jғĪϯȮˊ˧ΓѓЈǿƜʂ\u0378ҌЉɻ˼ԦŤφЃă',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'bďәǙǁˁē\x82DѓʏŢçQΛɳɶǿ\x95ɼ\x80lƦ˅ӝä',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϖрі˰ʬѬϮɛƺĮ¼ŵa',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɇ˻˼ÝɓɻǼˇį|҆ɩϜ¦ĢȒɌ˺\x9fMʉÎЍЪĚΗʲĎˌȑ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƍúʲʱ*ĥ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3167860898479268470,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ň',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȫ\x8c\u038b&Ў˧ыЄ\x9dϐǌǱӎҬ¾ǜѐãϢˀȃӵiѦɒǍû£ԂȠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ː˔ŧÖȀѶʣȨːλϧ˵ğʧǍӃĊԉɉīǂˣХȈ\x87ћфɉѐԜ',
                            'message': 'ʷϯэͷĝʮĮ',
                            'arguments': [
                                        {
                                                        'name': 'ӞϐƱӏ[ϏӶÚЍ^ͿĳСĮӬξȚэӯ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 530471.7801664997,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌΎԞ\x80ǐ»ˍωαǒ˗ØА\x8dɈҔΊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁʗҠƜɾЎʟ,ҡǥˏĸɒԢʨѴϣΪȎͼæŮķĐ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.327509:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÖϥϥώÏŶΔǷӭȗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.327902:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˮ\x87ŰґòʫυˌЭÕƁſԤєɍûʡ҅ɥ\x96ȁnЏцɯ¨ƈќǭĳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŸɶϋȈˉȨ΅āûǦ˺Ș>ϗ¡˄ҁϢ\x97ҬÙ/ͰƶΩ҆ďƳʜЊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҭ6\x8e˱ÇΛӥŔχɩ˖ÂĆԀҟӾǩ¹ĠȼӵΙԭÔԒχ\u0378ҢĪ$',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6762061942741657165,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Πʣӷʨ\x80ԕЂӤϾƘÆЭ¼ɈÝӓɲӱЊƉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'МΑԉΉҎѤƧ\u0382ΩƛŏɮɀEGżȬӐ\x8aµôŋǝB',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 633267.3995858441,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηŰûɊɨӺĤЮЩҪ˅УȵгҰȮ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʿdƠϰєȰʗʔƄǛмҜӵʹ\u0380ɗǎҵǘǸʨˠқюŠЄďĈ\x98ȿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ƈȻŰĂ\x8eĀż',
                    'image_id': 'ƾϻɃфɅЕӧĩ˾ϥŵѥǧŒԒGϩđ҂üҸǬҡЂѯҮԠœϦƄ',
                    'title': {
                            'catalog': 'ƃǡН;ōʪÄ¦ɥʌƯѱôϛʡʊʄĂ˪ɕǔѪϞB±ԚѓϰƺĻ',
                            'message': 'ѷKΟԖГҀ.ԓʷΔɊˡȳƲԩpҮ˶ñѲǙõʈϝѥӹҭɿʦБ',
                            'arguments': [
                                        {
                                                        'name': 'ƩІԫаӵаϔњǣ\x95ƴɳëФKʨӉƿϑűÛħũ\x95Ԡʹyʢёʲ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯˣԆāƧǆύĚӌϘԍӔωе;ɣ\x8fƧεѻ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӃԏЅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'żơŋŅɳɶÅè',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˔=ɪïԇԜ˸ˇӯ\x96ԍƉŌʊʼЁ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'LΘ\x98ф+ҐĶïϫ¨Ъåvҷ}ζκιӦԞȎөХƘÉ\u038dӮƐԡŨ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '0Ԉ[ƍȬȁю˙њʶ˗ŽӃ˔ԛƃɊԝж¨ɌúчАȊ7ȣϾƁѐ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.334163:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѩȝҋ҇ӥĉM',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.334554:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԟʃђ˩ѐȯŤŮдԋåƗӟϛ¬^жˣŤѸѫΉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.334951:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͽðȓϾ˅ԕ϶ʻĲĊԟŽȻѩÿҫäŚΏ#Ц˲ҠӢǫƪҶ˄ӢΟ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 698335.6899224008,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'źŐϪƻ½ԄɲʲөÅΨƦπˌɈȽпɏИƑȖİʯh»ʥʦОԏκ',
                            'message': 'ϥŻċʝ΄ʞͱԟˉǘŏ,Є˲ωƘƎҦѬͳˈϑ˶ċèĲKʳͼƝ',
                            'arguments': [
                                        {
                                                        'name': '(ԠҬĺȽū҈ОвãӯRǢʇӺŞ£Ĩȥ¶ǻ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Σʏ`ҕԋŨɰȲȘ{ӿϛеԒ£åƁҳӸʻɮЃ¸Ԩφ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'б\x9aԜȏԂɢҰηԖ\x93Y!ƸιӐӒҹҰa',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȗӣ˕ԫĤǾϳǝϮǦϲǕ\x87ʭěǒјѯӳɓªƜ\u0379eԞȠʔåzԚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŰŎˏӸσ˓·ʄТ¨ăυΛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭǍȢɛȀжò=eÆԒǜ˖\u0379Ő',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.338335:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˙ȁǗŝӍʂЪԞèÙӵVđІͰλƆčªœ²ƐѾԫ˅èȑ9ʲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.338743:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΘӐȽϷɢӶŽџɘ"ҭ¤ПɀвѴħѨĠͺ\u0383ɽ\u03a2\u038bĶˏȖ\u0382Ħб',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҳðθņ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8846730765898268393,
                                                                        },
                                                    },
                                        {
                                                        'name': 'βð˹Ɏȁɬƌ϶ӯСӴɢрήÄˤƋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǵŒԄɓЪӶõϾÕêȇïɴĬςɉĂ±ϔ˶ЙщËɩļ҂iľʮê',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'Ǟ²Ê\x91ĀмƠԜѯƨϵÉҜʀʧĂϒЉȒΐїĤĭʤÛßŅԖӾĲ',
                    'image_id': '˾ɤʹҠȎʻӕȕʆ˧ßӂǙԏȿɍ˜ʱͲɉ.ʐİӟƺϥҷȿ˔ɝ',
                    'title': {
                            'catalog': 'ɧϕɕ',
                            'message': 'ӄȯȏϨnhĀŻ{˻ŢЍΗԙ;Ǣğҗƒҵ²ԡƏ¯ʇӐѪ˫а˗',
                            'arguments': [
                                        {
                                                        'name': 'τȝԪ˒ŜŨɰҺΪЬXɷΆżПŷͳɹΆŹͰΥʩ˄JϩˍŰŮƹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҳʦäÙɐƩӇkĲǋʞĂǙҒ\x8bІ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӿ˷2Ƈϊ˦ɽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʿӖҊҮԥѫ\x91ŬǔϻŏΩ΅ώŅԁΜЍџČкűȲɌҮ҉Ŏ˒Űė',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.342475:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŧϐŘȏÿȰ@®ȒĜΪƖӏēƾŴYȹʕ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠİ\x9aӪÐÎoѼíɏĩӄλɓѠƵӘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5727313082220502703,
                                                                        },
                                                    },
                                        {
                                                        'name': 'YϯuąҜƌŪĤˈǕŵ\x82ƗѧΉɔRĝˣǙ[\xa0ſś±²ʮ¦˾˽',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÛӝrҳМƼ\x89ʙͼˑŻμļ҉ҀGԕƚΥł·ŉɑWԊɝ˹ъ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 414707.65874026745,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǠH\x9e˷ԍǼȯȡʔƹ^ϊҒҝȀƛϲҮϩИѓ˞Јǲȝΰыԇʎʩ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.344507:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ϊëģĹǾЏOҚӴѳɠΝ˼ȋ\u0378γѹ\xa0ɮȮęԂ\x89\u038bŪҾ4˘vȅ',
                            'message': 'Ϻ:εѣƕŭʯ\x7fɭƙđ]œʤԬɏεŘƼфˌЈīɬȤƱGɼӀΥ',
                            'arguments': [
                                        {
                                                        'name': 'ԎǎƮΪʄҘҜӠǓƊˈϗɆϝ3ӌϴǑɈѽԅӵӎƺ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǺʨвE\u0378ǊШɐҐͻЕΠƎ7Ѿθǭп˝҄ȣˇʡǕɭα½ƅӻe',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'І&ҘѥŔЯ˔ȢΝϾžәȋǚÅЗȎ\x8aºǎңӬ˰Ӯԗ¯˫ȕ¹ί',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'πŋŁͲȝĞԈ˵ɏƝŭlżÜșȝŅŬϞӘϧſͽѶӒϡ;Ҽɝǔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʯҙˌӭˋӰҿǻħpɯJ]ŬІ~˾ĄҊȓȌ\x94ѡĖ\x8cȬŮϪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɰϡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɗ˓ΆĪÚҶr\x8aÐȶіɴɄDˌ¤ΎưуšjȐҧ˹ǱԆԃӪԥě',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŕѷTĴrȖ·˲ѻҋţ#ǹԖήϽǩŽЂĳͰǄŋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƕнϋwԂϣʢыɵԈйȧԮĢƫǿҺʂчΠƯѳBŕȵǎʛΑԪ\x88',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ρ˗тhƹӌɭȇŇĔðӍьƀŋŗ˳7ЕҹʕϰĻѮȨҕƺНŲД',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4283092144900999542,
                                                                        },
                                                    },
                                        {
                                                        'name': 'țϽΏԤІʨưЧ϶×\x9dƻƐУг˸ƈēÐѪȹɗЎȮĿȻĳʹԑȊ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '8ѽʸəҦ.ɌӶΌͷɢVӺȓϙĶƉȗɽƛ\x9cƋўȗ˫ˈǒ҅\x81Ʒ',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ĻρΡŷūӊȝɊθȻŸδһѤɄҪыɍўƩРƱǛӉəÏØƃȒN',
                    'image_id': 'ΘǏɺǷ±ΞҰŵϑȄĪǷӉĉϽϚνƊƋĤʓbΚȹзZσƬˡσ',
                    'title': {
                            'catalog': '\x9fϠòĸҩȜũɨЀΠɁ\x8bŢƭӯɨέɹʌɀPƥ6˅Įȧ =ΐΡ',
                            'message': '϶ЃĆίļʺK\x91ӴһΚЪɅǣҶϞŖǩĢƲVƐzɿ\x8bǐĝ\u0383Æǂ',
                            'arguments': [
                                        {
                                                        'name': 'ɼӵ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '.Ρ˴ѺƾÿʚѺӶҞҒˌʘЅǦBŕ`ìͻÆ§Ǡ<ϾʱЧ6ǩ\x95',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǛǂԔѯȜҼȬ\u03a2ȹɾӾ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĚΣӇċΥ҆ψŵ@ȡ˥ǻѤűϢſύtʐзƦЀϰ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʝͼлɟӧƖɠǡш˶ʹƈǝϼгҩӜχФÔӱ´ӶѬɆΨȇӨԐŒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ўæˊϐΡ϶Ҵǅѵɉ^ўМԊΐόʆmȢ;ĚΨώ҃ʄӟͱ\x8eδӵ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҃·ȗ \u0380˰ҢΦɽɹ˩',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҕҶĒÞӎξ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ί˻!Ѻҫ»ÔɖƌɾЭͶӃԫɅџ÷ϱƝɉŦԉƺǤŨɣώξ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĳѴʋ˸ɐŕѤķǈπЕѾԌӴ¶ɾӇKϠ2ˊЩƸ͵',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.354012:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƬԣӝȳɂdТϟ˞ʹϡγáǌӳёҽӍǧŸʦhƈӰӏ² ϤƉά',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'íӉюұǧхʖĢǡȞʟ¨sļѢȱǧȰζɩșũӭԬė.юȣςˉ',
                            'message': 'r˜ɗɪ:ǌӑȍļĝɴ\u0381@ɋϕȢжσюđʢǂϨϴєǺƢǓάś',
                            'arguments': [
                                        {
                                                        'name': 'iŎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ö˭˘ЧďʺОΦȓŅȤϮԛːŰάѕɛ)˱Ȉшˍ҈ŮǔћнʪƼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϝ҄ƾЌɽ˺Ȭ|șĄ¡ɀĴӼԀĆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¿üΆ2ΤщӥĭÝυēФӔ˴ʤɜōԕ8',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5628477561002373863,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ă£җĈĖʯͼǿcУΥԛӉŘƆϨőԕKʞ˂ŋȭʯę҈Īʵѳɦ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϛʟƟȘзɞԀĊ^',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ώ\x8fǅЯǙŏɫ\x9bĴΑЬΟp҉×ʅėИĥӈîÞȁǒ!ηʽІΊΆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊˢџ\xa0{Ԟʭƛˑԥҙћʤô®АǸĿ˓ԋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¦òĊѺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƠɒҔИʗӜ£©Є',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ļʪļЯОςӥϥϯәǇ\u0380ԡ\x92ɥȬԄέƬӚęǈӮҴ0ϰËѬ/Ā',
                    'image_id': 'җѰǒ|\x94¥тƻhǵҹϓŔѦқѽƜ·ţαһɛ˒ƞҞӑˋˀʌ\x8f',
                    'title': {
                            'catalog': 'ˬNҍƞϥÙΠý¾Ӡћ˼ˌAÊз;ňѪІԜǤГ¿˪ŐЗʢǶŚ',
                            'message': '϶ΫɱʸВȮЕѡͲʻԈƽŔ2˫óãбǨԢԝ«œĉǽ\x9fɬҾNɰ',
                            'arguments': [
                                        {
                                                        'name': '_ÕɹϟǭɩƩϐЃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.360367:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƫӣˣΠäɯ¨ʿϺȯʪƇĕʏ˧ÜǵìЗȌÇ\x88εĺ\xadҟңǭӞΨ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɧŨцˢXǊ\x88ʔ\x93ɜΨѓɿѶϩҎɪύŊåŤԪʈɋͼ|\x80Ңԣǟ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'иʚĨϵǭӥԂԔӪǐ±+Ӯ*ʥҿќԭǕӘρɗѸTˢѓñ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.361186:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԂǿвŏˑԃΗŠǔÓOŕŹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.361583:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'âŶшǳ\x94иɆѐ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0381ҬʣөùT˫ɆȪÃʀ~òϏʊҔξĚȚӜĖфǝΥѬΊԍӰZċ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 218365.86686369928,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӹҌϝɂ҆őƺҏʡĦăŷ\x90ƬÏ\x9f',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǚʟĶРʀÙԖƃŖҌÕbӰŠɘʋDöyԓǟȮɅϖӲ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'өÎØϢì',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ' jȦοȊЂЛӺή˻ϳɧѰԎ˶ҡøǟдǷ\u0383γĮѤϤY¥Łʽο',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ýȲûfUѥŸËÊǽʺǥɫǠҊÉˊҏԝ҇ÙȘčɂ҄ěӍW˚Ϗ',
                            'message': 'ӜːԦԚҨϘ\u0378ǻŭšΙƋΘƅϞƭxԣИԚðδƭӶҎɛ˯шèo',
                            'arguments': [
                                        {
                                                        'name': '\x91яŁεҡҰīʩщʑϬʨɌԈЯʪȴПǏЅʙĳԬɹϬХŅŅɥ§',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'нŚĉҌѾτïƠ\x82Ўʳ¾ҜĤ§ϋӑĆѫȱ\xadWѨ=Äʐ\x9bӃӚį',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƘњҭŐ&\x9dɧǡϳ˰ģѨԎɩԩˮ#\u0379ʃɃΖéӒҭʸ҈iʕ}ǘ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȟҶ%àŏÖҿŖ\x91ÓƾɔіȢԢԐ\u038bũЇn0\x87ˢă\x95Үȣ\x97Ñ˰',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӤȯӇƐυћӉ\xa0ԉkӒ5æтҳȦ\x86Ȋ£ʷƲϹĶ˼KжV`Ҵ£',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7387367556707994030,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƋÕċњϽâϘʀėӎÏŽţȆұЧ§ĖȜ¤=ìĨŗ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Īĝ\x98ƂшÁҘɑ&cъ´Ӗʢ\x8fŞюмíŚʟˈԈ˱\x95ȖԮʚȉ\\',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Α7HΉιĕǰϸŵъū\x8eёȼˎІӿӯɚȵщл×ʢ\x9cπĠһŵ˽',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 109032.47934695921,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҮӰěˊҧЦȈāԋ$ͿƑ˺ʷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЪTӏǆѼҏ˚аƜÚÃƶǈȻԠδºѪʈÖϱǖɥƿʜļīтäƼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǶNιԂ϶ɚΆԘϴХȾƯɸԨ°ϿԣƮҝ΄ȅƽȎѮƯеwӧԎӸ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˟ɗӆưӸʢȌȐŗЄɺʧϨϿϽmΊЗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.368211:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӉªǻάǕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170407.368603:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'icons': [
            ],

        },
    ),
]
