# GENERATED CODE - DO NOT MODIFY
# Created on 2020-09-01T18:29:17.099062

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n
from .. import extension_loader


class LoadExtensionRequestTest(unittest.TestCase):
    """
    Tests for LoadExtensionRequest
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_REQUEST_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequest.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LOAD_EXTENSION_REQUEST_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequest.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_REQUEST_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionRequest'),
            ),
            
        ),
    ),
)


LOAD_EXTENSION_REQUEST_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'name': 'ӕ`ҊӧmϳāÐҵw9ϠÒѰǌ˷ɳǢďʚƆƼГϱțm¯ΈѿɆ',
            'minimum_version': [
                -2402526937720350943,
                -1238718549147446293,
                377030330938688685,
            ],
            'below_version': [
                -8975008489774876708,
                -2465346333106826214,
                2401279815956568495,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'name': '',
        
        },
    ),
)


class ArgumentsTest(unittest.TestCase):
    """
    Tests for Arguments
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ARGUMENTS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Arguments.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in ARGUMENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Arguments.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ARGUMENTS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (

)


ARGUMENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (

    (
        'string',
        {
            '^': 'string',
            '$': 'ЬDӕĲʠș\u0380Ɇ҄ʄɧʡΛ҃ƲǏ¼θΊҘԀźЛưάıˎƀxƟ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3230000529007986547,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -59627.37223316166,
        },
    ),
)


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
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in ERROR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Error.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ERROR_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
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
                dict(field_name='message', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='arguments', name='Error'),
            ),
            
        ),
    ),
)


ERROR_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'identifier': '\x91Юŧ\x8eΏДȾ¤ҊÂɂ¡\x87αǸєҖ#ƠȌ\x94˛\x92Ƈɶ5ЬƂϠǘ',
            'source': 'NʜȒŖơCȚ˶ԏԗƉѠϰʕчˀçɲˆҲΖϐǖщϮѮȏϙˮ÷',
            'message': 'ʺӨ\x9aũȸŲĎӎқˠī{ȮŖϢÄѭϡԕˊǤϝƺ˻ӋҧϑUéΗ',
            'arguments': [
                {
                    '^': 'int',
                    '$': -2098382196476695793,
                },
                {
                    '^': 'int',
                    '$': -2058232308823097591,
                },
                {
                    '^': 'string',
                    '$': 'ģ©ƧŢҨѕԏØӘ´ЂȋϞʓѦ7šȏŝÔєӣĎѡӳΖöɾ˙г',
                },
                {
                    '^': 'string',
                    '$': 'ѥ\u038bǕ\x9fɈЋą҆ԘԄʪŉЍѾϑΔӧέ-ʎ]ƯδƛѩѵϬυАȵ',
                },
                {
                    '^': 'int',
                    '$': -3534069308149237986,
                },
                {
                    '^': 'float',
                    '$': 93092.66248498904,
                },
                {
                    '^': 'float',
                    '$': 359613.446782637,
                },
                {
                    '^': 'int',
                    '$': -4311675932345520809,
                },
                {
                    '^': 'float',
                    '$': -7966.272835352371,
                },
                {
                    '^': 'int',
                    '$': 7923400975076671016,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'identifier': '҇ɺ',
        
            'message': '',
        
            'arguments': [
            ],
        
        },
    ),
)


class LoadExtensionFailedTest(unittest.TestCase):
    """
    Tests for LoadExtensionFailed
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_FAILED_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailed.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LOAD_EXTENSION_FAILED_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailed.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_FAILED_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionFailed'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='LoadExtensionFailed'),
            ),
            
        ),
    ),
)


LOAD_EXTENSION_FAILED_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'name': 'ǙûϷѡȌėԑĘňӳДԩĠнÛ·ĺäʱϻԤФ҉ѮÅԉʇӱǴǷ',
            'error': {
                'identifier': 'ѩп©ǕK\x99ĞŜƞ\x869ÄҙЊрǨ͵¦ȤԑÉăÉӸӥƝ˥ǧϢΥ',
                'source': 'ћӉɸqӛ¥čΥÑ\xadґϲӑŦуԎʟҪ¡Ѣ¢ɔҭ˽ǿɳ*\\ğĘ',
                'message': '˓υȵϙϪӼŶiʈÑĥϛvɝϼҧǟȆ\x8bіѪӇĔњӱίƏĨ˾ɤ',
                'arguments': [
                    {
                            '^': 'string',
                            '$': 'ѧιˠϒĕˀŔԃӳĩǛ˻ɐĻг´Ķ',
                        },
                    {
                            '^': 'string',
                            '$': 'ΫºƲϗɒˌŇԛOәĤϘϏ£ʦ5͵Ϳ}ɎÚrӽįГƀˡτǘʊ',
                        },
                    {
                            '^': 'string',
                            '$': '\x91ЍǐĳϲȘ1ÿҘхÈӄżƧ˅īњΜҰƅҕϨ͵Aϟў\x9cQԝҜ',
                        },
                    {
                            '^': 'string',
                            '$': 'ƠìҢӓϯмѵò#ϕϻŚŷԚǟАɷ=˸ДʢȹãѵƶŐμ?н4',
                        },
                    {
                            '^': 'string',
                            '$': '\x9eȅϵøƮȽ\x86ԚӆѴƁʪҟʣˮ[ӻӧɸÂ´нΥԏσ\x8aŤʽĎЍ',
                        },
                    {
                            '^': 'float',
                            '$': 87063.86808953123,
                        },
                    {
                            '^': 'string',
                            '$': '1ǎǹɂɖåˠЧҬˣ\x84śƕÕȥŲĳΟ˜҆ŖӫϚǫʏ˩s¦ȟ/',
                        },
                    {
                            '^': 'int',
                            '$': -8472047020754250990,
                        },
                    {
                            '^': 'float',
                            '$': 645240.103721921,
                        },
                    {
                            '^': 'int',
                            '$': 1489064233828169113,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'name': '',
        
            'error': {
                'identifier': 'γȩ',
                'message': '',
                'arguments': [
                ],
            },
        
        },
    ),
)


class LoadExtensionSuccessTest(unittest.TestCase):
    """
    Tests for LoadExtensionSuccess
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_SUCCESS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccess.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LOAD_EXTENSION_SUCCESS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccess.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_SUCCESS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionSuccess'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LoadExtensionSuccess'),
            ),
            
        ),
    ),
)


LOAD_EXTENSION_SUCCESS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'name': '\x9bΤӏčõċʽʃʧʙ?ʧҧβĴųВȈrôɂûɲοÏǸпԢћŬ',
            'version': [
                -7998256707998195892,
                -4531588102280316063,
                4645017465398917821,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'name': '',
        
            'version': [
                3425763583602975557,
                -2183971419123168271,
                55228789069324392,
            ],
        
        },
    ),
)


class PermissionsTest(unittest.TestCase):
    """
    Tests for Permissions
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in PERMISSIONS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Permissions.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in PERMISSIONS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Permissions.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


PERMISSIONS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='action', name='Permissions'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='resources', name='Permissions'),
            ),
            
        ),
    ),
)


PERMISSIONS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'action': 'ҰƭǛÇӯɃî!Ѽɻ0ӡDѿѽ\x85ìŊΈʓRҩʳÝȸ˔#ȢƓʹ',
            'resources': [
                'ҕǇԛȪùĴȩ0ʺѢǌЏғŐʨ ǎō˼ΠҌ·Ǚȷ+ŢиÕ˄Ӣ',
                'ˌѸ϶ȤƐËTΔȾ-ĜBҸрx\x8ażÐϭԢΝȆȝ˽ϹϑņνM-',
                'cβɸʼϪžðȾҳ˾ˏ´ЋÃˊȡøºɑΗԢqʄπƘѭȼԚҋľ',
                'ƀɪԆĸ\x86С\x85БɥŀєĘƸЇȠLdӖȬЍԠАԥƥ˒ϠŖǷűˢ',
                'ҮyȁѐӅñɕԇςǺѧûˈƴ¥˺ӮkΈъQŷÄϑ\x9bӻѺǝʛ˴',
                'ȢѰİɶƋɣԡɁüʨЄЉƈȁǬӬɠ',
                'SƊB҂ǩ',
                'ǜƿ\x8bǹɌĥǃĎӪRʘȵɤǍ˃ӯǻ\\ϴɯяŻȲŒ²ѫϠΗҴİ',
                'ɘѿЫǻÞĹ,˓ҋɌԡǿƽǟúБʦφԧ\x87ŁɈөӇαë\x84Ź\xa0ȣ',
                '¼ԩŴkŏuŖNǔȯȔԀӔϥƶŬ\x85ŤЊҟtӝÐnEľʁɔҟ\x9f',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'action': '?',
        
            'resources': [
            ],
        
        },
    ),
)


class LauncherLoadExtensionTest(unittest.TestCase):
    """
    Tests for LauncherLoadExtension
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_LOAD_EXTENSION_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LauncherLoadExtension.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LAUNCHER_LOAD_EXTENSION_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LauncherLoadExtension.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_LOAD_EXTENSION_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherLoadExtension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LauncherLoadExtension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='location', name='LauncherLoadExtension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='permissions', name='LauncherLoadExtension'),
            ),
            
        ),
    ),
)


LAUNCHER_LOAD_EXTENSION_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'name': 'ӥł(ĄӫλΫěοȁ&ǘӧфƏȮƢ0g¼Ǜǆ˓ЅзƨɈÌ¯K',
            'version': [
                3364430697694981156,
                -510924606088750426,
                -1589550762270178654,
            ],
            'location': 'ЕȔv˞ȉѓԄʔҨɢӞ\x91ϿƘРȹђɹ.лǊǨʟ1ǥjԬϣˢŴ',
            'permissions': [
                {
                    'action': 'ўˏǚȃ~ȊѴɑѱƕҟμЃӏˍȼůũĳÄӱά',
                    'resources': [
                            'ЯƠԉƵʚɒʇțȿιѿHˣÑÅŎʔŦŐǊƮͻ\x82ϝǅіŵԧĢɝ',
                            '¸\x9b`CƬθž¶ϕӨЎȦJ΄ǿґƷçʈŪ˷\x92ӅǼʏɼϔɀ϶ń',
                            'kȃ\x9aȉҶƅȎΐCĐȒΛ7ʳНAεӬ&ʐѣŪ)OŉӘŝЬϸğ',
                            'ǜԔϑW˸ĥCҀœǃӛȕįʁ;ʖǦϓ]ʥТǠ˔ԐɏαķжġԞ',
                            "ŞѰuзύɴ\x82ҞгʣǤ³'ɄњȜӂӉCʌɩѫŕ\x98\x94ȳџɦΕҺ",
                            '\u0380șӌшѫ˸ʠНəò\u03a2-[ðƠƍư[όѓɇăŤƎΓȓ˟ΤӶˈ',
                            'żɞŀƗşɒ˝¡ҸűƢđwRʯěΟn[ǊѵӰˍюʜȤˈӀʍų',
                            'ƭɿȏʺ\x8aʑŐѹНѪƽÛʬҺ˙˷}юɷǌЏ\x91Ζō\x84˪ν¸Ɔű',
                            'Yӹӏϊ˞ĊȢÍҎʨµʡǍѶſυ~γƽ˴5Ȥň!ѡş}˨ö˔',
                            'ýƏϭŤţν¹іҍԘƠˮȗ҈ӡǴ˟ӻÒƈƥŇʚđŤnԂͲǁ\u038d',
                        ],
                },
                {
                    'action': 'ǫϒˆͼǏҿҷѷіӽńǤҩҐĊ§ŵӳwɘ¾ŕ¢ƄҳȊǢŹӦο',
                    'resources': [
                            'uʋÆёŮǣΆ>ŵƋŚΣϪʀΔʵҀRϊ\x9dԐʓѷΗZ͵ӱŴϝи',
                            'ƴ҃ɍπӠНѧӂˤ˭-ɁˤŇɎŁɻԁғϩ˒ΉԒ~ƍȜȨɨŃЙ',
                            'ѨͳѬ`GǯŪˠȱҰѓҩϗԚƪΪs¥ÞЌҘӍňˊΖқŕ6ət',
                            'ʑаэȇˑɭÍØҕɤϫɪӞǈbʊӻŤǘĮƍʱΌɦʹŦĥ҇Ӟ˹',
                            'ƑӔǨÁ%ʏſξҔĮŗʜăԮņԔƋʉłҀǺ˭˝мÑ\x9e\u0378μǒ˼',
                            'ɪȐʂËƿǹɨ\xa0Ѭ²˪ŸǄȋǙӾ?ʸζҀԏ˼д˱ӂʅăΝˋ\x7f',
                            'МϋѬȻťͱȲǇjǦƣʯΑЄϟ҂ɻǆ˱ӺԂñάѝ˱ǥŨЬ\x87Ɂ',
                            "\x89ǩѝȤюΎͱҬ\x97ʭżʢѺѣ'ЊʙŅ¨\u0383ŎǇӬ˱ĉçʱǱϥk",
                            'ƑϩƈAμČǛyĸɣϤЗӧ\u038bƑźSʘ*ʘұɋϱʴʃ·ҁĴѩɀ',
                            'ƹΑ[ϕӎјВӳΞϕͶЯſӦʇϪǦѢψȬƼ\x81ēŌ8ЀĐϵκȲ',
                        ],
                },
                {
                    'action': 'ҹч_dӊϧŽœΌƯӧθ´ϕˇѝƙѯµ\x93\u0382ǞʔêɇċΩǩϫϽ',
                    'resources': [
                            'ђϱͲĘ\x9bӚǷyȴʿæøǡԖ\x8eˍÈђπ^ČƐԮǃˤњЖúlř',
                            'ǖȌŹ¯ҺЁпɮĮԑƊŋĊϡėʦȼ\x8fĩ˼˫ƁƪʡyɀƘșλԍ',
                            'ĉƏºŷǽ4DӸÎğϲǞЌÌ˅ԏǋҸ©ТóÚŌơæӰˠѕøH',
                            'ǧƤ',
                            'ɽş;ȅĪÐɴǓǘӴʝɿӞŤmЍjļǪKҏўӯÂӭĭͶ˯ѥõ',
                            '/ǎ¼ōŀдàϘ9҄Ӓ˭˲Κί9ˤԫͶђƎӭǖÍėϛϬҞȤʏ',
                            'Ҭ×ϩȢԟиѽÿŨʆ\x9bϷƯɡεéȚчηɏ\x87ԏľќ(΄˸љƽi',
                            'ӰĂȗɞłșϣ¶βŠʋŎδjқЛƽҖˀʂƖɗҧfʭï˫Ņ*ʡ',
                            'ŰѳЩȕĕхĽǧ˄ХÔǥŐ\u03a2УǫŊŎĔʁŌІĔĉǇ`Λ³ʙԤ',
                            'ʢуɢҎƹԑϞŅΨÄƵШ˷щȬːɟƑ\x8dйtɇгɧҞƆΖƢɏΆ',
                        ],
                },
                {
                    'action': 'ʿʐҸӎԋ˄ǽԚÌƱΥҟưȟäΈҁԘҭ˔ϖɈ\xad ύҥɕôÁҒ',
                    'resources': [
                            '˗ȖѢI\x9e˳ʪ',
                            'υˏƋǗѕȗWԖɛg\x89\x97ǤǷ²ƀȸʔЩԬŹˠΌ÷ԞͳԩĭȭĴ',
                            'ǍǨ҇ˆԘҟt¿ȻǙÄȭȪǿҼʟγŉԦшĞŰſСϚӾȟԌϓʣ',
                            'œΌǂ9§ʯѲʥυBѰƧκʻİІƼƨǶҋƝ\x95ӆӟуȢ˒п{Ϗ',
                            '϶\x87ŕËѺѪȸӰХÞďӸɎԛèúԕèƬ?΄НšŨΉ\x89ƈѩԘН',
                            '˧ÌʯU1ЅɽЦéǂśέƒCɔʜӊӥʤзĘǰǝÞʑζԐĵȖв',
                            'XʖŮĿǳõ½ĤΉµҒɔƛмÞ0ɚHƜϟĭƎȘӅΕүϙȤӥǜ',
                            'ѹǓΫƺѐ\xa0Ǎ˯Ƹ\xadÝӦRɯʱԟͷΤԀфǢ\xa0σ\x92žҐǧĀÇж',
                            'ГʾǥđʏǺӟѕ\x8aчҗŞɟóԕ\\=ʀԅƑҳŘӷ˘°ñȨǔЙԅ',
                            'iɍґĕԤȕƉģ.ƼƊ˴®Ɲų(җů%qӪóʮŁЫPΑͻӔˤ',
                        ],
                },
                {
                    'action': 'ʕȧƲȅlӎǀ˰Ǿ6ȉLÂѻӎːΦʚ¾ʔũàҴѥGϷ§įȊɑ',
                    'resources': [
                            'Ǐ\x87įɺѰÊ\x8aƪǤǿƪңв8ӺΰÆǮϼˣϬ˽ɯɠǛТ\u038bиÃҔ',
                            "8©ӕǜԥǞƋ!ҫүҌʮɸɿӧǻӖ'έҼÚċФǧ\x99˧ӆʊéʧ",
                            'ʼΆдænЏƫѻϕǌhїĻ´ÐÊKӺҫƗѽɕԚ\x85ʥͷčˤǛԞ',
                            'ƋɄгҞɯшӈсɆñȽ\x91ȫʮЄOĝʇ\x81αҌƇϡ/Ԛ\x91ӝŖǔ˘',
                            'ΟǓǴīЄ\x88Éɹ2eҼӲƱǢŠφŸƵ˂ŲԬƢǫCˆǌʝҎ˽Ɗ',
                            'υëԛŖϵʡ/йԫs˜Ǿ\x86Ì\u038bԀ\x7fӷ^ʡ\x8bҢԚċΘLŢʘћΈ',
                            ':ĖƁċϗΏġǛνǝ\u0379ĶŸɷЄå˾ɠӤǳǝǃȬӂʈ҄ɊϫƸɽ',
                            'ЬϠʸ\x85\x92ŝǹņǮĕԚʩɬʦòŭrŭɋлoӺ\x93Ț³ԭ²Ǜ˙2',
                            'ËΜ˞ҠεΊԂŮɄϭԤȓɲÓҤƞʀĲʎ7UҨŌӭʛŪĲ˺Ȗϐ',
                            '҃ņǌİƨӆ',
                        ],
                },
                {
                    'action': 'ǢӺóȮƏ˰˫˨*АʹЛŅ×ӭͿҀ7ʲԉѫ˜Üƺ\u03a2ыҡǓϪͱ',
                    'resources': [
                            'қȃŒˤFƘƙ@ʉʵʟΖӘƬӏǉһɊȡʌѕ:ÞѨ[ԡŷкˠȞ',
                            'ȔѮϯԎúÇÔ©˽ǂHƒǍёƁˁěҨԅӎȍŽΏϾϰ=θοҸɲ',
                            'ǰÃ˃[çϧιʢʋˑȧɒʠJԋԬœЕN¦ăҵ˳ǌǕēǔЇ҂ҁ',
                            'ӀŘӼΤƶÍɦфԕ΅ȗËǐӞɴƫO\x99ɋ˪NɷȂØϽ˅ҍХŭ˫',
                            '\x95qԁ˸m¹ŘĜ˨ýŗűεήʞȉɮ\x95ͽϓƞǁоȋФԪŶȦ¡Ͻ',
                            'ǁ',
                            'ӷȃНӃ{uƏĜԈʨϯ\x83έ΄ԉЫĤwÂ˷ϙНņ]˗хƿNҽΒ',
                            'ΗϰňͲΛĴĳýƵҟҚ;˝0:ʰЀpǨқ˃ϗήԋєʇѢɁ5ƹ',
                            'Čė üǪҷ\x91ιɎàςðαǨԧȓƓ°˹ǫǏ˱ŊηғćʂǄˏП',
                            'Ѷ2ƭ:ʋŚҊʍː;<QбҖǙϳʜ7Ѷ\u038dΘɸф˭˾ȄʳȒϷɏ',
                        ],
                },
                {
                    'action': 'ɗĻΐđԜƾ͵ħѷ\x86ɫОİХA͵ĲƉΫɐ˦ˉѿϪƉԮ;Ưƫс',
                    'resources': [
                            "ОnĈƈƿͷȐ˺Әĕ\u038dΩҏÈ_ϼѪӡѦ§ҭӍśэƜøɿƑ'Ѯ",
                            'ġѾǕ˾Ĝϝʯ¥ȑǐǕͿ*ΜͶԒȀȨƃҢȦаʆѡЀ\x84˪ˀЇӭ',
                            '¹Ƚʋ$ųҤǲʄȦԕѵƍ\x8bρДИɨВрȖʶѐmŷ{ȌљŃҟо',
                            'ҡԩҿƵøÿȞǺѡǀÝƐŴRξȒΰҽŠӹɼO.ƨ˙˘ſĈŜŌ',
                            '«ȡĩǉ\xadεϑÈ;˚АėϞх\x8a[Ϟĝ\x82ĢԘʐľкƛ\x7fиŦΊШ',
                            'áǻũЯ\u038bǐӇˑӋӴύ˒ԣɐ-ȳɻϐСɥȓδȯѺҿȮнрЭϏ',
                            'ϺϥŦɭȓŪѮâP$ȿҿʏʇȼ\x8fø˥8ƸӰӧ§MȒԌɹ\x91ˍƦ',
                            'ĶХ˯ďȱǭǯȲԅӶ\x95ӄ;ғЏǈȌӸįϠĘӧӽ˭hǠͶđNѹ',
                            'ѷыΟƺ+\xa0φęь«ǹƄрӔȫԏȸӔáƣԢȋǤҩ¤ɕ´ąҬϩ',
                            'ʣɾ҇ƋϲƆƨȪķЀǵӆȅͻъúЗҫ-џŔЭӻаȏʰҭĬăǑ',
                        ],
                },
                {
                    'action': '¸ȘЂûϠӚÏŋүҙŠȯʑśȥǏϯŒϵǑҷȦҁ}Μɡe\x8eӮ΄',
                    'resources': [
                            '҂çĶòɀϒ\x9bѥ#ɋ?ɶΧОШɸʧTљǗFß_˳ϋŌǬȨŜ ',
                            '\x80xÝˣȘȬǦͲтiūҠ',
                            'ϖ²"ϩ?жȣҙʕȖЋ',
                            'ɳͱΖԮϻԍ¨)ƙ',
                            'ˊɍʱlšʁ®ʔχӔˇËɅҾ˴ȤğеΚ˓ǳ˟ŷԈԚӑï\x9aƲҞ',
                            'Гч0ӛǙÓºŲ~ƦŉƑԍǍƳ,Mʜ]αҎԕѤΎƲĀůΩÑϐ',
                            'ȂҿǄѹÖȄvĲҠƩϻҡȖОƣԥȫЬGÛǲӦɈîɈĲĜŔbϴ',
                            'ź|ԡэЖ˪ǞoѰΑÍÝʿԣ˪ΘĐ҅зɁ˟ȍ͵ʥȒӗΈ\x94ȼȾ',
                            'ǚʕpʍœAüˍƻdӆј˕ƱҵЩđκnЮӀVϮЕɝοǜ˲ǳϞ',
                            'ƮŋáƏŇ˼ԚɁńÊƋíˮ¹ȍѫɀ\x97б\x85\xadċɇӘѽΎŚѤ˹Ĺ',
                        ],
                },
                {
                    'action': 'Ҫǌ¯ѧ½ʵӂӊȢώEӨФȶAҹƗ',
                    'resources': [
                            'ǜƌǳԮˬ\x94Òƍː\x82ȲǡΪõǊʭůѧκʓƎӦŧĬêÉҗ!\u038dΐ',
                            'ңȻH˰ʳàśſΎû',
                            'ԓˋťįМž҂Гľ=ϭΒˢϊǠ{ŐȅĬάŹĺҙȒƧӡѓƔEǲ',
                            'íĔҹƘёʄиѲɖΝΉɾ7hƴɽӈРíƊɹСԃѺ*ϚƑȀƇ\x96',
                            'ąɢÈΕӷ˦ƹөƘҟĉkĒŠħð#Ϙҋ\u0378ʈуМϾ¬вǯjʔġ',
                            'ØӺѣ7ρņʥÝШQӜґʔͷIĢϳYʟĝ&\x83ĻȵΐƸѣҁΐ\u0382',
                            'ѬqҮԃσσҎȴ˔ɇȿɆʶЀ¦ͼѪĨÐʕǦ\xa0ŌƌƚÎ>÷Жĕ',
                            'ŵɬȘϪȤ˾\u038bǳЊLɵʷå%ғԪCѳȩΦȡȕĩ˰ɍѨΨɛѯΜ',
                            'ˉǠЈҌЕųԖȐђƁÎͿ\xadέˌʑχÇΞΟҀкΐ˝МƥƎS҉ˋ',
                            'ɵƚƱȝӫǡӁƳĮ(їłоЗ˾ϿɺåɊ°ɀǥǷϫɨϜʮʈ˲Ҋ',
                        ],
                },
                {
                    'action': 'ĮýˤòÎȜϔëɁίƴǓΫƽ˷ǇӁ҇ƴЈ҅ȓϽƦÈùҠ\x86Ɯθ',
                    'resources': [
                            'θĩRϫϖϏӄΉƩԊИѡƠҪÚӫȿһԨїȄɳ\x85ɁǸƆóӈҳ˝',
                            '\x92ќɖȌӏơ˰˹ȵ>ô҇ˉęô\x85ξLҝŗZQƿȣԤ;@Щҧ˼',
                            'МɊʠӞ}ԐҶÇΒ˨ÉȂʶ҉ĦȰIѻϽ)çӗǫΔĦƊұ͵ʃƫ',
                            'ƺѿϫȢƺˁɷҖѾʱ6sȨƒҏΒӖЏқҌԜ˔ΐӯʃʇӽtԄК',
                            "\x92˨ƸʽӈƨкЫȒĖϷɫћЗʟĨĨƺɹéʡñèҨǨӾЉ'ӷҺ",
                            'ǋǷŤϡǇӡѨÇĺǸȪʹ)üΙÿ£əѽʯȫ\x8fӈ˯ɹ\u03a2пåҦȓ',
                            '҄Β~ɅūȕȄíʾңԨ˙âЭģ˜Ł˳ʒʳνƙƖɥӃɩþÎΔš',
                            'ѬǂϹԜĵ˒ҟļ^ƶҺȏ˵ɫҡƍƚ˻ɨİΣЭȁͻј^θ+Pǲ',
                            'Ʃθ*ʄԄÛЕʖҖÎЧӗʟмę˘ű ͳ҇ѝ;˕ưǆƒԉȀíђ',
                            '-ʨӵđӑΊƞ.ʛʷ¯ɇȌΰǧ.ԖϛԐЋŕԤMЊʣgŮ˔±Ȋ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'name': '',
        
            'version': [
                6231087559045104818,
                8504060798640655192,
                4011163119166096766,
            ],
        
            'location': '',
        
            'permissions': [
            ],
        
        },
    ),
)
