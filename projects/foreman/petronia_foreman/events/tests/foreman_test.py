# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-03T21:03:02.360452

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
                'Ȍ[ɈƺÀ\x95ŖʼƸȟԩ˺Π=ʳŻ҉`Ԡ{ĘԣŏΧЦĵӠͷɝɇ',
                'ђÎΊtĆǈ9ͼǁԗbɚĦɵZʪ˥ΞʾŖɏ˼ӜҿϪǰӼГϏ˩',
                'Ţԭšԅǳ\u0380ҙŜϬR˫ԩΚԓǲ\u0383\x8bȔµqɅʏȪ˜iоԛſǏѿ',
                'ԣёŁϔУǧĂ˶Ϣĩï¤ӄʎʖɐǙ\x8eŝńʖϐJȢǯü˥ϫ˱ӛ',
                '҄ҫХą!ÛӴȪϪɺɠԂВįӯˌ¿ŌɡřкӮļȘ,ǖˏʧɃɘ',
                'Ҿ΅ĤǝϠӑŞ~ŤŅŒԨƽ\x90ʍ˔ʣ¶ˬˌŁҰϥϥŹȢÿ\x80Эǂ',
                'ҖˮϻÉć{ºΛeϧčǿʬΊӊŶŦǐĴȿʣ˕|ΐԘ҃ϘǲŐʩ',
                'ԫȏǶȤƱȑǹ\x89ԓ\u0380Ò\x87έȯșǬȜąǮо´}ӗŰĬǄĄƸȊŤ',
                'ˈӠʼ\u0378tөϸ7ѵа!áɽğ˲шPӅ˔ɱé\x85ʾģİPĆӼƺƁ',
                'CÙϣP;ǐϹȉɤƌŻǵþуŹϰɽϟ˪țӆԁŅ˱éˣȩӌìǠ',
            ],
            'source_id_prefixes': [
                'ȗĐѩƤǋ!ʎɫѹIҖ»ϸϬ¾Đ\u0379ƋԒȆ<X"ɔԫ҃ɛј҉Θ',
                'ҿMȢΕҁƁƝԠҖԇшŲǆӫσʐԉґĿΨĨɇäΟƋԭĐ˓Ϭҗ',
                'ƅȑȠқȩ˳eІӃʨҟϴƊνΗřϥήĽҩϓӺЎrҷςЭΨŭŅ',
                'ȭφɻȀ\x8f҄ŐӚÀɘҠΙ ͱʫӈǵϱȳͶκĕŪFїȀ˂ƶ|ʈ',
                'ѮhηПɉȃƺ0ɭ¿ȃɺǠ"Ø҂ƭ³qġMҌƭӉԤȊɟ҈\x85ǧ',
                'ƎȴġѲʴFˏʊрɖԝ˷ɷɟđ\x9eϺҜӋĊǽÝÐʤú˳Ӆ²ʖӡ',
                'ёŔɏ\u0380ȉʻ;Ɇʧζ˺6÷˕şȥюʍɜӰȷõɯʎLҍ\u0380ʲҏŐ',
                'ĹЖ¡ŜǤŇƩϽƃƟ˥ΉҴʶǦčŃȾǎĨЁǂʏŬǢ|ɳŏμ϶',
                'ĩȫʡҞŃù˼\x93ӼCЂϟȝŰ˸ɥ˙Ⱥ·ơɃȵқǓ¼Ԗ´Şӯ»',
                'ʷӋƆСɄ>ԧΫмǂ\u038bȑҴʴҩΌĒˤЖÓ҈MĖ+Ǚ²ʏӉϡđ',
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
            'action': 'ĺʕʈϫòȖH¢%Ȫɽɻʓʺ\u038bдɺԘÁȼğƆǪВłh)dɺӿ',
            'resources': [
                'ˌԎԭЗԊʲӉȧÉѪҟpϨӱáӕҵЉǅļdĄɴbΧӫĵ¢Ĭэ',
                'ģЕ\x8bіÇƚǽȒНjZ3ʜļɐŢҘчǽtŒ\x83˛ŀ˟҅ί¼īȽ',
                'ĜԉưЏ¥ʔȠǜŶŭÎŜȡōřĄЩʂïœό\x94ҩƀŅѸʈŪҠѨ',
                'ZҺʉӇš\x872ŭӛ\x95ǵӫҴ\x81Ńˉ˚¾ȂɌ¸TǦҔíԎѣʊþҽ',
                'Ѽ\x8céҗĦϹϩҫńğõѸˁťԠ\x8bӘɴϮˁ\x82дґŖf\x8aϴÝқɍ',
                '\xa0ƢĂЯғίŔəƦѓΞȆ~ɵф',
                'ҨΚǒѭˑɾЪʿ:ÙĊʖˆ\xadΔԉŹ\u0378ӧřȼғӲH˅<ǿѲЂ΄',
                'âԋŞǟưƟў˟ѣj;ԧɫɗƞѺӋƂԩяѲƠϙѶșϹϐӘɲe',
                'ǎϳπϚĭфđőӐ\x94ӢϋˆȑƤфҺʝ˷ҲćӸдѕӹʃ҅ԬǍӏ',
                'ɪ˹˺вǜӺʤʑ·ŖҢĲųȯɵɃһˏҥʟѕȸȦ\x82ϝÔνψƆЈ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ͱ',

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
            'name': 'ǏҬ»ѡәAʍҟІӒОȠјӮΪ˙;ˣϬĨƭˏбŚ^ѯÆҝ8ԏ',
            'version': [
                -7622934999948555992,
                -7345328848433876633,
                -6292627586251620919,
            ],
            'location': [
                'ȔĊϧŪȮʔɻȨФ\x87ԜĚƖǍɄşѽӄxұ˔«ҁ\x89ĐǤбӛγҐ',
                'ӛbЯӉƍ\x89ɪ¢ǔǔҀѧċβϾïøǬϼŏϡͰώqəĹȧɾ7ĳ',
                '҉҇ϊџǋϿB7\x81ɹΎžԑ¾ΠЩҹƨĪƂCʧΦг\x92Ьƣǘ¶f',
                'GαйӷϽɍӟϮǥѡŢӑΖö\x9d˴=ŇȽҲʾӋη_ǸăЎŊ˧S',
                'ЈЬФ˧ƆɯɒȜâѽǔƭeԊ8ԭZƯ˶ĠȱǛƨϣÜӅƌˤţԚ',
                'ʍȎɳԤ˶ӔѡЛǪ=ѼĹ/ƦâǮʩɷͲƦŤҌɒɵưʯōІþ*',
                'ɖΙĠǛЃbµΛ˄=љƆʌԫɔтÑЂ\x9eЕӰɠӂíɻʆ3ǫê˅',
                'ăѦĐΜʢfȨЇ˄Ҋʭѧӱˬ®ƳжʖƾжɷѷԛʼȗĄәšŧʮ',
                '+˝ĦƷåҩђӸϻŽԦºɑҁΏ˩ŠѻƚäȵĹтIŬԙǭ·ӿӡ',
                'ŅӏҮцȋȫǽ\u0383Ț*ǩЍҦŽҚ\u0380\x96ǋöϨ)DöɬfӪȵƑϾϛ',
            ],
            'runtime': 'ҐǝϟʹԤƊJ˪ěԑǬħƱĕѰԚ',
            'send_access': {
                'event_ids': [
                    'ϱIѼ¸µ¤ƨǔЙƎɜϴϹ˲Úг˫eς˭ѻļǀӻéǓɩʩɐː',
                    'ż͵Y"˴ʸǣǏʛĨĪÊ7Ã9ԝӅƍϰ\x92ʛŚ˳ǍӻĆρҟʺɠ',
                    'èы˸4ǓЯɵʷʹƚψŨ¡ġΣʑħÈǎƆXҁŷϋƮΟҍÙ¹ɼ',
                    'ƪǨțȩʱӠȦѓӯĶòęҿˮθ҃ǸҮѭϫƑɠ˹γǳпӮдŚҠ',
                    'Кґþ\x8dϲѩЭı«ӊщŸ˷^ҦӊǨ˯ӳΒўż\x90ĮϙӷºϭʀΜ',
                    'ͿȵѐЮȄêҳġƟƑϻÏƶʡšnåAǟĳχǤȒӁŘąʸ(βʃ',
                    'ŋrȫʉǺĳ0ƼÛѤжǳԈ˗ˢԦҰ˳ɫӰЪɒɭҽѧŉϽζʨԎ',
                    'őȭʆЁμÑʹԬӮȺШӕȖõɿ\u0378ԆɗǞˬʽ\x90εѸ˝СǆϑɄƎ',
                    'ҐūöȝëdͲľ\x9aɒÇ˯пяʢɌČċӦǹöϝо;ϥĜЮʧʵɫ',
                    'ԝѐЖδěΘȅ&ʓΠιʗͷ˂»ÅСʄʭσѭД˺ŻƘùѶԊԃƅ',
                ],
                'source_id_prefixes': [
                    '҈hΠЭɇŘ˘Ȟ`θЎˏŎȮΤŕϰĵћƝȘӚώ"ѧ\x7f6TϜγ',
                    'ĮфěӆӻħϷÄԒȳΧƉD&ͺΕȐ,ЇЌӢŝ\x9bŌԍÓ˥?ӳõ',
                    'αŪӭӂđʚрx҇ȖǩưȐƅ$Ԫ¤ƥӱƩ!ϥɋʳǉǚƞѭɴϼ',
                    'ĥȎĊΔ-ɞ\x97Ŕý΄ҘbʣΊũҲӈɇѣ¿ƞŔҐӂԒʓʵʟўɲ',
                    'Ȏñ(ӴԋĬǴРʫϣǍ9tрǛϿµ˪ɱŞфb˖ӺχԣêƴǼҬ',
                    'ÉʋяϐƌѮGd´Ѓǩζ³ȸĢƌ\x8bԊҵʜʶҏɗãԗωћԑȧˡ',
                    'Ɋ\x8eÿǮƄԒЅԀƁà\u038d\x94ѻЗ¹čĤīчѬͳʴγMρ,ȱѻKǅ',
                    'ŚíǿϑĿƢƄԏϪǆӅЌɣ˹ǯ\x8bΧДԇ·\x8fǑӼvҷҽ\x85ԕ˷ǌ',
                    'Jċ¢ԪŪӓεǐȴāˆϔӎǄƝŞҫʒϦιϻK˗ɛЅ\u0380\x8dǓӥԏ',
                    '¦ç\x7fϏ²ƼύĹĈ\x81δҥψɵǻϣχǎίҞќαԊŒȋʏўθԙҾ',
                ],
            },
            'configuration': 'ǹϯǉ\x89ņǰԝĶƌGǵΠɇԁӬԛԃßˏ)ŉeșϩȅԖȊȀȧч',
            'permissions': [
                {
                    'action': 'ʳԗȉËөǫГԑϳżˍ\xadғȆΌһʶʘǞϸӲĠιП£ҟſđ˩ї',
                    'resources': [
                            'ϗ\u0381rҘɪýƐ\x7f϶϶϶àαҧĬʂ\x7fӆѵϳƞƿ\x8dϊѧǚůΩġʹ',
                            'Ψ˱ȡ#ƇÎ½ǖҏѹƑФáȩ`ԛΚɲʛɵąeрɇҞҠǆͼƾά',
                            'Őġɾ¡π¯ƘѩǓƨʚǘßǌˎԆDҽѢӏā½ʗЋ˼ҵρʴ˭ԟ',
                            '˴ȂɤΏEԋӕƁϏɤˇęɏ\x93ɴχÜϦɗøʢɻƵŴΛщԕ{ԟʭ',
                            '§Ӄɏ~ǝū˼ыʢϔČƶ\x81ǵ\x94Ѝ ҸÚȬɿ9rFȬҫȅƼʀɱ',
                            'ǜьƼ¢γӻѾҢхӃϪɵ˻ѳÌēοȊш;ӃŉϡˇҎsяŚdȏ',
                            'ȶВƯȕ¢vϨȜҾҤĚ/ӕˁƐԩɂɈƯSʮϜʢǓԒ҅ÊȟˇƩ',
                            'ȷLȧү\x94¥ΙǖьқȭʑʦԘѰȆġΉԦˎ˶ŪȶΈÁьԎƜˣƧ',
                            'лàġВôԥҒǳνƌȭϩƹԦĘͲӮkѶԆδOŊʕɽɂňͲӝϛ',
                            'ʋёǔƦŃƆφΘўɏԅ\x82ҲĥМ²ҮŨŨұ˓ԮȂӆιňщŗƝˁ',
                        ],
                },
                {
                    'action': 'ӉZɜäăҶ\x8aѨȦɁɍǜηƷȪҴҍҩ˃ſƹʬġƷƌˁɘ¶ʻΦ',
                    'resources': [
                            'Ԥ˾ηԬүΫƽˡĎҋÁͱåƱ¨¶åĕҬȼԊƔҌʪŴΛġɤ9K',
                            'ғ?ĂdЭɤѪȑјɽƚůфʡȀϨIʑȺϺ}AiTжĐӶфҘҪ',
                            'êYǃѵřҩɜшƙK\x8a½`Ʉб\x99Iѯ˗2;ҥʬʌє*ԍªǡŚ',
                            'ɞӕdҐʙǃ҆ԝɐɬċʋjŅ-ſәK΅ɶǠ\x82î¦ȵƌԔóΧǹ',
                            'ӕӘ˻ҬДϘˬұӆ\x90ƑǃϣΡ\x9fƻэɤɒǏ/@Ϟ΄ѶĹȘţ˔ҝ',
                            'ɍīǮӀɪǜ®@ѐκ{ǚcțоҊˬÑİӂ\x8aҤ£BǷǡкԪë4',
                            'ʸƯҵþșȟĿκҵ\u0380íЯԮoȾШǕ½ˌ(ѹίʹȲƺ\x8cÅΣξÖ',
                            'ȓȧѩˠ˂ƸǏѽ\x81ʽ\u0378ěīъɗʜΐŷґҾьӧƢΊ˖<ѷȎЊ\x82',
                            'Ȱ¤Ţǝϵ˓\u03a2Ǒƒ˘ɵðł@˧ӗǮʢÉɳпȧǁʦēͽŃǋƵΫ',
                            'ŪţǛʿ$ˣƛáӇԢuԍɛiɀƽԢBМƎƭ,ǒǻǵŤԌƑӠъ',
                        ],
                },
                {
                    'action': 'Ӟ҂ӀӾtΐǖѓĝ¾έ0ΖԕǊßȬԎЅԭπӃɜǣʑ\u0379ƙԄЃљ',
                    'resources': [
                            'º-ЂѸɷЎϧЉ˴Θơ>Ӽңǅ?Άɿ=ŕĜҙ˅ԚϒƍɝȌʧº',
                            'ƴΊҤԜ)ĻɦǒКɌȖɰВʊVȝȜҡʪÇȟω¢ˉÿͼŉϖӖˇ',
                            'ҚѳϤÊ6λȈƫԬʙúΣƜê\x8dȨӧшʚ\x8eԘêӠÃƿˉѐůӿˊ',
                            'Ĵ\x8cǱə;ǑĀҊ\x8beǟΎ͵\x8aԮҤϟ>ɝ÷ǛêБ˩ԌїƆ½īɕ',
                            'ƐàνӇŞҀ˫ҨñҰЛɆѱƅœ\x93ʲȭҶ˥ѮǄϑǡȾǎƽѱ·ɯ',
                            "Ӧϰʳ˲oҚ_ɲ˜ƬĴõΎ'φyƋΚʭɓɍAΫaɶҞl˽ӆ½",
                            'ɸˬƽɈʊɒΐŝδ»ƝƣɄǰ\\˱ϜǙΪѴӻӹǺiҬ˱҇ԖˢÞ',
                            'ǡӷȏ&ӸƇ˦-¡\x9dѬ³Ю˷ˋɉì˙ùȰ\x90ӳҴһӮqѭiJС',
                            'ҽȃӰ˥ԧȥŷЈӧμĳEɣ҇ɚʬѾŨǮā"˫-Ŋ\x7fɡĖŊҦ\x80',
                            'ѹ˓Ҟ\u038dŒѝз&˖αζ҅ӠɸlнȕЩ˸ȜƴɉȔӫĻ\x83ώ%ѯЫ',
                        ],
                },
                {
                    'action': 'ȔÕǵѾПѐĄʠ\x93ɑ\x9aέƃȣѓϼŨԀι¼χȘ\u0378ZƤeĲ¨ћM',
                    'resources': [
                            'ɽҀєˍ¥ˬǭºȉҫїέѮǽʰП˄ҹƲƎɍɔɃƆңɘ´ʪʓĸ',
                            'бΕ\x93ɅŚʖǧƘƞķȯŖΟККˍ˥ĈˬʯәԬŜԔ9Ǿ˞ћàɘ',
                            'ҬӣҞvĞèŦΛ#ŖԇωјȦȎƊ©šИΓήΎǜʯаЀɉӊԭЮ',
                            'ýԛȄ)ѷǚȑyԚϏпØΊƳȉЊôºȅӚƭʾԩБʽǕÒ˓Ȟʪ',
                            'ƥӵª\u038dɃ*ÕbƷƍƲЫƝѰӜЦȍ\x90Ѥҁ¨«ĨɱũԠӆˍǟľ',
                            '£Ԧŏ˾Êчȫȵȥτԅ˵±ùџ\x98УӧΡȼНɆÇԞŢŶ\x9dȤϧŪ',
                            'ŝæġȍƛԩƿvΔŋԋЃҸ˧ʑŴѻǔRIɥφƱ΄ȅЩşËԖњ',
                            'ǱƹVоďêíΤʃӆzÚǨŠϧłƦʡӭ\x9aʗ˫țʙpȶ¦ӗʴͷ',
                            'й˺[ҀҔǡ$ў˅\x85ÂґÐʦԏӸЋҊͿΩǽƢԧċȳyӝȴѕӻ',
                            'ήIų"ĎȎǬłìŘϑΗϊңϰ÷łƢGх#ǕФɚЮ˝»τȄɼ',
                        ],
                },
                {
                    'action': '3Ą\x9eǦ\x88ȅ˾ҧɐІя\x9eĭʴͺÞγ\x90:¤ѨΝȧʙŕzǐQЙғ',
                    'resources': [
                            'ȅȷέцӿ¯ԙӕŲлυÇƎЍĲǄѩľϞǦeƣ\u0378ӝώɮ1JŪͿ',
                            '\x8eƾȎs®˜>>\x83ч˱ԂġȓǞѽӵŔʃ\x93˥ΦԑǝԁđӭӤ\x8cЛ',
                            'Ò˘ŘЫǩλ3łΊӃȰHЪѧԌʰˣӭ0ĽšҗƻġɐсѢƅғȎ',
                            'ΦʞπїǋƺȡɵӆԝυüˁƴϠÒʭ˪ınĢͰά8ǎò˺ɋ×ż',
                            'ѰРǦӚɽ˖ɼͽҐͱ ȡϦ£εӖŢ³ӂѻT,˅ԡϞʧάʥ«ȶ',
                            'Ί;Ҕ;ǉпԨƇãʾÃMɄÅЉͼϊӝԒѩ˶\x92ΚѩРŧφ¯҈Ԍ',
                            'Ŀϥʩъʌ˽ěʰɄŁđĖƷϳѭҧǗϝȓ҉χĜn&ӕtqπAѬ',
                            'áĎ¬ѵӇζYӻʅϧ˔ǗБҎӶˈȄDNԠɬ@ěүԏў˘ƀǳƩ',
                            'ǡĚ\x86ȢӸԣӠȫХȈɡʳΕӯѽǬƏ˺ѕƃМѲºѳǙƺŦҌмǍ',
                            'ĉŵ§˙NʁϡĺΉĲ1ҷӜʯǏeaѥ)όʅɭ>Ö\x92ӐTсʛҐ',
                        ],
                },
                {
                    'action': 'ļІΐ',
                    'resources': [
                            'ʴΧϮK×Ґ˄ɪơԓʯ˒јÌӝƜȔѝ¤ŢδҀ҄Ȅ9{ф˟хƙ',
                            'ѨңːǠœΒ˸ȘɧͳӜ҆ͰȮρӶʒӟҫ$³ɦԠĵъǮďİнĳ',
                            'ΔǀɑƮΠφ§ԣƸĬƬxǈҘСǁԘðʋѶϐǴũƔ\x89ɄɢxК%',
                            'ɔӅҬƴ6чѨ\xadƘТүЁƹŃƨ϶LҟƽɃ˴&ɌҧǬπțÛýͻ',
                            'ӡɗŇ˜ŜϰʃӒ\x81ɔƴŲɢɹǽсq\u0383ӅӥđθǾã\x94ɯϡϜƒȗ',
                            'бʥǐv&yxҺȰ\x9fƶҿцÆʘºЌĒҨĶˌ%ʄĘӺǐѪӄȈʿ',
                            'ĴűɏʱͲ\xa0νвʨŨˇΉKϹ\x8bƇΜǄʽm+¢ǤΫÉɮΣϪÃƞ',
                            'GɏSӬѵˏЅʯбƮҲɼύҐѝΥÛɡ¶ǏҺΤԍƹǑԞӱɺȊԨ',
                            'άȦ\x87ҲϚ\u0381ѩǬýȭ7ԗɼfԪȟĲ\x94ϘҊȩѦͶɧ²ɬÅ/Ӧă',
                            'ɋNȦƂҊp7;ьБОΰώɁr\x7fqɢҏ\xadġBθѼɋҏŦƙqͱ',
                        ],
                },
                {
                    'action': 'ʠφϾ0\x8dŽÃ',
                    'resources': [
                            'σ΄ÕΚǯѝК«Ζα\x9bÛļ\x97ԠќřҔԇΫsƋɹǦ*ԌƒЏѐɊ',
                            'ŁŢċʾѥϟ¿ӈ\x9bɑȔŘϢ˚ґ\x9dțiУŜǳĈ˹Λԣ˱þʟġȶ',
                            'ЩїȗȻȑȷԇƟdǻŠύǙʳϯΥҝҦτӍ|ҎĿˎȡθϜӤԃV',
                            'ѾħǻӡуRŰ\x93ɡиʅȯĝŝƬŲƃϼ3?ӡ«ѸРĈɹ˺ÉŚg',
                            'ҕƌǱӟʽ\x7fnЯӚШŹʢşń¢ŠˋȖŮΛεӆχÀ]μNɆгϦ',
                            'ƚ\x89ͷʢnËǮӳŀҫĭǎɼ˚ȼЬЊkζ4ьԥ˦ÚıʚċώȊͲ',
                            'ФķӶmǹСѐ@Ӊ\x90ȊȍȆÆϏȾǁϛˉǅϖѢćĘӈǑʃ±ŧ:',
                            "ΌҗȾѵĴ/\x87Ȫ¥ĎρйҮ˔ϮҙˊʦţԉɀѴ1ƃЕʚΰŅ'ǳ",
                            '\x8cͱɮ\x81χфӗԆʺѯ\u03a2ɒлƖ˔öҝóÂũƗϺ˛œɉѝόдȤӰ',
                            'ˢΚкȲȭίÑNiyÒúƋσ˾ҕʺҤҕŪŮ˧\x91ĮſľȠ}ЇǴ',
                        ],
                },
                {
                    'action': 'ǗŏαŻɏ\x7fϿύƬȋʬԡϵɛҿ}ԆԛԐQʒǴǚùѢɀұĺʸԠ',
                    'resources': [
                            'ɘɄŚҥVȘƔĲμMӝƍƫĳ˟aԚѺoωǀƜӎ/Ԣ#ǵЙĸt',
                            'ЃªOЪΝǝΟ¾\x85ʎͰģËσƩŏѼ\x95εÖѧ\x85ԈѺºάǎЅ\x862',
                            'Ȳ#˥һ·ɋ¢ɃϕĿћȹʹÓͲʨϨǶӔŰ¡ƺƕҭȨĄωҖĬ˩',
                            '\x8bΝƔųԓƳĵV˅Pŵm@ǲԇ4Ųοȳ\x81˱Ρǁ;σӖӎ± ъ',
                            'ӜÏϗĘτҭɝИ±\x9aĩɀӰҢѡȘЌƄ»ɐ©Ȓ˥ˢӹƬəю·ʟ',
                            'ɆԢѩʇϗKɽłŌvŮƇǇ5ԖÉŜ˖]ȝƳ˷ȓŤΒʙΑĜǖd',
                            'ԇǫĚɔʀȑ˭Өś-Ⱥ\x83Ҭ˪ˋӪԭɻƲĔжʗъǉЯщјҼqԃ',
                            'ԔƭѬĶіˇҲŭаʶɈ˄СԘёͻɒŊӶǓƟѢɁǦ\xa0ǏǓȤïǅ',
                            'ԝϷ\x80ǠЗɡ\x88˸ʫȵžɼǵΊțFӧɮϺ˺Dԙ«GѿĺȪǃâҡ',
                            'Ѫ\x8cǳʜìԦʐѵѴ\u0378Ѓ/ƶҎŜɛì˽ʏԘΓkȈѾĸӞ§ѠʫȨ',
                        ],
                },
                {
                    'action': 'Ӹœβ\u0378ҁ«Ľǯӆě˔ϱϥƯгѺ˺ѻ˸{śũ8Ò˫ԫҿːƘę',
                    'resources': [
                            '=ʉͷȒӥ΄Ö*ϨtǾɀÙēȩО7Å+пĎҦÉtЍȄv,Ư\x83',
                            '§ŨʣĲ¬`˵dϢнʃÈ˞ϺЪɘƳɼԠ0ϧŶ(ҢqG\xa0Îʆт',
                            'Ӟʛ҅ηȭ¸ҋɊчʮϗ0Ǻť\x84ƨêĺ2ЛɪѡӺіаԍȑƥŋʗ',
                            '¸\x9błˋ˖rY5ʅϹ˨ƎўƒIäѐÝƍĜʃӶļfĴˇƻđ«Ԛ',
                            'ƈҴNђÙ©϶Ӿы˘Ô҂ˏѐõûБŧƦÝɶŝüϚɱӑɩǀҤњ',
                            'ɐм˰ƍͽɇbŖ˚ѻʞǿӂσͱȪӔˡ]Ѱƻ˙ʹatóǵԏӴϒ',
                            'ηƵёБѦǒ\x92ѠɗȠņƝǾ±ъÅƻɮʉΥКđŽҝǬ·ƎιʧӶ',
                            '\x98Ď\x88ѩ˦ɒԫüϋˇĂ®ů˒ʣŝºʉǠŦфђ˂ǪíȝNӟϑä',
                            'Ί\x9c˘oҊҬʆχЌџÞųҢɸ¯аΛҲƐļ\x82˛нɰȫsџӹȁɕ',
                            'Ўʽň\x88ʄwŽѣΠќ˰Ӡɍ-шЕĢ\u038bɗӈ҈fƭĶͺ˰ӄʇљʇ',
                        ],
                },
                {
                    'action': 'ĤńѱťǸѽĄXϷ¤ú-фÀԄΉ(ǹǂȼťȾ˫ØşӎСΤĄ˺',
                    'resources': [
                            'ɪӢЎŢȴϙȮ¯éǔ\x90Đ5ӹȝӱĴÊĲγˁ҆ÍˡǐƮŎnѠй',
                            'Ěʼ&®dѠԂВϟρ¡¡ЊӖδēӀҥIҚ=ӵ˰ʦ¨јǘүðА',
                            'ϽσҴñҤ˗ΨǼтΔӞbǼ0ԇɺΨǌРȆþЇĀˠԖ\x95ı.ǻœ',
                            '\x7fØԦӌùȽɿʐqǺûɡ$ņ',
                            'óӗŉùЌҴӳę\u038b҂ϭФǤƕˊƶϿɻ\x93ɸͲΜŠλǯ\x9eʓɔ˃˾',
                            'ɼІƦȣҥ5нѥʽũӂȀůȌƖʒʞËʥӺÃɵƱĬIЋġKҿŋ',
                            '·ҀҚυЗŔȽǵƩʸϮΉĒҮιψƑˡǲϘӅȐǼqøͰЮêGʵ',
                            'УʡɲÀđΣцɀƚȎ˃sЀȅȶϗȲҕǠÕǱ2н˚вӤǏǁѝҧ',
                            'ƅҥŏ\x89ŤǕМӜӝ²øĤʃGӶђӗ\x86ĶǤōȵɾA˦ƘƘȤыȞ',
                            'ѺØśϽʪõґɤŃŐ¸ԈȊќčϽС+³ƃͰҐàӾчϯϹʫѹҭ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\u0379ȭũ',

            'version': [
                -5797198009705829417,
                -1397645124663517923,
                -8457136255656002644,
            ],

            'location': [
                'ԧ',
            ],

            'runtime': '϶',

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
            'name': 'čНȻԭӫǄ¬ţϦŽ·ʋҕЋɳпЗк˨ȹтȏо͵cŦMԍȡ\x97',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ό˒\x7f',

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
            '$': 'еǽǯƠǳЅÔӞÜҟț2bЄÅȞɬ"ǞԣɗȒŧÙϏȧƵȆ\x82ǿ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -574085937124355549,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 547420.6553469378,
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
            '$': '20210203:210302.304602:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '˞\x81+ȇБӐˣΌ¼ԨΘҘȥöĚʛĿ7ƶΥѰȧ6ԂшсΔ\u03a2Î҃',
                'IӠŊȐҔȯëӷűŰӡӤʓȝɑĳεŏԌȶЄȋǩҏκŉƷӍ°ʙ',
                'Ɛ϶HϜЧƙĪԅïԍƌbƭΩӌʥӲʤҜȑγɻEϩĺșӤӟҰʐ',
                'ϲĿǤϹțѩǾѬƖҤǕΨ\x91ȚɄȦĖÔļиư0σʺǎӘϙȘɏо',
                'ǋéɟʞғсĦИ˭˺ͲşͱЭϢâƵÉΈȏɥԐˢąʸ=ͳŚ΅Ȅ',
                'ʹχϪʘĂmǤϑҍnίĮǪΰĐOҥԢƲӊőϥ˸ƪʄƻɜ˵ҤԞ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                7317855657732479818,
                7279652017505638280,
                8147010915465548397,
                -2137654313860388206,
                -1144145420697529567,
                7059110309076153595,
                -8482267061776342847,
                -5452153210984221140,
                8694131937259510995,
                2620152840572333314,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                650107.661093727,
                528301.8841723839,
                933941.4342104996,
                310126.57861125935,
                271679.41786405235,
                -21874.50182188544,
                138448.0841896265,
                275498.4922119628,
                223834.2413728246,
                369018.9907619046,
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
                '20210203:210302.305452:+0000',
                '20210203:210302.305464:+0000',
                '20210203:210302.305470:+0000',
                '20210203:210302.305475:+0000',
                '20210203:210302.305480:+0000',
                '20210203:210302.305485:+0000',
                '20210203:210302.305490:+0000',
                '20210203:210302.305494:+0000',
                '20210203:210302.305499:+0000',
                '20210203:210302.305504:+0000',
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
            'name': 'BЙɞʏΡɧƶ¨&ˋƮϡԢĵʍǈƸ',
            'value': {
                '^': 'int_list',
                '$': [
                    6859543080001177587,
                    3770474221855264402,
                    -5135890470418587987,
                    -3852969687973762429,
                    7021640413658104804,
                    -7101945067627221274,
                    -4043716819092874607,
                    6478596886733408743,
                    2544858678317003588,
                    -7100146200908812272,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ȼ',

            'value': {
                '^': 'float',
                '$': 252492.87914992968,
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
            'catalog': 'Ő\xa0ϗȶÖÏϱŃӲΠðыœȫîϒϹеȱŇ)Ҩ\x8dͺѫюđĞюƀ',
            'message': 'ȔfÞTȬɗ®Ϣ\x94õñϿЉѿѣΗśьĺѯƾņ˸ҥȺSԎƔӓǎ',
            'arguments': [
                {
                    'name': 'ˮȌ҂ǨаɖǣΠӤԀȌҖӼŦѦśбӚӎµǘ\x80ӊҥƝ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210203:210302.301114:+0000',
                                        '20210203:210302.301125:+0000',
                                        '20210203:210302.301131:+0000',
                                        '20210203:210302.301136:+0000',
                                        '20210203:210302.301141:+0000',
                                        '20210203:210302.301145:+0000',
                                        '20210203:210302.301150:+0000',
                                        '20210203:210302.301155:+0000',
                                        '20210203:210302.301159:+0000',
                                        '20210203:210302.301164:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ҩʝұѶŝm',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'УȈʿѭ\x84ÕǤ\x80ǂ\x81ɌɅɂŤ¢Ωɢæƪҕ,ϟӯĩĬѲн˞ǀd',
                    'value': {
                            '^': 'int',
                            '$': -1911781883861587797,
                        },
                },
                {
                    'name': 'Ҳĝ\u0378чԩӤҟʕИыʠ˞ÍҦѲӯú\x9bЅЬ}',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        2774645286670587483,
                                        -2926250255716732517,
                                        6171967595793505341,
                                        -3010093602428088137,
                                        -4493045197149388127,
                                        8796305789214218504,
                                        -2215529745529427440,
                                        -8982511138496993053,
                                        -2269602914667004994,
                                        -4386032509144613668,
                                    ],
                        },
                },
                {
                    'name': 'ϩ˾ŠɘƱRrκπәÁϬŏǕυʯыԩѤƤ˫яЁϞƥïɈāιý',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -8272470440776094335,
                                        -8771959911462702153,
                                        362321103425519307,
                                        -7349107107026089637,
                                        -4316869530768947474,
                                        190017058288015296,
                                        -879454893370297940,
                                        5466977820685167243,
                                        -8232173676778278921,
                                        3303713738566623579,
                                    ],
                        },
                },
                {
                    'name': '\x9bJҰВřêƎѠˀɘǖǐЖԪːȍ˱ŚѨśſÆӀϢǓZѩÊƕȎ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '˂ĪzϚԆ\x8dԨвŴȼ$ʟ\x9aӍȑԚұʢǹЖӳΦÕʄЈʽƓԏíѭ',
                                        'ɵ\u0382І§Ƹƺ\x83ƢФTÉqѕ˨Χ\x82ϕď%`ϙ;ԠǠŮьѲǝĈȕ',
                                        'Ƽ҆\x97ȨdːǴǣόΨй\x9bɓȰɏǠƖϓ¯ǥŢίűǏʵˈŬ˦Ǭ¬',
                                        'ƂЙìҪҌқЍǚĿʼŠЃƍφɓºë¾Ѽ[úǩҰĂȠɄHτԗĈ',
                                        '˒ɁWˎÊǑCϨǠμȓʣiӱкνԌЦŝ¶ô²ǓȕĝǘŞЁԪΞ',
                                        'jϾӶϘә˧ȑǑͺģјɊϻưʥȎЀζ¶ȣŦɡΠтǶʎ³ɹѦn',
                                        'ˎГѴǐàǈΜ\x95ɡÿʷΟɿĴīŔωӉ?ӏѹҚĞүέ<ʖͼҿǦ',
                                        'qÕƊʓŘȸȻӆpɾõϽԞʽӹсeʧħ˚òϲΏԨφĚƻхΖǬ',
                                        'ӁѩȥǩÈƋƞǎúʜІ<ƖӌĳƃeͽυѲʱϠӉ´ҕɘŬϓќŐ',
                                        'ɴƩϲɌĽϓ/ЊȜș^ĠɹϰɴθķʌӔ˖χ\u0381OɬӰύʰȑu΅',
                                    ],
                        },
                },
                {
                    'name': 'ƫƆ\x96ňĄΛʝѡƐŭÀɇ\x99ϾʸĶĀԫϯ[ļȖÁȣцȯƞʟČǇ',
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
                                        False,
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ͿgԌţǛȚ',
                    'value': {
                            '^': 'string',
                            '$': 'ҿŀÕ\u038bҼǶѶӜӯĶΉƂŰșǗԞοНʩɣȄʌɜ%ǤͰϜ,\x83Ŵ',
                        },
                },
                {
                    'name': '\x8f҅ũͽ\u0381ʋΎĶʔɪƃӯʌ˨ƹӛӯҒȎӭȞͱ{¾ӃĿʒ',
                    'value': {
                            '^': 'float',
                            '$': 414210.45227635757,
                        },
                },
                {
                    'name': '\x92όѣÌˢĶʅԕ|ϕϷνТӒǅΨŁ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210203:210302.303817:+0000',
                                        '20210203:210302.303837:+0000',
                                        '20210203:210302.303843:+0000',
                                        '20210203:210302.303848:+0000',
                                        '20210203:210302.303853:+0000',
                                        '20210203:210302.303858:+0000',
                                        '20210203:210302.303862:+0000',
                                        '20210203:210302.303867:+0000',
                                        '20210203:210302.303871:+0000',
                                        '20210203:210302.303876:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '{ԥ',

            'message': 'Ǎ',

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
            'identifier': 'đ¨сөҢφʟϰƯμ҉ͽзӥóƞę"ӨBƏѝϚӎƝĚʍΙӓð',
            'categories': [
                'invalid-user-action',
                'invalid-user-action',
                'configuration',
                'invalid-user-action',
                'network',
                'invalid-user-action',
                'os',
                'internal',
                'file',
                'access-restriction',
            ],
            'source': '͵§ӡκ˝ÆƦʂфƑҨǜʓʻьɫȚÕ@ԀŻԃnμćѭѥϟęǝ',
            'corrective_action': {
                'catalog': 'ŝċїÒĎŮƲʕӳеŰΗМӏђɝɬ1˥\x80ʐҸȁȞɶд\x9dԫ\x7fȪ',
                'message': 'ǌɾЏΨʼTņŅăҔΝÚǗ˪ÇřVʐˎΜЁǴǵƀŽȇɊ7сı',
                'arguments': [
                    {
                            'name': 'ȿҾϼЧƉӤɰкǺˉǶ^\x8bǴȮȬ\\ŝåɔҘΜӄU\x96´¶ɡѣ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        470568.5418948828,
                                                        703313.7496783247,
                                                        189087.9162581361,
                                                        -77834.3527990694,
                                                        920522.3686845376,
                                                        354812.12639216013,
                                                        93693.96318485116,
                                                        719753.9026724088,
                                                        33323.512336395244,
                                                        733066.7472129185,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ЦҨ\u0379϶ҙƷЊԫȞɑ7KǼԔКИʮψˢƠʦчc´ɻȉĸԬԨӉ',
                            'value': {
                                        '^': 'float',
                                        '$': 409391.0169064195,
                                    },
                        },
                    {
                            'name': 'ĤҘӼυ:Ѿ?τϏT\xad\x98ɓ\x97pҠ˙˻ʡњĊЅľCʸRͿϪЋ)',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        5439119128372023598,
                                                        6275225416486689743,
                                                        -7042869773206044069,
                                                        2781144662367380802,
                                                        -539074048985922224,
                                                        2198089883894237669,
                                                        -8523346751971493384,
                                                        -1020552940037172900,
                                                        8159070332562219988,
                                                        5026035931987514285,
                                                    ],
                                    },
                        },
                    {
                            'name': '¥°ȥӺЃΙɝʏԮƝę˚ȁҔР!ΗξΘлʸе¢',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ȚЕYU1ҼƦáЖҽӍ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĕҺƍǌς\x9e£ɢ\x7fɰɒÄӸҺæɬҔҞ\x98Ôњǫӊǒϲ϶ƋѰϔȑ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ɯѿԛМ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:210302.299840:+0000',
                                                        '20210203:210302.299858:+0000',
                                                        '20210203:210302.299865:+0000',
                                                        '20210203:210302.299871:+0000',
                                                        '20210203:210302.299876:+0000',
                                                        '20210203:210302.299881:+0000',
                                                        '20210203:210302.299885:+0000',
                                                        '20210203:210302.299890:+0000',
                                                        '20210203:210302.299895:+0000',
                                                        '20210203:210302.299900:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'YĘπʿʝΤ˵ƽðηŃƌЬǰǡțǟˑѱ˅ћʝ˺ͱΦȩϣǿɒŏ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        418345.5024750732,
                                                        380257.3781071483,
                                                        -20482.070869885516,
                                                        -70565.2105251296,
                                                        291369.54575342813,
                                                        203200.94957401993,
                                                        977058.8907940928,
                                                        840960.2608422451,
                                                        16663.93369686998,
                                                        318490.0821135984,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƄΙǀȜϪċʂДǕʱȥ\x8cƊ\x8dқһЙӎЋʆûӹ\x8bԌɥκӟɿ¿ě',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        349097.6802987864,
                                                        475469.71668360604,
                                                        324256.1995649872,
                                                        554743.3928011692,
                                                        375897.9893732763,
                                                        527900.6551582142,
                                                        85943.11801803211,
                                                        -83906.04281547182,
                                                        96376.35599544554,
                                                        438349.65622492915,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΖĳɛʎȫɃ¡ǚǓӫɏĳ×¦ƅß/ўĥœЀíӵƵɿ\x8bˆҗЬŪ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ͽϬҢʜ¶ϓțїiH',
                'message': '/ǡťŞΓK\x93\u0379ҪyˋȖʨǀƃҗϲӄѹҔϫȤӮĘũiʶΧSӽ',
                'arguments': [
                    {
                            'name': 'Ɯə˺Σ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        5564051331042676529,
                                                        -4303983770295906012,
                                                        2465029100947578914,
                                                        -6368977701431092847,
                                                        612527305823871663,
                                                        4600670120750135004,
                                                        -5232371385465312308,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӑνͼ\x94ϩȩϜM˜Ԗҁȭ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:210302.305926:+0000',
                                                        '20210203:210302.305939:+0000',
                                                        '20210203:210302.305945:+0000',
                                                        '20210203:210302.305950:+0000',
                                                        '20210203:210302.305955:+0000',
                                                        '20210203:210302.305960:+0000',
                                                        '20210203:210302.305965:+0000',
                                                        '20210203:210302.305969:+0000',
                                                        '20210203:210302.305974:+0000',
                                                        '20210203:210302.305978:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '\u0380\x9dͲȲɞωɬȽʕˀǵϙҼУºԄ0ȣ\u038dӊҀɪ\x84ėļҔȣBƭD',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:210302.306200:+0000',
                                    },
                        },
                    {
                            'name': 'ξŎ%ӓьǙҝRϙȢˇˁӪ˽č¯ЈǰȞѠϸςnWǕȢφϒԈҙ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        612581.3871551633,
                                                        620041.760060766,
                                                        465103.696945557,
                                                        693765.5121625864,
                                                        873643.7639065727,
                                                        178490.28313625132,
                                                        976364.0218456455,
                                                        936512.1382724193,
                                                        551972.1087169796,
                                                        866667.9300700952,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ãpʡӻμЇÁȼĉǜȎЀҡ͵TǣƾɋӜΈˣмƘɤ˔:Ɠ\x90',
                            'value': {
                                        '^': 'int',
                                        '$': -8270180224573428998,
                                    },
                        },
                    {
                            'name': '&lÄɍǲӞř6ȶb\x82DмɦПȾɷ\x9aǌĔ¢˖ǡƽɏО_ǜǍ\x81',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        861162.815086356,
                                                        -4829.675137895145,
                                                        428649.7904583976,
                                                        608050.9055942844,
                                                        629832.0575924444,
                                                        615808.4732313791,
                                                        388674.84040696436,
                                                        -67305.52632723385,
                                                        -61346.13424554236,
                                                        968626.9614168159,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ůά;ϔɗОƃǁρjpʜƽԗɋϰϥԅЁΓȅ\x96Ϊ˷UîN×òŪ',
                            'value': {
                                        '^': 'float',
                                        '$': 221551.65555013012,
                                    },
                        },
                    {
                            'name': 'ƈȭɱɉϫ\u038dùdʕǟ\x9aDΎɴӉJȍȄƌҸʀЖ\x84ơΌϤӡ\x8dǥ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': '҆VĐӑǫϴ\x8cɗӃЍʪ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ӣѼa"ɕԢпЇэϠº˟ƜӻǝͽȠȿÆʅώфщ\x8dΛ˝Ɉΰìǭ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ʘǺɂѼʵ',

            'categories': [
                'configuration',
            ],

            'error_message': {
                'catalog': 'ӝÏ',
                'message': 'Ό',
            },

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
            'name': 'êDӂłϟѷñ5ʶνӟ˲ԪΐηӴРϬӣ˵ӳƅĕι˕ǿù\u0378ΏƔ',
            'error': {
                'identifier': 'χʅ\xa0\x87ӼǭƣɬʿȦϗԋʺÁŪAˌɍČѲɭȃЁүPȻĈͺ\x93\u0378',
                'categories': [
                    'os',
                    'internal',
                    'access-restriction',
                    'access-restriction',
                    'invalid-user-action',
                    'invalid-user-action',
                    'network',
                    'os',
                    'configuration',
                    'network',
                ],
                'source': 'ƲʵˑȘȾþҜϡҠӭǜɁģͰĤѕȔ',
                'corrective_action': {
                    'catalog': 'Ǣˀ3ɛГèϠĢ˒ùͲȜŔνi]oɂÅʢȔͻĢԖқ·˙FˣT',
                    'message': 'ȼƗģɿԗχĴόɢ4öƑμж¥ӪƟӺƦХ\x90ưюԓǞԅʩлΙѢ',
                    'arguments': [
                            {
                                        'name': 'ȶȝĞŢņʒГчʴîʢǽˣЩӠÝϣɛƆҸǩīţɖѷήԐ%wӷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҦƼĜÁ˺g˻ǊҔȶ\u0381˗ªʑ\u0383ɻΛ˃ӁґϧþӖԕƺҢδʓʊӎ',
                                                    },
                                    },
                            {
                                        'name': 'Гȓα®ԊҺЩӷͻ¸ʺťβ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԉƺМ»ҞNɖтЌšǙ\u038bʐǌԍʌɼӎȁ¹H2ʹÄƀύ_Ȕ˻ɒ',
                                                                            'ˌƗιɽřťΆ\x86Ђ˘ŀÔҊοы?Ӳ˃ȳ˥ɣȃȸβϡԇʭĤʢЊ',
                                                                            'ʥ˰ũΆȗԅ\x83Ǉ:ΏʔǢȫƉLŉɣπ\u03a2ΩҸәδӚԐʴ\u038dŁϢ˶',
                                                                            'Ӄƾҋ\\΄ʿ˝ȝӉͽҊϙԫƟ7òCԆÁˬˤÕĝ\x93í\x89ʺ˫\x9bʜ',
                                                                            '}ѢŏǐǐwHĖáљƍԡȭΜǹбиφ љ»ŞǒVǱϘӼ϶ζB',
                                                                            'ԮŕŎŬ!ȋСǰѬĎţ`ϒʞͽƚȑŢϱо{˄ʃɋӗԌƕ\x87˃ҁ',
                                                                            'ѠÆĤэļΔМqĦщɹ\x81ʜ\u0379ϐώă˭ӆɸòʊǍӳԩμ\u0378ξƾ\x92',
                                                                            'ҤИŋӢϮƣȵŠђƭѝӍȊιB(Ȧ˟ĊϻϝТԟʪÃɝɉқԚº',
                                                                            'СнԄȣϯ϶ӕ%ѸІʝęӦċ£ƨGʸǲԧеƤŜλUӼ˷ΪǿӬ',
                                                                            'ǑЇƖȅXԎƏЛʒǶ~ȋȼǿԝҎȁ«ɓΚс3ΰ\x97ZɆĹîτ˖',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѣǘʗβȲĵǰƒѻӄÿư\xadѣԙźʁΒȲηԧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1519211329132694190,
                                                                            -4514758762273609824,
                                                                            -3066414700117706787,
                                                                            5315316917817825320,
                                                                            -5301090782236349744,
                                                                            5261581274061563936,
                                                                            5055360871969357892,
                                                                            -6189916490157968097,
                                                                            4219920352315906357,
                                                                            -6706431338982943168,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѭg˙ɕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 929597.580088915,
                                                    },
                                    },
                            {
                                        'name': 'ˁтLӏȯǗɡÉɟҸϺʝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210302.293488:+0000',
                                                    },
                                    },
                            {
                                        'name': 'һƦŵɎв`űķЯhȋүӶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 297444.92957029404,
                                                    },
                                    },
                            {
                                        'name': 'ЬԈơăƾǤɀƾ˼ѹЁξΊρԙҝƾ×ƃӦ˘ȽνҲ\x9eȒ<Ȅ˫Ҋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210302.293784:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ċ˜о',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'ϵÍβλjȣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ė˧δҹɁк8œƣͿ|ǱƠϪϝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6290592983710033911,
                                                                            -515641700608541076,
                                                                            4146066571532913189,
                                                                            1824079018270101674,
                                                                            1190705531877631461,
                                                                            -7303310121841608231,
                                                                            -664168851204972675,
                                                                            6431080026905017355,
                                                                            3782337787954191778,
                                                                            -5775166330361476993,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ȃZȳD˅ѺҤ\x94Ų΅ŌЦ°łǑȟΐ϶5hΣҜÜ"ƶҹ˶ǔĢǷ',
                    'message': 'ɆYԆȃ\u038bǅͻðɜĻɣцƳ:ßƓʼʹΡŌӣҟǂщ\x98ѹȓϘ\u0380˒',
                    'arguments': [
                            {
                                        'name': 'ňОÏФϊʢЇȰǝџȬɡИ¿ΞНÁđʹӆÆsǮӰĄ,Þ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ИȨҁÀшϸ®ӨĎѧżѣӐкϴâΣӤɌǯ}\x83йЛƘɃŇԮŧʼ',
                                                    },
                                    },
                            {
                                        'name': 'ŢȊŃ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210302.295154:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԎʶͼȆʜɹϐңέ\x8fėĕӐʙqÓOȪŞƱĚðЇȐ˰ԧΫȼ\x97Ή',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ļqϚǼğ˻ơʽѽºѷ%ÑǤgϒTȢΨɓ˛ˀȳʆɖʝ\x96Ŧ@І',
                                                                            'áћȪлÜ\x91Ͱу˚ӕҖѓӔɷϗΔÁʥƯԮGŢҕȲþȵ\x8fMʷI',
                                                                            'ѹӬȅ˲ɐɮŠ°èͱƖ¥ɑΟºǕĬƥƶƑøҸɑӚw1˕ɠȎĭ',
                                                                            'ǲsӸȨǠ»Gѓʹҽ\x86ǝА˜ю¬ȕӠʟѽǋɯԕˎǜ\u0382\x9aҞőƿ',
                                                                            'ԥǗϗĀóў\x8cǾȝź±ӌϑΧʻκǌɰѨҥŶΗÓ³ԧgϳчμɣ',
                                                                            'іʢˬѷcǨŸѶƍыĪʭίДӨнԁǐӧŒӹ±ԇϟǕБԧȽҏϲ',
                                                                            '˹ǚĴͳuвǍ·ĉɟā::ʖΜȝ˦§Ԁʕ҃ɢɛεÊÅ\x9fЄˊ^',
                                                                            'ԑґĽηԄЂɃӺϻǤö\x92ˏʠÎξȤǚ\u0380Ƣ9ϘԀʴFєşĿʮD',
                                                                            'ůǟ˒İ`аFƊƦϋƾƮÛµîÑфu¶ɱʮPäҋЋbñ\x84Ģǟ',
                                                                            'M£ɇ\x95TĴԨˡϹ˷ʾôǒ¿ǕҿоŹԪωмɎƴǎÌΨɰТɦǨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȭӆʈƻ¹ѱʦĹѰ®KΑƊş',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2633198053340475122,
                                                    },
                                    },
                            {
                                        'name': '¯ҠʍɄȺ1үфpí˲өʕΜ|ŞƘЇԧ9Ҫʩ\x9aÍԈЭʂƑ\x83Ӽ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210302.295878:+0000',
                                                    },
                                    },
                            {
                                        'name': 'АӥȻдВȓŤȋɂ{ӏϪƕѿԫ\x84ӭԗΦȣШҰί',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8465243167389494481,
                                                    },
                                    },
                            {
                                        'name': 'Ѹϛ\x99ʊӖӋ\x8aoѕ\x87ĘɨȐЪϛӿӻNǙұlЦϔč²бАƶϊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210302.296296:+0000',
                                                                            '20210203:210302.296310:+0000',
                                                                            '20210203:210302.296317:+0000',
                                                                            '20210203:210302.296323:+0000',
                                                                            '20210203:210302.296328:+0000',
                                                                            '20210203:210302.296333:+0000',
                                                                            '20210203:210302.296338:+0000',
                                                                            '20210203:210302.296343:+0000',
                                                                            '20210203:210302.296348:+0000',
                                                                            '20210203:210302.296353:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɪΔкҀ·Ϲ҇эZʜǞɄáĒӤƥʖӧуɷԙĮТ¿лðϝ\u0380ʳӘ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ːɷхҚ˥ɿ0βʀe.rԬǤ¥Ԗ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3950777648972380047,
                                                    },
                                    },
                            {
                                        'name': 'Ƚ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
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

            'name': 'ϋԁй',

            'error': {
                'identifier': 'ӭí˥ŵ҈',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': 'Ǜȑ',
                    'message': 'Ά',
                },
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
            'event_id': 'Ӊήˊʸǩ¤\x88gϒŚ˒ĹϽҷŚɈɳҗҶԡϜïɜ\x89ŧҠȻĦǡĥ',
            'target_id': 'εÐɬʳYϳŀӨǴ˶ЎÃ\u0382ʼʂČή¯іŃÙv\x9fΡʃûʭĞÝȃ',
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
                    'event_id': 'ɡÏԊǌɷұϊćȄÔz˒ΙčÅĵ˜\x98ϹѸӓƌđſӾ˛&ʴ{ԛ',
                    'target_id': 'ӿÓĐİɆȱӿÎҾĮîρŚŐƄçĐÖAřƱĀɓŉʀʏѣѻʸo',
                },
                {
                    'event_id': 'Ř҆ŦßtЛѐǇʘ0гŤɒȒñaČтҩǉнӅωȿПўӒԛʓ¥',
                    'target_id': 'ӯȾҌô҉ϫΒȩòǬϪǿӲøџɧǢҍɴTιоçFǹƻ˃ԗɋΤ',
                },
                {
                    'event_id': 'ŠƈƥҲӬҜ²ЖʥҘLķҘǝȤҲЂʫŀɷäϵǄŇ˃ҺȟÙŗӋ',
                    'target_id': 'ѸϹȀψĨȐɃTĕˁҭϻ#ϞϤϤεљĳëԥ˫ŃӺЪƀώǬŬȕ',
                },
                {
                    'event_id': 'Ŧh?ʹɝªŶΒİǆѷ\x9f\x87ʸLɲĘǑ)ďüʭˇãVĖˍ«ͷФ',
                    'target_id': '˽ɵ˅ѥʕʯφώFzѝɐŖѝǍχ!ԜӫŋӍʷхȎ҇ϯʎόΉd',
                },
                {
                    'event_id': 'АǸʝѝĩʬ1ʒĹӤňêҼ',
                    'target_id': 'ƏҽɝÄЩØʨʴјʌΤǎϤɾԛΜīþ\x95ƢqŅӝo0ɉȔ\xa0ҖŻ',
                },
                {
                    'event_id': 'ЌӌѷҾͱǘàÀюʂѥHѪӺʍΦʟƷϪȁ¨ӴЗBûǵҫΈƺO',
                    'target_id': 'йҋ\x9b\u0381¯ϜǌͻxѼ˸LӂȞʯƑжȅшlʷʽԞʂlȹƼсĭˆ',
                },
                {
                    'event_id': 'RӘǙǰşˢ]ϵԭ,əʆиʍǧԬϨԕϐΰˎȼƣɬƯƺ˖ϥƻϘ',
                    'target_id': 'ú÷гʺЩW²=ʭϿɓϕйӌҮċǷu\x9c\x9eȺůӻȆԪӋƗΎʵӐ',
                },
                {
                    'event_id': '»пʽȯƛƯʈқҸ$ɱКr¦ӸԎӭϓӹȭһƕǏӯДȑēӶҵΘ',
                    'target_id': 'ΧӌȈʑHĳȔèчЩˁԚƣUМώʭ˭ӀţȧľɶȱѶɀŉШОƸ',
                },
                {
                    'event_id': 'ФOȮоƶ͵ԀѴŹǠʉѧµʝǼϣѹǑ\xadčIBƚΘЬПʹΖɐɍ',
                    'target_id': 'р҃\x9bˑǻӵГӄάϻƉѧǅʄ-ѯƫΐӦĭġ\x8c¼ľȎʣ҇j¹Ȕ',
                },
                {
                    'event_id': 'ѵüӪŧҡȧzԥӅ΄ʷȤåΏMI˶ΓGНƹμҡξʡ«Γȁ×\x83',
                    'target_id': '\x91ϯ˹\x94Ĺΰ˼˒ҐƺâԚʾ\x95ԪKȴјԝǑǇСΝϕǤľVϓҠƢ',
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
                    'event_id': 'ĢƢǲ˞˱ˈ?ľɶ\x7fƝΊʖқЈРԥmϊʍ)ëЙʲCŎǖΌҙҗ',
                    'target_id': '±ɡ/Ԯ^F˒ϚʘÌӲЖɮͼΞǴłHϯʨŶŹӊ\x96ЭКӧ,ҠR',
                },
                {
                    'event_id': '˨ʺΡ˒¥\x87ЮĭͿњųϹѐҩ\u0379їȇ\x90}łɐ@ΧѭǏ\x9dƬқʠτ',
                    'target_id': 'ɯҗʃѻ˸Ͳ˭ѶʒƗʟӤθӿ-ÿ¨ªϼšƩҍҳӵφ˃˖ͺӪӬ',
                },
                {
                    'event_id': 'úБșN҂ŀѓΜӐʺɽɾʁʉԥϻ˅ҽѓ8˲ɳDÓз҈WƝφʋ',
                    'target_id': 'Ͼʾǆ\x9fкɆГϕѮ\xa0\x82Ǌì\x88ƤԤɔǉϲϝδżæЈ§˾Ȋŭ҃/',
                },
                {
                    'event_id': 'ŌȜĔƛ҂ЋκśáѠӨЗӕҬЏЉԊƵªфӭ|ˣЪˠӸĦĭҥȐ',
                    'target_id': 'ĠɶӜЭȳɠŠϢѹҧƯǺғʚÃ\x92ѯõȝӥȐVʡãɏƚŬƘԃӮ',
                },
                {
                    'event_id': 'ͼҧ\x80ћыѧзƓӀіƙʗŧʛĝĄǒҁϷȺãԡʛ°Øϛ«Њǚя',
                    'target_id': 'ˁɣЭ\x96ӿǫБmƃɰҀɥτЌƌҹ*ѴßŠǷǟÝњĲђȤȄϒʟ',
                },
                {
                    'event_id': '"ΐƭ˖ϏѷɂŌӼɯƇłӯśŌԥǹĝΎŃBҧϫΗÊǥвԓ°ǡ',
                    'target_id': 'қF˛\x87ZӚʴӂĴȶƟȈФΠˏɺʈƢȚюțђhϝΨͻйƗƍԒ',
                },
                {
                    'event_id': '\xadʅÃΏəˬ҆ƎԊŃăҰõ\x9aѢƲņǛȖʻȳѡʒƄӅϽφ˅ȴ˛',
                    'target_id': 'ң҈ϿʚϠúǤǯϦȻ˓эį(¯ѶÂԍưŗƊ˘χϪɮäҪ˝Sč',
                },
                {
                    'event_id': 'ҝΘҳȒǎѸʗȹːß˅υW.ѾӶ´МGũŨǟ\x97Ŷ˄ΧSҞ&G',
                    'target_id': '\x98ȲΟϋʶĹɂĀĖðЅȎ˴ƄƔκaaÙŅɹԧħfΦҭɄҢљҼ',
                },
                {
                    'event_id': '1ӶǩħŔλҘɦŨƫњ˰ӚԋҎĀʨƔԥǉӆů\x92VʿǹίӡάЫ',
                    'target_id': 'ХŹҔΔĝŴ˭\xadɏјԒʙõw\x8eӨrѿԜɔѽɯ7ĦԩԚҌÚçҤ',
                },
                {
                    'event_id': '\x94ԩŸΏдҵѿˠPΓƦȻʍƔʹýħĢǕʆˎņ\x9fȫȵϻĞѫ\x7f˭',
                    'target_id': 'ˇ\\ϰъǥΚǊƽИʱВԊӻ\x88ɔѢΑþǮˏõȉōɍѱˊфʒʝ˯',
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
