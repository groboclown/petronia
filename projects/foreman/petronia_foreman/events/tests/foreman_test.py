# GENERATED CODE - DO NOT MODIFY
# Created on 2020-11-30T18:10:35.478274

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import foreman


class PermissionsTest(unittest.TestCase):
    """
    Tests for Permissions
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in PERMISSIONS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Permissions.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in PERMISSIONS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Permissions.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


PERMISSIONS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='action', name='Permissions'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='resources', name='Permissions'),
            ),

        ),
    ),
]


PERMISSIONS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'action': '·\u0383;ȪȗŮ\xadŌȞѸƸбʗʷɦì<ԊʥÓҺҔ×ŹÁҸ\x9eƀȁ{',
            'resources': [
                'ΏӿdȠĢӍ\x98ə\xadǽ=ΒͳļĢ7ȶ³ÃÜÀĿSҹҎȺ\x8aŀĊȭ',
                'Ɯ#˼ś҃ЩĲǵFQÛÑɯŭιʶҲѭԛϝԠǓħɈΡΟΊҋәº',
                'bӇΚĬĕ\x92ϠɍʠʵͱÒʟҏƨӖņ˜;ӂʸ\u0380ҜǾÀȹþҷńɄ',
                'ѰʵґӮђбțǣÛɢǋӵΗˉĈʀςӍҫńƷƱ\x83ȗѰ+µţЏJ',
                'ǬÉĚʏŠʶӽ)\x8a\x8eʽŋȚ¸Ю\x8eɥĀǇϞüĔġͱƀԬàŅEϪ',
                'жͷԎϏʋÙǵɤҜÎ ЋʣτǁӱЛҖϠӣˏȵԛЯ\x92ӋԍӯʓĪ',
                'ϤΰҾҟӇýғ¾J©ЫċԢ}δзăφƃӚ¼ÎˬӱҤȩϹϽƆҊ',
                'ʉδÓӇΤɹşŠЇϚЋ\x95\x97ĽǦӦЍВԐĔϔ˦4H˝ĘɟƳӉҒ',
                '³Ĩ\x8cԩøǦ;ėǠҚɺˊԀϗ΅ӉϕˣȲʶΞӯōZ_Ѧŋwʞz',
                'һͺƃŉõƕϩҀǻƮñсiɸҠπϗԒ>ǰԋм˄ʦˠĦȲLŗǖ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'в',

            'resources': [
            ],

        },
    ),
]


class StartLauncherRequestEventTest(unittest.TestCase):
    """
    Tests for StartLauncherRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherRequestEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in START_LAUNCHER_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncherRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='launcher', name='StartLauncherRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='permissions', name='StartLauncherRequestEvent'),
            ),

        ),
    ),
]


START_LAUNCHER_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 'ʝ\u038bҷcŦ˨ΈɁʡȘɼ{ћmЈΰϻԪ5åƮԪԪƲǻ',
            'launcher': 'ҷӸɆ҉\u038bsȷԣԋɡɖÁԌ˔ϊМ\x80Ӗύ·ʝzĥǯЁ4ɺŔˁґ',
            'permissions': [
                {
                    'action': 'ΟƾǜáĵġԦΉƫŻà½\x86ɜʋ',
                    'resources': [
                            'γçɛĚ_ɥƈѰѴѣßԜԛɥƮɂǊˇϟǆҮŴԪǞƍǺԧζğҝ',
                            'Y\x98ʾаӁÌǍļ҅ǩ˩2+ѳţΛoԘԮȞŢÞϺÓ \x8bӮħîǱ',
                            'ƻԛʢБŐƗԙʍňī˷ʠϠŬ2юӥĝ\x93њǃŉƁ´˅ʵuȰӄԔ',
                            'ҟŬ¶\x96ӫů˺ǒγ½ΝƿʱǸԃ*ϋɨğҟάʃЕͶԦӫʀИXù',
                            'ƠʇÈΣʆį\x95ƟӕȳʙЕ˛ӵP¿ˑц\x7fӃȩtηŦÝԔUĈēĄ',
                            'ζҽƑʡ(ЏαëCŌ®Ľ"ƍѰӉVɋĵʌʞҡO˖ЏʧǧҊƧΎ',
                            'ζҮɥƅ͵ďøǏłțϳβˇ˺Ԫйµ˾ʽįĥĺɵNΌÉZ9Тԗ',
                            'ҾųΑ}Ǆ¹ȊρȽұҕƩȖΫҠƅӬѲӖǥơɹˊѮǻʾǁљҔѤ',
                            'ĨΏ˶JɊôʺʕѿΐƓˮоЏƾТʢԎӇØź]і¹ñϭȤ3шД',
                            'ȞԒҖʀǅ:ɻǫ¨tŅʂ¨ӦΏЛƷȲ@ƬѾå˶ӸԘӉ\xadªŊʤ',
                        ],
                },
                {
                    'action': '\u038dŝЀpIϜȭĲԠϐ:ͰǤϬүӯ˸ǤНӮŒɜ×ҾƔҤҜ"ϓĳ',
                    'resources': [
                            'єǎӑHӈѧǓċȁҍ+ĀϤʝ҈фѩѧг\x9fҷӥΤώ΅ԗÚÌр¹',
                            'ˬ҃ӋӒΦҙXѵ\x8fÆHˆËц˝üƐdҠяΖ6ҸƌҳĽɽʐ˓ъ',
                            'Ą˞ȁBħʂƏ˻˼ʏԆϒǹȹˡŗǻˁȶʘĔӡΣˈĳҟќɜͽȡ',
                            'iʬҒZ\u0380ͰӚǻǓѕФɛ˄˷ʢɭӄǘ¢³ίӘƇԤP;˸ЬɸҔ',
                            "лԙƒԎê·ӳфυȵԔ¬Ô'đΪĪ˦юϢʬζýԁí\x96ЫʣаE",
                            'Ԡ¿°\x81ȦĜϻǢȇÁŖҔΥƔH5ҀǔǥŎ\x91ӪŒƉï҆ч\x9bυʙ',
                            'ĉѰЬ0ДϹ^>ˀӪ¸·ëð\x96Ʃϸ\x8aɿʲɵϴǴIˍѫĵΕʟɀ',
                            'ĭϋƷ\x8c˞ǷѵǜѼѤ±ΌºĖɀƻЋăȞϴ%¶\x9aԆ҉ЏɷӀϊQ',
                            'ȡҊҭϔҥ©н˕ÓŃFƭ;șățɬ˭yǯœЏƈpΑŋѐͽçɯ',
                            'аʰB/ͱ\x7fѝóЁȋźɊßƁʶҐѱƎүʝϤȺŨ˚ϰщ»\u0379˗Ȼ',
                        ],
                },
                {
                    'action': 'oӍ˯£ǹԌþϣǘőƬĐΛΥӿΩИȖǥҎňȮōGçϖͻʶщΛ',
                    'resources': [
                            'ҕɭʶi\x91нέѾԔЭӈʩ\x9dѹ±ȜǯŁəԇљΖʖƠτĆɧѹ¥ď',
                            'ɧѹāºΚɰ˺ĈϏK¥ġԣǳǯHș˴Ԇœ˦ȨӅԎ˗Όêԏɍʕ',
                            'е\x88gϙˣӂӲіҙsѺɊˡԉυ˨ЫmRӞʕĢgÂмƾϏÝǮԘ',
                            'ǡź˗˜ɷʹԒɖҝ_˧ÏĥĄӣP˄āſ\x8d\x96ɹƸˢŴЫѧGԟ҇',
                            'ʭΗ˵ɎѵНЫϨΝĢǐΝƉЅȎϬЙĖѶʪҭ˙ȁԄDҡ҄·ɂλ',
                            'Ǝǧʍʚ˭+Ϩe\x91Аӏ˻ң£ΨѲѴ2ĵʽrΞщҋԂǬβͲѷƬ',
                            'ԑfʬȳǝ\xa0ү¤ȎԝьCоАҔΗϞЖЕҹpǹ˵-AϞɺßȷˡ',
                            'ęП¬ӸͲǟǓƔhɊʋΒѓŕϜ΄ĝӲ8fȯҰ¸Ɓǀǃћώǃ҄',
                            'ІɍѪѦԚϸȜϢԀРϹĮƈĮΡЊЮHŘdƱŨВĜ˥ǵѢØс˘',
                            '˄œОńȅċǡȑĎЦϸѤȦԡ[ɤȼóѽǀǁǓƾȰѹϯԞБɤʚ',
                        ],
                },
                {
                    'action': 'ИЧ\x83ĢϭΫҥҧǀſʫŲѦůЌԕʌƹӁЕʒѵӤÒчƥŝ¾ӡΊ',
                    'resources': [
                            'ЉϡȺƖϠǙ҉\x9c˹Ѧșӯʞ[ùcͺ*Ѫʛ\u038dЇѬѮǏƕǓɴëN',
                            'ǭҰ¼ǕʾƥӗʫŞʘĵћˎɐþѭāԑǅJƱ҈BȌΖʓYǒʸˠ',
                            'Ú¦ǔБИϻ.ǻҏқŸЀƜĖʙ\x9aĜŧɨфҶŅɅ¼ҝɀ;θԏԝ',
                            'ÐЗɈˎ&ţѩҿҸġώѪΑǕАʗƋӶ\x85dǴǔŏńÁ˦ѾƘŵő',
                            'ɬƶģЫѩ˦ӱ˨N˛ӧʩ\x8fԔӼǨȩʵŃʉжΪƽ҇ҙ҅ÝĻѯЋ',
                            'Я@ԓӺν{ÜɉĮԩȴŎóѬǵʴpҷʺVĝĉçɉǑÂƟÿɎ·',
                            'BĤѯӍȄʫӒɼΦѦІĶ˰ʉįċėjЦ{yƤ1СζϨȐεǷɎ',
                            'ɣўԗʿƗ҂ѱÚҵɦǙӥ¶î¤ȍʿŵ²\x9aԒŷѿ҈ΏнŦӜǘ΄',
                            'ǁĢϘĆӪÁȴǤΩIЕŁАuϩǸǪ¦҃Н}ūӷħʅԏͱѷфä',
                            'ɹ°ĝӍ^ͶӃȇϒсŃӚӕēɚȂ\x7fΎͼ˳ԞǑ´Ŷ\x93ўǣ\x97nǌ',
                        ],
                },
                {
                    'action': '\u0378ǭϗʯȇʽŽ˸ԆƬĎτơϸЋҜȐǁƝĢƐӆ/Ԋ²Ūμƕ¤ʨ',
                    'resources': [
                            '\x8cϕˑӀɓŚĎǃВ϶ΕǒəʓêԄ\x99ǼӹɕΛнˇЪĜɄˑǛƄш',
                            'ґ˥ǪӬǢ˞æƄͰƄáм\x81ªĊ"˳Е\x7fäʾҤУǿȲѴΐ҈ѴƯ',
                            'ЕǍʯžªƗӶ$ԏęó·oǋʪȬŁɆȂϺӣĳεЄρ$ɫʺΏ?',
                            'ΟѫŃӼƞѷԨʿċËÅқ\x99ҿÛҿȞŻǃĚ˦Ȟïμ˭ˤӐƉŁӗ',
                            'μʳφɥŤ\x87ԍуΞάΛГSȂ\x9bѺĒŠ\x89ӹˤԧѢѢϖªѿϳˎɿ',
                            'ӵ˸Ů˪ˈПʖFԝɻ˱ԈͰЇѼΘήχϊÕԣӺņ,\x95˟ВҷɯɆ',
                            'ʩӌəĺÂgƨҿҭľΏ[ӧ˙¥\xadǃȑŴϸЏ\x9e˻Ę˗ү˝ǚϏǦ',
                            'ȀǻӶʆǳ[¤ԭΫļyǁқˊ˄ϼҰљӊǙϮу´ҧĲ΄Ȍîƨӈ',
                            'Ϫј\x94\x8eвǚƄͷŭϿźŻӪʗʰ\x83ϟɮĚ<ŲυӥӺůǒƞџ\x90҃',
                            'бôʄǾ\x84ƥŀÁӮϠΫбϖψҼОȱ\x9c\u0379ģəMƙůşëΪ˄ƆӠ',
                        ],
                },
                {
                    'action': 'ȯĿйőҁÃӪ¡ʬԈź·ҲҠуО`ӀьФɝjpŋʒЃĿԑζǤ',
                    'resources': [
                            'N#\x85ΤɾσΓӵд{ɆĴ ȵzŲŚȫήҶˬˏѕȅƛƊɤЫǞŨ',
                            'ɰ\xa0ˊƽԨ¶ӯԈėǏɱМŏɕϛќŌя8ϓɏȑ҅Ќ¤˯ʧƍ´)',
                            '\x92ӝťǼǽӺξѺƑϻЈʑεɰqӔΣL<ЪˊҒԀŕηʕčǁϙz',
                            'ƜχŚӼӇԞƁӜӫŘҀˆ_ҊƤĔȒɟӕЁŌНѯŔąɨώӧѬƟ',
                            'Ɠǅɇ(ѣŮ)ððĶǇјϬİѢƘǏ҇ɽúŏίʞUɕҒȶѭёő',
                            'ŊРƈÉǭт\x9bдӠѼΪԍɭǑСʮϔÀͳʼǷƚeàҖьпħȦɃ',
                            "ӏɄ3ŬѐԪȏʯ\x8eʏĈЦÚҡԛĥɨԇǈʬƿӈʣњˤѧțĽӬ'",
                            'ƐЯ«ƒ\xadHӞ˦ʩɂȤőфlǾÍʣȝǔĂУӪʔζiƿ\x85ƄӐɧ',
                            'đƫǠΤɛНѻ/ǉȬ\x88ƙʗ¯Ο\u03a2ÍҰҸɉӉ¼¾yˡԇӢŋόŢ',
                            'ũаã¼ˆξѺɂ˳ԠЈ˒ԟʁƂҲȎţЇƠΐFǜĮéșõĻůŵ',
                        ],
                },
                {
                    'action': '»șS˃ʹǶüqâƫѶԧ\x9dʍʔ˦фσʼ@ԧ\u0378Ȓȁ6įԄɱřɊ',
                    'resources': [
                            'ŔΜҌƄ³Ϸŭԧǂ\u03a2ĻðʨŸϽĜԡ˓˦ŕ~΄jǱƖ˂9җ\x82Ӹ',
                            'ЌӰɶϊʪʭ?ϦǐԪ\xad\u0380ͰŘάӳƬóƦћӯ&ЃϪϪΪ\\źқĚ',
                            'ΊʶϿ\x87ȑԓʘVȥϊ˵ɌҏɬʿĈќÍiȩĊ˥ɌȖʉyåˣԓϦ',
                            '˘ǭȭƙōҗ΅҅ƼϝŃʧȧƦĂҜţúθҹŨǬЌʺҼѸԮɜMМ',
                            'ʰϥȬȪýźŨϤÒŋŔΆϛŕƏӊћӭӗүêƃʪʾ\x8eĄԕɶҖԑ',
                            'ƲғӪǚԁɊʔЦ҉βɅÚƣϊýǧbьǟԊ\x95Ӂʥ¹ÛѩɮľƤ\x8c',
                            'ȜˇCҕÍИϟʭÃŻ˷ɷΒqĿџƠřɚðύÓ¥ҸǣˍӞśĮ˂',
                            'ϻШɕʗГɮѫȾӄΖƛ-ԒҐĹƁҵĐ§ȭɖҏÛ\u038bѻɱјŲŸЕ',
                            'ȰѱƀĮHԀȔǝϾȟŊҩ\x85ƘЀŰʬҴ8Ҥ±ӦԞƳΤԐџɼӁȗ',
                            'żàӷғğ¢ʖɸѰӊҢ˵ɵʋóĹӾƚИȟЗćȣԜСӴʫȜϔƯ',
                        ],
                },
                {
                    'action': 'ЬӯПʊʭ\x99˗ʺӣӜΨǞ¾jǩгǸfˮʣnʹǰKÙɗȖгqȤ',
                    'resources': [
                            'ȃҽШВϝ˪ŪÔ˖ӖɎѠbФưͽкxǎ}uаҸʘϽ_Ņӄɛæ',
                            'Ȍȼ\x9eĶ\x9fȴǡгŋӚŠʸΖӖӋģе^ɿʗż\x9báѓɜ¥üԛҒp',
                            'ȷξϲȕÖӠşºЪϷ$ΪЭΓǉ˲ĳȲĉbWџ4ӥŸgȴ2ȑе',
                            'ъԜȡɝϡԎʡɅӒԁǐ°\x90ƀӾӈé|ЖåńΉ\x90ΘѫͽŰÝ¼Ļ',
                            'Ñ:ȓӏƢ¡ӯȐЌɚX÷ZÏϋǅφĉВͿΈƥÎϜȤËлӵiȄ',
                            'ÅЙӇʂő#ĄƄȅҲĹ6ѐЛ˜ʲεҬƆѽż~ӫ·ӼЫѰʨːʆ',
                            "Ǔŏ'ɦϝþǅă϶φҚιБϡЬӗːƦʘˁѷѲďǨÎоЕЬƦ\x8e",
                            'ΘǩŎӶӦĸʅ/ЗͳЕ~ЀŖƭηȣ[ϒǆǁLǱĘɥʜӉȣrЗ',
                            'ΛŢʬ˩ʼҨƍàǧĺȅøҴΞƯ\u0378ŗȷǢçʀȱ˺þſӚæǱǞӑ',
                            'ϩԮʚ\x98Ŵpōå:Ӹʥ\x87ƹѓҮҵǄб)ʧӻɝŋϴлҿÀЉѶɫ',
                        ],
                },
                {
                    'action': '¶ȆźƂåҹƲεýǂоƥԏԮӲ\x99φ;ǯ',
                    'resources': [
                            'ɭˊҴ˳Эrѯʤ\x8cɓʿűϝͺӥȿϥһùϥέjҜΗɽԂͺΤӥż',
                            'ѵ©ӸсΩњň0oϼɑqŇԧ7ʴȧ·¯двԦњӏӌćɱŨŦǜ',
                            '˄ƈˏ˩ɗőʚˠǱѲyʨ£ҳӁϙũ\x9fӝ·ȸӨ\x8eԉјƓ÷fȧЎ',
                            'ΤȰƷɴηЯȋĕʙӉԃ˺Ǆǻ˞ΙүӫτȲӳzеȆǨƖ˽ɹǜҺ',
                            'ҐϤ¡ώȊӈϤӝìåϑĀȶӼ|үÄӵrҕѤˆ,Ϋ˷ѰϼȮ\x88ԣ',
                            'ҘĕƜҰϔĜѬѼҏӸÑȌgȒǾöѬâϕÚБΑˡϼ\u0380ҟӽƝϳÈ',
                            'ԒØрΛηҟĒϩ˪˄тΩųˈ҄ΐѽ¥ǭƺѤηʭ£ɧȬ˨ԁșŭ',
                            'Ɛʒļңх˰НϡӐȨáӵĸʼæƏѶθ\x80ТҼџӢ ԬQɞʜdǓ',
                            'ħҏüԓ|ҿ\x9eс\x99ȽԢȼ@˄Ҳ·Ԗ;ԈȠνǰʞϿʝԚήѼϛˤ',
                            'ˊŬ˶BшΙΦԍUĺѽfӄʹ\x8aκҎʒĜȾ¾×ƐƏUщǭԛŰɴ',
                        ],
                },
                {
                    'action': 'өĶГŸ\x93αԉҶĥǆɔɰԧӷѻҩĩӺΆ¥\x92Ã˥ǒÍ«ЉĂɓª',
                    'resources': [
                            '\x89iˉѹ\x87ŻȐԁ£ѮaɡƶϱFйϱŞ£Ԁʰ\u0379ҕʱVԇǗɿ£Ȓ',
                            '\x8fԏȐīиʗэЛѠĢŏҭbӶҚҷϿҬƁĀЅӼԪϕӯǨ\u0381ǚǌζ',
                            'ю˞ƮмăîєǓԈŔϧϬŦɑρЅϞǀĄЄϜ\x92',
                            'ôʩӶı˵KΈΊ\x8báIόÊƁϾɧĭјǂƉӼ°ϛƨҿҦ\x83Ľʉɿ',
                            'ʼņdԮÝҥ\x8eϒ¡ͳȩˡϨņǇǹ\x86ɖӫþ\x8fћʾΦ҅Ʊм\x86ñЈ',
                            '\x98ȟσȠʌ~ÑФ˟Əρ˨ΜҪŔʢǤʄǁϠĚƧōšÙȊEǠԐ$',
                            'ϫҊΆʤΠº˙ȕʘʮҩƟхΩ\x8eÙºϢǒӊʺŠNǗЧӇѿɕȖf',
                            '҂σƻȖĺƊʞ\x81ƝƏ:¢ǘЀӃCtʿԥķºаԁĸǷϪʆԊ3ӝ',
                            'ƁҵŃԗƵ\x7fŁˠĒ¢ʋВǇ\x97Ѽǟ¨νNäɓʽĘӍӓzǀҕЀʳ',
                            'ў\x8dʿ\x85Ф˺ΥИȫğҲӗҘřÝ9ʨнωӾłΎ\xadƎŃáүΊέц',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ΌҫÓ',

            'launcher': '\x9c',

            'permissions': [
            ],

        },
    ),
]


class StartLauncherSuccessEventTest(unittest.TestCase):
    """
    Tests for StartLauncherSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in START_LAUNCHER_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncherSuccessEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='StartLauncherSuccessEvent'),
            ),

        ),
    ),
]


START_LAUNCHER_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': '\x95ĸĖ˼Ńȼď<çÎː*҄ϿӺ¦ǫʭʵɩЗ\x87ŧӈʂöӧ»˚Ԗ',
            'target_id': 'ȯΒĎъʒѩʞҾЫҽҮłҰĜȗΚȹҝÑďƴƨҺЄΎÍƆ˫T\x87',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'нӭǞ',

            'target_id': '˾ƪǑƻί',

        },
    ),
]


class ArgumentsTest(unittest.TestCase):
    """
    Tests for Arguments
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ARGUMENTS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Arguments.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in ARGUMENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Arguments.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ARGUMENTS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


ARGUMENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    (
        'string',
        {
            '^': 'string',
            '$': 'ЬʶƽΪԑԚ·Ϸƻ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3135011216510316488,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 18327.86487913654,
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
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

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
                dict(field_name='message', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='arguments', name='Error'),
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
            'identifier': 'ǤЂǽmãǚЯœԘ=χѫЦӰ˰ȗӼӍҋΰōʻ5vȾӽЄsķǷ',
            'source': "ƧÀ˛Ǜŵɛ'ϰӘϚƖonоәΒ\x9fȞξΜΊͽζԖЍǏơҘӤÒ",
            'message': 'ĖԍŁϨΓѻˊѴԦŗҔԝůΜˊʙƄѐȾґʦɈðž˽ýӢͿϬÇ',
            'arguments': [
                {
                    '^': 'string',
                    '$': 'Ǐѿ˽Ŵȋı҂τΩΜюńɰЯǫɩ˷\\ƂʵđJоźӔŊҔѐўƝ',
                },
                {
                    '^': 'string',
                    '$': 'ȢʥɠƥÁí\x97ЕʂǘԎɲɩąȾӟξUǀОrÉАĨûɍ§ĲŸӷ',
                },
                {
                    '^': 'float',
                    '$': 234063.6821375768,
                },
                {
                    '^': 'int',
                    '$': 4461355664701609986,
                },
                {
                    '^': 'float',
                    '$': 569939.8061982022,
                },
                {
                    '^': 'int',
                    '$': -4294506276403022670,
                },
                {
                    '^': 'int',
                    '$': -6130625609668321056,
                },
                {
                    '^': 'int',
                    '$': -6455377683979920369,
                },
                {
                    '^': 'int',
                    '$': 2391285744207349266,
                },
                {
                    '^': 'int',
                    '$': 6652739567821321159,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Ԋɷ',

            'message': '',

            'arguments': [
            ],

        },
    ),
]


class StartLauncherFailedEventTest(unittest.TestCase):
    """
    Tests for StartLauncherFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherFailedEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in START_LAUNCHER_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncherFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='StartLauncherFailedEvent'),
            ),

        ),
    ),
]


START_LAUNCHER_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 'ГиȤХ˦Ǵьрυɂ҇ˌļͳӫǟâǣ{ΤԤëʵϬȡɀяʍԡѣ',
            'error': {
                'identifier': 'ýŖPɪ¿%ʰѢʩ-˂WʄɗѪТЕƊЯțΘaш\x9bхҋPȝ˺΅',
                'source': 'ºφͽӯǙǈȨĦЍ-ļҠԍȏŪΤōȁʗӗҹˑчɮћȿЩˏȐϢ',
                'message': 'Ҽȍȯʨ-ĚԤӞȱЅ=ϊ\u0380ԅ˔ɋΤ\x9fíʃɌӥ˂RӋ˓ҟùњr',
                'arguments': [
                    {
                            '^': 'string',
                            '$': 'ьӭЮΣúQǛɹүԝʚŠс˭ϥ\x91ŝМέҾ\x87ʎ',
                        },
                    {
                            '^': 'int',
                            '$': 713805528189344666,
                        },
                    {
                            '^': 'string',
                            '$': 'Υӽ҆ľӦɏŞ0ԕ\x97%ТРǧCˇʻѡǆƥΘ$ΊͽǻǺъК\u0383υ',
                        },
                    {
                            '^': 'string',
                            '$': 'ԧŗĪ\x9eAчˉăsϹ\x92ĭʭʯ',
                        },
                    {
                            '^': 'float',
                            '$': 480140.0005777001,
                        },
                    {
                            '^': 'float',
                            '$': 134675.793240125,
                        },
                    {
                            '^': 'float',
                            '$': 346098.63486935664,
                        },
                    {
                            '^': 'float',
                            '$': 484916.32724015275,
                        },
                    {
                            '^': 'string',
                            '$': 'ЀŢΛźͽƎ?ċĿ˦Ƣ˔ԡĒƤťɫèͱȓϑ˯ϕԘŘöȯƪеĺ',
                        },
                    {
                            '^': 'string',
                            '$': 'øƧȹӏŇ7ǮȜ҆āɥŞӉ£ћɒԠUŝϹýӥËX;ÏͷӳȟϪ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': '7ԥԠ',

            'error': {
                'identifier': 'ɋч',
                'message': '',
                'arguments': [
                ],
            },

        },
    ),
]


class LauncherLoadExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for LauncherLoadExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LAUNCHER_LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherLoadExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LauncherLoadExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='location', name='LauncherLoadExtensionRequestEvent'),
            ),

        ),
    ),
]


LAUNCHER_LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': '*хǹŃǝλҘѼƮƦӽĬʋ±lҟƴϾͼӀԔĂʟΫϔƭǐˍфȃ',
            'version': [
                -7971931551079438267,
                1446674518620107694,
                -1459394048870586262,
            ],
            'location': 'ʺ¼ƄԫʻΔΣŭŧԤŏbǘîƄöȏ}Ыƹĉ\x92ų\u0383óʟƘǞǉƁ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                1325994848948221472,
                -8778456019265665043,
                7669806357919636184,
            ],

            'location': '',

        },
    ),
]


class LauncherLoadExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for LauncherLoadExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LAUNCHER_LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherLoadExtensionSuccessEvent'),
            ),

        ),
    ),
]


LAUNCHER_LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ƪěЭʪDƻƥԓϔӅĆІŸ˪ћÅ\x93\x7fƂɇȱƓÒýǷΊʝӄ¯ê',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

        },
    ),
]


class LauncherLoadExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for LauncherLoadExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LAUNCHER_LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherLoadExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='LauncherLoadExtensionFailedEvent'),
            ),

        ),
    ),
]


LAUNCHER_LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ȠJǶ¢ǿґŀKҏɌҜàƨċăĸҀńƪÀбŊɢɠӲБǬҐΠӰ',
            'error': {
                'identifier': 'n¤ԥϱƼƈɥҠèȹ6ќ\x88ŰŁѻӔӘϪлҥȩԘΓǄΡӤȘJӃ',
                'source': '¦ԬӎɼИ·ĦƱǉËӇľӆԥǗһѻŸÓԢяӯƢοίɬĒΪŖ\x98',
                'message': 'ʓҦҡɞΧӖċőҙЩ£Ԓ´ɘƦŸȎΝϧQ˪À\x9a˱ʙр\u0380ǝɜѻ',
                'arguments': [
                    {
                            '^': 'float',
                            '$': 569756.4233681199,
                        },
                    {
                            '^': 'int',
                            '$': -747450953551464176,
                        },
                    {
                            '^': 'int',
                            '$': 6263503468872528797,
                        },
                    {
                            '^': 'string',
                            '$': 'ϯ¯ӑ7ǜʶyҒӠ#ӝ\u0379Ͼ˙ӅСŎȉƿŢѻŧɨƟηáϢ9ў\x99',
                        },
                    {
                            '^': 'float',
                            '$': 571571.6469661933,
                        },
                    {
                            '^': 'float',
                            '$': -53267.75416462175,
                        },
                    {
                            '^': 'string',
                            '$': 'дЉѡȻ"ĄĺϋҰĂԪťϸӱԄͳˉЪѶҫɠƓvĵр\u0383˻ƙФЩ',
                        },
                    {
                            '^': 'int',
                            '$': 4773106129862865958,
                        },
                    {
                            '^': 'int',
                            '$': 4327309448970239961,
                        },
                    {
                            '^': 'int',
                            '$': -7827393755027104220,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'error': {
                'identifier': 'έź',
                'message': '',
                'arguments': [
                ],
            },

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
                res = foreman.Events.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in EVENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Events.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENTS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (

        ),
    ),
]


EVENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'ƓƑȿӠҴÂǕˋѫ˩ЄӹħΚƂɾӋ0ưŜ\x96ŨЬ}н\x9b\x9aȲҁφ',
            'target_id': "Ӭ'˛δʚӦƪĻʯӚӶ¸УǜƋĺdúƧʱӔчԔԭˏΦԂŌƝ˔",
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
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

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
                dict(field_name='extension_name', name='ExtensionAddEventListenerEvent'),
            ),
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
            'extension_name': 'ƌ҂ҷȝň˜ Ǡ\u0383ʷƘÄ[ɘʹАҨΫÎӚЫԡЫУ҂ȋ˓ʹˊď',
            'events': [
                {
                    'event_id': 'ǜͺk˽ИԠĂŒ\x9dǡԂÎ˰(ͺǚƚκȕΜԦǠ=Ԓ\x97\x90ļɴƇK',
                    'target_id': 'ťˬӢԁ-ȑ\u038bэ˅[ȭňҮ0ҙɁɨҖŭƕéņӏƘѻЁ˺Ŏ˗Ȗ',
                },
                {
                    'event_id': 'ˋȚŵѰÎÐǔĺƌёÔԆǽĬǭΈѣҟϬԃ\x9cƳҵ+ЅǛƃȴАƍ',
                    'target_id': 'ԣ-w҃ҊяѼȚɺџѼ\x91ΟƮИ˥{ż\x99÷ɭжʧ҇Ưϕ˭ʳ\x89ʪ',
                },
                {
                    'event_id': 'ɉɀӇ\x81\xa0Ŧӗ¦¬ <ЮϖȵȑȢȊKԢΔŋϰĕϒ҇ЄĄȱɏț',
                    'target_id': 'ϲ˾ĖϸȵĎŒÀʣʐ¿\x87ÕōƛкǗ˚ăżȸŧāΪǽřŜE\x81S',
                },
                {
                    'event_id': 'ɀǭʱѭŨĢŲŕ1ɧͺȃΜˎӘжɵĮжȦĴOƈɏxӊTɫRӞ',
                    'target_id': 'ŅʯѱǲʨɐŽʰʁщ\x8bkʂʯϺôȲĵ',
                },
                {
                    'event_id': 'ïϥ\x8eɑ$ʬӮǌ$ˮӪώԡȼûƳ',
                    'target_id': 'ßѤĢʰĖ÷Ώѣ˗ԄƇƧ¾ƄşĆťļΪˈbəԘʲ˽(ɕ˷δ³',
                },
                {
                    'event_id': 'ɐƳϏӺѣŤŜ˪ʘˀʩнϫȳԅȷΣϪ˗qĿĜлX',
                    'target_id': '´ʈǆРĔ΅%-ʱż:ԊǠӍǑӜАįӘÝџӔīÉγVɳÈǿѥ',
                },
                {
                    'event_id': 'ɕƭҬǝŵ¬šƽǚψÞrłĵé-ȲţīêѤϵʁīʇŵĀ\x9cƚў',
                    'target_id': 'þ\x90΄҄ͺ®Қ\u0382ɛҎєњΔœŮWϤƙЏƾńԌС',
                },
                {
                    'event_id': 'εӖΎϟʎϿзЦҦ^ȻĿɧʐʀρԔÚԔŠǂĵϩĊɚɏəˌ\x82ϡ',
                    'target_id': 'ȀŎƕǁΫb\x8cǯťɱ·ëĔҕϓçЭԫСÈʣƚČǛѬѭňǼɫȾ',
                },
                {
                    'event_id': 'Ǝҡϧԇˍÿ_Ηх˃ɌлԚľ˲\x85υρuȲӮϿѣϽ\x92ȵ£ƋȃΈ',
                    'target_id': 'ˑȍȕģˈ\u0383ˤЂԖʕʬϞŧѥ\x92ϰЏ˦ӔяԄýŻмĎMөǸ˩ˡ',
                },
                {
                    'event_id': '˻ĝɭΡZǰɬмϯƹɬԇҺɞˮҠύƯэĩǣ҅åì%JĵΈɴε',
                    'target_id': 'ÙÊǲқĨaĵĔƳ·ωŧόйεÁŻԙȬ¬àˠɷ˛˓хťÌāԅ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': '',

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
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

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
                dict(field_name='extension_name', name='ExtensionRemoveEventListenerEvent'),
            ),
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
            'extension_name': 'ҥшƯďŲcjjĀӅӽѵ0ŚϼΡlҨäϾ©ҸѵŗѢΜĈѫÈƯ',
            'events': [
                {
                    'event_id': 'ɛşҤţγӸѲˮ˒Ɯįѡ^чuŸÐċ\u0379ҫϴНɾā˺ȮśʝĻț',
                    'target_id': 'Ɉ\x88éș®ŚɱҟɴȉϯƻƮѤ®GėоԔĕΕˈьĮЦ¡ԥüѱȄ',
                },
                {
                    'event_id': 'ѹҥÎБå+\x85хƲSũȐɺȭˣ(\x85ӨɝtʟUƣӪӂŇȖ˼ͷҽ',
                    'target_id': 'Һ%ьŎʍ΄ǕɲΞˎӕȈìŤфȬ˫]˥ð,ƢӟƝҧ¥ľҼʍȺ',
                },
                {
                    'event_id': '',
                    'target_id': '@ȝӃӞʑʎƏdªɆȲҾĶЛѪΧɟж˽Ӿ',
                },
                {
                    'event_id': '˽vŸҘӺǌϮɝԎӑϕϠҵвvξ\xa0ɼѭЊ\x98íҘîčȼӠŶĝƬ',
                    'target_id': 'ӜǸҁ»ј=0ӶļřʊŁӚǽƋϕ\u038dѿʿʈ\x9cόϛΈѕΥʀƫíŐ',
                },
                {
                    'event_id': 'Ӊɠɇʒ7ÀͲӌԆϠǮƌƚѲ ǞĺұʏҭҏԣԌϦǊм§ǀǥĢ',
                    'target_id': '\u0383ɼбӺҳʽͻθ҈ȞљŅɮCҰҾYѤЉ˯ǣ\x93ӇԁĒŪЮԚƼ\x91',
                },
                {
                    'event_id': 'ɧӁВаӡЁҒѬ1tŴĎ˹_Ӿ\x8fɀïǠɐΨnńСʴÁNʥƉǩ',
                    'target_id': 'ťʈĕӳ˃ŦӞҷȧȤӴĻª΄bʙǞѳĹятӄwРІ\u038bР6àˎ',
                },
                {
                    'event_id': 'ʟ\xa0ƦҾӔɀɯȷʁϻԙͼǙό9ѹҸȒӔˤцΦȤЕɴFԅʘEҳ',
                    'target_id': 'ƜȇѕuĄϘűĵԝӉVѲњљԜǮ\xa0úŌɸĠ˲ˌſ˵~ԏĨʱȂ',
                },
                {
                    'event_id': '"Пί.űӦ˛ŴaȎӺϻǷ;ԛɘ\x99ϓҨǈҋȿşZϨǔƬĂϟη',
                    'target_id': 'ɿG˘³˸¬JшɆǵ\x80âēϽѣǄΤϸЫ"Ϗԟ҃ХɎjҝ\x86Ƞʹ',
                },
                {
                    'event_id': 'È˶ɎӃ˦ď\\уǝҊſπҘΠљʙ@˫όѰfЀNϘŝ"ƼЋ',
                    'target_id': 'ǁϘ˽џӴșѤӫżͳыʄԀàϸiǺҨʅƠє\x90ʜȄêɎŹȵĞ¥',
                },
                {
                    'event_id': 'ɊԘŴϸŶ«ϺǽʮˁѷӼЬԣϻǶŬǻ·ϺǶОθăĮȻΉӦǽѤ',
                    'target_id': 'Υ˥Úǈ7ʢ¹уҮÕԙ\x8aѿÖeʨѮЪǊ˭ȌљΨ϶Ǹ&ÃԫӑR',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': '',

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
