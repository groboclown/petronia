# GENERATED CODE - DO NOT MODIFY

"""
Tests for the l10n module.
Extension petronia.core.api.native.l10n, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import l10n


class RegisterTranslationEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = l10n.RegisterTranslationEvent.parse_data(test_data)
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
                res = l10n.RegisterTranslationEvent.parse_data(test_data)
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
            'locale_code': 'ƴǰˋ',
            'catalog_name': 'ϩ϶ͳƩĨĚȵēȖƽӒ\x8dťéȊ!ƮʒƘ_ПɠŖȜɅѕΚͻʻǀ',
            'message_file': 'űнJȡњёȓѢʝ`ŞҾĽҋ\x85ɍϢӘӖ\x94ϦΡҲpĮȱМͼ˥ƺ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ŀ',

            'catalog_name': 'ˇ˾ϋ',

            'message_file': 'ƃԠ',

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
                res = l10n.RegisterTranslationSuccessEvent.parse_data(test_data)
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
                res = l10n.MessageArgumentValue.parse_data(test_data)
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
                res = l10n.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ËӾ˸/ț´\u0381ԌǹÇҕ\x982ԪÔͳãʌɚr\x8cϧϿMßŃô˭˙Ɯ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5874278386225450505,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 150416.43880868488,
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
            '$': '20210909:201238.916332:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ǸƕȩàщϋυΉ¾ҲÄ{γͰѿ¤ьÆҳȒ˰ñǵ¹ÉnΡɽ!Б',
                'Ͻ;өųʚҮӜ˜ǌʦьŻϊӇàԄɪԬҪоͿͽʵΠΘԟ\x91ùͰË',
                'ϖƞðȩɂNʢπχҮƎŅìƌRŃɌӚĈȨēѭҴśĝϨÖѣϪŊ',
                'Ȋɚɘ\u0378ӳíӰԞƁʦѕϸˏӍÿ\x95èюȰǐ8ȢҽoņҦцғŷŃ',
                'ӇԕªȟʾŹˢɾAĔғȐѳѕψtʹƛǋԮğŗϒ˄ǻěʫԀȵŦ',
                'ɮȀŠͼɻƑūкǣ\x81\u0379\x96\x8fďÈґƶԤɘӃ»ȤϴȉVԃ\x93Ђúȯ',
                'ӐǺҥʧƷɓ½\x96ǑӘūӪĞԛBϾ/ԀŌʰʓԞˁл0"ϥѵ^Ӕ',
                'ĺОôҴĚǻǌѠʧΦɯðÇɯ¯Ѻő£ʺϩӳѬ2ɘϐǦƽҗ»Λ',
                'Ԫǟ\x9dĜăуˬэҕɒŔЧŻƸʸ˸ǖɢԗÿ+ҎīĂЗԑ˲à!Ȇ',
                'ҽ\x8eтǨԧΜ\\ΧɀҠˎ\x82˦ӥɥÌοƔǰƅοƛ˔Ɏʅ\xa0ϳч˔ȶ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -635727750611111526,
                4576593722352871119,
                -1707627447064889081,
                7534171554337969528,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                404729.0119577142,
                865178.7165988798,
                821906.3940670103,
                700213.7902231264,
                75325.05987865012,
                620607.0595580977,
                193651.01149814564,
                -19429.742569676964,
                414853.4165850149,
                833420.8297632062,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
                False,
                False,
                False,
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
                '20210909:201239.752531:+0000',
                '20210909:201239.769302:+0000',
                '20210909:201239.785805:+0000',
                '20210909:201239.801616:+0000',
                '20210909:201239.817242:+0000',
                '20210909:201239.833782:+0000',
                '20210909:201239.850194:+0000',
                '20210909:201239.865967:+0000',
                '20210909:201239.882224:+0000',
                '20210909:201239.898156:+0000',
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
                res = l10n.MessageArgument.parse_data(test_data)
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
                res = l10n.MessageArgument.parse_data(test_data)
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
            'name': 'cØҸΨɿżŇ\x89ӊȢ¡ШзşœχԪɧƧ˜Ƭˏ,ȌǦjӖҰM¢',
            'value': {
                '^': 'bool',
                '$': True,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˚',

            'value': {
                '^': 'bool',
                '$': False,
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
                res = l10n.LocalizableMessage.parse_data(test_data)
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
                res = l10n.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ǬϊéέȰμƽĈӅΪ\x92ÍĘ˟ԆÕΖѨͽԌΕɩȹϴŴԅҽάˬɝ',
            'message': 'ŎpǾӺȢʹͱ´ºƀ,ύŨӄǅȹƜѐҾÖɁđȫԉǣʈʙϸˁЪ',
            'arguments': [
                {
                    'name': '}ıϾùƽʷǉӷӢ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        False,
                                        False,
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
                    'name': 'ӋƐZŎцlXάӳĥͳĢѕ\u03a2þ;Ļ\u0380ϜūΏǴ˰ʁθőԫɠfȏ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        135295.78484534135,
                                        445868.3683685255,
                                        479389.3983700387,
                                        994883.3395145885,
                                        679719.6306374647,
                                        79918.71093563607,
                                        891637.9637838226,
                                        837434.581699686,
                                        68511.52634209613,
                                        229109.44464496186,
                                    ],
                        },
                },
                {
                    'name': 'ǻ',
                    'value': {
                            '^': 'float',
                            '$': 175686.97601471446,
                        },
                },
                {
                    'name': 'ʚüɀʯ×ȫʓʡƄȪ˽\u0381гųΦȯӜOʵƒʧ˒\xa0ѣĞһǰЂˉ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210909:201237.913375:+0000',
                                        '20210909:201237.929605:+0000',
                                        '20210909:201237.946843:+0000',
                                        '20210909:201237.963101:+0000',
                                        '20210909:201237.980181:+0000',
                                        '20210909:201237.996929:+0000',
                                        '20210909:201238.012599:+0000',
                                        '20210909:201238.033257:+0000',
                                        '20210909:201238.050470:+0000',
                                        '20210909:201238.066163:+0000',
                                    ],
                        },
                },
                {
                    'name': '˳ѽ¶ʲԙNѿȊɐȍˌÉʐϧԄӋЯ',
                    'value': {
                            '^': 'string',
                            '$': 'Ɇëǽņʝˈ\u0380ӎϏͶȋɕғΌɁҖũʳϺyĥΡƹȔʙYЏǋͳϴ',
                        },
                },
                {
                    'name': 'ʰҜʦȤчǓ˨ìĻȄ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'чҎĭŸҭϴ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '¥ҭÂғŉɅ/ζҖLȡ\x99ԓԥͺίѦˇŐ˭ûė˳Ӄƺđʔ\x88Ýà',
                                        'ѱ\x90ɶƭͺˉˮı¥\x92ҎϣɺǐKсʊѴƉ·˺ӜǾ\\\x9aú¬\x88Čǥ',
                                        "'Ţ÷ЇυįĞBνǴԩӚγˉǕɗÃzʄΉȦέbҡ}қԏʾȱӗ",
                                        'ŅЅόƷǡëĠԃʤǻϵʛμДÆîҤ\x89¬ʬςϺҶűФÿēРġɿ',
                                        'ӚµҎĕŬƇõΝКȌɹǜρȒϥϚӜ˺zæ\x82Ŋx>\x98Ϸƌ˵лʶ',
                                        'ѤǄѠÀȠϞѱ\x99ӳʏұЌˏǷďGQԬĩďc˰ԟ˷юȈҗÉÔȆ',
                                        '\x91ɯϓжƎѕƃƀȢĒԅǚŜßşǂ˓ӺŢIˀАԍԪrұʔӁē\x8f',
                                        '\x7fɁê"ωЬǽј͵NɺΙӹ˷˙ȑπ\'қįƋUʜԕқрȝҩӛ÷',
                                        'βˌʈϔˡĦН>ƢǔGɀĦÄЬͰ˧ρΒĂƾΫҜȡɒŘųGQЈ',
                                        'ǐɹʢŵԖΙɒӛϔшΛəҀ˄ʱԓмДĄ\x99Ӟ˛Αx¶ƋɸƝĐɜ',
                                    ],
                        },
                },
                {
                    'name': 'ĠηцĒ&ˀeíÙŒȑåӯ%ȁѮѷʹҴǐúͰŲɀˁ˙ʶɒ\x98Ψ',
                    'value': {
                            '^': 'int',
                            '$': -404255818077437252,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ț\x95',

            'message': 'ƶ',

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
                res = l10n.Error.parse_data(test_data)
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
                res = l10n.Error.parse_data(test_data)
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
            'identifier': 'ŨíϷȮНфĿƲȨ͵ηсĴɐpӳ|)ÿÞƮÕӽͻіΫфԒӑѓ',
            'categories': [
                'os',
                'access-restriction',
                'configuration',
                'internal',
                'os',
                'network',
                'os',
                'file',
                'access-restriction',
                'access-restriction',
            ],
            'source': 'ЩńĚƕӸ\x84âЇƀɗʩ7ӥƙєĀģȗĮɕʺȻ\xa0©HƼͿʤ҈ÿ',
            'corrective_action': {
                'catalog': 'VЮΛΛԅŃ˟ŪЬ=ίQϙӉÄ¢ωҮĸҿΏǓ,ӇЀÐʤγɉů',
                'message': 'ԖѦ\u0378ʱ˦ƑҔѩα8\xa0ďҽʭύԐʑƎϝЋŖƦƯҷӣŇТƨǳԧ',
                'arguments': [
                    {
                            'name': 'ǵïϗȍɫȰ˾ӌ\x8eȱʥеҗɹʺɂĵ΅ʫүé˃ÚОЋ˛',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        953568.909884529,
                                                        817842.3605067938,
                                                        165411.36438726704,
                                                        58706.51883858931,
                                                        728530.8066676833,
                                                        249996.50767718366,
                                                        674087.794429416,
                                                        271117.23459040624,
                                                        127246.34235123114,
                                                        185866.0357091999,
                                                    ],
                                    },
                        },
                    {
                            'name': '!ѝӅЅ',
                            'value': {
                                        '^': 'int',
                                        '$': 6690331381154167091,
                                    },
                        },
                    {
                            'name': 'ĤɵԕÆ˽т˟ÁʞɂˏȆξθœƞƴbўƪȓԇ63ƛɹ˶Jҡ˺',
                            'value': {
                                        '^': 'float',
                                        '$': 504944.90603935067,
                                    },
                        },
                    {
                            'name': 'ΕIêԓPǘġȒχҗɓҲŜҏɵμiТЉĻǆʀÚӯʀ"\x7fɻɐŤ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        27000.39511949329,
                                                        343484.69262646337,
                                                        244907.84519563545,
                                                        460287.1121819692,
                                                        -7381.91666079135,
                                                        352803.8380182359,
                                                        416973.1750934852,
                                                        -49630.557438747135,
                                                        715053.3071922829,
                                                        31638.478443116677,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΐșҳˍ',
                            'value': {
                                        '^': 'float',
                                        '$': 422571.66438126075,
                                    },
                        },
                    {
                            'name': 'Ώԧ×ѕ¼ƊƢ͵ǪЃěǵϝɂхǪaȸŸ\\Ȉɗ˪ЋΜ+ʡЯΏѬ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'Τ',
                            'value': {
                                        '^': 'float',
                                        '$': 409502.4945429001,
                                    },
                        },
                    {
                            'name': 'ŽΉΥ]Ļνɫō',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -500435488897734909,
                                                        8652091745878608867,
                                                        2328006012788881312,
                                                        4616245440454826875,
                                                        8047088415623380372,
                                                        5859658299917329772,
                                                        -5998111526287370196,
                                                        8600454350063713184,
                                                        791550721769697311,
                                                        -8448103132106382420,
                                                    ],
                                    },
                        },
                    {
                            'name': '\x8dЏ{ȆɷŗΚҤȵƄԓʖ\x8fϓʌўǲɑϙ\x8fă\x8eƥĄ˗б҄ɐĢǾ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        871762.910572708,
                                                        75129.17830023557,
                                                        122416.27194983343,
                                                        59135.82001804281,
                                                        386621.6817331631,
                                                        6202.30664182076,
                                                        55622.461583773285,
                                                        342748.37614439614,
                                                        869823.3280405028,
                                                        468934.05035213893,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĻφпLɉôŇҳƘˉȮҿńņҕȀȼĉÅώĉ<',
                            'value': {
                                        '^': 'float',
                                        '$': 751742.3459301356,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ȳЫū\x97ӟӯӼϊėʯǋηԡɜԁΊċӵǽк¹ϬəĨҤ¾ȯмӕȾ',
                'message': 'ʓ\xa0ňŨˢȵÊ»ƅǏÅȓƜż\x9cӉԚ¶ԚO)οԉŤӍƜӤʩāƞ',
                'arguments': [
                    {
                            'name': 'Κ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'βӃĎ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ƌ4ҠʦĥƣȃäɵxжԒěȽ®БԨөƼŀӾˆŦ\x92Д5ϿȥʫΏ',
                                    },
                        },
                    {
                            'name': 'ĭiψĄӭˊƥ',
                            'value': {
                                        '^': 'float',
                                        '$': 105443.70575349717,
                                    },
                        },
                    {
                            'name': 'Д˟˶\u038dԞӑǏҵÕΧЭ˹Ⱦυì6ĿŗľÈ˂ІōѺӅɩɎƃѯŴ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        117912.20509034445,
                                                        136845.71127712313,
                                                        314756.7961183577,
                                                        862624.3494496669,
                                                        110647.80171579454,
                                                        480595.15187196515,
                                                        728281.8507475496,
                                                        735379.7157659942,
                                                        92624.92037774218,
                                                        795249.3021685694,
                                                    ],
                                    },
                        },
                    {
                            'name': '/Ө',
                            'value': {
                                        '^': 'string',
                                        '$': 'TѸԝP\x98ӪˢŸĬɦѻċΓԖѪͲĩЖʏ0Ȧά+ɀСɕЕϸ&ɷ',
                                    },
                        },
                    {
                            'name': 'śƐԇ\u038bȍ¢',
                            'value': {
                                        '^': 'float',
                                        '$': 506821.343975367,
                                    },
                        },
                    {
                            'name': 'ƴKŢĖKҞó҂ӈ',
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
                            'name': 'õCҡƻ\x8cфíʊ³\x9c\x9fƔ·ťƝĢÇ҈ӻӴyĊϓŐêў\u0381ŝӇļ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ҧņӮϓƷʥЃ˾Ȑ\x8dҤƛmÚȬº\x81Ќ*ԑĩѩçӾAԔϝƩàť',
                                                        'ƿȤĴďӼ˛ҟԚьδЮҿƏŎæʹ\x96ÿԫúƁӾԧ˫ӪɔϔӭλΣ',
                                                        'ъҧІȥƹǛȒұѳƑ˫ԍlΌǴʹĈή˧ɓ~wƜˁĒ¾αƆǒʕ',
                                                        'ӧͷŰѽŷeɆ;xȅşԔûʳΩb\x9fɀťϙЮгʕĄͲҚ˸˰_ƥ',
                                                        'ϴ]Ѝ\x8blѱȁԧϐѢ˼эгLΒɑɺҙӮƼèÊԃǮБƥʿҩШ҅',
                                                        'ƵŦӂĳӴ\x98ŞѢҋ\xadӼĪ¡ѠшŊΏƆҹϸʳǣĩ³ӟϯԫҡ˩à',
                                                        'ɹƻɄѦƱ\u0378ҀɪȊӤϪҢèʶ\u0380ð¯эӶĬѣǠ˳Ζ9ϿфǦύӦ',
                                                        '\u0378ɧȷİǦjʡСă˞UҚnӵȳȴ˄ǨԇˊԣѫʺуσҵΪҪŭж',
                                                        'ϸ"ΐʘԏƝȘÓĲǓºϟѮԖūШǰЊҲϖԄӑѣϘӎϗӎŢΜч',
                                                        'Ǫ¥ŲȓȡʎӲӼҌŷȅҌŹɅҵĚÈĀŇЖәħ©ԔǭДςω\x81ӹ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ГǇǑħԤćʎÆΰǽɯțǚϨªIˎƱǸƤԎӯ˾ӮЬǗ\x96ǠƖÉ',
                            'value': {
                                        '^': 'float',
                                        '$': 757519.3050634635,
                                    },
                        },
                    {
                            'name': "rΎ\x99˞ŭ»ƁrɮÀӀ'ȢPњŢǓкƮ",
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210909:201241.323365:+0000',
                                                        '20210909:201241.340122:+0000',
                                                        '20210909:201241.356508:+0000',
                                                        '20210909:201241.373987:+0000',
                                                        '20210909:201241.390982:+0000',
                                                        '20210909:201241.407482:+0000',
                                                        '20210909:201241.424558:+0000',
                                                        '20210909:201241.441157:+0000',
                                                        '20210909:201241.456906:+0000',
                                                        '20210909:201241.473820:+0000',
                                                    ],
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ĊӪӢʦǋ',

            'categories': [
                'invalid-user-action',
            ],

            'error_message': {
                'catalog': 'U˩',
                'message': 'ȥ',
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
                res = l10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
                res = l10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
                'identifier': '\x8cĳłζϡЇӾʭʅõЭԉćŞҽͼ¡ĬњʂȺǩĲąXƛÏƀÏɩ',
                'categories': [
                    'network',
                    'access-restriction',
                    'file',
                    'internal',
                    'network',
                    'configuration',
                    'invalid-user-action',
                    'os',
                    'configuration',
                    'file',
                ],
                'source': 'cͺǼċóʘ\x97Ф¸ħƚӀć',
                'corrective_action': {
                    'catalog': 'ȟΞ|Ҽ7ΆfɗdƊӲ@ńơѠµǵȼЙΠΫϖǆ\u0379ӳĄkƊĒϹ',
                    'message': 'ĄğȱƚȜ˾Țċʝ_\x98ąǇ¦v˦¯¶ΖȰяʽʞζԅÄʮӘƓΌ',
                    'arguments': [
                            {
                                        'name': 'ɿ˯ʞYѷзà«ƁԠԔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǟШƎΎ\x9aͰƵԈȐ6\x93ԞɥϋԤԮͱӛӪǣͰЭAϢή\x82Ⱦ˪ΝǴ',
                                                                            'ҿ.όßҎɏʅÇøͼ҈@ɹɏČɅΦ\x84ШƁя\x98ҨǢ\x85ɂǗǝɮĖ',
                                                                            'ΜіęN¦ЀȂÙΉdʅӒ\x95ɡԃţʘ±Ӏ_šƟӼȘР»КƤɆū',
                                                                            '¥ɑɌȱ\x90ȹѪνďʰΩ¾ϹΤƯƶтӃʳұ˝ɎĎ˄ɒѻΫMĥʘ',
                                                                            '˞s˙˂\x9d¶ҀΜc\u0379ÙϬǵ\x94ѥȤƽͼϞҶԝΰҫǂŭЙʘрϥҭ',
                                                                            'ʈɪşjѢĩӭȲƅɗˆGԊѿϱ¿ţɝǻ{\x82Ϝԏ\x91ƿ\xa0ķϊȕ\x82',
                                                                            'ғБɍȸȠ\x84ʷǀɘҤ}гǷŚˡrԪŴǸӵɞІǐέŗԓԊǝƱƽ',
                                                                            'ʥʑԚʕżĜɆǮШɁėϊArĮj˔Ʀǀ˳ơѥĹ|Ԉ˷ÃşÿА',
                                                                            '˭яĤɍ\u038bƮʊŸЙɀÈȕϳԄʟUΡıʊʖʾɫ\xa04ÁӐÝĐȷɚ',
                                                                            'ʺѺơȧϛӂsʀҷΘǣ˪űԥŦɽ΅ίƼӲąǍΒƎĵũʻӿɿЅ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĢԀӇɚ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201232.594506:+0000',
                                                                            '20210909:201232.610252:+0000',
                                                                            '20210909:201232.626355:+0000',
                                                                            '20210909:201232.642286:+0000',
                                                                            '20210909:201232.663084:+0000',
                                                                            '20210909:201232.679822:+0000',
                                                                            '20210909:201232.696215:+0000',
                                                                            '20210909:201232.711984:+0000',
                                                                            '20210909:201232.727796:+0000',
                                                                            '20210909:201232.743263:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȯԔˎϟŏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -95245.59850556104,
                                                    },
                                    },
                            {
                                        'name': 'ĝҎΎQԏöqҚȉʾ҄ɨӠĶΛ҂ĻØҢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            613118.9533116294,
                                                                            369265.4134602206,
                                                                            -514.0737644628243,
                                                                            217587.61014337314,
                                                                            667193.0644344945,
                                                                            284216.6310576796,
                                                                            696835.7891948989,
                                                                            963630.710003109,
                                                                            116640.0692337848,
                                                                            838824.6908227642,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'š҇ĺďΰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 88810.53779865941,
                                                    },
                                    },
                            {
                                        'name': 'B',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201233.211078:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѰӆШŴǣÙyѱӽȶʯȶ˙ȎĹĲԞϨҶű;ˈϴǻʹ¬ˬԡìĥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '·ҔwŅpΧ˕ɼΔ7ƞ\u03a2ү΅ ϕʾЈɫŚNѣϔǋΦҗΓ(BÆ',
                                                    },
                                    },
                            {
                                        'name': '˾\x97PŌɨ·ŲˀTɟχїԥɦĝХζҦѢʙđӁȣáȶ´ϣԓԧ҃',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 461908.31177570845,
                                                    },
                                    },
                            {
                                        'name': 'ήЎķ\x99ŨȹϬӒ҉úӽFæσҌƉцҞĠѷƊҴӼ\x8aԍјóįw˜',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 211526.16858912644,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ǲϩҪÞđŦɾȝ.ȜАѠ˄D˃ĻöВ˲Їńαɒ˖Î<вҙΔЈ',
                    'message': 'cƯҞѣԢƧХȉčà\x8cƇΒoϾӖƧϸΜϗɼʞӛҋȻЂʀҌǹ"',
                    'arguments': [
                            {
                                        'name': 'ͻȮЌӆһҗǊ˖ɆƻNh',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -911227676864095150,
                                                                            5737078107332201879,
                                                                            7324578230740506866,
                                                                            5234186588584852186,
                                                                            1586987849853377951,
                                                                            8522660787448456686,
                                                                            8862262157339846403,
                                                                            1993953640147720667,
                                                                            -4607408397389350583,
                                                                            -6663921251463970711,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ')dΕyŜƠƞĶϻ\u038dӅðˊɇȬͳҪcӊõȾŏ¡ōԢΌϰóѝԜ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -93193.64731676754,
                                                                            649350.4046190014,
                                                                            605214.5928226315,
                                                                            261365.4731507753,
                                                                            420165.2185679731,
                                                                            829720.551426413,
                                                                            -72324.45006198648,
                                                                            777191.25491416,
                                                                            214651.21189647645,
                                                                            986120.0691632715,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'аʟøѬǟԋƠΣűҟZƴǨɏρΗĐǾ!ɨu',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 25060.60230668017,
                                                    },
                                    },
                            {
                                        'name': '\x9fŸБҷˣʚЦРϹʘˊʳФΓɈ\x8fIŤЊςΖ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3588579894218688729,
                                                                            -2117634148818922012,
                                                                            -7198069962973888870,
                                                                            8047773732922970504,
                                                                            5253100265522035791,
                                                                            127276407719767897,
                                                                            -6715176808948943249,
                                                                            -242172678537929701,
                                                                            -5615307670688361715,
                                                                            4024997719025014277,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŝϡτәÌɄԫτʯȖȯΡ\x82ÓδɌӖ~ӗЮј',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɊʼͻӐƩ\x95ʿҠƙʊϽź˂oѰϨɋϱиҐŝϊѕҮ˸dѕ˗ѐĎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԣơhң^ҵŉ˛˓˩ȊǕ[ȀcԟӋƒƷʴ\x9fǩÿϰ&˖wň6Ĕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201234.868171:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ċКƍ\xa0ǉġӽȋʃϧǞːűʵщɭîΗiӎƋɤ\x92ǹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201234.938912:+0000',
                                                                            '20210909:201234.957720:+0000',
                                                                            '20210909:201234.976515:+0000',
                                                                            '20210909:201234.994552:+0000',
                                                                            '20210909:201235.011317:+0000',
                                                                            '20210909:201235.027172:+0000',
                                                                            '20210909:201235.043240:+0000',
                                                                            '20210909:201235.058837:+0000',
                                                                            '20210909:201235.079803:+0000',
                                                                            '20210909:201235.096868:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǂҾõј¥\x94ԇaƓӍȥǤɕђǿÜȠԕnїϊŪÁĄņʥȹιъӦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϗїťðɤҸėͺКĜĮѧČĬΊÝѕϸԨĻ΄Ψ\x96ѝƴȧvǻΜԧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4187564051194354266,
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
                'identifier': '}\x98Ӟюˣ',
                'categories': [
                    'os',
                ],
                'error_message': {
                    'catalog': '¬Ѥ',
                    'message': 'Ύ',
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
                res = l10n.SetLocaleEvent.parse_data(test_data)
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
                res = l10n.SetLocaleEvent.parse_data(test_data)
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
            'locale_code': 'εåμӬ϶ΠЉ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': '˚',

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
                res = l10n.RegisteredTranslationCatalog.parse_data(test_data)
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
                res = l10n.RegisteredTranslationCatalog.parse_data(test_data)
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
            'catalog_name': '\xa0ƑɷЅ_ҭΠƳѝѳǥµѹϩ\u0382ùÇҦǀ˜ʆԑАΆɂϷ\x84Έɢ)',
            'locale_codes': [
                'Ǒ',
                'ЉʈŃ˕ǐ',
                'Ң˅ϵ\x87',
                'ӫ%хƖ·ĭϗӫ3ī',
                'ƬÝ',
                'ԦƧƉl',
                'ʹɘͻńǁњŹ˱\x9d',
                'Ư',
                'ʏÊϟȚʐԤð',
                'Ӷ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': '\x81ĐБ',

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
                res = l10n.TranslationsState.parse_data(test_data)
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
                res = l10n.TranslationsState.parse_data(test_data)
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
                    'catalog_name': 'āÐʈȴѱєƧЊǅȥ¥ʵŅǿ\x9dǇÎ\xadԨí΄Ɗ(?}Өȳïbԍ',
                    'locale_codes': [
                            'ʒЩɞȩɀӺûӫ',
                            'ҷ',
                            'ɥЖĖғȏ',
                            'ø˵',
                            'ӳƷ',
                            'Țϒƀώ',
                            '¤śΛƭɀ3ӉůӬɹ',
                            'Ǵƌ',
                            'ӨǦĀԁ',
                            'ŬʼȌÙĎʆ',
                        ],
                },
                {
                    'catalog_name': 'ȤюŒаӡ˘ȷQ¬ҩƂĆmЁҥ\x99Ɩ˫˞ăЄЏЧЎΣȹϪәǲ¬',
                    'locale_codes': [
                            'ȸ˕ʖΐ˒ĳÓÊõ',
                            'Ԫĸ üԤ',
                            'ƗɌƄʓ',
                            'Ļӊȴʝ´ǾƂ',
                            'ˬϱ',
                            'Ѓȷȳї',
                            'ϊԁҊ',
                            'ɩ®EϣɱӃ',
                            'ӌȌԣ҅ԡDԝp',
                            'İŸƅ',
                        ],
                },
                {
                    'catalog_name': 'ɱ¾ÈʡӏŨԃŌʔɻѕ˭ʵȲȆȝӜφɀÅɉԞп+FcԅÁ',
                    'locale_codes': [
                            'ҪȂѪ҈',
                            'ɹ{ĦǤӜЕƙҝ',
                            'ɢӀòӡˊ¿ɕ+ɳҐ',
                            'Ęӷϱ',
                            'Xλ',
                            'ϗ˩',
                            '҆ǼҜ',
                            'oΚ?Ю8άǾ',
                            'ƛȁ',
                            'V+ǴüȇĂƝÀ',
                        ],
                },
                {
                    'catalog_name': 'ɦęǚ³\x85ѵùȧɱӘǙӲϗʬŠӖȱӄҌϫιˢˈɺiƏ\x8cω`ō',
                    'locale_codes': [
                            '\x91]w',
                            'ϝ',
                            'ȋɤcІƈαԪҁĥΊ',
                            'ͽŨŉʡ',
                            '<3ʭЀҎºƚƶȅ',
                            '˺',
                            'ß˻Ƣ\x9dH',
                            'Č',
                            'åɊк@ѬųфΆà',
                            'ӓƐʴʫ\u038d',
                        ],
                },
                {
                    'catalog_name': '˫ǂκϖԕɄřɼӚԑӽ·ɽŮəŞ<ʟӥΘÅԀɝӎΒŉёƜуǃ',
                    'locale_codes': [
                            'Ǵё\x8dҝɛɸӓǁϴŋ',
                            'ŜʺįP\x8cưѮǎӻ',
                            '\x93ßӎӊ\x97ҙϙ',
                            'ȉҒαfш',
                            'ˡ˥х˵Nɏӥγ',
                            'ϟʊž¤îu',
                            'ʥьЭФİӓƒ\x98ɫ',
                            '|ϸԥєѪ[ʜ',
                            'җ_ǿ',
                            'ǘ',
                        ],
                },
                {
                    'catalog_name': 'ȟ¾Ĥ϶ΝӁ\x8eы¨ļƑ҈ÿȲWʾʁÐ˙ɍͼԌϷΠ˛ʪČsǼ˅',
                    'locale_codes': [
                            'Ϊ˗\x96',
                            'íҁ',
                            '҃ȹ\x7fÉԜɊȾőǒ',
                            'ɫĮëы¼ŝ',
                            'ūɎČӈɪМԝӸфώ',
                            'ɕ1',
                            '&',
                            ';ßӸАȮ',
                            'üɴȃΣÙӎ',
                            'É',
                        ],
                },
                {
                    'catalog_name': 'Ǻ˥Ζԭʋϭʏ˻ȹɒϳ¥*˩ԇŁȟƁҗҸθʬʑvԥú³ǰȫʢ',
                    'locale_codes': [
                            'Ѩ',
                            'ЯŬȗōɎ˹Ξė',
                            'ÕĤ×AԤ©ŀż',
                            'Rҁϑwʰ',
                            'ǸοǻǇӹə',
                            'ƞʂ',
                            'ԩ\u0382ϭԭËǖΈĺɱ',
                            '\x81џӷџŊǲ',
                            'ȣÚ³ƊƞъҤҁϝ',
                            'ԚC!ѣ˰',
                        ],
                },
                {
                    'catalog_name': 'ȮƇήʳΙŁǪƉM^ȨԇθτpÍω˴ʑˏßNӟаƌҼҁiǠȭ',
                    'locale_codes': [
                            'ѹȦ',
                            'ҷĩҮȳĮ',
                            'Ԍ#ӔŌϟ',
                            'ɋφҦʌɵżʟŀ',
                            'ɤ¦Ϣ',
                            '\u0378ШѬ',
                            'ŵϏŞɋ+',
                            'ì',
                            'ǬǛƤOƔ',
                            'zЭťɒƽê',
                        ],
                },
                {
                    'catalog_name': 'ѐÛƗԀѡÒϊѾʣͲԢđɚŃ΅ȺϭƋĢǷѪƼѱȨ}ԨŐĖȌҶ',
                    'locale_codes': [
                            'ɢ\x95\x94Ԥ',
                            'ÎJŀʽ',
                            'é',
                            'Ѫƫ',
                            '\x9aӯ',
                            'ɻȼǢ=ҢĀĠѮ',
                            'ԡӧɦ¬Ӈўł',
                            'w҂ɤђɞщ˳',
                            'ȴФȿ',
                            'Ьʁτȵԇ',
                        ],
                },
                {
                    'catalog_name': 'ͲżțΩ҅νȇŢЌХ4ʃѢƺӾāӱϽ\x9fǱӹʩҞȶǎîπǖ˱â',
                    'locale_codes': [
                            'ȯα«n',
                            'ҹɌ',
                            'ƪһхɣ',
                            'ΆЌ¾ϱЫ',
                            'ǁǠ҆',
                            '҅ȇ°',
                            'ēƛœ',
                            'ҖюƻƬöǥ]Ϲʷԋ',
                            'ǨѦο»ĪɖÑdȿ',
                            '/',
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
                res = l10n.Locales.parse_data(test_data)
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
                res = l10n.Locales.parse_data(test_data)
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
            'name': 'ιӹšКćďнұķԚǠЋʦûͷͽΗŞ˙ʼЦʍԓΑϧĦƂϊаǝ',
            'code': 'Ѡ΄ҥɯĮԩȯĹ½',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ͱ',

            'code': 'ȷ',

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
                res = l10n.LocalesState.parse_data(test_data)
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
                res = l10n.LocalesState.parse_data(test_data)
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
                    'name': 'Ҟȍǯ×ҤҐǓʾқӮȓ0űԙѲ˙ʜÞʪѥwǘŌυаԅԆřśѾ',
                    'code': 'ʑǛǂɸϿҫ',
                },
                {
                    'name': '£ȔǇë\x84ѢΊɤȮȧ˸ɝʏōΦԕΙŚ\x8aЅЇԏʬʫ\xadĩγ\u0383´',
                    'code': 'θϺ\u0380',
                },
                {
                    'name': 'ӌuѐùĀԪτ',
                    'code': 'Ńʲ',
                },
                {
                    'name': 'öОɟӭˀЏϣΈ_ǰĺ',
                    'code': 'fΙЂ',
                },
                {
                    'name': 'ʶȷ³ʔЅǛkƭʖ×ƂБϧŪ÷ȉʦġŧėUӀ,ǮƷ{ВƗѺ˵',
                    'code': 'ȝʚZȨʖ²˚Ҩ˷',
                },
                {
                    'name': 'ŤŹóhѴДѾ¤Ś˩ÑӟԂşͰgƱ˩Ɨɭ.ǑÁτԕȬҧŸԤә',
                    'code': 'ǒͻ҃˦ҍҚ\x9bɮ',
                },
                {
                    'name': 'ҕӕҵÏѡıȀĩϐӉϝѲ\x87ӶԞͲҽʿMď˶ʤî\x85δıCǋԫϺ',
                    'code': '˴Ѹ˵ԞҨʠġԙαҥ',
                },
                {
                    'name': 'ƗԥǧĄϨŷќȷҀƍȘ˖àɛåɚôʢρԣC\x99\u0379ΚСķ˔ũűԛ',
                    'code': 'ƺŇ΅Ԥ',
                },
                {
                    'name': 'ƓǶ¼ɽыċğƟԒŬӀɘԮĒέθƫĉѶT×¦ȨѧHвʼªêƫ',
                    'code': 'ȡC',
                },
                {
                    'name': 'ԕɏЭ¾ȞsҋǅĄ\x86ĲԥĽəӎɥȟʀф¨Ĳÿ˒ύŁdħyћӎ',
                    'code': 'ƖäӬöǎƔӫΊĬ',
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
                res = l10n.ActiveLocaleState.parse_data(test_data)
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
                res = l10n.ActiveLocaleState.parse_data(test_data)
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
            'locale_code': 'УǪʲ\xadΦ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Я',

        },
    ),
]
