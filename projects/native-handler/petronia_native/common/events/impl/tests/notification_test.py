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
            '$': 'ɜΨ˼˰ȏ¯ӝ¬Ж˫ĎԓӱғǟϹ\x912īɞʤƧМı҅ЏԚџҐƽ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -2688186115372077381,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 695120.9659395097,
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
            '$': '20211104:182923.467411:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '˕æχ˗ǀƗȍӠ˓ϏOǷʆɖʱÖӋӎŜР˭ʉģӝď˵ʹϔȶɌ',
                'ƤԎɨœьOҭŋ΄ůұБӬҜȣƶMҜ4ǈȖЅԍΛøɡŌȱ\x82|',
                'ұŪɷƞӠϠjϫҁÏdƳԭϷʭʁ\x93ЪĚҚŕvÓњцŉΥʹҘ;',
                'ӡëʿĐԣҳþЗƦΏү\u038bɭȐˋĞɲњ˻¬ƴΊҵʍҝȂ\x8c҅ïй',
                'ώĆŭƠ\x83Ϝϴ\x9eαÿƜˆԕȩΞӬӒ»ӓξ*ԋţ2¸ûÃϛѓǒ',
                '\x9cǔȑȡřȻɣʘɿѕȑυąƚŜȴǻѶˇȿâ%ʦǤξɂȭÀȹ\x80',
                'ŘĭχŃϪʽüͰ\x80ƲèϾȈĸĵԡςіԨοĿҬВǌΤȷȐȫӒЍ',
                '«ļ҉ÄƝ6ŰѱˢҺѹıȌщķȾĩ˻кƲUĢϑЋƫGNΌѼδ',
                'ǦЈxӟȄѕэϩɜµҘϥҎʲɪҏΧ?ȱӟҜҤԕҫϡÁ×Ć«ħ',
                'Ҕԫ{ƺȑˁԊČɫĴŞӃGРЏҒɼſįєtȂ6n\\āɡҝ=.',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                8117837702981144028,
                -1122329223454403775,
                2374322525416645812,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                797161.3000794519,
                -93065.85912255856,
                993022.2576870066,
                720131.6099404097,
                821160.6953055899,
                669150.4569241852,
                360103.93892785796,
                710586.2870876719,
                127196.63484353185,
                -55773.33961563109,
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
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20211104:182924.162876:+0000',
                '20211104:182924.180661:+0000',
                '20211104:182924.197636:+0000',
                '20211104:182924.215021:+0000',
                '20211104:182924.233084:+0000',
                '20211104:182924.250870:+0000',
                '20211104:182924.267763:+0000',
                '20211104:182924.284990:+0000',
                '20211104:182924.303874:+0000',
                '20211104:182924.320832:+0000',
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
            'name': 'ò˭Ĝ˓ԔǍԒýŉ˕ѷМГŨԔRļʏŌɼʉĬ˟ȽÚЈ',
            'value': {
                '^': 'float',
                '$': 287005.63008045586,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʳ',

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
            'catalog': 'ħƌƁѐƵѦóɠĕƋ¦$˨ˮŅωɢхŇҰԣƷ_є/^άèʲǓ',
            'message': 'ͳâԢͼpɔʦÐǧ˼ФƲ˵іÇӠΊҸҟԒƇƵȓ,ѕʀ\u0380ǖúˎ',
            'arguments': [
                {
                    'name': 'ÂǍӣǬřȬы',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        4152890564848919207,
                                        -5052551591794115482,
                                        -1125757839635841021,
                                        6994213687817270500,
                                        -4671364142662639242,
                                        -5371942133549647480,
                                        -3310451171223161439,
                                        2397814134720819471,
                                        1392265030350607874,
                                        2534646175749080277,
                                    ],
                        },
                },
                {
                    'name': 'Ωӣҿɬ˵ãZ%ѲʜҿȓӥҹʯҫǾЯПү\u038bƖǢ0ҬӐʛɜϲÐ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        398557.0096684513,
                                        758674.2742727955,
                                        263026.7348036139,
                                        813620.2652509435,
                                        328871.51650908915,
                                        18674.510777059797,
                                        620034.0993103359,
                                        403226.8748433396,
                                        93270.65452880284,
                                        623455.0796350014,
                                    ],
                        },
                },
                {
                    'name': 'ӏԤѺµϔʾҮɥΔƉ-ĪΟ˄ÀǞΨƝͼzǠƇбéŜÔ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
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
                {
                    'name': 'ɞ҅ʆίʲʐЖ~уЃʂȋ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        767883.224623873,
                                        770122.3437059828,
                                        818226.0560991928,
                                        363254.0617653148,
                                        219949.6949158716,
                                        746767.8801494114,
                                        312277.6857681653,
                                        127370.11542884857,
                                        -97560.27527439802,
                                        701362.6652476386,
                                    ],
                        },
                },
                {
                    'name': 'Ͱˌ˟ԀƞÃʅʲŽŇ=ΚɀŽЪӦȊϛhʇäϠϾŴЩ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ЈϢʠʮǊžǍƇʔʃɞ\x99ҕƾ\x9bƤҷʭåK\u0379ȷóϝ^ˤѓԁŁӧ',
                                        '˾r5ĪȯҬӒѝŲǋ1\x9bЃĸɈșӄ϶ӊĬҳȡɆɇʟӾ(íԢ÷',
                                        'ЃǯǱÉĻ\x84ɅĿҋɻͼǊӌıțЄȀҾӵéǙɈ[ϭƐΜьӺƿƖ',
                                        'Ⱦʡύ˨ӵԔ/ӹƺӧɅɨӗҋîŲŹЏӕīĖ\x94˝ѶƄcæϮŎA',
                                        "ɓʤҏ´ɍ\x98Ákđϧ˓BJԄɔϳ\u038bʡ˙ɳƢ'жŰ\x9dӽéɢҤƕ",
                                        '͵Ď˙üwʧłŽëѡŞϘɬƟϭȍ<˙ѴþƳZӒ¦Ɋł&ΣĢ\x91',
                                        "Ʀ'1ԄϼčϚRȻԕƧӴŎʟɟȄåДɢȊԠǪԘЊBϋЄƥщ·",
                                        'ćέĆэǕÁŸ˰ɵ˹ЦǰëϙϲīϛƳЫѷ½ѲķƳȪИǟǛǜɚ',
                                        'ϚӁңө\u0380зˆҚcˋʍ˅mΈѨ\u0380ӓC\x86ƙɴыԟǤ\u0383Ǝ\x82ʺ˽ų',
                                        'ŏŌŖǹӃŖϱͳźΨʀŸφŋԆдά\x8dͼMԆ×ͱҌΒȄƬ˫˝/',
                                    ],
                        },
                },
                {
                    'name': 'ĠӴӂʅőċˉ˚2Rǜaãʯ{ϰԕφʤ5ƐƆӛÂőτˋ˞ԭԒ',
                    'value': {
                            '^': 'int',
                            '$': 263568859425358612,
                        },
                },
                {
                    'name': '_Ρ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        970293.613569818,
                                        521799.6325523874,
                                        291650.6413160962,
                                        811787.104111852,
                                        125416.8201628995,
                                        394632.3361931661,
                                        203874.11536023498,
                                        711895.3612554703,
                                        222133.67035729898,
                                        469147.6135985607,
                                    ],
                        },
                },
                {
                    'name': 'ԃӂJǞƼŔкϸɕÐĔN˧˲ϑǁ˸ƀέȹ',
                    'value': {
                            '^': 'int',
                            '$': 6768074041981807646,
                        },
                },
                {
                    'name': 'ŮǃǜҒ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ˈ·Цɒ˪Ðʑǘ©Ѿ´ŭønЎű',
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

            'catalog': 'ƹ\x8c',

            'message': 'Ĭ',

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
                'catalog': 'ȝʆȪGиϻ\x8c\x89Ҩҋϣ©ȦҊϛŉΥψƢʶĴҗҠ',
                'message': 'ƖɦxГǨҳİӊѺȳҎɸʇ˖ȧɌÿҨbό¸ɻ˪ѴȇŌϸɛͽο',
                'arguments': [
                    {
                            'name': 'ЮȦËЉàʙèãżÇȾǘһ`ԟϡϘԜϮ˾ˎȻħÒФͲɄóЂЮ',
                            'value': {
                                        '^': 'float',
                                        '$': 860061.0880753181,
                                    },
                        },
                    {
                            'name': 'ѩ¤ſМƅ\\ʚēóπЧţaѥԁʼӒǫΓˁƖ~ğŸʃʽԚԏͺý',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        199625.79200920026,
                                                        450408.4438808358,
                                                        184249.15458260197,
                                                        51391.47182206888,
                                                        229667.8250945651,
                                                        956280.4986909409,
                                                        159166.35657640238,
                                                        569645.4801964184,
                                                        434686.3713065097,
                                                        777836.1865516216,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΑĢӱɏƍҨУͲȹƨȯ¢ȷƓΈƷһϘÂ}υĜ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ãéƮɂĕȰȂѕĢe²ʧэʷΗӅÊϸÿӁƔʯӚԠɀҵřӈeÿ',
                                                        '҅пǓƥͲūĹѯ¦ѡʞƁŽ˵ȁ˘ф]ƣǷͿɬŨ˴ˉώЎ¯ϯƃ',
                                                        'ѬкDӍԀŬxʖӨÜɪŖɭɽҭҕѴЗŏ\u038bˍ2\x7fșӌ²åǣҕ[',
                                                        'ʂʦƾơԌЊȏү:ӄǻϦã\u03a2ƯÌɪ˪ʐҙЃðӐØзšν\x90Ȑǔ',
                                                        'ˉҞʲéñòUɠɗǨρϣGǛг®ԩ%ǞϙӎʠрϧēȐʿҹǍú',
                                                        'цΧΗʢѧκOҥēҟеǨȧѠѕòȧοɗðǁņɶúѓľčƙƒԋ',
                                                        'ψ҄Ȏι¿ќ˸îϡƨééԫ\x9dʢĦ¨҈ȽȍƠʞДӍĢŌJPǨӇ',
                                                        'Ƴ˺Í\x7fцΕѸёŀывǛΝVƫqхŇҮϞ.ȐȢӃЧ¬ӅƍƗ˒',
                                                        'ŖƅÝǒ˧ĒѠѸėӝΜɚĴԄÂԬ\x7fʁP\u0382ǿԋÅ>ȩĞɭņƒĖ',
                                                        '˱ʃˉƜʓƌͶňԀϋѯÜǶƙòѡͶ˽ċǁͽ҇Ɯ«ýòȘĤҠȿ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĎʜҶɲσӃ˳Ѻ¦ČʅtӂɎ',
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
                                                        False,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǩøɧȡɾˡ˵ÀƟ¿ȂĶĚƾυbȟÏϕѻãԓЀѨǤ0уĕȸȆ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'μʆԫǌщќLӛѥӔэ˵ϊɶȲȆƆTÍuˋΜ#ҍʒψçҖώė',
                                                        'ςШυDЕӕѭҜ{ŨÁȘϵЈӀȶѣɺɲ˪\u0383ѹȥSŔrOƬſӣ',
                                                        "ϫ˯ȋJƼ4Ǟŝƻʖ҄ȕȸƭåѐʕҔǡͱʑũĜƔ'ёȇƣɘÌ",
                                                        'ÃŌϜ«óˈчÀưǖӑȕΈ#ǻʪѧʮȂөɉ¡ЈȥŽԙͷʺƈʚ',
                                                        'ȬŦƾѴʎӡʶɔϼƇȫӽяФϜғ^ƖŧŭΆӦ\x8f+Ðµҷ®аа',
                                                        'ɥȮЈƓԡˉʘѭƋ¹ȒſӒ\x89żŘȻ\x8aʗȌȤ«ӲɀԔǃӲȟ²\x8b',
                                                        'Ũ\\ʃŴŘβӻΰƯ΅ɖљӍlӓ˖ɰѳʰΐmԛӕƽÎƁӜ@ϡІ',
                                                        'ӝǳΟ\u0378ϯÒ(Š]ҶɿʢӲЦɲŕ҅Ǻ˃ŭӔəůóȵ\x92Ǳјɦћ',
                                                        'ǭŪϠç·Ϩy҈Vȍþ\x9a}%PǐҼˡ\x8f˩ʗJǰ\u0383Ǵѻёдԃň',
                                                        'Iϕ\x8bȐ\x92ȫƍϠИͳĵӴѫҝ\x8eЪԣƃϞϮtϭɼƌЀҧĐʴƁǔ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΠƕƳԮˍʩlũǻȄѱԘńɐϕТѯ(',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20211104:182920.264452:+0000',
                                                        '20211104:182920.281206:+0000',
                                                        '20211104:182920.298255:+0000',
                                                        '20211104:182920.315716:+0000',
                                                        '20211104:182920.332870:+0000',
                                                        '20211104:182920.349455:+0000',
                                                        '20211104:182920.366840:+0000',
                                                        '20211104:182920.383797:+0000',
                                                        '20211104:182920.401420:+0000',
                                                        '20211104:182920.418330:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ĥ6ΝˠƜвӮȍʀ×BϚԮж϶οǜ\x99˩шϼДŅέĩƨΎƓʐZ',
                            'value': {
                                        '^': 'int',
                                        '$': 8518470832279284581,
                                    },
                        },
                    {
                            'name': '1Ȩ¾Żρѥ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20211104:182920.576904:+0000',
                                    },
                        },
                    {
                            'name': 'Ƕ-ԭǇĆ˽ΙПҀ˼ʳӎϟљəǒȧʨϺϏǶӖƞ¢Сɓȿ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ɣɄȦ˱ю\u0383ҦȒһЁҀÎĒŚƿǿȲȭȾ¡6ԋǹłλɳ·ǧФƍ',
                                                        'ǐυΑ5ҋdδТЊӭǍ\x80ǎŷбƪǡϗȤЅΏŇѧŋҲǕʼ Ԃϥ',
                                                        'ƑԠłJ\x86ȸȡʅҳ\x81PǸιԭϫ˥ӴȒʐщηžѵʛɥʆ\x88ʬЭ0',
                                                        'ʘȅ|ɹŎϰӡбԃ\x86ĕęďȁӀŏѧңөˎőѬÏӱɪʪǼGƌѽ',
                                                        'ëŵÙҊ·ТъˍĎΦќΎѤΆӰŦʻѧЩǬӤʁĖҪʺԜ²ĝɹΎ',
                                                        'ӍʅԊԂԎųįѨНϷʰϷřϾİ\x8eџіьōũöĘԜѶˀκùĨ҅',
                                                        '=ťӉɴ˂OЬ˷ļϢ˒ǩ?ȨʻōŞѨΩԫƍ˵ɽµΈǀķ\u038dѷ҅',
                                                        'ǟʗіԫ ȔČЉʁȲťɢэɩʎšЎȻФʘ-ɈɱȤҾϜŬϳёɎ',
                                                        'ÎӋɦҕƔɴůΣĖӞɬ\x88ȡ϶ɨ\x9fӫ҂ǵ\x94Ǎǭ\u0378ΝŌfđяýϱ',
                                                        'ɅҩэӢɕȩàˁЮͼ&Ё©\x90ǆØϯɖīȖӟȇɰĢŏԝӶʆ˙ć',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԝӋʳϚʌƿɠԅэř¬Ų¯\x89Ƣ2ΈԜѾɬά',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                ],
            },
            'title': {
                'catalog': 'ԬΨǹɵǿԛ~ʚӥ/\x94ѭʊΐԟЖˤϫÖĳӕ˗ЦȱƝҦƇzҪƨ',
                'message': 'юȦʫƀƦѯ\x93ȑɜиĢƫĄёǚҖβҙрҹίİÒҍȦȎКѻҼĽ',
                'arguments': [
                    {
                            'name': 'ӏ\x8fЫȵғ˸ʮ\u03a2cŏԬ҄\x8bƑǱ½ҚʪɍɷǛɿ˱ʊӯ',
                            'value': {
                                        '^': 'int',
                                        '$': 1927697668533788585,
                                    },
                        },
                    {
                            'name': 'ŷ҆ǳƲɤƌКϧɫəĶӹ\x9dưČzǭʁʊǑӺƥħҎΩΩǕɛnʇ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ɻƯЕЬž˳D\u0380ˎʒȶɟԉʮҲ½ɹÂѳѲƤӏĽϵ˅āƤѾɩ½',
                                    },
                        },
                    {
                            'name': 'Ɇѯ˥ͳåκԛžHÍɪĵ#ǱѿűĥþŤ˻ļˇ˵\u0379ϙӚʚӸрŅ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        True,
                                                        False,
                                                        True,
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
                            'name': '¤/ӾįĘɴǴg',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'җĠ҇Ĳ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20211104:182925.018805:+0000',
                                                        '20211104:182925.035548:+0000',
                                                        '20211104:182925.052323:+0000',
                                                        '20211104:182925.069145:+0000',
                                                        '20211104:182925.086025:+0000',
                                                        '20211104:182925.103566:+0000',
                                                        '20211104:182925.120524:+0000',
                                                        '20211104:182925.136866:+0000',
                                                        '20211104:182925.153723:+0000',
                                                        '20211104:182925.170438:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ϤͼǝįĆĶЃʡ\x8aɧ,ȣҮǭɯuŢ\x9eŉҢΪǎ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ƵȂұћКǿϣвÅůϐēӽүȲɴƐͲĞǼͶΊŮʻӛқɞƼʺ±',
                                                        'ѼÑqωɑàȂτ¨\x81ԗuȺʇÏȟҪăѱЩ҉˙ΉÆɪќԦқӢͽ',
                                                        'šİ҃η¹CźѦ˚`˻BÎӿưğғ´!_з˨щҁ`Ȋɪĝљ\u03a2',
                                                        'ΗԀd;ШоĠΏΖ˝ԓ$Ӈşί»ȍϦ\x9bυŮʵϛūõӻOǚØĲ',
                                                        '˭Ӎʨƞ˂ӎŲШҊȎϬ;ϝHɒŐӲɁÿɝϣ[\u038băɾΦͽŋJχ',
                                                        'ǖǁǄűŋɳńǡȮ¦˱\x9cьŻ¸ĊѻԢԂѢϵ˹ԀùǊҐŎȇҋ^',
                                                        'ƏԄƕҘĦѕǚʢÿȘƫσӯˌһ¼ǈǽ҇ԅ$ʲрƓ-ƉϜίĚ˳',
                                                        'ʎ\x93ΟЕҡȐʟɜˋПԬȸχǁ¸ƔǖøІŊΊƮƕƬМȶ˅Ƿ˼B',
                                                        "ƾÓȺǝǢĀϮǛǹƮʁЌə@Ѽ҆ҮȚӆWѯĺҼ'ȱ®Ɇ`Нʝ",
                                                        'ӁТάŐΐȏaʢӱőùȳԡ˄ŶϼĢǆ ҴʴʜÐȩԬeʝTȂǜ',
                                                    ],
                                    },
                        },
                    {
                            'name': '\xa0вņɏƤ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -822934538626913847,
                                                        2848527596032993189,
                                                        -2407722187814470360,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƩΨлƗŷŚŴϤҮďʴˉϭ\x9dϱ\x95ƺыŒpʦԡģğµб',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        611493.9776188124,
                                                        909718.9527964048,
                                                        601919.6721660485,
                                                        211267.27121315186,
                                                        455014.02450543176,
                                                        583817.6588169377,
                                                        564345.6683199069,
                                                        414624.97522705887,
                                                        -46475.72109545357,
                                                        562851.7232167892,
                                                    ],
                                    },
                        },
                    {
                            'name': '˯ŌӞˍӖ\u0382ΗѹƝрȭ4Ʈɹ¼ǙѝΦό\x89żƉŚÂĴĄӡɜӟҎ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -425879604545165209,
                                                        -1487348724299994043,
                                                        -6404467561626683422,
                                                        -1757952730878134189,
                                                        3047026019193405708,
                                                        2593450618265958674,
                                                        -6420858949220081352,
                                                        3046970782856504387,
                                                        1540752753836502947,
                                                        -4856549577081314390,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Νɻ[ͽ@ѧďҿтPɿ˰Ƅȅ',
                            'value': {
                                        '^': 'float',
                                        '$': 696840.1409511812,
                                    },
                        },
                ],
            },
            'icon_id': 'ȀeЈъƌĐˈˡрћâШǣю',
            'sound_id': '\u038bǾӻӖ\u038dˆƷϊĀәČ];ӒɧͶĹƦӁчԙϽBǆҶǅЗҟԏј',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'text': {
                'catalog': 'ǷТ',
                'message': 'ɀ',
            },

            'title': {
                'catalog': 'ǧŋ',
                'message': 'Ǫ',
            },

            'icon_id': 'ß\x85ƹ>{',

            'sound_id': 'ʥʞ˞ΰơ',

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
            'icon_id': 'êƍƢŠ\x8dЎЦÃɃ!е\u038bŕƴȀѼÀvԢȟѾ˘S˧ӸуϢ˳Ɓґ',
            'image_id': 'ПҵцЉыǿΖϔ?%ȫʐԌƮĔ҉w˘ϳҤƍȟ҆×Ӟ\x84#ШĘL',
            'title': {
                'catalog': 'ǚRǾǕ˦ĨîƭҮԘØԆA˼ōȫЭÿ`ьƢҜϟɌͿȵŻɄ\x92ѷ',
                'message': 'Īº>T÷ϯ}ʪ\x98юŪԨāӰǭώ\u03a2ΨЁưԢʩƟԖξхǣă]р',
                'arguments': [
                    {
                            'name': '¿ęļɤļóŜςŻƗ8ѦӣѹȅȎӅ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20211104:182941.539727:+0000',
                                                        '20211104:182941.564742:+0000',
                                                        '20211104:182941.589556:+0000',
                                                        '20211104:182941.614284:+0000',
                                                        '20211104:182941.637046:+0000',
                                                        '20211104:182941.654277:+0000',
                                                        '20211104:182941.671031:+0000',
                                                        '20211104:182941.688132:+0000',
                                                        '20211104:182941.707706:+0000',
                                                        '20211104:182941.726869:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҸѵӦʵϞΈοɇҭ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ȘÿȫҟӑɥΌǊǮņԭYȸӼ\xadӯ҉¾ͽʰɷĖêǺʆԈȃǳӔӁ',
                                                        '͵ЃϗȐϥŜϔȁнńӾЮӒÓÍԄ\u0382ĿҼδOʚŗưȪ˃˝ÍƀĘ',
                                                        'ƣĘДĿĎτʡѓũҵǔѹřȚ҂þʠ¥ɣԙӸƣʊЂќӬɑҩΏ\x90',
                                                        'Ŏ҉"\u0379ΜѮǚϟΤȚ@´Ҏəԋ\u0378ЬʏԔΖɏǦùюȨγðŀѠӹ',
                                                        'ƥƝчƝѴkŠϓƦǎ\x9cҊɣʗΤуϙыʸӇw+ƣϼƽϦ,ӃƟГ',
                                                        'ȁУӿÙʠϢδ˾ɥϥҝͰδåˤғԗøѩҽǃȇаӇʕiеǘƀß',
                                                        '«ҪĹӰΔґɪɢͲИƖӑȧØœʧњςςʴ%ì˾ȼǊύɈɽúԚ',
                                                        'н~ԓX½Ѧȁмɍ˓˯ǢĒ;ϛóʥȅɽʯƏɈǦb˲\x9bͰ7Ϥʖ',
                                                        'ҦѽΤ¦˹ΊǏĜ҄ЅӬǎü˴ѨҵӈђϡϝƄŃɕǌȏǝƔ¤ǂL',
                                                        'hŉģϽ:ǞĤԥż»ԑГϏӓΖ˭βҤŎ\u03a2ӵӶΣ\x83ɾЮΎ҆Ŵƴ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӼȔŽ˱ӄÝȆόÆ2ƻĩԒž˷ӵƥ҃¦Ѣ\x91Ưϳ\u038dhʫƌͷǜɕ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        297079.81784205494,
                                                        646704.2335106393,
                                                        202321.5130699973,
                                                        136155.7047642475,
                                                        366001.70908932504,
                                                        450743.863616699,
                                                        372550.98174243764,
                                                        751049.3986074873,
                                                        422450.8408860714,
                                                        567696.1112106913,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʈ\u038dɚɎΘҡōßЖљΖ"ӓȪǆϿюŦΌ\x81ԮƣhСѷҗ˷¡\x98˲',
                            'value': {
                                        '^': 'float',
                                        '$': 400646.53415700985,
                                    },
                        },
                    {
                            'name': 'ǷŢǶǂԫЄ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ű\x92ǭњΉɆλҟǼɴ4ŞȣȞкŽΛƟƃµŗǘȂ˶NķҮΘӭЏ',
                            'value': {
                                        '^': 'float',
                                        '$': 383702.92007881275,
                                    },
                        },
                    {
                            'name': '˽K˓ʛűɅȔӨͼɎΈϴȷϨiʒČŰѫƷųѭźÒь°ɠ¨Ņʤ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        450530.05463001656,
                                                        430926.44019418804,
                                                        428194.2475400509,
                                                        479326.6695373615,
                                                        885474.8500855078,
                                                        568900.5293625864,
                                                        -3763.3195913138916,
                                                        -73204.57683626743,
                                                        917123.9883679705,
                                                        135763.42345741714,
                                                    ],
                                    },
                        },
                    {
                            'name': '/ĄƟѵŸŒ˨Ã\x9aϖϪҬϫɇΠYŢʷýŖӿŐŔˬƜ˶ºʰӎʚ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20211104:182942.929207:+0000',
                                    },
                        },
                    {
                            'name': 'ϵǜ˅ϔ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20211104:182943.008863:+0000',
                                                        '20211104:182943.025837:+0000',
                                                        '20211104:182943.043135:+0000',
                                                        '20211104:182943.060848:+0000',
                                                        '20211104:182943.079334:+0000',
                                                        '20211104:182943.096989:+0000',
                                                        '20211104:182943.114255:+0000',
                                                        '20211104:182943.131533:+0000',
                                                        '20211104:182943.152299:+0000',
                                                        '20211104:182943.173262:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': "ѿɅyGĕҜäԆʛѿњ\x8cƑƋˣȚɌǇřԤÆЉŶŧɹďԮ'ùĿ",
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -5299799522044617330,
                                                        2716863588059757307,
                                                        8782044369030609441,
                                                        1015117296228793603,
                                                        2513060999929146943,
                                                        2525327050905825433,
                                                        -5604169947361973052,
                                                        -6713543549371132113,
                                                        -2907571362149118840,
                                                        -873911654525195436,
                                                    ],
                                    },
                        },
                ],
            },
            'hint': {
                'catalog': '˙+ɰǧʹʾϝəҥ2ÏŭÀѶӍĞҷÕŃ\x9aːʴSҧЬ\x95˞ʹӡȝ',
                'message': 'ʅѹćӦѰͿĕѰBɕϏƬҠǇƀĤŲҖђүҝѺƨʀȫ÷ȉƛЀь',
                'arguments': [
                    {
                            'name': '·˪ΖɃǛѡȑŮϝńɇŪϭЗÔůƉЬɘМϭϫ¤ʙƢŕӅğȚð',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20211104:182943.708316:+0000',
                                    },
                        },
                    {
                            'name': 'ӳӦ˲дǮӮ˛Щ҅ɓÔ*"Ć(řɊȆл\u0379ύťÜΪʳ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ǞѫȟшŅŒҜѡЈӣɟnɨШλĪԂөͽǼϝыҖʨƄѠƿţ@ç',
                                                        'ĉƸƻ˲η{ΐ|£fԪÍɫȃ\u03a2ƻȲžЉɳӔÊϘĂӁθō˚Ϋ\x8b',
                                                        'ċ\x9cƠ˸ǈȤƻ˼ѭÝПƉǠǏԓҾƄŅÒțȓǥĞǼҫŒʕØÛȾ',
                                                        'ʭЂЄ9ѷӍӉʐ|ԪÊӺԚŦØцԑòφœȾЄ҂GŁƟŒ\x8fĵŧ',
                                                        'ӔĒӎҭЙkċ˼ё<˂˨Ūʉ\x98ϑĻĮӦΉҽџȆ˝ԧŰ¦҆ϸӿ',
                                                        'SΗķʚƒǔɌǋҒгȝǎǅΧǸ(ӀˠȫŭΪҵ¥ӪˮԦЭơǐĸ',
                                                        'Ɖҽӄ҂ԦŬʁʏѽ¯&lЖ\x9dԐʽťd2Ы¹_˪ԅăѶJɎϥҐ',
                                                        'ȧyȹɰ˲ϺˁψϿÊǯҞӾάŅlɁǔ҅ԑȃĜЉ˙ЍďŠſǗ˂',
                                                        'ЧőйǺȷøǕ˨ɛƠ˷ǷʫƶѷώźЁѥӪʌʁҳҼ˔ʧȺɬЃ˓',
                                                        'ņйǦ\x9fЩäͺLʞºԧ5ЊMŁӏѧǾˈԔе\x82~ʖˈϢЮΣѥǂ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ıåӓğԖчȆŗƛдēĉǮП!Сʅĭ҇˚ɼ˵ǖΟН',
                            'value': {
                                        '^': 'float',
                                        '$': 219142.3341046907,
                                    },
                        },
                    {
                            'name': 'ʡϒ',
                            'value': {
                                        '^': 'float',
                                        '$': 352143.32672994223,
                                    },
                        },
                    {
                            'name': 'ƙƩƤӥƚ©UѰо;ҪŰöȈŌȧќ«ºŦ{Ԟ,',
                            'value': {
                                        '^': 'string',
                                        '$': 'ƨҨΣϔш˙ΎnӶϢʑ`řȺɦɌǃԠƋϧψ!ɍǙȄǾ\xadšØŐ',
                                    },
                        },
                    {
                            'name': '˒ȅĕѷ˃ɶȏԫґΑȊԔ˧ϴȬҦǀ\u0383',
                            'value': {
                                        '^': 'float',
                                        '$': 199968.06747743144,
                                    },
                        },
                    {
                            'name': 'эżʅΠғӤ"˰ŗϓν',
                            'value': {
                                        '^': 'string',
                                        '$': 'Ýˮΰȹɺĕ½òϲǔÉɌԝ˨ǿ˥ԊжʊҝƱɘʥӈįȷӪӁâū',
                                    },
                        },
                    {
                            'name': 'ɽƤ+ĢıДȵѧɧѵ¨ρÊȞȣϔÿΏčϖĩ\x98ӽԟ:ЌŢɐԡϥ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        True,
                                                        False,
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƉàҰӥс',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        ';ÃӿǕШςωÝ\x85ŴӘӀƸЂκĉėOӍЉáɃӭŢˍΎвϴҕҀ',
                                                        'b˒Ƚǯǔ{ħЖӈԆǺʠҌѦԁŠú\x9bÛŴ9ѝȎŚъʼƭŰÂ0',
                                                        '\x8cƠōʠň<Ӭ΄\x99ТҵҜˊKǌȮʃҡ¯ʸ?Ԕˋ¼ί ƞƘĮѝ',
                                                        '\x97ɘҢԦʂɣϽБŹɗωʌ¿ǹɊ\x90ǻƕѰ҆ɻKȑMНдҶˮЉб',
                                                        'ȐĺҩΡɘШÈЫ\x8eTԪɽɃǶԪӊe˺ȊʰʥӓΞąʒӥЮǰǛѮ',
                                                        'ãА\x8eωʁŇЪҤȳ҈КĬԎ ÷ʍʦɨºjҐ\x88ȨϔǣÅРӛʨM',
                                                        'ԔƐӃ˺ĪÎȻðȌŊӔʚÍȎ΄ĘφԆǰϤϪнZǟʜČʛѡыʶ',
                                                        '˽ÝʸɜǌуʢǺѫаΛѬԐÇҵˌүǄȃѫ͵ЂŏΤϩɤ[і҄ŵ',
                                                        'ǟɳȫԎ³ύǎļ`эӕг˵ȟл¹ɪю˞ƋΞŏǀŊϴñΠҚр#',
                                                        'ˎӦΐ\x99Ǹ˰Ҷ˨ʓʼΜe0ϻΙͿ5ԭɟϚ˛ӰųƀҧѻǷηƻΣ',
                                                    ],
                                    },
                        },
                    {
                            'name': '\u0382εЇʔѪШ˫ŭŕӖϕüƶȭŉȆ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ì1çƀ½ѣӐ¦ѢίǏǑˊPɀȾƆʠɀӧˀκĊ.;ÏÄȽΊƌ',
                                                        'ѳǽѸϥͺΉˡԣǋʒƉϑѰҊˏϬ!ħȃ˧ҢҒĬѱ=jɐʠϩʭ',
                                                        'ŰώƝǍЛʪӝȎћ\x8f\x9aаłŭ\x94ΗОwϲԈЎCўCcƶʴŅɢҲ',
                                                        'НɯØÅɷ%ˠѱƪλŒғ,ǎĴƘӴŶǍӍ[кʉʖ\u0380\x9dˑҩЕ\x9e',
                                                        'ĞgÊzԡеƪԔπÁ\u0381ΠЉΔţʨԈƛȨзÆɮǁͺ*ͶұΥϐӓ',
                                                        '˽¨ӨǪҕɣҩzԝŔȻƟ-Ο˓ѴζϏ\x9aɰӯҞршȞϜΦƛ¨ԉ',
                                                        'φ´њDԝлΏϸϯɿŏЇҳźɀŽȧ˫νă`AьǘȦǟǄĄ&ĸ',
                                                        '2ɱǐɇÚϝɡÉĀ˚Α\u0382\u03a2Ĥʸϸ¹˯ǒǴ˦ЬɹNǉљҝˋǲϋ',
                                                        'ɤҥˍƐãҪçʂʎ˾ӓƈҶǼ\u038bΣѷȿũʸѽԐ˜Zâӎԓ˹ϒƍ',
                                                        'żѷӬЎ7ƘɄ˴\x9dИǛpÈԣ<άͿ+ǁΊ9ȶĨҔƿɄλǯǣГ',
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

            'icon_id': 'ҫȧɓʩԘ',

            'title': {
                'catalog': 'ŝÌ',
                'message': 'ъ',
            },

            'hint': {
                'catalog': 'ɸˑ',
                'message': 'õ',
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
                    'icon_id': 'щƨėҁǙҷҐ˓ȞGӋǲѺĖƣɂЅŌӷȎȩҐҳȩǧˡΠҺķå',
                    'image_id': 'КϥǶϸЬɋȵȪѥăԍιµŁѶåƉQԂ/ҋǂǼĊˁɐĸ˩ˍȄ',
                    'title': {
                            'catalog': 'ѠÝȏˀԠ˰ïӼȿLҽΓʲˣάϙ\x98ɾԀӾ´Ʈ\x9cͺgѐȣǃҧΜ',
                            'message': 'Ъ\x8dϐºǆj\x8eԮǴñ\x8aǘӆӘʥȢŉ»Бǡ³Ғ\x9cÜʲт\x87ҾΡˣ',
                            'arguments': [
                                        {
                                                        'name': 'ʛȫΐàƚԘѣͿԥ}\x94źź\x9fҏ\u0378ĻɲΏЫLȹƅϱƘѾцƑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˮξ˜С\x98ҋȚъˌ \x93ӝЈʦ\x8fǼцҍЃ˺ʳлς]ӇӰѯļϫ˷',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԪơѶΪƺ¸íǮÄ\x82ԅkĠϿɾ˅ҀƬʜǆĨφɓμ˛ȀƧƝϼĚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ó¨Ʀ˟ŃϲǖÑʤХÝļӱϳËĜŋϞɼҜϖŊEΘŘүťυӸƪ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƠϰҢûšϭÔѦĮ ˻ԂϽέԕĦ¸ɖŃͺԇôшʖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŅÎîӻІ"˨ȣҩɧúƯвȏԛʲāɜҏʹэ϶\u038bωВ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4825015179558297915,
                                                                        },
                                                    },
                                        {
                                                        'name': 'г˨Ž·ԚßΔĲ!ƱԤ˟^ŴҞъҌд˙ċѨʯͲʰҶϥЂwÏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182926.842179:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯӽ˟ʴ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 665330.1053657162,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹΦǤœʛÞҐƵİȐġǒǢф˟ГƺǠǈŏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182926.982922:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɩԩȴ(έ´řʑǙн˩Ã¶ˢ˽φԟѾ˱pӋҎԐÓY\x98ˬԗɄӅ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭ˛ΛԎȒ/ǃŸÆžǮÍĒәũ\x9bsҙļԝĤӶʐϼǽ҇ɲԋƒ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ͳȸԠĆťϤϷȥ',
                            'message': 'ɔχιȆ˚ǉ¡ɝӒʓóŗŻѸӔŤÇ¢ϴƿ/ˮ«˯һŋӋâϘљ',
                            'arguments': [
                                        {
                                                        'name': 'ýČɕЀôԝӃƱXЋзɎǷiәƽЯХΈȲĴǴŜˈжΧАXɕÞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӗԩԁ5ӫ΄ȠΚÚϼӍhі',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'І',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 207033.76975230535,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƈεϴɑԝγƀа0ӃʃӘѧ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '@бʂʃ\xa0ʭƽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȋą҆ǸžӐļЧżҢϐКѪǁƖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ә˯ŊĞӞӿҲʗǒǙεȒσӠԨʧБΣŘЁǇ¸ÞҢΫ2iºȪі',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԆҸșʻ\x82(ÖĶȔį¤ѮT.\x9eȆЀΥǑΞʸ\x9cҔϋɶʪJŉƴБ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182927.793889:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˏʶǍѰʚďėΊӄȣvƝÔαɍӍƕ˕ҞǜԋķĈ˰ÃʧЪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 143877.4915365604,
                                                                        },
                                                    },
                                        {
                                                        'name': 'тАЮ',
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
                    'icon_id': 'ϞǨÄã\u0379ǒџʝƶͷȔԦԞ˗ϋĪʞıͳʕDǵǢѶ\u038bǪœԠԐ\x88',
                    'image_id': 'ʟȝƅԀƶąԁԋMʔԖűͲ\x84ҳžζƃʶҺů˝ͶЫмяȰԋ²\x9c',
                    'title': {
                            'catalog': 'XŠȪĀšӿӡÎ6ôZʘЈΤțƳĽȌɣǝc˵\x9aԥνÙɇɎ.ӏ',
                            'message': '«έȐƄɨɩΕǙГϋʤɺʿΚҊ҇ҨԝėϿǲÅǧЁҨ§Ҫɹɢ\x8e',
                            'arguments': [
                                        {
                                                        'name': 'Ǿϯķǜ6ԬćԠBǎĂСǦїѸҩĉʝ˶Fϭ˛ǫ\u0383ǛŕŊɄƞ˄',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5653050365555994175,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϬШЖΊͳ\u038dѕӸB@',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԈǭϋjĪøҧoʋʲ˕ҫӛ˞ĜÕŎʎΤɫƋҚΜŦжΩн¹Ǡƹ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʞƿЙƣRȝ҇ѺȤΧȍԗĹ\x88ѡ«ơ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҰМ\x9b\u038bɇϑȺ5˵Ї΅ΒɍǲŜğǫŎͷЉ"ȌǆԟċљϦ΅ԕ\x8c',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɰш]˒\x8e',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȿɑťXϘʎɼ΅жҳӃѾӖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'эɬӲhјó',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǐѾτӋūѱҭͷβӵŠʐϚϺЅ\x95Ӗɳƹʹˋ˄\x8dŅėѝċҼɩʱ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȅ¯ӤϟλӏԮҩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˞ӌȵǫһ\u0380ȀωɎʞԛĢˡmļŧҗņȈ«ӏϑґɅ%\u0383ŮϗϙƆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŦùĴЅïȺɽ\u0379ŠӷԞȡҏ˔ķuʁÍɝȭώӷáԀP)ăӷ҄ν',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЃϭкğλǤˑԀЧɀȢɑķ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -515570049756660111,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƃʕ{ǻЂѯϺòƸ9Ҫ˜¢Јġғċ)ɍԎŤ´\x9eӉrɊͲʷƁ˟',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 613744.946799531,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ʽұc[Πɧ&ȤǧļѨǙƮʂŐǽϯ¦қŃħŕĉԅ˶ԋΣҞŗӻ',
                            'message': 'ӂЄťʽ\u0379źȫǽрß\x92©ˠϘҌϚғҹÈǺԭԧgĖ)б2§ɛÜ',
                            'arguments': [
                                        {
                                                        'name': 'ɏр\u0382®ƦΆҎĩĤɑαʲωʋƣԖ¾иǢҦ҄ƭӳϬÆƙӷÙ¿Ȁ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182928.883356:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ұïȁeѿĨΐȶӐӱȠŤǨƱǠǷԐeąϤуˆ˾8ΚTҋѥ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x97ćʛǵɼϖǍϺԪĵԢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '·ƈΨѧɠβϓöЙŦԃ\x9bҹΗʒƾȁԃЏ«ɖ!ÂҞƚұ(ЙǸѪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dɏ½ȼ*ƝʏΕŴҫʑŰεɑ¡ѻПϊƔwМĀɔӃԏŻΙ²σϣ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΓƲҐϼс˙ӾҵǪѻΛηOҪ˲ŪȖʭĳ\x85Ҥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĳѣʒ\x8bоǸŹɟ˸ȬȅϤУ/ҴЦӰԧϱӏɟ²˩\x9dżӁÐʦ¾Ǎ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋӢĜǡчβӃ\x85WȼĕJĪɆAƷӥ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7766450089846674526,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԤљǷĘȄŇń¸Ǎњȥĝ¨ʶҺʂ҄ɮһЫНˋ´ёô"˚ÑŹӞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'и˾ȅҴɂ&ӎʹΦίƘ˷ʯǃǆ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182929.432216:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӠʁϭȫИbӐ:ʎžÐӋʞІήdɮÞÒϲҋȖȡˮԭ±ʾӡαщ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ԕѿȒļ\u0381ЮȫЅ҈~ǿǍИűȈӄǁΫӐǘvȷΜ\u0383әˌƒӢƟĜ',
                    'image_id': 'йȇЕˑџӟ˳1хʱđǽ©ѭ\u03829ƯƩKȀҖȦбIѣӑƚҥʓф',
                    'title': {
                            'catalog': '\x94ϋǅȕƴӮƃȝλъiљάĝү@ɞʯʭӤǨԀ\xa0ƀĜхɖ@ʵх',
                            'message': 'ɴ\x92,ԐʯʹħĳϘβÂŕɞɇϩɵĝƉҫуȜɎҩиЪѲȍҡåj',
                            'arguments': [
                                        {
                                                        'name': 'ЪȩƪΤƩǶ£ҝС\u0381τOѯºİȅϛ˞\x8eǚӌǅĞś7ɐšĿYǦ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʨ\x81Ȏ\x8eʃʫŖ3ǌБ\u038bȦԫĤ˥Iêũӝ·ɝͼ&ˉèžǎŴʁΖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 966589.3018560365,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻVƝάϣt-ғŲĩʷԦǩлɿŰЃϢÞ˧5ҞʠҤÛAɟґƥƝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵѱҥҤʍʷΝũɅºӡФ˸qǰҬΜĮQȮҋʁƕuԟwџ˧ϊĎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182929.935372:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Х˭ѩǜǀѳǰĦӥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԅăҿ®ʓüΉǇԅԪќǢǨƑȰȍшʤÁɍџʫȠǽΔѐżʚѫƧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĸÌǩӊƱȤǺ<ǞVʡɬʄɢù9ҐΆœԌϒɹȝȗÈxƜϰӃ\x9e',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ôÐǓO°ΣԮϭơʇBŪШзӗӞȔŦ±Ǒøħ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĦɊЬ\x96Ɵ\x8aі˱Ñǆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӅàԚÛʒνͲЊSȣľȊĄƢуӉͰƻЮѴөǅʯ˺ЃŜɊӟщѨ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻĬцЃ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -132903485649577981,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ϾϸΧôÒУϪˏсə\x9cǯϬЪҞȬї]¥ÄĐm°',
                            'message': 'P´ƫœϸѺɕȇҍϒƶΞˣκɁż˥ԭʄΫĸ˂ïʋΝԖŤӥ\x83P',
                            'arguments': [
                                        {
                                                        'name': 'Ǖӷñ°ŤÝ˾Ҁ^ɡғ·ˣɡΩ\u0380ѻѽҷЎӟȑLιǾ\u038bǣšμǇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃˈϐɘϠLԭƈʜΒğҊŦЁϊʐϖ҃4ӁƺϏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'cƏϴʿʌʬǞϧѢȬŚԎŊѮʶɕǤқԁŴwƒξÞʰėȝȭӯʘ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ơ;ӜӸӆӵԙɼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƹ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƦĮϥQήѴȚҾ˅ɡșȋԘҟƔφȹG',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƹ²ˤǦΓЭȊХǩĪϯ˪ǇԎ҅Ǩ΅ЖϘϨǥҥƀӂҦ!Ϊǜëı',
                                                                        },
                                                    },
                                        {
                                                        'name': '˅\u038dҩзĪҋɷѲˠ¥ȜӳʤưƄЃѽѮćԀϚϹЖŢ˴ƹҁ§Ҏˏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϩԄȅιʹĮʷǀϯΫêҷҚ҇ȊҎɔԑŧϣŧő˙ŞȬGĪ˥\x90ǵ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȻˬӋʍӟšǅ҆Ϭʰʡ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "Ф'ȤɛВɲ·ˠĀϡȓҊģŭςw\x8aʕȿ)Ăʰŏ\x9fɥĐɡiΰГ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĄǾҨ«ӝЕԨhG˄ԖlɖŔˣѼɄȻŜϢЍϜϣøȿʺ}ѝƒ˪',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɼmŸѲǺ\x84æŞQȋԉʋ˘Mә¹ȖԘɱ\x81ўȹÀǸƋԌ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182931.161673:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ЀԧǪύʆƳǸū}ǟ˽Ϲϔʜ˧!ūöԭαǽВŸҍ\u0378ЖŦĆЧƁ',
                    'image_id': 'ӔĈǹԉɤȼʎȀʥȡʍɿ\x98ҫΗйʡ˻²Ȅɳƚӹ®Ґǆ϶ǹҹя',
                    'title': {
                            'catalog': 'ИˆɼĈȒҋ\x80αȉǺҀȇȶͽɳҶȐϹ¢ȂǢЁʲʮϤď\x8cžj·',
                            'message': 'kĤ\u0383ҟюÅǐЍȮʆȕaˢЩpԪРɼΏӊÆΎȴďɼˌʷӼКʻ',
                            'arguments': [
                                        {
                                                        'name': 'ā\u0379ԍĽ=\u0379ԙÖċҟrԤԃȻżѽɵΆͶъɤѐɟƎӷҼ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӭҁȫ͵ΘyζΪɯĺѢɪвƐжŁĖ{ғ\u0383Ӻȿӥ˒ʞƶǏӊҩ˲',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŭǚҷŸͰԝɔҰFΆČȇА(ĂġäЧљ@βǰңҒçͼ}ðʩ×',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˲ΝÄ҃ѽıʛҙҵǅ0ɱƷĞgĤЍ~юԔ"ώ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĊȒPΒήҀӢǳЇȯɫ´ʉÙǫŸǢԆҠǍѵʯjþşӵŷȃΨӺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɌʰŘӽɍԝԟÇťĻǒԭѝęAѱɢӤ˵ˌEĩӚą¤ҟ˲ѹɖȔ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӅϨ2ѹʠƫƘƌͻġԤҬÉ·юСφуːė҅ԟšbȚǗ\x9bӽϲ˄',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˳\u0378ǻÊљʒӆīŌϐӃϻ҃',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4464083683160727085,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӧԛ\u0379ɾȖ˴ǵНԨϓТ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182931.867217:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЀςɴɍӧƛѠ\x93ȵǇĎƲfԦŭѳ,\x8dˬ\x94ǻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 167303.66915253818,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǬʳϺȱʏҪΜΧϼҧɯʫ˦ѱСýǧНŦWĖDЌĪˊӻљȅƛ ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 506042.104685516,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ĮЪлԑğ˱Ïʟ˯fЭԚάʵɾNºѾёŞϪƠҿ°ɫαʍҲŗƴ',
                            'message': 'ʂʾǧİÔƏğǽӸʴȮʉї5ϒ{ͱ\x9e¶ǯԧϭϱͳ°Ǡ\x87ŰЦҊ',
                            'arguments': [
                                        {
                                                        'name': 'ĎÑ·ΰ\x98"ҠÅÃʼѴǡǱѷӱΔҳ˒ǀдŕ£ůɄ˵ӿͱκԕÐ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182932.138411:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'όΒŜχ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѰǖѻΤ˄',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϫӡҖ,ϩɗƄþȠɬͿΔŬiƙƈџȶ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԥ%',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʌʧЮʉȈӀČʚțӉ4ђ3ЊŀÄřԊ\x93âµX΄ɸҀȣņЋϬӭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʟǴҘȷ\x96хƖƩƪȿŧӇǆӬ¶ӚϴУʄōԪφɗҢǧƴɂ½Ǧ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2373941876906428809,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʺn',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɴӠ\x95҂ȘЙϘȂ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼϔԪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ЛÑƛ\x98Ûԙαœɨұϔ\x88Ԫİ\x96\x87*ԎҎϚǩûрӻÔӂΐ˔4Ɖ',
                    'image_id': 'ѓUɞ˘ʗǄϧɯԂʗˠтϧĚȚƸ5ʽвΆɀϔͻvЖ˰γўѯù',
                    'title': {
                            'catalog': 'Ǎ˓ŷŕÄɁϊƒˍȾѠƈɷ˨ϻrɋĚйěЪϷƽ˽ĿǍϨʙǣȲ',
                            'message': 'oʴԐŗÜϦВ˧ϋƖȅıƃɘ˃\x95ͱЁʀϏËȣӱȑKӦƁʗȂ¹',
                            'arguments': [
                                        {
                                                        'name': 'ЦΘ\x97\x88',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4211733921574598430,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʨğϽÞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '®λѴпӍʵʭϛϪʆɠǼΑбɈϼūԒҽВČΩůɄћÑƷĐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¾ʰżɗтʾѧϻǟqϮƬ&æ0Ũ˷ѓǸΞҪҹӑʯßӈҞΩ»ʃ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŔlóǍψӱȺҒӍËǯҁʝéΌцМрԆэ˷Ǚʺђ£\x9bȃűͰƿ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɖřÜѝѨҙs\x97ÏѾʬ҂ψʪЋƻʣÄʧΫҀɥԩҴ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʠUĳԥŗȨʏ˨҄1ΣƖϷʑsȹөɈӛ˄ͱoƭѰЙ\x7fŘ\x7f<m',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3587560839903740888,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁ\u038b˺ˑʺӣМѶČƪΎ\u0383ԛšҫνϺȹԪЗʬĆȦͷƜƅӋѡnϸ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'wâǚƼŪΎŠ%ӄʽѲĩņƑʡЕĖƴ˦ˈҚȾ\x94ʈјɢʑȼӱˁ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'lҾƯƱΥӀzνƑ\u0380űź҃\u03a2ɕЊφĉԎϋŧΓыѻЪʗÀǣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '9ʾCѼƂΉĖШҮώĻâƌѺˢϷя+ĖϫŪɰӆѦŨԠȂBӱŰ',
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': "ЍӸʺ'ѺJȽʊˠҔØό\x8fҢƂěȒƭŌȹΞNϘǩǗrϧnȮɜ",
                            'message': 'ƃĵрэӐīϵėӝĦϊƌƵѠŗԁҟŽśƑ¡{ҔȣðŔǃԑԍӴ',
                            'arguments': [
                                    ],
                        },
                },
                {
                    'icon_id': 'ԈǓԈƄªȓʒԟӖØÈɑŖmÔ¨ϛ\\ʺǼlŌс¿ɣҪҼÎŚõ',
                    'image_id': ';ԫŘ˱Ɯ\x81Ƴȍѵ=ƪʂıɗҹØҁДʺΩŶĒĶЯæмΈ\x9cӶЄ',
                    'title': {
                            'catalog': 'ʶӁɏɀ˜ȈɈ˺ӄ"©śɇǺČóҳα;ʈǏɆ҅њˢ\x98ͱʂǕʉ',
                            'message': 'wΟ˩хʟðȼӬÅԟȾԀÒЊʈӶΆ\x91Ͻ×ӬMǔұǳŦÃоþɯ',
                            'arguments': [
                                        {
                                                        'name': 'ɕ¥»ǝԛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182933.897708:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԢԂɯȢϛšQ\x8f\x91«ЉȪ!ԅʹʶҼˈʷʌȓĶӎÙԨZБӜ\x99Ι',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'æѝҒ¼щȴʰʫÁӝɫӓǪAθĞҋƠȷƱƴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182934.036918:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǮĹӂȏʇдɽȁȃϺŶȃtŕФϘøқә½}ӹӶĴұëĄЯƣΙ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182934.105132:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'õɚӳĈʊ=ĈƉĪƯŨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4021166281340802240,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϻ\x81ȜÈљƴʡуÍӣаҷ˵ԉϔ҉æɠĳ¿Ήϵԛ"ƁѻȊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ːƍӉˌͺəӹʸԡӫ˲ƶή˚?CИԙШԎøԮǙ\\OJȿңǱ˪',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '²ҕɔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'β¶ӐГӖūȓǻ\u0382Åͻǩ¶˳MѼȾ˱Ԥϸ3',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ž˔Ӯëқĭ;ŢǜwÀÙѿϏĕѣέѠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182934.533906:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': '\x9aȁǫГŅƦїɍƬUҒȠбӻһέćýɶôȟʌʗԉ]αѠ¦ÄҲ',
                            'message': ':ϯӓҋÌцϯĐϦ?ԪȸԠŽʅԡиϬ\x83ƲӵSƵ\x8eİԬƦȺUφ',
                            'arguments': [
                                        {
                                                        'name': 'Κΰȭ\x9aі',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182934.669905:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĂƲʒƷУ˟ӧҏĩȭԦȸǵɋǍŭ)ʳǊνġԬѶӌԕУĒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182934.735853:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҺΥ%ѵҵҭZȉұԒșɻϓu\u0380ƞÚеδ˃$ɻńϾиқͽҋҟn',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 992513.0313174252,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ζàɿŏ˶(®ȲԒЎÔӗæ˄B&Čȗі\x9eƼͼ\x84dщ]˂҃єџ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8060370587969046632,
                                                                        },
                                                    },
                                        {
                                                        'name': 'UüʴŖˊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϢѦưʼå҆ɕԄК',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɸϤʞĥɻǣ»ϨԥҔҫ7Þ\x83΄ʱґĨ(MǞˢʮιӹэ\x95ψŇԔ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˝˞сϦ˼ҊʆʅʲЪԪȭԐƂ%ɩȜʵ˃ļŖӰХǛїθǇҁ\u0379ӏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӂ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˺ɔÎ;ȖŢ\u0381ȐҞļͶņ½ȒĽӾǢжϪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӿǫϢǓʏϔwɦȐ˭ǉКǊʑƒęÀмĵ\x9eрü',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɕȔQƈѥɟɇ˚ÕYUίpΰƧʒƻԎ\u0381҂ǻηҹCӪ˒ÜʎZт',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ŝǐ+ØΡ\u0381ʢȯ³ɘӼƠĻƮӒ:ǥΦϊԄrȵʵĭĚ5ǃȯϱ˹',
                    'image_id': 'ЭO\x9cěȮΤѹūмϝЭƯƔ<п\x8eôӚӜҜԛФ¨ZǅΛŹҔĨҹ',
                    'title': {
                            'catalog': 'Ҍ˵Ǝ]ŤŚȝ|øāęƃзӢҚŨЎȧŉђĵΏĐ\x8cƮѸӟΥǷϫ',
                            'message': 'ǅˤŒŔԬϸКԛ˫ƩÍ˩ĲVӕʔƦԍ¶ͰȨúǴƌзŎʲ˂ĕ˅',
                            'arguments': [
                                        {
                                                        'name': 'ƑуƳƸԀÓ\u0378ɮ%ÿƶ҆ϑҬͳŔƬОѪͿ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7812008272822855054,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԙǕΫʺщAӘѥ@жĵкŷŸРшÂ$ìԓƲ³˵Βsǧą²Åα',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȧʳʒȇţųʌԮ˜ɋ\u03a2Śė˶ЖͰѐƸΒѶƊФiӓѕȠҋɏҦʂ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182935.642019:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ō',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȞΧлў˳YԍΧ;îԭӧɺÈ˞ƞЩ΅ƶʥŖ˸ȃvԛ˄ԑ÷ɘϳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȹǠϋȃԉ²ŽʧɶԖёG',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '}҇τϸϨ˳ēȂȽͱ˰Ҕ0ϻЍӞƽ\x84ʛȣIβʘƻ˾йϲɷѩǕ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҿҀȚĞˀÊӮԟӪǅîƂҰcӑħŇǹӹŉòʒӡР\x99ођƙʱƯ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƮˇΆĺӛȄѬˠɑmҶϗԌѻƭЍ҈ȘϭӘȊń\u038bʂɼƊUʻ]ð',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǭҼɚǸõύ˃ćʔƭњЗ¡_ӽÈsȘ7ӪĮˣОûĘɘŽȔӋЯ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 915134190328620591,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΙǢӢƿǹƉζҖҳ)ɟ©σL\x85ŘȸήѿϯÑʗΤѠԅԩţÃЬѱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'Ԓ³Ʃōʩ˧ǥūϣù˅ƌСłϺȠϊǝёԖɠԤȁʏ³ɓ\x82ҷơӺ',
                            'message': 'ӊʮԏŲВɅԓʎŇ¿ӆӤáďҙɪ˯uЕrϜ˟ȬѺɿŵѨȀѭҎ',
                            'arguments': [
                                        {
                                                        'name': 'åʭЏјǃǌԇ3\x9eˬдӻЎɌҙºŻоŋǲ\x87wŐĽƶҵɥҲǝƆ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 174002.23687116464,
                                                                        },
                                                    },
                                        {
                                                        'name': '$ѐöϙοŃϠʍѥ\x87SʴεΏҬҸƥɕʉGҧÝƇĪʃҪǫϰҁƑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 806596.1654682222,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǰGʏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѽƈ[ԫĀǻʤţıΑ\x86ϋɷĘbĭ\x8feǕКӣŅ·ϛɐŜɦΕʃÆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѱіԏԠ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '?ӊӖX\x9eЪ·Α\xa0ΞǩȐѦǝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'иӘҴӑρΫ\x87ΝɤʈЗ¢ΦʳƥȗԖǙı(ӏ˩ǵҸӶŶƻā\x99â',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6549509625683497888,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗǰΥŶқʊϱеȜΐѺʟ#\x9dӺĭşWūąŋǔʝ\x95˺ÍхɵαƑ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯɫǫжȭ˴ƍ\x93ħMԭ\x90ЈԒЗĳʎѱÀĊѨΕΕ\x8aзǫ\xadȷɝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2820379276767669737,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΒѾϛӅȍŽдJǪÍъƙˈԗ˚ΉѪӻϖӶӯTāϒåɦȃaÏϐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ϰˌô.ƳĉͼÒ÷ωƑ\x9fԜǻư˅ѣӘƱƢ#ɨҋҩ<Πʚ<Ӫı',
                    'image_id': '˦âӘ)ƕлƵε\x80ӡҝʇƘƶԑȑͶˡZЎȏǖѪяέʦǥlŢԟ',
                    'title': {
                            'catalog': '+ΣČɊЉπϟ',
                            'message': 'Ċ\x83ȟƅƄͻӛΟ\x93>ɴ˜ϖѣƙ*ƢůÎːȫǃϻȫҫƓĬӶȎǷ',
                            'arguments': [
                                        {
                                                        'name': 'ΟʋʾϴÁΧ˲ӆԘʌÈЂШ˳ŷʮƻûρҷµҶϡȘ¯dЖțаY',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2370573140906184513,
                                                                        },
                                                    },
                                        {
                                                        'name': 'łԄ×ʇДʻʫ¹ËƵ©$ʎ\u0381ЇȒԅΆЉԏɡƾùԀǻΎNŀӤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƳОюŦǌўëќǴȁ\u0378÷\x8b\x83ʕ¸B\xadÍӡȬρƫѸȅ`4ԛɶù',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 262406.40553503396,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӳŻȚxɣɾɶƛȮħϾʉԑћȟɆÆҴҶƼȵӐ˂ӰщХүʋ$ʿ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƈςʌŦʯfƉ˃ǹϤɉɛԙŀˌɧɷŜȟѝɥɛӉ3ÛҬǃѴɹ\x99',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξɠǇƧ"ɦ˪ȑѥ\x93ȋӧʂѬɪ\x81îϢѬlπēȔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'үĝhäӧ\x7fӖƎǝǣȷĔʌ\x83ɻ¥J#Б¸ѤюȢĳѯα9žию',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'žӼɔ҂ԔѻӲџѰˀҠŝҸϨс\u0379ЖУ\u0383ǿȃǫΚѠԨӘɕаһҹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8209235457564936272,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Җӽҗƕʕ:žӀ¥ȫNȧtGȘæŮȚлĪöҽʇΪ\x99ǭϺÌſī',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌӪąҹċŬγʡ\x81˞`ФͳȕШϘ:Р\x8bш',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'Жƚ˟ϱΎҡӉªԦ˵¤ʷӳƚŗȫȊαʧŢŒ\x8b\x9fҊƨ[ȘЎΖÞ',
                            'message': 'à¶АмΈӦǹE¦Ѱ˹έьȆˤɴҙǉĺӔEɘЩӛΛűƽԌŷӡ',
                            'arguments': [
                                        {
                                                        'name': '˅ɪȳɛҲԉԆ\x81ˍòӽΚӤĘʨԙăɍиφƵΞҭǠɡǶҊŘÉʙ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҀКԂ˖]\x9cĚǷǥȀ˻*Ϛ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӟȄ@˟ѠЬɀÜĸ\x81áҟǬĔʕö/ɒʮΈŰȑæǊ¤ɸӺī?Х',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЕΘʺj¾ԏ˖ɕΚȣŒ҇ªŁȭȂϏͿӹ\u0381ȠÛ²Ų\x97ΟϸВɷ˺',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '^ƠԬaѧfNΔʙϸа˂ʁϬK϶Ń˶ɝƖ˫дŻ˾ĄͶӥӿϙƙ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˖Ϭɹ˕ϰŖҫǼFǻϙ˥ƽͼɣϹуЊŞπΊÅǿҊԇȱÈ\x9f',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϤӵϊǪɛĐ\x9cɀɮũѾŎȇǛȎƊȉӢ˾ԀуӡΨɌV\x90',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2549473580031780457,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҠģӬˢгùɦ\x97ͰýīΚƀÏηԤȌͶ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ' њϱőʼӧһhǨҼǉǄ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˼ѼѵɿɍԢЦĳő\u0380ΣřӢƔʟŋʵѢkӔʁ-оâѦгλåƋқ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧӷÂЋƭјӤb·ōМïʼǦǮǓƛΙųʃ¦ϺĻƨ¦ҜςʛԒǒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': "ӢѽωʡӅņˮƃϦКӳАŚɡɹѼѮ|ʸ'Τ¨ѥϚҫϻҪĺɄɾ",
                    'image_id': 'ƾνҖҵˢҨȝТčȌѣҎǨâƿÐêυηцÕеΉǉ;»°Ԍː,',
                    'title': {
                            'catalog': 'Ñ\x9b±ʼЛǝʫӞхʁǎɒԡΖțÕĳfӾѤìXÁЕҘΆĩˢǗˁ',
                            'message': 'ԩ×Ǘ˘»ġʝΞϻ\\ˠǅǧɤÌӫҥϏцӌǖԀŜɉƲƣÚ˳ҩǢ',
                            'arguments': [
                                        {
                                                        'name': 'ǜє0ʅĲĩ¶Ϯ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '·ʢ˧˥VљͶĩǡĴnǀĴɚĨӥџҙƮй˗һȴȘԎĿĚˌ7Й',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Үʦ`ĳϟȲɰϯğïѮ˟öϳ\x9fǚΙ|\x99Ɇ˩',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϗʖĞÓĽӗҼÑ¶ȰgӤĺ҂ϩ=ɔ˳ӰłƟϋĂË\x93',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'вЦӭӄĝӉǗ§ҹλɒȳԝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 12049.293771161843,
                                                                        },
                                                    },
                                        {
                                                        'name': '҃ÕƱΐÞǻċЭ΅ºЬÝƝƢƇÜл˷ǋŘӋƵΥԁ˸Ȍõʯ@ε',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'aɓϿΑʖωƪùʌђ·%˔ăžĊƬȰĒόɮŊĵð҅κɵŰѢπ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґƅƄHɐȮϛǒ˼²ȑʰɉÙӮ˕ˁʁӷðϒ0ҳԞҍѲθΝŚɬ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 517192.1057971895,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԌƜ\x9dТȹѥ?˕ԋ˂ԟϽīˏɼ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƻаxË\x8bΫк',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƦѕӺ\x87ÐƍË³˦ǗȋҏϱĜƁήœǷϻԓӋʸҾҶΆƪĴĆҗǷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': '\x9fɡϩѼàφ˛ĺӛ\x92ϋ©ʹȰæТưШʡƩdŰʉȋţκ¿ρɅǡ',
                            'message': 'ɺЯ§gӉùԑ\x93ȕӥØºЫљǴÆLbt\x96\x8eюɳƌʶhɒÚőĴ',
                            'arguments': [
                                        {
                                                        'name': 'ųXҦǣӗōčɾөιͶŅɢƗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȦАăʘԩ˚\xadυΈȤƟlΞ\xadƃpš˓Ō',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'НΝԩѠѼ˳ԍϱΆϭõѠυЭæӖĽίѶǼԅЪŉĝʿŸťζǫ˲',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ҳƤġϿҵҿшʭʠŃӃǵ˗҈˨ĸϭİʘѪȊ)эфŐŔѼɏɸï',
                    'image_id': '÷ɯ҈һӧ˅ǋːɻĻϨГñʲĜŁőƑϮaĪȄʃӀșѲƙґʆǁ',
                    'title': {
                            'catalog': '6l[Ēǳ˵ϻ#ʬЗӘѮɿңʔӵ(ÈɑĢĜ<ԪhӟͿ',
                            'message': 'ęÈȣȰ˘2ѐūφž͵ǽї\x8dȾǬƹɉŀʒμӫҐ,ȏԓΝĴxɠ',
                            'arguments': [
                                        {
                                                        'name': 'ђԑμˢȫś\u038dїÛñĸкń˂ŕʌѨǃŴEԚ\x88ͽȣ\x9c+бҘEЋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϣνϘʾR·γ͵ʢʢƢɛÆÅǫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182939.867454:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɂнğċқƎÐƾQĚņϧԋЦ\x83вʂӲ\u038bɅтûcͳȷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЏίǘӷƯņɱ?ŤЗʐ7ʕʝɳś\x9f¢҆ԏùЩӃĵΎΒ\u03a2ɺĹӭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͽΨЯưѾӸԢƸŮξ\x9c4ʘҽǏÜÔͰʷHǵѱŭЂϕɂў.ѻt',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯYƨĠĤǔȯƖÌͺϼͼ͵ȗΩфӓʔŕŔ҄Ù˩ͷƕΥ\x91Ѭ~Ɉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖVͻҟΐ˪Ĕǎ6Ғ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '[ʡÂɂĩ\\ǳоǎć\x8d¡ĝĪƘŌɀɖȏґЯƏ҄˲ĎƀʊϤӁϥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƸȆ·ʳDȜȓ˒ÑԁȒÐfΊŗЪǵǐĒԦ\x7fĤ\xa0˗Ǡ¾ɧδ#ɽ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'с´ζʊéĥŞşi\u0381ϨƐȷǜʚˀɞöюȡªѐ\\ƗǷƑĎұѳα',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5271928464622226589,
                                                                        },
                                                    },
                                        {
                                                        'name': 'і\x7fВ\x85\x94ȩԡ³ŻчϜŀЪŴȩǚ-Вdͳʜ˒ǐϥ\x9bσљēӁȕ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ʨӶʦþēҹΝaöѿєʯҸ\x98śȑȔ\x7fʬΨȻĽśѕǪȗƆ·ƶÛ',
                            'message': 'ƙэмZƢ½Øͱȗѵȑʢ`ɡǶȱÃɔȲˎʊąǊ\x82ҧяӲéʩò',
                            'arguments': [
                                        {
                                                        'name': 'ƪɲфР%Ѧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'LõӹŢŇƠí·OǢƤʩɉÂŤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀȇǚЁДɐƚ\x85ƣȶϢӾ±ҏ¯š˜ȘǮҠΟԀʉÏ˾˵˾ͼèŨ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӟ˻ǜЮƻïǃԫ¶Ɛ\x81ǡϽĔĥаӖ§З΅Ӵϳ\x9f',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'áèҿѮ˼',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5038931055767259817,
                                                                        },
                                                    },
                                        {
                                                        'name': '±ǁˋͱˊƊʜ^νɳęjˉыʬԉδж˫ƢїηɼѪřӉCѓЊқ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŅшĆÜ\x94ϥȩģɞяʮÅ:Ó&ҨɈ\x84˔ҨҺƵB˓ԀϔΘўȯɳ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'dGҸ\x9a\u0383ſɕͻŮ\u0383˒ɕΓ˻ǆɉЕƮŨԀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 897875.0303047864,
                                                                        },
                                                    },
                                        {
                                                        'name': 'YɌȾNƫȓү',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 765213.3750549975,
                                                                        },
                                                    },
                                        {
                                                        'name': 'к¦ñ\x8bԓӹԕɡɏšΊԔʊúřȨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾ\x85ģ˅Ǎʳӽ¥ŪpæˌďŒ*ƘӲxϊæЩ#ȘZЧ/\u0380Ƃoø',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
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
