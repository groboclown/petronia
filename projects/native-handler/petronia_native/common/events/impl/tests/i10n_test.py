# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-12T16:50:56.749082+00:00

"""
Tests for the i10n module.
Extension petronia.core.api.native.i10n, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import i10n

class RegisterTranslationEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='RegisterTranslationEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog_name', name='RegisterTranslationEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message_file', name='RegisterTranslationEvent'),
            ),

        ),
    ),

]


REGISTER_TRANSLATION_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': 'ϽU',
            'catalog_name': 'ҀǘЗĨÉӖȥŗѨ˾їѾȱĻӁĬԣԍҳ\x97ϴϧʨўǬ˥ŭϟ·Ў',
            'message_file': 'ʯ~ԏŐѯ\xa0Ӏ¯\x9eœǉƑ΄хƞыβMãҖžП\u038bѓyЙйŻËѕ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ԕ',

            'catalog_name': 'ȧҤ˵',

            'message_file': 'îi',

        },
    ),
]

class RegisterTranslationSuccessEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationSuccessEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in REGISTER_TRANSLATION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
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
                res = i10n.MessageArgumentValue.parse_data(test_data)
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
                res = i10n.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ȁ¶ѭҫ¸ҮʃşǴǧԒʯάƎ\x90iŶķǿ!ȿȾȦƸƅȤŶɌßҶ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -914193098218231361,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 596953.9756445179,
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
            '$': '20210212:165056.682556:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ƪӝа\x90ΘȱǪ\u0383΅ďѵԫÖϹˤ?Țǡԩɾǲ\x80ǍԂŏÐǌµПΧ',
                'ʳmȇŭɬіēԣĕàӲғΈ;Ħçʴ˘ΥÔaaťϙÌΉʍκΈǁ',
                "ɚ\x92Ҁ'Ԓˇ3ήŌ¤ԤżЩʱҸͽΚȀɰц\x8eÅϣͺΏ˗сӖϬо",
                'ƅҤύ\x92ǸĝĭĺѽфϾĿʭȣʤҌʊҞgΑĎǌȲȱǀѴӊ#фЂ',
                'ФҪɁł2ѝǲ\x95ΕˁĊҢϝñʚƔ˼ϜӸJ҆ӽόӃõ¡ǬȾӤċ',
                'ãʞюзԉȶO\u0383ѧŬé@¥сԔȐǽɽѕӁeԙн\x7fӼːϷɠԞˉ',
                'ŚѢѫĜ˸ӥӎӎ;˹˸όͷ*¤ϽάӤ˄Ĩăԥģ\x88ѡ˫Ɛèƥʼ',
                'Ā\u0379ϼÕΠ¤˅ǵьϛȻHȪϰԗŌ;ØĤȍ8рӭЋΒʄÛˢңҺ',
                'ȩǁĭ˦\x99û\u0382Œʭƾʷ˫ԟ\x99ßϙ¾ƾǿɅ\x82ŵҔԝШƯ,ǉʺǴ',
                'Ěҽçҗ¯ćÏИӷŬΖǄɷ˒ϬӬϣ\x81цɀƵΓζӞŌʗ҇Ǒэκ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                2324395850820680126,
                -3807988194049579295,
                5680836227475319619,
                -550636949192582217,
                -4603557216650401276,
                6470597089544433007,
                -8184016371664472275,
                463079437448924557,
                5120624652832919244,
                4609804071284595827,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                418128.8557213116,
                491763.19717976265,
                716655.1714346745,
                351239.4327013111,
                608368.5388357142,
                4090.11800209606,
                102652.97005243474,
                801705.2323584028,
                -83025.96146036562,
                -9268.43383103171,
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
                False,
                False,
                False,
                False,
                True,
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
                '20210212:165056.683381:+0000',
                '20210212:165056.683393:+0000',
                '20210212:165056.683400:+0000',
                '20210212:165056.683405:+0000',
                '20210212:165056.683411:+0000',
                '20210212:165056.683417:+0000',
                '20210212:165056.683422:+0000',
                '20210212:165056.683428:+0000',
                '20210212:165056.683433:+0000',
                '20210212:165056.683439:+0000',
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
                res = i10n.MessageArgument.parse_data(test_data)
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
                res = i10n.MessageArgument.parse_data(test_data)
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
            'name': 'ɱќҷŉѦҴ҂ԃ·ƭȯΣӞӼҴɵȕȐȷʸƲφ¶Ҧ˷0ϛȒ¶γ',
            'value': {
                '^': 'int',
                '$': 2105295869349163897,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ľ',

            'value': {
                '^': 'float_list',
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
                res = i10n.LocalizableMessage.parse_data(test_data)
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
                res = i10n.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'qƫ_ȗƐȫӊ4kɢēѼƘˆœτǎùr*îӮэȟďάțÆЇÓ',
            'message': 'ЏUǱǇĕɞ<ơѐÓϮԓSˎăŘϵŀҮѨɾpвœtʤʆɃԉӏ',
            'arguments': [
                {
                    'name': 'ˡ˩΅рʧŔμʚǚɈʔƞҼšѪТ²ɜǡȠɡѤƚԦѽķ˗Ȏʴ8',
                    'value': {
                            '^': 'int',
                            '$': -1299474195568766985,
                        },
                },
                {
                    'name': 'Ȫƥ˳εť˰\x9dӠ;ǖƄͼŜдѓ;ʓ¥ѿ~ªģ\u038bTϴøuβ',
                    'value': {
                            '^': 'int',
                            '$': -382522337601870848,
                        },
                },
                {
                    'name': 'ǀʩѺnňҿʇѦɲΚʈ\x8bϻԎɸѽÙ}Ϙъ»åЄ\x96Ӡ',
                    'value': {
                            '^': 'string',
                            '$': 'ҟҮŰЈǥԞʧŗϾzʫˋϡ\x8cɆԗȶűЖңϒԂѿРӧƏӺҒκN',
                        },
                },
                {
                    'name': 'ϨґϠÜή4ҋƗҰ¢ȞìȮˤ³ȉȺĨɈШԬϜȩĿʉĚ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        521736.02599821426,
                                        343624.3848837439,
                                        741901.2241530927,
                                        985394.828246,
                                        993709.4141948961,
                                        822718.111891035,
                                        848926.0151365862,
                                        153063.95300125802,
                                    ],
                        },
                },
                {
                    'name': 'ˮȿў',
                    'value': {
                            '^': 'string',
                            '$': 'ɍÆ¦ÔǽȗɊĶŦē^ćϫʕŵƚҌԬİəĈНΰ˔īƗа҆ԠƄ',
                        },
                },
                {
                    'name': 'ӹұœΔpϨӐ®@Γƻ[ʹԘϑàӽȿѧñπɢӂ«ԈҤл{Ǻ˒',
                    'value': {
                            '^': 'string',
                            '$': 'ĆЦčõΘε¹kÞϲʪ´@˕gþѩϵέȲ>sʋє>ƺʙwАӋ',
                        },
                },
                {
                    'name': 'MƠ.ΩĮĹƭɪƎǶàXŪҎИЄ\u0382ѶʼɶыѹêZҁКɠ`˰Ϲ',
                    'value': {
                            '^': 'float',
                            '$': -48544.1150750533,
                        },
                },
                {
                    'name': 'ǻҐУƌҞΥAå·ɻUԦԃҰʜƙɜг\x8bҘĴ\x9bűǋ}ʌѝɭԩʓ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ɺûˍ¹ǲњͺϗȰ˭ЈӮĨɷ\x9cʏŹÎјİӾӕ¡İӻȻĨȡӵǹ',
                                        'ȦԎԮɼӜιӤϦΊѢŝ\x89ЊÆ}ɞɁͱÀӻȿӍɥТφАĉůѦP',
                                        'ô%ЧϊӿҠϾΝŒʫӨɬƘЕɌҁίhǡøϲŘϩѢҥʧԂŊ¤Ƃ',
                                        'ĄŒƘ͵˨ǪʔĳВ\x91ʔȚҸǚƗǧƲǖ¶Ѫĵϫϴƞlуı¿ʤʹ',
                                        'ͻΑʥɿ\x7fΖbҵˊ^:ԬèĦѭʏŷžғϞēдÎˣњˮΈȥԁн',
                                        'c\x91ϤŞŻĐτˬͲ0ŁǌбχŢκтȖĸҁʢ&ɤȰˮĨ˵ɠϮμ',
                                        'ƞɵƫсȰѶâҒ×ÆřȪɤʁaЧİν\x8eэŅʀЩθа\x7fЛɿԕȘ',
                                        'yҶ\x89ԏjÄ\u0380ӾϖfĻ\x95ņΎȃȹvԩ|ʦȑ`ȘĤТáǺɴȔǕ',
                                        'Бvŉ\u0381ɳˢҦ˸ȔӀѦӷҲЮĩԦԙμǂԖʔĮОʈЊńǷԫƩĩ',
                                        'ʂϚхδԆЂ\u0381ԠԀ˱ƪƎʓÐӋптˁɅЈɣԨΙ¿óѾиņǒԖ',
                                    ],
                        },
                },
                {
                    'name': 'âёÄɼÈљӄĎӽɴǾɹ',
                    'value': {
                            '^': 'float',
                            '$': 929206.2316659122,
                        },
                },
                {
                    'name': 'ӘЭĠӋtүƑǊӸǭΞԍ˺ĶͼŀʂıԟāӺŀʜëȹʊĘԢïӲ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ƸүҰ»АȺƍ\x87ҔȺßǰ\x9dσtɉ<ԝːЏÁ\x81ȐȧȽǴjƽĉФ',
                                        ' āѬɣʹӽű\u0382ӱŽƂĊȄχɥԋZʲҷԡȺɣЯɖ\u038dȳӖѣ҆Ɩ',
                                        '҉ŲVЉϒπͰЍǔѮȦ˗\u0378ӟȨöƔϙŝȃϹψƸgӃʲҖ.\x8eȚ',
                                        'ũÔҗÀϨҁԜɝ\u0381ӔƩǦʏӞ¤ɅѽɣӃ˴ǠԜđɇÈɪƀˏίψ',
                                        'ŷљÔĀȂR\x8bü\x86ҼϙƮǒͳŏӭǾћ\u03a2!ɠӳЋЄŶOƌӌµӰ',
                                        'ǆ\x9fɩ˾ŇǸgэҏuԚƸŀȁԬ\x7fѵԩҽәĚ\x9aϦЇɿǌԚϸƫΡ',
                                        'ЧΤHʒʺţ¯ˏįĲѮ˽ŞӺщԫʝōĉʙˍĬŊϹǜйъӅӒα',
                                        'ǧëʫЇõȕҋѸ¸\xa0ɺL\x8fЏµɥΡτħуȇ\u038dĨˑһɜťӴГȆ',
                                        '΅˺ȷѵȏ,ǰȹɴƗ˯ˇĈӿKɮνΧɚ5ʾҒ˭ϨĽJЕσǘʋ',
                                        'ԂӻϖΌсvϪϟ+Ʀт¬Є;ԛτБ»çłҝєЅѨʘáжҏɸʓ',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '6ˣ',

            'message': 'Ю',

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
                res = i10n.Error.parse_data(test_data)
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
                res = i10n.Error.parse_data(test_data)
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
                dict(field_name='error_message', name='Error'),
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
            'identifier': 'ҪƷƂ\x96cƧʹÝ=ԇ;ƌѴŃ\xad4ʾĊɦøЯȊΊȠµû®ϊԑϲ',
            'categories': [
                'internal',
                'access-restriction',
                'network',
                'file',
                'file',
                'os',
                'access-restriction',
                'invalid-user-action',
                'internal',
                'access-restriction',
            ],
            'source': 'Ϧй˵ɝɭБлîĔΣӯĺϷɵԧʨ2˞ЅYďɵȥOѷɣ˲éÈШ',
            'corrective_action': {
                'catalog': 'ԤɂʴșͰĞ3ńӊϚůrʣȩǹҴϳҵѥ²·ő΄҂ɧşªԕЕΒ',
                'message': '\x83áǾΉўӻԡʽ÷ԔɠΉƅȨ\x8cµϹǂ\xa0ÎɤǞћЬŐϡʑ$ǳǾ',
                'arguments': [
                    {
                            'name': '\x82ÀҀ˧ƳџίэӛћĊΟðӦʺfΩ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ɴбȗƪșΎԖҤ#Јɮē.;ҩвȱҬʤҭԍҺћƮƭǇψѮβƦ',
                                                        'әK΅ĉͽ\x9f\x87;\x95\x87ψѬЊ͵ĲηЋúɓƑђй+ӯҤºђ˚ȶǢ',
                                                        'ŮʫƚњǣɶŞǮɾbˡɛӸ\x84ʸЛԀǵǥʭϣˆ\x85ҌɝɱӃԨƷԍ',
                                                        'Ъɋȵ6ҀӱɣǌiĒØÔЩVԓχЬƘϖ˫ǸȕÐԡʨȈӒ\x95Иƿ',
                                                        'u˭ǁƷɄźӠҶ˓нŭ[҉ҋ]ȰƵѹãıԥʞjƵƸƁҐǛǭɭ',
                                                        'ΰƆқʕƱΜʝɺʥЏЉһͲɻŬȉЀTɬ˔ԇϫ^QĐҿ\x8b}ĸԆ',
                                                        'ӠˉԈϏĽɏѴͿӥʭȺÛƓ¤ԇȯɥ6ğϲ˖ŗεǨɽŮǄԧέˠ',
                                                        'ɗϢԜԀӌɡξ%ɤ϶áʖԂʶҍƌʹM˶қˆιʦԂӊƧ¥ĳªѭ',
                                                        'ȵEʠҋφӋϨɱҩҸǐѧҝǊ҄ϷԟϏȦԟŵѓȉ;ԎӝǹϮʈ£',
                                                        'ǐҼșіÏѷȧ¾ԓ6ǨӆҕˬЖϾ¨ς\\Ӭʏǉɗͻ[ĉԊԌєȺ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΝƳOǱѰǲѧ¶ЫDĖϡŠҖȗēӉԔуǚŞǡȜǑȗȡԡԤʴԃ',
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
                    {
                            'name': 'ԁȏƦćʽȗфˏԄĔǨфʕ˟ėεΨiĊ¢ʗǺļǨЂɅƅüÙψ',
                            'value': {
                                        '^': 'float',
                                        '$': 455856.49756043754,
                                    },
                        },
                    {
                            'name': 'эͷɦɡԇΒƝ·?ϱɞ\x90ƕǘ˯;εϘβț0ӳǵώǍĂϳǳ\x9dƃ',
                            'value': {
                                        '^': 'string',
                                        '$': 'юˇʚɵ%҂ţϟñИʢˇÔJЃˢɔõΛÑ˭ӅɷφѸ͵Ԣ˝ҾӇ',
                                    },
                        },
                    {
                            'name': 'ʺїŸ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        1425028323144727993,
                                                        7306231880747490202,
                                                        1889686310226392246,
                                                        -7840658855487648968,
                                                        2062155604800072533,
                                                        3552440635208661562,
                                                        -1948193797140316027,
                                                        5287335036941680541,
                                                        -7091436424134790435,
                                                        147584329110193521,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƄšʢƩ\x91ǣѾ\u0383ϏлԘɯ΄ǘѶŁҗѨѕǓ',
                            'value': {
                                        '^': 'float',
                                        '$': -84899.25609589666,
                                    },
                        },
                    {
                            'name': 'φŕћѮɥ҄ĸ»ȜąɴЏΨ˞ʄΑ\x81ыЅϩԈѪϷɉ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ÚȻԉԬȟίˬѷǰƵȍ˾Ȥɗ˫Ƀ\u0380ŧ\xa0\x7fѧͰǘƋ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԏӘ˪ŢԦȪҩŧʎ^ІЋϐӿƀȄʊеʬőϹɭϘʤȗ*ʞӝǥ˝',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        216465.17773035786,
                                                        855118.6455699963,
                                                        747665.6748001338,
                                                        900947.1111540435,
                                                        969676.6469158051,
                                                        970295.3381795788,
                                                        115547.3318638306,
                                                        616699.418131873,
                                                        567073.6033877489,
                                                        687635.9279098619,
                                                    ],
                                    },
                        },
                    {
                            'name': 'џԜҐϫʑӼ҅Ő',
                            'value': {
                                        '^': 'string',
                                        '$': "ŶÊ\x9fƌŹ'\\Ѿȗ҄ϋɋԥƕͶҾБӊɢĦУQԃЍӘƘԤ)Źċ",
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ʍŅÚʋȝԁț͵ӧђˋҳӓʓQЛˇɷќԪÁԚĨЏɔϏͻłƌӋ',
                'message': 'ӖҊ˺ʓǧӾԬɱơÅеȭтчѝĤŦΌŌƆД˰ȶȾɈмϯ©ËɁ',
                'arguments': [
                    {
                            'name': 'ǊÔÑ\x80ώԒ\u0382 ƤŇюǊˀӋ˛ʳλѕҜő',
                            'value': {
                                        '^': 'int',
                                        '$': -4173970319760047613,
                                    },
                        },
                    {
                            'name': 'ǔhšƚ\\Щŝˈȉ˭ϜԒϲĴϦ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210212:165056.683773:+0000',
                                    },
                        },
                    {
                            'name': 'ʒԡɞǫƈÅɝōɣƺ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '=ćĒΫҵѐĦέDcʫӚîëѷ҈ſíԦГЃ\u0383ǟϐļ͵ŵȣɿƛ',
                                                        'ԈƝˉǶӒЃіɰÖЛXήɕӭʦȅΑĦxԕůÌ\x91҇ΧǣɻɎ$ˤ',
                                                        'ƧÿȸЁɉЫͺ˅ɧΧЫ\x9aȢȬǲ·1ΙҏȠԛӥMȩƉʠʡӪѓÅ',
                                                        'ŹǞɨˁˡ\x96ĳЏӳǬŤáƹNšηқėбʋÅƊԘѝ-ѫϥѬоȧ',
                                                        '˄Ǳĥ\x92хΨ»ҞƒɆԭʮӌ˜+ʖȌƬJđƅЩǧ\u038bĿЭHɃͽ\u0378',
                                                        'ӜŅӊJɶʈʿ*Ż\u03786ɪ\u0381Ý\u0381ξʾԭȳԩŤԍƫƳҵʉɺ\x9aɦn',
                                                        'ȸпåǢβƢǇѻЎǆβzȉД˼˾ɵF˻ɛȄ]ӤяƏȳȋφ˲ʄ',
                                                        'Ǯ¸˳˟ȏʗýΖĠß\u0381нO˱κɄĀȥϊƞϦ˟ǓȓОһсХϷ\x8d',
                                                        'ʴʇӆɮę\x86čÕ(ƳĨπȰʬȬάɈѻͻCȋЦʃӁȠW϶Ѱӿά',
                                                        'ˣƶ³˂іuvџÌΊ{ЩԦѬӟţ҃ʙ\x98үШɒƨ\x82ԃōοŝѼA',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ÀƴßŋϩȵԪŶ\x80˙ӋФģ®˽кӖ˺nΑĤƞƹ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210212:165056.684287:+0000',
                                    },
                        },
                    {
                            'name': 'ԨҽҧȱÔƲӤԪЈͲӠϽӞν©ʃȐȅӉϓӶŸ<ΏӷŝjƹǏȇ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210212:165056.684462:+0000',
                                    },
                        },
                    {
                            'name': 'ˌӨǧ´VĚ¹1ԭƦȎʷәС®ОΤŴѣ5G¤ϽĜ',
                            'value': {
                                        '^': 'float',
                                        '$': 269685.6240561534,
                                    },
                        },
                    {
                            'name': 'ĺɲĹ(˫ȠƦάɐӅBͲ®óƪǂцơʂOΥ\u0378vȀȆ\x91ÀӪ~\x85',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ʤɒȧOӺVѠԅ͵ʊɠФĊѻдƔӟȌҥLԡʬЉkʃsɥζё˛',
                                                        '°ѹǳ\x9fɋŝҾBͺԩиΏɑŇȂDȮУеɹ!ɬҡТɆ\x7fŋÀć\x86',
                                                        '·\x9aȮӤǠԡɩ§ʗƱР?ŕƍǳŷɽȕƏрi¬pйǐˑїԛƸӚ',
                                                        '\x98ƠƁ˚ҳ/˒ҠȤԦ¶јȑʦζŎĿзÓЮɇȀĆƋһԑȦҢϵȟ',
                                                        'ƒ$ҋŤѷΊƚ\x8fөѱʂӠ¿Ԟʁ¯ҷ˾ѹˍԢʻǲПƬéǱͳĄ˖',
                                                        'ϧòΠćћnʫόӈϏ˜ҧɳϒЈĚWƺʛɐM˷ӴƪÓÖˣȢŏ;',
                                                        'ž·/ϿЋĮàӂʩĠψÏΒȻŚ\x9c$ʷцκƤӣˆŞ˰Ыďуß\x84',
                                                        'ö,ʩʀʦɄ΄ϽʉɠʊҙѹήѵŖӘϖǥǤš1Ψ\u03a2÷ʷǍ\x8a\x96Ǫ',
                                                        'Ȭ\x93ƆӻtȥԥǎąɋɐҺˏăĔрБʟǳȪϟϯʊʰĠǁЍ(ʉǒ',
                                                        'αњ҂нэΔЈĮɺˏ\x95ǹŽĥъΔŒýϰϣǘáЁ+¸ЈĽǔƊ\x9c',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĵˆƥ\x7fɋӨˋË0ӲЍ-ΙΩϩχёʳЅäȋęˆʈяʣoȇǍԧ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'őЭʣʔҳæμź+τҋʝxǖʩȂ·XËȿŪýÞҁƯǳʩɂŚҞ',
                                                        'ϮĦȿęʏɡ˻äзе˗ǃӯȮŸґŃ϶ћкπ4ŏ˟©х\x83\x8cDВ',
                                                        'ҝȹԆԔŖȉщѐţƾwˮП0Ùķƭъθđǆӟ\u0381Õη9΅˫Ϗs',
                                                        'ħÍˑǦΓĮŰтɓѹº\x96ΆΩiЦϟɛˢáΦҎͱ˶ǩГŔ˂ŤƘ',
                                                        'сÜ,M²³đˊƒˇӤ˙ЉҿÕεƠǊғǩǵԔ\xadâ¼ĀjµɬÖ',
                                                        '˔ʢ.ŞĢɢʑϭșЯΌɄíʈӛΠʑɈЮїȥħ·аѨòδɜѸЩ',
                                                        'ҪpɽԦʜȪÆʣżνʑ\u0381¿ĆСЍˢԊ\x91q|ԠɠҩÏƾɦҡƘǈ',
                                                        "Fϵԉɋ'ѺЇҲԢ˘ď\x8e:ǸНϩoĈӠψǠǔ¸ɂ\x8eɯFüńɍ",
                                                        '\x84ƧԡЯćɓÓıʤƴʧħϼϓӡƜӁΙɶϜЍЁϟœŕϯǻóJʛ',
                                                        '¥ίΕɰ´¸ġǂÇĮʏǬ˴ȣΕžƄȮƱиə3ӼїϤcԟϟqϗ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ņĎ@ʼȫόWʿљωȱǧҢɡӝҤϝ\x7faˆͰÒɻŶƬџЃѹЂș',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        82788.67037861244,
                                                        332146.35914097895,
                                                        82095.51412299118,
                                                        572316.3049522972,
                                                        891506.2529757211,
                                                        -58950.893566094455,
                                                        568734.183939014,
                                                        179726.95434470067,
                                                        578807.0916315177,
                                                        129812.95049735412,
                                                    ],
                                    },
                        },
                    {
                            'name': '\x85ҋŀɴœÒh˭ĶƍƌŞȘȻҰ\x9dѿцЋȰʶƉ˾áǔԜƵӱȸΪ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ɼ\x9fň˳˴ӶC˳ʚ1ϧƠˈśӽ\x93ģQśǺҷӲйԑԉʄӟ.³Ʒ',
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': '©øǦʟť',

            'categories': [
                'invalid-user-action',
            ],

            'error_message': {
                'catalog': 'ˀ\u0382',
                'message': 'ˤ',
            },

        },
    ),
]

class RegisterTranslationFailedEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='RegisterTranslationFailedEvent'),
            ),

        ),
    ),

]


REGISTER_TRANSLATION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'error': {
                'identifier': 'UЃǣԉʼωҎ˶Ƣ\x8dӬďŎа\x80ˡǀΞҍjÊ\x81ɉӤӺбǹźÄƃ',
                'categories': [
                    'network',
                    'invalid-user-action',
                    'configuration',
                    'network',
                    'internal',
                    'file',
                    'network',
                    'internal',
                    'configuration',
                    'internal',
                ],
                'source': 'ƖњүҽŨҊҁiҡӃķę˩ˆ°Ȥ¼ҞέİΙɈϝi·ҙδʊŲԖ',
                'corrective_action': {
                    'catalog': 'ө\x9fȔҺϵӒѿX\x8abԓΞͺҩѧҲπԢѓËǻƙĠ°ŰƞǤɯДӆ',
                    'message': 'ӎУĹȍł˥ɣ˦ͰȣǢЎůǡϙȍӓϵǆĲʤtҌʣͼɐȪǫқΈ',
                    'arguments': [
                            {
                                        'name': 'шŞϒAˉŚˣӷηЊϴВùѝŊԢǒʳfˎíqɘûqԊԔŴѺж',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6489840766885722816,
                                                                            -1283582735808325301,
                                                                            2569374005800629667,
                                                                            984564855127388588,
                                                                            3148940753564726314,
                                                                            8022088641645626525,
                                                                            819536059105123135,
                                                                            -930333917718960884,
                                                                            -1281147158547377573,
                                                                            -5507072447171936919,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ļ#ƝğԍѐĤ͵ɜǘϤǷƼхƿʭ˛ȯoѮɷςȢŃ\xadÐÃĦǼ±',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165056.671233:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǴҞăǹҗĳɸӹԜӎƂɯ\u0383ȓΪɂƯϱ\x92Ȼzӏ1ω',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165056.671571:+0000',
                                                                            '20210212:165056.671639:+0000',
                                                                            '20210212:165056.671659:+0000',
                                                                            '20210212:165056.671677:+0000',
                                                                            '20210212:165056.671697:+0000',
                                                                            '20210212:165056.671714:+0000',
                                                                            '20210212:165056.671729:+0000',
                                                                            '20210212:165056.671749:+0000',
                                                                            '20210212:165056.671767:+0000',
                                                                            '20210212:165056.671831:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˇƻăäԓѕɹbɲϜǲƓ\x85+ɸ»ɄƋǑάЛǴVОɗΩҰ\x85ѠÔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 342903.4706287412,
                                                    },
                                    },
                            {
                                        'name': 'ӹШȈǩɐ«Ԑǹįӊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165056.672720:+0000',
                                                                            '20210212:165056.672737:+0000',
                                                                            '20210212:165056.672745:+0000',
                                                                            '20210212:165056.672751:+0000',
                                                                            '20210212:165056.672757:+0000',
                                                                            '20210212:165056.672763:+0000',
                                                                            '20210212:165056.672769:+0000',
                                                                            '20210212:165056.672774:+0000',
                                                                            '20210212:165056.672780:+0000',
                                                                            '20210212:165056.672785:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѹʩůΘǴŰªЌ҆ȹӛɔô˗ΪƵ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɘΒćɡЩȒŵҕĩ¥ˁƆŮlӧϭϢУ\x92ȠΔЍ¥ŕƩӧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '±ʶʫӪȒɝQӓ¿jƨƯņΛÑҠƴÎʼ˒%ċΏēԄŝҍͿnē',
                                                    },
                                    },
                            {
                                        'name': 'їҹşіg"ҸɃФԒѢѠZͰҼ\x88Ō',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1926208171864117323,
                                                                            2589675525366590444,
                                                                            -19085141675275178,
                                                                            -4689488602066489724,
                                                                            -7949383462714050106,
                                                                            -313817270309746104,
                                                                            -5013150523211859642,
                                                                            1127993914958009931,
                                                                            3218759281532589378,
                                                                            -3213979118708318772,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'żǔsѧ˛ԈĹΗǼÏΊŎ%ьώΠё1ýӸÄӖҺŵÕǐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 832866.0484072721,
                                                    },
                                    },
                            {
                                        'name': 'ȑȥ˴ƚňďʣѾƓƶʹǿгҟϠЅ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165056.673695:+0000',
                                                                            '20210212:165056.673709:+0000',
                                                                            '20210212:165056.673717:+0000',
                                                                            '20210212:165056.673723:+0000',
                                                                            '20210212:165056.673728:+0000',
                                                                            '20210212:165056.673734:+0000',
                                                                            '20210212:165056.673740:+0000',
                                                                            '20210212:165056.673745:+0000',
                                                                            '20210212:165056.673750:+0000',
                                                                            '20210212:165056.673756:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'Tǡ\x81\x9a\u0381\x8dͿөЖ\xadʓƷȥԎɧԘȎɲΝƖŰÀʺгȖҨЭnΆҍ',
                    'message': "ƂƔԣЋҮҺ8ĹŹ'ƲԣİŮƺͲԇȈȥЭ¡XҬĭƘʆɶԠƘб",
                    'arguments': [
                            {
                                        'name': 'ŋҿ;ҳԔĭ«ԚǒŏʯÅʾŘøȫǰŦˊФƥ˔ͻśԈ˹',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2814423818639411004,
                                                    },
                                    },
                            {
                                        'name': 'ԦҨͱ\u0382ȸЄМӛҵǧŷʔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            615658280235074819,
                                                                            3384007571775504841,
                                                                            544656778997428475,
                                                                            -5802498743838630259,
                                                                            7892828960961275975,
                                                                            -7139539884120105204,
                                                                            -321661706881213487,
                                                                            9000042548753009714,
                                                                            -4733157337423143210,
                                                                            -5460751145245322112,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'όƥОϽΏъҕĈϧѩȄĈѨƉǫ˼ɛӮ³ϴê\x87<Ĳ˻ʹ¶ϫϋώ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165056.674603:+0000',
                                                                            '20210212:165056.674615:+0000',
                                                                            '20210212:165056.674623:+0000',
                                                                            '20210212:165056.674628:+0000',
                                                                            '20210212:165056.674634:+0000',
                                                                            '20210212:165056.674640:+0000',
                                                                            '20210212:165056.674646:+0000',
                                                                            '20210212:165056.674651:+0000',
                                                                            '20210212:165056.674656:+0000',
                                                                            '20210212:165056.674662:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ßňϽÌʭŚ͵тӅ˂ɲтÏı9ԦҺüɡȮϋÚɥѓͷ˜ЯƗћŧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1000049725457662125,
                                                    },
                                    },
                            {
                                        'name': 'єȁįԔͻϖҴԔâYʥȝЬȐʌƲŮҌʁϙQŰϝмӢΒҮɓǬʠ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8051887862798758615,
                                                                            4537033921449103590,
                                                                            -5691506115092318441,
                                                                            976644248243035159,
                                                                            5974024916767916006,
                                                                            -7514363083423523702,
                                                                            -1049807149660413682,
                                                                            -5130267400746191186,
                                                                            8450888351221791121,
                                                                            -6925465685713616533,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΩːΊњФŤԈ\u0383ǯԇҌį˜҆qΏĉƎʹǘüɻ¿ƏƩĄ,ηѸɂ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165056.675232:+0000',
                                                                            '20210212:165056.675243:+0000',
                                                                            '20210212:165056.675250:+0000',
                                                                            '20210212:165056.675256:+0000',
                                                                            '20210212:165056.675262:+0000',
                                                                            '20210212:165056.675268:+0000',
                                                                            '20210212:165056.675274:+0000',
                                                                            '20210212:165056.675279:+0000',
                                                                            '20210212:165056.675284:+0000',
                                                                            '20210212:165056.675290:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'A',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            954462.6205330694,
                                                                            686194.2189996759,
                                                                            4965.55658492654,
                                                                            385622.86884500366,
                                                                            -15666.619208332457,
                                                                            -92301.96479072262,
                                                                            99024.76238219396,
                                                                            392090.27974365605,
                                                                            262276.67075382586,
                                                                            -4644.829562020663,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŽΑƠǬɀЂʆϴнʒѲɀǒѠĒÑʁƐΣ(WБ˰ӡɳ\x96Q\x9bȃé',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŗԮʝАҿΈȫɴΔǆɽЀѢүΘîŘ_ŹÕ϶˯ŎӁÍªȯƑβʉ',
                                                                            'ĚœˆμДԩУȇʻĜϩǶͱѥΈӜВʏƹѮгЦƭ?ÝьҤшΊϖ',
                                                                            '˨Ώ ?éȊƈтИФĸɯɾϸxӂҐҜӔӮϕƳ¤ɑ6Ȃ}ӪΩɭ',
                                                                            'ӒСnŒʦҵɲǡѵφι\x92!ǱԡԮɪ\x9bϨ\u0380˖}öƚǅҹΡј}ξ',
                                                                            'ƆɨȨ\x8aǉЩϘӵλϯǱ;ͰGΨʁĨ¦Ԙ\u038b\x9dĭӸϸ˰Ʊ˂Ͽóʹ',
                                                                            '8óЦѠ\x7fĶȆԟǥϕǍ\x8cȶžÂ+ϖЁҚ3ƇˁчˑӣȈΐԕˁų',
                                                                            'ӑԣ=΅҆ϊŏę˒ЕяƘŸBĢȌҩî˜ΖǖĖΤΦҪοŵǝϹԐ',
                                                                            'ЕsİɗɴЁӍϣNĐ˱ϩБȟʟxűƵ˳˕ѸԨцΙɗ҂ˁЀӋˣ',
                                                                            'ԁ@ѓшȆԔŲϭˋˍȥȟċÖΨЉӍΙǬƈĚǁʹдϘÙӹΥӧƏ',
                                                                            '«ğ˪ƨαӏ˗ѺγoΩBȕ<¸ōƦŐƈͰ҃śŬӶȥõѿ±Ǟƨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'һ˜qѽİϚӳӔƃϦʜɁΑˊ´+È\x87ϼTσȗЇяáԚӨӑӛȺ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ùϩа6ХƇɖҜӉɰȬ:ϛ\x81ťǃʞԅŹǽβɡ\x989ǟŀʞŵʔƚ',
                                                                            '»ďτʂӪāàóҀɉэеqΩϕӶwɮӣƶҩσĽ-7ȍѳέǋË',
                                                                            'ϸˏ©ԫϔˑϥĿŶ˚ӭɧΉКͷрЁ҃ΝҙȒǷćѺП҅ЗΊƫϥ',
                                                                            'ìπǲ£ê¢ķӧɉ˭Yǎˑí³ЇӒϓѰΎg+@ʦԦÑʗăϑΌ',
                                                                            'ͲғǿƎǃҋĄŕӄň\x88ћͷҸŵӤʪьƭԩʖǿТo˷˓ȿfТǅ',
                                                                            'ÌÀ^ҿ˱ǞΨϾπūƆğƴΪ«ȸoɶ˦ңӧÄǫ˺ҬǥȶĩŜ¶',
                                                                            'ӚѬӧгӢʕхόɣΤѷĥӷǼщsѩʵԊĥӬƽÃȫƧLÜϋёΫ',
                                                                            'ΣϴӞƸçſ8˂ˑοҫϪĵϣǇʞǷϙ\x9eЪчʏƑʜѦЧӚ¼½Ο',
                                                                            'Ѿ\x95Ǽ˻ΛĊ¤hӻԛӈѪ\x8a\\ŢÐ҆ΪȆƈ×ƪкϫĘǱīʄʼʌ',
                                                                            'эȿɶǶ˳ǨǐƵɡɸѫʊƵeϱĚȴйѣ˒ʩүÄĺ˛ˏNþГʘ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '[ˍǦC˶ǗϘлŔǗκȄϤӒѽʞˣȞѐзĥԨɸϊӊҧǧƥŽ/',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƮɮʤŏɨӲɫªʭʎŶҰǒÒҩß\x82ԎʒϚǟÔ\x8dѶɪ˅\x9cПːԛ',
                                                    },
                                    },
                        ],
                },
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'error': {
                'identifier': '\x9fŷӿØă',
                'categories': [
                    'network',
                ],
                'error_message': {
                    'catalog': 'ѓL',
                    'message': 'Ǝ',
                },
            },

        },
    ),
]


class SetLocaleEventTest(unittest.TestCase):
    """
    Tests for SetLocaleEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_LOCALE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.SetLocaleEvent.parse_data(test_data)
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
        for test_name, test_data in SET_LOCALE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.SetLocaleEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_LOCALE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='SetLocaleEvent'),
            ),

        ),
    ),

]


SET_LOCALE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': 'ʎԋͶùʟЗĝē',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'S',

        },
    ),
]

class RegisteredTranslationCatalogTest(unittest.TestCase):
    """
    Tests for RegisteredTranslationCatalog
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTERED_TRANSLATION_CATALOG_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisteredTranslationCatalog.parse_data(test_data)
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
        for test_name, test_data in REGISTERED_TRANSLATION_CATALOG_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisteredTranslationCatalog.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTERED_TRANSLATION_CATALOG_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog_name', name='RegisteredTranslationCatalog'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_codes', name='RegisteredTranslationCatalog'),
            ),

        ),
    ),

]


REGISTERED_TRANSLATION_CATALOG_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalog_name': 'ǈEӠǀљăɸ˺ν~aǌӯɈϙśͷKä˅ÖӻùЃ|іĢā\x98ώ',
            'locale_codes': [
                '˳ȞýĻͲ',
                'ɶ\u0379оɀќʲϢƞȯŐ',
                'ɦ',
                'âԚȡS',
                'ɃӁЍӅͰϕʶнД',
                'K',
                'ǋ҆ЅӪϱыŏԭ',
                'ƓƎңŻԉ',
                'ǵ/ѵˡ\x90Ŏč ',
                'ē\x85Å¥',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ˀîȴ',

            'locale_codes': [
            ],

        },
    ),
]

class TranslationsStateTest(unittest.TestCase):
    """
    Tests for TranslationsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in TRANSLATIONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.TranslationsState.parse_data(test_data)
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
        for test_name, test_data in TRANSLATIONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.TranslationsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


TRANSLATIONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalogs', name='TranslationsState'),
            ),

        ),
    ),

]


TRANSLATIONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalogs': [
                {
                    'catalog_name': 'ɝϲȦČŴɧǷϺцӛϜƉӿĽфќɳȇʥɽŖˋʨoΤġɷΎюΆ',
                    'locale_codes': [
                            'ʰ',
                            'iǤɹ_ԌϾͺ',
                            'ѻʘťԓɔ',
                            'Űɤſϩʡ',
                            'ÁʋŌǇ\u03a2ΰ',
                            'Ȯʩfϻ:ŀȵ·¬Ю',
                            'Ȼ"ӜӋӤʹÈ',
                            'ŗ',
                            'Ūǖ\x91',
                            'ǴK˸ӱ',
                        ],
                },
                {
                    'catalog_name': 'ʺ9\x91ʺ',
                    'locale_codes': [
                            'ãјĴ',
                            'ÒӉҹһŢ҈Ǟ',
                            'Ӯ',
                            '>ǽƏ˙{ʥƢҗŋ',
                            'ʾҍͳΥȎΟ-Ȱ',
                            'ƩκɌĪТԀИӔӼǐ',
                            'ӐʉSɠ',
                            '&ԥϪʖ',
                            'z\x97ǠćŃѸ΄',
                            'ŭɊγ!ϡŹDѼĻŹ',
                        ],
                },
                {
                    'catalog_name': 'ȁЦɪǰϴ˪V^ƆøŧôѰ˲ѳϝҨƐŪǶԗӰϹãĊԖΝčɠӘ',
                    'locale_codes': [
                            'уθd',
                            'ӚǘΩɱɻ¶ԒǱѦ',
                            'à',
                            'ǻϮ\u0380ȞтƦɺ',
                            'ў2рɽʕƇerӥ',
                            'Ĕӏ',
                            'Ψ',
                            'ćИȒˈ',
                            'Ñ',
                            'ƆA΄щ',
                        ],
                },
                {
                    'catalog_name': 'ΓøȼѪƆ˺\x9bBʋȟʖъǃh˜ƮŰѩʬǙģĂȦMɩ\xa0ԉӏ§ъ',
                    'locale_codes': [
                            'Ƴ',
                            'σȸɞÚЂΆ',
                            'ԃɷ',
                            'ёƤѫͷˎ',
                            'ɬƶȴіʃѵǇєġͳ',
                            'ϠʥƆҊ˅ş\x82',
                            'ԃɒέͷˠąϯ',
                            'ŁS',
                            'ԌʶɎ',
                            'ÇŚ˽ЕӪď',
                        ],
                },
                {
                    'catalog_name': 'ϐѥýǙȴϸ|39ŃιȚȶâaȁњ«Ѯ)йK˃ҟΒЊǠ\x93ʬʠ',
                    'locale_codes': [
                            'ԮЌя',
                            'ǨѴлԫ',
                            'ˉĩҢ',
                            'Гѱ˟P',
                            'Ҳ˚ʯķǵʢ˗ǝƵǂ',
                            'Ѻ',
                            'Ơ˩',
                            'ɹƄULIɞſІʶŸ',
                            'cȶ',
                            'ϋϥŢБϚƫ',
                        ],
                },
                {
                    'catalog_name': 'ϠˌԏΔĎ{ҏПА˚Ö˦яǗʬ´VWKŖŋ^љƭȄтΞĽʫɱ',
                    'locale_codes': [
                            'Aϐǿ',
                            '<Ԏ',
                            'ςѶ',
                            'pŬös͵Њʪ',
                            'åĪƎħȖÃÖԧKɍ',
                            'ȘԠϩ\x8dɀŀ',
                            'ȹ˞Ĕ',
                            'ϑцғ',
                            ' °ZºǮGȄ',
                            'ε',
                        ],
                },
                {
                    'catalog_name': 'ϵѪĪϊϋùШ¤ӛҍŃȻˠǊөĊʀřƫĉɈʰǩТґ',
                    'locale_codes': [
                            '͵àВqʛѤWȏƔ½',
                            'Ƹʽȁʧi˘Ҥƻ',
                            '϶ʕϕˆȦǯƧ\x9e',
                            'φΌ',
                            'ŉ΅3',
                            'ɸ΄Ѐ',
                            'ǅԉϪśŽӭ˔',
                            'ѸͿ',
                            'ƟϰӮʹζʏŵȅŔ\x85',
                            'ʑғǴċ',
                        ],
                },
                {
                    'catalog_name': '\x89ƁЦdÛˆİ҅řņθЧԠΐĀЇȎˈȍžù¤^ÎʅΡΟʷҖԐ',
                    'locale_codes': [
                            'Ĭ',
                            'ǴтÈŎɚҾ',
                            'ȨǙҽ',
                            'Ƒи˂ҁѫыoýӧ',
                            '¿ŠŋƒºǇÔɘů',
                            '(ǋ\x9fϊ',
                            'Ԗ',
                            'ºˇ',
                            'ФӈАɼȲ˚Ƞѐ',
                            'ıļɶѯϙ',
                        ],
                },
                {
                    'catalog_name': 'ҨҡҞҁϩǅ΄ҹǫ\x9bɾƐԅ´ɕоƾ½ΉFēRȫЖǍǾ\u038bϿʃΉ',
                    'locale_codes': [
                            'ġӐǙ',
                            'ȴҨԜź^О',
                            'òĸϸʴ',
                            'УÊ`ɞ϶ÑщБӗ',
                            'ыəԄ¢Ӎ',
                            'N',
                            'ĊΩAˊʴs',
                            'ϗĒԥ',
                            '»ûƛŃþєҵ',
                            'ѵϝɴȶх˧*ũ',
                        ],
                },
                {
                    'catalog_name': 'ċǟwɹ\x9eѹŢĉŻйŲȪǄʹ\u0380мЫƻĊżЊзӇҕŇЋДӔɯǨ',
                    'locale_codes': [
                            'ϐG~ʖµ',
                            'пњœʐϋιˬω',
                            'ãSŉӖӣ',
                            'ǭϧͼŁ°ȡȻ˶ɇ',
                            'ƹ¨+ˏΛ',
                            ')',
                            '˨Ə',
                            'ʡǢőˬ\x9fӟ҄ǭ',
                            '`_ϷҸ',
                            'ĶСЌ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalogs': [
            ],

        },
    ),
]

class LocalesTest(unittest.TestCase):
    """
    Tests for Locales
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALES_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.Locales.parse_data(test_data)
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
        for test_name, test_data in LOCALES_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.Locales.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALES_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='Locales'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='code', name='Locales'),
            ),

        ),
    ),

]


LOCALES_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ё!Ÿȹ\xadЊӦȭƠĝЎǚъϢȇԅԄǋԚŏl˄ӤqǲδōѨЇƏ',
            'code': 'ɉ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ȼ',

            'code': 'à',

        },
    ),
]

class LocalesStateTest(unittest.TestCase):
    """
    Tests for LocalesState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALES_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.LocalesState.parse_data(test_data)
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
        for test_name, test_data in LOCALES_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.LocalesState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALES_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locales', name='LocalesState'),
            ),

        ),
    ),

]


LOCALES_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locales': [
                {
                    'name': 'ŅҪtԠςčɏ\u0381ŊЅŬĤƞɄѐƔȵӊȪΙлɛϋƩƋǜη¢ҦW',
                    'code': 'ƝǾҨϯŒãɨ-ȃ',
                },
                {
                    'name': 'ʡԗġќνPŶΥvsǯ\x8aʀӦĪˉšҍƺҩĠƂǾȯɢЊһ˔Óˍ',
                    'code': 'Ϙ',
                },
                {
                    'name': '˭˶Ëʟгёȹ+Ϛ*ˊʢʐѲƊΎ҆Ɗѭ\\®ɯԮӤƣÒěǆü˥',
                    'code': 'ԜщѶ',
                },
                {
                    'name': '¹ΤδСҮӣ\x8dʶˢɾдϖʐƴϖзȭƳХƜԓƦԫұoҜ=vўҳ',
                    'code': 'GŜ',
                },
                {
                    'name': 'ԗȸ³ɛĹʰʞĿěωʭēЦÅ˟ʬŹĹ« ΦϹ&ȢˣϏҐӓɆи',
                    'code': 'ӛҵī҆Ž',
                },
                {
                    'name': 'TԔyÆǺ\x9bґƴҖəzÔӠŕśűҭѭƍӯГȚԎѿÌрȝĎǿЪ',
                    'code': 'μͷө˛!ÄÁÀʻ¹',
                },
                {
                    'name': '҄˼ǻTԛžΠȌȑŅIҍ»ϲΒVҿԧ]ȜɳԇʰlљҹΞŇѣЏ',
                    'code': 'ΪǪΉʴʇv',
                },
                {
                    'name': 'ˡĹԁҦɪ˂ƚȹϷȕҋǱȽɞґџт\x8dŢΟͻӟϛҐӖӁ\x9fθÝō',
                    'code': 'ϮҼ',
                },
                {
                    'name': 'ɦǝшZăίɮȿ]TĉґƧ˸һˎɎŧԖAƁ&ʟˏъǕΡӯ2z',
                    'code': 'ʥËҥɯĺȦΟ¾˵²',
                },
                {
                    'name': 'đĞǖȫʍӪѤɦϬ»ǇƂ¡ČĘÛjԦӑÖ\u0381ԧѠŧͱʊΟĬјo',
                    'code': 'ƶԖԟҚҲ˽ү',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locales': [
            ],

        },
    ),
]

class ActiveLocaleStateTest(unittest.TestCase):
    """
    Tests for ActiveLocaleState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_LOCALE_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.ActiveLocaleState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_LOCALE_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.ActiveLocaleState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_LOCALE_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='ActiveLocaleState'),
            ),

        ),
    ),

]


ACTIVE_LOCALE_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': 'ĄÕʺN',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ƾ',

        },
    ),
]
