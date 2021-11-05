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
            'locale_code': 'ɰŵǴȖʷ\x99f',
            'catalog_name': 'ȊĄԆԋȣЙ0ɅѓъƉ\x99ɴĔҺɸΙŰ҃Î-¢ǜīӵ÷ƀ¶˧Ͻ',
            'message_file': "ӅŔ4˨ϮϹѓIΣE'ӷΘǰ;ξȝǾȮƫƆƎӸƧȶӛçȜϢҬ",
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': '҄',

            'catalog_name': 'Ǘȧġ',

            'message_file': 'ɕŞ',

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
            '$': 'ͳϷɵŬşԗǠȘʁɸϓХϚφ\u03a2#ɝЊӷűѹȴŨȼˮЈшʜǘԔ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1028483866426084229,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 285964.125360767,
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
            '$': '20211104:182738.681413:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'âUǗ˜ԇԘÅʕſ<ԋȈҠʐ¡Ȳ:ȵ˱ĬΦϗʵłƣǷļѹĸѲ',
                '\x91ϩӑӏ˨ҟХʞԠŉVƇїȱƓΑˈʞʡ˗˖˂ϔǿȐĵ©ҙαˏ',
                'ø˘ǸÙҒʷΗҮԖƐÊҲ#МʒšѓҗgΗƯˆЗ˃ɚƪGþǹï',
                'ЉϽ˻ȀӵȮ#ŚƎίʑƔҝԠrǙȭ˓ЅзӷȺҨō{Θ"ҥȤʰ',
                'ƓғԔΐİÍ œĶОǡ˂ȚʒͿ\x97ͽăʶȏƉʱƧӘрɟĔϏčЭ',
                'îЉŶ˄ͱϢЪԤқȢɺӳđΣѮԊӑġΒnʪǡčîÊƒƙҗґ˥',
                'ӻȐ˛+ìҒǱΈǍăŐҔˁưǱӜгzɺЕĔƅͻƐϞʹG\x89\x8aϣ',
                'É˾ВМʽɌǧӋś/ΑßеȩĦřˑʨȝϚҫʽк>ЈѹϷͳȶ5',
                'ψѫĖǁӋħƭƅƕμɒ\u0379ǰüɧϛɅīʲƈѫšˁʐ(wԧ¡Ѵк',
                'Б˥\x92RҤʕѭÆΐ\x8eĩVưέӂ\x98ʇǐěӪÿȩôԉβǮоҕ/π',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                8012569342853807761,
                -8105258207013327056,
                -2304761377623197606,
                -142276339856163202,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                435646.3298274885,
                455375.54422636353,
                892223.9791797127,
                393795.46574533195,
                389310.5626272269,
                -1042.059582828806,
                708212.3062293254,
                73501.2040555666,
                72603.26181323433,
                -35556.16877826892,
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
                False,
                True,
                True,
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
                '20211104:182739.567036:+0000',
                '20211104:182739.583875:+0000',
                '20211104:182739.601088:+0000',
                '20211104:182739.618468:+0000',
                '20211104:182739.635599:+0000',
                '20211104:182739.652191:+0000',
                '20211104:182739.668758:+0000',
                '20211104:182739.685588:+0000',
                '20211104:182739.704760:+0000',
                '20211104:182739.722668:+0000',
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
            'name': '\u0378ʘ,Û϶ҡаδǝһȇê',
            'value': {
                '^': 'string_list',
                '$': [
                    'ԎϼϷ˞ƒӕɪʒΚ¦Ȣ\x8bˁϗģ3ɶμ{ϛҍиϽϭʔяʘ\x95ĻӐ',
                    'ӴѹщǵуϜα˓ŠҚeYʱĘàЩӣӯǽǾ0ǋÑɕˏ\u03a2ēΆшǎ',
                    'ҬȴȓҏțϴΰΩ¿ӄйȲϰ;ӓԤƆ͵Y°˩Щǥ˺Ŕfâ\x8eӫŒ',
                    'ϖаǳŘɇǮ˙í©ȼζâғΣϫɑɭƇʇp\u038bӴӯƴɼǨ±є\x87ǵ',
                    'ѰҤŹԢȜʉ\x8cʟ\x9cŽ!т˒ňӵŁƠ\u0380σɑƥǾͱǰŘü\x8bкǣϺ',
                    'ηiĤñԣӨБcˣӉΎѢʇȶʀÿ\x9bͼɴȟʗɑŋѡΛϞ§{ҋɈ',
                    'ίӃʕŌСоʵĵL҄ɋӜӐ¦ĹưĻĵϽäǩԛʃđХɕҥçɯѳ',
                    'ўҥǘ΄ǥΠĐ˚ɄdϐͼňԂоХүπªƭƁԣѴˆăȉѠG˳Ȯ',
                    'ǳĸȁϿŪĹÈ˨ɂǼʮĉѥ\u038dʹȰťñҴ\u0383ēϸj¨]ʐȣиɉP',
                    "ӗӸàϘϮȲϢÛǲ-ʍҰǅЬу˧ĮЯg\x82ĤиÿǅͿӷԠr'a",
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʔ',

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
            'catalog': 'ʽȞʔρОǽ˹¡ɋċӟѓǖ@˲ɻ\x8dюǒϐǆѯНėѪ˫Şύʳг',
            'message': 'ҼǟΤҵÙ\u0382Ϣ҉\u038dÑ\x8aЁЩ©ҌԓǾ·ҽ\x93ԧ\x80\x8eˀ7ȚǝȝΥҝ',
            'arguments': [
                {
                    'name': 'эЊώϘǢƔȿƵϫȾʺӊȉĩдūΚ\u03a2ʇФǻ¢đðƎ\x9dВτāΡ',
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
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ϗ϶əІCæŘ\x9a˰ƂϷ\x98Ʉˊùhɨ1ŁŷŽÊ6',
                    'value': {
                            '^': 'float',
                            '$': 492068.4963732087,
                        },
                },
                {
                    'name': '\u03a2ȩ;ҟȖFϋτ˪Ӹё_þƩA˦˅ҍ˦ȤҚĩŇϧƌ˽Lɤʺˬ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ȃӽ¡źԤ+čŖŕϋЖʮиķΩӎӱÁȒAÃϘǴϕϢȳԌӯ\x86Ђ',
                                        'ϣȺԧԁϺҙӇʶǚAԆfÐиɓñȭµŔ&Јə9ӥȉYɮʰѽХ',
                                        'ÕïƓҩƲȳǸԫȔϩұҹѿԛʉ\u0381ϳŊˡƄţҬңϬϲӆɴ҃аŁ',
                                        'ǊÂѥ\x9dʝӾŲŻƛ˗ǛҍɫΖԎȩǿМƛɆ^͵ɗÚҺǆĽǷƨɈ',
                                        'ûϦˇRӋŃϦɜVňǇ7ˈΧ\u038bÑӠĮõ¢ŐȫӻϡʳOԪφšŕ',
                                        'Ԟ>Ǡҏҝȭƨ҅Ģĳ˝ԁ½ЊӤKƠΡЅȱŵȽȚҺϚÏ˨ʱІО',
                                        'ąҵŹӣȢöѺĸ˨˙АːɣȎįNДʟ£ɺȵƅԑ˼ɇƐ9O¥İ',
                                        'ӻϛѦӻПъÃԃŬƺƮƸǡЛѭͼɏȼ\u0378\u038dЭϫӹԝƦҪlũ˱˓',
                                        'éя˔ȔʤҹѯȚȨҎϠԡIŻʼӚ˻ĦȃԦқ¤ƎǠʹŴ®ɥɒA',
                                        'ΚȆɨљƩˁðșҢƼ\x97ȣΐӊЍŁӎȏιŚ˞ʬϻȾ\x9eҐ˭ҟʢŗ',
                                    ],
                        },
                },
                {
                    'name': 'ԇΔʛТοȶȜ\x83Ί5ѪԪ³ѝƺҝšɬΔҔǞϴðÍķĩ\u0383ϖÅ˶',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
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
                    'name': 'ˈѵȹÏŤǐтţѰx˗ӽ\x86ӻӠ4\x9dԌҍҔ˸ϜǻҀJЇˍҺҙӿ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ȃƥλƜʅʙĮʌδԃѡΧғѕҭӈ\x9fĞǝɑʹȏµԐѤһώʼ˪ʃ',
                                        'οǉЏɶɍĔΧɍʡœċӆѴ\x83ʲѐψѤƽюǍħÆ҉éŁҗëѭӬ',
                                        'ʠŜò˜ǓˑŤ\x8eãӲďȉƎȊɛȢЁãɹʸʥ¾ͰӜӐ\x82ZԘǌч',
                                        'ŎÖɮƎˀáΨȧȟɓԝсȶÄӲ£Ǒȏ8ǞǙȚMƉӹ\x8eĒɌɃΏ',
                                        'πo&ŎÝńĹϷšȽļѾʱĀι҃ʀϺÿÉ˦ͱΙ\u0378ЮКˢ\x9aʱʇ',
                                        'Ѳ.П@ŰʰʺǵԌŲŜΈʵӔáŏѾ\u0378ɗѣːʃôѥВѐǚГӗг',
                                        '˖˘˲ǊÑ5¾Қ˰ɞӣΊ˔\x7fƌǓɴǶ\xa0Ȟżŷ\x9b·ϖĘѯʧѼʰ',
                                        'GĉНʞȊȜžưĬ*βѤҮɷѲ\x9aʣԄĦÒӵɎ˝ɩǭϭ˼ҮÔɵ',
                                        'ţDȌĎЙυӴз4ҨҷƁϩ˩ӛζǑ\u038dŦѪƉǇұјŇȽŴѡЕú',
                                        '|МѧɟѝЖҎɴљČЈ\x88·ǾÐҲĒʡƣфѽԇ\x95ŮǰˎԋҰӜȊ',
                                    ],
                        },
                },
                {
                    'name': 'Χ\x81ҭƝӖĀʳϻͽЩQʤЦɉ\x96ä\x80ӊ҅ʮʝѴԀƢ¾ӼgǫÀԌ',
                    'value': {
                            '^': 'int',
                            '$': -8835970115233295707,
                        },
                },
                {
                    'name': 'ɸɅːƷȨӲҩƱԂĕ)øˀҰŊтθOҥoǷPҾʁϾѲόŒƬɗ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'Ĩ˥ƒсͺ3ƬлǇȨ\x89³ĥŧ˖lσҺ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ԝɪҏˑ<Ѿ˨ЪġŦȎǸΟÈΐńĕ$ͺȦГɥϤҽУʕɉђΒˇ',
                                        'ΘƯ\x81\x84ŉÿѯ¡WʉԨ\x84ʍԈDʐȔôαˆ˵ҝøOƧ҉ʙтǐǩ',
                                        'μv;ҴϞj҄ӉϜˤŌʢÀĎŸøΕԡζԙɕɔϤΐʼѨǲљͱǏ',
                                        'ÑƚĄǯњƅͳŮȋǞˆÛԘцċҏÂGĞĄʄńŠ¡z\xadӋѽķï',
                                        'ϐӉÕƓϔ;ɂˬłˏҋԜБŢțƬϥŵԐÖбӖ˳ǵƙϸǭŒʢɯ',
                                        'Hѧɫ\u0380"Ҵ ɂùҮƘdǾ˰ϣӢҘ°åşͿѥӄ˟ҍÑўёʋɌ',
                                        'ӗɐĿƜǂǢ˲ǀǦ\u0383\x86N˲ГϝӶӼǬˉѬжĕϜǿʒðţŎʷĨ',
                                        '˽YĊΛÀ§ϙԥӬƹ·I:Ũˏǆ¿\x9dɤQӰЊϾǺӑԔȷԖсƘ',
                                        'ϻ]ƸԦӁ¥ҲįˮЧ˩ещяКɇ˕\x81ԈĘðƧýůҞɪʋϑǞҐ',
                                        'юφɽƎмȧ˙ǔªȮЮîʗˢ\u0381ˋӋIäǾµàκӊήˣǎѢҔ˄',
                                    ],
                        },
                },
                {
                    'name': 'ķƺҢā,',
                    'value': {
                            '^': 'string',
                            '$': 'ͼжȆȐ\x95ːŔҊωѵ˛ʎϠǚȬʡѥȟĞɂƈϰȆ±˺ǺΡʕͲЫ',
                        },
                },
                {
                    'name': 'ԏԓ',
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
                                        False,
                                        True,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ʃʖ',

            'message': 'ό',

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
            'identifier': '»ӚîјԠxϰӝ_§ϐƯ\x9aа҅ɔͶƉ\u0379ЉӆԑȜͶ˳Ʉѿ˰_њ',
            'categories': [
                'invalid-user-action',
                'internal',
                'file',
                'os',
                'internal',
                'internal',
                'invalid-user-action',
                'invalid-user-action',
                'invalid-user-action',
                'network',
            ],
            'source': 'ӪфʣȖȏμͻеǭΡԟ;Ť҈9\x9e&ſҳȠњWUϊΔ%ЊİκŶ',
            'corrective_action': {
                'catalog': 'ʨҏįӯÐ\u0383˸ʳΉҙǴʆҠěЗ˖рˍʝʃŒˮӮʃ\u0379g\x9dʹxy',
                'message': 'ɇ϶Åξʊ\x90đƯˮҖӸЏзАӢÐǨŘ`ǔϏѱǆѷԊāħƎďʹ',
                'arguments': [
                    {
                            'name': '¦ʏŚȶȐÁБΠȄҵҟ˧ΔȣǒʔԮʝĩԓǌ*˹ӖǎςȆнȱň',
                            'value': {
                                        '^': 'float',
                                        '$': 970431.9989097586,
                                    },
                        },
                    {
                            'name': '\x8eЀʹŽgŭɱѮ\u0380ӢȖĂŎƚÂÖлѯīhήњȟԝȗҲʅǒɧѮ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -708250836781081925,
                                                        6702229604516540059,
                                                        -356185151770348721,
                                                        1076859088053411885,
                                                        1012865535516656420,
                                                        6178996967831684899,
                                                        7195941871054667996,
                                                        5866682761951423424,
                                                        1696572929692173121,
                                                        -73931929340837912,
                                                    ],
                                    },
                        },
                    {
                            'name': 'іηѶИӳƱѠʖ\x84ʨԑƳ°5ѭԉʇұεұŋƲԐ\x82Ɖɮǁ½Ǚ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǋΦÿшɵĴʢʽӟϭ˖һȁΤ',
                            'value': {
                                        '^': 'float',
                                        '$': 381341.73284896434,
                                    },
                        },
                    {
                            'name': 'ïԟǇºα҅ðȷɅɮϊӲɚ\x84ϋ°ƧéɠɂčȜɹ½¿ԔȩƺғϷ',
                            'value': {
                                        '^': 'string',
                                        '$': 'țӽхʋġԄ\x88ЪǑӭŸԛɪїĩҭĉΪʦơϾѾp\x9cɲҔԊʩūJ',
                                    },
                        },
                    {
                            'name': 'ɜєŇƂȮѵȔζҪĎÂӔĿȦʍyΧH:Ю*ǝ«ÏҼӺĬϴΘǲ',
                            'value': {
                                        '^': 'float',
                                        '$': 864974.7401784868,
                                    },
                        },
                    {
                            'name': '\x84ɋƅϣ¯ȹȄΤžƍ÷ϓƤ˭Ћû',
                            'value': {
                                        '^': 'float',
                                        '$': 815430.9822124953,
                                    },
                        },
                    {
                            'name': 'ҲȬˌĔɶĨҟíѧѾĸǀǵǟʑϚēɁ-ȮOőң²AԞѿě[b',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20211104:182735.751551:+0000',
                                    },
                        },
                    {
                            'name': '\x87ъӜ÷gϫȆғ\x83ķѾąҌʅ˾ȡ&ϜӅ¹ħĵtԔÜJɀићɀ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ëʮīЊĤӸѦ[ƠѬPuś˲Ґ˦ҐԜʙҚɥpϸɿЌϮƩϸǖĻ',
                                    },
                        },
                    {
                            'name': 'ċ»ˬVԃ"ˬĮʇ³2ВğӨȾȍÇȝȳ˔ʳȎцǀϩʱϏǸ!Ǻ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20211104:182735.894140:+0000',
                                                        '20211104:182735.910491:+0000',
                                                        '20211104:182735.929036:+0000',
                                                        '20211104:182735.947712:+0000',
                                                        '20211104:182735.964251:+0000',
                                                        '20211104:182735.980751:+0000',
                                                        '20211104:182735.998199:+0000',
                                                        '20211104:182736.014872:+0000',
                                                        '20211104:182736.031584:+0000',
                                                        '20211104:182736.047947:+0000',
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ˠŗѢάŭƑǽƑϼũ\x99óţаʋҲԪӇ\x7fͻѦ\u0382οėø˅Ýӄý˜',
                'message': 'FλʯȜĨ\x8dǐňˀЈϑʩĳdƚ\\+ͶҹŠÍҰ˨ϓʠ4ґӿ˨ǀ',
                'arguments': [
                    {
                            'name': 'ê6ώċѐϯԢύƹȑòƄWΊɒǆOњӎ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20211104:182739.972189:+0000',
                                    },
                        },
                    {
                            'name': 'ˢʅɱÔʲUɻǏVǒǴӅȃԌÛ©Ȳ΄',
                            'value': {
                                        '^': 'string',
                                        '$': 'ͶƌȿѯīϽμӱӹҾҮʽiʘ҂˺ȤÚɅлîÜ˰R¼ʹһǁѠΠ',
                                    },
                        },
                    {
                            'name': 'ӼѝǥÉ\x88ŎҴɛ\u03796ǔƄҤϑưѥŷƴϦč-ѮŮʀȹѣҷ҅Ь¡',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20211104:182740.108147:+0000',
                                    },
                        },
                    {
                            'name': 'Џʧǹ˰ԝí+ԛҲɂĽѽğȲϮ˩ƤϜĤŌɟйąϧŢЮĴԍũϚ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -2954586269724433043,
                                                        -560892944524993793,
                                                        -3536802886610057858,
                                                        6115010755373068400,
                                                        -5239893654772987064,
                                                        1683910019986248415,
                                                        3411879445667113542,
                                                    ],
                                    },
                        },
                    {
                            'name': 'eχ˺VGоA',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΰԋƓƋюпКɝΓϦȑͶ.ƶ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        722441.355220341,
                                                        709762.0208029088,
                                                        962977.5159913264,
                                                        426996.37862288917,
                                                        885017.2106498146,
                                                        961720.5616758163,
                                                        833337.7285301364,
                                                        233416.10346569726,
                                                        539668.9426032063,
                                                        365254.73237956694,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʫԏӪґԭΖįȵóЋƯĉс\\˅ĘԩϹΙΡԃǋцєϏā˟ҤϷӍ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20211104:182740.754992:+0000',
                                    },
                        },
                    {
                            'name': '҈ƃѫČb%ˀǇƓīƓwPԪC˳ˡɭɰ˨ɔνȢū\x8bϚҳѰƶʷ',
                            'value': {
                                        '^': 'int',
                                        '$': 3943944504251413270,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': '˂Ǡŵǯӌ',

            'categories': [
                'configuration',
            ],

            'error_message': {
                'catalog': 'ԃӔ',
                'message': 'ĝ',
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
                'identifier': 'HƯĕÝȺ˶ъ@Ȓ˯íī`ĢǦʇĘqԖӐˇЭǇƳƿшâĘ˯ό',
                'categories': [
                    'invalid-user-action',
                    'internal',
                    'configuration',
                    'os',
                    'os',
                    'file',
                    'internal',
                    'os',
                    'configuration',
                    'os',
                ],
                'source': 'ϔНiXӉԭ\x81GŃήÓKŬƮɪƶϧ\x96ɖŇϨұҔӺƠҢƺНǡs',
                'corrective_action': {
                    'catalog': '˰˦ŘːƚΞ΄×Ē',
                    'message': 'ȈĽМ4ơȿԡÈČĳʰʈԨˬ/ЦùϘʿĂƕT˧ĆɿϫĻƓѯӄ',
                    'arguments': [
                            {
                                        'name': 'аΝтϖˌMą;ͽΒҗԓͺϷÉćɚ\u0378ǍɬˮuŢĸ͵ĤŏʰȂЉ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɐъϯ9ͳОȜʳӋ¥ˑӖǣӁ˩ȑϺ+Ƅ"ПÊʚӧґϳGӪƛĥ',
                                                    },
                                    },
                            {
                                        'name': '#ϿѣŴЛǲƾӒǐԇϣеǄ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            344591.14575980935,
                                                                            727423.2206129975,
                                                                            569267.8613681147,
                                                                            956758.219937813,
                                                                            576613.5800454244,
                                                                            49126.42802500661,
                                                                            671829.5842687096,
                                                                            268618.85663322813,
                                                                            618137.0568235479,
                                                                            266483.5357628304,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŋ˾ƫӯУͱÌӅʍ°(ƶŴȪ»ŗ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 132278.9454769695,
                                                    },
                                    },
                            {
                                        'name': 'ʖҬɽkѲΊNʐЍƔɸҝвƩƯʔ˸ϼ}\x9aӠɰʲʜΚǻǩśǕý',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӢĕӦӥȩúƄʬ_;ωǲÆтPʻƗɡѺŎӌӬӄ˄ԃɼɢΦuɕ',
                                                                            'цʺ\x8fѣIăȊЀΕɦӚ˪ōŸΥҸƽɣɱŐˑҹ[ĚAƴϔÜҿʸ',
                                                                            'ϹDǚқġǏ/\u0380Dԉċʀíʴ¼ЁŬѤʹƀăϡǛ+ɞçɠ\x8dΝӻ',
                                                                            'ѹʓŉˋǂŋìȗü҅өӴǨɐˏ?lыǦŭʤĳĭ\x9eƷҽɽȥÈ´',
                                                                            'Ҟ£ѷɳ\x8fЦӌ\x99ҹǵΎˮųϛсγҙ˙XôpSΟŋѬYĹЧü¤',
                                                                            'ұțӰGʼȪҙРȌлвьҩϱ\\ӂσҶG˘Ӫӵ-ϏƟƒЩƹȄĴ',
                                                                            'b!ŐXùȫºΌɴȓǎȇǬ"ɻȿȒЪҧяҥ]Ιв¸КвКԂҩ',
                                                                            '¥ҥˋ˝ȦӌӨıϟґ˫Ȍύԛ:|Ņѝ}ŞԔ˃ǫǫϿƪϏӛφ»',
                                                                            '˅ĩZϞ\x86ʭ¯Ă«ӄΡ^У˾ǘԟɖҊˇҷĊ\u0380ʹгˋήƼùΒŗ',
                                                                            '\x84ĻĆɍԩˆͱƙʐѳ˺ɠȆ³ɿх*οϑпŽÝƠДҭ5Ҋѣ΄Ѭ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɺ±ğҺЖɝҳԢʹΓ',
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
                                        'name': 'КˮΊѐßɹΠҧйӬҠ\x86ѤԞu"ψɷɜǒ,ǙҚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǛĩâYɣθƬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 666858.7653838104,
                                                    },
                                    },
                            {
                                        'name': 'ÃqȚӁŭӬʾ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -28021.98276391749,
                                                    },
                                    },
                            {
                                        'name': 'ԠʡʘƺΚԉʎΤǏś{ǓũťҪ˹ı;ÒƵқǠɱӢ2Ƅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɎҚÉζԬӋǻ\u038bŻҷ\u0380Οϕȭǀɿ|P¿ˌˮˍ¤ɜĒΘɇċίǞ',
                                                                            'ƌ˫ŪŦǣίҹ΄ƏɵҝȋkɑѳÜî˰OҕʏǤϱҒЊĲϥΨ~<',
                                                                            'ӯº6ʄýҭƀɧѥÛűǀ˺ŏƶχπВΏĘϩlѺϼΥǝgªĂĴ',
                                                                            'ϓҪҴԐɹȄͼ˻Ѩ˳ˊȦș˟ŏÕĺџʷѴΨÜӻϗ«щlʹΚȞ',
                                                                            '"ɌѰȏЫƅǋ£ɈěǿΖơƍЅԎ\x96ȶѼƋĎʋĄʚ҂ťéԠϪҐ',
                                                                            'ӫ\x9c\x9eϋʻ˯ϸ\u0381)&ϴɆΈĉêӷͱʯȮӻƌκфҺǖѹeʢĔ¤',
                                                                            'ȃƉŅTҰÇJӈ\x9f҂ŴŴ*<¿ϷɐȖΪ¯ǯԨыю˅÷΄²¦ğ',
                                                                            'ҹѽϑŲɲʻ\x89ϠƻΚҶҪʚȳǎпԨȭʥɆˇӢƐrѵǢÕȑ>Ϡ',
                                                                            'ãЛ"ΉȌƈʒˬԟƣ<Рˤϵ\x88ɁˏΘÁΊк¸GȾǴȆҨ\x91?ў',
                                                                            'ƒѷѴȷżŴLӗʬƶ\x80ʼ\x8a\x9eżʕx^ĬǌџÝαтЙ҃äҙÁԏ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѷʕ˵˶г˳˽α˻ӎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
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
                        ],
                },
                'error_message': {
                    'catalog': 'ˉќǻԚÙdµê½ЀѪҿčŧƴʲ\u0381ļƛɠοǭΏȂĄä\u0379łȤҧ',
                    'message': 'ʆӇԖƫvqЧНƵԟȈ˰zãŎìҺӫ³ҼяӠȊϚӴōʉϹӦϙ',
                    'arguments': [
                            {
                                        'name': 'ĞƔɐоɹƽ/ԕŹӐȆʼɟҕѳƙĴύ˰ΏŞ³Ϳҗ{Ҥѻ˨ũZ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7647973813933714882,
                                                                            4161148101546177172,
                                                                            5937690101811278730,
                                                                            1256801041786771057,
                                                                            -6332679265204646654,
                                                                            -2678306452666834279,
                                                                            4594639914445032360,
                                                                            8454300180706045723,
                                                                            -6151612442783962658,
                                                                            1254649014061629396,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʲӱϿƇ¦øɣҳȩƉJK\x81ѩƨǹƫғӼʕƷͻDѡƞŏѮϦǢԈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Rʎϭ\x905лʮ҃ҙǙʒƣÀÐ-Ң==ƸʌÍ˵˫ͺϸƤΙзϬʣ',
                                                    },
                                    },
                            {
                                        'name': 'ӞİзğԉҼÜҺ$ͺӔˌȴβţΝі˓ˍ˘¡рȈɾӧæеƓЏő',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182733.375063:+0000',
                                                                            '20211104:182733.391622:+0000',
                                                                            '20211104:182733.408797:+0000',
                                                                            '20211104:182733.427292:+0000',
                                                                            '20211104:182733.444758:+0000',
                                                                            '20211104:182733.461424:+0000',
                                                                            '20211104:182733.479743:+0000',
                                                                            '20211104:182733.496586:+0000',
                                                                            '20211104:182733.513199:+0000',
                                                                            '20211104:182733.531250:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϙ(ɲƱҼƅ϶ǰϭţȣΣъúԓƞçȗʈϺ˗\x85ÝΑѻƨʔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -96995.90411349593,
                                                    },
                                    },
                            {
                                        'name': 'ҎҾЗɽVĿˣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˊȉáʎһ×Ɗ\u0378ήÍŮ8ΟоΠ\x96Þ£ӱȅԑԟ¦ïeŭƑNѰ\x8b',
                                                    },
                                    },
                            {
                                        'name': 'ҬѨĞƫ$\x8bίӲӟØ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -37998.28819393049,
                                                    },
                                    },
                            {
                                        'name': 'ΓѪɎ±ҒĦůʵиəсǫΗ',
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
                                        'name': '?əPЗˎ˕ѫÎψȈҒO7½Ӹ˾ϖĀôKǕȁ˰ѼʱԧͱΑèɛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182733.959784:+0000',
                                                    },
                                    },
                            {
                                        'name': '˨ëǍІΔԐɝÁЫӷǖ?ͷÚȜˊѢģԓτĲΓҸðĊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɡ¡ԥƈȣģźԜǀӄˬϻãƠӞɎ>¦ɍԃEʯҲŜƞ\x91Ⱦ8Һŀ',
                                                                            'Ϟɾ³ЧǘϚˡˈćʄԭϫ˝˖Ų;Ǳ¼ɒƎȎЅԋϞºӣчʣҷþ',
                                                                            'ĕǺΆԂԎΫ˞ҝмҶƯ\x92ÐЕȀЏ>ӮƩêɢˀ\x89ǘόӹҒưĔӻ',
                                                                            'xdÒʋ0ƌƖǈӑƥ˔ˌђɫËҾɏԏˣυʻǉÎԘͶўıƤɁƨ',
                                                                            '\x93ɄØҦρЙзĞѾɨȪǰԩŒXӼЏ˸ƩĹˍԁԡҒǊàΒƎώć',
                                                                            'Ǭ˞ǦƙɔǁΦЉԭŷŋxҺʻҸʹșǣӋŠɼâәΝ·İɧѷұē',
                                                                            'θԞȅΐʹÌɡЙbˀʡѸЃΩƊĩӡ͵Ԛ,ӂГȣɈȶяʹvɛ\x90',
                                                                            '˫ѴԊϢ˟ԗōѷƧƗҠǩιkԙ˔Ņɡ½L»˰ǥ¤ϡȆǍԫҸԫ',
                                                                            '˰ӳȯοǥӱ˽ŐɭɈӞҀνҤН˽ԡϽԈӜѣӕɑȖ¦ɷӑɗɽφ',
                                                                            'mҸČ\x8fɌ¢\x87ӹǺұΐk(FԘ ЪАзĞÐ(QѵԕхDì˩я',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '±ӹ˝ԮЊνҫӼ\x8fƟ˙\x9cϲ\u0382',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϖĽƁёťϠMɑȋ\x97ǩѭ\x89ǨϖόҵѵΚ˩ćгԤmƓΟʟŞѝǊ',
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
                'identifier': '˅ƪŷQÕ',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': 'ѵ{',
                    'message': 'ɩ',
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
            'locale_code': ')ι·ʢŖßʏȊѦ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'º',

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
            'catalog_name': 'īñ˛ԀĺȡƜǅ˥ΗҺ\x8aӞüãήԇ®ØˎÈƌÊ˹AҐŁɬ\x97ã',
            'locale_codes': [
                'ÉɲЅԧ',
                'ϔѳ6ӒÍAʯ',
                'ěѬȃŘԪp¦ґ',
                'ʦӍB',
                'ģϔэ˧Ќ',
                'ҤѴƞǒ',
                'ҹ˂χѕƏťɈLԍ',
                'ѤȏΦɉƓƋϦĬƨİ',
                'ʓ',
                'ġǆ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ȓĜx',

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
                    'catalog_name': 'ԡϾÓʾʵèɹĢĉѡ\u0378ˊϾҧҏɄÂӊɬǍsѥɱÌϤΩ¶ͶΒӂ',
                    'locale_codes': [
                            'Ǳ\x8aИӍWԍǾϳ',
                            'чҘӚʞҀʮҵ\x9eɿƁ',
                            'Ä0',
                            'ȃ˹ңƞμ',
                            'ɁҢāLÝѯϻ',
                            'ʤԊƸ',
                            '\x7f',
                            'ª˃Ġȫ',
                            'ɋ˅ǩ;',
                            'Θ\x95ԁ\x96Ǿ΄ϼ',
                        ],
                },
                {
                    'catalog_name': 'хȶ_ұoƱ\x8c˄\u0378GӂИȄЁ\x98ͿЖĐ˳xƾǒǆӜ˕¬ζїMɷ',
                    'locale_codes': [
                            'ѮηĿȘčԑŎ˧',
                            'НĚӼŞ¶Ľů',
                            'Á',
                            'ĨԣЛˡ',
                            'ĩźǜƝćáǭϭÅ',
                            'ʵȑɋŃʷɹÌӮ',
                            'Ѥ(Ő¡6ʢÕɪŬЗ',
                            'ԆW',
                            'ԟɼԧў(',
                            'ΧӣǐVǦ',
                        ],
                },
                {
                    'catalog_name': 'Úȫə¬ȟʁкʖɜǠƱһƭҧĈΫ*ϵѼǖ˰ЯԒàʔйΊ®˽ļ',
                    'locale_codes': [
                            'ŝˆźǹņ\x95ήʟ˒ɺ',
                            'ǫ¨ĨȚΟ',
                            'ϯǥÎчӾȞӵǤ·',
                            'ѐɈЊ˺',
                            'ȽàѴϧ҉ӑĵΗ',
                            'і',
                            'ΖӶϼʈɣҞ',
                            'ʼҧ',
                            'ʵľͼǚɰɟϴ\x8bæ',
                            'ƥ&ȉΞʨΉ',
                        ],
                },
                {
                    'catalog_name': 'Ы~ӸͽӐюŤęѾљ˙ӣÌϣĖǾԛϜ˚$ȖŏԥԖԗПњ˓ԣȀ',
                    'locale_codes': [
                            'ǜҚǀȍʦ',
                            'ϻ',
                            'ѵ҃ȌȅǱÚџ',
                            'ѨϾ}ɇйϲӓƱ',
                            'ɗ!ʖ',
                            'ǝρɎ',
                            'Ʒ\x8eʿěÄɎѨǦ',
                            'ɟÉȚҊСNя',
                            'ЈƚýȤȮ˞ˡԟ',
                            'ŋҼƃҒϪ',
                        ],
                },
                {
                    'catalog_name': 'ěΈԂǥÎԢϫ×ƯԄԞĺя˟ǼǕǅьƥȾӒΝΚe˜ɌošƆǕ',
                    'locale_codes': [
                            'ŜҦ˪ςʂԘı',
                            '\x80ѓҖсĞîʳӀ',
                            'ʶЀԃǻ`ƅʐӝ',
                            'ƵĠ',
                            'ԏҡӛɗǴ',
                            'ӐÎːƥɡ÷ŖĢņ',
                            'ͱŅ˯',
                            'Ƣ',
                            'ϧжJ\x82ɧʹ͵',
                            'ŜƼ',
                        ],
                },
                {
                    'catalog_name': 'î˝ʣ@ƸƸοƀӨƕʠdɄȇһԏ\x8cőŗǃѓˏ`ǎÅТuʉҸǴ',
                    'locale_codes': [
                            'ì',
                            'ҟƖĢǓʴšùʀŊɧ',
                            'ԝşΧxþƃƤȶ÷ҟ',
                            'μ',
                            'ӷnţ\x9f1Ƶ',
                            'ȢPƕǥεͻ',
                            'î',
                            '5͵',
                            'ӎ',
                            '\x8eѡǚАϚ',
                        ],
                },
                {
                    'catalog_name': 'İǈƦAȱıԫΆЗ´ɕ҄ȋȅňɔ˧Dˊ˯ɇɳʥȕҬҨȻԁĮʲ',
                    'locale_codes': [
                            'ʸҼ',
                            'ӆįɉɫ',
                            '˪',
                            '\x87ʆ˺·Ђƾ\x85U&',
                            '°ǴЕȅÑ˥øėӰ',
                            'ϰΉІúˇů',
                            'я\u0381Āђ\x95',
                            'ūJïҍȏŀΆɏˤŷ',
                            'цȖҮʓǷЅ',
                            'И\u0383ĜǊÛҬЮ\u03a2',
                        ],
                },
                {
                    'catalog_name': 'ƓǘÄ˫ӓκśӕ\u0382Ӎ\x9fʷ˟ɅӯЇϬŨѳ\x96ǐКȓɕ˵ЁĬȵȅĝ',
                    'locale_codes': [
                            'ĉİö',
                            'ɪɻÑȩΑɿӅ',
                            '˳ʅşʐŗɡ˾¤ͼɆ',
                            'Öˋ',
                            '҅Ѫ˷',
                            'ʠЩʍĀʣxȘҏҵĠ',
                            'ķъƖȻȺғÉŖ',
                            'ľΟǢ\x8aѳ',
                            'î_',
                            'Ƃ',
                        ],
                },
                {
                    'catalog_name': 'Ƹž3ѵɡΖ6ёŌfxԅҦʾ˪В˻ȊÿħåͽƚZӤжɘō\u0381ǽ',
                    'locale_codes': [
                            'Ϯ',
                            'Ɓˠώѱ\x8c',
                            'гʶȚǺʵƺ&δ˒',
                            '˺¹θΠʅѮԆ\x9a',
                            'ƮƠȻ',
                            'ӪʩԁԂ\x8cВƴΜӆ',
                            'ӒƽͱҸӭŪ',
                            'Ҥ',
                            'Ǳđȗͳ\xa0°',
                            'ŷӷϞѺ?',
                        ],
                },
                {
                    'catalog_name': 'ϔѲʧ˩ʽԓöǴċğĢ8ɸϳѸ"ǢͺΣǈΔ;^\x98\x9dkŦѝʍä',
                    'locale_codes': [
                            'ѻǷǔįʏ',
                            'ǧҝ',
                            'ȄВϑŊӿёԮ',
                            'ҴēÉҪ',
                            '¸ЃΗīзԕǮӗĩ',
                            '+',
                            'ʺȐÇćǗŃӰˢԨƥ',
                            'Д',
                            'ɝ',
                            'ĩȑҼĺɢɴƢ',
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
            'name': 'ЈĦɇĒмӧʁһÕʴο@ԝŗ˃ˊυ\u0380ƕɓ\x89ѵÆƝȦˇșӶəȸ',
            'code': 'țT',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ď',

            'code': 'ɛ',

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
                    'name': 'ҞƽÁӳԖԉƊáŁϚêȸѨʲѷϿÂВǤӂɃĽȈěbͶƻȪиλ',
                    'code': '6bČɅ˭5Ǳ',
                },
                {
                    'name': 'ƔԍҳԜöӌŲƣŤҦГɻ˸ǕĄhăɵхӟ>;Ϧ\x8fʁȄԦҧӤҫ',
                    'code': '+ǶĲ',
                },
                {
                    'name': 'ƍˬΫȅΕάϰ®\x9dҦԅӬʳҀˎҋâǰɏ¦ӲѸŕшϒԢɄ4\x87ȿ',
                    'code': '«ȦÊłԙЩ',
                },
                {
                    'name': 'čįǅʖԣϥѼƸíшǵϚmʗSѿʧȼȊŏʪԞЩҰįŧϙϕ',
                    'code': 'ŉĺ4ԣŒЗȖƣÚ',
                },
                {
                    'name': 'ƣӖƮRԤȄϪѣØԦĹƑǎρ˕ÛǺȴ\x90Ċ҅ÕĉѠƞƽïăL\x87',
                    'code': 'ņ˾ʎŷɗɵ{¨',
                },
                {
                    'name': 'ϑτȒǛŗɌƮКЏðYѾFɰËQ\x9dn|Ŧňϵӣń',
                    'code': 'ŘǊŹǓ˪',
                },
                {
                    'name': 'Əǥņδʛ҉ϺƧŌ§МɊɪʊʽҫƱPɹҏƖβčԪûěϵѿӅӝ',
                    'code': 'ȮǕΣÜӞϩœśL',
                },
                {
                    'name': 'ĜΜӷxæєʹżǄǟӮ˰ҙԢҝlξʹϰĮƎϮІɲǣĹũίаǋ',
                    'code': 'ƲЁӫĘҷŏɶΕ',
                },
                {
                    'name': 'ʦpίãǅΥƤγüŨɗȶЀ£BξÍоǭĊDȶÙϸx=ҤŠ\u038dK',
                    'code': 'Ϳ˹ϜӑµŻЖǸυ',
                },
                {
                    'name': '¨ΆϜҷˁ҉ϱnÖ"ѴÕҴǚϥęĖȈÌҕɮӡ͵ϚюǷшʾƽԎ',
                    'code': '˴JÍʨƋаґǘǖͽ',
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
            'locale_code': 'ǤǎΊΦ\x83ӚӁɮ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'R',

        },
    ),
]
