# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-09T22:28:54.686560+00:00

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
                'Ș)ѫΞŹӢҴĕ·ɈӄϻЯ\x86\x8fӘůżĿƻˢϾԭgԧʛлƑ\x7fI',
                'èЂ˳șȫΠřǳΔҽɟŊˤѮŞκbϣХЋ9ΝǝρԏɻӃ˪ǟҟ',
                'ǋɐŖѰ\x94ƯЈ_ЏИхԫĥlxҺƭ\xa0ϠěÏ˫Ҍ\x82ɥЩƜӣйó',
                '¬/҅¨ωʏ˝±ςԑ\u0383ȫĘʚ˾:ƙū΄\x95ʞƊ;УӠӳϻĲҔ%',
                'ĿҐ˰ǊĶðҞҔΩϪҲϣӷТåҝϿ4ʑΎ˖ȾΛ˙ΦLˈϠή\x98',
                'ìmȒ˽³ȔƹҖtѭӢНģΰҲĴ²Əîõ˶pÅ˹ԉˡɥԊ˫\x87',
                'Ȟ\xa0ĐʤϦĸGň˲°ǋΈĪǧK˴ɶ˯θҤƗӨûűʕϊӖˆ΄Β',
                'ǭϳ\u0382ӝʚPԫǴȱѶ2қζĉҔΩƱɵȰíΧЭǜŊϋ»˙ÃǼҲ',
                'ԗp˕ӀӰãѯёũËӵǲԄӡʽȱrԗυЄϣŭϽ˾ϊFȸȔMФ',
                'ӵOѺǪlȕ\x9cÉ\x9bέŀԋÉϣӶѻѡâϘК\x9cμòǑгʱƙГ\x8e\x95',
            ],
            'source_id_prefixes': [
                'ҙȡϊɄКɄџƉɗđþӘҹȥщӺ^Ӝ˴©Ȭeԁαó}ɮƠćÙ',
                'ǺыƎ\x89ėś˰ҦªΔ\x98ЎĉԊ¶Σɛ\x98˥ćȼӱѯшɅɔˊŞɉЉ',
                'ĉðьZȋηɆQǲ˯řſƁŗԇŮđМLӥтάʮͻ˽ÅԩӍҝǳ',
                'ʘȭ˭u\x83κӅҍƦƢȰьȕԂ\xa0θJāɽϞýϭbʇȾ§ԘÞӦɴ',
                'µ-ϳӃдˣщύ9ɐĬUɪ\x7fʀʆřɪĲȚНȨǼѽʚǩãȬɟʰ',
                'ϔŕΈҼ¯əȠȈŲîΪʇҍʱì\x8aӗ˰ȶÇőʃʒɟО7Ȧ:ì+',
                'қȗwuҞζ£^ďȦӒʾԗφ\u0378ЙåεԀԪǣ2ȔӫɖǕȬ\x8fǓ-',
                'ǻŴCβØт4ɇҟғѫӎ5τʺØԍаɂœҹȑкÚ!śwȣēК',
                '/Ҿ\u0382ǖĿҳȉ©ǞŚŇϼˤĹJӹҙøЦѡǧĈΈЮЂβВҪΠΨ',
                '\u0382Þɣ¬ԖȂɢ§ҨêȧξҋƆι˜ĲÜȁґːtɛЇӭҦѮΊʸͳ',
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
            'action': 'ΗŶȹτȓƔӼ\xad®ĜRʳȴȷќ˫ШҍýӦêԨϯыÒĢƥf˫ʞ',
            'resources': [
                'шʓΝǽӣȕˎҿ˺˹ҲH\x85ЯΚŁӿўƋDѬƼа҈ʔĖѳӜӢʓ',
                'ɾìLȒΩɳƙԅϾ˲Ǎĭ~҆\x87σAοǉкӛԇǹԁɞRrȬΒ\x88',
                'éʊ\x84Ǵʧϡ´ҌԦŵ9îɾďćÙџɶ˚ǙƆ˯ңɥҏċŖͼk҄',
                'ƜςаØĻ"ιȲΚσŎîˑŷÁΟ3ичвΰǱɺìŚԐȖԋŝȕ',
                'þȀЪĴPҁƋάӃ\x95К˘ЛӲ»ԂŨÐǆȊ\x96ɶǏåɈӰńҶƉҲ',
                'ɚɄϯōƬ\u038b$έԋǄʃͽɚӞ\u0382˗KĸӕλНʽҿΎ>ќ©ёҾ:',
                'ǎǶӞƵʣϞɍĬǺкДϋÛțȞ҉SГӈɂҺƳŤ˛ɅԒƱϲʹη',
                'Ǻʱöː˒ʹԡΖǖȚˀŒźäԬӒrӚӡœ×ϯ¤\x97ҩţηČаϓ',
                'čǍƥɹƁΞɫƓƇ\x8buЁ¾uʆĖ~ˮЯΘ\x80Nƀɤǿɦ©ɭԎΏ',
                'Ɩ\x98ҕCŔì\u038bĵęӺʒȒˮΙν˧ȟf^ӢķǮϿϥ\x99ңżg¢Ƭ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ζ',

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
            'name': 'ˈƍÞτЯЃӥЁˑŶԈǀʷЬј\x9cҵ?ɟҤѨӣşӽӨǧς#ɤǘ',
            'version': [
                -2932008921194876842,
                -3051800912094491053,
                -6954760194160082605,
            ],
            'location': [
                '˱ҁŎʌ.?ьΙͲǜµħ˝Ȇ˼ԮΊ¥ĐУ^ˬ%\x84ǐɢԏǎӢɩ',
                'ɲ\xadÔԃĩRӄҜCҭŴΈŔŶǾ6ȘOÓЈԖŕȕϡ˥ɤɄɖɊѕ',
                '˃ʶΌơԁԦhӌ9ÕvӢĞɋѹΊ\x8bOќɅǜLӧφƲǗȰʻņԢ',
                'Ϥ«[ǲҘƆϼƸͿМƤƄǣǁʗƌІ\x95ʢҖșĭɠǑϠıoͷŭӠ',
                'ЁϡηԙġӺʧвɡЮўǜǆǊĔȗʬŜˇȔˣΚðϊΘΘ˯ҢѫӺ',
                'À˪ӌЄʨόқƩɕ˲˝ʴ\x95Ϙ\x83ԜOБǏ=ʘ˖ƅųŷ}Ȍƿ˒Є',
                'љĀʛ˨Бƽϲ+ԏȉąΈǖƙĊEέÈĺλɤȆѷҋιwT\x90ίΡ',
                'Ǥ˒ʑˊħǨʒԗЧԐӟӰѭƟΝ&ЪʼŕŁǹнķ˂ɾÆúíӅǶ',
                "ҁţЎ\u0380ɳ\x93њèrмˇВѦқϓ_Ǽ2ӹҒǥƿҰ3'ϛіύВ=",
                '˫ˀĴ´ɼ\x8eřˍɚ˞Bŉɜ˳ЩҞÁӑƄѴж·˻Ǳӈж˪χ\u0381Е',
            ],
            'runtime': 'Ϛ˒ƔϔÛѻˬэȵıЌͱӈʁӋĈɚÐҫ3Ēѱ¸\x7fɟĹһьͿǖ',
            'send_access': {
                'event_ids': [
                    'ˈҺϜȈS\u038dζv˝ǋġȓӑǚóŴɖʼØŃéːѫǑѭӢ\x97ѭlы',
                    '&ӵǞĬҗǓρӔɌɃ˥ԎƫÝєҚn½ӕҗõŅҡɥΈ϶ƬĚΊȋ',
                    'ӐϨńċƈǎʭ҄ϐȾ˪ѬѣҊhʝ˓˫υĭÕă\x98цɬ4A˧ĳǨ',
                    'ӗĴĶɕ¯ůʤÐƦÊťЬѻρƫƏəöǀȬэɚçǛϻȹӢϮŞɺ',
                    'ԕvПԓȲх',
                    'ϱ@Ÿ¦ƴѣơʜ˺Ʈ©ːӂǄȷĥ)ҞŮіħèоɈʦ˙ȓòʕҗ',
                    'ΡƈϖƇӝ0єΓɄɁ˦ÊϥҀē ˒ǓƟ6ēoԊ^ҀһѱЄ˺Ӹ',
                    'ŀǃΟ©ŬƾŰӡfĘİv¹ΡĵВǾÄAǺԁȰҋʢ\u0380ɕȤȱÛǂ',
                    '\x96Ϧqʊfɣˮ\x87ĐԮлΓˋąͲȚ\x81ѢӬǳϒӯǙȎпƐɦǸȰ<',
                    'ͱӜ\u0383ƄЧŵμҕƯӱMǇмӋȞņÑɢǚмˋҚˉƄbġIӰxΊ',
                ],
                'source_id_prefixes': [
                    'À\x80ĥќΎ½ƸɺǐȏʾͳǃǇІİĳǥ˦ȃθD\x94ŅǤҶō)҄ȉ',
                    '˯ɃƑ˲úӝťÖӟЍϐƓʳʣΣȠіƒΉҋʡŧԈΊ;æо.ɾɄ',
                    'ԇӸ!ЗЮ/ƸѹνìΧϧʯŜΐ·ȮǲмɡДӄѫɧӠſWѰжќ',
                    'ιÌɄːȓѿЮϗŔ\x95Ѝ϶ʮԝ\u0381\x93ĒЦԏӤо´ë¿ŗǿ¦\x9eϸÐ',
                    'Û˩ŊȗĐΈɪƻЈϋHθȟțĖƢʦηȲϏЩ\x9cèοѲҏӤҙ¹Ԯ',
                    ':ȿ#ìê˺Ɓ²ČΪќРƳУ\u038d˲ѕ˄ǷʙδƨǒОҵÑҽÍɹǕ',
                    'ӽҌȄЛҔʝҁι¯ưɿӟҸѳˎϝ҄}ӺŢӓķÿżŌƀŢ˨˯Җ',
                    'ȰŒӌ˳ЦКмΚ%тӸэӃҫӅҜЎìĽĄͰͼʭŤĖζѵӌҏĥ',
                    'ҝҾШԂӆԭɃӎƩ\u038dɲv¡R_Âɛā˚ĕΠʭԣɯɎN6σɵm',
                    'ĈʳƲӚǑ˘Кǐϴdç¸ˠßɳȆȟУԖθ',
                ],
            },
            'configuration': 'ϽYķηȥƿɴñвϺѼǂǇҝѿȼАʲHƈĴ½ϪʔÊʎ',
            'permissions': [
                {
                    'action': 'ÅųяӊÔïʃuӲĂѾ\\ӹ҃нēķϲàξɪʣӤȳũЖǩɱԭƌ',
                    'resources': [
                            'ҿҠΟƏ¿ҒǍȸҺʸÝˠˌ\u038d˕ΐɘӾʱ*ǼӘі&ѷšʾ#ЊѲ',
                            'ɆÑsßƧȰ`϶Ʌą®ΔψАY\x99ΖЄʽƍ΅ˬ±ƌ҉ʞƋƷцʛ',
                            'ԇŏǊɶØњƩ&ЖΩҘԜĒUҷǦР˅ĐŷΒλҟͼӚȋˮԃ®Ɨ',
                            'Щɑ!ΚάÛÛŊwƆʕ\x87řǝҍԢƸʰ_ǫYNӭ½ˇбӼȘ\x82ġ',
                            'FȟϘѱ˚Ɉԟ¿ȷѓӒςϧeȣCɬӢӜΦĞфӖƾ˪\xa0ӞƔ{б',
                            '˓ƢʩƚȳҟОɗƚēƧɽ\x99ЪĦǋ+WĊĠң\xadȅƫȖԞŷҐєǮ',
                            'ʑȊԗӌϳҌƉӓǀ"ϫɥʉ˲ΎƥƞƳ˟ɥž¡рûќɬŗʹǐ\x83',
                            'ĢmƘ\\ĮЭˈʱ{ӈΨǚɘ×\x90çƕϝЃʕҞƞЫğʥƄê˗˅ǟ',
                            'Ыь\x8eЈǬԭӊΓ¦ÉŊɂДӵʯŴİʊ1αȜɎǵÔӾĨċČ¿Ɯ',
                            'Â˨ɇϙӖɎďӮ&љŁ¥ƫѨ҅Ԛįϐƨ0ɊɫŹĤӇǛʮȫɇŔ',
                        ],
                },
                {
                    'action': 'ˮɩǸȸâðН"ЃxȠѹϯ\x8doȴЭҽɸĽʳƧĺǕҖƬǉȚĭϜ',
                    'resources': [
                            'ƁǨϊѤˊȗȾΎЈĽԁ÷Υ]ʷˌƓͷƽˏώȡĦҙѓ¸ΩѨţǷ',
                            'ƧˁϜȚĪǄǔɧԋТԞѧɕƓƫ˺ʼɔԠȉΚǻуӰвϔŲɣ͵Ѫ',
                            '\u0381ƩӯөɠjȊȄѫǹӂŊÆǜƗɐЛ˺Ĉ1˾Ƭț˕ĽάƝđѱϝ',
                            '6ǼϴϓӒӋзϢóɏӦĿэLŅ˪üĖąΓŦˌќĢΥӃΣӡҴд',
                            'ʶЎ\x81ĈҬȂŞ\x89ÖƜӱôˬɧſԙƶ˖ҍÖǡŏŲĊŴҵѩοӬŽ',
                            'ʩ\x93ƧԎǽʊϵ¸ˁҚͰñГoƦƦ{\x95ŻӟӜǢ˙Ԧ*ƶ\x89Üьʳ',
                            'ÂƤʅϟłåƅΪʔBȍĳӆŝÕӰϲχɝ҅ӴŶŜ\x8c·ǴǵyԂβ',
                            'ԗǉӝƅҍѪɢǑ\x9fӀ´ЕA-ƙąϡԁ3˕Ԓϛ˞ȠƮªcƳϜƏ',
                            'ӑƉVčǿΒʣ˛˯\x8a*ǎM\x8d϶ҕϰkʇȎʓɀϺ.Ҋǎëyқʭ',
                            'ʯ4ІńǃҵȚȟѺ\x9dȩʨʶЕˊηљ\x83ϧӯĽƷøōФèĦȐӗȁ',
                        ],
                },
                {
                    'action': 'cԡɄūȲРŶύůɨ6ҫ',
                    'resources': [
                            'ҥ˼ҫĩāԈ˙ҴȒҠÿǶΧȡҴĻϱҰơΟo˪ăǆҡɵ˗ŏĹï',
                            'ΩʦЏŰΨЯ@ʈ\x88şМĪ҄ҋȱ`aӔȴϴҖÍ4ϑ`Hɂ˟Ԡ˟',
                            'ìƼӣˤu˓ˌs϶ɍɿˈɆˌҗö҅ԝ\x80ѽӆˎӰԜƃϡʍªʗŒ',
                            'ÝǅɈûɍɏ®ȃέРʻ=ʀԦЎȽɹ;ƄΣ1Φ˔wΣιȾƿГ\x99',
                            'ʝ҇ѾѨϿuĦƣиgĂн×ͷÙӒʘǑґΖ²\x81Ԗφηŉ´Ѡƥž',
                            'ʗƍƮƀɫЪŐώӥƒώȖϒǙȻĔɔӮǷʭ˭Î)ˮŏӓ{ѝ˼Ф',
                            'dÊ\x97ԏZϋɳ&Ŏи¶ȪnXИ˔ĪϜӔʭƩ®ɺɍǫѺǣΣʹΞ',
                            'ŵɹɐΤźϧÅҭϰFŽȳȒġˌʸơ˝ԦƥțέɰˏαŪ\x91½ʜȉ',
                            'ƨ(ψӛˡĘҢŹĈæџˊѺȑJ¨ӷĈ1ΩñѭįӷǭÖΕMҍʘ',
                            ':ѓϯɺԣЄǠӘѴзÁ\x8cт³ӥ2ƋϧʪϪмĤnɣϪζѦʟˌĆ',
                        ],
                },
                {
                    'action': 'unÈҽВx7ΓơȫɩѽK\x85ŐːɛˇͷƄɏT·˒Ʌůχ*^ɯ',
                    'resources': [
                            '\x8d˘®ˀщȲEĵ˓AȄɅŞϙԏç˔Я½ʑ:ɚҧԚʉΚҚoãȎ',
                            'ǍȖѠǆӹǮťȒΞѸɬâͽЮσгʋѰәӾ¥ɔȀƶ\u03a2ÓҔŰɅΥ',
                            ';ӄʜBOıԥ+6Ӆ\xa0ӔΨ\x97МмɊƃÉӘʿԐʎȹгĘӓEȋB',
                            'ɿúˌN;Ӷϴɖġ²ʇČӃвюˏϠҔȃ1Ʋ+ȴIζˡͳɣӶĈ',
                            'ŞȡϟһԨԥƙǒǎƔżӭơ˝βɛƚĞzɓpÊăЏνƔŲŉZѺ',
                            'Ϥцϡӯ?áμDѧϗȞФµӥɁПѪ·ϑ-ΧАǚȥŘɩϩǎɒƶ',
                            'ѹÃƚQȍԋ\x8dː\x8c˛.ƉϚъȃāǲĢ¬ʠЈŏ\x92ʼϮӅʗ˛ːį',
                            'ʇĿԗÿΜǧѳŭƊǫѶɏáǺѶ˗4ì³\x88ƞ0ňSϝŶ˖Vˏȴ',
                            'ʯҌǎF·ǏȾɐŃѪÁĘԛӹȽƐйѣĬu*ʘŰԐɤЌ˜¬^Ҿ',
                            'εяǥОȄ˹}]\u0379ѱǒɪJϺηѼqѯ˧ŊZϫǎůϒˇҵĵȗŌ',
                        ],
                },
                {
                    'action': 'ɡόÀŠЎҢ˻îǮ`ƒɀɳʃȺҒίπ҉9ʳѥМZеѲýΏϛǚ',
                    'resources': [
                            'ǄcƘÃǕťΗŁÛ',
                            'ȰŻċфјÌϚʍȈĀ\x9dʀVȑӥA`īДiɫÙȦɂ˪ɗ\x98ǁͲ¸',
                            'ΡQѹ·Ņ˩ԊӛÕΜӟʹȃҎɟˠѤѡφıХĶƜѱˍ\x8dϘΛǏ˛',
                            "äȺœӃѡҏЗ˹ɼ'IЫΫīǐǖ\x85ΤGԖˎƍ˯ԍʯɛΥцÜǚ",
                            'ī©єmѳɀĎJԙȮΗρϠ9\x8f˭ʒϾѼƋҐŵ;\x9aǌRÕи|¯',
                            'ʯӪˮϯІȊʥĲÆҷuɭWşє\u0383ԪɾӗΎѼͳcҥ˩ʮԍѩMн',
                            'ĨȄɁҸ\u0383ǠҎ҅ÞԍĢĉĘѥЧˆˆӬԥӐǻΈУǒӤɔǒŐԫŷ',
                            'òȘоѢǟԜϯ.α·ƙǆǶ\x9dˢҋ˩úȄӽñʟʎί˰\xa0ľ΄ǜɘ',
                            'ʂѿ҃×ƞŋǀƆһǃҰҎɢ¼ƲǅҌ\u038d˼;˦ˊ4\u0380ʋ«Ơ+ğǻ',
                            'ЂʰǃјmҡnțɃɛԖˮ«Ƹg$ԙ˳íǍǜϻƩjӺǎlǷ\x97\x87',
                        ],
                },
                {
                    'action': 'ёͲӼҕγȱюΣԡńĔwÚ˳ņĲкԖŇƭԙ\x9aČЪȬʣӃЩsȱ',
                    'resources': [
                            'î˃І˦ͽ˵ŖɜIԕǉήΒʊүӸȺй¸ъЈÂƝ\x82ϗ®Ёή Ӥ',
                            'ИъԘą©üÍΒСÐ\x91НʟŴΒˑӠyԀЇΧрʵXˇ÷ȤćЛ҇',
                            'Ѝ˚ØͷƳ,ɀżgЖǳȊ6ǷȵͿ·ϜwˢŃΤ\x80ķӎĊ˕ʺϦԪ',
                            'ӉƀʇųѰ҅ʕɪ˃ΔԔӝ¼Ѻǭ΅\u0380\x88Ɂ\u038bôЭ«ĢƣyЋƤΐΧ',
                            'ͿɗƿƸƘɍǩžĄȼ)Kľːӟў˄ȹґŬǵÄτԔ˯ԭԀ\x97ӥͺ',
                            'ɬѣ¤ƂέӗÄŷƗϯǼóϯΨћԆҁì˺ÆкʉǧѰłɣƀϽыȬ',
                            'Ѯ6ӜŉӀȀêƷȸ¯ǉ9ȻӖˤĹиЊʹӟʊАρϧШʆЉĆоЅ',
                            'ʫΖʳĩȩȝ[ĒҬӏʍĺǥԨȻ«ÚХǷůԍԄ˖\x8eϔQ/ѸʻҪ',
                            'Ƴк6õʵĜѻѻRԅȕŬĿȦʡȖԨˣʔˣӲȼ˻ŉΓǌԄыáĥ',
                            'ĲϫΞҙGǦιȘƺÞɂĹљ\x9bǺǥˮѩчȕſÃȇÁЄԈƫŴȏĘ',
                        ],
                },
                {
                    'action': 'îſͲҊӥȚǼĉp7ê˩҇ϹŦӊwаŐͰľӵϕĚχɀŮʇιƼ',
                    'resources': [
                            'Ҷ¬Ӡ\x9eԑԞƪþϪͽȨˠəɡĜGѭõȜѐz ӳϠɦKԫ˥ʓ,',
                            'XыɧЛ˹˰ѽҝˢƙϯ8ʏЫǯ\u03a2ǬŊģΈ"UŠӼėɋϹŲћʒ',
                            'țҊÁʰӠȫĲϹȅʏɊǾĿ\x98\u038bΣɰɕŦҠ˾ϓӅγûǤȐʼʅҹ',
                            '˾ɌĄȋɫŖʯȽĞÍèщѡκҟ\x87хԮǩ˰ɦVϽȌ=ŐӢѓpҵ',
                            '~ÎŋЮ˭ϫǬŘ\x94ЫȠǤыԖĦэ<ˉϬΕǀɆʺ˜ϤʯΚ˟ϰѡ',
                            'ӬYȰϧ҉ʱłηŋ,pɤõjͳȂ\x9dª\\ӆċϦĿ˒ÐʷӖϫϞb',
                            'ŵʮ©\x8b\x9eӤê%ԢϝǏΩĵȁџƋΊťҠǼӤɔĹʠĴʤ\x9f\x9aˎˏ',
                            'ӎԖʧȴԪʙϵǷӤɖьϘмŖÑӀǗǀкхϣѶѢԋѿ<¸Ȋ˪Ƶ',
                            'ʼˮō˽Q»ÚǢƃΰԙĒ˩ЛˍϋɿӪһŪҖзʠ˽әxsгȋĎ',
                            'ŌԈďXÅѴƸР×ӽǻGθ\x8eξɫθӝʜǌ\x9bƷŚ˕ҝŁќ/˄ц',
                        ],
                },
                {
                    'action': 'ǓυăȞȇòѵʟЮЅŎgʖ×ʎˣKȈȮȱҟňLʀθӗʆǗÂÙ',
                    'resources': [
                            '͵ǕȹĄƗɛӉͷˑǌ\x9e˦ӳі˴CиҎтηиƶÛкӄțŒŠ\x80ľ',
                            'ȁ˱£ˁȻԐфĊôѣʙϿα˹ƖϨʔСˠȅѺҙʮʧӂ˗ЬɅЀʐ',
                            'ÍҜǳ¯ʗŐřӌҼѳķƮȕҤӨ$ɐʿʽԎ+ǢĖһϢ"ϛ˻Ȱ£',
                            'ˠΏԮÏ\x8fʈԙѴЋ\u0383ӝɐōȮɨ³Ǖ˚КϪԏЧŇÖ˦ȈԎҩǾȪ',
                            '\x9eњQӡƛǐŹǓÐγҴƄģѲɟςυȠƗʭћʃŜѮѭĽӻɫӄɎ',
                            'ĭԩ˖ǩȠōȸƔϩ¶Η"ıɪÿͼ\xa0ɡϴΠķҿɸƴş\u0382ɗӃPТ',
                            'ϗͷŷ9ɤҸьάȨѼTƦϿˍǸǶşeͳӡ˴ȤɭбeӽǭғǗϽ',
                            '\x84ˑʩƪ\x96ˊǴωƃԑϓƙŻªҬӜӧȞωӝxɍΉΆӽėʧʟӬͺ',
                            "ӞҐ˲˝ɗΨĦUΜňˋɟҮi)Ǘö'ΗǨОƥɝŬĵƷҰҿĊÜ",
                            'ӨԌ˹Ҭ»ΌȰӊюʸкɧӃɟǖԂ\u0380ӏʍȬгȾαŽӝЛƒ¤ҟЛ',
                        ],
                },
                {
                    'action': 'Ӫж\x8fsˡhǗʺϡɗúŀ8ΞńN´ˣ҃ЍĺӨ΅z҃Bĵ˗ӌċ',
                    'resources': [
                            'ѽ\u0378ĄФĞԞұ˜*ˤÖϨѺȸԫѠ˴ŏɎʺŉɍ\\ʏξɤϸΝͳ¨',
                            'дôĢ\x999µùɪҨńɈˢΔˤǤØɝԕԀĐŖɈҥÅôǜƪάѮΕ',
                            'WѴȡӲƓƝёΟfʔǳLёƷǁӸφЃСêĿӆ)\x9e\x91\u0380ʰŎ¶ԣ',
                            'НѤG\u038bЁ\x87\xadß@ώʕηρĒѺ˜\x86˭ԓÐӷ»ȀөӗιќΥδǽ',
                            'ѧҼԚʢƓұοžŲΞɐƆ˰ȧΜǮž]6ɛĦȄѾЊ\x91ЃΟU)H',
                            'ǯӱϟпҘҮ\x86ӃϓƬƶʅѷ\x9dҶƆ{Ґ¼рЌơВиmȣҾȢʏ`',
                            'TȅÙԀѱȻōɓ2Ą˭ƍMӡOӪĦԣϫųжʃŌɯũϴíαΣŉ',
                            'ґΝȰˣ϶Ś"ԍιÁʘØɤӴȬљǫQƾùǪƑʼȖơüϊÁĻ҄',
                            'řʠ\x7f]ҞФкɐ˓αҗ΄ȘόǫģóȬʨȔϦΎŶӪыЊ×Ǆ\u038bÜ',
                            'ʫƼȍċɝn\x83ǃȵƘлӇҬ;eĽĒʺŏʠ"φǛÿěƭԠѰȟӋ',
                        ],
                },
                {
                    'action': 'ӔѡшӳхȅӑԒИÌσ\x95Ÿ7áƬũˑә˶ĔǪ^ƽϋvž˜ҏΣ',
                    'resources': [
                            'ѝȞ˴фƈɦƗѓǎ˾EҤӱѸDȴʿϙĜШ˛ʊ}9ɱ×ұӪӊù',
                            '\x90Uɩ[ʌԇӭΕǯΣĉǔŁĨóʤԌˀӸʀдӠˣqƽǲĽǞȏǺ',
                            'ȞrХǫӑƫԢɪüӎ˃ӾҍӞϨЬǸŘ±ʆºƋʻҊȎΐ\x84ńͺȎ',
                            'ɕİƒǭвү\u03a2ЊŦ~ԋҭ\x9eқ˴Һ\x9eǠҭƫòʊķϨ\x89҆ѦÍœŖ',
                            'Ѵ;ˤԚâřќҧ©Źԋˍ˓sļԍ\x86ЁgϬ\xadҚǵc8\x9dӊAŶÑ',
                            "ѫҘ˟ǺɀÞȐҖZìԘȫ\x9cъϹӨΝžЏӔɣJİИЌъƢњ'Ǡ",
                            'ǝҵ\x97qȴ_˖aѐ§\x80żуQăε¬·ʹʌąьʨɍȑƖ҈ƭҠ|',
                            '˱',
                            'ʛ¦8ãӼҖжʥŁӈ¸ķǘʉÕъԃȹȠӰ`\u0381ԁ\x98ʞɌŜӂВɊ',
                            'ΐӀƕɢ\x88ˡĂƍΜɀZφϏĎҜ¦ɥЛĪКιƧûɳʊǕɎŋԫҝ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǐĕƜ',

            'version': [
                -4163075997880018584,
                -403059505877941448,
                -4187391516187357925,
            ],

            'location': [
                'æ',
            ],

            'runtime': 'ť',

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
            'name': 'ǉϋΩ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x96Ðș',

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
            '$': 'ԐҝӮɀǇ\x84ѢƜș\x81źµΤԧȧÙÛЄѸϊɰȴЮɼǘӹѭůʀ\x89',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -8120702859264643362,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 381811.797877098,
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
            '$': '20210209:222854.602445:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ѹǰјһҔЪɴ˻¶ǾíѿҏщʙˮΦ[ԀйԜfoɕʽ_ɜΞ˵ҷ',
                'Шǈ\x93лəΜĿɒŵǜͺʼ¤ЃåŘ0ԀŦŚĀAȌ˩ÜBɦɈ°Å',
                'ѦǲĻǽ҇ѰҡƙŵŌөѧĆ§ĩРGð˧ԁͻùǅҁӦϼĺϳ§ģ',
                'ĩnĕʞčӌҩ;ҭȈνҮɴν҂\x9f\x9f\x80ҽӝϱŭǣ҇iˋżԋĳҰ',
                'Đ˓ȆτŻÑŌǘŶĐ©ĠˮѷЧǊ\x99ӑӱԙӄӹĲϖұѐʙ˟ŢǺ',
                'ɂԑоӧӧЗGƪπӼɲɍƀ{ƥҭӥ˨ѡƮƘϋGӞƒӻΫ˽ΦӲ',
                'ŁúӅҙ\u0381.ҵǼƼ\u038bǌıǓĵЋ\x97ʍϨʟēҲũŝƚʽСɯΜ˒ȳ',
                'ѿҵԜȽӓ`eN˥Ԝԛûq^őΜŖϟ\u038dυӂѳҤҌӘδÙțʵƞ',
                'ϒıʗʶΧȎԂϜŁƇʅ®χƆΙӱҳ¼ӻȋӭbӦÄ{ϲԍȟɟŖ',
                'Ńϻϭ!ĝџ?ʃvѻƿю¯ҪƭǯϡУ->ɥЕōРԎŵY˷ːѠ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -6021799452336261142,
                -8977733401164711481,
                5980496231828478619,
                6552448285659652709,
                -418491272541796033,
                572967427593161059,
                -8006025994468895557,
                4191968815753302162,
                -7694600072021461589,
                4953761080516078448,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                925065.6937637355,
                929299.6601523003,
                -98657.10090998092,
                116420.84291934673,
                639121.6419532596,
                109681.6693139589,
                563552.1263685505,
                507263.1044163178,
                776638.9595101316,
                406790.1523867859,
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
                True,
                True,
                True,
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
                '20210209:222854.604382:+0000',
                '20210209:222854.604419:+0000',
                '20210209:222854.604439:+0000',
                '20210209:222854.604456:+0000',
                '20210209:222854.604469:+0000',
                '20210209:222854.604482:+0000',
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
            'name': 'ьɜǑʖõǪͲǕ½ҕ(å,ήj3ÎӴсȬi˃Ĺɰ;ɳЗ\x94ˁԜ',
            'value': {
                '^': 'float',
                '$': 615258.4924067341,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'µ',

            'value': {
                '^': 'float',
                '$': 795050.4089391882,
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
            'catalog': 'mӞ\x94үϓеƙÄјѤЗэ\x87nǂċԪď\x90{ΉнҫЏŤŖйɎԔʤ',
            'message': 'ҜˆԣϤʠħΩǺȁҁÐʞǢ/Ϝ˰НњγѻƴzɆǣɩҬӔ6ƓĬ',
            'arguments': [
                {
                    'name': 'ǦӘˠԖŴԩŞɤǬřΩŅΔЉĥ\x80Ò\x87ӏÈƴұҡĄúŃąŒŋ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        2124285429723040492,
                                        -7711035922769221939,
                                        3247178507994629790,
                                        -1479760897847304667,
                                        1640126017515557947,
                                        7922154536714222626,
                                        4383002958880308788,
                                        7477463109676384275,
                                        -1250664392852848064,
                                        -3766396838378882927,
                                    ],
                        },
                },
                {
                    'name': 'đϋêԮНʑѵҒʽ6\x87ƛɪЪxˊȑǎϏΈϦĖʼmѩ',
                    'value': {
                            '^': 'int',
                            '$': -2365242149997939058,
                        },
                },
                {
                    'name': 'Ȃļ.ɟ˷ǲШŜʏϯôӵҵkŧаʩCуʲ҇)ԙΉƇƹʓǘΡɵ',
                    'value': {
                            '^': 'float',
                            '$': 803698.0571300989,
                        },
                },
                {
                    'name': 'ўɓѽЏҟӗñŢʴάϴԭPɎʍҊЯɁͳЯΊǩȖЯ©їʑϚǞЍ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -8650301272805980426,
                                        2325311495826105154,
                                        -501779670519812969,
                                        6160203619050470236,
                                        5614782596523228787,
                                        3031263190753808053,
                                        2790258069500025721,
                                        1501898247703647743,
                                        -5280621856043283690,
                                        3433315270412795406,
                                    ],
                        },
                },
                {
                    'name': 'ҙʓ\x9fӄĊұʖȽųɋŽʊƐцԐІƏѕӮuƟԜΦèҳÙ\x8f',
                    'value': {
                            '^': 'float',
                            '$': 116292.40755035926,
                        },
                },
                {
                    'name': 'ώϠˉŎºǞҥƵҰŔŁӸǶЉќԫȭҰѤĘЋӻǟʅªǯџőА',
                    'value': {
                            '^': 'int',
                            '$': -1303681145265885247,
                        },
                },
                {
                    'name': 'Зԏ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210209:222854.599559:+0000',
                                        '20210209:222854.599608:+0000',
                                        '20210209:222854.599630:+0000',
                                        '20210209:222854.599650:+0000',
                                        '20210209:222854.599670:+0000',
                                        '20210209:222854.599692:+0000',
                                        '20210209:222854.599707:+0000',
                                        '20210209:222854.599720:+0000',
                                        '20210209:222854.599736:+0000',
                                        '20210209:222854.599759:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ʹǊŁӘԫɔеӉЮΈĸ\x92IĬ,ԁɪŸɃʨҝ\x80',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': "҇ǼǾÕͰϹπΞȋЅӳ}β¼Ɋř&ˍɭ'Ҷ˳",
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ӄ\x83ŽƋԂ9źҴ\x8aɵ[ϒ˚ǽ\x82\x9f6ô1\u0379ԎĚǸЉөɲͷǫʈ˴',
                                        'ѧ҇ˏӵϮ\x9aϭџϙƨюĹh\x99ſċЃϧӋɏŰÃʩǖʐъŨӍ_ɖ',
                                    ],
                        },
                },
                {
                    'name': 'ǴʚҞǏӵфÚԊ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ѮϽ',

            'message': 'ј',

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
            'identifier': '-ūΜŔƟєĚÖŻԥ',
            'categories': [
                'access-restriction',
                'network',
                'os',
                'configuration',
                'os',
                'os',
                'file',
                'internal',
                'os',
                'invalid-user-action',
            ],
            'source': 'ҬϣǴ\u0379\x8bĝºǱ¬ʈǸьĉΎΓǧͻѓŜưӇɇǧпμɸƜǹįӺ',
            'messages': [
                {
                    'catalog': 'ѝǥӰјӵͼ\x97,цϰƷ\x99Ѹ\u0379ɉǹΓԎˊϝ\x8aëÓЮƱȥˌ¨/\x8a',
                    'message': 'ŲƿâϷ¸˙˒ԊНˮ˰ΆɠҮ˟ÁԘӰӁŕŤҏʏŹˮŧʻԔ<ǰ',
                    'arguments': [
                            {
                                        'name': 'ƿƚèҨ\x8d',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.543580:+0000',
                                                                            '20210209:222854.543625:+0000',
                                                                            '20210209:222854.543645:+0000',
                                                                            '20210209:222854.543662:+0000',
                                                                            '20210209:222854.543677:+0000',
                                                                            '20210209:222854.543695:+0000',
                                                                            '20210209:222854.543713:+0000',
                                                                            '20210209:222854.543732:+0000',
                                                                            '20210209:222854.543749:+0000',
                                                                            '20210209:222854.543766:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѽĕΘ\x93φąʂɴԋτ®\x87қȒɊ\x83ϒǭ˃˫ЄҍРƉϩЗɝβ;ԏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '8Ҫ˞ǹǵ¹ȵƭɰÓΪȰ˷ϦĎωѭҎƁҘʑźƢ\x94ǖвҩüϊʕ',
                                                    },
                                    },
                            {
                                        'name': 'ƀƤʧɛ9ҾĤŷƄĝŉǱіȷŵѬԂ҅ϯ×ʓʝϽǭԂӫҰαӿȀ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ůʏ\xa0˪Ӗşɂ\x86¥˗Ζ\x87ңɄή«İͻчīȓ˙>ʏʣǩʪηлн',
                                                                            'ӅçԚħ˄ʤ҅ƀƾҟнԭuԌϝÜƼȘώӀЉϴŜѲӅûɴƙϗҗ',
                                                                            'ӯɸεҟǍȥ¢NfоҷƅԤӂУ\xadφ*ҙΰ²ȋǌ$ϫǄɗӭΆ¸',
                                                                            'ѓʽ˥ԀχTƔ\x8fķ8ɤԭˁâǭƢiϢɫńζΎ\u0382Ө:чȤӕԉ7',
                                                                            'μɋƩŚØθˌƔƑԁΆ˻łȥѬΈɳǳͻѯϽɂōϢ´ \x9bȹϴš',
                                                                            'ŰĆʗЏħĠmϛʊξ;ЭˍӭʝʚʹœЩȦлxӆʻͰ\u0379ʁƇʆʉ',
                                                                            'ˋјΈʪӮȿȗ ȘTϘҵΓǴʺǱPɄbɧȠʩœʋƥƋΓϱŲˎ',
                                                                            '҅ŃҋǍƕԝ˾ӏîεÕğΟųr\x87ΚӚȌпǉȸјΨ\u038b˙Ɇ΅eЫ',
                                                                            '\x91õsÑϧğʜЎKЩ˝Š·ķ\xa0ƱʤΈƶϔŚȼɧPÂŋɆКĽԛ',
                                                                            'ȦϺŀZМЪϮȈŘɃ˓ĬмƻċԋλȫЕԎωŊγFɰɽϏӀʸŮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѶӾ;КҦӘΡ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Űкʿǻһү˅ŦīԆМÄΣĳȚϩ˦¶\x8eϘSʸsƚс\u038dêʥƢƝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            634087.8315328674,
                                                                            748774.429744651,
                                                                            781892.6252075348,
                                                                            510815.1323402092,
                                                                            -81048.8766181854,
                                                                            344134.86221076635,
                                                                            -65674.37045565131,
                                                                            561145.9532237349,
                                                                            4127.718118700446,
                                                                            687306.9222834193,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǡȋQʒĂӕŧоɂǄΗÉʓȚһ\x8eϾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.545545:+0000',
                                                                            '20210209:222854.545567:+0000',
                                                                            '20210209:222854.545575:+0000',
                                                                            '20210209:222854.545582:+0000',
                                                                            '20210209:222854.545588:+0000',
                                                                            '20210209:222854.545594:+0000',
                                                                            '20210209:222854.545600:+0000',
                                                                            '20210209:222854.545606:+0000',
                                                                            '20210209:222854.545611:+0000',
                                                                            '20210209:222854.545617:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŭįƮК',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѨԀħѮƭϗƫ¯ҕǄυжI\x87@ŸХ˭҂˪ă\x8dђцƚԓˠĦŰģ',
                                                                            'ѧ$ǖŬȖȆǾӐԩγѢȅĝҏπύхʳӧʁȔđ·ϥРѮœʋxœ',
                                                                            '%Ϊ\x82юЋÜˡǃǢʌӽԒˇȑňǈʠ΄ȧѮÆ9ɊԠȼ˘ϣȶ\x87Ƹ',
                                                                            'ТВӁʆёȲӫӆӟс\x89ʘŉЁɶŝ~$ƣÏȒ¨ϏȘϮʠNǏǶȒ',
                                                                            '%Į˼σÅǼԧԋʦÈɜҿϭƅĬѱϑſʰĦƻϷˆҨΆȘĞ}ȴɷ',
                                                                            'Ãǜ\x95ЇҎϪ5Źɹǵǡƞ2˪ΊͳҎΘьςŬ Ęͼǰ˱˟зȊȘ',
                                                                            'Β˔,%ѻAȿĆ\\ťσҡ\x87ŦǩƔӇπЊҦԕïӷ<\x90łɼɷȪЪ',
                                                                            'дŐØƇǞѴ˧ė>ӧCΰƿÝğҎлџÈшϖԞбʡӇȜԢ8ĄC',
                                                                            'ЅƍɁ\u0381ˠʫ=ȕӪɈ¸ςưϜ˵?ǟΠńҎEħĒί˚ϗŬeĆЩ',
                                                                            'ɔèěӾĶҿɤЏ4ЕЃēӺĨƝǒбҟÕtĝŻͲʏαˑȇť|ĸ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÐñʡVȶ\x7fɘŉƘ¸ˤͷXТSЀœ˵ȢԥƧ˔ƻŵҚʥїɎý\u0383',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2772053850286070060,
                                                    },
                                    },
                            {
                                        'name': 'гƃɽȯѢɢҭЈϯДўѿɇ˾҈АÃӬ½ŶӍӊªǎè',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӃʯǹȨȑŘ³4ÂʅЙԃwƿΩкчǧ˄Пϯτї',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4518684194019456509,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƉžĻΡΘ\x9fԛ$όŃӀӰԋСïҐɶȏ\x99ʾУrŦĐƓӬW\x99ģƠ',
                    'message': 'ǬōЅÁŞŝ¼ϭģŀҚǖкωɒɡΗæΐĽӏĥÓˋmXӧʹ˃b',
                    'arguments': [
                            {
                                        'name': 'πȥÕѝ\x7fɇɯǃˣǇҕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1716603586649329350,
                                                                            -499001129219104092,
                                                                            -574471012003023470,
                                                                            868975377630253501,
                                                                            -8695572773596247137,
                                                                            -12851881449488713,
                                                                            -7807470782167831980,
                                                                            5003058076806777352,
                                                                            -4560618566550715673,
                                                                            -2342770179936117118,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӮŌԐǒ˥ǰӲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ʒǡû˳ɉ÷ΘĵҪǱӾɍвɲȎϼԡĺ÷ɔ;»ǬÝϺĪš',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'dϱüɴӖǄɥƈ˧ӕɗы;ŽɫřqģÊħâϒˢɞК2ãϖRȃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.547599:+0000',
                                                                            '20210209:222854.547614:+0000',
                                                                            '20210209:222854.547622:+0000',
                                                                            '20210209:222854.547628:+0000',
                                                                            '20210209:222854.547634:+0000',
                                                                            '20210209:222854.547640:+0000',
                                                                            '20210209:222854.547646:+0000',
                                                                            '20210209:222854.547652:+0000',
                                                                            '20210209:222854.547658:+0000',
                                                                            '20210209:222854.547664:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¤ѤİӕɚȝѦƘһʂíãÀˉǲÎšѽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            767745.8368548573,
                                                                            369053.4727613357,
                                                                            836013.0388754142,
                                                                            861992.9654033021,
                                                                            838529.2548134538,
                                                                            617670.7837610417,
                                                                            52993.650514721725,
                                                                            185778.06603344582,
                                                                            828507.5275128644,
                                                                            179084.77595496917,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÑӈаĄʾӼ˥ɛĊŁοŷĵ\x8dĥKǋłɉͶĪһϴŐɀҞΝЬ\x8bˬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.548138:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÀϺʩł¶Ǳ4łǃ˂ŧԀƬ{',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5802682742207713995,
                                                    },
                                    },
                            {
                                        'name': "϶ЖKѬĲт\u038bʹǀ'ȴŗáԞϙǴ˵ҾϲϓPCԚс˃Ϊ5ϼϜ9",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȩ˧˔ΖǏԆmēȻƘlł³яŢГ\x9dźƖȭӜѵТÎīŤȎȡһѱ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 224287.84142415295,
                                                    },
                                    },
                            {
                                        'name': '$ſˡʈneήńѹˣоξѩŤƗĞz',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 276129.0805187217,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˺ŻǣЊљȒԆȳΫЪΉνӝĖѹɉŷѭ\x9cѭáϨ\x87˺ѝɯʌƌ˪ӟ',
                    'message': 'ҬÿҧĢƊѷԖ]ӷϥˬΨɅŕĨÝҚҞʤ\x99Ѵȣ¨˦Ϛҟȸʪƴҋ',
                    'arguments': [
                            {
                                        'name': 'ѰлǾшԘӇӎКҾΙĸvUˈΒɑŹʅнρƩц÷КÊͲƷ\x8dAů',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӑϬϨļĔԅΥöǁġʱBƦĈƈÓϚĩǮͼ.ʽʬӈ\x91ѝМѧȽ҅',
                                                    },
                                    },
                            {
                                        'name': 'ӭӑƦǽŝρźÍĀˤ$Ѿ¢҅ʽ˩\xadΞѽԈʓĥɟȝԁъƏǉӧ&',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.549379:+0000',
                                                                            '20210209:222854.549409:+0000',
                                                                            '20210209:222854.549425:+0000',
                                                                            '20210209:222854.549437:+0000',
                                                                            '20210209:222854.549448:+0000',
                                                                            '20210209:222854.549459:+0000',
                                                                            '20210209:222854.549471:+0000',
                                                                            '20210209:222854.549482:+0000',
                                                                            '20210209:222854.549507:+0000',
                                                                            '20210209:222854.549530:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ў˺ӼǡbǢ˥yϤ«ԂˢрӀ:ӭĒѴŵŃ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.549904:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŮΛһɪԏóδ"Ş\'ȃǔïØԚĄŗяǬȃ2Ҏ\x90ÆƇƞ˅gśФ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'φ˴£',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8966169525681802928,
                                                                            7936590545923218406,
                                                                            -3099535963579990473,
                                                                            -429593183649363588,
                                                                            5201871286401686279,
                                                                            -5182228446543833337,
                                                                            -6182843351757620884,
                                                                            -5936260731245820591,
                                                                            7110897041134402047,
                                                                            -5733585138072805584,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ńʚS˰ˁУϐǑϬȟ˒ǃȫ˸Ћόӽǿė6ę',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӫʝĜɾźʇԥʁέϣʌϣВì\x89ñŠьɝθĜ\x97ЈŰһÞ˶Ɇ϶¶',
                                                                            'ԜɛҸԁʂҁҺѥ\x96N\x8dˉńƼ\x87ɓϩéôҟɲƁǣ˼ß^ĩ\x9cǝC',
                                                                            'ǐ˖ÁɁэĵȄѫȩΤҸҦԄΡѦɕòƶǮǺ˄дϜæŔАdЌƊŹ',
                                                                            'ʹԊЉīèʑԄ:\x9cȶԄˢŨ\x8cťʔĎΙԇzˡtҰѬɘêƄϕϬǴ',
                                                                            'ͷ\x8aϮӗ,ɴĢ<hι\x99ӛʼ¤žŋĳӅц;Ϭ˨ĆǝέȆɇƹş\x97',
                                                                            'ǌĐԅ҈ѓOɅϒһθˇ҃ÁƲƢɝɾȨѝEӉʈΠqxι×Ĉѹ˵',
                                                                            'уŶȊȤӺ\u0381ʳƁĠ\x85ұȲҳҌΚ»ȫͳФiϲϒт#\x99µǢϤġϠ',
                                                                            'ȗʲĹ3Őäʯ7ĨǪɰʝ\u0381\u0381£ʬÆŧɉ}ԦʠΉӡ·ҙǟʢɟȟ',
                                                                            'ԀщˆÏſӆ@л\x9b˰·ԞɌǙɈͼ%Ύҍыɞ±ӔĵОѫʠʈԃȜ',
                                                                            'ƍ\x80ϰ³ƀʍӁˉcǿɻƋѳԣŬћŉҩʊżÜЩǗɰ½\xadɚҧĐō',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӏÑ\x99ѻΝ˱ȘĄŴϭкѺ[ΉóǈÎrƆʠÁѴǉńʤĥϧĽκҺ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ơ?¯Ƞsńƒ\u0382ҨʼıСΓҒźưʺʷҡǷԟљħʆˑϡēʚáƯ',
                                                                            'ǀ˗ɮȸұ\x82ʅnˁ҃ҨΎӷέ˓ЩЀԛµɽюɦ«ǵĎҧƭȬϥƖ',
                                                                            'ȱϩϩіԍЙӁ˱ʶΤͽԙY\u0379ýċ˲£#ʁɦȜǎˑΐŠ%ԁƊȼ',
                                                                            'ŏʯÜǙКѥɬΐrԃϒĶɛȿҸa×\x99Ɖ0Ҧ͵СӭɄѲěϬ¿Ұ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӲӊĈϔқӐƽȸøjӸҜɬʅҡͳ¿ЌŻȥǋʣѐѯɽżȝӏӝӥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -8456.882767423522,
                                                    },
                                    },
                            {
                                        'name': 'Ȑőːȳ¶ƱɌӹκϦïқ}ʛлĝŇɗøǸόΫ˅ϯԐ¦оК4и',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.555847:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԛӼЌɟƍȰԠôѥˌϮі˖Ȧщĭҫ˨ʞũɌΫƾƙӍvтũӧņ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǵÏӋμƣȮœ\x87ғñʵȬʻϵȟͿκļŖęԞ\x86é˚^϶рԉǈÐ',
                    'message': 'ʡƉ˩¥ϰΘǔͱʢıҗǯ˝=ȱáЇҖЌЦԡƤñdªͱƅ9ȂB',
                    'arguments': [
                            {
                                        'name': 'ʰŖƏıʂ˅dӉʓżÐYӈԩʞǰӹς',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2841933444037917763,
                                                                            -8640642667012736720,
                                                                            1828865279113570777,
                                                                            -7138756307674311832,
                                                                            3384307436664845593,
                                                                            401203882105397959,
                                                                            -5482630200376447761,
                                                                            -1124652605391579638,
                                                                            3058972280610113388,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Љ+à˝ƈ΅т²чǦɖ¤ƭ˰³\x91϶ǜϼҙџϧˢˌЈӉJσыЩ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2979682787230568150,
                                                    },
                                    },
                            {
                                        'name': 'ӫӷĽo˯ѻɍ§ĚǛƗɻyѾɥȩ\u038dӽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            512463.47027765855,
                                                                            -59912.17064144496,
                                                                            281152.37851477443,
                                                                            806865.8356871174,
                                                                            -42073.939338757475,
                                                                            190484.0951413914,
                                                                            813181.5907920212,
                                                                            715847.482534477,
                                                                            769622.3288369292,
                                                                            796401.0865048271,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǧƿƐ϶ŉΉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5028491247314737003,
                                                                            8372749885278819078,
                                                                            7398140353008109314,
                                                                            -7307015704093126670,
                                                                            7032751199846931316,
                                                                            8911924102044437932,
                                                                            -4115807963617126302,
                                                                            5543036076647035464,
                                                                            1673163157336216900,
                                                                            1497883148107610131,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƛ¼ʬɵӷnö-¥ЋμǳԑвÆʰ\x8eӅдȒǫȁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʧӸӆ\u0380FãàĳÈʮԢǨДƟәŎðäкʼÚʵԣNǬͰԂǯѸɭ',
                                                                            'ƶѷӚǏơуǝϊƷʹȹΝѢ¹ɈʁĦнȳѹɸʎЈǌРƐӳ˜ĉѺ',
                                                                            'ȍnϨҠҞίįĩӑӝѽɉɎɤȘˠĝªȄąћԒҹȉśԄГʖњˌ',
                                                                            'ví+ϭϑϮѺ˴ȵǄ˚ˁǻɸ\x84\x80Тї\x94ҜơǬƞÈC¨§Ӣȶ²',
                                                                            'œȱĴϦөėвŜәþҹǋǼЪӧϮĎǵɫéϵϫӌĈѝ6Ģ˗ХȻ',
                                                                            'ǶʈʉʄȾӺьЇŜQ˝ίϗΫ£ʽː.;ҲΔϺªаȠŊƶŧʞ\\',
                                                                            'ЬѾ\x9cӪpʥĢƲԗπĭҏȹ˽Ӥ¡ѓǘҫțȃźЃůƶԍ1Ͻґ8',
                                                                            '#ƁѮwø\x9cζѐгSĒƂ\x8dȧЅΑ±ЭȝȭɩˁȽЭʅǕƗюKΊ',
                                                                            'Ϲѣҕˠӳɯа҉ļ˾ĀϨОДŎǞБҽ\x92ҧʺΌ¥κХϦԅEō\x84',
                                                                            'Һ°ʘӃņ¡ӖӘƴѮϦҙр΄Kɡ˨˫¡ǁΌƎʂˊǾüAӂǿǽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɝɿĕ\x8eŨ˟īθςΥǸӝϕȓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1896950533388928921,
                                                                            -2260941824409860089,
                                                                            2052926015267804012,
                                                                            -2333257422964001513,
                                                                            5478547239001669433,
                                                                            -4933516205205091875,
                                                                            -1014927945988438410,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΞђʗϮȫǪʜњуҸŕˏД\u0379Ϩɢα˻˸ɛЎũ\x90Ӈ\u0380ŚàΜģ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            ':ǅҖХȬɹhɢΆ͵ѯӽΞԘѸX/ČɶʺűҦąͱώЬǴ\x85Əˑ',
                                                                            'ͻϘʄȺɲȹbɨƮƽˣωϴȥԔѬӂ\x81ûϓ¼˨ԔɹƖΆ¾ѱЩЄ',
                                                                            'ɼџˍҁΝčǇÇ˧²\x9cΛΎϺșǑͶѭɻūǦԬȪĲĤƐqĤİЪ',
                                                                            'ƨϮшȘѝ\\ǟӦԓʕѳӌȗ˚\x89ϮЗɓʌıˏˠ\x97½DŹɫ¶Ɔɽ',
                                                                            'οЉȇѻÆȥQʰʓȣҽŰ˙ѱϱϲĮŦҼ&ЏԌ|ӲωӾӠƲМÇ',
                                                                            'ЎӏʾŃƏЏɘˍŤҍАǜɘԫǄȄԥАΚ®ѕŐԙȹ˔ƒzš\xadş',
                                                                            'ϊӒǍϒмѪϐʆ)ιFȽԖrîҪƛǏłòÂȢϴ<ǺǁԠȓҨҨ',
                                                                            'ίɶėΙʈñіИïƔ˓ȳѻ3\x9cѮʥ$ɠö¯ʂφ҉\x9bʞ˾š΄˞',
                                                                            "jιχӳeӸ'ҶŅ¾bǵӔҖ҉_\x94ү˜ҤήΡ˪Ǟ\x91sӔÍʡÄ",
                                                                            'ŤPЊΨmʥbƮҭǚ\x84ϕΒƅpӟӫãФÏ÷ӬяʉԌƞбΐʙõ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɊŪъεƟΙҠ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 909750.6831551349,
                                                    },
                                    },
                            {
                                        'name': '\x83ǔʝ˶tɰŤΊgѳɦ/e!ӈѢΥĆŴŜ2ʲ΄ӽʤƯ¨ρųą',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.559197:+0000',
                                                                            '20210209:222854.559226:+0000',
                                                                            '20210209:222854.559235:+0000',
                                                                            '20210209:222854.559242:+0000',
                                                                            '20210209:222854.559249:+0000',
                                                                            '20210209:222854.559256:+0000',
                                                                            '20210209:222854.559262:+0000',
                                                                            '20210209:222854.559269:+0000',
                                                                            '20210209:222854.559275:+0000',
                                                                            '20210209:222854.559282:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӰɨłѱЏͱΤƫ\x90ǩԆȷƾнȷΑӈҼфϐɓӝǞȯԘ\u03a2ƸĕΘȍ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÕѺӝŲŏԜШ®ǛѬϠ˂țĮѼũ˛ˎďÖҨɤŸʝʸòѻˉƭӣ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ґѼɂˡΙʞːҳ5ĿӺѦɮƿÁМЮůŭҸ*ňǉǼÏÊʸӮ¼ʬ',
                    'message': 'ʰǣ]ҧϩȻǻΙҳʷԠ@ӕ˜ȼякǵδ$Î˙ąΑϓϋkщ˃ѯ',
                    'arguments': [
                            {
                                        'name': 'ȽОϖϜñϝ˝ώɥлđˎĥİȶ\x89Ԛѣӿŝ˦ʇȜӗӤƎϻĦ¢ϱ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4130811325563459146,
                                                                            -8562638752234997477,
                                                                            39599583425702835,
                                                                            7105599557537748328,
                                                                            -8702555254349635365,
                                                                            4107390431274091956,
                                                                            -1487096996703945678,
                                                                            -4472994706970740601,
                                                                            -2091649432808873957,
                                                                            3355573873187187115,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѫӓɔ˨ΕɮԃȻΈЁ\x80ӑǹп\u0378ҰͶϼŖүÒ˽',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 190730.59564110741,
                                                    },
                                    },
                            {
                                        'name': 'ǚ\u038dϵӈÅγҞҳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ϋϙ0ǡϼ¨Ћ˜ΛƗǡНŖ˷¥ǵ4ƳύСҨӗ´ʖКǙɕӻřĹ',
                                                    },
                                    },
                            {
                                        'name': '¡šӖˁʶ¬AьȍϏͺ˙ѸϕҹʲzÌǸЯn\u03a2zɎ«ΗԮЧ\x99Í',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͷ`þʍυϰϹİϞѹǾĜÓŴѲҟȠʆūŖѾ`˔ѴȚƙƋҿșҋ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.560918:+0000',
                                                                            '20210209:222854.560936:+0000',
                                                                            '20210209:222854.560944:+0000',
                                                                            '20210209:222854.560951:+0000',
                                                                            '20210209:222854.560958:+0000',
                                                                            '20210209:222854.560965:+0000',
                                                                            '20210209:222854.560971:+0000',
                                                                            '20210209:222854.560977:+0000',
                                                                            '20210209:222854.560983:+0000',
                                                                            '20210209:222854.560989:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'äЙʖĲȄ\x94õʞʚˡͱЎѬƻǐѸԩƏǵ˶',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            925849.1748452518,
                                                                            431526.6946926605,
                                                                            587771.5506283087,
                                                                            308403.16983665375,
                                                                            965400.4180952453,
                                                                            474534.3977301228,
                                                                            590621.5286318741,
                                                                            294437.6945294524,
                                                                            575970.5253804505,
                                                                            905006.0741321146,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǤjѱχĬg^ʛζӰʯʖU¯ÁʩӧȽǬԙρŁĦǦŸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6145801255843752916,
                                                    },
                                    },
                            {
                                        'name': 'ǥÌΡÁ¸6ьȸOŲˀ˪ԝɵƄ˟\x95Ǧ˽ƸƦГƳƏ˚ҫ¹ŬШΞ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ғćɳłĻyɅɽǡˇїϘ\x9cԡƆѡǦΰҞ)ǀ\\ϨҺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'µтƦβǇdũĆʉƨ3ϼҩԂΕˉаӻǗ\x7fç\\ˮ¥ǦϗӋКҩˇ',
                                                    },
                                    },
                            {
                                        'name': 'ú\x84SѲӳҠƂ]ʂ4ʁȦʬ\xa0ɞУɟԉΐȆХǡŀȉЖŌȇȶşō',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.562800:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '´ј͵˄þҝ"ʨʓϥ҇ˡȆƗȌ˖\x9cѴ\x9bş,ȈŧɭƋҁŒҶņϩ',
                    'message': 'ŐȾψӗʊǝΚǊɹϢĺƃñȿƘʌҡ\xadϙΓťɼѻǞԛɨΨîӰϢ',
                    'arguments': [
                            {
                                        'name': 'ƨАȻѯΉŃӅlи½ӝȖΥ˴ĖȺƾÊǢʎ˩ԛЄƁșŞ˕ƃŮɨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.563684:+0000',
                                                                            '20210209:222854.563706:+0000',
                                                                            '20210209:222854.563721:+0000',
                                                                            '20210209:222854.563736:+0000',
                                                                            '20210209:222854.563749:+0000',
                                                                            '20210209:222854.563763:+0000',
                                                                            '20210209:222854.563776:+0000',
                                                                            '20210209:222854.563790:+0000',
                                                                            '20210209:222854.563803:+0000',
                                                                            '20210209:222854.563816:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˾Мѻ˸ȸƅҎлұťǥȽ\x94ӀяѩǇȌŌѴŇȭϩɚƀҀÇνßĮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŷùӵ\x81ŮʩҸùǠ«ǉϳԀѾ˅ʎǨí>ȮÛкȁűƕҭ£ԉϭa',
                                                                            'ǖǨǤӗʽĿ\u0378@"ĹҔҩɹĨȍ«Ѣʨʴƻ˪ɿĞưɗ®ќHÙ͵',
                                                                            'ӯӢʡҬ¾йŴϨĪщùΓ˱УϠԃЉШɘȤ˪˸śѲϒоӯΑ\u03a2Ĺ',
                                                                            'ˇяzвțǷƇźѴѢŔƝϧуǄfѻЧˣѝÒΓƮĿӼƯĲˬȗʰ',
                                                                            'ȃˁ\xadɏɔϏёǚʢȽ\x9dĚϡÉÏфǬrʐɵΰđ=ȣϽΈΈԗѼҀ',
                                                                            'ȷƕǸe˔`ɜ¯ʑ×ɍǤԣĮϩ҄˃һ|ӷԥӊƲΘ-ќÚҁϩԙ',
                                                                            '˖ωˤªĩŃʁǑӽɹʄʵʰɅÎҪˌԒԍĕöldғĐɂД˯Кǈ',
                                                                            'ϜѹņÉǈ͵¢ӧ%Ļ|ůШθΗ\x85γТÌБÍԬϯʿЁ\x9cʧƳԝȮ',
                                                                            'ωĊƚϯԫƻƄô\u0380ӶƟZʘ˂ԌŔўȣϯǐǞ\x95ϽÉŖюοůӻε',
                                                                            'Љάт˱ŀȻкưǳήɚȼǗЯɂЎԀҠο*ϴŹҁοҊҧìͼϱ)',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǐɔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8826792184776661001,
                                                                            2179116871264607027,
                                                                            -6248198949486191655,
                                                                            -5851027878579513700,
                                                                            -8538810053802897127,
                                                                            -5993775555184722169,
                                                                            8099114937050576295,
                                                                            4519934355711387888,
                                                                            -1624759136521481153,
                                                                            7839482262698876234,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '&з',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΘȎŻŇȎďХϒ\x81Ԏȱѻѕъѫҽν˂ŕŴ˦éúȚȦŇɉϦõμ',
                                                    },
                                    },
                            {
                                        'name': 'ȹχѤÒɸԑΛѦȄзͺľñ\x97Ѷҕ\u0381ѶGĒƿ¤ZгςøĻ˦\x90π',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3786510847368926143,
                                                                            -601119863484481413,
                                                                            2225794602829873671,
                                                                            -8537085628422917704,
                                                                            8262062462418058162,
                                                                            -7813998021075623873,
                                                                            3697497405117787268,
                                                                            6448071772181813559,
                                                                            -4993007635855484778,
                                                                            6030122468136905534,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '´ѿɖƿӧҎʂΣΗˑRƹ\x7fǳɴ҄',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -849064915776325916,
                                                                            -4590653756236909648,
                                                                            -2241087084965896617,
                                                                            2336215286844904168,
                                                                            -2790296794202855723,
                                                                            -7425387900974994566,
                                                                            -1844249259019520810,
                                                                            1647053033557336223,
                                                                            8543619821886944809,
                                                                            5595809567086645360,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ўзʅѵәϤѿvǊʴԠ*ϝԑĒŃҥKŬҲΑȖɵ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӋРƼщ˩Ͱʃ¸Ƞß.ʈ +їɢđ\u0382ƹ÷ΗѓЀ˒ǲШБԂ²К',
                                                                            'ÙɿσĽ£WӠŲϡϥҽѱɷͺуԜɖŪ˫йĉѾмϘδÅ&ǯƬǜ',
                                                                            'ɶgʿΗǽɗƑͳwǴúĨӖmʑгqϽtʧŘкȌ\u038bƪˌ\u0379ɮëɟ',
                                                                            'İƚѻÜӶϗāƑLȉΓΔȵˣҊžƏĸƈż҉НρЗŏˇȆÃПÕ',
                                                                            'TˊɾŤαԝ҈҉ɊϙϕǽҕČню˔ύËƿʌĝ\x8cόǜǒʁƮđϾ',
                                                                            'ьӥЏʩ\x83ȫΎϒȥU҉¢\u0379Һï˯\\±ɴҧí-3ȈѤӐΣ ƻΙ',
                                                                            'ɭºԠȎ[ĮПĭƜСӡŉȲϟϡӸԤʞԍīʸĽȩϔϕԅːˮԄϛ',
                                                                            'Ƒêӂӻƥс\x8b˙ҡʓǤ\x92ǑČҳӁűŅʊƗǑϳљӃ§ҍєcȟþ',
                                                                            "СӅӭʐÑҜ<ɉɌųјƥǝґƫ\x80ʄѬ'ÄbǠ˵ϓō˷ªӨ`ԥ",
                                                                            'p]ȴþĚáţΑÞǓӡ¼ǒɂЈϒ)Ұ\x95҄ҽɧħϋǫƫӭƲȯȧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѱɂήČԢχɮІʎɛϓқÀěǂɕЗ%FӠYƬżѷϾŁƁɳ˟\x97',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1831796731089468523,
                                                    },
                                    },
                            {
                                        'name': 'Ý´ұϽĳƵѾԄ´Ȋ͵\u0383˗Șð\x95ȻŋҶÊî~ƺѝť\x9fČÐʚƀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 902046.2782432721,
                                                    },
                                    },
                            {
                                        'name': 'ȩΗΩҠΖŃѣĖɰȖЂɚɏȞąļʫӼѯºπ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5168430307389282413,
                                                                            -4741195900287577898,
                                                                            1194009904487868712,
                                                                            3509262346877785351,
                                                                            -7319922348130300456,
                                                                            7239776500523023024,
                                                                            -2003755342094394673,
                                                                            -4195318245893269938,
                                                                            6428605497676839580,
                                                                            -6805499921990426998,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '}ϳ`S\x9bÚ®ӝƤԃԅјƽɯnȗЎũЖҬɮ=\x83вŇȱĸ˼ʻÂ',
                    'message': 'ɎƴRèɇѣВƐʬTŪǔʁÎȳΖӤԌȾÅʩĴȓeϦʭʋ˴˟И',
                    'arguments': [
                            {
                                        'name': 'ʞ˔ϊĠʹǡԊcǽΆoϭиƸͿҤǅгɳʸҝϗԭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3039640880489524417,
                                                                            -4450648944486544257,
                                                                            8913864284211692666,
                                                                            7734188912580246298,
                                                                            3197462793085369105,
                                                                            2728375448904149323,
                                                                            -1652728806888022016,
                                                                            -1005378795914450787,
                                                                            -3703037430039872501,
                                                                            -9146809014855831449,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŠφÔϸàЪţ¿ΣҶɝÐĄӎџWδȢӌƂȥӮȥϹ\x86ϊ϶ҭ˗Х',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.572771:+0000',
                                                                            '20210209:222854.572801:+0000',
                                                                            '20210209:222854.572810:+0000',
                                                                            '20210209:222854.572816:+0000',
                                                                            '20210209:222854.572822:+0000',
                                                                            '20210209:222854.572828:+0000',
                                                                            '20210209:222854.572834:+0000',
                                                                            '20210209:222854.572840:+0000',
                                                                            '20210209:222854.572846:+0000',
                                                                            '20210209:222854.572852:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'žԪȒ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'đКľ\\\x9cɢʬВԉǁԮ˷ӥʛùΈZȁҺѸƬʻăŃǄ˶Žȱӡz',
                                                                            'ϨIß3ɠу»˽ƀĤÀĠѮXӟOƽԮȹӃŖԥʶϙɆɃԛʕӮԣ',
                                                                            'ɽ.\x90ǒʻÁ˥[Ō`ńĭ҅Вĝ˓ѰƜK˃ǶşȥkӆÎΞƟ²҃',
                                                                            'κԈΫĀȹˤƆşȫƇϿ\x8cđʠįυ\x86ίҫëх\u038bҍǴӄľǺѷΟȁ',
                                                                            'ĮĻq˖ǒǃãΝɉŶɱȴƏ\x95Φ]΅ƉÂx^ӓvϑǉø´ʯіҦ',
                                                                            'тáӁÍ˜Ƙƍø«ȫƑβǤӜłb\x7fʈͷԃȃÒɚӀǏ\x85ńđ˚Ÿ',
                                                                            'ƳТԮűӳ^фԦ҄®ф`ҚӿЬұЖƠʵ\x97ТҪƶǃҰѹΉҎнś',
                                                                            'ùΥԈӖʶ˴ƼЪҐӷʌЦΤʒȷӧϺĕɁȐĄ˷ǕƪÕщʸøHd',
                                                                            '\u0382ϩΚĝâ\\Sԃ·ʪȄ\u038bňf*рӃɻӪʐʆǹȹʐѓ\x94Ӧǒɲk',
                                                                            'ԜӧɞӻӷΫžӷԓâͿȜµŖOҺĞЏƶЦLΕÇʹ϶ɬюčÖЁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ů\u0378ȠǭȭWaƼ\x85ˑĴģ\x88ϸĽѡҦҾԎЙ$ӹǏ\x89ǡƓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.573789:+0000',
                                                                            '20210209:222854.573818:+0000',
                                                                            '20210209:222854.573826:+0000',
                                                                            '20210209:222854.573833:+0000',
                                                                            '20210209:222854.573839:+0000',
                                                                            '20210209:222854.573845:+0000',
                                                                            '20210209:222854.573850:+0000',
                                                                            '20210209:222854.573856:+0000',
                                                                            '20210209:222854.573862:+0000',
                                                                            '20210209:222854.573868:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӚøŜǂԇԥҽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ëІēϧΆњ\x94ԃс',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȑԚʰ˻ŠҝʷƊɕƮԉ\xadΟȚӞΗ|ӤξϺ\x88ʟɴƙ#Ŗ҂Ȧìѐ',
                                                    },
                                    },
                            {
                                        'name': '˫ȗȅҬǍӀiùǯȒϩǄ*ɛɶ¿8ëЌ\x95Ʌ˖ǂˌμŪīԗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʏǂɂ¿ȲӐѡӀӆ%ǷmΑǳɅ\x8aɠŝδѯȟ1ҹȤıſǆɪ˝ɓ',
                                                                            'ѣҋƕъϺG\x8c϶ћҞǺÍxԂǏӪȩ҃ʚӬӋÈǄҩʏԁͰÅŶv',
                                                                            'Η\u0382ҞɿϖԈЮƴǑĴͻǨ˶ƲЫϢƊŤħóϟŚR\x80҈ԏ¦АǍª',
                                                                            'ïЀόүњǕАŨѤэАȏ°ȩҁŞȴ£σΤӌұΟǧΰѥҢąϱҸ',
                                                                            'қ\u0379ǐЭҕĖҸόӴȲ˭νĐԩѐϋƈîŹҏåѿ\x9cӡҞа˷ĄŁέ',
                                                                            ':ŔҙäбĐȫʭ\u0378҅˽ѩōǙʔ¯ƭþǿӶƩÛʇ8ɺӊˈ\x9cǅǿ',
                                                                            '\x9fϪʽŽΈҪ+ÖĨɑʕѐϐɎɨѬђĉèō˓©ĻǨ5ҳƞɝŔ˜',
                                                                            'ɞȣћY\x89ʤǛγʌSȜ\x8eʇeŭұɐ\x83ТøÑΎѴЮϴĺŽʲҾц',
                                                                            ',ʅɕеѕ×ѰȒť©ơɞɣҠӏѧɡʵ˱ÉƲϓÀδˑ\x96ɺɌɬȩ',
                                                                            'ӳÍüϛӞԐѫ1ġҗԌ҉ҩͰѾŉźѝŧƵªəüԧСǔ˘ƥ˾\x9d',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Éoǳ˺ƧԤŉȒщŶï&ɼϴƎƬˆѸǻͶȣɸϏŋtǁ#Ԕӕǝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5441339317563823376,
                                                                            -2497315654967520534,
                                                                            -527117883422357398,
                                                                            -2728435610994135393,
                                                                            -8287859308134742747,
                                                                            3631556695606830809,
                                                                            351007241880200405,
                                                                            -7182881667563036577,
                                                                            7516923163036303952,
                                                                            2874938331384086081,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ':úʍȷӠɷΩ½ǄnˣǷæφϙōȋˏӼǺϛƷƅЭҿ˦ɻΓЗӿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.576359:+0000',
                                                    },
                                    },
                            {
                                        'name': ';ўҝԉѹyäДԇɐɡΝӭ}˚Ϛҹ˒ʤѣ\x83҃ʛʻšĦ\x80ňđ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȫԭàǲӹKĚʫϘĀӰǲͱǠ®Ϭ\x9fʚʐǥ%ӚĳҾѹʕμƘǭȎ',
                    'message': 'ȡцϭóÓΥȁūŊϱʩŗ˱ɣʘkÓ\\ȎйǯɾӏȗԒıϋʸŚͿ',
                    'arguments': [
                            {
                                        'name': 'áΙˑųǎЧΞ\x99ȥΥˢǳȳϴ>ʙ҈\x81˝ǂ2ŝšȶ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.577166:+0000',
                                                                            '20210209:222854.577183:+0000',
                                                                            '20210209:222854.577191:+0000',
                                                                            '20210209:222854.577197:+0000',
                                                                            '20210209:222854.577203:+0000',
                                                                            '20210209:222854.577209:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЭчцɝщȵƷŕҞƤ\x7fʨР˛οϷČƋȺМ λїΰϧήʚΡɳԓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϵӦ?ĩωūͽ\x97ҮЖƾč©Ƅʡšύ\x84Ӵр=ĵ;ΔkԭÎ¯ǩŇ',
                                                    },
                                    },
                            {
                                        'name': 'ˎgǭҳÛ˙ȪũÝèɳQȴɇʴа\x99\u0381ȧКʃҵ>űŝ˽ӫȥǢ¨',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 392625.5092560927,
                                                    },
                                    },
                            {
                                        'name': 'ԞǩˀÓʱǾҖ҂Ͻϖѷ\x89ʫӦШҵҒŖȏĭSλǃδŌҨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.577730:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϩқЮsŁ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ƫƷÊjǤϾ+бɖ;ҢҁUˠǥӈγưȩȡЛʚϾȝȲшƃ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŨƾʣóӸɒωͷ˖øàŀƭȱǪļȍκʺόŅ³ɒɹËɴƞɻƗİ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.578343:+0000',
                                                                            '20210209:222854.578355:+0000',
                                                                            '20210209:222854.578363:+0000',
                                                                            '20210209:222854.578370:+0000',
                                                                            '20210209:222854.578376:+0000',
                                                                            '20210209:222854.578382:+0000',
                                                                            '20210209:222854.578387:+0000',
                                                                            '20210209:222854.578393:+0000',
                                                                            '20210209:222854.578399:+0000',
                                                                            '20210209:222854.578405:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѻ\x89ȄИ×ή¤',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 267306.039668825,
                                                    },
                                    },
                            {
                                        'name': 'ƆΛåÓѶɟƿ=щϧƈŠϲǑҙүϟ.ΜéȶΟ˯ʫ\x88ϡƨͿԚϿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '°ԣƵ˅ԩЭқlć˦ΆĔΖȓԊχϿǗҟ˖#ϑͽӐ\x9f˃\x85οȀЩ',
                                                    },
                                    },
                            {
                                        'name': 'ɷӉɯЊş˼ӿ`\x93ʅǳ¬ϒφѐ+Ƥҟ˪Eϔȼʜғ\xa0ŝȩνѕϴ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÀϊUƅ3ŉѭÈ¼\x94\x86δʀѠϝʩɒʪØɆԥǺŴŪ{¯ʰҙАʹ',
                                                                            'ȶԍƏƖɒь\x8dƓеêÛђЯʲóqѨʢÚΗ\x8fʚϨϔвĄȧΌʛɐ',
                                                                            'ɴҕӖîѫʖˮʟӷbŲѳưíїčÙÂҀːÓТԗϖƒ9эӀԠӊ',
                                                                            'ϺƈˬЇP˂@ϔϹČϷËȦNӁHǊГɺӉӯÐ"Ʊ ǚÜʀүӴ',
                                                                            'ƋʵӧġάÒԔ˗ǋȿȢΑɈѢӚjžŒЃƖӶǻԈΣː˜ΑЏǡ˺',
                                                                            'ѝƋćÐӾǐŪҡ£ɳʭű\x9fԜĆǑԛҾѬɪѓʺҢƔȡǝďÝʖз',
                                                                            'Ϣˎĸž×ҜƐöάſƏƀƻǭˇ˫ƯӮΉˊпŁӱɨłӤаҺȧɞ',
                                                                            'œĹԃӭҼӅ˽dβБϒԦǦÏďПЌźд¸ǞɠƃƊһŇ˧Ð˨«',
                                                                            'ū*ʤZǍӗЂǮŒǘʨ!ʫȢΧƁəşˑұҜҞӬЯϐҧ+Ȕǩł',
                                                                            'ȪƘԓθƕHƊɠӽūǔɖԭʀˉʽťʖ˰wԒŲҴҝͽĂɰ˄Äю',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¹\x8bˉɬҨĸўǅ҄ųЬĢӈԀâѓƗü˱kßΆ`ˈƜ©ϭƖˆĸ',
                    'message': 'rĥƎ±ŖłɪϲȠ˅éđӡìϘŐČɈс˻ƣƛЁΟӍƃЁðʮƉ',
                    'arguments': [
                            {
                                        'name': 'ԧϩĊŲˋƄҦȼѼʫǪVӮώʚȗłƋĜ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            821940.0886991118,
                                                                            88465.76042168128,
                                                                            632916.0886351096,
                                                                            990164.1890045172,
                                                                            461080.6414718949,
                                                                            735841.3013530307,
                                                                            536953.4296526338,
                                                                            760626.0820376183,
                                                                            564975.6409894235,
                                                                            485288.9202620323,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'τŚȄƔ͵ӛ\x87ƚѾ"įÜҹԫΕģԗŃG)ĕˠàОѦðXҥϤĄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.580004:+0000',
                                                                            '20210209:222854.580019:+0000',
                                                                            '20210209:222854.580028:+0000',
                                                                            '20210209:222854.580035:+0000',
                                                                            '20210209:222854.580042:+0000',
                                                                            '20210209:222854.580048:+0000',
                                                                            '20210209:222854.580055:+0000',
                                                                            '20210209:222854.580062:+0000',
                                                                            '20210209:222854.580068:+0000',
                                                                            '20210209:222854.580075:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʇӨ \u0383ҟg˰˥ȭӓҁ;Ģˉ]ӳӅΞЕĿɢɝ6ŉ҉ſӗľýΒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 405904.79571088316,
                                                    },
                                    },
                            {
                                        'name': 'Ѵɧӿƀǥҳʼs',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4422158864311859560,
                                                    },
                                    },
                            {
                                        'name': 'ɜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8851382809116016040,
                                                                            -4913902379439657377,
                                                                            7086135514105663430,
                                                                            -972900208190670235,
                                                                            2416605839234116775,
                                                                            2702128854413082747,
                                                                            -236776894382421485,
                                                                            58012344925805272,
                                                                            9217306346667965801,
                                                                            5669929440328170587,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǾėʌɹĆǛΨŉ\\ΐɌϹĨϢȰɻĮǡҶ\x91ЕŻѓƍ%˙ѩġъʶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2627770125700111932,
                                                    },
                                    },
                            {
                                        'name': 'ƃѪҹ˔˯Ƭʚòϩґ\u0379ƽԑĈ°ҏФÔČȀӍǗɑҿѼƻ\x86ä',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '@ϊƹӚAΪĔʤ£ŢȻ\u038dδ΅ŴȕΡ˕ǾƪҥȽōͶο˲ƾōԮ˘',
                                                    },
                                    },
                            {
                                        'name': 'ҝ]Jɔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.581182:+0000',
                                                                            '20210209:222854.581196:+0000',
                                                                            '20210209:222854.581204:+0000',
                                                                            '20210209:222854.581210:+0000',
                                                                            '20210209:222854.581216:+0000',
                                                                            '20210209:222854.581222:+0000',
                                                                            '20210209:222854.581228:+0000',
                                                                            '20210209:222854.581236:+0000',
                                                                            '20210209:222854.581245:+0000',
                                                                            '20210209:222854.581256:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȟʨ\x8b˩ӞѣÖɩҒƅхԔŔ\x8c˵ϚđϜҽżoȮƟҴӍÝɞŗЕN',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÛәʻʅɳĈ8ώ-HΊǹ˜ԋБɛȸӎ=ɧȁèȬÁǪʛӰD˅y',
                                                    },
                                    },
                            {
                                        'name': '˧ʵȾ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.582028:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŦӱYˋӶÑΌ˂тДҮьӧīѣ÷œǉƘБҵ˦ӔǼόǍïúѺʥ',
                    'message': 'ʙeɷǤѼTāԞЃζ˟ǣɜʾʃҎÍҽЉ#ƹԊӤ΄ɫџwӟ҂ɗ',
                    'arguments': [
                            {
                                        'name': 'ӀàĶɬԅԛĕъ´ӰοūЮɔӂñϙԁкǇãҁÃ ĩБԜŤӶÐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'WѹЋΡʿȠԛñƅŽēĩˮVѿҚˁȺǷέǩԋD҉ϝѸyS\x90ȧ',
                                                    },
                                    },
                            {
                                        'name': 'ŅõϗǗ\x81ͷʱáшƳшёˤ\u0381ĴЙȘΐ˼Ǽ¦ʛ®όύʵɲˢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2321261705102992508,
                                                                            4389266259401664861,
                                                                            6007376937361180487,
                                                                            2491758342049398831,
                                                                            -7832112285613162892,
                                                                            96473305510485198,
                                                                            -7162861805781575731,
                                                                            -7090818245137663905,
                                                                            666434673229033906,
                                                                            7489420019813730151,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'фНµѯ0\x83ʓƎǃEˮаұõԘŀ\x90q5κҍӛʞү˕єȳ¹ƻΊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҹЩȎȷwϤ\u0383Αč\x91ӷƀÝϞîȚнҕZ\x98˽ѽ7ĚӸӛεÂǃ[',
                                                                            'ѡϖγ˗ϺǬЄƽȒxƮƁ6ˬѰǠÄӿȞˊƄϝϋƨí3ѬϕӦĊ',
                                                                            "ĔƤȝŻԌԗ\u0383ƦȏųȭLѻԊǧɗiǎũ'LøɜÔ+ӤŻĎí\u0378",
                                                                            'ˀŴ¢˱ϼӿ°ǄGҵɛϢϏ\x7f¶Ұɩ΄ǬɋʈɦźͼȈ\x98\x8a¤ɌŮ',
                                                                            'ʨҡÕǈҾɜΡŤɇ˩ԏɜǶPоӏ˸8У΅´ʳÈúɶϏĢōҤ?',
                                                                            'ÀςӅҥ;ˆӪԧʩϚȦwϫӘ˒Ĥү)ƬӬƂKįҽюŋ\x8dĈϻƢ',
                                                                            'ŚыќėϣҟǳѡΰЗñɹөӼԘ˟ǥ˚;Ř˖Àӿ\x90¿ѕϘƕɷЗ',
                                                                            'ҒϺ˒\x9eýжaƜ\x9a˶2ӺЩκɧһ³ʕ˾ʠđƯѹ͵ŝ˅ѡǼʀϻ',
                                                                            'ɻËęЃĎ:Ÿþ˼Ԥϰəλ¤ȶŅė\x87ĐӍѦȟӥ±ҰɉʉԘã\u038b',
                                                                            'ē\x9c#ҜјϜϤ҆кѵ҉úѯɄðΛҧƭƃжǴl҃²ӀȼΨ҃Ыˮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȷƮƗơΑԠǛγͼʓΦҕoӲ)ԐԏȚ˂ʃФȀɻ3ѡ˷ɣŲ$I',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            489995.19397008093,
                                                                            -25563.184895668834,
                                                                            675729.7797605459,
                                                                            374782.06678602705,
                                                                            108656.74769780194,
                                                                            794123.7640758074,
                                                                            -53259.49994733905,
                                                                            905582.3215346369,
                                                                            507514.49202390795,
                                                                            966831.535162665,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʝĢIоWȃƵƋƒͰΘϹѓњ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.592395:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ͷǭҏɕƍϒӕkӵɸȡǒǩΉƘϭϕšžƢѲǇʢŀɛĘȗ\u0382*Ӗ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҝһά΅љȗˤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            229411.19024331664,
                                                                            389745.0448929912,
                                                                            343793.9882697217,
                                                                            928756.363339987,
                                                                            215289.80563735415,
                                                                            627331.655363861,
                                                                            -81144.28559751358,
                                                                            173282.64730552863,
                                                                            642213.1042875501,
                                                                            127373.08461666488,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'p\x99ρӨϢʛϴѲшƀÙƌӄϨļԃș˔ͿɡРѦιχʲʼǒΘʎѴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9095288142808409889,
                                                    },
                                    },
                            {
                                        'name': 'ͰȞ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            404156.796589133,
                                                                            604595.9662654187,
                                                                            129829.21418565483,
                                                                            483016.2910696113,
                                                                            827003.2594371885,
                                                                            697411.898633927,
                                                                            120077.52878105521,
                                                                            -15013.410686136514,
                                                                            959345.2820606139,
                                                                            -81824.90413081623,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '(ĀҤмľƽҚʷțҢȬ҆Ͱˉҋ˳ѤƆϱςЩʸǼØўǶЂѠiѡ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
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

            'identifier': 'ЃƼȅˠϻ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'êȏ',
                    'message': 'Ә',
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
            'name': 'ë˗СϮŸɼ\x91ѢώƱЃ΄ơт/ɉƗПðȵɀϰлǦʏԃϗMҵ;',
            'error': {
                'identifier': 'ϽЏťɰԡÝБɿ±ѰȟκǇЪӜȂɽ«´7ӝё;ÿġžҏɻǁԔ',
                'categories': [
                    'internal',
                    'os',
                    'invalid-user-action',
                    'file',
                    'internal',
                    'access-restriction',
                    'internal',
                    'network',
                    'network',
                    'invalid-user-action',
                ],
                'source': 'èâВͰŌȦɑƿĿǌˑĒѣϰĢʿѐǻwììӓȼūѤӹԮjʐˠ',
                'messages': [
                    {
                            'catalog': 'õĕɬӂ+ЫŐqԣƧ¦ƙƻŢӲɇэ*ѷĄĭə˹îXНɛȌЋŃ',
                            'message': 'зюӳǀѹĹưş\x86ʜԞŤП^ŤɪсȡѤΙ¢Ѧ҅ԏʂʜ\x87ê˨ʸ',
                            'arguments': [
                                        {
                                                        'name': 'ԕùŔι?ÖBƑƦƙƆϫmæɇͷП\x84ʣӹО\x98ο',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5820579246267331426,
                                                                        },
                                                    },
                                        {
                                                        'name': 'KÄԈϯÝ΅ҢΔ.¶ƚ/ԩѼȽƤǣӶbχʝùŴ»ԗдөɺʧԊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '©ψщƌ5àʨҪҮ҃ӡ˷ʞҬԥʒΟw»\x9fк҆ӪїȄǫǱ˙Ԣ˞',
                            'message': '\x99ʟҙ÷ʳƢѐ˃ъőЛσCϘŵĆ\x86Ӆˮ˯ɘԡϥȸѿɕˡΠɻŮ',
                            'arguments': [
                                        {
                                                        'name': 'ȘȠԧϫͲηҴΦǒ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'РµʌǄXiπčȤßGԦp˻ЪӌШů%ͼʱСΕȯ«ɆƓûҦö',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 494081760195874141,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɵԙ¨ßŌˉҌѵˉϝ\x91щǲôӛɎБАìƄΙњ˱Ѱ^ȾƿІќɮ',
                            'message': 'ʕϐԟзǨΎźOЎԙĮęπϿʤ˶>жƊЃӂӣsҕӓʿ˙Đĸч',
                            'arguments': [
                                        {
                                                        'name': "ǅԀƿԋŅˊͳčӅʱȀъĝɍƄӿˍĔŸƹɄóԛ'ʹŬʠiŷӊ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩƨ҆Åç°ѶϊZ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÈŬʎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԐϑПȐɽ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϏɦυLæ¹ċӈӬ\x81ʆƄѦōǥȆĜ˛ƁѶÃҧŰԈͰȥҦǘȜӦ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'еĆşí-ҳӚʹ˽1ŝǫͰ˧÷ìлťьĐҭʥ҉ҁɽɺTӢŕɼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҋʟȹҷӒˋ҄%ҝПľӻ$ΑȘÕ˛ƁΐӽфҔȃ¿Ðˡϒ¶ќĔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋƗѴ\x94Ü˴\x8b ǯϟőµйƍƺӿÁĭ˂ϕӭɸǺɮҀȽйĵBө',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԩ\x9bζ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƛˊIőΓыʣΤԤđŜҸѯѰȓҧɅфҴɔŜѼVҒ\x8eĉʒÚŐԈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӠŧγĮӟȏѠűιеӪĺ\x7fҾѫҐҭԔǪ\u0381яԀӣɾÜǅȂɑϬϫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɨďϜˍԤρ*\x90ƇӎԊǶЇ\x9dƯCǞΕìýäҥѸǓȯĉ4ӟќɄ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʙľΤɺZ¶ʒάˋһÚȄӖȂk;īЄϜʚɽΪѽЙŋɋ\u0380ƧΣT',
                            'message': 'ЊųûԐȥӤɟѦĿˀFȫԔѬȴˮėӓ\x87ԭȠ4ҲÅǟІƓÇŔɞ',
                            'arguments': [
                                        {
                                                        'name': 'wȕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '͵ΎҚЄɌ΅˸ԎҐťȣӆϑӊҞкώώÑƓ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɡæğÏňĆŹŕΚȘƚґȒuɱɽǍұ?¸ЄѢoĦȯĠӢəȈʳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8aιβɥ\x94ƮíHӶm˷ǈôÌ˦ЯŦӮʺѿφ˂XļĹŃIŰĎɭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.528559:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǔ@ȚĔüƇ҄gς΄ΊEӥ˛θΝƼȥμͿùpʧΣȲԍşŠǼj',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǼѯϞǥϒ£Ӹʴʪ΅ϲӛȬȭqǢƊѪ°ҟЀ¾OЉ˺ЭԒ^ыˁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x7fČҬƱŠ͵τSфǩσƩӺѢŏKÃсʝˏ9ΙȆѼęåƛUĕɄ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȋéВåfbћõˀÑӡФχť¼ƈWŘǫфϔάмŤȨԀһѽԗʸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 863530.9550754494,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԟͲ^ρ\u038bЮҷΫȯĦ¬φҭƊɡʆȍŏҤŶ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǹʮӯʂȐɱчƠūͿʾҤŪáҭȇƲΥˌѳѯ҅KҙNƽAѷБԦ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4220015173048705627,
                                                                        },
                                                    },
                                        {
                                                        'name': '¸БšłΊňȹãћѵԝқЖȬԩОӍïħ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 33473.65082415039,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'À\x9aΨǟ3Ѧ\\ĦӽЊΐȮɺсяȋѷϐɨƹPōͶ҉ĥϕżČɔд',
                            'message': 'nÂǶКƛƤŎΔ΅UӒƝӃ*ϖȎήŐӺ϶ɚǦƔ˂Ηƣȫáſѧ',
                            'arguments': [
                                        {
                                                        'name': 'ˠŝķ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɌңҴͼǺ҅ѤźɑɤˏϽƕŐǻ͵ÙǊ$\x98ҭɓ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҪǨ%ͺѴƢɸS\xad',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.530238:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѴҤȠǒżҸAϯ½ɏтʸӈÔԛ²Cʮӏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'МʸӼϺԠ˦ȴzƥфŵϝŀ:ÈëҦӕHYЎɨĤӿӛȡǛДʎм',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȕʟіѼϤϦǮѡɛ¾ɞĸѭ»ҢќƈυψѓяΆԔÁŒǜњ˘:Ȓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˈ;˧ңëGó\u0380ú˰·ġԆһœ\x98ĜÆрʟΘѾ&˥ѤʤϗĀɏò',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.530698:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥҼúϗӿňɷʹӕţʻʘƜϳȬкƷ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƼŭêǰԙҎҳƹ˯ҊƞԋϣԗÛBƾʀĽΦɟϩҏìԔǵƻŉҫь',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԋԨƑˈцŕȤʚѓуӪ˯ӖЪĸμƵŁЇŤ϶ԩθJԇƮԑѸХȺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.531129:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '{Ν҄҅цζҳϙaĝӸaпŝʙƬҎӔʦʲȍʳҊФǨĨ°ҡÜ˶',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u03a2ԁʷӝŽȏȐлɇAǝúΥSĲѹŨђχͻ˄ƪBͶųԌʦ˽ͽʺ',
                            'message': 'ҵЛǹ+\x90ȈƤ˥ΈEʔƍэўʓԉåАƈðϗĩћΒyӨӺĚЌϞ',
                            'arguments': [
                                        {
                                                        'name': 'ɡőƋЧоЋʞҐΥK\x9fǿÁǾʆδ˜ҒϦ4ǐ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.531688:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '±Ѥ҉˂ШӋӄΗʋԨǻ&^ŲԊZ\x8fĳДӰɉʍΚȥĦ\x82ӽČɏǟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϡǾЀ˚qň҉ŹϛҶЇbĉϱʭʲˊĈєԞǭȰҟǺʢԃØѥǽA',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4216081975541930370,
                                                                        },
                                                    },
                                        {
                                                        'name': 'åп\x9cƙ\x89',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¦\x90гėćВϾāϱƛҫɯĢçōǹԎ˼WbӏύȬΥƫɞѦƤ˨΄',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 797784.9104709715,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɩ\u0378ʞх',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ēрŏό\u0382Ĺ\x97ɋųѦǇAǂʛȚ˟ѪƋ˦Ĕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґƤʭϿȪҧº˫ǫћ·{ξη\x8fƘǈӺgϊҎƟIԏŏ˙Ȑ}ȟЁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҕƵ\x87¯jɱ\x88˜ӻϜĉ=Ψ6ȟҌҨɶÎѤŎ0ƩƣҀ\x99ŮҬƾ\x9a',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x7fȡ\x8fæďӭԕt\u0380ιӨƭÒȈ&ȪЙҞʋȽň5ɑҬϔŠˮșσ`',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧΚҟſƴƧȆԩ\x9aҹƪ3ΑIȌөѹǊɶȃӝФǖ5',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1939093659256252558,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '9Ύǋ\x86ψӺȥӹǇζ˔ƬӭğӱӛȁԐ\x91ɡŦŪ\x9c±\x8eԘÌɯә',
                            'message': 'ʅδӦɀђӼĤȅĺ˾ŋӐ\x97ɍǁċɘÀʉƞ\x87҆Йʗɲ·ϜЇ8Ѻ',
                            'arguments': [
                                        {
                                                        'name': '˅Ȟëѯ\x8bԦƼΠΣӇ\x92êÏÊǸӍΎьЧђƈ˕ʊӦȬƋȧÔ÷ɐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȲΤͻӠӵ\x92ʈҖƟγŗ˫ǐӗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.533716:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'îҚȺ4ӆϐɎ\x85ÞȵәҼ=ʹŔƆʻıǒƮζԖԑʽōʈИҜĝʘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʴĺџȓƶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'жъƿӲŘȈЎҬѴϑρρ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'vӐǁħȻɾ:ɫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӳ6Ԗ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȺήϞ7\x8aťѼŋͱԄƈԌʪ\u038bƧşŇĘɀ\x88ñЯӖΗԎԗйҭқȲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3444800110250019007,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Kǧɥǡʈ¬\x88ĲҊи\x80Ń҅ʿƱʔĐ˂ĞȣňƚôĔȨďMŸϑs',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ź˼ҟəӪɀЃșϢϒЫÀԁͰӖүƘȡ҆ʨҲˤґÐʗ\x90ǐϧÿЕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'p\x9aǚӈôΝˇ8ȓ!ʎͳƸˡŠ΅ǫѰNЈuΥɿDʾǖȾǲɃÌ',
                            'message': 'ȏÂˡԈɴ˹\xadѠ҂ӡұƽþDǫ\x97ʱǘɫѣґӁ\x9eɆǍ\x87Ęğϰ[',
                            'arguments': [
                                        {
                                                        'name': 'ϲϊҞҗИkτ\x9eĽƢòʧӵ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƱϜʽʎƎʞ˞',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1729268511428819332,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΪȳɳʞǜƮİtĝЎäәŬˡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6181955473278052963,
                                                                        },
                                                    },
                                        {
                                                        'name': 'δӯť¨ΰ7ˢ©ӨǅɃԛǡɗČʱҞ>˺ŴǟҁМԦϷ>˟ȘǼô',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'rАϔɼʇɊƟюҪҲĸқɺϲŊɛԔŦǔ˘Ƿҳȗчˀƴҥ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȨȮɸѯ<ІƮӦѽ$ҌɟИЁԆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǍӲ҃ǆ,ȔƗȭϽɝĤҖӽδÙȶђľ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'υɭƟӴмѫȰĻФÂ9\x94ԕɰÒƜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'yŎʋԎɔɀĜőЍ?Т˥˼',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҿİҠǍƾ҆Ƃʉв',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҡԁδҽͷ6ȨӼÕҵùѲϼԀуϟѨϤʑÍѠȟԈǸƷĨRƉŷʮ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˋ9ʟ¾үįɰԋаԃǤʉȼϸ',
                            'message': 'Ԁ\x87Р˂ϵȲЬƸСΦΟϊD˗ӖʎKȭх@ȇäϡ\\ЅȺǎρ\u0383ʽ',
                            'arguments': [
                                        {
                                                        'name': 'СԀҧЁϋϗːêbΎҤ˞ӛͽħ¾ħ˭Ɇ\u03a2Ōɓϭʶ;ҳһĄкȍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Щ´ŘӑũɴОʲǚ\x95тΪќ˴ǩϠѩΖƹʨԀƓÎȢƀʽҪ:ÍƁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'тӡԠЏ˭өϘÎбғБΫ˃ӔԠǴŘśГһН+MѢɁ¦ǫȬ8К',
                                                                        },
                                                    },
                                        {
                                                        'name': 'hԝаЛĴұ˶ɸʁÒјʔśӭԆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8400716921713253405,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϚɘҪϫӛǼь:ŌZҒ˭˝΄òôåХԗӻɐˤ;ķȞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x85',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.538121:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԇĕ˶\u0383ƽ*ÖӣʒʧЭŘЫƾҲ+˨ЅϒҰψĆηƛ\x87ȆЯήԥį',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǦҌѰӺǝiē¢ǹӽϸдӣрȑɠɑåĨ\x84ϧVԇTɛ˗Јԁԡʽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĽυƋʽ®ȺǅҚĈ\u0380ɱӍρàɧÖʦ)',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊƖ˾ӟ3Ҥµӥ\u03a2ϜƼ˺˾Ƽ˧˵ԠҖúŷԞӿĮʍƸ͵ӹ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԘßχЊӱ˟ӰԃĉӴɡδȩŏˌұһƜUϖƎżmɖȉԢўҥ_ӝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ǻ˶ϢŐČƼϸд"ơɤŃӷˤͺӹÅĢȺĤ\x95˦ѳČŢѧǔёǝĎ',
                            'message': '¨ɂ«Аƅǅ\x8fƖɛрʱʑϞɝӓΞÛӴʴ҃Ż΄ȘˆYȜƃɠ\x9bƞ',
                            'arguments': [
                                        {
                                                        'name': 'Ї0ψbą¢šJϸσԊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŝΐ¹ϯŚӇƝ˧ƗҕêѩСǥБљ˛ԟʖбˡҎű҄ªҼ\x83ĵ˥ƚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͻʺͿΐėʎ\x9d',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'čβǇͳѲ\x95ÀΛέʫφҿϵÖ*Ú²ʺëџѺɟѹđEˤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 698165.2720566331,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʌȲʪЕWʭʴbǍ¼ѠưӷáН҄ɻŽŉԁˤЊ²ɨƱ\x9fGæҰʌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŚԨϫmϴÝǕҝƹΎˑźČϷЃǰϼ˩ǙęӅVȳżȷƣ8Ó¥Ū',
                                                                        },
                                                    },
                                        {
                                                        'name': '˒äʟƧɪǟȊӟS#ż˟\x98ͰχԨȒәƶǵǢĺжԇĤϒ\x8aɥGɠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԒҷÒͷӺϤғʊȁӏˋşɕ˺TҞĔ˴Ϛӧɖ˶ӻϜԅİ!ŭԤҔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4662916764099857890,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ôjӯ˒ԪѽҪȂʷȽñòķȼǙ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'iΦ\x95ÝǪԞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ρŅη',
                                                        'value': {
                                                                            '^': 'float_list',
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

            'name': 'ĕˣƝ',

            'error': {
                'identifier': '·ͳ.ѧԠ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'Ѱɲ',
                            'message': 'Ѥ',
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
            'event_id': 'ҝ˵д·ӯÐȳīѵş9Θϭɷɰӓɷ΅Ô;ԞFНȱˏ¥vЊǳɸ',
            'target_id': 'âĐ˃Nɰû\x88Ҋ˨Ĝ@ѯΎҌô\x7fœӡǥǄŠËɼЀÕʎȚϴʒȮ',
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
                    'event_id': 'Ԍ±\x92˄$ɓΗѥс¾ҩɕ¾чϞíԫвȠȗğӞɬŵYυԌϫʀȠ',
                    'target_id': 'ҴГϋɽӥԑʵЗƽǠӓӭ\x85ĦưǴŉԭŨηźӔ҃\x8e!Ǭ',
                },
                {
                    'event_id': 'ŘʮмӈˣʺѶҙŋΧÊƼʔкF@Ή"ЙλǍŘƁǱ҄ƟƮĚõǦ',
                    'target_id': 'ԭ,ѐζӬYȃ4ғƥӬMԭ\u0379ǚηˬƁȲϟĈòæʯǶԘӶαϻЪ',
                },
                {
                    'event_id': 'ºНǓȟņԤʵþҬϴеɡɰˠӣΧӣЯ˕мŔұӡКʝʿʐпˍͶ',
                    'target_id': 'ƙӃɋĐƦ˜ήǢ',
                },
                {
                    'event_id': 'ǈī?Lҧвȵˠ˓˚ŘΌҹɿаFoˡŬЮйɕːȔоЬΕǲǎɹ',
                    'target_id': 'ӕǶԮʷс8ɘGңµƘη\x8eŌΜʣȊßϾÙɼʳǿƛǡǱΧΫǺº',
                },
                {
                    'event_id': '3ǀē¬ħǱȣϐáɜШҍԨʬάӒŪʻ˴¼ҀȶɧϹЈǬÏ<ɜɘ',
                    'target_id': 'ɯҢy·Nɛ˄ΈȺǞІƾҮ~пĬąҜӘšӻưɜΫàҠȌȲƿΖ',
                },
                {
                    'event_id': 'ǹΞʊјʧşɻδƈϩŐӒ҄Ưɉ(ɥʼʉϟʮΣУɡϲ±ƞŦӬƎ',
                    'target_id': 'υЛ\u0378ȞɐҲԓñХъrГʮҙɴӣQȭ˷ǡmĴƦ\xadȭ҂ŪӒЂƷ',
                },
                {
                    'event_id': 'ÅĵˉЭӾ˙ÇÐԌЛ$ɝȦԂì\x94ͲӚέʪӳѶŴӵȕɒɩȤ/Ι',
                    'target_id': 'ǏӔďɑҳăԂϥѱģĲːӚčѰҸѨӏ¥ǎɰťҁXȲƺƩŸɇŴ',
                },
                {
                    'event_id': 'ӪǺͻïӀƻHӆɊŅǟСςȤǏͿΥ˪Џԧαʵȡƶϸɽɠżɴʞ',
                    'target_id': '\x9fȐ\x85ԥҔϞǻГъʃё˔ϸ&ӓr\x95ӺmΊŐųnĆå(ЯǐӮө',
                },
                {
                    'event_id': 'ƅÆԀŌȴʞԩμϘƈĭǰϖ\x9e˧őʇʜ\x8bĩ¬¹ќƂԂлɮŀɡî',
                    'target_id': 'ŔƐɶÃlɣόҞʑΠЉƙɮВζɹĕ«bÒı\x80ƄÐɈӊ@НĺЧ',
                },
                {
                    'event_id': '2ȋƼӴπȲнӟҁӚʌɼā8#ɰąĘșȏ\x94ʟҢѻH7΄ϰÚЙ',
                    'target_id': 'ăˑҶΆwӛԎƑĘˠ˔ԞʎʙҸӮØʌŷ\x85ȇ˾ӌ@ҝƣϥëӼЮ',
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
                    'event_id': 'ŉ\x84\x99ʯ˄ÃΕđόȌ@ŭіϠԌĹӸº(ŔыжĜιȈѯǄȌ҉Ԛ',
                    'target_id': 'ʑºҦņυΐЭжɎϲΘҢǹ¶˅ȚϜӇĸTΆSóɢ˜ūɴԪИЇ',
                },
                {
                    'event_id': 'ЈЍįӏǊʁʬӾҼϺӴѐǥНʈҪΤӜ҂Ϳ$ͷÍŋйȟʊ˪Ϩɡ',
                    'target_id': 'ʋQ\x94ˍϏσ©«ӹпhțɩƚȴү¥Ȝ;\x87ȼʇҏżЄɄÝБĎû',
                },
                {
                    'event_id': 'ʅȳ%ϴϾΖºšëĦжӞӈˍiӢǆϹʄԁǵԓʗѢʹ˱Өăķђ',
                    'target_id': 'ǧɶϓmʆŀЄ\x88΅ţтԣЍРԇƢȵБΨҋØZ˛ɉÀф΅ÿάϬ',
                },
                {
                    'event_id': '0ΎŷƿЋʺʟȅӊ\x8cśΣÂӁĒСƀϘΞΛҨӶԛȚ˟õϱԝŐϷ',
                    'target_id': "QңҾцʻģ3ĦрƼȃ8\x9eы\xadŒéтӠŦ\x97Ш\x9d'¼ΥƉğDє",
                },
                {
                    'event_id': 'ˑʗ\x81]ʲ&éДӘˎ¿Ƨɇ϶ÞɯķҍÅƠĥàª\x97ĶǱ\x8dѪÉϰ',
                    'target_id': 'ғȪϪɧ˫лҚȞĒȏÃ6ѬҔɎ.´Í˘ɶϥԎˠɈшǵʞƟɕŚ',
                },
                {
                    'event_id': 'чƹҬѯŐƛƏϥҀǜĐХ˕Ƴųq˝˙ʇdʉѯͳƲǣ)˚Рνʙ',
                    'target_id': '˄ŶТєΗΪʤ΄Èćȵ˝ǞǃыѺͼ]ϕ˲vaÆͻʕǖҪŻÏԐ',
                },
                {
                    'event_id': 'ʸϚԪйϒѝĒǉЧȱ\x99ϜʷΉӱťΫϭƛ¶ɩϓǃɲϊaǎЧ\u038bØ',
                    'target_id': '%Ėђĕ°ͱƧҳӫ\x88ȯжƾÏΈѭÁӻ˔јԕ˜òÅˠʭ҃˯+Ȱ',
                },
                {
                    'event_id': 'ԋӟʴԁҩҽҢѐӽȉŽˢͿMʤķ;Șȉɽ\x95ȗǋ\xadłĄ/ŤҊ˽',
                    'target_id': 'ϦȐ˫ЬˑˢʼϿԣϠËΒWԮ\x94U\u0378ɴîѦԞƙǉǊ˪ЅѫºҦ\x8b',
                },
                {
                    'event_id': 'ŐРƎ\x81nÖɕ\x8e\x94ΒҚġÛω8ΎԆ·НɈӧХίȻҨʊřҟϼћ',
                    'target_id': 'ŰƩƜǛΑȝѶќƆΈŀϧҶϥǶĚͳĮҪӡҭcˎÑ;їǍυˣѩ',
                },
                {
                    'event_id': 'Ϻũ\x90ðςСϒǌɶԙ˅рȷ±Ɩӿœˀҁ˯ҍɭɣѯƼǤTӲ˪Ŀ',
                    'target_id': 'ͳԆ˔ŀìԡͻӿԇ˙Р¨Ȱʰƚȩƶ\xadɠЃ˸Ōǡ˪ʙĩԂϟϫĝ',
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
