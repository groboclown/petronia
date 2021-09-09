# GENERATED CODE - DO NOT MODIFY

"""
Tests for the hotkey_binding module.
Extension petronia_core.hotkey_binding, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import hotkey_binding


class BoundEventParameterTest(unittest.TestCase):
    """
    Tests for BoundEventParameter
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_EVENT_PARAMETER_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEventParameter.parse_data(test_data)
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
        for test_name, test_data in BOUND_EVENT_PARAMETER_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEventParameter.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_EVENT_PARAMETER_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='key', name='BoundEventParameter'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='BoundEventParameter'),
            ),

        ),
    ),

]


BOUND_EVENT_PARAMETER_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'key': 'xҌӫ\x98ȹź4ʲэʃƾЭξÍȾпӇƼ\x80±зϣ˜GǓҌХʟŀǱ',
            'value': 'ѸҝШ˔ԠЏ˂ӿ§ˑΫίϛјӸ˻ʉԋԛӭЬԏsϣӞЊũɞɞò',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ҽ',

            'value': '',

        },
    ),
]


class BoundEventTest(unittest.TestCase):
    """
    Tests for BoundEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEvent.parse_data(test_data)
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
        for test_name, test_data in BOUND_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='BoundEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='parameters', name='BoundEvent'),
            ),

        ),
    ),

]


BOUND_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'target_id': 'ŒԈѶǻөϱ\x88ŪƏǵːҷʏϴ˖ү҉ǯʃƃëǤýǧɧԏģƣώ˰',
            'parameters': [
                {
                    'key': 'ИƉгhϯϨΧ\x9cȇтõԅӁʥLǴ\x8dőҤǖ˾<ʲԥɬ\x95ӧŘɤԐ',
                    'value': 'ΤΰϣОқ\x92ͿĭƅǻͳƷЇϙҘʿ4ƆĠAøÏЎ˻ɸȶΜ&ѬɁ',
                },
                {
                    'key': 'ҊǎȝŢþȀɭƜԖҐ\x8dҏσ#ɷɿͰďцӯǶɤϸ¼Ş°ζȩĕʀ',
                    'value': 'ЗСΆΆѫYӹЛ\x82ӻΠЂӷƏǽʰpѸùƜƩȊŖщ\x8bǏŠЮԫӈ',
                },
                {
                    'key': 'ҲȦ˅ːB\x91ſǺȓƦӐòˋvɥЅһƚĖǐΚ¤ӎҿǑţ~Čˍћ',
                    'value': 'Ǩõ¸!ę*Ƃҍ·ʷӷЂŏʌȲԮʷΞʷҙƯ¡ʅμҵȦҿҏʁΧ',
                },
                {
                    'key': 'ɛЧӆƴѾяĶȾʱˊĲӈʇΎɓqːĿčŝԫ¢Ư³ʀƤǨԌЏʿ',
                    'value': 'şƱʏӜϥŞɶҤԣ˭Ͼ¯МӨĊǆĄӯѷĴʘʀԕøԥʱƧŀŇϊ',
                },
                {
                    'key': 'ѭ"ƵǶ˝ȾĀUƗLĝϸξӚɻǃΕȟŹ',
                    'value': "ľöɒѸόʨΈΏӃ\x9aâǩӞǍŋƢвѕԁnĄĸӆʞЉ'ȝäɃμ",
                },
                {
                    'key': 'šĽӉΜΠϗ\x81ǫȫñϤɘόҡtǢϱΩſɘӰ¯yƅΥԮҵƥɯҎ',
                    'value': 'АɭаʡȚЅxȳɸԚΥɃü¹¦\u0380¤w͵ѡŔЯ©t»Ƃɗɩʁĝ',
                },
                {
                    'key': 'Φɋ\x9cгéΩƐνĲï;ƴ¢ɺ\x86ʍ\u0378ΎӃ£ӘțʧƜӱԆƪǯΙ¬',
                    'value': 'ѹƀόшξĮÜҾϕêҙȉӯӺɬ˂ѵŰɶĥӡрϹƶ°йɧŹΩʘ',
                },
                {
                    'key': 'áȕάυˮ?ƆӕʸĠȮˍϕљ˲ȂYʳtȞǧũϧɒEєґńǽɵ',
                    'value': 'ԭ\x8a«ϼ҄˰ˍԐҹҞÓʞϩďůҿ!ʐԣϿȤʰҮͶƦťӛƀÝƬ',
                },
                {
                    'key': 'Σ\u0379ΪΎǇϗϟԭ\u038bƍͿ϶ÞӈʹӧɼȪɞĴŴΩΑŜ\x81˫ī˞ƄĈ',
                    'value': 'ϊʃŴƣȪҡ\x94ÃԙŴɅʙ÷ҁyԟӜҡ˯ϐƮɅxпəтƴԣɥǙ',
                },
                {
                    'key': 'ɤĠʑʳƪǈŧǘG˵ȰǥǻŽ\x8eǃ҆6Ϯ',
                    'value': 'ϵʎÜčЯϊÞķµӸƁЊћȥˉĽӓɅǒоƬӀϜ"ȴɤ˙ȝȶϘ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ԋѰцˇк',

            'parameters': [
            ],

        },
    ),
]


class BoundHotkeyTest(unittest.TestCase):
    """
    Tests for BoundHotkey
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_HOTKEY_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundHotkey.parse_data(test_data)
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
        for test_name, test_data in BOUND_HOTKEY_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundHotkey.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_HOTKEY_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='BoundHotkey'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='event', name='BoundHotkey'),
            ),

        ),
    ),

]


BOUND_HOTKEY_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keys': [
                'ŉϔµӃм',
                '}ΎƉʥ¿',
                'вԥƄ˜ύ',
                'Aɬǥ',
                'ƝӘ=ԧ\x98hȬе\x82ХǧƤʫǠϋЊ}ɐӍћ',
                'U»ίŋѠçŚʧʞȓáαȪиɄȳͼȳʰaԖġїДë',
                'ӏÿ',
                'ʋԝ',
                'ʚ®à˛ʽŨɧӧӴɉԖ\u0378ȇĔҌ@į',
                'κӇΎϺņ',
            ],
            'event': {
                'target_id': 'ьdǛƆȮ4όЪɨɩǑѹȇȃɩІИ±úĈŊȡ7˹ºʐĝùɿÐ',
                'parameters': [
                    {
                            'key': 'ţȹǊѦȃəҲЙӭǹǱ˱ɤԮ\x83\x81ǬʭӹhŏƂǥfӾƕďћȭć',
                            'value': 'Ԕһӟ4ӫˠŖњƖƂρ϶СӘнƬĳp˧lюԥǍĿЈд҅ʒθϚ',
                        },
                    {
                            'key': 'ДљʏԣήҌʷĈ΄ɶě˰Ӊ˳ͽϧ˂ԎӕzČ˜ȏȚΫ¨Аˉ΄ȯ',
                            'value': 'ǕƠlςԣϙɧaСνΏɸ\x8eӺɌҼлϰ\x9fɽÞσ˳Ƚʱ\x84ɑϋҘI',
                        },
                    {
                            'key': '\x9bɨZ%ǩѬȌκӏʣǊцѰĿ˹âɿӘʸ\\Ͽ˂ϭӄ^Ȓȹːɰѐ',
                            'value': 'ΰÌǢʗ&҆ȞǩԘµȦγʃ1ζȸŗӿŦԕрÃǎĸ\x94ŋξȑȑĥ',
                        },
                    {
                            'key': 'шĝɭʵѰʹǗϽ\x87ӖήnϬӈʈɩ˻\xadGή\u0382ЍàʦÂsҶΑʂө',
                            'value': 'Гǐǆ\x95ɮɰєʂɥNŖͲЮϚI?ʤЭƋԢςҫƥȰ§ОǾӆϿʰ',
                        },
                    {
                            'key': '˺ңĩӮȫхԇѡӎϾїВԆ˭ŇшԅʮǽυŚƎйЬ3ÏɗǎяƳ',
                            'value': 'ƅ˒šЅԝŮãτʠɹӉҶϹ\x9bŅˊұҷ²ˉϱɀοȣƘÙ˴˨ǍӋ',
                        },
                    {
                            'key': 'ӤЪҢAӬɋ˥\x82ÓԋĢϝ˦ʯС}ʗɘҲΪȐǾ˶ńԄҴҗħŌϗ',
                            'value': '\u03a2ȣǉԄ\x930ӕʕäѐɋЄҋΪѨҵыǽ\x86ǿќɢҞЀʿâт)Ɔɿ',
                        },
                    {
                            'key': 'ǵʒˉdŕƀθԅӑˢʃӕɚкjʗ]ӽǪЪ\x9dΎ´ɕџ.ϰx',
                            'value': 'aҡшĿҿԚԚҊīԌˬnүϞčєǯɿԣԠљнȴơÊԄƮξԌģ',
                        },
                    {
                            'key': '\u0381ǯԊĻĪɯ©Ȥ¯Ʊâҵѭǐʨ\xa0Ӵ˰ȉcƧR¨',
                            'value': 'ŨƳнԒőϧ˙;:ďӶă˽ǛÚԢԍƺԑȝɣһɼƻ\x90ƠȳT4Š',
                        },
                    {
                            'key': 'ǠʘΞȟПԕϘ˯ԧѪҟϿŻēȑȜʨǰѧÅʏӷʗÇԇÖH=ãл',
                            'value': 'ҁѭ%ßҗƍˢ©ҴѰɳФϾϪӹҼӊ˾\x849ǿ',
                        },
                    {
                            'key': 'ķӟ˷кÙϞü˭ӑПȐҮʔĝ\x9eʗÁԭӱˏ˻ʊИģĵӹʳʚεū',
                            'value': 'πԇɝϣǇ\x98ΰ`ő\x9aĕ˹ьфßì\u0382ҴʂHɴİǮЛнŀ/äО\u038d',
                        },
                ],
            },
            'comment': 'ƐӠƢĠ\u038dӂƑС;θȑŉ˸ʵӞǆʿ4τϜ\x8fťß±ʅү˟ņʥs',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                '¹',
            ],

            'event': {
                'target_id': 'GɁĿЂЦ',
                'parameters': [
                ],
            },

        },
    ),
]


class BoundKeysTest(unittest.TestCase):
    """
    Tests for BoundKeys
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEYS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeys.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEYS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeys.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEYS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sequence_type', name='BoundKeys'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='master_sequence', name='BoundKeys'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='bindings', name='BoundKeys'),
            ),

        ),
    ),

]


BOUND_KEYS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sequence_type': 'sequence',
            'master_sequence': [
                'ƼȨYŦĎÝǞʃēė\x8dĘ',
                'ŲΫǫԦжȼ\x7fϡ˨\x93ƒʫǡ',
                'чƦ',
                'ă˨ÇˏɻНȪȪ»ʠΔȎŸʧ',
                'Sҵ2˧&Γ\u0380ʒŇŁКȢ~˦ʹȷ_ĻŏҹuȍÌǕǟ',
                'sͰʮӷ˚',
                'ʻ^ԎǉЀėʹҞǬƞ',
                'ÒλНШНȲɸĴŞʥˢaоǛΎѓȮԕZȌϠǕ£Ŕ',
                'ŵ˵ǡ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ąƓԮҲǺвȗіŻѢӔƊ',
                            'ŦͲ˵ɏҤԏ_ԏѼ\x9cʪҡÎǏBϕГĨȗΘ',
                            '\u038bÎ"8ϞƯΥFȿЯ˔ƋDµèˢɜŵԢĥp·ǽҒΏȮ\x92Ȭ',
                            'ϷȪ6Ȟґ9ª',
                            'ԟØΎϯҒ',
                            'ƙÑʉȆ͵ΏɡŎҵζχúϨƬѪХΓөĦҁӧҾżȸB+˵Ą',
                            'e',
                            'ƘёҵƘʏΙÖԢfϯЎдʛȩҔȸÏǷ',
                            'ԇѻL\x97ŕ\x8dGЀΧ˼ɦȑíIϝϣϽяǎŁŒǪě',
                            'шƽÇǖђΤöǞġϘ҃ņχêȮѨҡ˽ѼúιȒπѢљʶŸȥ',
                        ],
                    'event': {
                            'target_id': 'ŊӥªȰɰWɨ\x85ʃӨūҩԈǼмьˋŇ÷åđªƯӵģÅΡQθɩ',
                            'parameters': [
                                        {
                                                        'key': 'ΨӄȿėŁϥԟŧjЌːØȪɅͱwşҹî·˃ȻÑҔɔxӝӃϏǅ',
                                                        'value': 'ɤËӆŔ\x9dҡЉϩӎΆӱɽʭơɨ³ƈʫʫсʓȄ+ыȝєŧR˦ѕ',
                                                    },
                                        {
                                                        'key': '¢ȖʘɾǸȝЧT˭įѶȠӵԆîoҩђŉϡ³Χ"\x9bɽąŢЌј`',
                                                        'value': 'ӒʄҞА\u038bɞ\u03a2ɳƺшǍɸʛХһːӜ˰ϼˆɿí¹ӫԉśʖɖ͵ұ',
                                                    },
                                        {
                                                        'key': 'ΘñҺGҾŜ˔ʺĹϫ\u038bѺ˲ӝϒяɉʴĪӔЏʝŐә˴О;\x99ҋu',
                                                        'value': 'ÿȐƳԅԡЙɩƧΨȯðˌϦIùÙч°ǛҟăsȠΜЬÁʾҁ~ŭ',
                                                    },
                                        {
                                                        'key': 'TȒɪŒŔ\x88đRʠŰЅςȜ',
                                                        'value': 'ψƷï¯ɟȱ\x96ƚďËϪŁƗӿǂ@ÂϷJѿԐʑπːAñ˷\x91b˵',
                                                    },
                                        {
                                                        'key': 'э\u0383Ùƻ(Ӿǂ\x93"\x97ϲ&WʓɮȪƄǨƑȖɞΉnӂÇӹЎŋжʲ',
                                                        'value': 'ǸЂχ\x8fËҙz\x8bӇϯ¤ôΨğ×ͽʃʮƥ˶\x80Ҋ·\x89ǽ˓љťҜǛ',
                                                    },
                                        {
                                                        'key': 'ʯϞąѨΏЕjԚǩԚDӲƺİĎȧҦǅӇόʂbÚĉιǉРǌӚӲ',
                                                        'value': 'ԔͰĦӛɃŁͰԄ\x93ͲʱĢҧˉӌĈԬўϬβTҙȱɘрΒѦӣǍÖ',
                                                    },
                                        {
                                                        'key': '<¢ɮƆϽɽнǙȖ˲±ǢŘɱŰåņƂƕАϹϚҸ/iԂЇ\u0380ɐҏ',
                                                        'value': 'ώӡʓ',
                                                    },
                                        {
                                                        'key': 'ǯư˧Ǆϓ®ЪĪб',
                                                        'value': 'Еǌԛӭ˧ЌҜεđäƣҕ\xa0ã\u0383ȼəίѤʼZυӻҌϩцˊƷʊǫ',
                                                    },
                                        {
                                                        'key': 'îѳϚɹјÈϚѸɶѧûÇɽ|Ԛ',
                                                        'value': 'ȳtǮșȾ|˖¬їΰѱ\u03a2ʝҶǓϒѫȈѝΩŏʰgώϤѝŏѳHӚ',
                                                    },
                                        {
                                                        'key': 'ɹiӱ\x8cÌΫŃȹϻȜҫƿΉԉЅåÿφ˳Ÿ\x96ѣϼϔŋǾљ\x8fŴӱ',
                                                        'value': 'ҊſƙȳɼůɥëηҝĦXȘƂîɭΥүЅͲʸˊ:ρɞÙ\x8eҨԃρ',
                                                    },
                                    ],
                        },
                    'comment': 'żȴӎӣӈŏªɆƚǄЅӽȧĬϡ\x82Ǩĸȃ3ԏ΅ȍt|ħӐÔ˕ʮ',
                },
                {
                    'keys': [
                            '˃\x7fƶěʙғʱò҄ƆϮӨgIęϨмǻƢ,з',
                            '˞ÈϪɥʽζŔʛҙɐѣӖϹʟ\x96˘ԤѺԘʹȱƿæӥɪǥčӔ',
                            'ҎҽÅ',
                            'ȢųƢϯ\\',
                            'ǐβǃʔ˒ĐŞІǣ÷',
                            'ȚѰѹĜѬǳΝʬԪїű!ρ',
                            'ˬƁҮϻЬńЈЭKҩҥАRǧ÷aɛĳΘӽęAˢȭФʬɬϱ',
                            'ɜЩʄ=%ёВãɠ\x8bҀ`Ɛ[ϫωюŵώƢ',
                            'ɂӒ¨ӝťˁğª',
                            'Ы҉\x7fȻɍªąѼ',
                        ],
                    'event': {
                            'target_id': '0½3ƂǗҮƢĝűʮûвǉʜŢЅѯүȽοΓ|ŃѪ˂ҧ\u0380ФΧϩ',
                            'parameters': [
                                        {
                                                        'key': 'ƅǳΕȞΫǺʋː9ӏԏŕʍӒǝҸ¤˛ˤǯυȉϥтýɫϝƘpҦ',
                                                        'value': 'ŞȳȪ˄ťrϩЎĎӒҴԑӦԠŊĞĄʪÐJȸĦӖʊӻ҆ѻɇðԟ',
                                                    },
                                        {
                                                        'key': 'ӎџǎҜԄŌԚʣ^ǐȧ˟ͻӪКȣӪơюʄćȧҐƁЃӦʛ˲Ăʧ',
                                                        'value': 'úǊƕcэȳЖƊʝ˅ĢØȻˠԣDїȀɁϴƛ˱ЈόřƻЬҴɚå',
                                                    },
                                        {
                                                        'key': 'ɸ±ŏ6*őɨəı\x85ȡKъѠɐ"ˀǌϕmΡǺǙȼĊɗʰʔ\x99Ԋ',
                                                        'value': 'ѽ]ΩɊϖ¶ŷЄWƨɡίāЛƵʹCұѶȷаÿųӢӊƑƚĞѕˏ',
                                                    },
                                        {
                                                        'key': 'ʈȣŠ£ʛΧ½ȂҊu˙ЏEϷƘòά«ӺŹʑӦӦΒĿ!ѕун\u0378',
                                                        'value': '\xa0˭ҫɾŕԗΑMνȗĥ9ͰѦҿЀĊϩɹϋӃЗοūæ@ɑÍԔȾ',
                                                    },
                                        {
                                                        'key': 'ϕęǝɍµϞϏΓjǸǒÏȲɷ\u038bűҭȆƭнēҁ-ɋVȘҸѴ°ť',
                                                        'value': 'řȸТщǘϖԈѺȔɸ7џÎĦӍiӚÿ5Σƍ>Ǽю{˷ǖԑЁĸ',
                                                    },
                                        {
                                                        'key': 'ÅΌȎʕԅǑӺҚҨЦʐ3ɴāϮdѣħƸξĴѹǞaȕɏѨӍŢ\\',
                                                        'value': 'ĽȭʉƍҺ_ԖɣɎиɜɟε\x80Ѕ¥÷ɘӠ|ЏϷǭ]ŗˮŪǹѵǄ',
                                                    },
                                        {
                                                        'key': 'ʵýǡWˌʲĎâʱǆύБʞ˜҉ġҜНȗʄʿ\x8fΧвѢѩ˻Ӂƛƌ',
                                                        'value': '§τJȕKζҬӁԜ¥ЁâȘҖ5ȁɵѥ˟ѾîęŬ\u038dÝ\x81аΚÖӊ',
                                                    },
                                        {
                                                        'key': 'ĩԓМƨϥѦɯńЮϖ\x88˃ԄȖʗͰ]IӡƖȨю',
                                                        'value': '~ҁXҰʱǤȖ˽ҺɍΰǼǴѴĲƯ(ӍėȑӂƵѶέʴɕ7ßț˃',
                                                    },
                                        {
                                                        'key': 'ЈЯƒ$èЈϽ˲ӆʅ\x95å˭}ʲңϽɧΈʝʤ\x84Ƈǥøϵӯѿњ˻',
                                                        'value': 'ӛĤʏԦµʹ6ĉ-ˌǹÑԖō˗Ѽ˭ǺĔɪҕÏɸƖͲАĚӪԠʓ',
                                                    },
                                        {
                                                        'key': 'ӡԜǍkԭƄӱΧšɳˎδˡbȺɽǭɩЂƨƾuǚˍǋɈϴχӲɊ',
                                                        'value': 'ԤɟԊя˩ăϳ£¶óϊĀ\x7fˢ0œ\x98\x90ѸςԍӼ|ǌҿȂШӆǫɃ',
                                                    },
                                    ],
                        },
                    'comment': 'Ć\x8eҲŜ{>ҹʧΧЃͷѨƙͳƲȁъӅЭԦҾӹοђ\x86aÐȞцË',
                },
                {
                    'keys': [
                            'ĹʤëȰӝόˣūӱŪҏǯхǁZϤԨĨқ',
                            'ȫǢ˹ƂɎФřгLПŷŃСʝũЭ`ѾӮ=ˍƙνͻ˄љѿʶ',
                            'ΨϨŀȌƢÂԭĤ¸ǡùԭʐШɚѬӪǍĸӕƲϖӒҵÅȱ³',
                            'uʑΫ',
                            'Ћʍ\u0382ơɯ',
                            'ȇQӟ\x8eǘɏŚÚԪοӕJЌӀˬ',
                            'ѻЬȡώνšąţҊ@DϮΡӗӡ\x8aĳ',
                            'ҎŉѬɏ\u03790',
                            '\x9fѬłŭǻɮDʠѴǲҘǩɔjϽ',
                            'ƕĜќΑԕ˵ԚҷǢǃƑˇ³ӣȗѕМБмӝ%Pə',
                        ],
                    'event': {
                            'target_id': 'ўͱĢџ\x96Өɿ;Ҷӽlõ®ХυЄмŬƸŦΟԗĨÂ|ȏӵGѕɏ',
                            'parameters': [
                                        {
                                                        'key': 'ћȭӂ_ƵԬżgѷʭśĭҔƞȗъʷ;ȰӛɃԛѿ\x9c\x84\x89ƖѴýˬ',
                                                        'value': 'ξɶĪεӕýƻȵӷФ\x80ÐʘƠįўҿϸȴɝқǶʌ\x88ˤ·ԁĚȜƂ',
                                                    },
                                        {
                                                        'key': 'ΘѳÜeϼɮϿӏЛЏʁУOѬeҾҖVϧԖϽń}ԛƶС҅ˮȀÅ',
                                                        'value': 'ȣçэƩŞ[ΖǸʼҜǇΊ˚λЙ¼яӨRɁĞδȀăyϖԘÒĆӓ',
                                                    },
                                        {
                                                        'key': 'ϱɬӇʾŐțӠ\x92ĎòқϖɬưǜɹɦțЁyǖýδbϤǦϹҊϝԓ',
                                                        'value': 'ϪзÛĉĨϴ{ͷ\u0382˹ԟȶшíϬҫϽϯǺΌϧӟΑΝЦɓҹԌѶ!',
                                                    },
                                        {
                                                        'key': 'ԫŧǃҔɑĝЯν˜ԂԙίƥϹʦѩȆʅӂӹ',
                                                        'value': 'ʯ«υӠЭ§ŤԮԢԪԩώӅ7˒˵ϝʪяϋRǟʐˆ˝uϤǣ˨ʍ',
                                                    },
                                        {
                                                        'key': 'ȄōοƋĉͰќȰȁѯ\x86ȚɋÐͿД˟ԐˇÇϫÚB7оćɱÏʾÌ',
                                                        'value': 'ҁӄŤØƤ6ŁѝȏƗԡɕЦ΅єwŮΓɒŴϲТί',
                                                    },
                                        {
                                                        'key': '\x95ԓѕ',
                                                        'value': 'ƯϞhÜ˾ɴӡӂӢΚ˗ԊɘУ%ŚʎҭΆˎiȸɣǖMȢ^ӑ˷ĩ',
                                                    },
                                        {
                                                        'key': 'Ũ!Ȱª|нȸF©˨8ŝ\x91ȉѵſɱЭԁɡѵAԕɔӹө|',
                                                        'value': 'ЦĿʴăѷaЋÉ\u0382ƀǇ\u0382ɱҶÃǬťǫöӰҢáү.\x84ŋОϐ΅Ϝ',
                                                    },
                                        {
                                                        'key': '\x98ӝĠΒ',
                                                        'value': 'ӋȚŖԫĲÃʚ\x80ʠ\x87˅ɓ\u0379ϒãʅӖýʄɐɎϛÄΆΛɛ§ԤϻŃ',
                                                    },
                                        {
                                                        'key': 'ӯ˫vϷѤXƱϹҜ˼Ʃ%ІĒǮŚчʼΩǘЯǁɔȍЃƃЫŃ\x95Ĺ',
                                                        'value': 'ǈΈêӈӘģʉӪȋƧЎɚʯѱ˓ȺʖӲцһѶЊʺũtÌЄAӪî',
                                                    },
                                        {
                                                        'key': 'ŒĲǍFɼɔʳ,',
                                                        'value': 'ˇɺƓ\u0380ƯƙͳϥӎʇѹɌǉƓ½ГӬȬƏėǑΗ¿ɯσБɀŢϖτ',
                                                    },
                                    ],
                        },
                    'comment': 'ÓƹˈǫǾ°ӬƞѾыŊΚіѪ\x85·ȑĿωъˑÍҧʽɞƵР\x8eϠ\x81',
                },
                {
                    'keys': [
                            'ɠʊϼĵ\x98Ƚ\x89ұķЎƵϯнϙǾͳʗѼŶΑϭΝʅ',
                            'ƒϪƎԜĜґʊҌƎƓГΪȩ',
                            'ɷ',
                            'ѮÛѬӣԃƞƯƒeËЁßïсåNǰŗůЩ˩ɋȖǾ',
                            'ƵϭǥәӣʖгȼȢƫŦʲΈюåÚȊґŒҴǡβɗȨǨԅ',
                            'ǵɄÀԦ˕ϙ¸ȵϮʐƜÚGϺɵƸиˏçό˒ɽ',
                            'Ͻˢ˚Ƀ˜',
                            'ƋŖѮӨɬġѡ¿ҩʡɖȟĞʝǁƦэ',
                            'ËČȨϛˑіӵĦԬɤԩԒơηŰİҡ\x84¾ӟʃǛȗx˔Ģ',
                        ],
                    'event': {
                            'target_id': '\u03a2ϠƳӲʯ\x88ѼԓԁҒ˕ӈüѦʿɫ҈\x98ǿO(ĭϕʛ\\ϊɬǐыΘ',
                            'parameters': [
                                        {
                                                        'key': 'ěѶ\x95Ώ\x9dєˌ˒ÕӇ˃˃\x8f\x80}ǃt\xa0ѱҍſLmҦʽ\x7f/ԍв\x95',
                                                        'value': 'ёɦŴŠȓ\x86ȝωȐǫ϶НйȗΒɀЇβʣ*·Ί҅σĻŗʤƽ˵΅',
                                                    },
                                        {
                                                        'key': 'ğǹͲ0йȳ\u038b˶ĈӰЮӺт˂ǩ6ķŁǃѢƍԒǗҲҙhΟÖұȢ',
                                                        'value': 'ɲΫӇэˋϖŒɧĴǳŖъõϔʥχ^ԧʄȍǅӂǡеǡ˧ũŰџƲ',
                                                    },
                                        {
                                                        'key': '5ϖãȂΦЕºHМ!ʩщϼʣǬ˞ǰɀ_ȍǑ˥2˭ԙ˱ɂȓ¬ʠ',
                                                        'value': 'ƍ:6ƜΧ\x8bѕԜŮĈԒmʅɼřʒē˾ǎǦAԦǤӭӦƹɾPԛϙ',
                                                    },
                                        {
                                                        'key': 'ԞѡЖǛқĐωӎĕāНҘľŏώʱƀʑʺǋƴƬϠǬɬ {šѧŰ',
                                                        'value': 'ÌҐÉʩѢȰȣ\x91ʫȟқƕƊΞʣőĵӀƮȿˢƒэʛԏǅˏġԁȱ',
                                                    },
                                        {
                                                        'key': 'Ƹ\x99˴бԃē',
                                                        'value': 'ƽѦѺƾѴψΫǐԔ\u0382эǼӿÂêϲȪʲѨϔҊʿͳϠʪӭüԘҷ\x84',
                                                    },
                                        {
                                                        'key': 'ё²жʄˊΘƳƌŮǤҞǣˏ¯Ɯĸѳ\u0379˴ÃԅòŬłЄΉӏʺYθ',
                                                        'value': 'f«ǸΗ ĄύJɉɵõɵτǠģѓǂȏ\x8dǚҪ5ʌ˽ĥűΗґζ-',
                                                    },
                                        {
                                                        'key': 'øʌ`ŅԡҺӍƧ1Ѽх˂ɎǀįκψϚ·ȂϐϹɅƢ˘МKʜ˼˷',
                                                        'value': 'Ҡό˴г\x85ĳʪïɶԮ ʫrͰӖǺ¡ͿҟĐŬĨ˟ЩơŋѐǓЗҬ',
                                                    },
                                        {
                                                        'key': 'ѯ\x97ĨȱɒЂĜFǖǭŎjғ)Ȟ2ʅҬńiԒɀԗӒϪ˵ȌżԙƖ',
                                                        'value': 'ǽҽ˺ԔĖ\x86һӣɀІ˟ĳӱȋƐțҭΥņɘϐ˥ΑҘȫёź҈ɞǋ',
                                                    },
                                        {
                                                        'key': 'Ǘ΅ƒǂ˼įѻȇʎǛѡˑӀǜǴʭɁ\x96ȡʭѺÎnЫ\x8fÌeѴɟ˘',
                                                        'value': 'ΰʚ˵ªʊşšưʵʝaЅΠÖûЉВƛӜӋÈӔĳ\x84ϿπZҢȯЖ',
                                                    },
                                        {
                                                        'key': 'ԉϩŹÌӓӓɣ[ουɩΠĹҾσБʧˬЉǾтԆȅʩΛҊ_ҽǧς',
                                                        'value': 'Ç\x7fкΪӅѱǧŶ]<ƏǘʉѲɕĴͺђѪʩ϶ơɞȦҊģȟ>nȠ',
                                                    },
                                    ],
                        },
                    'comment': 'ąЧµѬӣӠ\x98ҤʐiǌªͳƓтσѶuЪƦʭĤŠǪȴȹ6ĚҴͶ',
                },
                {
                    'keys': [
                            'Ƀ͵\u03a2ӁƆÕģΉƐԀԔҙķɮБɪ˘ҏωӖŌƬԍǖŘϛѴɡϣ',
                            'иTԂhΏőǎǸė\x88ɪ',
                            '˗ġӊƖŇεϡ',
                            'ԅ҅ɪıĘƿ4ǒшѴ˸ȽǕ˃',
                            'ʉSȉǗɋǡѤҺǧǫ¸ȯȮɎƼäƁr\u0380Ζ',
                            'ƼȝyƕŒšˋ×џơ±Ÿԥ',
                            'чǘЕ¢Ͱț}ȋ',
                            'XSɞΆ˜Ӕ\u0379҉Ɵģ¿ʳȼəØϙÏ\u0382JeŤӇǧȆĚȒ',
                            'ǉ¡ĮӢØ^ӜȉЭĢÔҩȱȭ˹\u0378',
                            'ȇЍЈ',
                        ],
                    'event': {
                            'target_id': 'ѝŞφƆǳ9ΰxҗǒȽ҂řžȬǕЮп\u0382ґϔ˥ȻȅѮåŋģͿċ',
                            'parameters': [
                                        {
                                                        'key': "ЅȠɃӹšс'Ҟ¡җiщŨϪӕЬæŸCõǍĿİ«ΑӥºΎόƆ",
                                                        'value': 'ǹɞȹƨ˲ŢƜФԑĨʧљKƹÒȥλƕ\x88Ѷˀʹu#ĭѥ\x9bɰ҉Ж',
                                                    },
                                        {
                                                        'key': '\u0378ÇԀΘǭðʟBŠ˸Hԇ\x81ȴ\u038bʛēȾԖЛɚĲɶ',
                                                        'value': 'Íʟҳťŉ/ҮҵïϗìǸ[ĽИҐv={ĬˡЍҸëЗφʏæIΞ',
                                                    },
                                        {
                                                        'key': 'ϐƏ ϬʺҾęɴЬȠѠŜѺɺɋǾDiěϊ]Ė\u0383pP˞ϚѬvʲ',
                                                        'value': 'ȕүϸɘ˘ҧͶӪƍɕəŠϑғЧŵа\x8c+ƓϽ\u0383ŢƭĜ\x8bҽ\x8fʷF',
                                                    },
                                        {
                                                        'key': 'ϩҔ˕ҕȦͱʓѯϝÄsқ\u0381ǯѿͰ"ƒћхǟԏƶʂɬpӴʭȯÅ',
                                                        'value': 'ӌҡƈǾżϖɂʷϼǋԂˆԤΙƹԝ\xa0ФͰЀύѦƦƤԅЁԓņ\xadξ',
                                                    },
                                        {
                                                        'key': 'ʍȗǎԁʘӈ˔ȐȮϴźμpºΚɜ˙Ϣ»ʄȾҵɭ',
                                                        'value': 'ÑŀΌĿЅ˯ʊ+ƏΙjɬȸгØʩЪÈñ˗ϼԌːҕƕ"ɺťǑʠ',
                                                    },
                                        {
                                                        'key': 'ʳԍŦϑũɉ\x83ΧОϠӴϘѡԥԜҴȃє"Ԁʋ¡ÈЂέʸўŔ',
                                                        'value': 'ѽţü҈υƶț˯üҧʬǱјćȉɯГΛҚџӏϞϦӨ\x850ԡέȇʎ',
                                                    },
                                        {
                                                        'key': 'ħѲ˰ɛΒƫхʥťɜȑ3ʝϵǊʲХª¹ԦϑĂǄƞjϚkʯǬĆ',
                                                        'value': '(Ŗˑ\\ɣϋɏχïˠ\x80Pħɵ˅˨ǇҌ˘κѫƵ\x8dĆǙȑeWӒÕ',
                                                    },
                                        {
                                                        'key': 'ǠɱǨɊȒĕ)ŴέŐɵәɣ+Qѻ#ŧӼiƮ`ȤŐ=â~ķΔʠ',
                                                        'value': 'ȱΊ\x92ϥĝ˄ɽɰҞZȤ\x88ɜǠĢȐ!ǉҪˇɛӠӸЅɈҏԉSÎä',
                                                    },
                                        {
                                                        'key': 'Ӝћɺʿ8nŇĖŴɏǤҍƩȜƫѨҕ˸ʅƿƫǫÐʀě˄дϸŖО',
                                                        'value': 'ӽÀ%˸;ӵʅčϦÕϙǭӸӱ^ĳȋNӻʗǨѢɀѥϰӤȜ¦ҨѦ',
                                                    },
                                        {
                                                        'key': 'ςьӵØͻѠɓȺ˓Ү;ːŘ҅ξҀЗȰ,ȵʣþ¨эԃ\x91zFςɛ',
                                                        'value': 'ӕБѰ*ǈ\x9c˦ΖϼӎɊȄåԪÅÙ\u0383ɴȚӤ\x8aӝŶԬĊȷԂҿʝɗ',
                                                    },
                                    ],
                        },
                    'comment': '҄ѱê#ŮzɣΏ;ăҖJӁљҖõǛ¶˖œʹӬ˭¸ҶɆȆąϨө',
                },
                {
                    'keys': [
                            'łӟǘӥ҃QϸËáѤϠ"ÛҒ8ϖʥʢ',
                            '¦νšʺҧ˭ʩ',
                            'ÓɄбþÅ',
                            'Gû ϣүϟ¬ҏŉʈËУŊíȅѓ¥ȠţȳĭÞ@Ԉ',
                            'ΦʛɶΰԊŲЊϲĦǎѼƗΤ¬ˮϫșĶmʟŸć˭҇ȡɛμʾ',
                        ],
                    'event': {
                            'target_id': 'ҲƶȣҬ\x87ïŁ\x91ЩсПӝQɝρҌƧł!ҫϥҒҪƏįѩȸf7·',
                            'parameters': [
                                        {
                                                        'key': 'ģĎƸĤԞԄȠʷˇ½ΈĴњяѷőΌɴŌӲƽ~=fÁзJȰˇˇ',
                                                        'value': 'ð\x91ʭ÷ȹҎўNÒ¤Gҙ˵ǅŒқɤĸйƹ\u038bʳѾϽƴƔԖ˨ĘŚ',
                                                    },
                                        {
                                                        'key': 'ʃȘɮʺŚäʃǣ˔:Ćҹȃҥvɸƞ͵дȧŬԙ\x984˪Ǔġѹ3Ě',
                                                        'value': 'мƥrÍŐιǝԡƳÁԀғϵӑϙӖʺʮΦťͺѐʐ³ÂΛ;шÝћ',
                                                    },
                                        {
                                                        'key': 'Щnƞ\x9a˪ЛəǑʛԂϼʃ|Ǽɡşʉɑ0\x86ͼʽ҂@Ѳω˴ϛʎÉ',
                                                        'value': 'ʼХΘſϿǈ\x80Ǥíűϼɛ˺ȵɭqŻѝòȊÑԎӨҿʺYΠɉԔǉ',
                                                    },
                                        {
                                                        'key': 'БžĨƊɡF®ϦɤmÚӽћĻяŲƚҫѠԜ{g\u0378ĚǄΪýĝԞɿ',
                                                        'value': 'ј}ϋʑӐÂʌʘ˱яˑȤ\x92ɬğǢιQԮһ\x85ǑǳӐˠ\\ǔēίŔ',
                                                    },
                                        {
                                                        'key': '\x8cƬɩƚGӠсѩŃɉԬưԏƹԆȐĒΘtμ5ҍЕԍ\x88ʔΫ\x8a\u0382đ',
                                                        'value': 'ӜǗ½ǳ=χēƃϿȋͱț˜ѺšŋǙâΘϓŅǎНȲ˝˻ʅǟĪɪ',
                                                    },
                                        {
                                                        'key': 'ŹԟҧƙζŨɭЭ}îĲʺȷʽ\x9aÏ˚ʍθţГtvűȚÃĻdΦȄ',
                                                        'value': '2ơӷ9Ӓ0*ȿȮǯ½©ßΧĘ)Ҏ\x8aОǵÿȐѦłȧԃҞʈǾ^',
                                                    },
                                        {
                                                        'key': 'ԫͷƕҸѯѥԋӅӾ\x9e¾0ȻɠƃȲ҂ŃʖŨǧ|Əãͱоӽztϑ',
                                                        'value': 'Ӷʬ˹ЧʅωϮQΙӬŌ\\ѽɉ¤ĬǱ£АϨђmÙȦ·˂Ƴɧïʜ',
                                                    },
                                        {
                                                        'key': '1Ļƿd´ζsèϝҗ\u038b8ȫėėɭȱИӋJɐѪԌӥѫИŶͼ)Ą',
                                                        'value': 'ȉĪʡ\x9dΗźÍ\x9aƴɷŦЍɧŅɂэʪЅв·ȼʮүѽƇ˞ƜӫӅқ',
                                                    },
                                        {
                                                        'key': 'ҪţϨзϾOƤɾȭѩƁȖʟkʭŧӒͲȠ¬wӂӋcˣʄԕƪĔ;',
                                                        'value': 'σÚ7ԡą¬Ҕυʀѷ·ȭжϝțӫӅЩǮƴ±ӹǐ58βɍәЫћ',
                                                    },
                                        {
                                                        'key': 'ђòɖЍϽʲϽжÀЂ˨ʡϪŨψ\x96ȎˋǪźɊΟRοM~þȽӷƦ',
                                                        'value': 'ȽԟφɚӦζʤɡϟƺPǜы>ɾ\x9bψ\u0380ƀѣŸ·ђ҈ďªҿm%˹',
                                                    },
                                    ],
                        },
                    'comment': 'ʵӗ҃ȖVϲȻԊȇɚӘҚϬ˂ȷК^˶gʛDϓЃǈеǁ\x96ǼǝƉ',
                },
                {
                    'keys': [
                            'ӗǁŊϮ´ƻѷΜĦ\x82Ч\xadƬˣεҭР˭\x85Ơ',
                            'ɚ"ÖòƞǍѰҩӷӹĘΉŋƟ',
                            'ċ\u0378Đ',
                            '˖ĪÂћʐтǃĨԗӟ\x88',
                            'ѕɓҾһɴʟǍȐdΡƑτίϵǅ',
                            'ƛǽɊӘlƀԜ˄\u03a2ēϮ_ҠS',
                            'ϥiԇ¼uЋҴӫ}Ɗñͱ$',
                            'Пϯ',
                            'ԃǺԦӣǍ',
                            'С\u0378ЈΕɌӍҢѲΉŬ±Ρ\x98ƙȐƆ',
                        ],
                    'event': {
                            'target_id': '@ʑύ\x82ă\u0381Ζр˵Τ¿ͶˬȼԛѧӁĺϛύƱҿʤӰȽЭǲҚ¿Ѵ',
                            'parameters': [
                                        {
                                                        'key': 'ӞÆš˥ͻıҊŮЙψƂЀӭЯ',
                                                        'value': 'ԝɛõɥϥʽсǚůʰԤgɤ=ˀĜϓӶɔԊ˙łĂѝѪʤӈξɫԊ',
                                                    },
                                        {
                                                        'key': 'Ʌҥβ>рүĊɁѡȁȠӊǃτϷщ%ϒ˓\x87ШξʍƎȥҍ;ąϾǄ',
                                                        'value': 'КъƀȟŤſҸBeʏȷѷΐʙʁɟʿßӮΏČХÊ\x8eщЎңʄΩˮ',
                                                    },
                                        {
                                                        'key': 'ʷ.îʇƒҶ\x86Ğ«ĨўȠǮѫӬ÷ӉŸҗӋŚϢȭPŒvūΐĸԎ',
                                                        'value': 'ϞʭʗɬĽԧǇĤӓ¸ŦѱßǊɝþʀсʄҕĚ÷Íѭœп\x90τǝӋ',
                                                    },
                                        {
                                                        'key': 'ŷѷȖϩçÂα\u0380ѹвʽϸŖ®cϐʲƫϑɅĜӸΏģ¬ɨθż.Ԣ',
                                                        'value': 'ӳƄƮҬǋº҉ǲӴɡÞĿ\u038dԞ˩ƖșĶ˺шϡQӉ/ѦȲƦͶͼʐ',
                                                    },
                                        {
                                                        'key': 'í˞ǋįЛΥѠгѩͲ0иɔҝéΕʾǽщĩ¯θűwЗԨļљғɯ',
                                                        'value': 'ƆӎɋĖV˩ƿ҃ϸȧдьǶңŜÊŃ$Śʵ˹˖ƏŎơԅµɗžǭ',
                                                    },
                                        {
                                                        'key': 'ɅԡƎʺʩ',
                                                        'value': 'ŞοόʅϒѳñɤŬʙ¦ϣО@ѽƏ\u0378ѩϵǙ҃ǭȒ,Пӣ\xadпΊс',
                                                    },
                                        {
                                                        'key': '\x84Ƒ˫ѱʸӰȏĸЌɾL˖ÊԅӫŰ°ӏɎǿÙŵӥǳϯǯƵ$˾Ƀ',
                                                        'value': 'мɥ·ӉŲȰǺĐǁưƇƹӞwˍЯԔϩҏӍNѨɟȸƭνԢʫŉϮ',
                                                    },
                                        {
                                                        'key': 'vwϓҹԟԠ\x86ňΑ{ȶЋˆʑϙÂѺӴǥ\u0379ĐȯȖɥɤˤΎϬϓ\x93',
                                                        'value': 'HӞȁӿɽËǪӁˏͼȻŮɬҼƉ\x97ԕɩĥћʭEYԭȱѺˮɌ(ԋ',
                                                    },
                                        {
                                                        'key': 'ŧňe(йԀљҠ',
                                                        'value': '˓ȟ\xadӥΏʋМ¼ʔRnϩnʡϥōДяŒбɛƷŋϤʣ˹Ѫύkѕ',
                                                    },
                                        {
                                                        'key': '.Ғ:ŦӻѓvηėɧяŭίыĔԞͶϼюǺ˧Ȏɘс.wˉʀǴ\x99',
                                                        'value': '˺Ǒˋ\x88іϓ¤ԆɏɪKǰҦʓüɜƨμÄǽȒȩƹ\x8bЋýєҲǚǬ',
                                                    },
                                    ],
                        },
                    'comment': 'ʶЙ\x83ƊԨéʄϦʖ+fąʷͰâƯ҈ԅӣȉʀWZ©Ψʹwīi\x80',
                },
                {
                    'keys': [
                            'ƦŮĞ˴ȅ³ҖJΈϒǨϕľѸԟƇőǕɚɪyƀǑş',
                            'зļ˖ȕ\x95ԭҊ5ɐҸØʥǃƨГоЮѽ',
                            'иЉέDͺЃ¦ïӼ',
                            "¢Т\\\x8b½ȤσΑ˔Ͳ\\'ɂ\u0383˔əʢɒƅԪÈȋʆѠ",
                            'Àg¶čŕƋҫŹÃκѷ˺ӖŇ\x97áóRĝөςȧ\u0379´ίΒƤӅ8û',
                            '˚ȯȗΞϼϱŴ˭϶ÛƅɲSÝ\x9fÒ:ɫͱΓҧќƓȅǋӛ¶ǃҮ',
                            'Ɍ',
                            'МζȍǼʺӍɞɗ@ъЉÉĝ¥µĘϰʴbΗĹ',
                            "Ƹķ¡~ĄƧȻ'ȖɗЏҭαіϘ˜",
                            'ŰƦȢМǶԞN˳срƛŬԋĤþƻšӭ¿iΧ',
                        ],
                    'event': {
                            'target_id': 'ӁɞǇʎ\x91ӥϮҋīԙȢȪưΣʩΰUďʾºӍʨȄá˭ԉÓ˚ӊǂ',
                            'parameters': [
                                        {
                                                        'key': 'ʱΟʽĐ\x9eЛԙ˯Ɔİêαø˚è˴юźűɑюϐԚ1тҝŦvΩ˒',
                                                        'value': 'ѱhÎǇΛÜȬԞĬ˟˜',
                                                    },
                                        {
                                                        'key': 'ŽǑП@Zǳұ/ú\x9a¯ЃдƘȦ˗Ďϊŀ\x81ƜТѶӐҴkʣұЧɳ',
                                                        'value': "1ҦŋnϤҤĐɧҠÃʏʲ¦ɯ¶ŮџÕǍʐõ҅ɱŋȤΥc'҃\x82",
                                                    },
                                        {
                                                        'key': 'Ɲц',
                                                        'value': 'ʘϲЩѷ҉ȤœʁƲ\x99ЯǚԈȸ(\x9fΓʦӡԏԎӅυď¥äĢҜҠÂ',
                                                    },
                                        {
                                                        'key': 'ҞƊдě·ϔӈßř¼ԍ\x97УǰɓʤˑϭĴìĩώ˫áǇ\x90¸ҮʫȢ',
                                                        'value': 'CмŊʍιфüҢɶŁʙԦƏĴƒǔƵÔЙƎåɑӝ҆Ϟ7ØΖúˊ',
                                                    },
                                        {
                                                        'key': 'ɪΨ\x9e[Әї˦ΏУȪ',
                                                        'value': 'ʕɿRɾϵԀǫǇϞÔȠɣƣʹѐʛ˦ÂҞ˖ѵËȚȨȨЬΦӡĄǗ',
                                                    },
                                        {
                                                        'key': 'ƫȤΈɧɒĕ˽ѦҪɬӞͽǂӏӟȽɶīϻЮϕ¨ɏƊ/ѷǍŹȧ³',
                                                        'value': 'CѰ)κɑȷǫȍľºȇÉ¼ѝÏˣйĒɁӻ˱ԌǰԔԙӬɖԦ.ű',
                                                    },
                                        {
                                                        'key': 'ΙȦǱ\x9fǣʀƝ˪ϿΈĊЋ4ȤıŦƑ',
                                                        'value': 'Ǘɼԍɫɒǡ2Ɇ\x8bçǮêԆϊӾċҍÒěЏцŦ\x98\u0378ɂƨƓɗԔȥ',
                                                    },
                                        {
                                                        'key': 'ЍŅɐΏŠʠΏЎɮɘѩΛ˼ԏԋϖŷǵ-џ\x82',
                                                        'value': 'ѱĝó˚ѻȝҏ}|ȷϨӨêɻӻѝƉēϦ\x8eԇʱΊĸʻ\xad˥˩Ȧό',
                                                    },
                                        {
                                                        'key': 'Ë˜ɗǷʓŁņ²ȊǂѐʚгWάѣφÃԗйƝ1τӪŰˏɒҬąԕ',
                                                        'value': 'ÜçƇɽŵƩԂӼЫΣҙįs\x9bΰɕθûǸ$ͶҮјӳÍǺ\x8cǯєԠ',
                                                    },
                                        {
                                                        'key': 'εŜѬǬѮÒȦʦÄ',
                                                        'value': 'ю˳©΅γ\x8bŽԬΡ¬ʓɪ҃T˥ȃǯƁʪѹЬ\u0383mĲɏП!kQŃ',
                                                    },
                                    ],
                        },
                    'comment': '˺ǱòΡˮ˧҃ȴǓШǿĴįˏǦĭϚҾˊѝʲɤҟӿơɏƈЏɃʜ',
                },
                {
                    'keys': [
                            'bʠϪǖLѬɧ¨Ԫϔʑ5ԀшŴԆȺ\u0379ιíȠ\x8cɷĎȌʾɜ"',
                        ],
                    'event': {
                            'target_id': 'pόǘʊǦĮƏϣĢʙДԖªшÊϖ˒ƈȺÒμȾȽĆɈǟŞB:Ӿ',
                            'parameters': [
                                        {
                                                        'key': 'Ѡя',
                                                        'value': 'üΗɭ7:T^ĕaɮԬǨʲν Ɉőϩ\x80ѝĒǦʜʕхǨÜΒНӫ',
                                                    },
                                        {
                                                        'key': 'ΫƑ ɷϖĲʮ˾ƛӧэӱ5Ȋ´ǝȯʔl',
                                                        'value': 'Eà˝ĘјԕȳƉɥӲ˽GƸɸҁӆ˜§ԍĐͱʬɛßӷǧѵˉͷ3',
                                                    },
                                        {
                                                        'key': 'Ǚ˧хĿК¢ŠǃC.ӼēѸȢϼѭʊ˧Ԏ9΄СːήӓÛѪnʨƋ',
                                                        'value': 'ҾМӦƚмÂʚԧщĺзǸϭŁľĖԉӱʎ\x99ΒΖ˥Bźȥȏӎzě',
                                                    },
                                        {
                                                        'key': ':ͽӕȘ¥ź2EϷ˽±ɛĞӓɽȱˮũџЛūǅƏʅǫΨ!Ӑkр',
                                                        'value': 'ϠǦӅŗԔ\x9erϣшжǿĕǡˀðȫҪʞӚҵҤϒфңɍǬŢЍȿǺ',
                                                    },
                                        {
                                                        'key': '΅ӟΏZy˥҂ɏ\x7fˠŤЊИŌϑƓ.\x8cËãЗˍѭȧŷюѭƙƋӒ',
                                                        'value': 'ʆўçEΐѳӱ\x89ћz*БơˠńԢĊѶɄıԓԌ\u03a2ȦӲˉƅԣ2)',
                                                    },
                                        {
                                                        'key': 'ѵ\x89Ӻϲɋ˴±ϗ\x9aаƾŇŻΖǂӘλƸҪƱфςм\x99˹ŭʪҹ?Ƹ',
                                                        'value': 'ȓʴ˧Ԯĕ¾ǢǿȰɑϮ¨ýŤƂ¡тÿZňÓ+Ůł[ΕĦʽŸӆ',
                                                    },
                                        {
                                                        'key': 'eĊҶԔбќѷӃϲθ\u0378ÉҋԢʘȮ҅ʸϤťɫǤĆ\x97ίƋοȬ\x8eŵ',
                                                        'value': 'ʚȘ\x80Ǆӵ.ʛUcßŔԏQÒɡê1ǙȔч5ɀкțêąfǝҗŐ',
                                                    },
                                        {
                                                        'key': 'ʳŒțɴưĲ\x87wɛƎȎʝǀŚƴ»ϥˏβɵьϜЍėĂŘ#ѾΟˇ',
                                                        'value': 'ƧīǯӳȭĄҽ3Ĭ*>ȊǣаɀƖ@ßïɍӏ˷ԆϫǰʍƦϰѻɧ',
                                                    },
                                        {
                                                        'key': 'ԆĂǱđGǾϫƥ\u0381ȕҮȖƆŞʶƇĳƗѵқɅ˄Џ˦џ˻ǒҔʦȭ',
                                                        'value': 'ӽ8ӑԉƸӚǼ\x8dUȀ˜ԊƓӋCǿǦϓŇpқΘˈ\x9bĨӨʙƍΓȎ',
                                                    },
                                        {
                                                        'key': 'ǋΆˣůЗέǻŉɚԪӨĆ˥ΙǯȠſÀŸќӜǠЃ³ЄѯǯˤрȮ',
                                                        'value': 'ɛuɡҡ;&;ҐӈӐÍʪʅԭӵͱȝќԗʫɌŖƍɹ¿˾ΟǕŔʗ',
                                                    },
                                    ],
                        },
                    'comment': 'ÝҶσԆҌƠɚΏƯΘϥĐμғǯӬÎ\xa0πӓˮЊ.ΘЇӌʮӺҎȕ',
                },
                {
                    'keys': [
                            'ˌ^ΦȖԃԎɸ',
                            'Ǩªɪœ¼Pů',
                            'ҭȍŲʙ\x92İ',
                            'êĂʓ°ΧϹ\xa0ɲϻ˨ҥĩ',
                            '\u0378ʗӝχǝÀ\x95Ϧ',
                            'ʊÙªɳ^¶ÇǹɏǪǟПɔ',
                            'ȕ϶ƺӲӁԭҀ\x87ąɴҷPϛ7ŧİ˱ƊˋϬɵГŎЋҍ҇тŨɈ.',
                            'ΏȦϳ\u03a2ȦĸϿӳхӻ',
                            'ƃȓД\x8dϏҩȱԄɬӿÃәѳόӟ÷ˣԁŷ¢ȟ˸Ϙ',
                            'ИԊϪ҆`é¯ßkӠɐԌӏµĝbΣΌŘ˟ǎȚÌÇҊ',
                        ],
                    'event': {
                            'target_id': 'ԁȈ×ǚžʪȻȠѠTɱͺҧӄ«ÑǳÔİǫıÈҠĮȩ',
                            'parameters': [
                                        {
                                                        'key': 'ӔǚüĚԉҁΈ5ԈΰЈ\u0381',
                                                        'value': 'фѬѿ˔ʉς1\x83ϵԖǚ˶áͼƻCjʌÍƊ\x93ķ&ӽs]ʬ\u0378Ҍɘ',
                                                    },
                                        {
                                                        'key': 'ɑǜȐŧϕǃʰϤɘΙ8ƭŌΊÀ;¬ŅѼɖӂʬжοВĮĈѲ˒Ӄ',
                                                        'value': '*ȵǱğɃʨǈǦVƺʈȏɯȜɦńȎϔńƶʬİѲӺάѢĵŽɯə',
                                                    },
                                        {
                                                        'key': 'ͺҺ%ɶϝɹʜ\u0381ҶɧΚрϮӍΐӬʴϗzҊϚˍ?ǒΠÀ˸ʀȟю',
                                                        'value': 'εҘĬҙďГǽГȯΆӳÐñ1șőҲ¥ҦǄԍǵŲƪƁ(σ˷Ѡ˺',
                                                    },
                                        {
                                                        'key': 'ɹȷҪŵǶǖҌŤȢ',
                                                        'value': 'βυѿǷȎдћтΣӀwЧofƧДɺĨЯHRϪмÜóƻ\u0378Ӡάʠ',
                                                    },
                                        {
                                                        'key': 'Jíȅȴ\x80ƿsȴƮӔр\xadεʲԎÌдǔΕĂǈӼǮ\x88ʌʪљ\x80Pԕ',
                                                        'value': 'ϸǚ©ͻӪЃЭСϱǨӷʮ\x8fÍ\xadʜʸ"ȑɼŜӛ˨Ȍǧһ\x97ӰgŲ',
                                                    },
                                        {
                                                        'key': 'ĒБȡӜФ˔ÜЫʬ¦ћÜǪЛџȓİEņķԐkӭɐȉ˶Ӯ*ŠŶ',
                                                        'value': 'ӵʞŦƅӨΰѦˢљΏӴŦǷϑɱѹы=ы\u0382Ğƕɠĸԕј˗ҏσę',
                                                    },
                                        {
                                                        'key': 'Ơ¯ǠΆi×ȶн\x81_ηǬʔɊ#ʜʑʶɍƞǷүȢ˖ɿѥƩԡȓ˯',
                                                        'value': 'ӈЌȿʉ\x86БθҭEϳқ˞ȣʵӉлɄΫҢбÃŨ)ʞ\u0379ЩȵҥԟȲ',
                                                    },
                                        {
                                                        'key': 'Ǖ0Ҙˁʸ;ҏкɳǽМɃůѽҌ҈Ȳ«\x84кɬ\x80ӽ˶ъьyӒŢМ',
                                                        'value': 'ŷŊƘşłΖ;\x9dƊB>ԋѓȩϜǁΦΆĂӇʿĀʞԈ´¸\x98ʀȔŚ',
                                                    },
                                        {
                                                        'key': '©ŴDϺǣģì!ʬơdΣʢʙoҚ˸@ʳŝʻƷ°=ОʹкǓʂѤ',
                                                        'value': '0ƞɟȖ,ƘɐԎÌXKʟažԄэѢћfϏ\u0380ϩłˮԤǓƙςϦō',
                                                    },
                                        {
                                                        'key': 'ѨeӋñСșΤåȵΩƨþϴġʳɏΟťϻʿƞӃȞʠǇ҉ĉȬĹӜ',
                                                        'value': 'ʣɶʋ&ʟЬ˨0ƅʸ\x8a~Ȁƹ\x8aƼӥƵʾɚ,Ɉǫ~Ŝ˩ȷϋȓ\x8c',
                                                    },
                                    ],
                        },
                    'comment': 'ъ|ǬøұƠϼĆùҿәҬǘđ+fΡ§ӆƃĺŨҧͱ§%ϵȶȜΌ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                ']',
            ],

            'bindings': [
            ],

        },
    ),
]


class ConfigurationStateTest(unittest.TestCase):
    """
    Tests for ConfigurationState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ConfigurationState.parse_data(test_data)
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
        for test_name, test_data in CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ConfigurationState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='bindings', name='ConfigurationState'),
            ),

        ),
    ),

]


CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'bindings': {
                'sequence_type': 'meta',
                'master_sequence': [
                    'ĖÕϴѸҁƁ·ɧůǢÇˏɒƏ˼ͽǴQʮΝȚʉ',
                    'ǺοѪ)Ⱦ',
                ],
                'bindings': [
                    {
                            'keys': [
                                        'ß\x8fҽˋ\x8cѯȑЖɰʬ',
                                        'ΐԚǦџΟʁǦƞӍ\x99ԟžĦ˹Vċӫљ;ÄѴӽĘŧɸ',
                                        'șϗ',
                                        'ƖĦљXɐȋʶ\x96˳ƧΏŪΒϩɥɲ϶',
                                        '©',
                                        'КДʜıíRı',
                                        'nɛƛˢҶр¥Ä',
                                        'өʯƞȋ˒ķʚ˜ҪРδ˘¶ѭɗȢÛȊΡѻtЫɾ',
                                        'ȟ=\u038bíê˷ȏТˍ\x89ɟтτ\x8e\x85}Ö&\u0378ǼфǺĈ',
                                        'ˀĈҚԔ˦ӍӷqƕӲӛķĹøĤуσÔ½ɉԚˈÃ΄ӉǸĚ',
                                    ],
                            'event': {
                                        'target_id': '˗Əϕ\x8cҪǢÑϳĸС8ƲZʷȉʘРԜџωЫǫJʍÐńĳÜʱҜ',
                                        'parameters': [
                                                        {
                                                                            'key': '$ʾʁĨHĞϨɷΪľ:ƎĆđʜ\x8eĀŘԇҧãκΤγӤéģȚǍ\\',
                                                                            'value': 'ґˮѥɂƅ˲;ȯɤҧŅӊƿǹ:×Ƨ\u0383ѹõѦӛʌΗҞȡŵӰƻЉ',
                                                                        },
                                                        {
                                                                            'key': 'ŠũșÚʳvŉά\x80ѤͽӥЭŷɔϴˠǱɵʨώԮѻuȐʪʀ5K1',
                                                                            'value': 'þҎȤĳėÑÚУ\x8d{ΧØ˙ȫҸ˻ǤɉW¢ƕӳɻΚ¡ǔӷψЀq',
                                                                        },
                                                        {
                                                                            'key': 'ØњƊјÈBɩƑýǌʂđϾqŬԣԌӪ',
                                                                            'value': 'ʎӞʥȞþʻɴǛɞҺϥϢľӗχcˆƥ˂ʱ˘Ǜɛʡ\u0381ǾʕĩЏɐ',
                                                                        },
                                                        {
                                                                            'key': 'Èӡˉêͻѹʠ˦ˣӱϢǙɝġϾӚѻϱΏơèřœɧɶʊҖ',
                                                                            'value': 'Ŀϖϣȩ˕yʖPˈȿǪǱаǟϖмʿҚԪŸƬǕ¿þēӄӽϭňͺ',
                                                                        },
                                                        {
                                                                            'key': '´Ȁĝ',
                                                                            'value': 'ɣ˯ǞЄʊņʨʈΆďDǇЎɘҥǇԐ˸ˢϽ¶ȭĺ˘ϳɪƊυČɩ',
                                                                        },
                                                        {
                                                                            'key': 'ěɓӎȍϧƩ\x8b·ΑџѭϽūØЀйɘŨƉ{ļˍЋɒɊϔdʘӭo',
                                                                            'value': 'ҲӒҳǳŐ˲ŵŀʀԡəɥϪk҃ŻѡάόпXϾpх\x8dӓɪƖҠƆ',
                                                                        },
                                                        {
                                                                            'key': 'ȚсϊЉD\u038bѶт\x95ΩɳŰΗƽƴәϵ\x82˓ϸğɅĊ\x90ѪĻΐѡƢƻ',
                                                                            'value': 'űƁƉǾ,ȏ\\\x93ΞłґȼķͲԇăʇƃβуҎ˃Ä˗ȥЃəƨѡt',
                                                                        },
                                                        {
                                                                            'key': 'ǕӉïŶȖСŶ',
                                                                            'value': 'ҟ˖ŋФлΐδVѦƀDɟ©РҐǽЩɓ˓ȟдǭЀŨǞĜðWªң',
                                                                        },
                                                        {
                                                                            'key': '§ŦЉŁίňϳȈȄϵ\x84ϞΡ®ɬˌpɘҦӟ\x9fϸ΅ĭӂǡЖƅӭ\x91',
                                                                            'value': 'ɷсDƴȵ:ЕǝϤ/ũ˕Ư\x89ȴПhE+ĝώ˵ԇĞЛȸáόŹ˹',
                                                                        },
                                                        {
                                                                            'key': 'ƻɝ%пҟӡéɤĻÚ.hƠǁΪԊwΌȷĜÃīȑŦŜÇӊϯÊń',
                                                                            'value': 'ҘȲԪβБňŒȡӠŐɎʁΚλĊ-»şƲśƧrϡԃǐ%΅ѳŬ\x7f',
                                                                        },
                                                    ],
                                    },
                            'comment': '΄¢ԦΐÛwϢƳTѰɼɧ\x94ɎZƽ˷ļƱɶÀ˪ѦǃƪpìūѐȢ',
                        },
                    {
                            'keys': [
                                        '\x8cʨœ',
                                        'ƂXϩ',
                                        'ʇΘũԞǸ\x91',
                                        'ȕϦɹєӖԉ~Ś§ӇƢҘǰɮʩЋԠӎԨȟϵϷΓĚТǁģ',
                                        'ΥǟdɲԍÀEǥԗӱƲεɃʶˡҴӁƀȑ',
                                        'ɁȘʬАЋõŏɑ·ǡжЊ6Ʈ',
                                        'ǈҟƈԁϬΆԀ"қі˅',
                                        'ÉØ`ƢöǑ5тЎĥĬ\\ͰҠə[иǃȐzѕѱȇƑӸŚʶ',
                                        'ЎϡЌoƯȷƢʻΨň¥Ǚ˻ԄɝˉҞ÷ǖЦ',
                                        'ńɅҩčWȦԢ',
                                    ],
                            'event': {
                                        'target_id': 'ɜѷӲϕVǐʐΓԂȋϘſԞѲɢZ҆ѬӐđϖâ«ёȼ+\x84Nvų',
                                        'parameters': [
                                                        {
                                                                            'key': 'ƾƜ\u0382ϊԣZĔҋˈπRȇЕīГÏлȨͿŒɻ;ƞ˅ɫΟŨҍɗˠ',
                                                                            'value': 'ā˸ȾЇȎʳţ@ŘҶƛΤɺ\u0379ɹŷǆƁǽκќĔ\x8cӸǯԨŴ˫ΊҎ',
                                                                        },
                                                        {
                                                                            'key': 'дӗ+Ɵ˦Ə҄ˍ',
                                                                            'value': 'џɶМǺĶ(θËšλˏƒӫͳˏΞÃÔʒªɗēǑӁћҾώωǿц',
                                                                        },
                                                        {
                                                                            'key': 'ЪΓřѽ҈ȶ\x8fϥǏɥɼy\u0378АðdӗсȸεǙϹѪԤªЛѽɤɟȿ',
                                                                            'value': 'Ԛˊ;\x89Φ\x93ԗ˶ҠRуƈǛˬҦȼпÀ˰҅ɨӵǪϪҒĤɌ)ŨŪ',
                                                                        },
                                                        {
                                                                            'key': 'Ѭй¬ŵέΡ¹ҖÕż˗P\x94ƩɑIϔʔοʇ\x8ckӱȭφœϼɣȋ{',
                                                                            'value': '»ҭΖ\x80Ȑ҅ΞϘńƤŧ҅ʱgǙΆɥҫ˥ӫǑΟĴȝʏČӈͺǙ;',
                                                                        },
                                                        {
                                                                            'key': 'ιӼйԟӒʗӡ\x87ҞιɓǣǬRʲЋϷϗȑǕӨˆƓʳбҹǌǸƔŮ',
                                                                            'value': 'Ч[ȹҢԧɈӲȬǘϘƔ΄ҼΩȰɴʺѷȌԪǖґЯϚԫԟԀɧʬW',
                                                                        },
                                                        {
                                                                            'key': '\u0380ʨǑÌiόӔ\x88',
                                                                            'value': 'ǍїƞξˮŤԀȽ\x95ϗϐÕ8όɕĮȚӞȔB·ҞѻƿőʜȢĎˎҩ',
                                                                        },
                                                        {
                                                                            'key': 'ԥҾˀQyӈθ\x98ČҪРЋјɻÂϺέр5ѥΌɲӌÊʴΨѵŔĥ',
                                                                            'value': 'ϪΆԪŲ\xadЎɁ?ȀҥʮʔұԧαĊŧϜӰıԣѼńɦƶСņǔƭʚ',
                                                                        },
                                                        {
                                                                            'key': 'pцΰҨƗ˧ɛϠƒūɡνʹɡЕǕɭћƞӅ϶ԜσЇγɷȥʹԪ',
                                                                            'value': '¦ˑȂǷɔ˲\x94˭ǩбƸвʞÄƁ˱ΈѻϒLƯͶƌKԉсͰѵźˋ',
                                                                        },
                                                        {
                                                                            'key': 'Ǆκ$úѤìƽțǷӵũԧźŸȩѬɡȳƿϤɭͽЈԏιӝѠоҔĺ',
                                                                            'value': ' ˕ȯʽаяʚžĭԕπøҩАƍĺ¢јϱҽѤŞОaƪЕ^ɔ>\x9b',
                                                                        },
                                                        {
                                                                            'key': 'ŅɒϵØÊTГƆӂ\x9f§-Ұͷȣї˓ǅʪʟ҃үưƛƚǗγȬņҴ',
                                                                            'value': 'dѠƺū·\u0383ίкº҄ǹЁ|ˇȪ\x8dįӟǉкVƦϰɀԒÑǶaÊʗ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ӷΉӦтʧŸʘM҃ûʷüdȟГѓӗWɹԄìöԈǤĴƠÁЂԪʼ',
                        },
                    {
                            'keys': [
                                        'ӢҴ˚ԕȅ\xa0ˬЇǲϞöˣÃ8ǦҐЏѐēyǆºȽ',
                                        'ӀӪʍʥѲŀ\x86ԆӋKTˎΆԙWƁȗ¹ҘϢǶȽ\x83ɟϢ',
                                        'ӗŇW',
                                        'ĬņȮǲтѭƈЗȬƐѨűҲ',
                                        'ĉА\x86˺ƏΆҼ]ǻӬļ4μǨ˱ηύ{',
                                        'ѾԝˢëɪπīȀӄͻˋÍ\xad\xa0ğTȗyҒh»5Ϝ',
                                        'ΝŻʤA\x91',
                                        '˝ˣŠϺxҵʪτчɒҊǮȉȁԦє"Ңͺόa\\ԚʒÌĉ',
                                        'ƠŻMӝ˂Ѡ-ƿϺӷұǦ',
                                        '(˅Ώ˓ƁʁÖϾʖ\x91ȏŠǻЉ',
                                    ],
                            'event': {
                                        'target_id': 'ͽ¬҄ͲϖƲҶ\x95ʩѓԍΠʲҽϬǨĕÒȥ\x8faͻ}ϢˡӳӶ¨Ԏп',
                                        'parameters': [
                                                        {
                                                                            'key': 'ĠAӕӕưԢϓέМǛԓ˼ʯýōяžǱÿмʽ҆',
                                                                            'value': 'њnɒ*ƶҘňҝЄˍ)Ǔſͻѷ®Ѧ9ȨυˁЄ˄ƬӽТ\x87dңԛ',
                                                                        },
                                                        {
                                                                            'key': 'ŉĪѽƄÇàÛԞͲҺɋϽΕĩĚMϣXǛ\x99ŜӧòȳͱċБɏqϲ',
                                                                            'value': 'íœ%ŀPǁ\x98ȉ\u0378ĐɁŲ҆҆ťύΜÿЛɮҡαȃɹАІϘúɺį',
                                                                        },
                                                        {
                                                                            'key': 'ҕˌɝˋȹ\x8dԉϏɑͽ\x94˸qɓǎϴſѪŋͻǇДĨ˺Ş\u038bӶтЌȃ',
                                                                            'value': 'êŞ±ӊҩǤ½ϚǀВюAWħӄяÃǰźлԊ\x81ғ,Ɠε҂áŔƈ',
                                                                        },
                                                        {
                                                                            'key': 'М҂ǣБӕƑϕƝϪ{˞ԑô\u038b',
                                                                            'value': '?ʻπǢ˴˼ɄȨ͵ĩXɸάμːʩľɺŋӇĂƊʵӬǁéфɔɲɉ',
                                                                        },
                                                        {
                                                                            'key': 'ǸЌќ¦ɥŨβUĐC˭ԗЌÕ\u0378ǆ˴ǐǚоcʱćƽżșϢȈԘė',
                                                                            'value': 'ŋnʻΊɞѝʣѪӨϴȜ˕òɅħԌʂÅ>Ąʳ?:;ʁǂ°ԘÛų',
                                                                        },
                                                        {
                                                                            'key': 'ƫXɣЗʜɐ',
                                                                            'value': 'Ɉ\u038dɥęˎīû>ҩɞ˖ϓɖˆάƥ8ώʠШτɡіˌôĚÈXǍæ',
                                                                        },
                                                        {
                                                                            'key': 'бċāƝêΙӤ|ğǒƐÛѸƇϓ\x9bKƵτªœ×ƺńҢ²ÆωϬŸ',
                                                                            'value': 'ШȩúŰͻђжʄ³ʵĻґљӼƻͰъΔ',
                                                                        },
                                                        {
                                                                            'key': '3аʐ#˫QΗƂhĴɗʂǯʐřԅ]Ŋ҄oˀʹĹӂĝĉŵĺē\\',
                                                                            'value': 'ŗ´КȊů¥ǜǉΜʹȶόōəǍƤ˥Ө\x95Ѫ\x90ǧɵΧрĨƏ°ÿӠ',
                                                                        },
                                                        {
                                                                            'key': 'ťƛѬυŔԗӂȶϵȔĚʠͲϕ˭ѩмђˊ˲ũ˔ϩȠƖǎЅǜƮþ',
                                                                            'value': 'óӫћǒԢʴǎǩʒȤƇϽͻҴâԡĠɫξʕ\u038bӑӱђȇĮСĞɵǖ',
                                                                        },
                                                        {
                                                                            'key': 'ӵ\x9eƝͷҋδκȖϋȎæȰЎӛʅƶÀēǕыǢ!Ћ\x88ӌ\x7főǐλє',
                                                                            'value': 'ЧÑӉӎÐԭЄɏU\u0382ϞϷǃӑϭЏӀçҨʆ˃łƺǠ\x84Ȳɾӷʐ\x95',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ѿɉıãƲ˓ʡҠϭщчÄБРǝˢƯ|ƌĢÛɏɭʮDďĝƃ©ƭ',
                        },
                    {
                            'keys': [
                                        'љlԤŉƉ҈ǳѕ',
                                        'ȲȎ',
                                        '¾ɞΦɛ÷Ҹǜēʧʫ',
                                        'фȱŬΑʍ\u03a2Ǵ˸ԊѻϱȠɨǖʍΒ\u0383ϼ\x87',
                                        'ε\x96χÑʣĲÄбĜ¤ҵў5pˋn\x8bӂӞѨ\x88ъ\xa0',
                                        'ǖǶ×ǺɪˎԒϨġύВ#ҷ²ы҂˽',
                                        'ΧŋԞȌӰяΪԣĀ4Љԗ',
                                        'ԍҽ¨ɃǷȃȌ˓íĪԌ4ŎXǳã\u0383Ȩ˶шцЇ',
                                        'ԭŒšӓӰţňѦэ˨',
                                        'ҬĔ»ѿP:͵ȳV/ԇǠЂɗ',
                                    ],
                            'event': {
                                        'target_id': 'b˔ʏϼϳƑɖ\x9bҚ\x9dʍĬŬǶͼВʠʉҰһ§ǠҪρƒѳƂɬŻҪ',
                                        'parameters': [
                                                        {
                                                                            'key': '¥ԋʶõγӌӐϬКʬŭƁҢθāӱȝoюϻ\x9d.ƻıʶӏǦ҉ʒϴ',
                                                                            'value': 'æГԐЇʃǹЄǲǅȷѲ]ΛҔΑǾőǟΓ˞ɇVΖ,ßųĦËwӏ',
                                                                        },
                                                        {
                                                                            'key': 'Ѐ0цÇOɥƢдʹ˥vƖȲΡΰĕͶɓƖΣ4ģ\u0383Ɩ"ƥIҖ',
                                                                            'value': 'ƝӤF?ϾЃ˒ѳǅ\u0382Ίӷ\x83ƱȻǎƗԇ·ȏҿˆМƏϺyʻϦĶ¯',
                                                                        },
                                                        {
                                                                            'key': 'ϊĐіêўԨǘƖЄԤ_ϵʳșɰĜƜϣæХȥΏѸϏɛȤșĒİǅ',
                                                                            'value': 'ϣѱϰŬ\xadэиπҒŽΨһǗĂЎǔγԃʣÔʹƛԨ˶ʔӻÏϞɈ҈',
                                                                        },
                                                        {
                                                                            'key': 'қʈ˞ïŵԥæϳʣίɌõ',
                                                                            'value': 'ўŅ˟ƇɂƮõ\x97öÝԁƎξŌЀεƀԫўΩ&àцңѥƼ0ǖ˴ŉ',
                                                                        },
                                                        {
                                                                            'key': 'ʔѢԙԥ±\x95ҒÀФϧ¢ǭLDΔӉÌǌǾʅʝС˓Ť˼ʁɎϋŤ\x7f',
                                                                            'value': 'ĢѻȲȦЩԨҧѭȼ;ʰФǏĦїїЂŅʉΒăѲ@ө=їɽϏԕʐ',
                                                                        },
                                                        {
                                                                            'key': 'ɲʾñůŕ\x93ӓϤӇŕҜğ\x9eȄƼ',
                                                                            'value': 'ǰǓМŐΔ\x84ԆŒkёҹҲȻ[ӐΑň˝ЗЎƎϫǳϏҫ\x7fηϒųȥ',
                                                                        },
                                                        {
                                                                            'key': 'ìȜƔ¦Ɣ%ӈӹ˂ÞˇUĸgҸȈ2ʌĬЏиƦшԄȱ϶ Oǉʊ',
                                                                            'value': 'ʨǋτ\x9cɪʦҜҖȃʭ¼ӈ˝wӇʬЏ\x7fӎԣȦ\x84ĠϞфȔŋɺŨˋ',
                                                                        },
                                                        {
                                                                            'key': 'įԔŌ|qҽԤԏ¸ԓ҈ʝӲϘʀϋÕҜ!ɾȞȚϐ',
                                                                            'value': 'ϚǞή\x87ѳƕƐĄÔAϥԬϦ\x83ˈʋĚčРǝ°Ґŷł®ș˦õƋѐ',
                                                                        },
                                                        {
                                                                            'key': 'ĎɥǣЅˌŀ=ȑÔǄңԫȃįţRjӏºӶϔѴƴŁҭóTҲəԓ',
                                                                            'value': '|xʒӀ\x93ʜʬԌΝϥͶϴϰʪǖÇq)ǕÌԛȶӓѡϿӍ#Ģĸʸ',
                                                                        },
                                                        {
                                                                            'key': 'ɅǁɴԤӗǄԦˀʀƜοˑɠјPđFԘɓˬȍυÅʂ0ŝЪπƔĪ',
                                                                            'value': 'ӖūʟԎCӹÙ\x7fȀΣȇŮĒʹɜсȡ˒·ЌΣÄʄԨҁҕХӴѳǻ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ԒĚʺ˥ʖɩрêǢŚТĘ·"¬ԋQƆÇɞȿϾʞѰǬÀÄʚǥɒ',
                        },
                    {
                            'keys': [
                                        '˲ҔɀĿoĂӢʀҞãҬ²',
                                        '\x877ȼѺ',
                                        'μƟ"˴',
                                        'ǌ˜ť;¢úħ¶ȥԡuϙьӂӳ˫ɕĎơԗM',
                                        'юɤȳ',
                                        'ɖ˳ѷѨϊϫǧ\x94ΆϽ\x9bĂΕĒҺѻѽ',
                                        'ɽHȅфԎŵԂxԨş˭ӳƜӫҡҴˋӝѕЊІúßɑˉĴˑɳ2',
                                        'WȺȍӿƂϿQƸн£',
                                        'İƙýʣнӶGĹӅ¢}ʸʏϊŃÛşЅ˭͵ņҔԙЫë3ĵˑԤ',
                                        'ǅŲʹǺȱɓɒƄɝԏԊƷȪƯÇĉҩъ˻\u0380¢Ǫѻ˲΄',
                                    ],
                            'event': {
                                        'target_id': 'Ю0ʘ{ϛÔÿƆƍЊŤԤҿаǃĎŻˠƎ\x97ĴЋʜēʇ3ФˁΆҨ',
                                        'parameters': [
                                                        {
                                                                            'key': ';ӌɦŏÎóɺϢʭFΫȾԟʆʇҷԚ:øӜϣӲÒĿСӂωâ\x84ʉ',
                                                                            'value': 'Ȃƹƫ=ˠZҖʠϣw¡ˮÓъɬ¾ɑľ²ʣϘӻԡт!Ʀȋ,ҀϨ',
                                                                        },
                                                        {
                                                                            'key': 'Ǯ˅ʕԨX\x8b\x8aϙƋɠŰʷʅɸʨΖѹϕ΄ДÅʴȱκҭɤ˰¨MΤ',
                                                                            'value': 'Ϊ;ЭƤԧҊλɧΒ¦ȝƭӽ҉ȃæЄҍϲȧ˫҆6˧(ВƎǁͺƫ',
                                                                        },
                                                        {
                                                                            'key': 'ΤӻɆώρԢɜϜʇȟ¸Ú˥ĭǢËɌƶåĘѺˀ¿ʻˋӿԠӺԡЀ',
                                                                            'value': 'ʞƝŴтʮ\x7fx҂҆ʓªȉ"ƣшĲ\x88ʀԂԉ˃ʆǰΥ\x84ӅěɡӽĹ',
                                                                        },
                                                        {
                                                                            'key': '˒ɣȀҟ@ȬԬAѼΎКɵɷSßƈșʳǫʤ\x97ʇӊ\x7fňøϤЊȞғ',
                                                                            'value': 'qΊҗƜӹ\x8aѽԌĘЯԃ\u0380е\x9f\x82ťǭϥ\x8aɠҲҖʫ;ɶ·ŽɀÞ˩',
                                                                        },
                                                        {
                                                                            'key': '¡ʙʢѷȳüъĵѤƜҦɟӆþԓòǒqƍĵšӧŀ\x82yԅҜԕŏƢ',
                                                                            'value': 'ς1уŉÙǄό×ЫҟĽ;ŚɇƩǵȍɮϡǜƢʏԭ\x9bύЪȋ˪΅Ɔ',
                                                                        },
                                                        {
                                                                            'key': '@ńȐ"ɉѼЍˊϫӇƓŒ˽ΜIʻƚӉͱƯȯ΄\u038dd˄ƮԮʐǙ\\',
                                                                            'value': 'ԜȝêӐÔђѝQĿİΌˎ\x9a˟cȶҙ/ɹ϶\u0382ɕǺçƯ\x8eόδϲˋ',
                                                                        },
                                                        {
                                                                            'key': '7CȬӺʌΐûöъҧˊŘйәċƮȷưίȰӗфѶ\x8aʰÍżЅϷӸ',
                                                                            'value': '˱çʨɉʄˇӺΖǕӆЗӰͷ-ŋ\u038dԑҨОıŦǥıϯŶǔ:˥˧¶',
                                                                        },
                                                        {
                                                                            'key': '\x96҉Β-_ϕ¤ǇӕŲļ½5(ǅʹŹ',
                                                                            'value': 'ϓ˫ëȥ˦ɆɖћΡҬŠňHĹ϶ȈҿӻɸʅЏНɖ\u0382ʿґƟǼџȚ',
                                                                        },
                                                        {
                                                                            'key': 'ʆ\x8a/ӓˬǛȧŴ.ϹȏƹΛԄ˶\x93ǴȜϑԕŵЧǵԃɛіǎԓ',
                                                                            'value': 'ϴϫϤǉɵ˕ίΤĆ˷ЎԦ˪ɬȍɗŔˈʭ5ӃҴǍÖƏіªʵ˚Ȇ',
                                                                        },
                                                        {
                                                                            'key': '/ѧπԍӵöÐɃÂӌγ˕ϺљӟŧϯŝОǑůɵʃȉѱ\x83ΒԀνɬ',
                                                                            'value': 'ɗȣԣƚʤņ\u03a2ȔÏӰƋԃȟԝͶУ\x88\x83\u0380ǓĥƆлԀσűʶ[¶Ċ',
                                                                        },
                                                    ],
                                    },
                            'comment': '\x9fƆΝҿǟĪԀƮҷςШԥρnǟӧȧІκĜӚƺĚψ`ȧȪǆхÈ',
                        },
                    {
                            'keys': [
                                        '¤Ơ˝϶ПƄěˢѿ\x8aӗҝΆɿŏŗˊѡŮƜĂөrˎŃƸþÂ',
                                        'ɝѮɏʿЦѶƳtǒǹʔȶ',
                                        'Dʞʑŀȳūδԁ}àxňйǪ\x99?\u0379ҺΜÔǵѲ',
                                        'ҝëϹǪУȭtɑĹҺd˘<Ⱥ\x8bΌОăӧǍΠ',
                                        'аɼӑǮ/ѝCϊ',
                                        'ҜңåȊ',
                                        'Ϳλʼԏ',
                                        '\x85ӕɪɘҢ±ĖӻìҢʏð҂ƨэ҇ƿĘƔӥ',
                                        "-ɕ\x84˃ӑӟʈ˩kxʷ҅ъ'ʭйЁҢȑΕ",
                                        'ʝ',
                                    ],
                            'event': {
                                        'target_id': '&¨ԆþǩƧșÇȳǛϾҳü\x8bӑƏΔ*ҷ\x93˭ȮҸƎӟƑǃϹԐǾ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ČгƀÿµԝȓЦѴơʏʄʪĿǁηӣԀʦƌĸ|ŋ8ӚȭǱρўȽ',
                                                                            'value': '"ÝϻҁÀέәҧƝӄ\x96ǁΦ7ģöʻʷД˴ѮԀƋ;ƲКƄҬˮȇ',
                                                                        },
                                                        {
                                                                            'key': 'ԇΪ\u0383κ҃ωɷƷΊǹŰBΰΊԍŪȭx6өǛ5йҶЕʏѽж{ǒ',
                                                                            'value': 'Ьχ×ӣԂˊĂŴ{ƨйíԉĘȾƟҹȻΨbǥÙ\xa0ǅĘȿĖǛϗy',
                                                                        },
                                                        {
                                                                            'key': 'јȱд\x8aɰы³ŗ',
                                                                            'value': 'Ψɴ\x81˛ˑаΠȽГ<ȫȱȜʀȠӃ˄ȥ\x81ʽіѷʀѧfȺ\x82ʺēȉ',
                                                                        },
                                                        {
                                                                            'key': 'ɦƟmύk_˓;ԀƣĨ[zŖɱǷа˒ϔϧИȈ¥Ύԉщʅźʬл',
                                                                            'value': 'ԤТԂçőúЂӽƴĻ.ģ˓ыɖˤԖĂϮӠэҴïҊ¤ѱ˟-\x89ɓ',
                                                                        },
                                                        {
                                                                            'key': 'ѢԦF{ϻČӼʇƺҷÃЁÎ˰¸ӴǮ\x96ҮĥÜȗ\x93\x82η9Ŵ˸ЁȀ',
                                                                            'value': 'дʙ˶ҩ\x93ΠïȠĶϥĈɨ~ǊҼͿŕЂɇ˽ͽŤеʹɶŵP˰Ӊҝ',
                                                                        },
                                                        {
                                                                            'key': '˝į˟М<Ń΅˛˷Δʴӣŕ~űˢÏſԕɽЉ/˨ȼэӏˮͲҪϲ',
                                                                            'value': 'ΖјȉʶΈ-ƧǦӆGǬşȃƸˁøʝԭƔÚϓԐ_ӎ˰ǖҕӇȣ҄',
                                                                        },
                                                        {
                                                                            'key': 'ΘГ¤œǠҾѠΡʥЭ¬ǳʛѶӈ=ѝ{ăũŨˍӽɷѫȍͱɫ·ξ',
                                                                            'value': 'ɓÕӈƛϦɀǎł\xadАƁˌĒȱƐώѕʃΕʍҔȻǗɒɫӐa˕Ͻɳ',
                                                                        },
                                                        {
                                                                            'key': 'ҵɌʣ\x97ʰ˰\x9bиѡăÊ',
                                                                            'value': 'űҳ]ӒƔ˹ϸΩԉѐѺzʚҠùμʭŻľϷӝȳCԈɝΎTӺХ©',
                                                                        },
                                                        {
                                                                            'key': 'ȇƥæƾʟÓȳŗӿ\u0379Ȥ¥Ōȋȝěñí˭ЦĨƋҪάҘƔϺǇŴӽ',
                                                                            'value': 'ȠʋЩώДǿɤƕƈҘӀǻԮЛѣGş×ʍγнĖȖǊăҋҦγżŰ',
                                                                        },
                                                        {
                                                                            'key': 'ƃɓ\x9cѯ,Ë@Γ5˘ʋɜҤėǸНͲ;ǣǰФĲĒɯÜÉeLȍǸ',
                                                                            'value': 'Ĉѝʇ˪ˑЎʐǄVČįƤ·ʏĆιȡȅиȆБʔţԦėжͰțѩǖ',
                                                                        },
                                                    ],
                                    },
                            'comment': "đӠɚ\u03a2QԀʲ'ӸǞŤѯҰCҺԡŷʹϢ˭ƿӸɍɉÈѧóөΜ2",
                        },
                    {
                            'keys': [
                                        'ӡƭǁТcţмƢϺЛԅʝє',
                                        'ˊƴͱɤɵʫ¸ѣźƮҊӬʎʃ˯ʷɸ',
                                        'ēȜ¾ȃŠӕΣȎÓƥƍ«ʗӺԏŲéŚŏʹӣӺ\x8aʣř',
                                        '˲ˑƠОȂȡìӋѢ˵˯˕ĊŇM"АғӫԎԙŬίõ\x9aѕɭч˦',
                                        'ӅȄ˱ȀÒϰϜρԣśũɫ˘бϧĤȐ\x9cТÅϫÎԣʍȏąϬWªϩ',
                                        'ҐύӧɐѤɠǉĜʫԀ\x9dǊYбĀԭӱµy',
                                        'ʴʒƧĐ˩ôɻƬø¦Ϯ˒ƶǈӴŌĳ˩Çԏцс#ˤ',
                                        'ΞǅȚüʇ˜ƻǸŔʟʢÊϘϮȣšȆæіɄϠӇϦt3',
                                        'ßϜͺ2ǴНĸзǠʘŞʹϿԦƔƈϑ/íøбӁΏȇ',
                                        'һɁˊÍºɆ¦Ӟ',
                                    ],
                            'event': {
                                        'target_id': 'pʇĩҞƢtιϑǋȧҚȯÞ¢ӄ\x91ŅmӰώϠȩĵʫ҈ǏƢŕǄƧ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ͷҳƳ«ͶĸΟӛШƾʢʸόʤҫҺҞ\x83Ԅɰͷұɐϊ\u0383ɣæңԘЏ',
                                                                            'value': 'ɪ˟°ІȕпƏʅƥʣΣŭÊγˉпЯѳϤjԍͱ\x9aϤǒҹўԢ95',
                                                                        },
                                                        {
                                                                            'key': 'ҧYǜɿK˻\x8cНХʗѿˏύÆưƼέΫʄԁϤҴјͼ}ӖͰКϙŗ',
                                                                            'value': 'ŝѧѰťͶмǡϩ\x8dˈȷˎԏ3ОӿȜåѶԔԕȿɽѽʒ¦юĢОɱ',
                                                                        },
                                                        {
                                                                            'key': 'ѴϻƧŻȑÓԑZƼιЇƯƯʊȠʮͶţpҰҟРӯљʑ\x9fʹҢþȜ',
                                                                            'value': 'ӪЄҟcdȯŐȴưǟΣǬɅáʡώĞNс×ЋOЅƇȃяƁ\u0380ҋȊ',
                                                                        },
                                                        {
                                                                            'key': 'ȸĦ³ƃ\x8c@WʡԨªҋТӹǉǿžƮœѳ)µњɅǎ1ήΤǜ³ҳ',
                                                                            'value': 'MԆЅȤƧǨˢЊΒǨЩȎ˹ѓ\u0382ΥвЌŎ\x9aωяʻǝƸԣϧӟºˤ',
                                                                        },
                                                        {
                                                                            'key': 'ӜАԐȐˮƏȊZԆԖ"҃GџˮƯУʀͻɼӳαԄУÅʄ˽jӝғ',
                                                                            'value': 'æÒ½wÌɰƜϕ',
                                                                        },
                                                        {
                                                                            'key': '¢ȦϝΟÁÜĄмƟ',
                                                                            'value': "Ҏđȯħґƅ'ƺͼͺʵ¥ҖӇ˙РˤϚķɆȃėʾɵңΠΈ΅ȸΘ",
                                                                        },
                                                        {
                                                                            'key': 'cΤƂɇĘñŎɗɑǮƞˮɒ\x9e6άXϳнͳĖarȴϧ\x8bÎӖαƖ',
                                                                            'value': 'ӗȫ\x9câŔΝύΡ\x82ђϨТ\x86ɧ\x8cČңȁ˸ıɕώϜҨІ\u038bҚЙƮϞ',
                                                                        },
                                                        {
                                                                            'key': 'aȃӥǋaͷӬԘWˣ\x9asҘƠͼӐŤ˙ÂϏ҃ҞԬӒξʵκ¶ӑӔ',
                                                                            'value': 'ϏϙоȜ&àЩʃȸŏǄνźűҙЂĔеǧѽЯǥȿϥΪɼȓ˷\x8fs',
                                                                        },
                                                        {
                                                                            'key': '^ƽǬǏkĎÖЕƓƘɁБǼ˴ιǼÿΊØƻҼϛюõԪǎѷ˫Ǌʴ',
                                                                            'value': 'ТΪ˜ŖĸũńīлĿѕэœрʽ˯rɜЮ˯ʌˁ~ɋɨXŬϼ˵Ԁ',
                                                                        },
                                                        {
                                                                            'key': 'ԧL˭ĭ˴ЁtĐ°ĥόʫđϩҥłǠǪzÂƳƂԭʳµͰʴ\u0382ӣӍ',
                                                                            'value': 'Ƴ\x92ɂ\\ʇҤΗyƔʳԜϞųӄΌһѷӃɺƫ\x97Ǘͽư2;ҸŏǹԌ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ǰРӱŷӋɱ˹ѡˢˏόµǪ\xa0ǰӍŌϦùæ˛ÇԐ×ɚӷ?ΕѨȖ',
                        },
                    {
                            'keys': [
                                        'ʦԅ˄ƚ',
                                        'ЦеӲљƺћǰӲőһϖħåŽӃmԫȇшȲЋVɏ',
                                        'Ҷз',
                                        'ʣФĢˎ;ΙʨџЀɿҵƐ',
                                        'ЍŚˤ',
                                        'ǰѩãϯ͵ϏԛƚǠǶ§',
                                        'ҫШǿpŦԑʦ',
                                        'Ǡ©',
                                        'ԃΐϞÖщЧ˲Ά˔ɾЁũǞώπ',
                                        'ßӍΚ\xadљѸɳ³ЈЉȒ˓ԦȦƽɢӪɒμĈŉhϓ\x99ɽлÍ',
                                    ],
                            'event': {
                                        'target_id': 'ėƈМΔ˦\x8dѨӤɋȢԥkĢ¨ɂҚΣΖĚƔN@РçǥDѦĴʥĖ',
                                        'parameters': [
                                                        {
                                                                            'key': '˅ӝҶĩ˚\x80q\x93ƹӑʘϖԂÇΓӰɸѳɐЂ\x85ĤBУíͳǨ˅ʡÑ',
                                                                            'value': 'ӄϐ\u0382ʳ˖Ҟ˧ҭȎ²ѣΜ·ƫЄ£ɎˌҨšЙҎǹ\x84˒ЌӧѿĎˮ',
                                                                        },
                                                        {
                                                                            'key': '¯ŽÿƉɝҹ˗JÁ˦ŲO\u0382',
                                                                            'value': 'αӎԬԨĜǟʿśʋØԂµнŞüϜŤ˚ȧÔýɚɓϦ\x91ŉϦʹɁҳ',
                                                                        },
                                                        {
                                                                            'key': 'Ĉƍͼ˵ľúƆыѻѾǒƂ\x7fȆӏūšӥƊsӓԐ«ÁһȨǮɩĩˁ',
                                                                            'value': 'ԬҖʳӟғԜΨhȕ¨ϜAɿaƙȚiӟѪˊ°ΦȑɣŴɀLϱ˪ʮ',
                                                                        },
                                                        {
                                                                            'key': 'ϯΔ˖ԛěȶЉȧĘȣ\x80ȿΐ\u0381ϲϖдш˭҇Ӊ',
                                                                            'value': '2ʗѽƺҞơϚƮͲ˶¥Å\x85ǚӄǪ²ʃеʔ6ˀțÆЏĚȝӯ˷ŉ',
                                                                        },
                                                        {
                                                                            'key': 'ԛ˫ğŭĮɣҭ',
                                                                            'value': '×Êē˅ʱİ{χ҅ԬȤD#|&(<ċЛƒŪƮÙǭİ;6Ӳлʞ',
                                                                        },
                                                        {
                                                                            'key': 'Ŷ2˩ȁèԝ<ŔԥʕΩûҼԕȼĖŔϖĤҐВћɢ0оɪqʴœϸ',
                                                                            'value': 'GʼǣɒąȨԬǍǮfӶ¥\u0381¤N°Ӄɼ˱˂˕\x9eȹӽEɳмцˊφ',
                                                                        },
                                                        {
                                                                            'key': 'ƣțɨvӶ\x9fŵАҼǁѰǍƣԖɕƨѐϕÐѳ',
                                                                            'value': 'έɳΑƚԒʌǦƞƃġƵīŚЩ-ÁţҰʝçĘџͱӱтƐѩϳǘq',
                                                                        },
                                                        {
                                                                            'key': 'À·ҊƘǎΉǎǯƁLңȄҎοĈɤͰӖˉ\u0381ӗŖǜӞġԔɐɻjʷ',
                                                                            'value': '{ðȀȉӾӰѐJŘʒΆĵǣAҵ¬ƟˇïŅƓăΟϥДǦɤ˲ЙӍ',
                                                                        },
                                                        {
                                                                            'key': '˦ВӀA˧ϭСΣ˭ġʙӦ%ҕȚ«\x98ԔӮ¢ԦƽŅ¬ςЃǳŻϾӁ',
                                                                            'value': 'ʙƻŎ÷ʰɍʌƍųϕɚÑcÚӂӾġTαȃϡ˾ǶяiҬȳ\x8aτɱ',
                                                                        },
                                                        {
                                                                            'key': 'ҠŸƭʔyŕʞŎҰȧώә',
                                                                            'value': 'ԦӲ>ĮÉǕɫɻŢȌϸȾþӖǺaȣҠҁԢ´\x96+ČŞŀƤʂɟɴ',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ŢŮ҆ĔΊÕӸʴЦŭԑ\u0379α4ϛӭγӽÅȯӒƢƉΨӡԨģɾŚƱ',
                        },
                    {
                            'keys': [
                                        '|qѷgĤɿΠŻцǲď˘ѸżŶ',
                                        'ȳĺέǈȣΐKőȻβ˭Ιѕ:Ԧʙ9ϱҜ\x8fȖλF·ӡ',
                                        'џŮɄϭ\x87όʨǿѯǳӾƩģҒĝϊȅҍ˻ҐÞʘ',
                                        'ryƫé',
                                        'Ş\x94',
                                        'ĠçӖԔǲӏŧ²Ҧ',
                                        'ϣԔπҏÄҾϸ',
                                        "ԕήĿǭǎƚɬҍҠМ'͵9һҮнŤџ",
                                        '҇ˍơǿŷƃƪĀ',
                                        '¿ӱÅʶŷ¨ϓҍżџƈ\x84İfһΣΪŲƻҕQÄîθȦ',
                                    ],
                            'event': {
                                        'target_id': 'ǧїӨġʕʡmżūӟƽΚǅǍќφȇμƊƞƏͺºawҳǣǢԑ˴',
                                        'parameters': [
                                                        {
                                                                            'key': 'ɫӡǱőαˬӹЕʏɩƎìҷӮТѢ½ˑÆɐĘ˪ϻɠɍΏοƼΙȜ',
                                                                            'value': 'ΥӁÚʧԀďťԐлøď\xad\x98ßԬȅΧ?ѳƶĘѣʾРʅџγ¯ό/',
                                                                        },
                                                        {
                                                                            'key': 'ʣ~P"JԄūȜӴ҇ЭӪѐ¥Ѝˤˁå\x98ΥňͱǃӜƂ$ρŶʘβ',
                                                                            'value': 'ϪͷưԮԬӲϨ\x9bƶǅфʀǙӭÙȥҩǧǝ\x83«ȧƅҲœ ҵ·ƭ2',
                                                                        },
                                                        {
                                                                            'key': 'Ԇ¶˭ǥԒsCǙĔǋñҦɚ:\x9bůÐѣ³uԚǷѥōǎƊŕʮǫƪ',
                                                                            'value': 'ʟͲɱӟϱɭβĻєŗЧԆİПȈөUԧșӯȳԗҿӇҴџѡΓζɠ',
                                                                        },
                                                        {
                                                                            'key': 'Ƅӄiѵ>ҴǓƘ˻ʳʷěʵ\x8bȢɮɆĸ\xa0Ɣɤ\x98ʲĥɶÁƫŃ//',
                                                                            'value': 'к҉ǭϦӇЪҔ`ʥƲʟȤŪͻӀʞēљУTʰвҔȇʢɿɴʺcϊ',
                                                                        },
                                                        {
                                                                            'key': 'г¬ſŇԍȤǬԁ˚σĭ͵\u038b\x85ſĂHðǒ˯ΘȟƧȱъїрʮԠõ',
                                                                            'value': 'ΔϻfÞŏϩϷ˩øƭʋɕθςʹÚӿtęľšőӣчƥÈ¢҇Ҏƶ',
                                                                        },
                                                        {
                                                                            'key': 'σȯҐËîМөˎ\u0382ЅƄĤ˭əӥʙřʖ?ӚI\u0380їʍ',
                                                                            'value': 'ӘǛȊȯӘЀǞɼ\x99ŷõȤͿǛÔΝ(ϻƻɥӺȅƏȊŚěѐdąҩ',
                                                                        },
                                                        {
                                                                            'key': 'ә³ƓƓϝʫɸ',
                                                                            'value': 'ԙѡŹjʦϿUkȓҐ¥ϕšэ\xadћѴɥуðυÙǚɥРÐTΌÇǝ',
                                                                        },
                                                        {
                                                                            'key': 'ĦԋǰҶŪ/ßt˂ÇԏβxАӻ',
                                                                            'value': 'ШǬmЋӦŠʸʥÏśǮƘƢӞПКțŎЖ҇×ÍΜүǐƄԢǍϞŜ',
                                                                        },
                                                        {
                                                                            'key': '\x8dʈǵЇŻԪиäãѱԕʦ˼Ѱ\x83ώĖ5ĲнǦ˘ζ',
                                                                            'value': 'ʹюĐϥКƓȶӕǯΛ\x88ұƎēTӠЛ\x86şşɏ¹:OҖΥ\x87ƞƫР',
                                                                        },
                                                        {
                                                                            'key': 'ϒŸɨɳӭ_\u0381ǨҟɥԘǏªԐѢξџ\x96ǴȂƢҐРѣǁԦǮâĬԣ',
                                                                            'value': '/ҡɛӎ÷ϏΣʴ\x87ſȖ\x84щȆәαψȳΩƌEʣ҆ǠȅŰӯӯSО',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ãѢӅŖʼ˼Ǯϕѥρ\x87~Ȣ˶Ő^Ϥŷƣιɳӓʴ¡ʀǫŒŮhσ',
                        },
                    {
                            'keys': [
                                        'ʴ',
                                        'ϏϢɿ\x9bëΞ΅ШəIɔǩѡ¦',
                                        'ԜŜěƁɯƥϛÁʳӣ>',
                                        'á\u0378õʕ\x91ȮĊÎɾǆұзβ©˞ĺĢ\x8bҒǎԞ˯',
                                        'Ҋ˚ǤƺÛǯÙѾϺƢ',
                                        'ɊĜþǬåΖŐƠϔ',
                                        'ˈύRɟǳ)ˡ˩ƆҪβԦ\x86«˟ˑƢǋӷԀơΐҥӠʽĪɆ',
                                        '҈ϳƄʺБҗƁϰɪǸӷϿȓρ',
                                        'ǊǃŃȧ¢ÝкԔԞѮȢgɖƈҫ«˶ǔԙƒӽГĨҲùԜˠʅ',
                                        'ϮαΞοΎ',
                                    ],
                            'event': {
                                        'target_id': 'ƣĪʀԍӬԛeϔΐɂiĂЍÞӱӨǂӺ7ñÌͻĻӬʻɩȯҗŀӗ',
                                        'parameters': [
                                                        {
                                                                            'key': 'ҹҷѱƼЫɠαŌЌȔɸǈʨӔʹǌвҏ\x97ɿŪɓϏ°ô\x89ӑлKƫ',
                                                                            'value': 'ͼþӺѷӶ·ЯƷϰѯӨƓӼѨӺԗűϬβѤȒLǟľɳe҆ŃĆɦ',
                                                                        },
                                                        {
                                                                            'key': 'ѭ˙ť\u038d˂ʹʔuǭ˦˷ϨƖþѐĪǨƇêʣ͵Ѣɯ҆',
                                                                            'value': 'țͽƤãŅ"ҞӡƚϮѳьήαѬáʋΉŬɃʨʦη$ԝ×ˋ`ƕĮ',
                                                                        },
                                                        {
                                                                            'key': 'ƗСҋǳ˥ЀƨȫԜƺĒǈʙςʤщˤ\x90ƬţŕïӞ0Œ³έʐ&´',
                                                                            'value': 'PėəƻˌʰĠĲˇХŠƱΥӿɰƙȾMγөԢЎҸ˶\x9fɎ\\ǹ\x97Ȑ',
                                                                        },
                                                        {
                                                                            'key': 'ʂŰӀ\u038bŢӁƜФĥҵÖĉӉҬ',
                                                                            'value': 'łӚʭɃηǃ°ï\x97ѣ`ǮЦԫ\xa0ZψĒѷÚɓžĤΡǊɦΥϚĖŗ',
                                                                        },
                                                        {
                                                                            'key': 'ɺƇБȅϤ˯ƦƙǙЙʬ¡ɐѐʓԤϺè˶ƭѸϞϼHǐŲͲ',
                                                                            'value': 'жİӪɭĳƮʈHͼЙҎź0ŋͼ҆ƭƌ.ΑŞɋàQȺÀΗƾ?Ò',
                                                                        },
                                                        {
                                                                            'key': '+ƵǞαSʄɨƔƋƽԋĘƦϸЮӎǲËЋƄΘϋȸɺҼɶˑʮЬ^',
                                                                            'value': ';Ż˪ŮÔǋºӗӱЧ\u0380ЖXðΒԅņȌͻŗİ˲ĳÝ2њ¶˲ˡǯ',
                                                                        },
                                                        {
                                                                            'key': 'řЌϞ9ҿѻǐȻģӈàɈf˩ˏĒκŶùéӃȉ:ĭЖ',
                                                                            'value': '˗ȋЕϊƝƒ=ėćPφ×ӷԝҧϋİǘĵѢԪԔҺϼÍҲÝήӃх',
                                                                        },
                                                        {
                                                                            'key': 'ċΥ*Ԧү˗ƭut\x97ȉǓ\x80BUǝ',
                                                                            'value': 'Ҋ˔ώƷԫƅ¥şɜǝþĺʎĈ(ͼұћГȴȻˎœɪ΅dз¶gȧ',
                                                                        },
                                                        {
                                                                            'key': 'ˍϾɘũνϣԗϮǷԪĘЎǃΑώҩɺЋӻÞýϭȗġ\u0381đˏɒԕʜ',
                                                                            'value': 'Ȧ·ƵŭʾШBɥЕϓɭɁN#҉ȥӵ\x83H˻ȍҥđɽǅэIGϪň',
                                                                        },
                                                        {
                                                                            'key': '˻ÏDǯˋДƢЬп>ˌ˭ђӫŃҚĕͼƽɰυңл˔ѵ)ȼÚĞƍ',
                                                                            'value': 'ӎηǜňɟɴϷԥп˧ԐïЙÛӇɸ˯њaӘқΠϜĸϥѷќԅɽ7',
                                                                        },
                                                    ],
                                    },
                            'comment': 'ͱ¤nƃ|5ÛSΝα]Ĭm"ԇƉЖȾǌŇɽ΄Ǯӊ\u038dΕŔɃԗӵ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'bindings': {
                'sequence_type': 'meta',
                'master_sequence': [
                    'Ϻ',
                ],
                'bindings': [
                ],
            },

        },
    ),
]
