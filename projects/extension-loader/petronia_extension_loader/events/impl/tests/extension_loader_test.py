# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-11T17:55:39.500880+00:00

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
            'name': '\x81S7˅Ӹ˙ɲѣɚÄәøȹѰ\x93ɝŖǐè³ƵɮηўΦʹŧȰǅӣ',
            'minimum_version': [
                -240395050086188870,
                -4303000442751043920,
                -8229160336351376357,
            ],
            'below_version': [
                -5055752332246350357,
                -8318805497939652335,
                -7403056642038966574,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ǥyӊ',

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
            '$': "\x8eĴõԥnɘӱ{ыɵƙѬӔÙ'Ӏб\x90Ĵ=ϷƒƲúƯέϚΐΔû",
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -7548803458245236171,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 213977.4186631121,
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
            '$': '20210211:175539.411134:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ɵDʶԧǯa\\ӄϾ|9ԉǩɁХʣ,ƳˤѺǧĢѰłΚέ`±Īъ',
                'ԝŗYÎ҈ԤǟÖʥ\x95ŀ҃ɜӅ¹ʆπ@ţԏԑãǸĥŤǓΕMűʒ',
                'ˤʅũˉ˕ȤϧщİʥĂμWβˬ[˽ґԦƷһˉɜ_ŌŌѰӹ϶҉',
                'ţȋƲʏдł\x80źѢÖˡɭһϾ\x8fͳƛ˅ŐОжGҍɎǾÓƀˤπҾ',
                'Źз˛Бǚ\x97ԥʺƜĹãÐԆЀҭҎԣѮĪůƗҋԐXѠ˟ˀÈГ<',
                'έĭϸƴɰú£ƞǆƕ>Ѣ˚ʘŌ\x93 ӳйŢȹѓԥǬιӚlœϤϹ',
                'ʣҁ3БˣģǓįˊτ˖T\x96фѶŇͽ\x93ҞţƿЎZý[҂\x87χϯˡ',
                'йǌ҄ύХϩѣцőȣ®ӘɔBȭĦ҇ҀiϏаƯΜѝӻѕѨŎɪΧ',
                '³7\x8aϊνǋϋ ʃӀ©ˤΟ\x81ИĐϒѩΨ҆ʎȍјЬκƖ˷ŒˣƸ',
                'ɎŴΘʾІϠǇ(ȥΚЯɄĔȖ)ӢǫϵҲӴ˦ȳҘӟǎwPũʪэ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                9086268480677451867,
                5231520185428599302,
                1257184105117162272,
                -6359017584763276448,
                8284118166446811546,
                5697551593478080328,
                -1747522351595541547,
                -719814661004383613,
                4933273457658937481,
                206902281085665966,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                198894.29206371185,
                506490.46727449703,
                183019.59706710558,
                682447.6503817199,
                140017.80013684995,
                -8528.219261309307,
                928474.7950689069,
                106967.6866046632,
                524279.81389608956,
                819034.9947882264,
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
                '20210211:175539.411934:+0000',
                '20210211:175539.411946:+0000',
                '20210211:175539.411953:+0000',
                '20210211:175539.411959:+0000',
                '20210211:175539.411964:+0000',
                '20210211:175539.411970:+0000',
                '20210211:175539.411975:+0000',
                '20210211:175539.411981:+0000',
                '20210211:175539.411987:+0000',
                '20210211:175539.411992:+0000',
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
            'name': '\x7fτҦğˈgӥӃԐ\x8dʶŋԣƔ˭s\x9eʡėĒαéƣ\x94łӺԪôԉŅ',
            'value': {
                '^': 'int',
                '$': -4647301276417856451,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'O',

            'value': {
                '^': 'string',
                '$': '',
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
            'catalog': 'ʚʹҺˇǷƜŗϞΪҲАɽȟĳ<Éы\x9dãƶѢҏüǏǊŊʘЀàĸ',
            'message': 'Ĕԍ\\Ԭ˻ƎȒЌˋ(ɩҹΟȫċʬǤϪĺ:BŧɣϐǇίҡϕНν',
            'arguments': [
                {
                    'name': 'XԊČǤӓœ˾ӡӦěϯʿ˳ϝʑʀΙ˭Ɏȏ\x7fēΠЏɬϼƴȴ:Ş',
                    'value': {
                            '^': 'datetime',
                            '$': '20210211:175539.409113:+0000',
                        },
                },
                {
                    'name': 'ϽӲµϬåˁː˸',
                    'value': {
                            '^': 'int',
                            '$': 5447386951901069005,
                        },
                },
                {
                    'name': 'ɦҨʂ҈βӻӀŲ©ŮÃӆӄUҤϽˊиĴӝѡǿԉΪ^έǶ˱Ă',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ĵƪőǐϕԕɣcRɇ҅Ӥ`υӐӖϒ(íϕĈˎʬŭƳίҽūHЁ',
                    'value': {
                            '^': 'int',
                            '$': -7043764019418344185,
                        },
                },
                {
                    'name': 'ңAʦɖʅ·BNȒďδ',
                    'value': {
                            '^': 'float',
                            '$': 318920.7791824713,
                        },
                },
                {
                    'name': 'ɀƆqĦġ\x83ΨξɯŊҬĕųұȊ˫Ӱ˰dҹПƊϥԢԜΉŻЮӖ˭',
                    'value': {
                            '^': 'datetime',
                            '$': '20210211:175539.409735:+0000',
                        },
                },
                {
                    'name': 'νSэɫ£θјųǾɯВӛ',
                    'value': {
                            '^': 'string',
                            '$': 'ǘӹҁşЩǮИǘĘњ\x87ˡѫƣҵ҄ȿƤşӟ\x92ăΖȪѦYěԤ϶˟',
                        },
                },
                {
                    'name': 'õ÷ΪӞ\x86ɢпΆͷНǴʹʖȷΕ\xadϒùɴ˲е§ɮţԫȓϦɍˏP',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '6ԛƞɵϺϑΤ¦ʸҖю,Ȓʼ4ɲӁǇɎƷûhϊӒͲ\x97φҳϓä',
                                        'ɞ{ӣ˼ɫáˀь˭ϯЌӪΰˤʲļǇчȩŗ§ÏāЁ҇ӾϴҾòʙ',
                                        'ÒˤǡǶ$ͽћʭЧ¢À\u0382Ȏ҄ʆύːəɹϜWԃƸūЫЦĥĹˁ΄',
                                        'ǙњȜˑʐ\x88ԚϨМ΄úžҥӰш\x80ϊұǯ˺ȁʋԓʵŜɫНØˢþ',
                                        'ǝҹƃη˨¼˛0YĘӸ˯¾Άй+Έ+ʢѧȮǉχȌkɏŚҸɀǃ',
                                        'Ҟ®\u0383ԔśƃθǅăҪϞ˃ԊǯыįȃѻжʺКÏԑѻҚԂǮ¾ȁ%',
                                        '͵įŴŌɓϹĩӽɳҾҘҦӥ¡ĆѨȂӱÿфʦȋҊѣėWŃѸŋƿ',
                                        'ǱˋϷӽȳƂԁ˕хҤȦτҙȌ´ƚЋ˞ǛµİǓǲČ\x96҆Ȇϟ\x90˩',
                                        'ԃМȋŽҠ\x9eЕ-\x81ϒҒǯ˃ϱɒ³ćαǦȰfʖӵŰð˯W\u0381ӑƌ',
                                        'ˀɐï\x9dԮʩϔɴŝ˒ɧӑóЩԃ§ӋͼȰ˄зŦď˓бɐʏжѴӆ',
                                    ],
                        },
                },
                {
                    'name': 'lʪ',
                    'value': {
                            '^': 'int',
                            '$': 4100330803716052526,
                        },
                },
                {
                    'name': 'àǙΔȈţξʤ[áʑȯѺԞƙϟáŗȴˌ˯ԬҁЇɅъɋŘūҫо',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        8872938008706127397,
                                        -6688928336865420124,
                                        -6894056544452686484,
                                        9110689787331281040,
                                        -3150166983174737279,
                                        -1320951672426955609,
                                        5967140770624346056,
                                        -2790022638889748604,
                                        -9001429299080286777,
                                        3011194310308760298,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ɸș',

            'message': 'ͽ',

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
            'identifier': '÷ƶЄԃʮԝǢKÈԊȊӆ>ΗɩšƙӴҞȔԀ#ȁŶÈЊĚuƾԥ',
            'categories': [
                'network',
                'access-restriction',
                'file',
                'internal',
                'network',
                'invalid-user-action',
                'internal',
                'internal',
                'os',
                'network',
            ],
            'source': 'ƏǡóӛĢҐʎ#Ԗȋ¦ϠǱƕнϛˍǵpʼȁќĘǔ±Ӧʥљjʠ',
            'messages': [
                {
                    'catalog': 'Ȕ¾Ϻ\x9b\u0378ЎʨҀœŦʻҮȀЉǗϏќĠĳǡʠ¿ǢԕʜѰɝʧŒľ',
                    'message': 'ˁʩǓƗĵƃ˅ӻţƁÊŃɖǿӅñ%ǙϜ\u0382˅тÆӃŃϫԤқȂʠ',
                    'arguments': [
                            {
                                        'name': 'ѦŇяԬϲѻԤӸ˪ψʥʲ˵ԐҸ\u0380ǳӒ˸ԄőĨϰțǱҚŪsыù',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 702980.9748272797,
                                                    },
                                    },
                            {
                                        'name': 'ʗˢm¢ƛҖÊБѴTǲϲÖħŜȰķ_Ӷ×',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            547792.3964061582,
                                                                            60682.74633934276,
                                                                            826686.2028569969,
                                                                            461412.64151115716,
                                                                            422493.3080321673,
                                                                            40425.98806607566,
                                                                            134969.83268178214,
                                                                            138875.66355439668,
                                                                            167081.14661315776,
                                                                            480529.59838743636,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѓ\x98ЧӖćԫȇďáʋӸƢȔϰßԧԅҁǟǬөӭ´ѭԂӻη',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɚЯ±ŏ\x8cɭƈΗӒѩШ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            964308.985294461,
                                                                            5133.219861044548,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˷Ȱ˟ȾӒԋ˱ȑгŎϸȞͽЖҕĄʺëɮųϐɡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǍȊҖƯȩѐƙФуʒ¼\xa0мϾ\x9cŽGɝΫǼбĎūÏҜ<ǆԢʵů',
                                                    },
                                    },
                            {
                                        'name': 'ȓϘ˩Иƅ½.ț˛ɴ4ƨŢНԟ˓ͻaеǦÀϭɃѿŅƅͰОźӻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 820956.2979868505,
                                                    },
                                    },
                            {
                                        'name': '\x93ǖ:ςŪӪŝɌӇŪȷU\x9eĲćЖӺȨɑӁԘŒť',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӤƢǔAĂɌҿħȟgʮŻćЀҦтʫɗǲr˻Ƴ\x91ǌ˲¦ɻŽΗĸ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7637187146699792535,
                                                                            -3017174675754028135,
                                                                            5586469548644943071,
                                                                            5324681724231318044,
                                                                            1904307992385975695,
                                                                            -6631347718087578631,
                                                                            -1404511783383271163,
                                                                            -1057313365454211490,
                                                                            -8535858338567777162,
                                                                            -8806203714999198187,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҧ¼Ŧ΄ǘӨR\x85˻ȏВ!ÓȮðǴԖşʀƧɈŀŗĿ\x89ӄ¥Ўǲӡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'øˉ~ɟ4ʇƳи˙ǅЈҎÜǻŬҢӆʅъľџѱѯÇҫϷ.ԫӖǼ',
                                                    },
                                    },
                            {
                                        'name': 'ƛ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϨúӲǺɟÌҋȉƣϊŲǲƮ\x8f·ѰʚFŹǘύԃŎȱħļɳ\x9dɌË',
                    'message': 'ɓȦƍѿȟÌѪґʂϑ҆Ü\x82ǯʨΝĮɌĨǀ|˂&ҾΎʌɳĮғŭ',
                    'arguments': [
                            {
                                        'name': 'ơԊΒԩǋŜѴ,Q҈fǫѴʕȕҒƃаԈɝī²ȖǸѳȖǑĳ˙Į',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4470069831295194153,
                                                                            -8602636889866081092,
                                                                            -3806218225595018881,
                                                                            -8093654472624499257,
                                                                            -5598901627923673320,
                                                                            -1900375360725150945,
                                                                            -3113863675283041768,
                                                                            -285713681647730058,
                                                                            1826596205738493283,
                                                                            -3405573980644123553,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˹Ҋôáǻ\x8eѾçҝʐ\\Ȟ|Ҿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1974379146113973243,
                                                                            7893301889642598911,
                                                                            5655860762747539453,
                                                                            5991641754134227446,
                                                                            1864037339264860434,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɀȜďUѨõ˾KΏ\x88ѼˏǣЎ\x95ƬÁЁԨ¥ԟŶ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5861964101756998625,
                                                                            3957391426502016348,
                                                                            6758944597831774978,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЗÔӫԔҒāƥǪęʷ˱Ӵѓş÷ĶDҢԌπȼƍĊӬЪ\x97ѐΙͼè',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ό\x9fĪɜǗŶкԨŽgΕuDÏƟӠwŚ·ɳɼɇɘόǖ˱\u0378sĴç',
                                                    },
                                    },
                            {
                                        'name': 'ƇӺī«ƍʟŰБήĮӹƢΩ˴ϐ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.386299:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ьȱ˵łή˴˯С\xa0˜Ǚͱ˚ŞӤйɌʬԢ\x83ӌѷЖЫřƹӆ#Ҵψ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -346703729220515788,
                                                    },
                                    },
                            {
                                        'name': 'ρ¬ΛϜͲĞԘòԆŊǵҜѣԙɅ˨хǕǓȍ˱ȡá¥ȘƞɾӁɏE',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.386564:+0000',
                                                                            '20210211:175539.386575:+0000',
                                                                            '20210211:175539.386582:+0000',
                                                                            '20210211:175539.386588:+0000',
                                                                            '20210211:175539.386593:+0000',
                                                                            '20210211:175539.386599:+0000',
                                                                            '20210211:175539.386604:+0000',
                                                                            '20210211:175539.386609:+0000',
                                                                            '20210211:175539.386615:+0000',
                                                                            '20210211:175539.386620:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'έøĽȄҿĲіԠÚĈ΄ʏƧȭӃƓМÑʼˬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 851015.6642573553,
                                                    },
                                    },
                            {
                                        'name': 'ʶʨjɰ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8571369500407066101,
                                                    },
                                    },
                            {
                                        'name': 'ЗɬɃ¦ρɰɎƵϑф)Υ¬Ԅ³цҔśʾ\x90įҊѤŇɷӯ{Ӌяɾ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 501985.72466812027,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӍƦøʉОϣЩơƘ\x93(±dǟĊϦʛӒΡƱˑǥϷ\u038bΈЗȓϟˈ˼',
                    'message': 'Ȁˑԕǡʥˊ-ǌōљ!ҌЀĎєĒĞŎԅXôёƫŻfʃЉӋќҷ',
                    'arguments': [
                            {
                                        'name': 'ĽҕrƊѽʔʂˆԆȼΔҴɱʒ҇ǋƫƇǋůųϴƴ\x88¯ǑǰͽЊ¤',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÞҷǉƖ)ӠӹұԆϞɓЙýæ7ŹǁØʞhȊρq\x84ȶԞŏɯφÆ',
                                                                            '«NØέț\x95Ā\u0382%˸ΚλɔϩǽƱȔȾ\u0383ͻ΄ƗʘƽíRǦª¡Ν',
                                                                            'ëŁїю˾ћ\u0383ŵʼJБÒ\x8dҪӹɚÎțȉĄěŀЦʬãăҤɭӨѠ',
                                                                            'зǎł©Ώ¿ҽϑxƱό\u038bǔ\x8aˍȾʣҶœ9ȆѝëÛξŞТ˧Şʢ',
                                                                            'Ƅ˨ѧŭ\x83ɐɍ\x8fё´ЉľɼDяıÂƄʰ˪ɕҏј˂șѨŬȚǱǽ',
                                                                            'nØʡxÖȲhӗ\x92ʙʪδӂ˾˦å,ĬпÌύʉѠƣJǆıҖňæ',
                                                                            'ϕĞɢҀȑËǜčôѶ©ŉʹǲ¼\x87\x8deŁϣüɤԏӇơ¹Ίɿƿѿ',
                                                                            'ǫƦǏƸ@®ˣşũɽіʌψĞ˳χѝʞӡћӼħϖΈ Џ«Ōҹq',
                                                                            'ͲӾͽ\xad\x93#9ŎǃЧȖďѰ|ҤɅьäǕǒhǏʁǧԠʿŃϓόӥ',
                                                                            'ӗȞІǂӯΰ~ήщʤɒǘlɷЏˌʶ<ʵF^Ů2ǧЬϡУԄȘӶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɴǥȪӚΊƬļ`ͽƝȫřF9ȩ҄ӮƐΉԜЏԗȗӰáBΧʎ/\u0378',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¶ƬԊɫfţԕǱď\x85ˣ|ԕ?ϯŒҾāȝǖňТ˳ȦŠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            721075.2743839846,
                                                                            600797.2474821943,
                                                                            906471.4087645983,
                                                                            -59930.69722587426,
                                                                            -38885.304673263534,
                                                                            -15165.697180254283,
                                                                            34071.24502392646,
                                                                            647735.9356704205,
                                                                            899230.7121916341,
                                                                            605241.5952236252,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0381ƿˁ³Ĉϲӱ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 59985.32146616673,
                                                    },
                                    },
                            {
                                        'name': 'ãÚ˵#ˋƆǂɿΒЀʬóɺҜçśʽңł\u0381ԌɜǧԛüʠΕϽ÷Ϋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
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
                                        'name': 'ʠ˰ϙőÅО˯ƠβɰЪΗƄđĜŧǊçĴӹԊҬĤOΘȆį˓',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 439085.8148427446,
                                                    },
                                    },
                            {
                                        'name': 'ΒŇөƐӻƐΉƆ˴ıӗñpϱŖʡɶˠԄȑμʊӑʆ¹ƗϤĔǣű',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƮуΏƻ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˅ùƠ.ӿ»˅бf:ыͳȞ²ӢɎY1ӪŧԨ<¢ЦϧЮҍЬѳϢ',
                                                    },
                                    },
                            {
                                        'name': 'ҤČѕϘѿáΖ\u0380Ɔͼ.Ȇû¯иҬƓҤƷ[ӊЧǟӆŖѳґ©ʻʐ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЪƤ˘ÿŊƁʪôѩįɟӮνщÒρ\x83Өʿˌ8ʯƷҾ\x96ԧɳĄ\x9aԫ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǘ\x9bķȹțȦɼͶÈ£ςŊӤDӕӎΣԘĹȆήɸԢѰǟ˶Ί{ʉɟ',
                    'message': 'ɎŖʙάИǢĸʤuɊЁÉï\x8cӓӑɝʥȦ͵ǜχԂ˃Ǩ½\x96Ѹƪ(',
                    'arguments': [
                            {
                                        'name': '\x95',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.390960:+0000',
                                                                            '20210211:175539.390992:+0000',
                                                                            '20210211:175539.390999:+0000',
                                                                            '20210211:175539.391005:+0000',
                                                                            '20210211:175539.391010:+0000',
                                                                            '20210211:175539.391015:+0000',
                                                                            '20210211:175539.391021:+0000',
                                                                            '20210211:175539.391026:+0000',
                                                                            '20210211:175539.391031:+0000',
                                                                            '20210211:175539.391037:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ц˓ϕӫȇKΤѨΝʹʈHƂĞԦſǽДʔ\x9cÒδӅԢΆжǸ˰ʒґ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.391262:+0000',
                                                                            '20210211:175539.391273:+0000',
                                                                            '20210211:175539.391279:+0000',
                                                                            '20210211:175539.391284:+0000',
                                                                            '20210211:175539.391290:+0000',
                                                                            '20210211:175539.391295:+0000',
                                                                            '20210211:175539.391301:+0000',
                                                                            '20210211:175539.391306:+0000',
                                                                            '20210211:175539.391311:+0000',
                                                                            '20210211:175539.391317:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '_ԪѭɚʄƭĬǰɲСȖƊԈʽΜ=',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.391523:+0000',
                                                    },
                                    },
                            {
                                        'name': 'èѴ"¼ˁȚӲİǻȫԠԕӺƈåԋӫǈŅѓ\x86ԎҮƪϜǳɃеŗm',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϕȰǫͿӲϙÀɨ%½Ƴωӗ˺μęʤҬйϫʖ˞ď¯ȜʫǖƄǧȭ',
                                                                            'ĆӝȓɀΈјΥӓӓԫŃƧҠӋǉҕź˷ɖҘŉʋo\x81ҵƣӉÖ}ˉ',
                                                                            'ϰνҩ˲ȕ\x9fϦɭƝȍқ˹ԛԧΔÖΘ§ӮҀˀИȜСĝҫΉ9¹Ƨ',
                                                                            'ӥӁǀƺʳηҶĂҊ.ȚђԭԥſĴԩŖԔќиɅȀɂzʊʒҩ\x80н',
                                                                            'ˎƠѮ\xadˎȑōŞOɼÀѭф¶χԂ\u0378ѵȁɞŐȑг˦ҪȤԁѷѳ@',
                                                                            'ʏǗÜˣƑƀŞǈȃnӍ¸įˡʖɝǤǿ˙¶ǐЋiқƉӈũͷџ>',
                                                                            '˼ŷуи˞Ţ\x85ʈҚň\x84ńƨːİӁҾ»\x88ΧДƞЌŜbґӨҸȭҝ',
                                                                            'ϴǸѵŽԋWЌȬȔԉ҆ƒ\u0383ƽǿΚǚԒĶɓҷϮԀԭɠѽɗǄеШ',
                                                                            'ӓšĖȰʬȤԂ\x7fӛԃɪŔʬɅɛ˚ʬȇɴϓ,ɻȂšԮϒƍ×ɦγ',
                                                                            'πºȬϧѥ*ǵ˨ӡπӢlqL¿]ԎʣJ˾Z΅´ҔҟȭҚĩȓҬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȧ8ƱѶưԂ\x99ˎƻĳǉTΛĐӽŃÎƩȍ˓ñϮKeԄƛԆЍ˛Β',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.392052:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĥΫěϗ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8641268480043299708,
                                                    },
                                    },
                            {
                                        'name': 'ʟĘӬȸҰǧғȤâƜŖǗȣϞĭ˹ņʈŉǾʕÈьHL˦ѷ£Ϣϙ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʧĠȩΙÍȞ˕ЂѱçKɟĒӿӦœѬªʙѷđʼϙȜǸ½ʛ4Шϧ',
                                                    },
                                    },
                            {
                                        'name': 'хȡȊˉaÉȲ˭Ğͽ˨ȅʌӿƮҪċёƪϘУʦŚȿƏІĎɌϘ:',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -714998855535428808,
                                                                            3098257475187906018,
                                                                            -5468090691338301755,
                                                                            -2052045626979166320,
                                                                            -1662298742079423401,
                                                                            -769078977665785137,
                                                                            -1058316088442887514,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˗°!Ӯ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͽƜļ҃ɜɔЏҦȐȜԢҀѓȔĄΤлΡ\u0379ʕʨ˛ˁ¸Ȧԁêóԙʷ',
                                                                            'ΖɪјƤěżÒҤĘǾĵѬKӎƺμҐďȞӇӔԎɥӜũʜˬó¼Ū',
                                                                            'ɣґŵÕʪVƈӶʴ˖ѷʿρĦ\x89Ī҃ķ\u0382ƬΥÑЧΡѕ˱ϳň²ҙ',
                                                                            'ӫӓҦ\u03a2ъˊƿҧȪζĝȖƌʩйƸЛǶɫ˽ӖźʯþӸ˥ɝȥϮ\u0380',
                                                                            'ԚɴêԗëǲҧЧũѤɑɪʷϨЈҟ˸S"ŠҞ˃ƭǰҰŔҴ\xa0ŻȎ',
                                                                            'ÎȮЂѡЈƳƟuϠΒȋͿӨ\x80½>˽ϰ\x93ςСŅύϘˆIɽϻόЍ',
                                                                            'Ȼ˝êƛӑѫԀԎˬÞǚЧʙʟˌġƤҗԇͰʌÐQЖѻǬӵģԙҩ',
                                                                            'ȑΣ˨ˆjҍԕӒЊСΙȝϒӆ[ӬÜĎɡԖŻǤˎɤƯFƘǗнʥ',
                                                                            'Ǟϐ¼ÄňɆĝѴԀһ&Øȗ˘ϞȁƱћԄȶˬȴÚŮʰχŽƲԞΩ',
                                                                            'ǹԠˌˆ˕UȃëʆҬœӻʊԉ£PŷΣȳïʇ³˩ʚǬʗŻзƆ*',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɃɁԬ˺ωʉ^ϋ|εκӅΕЦ҇åZȵͳǸԜƶĠ\x9bȯНıԏǜˮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÕȽвәԄΛŵԔΎ3ŐËǜӽԄȒˉгů\x85ͽΜΩӞØοIȿè˔',
                    'message': 'ԩʜ˟)ǫƍʻʩșΕƙшŽέƘ\x97ͶʅɷҰȟʍ˨Ѻ¨ʅɄȤæɵ',
                    'arguments': [
                            {
                                        'name': 'ĥʌ@ԟΫǰĕΡϔǭȌӌʭΑŲţɊ¾ǛΕϥAѲҀ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ơѩɕ2ЈƪιԦĎ\x91ϪƍοєҒη\xa0ĉƖӿӛҢɖҐŠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.393746:+0000',
                                                                            '20210211:175539.393762:+0000',
                                                                            '20210211:175539.393769:+0000',
                                                                            '20210211:175539.393774:+0000',
                                                                            '20210211:175539.393780:+0000',
                                                                            '20210211:175539.393785:+0000',
                                                                            '20210211:175539.393790:+0000',
                                                                            '20210211:175539.393796:+0000',
                                                                            '20210211:175539.393801:+0000',
                                                                            '20210211:175539.393806:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\xadưđёԠəήʶ\x82ԩȯӽƋˎɴΕҠíØΎɑʣӕ7ϦǎҖΜϋˤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            317037.9442997572,
                                                                            52513.61649718112,
                                                                            -23632.05010501365,
                                                                            124162.06919816477,
                                                                            282743.08117929456,
                                                                            114103.98677058221,
                                                                            555499.5827834184,
                                                                            891540.0068238508,
                                                                            511998.7150223884,
                                                                            503862.2204544543,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ПЂrϮĎ1Ł҄',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.394287:+0000',
                                                                            '20210211:175539.394302:+0000',
                                                                            '20210211:175539.394310:+0000',
                                                                            '20210211:175539.394317:+0000',
                                                                            '20210211:175539.394324:+0000',
                                                                            '20210211:175539.394330:+0000',
                                                                            '20210211:175539.394336:+0000',
                                                                            '20210211:175539.394342:+0000',
                                                                            '20210211:175539.394348:+0000',
                                                                            '20210211:175539.394354:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '0!ϐÀєҪÕ$ҶӗʏЭϕύјƖҼгѲЭřӟԆłҕ§бӁаӝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8589337639353037022,
                                                                            7596498489882017711,
                                                                            3528498598636149782,
                                                                            -7012375526068889666,
                                                                            -7278762004344759829,
                                                                            4743674512022297056,
                                                                            288137140115138549,
                                                                            3625766234271049666,
                                                                            -3692204534950777882,
                                                                            -7711638345031690026,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǿȿßƖɡʳϷƳċԅϕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 763752.8388631049,
                                                    },
                                    },
                            {
                                        'name': 'aǿúƋǍ\u0381lĺjɊԊ\x93ЈŶ͵ŕоƂɪąɰХĜņ\x80Ћ˼cӲŝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԚȞѳɿȊʷʋĿC·ѕ\x82ɨȻ@ɾĊҝΪЕҫԆàȌɿ˵Ǟū5Ԛ',
                                                    },
                                    },
                            {
                                        'name': 'ˁιÌƶaĉԋ˦ìɎӟƲҙÏĈǄ\x97ιГ˾Ԛң',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ͷў˲ԄhӒɛȇĽБΞźXϩîĈԛТѺҭ\u0378ѕоǪĚɭ±҄Ò҈',
                                                                            'ɰHȦ;ΞǙǿуϺÝҷæώǣɁӻ˖|фːȍїçċʅâӎԔƢ9',
                                                                            'ɎҞϸZɰJΏӷЇŀğɛ˺ӅųǓZƊϒIɥԖ@ŹZўϫРʴ&',
                                                                            'ΒϹɃѤғŅɬŝ#ɟчԩȄ\x9eҟ2Υ\x8d.˵Ş˻ЂѾЈɪΌɝƵȡ',
                                                                            'Ӷ·ʇǰўѵUȽŪǋ\x8dԛϖëțϒӷ.ĿɎӀʛǹϙȌηÂǆĮѩ',
                                                                            'ҴγӃīÐ¥ɶȺɚiȉЪˉÀ˻RƎϣѰȆΖψɨɀĕӝԕ%ɹϠ',
                                                                            'Ӫĸ0ЀёÀïĞOĒӬɂӽ×ÎӥÑΆƷeҍĺͽΚƽȏŬȱɶĆ',
                                                                            'ǮψѴɽӁȢȜǝě¨ɿßÈДǅʏͻDϵΚϭǢԆԟǫ\x8bѴŮҡġ',
                                                                            'ŎĶӽϬЁаƞцƦŻӈԁхǌǀǝȺɝĀɾϏѭƆʦ˴ЏˇѓÏƧ',
                                                                            'ˮ¦ɛԎăВĿƚǖŴ˩àƐMÙӛƿ@ɍƓ3Πˊϼ¥ӗɣƸӓХ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԭ˔¬ϳʡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.395536:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǊӟʙҤ®ΤҁλΝӡ˪˕;ǋōĎě˛ЂӁǒơ]ĝZĺŅɌĜn',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            953728.957214657,
                                                                            377505.46288494975,
                                                                            829013.143784002,
                                                                            622741.9976524349,
                                                                            535237.503221746,
                                                                            757620.0169312116,
                                                                            916330.8635504931,
                                                                            365187.29604178434,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĠȐƘȇ˅ȝiʗǪΠȢƛ\u0378ǽ˝ˏҙҾΰóѐ\x81ʎЙƑЄƙĄҩɌ',
                    'message': 'ìϠʼήȧϒоƾŋǝϯȌвȇϵŖϨĆǐЧ˭ǁǽ\xadԌǵɆ\u03a2Ʈʔ',
                    'arguments': [
                            {
                                        'name': 'аѿѿ\x87ԬʺƨȼÃŕƈÆĪlϽΛˈ\\ǌäԞХǸưʢϾąɞӇƆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 440488.2618755483,
                                                    },
                                    },
                            {
                                        'name': 'ЙԑȠ\x96Ǭȳ(ǑʼԆɱјŅ#ŃʤӗΦЙǩσԙʹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.396366:+0000',
                                                    },
                                    },
                            {
                                        'name': 'jԚƺŵνµҩ˛\x83ʭҏΞɋ>Ș˘Æ˕ȝҶЄӢ˞зÿ-ЕǓǟʏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.396515:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĒʘƟɠĲ®ǊǸІɢēӥƙО;ƧΜĄ˖ȹʨə˷ҁ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.396656:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ϝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8306795524020129740,
                                                                            642591874871073633,
                                                                            -3524929006074406728,
                                                                            1986591044750978631,
                                                                            4662380746713839796,
                                                                            -4123741639670619219,
                                                                            1845062341893821048,
                                                                            -3777189795981593565,
                                                                            -4437003548061644037,
                                                                            -3095847328635305714,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԫϲRtFġʊɲƜʻoȴҚǔʜҕӯǀϡϴЃϦ˟ўΩ\u038dԃԞ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.397035:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ºŪƯѰеԌӄӪ}ɱǮɫ,ɣǭ\u0380ÊıβϗԇѓýϦΌϵŵÏȇϖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2172825278388828362,
                                                    },
                                    },
                            {
                                        'name': 'ё|χφ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2185071808375833971,
                                                                            -8027400593693368412,
                                                                            7499619835652626348,
                                                                            -39068178438557596,
                                                                            -6048192778732791814,
                                                                            -3639171962941053148,
                                                                            4502686446735795405,
                                                                            8337268022117140086,
                                                                            -1247354809082030721,
                                                                            -3366365665037180433,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Βϧ3BǋÓЉǏљͽҫͱΙЃ\x92ėȥȀέćΫЈǽƍԠǡĥԅǸ\x90',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.397617:+0000',
                                                    },
                                    },
                            {
                                        'name': 'åʊˌϝҺϦԎɆҴƒњǄȒȾяƂŧ(ƮyðӝɄVʄ¾οԠ:ԑ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\xa0Ѣɬvǆǚκĥұ\x98$Ц\x99гɒȓІđǄĕāӽѿɗœұɪ\x92ʁ\xa0',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'źŖѿ',
                    'message': '\x9f!ɵҴϣ˜ӞĘɎӢġһ{ȋʼ%ńRͽƜӖ͵ҘωFȜҭЩΣɂ',
                    'arguments': [
                            {
                                        'name': 'ңƳÐҐ!үŗϜҚ\x9eԫԚǰĘНХȟ˖Υ\x82АYyНķƾ¼Ҳʃˋ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȓ§˼ΌkÊȯ´ɌǾɱˤƺyΩϿӋԋԪŁɓЊȡ˴Ԩ҆Ⱦɰʸγ',
                                                                            '_ŨǎеÏҭƿÎΨͿƩʜҮΓDȻȨ˻ě˫ˁҋ˺Ŝ˱ЦǌǂϨW',
                                                                            'ɹɰӗ8Α҆7ɮԞΗҁ5ĜӪԞʻơΡӊӐϩÒǊЂȈʻǙώȑ\u0383',
                                                                            'ûɴŷѯʉɢʂʮΦƷȤжðєϦĹѸЇл»үŠ´ԘϨɒȳÕ;΅',
                                                                            'ǲ#ôǈ˹˷ǙȬËЈȁϷǦƲƷŠԐн\x95ћ»ʋλɓ˺Rȼ\x88ƸȻ',
                                                                            'ˠħŲdFơǇҹϴ˕ήĳ϶ИǚîϚïʅҜĽ·QɌӓĜΖɺƧz',
                                                                            'ӿ¨ƊǐE˚Ρǎӗɮ«ˠʰĻàΞШ\xadҐ˕ƕˁ/ɺǒϳԔƼџԋ',
                                                                            'ɽɺ\x88ѥǒŽĶǇǄҰǿӺѹˑȔ\u0379p`«ȡ(\x8aӸɠĐćAа%Ѯ',
                                                                            'þθͿɩόϮҴϮˡǯĐďњѦǐǼЏʉȴӂˍҎǐē҄ҲЏƲŌū',
                                                                            'ӢʹɝЈԥźĖϯʥΥ\x8dԏЯöОțŦɱӟԝθвğΈѝϒҲšϩʦ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˬλ>ҟJ<Ͼ΅ĮǴǍıďʸԚϮӰӶԎƆ˃ȥɒфКƟԋȴ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1922984616630862950,
                                                                            868530384356902215,
                                                                            -7921139680164059883,
                                                                            -91911532632189800,
                                                                            -2420119565804855392,
                                                                            -1387533921655460612,
                                                                            1364021202681495730,
                                                                            -440111372037207872,
                                                                            -2121437097066234922,
                                                                            8681959769197095426,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ôЬĝɴλʢ±źқ˥ɻɡѵ˼',
                    'message': 'ӡ|ʻ£τƦò+ϹϛˀcΘŨưȚϚ¡ňĂlНdưѦȤ`ǎ҈а',
                    'arguments': [
                            {
                                        'name': 'ɖfѿϙϩУȯ&Їǂô˶ԢЪΪώ˺ϼėӡĄȖȸuȴńƵǂ9Ҽ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3118943633326934184,
                                                                            -6723934463070055766,
                                                                            3284376787889249653,
                                                                            -1879150724688526373,
                                                                            1621863750132451310,
                                                                            5902564003260710172,
                                                                            8117763840896495308,
                                                                            -8369972239526336235,
                                                                            -3402538619188253057,
                                                                            3400576581594893892,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȸЋӤƀɴāΎǃ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.399140:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɏҚÚĆô˳ЫȆb˧ĺ3ƥƺŷɗ\u0380)ίĮņı{Ѣ©ɹO\x94ƭw',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            485972.23811633023,
                                                                            108791.58489670552,
                                                                            242842.0548623918,
                                                                            494277.79532886937,
                                                                            870703.0565012088,
                                                                            674316.5601926744,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'OɘƢƆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.399459:+0000',
                                                    },
                                    },
                            {
                                        'name': 'зϺˉцɷĄɎîǝА\xadϋĥΛяøЍΜ\x83Hɍ5',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3881757175458592595,
                                                                            6300376655791445004,
                                                                            1523632150362573278,
                                                                            8168838095305834774,
                                                                            -6330329124466131924,
                                                                            -1967875363258095449,
                                                                            3604450131315482274,
                                                                            8179887666068660047,
                                                                            -7984197071214667490,
                                                                            4124877654158628681,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɛ²ұтİǵͳc\x87\x98Ā',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȂĸҩōʽvщɦɳάĢ5ԉɔȼǃѶɣҢЎAțөĩóŃ˸Ĝ\x9fã',
                                                                            'ͼϫúφӁĹ°ĤȷöǨþĊҤSɧşΌG`ѣҐцҥĀйԠϪӐȁ',
                                                                            'ÕÕһʸơƕƚԅʳǺԝͰÏԁƯġʯԤ#PƋѾ;δӑҔņşƸò',
                                                                            'þËȏǾʇÄѱȅлӞӂɴJĢȟªʮҿ\u0379ĕŁѥĉ\x8eРϔBǑЮɊ',
                                                                            'αȄЃаӪЋϘќζԘwЌϰƓˊӃ˘ŵʜɿΡӆµϵυćύѦћâ',
                                                                            'ϕҿĿϸҕǍţҾu#ǧƄѳɱɵӱϭɣȻ\x8dоѩԈȼÃШǾΎʌд',
                                                                            'ϕ~ɻΥɁĻƔ|ѣѮҮʔȺǬ\x8cîɲNӵϹȩБÛēŵgºďȐȒ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϫȑ˴şӿԘśˡƽđţÊʇ2đōʧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 399208.12640197,
                                                    },
                                    },
                            {
                                        'name': 'ǒќͰΰþĀƢǃ§ǣʊǔ\x9c¾εԆȱȢҚӟ\x95ĥʭɘǤùǇ\u03a2˴Ϣ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŤȡŪʤǩӕӟkκȫŲЪƊǊíΘɗbǺԧƆѶŴΠ\u038dʘͺȊβƪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6464309967452504817,
                                                    },
                                    },
                            {
                                        'name': 'Нɻ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                        ],
                },
                {
                    'catalog': 'ȜѩȿũѫɊĻb¾ȿΫζҞÏȒȀюȊà¼рЫȊґˍĜ˜3ӈ\u0381',
                    'message': 'ЁЖΚКƫ\x8fεñŵźǥ˶ϷςʔҿѥǑyŤˣȓӍγȒцνҔȪҧ',
                    'arguments': [
                            {
                                        'name': 'ҭʳſȤ\x8cӘȻ˅˹ÔҞүȼɌ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.401213:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ѧ+эǯbbдԐʋ¶ƠͱɥȩZѴʑŏƦʢŔɢǀöĕʻ³Ǥәǔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.401378:+0000',
                                                                            '20210211:175539.401389:+0000',
                                                                            '20210211:175539.401397:+0000',
                                                                            '20210211:175539.401404:+0000',
                                                                            '20210211:175539.401410:+0000',
                                                                            '20210211:175539.401416:+0000',
                                                                            '20210211:175539.401422:+0000',
                                                                            '20210211:175539.401428:+0000',
                                                                            '20210211:175539.401434:+0000',
                                                                            '20210211:175539.401440:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɩƄѷԭԌǖĄѹҥġ\x95ʱɮ\u038dŤʺҰ\x97ń\x85˯ƖӚιе',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 975013.7737371759,
                                                    },
                                    },
                            {
                                        'name': 'ĿƳ¨+ŽсŘɩНɰa\\',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.401811:+0000',
                                                                            '20210211:175539.401823:+0000',
                                                                            '20210211:175539.401831:+0000',
                                                                            '20210211:175539.401838:+0000',
                                                                            '20210211:175539.401844:+0000',
                                                                            '20210211:175539.401850:+0000',
                                                                            '20210211:175539.401856:+0000',
                                                                            '20210211:175539.401862:+0000',
                                                                            '20210211:175539.401868:+0000',
                                                                            '20210211:175539.401873:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƠŬͲì',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.402098:+0000',
                                                                            '20210211:175539.402110:+0000',
                                                                            '20210211:175539.402117:+0000',
                                                                            '20210211:175539.402124:+0000',
                                                                            '20210211:175539.402130:+0000',
                                                                            '20210211:175539.402136:+0000',
                                                                            '20210211:175539.402142:+0000',
                                                                            '20210211:175539.402148:+0000',
                                                                            '20210211:175539.402154:+0000',
                                                                            '20210211:175539.402160:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȎжψШƉɦʜȗҪêţңǬ:ƌuĤàжʓɂϡоƱŸχѩлâќ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.402399:+0000',
                                                                            '20210211:175539.402409:+0000',
                                                                            '20210211:175539.402416:+0000',
                                                                            '20210211:175539.402423:+0000',
                                                                            '20210211:175539.402429:+0000',
                                                                            '20210211:175539.402435:+0000',
                                                                            '20210211:175539.402441:+0000',
                                                                            '20210211:175539.402447:+0000',
                                                                            '20210211:175539.402452:+0000',
                                                                            '20210211:175539.402458:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɓʐđ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            533713.033425112,
                                                                            -48779.93413007744,
                                                                            564234.2746687438,
                                                                            528907.0990910722,
                                                                            560984.5353736021,
                                                                            957608.2974650895,
                                                                            835653.2343188351,
                                                                            510988.23088633444,
                                                                            -84949.50420700097,
                                                                            59129.793589888635,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɩǹƥӆÏҧɄ\x96НLɾѩˆ҉ԀєȶѻŕЦοϏнɒǐ˄\u0381ϛЉԊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3734964067565285793,
                                                                            -790322813402691385,
                                                                            -584250705906185205,
                                                                            6234394852890595308,
                                                                            -5833000707269876383,
                                                                            7751262379430389698,
                                                                            -5447780976504938210,
                                                                            6410344982490427038,
                                                                            -4794508824613655316,
                                                                            -864828925713654081,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÑԔƶhы҃ѨgėƅЅϱ0',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'b˽Ƙ÷®ԮǾɯΜώŶʖ<ХφDǮĶȯȹ}ȳ˥à˭Ζя\x9fÚμ',
                                                                            '\x88˾ҺʬҠʆӔŘ\x88LšĸĠΣ͵ԊƘРưӺνƙÍʎƐ®ƾƦҮȝ',
                                                                            '΅ΙҡҪŐÅȐɠdӜі\x8dǺАΣҮ˜ȒȂє®ѕɜÀˊЩФӔ½Ǥ',
                                                                            'ϧLŖΒ¼ԬхƆů˰ΒĚƻăН˂ːĳ[«ѣɚ°ŹƾŭӶңǩʑ',
                                                                            'γĖҹÏ{ʘȋΣɨuŗϘ˄ʹ˧Ǔ5ӶÀƍɷð®ˣÍРťʓ҇ț',
                                                                            'ΕɶğηȥSӓͻ\x87Ǯ¬ƮˬԊΛңƝɶùÌ˟ƌûϐљɫӯҊΔИ',
                                                                            '˼±ȪŹǑԁɝϰ?7\x89ͶƨҌ\u0380iƓБőƴϕƅƄoȭӣҊӢͰԗ',
                                                                            'ȶАǤҴġņˏ\x91ǮԮÁʗȺΧξұӍѻW˷Ɩ_ȗÕàȧχάĳj',
                                                                            'ϗŴªӛҫĒ\x94ƃȲrɉĐĮƄԎαƔǭāɺúĺˠ˶ʘɝЍŘәĭ',
                                                                            'ǬƯɴȭıơìɱʄСǡjҎǐЮƪǢňɵȽрťơ\u03a2\x92ĜώӰӔϳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ыʃ˄ȖʻɳǕίɋЅŧɟӳʱӧɤɅɖƱē',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ă\x9dľƞҶ+ɠԜͺԠϵҽfƽѷΟÇΆ˽čʭȍŨҚəγǍǩϽǿ',
                    'message': 'ϹаӛĆƾΎҞ˵һѶңò˹üϱșɓƒƉμƉ)ɨψìƧÊ\xadǝʼ',
                    'arguments': [
                            {
                                        'name': 'γpϩΩ\xa0Ƃ˴~ɨ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                    },
                            {
                                        'name': '˼\x94ѩ/йŤňȻЬǊŭ\x99ɇɕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĚɳӗϵǿɮԧʓКμ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1149616006407846157,
                                                    },
                                    },
                            {
                                        'name': 'ʃӸȣɐǫÏӯ\u038dÎΑǎ\x93ˀʩóϑ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 910625.2277821719,
                                                    },
                                    },
                            {
                                        'name': 'ʃȐˡɤѠұҷĴʠϫӱГǫğӌαǚ˘ϳŹԙɮлǝȏ0ǵ%ȸȊ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ŘʴͼɪɓҲǀЋѕʧ\x98éѾ;ζ\x90ĢŅ]ǨӃζүÍӃĥɅңԎҝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 984665.0640971914,
                                                    },
                                    },
                            {
                                        'name': '²\x94ƚҚºԡʔΤgʰ³£н',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 41985.376573900285,
                                                    },
                                    },
                            {
                                        'name': 'ÝÂԍ˭Ќǂ˫ĘC˗ЬǚI˷ƢŔѳLҵѬʂɨԭƿǘŵӯʗԥě',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.407252:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Þ«ΩͻĸŠ҂щ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '4ǞgψȭìÎώʳϿ˒',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƪÉʏȃŐ˜ӽǯʉÝɼѯ6-ЉΒ+Ɂ҂ʙȆΤɞƸTĕ\x8f\x8bS¥',
                                                                            '|LĒ/\u038dǊ|ыϷ«҂ͻʹ%Ӆ%-ˣƴ\x94ü\x9cž\x94ǈĄԢʛĎ\u03a2',
                                                                            'ѭ˸ɮĀΗ\u038bƍ҆ɝѽӋԔϩӌ\x9fүЖΦҀԧҽȣĥԡԎʹ˧ɊFШ',
                                                                            "ƥїωQƳͳǠέЋʃӭҊϖŰÌԓʕŏʧ³Ȓ\x7fLbżư\x93ѫ'Ϣ",
                                                                            'ӾP˒Jѣ˦³ҋġϧõҷOƊŽ҃ŕͷɈŀɋΛԧǤҵӉɌӦɎC',
                                                                            '\x99źǴȰӓɪӌɏɳӅʐӱъԇͰϔ˽ȜӐÅјӧ8όЎŦȵŻʝȟ',
                                                                            'ΐðĤůԡЪǚыɘЋʮԙџɍƕϖѐİɒuЌӫľKϩѭ˓ǷѽΖ',
                                                                            'ȴʡӿ\x89˷ѴѺҟŷĂȲǿȧǏzӸȂ\u0382\x9eɲѵƋΰũцϘӒˁȈǀ',
                                                                            'ŹǴʰԘФņӟЪįǒőϵ¡ʪђԮɎϢιǸɂɒ˔ҎȔɲʝΩϖё',
                                                                            'ΩԙӶό˴bΜÆϜȭΏкŲҎѭɈʞϠѮ˵vˇϢƤS\x9a\x8bђТϸ',
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

            'identifier': 'ѼaӕЅϦ',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'мН',
                    'message': '˭',
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
            'name': 'Įüģлρ˛ԍĊȧɪ)¶ӑΖ',
            'error': {
                'identifier': 'ƾɵЂͰдįǣ҄њϸ˰ҏɘϱĠҙ0ѩ<ʸ@ŉÑë\u038b\x9cњѧǷϿ',
                'categories': [
                    'network',
                    'file',
                    'internal',
                    'access-restriction',
                    'file',
                    'network',
                    'os',
                    'os',
                    'network',
                    'invalid-user-action',
                ],
                'source': 'Ҕû"ůgϐɛ˯)˼ȐиÛҠɳˍˆλϝƫơӈȟӧΌȘέ®\xadʻ',
                'messages': [
                    {
                            'catalog': 'ȄЋnѾҢǾźyȺӅșÆԊӜЈʚɌƲ¦ЗƎȤ',
                            'message': 'ɚǈʢЗȁʔƕȿñ;ЄԬ˼MǸǘƮǨЭźȪΰɝȮҾʬΐʰ˃Ѥ',
                            'arguments': [
                                        {
                                                        'name': 'Ҥΐ\x89ȵˡͽʙбʓÈȰŃɷʀ\u0383Һɷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҷ/˺лʀӦ˂ðԛɮΛʦϐʈÁАΧũ?ȧ˥îēӋ°ɸΗ˃Жȱ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɝϖӝȭαȢǏǿńΛӏƍƝ˖ѳ~ԡƛ\u0379ūŅ\x8fҗũȡщʭҀɬ˓',
                                                                        },
                                                    },
                                        {
                                                        'name': 'şďǡɾŢ҉tӚƯȟ¿ΙµÝɁdϭRϜcΪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ҨϣȄŠԥҎʅúӼѳǍ^;ӡзɎƴӺԃӾΚ+'ӕ ŀQαÊŢ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǔєңҮŮΥηˣɍqŁπ҅͵\x7fģuôƑϦǢѶԩӡĬÛÚðԟѠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҏ͵\x82Όʫ®οƀNÛƺǱíԣʣȠǯΔǑѦԁLˊƥüԧĦĽѣ\u0383',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҭςƗπĿɳʿɿʐҾѴʍɦРОŮ0×ÐϰSηȤǵҸ˭ŭӶćɍ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5003966438817246295,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋԙǷɄѬӜɱϤԡѩʪTҢʓӗӰӢөǛΓθƥπѝ\u0381Ⱦ(ϑƜȓ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 693980.4902817354,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽƽӱƫλӮѷκ \u0380Ώ˞Ɨ˒ϙGń\x91',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɒәӌԈǙϘЂŠ£w¾Ѣƻņǻ\u038dϸțίԪÏЀөҲˬœХjԣԨ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӶӸƋôƶŠʽȞӕ˩˻ҒҮҳɞÒӟ+}yJϤáȴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ġλӏȒöºǼӨ΅æȖ˴÷ƛ«\x8fС}eo˧ϠŹ΄RȟǜѢӻѪ',
                            'message': 'ћƣʴ\x9cÎ¿1љҨ˞ɥ\u0382+ΎËlġ\x80ԖʰΠԞɴƲӦҰɝƐıǃ',
                            'arguments': [
                                        {
                                                        'name': '\x89σȡұ0ʴϷ˃ѿйŔʑȇɱȆϋ˼śФʓπê)ȪȜѧуЧĝȍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'όϫȸ²ϼȓæØ¶ûԚюԕD.ˌɥǿǤӘϠ\x8eύόЈ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥԑϱȍŝѦзƖɴŴȂ\x87ʓϋ%ɟȰ\u0381[ìƭǓҙƖƼ҈ƖXŘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɲ\xa0ʋ:Ϩǩ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ľʐЖԕΫ×ӠłԃǹƛçǸžɟ\u038dƾʯБǴӀӪ\x81\x9aӵĹМƂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6267118580794545339,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9bӢиϖëÓǇѾƥѹ\x80ȓ\u0381Ѝ¹ǝɂˑǪcŰΉʼ\x8eŠȧџfҸŮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7981129419428932874,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĢƆͺđƊǟhϪӓɪєɠˢҀ˂ňѠ\x8fʄɤűέ#Мđ˗˗Uʻ\u0378',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'τщʯǇѣϞ#ԎӜ˰ʠŎśɑáѿǮο®ӑǅӔ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.368360:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8aԨҸ\x99ɎŕϗǤ\x82',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¶ÓÓƿǆĜЇɗHй˒ȁhґŬBʚҋғYʞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӣΈŲƂЌʕɔ˶ѼӧĆɑʦҥ*ØҝԬкԬюCџˊØ˻ðЖãƟ',
                            'message': 'Ǌ¾ŽλȝϣϿŧӎ\x9cӜȾҦлːGʧǝͺβɾRąÎήѾ$Ҭўğ',
                            'arguments': [
                                        {
                                                        'name': 'ˍƆÊ\u0382ɜ?',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɿԧƑ#ȝƜɦΖΛƥɄʤĜЁԔΘßϖʏцӽàϓŭВɾԙĖʒĭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ӣe˵ǣεʣΡȈзʘ˺ҕɮӇӍšƿʖӻ\x8a˞ҕÞͻÈ\u0381ϖʁԀ0',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʾ˦ϽѾѭԑĈȿł˚éĥ˙ѰǓ\u0378fӶε8VȘÚaú',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.369420:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȓΣԨҟʨѭΎƅȪύÚԗǣġӐȪāͻҍιșӮͳїԟД37ēŀ',
                            'message': 'ϧǢοёʮʚ\x9aÕӀÙΖă«ȸ˚ԨюɎĵѠÖ³ĮǜėҒԌϬάп',
                            'arguments': [
                                        {
                                                        'name': 'ǢɭžΠϨɲǵİǭдĥңìϙ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ҭ˩ÜVȒЧLƪǰüʦБѓˬʑÕͳ˖ǣϡћщĘԞ˺ѪӋтʤԦ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǔ¤ԕͺхÛÃĹǀӴ¤Ұс»ˢ{ΉӾȔ÷ҳќ+҉ɗÉɛЛЅÜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5415743063115890937,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӳɥŜΊǄА\x7f͵ʯҲ:\x80ŉȔɜ]ʗǗӻǀʒýöЛÖˈĔ\u0383˄',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԭįþˡ˳ѲφʧĪɉҸύƺɀӥφŬ5ɢЃǕҘɸС˸ʳŉŘ×ʟ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉ#ӘħӧǞԧʐȻ(9ӻ˷ƭˢʪҜǦѡЩ͵ΑΔÇʓʟYĪѣʖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҡԣӇҰǣќ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ОɪúƳѱ\x8bȂYȇVɇƳɍĻнȜЙÄǷЉНӞǐθ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 306295.12359480705,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԄȄҍķ\x8aƪӟoƤӆaȅoɉм]ȃʡ˟cƯńˈ˕ǴҚƾҿґȠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1284651854106049212,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϫ˜Č»ɛӭRӷҡϔğĨ·{¢ƪŘƥ͵Ļ$ɒYӸөђξȒɒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6749084691098393775,
                                                                        },
                                                    },
                                        {
                                                        'name': 'őă\x7f˯ч\x94ϭӱʬȳäĿ\u038b',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.370964:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϴʦƮΊƘѐȼɑԛͱԎϸ϶ÂҵeҔҖ;Ɣѷ\x9aВĥϦøͿɝƁΖ',
                            'message': 'ǁț=ʇҲĜō¥xϓƇЉΣϬӑϥԜҩάƨßħ¿ӀȝҢ0ƥơŀ',
                            'arguments': [
                                        {
                                                        'name': 'мˎ˼ŔƞˋǅДԚJÕ\x90ȴˆҳҗΒĺѩƇȡͽˁΡȜŵˬÝģϚ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2805392198342389423,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˎi\x80Єӟ¸ʱͽƴрˣɓԦԃЈҸ˃ňӧʆů',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 395555.16380140337,
                                                                        },
                                                    },
                                        {
                                                        'name': 'įҟß΅ƥʩƖкɶ½ĊȡӸŘƈǞ¬ќǭʷǳΧυzʅʳºˣèí',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӘЋζD\u0381',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dɽҘłȁƏʭҫӀӤʾΩʑѪíżǴÑҺåҵсԖґɅ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3223287124914681334,
                                                                        },
                                                    },
                                        {
                                                        'name': 'qΕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʢмԠЀԠƑϭǆѱc\x95\x95ЪƭВԇΎŲwšƘqġųҤϦϞÞgЦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'чԩƀӶɌѧñ\x95҅ǋ\u0380',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '·ļʐϗǃŀɘĳɕëқɮбʢŅЉYǧ{ʈ2śϙҹǴ<ǻӾԖϸ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʒŜ͵ЖғԐùΨɭǑʱЍǦOӟǬŵƊ˅ѺǁГ˭`Gԟğłě҄',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.373166:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưϦԝȘĈҪėΓșϧņɉǃЀǳ~řȇξȯ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ώӛʂӭƐɪ[ʕýŬĻљɂǱʚǰɧαʸʢŕДˁӡŬÈˮѿԒƘ',
                            'message': 'ӘĮŒϽœɴʖ\x8dόН_;Ȩα˲śʴǋ9γҚQIКĂπȼȲÞ0',
                            'arguments': [
                                        {
                                                        'name': 'ϤƼƿȸӥn\u0380ԃƋǃ\u0382ΣǣǭĤƚЏǶDɄ˂БɥÍˎĈϏęŀɠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĘϰÒɗЊЏgĒˠԫɨ]ƇŰ[ˡʃŨϮŖʊғƥʀǠԉúƵƏӜ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ØtѲǦ҆ɼ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ГǓ\x91ɐ˷w˷Ƅ\u0381ǒʷʹрźӔҚǓǂЗTΫćЮԘ¨ǔӔ6Ҧϱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '1ʳȔĝǝƾOġәѺƦъưʐ"ʄʗѭÖUѬôƤaôÌżѭɥǩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ӊ҆˶фЪÌʱ΅łăÖÑΧʵ˰Ҳ)Μԟ>ƤɳƭkνɡΛʘ҇9',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉϽɊщaʛԣɢӛЂԍɣ˱ɴсӮȊŋɈrŗ\x80ʲϾɨǗËɻŕƲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'τ˱ðȨŖҰӅFϴ҉œÏ\x96ϢƁϒĂϦВÅӠņҌQʆҪ\x95ɬƚŁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 668973.6197589398,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ïӓϜҭ_ξĄЭ˅ԂƧӺȉǰɥˤМĆʮƍUʠѲ˼ɖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.374719:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˇӣϞӇìΕǉƬіѪɓ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƙưмʁʣ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɂʶRΛѱłҡϣ7Ӈ×Ő^ϩӎȐɯÏűȀ¯kȾЗǨƕįХɛψ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7627114815734865448,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'έѶ˛ȕԍ˥ØΩ\x81ɊǝҪîѧɣǳŃϜɀњˋӽµˀʘTúʰȮΓ',
                            'message': 'úʹgɐȴϩDȸν˫ӊèˠѕɖ˪ŅФϫ˵Ґжŋĥ%ȽªΜuι',
                            'arguments': [
                                        {
                                                        'name': ',ėԡMěā,ĐŁ˱ɮ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʨԘΠÌϤłϨϝпʽĎϜ\xaddıUʑϟóɕѬȬĤɍŅӨҐƐ\x8f\x83',
                                                                        },
                                                    },
                                        {
                                                        'name': '˱ӱώΊѳȤҒʔʂȾƪƒΞИкơIͿ¨ĭĜΛҭВӝǅzķɴԑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 685311.4064141738,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԫǐ҈ːƪҭɃӜ}ɍƁŮuÊΓΘоȫϝ½',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԒЌҵͳLɉӯȜӛMҾпƚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŽȝпқčýȸȌˮδȯЦ\x89ƢŨԑҧǯČҏȽǑϜőĵàûɳеǏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȋѦЩЕΜMпԄӊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀˊÄ»ϘўˀҖRđΖгϵȫ\u038dͰ96ϨΎɐˑäġÌź˩ÕΞe',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʃĖʲĄĀШăƎȜўɁЍĬҤƔрʍ\u038dϭԡ.вǎϞҿ\u038d£ʿѱü',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱԋʛʽ\x83қҋȾкêr)˅ʔʰ´ŜʮɬѥϕĞúɽ˗ɨʢпƣŦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄҈Ƥ&ƊЮ!ΐųŅɕӔѐƪόөӆАΖΛЩа˒nҙʒȕӰʑʹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЏԂĠԜʨǀP>Ϭɶ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȟҢǜǿúФ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'чЦѲɨ҉ʘүǥΣȥĈÇʼˬI˼łʫʋȆĘȢȟhǭĆÐɠ4Ǵ',
                            'message': 'ʱһɠөÑɖ˵ҺǞģV҈ƆȆäƅǗсÄZЃϪӓЏĩӟƾĸж%',
                            'arguments': [
                                        {
                                                        'name': 'ҝӸԭҎ\x9bБӼˡŊҐɿÏKǀßѻġŖӹƻӂ˶ɍǻҝԎäʸʶë',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.377076:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'R˱ĄřïėΔŔdiѕҶʹǝѕ˳ԬϽǳŋѹˠӽƫ˪ʙӤΊƱő',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.377218:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '϶ԜŞŚψЁԌ²,ɖȪΥG0ʘŰÑυRӮfÔǹϭ{ŜıРͰ&',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӂcҿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǟΘȰғӜǸМҮ½ЖõƧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 669100.4153265381,
                                                                        },
                                                    },
                                        {
                                                        'name': 'oҤʞӕҳʨxӆөȝȐȡ˳ąζ%˚Ԁòĝҿʎʭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĽΠνϘ҆FÎϲӑơ<кïиǀǟԁϳĕǛʯЀš½ȝȞȤБʃ\x87',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'iȸǺΡâҺɂnӅÈʀϵƶĒѪԐ\u038b·ÓƍΨӳcˮbÿΑǁԉô',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƨѿҍʦДКϠìј~ʛξʔƏӝѭ§ȉ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x82³ӆˆ;˦)˻hΧ||Ԅ\x97ƥǴҌ±кǿŔƴεǢ˦ЍʬɲŻƆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'v;ƞʨΕ˦ѨʦƚԘƒȕ¡ŠsǴʸʕӣȁӡҢΰΚґDˣҊдɭ',
                            'message': 'ΎʩвƾƼȼ˯ÜʩϨđȉǼµˈʑʧϠƏлʗɉŞҹˊ˵ɩȑ҅9',
                            'arguments': [
                                        {
                                                        'name': 'H˭ʐģгǿ\x90ÞΚзǟƜɎʤɜ\x8aŗŐхľόʚǄԕƮԟʏ\x91ǸȈ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԓΨɗÐPɀǐEōѰʀƶќΈʍʅԗŇɷðǼԤ±\x88aī#ʞѱ҅',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'pŬʠίɝԎśǯšȑҝζʦÁ\u038bUҳΫԭ\x8cґùǘŕʁȬɐϞŕğ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԣŝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŰƶƢҁʮϽ\u038dBȯШюг\x9fǒα\x81ʸЗŒɷɮŐOƛjȭӝѸҽ»',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.379242:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƦԞψάʐĭοżđԖƕıҤWȌϬИԙʈ\x84ƲȏԜӔӛ\xadÐĿѶ҄',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/Ҍŵьˢ(ɋӄZĭƢɐǞĊԐ<ɰʾʓЮƩvΑ\x8dɥǠѿÎǬɥ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˥ϤИь´ǘȃ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1908111618514077369,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ш9ûåѺԖ҈Ѐ˹ӟÙРͱӼρОÿsƔŪɌӈxƢȬăɨӑ˷ҳ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\xad˰ž²ӵΛ϶Ԥ͵ӺУˈϩџðʶ/БŢ\xa0Ӻ҄ñԡȕјΤʇ9ӟ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʾҨҟȼCǘЬϻ\x9aԙѺҷӤЭϝбϒӔІˑm˄έϧԖ˩ũĔΪǑ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.380080:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ìÜԉΊÙGЖǹ\x81αóʒyʌ.ǒћǯӕƀɅǯ˃ɫЈnҢД',
                            'message': 'цƗmʄϻϞǴͱ˦\u03a2əȓ;ԪэŭÁ¿ȴӐͺĿȞɨ÷ɫʌДͽӰ',
                            'arguments': [
                                        {
                                                        'name': 'ŵг\x90ĲʙΑǑÊĘǎӟ˴ɚә\x83ΣʟƣʸӰÁɏȀΫϐҜĤЕҰҧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 402675.3005206343,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹЊĶğÃĄ¼ʆ9ϝ¶ɱɭÕ˟Ɂ:ßɘ_іƼΩғȬύ˱ҼÝЬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˍɡʻƫɼȣŜh\x9cjѷȂĸц\x91ŮɆϨ\x9fҫȥƮɣ4\x83ǡӥɝ˙΄',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȄzƥȡĀ®ĽҏϢ\x9c;țїѮçӪҧΎ-ȌюǿËÔǼÛƾ҉ɡѐ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϒ¼ȡūŉʬѥɿ±Ξ7ƔɆȅӦϕϚ&ƳǾȐɷύ!\x97ĕNʍǚÿ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӟăċūƜЂӀҕüǩзũԪɦ˛ÆΫƷξұŸҘ҃ɚˀϝ\x85Ǭ8ƶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '+\x90ƳD/Ⱥ;»ԁԋɤȫèȰϷ\xa0ƬĥԤȕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'чŞ҃\x9bΫҹĿɊË©țͰRŞUҥÅӖъ!\x84ƖӪŶЋЃЉҸșʈ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȁħ˱ΔϪħѾĥ\x98ȘɻӜƻчўҼɲ\x9dоκ\x90ЖЋԔǏ7ɶěϠɶ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'âɃžƧŸĮƐѫӽŇʻ҇ȤζǺѴŞ÷ΣΨқȅʖΘԏϲÝѡȶЄ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'љϷŚįöôΡʸ6ʲǰƭԁxěɨªϗӌђɑİӜˈпƋˍϋ\u0383Ķ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
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

            'name': 'ɺ҆Ȇ',

            'error': {
                'identifier': 'ҬĠԕҒT',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'ƀ5',
                            'message': 'Ģ',
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
            'name': 'ƕΔĶƽőŗԍϘӁɛ˄ί˻șά',
            'version': [
                -5205713469314457731,
                -8796502995580678493,
                -6558356203912141996,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '·υǱ',

            'version': [
                -1905338744477472170,
                -3181409034933364755,
                -9076109887356766446,
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
            'event_id': 'ΖҖϞЮԎţȈĲnŴ´ӉΟυȾÏŤƷĐÚΡƚʏŰ˾҄Ƥ˹ҀӒ',
            'target_id': 'þѝ¬ψԖĿɞҰѡϤȌѡʎμʐ҅Ӧʪӻ˛ʥ=ϩ-ȗʰΙ˝Щ=',
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
                    'event_id': 'ӂǳȔМӧ°ϰ\u0381ɪÁuеЁ˄ȬӐą˲hӼɰɴӾǽbâîŸÃӫ',
                    'target_id': '\x95ќРϞНź¯yӮќÝӑʿ\x87Ф\x93ԀŒ˓ȋԡγɦΪ°ʙӋҙӰÝ',
                },
                {
                    'event_id': 'áÑ\x8cŸӑŶю\x9eƴӒҽɻυćΠǏԟгǇϰ-ПӬˇʥŽǳԐжԇ',
                    'target_id': 'Ϋ\x8aɽѝĦĽģĴλʨԔņɧǚɖ\xa0ΫďԚĚӌʉăťÒǎƒΙΦɒ',
                },
                {
                    'event_id': '˘ǴŌÁÝʅɩԇŜǥԥ˚¤?˙ţaiҞеθ\x80ƻȠƍXϢŃɷĲ',
                    'target_id': '.ˁɛŒ˥ԑʳ@˱ѣ¯ȸΊĖЍƲBЇΉеGĻʅ˰ľʬϐԁѨɂ',
                },
                {
                    'event_id': 'įƣǶЕӕǝǂȕƿĽӉǭФқ^qÁīӖӣǍʸÑϳ˂şã\x97ĝс',
                    'target_id': 'ϰˎɩJǬʜϾσ\u0380ҵÖΪʯѹǻҮѡҐԭԛǐőθȣ«ǘĥTĐǝ',
                },
                {
                    'event_id': 'ĐΔэЭɜƊ5ДЅȫ˚,ĐĥӡԢĢт¯µʚ϶ό˥ϥËƿǏНε',
                    'target_id': 'ъ\x85\u0378ϛKюԏƮǐЉнá˫wȀҗҼΟњӆîǣȲȨˀľЄѐǼƪ',
                },
                {
                    'event_id': 'ΥȾʻŘɹѦɟ\u0382ΜњȅǤ\x9fΉѷɕoǾʳ\x85Ҏ҃ЃɛƪѩüŁŅƽ',
                    'target_id': 'ȴԣɼӆæϐ$ϟǿ˽ƛǃâрî\u0380ȫęȞ7ȮԥʽВSƓ\u0378Ͱů´',
                },
                {
                    'event_id': 'ʱҳƍ҇ͳɽč,ήÌɽǺo˳ИˆȜз¾ǟѨӝˠʛӲ7ȽѨΧϑ',
                    'target_id': '\x9bƧэ˖ˊкͺԠÞѧËϔºĘ&ҾĈġh4ԭѰͷƛ-ȍǇӮƸԢ',
                },
                {
                    'event_id': '&ӯɎоɣҊͻ\xa0´¼Ѻzϋòʏϐ ŗ˹ԮӋƋvΗʛƩ҃ȑƻƝ',
                    'target_id': 'ĺΠʗȯЯɓɪ\x8dѕϢƫɏƒÖ\x83üӡ2ƌѓгїę\x8cйӹJŻgÔ',
                },
                {
                    'event_id': 'Ƌʝ҉ϿύҹŮǿҟѼȗŔҤѻǎ?ǻЉ˱¸Ά\u0378ҙÆȝ\xad¬6Šˍ',
                    'target_id': 'ɫǵɼԈɝЭŐЧЪ˶όяvӯҙ9ˌĴ¨(ʷГӝқǧҔęӊƮʨ',
                },
                {
                    'event_id': 'øЅƍǽʑġͲϬӚȊķĽљӭѩўӪǆǞϳbȁύѭ˗ƣτ1ʱƃ',
                    'target_id': 'Ǉʊ҆=NҊ_ƴȹοÑϺдч\x83҇łҚˏѲȠĖǸѯˮ.Ɯ\x94Ԡβ',
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
                    'event_id': 'ҹЛ8Ѻҏ҄ʪӃǂȝЪԀÔэʃΩŹóԘˎǗ\x80ɦxҊŏΝɦːʕ',
                    'target_id': '˶ϱΪȷŅǗʘgǙƔѬɊƎҠɭөԡӝIɼԡČπӀȁŞ˕˰ˎϛ',
                },
                {
                    'event_id': 'ǧ}\x86ŖӚЃȴђȮϧˉˈюțϮȭčːԗˈyǒЎǁƊɤü\x84àϢ',
                    'target_id': 'ϙƨô˼ÉǎĿÕǧ҅ԛȰǌʹ϶ǠǾłĈѲѦŮȣfȳӽǎʴ\x96ʍ',
                },
                {
                    'event_id': 'έτ£ϕŹuɭőԅþӘĺǸɯ5ӗq\u0380ŰǶ\x9bǭΓWŤӾԂłəʛ',
                    'target_id': 'ԠƟѰ϶Ĥ˾ӎċɌ#t\u03a2űӓƓɧɖșӄļωň>ѷѣčͲͿûƫ',
                },
                {
                    'event_id': 'ɋƿτŒ±³τӊŷɺț§(ȹʮǾøӽŕЁźηϓ¦ˑԃɷѿűø',
                    'target_id': 'ȩ˶ǽʹ\u0378ЖϷơȢη°ΏȆǸù\x99Ÿêԭ˥ˏЂѦљЗӝԘӳâӠ',
                },
                {
                    'event_id': '»ʽ\x9dǤб˾Аòǳ¦Тʚŧ\x84ҟΣ¬Ҩʫи·ȸòġƂ҄Ԫʲƹѡ',
                    'target_id': 'Ŭ҃ΕĂгҠӃΡ(ЄˀƎ6şÇŸцĺȮƴϚŀǆρŒőќͰļҖ',
                },
                {
                    'event_id': 'Ӹ\x94RÍЗaԟɢÐҘ2ёǊЕҨ}iƲѿхҊƓǑъͽȍŘЙӖМ',
                    'target_id': 'ŜΏϸ!Ʌ΄ĉǜӳȖȼΧʞ«ВǡЯӼǙ\x94ѐưҦȏlʲόņӟз',
                },
                {
                    'event_id': 'ГҤŏϣnƩӁʷÈǝÒƟхώÓӁőϺǪǸӔōӫ˳ԢӖĞɻ˼Ĉ',
                    'target_id': 'ʫɃ҄εӳѠԩӼű\x91ќŨǬҁѢѼʙϹľʥáŧǃZˤўӆԭʈȚ',
                },
                {
                    'event_id': 'ĿκΝbˉƾӥҠãХðƳ×ǧ҄ƼʢԀ˵ʽӓ˥ǛҹʍǍÉ\x9dÀÒ',
                    'target_id': 'ԉĈͰүqϙѷΐПƋȨԓЅѕ¢À\x9fάʭΈ˶d6\u0381ȟòËƄМơ',
                },
                {
                    'event_id': 'ϋȄʆÊďњѽϸŲˣȆ˫ԕ˰Ȁ9ōΜô\x88ҟҖӆԄοҜѳЉѵ\u0381',
                    'target_id': '\x9dįԞ\x7fӍͷcƯү\x9fĸˁÝĦϭӈʕΊʣӗҮĢȆˊЩȨԐ\x8aϲҬ',
                },
                {
                    'event_id': 'ҙ˂˹ԞϨ\x82İήǚżɉӬοӁ˲\x7fóʵЇƉЈԧӂĈԟЀԒϾϲǁ',
                    'target_id': '˵Ŧ<ѓ˻ξʛȌƿnɳūϪіĲɌˋġӸ\u0383ɚѩЄȗ_Ȅ³¾ȔĴ',
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
            'name': 'Ĝ|Ǹʜ˩ǤɩƛёǾӕюһГϠˣʊŤѕ[ʜ\x9dɪčνΌҶëĕІ',
            'version': [
                -151271557203370706,
                -1122335683388405356,
                -8894136309650990633,
            ],
            'about': 'řǳȔ҂[§ɺȉ*[Ǻ)ӠѥΪΉѧJςĥʠеʝԉɡăǗ΄ϱҕ',
            'description': 'ĳΑͰǉѠђŉϤΌЕƅ%ɄŻƠĩčØœȠЈɉƶŖԀɐϐĲʢĂ',
            'authors': [
                'ҵϩʀԁМϸȑºЯYǸIПtӫɰƢͳƖʰaФԜʍтɔƭΠ҇\x93',
                '\x87ѼύƆ]Ϸȥȃόǲɭϑȥȕ{ϳ\u03a2Íҩϵ÷ʲŜ˅ʗжȷƬԊȺ',
                'GʊТÎˆϥâԄӄΫѳCYԟэŧȽ{ğVʧłɑǯŖԬ˕ŧӣġ',
                'ȓ^jáÅĻΌӹ',
                'ԈЩҫș˥žϯʜͱ˒ӶƌӗӥȲŤºѥƋŖɯʗЁĳӺĴTǹΔƢ',
                'ʒҥȾϸȴϊƷʵϥ\x9dƵˏǱʇ\x86ˀϝ_ӞӢ\x91ÎʒƑĻƒɔΎɬ\x92',
                'ȫąʑӡɁѣ˽õϾԡɕӮφхǘϹԝʧŉ*\x82үΛǢΜϏЖӕЍg',
                'ϽǸŲ4ʳӑʧϭ\x86Ԋ#ѱƩʳıǜԥƊÔË˱cԩǗ\x88щҦрά\x9a',
                'Ԓ¼ҤԬĒψӶӛφѿӴˑҬΝ\x8cѫÜʲ.\x7fʻͻǣrԭ½dɰҠ\x83',
                'гȟɱ~Ǫěʇԕ\x9e',
            ],
            'licenses': [
                '͵ȤԮˬĽљɎȪƎǺй9ʹэҤѿѲüʾЃƎӏȳ2rΣɈʅÔģ',
                'ͳʏϪɮԗӵϭ\x9cɠDӗãӡŏʀɂіСөKĪҲ`Ƨs',
                'ϿĔƄɆΨ˽dù\x8fźϩӾҬȚ@Ϣɹ/YΆͲЛēƯgӃ´Ʌ¹ӗ',
                'ŒƗďФōȀлīδƦò6Ξāέˢň¸ԫ\x91ƼpÅǭқԟȬˋßϺ',
                '©',
                'ěďľǠөбųҼHҪʐЕʃӅʾ^х˷ȃьɪʠєʵΖȣқIϯҳ',
                'd˘й\x85ǮΧ-îˊϮɧ΄ȠĽÑ˻Ј\x7fͺ˹ǟÕVϜǧɚϑɩƆϨ',
                'ʰʚõνƕ҈ǔоԃ˵їŭҡґʢƮźұĢңũˤ=ӉϊΌͻǼˇž',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӝΰʫ',

            'version': [
                -709782674125304198,
                -6708605542726102078,
                -726692215950338645,
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
                    'name': 'ˉƄʕĎȌĘĘʴÑǿԂvҵƧʰї\x90ϽÞħУˉΤҤʓAӖUДґ',
                    'version': [
                            -8536627991701150601,
                            -7875307635107990074,
                            -7413639043449803717,
                        ],
                    'about': 'ũŝɷȄɟфж',
                    'description': 'ƌϸǬƂΓɯЊ÷\x86ǅΒѽ˻ӻ©ǂ>ΗӏӶłǇČѣ˝ɨʢΟ-u',
                    'authors': [
                            'рϑӦ³λѺĵʾͻ_ɞÞӈ˫ƄȭϞˑпĤԖɣʴʤφȻbӫŻҌ',
                            'ҁϛωĖȾý˲υ³ǰϔʠΰǄB\x92ΔʗʢƥωЍƥӨ҃ȭ\u03a2íѣЧ',
                            '\u038dѢйfđӶӡΞӑ?ʴ҃ϏƯƊţ#˺ԝ\x97ŧӢ˂>˸ʇӌ&ȑʹ',
                            'λƅ˴ŜШɱ®ӈƧȰŸҲěǩǍλ\x99ʄԃ϶Ũˏ®ŗΨӿѼӜιʯ',
                            'ЕǻƃY˖ɭʏ½ʪѾĦtЮϻʹĚĥҸιҪ÷Ԓңâȑμ~ȱɁɣ',
                            'ȖдϼГ¦ȸԆϗɼьѢ˺ÐӲNǡǱԣԓЌί±ҺӔ.˔ńôȫσ',
                            'ʥȐԕǘЍФǥϳ˙zʩʁїɀøɬϣΈҪϐÂѻɘ;ƐЊЂ˩ğ˴',
                            '˰Љ@ŜƩΒǒӔӑ˾ǓƕʣHăȲȚӚԓҡʋŕɱԏɊķ²ӹЉ.',
                            'гìЙǟˣ˻˒ǖʆΆʚˏϰ\u038bÇЗύѳӨԎŕÜͳҙƧ»ȓǶωЄ',
                            'ΤÄҠ¼ԙ\u0380ĳҳϯȓщΒ˦ʴԛʌëщűϜæȟ2ͻ\x8fӕȩϺɭ\x82',
                        ],
                    'licenses': [
                            'ʕɆΆԤlǾϞɂ˳æ8ǾΘɱϸ˙Ѿ2ÖǗqĵɓӰ"ŨɑυΆ',
                            'ԇɣӹɱķɕƒůБӥƝң˞ÙϬǒǱҁ',
                        ],
                },
                {
                    'name': 'ȶWñɮ¸ʉJӉӏϳ҈ӣϑΟȚΜSԤ˜ӥ˗ǜ\x7fνęӤùΝʡ\x94',
                    'version': [
                            -2785356563838118574,
                            -9014106633622119266,
                            -8853165810036001069,
                        ],
                    'about': 'Ō˚Ң˹ϘŎʧ»æηʼϐuȣ˷ǕʕȹР҃ƬʽϢҨ˓ÓīƞɁΰ',
                    'description': 'ʵӔшT03ƞϨʹŰȭ˻ǏҞѕƦ˘Ґ¥ÊŶҷӋӋ˴ƪɹƸʗӨ',
                    'authors': [
                            'IɂǻqƯ2ų^.Ȓǫ\x7f҅ƁϏӝʢǒΟцȑ©\x9dɉɼǖƓеη=',
                            'ҜČʾĉǱæϞȫa©ԨˢъŁ¦Έќ³ӪðŦ\u0381ȓмԋΝ˲Ѫ˕ϲ',
                            'ϭŻęÍ\u0379VʒˢʕʨȡόWҪКβɓæšȃ£\u0383ʒ?Ïɒˑ¬Ӗҵ',
                            '˕Ρƪ¢ӘΫҧĪʟʈы˓΄ќĭˎɻйʚǲʛДȊĹœηƋƄŻЮ',
                            '@ÉÉљё\x9dϛş\x8aԃTǌǣΝьӑԓ˯ɟӸСҫЬŭԢÔƄŀЫʚ',
                            'Ėϣčˈʼŝҳ\x85ˎÃ\x9f$ґәêżǙȰѣ4wjϑ\x96Ʀ.Ȋӥˠԏ',
                            'ɝ\x91ӒɗƾνL҂DкӧČʻηĈãŋӾҦӇ˻èƠ˳ѶЉƚŢӫȻ',
                            'ˎϹӓҐɲÝѿʸŗƜþԮҁÎÁ¦ȍяJɂřЬȅ¯ΑɎưɚȇĴ',
                            'ʊĂΪҕǕ\u0382ϧːœȚӏūđƭƪǭҕ~Ԏαȓјυ(˹ƬɰҎǑɌ',
                            'D˚ǕĉPǍ½ӼԦЛˇ˷ԃƒŵӝŶƇΌʻНPƛςϸǙρϵSƿ',
                        ],
                    'licenses': [
                            'Ϝ\x8eƔə˦ƛƐʡÒâҧŧӧ˪\x92ɩlλɢЍѮӨЯĭ?Ά=řȺR',
                            'ˠŶκȺɉſŷȕ\x84ÖCʎѧɠáņÅΧ?ȀªíњîϙĐηɬЁҳ',
                            'ǯ£ǝӛßǅԨɪǿуTХēɄˈӬƉΠɅØɨòȔѷȱÐʦ,řƏ',
                            'ϖȊ¢ґВҀӒҧɡ˻ԟɚÝˠƥԢÁcC\\҄\x87ŢŢψҴʡЕѮû',
                            'ƤŷEˇҿϒϺɌǸƤеĄӁɺWƽȚ~І\xa0ӝːúόǕр˖ԥ',
                            'xж˵ϏbԔǯ´ϦӄĭѾ´įǤ\x99ˈ˫ОɄи\x9eѣɤʦҤoòXγ',
                            '%ѯǈ҆«¹õѢФԄɘɼпҚ\x89ɄЮЩ¶ϖȹǹѳʽŲƉǈ;Ɇҋ',
                            'ʔ',
                            'мĉŰƹȝЁŬ˯ÈƑ}įԧɪþŹԞ˅ԚIϗʱͱƵɝˠǦҜȥѧ',
                        ],
                },
                {
                    'name': 'Ýη\x8aůÎĻɨžѝӁ÷Ц3ǿ\x7fĥΟ\u0382ɉɖǞӯ˰KśіҘǍ\x8cү',
                    'version': [
                            -410416139400661267,
                            -3260153361021380572,
                            -7660508207054749525,
                        ],
                    'about': 'úλƼыȦK¹ŕ\x83ӛˈТ\x98ԑÜɍ˥ǈʡԊʷωƣǧƈ±ԚÍҕɊ',
                    'description': 'ԓΚ˚N]șɧ×јäuԄĹJȌƍϟʣͰɘɋϞɱΩϙ\x9b¤Ⱥ˪\x86',
                    'authors': [
                            'ʳʲώ˃ӃϐΔАРĎǭŗʆǣҞΑfǣ]ϧʡŐӄȗùӴĝĊҽə',
                            'ĕїǖǽ˜ԕəØʳʫЪԧӈǽҪϵɔԗÔǭȖ˓҈ēқ+ͽ˵Ӥº',
                            'ǣƠÏ\u0378°л£ϳfˡʏΎÁγ',
                            'Ÿˣ҃Í2ɂϞѭЖɒɢĊͶ×\u038dǔȁƁӺѝ$ͿŸɓӃЀʼԥӻѹ',
                            '˱Ұ\x90ɄƷɡ³cԮȈԪЖtϛ˗ϔҽӭґӮɴÔJɲºӿԡəǂȵ',
                            'ēɌÏʦϜԣ*Ω˭ȋɾɎÜɅѤ£ΣŷȤǔқ©ńΥǤ\x7fēΆǏѳ',
                            'ǐәŁΑЕηƘŁ_Λΐǹɥ˄¿һӬǐıēЌ\x9aˠƈıІìӁǙŢ',
                            'ϡ)ŨϞ˜яǷǂŶвýɝÖƀ\u0379Шʷ˩ʏŖ˅ҲΞŀЅˑұФĆʾ',
                            '˴њϿ!ŉγā\u0380ԨŵÒͶĨəӑҐŖaÔΏ\x8aɷӛ˽ӰħԕԚԏf',
                            'ѢʓúƔϡϚЙƵɃ8ЀĩҜМЦҞ\x93ªԭϯЫʹǢͲΎЀ',
                        ],
                    'licenses': [
                            '˯Ζ7ȶÓµȮ҆ӭƭʽΣӿҚԇΊϓΟʢғʄLάđϰӯɎ2țĖ',
                            'ҙӋԂҼɃ˲Л\x95ȹʤќѕԮЮЍȽŹɜƱʐѽ\x91žӺУĸѽɾǁҊ',
                            'uтǩЛІpØγU\x81ˇʼ\x89îǱөΆÞɚɴЪЪΏʢ9Ӻˍāвэ',
                            'ɥѰªʎ˜ǰҖ°Kϳ˱Ůњŕɡ|ÅҪΈ',
                            'ӌΫ¥вȳoƣŎʿéƵҌё˩ϐŗAȯēҵÉʎΑƇѪҾЗԆΝť',
                            'ԐвӪʎĶ3О\u0381ҒɭβëȊǤӺ\u0378YȎόƐҲɠĻɗɚƋўŅɐԢ',
                            'ϹyȐѥǯO=˩Ҡ˩ż\x99ÔΛĥ"ɍϾŸƊɔюâɶϼʙmϔǵʻ',
                            'ϊЭГȽԣ˪ĞԌȗһƞƃȝ\x9cҡɅ',
                        ],
                },
                {
                    'name': 'ƮƣÊȥüɪ',
                    'version': [
                            -206342134310726243,
                            -1733013408720376944,
                            -4111728454615941789,
                        ],
                    'about': '¥Ȕśˈ°ӌĪюɝϊňģʁˁǪŲȁðęϵТϥgҴvŪñ¾ӳ©',
                    'description': 'ȋǾάƺϻХǭƟĵεHŸКʼˆ«ɰǂďǿ˳§ϠN¼˼ӆʊҐā',
                    'authors': [
                            'WνEȿζ;ӽwȮEІŻВɊǜʠĵǱЩжвƉȩǬѫ.ыА+n',
                            'ąԐѫЭƐϺʎBǒќχżԜЦǻŬҨҖEԧǷÖƻȅʘʜӆԔÿˍ',
                            '˒ė£ͼ(ԊɈЁ5ĺǍlȡͷԊӥȴΎŞҐKšʦєǭɜɯŞ˾[',
                            'ȺɀĝúπѕƵŬƛĒ',
                            'ÎӰıǰжҡĤʞ\x93ŒǩBAӜ˽\x8bʷѦǋ¢ǘӣíԣΛƛѦтƦǒ',
                            'Ƿıv˘ˎ0ʸơԆɆ$ʠĘϣɝɺ҄\u0383°ȄhǳԮyѿťкȑФЭ',
                            'ÇѥеɡúàȗԄЩͷͶϥԎĎ¾ÿΤа¨ϗ¿ΠǬƼϔsғ§ȧљ',
                            'ŕɞʗϙȷİʘ\x8bԔĝKǤƷЉïϏƱɋƝϗϝʿϙɡ˷ÞѱȦtH',
                            "ʂͻƋЪȰʖρΉҖƘӊӥèәЭZȵ'ʪˣĦİÅқƤg0ԝӺұ",
                            'ΆÖɨɟͲ\x82\x98ЍǁӄӶȵęӟΑĐΧʕ\u03a2ЛǲԚɆйԚЉ˕´œɓ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ѮϴԣЋōʣӛưQοΓĂ',
                    'version': [
                            -1609560908230179556,
                            -516995798913658825,
                            -8074461041449537694,
                        ],
                    'about': 'JǱ³υ\x8bлҎɉʇʝҦ4ЦɞԦ҈èʂкд¶нʛˇıſѦɅеX',
                    'description': 'ƅ˃ǺµǙÝ˞É˱ʒŸǘõx:҂ɲƛApgϦԈЪɒçćΉƾ˹',
                    'authors': [
                            'ѾǯƟϲ˂ɏƈӿԙhѥʓҳˠþƛԤ˯˸τϺʏȁОĘ{ϗVșм',
                            'ʬʍћʙ9ƋӂТʾхǘ©ɲȗŶȀЩȊѭӐǏӚ\x8bĺэ]Ǟ҅ʖǏ',
                            'ư',
                            'ǳ"ͻľɅ\u0383ŌЀʀŀү³ҴϲƻҊÆҎɕ˟ǗСҁƗįӬĳҞ\x90П',
                            'ͲƖÌőQѨΑʀjʮ²ͼʛǌV҂ȭԃ˩ӋϋǬɈ҂©ҕƆԖ(҅',
                            'ʜӓѴɊȿŉӭʅ\x81?˲ʍǽθҮǰðǮʅщĆ\x86ȱԖԔБ\u0380ѧЄ\x83',
                            'ͽӰĺһЎϼàLƃʣΓϨx ʪ\x99Џ˪ӎǞđǽδϻӜΣĥàȄʄ',
                            'Ӌ\\ł˩ҮɹҧTˊǖ΄ɧ[S\x81Ъ˶ϻ˶ƍЋѩë҂Đϔ˰О;Β',
                            'ΐƔǌ\x8bȾӸ®ƓƃӦŠіΪȧӭ^÷ϯνАҘӨОǱÙ\x9dԥȵԮԆ',
                            'ǁƴчŲzŅQe\x8dź¦ԎцӓҊǎӍТĉšѝʚÊĩϴĐƔҿϡξ',
                        ],
                    'licenses': [
                            'ÎV-τÊŚľ_фҌѼђAӰǸȍȝ÷жÿā\x8bΤß΄ˁ)ŘřЮ',
                        ],
                },
                {
                    'name': 'ˏ\\ƝNыӀňǬӜԍӌǡĸҌǮɁȧԂʸίƔòƷ©øěӔ\x82Ӌµ',
                    'version': [
                            -2440778327155611396,
                            -1216221688885257266,
                            -7075269833578256285,
                        ],
                    'about': 'σ\x9eʲʎ\x96ńʐ(\x91ŃȕΨLĚƳēԥЇȉȄɚαҲ Kˁȥp×ƹ',
                    'description': 'ѺŮ¤nӘß[Љ\x8c¤ŖϑǠϽRɌ˂ɋɫµÙƒƫЃŨɭĎ˯Ũԥ',
                    'authors': [
                            '¥|ǤľϥźqĿТǷɟŶĠŶʢãë%)˂ɎīȁǟЃȷ\x8f˛ϤͰ',
                            '\x96҄άì҄ӫӺ˘ɤѢYƶōʸʄ˩ҼΤŇƗȈţǵď˴й\x89ƽўΫ',
                            'ϹmȶāҎҋѱȏίҳѢñӺвǢÓ-ˌĪђ҉ʄǳy',
                            'ӥðԊŲǥԒŭǪų`ƤΌF\u0380§ʵķǇҊƃˇʗȑʤӑȖӘӇɄж',
                            'ɴ#\x8dľȼїͲϒǢӘȃȖЩԣѩȾϪn\xa0(¬ѴԄӧԞЛĔ\u0378ǻҡ',
                            'őŃtϣɮ\x98ҜȗъϜȭʬǯÇɎѲЪŸӐ˅ԓѐчЄĥҪӽқĈƟ',
                            'ʶ˳ϑRσĳɄӱɽȰΚøʧʓĀǵҍŜȼžġʟԒѯųƃћëžђ',
                            'ԡɁώҘȡ¤ȰȣʃңƁѺӠa\x95ԕìъ˥ȱХʙ˚ҤµªĶưσΑ',
                            'ƴɛіѼϵĀǠ`ΚЫŮϋȝƨ¡ιŶ\u0379ΙʯԟźʹtœҸ\x80Ԥʪȯ',
                            '҅ͼӉԦЅRƃĽ§öЬќǇ϶ʒѫʶǔXêŖфfԡЗа\xa0ďřǑ',
                        ],
                    'licenses': [
                            'ƍФũAĪ',
                        ],
                },
                {
                    'name': 'úRoȚoǕϽ˵ǬͲѳʱȃȊ\x93ƺǌΦŦУ%ʫÝθб\x9cǊǣ\\ơ',
                    'version': [
                            -7384541635932598000,
                            -6758649558843809467,
                            -8352571596759097319,
                        ],
                    'about': 'Ƒ=ʊɭƚӁҢѼ\x8eӶÃӽȽϟ˛ʛѷƢљļφŁǚʙТŠõƺʭɕ',
                    'description': 'ʌ3üȂpҥ˂ƈԦÒîǒчЍˇѐѥȚҷқʥĠÉφҩԚҁёТ˅',
                    'authors': [
                            'ҥɩǭЮȻƞɼ˓ĳʜˁȒȎ҅-Ƙѽ_6ΚϑǣμˇЁǛƯ\x85,Ů',
                            'ӡ˘ȵΩѷèϽ\x9aӄɶĕ¸хȍƳΪҞɸ3GƉƄȮη÷ɇǔ˴ɹǏ',
                            'ɔъϤ)МъϯĒƞлŲ\x86ɚҥӔȳzq9ЙΉɤΎΨϷȠǒʆȐŰ',
                            'ːӱCӥπ\u0383ΝɠыӓÜŞϊӀν\x8eƬѾßȠ\x8a¥ͿΘЮ\xa0Ϟĝϳɐ',
                            'Ϩ;ÒȷʊķҜȰӛ˘Ħ±ϙΙѧÇĤӧơΫӊӵrԙҳʨĹҀӶȪ',
                            'ЖĪ\x88έžɃϞǷҡˊѶ\x96șзҒčǚŞÆĥύę\x81҉ҺěŭԠʀ{',
                            'ǻ\x9eԓзƕοӤҌŬɍ@\x8aɀӤʊϒ\x93ŤȞʾНǥӋǠɣĦ',
                            'ąԆʀϲҿʣȺѩ·Țʄ˓Ƴɘʱ˒UƦВǿ¶ŌԜӟɖ\x92űӂ÷ʜ',
                            'ÑÈ$ƓʸљԂҙʿ´pюǯÛmВǐбōȒͱź\\ɚŠŠԮҖɭ\u03a2',
                            'ʖĆθɿƥĺ!҃ŭŴκӌŃǼψ\u0381_Ȩę˕ӻƴ\u0380ɽÜ˴BңͱÛ',
                        ],
                    'licenses': [
                            'ƋЛǘːÚƾϸрұ\x9fƻɕÖЍϻx~ŶȒ͵đKɣΌɃKΆɕЄҙ',
                            'ǩɭũƌ\u0380ӆԋ˖icėмg<ƗǓБˌȾǢćʨ˅ԦͿ\x8dϑǍʃѫ',
                            'Å˭DɃȅ˦õĂʔƱ»±о\x86ӾſŬ\x80ǰƖʏĩӧīnĒԦáӪǄ',
                            '\x9eƥӉƜƤԢ˹žʋcǫщºɊ®Ǖ:ѯӫΆӂФчÉǘτќFɀĝ',
                            'ԮƨԕcǙԈċǱfшϞӔԥǟǉϫδ˕T˟úζϕʅЍǿ˻»ΑƘ',
                        ],
                },
                {
                    'name': 'ʝʆ\x99ƐμѩƬҠźӀƑɋѓʮêӸҖӝȹɟšЪ6Ҿψ\u0380OʕЄe',
                    'version': [
                            -7946914356433696209,
                            -6248411314776424883,
                            -565693919931585654,
                        ],
                    'about': '˴Ԇԏ7Íѝuð]ȔΜĤ˝ĝԛå0ū\x82ʹǟžŰˎΑѫЗʔЏώ',
                    'description': 'ȹǷʅԇϪѶǊ\u0381Πƹˈҵɉ˚ģåɘϯʡ¦Ċɻӄ©\x83ϨʃxҘǺ',
                    'authors': [
                            'ѨЈâГwԨfƿŜɛϫƇϏǎƪɾǘҧδÞĖϲ҇қӢйġχǑр',
                            'ɡϔĘǺЌÛɼʭζ',
                            'ˑ\x9b¬ưȃԭǷĞӏǕɁĲ˚φҢƹɽȎĄʱʛćЋ΅ΨЖ$ԏμɗ',
                            "Žŗ%KǮѧҳќʾǗʎҷȦʊƁť'ɕѴЍŔΦԊξƦħȷʿӧÊ",
                            ' ЪĵʖnώȎƯҞHʑѪ\x92ƭɘɼѲѢǫСÝ÷ДÖʴǢØѴєƵ',
                            "ͳËɢƩӌq\x95wȟҒυԚεφńŶŶ\x91їұƻϙ'ƪҔʲѪ\\ԍã",
                            'ȭ)·ԪXԕ|T¾\x92ÑĀшHƹμȶОӐҰӬαΫ҆Ɔʀ#ĖϘ˧',
                            'ҰıŨ@ԑΜԡPːŁȖ˶ѶŻĒ˄¨эˣ˱ʦb˙nϩӘ·ˢԧɏ',
                            'ϗțŹ;ş҈Ƿʳˌ\x81¢ӞɎϡϷƹȐ$ѴӣǞ˜¿҇ϓɺԃƣʉ*',
                        ],
                    'licenses': [
                            '¯Щͱ`ȨЊ®P\x81\x8bӞˮ_xӢ´ˆ',
                            '#ʐʁϋYȥәsȘȨȍƏκґίԕʬÎƐiOĶɡ\u03a2ʣӢ˸Υóƒ',
                            'ǐΖɻɾŨ҅Ź:ʃɆĝȆ1ҩЦΊʤBΑʼЄǌǡɬǦӽǘǥǃ;',
                        ],
                },
                {
                    'name': 'ȼѧӫχŅǽëέĚŌЪҺЪf҅ʞſαȸΤZǤ¥ў\u038dҿĆ$ś\u0378',
                    'version': [
                            -7280970427717754532,
                            -7332267634113007795,
                            -5833285191250364943,
                        ],
                    'about': 'ʑʭӈ\x8cǼѹѤ¥ϐ9ѼϋҁЬ\x90çʃɞzÞ,Єǐϛʳɮ\x95dЁǳ',
                    'description': "ȎʂԒњѤɵҁ}ˉÜď\\ÒıƲҶЈйԂԀħҰўƉƺщɧÇ'Ȗ",
                    'authors': [
                            'é˸ș?ώĨЪɼΪԃ˝Х@Ӎ\x91ʵБɂʹɏIS\x93ҙԏ`ʛƆʎҗ',
                            'z˨ɉҶѸԤƒѣɮl˞ӾŠΘīјͱґūƑӡwÆǲѢƉ2ǴҔÊ',
                            'иfʣӥ\u03a2Ҁһѐîdҁȟ³ЙĳɋɐԐoƝŲƲЀӤίҞɻòEţ',
                            'GȻŮģʼěɓ\u0381¾ͷ!ĩΩȞĿҟŖŃŲʈżõΌͱ\\Јҥŧ˵Ā',
                            'ȹҶԔҪ¨ÅФʳϬȀҧʹ\x98Ѡɏ\u038bǑʲ΅ʫŭʭԭҚŶͺ҂ɴƶЦ',
                            'ĉωɿϜěҼΌϰΞMгY˄ĳϊ¬ŋɶѨƵӶǘԂǶȹЂϻáәӊ',
                            'Ʒľй&ԫғèҨŜ˘ȱαȳѬϾԜ\x83ԢСʄο0Ҵ\x83ɇƇȒ5ϗ8',
                            "Ì\x82˦ϺͿϮľǷɡʅҌиˬăȬϬ˦Д˜ĔĭŖΈȇ'ҲηЛÊǌ",
                            'ϷҹaϭVνыȄқØϖɝȬ',
                            'Ɇɓļˀ\x94γѳFÀŠȣȭӢɫʼɌ\xa0ťŔЁËȐεЍґϷ³Şѕğ',
                        ],
                    'licenses': [
                            'ƥ]Ǡ-{ĕӜœѰ«ς;ȠɊǬ˝Ř\u0382ҞʀѵρП˅ʞɵϨΖŮϓ',
                            'ûѡɁŕ҆ӓӸ\x80ŔĜƽӴƃ˪\x98ˠ҈ȅ×ЁƶƥȯҩȾГáʌß˳',
                        ],
                },
                {
                    'name': 'ª±ǒʍɽӡÂɂҲˬĆƐLMԒΞԨӋ¿Ƹ˻ѹ҈ȹ˟Ǘΐȃɐƒ',
                    'version': [
                            -6456934430254206838,
                            -2157507784896521904,
                            -7055323420891454240,
                        ],
                    'about': 'Йˋпϡĉн\x87рӑƞÙͱĳɱÍӊӆˀĈӎȄќїǁѸϲǗk҇ư',
                    'description': 'ЄϝYĈăАɏ˙ʡНϘ;Ӧ˜ҊƕʁĚÛŁ;\x7fˮŖ¬ȒМ|ƥɼ',
                    'authors': [
                            "ѨǮƴåĞ\x95ϓIͰШӚ˨νΞԁ'ʕʉӐÀзºӰЗѝƛˡΌαǦ",
                            'ÈɊѲȷǬӢʌǽŊтȞ!ǅͻРČԃѓū˫xФ4ēzѳӕȟ\u0379ƒ',
                            'ȨЃ(˷ǻŉǰѥƏ<ɰϡԞҦҾ_Њшė¹\u038bş7ħĦ˖ԄѭǾȤ',
                            'ȔҷPȓӗΊýеӟɲśƹʦƾԇUϪϮXˋĸϗǸɖĀ\x91ˢqɦȨ',
                            'Ň͵ȏƌЄ´έ\u0381˸ƪĨɶPϫПҘĴΑǏƆѓϒǙľҠ¬ʝǮуʯ',
                            'ѹϛϥϐʗҡĸ\x98μПͼӺ\u0378ˊȲϝɺЋδԨКȈωХŭĈşȚï>',
                            'ļҀΛȷH²˭.\x9aȅǃŜϹǥʒ¿éǙƻϋϪѱƓʐƜԃԖѤȘˑ',
                            '7Ԡ',
                            'ԈʿŴʞœӵ_ćȚ˕њɳҳӸњǃð\x8aҶǧ˪üçЕѭβ6íҙʃ',
                            'ʲàĐʗΣʯǃˤћУčϞϑðZϱ\x8fʵ˫ҍǕƛĄƄΚf\u0378¾Ңκ',
                        ],
                    'licenses': [
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
                    'name': 'ԖщҪ',
                    'version': [
                            -5560844308749275991,
                            -4996299478445126972,
                            -4848329130357432326,
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
