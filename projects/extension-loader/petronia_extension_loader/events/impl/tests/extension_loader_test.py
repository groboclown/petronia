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
            'name': 'Ǵʿӕˀ˛ѥå˕ƵɛŢЭÁǨНŪԒeżҫȣʬˉМίӆӵЂͻΊ',
            'minimum_version': [
                -5424717300807159375,
                -3296407945212610959,
                -6857553305458092069,
            ],
            'below_version': [
                -3521424596640177183,
                -227349943578042377,
                -5450613740913303478,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ġ˚ѵ',

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
            '$': 'ʎӰ\u0381ҥȾʞΟԞʻQț\x8aßш¬ԊMҟ\x862ϛ˵ȻкŜŘˎıĶҬ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4439162840429276640,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 780937.9019946639,
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
            '$': '20210910:161342.025563:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ƃȶ¬˜Ŕ˼Ή&˕ƟӄɡƭʏӄˠĂĸґþʾˁͶΣɫΜʅÑԬÔ',
                '΅ȼѐ\x7fĖƔ@Ģ3ϴ\x81\x80ŖӚʔөǛτǙͿЮЦåp\xa0ư¤ƪUԊ',
                '˯҈ϺɒĚԆżʂɧӗΙɬӀŬƆχƿ\x80ĴХ˙ΕѶӼԊұȂά\x8a§',
                '-ǨɚдaΆТј0ѭ\x9eŘǹҝӢėӂęΓɲªȸŬӁǰă²ëûǒ',
                'ȺʼϬΟƠ˚ɐӵ˙қÛѭɦˇӬȳȎǷԉϾƹΞҟƺ˧ŠǘǶӘ+',
                'ωƳgǪǤ\x82ҷƝКɌġ\u0378ыѸōԪȪԡØ;хпƯƐϨʕƐ˪¯Ԕ',
                'ǳƇѹњǵѲǼ\x89úӾ$ŖѢЊҎɘѰǢӧăƂǮȩΡŎЊϥӔżЪ',
                'ǐ?ĽӝöĽŖ˩Ȓ\u0383Ʒ´ɺɚŎ\x9eÒѮ\x9eӵʌɹψωʄǎǵŐӄǼ',
                '\x98ʘˤ2ƻÉ6ͱʫюÏɘĄΎϪ¥',
                'ȥҋù2ƥĢǽұǐĿ˫s®ɆΠΈ\xa0©ƧаɾӳȤΣϩХҵуɄѰ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -9132290828303419442,
                1373697109457244587,
                -3642245228379882224,
                7265070931622589657,
                6185070845708537023,
                4168892672560316159,
                782388469665195614,
                -5620171760450131529,
                -521960640580401917,
                -322503846383756633,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                907900.5971262077,
                254297.7783365653,
                5200.846151760823,
                776439.8457634328,
                216833.66706428007,
                -66306.9631975909,
                485010.4319958652,
                675327.3811487405,
                655194.6463932191,
                -45930.76711933638,
            ],
        },
    ),

    (
        'bool_list',
        {
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
                '20210910:161343.128814:+0000',
                '20210910:161343.146169:+0000',
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
            'name': '\\яӥďƴδĚȆʗҚp',
            'value': {
                '^': 'string_list',
                '$': [
                    'ªЫͺƳȗ˘Ϸ>ӛ\x85ÓϐΨŹηɥьƙʜтҋ¤щҕɂǔаųϑ˙',
                    'ҾϼŎӯıÁыҰŁʒЧ¶ύҡˆ\x9aɾJʐWßȟrӜϹʮГ]ǐЗ',
                    'ˈƼȷŵαʌԓȫ±ƝbũʳЏӋɡϛ҆ɵÁгųҒñŤƹʦɽϘӃ',
                    'Łĥ¯\u0383ŝҦƭѥфεӯԬνЬã˘īӋ\x8dҜÉ7ƶҎªѣ\x9bĲϫӾ',
                    'Ƀƛ¸Ʀ/ԏęͽŬӬ\x91ůʡ˖éΚɮ˂öōҼʼǢԢÈȀӭʋʛʵ',
                    'Ǆʧ\u0378ԖĸɵʼÃԅSɛҌõǩȳπ˟ǐĸФʋĂʝƐȖĬȞƏǞ\x98',
                    'ɑƏ.ѡ˃шΝˡôʿѴ˲Ȓ˨ȍӍűǏJΠɞÑԜWѳȿҥˑǴϥ',
                    'Ⱦʷк;˄ǯ\u0383ӕԮЊ˩ŇҬŭͱӜŒŉӋЊųΈϳ\x93ǑŊȷƆӢJ',
                    '*Ӳ×\x97ǧԘӀűFŘѽôČϨϔӟӯǥǮȤʋϰaΪʞϴɕӲʙǶ',
                    'ΎŇƐ\x86јǊўҫȳҽŽϋε˦ӳʰͺƉƐӷƮЉƑҟӨžҪϽЎϸ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ө',

            'value': {
                '^': 'int',
                '$': 2556974836029229152,
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
            'catalog': 'ˑɜȾЭҊԣ}ŗŭΉʣ\x86ϴɇǂ\x85ǹžԐѴ˙ғôУȵ˂ʓǘȬҡ',
            'message': 'ˁȮqȸȫ²ǨуĒӌ\x93\x86ΜήОPń˅Ύ˛ҝȼΘɛɖʟԨлJӨ',
            'arguments': [
                {
                    'name': 'ӱƼʾɴĮЮƁÓСdĽȌΏ\x9aȕ&ѨъПқêёΘɴȮΩ˂jǎġ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:161339.778813:+0000',
                        },
                },
                {
                    'name': 'цȡǑԈɰѧw{ÆİǥlĤūɄԍԂ^ǯǛϤϮ7ěӿεҶuĴҡ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        499860.77734546585,
                                        359263.00917567784,
                                        90483.34917166462,
                                        875694.8331247767,
                                        304215.7168898224,
                                        13192.723372824941,
                                        -72299.09951067898,
                                        597817.6434376746,
                                        554422.0880726769,
                                        511733.9434871144,
                                    ],
                        },
                },
                {
                    'name': 'Ǧ˵ȽɣЮӀɆϝΛǏʍʆӤȂҵ¦œҾĚØνЂ',
                    'value': {
                            '^': 'float',
                            '$': 201123.6199437604,
                        },
                },
                {
                    'name': 'ѭљѲԪǒӶʴ˛ИϗʏȖϤŶґӠĬȤĨϪӦǽ!ħǸΑσѝĕƊ',
                    'value': {
                            '^': 'float',
                            '$': 141944.59593843692,
                        },
                },
                {
                    'name': 'șєԞêǴΎ˭ӔфΞ΅ӰȅʶķʪѾ°Ǡ\x85ǽ\u0380ԥɒőɚƶώíȁ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210910:161340.311680:+0000',
                                        '20210910:161340.332503:+0000',
                                        '20210910:161340.353895:+0000',
                                        '20210910:161340.378041:+0000',
                                        '20210910:161340.402506:+0000',
                                        '20210910:161340.428743:+0000',
                                        '20210910:161340.447197:+0000',
                                        '20210910:161340.464763:+0000',
                                        '20210910:161340.482632:+0000',
                                        '20210910:161340.502774:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ǀҙ΅ıӎĸKˉˉχ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'UưԃҕѢӉ¯ϢƢʡÿůşŨіΫɐɑРǝѵϾэɼѠѯɉɟҹɟ',
                                        'ҀԏuFѽҀˬΠ҂ɂқÊзʝ˕ƯӆѽҋҡƒӥЛθјĄȩ0ԑă',
                                        'ϒcǝĀϱĻȱɆ҉ƺCǵοǘȞ˫Ѫj҇ɹ˽˗ÐÞӼМȪɊɻƮ',
                                        'ҙҤ˕ВԋӆÿǁDЙӥӺʤǴ\x9cрĽϗӧхʑΚԚ9ԝͺ҇͵ʐA',
                                        'ҟϳˑѼɞʼÒӍҬƁKϾёҬ˾рȔԁѺΘзҊʺsҴԃg\x8aȂϛ',
                                        'ǫʿˈ\u0381όӜĝʔ\x91zͼǜΖɢʫŚ²ɂɩӞаʮÔƵ\x8e˚яzɆĝ',
                                        'ƩӉӬǔğʝʭѷ˨҃SŅšpΪȠŃř\x8bӘԇȮ˔ЧԠԁÅƲǒч',
                                        'SǩɀƷĨŮә3ȸůŊ҅8Ӧxxȣŵ˳њµɂÂ¦ȚҮыëȶЪ',
                                        'äӝɡ˼Ұ\x9fǤ0ŞԦ+@ƳûXĒи?ÅȗϋɊcǽϫĔĝϖ:Ŧ',
                                        'ļѺZɷ\x96ΰѷȺȂ˓Ⱦ˲ʜȾhԦȃĦԢĹΌȍͽњǣйиɱˏh',
                                    ],
                        },
                },
                {
                    'name': 'ƀѕÊŻҷЌ˹϶ѫΏTӗƷңѸơťx\x86ɜӒ҈΅ƀӇȡȤҐȑȓ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        True,
                                        False,
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
                    'name': 'ˈϚԠ҇ÿǦëƌϹӣȳ#γϞПҝUʲӾѱԂ\x92ϴĜǠΈ',
                    'value': {
                            '^': 'int',
                            '$': -628022368709302675,
                        },
                },
                {
                    'name': 'ѳԔȉЙÛȬȫЀȋĔ\x95ϔ\x9aǠƺ¯ЇɾхПȓȗӦǽӂůʴЌƖԘ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ӵʙМӘѨOъňӇӂҮΐƋǛȽ¾кϴιÖŔǍ·ƯÏϿņҮ˟Ɓ',
                    'value': {
                            '^': 'float',
                            '$': 925755.9923769996,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ɔȅ',

            'message': 'Ȟ',

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
            'identifier': 'ԈƟơĖџîяÌĠЌϯѳµѲ`ԣѮʯʦӰʿ˄ИĖƮ˕˴ɚɃK',
            'categories': [
                'configuration',
                'os',
                'configuration',
                'network',
                'invalid-user-action',
                'invalid-user-action',
                'file',
                'os',
                'network',
                'os',
            ],
            'source': 'țøτǲ˲\x8dʄ˰žªż´Қ˞ĔʘϿƏϋңț',
            'messages': [
                {
                    'catalog': 'Ӥ\x89Ǉ©ΘlƊΚΒԘ\x93ɯԐиęĊ\x7fAѤАԬǢΪԓӣƊRØӵҖ',
                    'message': 'ŁɪȺĐЭŒŢβ\x85Н:ʀƿɝκɈӴ\x8aѷӏǝŝZӎϭҖʎЉþǃ',
                    'arguments': [
                        ],
                },
                {
                    'catalog': 'ȅ²èÔĉɊԕбӶ˾ɚϑÔЋFôΕӻҮτѩёɃʉ$ÎȌÑσͶ',
                    'message': 'өі\u0380FѰӇǆ˜ȁŔǹȳƟďϽʆ˳МɔДķȤƙ\u0379ʺҴƐƤι\u038d',
                    'arguments': [
                            {
                                        'name': 'Lcȸ7OԒѺ/üԈϣʀ{Ґʬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4426912987984565263,
                                                                            1165957833387476236,
                                                                            3003061969668917125,
                                                                            8551398332515484920,
                                                                            5923194806703596934,
                                                                            -4681474432015137921,
                                                                            -3297817553585935238,
                                                                            -3938480274127563430,
                                                                            7425253692811855910,
                                                                            -4235257610519979452,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԗ·ȳʧΏǷ×ʫûČѝ\u038dDԅƻɉä¸˩ЭçlʺҨ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƹ\x88\xa0ϩēɁрʟ\u0380Ʊґ\u038bԄǅĸZҞϐҬ\x9bʯɋȤΊ҄ō#\x80[Ԟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4115416164300345627,
                                                                            1596202363768806500,
                                                                            -8659432277625617396,
                                                                            -7078439706746321335,
                                                                            2121396193661155463,
                                                                            5818856594502828285,
                                                                            -3814108910078614791,
                                                                            -8819343392903023552,
                                                                            4052327038879571447,
                                                                            -4379550385157469082,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʙÅ`ˇǗ2ӚҜaȐʙʼԉüʯKхȖ¾Ȫџ9:кгԛѩŅ҆л',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ųƱɲӬʆЖδʖƝ·ʟѨ{\x9eÜ@ŰԬǧγȉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6992266396748342252,
                                                                            -8767076286459691483,
                                                                            -515088428609640287,
                                                                            -3481984353108705207,
                                                                            -6135390141732938010,
                                                                            -6967596348187452573,
                                                                            -2481873259774503539,
                                                                            -1226240278013117484,
                                                                            4639726893634390480,
                                                                            -3920097819859059674,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԏ˽МÍЗ9ˏʗʽӕԗ˪{ΕƲӜmŘʚԭѝ͵ςӼɫш҅ǞŞ\x9d',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161326.416981:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӕЏƴΌʌǿķʻԖĕĀάϐŐcɭƐˮЉɎʋ\x86ӕĞΔëˮůЮǱ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 18514.961154997407,
                                                    },
                                    },
                            {
                                        'name': 'ЎΟŸɳ«¨ĪǃѿȍŻѽԌǁυќϼ-ХѿˮŃOϳɧɴƬǠϡ(',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161326.568443:+0000',
                                                                            '20210910:161326.586010:+0000',
                                                                            '20210910:161326.603925:+0000',
                                                                            '20210910:161326.621799:+0000',
                                                                            '20210910:161326.639589:+0000',
                                                                            '20210910:161326.661095:+0000',
                                                                            '20210910:161326.680106:+0000',
                                                                            '20210910:161326.701683:+0000',
                                                                            '20210910:161326.719275:+0000',
                                                                            '20210910:161326.736873:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'лãӐώʻϡȢ\x9bǒĕӚπѓдθѦҺ˝ĩΏōт˧ɕөϜϩˊΔǢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ԁƫ˪Þɓ˟®ɬ˧ҁȝ\x88ΞБȋʵȈȳɡ҆³iłƞФŔÜҋ\u0380˥',
                                                    },
                                    },
                            {
                                        'name': 'ϒӰǨʣÁSԦΪĵʟƹɼ˅ɸÕЯ΄ɅƓ+RͰ«ɗč',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161326.907173:+0000',
                                                                            '20210910:161326.925311:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƩӮbϳϰƶѲȴйҺɪг',
                    'message': '{ǯ\x90Ԛ ϟѹīěɘ\x83ЛԍǢӮĺɟфКŐǬ×ϾģĀӃѭЩõӦ',
                    'arguments': [
                            {
                                        'name': 'ϓɩӚԀ&?JҩÅ¸ʌµјʆÊȩȯÑVÙ˜ĳāˈЎу҉˭ԫƻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -24841.31609931626,
                                                    },
                                    },
                            {
                                        'name': 'ĜeȢϘΫϢȄ¦ƽ>ǍŶĥҘ\u0378ԙщʸąǤѿǃśȀ¡ɡÃťųН',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161327.168480:+0000',
                                                                            '20210910:161327.185071:+0000',
                                                                            '20210910:161327.201879:+0000',
                                                                            '20210910:161327.219028:+0000',
                                                                            '20210910:161327.237406:+0000',
                                                                            '20210910:161327.256921:+0000',
                                                                            '20210910:161327.273446:+0000',
                                                                            '20210910:161327.289980:+0000',
                                                                            '20210910:161327.314959:+0000',
                                                                            '20210910:161327.337300:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȋĬ',
                                        'value': {
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͽу\x92ǑʛρʭȣɎȚȳ\x98ҢǂԛȂјρѰƆ˺ĴǒɱōŨҰģɿɯ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1924886503574528920,
                                                                            5796515866278509887,
                                                                            -6265354110489212851,
                                                                            -2967790353118385395,
                                                                            -9109050385573970150,
                                                                            -1315192693764782839,
                                                                            -6820262302037892754,
                                                                            -635737098583192583,
                                                                            5566063630456969872,
                                                                            -7066399738712640875,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʣɖԌ`˟®ǠɏȄԢĠҦʎ¿ǲǃ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            415946.32880548405,
                                                                            -28941.53403112371,
                                                                            -75052.51920432791,
                                                                            923676.9583015055,
                                                                            935417.9592512762,
                                                                            668574.0423482662,
                                                                            498870.07716327417,
                                                                            278714.13266014436,
                                                                            962601.618638332,
                                                                            43277.35987922372,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѢΚ\x8dЛПĜȃžǅÙŏмͺϹδӍΏϭǃȤЀɘƉѰãˁƒƽӼҵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161328.217238:+0000',
                                                                            '20210910:161328.237799:+0000',
                                                                            '20210910:161328.262581:+0000',
                                                                            '20210910:161328.279844:+0000',
                                                                            '20210910:161328.298389:+0000',
                                                                            '20210910:161328.316598:+0000',
                                                                            '20210910:161328.334072:+0000',
                                                                            '20210910:161328.354359:+0000',
                                                                            '20210910:161328.371813:+0000',
                                                                            '20210910:161328.389122:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȎΘ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6428575289461549771,
                                                                            6203404731058604375,
                                                                            6808190999727599942,
                                                                            -6429750612445990881,
                                                                            -3968495869078649653,
                                                                            4983637929577250725,
                                                                            3404468082407090846,
                                                                            -1045116667457058136,
                                                                            -8348472606720238768,
                                                                            3874767422255086813,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʝ\u0382Ѻǵ\x82ҷ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4142426322352652848,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҋӜʆϓĉÏΩȔǑ˜ѪîӲĹű͵\x89ʄwєԠ<Ѯ˨εʙКŋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ϝҀʄɥ.ʗҊQ'˾ʸɒŹĎïkÊį\x87ˋʿǡƳÀфgȪҷύƯ",
                                                    },
                                    },
                            {
                                        'name': 'Ѽșǐ\x81ʘҍĵƑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǥϧ\x8eΑĔ`Ȁvǽ҄Ɓ\x8cêSεɄϝɆȾͽƜˢıӮǒ˴űЖŨǖ',
                                                                            'ŅϙтŭʟйѶĬӚҁȺΞӨȃΩĖѣʑȨÂɲɀҧ÷ҽ5ʅľ\u0382˟',
                                                                            '˘ʄ¹ĆȃҁɚʏҩѾɰϠ˂ɱǨːԃѮĮЈƦѷΠҧàçŷбŇǊ',
                                                                            'ӸаȽҾ˘ǷɁ˹ǀȬ=ЪÔԪĘԕԍȇЛїɕϑȚǦĢ*ƧɹĮ˳',
                                                                            'QɛԐӰшΠɍϒʤǙƪЍ\x9cǮԎǠɬѬɷĨƭvйԘԛЇʴӡβѲ',
                                                                            'éΣӢÎǿǾŠΪҧ\u0380)ΡaȶˢšjӸԉɖҚΨȀɦǮӐԣOóĎ',
                                                                            'ϴ˃˧ĽΨūŨŕ·vɠöЁ˵˅¤ШԆɩ\x90qGŮβŁˀͰЌƸˑ',
                                                                            'Ņ×ԗϳϋęΣ-¬˄éӹȦúĢŧѷƴɫżǰ*ʣǳɧϼ)Ʌ˃Ƃ',
                                                                            'ʛŐɃÄÎӷЙҳµƖΙ¾ӼǛʷşɉ\x90сîÛSΙ+ԄɡŔ҈ș·',
                                                                            'č\x9dʖǌ˽ӝÀԃ\x9bГӫÛȗyāњƱɌǡ\u0380ĽͺІ˦ˊʮЙȯʦA',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĆκҷΞѵӂÜЁӪфЄʎ\x9eѪΖԨīѾӃԌĢđԅƓǴҞƑOҌφ',
                    'message': 'ƬPqѿȡ±΅ϡRr°īӧ\x8cεåɶӢίӁӷŽϼɗØ\x8aȒŎľѼ',
                    'arguments': [
                            {
                                        'name': 'ЗӓҸτȂȟǧįήϖßӲ/Άɳȃ\xadͶѕơȘ˗LδͶμ°ƪѥӾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7357397009620151624,
                                                    },
                                    },
                            {
                                        'name': 'hϯмÎҔӡҁη΅śԄũ2ƗѷΌƙĩΝӺȻςÕʞϷǑũ\x95ӡp',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4797792730806222174,
                                                    },
                                    },
                            {
                                        'name': 'ƍˮðѮҙʣ8Ì¥[ϱêѳɟQ\x85\x84űҏӃνɑçѸɓʹ\x94Ҙĭ.',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 519805.01019011263,
                                                    },
                                    },
                            {
                                        'name': 'рġʥϬĉΑʷŝeϷ˄ɖŉɯ5!¨ӿӗтƀɹ½ŷН¢ˤҝҮɍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            6384.697362216204,
                                                                            712696.4797005104,
                                                                            137709.81233659925,
                                                                            775494.7538591373,
                                                                            780971.4000188174,
                                                                            587710.5602611939,
                                                                            67545.28091096116,
                                                                            872351.0462605745,
                                                                            4772.497129540978,
                                                                            688695.6112966592,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'љӖtϻѭƣ˝ɓАӘưǘêȁäƃŗĆǕԦЌƐÿЯĠ\xadГʀĮˌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѱӯ®жĈơĕǉԣ#ƖПӌϴԀɢÕν˞ϱ^ü\x94ҭБđɣҋѬҎ',
                                                                            'ĲɺɕȫŤʁĘО˰e\x9bӻ¸ҹĚϑƜGʾƪˋ\x801ƔŜņ(ҞѝĚ',
                                                                            'ƿļϽӼќ˩ȵ+ӧʦƒ\u03a29О¶Θ¦ӌӎǒòϘΛˍԫʔÂiЪͰ',
                                                                            'Πjǈԟ˼CɃҗϚIϐϴǬҳ#ŋЮbǮƗԂԤGcʲҎÛǪƃ1',
                                                                            'ʵӦίϧNСѪcʋВ˹Ϧԟź\\ԏ\x80ԍǞǩ9ĩѐЍ\x8bϝõΐéӱ',
                                                                            'ΩѩɵИ=ѷų¶ĬϺɥƈďѷԔNҲǱȦЏ\x9fϿ҃Үƅϩӓƛӏʃ',
                                                                            "ŔƠϪȳǝ}ɲɮτ'g˦д{ȴĵƷ\x9cЌʏϬѓӯΙʛӅƘѮζÞ",
                                                                            'εŖÀ˦Ɩ˻;\x94§ˠƓĔ¡ǹʥɻɣԄÐ\x91ĞӸδɌѮďÁʮԔԞ',
                                                                            '#ʬԡмºСѬʼʄıѼΌŵʥɚÜ\x9aɀɢŖμԊϛH϶ԅМè¬Ʌ',
                                                                            'ϙȧҤÑ˱ĸЛӢɮó˾дѤє.ԦјҘāƣĤ\x8eȖԘǲƭcŵʎɚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԂȣʗȖͺK£ðΣРǲȈɕŝǖЌǻМǗɐҗ\x80gƄÅɱ˶Ʉ\x84Ќ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʁcЭІÚkӑƱƾ%ӮвқƕҟɬĐЎӰһ6)ҹŉʼȬ\x98ӌЫg',
                                                    },
                                    },
                            {
                                        'name': 'ПͳжԒĞˏӰǢќͿǀИӽӳϊþOҽƞȎ҉˻ʝӻѵő˥\x91˲ό',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɊʰɳҪө',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'УɘǱԞ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161330.960759:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɱƈŨѷǱŒǅȞƱɢʰЦϻΣъԗҜʒǏήƯʲ\u0382ƬɎѐЩάȩʦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'әͰȘԖƳˤȐѤˍɱâ˕ɬƷѲ\x9aƩ˲ˠӢ͵)ưΥ˧ӮĒδŶʭ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x9a҄ŢǯΕǇÂϕƌCяáǺΤŌ\x84ϧԓĢўˉƤӥŵƐЏƼʵBԒ',
                    'message': 'ԔśˠќєÚƗєš\u0383ȩ:\xa0ŏΤ҉ǳεҘKўΦЎѾҩЈǲϡŀǲ',
                    'arguments': [
                            {
                                        'name': 'ĖȼĐēɴєők˛Ζt˩¿1ҡȕɭҎ®úȄΤʵș\x86Ł\x87',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161331.198807:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ɍ§˭ÊԏHϢčӻӷȉϦѹĜԃĸѨȄЍÖɗЏϡƒѠ\x9f',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ψʻЂҬΙ½ʳǺѮǹΑɺжѤԀӲϕĲˎŕɣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 868997937369389614,
                                                    },
                                    },
                            {
                                        'name': 'ÅŒȫÒӒԏƎ7ĳЋÚŔşƤԂ˹ƖіǛЃɣʒīˆκЩȳ\x89ћ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '϶Ёņ˺ʫйǶŐ ¼ǲɑĹЯҘƃÄŽĨǋɤ\u0379¡ùcʝɑ˱љО',
                                                    },
                                    },
                            {
                                        'name': '¨ΪԂȺҌҕѸǨΊUrѐѬÚ\u0382Ýіà˾ϢʜǇǥþȴŠі',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8669253451280412240,
                                                    },
                                    },
                            {
                                        'name': '±ϜǚЈɺΝ˫ưT]ҡˍыÉ˯ǟuʬͲґˢ¼Ӯðԓɳ\u03a2',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3964932802360999351,
                                                    },
                                    },
                            {
                                        'name': 'Ǖǁģӷ®dӘíѥωzͽǍτԔ\x99ŘāƦíǡöʗјÐǊ¸\x90ӱþ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ѝ\x87ëί˫҉ґӒϭȿԀĚВ\x8bҡξ҅ɍѪӿеe˼ȖәјѴη\x8aȒ',
                                                                            'ӕϪɾϯһдǅҽȂͽȿȶɓȾhĝȲҕΐЩщʬʧĔ5Ķţŕϫҿ',
                                                                            'ӱǴDǺFϬąˍĹϔǩҩáıϸ$cƚɟ·ӃҌЈƸ¦АЏӚ!ь',
                                                                            'ΖˢˀԟŅè\u0378҅ɰҀɀȋЋigэƧΝһêȖӗƖ`ŲӈќżÅȜ',
                                                                            'ïsˇđԅѠÞŞΧвсŀ\x8bңŀǈÑќƍӷŃǎÚÙƌʋϸѽǨÒ',
                                                                            '\x8d҂ȨԂþӉƩ(ÏƴҨ˃Ҍˎɚą±ӽ˼ɁȸÇ,ŰʐθѯŇӣă',
                                                                            'ʷŴҝǫϱҚGř˚ʖ£ϩƩŌǰlČJԠ+\x83ˢĄӲûɈȌǸɭś',
                                                                            'ØоŔΦИȜˬćŶSǧθўƀûċ҉¦SûΨŤΝýĚɱƃʼģԖ',
                                                                            'čġ˒ήCɪģԟԊȸÒǭ@ƙʧʣѹÅŲǷȂӉˬύƑмȂΨÐћ',
                                                                            'èҩŮҘűіȝɺł;üĨϾԞŧӮÓƵwΫ\u038bԅʞƄŔȥɏĬəè',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɻƈӣůЂȧɛƵΝΘӀ+gəϓȮѓǧ_¶ы˞ʨЉȠ<Ҡĝǫʎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ǧ˽ϷəɚŬβÎͺˎǶLӹǒŢ<$,˳ƝҸ˨΄ҊóHʛόƣų',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '}ЪϺӄӣʹǟеʹòϘ҂¢ͼmХĊʹ\x84ɮù҂ѣԪφÂĕʳԙī',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÿϗjǼØӇÊγ\x8f\x97ѐłͶpƣ˖Ԃҷ©ɔòҋʭǺʙƉғǔΑą',
                    'message': 'ȳϦ˭\\е]Үmɦμ»ӉˈћɌЧȷŵſ˥DŇҸ\x8fҽ\x8fʰ΄Пģ',
                    'arguments': [
                            {
                                        'name': 'ǢʅӄѿrԟԪIʍǒæƳuġҽΧK˟ʫ҃ŊɫęӖĽɊώŀŁŢ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ťƍтçɚ˝˩цĄѿɌíЬπʅХėƉƯдōǾϠфɍĥ¨\u0378Ӟƫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ēˉŰǵÝЬʂȶѷõɃ\xa0iĤИϬȢȄÇŵǱυŢЄŔʁʑȚƴN',
                                                    },
                                    },
                            {
                                        'name': 'ȺɢȎϠƹ£ǿ˜ϑh',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʻӢϘǘА[ËrÔŌťʌĀųşÌ˘ƬѢԄҥўźͲçďϚǫҊχ',
                                                    },
                                    },
                            {
                                        'name': "Ӂ\x97μεʾʫԛӻԈ˅σˋĻӼДύÄýƧЊ¸'ŞʐũЋĞӠҁŪ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161333.214010:+0000',
                                                                            '20210910:161333.233932:+0000',
                                                                            '20210910:161333.252003:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȝďŕǾ˓ΊйшϊԟɳȒŋȜś?',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            938630.1824588791,
                                                                            982838.0518488544,
                                                                            875104.4520080246,
                                                                            375554.96649436577,
                                                                            548073.9603026096,
                                                                            918652.0077795156,
                                                                            434853.05533175915,
                                                                            30874.502179405565,
                                                                            559373.3937374132,
                                                                            -79570.05942904585,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɌԖɥҭжƒРvѦ˅ʝsǡʍŋʍ;%²\\Ťόԝ`ҶŉĠѰɲҬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8944538491871356722,
                                                    },
                                    },
                            {
                                        'name': 'ЧўЖΊŸϛlŽɕϮÐǾʈɀŮʰˀķɆʟҸˆѯ/ȾΦɡɹȐʟ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 119915.80502883537,
                                                    },
                                    },
                            {
                                        'name': 'ԝȺǪѓˤŽԡԬԆίăsĆȼĕиΙĎ°Įȫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161333.790641:+0000',
                                                                            '20210910:161333.807740:+0000',
                                                                            '20210910:161333.829745:+0000',
                                                                            '20210910:161333.850815:+0000',
                                                                            '20210910:161333.872066:+0000',
                                                                            '20210910:161333.893067:+0000',
                                                                            '20210910:161333.913899:+0000',
                                                                            '20210910:161333.932408:+0000',
                                                                            '20210910:161333.950257:+0000',
                                                                            '20210910:161333.975376:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɠԩүэӾćӼσϴ¼˕ƥӀ˗ŭіūы¨҄>ÂҁǮͶʚҚǫϬȵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161334.074231:+0000',
                                                    },
                                    },
                            {
                                        'name': 'õҤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161334.141148:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʃŇŜƎҭiΉȼҡĥϸӅć\x8dИˉҦǢâÎѳšԡʒΰȑțЮɌʨ',
                    'message': 'ƜвȨƤτǈӓĘȵЍКӥМ\x8bҥ˒ЛȫɫɣƴȲƮŎƉˋƳҹŷȥ',
                    'arguments': [
                            {
                                        'name': 'ƴźǌҏЊɹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 616720.7740738614,
                                                    },
                                    },
                            {
                                        'name': 'ŮʸԙӧȹѣїëŭӠÇķӜфťŽß',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƒΌэ\x87ҫ˅ǰɇХͿŪ˳зŷɂ˚nņќ˻ʀ¢¹δƋțɯˎãӘ',
                                                                            'ћɟΒ£¥ŚōЂò\u0380\x7fğƦqĪĉϖԢÃӤѤӵàȨ˰ɣԩÑӘН',
                                                                            'üŌŕϡйҖàѓСɶĸсϵ«U\u038bϚZȖƏϳ¯ҺǤԩƛ¾ȖѸ»',
                                                                            'ñģӢуκόͶ3¦ʆӺуԎ\x9f%Ěj\x91ҌͼħĉƑѾȩҞԐeӌƊ',
                                                                            'ʯǿÝšγǫnǁοZǕřŷǬȠʂΞɜŸέпȖ˙ƽÅЕǚǀʃԍ',
                                                                            'XǜȪûĬҶɠZ:ͳϱĀİӗŴθʔƄ϶ƙӵ\x9a]ȃέåԆȿЌ@',
                                                                            'И΄ĻVҜΔQˮѸԆǐ˩Ɯˣaїʛ\xa0eËӥɇԎѨ˽ÈȝȄ.Ҹ',
                                                                            "ӔɜӦг;ŃăˑǕӿϱ'ԐǍǰȋŞɛΒӧ˹ǶªʥɪχNѧmƣ",
                                                                            'ƁƍǂρѭȌҩŀ`ηNӢѶΟǊϺĵͱpέƵѧеЗ\x97ԃ«Рǘ5',
                                                                            'αïʤĔҩѣΊɹĹ\x93Ѧ\u03a2ЯʝĞҼȥ˞TEΡТʱԢ˩ΚҝӯÐ¿',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʥϠĿʼϑ˺\xadѲʍū\x8eƱЅҟ:Ǥˍǁ˨ſ®ĪǤӞūʀѨȒʇé',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -41807.68310900313,
                                                    },
                                    },
                            {
                                        'name': 'āĵƞɤĄǠʃ7ϸȗǚȏԝăƠȨҋ\x9aЎäýƏÒӹΞ͵Ѻ\u03a2ǁȶ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3000304646347161978,
                                                                            -5396859438267290550,
                                                                            3887852729082261212,
                                                                            -8344387722019951708,
                                                                            4558722386283307479,
                                                                            -3331011742918883853,
                                                                            7371470484814275098,
                                                                            6752642575437484082,
                                                                            -1387445608951862178,
                                                                            -1263815119218795398,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǲóȝǲÌȡŜӖѤ-\x8dҮĚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'éʇѣŉѨҎȬıʝŲӶȦϨ¬ŢǆĆϡԆĘϞ,ÝӁĪ˰ǔɅǯĜ',
                                                    },
                                    },
                            {
                                        'name': 'ϱŪϒɷƌ-Ǟƿ˄>ѬˢŚ˻ƢÇ_ӆȷӊʮƦҰˢҒЬȕԙìҗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8820950242576021414,
                                                                            -651544153531337273,
                                                                            6975418461696056341,
                                                                            -5487269065867340680,
                                                                            6487242465842607004,
                                                                            -3360183287747873331,
                                                                            -3775034902370123151,
                                                                            7545242832928140698,
                                                                            576191497054416302,
                                                                            5294787850755435162,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'РȈ·ɕȟÒ-ϧaǌ¼ʠЊưƋшȱįԬСϔkŮɏѩÉγɶƻȚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'T˛˽ǈЌψŁ¬ԖtӒҳάӛЋѺŤŜˈҰЋξÛԝLҋԎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4252184027948852500,
                                                    },
                                    },
                            {
                                        'name': 'ҀѤӎÄˢαѬӟȤџĴēΗ˛оиkȦʡƢʾʥӦ4Čʚ¶Ż}ϛ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʌŴΥɠɮ¿ɹ\x9cSˮÀɩ§ӫΦ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3583137558680968554,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƄηŕƚΖˣȶŋͻѼɢӚÜ҆ǺŒѶǪͺţТүKҨϩѿϽșҢſ',
                    'message': 'ķHâѝĠˇөʨϞӼίʏĴĜȞȍ\x9enɥ`Б@ԏήԐӨǖªʬρ',
                    'arguments': [
                            {
                                        'name': '˝ɱ\x93Ϗʹɛπ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4582371975841386705,
                                                    },
                                    },
                            {
                                        'name': 'ԑӉȽҭĸʟ+ǂҩ˟ΐŅƌ˚1ͺ˾ǆ#ЇQϏάÔҎǴýǉˋˢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161335.972228:+0000',
                                                                            '20210910:161335.989580:+0000',
                                                                            '20210910:161336.006808:+0000',
                                                                            '20210910:161336.025793:+0000',
                                                                            '20210910:161336.045532:+0000',
                                                                            '20210910:161336.062968:+0000',
                                                                            '20210910:161336.080095:+0000',
                                                                            '20210910:161336.098274:+0000',
                                                                            '20210910:161336.115331:+0000',
                                                                            '20210910:161336.133355:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȕŧɹӲŃӵʙʗԭϞŚʔğŔ5',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'uǠµƗЛҊÜъ\u038dʴńȡưϷ4ЊʳѨѴњėǬŻѥƅԝʌ˗˽Ƣ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161336.584243:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԊφɊиӲσʭȽŀɽ˒ŤѐĄɎΡāĤȩRÍʎ·ԉҎƷӘȜ\xadς',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϵРӌƣŉЗїȉ˾ɚɝԀÐΣѿӡӉ҅¯n\x87\x83ǄȺÅ!ÐƦαж',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƛΚǄ\xadфцʠƲǑϑɏɔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԨЧćЙȀnˋƞЏϬºҩԠǷΖγЧ<ǢǱӖѰǘӐҢʒƆҘΘĸ',
                                                                            'ξɐŖʛɝЪȂͲÝπɶtΖˬӳı˫ҮӏЪťŔĲŽĭ҅Ԅʱ\x88\\',
                                                                            'ӪśӻҔȜƲŽεłщ7Ơ§ѓʖоĀ˅xɹӌH5\u03a2ϖќˢΫɗɤ',
                                                                            'ǮʣϣǨҺýӬˆɌЍʞ˥ҥәɹҮģѪΞԝġҺǙƔԗ˼\x99ƻǼѪ',
                                                                            'y¶¬ÉϖϝĖєřўǶɖ\\ȜŷȀмZӒ¦ȳ¢ȿöфǊ\x8eLʅγ',
                                                                            'ðČÊӡ\u038dϗɄ\u0379ɧȤҋʋ\u0383϶\x99ԎƀĶ϶ŝЬ½бɜĈʮįɉʳÏ',
                                                                            'ǁϜѴǁҩȿšƞŋǷѶӅîΩ¢˜ԜШʟǳƺɽQɫʔũ˨ɖ˳ń',
                                                                            'ȌѼδȀʈԈǙǉҭ`ǻ\x9bϡήʈɰһʡΜΠ҆ÉóςҼĪϽʪӵƽ',
                                                                            'ƈζǹα8\x82WΧѾĿϐ\x86ŗïϙŬȣԠȳä"҃ȰΘĮђRҝɛŏ',
                                                                            'ϊνц@ɅӮʰʭɶǽSӬҊМʁΓȃɰǿΪƀӀůӱǹAˮôԌµ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ċԮɛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Μà˗Ȑǅӿ«ʵђÞƽȤӒӗħ˒Ŧʎӽɀ\x7fǴĐŷȫśьɵћȜ',
                                                    },
                                    },
                            {
                                        'name': 'ƵпΔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'OƑŨϸ@\x95ѢδFßƣâԦɜ˖ΕɡϝъÚ˪мB҇˕ȒˌшΘ˞',
                                                                            'ХƜ\x99фÎēҙÝ\x94ιɛȄ҄ĘϗΚĳǇӏŬѨԎӕҳѣ҅s5Źд',
                                                                            'Ѳȧϸǀ\x84ϛ}@ɡ˟˧ҠʴʬЌҕ˓ϰе ʜ$ġȏΥƾȯ˝©ӏ',
                                                                            'ƯԦӵɀ4ƂǻΗɫôɯҖƵ\x99iXñǰњ;ɝΚĤҹɈ҉ĸӞȔӠ',
                                                                            'xǛɿ¿ħϝΡԭʏȍ\x86ʈȣԪя\xadƻѵ˦XґéοŵϰΠϧˀğά',
                                                                            'ӫʴ\x94ĨœЫΩπƲҶúшțұҾϙłȧμВҢi,ɮůǜÄѰМҭ',
                                                                            "ȄŦƶԐƽѢqΕӵ;ʎʜҫ·ԀơHDǰҖ\x98Ӄɛ'ʩЪӟȑƇs",
                                                                            'ȇƼ˙ǩԍ˸Ɓ˟ʑɩʘʴшʮðɊŌϬΨjϫ˒ū¹ӝkʣΙґ˄',
                                                                            'һǹ&ӎğèϵɨҮ`ɁßЖǭӽ=®аˬìҾǻîѰӀPʛɊKɠ',
                                                                            'ɄѪиȏɃϋé4Ì\x96ɊɚϼõϺωԖјԒ˥ΞƝ¸ˏ\u0382ͱӫΚҭβ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɋćО\u03a2vϏӱѧΙˁоТǊěÍϣəԘAˢЮƵһρԚˊǙʟ\u0380ɋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '5Pь\x9dшқɎҬŔǴ*ςґFȱτ\u0379ʥ\x8eǬѺ˝_жðΞϳʿĔ\x95',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЁʾЌυʜáȠ±\u03a2<ɖΛόԨøδӍ\x87Ō\x99ѣҡȿёŷ¾Ťtөʅ',
                    'message': 'Ѐ\x9aӚѻѤ҆ҡƀŁƟ˪űǭΓΨǩƝĚȟΎϔ2ϢʩPәǥķǼӰ',
                    'arguments': [
                            {
                                        'name': '´ŵ×tѷӔ®˝ȧҲď˒µӖҷ\x89ěӛђκǺ\x9c\x81īƗȆԨɳ¾ǁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ųΔ:',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                                        'name': 'әΛɆϘ-ЄӲӒȟϩʒˤȮʓʵ',
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
                                        'name': '$ȼɒJŗ\x89ıʭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            910449.3158059949,
                                                                            383869.5552821094,
                                                                            863499.0600091646,
                                                                            862141.1440449049,
                                                                            728410.9554870705,
                                                                            30726.284489951227,
                                                                            100754.744138334,
                                                                            290994.4253117032,
                                                                            930141.8063330478,
                                                                            150800.95533436636,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'îǀŇƀŧ¯ԫˑǗʵ˰ɩΨ©ӏ҆ЃʎǋćϓЛ¸ɹ»ӹ\x94Ȭǈʰ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ϙ\x9cυōʌ)ƊЯȞ{ǶǉԊθ\x8bƇɱƌȐӞɕͿļȦn¼ƐӀÅɉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 155607.89419777755,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ţɉʝ\x9dhĺ¹Q\u038dӡÖƸśvΥ0νάɤ°ί}ď˭À҇Ε҅ӈĸ',
                    'message': 'ҽǴǯȼȮÙŀȒΎЁŴϨͲ\x86Ģ\x90ыʘɁ\x8dâӀ\x9b҅ƭŪɋкĮɬ',
                    'arguments': [
                            {
                                        'name': 'ɘΌʍŦҭ˼Ҫ¹!Ҙ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 358934.2167595258,
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

            'identifier': 'ѻá Łљ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ýΎ',
                    'message': 'ǝ',
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
            'name': 'óɘЉѝǶí\x9aǞсόĒˀ\x91ԭ˔Ȍԋēŗ\x9eɺɷįӖͰŚѷÖ\x8bʩ',
            'error': {
                'identifier': 'ŎӏҏхœκÕҲʿǍ¦ÙZȢΌģȌѦȖĝҮǷM\u038dčōҿąӫÁ',
                'categories': [
                    'file',
                    'os',
                    'file',
                    'network',
                    'configuration',
                    'configuration',
                    'internal',
                    'configuration',
                    'os',
                    'configuration',
                ],
                'source': 'Ů?ҜĹѽЂѯ\\ȒłƪԥѰǭ˞ѓ¶Ȼ¼ʞơѡήιDƄ|˧Ą˲',
                'messages': [
                    {
                            'catalog': 'q˳ѝϻӍрϝҺѮʱ\x98ԁ˲ʝƯҸÐȋԊəЧгӉΡθ\u0378\x97ΎȧԤ',
                            'message': 'ҬˠůӇΗWκѯ˩·ɪŝĢ*Ń˧Ξ´ԑƫøƂÔˉԦˣ¦яɕШ',
                            'arguments': [
                                        {
                                                        'name': 'Ƶ˹Ūσˎ}шƍǜϽўěĺ®ƙʱřÔҪ˜ԝ˓ȕԄ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8578078298553303539,
                                                                        },
                                                    },
                                        {
                                                        'name': '>Ź\x8b\xa0ϜÅďͶԈϸ¿ѨǊYȥ˸ʁϝҩ˥ß\u0378MϕϵŖ:[ȣЩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˻ÄƑŁνǍƊɁӋĤÌYưѰϧɹƥœ\x9eʧǜĽ\x90ҮɺңћǺͳÜ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȹƇˏԠ˙tvәĶϤҔԬЕŗξƬǽЉӑǔ·Āɏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉTФqΨӢżʁуϲʚΖӚĭȔſε',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161316.225738:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'җѤȣϺΜµʮˊƀÏɸĒɊӤѺþϏĭ˝\x85ԦφŨΎȁзʥӕ¨Õ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԈÝR\x96Ƽʶħ0ˉ.Ûҝёγ!ӨтћΪΡ¬ЃáҰʀÛұǘǑЍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǷΰҫψѤϮčhөκȬϲɲȓƻэˉċǅѫΌƌȔŵȳĥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'å¼һxуϥԞӦÁȺ\x90˟ĝӎʤԥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'нъǙӡǕІǢιˣ1ϔțҟAċͳпĮǷ¥xѳʣӃ\x86òƗƪǻ\x92',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΕʈŴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƭĞџƧβȕɍφʭұϳӄέSӮǪʼιȌɽԓoˢѫʁž',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯͼыԏӝҫȘº7ԁș˓ь_ĠÞÄ©âѾĦӏī˺Ąʽ¾µҍʰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ТӗΗƞTҥҌÛȴŬӚˎ˼\u0383ϮѦƟŖʺԏÓęȷȧчԒó\x86Ϣʈ',
                            'message': 'ȱЪæ£Łπ°ŲºǷʣ#Ƌƶ\x94¡Ǽ4\\\x9eΦʽnVĐȁĆŻϣ¶',
                            'arguments': [
                                        {
                                                        'name': 'ԋˊˀԠӥͷͼțϾłԎњ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 122466747221351178,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΣˡġʽϹΡʐѲ\u0380Ӆǃλ˔ëǃâο',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '_\x8cƬЦȽϺƖюϚòϲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʶƺԗǱŻԕӎɐҒхϰԧƅńƶǤǠǅ\u0383џϬӢªН˫ҒǴȚ\x96ɷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÃÊΣgӱfΏ©õǽʄʅ÷ͼҸʮύη\x86ƏƖϢϼń9˒ƫ´ѿÝ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɇȇǥ8yѳΌєĎȱQǏҕĈʒQԭ÷ʹϪʛə1ѨϱĴѤßʧ˝',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˹ϖϩѪϛςǦЉİΘɤƙKʈ˳ПɁ˞ŒџǠλΤǓҰΨêνȭϵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸηϗʯ[Ť¯ȋʴϽȘɱʆ˔Ɖӂю҉ɍÙ¢ȞɣʄʖԪ2РΞ˛',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ċüɲ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǆ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '"üɚ\x9eŊмӎԄͲ\x8eԐΌʋ6гÔɭѺ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 521301.3436685222,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ХɗΖԄ\u0382ƅӇeȊΠ\x7fÇÿӛˉŌăPȐŁʮĦ·ω\u0379îz\\χӄ',
                            'message': 'ϙà"ÝÅˀȕŒѲˡȗɚϯ¥ȲoĈǤϙϋЈΰҹƪѽŎlƪӫˉ',
                            'arguments': [
                                        {
                                                        'name': 'ʂƱз҈҉ϘĆӗԣҚòƐύƲʩǋsê',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Οї¨Ϯäľ+¡ɫʍĐƳԚ)\x83˖˛@ŁƟӆԮҖ}ǵǎҴĸΤҁ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161318.119238:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϗsġůӯћŗ\x9bȗɌԏсѱВƞů\x87ӂɘΡúü\u0379\x84ԩŪӱҌÄɖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "ƯρʘфÝү˨Ơбñ˩ÚȳĳƾÇӖǹ%ʔҒƅɏɄÈӟŀëƇ'",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ñļĐɃϩè]Ɩˋ\u038d',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѢƓΐмΥʝӖːƻīϖʧĳTÔ\x82ϗƧкȻȣѸέ\u038bҗēo˝Ыџ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161318.509419:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѰЬΏ϶ӬgϛəaʯҐgҌ«Ēǳ˹кʓěΕĳԟƝK\u0383ӳӤҶč',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʃԂ˹ê˪ǻƕїʐǜʨĠª×Ãƙļ˳ɶªkŁΜÓ˦4ȯϵɕŋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˈǢɁƓЯȰ¯ӔҋѪӬ\x95Дқϻ\u0380Ⱥ§\x8eѼƤΐä¹',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԤƘ+ȣǁϕ˾ǐŃƃŖӯƔûŷԃϬ\x8cΧћÛˣÛƸөўћɛȄӼ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Άǅɭ>ӝĄʒѲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǽѵ˜ɏӦĊѵӳ˪ʴƞçͼ\u0379ŞԙƸϺi˲ǇDԟҐОIɦƝƔƻ',
                            'message': 'ĘƉҸҐĢѿҧӔʗżΗϡнÚњíŖȾϴFΩ$NϴȾʼӞԁ\x9bѩ',
                            'arguments': [
                                        {
                                                        'name': '˪˳ȿοʤ\x7fЋѵǺ\u038bàƝқȍԣǱȾǹOŠӒѷԝӏɳЈǮHϴď',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '#ȪώЅȝЖɇƢ¸ϞU˃ϑĨɰϊýѪ\x8dњĦҲųōŐдǜɖ҃к',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'βãÛϐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'εƱӷɩѱͿӓδɵʩʝSΜŭƙ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3531544492207040380,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӎ˓Ԉd$ÕēSЏŃΏǐ˝ͳϒɦ΅ɒȝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӵʆҗ\x89EƬnԡƳ¥ŭʏ\x95ˤǮϨϮƲ1фˉϗƸвќȈҞŦЄƘ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӝ\x84ȪѫԆÈȏ\x99юƫˤʕʘԧn҉ʗ˟',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '|ƍȚFM',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ēҹɺή',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǩ¸ȇ.ěɯɴɹɆĨĹ<ʂƺђŋơŕ@Ӣ\x8aппжϹʄȍ˞ˀΣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҜЕĉΙčQӧΆүҾʫЋёPʋʛ¿ϯԊ!ɭǍάҟŎǽƢӫĿW',
                            'message': 'ĔɃŅңʹóɮµąƖý¤˜ɻҋöʔҶɰuȱǃτŇàԗѮԝΞɯ',
                            'arguments': [
                                        {
                                                        'name': 'ƷϑӁіȾϦή˸ɿƇǂʗԠп',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȍҒѐԇʿǞʁԫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '´џɡЬˁƊǤДӮєԎŲÔÊŇàüæþҁƇͽ\u0378ċÔMƉάǚ҆',
                                                                        },
                                                    },
                                        {
                                                        'name': '4Åϲö˽˖ȆˤëΏҍϟdҕǃǩлǞΑĜŴeȻĈѐÂɐʍɹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÇmΌΗϠˢ·ŗƊȗïǫçzǚ\x88˧ѢӃǎ҃ɶlŃԆϭ\u038dўōё',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'È ͼA\x9bß\x9fȪͻì·PЮЃƶ˚ϽӞˌ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161320.350530:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Zì',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161320.438526:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "ηƛӯȜʤӌ҄ϡɥȃФŝ ЕϬ¹Ň'ϻσĈԇʻƞ¹ұˬӱӂ\x9e",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѾӚ3Ϥʮ.ŅéʰϭІʋĢνǒ\x7fώƇ~ǋNΑɡѿҪĪɬːĒԈ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩşɢƇɼΰһҢˤΑӒɹƻǽĐӿ8ÈԪɳӢҽǍȭЧƻФĨɳȟ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3841725694736034183,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉĤĺĎϘ\u038d\u038bŷĔΊϳŬȳǞŦиżŦ¸φǓċ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x81қǥȻϫǙÔƤӪѼҫΙў£ҦǨÇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8201484679312420554,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʋƺǦҹÐƽėǾХҦԥƯ\x8dĥρòêԉҢˋǐǬȾҋȜѫҟυԃǸ',
                            'message': '7сĹʆŃƅӫ6°ěėΉõӞЍ˷ƆƂȸѤƃϭІɻϺƕɢӐȚƇ',
                            'arguments': [
                                        {
                                                        'name': 'ŸɱΑȀҖƨƜƹӨƞɌȇϿǖΒˏëĴ\u038bεфqŰŲ~ωɣʺΘş',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԗ˓Ú',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϧҽυԥÞλύґɡЍҎʹԣ½Ԇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠŲӆ4ɽϯЯŵԉЦ͵Ƨ¥ӔӢόƳξ͵ѱƧǱȃȐȱ΅Ӄ\u0380\u03a2ˢ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6058964980751235065,
                                                                        },
                                                    },
                                        {
                                                        'name': 'șʟҦЏԇ\x89\x80\xadǔǀĹƀ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161321.188488:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ô`βƇŽʞĎԦŚȌЯzѱò˴ðhƦÞԌѪ¥ǀСǶŉrɀ2ԉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161321.275364:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'сͽԙԪȘǀʄ˫\xadʺȐΠǋȁŊΞȫԁŃǅѼíȀàӻ\xadġˠβ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -54591.82345127675,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӶԐıīɇΥǒHҘƤƜ0ԧ¶Ɓɑʈȹ˘ͶЇʌ\x9eϖ˚ȇп',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϭ˞ϡƆʮżƇǈδӛMΌҞѩ\x80͵¦\x94Ą:ʊ\u0378ĄϮΰűҧƠӐў',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '©Ɣ\x84ŇҟȍЯȤ²ʠ!ʲӧҼèð¤ӜŇęĺųɸTЙ[öÉʹɼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЫΝ$~џҳΒůϦȿцӟiÑYɅˍȭ\x9dǐεÌƐ\x9aĭûӬǩÍȄ',
                            'message': 'ȚϻӎΤȆʭīӹʳʄ0įśҥŕVӥǾòʪҨХςϗͰşшΗ1Ŀ',
                            'arguments': [
                                        {
                                                        'name': '\x98\x87ҕγyŮ|Н˻ȍ-ϐ\x93ӳŗԖȦңδѼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161321.768633:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҙ˚ǰȱж˺ŃȃƎӐԗºӶǠ\u038dĿǏ\x87ҿĩˇ\x8cǉǨԮѥºΟ˄Ѷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑĬľɤ·іӚ҉Ėƈx\x9dʏǅзʉѪɘѺ³ч',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʖҟ˯CˑЀȠŕÄąǈӭɫǯҶoțҗɀ҅ƏԬ\x9cƮʁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯƳ\x9fżŉɚũF¤łÉŠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '+FVυсƓӉѡȕĴǩ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǡŤϟÒӰϗƴƁƻǌŕ#˭СΨŲԊ\x91ŖɚΚǳŃơҔ\x94Ϡ_`Ͷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Sԭґɑ»ǌľGԨɯºϹɲҦΏ\x96ϧσóɼŸő&ŘÑŀϰϪĽӂ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɛȯǕǹͺ˔ѡD,Ǖɘ\x9fӲżӺк(ük\x83ӏԔ\x94ɶȮϣêԒ\x9eһ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԙҮԮƄ×ƞlB\x85îШʃS¿ǌϾŗΌƉΘöӌĻŽĬƍčƬɓŎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161322.378903:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҮÄƢʳʬ[јƚ҄σˣŵͱɬŲƲɸԂŮöкȳɭ}ËЅԁЗ\x87ň',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u038dИҎʋŪͷΡѦϐʞұϕ¿ŞȰìҮ:¹ӊЮĆ\u038dԁrǧЪбΙʕ',
                            'message': 'ԟſ\x8e5ƏԑzƚȭɃªѽЙоΉΔQ\x97ȬƏͺɂ˴Ȯƙ\x90ÕѿԋŔ',
                            'arguments': [
                                        {
                                                        'name': 'ӏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'é×йĳǟĘȀњɔʠ˕½їɿψĹǌқ0Ģƨ\u0383Ō;ԚҝRʙ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1300568738519383696,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʓΛ҅ŠӦÖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ųÓΧǿǘҝӳòɧѷɭȺϕŽҴԬϧ\x9büӑԢźÖƈю6ȳΙù|',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊPȪƾȝɢƯ˟ϾǺ¨Б',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'īҖɣ\xadҹįʑαÆ˼ɮĵҽЭʞɊȵ?İ$Ȩʖэ\x81\x89Юs˒ʱ8',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 504407.40311503,
                                                                        },
                                                    },
                                        {
                                                        'name': '˯ǌМɻ(\x9eɽϚƊˋҴǊϒÃɃѶϭɅˀι;ҳˣʭƿԡ˭ŒҰ\x89',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȇҥίŪҬʆƧͻ\u0378ҩх9ЈĂƞĺʢȖOǃӿӕɧΜ˞ԂԛɣȗϏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ғ¹ѾӤÑʚӲΙ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2853923854963525826,
                                                                        },
                                                    },
                                        {
                                                        'name': 'zЋϹɪƐ!ҦϦο6ԝƛĔͽXΐȦƫ?ԏ\x97˂ǮƑάҕǓʢӓǲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԢЀ͵ŷ3ĨǮԍУǝѸ»ѦѸǷRĿϺϭȈ1ŶÏѠϭӣϡ©ʮż',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'қϞ²Ϙ˛˛ҎʈҖŗĚʕĚοЎǷŢʮƗϮ˩ÎǇӕʻƦâÆӽɟ',
                            'message': 'ŐоėɜĵˇҚԪĞǩѿΧϰɎˤӮƯÐ˺ǘ³ԙƓ҃ΪƁ¼Јѳȳ',
                            'arguments': [
                                        {
                                                        'name': 'ҸĬΘƔϰԠoο˵',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ľJғ΄ӿˈ˞˨\x87Ԇӹˈą(\x9eґөƈɴǮňrҏШ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѓ#ʣɷŷӐĦДʒ(ñʃҟ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 580222548873537054,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϗg!ǋԍKЀą˾ϓǌǿґДŹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ў˺ĕ¹ӫ˶ǗČҠɢłɋѥ˥ͽʏ˸˷҉μѸю',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҉ѽӢʫȓ˩Ƃłƀ˼˦Ćȳ²XҸ!uʼȗǤƎ˪Ӣєӗ3ɗɗҼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƙ\x7fĜÌkĀȬҖɝҌϚԑє#ΉѿƾǑ\u0379ԉOЗϔɜϹÅļʭӢͶ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˠǣ¤Аëʒ:Ʌε҂ԀľǄʽŭЀӼϢÏǝčș§ͷР˩ԋŹԖï',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161324.086934:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґĢ>ǎöаʳԓϬǻȔȘ6Ԡů\x9cӴӥ³ˇ\x86ßіʱи°\x9aԍ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3971376810815882427,
                                                                        },
                                                    },
                                        {
                                                        'name': '¢ƿ΄ĺҔҦԉŔ',
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

            'name': '\u038dņâ',

            'error': {
                'identifier': 'щϐĚȫ\x9e',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': '·;',
                            'message': 'ԝ',
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
            'name': 'ˆџҪѤј҉\x8a\x9cԭйˣѯʸӧξTÚщƶԓӗhɸσΩҖһŒƆβ',
            'version': [
                -2560764516414737551,
                -8975422232361517315,
                -7868050469190914913,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȇųȴ',

            'version': [
                -1026681134691372881,
                -5690806700173110876,
                -1626456918146559157,
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
            'event_id': 'ˁ¾ǛӣÝӦ҄ӏcҳ3ɑŞӒȜȬ©ǊЏѓĜǾ˵ʥѬ҂҂ӤɈƠ',
            'target_id': 'Ж҆ӀҫÞȪ\x89\u0379ԠϔˣƍѾƷēßUeųśґÈʳϟǒOНƫŦ#',
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
                    'event_id': 'EЎљpɐЀЧυʊÎ§҆ưɻ4ўҁΏЕĲӾȜԬˣM#ļϴżʭ',
                    'target_id': 'ǙȾνʧƇSɒčŰƨϧȸŰ˺°ͱîȑΙȣù˚-ÕΘǨħĖĪў',
                },
                {
                    'event_id': '˾ϕȎζďʝƃƐƧҙŷĜΩ¢ѺǼΚǷÑǕʬȜƤƐǕ½ʣҩ8ό',
                    'target_id': 'ҔɎ8ӖɍΊҧь˴ĤдɷȾȲŮЇ˱.\x88Ǩ`˩оěǰЪɆɛɬӱ',
                },
                {
                    'event_id': 'цΥ˯Ψӯӣɀ˰>ϑƢŕϫӻϿ˪б3țѫʧòӴWȳ҅ƶ\x9dКԅ',
                    'target_id': 'Ő\x89nςЦҎʋ\u0378ӐǬƴ²Ā˹ļȂӵÐψͺɛұǓȭҨǩˈªȌʖ',
                },
                {
                    'event_id': 'sɢ\x80ȦԋҝʇȡƨϖхΜϓҶȭвk¾ͱƔĖ2АӱәƂ\x9aŚɛФ',
                    'target_id': 'ɲůȥѰ\x88$ˠĝʔŮυ\u0378æТɔˊÍ\x81ƆÞу²һȩʇѬҨũϱҵ',
                },
                {
                    'event_id': 'ȋϘϞϴǰ˼¬¯ȊȡЊßіŇʛ?ʫƈ˖©h¸}+ŽɁыðRɿ',
                    'target_id': 'κҪʉʿǦʒˊ÷@ÝʟҜtÖΉϥӌŰχǏʑԐɕвϚʤʄԟцѻ',
                },
                {
                    'event_id': 'Ȩ\x98ԠžҋһťνǖǾуǴGàˎLӣ˫ɕħɷ҆˨Ӈ\x8eоǆǥƬ×',
                    'target_id': 'Ԃ\x83ƲɌZȡŤϦʷɐШЭɅҺʞЅǁƳTіzȈИѮ)˱ŅҹЀʪ',
                },
                {
                    'event_id': 'ύǙӱύΰԗʲСΪΡĠǐƦʛΎФ˓×ɯĮӧġѦâ\\ҸÞҚ1ǳ',
                    'target_id': 'ĉśľʴϿǫҒѓŠ\x97ȱɠŨÍ˂˂ŖǕƝʻӈϡǰзȾãѧ±%У',
                },
                {
                    'event_id': '{ƸɂОäG©ԊʥΪс\x86ƃNȥц\x99ɥШҐѰďƀȨčϹϙΕϰС',
                    'target_id': 'ǐΏźΉȡЖ\x9eǑ!ԗұȾӺËƐǨɈɏцҬĤʷѠĳĻ·ӳӗϵ=',
                },
                {
                    'event_id': 'ɹȩ\x91ԣŵțӑɲғ˽ƟҏϽԋєĘĕϠǶŏɬѠƂΠѤӑ4²ưϱ',
                    'target_id': 'ǵÈĶˣǸˎƦΩŽĆσЏʯϳǪʢ¦ɒΣµȮǷĪҦ¿ʷǃdÁˢ',
                },
                {
                    'event_id': 'ɲӔӯɌȌ\x90ЈȭÛͺ-ZӻҠŁƼÓϴИ˵ͲʜS=śΩñ˲)ę',
                    'target_id': 'ǨƴЌěѐҀΖƳȒԌǘ\xadɦ\x9dϙӮϯʲɥ\x97жôѬҨXʰäǱԔȽ',
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
                    'event_id': 'ɇɢ7©ϗ\x84Ұ˒ϑΛ΄˞ɹԈʃϸχűćȥʗѳ>υΏƬөѠуɖ',
                    'target_id': 'ѮɅ\x83Ĭ"ѬǨɡɟʯɚŨȏĝɑ\x9bό`ŝȀƏGΛРϴƅȒ¹ÆŠ',
                },
                {
                    'event_id': '\x9fԭʞͰ\x90ŖȔГԍʙ˟ŴǆɨĳπОқҦќ¤ēǗҹӦӊӍһgˍ',
                    'target_id': 'ĎPҚҳϳʓʁÜŏϏƤɳԪɭǟȡȦͶтsŬɱԡҽѱԈу˔ĄǪ',
                },
                {
                    'event_id': '[ȸӸcǧѹjāҙκ˦Κȫҝġж6ӄϙ˘ҭЎ\x96ηҽƷяÏǸʔ',
                    'target_id': "ũ+ΡӛǴҶ\x9fώԧ'íȐȅŽ£ʛЈ/ÁϤđԨ\x84чƱɨõҮϭӧ",
                },
                {
                    'event_id': '|\x7fҘ¿˯ѸΥ{Ν˞ĕǕђϕʱɯ\u038dζλĴƠʖxFдĽȰ¸Ҹ\x95',
                    'target_id': 'ͲVђɰ˩ĝғģЖԐ"ȑŶҔΔƺԫˣŋϱΏӛȁĽ>ӬĒ¥ңĳ',
                },
                {
                    'event_id': 'ɅΐԘ˝ȐɌ\x90ƍЍīӂͺӪȊӼĆʑѐӟϘӒψ˚ɑʵЩӃҊƤȾ',
                    'target_id': 'ͳŰκͼҏʹϧÇФюЎ˚ѐĊǸηͱʶέ΅ЗѐȂˑјάϿʿӓĩ',
                },
                {
                    'event_id': 'ԣʴҪеΣrҼǏɚԏӃŠдԧԛąѫÊУϦ˙ҳCʭѣΈǳӀԡӚ',
                    'target_id': '˒ӽɬɊʽÂƇɡǚĻ¬\x85ӥŅэΓʲӃē͵ӈ´ǉӉѫɓʤǣwǸ',
                },
                {
                    'event_id': 'ȬəŚ҃ΛҙԧΰĠÑʱ%μԖȤÈˠӉ\x92ʯϫɍџV¨ϝĻӆŖϝ',
                    'target_id': 'ƕɁɔµǫ,˦ʶӈӉɣѦɍӴΔӨʹҼĴ˝ΥѓʈϺΔɖ\x8cƹΡs',
                },
                {
                    'event_id': 'Ɵԏ\x7fřƪɝǇ\x95¯ũБćгĈșˇǱƇʇΕΫ˔ԩθФФũͱǺϒ',
                    'target_id': 'ăŢɬЛĒ.βĀfͻҤφүˈԌʃȆВѽĥëҌЃ҃\u0383ˁ\x83Ѵžſ',
                },
                {
                    'event_id': '\x89Ƌʠq˛\x91+ǌҼд\u0381ÄĴ҉иɧΐĉ4ӧÄҍêŬ΄ӅǰMЪϜ',
                    'target_id': 'ξË˂ΔɮџĽɯɂԣċӌoƞʹ<Ӷ]Ȓ:хȣԪԃӧ,+ӋɩШ',
                },
                {
                    'event_id': 'Ё˓lvŢ.Τ˙Àѵ´ҟβȇӐӑFҴΜǖȰɨ¨ѧýɇǶО˥ϥ',
                    'target_id': 'Èɡω=ʈөϞǭ03Ŏͺg¶ȸʱİ>ǂǢνΣΓĕмӸϫĩӟA',
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
            'name': 'ņȯĂΝ_р9o˕ΙѬǎ)шČeʬţӼǃ˩k¦ĺʨұӍϱ8ӷ',
            'version': [
                -4335450325806490440,
                -2872195042427853215,
                -786359416692947439,
            ],
            'about': '¯ϾļČœȚҏȳ»ǐʦsĲҽĲʕřĎ;ӋӎԈŴоѲϛϛŀЕҐ',
            'description': 'ѰѯćƁț˃āÛ±˃ѢŬƬƽĴʬ¬ʨӆʃÙˊRŖђȬԝԞВɫ',
            'authors': [
                '|ƫϔģϩ}ȃ%ЃŶǰ\x8fÇȣϦŝ҈ĈȃʾªƜǃԪƬˆǩǶƐԂ',
                'ɺɪʁûɭāǁĿϱxδӐĐʨεɖȉ',
                'ΰ²ťʭьͰǋТͶӝӫʖ¼ɓԖϜȉǎʼͼťΦ5ҵĽįǶǇ\x9bî',
                '_ϽґʫŭЫˡԖëԛďθϳѼ˃Ʈғ\x97ÝȋъӠѸĕ&Ň',
                'ɱқѨԏ¹ͻӲл·πҁґʦ\x9b',
                'ΛӱѼǍΒâǕâйȄԬεķªsźυΟǺȯŅЀӴӼƖɻЗǦĴЪ',
                'АˉιтðέİΈȴǊѸwӵ\x94ɵёľ¨ԋǲϗÃdƏԟɷŖʭł\x99',
                'ȭĩɩǋѿԪɃɍŎhĴʤΙǡ&×ǼΓЛϙϜҌŚзӀ\u0378əΑǐĀ',
                '.ŤƁɸԣơʭϖÌԏӉ˪ʏʮҮ\x83ˬ΄ιїϝÆ¶\u0380ҹԐX҇÷Σ',
                '\x958ԙлőЬϩ]ȄǁΨӜĝ\x8eДƆëñȘ͵ΉЂŧƢʰęɆɉɴθ',
            ],
            'licenses': [
                'ȶÁ(ÁǆßWˑӵΡ\x95ͷſɤҘ˭ʸΧϏǯɓäQɂӌň҃Æ\x8fβ',
                'ɖ¯ƌÿӀʱϢɢўĿɻʇ¸Ԅȁϋʁ҂s\x93ðƼȎыȣTȜʸɀɞ',
                'ԤΗЫλЁȐόgӓʦˆˠԚƬɉċƞ\x9a& ϣƧЎѲ\u03a2Ǟή?čӏ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƘˋД',

            'version': [
                -3904729673574368596,
                -6239624088627525001,
                -90358176769451537,
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
                    'name': 'ϡǴ\x96Ƿˋ',
                    'version': [
                            -1497384748028231056,
                            -7557936780956268461,
                            -6777435145130091612,
                        ],
                    'about': 'ɭ;ϗ½Щ5mȘǀӼ\x84сӨȩɷчnȧ·Ίђ˥ЃέrĶ˓ϏΛE',
                    'description': 'ŧƏpɷưВӝнԡȭģ\x7fфӑʺʽĲǑУϕΦǁИŪȲ˟ķ ĵ|',
                    'authors': [
                            'ҤŹµ˭ǐ"ЮƑιíϞ$éÃŌˈȽȯƼ˛\u038dǭœϗһǢҥпШȥ',
                            'a¦»һí*ɯ¾ѹDѕϘӾϐєЋ¸ɥӬðЋҵλȣɎǉɠŌ˓Z',
                            'ƱɃȮ\x89ƓΊėѧäРŀʙ·:ˠ·Χσˈåʅƚǰƕ4ƹԁBŮƚ',
                            'Ѓĳҽѿυ Ӑɵȇ\x92ԢԀϰҰuΧ˧{|Įèȕѧ§χ4ƣπу\x7f',
                            '¥ŕǏ¹þӴϡÜΟѶӲèėİ¿ӥϫҺˤŇɹɗŜɦύŁϦʓEе',
                            'HÖԜćΞǐeϷшĖԟǉĊ\xadƻÕҦҒɄÙΞԠŪȥћІѹҡɬǌ',
                            '҃Ιɶ\x8cµӼʯʓ`ԎўƔЉƜљΆЃϡƁʥ\x80Ţ˲ƒǔΕŜŊƒ×',
                            'møӫ˂ȱʏ˴ŐëЧɻ˸oПƚǄfhǩƕƒɲōʞȻZ.ʂǾ&',
                            'ķԍêͱ\u038dŚԎƼŕʚѨɄμQŵɪ7ӟɊƊÔĚƗ',
                            'φJʮȆÈǆΔ>ÐȳÿҘ˾ǾZǶȥϝʓϕРȃαѕƞvҝ\x8d˱Õ',
                        ],
                    'licenses': [
                            'îҎӘƠĵƕʋʃЯŒ\x90ӲΏΟрƄԢӻ϶ԀǌħԬʜ!nΙөӧŀ',
                            'ǜĉώʹŇütŀ%{ŧГξ8ȣΊіɻɻĖǨԋșѯьȣЂɛƺϕ',
                            '¤ȄǔкӐÞǭÉĒ3ѫʮʡŌ+ɪƏпˍчɗѧAѨɷ¢πǫЭе',
                            'ʽόӫ)[ў\x80ĤȓɪӞĔʂªņƤ3ђͶl˲ӆƹǒ˱_ӔϐȦӥ',
                            'ɧ\x92Θ;˅Ϋ˸\u0383ȸОӠˏyǊˇʶѰƸü(',
                            'ťˁ˸˃ĳǌàτʼ&\x9aīƩÐϞԨʩϑǑǈѾƇӄ\x8dųήТЪԦΰ',
                            'Ę\'жр˶ʦ˼BɵίʢҁϗӒTǃ\u038d%ʨBɯŀŵϕϞͻ"Ϗ\x91ϒ',
                            'ϦɛϘȕǹΟ¼΄XϡƎ\x96ʶэːəҊNǉʂұQъƢХ\x83˵Ҿε}',
                            'σҥJɈʝɰˇԎ˝UįɎĂlфʈгӬҜҩ¦ƄҌȉΛєϴǣσȪ',
                            'Ɉвķ}ʤΦ³Ȏԑ\u038dʶ=Ǟ\x9aЋ³ʞ\u0381ƧɷəѪɈȴǅ¨ȠԦӠɭ',
                        ],
                },
                {
                    'name': 'ōːʚĢ±¯đȘʙŮƟĳˀƄʩО҉ВʽŠɳԐҢОµј϶ãѤɃ',
                    'version': [
                            -7591272794744352892,
                            -4935418205841482629,
                            -5661861638247895047,
                        ],
                    'about': "\u0378ӁԐ:Ƨ\x89Ï-΅ƊϡȤĪǕƈÆВƷԖ'ƳŧȬќΖɆ˾~ɐŘ",
                    'description': 'Ѕ0ъВśϭͳԌɌ\x9dȇƪғЬȝƂŋλːĚ҇ȚĨŐɎWɊ1ӖЊ',
                    'authors': [
                            'ΑђS=ƵЋƏώαêńÃȤǺйâʗлǹ2NͿŔʰiΫѤΓȕԝ',
                            'ÅŗDԛζёΨӹč˙lΌΕÂ҆ĽĔ˒³¥˷ĹɋŋƟЊſɅŴѬ',
                            "ǴøҳŃƟάoљΡσҺƆ˧ɼʊpԓϤȤ}Ȳ\u038b'Ԍ¨ɜƅŲbƀ",
                            'ғӪфԁg\\6ƒˇғƷPΰɀϮқȸʍǿ\x9fșʺҬbɅśƇ',
                            'ʿðԬǩҒъƿl£ԐƑœħüʂïοLщɝϱσÅñƞpгyѪщ',
                            'ЃŻ4˥҆ӐȧʳƄțĐΗˋΩЏļҚϴĝʚÖ-£ӏǅßÚĜɂ˾',
                            'ĬэǪǠӂĜϧǄǴΰΧĿřɜȋåҗќҮȍЛðʸǼ¶ƴЅgǘÄ',
                            'ř¡ЄȝеˇΧĖƮ[κњêÚǃɚɗǋʸЋƊˌΞ˯ΐŦƓӨÛ҂',
                            'ϭͼαĶȈĕƧ΅ªʠŇʩƋDҥԈδWƅǺÍϴϿˍ;ҳΑϻƽϤ',
                            '\x8bʂϦβЯŨѰȦϊĽŤоMԛȶ\x90È-îıсOΔҶӰΝ)ȥӴ˲',
                        ],
                    'licenses': [
                            'Ёҽϟ|ýЍΉ˙ȥѮѰϞʧó¢òԍƍѶҕšǐԇϣ\x8fҝÛѱŖ ',
                            'ΚJȋŨХÒΚśϛªǹ˗ǽɚ5r˾ШӶЌ˳ǩŃěǆĄƴΊƷI',
                            'ʕȦӯĤӒŅƪ˼',
                            'Ҹ5\x9aŷʗÓ²ʒΝĞːD¾ϨʂеpÌџ˙ĐķʽʾϫӞǤѷϰԞ',
                            'ǠȢ˘mĈ/§рΏӰӯƗҸΒŰԣƸ}ͺϮ<ƶDϽǑƼ\u03a2ѫҞͿ',
                            'ϯoǟб˜ʮέǀФʷѺʮ*wƶuɗԪˁђσ˲Ǜ˵ԨŉɱҷɃɫ',
                            'ͲʩωƃӘ£ƌƝʻҥϺɦĔĸƽ҈ȠЖӽƿϿ·ŸҽсļɩËʥ»',
                        ],
                },
                {
                    'name': 'ŔӒ%:ԗ¡ВϖƺŒψȍˡөǳ\x7fѡ\x8bǪф҃зԕΈǋ:ʻŎең',
                    'version': [
                            -352358129516130783,
                            -1990693246774110878,
                            -4278117642163858851,
                        ],
                    'about': 'ʵӟɞӢӟθǡΏҺҚеȩĤȭ\x89ŐхѐĕͳŎɁ\x85ȿƘĂϊѯԞǰ',
                    'description': 'ҩɷԎӠА\x9aӬǴΓʙҾӬʙТΫʊʬ\x83ҘɰРΥБͳýɒҗțǛȨ',
                    'authors': [
                            'ʣƵ*yFơ˟ěʟ Χ\x93ѨϹdҟ˒˞ĂƸӝԋЄ˕3ԙҞŏćȍ',
                            'ʋĵƳ¢È7ƚʻǛͿȗҵԨƸɯЏǡġGſϢtRɻφìʃϚ\x99;',
                            'ƝφFӰUǻŝŢĜͿ/ÊӴҵѯ˷њĵȻ¹˙ʢԡϏѻΣĔΩŞ©',
                            'ϯťǢǘǄԞßѐѰɣϚГ[ʿHMAΖӖ»ˁƅϯҌҟď&˻ǯԀ',
                            'ʻ\x86ʝïˠҾԤʶНϭɮ˴ĶԭˆǠ\u0380Ėǟ\x9făǡsĊȠĩƋǶcі',
                            'δοɏȝƆϘӘІ/ǟКӋǘʛtŪӼϫҙBȷȀɐЮ¼Ά9ʭ\x83˴',
                            'ԌмԐȈɆЦåӍϼLзңŃӎƂĳ*ĵѹΆеΉ¡ģӐˎӰϥԬ˩',
                            '°ӰƱůβΑǖÚĊġȧђ\x84ʮ\x9d\x95Ʋƣ',
                            'ɐĚćīÔØԋАʙΛœҺԘ1ɥϠǺɗϱƔ·ǑʤԇƇˍ϶ɻҎå',
                            'ĹŻϙǗÃņŴƇːʡˈӛƏˡɲЂγHбΕhΰϡǟёİҭǗʆç',
                        ],
                    'licenses': [
                            'Ͻɛ˝ϊɞˋԓ]ί§уɧ©ǡüԜГԟOƥƅsĻºɩ¶Ųγȷɯ',
                            'ƃ]ƨŉɬŶÛӫϧʸϿͻƬ~ͶČÄĪо·мϐɅҸȝɆҠ¸ǎǦ',
                        ],
                },
                {
                    'name': 'ƫ\x84.Œӻʑ\x80LҝҿɺӚҐϲԇȲơРŵ\x82pԧʬѦЪKԓ˯ĲŻ',
                    'version': [
                            -4879556674175334960,
                            -457986955892182630,
                            -323217518181963323,
                        ],
                    'about': 'ǰȢͰƂĚѓͿϑӯƏʠӮӄǎʒɆóɬ˺ӏӝœԄĶ˙ōϱùτ\x80',
                    'description': 'ž°Ǜ\x90țψŵӺɱԥðŪЧНӊ˷Ƨ˭ЍʏǠΌÌjąǋʤ˻Мλ',
                    'authors': [
                            'ɪ\x8aȕǻɡ\xa0ùХΡƧӽEИǜƳϢŵ҄ӺӪˇ?Ʈ\x8fѾњ΄Ҹͽä',
                            'ЦğϿʭư҇˜˵ƀ;ʖʮǵʞǯϸģͶè*Ԃҫέѓ6˭ϧͿ',
                            'ƾǈЪшͳ(ЮϽЮĚȩЀpƝņǉ\x93æǒӼӪϪ+сϾǿɑƆΤē',
                            'ЎbьφвǛңԐÉԧ\\ТǤīſώѯȥĢȿǣ\u038bƘӖ˭Ń˶ϣƕʙ',
                            'ӋʛДʀԎ6DӾНɠΑ˘ƼƓϹҍӋÃ˹˪Ǡǃ\x9a΄ͳŀƿ˛řǺ',
                            'Φț®ˎʌԂнňǰ%\u0383һș\u0382ɭɘѼBπ³ɝ^ӆϴǢĶӯȢ\x96Ò',
                            '҂´ϧαĴӇ˹Ǻ!ĶǮ4ƘƮ˚ӵƤƹГťç˸\u0381óȧԌƾеfС',
                            'ѾĥăϿɤŜȣлңƷÛǘӾКċʨӗɭǄǝБǜїԕͽøϞʯñȿ',
                            'Ԣȸňʜ¹ҔŔæÒΝŲǐʈ˅ӫȓâȗӟΦПɞē·ΤЌ˷{=ʸ',
                            'ǋԀБӑɧǤȠҳԧǺ\u0379G»ŶѶҧКˤŗә˶Ҝ\x87˯rѣϸԮƒԚ',
                        ],
                    'licenses': [
                            "ϋûRˡԡʹ'с¨ɰӻΖϐіȰȊРӶŬҠҼŝϥʀþșԣФʃ˸",
                            'Жͽɖѕŭγ',
                            'ӅϷǻх!ҋìԘ·ΪӅЙǿǗɽȷzȚѶ\x89şύ?ЗМŃͻȪȌҩ',
                            'ϱБӽĀqѫȌÊʰ',
                            'гȃŅйǵ\x84˜ĖϪkRiй˙ĳʱƒʂʽƛˎǨâ˘ÆlԤ}ґԎ',
                            'ηŏȿ\x9dѺòȸŖɍĄbÕʑɚ\u0380ʜ΄ɚ҄ƂˆƭʡɈƷ҉ŤřǡЕ',
                            'ȶϦ^\x94ȔĄξǹȁ¿ϹδўкÌ\u0383)Σƌʵ˄ЋĸɰĂʛԍǻѤƦ',
                        ],
                },
                {
                    'name': 'ȧхŰҍ˥ŵҸāɎA"иΙ˹\x9dȖǡĞʍÜөԪȦǪҜǌņqʲԣ',
                    'version': [
                            -5478996027648936743,
                            -5365436359706754236,
                            -2573774393789879949,
                        ],
                    'about': 'ҨřˮΞQίɋŚļˉͿǇ-ȞƲΎ˧ҥǀзȴʦǹŷˤɎϫǍēÏ',
                    'description': 'ƊǬˎ·ϗ\x92ͿөAǑЛƺϧѮ\x8e\x86Į\x85ĈЋ£Ȉԋʠń\u03a2\\ϕΛκ',
                    'authors': [
                            'ђêȋ\u0378ҼjеԜ²аŧÉŹƦÝњԞ˄ǣˎǃŃØÑȸΎщǂ§ˉ',
                            'ˑӅЎβȸ\x86Ƣ¼\x96ÞźȭĈмL˔ņʶĘUǂ\x7f£ӳĜ҇ƶԠhԏ',
                            'ÕЇƾ\x8dɉѓĢʒűȺÃӖȌȺfİӐŢĚϹ@ȷϠŪǐӤǵҖȔϱ',
                            'ΧԠԁƏ͵ʮӷΎϘΓ×¥ԙɥԏƚҽPŷӵġ`ǼɘáԐ¾Aї\x8b',
                            'Ńˏ˱ȾʇÒǾǃʌŹˬǄѲȡ?ȨˑȚÏÚϭҨȝUmɵΓіƥƀ',
                            'őѣŵŕӨśԍȫϘ_ϯȯċƵǚѩ˺lťΥŌťѫÕʻӖÄǥӉô',
                            '΅ĲҫôАԐûʹҲЋĨЕӶӉýϔд˒ŃęŠɺTaƱңǾǏưɅ',
                            'ĭ˻ɺ6»ǰȄUӠɓӷǞªϵμͷˍҥĂԌɤΞZΰǌĕƺ\x7fųԥ',
                            'Ɠд˷϶҆КɊҎƬ\x9bϸ\u0383ʾҜƉźņ7ϲǬЕҌɊӧĹyɁѯ`ʸ',
                            'ϾЛϸŮưÈѻəɮҴУ5ˑɓԆʸȚΞЃӘ\u038d˪ɎлҜÙӸƧŲǂ',
                        ],
                    'licenses': [
                            'ĞOƵыʯˬүˡЅԏˀǨɱŻЙÍåOӄː\u0382ЦȔӅĐʹ˯ήɬş',
                            'ҼΪЄƺȚLˎɉϊϒѳƐhε²đȝűœJ±ƂȠƎĬѹѱȬť=',
                            'șҮɜɵˮϊɗһʹɢɃh˦şϖӡͳӾ§ʖıϐƼēħѱːΚΕϮ',
                            'ȆɜΕҨɫŅż˽ƧŎҁȪ˗ƀȷҏƘηȥɒĳǠҫȉɘЉ˕ˡďЪ',
                            'ƸҀΛӤȘϖɽԪЁέжŋĵӵϢӨҦĎ½Tʹ˰1ӛļϩķУš\x98',
                            'ăĎˁРůĥŁʶʍȀßȖ\x86i˯õŋ¥М˨ɂʑŰдˊ²ǆʽɷ҇',
                            "ѺAɖОϐΜь'Ϗѝŭ9˂ǢDɧǉԘãƨҺ˷҃ԜӴѮǽƮ'Č",
                            'ӤśķĈ|ʴΪӾοҡίΔɝwˆʶÀʑиâƩĿԌũ',
                            'ĺóѳĸwʀƍƯԜûʦҦΘëκ<ѵΧÆӷԙҠ˭Ȼ(\x88ĔȯЊҌ',
                        ],
                },
                {
                    'name': '@ЕǪʕʆ¥\xa0Α´ģѽRʝêF\u03804ßѺŻ¼΅ĘɏʳʺȋΦɺy',
                    'version': [
                            -5125972772583165557,
                            -3178358571312680052,
                            -2737876418804885136,
                        ],
                    'about': 'ēйҧőκԓТ\u0378Ѩθ)ʊяǸɥӸƤ\u038dԪԍȵһæļäŎӭѣŚҥ',
                    'description': 'A\x8fǥдЇȗρԇ˂Ĺ8Š¬!Іƪ˭ɸ\x9bˠэþѡʝˌƉʮӓкå',
                    'authors': [
                            'ΞʹЃĜɻ²Αӆ^șϡӗɯѢ2ǢʚpѮʮӚ0ɵӬȝӯˎλЈǣ',
                            'ģԩǋÏʜȤѾʊ_ӂ˱ùÈЃҖɀµнԒƌȅҀȲæΙtȾð˲Ӄ',
                            'ɺȹʹ˘ϵä˽ґɯӎҋκŃȊσˈ ƁǹSήƉɤѭтɳęϼ1e',
                            'Ӣ|ӑΎõȈϔlԢѴǂɓΙϧәјǲϣѺħԀͺсϖǒѽʱǜɒ҇',
                            'pѶöʸ;ÏкŅфҪЖҸȩɜ¬ӼǉǺŨǃƉǏΛąћξϋȓʧԔ',
                            'őhǚѯ\x89wԢÜѓϐкȉšɾп³҄¢уӋgʱ¦ˁˏԀȭМǼε',
                            'ǾьԕςӻΔǥl~ӀДʉʳĒ˫Ȉ.Ҭ϶ǠØńňԫЊӿϛѥ¢ϒ',
                            'ҕӿ1ňЇƽǌĠɿ˕ѝİΊӧ9ęʮԨĞɹϊǂĄԙ϶OѦĸά³',
                            "'ҺЉƘaЏƠį[ǟďфOԡ\x98҂ĳ}Ά˳ҝӀ\x97ʆɁ\x81ϥûʽð",
                            'ϽѠʑο\u0379fͳζӊϼЯʹȾĀǟ©ϾôѫÎʿŲȀϵğ0гҐ*\u0379',
                        ],
                    'licenses': [
                            'рź\x8fӹ!ӭŌkγѲǊ$њš\x9f9˔ҔÈϫхɼμƘ\x9fԭͿҟɑx',
                            'ԠƱϑЭĕǱƦˠkɜ-ӥƨŴ\x7føǆÛȚɏ˩ӻʞŮͷÌȡ˔Ƈī',
                            'ϖŷзʭӥIқΏĵԍxʦɷǅҩΫωҤɎÚʈϹıЍVжǧʏƂċ',
                            'ӌМǛòҷʩsǛˀ˩ȕĨûǏĥˠΊт|ʮ˵ʗԠɻӗуЯξʅI',
                            'ϛɝÜҶӧѸƕҹԄȷϪҝɊҁ<fҨуіϿɛƴKΔʐǙþ˕˴Џ',
                            'ƿϱɖͷ\u0383Ƹȭ˧ιƠѳΨ£ɀІ¼əΜȘUʏêɻŰӊѵԪȊƔЯ',
                            'Ĩ˃ϩ҉ȥБӍжÕѳåĹԌʕ\x85ɅмӒŤ˰\x8dðŉȹˠ\x9dk\x8e',
                            ' ˺ћǇYʄяʆͻτ\x99mȧМͽĲƎPǜˬˎοώŏΘԤşĘҳҶ',
                            'ļ¥\x80ķóӉʦfɯ0ɚЅ~ĠýζLҶſÞʧ©ƽɝɰȥϖƇӤZ',
                            'Ǿ«ԕɻфȝȠŧʏϕϷĶгƃƛĒě˂ԤƸˀěΧώΝěÎ҂ļ҉',
                        ],
                },
                {
                    'name': 'ǩŽȨǕЇͱϫ\x82ǐɞбýȰįˌțԦʀϐʟìћ=аО˒ˌIюђ',
                    'version': [
                            -1047322957426945374,
                            -3172706365879902523,
                            -7902373529275574485,
                        ],
                    'about': 'Ź\x94ҵʪũǰ˾Ρˈð˝˚ƻƣÄ¦ԣ>ӢşĺŴԩǎFΪˀƣЏɛ',
                    'description': 'ˑœҷl¸ĬӛʼƼ˺ðΧ«PǅɳӬЄԋάʛŚɵȆЕуȼǸȧȮ',
                    'authors': [
                            'ÅԈȕaÒРǝЙԦȬԌҪƺwρѰĿȩԑʊǑòΒlҋĄǈԑʾÍ',
                            'ÜяΦ҅˵ѫӋҝ»(ϴԨĠӋˎÌƎѻ±Ɯˠ҇ρơ˛ˌϬȄ϶ҷ',
                            'ϖ\x8aӚ+Ùԑf+¿қԨєƖͽɷɸ˅аaMӃЇȒνΙ\x9dԡѠϮщ',
                            'ƱúƄƽ7ˌÈЉƞ»\x8dϥʋǃʟόѕњҍХцϠƈ\x8aӈʪԁɍŗ˫',
                            'ȑкѮçƣØ˻:ÉΜ¡ҚѓŔΕЅǰԂЗԤ£ėӛà',
                        ],
                    'licenses': [
                            '[Ν˗gƪˡУƛŭʽέYѡɚ˲ɏý҉ǁ·2PόnĖӬʬͺěΧ',
                        ],
                },
                {
                    'name': 'ЌѮďʅřȖ˓ѤƑɻОǰȏлũŻԓβԠ˥LƯʵȸϾЯϙɲʺ¦',
                    'version': [
                            -6993687883124308383,
                            -3554559918465133407,
                            -6472820659038867569,
                        ],
                    'about': '˞ʢÅʰɩȹ\xadʳ҃·Љ\xadǇúѲσʫԤΕ¼ԈʅОϦοǸİƱαŧ',
                    'description': '0±ҠˋҦɌʽφǘгʯǨж҅˷ʎ\x99ΏѾŘѰ·ȘԬԒкŗɑăё',
                    'authors': [
                            'ЁˑēќʩϽʭȖ\x8f8ˆȽˀ\x89ȃШƎ˫ǿʱȜԪӝщӐЄ˷ΜҎ˔',
                            'ͷˊwÞ¤ϔԏιʹ˙Ԕ¾íĬȁϭƀȬƟщϩùČ˻ˑŔƠцεù',
                            'ƊȓѦНŋҥˊҦѶ\x98ԞñҁįɩҰΛνԂԆǸβʦŵǩ˪ȟƽ/ɽ',
                            '®XЫІѹԠͱĸ\x98Ĵ˽ҝʜǃºѻ]ѐ\x96ʨZϝƭøɶɎƚǑ.ϝ',
                            'ΪΌԈҐ˶ɞ/ǆŦфȦϙрҚϋѕΣǺ;tƥӿϯϋʭϱƁȃϑɸ',
                            '·ӽѱŴΒñҪƟÊǼəe²¼ʜʴʏЩ|ƃќ\x8dʨƚʼĝ¹Ə˜ː',
                            'ѓХΌӔȞ˄ѦɃɥƮǔóҊŌͿĥθƴõ˴ȲÐəeγļ˅ˋӯ(',
                            'ӱѦòсƔͷʏɡđҨӕ˓ȭŗʅїǕʸяOӱѠїˌʃԃҰćń¿',
                            'ԁ¶нҰɐĸϼǓ˲ԏ=)οǈΡŠIRĿμ\x9eĎțјҐ?ЃӚǫZ',
                            'ŧɹαæμϘһɀёǠϴӛοȊàșͽΪAċӵ\x7f\x96ÁҐ˚Źf\x80Æ',
                        ],
                    'licenses': [
                            'ҨΉȹıȌ:Ωũɬ˂9҆ưϋɫωτǂƧŚɀ˨˒ƇŎӃϔ\'"1',
                            '\x98ԊʧŻ^Ԧо\x9fȴťӝȜȎ΅\xa0ӴĞɛкԠӌhɜĄĔŤˢ͵ǞӦ',
                            'ϚƲĎŏ˒ѹƟξґҥĘҙtñάɣȪ\x8eЦčϹÂĉРŐʕʸȤϘç',
                            'ƺîqŴΞüϖ~Ьйҡ϶\x84ƒΑ¥áԑŅůɍʀ\xa0!ʿ±ˁ&ȃ`',
                            'üӱɄԋӄ\u0381°ʣ˦˒˦ҷҹƛ~=ûǩŁfȠѩΞõ\x97\x99ӝʭϞŁ',
                            'ѳȲŻЖĜÀʀԢŊˍЛīý\x88ʜĵɯѧŤ;ƾ\u0378ӇǃƬӥ˭Ȼԉρ',
                            'IȔqɤȟsӸÀlѩВłơ8ԩź6ѭȏǰΰӅ˃ĿɣǈєĖѵ',
                            'ēțϝYðΈ\x80ȄˈԏɕĐԃɀƌ\u038d¹ԃÀҫʯҏϝΓʠСȬϣИǑ',
                            'Ԟӧ\x9dӏӊҬ´҆ĹƎHȧƒ:Ϡ\x88ÔϠɝЇҟҕɗİʌ\x99҂öD\x80',
                        ],
                },
                {
                    'name': 'ǰ=\x96ҡюӡɓҿѬӮǜԆˊ-ЯԋÌԣ®Șеʙҵрʀ@ΜſĻƨ',
                    'version': [
                            -4166572375514588214,
                            -1758648133261477448,
                            -6471400329105338182,
                        ],
                    'about': 'CʸGaсҬʳĿԞ͵ŬȏҮҙəҩ®ŪőŜ˹č\x83ɚҘĊɡŖƬЏ',
                    'description': 'ϙoҰlǒѫїgʞǵә\xadˀnǈŤǩíŁЙʷɹʀʈxΝӪĬ@˜',
                    'authors': [
                            'ƁȭʰǼˁƉҼə\x7fƑӰԅʺƞʩ\x9dǄƬÎɞҀӡÝǭɢŵȚ',
                            'Ԓϡŏł˸vȨɹЖɱĽƮ˸ίϊ˖˽ԕʭѢӎҁõåȹɳӅ¼īϗ',
                            'ҟŜƐʔΦϱ҃ѬƀԩҺ5ʮǤʕϕȐʽΖɲƞҠȢǚ½ʿ˖ļӇι',
                            'ũƣҌл¹ɋćǋä:NǭˬożłƂɸǎϨǌ˯ŃϾ2ȜȿƬăȤ',
                            'ȩËƙɠ˙ΰғȵӉЂԠԡƜŻÉŻɫµϒÜҲąӹмԉǎHǖϘϏ',
                            '϶=ʜсϳĬÊƣȢƨЅä҈НŌԍĈŎӒɷƾɔ϶ҩяÝũіÄИ',
                            'őЗ˳şǝqǯfbҚҒϤΪƘӾCфŮĠĥϊtӞŅѱʊ\x83µÉϯ',
                            'ϔȷ˵ʂiӌ˧ǏÀ[Ïѯ˱iʷΎ(ȘҶƼ?Ѱʛ\u0383Θӎ҇\x91˺ǐ',
                            '>ʐϑʕԩɊ¾ʏxÖүʳȨӯưʧϿѹӱӣ\x82њȯȎ&ȮΈ·ϴԧ',
                            'ȑӊ\u0378',
                        ],
                    'licenses': [
                            'ЯɌȠсˌx˄ʻ˖¡ȽtϡӱȁΞƺȃ\u03a2ϿǹŦӼ"9Ïôǜșɀ',
                            'ѺÈ˼çϛ',
                            '҉қġԞԭΗǋқĈÙŔƴԬ˱ҀɕјԕӥǙgȠFıϭëϑʦӌυ',
                            'ǼŚɰ˘ӍèǯЦPɉϩ5Ҿ˩ȑҠţӜˬҦҞôӲԏτӾƄҼĞĪ',
                            'ˬЙҭơτГºҝɄÕĝɲӇŚЊ\x9dŐƯʑͳÆҐvˤƈ\x82ӋϨŪ˴',
                            'ĘŔԃӆϿźʼ',
                        ],
                },
                {
                    'name': 'ԧҗдщĲȲЏxæǳѸϓЧԡȊˏ˛ҬдyҍɥϹĕ×ƵCҺғĀ',
                    'version': [
                            -3959575151603162517,
                            -4213431765915797820,
                            -3155981573852274439,
                        ],
                    'about': 'Κ<ҫМʨ¬àŚύŐʠԄТʃϰǌŘ¡ȡӽВðǆŻϯӓ\x8eӖˏѤ',
                    'description': '΄ǀƮԘΒƹƴşƛΐΨџÑ¬ȡΆȚ¾\x85ƈ¼ϦаˎîϒџˏԬ8',
                    'authors': [
                            'ʝσʕʗěӖҩ(űѴǛȾċȎ щαѡYҴɀĻҾɡϗȻʛЌӜЕ',
                            'Ρ\x8e˘TµϘΨҥɐųŵԆ}χЁȸгѬɱҒ˺ÏΓǱЌǩƫőОô',
                            "ȵɡԣљӂ˵Ԅ'ˋŅЄÂԃʴΜΨɰң ǒϺWu˒ӟȁȩǈϡό",
                            'ɐȔԥˎBʿӺˎǎǝǺˌʌ\u0381ѽǜćUźʹľwӍrШÓѪȑҰґ',
                            'Ңxɘԧϝɛ²Ӻŕ<ʻpϹÀƏɿѶʀĖӳʵWҶ˾РӣňԌȱȠ',
                            '¹ţȭҭɷD͵Ӈϝȃ«ÏчПŔЋ\xa0ԉϸ˟ȐΝȲ˕j/ЋˮƖԟ',
                            'ǰǆƿΟȿͲæѐć˸³ȹѤԕÈ%ЊήʧĵԮòЗШñƯ\x8aˬρǞ',
                            'БӇҭä҄ɓƜҪÉ^ćИŇ˒ȊȩҊǌҢˢĢҞQϮȇʫčҵтê',
                            '҅˦7BϘȫˆÚ\x97ɋɢΗсJđƟжġ·ԀBƹȇƎąμЅĲſӧ',
                            'ĳԌӭ;ȾǢԊЀƕʺĸαΓԫͼʣʼԭɚӼÛӀõȒæˈԖɜѫ˗',
                        ],
                    'licenses': [
                            'ŜǐŵѬΘԬ҉ҭ[oǈ-Ȫ',
                            'ūˀӹΰˇыѮцηϣw˲őĊķ¯ȹǔqȸäǤ>ѕӧ_\x9eøςͰ',
                            'ԩҙɆ\x8dϭūĮȨʹ4ӬѾIÄƁəѵ˚\x97˰ТŶ\x87ʱ˒ҝʏ\x96˸¯',
                            'ʑ)іŤіϼĠҖԘѪɄԁȨӳĒșɝ¶Ɇ\u0383ːЈTϸҖɎñ0ӌ@',
                            'ҡ (˱ΥȞЧѦҋȱΕȺKθˁɬʩӒ¯ÉËM˽ҥɤơʇЕүњ',
                            '˗ʁЃ¶wɆѕĊqȓѕɆ\u0382_љɃ\u0382ѷw҈ӭ\u0383˸ǴʺϫԔӆҬʄ',
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
                    'name': 'ƨјϙ',
                    'version': [
                            -3710484483074004844,
                            -5760602353906144834,
                            -6124678657438849515,
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
