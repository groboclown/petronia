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
            'name': 'ӻǟȖπōвԊɉǳ|ˀӯÝˮЋC˨ĕ4}ʹƬƎѺǍĐ҄',
            'minimum_version': [
                -6886104738770281664,
                -6080696079091279216,
                -3699237787091818303,
            ],
            'below_version': [
                -1137949684765201081,
                -2564871960262204474,
                -5360066144026490984,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӫ\x83¾',

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
            '$': 'ǝĘӆ˕ҿǬƿԜñ˪ʗ\x8eƃ^ɦѮɥʄȗʫԘ\x88ϙвǟY\x97λԍѲ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 4894944651293534326,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -63487.66255711101,
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
            '$': '20210309:035052.292465:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ƿӖ˖ĢʦҤԅϠԡ˒ƅː)ѽʅӦɮȾŏ\x9dҬтÓͼ˜\x98ȵƊƯ3',
                '\x8dʛƬСkјг˝Ӿшgđ\x86ӞǁìӽҦʴ©ȵȁȘǺǝɎ˦ҔϤΖ',
                'ʴҘȕʹѩѽйȪŒˣӻÈɢӆћӘʄƊ˺ɋϝRЛ\x83ĻǊ\x8afgȣ',
                'ɉ\x95йǾyʭωЩЌд˩s\x8dюӅʾʟ}НΚĎĆǬċ\x8dȨƴGĢƻ',
                '×ԕяԉц҅ʋȆɹӯͳʕƴ¥ʝϤΟҙНԐӚǯĀiħЫӇϽ˧ы',
                'Уʯϓ˷ɅʒŞμǑΪӵɤƿΗǣǬˣѳƇΕù|ʒмΔʛʿϘ\x9e˙',
                'ģɱʑѰ˄ĈƶӋɨ¼ʔhҪҫǕOώĿЬν˚ϑǍ\x93ƒўŊ˳Ѓӽ',
                'џΘɟÃŭӫĆӾǡǥȃ_ÒʎĔɓɶǢ¦Ќʢ\x9aʓɤ°ͻ;\x9dǥÑ',
                'įɥƛԛȀĆ҂ѻˡȢψѷś;ΚpΒӣ\x8c&ҿґКEʮˠ\x94ȚÙ?',
                'ɓιԗȷƼÀÜʺöϋѽʳ˭ү$ŎˎͳʲǪδǻʕ7ЭİŏȇƟǓ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                169618471490047361,
                -5378171896634060114,
                -8503689720809764292,
                1526336260549467776,
                -8807397321076028887,
                -3980732100775761359,
                -8407242626766234258,
                -5615465347572216092,
                -6176590746448890662,
                1126943657660812860,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                958003.0758751084,
                764105.8076585388,
                -32913.854817799554,
                640655.4278510928,
                924257.8965540299,
                95799.19871374662,
                675120.4288203126,
                357210.3282695852,
                80438.91500704517,
                323096.8272495522,
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
                '20210309:035053.460863:+0000',
                '20210309:035053.481698:+0000',
                '20210309:035053.502970:+0000',
                '20210309:035053.524089:+0000',
                '20210309:035053.546280:+0000',
                '20210309:035053.567771:+0000',
                '20210309:035053.588696:+0000',
                '20210309:035053.609377:+0000',
                '20210309:035053.630334:+0000',
                '20210309:035053.650484:+0000',
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
            'name': 'ŇѧОњˎԆïȦҐ\x9fЌǟ',
            'value': {
                '^': 'string',
                '$': 'ѣʝˣҙҼůҲç˺²(˒ҭͲxǋҝӧȩʯɶgӎуėÓʺӾҪӪ',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ȧ',

            'value': {
                '^': 'int',
                '$': 5982248155637776945,
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
            'catalog': 'ԟÆVȻxΔљΗϤďʷǴ˖Хҵ˴ΩҶšϮ˾Ơ"ԥѨÄ϶ςʂƏ',
            'message': 'ҞӇҩҝԑÞ`ɶ|ʦʣƠΏӠļĽκԭ÷ÌцNҗ\xadŞʶŘѐҢͷ',
            'arguments': [
                {
                    'name': 'ԟѩЫӵҺŷ',
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
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ɼҏ\x8dıΡŚ×NΊȣԠӟĴїԪȟɬ\x8dΠʭȒӽóӚƌήʹԈǻǅ',
                    'value': {
                            '^': 'float',
                            '$': -97576.78055420524,
                        },
                },
                {
                    'name': 'ˤβԔΗ\x89οεȻӖӻβĮˣшгǝÜцӾҨʱӇұ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210309:035050.653103:+0000',
                        },
                },
                {
                    'name': 'ѬȘp˘κʍǛŕêïĤʍ˰ӹʲȋ҈˨щ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        132142.46904788283,
                                        196845.99244799814,
                                        77753.22792491346,
                                        -36825.33145069491,
                                        846041.1721769173,
                                        288810.41955695074,
                                        244996.83148791967,
                                        559661.4627651544,
                                        301200.6937717394,
                                        716164.836610421,
                                    ],
                        },
                },
                {
                    'name': 'ԤȘǅU˂ѿӴ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'аƵϒVЋŃ°ЗŗĽӣҭƧ\x8dfm\u0378Уŀ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'Z\x95϶ɝӀΨǇȼȠʰҙˏa˜ϱ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210309:035051.173022:+0000',
                        },
                },
                {
                    'name': '½ŽϰQcȀӄɦΊĶǶȞΖԥ¨Б,ǳʘΕĂˆƎђРӑ\x8fČǨҙ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ƤǟɂșĥӰpϹ,ǍɃĨƒӱnρҳӴœ¶ʷȬͱԆʓҹ˵ЦѫѬ',
                                        '}βϭ)ϮȴĴҗʞЮ`Γ¥\x83˗ćҥƵʱӪ\x94КʯΡˏɪǇͼôГ',
                                        'ĨўÓđǿʌҒƅȞċԊϦүӥс&ҘӑϾǀӨԝԩˣɂɗЎĺΐŅ',
                                        'ǠӶɅÊ\x8dџΣҶƣх\x8bgÔїQϓɱԤɅ¤4ǅÈ²ѮǘȾ«ɨʤ',
                                        'żěͿѤƅО\x90OĻԀ¿ʖΩҀϦÀĂƷźӳѲҥѓěөґҨɘÔѫ',
                                        'к˛àÅҠƤҠȧЊɦǙɇӏƧíЎëōѼяȥƨ\x7fľʻфɆ\u0382dǁ',
                                        'ʓΖ@Ó9\\òÁ¡ɼ˕9ȍÓƑRɨƬЄÜÅӞÙӡВđӹȘèű',
                                        "ǊƛZĈ%Ѳ'Ģ©ʉʎϖK˾ɕ%ƫĵˀȡӪχŝйқLàԞһŝ",
                                        'ƯЌҡϣԡөȤ҈\xadʑˇΎȥɼӳŃʊΔēSЧƟԎ˷ΘÌ҈ħƫT',
                                        '\x85RʰсɊϒίΜϲΜΒ\x89ˌʲºȟµͽɣʰӹЀɾҤÇ҉°ǎӌ½',
                                    ],
                        },
                },
                {
                    'name': 'ÒΎȔɠ\x9cúϐѨ\x8fӦ0ѭʽёÊGšKǍíѷĄʖƳ\u038dŴƜлɯǪ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ԭѐĨʹʡоҿʊѫӛ˽Ʀ;ʤɭӊȺҳѦԤɈǞΗгƮˡȎИԦʼ',
                                        'ΌɩŸЃ˃ϠΐÿЁĈI¶tʻƾшǦĘѣς˳ΰӀ$ǏӚČǞåǬ',
                                        "Įų$лǹԖӨͻЏÎΜÙ'˱ǷŭőӖǌΟiŨχńċπͼȨƷέ",
                                        'WƄʱԕҟ:ÄĆ҅Śȃ!ЋɑόŴĶĻåїӇʛҀΕ%Ж\x86-ӎΛ',
                                        'ĺϧĉƱˀǥʖʭɆОɰǷ-ЙʃɁVaˮÃԌɨüђԋń҆Ӣϛ7',
                                        'ůǌӹƛҦѷ˜ěҶʗİśɆιѰȐ҅ʇɠʼѭǱМ\x94ǎɕǊϙεѳ',
                                        '˧ʀԄĀϷϒ©dϐ{ӧƑÀƞĊҡG\x8eԧŅǹɄÚBĦŮ;ЪИҊ',
                                        '%ķļǞЭΦǼҤѰҨ˭ÓѺɏћґĉѬÒҮЧĪ\\ıǐсˬӯŅб',
                                        'ĞǅКҽʁɯˆɖˉӐ˚ȺϹΨхē\x7f2ƞȖ˂ʟþҰ\x89zԟÀйŻ',
                                        'Ԉ˚ѯɏϱΚңɉ:ȍšϗȻоůÐȔˉɺˉjʭҥϊȰДĀАƶʈ',
                                    ],
                        },
                },
                {
                    'name': 'ʦJΐįȠԏġļҖԅňҧ˂˟',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ʣΠǗċӯӭԤɊ҈ҙ˥яɱöeҜέ˘ҕʯʇAȆ©˸Ԭːˋy2',
                                        'ԞΒɕɷĸ´\u0379ӮӥΠЌú\x91Ԟiӕˑù²ȈԉÂ/ΖėŠ}X΅ӓ',
                                        'îԎлȋξϴʨҡzЧϺζƻϞŔ˞҆ԚΏϯύȣćĵ˥ǞʟԌҋí',
                                        ';ɚǬ+čǏиǰ²ÃĨɌчЪȫťùӴmJ"ʀҸǁå#Ēˈʖ¬',
                                        '±ɪɌȺӍɼϥ¾ĞuɯȑǶêȰЃхƸЯʑĸ?ĖЗϔʉéϯʥƚ',
                                        'ӂкдćϒĀЕNϥÑ{ѕБԧȬ¿ќ»ˑƸӕѹЕәΛʝŬǥŇń',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ėϟ',

            'message': '§',

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
            'identifier': "Τȋ\x81ɝÒ'£ѭˀ˾СӖѣƬдtPќɪξу,ΓƜʋ˨ȒʺЬЁ",
            'categories': [
                'configuration',
                'access-restriction',
                'os',
                'internal',
                'access-restriction',
                'os',
                'internal',
                'access-restriction',
                'network',
                'os',
            ],
            'source': 'Ć«ԅÛӝĞŜгӫӲʜґǧтĨґϛʓĽƍ·ԗɖǃʈƩŘËαǆ',
            'messages': [
                {
                    'catalog': 'ʚӑͷʕǵδƭüѠŽƷĥЅпβϒƗ´ǡʽʑƮŀǺɢα©Ƶϸª',
                    'message': 'žˢϏѳƩæʹўʾ˖ǖ]˻ǇɀɂŵΓƐɩàѶѥѥƝËǅŝκЌ',
                    'arguments': [
                            {
                                        'name': "˖ɒ5Ëʯӽ'ˀӡ\x8dɉʜϤǯЧȍΚΒʁƙĖʩѮАӹƌƥѮ\x86ʮ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035031.102175:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŕѽҪΊǢĨłϙҮѳˌѧϵ˃ϣqŴſ\u038dťҫ°ҩrbķ È~¤',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 567168.7126962258,
                                                    },
                                    },
                            {
                                        'name': '÷7ȗĢ˸ţˬӤҋş˰óэʵѪđП\x98ϣæķ>ѝϣƂΛȚɟ϶˓',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035031.236845:+0000',
                                                                            '20210309:035031.254984:+0000',
                                                                            '20210309:035031.272460:+0000',
                                                                            '20210309:035031.290076:+0000',
                                                                            '20210309:035031.306332:+0000',
                                                                            '20210309:035031.321238:+0000',
                                                                            '20210309:035031.335784:+0000',
                                                                            '20210309:035031.350533:+0000',
                                                                            '20210309:035031.362987:+0000',
                                                                            '20210309:035031.377929:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȡƽƢԌϬϖÄҗƣʒ҇ŵ×ȨɓԨʧγ/ǝƠ]eϳɣδʧƻxˬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -75954.71600661811,
                                                                            25991.596303604252,
                                                                            396683.1463186832,
                                                                            822791.2299660961,
                                                                            971992.2866529934,
                                                                            402613.05779336696,
                                                                            -33473.55481162622,
                                                                            224825.84035920684,
                                                                            441943.29222870304,
                                                                            -40760.55484958514,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Қųƹě˸˪ˌŚțЩͲ\x94Ā',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƕ%гйŸӦƄϮѲБǵàÕͽĳńμ˻ʳɂ\x89ԑԈʿ˒ßɸʢ˓Ⱦ',
                                                    },
                                    },
                            {
                                        'name': 'Ǳː®іôԩҒ\x8cȻǕђ˼ƶā\x82ѓǿӵƻӦǪĴĺΈžɔŨӰ˘К',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -68253.96857245945,
                                                                            176586.9307520152,
                                                                            799801.0449112651,
                                                                            932047.9316436838,
                                                                            226280.84484005894,
                                                                            45738.44829890557,
                                                                            203667.1714081943,
                                                                            310733.9564908971,
                                                                            861835.6727691371,
                                                                            509382.0967011724,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'аƟɻюñĳ:æÚȜó~ʷџˈÏӎɩʫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035032.142253:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˉ¤ӡӓÝԦϲÌzӅ¹',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 924971.7979881935,
                                                    },
                                    },
                            {
                                        'name': 'ˏǣǬΙIҙθєżѧȪɷõÿ1Ʌwϕ˗ÚÈԭ\x94ģđƮ˴ʦƎȨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɕ,Ɖϭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 139171.13777967275,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˦Ϻ&ɵӾJ«γȂĩƵҳ¥њɁдѨуǛѪϩĎząΈ˼õċɯι',
                    'message': 'ǅƅ,Ͱ¦Şзӯ\x9aǕŐȳƪġɮҡҿ˳yΞїöӪâПͼӔв\u0380г',
                    'arguments': [
                            {
                                        'name': 'ɎēɈʷĮ4ÃɑĘЙΘ˹ӺЂŇŵҋЧӞӻǱČШǒΣͱʄɑїΆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035032.762449:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϾēЏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8746721897675815815,
                                                                            -2996424363444326772,
                                                                            8171309326529898062,
                                                                            2665027830290672253,
                                                                            -3678675086460775173,
                                                                            4589707309473991588,
                                                                            2563358093055928654,
                                                                            8763754558004910137,
                                                                            -6266462424164604574,
                                                                            8987295801990083685,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǌҢʋʆɽЗ˝Ǝ\u038dеɽˋʰFӮɲņѦӁҔӂѲ@ҟØ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035033.149099:+0000',
                                                                            '20210309:035033.168256:+0000',
                                                                            '20210309:035033.186529:+0000',
                                                                            '20210309:035033.204130:+0000',
                                                                            '20210309:035033.221930:+0000',
                                                                            '20210309:035033.239389:+0000',
                                                                            '20210309:035033.264005:+0000',
                                                                            '20210309:035033.297471:+0000',
                                                                            '20210309:035033.326442:+0000',
                                                                            '20210309:035033.363480:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'бҔѿPԏȪůȆ\u0381ȫļʒҲŵΌňǭȏӫĀѣ˴ƽǏĸδмԕťѱ',
                    'message': 'LԐȴƮ\x9cԫǥ»ƂĚƇÚGΕǾZƬγҳÔόͳÄʵʁϭŁԅZͱ',
                    'arguments': [
                            {
                                        'name': 'ίӿæбƇӒϑƌώӀεϝ˱ӖƛǇĘҹпˑǺʷàΨǂʅĚǍÓў',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035033.555489:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΫϲÏçˮғbȧҿʎҭƻɓҠȸǛ˚ӤʞɢUѦҋʓƱƏȂԢƂ\x8a',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            122743642431315711,
                                                                            -2060654341832822757,
                                                                            4531992022348350831,
                                                                            -7486005427589461182,
                                                                            3240695329481927487,
                                                                            -8862934557327806916,
                                                                            -625366651105458734,
                                                                            5935776659631085234,
                                                                            -5583364101142282368,
                                                                            1063976996238107429,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Gʆ»!»ʂŵ\x89Ûš˼ȷΝΖ´ŕżЩ:gԝ˯ȾϐµȐøǾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035033.949770:+0000',
                                                                            '20210309:035033.973267:+0000',
                                                                            '20210309:035034.000505:+0000',
                                                                            '20210309:035034.022546:+0000',
                                                                            '20210309:035034.049807:+0000',
                                                                            '20210309:035034.072137:+0000',
                                                                            '20210309:035034.095564:+0000',
                                                                            '20210309:035034.116202:+0000',
                                                                            '20210309:035034.136555:+0000',
                                                                            '20210309:035034.155119:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'κ\x8eǓ\x83˂ʭȿª\x8clѪŨɣΐҹӇáț˷¹ʠιζҀԋĵf˝Ļƥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'ѝóɕǢԟȭOиѷŴңĳ˶ʥˑɪѾ\x90ƖʃŒǄӪ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'șӲǊɼƻУ©ʷɒʳƿǆ\x9aǗΤȦëу,ѮΈŸȤǃŌȝŴUǤń',
                                                                            'ȩtċʙҘɐMɗԓǲÏʱҾʕŔŁĶϥŖàhŎ˸\u0382ˁϾԠȅǴī',
                                                                            'έŤĖΌʫԍ9ǅ˫ĮϜǑΡξöɊϲЭŌн҂ΦыίÅϪӾāЙϤ',
                                                                            'ʂ\u03a2бφȜ҅ΑЫϾȫȑĤӒßйƎŖΈʴΤȼϴĴԋҒԪӐ:ƟØ',
                                                                            'qǆԢФxƮɊͶŰγÛŋƆƍͷ)đȟжʑbŰЫљщϳřŦĨô',
                                                                            'ǩŲʌŖȠѱŧǥǜӬĲΆȹƅÇɊӘλů\x84ʿdÖΠЧȫԎϹІǝ',
                                                                            'ȀɽřҽȧǮa\x95ȘϛҲŪɕʺΜВűћʔÇéȺ\u0379ČˮϸЄԆʔx',
                                                                            'ТǓwʗюʥӶōˣÑÖҐϨǦļɋȇџƹŠыӼɊʊɺ\x9dɍ\u03805ʼ',
                                                                            '\x89ƺѯʝƾŐɺ˹ӜʬЦǖоԕϞŗƫɓΗӍǔżϿԅȭ\xa0Ƞҽã\x86',
                                                                            'ĜЛЖЫЬɉʟ@Èѯ\x94DŴÊŃԧŒʣх˹нϷԕҝφCÍ\x93ɚӼ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҌñγǙţ÷ԕǳʇØɕǐ¿ãŞМϿ!џƨÔʹmμǶҏԊӫϋ;',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035034.866072:+0000',
                                                                            '20210309:035034.890973:+0000',
                                                                            '20210309:035034.915871:+0000',
                                                                            '20210309:035034.936591:+0000',
                                                                            '20210309:035034.956399:+0000',
                                                                            '20210309:035034.977647:+0000',
                                                                            '20210309:035034.998682:+0000',
                                                                            '20210309:035035.019596:+0000',
                                                                            '20210309:035035.041663:+0000',
                                                                            '20210309:035035.062719:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ėТȵƝøǫҳΌг\x95ž\u0378σԖԁʹѮƻԤ҂ѐǯȜŽU\x87ñɚÆƂ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035035.158292:+0000',
                                                                            '20210309:035035.176375:+0000',
                                                                            '20210309:035035.193649:+0000',
                                                                            '20210309:035035.212030:+0000',
                                                                            '20210309:035035.232262:+0000',
                                                                            '20210309:035035.252131:+0000',
                                                                            '20210309:035035.271285:+0000',
                                                                            '20210309:035035.291796:+0000',
                                                                            '20210309:035035.313402:+0000',
                                                                            '20210309:035035.332941:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'οӤƞǌǣӅ\x87ϧ§ˊá)ʨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5138003487569194685,
                                                                            -2061664350403826403,
                                                                            1533288640936774315,
                                                                            -8256760455912916063,
                                                                            -7266291818916014221,
                                                                            -4607193418485067949,
                                                                            -3354013843145911308,
                                                                            3635981650266085867,
                                                                            -9028220526986492610,
                                                                            409596217059489226,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƈʦǣήĺχ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7872966514657652328,
                                                                            64001740238526118,
                                                                            8612132719828927594,
                                                                            -6662307688240734699,
                                                                            -6349031384915333148,
                                                                            8437778045071127989,
                                                                            -7819009244805504348,
                                                                            9061979777095599548,
                                                                            1334389479952577797,
                                                                            188198550351247969,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȕӽä9Ǜ-ƗB1϶ҭʪŕʣɯ˦·d\u038bңΖ˔<ǘƴчЂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5990951472704506800,
                                                                            3640136057921842259,
                                                                            3138332337381878824,
                                                                            -5536925187169721261,
                                                                            -3414092941195646697,
                                                                            641280296909651595,
                                                                            -493314091488308050,
                                                                            8549277129744814768,
                                                                            -609414551542594317,
                                                                            -3005471023960141539,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӣőŹˋаǥԉΓĒƽѦġæEүƬǭƮʆИэȾƌЋԦƳóєїˎ',
                    'message': 'ϠóƇҰ҈\x90úћέЫȖʍ×˧˖ҙѻϱάҌˊϫJâÆćÛǊӃ_',
                    'arguments': [
                            {
                                        'name': 'úƛŗ˪ȜťɣėЏЎ®Ǹİ˳Αȧ˗ΖƵЉʘɝ9',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΈπţPϣШѳŬuεĴăԭћưʮӝʭïґǙΉʲˀǄ\x99ά;ϴ˹',
                                                    },
                                    },
                            {
                                        'name': 'җЧɸʈǂȭ\u0383ɣΊξɘ˒ÀŌωÉɊчХĦҖ\x99ϘўɠƤӥ(ǐӷ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035036.499358:+0000',
                                                                            '20210309:035036.524066:+0000',
                                                                            '20210309:035036.548372:+0000',
                                                                            '20210309:035036.572764:+0000',
                                                                            '20210309:035036.596340:+0000',
                                                                            '20210309:035036.620117:+0000',
                                                                            '20210309:035036.645552:+0000',
                                                                            '20210309:035036.672596:+0000',
                                                                            '20210309:035036.698264:+0000',
                                                                            '20210309:035036.722644:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ɨH˜nԇǸӌҴƥǐϿĉҍ'ţɗӚ˫ëRŪǢʶҨΨͼѭԍǗѺ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '.$ƃǁΑǝƽǤ!Ѿ\x97ɓ\u038bǹԓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'HҒѳɱɟĜЄѹĔǬźӹʘȝ˙˴ԚɸG\x9cӞе˛ʳȔͲǜGƆǣ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǬƆӪđʣ˓ƺ\x9cǶͶɬeȣԑиɧͼǴүмϔ^ɖЄѹɚʶāѧƟ',
                                                                            'Ӝʙҳ˂\u03a2\x97зȃŰӖкҒ\x8bФP]ǯ{ΧƧœϓȔγόĭËƱΝ˛',
                                                                            'ғȀш?ÖɊҴҽȭϏƵqǞ\u0378ǄЋhǱơʑŸӿИшɳͺӳӶӴĄ',
                                                                            'Š¸ZЀɳąӁƦĎӠƖCǴˑʸϱͶɇϮΠӧɣϓśĎrǬӓ0Ý',
                                                                            'ġʫˀҘԝħ\x97Ҵҷ+ʏβƥşԀ5ϥԍυƒƦ(ǚþǀˣƃ͵ȡΪ',
                                                                            'ʹóǃȿǟɧȸÅǽҵ¿ΨʑǤЊ6юӭ£Жù˵ˤҠˈɷ\u03a2Ǽæę',
                                                                            'ȿɅŋˍƉєŎÜɹуԉӛ˗ƿҀkԜҞΝʖњêƨϚ҉ˏɕѲΤœ',
                                                                            'ōqÿĔɉІүг1ҞӬǆRÒ\x91Œ\x81ɊʈЂoǄǅԟđŒķƮϓȃ',
                                                                            '҇Ǧ-˞÷ȏˋǕĩĻǚŘƘąʫ\xa0ЖфĩȹԜȕƟӒ{ƽˁяϥĬ',
                                                                            'Ш˛ǩϦVȤŴȫӁҌƝȿλӃѧzĕЉΊƿǯў҂˔ŨȃƽÒxӾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "Ц¦ƻƏäҘтtÊѵʊӢҩЕéИӫâ'ǤīӧăύЀϥǕ9ɜė",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 333191.74206212605,
                                                    },
                                    },
                            {
                                        'name': 'ҁĢΪĆΡгŸʗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɸƉʑτƍǨȰӮǜĦʞґȴǍĿΙƒɊƩоГxğŠȹɇq\x8by\x9c',
                                                    },
                                    },
                            {
                                        'name': 'ƺȲ˸đԗǲ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˑ\x8f`Їɏ³ȧʑƺʇȀтҳΏεƿƢňŒѼǀɫƵнǂлҝɊrʜ',
                                                                            'іǝʬбҀYÕƤӹʳθϔÏιϠѤɚȍηnГӴ҃ԙԭλ\x87λʂ-',
                                                                            '\x9bĖΩ˯ȩХ˜ƽўҹdыY\x92ϏȊRφÜƵтˬǷҕƇ϶ώιүӁ',
                                                                            'Θ}\x88ýɮ²#нǄŽ΅ōĶЌ˻Ԁ÷ΒƲηԓªeƮΘѬɷ¾Јπ',
                                                                            'пȦάʵҍĜWә˔ƈǌӎȼŲǶɵ¾}ĒɚǚϭƉëAӧ8\u0383ҏ ',
                                                                            'Ԝ\u0382ϫɾΪԍƫ˷ωŞλǯĜѠпАҾɦДϒĠŶȬΖӎÝŞϞƑė',
                                                                            'ҧˈļ˃ŞяɳƉҍãӈțπ(Ô˛ЬĞ%ÞgťkmÜkσɞɐǅ',
                                                                            'ÀЋʊϦșȹϠψњҬІĘϓĹс\x91d]˺Ɔğ˲˶ӻЌŖФ\x99KĮ',
                                                                            "ŅНͰйѴ˗'ĩў\x87ҁΕÉɧͻчηӽƪĩŎÃҝɅŨ!äoΠƗ",
                                                                            'ƀǽ(ȯMèǴȨ˃ȧȋ˖\x9bқȡΕīԤ±˘˻ɂЮģȦɛҸ-ѭĽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӄύ·чĘԚȓȳʍɡ˲CŨO«1Ȇƍ\u038dӵѲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȕ\x94тҟˊˀ\x83¬ƲϳЫζƐɒӢçĘɛ\u0379ӋкŻɅԎѨƄ#ϭȰϪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2342905346547666871,
                                                                            -6005496889794265195,
                                                                            -6658544052305346080,
                                                                            -4816024740433660288,
                                                                            -3421217828672305940,
                                                                            -397205049869676813,
                                                                            -4363904909008261090,
                                                                            -1440998769996234250,
                                                                            3211826081284244438,
                                                                            -4789394201318611592,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˉ\u0381B¿¨ϱƷғȃāқ>ɹŋїӽıťҶRǒʪʨcіƩўø¶ɂ',
                    'message': 'šÁԞŒϰͽѠӱ˾ћƷĻй¹ȹtɻȌ˗ΨǋȽʧǰÆԞȜĆӜǲ',
                    'arguments': [
                            {
                                        'name': 'ƏдǱŸÜξӞƯɐʀà\u0378ƄԆǑҧǕčΌʪѾǐɧ\x834ý°Ҽϩƶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4283613923816366911,
                                                    },
                                    },
                            {
                                        'name': 'Øβʟ8ĳĞӖs×˗ɩϧҪɗ)φєΗŽͶƈаȩǞ˄ˁΗʗ{˧',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¾Ǟϑ\x91ŘˏʕϛѣʘǙǅǙı˅ňӐƦαËιξ(ДǦчʨЇǾʅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035038.518618:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x9fĽԓ҉đŠЦʄ)ʟԕǺǼƤ]\x82ԀsįԀΚԄȞѬȼУˏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 561945.8836659925,
                                                    },
                                    },
                            {
                                        'name': 'łƍȐɽϹ΅ƀҽ˒',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035038.691083:+0000',
                                                                            '20210309:035038.707090:+0000',
                                                                            '20210309:035038.724244:+0000',
                                                                            '20210309:035038.746344:+0000',
                                                                            '20210309:035038.763218:+0000',
                                                                            '20210309:035038.780191:+0000',
                                                                            '20210309:035038.797051:+0000',
                                                                            '20210309:035038.812487:+0000',
                                                                            '20210309:035038.827029:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɲƗ΅ū7»Ŵź±ӺԛҡmąÏ¢П\x87\x95аʬӰÍ\u0383ĖżԀӭČѕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1716007101152686493,
                                                    },
                                    },
                            {
                                        'name': 'ЎûŤҜʨz3êĢ˻üʤΓўŏϝџ\xa0ťkѳ˟ΓЮŰī¯ͻǡ˾',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'өǴΤ`έȠǎ\x96ǷƨК˵ń˘1ыĜCt¥ѸѨǥśѮщʨыɬf',
                                                    },
                                    },
                            {
                                        'name': '\x9eΦŗ!\x95δ6ą~ǽħԈԛɥƂ˹Ŧ҃ѤˈЕśƙÆ˳Ϯ҃ѐ϶ɞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9127262044392414483,
                                                                            1086046466619067325,
                                                                            -1135008084762175807,
                                                                            -912172997780023373,
                                                                            -1574452995789062892,
                                                                            -4332127428570769065,
                                                                            2312929479949346107,
                                                                            -6956223692740112941,
                                                                            -2972417273049154241,
                                                                            -5491430836478335066,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԇį˖\x91ƓÍ¶{ϒ\x9dӑПǵż\x91ǷʙpҴћŗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɐēìËèЮȣ҄ǩ˂ΡɜˆԒƒьҳĹŪƩЅɚhŕВˁĿɞϧӀ',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'чͰʤȼǭɳΔʄӬjԔΰƭkǳ϶ĂѡӔөΎȳȄǈǽӫҀN΅Ç',
                    'message': 'ҖªΊhǜřμѧԩƈĿƳȳʆħΟˍԮ˧!ɐԛήЅźҲʮĢĈȴ',
                    'arguments': [
                            {
                                        'name': '¨ŏʛҔǨĈbҢĻ\x95ǸԈʹЇӚƏşƾϠ˨Ɣ\x8cӡƤϑǚLü\u03a2ˑ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1620623795605300047,
                                                                            6974479528983227401,
                                                                            -7939610884008401184,
                                                                            -1166489865868669815,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'БƠʻÄ[îèľҘŠƒԗς˽рǳҬ6ɦʮĲѺɠΓʵӀȉσ4ˬ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x84ȀɢϘҏʲȪ˳ȫćϺȻˀԕѽИɏɂрȎÄ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ğάɭяϕԙ¢ӞȟǫʽȚǧχƴўŻгĩΊҾʇòΧș˞ɖΨ~\x97',
                                                                            'пΓ\x7f˃ϨǼǀ˟ˈî;ƚňšϗjÕHÅɓźԆʚǃφЎ`УŖѬ',
                                                                            'Ӕqɰͱ\x96ȝԪű6ϝƕѩϊǅҋλͺũƏͼɶĈɣѳ˥ź½\u0383o0',
                                                                            'ҠÿҺëƣǯЄ˪ĤˆԏNǥˢ҈ϣʃȹϤƌǼɕǐЭŨgѽЍҐȄ',
                                                                            'Ǥϔβ\x8aȁψњ,ȏıĕ˕ǣȝɍґBԊx-έ\x90ћĽȡҰ¾ŪƝѸ',
                                                                            '\x8a¹ѦԘŜѧçɚɮÅŦƀđƇĮîҀӲǉʭԙ˘ǯΒԅδȃӱТ҇',
                                                                            'ˑƑȕĽƸʠɳÌɇȨ҇ɩpԏw\xad÷čɹԟҮ˝хʦѴȐȴſˎʸ',
                                                                            'LɂƛҾӫˢȢȵˋ~ѮǞљԜӬπҥЂȉŉӽ\u0378ǞҟсȕӯĈdŠ',
                                                                            'ϙќź\u0381ɳŚũΰ!ʛÐ˗Ӛ;ɣpԉ˂\u0383\x90ɂӷѬǓÇȎ΅Ǟșʯ',
                                                                            '\x97\x88Ȏʒ§¦ͼΒʀĝϪǥʊǪȖʣѹԘ˞ğĈ`ƃªŁ҃Ӟÿϱ¦',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'țǻҬԦǋɈʄʼ\x85ʘĎƿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035040.690386:+0000',
                                                                            '20210309:035040.712477:+0000',
                                                                            '20210309:035040.735520:+0000',
                                                                            '20210309:035040.757973:+0000',
                                                                            '20210309:035040.785184:+0000',
                                                                            '20210309:035040.808053:+0000',
                                                                            '20210309:035040.829894:+0000',
                                                                            '20210309:035040.852366:+0000',
                                                                            '20210309:035040.874165:+0000',
                                                                            '20210309:035040.895934:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Юѽ&ʄÞмҡԓ\x8dŰӕӞǘʃʽãǿΰˠӳØȜǁҬНЅŜ˜hԦ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƞЁÃĆ÷ĐŒȺʟȏЩmɪòѵԍŲ\x9fƠȦYƄϽԛɫɿԨǇʯE',
                                                                            'ФγĞƻƺӺϺͶǏʘΠϵȲΰҧƺɬ£ϰΡӼɏцƈԪҝȾ˽-˘',
                                                                            'ǯϲǜĕʝ"ÕϐԋͱψѤϯ2юςȐFèājзибȕҒвƍnη',
                                                                            '·AӅəƍПȰĞԇǐŊԦӀüŌǻÖЪźǈƔСǐѭˏ®ӀÎ2Ѳ',
                                                                            'œʂˋÉʹ(Ŵ§ÙϢӽǝюƠӼ\x9eɐ¤Ҟ\u038dˌԘԞԆʻφŤӓĘч',
                                                                            'ҾȿƲȒϏϟÜ(ìŗΫÈʭЊ\u0381ɋǔŽǹΨӦΧȈɎӌ\x82ʯύғɓ',
                                                                            'ɊӥŝϓєŹіɣƐЌͺʭǅǽѹžʗʸɞ˰šȢğôĵpӭ҇ңO',
                                                                            'Ϝ-ЪʫʃгӝsϰĶƺƀŝƊǚYҥөĕѡӈϐĳԚҥѰӋÏʽĤ',
                                                                            'Ϝƺ҅ύȺЁ¢Ûý6Bџ˾6ҲŀҌȫϓɶ\u03a2\xadӪʌȻ!Ҙ˓ЈН',
                                                                            'ȬˍʢŻӡҲʫŮԡԡȸġʫӝ˄ȮīʚϠс˽ԜBɁѶĪ\x9aМɋΤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĝȏө΅ϼǋҫȂԟƒˀēdoȖԒˠΦ˶ǋͲϴы;ŕáЏūǎӌ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '!šg;ːхȗ¯ф\x8eΏżƘȿĲƊҖԧϋ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            245450.9501071396,
                                                                            565187.1844392958,
                                                                            419443.15808945784,
                                                                            242735.92930708855,
                                                                            76532.74337650894,
                                                                            675270.8691923033,
                                                                            -46730.96263715254,
                                                                            121859.72035533268,
                                                                            577716.6454335522,
                                                                            -87693.42510317318,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ý/ȭͶʅЅчǑπ\u0380Ѕ`ӓƀʚ³ϲҺɱЪSˤкЈԉɄ΅ӶȖʶ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035042.174886:+0000',
                                                                            '20210309:035042.195624:+0000',
                                                                            '20210309:035042.214418:+0000',
                                                                            '20210309:035042.234293:+0000',
                                                                            '20210309:035042.254749:+0000',
                                                                            '20210309:035042.274595:+0000',
                                                                            '20210309:035042.293166:+0000',
                                                                            '20210309:035042.312821:+0000',
                                                                            '20210309:035042.335291:+0000',
                                                                            '20210309:035042.356323:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'гҏЏ҅Σӑ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6750771195281347684,
                                                    },
                                    },
                            {
                                        'name': 'ʐɟƴƓϞĜЊьҿȟ˚ʇ\x9eɨЗϵҏϠQѭ҅ȹ\x9c©ǌĸбRʻv',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2933871360409678044,
                                                                            -6144804131214071499,
                                                                            -8879005479049150154,
                                                                            2875414274966862525,
                                                                            3393472905145627041,
                                                                            6872594449731320584,
                                                                            -390956531323420819,
                                                                            -8408218933872315847,
                                                                            -5696820666771262779,
                                                                            -3888355189939185790,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ͳҕņҗΩҬu;ɍĘĉgΔԅΑѢȜƂΨŏɺçщӗɋӇõҙΜӯ',
                    'message': 'ɎÓƼзĂÆ˷ʸʘͽӑԐȋƴ\u0379ʅФ\x9bȕÇл\u038dӇjǽϓԏѮæӾ',
                    'arguments': [
                            {
                                        'name': 'ɽЋĸŪîѝуȤ˦Ȧԫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035043.086073:+0000',
                                                                            '20210309:035043.105022:+0000',
                                                                            '20210309:035043.126667:+0000',
                                                                            '20210309:035043.147588:+0000',
                                                                            '20210309:035043.167211:+0000',
                                                                            '20210309:035043.186202:+0000',
                                                                            '20210309:035043.202528:+0000',
                                                                            '20210309:035043.220156:+0000',
                                                                            '20210309:035043.237158:+0000',
                                                                            '20210309:035043.254888:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˡҦŽϵĜсӱŮȐʸŵМυƷ\x91ƃǐϷǕǖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035043.344024:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǴӒӁ°ŕӭŶ}\u0378ίU҉ԋ/ǅ×ѮʒӓǺʾζχ\xadԞѰʔТӪĿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035043.423322:+0000',
                                                                            '20210309:035043.444109:+0000',
                                                                            '20210309:035043.464770:+0000',
                                                                            '20210309:035043.484817:+0000',
                                                                            '20210309:035043.505419:+0000',
                                                                            '20210309:035043.525373:+0000',
                                                                            '20210309:035043.545657:+0000',
                                                                            '20210309:035043.566598:+0000',
                                                                            '20210309:035043.581204:+0000',
                                                                            '20210309:035043.595710:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˁӚѿΉʩɖǲҲ˫ɹԬ˵éѲ҅Μʚʒҡҫ҂˼Ԕȳԏ\x8eѶϛϡΝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035043.672289:+0000',
                                                                            '20210309:035043.689305:+0000',
                                                                            '20210309:035043.705814:+0000',
                                                                            '20210309:035043.721250:+0000',
                                                                            '20210309:035043.736484:+0000',
                                                                            '20210309:035043.750731:+0000',
                                                                            '20210309:035043.765121:+0000',
                                                                            '20210309:035043.780150:+0000',
                                                                            '20210309:035043.796526:+0000',
                                                                            '20210309:035043.814525:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŝϝļżˁ%ȝτͶƵƁΪцɭ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ұӓҺėuȝēVϾϖϫź,ԣŬԤρƪąslAξuĂƯǋ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȣĹҎʊўͼSҾͱɎ×М\x8aŁŖӲĳ˳ĭȸǡʌƗ)ʢҚȷ3ūʫ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                            {
                                        'name': 'ϨӵʉlƩX˪Õ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɾưμφʽ`\x88ԝĮ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            91434.26408981674,
                                                                            493873.7004620207,
                                                                            729227.3175975656,
                                                                            613971.0071544003,
                                                                            74299.25208615747,
                                                                            -1628.8268049207254,
                                                                            706330.0571123944,
                                                                            10077.196160387612,
                                                                            689107.3344551147,
                                                                            987620.1863385476,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɸƏЌҍ\u0380ÐϓĎӡ=ӾǁӤ\x86©ϴȿÓϋԅŉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035044.793903:+0000',
                                                                            '20210309:035044.809748:+0000',
                                                                            '20210309:035044.830129:+0000',
                                                                            '20210309:035044.846509:+0000',
                                                                            '20210309:035044.862937:+0000',
                                                                            '20210309:035044.881439:+0000',
                                                                            '20210309:035044.899614:+0000',
                                                                            '20210309:035044.915694:+0000',
                                                                            '20210309:035044.931239:+0000',
                                                                            '20210309:035044.947466:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ԉ\x93Ćώñҡ0ҫ˽\x96σ\x93ѯ\x84ѷȍϠРϥȃӘȬ_фŷFǬȓʍƯ',
                    'message': 'ǽƽÿŒΩšҎǭōJĤ¿ͻҭҰͷѫӫ\u0378ȓĳƋҩԏ½Ĺ˜ZȘѾ',
                    'arguments': [
                            {
                                        'name': 'Зӊ~З',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4356561788418365756,
                                                    },
                                    },
                            {
                                        'name': 'τǀѷϳҘǍɨʬτѲêјћD',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035045.193727:+0000',
                                                    },
                                    },
                            {
                                        'name': '"ƇԋŠŧį',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035045.264155:+0000',
                                                                            '20210309:035045.282519:+0000',
                                                                            '20210309:035045.300001:+0000',
                                                                            '20210309:035045.316445:+0000',
                                                                            '20210309:035045.335131:+0000',
                                                                            '20210309:035045.355664:+0000',
                                                                            '20210309:035045.376008:+0000',
                                                                            '20210309:035045.393446:+0000',
                                                                            '20210309:035045.414706:+0000',
                                                                            '20210309:035045.431124:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʭе˶þΉѿӣɚűε71ĝ¾Ю³ȪʵӯԣҠ˽ΠǎӈͶʛʓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ͿεħBҹтԪΧԢƪØ˼ʈ\u038bÞҜџʦ\x97Ǯ©қӢʸ˚Ԧ\x9e˳ԨĴ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                                        'name': 'ґϗ½ΔpҦϵǟӵŅȒǭϗƁҬΊǆȪӰɩį«ͿҁM\\~\x95[Ь',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʪʶŸəёȼɰʐ+Ӈ@\x8fԟȔǱťԔԘċʹǉɔ҇ǈԉ˚0/ˋʾ',
                                                    },
                                    },
                            {
                                        'name': '#\u0380їԏˊӘ¿вɅХгŎӮ%\x8açȊЭѠ˒ήӛϛ\x8dƫ{ϰƇɊȭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3383932217338662077,
                                                                            -9218395293457795369,
                                                                            615735135020882241,
                                                                            -2189251602500393755,
                                                                            1723938999278379486,
                                                                            -2076622313134924216,
                                                                            -6714769962122315205,
                                                                            -7305114986918121829,
                                                                            -6599220871845397633,
                                                                            4010260055922073868,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÔŁĸ«ѓѤˈÖɐʹҾӎε"Ԫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035046.078837:+0000',
                                                    },
                                    },
                            {
                                        'name': 'XӕÇ)³ʌǪµȔċҜɟΜԋόϼĨĶҹʵͻˑ¯ҟҔҀϔѫθӠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ſȒɪɞҫˋŞĽӖχżãȴͳϯϡô¸ȹ˒×ͲСùä\u0380ūҗȸЦ',
                                                                            'ͳ҂ԞɛĘξȱɫҖҰѵΆӶɣʌģҿѭȲӅMτZϐӼӹψĳƲŧ',
                                                                            'ęƅήԁȺӪƷԂɂʲԗȗ\x8cʊӨΤϜІƟπӚ˻ӧxǓʲdĒɅʤ',
                                                                            'ʞƸаŮəȓıЯ¥ɍԣƟˈ+ƻǇlӡϠ˟ĈÞ|ϲºң1ϔǦɡ',
                                                                            'ҢԠũ\x8dІǖϔҰχԝăÎȞņʞ9=˷Őӏϛ˩Ȑ\x87όɶӘ+ʡР',
                                                                            'ğưʝ˲ӕѲÕϦñʰxgΞʟȴãŊ\xa0ȉ\u0381˽ФѤȄķɏʢƈÐİ',
                                                                            'ϱΡҟ\u0382£+ÙӔϺӍԔʲƽ˔Ƨ$ȘʅϋǃʟǭŢȚηøʸȻʡЅ',
                                                                            'ґʆʈΞò\x90ϣ~˗ǂϽ˱ΟҧJʦҎQΌÍюȵ҄ĉʲϊɻæԀϕ',
                                                                            'ş\x91ҝOΌyӱïδÄΏӤҾӣQʩų˻ĕȠҐjǊάDƯΏхĽԓ',
                                                                            'ǊȹŵȰЙāҧƘϏѹѫȺŊΟ0ӏԆįЦÇиɦ˽ȝΈŷɮYҚΩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɹƈǰԧɾѝȵǩƳ5\x87Эг¤ɚϳȐųǼøԊ;б',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ôӬ˫λΓΥɔɸΜśĠźǇŜƧÔÅɶɛǸѐʢӐюӛǿÊӵѦ9',
                                                                            'Ԓě\x97ҘɛĆԡʗˤӂҊΩʼϲʀȻ\x92Ȭ±ʂʄμȠwѱĉЮƚϷʹ',
                                                                            "Ƣőȼ'ŃϊɯЬȪŬ˾ΝĹԩPʭӐӸƋB?њњďѬӴʬŊŐʃ",
                                                                            '˼ʆΊvĭюĈǞƶÈ\u0380ŧ΄˧ǗҒö\x8eǍʎƍąǡ#ʀНMӋèȿ',
                                                                            'ēΫʜЈȈǙӱúêƏЕȸҍЦĄŐͳÜţ[İΊҙΣӰâ\x8eˊιʀ',
                                                                            'ԊҽяΨšǁԧ҂ɯԄҭҿλGɊʰq˦ЄΘбȊȓʅØfŻɍ\x8fϭ',
                                                                            'бӞBȝŬɲʯώǃʱ˰ΐɢˆɴИԄpèˮ\x93ŴɨσʬǚĳϢŁ\x9f',
                                                                            'Ǭ¾Ƚ҅ƛǳĤƆҞɻ/\u0379ƀбĺ\u038bηșºǾʹѧϠà˄ǄЖǶΌў',
                                                                            'Ģ8Ƚь);ôȽǏѬ\x8cӡϗKřʹÌûѪ˄ӧˮӝэҔétɑЍɅ',
                                                                            'ţЛǽsҁɜȽʉ²ſʝŃġр\x97ϓ\x83ıӥӣӍâ˻ҀˆЪϑɜЛӓ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʅŇ;϶θ˃ǚоɧѝQцԄώǕёƥİŎʮȫѥɒϖΙŝϡȥȯǪ',
                    'message': 'öƟʋѺ©ÔԓMΫJĄŏԄ5ʨˍʔ˚QѵǤˢʸϳÿоѭǽ\x96Ĳ',
                    'arguments': [
                            {
                                        'name': 'ƒăǽ¼ЯƘąԅÅÏ\x82љƞʼãӅψð',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԐӐӏϿŹʲέȡе\u0381˵ӌÛưǹɾ¢τɼΜр6ȴΗƧcӺ4XɁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÁΖГλϣL\u038dЩŘҮѠŵӉgǱʫөǹӑѯфɺʖҟԭűġ\x8b҉Ü',
                                                                            'ԠȍƢȗƍˊƙІӨÿʚбOˇѣȆӴƝӄҕюƇÒŌӹϰ\x99ɬСА',
                                                                            'οȐӔ«ƋʨeũύƻɗöҗȺ#ȰĤÜȂѐњɸ˴ΘõƏЉǥPƲ',
                                                                            'ŹӵψҷbӴтǯŪӛ_ȋ÷ԄǿωϵǙ\x86_ãŭþŜ҃ϟɋɜлԏ',
                                                                            'ǉı͵Ɏ¿τˬİēԎľ=Ïа¡ȵƞĥ\x93ǩҦY7ѝ:Ϡȝɩιİ',
                                                                            'ҝϤϓȳрɛîҀҲьϺTĨ˞ыІϥƆӯĒȋʞΉʜɾѹăĬɣç',
                                                                            'ƒwɮīѣЗђэžǊњˮƆjǄΡʲƅţÝƖϚňǺ&дǶύӽЂ',
                                                                            'Ɵɸ˸ŚŴ˱ǐӮʃϵǰ˻Ʊ\x8aϋ˕ΆɻҴ\x9bȱϢ˂ưȣцϘӈmΪ',
                                                                            'ŔȍǍˤ҉\x99ґĈł÷ҷлҮ)ȮԬѮҪ˞ʮʾҐɵȕȜԪȚӺʆԬ',
                                                                            'ѨӭÒ\\Ɉ˫ˊŹЃ\x8cŔɐϸƝеȧīϲǌҢȷІ\x9aЌƏѾõвœȫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӺЯ\x83ȂϿßǨԨĄΝǒĹϰ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԨҨ}ε˕Ǎîƽ˷ĥљªϙŬɀǊѲɑ\x8bЏŃĵµMīƃθˎĭŰ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035047.540639:+0000',
                                                                            '20210309:035047.566161:+0000',
                                                                            '20210309:035047.588342:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÃЎªùʧ\x95ĜĬîϸˮώΛԙÜM\u0383ƸƐ\x80¤xǣŘԄƫǨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2314753763940437642,
                                                    },
                                    },
                            {
                                        'name': 'Тȯрȍʳȼ~ê҈A¾«ҬϬȘ¤Ǹ҄ϽѠ\x7fШˀ£ö\u0379˨ΈǘĤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҐҴ<ȒʦΡϠ҈łσƗΙİÇη¬ЋƧҗī˅иȶғўǬǍӟͼ\x9a',
                                                    },
                                    },
                            {
                                        'name': 'αʼԀvϢŰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1978998865050569657,
                                                                            173837292373798621,
                                                                            -6477840354338562549,
                                                                            -8430105639292213639,
                                                                            -4491856141973699197,
                                                                            -2978145483983991350,
                                                                            3783352632492900698,
                                                                            3797552948006930626,
                                                                            6315937170229622376,
                                                                            -6819510998825215423,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӼȢϷԡǸѬȸƧγǼϬϹaψǎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҽ<ȘǍǒιƂϼύǉΖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 259555.37706983293,
                                                    },
                                    },
                            {
                                        'name': '˦ҋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʛѕґʛŪƂ\x91ūŮӯƳ@ņ%ЂԠςȜϘʫϮ8ӑѫлɻ`·ʥ}',
                    'message': 'гӆϞǑŐ©χӔǱ#ǅɆMΕɢВѐӆ˳ɀˢҮǦɓш˳ɑǯśԕ',
                    'arguments': [
                            {
                                        'name': 'ѺӆҒǌ˰˖ԉзŭȊ˗ϡȖeñǍ\u0379ԃҚ¸ОɉҾӉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035048.739903:+0000',
                                                                            '20210309:035048.757391:+0000',
                                                                            '20210309:035048.773406:+0000',
                                                                            '20210309:035048.791388:+0000',
                                                                            '20210309:035048.806180:+0000',
                                                                            '20210309:035048.821666:+0000',
                                                                            '20210309:035048.837784:+0000',
                                                                            '20210309:035048.863166:+0000',
                                                                            '20210309:035048.881478:+0000',
                                                                            '20210309:035048.907792:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'š',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'юɔÝГԙЃɔΚћȟwŤˊǄſӕƂЛƝɉкƌ\u03a2ʕПɲɣƞүм',
                                                    },
                                    },
                            {
                                        'name': 'ĳΐɫϘωˑϐ\x8a',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '·фȖ˂ɩċʣѽʔҩƞʀ7ɌǜéͺƯӶі΄Ӽ˲ćѝҫʀ$ӺÍ',
                                                    },
                                    },
                            {
                                        'name': 'ȞãʃƕŃʟǅ˓ͷ˂ςȑǁĖϵ.Ҥ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӿŘzvұƮԠΓʾwăƢҨÛ\x99ì+ЌŻ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¦˵ԗCLԉņ\xadʿсǯЅΌѭѼƗʷOӴĔ˯ʎӜјi×мuΩȨ',
                                                    },
                                    },
                            {
                                        'name': 'ϸØŧϦԛҦü˰ҁß\x8c\x80ʭ[;ӷ0Ԯ#˘ĞÆΤNԢá',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ėŊǙƾΆɾѨŀŲ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʹƯҰɄѤ˨кѽ˹°ӶʻŒƐʵȽÚəϻèœ҉ϱÌɣ҄ΘɑÁŞ',
                                                                            'ÆτÇњҖĥŇɀΤËȃʮӣɮȉǞǹұņÍ\x81;ʡŹɒŉϘĒƴŕ',
                                                                            '#ɱɪĨӄЋӽƵϡ˟҆XҬǦϿІˣȮѾʹÕïǭʽžΝɉӜҲϴ',
                                                                            'ϰ˗їɜxώѺЄɡǙԩolǑɪȔJġƮñòҌΦ\x8eáĉП˺ǶɄ',
                                                                            'оҜȐЍɊĎβЁԊǙїĽƑώǺĵȬӓǐ˼ԙӭа5ԥϑŀÞεȡ',
                                                                            '´ǿBϥľȂФŷʹȽǟȒiÆƕƄÉȏԊĠѱ˔ӊĺƎɾϔDһ˾',
                                                                            'ϑŴŎ;ŻӷϩȊ\x94ˇϠéƄȓƴʺʸѭʓƗϕђƁΏʆɝŬǌ9҈',
                                                                            'ЧΛǅΤĄҚҠƂrn.ƮϾΓɏ°ãΣњûȗ\u0379ΥѹʓЎѯӚFŁ',
                                                                            'ЮӰɁ˭ԦċÓʯ˄͵˛ȣҧҟθłȀƥÊĠšӖ,vЧŁȳ\x87ηҿ',
                                                                            'ÐɃѢˬ\u0379œǼ\x8aȽu#ѩƊ²¥{ҒÜóҴ®sϒ¥Ɩˀ|Ӣƫ\x9b',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '®Ѧ\xadˠ§ǎєѤǜͶĶѰ*ȅČϮ³îӋʽî(ѓѣоɃχøɦɵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035049.817079:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҽюϹjǡ"ЙϫƱ҉îȮӧéЗŦң',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ђǑȈˏ\u0379ǫʇťɖȪéǴϱԃ˃ĉӚȼɥ\x9dƛЋ͵ЕǨЋ]ҝǎ,',
                                                    },
                                    },
                            {
                                        'name': 'ԟőĝĊAǴʘYʣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ιŲˣx\x94ԞǲŇʜӎơАºțÀΓЧԎȻ¿ƛËӈ½ȕď҄ЪћǶ',
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

            'identifier': 'ӏηϪĶń',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'УC',
                    'message': '\u0382',
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
            'name': 'ɸťϰȺӚӗϓΕȀ(ĿφυŴώӫѕśʅԜԨǽ\u038bʟ4ɐҖĉ˕ѽ',
            'error': {
                'identifier': 'ıďÑ¿ƅEĶʚ˯ӴԜÊͺԚʪümĹԌƃÑӀ\x80Ԋǅ.ԑҝ˩Į',
                'categories': [
                    'network',
                    'access-restriction',
                    'configuration',
                    'os',
                    'network',
                    'network',
                    'network',
                    'access-restriction',
                    'invalid-user-action',
                    'configuration',
                ],
                'source': 'ǩąƀƱьƈȫ.ӐɷɁΊÕОòæÊӨčуǲīǟΑӜ(ĭʉрǃ',
                'messages': [
                    {
                            'catalog': 'ҁʕϼƖӴКȾǜǲΨόłɗ5ˁ@źѪɇ\x823ЧϑźΘκАɡIк',
                            'message': 'ʄˁ\u038bӜƘɝ\x86щÆJԫŞùʘċӗǞЌȡ¢Δѡǐɼ*˅ĀĎʋĨ',
                            'arguments': [
                                        {
                                                        'name': 'ѹԚȬʢф҃ʉ\x9aƢˍ\x8aȣЂζƁ҉ˏȔǙǇϿʅȔǦųƚʽӪʫё',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɂѳxΣCƛ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΧӨ˶έӘӧПÆВÇάўȵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѻƼ/pƵϻǚŹø',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'μ\x9a҈\x8dӬɳʉ҇ŽɞӇƴζέѣξȻϝµʹʴʔŰʼ\x9e',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ą',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x98ĒʫĩrɢɢơǲǨƔԔҗÕÉďƂԞƎϲ\u0379Â˃ʦz`ȽƬɰ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6332674759558246939,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҥϥӜ<ș',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˕ǁÎ_Тź!Ɇ˼ǜƅӽĲŷʺóΖҡΟЇȁґКѰςіҎΚ˾5',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035023.716235:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '@ċʎɌˊWЖΗɘàùɒǹε˫ʚЫѼ\x93\x82кÆɂȘ$Ң\u0381]Ȱ҂',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035023.797312:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'µбĖǮĆǺŲѪ_ѯФҹıЏʓΜȜОЇ¼ĝϙΔθʗǰӷҏʇг',
                            'message': 'ԌëԪΌɻģԚ³ϼɄӕϦɖĜĬʛыцɸǇɓĊ<ɖІůȧȿɂ҉',
                            'arguments': [
                                        {
                                                        'name': 'įǽËӺҳШ¬ͽ˞śˠ«΅ҺɒČÒ҃Н',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035023.969596:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĠńԟЕ!ԉɈhѾȮǨʿɣȪïĩ\x83҆Ч',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035024.062824:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŖŗΜRϢϬǒ˧ɦƛәœ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŻȰŀǝЬųΪ(Еȷǭ˔ũБǒнǗμ˄ƖͲӇүʛǄĘǾ¶ϜƄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӛəɺǳÚϑӅυыɄÒ`KȂ\x92Ɵ÷ɤҢҳĔȱΤԇǎƱϒ)ΗǙ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳɤľǽҖ´Óǚ·Ĉ˷ѰҞϞрȓî˼ʤұǋ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņœцҘԀєӉѲӪʍЦѯʾʾАǼӬ˚ӛԀͺ+ҕѢҶǀ\x91ĸ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƋʂƉѻv%҄',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035024.446756:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'γʝŤġ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'wȶήùġĒ\x9eλνǃșЮŃԬÒԚɅӥҨˡOҲόȠϯɜѬӀĜΤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 842887.4267849661,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈɌΖˤέЪʎӣɚŌßɬ|ɘǩ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѼÂΔ\u0383Ěɤԁ҂SwЎȨξяҪȥӞƽҲĂʟĳĦȤźǉήϸŢĠ',
                            'message': 'ЩϦɕɩŀǔǛǌǊȆѤпɠȔɠʣʴƟǴϪǔüǲƪӲΟːɻρԢ',
                            'arguments': [
                                        {
                                                        'name': 'ŸԃńОΎuҏҁҵʵƙһӠÚéΫȝɅυύєş,0ȫҁĤѧƘ)',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˈˋřҬǦɪΕϺњ!ũƠԒҢξʈΦƲʥҞŘʦý\xadΓÖξ˥кĨ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽĔÂɬ˧Ɛɿê҃ˮÛԢʯŧèƔ\x92ɵȽѹȼ϶Ɵ҃ӑßϙпϔŭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȋуɊǐʒӂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3436165766149748119,
                                                                        },
                                                    },
                                        {
                                                        'name': 'џɓŃτɑʏЪΫџЦ˪ƫƏŁҪɌ·ÉҜФСʲԭȆƶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӫMҹ\x8cŷƜɟǑùɡǖɌŬđģӇûљMśԢOƒΖӓ¡йќĢϿ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'sЈƤ6ȬƕǜЬǊ¿\u0383ɓўŻԪҵɂφԘȈ¹͵ʎƏԡˇСϵψʢ',
                            'message': 'ƅɗϩшʊȲĬϷҳѱɬ#ǈϩ\xa0ƉǷ)ʡƱr\x95˻4ĲɃҞ¢ϣѬ',
                            'arguments': [
                                        {
                                                        'name': 'ʸǑ˅ΰȆJ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ãƖϯҩʼƷЖʧ˽ǭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 842946.2554249826,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͲӀүưʼЀӼӤ˾УӀѣƏԪ҄џƄўϨŎөѸ7ƀҮҏқǄSƼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÀņέσӌǦϢԞɋd\u0378κЖӤˎȢͶʃαҀYԍʐŻɀҷԥӺɋr',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʏ·¼ĳѫˣƕ]ҊʞŇΆȎ˖ÙƢȼɼӭѕzӸɷȚɲɼßɨ҄κ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɶĨʸûţϨčÂɨđѫǥӖͽЗЙ,Ŗϻμ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x96öǶzǺбđӽɲԠƐϟ\x8c˝&¢ЃόҖƈԫx®Κ"˺ȧ8ѯì',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 466441.569862767,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭŏĤΊ\u0379π×¹ӿ{āȿ¢Ť',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξСёǰœKǺÐǻеȽ±\x9aИҿгƠѕǃϓƸʢɲϲ˴˱ϩәƙɠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƥϐŴ)ÈŴӡ~ʑġ˓\x9bğӥɷ\xadɔʰΫĕΫǀĐ¿ӂʕʰʼТʸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŝɇɆƳƌÙpłɿˠîѠӽӢ"ҴĤѠԌ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҹ\u038bшîīȥōƃ9Џèѫԓ ˴íÆʐχӊǛÕęԬiļӳƆâΖ',
                            'message': 'ĸč!ǵƉ°ԍδħȱʦƱԔā\x92¾ϔӥӮɬÀˍǁĤњѴӚҀ,ü',
                            'arguments': [
                                        {
                                                        'name': 'ѰѡўÁΖӆ:Ʊɏ[ǘȺƸϭϫжԋΨӬǻʨϤFńˀ@ſӣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dďԔ\x91ƜȗǷ¶ĹюӒ\x91ńńĈ\xa0ɍƫӓŻӑˑÆŇƫLƛĳźв',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'uƘͰԤӲŊ˜ƺʗɿǰ¤ǉӜņʑʣCӧƖӦFȖίSϱțʩgƖ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћƈ½ȞȲ|ʺȂǉ<бҰԚʫүβћíĴΕςѦ˅Зcҳѹ_mȷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'C˰ǕǢ¾ΛԐŎңѐӳɞҥʺхϲʶʬÀҊ\x88åƁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 617530.5112970022,
                                                                        },
                                                    },
                                        {
                                                        'name': 'OҾ³F',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƃŘĺϮƥϥʍҮǨаѽǆěɸʺĿԉʹΫǎхˈҘГ4ʛǹӱ\\ˇ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035026.734757:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯzԨnϋύӣӼGȈĹǥҺȅĖάʼ˲·Ɋσ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҳΦÜϷöӯ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'iȭҍďCȎĝōǷΔɊң҉ħӤɋϭѰқƎҸ\xadʌ7ȠłˌРΏЏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'šɇɩƥЙ2л«ŪċʽϪQʂΩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'АˎӼƪ˗Ҳɲγёԧ҇ҊǷ˰әťǻϷМɘ¯ǔʹѕżĔҔƠªʫ',
                            'message': 'Œ9ҖӲԨўҐӑĻҡ¾ƕϜȁʑŜТϋː˩Ő\x96ӃѮÅѝ˧ˑѹɴ',
                            'arguments': [
                                        {
                                                        'name': 'һӚĥȟӂЛŔԥѐӋýШʗϲιõЋƊʺqӠɝʺӋгЀʏǚǣƥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӦӭβІεɦŇ˂ӛȋʎł϶ĺ¶',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʶ\x8cæԬԪӏѪӡʵΙ\x92ЪZ¼',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȥȲɽ\x9bɕ-ԪΘȸêƒΌƼΟʯĔϿēϟȺοЈË˒Ӡè˺ԐԀ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8602993695611853566,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƖϿбȇƼǃǀΛĂώʧμӈҹĴҸ\x9cѿЦʷ˅#\x8fĿ¹уɾмˏȇ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 747711.7808679491,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǘԪȠǺ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'НϓьĲҭʚÌʮȧԧAҙƙϝϰȂϻČȁȘȫЬўƋȿȣǩƝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035027.492144:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ъ»ƄķӻɌяřǶԧԡΩфȖţѡÀpϣˏΝϛ˕ѼƋҼТЃσũ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȳƀǞhƽKԓɿϸπĘɴӋФԍԛ4pԮҒҊˈßĴ͵Ϫûǯǿе',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѝ@ʞȑŀðÒw\x8cԠǚĕβ\x92ĺĚύyдҔŸТ˩ҘźήŝɵÒ·',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035027.738924:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '϶ȵԅȵЛȦđsԮ\x8dȬΆЂ˛ϜѪ<ɠȊˊƜƾſ\x98é¨(\x8aǺӗ',
                            'message': '·ә\xadƈƜÇӭґ«ӖǂóҰğɰ҂\x97\x8eԖΟϡʖϔ\x82ϤеLȃɖŏ',
                            'arguments': [
                                        {
                                                        'name': 'ĊĒќԄƀȩĽȐлщԩȭΉҸδɅєɺЌϿlҦĥȕӱ2ͿŊԂͰ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƃ\x99ɕ\u03a2Ƚ·ѥԡ\x98tƜþˣˬҰҞ˵ƼƇҎƌˬЊOěĲӍͳɾϔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȀͽȤŕҥӇ˱ƤlȘŗâƹҴŬ҇.ЀдʫƗĮµЫ_ʳѺƆ_ӕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ħͶϴΩƒβɠϿќǺƸћэФѦЕЛĐȆпœŶѿΐ\x854ӌʸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 372748.0275568464,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÆǶԐѐӼ\x9fĵѯ=ŦǓǙфʽҾɭâȦЩӪ&x\x8bRʶɼɰ¨Ŝİ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'фЉӉƫѝqɦ˸á1мЮċɄӸǤ\\|ҿϸǪʀǓ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɞЉƒ·ɾɽǳѮщĉäÜʠĽƔѤƴŴùşĊάͻȕĽƉǻ˲ɏ4',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x92˘҈bʵѤʕ˃яæ\x81ÀӌŬÛŝϝɃҦҏӹɲӝЙӣˬÿƳˀЧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '}ƆŮƴ}˪ԅ°ȏϰΚѓԟyŁҹȗȗӧԊӬαǢȕˠʏƦɁѿț',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǬúǪӧþÿ\x7fʳΠɤšǮϋąĲƗÿĤK\x9aɹʜqáƫӳЭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x85?ĽŸ¨˚ΗйʱҤŘ´ԀѠƬϸҙϤў¡1ΑϦə¶ŹȇŀԂĽ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': ';Ɗ҇ÖϭŃг,˦шБɎѡ;ϋ˒ŀѫʿäϤԡϊӟ-?ÍϨҸϓ',
                            'message': '˔Ҡӿ·Ȫ\x91Ǌÿ8èyġǪЊiӝǺԏůӠԧԃɄđуϙÿкŻ˳',
                            'arguments': [
                                        {
                                                        'name': 'ĀӃťӛʰďČФ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˯ӨšͷĚʷ«ӼЅЂϱƺ£bĩҨbȀѯҔ,Ҫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԭҏ½ΫΓƵďʾYĖȔʝɌю\u0378ԕĞ҇tițƥɿԠѲә©ΥѳҮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯəĊ`ιǒȞƏӤыǞ˃ЮƭȧЛƁǬ\x8dѶˉƺХÑ\x81şɒέʗϔ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˳ӭƔƜҨϗеƕχưԦǤȮɧɷЭҬ\x8fѽʃÉүŧЭ!ÙΣƙʌ(',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035029.190559:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ТÐŭʄʚισžԅɾɋЅ¤ǠɪɆӲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÏY˃',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫĹΓĺϩΰ\x93ԆϽMӸþҘʅƸȒѲҁȋǏ˧ɜŋӎ\x90ɒ˕\u0378ԙ˖',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ИƲϽNюɺǑǒԋɺϷˍϷȈXŏɖŃĜǅгȭιʔǆ/ѓƓзԏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 125259182736929376,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͷŃĲʷӴR&Μ»ȜӳŏɅϝͺȠɼӕȖԇϝϺЧǟӴː§ċàҴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӪǴСѿɕвǽǘķĔƱǼVãĹɏζˏóßÞǴϚˏ҆ʩρԟӸү',
                            'message': '¥ǣϬΓˏӵԩÄĿŷϧԫʏӜyöΠk\x91ȀČԩʙʵɽʓȋYǪɳ',
                            'arguments': [
                                        {
                                                        'name': 'ԝͺʱƱɒ҆ƚmΉǭŨ˜\x90϶˭ԃΉɂ%Œ-ԝƱɤʨӀҚ˻ʑβ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:035029.733963:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʮȅĿΑɷԅŷƞҡ:£ì˚˒ōӆҔόŖɥǎσȖΘ\u03a2ФРǭśĈ',
                            'message': 'ɢɒýȌáȚĢѰǎƬ,\x9aҸ˼ÐңμȟƓƕ˹ӷІĢƗШƶʡ˰˨',
                            'arguments': [
                                        {
                                                        'name': 'ҧĘrѮѶ8µÃƶñ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3623441452330357010,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÄǘҼǁԆŨΨҹõȮůǁǧяªǂԝͲßĶε`ˉư˅ǡ\x90ƒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ћŋғλǶ\x95Ƌ\x84˄ȿӗӼҙʁǗаŘϊƲʃͰɼÅĎͶҽiG`ι',
                                                                        },
                                                    },
                                        {
                                                        'name': 'яѶҵěͽҚЁǾ˜\x8aʢÊΤ&ɡҠÏʪҳĦӄӽӳȵҷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηǦДǻšњњĸĊӬˁđÏÐWǛɾΓǰle',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x81ıɿЧtÆǰϦҌǶӋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'łϸʁƚʎ¨ɄχФȐЊȅҕƖД˥ŻχοƠƪǨʉ^˛ǑɓƉǉΧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŷȥĸmǾ3ĈǩˊчȢ·¶Б¿Ӊ0»ӸφȐс˛ҿ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 36064.74211112439,
                                                                        },
                                                    },
                                        {
                                                        'name': 'vƴЀǦ!БԄӶ˶ÆԈƂĮҗřǻӇdųĨЂϕ҂ҞɻĠ<',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǺҗͺSԉÌ˙ΔɖЫΨӆϯӜӷʬќԎжËҞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'hЯԌәǓҪȍ"ŤϛʕȩԠΉRř',
                                                        'value': {
                                                                            '^': 'bool_list',
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

            'name': 'ʌәǈ',

            'error': {
                'identifier': 'Ԉ7īӪψ',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'Оη',
                            'message': '1',
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
            'name': 'ЊʓϚӦŀȖŒɌʻĩƷÛȻțǋǬΝҮϦɂԩơƤÕѤ;ÊƒԄ˰',
            'version': [
                -5451785537010806827,
                -8882482515143764639,
                -8273098558871913324,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ĩƸԧ',

            'version': [
                -4316444027983598218,
                -2013434534947082301,
                -596033912146800079,
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
            'event_id': 'ƱΗξʜiǶͲưç˚ʘӷγΔҲӮΔ?ǭ]ĝфЁ©Ò\x88pɖˍĘ',
            'target_id': 'Үʏӆǝ˳ǻЈϔ\x85ɑΝʭɑ˙;˽ȀƹϺǎε ԚрʛƶǢā~ӗ',
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
                    'event_id': '˫ȦɿřβĶΞŁˈ˪ǘӸĠ\x9eśԁƫůәd\u0381ąªtһЦӅÄʁý',
                    'target_id': 'ΏǤÚҸƖKŸѤËρæāӨǰРϨȷЭûƏԖkȄҕ˾pъʇ˄Ƥ',
                },
                {
                    'event_id': 'ɓGŖԣƖ\u0378ѡɆ9ɏʉȨϷʊzŉȜ\x92ҤɂҘΝ7҂oŅˍ\x88ƊϿ',
                    'target_id': 'ƕĢʼˀʄƐ6ʒпǎǔԍóÁǻбΛ˫ʕ5ȱбƳӜӛ\x9aԃĕǓϘ',
                },
                {
                    'event_id': 'ϖ\u03a2ɱҗÂĚƏąӤɐȲтǾȃəӿOұΉĀϯȈĖĂӏљ\x96ĆŌɇ',
                    'target_id': 'Ă\u038dƾүΐ7Ϸëе΄ЩЖįК·\x8bӄƿЁȉӑȗ\x9eϱ¥˺ҀӵŸʨ',
                },
                {
                    'event_id': 'ӭͰʆѓѓˋɘȕФɸƚǜϚҩ{d \u0383ԁǺ҅ǄҞǣҲʹщǔʋȽ',
                    'target_id': 'âύŲľˣɪϋŷǈЛҷә´Ʋɠųͼӂʄ\x9cǰхς}ɠ\x9cǽѝȹˑ',
                },
                {
                    'event_id': '˩ˇǫЁǅVιϙԜr#\x89\x97ϒƟìЕϊɖǄԐ\x94ϐӽȃʨԚӯ4ͱ',
                    'target_id': 'ĴʮʦқΏŗŅчɞĳɶL˟řңԘϓНљʅԎņzǧԅӦʬǊєѐ',
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
                    'event_id': 'ĖǳďДӖӹφȼҝáМĦӟÉǮҼЯǻҭӁɳǰ@ѾīȨ\x83ԄŌÖ',
                    'target_id': 'бԓ˵вΙZƣłҍʌԏȔГçӹ˴ǢҩӶ\x94ќ?ʷˬłѥϢɂиʿ',
                },
                {
                    'event_id': 'ŊԜã|ȓǣѮQȈԇ\x98ʊ˂Ř҃ѭųȜ¾ŲқòƮҗьõ\x8aLȈb',
                    'target_id': 'ыєӬʺɰcɋԇǕ6ӣӬ\x83ƔΟѳĴ®ȞģӧΠ҃ŞҟƆ2ƘϔӪ',
                },
                {
                    'event_id': "ÜχɮΈˋϊЛ˷í0ʱß'Þ˜ϮlșѸηˇ}όɂςÐˢƴʵҹ",
                    'target_id': 'ŸԖϊΔӅүɥϲĘӸΜΐşɌƃŵϷģȒζȸԪʶɯɟƒǱ´ТΩ',
                },
                {
                    'event_id': 'ǋɎͻƞҕ\x99-ϾǑҡ¼ёʙȠ˔ɽύˢѶ÷Ͻ˧ʗҕҖŹұòŏˢ',
                    'target_id': 'ŬƮԛϴМĜѦĮģύ^ͽ˚\x8aЦԈ\x90ǉǺϓÎǞњȝ˰İχ˺Őж',
                },
                {
                    'event_id': 'ϚñμрƇԕʋӽ\u038bЌȏЈͰіČϗ˼ҮôʯʫƸƉӳӀǘәïѸЭ',
                    'target_id': 'ÆɷʙΖΝʩƝĞǾђǑƜҦǶпξҾɽJ\x9d}ǽԥȏƎɮɓӳɝˣ',
                },
                {
                    'event_id': 'ԈΞϝѮƃǫʙнĜʨЛ\x98ŧŐҐɮӱӓԃѥјΝԚѱŸÐƔǔőƽ',
                    'target_id': 'τӭFʀĊr҆ʡȂŻθ˾ДҧßӄҠÅ&˵cӍĬΆèƖɰ\x8dϞѓ',
                },
                {
                    'event_id': 'ǐПÝӈвñΖэxɞ§¡ӹäʯм|ʭ\x7fɵʜҁčʽďϙʡɹӹɅ',
                    'target_id': 'ƥʈFԫĊ;ƃЗʖßnҪȂɫ¾BʟȝÎƭ˰ԌӺj˘ƤŻϜҬχ',
                },
                {
                    'event_id': 'ϼˇȷʖȉnӷӪϯԣӨxεțāƫɎǊЖóȯ˹ĜЋ\u0382ȆѢɄŹ˦',
                    'target_id': 'ƭϾӮζʤQǶ-ƍˑǥɖώgӬӧǩƑмЭɭʺ ůȩ`æ»ÇϹ',
                },
                {
                    'event_id': 'ϬЄÇЦ˯ѢԬƖљʜƼҝыˉϴʜϬŎзҲŐxԗҍĳƂГȗЮǽ',
                    'target_id': 'ŨĆԒДæҦȻċckΩΨUŦɂ˵ѮıԈńԛгыɖɾɌҟԎƁ\u0379',
                },
                {
                    'event_id': '҇ϜįƫПЧtӮ´мɎÑҊуϔ\x99\x845¡ˊ¢ӡђґљʤȧŌӛŋ',
                    'target_id': 'ƊƱƉʏ˹Йӯ×ҝҙ·Ł@pͲʫħǌЛϲˋШϿƇҽӍƪgˈǠ',
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
            'name': 'ЫʗŧʍȘЦ\x93ʏЯb¬ȄøњȑűˌԞТȒ˴ʉ=ҫ#ΐFµˮϔ',
            'version': [
                -9009821608957249546,
                -8827650442191496800,
                -5685736158267605343,
            ],
            'about': 'ӰԭȆã{ΗÝУʿӫЮӟĪ³ϵhԇĢşӏɦĮ1ԄԧǑύǭʊŃ',
            'description': 'ŶӄҥɊʸʜˈʦŤɵʼΞЂԬЎáƠʅȢxǷӫӽǦ˽Ǡwĳ˗ң',
            'authors': [
                'ǔ!Н',
                'òζрĳϰ¶Ӥȩ\x95ş$ҲԣȍϤϼԖĄ\x96ѫαқʆɩ\x85˦Ӎ\x81Ɨç',
                'ɚı\u0383ɔґk\x85ˍӘш¬įύȷõѫ˱F˽˗ϠϋĠ8вȷȑɯƢĤ',
                'ɴҫŧ¤ŗĊǞύˡÖʚĝˈˬ˔Ù£ʚ\x8fĻЀԞȇѥІϠвƵ Ŕ',
                'ӰdˣĞӿȚӇ\x99ϕӂ>ґύʞ\x96ȅȱԔӧԀӅǝӺϝвŹωȞȯў',
                'ËIÁūҏȲОŌӖ˕ͳʋȷĪ\x9f£ѴӒũʬΩÜƟ\x8ež\x89Ĵ҂ңӼ',
                'ЬјѢЖїϒĀ7ҨжoȍʣϱƯíƈĸϛƸѐ҈\x81Ԟˊʁί9ѺĂ',
                'Ùϴ\x95˂Ȗ˹˅˖ʭ\x99ωӵ',
                '£ĲƪσǩΆƄ\x95ӹ\x85¨όҘŜǂçFƚʁѭ\x9fфʡĖATɭŁПӌ',
                'ƱӼƇɮ҈Ұ\x97ŰҳȦˎ"ѬӂҟǐӅӚИΚǙҶKѴĕӃǰǻѵĎ',
            ],
            'licenses': [
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӏŃĨ',

            'version': [
                -1154940940872003778,
                -667599179957797439,
                -6473063547134572337,
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
                    'name': 'ҋʯѺ¤;ʺǶĠԀϥǪ\x87Û\x8aˉžƨ϶jˢҏǍəvЈ҅ϨʇҦĊ',
                    'version': [
                            -3918177750901523066,
                            -1187720204933291289,
                            -8230491174289289173,
                        ],
                    'about': "ЮƼҥǦȥѺjдÐÓǞýƙӶƾώ'ʈƱuΙЅȦƿʚƲşʸǑϭ",
                    'description': '˛ˡ\x97ĀϻϲɪԩĚØėϗәȚw˅эаʉƽʶǹÀƪʌppԛƞļ',
                    'authors': [
                            'ҲκҥȤƑkÖâƌơǨǵӠʇƤӹǃƕ¡ɧӭё',
                            'ˈʚ˧kĘҔӤˌ¢ԔƩɾΙƑпӑƓЙϣѯƁˋоѹњĀȔȵϪʽ',
                            '҂ԀəнlӊҚэѓӼΪƙɐUсɺȓ\x97ɵϼǅ\x8eȀϡĳUæ\x9d҈ԇ',
                            'ʡ.г҆Ѵˁ}ɣƜŐΏӃġŭʒǨΟƑˬUҼҗǜyȁñȅӘġȢ',
                            'ϳȐʾѩϼІƹɒŪɚŬʖ$Ͻư£ĩȺʻɶʸF\u038dҳǔǧģʾşό',
                            '҉ɓҏǱŻԖцӟƻǠ\x85gӶґbÛgƈԑиoӜɶ3]ħЕ;Ħŷ',
                            'ώщvǎӞ¶ƌʍ\x90Ǫ˓îŶɎ"ƄԮ\u038bþέȇǚӥќеɠΉŉтǹ',
                            'Ïҽ',
                            'ĒȬ¤ǢψΓσɼ\x9eɷԝœǞ~ǣǝҘƼхIϬ\x90ΗȆѷoțϗѓƭ',
                            'ęĿŶїϺ\x87ʠäc@΅ˊєхǨƋґǜɢɉdĔ˘ӀǶϪɭїÓˌ',
                        ],
                    'licenses': [
                            'ԩДƸ\x95ȭҙĎǠ\u03a2ЙȎцN҉ďŽMϿòțǄŬΓųГɟƽ³ËӮ',
                            'ƂƅǘϋϚϩƇ8πğʕŢҲƱңǅɸʉӗ˼˄\x96õÓάω˓U҄Ϊ',
                            '±Ɯʟȹʲ\x98уÓԗ©ԋӎΪԅΪˠиӽɼʠ˨ɞʯʌϕφǡŋ˴ɟ',
                            'Ү\u038dʇÏԛ˒\x80ȨĐ˟\x86ƘӮǑŴεϺvɉņǢ1ϓϺǾҦ©s˺Є',
                            'ʅŻ ӮπUͺÀˋŌ®Иĺʡ¹´бԋ\x87ҬгРЇѯ˘ǭůǽοŹ',
                        ],
                },
                {
                    'name': 'ôsĄдÏĢŗӹØrΌ[L\x8dХЫúȘͱŝɦ˯ȈǬɍûΕϘҥή',
                    'version': [
                            -1435033332126736621,
                            -5589685050785428116,
                            -4662219357956324111,
                        ],
                    'about': 'ĵˏȉȰɐÂΎͰȋЧƟƲȷʖζӤ˲ΔʙdȗρˡҼёǂȮ*ŀΈ',
                    'description': 'į˝\x82×ƕŵϣƺŜϭĢƾԧ¼ÃǱȖӛӸҪȿԙđęôř=´ç˫',
                    'authors': [
                            'Ϟŷ)r\u0383ʒԤҟЛĺŚӌyő˅зќҪ;ǦΐfОțƌȪʬȫаυ',
                            'ŖĪϔʸЖǀøèʺƶыϙέа¤ŗǧ˧ϫīǧùƦÇĻԗƄþɭ*',
                            'Ɗ\x90ĂϤͻʭȡůΑƌǨɅȶʉäȕlЫҟůaӁĺɅʝ^çȶ·ԍ',
                            'gӟƌȫʨ¨Ɯơэϼϧ\x9fϺèёԔɋѕɋ&фŠĊƋҿʮȋбöљ',
                            'χ˓ɏzфκĹƠΝΆÏ˓МξҔÃ˶ϾűƊɌ\x9fƚɂ£ǣXԇϺ˝',
                            'ͱРŎUɈȴ\x99ͶÖÊĕĠʌӔĊιȦЖӆƻǺãΞҁΛȌЮґÔϣ',
                            'ҁ҅ƬĽзԍ\x8aźÍčѣŴѤ˩јWϲXƌуЃƘȤҏǔĽaоĠå',
                            'ċ͵һũ@LһόͿʁʺü\x92ɛњϹѩƇǊȪñɏϵƈʊȫ:yкΉ',
                            'ΨӤƢ·\u038dԂңľԉѸ>яǒ˚ȚгȠʦ}kĵС\u0378¯ӞѽȚĘˠɏ',
                            'ƛɮͲ˙ҩѝɁç\\Ԓ°vϐӀʒҜÜƒΛĜѴ\x83ԃƭΪϟ ЄƬϲ',
                        ],
                    'licenses': [
                            'ʠ҅ʥЬɚ²Øʝ\x85ѹĠbʥáɿԚ҈ҲǇȍPӛОɔæǭѓŻʰÄ',
                            'Ș\x97ŪȌԮˑȐĵҖ\x9dĆƛȌäΕ\x82ȲűtӠΓäӚ,ƁԐαƖĺϸ',
                            'uǧҹ½Ÿ)ҴvϾnњѡѭǠƏAԄǥЂʡ҃ѯƛ°ϊƮĽʈ%ə',
                            'ĭ«ƹ÷Ćʎ҈iǄƛ/Ͱ˱ɧѣӅ[Ű˻gƀøˣЪƱĉˉԎɈӶ',
                            'ŁѲɷǂДǖҖȀҹŧҢіΈ«уßҳ,+Tʋ@ǜǄÊРʪѝ҄ǲ',
                            'ӫ҅үƨŎƻȺŭƿ\x89\x8f"ƠӂDŻɼʛWϓ˚áЩ¸ο¯Ϧʪ;ӡ',
                            'ϔʵƶϼõϝҌĀŊȿŋО*әÓȳƞƪʎɞ΅¬ʟϽÌύϩǈґŴ',
                            'ѳɀȀуϤϝǊȳ\x9eGԑşϻΧkGԝЖǘƊʾvŖµνơƴɷЈѐ',
                            '@ƼʔōѠɻˇѹȳӋɊǞ΅ɀ<˧яϫҎԋŊª×ʏÝϑӵѧƉȮ',
                        ],
                },
                {
                    'name': 'D˽ɨZƯІɢWȿԢ˙ЭМԥĒϩѭѽԢΖƂԎԛÌӛ',
                    'version': [
                            -6399297832344306557,
                            -3256946312133016690,
                            -1790503433215766149,
                        ],
                    'about': 'ԎɇzʖϏĪÛѷťnEΛρϭŏӥɝƾҘ·HşҕĤ)âƴϏ¶λ',
                    'description': 'ƠϚƙÔŴɟ^˼˪ŏÊUθGԩшȬķӲԤŒ¥ɰÁÊʹӻȜѰŪ',
                    'authors': [
                            'nȲğɋFʖȅĜ҆ʳɒ\x92ƳƔȥ\u038dǟŌΎ$ʉк.ǸʆƳͿԟVȎ',
                            '-њӇΧýǅϡҞb˚&ȃƍʑȒΰŘǚàǢ¾Ĕ2ǔԠѸѓ)ˊʺ',
                            'ŮӁξϝҧɥĳĨŦʑϏЯҼƼМҥ©ö\\`ʮƋҦȎЀ\x9bϲʓɇӓ',
                            'БĐŋ7ЌȡɬpϱúҨʔƯʓϽϭ΄ɴζ\x86Ē҅ʑĕdƿƠҩ/Ή',
                            'ԀӨΘǫϔƥʆĀјhԦԅTԜПÚ¾ԫwÌԑυ˙ɩΑЯüŇȻ\x9f',
                            'Ǎ;B¼ӯȪѣFĞҢȔҳԕðЫӥө»ŁƦʨ_ÞπʝѤϪζпӞ',
                            'ўȨŔðë\x85άɪӳþʟǛӕóԫž\x7fǏĲǰΎΞ^βȵЪ˗ғκ˪',
                            'ћɤҵʬљЯԌВӵ\x8b+ȖɜÂɊpĩДβѐȓŌϸjǸĈѺɞзѠ',
                            'ȇʧǫΤjϓЀɉ˙»ҨʐԖΥŘУиӿ92ѭӛƼ\x94ɂıvÉЊΉ',
                            'ɢΚˤ´üҊB\x9aҬΔɦ9ҍʰ\u0379І>ĿɨõӿRϲÛͻΊʧƬ\x93č',
                        ],
                    'licenses': [
                            '2ÜԠБʥĤѶИҤɺ\x86ǼϜηɥ\x95eҘʔϴġɚӡĽªԧѢȗÄѼ',
                            'āƱɴӢȖƼqԚƫϏ}ʹ#ǞRѽяÓЃµϗȂЫԝɟοʆʽ˨(',
                            'үˊӌІӵӥŰȱΟ\x95ҚЯAǇǮыƮ\u03a2όрïö¬ȍȢrӌɋöǻ',
                        ],
                },
                {
                    'name': 'ĆȘǩɀƘĬɆƍȁƅʽϜ˒ƦϘǖɗĤќșҰϼĄͿŲƴҊɧŜǋ',
                    'version': [
                            -180937246766248575,
                            -3873421530233885509,
                            -4708935558354013439,
                        ],
                    'about': '¶ʿЪ\x9eɱэȭȀʋӹϙСôўɍѹʿЛäȴˤ½ʔĭYʫиɦēE',
                    'description': 'ҬʴϹČұȟѻӧЬӜÈDǛ(ɯ>ӐҒăÂȤ҃ΕϰȂȥǤϺĤС',
                    'authors': [
                            'ѓɭԮĹ˻ԧʕҟǞΞȿǜǃɑϦлԘÆǮ\x8aơӚːƭƀŦĆźȎ-',
                            'Єʴ]ʠҺ\x87%Яģ\x8aǿȦӮ҃ΊBӜαԖɅʭҔѴµʀˮγή¥Ѻ',
                            'ԡҪĠVӹƸȌǺӲĘϓǱʀŷ»͵әɩǆǫ',
                            'дȶ3ǖЬ°ŴӟƁ,Ş',
                            ',ɝ`ʗȸΠкƪҎӥŪĸȩ˖\u0379 Ѽȍ0+Ëӵ˅ɣŎԓК˺īɞ',
                            'ɻӨҝƅʃӉѪӑƌŠƞҼĵНο`ÔԟǵЋϰìӯNτΐɉΰĜĦ',
                            '\x9bŹώȚǖmɄЧʰԚȞҘǥ[ĲˠΚβˎџɦ©Ɵĸżйԩ˟ʋD',
                        ],
                    'licenses': [
                            'ƅː˕ȫӘ҇БӿҁzӐβάХѲɺÚм˸Ғ«ξ~ӣӪǐВЋҹǠ',
                            'Ȉ\x9eΗ?ΙЗˮԅq˂ЦȂơђрўѼʊζðӑ\x99ƃġƱӼƛӽң˸',
                            'ԟІс#\x9bҮǜ;Ć\u038bϤґƑ˒ɃЇʳϚҳł9Ԁ\x92ҎˀǱ\x8aӁǝϹ',
                            "Ŏ\u03a2lÑˌ'Е\u0382˶ǾҁƌȀŕʋůˮϊӲЫvғpЁұ҄б\x97ɟΫ",
                            'ҽҤő\u0378҈žȌĩԗĵȿǩʾӶϞ¹RʛѪɝ&ȋӋϡɣʚƞ˨Лʓ',
                            'ăǦǔČɺƥώγҜΓƘŊǀӰaȦ^ß¦ήĝ2=\x8dɩˤдȕѨǻ',
                            'ǤϙɑƣԁžӘʡǶɘƦ\x81Þ¤GþЋʳϳʙƍƃ\x9c~ŞĴɋҸɸǶ',
                        ],
                },
                {
                    'name': 'А»ϓˈÜ҃ȶЕºȍȺ`ѳʶʫʥ¢ˈͰƊ¸ͳŮȧƛρ˱oзʳ',
                    'version': [
                            -551006550945216044,
                            -8011350235602467933,
                            -2362925848325988982,
                        ],
                    'about': '˳ċ҄ωWªťYĥTҧϮȌ˦ɄϮɹʐȼδģʾϲěҼϿӃÉ\x9cş',
                    'description': 'ȺɸǋʤΌωѐ¦žɍҿˢѾŪӜ5OžЉuѣ˜\u0381ˎРԀQôϲA',
                    'authors': [
                            'ɈҠΖɈÂ\x85ТɔԬÛØЭǴ ϼļǐƳκÆȉΧѾŀïʗÍÕξƊ',
                            'ɁǰJƦϦӫӭ¾Ϊ½ӋȬɻū[ƉӥӲȰèϥϐԆ҃ǀ\x96ǖ¿ϧǳ',
                            'ǌΥɋʃɋѩȐо@ĖӖƜьƇn˭ȕƵƀχҒѩѫӕãȴ΄úǯ\x96',
                            'ʐ҂T_',
                            'ȩεķЏСċѤBǘјӕѿŦ\x9cЈĕәԞîĔƁΟΚ=ҾÑЌ˟ȣȜ',
                            'ˍʣi\x89ŋӂьѴƈ\x84ɛǨϒŞ/ґΐѾˢĹÄȉÏˠVŢϺÔɅǯ',
                            'ԘΓƑѐȠoʮϪ#\u0379ˏɤɷǿéƇҍ2ӫIYɧӨѶǆýOҞš|',
                            'ԏŅȩΠċǪӼĥÐӉʫˮȒYЮƍŮΗşϡцżʶŦƧÌǬWOȖ',
                            'ԘϺɻƪˍʹɱɾӢ¼ѿÓЏ}ľ\x7fÈÃŧåΆϮĺǕʄˁ˛˪ǝ\x82',
                            "ƖȬϙϽ¸ϯ\x9cӒΒˊԥÝVǾѩѩϫ҈ǵɉϢ'æʫE͵ЇƋ˽ʑ",
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': '¯Чǡȫɦĭ҂ӓɜ\x95əʷɴԉɮÄΖŌÃȝGăŦǛˏðЩɅѩǰ',
                    'version': [
                            -1027834329581275928,
                            -5657574226918031419,
                            -1802759635832119650,
                        ],
                    'about': '"ӡҩǩЁ˼ԊӲИǬ´Тϒ0ƲłɪĦȼ\u038dÒţϗПǴȅӊC˅',
                    'description': 'ҼӊʿЄϛƫӶ\u0378ƲϖҪʱɼŰǓȇBѽƈϿ.ǹŶԞʃ˂ÆưГӏ',
                    'authors': [
                            'ҰɍƾPɎԖ\x82ǂ˻Ƈ=ȑ˙ɗȰʬǥЪȋҺ˲˩ɡɥǿEđϹĖӖ',
                            'ŪѰ\x87ДқȘϸϾцƤԖȚЭǨϏ\x97ť-;ǵԍѰĊ˙ÝǐĶӒɫŘ',
                            'Ђ˶λҀŲƻнƥéƕѮжиєŅˣ˰ʴĥíô¨+ϽĖ®Ю/ͿJ',
                            'GȫƂ]ɃâĲôƱ±ŭȷHʍ˰ўʦ\x88ǿ˹ľǷĮγЀӆɳȤ\x96Ή',
                            'ťD˝ΨǑĐǩÓϪѹÜͺ¬ĸƆėԧțŠλŹ˲ҞĕьÙćΧȤŤ',
                            'ÒĞɎÕkEʛƢϢӤÊҳ\x90ÒШÎћѻϘӖ+ưθŉ\xadѫϝͰԨй',
                            'ӦûԎϿπŬӳʼЩī1ҨƱŭƐӳ˸іΥӝ҅һ£ZʴȒǍlӎǡ',
                            '˦ә2ϫÇԊӷÒɿҔ҈ӶĞɤʥƛƹƮХΒ\u0380ɋŇѸϤϺƚЏƫƪ',
                            'ˑį!˙nɨӨѷʻΝƴϝoψˮϪђѡӟǳƚԆɏԛʏϹԋ\x9bԃҼ',
                            'ϒӛӎȇI}ЫЇʽǯGԢ\x98Ⱥъь>ˇΧΎ\x8bͼŸ»ƍƚ\x97_ǗБ',
                        ],
                    'licenses': [
                            'ɕˢɃʘʻπҴȃǖ>˭єŞǒƑβΉˊJГэйė¹ũӅϪЯσŖ',
                            'њƬºАƽ\x87',
                            'ќяЯуӎbӬʿЀ1[ԩӗ˒ĭʟťƭƴƠњѷßͳʣӭĒτѸЕ',
                            'ΔŕώбҰϊƅйνϢнȧǌFеǆǼ\x91ƶгĵð˘\x8aƟʭӡȷāɯ',
                            'ǭʯʀ1ĪɁόԆ¡ēƖг˔lǏȑéŜʖѓǅќñPǚԐΎšʫǾ',
                        ],
                },
                {
                    'name': '\u03a2ŧ\x83ʬ\u0383ï]ҡԆλЙϞƇԦҚҴ÷ƂҊ˒ŉ͵ʟȊϟZÂȨһŋ',
                    'version': [
                            -5449937142350341836,
                            -6166333328410756051,
                            -588510019928937567,
                        ],
                    'about': 'ұƐԡαԂψʍϾсβԆPШ=Δ3˯ĲҪйČ˂ɫѤøtθ\xa0Wɏ',
                    'description': 'Jʫw˅Ӌ©ˣţĦͷҐ˭ɄGдɻҩѦМЛĜ˙\x80ѾFưƊɕԁϚ',
                    'authors': [
                            'ҠѭʥǇ÷ĿĬѾǿʾƴРÆϿɃµʥ\x92ҾͽʾώǾϊÞЗԘȅ®Ƞ',
                            '\xa0Ȋ{п\x95ſɑıӇρТԜӸԣʯXĶ˃ǲ˒ϐ˳Ȏŭǧ˚ԋʕƁˮ',
                            "6҆ϕϳ\x81ǰԙƍ\x88ſƗ\x80ĪдƆþґé˄£1ǂũэӑ˔ƻѹò'",
                            'xȏӄѳ\x951ϦƶCʊǱŵҊȳа\x97ŏƬԉ9ιҨľәsKʻоï×',
                            'ŖӭyӇTȖȻŬˡїżϛıλUѩĽØѨԦĨѪȹ:δɠӤȗҀǋ',
                            'џǫ!шѪ¿ͰҰůǽȼVҤɟʰ±ɨ˂νƬȂǬҽ=ɡƯΛѫƹï',
                            'ƥЕÙϹѦΧƁùŬĶϓoƗsþӻˉЁʤβʉ¯ʑҥσċu\x82ĈǢ',
                            'ĭͽ\xa0ԉøɴԅҗŷΚɽɿŗ¹ʰ˧ȫӢʞŲǟÆ˥ԈԖŤʅ\x86ŝϐ',
                            'ԃĩΕ~Î\x83ƾИˏϫČƇ\x83ʐǜυξτÆʔҌʼ˥ǳӽĭžӟȞΚ',
                            '҄¼ţɊӚĨҚέ-Ē҄ã˔ȘԂʏƐʐӞɘƸʈyʟúǈΦȺμӝ',
                        ],
                    'licenses': [
                            '@ђҲʿíρԚҰŘŐȞɟы\x9fѹґƔʅ˳єКɞŨǾːǓ\x99˯Ŷʺ',
                            'ԢЋ\x94ӺηНSɇѸѡǗɗ\u03a2ː;ˆˍaǕŸқƣǾyһё˗˳ίЅ',
                            'YΣá\x9fĹͰϛʁϼŝΕĂω\x87ͶǩĢ˴ÎÇԅɊńöŵ\x88xɱ˸\x8f',
                            'ȑʯŌrńΟŕҞŁȏƛԛǊϋѢЊ\x89Ң\xadǀԔgҕјΤԠҞ\x95Ôͽ',
                            'ƼԜчǌӵϬѺ˲ȟȴýԤƚOëĊˠ¼ȾƗȘЦĦĺʀæԉǚͱÚ',
                        ],
                },
                {
                    'name': 'ҾȑгϷƙȥȻԖϐ҄\x9cӦΙ҉ЃĥɃȃνǅȒǄζŎ¸kơӥƄΜ',
                    'version': [
                            -1167439640941926567,
                            -6022065016653013562,
                            -1516098165161736237,
                        ],
                    'about': 'гŃǷԤþΠȴлĆʲ҈ѶԗȱЃȫǎΆƎŀқİƩѩ¡ұŬƦȩϭ',
                    'description': 'ѨúїнԅЭϮԨɻϕͻPƓɩʱ-ĒҒѫԙ\x9fљʳʺƳĬǀeȳ˦',
                    'authors': [
                            '~7ϒɼ¡љžұЁӃΦ˜ǒƃĒ:HɳȺǍéЍҤšȑ"R\x98ųƤ',
                            'ҢɨĘąɼЅӶїѿӫ˒ԋo\x8fӸƴтѲγԋ˟ѐÞƥƃɟǜǟ\x87я',
                            'ǰǪϾ˗\u038dЄͷϏɹʥЌƃѿļͿѼϹǥԔѫѢŅШσǨљ:Хкѭ',
                            'ЁΛԒǚ ēĸŭϜ\x88ǶʫKƬγԓƛσ',
                            '6ϪĘԄ\x9fąǗ¡SӐɖώƾ#ίŸnʡ˝ќѦʀӢCŗǶlÆǴˁ',
                            'ұċяѸЂǚұǗąƽϟĀş\x93ÕȜų҅ҔyhѩÝʊĵ]ʚʸ\u0381\x8b',
                            'ȅʕȵԨǜЗɎƿӱ˷ԍϑƆýùїȳŠ\x8dҼϠʦЖѴκ˨ӫJrq',
                            'ѺĵΘ\x8eˊѢʏӹȴҮ¤çʓѦ¥ӓ\x87ӺАå\x8fϣŊΖĩӡЛťԦʊ',
                            'цʗӏӷʬЊζђ˄ɫΡνėĉƤ%£ÿȜŬźɂŮŜϫϲFгĞ\x88',
                            'ƊBȲýΪŵӊâҩʓÇɔÄљƅԧ9Ϥ˓ø;Č¯ƁͽҤ¨Ϣ\x8df',
                        ],
                    'licenses': [
                            '\u0379ԠÚğ£ʄϮοȫǼ˄',
                            'pФǙ6˔ÊʺɌɈ\xa0ʏӾ|ɬÊѲɲӛÊ&К˷ȊȊԔɼǀƐɧŵ',
                            'MƃLØӛиη\x93ʄϵѠϨӋϟЩ³ǊӅӯ',
                            '¸ǱˣΤӪƆʪӹЄϫħʡĄҷʱ҄ǯѮĚ˵ʂč˺θ\u0379ȶҿЂƍ˸',
                            'ȡ\x9dēγPňÌйΨĦĔӅӃȺЛʲ;ÏҢӌpʝЦΞːƊфҩģӄ',
                            'ǎӐӲħ.Ԡɪ;\x82ъčїřјі҂ƛÂƷˌȤǄѽζѮԫŗǀŊ¤',
                            'ԩµФϚOХѿ˸Љ҆bˌɛ˂ԤϿɎ`ɇΈóԮƐ˦½ ʜĖ˾Ë',
                            'ƘɟǰǜЁ˭ӷ',
                        ],
                },
                {
                    'name': 'ƭ˜ӜϩφƞζȂʀȃʅ|Ī\x7fҺϰͳѨđώʪˈӻΙĲɁǵɵ˄\x9e',
                    'version': [
                            -5362128220418459155,
                            -6529429767090694466,
                            -2421205962746443887,
                        ],
                    'about': '',
                    'description': 'zşǴů²Ҵˆʱ\x94ˁȮź˅ůÅѥΙϓ\u0381ќ]ɽŀýҲ˥ƬƋŁǬ',
                    'authors': [
                            'AŤźӀѿňƈʫ҆@ĖӇ>ªΐʎQңJɢǇÑª˭ȨǝҝǜШʕ',
                            'gͳ\x98Ҋ҄ѣQԚŐBγМʴȿɓĵk}ӶǛѠ˹п҈ÂΚʞȐƭf',
                            'YĔǜӮή\x88ҙ\u0378Ӎһ\x98Ԙ\x8dƿϐèӮėþǶȸϴƮ\x9cΪКɥĔęT',
                            'ɵηʿ½ӘԘ;ˆͰ˸ĩȮΐËĎѤ,ɈΆňǇ[ъ ѦԡђĽɖǚ',
                            '~ѣ1КВÎԄͷʶȸюɮ˞˔ʦ\x98ʨŉĪå͵ΨǋÙÍÖƋʉӨȤ',
                            'ӛȎѤʾ˥ßª˛ϦҹщʫųϚȂɒěϷĤģЏʑƨÞȅK&Ϫʢό',
                            '¦чΧ˂Ҡ\x9fˉ҅үɷǵǝŰkǎĪƃҟφȖʌѶĈҖҴ\u0378τд˘˄',
                            'Ί˭\x7fҋӊͻŐΥӦȳϞѷʔǠƀĊŧΌǦ˨ШҾШưԢȼςǰŌȦ',
                            'ëӄʖӓјϯ\x95ɾóϹµGѫгБɹΨԖ˟ŏγɮѮȠФʇġѬЯ\x93',
                            'ʗ\x8cԡĆҩÏҦΎԋƙ΅ƒˣÔΆ˞ϻщҾĺɮƒ¡ƔАёřʉѴϕ',
                        ],
                    'licenses': [
                            'ǂƑ˽ϝKãâӔ',
                            '\x8e;҇āʣǢѹΝʋϯ¿ԈȆʭРùԖҌƼˮԛȗӵĒчȒ\x82˴ӸϽ',
                            'ǐ˴ӡўCɝº§Ⱦª*ωӇЂӠԉϣĎ˻¼˻έĆiһ\x84ϿŇîÓ',
                        ],
                },
                {
                    'name': 'ϽυǸ҄ʐƇdȐlӨÏӶВѬӉԗȭB\x96ǹŵӈs\x87ЃБǙmȓϭ',
                    'version': [
                            -8001387718209306501,
                            -6834833880673053393,
                            -6759373071545645019,
                        ],
                    'about': 'іɡˊˊ˨ӭʿŇΎѮ¶ȬÅ\x81ѠԋØ2æγаЎɇȧþӋӊʚŀк',
                    'description': 'ȠсДŕ\x80λ/˰Щéў}ԍҐЀʰԩϴɧāӟͱŔ\x9aϿ\x97ěŅәҩ',
                    'authors': [
                            'ˉԔ ĕ\x97rġ˕ҁʴȌӹ+ҤԔPǑχɨǉͶʻûĭ˭ʰ¾˫Ǽđ',
                            'ĉ±εӲɅ_ұӴȕJʿɫ\x84ƀϲЃıԩ\x8f]Ϫ^[ňԒЧԒɈŵѣ',
                            'ƹΔԢnӪЅɜѝԙȷǍǭY˛ќӓΑÄԊ\x92ǜƕԬ΄ҫĜɘŐȪщ',
                            'Ō@ǔԮȩé΅ĎÅͷPɾʷңґşĳˈsҵѫƵ\x9cΎϖЬ,ӌʋҎ',
                            'Ėŷ\x9b5ǁÕuuɧѝrԗʢωКҢaɻМХɾȬқť\x82\x90\u038dҶӶʠ',
                            'ÈЌ,Ԧ±ԦӛғƟȝέ*Ѵ_ĒфǊƀ\x94œӱzǨɌ<\x81ġʴÈǯ',
                            'º¢lʖΗѬȩϰ˒κӐҹԫԎӎɸĞĺɫЍʂ»юӼőŋЌRfӉ',
                            '\x92?ƶӟŚЄ¤ǵԓӔԛҚʻqцΈϳʾŀʩǋƤȊǇϘơŉ˄Щǆ',
                            'ĨϓɾԁMѫтȵ˸ĹΩԐńԉǐƀɪ^ˉ¾Ŕν;ѢҸӅʝįɷɦ',
                            'ɂ˖ͳѦƛȼîȰƱʾÊπȲɏМ`кϨɧόʖĔӝɞЙЂŐϫһɺ',
                        ],
                    'licenses': [
                            '´½˨ǴҤĦȹȵӒƣ¤pΔǅǪi°˳ɍû˃ҌKοĲƼņǛ?с',
                            'ǻˀƨʋƉũΚēƋһԢΥǒƷЗԢġмΞ˯<ǿӿ´˙ϸΪ<ϗ\x90',
                            'ǚΠЋǽĔð+ħЊŤ<цзΤǨϘΆǇϹÐŲäɱșȾԐƋΛˑȗ',
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
                    'name': 'ɶґŁ',
                    'version': [
                            -1147086469490627738,
                            -6399518844945043801,
                            -8469923590189099880,
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
