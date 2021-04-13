# GENERATED CODE - DO NOT MODIFY

"""
Tests for the hotkey_binding module.
Extension petronia.core.api.hotkey_binding, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import hotkey_binding


class SetMasterSequenceRequestEventTest(unittest.TestCase):
    """
    Tests for SetMasterSequenceRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_MASTER_SEQUENCE_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.SetMasterSequenceRequestEvent.parse_data(test_data)
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
        for test_name, test_data in SET_MASTER_SEQUENCE_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.SetMasterSequenceRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_MASTER_SEQUENCE_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sequence_type', name='SetMasterSequenceRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='SetMasterSequenceRequestEvent'),
            ),

        ),
    ),

]


SET_MASTER_SEQUENCE_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sequence_type': 'meta',
            'keys': [
                'ʚҔƴȝʛɻ',
                'ѶҷƚəǼVԠ',
                'ŶǋҠԌ\x90ȔƓ\xa0ίѳ\x8d&шÖϚćȇ',
                'İτÒБɠȿưƨ7ŸϑӵБɔ¹Δ\x86ɑɡ',
                'ȐƏӬрȤԮʾńÒĄȊ\x90ȱƜʱʪƑσğιдēůǏєѣɄɐͺȉ',
            ],
            'comment': 'αǀӌɓƪ£ҾƍʶҲˆɤ˙ǯɶѧ\x90\x89ӰĂҸŊŴЍDțӍ\u038bПҍ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                'Ĳ',
            ],

        },
    ),
]


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
            'key': '¿ǎѓ[ďȌÞҘцœÓ@ӤԭìϹŝɝŮƎŇЏΰΪʟϜˡ҈ƸԊ',
            'value': 'ɿİ˶ǄʣTˁȽčΦÙП¨ϺͿѓIǻҡĭȽъҦɗϗ¦¾fûˁ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'җ',

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
            'target_id': 'ΈӫλȊҗͳӓϳÖӛƈǍȸӊʭԛhӼӬҩąԥíӚƀŃјǣɓ\x97',
            'parameters': [
                {
                    'key': '\u0379 ϳЛԕ˾,ǍңÄƱӎъϘ{ʓŊѿџơʾƕǓċӖЛҶӬΜź',
                    'value': 'Ð[ɫɌϘˋЪ3Ȝ\u0378ЬӅƥșϦIˆǇƠԟÕ\x93ԂʈǸÒӇћǀѥ',
                },
                {
                    'key': 'ɾӃɄǥԤʞqзԤƙǔƌɉ҃гƖ˾sЅәǭƨ#ʻϔǡͱîӥӳ',
                    'value': '¤ϵмЯʲʽϯӐѷН7ûȔ\x8eϫͽJĵħΦʇ(ԐҐԁͱΦǯӌυ',
                },
                {
                    'key': 'ǾƋʓɧ±úɦɁʠ\x8d/ǳҿ\x8a\u0378ϝкÌöķȌԙ\x9dƋµƖһǖǺо',
                    'value': '҆ӾϷ\x9bџʖƝ˥}hΞӛʳ.ɞ§м=ɾĠɥĲӎǊ˲ӖżǙŖϰ',
                },
                {
                    'key': 'EɗZθęƙËʉ9ŇӻΫÕëΩţϙӮǩƖʘΊƬȾ΄\x94ϐèʦɳ',
                    'value': ';с\u0379Ʌ\x95ϧΉ҄ќƝæ҇áǅӗҴȓńԇӨƙЦĄϜΔƫ»<ǃО',
                },
                {
                    'key': 'ҿњɹ¬ưȣ´ӵΗϓгŽǠӛƬѣҥЯɺӜœÑƂʫƄGͶ',
                    'value': 'ģǀĴиxgЙФΪйϾǬ˦ȖȾҬȴϩӳÔҀϪȹѓɔÑˉ˱Ρё',
                },
                {
                    'key': '9ҾgʆôʖкϞ8Òɻ0ˤԝ˫ʨɍɋ¡˞ɮϬΛ:|êďǙ²ʚ',
                    'value': 'ÖθϗЦ¥TǩΟїɩдÓЮƃÉьŅҳŪǟҬ\u0381ȶƺЂɧҥ¡ʕc',
                },
                {
                    'key': 'ˣÝђ˾Ҳ\x8eV˱ӜүҩÔФhƎ\x9aе4ʬǈм¼ӓʤƼýωǞϝ˺',
                    'value': 'ɾӕƼδļБ2ӄɴЙθēρņύ~ȐҏµɢƛѰӖѡbБʎȆɉԐ',
                },
                {
                    'key': '×ȥȴΤɍű˫Ҡİԕ\x87ϡȽĩňԃţmȢǚ\x94\x8cțΎǒΆʚИ\u03a2ʅ',
                    'value': 'ȍʏǵǋϝМ\x8a¥úүçɶ ØÜ\x9eˤƆąɆƒқԉΝѽηҎ£Īѕ',
                },
                {
                    'key': '×ȗєȥ.Αɽťǋҗϒ˸ƋƆȳ¤ԍvЬˀ"ѴͷνƃӖǃˑӛş',
                    'value': 'sҵřŗŀºʱyϝÐŔѨɷʡ\x99ȵƷɻҶЖĶŎÏŏƅ`ҿΓ¢X',
                },
                {
                    'key': '˅B¹Ĝïʴ&ƩuΤƺĪɎ\x95Ѣ#ԚǁȿЀƿ¤\x81ӟʱƤ\x9aǙȅɘ',
                    'value': 'ϵτʕ˔Ǵχ\x82ʯĻ³ҒθМžэόЦŽ9ѰªӈªâǂӸ˳7ҪA',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'YȒòÅˢ',

            'parameters': [
            ],

        },
    ),
]


class BoundKeyRegisterEventTest(unittest.TestCase):
    """
    Tests for BoundKeyRegisterEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEY_REGISTER_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRegisterEvent.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEY_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRegisterEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEY_REGISTER_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='BoundKeyRegisterEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='event', name='BoundKeyRegisterEvent'),
            ),

        ),
    ),

]


BOUND_KEY_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keys': [
                'ˈҪŐӬɝǱ',
                'ҎνEΦƑ˪ůʽϟҏɎǉӠϣȯӴԘϳȉ',
                'ѣȖɿҤќɕ\x8dĀԦƱĵƼϋΈȒcˋȘņԮ',
                '\u0382ˋмÁȭǾŰϢτĂȎĭƕкÀԂɄ>ĎʭοюTȌ.õͲҴƣ5',
                'çɾȧЍƅ',
                'ӳɆέǶÓωOǝħüӚ˱ĬͷʃѭЈʴǡ',
                'Ɯ¶˽ӇɓАƇšòˇÅŁ*ěƂ0ԏ\x96±ʋ',
                '΄ŧɐҐ˼ʕϧɎӴİþяʈЇ',
                'ȾіӀ',
                'ԬʅĬҘЬ^ѫµ*ǖşԘ',
            ],
            'comment': 'ÄŹˇțԊȁʋǢ˞Όň˕ŜͲþƺdѤȕaԔXγԋƿΊ\x84ϞɉÝ',
            'event': {
                'target_id': 'ȾȔōEǥk˶ȤǇŏɗmˇƫҿͿɉɤĎʊϸѝʎŨϮį¸ϴάБ',
                'parameters': [
                    {
                            'key': 'ϹКӬ˄',
                            'value': 'ǤwʄƭϑҨҚ-Ǉˀŕʷ˾уԩĮ\x88ŐÉЩƯȟεÝʬŋԔ΄ćĲ',
                        },
                    {
                            'key': 'ӔϖΟЍÏ\x96!χUş=ԏƒҙϾԖĳԍʡζѭҎҦɼȼ\x81ҽŃԬ˷',
                            'value': 'ԛ˽`ǝӽСĶa\x99\x8cǨɔĺӔǢȴpԕ\x8eÖ6|ǹϥÜÛ\x98ʲϦϑ',
                        },
                    {
                            'key': 'ƟõʍԦǓӒɑҦɢӳ-ԍůŰı˰ѧ\x82шoƸАфѝЇ§ҦЫůƊ',
                            'value': '¶ѠŵǜÚΖŹԧψћτΤ\u03a2˸ʻƳʓхǿŃѕʥĻͰǘ˻ȔȻϔϤ',
                        },
                    {
                            'key': 'əӹɘѴʠԭ˷пë\x9dnЏ˹\x93ʡǅöʧ\x89Ϙˁы˝ҿӐȓˤѼâͱ',
                            'value': '˓ԜƄȰȯſ®ЄέıιǬζɱňѾПȻ˫ʝЉ҇ҟˢŹԀҁÈ Ӫ',
                        },
                    {
                            'key': 'ɧǫӫɆρ±¿Ŕʝȋ$ΎũфδěŨђεƍȄМŤѐǉшќˇÌ¤',
                            'value': 'Ϛ\x82ȦJķ˖Ɇɻɀ˥ÊєʋԓЕUɦŴӓʆ"ɦΈƕ·\x91чIӫА',
                        },
                    {
                            'key': 'öϨΠŷԁɝːƈʫδф¥ԟɕȹήʽѳΑʻ˷ѭȫμӽϪǼ˶ю´',
                            'value': 'ӼɎѫƔˋǹë\x86ΌȑćBӀѥϠcϼ²ʸǍьŌ|ԍȄΠǥ}БE',
                        },
                    {
                            'key': 'ˏķ\x80ɏzŊĤԆҚӻъ˦¶ɨќΠͻХƎǶ«ʣԛÏԘҜɯŭ¡K',
                            'value': 'ςѭѣҟГѬЅĤǋлǟĳ tĤȏǏƪƭƝщɖҠ˝ȥїʆԮоӇ',
                        },
                    {
                            'key': 'ƄҡāÝԉɂ^\x99ҥŪȖѾҒͷ˵ȏǆϕԝʝÐԌƾűűΈѣ˨Ҙɸ',
                            'value': 'ҙıƃȘÀ5Αέà\x91©\x82лЌŃϵʧǚŭ*ΘЖІ˒ϘѩǂԆБĭ',
                        },
                    {
                            'key': '˫*В&\x8eΤ\x80ėԐÚɩѫǙwԖԞʼǱ',
                            'value': 'ϵˋ\x87*˜ȜL{ώɖȾфø\x80ЕȤÔȑLМєϻļľϿȁǏˑХ2',
                        },
                    {
                            'key': 'фy˼ĉμ·ÎSyӜтӜόȵЁǇФϿVʏԨ\x84îǀ6ȋǵ?Ņş',
                            'value': '˱ВXÝϿƧѝʺӒΩʃϿӽǮԡŵɾvɰҫʞʐĬҤЎЛǃȿҪҚ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                '΄',
            ],

            'event': {
                'target_id': 'НИŖӻΫ',
                'parameters': [
                ],
            },

        },
    ),
]


class BoundKeyRemoveEventTest(unittest.TestCase):
    """
    Tests for BoundKeyRemoveEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEY_REMOVE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRemoveEvent.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEY_REMOVE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRemoveEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEY_REMOVE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='BoundKeyRemoveEvent'),
            ),

        ),
    ),

]


BOUND_KEY_REMOVE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keys': [
                'әҌАҶΪʐΪxơķʮϦʙРƇ',
                'ʍ͵ǆǪԔǻȜƆdʧԉʯҥ',
                '˛ԎԢưvǼԢҴĮҐ',
                'Ό\u0381ƜơĒҟλμÜЇͲĢԓɭШƖϠˁɞВʎѢԨ\x84Л¥¨˖Ŵț',
                '˹ŪŦϙӆεlĀζɚҾ\u03a2ɫǃ/ȠcҾӖɜӖűˢòјǄѐϗƧл',
                'ˁ\\Qԃ\x9dпΧ',
                'sAƶӼԒ',
                'ɡȔδȢь#šӥԩԊγҭǸӚʻЃҶ',
                'şΑˮ;υņˑѾ\x92˛ųŜȶΕɡҵɾƲыËҁ\u03a2ÎȫɇYʦѳ0',
                'ɮЗϦˋζ<Ʊ#ȝхҤ`ҤřӭчXϕνɫř%Iŗǲ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                '˪',
            ],

        },
    ),
]


class EventParameterDescriptionTest(unittest.TestCase):
    """
    Tests for EventParameterDescription
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENT_PARAMETER_DESCRIPTION_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.EventParameterDescription.parse_data(test_data)
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
        for test_name, test_data in EVENT_PARAMETER_DESCRIPTION_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.EventParameterDescription.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENT_PARAMETER_DESCRIPTION_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='key', name='EventParameterDescription'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='EventParameterDescription'),
            ),

        ),
    ),

]


EVENT_PARAMETER_DESCRIPTION_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'key': 'ƓӆҎƱęɅȰеӅƔοԑӺф',
            'description': 'Ѳȍʝ4bӀʖĦ;Ԥ ƦļǙǘѻőϥτǗʑǾJő˺ҽĶǷĊι',
            'default_value': 'ԥŏĂЬҚΕɜȭĬЪц5ѡƆɷæȺș(ȼɞӜƻʈÑǱӛϰʝƁ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': '\x82',

            'description': '',

        },
    ),
]


class ExtensionEventRegisterEventTest(unittest.TestCase):
    """
    Tests for ExtensionEventRegisterEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_EVENT_REGISTER_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventRegisterEvent.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_EVENT_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventRegisterEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_EVENT_REGISTER_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='ExtensionEventRegisterEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='ExtensionEventRegisterEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='parameters', name='ExtensionEventRegisterEvent'),
            ),

        ),
    ),

]


EXTENSION_EVENT_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ӁGŨ#à˰ϩʈ¨Ѷ%Ѳ˞ŶÃԖΘ˃ѡӝ;\x80ƀϚʇ˟ǧȣѱY',
            'description': 'ԒӍÆǩÕѯѴ}ZёѢĿЬКϑƏӿǐÄӀкŜȐțǸʡȅˤѕ\x9a',
            'target_id': 'ãιµыЉΒĜ',
            'parameters': [
                {
                    'key': 'ԃΏ~ҾʢÏʩαʁóƈʦ\x9d˭ǁ§ыǚʃʚĔӄÇğx±˰ѮҪȺ',
                    'description': 'ʎԀԫĨȲľю\x8fϼƻȥÔС˾ҟǚӀēźЂƍԤæŘÊ¹΅ґƥʃ',
                    'default_value': 'Ԇɫʳ\x97ѬȠƀaυsʭzxϤǃӵƗ\x9bȖɹΪZ˻ӓƎ˃ŏzƀр',
                },
                {
                    'key': 'ɺǤȼαҨdčJӂӑƞӲ˧ҎʍѰЩӉѪąǪъã^þƮϺȰͺȾ',
                    'description': '\x98ΜuǗĄϭ\x8bƟȝФƌàǃӇμӈr»ÌΈɇԆŏŜÈŰѱŖжӬ',
                    'default_value': 'ӞȤřəӇԜșʻԓGɾƩƋƗ˄ϲш%эŅϧǥʨŞÿʕɋєȌô',
                },
                {
                    'key': 'Ȁ˒ɦʳ˳ƨ\x8fΤԡƙŞȖԞǚeŦӟǡԔĊøΙłцßӄ\x96ЪӿԢ',
                    'description': 'ΠӁчʟƳϹĂiͺϧƀҚӁӾҐ|ů˸ԚʡƢěȫЂѕ}ҟʹѫя',
                    'default_value': '˙ǾϚԧ˷ϦʋΏΎԞȕϟ¤ű˩şγԩ¿¹ҏȿԈʐӣʠҰ˞ϙϠ',
                },
                {
                    'key': 'ҴȠɸƮ\x8cҷɿ@˴ҏȔǧë4ɉġ\x83ҎǐϚȚЋԠьɰÀϽcĎû',
                    'description': 'BʽÖȿ%ЙşgÇ£\x9fØȵțʯ3ЧōZăˣȤĽbҰԏρ£ĞϽ',
                    'default_value': '\xa0˫ŹԥĺȮӤƉȳӵċŷƞԚéҤʃӽȬӑĵ\u0382ʵɞϺϚҊùŤG',
                },
                {
                    'key': 'ʮΡ8ͽɫ҂ʴƃŊ\x82ҜѨ',
                    'description': 'ӈġ˅ǊӒĜͱ6ʮΝɪkƧƭʾє;Ͻѓ¶еΈӃǑJǸe\x9bϮʇ',
                    'default_value': 'ʦʳОͱ-ϫˆ]"ǋр˾έЍ©ԂѷəȌÀǀ$ϴ҃ϭ\u0380ʂƅËʍ',
                },
                {
                    'key': 'ΖχϳɖǊї5϶ÇɎɴѕ˯ʭňТʶцɼ\u0379ϐŀĉЧÈʥǧ@Ĕ¯',
                    'description': 'әýϹҼ¤ɁτәēɾƎӛʼӇãϫŜϮƩҊԔѶшǣͰӵʲύ˽ϲ',
                    'default_value': 'θԈд˅BЭBҗīqЎſlǨЇĤeѴôû˄ԂвЄΠɖͻлZʩ',
                },
                {
                    'key': '-ǏΏɯwӇʤɾφĨƗѲγӖжǾЫˉĊіįԩÙԌƹζаҷτa',
                    'description': 'ɺќѯ˃ʲϙĐÖ\x99ǩȴΒˏ.˺ÞɟŏfſÜÛҳґǺƓȕΓɵŃ',
                    'default_value': 'ğƩɫ=ČàķΦǲҗȧҦˉΧǴƻʡİx˹Ĳàɾԝɰ~żOĘȲ',
                },
                {
                    'key': 'əǬҌғ³\x9eŜҨɅƢҮӇ˦ΌѧӅφɘЄǺˋƶʦ\x89ĝʒkԥӽȕ',
                    'description': 'ʼɡŧ͵έŘēÐф\xadrʪȧӏƇȐP\x9cͲΦɳǨĢ_ӏɈвΟԙқ',
                    'default_value': 'Ӟ˅³ɔͳʧoŋ˺ҜǉáŨŅT\x96ǥг®ȂĘϗƥ®ҥČΐșЁҀ',
                },
                {
                    'key': 'ɥƝīӦӈҔýœԠþϥ¼Ļǔѯθɴũŏ\xa0ÚɞӷӰЮäë˓ĦǏ',
                    'description': 'ЙĊÙЯϦloϪ·ίZǨ˫ӰʋѹřԐìƄεԇȰ\x83ίǄώçŷϖ',
                    'default_value': 'Ҵ҄[5у˚ҪԬ\xadʣΗаÑÊѭԈӴǢȯTгƛǊľӰԆùkɂԑ',
                },
                {
                    'key': 'ηʛϙˎ}ɹǶǱɩЋěơԛюϦʺЏдƯԡњ˼\x92ƥшʥӡүƗѳ',
                    'description': "ó˵ԌτĶѵşϽÐήͳïaеǎтюԜȢªЧσϥNů'ƽɚӤС",
                    'default_value': 'ʠǵśĸƯЃȉЌʈЈ\x8fЗӷ0ЇļѾєϚȥԏҘ˓ӠǰƓԎč҄I',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ө\\ҙ',

            'target_id': 'ƣɊӖǑØ',

            'parameters': [
            ],

        },
    ),
]


class HotkeyFiredEventTest(unittest.TestCase):
    """
    Tests for HotkeyFiredEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in HOTKEY_FIRED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.HotkeyFiredEvent.parse_data(test_data)
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
        for test_name, test_data in HOTKEY_FIRED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.HotkeyFiredEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


HOTKEY_FIRED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='event', name='HotkeyFiredEvent'),
            ),

        ),
    ),

]


HOTKEY_FIRED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event': {
                'target_id': 'ʘоΕͶ\x92ғӢþƫΉŹ¢ʆ\u0379ЈͲSƣǒȌHȜʟƄϷȠ\x81ҭѱȑ',
                'parameters': [
                    {
                            'key': 'ѰУΡŔƑÈĈǗ҆¸Ғ\x9dԋƇʻòĪƈ1ʲΎ\u0383ώђĞǐΘԬМɻ',
                            'value': 'э>ĄɜǱĚͰϝˏҕȐ\x9c\x91ĞσЫԂίŅ\u0382.<ѯ\u0380ɜѕԐкžĖ',
                        },
                    {
                            'key': '˴',
                            'value': 'Ȣ^ʏϿͺǯеʥӝə\u0382Ԟ˯Ũ΄5´ӤɇĻɹҨЪћϬûЏșʀϚ',
                        },
                    {
                            'key': 'Ʉ«ʜɕүŀıƌóɌћΠǦѩщȃԍɧ˹ˌňӶϯơáӉҔ҈"ɱ',
                            'value': 'Шj˱ϭDǛLӝіóƯǼ\x98ӪЦƞǗȞʪmљҏt+ѳ˒ʋȯϙǇ',
                        },
                    {
                            'key': 'ƃtЄʺʹΛҌ˛ɜɢфςņƳÉҳђ˗ұѠѕ˱ºРɆ\xadĊ\x81ˏǁ',
                            'value': 'ѡ͵ņԉÌňýӴƊ\x8bѹ˕оDȍ˪үƒјѣªƻйӾȣɢҡӹǵҐ',
                        },
                    {
                            'key': 'βǈɌ˟ĎĄ¸ƇÊU˾ƭΕ˷ў®ƚ\u0378ĸͳԖӻҀ¦ͷ\x9dК"¾Ǥ',
                            'value': 'өǤǣəőΜǗÒҺʜѓɋ\u0380ѸƐԧǃͶƂÄ§;ĲƞãрDƏɤǻ',
                        },
                    {
                            'key': '¾ѯΕң\x8d$\x84ĦǭɆĞŖĲ¤þҤӳйϒ§\x98ϩ½F\x99ǀÂ˟˼Ң',
                            'value': 'ЛʥQуΝӦ;ǿϫ}ɌʣíɞςȲӁȚiâͰЍǘӿȘyεƥыԞ',
                        },
                    {
                            'key': 'ѓϋ;˨Ѕϼ\u0381ҪƟäˤ8ƈ҃ǻv˱AːҦ˱ŝſ;ĐіǍξΏȾ',
                            'value': 'ӥa¢øΊÖ\x94ʎJҺК´ЦŜŗ\x92ɩъԨʏЍѯřődšȖɴˤȯ',
                        },
                    {
                            'key': 'ɇϹԕýξƐǰζΠÈ\x84Ҁӽʅκªһ\u0378ԍəԭǇЁғɏ¢ϢȹϏӽ',
                            'value': 'ůԖ¯ǮɆ«ƫѷƭԠɲӗЍŒѩɏϙƹïМȏǈмĵӱˣ·čӘ\x81',
                        },
                    {
                            'key': 'PʋѶԉϋѢϘІԦѸÆȼƒϟс\'ɏҤǧȺƓƴñЋΚ˯ЛȄ"ʬ',
                            'value': 'ԐľÌƘͽηҹJоϣˉÜȑŪӬ¶ɵ҉ǽҝpˡ}ҮîЎGzҳĴ',
                        },
                    {
                            'key': 'ǌƂӢûҪȪŸԌĴžǶƈԦ\x85ӼŝυҩƴŪα6ϏĂɥŊӬÞ<Ū',
                            'value': 'ȉԛƳƓȩƋɑ#ϙŒ\u0378ȒҹĹӊ&ѫýÌÖԟȘį\x9bǿϧϷҗβǄ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'вöˏ˧Ҿ',
                'parameters': [
                ],
            },

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
                'ѩůԩкʋ',
                'ȌԛʬʦˤĔɿȘÿ\u0383ҪϿҔ',
                'Yǋ˞ϦɶԫЕȳ',
                'ʪǜȺʰǦςϢɽȺϢʵ\x93ʀ±ŧԓȮV\x8a\xa0Ȉα&ԭŶʥϤԥÖd',
                'Ɇӷ˛iϼďŮҍϙă˴ҀӱgȷѣϘѽ',
                'Ϗ҆ϺʉǾȣ',
                'UƾϑʛЦϾāʶƔҞѾāȻԞϑpҍΜ',
                'ӌӴƗєԗύɊ¨Ș',
                'ɒΣ¢ıôȖҒҲƤϧǗǐҪК¾Ŕн',
                'ЀRƉςƢÏҭҥǱ\x8dϻ҇iϜ¤ɇŁ',
            ],
            'event': {
                'target_id': 'ǟԟȲλˡƂɘӏ\x8bʾĘDӧŲѡӹ£ǎЯѯɸíáŉЈχ˟ːӽˮ',
                'parameters': [
                    {
                            'key': 'ώĨБ˰Л\x97ˋňƹΗǥͷӃ·ԅԬʡЮǊУѢː˥?:ҥҖѶïĄ',
                            'value': 'Ĥžǅ;ɤΔѮǺǶҀ\x8bˤɎѬĔöŸ\x8cѢėoʠŪǠ¼ɪˣĊԤѩ',
                        },
                    {
                            'key': 'ԎϣʕɌ¢В˺ицԮԐưĤȢϢÍ˪;\u0381Ҕӱ\x89ΗѐtӚϋʗGƙ',
                            'value': 'ŷ¶\x80ǏĹά˼ϣʗƬā\x81ͳ˰ƇˮϢϣȻʢĀÞˀϝǱюɩʦӂˊ',
                        },
                    {
                            'key': '|үǑҖϮЊФǙƋγÂάǗϥѦҎ\x94ҚțAϴɵƞȏȊòЌȒѴǿ',
                            'value': 'ë¯ȧÙ˖îǝəӶÕҼϋȎϫĠƪŒœ˯ϝɞ\u0378ŒѕԋĳÄӆīи',
                        },
                    {
                            'key': '\x9aҒ\x81ɖĢӝɬʣúȄͶȿmτҖԁƇÕ»ǡĆɘщA¸Ұʿįųɗ',
                            'value': 'àƧЯ¸ŞқԂÚŢԩѱǤǅƅυΥØɒ\u038bԫòҲǚȌΚƑǕ҅ѫ\x9a',
                        },
                    {
                            'key': "'йǀР˵ƖΝҪ$ҵѱҗ*Њв\x96ėҀEQϺĄĊїǐϥҗ\u038bϙſ",
                            'value': 'ɯȸZŢĔϔҭé˝ΜϒÈќ˗ӛČкѳʭǱҺǏЏȚĆΰ·Ňԏ\x9b',
                        },
                    {
                            'key': 'ΛǄʗҡOӻ˴ɛæѣΕ\x9d˪ЕʴҔ˸ҭ¯ԛԫШыðӽɺ\\Ʌә\xa0',
                            'value': 'ǂOȴЧʐϨɵρɸşʛƷáԀϾӭǪӠӹϏФˠΈɳӸϠԛӳλ˸',
                        },
                    {
                            'key': 'ԍƓʤԬͲϽγѢƌĳɫüɼɟͳțļюæУ˒гΦϼƧҏǡ˱Ϋª',
                            'value': 'ԣǞśĸӒɀčРȲηԌѵЛʐ\x83ŵ˄ЮȤϼ\xa0ġȂȌÂ˛Ԧwhυ',
                        },
                    {
                            'key': 'Õ҈ĘΟɨ$ƄŬµŧϛǙҎŚ0лσ˯;˓Ⱥǂ,ŲӘ¯š҃Ԑɩ',
                            'value': '҃â5ϛyԘϾĊ/Ȗϝɕͽǔóκ¶\x9aǃҗЬ\x8dªǖGԃ2ǿĺĭ',
                        },
                    {
                            'key': 'иѮ\x8eӴŒԃИ§ʣπƀɋ˓ǖĴäъӤϗàόѭѣͶνЍҟХҨɩ',
                            'value': 'ҌьηӞĶӹɐäʺѢƃ\x9aԋыΎмȚѷ;ɾяʬħɳ˥ŕȧ˸ϟǖ',
                        },
                    {
                            'key': 'ћǦԁїӬIǱ¾īϺŝ˛ͼҭ%ŬδӪ`Ġ7ɶ¦҄ΖʆˡДʓ',
                            'value': 'ʂҏɘҁȯ#ϤͿ˹ÐΎбš\u038dўɔ£ԂҩҍҸϛ(ŅϙԆˈӢҭǨ',
                        },
                ],
            },
            'comment': 'ȈɂԑҴωȰƸϜӤ$ǷӇϬǖő˲ϵǨӉșʹ΅ˤςǻɓ]ɺØ\x91',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ý',
            ],

            'event': {
                'target_id': 'ǜЮǝҀđ',
                'parameters': [
                ],
            },

        },
    ),
]


class BoundKeysStateTest(unittest.TestCase):
    """
    Tests for BoundKeysState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEYS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeysState.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEYS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeysState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEYS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sequence_type', name='BoundKeysState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='master_sequence', name='BoundKeysState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='bindings', name='BoundKeysState'),
            ),

        ),
    ),

]


BOUND_KEYS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sequence_type': 'sequence',
            'master_sequence': [
                '\u0380ԝ\x9f',
                'ЀʑɭOѷƵ˞ľ#ҡ¨\x9c˰ōǯӕ',
                'žĤӿ7èсδӐƂґźǘUрȫеσǤơ',
            ],
            'bindings': [
                {
                    'keys': [
                            'ÌɢčӸǶȿǈ',
                            'ʅǓȺХΐɳÙοŲĽ҂оȉɽ©ȅÊϭд˲Њǜ',
                            'ȗŶЏѵΒń¬ƾRɫ\x9cүϰǕǇ˂À`',
                            '¯˲јöΩɑ',
                            'dAВϹ',
                            'ѪiXГ\x82ԖęԫҍϬǗ˚\x81ҽŶNĎΆȕԋʯƿƏӝƱͶ\x88Δ',
                            'ˆSǁСӄӼаžЙԀ3ŇҞňĝΞʛêʐÝȔƬЎʉXΏѼĠȮ',
                            'ħªαɴԐ²ģԫǔхќƸǾ',
                            'ĺǫʙӵƱÆԟËɎɛĖ[ǲ˽¨ѫӴ',
                            'ʛ\x9eʇȖʘÍȏ¸ɀƭδ1нȑ',
                        ],
                    'event': {
                            'target_id': '˴ʭƑѺΟώˆÛ&ҊņØ|ɾĵԋƿńʝnźȏΔѣü¦Ǘʄƀχ',
                            'parameters': [
                                        {
                                                        'key': 'И¬\u0381ȤΊŔǻ)ϋϫxԗ=Þ҇Ɓӽ',
                                                        'value': 'đʞЏӍǙΌ+§ǞΓʀ@ǅħϑ˽σʄӘȬԣьҠśāʦŅϩͷʉ',
                                                    },
                                        {
                                                        'key': '#ȎǘϵǁÓǪЍԢ\u038dԪ=˱Ѓʋѱѵ¿ҶʬǽӖĲ©ϬĭΒiŧĲ',
                                                        'value': '˛АǟӾ\x9eҼƧ\u0381ԇĈcǈѪʧ\x8a¦u˻ƭХʿâИĻɉҢÑҲūѓ',
                                                    },
                                        {
                                                        'key': 'ҧ|¬υʾĘÃpǇĪҌƐǀ¤RϼѐЅ"éϋΣ˛ǯМ҉ӝóʹҢ',
                                                        'value': '˰ƛƉ`ФíĚ\x81ΉmľĴ\u0382ŐĂȎáφËɶԤƭ°ɴȣ˶l¿ɎЗ',
                                                    },
                                        {
                                                        'key': 'ɏΙΐǣԡʹ¾ҫхɚҺгȪΠњɼɖ҃˘ƨ˲ˣҵBҘϮГȨ',
                                                        'value': 'εΰƇƸƆʾɺǛ˨ȌřEǿÄӻΜĸàœɯΜʹ¶ңǳʶŦ͵ӊХ',
                                                    },
                                        {
                                                        'key': 'ԨÍΧpǼŉѢΧūӢЃǮ÷ɫγƭėөßϭƞͱБԣǸϷ\x90Ԡȷσ',
                                                        'value': "Æϑ[ýгưѴÃǅ\x85ϖdƢЦɁƹĦҒ'όϱǯϽ§Ѩƻ=Dʈæ",
                                                    },
                                        {
                                                        'key': 'γȄƳɎћȕϵĎǴ',
                                                        'value': 'ϢԧʀāȎ\x9cȭ˂ȯʈҰԊȯЊѤˢý˩\x83P˭vħʻ\\Ѷđ҂ϔW',
                                                    },
                                        {
                                                        'key': 'Ɏó',
                                                        'value': '¶мӺǂƠĨΈŮȯŠԢǑʴıĶēőұ\x93ľϤEҝӮaΒŚҏɍυ',
                                                    },
                                        {
                                                        'key': '΄¹źʎІяŋОӖįɸˊ>φnïͼȩѧӇѭŤɏƒЋĳZԩɍ\x8f',
                                                        'value': 'Шʖ\x84ҴơƣŃă҅ɤʪ\u0380ƬǴƈ\x86ʔǊǒӏҿϰΩàԛʮʀӚũ#',
                                                    },
                                        {
                                                        'key': 'ʴϛ҅ԫŘı҃Ď£ӢϘμʺӹʲǆ¿\x83˩Ѫ˪іΜ҄ǱԝЃÑƆΞ',
                                                        'value': 'ȺҀˠȖ{ӘðʮΚȒ¢йӾȯƶņT"˽ςЀˉͳȰƟǝɠɗȑņ',
                                                    },
                                        {
                                                        'key': 'ǚȼԩϱɋÑɦǆӠϦ\x90ÞđƎƾĺ',
                                                        'value': 'ƊѺЗѫĒ\x90ǁˢ˄·ʋĽŕƖnɐŘZϜĶʙ¿ɔʳ˩¢ƂȞĶț',
                                                    },
                                    ],
                        },
                    'comment': 'ӀǘǰҦчÓΛȤШ\xa0į\u038dȈ˒ŊΙґɅÅͻ\x9cʨˢԪιҺȳƁʌΛ',
                },
                {
                    'keys': [
                            '˟Ȳ˟ùшȶĞͱˁӓχͺǅ3ĲɱлеϒǣȶқƶŲ}ѱ',
                            "ÇǾoʠǲԔԦȴě'Ĕ4ːϗEĩ˂čZŔϬ˸ѩ¶ɣ",
                            'ӑ¯˫ѬӸύҽԡҙǸÍԃ˒',
                            'ҕʷv}ǔȣы;ζʵӉ\x93ĐӞ',
                            'ĀŐϺ8ˌ˙ÊŞŭϼʫȬǖѲиΜӵΌҲ\x7fåˠ˖ǳ˂Є',
                            '-тȝ\x93ʼŝ\xadĥȡÀңԢ˂ɧ\x89ǤӉʘŹÅȤψҫȓЈηʢŨ',
                            'сҟ*ɃǀμɈԃłϺ',
                            'RƵ¥˘ƐǚπƯǥӏҍȷ҆ҁСţЇǞ˥ñ˒ԑɳ',
                            'ԤЯӘÉϥѕȹņӼ^˴ԧ¦ˇŧ\x86έeǊȷɠԚ',
                            '\x85\x8bӯώϐˈǱɟÙƨbŞȓВӣiʗ',
                        ],
                    'event': {
                            'target_id': 'ҚψϗȶŪӀ5?ɦȔœԖ\x86ϱ\x91ȧ\x9aw\x9fǂѩɋýѩ˦ůԔяɚJ',
                            'parameters': [
                                        {
                                                        'key': 'Ѵ7ϦԦ˞ϡ-ȨЋŶ\u038bƐяӡόĹ×Ζԏʺğ«ŎѷҎ{Ρĥˤǲ',
                                                        'value': 'ƞȐɮӥӈҰɪÏĐҜǒɗΘϲφʓ÷\x8bΖſîԦĕϪԒ&ӑ˷Ζ"',
                                                    },
                                        {
                                                        'key': '°ҽчŮǁϖ˨ōԌӴ§\x85ʮŅ¨W¾ʴΐҏťњωĕΊǪѝҁ҇#',
                                                        'value': 'ұΊͶėÌЭȯϻˇԂ˾Ӝǆȣ³ȇãȧŃȹŃǭǮʓ\x82ˢ%ǤƆϴ',
                                                    },
                                        {
                                                        'key': 'ЖƷͿԀγXϔâ¾=ǧn',
                                                        'value': 'ċA˳҅ČСǀԠѫұ\u038dЍƨԇĹɣвɎҠѧϴĿƏçӾԖΥǰԠŊ',
                                                    },
                                        {
                                                        'key': 'ҒǠЮЭĊ\x80˂ЄӡƻɣГũѡʦĸоѧΏɵΔƾßɶ˂ӈӜӊŷ\x92',
                                                        'value': 'uϗƧјωѬɝһlҡЦdʾҬғ\x98ОǟΞÇǧøΦͼύҦǞó˵\u0379',
                                                    },
                                        {
                                                        'key': 'ʁś',
                                                        'value': 'ÑƠϏ˦˩ͿǩϺŗΞ˚\x8cǶXҌԧЀłõŀЕöԃ\x84üʰǥ͵Ѳѱ',
                                                    },
                                        {
                                                        'key': 'ʠʁɎǥεѳ.ͿĪɥɩҰ°НΘƚêʃћǴЈǸȼԮǚƻҙϲôŨ',
                                                        'value': '˘ԡyϩsͺμƁʁӈҎàԋѾԆԕǌԪʯϗɓӛХ\x82ԇ˗ԊȰϰÁ',
                                                    },
                                        {
                                                        'key': 'ȴüɢΔȢ³҈Üɨʝ',
                                                        'value': 'ϱ»˻ђŉˎȋ9¨οɌʐņȡɽʳǣˋ\x9b˪ʂʦХϟĐȭǌǵҙȦ',
                                                    },
                                        {
                                                        'key': 'Ө{ſӹYâ҈ԙ',
                                                        'value': 'ȺƳǓԬѱ¡ȈʘΞŒӻԢѮǵԓμєêǷǚÇЉƴΦȐú҂ųǒƝ',
                                                    },
                                    ],
                        },
                    'comment': 'ɓӖҲMˍ¶АKҨƑəšȡӄНҭfїðƐʴĸĸʠɣǛϫӻǬķ',
                },
                {
                    'keys': [
                            'Ⱦʛ/ɎņαЬŌҟԆϮѩȈӷϽςӴ{ǧίжΫ϶',
                            '\x92ѯėǵXвɿɠJө¹IϠƶƖ',
                            '\x9dīǡґȡ»ȔӠ\x86ЎӨАЪ˜ԩτLŔ[',
                            'ЂӄӪƐÄȊƭфƝЀ',
                            ' CԨſ',
                            'πʔѠĩlʴɸȨ\x84ЯҋƓǿж˘Ҿ',
                            'ˆʵιĴӰ\x95ÜǾ҂#pľΙɀ{ŚƖǲΠïҬǦ˺ɺ',
                            'Ԕźԟ˘ԮϜϤĕ\x93±ΏДҀģΤAǄtСϒ\x9aºӇ҆Ƴò×Ε',
                            'ԁή҂΅ƔąEɘТȅɨŪ#ϼуɐШӊˆ',
                            'Ō\x93сʫƝκĥϖǺԒԛҜͷÐ',
                        ],
                    'event': {
                            'target_id': 'ϕ{ǞȊĳϵ\x91џŕѡЏΈʡǸĚιşӦħ5Ƚ~ƈÅрφRǵɃή',
                            'parameters': [
                                        {
                                                        'key': 'ςǅρĚѤ˗ƣÉбӡϳɎɧͱǷѡ\x98ǣ#ɽŌѩӦρϏύ\x88ťÙШ',
                                                        'value': 'οΈҝ9ρ҂ĥ˭Ȋ\x9aı\u0380ǜ\x94ɽΘ˛ɑϬťјƂƀШԜɒӄņȨг',
                                                    },
                                        {
                                                        'key': 'ҝЙǢƸʍӽΚҤԔŁǂԁ҆Gҙ˸ǄXѽӕӿӓʅΔƗɽƸƞʡʓ',
                                                        'value': 'ĻˣґŲȬѦ˴Ѿфɋɺԣτ0Ǉӳrʼƀdƒ˺ÒЬ¸Πτȶ\x81Ζ',
                                                    },
                                        {
                                                        'key': 'ħžЃ\x80Ϯ&Ĩɋɼĸ¤ͷÛμÑŐɥϥԧҎέƁчǉŐȦůӅ]Ѳ',
                                                        'value': 'ËBѣіǝ¥ʀϷ˱˗ȿɞĘɿѬɢǱȟ˩ɄĜùQiɂ)ѫɂӃҨ',
                                                    },
                                        {
                                                        'key': '˂ΡĐɫӽњԮхƚϔөӂ\xadbɛЂђʹȔГƧ9ÄǪϱǗǦӶӳҌ',
                                                        'value': '»wuįǢʸбѳȩǒѨĚţҴԈƙЙÀ˗ʍÇυʶшǾśΉXŻҦ',
                                                    },
                                        {
                                                        'key': 'ЗањΧҧĀЎúτ\u0380џϸѐҥ˝\x8aʸ˴ЙÒŽ\u0380ѕҰζlƨˑ˚ţ',
                                                        'value': 'õҴÉҜΓɠɎȑʽ#ϒЫͿ;ШЋʪќԀȢɖЍϏԔϖǕԗʆėÀ',
                                                    },
                                        {
                                                        'key': 'фΡĉԡǯɻ˭Ϫľ\x94ŧˌϮʞмƦÛ!ԇɽ˄ĥθƨȋԆˎ˕/ϟ',
                                                        'value': 'ҕųѓĈȠôbнȸԧÆХӘʤʍҰıȜϫìӱŌʑԏ\x9bCĚĚ ¬',
                                                    },
                                        {
                                                        'key': 'Ǖóҵ?ӛɩʀŔȊ¡ɶǫʈǖŀϚΘѬ\u03a2ѯКѯwXńŕ,°ȧp',
                                                        'value': 'ҫ9ѝЙӬƎЌgӶϙqǈӡвƾȠҸVˀϳʀɃΠŖûdŪŦϯо',
                                                    },
                                        {
                                                        'key': 'һÊoӦƳА˓ǩʬһ',
                                                        'value': 'ĥʅȅӴɥѥǙŵŸяðȳ\x80ͻӞ8Ρʐԉ˯ӛиӒfѢԏMҭƀҫ',
                                                    },
                                        {
                                                        'key': 'ЏàƼгʹ@юºϒ¢іșĠƃ¾ҦРӀÎόʍĄ˘ǪҎôƉɇ1Ќ',
                                                        'value': 'ɰҕϞ\x92Ҁ˅АȲˀǂѕǻˇ\x89пϥɴŤȣϻφҊǣľӷϧ\x93ƀ\x89Ǫ',
                                                    },
                                        {
                                                        'key': '\u0382iPΕ#ŠԨφéīčɕҫˈƇӑѤΉѷУň˻ψ˹ŉԢѿNӘɴ',
                                                        'value': '7\x85ůǤςƞ˰ѲþI{;ÉӵƺӁp\xad¥0ȡΟыфΧκȥĊѼ£',
                                                    },
                                    ],
                        },
                    'comment': 'ʨʴӫγɀľ]ʪ˂ҟѵϟѺѬʦƁҕӺʒ[,Έƽѧʏԟ˦êЬ˫',
                },
                {
                    'keys': [
                            'А\u0380]ćΐΰӨĵ·ҲӻȠҷԭǝĳѬ΅ɭíҋǂȈɷ\u0382Æ',
                            'ŞˊҕˊκʤҡʭѬ®ƬRǇѓƏҁіÓƂӜӺ',
                            'ʅxƀǗϚ',
                            'ĳҔ҅Čɞϧ±ӇÔȢ\x92ȧéγћҕɞɺàɠӄԒЏ˒õ',
                            'ϸИϙ',
                            'АҧŉͱҚʯȞňĎЁґǿҔǮƉ',
                            'ѬƌәΛÀƾҐ\x7fɽĐưӕ˺\x97ǹ¡Ů',
                            'ɚǣlˌõʖǘuϿϙÈʽԝƱɅɧœϵǘɡʱdѢϧȑ¢\x9f',
                        ],
                    'event': {
                            'target_id': '˛"ξŹϵО˺1ζӹҚӶΆˇÉʭӣ\x89\x87<В˻˅ң҈ʵgJΒϲ',
                            'parameters': [
                                        {
                                                        'key': 'ɕɧȮГĈɫÉТńʒцϏЃШǂÜАʖёĵʌ˷\x91Ŀӧ£Ƕ˼A¤',
                                                        'value': 'ȐЫŬȥԓͷřʥǌӝ$ÿфΝϼåц"ӑΆ\x80ɌӅϏҫþð˪ʪ]',
                                                    },
                                        {
                                                        'key': 'Ǫ\x81ЊΜΐԗӗӯćƧŹѐЉȀŖ',
                                                        'value': 'ËQŢŦӫԙγϢѸ˭ť˘Ϗ˜ΓXƳØɛҶ\x9aƼ\x8dƄϫӉԡīzƉ',
                                                    },
                                        {
                                                        'key': 'ƖŜUȬɚԡǌąќłǅˇӤ˗\u0381ɏƏ҇ʓΐŤʢǡύСҚЗĊԦ҈',
                                                        'value': 'ĎҝơŊГ˖əǥɫȾϐΝĹҥԔʰϖNȬ҂\x85§ĿϛMԧхӔɿĢ',
                                                    },
                                        {
                                                        'key': 'Ͳ½˼&ʘәŧʧƗƬЩġíɛ\u038dԁƤ4\x82ΩЩǻĺƏbƓ˫ĭrӅ',
                                                        'value': 'Ͼ¸ĔÄЍɌÀӎλòоɨŴrȋɘ˓ȞΝΔ}Ǿ˛ȶг[ƿɞҌѸ',
                                                    },
                                        {
                                                        'key': 'ɞѣǆÛһ[ӱ΅ϘҎEȸƵΜϚŸǼЯɟ\x89ĀĀϭҭÖӼ҆Ҋεÿ',
                                                        'value': 'ǵͰʽƦ&фʱӠΒ˖ϴõÐԋBȃȅɻˢͱпĝтǡԧϊËĊĝʟ',
                                                    },
                                        {
                                                        'key': '˺Q҆ƊŜğr',
                                                        'value': 'ҧҳàϤΔĮԌɸǸЩ˃ѥ1|ŹР˔ˮŹ˸οɼȤĄςɸҬПTБ',
                                                    },
                                        {
                                                        'key': 'ԠȗŪѯǛˠΫƦÿȶӪѬĬIǺŗϸǻǂ҄Ƨòˉŧă\\őΖR2',
                                                        'value': 'm½ʡƜʪˁȰɡɡӤϞΓϻЩȫԋ\u0380ƊǈЅӒӣйЗģьЗȫͿρ',
                                                    },
                                        {
                                                        'key': 'Ϣ\x8dʴҵѢȧК\x93ԍëΟǶȢѨʾҋȱӛӶ£ϊ\u0380ŴʷЋ˜ŏα҂ß',
                                                        'value': 'ɼЙуΫϏǅ˒ˑÖԮӼњƁƱӤʲ\x98%)ҪϙѶϗѕӚЬƶэŔ÷',
                                                    },
                                        {
                                                        'key': 'įĖ\x8e¯\x8fĳĜӡϛ˚ȯ;ԥņʜ΅\x9fƇȵϧʅΙȐ2A¿ÅVɑШ',
                                                        'value': 'åөϰ҄-ņŻǯԐӐĳδʋǧňүıƽΕƓɮʑʙȢӻkǀǬѡԀ',
                                                    },
                                        {
                                                        'key': 'ˬСǵз«ŧˀʖäI\x86Ͱɹϳ\u0381ӖȚϦ\u038bɮґȐǵăŢЇǖƻıЮ',
                                                        'value': '{ƥ<ґ;τ°ӂҥѬǚȰɽʹӲʣƾƲģӁґʨšĬΤͻϞʝѼă',
                                                    },
                                    ],
                        },
                    'comment': 'ʰ˪҃ОÕϳɖĻѷsЎŪǝƗħӉԍĢѭ±Ѿ˂ѴѩϠĶηΚNЀ',
                },
                {
                    'keys': [
                            'Žъ\x95ВϹU/ʁЈΥşg3Ү΄ϩǍ\x80ĉsў\x93¡\x9bϏ}ΟuȫΝ',
                            'ϡŮbȸҔˌğанǢӰқȲ¦ґΪȷțŀŮҥ',
                            'ɳ ˰ϐ[ćΠЖyƀƤÕƌȷМĄ\x8bʦӖѷԤ\x8cƋӣøĢ',
                            'ϭĊ˵OÎȔȇľ',
                            'Ά˷˷ɡ?ѥô',
                            'ɳΚӻ',
                            'v^ӂȥўwԑӥjΑƵҥ˯ʢxƎų',
                            '\x8eò¿˙ȪшӗӂɟПʹ2',
                            'ÇƘňǶ×;ZӀӆǑӿ\x92Ȇ',
                            'ǬƮĺɩАͷüЫșҫi\u038būǽӧә\x9c˲ӥο',
                        ],
                    'event': {
                            'target_id': 'ɅǆԦéЩ\x9cĻȁЖԛŚҿӤŘ|ҵʦȐˬЏТʝZȀӚȭåҖú˄',
                            'parameters': [
                                        {
                                                        'key': '˻ѾѢƊϐѴʴ˛\x92ʢјȢΤÍә',
                                                        'value': 'ϸƳӶƍǤΩͼьŝmΔƲ Ź\x9aĉΪҜңĉ/ѩ¬ǟʣƮ˳ƒЏĞ',
                                                    },
                                        {
                                                        'key': 'ԂĲ˱ʎˠτǑѐ²ʹƔ϶ԏρϬϗʄΫ˾ƽΪżҒЁϒϙΦҚԚŲ',
                                                        'value': 'ѪzԄ÷ʨЉϜӗʵѥχǐ·ó;ԅӂɚӸɐîƣӫӶЋǱΉŜcɚ',
                                                    },
                                        {
                                                        'key': 'ԄЌɃÙӨÅƔǤţҬYɣŕǤ·˽γ ȩλǏΏƋɆҿ',
                                                        'value': 'ӭƬŵ½ткÑƎͻ>îǢÖƅӚǹɃ˕ԛđ˄ŴϨçʣİʬŞЮυ',
                                                    },
                                        {
                                                        'key': 'ԨƘс_ƟʨӳǄ˜9ӛʲԚξ+äʐɸAȐ\x8dþҢɽƈұϠҳwʉ',
                                                        'value': 'QưβŖЄӴǋԣŌҽϩϾЪ;ТGɂǟʣҩòǌѿЪƐǹ×ǝçɣ',
                                                    },
                                        {
                                                        'key': 'Ӄœ˘ϳ',
                                                        'value': 'ěɭ҂ăΨўЪŧұξ˾Ӭл ҉$҉Ãξj$ÁѵȎǱƋɃōɵă',
                                                    },
                                        {
                                                        'key': 'Õā\x8cӈȚ0ϰȼɢsÞТƢΙϯҐҷάŀĲ(Єs°',
                                                        'value': '½ƶ\xa0ȀƙеAÎΊͳԫʰԥ-ËέʋĥȀϸЕɪѧƤШɤяg˭Ȫ',
                                                    },
                                        {
                                                        'key': 'ʜǐʋƽ3ƀȧԉвļǘԎшȋԁόɰρТȓƟŔăȖȟ?Įá\x83R',
                                                        'value': 'ȹİПƷ¿ΫиǬзϓԜ4ȒɪϞɎŭ͵˜ʊΙǹΆÊůá5¨ʐƽ',
                                                    },
                                        {
                                                        'key': 'ѪѲɁŦʧԊ×ɗ\x89ÛÚήɵ§ŷѶ˲ѕў\x93҄ǏȐȫȯʫǅwÑȯ',
                                                        'value': 'шθ1Ǹ\x82ӧĎʵŸȢɹɏƤɀéӎ҉ǯMҚңΓ¡ЏϠĕѷŝȆĈ',
                                                    },
                                        {
                                                        'key': 'ƸΗƚ\x95\x96ȰʄγвƆηeKlɽ\u0378Çϱ˩ƥ¬σ\x97ӗƏȝνѵͷç',
                                                        'value': 'ɿĄӡ\x9dϞǚ҃ˏІŤ\x80҇ѧißԐʓўͱԘӅѧúʨҔȧßUŪԤ',
                                                    },
                                        {
                                                        'key': 'Ȱ¯+ÑǿԇΖāӪ\x81ƾºҖ˙ҊʮИ¶ļӵѵѬƮÿƬ\x8aЏ҉Gþ',
                                                        'value': 'Ʃǋ\\wD²ЯµŗĽхɿϬȩȘўʞˊÚ\x87jýІĭȼLȡč\x8dԜ',
                                                    },
                                    ],
                        },
                    'comment': 'ǡŔƑèºԇδɕǃӟΑҀΞϦķԣ\x9aóԔ»ȓûǰ˴Řӻ˳ӡиҢ',
                },
                {
                    'keys': [
                            'ȰʬΎʺ',
                            'ÖĐХ\u0379ȣȏĀ˖ӺȰ',
                            'ˑ˫',
                            'ҚQҦԇԊºȍѐɔпÀƋͼŃѿǝѾ\x7fΜоˣŘώş',
                            'ɤϐѤȼɕԮÁ',
                            'ÍļΗż·ɑú[ԗ˔ӟǏԗÅ',
                            'γȳҢҽЍã\x9c³˻ȼðɮ:ɊнȿčҀƲlġʣԤυВУиϕÆ',
                            'ǏѻȨъŦĈϘцҟԃӓØ5ȑу',
                            'đ',
                            'ϧϫƠĔ˷Ȑ¶θʽќŶԂ!ʺӨȎќ',
                        ],
                    'event': {
                            'target_id': 'ƪƗɄɚЙ\\tƴ˒˼å˲ϣ¸Ť҇˷ЄʡΧǮíʯ»ȑȅӢҾϦЕ',
                            'parameters': [
                                        {
                                                        'key': 'ĊǝĩΥˋ\u0382%ҞÊΎȹȼĺʡ±ԗ',
                                                        'value': 'БˬϝǘƘî÷®˥˫ш·\x9eĬ˚ǿƻóɨэԑŰɬϬʙʨƜȆ¦Ƚ',
                                                    },
                                        {
                                                        'key': 'ͷкШǣӿȝˢʔа\u038bԀϤJˑĲˎ¦ÁРǙ.',
                                                        'value': 'ƧӟFïϰ˲ĀĊĨωOŝΞɎǵɞNɯϡŝψғȗ˺ѬέʧӉȇĄ',
                                                    },
                                        {
                                                        'key': 'łζǣŠ`ĴӋԡӷǙƢŖϘʥƳηӾƀӂӯрƭ{ĩϽɥӚϕńȨ',
                                                        'value': 'ӧԃҲƀƤεϮŀsӲśa¹\u03a2ŷȮëү˛ZǇ˲Ģc=ȔýłѰђ',
                                                    },
                                        {
                                                        'key': 'ϱƎ\u0380ϏɶĖ\u0383΄Ǫ¹ӍμxƞʭĹŲ\u0378ȉƛƍȕϭԪįυǜˑŊэ',
                                                        'value': 'ŭōBӔ\xadҏɌЍ´ŏĨϓȼΏѹ\x88ԌɧӮ]ǵ·ǊɾӦǯдPљĻ',
                                                    },
                                        {
                                                        'key': "ɜ'ŜőȵŃĤхťɕËʤɋҼPνӎҊʙªΔĢčȶҮ˸ˑ",
                                                        'value': '-Oxʤ҅ѾИЮtΎǈþɟƎɏΖÛĲɻƤ˫ɒǴҷҶ΅Ð^ŦГ',
                                                    },
                                        {
                                                        'key': '\x83ɰɽӌö±чӓĹЉҝ',
                                                        'value': 'й\x7fӼǺя;«ȜWȘ®нҷÌƎlǥțȔʂãѧҳŮ҆RȫƼȩΦ',
                                                    },
                                        {
                                                        'key': 'LȻͶ˨Ζҝͼԧ0śɰΉ\x83ǵǮ#ПƁ¾Ԋ7ǺʴϵýωϱԙƔˊ',
                                                        'value': 'ӞǇНƠƆ£ö˕*ӳ\x8fТίĦʫӬӀĂ¿нü[ҌԦΑ~ɤґ\x9bǭ',
                                                    },
                                        {
                                                        'key': 'ƫ\x98ɯαӳéȟ˟дγԞД¸˕¸\u0378ȕȀ¿ľϯвΆϖǅ£ӻÊ΅Z',
                                                        'value': 'пǾ҅Ζ˲ʟдµȷľőӉ÷øħӜԁҢƌǎĦөğǀʼ˖˲ϲYA',
                                                    },
                                        {
                                                        'key': 'ɆȈũɅj¾DԀȚ"ª҆r`ӃUſ¾Ǆӏ=ȤɻČŋԏуƾһd',
                                                        'value': 'ЧуǐĘƩȷǽȖΪό.ӶөəԓԇʊȚʷgʳАɂʲԌξƵԐàƣ',
                                                    },
                                        {
                                                        'key': 'ĺԮЌΙҮ¤āƢƪƤʒ҈ɅғNԑƔHδeôő˕îŊώȠӲΒd',
                                                        'value': '\x81ǩҊɒͽőʶΒǠϥę˪ƹĉ϶Ǟį¾˗ŒԉқÑ϶ӳÛżɯвҳ',
                                                    },
                                    ],
                        },
                    'comment': 'ЋNОǞИңѻгӟю˭²ђʉԎˉ˾ωúҖӯԅҭӉʝ]ԕƓȹЫ',
                },
                {
                    'keys': [
                            'ƕ\u0381О\x86ϊŊУӻʘ',
                            'ıԃāӫ@ȡўҺǇΰÆˮ',
                            '\x7fǄ.ȹ',
                            'uÄXξǔUÎËǨέŧ˪rҫǎπɹΉϛóʏԩ\x8dɊ',
                            '_ƱϷʦȌ˙˗ɂаǿąæ҂ǣȔƪ',
                            'ЪŶҠЏ\u038bԛ',
                            'ÀȨ',
                            'ɐΓ˽ѸӖԡˢдʙ˻˰ſǇŠǾþ',
                            'ϔɃɋȕǧΨĦĎ',
                            'ˌϰĭα\x9fȯĽEWĤÝ˞İɄͷɧ',
                        ],
                    'event': {
                            'target_id': 'ÉÀШːҁӟÛ>зķԑƎŪȴϺȣvЋɠόǏβʀ\u03a2˭\x89ӨѾóǄ',
                            'parameters': [
                                        {
                                                        'key': 'Ħūʬ!',
                                                        'value': 'ö҂Ėʹҗβ˒ȆǺɅ҃ɣũϞǞŀʛ1ǡҡѤȽԑ+ŢԨĻăήԘ',
                                                    },
                                        {
                                                        'key': 'ӵџшUɭħɚҏÓǞδҸ˘Ɏ҅ÈΏͽƦʴɅʠЖ#Ƭђų\x9cʅξ',
                                                        'value': 'ÀԏΩӡ˫VǜѿǤȊҵюϲºҔĳϸʬ:ҍΊˮԁˮʜŅΆτӂ˨',
                                                    },
                                        {
                                                        'key': 'û§ĉɝ»ӘȍΆͷοїʜѝ`σȃϾΙ¥eϑйĴfĬΊͻʒӆƈ',
                                                        'value': '˰ѢϦ\u038bƉƆȸǳʹяɵƌÉǡiʧƄԤн\x80óȋ¿ӹ\x81Ŝʵȶʃˮ',
                                                    },
                                        {
                                                        'key': '´ХʣJӹœғԞʫĢȳƮμӨοƾϠļһ˥φȝʱ҃˵·ԜβЋѮ',
                                                        'value': '˲źłŤҸǸɎȵŪӺęԛRʤұ҂џȀцȖӤģƋȗГǙȩĝрѧ',
                                                    },
                                        {
                                                        'key': '§ɕʃ©ԧ\x84тˇΡƭʵǱȄɚéͺїчҐOĈ,ņɊԇɵ\x7fǅIΩ',
                                                        'value': 'ЮЗͰ/Ųƛeƫ˓gŋ\u038dǜƆ]ʹȩ˭«τˎѡ1ěUԐҟHƙ\u0381',
                                                    },
                                        {
                                                        'key': 'ǂCй-ĕȪǬ³˶ſӘ\x92ͻӠȪСӐӵ',
                                                        'value': 'ұҼġΨʷРLѶΆʗЊŧӺԜσʎ)ð͵yԭĸҖύчҵ*étƸ',
                                                    },
                                        {
                                                        'key': 'ӃˈӭŘȹ\xadƌȦůѡ\u0380ȉÈĉöғ\x9eš\x9f˞ʨ',
                                                        'value': 'ʉ˳qŖч\x8a˗ĶΫɊ|ǹϟГǍЛǍƉ¨ΩΏèĒҹ\u03a2êԜȦӼƫ',
                                                    },
                                        {
                                                        'key': 'ȱ@ӮǡşǳҿʮҩцŹ',
                                                        'value': 'ip½Ίчҗњ\x86ԫ«čΧӃƲΓŁԦΝà҄ȩԛωӺǍLη=ǭЗ',
                                                    },
                                        {
                                                        'key': "ȥΤɩ'ХЄɟψҏʞҬӬɠʂηӟrύΆӺȫӭ2\u0381ҵřõuōQ",
                                                        'value': 'ʣȦŗϤҦ@ҡԦ˺ΘэżzрЏɡªP҉҆ʠSϽîńƐүȃȼȊ',
                                                    },
                                        {
                                                        'key': 'ŝĶΓҹӼԆĮѿЙϤƒΉǄŖХЋjȈ˹ԟ\\ҒøčÍ\x91ǊùȾı',
                                                        'value': 'ǋɶːȒŏɿɥŲŌA\x93ϜʻмÛүėӎϧѓÐȥ\x8aħҮӺЩӠǉř',
                                                    },
                                    ],
                        },
                    'comment': 'Ԥȸ\u0383ʜϢδҹ\x98ǺéЂЌдͶӿȠŮĶǪ\x9cҨʚʞψ0пĩSǌΘ',
                },
                {
                    'keys': [
                            'ćƮğˁ\x97XǴǄʍǸϦҀÅԗɮƼɇġŎtȥΤÀӳλǁÑȏϏ',
                            'Ҳ҂ϤГ',
                            'ϗåѥêuˬͻ\x83ҵ\u0381ʎǊ˦ӴδʤņρԜ-ɖēҳſ',
                            '˛#ʀęƗ',
                            'ƁΊӕ\x8aӓϨк¦ơԃь˙ɦТÌӒԧȣұȟĨЬΘÐ',
                            'ŎΐӍ',
                            'ùԬӻŌİӣȘƑйϻϙЛǿȸĤăCǧќѽɂѩÀt˩Ŭ\x92҂ӌǔ',
                            'ĈЇƨ¶ɇȅϞԣЏФђ\x9bɛȶŮŎûʥūũ¢ʆѣкԛϨα',
                            'πɼƮƶωϢĚά',
                        ],
                    'event': {
                            'target_id': 'ŘɵA\x9fÕҵˬ\x9a\x81ǐȺҎКĝÆŸǭѭ«ҝԐπЬĘĉɄuԊô¡',
                            'parameters': [
                                        {
                                                        'key': 'ѿǥǖʡӌ²ǟěŉˊčӽâǌȅçëɳɈЂɮ\x88ȇΈǃéƃˮȈΣ',
                                                        'value': 'éŧW2Ŋ!Ù´;\x9c5ɮÆ®ӆЕɆљƔɢ¥ʚĬƭ£ɧԁðʟş',
                                                    },
                                        {
                                                        'key': '˸ƪԃΝ¬όǴƙˏʎӖ˽ЮМĶԃdȰɈЪƮӼ3ĖѫǹmóƝƕ',
                                                        'value': '{ŖA˱ӢǾȊRÈƴԉĀ\x99)ɶԬ҇ǘԠЈſҹȘȹҁκӐɅ(ϯ',
                                                    },
                                        {
                                                        'key': 'гɤʣԏÍ˗Ǘ˦ȕƯ+ДҼĴҀӝϺέѺ$ƯÑýʛįϩȝąˀӞ',
                                                        'value': 'ȋǝkԝéGҸТoϝӉíɵˎҴԬ҉ԋÓБ~ϕԦȊЦȦРӹƯʧ',
                                                    },
                                        {
                                                        'key': 'ҿˡ_ʄ\x98ǫѩȠϼǇ¿ӿfǵуÿ¿Ɇǧҷɑƅȁү6f\x83вѱȬ',
                                                        'value': 'ҲǕϬl\x84İĝͲªȴƱĂĻʗŋѐǁŬҡȿ˹ǡɺèаƝҧȖԥϱ',
                                                    },
                                        {
                                                        'key': 'ȉZˆɷӭϔĪЊФcєӮрӧ·;ͽӢƓ˯ӎњΚÑȑͼ˂',
                                                        'value': 'Ɣ]ѳβЉιîďЀȋíѰɞәҚƷȖɦČ˙ѡϢλ;шѸ¤ӔΏ*',
                                                    },
                                        {
                                                        'key': 'ǔͽ?ψԪ˅ŠԧIԣƥ;ʂҩЛЏʀȴѦęюϑŬȏʝčɵϳȾÿ',
                                                        'value': 'ÜӲʮѢĞɤΠ˶ǭΪͷЁ҄ΟтϏ˫ĺОҼņ\x99ӵŘɯǖϋɜªȌ',
                                                    },
                                        {
                                                        'key': 'ҽN\xa0ƍз`ľӊЯʣԚǿŢ·ӎѝɧѿǃČΡΨŔ°ȔʹоƱϛЛ',
                                                        'value': 'Ԗīk}AǆјGˁüʚȓǟH\x81ïϔϋ˂ԕ˕Ħ҄яƽ˥ԣΧȡћ',
                                                    },
                                        {
                                                        'key': 'pȎҜΖȆǽɨѡцЈҏƏɢůJƦàţķҪԋЀдą³ǽóϵʺӄ',
                                                        'value': 'SɣȯγґÌĎƱǷжқӺĆБ{ƢƐʹƃԪϑɖ3\x9eğ\x9dχʒ˘Ϯ',
                                                    },
                                        {
                                                        'key': 'Ԑǟĕͺљʌ\x90ХкʀԃɇčŸ\x9c&ŝȿ\u0379Ǻˁ¿#ӓȱřӴʑĸĽ',
                                                        'value': 'ďСĊσ<¨ФǅĕǃӟƯǬĦ\u038dӨёǫʐòȟÖäӁѱXǁȆɚш',
                                                    },
                                        {
                                                        'key': 'ǻŒîӼ˹ЗHʄ/χƅ\x99˓Ŵ\x89ѕ',
                                                        'value': 'ʟ6FǖťϫζƗͻAS[ƧӎdǱƁÂҕϹ\x80ɱȢƾÒʵ˄ӑǱԠ',
                                                    },
                                    ],
                        },
                    'comment': 'Ȍ\x9aѨEѩqγǾ8ʾϐЁÃĜkɄϊӧˆƓɵʹǹǃǫǶʍʨαώ',
                },
                {
                    'keys': [
                            'ͼІȲȾԎӉɥӉӆĂÊґЯĽϖʉўɻ',
                            '(ĹΩȕʸљĆѓƭʮҴАϔѺН',
                            'ɟӰȈϡΠѧ·ʅȳƗҮҧ}ŃȺ¤η˨\x86˚ˑ¸Ìχ\x96',
                            'γϩX',
                            '\x96)ǢϝČҺԦĤѦǏǕ',
                            'ԃʒíFĎãĺéѹɇȪӝˤǌƮԚ',
                            'Ѩԃ',
                            'ʑƟ˧я ŀ\xa0ǭϔǹǟȉӘŋFȎјlƶɝʈ˵ĉ\x96őƒԉӶ',
                            'ʪҲĶɬиҊϕɿіƿτɚɁΤ',
                            'ƪʒȬËӍӾӟbМͿŚĳ¯˝˔\x9f˥ф\u0381W˰\x8eƭĂ\x9fĀƊƶ˺O',
                        ],
                    'event': {
                            'target_id': 'ѕ\x9aʻқҭˢƢҶȱħ˺şұɛӆӘǏΉ®нςƘРѼӅȗȍεͱΚ',
                            'parameters': [
                                        {
                                                        'key': 'Ҧưy\x92Ќ\x9bΞƃϟƃΑӭÓƘĚɻӹÀÊґA÷=ǎǒƫGʇʷΛ',
                                                        'value': 'Dˀľȏ\x88ŁМҏǩºKǛɥȊȁӃȎʀôRʎκȔѥҧćԫÜȪΜ',
                                                    },
                                        {
                                                        'key': 'Ӧňҹǔ2ƍȱįθʨҿЧȮπԪʺˏ¼ƒǢπȳ',
                                                        'value': 'ӥОŭʂǔɍǒщ҇ҏǷɑӝͳǢɢƥѿˢδ9ΙúdͽŅȆӋʕӶ',
                                                    },
                                        {
                                                        'key': 'ԚҼ÷ǩĮʩӍ·ΥŎɡʄϾӋͳӳ\xadӺӁǶƺǧǪԊŕ\u038dăѕ®ģ',
                                                        'value': 'ųϷȹȭƱѣV:ЍĴ\x7fҗԪ;˂RΖȗǋɞȥȎΕКɨΑɣҹĜϺ',
                                                    },
                                        {
                                                        'key': 'ƖÝè˵IˤΓ˧ʻƤqˍȾ\x91ș',
                                                        'value': 'ӴÁɂ϶οʱăʍϔΰ×vδˌТɛΰʕСÉEΪϲψξ\x8dƱȟѢŤ',
                                                    },
                                        {
                                                        'key': '\u0380ĿΓș˅ҡʷ˼˸ŮǑѶ;ŉɍĕЅ˗ӉŁвĲɍġȽǮӠ\x81ѷʵ',
                                                        'value': 'ƒξϫRíâȘԧáȽɠ˟Ȳϰ¯ĕɒ¡ƏҖ\x9bwÕЩƿɥ˒ͲHԀ',
                                                    },
                                        {
                                                        'key': 'ВȯФѸʿâεŨŃȏѸ',
                                                        'value': 'ʓ>ЎжēȮ@ɓʟ\\ĤǅУ҂āǄůpŎƄжɢƻӇ\u03a2ӕͽĹԍӬ',
                                                    },
                                        {
                                                        'key': '\x7fΤԐ\x9bȫƇ\x7fгӟŨԒĳˈYǾͿѮȊp\u0383όҥɲʫɔӅfԫɀǧ',
                                                        'value': '˳ɨîϥƚĒƎƢαҌ´ӥȨҫDʕɵʙԌđġΆŅ.ĎĜгϋƶi',
                                                    },
                                        {
                                                        'key': 'ϨǇBɴǡԕȕӨӑƦŸN?ùŤˋƫƕsг\x94ʶɭ[ЫƉ˯yȰğ',
                                                        'value': 'ăľ×ɆѭͶӛûӑјƙķԗyқ\x8câѨϘ˂ˤ4ӹˍКǄŴ¿ƢÊ',
                                                    },
                                        {
                                                        'key': 'ΚKƲ^\u0378ƦʤѶƌӸÚwʗԐˉԆ҂AәÆ\x8bȯѷʭС˚ǳɫɔԔ',
                                                        'value': 'ˮϑ˸įƵ˨ԋśΉ=Ќ\x86âŎϵǯӶʩÔƭÏ¯ĔҴӌίѤȖȉȎ',
                                                    },
                                        {
                                                        'key': 'ǿϐНҫĀǂԬӜɿĺιeѠэυˡ+ԏKƦc\x9f',
                                                        'value': 'ҞʂĐÙƣ¤bӑöȒʤӣʋɂϜɿ°\x91ǻwϦɿğİ˞ӖɝÁӗĬ',
                                                    },
                                    ],
                        },
                    'comment': 'лФҷЌϭ\u038bƥɒ¢ҩԇÊӍėѤĊǂȕɦӞʉPѬҥǰ˞ʳԗƋw',
                },
                {
                    'keys': [
                            'çӎΡӫȩπơʅȗѣΕԛǉÎOŊȣύʜȼһʿ',
                            'Σѣ¨ԐбĨȩķÚ\\Бʥ;ҪȬŐ8μ',
                            '9ιɾԒ\x81άӯӾƅћӌZůʏύƒǄˢ˥Ųéψȯ\x9eӬŦɈɨ',
                            'jʻȲȍӽɫӇѪӼϐЯƻ',
                            '˔ӻӶӳ˟ӤÑ·ǲĚKÓʊȉȟɫ˺T\u0380ʀɻћԒ˞',
                            'ëΗǥƂΑ®ӉӴĐϊ\x81ɂ¯\u0383ԀΏԈɳÆŃ5Ҫͽ˓Ђѩζͷ',
                            'ԅ˞σΦ˪ϲ˵ōŞӋӞӹ÷\\źǇñ¬',
                            '7ΣůћńԞ\x95\x80ԉĉƅLƗ·ԡʝ',
                            '\x92ұÌƷʩĄ˃ҏǤɕ|ēĿŮѕȎϦɲbΏCǧ',
                            'ԐϖʎɆнҤÛȑҖbԃ·ˬċǜǛʍϴ˨ϴξǼ',
                        ],
                    'event': {
                            'target_id': 'ĺFÂóǼϖxѕʁϜ\x8cǂ?ЪФȘʯ?aüмȾͱƀ\u0382ϭ9ƭƔα',
                            'parameters': [
                                        {
                                                        'key': 'ЛҩӂȔѢŖ£ǡ}ҡĮôŽƟΚÍѳɮʔưƧʸŤ˖ρЋíΊșɓ',
                                                        'value': 'ʾƀʿҔƿНИнӏĉлӎ˂ƎɑƵɭνmΛѰ»«ə;РηԊϘ[',
                                                    },
                                        {
                                                        'key': 'Ѵǂ΄ғԄÅɮŉǚΨг\x9aԮ˺Ѳɥʕoʒ\u038d ˁόČĝĿ¦ũÜβ',
                                                        'value': 'Ӫ\x9eōҼñҽΆЯǳˏɱ˵ѱɮҨҭϰԌҷEϠȽŗҹċƷ˙ţбΗ',
                                                    },
                                        {
                                                        'key': 'ŕƩàÿµɽ¨ΚļӍʁɓƳЦԀɑ˥!ңҩȚЍɈԥӰҞѿöяг',
                                                        'value': 'ԕƾѱӔſǀÚʕзȶӑɳȵԖҽǜƉυǳɀŞɗńӤӟłҙœȴʄ',
                                                    },
                                        {
                                                        'key': 'ŋЩЪƟƇǒ0ĉńԡїˁśΚűэȂĹɥҷzǑɬͲʘ³ϷԚƷʛ',
                                                        'value': 'ϠŨ˓ҋɷȤˉЖӁˏʶԮʠΉϨіĝ^тɉԍȂɝɭтü˙ɂÿѩ',
                                                    },
                                        {
                                                        'key': 'ʹӴϪѺԃԣʕƏ\x97ҝ¡ΦɍӚȂɖ',
                                                        'value': 'љ©ђėЬЩȣtȶŬАӺЁ¤ɎǍƷ/ʤ¼ΧѸƈ)ѵ\x90ҨώјƎ',
                                                    },
                                        {
                                                        'key': '¾ԀӾʨ',
                                                        'value': 'άӝ]Ηкɽ\x82ɗӆɏҌҶ²ԎʬƹʢѣӮˠʱ"ãIǨÒƹɋǮȲ',
                                                    },
                                        {
                                                        'key': 'ӯӆѺβВіzǘD\x85ϱϾҁƛ\x97«ϼ˾ѺĆƾԈӏƂƠЁˬҹ҇¶',
                                                        'value': 'ĖɖԄҒʣɴ\x7fȸӀÀƬҟӍҶΛ6ɔӣříѭϤəҘLáпсԚӓ',
                                                    },
                                        {
                                                        'key': 'ҾǎыƩÈ\x9ačԬˌȖ˷џɬƎϽͶƔӖѮӒΊԤїŲŊѹϟӹǮ',
                                                        'value': 'Ϧĝɏϩ\x9eҺńΥǫèɈѦщĔ]0\x93Ѝĵ%ɫ\xadșЅEёȮόӛ#',
                                                    },
                                        {
                                                        'key': 'ԫЪĶƣѝȔѩɪȀϞ½ˇѧp;ΠɉЋ)Ȓʘȩǭrѭ\x8dĘ͵ɠŞ',
                                                        'value': 'РǟŲxŔŉҶӯ®ʾҮЕϫǖʪκ˷ʗʥťȠǊѕϖ]ũӹ7ȕ\x85',
                                                    },
                                        {
                                                        'key': 'Ȝé˨÷ÜóЇƔώȁϨʡȑϤҊŎËľҙþωňɾϔƹƔӜʕǇ8',
                                                        'value': 'ϷΌȨǻ҉ǧПʘzǶɟǥҊ˘ʎ=[ƏOѷɀŁƵ˃оЧˬϧԄέ',
                                                    },
                                    ],
                        },
                    'comment': "ǝ\u03a2ʓΑЮϷвbϬǦΗΉǁҌǰϦTîƢҤӉ'ȸÒԚАĐΧÏà",
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'master_sequence': [
                'ԋ',
            ],

            'bindings': [
            ],

        },
    ),
]


class EventsTest(unittest.TestCase):
    """
    Tests for Events
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENTS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.Events.parse_data(test_data)
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
        for test_name, test_data in EVENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.Events.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENTS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='Events'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='Events'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='parameters', name='Events'),
            ),

        ),
    ),

]


EVENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ªYɠԁкӳ ЂвνśľɎȵ;ʳ{ȔEӿӲΕ\x95OƞŤƊÄƜγ',
            'description': 'ϭ҉ƋѼөōŶˍɚɣӉϒɰЫљGɒЄùӭɅnãǳīҀΜƒΎέ',
            'target_id': 'sÃ\xad˩΄ÏɜӠжʏоʓ˦рӋЄ\x9eϑƃ΅ǟlЮʛÏЎÁԂІġ',
            'parameters': [
                {
                    'key': 'ѕ3Θ\x94ʸŌ˕ҒȕƿϱʡśȐńʧӒΌ$\u03809ſÎ\x7fǃEѽǏǅҼ',
                    'description': 'Ж\xa0αɟ\x9f˸ԓєΝƗԡѨɚȘԇķCJ÷ԘћюŝśũВзcƜа',
                    'default_value': '¡ʪɂȽԒҖĶŷ@ԌГďϋҚ\x9aҘŖԋӯǄÀƉǜƮ˟҂ǜʱΰ2',
                },
                {
                    'key': 'yй˜őδВǍΕEӌӟɨԑÐʻѼȒ˅ɱʃыE˛ˈÅά\x83ӷѴΩ',
                    'description': "ŜƘɌдЪҸϽϷĉĈʦxϬ'ăáФ҄ĸȿžÄʣǽȑɡ¹Ѱőӏ",
                    'default_value': 'Ũ\x84§\x9aƨϼѝƂϭ\x8fƼ˷`ɴͿ\x8bлƷīȵϮΡȊˈȜʒӷ4¢ɗ',
                },
                {
                    'key': 'ˁʞȓҙ\x9dԦӻ¨ɦҜǰɯѷʀ',
                    'description': 'Șˎ\u038bɥ϶ʐЋ\\ѻϲˡÙ˳Ʊу¿˙ʓеɆ0Э¦qӡǊ²Вǌӽ',
                    'default_value': 'ƭϽƃü˻\u0383ȵŭPíĸƋþǐz\x7f҄ŮĕҲ\x9eͶϭsЯŗ¯5Ъҽ',
                },
                {
                    'key': 'ĞЬϐΟʡ',
                    'description': 'țŨǪ\x8fŞʺĘȺƘɿӣ|ˀȏûБŵȈʩχԜƹ\u0380ӭźҞͶΆʥɿ',
                    'default_value': 'đ[ͳƷӹǾ/]ǴЮƘɛӶɩR¶ˁËʷӌ\x95ӻ}ȭӸɰȴʮг˷',
                },
                {
                    'key': 'ąƩԮ¤ƁҘЧӝƔũʶϲŹ',
                    'description': 'ÓЉ\u0378ɎɬÚȻńҴӁʩí/ɂЪʥЃöɨʧ˽ХΏɓӹԒЫːұɮ',
                    'default_value': 'њЮǗҳʝ1Ѥ,˂ʷϻ˽PũSĀӥȵѨԘǄěЋȃӯɔǭȕþˍ',
                },
                {
                    'key': 'лƜ\x8fýŊԙ!ĲƭЪ"ў\u0378ԢҀƑѷǥ҈ϩʯɽ)ȝҎӗqăӐđ',
                    'description': 'ʜмԉƈğΌǐ\x96À˗Ͻžҝá˅\x97ӡȐ\x87иČԅöɁ˝Ӧ>уŇŜ',
                    'default_value': 'ʆfĶɺʬÉќTãˉǏѲ\x8aÃʧҿ`˳ӏƌȈǇǴѐΤM',
                },
                {
                    'key': 'S\xa0ԗȥБǌԩϘȟӝƣԨѠͻȣӚ',
                    'description': 'ǴѬʜӁǷ',
                    'default_value': 'ϦɝúШƀˋæɴўжƾʱԎίӊɎǥĵrǩОѤӲƶԜɀæĨ;\x8b',
                },
                {
                    'key': 'ȻҩɀШʭҞĳǹЇϯ§ʬӋϣӏҊ·Јʋѐ˦ŒɆ\x8dҎŕѣʴɦš',
                    'description': 'ʱΎÃƯԃͻьȀ\x82υԅtēΖʽɨʁ+ÑρɾӶҁÉξxԛԣϑԬ',
                    'default_value': '@҃ІÑΟύsϷ>ȇЏ-ˑ\x9fАѽРҫʹʲӬЌƲԣȺͳѕȅ\x95˪',
                },
                {
                    'key': 'ǟFγĪƱ˽ȶέκϊǇ˯ÌҋʹԈʰΐɛʃȷçń\u0381ʛéмԩұļ',
                    'description': 'ƳĖsӧԜɤPĆʵʽΝƎƛȘĒ®\xadҸŇж˟ÍǴ҉ΙԧŽɊƐͱ',
                    'default_value': 'Ȟ\x9dҬ҂ҖƗѭȒ˟EԣŦǯΘÏʥϘRҢȈɷ¶ϸιʀѰг΅ʤѩ',
                },
                {
                    'key': 'ŅuӄήӰξфƞɇȋхεԝΨˮъǡӣĽmǤ҄\x8e]ĥƎ[ƨƗѤ',
                    'description': 'ƜʀƶԠϱ¥ŲƅƵ\xadSʍƍ,˫Ϯǽ\x9eБȖ\x8a\u0378ΓșӢsSѨЩ\\',
                    'default_value': 'šçˉђżтъȡҸɸť*чɼĄҎůɨʏѣȈƼėԩʧɗѥԒҀǬ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʘ\x80Ф',

            'target_id': 'ˁǑ\x96Ƙђ',

            'parameters': [
            ],

        },
    ),
]


class ExtensionEventsStateTest(unittest.TestCase):
    """
    Tests for ExtensionEventsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_EVENTS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventsState.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_EVENTS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_EVENTS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='ExtensionEventsState'),
            ),

        ),
    ),

]


EXTENSION_EVENTS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'name': 'ô\u038bԘҜˈÒčŖūҠșȎ2ǫ#ԕ˯ДĭІu\x80þ˩ɟɊχԚĮԈ',
                    'description': 'κġԎǥÛÏ*ˏǙê˫˶ÈүҜІL\u0378ų҆ąǲӛ(ӸϨŷŰуϤ',
                    'target_id': '\\ˏƊɢőȡԌ·ǺǣzȰĊË˅л\x82ӧΞɀɢРԖŷοɢĆҡ\u0382Ӳ',
                    'parameters': [
                            {
                                        'key': 'ϐ\x82ŤxƸфԏĔӝҹɴǯǕɺzӯÿƟĆҞӝƘ^ѩϬ˩ӓѪЀ«',
                                        'description': 'ƎţҧЇѼҲ\x92ѻʯºÙѡɓǭʣŽ˾»ǧJȧԆǪƆȾӰԩïŁӖ',
                                        'default_value': 'ҶԖЏǳ˽ʧɕԢ\x9eҠьҶˤū\x9dùҲϭƄФ(ĶşǦыӷͼ\u0382\x9bČ',
                                    },
                            {
                                        'key': 'ԑaϠ¯ԕгőыΫýҜѝƦēéǇԥ\u0381ԛӫѴѽŔlψŅщ',
                                        'description': 'ʏŭ\x8cu1ӿǟҟӃĤѺщ(ɴǰʁъȟQԜԂ˵SλŒʡYBȶŮ',
                                        'default_value': 'ҭ\x98yӍɤӮɩ\u0382Â\x83έͻжŏΰӕЇӖͼKц;ȼ>ϱѳλƥȽʕ',
                                    },
                            {
                                        'key': 'оƩƜɩĴȊfϷҗԣԂɚ҂Ƥς҈Ⱦӂƻвϔ˽ǓЮ©ǏѳΉóʁ',
                                        'description': '7ǻƋТrʾˇёҜцΈ\x89Tʵğˍψ\u0381зĻҢ¾ͻɜUԤŽ\x8dϣ˕',
                                        'default_value': '˻ʶ\u0379őÀɰǱрƠԭƎԏͷƌѯІϏɅӷŇ\x91ҊáӅʞǐjȏ\x9fƭ',
                                    },
                            {
                                        'key': 'ėͱвÓӝTʸ¡ҩ¼ǱɄЭή˫ƺņǚˋс0ҦʲȵΤśʃҕ\x80Ģ',
                                        'description': 'ʄćӤԨόОɆńθϵϺʊϽǏДƹ˫ȋΝѤŌʽ8Śӌƪɞių\u03a2',
                                        'default_value': 'ǐѝαùӎΞáӑԎч˥GvĤĦiӨӕCӝ²ԠíԚĕӈЛǧǫҷ',
                                    },
                            {
                                        'key': 'ϏƷÃȡԘʆϝʾΛêӒʚ˷əʮ\x89ƃ͵ϻгB˾εɟφʀŊǇƗ˺',
                                        'description': 'Ԫǵ˶ǹΣʤЫȽ2ƺȢƣAʮΟҰƫjǸI\u0379ҵΪѩǩ҃ɠǥԞª',
                                        'default_value': 'ϞўȺŞl7ȰɰҠОȻЌȧЯƘсǪ\xadϝΓЀƝϬӆɽ\x7f˥ήʗ8',
                                    },
                            {
                                        'key': 'ԗλŞʹԖθʆѺɯƞ{ө\x91ғЕVҔɔ¥',
                                        'description': '©˶Ԏ˴ƎϣӌϫӹȣʂҭӈǛ1ƧΟɡö+ЂҡˁŝѬ\u0381ѵǌўӧ',
                                        'default_value': 'ĔˇΨӀơǵ÷ѷ6ȻΝĸͷΫԨјͳrʥΨʜӧϚɵǦŻāЀþȃ',
                                    },
                            {
                                        'key': 'ȸ\'҈ΌԒ;ɄƦ\u038d"ԒӹPϷΨ҂ƢlϬJò¿Р',
                                        'description': ' ĔӰ~Ǳάæѩǽ\u0382зÑŸ8ůӊüҝΘ˃\x87ѯĻЂйϦγԗӭɹ',
                                        'default_value': 'ʘ˶ԍԤŵòéЛ˔ԍĘԢ҇ΈƧ˺2ГҎʿʊӰΪǕ˗ί[¨ȑԊ',
                                    },
                            {
                                        'key': '˷\x98ȗőɈ\x8bюĬǣΫ',
                                        'description': 'ŒŏѮʙԦƮǠ±Ǒ)ʼѣόϥ,ÄВ\\ѻзčӟΐ\u03a2˼ºϑΨҫΗ',
                                        'default_value': 'ϳԀdЩĶƛΪɼɮг˄Π^ŌƬƱҨҦӻÇ˘ѠγҾƭϫRƕϡҽ',
                                    },
                            {
                                        'key': 'ο©Ҧъϐǂ½÷͵ĔIҰΜˇϟȊĸ©џcĤϪėĺм_ʪƋɈƒ',
                                        'description': '˾DϙĕҪ˳ľFΗ¤\x8eϡȞӷҥԦʼҧzԎƩǲӡŭƴЬθäϥң',
                                        'default_value': 'ƁҳӜɹΧ\x7f іmМɹưƺňԥ˷ԛȜрǴλǚЬҴԈĺҁŦϰ\x81',
                                    },
                            {
                                        'key': 'ņЭƃFЏŨůʴ˲ťɐƞэΞ˼ɍѣ÷ȁϥЮ',
                                        'description': 'ɪǃϰˆѕʱŪŵѱšӥ˫ŚƤŷǨĮЩǕӞʆӑЯˣŷłͽ3Ɓњ',
                                        'default_value': 'ÃɁŝÖȔúСʊɳʢŇʒωĒ\x94οӵāǡμŸeŏć˦ΦSЭɃ ',
                                    },
                        ],
                },
                {
                    'name': 'οȤʌʫ˻ɟʝԗvƍǇχʨ˼ң6ǄɈgȆĶɑ×£(ȄÕҠ\u0382Ĺ',
                    'description': '˟ɰɖǕϦ\u0379ҔɅҎŲωfcɔќĶʴǜƭ˽θƛǞ´ȟ>˙sƬо',
                    'target_id': 'ӣΔƭмą˔јǝ˼ƿςЍɿȩˀҷαȝǭǳЏЅĴ#ӛƑǻυӯѭ',
                    'parameters': [
                            {
                                        'key': '\u0382҃ƝȿΙŮŭͰ¸ʄXɣӷř2ʫ͵˾ɀ<ʛκƲõȋРȇЕ˘Τ',
                                        'description': 'ҊȐũӈƱ\x94\x91ҭҟɲφщɪ[ǁʩǛеȝʠτ\x82Īɦ\x82Ѽ3¾Ʉҗ',
                                        'default_value': 'ɿˉċʺбͷǲЕϞɩƕƘ/ŕˊϩԚɊͼЧоŪҤ&ˋѨ;·ηԈ',
                                    },
                            {
                                        'key': 'ώÉӟǥԘŃҺˊƙӔ',
                                        'description': 'éўƢ´ȂʖԉʙВːΗʺѿʦʟűȋԦeΆ;°΅ȜҰԘі˗τǔ',
                                        'default_value': 'Ɇѭћ˒ˇĢɡҟϐӚ2ΒyǵĞ˹ƼŗϷ˄ʉɤɇɗʠʊʂϫIɬ',
                                    },
                            {
                                        'key': 'ɯð;ЌĒæѵˡˢmѬȀϋǅõІǊӊήƧýȰȚЦ\x9a',
                                        'description': 'ǫȡƟԚ½ǽƒӱR\u0379ľԃfŃӞsҭϒйǯɉѝ%әřΪԑý\x9dҰ',
                                        'default_value': 'Ƃаˈ҈ŖќýÂîˬ\x99aοѹˌҹŕiƙѸ\x84ȫȆȷȞ~ёЭħŴ',
                                    },
                            {
                                        'key': 'ѬњŃ˾ԓɂMԎҶʳ',
                                        'description': '¢ΙƍλűҞͳѴ(ȑѶǖĞяԩĐǩƉ(ƨȩΧŭďЪцQέq˭',
                                        'default_value': '·ϢяĭȆŠԀԇƃтÃΐѭϫŐƼ½CͶŧͽɘ\x8fЯϯQ\xad˯ĎΗ',
                                    },
                            {
                                        'key': 'ǲƇɿғţѶ\u0379ЇġЎ[ʁȷȨΚΑVĠԁ˳κ¯ӪʑɱεҺєǻ',
                                        'description': 'ӜǶԢң\xad˜˜\x8fМȮ˧ԒhʖʹŮίùζΘӖi[ǍǊΧĽǦ»Ȍ',
                                        'default_value': 'Ӧ˦ԙǩēнͰɳtҷҞԨҌȁƷѡӂŒńńû҆ʪ΅ĢʯԌʊ\\ʳ',
                                    },
                            {
                                        'key': 'ȤйȓȧѳNыˣӏӥuƦϥƀѷʥ˟\x98бø}ĳǹ\x99ŪˇŋʾԤˤ',
                                        'description': 'ƴԝΥȑҕ¼ɳʓ8`é҆ɫ˝ӎҹ^Ϸƣ"ӟǩ\x95˂Π\x83ѧϒΆҦ',
                                        'default_value': 'ІȺŶ˜ςƺʬӎ\x8d&\x96ӎԈкӓŧҁ¶ќƔԍ]ȒÂȠĒŇӵԓϽ',
                                    },
                            {
                                        'key': 'ˢə˄ʤԚ˵ѪġǠкűӍƔ\x8fȭӾɈŰʗȲÔʨΠҕєщͻΘÇԢ',
                                        'description': 'EӾѿ¶ӗ˗Ľ΅ĹȊΊӣŗЯƍҜǷӖǦ϶юΝҌqŅ\x86˪ƇěĈ',
                                        'default_value': 'äǕЫȠʏN¦ɹȬͼ˰Өџǳε"оӽԥ\u0379ˆҼǼýĻƀ\x8aȓҦʈ',
                                    },
                            {
                                        'key': 'ʲӬƵԧŔϷяùүͻſж\x83ʑКϹ\x83ʍ\x9b˟ͰɽIǶΈҿѠРͻk',
                                        'description': 'ŽăʨљǼŤʗȤȣԚӳϛƅ^ïżҍѝȧȓЛĄāĢBԝϘ˗Яɥ',
                                        'default_value': '˻5\u038dƴ˪Ɣҍ˦DңҤǋĕã~ƑºșхиҞ~VʞѰĶ³дëʐ',
                                    },
                            {
                                        'key': 'ĒĆƪζȮԮɟΥˡÎ×ʺȜ?ԮˇӝɡӝЋѶʀА×ԙҷԄ҈',
                                        'description': 'ҿǽÓȀͽ˂ӲӥɏcȆюȊƗƏʍ\u0382ԥŊӊӈʧЛш˯Ƀș`Ąď',
                                        'default_value': 'ơ\x85ȗǦҁƩӷӣԩ҅\x85ѫþғƙǀǜǐ϶Ʉźϯ\x94ɜϘЀԡԤӢѻ',
                                    },
                            {
                                        'key': '5҆\x85ʐЪǄɷΎżɯđƠĮԐ(ŬȈԇӬʥԦπϣͺÍѭϜˆ',
                                        'description': 'ѐŴЭ˻ҒǑÑǏʹζԛZ=Еūʉ˞Ɉї\x94Ǽ¼Ѷɭѿ2Чˆ\x99đ',
                                        'default_value': 'l\u038bɖΚӧӯԖƭɾũУĘͱҦΖͱǯêέǂpʩԌƠ˓΅ǁ3ΉӍ',
                                    },
                        ],
                },
                {
                    'name': 'ɑҲǐǬԮƸǁʂȇǋƯзεˈ.ѻқɆ',
                    'description': '«ȍԮΫ рώˁϿûÇϞˉϦéѵ»ċȧ\x90Έɇ\u0380Pуˍѭǹѡò',
                    'target_id': 'ƉѽǡԬпĮї8˸јϑJʨԓɒƤΚҋĹђӱyЇɃāӢÖ7ӏΞ',
                    'parameters': [
                            {
                                        'key': 'ƸӴǗлдϔ',
                                        'description': 'ːʤ6оɮŒÇяʌјϴī/˚гƓɻίŰԞϬĝԌʘϤžʏȅǍÍ',
                                        'default_value': 'ǕɊ˒Ƴš\\ɝ³ҀȘƖԁrӣΠŦǘԕænȾӥȉƵͿªƿҦҔϬ',
                                    },
                            {
                                        'key': 'ǩς\x86ϼʁɧҚѻϰɆŞ˒ҔϳŠрΟԃҗ˱ϱЬȝάʪҢǵώʑĞ',
                                        'description': 'ċʴɽϥ!ą˲ǭμČŴ˾ѽЊ6ȸɌǎӚŅ\x96ŪïUɉ¬ːƫĝ\x82',
                                        'default_value': "Ҧ˲'ϙүηLǺ˭ȆêӮŝσΞԔȒƫ=ºјãɨΞăΡͽԩ§J",
                                    },
                            {
                                        'key': 'ŝϕ˅Ƴ5<²ƹʙӘȍƜ½ƵʱmѾӲʁɼѱϩԧѕ;ƠĈĨƀӳ',
                                        'description': 'ƽʠïʥϑț\x81Ǻ3\u038bƛǸϰɫEĺƠ\u0381ϙÓ/á¶҂ɛдǨʗ¡ʦ',
                                        'default_value': '˦YȷƺϤ˭ѫĪгҟǆʍ¦ƶȸùʬ$\x9eȓԛǒӝđЋϩ҇řæϯ',
                                    },
                            {
                                        'key': 'φҐòϾɲËʼ8МʵɖφϧšÕĤѕѻ˥ŦЍÎƞþӣϥBÜ\x83ƣ',
                                        'description': 'лψѧșʏ˦ԑΕŜдіҼŻ\x8fѦǒԝӘͽѯγS\x85ϩʁ)ȧҔҀѦ',
                                        'default_value': '¦σʺġŦǔϊǵҲéƢ˒ӭʨɪȚʷɀRȖƹјзӳ"ÅǓ\x8c˟Ȭ',
                                    },
                            {
                                        'key': 'ҪіԟϪOѴʳ',
                                        'description': 'ǢŞǅØʄȬʉŎɰ¼ɒƹͼʟĔšˋнҎ)ŬԈЊȆŷԖƘԔшǟ',
                                        'default_value': 'Ԟӈ8Ƀ˞Øɱ˲ԩҎƪҁʺ`ơʮĄȒ\u038bþƎâӎ3rţҽʶЙԐ',
                                    },
                            {
                                        'key': '\x9fҧЉ®КðRϢʙωǊȏБӂьoƣзƉ)ƺ%ēĸ˜ũŏ|юó',
                                        'description': 'ƟƺώŔ˸˂ƢґȒӌпƘÖƼß҂ŖȜȰÊΡӱԉ\x97\x99ɗͰÃԃć',
                                        'default_value': 'ЅȝҎΕ_өI˂˗ÁνԀлɶɳѮĦĽԭɱˎҌиәь˃:°Ʈa',
                                    },
                            {
                                        'key': 'ůĪĮѧˮҀȋ+ǢДÜѰ«ϻʺbŻʳ¶úяӃƤĉҕǣɣˈŞŤ',
                                        'description': 'Ԟσíͳң˾ŨԊĢʢÄѐǇɻӌ¡\xa0ԑĭȍϓӫǙӄʍDŴѦűȽ',
                                        'default_value': ']ƢǉȢɝςβŬKďĪςԕ˖ԦΧɾΓϢӠӷΊāɕƳˡΥźжȰ',
                                    },
                            {
                                        'key': 'ЅΩɾКΧӮ\x81Ċ8ɏӿŁӓ*Ұԡ\u0378џѰʕЮĵԪԥʸŢԈѪΏŋ',
                                        'description': 'Ü˻ĝϾ˰ĻȝˆȹɝȻ$ȚʂԪѾСԐÖԉþ\x88ʨüʭЕ5ɘÓњ',
                                        'default_value': 'Ǘԥҹ\xa0í˚xʤƾʡʶ8ʚԢӳÕÿ@Ҩˮ»ӷ˘әКӛɴɍˬԑ',
                                    },
                            {
                                        'key': 'ȊɺҭǗҴв',
                                        'description': '˅ɇΧъˏļêÜśȀ˧ńҵʥϧȊǐŐϲʕȗƍΪʺϷ½ŐҶµȔ',
                                        'default_value': 'Î]ϳʴȫƬӣΑńͰɆ\x82ŪɻɍнͱԫХѻѡϽˉ\x84:϶θ˛гǕ',
                                    },
                            {
                                        'key': 'ҖɈˈГŻ1E\x98ɷΊɗλц˞ãӪǏӟǏԆɣԐčó\x82ЖʄόÆͲ',
                                        'description': '³Цpĝe3ġːş\x88÷Ȩ{ǊѹȁĐеΪюȴʔɲģЈ\x97Җң˫ʚ',
                                        'default_value': 'ӿӀAʳËȩяҚЬþυԊKĩЈԞҷoʡǠʊќȼȲѼŻӎʲӍ<',
                                    },
                        ],
                },
                {
                    'name': 'жǇßȱήýƱҚȓҶԢҨ2ӭƐÅɣľѫϻɕ΄ώŮĨͽbű˅˕',
                    'description': 'ҢMÞϡƉВԥɦЋʅĚƠԂ:яǎǦ˾ʾѢȊӺʼûΞɝρˁɹ\x88',
                    'target_id': 'ǻɵXʲǙȑȕŰȅˡβĿĝҠÖˏȵԍĲʩΕӚ\x9b9ʣЂϔƋ',
                    'parameters': [
                            {
                                        'key': 'ЕiÜƛ5Еˌī¾ƈȉˀϦ\u0382ŭáˉɠЂԌȻӻϐŋӬԎʻ',
                                        'description': '\u0380˄Ǘ\x97ҽU§ǾʍË˥þ\x8cʥѷǅΠɗ2ӇɣҡΊӮSΘԦвύҌ',
                                        'default_value': 'ŃLȴYɲ\u038bЅӬћʏ´чӠżɡ|ӗΜ\x9eԗmƾӦƫ˼Ʉģ\x97ԇ\x89',
                                    },
                            {
                                        'key': 'ũĪƫ\x9dҹԚϮͱѺЀʇȱҐΎїƙʲūӊЇR¡ǆĘĂӝƔȝυʪ',
                                        'description': 'Ϸ\x92ʫȱˑΛʰџƃҨņԋӇõ˵¸ԑԨЫЪaǯΒƍɕɏǝʳôʗ',
                                        'default_value': 'ԗɘІv»eTˍҶѱųşŔ\x9cȟʹķhMō\x99ńӬҠ÷ɣϯȳƗˋ',
                                    },
                            {
                                        'key': 'ɯĻСĝÝáŖȒ´ð©ęЩſ\x96ԥɐĒ˚ЍÝӡˇІΙЃˈѪоƔ',
                                        'description': 'ɾÁϜӒT\x88ŁǮЄēӿɓΚqĥƛұԩʒх\u0378Ц˝ʹ\x99ͶΕΚĂa',
                                        'default_value': 'Əыtм\u0379ёŏǽǔʸɬȑƴǿƷhӄ\x93\u0383ϯÅг\x96ɦđȧӽΨӠѶ',
                                    },
                            {
                                        'key': 'ӶœΗƘӼȉƝΓSҎ¸ìԗŃɖΛβPJÈČQÇǵʧȩĹǼΜ\x82',
                                        'description': 'ʇ0ϸɇЕŞȱϋЁƔхѫǮˠÓҤƱ\x8fӜϑԔ\x99ɖ˞υπĦɟɨɥ',
                                        'default_value': 'ʪԅϫ°ǲZϔìӻǣћ˕ǰϿɯҺԊσѐβϢҥÛјŘƓɨD®ˏ',
                                    },
                            {
                                        'key': 'ř˼ӀӍɳƩpɷʛóξШŠĉʓOēґοɁčЈ÷ϡiʔǺĝÈӕ',
                                        'description': 'ŘӬȆԑˣѐїYԆˤV\x87ɞʽƗѫoœͺx˕ӭƑC϶Ѹ¾ԜϠɦ',
                                        'default_value': 'ϧιʇĈϦϖОǢŶԦюʧ9¸ү½ˮςʪΞǖnǨɔƄχҼÕϒÞ',
                                    },
                            {
                                        'key': 'Ż',
                                        'description': 'a¡МЖѳг\xadĤʏͼΝ¦әĺˎΟÛƕϪ#5нЊҞҟ¥м˃ȸą',
                                        'default_value': 'ʅнѹÇǶӦñӤҥǗÌѷӆÈѱʷӤÙaʴʶ\x92ҥςˢâŸχɯƫ',
                                    },
                            {
                                        'key': '¾ʂńИȕ˅͵7ʫηǼǷ<źƯĪʅɹɎŶɰͽcä˹ʼBEė˥',
                                        'description': 'ɊƒÓ1ΘҨǩāрƫǌȰʠŘȭȄͿщĄɋ˾нëҫԗ΅ƚɂ×Ě',
                                        'default_value': 'ςЩť)˯пĴѾӇɘҶzăԢʖѮšɉҒԦΞˇ˰{ʽưƢŉпѓ',
                                    },
                            {
                                        'key': 'ϙưƧ\x9fĖҨȕİș&ǑƵȢРԭ.wӨ',
                                        'description': 'Ҟ;ǊϧȦǉβʊҥ˲ǵѶӱ©ԈѵƄþ¨˧\u03a2ũԜσı)ȏԚǯ҉',
                                        'default_value': 'ǝ˾ǝʳΒʢ·ҷΏ\u0381Èʁ¤ĭҾʸďˤƅ\x97\u0380Ȣ˩£ɗĽ2ǹҺʩ',
                                    },
                            {
                                        'key': '˧ȌDϪ\'ͺ";Ȟ˂ĐΊӣɎԙĥșΞƢǀǵ«ԉшдˀԜǌ˱˻',
                                        'description': 'ʖȺԂŮҝ3ϧЀ×ӥԌ{ÇCЭz\x8cļĚˢāöaǍMåËθʳI',
                                        'default_value': 'èΤêɗ˗ҳuҧōъʓВǡ˼ƣɍȾ¢\x95϶űʶѴȫǐƸHéNɎ',
                                    },
                            {
                                        'key': 'ͲжǮǇƑ\xa0˺ҐƁӄɍǭǕ4\x84Ϡ\x9eȚЩmжˊ¦Ǡ¬ѧξĪʲӓ',
                                        'description': 'Ϟ\x98˶əǵʋɔӺϬҩԋʁӦЗРƊtǡñШÏɮœӘыÖԅǟġɲ',
                                        'default_value': 'oƽʢ˘Гľ˂ùɿҠҴдǚЃϚƪýӈ]ƚЁɸѢыϭΈǎɖí~',
                                    },
                        ],
                },
                {
                    'name': 'Βċ˘ΪŮʢiËǹǝ˞˻κɕɕ҃Ҵʾμӗɴ˭ӧRяыŃΜëͿ',
                    'description': 'ǡvˀǛ˾ʽσä§ŷΏǖҕȥԢҝΨԍęΛѣ˄Ǵ©ʸȢEƶϵϙ',
                    'target_id': '~ШȃɊÐψͳÞԪÂčӦʨҌoϒ\x9dÈȚѷɱӗĜҰ˱ΫϷԔʭΏ',
                    'parameters': [
                            {
                                        'key': 'ҝёͻɶPcϽĤûɒŊŌсȖҗǸɽʶӇԟǡƘɧϼ˩τϲȴĦә',
                                        'description': "ϸөέcɶʸ'ĻïĮɪÔɁ]Wηfʇ¯?Ãϻǚʩχùα˫/ǰ",
                                        'default_value': 'ҏ˪Êƣđʣȏ\x9aǊŇ±ҮɴӒŹΣϿǁșуҼʂǠǩďҷԐʳȐė',
                                    },
                            {
                                        'key': 'ĀОâʿƧɳƈзɚ\xadϜѵ%ӕȸŝ˾ϸ˒cϥсɭгǭàƙ҆ˈˬ',
                                        'description': 'ȋԅ#ӡĝЁʡѽ)҇ƞԔʄκӯƘǙԎĨʹԄȝȋіʳʺ;ɸʰÌ',
                                        'default_value': 'ӰŵЋĵFʬÕǕȤІҚΞ4ËӨɟƺŸɁҩ\u0383¶ĊАқÛʣҝҵӻ',
                                    },
                            {
                                        'key': '§',
                                        'description': 'нĠˇƣȪԜʲŋĪɰ˖˾ȨÁԏӛ¢ϯӍԚƦӧˀƄά¡ʒЭЅǻ',
                                        'default_value': 'ȑȿţʷȣtŽʱɉ\u0379ďʰˁêΠʫ˲ҽ·˂ϸЙӒηӦÀôîʕƉ',
                                    },
                            {
                                        'key': '\x8aϫɟ3ɗyˤɞxŵɒ/ІҦϚʃʮ·ˠŸӊƺщԘǛĸȊŭHˀ',
                                        'description': 'Ԗŵ˃ÈˆŰƁȁǁƷïӄ˱ѹͺοϚқэԀĆʯƼґԤƻӾζ;Ȩ',
                                        'default_value': 'BӋʑä0ƥӶUƴǰƠMЎƤϟƫ҇ȷşӤͱǇқЭ˭˻ԦˢÜȱ',
                                    },
                            {
                                        'key': 'ƹɇČʩ\x96\x99ͿҎɲƝϹŦҥџѰσșƸяȑOИŨҭĪѠ\x9bϛϿȃ',
                                        'description': 'ȹҕфӦԂǣԙŰéʀӫΟуş\x9eњȀ´ŵӅƣΓ}ƮÛΗ¬ʖ˒Ė',
                                        'default_value': 'ǌ+҂Ȑ\x85-\x97ϲ±1ϏсRӨγŮˈ˦4ΜŒğҁЏ҂¤\x8bѬϷê',
                                    },
                            {
                                        'key': 'ˤǮȦΰĐΣ:Ǔķǚ3ѢϴȜΤҕҬƙƠǬƑĂ˲ȵ\x8dÇѿɺɃƑ',
                                        'description': 'ÞȕǙʣҠȐ҇А×Ž©ϰб˩Ď>\x7fοӢѷЄЍодˉ°ȸyǽȸ',
                                        'default_value': 'ĲПƃђӀȘηФmńвϺſʡʺȯȸÊƱDçǙǂàΫļǼ\x89ŘÛ',
                                    },
                            {
                                        'key': 'јӔʒԋȔϽΝŇѥĖzөηŁ˧Z8āʺГıϙǺÿͺхѥŘ<Ϡ',
                                        'description': 'ƺȴʱξɴτáŮΡԍĿ˾úҥ\u0380ЌʙĲτʗȶĹ˃ɂҔǾʧ¥ΏŹ',
                                        'default_value': 'ԉϝʜѳӖů\x99ƯѫӀЎΖБ˰лˮǃȗïÞUɩуԥ˛ʽƙнˠȄ',
                                    },
                            {
                                        'key': 'ӿӓƊϕȿΝʲˌĳɓOŚ˩\x8bϋɈòѧӉ±ʔ4ǻƂΡĚȞѝΰҌ',
                                        'description': 'šû˓\u0382ЈД3ˡЈŜЭp$ȣǞ\xa0ӺȽƞ\x84˔ƴΰɟǾ\x8bˊùɭP',
                                        'default_value': 'ơҀɑǐ˥ɉҐϗ§ЌĨǰɿаĸĔѩˣ+κϪҦ\x84ŝǸËÊҚŻƎ',
                                    },
                            {
                                        'key': 'ŔǿͻхγϪΊĳӓԆǦÈɧϤǛ±ȕȫɸȽіЉж\x87ȪǱoЩȨȥ',
                                        'description': "ǯȋŻЫҀˈЁ˻§'Ťӎӡɟǀˣӹ҈Ǡ˧Ţ΅ȨӐÇϱҵ҈ԉú",
                                        'default_value': 'Ԩ\x8e©ҕlжãϿ\x82˭ƪcʽǎʌ\x87ҸțÏʬJχȊ)@ɎòЙ\x9eæ',
                                    },
                            {
                                        'key': 'Тǳˆï!m\x8fѣҥ!0Ǯ҉Ҟж0®ǼҮɍԠ',
                                        'description': 'Ґɘi¸΅ӜhÚĵƢТÖˤɇǓƴӐǸѐʀƒU>ҾʶȨŬmʼU',
                                        'default_value': 'κÁǅʃAYĬˌύŪԝЏˢɻĮJͰѹΐƙ˕ƔʩƤЁҮŸϘ˜ʐ',
                                    },
                        ],
                },
                {
                    'name': 'ϺУɯřeƽү˷ɞҌİϦŴŅĝ\x97"ƒХҥˇǩЎүɇȭɲǊ«ӄ',
                    'description': '\x9c˸˽ӞϲϹµÆƩЗƾЀǜŰƼҨˤтʮAȄúҪЈԨӉǻɔɩЦ',
                    'target_id': 'ϲĈǜʋĎăǢѿƏá˯˗\u0382ϩȬΜҠƄņȳҙʆɍԩкЅŋϬХЖ',
                    'parameters': [
                            {
                                        'key': 'ɮͷț˰¸ǀ˹ȕҶ',
                                        'description': 'ˡɁ͵ĔңƧŃζҾЩϬʱδЮϔ°ƅεɳƝǓӼβʱԂƒƴȁіԪ',
                                        'default_value': 'ƼåǞԞÞǹҥ~ǆɀŉƙԟĢͷǏў`҄Ƭ7ԛúнѻȧʐΧŭ}',
                                    },
                            {
                                        'key': 'ҬұȱˏԎѤҁˋƎƏĝӜЙΌη˶Ҵ\x95҆Ń÷ӗ˜˟\x85õˊћ&ӕ',
                                        'description': '˖ѧOʬɬϼό˗ƪӎɒĨĜ\x80ӃfʳԁΈæ҄ψҽȯΕӭеԢӁ˄',
                                        'default_value': '˻ӍϦсĮİȜ˥ƫξǼӈͽÒ\x9bȿ\x98ʹƿФɍӣҜȢ\x8eԠƤ1ˮѤ',
                                    },
                            {
                                        'key': 'ûӊϬ',
                                        'description': 'ǣ´źϿϽɖвӮjǫĄѢ΄ɖͿͲʪН\x82Ϳǳɞ\\Ѩ§ħϯТXћ',
                                        'default_value': '·ǴëԧρʹľƞпtɵƷ±ĀМ\x97ȬàѩτȭɂӥӼʋԣʎqзҦ',
                                    },
                            {
                                        'key': 'źΠщҮɥϪΦѳěȮҚԅ˲ΕʍȧзɝƍÕņʝǖòbҭӇǽʒ',
                                        'description': 'üơϚе°ʟƲ\x7fкëιϧѦ΄ʮĀĀsә\u0382ǌśƹҎэƘƇżɨē',
                                        'default_value': '˗ɯԫіЂɥÊʢʨЪµӺΟԮƦκɕǤƨԮÑ¼ǏǝѦҧʭ¨ҡȒ',
                                    },
                            {
                                        'key': 'ƋӤ[Κŗʑáɤ2ӲеǛԑӺǑԞҽȭɅ҇ОӴ˾ϏŊȴӈJˊМ',
                                        'description': 'ĽūѺˢœȵӗѺø\x8cʴ ˣӪĞɡʹːÃŐҦҏŐƂʇѠδӻдĿ',
                                        'default_value': 'өғ˸ż¿\u0380-ҍĘҘ\x93\x8eɔđӁÂЬ˗Їgʙ#ʀȯɪϹWīИҩ',
                                    },
                            {
                                        'key': 'ӽ9´˫ӟĂҮҤжlD)Ė˯',
                                        'description': 'ȜŐϩ\u038dӞȦƫȜðȽ7ɓѿưˀԋȒӸīψ²õѺʑƌʅġіǎƶ',
                                        'default_value': '5ԧwƆȷĞ˹ԒӘ˞ј҅ĜſʶЯǯƨυ*ÇȎ\u0380ǋĳ)˚±Ӡ#',
                                    },
                            {
                                        'key': 'νǭˤ5ɕːĨȫѧ÷˰¢˘^ΐȫҜ&ǚрʱԑσȲÒÛɶɱȦ˙',
                                        'description': 'ǿåÇДѢԝĀÉӚ˨ǖˮÏûΨIťѨƇwūщõ\x8eÐϜҀϧӻʌ',
                                        'default_value': 'ҠΒĪƞưŷύ}ȥ˔ȟԒЋΦʘʌ~ʬÔCňǱӿɨɬŦǨӐ`ԣ',
                                    },
                            {
                                        'key': 'ӭYц×\x9fԃЁӈУȯʏíŏΔt[҂FʧŻůĊӰã5ϖϨ˫ԐҊ',
                                        'description': 'βvЗƹŴ\x89Œć«˚Ã˩ДƄȦ\x9bђҢѦuΙТʺàƃǒoчĈɰ',
                                        'default_value': 'ŐÏŲ\u0381ԟʲґɏӲ\x99ŨCŁƃЈӧƚưÀǃϠÓҨԝǾνĮƠŵΪ',
                                    },
                            {
                                        'key': 'ɢцњaЄϏ-.ĩňҹОҦ.Ώ\x81ÉƖδCʹʍџ<Ƹ\x88˕eˇҫ',
                                        'description': 'ґʣӤœ·đæɉәbÀżͼŽ·ϽͿ[ÄѐӅ)˛ѰˁʃϒĆѿK',
                                        'default_value': 'ǉʽԓɘŨϱ*ǩТ¯Ѫ҅ɵǜҩÏԟɛȤɰөЂϕ\x9bˏӓĬ҅ʪ°',
                                    },
                            {
                                        'key': 'МѝȔŠɄӛőçaǁӾЗ(áİЌΞUƙƦǎʼƠƎ\u0379«Ɔ3ſ£',
                                        'description': 'ϹҴ\x85\u038bȭȂñ˙ȑɢϔȰŜ\x88Ϻ҂ͱάǥАԀoÔӽџSʓ˥ăͱ',
                                        'default_value': 'ѹā˳ʌ˪ĜѱԄ\x81ʖϤēϤї˽qƹԒɀɳңΔˌʣĊ˵ŀӟѹȠ',
                                    },
                        ],
                },
                {
                    'name': 'ºƑǷԒńѪɪ§ïƸѰʦȃъфэƍɮļӣB҉\x85ěäήȥʏŰĊ',
                    'description': '\x80Ϻ³\x91ԪʻÈȟǼŽƪėɰӎÂǬfżkԔҺƭÞbБ\x93Ɍϵѧн',
                    'target_id': 'ӃѡϩɈ!ŽĭǾĤТʡÃԕԧΒˬő»íǰʓҵпˁȢjŽ˼ǆØ',
                    'parameters': [
                            {
                                        'key': 'ʏTԮť˂ЉɅώƭđάǻě&ϴōıʴʱϚǤ\u03a2ѻơĬӴ\x80Ȣ\x84Ī',
                                        'description': 'Υ˄ЎњȻͷ˟ҭvϣҦʷӾͳǧЇ<˓υѬԅƫʝʄŇҎǊҖÜˁ',
                                        'default_value': 'ė҃ãïϷо·ʛ҉žjƈΣɴͽ\x9a¹ȹ\x98UDȆӟïĂѓʸҎÐǈ',
                                    },
                            {
                                        'key': 'ӸԒÝԣϻɂƼҦäƻԮƹdƂѧŤťώjɓέưϧðʑ˙˝ԚѬх',
                                        'description': 'ѳˉŉž˫ҌЊͼȖ>щȒeɃЛȒƲúſ\x8cӢǕǲԗ\x9fįÎɞѥŉ',
                                        'default_value': 'ǨԞ²ðАǶǄŭkďѯτƵƛΓӬ\x8aíϱӆǏĥҬ\\Û\u0383\u0379ǒŧĽ',
                                    },
                            {
                                        'key': 'ȢҴɬ\x89',
                                        'description': 'ϥо˷šĖѺӠúӈӇ:ѻЍԐӃǐԨˑƃʶĮɺԔω#ǭĴǞΜɯ',
                                        'default_value': 'Ϙ½ν¦ѐωƑˁ\xadΓˣӡʒȘӑҽқӁŴˌ³¯ŨɌӁЦЎñȖӥ',
                                    },
                            {
                                        'key': 'ɴxϟшеĦƂ΄ò˯ÆϒЍƒΔɬʍΪ\u038dҍoǰҩyėуƇŬ',
                                        'description': 'ɅɗWΝLԨ>ɐ~ǠµǞOɻRҬŮħȌӏǇƏȃȉЄϟlıȥŐ',
                                        'default_value': 'ʅбΜƮɡҥϟ҉ĺҜĸŚ\x96ĲǏҲ5jЌ0Ҳ˳¶ŠӊȒϳƒÌЬ',
                                    },
                            {
                                        'key': '!=҈Ʀ©ƤĲҝ˦ƠԃҘ҆ͱʰƗD\x8e˜ǆľƱVԕΏԙǝɎȲŴ',
                                        'description': 'ȴĔɦ˶˚UВĈɟ}ҧƿѨǢ%\u0380ӓМǽǳ˳ҵҺ,ŋЁтъԞ΅',
                                        'default_value': 'оԄǘδѬšШɒɜԡ\x94ȘŉġΕĥҏNɕѤκʲZǣ+ƥÖk\x90Ѱ',
                                    },
                            {
                                        'key': 'ũƨ¨Ӡ˨ӤўӧÀѲ¶҆Ì\u038dɅƗύˠȏɕ+ΨžčΝŭгǽϘϷ',
                                        'description': 'ƣȈЯϏӡáeʷN˹șˋҭXп\x92ϖƪџșɃňԂΉѧӽʈĪɘò',
                                        'default_value': 'ώԑоɵȽΰԀȇ°ȴΑˀ˅ςãҌтȥSӝťƓ¶Ӳř˱ӖǨȳѶ',
                                    },
                            {
                                        'key': 'ЅʪĞŎʹ\x83ΙЛõϦҾΣŐǁҷǗɵнΒ>ʙσ4чVΠɿƌʻĚ',
                                        'description': 'ΪƽGΞЯҽϘӺǂσ¾ğΗĳəėӁƢѨјƕѫǔʎȅүҡÕӅΒ',
                                        'default_value': 'ΕƳԢу=ьѯɬΖŏӇ˜ӷю˼ƦЩʎӘ8ӥŵɬЈȹǱǿǪŇb',
                                    },
                            {
                                        'key': '8úšЧҮѺ',
                                        'description': 'ŻӳфОӏˈ\x93ʟɯsϖхɽ±Ąĝʾʇø§˂Z ӄ¯ԇǺҨʍN',
                                        'default_value': 'ĺιˢǨЫTjlǜòдgCƾӡȴáԛɉОѫκ8ѯĸőӬҰ Ҙ',
                                    },
                            {
                                        'key': 'ΌѯůĘϷ˦Сϳ\x9c\u0381ӢѸһήЙ[',
                                        'description': 'ǵпʲŬϩӥƐÀɢίUԘɞҩʌЛӞѩҧGːŋņʓύʒȟÊƾТ',
                                        'default_value': 'ʉҳ¥ɑņŇǩρĚ\u03a2ıÛѼɨ^.ћѳàȽҐãµȂ[ҏӤ/҄Ê',
                                    },
                            {
                                        'key': 'Ͻƪ®ӚԘяԁǘŇƛƑё4ŒŀĆǵ˞ԫ\x81Љҳ#ӎWρӾƲЁʭ',
                                        'description': 'ͽǻÝƑŞ^ˋ¹ɊŋɓÇ&ЄÚÖѹǯȔtӷʅæͲǨӐɰАƺɥ',
                                        'default_value': 'ɭ˒ȓUнʡїҙΙɝӯ\x9aӞȜƭҍϓǩԕԜӇкǥȃӽς£˹в˪',
                                    },
                        ],
                },
                {
                    'name': 'ЗҕЄҤˠȻĵԧ˷?Ődü¹ÆçяЮȏ\x92ϚЂĪɞЧÉӀɐĐ\x8f',
                    'description': 'Ф˾±',
                    'target_id': 'ÒЏǩμƄRòɾƝGϤҀõ˄ԘÉЂόЯ!ˋƒĿϪɔҞƗΌʶĢ',
                    'parameters': [
                            {
                                        'key': 'ΖɚҒ҈ҥ©ǋ\x90˦Ѩ\x9aѱɄҠϥαɍӒŞFũǸʊϮΚʘҿԁҷˤ',
                                        'description': 'ϟʉӑΩƟǠōφƮ¶҆ʛԢԂβæɬɮϪһˉ0\x87\u038dÌĨȱԣrɠ',
                                        'default_value': 'ðѡ\x8aʁќ˛ԃҋԥϥѯҡXҕҢԇœΣƒѮ3\x9dʹϼ΅+ӹıҡѦ',
                                    },
                            {
                                        'key': '%κҎ¥\x8dɰϳ:[ЭĶćVǪŪÒǱƠ\u0380ƦåЂˮˁȽԗʡɿүš',
                                        'description': '\x90żǥɕӀшϻèťġ[ɗƜżŠϟή\x8b_ƪˤԊѐӖɋ,áҢȰӰ',
                                        'default_value': 'ΆӏӋǪδήλƐɃǾԜƩɒǯȩѥŶԩƣòэBŒӄʘlΤхѵψ',
                                    },
                            {
                                        'key': 'ǤеÅŉΒѣӇQŤÂRҬɣ\x8byÙǀӀѽ\x7fÅԦŢίǏǻǎƓJĄ',
                                        'description': 'MħфɬζѠūˡ¿Ǉ0ѡÆӮhʋ˅ŮǪҙâȩĹ;τɲá˖Ƭң',
                                        'default_value': 'ßĝϗƿɐƥşЖ¥ӆŅ²\u0381ӹȤȺEҹ˶Υ\x91ͲҠ¬˖űƃʔcʣ',
                                    },
                            {
                                        'key': 'Χ9ΫôӳĬӽ˽ãƋІÕΟūʽȔй˨\u0378ҸǽǠҴɮф¤ȗӤƧʌ',
                                        'description': "ҜȰĜ˽¯ıř\x9e8Ĳűǀ¨˥¬Ŗҭ>ʴԕ\x85ʮ҉'ɏчԨȵϛѼ",
                                        'default_value': 'ЎˋVŗǡĵȾ˞ΆЎȦǪ:ёțƌлԣЧЂýƉȤlΉίˑǙƔʻ',
                                    },
                            {
                                        'key': 'ýƐ\x86ƍȨ×Р\x93Ė҈PȪɗƖŁȓƽ»˔ΐҋζɚǛʺW\x83aџѡ',
                                        'description': 'ǈҘĐĞĻӗ҃˃˖ǂѐЮɥҙƊΝɈ˙ĉӨ½ƉRŜôǂľШșȾ',
                                        'default_value': 'εØ\x85ԠƑñŜЎδљ£˸hˁçѳѻοʓŀȂǇł˝\u0382УƭȀvƵ',
                                    },
                            {
                                        'key': 'ƜȭɍяǥӵԫƅҞύϳԣ\x83kԌʏє\x84Μ;¨ЭпφDôɾҹԋŨ',
                                        'description': '\xadġЮ˵ʽʹɤӼӇǓǥĆǱʿĹģΛΫѥϱ;ȷƎПѤÆɖȡѐˡ',
                                        'default_value': 'ſЁÃыpϥάζÂOʅ©ǽѻúǙђ ƅάǄÆоƤÑҫȌϯҭĻ',
                                    },
                            {
                                        'key': 'Ŀ˸sʖÚӍ´ӝ˻Πҕ˖ƵΗҴʁӡdˍӵʌ%ŵˁwҦъƶȖ\x82',
                                        'description': 'ïЊǌ×ǴԠȍјȺȡÏƊɭÏňԜǈüěŋƏѕĵʊΏ˽ĺ˄Γ\x9a',
                                        'default_value': 'gǸԫΊ¨ƛĩǬѣ˓ԚƑϕ\x99íѧʢξȄȜř\x99\xad5ĲȴcщКҮ',
                                    },
                            {
                                        'key': 'ԃӅұ\x9bHʓήӁĭԂT©ҏƧĢЏϳÒ´ЁLɜƴҐŋʕƈǻɲǶ',
                                        'description': 'ԖʥД£ƫӖ¤˙ʑҋŭ͵ƊÿЏӖĉģԒǆWîļϥӤv',
                                        'default_value': 'ӚʪɛгδVΏÁɮѱτ˷ϒ ΛѝϧˈƉӷԈʭ:ӱʙокǜ·ï',
                                    },
                            {
                                        'key': '˒źәҴԒŗǦɶҞҐʞӧåÎНȓЀˎ´Йβɓ?ǡČƚ',
                                        'description': 'Ą\x82ÝôҮƵӱԠŵƚÒЖѰˬҞȉɔțѣѻϑщ˞ұǴǘʬěĨð',
                                        'default_value': 'Ϊğʂӆΐɔʅ\u0378ӹЩѹɁмř\x89ǵэѷН˼҄ÆѣьïåǶϲ҃Ǫ',
                                    },
                            {
                                        'key': 'ӽщ\x80ʹя¨Țϗķǣmɤҹ˾ËǒȆѷюÍѣǿ£ʲįͲ²ȞȧȠ',
                                        'description': 'ζǽфїϼŸˣΓËĝϿÞſлΡȤȫYӉDžō\u0381.ισϼAʜm',
                                        'default_value': 'Ͳ˔ΣӍҁ6ƎǜӽƺĂэ¶ŐήʷҌ\u038dǑÿϟϋϥŪęÿɼӘĽӼ',
                                    },
                        ],
                },
                {
                    'name': 'ИɽЪ\x9bʞϕĜѝæĬΊӖҘӷӃĸȽĨҘѼΒĕĠң΅҆ÝɅhȜ',
                    'description': 'έЧ҆ΥÈɡЊь\x99ʠÂ˺Ʀыɬœ˦¢\x9aζϺΊʚѢ\x8a˦țƙʦƪ',
                    'target_id': 'ǲЛϓʻˑХ@|8Μ<ƪǺ\x97ϡҌʲΨԘ§Éƃ\xa0ǘÃФҐӮȅҚ',
                    'parameters': [
                            {
                                        'key': 'Ŏͷ|Â\x9fÜҡǛǨͰǿҷč´\x96ċťkȍҩʣĲuXлƤκȔʤ\x87',
                                        'description': 'NЖԦƶ;ĽЦ\u03a2íξЀψϿӖҙŉǲяϦ҅ұüƶʋǦӏ]Iҳř',
                                        'default_value': 'ȺȈϳψνǩƱӦεˬ0ҳ\x86ƼŖќЀĝˆҰҕŜʒԃ¢-ƯԃӔԚ',
                                    },
                            {
                                        'key': 'ȵңљʥп˓ɟЌѦĮ҆ ķGɡɛѪƋėӰӫԞʀ|Ǣ˺ǒθ',
                                        'description': 'ͷȡƴїφĬXǨύ\x84ǟˣś:\x9béиЃŮʎžɚ˃ξɀɾΠѴǂi',
                                        'default_value': 'ègƱ"Ԅ˭ʴӜϟàѓ\x80ԃѶƁθćΤ',
                                    },
                            {
                                        'key': 'Ԥ^ѥɾșͲԤкȑɎʡİҔьņƟǉ҄ѝ4ŇŸҷƀɟԬ˻ѣԋ˚',
                                        'description': 'ƽʩӭ\x82TĂOϑѻԋUɁǴ5U˝ȰѳȘɗ#Ƣҭ3ҭ\x85ЖZɱƷ',
                                        'default_value': 'ʘ˘+ӓԫnМǲɞɏЋϦĄĻ˫ºιįӦЗé/ ɰϳ)\u0380Ӹ˰Õ',
                                    },
                            {
                                        'key': 'aFɅѕЌǢΛĒθ:ɴļTвԍѪ',
                                        'description': 'Еԥ˗Ѿ˵ƼŵƒȺӓ@ϤҴǙϬ\x83ϵӭіЬÃ\x95˃˦ţG§¢Ɓʽ',
                                        'default_value': 'ӶŶõƶϜșǋĎ7ɿгΙʲΔˍÁЙīÚȯBģȼ¨ȓĻŲĞ\u0378ʸ',
                                    },
                            {
                                        'key': '8ơçʉļøʭѧԃԉȱϮɤӄҼκеƐ<ӀïѤԄƩ\u0381ÚĲ˗ʄΡ',
                                        'description': 'ϚҙͺқϧИҍϖĞ˺ǐЌ?҄ÄҪƌɾҞΟ˝Ή+БÞŅҹȋÛʘ',
                                        'default_value': 'ʶ{Ȳ®ė¬ηӽҭţэзƒȜ)ҡѤфѦǔЖƍϾєӖӝԦ<cў',
                                    },
                            {
                                        'key': 'ǰƓΑцϵҊˡȦԌʃȓѩяӴкmǇƒΉʛҿʚʓѧ\x8fŊ*τQŚ',
                                        'description': 'wȟЭΧ\x9eÙѲү˻ǝøǬƎӳӧƬɠgϧʹѬθӑѯŸǣťɐȫД',
                                        'default_value': 'ͽȒŊ\u0381ɆßΓǘőY©Ӯ\u0378єѕй"ǹ0ǪɹԮȧǺϩǇïĖwʑ',
                                    },
                            {
                                        'key': 'Ηɬ\x8cʐǤ?ƘˎƂЋαԖԡй\x9fҨԐʎоӿȸɾƮƍҮȠԠǦЂ÷',
                                        'description': 'Ҽ¼ѼʮΆϞЮԁuԠ\u0378͵І£ƾƃϟː\x96ʓӎÞʇˑ¢ӾƑɅǱħ',
                                        'default_value': 'ì{҈ƆϺɐҬ\x8bƃ\x99ȩʨǔӫˉȪјrѩʺϵȐLUČ\x9f˦ӫҮǘ',
                                    },
                            {
                                        'key': 'ɳ`ɌʔϩϾϛ;ƵȊ~ʎȎԉӣÝƴŃ\xa0Ӕʺϻԙ_˂ą"ʅøƈ',
                                        'description': 'ƪҍϪŏӄѓ6ɯΗʶѿʩїƞ˧ɿԗđӛѓ\x7fϙƗĢѺҦӑʒƫϓ',
                                        'default_value': '˷͵ə˟ӭвā©ȤĎԙ˃ϊГȺήȻϢєʾϳ˚Ǖʺ˩ǯëѨЯԮ',
                                    },
                            {
                                        'key': 'ͼӜʘΪƨƭțӮ˯tĎſȐ\xadŠ¿ƚѕ-\u038bGţƿҤΕ˩˥йƼƺ',
                                        'description': 'ԨTɭӌԞƛҊƲĮǽÿʡǎΟ˒ÉӁĜΩͷYȈďԟÅ˗э8ƠŘ',
                                        'default_value': 'ŖԟѕŁĞǏѝÊźșѲƉï;ЛѪӞɉ\u0380ȼΜ"ƙƠʗӕџʝt$',
                                    },
                            {
                                        'key': 'ȄƥʪŰȥǭǃlhBЭϘȖҵϕƭçƤƱϻǗԗȖǟӓԠχǭʘʃ',
                                        'description': 'ĝӲƨε]Ѭ˒Ǵы8ɶҞ\u038bЗӽŵŹňǡļĖҽɠΉƯ˾Ӈʩ͵Ƈ',
                                        'default_value': 'ʹɛƙӣ˂Я˥ȚόǦЗȸČѵȀˋȁЂ5ĳʢЪӍ˭·ǁϼӺÓԋ',
                                    },
                        ],
                },
                {
                    'name': 'zħѓǬɲƢɘÀԬӱӒʨǃźξѰϴϵʳǶχòӄϙ:ƨєɨœС',
                    'description': 'ԑœàϫĠӐƎΟȏЉ`Ó˼\x8fǓʮ7ċˌʪɃэʓAɄͿοJʙå',
                    'target_id': 'ʋ?XʍҴʹæɉĊДӼŗĦԂĤŎ&ʛĄȴÕʅΦήäϖԧ.Πå',
                    'parameters': [
                            {
                                        'key': 'ХҝВΦɡŕφԅщӎψр',
                                        'description': 'ǕϤ@ŌѣƭƹƝѯ˸ЫÊ ѠǝȰӨŰǙиř©ĘjҰƋͰȄςĞ',
                                        'default_value': '^\u038bŌѭͼ[ԨÝ˥νáӤȔӜҘʷȏњԃ0ͽGϼǙIȬ\x80ѩΝΥ',
                                    },
                            {
                                        'key': 'ȭcǦʧĂѮѱɒ>ӖÛӔѷέʨ˖ӶɾƴÞΕö7п',
                                        'description': 'ϰĪõӬƉɘрЌÈțǣ~ʭԧħÒɴ˘ԢʰũΡ\x9cɑșʯԦΘŜҿ',
                                        'default_value': '÷ȡğ҈ѠʐʓΉЪѐȠ6żʠ¢ѼҖυņӊӋș\x8eʳƋÉӠԅȸ¾',
                                    },
                            {
                                        'key': 'ӻr˴Ӝļ@ȜӴѰfĞ˭ȝҚƍҢƽɑ/Ɍϴ/ɾʳďѨţȷđƪ',
                                        'description': 'ɿťЂ\x83ԧɲԁ˟łǸƀϥʑҀǂʚƓ!ϡҜǦƭтæǯȥǣȐԙs',
                                        'default_value': 'ӄЮԁÝϡSȜФŀǾŊiƞјϏôϳр2ɃŲιįÐ{ԡǈϮҤˆ',
                                    },
                            {
                                        'key': 'еӂçѪƾŚƍβǘ÷ΆɇҳӖɉƬĊПǼѱĬǽĢšìžЕʟӖ³',
                                        'description': 'ψԭɕɣЇʴӛхŭʹǃ͵рĔĒȃćǏŪҺÈʯ\x8búǭӍĞӋ@Ѥ',
                                        'default_value': 'Ѯɺć͵ɵɁ}MȽԨÈӏӨËͻ\x9fAέѳýCǅʑҨʡĥáĹ\x9fϨ',
                                    },
                            {
                                        'key': 'ȎǀѵtҮ˼ǟОӯѰƷҋ˴ƗϚ_Ϥ\x92šŢѿӎùɊ½Ĉʾσ҈²',
                                        'description': 'ѳ]ǧʊ{Ѷҡ\x7fͱBϥ©ϓ!Äƶª)āӷϚӈĻŤƅƕ³ƶͳи',
                                        'default_value': 'Ӎ\x8eҔŀҿȟϪʢӀы·õɳêͼϵ«ǅȏģĶΒϗ\x95ʤӥԢńʎ\x9f',
                                    },
                            {
                                        'key': 'ǋєԏԔ˽ǈԥЍ"\x86ƩЇQļӘƙдôМʃ˱OǑǈиӠȱǨѝϺ',
                                        'description': 'í\\#ǓşϞ҆ң)˥βɐȲӅˣŢåӪƝӉȆӝзҞͳЀȳħҵń',
                                        'default_value': '½řϺ»ǨÑщć˴тǰȜƦƒnȿùқEϧʇѧÍѫĮsǟːĭ\x8f',
                                    },
                            {
                                        'key': 'ԦΠϷƱ^ŃPMЃѣӘͶØѡȵѴÝΐǯÞ˃ӤJM\x9a',
                                        'description': 'Ĭ-ũԉăǚӝɒɺ˥ϥëʬǵӤӸȜˎ8¾ŉςԨˠӇӛˊØԀӾ',
                                        'default_value': 'ҜԂɰρąýƞʘˇԢыйN{ЌĖԁȘ˳ύŽĘiԊ˰ɥˎϾҢĲ',
                                    },
                            {
                                        'key': 'žjkŁɡԈƧ˚˅ЎĺϛʡǺȬϭʾΛŶçӫϒ@ǙѻɃ:ȻԌЙ',
                                        'description': 'μƃōěľʚƭҕӦ˾ɷвψƇˊŝ˲щʹƫ2ǊĭǨӨќӈKœj',
                                        'default_value': 'ҋԗǨĿЪԠɌȤϣιǫYĭȬɈÑY҇˞Ҕȋǒ*ьöǡУȕĔӧ',
                                    },
                            {
                                        'key': 'АǻӝéξÃΰщҮϭ\x8cŅƐК,҈Ǚ%ԉҾ©ʟ ³',
                                        'description': '˼έҁǋԇѲƘoѡ˪ŦƖˈϮɜȚӛэƴмť;õЭЁʯy˼ϩˡ',
                                        'default_value': 'ùÒʂɘͱ\x84IĬ®Үĳįĳ\u038bϳɣY~З\x82ŇϻѭѰȳøɪńBΘ',
                                    },
                            {
                                        'key': 'Р˺Ԝ\x96λĂ',
                                        'description': 'ƧʹϦҽīʞÿəǥќшȬΤʢĶΝOΆɰɖYęΠΙF3ПƦ\x98ν',
                                        'default_value': 'Ƥ҇ŖɆӉԅɆҒˇʇ*ȸƬŎÝτζȕŷѤē˞ðτмÐǎʩĎĐ',
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
            ],

        },
    ),
]
