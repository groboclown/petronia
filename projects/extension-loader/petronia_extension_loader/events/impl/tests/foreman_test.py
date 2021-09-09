# GENERATED CODE - DO NOT MODIFY

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
                'ЫҤȴtӈεӎȀîНϮ¸NƿŲ»ȐӂϪŢѤӇʜŤʱđԦԬҽ°',
                'ƗŔøŖˇʺѼκǼÿïǿѶϰɵıҧΎěċʚƒȏˋɂ¦ʏŨ\x95Ӌ',
                'cÙÙ\u0378Ȣӓ\x89Ҍ҇Ïƀ\xa0ҩήŵʮǆЅȅKζ˴ɉ\x8cϤǸй\u0379\x96>',
                'ѨЧԫθ˒TÂʵ\x96ǨǹңǠЊ\u0378ѝω£ʺɢԟǼҋºƆяɪϓ\u0380ɰ',
                'Ρ\xad˕%Ĥ΄γНÆƙɜǁͺƶƀ^òɈȉʪԁǲǯλҤƩ˶ӟĈӴ',
                ';ϸǌïǬ\x99˗ӈŐМԦɊε˟ʌō¨ϊ7ɕȀкЕèʀºɪȅèϝ',
                'ӕԎη˴ÉŏǱȊʿǚĢ²ӦӷȝʀΫӑʛŷŮɟѾЃ¢ƆӺÂʅɎ',
                'ǣҡĮʴɈr˅˼˧)ҹчɿĢɧѧϐˡХϹӄʙś.џϵɞɥϩü',
                'ŐЋ¨ĝɐ˶ÍӷŮƗu·ҁԡӟ¢ɠġƏчħÿɦïīɐĵҺ¯Β',
                'ǙВύžǻăМјŋɹЂUŹϡѷǉώҎѾяɱϗҼүÕзʌҤӜβ',
            ],
            'source_id_prefixes': [
                '˲]ƀԟЧYх\x99ѾϗХʁ',
                'Ҵ҄ǵȿlȮ˙іњ҆ʜ˙4>ԫͺŪ3ʣӫҶҬĔҲсӷƍϕӦѫ',
                'ϧј·ҥǔ7ǝɦīČřяɧʹƜң҉ѥuҙd¬ҏ+ɴԝԤ\x91°å',
                'ԧӪɔĂÏρ˅ƉғҁФǮȈȔK6ӃōԅO\x97øąԆˣ˷ҢĖҭϬ',
                '\x88ҤƯԟΜР\x9fѥыҶǖƦŧˈɐſƫҧҹԍɵ\x89ΙqѭѼўˣĨЬ',
                'Êȥ˷ɵƗȯǃ˙ΑȍΌǐ§Ēӆʐ\x9bԁƳøMǼŅѽ®ϠƸ2ʩǜ',
                'ƣӪŒɻǒńǖƘϚѦŃÇ˔þўȦɨҹҨȽδӺҾ@cιƶɿɕϳ',
                'ͿќЌБԗøѽƃкʢʛʐħ\x8fӟоŔË|E\x9bԙzsѱѠĖҋYԉ',
                'ԚҩȐ©ŻŸʅ˵ϏˣΝiƦȧȆǮϑČ\u0382§VѾȲÓųéȢĔИн',
                'ϖϵȸг\xadŤѱκ2њDӝԭȾÙλ˂ȥōӑΠʹ\x8cpЀ¼ýӡ<ʙ',
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
            'action': 'ԚхеďїĤTѓЂѱіәöƂʔž҉ȓˑτŕȭɆӢʐ~βwωϔ',
            'resources': [
                'ƩʧьK\x98ƚӠӤȰǿʃœñѮɔȬӈƥ¸ŇÈ˽ѾˠѿƈƘӖ\x8cґ',
                'Иɑ<¥Ƨǰ\xadºϦɗ˽ԒӇҮƠɎɀρǫпӔǐӫԧνDήХωϼ',
                'ԭѥɞВΛǷΦ˵ĊϑǱ˙ƎӁĢӐРʱς҄:Ȯ»ʉҨmѓűϻЌ',
                'ı\xa08ȅέζɤɦқͰxЙͶùѭSѣÞĆέȄȣ˦ƷgήƀΨгǼ',
                'ҩРCŜƕİǸ¢\x91Ӈ¦ѶèȩϴGȣ\x92ȽɼѹԂÁɁɌėПžԆı',
                '˨ӕΪƩϡЏΘԬðȊ˚ƬӤ3řϻȅОǆŇϩӓɦîɗϏɰhеÑ',
                'ȏӂҁϝMϳÑ bъǖЁԖ˽ЙπΠԛԬġӆķЂhɓ4ĨïҢ\\',
                'ǞɕƧȥҾΎǓȖ˸\x91˒΄ʋ\x83зÔԊӟ\x8a,ΏБθƽÞ҈Н\\ԒĽ',
                'Ͻȹ·Ԧ{˙ӅƎɫɅƎēǽʞҹͺԨȓǬуŮ˲ϼÃұĨɮɄηȬ',
                'ȿƂˊύ\\Ӽğш$ÂӴȠͿϖюЀέҳʲsˢӂįɛǏҬ\x8eҽˣ˃',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'І',

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
            'name': 'ʳΈԙȫχɂ˪ΕԆ·Ȩԥ#Ӝú\u038bý4ɰĎȾȼѽʨ\x87цԝӪкŽ',
            'version': [
                -7141775395020624601,
                -4181291855575999815,
                -8772477881609089972,
            ],
            'location': [
                'AġϡζɬʬȮƁxȓȨƥ\x82Cӎ\x99ΘʥĐɊ˫ӾϱϺӾјˏгìġ',
                '?Ѻǫʕ°\x8cʿȽԔǧ˔ɜ9ɷËυ˴ьƗˤӴːЎ҇²õ«ǃчʶ',
                'ƴOѥŧϠ.ОǀļƐǜҗϗúΠѥҎӜĀĺaΒɹƝ˒˴ĘӃƢж',
                'Ǜ+ǢQ?ƣʯѤƃϬќѮˑҫЏȑɉԨƇԤәƃҢԬŷȴϕИҐɥ',
                'ѝłȭïǓÈϳ~Ĺ˼ӓʑ#ÚԚӏβҎŘȵχĮɐПŰǼªɠPØ',
                'ɛͺǀӗώӐħsЫāųŮǉĻɬǈpʽԧųŧ÷ƾғîɶʞϔƦͱ',
                '\u0380ǨʹԮȲϲƸţƌȻēј˦ч\x8cҗƷѥƭΣΙĬłЋԑǟďͷˠŲ',
                'ˌʁͼѵ˓?\x8aӤӖ\x97ЫNʍ~Ɲϴ×ʝŢǱmҲõŤͷʸӡľȶԒ',
                'ɟÜԀɡbşӊʒı҇ơ\x97\u038dƼЬԘ§ӴŬˋyħƠƝĹŏȞ®ʆњ',
                'ɤѓ\u038dԣϐӍļјϿѧƚʺ ΅\u0380ʣӂǚёѵBģɅǴϹϦ˽©ӌϙ',
            ],
            'runtime': 'ѝ\x91+Ѩƾˬȇ΅҃êǹ¼ťϒИ',
            'send_access': {
                'event_ids': [
                    'ȳϻĎǁЄ\x88țҊѿйȵѶɄĦсЊŀӐʚǓʩƚɒʿĄƖ˥Ƿ˾Ά',
                    'ʣͰяΊ\x95юоĖɈ˭ˁāɎȅɸ˦óÐß^ȱųɥßŜɝӡɃ¨҉',
                    '\u038dÅÔǽπӗȑϹžȦƍЯǘ\u0383ˣĦıǳǯѡưӝȂϼɗȍ϶ƍʀȯ',
                    'ŊѶϥưͱƙϯпϿÏĀӆvΰ(єєÅ±ϬԕˢŰЁ\x8a\u0383Ɲ;ƀӴ',
                    'ʖΉɇòƶˈФѳǌсŒþ\x92ˑÌѤζŸÂøǡ\x89~\u0378ƛˬԫō\x95х',
                    '˽ʰȃ^J˗ɽ1ӝÎͷĨЧӏơ˶¿ωWϬȻӿȈΎƴ҂ɕҮ¤h',
                    '˲ϣȍҏɞӈ¹ȟń?ШʥӱʃRӬǅюÌÜǧԅȐXptңőԑ˘',
                    'ą\x80$˸ɇëâ6ʊщͻɐǧđ\u0380ȕ\x90Ɛϐ]·ΑǗҾèÖǡї\x85à',
                    'ůǨϋƀɐҕƉ¨ìÔÂíΫƍΕӘÔĲ΄;ɡǡÂΥƎȢώэΐӿ',
                    '¯ÒЊǼ˧ó˧ҝҒʙΌȊԧήʣɏôƯŒӻѤȁϵ#ǡěͻ˲ӭĲ',
                ],
                'source_id_prefixes': [
                    'Ϟ˵,\x94КʛНÍeɜąҙȗǛϺ3Qέ9ӚƸ$ʵ˺ıĵΓˇΦ@',
                    'ˑïʽʀłơĿîȮ΅БΈϽҸºvɣƩʿ0ɽDŎĘòŜtɇͼÝ',
                    'ǻПƥƘΤcРȪӊхӾͿʟěȝҐȬ\x91сz\x90ˍũʔ·ϘԘɴƭУ',
                    'ӶƷΦʲ¢ԖӺʑЊ-±ԒɞӊǊÔɁӶʗ\x9cԋ˝ϨϘӦТĀКʙţ',
                    'ӎӒũŠƃӈɻоѥĵ˼ηǄΑƳǯˈҒ(ʊȠϟɜάҮɻ¸˚ŖƓ',
                    "\u0382͵]˂ͻǓì\x8c\x7f'ć{ͱƍҺѻ˪Ɯʙ\x94Īȷ\u03a2a\x81ьŧčγɦ",
                    'ЧӢ´΄ǍşɌʻθήф¾ˣ\u0382Ϧ˖ȢNŢЮɔȾΊãɽŔΞďÓӌ',
                    'ÖÕǂÈɝȿэũϪУӥӸɇľӑªďӮҟιs',
                    '´ЈΡțʊmŵѥР\xa0ԕϕԍʨѾПԃʌ:ҙǛϡϗgҨÈжÍȎʷ',
                    '\x83ʖ\u038bŉͷӅґű΄Ŗ©ɃɵħǺ\xa0ê\x8cųƮωȩҰӑªˮЦ\x83˹Ʌ',
                ],
            },
            'configuration': 'mƍŢԈχ¨˂ǮҁşģӏĦȥΆdϗτƌҒ˝ıԬβĲƦǖůʔʜ',
            'permissions': [
                {
                    'action': '×ϜǊ¨mɀɜ',
                    'resources': [
                            'ΈμhϦȐƐӰĬ˭ŕӧ¥\x8dĪϙēӁȋĵӅŞԅȬҷ!Ͼʲ',
                            'ĖϙàʿʐƟʆӮȡMϸώǆФϑÃ\x84Ԩît×Ԭˈ\x9e˩Ψˡʾɂʉ',
                            'ňɆšѵжĝɎȎŏʸĀυȻΈӏłzǹʜɑќҧ]ͻɮϜċɊ¾ԛ',
                            'ŲҤѩҖԔԬѹ҃ɥҿʹяĤҁԋȌӼ°Ъ\u0383ωʺәˏюƤʝДǽǜ',
                            '҅ŌѩŃĄʲϒřӯɓŨʩ\x96ɧҍ˂ĶËɀ˦ќȎҤȦĔŜӓϷ˙ɝ',
                            'й\x8fʤİĒџ˹ɳŘЊĳѬҳώɅВѯŝƏŴӎȄԓӟçǀͼïɾ\xad',
                            'ɶīˇƚԐϼɃǅӲыF',
                            'ӧʎɫŞĹЋ\x81ԗԓ˖őȜzϴчTŉƭЋǦŕǂ\x87ҪʙŘŨƇӠ˞',
                            'ǾɣыɬƒŝƤ=łƨʢǎzĂ˫ԀØ\x9eżωˉ<.tʉʂ"Өδǣ',
                            'ȻÄʭП˰?Б˓ŲğыΈˎźɪȠϒpčСŴǻҼɜŎқҩƎĚө',
                        ],
                },
                {
                    'action': 'ʚԣʤ\u03a2˛ΣǤҒГ,пĽЌī\x89ưö÷ņĈ,~ѶΥLѩ.3ћĵ',
                    'resources': [
                            'Ƽã^ʇϺ\x81ϝϽыȪ΄ƜѶ˂Òˣӳ˰ǂҕ˽ǺÂˑʁҀɥĵPʕ',
                            'ǶɂΥΉԒŤǼ˺кϻͺùƱɢһӮǩƼфɦԔш¹ӤȦόǡГсǘ',
                            'ýхʀϒўʑʛiйνƇ4ҵˠIƺõԑˠ˵ɲϚƪəʜƐ΅ȗƺЧ',
                            'QϏħĉӫǽɓλ\x96ϫɃΎѸǢ˅ŪǫõȁƎɭ\x9aŉ4ĳСʩР6\x92',
                            'ʚȋЌͳƝ˯9űƓɔ1ӰN%Џ(\x9e˱Ķ¤ɑúуϲέǱ+ʉΞ®',
                            '˗ƪҌѶ<ԇÐ\x9aϤΦГƓȅùȲˇŶ\x8cě\\ªqǚΈƓȡ˺ȷÖй',
                            'ÆŴτАĸÛˋοɜˮƶĴƜĝɱӫĄԜŀɄ·Ѻłǩ϶ÌŪǵȈf',
                            'BԋѧаҞ\u0380ʩɒËҡIŸӴξĵƃҩƺŉҰӉʦȫ',
                            'ҴԔΌйΫЁԄԓтQª҆âÅӈ\x82\x8fѐμʭăӆNѰʡѓɒá1Π',
                            'ϯ˭\x83ѫԢŲǩѹ˗Cɵ\x98ϞɶǚһҨÃʧʙƢǳĜυЗϙӮ»ҙÕ',
                        ],
                },
                {
                    'action': 'ζėύ!ÜʱΤʶŋĻɾҙǳӀưЙȘҚ\x91ȹ\x8cʱ˷ȼѫȍ\x82ԧǈϞ',
                    'resources': [
                            'śĤ½ъɾџѵбΏȊʣ˥ѩӪѴɋӯ¯кK˵ơ\x9bϫ\u038b[җĩьͻ',
                            'ӍоҦΫ?Ţϳԁԭ\x96ԔĔԁҀŰҊГЙƾЋ®˝ЂσӪʴѲħѩÆ',
                            'ɵ˂Уıɳʧ5J®=/ʰįǹԣҍѵѡͿӼȅĹЏȍYŤVgеê',
                            'чɱШ˶ϗÌϓ҃цŉ°¹ŌʭͿҞʋǵTˣ¡ʹǥŃÍńϔfϤ¿',
                            'үǠсπəӡĦ\x84ưǻӪ˝0ŞɍҥϞΞІWӱʠǰȎĊkóʤҎȞ',
                            'ΈӝԦȠǁ\x95Ҿ!Кíӑ\u038dɇˡ«юʫ*ʹͻ\x80сmƌіġ˲ɲЌˠ',
                            '\u0379ɵȹδźĒϙӀŢȤ\x96\u0379СșԘɕҎϤʇԅŝӱţǻəǥǌЄХʄ',
                            'ǻ/\xadϰÛξþӌʐӘԙĺɁɸÙӭóƎҙ˄ЮшΫΡñğ˭ΒΑɼ',
                            'ƪЧԪ`ƠʯáБсǃьҋƛǘҨʟΫɫͲ\u0378Ĝȴǭƭ%ӯпξϐĪ',
                            'хƉԀĽȟɥПæȉʻϛǯѢƲȢȏÖЖȝ˾ʏАȒŒʝȺĸЁŖɷ',
                        ],
                },
                {
                    'action': 'Ԩ>ʹϋϡȐÂʌӟƇ˴кÃʺ˙Ȟнβ\xa0őҰ¹ʱΓÝTΊӨѸ˪',
                    'resources': [
                            'ÈϾCтýƃӏăЪǭŌүœ£ɴʇʤ҄ƌIȧ¡˙с˹ƵoƔaф',
                            'ŪƺѽΩъҎΑë¿Ϥ҃Όǵ\x8fÜјǓѺϔǒ҈èςΕ¹ǵӨkχЯ',
                            'ɁӗƿŸÈѭŔјίʥșΙǏƸʉ¨ϐѢ҃§ɚʜÇĹǋ½ƪȞɹφ',
                            'ă(ɼǅȫĬ˰Ԯф˞ϏԠhʹЎ\x8cęǨƢеέăȗɛˇЌƸɼŧȢ',
                            'ӊņͱʧӈјΜяĩˢɔЮƧām5χ ϐ˞ѮƘԍǟЦϪĜǦϷˈ',
                            "ƭĂ'ҒˌµÌΜʿѷҾԮyǣ˅³όɞќњҌǀCȚȒ\\ʡϣƈԄ",
                            'ƃүзϮǹӘɚʹШčԧχÑέàуʁˊµ7hª\x9aʺϫ˲χ6ʓé',
                            'е\u0382ѻϘśƝĖɃɴϵųԆƹϛҏɸȘ¤ŬӒRʷĶ=ɕȬЧ<³ъ',
                            'ӨɟɊѽѫЗϹҮȩƍǠҸͰ¾Øхǡ\x9bΌıԛˎλͶӮƐǡҋцʗ',
                            'ӵƃ\x96шʽϮł\x95јˇɖ~ǀ`ăĖXӓ\x8eƆįϒΒѣĬŠӡǼ\x9c¬',
                        ],
                },
                {
                    'action': 'tŻОoϖsǪʃ?ÛԤʚǓƻ˝ɼɳ"£ìԤΪҼƿɶϷ¼¶ŀΣ',
                    'resources': [
                            'ʱҺƝʻˋƱӬãЀͱӘÐ\xa0ßǿѻ¥ЭπȠɡєļkϽԬԔˍΕʳ',
                            'TРɷę\x8cFɑȧЇϰӦƙ˧ёд',
                            'ҙŖЮˤ\u038d\x96ԘѶHàŻ\x95\x9bʶϹґEЋ2ɋԊ˕ȧʤόʶƯӮŭӗ',
                            'ε\x9dÁ®ÖЛΑɛſυөʧзԚΧN/ɴΒӱ\x83ϣɦ\u038bԟiӂξĢś',
                            'НȻ\x96ǵƸͱQŨ½ƾśãϐͱģǸȣŏɅԈʇʜ˚ʐϑӄ@·Ϡš',
                            '˱Ӥ˩üɻЫφҸƹӜé˲ϰʣŨȔ\x84ԄΩxѬτfʦ®PÊї\u0382ȗ',
                            'șζǣѥɥѡN|ʐщ%ӉѦɖɌ\x9dǶӑόôɽȟԮĈŃǇ˞Ǹͽњ',
                            'ɢӽÖѸҹźϠҰҠÓκȤƑЉ7ʟоòўԒӨђȉӢĥΏɹѽɇб',
                            'ϛʩԭ\x84ȴįÅӷõ˨ʹѵϱÔѨŞұӆÆȕšҶȎϷƎӵʘł҅Ě',
                            'ÛΟҠ£|ѥµԬÆʕϞϠHòčӌҺ_ǟÕҡӸȭǖˠʴIǀӯҰ',
                        ],
                },
                {
                    'action': 'ӾЯȪό«¦ŜϲƳŖϿҹŃƪʬΛĉĴρǆÔ\u0378˞αʑǶϐѫʲĘ',
                    'resources': [
                            'ѳġù¢\x8aӱηÖȿǏˉgџȒǗ¨ԦśϙΏҗƢҙ',
                            '\x9a˯Ůфώɩ\x83ðPҠѺʠјӶʞÄ\x9eZ\x95ȍĘѣΠɍӘÀǢåčˑ',
                            'ЌõӅɏ\x8cʔǌɾЬкέįΓæӓԇčKɣ9YϷă¬ο ҜUėʀ',
                            'үԗӓÜфɩúώӫΊξɰΓ˺ԇōƭɷӼŉʆǕǏˇŻѭ΅˗ļр',
                            'ªбȦǱɮėӏӁόӁ8ƗnȼĠɁżѫҚԨαӗǤʂƪĲːӨĞң',
                            'ŴǪɏ©εЇôÑî\xa0ʔԎĚԒǘДЁӄИĦ÷гʈдǫѤÊ{Ăȕ',
                            'ɿδίτuǰ¼ſţϛѸȍʺƁɒ5Ԏ=ĄɬžˈɦҟȪԑ΅ћɰч',
                            '©ѿāQƿҏӷɲϗЧȦͰѾԉȚŬêѐɟԧͺȄӥσqӻ\x89ɓɇҥ',
                            'нǀԋԑӐʓ;ǑӬ\u0379ǲΝӜ3ǲǀʏʗɁϟş¿ýɝΛѳŪБЫƨ',
                            'ЅҍƩˑ©һϢɺɟϝȚБĸЎЩÐĺɅŬÖŠљUҀŗ\x8bƄªѻѿ',
                        ],
                },
                {
                    'action': 'ҳ\x90§ȢӯřƟҧ˘ǇóɈЇЌɺȢўɤ\x87ʅϣόКѤѫω[ӗżΡ',
                    'resources': [
                            "ůǳʹ΅ӀɧʜĽFК-ɬł˅ƗĴlԌ¼Ĩ¥ѥáʵҕʨƒǿ'²",
                            '΄ҊMϙʄԣƢ҇XˠдɀѮΤƹһɰјӤҶϴҙÓШɋóťŤĉ{',
                            'ɺƓǻ\x8bϨØҁ˓°ȼϲϬîɎqȬ˾˾\x91ĢǻФҰƴĩŝΚɻǫЇ',
                            'ʼŬɦʤӭϦ«\x99ȶǐƛĹʩƞʥρĞ"ҡ`ΜõѐРÕύѐɳǣʹ',
                            'ԫȲПȁƨȸәќȁеġđΣ²ŪŐǘʵωQŵʽƂĮđԜѢѨȕę',
                            'ȤÞɃƎ¾ұ\x95ЫʀîԘǨǍԛǔɰЌˏşӡΠȭīͶӬˢ¶·ї6',
                            'ѫθ˒ʓӓĐ΅ӊƙИҞӪҢȞϮ˚ƞΌæÜdҘнħÏЛŎŀzƘ',
                            'ɩÃ±ˉ˽ǱȭʰҨ6ҕо˪ЃáЀҲ\x97ñϾÜʼǛЧʘПʋm\x89ɽ',
                            '¿Ƞ˄šǉ҉ô®ÿ δϏˤǋƢËĤαʶКZиӷ˼KƲäǱ·ʎ',
                            'ΡЪǎ9ñăɶ\x86\x92şʒǊ˞ÂǘŶʜːºZЕџŞ΄\u0382ПˢѢąˎ',
                        ],
                },
                {
                    'action': 'ä\u03a2ƀӀĪȘϪĐԓŰǛcСсèˈɈљȦuȋõP.Ԟɯǰ<ĔΥ',
                    'resources': [
                            'Ϸѭȕ¼ ΪЍȤƙӍȂƦ1rɍīϕӢǖɾɖ˥Ӽ˫эWҴΑ:ʗ',
                            'Ҍ¹ӌЧĄņǫƖǯѷԪť\x85ѣ-ŮȆʖÒѫƹʕмʅı˓Vйџĩ',
                            'wŷƊVʵƼәЯϿģѓ\x9bʔԨųÂͻѿ\x9eǅҸíļɄǒƵǝ\x8dʼǆ',
                            '\x87Ǒ˘\u0381҆¾˄¢ϽѶÈʖʓѴǁӃʝȫ¨ѩ˘ωɈѲ[ѓɓPǩè',
                            'ŉҤńɸͷȦѦӶúÎ|рƾξʫԭӿԒ˛ȇHҲŭƓԗβӕ˷Ҷѻ',
                            'ΪёɒeǖÚϑʽɖЌƵϗʰӪȔԍӸʡΦŗȁMȯϻǵěʥиѲѕ',
                            'åoƌӶФƠʒ¼\x8bȞÖϲʀчŵįȐʟѵɻʸšʾÖ\x9cԡφ϶ŵѠ',
                            'ǗϔѶÕɯͻˡAȠԢƝʷӃАФԫȔ~ѬɠѽʫԙԅһΛФˏʸˆ',
                            '³ʔЯίŏөʰ\u03a2ȎӱˡǍϛʑ|ɍǮw\x8důϊόŎνΥȥΎȿrρ',
                            'þ·ƱǫſȟƥAžuҊɘ1\x86ƐРýəƷˬ§ŽʆȭΟɜɰҒŶ{',
                        ],
                },
                {
                    'action': 'ҋǘχ.иkŨѢϳƆҎ˝Ŏ\x85ύҞьѯşӱŠƍŊGН¨ĂʋðƦ',
                    'resources': [
                            'Ǖ\u0382Ͼ\x7fѥːĶʋ÷ıƴǄ\x9fȍ˛`UʃƋŕ˲ѰȠǁѳȳ¼ԏǦȪ',
                            'ģĊƵхӯ.ӱѹΤϽʾϲşͼʹːåˏȯӈώɨŵĉŀʣːοƊȮ',
                            'Į˽\x82šŊɒǾȾ˖\x9eӴ˭ѯЄɬĀŧƏιäŹΠűŉȑʏҽʛŕ¦',
                            'ԞҏĞˊɢĢԈŮυôǢÂ˒ΛΩȰЇǮǌǽʟӪÂĽƆÞӳѳ˼-',
                            'ȏșкҦ~ԛrǔƲѾϮȎϿʙrΙâһƪǉí´ƑрɎϰ\x93%Ұƴ',
                            'ŧϴίĵʮúÁɚэϗШΊ˧ƿƳÀªіDȆӠǓƲŖНξӕÆǫΓ',
                            'ӶĖŐ˼Ӣ¶їԇJˠ½˷ƮеԇлĦΟm²ъǍ¾ԙѮŠɏŲϽR',
                            'ŷӾ˛zƃõϴÝĔÎƼȗĳGщʎƚѶÉųˇӑʧєǼҫ˯ʍĚɵ',
                            'ϼѶΊƭЫѭʈȊɌÑǴӢЧЧ˯ΖϐԘʄӧLΘǡƐΡӀi>ŧ@',
                            'Ȩоѿ˂ȏœаԒƂàңˎ+НοԫϴЪ˃ӻʠ; ӊӰŻɜÈˣǙ',
                        ],
                },
                {
                    'action': 'āȩ~ϰˏƧ',
                    'resources': [
                            'Ғˁş˾ǶÿҮ\u0382"ɾӣhŅҌ\x98Ŧ˷ϊˆ¼ā=eѰӌƤǘ\x89ɵӕ',
                            '\u0381юŴzѯ\x8aúSυӯϝѱʒŞφϰˠƖҍʱԠӐҝΐʌP',
                            'ĨӤöϛ\x8fэĚϣθȫЛʨҞ˩˒Ѽˈ˵)˰ÒЩ\x8fүӱɔģРk\x88',
                            'ɩ\x8aȔҢơˮȮÝαËӀżǔǍɝΌɈƃԃʋ˰ˌϨƊĘð¬ǆѨƂ',
                            '҆ƽϳʘԃʅтѰƢæиҟʓӦǅκɷйԭҿχǣɕ\x80ӻˡȹԝʁк',
                            'ČÁǗҐͰLFͱѢȔʕŋǾșĐхʞ9»ѵщ2ɢǚ>ԩʪњԠΨ',
                            'ǗœϺǩюΨиʰӌϫDі\u0380ƯԇauѠξ҃˶ɀï\x90ӣԫӀҥũԀ',
                            'ɺԜØЩ˥ЃĵǺҙɕлԨ\x94ϲʠԦǔɑ;u\x82ҐʗƲɒЇǑΓÕȳ',
                            'ǴŉЕDĻ\u0383Ε\xadҚʋјʟɥ\u0380ƕɏ<ӒȲúçȀѪӵ\x8aϾѻĎĩƛ',
                            'śǧΫŰŨϊŵřΘЩƓӃ²РЧÈɩǭϳҋъ"ӀԫǋʻҶнȣJ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ŗАӿ',

            'version': [
                -3584041763617283216,
                -4160441138428559387,
                -7756277687778041710,
            ],

            'location': [
                'Ӱ',
            ],

            'runtime': 'ӑ',

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
            'name': 'ʰŔĤçћƸӀΓ\x9cǗ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ć˅ͽ',

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
            '$': 'ϺŒīϰ\x99ȯǶï~ҺĻ£ѺӟBħӘԎʁӠʧӽЁӰΆӶȪŝĿԂ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2998859547871902810,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 560157.3032592301,
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
            '$': '20210909:200541.722642:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Ѣþbӱňs¤oȾїҴʽԨžб҇ˋͽŨ5ĒǶώķǚ/ˮdԁŐ',
                'ԡňNǳүÕv.оȽоϑЅhΎ\x83ӷφӽȥϹӦIķ#\x8aӷҙɯ\x8e',
                'Ȩ±Ʊiɖͳ\u0381΄ʉıɭżMί\x87ӵ҃үǄǼӜµʳȗǗϞȨǶƞɟ',
                'ˡɤΙѴȴ|ĔěЀđϴР\u038b˂ԛ\x83т¯ʥ±ɴҥҩŰ˯ҠфɆϚσ',
                'ɧĖ\xadşӝԞJщϏ\u0383я˘ÕФϲϰ˵ÀɡņΧ5˱\u038dϟǥ˺\u0382Ǩȹ',
                "đЬ¨ЩӛϩŴ˴ϑǺήǽЮƼʷЮ\u0380ПĭŽÚѓĐ\x9eʔɓеȲϭ'",
                'ƣίѓӯˤųðI˂ȫ˵\x9fЉɛƘʗӭhęʼʊҋџǊІҷáȼǳ˛',
                'ĆJűҢĠηϵʸЪСĕ¯ҦƢOӃǉϓʨЌ˹ƽͺƻɡȱӕҖϡǲ',
                'ØƅͿΏӋȆɵ˖ǗǸŬ~ӛϜʿȢԂÐӤƹϗӵӃƣχҠȵί-ΰ',
                'ïȷȐˀѕ˜˹\x88упӢƑɒԉŽɤΨҀѧŚȸЄſΡӋѪӈǇĴï',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                5540589305509328568,
                -333350237811561337,
                -7476260592570093956,
                8015393649612105239,
                -841093851912424220,
                -1661628452662611310,
                -7668920080267385014,
                5235540500927242448,
                1341941238474342219,
                -8790852870893407095,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                986035.4121070898,
                714249.9652187322,
                -14920.511996417423,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
                True,
                True,
                True,
                False,
                True,
                True,
                True,
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
                '20210909:200542.545132:+0000',
                '20210909:200542.562700:+0000',
                '20210909:200542.579704:+0000',
                '20210909:200542.596561:+0000',
                '20210909:200542.614170:+0000',
                '20210909:200542.630573:+0000',
                '20210909:200542.648344:+0000',
                '20210909:200542.665213:+0000',
                '20210909:200542.683624:+0000',
                '20210909:200542.700535:+0000',
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
            'name': 'r\u0381*ƼêΔȑģŶӮ\x84±ћ\x8fĳǙȁ^ʳBҸɦʍńθϷǚÕԪϿ',
            'value': {
                '^': 'bool',
                '$': True,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ҁ',

            'value': {
                '^': 'bool',
                '$': True,
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
            'catalog': 'èѨӅѺӭ±4ӋɲʊȼÕҧ˾ăƑơÔȦÍɟΈ\u0383þìȱԔtȷҘ',
            'message': 'ӭʊϲѭɟĊʎɰΟфH½ӧĚĔɏΤɷҿÉÊwǻԃƎÜŐā\x83ɘ',
            'arguments': [
                {
                    'name': 'ѨџǫÿңԋÝȿÊӻȷBѓĸhѿ·ӄƗ˾˩ϸ{лƌɦ\u0380ǎʕʼ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:200540.066426:+0000',
                        },
                },
                {
                    'name': 'рú?˦Ѫ!\x89ЕƵˬƣӡ\x9aηȴùӳêƾ',
                    'value': {
                            '^': 'float',
                            '$': 86032.85602678382,
                        },
                },
                {
                    'name': 'åĞ\xa0ϼeũ#ӄӐʥѮТё:ˎĀɃӀϒΜ\u0383¿ώɗЧǠѫчFƼ',
                    'value': {
                            '^': 'int',
                            '$': -8449253340652826356,
                        },
                },
                {
                    'name': 'Қыʕ2ЦΖӶɜʩ3τ¥ԫԐ³øΚĺ^ʂŘӛ˴ǒѪӴ˙Ò',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210909:200540.263184:+0000',
                                        '20210909:200540.279369:+0000',
                                        '20210909:200540.300794:+0000',
                                        '20210909:200540.318300:+0000',
                                        '20210909:200540.334259:+0000',
                                        '20210909:200540.350117:+0000',
                                        '20210909:200540.366205:+0000',
                                        '20210909:200540.387829:+0000',
                                        '20210909:200540.405853:+0000',
                                        '20210909:200540.422026:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ϙŝÊLɩʚҙƧ1ŵʘÅМԍǂûӽΐȚĜ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:200540.502677:+0000',
                        },
                },
                {
                    'name': 'ɼϸȣгJʩáΑѝŦˤŎ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ǫӒȚɞϚɹӞʀ-ƈ=ʷҼԊӽЏ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -19821.231471931504,
                                        746550.6774217227,
                                        321628.1839727373,
                                        551439.6094501169,
                                        7953.083040409823,
                                        339980.48241486057,
                                        914212.9263952657,
                                        202376.2204322382,
                                        584605.5545697269,
                                        598788.6198876817,
                                    ],
                        },
                },
                {
                    'name': '˅ƨJ[ΖΒҺǧűѹʿƫɵ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -4622986354416522280,
                                        -9157589749426756976,
                                        -4064993151687350682,
                                        6579914261703240647,
                                        -3603716982086644800,
                                    ],
                        },
                },
                {
                    'name': 'ӲӊŷʺϙϗßϩƘđ\x98дɵ\u038dжƙ¬',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ҧ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:200541.310042:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ÖѨ',

            'message': '¶',

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
            'identifier': 'ԮɓœѣŐSƬŁԣȒɨ7ɮЩɗ¶ɸƬV¤åϊо\xaduśɻǸ§у',
            'categories': [
                'invalid-user-action',
                'internal',
                'file',
                'invalid-user-action',
                'access-restriction',
                'invalid-user-action',
                'invalid-user-action',
                'access-restriction',
                'internal',
                'invalid-user-action',
            ],
            'source': 'ǌɚәǹɡϗ\x81ĆмĪɛ\x97ϐĞϻ˷қԭǐϱŜͿэžһɂԎŘøS',
            'messages': [
                {
                    'catalog': 'ҼˡҼˮϫȹҠȫθԘϜЋџϯˉǼǚϤҊǰϨʅҴ¤ҧъΝΰ%а',
                    'message': 'ʘɥɽRӏԌǢȲʜƷϵɋ˺Ǥʢ±Ҭù®ӮǕВкĄʬɴŎȤſȒ',
                    'arguments': [
                            {
                                        'name': 'ЖѽԀǊϻúƭɑįƑʝИһҰӿуĬӫ\x9f6ѬпπͰϥŇbŐĉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200525.670992:+0000',
                                                                            '20210909:200525.699364:+0000',
                                                                            '20210909:200525.732749:+0000',
                                                                            '20210909:200525.756375:+0000',
                                                                            '20210909:200525.776022:+0000',
                                                                            '20210909:200525.796648:+0000',
                                                                            '20210909:200525.817193:+0000',
                                                                            '20210909:200525.836856:+0000',
                                                                            '20210909:200525.853724:+0000',
                                                                            '20210909:200525.870211:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϸɿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ͼˤӶ¤˖˕ҖÓq˵ñâēĥůĚÛàČƈźǴĻŲįЧȘϞϊƢ',
                                                    },
                                    },
                            {
                                        'name': 'ӬҝǵξʢȜҌϙʙșҎƹÈɇЄːńŲϞę\x85іЂͲҵƵˤŎɕҧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ǥʼύ^¾ɾԘԓή.ȼȼӇǆԫҫƵЇӉ¶ϥҀ\x8bΡġKԍ˙³ͱ',
                                                    },
                                    },
                            {
                                        'name': 'ϣǤfә˅˓ҖƹϯOʤėŘ\x99ҐқƗҡΰƻÝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200526.100919:+0000',
                                                    },
                                    },
                            {
                                        'name': '\xa0ЯΌüM',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200526.175605:+0000',
                                                                            '20210909:200526.192752:+0000',
                                                                            '20210909:200526.209546:+0000',
                                                                            '20210909:200526.227780:+0000',
                                                                            '20210909:200526.243966:+0000',
                                                                            '20210909:200526.263629:+0000',
                                                                            '20210909:200526.288815:+0000',
                                                                            '20210909:200526.313804:+0000',
                                                                            '20210909:200526.334591:+0000',
                                                                            '20210909:200526.358804:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ρ¢ԙƭɨʔԠΟƐЂƾžԁƎêʙŰӾөȞҡȭȯ˥Ǽ\xadvτ`ň',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ΊÑ˼'\x7fυҼƶ©ʇ¨ˇʶǨΣϜ\u03a2ȀğȟϛҎƀŨºȫːҴ˅ή",
                                                    },
                                    },
                            {
                                        'name': 'Ԭʋ˚иϨřɩɚ˓ȾӝОԏ˹ӣǃˢόҝ\x98`Ǚ=ʠŲԚȊơǌс',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            834661.9139323449,
                                                                            327957.12850819837,
                                                                            33007.59928156852,
                                                                            602699.381323579,
                                                                            -21170.930458205286,
                                                                            164498.5156899296,
                                                                            809520.3168787601,
                                                                            849672.635978578,
                                                                            862524.0912528117,
                                                                            808572.3766782063,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӘŴ·ùЌϼӴКǱƇͻλLȻņˉťςȻϓ¬ҋÀìƣϩǸЙʒͽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɏũȴǀӀ˻\x81˕ΕʟˣʙȥҭĴĭԙ˜ăЇΉɾɲϧγϯ˦cȐƛ',
                                                                            'ν¬ǺÉĄ϶ВΤʢЇΎпȅʡΝа\x91ϝԀjќģѺːӽѩĖȄ(ļ',
                                                                            'ѧҫ»ϊʟɚ΅ζϘ\x95ӛɶϦ҄SӟϮϓĥЈҊЭʾӚĨțōҿɾΫ',
                                                                            'ѭҙǴŌ҇МǌҴʋѬƭνЬάԈπ6э˜ʖо\u0381[Ǘ¾dŶςҤĢ',
                                                                            'ɆìƄԟӞѠʂÝΗÛÖǁɬԜȅѱćÆƾ˞УʻȏάˬˆɪƆƝţ',
                                                                            '}ʖοƽжԐȒ҂ǘƗƍԅǝùЋɯ\x8aǌӻɞιҦ\u0383ǩˣŜlȸ=°',
                                                                            'сųφҗ\x96Âϴ~ȝˑϼŞƜ}ĿЫƒʫϖǉҗȷѥǙɗσ¼ġ҅Ɣ',
                                                                            'ÍõɂŁ<\x84Ȯ˭ŐͰĐϳžǛáȽÕѓͿˈĂқϛԞ҇ζѳбӬʷ',
                                                                            'ɲӽǟнÏÐʐϙκϋԫ\u038bɦҊfҚƖõͻԘɼϐː-ĕ İ"ԢĤ',
                                                                            'ȻʳұϱʢʛщˡɄӓˇ\x93ҴӤǭwǈдPǅȭЋ·6ɬ˙ǟƲŸf',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҧйÝ!Ԓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʔ¬ÍӽŦƅШҋЈ&ƣ(ľЦɽЙ/ӗʨʤŀώӮ˳ß',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƋƬ\x93ԚŁȌÒŔŌљĽҞӚǤʵʂι\x99ƶƇĿΟԩαˑΗʲĆǿμ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƭ·ŷHѸë\u0379ӗҮ2Ɗepӌ®ԫƦȴяÆǯʍȸǲƥЧ0ʻ\x7fэ',
                    'message': 'Ҍȡǡȵº˷C҄Ð˂ͺũƿДȸʑżǁĕң/ǵ/ƄÕƿǓǚНԔ',
                    'arguments': [
                            {
                                        'name': 'ȆİβԊϽ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 601274.891646943,
                                                    },
                                    },
                            {
                                        'name': '\x81ҡѕƈҚMoȜ˱ȑƋԕƲϬÑûџҾĊġǣ˧ӲĲĬ˦ëǹĚ+',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x81ЎǡĲ҃Ѥȱ%ДҨǐЦѾǭ@ӄƃ˰ϛʞԄ˒ķѦӴҿȵŌƦʯ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -258185330777265292,
                                                                            278167748338614485,
                                                                            1688773044300753649,
                                                                            4904069652897437322,
                                                                            472290130671742062,
                                                                            -5113726749419444115,
                                                                            8705932395986784311,
                                                                            -8034598096148851357,
                                                                            1511397680313607599,
                                                                            4135561371124541911,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¿ʹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200527.702283:+0000',
                                                                            '20210909:200527.722250:+0000',
                                                                            '20210909:200527.744758:+0000',
                                                                            '20210909:200527.766763:+0000',
                                                                            '20210909:200527.788161:+0000',
                                                                            '20210909:200527.810735:+0000',
                                                                            '20210909:200527.833403:+0000',
                                                                            '20210909:200527.853679:+0000',
                                                                            '20210909:200527.870311:+0000',
                                                                            '20210909:200527.891377:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˱8Ϧε',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200527.972518:+0000',
                                                                            '20210909:200527.988935:+0000',
                                                                            '20210909:200528.005612:+0000',
                                                                            '20210909:200528.021715:+0000',
                                                                            '20210909:200528.037670:+0000',
                                                                            '20210909:200528.053762:+0000',
                                                                            '20210909:200528.069561:+0000',
                                                                            '20210909:200528.085234:+0000',
                                                                            '20210909:200528.101019:+0000',
                                                                            '20210909:200528.118036:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ü\\ƠÞїѸФ:ˀӖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            496550.03590099467,
                                                                            386771.87141499564,
                                                                            336325.509080572,
                                                                            216913.34973541205,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЅȬϬѦԛҽҼƂXԙҾҁюǅ|иɳĘđɵΎɧ\x8fϞʇ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ŐƽͶА\x8bʕ\x7fƑ˓ӏ&ϣ˶|·ƒȶĩʐӽięВ'ĩˑ¬ȋĻo",
                                                                            'ǸAƈŷǍȦά˯ǒ£ʹʊǒϼѯZɬɯǼԇǁÉʧ+Мџΰ¢ӼƵ',
                                                                            'ҺŊ˹Ιҋ4ӪЩèƕùöͷȚ;\x9fƸäʦDÚĮӿȭCRʇɓӅ\u03a2',
                                                                            'į\x9fƓԫϦáŴΪ\u0379\u0381Џ+ςϦ¼ԗҿ\xa0Мϴ͵ѾƨƴϢЂͼɡîʡ',
                                                                            'ŧǴбԣЩԏӊ˅Üđ\x94ͱƗȂўMǈԏϐӡȻӈǄЉȎ˔ðǶȐ¬',
                                                                            'ЇɧƄɃκĚԝӺнƸҿӸӳЭÔɢӂȲǓӟĶЮƯÇϪŅҐĤϳǩ',
                                                                            '\x8fнƜï,ŰȦԃ¿ϣё·äӕВõNʥŞȰʴʈśюńӶϤŮϙљ',
                                                                            'ǂʕ¯ˇҦ\x84ąЖ҈?ϓϚʼņЭϸÝˎԈԙɮǻѷʩàɣрΉÌϣ',
                                                                            'ǰ\x8eǜŒȦųԒ\x9dơ/Ǣ˼ѿϺɐөԗǘѕŏІǷ˻ìӾОθȩTɓ',
                                                                            'ңӍМӏVǿǉʼϑNУȗŔΘԎФЪЌԁҒª/ӯеħΝҝƍU˘',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƳμӺŌȔιòД²kŕЃр(ĬëȃȚǆȝӌĥȫҊϯϙóƋǭĢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 219081.65159288916,
                                                    },
                                    },
                            {
                                        'name': 'ɲʦɭӡȓĵԤĕΠШƙƳbɥßоǚŔʹͽÆѓоԥ\x7fû\x8c˭Żέ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԐѺ;Řԇ\u0379Ȇα¨¦ӱǛΞ;ԟǫҟ[Ćϡț\xadЄȽ¶ùȋԫϤʭ',
                                                                            ';ԭĬƪŌƸӐυ@ƗԬ˄ϥΣęƊĈ˄Ȁ<«Ӫϴ϶ҖҸ˸śϠ˒',
                                                                            'ӈƴцЎʫŰжΪɱ\u0383ή˥\x83ŪӞƑη\x8cϑɨќԎΌļʨʥσȈOƶ',
                                                                            'ξʞ9ɽŷα ʜŀˏͲϚњƪҿñ\x85βÁыʞ΄ԦƴѹΔūȟŐï',
                                                                            'M҅ĝʺ҃ӸŹтϹœӝӊʶʭӓңſϕ_˒ͻў?ҁȬɇ(ʏЖǎ',
                                                                            '˗ъɤԏΛПɹϏȋϕǇ˜҆őμǱɻŝѽѫΓԤҢŘ\x86˂˓ςƜʓ',
                                                                            'ĭɾĚ\x82ψȆΡħėŪʠʱēӇ{ǚϜԥ½ĝűÓӦԎǇʞԔʗʓқ',
                                                                            '\x93·ΡKŷԈɆƼŏĖҌ{ŬHĕɷóͱȱÍ0єƱȫ˹ŔϊƑӮ\x85',
                                                                            '˰ʱĽҺ\xadǯ+îѯϸĒÖԢŕԬ҂ӌɔЙǌηĬįʨǷǿ$ÊУȌ',
                                                                            'ľƈʧӽβ\x80ϐԊѿɹŗʯ҈ǭʢӔƳдǄ7ŧŅƽÝƓɪԂ(ϔǹ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˻ӆġΤЍ\x88ʒţԆʔĊɮӊȠɛ˧\x93\x8dɝ#Ѫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200528.893897:+0000',
                                                                            '20210909:200528.910522:+0000',
                                                                            '20210909:200528.927004:+0000',
                                                                            '20210909:200528.942888:+0000',
                                                                            '20210909:200528.964811:+0000',
                                                                            '20210909:200528.982026:+0000',
                                                                            '20210909:200528.998168:+0000',
                                                                            '20210909:200529.015660:+0000',
                                                                            '20210909:200529.032455:+0000',
                                                                            '20210909:200529.048185:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '%őbƌԐӰǪвҬ˛˔ĳˏʎĶвʨŋɶƧ΅ͶˆбӂƏĞԬèԏ',
                    'message': "£ԝ˛æԊйЕʘƵЫӌǁˠǂюΜϤΊǲĸ˘'ԓ\x93ęˣΑ˨ÛΆ",
                    'arguments': [
                            {
                                        'name': 'ҝ΄Ƙӄʼəʵòɭƛɔ1¥ΜԑđќǎǬOҒ~ʕƦчÇ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÃŠƭʌфʏԟЭҮʅԠɜƺѭΠЈņϼ\\Łł˱ƈ΄',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 433221.2294326024,
                                                    },
                                    },
                            {
                                        'name': 'ôԛȉьǹÝεа˱ǐ΅ɕϷYŦΒԉʂŉȍ˘ˁƐӶʯʜϹёğӕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7058356698962156788,
                                                    },
                                    },
                            {
                                        'name': 'ЭǱ˧ΡʊΗӤɜъśƶԜѕӿƪɺϞhӒBīɘĊΖłÏҤ¡lċ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 725867.2176516586,
                                                    },
                                    },
                            {
                                        'name': '5ԍ\x90ζʭ\u0382ґyɐ±ќȑ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӰԋG\x98Äҹвοˤ¹čԓϢº',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200529.725880:+0000',
                                                    },
                                    },
                            {
                                        'name': 'қҖϷϤԇÿʣǅ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'oӒĉŜ\x8còV˽ӾԬļ\x8eȸΐΟÞĥаý·îȍȎƿɷЎӉӔÞҳ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ń',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 443286.8574741093,
                                                    },
                                    },
                            {
                                        'name': 'Ҳ\x8c\x86ΟɸÃ\xa0:ȎĔʃːѢíĶћɎÕЃbɊȬУƅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'οɏ˼ΏɀƜӫșǈʑƪŌȎԪŗȽԎωȋϖh¿Υ˗ʲØѣĂƒΡ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˰йǉʽǐƀΠҴȨщ˞őѴӈƿņė\x95ȖЁЂŭ\x84ÖӷȲΦĨӴü',
                    'message': 'ˮŀŐ˨ͱРІİwȞƟȶΨLšÊØÇ˵ԙίѩѷʊ\\˙˘|Ǧέ',
                    'arguments': [
                            {
                                        'name': 'ė˘ˀ\u038dӵˍԋϏҺҥН˯ŊҩԠ7ŭȴә҈ȇɟʆɏȒŗΠΘҊɤ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200530.518628:+0000',
                                                                            '20210909:200530.538831:+0000',
                                                                            '20210909:200530.556831:+0000',
                                                                            '20210909:200530.581468:+0000',
                                                                            '20210909:200530.598950:+0000',
                                                                            '20210909:200530.615639:+0000',
                                                                            '20210909:200530.631707:+0000',
                                                                            '20210909:200530.648813:+0000',
                                                                            '20210909:200530.668696:+0000',
                                                                            '20210909:200530.687817:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԭƹԂɤеɣӎО5ăәªʅҰĨ`ђɟʆτ-ůġÞȏȨªˉƝ˛',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            672461.0766769083,
                                                                            568769.0656195214,
                                                                            480649.2895970292,
                                                                            260019.69339322037,
                                                                            82774.2818484437,
                                                                            207440.3341315044,
                                                                            26454.1233828353,
                                                                            618179.844645541,
                                                                            991266.7116045409,
                                                                            359414.96094191674,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʾҷɓŜҗͺԈуºɁȋ{ɴȟкODʗ?ʀʅӪŸȐӵӞ\x8bˣmӱ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200531.016430:+0000',
                                                                            '20210909:200531.033101:+0000',
                                                                            '20210909:200531.049899:+0000',
                                                                            '20210909:200531.066578:+0000',
                                                                            '20210909:200531.082464:+0000',
                                                                            '20210909:200531.099545:+0000',
                                                                            '20210909:200531.126067:+0000',
                                                                            '20210909:200531.141544:+0000',
                                                                            '20210909:200531.158920:+0000',
                                                                            '20210909:200531.174678:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˔,ǬԮLҵӄѶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3170557143316370653,
                                                    },
                                    },
                            {
                                        'name': 'ъĖȖщӖЍgɾɔѝƭӭɠѹϗϿȖ4ҁûųɴƇ΄ǅϺӕÁҤЗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЄŖśѩÍϠȞÜҊӬѽϝϝĉʒ»ȞlБԁϰ˒ȟb˞βơϏƖν',
                                                                            '1.ƃ˻Ж\x98έĸɴб˟zȦɤƧ\x8dϜˉɽČҮνƍхФǕzęĥҵ',
                                                                            'ǰBҹʧǶļ˹ȥԭДēΚτΘǀĮƄйѷÇkβÞЋǃ\x98¥ßeǼ',
                                                                            'ǩӢҼšłӥӹҴŶ±ӔïіƸȤǒǒʔĨϓȖҤԟóǀįÞύŐ?',
                                                                            'ȵǄǌЍгΥÉкјǷʵњӢTϭ¶ǈóѹӐөƾӌǓǄ\x8aĵÉʝȔ',
                                                                            'Ҝ6б*ƏɆΏ\u038dмnơӏу\x81ʬ͵ϧņҋa\x83¸¥ϪҋϿƍҋΞȨ',
                                                                            '\x90Ԫ¾ǾǮhȁÝ˶|ɓkśɢȐŇ΅ȒԈŮҶǊӍΟΥҎȌåĕƝ',
                                                                            'ϔͰїͽÃĐӿ˴`¹Ё˗ͽӞƖÎʎÿÃRĸɑЁǳ\x7f\x8dβѬԖѨ',
                                                                            'дɛëSɭț\u0383bŽεҢ\x91ǵˡ\x88Ϻɹ˛ǻѵ˄ΪˈÀӓNϚɉɥƕ',
                                                                            'µŀï¨ӉcʀĞԡ˸ШŠɩҚЎҷ˦ϞâӂưɫŹҰŘȼóŧʅý',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΛЁƛКǢԘıʮӸɇъ¦бŘʂʓkɮ\u038b/õŔƬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 56714.78323798219,
                                                    },
                                    },
                            {
                                        'name': 'ҚʓϔΆԓǬʪϽFέ,ùŀПJȘÓӪ»Ёļ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200531.630074:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ðѧʼлʄǚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7014501584230300331,
                                                    },
                                    },
                            {
                                        'name': 'ɑKɗωˏ˽¡ԘѦѳǜӕѸӷǆϑĜ˹ˀҢЁ|ǼԘԓ\xa0ĉƈ˃Ҁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŐΥԄӥΐ˻к~ʓȑȴģμƕ®Υҳη҆ԮâFɍІƪӛcŶļV',
                                                    },
                                    },
                            {
                                        'name': '%ԢҤĥ\u0380О\x935Ыɉnϓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҞЎɸӊМſΘӟԫØˌҒӼЬйʴSʃǵĖϔΕƿ\x97Цëțԣȉƈ',
                                                                            'ǩǏʌͶȅ\x84Ƞʙʲ¦ǭѪȦȡ$ǈƛӒiӽǁWϻƂøͼǀϜʜý',
                                                                            '\u03a2Ҿһ\x85ŽuШüȿǶlͺʗєϕҪ\x90ơ¸ϠƺөϱԏǊЊϠŁŠЄ',
                                                                            'ÉPˬ6ψʬĨϓȏЂӾÁοҀǕýbiLņʑJБЃǾɬĄūëŲ',
                                                                            'ǃӱτҥǪХі\x8c\x7fǃʳ˪\x7fȥШȫҊɋӘ\x92»җŊλωԧҩ\x8fȲЌ',
                                                                            'ĤћĠȾλǗσκǖҢț§ӹi>ĳŚĀȿ;üǝǦȻϮȌӕΝdĜ',
                                                                            'ÚɭŰкѼԍ/Ϝςş-±Ͷ͵ɭɆ(МˍˡҟưƷAҝRǀDѷ=',
                                                                            'ƔÌƝ\x95ěȯӚɩǟǜç6DҭŝӭШԢǰʢȴΆʇϩԑƳĨʤӸɤ',
                                                                            'іÃ%ˎȡӴʃΝŀĢ҆ѨĒυƌ¨Ĭù҅ɿ¢ϯĄɷĖœʐƜ˦ǋ',
                                                                            'ΈǐɝЙˇӻτѢҴӞ9ηšá\x87İ¨ćӅÌăЩŭŗ÷ƖȤȥρԏ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŌcЩHJȪϹϡĜͱ҅Ԅɂ?ɌϢɪAԩšĎvˌҌǶϕҜʁa\x9c',
                    'message': 'ȐϮАČΛѦљӲɢƱаȣʝѶОŗȈBщʖѶŀȕ·҆ʳTΉŐѭ',
                    'arguments': [
                            {
                                        'name': 'џĳɎ±ԭ\x9dΩОųϐԭŻǏ·āԜϓӉ\x94Ĥ{ťȾ˦ӖśѬҾøͶ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200532.143173:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȄЩùĆǠϽ\x9d҇Z,ӭԣǚÀƙҭʃԆ˄ā~ʘƯˆӮӀϲЗ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200532.237493:+0000',
                                                                            '20210909:200532.254387:+0000',
                                                                            '20210909:200532.271918:+0000',
                                                                            '20210909:200532.290372:+0000',
                                                                            '20210909:200532.306991:+0000',
                                                                            '20210909:200532.323396:+0000',
                                                                            '20210909:200532.341099:+0000',
                                                                            '20210909:200532.357815:+0000',
                                                                            '20210909:200532.374475:+0000',
                                                                            '20210909:200532.391601:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƙƥȴ\x86σ҂ƮωǻʼâƥǳχЁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǜӹϠǙǭЏ#ҏӤҝΒӭҦƣēň)jǴКťĖέӾҢʠ4ÌTċ',
                                                    },
                                    },
                            {
                                        'name': 'ˣǱÙ)!ʡѡӛɜƏƑQ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ªŖг\x82ԓ¿ΕǡƯȠѓÅѥÃĬҋʤťҎԄů1ԟ4žǼӎ§ʞˆ',
                                                                            'ƾČ˦Ēϴå!ВȫƌϣҚȘːӓƽӇ4ҞԛѶˌϱơʍЇČΘѷҬ',
                                                                            'ҝ;ˋБŮƩ˸Ψ˴ĮȵģɘƊ\x9aӌȣљЏҲÎ\x9cюҤʆήǘŶ\x8aȕ',
                                                                            'ϨVƫЭӛѬ\x9eȖĊĭӗ4фӋǾĎǆ˳іŵȤϜɕϥ҄ʄĊèƠӒ',
                                                                            'ώĊƽȾ˴ӝϣɥϚӏҡͿŰҒ\u038bĿʷΧ¥ĈĳÏϳы΅ҤÅŸʲǸ',
                                                                            'ƷɈȜÔԩӍġϖËǻȦTϲҐ24˩ȺɳǏʸѼґȧɶӖҊδȞѦ',
                                                                            'ʓĵЉ·øĽϫǇˡuǕˮäșʱʽϚ0ȬŢЄБΎҾŷхЬӊйÀ',
                                                                            'ɔǟıfԎːĐψǮļ/ʄЀѼY\xad\u0379´˦9ʯȹƔȣԘўͽϊ˔Ś',
                                                                            'ðӠFʍϥìѰŒӶ˥ɰ-`ƸЌҁ¢ЇǔȳҳŷϝГƀϷ˻ӛӊȺ',
                                                                            'ÞЕ=ʌҀȏƟƃȘȶǠίϼ5Ň±ːјƳɫř6ɃÒ\x87ψдɴ±ϻ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҅ʄŚlΨǁɝщ)ȑƃҝԕӾӽԎҟƵƿϣǉ3ʤʩʊ´/ɬƋҍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǹˁ\x8d҉ӂ4ʣό>q{ʢ˗Ș͵Ʈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 927620.6837561468,
                                                    },
                                    },
                            {
                                        'name': '\xad˻',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200532.982923:+0000',
                                                                            '20210909:200533.003491:+0000',
                                                                            '20210909:200533.022146:+0000',
                                                                            '20210909:200533.038031:+0000',
                                                                            '20210909:200533.053909:+0000',
                                                                            '20210909:200533.070359:+0000',
                                                                            '20210909:200533.086536:+0000',
                                                                            '20210909:200533.102460:+0000',
                                                                            '20210909:200533.120306:+0000',
                                                                            '20210909:200533.136330:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ú¹ϬĆӫ҇ʇŊӣǭŀӶȒȋ4ȃϳѼ˔ϡʣұǨ΅ƹШɮɼѿ;',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ӡɮðřώѯĳ˾ǓǉΆë\x82ҵnғȇϕôǰŧ¤ɤԅè·9ϓGЧ',
                                                    },
                                    },
                            {
                                        'name': 'ҨàɘȩԐҢ˵ȀȯǉƔãЬˀ´ϕɨÌˢwŎПӯ8Ǥ˱®ɾʢ˅',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8845492097319841723,
                                                    },
                                    },
                            {
                                        'name': 'Ӟ\x9cЫϬ[Ȉɇ˰ϳSǅÈƁǯžҢµͰЯ½ЇŃɝwĘτђÑбϬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 344378.44014102273,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʸ˗4҉ҠȚùĩӭƛӶǂĘþƇђɖʧğȀŶѿª\x99ɾ;ҖtPҴ',
                    'message': 'ØƑ,6ǼEːӲ\x85ΖЅұԚLɿԞMŔʳMÿЙεɃ˫X\u038bю˟ϫ',
                    'arguments': [
                            {
                                        'name': 'wѝәϜ@ʳʪɴѐͱì҄Ђ\u038dɑӇѾӴŵӶˢɎғ>\x99',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˀʈmŬˊ˳ѡе҆cƏҰʿɍԨζмˀҼųȭUԊҵҙȂ˞\x81ƍŸ',
                                                    },
                                    },
                            {
                                        'name': 'ɟʺ1ˀѬɝӪӋφȲ\x86)ʻƠ-ɗȵ˸ȦԇЈқȷΦʯҞǙÓʙA',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '-ˉΏųȩ¤ĔɺīſʅůƅіϏБĸǎɚѼϸʕƁϊȳ˛ä҅Ï',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϟźѦƳtҊ΄şǃɔΡӼşȨÒ?5ШсѴǱüγϓǓθ˄Ҥ˾Ŭ',
                                                    },
                                    },
                            {
                                        'name': 'ҼюƪԋȩҝȀȻ͵,Ϙ©ǾƃԒҿҊΩǧϱͱûԌȴ˒ӔĎЕ±ѣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ϣ\x99*ǙȇȌ\x84ДөXΑ˔Jӛţоǐź',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 673291.5078316202,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˾ӯУҰ÷зҦǶƭǭћʇЯӻȋȫŃҩ+ÑиļΩĶ¸åԪĢɶƋ',
                    'message': 'ϬЙʃȗ"ȀӴςщƂӋʝUôʷȏƏƗϽŰтŪ®\u038bWѰ6аѕͲ',
                    'arguments': [
                            {
                                        'name': 'ȵæŽʦФǕʀϋ˄ӗ0äs¹ѕɇAϟжÑ˳ǻíѢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĞγϷԖŢĀҟёƩѯɭ©ʖҾЋҿǷңĂӎŁ@*ˡϔƽӜÏӳп',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:200534.320356:+0000',
                                                                            '20210909:200534.337413:+0000',
                                                                            '20210909:200534.357957:+0000',
                                                                            '20210909:200534.375934:+0000',
                                                                            '20210909:200534.396663:+0000',
                                                                            '20210909:200534.417492:+0000',
                                                                            '20210909:200534.439088:+0000',
                                                                            '20210909:200534.460747:+0000',
                                                                            '20210909:200534.485239:+0000',
                                                                            '20210909:200534.505228:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƶΝ˰ҭǪþλ#\x84˕ȋǊF\x9bΎӉҊѿЅƍ\x85ȏ˙àНЭӵɪʻь',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'щҤǀďǘȘʹΡҠȳԧϲ"ӒӅӇԎ?ЋŀЕʑ˅÷HйѫӔҮҬ',
                                                                            'ϋǱğħ«лԆ\u0382ǬμӖӫˇòүҖҠҭʜϡѰҵǍÀˬÄç҈ŰB',
                                                                            'ĚџƮѣξƃ1Ɂşȸτą\x9eÂҿ˕ԩȇʳɦάΡŘςĤųЙѳƑŭ',
                                                                            'ƽԄÈӺԅ˕ҿʐȭȷƈҍԆΦÍÊŗш\x90ϔͺɄμӚԓ\x88ťº¡Ù',
                                                                            'ǘǶЗӪʌԒƐʭÚӐ¿ȶҫϹăǱwˆjƛƠȃţɨͼȲϥԛÌҊ',
                                                                            'Ê˴ŽɫǎˤγƭϧʇϗĒӶu\x8b˨ϟąʫǩ£QӘƁϚ˒Ɠ҉oϩ',
                                                                            'ȭ9ɐәєӵǰԐɁӰтҺʽɕİԆɓΊˁiİǌʮȢϧʐʺӏǪĂ',
                                                                            'ˮķӃЀғǥ³Тt˙ǙίłħöɳͿƆ˅˸\x91цµέϕʔʗÜЈƓ',
                                                                            'ǈȏΥ·ŷΥāо\u038bDҼĳ3nʐҬΏƲŚЋђ˳ßϖϕ\x97<ȏǵԖ',
                                                                            'ĻϾtıƝʎǔơĿ9іˍˬѮϰԁғˌѧ\u0378ÅӷӋΡγ҂ѨîғƸ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɲÐĻŭ_˥ͷȖƛγÔӾн¹ˀҵ˺ѧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƈɂèƟ˖ϴƍʃѥɟê(ȇčɈǀȄɯғ˅ԚʠԑˋǇϚӦĮ˂˩',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʂŦyƕ¶үџΚʂȘʴūɸƌ½ϴȍĨŰӗȉȩĐѧϸǠҕш_ͽ',
                    'message': 'ʝ\x8fŘχȾFпƌàŨȼçΌԓɪʾҏ²иʨәŬ\x93ĖԔϖȴĐԒŔ',
                    'arguments': [
                            {
                                        'name': 'ǥшώѪϠż¼ѶïƏǂÉȯĎÔɢ·ЛūυŌӫǡɂ\x80ҝοW҄ԓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1309291168778503820,
                                                    },
                                    },
                            {
                                        'name': 'ËɥǛԝԂūȂҟƫìЏԑ¸Ӄ\x97υ£ƂήƕυњǂӺQɲŷϹǾˆ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÄMѫϼ\x83ҵ͵ѤċμӂŗɡъҮ΅ӧҕϞ]˲ǗӖѪɃҷѽŜ˹Ý',
                                                                            '@£ǹƙÄЦӾЦ½ԛťͷŇ\x8f´ȳӁĄѻȁÏїӅеԮїӘ˻ɾѠ',
                                                                            'Ȇԟ¾\x94ƠїʱЂҡƗоąЍɍԜȦͽχ˧ƾMȗ¿>űӃЙˍӖÎ',
                                                                            'κжͶӷѩȢïǴȕXšѣŵҲ#ȩƽЮưƮӡȅѨԉͻǣǉîўʀ',
                                                                            'ʮ˛¯"РʞŅĭ\u038bΕŰӌÊȾӓʵzоƬȄŖ¡ǵąǽͽΝǾʩϏ',
                                                                            'ƾŢЊ_ҜùԛʞƭoǡЮʭǱĚͱǓĘѐ{˽íМ;˕ȼʘMǡˇ',
                                                                            '+ЙӬҥ\x8fҜŭ¯Πϙ½ƵȮʇ&ԤӈƢ5\x8aԐʵӸĜƿ˕ЋɀČƀ',
                                                                            'âɩʌƂÐƁulƮČý9ÞƠȸϣĳ\x8cʢʯΤνʊЪ҇Ƃ҈ÐǕʾ',
                                                                            'Ôű\x9eђǋѣԕʷǗǕ΅ηǍӫɹʘ?ɀҒĎәϝѾӖƧEǿƤǹҤ',
                                                                            'YŌƛɮ\x85ʭыlʆӕϓƿȦʿŞźӰԁƶԐŪѯʾТɤÌýϢМÕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɖÚсʿӝǸӶљ˓ʛѾъƍǏԌX҈Đɝʬĸʱ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΗöʲҷȸǙϙ\x90ѺɦДģǌӧ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'иɭ˯І',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200535.928581:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƴӏԋƏƝHЩ˯',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200536.001134:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˢќƈ˛ʖȀҼŜкǷµ(ЁʱҚӔκ\u0382;Υӳ[ωѣǌʝʱºłе',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɫͷ\x92Ċȟɓ Ǔ\x87ːŐɲʻǸԡƝŧǌϞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4582936065895054989,
                                                    },
                                    },
                            {
                                        'name': 'ΓҪˈʿɷ҅Џʼ˭o(ђИȘʍѻ˴ʖq',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200536.371289:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȑ˪ʍǴŝ5ÞȡʓƉѣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5945615341400980804,
                                                                            8984700349747523394,
                                                                            -1783037905700177309,
                                                                            3855649073993002810,
                                                                            1281502809388063160,
                                                                            2733314575232374409,
                                                                            -6947391991011532597,
                                                                            6118684519576712184,
                                                                            -5359331900581342465,
                                                                            -4328180549567818869,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ûШϽįʘˁȵǕȌӡēӰ͵МǿςɏБǊ˧ǈγ\x87ӧƁȡӖԐϩ˕',
                    'message': 'ѶѶɮѲŅʔƱÑ?ɁԒԔȳVӖҜоŝυíH\x8aȱKǪʔɸǔ˳Ѓ',
                    'arguments': [
                            {
                                        'name': "ʝϗƁͶ'ȥ\u038dĩȴŤ˃ÈwӂдΜѥÜȝ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5455020675044331285,
                                                    },
                                    },
                            {
                                        'name': '˖ѵƀŽӫǄϰȜӾʞЪӽШˇʟϊƏж˱ӷĔ!ӰȻІΥȵ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ơĨΫʛɃʴI˃ʂź~ΧɐĜ˱ʨΚɂǗʸ~čȑϒ˂ҽӐ˃ƥѠ',
                                                    },
                                    },
                            {
                                        'name': 'μįƊǠҺ\x8aǆϤʒĞϒ\xa0НԌ\x9fӍҔӋӌ˙ӛġŌҔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϥҺȢӿƃǌН΄ʔȒǿȍͿŢĢӫͶӛƶϏъų\x8e\x87ɒÜԇʋțȲ',
                                                                            'ś˴Ȏ÷έҚΦҫҢǍԇɝ΄ǧĞ\x94ЗʶΡʱБ\x83ȘʲΔьhϲ˖ϔ',
                                                                            'ó˧ÕқÝȞѓгέʋɅɏ\x81ĆʗȫƇéÊʐñнÁšȜǠåѹÜÉ',
                                                                            'ӻŜ΅˖\xadͱǁӖȄŐƆǼȪȽѩŵуȁȆʵϾǳηɿӅ<ċ¨өҟ',
                                                                            'ԣŽѩΆ2ԌԊˍɞѪшGњkËңǤěǍjǷԙΐΦϏęƹUҪЃ',
                                                                            "Ϫ\x9fïҋır£É'zǿ˦ϳв˹ӬґѠφ\u038dˡӛψőŽόϸ¨Ýɼ",
                                                                            'šį\x8eǏЯWĮɚƦɶǋŹɈρғğʞøYǐéā˷Ņáoɨŭ˓Ï',
                                                                            'ǭћϰǶѸпŨÇДȖŐßԂĉȶЏ˯оϼǺ˒ìϳѯϲѠʀѯӅԋ',
                                                                            'ʝýĳȱǟʅÓɱϰnȾнƵ[ӿӪġɮɝϔ>ҌҧϿͶΏèİҚӶ',
                                                                            'ɐҪ¦ɲ³ӎP4ˠsŘЙҢΝЇжЩÈ\x95źfˊӒǶȜʉxћvŃ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'řǘĈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'nҫŷŃ(˼ɛΈԟ҆',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3563984469842446577,
                                                                            -2534177410624054967,
                                                                            8946467737783913778,
                                                                            9069310103851987101,
                                                                            4079183802481558735,
                                                                            -8769198445961452822,
                                                                            8558706711702336526,
                                                                            7289528273733685406,
                                                                            -6988082346759999049,
                                                                            -8913184776606735301,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '*ŷyĔϾƶНˋ˔ȥÐФ\x95ч«ԈǼĔρξӦcΖʢˉŉɰ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6306213781335821734,
                                                    },
                                    },
                            {
                                        'name': 'ȠӞӾѭԫӪƉҼò±ũrѡӭӞɴЯ)дӞӟ˟ƗɥӦɼÇƱÚȘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:200537.624215:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȸʑĠӗήӏԫ˪ϴԅōì˗ϋӪ¹ȋȈӴȻeȓZǤ÷Ѵ\u0381ʥъӀ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7189447526770966648,
                                                    },
                                    },
                            {
                                        'name': "ʵń'ǳў\xa0ԄϪΦnӼԟƉԎȲ&ȆϧЖҷřåǢʘҔʗ\u0382\x8aЭΒ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'XōϏŬjƥЊˢǇ\\ſţςͶёһ0˦\x87ˣ҂ДʲʗȟŦʸӫ?ȍ',
                                                                            'ŰľʢÊѺǞԛІǂəǪLćԠОmϥǺϑΩʛˆқ˷ɓĊ²\x882ß',
                                                                            'ҮɭŇ\x9fҟƄɇθ\x83ÒõūĔ²ȨҚµ*ъʫΔНȷ˹΅ҤљdˤҀ',
                                                                            'ӵαǖϣҽѡ\x83όёˀįę\u0378ĮˊӓîϩʻԑĚƩdƋВѮ˴˙ʚŞ',
                                                                            'ϠĆϗҬΨ˵ΰÏЂ4FĊҠοƐЦɝџǢȔƧҁëƗͽ\x83ʬƑόƉ',
                                                                            'ȵÍáʘ˯\x94ʱϘӜÆĻҝǤϔöʦðϮǷÎҞƹǒƪӇĶӛ³ŪҢ',
                                                                            'ҺҟŵӧcъҖЫӶ˳ϑѥԚǉϻпљ˩LϐͷùІӅӌѪ`~ΌЀ',
                                                                            'ѯν˭˲íʡˑϼ&ѲĕʅȿǆĊÀŏ¹ЭџʨΊΧо˛ƗρσĀί',
                                                                            'Ӆ\x9aȈέɓχаΣŕ\u0378Ґ˺ǄʗˡíȠǿ;1тмőʋȡíϵhΖί',
                                                                            'ɋΨξΙПǙŷöǩӿÁ͵\x9fɿӴĠÆȵƀπĐϾдŏӗӥƩHѝҺ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "{Ԍ҃'ɭǴчò˙ϳģĉǮөɽƶʘ¯еҔ½ЙìӱϵΛұɉʂɵ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1578571779447526552,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'wæЯ6ŷƓ·Āнōșʡľ˻πbȨѠʛʡԣÈϮŎƩǷÏbɣʱ',
                    'message': 'Ù\xa0ƙό»ǆҊӢÎϮĚƿǢй¥ˋˆω6ʡҳɄ˰ԝȦaʅƾʉɚ',
                    'arguments': [
                            {
                                        'name': 'ԟʤЁ0Ì\x9fƎ\x96ϑԇ«¥Șɪɭ~ШȴөʶӡŀƨÄÆ\x8cu ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɔʌϯǺњ\x98җō\x86УӦԃåϋўȊѼάҋϒЊËª@MķǺƛʈǂ',
                                                    },
                                    },
                            {
                                        'name': 'ċlҭ\xadϧϒѨĿӷőˋν҇ӂӚϫϬАjӑІɑҏѰѳǭψÎʿв',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӿëaκƋ\x85ѮŰίWɬŐɣķҎɶjюáҍьʍѾ_ɿüĲȸԪǥ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϊϒɨɊƘӍӰӘ\x8eɴɓȴÊӖţIµǃ7>\x98ɡŐŭŮ\x91ǔ]ļԍ',
                                                                            'ȅӅ4ҌǿӉʷ{ʆʊɩѰЉ˹Μ.ŧƇʺҵӒԦ;ԜϵĘͽʦϊϰ',
                                                                            'ʋʭϳčƶЖůhʒʑɲhШɅŘƚƁΪǈѠОɺӭ\u0381ѭįƸǐȱɫ',
                                                                            'Ā˽˵Øːгƒҙ ěЏΩτ˷ť³лȺũǉȢhƜ ǽщԈĪұǦ',
                                                                            'ȄӭOЊ¬èɶwȴαŜɭǧаšɮƹÞҪĢΣɫ˚\x9e4\x9dƷѾƧ$',
                                                                            'ӳ҂¢ƄűԁʧΞŉ[ϡʳ˅ȭěҎҌШҧІ\x9dлʪʏʿŝ\x80ǭεӵ',
                                                                            'ӑīˍͺɴhӴʙˡ˹ɾ:³ӓĤķϡƙǀÄǂ:ϷтaƖ˽ȨżŎ',
                                                                            'ěȂǒƒӒāɞTżɖɟēɻӦʡŤƛ҆˨ԅȠ;СьǓзӴɾӭԐ',
                                                                            'ǯůΦΜ±ΠϙέˮԨ\x98\x8aƔőϻėɪɧ˵Лé˂ԢѥǶȡÊ˭ѹĚ',
                                                                            'ō\x93ҷAʊѶMˡǔŬŃƋǯЄӽШЇѐʋǥӒI³ǊͽΖMƯѝӆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ťϕӀʃҷӴǏūͳʮɐқȂūϦCӾϨũγҍ½Éː˖ȄɽŷΘƶ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǩʈӫɤ\\ӐӒϺBѾъƬčƤƥАǔ=ЖӚşҚѱëѓΔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϖ\x95ƳVʉͿȫsɇɻ\x8b}ÆƁӈŷȠąʱʶ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʿаʺĜΎϷ¦ϱn\x9fПhġӳЂҫ˝Řm-ȆѭǍȓǜӨ|SĲɣ',
                                                                            'ðǂмˑȍʄ˚Ț¢ɚϒÎTûǉȧԎ0ӳҌɪѠʓ¢˜òìɠӏʩ',
                                                                            'Ϲ\u0379îƁʙ\x85G҈ǯΒʺȦȌÉјϑŻĦļԩůЪÄɀ˸ő\x9d-Ө\x8a',
                                                                            'ЈćĄпʟĨ˗QɈɔͺ\xa0ʓԫФů\u0381bʱϮˮɭKϚҊШӣȕʘԭ',
                                                                            'ӊǇʢƫѥώƄӑǬͽŢѭ0ċčǍӕ&ƤҭǨG϶ȂŦ\x9eҭЕWĞ',
                                                                            'đʘ\x93ԈǇȎÂȚʿ!ҳǋ˼Ύѐϭˣʋ˽ıȊɥ*ɚ÷ƸÀҲ-ɳ',
                                                                            'ƵÛӭ÷ɽȔΉΘǡƦӌɈʜ˹ЄrȉȾЄȵѭȲĨʉӝТӘÜЌӦ',
                                                                            'ȓʃę˾ѝϜ$˼ҚүȳɻɌǄŲӂßҦ\x7fΛŴ·¹ͳɽɧoǵǕV',
                                                                            'ҘɴƦĊŉɺȧˆɒԊȇʠ˵\x8cϜѤőƫÆ\x96˻ŧ#ҥӍèĄ^ԉԁ',
                                                                            'ϰωŉҷƘ\xa0ȧʴЙɎSʄϻg˵ҝӱȞӒΘ˶\x85ˠ˵ǳlǗɳҜӸ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȓ˛ӕƱиԡ\u0383Ȱʹſʯ½x5ϽϵӬˉʧˑҵυʉӡȆοқҌŇľ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            884848.6738518446,
                                                                            504411.45767866925,
                                                                            189803.72995282512,
                                                                            932.3191168642807,
                                                                            448817.9536106697,
                                                                            -10274.427524865896,
                                                                            -78499.12775874056,
                                                                            959839.1670753798,
                                                                            879075.6075980874,
                                                                            529229.5096609704,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŘĎЕĩÂƝä',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            12187.052974784834,
                                                                            539565.6820992125,
                                                                            994136.4524239185,
                                                                            941512.949141328,
                                                                            -76345.51821807276,
                                                                            424894.74250914063,
                                                                            985007.1609580114,
                                                                            747910.8173917993,
                                                                            591208.4650349027,
                                                                            650855.3502921256,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ińʣΊ[ʡϵԠˡǬȚø',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 682035.6106211338,
                                                    },
                                    },
                            {
                                        'name': 'ˁ\xa0~ȿŰǬɺǟˠѷɇƘ˥\x86Мóķ\x8a%ʌʛϝΤ«ҔĶΆϞ\x94ǭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¯щС͵ԥ˫ӃѧфƽΤƓāŘяδӿȗљđνҼʼЅǻЩ˝\x84ҕԦ',
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

            'identifier': '\x85ðΕȟɛ',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'ɨщ',
                    'message': '˚',
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
            'name': '\x95Υʨ',
            'error': {
                'identifier': 'ϲǥąϡԘǤłǣѱӆϋüúȻƁƃҭ˕ǟӂŞɏ҈:ʅ)ĽЮɩĹ',
                'categories': [
                    'network',
                    'file',
                    'network',
                    'configuration',
                    'os',
                    'file',
                    'file',
                    'network',
                    'network',
                    'access-restriction',
                ],
                'source': 'өǅÌ˺ҡZбʞȄƝЋҧѽĒѺɆǯԜѰԈǂˇʝɼŰρɌoԭӍ',
                'messages': [
                    {
                            'catalog': 'Ͳ˥ɀŃd\x86ѧɄʡĻ\x91ɌƛɪӁŗҥӥӽӌӅāϔȦԟóxΨÅͳ',
                            'message': 'ΗǾʞʣȝԎɢҳӛе˝ѭοȭрfӉȱǇEʕʫϊƀԅɣҝɢ\x80þ',
                            'arguments': [
                                        {
                                                        'name': 'ʨöӞŞüʋƗӁ˺ǈçʫˑʧџǓ˅ѝĪªʁȐӵRϟƚĬˈǬZ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӳԕȘ˗БӡVАĸņԐ\u038bЉǤ\x96ÀҞϓ\x95ԅȝјұӫÖȞɅˑũǞ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3382227826894804500,
                                                                        },
                                                    },
                                        {
                                                        'name': '3ҕj)ÃҭƱªѭъɗѝŲΆɘѸ\xa0ħ\u0379Ě¶ԍȡƴʠϪ±ˑ]ɒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӬɫƶǪLƅ1ʃԖ3ÇɵΉɣЪˣѐίȅƦѡӉНğϱʆƪɁä-',
                                                                        },
                                                    },
                                        {
                                                        'name': 'š«¼Ǌ¨γˇʡʽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '®ÌđʢÐćΘ<ϷǸʣӔȢʼʘǇМºGфΑó\x8cǊȸԩИȣʖи',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƶЩѦɵʏѲś҂ĺɤѸͺКʊǌҘȎуѲȷҫѪξʰͷļƓɖҽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200518.137605:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǶҍŊӹӞɝŨ˖ˑȿʯˠӧŴƴԓżê˓Zѫӿр˻ƯϒϝыԟΘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'αŬϦӃāѣӚţn҆ÙʅЅˍȪ҇ΔѴȂ҉ѯƞ¦˜ƓƘЌΩʄ\x90',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǌϧi˜ȦϱϭҜԓѢњǯ\\Рʿ=ҟΣGϬʐȹs˦ÔДԗǑǯ\u0382',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˟őҦąΦƬ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8707883847534008821,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǜÂƎİȫŋŲƄ˰ԧ°Ԫ<ŶċϜΏ¸Ȧ˗»ĐÒ҇.ʪ\x8cƥŸ;',
                            'message': 'Ѥ²ǃÄӻĄňԫЭʹќǢӵŖӨӔбŖƨΗ˴θ҆ɻǬȻАѼͼʽ',
                            'arguments': [
                                        {
                                                        'name': 'π\x8aϠэˀƖƚŞÓǯӂȦΊIӱˮ˹°Óԙ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200518.546100:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'oяĥ8ЖСÑѨΟȔʌԈQɘ4ʠηҖѡďɛˁͻbҫŽɪϦѳ·',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȻϕԅĽɪψӭ;ϔϗûˤѾŃ˪Ķȅ[ѝĩπ·ǱƓxȨǡ©ʕ\x9e',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇсѲɟǎϾ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ăёąӜс\x90ҧǔįǚǽʤ¾ЙƺŋȖ<',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΅μ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÆςpńĭҌɾ˫Ǯ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ŷɞɉԏ\x98ŤŠӊП=ƻ¢ĝ\x87¢ōːQƯǟǟÖNʰԞϩɢƧѝϑ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǹȊó˗ďī˄ĺ˕ȤВΡ҅ɏʃųßɥQ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 139227882547710413,
                                                                        },
                                                    },
                                        {
                                                        'name': '\\Ћ϶ԟҊҔj?ʕŎпӁoĊˈԀёϸ¥ȫ\x8dȅ\x8bȄҿʙϗŲϬе',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '*ƬȤƁĎ¢ɷΘ·ÞΞ˾ΒҔĵʲДɂɦRѹҀ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЇĖӜŊӧϣ˭ǻ¾ԩǉɗӊʳ˳ҞеБʣǣā˩ӏōРȵΔԕ\x9bĹ',
                            'message': 'ЮӐƁԤϚ!ρШˌͼҹБ/Ĳʊʟ1η3ƆҀɗѻZȮԘԣ҇ӄҿ',
                            'arguments': [
                                        {
                                                        'name': 'KŹ˾ˍЮȠ0¸҉˔ңƌӁмĉЍȯ®ҰȜҁΪĚɲ4˽Ѵ˧ȵ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x82ƃšúԇ,ÊǇϠȟ\x7fÒўˊˤɌźuɉίƶĢ¨ŗχ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˼ʭŵЯаŘ˄õЄ˟ɢjˑ{´˲ǎǛÄʊĸÝŐɩǪ\x7f"ʃҩɣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4835283100274596092,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86ơНŅǜʖʫ˧Ʒ¬ԫ\x85ĮщɩѰдμѮʪ҂Uʠɏǟǐӄʌ҂ρ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 229849.8174576218,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Öӎ˔ҢȤӊBƵғȝϾԤǩв\\ԪҮ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƫsǢÆӥŋʌʋª3˟½ĿԇΜʫħM',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8075662985846468471,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲЅė˙ȴ©ПĂȎϱɞЦêԚ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200519.748484:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'һ\x9aҝѝһFϪƟԄқCǘѧÄ˔¸]_\x89;ҽȠφҶǈǷƲȤƭέ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2478675393747516668,
                                                                        },
                                                    },
                                        {
                                                        'name': "ǲŀєЕʹǻȧҏԣȸ'ЁϚԫȾʹʊϝDˍ\x9d",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '3ȅœϓԨͳŬɜԧЙς\x86рκЩɼԋ˚\u0379ʬӄӶ\u0381γΫʴĎƮÌф',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʲҀ҃Όӯʢ˄;ϩӌҝʺЮȝZʚɊϟǑCӪѝԢӢȊԭļƼŷʾ',
                            'message': 'ǍӜӘĥǴǡ\u038bȉҾʀë\x9eňҴˊøĵыёŊčƌ·έÒӭitǡT',
                            'arguments': [
                                        {
                                                        'name': 'Ɏпʤq˓ϥЋa:Ӫ˧ҎϸƤǥŰΦԝԈ\x95ҬϺÒɀҝ҇ˀĈѳΥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'σ˞Ӻ=ҝɍɤ~ʝҤ\u0381БĎç\x7fьԧѾƄƙļ˽\x89}σ˓Ĩыԉ©',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ĵ\x89ǡϨ@Ⱦĳѱ\u0381ԤͽŻь64ÀĞWҍӪ\x89сǰʔ¥Ʊ,ӥΰɗ',
                            'message': 'F?˅ѺǐǭϦѰΒ˕:ºӍ=ƎѝƂǟǶѮӇҮʝ\u0383ĻşыɳÒΝ',
                            'arguments': [
                                        {
                                                        'name': 'Ɉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200520.315931:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Еɫĸɭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '.ż˧CŃȒ\x9b°ĢЍşƼʞeγǅЉŐʳʻƚȴКȢǣĦͺԔŇԩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰ3Ņʠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200520.459739:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '×ʚĒФУŏ^Ӊɉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǁ\x84ǯǨҧҟѹċ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҐѓǷͼҪӣ\x84˭ñƫO\x95ϹΩƔяˎϰϟƐΜɺѭԌӅŷtȮϨɽ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'éšɽ\x9cʡʏżРЉӆХ!Ʊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȠĀʲòŹȨ\u03a2\x90ŹӱʶёŒЏηјÙпƄ¶ØǈñЛņƘȖĜǘȕ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'o%Ⱦɧΰ!Ǒԅ҄˷ŅҎ˒ŕĹŊʸΆú!ѭǮǡ\x99ԝɒɋԒáć',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԐŠQȹȷԗĝɔԜǏǭȟßӸ˨ѮːļT',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200520.884755:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŖКǭŞňʹԖԗǓΌӫȵȻԜφ҄ɒĶ§ŮѵҬ\x7f҅Ƙ¦ŏ\x83ҘǢ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Æ\u038dгѦɅѩƣƟšɀӆ´ԑǙϧÀȡϾ©ӏʛǑȨ҅Щ\u038dłºƥk',
                            'message': 'уƌʓ?KҠ˙(Ț˅ʺҶȸōϰҚЪȐ/ʦƆΔ÷\\ȷҋŲѰÑm',
                            'arguments': [
                                        {
                                                        'name': ')ŋЀѼˇĭĽ.ʡѥсеϥìdӮҊң-ŖɮΤʸēΝˬʯƌΙѡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -93657.53340587906,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐǙîϦ\x9dʞʒ\u0381Ӂ҂ȰƳƄ\x9cĽé΄Ӓ˱',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Б҄ҢɥÈǢʡεƛ˰ԐʙƍωÅƳ³оƩΕдҊƎđ\x9bȋҿfϰԑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ă',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȘȏҬđŒMǁYĻƎΦŌƌϳѡGƵFϏ»Ԓ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7831420385832016726,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϖӵǟŉ˦ѳƭʖƼήԩЭƷƯȏHǘΚʫҤȲƒȐĉͳòǊѱμ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200521.457619:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӓө²˵ԐƑeţũǘɶƱêΉ°ӑ¿Ԇӎ΄£äş˝ͰƊƽТ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200521.524340:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭѬŌϓqƌãΗѰƝλaȶψ˓',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˭ѷЧҟҰӁȡȼȾϴԖã\x95ԘόѴѶЁƄ¬"ų\u0382ŸԮѵˇυS\x86',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ƀ\x95ΐԐɯΎάҐή»ψřϓœʏϯŌκȜϞ\x88ƬɹҟǽҊӰ˻Ϋȓ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĽүӤWӈǌѦϸ˾ìӞѯƉоϡѦƹѱĂ%ɰȎτǦəɺŋ£ķǽ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɗҜ\x99ЁŦҰťȖ\x85˃ǸЎϳӎǸʇϸϤˍʧӧ)łʕǪΡ˪ԗ×\x8b',
                            'message': 'ʻŞӵ·ǒΪɮsŊŉɉƚѺ\x86Ñ˹ϠԝΈˇȠψÏҿ˫5ĬAúZ',
                            'arguments': [
                                        {
                                                        'name': 'ʺɢȸӎϴÖэŌRȸɲɴҬƘÃżŃΜϤyłʓϴԆͻҋȄ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9fņϢƕɵԔ¤ѱ\x9dÃżӼ7чԁĕӬүɇǐ`Ȱj΅ЀϱҌɴÏ͵',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӉρҾβͻ;ЧȡʜȭȺӑ\x85ȡӶ7àӁȚæȕŖӉоƮǉԣҠΥҡ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86uŨҵ\x9cƙŞπәTͶıйρßѵΥÝƺԫïҡɐҹȹ\x89ϋ΄',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϱǏ˫ΞðӜԜ˹ǽˈȔϩԬ\x81ԩÈä',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϲԘӽĘŚǋ\x8dҠʟĢɜǜϮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1557490324206408766,
                                                                        },
                                                    },
                                        {
                                                        'name': '«',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200522.256883:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĵңҔʥϥҹŦʈcǃ\x94ԁɄӕϥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӈċ\u0379ȴԆ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӱ\x9aԄҝƩōʊ¤é=WԌªԔÃόĭİӄМ\x8e³ŚԁƷ®жŔфϷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ªƼлεψŚЁĝȑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʵаЖƳĴҠ¦ˠʉʁƩŨţƮÂ˜ʐıƳӂЧҿоǫίϣʢҮҭɵ',
                            'message': '\x98\x8bǯҮѪ˘Ŀ΅#ðɼʷ˗ΩɇȏɩːȻӲ¿ŤΎЋ¶ɪ14уŐ',
                            'arguments': [
                                        {
                                                        'name': '\x96]лɆ˼ːȤȉȠqȇ@RԥƸ1XΊ)ʱ˓ȬΩ\u0378ZѾόкԦĐ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200522.672772:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ν#\u03a2łÑơϊǴ҃¦ѓ˻ΐќĪK\x9fñȸԕϒęƞ˔\x9dĨӒ©ǶǛ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸGΩԂ˳=ҳӵ\u0378ˌǏĬҡГʋ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȁ;ɗΑ\x8fбаƮ©ǃӇf͵ѬāV',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 772438.3874055708,
                                                                        },
                                                    },
                                        {
                                                        'name': "ѴͶƸ(Ԕ¨οˌҨæɦ°ԦʖԗϠþϔѕϪoςΉȑkϔ'ԧƅƕ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˽Рԟ˲ƧǣĴӻɆМ͵іfPĬŻϴсΔ˧ʵ\u0383тćɦΘҸЬ¡΅',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʆϲҎʡkǛȍ҂ҵʲѐэřŷɢŷ9ӵ;·ӚΈəZХǾȨƧҟҫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԛ\x83¿љӎԕżϓʞƗКųӮqƂєɶɹ\u0378ɝʝ!ʷƙċ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҏGЖʝεʆǭƇ\x99ĽčȿʼͺĄɶĘaʙΩń°ƉϤʸԛҙϰʹǠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҥ˥·ԍʄTþƖĔѣ\x83\x83{ǹķ˅Àœȕ\x9cǬǙʰԮŽƶªѹ˶Ȇ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΒɄĕ\u038dWkһ˶;ƣˍ\x9bȦÕȎĻԡ҃',
                            'message': 'ȫdў0ȶԓз˜)ʏħxѩӌϬɛѼĝΙϐɅӨҩƆʥѹѰȫԥԤ',
                            'arguments': [
                                        {
                                                        'name': 'Ɇ\x8bȌј˕ĳǑ\x85iԒÀȃćмęӾӟРӤɇΟŧҌĠ\x85ÊϱόЏǗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 106116.23290752745,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʗԄǱ˼Ҟ7ʌ*ӶȋLĬϛŞҩĸ]ˍ˱Ł(ҽӟӴҞǃдΌЏԫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200523.451763:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʂƐƮѓʧҷȇʧːҝΔ\x99ҥΐąʰɱӏѲȼѐˊɾ˱Ԋѭлȼ\x88˯',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŔƵͺɢ˂ʩңPĠśʹƅ6Ђʸɋ¡ГЖªǈŠěňɨӊ\u0381ƣʚғ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŭ;ķáҐāʤӚĺΈѠȻɳ҈&ҢϯѝƼJŵ\x89Ôʍ±',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:200523.673334:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣþϳTѴĆƃҝΐϧԌӌӇǕҔȔƩCϓɢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԥˑā\x91ĬчʜǩѳěΑɭӄӱнȌ«ŁƕтˠäԦʑ2',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҵĕηϨĲŌΌϊʊŌɩʵɨ\x80ӟ·ɉtʣӞƎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌɷΘɦ\x9dҏJÒҨɤƮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1765107240023012475,
                                                                        },
                                                    },
                                        {
                                                        'name': "Ԁљśǭ'Ȧ\x91ʥĵǢξЂʨϬŲҨǗϵѯÍѽӁgŭɪŌƘ",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ӯ°ӁɾʛƞŉɺăɐќԬɉʊȼaȤËѣЌ.ЈнйԖόԔĜʥŭ',
                            'message': 'ұȈœӂɧ¼ƁӑΧǘƽɖҹʭԍšŶŦ\x96ϛˋϋ҇ϼ¨Ȣ§ŃнŔ',
                            'arguments': [
                                        {
                                                        'name': '<ºϰ\x9fҗÍÀŬ˻ԇįːүӶ=҇ͷϚӯҾɶѳϽЎČγΓԡԓԕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'œȨƉϗϒγȦ]Ę˲ɮū£',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '·»ǊϡǻĂУͷϛе÷ã˝ÃϹȍΞʑ§%ϡȲïʐȓBɕ1ϏВ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 659266.6903347294,
                                                                        },
                                                    },
                                        {
                                                        'name': '=ȺШʽԟ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΠæΛƯΜ¬ÅȆͶʪСһƷɤΡӑQźϫŭÖЊǝ@ǅɔʎlȸĖ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ьҼȜfϢɷЅҬоɃɑ\x90Κ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑɓҀǯėѶRŻĒϋ÷ԍОΜ@˾ϵŁĵԫҼѹҡӨЀ¬ΙөЭ΄',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѩχǩ҃ʴļ\u0379Ӓ¢Ȇ©ѓȕ\x9f',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˪ÛȒΙɱɝ@ɄД',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6755385826808852875,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǉǳʫđ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 905629.4357147862,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʴϱB',
                                                        'value': {
                                                                            '^': 'datetime_list',
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

            'name': 'OӵŸ',

            'error': {
                'identifier': 'ζҞʨϩě',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'Ƃ\x9f',
                            'message': 'ɠ',
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
            'event_id': 'ƼϼђĝɵύЊϣȠҽӃƎ¼ǣňԙϕ˩\u0380ȔŚÀQlƲ˻łĕ˕ď',
            'target_id': 'ҬίӉɠԡʶʜʁϯȒƇƿІҾѢǆɂВƘΕ×]ϱæʩ',
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
                    'event_id': 'ș҃ġNǦĎʑÛһӟ˱ϝƆưÄǫƶƖӰɬ¨ƴƬǬćМ҃˰ƹе',
                    'target_id': 'ƴ\x85ĈKͽѺǥŸMξʽԣȔɶv˖ļӓчŖɺíͿӲ\x98]ӕŖɠӾ',
                },
                {
                    'event_id': 'ɴІǱĚʑƾɤћɪҎȾӮ\u038dMΖTȨañȯɛԎƂĒĿ˙ŎƩʊӶ',
                    'target_id': '¯҇ŭŶ6ÙѡǷˊɸ\x90ԚǶʎ$ϱ˂˜\u03a2ƔǓǝѐ:šˠˢȣ}Ʋ',
                },
                {
                    'event_id': '\x83Ĺѭô\x91ԩǥoʪǂѴǻȿОȳϒҡ`ɄӞԔ1чǟϤŲЁˠʴX',
                    'target_id': 'ȭҤ§ǼѯЊӿäӰŕΈ\x8bȋ˘ӵˠͺǰγ?ʴ˩ҧӯԕϓŭϟāj',
                },
                {
                    'event_id': 'ԐԨαŶȌ\x82ӉŎϫKϮҒÅҺŲПɹʹí<χŁĚӭlӼǧșЅƫ',
                    'target_id': 'ĖҢɕɄʘ\u038dѝ\x80ʎŅĳЗŇ.Ԕ_ν.\x94ҥɠǮ[\u0382{ȏʿŷʪϦ',
                },
                {
                    'event_id': 'ǫǒ˛ʀɺЗƁУŮлF¸ӎԛҖĬƴʁˎñюѽbȊΜ»˹ȷӀˡ',
                    'target_id': 'ȢzļʞīŜϩʓаԧ\x9dѭä϶˵ǦɜƐәȞÊ˓ȿё҉È˻ǕЮƥ',
                },
                {
                    'event_id': 'ӾIĬ˺˘èʣԅѓ\x83ɰєȿƧдʹFϹĭťŒН҉±ŻǔĭČȌϿ',
                    'target_id': 'ԀǙ/Ôӹ»ϦơϞӿк\x97˳ӗ΅Ҷʄņк\x8fƦőș_/Ʊη\x83Ӂҗ',
                },
                {
                    'event_id': 'ʳȖĜҥԩ×ʡÀ3ѴΑҍĐϕ҇ȧѽЉϔǠӝϖ˲ǥŁ\x94ѫ.»)',
                    'target_id': 'εШ˧(©Ӽӝ\x8c˪äȦńŔыψʐĲΒҎʰʤўȺȽБʣȖʟɊ¥',
                },
                {
                    'event_id': 'ӅάĥҸÏō\x91ǋȽƓȔ_ԏɃħŐP\x9fɌˇыӭԙԘӋɤȕˊc˨',
                    'target_id': 'ƍϕȶʿӵˠğ%`ǖПeʒˊуξ¸ӽʖщť%®ίϲɝŇÈ\x93ͺ',
                },
                {
                    'event_id': 'ˎӞ˗@рΰ˕ԑѨбaȢЇΌǔŦƔ˛ѱҾ>ĉOXҙκѳМуυ',
                    'target_id': '\x90ѩϋLӇĕеˤˢƋӼβ\x8cŬĐѨԍÈüѦČЏЬяʵƴéмŞ˺',
                },
                {
                    'event_id': 'ʙrҁχlǢ=ȺòãЧюư\x98ҹZǉϹʣЙӻӞҐҀeчǯϧɽӓ',
                    'target_id': 'ӊƸϪƮőľɝȋʃʣɜйώħѽϕПͽB¤ŔʤÑ)\u0380ѽϸɛƕʴ',
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
                    'event_id': 'Ϩȑ҉ǑӭѪ.ЦȻĪХҕϐ\x7fν˒íЏӔʃmǨȉȲѿāžŹ`ǣ',
                    'target_id': '˝ОКϑʦюϚšȳĠȁ\x9a˓ӈŽӑĖǪHƶĿ\x80ǖǍҋʊoїϢь',
                },
                {
                    'event_id': 'ϱBȓïϢέʤԌ˔ӝliĦȳȇ\u0378:͵òǏ£ʙåëτˋȈА˧ŏ',
                    'target_id': 'Дˢ\x87)ИΔԋҍˤԎАǻÐдÀґyELĥЕҸǌΩҀϠϘѭŰÖ',
                },
                {
                    'event_id': 'ѲцЂҫϐνџɡС»ʉ;ɎάҿΨӈɸɢɽбėɍЂĔҴɺŎѓǹ',
                    'target_id': 'ȺëŚτəƥʞѨԇŌӨΖeÈȳӒeԉʫЅΏʨҙ\\ǍĢ\x93ʃ¢Щ',
                },
                {
                    'event_id': '˒ʏȻ\x87ŧӰӚȲÅԇɰƗʺʬέËϖëɵǇ\x9fȸ˾ҚФгӰǨąŶ',
                    'target_id': '˻íѹΜͷԅ¢ǎʮȱưĸ£ɿΦΝѣҹõӖǐвϘѡfǄŉǺɳĻ',
                },
                {
                    'event_id': 'Ȗȍ\x9cɥ&ǆҽÏĵƦȞ҄ƗƀώίØφҗ¨ɛnǠǭƴŢϦȈӑд',
                    'target_id': '°ʜJ2҅ǣ¶ʝњʶ˴ѨϒӇԖҁӘҡҎɍҹҏťӊϸҩҥIжŬ',
                },
                {
                    'event_id': 'ѢІņҠʉԗ\x9eϓǣ˭ҍǩ\u0378ˍǩǠ\x9eΆӄİšȯɳūСʕįů˙ԏ',
                    'target_id': 'ʋŠũĪ¾\x99ɟſ¹ӷʲxшĄΘѯЮĠʕ϶BŁbɈƂѣӔÆі0',
                },
                {
                    'event_id': 'ҶѶɋȃʂǑʔēȈѐΒɎς»ʮ\x8bҵ\u0380ΓǴʺ«ƖɕǴȡƣ\x97Ͼç',
                    'target_id': 'ĒȌè¯ǾȱѡΪ)ɾȴСů\u0382Ǐ˛ДSjľѡ)ãĿĸœь˜\x83ĳ',
                },
                {
                    'event_id': '1;ő PӻʏʡÉԄȝIúɧΚюȃɉ¯ӬԐ˗ɟþņӞDϛȎ¥',
                    'target_id': 'ӚѵîӮʐˢώΎҹĞƅȕύϋǎaӷ˺ˑӍϋǭ³ђюһ_>ȍϿ',
                },
                {
                    'event_id': 'ͿԕȋѬ!εȁɞŵQŶРǧӋŦ϶ƉóЛʞΠԤ{\u0383\x9cÞYKϹý',
                    'target_id': 'ΜH˓ãϠȶǊƋşǲӊХȺǠѠұΫθá¬ʄȂXȼɎӵȒǵǊǻ',
                },
                {
                    'event_id': 'ɗQĝЉ\x7fΩзӃȴǸǰҳɨΊpżɄӪǧȮvqʗǞΪѣǇ3ԖǤ',
                    'target_id': 'ϠԄ¬¸ψэ\x92өȁƞӜŽγbƪɺѧкë˝δԭґͰΟҬ\x89Ҁѻb',
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
