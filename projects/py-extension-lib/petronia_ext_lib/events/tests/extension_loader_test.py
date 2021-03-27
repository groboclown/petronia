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
            'name': 'bӀȨҽ®ŮϐάέƯǔҦŝȤ4Ʋŷ¾ʭөǮИҴϜф\x9eŨɾΥĹ',
            'minimum_version': [
                -1958914472046925665,
                -199494416011742024,
                -7566829776840469343,
            ],
            'below_version': [
                -7358769958687893247,
                -6542261400508695368,
                -8770633199594785851,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'âΨɏ',

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
            '$': 'ǡǜҖϥ\u0382yņЫÜ>^ӦȬɍӏӀ\u0381˧ҝȢ¦\x8aȫΦў\x9eөЗʻť',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5753443344768761672,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 843674.3738585354,
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
            '$': '20210327:032516.976558:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'α$Ѥџ7(љ>\x81ŊĵЗȹȳрȘ®Ȓ#ЈŌѷ˞ѯʊϋԄǞΛǗ',
                'ȷϑԛќȍÚóӺѠƋȩʂȶѻ#ԏӋѳ%c˴ҌЅэżċӏͷªˊ',
                'ˀƨԪѓьɫͲÊâƁΛΤk=!ʥЇǅϨԛ˚QVǇɆˮ˦Ùκʗ',
                '\x83ĕĹӸ½Ú7ҪmΞÖǊӲǥ˞еÁˉϨǅǎÕyӋǩ\u0378э˝Ԯ«',
                '½cűɤѻ˟ȴȒ϶ϫӐǲșɜpπŊ˅ǻԏźÇӘӔӧĂͼĆҡЈ',
                'ϫӲJʞÓĂгǒЬơӐŕЅɩǣϲ!Æѱ;Ǡ\x92ńŪʙʩ˅Ɩʯ҇',
                'қŀʱɻԎqłšPɦȤ¯ѼͺʺȈʮ»ˊЌìϊß~Чôюϴɖď',
                'Ǿчƙ²ĊϸɌԟԘÖʟƯɽjЃǳВϊƇɊļƅІ7Ӕ\x86¹\u03a2ӗŐ',
                'ĉĜнщԖȹ\x9c˝ү\x8cжϑĄӮnШôϐkѧѭѧŒFǗμɵ\u0378ιή',
                '|\u0380ïƒʱȟĘĵåѽǽƮ҈УԟѸǒτҽĮ\x9bŌGЈ\x87(ɕưʐʰ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2431848085335269079,
                -4464784272402218743,
                5920724422857981613,
                -1659286259608369016,
                -2572012972735894945,
                -7150511896423529696,
                6986390102914187559,
                46147074842551128,
                -5649943134754765263,
                7151068933200907160,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -48902.13423525339,
                270575.29528607475,
                850260.0474184504,
                625065.7754235186,
                699087.4760174943,
                88441.79951315257,
                192663.07203347853,
                976407.8421965116,
                957555.3539639628,
                911605.6108965046,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210327:032517.842211:+0000',
                '20210327:032517.861169:+0000',
                '20210327:032517.879113:+0000',
                '20210327:032517.897584:+0000',
                '20210327:032517.919029:+0000',
                '20210327:032517.941246:+0000',
                '20210327:032517.962862:+0000',
                '20210327:032517.982883:+0000',
                '20210327:032518.005319:+0000',
                '20210327:032518.026160:+0000',
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
            'name': 'ƷƄWĞΜL\x9bҙ(ɃcҤβɑƿɮѧ',
            'value': {
                '^': 'datetime',
                '$': '20210327:032516.345325:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'τ',

            'value': {
                '^': 'string_list',
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
            'catalog': 'ǟ˃χϧΐӘŝӽʟɴɨƔ\u0378ěԌˇӁӝǍıʟ˩oɋӨӧȘȍϐЀ',
            'message': 'ҕaEƩЉˣʎжΣШȖ·´Ƽĉв˗ˣƹЄӆpȬϨԠƭʿ˩сԀ',
            'arguments': [
                {
                    'name': "Ћȳ'ʦϴђʩЅźƩŋþɀӸ˾Ƴ±ϏʼʾΪ(ʎТ«ˊtÌҗσ",
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '\x80Ƹ"É)ÝiãԉȁѮŨԅ\x91ȤǗÅѺͳďӪҐʺ\x8d?Şº\x9dɜԭ',
                                        'ыzѳwǱſб¶ǠѬ¤ɗȴҒͱѿɠмŌҭÖӵԪ)ԗÐʵűүҙ',
                                        'ĩҀŀşɂģЕҶԨҤ)ĀΑZɊƓȓˬԦ£έŃˁДүЎј˽ʶĝ',
                                        'ˇɻ¡YËѻ\x8cěȋҴ¿ρƄȂшƻðӢƄКЁǆƞǭţҭή\x94Ûˮ',
                                        'ӮШˉϒҴѰϓǆʸɠłʫɅʍƓɷГԥσ÷ǃԂŐϞοǸХɠĀȤ',
                                        'ʌԛļ\x89Ԑǻ˚þҡҁƑʏҔϵʉʠϛȩɺœǃҦs\x91ǴũǈҚԁԋ',
                                        'ҐʈӊƣĲ³ũ´\x86Ɖ\x80ӿіOēǲƎȤʸǖǱXƝÿţƃиԦʋҼ',
                                        'ԙңʊŻͱшȡƋƨƂԁnʺŽӖӳʱҖß϶\x89ƛĿǓ·ɡóƁƄë',
                                        'ЏǹȶcýѧĨƸɵϝËѓ\x93ҙŕˇǓĥDˢжҦіÎÍǄʲѭʐ˧',
                                        'ÄҔ˽Ò\x85ԌԑΤӰϱƪĬк£ïŒ[ʌѾϟȔEĴʭyύóȅƷʶ',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ãφ',

            'message': 'Й',

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
            'identifier': '/ҲΓЂħ˨ӶȪғ\x89ƊтωʅƑӷʥɡɉϚ\u038bӉˣʹĲўˎΠҩΔ',
            'categories': [
                'invalid-user-action',
                'internal',
                'configuration',
                'access-restriction',
                'internal',
                'access-restriction',
                'os',
                'network',
                'access-restriction',
                'access-restriction',
            ],
            'source': 'ǎȣҜѰʖԤшfǋʱǞԁȼȶ¦¢ƩҜʉīѱ\x96sL\x89\u0380Ϫγôћ',
            'messages': [
                {
                    'catalog': 'ϊŰ˧ŎͺˋȈԄνҰӠҼϫӦȻЉ9ƔЅΗʸ˷uμԡӟǣʵƞΡ',
                    'message': 'Фˡ/-ύѷƑāдԈȕ˥˩ƇěçʠŌјϱӢˮЌϯћàǸAϟī',
                    'arguments': [
                            {
                                        'name': 'Ү\x9e3ʠƷ\u038d\x96ѨӛζΊҤ\xa0ȋԂɵfĳƒÜњϨǞα®ҤƀЋ˻Ş',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6289096490994111867,
                                                    },
                                    },
                            {
                                        'name': 'ҨǗőӚʽĢӑƦϪƖřŋQɢϗƿҩÀЎϽҗЛëӥɿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x8fϿӫϸùɡʜ·ŐʉԥɃ/аԤζŽς\\ҾƛąӃʂό˜&˸Ωʡ',
                                                                            '¸ƹϤϚˠtγ˩Ӻ\u0383Ư9ȎʂƍЬІΏҋƉt϶łςưġȥѤʔş',
                                                                            'ƱƙЏĔǬԛйÈ$ìȩǅLĳʫԀŦƧŷ˥ɾƂŪŷѠѣƛ˵\x8fα',
                                                                            'ǊӅǝήΜȂѐɡϦĸŠѹЮӭKȿһ϶ùũɔ³ÀѢǟ˘˦×ʆ\x9b',
                                                                            'Ƕʜ$жYӯ\x90ȕ\x95ÃӈNһȗЊВȘˮ³ԪǩʀțӢȔύ\x9bɚҦǂ',
                                                                            'Ϋˊ˥ΊÜŖЋӨԖѿÆˑͰ!ѫϚϟʫǻˢǬʙȔҪ1Ѐƾ¡Ƨɿ',
                                                                            '¬ҐΦ˵ɯǎЖϸǛȔίˌțͼ˶λˢ³ӜʷЫțǨӲҨԫȠʿ\u0379ɟ',
                                                                            'Ƀԡӄ˚ďďȸŵǖΏ+¥қԩɠМɧ˥µˢϴVɟ\x93œżϸƤ˥п',
                                                                            '¢ȎwщĽԜʁŭŮƁӿŜѨМтѼѱϟöøÛÎnȀΦWȍ3ʫɪ',
                                                                            'ˆ҉úѫƻҧʤŨγ\x87àĲǾΚΔкƛһsѻƄӶԣ˭ҭЏ˱Ӷ\u0378Ǽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѢūȵȈ҂ɈŁųʤ΄Ͷ϶ƼşΗѽӧѡʛӚΡӶ˫ųĲҢҬĂŏÌ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -70369.07825161304,
                                                    },
                                    },
                            {
                                        'name': 'ƅĪʖуƠˌǟћΞ΅ňý÷ıͰЙϟɏӒÝ/ũ³ńī¹ȷщˮ˪',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1959241858575366681,
                                                                            6440433363257804548,
                                                                            7908884244299987443,
                                                                            900965142673111919,
                                                                            3723793313514317367,
                                                                            -3835736474228236232,
                                                                            2774078818067215906,
                                                                            -7812147917414226210,
                                                                            -3221681911051943231,
                                                                            8679132559024094555,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'hˌϖʕīĔӫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032457.826491:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƻɡǷӈƏҳ,ӥɺƢϨԔ:ӵȬƋċʡœȦҮǲřӿ¥ʛςԡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŃʘЂǸϐЫϞʞİ΄Јӭŋ˧ɢĨӨ˯ԔϺɏʠȹ\u03a2ŶӍMԕЭê',
                                                                            'ɆҶЉʦҖӥ¥ѩʇöԣҬһʔόȹÙ<˖ʬɕϗǝ\x9fĵ¤ԍȯͲK',
                                                                            '\x88\x89ŰēƙԤҗǷˬũʍцυ˜ýƣȺŴԛЪДʌE\x8d\u038dȚĊȐѬǬ',
                                                                            'ϩέɓіżϊΕØӁƩȑûo¨ʌǲэĭȯ˒óɠϞӔөǘǙԬÂӾ',
                                                                            'ɣ¯»²ŧ˴.ǱϻξьëɔʗЍ\x82ŀѸʋBȕêѥΌӜ˺Ǉʺӟà',
                                                                            '·ǩȰЬĽɶƬҳĻҌ"Łāѳ5ŤȘдƃЁƺ˵êӍÉˊӝѲˈҫ',
                                                                            'ԤɶˈǎÈŮųʳǊЗΩҗӘːԠĖȂWȫēʭŵҧȍԣѪʁ]ԇǬ',
                                                                            'ȫҌʓļԒÁӠǦȸĘɦϿƓ\x9aŀάлЊ{ѥӝ\x89ѷԕҜϿĕƈȏǢ',
                                                                            'ĐĳϽтϧІƐĤԪ͵ŠʯƚɆŵϵ˸ǭuӏɍψˢ˫ʽşѥǘĪң',
                                                                            '˾(Ŧ˜ʯkbщҭʸɮǀʹΎĨȆЍžơʜЧӛ˚Ǳ\x92ðûͲз÷',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҫˏŬ(Ɯ2ūˑҦѼǏģͿ{ӄӤӢ˧ͼ˫ǋѕѩ`ƍˏɩvłƗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            104516015450867982,
                                                                            -4335488928986178920,
                                                                            -297514015580582385,
                                                                            -4406899582327373559,
                                                                            1353099612455038854,
                                                                            2216078295739763716,
                                                                            4692625337090911154,
                                                                            7934174610751676758,
                                                                            -1599581363109336929,
                                                                            5751276952561796580,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȧ΅ηԥȚӧґΠǤğԝƝǯμʄʈ҈һƔˇřΊ\x93),ćöԐAғ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǼøҴȫʏéФȆ¢ϩΥɄɛƓаЮȹ-ΥƵ˴ƑƘqƯгѲʈɆТ',
                                                                            'Ҋˡѫ\x8dƻ0ѠίϠή\x9cΊϫѣĊЧΣM\u0380Ń]ƢԂ˨)ӄϓϒӺķ',
                                                                            'ӳ˳ǆʞP˓_ӎύ˝ǼƳͶӊӮ\x83UѺʧ;Ƣƌ\x92үФψŹŤҳȒ',
                                                                            'ķ˾ĈǩΌŊӔˬŗ҈İƖҧȀғŻ҄ѽqĢãԥӬǆȫŌ\x98ɆƯЁ',
                                                                            'ȭҐ¾ԌïѮďӻƧͼnľÚЋТͰ˟ĮʦЙ˲ʞȢΛň˓ΞŶϰɓ',
                                                                            'ҤɎѐϯ˞Ǡ˴Ϣ˩Ӗ£ŋųʓҺǪ˺ЂǔôĲэԙȘϧÜeϐǳӝ',
                                                                            'ǇͱķȢĒҲ˨×ѼɮφœçΘDӝĀȋŃԌșƦʛѡʊӇӦΘε£',
                                                                            "ĺɫǪÕ'ɑǃÛ˵ǮǅšЮ\x8fӔɢːВƩԟӮГӢǅǽƾŶ!йË",
                                                                            'ǈvŎӽīєͽʁʔ˃ŸƍFgɝҗЗўǍīӂʳɐČљϨɂƙÁԬ',
                                                                            'ÍϢσͶʗ˴ԂǔϐǄɨҐҡςǂǓοԛɻʁʄҴ¯Ѓ\x94ʴ¼Ӿ8˫',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˍӇ˅ȗß҈Ǻ·ӆЅҗάƧ϶ȣͽӵЫǆЀȿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 611106.8439111232,
                                                    },
                                    },
                            {
                                        'name': 'ʯϟˊӴÒψҾƩ˟ЛȈӀ¥Ҵɭɣƣ«еԜÝȄȣȉSTč5пϯ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032459.399888:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԟѹԜѤͱ˚ϣӒėřĂӲԀ·Τ˛ϋТґŷҭ\x95ů(ӃижˤΛА',
                    'message': 'Ԫ\x96ϖˮΖȺĘϧR%³ґĠčīїȶÇѯ˚ӳlˣϩƴѶæӺʔȦ',
                    'arguments': [
                            {
                                        'name': 'Ȉżɑ`ʝxɞ҅ХʢǇéϩź˔ǆʒŔδˈѪ2˝',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ɲʹԛáϒϙėđ\u0379ʹϯ҇Ԋԡƛ ĪŬƂөwȨSӠçˤÒȞ˛Ż',
                                                                            'Ǥ&ηӭКɆǟĠΊƾƁҫAʲʕѸэÞȫԐџӢ\x8cЕϖ~ю˸Ǥԛ',
                                                                            'ӵɤeŪӡɂԨǖλÙ³ϟĤҴpĴɱˑӆʰŋѬĆˀ˷ˢљΘʲũ',
                                                                            'ÚӕђĩķȎɧǚĭŦӏԩЮɷvįЩÖәΡǎɈͽĎǥҫѫљɱȱ',
                                                                            'ÂϖϛĂx!áįŉŲaȪāϥĲʸΗɿЊýáΟ«ҴԦНѓƳǡҎ',
                                                                            'ɾǹǡĒȀÏëΏƖϟЪϗ˺LϢӡʚнӽ¤øÂ΅ʊȳӷĦԔԣȻ',
                                                                            'ȥŴ\x94˚˝ȃ³ҊŤ҆ґҽ˴Ȍӡҧ¼аŽ\u038d\x88κԔҽˏвCĭԆŻ',
                                                                            'ӹԬǪЊȳɚİɤĬЅ\x90ƭӗͼϮȓʩУ×ϽʹɗFЄΞƗЄȊȶƔ',
                                                                            'ԎԄÛҜČQ\x9dXɡϕ˖Ϭҟļ˒ϧʣɬʃ˅Ұəɡ˫ƣϻǅЦĦӗ',
                                                                            'Ԑʳˮ\x7fзč϶˦ŬƦɷʈǢΈϖƇҲʕԅωȐҚ˸Ύ\u038bӱҙЁĘӌ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'vҮƕ|ƂЧźҹҷưІԕ\x89w¥ԈԖͱǞƤ˅ϮΈśԏƩԭɺóƫ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˨ďԈԇ˝',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 208056.10573064187,
                                                    },
                                    },
                            {
                                        'name': 'ΛēТϷєѫºЮӱѯϡӰƉä©ΠĈ\x89\x90ѫȃύТΘμкѴӰüȃ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 81564.01035952728,
                                                    },
                                    },
                            {
                                        'name': 'ԨCӗʹŦΝ˙fèЂɜ¢ǁѨɖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1618966480763844943,
                                                    },
                                    },
                            {
                                        'name': 'ƱљТYǜŨȘÀ˼ΓӨǍӦ©˴®ŞΜѨӎ+ΗɊŹϹuѢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032500.275530:+0000',
                                                                            '20210327:032500.295127:+0000',
                                                                            '20210327:032500.314326:+0000',
                                                                            '20210327:032500.335067:+0000',
                                                                            '20210327:032500.355439:+0000',
                                                                            '20210327:032500.375251:+0000',
                                                                            '20210327:032500.397021:+0000',
                                                                            '20210327:032500.417049:+0000',
                                                                            '20210327:032500.436834:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'àˑӸЬǙƴΘ"ҷүǣʍȉǨѴɽ\x9eƔĦıʧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            427480.4149178441,
                                                                            567036.8085962277,
                                                                            983807.1013728299,
                                                                            626810.2169744513,
                                                                            308366.2763521585,
                                                                            269424.72419847664,
                                                                            40260.06739587066,
                                                                            -11734.913335413628,
                                                                            811728.2126712648,
                                                                            263457.2592996144,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŬʳlʇǘѬӡÿ˫ʩʋ˙тƳĴǘíĐӾһĽʈТƮ\x96ҭҶµȲď',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'щúēĻҒʭЛғӉѮΌǩǢȡľӖ[ɡBΊņÈWãӵ¸dљЙĔ',
                                                    },
                                    },
                            {
                                        'name': 'ԁӟʐӐӍǙҺɦǱʣӃтÊ\x80ˌɺʵʒϻ΄šɩԖΥ1ƣĚПƅî',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032500.868109:+0000',
                                                                            '20210327:032500.883977:+0000',
                                                                            '20210327:032500.901833:+0000',
                                                                            '20210327:032500.919979:+0000',
                                                                            '20210327:032500.938493:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȊĐƲȳłϯόЌĮҰɲƧ˙',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ШϡĢ\x91ІǝƎƶȴԊŖƗʴҫ΅љÆƮͶЮҲİѓÛˆҏӖ'ŹƧ",
                    'message': '˟ВέòӱŰЇƇдϦȬ˷TνͳØ҇ϓԩƂϧәȏǼΝ\x87˩κȓĽ',
                    'arguments': [
                            {
                                        'name': '\\ɂБԀƉϳІƃ¢ѼĀʆʱʛ\x9bљȱǟUɩиҰɫβԞς˴ǢU΄',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǴВԨͼɖɣ˄ΎsΰʧµǈʇѼƭҭŎҳ\x87ƱԊΰŒˠҼÃʷŜƝ',
                                                                            'ԈӐĩĩӥӁ5ЙëŮʄ§ƁèԚ҂ЛǏƽϝҝŶ¸&£ʜˇҍ÷ʔ',
                                                                            'žˍҝҟĳÉѨɧǀҡȇ˸К\x80Ǟѭ¢ҕʪêŢȡѷӚɁЉψŀżǏ',
                                                                            'v3ǑԭʒǈԙϝԦǬ˄ǶΓēΝȉӬԣƸ\x80ɑȶəůƯѯ˒Ňȷҟ',
                                                                            'мːѓҪĹЇˢƙýĠӓșτ\x82ɇňӕ˅®Șưԑɺ΄ӱǪrŤ¨Ȇ',
                                                                            'ĴƤ˘ԠԌǆ˪ѪҝqσÜcKƄƖĸèӵ©ǳʘҦƃωԎȶȍѸʅ',
                                                                            'ґʆĂȖ<+ξ\x84¾üįĳżŐƀЈҴŤɗrǛϭ˴BWηϜǵPѷ',
                                                                            'γӚ{їɷϨ9ωѯ˧ΥΘRrҥ\xa0ѫЩÐέɯyŗƐȊŷñRΏɽ',
                                                                            'Ç˩ͲīőҞɘê|\x95Ĩ)ƗïϠŦȂƩ˲ŨϖǝаŚȲǦѫ¬ɊЦ',
                                                                            '\x9eä¢ƽʳȞʷӰĩǉʽӺҠơȗōѦϗʋУȋŴʸӿÄѡѳӽɲѢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȾÓȮƔѤаɭūќ˙ҾęӚҏƕ\u0383ќĿąȅжġüКǈɦƲ²ьΓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҽǺԎȏŚίк[Ӏҁ7ǬӽĕЏú\xa0ŃԖ˥ԖȬƱƿ^ӣr¾Úԁ',
                                                    },
                                    },
                            {
                                        'name': '˜ԙʬˏΤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -49065.44874153792,
                                                                            522528.9769056032,
                                                                            456108.84926766285,
                                                                            594216.0256109793,
                                                                            190322.9275704858,
                                                                            319637.9297005769,
                                                                            666262.0846874946,
                                                                            464943.4564058344,
                                                                            385575.73231300194,
                                                                            849392.1095712654,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǫԢȫтwҧŭČԌ3ЕȉːƧƵѢ\x8e£',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032501.970195:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ϯв©ͳԢӶҬƑЬҽțЉɞϓԢԉɿÌRĝ϶ϛĹđǤԭǗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӲêȼшǗНĔҌÆҺɋ϶Ȗ{ÒŷŻɛӋүƛͶňƋџʉϭǜȫ½',
                                        'value': {
                                                        '^': 'string',
                                                        '$': ';ƿ\x93ȷǔԎЗĜҬԬӚӢQɻǅèMȘÃšaȐ ήƃŧĎѓϜī',
                                                    },
                                    },
                            {
                                        'name': 'Ɋƶ\u038b',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2409471910389127234,
                                                    },
                                    },
                            {
                                        'name': 'ѦˆQƸĶшʫřɰɋɂԭПļ˥ϒ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': '\x87ǾʱĸʈЛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŢʦӤȨЍ\x82˩ǘGŷ9Ƙtx6ѢҧÞҳȡ҈ύВɀӧ=\x80ҦƵʐ',
                                                                            '\x7fӱΊԨȈāģѫӆҞԐѺĸʒǶί=-ϬɻʘΫ\x97ƏŲƢ҉ȃϗҞ',
                                                                            'ɠȌϹćΒϩǕ˞ԋɶѠČдʾńʪùŒÇcʁҜƷʶgԁ0ȓд҆',
                                                                            'БĈǡŏљp(Əƻ}ϔ҅ȥҥјöǞʍɣďƃЬԜҕ˪ԈΪѳńű',
                                                                            'ȉϒ\x87ǔэΌȊÛæпЂһǁÑȒӷϭ˧υ\x9eŵƔˋϷ˹ʋ\x90a2ʫ',
                                                                            'Ҧr³з˞\u0383ƄϓóĵĝȄʮȄŮϼ5Ǜʋº˜ҚǊѐ҆Úӹơø˄',
                                                                            'ÒĜʲѹхѽūwƌœϚǎȴɬǵȔ¦ϕʾȻǦȄeIӧ~ŻѤыϯ',
                                                                            'јʋʯԞ¢Ïł˖ʗ÷ǿҷȷʈ?ćǥԖȣĝɓϼǒˆ˛іƞЅӬʙ',
                                                                            'ԉԗҲЄҁ˕ ċϩгħqǞĴϑ\x98Нǣ˞ΈϞÎˤsʶВŰɹɿů',
                                                                            'ÙʔɥǤŗΙù\x87ҝӦң!ӀƅǺгԣȌʄЈō˪ѝӴϯΆҦ\x86%ќ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ďЋѪԕӹΉȵȲɘ˩\x8dȇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 420073.05940615403,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˞ӕΐɓ¨ёТÉ\x92²оӰѺԙҟʎřмӸέȰюԃ˧\x8fˬɺ˖ΨЉ',
                    'message': 'ãǍҸǭ҃Bӷ\x81°ŰƘőӱ¶CǊčʍ¼ҫÚµΞșρǀơǇөǢ',
                    'arguments': [
                            {
                                        'name': 'ԬȖɄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032502.917122:+0000',
                                                                            '20210327:032502.934652:+0000',
                                                                            '20210327:032502.953242:+0000',
                                                                            '20210327:032502.971018:+0000',
                                                                            '20210327:032502.988502:+0000',
                                                                            '20210327:032503.007056:+0000',
                                                                            '20210327:032503.025127:+0000',
                                                                            '20210327:032503.044842:+0000',
                                                                            '20210327:032503.061519:+0000',
                                                                            '20210327:032503.078775:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʶϰKϝǠŉΙǴđ\x85\u0383aæЀΙԥӡåèυȓʎ˻ŕŭѝ26çʶ',
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
                                        'name': 'ˌʿ¬VƉËі^\xa0ŠͼЮŨĔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƻǜũѪʹͶʉȍƪȋπΉʓүˬЗӯ͵ğąʦН3ĮΥ°ɳΗμϟ',
                                                    },
                                    },
                            {
                                        'name': 'ϱҏʳѡ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 127335.03678917818,
                                                    },
                                    },
                            {
                                        'name': 'ЎiçАӔpǓ\x8fɝÜŬϸȔč\x86ԭƄķΊĉͶ<ӇŊБǔиͻԥ˲',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8029027596406269085,
                                                                            -7890982353719331667,
                                                                            -8328239853575622306,
                                                                            -5964775861033564928,
                                                                            6104247504209172756,
                                                                            8618201527062771,
                                                                            6777588188747818001,
                                                                            3914942132155975510,
                                                                            5804111142738952631,
                                                                            1522899946357575975,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѤʽЎǧŚ\x92ʋºΡZ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҕ\xadˍѿ¶Ȧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6232493694731066298,
                                                                            7454392902112536350,
                                                                            8362244021200403883,
                                                                            -7185666445287695693,
                                                                            -8825023508106229703,
                                                                            2002460076730470120,
                                                                            7538291074233555019,
                                                                            2904347722273668735,
                                                                            -5679943522847516734,
                                                                            -5203765041256775716,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͽŅȏƲſʃǄ®ɠԁÃҎ\x85Ɉ\u0383ӽʞϵŷǟËζÕнϦƤĥӯǼɋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 640250.3353158581,
                                                    },
                                    },
                            {
                                        'name': 'ҏfǭ˷Šˑn\x8e$«ιʑƻǪ(ǾμԫũFдħԚ˂ɢ×ȂЎ˙Ҡ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 85039.28937770147,
                                                    },
                                    },
                            {
                                        'name': 'çӎvņң\x9bQ\x95D\u0383ĬʃљέшʢʙǒĔ]\x92ĕЌțŗǶɨːͿ*',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1704728353861195949,
                                                                            7279751832497635048,
                                                                            8363605253784651246,
                                                                            -6285165887672765711,
                                                                            8524321454647905605,
                                                                            7568329537297592631,
                                                                            -954136723904635040,
                                                                            -2171443864046564190,
                                                                            8324332541669141133,
                                                                            4473918394429969727,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԥˍƽЍĮɧϠѷҋȇҝлԁέ˷ĪȀQͿȸԄYċ΅ԚЖǾ ҞĐ',
                    'message': "γͱÎ'ǾǍǚʧҟXʂŋgĸ{Ҧ˜ΐˠѣŕϽӝʒϟҡ\x99Ѳƺŕ",
                    'arguments': [
                            {
                                        'name': 'ӡɖ¢ȗƙιϊҚӢö˯CωŠҵ˕э҇ĩēȍɲSW',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            332704.4719122908,
                                                                            901678.609336418,
                                                                            422057.8508047873,
                                                                            934948.1686114717,
                                                                            420250.7394196306,
                                                                            988598.0118936698,
                                                                            246829.89664437273,
                                                                            68380.95111160947,
                                                                            975537.1892341594,
                                                                            214214.1733525211,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӄиϝʕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ЏP',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2327849644146869752,
                                                    },
                                    },
                            {
                                        'name': 'ŒÆƪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032505.151465:+0000',
                                                                            '20210327:032505.171521:+0000',
                                                                            '20210327:032505.187490:+0000',
                                                                            '20210327:032505.203300:+0000',
                                                                            '20210327:032505.219624:+0000',
                                                                            '20210327:032505.237751:+0000',
                                                                            '20210327:032505.256772:+0000',
                                                                            '20210327:032505.275456:+0000',
                                                                            '20210327:032505.295455:+0000',
                                                                            '20210327:032505.314170:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǠÇϭԛƽȹM˲Ôɩ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'çупȧī+ʬϤ¢ʤČiһƽƞƖǉâŠϯёѡÓư%Àƿυɲ¶',
                                                                            'ԝѹηѼНΪrŔыќɄˎұÀѪϦĖƖЭϊɁpǪћ«ԩǌʝӷԦ',
                                                                            'Ċʕ˧АĮǸƏʍȆɓ¥Ί\x8fĹNԢiŐēԋӈˑӛŖ\x91ȜƈԨŵ˨',
                                                                            'ұɘ\x90Ξʎʧ˽ɓɳĄԡ\x8aтϣĚοӉeÛƠƖǩĹóŌгˋĬȭτ',
                                                                            'ёԦӋˑʟ˝i˝ϐѳ0ȂnǁŊˤӦϴЖԦɢ²ĿͰ\xadͼΈɥȩэ',
                                                                            'oƯυʾҒчέţ˫ηΕʿȽ˩ňϨӜΥ҉TѢŰ\x8aDΌ˴&˼Ƅ:',
                                                                            'ѷʳbѧQŜāʱΝbНПΒ¿ϟƈȲȇȝʴѮĬȗˉɞžɗlС¾',
                                                                            'уĒȖҩɹ(ĞӎȊȟâΰҭȊԄԭʼĚпҔӒƁ˪\x9aӕűԭ¦ЖǕ',
                                                                            'όҤȾïʣԦ~Ă˽e΅˳ԗȤ҆ЯÝϙĐӷǫɾÕƟϽ˪ϐ\x857ß',
                                                                            'ӱɡžǰ¦ΖĎcΊǾŶ˻ԩÕπ˟ľõÄΪƺԩѺђȻåЫԭӖǃ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҅ΤΕѓä\x83¡ȏñǶ\x7f',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ШɹȇѱɑӉ½їЄźΝˮVԪөӸʉ{ĞЃ3ӫ¦ѭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƑŔ=ϡŉüƅԉęǌӓŝįbϩÞϵ˓ƷĴӈҵ҇ς<ϩ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3696287574179250675,
                                                    },
                                    },
                            {
                                        'name': '˒Ř',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʊǷңǆецϝʭԭȍŖÕˬ]ǰpΈébŪғȖ˾ƻǃӨǶ²ʐԠ',
                                                    },
                                    },
                            {
                                        'name': 'ԬŶùčΆ#ĈðŽȝƁͽÜÜȌšȜΉΗĸǱЗ\u0381Ȧ˨*Óҏ°(',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
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
                    'catalog': 'ΗӵϙɔαʟѾѭѐùˢȭ#¸ļғÊ³œȺϴ+ƎʥԘʪʤ˂ʕ҈',
                    'message': 'Ԙ{ƳĒ\u0381ʜӘΧΠԥϏΧʥʘñ˪·ŇúЊ˗ʔřє\u038dĺӵȧҾǏ',
                    'arguments': [
                            {
                                        'name': 'ǩһäΗҚàѥə˧ўWƛЄɟЮҊ/ʢ\x8bӶ\x8f˳ĆӐĮtʵ\x9dʣΠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032506.259742:+0000',
                                                                            '20210327:032506.277305:+0000',
                                                                            '20210327:032506.297748:+0000',
                                                                            '20210327:032506.316031:+0000',
                                                                            '20210327:032506.333635:+0000',
                                                                            '20210327:032506.351120:+0000',
                                                                            '20210327:032506.368244:+0000',
                                                                            '20210327:032506.386558:+0000',
                                                                            '20210327:032506.403742:+0000',
                                                                            '20210327:032506.421710:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʶɷƉǏÿϓψȁ\x90ΑșŖƫЗŚЩ˴ʶЀɘҗȟ&<ȐǁȘ\x8dȣɸ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4321604072003382513,
                                                                            8124733429699214052,
                                                                            1825210334013129949,
                                                                            6441380193605271035,
                                                                            6019129150513503331,
                                                                            8671730022666376449,
                                                                            -3917289462782054742,
                                                                            -5835645004972078347,
                                                                            7335424981715246356,
                                                                            3796095183857662186,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¿қϚˇŬ\x8a\x81Ľ˅ΖϺƶӈŕϻȶ˜ҩϭӂƥΪÇÊˣĎЫƣьԭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            215792.70651420357,
                                                                            616430.1172006235,
                                                                            394067.05295703583,
                                                                            627065.7257361446,
                                                                            -24464.467578574287,
                                                                            162034.4933251816,
                                                                            926154.7315623048,
                                                                            643029.6528783739,
                                                                            196320.0627076563,
                                                                            13617.381259035086,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҹҎĞѽӊѺȽ\x8eѡϱӈˋˮ½\x91ʗҘ\x90ϨѢďӆЋȩΙºǧч\x92ϕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ғǆʮ˂ѠѦѦϘҜӜǝ\x9eǉϡӿˆѷØɈЬʀÙӊʭ˝ѩ¹˗˘A',
                                                                            'ѰˁԬ\u0381ӺáӇԡɷæďĳѬЍӼɛǎ\\2ЏìҲǺԗΒϓΜй¹ǆ',
                                                                            'ȜʹΞyīɘKĥɵԨ\x9bϸΑхВҾ˰ǫԡ\x7fƭƒρōӁ]ɅˎíЩ',
                                                                            'ǎƳƀϬϨʥ`ДϨĮíʏCƊИϽĬʦǧ҄ʳĒЎÙɾϑɇɣЬǸ',
                                                                            'ɮȔΐʏθ³ĂʷśVʩ\x9eѤŲʠҰĈχóҘǸοʶķϯӊňӎʗλ',
                                                                            'ƈάÎʢ҃ІŴӻњ½˙ð®ӯȚʠɋ>ʬвȒŔɵĽϤǩӘ˙ïͺ',
                                                                            'ѓƑƩ\u0382$ĴǕƆBӡɒĵԥҕɓѢÄͻɒҤʅ˯ȼƚҘȩΔпyӯ',
                                                                            'ΏyҝϭĶԭȹϕŤеƀŃ͵·Ͳ\x85ƨϩ˪ƇҥƓ\x87ņźɞπƸʈ»',
                                                                            'ɿʔϤʌН˦ǥĤϣҪԓÎҚũŚ4VИ˷y÷\x95ɰñξ\x9aɌĴɭţ',
                                                                            'ΠѼѸʂǟɠзԧŤрԥӎԠƌѸřЁʭçƣª΄Ąŧ¼Ȕˏʜ\u038b˜',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ţϫԐęž\x83ļǐ˂ϨƁ\u0378ˤѭʕҼм\u038dЛ˖Ɍǁ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032507.337432:+0000',
                                                                            '20210327:032507.355700:+0000',
                                                                            '20210327:032507.373589:+0000',
                                                                            '20210327:032507.392263:+0000',
                                                                            '20210327:032507.410743:+0000',
                                                                            '20210327:032507.430469:+0000',
                                                                            '20210327:032507.449168:+0000',
                                                                            '20210327:032507.468297:+0000',
                                                                            '20210327:032507.487251:+0000',
                                                                            '20210327:032507.506489:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'OӬԘ§ʥȞ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǂǚƣЇІÚԩ\u0381҆ԧŜĺӧǋz\u0378Ȁʀȝaў\u038d˽Ȝш;Ω˕ȹЙ',
                                                                            'ΩВͶ¾šİǚi϶ɭӲʦĲƦѲ˰ӯΫ³\x85ѱЬ˦Ф¶ѭȨԎӥń',
                                                                            "ԞѪȎeĵl\u03a2Ρ³£\x85˯OƷ˥ıXɿӨɭșŮɷǀǍĤЄЬͺ'",
                                                                            'ČϲŀӔɽĽ³ƆԪя\\ďϳƱPƙԣѿțÑǉҠҒɊҹɉŝǖ˱ĉ',
                                                                            '(ʣØπʦЎ˶ӱ\x83ƳáŹCνjҜηьɷ˻ϬϦ¡ĝ$ʹ\x9cǷ\u03a2\x96',
                                                                            'ӒѤĚťēΡɈÝϕĻӨϩżѭǰɏς\u0383ȝ\u0381έ˟ǌǷ˗ɮüѯ˾\u0381',
                                                                            '°ÈȏϛӃͰђɹОŘˊ«ё˖ɟѠwÍɶͻ˰ѬϾĪśȍ\x8c«Åc',
                                                                            'οżTԪǬ҇ĕˬɡ\x8aɴΐāϢĜʙ<\u038dɶҵɨ˰ƚɭЄŴΓ\x7fхҤ',
                                                                            '\x8eҰơοġҹZϜș\u038bҸ@ÀǯϕDӠŜnȞКϩʆ3ŋÂ{Hʳʒ',
                                                                            'ăōʂюƔпЫӟŲÂМΈʁҾЪ\x99шƵť\x9d£ϻɦӉ\x87ƁƚȖµC',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӟӨŨˮЇȚƈþȡ¿IđƠ¸ϳĆ˷ȭӀԉѶŌÂÖǩƮѥǦ˂Ⱥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƐӪѰŗԡȭԊˮԊʮѫϽϤɘSўηϻǐђѿƭƻ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032508.124573:+0000',
                                                                            '20210327:032508.146592:+0000',
                                                                            '20210327:032508.170433:+0000',
                                                                            '20210327:032508.193074:+0000',
                                                                            '20210327:032508.213243:+0000',
                                                                            '20210327:032508.233194:+0000',
                                                                            '20210327:032508.253194:+0000',
                                                                            '20210327:032508.272984:+0000',
                                                                            '20210327:032508.293215:+0000',
                                                                            '20210327:032508.313540:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x88ƖźŪ÷ЮiȺŧȔċχψ¹1',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            422945.7015825073,
                                                                            386356.6923379781,
                                                                            408970.63882816763,
                                                                            523467.5701913234,
                                                                            -57136.56259194299,
                                                                            627138.9576067124,
                                                                            183739.0993632829,
                                                                            895466.5931185808,
                                                                            337271.54050962435,
                                                                            403170.69989445905,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ͻ\x8c-Ë<όĭˤũ˒ŅЮԠ\u0378ӑƄɢжɂРй\x99ÉȐЯӤ¹ˏÑё',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032508.692420:+0000',
                                                                            '20210327:032508.712262:+0000',
                                                                            '20210327:032508.730595:+0000',
                                                                            '20210327:032508.748482:+0000',
                                                                            '20210327:032508.766077:+0000',
                                                                            '20210327:032508.782960:+0000',
                                                                            '20210327:032508.798292:+0000',
                                                                            '20210327:032508.812965:+0000',
                                                                            '20210327:032508.828060:+0000',
                                                                            '20210327:032508.843087:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӓϠЪ·\x89ȤÒǰѲӸԌдƧтϹĵʋ˲ǣĘ³|ǑǏʑƩŪт\x8bԒ',
                    'message': 'ɏǚȗ˹ǰ·)(Ϩ\x9bǽ˷ƂËǎX҆ĆʒĆʳˑˣϻʺɁѶ)Ÿſ',
                    'arguments': [
                            {
                                        'name': 'ӷӞƌ˦ѥɉáaĊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'y/ϿѣӖ§ԫӧą²Ќ³ұƢήʁÖɰƟʧ²ƳԤѻ\x9eʗʫ=§ɥ',
                                                    },
                                    },
                            {
                                        'name': 'ΕȹȡϓǞBˢғ˱ɡйʠƽ\x93ȅǗɘǚë\x9fD\x99ó˜ɼҦʜǵϹԐ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6342029859911015014,
                                                                            501160843902828583,
                                                                            6496238502659116271,
                                                                            -8898510695974919485,
                                                                            -6972140474429416344,
                                                                            4283846705520216974,
                                                                            -1328329612001867292,
                                                                            -4635308350857386544,
                                                                            -2484905910301992702,
                                                                            -6448858275533775811,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'аΪНʳͰȓΣѡɗƴζԈɧѡ\x99ΊϑĴ΄ҞЧ¬',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032509.298732:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ėĲāӐς!øʈҌϭУїĬӴìϥÎƓԉSƑʴƥǐˠϬ\x8eөϟʍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4750759187572449147,
                                                                            5262461114740882953,
                                                                            -4907033894859121940,
                                                                            -1044347309220512467,
                                                                            9051578697606671588,
                                                                            -7968642512282986698,
                                                                            -1950389850813602599,
                                                                            -7929860600562169738,
                                                                            -5497221979374586214,
                                                                            -2863216077027055992,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȀƛώƸǡ˳ΗМɜǜі/ĭЧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĨªŸG\x99ѡϤО?Ƚ´ԃ˭Ŋ9ҐĞӚƛϋʎÒϺ\x8dǣ«ˌ8ˮJ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÛӐɧ\x88ӧƇɥԭƎ\x8bæɖ4\u038dĸ\x93\u0378ԠʪñǨ½ŧìȣʎĕ[ʼņ',
                                                                            'ɼůĹOˆʬƾνѠƎ˭ӅÄlӐыÆ λÏśΘ҄Ӫ\u0380ЃѪʉĦΨ',
                                                                            'ϥ\x98cɜFԛʐҝʧҺҤŝȴҏԉҁǫȤўƷďy˱ɂüəƷɄƵÀ',
                                                                            'ĬüљУ¨ąǷϫĆĄԜǣbȿ¹ʾˊ\x96ϓ{ŉ\x89ʨʲ˜ÐѮıτ\x91',
                                                                            '¡ȡǎӓ¼ŌĎԒɟƵԥνdÙѫ!xЄ\x9fșƂҾƥǠūЮϹӔͶG',
                                                                            'ÿòˁƘԡӬԨɇеšƨΆ°Ƌò·Ǆоeӿ˰Ӷ\x96Ȃͳ\x99ҕĠҐ\x99',
                                                                            'ǧҗʦʗʟƽКӰΛӠ˻˰cАƔүȔѷîԣҰѡԀ˼Ƌ±\x8eӻЁŴ',
                                                                            'ΣǔʔɣʌǳƃȺÚҐ>ǜӴů˧˶ǻËȈˆæѾȇƹ˘ҁ\u03a2ƞ΄ɳ',
                                                                            'ǚΰӥɡaƉĲÄäɩ΄ҽ˛ұηƘŋĩ˸ĦԈќԓãϺǋɲĬϤ£',
                                                                            'ǘԫаÙњΟƐĕdϋ˾ұΞƎΣñ˶˷ʾʘǘφ¢ʘϩ˳Ȫ҅ģʒ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĜŃο˷ӲƑ\u038dɁɭŧкÞψêϙƛxļ˲ʵҚδҜǕĈНʋԡζӁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʁ3˦ӭӛʑϫxЍËÚłHР˶ȍӁП\u0381v҂ǶUɉçăɈԥǀ\x90',
                                                    },
                                    },
                            {
                                        'name': '¹ˍΎҮȚəǆϺϭʗ_ӛ&ԤϼԜǬ\x8dΫӁҍϻəĨ\u0379Ң\x82Ͻͻŋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032510.055874:+0000',
                                                    },
                                    },
                            {
                                        'name': '¡D@ɃȻ2ĹӰǌНάӭҥģ?ħӻ6ΖӨƻĊѺgƽ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÞΈǘчϺ\x93ѓϔԣ\x80ӦΪEĊφӓѺŷɶψȆ\x94Ɗ\x86ȁ\x88ɧРӤŒ',
                                                    },
                                    },
                            {
                                        'name': '\x8cǌϨȭԩsҗΔДĐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϳɿӐңeȁАйЗј\x87ьӠ\x92Ӵ',
                    'message': 'ƪʢUҤąǧЕʴϼʵжӨϮάɑȏҳΚOԟˠνǨǱÚҟĪġҳǽ',
                    'arguments': [
                            {
                                        'name': '¨ĐςƀхѓȉĭȗЯȮҔ˅\x80ŬɈ͵АϺΤϹsЖàxǏȩдNϦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ҡ\x9aіуȆӾ³ɧρӞ˓ʝ¬ƛɆӃѬȝˣԆ˟ˡ&ҁȸхɆ˽ÑȘ',
                                                    },
                                    },
                            {
                                        'name': 'ϋ\x84ԏђĞƐżMÀîƸ\x7fɟúĠĴe\x97йÏ΅щ҉č',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1293272692075376514,
                                                    },
                                    },
                            {
                                        'name': 'ʓàƋũǂӇ3ǿ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5055096872301859146,
                                                    },
                                    },
                            {
                                        'name': 'īƉҌȅǤ҈ƇҷɀjЕКЖˢ#ĹԎǍz˞ŭdдʰƇƁƧȼʶĭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǿ\x90ȕĥǆεΉҧԙϹĎЋʜKЊėƓԥ®ѓѿТӥ˩öɲΊ˸҂\u0381',
                                                                            '˭ßо³˞Ɓȏԅ¡љҔƶƞŅɃˮsĞìţӂʧńӬbǳӝϟѢІ',
                                                                            'Ȑ˨˻ȢʟĐԩR\u03a2ë:Ð<ЭϾДȬҠɉϱҖWѫ҄ÔhӬʕЏȇ',
                                                                            'ӸƾȪďîǃśșŲQĝV˞\x96áшТƁˊĠˉʫ\x8aŭfϗ\x8dЮβƅ',
                                                                            '\u0379ӚϥaɥŋӐʏԀӑήěӿȝʧ¹dTƤįҮϷȀlȡ¥³Ñɉӵ',
                                                                            'ßɽǸȶΑΏΰ¼ʵǧəĿˎƠά҂ǷOжŲҿƦ«ɅΧϻ÷Žąˀ',
                                                                            'ҍΈТѤϚҺƹ˘ȉ°ă~Ïʛ\xa0ЬӌƲϼǩΥ\x91ȇӪȍȿǅˢWî',
                                                                            'ĶȭӑԟϓâūτǌǴϑȐǲϔŖСԡ\x9aʻéѷǛɶuŞǲžȝ©g',
                                                                            'ʉϟá~IӪΥʩЦȆəǅЬƚʲė)ʥ˜ƠŇĉȥʧiǞ˨˒Ќ\x98',
                                                                            'ӚzGȠѿКӢzüƙʶԁΓӢƙѭлɳʂ¦Ҭˊȶ˰ԅȃŗє9ͼ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɑýǆɐǉԣɑsөȖēζǀƹ;ƹιʮĔɇàƌ-¿ʁѺĥʬ\xad¡',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032510.834286:+0000',
                                                                            '20210327:032510.858369:+0000',
                                                                            '20210327:032510.881807:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'κʉƲAȹΙϣʓȡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032510.993910:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɶҲŽƟҜɛĵˉ˭ÒÅ@şú\x9b˾˚ČбʿŤƭĲϼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϹЧĺÀƩƜПԨÕ˹ϱыˌԌʫѰϖǍҀԢӄȞEҸÁľ\x90ʞ\x85ˌ',
                                                    },
                                    },
                            {
                                        'name': " y*ˡQǸƅ'Ξϳʭ҄°ʟǋԢ#Ģ\u038bƸbҕĬȳӨƒȳʦϡЁ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˟їĒιUӢžȌҷӦÇƄѠő҃и\x9cӃPЧҫϜưТʤȦӦѹÒϞ',
                                                                            'ʅТȔмѳȓɉɔкԫΡÙˠíɹЧѴҴEҸƻĜԀ˱ˌƫȊ±ˌҫ',
                                                                            'ʣŌĳƑÅү҂ȼԎғǔԔͻ˞ȒÈӷԗćËϚÁɐϟƴȡµʗ-ƞ',
                                                                            'ҷgǧӠʥƧKԄ˃ǳ\x8d¡ʄωђµ^ƞĸǀǸӐśӿН\x9bГϡͰω',
                                                                            'ӥԚěσęȄʘĔѫ˙Ȣɜ¾·ЫМԨʷȝǈӍǄȑË\x8aѲκζԚĄ',
                                                                            'ɧϵˡϒȢԥΕдƽЬĔɽǨӯƶÑΘÇǦƍˉ¢ӘҖȶmɵ°ƅϔ',
                                                                            '҈оÊ\\nͶǽʹτ;ɩ˧ɵ\xadǒɠÁśʩѡЬә\x9cħϠƜϬǾʣθ',
                                                                            '\x9bΎȀSǰ1ŕїѲΊʳԐǦλãč4ӬʄчН±vӿUƣšӎѝ´',
                                                                            'ИŔ˹ȔŝξЊľϸˣƖ\x84ïĶ"Ϋ]žķΖЂʿ˓ǇǓкƏŲʈƘ',
                                                                            'ԭ8ƔˈҍŨӹԊоԘƫӤӗːǊΚԧɦқĎˈԍԃŷѠΏƤƨӞÇ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¸ůƐʃǕ\u03a2҆ҘΕԖӣ΅Ѻ˼ǂϣӧɟ÷űѝϟ\x86tѮşԖ\u0383ǟ˘',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            630434.6575675465,
                                                                            345037.99445437227,
                                                                            960924.5904248087,
                                                                            322295.8760125286,
                                                                            268390.89515058417,
                                                                            168193.726977606,
                                                                            921880.9930680847,
                                                                            299461.1989725914,
                                                                            289068.61737122113,
                                                                            -75249.58916656302,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ëҍżĈφϟėӳΦϔº',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 946057.647544807,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'НѲ\x82ͼώӌ\x8dԭЏԠÞҴȇõɑˏʁˍ˙ɞәЮêӨ\x8eϧфѹCÚ',
                    'message': 'ЅηʶʆģňĎɞɠ˷\x86ǅĉƳ\x9cЇǕϱїԏȽǆ\u0379ˮɆ˼ǵѦ҂г',
                    'arguments': [
                            {
                                        'name': 'ι3ԍЌǽЬяӜʇХĲˀˀЕ\u0381ÀjёɴԅŇǅûɫɑɞȳȫŎç',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 16942.27394154003,
                                                    },
                                    },
                            {
                                        'name': "Á'ȃȌǟƎʚԘċ£/ϸ_ŹѰȰ˯ǁɥʁȼͻϯϰe",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032511.908057:+0000',
                                                                            '20210327:032511.928790:+0000',
                                                                            '20210327:032511.949271:+0000',
                                                                            '20210327:032511.970039:+0000',
                                                                            '20210327:032511.987872:+0000',
                                                                            '20210327:032512.005592:+0000',
                                                                            '20210327:032512.020922:+0000',
                                                                            '20210327:032512.035742:+0000',
                                                                            '20210327:032512.053246:+0000',
                                                                            '20210327:032512.070333:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'œ-ë3ȩƌӘҭ%ϸ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032512.160762:+0000',
                                                    },
                                    },
                            {
                                        'name': 'j΄ĸΞŊҐӰƃ˘Ǧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            295622.3707334248,
                                                                            621562.5949663519,
                                                                            933581.7872568924,
                                                                            285553.57937246707,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҽ`ҽ˔żȄ˟\x9cүÜʟŐνϹyϜƸ9źȠӁԩÚƌѴΰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 613152.5923327324,
                                                    },
                                    },
                            {
                                        'name': '˫ˍ˶ƗíΆΠÊҍ˖љԬŔͲĕɶaίʺѪυɴмȖǛʇɅΕԍƉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032512.401878:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҝː\x94ԛТrĊŘЖе',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'żĂϏǒyЊmżɺɐ˱ѭˉƁӽȉѣƈўɘ}҅Ϊ»ԕɃsĉâȃ',
                                                    },
                                    },
                            {
                                        'name': 'Ű¹ҫeěæʑӖûҥƮЧɚ*',
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
                                        'name': 'ÔѶǵͼʦμŸēăԎÈ=ʊąǃŒēй',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'œ҂\x90ƩЖÚƙ¢·Ĭωыċ²εэ"ӇǛCʖ˅Ԗ[\x7fɓt\x93ǝё',
                                                    },
                                    },
                            {
                                        'name': 'ħϺѵ¡ҫʂèϚűɺԫĲԪʽ˗ϧěǑǞпϋ˻κˉɸŭӦ˘',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ǔʈ\x86ͼЎŻǳџμѪɸ҃½ϞҴɂŔҔОѰŽĚԗpԩѩέ.ȫʟ',
                    'message': 'Ӑʺʋſӆ˗ʽӗĪČƜηɶ$˳ǣkǲµŦԥƫ҅%˲»ǎ!Îς',
                    'arguments': [
                            {
                                        'name': 'ÙǩÚΤɼθϣȮƹĿӶͶêŊēeȁѬʫɰѰʚȢӈ\u0379ð[ˀ"˲',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            776570.1135844936,
                                                                            -7682.803591202814,
                                                                            516974.08360473684,
                                                                            637529.9168702678,
                                                                            537772.275107327,
                                                                            254457.6018131721,
                                                                            661746.7554671599,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɍʺʠʴpǒͺϔӈĀѦ\x87ϟԎǵѮ҈ίӷƥɇүΪšɦˤŨɘtҙ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032513.731368:+0000',
                                                                            '20210327:032513.744569:+0000',
                                                                            '20210327:032513.757791:+0000',
                                                                            '20210327:032513.771313:+0000',
                                                                            '20210327:032513.784414:+0000',
                                                                            '20210327:032513.799076:+0000',
                                                                            '20210327:032513.813126:+0000',
                                                                            '20210327:032513.826658:+0000',
                                                                            '20210327:032513.840366:+0000',
                                                                            '20210327:032513.854035:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŅΊÛį\x8f\x95ϱĵ(ő',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x96ƁӂʀƐˊƸҝĲѬdԏĽԗϞԚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ґҧџыˣĐ\x85ŴěϻГѤÒńˁпͳԒ˶ġэʤ˕ιӴсО˱Ⱦ\x9f',
                                                                            'ǪӆҼȱ»ňÓǷʳΣ˹íɜʮ\x95ʣӧԜӿиӞϔϘҀάȪҔƍīΊ',
                                                                            'ҞơˡӴkΊϏΈĊѹ°ѽeӤ˧\x9e`þά²ӎϥ*ӯǓΎŶá.ɪ',
                                                                            'ƹ<ˁϡѢ\u038bŗєρȯˉіӊÏɠӅҪʛчƳ˷fȴϿ\x94×Æ÷˱Ӂ',
                                                                            'ȫ¤ͼшĢҁřӻЁaȣ˜ӋNϭ\\õ\x9aУƖō(ȴӓƉʦѣѻф˾',
                                                                            'ėӊΈϨ\x8dҼΥϚpËÃhҽUĀȋԂԮτ5ìÊǴšˎƝͼǇӳɿ',
                                                                            'пӞĬĿōѾʝԑƄ˻ӋЅœAĒфηǚȾǚżƁ\x94Яǀʅέԗӛɼ',
                                                                            'ʐС:ӮɃŷêΩİȎфΆҿԇȡςɪѺ˞\x82ГʣϖҌˋ1oʛòˋ',
                                                                            '%λÄĨˏнwǮsςĽҞǘȶʊ\x92ҴÚƹΉƝΈΪ¤Ƈ+ĻцǮŘ',
                                                                            '±ũ2ʶ˥ƚʴҠ˙ɤĺŠµВƙΏ>ŁЙ\u0380ӘÛоȣǥƜˤƚҪǈ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ůɏŕѿŭЌΕʁϐδӌͰʬËκŬȚǋԍĕǲʾ ţН\x95ľЅρϱ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6429918587882372489,
                                                                            -5835178272948889108,
                                                                            3559036554060303651,
                                                                            -2374902394503099431,
                                                                            4315074812766710007,
                                                                            1170510113921841399,
                                                                            8186675470370608562,
                                                                            -3841245909187944368,
                                                                            -8066744256797340149,
                                                                            737475258599123904,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԓ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032514.742034:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЃЌŊҮłȬ˛ˡѪϸ¤5İåƺæŝʈӒϜрβ˰',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032514.821450:+0000',
                                                                            '20210327:032514.840918:+0000',
                                                                            '20210327:032514.861948:+0000',
                                                                            '20210327:032514.882403:+0000',
                                                                            '20210327:032514.904590:+0000',
                                                                            '20210327:032514.926254:+0000',
                                                                            '20210327:032514.947201:+0000',
                                                                            '20210327:032514.967014:+0000',
                                                                            '20210327:032514.991950:+0000',
                                                                            '20210327:032515.016082:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'φԔɵʝÍ϶ˍȰĄΠʂƛĭϡȩϺǪҦ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'Ѿ¥ʴӠĔǻӛtđԦƏ΄ԍͼ˧ĲfĜȠȶĜԊŭĨӨŉҶͿ˥"',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032515.377206:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƴҮУѻƯƳˈȱџˢȿЍ\x8eʓɃƔɬϹǕŏ˛ӘΪȪҜύ-¦ɋò',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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

            'identifier': 'Ҿggɹĉ',

            'categories': [
                'file',
            ],

            'messages': [
                {
                    'catalog': 'ʺ˹',
                    'message': 'Ĺ',
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
            'name': 'ϡơLǞğЋȲ%ϳәƳũȇ3Ĥ^ƕͻџĩМĕƄΗƉ\x98șώȦ˝',
            'error': {
                'identifier': 'в)·ҁ<фЙɌ҂țŪЀљ΅һťqÙѐąдӈțПz˩ĩ˚Ԧϑ',
                'categories': [
                    'os',
                    'os',
                    'configuration',
                    'internal',
                    'network',
                    'access-restriction',
                    'invalid-user-action',
                    'os',
                    'file',
                    'internal',
                ],
                'source': 'ͽqħƚіɎĂĖΎţȝŲǻ҂ԙЋӮҁͲ ӧEϲͷҝǭśĒһŧ',
                'messages': [
                    {
                            'catalog': 'ħԈˏɶЁЫÁ§μйsӦϑЈɣȬ΄Ҕǌì=ʖWÒϗԬÀrƊʞ',
                            'message': 'ВÒH%ӇƽԔɸ;;ɟӃƪˑȸͺͿҽоǁϴӼĉýƩʓƥʻ¹Ž',
                            'arguments': [
                                        {
                                                        'name': 'VʼGԨÔΏїӽϞЁȚĩŦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӰԫӠʚɢџлԉŋŇįɰǕӯɄӗӊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'зҏѲǽ×ĜόϺɗ\x89ȄӲđѵÞñðǆŎϒĳҴɩʇә',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƣӑđцΥ҂ϵϴ˺ıіµ\xa0ЗХƲɈƾʜŲǍ˹Ԓӓ˛ÎȣϨɎë',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄ɗѺȸƉӹɡƐƖTǋǉʡϬϧΉɠѠԋHкƋѲÙęιѻВƅҮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȞǫϻҶðκϷӔ¨ʦɍǄϾԬϨЃϊSɳʜʂ\x8bSƄĹƧ\x9bȑѤÓ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӚКȶҊҔņȇ2ŁŘȵ˜ѕnέɓǳÕѺʭ ӝ¥ȿтӲϹ\\ȎÞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x96śʊЙѓʁϦЯу\x86ɚҖǞӳƹжɄdʭʧλ`ūƹTxĝ˟ɯr',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧΥшĊѷηįʋЧƎΨӪBǥѓЇƐϩʺ\x8bˋ˔',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɬōȘΧŴʪ\u0381ЖǏІȋ\x7fАƿϱŎɰáρɑȰγĢĚàˠԆȀƀ)',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'éƵµ\x9eѝƚˀƧū;\x96łȥŉ˾ѸҼưӀÍȿɁÚѱəÀŏѠƱҴ',
                            'message': 'ʻƻɸńŪʀɹпGќŞtĄǑ˕Ѩӭ¬ȞяĉΦƄЂ˂ϥǩЍČϠ',
                            'arguments': [
                                        {
                                                        'name': ';TΆɀζžÔÛГ¥ÚΣĮҀʝӇʂчԡϼıӘΝ¤˚ȟɍʪӉά',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԙǪȞЇΒ¹\x97}Đϐ\u0382ɄŅѸПď¬ȿѡԃ·ԥǷȄԘȭѦ´ɢǱ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӧňǑ\u0379ʶθҸԇТǌêʅĹϒ҉Ӑѕǁ¨һѧǮ˰ǡ˟\x97˜ӵg˄',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӵфȁԖɴʅԐѮ҉Ι˜҅þľʹȁӑſ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032449.263179:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷӒԏÝh8ѭԭɼÓʟӍʼ˸śѺͽΫǲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͻʻι\x82ћÚӟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˱RέԁыѷǥG_τɪĆ϶ЅķȭƩëҩň\x83˵ĘΞȧȂͶϴȣΈ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˈ;Ɠѭ΅ѭ¿˻ʴʫêǬсȞПǯǉSҺγŕ¶ŐѻƄǂÑЍƭѭ',
                                                                        },
                                                    },
                                        {
                                                        'name': '³ЭǴ_ºĥ˫ȞƭҖɲўɼÊѪǱÆɁ҇ˊ|ҟǒ®ɐˍıӚƯӆ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ēѴkьӿĒ\x90Ƈǃёљζԓј˰ԈҷƶѷȮę˽Ŧ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˹\x88Ǆ®ҳʐϞΧœÕŨΛϟѿԁƑ´8Ġɇ\x88ˍȫҦŧȤʢЭӨŌ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032449.716640:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9a8çǪǆªħ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4433020050530755577,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '>˒ÂɥɀżʹļȐɿԀӼńĹɴƻ%μVķ϶`/дґǺ˙Ɔҽ˾',
                            'message': 'őҕίRԙàǝŻǎҮɤԁЅӑ˲pӉHÛ®ŉBɸ´mӉĀɟËȍ',
                            'arguments': [
                                        {
                                                        'name': 'ϡȑņӼÞƶ˦Ĕʅ˰аЋПưҵƄҀȓ÷ȶƽö˴',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɦȥͱɒǉÜǍΜ\u0383ѻԏΙˋˠ˰ќˏͽ1ӶŲÃû:ɩfüϰμҨ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ćǫʬіӞƸȐˢΚȟД',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϚŝΉӒÌîӢɲЂңʈƆȱĈvïϝζŞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰƒˑэRλѨӪʩІӠΩ\x8aɕÆ_¹҄řҺҎƝSѯʹϬ¥ͼҰʊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7540501170745113830,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǍƏѯнҠЂÒžʼˊ.Чɚ\x88ǀƎ\u0383ƣεј',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǲԨЕʹƝмˀЅƞΦϝƴȞύʆӠƸǣĳ҄ӧǱЖď|ȱҒǨLˣ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȐęӆǯĹӕʊўɇªˤүiώӈũʸşΆçњńŢˠĐ·҇ʕҝӷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 548011.0544122654,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҕxѸĩ®©ӷ˦ȮӀɷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 548519.4323896397,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032450.427595:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӄì˶ƍƯϠѕҞЧјʲ¢ԭ?HàȳӸΔ˹ЏƓžûїѶͶȱ΄Ţ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ιӠӔʿɶӊȔɠЖJOÞϬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȦǽĻӧɆĝӱȭȨȖŉŉƼδ҉͵ёǞĢӇǿR\x8cľȪbʚҸ_Ģ',
                            'message': 'ĵΪԤβҋэҳΗ"úØӢ˦ŌƴˎԖʼɘĜʜΜϳƛƒɪ\x99ʓĆɋ',
                            'arguments': [
                                        {
                                                        'name': 'ĭɸqúːҒ±ǮƊ˕',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˻ƂȭýҟȴʄƖϳɜѧύʤɮ&IÒɮɟƗčʷӒ6Ġȭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8298090992774626753,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΜӒcԖӀǭƬ5ŖƖɉӳƹ҇˨ѨƱУΒЋ҆ŵ˰ЂϤ\x98ŌǏõй',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҺԈ˲ȈɦƤċÛΙƬʙӇɠЛԗɻŋҔɔϕӝ\u0382ДýkNө',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕʳƉѓ˨řιưГÍ8\xadРҵƤɜԒȾɭ?ЪȍlϑǴ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ǃΏϊԅѾ\u0383Ɠɕ\xa0ɫԟ˻˸˖υμҌɕǽТŃŶſǬɝƯƅƁȅ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҒƼē҆ѱθz',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 623157.307055155,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʞӭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 824156.2196527534,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʄɡŏέŽμēԧΏľĊmʋ/Ӕɗʳƞ¥ϳǚ&μŕc˦Љ˰eɜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7639310621446788921,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЌϑѩƣӼ\x91½µkʷԬŚӟǻƑȿǓƊMǔŜδʀ:ʏϜ\x8aШͶɧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ģҿҡ΅<O#ЈԔƇƞЉˈDaƨҎĄϨǐԅѤӔģčҁҿţҌ&',
                            'message': 'ŴŘǺňϲһͱ\u038bӉĎÚʹȟĴsӼŖϝˎťҧДƃӎʃƑĶǴʕʓ',
                            'arguments': [
                                        {
                                                        'name': 'χ±ɀƺȺǖɕE',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8574709221018718554,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˢўӞłҫʠ\x8bťǏӍӾǭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4039861773039135627,
                                                                        },
                                                    },
                                        {
                                                        'name': 'UԨҙɨˍВǠX\u0378ˎ9ƣ˧«ȑƼiʰőȭϮˈԫѽ9ϰPȯШ©',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Њ\u03790țѸʅѻӮ˽÷Ӟ¶ԓνȕ˰ΠԐƸΥˡСǐ\x91ñφœήУϔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҐӺҵĎhÌɯеϿ˾ƨĀΛ˝ѣҊƳˁЇͺɇ®ԘЫ\x83Қԥəίβ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѴҪΟοɉĨԆ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¢Ņy@6҄˘ĀϐȹΧҺҧ\x99ҵОΡŋŖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ʴӽԐ\x8dGCÀ϶ʇł˙Xȡβ\x92Ђш˶Ϊƥ\u0382ɎÅŧʆѡ|\x94'(",
                            'message': 'šʮˉÓ&ˎъɛņьÈʶȥţŖoìӆ\x98Đǯɻ.ӥҎҽǸωřĄ',
                            'arguments': [
                                        {
                                                        'name': '˝ҀϔĆԢ3϶ȚӜŭ\x8fûҡϙ\x97¶ʅ\u038bĈŌѕΎԖԊȃϰƤыƣɐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x93ƒŦȄΔΞʞԑ˵ŒĈɠϽȳĊԤѕţŬԕɼҥ\x85õ¹',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȰĶǧԒҪԘĸҷ˖ʌɞưsĢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒy$ԬӪ;ČŔoȽϞӎӄӣњœ\x94ƈњÔʧȼѕÚŏÖӡį·Ѐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐǞɒ^<ǐɂшŚǼƉʍ]ǙЂçȏɍФҋȱУζÛͱƶ\x94ŔҤR',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǯƚƚ\x84ӠĔōʅȏÀ8ɨѡŏƆӱ¯ÓѷˤХƴɋϛ˧ѝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԤɀґҾӟ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 64764884631460752,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȎΞɦ\u0378Łū·ɜ<øƋϙҖϝÁʌǋδĹː"жѯū`ȄзΧfȔ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͼϓŭwз9Ҷ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4525807362024911772,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʊʢơЋȂɠɀʡӺЕғѢƸ4ӰɃӼşҋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЬƖ_ҵƫǱҏȢŮāIԬҺŸĹ®˴ϾЃóҽŁЮǈχΉɤķїǿ',
                            'message': '§ˎԞӵ]\x9eԊұөȆ \u03a2џҀӏ˱ĮТҋɣʑԦ!ӧ\x83Ӛ˹ЕЌБ',
                            'arguments': [
                                        {
                                                        'name': 'ȪЙлŜϨеџͲԙ˔ΞĖљǋː˻VƣΦƃЋŅȜҚÇЧЯϨƅɮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5972402281030575386,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƾҳџ]ƥϓɤȺ\x97Ơ,ɑ*ʸӞƠϟ"Ә',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁɔżƛmɪϱҁɝɼǓ\x9dʟψ˶ǘӄнԦ»Ǧ°T\x8bŏѸˡBǎ\x85',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 28263.368779705284,
                                                                        },
                                                    },
                                        {
                                                        'name': "ͽǰӿ҇\x89ǫġ҂ҦȣҺϏƇɊЍɦԩ×ż\u0382\x9fƟ\x97ńӜø'ĕőԢ",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ƹɲӛ˄ǂǫŗһʉΦĂѱȅ˵¬ԗƝ\u0383ғ˛ʷĊƪ˞qǘɟşϿʣ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɚǍҰҵȃĞ%ŗȺѽȪŅфȅʶЋҎƐЊ¹њĤǊίԃԍɣƑΙĭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɬùȕ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0381·˩ϛԇ:ȚßõʇÈȎêͳć/ǞIѸgԅԐŸĴÆ˶ȥˊ\u0379å',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¾ӡшĄӅǆ\x9dƸƇ¸Ǒҩ҅ȣ\u0379Σȸ\u038dƈĺ\x84ԦɝðýŁíԀļƕ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ıˆĹӊуěοЕć#áĻСғϦҢԣϴπϜʵų\x86ƑϯЊӯˊӬ¿',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1863622330668992300,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȿӷ˧',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7816160681741195731,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЃƴÁɷǽӍ×Ǖǚʫ˫ԙ˱ҸˋqåұЃγđɡҀʺӽ\u0381Ȕҷ!Ž',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032453.631337:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϵƌώ>͵;¬aΓ\x9eϼΓźȬɿʁ[0ʊÚЬƽȖԃӭӀͳΏόǩ',
                            'message': 'ŝιĳϧΧǤʷцҚЋӯƿŽΞοƾκƟөΓӱėɯūјҖϭͻs=',
                            'arguments': [
                                        {
                                                        'name': 'ҤӚƧǤ˷ϸƄȧĘĹщΡÝӻʅǋɦŶż(ӲŽИДvΛѨǚͺħ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 428859.2623452727,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǝˌŧǂ\x96Ņ\x8acЛϊďʱʌ˰Ίʍ+Ҹɻǹŧаʕҋǀϴðqεʝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 196564.2524031803,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΨΕͷҋҿӐӞˠΝȕkη',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɗˉEлѐęɫғŌҬʥӃѻýˉѿwσԄś',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÂԇCЭҒ˼ԧʮР ʐҡǋÎˑԬŕϹϧhÊŚÔВʁѱɍdҹý',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032454.022343:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƻƫ\u0379ąˈˀҲҽ˜}ШĭгĤ4Ц',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ωҟ²ƷӖƛśÆȴǂԭÊȕǥʯδΙˠ8Žɘжӡӟʙj@Ȉɮί',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȬȔ¨ѹǳƺĕƧɎΛͼѬȱΠІʲĄȱҶӸĠΪ˾ҤϳĦǻѪ\x8aČ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032454.185636:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѧ8ВӆҰśСɕʪҥΐ.íĄȟεŜ]ɐȱƵ˂ȵźUηвôǬ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032454.278282:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҷϧʌƱʚƗ/Ɍ<ˇјΤʎƻˉʙͺːѷǹ/œ¶ɸԊøԧϾѮӱ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ͶȩШÜǇźĶˢņgτbӓѝȁȸщӹӗƐ˪ʏģ¨ӭUΡ\x8dǗʬ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'όԧеʤψ\x9fƆŘęėǎѦīRҺÙʉƍϖřɖѼǖƯЇԛԨwɪГ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032454.456327:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɼϜ˥©ɗȊǧĹѽé|bĘ\x8fŃQĉȌǊŻȽѐWwŲĦ©ўѿԔ',
                            'message': '\x9cВȮʩˤѶѩƎɾΉѹÙ˕α¡Ȑ-KǔȮǸѕͰ?ɬʴÔİӺ˥',
                            'arguments': [
                                        {
                                                        'name': 'ΘȩûОЅȷҙǖϡ҈:QʚƠȸÚŌԟ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǣ˥ΤӜǍ>Е·tƉĬ\x8dͽĩΚѾÄз©Ҡӟ¥ʉˉƘԋǏɞɜƒ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ПxŬ\x94Ȇı\u038dǡïãА',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6706154711231367765,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҭ\x9c˖Ɣ^Υуʑβл΄ͼɨȦƭЛԘȈƍǍęˠËɺӐЀЌǈӥ\x92',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˯ʓżɰĸ¨¶ñġЕʠӬӚə\x8dȞѯѤ˚õȥҁӔѴґ\x9eԘŵȀΒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҄ȠqŗѠɞˑƺĦĶ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƴԨÏÅzЌ˥ǊҬ¶ЩЭĒƼ\x88iГʙɽϓTʭҥVϔ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʶЩӨвҬǬƲéá',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032455.049782:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "ӝƩ˜ÿɠσĴҗđʅȌȾĒʥņN'ӏ\u0378ҲƙɴӐƤŵ˕ƆҩϴĜ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҶӗӰêΈǾɥɬɑɑі"',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯưΐņЅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'џʹФƭʕӪӭ\xa0ЅȽ\x9cĶǢ\x88ˉѶƥϚÄӊȬ\x9cԨʭš˶ƥРȦĉ',
                            'message': 'ɛęɎҸωħǸϣȔǳη˼ұřќʁ\x9bϭш4ǟÈ϶ԡ:ƒĖƂξҡ',
                            'arguments': [
                                        {
                                                        'name': 'Pȼ]ѽĞƹѕʲ\x94ăѡҮ3НȜǬӈǖ\x9fɅŖ`őŝўоĎ+Өό',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӎӌͷŧςèҒɋˌϵʠϜƾƞʎ:ŇƚԤƷԈ˫UáȿдʙЄ҈ѽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӄʒʕҷȋȟћ´yӆȚĂΤ\x8bĠʰB:Ϲнβ;þΞƒůĿίЌӪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҸЃ͵ȭΨŉԜȧκ˗ϪĨ҂Ƞȝ¸ɛδϕƑЗɌʦºØ˻гѤцԉ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 299449.739135185,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϒʔŇVĸʳ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɢȹ˻äϩwЯƙϮEÄɢ;ƿҰҧϡN\x93ԢβЗvӜzξˆɛœԢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˝ãѯEúȳрCÿ8ƨˍúƂϱҠϚġÍƤΓɶŇǚȅǊΜdҢϡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032455.946440:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Д\u038dĔŦͻɷƩĸПɤœȁѼǙʗ˹¬ŖҬΩ˷ӨäɰѺœԤѓ¡Ő',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǉęӴΧɉζґ\x9aɍκҬ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 979069.6264743181,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʌc',
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

            'name': '\x9e\x89ä',

            'error': {
                'identifier': 'ńßŽБԝ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'Ԟʠ',
                            'message': 'ȴ',
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
            'name': 'ʫɁπȱҶǒҽxэ˸ͿŦʈŇџЊØʘӮЙV¨˗ŤǫĨǄbɷV',
            'version': [
                -3265902597056436686,
                -576842757981396743,
                -1909211257926534632,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'δƅļ',

            'version': [
                -3605183915872750429,
                -9175703188214413781,
                -4105180217662786343,
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
            'event_id': 'ϫňˮȡǪǀĒʳԘDԤʧáʡʒÉΫєƣɥͷόYPӉѽҠĠԜɳ',
            'target_id': 'ȽNȠÍƹƾüǑʅїéϙɡѨωɣԚȂϛǽoʵŧШˮȻԒĲɸr',
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
                    'event_id': 'ћ\x84ϕŜΰÊƗ˰ʓŚӣЭӗȿŪƔYȫÓłӁȩ¶¹ыċ˅\x8eŜΖ',
                    'target_id': 'ӨȪŉĿƕȕųɞƗѽʸҦąɬβӨͲ_ř|ŮӕнǢiǾɝԭŀҐ',
                },
                {
                    'event_id': 'гȳ˺©ɈʻīҼυʜөЧ\u0380ϙȗ¡Pӳϐzʴϙǋ˚ҠæȜөМŸ',
                    'target_id': 'ӢŵґѾԩñśǆǻŉ\x94ǟˀϤɄǯP\x97 ʿлԂȷ͵ӽТ҂ńȭį',
                },
                {
                    'event_id': 'õъ,бȔ÷íӉЄȳmҘB1Ĭŵȷ\x84дԆĿƈ6&ƃŻÔÅêɾ',
                    'target_id': '´LÎӳͻѕ[hѴΉ\x95ƫђʌͻ҆υӥϷɽ]ʳɝ³MʿʠǑІԗ',
                },
                {
                    'event_id': 'ёЧεΚ˄\x98ìʜ©ƯǺǮ\x87ŒʶҶѻĭôҝOӇȘ\x8eƶљƒÿǋӺ',
                    'target_id': '\xadɐҩǩ¶ƥӰ¶ӗϏϧôСШ§Ҋţ@ӐџŭӻӐʹŏѲҚń˖Ċ',
                },
                {
                    'event_id': 'ʿΜϪÁҬрčĠƦɔЀɥ,ÎȱЋԒqԝɑÍ1πŤΣĸɳ{Ҋҝ',
                    'target_id': 'ɋ$ǅȹˊʓýaåɼѠ½ǿΘαŢӣ4ˬϹŰϑɸ-Ͳɨӷ˨çȨ',
                },
                {
                    'event_id': 'w\x92Ҕ¾ԁϿΙɡсΛ¶ŘԟÎʘǚϪMҮǀOȻԟCm˽ѹ}ѽĊ',
                    'target_id': '҃ѾŖȧ҉ƖɲѥȝɌ˵ȢӔїʒϧǽʌǡ·ԚҔłѨǑ6ĿƳŭШ',
                },
                {
                    'event_id': 'ΖΚѿəФɕ1Ɇ˚ɬǉ !ɱӈǐʈĭȘ0ɜά˚ԀrȜƼϯƻØ',
                    'target_id': 'ʶ°˖ѥ˲ǨˑŬÇ͵XZӠϊԤрҊȉȉήTЍʫŌӴǝĞЩ͵ɷ',
                },
                {
                    'event_id': '˱ėƿ\u038džͳƉѬȏѪÉí\xadηŲYυӤ(ǲÃψϏξœˌơƵžг',
                    'target_id': 'ŅĞŽ\x95\u0382ΰ½˱\x90ßʪɯȭˉ\x84ӷɼʉ¿ãпȏĈœƛǰàĎҥϠ',
                },
                {
                    'event_id': 'Ѧǚ\x95PɨȟGͱΦ',
                    'target_id': 'ɩǋ¼cœϛƒω\x92ъΎčӁ϶˰\x81˺ɜһȸѭεсԄчӘэˬѭ×',
                },
                {
                    'event_id': 'ʼËТĔɫӞØҒӿ6ΒѬÇӑöͶҭɠТƴȆǉȈчĀǐԧǠхǵ',
                    'target_id': 'Ȝ#zԖ¦ăұƪͼɟťЪǿ¯΅\\ɵЌͶңёԨ˼£ԔɦҒԦѳԖ',
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
                    'event_id': 'ɳɼϖӢԈǨӴàƨɿ˒ӣƑȚƱӶǕӲɶϘș҅Ńι«ӏͷΔϿь',
                    'target_id': 'ȨʏƳҢԛǝ˔˛ǛΆЂ*ԁ˖РȉǡφÀґØʌǈӐΓR3Ϡűѣ',
                },
                {
                    'event_id': 'ӻlȪ¶ɱɓȪþ\x95ȕ˲Ҫ˵\x9cÖσчǙԪβȚ˲ɰҚ]ʙû˘',
                    'target_id': 'àlŌɡȩүҩԗÌϟʢçӤ\x96ҞƈκȷѠΒҫ?vǣņxÁňŮʛ',
                },
                {
                    'event_id': 'ȞѬŻĶɖ6ѭȊ\u0382ÊӦ¼ʢрÊѬҗŷɅǃ\x9aVѭ@\u03a2Y˦ѱ˨Љ',
                    'target_id': '˻ƎзȮaНĎ^њÓÒ\x8e6ѴџɾȿĜƄϚ˓ȋ˪Ѿ\x93ɸȕĎŸɟ',
                },
                {
                    'event_id': 'wҞ¶ćěΊĕ\x90ҭĴԣÊӈȩȫȤΎѠҲŞҲSƞÜѡîС±бʋ',
                    'target_id': 'ȚъǭŠҒǵbǻxƉȲԉӍλԓҁĭř_ԪɴȟƌҒɽÂĜ+¾ƴ',
                },
                {
                    'event_id': 'ιч8ǶȽ҅ҙêυŬđϋзӚ˳˂ͺʥŕкʦɋŗυǐɣΰ\x93Ŧѭ',
                    'target_id': 'ϛџɽƛhЮЃҘйȒӥƒĵΗԣƼΠʦРцȏǰƦƂ\x80ԭϿĢҏҫ',
                },
                {
                    'event_id': 'ġόϠѝőàѪgŨѹΈAɍԗ~ɦŵϯɉǕúиϪүǸHȒԖͿ',
                    'target_id': "ϵ'æϐԗɾʈDǉˀɯФ\x84.ʚҒδзïͱêʊ.ˠ¿Ŧюˠҏ˷",
                },
                {
                    'event_id': 'ѭ_\x98αʼ˖˙ĀϭʂԁӃĖԈʀï>ԔÒˍѝȯ¿ŀԩϨӵѡϒh',
                    'target_id': 'ØǟԍȞ\x92ȶƜáʀ»ΝҖāʝҪКɍМɎ+κТãC˞YϞɯΨΠ',
                },
                {
                    'event_id': '¦ăǣţξѦSÖŶÚӜłɐԈӸȯ-ɷĻƤҺϴÊŇŕƦЍXϏW',
                    'target_id': 'ǊуɱІøƥĵ˒ŤѓMĎԫɔˉKћ\x80ƏϸЙǟӖʋџӚӝrˠπ',
                },
                {
                    'event_id': 'Ŵɼȸ\x94Ͻԩ?ɾɻ҉ëΤһ|ǓˍϾʺԥћˇJі҈ˡ҆ƀ˺ö1',
                    'target_id': 'ƴ|ÒĩoӋƤÊʕӯφӟ҇\x8bǉӨʺƓӓЇԌvƭ»\xa0ǣƷ\\ӾӍ',
                },
                {
                    'event_id': '\x80ŽѿҳƄєμˈπˑƴҩAўßȇСϣʯЁoϔѨǆǞΌɵ˯ȽǙ',
                    'target_id': 'ˏҙ2˽ĩĳ¬ЏЃũӴɨ>Ѐǂԓŉƅα\x8fǕ~ʒăŚƊʒιΥƏ',
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
