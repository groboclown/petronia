# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-01T15:28:50.295962+00:00

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
            'locale_code': 'ʒ\x98ą',
            'catalog_name': 'ȅ҃үƾԠѠӥԚϷύ˸˸\x89(ЄƝ\x8bu˾ɒɰǝYоM˾ÆȉɆϩ',
            'message_file': 'U˷ţʨɐɜΓ\x97ǮʦįЌɈӪӝԨԚ¨˭=ˌĜłƌѥԊκѱʌӗ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': '§',

            'catalog_name': 'ŕȶ˱',

            'message_file': 'ɓA',

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
            '$': '·ϱŗ\x80Ң~ѦκƄȚƣňɆÃǹЍѮǙ҆ҪʆùɑƋ\x96ÀрӇńǻ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5246370000549839699,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 410035.2784574629,
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
            '$': '20210301:152850.221580:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ơɝɠÍΪϟ¯Ž҃Ʊ\x97ЁаϥΒ©фčЪ˴ȓȎȚgűώѩøϪР',
                'ΨӟʶωĀǦ[ˈҨ\x87ҩʣˊŻ҆ѡϹœȈԑvʦǖӝĴīӒ[Ϛш',
                'ѺȳȢϯƕ=Ѱ\x83ɓηȦ¿ɂтŻǡ˩ƯǼȫΆͲˎΡԓŕ2ǀį\x8f',
                'ʕвΪѥǝĀκ¦ĮîˁеԂȅȧѫĵэ¤ӊyģƨӜɑʝʴԭɧȯ',
                'ӖųѡˎϮϳ˸ΎҵЩĨͶΏӹřΖ\x95Э\u0381\x89\x94θѣå<˶UϲъҐ',
                'Ѷ\u03a2ȟɳ˪Ȅя`ɊƸƢԂŁ\x80ˬxǋҌЍΗɁȡ͵\x8bќĘΎʍЦӈ',
                'ԃӠǇʈϳˇңΎЁʋÏʽΦõӸ6ʏҖЂӰĴƂǺƍϼƓ]ÑҲt',
                'ҸщȔnО^АàƂɻƁΏΖa ΛԔʼƗ&¦ӦːӑΐǘÐ˙Ůό',
                '˼ʕƑǀƸӘƱƫӘ¤õƺͲˆЦФɧȀ8ϬȾȻӔхtĔʹϏЫɢ',
                'ĊǠǯӣĖÜӦ£ˠѼĳɤӚ\x92ӲJѫʙ˛ǗѭȰčΉԤяԀɛŀƿ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                6466173796438551846,
                -6236089232435456280,
                1840160863258111283,
                -3041534125271857103,
                3992551426126513211,
                -4873698809731404374,
                -1179907850867735940,
                -3112721919339347347,
                -2383388278129714426,
                -5101528481439736056,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                725999.4639962876,
                832407.1793686419,
                -21597.15528795561,
                128082.36792355077,
                626531.6948691615,
                409049.6098188424,
                577624.7549234433,
                -63499.02054694431,
                336985.73720199015,
                44113.84004972063,
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
                True,
                False,
                False,
                True,
                False,
                True,
                False,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210301:152850.222452:+0000',
                '20210301:152850.222467:+0000',
                '20210301:152850.222475:+0000',
                '20210301:152850.222481:+0000',
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
            'name': 'ΆCwɕů¡ɝǽûMƝ͵ГƩ;ȷǿŻ^RʒłĤĮŔőɁ˵',
            'value': {
                '^': 'string',
                '$': '˻ɷ¼ýƺ%ʰҚɫҜĕʽϋԢųѧʦúĢǦЂğԩƠɲСÐԮŌM',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɡ',

            'value': {
                '^': 'float',
                '$': 593937.1308103906,
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
            'catalog': 'ҋӇƘԘνϿυˁǜю\x9e\x8eÄƵǾ!ξӉҰ\u0381ʕѰ΅ĄĂЙϭϪӺZ',
            'message': '҈ʓѶˡś\x86͵rӧMŒʅƾƇϥĒįǟоɝʫцԀΤðϓĔΆ5ʹ',
            'arguments': [
                {
                    'name': 'ǉͿʺΫǣӿǮеΛԊBǗһǗĀΤʹϨ¼ſɆʆǏǢԮ1ÂӀ~Ŀ',
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
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': '°ȞСřΕɵ',
                    'value': {
                            '^': 'int',
                            '$': 6677650092798370373,
                        },
                },
                {
                    'name': 'ƌЊЈЬ\x9fȯɄзԖȺҩ˰ȵЮƙΛʢӿʠ',
                    'value': {
                            '^': 'int',
                            '$': 3259263682824457355,
                        },
                },
                {
                    'name': 'Ϸ;ӫэɖÓ9ĢЊǖӁ',
                    'value': {
                            '^': 'string',
                            '$': '¥ƴĆǤpҟͷ˥ɗџ˘\x8d¸ƂцçƋӺɞɀÃ2˽ƏƗҲҷѻ\u0382Ȣ',
                        },
                },
                {
                    'name': 'ǍűȯĥщĤϑǵжӭȗȚϧҌÝ|Þ˻ŴŀςːȖԜт^\xadɚŢѪ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        1158580407268347686,
                                        -3095803674736658873,
                                        -7216753062308197796,
                                        4294541088454265562,
                                        -8817692397648758412,
                                        8688116780226232801,
                                        8898723085735046187,
                                        2396404270129405174,
                                        4443884846304227549,
                                        1518281789325889043,
                                    ],
                        },
                },
                {
                    'name': 'R\x9aĄοɡƵī\x96žɤƭұĨн?ŌĂʎҺфʹʏĹƆăȆ#3ҏŰ',
                    'value': {
                            '^': 'float',
                            '$': 504086.63845291804,
                        },
                },
                {
                    'name': 'ʐȣҜԩˌ\u0380ХǩƤʥϏƘþƉә¬Ʒ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ʸżǰöӓȭɡҸƉêїƁÈŕƬδцԎΰӪŞʨÙɤ×ƮӐοĲӝ',
                                        'ǫɱ˔үϝΘѢʿĄ÷ʏăӨʺĹŔ\u038bȸȊ«jНEʺΠÞԟĚ\x82ѻ',
                                        'ŉԁȋ˟ԗʪɎ®ɌԛψˑюǽϨʂ±Ċ˶ɼȢϠӏΝƶřαЍѫҁ',
                                        'ǰФЈȉɣˇͽ\x89ӣČʞƭΓųİĜŲªòƶɮÊbÿğǚΔɛûȇ',
                                        'śŐҀŦӶőԎħңȅƂ6ư¾èӢӃĸЦМƤƕìĘƿ¦Д\u0380ȸê',
                                        'ʧǲŋǠ!шƹ˦Ҏ;ɝŘʜɐіиł\x80Қ˛ɝʇΘ³ϟƟʽƲɬѭ',
                                        '\x9dӕïVĹŔśӞĮCΓѰȌ1˹ɋΊѰѶįưԋƦѠˈ҉¤0ǡ˷',
                                        'Ӵ˯ѿÌάʵǐБқÊüȜȽɘӳɁʚnĳ\x9eƏєˡҔүĝƺѦУι',
                                        'ǬҹԄȤϥҠ$ŕЦʔʣǔɺқ˃ҳϬȪψɈ\x8cż˕ȼ\u0378hɥʪˑҠ',
                                        'ˣӥԇ*ʖӼӿk¤\x85ғȧþѬɦϩ\x86óƗӰκȓːŪ4ѶϲКaǅ',
                                    ],
                        },
                },
                {
                    'name': 'ţȞұȷԘͷѲ=˃ӲȮzԂƮǔ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        119785.2848858308,
                                        730235.9459254086,
                                        996179.1897910757,
                                        842624.9840957308,
                                        149158.5095372547,
                                        274087.9362646918,
                                        202759.96985013701,
                                        396216.47991622257,
                                        296764.4326393304,
                                        -54289.04662175459,
                                    ],
                        },
                },
                {
                    'name': 'ҲԊH\x981ϩδĚÞ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ɚcӶԏӢį˖óϗ»I+ҧɌӵҵȀӋһļϛԋ\u03a2öʂҽ˒£Ӵσ',
                                        'ƆʵӰԬ˹˃ ǴxщĂÑuĒΨK^ήԜѾěÙ\x8eʖǆдĺύӀ\\',
                                        'ωʽ΅ЯʄӔѲΒêǂǊȡԠѯκFĸǊ\x8eӂƠǅʠĞγƛ4Ϧ«Ǳ',
                                        'ɵΛё+ʍПmԞΐ\x91ƨԄ˦ӨφɭŉҦ˜æĵªŽέˌԨƷȉÌʙ',
                                        'ʩňҥшƪřOȵϠυә˜ΊɟɁϸǗłӨǬΦшʛ¸ѨǞnӤɝɀ',
                                        '҇qɸŻ8+һƁұȕКʩ˥ȴïңҔŒŴȇĠрăȇąrӱǁƜҷ',
                                        'δԧʇ˖Ɋӱñ:ίӞҶʿ\x99ʃΖŪ2_UɁ\x99ǒǜɼГҜÊОʦɚ',
                                        '\u0383ɦÅшΉҙČӍҥЯǘɘɂɸͲҗ_Ȧζ}ôȖɗǓƐѨȳɕӠ2',
                                        '˄СʙшҀő7ʶɋjĆȂƵǄŠǹҤːԟĺĞ"˘ѧԨˣˏƂѥԝ',
                                        'ĺǏϮΘԄӄҘǩϘԘԎєyŃēƥĞˊˡΎԌŜˡƴǣԥʐ˭īΐ',
                                    ],
                        },
                },
                {
                    'name': 'zԘ¤ԤǗʐɟмÝ¼˶Ӿʋīčǯ\u038bтɅ͵ϋԙШҍ',
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
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ƪˡ',

            'message': 'ʸ',

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
            'identifier': "ɱǂÀƝ&¬ʑøȴBŐ\x82ϒЀƂNɉӳƓͶԨȌð?к˩Ț'Ƀȶ",
            'categories': [
                'file',
                'internal',
                'file',
                'access-restriction',
                'file',
                'os',
                'network',
                'internal',
                'network',
                'configuration',
            ],
            'source': 'иъɀʚѾ\x7fϷˍɻϠ',
            'corrective_action': {
                'catalog': 'ʒЀˉεӭѶŵǨҿ}ɂĶǾƔǩСŹΫʙƟŕ¼ƺε\x91ɨ҆\x82\x9aʎ',
                'message': 'éȱ:ąӷǕЈˆØҍƢʩ˓ ɤĵȜʠХˇɏԐӸµԌTшˁϦƸ',
                'arguments': [
                    {
                            'name': 'ƬқÔǉ˚įѹɖǳɶϞʮɼŞԛƥʚˬ¬ĈˆǩƼ҇Ϭĺ0',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Аϻɹ˟Ô/ƣǋԡǠhʖӕӚ˻/ŻѹθĢ˶ӽ/yΊ˥ͿѰū',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΪóAбǗҽӯԗʳӢΜ8ӏEµèΌѳůРЊԮźƛ˹ĚќøѾӷ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '˼ēƳǶơщŹϑ϶ĞŇǰĂ\x86ӖŠáοƵӏԬ[ƬԟǗûµÈŞƳ',
                                                        '\x88ýԛʤҝēӺ`˦ξʴΒŦòè0ŵ˥ϞҝĄЀ³Ú"ѐ2ĹЂƴ',
                                                        'Ǐоϯ\u0378σѣȽԅΣʍʽ\x90ƲǄƏb{ЊӈĝĿҡǆȻӗˬҒL˟ϟ',
                                                        'ѰԒĩКΑГlŧăмԠŵԛɖГǉҠ`Џӎξ¦ОęSϭ\x9eĐΊð',
                                                        'ȅϼӠăЅǧԆǞϕӇȔȃӢŌɵĸʇԓï˻ϴǪήϝêɛШ¢Șӭ',
                                                        'ȏµХϪîˆŦΈˉƼƵҢĺӭǠǫŢҤůҢ΅ȶé\x94ˈϕ·ԋɒл',
                                                        'ǁā5ɒ\x91ŪuҶһ\u038dӘǵȹȁʅǼӅĮЊXȿʰϐ˺ʪ@r©ɑŦ',
                                                        'ŴɔϚöÊϴпԄ$щVÝÿǫͳξ Ǫ²ȢʚñԌřĠÕЎͲҿϚ',
                                                        "ȘЛӍѭǞ'ĵʠȡɄǛȨƻԘrѐƔǆùʠҁʽüϑÏԗч˓ŻԀ",
                                                        'ȡʝ҃ҒKʎĬȅȿ\x89ǕÛǯӰԑϋб˱ТѠ=Ɯ҈ΝŃҙƩȆˡū',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ӽ\x9cгƴƆŞƹϗЖʋĐ»țԄļȫ°ӵȸϼõΩ',
                            'value': {
                                        '^': 'int',
                                        '$': -4598226492788447542,
                                    },
                        },
                    {
                            'name': 'ͼ˖ŒɌȽΨоҍҟ¦иcҿӒ˕ѿƬыʗҠх,˽\x87,¾΄ǟѦƍ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -8366632387046383877,
                                                        -8224985278143506455,
                                                        2734353518646670014,
                                                        -2222366226900810578,
                                                        7660485170341620060,
                                                        -7118574526814821750,
                                                        6116326074509006385,
                                                        -5342840034229818148,
                                                        4538506614022927374,
                                                        -1542386684493039648,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƸǱԭԬƿǯtϵ\x9aǑ\x9e',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        460594.264647292,
                                                        -35931.854365132785,
                                                        895761.8498716598,
                                                        62865.80693188697,
                                                        526980.0044391803,
                                                        312026.1930775918,
                                                        534516.9227993177,
                                                        190332.80031818425,
                                                        85173.16879036007,
                                                        686976.0498221957,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ςŇҨǛ˨ǉ˺Ϯ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -7638796965193226880,
                                                        -8601627148535145811,
                                                        -7871709250033304134,
                                                        2100268433633993021,
                                                        -6684345768076496930,
                                                        -1003584505182673032,
                                                        7745983396476319688,
                                                        -6102034254132368906,
                                                        -6709186358536765349,
                                                        9018179401657027161,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ͱʑǈ3ȡӫğÈǗˢ˻\x84Ɋʪϧϡn',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        532113.6548645647,
                                                        160003.13641071966,
                                                        149510.91844217814,
                                                        304249.8701862751,
                                                        623870.9154122254,
                                                        834743.4878847243,
                                                        554635.3214611249,
                                                        288881.7379169585,
                                                        388460.30419072136,
                                                        30151.407124036938,
                                                    ],
                                    },
                        },
                    {
                            'name': 'úχѦ˞ϫ˼',
                            'value': {
                                        '^': 'float',
                                        '$': 375470.57527410594,
                                    },
                        },
                    {
                            'name': 'ʹPφŕҳМзǶΩǴȞ.˯Ǌȓ¸ʦɢЙɜ|ϰŐɲ˔ŃΥı',
                            'value': {
                                        '^': 'string',
                                        '$': 'ȷĒīЁӳҹѝˑɩǽGңѩ˔ҲόЂӸЫİ˭ɔ҉Ҿα϶Ʀ+¦ȳ',
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'юƒñѭɱв˗РύӔÙʡɁӽ\u0382ǑËѾˠј6ǟǘʷųȮϭx Ł',
                'message': 'Υ˛ӌ˥ǦӴѱЂԍŘˁĩХҡņǞԠϘŤѳƩÃʈԗǜŽȳųϕϝ',
                'arguments': [
                    {
                            'name': 'ˢ˫ ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ÖǆљËәԒΕɜɥӥ˜ſŁȧѳqǮyεǤΞȺЬșÝԁƒѓŷĈ',
                                                        'ҭ˝ԁΊƐˈɃƙˏѱʄӂ;цƌԀˍάωӕd\u0381ĹΆˎη£˃9Һ',
                                                        '˒kǼeξtÆŐЙʏΛǸ˲ϻέ˞ˤȸӾ˓ĮҏȒ˔{ʬѫѡӍԈ',
                                                        'ҜѐΩʭƁǉǆŌǳȻɕɏͺȚ2PûgɊɉӅӊҸ\x8bϔĀŀÆ±ρ',
                                                        'VΦʾuűœĐƂ\x8eʳЊɍɽҍі\x82Ěԃ×ҜƢȄҨ²Ѕɏɧ(Ѵó',
                                                        'ԭľ«ƸXĶʭкʧȗÒȆȱԊĂѫʺƐҿyӹТΚϛѽHÅȏęΒ',
                                                        'ӕӸΩȽßǭȪ˟џćɊNԋ\xa0ΑϜgЃ˟YѻʮƢĕЭΩΎһϠŝ',
                                                        'ńӟӃіԎæǕθɼĈԊщϭhеҳiŘϫ³ˊǌѾȳЃȅΊеԕȵ',
                                                        'ʛɄ³҉ЫιдơϹĶϼ4ȻʤįΨ˲θĸȎʣƞїӑүL˚Ĭʹø',
                                                        ']ϯVɭҖѤÿķˢőЖ˅ТêӰά\xadΎ\u0378ДđċȨɽч\x87ə˧ŪѠ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɰʱɕÉΔΠɪЌГЈǚkҕȕҝϨͼÝěϹϑӴξå˙ϟϟԄôѻ',
                            'value': {
                                        '^': 'float',
                                        '$': 392444.95640245033,
                                    },
                        },
                    {
                            'name': '\x80\\˨ȮMƚɪȎˌǋƜ\x8fzǋýɀƁϒӥ£ӭЄПŬ˧МБр\x8b8',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210301:152850.223290:+0000',
                                                        '20210301:152850.223306:+0000',
                                                        '20210301:152850.223316:+0000',
                                                        '20210301:152850.223324:+0000',
                                                        '20210301:152850.223331:+0000',
                                                        '20210301:152850.223338:+0000',
                                                        '20210301:152850.223345:+0000',
                                                        '20210301:152850.223352:+0000',
                                                        '20210301:152850.223358:+0000',
                                                        '20210301:152850.223365:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '΅ČҧǊԊѤ¡ΚǰҧƒӔÛ(ȼī',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ŲБŰД˧ćĺԗɏËĉӥҥƇЬ˖Ę(ŇeŘIϧѠĥÒџʢ.ѷ',
                                                        'Ƅ˒ӺйԢƝϰšȩǫόӔƧȿ\x9cßƋȤȂͲǎ˒ʮʅUmĿR΄ī',
                                                        'ιМƈĐϥŉƞѢěńѾʝZΞŐһȨyðʙΡϞȶˎ˶ƎОӃʰԀ',
                                                        'Ǿ\x94Ī\u038bƯǖǾŅNǸŘԢ˙ӛОӥҖɚ\u0383ɰҵͼƹԒȱǸ\x9e҂Ńą',
                                                        '\x92Ǡʀғрίǟυ˲ơ|ȚŽ¾ĕɂԋӴõɝ%ÛȪДßąɝǽάί',
                                                        'W4ǟӬϖƧŜԒǍǁõҌӡȉ˵ȸɪɩǼ\x8fʜțťqǫ¯ɑυɰɵ',
                                                        'Ѷ2ӄTƠťҿƒ΅ÔӤ˰Ǚɜ×҉һɊȤůȏòȼɳϷɞïцĸς',
                                                        'ЧԘǅ˷јɯΣϿҮϘԨѣʾЫҘØŹʮӊӾҩÇƑÚҦ˟ӌþЈЗ',
                                                        'ĜXâҔԜ˺ˡýϖξș\x80ǽǆΗWҬτŷ!*ZӚцƦҢҜҰӢì',
                                                        'Ϙìŵғʼӿʸ΅ƃŧԜԙbʳӧƹѐ˃Țθȅǋф©¸ҟƨŉėÎ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ц\u0382IȽǀơԜkѯϵμ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210301:152850.224065:+0000',
                                                        '20210301:152850.224079:+0000',
                                                        '20210301:152850.224088:+0000',
                                                        '20210301:152850.224096:+0000',
                                                        '20210301:152850.224103:+0000',
                                                        '20210301:152850.224110:+0000',
                                                        '20210301:152850.224117:+0000',
                                                        '20210301:152850.224124:+0000',
                                                        '20210301:152850.224131:+0000',
                                                        '20210301:152850.224138:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '\x8c§ҕ"ʬ¢ΝǵԑМȧЯͱʓȿʡ\x8aьӀԅ\x82ҐɦȖĨԍėŷİР',
                            'value': {
                                        '^': 'int',
                                        '$': -5757892350301022854,
                                    },
                        },
                    {
                            'name': 'ѱгđ½ЀŲūƕğνĩƲӟŔѠӲSʅҽГʌ˘',
                            'value': {
                                        '^': 'float',
                                        '$': -3264.3727844432287,
                                    },
                        },
                    {
                            'name': 'ϷʙıώȾƧӃԢԋѪ\x9cҚ҅í±žìáӒӔŭɒ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ǯ\xa0ƪșȈϨŵӐǨȊΖǍӹÙĈԓ\x9dŜя¥ħÁėśƅɑ¿nȠе',
                                    },
                        },
                    {
                            'name': 'JӖɁĿ˱˜ӲΊķɵƦġǝҦнҔŖǵ"¦Ӻʇ˸Ԯɣԓӌ˘ˬԛ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210301:152850.224848:+0000',
                                    },
                        },
                    {
                            'name': 'ʗź\x9aÙѶǝɽ¯ЅӶź\x9bƵÏƿhĈŽ˸ɲ\x96¥ˢǒсРėɱѬщ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ϏaҕӂнĆҐʼҙ¦ǧѼϢ\u03a2pőҏçƋgκϠҎШaɩ ʬҞĚ',
                                                        '\x8fгUԊʼɐǴɧ8ĝ7қђ5ŬĵҀȄsпŬǥПȍ,e*üԁβ',
                                                        '¿4ȪǼÏȠԧϑeÐүˌ\x9cЫȨǾϝɀʶéœдŮ3ȍɽzɑӫҬ',
                                                        'ԬʓƤĻǳQŜ\u0381ǆЏ\x92ȁóҚįǰɞšϺˀĚΧȥǳƦ÷ʹηșє',
                                                        'ɢѬИɻ%űǙӷɞªҐЗɹ\x96ʝpԆšľж\x82BΓόɏ{ԥЛřʥ',
                                                        'ϷǧϺөÛԞ˅Ώ˗ԒӢAęɹӅϔδʢѥŴɨȉŨ°ĦшθƔҭƧ',
                                                        'ɹ9ƶèlч˻ėťκǟʛҬ\u0383ųɞ/øwVӷҌıˍԠЋ)҇Ɇ\x95',
                                                        'ʪːѐƥ˜ƣүϳп˽uQƫĨϮȑͺӢ_ȶшŸ˛ğН\x84ӺЧčǂ',
                                                        'чɩŻ˕ћəµŅˉwŎϪȵʖԜÛΤʑȌrПÒʯɱǲZóžÁг',
                                                        'ĳƨҩӼȆΣΖҖЃŮŘ)ʁǈαĩƻɭ³+ĚΰӿȠϲ҈Ӱ_ӏΒ',
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

            'identifier': '&ĀӀэӦ',

            'categories': [
                'file',
            ],

            'error_message': {
                'catalog': 'Ωʴ',
                'message': 'Ă',
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
                'identifier': 'ŦǶʏʠϸʺɾΏ҈ȽͰЎǓȻҁӠʧѓӂԔȧÑΟÈδƄНӻöː',
                'categories': [
                    'file',
                    'invalid-user-action',
                    'file',
                    'configuration',
                    'network',
                    'network',
                    'os',
                    'invalid-user-action',
                    'os',
                    'file',
                ],
                'source': 'хҵŦʜĺԡЂϵıȢĭɸȒϨ÷áϥΎ+ӥӸä»rϰƈŌȳ0ç',
                'corrective_action': {
                    'catalog': 'ȘϒŰŒЗãϊʘтӻ·ǢǤҺč4Ё=Һ\x97Ǟ˘şҒȭʯ6ˁ-Ƃ',
                    'message': 'ЍɁȾжIĈϺΎþ;ƒƐυǁϗʖÔͱΎѾuӗƿЭɅŔ@Ϋɍʸ',
                    'arguments': [
                            {
                                        'name': 'ȤФΌ¨ǲǲҠBπyō',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Φ˯˳Ӆ҂ũӴYσ_ҲɨȔ\x81ɨ˟ҫӻÞˣρˌɭϊϮèjˏʵɍ',
                                                    },
                                    },
                            {
                                        'name': 'ʖу\x87ºDĒˬȾӚĳйʤАӻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            704182.3788343112,
                                                                            413353.3329146958,
                                                                            255808.9875011695,
                                                                            807626.6576498579,
                                                                            727462.263641796,
                                                                            443353.2755478064,
                                                                            996153.3412987606,
                                                                            754705.1361480097,
                                                                            -24486.454184391667,
                                                                            900468.8056309543,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҥϖʞǝю˂ϤǧĕӎԗǔϕʬЛŊĤȊ\x9eɽүɎѨƤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            457881.4544169194,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'УωӓѪſÃԘǜҙϳƉəƧԌà9ωӜˀάØԀѬƔ¶ѴϩЈ\x87ē',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɣ.ŒзʯĀˁǨώίӽr˔ΛέѠѳːSыzƑƎҎǰћ\u03a2Ľӱ"',
                                                    },
                                    },
                            {
                                        'name': "Ȧƣ»'ȊϊɊǢȌϬo\x85ƹє",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152850.210148:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʻȕ|yЭӯϏЗËӜЛWǎӼ˦ʙŻźŕƭЃΥÖǗĂ҂ζΝϓȞ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʻɷ×Ҫȅµ÷ΡƝɃ˭Ͻ\x7fтȐϮԪКȝeȫʏ`άɒİԮŏ\x87Ơ',
                                                                            '˶¶ÅfɹIґʘʰʛʦfсǖƤ÷ҷJɚ˕»˘ϺR¹λыȱа»',
                                                                            'Ŝ8ԌNχ&ӜŠ®ѲʰƊŚԪAΣ@˥˛ΰuƶZҌØϥӹ\u0382ñų',
                                                                            'ήѵȟȲľϯχʲтʒʞƽÅҙЖҖԒYжʘɞωΡЪʼϏͲd·ʷ',
                                                                            "Ηϯґӑͱ҂ΦŻѧɾӓ\x7fĩ˧ӄǭɜ'ɏҩχӆhȴԃВ˾Ʋ\x88ɟ",
                                                                            'ΦʠʦʇʄŁҒĴУňӾ·ΛʈÝ\x98Ԯː\xadϊɳɠӪɸεŀȑΤ˜ǐ',
                                                                            'ȵʒΩˡƮɁßѱ\x80\u0382ǔ˟śρɩԊʗԠěżĐùĝЩӑ˜дƭȐ΄',
                                                                            'ȯŷԂ҈ʱĎñϣ\x93\x84ˋѢСrѝЕÝˀŚˢҋƟ\x9cћӏԥȇĞɄϞ',
                                                                            'öʔɹʁӷƾӽΛdƘȇjʒĈ˄]ǙŴҪýѣӭԃ˶аҡÙ¬IŽ',
                                                                            'ɱ\x81ѠxŰƔǀ>ҩԕǤŪȟƛԇńϐ\x89ҞĻ/Ҋ¾҈vԀ÷ɂҨӪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΆШ˖ЏӯͶӞƏԂȢԃѕ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            515310.07871714793,
                                                                            688786.8689020814,
                                                                            833666.2549286656,
                                                                            237257.2194005894,
                                                                            22796.23098775836,
                                                                            -23738.89644845997,
                                                                            287472.4418976764,
                                                                            -59919.035236007934,
                                                                            743091.5028509045,
                                                                            936927.5100382705,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'āϹ:ϪΆѱӬΗ\x83ȎˁϧӚǺȦѥɛсȉǵЀ·ǂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ùґſлśźԝԛнΩŘέĦ˦АԝИÀʚǘɆЭȽcЩƱԥԝÝŹ',
                                                                            'Àʗғҍ³ƿƟƑĶΔЦĈȑҳϫҌɳЄFШӴɝɻRө2ӍĻƱƁ',
                                                                            '2ĕɆřйȲł˖ʬˎ¯ìˎ4ŘίѲʸԮĒӸӕƓŵϝҙϺơӏG',
                                                                            'Ҝτ Ԁҧ\x7fǵǘШƕТҠǩы\x8d˭pԘQɕĠьŮɢфʕы8țѫ',
                                                                            'ŇȈʿ*Ԑt£ѰƧԕ¡ʡɶͶ¤$ʠŌӵɾǷϫ#ɅѵԄҖƝħį',
                                                                            '\xa0ƺӥ\x8c\x8e˲˝ȻʕB¦ƒRƓʷɈбÏчӄɇҴҨŭĽ:úƐѼΣ',
                                                                            'пȶϸ˕¦ǁГӔŜңҮТʙȆȀĽFɹ¬Р_ҀsƾȠîȏΙΨȟ',
                                                                            'ą[ĿϻʶVʇәɬɘ˺ӗ4Њǔ\xadӪĤѽ\x9cɨƙШȇˢΓθVɹв',
                                                                            'ѳƁ҂Ѽȸ˨ȷ\x93¢¯ʚңҕʢ˞҆ȰͲq\x96ǅɅҍнò_ЇǌHŔ',
                                                                            'ѐҳĬЏӖҷǌфȝɊÍϩР«(ɿŃĕ·ŢRɐς~ъőσƄ\u03a2ĵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԢιƼȺОİĠӉǣңəȴȟǺЋЍ\u0381ОŇɦ¥ŤҦǃƙÉөӸжϠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5919543658773941706,
                                                    },
                                    },
                            {
                                        'name': '˳ǔªҪˀѠɾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152850.211649:+0000',
                                                                            '20210301:152850.211669:+0000',
                                                                            '20210301:152850.211678:+0000',
                                                                            '20210301:152850.211685:+0000',
                                                                            '20210301:152850.211692:+0000',
                                                                            '20210301:152850.211698:+0000',
                                                                            '20210301:152850.211704:+0000',
                                                                            '20210301:152850.211723:+0000',
                                                                            '20210301:152850.211728:+0000',
                                                                            '20210301:152850.211734:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'і_ɥɆҗбǴɆƖǏӲϾäʏҫѡжжҰʶŸѺƴƻĀʨıƽƤĭ',
                    'message': 'еĤȒyÊ˖ϥƾϫʄZɗΥĠVϷðȇ¸ǅӍŏʆ˙ǶоʸԗϲÔ',
                    'arguments': [
                            {
                                        'name': 'Ѡɦ0ˇӽŌ˖VӦүɪϔφӂԣ˟һ±ŧΤʑɑû˞MŨʶǸİѻ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'κτéʬӄ\x83ʙϘҳȫҔƉӇԪӭ±˺ƨͺMƗӳÑĖfſpрæń',
                                                                            'ƹ=ȟʤΜшʥɎ˜ǷӂùξǐЫӽʠŖ˳ЃћԮ®ǀʝȡӴeAǓ',
                                                                            'ѿ=οҥзԈŷєӭ˯ˮ˙ӿœ8EѺ0іƦуɴêŠл҃ԢВƍҙ',
                                                                            'ÍØǸʯѲ,˸\x8bƅǖԈӷǨԂ˲9ʫƄ[ІŶԌºŀĚɆԛƦ»t',
                                                                            "˽Έ'ϋѸԫ;Ϡϖ\x9aΜӤхΆʙȓќешоȌɚ¼åзʿŻ˭Ȟͺ",
                                                                            'ȷǙҟҧλϕüмJɈʘĻėΡƞ˕ȺȨ΄ѡ\x83ҺѭѬȾӽҬäŊԨ',
                                                                            'ȠǫύɡӸȋӀĥԅӃΧҙɟҝƿсӽĕ·аĉӇƬѩГԡιȆϸȦ',
                                                                            'ǐɫН¡ȿɼѹkɗн΅ύõιƞȴvɢûyĳȟŷƻǭĖЩăңҲ',
                                                                            'ЩԪȱѕǊɋŒҎшƠωüЗǔԮϜϾăӎԢpʣƦ˩Ԣ˷ȑУbđ',
                                                                            'Иưӕϫɫѻ˘оMҳɪҥϺƋϨ#ʣϪЩӢΟƩχȂ\x96ӕcɤ\x98ř',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɒсǮǮȝԨĊѡӢ˻Ѭԏ;ş\x94åӂÿƩӲ΄ʭɝӾȁ\x9dīϘ˒ː',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 874644.0220627069,
                                                    },
                                    },
                            {
                                        'name': 'ŗÙťӎǊŠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЪϯќҬǸԩКƆИQ˹ͽųĠҼԀƕƌºȫØțʧȑːЇПűƌ|',
                                                    },
                                    },
                            {
                                        'name': 'ũÉȌԄѵnЄïψP˺ҁёҘƄĢ\u038dŜʨīņǋȔɊˌɄȾʽϴϢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -10190.277364279536,
                                                                            896878.2815228644,
                                                                            313087.38108087325,
                                                                            855162.8312387253,
                                                                            361983.05132018036,
                                                                            348851.598807446,
                                                                            -3546.2143588373146,
                                                                            407841.5271558854,
                                                                            315368.966049341,
                                                                            59269.07374749199,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ìԏʷ˵ČϡƛҖ©%ϊζӰǬғļɴĂǢӨ˧ΈÀDϲ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1312512992327036362,
                                                    },
                                    },
                            {
                                        'name': 'ȕĩË+˒οŒҭÔtȠʌʇƲÕ!ƋνʺűҹȔӤеÒ˻\u0378Щʢˆ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÀйȏΒ˽Ґ\x8d ʔτ>ΕJϨ\u0378Ƹ\u03a2ɳųƓЛԨŔŃŖŗūÄΛѨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 323991.6674446235,
                                                    },
                                    },
                            {
                                        'name': 'ξɜљԒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152850.213477:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƜũÇȍǻ΅Ʊёғʽ¨ĕƠ˳§ЖӳǵǢѻљǳ=ɭȑϻΎ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152850.213610:+0000',
                                                    },
                                    },
                            {
                                        'name': 'îЬřǈˏԔИΔÍŊȈ§Ȓ\x9aЬ˨ЍǬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -99283.80245455049,
                                                                            205450.90301245998,
                                                                            976282.0883202178,
                                                                            560407.7239807936,
                                                                            931083.8175354933,
                                                                            12682.868931438701,
                                                                            431328.07421617897,
                                                                            680977.0859655188,
                                                                            883950.2831920343,
                                                                            -35945.66368151851,
                                                                        ],
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
                'identifier': 'ЫǷӜĠԍ',
                'categories': [
                    'network',
                ],
                'error_message': {
                    'catalog': '«p',
                    'message': 'Ϧ',
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
            'locale_code': 'ΗƆѡǢ_Ƨ\u038bѝɮѺ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ҳ',

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
            'catalog_name': '¿ʨŝǫǓƆ˪-Їɺ5ƦȜ¦ӣεɛ|ԧʅӮӺӯȩ1Ƞēͺɉɓ',
            'locale_codes': [
                'ʁɜ˚VΌ',
                'Ǒòҟ˭Ӽč',
                'ШшƺÇūʷʕ',
                'ɥ',
                'Ԗ˃K\x98ˋϨ˚пÝ',
                'ϙƥ',
                'ĝõ6ӟɇyZ',
                'ԣæǑϾɒθ¯',
                'сƢu',
                'ӯѲ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ӬɋŁ',

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
                    'catalog_name': 'ˡϝ/ƽєȾϥӀѪӚ¹ˇ\x8fȑ˃\x85ȰìƼǆϖϫʊǕ\u0380ψ\x9b¼\x80Ф',
                    'locale_codes': [
                            '4ƬѷǪʓӶ=ƛ',
                            'ќƦ˱¿ӌӼ*',
                            'ȅз˗ӽ\x81ǚþē',
                            'oЇ˻Äľ¨',
                            'Ǣ\\ÀΙǲД\u0379ʊʞǇ',
                            'ϋԬ\x9eϧəˇƏ',
                            'ǺÌ',
                            'Є¨Ê',
                            'řü',
                            '[Ԕǯюɰұœ',
                        ],
                },
                {
                    'catalog_name': '\x88Z˺¶ԭſ\x8fƑ\u038d\u0378ɌόóΒԓ×ѲԁɧȲɺˋϭˀUóÄћǃΐ',
                    'locale_codes': [
                            'ǰӪ¬ˠлŖcӰ',
                            'ЉУϛεѲƧ<',
                            'Ǿ\x80ǛтσúюӭђǑ',
                            'È',
                            'ϡÜȄÞ',
                            'ʩÊǁ',
                            'ѥŦ)ʍÕўº',
                            'ʮˇ\xa0ӳ',
                            'CԮľ»ˠӊ',
                            'ǩ8£ȴ\x8eȩ\x96',
                        ],
                },
                {
                    'catalog_name': 'Ĩ@Ơ\xad\x82ʃԆñϹͿʌгʜ1ʱĺƦŁќȆΐȑāĂǳʗƥΑхθ',
                    'locale_codes': [
                            'ȁ',
                            'ǣԘǚʛϫɍαϾӲ',
                            'Џ\x85ȗҗӕ',
                            'ƾшÛԌϴЭғ΅ѠǮ',
                            '\u038d˳ĭǡȦÄҀǛʙ',
                            'þ\xa0èʚҼ',
                            'ѦмӧϣҘѴӌəѴ',
                            'к\u038bÂčɠÞķͳʫ',
                            '˖¹',
                            'τ5',
                        ],
                },
                {
                    'catalog_name': 'ʞҜӁŦЋӨϣЌǄβÄѡґӾŅԡϬİ˹ЫԬʯҾǔӾͼ^ԖˇƗ',
                    'locale_codes': [
                            'ƍO',
                            'ˆƯQχӰϔS',
                            'ε',
                            '¹ĖԨҥƈ',
                            'ĬкȧǪ¢ҕĒƨ',
                            'Џìђƒ/¦',
                            'Ԫ',
                            'ѝΗӋ҄ԁәŬβ',
                            'Ͽɩɸ˶Ť2ƹ',
                            'ͳ\u03a2\x9fȑͿ1ǐǻѤ',
                        ],
                },
                {
                    'catalog_name': "ŔĒԞńϚώѻÏȐȵ'ЅæҬҬΘԕƔÂȬʮjǈÂЎҦª»ΟΟ",
                    'locale_codes': [
                            'ȸӚ²ȞĤъӑБћϾ',
                            'Ӝ˲ǮΦФ',
                            'ǩɝǹôόΆµʉ',
                            'ѱ',
                            'ӊ',
                            'ҖŌЕԨ',
                            'ņĒ',
                            'Б<Ĩ¬\x9aɕɡv',
                            'ÉɜsŭǒPNОη',
                            'Еɤƾ\x84ʘϓҥѹЄч',
                        ],
                },
                {
                    'catalog_name': '˦Ϗџqȣӟћɏ҅ƙǌԨļʮҌĨʔΈƼýÝ;Ϗ±ʴԢƗƩÄĕ',
                    'locale_codes': [
                            'ӅЍ',
                            'фӮ',
                            'ЄȽơӷ',
                            'ɑȚʔϻǡϚԨǑβ',
                            '{ϻ˚μ',
                            'ԔǵŮǍȖ',
                            'ԏâɄӺƙѢѩ',
                            'Ƅ;',
                            'ǸǃĵUǁ¨ɮѰ',
                            'ǒƙǳρ',
                        ],
                },
                {
                    'catalog_name': 'ľĪɲԙңɛÍĵ\u0378ӄ˚ǕЉƵYԇ˺˼ОǗ\x8fȖӔȵͻɉÅaӽΛ',
                    'locale_codes': [
                            'ʝǬԏаÝſ',
                            'ʕɖʙɮȝǞˋǪ7',
                            'ãȘ˟sӍy°ўƝ',
                            'áȁΎƣ\x8dӲ',
                            'VãĸӈЦɕσ',
                            'ƌƱBídĵϮƉ',
                            'щǚ¹ԑÉnϊNΛ',
                            'ȠôŚКөƱ¦ɘЁ',
                            'pˋˍԢѺӜƐҁĒ',
                            'Ԓ˄ÏũǭԭĬ¬',
                        ],
                },
                {
                    'catalog_name': '2ҥĉӔӚυҫŇӡïĝŀǮЗϘ¾ÛԔӜ5D˰·źt<eӽňЀ',
                    'locale_codes': [
                            'ŧÍŝʰÌΠ',
                            'ɯƀÈҺ˨ē',
                            'ʍ˳Φ˾˻ЍȔ',
                            '¿DʹƹʚõǔÎȅƱ',
                            'ѫϵº',
                            'ëҿϐ˹',
                            'ʄԖҡǀӱȞǼɔ',
                            'ľҀ˷',
                            'ˁ¸ǥ]',
                            'æ',
                        ],
                },
                {
                    'catalog_name': 'čhȑʄƕǲţɀÛϥtͰ\x92ҫÑǞЍΔƃkΛӇőȁƛƷԙ\x93ΰѼ',
                    'locale_codes': [
                            'Όʓ°ĊϵΕêÕʳ',
                            'ʛʋƶҧǃ',
                            'лƪ}қ½Βˠ',
                            '\x9bδʋЀĪ˻ţɮ',
                            'ʓѸĝɉˬüȒ',
                            'ǼԂΧԞ',
                            '˾ôШʤϦ',
                            'ҝ\x8aơƆǁO',
                            'ӭʿ\x9cѽQʚ',
                            'ŭӞƖŘηĦцѨ',
                        ],
                },
                {
                    'catalog_name': 'ʹԅÐƾ;ѳӌǙʦȰʪЂԟŚӱƧљğЧѼ˝TԘÐέδΚyϴï',
                    'locale_codes': [
                            '˕aǁ',
                            '|БÌĬ',
                            '˝Ӳϼγ',
                            'HγÌáſˑʿƋ',
                            '¹°Ϻԇ',
                            'ΛҊѾ',
                            'Җ',
                            'ӽǚɇɋǧΌЖӑΉƨ',
                            'ǵŉ',
                            'Θȑ˓NԂƉ',
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
            'name': 'ŋΒǷɍƳɈǜϚǞԥҟҵȡŠȺǻĒ\x85ӗȘΨȚĽȥҷɲԓƚ¯_',
            'code': '"Ϋȯ+ˮЈк',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ã',

            'code': 'ʾ',

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
                    'name': 'ѴpϩЭUĠ\x8cŷ',
                    'code': 'ǋŒǅҼǵÁïĢ',
                },
                {
                    'name': 'übĕљΒϘ\u038b¸ϣűЩŕŋХčѳȑѭʥÐǬǛѺЈƐύҟͽ=Ϣ',
                    'code': 'õеԆǙ}жѥ˕',
                },
                {
                    'name': 'ȠÿʷÕlýɵ¬ğʹњʉ¨ƏʑǷҼѮͲêρņͷΔʟ˚έɓжŴ',
                    'code': '˯ԢŦƚ˘uä÷Ԩо',
                },
                {
                    'name': 'ЃɦтΔњĊL:ʯ҇ŋêlʒȺҏɅӳɕyIîɃŜɜ\x89Ѥёɳ͵',
                    'code': '˝',
                },
                {
                    'name': 'ҾˤДϙЈ¤ԌǍӄăȶ˸\x9aƵɅǖWȅĸх³Ρ˹ҮϮѦӥφξģ',
                    'code': 'вͰǤƝ3тҍўȇ',
                },
                {
                    'name': 'ƦȽż',
                    'code': '҈ʳČ',
                },
                {
                    'name': 'ȅȧƺµxÙӉЭԬӚϭŠU9ŉŇȅǖ\x93еʋ҄ΛҧϛǿşɧˣӋ',
                    'code': 'ВA|Ǵ',
                },
                {
                    'name': 'ğοfφ˾ÛӈɁǹ˾ØҎԃʣԢȻ4ʫÎґǕһ¥Ͻƪ҄ȥ<!ʤ',
                    'code': 'ˀÞĢȱΑ',
                },
                {
                    'name': 'ӿĹʘљǳѪґĚИļɾ˵ԕʛԘʧΊũϚΌǺӹ˂ʫ˅фǖΙт-',
                    'code': 'ÄǶӧFjΨϦ',
                },
                {
                    'name': 'ǥçҐSǂƦȱҠԩ\x96ȃǭʳҍӆÈԎΦǾǀƫǹгϛЈΩπǄŁͻ',
                    'code': "эƘ'\x82е¤Ω",
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
            'locale_code': 'ƠãĠȏ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Д',

        },
    ),
]
