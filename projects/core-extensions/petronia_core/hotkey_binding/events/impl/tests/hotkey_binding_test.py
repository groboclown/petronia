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
            'sequence_type': 'sequence',
            'keys': [
                'ҧǸèI3ЕЂԒ˅ҊȈ:Еȸѓɔ',
            ],
            'comment': 'ЁԉɾȭàɴƔǥшűʅӻü°ԝϛþÐ\u0382ԓǮȁìЋBЦӟӃӤ@',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                'Ӣ',
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
            'key': '}ϚӟɳƍғѬʲıƐƙŘ˷ȀҹðοĖЄƄɲ1ɚ˪#ςӞъцÏ',
            'value': 'ИƅҾ\\ŖѪü7РԂȿǻˮΏƺ8ʞг˃щԅю¶СʸCѩӣųſ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ԓ',

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
            'target_id': 'ĽИəϭЦт2Ȝ\xadԇʢϱуÝÅävσяǺюΥʴƝҥȄӖǆĽɤ',
            'parameters': [
                {
                    'key': 'ϥўИГ\x92ȄÇӌƱÙēѵΙˢҪҔͽʧĈwтȱʠǊ˓ɮŏƚɴϲ',
                    'value': 'ԮȀЦ°˱ҮηӹĕНΊҗ҉ȥͺ|ŧҚэĮ\x92ԟΫĐӸӻ|ɛˤɒ',
                },
                {
                    'key': 'ӌƿҧǒҊÅϿƇƺɹŗ«ȰɶЍӿƾͺϗȄǱ',
                    'value': 'ƐÚĚ˂ưЂΛӧЦѱΫҘĶџnӫŜW¤ĠԐȪȻŇþÎэĊŲӛ',
                },
                {
                    'key': 's¿ѧ,ƌVӏѾӱȱƷˏҤљ˴ȵ\x81ΈɛѵǽȞGφǒ¬e҇ӦΫ',
                    'value': 'ȶ\u038bϖΌ|˭ȌåƶғɻӃǚаˉ¢ȝȨԋǏ˅ѹӶƒǡйàġ˹έ',
                },
                {
                    'key': 'дѝч0ƁǩǬ',
                    'value': 'ϑýˡǈԨúƶdԣǿ˄ȴҪiƚɕ\x96ϞϣƆІĀɞÝȓȑԥʳ:3',
                },
                {
                    'key': 'οŞ%Ӂ\x88ѰÉɢθ\x8f˗ҌϟиϻШԡЪвȷө\x9eʵɮėήӈˌȂҮ',
                    'value': 'ʷΊǮ˨ӳɷ\u03a2϶ʹӂ a²ǁʉįÝӪʁίяЄ˜ɴҹ\u03a2ԟΓʔӣ',
                },
                {
                    'key': 'Е˝ǉѦĽ˺ÏƬƃǞĩʇӇ!ǒŰЬȁųÇśӮӮԮǔЀѨ°ʯ˞',
                    'value': 'ƝˬȬӞO÷ŊŨʮwԇʎȺϼΡȩǙɶ1ʂ®ŻʮϨ¹cϤκѸƢ',
                },
                {
                    'key': '\xa0ғĨơwȘ˛ÀǟĄɕͰѺӝόȈʉƉҨ¿ƆġxƁhƒʮZÆ˩',
                    'value': 'ә˼ԤĆ\x80Ȱɛ˛\u0380ӋȰϯŭüçć÷ƭ£ƐўʜȘӏʣхϹųαԪ',
                },
                {
                    'key': 'ě˵ѾȲԥʹǑǎƇԣ§Ǻӟџ˓ԠʲрҧƔМs\x81',
                    'value': 'ʩǭˏȺŵǣŗĈҞĨǿ˝ːԥǾŭΟˑƁζȄ±чȩʕҹǩȹɫΌ',
                },
                {
                    'key': 'ƟԦɅģĵƙɡΣБʸɩϐȶȲǉūŔʐŷǚ\x86ƛ(\x9a!ТΎúӈƨ',
                    'value': 'ýÆ\x88а¬έ\x8aкιӼǭϾФĂÉʁҕUҼЍÕӘңѨƨƿͽȋдƈ',
                },
                {
                    'key': 'ӨVǇϾ',
                    'value': 'Ưӄӎϛɻ\x89ʚɃѽ\x9aθҏžҋɩϠŇ˅ǣҘ\xa0ΰ΅ȈƢʴЎӽӣą',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ĩƂϋrA',

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
                'ĸӒɒѡԇđ',
                'ȒːΎǾŰ˼',
                'ǒȴǽéɡbȖʛ\x8bǖ«',
                'ǟѽˁл˞щ9Ć.ƔӚž[ʨηӷԗ˝ʦĥ˙άɴ˅',
                'ˉùѪyԉҞО8ӴԠ&ƯғҞͲЫĵӯǄν',
                '\x83ҜϓӵΟĕ',
                'Ĭ2ҨӲƕгɣȔτΚ¼',
                'ŬѲƱʛ»ͱÈͼϽϽψȅʕǄƙһĳǮΛʁyӨ',
                'О˛ӯѦϞɹѕ/',
                'ΥҞȣёȾƳ¸ҏіûʶӘAΓɘњЅΏͿ',
            ],
            'comment': 'ˮʚƒίʐЇƐƑԨ˰íȑɲеƈӨеÖ¥мΠԝёԡЙԡʇАƠʹ',
            'event': {
                'target_id': 'ƺѩÍͿēѱʖЧѹɀӚǮ˄uHЊyɤVÏȽŞΎѷ˂ЏϹϸоp',
                'parameters': [
                    {
                            'key': 'Ǆ',
                            'value': 'сˣϊˇ(©MϛΩǩ\xa0ǱɽŨȵ1Хd}Д˹ͲɢǹсƸ°ƯӔʹ',
                        },
                    {
                            'key': 'ԟѳЇЄȞПɱːæΎcożʘʻϥͼƖƨĖÓЕЭ˼ǟ˴ƭ}ɽɾ',
                            'value': 'ȚϚʗʤǝǌʨЩıӵǜϿōƧ\x80ȗdѹӓǧɊҭʈлŽʎԄĒˌė',
                        },
                    {
                            'key': '˰қ¹ңƹа@ɮŴѕϖǛȸБιԈ#Ԯ\x99ŋȯŠ4ϞҥҖŭө',
                            'value': 'ҒwɃŶȹȫʮȍǅ-\x9bʚÈƾʠŭгƀ\x87\xad\x88Ǟ˽ϡЅɨӊƎŽӘ',
                        },
                    {
                            'key': 'ͱΗϜĊԩБɗjҁʚίϔǎİϔŪbå«£ɃȺʡŰЍѓ\u0380цȾΟ',
                            'value': 'ƆӺĸӷÂΥ\u0383ȕȎѴԑðSĎѢцʯơĊ\u0378ҎѼсƛ\x90©ƽ\x84¤ǌ',
                        },
                    {
                            'key': 'Ďԣϳȿˋ#E ƆеƐǦĞΈƍǬōCȴʈɽƝȸ\x8dήȿΨΠÃӌ',
                            'value': '¤ύԢɏɀʵяƍīżҷӏŅŊũŋÇ\u0382ǞКɌήӚŴЅӻԨԥР\xad',
                        },
                    {
                            'key': 'ʭҿЖ8ɐùҊ\x9bż§ιԖФѱʫɎȬʧľԢɬͶÔǋϗʋŴɥȏҍ',
                            'value': 'ƏШŝP˘Е[ϥѶÚEÒ>ΚŪĉӛǚƮȏĹΝǫҺǫӦɞҏџǇ',
                        },
                    {
                            'key': 'ơņˍéА1ŲʥǬԗŅȇǵЯ6ûъIӀȱėӓӌϑÞɦӦÇѠˍ',
                            'value': '҂\x9e@ɲҭҵҺȼљą\x94ľŎÈÆǥDӃɮӜȩ)ӕGƣÌɲϷҧŅ',
                        },
                    {
                            'key': 'žĊӟȓɴõǫēϤƼɑͽ¾ÎSԄʞҠǵǠʪʌǅӦΠρ\x88ˌ΄ƽ',
                            'value': ';ɬ¤Ѓ˙ċƿЅlǅҦЂ\x94϶ǨуІķˊλМƔnϋΘ/˨eϣƲ',
                        },
                    {
                            'key': 'ϣҴӪŐӵВņŏȀğÅ?\x86',
                            'value': 'Νά˲\x9cƩѯòĽ¶ҨΏ\x94ǄʪӻxɛɲǥĔĆ0ɿĹɛƕѤϭĄӾ',
                        },
                    {
                            'key': 'ω\x95¶ѧǀ~ҙбСϬǃϤΨԇ҇ȵȕӉǾǘĢǥȪkԒχӖŧш®',
                            'value': '½Ñä˞ěͶЬŸɣΤǎΘѹ\u0383ѪŐыҵįȉLǛғ-ОďʝӣÑ˽',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ұ',
            ],

            'event': {
                'target_id': '|ԓ˧ӭԝ',
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
                'ƱG§ųҀšɯ\x91ҡҏ¨',
                'ӶŲRԎɮɽ',
                'ɑɎáҨȒ2ʯūҪƷȍӃɀ¾зûϽϿȂöήȶУϧ',
                'єԈ',
                'ș3ғϚɠΧΉʬ',
                'ëȆϥσǸҎϟʘȡ^ϲǃΌԢΘÇɅҞȝӫВ\xa0ʔ',
                'łƑąûǈǨöǙïǸȶ&Ŷʡ{ª#џÔɅ6ԓ¢ӡƳϱ',
                '\x93ҜΈʭűɝʠȗȊʃė˭ϥņԄ?о҉íЖЕͲͶĳďδϰͽ\x7fW',
                'ӎҘɸϩƞ',
                'ͷëĭÂѕ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ȟ',
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
            'key': 'ҧΫĭĂƐȐ\x8e\u0380\u0380ЇөʧǠǓˈƳѫRƷUԥȾҢɸϜϾHȋк˟',
            'description': 'þӶЖłІ·ҨοϋƀȹźͽƹȨƲsΟśŕɐˈ˕ԏǄˇ¼˅ԟǘ',
            'default_value': 'ƁƈӈӞĻǟѕĢ˝Οɭͽć¹ǰфνҤѾϛġŨӝȅǢȜƄҜεſ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ǵ',

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
            'name': 'ϯĕ\u038b\x85ιЄÒΛǀČɦЛ\x83˷ÝԎĠȨɕˊȚˆҾ+тǁѾӭӦԬ',
            'description': 'Ȧ˂ˏЙȰѮÙЖԨȮӧӼΌϙ"ȬĘ\x86ΗtħŸǜѢρҁęɃϵС',
            'target_id': '°µÑ˰чȧƃâчʦĉыѫʢĳщӪбȳФEєǑУȰ\x88Ǉy/.',
            'parameters': [
                {
                    'key': 'µ\xadĜ\x95Ϙ҉ɖəsñƁǿӱɣԔӌ\x80RʶˤFHύȪϨӠOƜΝ ',
                    'description': 'хĴĄӷzȭÐűԬҵӅф<й¶ɲ4ӴɅΗΌИɮƁ«Ӷ;zӼϤ',
                    'default_value': '\x9flʝңʧћа;бȖӃțɝŬΥrĪŞ˱³Ӝ©ԣ˳ͺ҃˃ƇѬ\xad',
                },
                {
                    'key': 'ЅȰФХϛɊˋ\\Ȯά\x8bёƚ®3łĩИѸʫǲǋìǮ҆ҧ1ƋэÇ',
                    'description': 'ǽɚӼГńѧưǠǣǪɏŠŹε¾ØНŸζӳƹÚʸʶŷLаuфȫ',
                    'default_value': 'ǓğΑԖһ´\x9cЩǪӨ\u0382ȍϗǰÏϏʯ@,ƹ\x99ɺÔЮ!Ҭт˥ȥщ',
                },
                {
                    'key': 'Ќъ1?ʅΩÏҌǗÏΈϕɇЩӪƗѽ²ΌӣҝҰħӴŘƢ˷ŨŎʂ',
                    'description': 'ˤ\x84ӹŎɽÃwč[ǫɐʛʢƯwɓȕǗďΦc\x84҈ԡԓͶ\x8d҃ÛӔ',
                    'default_value': '˟Īһϑ϶ɷƉÐɹɹŕϮʨВƍķŞŧƤΝʙȭ˽ąŬʙдTȏԞ',
                },
                {
                    'key': '`\x8eƻyЦɸĖöŸǒ',
                    'description': 'ӤB¨ȇϛ΄ġŔêǔǼиԨʂ˂ʠlƖɡԑħşʳΰӁĠӶҐαӨ',
                    'default_value': 'ûɎw˟еûVǏɓbȳȌ§Ƅ¸ʿõÞ\x97Ȉя¿;˨}ĭҚχѹ\x8e',
                },
                {
                    'key': 'ɣИ·ˆƠͻЁ˱\u03a2ǋ\u03a2ӳ˩ԦƣďvϔѷȚUĸ',
                    'description': 'ʋРѼƨÑӔЙYӕƧЉ©ãʋúɎҸ´¬щ\x92ÚεӨЉύЀ˫Ωț',
                    'default_value': 'ƒɥԅ±ҠƲӂ[\x90ȆϏtȗɲȧşξǄďɤȀЉϛŢҟ\x9eϟшōʘ',
                },
                {
                    'key': ';Ȣ+ŏӞ7˲Іͱ\x84ŨʶċèȢĳų\u0379ӥѿȊǵȨҬ\x8fˌоίΏɆ',
                    'description': 'ˆҫҠ\x93ō8Ȅї(ĄԫĘϥѷȷҤêƁЧғ\u0382ǪƤɫ\x95ͺԙªƳł',
                    'default_value': 'ҨĖɫØyɽϵƈ\u0380ȧ҉HǮcăԟкʀτŚōҺήʾκѡαŞδɯ',
                },
                {
                    'key': 'Л˟',
                    'description': 'QȒ\xa0ǧɗүȥ{ȗ\x92цѝ¿¨˸¿άʹӈɔʛЅˁɩƨçȒˏɩ^',
                    'default_value': 'ȩ¦CʑѪƨΜÉϟ҃ϛIҀëYӾфϒͲј\x9bɇâšĶȸжϟӸ¡',
                },
                {
                    'key': 'Ɲ$ôƁȌόќȵǟɚŖľɀуlЕŖ˩˨ДӐ΄ӑŠǂĪɿŉҋȉ',
                    'description': 'ŬΗÒ^đǬȃΠrΌԈĄʎс¤ʍɹ¯ƊŎҹϖƫύ5ʚ£ŭƀ\x94',
                    'default_value': 'ԖѸԏҽÏғhХŻъǹƺ˧ĴđӤϚǵĠĜϩȃԀɾʠǥтƚҎʯ',
                },
                {
                    'key': '˳\u0382ѰЯϭѭϟɌżżÌͶзΐɐˀēȩWқѹ˳ϓң',
                    'description': 'ͺЈĸСzȣϖϲʧʽԪ˟Ӣ\u0378ƿҹ˛˟ʏʪØŌʕ˻àҪΌĒԧщ',
                    'default_value': 'ǼːĲƟ¢ƀTŴ\x9eȖԧ\xa0ǆɹ·Ģ҆ƻяŇʍӂ.ϭѵèϿΚŨѢ',
                },
                {
                    'key': 'òˍ΄ΞƫҮƳ˥ύōķ¥ԧѴԙˇÕӌҀϿ\u0380Ƣü&ίʅʣ˄Ĭˊ',
                    'description': 'ĜΆΐɊɑӼNwŚɺψԜȰΏЁ½Ó¢Ʒ;δȑ/ŴʎҹҲ0Η˧',
                    'default_value': '\x85ĊÂώǏȒϬɴĘ+˜ȼɹƃȿˤɽЗҬŽ\xa0ӷnԅ҂ȟДÝԦȍ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ͷϽϐ',

            'target_id': 'ӴѸΉѩk',

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
                'target_id': 'ќЌΛњʹр˦ȶƏȪӰɈȃÑԑưɝØѤZˌêƸAɰ[\x90ÇȷɊ',
                'parameters': [
                    {
                            'key': 'ОĥЄĖ.ӸњʫѾ½\x9cĔýͲʨGԫγĘˣҲȑ\x91м3ʕͷƴȟӺ',
                            'value': 'ÒӼ0τǰʁ@Ʃʛ\u0383ΘɷďΉȾϸhˀȎӐƸʾʩəΣҮǍҘzȍ',
                        },
                    {
                            'key': 'ϣԬԉϢϵƅBÇ\x9e;˖VŢȈ5=ĳÄӶ҅wɑ˳ԣ\x9bѩ˷ɾΣ˹',
                            'value': 'Ҹ\x91ȃ˪ùԧҗɒЎέЩΔ3²|˵Ÿ*¡ҾPȴŻŊвеξÇCǫ',
                        },
                    {
                            'key': 'ΗFÝĎ½КːGɦÇԞɘʴӋǴƛŲƹҍǬίpūЄ¸˚Əǅοő',
                            'value': 'ˌқӲň\x90ΎV1ŏĆОkİƧғʮԑUƉ¸¤ϮӈΝȬҐǓÆɃ\x8b',
                        },
                    {
                            'key': 'Јʤә;ћƽǭćɆIąЫ\\Ҕ҂ɐѬƥȊǞԔӈǀͼʪ"ȩ˖ǩf',
                            'value': 'ɶȒĤƟϗåā˚ʊĈʷdůƺʉʝ҆ȈȯΊɝӔӢɲͿbϔҸ\u038dҼ',
                        },
                    {
                            'key': '˕ΩȣuƅϛȈĚѨцˣѨͱĥȌǢ]Ƿ\x9aЖͷPɶM$ȲĀaȨǣ',
                            'value': 'ɢЍӬĝǣ\x9dġÒƩӰȉӇÝřӅԓLhπвȬкǕĿȢ˜ԤǮԈʻ',
                        },
                    {
                            'key': 'ѯġÏÂiΆх',
                            'value': 'Ϩ½¯ʸŅ˛Ѧļ\x86εȬԘ|ɯ˷ē˃ĀŭňϾǠǚüɭüɲŶ˅ʚ',
                        },
                    {
                            'key': '\x96ԐʪӥΫҷΝҽԈȜkН}ĸςҁ˲\x98\x95˯ǁǚȚŞėɆѬЀϱȂ',
                            'value': 'ѦюȰԏƈ#Ɯˀϴ˭ȝÀȑͺħҝʣ·ȟʣԤwѠѢŊŪӚʩ\x8aƯ',
                        },
                    {
                            'key': 'Бƿ\u0380ęҳєÝàϪʷGАǛʙɵ˞¹ӚͳӯĞчƳç͵ĥ\u03a2\x8dɏɴ',
                            'value': 'ѣƻԧŨǽʖ\u038btϿȂľνн\x91ĪǨ¹ȥϡϻ˗ǽϛ˗˖ƴЩъϢʒ',
                        },
                    {
                            'key': 'ҥÝãωΉӓѵŹĂ\x87¤ˀĘҏʋҥƄˀF\u038d˂ѫ',
                            'value': 'īΰêПҺȪÚΓŖԀȲdǟʎĵʲƌӃ˔ΦθҦѮȬτȅσʄŞ=',
                        },
                    {
                            'key': 'ӄΉZӫӬΩӚQтаҨϟƦұӅҠӿȅѢǴęɮɤцµΥȰBɠӛ',
                            'value': 'Пʦґ\x93*ϿŊ¼ͺѢčѢǷϨʼәӍȸZ˸¨ȋýʬӤͷҲȃŐX',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'ƄΰɈˬȜ',
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
                'ϢɜҘĔąʙӇ˯wp³ǯǹʹқ',
                'Ȋţ˅˴ԀПώʱŐ Ȏùÿ®}ʟ˳Íϻ',
                'ѠǄѭîņʊԑԑ˩ǖўż',
                'ѽêWà˸ȼ5ˆœĞѿ˸',
                'ǠʶËԎϕŚ\u0383Ԃɥ˹ɵŜѓYӖ/˙ӱxɹ>ґĤ\x98ǑԇŅ',
                '|ȺѤĿξӣνϿӂ\x92˖ƖԃЍшzȃ',
                '\x9ašĊ\x80ѾьjǻӢɳʜҳǖǶ°ϝτԛȈ[ˡ',
                'ѓ*ɿӜЫοέѼˌʫǶɫ\x98ʬǁЪӌҨ',
                '˜v',
            ],
            'event': {
                'target_id': 'ĥҶѠîƳҝĬdȞзΙư ΖҰѤ\xa0đȳ\x91ӊʒǹζŎȀԖªʠļ',
                'parameters': [
                    {
                            'key': 'ȓiʰ0ąʘԋɳΗķγϰϢѕ\x8b\x9fԎEĽНįƈ¶ӢçʼɯȠßɗ',
                            'value': 'Ң¼Ɛ˧ʊʖ2Ȋ\x97ĦΒκɞɕȻǡ˜°^J\u0379Д\x9cˌʴΑʻ5ԕǽ',
                        },
                    {
                            'key': '2Ή}ӿѤȘŕˉǍĔґʈś˄\u0380ӥȳѶºѮ;ǭʹȗЯӎķɟҏӋ',
                            'value': 'ҴΌԞˠԙZǻɀԃӸƕԡΒϝ-ŏĵ˻ĭЁ˞ɛÂѾɠͺưʣďĪ',
                        },
                    {
                            'key': 'ʄ˾\x83ķԔť˞ʮ^ƸE҅кБNȟEφӴ˞ƖɕŘȤчȣԢĵҰӆ',
                            'value': 'ſм·ɌŖϷvǁЛĆ[H$ѹʩüΎχϲśʿǈƑǊʭû\u038dϳʒl',
                        },
                    {
                            'key': 'ҭ¬˘ÈԨҨƛ˄xЂӰˣȞʜǄӇƂ¸ĘʁϜ¤тζΪ3КΖƾΒ',
                            'value': '\x89peÿȞѦȥѧ\x93ɫϪȑͲϝѯĳ\x8aΖϖҥӡАB˘üʏҝɋƌұ',
                        },
                    {
                            'key': '\xa0ÑҒӀɱĠŀÚÌŪҔÔёɨԨsԌÏƋɿͱңΜɒʑǕč`НȂ',
                            'value': 'ǬG\x9bȰǆƉȏЍүԕάĉӨͻҚʷԔʴʊyŽÆѩƌϥǦϘưkʪ',
                        },
                    {
                            'key': 'žџ',
                            'value': 'ӣ˭ȰY˒vпłμƁ(Μ\x99Ӑ\x8dέͰÏǲàÏƪʗȻÉnɅԎϑȯ',
                        },
                    {
                            'key': 'à˪',
                            'value': '\u0380ЗʓϔʦǾу˛p˘ģĥѳĤҢɭ˨ʯǷûʩȚѕԓŁ˰βǚȌǏ',
                        },
                    {
                            'key': 'Ɓ\x9c\x99\x99ξʤϦǐˇļǝвϿȒʧ҂ŮoˆΧԋȄÿ',
                            'value': 'ҏµ-Ē˼Ғ5ǰƉȩƐʿĜȚɿÝǝјϛĸɋ\x83ßȯƔſϲŰΫъ',
                        },
                    {
                            'key': 'ɵʂэ\x8aατшдӡϝÓȒ˒(ƄÃśԩѳΜʜϴѱӯ©Àҍƙ',
                            'value': 'Ѽϱǎ?О,µŀоҜ\x85aɬԎƴɖб¿ʗïˁǙȲҴěȨ\x80ČŌƤ',
                        },
                    {
                            'key': 'ӯԤкӤτǗҍƐԐSϜѮƩɸǺΩđ˖Ȣ҈ŧƩуΟӢAӨʪ\x98Ҵ',
                            'value': 'Ǣҽ[˞еΫ\xa0ˣϝɠӨ˨Ӳ\x89sǿsѻҐðʛĨȁΎΗʒŁ˴ɺɐ',
                        },
                ],
            },
            'comment': 'VньčƢѥîϑȕΛӥÄШϴͲĖӰ˥҃ԣƏÐʇӶǖːɎ¹°Ś',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'Ҿ',
            ],

            'event': {
                'target_id': 'ʵȚpϗ˪',
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
                'Ѕ0˪ƴ',
                '˒lgMɘU˨˖\x86Ǝɻҥ҇ʓ˖ːβ΄HѦǍУ˃ɀ˾',
                'Ȁҡvĉ_ԅčƱϒΤ',
                'ԢԁΌƊCьϦсʥÌȈϹã"ĉп±Y˘ДɵѯŨ˅ƌņπƾĥM',
                '\u03a2Ĳҧǐ',
                'ǽƿеƄӕϫ\x8a҉ϭϺɋˋŦμĆȉϖxäψĒϤ\x8dԢΏъкӯ΄ɓ',
            ],
            'bindings': [
                {
                    'keys': [
                            'Ͷ¶Àԅԇҙм',
                            'өϭƍȪȱʤçлαáÅʟӍМ\x83·§ϓÔͲɛңǥķ',
                            'ϐ¶ҢϘѐϖΘuļ\u038bÊ΅ȮȺα',
                            'ҳ\x97\u038dʿϜсɪǸяqƻŦȈȐŖå',
                            'ΊӑĻЗĨΖŅϕ\x89ʸѯǷ',
                            'ĎͺҔʥ',
                            'Ï˦ӈÌ¢ʸӳǦǾěϓӼѐ',
                            'ҽŤǄɷԣ´Ԡʜӳ˱ΔҡǺƜΎƩ<ӋνҴͲ˰ɛøɲƁ҉',
                            'ʺĠмʏϴϛѬŏӂбХ˒İɠƫɄѲԥӪHԔźЇ>ɘáѠ',
                            'ΰǨȈȲĈś¢ÕӶŕƱœ\u038dȐȎΤϊҰȒ˞ģ\u0378',
                        ],
                    'event': {
                            'target_id': 'ӆѺϭʤȘӪԁ҂ЇʅԟǟћŅĆ;ˋ\x8cıΪлмԟʎɗѲʏʩӒҭ',
                            'parameters': [
                                        {
                                                        'key': 'ȹ[ ˜ѝѹØŚÙЀǹɟùƉѽtƹϽǜɩĞ¢˭ӱǙҍĔpėҥ',
                                                        'value': 'ΚβéϡŇȺЕΛƶ=ĦȭϳиȁˏԃɶчÞӽȘɑϫѲʅζaƳŉ',
                                                    },
                                        {
                                                        'key': 'ǡÏǩcͱθȇҳЎƺ¬ƏʉƩ\x96ǦǧǂϠφҎфԕЕͽαƎɷŉ҆',
                                                        'value': 'ΚƧҨưҭӔʀƵǵ8ԉҗӜΥԬΓΣƗԤ˾Оʹкӿ\x91ǗʤǭӍö',
                                                    },
                                        {
                                                        'key': 'ĹȻϞưǑˤҞȴұоČ˳',
                                                        'value': 'pсȤƿ:ˉ@ĢІʱˍȘëҍԭ^іʿ`ƝɡʨʝMËӕĜĢӾϿ',
                                                    },
                                        {
                                                        'key': 'αľȉFƥԒƬėΰNтƝ\x95(юԪ\x9eΔҒǢĊ҂˂ʬο`αʞ҇Ė',
                                                        'value': 'ЫЪėɶǨɀõƓŸ˩ΫȥϮѻɔѓȃΣɴƵĜʔΖʓѫ°ԕͲϑɮ',
                                                    },
                                        {
                                                        'key': 'ĀϻѮҼϑŌ·ӲҜѺʧãΠɅġĤӺȰϛǄ˃ӓԍȫɜƿŀζ҄ʰ',
                                                        'value': 'ǂÞƑыSҍњǦʃƖԠȋŠ҃ԅϓ˜ȫHɨƗˢƘʗӸÛϮǽȻʈ',
                                                    },
                                        {
                                                        'key': "ΨПĢǭǛ\x87ɋ˛˳ďʆ'\x8eӮΒǾʝâ(ϮΉęͼóˬή\x9aʅҢŴ",
                                                        'value': 'Ȏ˅ЏϽɐ˹ͺϯϨτȓ}ЙŌȰ\x87ÎϱϸĝӫȖƥҘ3мZJ˻ȉ',
                                                    },
                                        {
                                                        'key': 'ӴӼԢѳΌӧǭӇȆȩÛӈГȩɉĢ˃ǏɝӆгřÅŖMǙÓΤЛĲ',
                                                        'value': 'úŇc\x82ƔңηϓčԙϞǜ¿˔ϙtƗȏɇĲǼÞɔ;äÑƞДЏІ',
                                                    },
                                        {
                                                        'key': 'H˻ѓ',
                                                        'value': 'ŠѿǦöмſɔƺ¬ĔǂʫǼũƲѴԋʢxǻʯÄŃр˅ĊԜˆӎè',
                                                    },
                                        {
                                                        'key': '˧ӗKԕ²эƃϱʯs\x8c˟$?ŋǶ>ǉӤȚ˫ôҚӏǆΪôĳѧп',
                                                        'value': 'ЏϴĹ\x87ö˛ŰAϓwϬͰ\x97¤ĈӿõÃȮśқƤƟѬʇ\x87ӦßѴ҅',
                                                    },
                                        {
                                                        'key': 'ë˾Πӕ˛ӵÌɽДѮŊКĚ˧˗Ԧ\u0383ǜѬÞ_ӺʍϼŦƷˬɐɣ\x89',
                                                        'value': 'ʶɌӖπҖùҀʿǓѴƒÈɘFϘǞīϝԡͼÕ˛ŲлĔªӒŻ\u0383ɓ',
                                                    },
                                    ],
                        },
                    'comment': 'ҫɄ.Ȏ°ƫϐҾ\u038bɄÂйӝɳӮĄоcŅƂ\x9bǈŇw÷ϗ¬ɄɟÜ',
                },
                {
                    'keys': [
                            'ȏȁ»зŀӛɺĒĐѕ',
                            '5ŢğȕÝ˳IǻԓĀ\u03a2ōčS',
                        ],
                    'event': {
                            'target_id': 'ǈ˟КϙїϞƘƛǼϊѥ\x80с¢˔һӲҜ)ɶƙϪŝ4óκǧѧϻͲ',
                            'parameters': [
                                        {
                                                        'key': '\x81)θĀɥЄĈͷƣм¶ǖ\x8bϒ˞ӷϐԟÍ\x81ɡɡ˚UԩşʹǨʍɓ',
                                                        'value': 'Ƒ˅Ĳӛҷ˪ѮС<ҳǳΞȻзĊӬØЛӲŰӦcȺʥώĦτǠȩɋ',
                                                    },
                                        {
                                                        'key': 'ϪҳǡƥλЁƓѷѮLҳ¦ʿѣĈȶĬ҆Μˑŝԕŀȥ¤ӑǑӿөŔ',
                                                        'value': 'ѱϖϲԃ\x8cyǠϥҦ҂ΰ>ǦѻɺʩrȭǢΩɲӺІȳ\x95ƈǁʖԅˬ',
                                                    },
                                        {
                                                        'key': 'Ē\u03a2\u03a2кΕϨ/ϓʢǩμδĥ˭',
                                                        'value': 'Ԝ÷ʇņpξŀ\\ϰӴϏҤЊќŢ8ӷԬёˌ˻\x8eʅԀӝбÑþ]a',
                                                    },
                                        {
                                                        'key': 'ҊʤƭěǻΔ˱',
                                                        'value': 'ІΔ˄ʹӨɫЬӬʕ˫ΨϭӘϟӜʕǨȓǂӪÃɬĖ\xad%ʯВҋ²ϟ',
                                                    },
                                        {
                                                        'key': '\\ϧ°уĂ ɓӄЙŪËɕȟƮҽƒ/ԣҧǬҀ҃дȿűKӞăǂǄ',
                                                        'value': 'İғˈ\x86ÔИťĮƋҟȐ\x98ӆ\x97ԤөŝҫѝǲʒӸʩÏʶŲʆɑƶȢ',
                                                    },
                                        {
                                                        'key': 'ĶŦɥʨš҈ψÂ/˃ε˙дǑPȉИcϕŔɄҸʽɗȿȼƺĚԋk',
                                                        'value': ')ƟȣɲФԞǇɋVɩͽѠźҿƹ\x7fƍ"ӱWΜɠ!ҸñƀĪ_ɔʰ',
                                                    },
                                        {
                                                        'key': 'ǡʹўƾ\u0380΄Ό\x89ϷʑɷrӱŶҵиƲѫ4Ӝƣ~ňƤ\x9bƊi҃ȰЃ',
                                                        'value': 'ɒɈȾŔ\x9b"˲FÌɽŀ\x92ԍˆƟ˔P͵ȉ˹çʻщŀƐƢǲÞß˪',
                                                    },
                                        {
                                                        'key': 'ж·¦нѥˣΔϺʒ͵Ь˾҃үҼύβѳѰOЎ{Țƒј˾ƩŮ|ϔ',
                                                        'value': 'А˕®ŐΝɓĂŀлȔЊʐ\x92ȋ¢ʤКʻАÍu\x7fșѪ\x9dˤМΗɷ\x84',
                                                    },
                                        {
                                                        'key': 'ϡіĕДԝθ\x93ϟȂєǙЋǽ\x8eģѼʇǛһåɡŋƱΐʇ˪ʯĠɝ˥',
                                                        'value': 'ԏӡʻήÜˍ\x8fǑY˴ҎȎűʇԛ¹ǻHKπ»˦ɤԞcԬĸÈĲó',
                                                    },
                                        {
                                                        'key': 'KӀϕҡӴ]ВĢϚԑҕƍԣτźzÎ˱ҴǍǥώѱҁȘĐ/Ͷʍ§',
                                                        'value': 'ƗҰȑțˏƢĴ˾ƟϹŭ®W6¨˲ȏӊHBћĊ\u0383ϩѶƀ˝ɇӖĔ',
                                                    },
                                    ],
                        },
                    'comment': 'ҮƊϲªŌǕɂÎûɸ1Ĝđ˜щĜȼɫ\x90д˵ÐZԘtǉĦʮԇě',
                },
                {
                    'keys': [
                            'u·ǘtЪѲ:Ǖ˪àϟĶԌ',
                            'ӶʕƁ',
                            'ʰǂǸPԈLóŤǜѶǴȯњɒɰdЦπÁгǙӣĂɻ˄',
                            'ƵΛЃƦƻˇвѼ˦ҿ\x99ϰLσѵӺ˄ʠҰϿ˧K',
                            'νŇԝÖǲ',
                            '¦ʓԩϹ',
                            'ѽĕӯ',
                            'ķď ¦˵ΛɀҙίʸӬdˤɿˈxрÀʃˎҧҖʹ',
                            'ɻ0҆˟ƭÌЁ˄ɧŗϪŽźʎůӘ*˗ϑǳѼŘƤǫć',
                            'ӢϸђɎɄΒʱƹ?иΏʼϵμƊ\u0382ΘӸӡЖӮВƊ\x9bŹĤҠэӻ\x8c',
                        ],
                    'event': {
                            'target_id': 'Ѯå@(ͷƜʐʃΎЙΟǐżȉѬѪҟѿԆʓщЪѲυӄɧyѽʎϿ',
                            'parameters': [
                                        {
                                                        'key': 'ëʞĹ§íΌɩӮΞтĨé=ζwſȚҍţɩԓĮ˱ϙȪ˝Тӱ·ȣ',
                                                        'value': 'ǲȷԍo+˕ȩɂ\x99ŜÑȊâˌvѵʍĖчΧŴȘ\u0380ФăϼʁӭйĢ',
                                                    },
                                        {
                                                        'key': 'όʿɕШ˧ϦҿÙŴɺӅǸŵЋмˇ=ȳțÂϛйʱё6ɡĚƐʗЩ',
                                                        'value': 'ʏʾҚɴΟˬȈϜΆΰŃϑчTǗÃΓԪҘG\x7fǢʧǿԧ҂tƊŢű',
                                                    },
                                        {
                                                        'key': 'Ȅ«˩zŊΆϮɆѥ˸ɲЂδȡԫӵӚӮì',
                                                        'value': 'ˆԃѸ@ʡϹʃԠȘԠƄ0ʯo³Ԯ҅Ž\x87ǫʚ˗ўсɽʕгŐșƣ',
                                                    },
                                        {
                                                        'key': 'ίRЩtСѸ',
                                                        'value': 'O¿ōѿǼɱӋТŮ˾ҏчɃЪÒҙĞѾ§҈·\x88^E\x80өzƛ˖ͼ',
                                                    },
                                        {
                                                        'key': 'ɎѬʤƶϔщNӜʑś\x94ЯфšʫȱSƏӵǊƁǀ\x8cƺmѷӬƕǈě',
                                                        'value': 'ŵɴƙЪʗƱĬǣЌҴ·ѯĩ˦ҎμĿϜаϲѬˠśƧǼıiΌˠĪ',
                                                    },
                                        {
                                                        'key': 'Ňӳϟ˪Ӊɲ˞ΡЁʖrǝǞж\x97ķǝіοʞ',
                                                        'value': 'ʼºŊkԌȮҸНŌμҪӮǁҴΞM\x86έŁƘОYҿŌυЍkӍДҼ',
                                                    },
                                        {
                                                        'key': '®Ȅ¹ʺαŴŧCŘăϔƔǓӾΆĸЮ˔ӃɥʖǥЊΠĵzԌԘ¢И',
                                                        'value': 'Ǝć÷ϠƼíĊ΅ŌΧ\x94ˇ\x99ȉʍ˹ǜZʓɉ˩c3ʒӌʴƌ]ƙэ',
                                                    },
                                        {
                                                        'key': '\u0380Ƴ',
                                                        'value': '³ɒѹY˶Ɩè\x89ȢƲҖȄӅ*˰ïƾΊϾςЧγ4ǖӿɇEüqӁ',
                                                    },
                                        {
                                                        'key': '¿ϺļǢJǡĭĝʪơ˫ΊƏћаŗѹԄæŌԣɱĉЋҮƆ\x8cƹΜǓ',
                                                        'value': '¸Ӏ¸ͽɌºĕȭϖŅҚȭ\x8dǦɆǧŷʩɱΘƁӃřϧý`ɦӱķӂ',
                                                    },
                                        {
                                                        'key': 'Όɠ»ԕˠӺҍǖ5ōùʒđю˶\x92Ӯ\xadѪˢЗ\x93Κ\u038dϸζʅʵǮ\x81',
                                                        'value': 'ț\x88ҢȹƮËƧŠ0ÜIϦϭбŤӄ˛ѲȖɉˡɎɺԓу\u0378\x93ļųԡ',
                                                    },
                                    ],
                        },
                    'comment': 'ɌУ҇Ć®ɷƇÆȹ§ϊĄδɿoӺƻ҉LҐвĤǔΗˏͱѕѼǪȟ',
                },
                {
                    'keys': [
                            '\x97ІρБä˕ӃĞ¯Ïç˛ЬȇŖ\x85ƐϊԨƁťŅþ˛ûƿӂ',
                            'čųƖͼЙ\u0382',
                            'ɱҜѧҤhĳUɪ',
                            'ȅǏɍ˕\x9fÉπ\x84',
                            'ɵ',
                            'ВЦɕԂƩλΚԨӁîʣȕи\x8aʅǬҙЗƣyɳ{NjЮ /½Ϥ',
                            'ĠċɓȐ˖ʼ9\x93ˉʨ',
                            'Ѥʮʦ\xadȫΉīϤ3ªҗɆԓ',
                            'ˍ^',
                            'ϘuЌԒλԨɱѝϔΎӦљЖ',
                        ],
                    'event': {
                            'target_id': 'ԝԖ\u0381ʋ\x94ӉȿAԮYŦҌϾҁőƬțđN\x94Ӕ%wӧɾ\u0378ȳùȞǽ',
                            'parameters': [
                                        {
                                                        'key': 'ҲΦҒσϩ˰Ăҗʡ\x9eѓԄ¸ɗ˵ЅĒҕѧϿŚțʖ˕6b\x83\x90άʆ',
                                                        'value': '»Ӟʨqʻ]ԣȵΔ˖ɯΩʑįʽеĬ\x99Ā\x86ʕːïҵșɲʋˎˈđ',
                                                    },
                                        {
                                                        'key': 'þxӳiЎ=ӞĽȵīäϢǰȹˑfƭɔϺҀθуƤ2żӪɻ]Ԧ˻',
                                                        'value': 'ҌҍіΧƁ˯ÊԃčƌƐɑʷүȢğяΈǧƨƘ\x8d`ΘЃ[Χ˧µ\x83',
                                                    },
                                        {
                                                        'key': 'ҩûͻμˁŐǖчϊǀĸɴϗǃɀțƴĆӘ΄ѹȿĭēϱ¼ǭӋ\x86ά',
                                                        'value': 'ʇºĘҟӸ\x85ÌųҳүЦӜˍӹтɃԜƙŰâУɕāǾƯ˗ƧӰ˱ó',
                                                    },
                                        {
                                                        'key': 'ƌЕƱȐͳϢÑ!ĦĎѻʤгҨE\x7fǅԡʗůȷĴΈʤ»҈ʶȊƏƠ',
                                                        'value': "Éϛ}˵КͻˤЕѝȂушК£ĳ)ҲĭȚцȤӥɅâǻЖљӽ'ԣ",
                                                    },
                                        {
                                                        'key': 'ňˀƬčҔӨɵz˹ҟéϟɎÞДÕԮѼɀōҒ˴êâϜʱöơŇӌ',
                                                        'value': 'ϲӌӳğ\u0379ͳПгɠʂШ˭ɯѓUčΜɑԩʍ(ϡǦҍtЮÖξɤð',
                                                    },
                                        {
                                                        'key': 'Ǥƭ\x94ӨȮŋÎĊ\x82\x92ĲЃˏѡɠл\u03a2ЇʹĽΆҽǲǗЎϺƧЫ',
                                                        'value': 'ˋnbΆǘKăϺʐÖ˙ɂǳΞҍǑåȈВҢɜˀӫʘПŬĎÉŻȉ',
                                                    },
                                        {
                                                        'key': '$Ǘɔ˰ԞVκɎΙԇɹѿҷȇȐβ˲Ådрü˜ŕĲˁȧ\x99țБ¹',
                                                        'value': 'ήɿοΦYȗҜ^˂ӊȻǁkŭʄȁǙ³ԔΜҧөѡ˓ԣΜūϹ´Ġ',
                                                    },
                                        {
                                                        'key': '˼ãƓϩţӗȂԬоȚсĀʙǨӕλ"ˬƅӒӬÙʁ×PІ˄˹ȰȌ',
                                                        'value': 'тπǳҭƌƨӡ˦ŸҍΫ˩ϘĆԡʡˎӛϓѢц@Ŭ¨Ƶѥɜ˄Ѐɔ',
                                                    },
                                        {
                                                        'key': 'ʌ҇ɨƴҟ˹ŧɿɮԬŴȩʹԮδɨǝϲФÍ\xa0ƐҽŹїҩŢƕʸ˟',
                                                        'value': '\u03a2Ǻ\x90ǋɰϥ¸\u0379èÛԗǫѾίϔΚ1·є!ʅΊСўѨÝ\x8bǋ˾З',
                                                    },
                                        {
                                                        'key': 'ʄпĄƟԁӁ˱Ηě7Ȝ˄Β˧҈ɐƗĜȓÀ˴Ɉņ\x8fʕ\x82ǘʘңȣ',
                                                        'value': 'ԍǚƧǷˈõɤӀɜϕʼżϕЍЭѷίȺȅÃϿ4˃óȾʚћνɩҀ',
                                                    },
                                    ],
                        },
                    'comment': 'șŤŻԀԣξΥϋʘϙȞџˋԂϰΜŃAUǤɜʟ˴еԔЛŏҒϝ=',
                },
                {
                    'keys': [
                            'ԞЁM`ўUã¯uĽСѤԘԢѡӃýҔӃö?˝ĵƛ˨',
                            'ȽԖ°Ƕ˧ҽҜĢԃʫӹĻʗ!ĥňρǉϞǅԛȲРƘɖ!ƅ',
                            'ŭͳκğĦԤ',
                            'Ǭñ˺ԕ~ѩ¨ȡɐ',
                            'ξҧ˺İНƚ\xadĭԤǊ\x9cЊкϜ\x87nHӤRѦȑӜGȮɋļ\x9bе˓і',
                            '°ŭΨœĪȈËɫϳĵťϡҝµˉфӼAҦAQȱɀԌɏθ',
                            'ȌAɌӽ\x96Ǟdӟġ:a³ГΊǥƜFшЀƷfȼӆӭ',
                            'ǉŠļŋÉǽΘˇȫс\x8cʹÔўξԇɟ',
                            'ƇԜ2ӪИЩЗĉ¦ãͳɥϊŸƓȲԀȉԮϩō,юNƖǬǇϺ',
                            'ϏәӺΨƤɹ҃ҏшKɋſΒӱǩĿȱƞɮ',
                        ],
                    'event': {
                            'target_id': 'ʁКȕϦÈɯӰR҉Ȕ»Ľ\x91Ε˝ńέϭǋљǓ\x93ӟ_ăѠàϴ˥Ġ',
                            'parameters': [
                                        {
                                                        'key': '´ҐѼƚƐυěŬЧ¶ˌƯʮɰâǈӕЌӵӨә҃íӝѻЧиˆӦǤ',
                                                        'value': 'ȽșŒįθų&΅\u0382_ØΉѯԢ[ʼĩÔАHȎŖϸ°ф¤ʻˢÔΛ',
                                                    },
                                        {
                                                        'key': 'σϋ\x82ŷǫ/čYʒǚ\x8bǧΦWˉɊɻnƇǩʱӬ"Ь',
                                                        'value': '\x9cãʡҤʝӦ?ǹçÝʎΦʧư˜ƨϱӭѱКԉʠçīͿěǲǖφĸ',
                                                    },
                                        {
                                                        'key': 'βȌȍѼԥʟ$ǂӌRҫ.ǚԑȢ\x90зųŝřºсСȵԉ\x96еҶΕ\x9d',
                                                        'value': 'ΣċȦȌƌҗπΠrиҧԌҧ˻ȇ±˦ԈļʿȈѦӣƯĔǾΨǗѼρ',
                                                    },
                                        {
                                                        'key': 'ƀȂƭΉÕСĝǿцЯȓȹâԆ\x89ƺϑƥʮҊѶǓǒӣъǠЀĕǗɸ',
                                                        'value': 'ɇ˰ĠɚźѺɵɿʮĵгӱ6ΦӍÆύѶЋģ¸ŊGɽSΤ˺ΰϓҏ',
                                                    },
                                        {
                                                        'key': 'ʺʻč˖ґöӪÎϹȫΟ',
                                                        'value': 'Ϟ҅ȊǺǆŖĈȩȵЁѫԙÊǂ;ζҀǟķƠϧʼ"£ӂóɮƠд²',
                                                    },
                                        {
                                                        'key': 'ӈƗaχ˒ʪϪԩǇʢĎ!ˮZ˶ԏ{)ѡŝǭӸé˪ѥщ8˾Њǋ',
                                                        'value': 'ʒҶӻsӟχͳͱɶƑm҆ҧóȐŪɯͺӠѪʖӠĨȃϵҢӉ\x9fȈ0',
                                                    },
                                        {
                                                        'key': 'ßʍƮ*ȭϸ\x8aЋǟʨµɴżĔϦƳϓƎġʟƄЮѵӆϚɄFĿƄӹ',
                                                        'value': 'ċ˂ƓɲțѫˀͽσŁˋƷ˰ԗǊǤˠʐȏϊЃȖƻZӅБЏϊѝв',
                                                    },
                                        {
                                                        'key': 'ҪǱȹǻ\x81ŀѫϡϮϾρˬBːβþçњǮʴЮùġȋƉɄуΏ',
                                                        'value': 'ZӍ˟dȺКʸҪҗΘϰȺЋгҡGɹӊ˧ŧȢȑűGɌĹßþĒǟ',
                                                    },
                                        {
                                                        'key': 'ÙǰǤƈÀ˭ҚԔ˂з1vʘͲöӤĹԔ/Ӫţҍʄǧ˯ӣԟӲɫƀ',
                                                        'value': 'ϓҚȼȠɇΤʇ\x85DӝĒΤġøӷƪӪ%\xadԔîӶԖʀϟяȢвũ\x88',
                                                    },
                                        {
                                                        'key': 'ӏȿÑéЄҍř2\x98Ȯɔɐ',
                                                        'value': 'ĵʰ\u0378»Ŭʋ\x91ЉǂӊΧŲΑǚ¶þϟɱʐԗʾϏеӏϞ˓ŉǅцӺ',
                                                    },
                                    ],
                        },
                    'comment': 'ɣм\x8cǲЙǏìÆҩΞɅǪȺӓȄΪμЩĸİ£κɂAψvҥӵɑˮ',
                },
                {
                    'keys': [
                            'җѐУƚȲЄǉЯüѴȿȪԞÈʲԙ°əƏƦùПʄƟ\x85϶ɐѝκ',
                            'ƣɗƋӕ˶˸о\x81|ŏS˩ń\x94\x81ǽЉ',
                            'ē£ϓʺвĄ{ǿŕƬö\u0380ňͷǊMϘ¹ʰԈќ˓њΟϨ҆G¼ʄΡ',
                            'ʞĢʼ&ӷǺȬɐċǇԊ3ȐǪȟ»ӚЖĖȼэęm΅рȨɨț',
                            'ÀɣƆΜŃÒ',
                            'ɉǿϞļЪϥċ\x9f',
                            'ʌǙΐ',
                            'xв˼Ңȱ',
                            'рԊ',
                            '6ѩɎȲΤӽӾè~TõщѲƒ\x83ɮ]ŔѼǱѷÚaΝ',
                        ],
                    'event': {
                            'target_id': 'ϯǸЎÚŬʆÏϓȫĔŻȞĉΉ҂αчŤɰƧʀƠíԫ\u038dɇϱюʲY',
                            'parameters': [
                                        {
                                                        'key': 'ҞŪͱė˾¥ĈĈȀąɪʮƦbЩăЅԅ$қԍӉ˱ԫ\x9cΌʹμ˕Ł',
                                                        'value': 'ɦűƭӁԬƠʵˁ\x81ӞǥzӤËɫԩмDʏʞȱêѨG4Ѱɹ˺ɭ\x7f',
                                                    },
                                        {
                                                        'key': 'Ƅē<\x86ΟњȱƾƲ¨ϚŴɒCjˇiПЋÉˑŴn˛\x93ĮԮӡ҅˳',
                                                        'value': 'ҚЗЮǅ͵~Þɸ¤ʿɖɹtԝǌ˵BĲӹӑĿʆѻшƊʣˣʻ\u0383ԃ',
                                                    },
                                        {
                                                        'key': 'įЭʈҝ©ȄѱțǾͻƃʁöĈǾҌú9ʾў_äԚɇś',
                                                        'value': 'ˊĞç\x93бȚňӈȻ\x9cǜǊűëӓˣˮkƔŭԒɮҕȀһĽƮ*Ɲć',
                                                    },
                                        {
                                                        'key': '\xa0жЌϢˆƁǮƧƮHĲʔΣ²˹Υ˞ǕěƵɞ˾ƛІ)ɽЄǻŗҤ',
                                                        'value': '˯ΛԈňɭЈUųķΆ(ʾƉÒ˚ҁƉùτƉʴΞʉȏԝ¿ƍѮ]ŀ',
                                                    },
                                        {
                                                        'key': 'ɭȖŔ\x99˜˙Âŋԡ>ΪБū7ѡҥԧķéѣg\x97ƷВ҃ŉƮʌĞΒ',
                                                        'value': '҂ʏňΘɢыÅŜϣĭѮҗVǀΟƻ×őxĺԅL\x7fƘǢ;\x89ŒΜ¢',
                                                    },
                                        {
                                                        'key': 'ҍuҎӿӒ¶ʋʓ˅ӊЧўȐž҆\u0383ʕԙвɻˈÅҿ\x90»Űż',
                                                        'value': 'ɀз˂Ͷ¯ԑ\x9dƩԅϻϭԩӲĴѭ˗ƙ¯ԆPԈˮÊŁɌǍЏΗšщ',
                                                    },
                                        {
                                                        'key': 'ŤɐΔ ԒЛɹøѦòԭåӫΓɜθ˸Y·˨ΧāȱθɛʑЛҫͰԒ',
                                                        'value': 'ԝ˟ǜΦββ»wΝɘѺʶҘыǱЦƂ\x8bˊ˧ȖȪГŉÅĻÿȦƁҒ',
                                                    },
                                        {
                                                        'key': 'ΠԬɰĚОρÄ˧ѼΫ\u0380ԑσMДʊȺ˯ʸ8Ɋͼ^ΥΤŲҠƜÛӵ',
                                                        'value': 'ʒʙ×Ԗҙԗ¡єԈ˥Ҽ`\u038bºѵԟЦάнɧʵʠŨGФXʜѩΠ\x9f',
                                                    },
                                        {
                                                        'key': 'ʥĮӒłлÚ®v>ÍҾkmӳíɣӘВć\x96ӃҏЎьͺ(ҁóҽ\x86',
                                                        'value': 'ħ}łуβĤάȉǥћζŗѣԀōԂмϿÕϓЇƧɾɬϥϷзçðѻ',
                                                    },
                                        {
                                                        'key': 'ϦÆƳɉƵЗǠV\x9a&Ҍԝһ˔ˬсӋы^ɗЫʕƘſƍԬřиɊ=',
                                                        'value': 'ϽƛβǍʄјɆαëЁwí>ƳҗǼƾǺэѡ\x97ŲˏǕňО˅°ΞԜ',
                                                    },
                                    ],
                        },
                    'comment': 'ԡĞŢǔӔ҈ԕҀЀŞʱˮþɀ"ϝȱȼˁƒѳƏÉҗæƽǁτήŕ',
                },
                {
                    'keys': [
                            'ŭϼԧПίрƫҤăѷԐϝя¼ԘѲЉðòƆүӥϫĪιǾǅɛЀ',
                            'ʁ',
                            'ϤχÁɩλʥ÷ΉϼŃƳřоIJʚ',
                            'ΎԬʂƶҷɍ΅ӘѨӱӗ7ĬѣнѨ˛',
                            'ŃŶȻΝӓͺTʂ',
                            'Ԕ',
                            'ҭƼÛҦǡцLǼӖӼЍĦŭҮӕζǔɏŵ',
                            'ͻɢˮľǵɮѰ҇ɥӦĲϮ',
                            'ƚqМSΌǽȩ˙ΤϏЗŵȘ¯',
                            '˽ҏȾɗĖȽǵ\x95˦Ұέœ\x86ǟûҔǘ$ѲǔӜϫĢ˟˘',
                        ],
                    'event': {
                            'target_id': '$ΈˮɎń˰ëʜеƯoϊӒƗЯƠ®\x91ƸĊǿӠȐǀàȈԣԎӦ\x80',
                            'parameters': [
                                        {
                                                        'key': 'ӨǇҺƎΔ',
                                                        'value': 'ʁ\x94ƷγҢ͵іΘОʗĔԠɖ±ѓҸÖϽΙΩǖʦбźǀĝªÎѰ¯',
                                                    },
                                        {
                                                        'key': 'AǇϜˤԣƕМʶӜӚˠʷȟʗİ±ɍϏ³īԇ®í8˔ζĢǳłФ',
                                                        'value': '\x94łӆџϫʎҰӨǗùǳĭҳҾϻԃȆҞĵǏɩҴŊŞнˊӺǧǔʻ',
                                                    },
                                        {
                                                        'key': 'ƚ|ņѰΡԈɚѿÇ',
                                                        'value': 'ϐԨéИɓТCʃƙȿěWҢΙϊƬϿwΑоԬɮѦĚ?ĥċĭƫӄ',
                                                    },
                                        {
                                                        'key': 'ɞȇʆϳȇŎЕλќʻȯʏǘԉϬҦӐƢèҏԟõіųũЂ\u0381bϋʓ',
                                                        'value': 'ƞďԢ˃Ĳı°ҡДŷŔʺȝƏҿ\x9eϜюĕΘǙkƊǝƦΜϿƆçϓ',
                                                    },
                                        {
                                                        'key': 'ƃ85ϓҝŁθѦԮϼӣЮ®Ӊʾǩºʟϵ˚ÀȪӕ½ɍȔΝЇˮǯ',
                                                        'value': 'ɧùÇǬǑȐ\x99ɾϷǴԑѺӳȈ˟¨ǟԬňĠĵóԍɣƝɷԍŷõǌ',
                                                    },
                                        {
                                                        'key': '}ԟ˷ƒåϨÉĀЌ]ЮÞŤțț\x8dǭҀӞŤľʋĖћлĶҤҒŴţ',
                                                        'value': 'ϭ˴ʉƝėԎʛ\x94˗ʦä҄Ś\x9dˉԧι',
                                                    },
                                        {
                                                        'key': 'ėοˉɸҶ˰ϬƤҲʜŷМδ˭ҶƏ=ԮǻЉϤ',
                                                        'value': '˫ΰ',
                                                    },
                                        {
                                                        'key': 'ǟЋ˰\x84ȕfȔϛȯÜ×ЍҘϨȴɑԫ˨ĳČņƍцРɨÆԗь˷ɕ',
                                                        'value': 'φӸǁўАƱˏǕŁŭũ\u0382ҦȎԁǪŷƬɌŰΦǊҡɧӳǒЇìķԚ',
                                                    },
                                        {
                                                        'key': '§ИҒś¬ȼĆìHѴә:ĔMͿӥƂь½ƲȉæӰŋϋϽ\x84Ƿèţ',
                                                        'value': 'ɧĄʱĂûÒҍǫНрԄԑƜɬΧāʒȹѵĬӑȀҷ¼ʄҦƗ˖ɓȱ',
                                                    },
                                        {
                                                        'key': 'ΜĦҋʯōΫŴ\x7fȦԡãžÛ˥\\ǖοʅЂг,КhǺӠЌ!ˎʅӨ',
                                                        'value': '\x87ҏȋĮЇ\u0383ҁЬÂǱϩӹτϹȜǼÈԙȚȡщSǣύʠͻɊģθЯ',
                                                    },
                                    ],
                        },
                    'comment': 'ӢɩÒˮЈӂµȥΑϠ)ѲŀЧεƷˡÈǃƛфŬӪңÂ\x91ƖθұÊ',
                },
                {
                    'keys': [
                            'ˉӶÎщɱͺ',
                            'ʸԭľƪˡαŉƛ',
                            'σ˸ҸƷ',
                            'ё©ιԇ',
                            'τǥ˷Ҍȹͼtʐӝʺґs˧үŢɈ@ǣÍ=ƥŨқʕɉҊ',
                            'ǥgǹє',
                            'ʕԢԡțЮК',
                            'ѥɀЀɃϗ[ǡ:ʩǵΛњǷӊ\x84ǁƀĢİΔԇƌźʕͻХ',
                            'ŰӔƼ:ԘǌҾA',
                            'ӮаĎǻβ΄rɨɮɻȥѴǉϼҜȬΔѺiɎЙϐĒ·ΰˣȷ˷',
                        ],
                    'event': {
                            'target_id': ';ŖĈÕ¾ӬЩѦƸ\x9bԑԧӘUƌ\x85τȹϼʐª¨\x90ƧЇǏӐˏņǩ',
                            'parameters': [
                                        {
                                                        'key': 'ǞԄұчȜǧâѷĔԇӽϼʀҵƌδŅïł½ŰŬϵʙѽԮɖþϚ\x88',
                                                        'value': '¨ˇӨƼ\x9cРǼƱыDĻùʐŰȞȽпԬЅǀϷ\x89ΎΦùƕ®ǐΛƇ',
                                                    },
                                        {
                                                        'key': '$ѳ¼ȬШșѯиφǲŷǱɭƸϡƦɿȜɪüƻǬęІǥ',
                                                        'value': '7ӇţƺƲˍyĽ\x9cEӀͰ/ƦѠҪԪʖӍƏwíϥʸɈ˅ƺӼЪӯ',
                                                    },
                                        {
                                                        'key': 'еʹг˻@ŋˤġƌǷđƵҒҺŮƗЀǭǯάȕҤəэ\x99Ϳɀϩ9ω',
                                                        'value': 'ӢƯԏʺԥƇǣǙ0ѣʽĝЇǙɧƣХɻѐԜ«ʕōȒӵˌΨ Ȓ½',
                                                    },
                                        {
                                                        'key': 'ɶǉΔӎЧˉΊɳjƧ˄ΕXҬєŔӑаȀ҇ԌƎƿĢόɖϺ˹˕ɴ',
                                                        'value': 'ĒηЅƭɦɪԍ˦ə5ġϬǯ]ӊ§ʮZ˳ǸѭҤϤӤӂ˴ŇӝƼЪ',
                                                    },
                                        {
                                                        'key': 'ůӪяĒͲǕʃēΫȥƝºŎGʓԒǭымʆ˖ȵЉԟAԔǄ\x89ǯȍ',
                                                        'value': '\x84чĴӾǂɡӭŗȄӰɴϚʨŭϟ˽µáѣчǑͶѬȠҐȹӐґФƠ',
                                                    },
                                        {
                                                        'key': 'ԇ҅ûǨțȱĂǿ˲Ӟ/DѴȜƃɳǢȚȎϼB§ζͷ@ѮìZҤТ',
                                                        'value': 'ҥ˝ϴɃȀśÁ\xa0ƆņĊǅэǈĿѫå:bƴĘ|ƅΐĂÌrӳΖʪ',
                                                    },
                                        {
                                                        'key': 'ӈԎωhǽƁ±ʕУ˪Ӡϥɼſ2ȭėϣ*ѹ+ʠ˷˂B<{Ͽ|¬',
                                                        'value': 'ͱǣӮÌѓÏњҨťǇӲΊʋΐ¿ƈǍȴĝøĸГžȳÌƙĔЁīɜ',
                                                    },
                                        {
                                                        'key': 'ȂҦĎĂηǼ\x95ҢƖȶøүÎϏƚƹ*ǥˌΓϻђ\x97СđҤƌϾмÞ',
                                                        'value': 'ˀſӾ±Σ˵ǼiҺlȦêȹɦӨɰҼɋӛȩȔˮÇʜÿԤƨ˘ʽӣ',
                                                    },
                                        {
                                                        'key': 'ѻÂÉ_ʇȿϗ',
                                                        'value': 'Ǝȋ˦ҸǦfϢĄͰA˂ʲ\x9bǼɻſˊȤʑɵȐӏÌÌŸфŷǗӼÕ',
                                                    },
                                        {
                                                        'key': 'TѸâĎŌ\x81ϛþˏ<ђĖ\u0382ͼκǵѴţÇԅЏ ɡǈǷϪ§ǟΑ½',
                                                        'value': 'ɲԘ¹ßȩ˳ѝЁϝȖ˷ԩ\x7fӝķϒ\xadяôԮ\x98ӂìѿМĢʻ˨Ɂ҄',
                                                    },
                                    ],
                        },
                    'comment': 'БɌԁΗԩɄрҲÿҕԨѪεƸЖӃʘʱ˶Ӓѽʌ҂~ŨѮԀȏăļ',
                },
                {
                    'keys': [
                            'ʛǹԟϩы˞ʆȸĹԥѕǅԪ',
                        ],
                    'event': {
                            'target_id': '҅ʨɬâŮ\u0380ҥПǫ\u038dĩʧϏîӌѳ˸ǟµԄЋ˧ɄԛęƝʒä3ђ',
                            'parameters': [
                                        {
                                                        'key': 'ˁҝěҨŝėźǝ˺ӂ÷ˇɉÏʵǼҗԩΉǲ±Ȣ˕ʬN˗Ǣ«ʔƸ',
                                                        'value': 'ξɱċǢȿɂ\u0382ҹ˃²ÕԩȈɮ˪їӧÀįύҦƿЁѦƮĸŪфΓ˭',
                                                    },
                                        {
                                                        'key': 'ΧϧӍįӗҬϰǛƞvŖŉϐ@ΤǍǓbȰÖϙƎԨ϶цdҭѠǟӅ',
                                                        'value': 'ʯɻƣɐ<ȫȨɱʿωгè7ԡρǪӣˡӖԚI΄UԉӌХȩѴўӻ',
                                                    },
                                        {
                                                        'key': 'Ӟдѱҟ\u038dëϑ˴ˡÀ[ъø¦oǁҬԡ˖ҘƄˠŴˮ¸ǑǂŪӾˏ',
                                                        'value': 'ĹUɢǫԃĈlΗͿeҜ}ſɭԡĖͺŉҕԤΠƎΦqǱƛƨ˵ȴù',
                                                    },
                                        {
                                                        'key': 'Ҡ}˓Ҭѿċ҆ϼǂԔˌͳҴȺѢȉɧ\x84(ґƒɻ˯˖ƫ\x99)nӀǁ',
                                                        'value': 'ѯХԢԮӯ˜Ѡ²ƈʙȷȜȓҏϲ^тҧ\x90ͽ_ˡȺ˺ǍŶКā\x9fR',
                                                    },
                                        {
                                                        'key': 'ɹҳӹҹřΟЎʵҒҎęÔӱǺɎěɸĆʀ\x8bɔ˞άĕӇƜɻƆφ»',
                                                        'value': 'ÁίÂ˘Ԧ9үśԘǢƓежѿΑӪΤȡɉΗȴçͼˣ)ӢѹӻǾл',
                                                    },
                                        {
                                                        'key': 'ĄÐҫӉê˱чŎȱɅ˃ɸеȕњºҨқNňƆ¢ѱʮʻΨˎɑϻƔ',
                                                        'value': 'ŷϧ˚ɱԗ˓˞ȋϽӰAƧb$ǸŧηϬπƎśȶ´bЧ˷ӰǨȝӹ',
                                                    },
                                        {
                                                        'key': 'ēοѡȈŅѯЊǄѡƪƬŉʫɥϏШȍӖĘ[Ư#˾˃кœʼ˜ȉ\u0382',
                                                        'value': 'ΥƛɀɣȂѓЖ˞ȊҌИΙƥϩѧīϷé÷ʹƘŁȜĐűˤЇQǴκ',
                                                    },
                                        {
                                                        'key': 'sЫԥʿͺ¨ʌҢОǮɡѽԀƻƯέҹųԧԫԔϾԣĐɄԮĒʎżӏ',
                                                        'value': 'ĄĎбϦëɔǴʈͶǏ˳ϷŊԔϡЊҀȘǘҙ¤ÇǛ7ǇÝŝǃʧƇ',
                                                    },
                                        {
                                                        'key': 'Əňɴɸ',
                                                        'value': 'ƠǵƕĠÍЎзȴɳАĽѕҿŞ˛ʱ˯&ʠǑƺѸɻҾΓ˥ÄȊɁӦ',
                                                    },
                                        {
                                                        'key': 'ˬ\u0383NǌŲsӘңʾǟƈ҄ɪħȠκˈĒүŠ˂РʶӭϚ˖ӝÝҘэ',
                                                        'value': 'ƨÐғӇĒ\x8f\x85șȬΕԛíĦΉҋʔùљ\x84ПĦĂѣȍÖҀӹӫɤѸ',
                                                    },
                                    ],
                        },
                    'comment': 'ŮˊǁˏԁҭӵЕΥWˤƃęοƁƣĭʏӏǶȨ˼ɞ®ԃҏПφȔƲ',
                },
                {
                    'keys': [
                            'ȬљΡV\x95â9Ă·ѯǵ¹ʚҢΞƘRʊþ',
                            'HƷϋʮóϨǥ҅ЯɌʝȽľ¨ϭˉ',
                            'ÿϊЈɜʙÚԛćӝĹƾԓÅПЊşn',
                            'Ǐ˩ͳɍ×UƨJĞƽ©âΪɋИɊȎ¿ϱҘφʦ˰ҺɪǤɥʵ',
                            'ɼӱϱͲȿŅVČҋʂҷϹʤӁ΅ѺËқ҇Ȼȗ҇ɞʹĤiǄÐ',
                            "ͿԨΙӒŅ'ɐȈόĮԊ\x9c",
                            '¦˛}ҀҪэ',
                            'ĽȦ˙lѹǸĲӋģ',
                            'ŭˑĆʑѶоμӔѶĂϕцǃʖHєǨӿƐтə¤¼ΊȔ¼',
                            '©ʼθŏƄ¦ÆŻÐЈʘʵњĂщyŗYĿ',
                        ],
                    'event': {
                            'target_id': 'ȓÂȯӐдȺ˾ÌɠБÅŹӤªňȦāχХӭ˃ЦÜÞқ7цŗ˦ү',
                            'parameters': [
                                        {
                                                        'key': '˼ʅĖҟЁŎ\x8aԐШŦԨȃěȖ',
                                                        'value': 'ɞĥкϦǸ\x80ɜƗѡѼRѲёǳǓҌӬ˝эɤЦǚ\u0382ӬЕуʩҜґΓ',
                                                    },
                                        {
                                                        'key': 'ôŸѕүѕ5ԥҝÚĒǷư\x9bӭƎТFʰÆӁƺkŴԇҮˣѿЬǾŧ',
                                                        'value': 'Њî¨\x95ҨąɟԘBԚɐǛ˵˜ǁўćƲƻˀϺǄͽȓǄǰǀԉV\u038d',
                                                    },
                                        {
                                                        'key': 'Μůхȅдîͻ+«ΏϏԮϫϠɫϱ&ʗ[^λŧĚŵ=ΐǳȋΨš',
                                                        'value': 'ŇƯʵǜЋI£ƍͽОϻлΌʚѨȶ˫}ĽĔɆŏǩàʾҒȢǒʠư',
                                                    },
                                        {
                                                        'key': 'Ƈħ\x98\x8eЮȖό²ұаŢϘҢԅϸôѰ˵\x8aԬǠсгȤи\x8c',
                                                        'value': 'ƈ҈QÂ˖ȦɽʏĖĪʳ϶ӾɳǱφгфŇɧįɰЧǦ҇Š˃_ŋн',
                                                    },
                                        {
                                                        'key': "҆'ϊĬȀԖˑǗǄ˓ϒ\x89ӓɐO˽ĬΈŜԂӳ\x85ǶΧҭtûʁӻЍ",
                                                        'value': 'Ѩǈ˵ЁʐҪ{ѳѡўӚКƕѤЧŀ\x92ƄɮΉԖξԘö˟Ĕ¿бŹƚ',
                                                    },
                                        {
                                                        'key': 'ļϬɖʱϴѰˈӐҶцâĭԨМͲӐӾϙѴǷФҏSΙъӝƭҦĴi',
                                                        'value': 'ҍ˫ɺόǌƛʬѨƓ',
                                                    },
                                        {
                                                        'key': 'ЖɺĺɍˎĎɊ\x94șƳӺҝƯMϯ°ʢΓɆ˹ĺѥқї˰ѿΓ\u0378Ęĸ',
                                                        'value': 'Õк\u0382ưaʟ˞ßǗшБ\x8fΪЈAɼµόǋŬ˒˫ȫΦҢԪвɖĵь',
                                                    },
                                        {
                                                        'key': 'ӝʅϼ\\ǹœƎϜ;Ӈ®ʧ`ŽȿǫяͼҊέ˦ӰɿʜƥњκѡɵԜ',
                                                        'value': '˰ʯj<ȘɅωѩ$ϷƪԚˎÜǭǖìԍҎϠǑ˓Δ;Ͽǝ1єľʎ',
                                                    },
                                        {
                                                        'key': 'ȝƺăƋ>Ӧ¸ɡ˗ЍƆҷ˳ʿԀŧ$ЯΣͱņȉӼƅ҈Ƣˢϋ˹ǉ',
                                                        'value': 'kҔԧϜϸТ˖Ӟ˪ɞńʨôъВыѡĒƥЮԏɕĹ\x8bŇ0ƼǄ×Đ',
                                                    },
                                        {
                                                        'key': "ԛҸҹʠUӒÓӲͷƳ҅'+ŊѭŇӛűƜѰԡ\x93ȝѽÊΈВCқ5",
                                                        'value': 'ˬĆ˫жĿҟҏ¡үͳɵUƐº˝ϲ.g˪ӲɐǅКϧ÷ʂѳÝĴΰ',
                                                    },
                                    ],
                        },
                    'comment': 'ԌǸƮɗÚȜãΖϴ\xadǩʢȺCԓԇφǃÛŌ\x7f¨өԫt\xa0ȚȤ\x94Ĺ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'Џ',
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
            'name': 'ƱáɥɽɂC¯÷ƈɲυǬɨͺhðɔѢ\x86ŞŰ\xadĄ±ʖғӯĕ\u0379˒',
            'description': 'ȧ\x80ѣЬƢɻĤёƖƁ\u0378Ƞѩƽ\x98Ӳŗ±üÜȦʩŧʡԥ˳\x93ϚԉŒ',
            'target_id': ',ȌƙAüЖӬĹ(ŞЯӟĦ˗tѵĖӨԜ>ԛҗʳκϺԞȡmɱǧ',
            'parameters': [
                {
                    'key': '˭ƃѕБʖаʣϜřϡϞΐĝ\x8bϤԍˁcÝɺĚƯȍҳƙϘĶ\u03a2ƽͶ',
                    'description': '\x96źʍӰιƻ\x94ΩǏʃǭϐɒѸϪŊҜҟҝńȫΪԕÉǩѪѽ\u0382Aη',
                    'default_value': '\x87\x9eДëǑЃéƸȅQƄƥҧũŨ2Ͳҽʖөδ#ˍԔȠ˅ǘ·ǫ˻',
                },
                {
                    'key': '˕ȯϦӊŢɫ˒ǉȻџμЕǀ\x9c\x86Ϸ\x99ͳώˊόZ\x9dŒgТЎśϿϹ',
                    'description': '\x98ӫʤӃНΌєĝλưɍЈȊ©ˑĀ§\x96˖ɶɽɽВԢЎӬʀōөʭ',
                    'default_value': 'ϘҸ˸ЅŲ·ưÎǼţ\x83\x7fŝ¯\x95Ԗϻ˕Җ\x8e˅ˢЧǀпҁǳŐ˝ћ',
                },
                {
                    'key': "ɳƼħҼŃмҌәěАË\x90ɢҎˎ˶ЫίĬӀԂћɴÿ'-Ҵѯ˗*",
                    'description': 'тɰͳмԂȫґҤçˊƣԘɩ7Цр_ïµǺTХиѹеϹʟʁ\x98ч',
                    'default_value': 'ζӘŠƨӥʹƳǤԃ˪ĀҮ®ʖќ˲ȍŸǂи˶\u038b¨ĴӋĠƬҟϷӾ',
                },
                {
                    'key': 'ɌˢɅєӏȓoɥҀϯɱźɄF˗ίϦӝИӱɼɒưƚũ%ÞӒʴл',
                    'description': 'fƼџɅǴǠΡɪÇˤΗӚԓǸŐ҃϶ΤšΟŎ;ԡĘҷvÏÍζα',
                    'default_value': '·Ҹ˛ϾȩЌǤ¿ǇȆ»ɂʎжƿЏŇИ±ΉΜèʿʖĮГ\x94âñм',
                },
                {
                    'key': '^ǜϡͻтѳӦҝˠʴ˅ˑӼԗʲɜԪʙ[ΖʢЕŹͻ˞ȑοʘҫʊ',
                    'description': '˛őӡȇÔѓңĬżσЁǲΕɈŻƥÃʟwφρŶɌɱĿѸԝĭƳ˝',
                    'default_value': 'ъĬȉɑǼУųĬаɆϼÝҚҝπϓЉ¯ЬC˰їšЉϤӇӫɏǌЍ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ЗsԔ',

            'target_id': 'ԌсМèŶ',

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
                    'name': 'ȸӒĻ҅Ɇи\xa0Ц҇éĭɬӳԄ˔ȫ.ĒƽԇѻɡβԙЊbɴƔ¾ɤ',
                    'description': 'X-tɞˌǵ&τöҩ\u0379ĽɻȉΊ63ΤϜЄŅĺü(ЄɊʡʮŜϋ',
                    'target_id': 'ƀʶ©"ЭіΌǗƽ¶8\x86ȊβʡˬМʴĐÄʿĚȭʬϵĤ¿ɗУŤ',
                    'parameters': [
                            {
                                        'key': '˻ʑЭӇ©њǹȟǣУϩɠҌǖˠ\x98Ѫѻł˝Π°ʒϠѧѪˌңҢό',
                                        'description': '\x9d°úɜʣѦǌЃǛgԊхȋψŶӱƜĺ\x9bОӾ+ɳЕчǯ҆˽˃Ԃ',
                                        'default_value': 'ɣҲ;ѣǿԔ˸EͰԀ/Ҝ½ʠЯΐҺƒҲȚǠжƯʸǲϻ\x97ҫ˟Ξ',
                                    },
                            {
                                        'key': 'я˷Ț˚tˁšϺáŇʇmɞčӊSɝ\x8aƅȳӱ',
                                        'description': 'ŀ\x94ƤĹаΥɰϮɷŸЊ1ёϪƬɟ!яŏǆҬ+ЅȄΨˣƊƂ\xa0ƌ',
                                        'default_value': 'ɂĺʪѹҸҸҞɝʟq\x91юδΪЍdŠ˗ʠԔӫдԍȩϰçҍˁơƢ',
                                    },
                            {
                                        'key': 'ƸūĺӞ\x97ȽǜȎ\u0383ʌȖüҏ-ѝǸϱ˶ÎǌũŢϐǏНſŖÖË\u038d',
                                        'description': 'ʵΘм˛ſŤȞѺęҁƶω°äŞȰԛсƜҩϺƬĲČǰƳΠÐ;ʓ',
                                        'default_value': '6iΙ;ΩǎΝǏʧː\x94ϧњɾϏҴзɞϊņӲǪŀƬδƢɧƠ\x8că',
                                    },
                            {
                                        'key': 'ǕѸԩƺơҶȐɓʿѤHԪʻҁȩĖяҋʰȐ¤ɦ¼йŇ¨ȭрȔÈ',
                                        'description': 'ȭҾʫŸəŌǫʾʟϳьɚҤ3ϚȞО\x82ӡҿºί\x8a@ѩΏӓñМξ',
                                        'default_value': '\u0378ӇĕÙ5ѽ~¡ʍцǩȤƻÄĮUϥȩơʴҐҰͽӥ\u0378ŉǿƥӏ\x9c',
                                    },
                            {
                                        'key': 'ϬΡǝЙýǺOҕǂȖȖbЍbˬɳ¾ť½ЯɍəĀфӓӄ¥Ýˏϗ',
                                        'description': 'ȱėɱϓF:ӧ\x82ŮČƷѐöɌ·řÎ\\ĨϮŜĨʒÿ[Ӡчβϯԅ',
                                        'default_value': 'Ωǻȱƹò˱ȃmԟ\x7fǟìТʵ\x91\x9döȆǤͷƼлЅŎǎ϶ԁͲєԩ',
                                    },
                            {
                                        'key': 'ԞɊÊƼɫώҥ˘ȉ\x82ʟӗɴԓҢϷξўaƐȦϮ\x8eɜʧЅԅƶƏԅ',
                                        'description': 'rхϡŌ\x8bΔӂʑӼτ\x94ĳӭǬюͶɔĪʗВʰƢƺ¶Ĳ:ɜ˔Ԥb',
                                        'default_value': 'Æʒҧ½Ǫɺɠȼ¼д \x97Мӟ\x99ȾɟϜŝ\x8eŪ[\x83ϡƉΤĢ3ǆԙ',
                                    },
                            {
                                        'key': 'ŵɕ˙ǒ¤ѥų϶ǒǈ\x9cƒ',
                                        'description': '2Җơʟ2҂ɰȨʾѹƀͲѬó҄ϾĶȧŁŋҔĊđĘǿʡ\u038dзǰԙ',
                                        'default_value': 'ȸҟӑѸǡɓσѺӳѩԄ˯ʕ2ώψ\x8aʳʴӀԖȸ£ӛĘл\x93ɋƄD',
                                    },
                            {
                                        'key': 'ȓˑÃӟ˔Ƒ[±wWɳĒϣ˧;ԃ˛ѶъϩŢЖǶ\x80\x91ĤȖʼƼȖ',
                                        'description': 'ͶԚĤɾԏǫĐҰŗӁŜ˹ƳбӆȣÀχĘôʻ\x92ӀĀ/ț\x9bĭōɗ',
                                        'default_value': 'ǰ®÷ΝʒԟĿ\x8eȪíʀμʭʦΑАϷȮҮ*ѦɥʵŠbӊϣɇ¨Θ',
                                    },
                            {
                                        'key': 'İƲҰԢԆɢǢȆΐÜȃƀϋÃƋԐĉƸǜʢ\u0383ӴҨ˗Ü҄ҿËӔѤ',
                                        'description': 'ҧYйʹǧɚі\x8cЛǚгVűΔĽĞϛƋǾǪ\xa0ȯȎϿɫƏ\x8bɟşɋ',
                                        'default_value': 'ѡӻԣТɑS8\x8eǝӷæ)h\u0382љøȂ˕νȼΟЀŧ¢ŒɢϸҭҔӔ',
                                    },
                            {
                                        'key': 'ϡǂ\x95ÊԚ\x9f,ζѳƊȴʪþɎҠѹƫʮҩΟўƕ\x8dˉӔ\x98ώέÀˇ',
                                        'description': 'ԒɬɊҨԜŭ˒ĝ˦ϤƧǴȓЂǴњPÆŒʽҿɛÖ`ӱѧVҁӪ6',
                                        'default_value': 'ԦщϨѻȮ%jţ˅͵ádʽ˙ѓƒþ½ԛЖͼфςåϿгҹˊԨſ',
                                    },
                        ],
                },
                {
                    'name': 'ό£ˌ«ŜĲӶҙӒͼʐϻ',
                    'description': 'ϥюĕ\x90Ё$ηѬɷ$ԎɳĪˋƀƒŽһяɳϘӱϑԍȯԡéÝɐÓ',
                    'target_id': 'ӎӂӵLȴƒ\x84Ūŉǲ˒țәӢɓʈΌԏʅӺǌӖ\u0379Ç˝ʜĶȨѧԝ',
                    'parameters': [
                            {
                                        'key': 'ҨѯҿQњ΅ʆѣN',
                                        'description': 'ɕ8УԂƎǙфщŝʌŵѫUϥуµРƃ6ǻϚ˱ԭǀːϩΩǤзŗ',
                                        'default_value': 'џӋϰӁʹAƼȏΪҸвǌԮƵĉӲϣ¨Ԍȫǔ£ĀϟȳјȃŒѷȕ',
                                    },
                            {
                                        'key': 'ΐӘӦǓӼδЎԔϏɊΎɒ2óϘƻͼωȭžɗfҙφƟŽҠҷѵә',
                                        'description': 'ϦЄĔԙƲțɺԊÇʺƵƄуşƞ˝Μ3ЯοŁ\x91ȣĐҼ˧ѓŨǽҪ',
                                        'default_value': 'žƑϖύʞӠɇɰӠ¹ªȳӈʖȧ%ɶЬѦ,ŔΣňĩΦҡé¶řǁ',
                                    },
                            {
                                        'key': 'ZǸϰȿŽ@λˍӪΰʾáȥŗʹҧǌcӐʠнȥӲpǙν¦íΜƮ',
                                        'description': 'ДÅЊźҀmԡĽ¨ɉƨȫǨӁ[¨ϼ\\Ǹ˕ЀϟƊ˟ҦjÏɚН˛',
                                        'default_value': 'ËԕϩиȰϚ҂ʋŗМΈԏčBӑӢƠɣɁ;ΊcƜɬԮЊ˝ʧǳı',
                                    },
                            {
                                        'key': 'ϱҟѓ',
                                        'description': 'ўӴӌ\x9cӚ×ϯԉ˓ˊΊ=ЯɮǎфΩÚˑȡȗВ\x84ĉ\x85ʫҏŉXҟ',
                                        'default_value': '˚:$;кȋƒϴƌ\x83ǡЇzµÅ´ȨÃѺ|ŖӽľʚÌǌʟŦ\x85\x94',
                                    },
                            {
                                        'key': 'ɎԛѐëԑGǅϷLŖίƵѕ×ҶОɒήϙЛ\x96ΌƩΣҀ\u0383ΜвԄБ',
                                        'description': '\x9dȱXĜǢϕCEüčͲͰŕαţйίț΄ʀċʏʹÓӸˠΉpΩ.',
                                        'default_value': 'ʏǫɁ˫ԮĠɈ÷ʳԅӹfɍƂƆșʠƑbҪόϔ¦Őˠǂƹ¥mҚ',
                                    },
                            {
                                        'key': 'Āйƈ\x93ǒбɺq/ˆҁӬɤ$τͿԮ$Ԙʽо·ākiэȠ\u0383ӰĎ',
                                        'description': 'αԠɳȈĄŊзВԨç0ΗęƜĴŉҖҮΊиŔыÊ£ѿʭȧʉģѭ',
                                        'default_value': 'ЈʌȄµіϲϳÃģŨ\x94ҥ%ŏķǰĪэˆȥԈwһϑŨҢƀӶҺҕ',
                                    },
                            {
                                        'key': '\x7fѵŴÄҹ˚ƽ͵ҧ\xa0оƱèǐΖ¦ȇӋѲ±ſΧЩĶɎǑœĸʄР',
                                        'description': 'РņҔӂ\u0378mQ˨ӬЬɿͻÆȳӖΩɆƹąӸʅLӱǨ\u0383Ӛȕˆ\x7f˯',
                                        'default_value': 'Ƙ˺Ȍ˯)ȏɰɐŇF<¶ýӁʜθˏ¢ɮΊaĉ҃ĞɗƮòΠӤď',
                                    },
                            {
                                        'key': 'ϵΠ˟ԘʁɳˉʱǞÔ˼7Ɋ\x8cƅʫ/-%ʸ˛ўϯƋδԑѤ¬ˣʴ',
                                        'description': 'ςҹĪʐŌ0ɳԀͰŷ~¶ЧʨЁǄȏ|ȸˉͶǣ\u03a2˧ͺϳì˔Ԑ;',
                                        'default_value': 'ђϮɿ˻Ɗąªέʳ˖҇ЎԜͺʧϢƝǽқͽġϹ{Ĳ˚ɋƭɜП˯',
                                    },
                            {
                                        'key': 'ʸȭƌɏÃ¦\x96ӆY˰ƼԙʅƱЫѧӚӪҮԉɝԡƵƜĹxґ',
                                        'description': 'ϝȁ\x8aΎʱԦbҡˊӋԝІӁǦéɹɏԌџƉ\x82±ñЪʥ˧ӒϢ˯Í',
                                        'default_value': 'iȌʬȊӵİѩų҉ӋȑįˇúrĨµ˻ϖłā˒\x81ǔ¤ПýҩԒȡ',
                                    },
                            {
                                        'key': 'Ŝ\u038bЀįǕЂϗͿÃԧȪԪɸӼԧAțȒљőĔ\x86ɍŦǼʛӞŨǚư',
                                        'description': 'ĊˇѤʣӴҀξǬΞћӉǝȜWʐΡсʒȫ;łʬɅ˾ɫЬǳɮѵԏ',
                                        'default_value': '҃ʟũɴċ˶Ѐ˴ԙń2Ӫ4˄ƴԗЬЏ҄җ/ȪңƋӛĭӺζԓԂ',
                                    },
                        ],
                },
                {
                    'name': 'ʹǄā\x7fɓɉȊξ\x86ɏǟҙ˾ùʏͺÖÃƷʥ¤ςǘ\u0383ʧѐЏËʅØ',
                    'description': 'ϒνðɺŶЋӻğžӹç\x98ђǤӭӮάӒѴŉZȸ²\x8bͻєĐb\x93ȣ',
                    'target_id': 'ӒЀÎȵѓɗİ*ƞΟ\x93ǵ\x99ö\u0378ĩÐԠ˖ԛƥϢӎЦΏҏŋ˭Ҏǘ',
                    'parameters': [
                            {
                                        'key': '˩ЛƣӇҷ\u0380\x8cҽȶˢϰøϤӺ˲Ȧ¿ЃʰÚĺԭʉԦĄĴ˧Ãɛӱ',
                                        'description': '˽(vƱ¹ϭƘʻʁϯƦԧ¦ȐΆÇD\x8eы\x9aşƴШ2&¬ŖȅιЍ',
                                        'default_value': 'ƧÂǎΥʑǱː=ˉΧʳӸТj]ϐԩɷŎѰϫϏëѐͱʧѧ˖ћϾ',
                                    },
                            {
                                        'key': 'ʹʠлͳȮǪҬɏΦϧÑӎҤ˗Ⱦі»дıѓ\x87ΉˣiԁʯɜƨRξ',
                                        'description': 'ҁνôʴϨďЎʴЛȭʸ\x9cΟʢʾƕɀȚķȱѮͰȜϒʺʦѐѫӚI',
                                        'default_value': 'Ǭҥƻ\xad˽ȟΨɦұʮŉġԊʖΟƴωßĩʼğ˩ΠȉӵЕź;Ҡņ',
                                    },
                            {
                                        'key': 'Ƙоʗīԁ\x90TÇ҆ƴ҃ĔϠϴÿĵ^ǬęĿÉĒė\x8aǒԑҺʶÄɗ',
                                        'description': 'ԐєƎʅơǯ{ĸΦËæž\u0379ʯǭɃϸ;ŢʲԞɍƮ\x7fӚhɱ҉ҁԆ',
                                        'default_value': 'ĉĠөԌóȓȻιҺņŮр˵ΪІ"ԊĎѓƉGÅǱώѫѲŎlȋ˗',
                                    },
                            {
                                        'key': '=4ɳԈ\x8bˈ',
                                        'description': 'уŬĬ\x90ˋѥNļIϗçџϐЉҨ0ɲёΖſǨńӧԂɊ҅ЕĿˀϐ',
                                        'default_value': 'ƒȰДҬʧššȫƷɕǣʚǯϡөˑ\x9fǔºύϧ\x95ďǦˎΊА8ΈƠ',
                                    },
                            {
                                        'key': 'ƘѶòȯë·˝ȁɩαФˡӬäˊ&űѥŢAʕͼɰӚǋϼɱƫµȒ',
                                        'description': 'ĽǃʃцӰǂ\x9eӝʛʍǅòÇ҄ɝʐâÃʮΉǔѐħΆFҸЬŚɑʭ',
                                        'default_value': 'ѴҁǻÛÀˊΒЯѤԉԛн˄ǺƭȽҷөӖɹ\u03a2˜CĜǏΊӠϽДƶ',
                                    },
                            {
                                        'key': 'ɂCǪĎȾŬÝʺ˒ıуԒҼ˪×ΞоʦПĹӡԑɬɉÂηƯàԇ˃',
                                        'description': 'шȽҁѯчãҽ.ɑƛĂҒг^ӘɉҀӀҹ˄ɶҔ˟΄ԫˎϵѼЀv',
                                        'default_value': 'ǒεŇўŧɜȧŏ\x92ʡ˅ћß˫щ˻҇ȚʫжĬԫƘңĉҶҬк!Ñ',
                                    },
                            {
                                        'key': 'KΖҲÓŉ˥ʶ',
                                        'description': 'ͳ˱ѤʄѕІƮɴĠ˶ϋɡ΄ŞӝоÊɖҩԟŶLӈͳ˒ћˤϪɭѷ',
                                        'default_value': 'ɎĎʳ҂ЙĵįÐŝЧk\x88΅Ⱦӛ\xadʘǁĄжҞɮ;ѺǿȒʫдӛӢ',
                                    },
                            {
                                        'key': 'ǾЬӿϋũĂēћυƊӅĴgÇǆˍɭƃŴɄƨƐǈsӥΓʨōԅӾ',
                                        'description': 'ӎϾʐʢÔҌʰhÔɉ˰ЍöY˷\x95ƥ˰ҀǉҐěgЊďIѠʔĦȕ',
                                        'default_value': 'ьӡԛԗƒı˲ҫΓоΐůϺʭÆAӮȵȜī˭РDΜƦрσ˱ӻʄ',
                                    },
                            {
                                        'key': 'Қ\x85ĝ\x8a˅ѳҿЂɥӗɀȗԮ\x96Ӏ\x97ëĵÙΟƦ\x93θ˵ѕĢǭρʲԪ',
                                        'description': 'НsĹОԓԮΦ4ʳčѳƝΰlʢΤŬԟԓΒbȊTɼ\x99λʫϤӔ\u03a2',
                                        'default_value': '˒ҝЌl˃ɨ҃˹ƞΉŶϬÈĽԬʊҽĈӿфǕƽĪϥҺԨӒmͱƱ',
                                    },
                            {
                                        'key': 'ԧ\xa0ǽɎ\x81ʾѵωƅʥŹ©©ѳ\x94ǈ¨ÕʒѤγǑчÈȍњԉϣӞȋ',
                                        'description': 'ÜʂәƽûҋʷƤӞɹΓԦ\x9bɔ\xa0´óяιǜΆͷWďϘшӌ¿Ɯ˚',
                                        'default_value': 'ѰӢʬŕ&LÑǇéәŹǴšĜɗŪ!5ҺежҳʊņˉӦβрԛѝ',
                                    },
                        ],
                },
                {
                    'name': 'ˮɭYσӍЂOĊюʟ\x95ĆӌЭ|Ʒǝ~ϔǊ#\x95˦ëԝȄĒʦʁӔ',
                    'description': 'ӡϢ˖İʔЍɌĊƋɗсԝѼʌňԤǂʔť\xadҿƴzÁԗǟчśɧȁ',
                    'target_id': 'ĕƛѪȓȃ ԝȜcȿˎÂǋǍãΠқϖʟ^˸әԣŚѽɿƣqͿņ',
                    'parameters': [
                            {
                                        'key': 'uԇ\x9fĕy½˨ĠСҽ}ǅ}έд1¶ӔˈĩųêʲƮ΅ӯÌȵЦŨ',
                                        'description': 'φȍgҕϛ5ɨίo¸Į\x90ğǝȗɉӢΌʹƹđӖǁ~Кč?ˇԢu',
                                        'default_value': 'ƻ¶ˀ˯ςƭŨ8ΒÓΘĿŬȌ¡ÑѺģʲɊġǝ©˯ʦȔqȜ˽ç',
                                    },
                            {
                                        'key': 'ʁĤӑΔΉў˻\x82ȓɜҾмԁHґ¨ǋԅü˱μч×ҠǰԬƙϛȅ¿',
                                        'description': 'ʃƿɇ5ӧÄРʭɞ\x8dơʿҒŦʠəâϔyЄɯǜȻŧӆԞϧqΐĴ',
                                        'default_value': '˛ϩуƛүΐȵɍϚȭñȫқŗӤŤpҩұϚʥЕОЇγŸάśӉĈ',
                                    },
                            {
                                        'key': 'ǣԁÈєτíӻ҆ˠvѺǴFуǡϫʰ&\x8cӶͲ',
                                        'description': 'Vʨє%ҒеƺƔƘ6ԆǌĴӽȀΑGˀǟϽʹƉϟάκóȦʊƢz',
                                        'default_value': 'Ǽѳòēԑì·ҋɯȾџХʙɣŁyʌσԞǺϦҥ\x8fì[ıbҀĒƪ',
                                    },
                            {
                                        'key': 'ԁƱɀźǫƉűƩJÖŶъ\\˽ĴҸӻԅ˹ϔ½AЭʡĘѢƐĞʙ',
                                        'description': 'ɉ»ӌÒrƁ¿\u0380ý\x96¸Ƚ¬Üљσk\\ΰ{ҍЧвӔĕĊѺȺøϖ',
                                        'default_value': 'ǄŭɯНáдϪǌџ`\x93ȴԉȥҦAϒјɄȏƓԮ\x93ǉƼƁƋˏӾ˅',
                                    },
                            {
                                        'key': 'Ӆ',
                                        'description': '˱ŀǘ҅ӝԤƀԎӞȣӠnºgȁʂǛƔƆd҄ȕҳѝĎǺԩǼҔΕ',
                                        'default_value': 'ÜϣȎϰ¿ЃԩαΥɩŻʀӓӾ˦ЂĲІŶԋӛuУŽԇСπ*\x89Ê',
                                    },
                            {
                                        'key': 'ɐƋԃōN˅Ϝ/ªÚīð\xadǇӡΫҖɴ\x94%əʨӺȥɐ˳Ƽ{ŁӔ',
                                        'description': '˝ÿπȿ\u0379ҾΞУĤѲʃǷŤϤԜ@·ҁƸ£UӿµñĬǲқβȠÉ',
                                        'default_value': "ĺӥԖŐ'hƗɌОĿǈ\x99ʚҁʏѲlϬɺʆǕŌϹŁCìñƖȝͻ",
                                    },
                            {
                                        'key': 'ʲĻӊȿʽѲ°ĞΝ҉',
                                        'description': '¨ʰӍȃăќÐĪ^ɣӟĻѶпйȆѶѳљıɎΟĢцɱҜМżøΒ',
                                        'default_value': 'ɪƞŝƴ҉Ҕϟ\u038bͺʺǎϦȴ\u03a2ӧ\x89ɣƵнѕӑыʏҺ˵ƒĂϊÓү',
                                    },
                            {
                                        'key': 'ƒǂ˶;ɔЗșЂЉҘήɚƉPȻʡЗʧ΄ԌԜȂƉŎƑģĜԫϤț',
                                        'description': 'ϡϦѡӍ˗ƚғ\x8fόϷΣԌäRɾ˞üԠǌϑȮМҫĭÿҐҴҏѩd',
                                        'default_value': 'Β҅ϕɻĶϖÒjϗÐщҙёĿƢYӞȢЃҵӭӰɎЮƨʄǍәŪӇ',
                                    },
                            {
                                        'key': 'QɦŀġͳРҟȡʉњĜNʟʔƹ¯6ˈǊåϪя\x84ʟΡϿѢЁѼ\x88',
                                        'description': 'ȬǼˇƇϠȤtіӿŠ˶Ҽ\x9c˛Go\u038dŒ\\Ό«р˨ǦUãцѮϤ¨',
                                        'default_value': 'ѓȔЖ˱Ǔ\\EÀTƶԐVáδ\x93щʯȥ(£ͿҒ˲eͽWѿòϻÔ',
                                    },
                            {
                                        'key': 'đӳȷʻϪƲ\x9bӻtˏԏąӇӉȨЦӴwҗЭƵӄӅҫŵїÝɗɌǃ',
                                        'description': 'Ó҇ѓЬʉĸɃϹö;ƃӟʮɖӸ^ĀĎŕġȦ-©Ί#ȲǁуΦϸ',
                                        'default_value': 'úɛ\x9b҇ÀǚċρԠК őˆʷǣΈţΌӨԠȕˣȐɵӁсĥӨҩ˓',
                                    },
                        ],
                },
                {
                    'name': 'ѭѶ\x8eŹȜЗJҮΐϝ\x9fĚ˱ǔˏŚfįϺЗàĵпWƍǅԪ˩rˊ',
                    'description': 'țʲEiϰϽԇԉȄʧ¹íЩҩԬ\x96ΙЏŒȏѵ¥ĞЂ°ɾщƢ¨ҵ',
                    'target_id': 'ĩԀɤГ³ȌǇŞҒ҉ѴͲΎɕȚ\x85ԧƑјˌZÃíƓ5ÈɩŨĳс',
                    'parameters': [
                            {
                                        'key': 'тƐļ£ԨѽȴťğоԎåě@˛ԃɅєѴ\x92ŎÁ˽İɿYЇЀΧо',
                                        'description': 'ѻҧĖϩһԎԅҨǽƞǛϪΗ?ԂӝˢɺĔMˁӯȶ\x9eɺɞ\xa0óŪǇ',
                                        'default_value': 'ӘȼQЄѯċо\\ĚèΟȊĈ5ʀкѤȶêĕđ˞ƪÊԖľЈ҄ϙĜ',
                                    },
                            {
                                        'key': 'ɑήǌťӍVɮưѽѺϼѢːӡ)ƣϤ˱ЅˎòʩÏƁбЏHˁB\x90',
                                        'description': 'ҌϺƁӾҌƔǢ˸ȡȴ.˼˩Ǩưśō[ѓʾбǼ\x8aԌрӏȢÕźβ',
                                        'default_value': 'ʽҫѳŎͱȘӰĳɉ\u0378їҪūҪɆʬƼ±ҧϲ˥ԃɪƨƎγȡ\x9cǗТ',
                                    },
                            {
                                        'key': 'ůɟԋÉħĄ҂Ǩű\x97Ӎġϻ¯Ęӷ˺ȧѩā$ʟΈӷ§ϤȓG\u03818',
                                        'description': 'ñȏӤOˀˡˈŧТĀʖԦОκǓϨҔžŗ°ʚ\x92оêʓńgĂЛҔ',
                                        'default_value': '´ѢϟļдӐƥ\x9fԬěĦȵѱĠɒԔØȨ˖ҝңĺ\u0378¦:ƠɒҀԁͰ',
                                    },
                            {
                                        'key': 'ɶϼ҄\x9dĒэŮ\x8cˉÇ˼˚ͺp*Ϳȫˬ',
                                        'description': '*Ԅ§ӔjҤÌϣÒѦѻɒԬǀԅȌɹ(ԗÈÕӫϟ©ӫόȇ\x9dν,',
                                        'default_value': '˺άԀ\u0378ŵҲ\xadҮʩ˧ʻѧÑӋˏΈÍµˤ@¸˽ӱϗȐŶµԐԡɐ',
                                    },
                            {
                                        'key': ':˹ȗцğ\x83ƶǙυԐΤӠºԐžǍ\x89ϧªϛєƺѳÁ}+°´\u0383ķ',
                                        'description': 'ѢϚҪƮƳ\x82\x99ɧʨѼҸʠ´ǚʾʲʱπʜŧлЮȏˀАȁąûƏ\x90',
                                        'default_value': '{ōøӸmӻ£Еòǋ˱ǑѻӺÈŬÁʴь¢ѡǚƶpŗɍҩɯèʬ',
                                    },
                            {
                                        'key': 'ϸΤ΅ŕńƁρȻпҏ÷ґȾ\xadOǸȀňϻӍʿι°c˾ʘnŷ҄ľ',
                                        'description': 'ұǄԩǝԌ˨ȹІOћ&ӻҋèυȄJѬdԞ-ɽϋʗʺʚ҆ĖŇ˸',
                                        'default_value': 'ӟ7ʐȣɴèϯ½ƮĀҸǞΌĩʚБ`Ёѫ±ΦΊԌԑϳʕʢˉɾx',
                                    },
                            {
                                        'key': 'сͲʗ°Ûό<Jσʪ˚³˄Ӹɸ4ɆӂψȓӥȞǦє0ɍшϜıɨ',
                                        'description': '҄jŸdĒBҺӾԆѿ!.ӣ[ԤcԢӝɞ˥Ʉ˛ɆκУЃ4ьӼѯ',
                                        'default_value': "ϐÞΐˏ¥ԫԇӐǶѠӱΰǜϸ¶Ϲ'˔ïé˫÷ϝӯӾшρӈ\u038d\u0379",
                                    },
                            {
                                        'key': 'мś˔êɞӧИÄЩј˨ΔԁǷԎԛ®ѧԇ\x8aĞċԒҎž',
                                        'description': 'ŏãϚμӗïțԨ˱mɼԌǵЉʂЀЪŸӆοȂӈCԨшǗϛҔȽӉ',
                                        'default_value': "ħΆӇѪʷрʌƛ˞ȇоȩȢУæЄ҉ҝҨw}Ɓ'Ⱥϒ˼ɖԄˀѾ",
                                    },
                            {
                                        'key': 'ѦȠÇԈ˷҂\x81tʻҟż˼ƹûͰӷӳύӲ©ªǜѹŝрf\xa0˱Zς',
                                        'description': 'Ê{ƅĐÕȕҶ\x8e˪ŷѓƵЕˑ\x9eѝԙȒΣɣҨͲEхŠʮ<ǗѵΑ',
                                        'default_value': 'ʇƄЦ\u038dӐ\x8e\x89/ěӮϽʸɳҡҨљРΏ҅Ԟȝ˵˒ƱpЇҨȁԎн',
                                    },
                            {
                                        'key': 'ӱЍόˠўˁʒ',
                                        'description': '҅\u038d}rȪʸbûəƑʢŷ§ŢǣіÿīРҲԝ҃ҀeҳǰϗÍ˷Ʌ',
                                        'default_value': 'ˋƈΨ$ԑτɊ\x89ǶʔЇӳԋǿ˪ҏϯГɤÄʞzαћ·ͶɃԎŁ\x9b',
                                    },
                        ],
                },
                {
                    'name': 'š˵ƅԡʓÉ¦˲ƒƨěgѬǓ˓ӶEǮ˗ƼԧņɲӃ"ȉҹюӸɪ',
                    'description': 'Ņԝ:ȟȔӈɫΑͼʩѺΫ-ŋӪӪȸɨȐǣɠďų³ѝǷɊɐ˟ѕ',
                    'target_id': 'ȞŤӞҹþːÌӤIҎԓɞoȩɾЬłѓȩǂѥŽύѯłǍÿȜЉȁ',
                    'parameters': [
                            {
                                        'key': '˟ʃ(ÇŮÍ˼ɂǠkǅǪѦŇ\x8bȅɪĤ˕a ϕʊɿŏˊÈβĻӑ',
                                        'description': 'ӬÄѿĤɼϊĴΐcϨԫęɞѲѸcǟɁǙʋ\u03a2ƔʞȓЍŲȃȷǵĚ',
                                        'default_value': '4´ԬơƚŒƢԉԜԍĻȍ¤ӔōʊΝȩ҆»£ҀҝҒǚ¤Č\x88Τū',
                                    },
                            {
                                        'key': '§ӿΓ˂\u0379fÆңðƼÙΥǠϯŰĂ˻ɲеæҒǆӱ&˧ϡŊͽĆѠ',
                                        'description': 'ƯͶ3ŜB\x98Ϻ\x86ːςϓˁІԌЎӹKх\x8dȱɆǠҊˡĔϒƐȕ҄ρ',
                                        'default_value': 'ˋЀħѰΤmӀǡŷɸцŐѾԈӑ\x8eȊ×ű˂К\x96ț˔ɅȈIFƋ\x9e',
                                    },
                            {
                                        'key': "ɒřį\u03a2ԄԏӨ'ƙʹƍӬТƠѧŅΆЭÛʩɎƖшŧЛεѰʮÂ˕",
                                        'description': 'ԄͿ}ȒԠъʩéΙӪͷİҎϓæǲ҂Ό˗ŐШͷ\x88ˏѕƢԦʸӽΗ',
                                        'default_value': 'Ҏø͵ĉɘˀҮɕϏXςñ҅ΕҌǏҝæ9ԌĊēчǷ.ԝ˚ǁŘѕ',
                                    },
                            {
                                        'key': 'ЮȉЦ΅Π@Ӏ\x84ǷҿԭŘΧɧл?ÓӞʞΜѻĹŤΧ\x80ØЦÀʞǮ',
                                        'description': 'ӭªĚōϨǜBʇЕұǄđʏΛ\x87ԓϗƂŸҀɮӓȄΰǌӻϩɱϑȠ',
                                        'default_value': "ȋŤњȘĈ\u0382ЗїɿӕΣ϶ԍ\x81ǭʹGůԤȰ?ʾʷϕȺОєƣ'ԫ",
                                    },
                            {
                                        'key': 'їԤԛ]ɧOʪІţϸ2ʹҩѴϿˊή',
                                        'description': '\u0381ϋψ|ҀѶϩ^ӆ\x8dј=ӎL[ţѲӖͰIʒҚŀ˪ŮѫЀMϵʅ',
                                        'default_value': '`љɶѥȜĘÐҧʌŏ\x86ʣÔ\x92\x8cĜŕƧϏƯøÚѮ˃\x92уӬƈ?ō',
                                    },
                            {
                                        'key': "ɶ\x83ƃΤӗŴɷˍȉ'wә˜ȟϙȽӪĨȪӠśʄăǡԂǠȆѕ˖Ĝ",
                                        'description': 'ҏȷȔΊ¨ӳǟ½ǌſÎɷЊ\x92сbżҌȔɤɼЊdс˶šͿĤґҩ',
                                        'default_value': 'ѫǌȷˀúʹšɫТŒЕы˹;ӐɪǈÑѤıͲHҎǒĨͻԜφԁ1',
                                    },
                            {
                                        'key': 'ϢӁʽ(ӰШЦϔɯӸǥƒѷϢĂbńǾIϿÁћаǈԚUƴƮɨφ',
                                        'description': "8ǳðӡ˂ҋûˈ˭ЊÁɎƚбνԑPҗ'оαůЙòϐ©ЖӃƳЀ",
                                        'default_value': 'ɡѕҦыɒʪ\x8dɄкТϘƶƲŬБ[ƣdĞ\x8cԠΰʺφͳɒɧ΄\x9eʑ',
                                    },
                            {
                                        'key': 'ǸBgӎʘưԭȳɩȜ˭ϪnтԠғŕ5ĴˬÐĨҴȪʐ8ӴΘřΌ',
                                        'description': '\x8bЙѵȉҒȨЛыůЗĨεfʅӜ0ҌʥɖԈǷnƟʑ͵ɐэ\x81¥Ï',
                                        'default_value': '2ɏĚБԘ<OƀǢˤϵƅͻϸ\\˭ϊÃѕ¾ыġΚWǂǩǲ˼ǽΔ',
                                    },
                            {
                                        'key': 'Ѣ·þІӞβѶɝ_ώгƙ\x92\x9eȐҕ˦Ö¢¿ǗƇоǫǐȃōÅУԘ',
                                        'description': 'ɩXğĦіΓlԧԠOҠѐ҇Vƞʴ\x8eÊɎ\x88ЧȬɨʉӷϝЅЍԗе',
                                        'default_value': '˵\x95ÒцηåΰhΆč,Ɩν5˅ΏЂƝЯѧћ;Ҥ#ҬϷÀɬƜƮ',
                                    },
                            {
                                        'key': 'ɻίċöҨҸÂгΡĠπ\x8f ſŤǳɞʔȡԞӥʬʟӛ҇ȿόĜ5Ο',
                                        'description': 'η\x95ˋ \\ǯċ-ĔɁϞɈѕǝ¸ԟξʸԏlǕЏ\x83ͿðÖζǸĮÇ',
                                        'default_value': 'БЍªҩΥī\x9eƋё\x9aНǩØҢǍǑǜӦȿΫɽβĝńýϻʊԌɟ¶',
                                    },
                        ],
                },
                {
                    'name': 'ӞʥĞҿƿƿͿАΑƿȧԠȏμΟɫӟɺӔϔϖԝҎ\x87Éӫε\x84ʷҗ',
                    'description': 'ǪƙοĽæBѲTHґԩköͷϣΗͿϟѺȘғʆΙźϥ=ӂýzȐ',
                    'target_id': 'ǐмÖ\x9aƝοȀќѪĵΉӢV5˞\x84ˌįԮԔêź|ήFҺζɈѸt',
                    'parameters': [
                            {
                                        'key': 'ú-ɤɝҖШĕԪɼ\x9c˙ѹȁÜϜơǝϭĦ˹ӫȷɆ ÅΞӹȿPP',
                                        'description': 'ĴǘӫņÿθɂƾŴͲш¦ҞΉЊӈή˫ǯ¨љˮЋ;ϻЇƥɁƅ\x98',
                                        'default_value': '\u03a2üďӾʉğНƯŮênӜǊʖɍħҤʏз¼ŷҲɹĲ\x8dӁ&ӃγȬ',
                                    },
                            {
                                        'key': 'ҘʵƀpȔҿҲÇ ɰΕɗƻɲ҄ż',
                                        'description': 'ɶΫзҎЕŗɠҮԇԆȱΉʈȸyǞшһƷ%ïǣ/é@ƟǾΏЀӔ',
                                        'default_value': 'ΟĶӢȋвǮΛΝʙɡ³ґȯ϶хҫϞƾӈӘĕƁƗϖ«έôҟϮԩ',
                                    },
                            {
                                        'key': 'ҍÓϟЌʋ',
                                        'description': 'ħĠƨŎɜě®CąŲȔĒӄ(ϩҢƈý$ˋȑʖɲЀʁаȠΙϚ\x86',
                                        'default_value': "ġȠ\x8eƊ'ǑɫƼјʴĩ\x95ŚȺŰ;ʯʙǫДȭƒ\x85į½ӶhӸŝΩ",
                                    },
                            {
                                        'key': 'ϬďÒӹӶĐʍǾ+ę',
                                        'description': 'ďŻɏϚͰϙPŲʏνǛʄê\x8bȑɜɢ˨¼ȁ4ύƙӟĿӢͻFŬȉ',
                                        'default_value': 'Ĥţϗt˓ɶėÞėƥħËѭĬ7ϽǉҠɹ;ѿԗϸđƎɯƳvϫÜ',
                                    },
                            {
                                        'key': 'ȁŗaзˎɓʢԦŉЭ½Ɉƭīϱőӓ',
                                        'description': 'ӹӔ¶¾ȒɯÃЃΤ˶ôĠÖÑƛǮϔɋ҇\x96ɯ1ɱŀÑʥИ͵Ҳı',
                                        'default_value': 'Ѭˢćќżҟ\x9aʸʱƽ\x9cŞơ\x97όȕȺϻδOː˒ϣӫOïЋ˔<ų',
                                    },
                            {
                                        'key': 'ԝȃҥϏ·θϫҜžǂƴдҸѪɈˀ҃ɼίөѤĒϪӁĚЖӯҧȕӦ',
                                        'description': '\u0382ƏNȪȰˏͷϟ˘ђҶʽҍ·ҿϷϿȶɪàȣIǔǁӃЗоʙʅȨ',
                                        'default_value': 'ŜуªŀιƧρ§ȅϷЭǧņ©ŕĲҘԁyёʘζÊџǼŠϱZǮǭ',
                                    },
                            {
                                        'key': 'ə\x8cʰΆѲ',
                                        'description': 'ǆ\u0378ʿӋŅьƦ~ĲϑœϰȇǭңЖȴÎОˍ6ъƐÒѣ˻8ūʕ\x80',
                                        'default_value': 'ψȬΟԨl~LU\u03a2тƬɷϲȻӒ',
                                    },
                            {
                                        'key': 'ǟ',
                                        'description': '³Ǎɝыɕ.Ѕê:ɲšBѼËнʨQėǴǎүĚ˺¤PĨӗғɕɐ',
                                        'default_value': 'ϲ¡ӶŅȜƤϼʪĽӼſNȦM˓қűųʢúЪµ\x9aʇ˯εЬҏðѕ',
                                    },
                            {
                                        'key': '\x96џή¼¾âϜǸɗ',
                                        'description': 'ҏ҈єѴ\x94\u0382ƞÿɅԉγӤČŒ˯˵Ȉ҅ҌƆʋÓÑҕˊƭθǐÚÍ',
                                        'default_value': 'Õʑǚ˨ыɻɮ\x95˜ŖѲƮϽȦČ˛SɥƳӬӿğƭSˁĿÅԜΒƶ',
                                    },
                            {
                                        'key': 'ҩȊЎȗǇӲdoɿʗɡÒʝļɺǺǵ˒ƿЮƨʰğ˔ǽĠʬǔΕe',
                                        'description': 'ǼѳcʣԫұњɢҍßΈpԓ˙ŕБҟźɗ¦ǿǇΪ*¶Qă¢ĝГ',
                                        'default_value': 'Ъŧ\x87=ΔƽɭȦϩÜĎϴˣϓǺɾɑʓѣ°ŒȒʠԅӑϨò%ǝҸ',
                                    },
                        ],
                },
                {
                    'name': 'ȦċԏDҾMŃǏξƬԜ\x82ͳԥ·.Ϻ˘ˇʬϖӵȼĘѵґѭ4гӧ',
                    'description': 'ƉԉʛȶԜЎѹɳˀ³˖ǭӈ˶ςϗϵŽʂ˅Σ҆ҥʟ˂ǜΉ҈Ɣǩ',
                    'target_id': 'ϵ¼ԇ°ѵKØ¼ÚǺΚ½W\x81Эԅ\xadѶϷӕǪɵNȲϿӮȲԨԓþ',
                    'parameters': [
                            {
                                        'key': 'ъЈ¨ȧɘҴ͵bŃȖ½ѩÒҕɣɇŞ',
                                        'description': 'ŰЦԑџυԭ³Űаˮǡzȫ¸ϭL˒ǴˉȝƿˋʝǘψȽЦ҇ɸ\xad',
                                        'default_value': 'зŻûƈѣĹԛҊͼǴʬԐŠǴŭȍ\x8eæӻðţťңҕԈxҥϴӻ3',
                                    },
                            {
                                        'key': 'ǛΏùì£ȎĀпѹǬƁђð÷ԫӸϝǜƗʃɷΪҦ{ιnȗӪȠ×',
                                        'description': 'ɖѹҺÈҋ˃đƧǽˡŦʺʲԥҬҵӖЮˑћӍӝÈӳ?Ķ˰\u0380˽Ŗ',
                                        'default_value': 'ύ)ǮӃϝ´˷:rʁ0ÎƵ˄ѨɦԣѢŒϸÇСǞѧƃӱǍѵǖϔ',
                                    },
                            {
                                        'key': 'ł@;ªϏщοкŻY˃ʚĳӼOt¾ΥӟɋӶýŗҜʄ`ŤȁǟӐ',
                                        'description': 'ԡӻŸǵʥǖÑĊǾÑɾѤд;˲˶ԌͽԌîʤȼԨѵȌӪÿНɷœ',
                                        'default_value': 'ˣqОфϷτƴЫ\u0378Ɔϩˉņǫʟ҂ù½®˯ΒԮΙҙÿтҟȠϢ\x88',
                                    },
                            {
                                        'key': 'ɫеǻԎмģSɩԍ΅ӝūѥ¸ϾŜйϗǞǛɝЫӆɞ\x9eÄɵñэΟ',
                                        'description': 'ĳăґ\\ůΑ¯ć\u0380ѾˣƅМΉȁЙĥŉβϷ\u0383˛ҪӭΔ˟гоɸԌ',
                                        'default_value': 'ǇƞҥπǟͷJ¥ˢƦĒ҅ԙЖҘҪӇ\u0382вɝɥӥяϡά˶AϙΦĪ',
                                    },
                            {
                                        'key': 'ѧѯˢǓԑŨԧśԩθЭɗ˃ǕνͻɉӻҳȪӚÛÓƷʂÛǍ½ƿʬ',
                                        'description': 'mŞѕ˂Пȸи\u0382ҫЪiȽɟгҾǫԪ¼ĩȅҏ^ȰēŜЀŮ˰ї˻',
                                        'default_value': 'ʀɓӛêʇΡρıѤΥԛƲо˯Ԧ/\\ě\x94ǦǄ˳ԠѹesĈ/ӼƟ',
                                    },
                            {
                                        'key': "'ΟŒӰƊĴ\u038bʞԋԗ\x7fYʣРэŶɳԖĎĽӦöě7",
                                        'description': '\\ƀʙıʰǆЧļʇĿΕțҁß9IԡȕŶøёĢǽƑǏɣӔôϷҗ',
                                        'default_value': 'Ӗȷňϓ',
                                    },
                            {
                                        'key': 'ˁř˵Ǥ',
                                        'description': 'лİϊˡДԆÅőĥƱӗ˙ЅͱǺęҌȭŧʩƪǡfǟёѥϺˁҩ¡',
                                        'default_value': 'ӂɻŹѾéУșԖВӃżƻΪПÜ\x88ȆƩǼθӏŹӖӬŮѹíȟī΅',
                                    },
                            {
                                        'key': '·ϺŋǝñŭÔҰ\x97ƽƩˈԎʣŭӺ0Ň#ӏҮϚ϶Ԝ¦ӾpǏԃȁ',
                                        'description': 'Ȕώʋ©NƇƼÞԥǀ˺ɲǼΠƧų˓ƅł9ƋʠӅԎŜȵÁ·TԪ',
                                        'default_value': 'ɌȋӝǸȃΓɬԒϊұϒҵʘЌųţȐѬyԆƜˤѭɤŔ?ԢǷѝѾ',
                                    },
                            {
                                        'key': 'ҸëɅҸˠɓђӾҝåʧƱŃіҿǉˬ˽ǗǼºϘʹǁѢɋĴСĔƼ',
                                        'description': 'ƏǘѻϏНϔ¾ɩҏЀȡӾϡώŨИA΅_!¸Ϡ ƞʱ×й\x87ң\\',
                                        'default_value': 'ї˫ĘθÐɦĢԤ\x99Ȕí˻Ϣd3ЮАǿѾŮӄĢǝвӂʝřřɇd',
                                    },
                            {
                                        'key': 'ʴȤͳɌʀЄӔ',
                                        'description': 'ɿƔŜā,4ΔʿЗ˙ŘʁЗ5ǣΠˡƕɭ҃ǟƹŚĐѼѩëʑļε',
                                        'default_value': 'ǌҢȻȕҔΨƼˢŭ\x97sξϠLɷțďțĥɪpΒŉƅѼdÉЮÜӏ',
                                    },
                        ],
                },
                {
                    'name': 'Ϗa˶ȦѭǻľΥφŜ˺ƗA4ЏȄɘΠǍȮιũхѻƴ\x81ĜöOǚ',
                    'description': 'ŏӆƬćĲƐÙIԝgȩ\x86ʍ¥ԅʘPǃʘΧĒӇȔл?ϱˮ°үŷ',
                    'target_id': 'ʍԓӴƧГ˟\u0380ŕȴԋƍʢ6ҍΫʗ\x93ΟƝɣŠΌȷʯЂ΄ЌӽİŰ',
                    'parameters': [
                            {
                                        'key': 'ƄƉјϩƸŕ\x86юːā\x9aϵ΄cȞǞвǹҥϟϲçɈŦǶ˰ƨогϹ',
                                        'description': 'ΐҀÁÖԇʍкJƏљΚʤƏѐźÐΜȠʿԏƼϒ\x94ËÎɗΛəШƑ',
                                        'default_value': 'ɖЍԗʜŐѳðҾіѿЫİԭƎrӮɟ҃ԢҠґЧ\x97όɱЯʘ³Ž˃',
                                    },
                            {
                                        'key': 'ʰăǡɞԠɆәŗήҏʋtǚͿӫΛɄȷýχĭљƿĔîСӺıϏǶ',
                                        'description': 'љѰ˶ĖɓȳɬѴšθ·)țˣʍfʨØ=τlyʲэ¬ңǏʾѸŭ',
                                        'default_value': '¹yӎǜҧϹǌ˞ӋɋӚёȞϚˠ\x82ȪΙƍШ½ƩΝȹƇРϔɐ¸ʘ',
                                    },
                            {
                                        'key': 'ȗӥһņʇ',
                                        'description': 'ό¼<Ţ˖\u0378XƠÅ«ƙɢ\x7fҁҰµ\x96ѤȍƀҢΓɲӏTǥӿŅ˨ȹ',
                                        'default_value': 'ʑ˲ũӅǞƒЬïӛв8ӵůƻΚ˱Ѱˁ҈ЛİɣʌӒFΞĨƼįǨ',
                                    },
                            {
                                        'key': 'ˬђǺņΞ',
                                        'description': 'HУ˝ºƱ҅бĉβπÒВ˾\x81Ԕ;e˂ŋˋĀтȖɏȓӠϾԧς ',
                                        'default_value': 'τƘmvʧЂҎƩǈӈԙŠҮ&æƑƒÿǔɑԗ˸Nb\x90ѫɉΌ\u0378ϫ',
                                    },
                            {
                                        'key': 'ЌϜRҡĸҢ҅ÅȚȇ˸ə',
                                        'description': 'и,ȗʳɯΚ½ŝȟ{ҋɣѼ\u0383ƥšŹԐϲήɿϫϥƘο^ƄCХː',
                                        'default_value': 'ԋ=ϧȑǤÓғРѿųϸēÚ',
                                    },
                            {
                                        'key': 'ǢǓӪВԎӾȬˬϜȃ¢ΫőH˵ϮȷȗɖӿƥϳϼҪđƮɑɻԬš',
                                        'description': 'ɰƱƂÒʶɓӂHʠđЀѾȵɰƐͼ΄ҜɡÏɓʲЫԤţĳ&ǂēÓ',
                                        'default_value': 'ԉĻŮvÅ¼ԪъùƄßϸɣǓ¶ϘƱΠϘǠїσ҆ӋϢŵԝǹϫ\x9d',
                                    },
                            {
                                        'key': 'anƷǒ;ĺ÷ÝϠЕĒѲɏǑ÷ŪK\x86ҌўʲʀƻƓƕŪϸɈёҎ',
                                        'description': 'ƷԊ\x93˾ϔþ°ӴŬ²ʂġϵ˥ā)ϢӺӉƕҨ\x97ØČеˆҫøл˨',
                                        'default_value': 'ʜӯӖуҸrͰȟǷʫAďïɭЂĜ·ечȨˈǸ;ӢРʢɚ¯Ҥϝ',
                                    },
                            {
                                        'key': 'ҝ҆QŪχѵ<\x87ͺƍǦőxв',
                                        'description': '˪əɽǯϼǑ¹Ǜé\x95ǅҤсѣя˄ЖΆɬВ˸\u0383ҴŧѣʘкÌ^ŷ',
                                        'default_value': 'ЌŴӔЄΦØԞωǧƅʐǮɇɋ×ɗԧѷaȹ\x97ǆЙȏˮƴҧӂΪԊ',
                                    },
                            {
                                        'key': '¢ҿӀԠЂȃКʫѷˡǞϔŴː:ҳзʐ\x82ɬɂ«ЮϡѹӕΠʵĺϚ',
                                        'description': 'Ϯсԑɑʸ\x8aȟżʟê˺ј\x83¾ʢĸɍѬNʱӘυΑˬáοġҏƍĝ',
                                        'default_value': 'Ë϶ˁʋÌͺјԡ țΰΑʬ¸ǉǃ6íŐǷƽɗОҲʈŘŎƒˀǧ',
                                    },
                            {
                                        'key': '<Ǫ˕÷ϷŞʌҧhŁаɪЬĂǥƤ',
                                        'description': 'ƟˠVҸϪȘЍЀϐ\x93ĬKбːˍԠɆ¶\x9cΐͶcȁԣĴԆmәơγ',
                                        'default_value': 'ѠaIˁĕ˪қɒ\x9bҘĎ$ҥĮͰ*ų˸\x97Ȇöς¹\x87ɗKȦс1³',
                                    },
                        ],
                },
                {
                    'name': 'ԘԀςɋƺ\x87ΩȆȎƵΦЄĵÂӜӄʙӔŪƪŵѰξɡϋ¤',
                    'description': 'wɶąʑȊβԖʅԫԂǹѳȲȡɻƤ\x95\x91ʉԋˍúǩˣä˥ǿUϦӇ',
                    'target_id': "ѻӄĦYίūʻ˧ʄʇӤљŊ;˶ŅĂä'ƅ2ȥЬÕД8ҸȌͼң",
                    'parameters': [
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
