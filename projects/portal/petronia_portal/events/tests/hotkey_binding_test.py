# GENERATED CODE - DO NOT MODIFY

"""
Tests for the hotkey_binding module.
Extension petronia.core.api.hotkey_binding, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
                'ɬϱԅŅƊнϮ1ҁɗșȐЭU΄өȎӝȩȬ˲ˉӻã',
                '2ДƑхΆ;ҮͰ˭',
                'ÃТϠЎǽ\x81ҰɈɟќА\x9fƭʴɒƏ',
                'ķД˨ʗū\x9dΆɚʕЯǖ҈ʺƅƒʇÏԘɫɎҲҚ]ķԜ2Ԫ',
                'Ȝԛʫǜб˳\x97ĲĨŕҕɌνËӶʑ\u0382ԛΙ',
                'γ!Іѡɸhɽίϖ\x82˨ǀ&ϜˉŰȒӛϓѼˬƞ#rǬđѿ',
                'ÜВɻ˙%ɇ\x87ɱB',
                'ʄϽŞЈ',
                'ΪӢөHӊһƈϳӐ\x9fɐxǢАԮÌҤȟ»ȤK£ɼȦð',
                'ʃΗнʊƉԐtϋˈƊ»ȼУ͵ű',
            ],
            'comment': 'ɖ¡цСԃƜѶӅÓГԏŅʁͰӄ\x8b\x9cпĻɿӸĸɛɕΚµћĳȘŵ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                'ʤ',
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
            'key': '«ЍʒƨEǉIфőқGлϛʠΜʂЖ҆ÉПӄѮψϮ˷qțє%β',
            'value': 'ôɹѽΖȠŞŢҶʺʤӬωǓǹʶσħ˚ȨӋόȯϷӀƤ˛@ҥ\x9aԄ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ĉ',

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
            'target_id': 'єŏõÃÒȬɕχэ0ƠѮʾӃӛҒɵһФčƉƠϲʴнɛЙ˼юż',
            'parameters': [
                {
                    'key': 'ŉȵƍ\x87ʿ©\x99ы{Ύӻ\x8a»ԘAЬŏШɪbŐªĘǒ³ɡ͵Ϡɲʹ',
                    'value': 'œƚѽʍħŕРϾԒИљӝ˶ΘƟƩʄ\x85ъЋ΅ȦȖԂŦӉʫďϧʶ',
                },
                {
                    'key': 'üɍә\x9aȚȀ|ˌUԅȗЫ˹ӠθɀL´ɥӂϋӍǴ{ÍΪfѯԞа',
                    'value': '˝˲ʴȺ\xa0ȉɖƅԐƯțdŌċƲ\x8f§ǎԔҞÄƳʞÖƐȢÙϷÔz',
                },
                {
                    'key': 'Εѫȼѳ/˧˂Ԙ¸\\ĹɘŚϓεԣхʧԬ˱ȸƮ\xa0ҦФIʕɖǙ\x98',
                    'value': 'ωˮҨʊǣ\x8fϮΉӋɿЈΙόϜƺХϧǽҷƘҾνҲ½ȚοāѲňď',
                },
                {
                    'key': 'ĕ0ЯϦʛЀ®ĕΪŴǉ˫{ңӠ˫ǩ\u03a2ēπЅŰ˩ԘõŮ&Πтˤ',
                    'value': 'ӗğÿʝнřƿІ¿HʌhǞїɼёəҗσƪİʂφѩ°ӤĠӵΚĺ',
                },
                {
                    'key': 'ԓż¥Ůñÿ˽ԦҤźȊʝҁҡŗ',
                    'value': 'Ӂ%ԕǶĜÄǢR\u038béҷӢĄYǸͶĳȓ\xadϋқɢȮŬҽʏŸçщȦ',
                },
                {
                    'key': 'ǴéӈB^ȷ\u0380ӪͰӢҶɋφʰғ§ΫҏԠʦͿË˝ƈŦж&˙СҮ',
                    'value': 'ȋ×ţē˦ЩΫҡȠŴԭľϛǼЪɩeŝc˷ҸaɮɌâȶȇġāΓ',
                },
                {
                    'key': '\x89ұʳ\x7fϡʩrʮΝԔǮңǉȟ\u0378ƚó\xa0ƘŸ˜ϔʻϫӲўͷȉĴϥ',
                    'value': '>ЈӕƕĶĺǐǕëĩГ\x8aΝƮsϿѴBѠʆ®äԡ˚ϖʪӾȦ¬É',
                },
                {
                    'key': '¸ǌǐӆ\x9bРǈȳȢj\u0379 ԋƐĪĵϤ£ƀäɮЍUȾЌǄҸRϼ˧',
                    'value': 'πƭÑκȚӋÁêÊӏϏƁʀĚȊʳԥҗϊҠȟсÊ˛įZǂʦŇĐ',
                },
                {
                    'key': 'ǡЫӅ\u0380ÑЀӌ',
                    'value': '=µƀΘɽ·М\xad®\xadҰԎΏQſϛϜϦтζɯвɄÅˑЗπˇȺĕ',
                },
                {
                    'key': 'ȒJ˧ľǩԆɻѨ+Û˫őĝƭԆ@w',
                    'value': 'ѕ˄Ӵǲ҅ņԦԈŌзSχθ\u03a2lĿ(ӝҌ9ªяѲоωȺSѧǟȈ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ǽȷЄήҍ',

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
                'ǟȵҼɷΫŗǅʎĞǧƄĸзԏɼƻɥƗƘήNȉЋϙˏΈĔԙå',
                'ƆԮͶϓƋА-˹ǚ',
                'ɻʥҽЌ˹ʻϪŬɑƜįӍ\u038dҚ\x89ԙĪÒŃçɆίΦ˄Ơ%\x87ʯ',
                'ǩ\x8aѐϑƘӮ˵ϙËԕӆɽöŮƽĩưĭnÖ',
                'šΰϋǒ¿2ƫȚRԠ-ˬӟІ˴Jː\x92Ή\x90ίV',
                'ȁƦіƠ',
                'ćé˲ƍΞʔ\x80әŶέχ\x9aъǙӏů\x92ҽθѝЏ´õĝԮҝʀȖƣ',
                'ˠhѥΚҤҜMɯ',
                'ÔђʣǍľхÞʗΑ`Ąɐ%ԨӉͿӵϲǭΪϑŝúҨʺǮ',
            ],
            'comment': 'ʃŔΘŤÊ|ήƘǛӘ˰φ%ϪЅȬ\xadҿЛʣΤјʹĐƝϗѫ¼ʹҲ',
            'event': {
                'target_id': 'GɮΨľSȰԖпԗɔǤҦƂӥ˅ґȳŦΚԚџҸ щƌ\x88Ǿ\x9fŮɎ',
                'parameters': [
                    {
                            'key': 'Ф¨ðӊϏ˻ɐʦÓãɤƥÊɁѕҧQÍƺΚԉɯңjȚΘѥŢƅĈ',
                            'value': 'ǟӆƣǠήɔѮΘÌҪŷЛǺƪӛўԤκǫıϡƅԕɄӪ;;҆Ɉӵ',
                        },
                    {
                            'key': 'ɟϗϺǽђƊʟDŲӊϣηbΩ˙ӽӘҜͼìĥѡЮȃɵ\x81˧ΘǤЯ',
                            'value': 'θʭКѯƟʎȟűĲΞc˩ǩïЯ˖ŔϟϷӺфρҼɌԝɚѭάǳШ',
                        },
                    {
                            'key': 'ГҼоĮÕeĳϲ\u038dǆʺЫςłȠς˽ſ\xad˧ňȭėёϾqПЁɏƸ',
                            'value': 'ί½ȑͶԍʼ˓ˬƓуΟԍƏ˨ſӀʏǕ¼ʇӐϬɍΖʐĪϝĐΎ¹',
                        },
                    {
                            'key': 'ϖĽľƶƪФjǮήϼɋ˙ĨĲ\x7fКĬçȻ>Ā¿\u0383\x83YԐ-еϚÙ',
                            'value': 'Ԙ˝&ɸҗǡѬυɑȰΆǂҸʨы?ǐ˲ȒҺĚУɫЍϳӌӫ?ĉԊ',
                        },
                    {
                            'key': '˩¡·ӠƢmΉКӫĥӟǞѽφÅk\x94єǢ\x84ƞνЪϕǋĻ˷\x9fƣĭ',
                            'value': 'ȥɳìӦʣɏƊœʡ˶Ͳӛʼ·4î<ЃԈ\x93жƋºƯ\x92øɍХшg',
                        },
                    {
                            'key': 'ӥͲ˛ӊ˨ǘКǰ*ΟȎҝđЙүł˶НɃȲϏӇˤϬǕ˶Ъăɡ ',
                            'value': 'ѸÍŷҸ\u03a2ΘɼɡɸƟʳԋҎ\u0380ӘǺ%ΌÚʹӼƛӈ6ʐѺƻƅʷѱ',
                        },
                    {
                            'key': 'ԍȁλ:Ϻҫˀåţ¬˗ŢҨĲšŀҚҎθǒÌȽԚŬǯҲĽƸʳȼ',
                            'value': 'ƯˢқйШ*Ȃȗ\x8eįΐȦCӾѵоқüсÆxŢǷːżҸΏ&Ńρ',
                        },
                    {
                            'key': 'įѷΤȞ\x91GȶғʜѻΌӅĹԞ',
                            'value': '\xa0҂ϸĘǈ?\x84!ЋӗĴ΄ӧǹҕҹĕͻPɴʷŉϨɁцǌϛȩɱ\xad',
                        },
                    {
                            'key': 'ƍѰƮїҤɾ`ЪʋцϏɭ\x80\x8dоҘԗŗʾΑűǍ˽äƐʙϕηÒ{',
                            'value': 'ɯԍ˰ǐԮɌǴêɃșѩΨƢЮϵ\u0382ȷ_ñʐЅĞԩľɢ¢ğȟіɹ',
                        },
                    {
                            'key': 'ϰА\x88ΛԓQφƚč\x95ˉгКÍůӄÕͶӴ\x7fwиſʆŃǂ\\ȚЮŘ',
                            'value': 'ϳȹǲ¨ǉчɀέʮ\x97UԒʵˆjкòуɶϣвԏϳԧȳеĺԏǸӞ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ʹ',
            ],

            'event': {
                'target_id': 'ÖȏȺŁɕ',
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
                'ͷѠ',
                'ϠΕƑǧчҧʥôͿ\x85ã2',
                '½Dƀ,ӘàūѩtӕǅĦÑɪBˮāȥԎєSҩȨɺɏ',
                'ƘŸ',
                '9ȀȆӓ@φГ½ԂÐίͺҬПϊÈӛď',
                '΄ο³Ĩļ\x8aƳŌӗ[ȿˊïҞD˫ɦĎөǐ',
                'ƈѾʮǍΕ˄˹Ӵ\x7fƢѹΎ;ǗϑBǓҽɫʍƩȘʹǳȒӱũĭ',
                'НȚƁŴԉ)ӤʩĒ8ӲϿȏƆźǒӳԎЦ',
                '\x9cƒѼɼӴˀɋ¡ԢŃαԨŢ҉ѥœƜ\x91',
                'ӾǮâ˱ȶӜǖɡȪW˷Ėj˼Ԛ϶КƖȖŢ8ϛǛ\x85ľÿ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Û',
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
            'key': 'ȧΰŀǜϱi˽Ğ˟ØàÜʔԖìН˲ȠӫҜӉζfҚʢҔBů˥ǒ',
            'description': 'ϲϋ˼ɺò|\x8d;Мʾ\u0381Ѧɷ;ҁɾĳƕož\u038bηДϣˉѼđϑżō',
            'default_value': "F'ʤ6ӽҫѸƌȎʅԥƤϑɤƿаǜǙň\x955˜ѣ\x98ϔ±Ǔ҆ɢƲ",
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': '-',

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
            'name': 'ӯÊǦ\u038bбҷzб\u0382³АšΨȩӀѓϰʇʧȄ´Ƭˁo\u0382ū',
            'description': 'ͺƦŉɓąŕӾӵϰӂųћҬҟĘжћωϔҝɫҲ\x89ŦωѤәUȥʎ',
            'target_id': '\x9c˔yҿƚɖх½çΠӔɤȴńʟӬԚжƄ˂ˑɴȄΪʆINƟ{Р',
            'parameters': [
                {
                    'key': 'ɛȻùδӕŖʴ\x81ˠ=ΡɺӊxǑ',
                    'description': 'Ԗ˙ˠ˛΅ȻıшдÓΙ҈ǢƿʅǽΤŉЅŮӓчŮƏ˧ӲӯƵ¢ʲ',
                    'default_value': 'ĝǨņЦëqʬĸą͵ȩάͿԠʛţˎЊȠΒˍɳҠқƍ\x8aʇȉљÔ',
                },
                {
                    'key': 'ǫčÇ¦ĘҍŰɇǉҖуŀɯZĬÁԛ0ϞсԡӬԝ˂˘ӭ\x9dьӝƠ',
                    'description': 'źϿǉƁ8ǀǐºnzҙ;ɨǔȰǅ˙Ƕeԛ·ӠʞЮԝ˃ɀŎҡȤ',
                    'default_value': '§ԥСπpͱԑʰ³Ҍтːȭɬ¬ʠӆǈʚÛzÎɓŇӄͻðӣ2Ż',
                },
                {
                    'key': 'ÈȭƦøѵŦĢƢѡ\x85ӼϢĩ΄ӔvȓӡҾτ\x91ɤiËʿԎϫȸ|Ѩ',
                    'description': "шVìмÈ\x8aɇΝʸȨҸȰ!ğξɬĞ ŃȣǑ'ʹʧʣНǗɋúҸ",
                    'default_value': '˷ʮϳũК¢ЫψΆҸsʟĎҮƻʭѨȁҐѬʃĖäƴŨ\x9bɂœВʳ',
                },
                {
                    'key': '\x81ÒaəȀƸȮӦзŁŘϒȍʨӉԭѦΥˊ˅ѻʟɻюϖǔҊΖˤȎ',
                    'description': 'qҳ¾ҨЁĲɏ϶ώƠʷҰʋЅáŸJyċȢ΄^ԖǝȥŇŀĶϨЍ',
                    'default_value': 'ʵʑїǙŠĪʇƼɔϝКќҜҮŌ\x8fαżȞĪ{ΉĒvĨʰΛ ӆƩ',
                },
                {
                    'key': 'ԭԚѥԈÑ§ҹӀӾ\u0378ВԟÅѐȹàϔδЛÊԧӗ\x97ɢĈҘЄЖżԭ',
                    'description': 'ӮÁĽӖԆÖɋҢ϶ԛǈomȹΦ]žԉΠҨÔŧѽȀȌɃΊĐϵԠ',
                    'default_value': 'ˮcūú£ĠѡǻpOŴµҠǙ÷ƤΈϮʛȟíӒˢфӕψƇɩʹE',
                },
                {
                    'key': '¿ʍʈϓҼưƦǢ',
                    'description': 'ʈĮђɄҳСΝĽńȁǫɕwͳϔЍŸԍҷς}ŷԂԘόк°Нǹi',
                    'default_value': 'ůПҶǓӈХǧūȒΝԟ˾ʿŹͶʬǕòƜŖǧĭԅǼ\x8a]˛ǥʊʖ',
                },
                {
                    'key': '˃Ļ¸ӴɬҧóŗϱŒӓҚxЎ\u038dьƭȓ{ˬζ\u038bĪźȿӪҢǍϚқ',
                    'description': 'ӗȏλԕ#ǸʺɕϱҚƥԨԌĘҟŏԆƳбұŌɀȢ\x99ԠɟƅЩÚı',
                    'default_value': 'ȤɷΠϫӇϮУǙ˓ѪΘȚ˸ÊшͲӧFǖĎÏȂ\x87˼ϯŀЂԩ°Ѣ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȏҰƻ',

            'target_id': 'ɖЗſǫǛ',

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
                'target_id': 'Ȧа\u0383ĆźΘ}aԘƧŨΪϨʗЃɆђƐɶȘҧӥ\x82ΤĲӱ\x87ӄϊЩ',
                'parameters': [
                    {
                            'key': '°ƙЗFΛһԨÒȬIъĥ}ϘќͽӝΕǍʟԬÑǨɴĢԊˏɏ˝ą',
                            'value': "³Әӂȝүƚƪґѩө˴ϲѐǛǧѬǴ˅'ЇβȘŵţӺ´ŅÏÜç",
                        },
                    {
                            'key': "ͳӆžӵȺ˟ǝԔľʇƽђ°ɮĹӵɡƵ'ȘϠӁƆǆÑ#Э®ϘĒ",
                            'value': 'Ѱ\x88¦Ѿ˘ЈҤνȵđɘΌ\x91KôτǝĿЁŗȢͷљʊǣŀŖǋ˧ɒ',
                        },
                    {
                            'key': 'ћ\x86ƏɽҎɟ¾ʍɐ¦Έ˥Ŀť\x84гíӎԭ&ʳƣƵǱɪǅȆņцұ',
                            'value': 'ʖoϮ&ĭƓ÷AhҩԬǵǿмǢņĨǾɨÐэΐyĸȁ\x86ˎŇϚȳ',
                        },
                    {
                            'key': '»ԟ\x85ŊýνтγψԨĿɫÓĨХˬΛӇˢ˖ȳxΤ',
                            'value': 'ʾÖ¸ɢōĶю˘Śˆ҉ҷŬҰ˗οXӽͷǢΐưԖȗƺϛˏђǨ˃',
                        },
                    {
                            'key': 'ǝԜ÷aԇʸãʤZGԞҵѩǢҗ\x86˩ǭƠʀÆŦĕ҃҃ɽԃΓ×ɵ',
                            'value': "âÞҔ'ǂśŷΏƌ:µЍ£ɚŁҥӅĩƤьĳȆɛӄɳ\u038dʬ˝4Ͷ",
                        },
                    {
                            'key': 'ǌ˞υͰͳŢχćǢŭȍǋðѹӷŠ˹ʗRӑϻɒϺӽӸǽЧӮȷӨ',
                            'value': 'ǤɾЫϐ¤ΜɰѿȄӨ˺ϙʹԒԖͶ3ΛԌĕ˸ƅεġ˖ѭƫŋʋˮ',
                        },
                    {
                            'key': 'ÚӲΎ\x8dÐÅťƆРʚƤɫțйҘЉʐ+mgә˃\x80ͷ9ǙǱɬ',
                            'value': 'άÖЗѩ˥ҍɡēŎķҧғþϐӆɽҖwɨˑŋŞņҳԄϟӵƈͼϟ',
                        },
                    {
                            'key': '˳҇ǑԩɘПԈʊÈѸhĒƑϮŽƐ%ΣѼРӂĸС\x83Ϊӹ×ʨ\x9e\u03a2',
                            'value': 'iώĻљĢȎ?ѠȋΊĠȃ)ňƏԟϯîЈі*ɨͶĚʐǕŬ˨ĥʋ',
                        },
                    {
                            'key': 'оżĜέˡƝǓɈ˷қʉ×ɇ˔yϢԖϼʞ҃Ӣҽ\x94ʏю˹#ƀ',
                            'value': 'Ӝ\x82żӞƮ\x88%ΘÙНѵщˆrШеђȇƺş',
                        },
                    {
                            'key': 'ШzGҁƻƷЩƣΘʲыĂʊƶЛԮÚȸźŀ«ǈɔгĵµμʁЦǤ',
                            'value': 'ǰ½ÙˬȾҡ.ȋɼα²ȯƫʹ\x89\u0379ЂɔέçƲ\x81˸ΙҜ\x97Ğ˵˅ʭ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'ʓŧ]ʳï',
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
                '˔ɪɇǻљ',
                '%ʯԝξϴϛҞǥѤʔȥβĐӀǭ',
                "ʽӲ¹\x87ӝÂԦϻaĈO'ȆɌh˂?НƨʼƵԤ\x81ϥɅķÄƁãģ",
                'Įщƕ¥Ȅ˦ҋʭϛҔԢĲԞ%Ԕ\x83˥',
                '\x95\u0381Ǹʦļɮӻɟʗ\x83ɕιѿҕρȔĹΣκďӀħ˽α',
                'nĢŠϊǀŭʣˑ҂PĺǕЮͽĬӦ',
                'ϓCĎŲăӓΏЩɯȷɃŔӬɁ',
                'ѠҾнģũˀÜ҆OŹ˦ԭѨԭƴϛэŽοЭeӀ',
                'ϿһϗЈ˾ǱƝƞŹȽǵɊɑǔȱǄ˞˰ȒƎάӴ\x83ȔéҖʓԖЬĥ',
                '8ɘĪˀƆ=ǌǀƸĆŒɜԥё',
            ],
            'event': {
                'target_id': 'ҾʪʝςΪľћđ-ńЖ҂ӂɲȮԨϊΝӮǤ˜åѮǓɔƥżΊ΄Р',
                'parameters': [
                    {
                            'key': 'ȣ',
                            'value': 'ƞðgiǢʴƉʘԣ5',
                        },
                    {
                            'key': 'РЖӚĵ˥ƪѓmѬїЂΞƥԜɬәѤ£ԔÛм\u0381ӻΪȀˆɖő',
                            'value': 'Βɮ\x82ò0ŢЯӄӃʾƱĂϢ\x83Ϯ±ă8˺ˋɏǮҟɮɆÓƑӇȻț',
                        },
                    {
                            'key': 'vǫƴ\xa0ȕϥŧɏ·čʥ|үԟŰӖǝΥƟxрДϕФҟ!',
                            'value': '\u038dӔĀϚӄҍȂʛөӷż&\xa0ñ¬ϧʨƟǫϘbQǏ³ǽiŔŲĿδ',
                        },
                    {
                            'key': 'ҩʫ\x8bɩȲʛÎ¿˂ǭŀƒ©ŭ/ѣň#ĥøȗƂԃÀƹфϸӳIҨ',
                            'value': 'ƽțӱїġҒøҤҶǛ7Ďϫ÷bĶГϷ\xa0\x8eZGҿˮԞʫɑĊ\x94Ų',
                        },
                    {
                            'key': 'ǐGĮǠйԆѨĄŨʵƵЏƳýɚϚÜϑІӬ҄G˽ưÇɪіʧ\u0383ſ',
                            'value': 'ʊͰϬŽȺе\x89ʱĜәҋɂʧҲʮѷϩǥӮωJīˢӇăҀŦ®эi',
                        },
                    {
                            'key': 'ӏ©śÀΉűĜŌʹѺͺǁԔŋįεÊѠȼεѮ÷Һǻ²!ɰɔ¨ɢ',
                            'value': 'ϷƩ˖ƅӔɁʧLԙÿ&¬ùƏъ˂ȓĶāκɿЧŖȸƷʭб<ѬԊ',
                        },
                    {
                            'key': 'ƗΒȍ1Ҫ˨Οǳ',
                            'value': 'ž¢ѝa¸ɘƽ`AĠǣǜǈр{øɺģCЩʈÌʙɖǞ\x90нпӛϪ',
                        },
                ],
            },
            'comment': 'ҎԑӉůφμƂȠϷɶˮҸ\x97ȹ&ˡƽү(\x87ňɄƱİҾƦѥɂåĒ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ϩ',
            ],

            'event': {
                'target_id': 'е=ÑȤђ',
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
            'sequence_type': 'meta',
            'master_sequence': [
                'ϠȌțдŶԓƤʈǥи\x98Ǥ\u0382ӃϨ\x8fɒ',
                'ăԚЁ\u0382ĆȾƳҨƆŦӪԑƯIøѨϖʸͼӛŅ',
                'ɬѲȵҒˆҁ\x83Ҥѿ',
                '˅µgĩͻєǃМˠϫe΄ϕ',
                'ο˽ʱѸɆŦяқǃВĞ®ЁÁɽʞҐЬѠ',
                'ǢƹѣҪĨѲʒʰҵ',
                'ÛǘҝŽůƮȭʬÏӌ΅҈¨ŒɛĵλʕÊ',
                'ӟԮčҦƵ˺',
            ],
            'bindings': [
                {
                    'keys': [
                            'ȽӷŪ5˳ȌµǴ`şԑ˵ԆсŐ\x97˃ė£ѨǃŎҳќɭũǄɨŚ',
                            'Ϗf}ĹÖ¢ӧˀ@ƻʤ²Ӯӱν>шϑҤ˦',
                            'вʃӳϽѨǔšŎ',
                            'ѲԍŲŃƐǊоǴƙĴPȖˏĄƻ',
                            'ĪɛԧȅǨƣ©ĵЖɃ?Ѧν',
                            'ԩϜ\x90ЅʩҶӀ͵y˝ЁǤ',
                            'ĐȚ',
                            'ʋğơp˫϶õ´iǚŏĞŢȹƈϹӌƺɛãʡӨԚȱʧ',
                            'дȣІĄèӏ˭ɢ҆ȑљƂ¿ŨŲѷЈΗLƃϝѶƣǴÄȘôҳĴ',
                            'ɿ"\x9d·ɓŇ҂ѸȎʤĨTɴ¤ǳ\'ȴɧŇӸȓû\u038bs',
                        ],
                    'event': {
                            'target_id': 'ľİӰҡʰԨϴ˟āѧÄʞϣ˩˟˞ԪK͵Ɏ2ʕΛƐϸ/ɫÀ\x94z',
                            'parameters': [
                                        {
                                                        'key': 'ıɾôВ\x8aØϏPƠѠηãŕеfÒǌĈľԦѡȡӗȇƍǹȦȓ7Ϗ',
                                                        'value': 'ĞҼ Xΰĭ\u03a2ǡЂ\x9e^ӥÉԀTgОˠȠ˜Țɿɠ\x8c\x99¿ϮҖɯȌ',
                                                    },
                                        {
                                                        'key': 'ûȐд=ΗцьӀġҿӁgɭ\x8cğʚơ\x88ƲӝѮƗґӘƹäˏƟ\x9bá',
                                                        'value': '*ǡ˩ɼķ¶ŻХǋʽɜʧøˢǀӀȲϞƾƓϦȀѻªɅбˌғʶ˗',
                                                    },
                                        {
                                                        'key': 'ɡ¶Εmáˬ҃ˑWѮƷ҆ǬΟѲԥÐ\x9fОǓϷЁʴΈѲбɐǧǆϜ',
                                                        'value': 'zͿǍ¦ūȗѧŅ[чίĢΙƱ҂ɓэұǉiƢӵǩЪ˭bТɲǢ˳',
                                                    },
                                        {
                                                        'key': 'ƽʍȻϽÐԨ\x93ϳ·ĕҏ\u038dҗɧЕɝЬwɪfNь',
                                                        'value': 'ҧÍΏ˾LRǞѤɑ«ΊſѭȪ\u03801ǭҁϓė=·ĕ҂ˑԝÃŊΛŊ',
                                                    },
                                        {
                                                        'key': 'ǉQɣƱį@ŒǄȶȄǊǘԈЉǪʽȺӈ¸˗ēǐ0ȂԦʮƧɒӿț',
                                                        'value': 'пҧƾӻЛɞӱʅӋҍϧǠԔ$Ŭϯ}ɽΪ|ҦǩĈϞϡОɑ\x93Ƿõ',
                                                    },
                                        {
                                                        'key': 'Ŏƫϱƅɓύ|Ɗ¿ŝˎĕơʂѣβΡɄȰΜοҕΊğŖʸǙ҉˧ӛ',
                                                        'value': 'ÞЖ&ʹѵʑŪXњʮ\u0378cǭżǎǬѝѭӲƟϖˎȀ¦ЩûΗʢƘϺ',
                                                    },
                                        {
                                                        'key': 'ƈѸɦWϫҳ˥ĖϢ\x84LΧӰ˄ΚӦƿЁДō¸ɷɗ\\ӥκ˵¼ÏȀ',
                                                        'value': 'ͳːԊ8ȜǿǧΈ³xɨō\x98\x89ЩȹȲӽƇȴʵӫ5ɘлEǿΦ˞ħ',
                                                    },
                                        {
                                                        'key': 'ɘŎ¥ɸӖ\x93ԐǠ½ʰҗ\u0381zʡŊĪΌʤԞâӦʸМӂӀǐϝIНŵ',
                                                        'value': 'ŠΥγȟ¸ôĜЙʋ˲ÀԚȵήΎ˚ðӄϰЙýɝĭͽ\x86ϯŨєΩӂ',
                                                    },
                                        {
                                                        'key': 'ѳԫЫ',
                                                        'value': 'ҳϳϾėɦÖtквĲШԞØέŸεƢЁЋbƿʘΉ˞ϽǿÈүˈӲ',
                                                    },
                                        {
                                                        'key': 'ѦţǯS0ж˫ԟdǅϣĊɧӱԏˏӚʒ0ӂǢ\u038bԩ˷ŶĒŉȺӨɴ',
                                                        'value': 'ɯЮ˦ǝȅҲοʃдŔĹΥ˞ʐʒģήʗʈεƿģoӁʊѢƆҢɪȱ',
                                                    },
                                    ],
                        },
                    'comment': 'ԏɞȪTēîǆ\x9c5ЎψԍƏΒӽг˴Žǉҡ§ԌлђÀƳнɟϤƿ',
                },
                {
                    'keys': [
                            'Ũΰŝȩəɀ¦ɘǸԐˍÔәɗÎĚ˥Ԟɵ',
                            'ƞpǳȖӝƜϋЖ\x80˯ŶӗȿĐ9ξΟ',
                            'ȐщԚʸґϯͳɿԃӕ',
                            'ѳʢ©чҹĊ',
                            'ѵ7ãԙ\u038dǯӞӵЛȍλ',
                            'Ғҧ\u0378Ҏ\x87ţȱӟ·ɻ\xa0ǰ',
                            'Jɵțıʘ\u0382ЮНʕǱǞʚĨɭʻΆɌĭѰſѹҔЉǊϮɾÊ',
                            '\x9evȜԆʲӋº',
                            'ƶΈíӄѭ+ź*ƷϙǄµȰc',
                        ],
                    'event': {
                            'target_id': 'ΥʪlϵЀʝЬÃ6Êʷɮ҇cͼÌĿȹÓİ8ˑ~ϫǹdũѦѢУ',
                            'parameters': [
                                        {
                                                        'key': 'ŠíҒɻčǴ҃Θμ˖ʶ¡ƲөЦΘϕ΄ȲſƌЈɞѧϗɦǲˋϝʲ',
                                                        'value': "˧Ɂϣχу\x92ɣȯǱ½Ҝ2ԦǊʖ˥'ƻÊƕѭƈȟƤ\x9cŝſˋĊˍ",
                                                    },
                                        {
                                                        'key': 'ĜƌˇÖь˵ƲǦƇĈǛɝ Ѣєłӓ˩҇˺ɐћѿωύΒƔMàɢ',
                                                        'value': 'ϵčơƢƤʆӱŨйf҅ԕ\x8bʴIɦǯЉ°Ƥ]ҿȳΓÌɐ0ƨϒϼ',
                                                    },
                                        {
                                                        'key': 'ŎӖɡԋÚԤːħѢԀƭëŁûɾɒκˎw',
                                                        'value': 'ҏԠĸƯRμɠŲ"ͶʢɌɡɅ\x9a˔\x9bƕȌУǾЄóčZǦ\x85ϸΩˍ',
                                                    },
                                        {
                                                        'key': 'β˗ӹšƭϳƮɥ˸Ԡ¤ίɓĵąύĵÁĜӫŝ˟³ɖ9$ÔȗԔĪ',
                                                        'value': 'ҳʕ\x93\u0381Ӈʵƃɀ˾ǄҰѼĶюŠǋČ_ӱđрǢɄʆӷԭĬПӢÆ',
                                                    },
                                        {
                                                        'key': '\x8eϡÝԈɫLϛѩхȂѿΣӵ˺ԥɾŴнΕńФÒέĽʅɉˏύɦÏ',
                                                        'value': 'ʵ˲ӽҔ\x83ʂͳĻɟʋʗɱЅ˯ƳМ˃ÊɉſԠƉ\x80ҾɾΑӊϪϺҍ',
                                                    },
                                        {
                                                        'key': 'дӐƿƉΞүЪơӓ¢˗мԡӲǭĄЛĕǱʸðŴ7ȳӾÔȘ˪µD',
                                                        'value': 'ѧǠѓҕԍ\x85ǌ˲Ĩ¿ʗНҌ\x87ʝΈȋЉϮѬȠ7˩ƦѲҿѢəĚϨ',
                                                    },
                                        {
                                                        'key': 'ӽ_Ĵ¢϶\u0380aɄǇ|ԩβɗӡɾȁү˦ДѳҷɁʣǖɭǗҭъZǯ',
                                                        'value': '\x84ĵǶϲÜ\x84ЩΧǌ»ɾϭҖӖїҞXηǎσӇԓˬɰȈʑʐʘØ˃',
                                                    },
                                        {
                                                        'key': 'ÞϪ"TȡҵѡӾȘӦÞɫŠԗãқԔƖ˨ȷӷȵˏʬȚТɭĲϝҎ',
                                                        'value': 'ȔͰ\x7fǄąͳwʌĔΡ\xadŀџĮũΫʁιˇĩΟöŉͲʖԥķѪìº',
                                                    },
                                        {
                                                        'key': 'VΚд£БĂІІɿŽɓǃҤʡǜӘnȐɈЅΥҕƮ\x93ƞϨģԥҏӚ',
                                                        'value': 'ҿʶ˺ű0Čϟҭ\x97ʙĥŜ\u038dʸΓˀʃӯɠŗҚɗЕџŻђ÷ņҼŷ',
                                                    },
                                        {
                                                        'key': 'ʫIΩҭĽ˜Ů&ўƾS6ӁӔ\x93\x83ŐѦÎȜΎǓͼƒ!%ȣιʼХ',
                                                        'value': 'ΘДʦғҶșлϨˑѮ»\x8cϒη˃Ȍəȟʭ;ӵ˫ďΩ҅ǚķԁǠӢ',
                                                    },
                                    ],
                        },
                    'comment': '\x97ĉйłƺЪˍȇ\u038bЩĺҞ˧΅ԛѕ:ȹ`ĻƉȼĪʝΌʅðŮǢŌ',
                },
                {
                    'keys': [
                            'ɇ,ƨǪӣѥħηНȯȴĴǏ˔ҭƜ',
                            'Їĕ',
                            'ǠzƯϫΩȖʈϚ˝ԨǠ#úċԓìóƺҜ˧˒ƙ³ЄȕҏǜΚ',
                            '\xa0Ĵʌ˳ŒǠƑɱΉƀʒɉԔ',
                        ],
                    'event': {
                            'target_id': 'ȕӜϔɨҙҌɀŕˡ\u0383ÍƍѲ˥`ćүʐſρҶʄԔҽãäѥ\x91ūƤ',
                            'parameters': [
                                        {
                                                        'key': 'νЖĸҸԁȒʆж\x90y˨ɇ\x8fɚ˱ØÔɔÔɼˣѢͰÛɚӫϷжȚҠ',
                                                        'value': 'ӚƐͿĨύƍėĸ\x8fΜʠōԆĎ®jӰ˗ϯêÜηŲƝŽΆ˄˶й,',
                                                    },
                                        {
                                                        'key': ':ȌҙӲŗ¸û¸ȆMїЏʻѮҫĮ҈JɫҌϿԚǚơǐƯϗ˸ƩЄ',
                                                        'value': 'ѠʉÜłãˡɞǄԒŮЍΜ\u0383˕кˑäуĶɹI¼IКжҗӷÄɟ¬',
                                                    },
                                        {
                                                        'key': 'ХƆљɇbɍ΄ΟѲɠĆȱ·J˪\x8bǞҤҍӵԒɪıǪŜјϩʥɔӋ',
                                                        'value': 'ɨѮʚȺԡЗɋʹ"^ϋÉŕ`ǖѩ\u0383ƦΑЃˏϨɬǭǱí\x84ӔĄҞ',
                                                    },
                                        {
                                                        'key': '҆ЧǶƔÝԑϷ˭ҤξOҤ΅ƽїϤ҈фЛ\u0378%ΌȾԏ^ėˏʞLɞ',
                                                        'value': 'ƯÎĆʪҌ÷ɈӢҠ!Ӧ°ĿǥΖҝτBҞƉҝǱȼӍÒ×Ξȇȸj',
                                                    },
                                        {
                                                        'key': 'ʲǊŉИĬ˝ʢԂȯғҟҕѩŽϦ?ǘ˔ӣƩϿĀѸɠNpΪσҐα',
                                                        'value': 'ĎԍйԮʍ<ʲÂƒķʝƼԆƖʌ=*6џҦƞ\x8cŪҸңǾĕ˹УȜ',
                                                    },
                                        {
                                                        'key': 'ĶҡǵϻȖÛʝ`Ԣ˲˷Ɩ\x94˙ǬҨŕŀǑDь\u038dԁ˵әǛ˛ɟȎɊ',
                                                        'value': 'ұȢӼяʲ¸ɵʓ\x8f8ʧȸʏӺΙI?ɽѪTϻYĎǴԛōԣIΖӺ',
                                                    },
                                        {
                                                        'key': 'ɣөƝƏ\x98ǈɩӀƳ͵8Ũ',
                                                        'value': 'ɶѦӭ\x95ØȱǖXҲ³Ҩ\x89µѡң˰ˬԮŇĩ·ǁȿūГGӲƲYə',
                                                    },
                                        {
                                                        'key': 'ώĚˮҵӴɭӋ[¦Ѣҧп\x84҈ȘĴ\xadһѐюЙŽʲɭȘk҅Jϒǫ',
                                                        'value': '\x86űƴƠҐ҄΄ƤΖʇƜθ5ыâөЎчѦуɩŏηÑҎәĉ\x86çë',
                                                    },
                                        {
                                                        'key': 'Ԅǳɉˬ\u0379Ԟțį˧ΩƮíp[ϏΓщÍʳϷȡǭԘϊҧưфƄЩҮ',
                                                        'value': 'ίϺѵʢȏ_ǙʂɍҎӥεԗéνŨӳ\x81\x9fԔȢрρ\x86˫ƩԘˍʝƢ',
                                                    },
                                        {
                                                        'key': 'ϡƺǳɶʡѭ\x7fԒǳĬƄɲЯĘſɣ\x7fѼɛũʪЙȊѭήђ.҂E¸',
                                                        'value': 'ƺǯɋʔӮτʉę˻ʕ}ΦˇışбӶğϽԒcĀĪąκŏʆEϰι',
                                                    },
                                    ],
                        },
                    'comment': 'аƸϿȏdԕнwȢҲүšɪϲΈ°ʭΐǄ7ƐĎǪɷϻӼΉĈƌҬ',
                },
                {
                    'keys': [
                            'Ǉ¸ŅçˁɝàԎӠӽŇЋϡsɦłʈ!±|жʐ',
                            'ď¸ƪīýМɁȧƈ´ӱŹňѝȏŧЧ±Ǻ',
                            'ɣː³Ż˂ϓc¨Ѥʜӷ¥\x99ԋ˶ωѢĊȾĎгɩԒǢΗЌ\x8fӝ',
                            'ӤƚÿzȭǛκԜТИĎ¦ʒȩԩơƮШ\x93ȄD+ҋԭ\x83',
                            'ʳƉюAυĎ\x84ѸΥΕ',
                            '³LʽЪϛ¡ϙϲβƦɅΚ҆Ҋǌ˸ʳЎӍð',
                            'тǗєȋǲĭ',
                            '˲˝|=Ƚя;ʛ\x86ǡɾʅΎ\'¾ȫȮ"5ɂ˵˰Ўĵͷʷ',
                            'ȴĉӥϣ',
                            'ѣԒɾ˕',
                        ],
                    'event': {
                            'target_id': 'DЋɞǩͳ˟¹VѧΡӏ¥¡Πũϙŕ\u0382ėVɶɇǮіСƶǥŐҠҨ',
                            'parameters': [
                                    ],
                        },
                    'comment': "εʅŵѿʆҜóø'Ҿ\u038bҕUϧӏƔʾΞʎϝШԏӝǐӵű;ɛл\u0379",
                },
                {
                    'keys': [
                            'Ϝ˚ʕȝ´ҲӕʔԦԜҐ',
                            'ÂʏԞȌǰ1ИƱ',
                            'ȁψȢű\x98ę\x86ϲԐʲĭĽѶ\x9e4˘Ҡԗ',
                            '¿ñïњǩϋ~ǋÌ=ȱɼ~',
                            'ѶА˺ʺʺk˅<ˣƷ',
                            'ȏΟηҧRτ',
                        ],
                    'event': {
                            'target_id': 'ęѿǢȝӺ¦ӓɊӍѺȻ˺ƅĬӘЏȅɜ΅ԧҞϘϠɁХгүԑҨơ',
                            'parameters': [
                                        {
                                                        'key': 'zŒΘĈԈҤYÕӊųԧȨӈҨĀʿ\x8bщЗ7ǹōσΖØ',
                                                        'value': 'Ȩĩēʕ\x84ԫOӇѴ΄ȑ˄Řүѹ˾ЬӲѴƧ˖ъɥ`͵ƠЫ@;ԃ',
                                                    },
                                        {
                                                        'key': 'ŕќӣƵȼƚӜҢӐZϿĹŝƮͱ˦κʛŰƳˋľxǆÂĚӢlɤî',
                                                        'value': 'Φή`ҰˡӁūɢĐɣȌϛɯƊʯĺюĻ2ѳӪԩԎ˧ˆΧ˾ȅ±Ç',
                                                    },
                                        {
                                                        'key': 'ÛćɠȥȦ',
                                                        'value': 'ɭЪϲjɹʹŽŦʞǾѐǜ.ƞΝԑï˟ǵŅŲÇӴщͼǎԩϷΆύ',
                                                    },
                                        {
                                                        'key': 'ϐńϑǰǀƪįËîϽæο҃ȓ³rԥ\x87ӜĞƏ7ͳˆəNѲʆƫɸ',
                                                        'value': 'ʃǷԄƟáɲ˯òǔ[ͳʹȟȏƖѸÙѧ\u0381ʎЀ϶ξś}ζȨҟʠϩ',
                                                    },
                                        {
                                                        'key': 'ԛӶ˷ȑƇрƱԗʖɀ\x9dȽҽƺŦÿ[ʻͺǡɽІǡǿҭΆ)ǌľӪ',
                                                        'value': ']\x9cć˽\x9eӕ˲ȜјԨýĞʭˡĕґȦЗ%УǊгтѪȯǣдѵ\xa0ȡ',
                                                    },
                                        {
                                                        'key': "ԡЊΊžɅΏ$ҚĜғхʫ'ѦƵ\xadȄӎÒΖƺșCɌ˛ҘζȽұA",
                                                        'value': '£ўЇÄѩ?ЎI.К%ˏ˱љГüОҏҼй˭ɩņѼξȅΌûǭɀ',
                                                    },
                                        {
                                                        'key': '\x9dÓāқũԈ+ɈәƻʵĳӪƄͺ˜ƒ\x93\x95ЕɫЉȇӬ\x8dǀȂѥ',
                                                        'value': '(ƳλѺɅmϸÝϯԌӷȅ´»ƙΎҒÿ˙ƞύɎʀоӌӭзϏǰƠ',
                                                    },
                                        {
                                                        'key': 'ƲʲƈêҌ˨Ë',
                                                        'value': 'ˌàMŀ˙ɧǠҞūТ\\EѪŗƠx®үӴ1ȅċɶƫˁѦųμɽҮ',
                                                    },
                                        {
                                                        'key': '?ЖИξҾ¶țѾɉϑʮʾƩěԣą\x89њĜfγϐ\x95\x8bЂôԍѢǇ_',
                                                        'value': 'жФʈʥĀʾԡ.ĻA§ˠѿгӋʡƣ˾\u0379ŭҤѠԃ\xadƇωӞmǜ@',
                                                    },
                                        {
                                                        'key': 'зƉӍ&Ԡɏ$ӸǯяÕɁ',
                                                        'value': '˒ϼ҂ϾʾϖdƨʭѻÓʉѼπˮy`Фʝ˽¢ԣӟūěөȀǭϯ˵',
                                                    },
                                    ],
                        },
                    'comment': 'MҕӱĢ\x8fŢ\u038dΕȞҝΎƪɀˆҚ˕ǽЁĶәʱɽӚҲӷӭȗ˾ˀİ',
                },
                {
                    'keys': [
                            'ÆŚːû΅ө',
                            'ĭҚσżWǽԩ҂ʿʦЇхϔӰ',
                            'ƉŬȫśƑћ\x8cВӣʗ',
                            'ξɇц',
                            '\u0382Έ\x7f\x8aƇӘԀνǩΙƻ',
                            'ԔԆУͺĞëƺÌȦ«ΐϷҔõΓɖˀ\x8d¼Èϖ',
                            'Ϋȟӭ}Ǵw8',
                            '¯Βɏɺξƣ',
                            'ǺɐҺˢƃόӢ~ԂƢϺʴυҤÆÂû\x9aΣ˷ɆϢɚҌ}ȝ»ЂЦЌ',
                            'ǭұǋUƅʎ(ɢ\x94҄Ș©ç\x9aԚѭ/ҩЊSƺ>ȹƠνÚǘбʽ',
                        ],
                    'event': {
                            'target_id': 'Ưԩ\x7fNɧŨŋҕɦÑȵùǌϖƞϯͰ˴ŚǒзӝƬʍʇѲǦЗҟǀ',
                            'parameters': [
                                        {
                                                        'key': 'ǿŮѲ6ϔX˄ʐÕŎжϧ1_ͽϖOɛƁЄѸ\u0380þͳÃŧ¶йʖԖ',
                                                        'value': '%ƥûԭαr¸`ИǪ\x9eŧɤ\\Фӹ³ƥ¹Ҟɢ"ÛΜɚ\x90)˕Ϊǖ',
                                                    },
                                        {
                                                        'key': 'ɴďŅĆðҹʅȓɩʧǷ˞¡Ϊøі˟ң\x9bÉҗҕ',
                                                        'value': 'a´ƅƾĜǰƹωGƝäɉөWӥҩǱͷ;¡ΖӸʲ9Ц˔ԧҊ)˻',
                                                    },
                                        {
                                                        'key': '_ȴȲ˽',
                                                        'value': 'ԫÂϪȨ\x97ƽңʜӻĤŒ¥ϱԀήȇ-ƙȟԇσĢǘ\x9cԈйȪѿȡʢ',
                                                    },
                                        {
                                                        'key': 'θӵǔňɬнҴԥǁĢҾԈɏέŸϙІĦӷβ',
                                                        'value': 'ʅ҄;\x9df·ΐÇʨũ˕ĵɈǎʧӸҾˬȪÑͳÌ˹αéͻҐǼǻӣ',
                                                    },
                                        {
                                                        'key': 'ҜʫАŷȐϋԘȆ0ƜʯϳӎVǮ\x8cE',
                                                        'value': '˖ϓ»ђǰȸ˯ȦЫРЫϪŉ-Ѝԃî˖ȭɪɯҰѧʊԆŸԭÍΫŖ',
                                                    },
                                        {
                                                        'key': 'ÈҥѲύİʎфóҝčЪƕȚț\\^ҋďşűб',
                                                        'value': 'ˍϖѝˉƦƖ҂Ʋґȅ¼ԭҼYӷϫ\x7fδӒǷИ²ˌӣɗԆƧˏŵƱ',
                                                    },
                                        {
                                                        'key': 'ūʪэ:ȷҬӂŵáҘϪΉäѷ7OφơϑñҪä·ѷ҉ΰϽ{ȌɈ',
                                                        'value': '¼ʄОǎÇʺԁ˴λϦƃŴɽ˔ːʅzČȀсʅӆʣĘȯԐԗϛ<e',
                                                    },
                                        {
                                                        'key': 'ȅԡȰ:ʿąòŒðȓɢˣεϲɧÔʕˎϐ>ÕӋƹƩǉËĠŗƀЄ',
                                                        'value': 'ŎŨɣǮː˨ϐʿӪÒώԟӄƜġ\u0380йшɄȯĢЇĒȫǄĎ҃ðȖ/',
                                                    },
                                        {
                                                        'key': '˴қ;ʴ',
                                                        'value': 'ĨɪǍʪүkԄӕîӻÝ7ȭӲĮŘ˘Ёˑδљʬ¥ˋ>ɍӂ ɪÉ',
                                                    },
                                        {
                                                        'key': 'ϭӉГÖŌ~ˏø˅λ҅ŔȌӯĩԅѓάҦШЗUќǷƛ\x94ƩБͲς',
                                                        'value': 'ϭÚҿƥԂţєƙµƊˢQźőïԮÍӓοԕƲġŽɅGĜϏɒӯʲ',
                                                    },
                                    ],
                        },
                    'comment': 'ƾȏϐѪљ7эêĒŀæL£ɻñʂȵѡɉƋЬӋ\u0381ɣŶȬΩ}ɑȋ',
                },
                {
                    'keys': [
                            '²Ѣ0ν˧ЙȞдҐӨ',
                        ],
                    'event': {
                            'target_id': 'Ŋˤ˟ȦΠ´ΏɺˍΚǮʌ«ͽЎÍҡʹӮƑŪ\x91џҷΥŨǢKŋ˻',
                            'parameters': [
                                        {
                                                        'key': 'ĒîÆҪÅǏ',
                                                        'value': '҈ƫʄӊĐӏÒʴɌ\x86ÆьơȰĥѦʁǊӅnԏ<ҰǏԠґ\x85ʂǀЪ',
                                                    },
                                        {
                                                        'key': 'ˈӆЙƸ\x98kӳҡѡҡʊўŪƸ·ӂƗμӒƓЉΝțǰ҈˛ŬZϮӀ',
                                                        'value': '˗Ǘ3ʳͼ˵иǷԋҗҍņƇǝъƟÄɪʰ!ƒįӒ{Ƣь`ЪÜö',
                                                    },
                                        {
                                                        'key': 'űԩѰĀȘģαԩ˝ΪϷϘ³ŘVΐүMûӘǄӽ2yŴɶҋǓĥɯ',
                                                        'value': 'ɰȖӛсʓǍʦʛϘʆЗoԕ÷Ƅǀ~ЭOСʐѩёȴԉ9Ȱӑĸɼ',
                                                    },
                                        {
                                                        'key': 'АȞȭ$ŀb',
                                                        'value': 'ɑҔϹʼʰŲõ-Ē˦ˠ6ʪҫŊѺҡʣ\u03a2ӰʞΕˀԬӃͽӕɉƠӗ',
                                                    },
                                    ],
                        },
                    'comment': 'ΝȗԌџƭƈѴKќǷůϝ6ĸƓǅϓȱOǊЕÌƹ;ҡǣҲѬŔǆ',
                },
                {
                    'keys': [
                            'кɏƨKύȻεįăŬŐ6',
                            'ƐΠɌǅʗơюaͺ҄\x92Ѷ˼ҜƀƇÌʹɻƟɰʴˬǋж+ǘ˸',
                            'ƪǶţóȥўɾԟʓĔ>Чʊ҂&ǥӇЬ-',
                            'Ϩđ!Ȼ,ɹӰÞ£͵ώˮҿϏùà\xa0ʽʻžȉ',
                            'Þ҉ΪйĐӐέʈʀӧ\x86ɖʥмӛȚτȻ˸ʒȁ˖ύŬӢˈL',
                            'ԗ¹ŢЬ0ˎǰůҔɰСəəόȵ\x94өǕ',
                            'ϘȆЌOϧQ;ȴ\x9aÌȾę½ǾƏ˽H|Ѝћ',
                            'ҕІͼȌˎΛ',
                            'Ҩ1ɷ\u03a2πνɨ',
                            'ʵҁ',
                        ],
                    'event': {
                            'target_id': 'яψŧȤĞɘӆςԎϪ\u038b\xadŧǐMˆѺeƑˌрϖӦһӼȓňЃӓΏ',
                            'parameters': [
                                        {
                                                        'key': 'ҁѶÁɠϰʞ0Ǵҡʜϧ¦ƇдǕҞǟŹǕʮϤɟƿűМӈԈΐƌѮ',
                                                        'value': '\u0378ƞŘɼΔϷΘȲΒpŷ΄īǶ{ҨѾʋ;ɆÔˎĩЛҵ:ˇƳΏВ',
                                                    },
                                        {
                                                        'key': 'ȘϽƔğǿĿСԕšԄͰЧ\x97ȱtϢŬ΅ŮŃͿшϬŶ҈ƦȄ\x87Ļŋ',
                                                        'value': 'φɸţ˧ѻҠ\x9eԘææȚʏӸ[)ҵȄŇ\x8bϿůȟѥЕӞʔКµˮ˹',
                                                    },
                                        {
                                                        'key': 'xϞ}ϓdϬЊÓ\x9bӣÌ\\ͳ¥ϸΕ˗ʼҦÿ',
                                                        'value': '¤ƿҏцφЕ^ū˕\u0380ǿϰҾȷʛϢţϛϏӺАЃΞԨH˥yԍљН',
                                                    },
                                        {
                                                        'key': 'ɠӨϋ˥ŴǘКʗԬš',
                                                        'value': '˪Ʉ\x9aѵ˹į˔ЮĝɴJņоѝȸ΄¶ÓĻԎ\u038bѮ½ƚBȹǔ/ȽҞ',
                                                    },
                                        {
                                                        'key': 'ӢɠȍɔƲέŁԉƨϱʕԁÈǦϺƈ\u0382ЅΦŅˌњʶХюэΔ҂ǒů',
                                                        'value': '˛Ëǒƶ{+ŢEӠʤӷǓ\x87ǋƤ©\x9b\x85Wԛƶл¾Ǆ҄ҋѫԞȲӥ',
                                                    },
                                        {
                                                        'key': 'ҺÓάϧǨƷћȎ\x96eefǻŉґ\x8fɓԌʞǮƹƙҀ˓Ѫȵσ-ҥҺ',
                                                        'value': '҉їǤƧ˷ԠԞ7фрѕ«ǅӳʈ`ҒУғΰӂʯԢʏҫǰЌƅːŕ',
                                                    },
                                        {
                                                        'key': 'ǏƿѕԒȨȢҽʄÍΈĭɅ\x8fʌԏÈϢżĻ\u0382Ҁб¿ӔҎԨ҄',
                                                        'value': 'ԪѽԑÓѐǯв˄ɵԭπ¼ƫ\x88ԓ\u038bȄί\u0382÷ӷƑÁѳ\x89ˆЦї3Ɗ',
                                                    },
                                        {
                                                        'key': 'ѕŧʓşƗҼȐͶȮӕɯĴĚƧ\\ʞ\x8a\x8bрұԧĝɹǙϫΒѼͿƕɖ',
                                                        'value': '±êiǑĢɒǻΕƸӢӐʺôœǊУ5Ϫɰsт\x82LɈʛʆКcƙL',
                                                    },
                                        {
                                                        'key': 'őϟǲӾƍГɮҾԉӈӓβĒaȺĢ\u0383ɕˌ\x94ЫŮ\x8dȜϹ/ƶ²ԩø',
                                                        'value': 'ыFˤúwӸ\x89Įƣӄ҃ӔоϑΥÝŕÓŃʃЦћ&ŠͺĆȋԕаŔ',
                                                    },
                                        {
                                                        'key': '\u03a2ɘƦҼҔȟͱÍԕw\x88â',
                                                        'value': 'Ȳ7ԣēͱș!ȿɓȝȓĄѾхұ˻Υ÷ψǱБԏŠÚѰy}шʘԭ',
                                                    },
                                    ],
                        },
                    'comment': '&ˤˁҖǤΪÐȝ1<ǫǤѫȐƌʫұʬiѸèҥѤǎĥЊıųǂƃ',
                },
                {
                    'keys': [
                            'δЗӒ˓ÇЭ\xadЭҏС˃ϨԭŐ(φ\u03a2҆ď϶ŸҔ',
                            'ӞΩп]сӬʩʹĆLǠșҽ',
                            'ѡ\x96ʃNˊЂϙ!РǦ/˘ɏˊTƐ҅ŊˬtDҿšʾ\u03a2',
                            'ӢúπƈΨȫʃęƉɉ҉',
                            'żпɗæ˖ŢԀNͽџđӪÚƭƿλƐƻ',
                            'ëɝӴîї2ғŭʌêɰǬÅмԬƄЉ˭ԏȊåÕҌ3',
                            '¼ȷˤӧUʉɋƛʲϡ˹\u0381Ԛ',
                            'ԒѠǰĤrЭ',
                            'Я\x8fӞɮcͰчΈȢąÚ҉şӷђʽҎ\x84ʲѧ',
                            'ĦΗňǋƍΓ0ĎÀ*',
                        ],
                    'event': {
                            'target_id': 'ЦĀʝӕ_ϿƆČɯԠΰϝѷǍƇšɅĉįǆϊȆϮ\x93ăƠȪē%h',
                            'parameters': [
                                        {
                                                        'key': 'Аϟǰ\x95þүӤrѐǵȄ;ϽʟҪ\xadʨÓʛӓČѽƘŰȁԃƋҹ˅Κ',
                                                        'value': '˛иӀdŒ˫ͻĸăǺͶµЂŰƑЖȸ͵Ϟ+Ϯ\x92ϔĒ҈ęɍΝɉʎ',
                                                    },
                                        {
                                                        'key': 'ӽˌϣХϻĿԪЂÍӹòӒęʴɡƗɌнÅЫĨʿέʇԮ¼*ĉϜϚ',
                                                        'value': 'ϣɼʨʛƉCÕɠɬƎà¿˒ΓǼҬ˕ʾͳóԏѹԘљ\x85ƹԎ¢',
                                                    },
                                        {
                                                        'key': ':ԤϗӚӊĄϷȜԮҘйȺÍЇ(ʈђѳˇȚeΪ\x94ғӴҥήsƚȍ',
                                                        'value': 'ȨΏǗɏ\\yóΐęπєӏ8ąѦɶŴ\x955Эβ˧ͼȢȔԄ˜Ά\u0381ā',
                                                    },
                                        {
                                                        'key': 'ϨŐԗѡ\u0378\x87ӖϠϑѫƬʀ\x81ƲПǎȹͶżǸӚԉʝҳɮ\u038dȀǤ\x8bÉ',
                                                        'value': 'я#\x9cѦːŇ˯ΰӷ˝ӴɀЖѼƜұŻҵ˯Ϗɼ[~Cȝ҉ʹ0Ҩƞ',
                                                    },
                                        {
                                                        'key': 'iâ\x88ÆɹƆӗɐĽЦлūU\u038bҖƔҴҰжĻäǸǸӧé˭ûǍν\x82',
                                                        'value': 'Ρ\x95ϙβʇͼý˱ɑӐϳ',
                                                    },
                                        {
                                                        'key': 'ԣƑȯəǶ˙øļ§δʹԗрŊґћЃщϙж¾҂ĵ\x8cӉ\xad1ǂÊʷ',
                                                        'value': 'ȜƓXʲǙΆïҐѦ¹Ȩǒ˷Чȟ0ɬʜ\x9fɩϡвÙ',
                                                    },
                                        {
                                                        'key': '˗¢ǁђ#Ś˗ǁ˺Ð',
                                                        'value': 'ZÜʠԢТ\x97ΟӿĔǄѥЇӉŇԗңƪԂ˨ȼƕ;ÑϡΜŨĎѢǏċ',
                                                    },
                                        {
                                                        'key': 'ҹζ\x9bϽȿx,ŤЪȒÀ©ԢΑгʒфφӭԆ5Ύˠ\xad!άЇΙʀǳ',
                                                        'value': '±Ѡ\x81ŽϾѮъϓΈ˃>īǇџ϶˄ʹzŹƑƹĲŕς҈ҏѧϚÙЅ',
                                                    },
                                        {
                                                        'key': 'ȈɫÁNË.ҘĀjңʈɷѩΥcȲ˩åϓȭGϾзƨęʏŴɉī×',
                                                        'value': 'ΟҀӋʾóϝ˝\x9bҷҊɜǚƥʩýΑΌϮҺӥ\x8cʦŵȎөќȽçҟΑ',
                                                    },
                                        {
                                                        'key': 'šѿȆĮӕю\x9cŻ\x9eӜӣәĥыÊ¿θԒ˂ѫˍԝǞėЈȎщ\u0382ϓè',
                                                        'value': 'ǟ[ơǲʨү]ӶpɼуĄУωɀҴĘԁһæąBɗœŃɕ͵ΐђɜ',
                                                    },
                                    ],
                        },
                    'comment': 'ԢϙԚ«ǶӠǃӦ\u0381téǲ)ІͶ\u0379ˇԋΦāǽŖȸ\u0378ȎŸӰßƱþ',
                },
                {
                    'keys': [
                            'ԄɦƁϐӪėŪʄӴчϠȜŞЀиΓŖƖԊϞɰуȍǬЎȩӧ',
                            'FӛӢeƓǚƚȨø˼ȝʞ˨Óпʯ°˚Ɲ',
                            'ȊҴѴοʗѪʰţӟĞƛ¼ƚs',
                            'ʏĕӨîӁҫɳEȸ\x82ʕ\x91҉7ӱ˽R;CϖϯȚÇєÌ',
                            'ΟĐŹƛьȱɯĚЁ\x82ŋßƟĽÛi˼',
                            'ʀ\x97ǼԊԟѿ¡ǋˆȒσʞņωęʁˠʗ˧˝ЕѥɟСyԏЊ',
                            'ȌѴϸČƗ˰ĳγńͼ ÐӾ',
                            'ЯӚ',
                            '\x9eĔźìΡaϭʖˍʻÑɗȤ',
                            'ъҚϔ\x97ȅӯ¥ÆʐɻҶˑDМГ\x8aЌҼ',
                        ],
                    'event': {
                            'target_id': '£ȅäϮҒξ҄łĢùǼӌѥϦƑѤΘťp˴Ǡϭі±ϭĕǹĕĚɔ',
                            'parameters': [
                                        {
                                                        'key': '¿čζѩûƔϠĵ°ĄƘѳŠȲɄвԒΏАƁȰƤӋĒѯЏ΅ϊŏÓ',
                                                        'value': 'Ӟtλ±ĥĺϕɢүƘԒËɲԠҏƽǪŉĿˤ-×',
                                                    },
                                        {
                                                        'key': 'ʩ˴vWϬǬƢӷӾ<ѤKҰԢҟԄ%ĵЉÔİ˙\x9cűΈ˧ǖԦÛŗ',
                                                        'value': 'ͼм˓\x96ͽҴ\x82ԫȕӸ£ƒʬʗʷҭӿ¨ɫȲҡšȋ½ţЭʷҀǋȴ',
                                                    },
                                        {
                                                        'key': '˪İ\x89Ēӕǀ7KӤϫĭŻȡȩƸ\\ȞΫБpɁaê\x89ɖƚ҉ӝŗԌ',
                                                        'value': 'эʅʹÙȮԗʉўĒǳӁʵIƶԭωӐʟ\x7fєªůЫΟ-ɧζǚȅƃ',
                                                    },
                                        {
                                                        'key': 'Ͼ˟\x9bуȶιʧ\x9bϿĎϡżЋϷ\x8cћˍəǡ[ΨӽтӕÔʹЉƂŶϴ',
                                                        'value': '˅ŕeÛдіʘŝ²ΧʪƮ"ԈɽӾalԄlƅ_ȳɼɉʪҿxќĐ',
                                                    },
                                        {
                                                        'key': 'χωҧȏɐ{γˁ˾.ρҙƵȊπÉ˃ȵʭҹŜťʧԋǼђħҡы\x88',
                                                        'value': 'áΙįơ÷ΎȭʮΘ\x9aÑМȐϢȼsɧӎɻįΟʪцΥҕÊъҟ;έ',
                                                    },
                                        {
                                                        'key': '\x9eǣƘ\x90ù\xadѽҶ҃˥£Ô\u0381ǟ˫УΎη҉ÕĝΝȓʧ˦|\u03a2Ŷѻԗ',
                                                        'value': 'ϣǻӛAґҗӿбƧĐҫѡԔNƧΔҗΖ0ȭŚϔǡĐЗͷūφǀӻ',
                                                    },
                                        {
                                                        'key': 'іΧƏ΄йԓϫɑ\x87ҫ¡˭ɲ]ô',
                                                        'value': '˩ÝЖȊΒʭоİϩɃЗғȫͷ҄н;ǿȷӆŧԂ˷êӺǅќśϡӀ',
                                                    },
                                        {
                                                        'key': '$ ҜȂš\x9eБơ˕˗ÅϽÐȽҶЀr\x83ĿИϙóoʌ\x98ҁβ˒ˋˉ',
                                                        'value': '-ɓÎȒĤIӯŸȩ8ĠѢҜɛ;Ëԑˇ#ʌƨдӭɀӗjԨɅ\u038bν',
                                                    },
                                        {
                                                        'key': 'Ι©ä˼·ɦĝД¡aʛʞoΆӎǄЫӋԆǽϋӊǀ*Ϸѱ\x91Нĭ˃',
                                                        'value': '®ȢѼŪӜʊǁèԑоóԖԉ\x8aϓmɥɐĮԨÉȭіѐƛ"ԙ×Ӄŗ',
                                                    },
                                        {
                                                        'key': '±ΜǜɞɳōĊΎӊ˰Ţ½ѵԮĮĸ\u038d;|иśǡџ/Z¯ʌӿԐқ',
                                                        'value': 'ÑƊϪ˥ĭϣΦԓԒtŔӕŕчвˌ˔ƽɝԁê!/ʺϒkJӭßЧ',
                                                    },
                                    ],
                        },
                    'comment': 'ÀԅЙʓѯοʹщȲͲÀ\u0380ȍ\u03a2Ӛӊ\x97ӷ˾ĢЃЊώÞʯЉj\x92ĭʚ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'master_sequence': [
                'ҙ',
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
            'name': 'ӳȶƑű҅ΘǕɬƱƣǜŰ\x8aȿѸtȫ¤Ğŧűȴ\x84ɱǣєĪʗƫċ',
            'description': 'ɐɤĥ˕ԈàɲԅʬǉPǃ\u0381ɼӿð³ɉӞӠɈcŮӡЮ÷ōΙΩɨ',
            'target_id': 'ɈɪН˫ǗǇˏҠϺ˛ԊưхыǪ\x91sж\x8dĸԄđĞԕшЌŅYŬӚ',
            'parameters': [
                {
                    'key': 'Ңʕ\x9cϕЂ',
                    'description': 'ɛȡоҷ˚¿ԆӶΔWÖ\x90ɀƐďǍɝʫƼÄӝ¾сŽŷӪ\x99ӿ\x8fԔ',
                    'default_value': 'ϼƑªƓŊǰƞ˵ÙҜѯƤӔ§ˌͻeʃԤQǐȠ\x9eȒϘùҧõëЄ',
                },
                {
                    'key': 'ÚѕɘıԘΡƾœȂ˫ȧӆ˝˵ǰӨőƩјȊŧȄɔƴ˖ҷʏүжŞ',
                    'description': 'îԌȰėѧʙǇҩɾʬ\x7fзɉ°Η˝ɩǔӷ˅ʫҜͰşƯ°$ÓǻƁ',
                    'default_value': 'ʭѷÂŏĮҁ˸ŏÛ҈ͿǸńЅ˄Ԑ&ÌʪǤќ\u03a2ĒȥÄӨԍϦĹǝ',
                },
                {
                    'key': 'ɑʌΚжɏƦƲӅӟњѽǛ@čĶʅ˜ԘўËǗńӉtђ;ąѡǯ»',
                    'description': '\xadȳʡђӫ˨\u038bҠ˵ԗБåú_ьʱrʘκǚǓɞʎ.ʍӨkÖT¶',
                    'default_value': 'ŲөϜʵɓЛį[θԛǶʴϰτԕƼԂӽƀđȐ\x84ΚÉɋӦʨʎҴϏ',
                },
                {
                    'key': 'ϦʥSӞſǿɱ΄uȢдӨҟӡЄѻ_ŤǶƫҟ"Ⱦ0ѾУǖЍЯм',
                    'description': 'ϫMː΅ςΛƋҚӌΆԀE\x92ŸĐř˩Ñ·\x98ҺҼѫ\x9c˳ȠƉțϜѯ',
                    'default_value': 'гӠεхƥŐҕʩ¼ˑŒӪҀ°ǸɔрҭfšaǱĘҋķºƘķ<ξ',
                },
                {
                    'key': 'ԠŊƟáʘнǃɈрȥǻė',
                    'description': 'ɫԠѦǌɎêŜÞ\u0379\x97Ś\x86бǙĤŸ¦Žȸ\u038bЃ˙ϚũϧƖŝƍϼҢ',
                    'default_value': 'Ӵ/˾\x94ɗӖò½ʈҴÜȋɒĉǌѿʫĚӳä˗ÀѿХ$ôҴӷƴƊ',
                },
                {
                    'key': 'ʈ',
                    'description': 'ɎʹϣwɃĻɷѣҴKiӌȾӒ\x7fӟҳƟ¼ɏĲûԉÒɢƏįόǵʻ',
                    'default_value': 'В\x8dƞБԘˀ˓rȼ´\x96ӈβЋİсˏɇǆď\x91X\u03a2ɼ͵ĈЅ˗ÿÀ',
                },
                {
                    'key': '5Ɂѐ(Ǘșǫ0ʕÓpʹϱńŜWÝƆʾΎćθЅȃď\x8fȃԁІɄ',
                    'description': 'Ədʒ\u0380ІӇĹn˗d+Ш}ŨͶć¶Ůƣ¨ΦÙǥѩДǭԟтʔ҆',
                    'default_value': 'Ӵϕӗ¡ЅɈŉˤ¬ѱźԗǿԞ7КԓőOKЭɘʣɂÖԒƋӬȆД',
                },
                {
                    'key': 'ʿ\x8eǰƦΣήʻúάmƏ˵ʋ¦ʢѨŧɚӎÁǽʘʿ\x95¯ʈa\x91ғ=',
                    'description': 'ȗ\x81ЂƕŠԎҥÂǾ·˾ғӣЃǊS˙ԎˤǭһʻҜȭζYý¤ųђ',
                    'default_value': 'ˣLԢȱԀīèëǫţԐΡ ǉȓ\x96\x8aӼđŖ˃\u0379`Κʇ¡ʿĊԦʹ',
                },
                {
                    'key': 'ÈɸŅɹͽЛϔҀśвŲѶҜѨӾªҡ˾ńѬưψ',
                    'description': 'кʪɆϞȬ§?ƫЌӁ~ŲɱдɱńǚԏД˪ƞÂӾL¦#Ѥȥðƞ',
                    'default_value': 'ηɡïĴΑƮǞƨΆũҜɵˑȩȔüώˌJӪʐ&ǔˍϒiʗԛȶά',
                },
                {
                    'key': 'Ԕ˧İ˷ʅȅZ÷ġͳ£xɑкԠӌӪѿ5ыͽRӸǆЧƵ˟ή8(',
                    'description': 'ƆʾԛïɇŘиAɠPʧͻȲȧʺǃӧǁuϵŶưl\u03a2ǏѨ>Ѯƞҫ',
                    'default_value': 'ĺĐöĻ\x81K˄ʗʖ\x8f˦ØЕеȟλǘĕ²ȓʪŎҫӤ҄ƯκͷǮ²',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ҙҍŗ',

            'target_id': 'ӈΊƉʝʠ',

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
                    'name': 'ÕͰŽóƊǝўԨʧvι\x9e΄ӀԤÙ\u0382ӇѪǅЖȝ[ͻ2΄ξGҢΓ',
                    'description': '\x9cȮӺ£ҩŨӞʓĶΔeXʳҞ¦Ȕ\x82\x9cȒ҄ǎm˦ьԪʀ˞γʴӧ',
                    'target_id': 'ʑ\x82ЅԥɂÕԁҢƝũΠÏӨΙыbòŴ|ˡMƜГ[ӇκӢԋ8%',
                    'parameters': [
                            {
                                        'key': 'ϦӦɠтǽ\x9b¾Έ΅ͼİΧɌ\x90ʫɕӱӜĂͶŭʙoс·ŭ\u0378ǜʤԈ',
                                        'description': 'ÈɊɀʈȊƏϓȧѤʟǉǾϑɼДӴŝφ\x93>ҍŊѦˆȔЙüў\u038dȲ',
                                        'default_value': 'ˍѶӘʇ˶ě҇đņ\x82ˍðħЃԝĦСè\x9dɂΖɍňƳϨÄʔʖɜ\x7f',
                                    },
                            {
                                        'key': 'іŖɬɾOӬˀðұӑЁҘҾѾʹџƄŖӏіVΊćԐӻЧȕȔϨΖ',
                                        'description': 'ҋƄȍ˽βɼË÷Ϭ½ԞǫÙЌCєǒ˽ČzĻɞƄŮЙą¬ӄ;ʎ',
                                        'default_value': 'ƨɄĒЉӷ^мʥ˱ӴňӅӳŎь@ѮүǸ\u0381ɛˊԨȠԅǱǬ˵łĆ',
                                    },
                            {
                                        'key': '¸ΫƽZăӓŃѼѬұц\u0379ĵåХҟɝĉÍȋьŰå\x8eӹқʔĠҧʏ',
                                        'description': 'ŋΏ¨Ð!ˍ\x88ǕöԚɡrӧ\x9dʉĪҁ)ˠ¾Ԡ´ϊϩ˓ˊǘƭʂΟ',
                                        'default_value': 'ǧгUҧŋΆřӚġĀΏʼǴåŤэ÷ņȂʣІĩҺǽдͰˇ@ӷƢ',
                                    },
                            {
                                        'key': 'ʪПƦԚ?ίuЉΑhˋį˯ͼσďӸΩԏɑĜԊľìɓԊʯҖȭđ',
                                        'description': 'j˫Ⱦ˄ˣΓǍНіOπέӍ҇Ѵˤ\\ινũŅйϫʹUѱŸQѧџ',
                                        'default_value': 'ɴҿƖѪŐũ\x9cӃ±ӅȌѥƃγѻьҌΪĦαĜТȰŰĮǔľȕɀË',
                                    },
                            {
                                        'key': 'ȐӒβƞʢS[ǙјɳōӞ-xСŧΰҦƊҔ~ˢǰ\x80Ҍ2Ϙ\x8cȳϕ',
                                        'description': 'ξÌũӳЯνǽԖΜѦɝǸюŪǡҨѫμŹҗӋ¸\x9cΔęʽǏЋǺɈ',
                                        'default_value': 'Ƣѣ҇ʘ҈ўǤɰͳѯШɽ\x98˒ͻ˷IɅӓɪ˶Ь\x81ϥ҉þԅØÃʶ',
                                    },
                            {
                                        'key': 'ŐÔҼŜɄϕͷVӋĘϤ]ʩŁһƾǡˢƐŖӗŖСǃʻΫΜˆƝȺ',
                                        'description': 'ҍǮɪɖÂȺϽǷΓ\x91΄ѓ\x9eȝĨǟɄ¾ЙĖɛ²ɬ>ɍďɕśϔԥ',
                                        'default_value': '\x8dСτʃͶåϗźƖʕѲȲ˕ÈƬԙҟ҃Цo˝ѬӰǵџЏҀyϜЫ',
                                    },
                            {
                                        'key': 'αŤϔƤŋЦµåƥ*ȪәȈŦϓȲӐȜйɘĄдήϻȆҵҝįЌЂ',
                                        'description': 'ϸԦ8ˆ˚ƝŚɥͳΪЅʢwİĵʿψȨ`ҬϮԋʰ˳ǟēʵ1ÓƑ',
                                        'default_value': 'Ɗ¨PǍѴĘŪԆǟХʍȳcWӯŠпč\u038dϲӌкǁʖ\x94ȉмʟķʯ',
                                    },
                            {
                                        'key': "Ƕ҇'ɳϑ/ȹФυŌ\u0381ňɴ:ґǤǯ\x95ʊɞҺɯ˜ʎJȯɨ\x7fҶʒ",
                                        'description': 'ʾξ;˰ΈĪǙȻјʲцǬqʱŒ˚ӂԫ·ɥ=Š+ȜǲԂӻ;Âѳ',
                                        'default_value': 'ЏÓƩƹбϙ,ђɻ˰ҦƌΞǴԉЩԟԪɟΣӂˋԜӐȿȀ¾ԜΡ1',
                                    },
                            {
                                        'key': '`чЕԦϘƌԛɎΣřКɡǗΌɯɣҺùӽӣˍҀĐªͻǬ©ӭĲƂ',
                                        'description': 'ĲŦ҅Єăȟј\x88ΞͰ\u0382iƆЭƏɴʢΪ¬ȧҌκΆϸɕůǯǣɱƁ',
                                        'default_value': 'ӉѸǅп·ȨEĨɽĀĒƷԌĔ\xa0¡ϙĹѣуéѽĀ«Ӳ[Ŕ˶Ͼǲ',
                                    },
                            {
                                        'key': 'ƇʯȅӀÄɻƲȎŅœÑӃӒżɘҌΚOâÇłʀàѵΏģцȠξƬ',
                                        'description': 'ǲΑԆɖɕ-ѽ\x9fɡ³ĥ#ӻąѪˤϽʑϡĳô˴ыҎưѰSǊˁN',
                                        'default_value': 'ΦҔӚɶΡǄ6ɋѿKŅͲȟϽɡŏ"´ӼζʠǟϥțȀʣΗȉɎВ',
                                    },
                        ],
                },
                {
                    'name': 'śǂϳҼƐчɷԬ`ʧɹϦɛаѴ˙ДɭРоӡgɦϫPȃπӘǨ¸',
                    'description': 'ǅ/ϭÒÇ˺;FĤ˼ūɿʛϫαԍԝȫмȕӬџʆ\x8cȈЎΗ{Ŕ+',
                    'target_id': 'ϧċÊ>*ФʵſǥˊˑéΨɳʑҷĽŨҔӏҪϖðҗVͺĢȢ\\ͳ',
                    'parameters': [
                            {
                                        'key': 'ŝ˻Ҕ\x9aʛωƽŻ˄ӘΛĜšÙς˴˕ФͲ\x9dǊԓѷљï\x89Űѻͻҝ',
                                        'description': 'lʓϥĝѸćˊDɘӠȚ˯ЇЖ\x94\x94ЩıˡûˑƩϽǋдȖá˼Șԡ',
                                        'default_value': "œɼʎ\x81Ӛ\x97ʺSтƂѳƟÜҩ҂ΜҗȃΡ'JƩЬҼͲǭǂʹʲФ",
                                    },
                            {
                                        'key': 'ӡ˄ǺўʂɹͻçҮϏ\x95º-ƢÒʀ\u0380ȶįϽéĎϻԜҮ϶ƛŗȳɒ',
                                        'description': 'ʽPɾҫ½ӞŷʒÞǘΌɆИԗÁB^ũϽԛԞpіͺԒҔϗϏU˻',
                                        'default_value': 'ąƮВϛηήώÛ\x95ĭ˦ӺňNǝâƜ?Ľ\x93ЙЮʑƎΤȗЬïӬ ',
                                    },
                            {
                                        'key': 'ēÌɝ',
                                        'description': 'ӟ«ϕưдѺż˺ίΨϽ\x84Щɼ@˅ȴЕиΓЈѶĺЕƗ҅ӢЏϤΌ',
                                        'default_value': 'ôΞňėяëŤŠ˟Ѽΐ/Ŗȷ\x7fɍԥÝʲѳįӀ˷ԗϪӹɮǳшӳ',
                                    },
                            {
                                        'key': 'ԛƿʵćԜˎӼӗϫɴйʁőҔЧȵЫɹƵϱɤŞѤԁ˲ΌĢΤχʍ',
                                        'description': "ÔγϲĢ˪½ʑȠϘˈ¬ńЄ΄\u03a2ɡѵĭ\x91B\x7f5ȧȧҲ'Ʈ\u0378Ʀ˷",
                                        'default_value': 'Ǉ¬ϭɽϠӇ3ɡψјѮϏƷŉƊȨǈɄħΰìɶJѠřʏɔïʕԐ',
                                    },
                            {
                                        'key': 'В˳Ӂ©ΕН÷ԢŭʱőǡʠĢ˒ӯԙˤЫώ',
                                        'description': '(˄\x98ɪфҤр¹ǘ\u038důÁάћӢѪȘoǗċҲӒΧǈţńНҡ˽Ѷ',
                                        'default_value': '\xa0ӱǔƩэӨσɳәżҔƼ·\xa0˛ʧԒ\x9aɇЀǃ˻њ\xadҗÊԁȟϱӷ',
                                    },
                            {
                                        'key': 'TƺÁʒΚʃǙřſŮАвgώѪҿ΅~éʆш»ϾČö\x9eϡȓ³ы',
                                        'description': 'ȄƾªȷëɅĹόɅҀǈČԧʟһ˺ŲĞqǗΡӣĶAçнʗʾɗԀ',
                                        'default_value': 'Ѯáķ\u03a2Ŏґå˒9V;ӫ;Ы_ƂϿήѿκӫŻУЛӅģĸ-ͼэ',
                                    },
                            {
                                        'key': 'ѝÀӴʢǏąʠκwEԁҊǗ½ϵĻȾԇрκÌԄđ˂ԦǖϛĠŻŃ',
                                        'description': 'æЉОԄȽЕ\x95ЎȜȷÎӧҦԣѢƍҹĮĵǴˏҪӲФqӐōţμŜ',
                                        'default_value': 'ȬƥǂЧӡҧđԨ˄ͿŽҽ\x94ɋǘ˲ù\x85\xadьžˢ)(@ǡѫ:\u0380ʁ',
                                    },
                            {
                                        'key': 'Ǔψʃ$нvȍūɺϷȚǃ˸У«ZƏ\xadnʑŚʭґĕӎ(ŕыҷΰ',
                                        'description': '|ȳɏʬсǬǮ2éǪѮΒËϔǶ\x9b\x81Ɨ˔ӐЖ˧ŭŝʺг²љԉǤ',
                                        'default_value': 'ˆ´лҥЪ8\u03a2ΎԍўªĬ>hԩ¢ȋЅӦȘҘʪԧŋҍƁǑаùÂ',
                                    },
                            {
                                        'key': 'TēϮԩШȋɟ҃υԪʭȀѓǻ˔ĄχҵͶŽïǥӿǃǆҀ\x8cԬPȸ',
                                        'description': 'ϛϮщϵȬеȂȤɞξʥʮѝԌϔяĕйǤĠĿÍЌÄċÚΤкɭҘ',
                                        'default_value': 'ԩΩш³ĶӝǕõ7ʥɓʟ˟ɔɥƁqǦĽΪęЕƏ`ǚϪõҮӆв',
                                    },
                            {
                                        'key': 'ʾđʠǐњŁĶȋÀǼ˓ȀϥϷʩƋ\x84ҍąʚAӨȶκOҵёӞƞʬ',
                                        'description': 'ͳϻДƠҿԅǭўӛʻϮħǃ£¢˭,ҍǶίΤʕ2ĽŎÚХǍƕl',
                                        'default_value': 'ͽƬþ\x97ȂϨ˽ɊȬмɵӷÙX³ϳǩͻǖϖ\x91ǝКҩҊêŶǭԁŪ',
                                    },
                        ],
                },
                {
                    'name': '˯Ċ\x8bԄˇĈȑ¸ΫϖԥăɢʤӄÎԀΧnǋɏÖ˄ӾöʀѴʺš¶',
                    'description': 'ǽαϹǟăŸȯžēҋŴԂD˚ʕʸĩȝͿŖοƕŭšӕҞ˅ÎȡŅ',
                    'target_id': 'ώǬФƂӡξϳҖӂǨϐҐȳˎѳЦґʒЛӘƷƐӴ˥ԙ°ƔǏЍӨ',
                    'parameters': [
                            {
                                        'key': 'Ҩʎӊѹҩ҂ҼӗͷʞƢñŨɝȑŰ\x9eĵŋЗӓ\x8eǕȎ˕ȯ΄Oˤé',
                                        'description': 'ȓXҰ$ǳȷεκ\xa0ǰҏЇÐȮХǶʅÞӹԢҢ³ǢȋҴ+ˠĝʆ\u0379',
                                        'default_value': 'ʢ=ЛȾɅ¿ȶɭҾłЫȯȮӯaǸЭǇ\u0383Ҿϟɬ¬εч҆ϣ˻Ċѕ',
                                    },
                            {
                                        'key': 'ɽʛ\x90ˌ{ͽЋǸСˣɛӁǀͻȎϩtɒ\x90ƪñ˔ȇӕʅžƨ',
                                        'description': 'ЅϘɥœđ]ԦЌӿҡԓĽѕτ÷\x84ϖǮӐԕьäʿæũͺϊ\u0380ʮʁ',
                                        'default_value': 'ƪÂǊΰȷӨԢԞϽĥ¬ƴƵԒċЦԨĀԅ˂ΐƐů˄|ԀɁȿӥȠ',
                                    },
                            {
                                        'key': 'ŪmүйίʵʏĐФЛØʯǇгӉƛéƆͻЩѲľȸxŗƘǩѤθy',
                                        'description': 'ДǹϹɓǏуqʹίЋџŐХԄȚӗ҆˴җɅf¿ŽͽԍˡԁǞĤP',
                                        'default_value': 'ʓRÄҡʊæѱʲӔʱĔҜɍГȧǅѾźўČˆ¶ɮȼǾЯӓӡӊº',
                                    },
                            {
                                        'key': '\x91ſ·ʚƻŻ\x94ȀЯ\x95ȤƁŶƅ±¤¼ώɰǧБǌ;\x98όхýƾeΩ',
                                        'description': 'ШңĔˎ\x86ɄϋƜˤȒŏʄƶӅȍԈҨвřĮÁçïʃğ҈ŷϩ;ǆ',
                                        'default_value': '˗ƿІɰƂʅIЌϩB\u0378%Ƴ\x9e]ƒź\x9dİĐÔˏʐϐԙȱłȩΊӬ',
                                    },
                            {
                                        'key': 'ǩζƷ˼ѕӦżγҡ',
                                        'description': '\x87ǤǪΊǕιʚǋǕ7¬ɔԚηЄ΅҃śϊоȈΕѠƭѥͿ|ʽǄ҂',
                                        'default_value': 'ӳ\u038dҔʤÍƋ\u038bˏЁĲʠĐԅȝĝƔτˈÚӵÄʍńŢóŠƷѾ˗Ӕ',
                                    },
                            {
                                        'key': 'ԖŜϰХGѴԂԈȊїɎȜƮӉǾΰ',
                                        'description': 'ӇӎΖАȋɚãÖҹцԀG\x85ѓϔ~ҘƿӦ΄ԠȞҚюƀǅҙÿØÊ',
                                        'default_value': 'ҞӶщӤWƈʱңʥƠØӊúύΕ³ǷҶмƻҨÝľ\x9cĜƌNƦѰŽ',
                                    },
                            {
                                        'key': 'ŔƵĘѝƖNЈαǅʠŹѮÎǆéϬ\u038dϚҳ¯ʼΔ΄Ɔ˵ĸƤνʌȖ',
                                        'description': 'ҊǕɏĥЗȖǬžԧƮөϼƱɁ҈ȽGԙΤɁЧȢӂѣƣғşͶԬɃ',
                                        'default_value': 'ČƤ4ɇɴҼşƋďȡ2uòk\x98\x8b\x8bϳŊ\u038bѻΜϡЇƤƕӉɾƪ҈',
                                    },
                            {
                                        'key': '҃ΆĠǱӼҔ˾ѯβʔČÍϹ3ӺͲɐ¦ȖͲǂӕȺ*tȢ_Ŏřͱ',
                                        'description': 'ЧʈΛΣùȱǬʟƺʍÁÃѱʍʙ$ŏЊ҉ȴяTЮɤÁãǵЋπ5',
                                        'default_value': ';ŧԣЫŹǻǎƙˊ\u0383ΔеÜϏɎ>\\ĲͲɑΜ4Δ˶ˡќѾě˃ϑ',
                                    },
                        ],
                },
                {
                    'name': 'ӌǉҫǜȋĪWϲͱĮƉ\u0379ʂʛǛ¥¯ӗԦġӒǕѱšʝэɁģŠӋ',
                    'description': 'ʅˀЕǼǥ{ƉƲđĿŔéˡǤÆˍωԔқƻќŢȶ®ƹєʀƂ˖Ζ',
                    'target_id': 'ҺPǪ\x9dşʷʊɍ\x89ÌƦȏʦОЖωԤ\x9c¨ʽ˥ȧӼөˍҎ҅ɞģѤ',
                    'parameters': [
                            {
                                        'key': 'ˏÚǃɧģҜȼĤÃ\x82ɍoϓ\u0378Ԁɓƻ5ɑ\x8aЮϦł"ӅϚƷДҞ·',
                                        'description': 'ҥȬàӪĮ·϶\u0378ɣưӅԥ˜ŉҩżÝŉŸŵӐéȩ\xa0Ӏϋ%РϢҢ',
                                        'default_value': 'ɰǏҬɀȯϴTǏӣҳʨтʐŵȺǷҤԬȱǬ\x9e˦ЕŇ\x98Ơŝ˛α҃',
                                    },
                            {
                                        'key': 'ǂҢȰđӻыӕΓ@ԂĪʍȺĽĐɞ¼шȩ҆ɝȃюΒӛǃwЛ!Ȱ',
                                        'description': 'ʌӃÚ\x80ɎԆͿвçƈƟϬȞԕѐʜρВɲѳҫπXÖǫƧчƩɈϣ',
                                        'default_value': 'ŨhѬǒà˕\u0379ţǄоҼҋ\xa0ŝÚˎǿέðǸϩϵԁ$}ɃήƤʳУ',
                                    },
                            {
                                        'key': 'ΆϨԫͻ\x9aԎmǳ\u0379ƺvԊ(ԇ*ΑĴ^·ɋχDнȠ',
                                        'description': 'ɄүЛɑЙĵĺЄӜӱşɖʶΠķхů¨Ƌʸӑơ˼ð˶ԛʠӘɰȠ',
                                        'default_value': 'ɄҘHϩǦҖϴðɬǊӸ\u0378<ʴʵƝҜӜēơоѫŞȞȅƳʂʜϐƭ',
                                    },
                            {
                                        'key': 'ӘҩяƵ˸\x81l',
                                        'description': 'ԇŻǺßƆѮĽдϪėҺÿqПρIϪ\x82ӗ΅Ҽ×à\x81ӱǑҰɢԘԋ',
                                        'default_value': 'ҸǼӰω(\x9dϩЗȗң\x8eOҫȾºѡŐ\x98ρѽʏǹǢӈƷɠѧƸɃρ',
                                    },
                            {
                                        'key': 'EЮĦ˚ͷ¯ʄ\u038b҇eЌȜÄѹӬέŗǀžԐĽ\x92ϲԜѷǍҳɀCω',
                                        'description': 'ĴƁΟɣĐѡцήͿ;dǛСѸ;ʢЛː ӊŭҼɅԊҟѣəѥHń',
                                        'default_value': 'З҂ʝ>ʨʹmȊӸѣщę\x9bCţ˪ȨЀ\x84ƖȯbɱĐуɋҢĦ\u0383ŵ',
                                    },
                            {
                                        'key': 'Ĺș˃',
                                        'description': 'ų\xa0ʗϵΓІȱӞžǤÇлɍəђϞϏKɭϘȝŖѶɽ҈ƸѫȔƟb',
                                        'default_value': 'PƩņUƓɬкәÝÀʯûȡҋÐΘƦεʢ)Œ\x9bʅ0˛ǩӯ˜ħϼ',
                                    },
                            {
                                        'key': 'õӾ6Ρ΄ȲȒŊԮƱŨƗϧγѨԡıùқӾÏŅҍϘrϕқːŕ¨',
                                        'description': 'ȀǀɜξԮŃωáɢέБΕɿӏϫȪδ«ÅϪśƲ\x93ɿΆ\x86ƓƴѶŦ',
                                        'default_value': 'ë6ΎŹƠѰʸΉTǴƿ&iѼҖ˲ӵӿ!˾ΔЎ9ƨ\x83εǱҗϰɅ',
                                    },
                            {
                                        'key': 'Ѯԃòǒ˾',
                                        'description': 'ϊ:ʮȩƱΘˣҊĵÖÃEQͼǳ9ͳƴ˜¹ҋΨЌ\x9d\u0379ŻƆѝѦĀ',
                                        'default_value': 'ÁΥŧȰАΒҤßԕҘӝ-ÿʙƉāӮǊáĔҋӍǿɥĄ·ϪŸǹс',
                                    },
                            {
                                        'key': 'ØѲķęŲ8\xadƍΨğƾňʪʭή3ё˵ύȗѱԋVƽӤ˭˃ΖǃŮ',
                                        'description': 'ɈϙƽɫŀΙ(ҡǂѣkǐF\u0379ΫȞҀɏŪĞǾϖʫϼӉԠĲԫžӌ',
                                        'default_value': 'ѐˋ\u0383ƽȔѮƨϯȨƿLǣwԣЅíŬg-ċLʃĠ>,ǜ¹Ĭǖķ',
                                    },
                            {
                                        'key': 'ʥˎλÕ\u0380ґОƻɃYϺВʫОĝŖӢɴФʧЉƁċ¦ͻǭǶ˪\x9dζ',
                                        'description': 'ΛԒŢʁͿќdУӳНќήȤƂɶĞ²ґ˚ȏюЅȠİǀƢпҝыȺ',
                                        'default_value': 'ÏɘȆȫɆ҉ʿЇƈVԐԆқŬʃҗɖҲ`ĦȀίӘ˨λѵԚJƾΈ',
                                    },
                        ],
                },
                {
                    'name': 'ѷʧΈχѢЗɾ3Γȫ\x8b\xadĲʃһƽɕȌˀ\x9fƐƀɕ\x8aˏϛ«˓ӎѲ',
                    'description': 'ŲΩҫЖԡș˒\x87ƾϣϗһǭŁьөȸǬԗӸτȒˏԘÁҷιʺҬΌ',
                    'target_id': 'ёӡѧºǢrͷɗȡǉȯǸʑĽƱLӑͼ³\u0381ӈŻɼȹόĔ˜øȉK',
                    'parameters': [
                            {
                                        'key': 'ͱÿЌāȵǪŨñƘэÍͿДɰ˅ȼaʜƖҒŪÂ',
                                        'description': 'ρǘʈɃ˵эЄļ°ɩҸϊ]ӭ\u038blěёˎȢʬǷΨɨ^ԞǐºŰп',
                                        'default_value': 'ǲlÜ˷b#?ǮЅKĮƩǹɵ»ßмĘΦҹȚ°\x82ĬϫҥÄӆˮȫ',
                                    },
                            {
                                        'key': 'ЈƣəԊɵˁŀͶ@ɷȋǟҗԖWƚΈ·Ɩ϶ʡ(ƆĳӃ\x8e@Ϊ˽F',
                                        'description': 'gŢɸ®˨ˠъǉɈёԌÉǩԕҚģȪϯ˅ԑȖ\u0383ȯƘɨͳғҙãț',
                                        'default_value': 'Ƴіǲә˹ɒҗŸùԟư\x88K¬ʵϨ-ěĜɐҺȸʥ:Uˬː˦ѿĞ',
                                    },
                            {
                                        'key': 'ϮϑυɜԆ˶ēÜrƂϭҘȑǑɗĨ´Ҩюʑį͵ƅԉϻŨIʠʖɲ',
                                        'description': 'ύ\x8eGɤ˖ԟTɭјɆԂȈӽ\x9fšƢǢê\x9eҾϠσȭɸ˟żňĹȶö',
                                        'default_value': 'ǀň\x8cМʽӋŕƖӓғīɧÜԂʟΦΜ¦(Һ)ҵϝˀҨƓįŉРK',
                                    },
                            {
                                        'key': 'ϸίŋϖѥȧEўґmғ\x9dƫŢѭǅ˳ΘŋϡϝģƁOűśºŭȶͷ',
                                        'description': '˹Â\x83ҀɗśŬԠűķϝнƏưŇԄ˘īʔɝͶĝʙ8îǭŪ¿Җų',
                                        'default_value': 'ϱƠӟʕӚƵɾʽʗʢЖ\x9bğ˲^ʣнτĩ,ĵ4ƅŷ\x91єνЂȞњ',
                                    },
                            {
                                        'key': 'Β˳Ëǎ҂ȂȓƟӶȧǷǨ3žͿüɜԝӢАĻХЄ¸ĞɕӽɓƆe',
                                        'description': 'àьмǐă.ʎɚbκǦkӎąˡƣWF\x86ɘƩÕΤŞϒθ\u0383тƮѹ',
                                        'default_value': 'ɈıƐηʾĈɁзɷɔØŀ1šԓƍ҅ΟЖԔƠӑǷȜɊ\u038bӹ˓øѠ',
                                    },
                            {
                                        'key': 'ҠʛǽӒͱľ¥ƛ§ƹęƲŜȏmʭЈŢөõMǓSʬÒҺɪҜ\x94\x8d',
                                        'description': 'NWөҍ\x9bŒϝïī¼êѧ¶ɉ\x81ҳ\x8aηÛçȴƘюΓ¡ǺäĿżѩ',
                                        'default_value': 'ĝÂĻİϛūȷʻΪΒƽÝòƍȾεȱʎ\xadЯҗɉƈȘǸŤmƴƛđ',
                                    },
                            {
                                        'key': 'ҢǛɗǙʰɯ\x7fƎʒǌӊ\x7f˫OʐУфɮϛ˦¨ЁVԄʷҚːҶôϢ',
                                        'description': 'ѺЋέҏɷӐĕԧɬ\x88¾μԟĄɩΔɈΑԄ!ɭħѽΓҭ˃ŘŽŉư',
                                        'default_value': 'ƈФɟαǶѲљɠ&ÄŭŎǳͺίɶҬ\u0378ǔ\x97[ѶŗʞӷƢěN¹ʌ',
                                    },
                            {
                                        'key': 'ǈʄȺѹA½Ɨԏʞ҈ÌχűƠΚӅӧ\xadóЌ\x87\x91ǫΨӭĦӔ˳ԫљ',
                                        'description': 'Ԁ˲ĂėѐԞĿ\x9aʋɻYԠcԜ˅΄ƞEѓǐÝϋѤòЃɘϞЈŘ˝',
                                        'default_value': 'tзʁřƜ˰˟еϨýѲ˃жϫԒΩɹĶǬȶơԔԁʩƴƠŗøĚϵ',
                                    },
                            {
                                        'key': 'ГũηĢǃėĚːϛƠϮԆоʆ˖\u038bѕ¿ëǕƌΪҭǠÈΗΖϥˮǧ',
                                        'description': "řɧшӉǱ¾ǡƦėɬɔgҬӟEѲӄʫѪѠʹő'Ⱦ˳ƌɬϦтȬ",
                                        'default_value': 'ĴҝżȏǅԔˡɵ˚ɢâѧŝѠȚæjrдşȖ҈ͻ˷ӟƬʭңɜƽ',
                                    },
                            {
                                        'key': 'ԁтļʭȘƹáðϬҀ҃ԇɖȮ&ǔƈƛǿġnʔӜ²ƞǂЗʱ',
                                        'description': 'бϽǢηϷ*Ȏ|Ѳ1ϝÚxлΆʝ˲чϲ¡ČȨ˶ȥ˛ɓǼũБÓ',
                                        'default_value': 'ĝң\x80ȶǳ΅ηĀԚԢáϸγ\x90\x87ȥȢԋĈѿŉηϥĦөұԃАŭv',
                                    },
                        ],
                },
                {
                    'name': 'нsσ\x96Ξ£ɪÄΔȂɋɬźÿҦѝċʜöʨ\x7fЯŕ\x86ǄŖ˕ВƯщ',
                    'description': 'ŽҢѴӆʡHӚϟЀіŘŽυåϘŹв҄ʣ˱ͲзȨ҇\x84ȚЖˏ\x80ɴ',
                    'target_id': 'ÈǬԡʕЕ\x97ɖϕΦїêΞЅ\x8b}ѴғЭ\x99ƶɆΦɰǷņ!\x8dύǘ¦',
                    'parameters': [
                            {
                                        'key': '\u0379ӲФѵƆƏQҙϪȌˀťȄíȖԐŴå˹\x9c\x81?ràоʒʰɵӏӫ',
                                        'description': '\u038bѹǮmńή\x9cƘXύѲȐҁϸ}ЁȃɄͲʫԊȟȡͿǏ¬ƕìűȄ',
                                        'default_value': '\x98ή·ӎ˒`žӬħԐƾǾɱʒÌˀϷĮʣŢɸ҅˚ҭԟѷʢΐRȍ',
                                    },
                            {
                                        'key': 'ԎƑǋϝǸ¾ˋ½пϗ϶ԡƊƱÓǙǥХ',
                                        'description': "ȣԍÜñʌǖ\x88ѵϤӸҹҖɭƢɈǙÃӒ\x9f'ò\x83ʵʼƑ¸lƳȬ\u0379",
                                        'default_value': 'ǒÑψЗҌ\u0382ʮȝŅƄͼйrŏɷϗɔпÕ˛ʆCҀTϳѴҺ?ŗδ',
                                    },
                            {
                                        'key': '\x9cκБϩʉǘȿӹƘ˒ŢҦȑ`ϩҡǯ˞°ȫÙȯ\u0379Дѹ˥ѮҵYǵ',
                                        'description': "'iҝʤӥˡáÁtҟδ°ǨВ\x7f˘ĮɔЦɑ'Ƭʽȗȳȓϵƒȼ˫",
                                        'default_value': 'ĊӝґѼʟΪĆMЬȪϩÛ҉¼άǯşѨ«ƧŖÍ˲ԇԭώҁΛϓђ',
                                    },
                            {
                                        'key': 'ȗ˝ŐĦʋХЅѣҢŲɸέoϱʄԚȥҵłӍˠΏ\x82½îǩȧǧ',
                                        'description': 'ЦǎΞϨʎѺӎȞ»ƉVԐ)ѽŭҌĤҠʧ˽ҖʩԈŏʚӺϸǀІ˒',
                                        'default_value': 'ŲȆÌƈϯîƿӅΆПЩ}"ԑόӻγʐɷƖπϯȘ˶Ć\x8c9ūΙM',
                                    },
                            {
                                        'key': 'ț',
                                        'description': 'ΪвǺŏɻȓľ˦ӫѢѲɈѻbˡʱΕь=ʬҔ΅ϝǚǸԔЉΈȕɇ',
                                        'default_value': '¯#ӂϜЯʺɉ͵v·҉WƴǫЗͺӓ҆ãԩɲ¿ʆĽƅҿųш²Ĳ',
                                    },
                            {
                                        'key': 'вѽüу\u0383Öνɧ±Ǎ',
                                        'description': 'o\x8eðȗ²ɰϋŸŢϊÊɒǒϗΟ˝\x87ӒƃȘԬЭźɤϣʿ\x87Ԇɸƈ',
                                        'default_value': 'ũċӃƯw¤ƪӥŔCҮ\x85ʥ¿Аͼφɬˇ¥ɳҰǒŊϬĞƣ*ӱ³',
                                    },
                            {
                                        'key': '\u038dеǭҙԛш.Ѵ@\x9c˞ȢώĒϜ',
                                        'description': 'ζШŋɒѪχʼŗЪǢӊĬ˱ĔӠϐТ˰ʤɅƮCǁø҇ǑϿԊϳ(',
                                        'default_value': 'ʺ[mϩ°˶ŀαҬǷӉǇʡŭγ˝ĭіӗё\x8cRtI\x84ԏŀӭӟǇ',
                                    },
                            {
                                        'key': 'сѦңʵԮñϤʳ',
                                        'description': 'ųǳԞϛý\u0379ϴƀʞͲʭЗԓҧ˾а϶ӤďҔīH҆фѼǴђ]ȴ˞',
                                        'default_value': 'Ь˟ƗϮȖҺωȣԧĿ@˔ɕЙ[żЏʍОӓɥ˳ǟ˻э˸ԈȪΤÎ',
                                    },
                            {
                                        'key': 'ɡЩÿƥϯĶ˸ZΎƎƕΎҒŹрγƳ\\ʭ\x8cϔƘĢ·ΊЏ˸ϱ',
                                        'description': 'ӓTʰaɅÙǤrԚϬѩԇ˦Ǭ®|ɍĮθY¢Ǐc\x88ͷ=ɕíưè',
                                        'default_value': 'ЧȴɋsþʥѪ\x97²ʗƚϒƼĚĆƼĺȉɧȻ˷˸òƺäǬ\x98ÄĐɯ',
                                    },
                            {
                                        'key': 'tΙɭђÃѰΓŃ',
                                        'description': 'Ēʍ˪ʚ\x97ѽũЄOӷʾҤϸϚǕĻƬҵπј¡×şƹǈļŕ:ʤӒ',
                                        'default_value': 'Х\x8eɨҌ҂Цƴ˞ЏȀƣǆѡԭlŒѸƅ˞ǿŠϟΞȩӨôƘ¬ԛ\x9e',
                                    },
                        ],
                },
                {
                    'name': 'cʕѷ\u038dōqө҉ź\x94˝Ԩ\u0380Ƴà{ʵ˓\u03a2ńʷàƚςʨȬnɨƾϪ',
                    'description': 'ϺҾȉɫǩëŰӷȷʪɬƪЊǢȲ\x9cØΆ#ũˣʥяĘ\x8cĽǫƪҲǸ',
                    'target_id': 'ԠɂǾ˜ϰ϶A¬\u0380ȻÕΆʸЌǂƙoжѮϹБʇҋɸ\x87˟γҸɟʴ',
                    'parameters': [
                            {
                                        'key': 'ϓţƸȞЩ˝:Ë',
                                        'description': 'zкǬaǑŸưϝ΅\xa0ͰљӮ¹яθǑƋǬĠˆŰȧǚ&RɍlƊɵ',
                                        'default_value': 'ϹӚǒŖ¨ʹpɧǉԘKˌƍͲԣȚɯҌϔˤȵҠѤȣӿEǲЋD\x9c',
                                    },
                            {
                                        'key': 'Ə[ɫSǬƌǧǄÕ',
                                        'description': '2ŻažѰǠњȇʙӼȬѝ}ыԩьïǭЙĭДɥѬηɺҪѹƬ!ҋ',
                                        'default_value': 'і`ʽǨ±ĄƅκЊšίΗƢіƆoЅÖǗʶ·Әчԓȹʱβҕ˵ȕ',
                                    },
                            {
                                        'key': 'ǖЖǿԇψϴɟWӨȈΏϴРЭˊԢҪȕŠǿëľʍÝU˫ʾIɎê',
                                        'description': '\u0379ȝЌAÛөӿʛӎ\x98ǃ½?˰˖Ї҄ǝǘÉƞϷÁЗЋɟɓŗ%ƥ',
                                        'default_value': 'ϨȗľÕƙŁÊʘԟѲžʘΜÀ\x92лӦ5ԝƉ÷)`ѾяγЧѺƂǟ',
                                    },
                            {
                                        'key': '϶ˤǟƅɚąiŻƎĳðΛԠ\x90ą\x9bϱЂѺɏ\x9eӜʘ\x8eϡԕþŦ˽Ӑ',
                                        'description': 'ԚȪϽшΔuȹġŅǅŎєǅ˃5ǜɣɴ\x8eʚȝͶİɼȓҽԖą҄ť',
                                        'default_value': '³оəԥː\u038dмĠ\x82ʇϟԑ\x88ɵȵˢӒ΅ǁʌѰ\x8bюƸҍɴΛÓѥÊ',
                                    },
                            {
                                        'key': 'ȂŚϓф˴Ȱǒ\x8dԓӣĂ˥УɵÎH˵ǭԃ2ˀ˫ʾώȁ\u0382ǊìđÙ',
                                        'description': 'ӒШԭьÑѝƕԕϣҟğюŶҺ\x9eќ˜XѾµųǯ:ZЇĀKĻˎĬ',
                                        'default_value': 'õƺLʼȪ˰ΆzºԕϮŶϣÏȞǈѩɏ\x8bɿĵƓǸНąҩĖȀėǜ',
                                    },
                            {
                                        'key': 'Ūξϧ^ѨmǻƤřӜǜūϪ',
                                        'description': '!ÞȲÝʰпϟ˕ώҪʈ˚êԙŒѤÓƚȭԥΌ»İ˰ϺɝåѢɪН',
                                        'default_value': 'ˆľǦʹĘıŜĂğƨЎ˲҃İǫŕƗӞԉŶ,ȴШ˦gЁĎƜ£Λ',
                                    },
                            {
                                        'key': 'ÿǺʞрɉϤuø3şĔĮ˗ξԂģΛʛ³ɰO$εԟƾ§ғϪ\x90ŕ',
                                        'description': 'ʱҎϞҿФҌµ¼ǕжєӖ®Ϗį˒ɤ˞ǏŘȾҜζчћϖԒċÜБ',
                                        'default_value': 'Jˆ\xadЉϒɤɁсӎƝǚбƓҳȗϋȐ\x89˺°ȑƋνӟūӑфȓ˭ş',
                                    },
                            {
                                        'key': 'ӸɅϭԪІ6ǷĵͳÚşU½ʃıĪȟϜˢǀɼŀzӎ\x86ȰhķÃĖ',
                                        'description': 'ɕӣǁƿƃ˞ҷċƻԓԘHӢʩƈȧӜ\x85ƊΡΙəїʁǌíʉȅ\x85ǻ',
                                        'default_value': 'щɜǤÓcӣ~\x9cèġíк®0:ĨϿĒţɞʕB\x91ʨԜзҘĝД[',
                                    },
                            {
                                        'key': 'ɹҷі)ԍ΄ț6',
                                        'description': 'ШɬĎΦɆʂΩ\x8cȈҰҟ˃ӆιЬˇƫɢϜʮԫĴ`Νëʧwðѭő',
                                        'default_value': 'ÁШɫћӆϟ¡ӾӨ˄ҷɆïŐ\x98Ҁ\x8f\x92ƎԢňϻχώÏ·(΅ҝѶ',
                                    },
                            {
                                        'key': 'ȿƸȅǠҭ˽ɑӎ×ʹΆӕдŴ\x84ƾҥӝʅϐԭ5ʜɋ',
                                        'description': 'ӛèơӌɞ+ʒ˻ЊƄüΜƷӱϲu\x82SƞаábŤÏРǏ˃ξ²О',
                                        'default_value': 'СĢӔԭ+ǱɹĕΖ˨ԤɊ˚žƻϷПҜћ~ǫʳͷϓ\x8dĠҥˢѸн',
                                    },
                        ],
                },
                {
                    'name': 'êΆǮϿԪǟӦńӓŨѺɥԠЮ³4țѐñ>ɏʻđɞюɒvϔ҂ì',
                    'description': 'ˋԣˡɍƷӰßѪʌıƆˮłğξįʑњÎƢω©Ǹ\x80˯ĵϟԒѓō',
                    'target_id': '&˜ƏΥ\x8cӁɖϢɞ\u0379Æȡ×ǍĄɹɣ˯ŞƍОЎ>ŐšƍԠƩҢŉ',
                    'parameters': [
                            {
                                        'key': 'ЙŎԊ˚',
                                        'description': 'ɄÇφɪӱƂåϣӏ˺ʟάÜˤԥӐ˺҇īψͷ҄Ђˣōԥ4˱ҷї',
                                        'default_value': 'Ɣ˴ɋϘčŗĞϕ·ҔʟËҌlƑņϝˊı4ʿѱˣԆϓ\x7fӭĆ˪ҳ',
                                    },
                            {
                                        'key': 'ÖΖDәѐ³ΌИƔˬҋȽťɕǈûȲɣǺΰ<Ā˃!±ňȢђɺ\x92',
                                        'description': 'ċǓЌɦđԞĤƻǫвƁƂǉ΅Ɠ\u0378ΌԠп\x98}ӹkɶDԍ\u0383Vаӷ',
                                        'default_value': 'ʂѽŷčɋҏˍԊЈȲϏǂƇɱ+ȂZnҬǖΡˁƾȥŲоЏԑÊК',
                                    },
                            {
                                        'key': 'іµԮӺӖõʻяɲɯŵϴǌö\x85Šǎ4ǨʬƎ$ĪŜѣčʦˎȰ˖',
                                        'description': 'я\x82ʅϱӿǝáʳӅäōӕѻŁǉԖħԏѾŊƒȱΈKǜ˳ӜʳɰԒ',
                                        'default_value': 'îɤ\x82ΏҘǢϿÃӛè#ЧʎĻԪ˕ϑэӠǼÝлҸӫʢ<ʊʒΫ˛',
                                    },
                            {
                                        'key': 'ϋ\x7fȈÊ¨ɌŒɬăԖ˄ǶԔӽΗɜӈQуȼğЩǆщ¹ɰçɦÈѰ',
                                        'description': "βŮӴЧίԊˡԨã±Ç'ԬҋƘčӌɋҭӡˋũȤӣĨɸƖˡ΄ӣ",
                                        'default_value': 'Ĺļ˅ɔǎũČѝҰΝϗƦʊġÑЉ˼ƫяϓҮ\x8d϶ƮΞ˃ϝΩҝƌ',
                                    },
                            {
                                        'key': 'πƪ%Ɵûжƃ˧',
                                        'description': '˺ǵŘǱѱ˖ӃғԝʐВҎŌǽϞNǦӼԗϖʙɶм˧ĈʱʶʬFƤ',
                                        'default_value': 'ņÑӠѠӎʬϫϘ(ɧѕϯǺĢǷύ/êKĖҥĥħ˄ȏɩɎȄ\x93Ӳ',
                                    },
                            {
                                        'key': 'ǡύɏδϊΚƌ¿ѼΞAԝǏƒċʢāϿYͺ\u0380ӰȁԎ\x9bwч',
                                        'description': 'īȯǿͼԋþ˭÷ýƒ>ÊŝÄµmȟӸLʛUñɷϯҴ҄(@ǋЁ',
                                        'default_value': 'Č>ҳɌļӱӣǛ¤ɤǕϡώʰдŻîÎԡȧŤѣ;ŉHƇDʉnɧ',
                                    },
                            {
                                        'key': '¹ȰjӾпÔūɑîʊǺǥɣԧΰˎʺˁҕĚƊƽУĚұҟБBΤє',
                                        'description': 'bӃӰ¿ӁɉзӇϑҖ˴ΏɓѭӆґRƳǬɬãFљ0ůōігĀ˸',
                                        'default_value': 'Ͷɚԏɑ(ýӮΓϔѩ¸ӅБϟɕΜŃΣƛˏ˛ґǙԤϩϱԧ¬ǔɏ',
                                    },
                            {
                                        'key': 'Ѫ´ɦͶĶҜԎϩk\u038bєβѠϘŰZö˔ϊȭǩâҘǊ\x83ҒüѤ~Ї',
                                        'description': 'ʱӐψɧѾÙȂ\x93ƀӪҬщӏ҆ɓҪϔȷӴƁԏƯΝҗϚΡɌɀΕ«',
                                        'default_value': 'Ćnÿɻ϶0Ǘʮʙϩɍ\x95˕ĒǉňНѾ\u038döϚϠ£ɳϵԪ6ϖƏѹ',
                                    },
                            {
                                        'key': 'ɲğԆʈ΅ćτ΄ӊʑ\x9fӋҬͲǶiĺśГҦǰˇԚЯŻƕӰǞҶG',
                                        'description': 'ŭ·ǥҀҤǳĬρʨipĊȍƒƾѥɗʒ¾όӻȎ΅³ʱȰәѽ˜ӽ',
                                        'default_value': 'ҫȭȀӍИʚΞҋјĩȽø¦όɊʘԫqƣѩӸɗͷ\x93ɣÁǱǋ£ɲ',
                                    },
                            {
                                        'key': 'еа',
                                        'description': 'ĚϞȽ˜\x8dӑǚQhƚЋˎӈƠŁ;ӚҊђ¬tʆŤŰƬĢȩȡȾČ',
                                        'default_value': 'ʷԨÕSʀƞ;Ʒ\x85ː£ˈûйýͻСǃȼƠȑ˵9ΙI¡ϱгǶԓ',
                                    },
                        ],
                },
                {
                    'name': "˅VΦƚŝĜÝÔã«ǟӝӅřԗƹǞ'ÌǓ\x84ҷԣӤӿˤƈőҥʐ",
                    'description': '˕þǫɳзǒӑȒϙŔɜɳ\x80ǣ˭ӣϗŚ~ɟ5į8ƝôƷ˛ʒȦ˒',
                    'target_id': 'ԞȀΕƁ;ţǘXғě˱μƞ³ХԋǼʨ\xadɛȨĽąӈźɂԆ´ϮƓ',
                    'parameters': [
                            {
                                        'key': 'įȱ',
                                        'description': '˄ҫÑ˵ǁǽĺņɰϰȎ͵êʁλϕΖ\u0378Ӝ\u0379ӬʙzŁóҖÇԏɿЉ',
                                        'default_value': 'ƯϮӍ˚ҽˌƑϷŒϳȏˈΪͷӯΥҡэņ°Ƿ\u0381˃ˬǿhԙ&§þ',
                                    },
                            {
                                        'key': 'Ҙȁʝˍ"ёҸ©ˊΠɏϨ¸ƀ\u038bʰǠάôӜӤ9ŀϿщНǿdѽɈ',
                                        'description': 'ʘЖԨԤӍюɞџԫΝњҊUѵјȱʡQ[ƔϊɻϞ\x9cǸĩƂéȾ\u0379',
                                        'default_value': 'рΧϼԚ×ҴǀϯԜǕЉϾ3ΥɗȴƶˇǒӽӬа˹ȥϳ§ϓ÷,ʣ',
                                    },
                            {
                                        'key': 'ıϲʇðĿрѳа\x84žȨÏΥʨʪƸŰǩ˭īʈ*1Л',
                                        'description': 'ăɖ\u0382Ͱʄæ¸Пƣ\x98πŢħ˹Ð\x95ѨæÝŇɞ²vŦԭĦɷБĭ\x8c',
                                        'default_value': 'ƻџ3ɴ\x95Ђ2ЕĺΫԝǞФ7Ưζү\x9cʻğʣƸ\x93\x95¯ħɐ_ςǡ',
                                    },
                            {
                                        'key': 'ˆҰŻãȅɏӋɀ˃ԍ\x9fӚ*ȊѬԐhȠĞŷBŴ˚ҍɡȍoĲьķ',
                                        'description': 'ύϯ˱ѶĶÿɋþȏĚɗĽǒɖʭº\u0383˄Ł\u0379ԋӰĤ#ҫӈ÷ή^Ѝ',
                                        'default_value': 'ǺǦӅѲFЬ·Ǚʥˢſ˺Е»ΡҸǎθѕИªǌ˵ώɜǂȭ\x84ёh',
                                    },
                            {
                                        'key': 'ΜsǅɌԙҠüʬЯʯȘϾӇ4ϫöӞτPӕ˟ϴŦvƺΪʤʹ˪ȣ',
                                        'description': 'jӰǋʷĦЙӫΪəʈО\u03a2ċϪЦŶӭʜʁԤԭԥǭćʠ\x8fγΒӅˤ',
                                        'default_value': '҅ǬҋΘȊĂɗŚ>щЁȉӉŐʧŪѥҢǼƘϸǉ+ӥNĿԓˌˣϹ',
                                    },
                            {
                                        'key': 'Ėǃ}_\x9cӔФŀɟӢʻӡŶǑрѦҁ\x99ұƌ',
                                        'description': 'ϾѰčϱѳϡӇǰÃǽó¼ƫҡ҃ҹÁфВʼæʮ|ѻƚŃ°ӛŌӗ',
                                        'default_value': 'ɼѕɢχʁҗ\x95ȡɤлǑͰȵʷ±ŭъʀҭѓȴфǫҨԚϾǐ·ǼԒ',
                                    },
                            {
                                        'key': 'ƸƤόԦӕţ˵ɞʃÒȟ˵ơѵмƎҕţϦϝ˵ϟĞѫǞCɭӊ\x8cƽ',
                                        'description': 'ŠȆɼѰȷˑƦµ\u038dζʀ҈ɞŠΧȫȎҗРǮfɆԬ˞iцȏôʲʆ',
                                        'default_value': 'ŴuŸӫРΞ\xa0űѫɭϑȅΝʏϣűɩҴ\x95\x97ɭԄӵʚ˷æ©řȽЅ',
                                    },
                            {
                                        'key': 'ŌȄÜџοƩɿȦɫԧŔ˰ʈƟΟŹϖƄʌÒńſєϢΩ.Ѕ±πĳ',
                                        'description': 'ȇƍƇĬӧƩѶǚTŭˍыſʊïǠ|ʶƢʹřҦ˻ˡǣ\u0383ӂǛӤң',
                                        'default_value': 'νŒõµƠҏ\x8aʆť˴ѿӐBЂФΏӬ˛x\\θҲюùɩÍ@ȝΩ"',
                                    },
                            {
                                        'key': 'ԋˠŤϮɣїƯәʬ',
                                        'description': '˱ˀɨύɐƳƔÜҋƐ˛ɐ\xa0ʑɃ³ǒūͻȚȹǎ˴ŻɤҞƾőǹé',
                                        'default_value': 'ԮχҙӬȌˣÃʄ',
                                    },
                            {
                                        'key': 'ƚÄӧӏɪĜƪƗɱѺғōëǫŲtґȴɰŢèĄЗ',
                                        'description': 'ӀɐϷîLƐ$ƔпѺīҸ±ӟ=ЕʣϵсˣȥįΣǢӡĬ}ƾ,7',
                                        'default_value': 'Ǆ<ӠȒŮҬЪˌƳʢɤɃÚĳńɌȠѾŢѡŝÀѻƻ˞ōуʅ)ԙ',
                                    },
                        ],
                },
                {
                    'name': 'д|ȷԖԖ\x91˵ƯΜ:˶ʿ¿ӜĲ\x9bҞˈɃҰӑƿҏO-ӷΥʬԐĲ',
                    'description': 'ЬрbEΔčɟ˞кˬ|ͰαʱͻȈĎÖŅ϶άфȨ\x83Ғ5҇ũѢǔ',
                    'target_id': '¼\x7fƖǧʶϣӑ¼ӎǸήȹҞʰʨΎ\u0380dǤԅͳоƃĸʁӦИĠȕΞ',
                    'parameters': [
                            {
                                        'key': 'ԠӃ˦ΞʌĮƜͺÐǠǋųȣg˃ĭˣΩӅŉұωø΅Ӓěк5ʢá',
                                        'description': 'πɐÉÏŁǼ˛ƁοϟΫϷć˟ύȗÐʁŨścӭаƉ¤ѺƠƠ˒ǽ',
                                        'default_value': 'ŇCɨŨì˪ʠɳгɥŌɣПеԈňΰχˬҪuǵ+ЖŇ˭ȈѰк\u03a2',
                                    },
                            {
                                        'key': ')Ϫʑʣº:\u0379ӻԓΰЉ^ҙӦҝѺȓϪIь϶pǇϱȹǥЖӈΫȮ',
                                        'description': 'kɿѳʍ϶˭hӨ±҄ΚƃDƧҢʛӢԃʠΎϡ£ɞΛЖ҈Ȱʰκʈ',
                                        'default_value': 'Ōʸ;ðđбҶӨ҄˪ɣ˞ǆԈѶĬlbƢˬLѣˮҜÏ\x9dȑҦҋƋ',
                                    },
                            {
                                        'key': 'Ӌ˭ƺӹǃőЄӏôȗɜ҈ӣɛȲïεǻ¦ɫκғӽάԨT÷ʔЊƠ',
                                        'description': '˒ZԜHǻΩɻ\x8bSӊ\x93О-ȼ˼ˎŮǪÔęˮё\x88Ȉ·ˈđԄ=.',
                                        'default_value': 'ìЏϓɏɗѼˣÎˉԓYθĴϵˡВʺ\x8a°фїÐӌűĨыgƥѝÕ',
                                    },
                            {
                                        'key': "óѺȀĽλǬΏѷ¼Ӷ\x8bӮDČ˅ÄɹПЦό'йˍИͽāў\u0379\u0381ŵ",
                                        'description': 'ɕ˪ǈϟǃºДѢѪȱӬéУЏȆӿ҃\u0379ŷŨȾSε˸\x85˨ʋÐĆĴ',
                                        'default_value': 'ŚȽЛԛЂ΅Ȭȩ˶îǜǆ\x95ʲȨѲʻӟʈӋӡ\x830;ϓӻǦôǹǅ',
                                    },
                            {
                                        'key': 'ȹƤήŖ.ŤˮŻ0ǨȮìǤxȮ\x9cѼʝʩŦȌþþӃ^Ɋɤ\x83σÖ',
                                        'description': 'Ӳѩ˦Ҁ%Ԕʰҹ9ŀǸW\x87Ɯвk\x91üƅǊ-ſĂƀ¼ƯϳÍϷӻ',
                                        'default_value': 'Ŏɞ¹Ǐ˟ͷΨԜ+Ѕʒĉ;ѷ)оƯøϿƸγЋѹÝԠ˱҉ǁåƄ',
                                    },
                            {
                                        'key': 'ǱŇ˦ȹӠ\x92˸ŗßwӲũʴʟȼ\u0378Ƅ˫ǷԨĊѭÅƻ˾нʻȸȦǸ',
                                        'description': 'ʓϣȋȧǼӢ˕ҷɁsɊ\u0380˻<ъ©ȻѪ˙νˉ?żǤÖȩƱѳϼэ',
                                        'default_value': 'ȌѓıʝȢĥśOĐ\u038dĚËќɤÝJȾљWӀтĶԟƆlÄˈԞӇ¤',
                                    },
                            {
                                        'key': 'Ŷ҅ƹͷͺΣ˥ЯĦҿ\x87©ϼ҅əϸǓԕɸŝɍɦяě˼ʹѾӯίǃ',
                                        'description': 'ĩ¼ĈΞʗѝºǙ˥¹"ΫӚſǱўƲɹ\x97áȢɍвҎӑǩЭŚɌı',
                                        'default_value': '\x7fȗʑɼчǠЇ]ҾҵŕЊӱʠǃԊˈ\u03a2ӔĎʢΙǟʺГΠ҇ìЛБ',
                                    },
                            {
                                        'key': 'Kˍ;ȘĴɌћúȍȼȨEЮ\xa0ǆŇѩ\x8fǠтȘҧΨƷɀʭ#Ѳԓȋ',
                                        'description': '˶ӎʍʵѓТǶИɌ˯C\x8bӳȷҕų˨ÆΩ,˴ȸʂÂɌŻʭȥǲǻ',
                                        'default_value': 'ƲҲԁ˄ćʥ\x7f\x8fӟУÌZˀʕȆ˯ÔҸӭϔ˦ǯЭ\u0381µVj;\xadҀ',
                                    },
                            {
                                        'key': 'ȟŢªȝūǁϪ>ҳвűÓӫ#щʺˌӑǑǉƱˀŹďǦŪӣǙ϶ǹ',
                                        'description': 'ҵƀԔ@ђjѼȩªƯǖ[ƨӉˏϙȩÅƇƙWɱɉȓѥrЋɐȳф',
                                        'default_value': 'ʽѠȚ\x94чτ\x8fˮ҄ҭцƮʇ÷Ѩ¿ŠĶë\x87ѐͺФΰɩ˽«Ǎǻǖ',
                                    },
                            {
                                        'key': 'ǜΏъĴʙżNȔUѻŋˍʚӵʼӄçȔcoxχ@ҍԩĝѪӚ^ķ',
                                        'description': 'ČԋőԌӳϐ϶үíɰ˥\x93δĖǝŦӨԀ\x85ѫυɴ˾MƉƮƷŋàљ',
                                        'default_value': 'ǿʜЏ/ĞțԑɽǬʽ\x9aɈɺϸǄӰɍ\u0382ɩŴ˱ą',
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
