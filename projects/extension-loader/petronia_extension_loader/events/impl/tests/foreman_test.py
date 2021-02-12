# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-12T16:50:48.496763+00:00

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import foreman

class SendEventAccessTest(unittest.TestCase):
    """
    Tests for SendEventAccess
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SEND_EVENT_ACCESS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.SendEventAccess.parse_data(test_data)
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
        for test_name, test_data in SEND_EVENT_ACCESS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.SendEventAccess.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SEND_EVENT_ACCESS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='event_ids', name='SendEventAccess'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='source_id_prefixes', name='SendEventAccess'),
            ),

        ),
    ),

]


SEND_EVENT_ACCESS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_ids': [
                'ßбǂîҸƶ˚ţÈTԅϰϧ\x81ѳБʧˇƥɬҮѥӯӁŹ©q',
                'Ҹkê§aҟřŸǭь{ϟĢԆбӷơëѰƸ҆ͱȦ˄˩ҡ\x88ӫÖ®',
                '\u0381\x95ҶϾтkƈԂԕƶѷѲΏ4ɲфǽͿ˒ʮԬȟԠŜǑΖ҇z\x88ʻ',
                'ÎļĀМӧОÙƀͿҧŖ\x8dųϣάŁ\u0378˅¼ĆϑЭʾΝƋʁɛʖѿ\x94',
                'ҺńȯȵǀŁĉӞЬЌ\x8e\x87ƂyǷ ȰɻÁҖǵ\x8eŧſΥƥӖԕq-',
                'æУòWĨκ?˚ƻɼ˓®ɿѯѴɄΦųǭɺ˂ԇȎȟ-ØÄΤ˰ҩ',
                '£@\x85źȜȰûǟПȋ%ŰŶͺЛҟ;ɵɹ϶üę˖ɹƿ\u0378ΡǑԚќ',
                'ȩˮǷȯЄȑѤʤģɠĉЈŗƶêǮӉżqIɜǯǙ£ſÇЬ΅кʮ',
                'ʣǛΊ˶ǕȪИġԏϠɊзϹÇĎͲģãҪ\x7fϪϗǔϯλǢSsùȎ',
                'ѸȁϾźłˤȯʑΰѾ\x98ѯîʯ˂ʳ $6"˨εҖНʈȧұϬӖф',
            ],
            'source_id_prefixes': [
                '@ˎϐȮϯӉȉƁϗňѾΔȆĻ˱FˈҾəÇˌ\x96ʆҨͼȁДӂǀӂ',
                'ˋ°ɀě·ŇӅйǨśɕˏԘƏŤʑ\x8amťӔʶƃH˒ӸçͷЍ©ɚ',
                'ɑˣˡϾĩӼơīйЙӒÖċǼ˳θϐȌĿ¸ˬųϊǯ\u0381҇ѓΖӓş',
                'ȡҶv1ѕǀԉҊѸπ6Ѭ·ȳџ^ΘɶĺbŊЕĬȑŉԮє²Ѫǯ',
                'ǔuɱɯŉſhƴŐҿľüƑŘɂ\u038dŋȽԉÐȽНˌQơ@ˈĊʐӥ',
                'ǲϭ\x8bϷˇŵʿ,ίș˥ǝҰƞԗω϶ʺÕŁυςˬ\x99ÇĢҚΞϽŌ',
                'ĢÉ\x9fϲϚΣǫˮҧǀʲʼ\x94ņҡáÞƿʎƉɼӝǧâӪТҳĨȠ҆',
                'ĦĦ9ϸ¾ŊȖϬӳÖӯͺXђőÀӷʧеҵɛǓ˾Ќh҂ťα¾Ǒ',
                'Ϳ\x94ΗʫʩҪϼɄϷò5Ǝǀ\u03a2ҵʽĘƊϴԙ\x83҅˨ɏˊAȪǻ҇ȅ',
                'ȿӂχҔαšѫȖΣƕӬȬӜҋ\x82ϨƱΊѐɴ1Ǐ ΩŇŎǬ\u03a2\x92΅',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event_ids': [
            ],

            'source_id_prefixes': [
            ],

        },
    ),
]

class ExtensionPermissionTest(unittest.TestCase):
    """
    Tests for ExtensionPermission
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_PERMISSION_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionPermission.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_PERMISSION_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionPermission.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_PERMISSION_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='action', name='ExtensionPermission'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='resources', name='ExtensionPermission'),
            ),

        ),
    ),

]


EXTENSION_PERMISSION_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'action': 'ʗǀŘƮϖ',
            'resources': [
                'Ă΄ѽÎΰãUЈ.ҁƯɒӽmӻкXɛѾˏ˄ɲˎǤɵȺʾӂ:ϑ',
                '&ΑƢBӸƗɔӇuӐɄɹȈȸá˗JԎԂtšϺ҇ŕƬƴгǣЂǖ',
                '=ǒċўťHƉĎɲǘΠҩԝĈŏЃ\u038bŰш¶ǹѸŮķԀ˃ƏқΊӫ',
                'ΈΟůÚĕӉгōȑӿыЖ¥҆Ӝ·ψìùȚĨÕъǦӔӢˑ+ǯU',
                'ҡȔӓ.ҪƯ˱ǳԧ¯ʅϹʄüƮíӼ˘іǦϰĹŶ[ˡϊǟD҈\u0380',
                'ӏɊɍCҽŊâƑř\x8aťȜҝŀ\x9c=ƿυȂÞȒεăӷHξŘɆ\u038bЙ',
                'ϽʃěƯĴЋӀӻż)ѶԔƆΐΙωԂDӆˠɏϘҜºÜӱȰÓѼw',
                'ǢϬĴî4Ŧʭ˫Ȟƺɚʱĸ&ķÙɿφ҇ҜƩɿ>˃ȏϤΒÂĚм',
                'œǬȕǢmǨƱɋƈά˥}MӺǰĈŵžϏӪȴӏѤɇ˓ӘÏÉŨԉ',
                '<˜ȣǖƻ¡ȌÍŗ*ˁǅϡ͵ЈйɆКˬǒɥ˫ȒìϙŖ]OԆǋ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ԁ',

            'resources': [
            ],

        },
    ),
]

class LauncherStartExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for LauncherStartExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_START_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionRequestEvent.parse_data(test_data)
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
        for test_name, test_data in LAUNCHER_START_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_START_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherStartExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LauncherStartExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='location', name='LauncherStartExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='runtime', name='LauncherStartExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='send_access', name='LauncherStartExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='permissions', name='LauncherStartExtensionRequestEvent'),
            ),

        ),
    ),

]


LAUNCHER_START_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ίɢɋʛǉѕɺɊл£×ÏŚˊцʊШǊӥɟƚЪԦʳ=ȫđІŴɄ',
            'version': [
                -2209788349890022737,
                -1780960358022824053,
                -7850224374847083289,
            ],
            'location': [
                'ǹЍȇĊŚǝˡû\x9aÂьо\x9bȤΧʝǥƾёÍ·rϬћuÜϣŹǓп',
                'ѮůßŰɍ˫ɺψ˅ˠŦ\u0383үϕЁRȻҨԑ˾žˠƱȇѻя¢уūȠ',
                'ʬȃÒҗԝϏϼœ§Ɂ˭пЍûУѺ\x98ӖǚЁǄƟЌӨңåńůЛȔ',
                '˂ʲКĹЁlƓĳ\x97Ďέ\x99ǸēʃϘңΔΘ\x8d¹М\x87ŘΣλѮϬ Ê',
                'šŝщХĔǋȁʉŗɥßΛŭĸˈОӃήƗϗƵңĲ˜Ȝ˕ʣцʋĳ',
                'ϱʳȮŝƄć»ň3ŶҩΔĥΊӂԙҨљ\x88ÌԁÅō}ɪƄѣʶӘʆ',
                'Ǽ˩ϷɌŜȶţƾGЯ!Ϝ\x85ӤżϳˣҼΌǵІȑѷӛԂɭɷ˲ŚҌ',
                'ȳǅƣōɒЃķʘɺBɏ˧əĹ4џĚĬʣǭҔūҵüǎʁșӝЇc',
                'ϹÜɹĔ_ż9Ԫљƾóαԓȱ˵ɰ\u038d1ϜIіǆԙЕ5ɲϓ\u0381ӎM',
                'ХЦԗÀӅůǢήÕǡԧλǒԏuʬǩӶʏǂ҄§\x9d¬ɫ˶ΛČĲǖ',
            ],
            'runtime': 'ɶ˛Ư\u0378ҁʲȚěқ´ƱɔҁɢϣǈˈҰήÏµ\u038bWӾ~ʼʣԊ¦/',
            'send_access': {
                'event_ids': [
                    'ÝɴśɛŶTш8ħ ƮͼǸӛQɧӿӬĆʝnԠʋΟșͱϓәїĮ',
                    'йϪ˼ѼςԫрŘDªТ˙ķƬЫłXɝʼԁǊt΅',
                    'ȴěÊ\x9d}\x92ðϼϏȺÌhːƾҥǲQȽͱˏęćѐʼϔΫǯĐѺђ',
                    "Ǭǒſ5ĊаҧüĨ'ƼҚĬǘΩũΔӝҦРŎȳȊВѺрŁfŭȑ",
                    '\x90˟ʽīƉ\u0382ŨĖòéǞϥʅȴʩԍϡǑͻӆҔʔș˪Ʌқ˫ӵɰ·',
                    '˄ȷ®/Ӳʕŕʹ6ˍԑĶѺƱыȻĿχ˫ƬΊ°ҫ8ƉˤРʽӁǦ',
                    "ϗƗ˯ǕЯ/ĵ\x8aĦӝ\x95ʦ\x8fӶĬɒŝ'ėŃ\u0378Ҏū\x92ҊϽĈěԛƔ",
                    'ͱǡ˚ƿƉаȟХȌҾЛϥҕӴ\x80ɠӧʊԏҎ҈Ԡɑҳh_ǿźҲe',
                    'У҇ӁώȴūɌїԐƺ-ǯĹуǛŢətˢІўͳеғĀΈĴΆɮř',
                    'з΅Ťiǅ˗ƩϔӛаЊŋБȊΕĵҜ*ԧɀɰəѡђбыАɤ\\Ҹ',
                ],
                'source_id_prefixes': [
                    'ԧьËԈҰԘŽ˾=ïƴˇÚCѣΊϞΏŴƍԊӎɔ¨ǅǭüŽ~H',
                    'йΌʄ˸ăį˩ÀȍҐǦӑ˾˹m˰ƫΪҸҖЂ;ƒ҂ǟԃя˸¹«',
                    'Ǯ0ǵчƸαĸĐРʢұħTJǑԫHɬγͻŬ8˃ĊəʶȻʓ5ˇ',
                    'ƬβǇчɏϏrˏӻªßŌȣȵԟɤĨΝ˟ǍŁřȊsЋԥѮ\x85ȟŲ',
                    'ʮ˧ϝĺ˵ʹӛĊȚºŭí0\x89ӴċζeҚĕɄȮȖӥƎԋ˓ǕɩЫ',
                    'ʇ°ԇҊΰ\u038b˖ʦλik˯I˪ӓʣ³ӃìͷƾɊҁŭŃǌ\x81®Ûƹ',
                    'ȼїϡFŎǈϜƯЦԅӅǎiΣƍǮǘÒΤьӡūʀƘſ˙òшǕα',
                    'ǩðҐưȿѻϿгψӔ·ĊʮǧΆϟȋ7ƣŮĀιӉɎӎ˃ÂԊΣӌ',
                    'ńԎҫȓ\u0380·',
                    'ԥņɌÚԬʱƹʠŏǇ@ˬфќ\u0379\x84ЀњԪLB҆ǚǝԌΆүЃͺȸ',
                ],
            },
            'configuration': 'ѩЗʽģěƄĮ}śшƚ\xadӶϟ\x83μԁʔуņʑąӛŨҖҁ\x95xņЋ',
            'permissions': [
                {
                    'action': 'ǧɏİŨśƜ^ԞӌĿƞȉʜ˒ɼҒÒӒʂęJŞ¤ʺϖσΑȧƏʔ',
                    'resources': [
                            'Ӈàąрƚ*@ӽʏήȌ\u0378ĄΪɄĊ\xa0ѿєʅЎöVXЅ§ƲƓɧό',
                            'ӕпʄ˹μɪяęƊȳê7ϺɴҚЮЩ¼҉РҰʽȂѭйӽҴG\x92\u0379',
                            'Ŭ\x8f\x8bèӌkȾҨȾԛXįưmʳ(Ġϊͻ¬æӗɯϛĒѠџӜО_',
                            'Ƶтǥ\u038bSÖ,з΅ǉћҁ<ͱӃāơԫĭƵϋ˃ÊĈØƂʲΛ´Ǟ',
                            'Έʡȃ«ˑзԌԅЗƛ˜ԕŇλԆȗȱϤ\x85ɗϚÀβ"Нˉҕƫɕʷ',
                            'ŸͿąŵЋΏƭΫРʭхѺȢрЬɯˡ˄ʢ\x89ΰ˝ɇĆԥɭİɤɢω',
                            'ѭibѳɆӄå',
                            'ðĈёΣ˓ζϱӈżήѨǼǃʓ\x8fԞ»μǆʜԚѣȍѮӨԨѿǂơI',
                            'ƨĘ˾СΐԪʚWё˺ΐ~ГăƝɼЌѦоҜʴƇǀɮӟΚɑ˷ɸʪ',
                            '|ǝǀp\x90ϢʰIżѥÖʺÈСК9Ԥ\u0383Ԏ˲ÞҌĜɉƧҷϽ\x8dȕǻ',
                        ],
                },
                {
                    'action': 'ϐǆˤһʙуșȆҤÐrɰűѵĉȳƤӫβԍɺǑKƊӅǺŁѕĶĊ',
                    'resources': [
                            'Чδʅ£»Ȝόͻѫ\x87ǩÀˀƃҭƃȍι\u0380ÄŁӧџƣřҁҖΚѶí',
                            'ËǲήȋѝʑнԁɠԀĐһŸɟŢˌ',
                            'kǴ҉ʽӿRҭѱÖΤ[˖Ӊ˩5ǦƚȃɒϏѨşǧ]ҿ^ʓˀʞϹ',
                            "&˄\x85ŶѲΜʫȢӤϛ¿ŐҶǩĉWι\x98ӏͶ'\x9fѫйǔ\u0382[аЌƒ",
                            '¿ȻϋaЅώ\x81ЗŔɽьžˤ\u03a2ǻԇơ˾Уʄ÷Ĉʔ+҈ǽӟÚΜЙ',
                            'ϰîčŕТʖȉæ҅όӚ\x8dμŜ`µČƼıóʕѳ˹ʯˎƥǩɓŇŴ',
                            'ɵыԦΜχӶó\x83ʁ«Ɠ˱ŽÜҒÈńzӖ˰ʁȤщ˅ı˫ȅԥūς',
                            '8zϡЛƴċɏǙɏïǰʕɲqԔ%ƟʽϹǖĝЖаĊ\x9aęѤcЗU',
                            'ƝɌѴґ0śČÿɘРǵyŹÁTɟ\x97şëXұϩӎЅνʪȐө˔Ϭ',
                            '\x9fǬɻŢЀįΰ\x93ӈȔΞӄƭўǔȄӃŉέɓÔʗЉéŽѾθҍǃ¸',
                        ],
                },
                {
                    'action': "ŰȿÓƱƆσßΐӚӢԊ\\\x9bÛя˒;ɦƢȆħʾȎȳđЋǴ,4'",
                    'resources': [
                            'Ĳ$ŜԪқƵ;Џ҉LȟϷ!ŻԠʬđІѐƪӊӰ\x9fŒ˃ƍĢƐ@Ŝ',
                            'ͺ/xƟˎ¥ν2ªɲÿԀИFȾѽѾѭŊǹɅİƁзÑƀ˻ӧɢŐ',
                            'Ȫƍe8ͶʎӞӵϯǋљ˧ȲϩӾĀКĜȯ¡ǎvЈƇ\x81Ψ}źʸƃ',
                            '˘ϙΨϕ\x7fΘ¼ȹϕȪϬđʹvѡƽ#ȑƙǀӪͼä\x87ƦҢγϟҊ˪',
                            'һЫȥкѸҡзΌ˫ԡJQʛŅɪǚēƁШĨҺʈуǎԓǚuЀτ\u0381',
                            'ȿʐφ÷ɷŜʗʨǈ)Ƽǀ{ǷȀʙԁΗȠˎ¹˶ҠĨ®ьə>¶>',
                            'Ȗ)ɛɖʠѽĹϯά\u0378ėҝѤɗӞƩɃΎ\x87ȝЄӎԘșɞÏҕ+@ʬ',
                            'љӗ7ȎŖǲʕɍţƢÅɓϲɰĈʡѝBɧȬԔáʠϪʙђǀΜ.ú',
                            'эĎÏ^Ԇİ¿ѭŨëʟηƚɜǵӷМҶs(ёdȮɎѰɴʣmѷÄ',
                            'âɬңҠȕɺ\u0383\x84ůʥή±¯ʿ˕ˡˤӺԭʓтϣӦ£ȞǤЭ£Ƴѓ',
                        ],
                },
                {
                    'action': 'Ї\xadŋȒϹ\x94²',
                    'resources': [
                            'әàςϳ5ҾԛӺ«ρѻɟˎɉӪĸмō˴ƍæ\x8cπʹҒȍЉȊʝΗ',
                            'ɑόʕɘ\x8aɽÂĨɲΊ4ɬѵʘĺӞJΩϵ6ѝŊҖNÒόѱʻʷҪ',
                            'Ŷˌ\x88ʙĬ·^ǰӷīХήĳФɯҢѪļσŘȜԢөˤĄРѕȦ½Ĭ',
                            '˳ǙȲыàԩΛƂǨǡȸãʇбˁԊŤӓƙʼGғНξѲUɜɮʑv',
                            'ɷɶҨϪϮ˂ƳЇn\x8bѷôҊʺςXΏҷÈĀ҈ǲӐӳӜAʮ\x92фÀ',
                            'ȴӼ\u0382Ńøʭϲʱ҄έҪŎźHÃХϤО˖іà¬@҄ɢǝǣ¸Ïś',
                            '˙ӘщˬŦʫѹЩǙʤф΅ÍӐѹѥ±ԤǻȞԏЧøʡɋИ\xa0Ȧƾx',
                            '!Ϲ5j°ÂǊ+ˤЇҕǝιɋҕɎЗЈδʻƙʌѥҙǕɥӴżͲӄ',
                            'ɒ°ΈІɢơΑ\x8bϲζß\u0382üΜӑҠǣȬΠЋþϵ\x8dҗԉ"ΌԩƯħ',
                            'Ұ˭.ř\x80ōď8ϲϗΥӦƂTIЫi½ƄίԕŢɁŜǤ˓ǲ҃ɼO',
                        ],
                },
                {
                    'action': '¤ИϛɁ\u0380Ԯņ˜ѯϐ²ҪƯȊWҗtˍӁӧʻȱѯǓӪŗϼѢŊl',
                    'resources': [
                            '\x80ýȡΒȻӷцοwОǆùĕӷǓӁðϖĎΥōԣƊWɸȏȵͶРˣ',
                            'ɂԧҨӨͶ҄ӎʱǄĜJ\x96ˌҺӫҽ΅ΐΑŬҰěǏɘǻѕȀûúӱ',
                            'ųŬϵOϢѬѻɤǨǰĎ2˦αȢɩɢřй¯İ˸.ƯҝKɫҮҵ\x9d',
                            'Ĳ£γƔɌЪǫdͽĜύӟ\\ДЀ\x84ȕԓǘϱtЀΓӃŁ×Àűγ3',
                            'ɧ˭ŐқźϔǱơңţͱǹʳǢˮƖˡԭ]ƨИЎл˟Ñʷʎư˅ƨ',
                            'ǌҬˇӪҤšȬΆϾ°æ\xa0ŤкԤŰӳ%čӺщåƈΟȹǷǵøԤY',
                            'ѠӴŮώ˚ȵØȐĔv+уҀЙȢѝJчØҨɲӍ¨ХзˑņKǊҫ',
                            'ϓ\x98ϭÙżÃȄȥąƛɬȷ°ĢǗąA2ˢȊ¿ŋ?ѬʖƓй˵ƹȉ',
                            'Ԧňԥɔ˱å˥ǓƼ0ХάȪƯҧ\x81ĴΦ/ŞÄƁˁòr\x83ƪƗ¿Ч',
                            'ӁӲÖьǍΚΊÝЕϾϹƅϓƟφ\x91ʏ9ʿ=ʭ\x9cӬԐȁӍɁ˽ӂʻ',
                        ],
                },
                {
                    'action': 'ƗжƆ˴\u0378ɼ˃ˏŪȎÈǥшЯ8ƫɳʿ©\x9aųÿҽǬҌȷü\x80\u0381ŉ',
                    'resources': [
                            'ӿŗɴʵЃ϶ǁ˯æɻŲƚдŨˣ\xa0Ǩ¤ΣÓơĠɫɵʤўPϢʒф',
                            'ӅϸĵҝȦͱÌYŐӛȏӰϷͱɬþΪԗǕǽƠҪһȑȸ{Ӆ҅ϴѠ',
                            'ёƄȽ\x8dÔŵǿȇңäȡҌɽҨԦѹˈѸԜǈbĎôǴЛʏʃőƾŨ',
                            'ϸʇAЏķНӇϵйƌśƷйƆȉʑ¤ϡʻ=рfˉФɖʑȜĵËӞ',
                            'ѯƌΥǔƈəƛĮǒӢŏȋѵ\x93ŨɬшǷҌүѦ˱пĖʑ@\x9cƜԔŠ',
                            '\x8bψ˶_˔ʲйϗĄ҄Τǂ҄ΦчӶɁǚԞcЂ\x9cϢEŅɣԜϭș˶',
                            'ƝʶɔáˠĝʵʎˤǟϷҚ7ȞǗˈãӸҸɽΆƜӺØΨψ¦řȚ:',
                            '|ȺҍƱӾǕēϨұƘȤʀ҆дÒψ¬ɇқğıĎĄǭϟŹуҸыĿ',
                            'ҧЇǧŜÛЂɎВͻȐӑ˃ӡҾӭӰЮӅƘƆОщ҂ȏϫśkQϏӑ',
                            'ԑÅŚũԅӍjɽҼЕŔǌϨöӗӆҽϏƉǜΞƸīˀɶϙšӿŞ\x81',
                        ],
                },
                {
                    'action': 'ҊύӗƘΈ)űʝűΚ>\x98ϲ\u0383ăθҽµŐЛŹэζɭWСtδӋȨ',
                    'resources': [
                            'ʿÄÝԞʏŢǀϮҭʱсņԒ«7ŮҠѲѺʬλѵ\x8fʷ\x83ЬӄˆtЙ',
                            'ɿѧӟƬǹȨťËȱúoϼǍӃxѡɓӨơѺǘ·ҮŻѰjЎsÃȏ',
                            'ǟ[ЖƣȯӅdǹҕ˹ѷ÷ӌϧɯξԌż\u0380ɢȺΐͿ\u0378Ő3)ωΎ3',
                            'ļӻԑʪ«ǚYėȠϒ˪\x80ȰÁ\u0378ǌʛұņǊΊĕТÌTΊĲ\x92Ƣâ',
                            'В˖ĢѻˉǱ˘ƁÈ\x81Ňˢȁϭȹʻ˷ȢĉƪÚ/ЈȲĨʾΆ\x9dҐƘ',
                            'ŸԧμҰˠ)ϓӬɱäŚȁӝ˽ӽƚ$ÃΪ©Ӟûʷ)rϛǔBҟΧ',
                            'ĪɾƇĸӎƕpԧˌыĂȕëýœтǏųǗ>˯ŐѷҹɛěԐǕ:Ǻ',
                            'ӡVѽΓǚ\x91Кʒ˼˾ƦКǃİѳ&ΐәÓԑĻҋͻпƓɧгȦϬŰ',
                            'ӦЄ˥˾ʿуѡңŲǺȶԑȪÜ\x84҉ΝӵƆыȣΠλ]ӲßīϷΖж',
                            'ΗԞɸϡԠϼ\u0382\x9bŖƽĲϹӜîέʀƼфȴċǲɇġȩ{ɊȧѼќό',
                        ],
                },
                {
                    'action': '|\x98ǖȝΒ°ʳѶԛƾһĳΥΊÙȈ*ƘӱÈύκƈ˵Ϭɍјň²ɇ',
                    'resources': [
                            'ŬǸyԐϜσǘŁpϑΠøϟӓ҈ǟ¡ͻčçɾÂġɬрʓ:ҰèŚ',
                            'ǂǎȔ\u038bDχ\x9b}dфǀӅ^ïͼŵ¥ѳԭɳDϫЏȡɬӾɇ§ϒϥ',
                            'ҔÉwӺœȓϡɓ˶ľʘкǛµùӝ¯ԟ`ǓҳӁЍÝӍˉǟ·ңĢ',
                            'ƫÏ«ŀϕ?ѠЂ˄ŒʻġӲQțŃʃoçΆrǊӌßɱĥȔ@ɕԥ',
                            'ФͻěǍЩϥǈ\u0378ѪҾäƄŃĮπϣȾ˟ďнɢхʰǢԗќβѰҧš',
                            'ңπ˂ʹΣ,\u0380ԣ¥ɉǄԜɇВ˔\x86ɮúϴӠлɁ&÷Є¿tRҋԀ',
                            'Ê-ҀÀМϖÉ\x8f\x87μӓɤǔΖдύӍ×/уȒЪҬœԎʦǱԂ¼҅',
                            'ŤƝȲўѬɽ\x93CͺťźxɇФªŬ7\x8cѣĒӋ҅ӬǺĴ£ӸƣҾƑ',
                            'ѺŻŮŦƬӪǅɈɷϱ§рӯʶΜţÚȩáёяԄƟЁїΦ˳ϐņ˲',
                            'Xԑ˺˗ѧǖrĨʣðęјχԠȴňүѵȐs¯ɟͽŦбрăҲ҆\\',
                        ],
                },
                {
                    'action': '\x89ΔX\x85ϺўѴÆ˅ŹФȚȢ/ȑȢϩɶ\u0383ųÃӈßƎJ`ρԬǷɕ',
                    'resources': [
                            'ӝΙόʤϊӪф9ȾūŜ϶ԒƫƱҡņ]ƍĴң҅͵ӇƂүųƩɆȕ',
                            'Ԗ\u0383ɧŰɢ¨]\x84Ίǂòö˹ǄŃӗȍϐΒЦӅӞŧӏϏɖңȣ\x94ʙ',
                            'зɊµÇŧǽВԢQ\x814ǊʹІӔƂ˽ãѤȍ\x92ķЀŲӂӥƑȾİқ',
                            'ɲſЕ˯ԂåʠȹЇǲ҈ȴƵĚQӌĆÿŗ,\u0381lùέ˺ӟɺЎŖ»',
                            'ӕЈȘȡǶΣсvÔϰǕ˜ų»ѾȢ[ϻÉԮϵ˅ǹ¹ͲĜЎѸɂƒ',
                            '=ǣĎ¡ɂԛʝҾʑ˱ʕūȱdȚуƼвϨѺŬӨԨΰǪΫҽΠπÎ',
                            'ҍtƐʥDȓ˂ǛlȰ¤ЇÏʖưʰȋҞѼʢƹ¬ÉѢΆɣÑ3ӝƫ',
                            '!ȊИԥɣҩβϺȱŚŮɨӺʑΣΠĬˇɦƴưɖŚӭɀǣϸS\x88Ǫ',
                            'ɁӦȆϞ˽ϱԜ¼@ɺτȬɞС#ÐȔȵ§˖\x9fԬ¿ɟT\x82șдˊԏ',
                            'Ɗѵǂ\\ӣȡҭŎѼԛ¤ͺгӻΩҽğR˫v!şҁԭ+Ǘ˕\u03a2®Η',
                        ],
                },
                {
                    'action': '˧ũ˱тέҷtԀˤțѿԞĖǃɟɬʴӫǭɿԪЄȅҩɯïƖӃŜɂ',
                    'resources': [
                            'ҧѲ3ѸåƶɩӏˏѶÛϫс@шŸĿ#χŋǇ¸ƘìѯǴóӘˎŶ',
                            'Ѹ¶ͽ˯pʒПσŔÛĪŔÙʕӢЅЕƳ˳ǽѲǗΑĊ˧ĲӆC˨κ',
                            'üΟŞυȀλҒͷŇˀӺэȧӋùƵџˤ˔ɭˣȚƋăÃʒʢ˩ӳȔ',
                            'ӴVǇɫP˶˅КŮɣ9Ǹαđ˗ʸЫȎƟХȺÙȜĴέԄϛМθѡ',
                            'ʾĹΨͳѲͿǨɜʸ˽ǳћ|ʂ´Я˚ɓĝűÄЁɡ¼ԤŤǍξҖЙ',
                            "ȗЉȽԟËęƷϺбȱ҅ʒТƇ˥ȜřЃǮРȒHӞθª΄Ӎɹ'Ř",
                            'ӁɶǋΥƾЧӔɄԅБЅʻ8ӛÿ\x98ζθqӜĉȵǥˤŚ.ĚƄľϑ',
                            'ϢеĞɖӠǗЮʛǣ¦˜ҳȞɚ\x84ҙţπЏʞìɆɽʤҹɂʇïÇʘ',
                            'ѐĳҽ<ñĆšħҗɟɝϹԁ9ê˺ʳϗɨļӓƶã˸ʈƢƬҥҙǀ',
                            'ҟԓÔ°ʀĩWҒŏƕϾɕ¿ҍǳӢÊÀǗ³ƸŃӮĮ²ˏʹĉήN',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʭӈҞ',

            'version': [
                -3136785708446692895,
                -6669300401483904299,
                -8713894511473596631,
            ],

            'location': [
                'Ͻ',
            ],

            'runtime': 'Δ',

            'send_access': {
                'event_ids': [
                ],
                'source_id_prefixes': [
                ],
            },

            'permissions': [
            ],

        },
    ),
]

class LauncherStartExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for LauncherStartExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_START_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionSuccessEvent.parse_data(test_data)
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
        for test_name, test_data in LAUNCHER_START_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_START_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherStartExtensionSuccessEvent'),
            ),

        ),
    ),

]


LAUNCHER_START_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ԏHФάǢΏϒɂŨJ҉ў\u0380ɥ\x7fAɜϗðǹϦőÕͻғФ4±ˢƌ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ŭƐӺ',

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
                res = foreman.MessageArgumentValue.parse_data(test_data)
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
                res = foreman.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ςøŚĳiŰØʻìʑҩӬȴȁӺҲҾĠNǊ\x9aÒьӨÑȈ\x86ͶΊŰ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 9008990298373822168,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 119754.13647731,
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
            '$': '20210212:165048.434977:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ɾϗїc˝ͲĄÄʷԂҵГӹɗ8ԥ\x9eђ#KΒɇΩǦTҷáʎʛ}',
                'ÿƔӂȻ¬mӞYȳoūoØƸӴǑ^Ңγ\x80ҰÈƲKΚПΓǡӳʠ',
                'Ů˄ʬʋ¹Ġ҃ę˫ŠӲ·ѢǸ˓ϡɢƙțƽǧˀŃ7ƵŎϫдČÅ',
                'ӬĈϝĸȷÜӿ˹ˬȩˁŭɭ\x80ΟÌιўӼ#ȆÏýɃ΄ğρŇƨӛ',
                'ȝˋ\x8eҌѵï¹č΅èɧÚѲ\x99˜ºˆʿӀė˘ǣ|ӢF=ѵCҾҼ',
                'ëѰīǶŻϫѺŕȢўrUѻʫȖǉͻǶԢ\x7fТŎŬPǽ˗ɔԑѕw',
                'ĐŪ˭ɚӰʖ\x85ȄψĞȁɶӡӪ\u0381´õʹɁ҄ɰu°ʌʭțʈҲOӑ',
                'ͱ´ӼȞҠ;˨\x9aòѢCǛáŷ½у¬ѩȋӨyӖўZʒ\x9fȻŢʛƗ',
                'є˝ԀɺȠƔж#ǎ\x8bΥӫ҃ϊŚŚԘ˚ӂÞƆśԇá0ǞҺҎÉǀ',
                '9ӹƻŻ˟ɖ΅ҙńŏɽÝÔҥMόӦǈĀLª҄GȌҷǕǪɕɕ\x96',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -7110364152677576278,
                -8233060119818825560,
                -887313674468051342,
                -1406526809025976165,
                8361435518020596766,
                -4206138849360731633,
                -1513130340651941870,
                -1982107797566150657,
                1585466641394726652,
                368109452403177126,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                98174.57544364574,
                -84087.56065294574,
                520402.6284835725,
                56951.81305084695,
                -30220.163849721226,
                692913.9450320039,
                23961.358498200512,
                -9411.413445518367,
                15041.545401390234,
                220177.43910633877,
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
                True,
                False,
                False,
                False,
                True,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210212:165048.435835:+0000',
                '20210212:165048.435848:+0000',
                '20210212:165048.435855:+0000',
                '20210212:165048.435862:+0000',
                '20210212:165048.435867:+0000',
                '20210212:165048.435873:+0000',
                '20210212:165048.435879:+0000',
                '20210212:165048.435885:+0000',
                '20210212:165048.435891:+0000',
                '20210212:165048.435896:+0000',
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
                res = foreman.MessageArgument.parse_data(test_data)
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
                res = foreman.MessageArgument.parse_data(test_data)
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
            'name': 'ǯ;ыüŮКԖӥʓŃ˙ħҟÒʇ\u0382',
            'value': {
                '^': 'float_list',
                '$': [
                    741368.090472481,
                    234499.24726091907,
                    58087.446638881695,
                    432383.62348350533,
                    323027.3730768443,
                    557255.1683401924,
                    949996.4718757602,
                    627171.891796293,
                    456542.4153255818,
                    137278.03773921562,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ɗ',

            'value': {
                '^': 'datetime_list',
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
                res = foreman.LocalizableMessage.parse_data(test_data)
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
                res = foreman.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ʡҏʏɚӣǯԠ¯ӗυǨҐΙˇǼƽҖȷ˙ĵĊ?VĝŊïғкƱ',
            'message': 'ψŘϸĉΊѡԢţϜąŽ*Ǚхˀ"Ͼɣ\xa0x"\x86ѩĠˏԫă9;Ų',
            'arguments': [
                {
                    'name': 'ПĩԨʢ\u0380ʿсϿӷŽѮ\xa0ŏҫǻǷ˸ĢŖԇɌɌ3ζԝЁDŧȰɁ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        False,
                                        True,
                                        True,
                                        True,
                                        True,
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'Ȣν\xa0Ý\x91ҾδƯƏbŒʚɖɲțNҥƒƻȡξǹϯŻ¦Ύ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        794024.7994342634,
                                        51311.824987098196,
                                        997532.9319188378,
                                        896897.3177187287,
                                        754383.3235027189,
                                        928029.4517758265,
                                        708340.3402237995,
                                        2610.4003960802656,
                                        745403.0118885409,
                                        159737.17476739854,
                                    ],
                        },
                },
                {
                    'name': 'ҳλȪҶˡƠ˧ҁpѶˇʆĔƢˍȥÁɌԭ@',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        843503.0192095442,
                                        -54655.01498485801,
                                        418940.7530737127,
                                        678345.3560645826,
                                        752466.1623762964,
                                        42433.80392111832,
                                        631369.6048380368,
                                        117145.33245190553,
                                        771571.9321295565,
                                        146299.86291211096,
                                    ],
                        },
                },
                {
                    'name': 'ǩCȴ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        95250327653973254,
                                        3955794697964117560,
                                        5034999360720862935,
                                        7250969166826285165,
                                        -3908164618647921442,
                                        -2951909972088415028,
                                        5949171422758544370,
                                        166892704729915256,
                                        6461935735024315494,
                                        4862254438102446337,
                                    ],
                        },
                },
                {
                    'name': 'ԪȳÄӟªҤ`ĴŌʤŵI˫ȬЅΉԈCфƉþñ҂ξɡÒ¯ˮɿȌ',
                    'value': {
                            '^': 'int',
                            '$': 6248432878733931803,
                        },
                },
                {
                    'name': 'ΨηʄЩҫʒHʛӐ\x8a1ӂҒɴȡϙӃϋɆŽƩΌυˮѺʬ¨Ȏϼý',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210212:165048.432867:+0000',
                                        '20210212:165048.432916:+0000',
                                        '20210212:165048.432938:+0000',
                                        '20210212:165048.432958:+0000',
                                        '20210212:165048.432975:+0000',
                                        '20210212:165048.432993:+0000',
                                        '20210212:165048.433006:+0000',
                                        '20210212:165048.433019:+0000',
                                        '20210212:165048.433038:+0000',
                                        '20210212:165048.433052:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ŪІҭÍǾǠ˰ԥ\xa0ǰƣѾϴǮԬνϦԏΔȀ\x9cәƓã1',
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
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ԨʫЬǤ',
                    'value': {
                            '^': 'int',
                            '$': 397224035462255821,
                        },
                },
                {
                    'name': 'ϡŶɠж\x95ҨźĠӥőМƢƉϔεӃĐƚώɿƁ¢ȑ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        6202215257139587274,
                                        -8022307925904667770,
                                        6044990826642688635,
                                        5523873068655586954,
                                        6365936743036820911,
                                        -751187952174516214,
                                        1505986271878625595,
                                        -4588938068340540317,
                                        -1074070965841133573,
                                        -1441772315081529807,
                                    ],
                        },
                },
                {
                    'name': 'ҁ˔ƣӤȊǼ%ǡĕɆҫĳUϨ\x93řĨ˂ѴƮŮ˖ƒɔɁYţːƔ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210212:165048.434099:+0000',
                                        '20210212:165048.434116:+0000',
                                        '20210212:165048.434124:+0000',
                                        '20210212:165048.434131:+0000',
                                        '20210212:165048.434137:+0000',
                                        '20210212:165048.434143:+0000',
                                        '20210212:165048.434149:+0000',
                                        '20210212:165048.434154:+0000',
                                        '20210212:165048.434160:+0000',
                                        '20210212:165048.434166:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ԐΖ',

            'message': 'ӗ',

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
                res = foreman.Error.parse_data(test_data)
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
                res = foreman.Error.parse_data(test_data)
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
            'identifier': 'u\x9f˖ŴƹǢƮҴƾϷ;ûŢˉͶТ¿.ȇɗ˨Л\x82œɥԖªȱҏÝ',
            'categories': [
                'file',
                'access-restriction',
                'network',
                'network',
                'internal',
                'network',
                'access-restriction',
                'file',
                'network',
                'os',
            ],
            'source': 'aŵȍЇԃ\u038dӰӖțԗͶМԚσķщ\x98ԥŹɨȤʗͰʿюϯӈħљб',
            'messages': [
                {
                    'catalog': '\u038dĎ˦ϰÙƽҽˈŅʹˎ˽ŞǭХТQκԕ˰į\u0379ќJϽɌθѿĈǃ',
                    'message': 'ӻϚгЕяԥĕɯϧɄņԌȅԟΓżϿȕǭӝ˯ˁˍѝơӺǦǌҪŹ',
                    'arguments': [
                            {
                                        'name': '%ĨˁѴѕΩřκΚ;ʈӁȈ@Ѽу5',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x8cƖưϧӀͼэ¹ӶˍȎ¯Щ&ōҢ˔ΰ˒țѪΕԊʹϗʬӨʹɵƔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.392512:+0000',
                                                                            '20210212:165048.392549:+0000',
                                                                            '20210212:165048.392564:+0000',
                                                                            '20210212:165048.392578:+0000',
                                                                            '20210212:165048.392609:+0000',
                                                                            '20210212:165048.392629:+0000',
                                                                            '20210212:165048.392643:+0000',
                                                                            '20210212:165048.392657:+0000',
                                                                            '20210212:165048.392670:+0000',
                                                                            '20210212:165048.392683:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'zŖў˛ǣ\x9dӸíĩ6ŊǈԢɣ.!\xa0ȖŻɑѿҢɹŬɃŭșӯ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҜżǨѶ˶ēăǡƋķǦȑтɗӓӸȂǯқҫɥȘʆʕԦЗ˂ϥɌԗ',
                    'message': 'Ťý˺ϒĽƥʀĥµ<˖ԦΔŶѣ\x81BЖʞ^ʢԊёӡŉҕύѨӝи',
                    'arguments': [
                            {
                                        'name': 'ͻцdӝúљĚˢ\x88ͰϿ\u0381Ѹϕϋ$ƞҋĳҧʝȮѣӄɏҜ˾4ˢԔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɉōӞǹOĝȖ\u0379Ʉßˌf',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            41881.64895763097,
                                                                            619084.9289610814,
                                                                            938018.7853809941,
                                                                            749675.7049223298,
                                                                            698908.5366640644,
                                                                            786875.3780584728,
                                                                            476121.0933208177,
                                                                            833675.647468153,
                                                                            287046.8395652563,
                                                                            153832.359020731,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˥ǤUʊˎ¼ÆǾΦ϶§ǽϱҶѮѽ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӒУΟјɣԛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.394945:+0000',
                                                    },
                                    },
                            {
                                        'name': "Z'Ʉ",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                            {
                                        'name': 'ʂΦ\x8cҫūδζπӧѶΔȘ©A`ÉğÜвʶҴОз',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.395666:+0000',
                                                                            '20210212:165048.395685:+0000',
                                                                            '20210212:165048.395699:+0000',
                                                                            '20210212:165048.395712:+0000',
                                                                            '20210212:165048.395725:+0000',
                                                                            '20210212:165048.395738:+0000',
                                                                            '20210212:165048.395751:+0000',
                                                                            '20210212:165048.395764:+0000',
                                                                            '20210212:165048.395777:+0000',
                                                                            '20210212:165048.395790:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɽøȦǕ҅Ȕ\x91ǨbƍЗ\x85Âĉѵʎŋӭȗ\x88ȕʇʀЇčϵýŹŎџ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ăʞӏǋˍÝӌϛʷъǘӂҕԩʧʘēȬҖɾŧ\x8fĩĩ˝ΆʌҙǞę',
                                                                            'ƭ*ɼɍЃ)ɗӑ·ŬԖZϫwÓʎƿŖԣҖƄʆ\x8bȿԞ£ŒlF˘',
                                                                            'ЍΙХάԙ\x80ʑʜʎƩǄƵ\x81ҔԋѾҽˀŃİĠǖҁä\x9fʪҵfҞō',
                                                                            'ϵİԐÕ˓ʠ˧ȪнǪɒƶ2ӺńңωΡ˃ʈҶҹҬĢýǊԟĂ§ː',
                                                                            'ŠĊÙGŎǲβаTä{WȸӂӡԜǛрʶǥƈl ƍԙ:ԤÛ˫ϓ',
                                                                            'Ȯ4ΨɤԏԟГԛԖϢГ\x94ˑ˸åȵҘǎÊ҄ÀѥĘϔѤ˩ύιҼ-',
                                                                            'Ƨϳ˸SΈ\x8cѐʌ\x89ƛͰʎЀϡʔʪ͵ˣ˛ŬϿ˚ʧɸʗĸЉκҬč',
                                                                            '˵\x98ЏƐȊǽĒ0іċÎϒԡsρвͳ\u0380΄ǹśɢÏʭϊѲ˸˞ʂę',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŘӠҾÞ˰ǍҦϗĘȸƶƓӏιɬЎҬʥūȓԇ)Â',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2256750310036999360,
                                                                            -2092205191985438791,
                                                                            -2859102491675183142,
                                                                            -7715245478384763874,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ЏŞ˅µӂƭ\x90VɫϼÃѴϙŇʣКǡɵēbΨɐ'xʵΣ\x84Ҫŷʒ",
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ҭǎњ\u0380Єλҕeǆκ˱ͻěɾ˰\xa0ѩɒeȗĝÜԁºԁ ӈЯ˔Ɋ',
                                                    },
                                    },
                            {
                                        'name': 'ǏқȾϺŰ˚σȈŰñƙԄǩʶиąӿψêȐϙφɫƇǺ˪šіӌӒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɁŢͺ+Й˵źhӔԆ·лRѱɠЫɪ^ħТÓˊԈХЙԘŦǒŞǍ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӶӾˑʶρƅ\x85ҒԩžϻϩΉƇϨeƻm¦ҙъѪˈ\x8bȹñΤΨʆć',
                    'message': 'ϻ\x94ĮʟÛȪǘʄԙ˸˳ɉȞɊҐ҂όfɉˍйҷɬЂё\u038bȲȣΙӶ',
                    'arguments': [
                            {
                                        'name': 'ӪҠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.398584:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɭҮǄȋǔʬÜ?ɍ΄0œÖïʣтαʅɄԌÉÕ\xadĬѲɭǇŴŤΚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѐЛɎʭѤɸÇЧε9ƫҙſƫ˅llϒȏʕ˰ǺѨƇêȐÝϊɂ˜',
                                                                            'ȔİρҙoĬPſЛϩͲƲπʯȸģϼι\x99ΪƠ{ĩѩБΛоŎя¿',
                                                                            '\u0378îŭšЇΓʃЧρĩșÆ϶\x8fƹӖάȍ϶ŷĲ\u0380ѮаïɭґҥɃĕ',
                                                                            'ÍѶ\x84ӘƩÁäŬԈ\x88ŨͷœӐԘӼћǳēßȭQԗǯϩğɩ§ɷʨ',
                                                                            'ʲĕ¾ӎSVʏ˫¸ǽϾƳoWУɷҌҀǳѸѫҽǾʿāʩA˞°e',
                                                                            "ƽҁӓԊʸНʍþǠǠˉǸɕΩVԥL҂NѴǡ'ɸп΄Ƽѝ÷èť",
                                                                            'Ҽ\x85ǄπψȬϭơʬϦʸļШӤύ˭Д÷K¹Ќɣ¤9åɒƦɓʔȏ',
                                                                            'ѱfǆϛǍǌ҉²ɉϔâ\x7fЋ˗Ԉ\x95Ňʦ ĦT˶ӻʏŰϳǾτϰʸ',
                                                                            'ьɭáěƅȗϙŌÄ¬ģШҎΏʊϸ¥]ɈȦѢ˩«ʪҷɕСøɅʴ',
                                                                            'Ɯνǵ4ӕɒŕΥуʞΫш=ŢĸÆèԠӼԁʯҊψӷƳƓÉϚҧ,',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0380ɋЕҶˆFϪ\x8aСʖ&јĎôҤΆƝуӷԩűӄӭӗʳȎĬАɴƿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.400051:+0000',
                                                                            '20210212:165048.400087:+0000',
                                                                            '20210212:165048.400103:+0000',
                                                                            '20210212:165048.400117:+0000',
                                                                            '20210212:165048.400131:+0000',
                                                                            '20210212:165048.400145:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӗŎɯɣӦĐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŊҧȲŕȪĸϚ¯їьѪҧʠЎƌökɐӲҥņҷȑǥӅà҇ɠӷʚ',
                                                                            'Ԝҝ®ϡͱİÌʻɛή\x86ÅŝѧΩ˧ыɁйīЬѵϩ˦Ѓƨɚ˝ɾǫ',
                                                                            'rɀЌМîʠ˱ƻзԕβͷԋ\u03a2ѩԖhɴȿʁŲƄ\xa0ӥħ½Δɡ¹Є',
                                                                            'ƗèѽŬɾ\u0379ƇĞҊӋҜǋƲԈ҃ΤŘΧXŃёѶȕҗMǛƋ`ԇÒ',
                                                                            'ǆ˵ˮ˲ЇɹӌǘӼлПѡϸԮѳɞÚЍӦԘʽîɣʠҼűʪυwτ',
                                                                            'όѮ˶ĹІԆʛŶΔόĸƶΎ˟цʘΗűǢʟϱаēå\x9cϹГщӋÒ',
                                                                            'ɇ`ϕȎRɹԮʌγ[ȵʬGĻđ_ʸ˺ĥԌɾћҠʯǸČɇÜԐ˓',
                                                                            'KϖɉМԄȿнˇзʔӏчÁƨʆȯӁǣǸνҵʬȔЊźпgį\x9eԕ',
                                                                            'іĽԇДћϢɲ@Ůźԩ҅Ǖ]¢bʒԢ˸˪ԝϩʄũЕšΗӧό\u0379',
                                                                            'ȵɗͳΟђƟē\x7f´ƞÊɀĳŃʍɊĂϖѷӠ\x82үĕŖúūӴϥίǢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '8ќЭôo҄˽˻˛ȹ@Œΐ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'E҈χƛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            441771.59465691086,
                                                                            259961.91484661488,
                                                                            236237.28558468423,
                                                                            -36419.81332536975,
                                                                            550060.3105958318,
                                                                            964654.1174289768,
                                                                            148352.49421931384,
                                                                            225847.40117114293,
                                                                            322279.1799432818,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԂϿҋђΡщȅŧɂ³ŰɵřӵÖɶŨѸ\\γ³Ĝ«Űâƛԩ\x91ơ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÄѦΐ\x90Ļ\x88ȼєQ¸¹ƯЗĒɁρд\x8aӗëɦQǛʚVɬϣӰʣw',
                                                                            'і\x80Щďʠєŕ1ͶéȆŁɲ¨ɑ\xa0\x97мǇϫʼжɲƘ\x85ɑԟЏɏȱ',
                                                                            'ѡɤї¸]ԛ\x8eȯҩϮѼЉƠÇήÿƨοҘʘíĹҽ§jɷαѣҥҟ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ќ҄ȔˎoˠʦȅͳĤûƶԧʆʪ\x99ƩίöǣӾԤԒĤˏ\x87НЕʚӧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3894504352219471400,
                                                                            -69455999571896436,
                                                                            9078235929192093453,
                                                                            -8526841609332782495,
                                                                            -6401903468525509137,
                                                                            3191506557826620987,
                                                                            8420683452713820435,
                                                                            5413465646766630183,
                                                                            7439203181191988671,
                                                                            3622868366701686158,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɧΊŃ\x95ãǿAˀиȤӯԛŜӳӰȥЄÅòғԒDҁń˹ҦŐԘωϪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.403327:+0000',
                                                                            '20210212:165048.403354:+0000',
                                                                            '20210212:165048.403363:+0000',
                                                                            '20210212:165048.403369:+0000',
                                                                            '20210212:165048.403375:+0000',
                                                                            '20210212:165048.403382:+0000',
                                                                            '20210212:165048.403388:+0000',
                                                                            '20210212:165048.403394:+0000',
                                                                            '20210212:165048.403400:+0000',
                                                                            '20210212:165048.403406:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ηΟї\x8cӑҙЯÿʚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЋōɂН%ŠГҩɐˬҧϳɧ˪ХɫŜ%фϜҦɱρгȟљӰÄƨN',
                    'message': 'ԆԋăˬќτПƴɵƮ/ҍëλЈ˷ñʟµĭɀǷӕЗ+ɦƜʢȟ\x99',
                    'arguments': [
                            {
                                        'name': 'ʨӶ¶ȫǪҗĬ\x99ϭɉʈғɱƿŎǚİģкúǓҔоԫȯĹȟB]ǘ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.404163:+0000',
                                                                            '20210212:165048.404179:+0000',
                                                                            '20210212:165048.404187:+0000',
                                                                            '20210212:165048.404193:+0000',
                                                                            '20210212:165048.404199:+0000',
                                                                            '20210212:165048.404204:+0000',
                                                                            '20210212:165048.404210:+0000',
                                                                            '20210212:165048.404216:+0000',
                                                                            '20210212:165048.404222:+0000',
                                                                            '20210212:165048.404228:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'нs',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 920464.456332065,
                                                    },
                                    },
                            {
                                        'name': 'ƷlĴшӬџDÓ¶ɍŝĚ2ŊԎҌԊӺ÷\x9bǥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.404669:+0000',
                                                                            '20210212:165048.404686:+0000',
                                                                            '20210212:165048.404696:+0000',
                                                                            '20210212:165048.404703:+0000',
                                                                            '20210212:165048.404711:+0000',
                                                                            '20210212:165048.404717:+0000',
                                                                            '20210212:165048.404724:+0000',
                                                                            '20210212:165048.404731:+0000',
                                                                            '20210212:165048.404738:+0000',
                                                                            '20210212:165048.404744:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'şʮë£άȅŏԔσǫѿҮ\x86ǑƐҞ\x7fңрŗӥr',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4382846012353736612,
                                                    },
                                    },
                            {
                                        'name': 'ɋϵɳӧƂԃjȗӨ\u0379',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            224955.80085024837,
                                                                            257715.4130580395,
                                                                            285345.66499073943,
                                                                            96137.46219717778,
                                                                            -12631.904272413274,
                                                                            816982.7057432596,
                                                                            944479.498121085,
                                                                            755954.27009818,
                                                                            -1854.6578435783595,
                                                                            87745.01960994693,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѝҵ҃āʈќˬʞűľц͵ŞøÂã҉Ǉ¾ŭƹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 531973.4463673395,
                                                    },
                                    },
                            {
                                        'name': '¡НҘӘҐbǹ˻ιȋÿ\x8aϲͱºͲˌå',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȭĝvԏ˘ҒԜʲѥ\xadăːǠԅΆœԔȠŮĲǪ*ϸɁЮι1ʘӕС',
                                                                            'ԥ˝ʿɺʤɚ÷˕ð˸ЙWϙʂДĩͰNғĖΟӠȜԩǔûʼ£ҳӅ',
                                                                            '˽Ӯз½Άnruμ҅ƇАЏ\x8fΆҨϻѰÞɌ{ĂϢ^ԮԍԓυϢǛ',
                                                                            'ƜɮFŀԃĖΆћ;Œ¡αƶŪСɖ£œ˙?\x91ɡӚνζJțзPŉ',
                                                                            'ɑǬϰ¿ĔҚ˨ϓѝȢ\x9eŻ˓οȭ¾ȷǒɊԄɻХҠ×HˈпЌ˰L',
                                                                            'ΤҁǟţΦҬǍƃţˑƝĦĕюȷˬȘÃͻȳȾчũȿϦŬŅÏԘ\x94',
                                                                            'ƷƢӲӉĥѳԛӲɩҀνƍӗҦƍѾŨƞʅЭτʛbʱΪϴŦþԒ*',
                                                                            'ΦƘɰΡ\x7fǋáǛȑ˚őųʜˬΞĘȁˮӟɇʆԄɁwԥɦԉ˼Ƞг',
                                                                            'Ȝ\x83ƃηFɩхХǄҭɬŇĦάŚǊӋ~чń2ѬɵˡΜцƧЅǗԩ',
                                                                            'ҰōЪȔԖɑϽœΣMӸԟǍ6¡ҚĩΡåƆΔѯɰѵǜǸǠбԙô',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǛǿȎЬǢҊʾʹΨφА',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.406019:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ļő˱ǶïāǁҀάɞϦǙжѡ¼ƌΡԩǘ\xadѰō\x97ѯ˼\x86ƣїѝÛ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҆ʇІɰƗcǲԏŸɪ>ũΛȇ҆ӿÉІȱţϙĮůðөϭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.406458:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ěʕԤĘɲνŭϘȸ˲˱ĈϵɩǡǜƂӇĲ˧ϨȞɄŇ{ҁ˕ϐ\x80į',
                    'message': 'ʏȾ£ӧ^Ìȳ϶ü˨ȅöÔɽњʩÔџʜʘƧʾǸҥȦ҂ΰʥɣȔ',
                    'arguments': [
                            {
                                        'name': 'ȺЈκȪǖѨγ\x9cџ\x88ΧӄǞŤɡȒ\x9fʏц,ͱˮŌЄўɨʆȚ\x8a¥',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3922125329540503087,
                                                    },
                                    },
                            {
                                        'name': 'ěҘԅ˼ʺ´ĐɆɝϒʞԙ»ÝůͻӞɴ\\ɀȊўQƮōӌɏĺһ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.407093:+0000',
                                                                            '20210212:165048.407107:+0000',
                                                                            '20210212:165048.407116:+0000',
                                                                            '20210212:165048.407124:+0000',
                                                                            '20210212:165048.407131:+0000',
                                                                            '20210212:165048.407138:+0000',
                                                                            '20210212:165048.407144:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÙȼɆʂ҃ɥ÷ƨ\x85ҌџҢÔȚΙƴċȩɋ×Θ>Ƀ˽ȨȃҥʰÈŵ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˇʮă{¸ðǥғɧ\u038bƠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˲>ʆčѤǅϴÎԍМӁĦΌɓȊʻʚɄ˨İ\u0378ЁĦDҠ·ѣǿFʢ',
                                                                            '˭НUή˟ӶHʬȗĒɵʎ\x8dϏ\x85ӸƇΑƷˇάôû9ƩџȊ}њó',
                                                                            'ǎΖӮЦѤӵʹΖěĕνʅʂɠԗӱйѪʓñöʌîƳ\x9eʩ\x96Ύǩɖ',
                                                                            'ǴƔȎƐȈρʨˉГŋĳкÚǴįϜԎЛμӸ¨ÝǐʹȡќпŻű˩',
                                                                            '҂ʖӀζ\x9cƽñ˔ɫЇk2ʌӞ$æѠКғӸ\xadĐВԞÌÎȤƈĪ˳',
                                                                            'ђЮȠʚχǤǂØʟ\x88=ʆɎʖԦǃѤīņȺєżѝЗʢſŊˣҺÀ',
                                                                            ':ŊШ˞ә0ΩϪȌƠǝͽҮĐЖɅүɆ\x852Ѭ\u0381в˵ЪƛÄΏ+ȝ',
                                                                            'кԝϧˇΡўҘљǉƂӶģͳʖ˲źāLϲҽжǍ¾ƛÍđæŦҒ\x93',
                                                                            'θƵǎĆǊǤʟҝǜщƆѲô»Ɩsʸü\x82ɒɄӸŅ~ň˸ěΏӅƗ',
                                                                            'ϺиȞԢльϭɍ\x9avÓԃɺ8ȉÕˀϘGк·\xa0ʅςɯŶŋĖϢȫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x96ɸǣʼԇγаӹЙӪʝɼ¬ѡΚźȹϥƂҶ˘',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.408111:+0000',
                                                                            '20210212:165048.408124:+0000',
                                                                            '20210212:165048.408134:+0000',
                                                                            '20210212:165048.408141:+0000',
                                                                            '20210212:165048.408148:+0000',
                                                                            '20210212:165048.408154:+0000',
                                                                            '20210212:165048.408161:+0000',
                                                                            '20210212:165048.408167:+0000',
                                                                            '20210212:165048.408173:+0000',
                                                                            '20210212:165048.408180:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʞƍӍС',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȫƔӀ҉ӈˇӢτ˵ҵϛĆUҫ+өѾșż˾Ӱ\x97ҫԗĵƜːϬȒƺ',
                                                    },
                                    },
                            {
                                        'name': 'ϽěҌĔR',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -76190.53346278178,
                                                                            577771.7782035976,
                                                                            780226.2093451396,
                                                                            539293.2664652874,
                                                                            567126.4975838809,
                                                                            572549.116843747,
                                                                            666980.9991832435,
                                                                            767352.7561418252,
                                                                            -75127.46181821721,
                                                                            189154.12355615845,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԩ|ɾƮǪӕŲɬZЩʮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4645916891957145570,
                                                                            -2585277700916800616,
                                                                            3266116064741181052,
                                                                            7261979631834863702,
                                                                            5403588026459794436,
                                                                            7059514130738987084,
                                                                            -107718359535979093,
                                                                            8258315533393798262,
                                                                            -2461871321875881023,
                                                                            -939112389782562835,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɼƩѧ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.409099:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѨløcĦΝʍɘãɫңӕӴ\x92;Pʇȶ\x81҂Á˷m·)Ԯxѫɨɏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˀѭЅ\x9cÉϞŷˉэΓŻΫӘŀ²RıʤќˎѥǶŚԁҼŬв҉ӁȾ',
                    'message': 'ɕĬßо½\x8cԡυȵаxƄӛАȄԔŮßHɹϐŲȂύҀȢŝЏǩȆ',
                    'arguments': [
                            {
                                        'name': 'НӁ>ˁʾşΈӍˈʖΰą ԥų˗',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -562623819882526649,
                                                    },
                                    },
                            {
                                        'name': 'ΘғƕƳєԂȼ ĺŊͲʺзʬԜäӮǊƠǅȞ8ȧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5514291504265309387,
                                                    },
                                    },
                            {
                                        'name': 'ŋϥǇȒɏѵÙɹ7ȓƨӤЈÆϣőӽďʬԨOƻGӥƪɑ\x91ϵș',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'γƸ?ƒ˦ƓԥʪӍUÒϴηɚ˜ºЪӴ\x9eˁѹĴӣԮ¨\xa0ҺĻ·ӻ',
                                                                            "ȠϚʖʧǷɗȈф)ˇɄҊǫ·ϡ'ƁƃoҒѶ?ИǿşǇǧȟүÃ",
                                                                            'ÞϾųƦ\x87œθfíȐƉƻ½˔ӼͽǝӹͼʐˣˡŮ\x89ЏҕØʁƋΕ',
                                                                            'ӈέξ\x89эw˷ÏƾБѬ0ͱѵͼҘ´щȶϑ\x8cҷʬΏʫžҡ\x9dˑ˘',
                                                                            'Jο+РѨͺѨǶɫӧēӦȬŎƚƂЏóȵPüǟҥ˅ԣɵŜ1Ļј',
                                                                            '\x9a\x9b˵Έ˶ƠŮĝҝ˳ƭø8ӶƎѣĎҰύ¾Ѥ\x93Ϛцҳɤȭȗ¶Ķ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǝį3ÓǄƢѱŽųЭĠƩąҦʟɽќɵęϋr·ŤRѶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 481046.8867131269,
                                                    },
                                    },
                            {
                                        'name': 'ӧҨɿҠ-ǯçƪ;\x8cȚɯ|ÓӺȸԇĉтͻ ȰԟѽȜԀȠӷ҆¾',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'яǇƔιүЬʹɮƘʂЀ(Уӗčʰ"ġYяΜǪŇƤ®Ɠȁ҄ǒӨ',
                                                                            'ǭΥȜ¨ΌśΉʫ˘JњĴмԁeȬǷĘЫΗH\x9c˼ˇĂϿƅŎĔ҆',
                                                                            "ԂȺƋɶȁʆ2ɏ\xadҼѢüǑрƌŠņɧĠìƙԨ_н'јѰBӆǲ",
                                                                            'ҹҳ!ʳ¬Ү˱έɹƯΉĔEńП\x8fɨȮ˦ÞУ˗Ý\x94ϮƠҲQǺШ',
                                                                            'ƵԉӶѹ§ÕЋʙáɹϨaϑӚѢɎϮԭҙћňϞ&ȾԏϓıĠwv',
                                                                            'ќҪӞҲвΑӝȹǒѬɣɚ~ĕԜΉǝȇɻŸOĻŰ¡"Ұ4ӄ\x8eȒ',
                                                                            '»ӸȎͱаę£ԠіƖ˯ӛ¼ǃŪƺ˒ӐǨ<Җ˜zђiÑЧҘĘȎ',
                                                                            'ѨϒӶҞђċǫȁэξĜˤ"ЦӍʜk\x8cӘΧΝŽξ]ѓӵXԔěϪ',
                                                                            'ʮόҮӨɐĸɑЭ˔IȔѲ\x90αЧǲОӗǬāѦȳчźǴ¿˼ėЕǶ',
                                                                            'ɗҲ;˔UӗǿȅΡºӰƚƳȢíѤĺĭ\x91ážԬǭƇВĘɵӋԣû',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ąį˅ăьϿԕͷΉȻ˛ųώ˓ɳҝôѤʪń\u038bðŞŢХ˥ωɜ±ϲ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8916131242334386087,
                                                    },
                                    },
                            {
                                        'name': 'ˏϥŰɾұ\u038b\x83ρҩƾÙӏϮˀǘƅdʴʵĚψ°˰ã',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '§І!Hʤ\xa0ʙɆʽΧohƝҤɳĢćɃħƿɫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.413436:+0000',
                                                                            '20210212:165048.413464:+0000',
                                                                            '20210212:165048.413473:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ţ/ŠìȊԝ7ǭɷ˖ѢхΩƥȾę˭ԃӭөʅΰˑԊҩˋ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6097979708743815429,
                                                                            -8519757642531965361,
                                                                            -3509676123450325656,
                                                                            5164530972015138156,
                                                                            3221875582367152504,
                                                                            8270738957596975113,
                                                                            5269125945251939447,
                                                                            -2228474091695479441,
                                                                            -8092708938100061229,
                                                                            2530936816602289388,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԠҜѐjƗȳϞˇɊľȎԅ˝фßŦʃϻCΞϑҦΪӝҝӜѷřȈȣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -9101666417758276075,
                                                                            -1986773566816782257,
                                                                            -6040339312602302594,
                                                                            6021255607431708775,
                                                                            491213814416651144,
                                                                            5470566301904124683,
                                                                            -1883038529148420903,
                                                                            674188751672268004,
                                                                            6442770023591678581,
                                                                            -3851934740411803536,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˶҈ǣbˮįãќ³Нč7ɥӶʟȃƒΡȑǧƒǃӽńοŧϳÒөӰ',
                    'message': 'žΐTҐǇӗʉϝȉ^hӘ\x90SǓ\x86ƂqрЙCӎЊƝµ˕ǐҧȉù',
                    'arguments': [
                            {
                                        'name': 'ȪXаäƚǈƃƒёȐțǻɆϋ{чφ˥ϢÂҊZ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.415924:+0000',
                                                                            '20210212:165048.415975:+0000',
                                                                            '20210212:165048.415992:+0000',
                                                                            '20210212:165048.416008:+0000',
                                                                            '20210212:165048.416024:+0000',
                                                                            '20210212:165048.416040:+0000',
                                                                            '20210212:165048.416057:+0000',
                                                                            '20210212:165048.416074:+0000',
                                                                            '20210212:165048.416089:+0000',
                                                                            '20210212:165048.416103:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʀɸȃ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 574437.6817402957,
                                                    },
                                    },
                            {
                                        'name': ';ȣ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.416863:+0000',
                                                                            '20210212:165048.416889:+0000',
                                                                            '20210212:165048.416904:+0000',
                                                                            '20210212:165048.416919:+0000',
                                                                            '20210212:165048.416932:+0000',
                                                                            '20210212:165048.416945:+0000',
                                                                            '20210212:165048.416958:+0000',
                                                                            '20210212:165048.416971:+0000',
                                                                            '20210212:165048.416985:+0000',
                                                                            '20210212:165048.416998:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѕɝʆңƲϭˀақɨɶЭʶԊӐΜ¾ɻż\x9bΖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1530880134487150188,
                                                    },
                                    },
                            {
                                        'name': 'ԃHʷЮ\x880҂ò˜\u038dҋгӮˈӤďѨŀɲμưʡΩΌз҉˰ЈԄԡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȽëӠԛaìÜ\x85ϢŹԖǛʪҥñѕ āϗ\u0379©СˍɇџʨĭЯʚň',
                                                    },
                                    },
                            {
                                        'name': 'Ə˨ʯφѿϴɠ9˕ѽ8gƪΩ«Г',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'bĮ6ǴĩƝʧqʂßЂђưqӗŰĝЀҗŵǳǮʊ˚ĮˁÞѥ.ӧ',
                                                                            'ӊΝԋšҥҤϣƃѸŸԆӚȻ\x8f®ҜUӊѽȔȦ˟ĤƼΠΞÜʆſΒ',
                                                                            'ʱѿɶɯȢŶˋȁĉʄǁƍȷ΅įȺŷĔȅ˳ǌзК˼҅Ğɲʗӓɸ',
                                                                            'ҪґʶԜϮɨ˺ɗÚӧ³śΥʢÍȧ˱ԃǠҦȵĈўϦӌʄ£сǵ¸',
                                                                            'Ú®ΐБŤАҊěӺÛBƈȫ˓ϯ9˸ȃɵɼӨԝË°ҏδƀǪƫԤ',
                                                                            'čлԞΪƕ<ҀǓWƗǞŸĈЁEɽԒ˅ӭԃѻȧ\x93Ӏ\x98ГǻҠnΨ',
                                                                            'ČЯ\x8dμԠǚǬҗ҇łȂǳТǓĽ\x9fȓωu©αȔғzɺ^ĆʏȄƼ',
                                                                            'ϒϻśȹkÌӅӊ\x9e\u0380уżÈ\x94¾ҨÍȽԄǗɬĭԖεӉН˘ÚӼӥ',
                                                                            'ǳ\x92ɭʞɭмϙΏŰģȜǋļʋȫņӣ²Яˤǈ0ȱεóѤρŨӶ\x96',
                                                                            'шôɺʤʴŪȀʪƇ\x9aǙèdϹɧԔϛŠÚǐǃЁСǣğϧʹɉ\x94˅',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѨɞÜϡ¥˱ӥЯӤ\x92',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÙҸλȕɆнſĺԃѣ\x9cŲǇʂwČʧѢŇΘťώƁΡäϙżԛ\x8aȼ',
                                                                            'ә˼҃˅_ƣњϑҨȰƂʰƷȉ½Ѻ4ȕǒ4ıĶäʘȓҲǳDЫʃ',
                                                                            'ʘ҇ǦϟΟµȊʩΒöąÝĜχņǏŔƟԐӄϋǱƯͽʸ}ӓЎӋ[',
                                                                            'ȰÀēïîϪςѐ˻\x84˟˲ЛЊJd¹ϱЦәҩѦћчҖ҇ģȖ]ǳ',
                                                                            'ɣʉ\x99ÉѽѦÀǳÀψҍηƖзҽîИΏϘ×˅ɏďONӑɸҿƦҥ',
                                                                            'ɘοľɉЏҝҕŀҼǽƻǱШïӈƫϵxɲĄ\x90˭əӌ¹ƀѶªь\u038b',
                                                                            'ƊԞЄǅƝŘęϔœβӻŇʕԑīǦ҇ǿĪʃːǓ\x84¸|ҊUɚϺN',
                                                                            '#yɺʕŴLԠӥɾ¾ΌĐΑƫ˶kǭɍɉ\x9f[ӑ"ˀƁtĀȔͼ˵',
                                                                            'ŇɎҨȤǲԍ¥ŻÆǧʆ˱ǈƎ+Χȶ\u0378κǑѤˢȯ%ț(ŷҨʡϣ',
                                                                            'ΪӜҠE\x99ϻǍďӆЬ«Ԛˤһ˨ԜӫÅԨrщͶКИÔεԍԂvè',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0383őˎžÛҺ\u0379×',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.418880:+0000',
                                                                            '20210212:165048.418901:+0000',
                                                                            '20210212:165048.418910:+0000',
                                                                            '20210212:165048.418918:+0000',
                                                                            '20210212:165048.418925:+0000',
                                                                            '20210212:165048.418932:+0000',
                                                                            '20210212:165048.418939:+0000',
                                                                            '20210212:165048.418945:+0000',
                                                                            '20210212:165048.418952:+0000',
                                                                            '20210212:165048.418959:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'τŋǟľ\x85ĞΈ\u03a2ǵӔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            953132.1652199256,
                                                                            624961.9265196357,
                                                                            996427.8708268316,
                                                                            337801.5674318897,
                                                                            802682.8268635088,
                                                                            209593.80697230017,
                                                                            472770.66068701143,
                                                                            279204.5826855905,
                                                                            533554.6413182395,
                                                                            -83481.80783351182,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'NɃ҂äŉΖȿµŚƆɳ˜ĀʟӬʈĿΉôƈʋ˾ĶҵΖ\u0383ùì˖ɚ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 341819.70982635533,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ͽ˭϶ѸӪƆɋґԠȩŁTȟДҾéȱȕҔΫΞǀѥʇӶϾҍ«Ұ\x9a',
                    'message': 'ȟèʓɺȒҍiÝ˾Ϡ˞ʃÚԃӳѣȽƂɎӫƤĔüɁ\x9d}ӋҾ˳ʗ',
                    'arguments': [
                            {
                                        'name': 'γȂγɴŢӛҔίΘȞԧ\x9aƏϒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.419965:+0000',
                                                    },
                                    },
                            {
                                        'name': 'tɠč',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9017012379700551009,
                                                    },
                                    },
                            {
                                        'name': 'ÔĬǴƷȘĒsӦaŁǍěƋʴБѭ-҃ҀXAşЛϤЦʓșBƥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.420340:+0000',
                                                                            '20210212:165048.420356:+0000',
                                                                            '20210212:165048.420363:+0000',
                                                                            '20210212:165048.420370:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƂőϙҐѝΕʢхȮӖć\x90ưͳи©¯҉ųéҽʓĎԙǇюͰďǟӲ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.420584:+0000',
                                                                            '20210212:165048.420595:+0000',
                                                                            '20210212:165048.420602:+0000',
                                                                            '20210212:165048.420608:+0000',
                                                                            '20210212:165048.420614:+0000',
                                                                            '20210212:165048.420620:+0000',
                                                                            '20210212:165048.420626:+0000',
                                                                            '20210212:165048.420632:+0000',
                                                                            '20210212:165048.420638:+0000',
                                                                            '20210212:165048.420643:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӜʊǧŢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -98915.37925960241,
                                                                            272749.7301426623,
                                                                            489054.49863371346,
                                                                            702870.6854393549,
                                                                            844629.927307237,
                                                                            381645.5285317557,
                                                                            760980.9872766584,
                                                                            92.19682493273285,
                                                                            -70340.31033289149,
                                                                            207960.2931914481,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 's<Ɛʨң\x9d\x83ƜéãĘ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.421106:+0000',
                                                                            '20210212:165048.421119:+0000',
                                                                            '20210212:165048.421126:+0000',
                                                                            '20210212:165048.421133:+0000',
                                                                            '20210212:165048.421139:+0000',
                                                                            '20210212:165048.421145:+0000',
                                                                            '20210212:165048.421150:+0000',
                                                                            '20210212:165048.421156:+0000',
                                                                            '20210212:165048.421162:+0000',
                                                                            '20210212:165048.421168:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҖŕԠ˚\x88ƭÑ˔\x8bʬħl˔ŲĜʝ\u0380mĂЙӱÑ\u038dΣȶΝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\u0378čĄиȱGǇӬɻƤӴǀǀӼϲϚϐ»FĩưɛҁûŃDЍèеʾ',
                                                                            '\u0379ӐͲ˲¬јQԐĔmϛeѴ˧İΟЇƗӗȟŤőЄ·ͼBuÐΉƮ',
                                                                            'ƻŭΝǃөmϱťƚÈÞҊµōĎӫŭԪӆΘ˻^įÿȧɹáâ\u0381ҁ',
                                                                            'ǹüæĲĬԑаĭӺόʸȨӻþӎkĦˡαͰȋѱɎ˸˔\x88ҫʭƩϺ',
                                                                            'ѐˣŝđȾǞŸͰ˕9ўϚH¤®ͿѦϋɢҌȕ,ìѲ\x91ѓѣĿʎʎ',
                                                                            'я%cǨʏҙsêϯƻʻñǸ ϝΈӶǲ˃øĆԧɗʝӽĵƘϰȕԐ',
                                                                            'ĘǊӖǧҧͰƀιԢ˔ȷΟѺѿpȐӹ˽ε0½ìȯϺʂˠǏƙɈѼ',
                                                                            'ƪɐɵяВɱɥĪ¢/ӬɯϏȝГΪ˙\\ȞҝНƲΗ+ŽƬ˯˗.ʛ',
                                                                            'ȯƏŹрρƣѵ҂ΈȤǉȤǮŻоϒ\u0379ԦҒŭҺϽ˨ΎͼƄŢБƂҀ',
                                                                            'Ѕd¸ǡѤǉ`ӄȽϨͶғДďˈƇĴˤnœ˘ZʁDǐƽXԍǂŨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x96ήτȓҀÐƽɂоŮ͵ҧǓǊѥ˔1ķ˵ѮƇråǕ\x86ŋ˨İҩƭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŪӿˉĻS˵ƞeɿ\u0379ĦӫʮûХÙˆδˡѽǮŁӷǢԀԁӯѵ^¸',
                                                                            'ōɱʤҝ6ʃ˳ɷёϱȁǙѱǂd8єѵǥ˻ ѼpԏȸӎǑȌ΄Ϳ',
                                                                            'ÚȝgÑÊȓӚ·ťźƯԑѡѧ\x96uҁѳҝӱ¨ӊϧƓ˅ΙöɏҪӓ',
                                                                            'ɈΠѮŀǯѓŨȠłФƢPШȖԆǜҀÇǥȄӇԜςĒŇͻá˛ɍĖ',
                                                                            'Ѧɡԉ2˟ēʨɆʛ\x89џɞϲєOƖ¼ϺŬƲÃЃΥҊȻȳӷĆѱˌ',
                                                                            '˺ҽĴ7ţɪıϓȊХă˚ŗӆWʽͽĈʴνŭ?ǃ+êŤ\x80ϙζϾ',
                                                                            'Ŧ#ɛԒӵ˯˧ǫ˔ӔŽήˇʏĊ9ȔǀŔѾZțŝɪҰ\x95ςѧΣʍ',
                                                                            '˱ӖįǖɾŴǒȬƽ\x81ĤŖΟţϯаԉŎҡʩˢҕіėĨԛäѝ»ĩ',
                                                                            'JϴӥȇɜǛĳ^žЙ¶˯ѼҝπĠŶǢǁ˼ΌɋƲӉςȫŜȝȰҠ',
                                                                            'ʶѱ˵Ҏ~įuŪӆþŲêɁӋwϐħӥùϻΤʟϫõӬԊÖȷӮȇ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'xDѱƅĳƉϨҀuʚѧηәɈϑĠ˟˕ŦűϐȧԜӳƎӬοȅïƜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5708975080207496598,
                                                    },
                                    },
                            {
                                        'name': 'ˁԓͺȬӗӥ*ДшɀÜʂˎƷ˝ԚϐȂƱβӚĨ\x94ʼOў`ȰǺɭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8038447193333205019,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŶΉѾÛԚȝ˒îűµтɗΘЂ¼и˓ʖ>ºΰƫÂRӺ\u0379ȜɔƴӖ',
                    'message': 'ҤʣԙЗʁ˪ċΗЭɐԩ˜ʂӋ\x96Ǹŗ\x86Ġ˰\x8dɀʂЇʜɓҗ\\˃8',
                    'arguments': [
                            {
                                        'name': 'M˖Áȵ\x90ĲĞӇыЍɘĽӃ4ɽԥˈ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.423950:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʠæƭ¢θԐԀʽκĻƘʐĪ˙Ę\x98êĩ|\x8fψ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5086301220159400735,
                                                    },
                                    },
                            {
                                        'name': 'vϜʐ?ǴùαðʗьԚũϢ`ʴŎa\x9bȡċɝ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ӌ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            987531.5669035974,
                                                                            231254.04911314114,
                                                                            221178.51483528188,
                                                                            608062.3063750796,
                                                                            763796.75074341,
                                                                            401113.2503309932,
                                                                            -71388.45331546302,
                                                                            449586.02208806993,
                                                                            -27211.63985619256,
                                                                            147740.07876848592,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӓ®VǎӃɴ÷ɪNƴûɄ˰AïƝԣĦȈӈÅӅÇžØͲƇǄЭѕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.425017:+0000',
                                                                            '20210212:165048.425039:+0000',
                                                                            '20210212:165048.425047:+0000',
                                                                            '20210212:165048.425053:+0000',
                                                                            '20210212:165048.425059:+0000',
                                                                            '20210212:165048.425065:+0000',
                                                                            '20210212:165048.425071:+0000',
                                                                            '20210212:165048.425077:+0000',
                                                                            '20210212:165048.425083:+0000',
                                                                            '20210212:165048.425089:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'γǃƚҫjΩ\x81&\x88ЇϹӣā˭',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -29474.758545339704,
                                                                            535206.4694250048,
                                                                            372204.0449104622,
                                                                            720036.1007442198,
                                                                            428057.8421174963,
                                                                            974705.676856712,
                                                                            238549.5956480261,
                                                                            959414.3577917421,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƯƼƣư\x8eʟҔ\x95ϒ˻ŴһĬӛbΝШԟŶ\x9eǧʹ˵΅ҏΥ\u0383Äţƙ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 386259.80547849846,
                                                    },
                                    },
                            {
                                        'name': 'ȯ\x82ûȱ¢ʫҾ˟˩ȝӯЊ©\x82ѸƔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.425773:+0000',
                                                                            '20210212:165048.425790:+0000',
                                                                            '20210212:165048.425799:+0000',
                                                                            '20210212:165048.425807:+0000',
                                                                            '20210212:165048.425813:+0000',
                                                                            '20210212:165048.425820:+0000',
                                                                            '20210212:165048.425827:+0000',
                                                                            '20210212:165048.425833:+0000',
                                                                            '20210212:165048.425839:+0000',
                                                                            '20210212:165048.425846:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '·ɚӽһƼ+á\x80ɢȯ˪*ЬʌĊώäƕԫѸѬðϳ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8535677863735235809,
                                                                            2982474696857219061,
                                                                            4001506719233338775,
                                                                            -5429855721221465677,
                                                                            2301852820799973262,
                                                                            -213436609475811340,
                                                                            -3681281291224462367,
                                                                            5127434131465304499,
                                                                            -4160176231170259272,
                                                                            126266421505006808,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x85ÄӲӁӈқΛ˲Ƒλ¢Úʿʘӌ\x9f˭Ŀɾӽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ãӞǀΊҗǧƣ\x84ʟΛȳ}äǣ\u038dÅԓёĕďϝКǒЙæɭѴ˶ȡe',
                                                                            "Қ\u0378ʸɵӋγƱѯ\x97ϙѪАMωԘǘ©ЧżɃЧԘѱ'ʹɠŀԝҪ\xa0",
                                                                            'ÃԔηȃЩӶęӴ\x82ӫĔѼɰǷŖҡЁХАԃ҆ŻƎǒ\x84ǉӑүӗ˱',
                                                                            'ȻΏßͻÑƬϣїʵȶĿϏѥεʚԒŸƠԤ$ðʸÛФƠ˥ѹã¸ń',
                                                                            'ӐʎȧÍҝŉŒĽЂɞƩőЍӎťuưϼȶʘŴŰƬƿџɬӤӞīԧ',
                                                                            'u\u0381łͻȫˮӻҟǎ`ͳΥǗϦǀǡΑƬӎƵͼŰʭɘ΄Ǜ=ȿǮӺ',
                                                                            'ΔňøąϭŪǏ©ӲԘíƧтʓ\x93ˑ΅Ƒɸ,\x8aƲҚΥ\x85 ÆӤȼƥ',
                                                                            'ϾŨ\x9dԣΫœҒ˅ľшɒ=υȓѿҚrӏ\x8d°ǡғʔԈLҙŃӬ¥C',
                                                                            'ò\x81ѮɂʶɷōΰʫŔ±ώ\\»üƸŅӡ˓Ĵӽº×Ή^πʈ\u0378Ȋʒ',
                                                                            '΅ƺǔɴÔyɴơÄϫŨɰƺϨĔ>ϖЇІ΅ĘǤӄʤҾʩžҦÀe',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ί\u0381ӰėсϹҶʭшý',
                    'message': 'ʘ΅ʆѝȩģʫɬԓǙÜЎ˘Ơŷ¤Đ˻nʲýή+ƺлЭέѤļ\x82',
                    'arguments': [
                            {
                                        'name': 'Ƌɦʉԫʭ\u03a2\x7fȼǃÂЎӱкƤÝĆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 883895.4913018215,
                                                    },
                                    },
                            {
                                        'name': 'ʞȑԀNϷϣԤѺʰɗ˾',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5712778553619883086,
                                                    },
                                    },
                            {
                                        'name': 'ϱǏѣʳdЛõGÇєʖΣӘԜɠʶxэͽ±Ęǖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȻĴӶKłюƻҕÒӇ,ӱʕƓЯѿğ\u038dВƍ\x8dɺҍϥӵʯ\u0381\u038dLҧ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.427587:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ҩѥ3ζˑʹӤ˭҅ІƃЅƵźԑˊÀʎԂϐ8 ҡ ѠƀƸҭѢɆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            88122.10147390349,
                                                                            331421.83460469905,
                                                                            -97245.43534002568,
                                                                            137571.0156567903,
                                                                            718863.7913000258,
                                                                            59298.59242898115,
                                                                            451024.1735461339,
                                                                            53204.66310347739,
                                                                            872489.7424453483,
                                                                            497048.93822058826,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӈpȭħҏ˖ʈǿӔόǛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1680349732377995082,
                                                                            8406599655090729143,
                                                                            -1771761935709152672,
                                                                            -9097655146669982072,
                                                                            -2419398397099387974,
                                                                            849247509122456967,
                                                                            -2019529533311960727,
                                                                            1245503166291053415,
                                                                            -3969523353920177363,
                                                                            -6093065350025969171,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȏKʣʀʉŢǋȽΧʜɴ8ƤĢ2AœƌʡЁАҙ©ɵͼӡń²˞ñ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 563365.3921842681,
                                                    },
                                    },
                            {
                                        'name': 'ѶƯ°ёЮҝȏзS ?\x85ҖѮɟҌƨΚҴω%*ͳϽIf\x8bɋĆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 800240.683494882,
                                                    },
                                    },
                            {
                                        'name': 'ШǐAӫǊЃEɿȩҡҶѝϹɊȖȟɈȪǖǈ\u0378S½ĸ˄ʃͶʔҵϞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǂӡҮʩĆÄȰΧ4˩ԍǮʴЌėƎ\x8cʥѽԎӵįªʻλԄk3ƴѧ',
                                                    },
                                    },
                            {
                                        'name': 'ɖĹɟҺҴɜϝʙɅʠ˸Ж\x8cǉ\x8bȒˑȌŊАϞје҂\x90ƴʴǵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 294570.03627067065,
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

            'identifier': 'ЫǼŝҙΨ',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'Üɷ',
                    'message': 'ѐ',
                },
            ],

        },
    ),
]

class LauncherStartExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for LauncherStartExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_START_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionFailedEvent.parse_data(test_data)
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
        for test_name, test_data in LAUNCHER_START_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_START_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherStartExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='LauncherStartExtensionFailedEvent'),
            ),

        ),
    ),

]


LAUNCHER_START_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': "ЎϮϚĒΏǯӫF\x80'ǐЙѾҢÒȯ\x96В\u0383ԒĔͻȊɤĭÜʩйӴӻ",
            'error': {
                'identifier': 'əЛFωжäƇԈѨ˲ƢʼЉ3ƻaҙ\xa0ѢȏйӨԥҡϛŝЄ\x82\x98б',
                'categories': [
                    'invalid-user-action',
                    'os',
                    'os',
                    'file',
                    'os',
                    'internal',
                    'network',
                    'os',
                    'file',
                    'access-restriction',
                ],
                'source': 'ϛ¢˔ïıόòƼϤΔʉҚƦ\x80Ԟɡ\x83ӂŉʷʡ',
                'messages': [
                    {
                            'catalog': 'ɧҋѭІɰˣЮɱȸǏЮǉQƻ˦RƭƬӞɂӮȮ;ёwɈȳșÞϐ',
                            'message': '/ϱʖʈĒƽŋT˂ĭˮ\x8fűɓɭοҠ¤ûȴăƹΛYԕҌXѧκϳ',
                            'arguments': [
                                        {
                                                        'name': 'ŹȁҶҬnӇ˒ψǑȞћƃċĚҀӥΚЏ\x88\u038bрƃλӋԮӂТɮˠД',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҕǞʛРІɣfǁѥȀőˠԜǵȞȒêȖǞɿÜoȖ\u0379ŭdƫ\u0381Ԍˎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '}ϩāǦñεý\u038bƁΡϗӸÌĤOȶÁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ğ\x96İԭЫάåɦŦĠŗ˂жļǉГ΄ǠƆȎ\x80ƄҐӨŭӊʡPφĨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƈ˖¤÷˺ǩʘȃǹƃƍǌ҅vяɝªϴˈʱԙҙƙΎŝ˨ѱϠҤΜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԯ^ȢʹʾӎȤӌ\x8dĔЂћĩӧΰŀƂƒǇőǢ<τҠƂϊшĲ\x8aҊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ſЏ¤Йъ"ÃξʇſɆ˫\x97ƨħҗȓmʵǜvȝʵĴ/bӓ©Фɫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЄȺǼ\xad\x9bȈΟhϭɶŨ˶\u0381ȗĉŮӜƔМĳҚѐuɺȳˡƊĵЮҹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÞşʱǠӚȎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 236701.83371523395,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɽК\x84ƓӖǈюɼҔŚøȯӷaӃȥ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'S½ͽƴԊǯѮ˞\x8eɝɞїд\x95ʼѺԒӞŐϠǋɅƩɹœΙҐƼƐϬ',
                            'message': 'ӍТӧJşŒĨҔ£πsĠԧʅĐӷǈ˻ȋÍӮԀҴδ϶χ³\u0381ųѯ',
                            'arguments': [
                                        {
                                                        'name': 'ȆӣɌϟ˵Ȍ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 23505.362579080087,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʪAʉңȖ\u0382ÌԉϱƋŧÎřϡ+Ńϥ˔ԈԑˁȪ/É\u0378ƪ/чEԉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4624577246494749383,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĩЮƌʖɰ?ҩEϣ]\xad/ƗѼƖǀӺǤȨӘƥɊ_˅',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '%ʪÉϊ^\x9a\x8dƂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2419689871065739938,
                                                                        },
                                                    },
                                        {
                                                        'name': 'hϟǍȣɰӪГ¦ǀϩ8ҭŘɗȖǃʅŗ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƁˆЛÕķëƿǛQΝʝʑҿѵz%ԜЬşԀїрÙΫhЮɓ\u03a2ɩŌ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĺ,Ϩ/ʘɄ˸ʱӲѦÀӹĝм',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӄʱԢГѴǑǴãřΧ¸҃ӜƇѫɆ\x97һҵӉΆĖεӭԢʪģϋʪq',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 811641744478856078,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÞđTΌҪѽƏ҅ʘφȭŷ\x84ǩ҈šɖʺ΄',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɑ³ѪˬĚѲťӈĸ˚ЇѺņσ˹Ɓ\x7fѥʳʨєϩ6Ӱ²țµζЪɶ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԝ˹őʻ\x83ˌͽǤә5>ʅȄЏѵ\u0379ϤţЀԭĲǛЈJ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x99ǾΞ\\ϻѪɬԈϐȌ»ϖŮψˍԂҔ˸TͰɃ˟ƵϦǛƶĽʖĔΣ',
                            'message': 'үȬ҇ĔɊіȥƁȆlϦЂÑȊʂη×ѨϏƵԞÏҐɯȳŜʗƕǀƢ',
                            'arguments': [
                                        {
                                                        'name': 'вϦǗÈӑКѵΦԍΊȆ˫͵6ĕ˰пХЛɰǡѶάʏϰȾƪΘίȖ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȻѼЯˤβɯʴʚƉԋΜМ˜ǭƃȐƙˤƜcȇͺɣӭÇÿжˡԨҽ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 816303.1510054012,
                                                                        },
                                                    },
                                        {
                                                        'name': 'УõǣʅБ*ҸЛъ˙ƹ1ѳėʚƧŢеń˝˜ŀʨφŧȹȩǝΘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 952504702069823515,
                                                                        },
                                                    },
                                        {
                                                        'name': 'bɜҹʹб˂ƴҕӧ˳ʕϰ҄пԡѣ\x93ħ;|ƘNłÂðžҟΣŁµ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 798092.457759501,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ķиÞĮÜǙĿ&˓ǘҮưiêӶˊģʗpі,ĥӓҺļȲ\x92ĩƀj',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˩®˂˫Ҵiԧ˟ϲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': "ǏȸӘϥԉ\u0378ͽɀÑĻ\x80˟ʖќ\x8dåДҋ¹ÊӹΙ\x96|Ҍ'Ʒ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 300024.72804934776,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӆ\x96ïó˂\x89\x88´¤łӁǊȹ|Ԙ\x90φGӢåЏˬҲӽ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȔˢЈßОɗЩɕκҰŘ`ǨʸhüĪ¨ǴǬѺˢź',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.368656:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԬҮĐѧƁҽƢԓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʭο˯ÆˡЈÍI˼˙Ȓγ¿҈Э[҅ʀ-ƵӛŇʑʂůԩƚҥ˹ϫ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ѐԉŕ҅ˉˌϱӑѫԖʥ&ȁăΣƊ¯ƹŤȣɝ\x85˧ŖȾĊŴŃTύ',
                            'message': 'ȂмӹӘРԂŤъʎϫϑУĶϠIѽσùæˆĉЖÛϪW¼.ӑĝ˥',
                            'arguments': [
                                        {
                                                        'name': 'ǵåÏѧϰÔʭǤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƄȦϴÍьʳĨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϣҌЮ)ʐ˫ГȸǬ˲ĤɱȔыҳɑǌĸӤĽːșʗ\u038d¢ӤӈƢ/V',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4116859647615955793,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӳўĒŅԞÏӯϕϐϾїǤǰh\x93VҾʿрŻƁԨƉвӍӢƸd9Ē',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϝѣ˭їäƈyǔӥʳ\x8e˘ΜMŒПҚӠ˶ӷŚˢ®ˢõϼŹȝϲι',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6086857977933939972,
                                                                        },
                                                    },
                                        {
                                                        'name': '˭¿CȭҙŁѫΪƵŔɯˑÍ9ԭγѦÐΌЌɄˤĈѻȌϳɓȵΕΌ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊ\u0381W˩ѦԨǲҚЉΑͻ_ɵǯƬҨèԊ\x81ĈҒŖˀԢ҈Ĵ҈\x8dȇП',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 936366.0180567214,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Àýɖ҅ͿÐǼ§тӺȈʫϘӰтƟţ)˷ΔЁ,AƹλƅӸĵı',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ðȻd\xadәƂΝ˫ǮJΉӐʊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '?þǄƩѰĽʮƺ\x9d)\x88ǱȯϋǙӶƵʯtȸdЎ¾ϗВӶșѮĎƩ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӴàϜӓŮɍȜѵeԢ\u0383ƜɢǜǼӫˆΨǟ\x8bԋ£άчøƎƳgЉԮ',
                            'message': 'ΦȆœh˧҂,ǇɌĔiˣǦ΄ΣäÙϖȗϊлƑɎDѯӛϫèϏ˲',
                            'arguments': [
                                        {
                                                        'name': 'vӞŘˈиͱӗêѼżďӆѳǻΖʷϘƭВǺІώwȈɄa3өӉȹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƫŲԥʜћ\u038dGƉϬŏӥχĹÓʥΊɠӒǡϱУŌFĴî¥αȄżҚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'yЧ?Ŕúʡ҇ƇϰΤȴ!ΖʸǾ×ϕĲAȎȑԩһʸxԚƟ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЮĴą˅ɘԭÿѭҫƜńΰӘҿƪҫӓεӣɝˀƽȂȜԮфƞȩĪП',
                            'message': "ѣɺνԥŎĨ«Ƙǁ'ň˺ůȅ\x98\x9aʂӾħ@īЫëĒĤɿƉʎĝ>",
                            'arguments': [
                                        {
                                                        'name': 'ӖԉɞSϭӜćżӵǹԤɡƯ\x97\x89ԝZƺϮȹЁƧэéҖ\x86ѵèʶӞ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǿǳΓΎѤű҄ˊʹӿԃÿŗ³ʹӐ҂úţǦĶэͻȮҁǷƳʢӾӜ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӱîƳΙ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɮǣўϤƃʚȘӴԔņδηө6ʦі¾ƪÓЈͻ˛рˎ\x98ЀĈŘӏĕ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѮӜͷдɾìҺʝȟųũе`\x94ʋɫēǃԕȾț"řԓѐЊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ńĨƔϦӫχҺӳȕҋЍԪɒȦɲ\x92ŢǁĢӬāŊ\x9aҟʳШ˻Ҧҵа',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ќ\x99Хȅ\u0381єĉȞWÔɳ҆ʩʷ˻ǰzƖ\x90đΝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ZӾȰ˗IõɗϑӾȆІ˛ӪƽȨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟңΝʌЃΣʾƋɏӱǣɛ9ʖӯӑŤԊBӴŁӣ҇ĨƅÊԫġŮԕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x96Є´ĒaӢӷԗȗȺѩѠʑÿĒŲͿҵƣ\x89ęзŦȪ\x8cԧҞϱΕf',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -780794107422870447,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴʾƵϭӛǘˁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ͻίȴ\x81ЯźϻǻƨƁӷŊҏAъӠˬ´WƭȼɄǒȽқ«Ǎɝʾ\x8c',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "˯ðӪʠβҹ\x8cҒΙƁϒʑΨԈˡҐƭƸúζ\x98äĬ'Ưɐ\x7fвЉȜ",
                            'message': 'ƤʷƘ.ǁƥªлˉϛ˻ɡ8ђͼ=ŵŜʠȇɮcӝԊΓʠΔʤ\xa0\x84',
                            'arguments': [
                                        {
                                                        'name': 'ɧǷӠŸΓԍǄΪȒ;ԜθҋϧҜȊѧŜŨɛ˄ԇJȽҬӠ\x8e`έǳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƱºªЋӒĥóˀ¸ˮ]ͱ³Н',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æ\x9ačƎУԎɞǨġΡř´ƚӧӈЖьǲɶԌЈ˂˥ƸϱҊӾҐϙʞ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'MҾĭʇɭύ2ƔʈìȶȸÄėǯұнԋȮ)Ԅҍ.ʚŚПǻ˃ҫҫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ';\x94ʶĊʁəɒ҄ҙϕҚŧӭŗϧХѵĖȆȼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.378031:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȓȋ˨ЩɈǘӈȡҡÁŠsʩ˹ʸːҰȵl\\˅\x9eɉȽЎǎпƶΦҾ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ȱ4рΫӪІf\x97ȬԄαzӂ.ƞǁÕȵȓ\x9eßѶÝōβ҇\x9aƨ˃b',
                                                                        },
                                                    },
                                        {
                                                        'name': '£ʖѬё·ˮоmњЮǹϷӒĥĸʷΤѤòėˡϐ§ϞуҞW˼ԒǨ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȻҞɒƖҮҗԁƺ҃λSȬǪʂ\x9fĒzΑɚŶȘԐΎҒͰӟӞώʯϲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6903038811164762909,
                                                                        },
                                                    },
                                        {
                                                        'name': '^˅ƪřӤŐΏ\x9dġĜѕƠЁԬЗĶϥͰρȮǛzΚԉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϓȓϘΦэ\x80ϼ¸ƸЎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŏɾѴԃȂůòlѰԙɾăʣǓȠǤ˅\x87ϼгȥăʅ¡φ˼ʙĀӀƂ',
                            'message': 'ҏρͱȼԪοҪÓȘҿɱ64ӷȁµЫΓçβрŌ˗ѾʍȂĤ˄Мʙ',
                            'arguments': [
                                        {
                                                        'name': 'ơŷ\x83êǜҎŀĆEƩήlΠ\x8cѕ×ȱțѰΠΖǆǀʡƍˏƜ?fϪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃˏҊɖƊʨ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '϶ǋīԩɐŝɣƽHáiƢвǒө6ЧƱǒUŧӰѺϷ϶ɭЬңƨŷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹ\x9eгiѷƔŲѽǢѫB¬νǱҎуԇ˜Д¼QȅIĝFȥĭ¥ьυ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˺ƺҹƵƼұTŭɚĵ˕ӭǼľǽ˖Äʩ˛ȷƻЇйфL|˾.пѿ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'o¢ԩфŞ˦ɗϠВ\u038dԋSˊŀηԜˀǙҵ§ȵƧʀʊ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.380151:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˍҘMЌҲʁЙӱŽ"ƟѣӬĖŐϕѤԩєѝϋɮIѴШčɥŘǴÞ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 18715.909937717224,
                                                                        },
                                                    },
                                        {
                                                        'name': ']ϻԒłVàŗçί',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'µѻľˡʭѺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĦûɘXˊԘ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 466562.45195674396,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʆß˝ȎЙ?ÇҗʲʽͿƵϓѩϔƕōɑ\x97ҀÑ£ƲƇ~Ѫûȵөϓ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƌȑȷ˘˓˶ǐǦѽ@ě¸ʧɄʽǠΓǆЪƅɌʁФĺʁФǅҲ\x97І',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĭȂ1\x80Ή·ƒ<ӫȞƫ¯ҀǳɓҔʁϊԐѮЅȲĠĴϤɛʿ¯GÚ',
                            'message': '\x8aƼοʼīͿʚԀʉЫΈ˥ƌȦԓɢřӔ½їԢΙʺӾ¤ѾІŶȆя',
                            'arguments': [
                                        {
                                                        'name': 'ҴɎšҊҞԩǍϢ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.383506:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɪĘˉÍ÷ȃɨђŵGκɳÊńȏИɑÙѠӹӮʉϴЭŵӛǠǓˇÚ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5227543141703398153,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҿԝêг\x89ɲȹâтӝШұɤϣҌѰȭкΞąĻ\x93ʿ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '0ńʉʒԋʅûBʣʜu8ŮɈ˃ȿ˵ƏӒƏʡԠȍˑҭįϛͳӘϺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȓ\\ҮњӘĢ¹4˩ӥȳʼЇũʹȱБśƕTûˆΐҚ\x8eưûѝ˭Ͳ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѥ\x95ŊϱķПϨˎ˺ƂĴёÉǤѭʳőґԠɐрΎ½ӿȼɞ\x86ȨǃӰ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\xadɤδı7ϋ\x85ԑ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'тԮɺėƩȹȟтϴʞ\x81ĄĳżǸˊξѾύģлWѨǻ\x82ǰӽʤƤś',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѵ\x91ãǬŕǘҼƄʇȈԢʣĺTӢəȉʆ¤ӭƤͰȮĨtғ§ЁҝƖ',
                            'message': 'ҳЁȩЦȮƭƏѩҵƃΑÛ\x87\xa0ҖˏťķɔŏЀΫȰɝǖѡ\\˜ёѨ',
                            'arguments': [
                                        {
                                                        'name': 'ӖЌƨ¸ҹҨ˳ˇɢҋԈƖѿѵǉɳˈànÉǱӢŋ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.386028:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɩ˲[G˝Ŀѧƒ\x88ǭɌǴĮӫԍ˪ ϔİԇȘҚȼ΅Ӄˬ˾sĉѼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ' ȺӗȑѶ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5069421767688098694,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҫʼƌҊӒ˯ƻӳǌϣ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˸ɐѳ˫áȷ˾ˣ½ѯα7',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѝŪǎ\x87cЦ˕ŞΙƛюƉǨčɖɹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.387445:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x93§ÀLīΣö',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǵӻϲЊԠ>ƨXқŤԨʿҹиԝtŮúѽϖ@Ѷ˄ǆ9έŬ£Áŉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 't<϶ÑѧȊ˟ѫѦЙϪň',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ťΙͷʌĢŗЭˁͰˏƜ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 760381.0145722466,
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

            'name': 'Ʈʪȟ',

            'error': {
                'identifier': 'ʷɚԝʾͺ',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'ɖɜ',
                            'message': 'ӭ',
                        },
                ],
            },

        },
    ),
]

class EventTargetTest(unittest.TestCase):
    """
    Tests for EventTarget
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENT_TARGET_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.EventTarget.parse_data(test_data)
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
        for test_name, test_data in EVENT_TARGET_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.EventTarget.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENT_TARGET_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


EVENT_TARGET_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'ŠʷԃǉΌ҇ȚѫđªӚßɴїȵЃŏȶΠ˛ɕґä҇ĞɩѸĀӉΠ',
            'target_id': 'ɮǚźŚСeφδάɒˍǏřƏʲ˃ɟ\x8cȚъʌƪɽ`ʰȷЂįΏɔ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

        },
    ),
]

class ExtensionAddEventListenerEventTest(unittest.TestCase):
    """
    Tests for ExtensionAddEventListenerEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_ADD_EVENT_LISTENER_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionAddEventListenerEvent.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_ADD_EVENT_LISTENER_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionAddEventListenerEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_ADD_EVENT_LISTENER_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='ExtensionAddEventListenerEvent'),
            ),

        ),
    ),

]


EXTENSION_ADD_EVENT_LISTENER_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'event_id': '҉ĞԜɪңįӪƗʑБȋÎǭªʺÿ\x7fˋƙϣηҘԨєԧ£Ӣƺ¸ʷ',
                    'target_id': 'ГğƯјѦӨ\x90Ȕ˄kȮʻɔψ˘ψɊňĶѩ\x9cŀӵˢŁūŏ˴у˃',
                },
                {
                    'event_id': 'ɀʙŵ\x9e˸8ԘƘӎ\x81˷ðӢѶŀÔӥÂ˫õ½ΟĔ˵ɪАƅÕιʁ',
                    'target_id': 'ʘӋʵɮÈέX˵ӷӺŁŲʧҶĤÓƎӶ¸ɖ!УЇΓŝύÉđϾ;',
                },
                {
                    'event_id': 'ˡŨёӗѠƟŔʝЧҧԓïϽӷʁ\x90ӀǷÃң',
                    'target_id': 'ϊ(ÏƽˤƍѽΕŘӈҲє(gȳͻȼ£ҵɱȼϯ˾"ҌÊƔҵԤʼ',
                },
                {
                    'event_id': "ԐŴθǬ˸ӭŻ\x84\x89\x85'ӅӅ\x8eͶѥӶΣ҅¸T\x96åё҃ǆȹСΈȻ",
                    'target_id': 'ǖҽФϢ[ҪЦҷӀӠ«ӳΘъƃ˲m˂Ϧѡύӱї҅ȏӬăϑгŒ',
                },
                {
                    'event_id': '9ǤȫҡѯӷЪд«ϷσȝʢƻŇXȅҜŭǀɁΧɔӇ2ʑӅ\x99Ęŕ',
                    'target_id': '¦ƥ§ҡ¤ɏȘЙҪЩkԏÊȡŖҍԑѺҟˡϒШϔèѼǴ];ËŞ',
                },
                {
                    'event_id': 'Ԁ,ΠŹñĀс4ŁЌіţɘ˻&ŕƞФâʯ#ÔӁèʆ˩ƩӱǜѼ',
                    'target_id': 'ţДȨȤ\x95҅ӉПPȄƖѿȅ³ѢϐΠԬÏДˊĖʤɎɌġҬєŊЫ',
                },
                {
                    'event_id': 'KӅ΄ǌńΓͿӶ£ӎ\x9eωǦςρԗѐüřљԣɛʢțȻˈɁʜÍƣ',
                    'target_id': '˭èԓƓʁȻȘԣ˛eКĝ˙˸ГԨǴѴ\x99ѶˆԚϨ¬ЃϥǴĉ\x91ц',
                },
                {
                    'event_id': 'ʒʫŉϦԛǧſӜҧ&ɁŗL¥ņӘБүϊʕ\xa0ƁҼФ\x8dҤЮȎʩɧ',
                    'target_id': 'Nѣ˧ϷҞǍФϻχЩъѨяɘ3фIėяʳ\x89ўńϱɤOÂШ˒ƒ',
                },
                {
                    'event_id': 'ҎǇ\x99ǖ˄ҵuǟȐɫȧĞԐė¸3ӕvǮNɝǵɈɊùŭ˚ìKƆ',
                    'target_id': 'Тϖ˧ќ%˓ʊÔǡҾԥfūʷzöǇƫ˘jʩùѹ"ͳħӦНØҵ',
                },
                {
                    'event_id': '¾ΞϐˏјԄPϦĈƍѦӖŸȜԧҩзįщӕӺӮŨßˊŷEĭƝԅ',
                    'target_id': '~ǂtǆӇσɤц\u0378ǝș\u0379Ӳͽȧө˕ԡ҈ǯҝɄŀΉ\x8aϪΘɪЂЈ',
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

class ExtensionRemoveEventListenerEventTest(unittest.TestCase):
    """
    Tests for ExtensionRemoveEventListenerEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_REMOVE_EVENT_LISTENER_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionRemoveEventListenerEvent.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_REMOVE_EVENT_LISTENER_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionRemoveEventListenerEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_REMOVE_EVENT_LISTENER_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='ExtensionRemoveEventListenerEvent'),
            ),

        ),
    ),

]


EXTENSION_REMOVE_EVENT_LISTENER_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'event_id': 'ωфήĹP\x9břϐԎϙΞЋūӮƆƭþԩŗʺĖǌĬјЧ˷хϔ˪Ӹ',
                    'target_id': 'MώҦϢϢӌ6Ф҂ϋq<ȯYơƋċɿ҂¢у҄Ίøеɍ<ʮѥӎ',
                },
                {
                    'event_id': 'έȱȪʨϩѬĤЕ¢\x98ʂѝÒöǨώÅԚҒб+ҳǦôόьҶCȽш',
                    'target_id': 'ǘʲ§М`ģǴɽȺ\x8dхƽbþԨә˪Āӄ˾cɆӬưɻxȴàżc',
                },
                {
                    'event_id': 'ӚЖΞɜ£ӶʹйŮɁǫӻʆĦɁнŝ>ҎȻқѝ΄ĥԦϻ˾ϛΪɍ',
                    'target_id': '\x8aĿǶĉïɰʆѭԭϾĶιʹÀŉƲӤŽȾϴΝ\x89ɒőˆŭjԓřӡ',
                },
                {
                    'event_id': 'ǱǩAѓϽʲνѴòѦɡǠԝв\x90҄Ы˫ʀȣɒˀκ<ς\x9cțɤԭ1',
                    'target_id': 'ƒΈȖїʐđɟɀҋĄÞԫš>АӖȱӢϴb\u0379ƁχќԁĬʉ·ǉҗ',
                },
                {
                    'event_id': 'џԂ)ӐɓřԩϲŧüŭŅʘ\u0380ǧɏ˻ȗʻȒºɛƲˈΩǳӅъӯ˓',
                    'target_id': 'Ϧѹ҉ÇʕıÕʺ˗β˲ŝϺϕøɺҗɨ&ӚÕʪЫԈĽǁʃ˙Ȇå',
                },
                {
                    'event_id': '\x8cΕ˴\x83Ґ\xa0ˏĿʸԏƨΣӀʀΑѼǫɧǷ\x93ͿȘʛÀѼâżžіī',
                    'target_id': 'Ũ˅ҽӟƒǀʞÙĀԛeĶΝȅÎĢÝŁ- Ħˀӵѵő\x8eӛӟ½ê',
                },
                {
                    'event_id': 'ҫĖɞяʙqϩ҂\x9cŝΩǈίɂԀґѡǒƙӾˑ\u0383ȳˤ\x95čȣƳɅİ',
                    'target_id': "Α'ɤL0ȑҬΰӰҙɔʜʍӭӟʬıϗчяҙќ\x9eԠśЂʭ˨ӱ¶",
                },
                {
                    'event_id': 'ҶȥÝѰϽɬtʼɿʩӚҮȉʑǽƛǒſƤǑӆɷˍLҡȤЃȨ\u0379\u038b',
                    'target_id': 'ƀӫɑӚŁ\x86\x85hƠȩϚǾΆC҃\x88ҊĆñοӠzδĄћώͽѽă*',
                },
                {
                    'event_id': 'ȣěӽȤѿʄǟ¤ɡШƵʢӉǽԧƚϼĎÞԡЫʐȪ˲ˉ&p҆ѝˎ',
                    'target_id': 'ʯɨĬχώұҔƠɜЭȂɒѫ{ЩԭԎƃҞϫѝҁƷȱӝǸΣϑӊ˾',
                },
                {
                    'event_id': 'ʊϽϰж\x96сϚεҋͷƴ\x9eћĎщβƳnƘŌԧӎɽБʉԛȳӫӛȱ',
                    'target_id': 'ҳũʚ˴˒ϪϿѸȞsҠ·ЦLѢ±ɞԤϹʼԚҦcˬũɘƃƝҙɭ',
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

class RestartEventTest(unittest.TestCase):
    """
    Tests for RestartEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in RESTART_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.RestartEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


RESTART_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]

class StopEventTest(unittest.TestCase):
    """
    Tests for StopEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in STOP_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StopEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STOP_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]
