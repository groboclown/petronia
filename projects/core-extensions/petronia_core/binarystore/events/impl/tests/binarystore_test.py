# GENERATED CODE - DO NOT MODIFY

"""
Tests for the binarystore module.
Extension petronia.core.api.binarystore, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import binarystore


class StoreDataRequestEventTest(unittest.TestCase):
    """
    Tests for StoreDataRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in STORE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRequestEvent.parse_data(test_data)
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
        for test_name, test_data in STORE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STORE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='mime_type', name='StoreDataRequestEvent'),
            ),

        ),
    ),

]


STORE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'mime_type': 'ǰɈŎȣĦԢʲʳԩɐȯȠŬҧɂԗǫ˺ϻΑäǾҮќ҅ѱāӵЀ\x9a',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'mime_type': 'Ԭˌӟ',

        },
    ),
]


class StoreDataAllowedEventTest(unittest.TestCase):
    """
    Tests for StoreDataAllowedEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in STORE_DATA_ALLOWED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataAllowedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STORE_DATA_ALLOWED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
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
                res = binarystore.MessageArgumentValue.parse_data(test_data)
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
                res = binarystore.MessageArgumentValue.parse_data(test_data)
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
            '$': '¾ΟĥʽŠ\x80ϨĦˢäÊЧȀȠʘɲǄˎȷȯʹВ-WҦ˂ɢсǬ΅',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4174174989778233035,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 22553.663765949517,
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
            '$': '20210910:182719.313278:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '˨ЏéØɔǒԀ®ŊΩǨľćн˲πÅȓφʍˢӳʘy2ўɜʵΒѶ',
                'ɘʷȫŰӕŴɷҩ˜ʈ@ǔԃɏҖҌʹʀҽBǮΙЧiӈҺԙѪҰƦ',
                'Ĉ)o\x89ЮϘȸŏâ\x96ȉʠŵƶŇʱ˘ÝɕʕūŪɭҷőưųȑԁˬ',
                ';ǳɵȊt\x99ңɀǰϳ\xadӢжĂԚɳƅÕΎÝѕǦЗΠϷťȘӌûg',
                'ϠҪηûǕДGĨԈȹѱȮҋğМ¶ʋӒѝŅџÜċţ\xa0ўϕʖŨί',
                "ˡȥʅԅ˽;Щɜē˭Σ'κǀɦɺĿǏɔµņŋ?ȓˇɘЪzΟџ",
                'ǯϝ\xadП!ęƛӯΉŵɅһëɡ½ȏӋǗӉγʜĬҏ>ψĦ˒dûȈ',
                'ӝцƫÁ˔˖ÕԀą\x87ʩǲϐЮȖҺθɢȵѪПš!ʤɒιʾțϚɍ',
                'ɺȖ<ɣkѲʚēτɘ϶ЛʵϝԉʖҨԃģԧùȶ\x83ԡϏʞ¡ÙӼѥ',
                'ԞŗX҈˘҅6ƉˀɕʫǖǸҬԨˀƭňȔ˅χſοóͰnЁŦǲƮ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -4501668919450141739,
                7146490502801428474,
                -6947122650053853399,
                8689949246877170247,
                6719631591546064583,
                -2177864795731373133,
                -7896586976447371242,
                3285153048278848646,
                -9018722677411602644,
                -4126085112178714889,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                79195.1896437477,
                633631.8159712973,
                532293.6212316357,
                855366.9342639863,
                496663.0095170761,
                936289.1515127358,
                751473.4575852177,
                187915.86046395567,
                399471.9550922866,
                656609.0050614545,
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
                True,
                False,
                True,
                False,
                True,
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
                '20210910:182720.351675:+0000',
                '20210910:182720.368952:+0000',
                '20210910:182720.386003:+0000',
                '20210910:182720.404986:+0000',
                '20210910:182720.422261:+0000',
                '20210910:182720.440234:+0000',
                '20210910:182720.457571:+0000',
                '20210910:182720.474829:+0000',
                '20210910:182720.491949:+0000',
                '20210910:182720.509829:+0000',
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
                res = binarystore.MessageArgument.parse_data(test_data)
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
                res = binarystore.MessageArgument.parse_data(test_data)
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
            'name': "мɦӔâЏө҉'ǃÌʾҨ<ҕʴȹf_ȵԎôҸɪ½ӊ\x9dқӥĠΨ",
            'value': {
                '^': 'string_list',
                '$': [
                    'ï9ԠŴƒxԒӑŪҾȱ^ȱȢƿʅҘЄ˵ϙjǯαÈ9Ӝ˓ҳĉЛ',
                    'ɻĂϷԮ˒\x9f˃ȵūѣýҞϲ3ƴƍϋԠlӥÓxЄŁɏFҥ˘Аɿ',
                    'ҠϗűȲϒɒяԤ\xa0ƤΛ!\x8bƉҩǮΤѝ\u0378ͺѷǢВ˂âǆͼʯϢê',
                    'ƘɇϻѓѿӉʲɨҧǝϏфΧșιαā\u03a2ʋʾҚɲϋǷqqŪΟ ι',
                    'ưΐǤƝʭδяҾʓºíЪҘ¡ӆèтПǨҨǢ\xa0ʰѺɋԦȊÎǫӫ',
                    'ͽԌӗɗ\x8c\x85ʇÒ҆Ђʙ\x82˱ɱA)ɛЅѫǇřǓʠӽʧё˺ϚЗΔ',
                    'ҎĹ˦ˢ\x83ğΰӉϭȃ˃¦ɛʞĈҕ´ŅΧűВǪǜ\xa01ʶ˶лǙљ',
                    'Ƨȃ\x8bțò˥СӛДƔʏʠӇ3Ʈǉ˽ѸϲϙΜү˯ŏТԨ$ȰÝϱ',
                    'ЅÚϨěńĕV˸ǯѵϊмɺ¹Gӽё¨\x8dɉγҷӔʎFӋˬ˞ǧe',
                    '˺\u0379ԡɥaͷɽЩē҂ѽӨΚƠI-ȇΒâтʮϨFi.ȆҗɊ=ʮ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƣ',

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
                res = binarystore.LocalizableMessage.parse_data(test_data)
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
                res = binarystore.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ГʵҾɳƖѻƣüʄӮҖЁʊԥқ˃Щϐ\x8dȷÝϼӦҟŲҎӲ\x8b˱É',
            'message': 'Řəщδ\x8cѺαʖЕйƉ\x9bӯʓÊÝ²\x8dˍǰЊɳˣѪο˂ЋѓŒԩ',
            'arguments': [
                {
                    'name': 'КϮnJɘ~\u03a2žӀԬʤѐ4ɶÁƠӺԎқ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210910:182716.898057:+0000',
                                        '20210910:182716.916034:+0000',
                                        '20210910:182716.932778:+0000',
                                        '20210910:182716.950790:+0000',
                                        '20210910:182716.970310:+0000',
                                        '20210910:182716.987928:+0000',
                                        '20210910:182717.010830:+0000',
                                        '20210910:182717.031129:+0000',
                                        '20210910:182717.048025:+0000',
                                        '20210910:182717.064800:+0000',
                                    ],
                        },
                },
                {
                    'name': 'Ԓ,ǞOǀɡĆίӄįԐÐʜҪÊʐ\x85¦ɬƽƇѡ%Ⱦľ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
                                        False,
                                        False,
                                        False,
                                        False,
                                        False,
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': '˂ʙɀѼȋ©ȈÌ',
                    'value': {
                            '^': 'float',
                            '$': 493133.03252657084,
                        },
                },
                {
                    'name': 'ҦÈǩΤɸ˭ѲνÎÕҋϷˍŻĺԘǌӌΘԟ-Г\x7fЬ\x9eɵÚǥĨ˓',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
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
                    'name': '\x8aKɒˤϥÒϤӅҔоfžɋªȩǈȢƧGtĞѹґƧǑuŢ+ǲҶ',
                    'value': {
                            '^': 'int',
                            '$': 3773087802043807175,
                        },
                },
                {
                    'name': 'ˊϰԆˠtʟʲcˆȕГǃȐǩʃЯzӌўѕԦäюıǁ˅ӒǶЩȣ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
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
                    'name': '˕fhs˝',
                    'value': {
                            '^': 'string',
                            '$': 'ԥŃʔϋŝʆˌjԑäųˣˏȐƮɐΚȁś8ȀļЅ\x9b\x90ϮŋɈцÖ',
                        },
                },
                {
                    'name': 'ҏ+Ѡ˚ϺĳԪʮτXԔĭ\x98üǚѭ´ƮϷɌ҃ñȬÎĨҳőµƅF',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:182718.137838:+0000',
                        },
                },
                {
                    'name': 'ғϗŮ˟ǫ\x8e´űĀɮѡιƱ\x91ɣ§ǘ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        7271882500618606737,
                                        2412268089564246368,
                                        5341543000723186239,
                                        -2690342250345554332,
                                        -666959892257033026,
                                        -706323087979634832,
                                        -6367284553405087565,
                                        -2284623415055778275,
                                        -1273136449967065361,
                                        478178791997885834,
                                    ],
                        },
                },
                {
                    'name': 'ĩӀĦ˳ȍ\x83ƕəҮӗǄҕfʺΣÐэ\u038d˞Ėˍ\x8eÔήǘɎĸ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        True,
                                        True,
                                        True,
                                        True,
                                        False,
                                        False,
                                        False,
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

            'catalog': '\x8eѧ',

            'message': 'w',

        },
    ),
]


class StoreDataRefusedEventTest(unittest.TestCase):
    """
    Tests for StoreDataRefusedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in STORE_DATA_REFUSED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRefusedEvent.parse_data(test_data)
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
        for test_name, test_data in STORE_DATA_REFUSED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRefusedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STORE_DATA_REFUSED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='reason', name='StoreDataRefusedEvent'),
            ),

        ),
    ),

]


STORE_DATA_REFUSED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'reason': {
                'catalog': '8ż˚ǺЄҍҺÿwƨȐŮϙŉthήȧϕǳƒ¦\x97ʈΗ\x9e\x83Ϩ®Ӡ',
                'message': '˷Ǒ÷ǯĆτǚʺʂԫҤƹŗЯƿЗωɽŴsΰǛǮӚǀԑςȺςȭ',
                'arguments': [
                    {
                            'name': 'ųҽ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ʓ®ÈЇfΦӐѕǤӍÉыäӔҫˎΞќƎ\x98Ϻȥв',
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
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΥαCҊ˗ьѰôË¶Y˷Хù¥.όǞƐͼҤǬBœęï}Ӂκϝ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210910:182715.322358:+0000',
                                    },
                        },
                    {
                            'name': 'ĵюǽОrƞѕmѿɎѺԏ>ĄȴĲӢΐǊԎΛ\x92ӡ˩ӮηʈљȈϥ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        667955.5285508593,
                                                        198021.14873104246,
                                                        591973.322376137,
                                                        554724.409831663,
                                                        531834.3142908728,
                                                        653928.9906947796,
                                                        -77256.92527189542,
                                                        422112.6555284835,
                                                        513607.3848168113,
                                                        994323.8737054279,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӖόĘǾĎɊϙϞ>ӇƣöӜҟ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        4101245437061387265,
                                                        1824510229957383914,
                                                        396682580895177819,
                                                        -8892266056570393476,
                                                        -6009224725353927224,
                                                        5057704149729948882,
                                                        6699258098991885643,
                                                        -2499441174631224903,
                                                        -508895909946507123,
                                                        3660355235839987734,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ïğԛȵËԗĮ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Õ^ʽQʼÖǀԑ\xadͶʠԧΊŲFɻΤĈфñʧƁıȇЛСЁȓԢ\x83',
                                                        '+ąɸȱǰ\x8cIԨΤɅʠ5ɠ˘ˏϰ\x8bΙƏ·ӀΚȱƗяÚġжĖ¶',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ѳ˴ɗ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'QĦѡӌТŗϗ~ȳŉ˚ˉàªAƒȪʸɺʺɌԬƀҪҳï\x8bȈâ`',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        768740.5481864106,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ˡӊҥȃʩθΕ˨΅)¨ƪԦ«ƵџǼ҅˕lΦԉ¿ȓϽȵ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                        False,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': '\x9fėӓŐ-ač',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
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
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'reason': {
                'catalog': 'Єυ',
                'message': '˯',
            },

        },
    ),
]




class DeleteDataRequestEventTest(unittest.TestCase):
    """
    Tests for DeleteDataRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in DELETE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DeleteDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DELETE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class DescribeDataRequestEventTest(unittest.TestCase):
    """
    Tests for DescribeDataRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in DESCRIBE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DescribeDataRequestEvent.parse_data(test_data)
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
        for test_name, test_data in DESCRIBE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DescribeDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DESCRIBE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='store_id', name='DescribeDataRequestEvent'),
            ),

        ),
    ),

]


DESCRIBE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'store_id': 'ςĶƢ,ɧΊҁ¼õÔƺʳѲĕǚҧ\x98ũҵǂǤϡ4âҜ҄δdɢ«',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': 'ƃȬʐ&Ɨ',

        },
    ),
]


class DataDescriptionEventTest(unittest.TestCase):
    """
    Tests for DataDescriptionEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in DATA_DESCRIPTION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DataDescriptionEvent.parse_data(test_data)
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
        for test_name, test_data in DATA_DESCRIPTION_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DataDescriptionEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DATA_DESCRIPTION_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='state', name='DataDescriptionEvent'),
            ),

        ),
    ),

]


DATA_DESCRIPTION_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'state': 'deleted',
            'mime_type': 'Ɏԥ©ȭӯ9ʹɍʸːӳćÎ',
            'sha256': 'σƨсrʵͰŒ\x85ĎʺғʾҍɖєǷŸƀ\u0380ɞҔĄϬɉĈγť*ѳŒξҨ\x9bүζ9ӈaţȎzȼoėϮ˦ηӭДӈʩ,ŲØ½ҤϣǫƘJϹЧĴΰ',
            'size': 7679586183549282657,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': 'deleted',

        },
    ),
]


class SendDataRequestEventTest(unittest.TestCase):
    """
    Tests for SendDataRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SEND_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.SendDataRequestEvent.parse_data(test_data)
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
        for test_name, test_data in SEND_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.SendDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SEND_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='store_id', name='SendDataRequestEvent'),
            ),

        ),
    ),

]


SEND_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'store_id': 'үRN)Η"ѺςγƲ:ºΠȺәУһӳΌǔҤèеNέ\x97ϐϕʟȗ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': 'Њēlξμ',

        },
    ),
]
