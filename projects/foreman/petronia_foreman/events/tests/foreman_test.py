# GENERATED CODE - DO NOT MODIFY

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
                'ϟ\x97ʁŏϐПΎЦǣǮˌÈjӚͶЭōþ˯ӎě˸ɟ@Ō}ΉѯØϊ',
                'ϧ(ʲΘ҄ǕӲɟҳҥǠť˴Ʃα˞çԩοҿ\u0379xǸÔǹӱүƂˆӒ',
                '˶Æŕӻθӵ¨ϙ\x9eϽͶˑǝƢɮyŔƞЕдpȿòϱǇſƀдǸҶ',
                'Þʦʺʅ˚μΡ\x83ΨԘƸДýç\x9eġϝЮЧȏŝĪîxрҪкŻǶ%',
                'ʀѢ¢Ěӗ`\x9eĹɸĩԕ\x8bUUɝқҹʈȞƌКРɰ×χНɖӞҢÑ',
                'ӤhԖќ˄\x94ɊԞԪ£ğ¢',
                'ƱsъӝɨȏûȰ\u0379ʅȗөхǯӎƏΈɘИϪҍɈňƆŴҵɀ\x88˝\u0378',
                'ˋӝƔӒηʙŊ˘ѻĎϾҟɁҲҷƅĵӧƲ΅ԤÒώѬƷǗɘéj҃',
                'ȲνŤêΨ˃jɞVɔɨĉДӧ7\x98JΪĮĆĥƇ\x80\x95ӣǧBÐϚˎ',
                'ӻЈ҉Ƅқзδǌ\x9cɌÉйʌӝњǇҕнͲÇѡȹȤʗČΟƄSϻʸ',
            ],
            'source_id_prefixes': [
                'Ã˴ǻЏ˃ć:ŋ¥ԉ\u0380ʐɤȵȗ3ƜӸҾѽԂӗǯіӥϕʱţҜȵ',
                'Ǳҫˌ\x9chžĚͷ˛ĥƢ˗ťɯЭδʚϴԕbOȼȧκĨԇӢɨǵԥ',
                'дȗŇĖʀĊѣғЪƤɀĳƷʎIyӕ˘ӮęиʡȳǊƠEͷȕǢғ',
                'зЊǌİҖĎ^ƭʽӍЪȎϢ˧ÍĐњӂɳǓżӫŘrԥɾRОӷª',
                "Β'üҩԈűʤ\x85zg˟ҖҾ˧˥ɬʲӶūÈғʅɅƹҏӒϼϸȻț",
                '˼ϓҕϾžѫʀǊҐǥ¯Ж\x9dîζXVѨƁμȫŰʗϒƒԪƀķȏĭ',
                'yϩѰü\x9aå_ϧɃģԝβƧʞĺĂũȎʵǪSςɀőʛȬȪćΩǵ',
                'ȫˌΒȀ\\˷èɋȼ]\x8dҜѪ˥˄ī\u03a2ƜʋӤ\x84Í"ћ\x9aϡҬ\x9aǕҶ',
                '×ŁȱƙǦɩ\x8eͱˡɡ\u0378˃^@ϔæǔϠШӾҕԟǈжƦǴ˄ƠǜĢ',
                'ΊƁȗРώΝɌǒҸʳʐ͵ēǞѧÊǔƾɂˍʖȇԕjОƦ\x81άϏƈ',
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
            'action': 'ԩϯŞȡР;&һˉȍǧҳΫūдVŉӖáͳҥƇaс@ĖƿԭɍĎ',
            'resources': [
                '+ȣǀ\x82χέӢƙåΩӐʸқǢȤҍŅԤɩǳ¹ΆĤÃҀƎʐĝ\x82ȉ',
                'ɡɟӕѺđcŨІĦǈϙ7ҤÙӛй\x8aʀɋÌ˪ƛØǽ\u0378ƟґɃͲϺ',
                '*÷ϣƇ˦Ґ˳ΩϥвǺĨʂƨɬǉүѡёͶēφǳίԞĔϵžԮʺ',
                'ӕʾǍ\x8eТƷǨҚ®kΧʋåɧäѕωΣpʁă\x8eӰўϙƷȆ4зʸ',
                'ųǻĸΞҍѻρΦħǹèXғҷӋґǻμƯɲΈǱњΚǊFtϨ¡ʹ',
                'ɗ˱ȼɪŴНͺ˛ȲˊĨ+.ΛƹЯǀˆϜʆɔʓżƋвМʩˢŸЮ',
                'īůӹƖгʃʓð҉ƒαМĶȁ\x8fˤǠϡɻƴƺϲ˽ʋ\u0383ϊƟȏόƽ',
                'ɱºȖƦʼЇƠ\x88έΎDłѲўϯМƟÆεǻ҅+ͲÊҮұƁΧİɝ',
                '\\ȚɶϞͱԖʥ\x94ԮɀƧ]Ϲ)ʩǙӠŘĕОtŞԉăǐȿЖ\x84ΝȄ',
                'ȫԩż|ƙɱiˠєģçҐѠѠ҄ΡçͲǓɂͲԕΖѵɘʫΡʤ\x82Ϳ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ҭ',

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
            'name': 'ȿϥã˒άʟɋӑ˫ǙȋɧԭҌϲĜσԟͶƔΌʱӽųòǐ˙ұΡʻ',
            'version': [
                -2723551032975079568,
                -6858210258615477382,
                -4436402777985051325,
            ],
            'location': [
                'ȱʗԧqǫòpɘФȯ˱ȋšеîğμ]ԑϱҐhĄķϜ»Ęʦӡѷ',
                'ŸԐǒѝϪŴfîȥˈƺҭ»ĔÕу@Ȯ¹ԀȣϙœуÖʆѠȃ˓Ѯ',
                '˼ȽɵƤҙǒνÇd£łҊυόәΡύǜȩ\x88ȧʟӵĵ0ϙZǞц\x99',
                'ǝȵԇһȦϒʃĄӍԑǜåďҪӱҖTӌӸɃАΖFƊřœΛӌѽʹ',
                'ûӴӴЙӰԥa<\x8e)ȜγӫаŒФʤʜͳΣԨȬѓӨǰϣǏӒνϙ',
                'ĝƑœҟǽɠÁԢϱįǒȚŸąұŇϩҶ˾у\u0379Л˒ҦˢƪɔѲȦi',
                'ʶӏҸ˺Ν]ϠƜǞҼөµʅ˜Ǉы\x8d\x9aӤҦˮƝͱΪѱОɞǙ\x9bĹ',
                'ɬщȞӣӏҩŃҮиϑӪ\x91ŬȧeΈŧțɄÖӒϚϗÑ}ДɨҨūѬ',
                "ЅMƑ¬ÊʍκǴΨˑΣпƞ~ҜɆ\u0379'4ҍ¢ƭdϑЀʝҤ˃ЎÏ",
                'ÜŲñѨƏӷЭуӻȒ˔ϗƎїGȗ˓ɼƗлyѧïϡΜͳ҂ͳĚԔ',
            ],
            'runtime': '§',
            'send_access': {
                'event_ids': [
                    'ȳ˪2ƝËǰÜȈ\x84ԇȇюɼ4ԑǦжјˊ˔Ņs}ϥȗʗŎvɑԩ',
                    'ҲɊ˦ФԏġʿɐӼvΤ>Ŏ¢\xadƐљĊǫĉ˔\x80ȁƦŜāŪѽĕ˃',
                    'ʹÖΰ\x81[2ȻӈʖƐЈώѶˀÔîȾ˳ćɥӷˏύʏțǊȴЬ¥Á',
                    '\u0380˥čŉʪšѐѕʩ]ƹãͽĂʬӼȸƑ˓3ɅʌИƽſșЂǗǁȾ',
                    'ЈŔʆǞɄÏϚѮ]ɀŀӢŕΐьΰåџѲΥƻ\u0382ǉԜҲͺËψϔǸ',
                    'ğʖ\x99ŞƱԮųɳͽęϢҫѧĺWo\x93ϴɣɲ҉æүή\x94ѮÐWʖȗ',
                    '8Ǣ¹ąӊ³©ҥʲ҇ғԊɞʄƙ҉ɻɵtӘ×ЮÝĢʌΖ˾ʣêí',
                    'Υ͵µυƙӉ\x99ƩŷϡàɋϼźΗȔ¨Ȅ2ȉӡ_ɗɢˤ7ҩ`ɹѶ',
                    'ɿɀAƳȻʺÌÒҤϣǫƗǎǘ¾ǽԒIӰ˘ψ+ώɃыñƁʯɷѱ',
                    'ñͱĸВʶҪӴёŔ˭Э҂Ĕ\x80ʾü·эƼĀ\x8bƥɁό˘Ш#˯[Ɉ',
                ],
                'source_id_prefixes': [
                    'ó˵Ф\x94ƛӎńtӌ!¡ΔӟЮɢʊDɽ\x89ΛԨƪļĻʛˣњʠſȣ',
                    '´ʝɎΝǪǇԗл\u0379ƐƔԃʖȸǯȬęŴԆʝǨɅÌͻĊ0Ũїϊˡ',
                    'БΧĪšҀùȈҭ\x91cȐ9úԄǬҰġӻǾÄĩħ˘μ҇ҘʰυҲɾ',
                    'ǼƚɣǎÚıōųóē§Ө&ӈȷŀĮȝǐʒĐЭïқ-ɭ%ѬϽŅ',
                    'Ӯĥáӿ\x9dɞʀҹ˪¡ǑĈMy˛Ġ\x8fМǠ',
                    'ƆиОińԅӆÓĨ',
                    'ԙgӤҹҟϚǰϽԙʘ\x85˸˪ɋɀćţʰɔō҆ƈӍӷҽĳ',
                    'ŹòіҭnțЎŨȱΉèϜWԉ˭ӌϤˡŀɆ҄ΆҭÍ\x81ÍŽП8ʂ',
                    'Ѝǰ˭bʄǣіOțπŰˉɕĖϨ4¾νɓǥɛÜ\x81ƜӬ˓ͻĵϱˇ',
                    'ʑêӷ˽ƛƅĈĈßS¬ɐ\x99ǒӍĵΐҚrŎϵηïĲƘϻʫƳ\x8cȑ',
                ],
            },
            'configuration': 'ԑƓҒύ\x9eѥиΦйƦÄ·Ӂ¶ĿͰŒěԛSʿʕǽɽъԕӭқϿ7',
            'permissions': [
                {
                    'action': 'ӡǡFȚʜpțȘǃWΖ0ӹӀĿƯɝΈ˵ɃBƒǑӢƦϒʙ8Ÿʴ',
                    'resources': [
                            'ӌ˘ѝͶɡɀ˙Ɩnӆƍ\u0379ϺȠѬÚӲӷƘϰȣŝαΕˬЮ\x7fàǁt',
                            'ӂ9ɇÀπƊȮиŝǩΠƎɼțʿúǺҤBӸ\x85\x8aӤ¿΅ĨʬŏˮѸ',
                            'Ǳí\x91ԢЗҨǠӵоѶҷîǝϟ}\x89ôхѝaȨЋ\u038dɊтǵǾеťʗ',
                            'ϦʛȘыӭӐҭШƅœĉϥǵɻʂɑƖńȉЫȑѬƑµ\x8eҞһÅÝă',
                            'ÒϾŜ%Ӿȹ˒˗мɩӦûϑɋЍЉ',
                            'ĢϡƖԐԧ¢;*Ⱦ˧ҁСασBǀʤCӇýѫџǆǡǣͲĲжƦˎ',
                            'λΗðȞƛЛɃͲΪεúќ37ЖŝɌÐƩëHȹԍҎǟɻ\x82ƢΉĖ',
                            'τοЀüɯӝǆЌXҪũҘςȘӛǿƉăЋ\x8eȈØ!tͻЖóˇǫӤ',
                            'ȋͳ;˙лЁƾșЈĂɸ±ΜґɊ+ҹ`ùEã΄ѝńѲѤ´ɿǷ҄',
                            'ÉƩԣЄĀĳҊŐĠѧСҋRϖϿĘCɞʃşʃƵˢίԝҔӺ¨ǚλ',
                        ],
                },
                {
                    'action': 'ĳϛоơʊÌwѐΏ\x9dҥǷʌ\x9cΘˡҵöҊƘŒ˽Ҕ϶ɵѶƁŝ΄Ń',
                    'resources': [
                            'ĆӅѶôɴ˄¥ĂҥˇʑĽԭвǿϷǾЏȍϯҨ˶ҔҩɴϝҒўȜ·',
                            'ѤÏэѢҟćŦϲp)\x82Ж\u038dǜЩŬԪ˘ϳМʧȭ\x9dǧ¾ϗӡϫӽȫ',
                            'ƨԕĿϟĩΙ˱҂ЊӌƄйӲʧбѓļìƽɞƠѹԒƼ¼ǠĸʝĕW',
                            'Όɇęħʥȑɣ·ӮҙȸɷůǇүǬͺԗǎG\u038dƧǀ§ŭ҂Ӆ;iǀ',
                            'ӚΠΤůȭТӦпʫ\x80ѼȮϻМԚӋÜɮŶɉxɡPщ\x97ҬƥЛǞԗ',
                            'ǶɶМˤд÷ȸǙЏʸ\\ſɬʞųԝ˧ʊù´ԩԥǗƸÎΘɷȽΈΑ',
                            'ʶЄúY˹ǘĨаǩ·ŴɨǪԩĬΔɩέԔ',
                            'ƌҵɫƴƾIӆ˞ͳһБǺƣȐôԘ҅ѯłˣΑĈƿť˹Ғ˂˃ȱã',
                            'ȹ=ӜɊpҵѷԭǧȑƈӬъϗͳч˚ƨдѠ˛CЖԙǠðΟӨC\x9e',
                            'ϨʘͷͽЋҐ°ǽȥӺj˹Ħɕ\x9fƀсЮȕ҂҃ĀϏѾʍ\x83\u0378ȷĞ3',
                        ],
                },
                {
                    'action': 'ȳҫϼˈ˚ûƼƼʛůЏVАɛ|\x80ķ˞ųѐĜҟУÞǧLλ˵\xa0«',
                    'resources': [
                            '\x84Ɔνѐƌ\x8fфά{ʉAȱѱԛӲϻҋOҺľˣİʽɃҥѫŹĚeɮ',
                            '#XҼҐȮq¯ưļѤțӥ1ΦΛӽĞȖ˅ρXҎʹŔċɻʫжӅS',
                            'ǚŤЎР0Ǝ˘ͷҜϬːǀhŧƬԓӐčgƲĖɻҋӂѶԎɰӀѲϖ',
                            'ǼӈӔѕȊɖχϩ)шÜΒĿΙŋeʧăÿʋ˱ў˖˳ȨЎєˠφʬ',
                            'ԨáǹѠІʯǜ҉ǪvĎΒоŀӲúʽȍưԒЧ¡ŅŲҵɺϯʴ·ϸ',
                            'ȃȱћЍɲPɩǋDѿҸƈԊƼɅҕɸRĹ˴Ʊ˖ѷҞˀˈ\u0380ѵøӎ',
                            'ҝȶΎ4&Ȗ\x84ÎΙϛˈͼ,ɿūѯIҽԝʶèΕѷÆʃËƧħΈɼ',
                            "ϣƪ˖δǷ*ʸ¸'ҒǡєϏeԧǋҰӉXХ҅˵\x8cӕӐVˠΘǽΝ",
                            'ΆőЄ4lЅɭǂ\x95ÊПǙŃєśĩıčɺϸƙċǷƝϾԈXŻчƔ',
                            'ʤƓЖԭҜψҀ\u0379êåÏźӲԎɨʹ˼˾ˣǘɚBͳЉϯɶѶмːԞ',
                        ],
                },
                {
                    'action': 'Χ˝ĎœͿҳœηŰѳ\x86\x8bɰϺ"ɡÙãǐʁÉʧ˧ʶюɤҖȺȃâ',
                    'resources': [
                            '¨ӌҟϏÖŐǀԚφ\x9cȰʶʖʸƽѲǢʏϑ÷ȃϚʹѮ\x9eɶϑϫȵâ',
                            'éҚ«ƟӽӖŵӱt˗ȽҪɚРѷ\u0383ѴɒΌřΣӌѤѴH˽ȟɁТϾ',
                            'ȴΰĉ˽ͼĵ˪ŪŪПұЬXʭʭȚʘѹӡÏÊԞϰϚǳ\u038dҭѽśϣ',
                            'ŭʺɋĜΧϔѽȈʔϙxʙ7WБӾΒþɼųԬ\x9bԉȒƨő©пĂѪ',
                            'ӲΗ4ӡΨΝʛƋЇЀʴǬÂʈˇ\x85ęƓ¼ɰáŽͰ˺ʂҩiàҢ7',
                            'ÇϳTΎƚɏ˞ȓƵφҁ˾ÝȂ±ͺ;ёƳʼӇʏТԌǽԔικϹ¡',
                            'ȟԤΥ£vIMĕȠʕӯɽԛǏϙˬ/ɥ4Ŧ\x9d{ǟßëԐăŋ+Ë',
                            'ХŜĻďôʠěÊЋģѧӸʓҋɓņ\x8fƔɚǙĢĸȔ%ϬѨӹDԐǵ',
                            'ɔıÄ˷¬\x9bäδéħɍʣ ƙѠɝĘưǣӐĶȁɻηΏӪȊͺåԭ',
                            'ƮˊęƸѻĭȡԇʶǦƍӦӀɒÈfŉ¾ǐÊȧԜԔĲʌӵĒɻǱƱ',
                        ],
                },
                {
                    'action': 'źȝӐŁ˝ӷ˱Pкc\u0380șɛȦǉ÷ʆͰɖȒʌϰϫҵūΆ˧ûѾȆ',
                    'resources': [
                            'ӲǅɹǐФȄǄАʣöǻȦѨԉкͷǉˮ˕ĠˇЩIφ3 ǫԎδ˹',
                            'wĂ2бˁԒŵɂҝȈx>ʣɛgĦЊϛưɶƹΒɴЂáXǪ˕fœ',
                            '-9Õ˘Ԧўę+ʒШҭŽpТÖǂΜϔͱȫѮԘΞӸҴoȴəʞј',
                            'ҰˀƜѻǵĨñȆʗľӛѸɎäĮǒƈƽƛ\u038dɥ҉ɟóӱ\x8bpӲǁӕ',
                            'ɽѶ±ԋyҹʺφ˾Ѯ˚ѿϢ\x99˲ϪƩҠśҹ:|ҏǔȅƢƋӛ\x85ы',
                            'äÀĕbѳJň\x8dǒ\u038bϊԃӄĥόÀɼȏοтʢÛǪёƜĬ.ȌͻҌ',
                            'ЪŞ"ȤêύԄԀҕXȿҩˌҴɪ˽ĆɁʳԛ˵ӗĭμŗʨƻ_ԎĀ',
                            'ɤȜîÉ#θɰ\x7fǚ,ɳ9҂ЋԣϘѱϮȿ\x84ņê\x8bţ\x93ȏć\u038daê',
                            'ǙƸҾǠ˳ʮ\x9aĹВÇӲɕĐρɤɐȈΚέÍъҶǪČʿËќϺ·щ',
                            '@˻ȂϗǵtǂaȦθȸ˯ӲрсʆͰфɋ˙žНǰή҅{żěɢɫ',
                        ],
                },
                {
                    'action': 'ѹâŒԮ¸ӇѐȓϤєјtw¥ЩԏºÍ҂óӀчВГ;яǡҳˮҲ',
                    'resources': [
                            'ˁʺŘʑΝˇϳɍ®ĂӠðȥLЖiɨԞǇσɳϏѣțψþϮԟƦɁ',
                            'ȍÓ΄ǬЃǐŧ;ȂǸщʛϝO˲ДӹʑʫӅ˹Ϟѻ\x84ΙƎW+ǻ¸',
                            'ӫľʹ˯˛\x87ΝŐɡľ\x84Ĝџõŭǆ\x8aÉǉşЃĠoȿҾyѰҢ¿Ӽ',
                            'ƇȊɩÅǠҨԂȀѼ˧ʭŏɣΞɀƘǹ³ҸҌʙēѧ϶ǛϞӚŕϢв',
                            'ӸԬŁȲǋȢƮεˉ·УŅ΅ʞÜлΣȂťʼҟ\x9fùȖɯLɣŃĦΓ',
                            '҆ƨǠҧ\x9c˥ӵʝʄϧ˃˚ĈȺɻțҕϩ˓ÂŮԤŕ×ԄӅɢʲΓÓ',
                            'ƍъÁɔˡŲȵʍϜҩĻ˨ӺԪjҟǋϟ˕ʈγ:ɿŹʲԤҊǙòˌ',
                            'ϘŤƢбҟ¼Ѵ\x94ɖԣҀӨɊʔԜԝҟҡċѭȥȌˈȘɂſaԏőγ',
                            "ӿřѡɻEȬьÖӒǾWƉΒ˵ӟ\x93ʹϷϮ'ȾѥñäȲȞȑюϿҎ",
                            'ɏӍ|ӹǦсƩǬÜ\x8dͲд;ϟ\x88ыƣɤɆɕ\x8fTѷɸцďИԙʺʦ',
                        ],
                },
                {
                    'action': 'țіǟǩʵϛǓԘwҘϮԦҔњɟ|ºГ˒À°°ӠҔ]ˣч҂÷ʮ',
                    'resources': [
                            '\xa0ɦ\x9c˟lʡǪӷƔC6ϩɠѡúÞҶ\u03a2üˏМӪԟēɼһčԂÑυ',
                            'ΒҜlХÙЧȕԮƗȐЙӲãȦ\x80ɴÌЉųŦſͼgҬ˽˕ˍĜŕȠ',
                            'ʨŊƓ˵ʓ\x9dʜЙϊĐκя\x9bϙʴEʦӂȸʒ\x94ҢӍ¶ȺѦύȫŜЄ',
                            'Ǿī´љƚΩ\x8cΊϜ\u0383ԣҳΖǮ\x8aȋҌɂIЬˎ+źƑːʄСɦΌȃ',
                            'Ԙā°ϸƵϱ\x7fåƅ˂ɪǲʠſ',
                            '<äťЩˬŏǔǹύИĦρӪԢ\x8dȤþ3Ϊҏȧӝ˳ëӪ҅ÖӂIϩ',
                            'ʞȳųŞԟԠεƚѲҡѽϔȑӂӜʌшθƦŌǼȳŮԨн¹\x86Γ)˦',
                            'ǴҏèЩˎŠԧŰʗԌϜӢǸҙϙȱǇβÃ5¼бԪąйȻΉʣÂ©',
                            'ԎǑȌǱʡϩ ?˂zǗƔŻȔμýБĝˊţĭ\x80ǖƯǜ˪υΝȜɇ',
                            'Убh;ʋÅƤƛрĜǊȦƋʡҤШËƨƞ8ưĠǨ+*Ǘй´ʂХ',
                        ],
                },
                {
                    'action': '¹ŧ϶ƏƓїӔ¨źЙͲÊµʥ˷9ɻ¥ԥʌɖЎʏҠTǑΩƉҲӠ',
                    'resources': [
                            'ӝˍʫő҉ѹ\x80ÖȜђϿϘƐҐԁ1ǋˇӒѲϖƥԢʄÎғˇbĤч',
                            '˅ʷàԡĕҗʿͱÃȮԍèĤ˙ҋƚύѰέĩϖƍҼɿЁЈԆŖӗ-',
                            'wȆҌηǜɱÈɀàѦ˕ΨїʄЀŔАőǠʛҬ¿Ӿ҇ɵ˖ҠʊɺÄ',
                            'B҉ǉʕ_ǿ϶ηЪɍҽ\u038bƇȫʖДq¥ӖњӍǰǬѾʣҟ˻ΙҼƷ',
                            'ƮЫáџʙʨùþó\x9bԗ*ōͰǤʮ\x99NԞӐͰ\x97üйȡѩҪTơ˒',
                            'ʡǲҲáͼȚķϳмÝӬ\x9b7\u03a2ԉ÷oďЄȋŤƕҺъÃĎϦɌjЗ',
                            ' ГǈςīԘΝыʍԓÎɭʳЁʯΘӖ˓(ҲʍҏӮЅȵ˅Ǿѿтô',
                            'ҝ҄\x8cŏɉÅ҃ȏǜCͲ0ǉŖ-ӪΝǍčӪЊέȊѿҼъӿчɔʮ',
                            'Ӓ5ÂòҼĴ\x85ӱÔŐӥøлqˈʥˤԌϢèІʙȄԉEǶѾʸĬʽ',
                            'вǩԩŌǢƉ˹ӱϳϧԥҋϽφ£īэҜΏȹԠ҇үƊ\x84ŧÁǧʣͰ',
                        ],
                },
                {
                    'action': 'ӁƤеɎЂž\u0381Ґ.ȃ<ɒ3ɎǈŬġɗĨ)*˶ǜôŹ$ˤϔ"Ϭ',
                    'resources': [
                            'ƛõʺÕҲΦɼžӇƺǷkθӝҒȕˋЙҠϟΆˠʷӟ@ғ¥ȼљň',
                            'ζқϢuȼ¨ģУˁ·ɇɹόȄˀџƑĤʟÆǌʯδЧϒҫß\x81л˥',
                            'ñ|эň˧ºıԙrY\x8eѰÿTƬʙàƜϕ_Ɏ9˱ʑɁĳОŢȓǷ',
                            '÷żɧÃÍɫЪÇёȰäȂǃȾȸěĕңϯăϷʃȳ¡ġΣϭ\u03a2ȶñ',
                            'ӪÍ\x80ƯŰɒèϬ\x87OʄőΐćưѰȂҸĨƜȞˠȍө+ъϨŸӫϴ',
                            'ʐ½ԉϒʆ˾ĉáĶȔºÝъУΙɌԆɻɧбǒӸȏѠӆ\\Ԭөɺ0',
                            'Ϝ\x81ҩʫŠǩҞʭ§Ӌ\u038bҶķӑØǻςĞȧȞ<ĻΌϗǒ6×4ȴƔ',
                            'В\u0379Ҵʚ˘ρȤ˭ԝԚŎŝƧ˫EΒЩ˴ɚļ;а)ŰКжHpvӵ',
                            'ˁӏϙŲĴԎǘӀӥнЩȿǉɠҍĈѝʈƁƿЌϢƤơČ\u0383ēε҆ɡ',
                            'ĀЧͼˑ(λÞӕːɶԖɪʘʔĠνƬмНǺѕԧкМ˖җͶƳ+Ċ',
                        ],
                },
                {
                    'action': 'α»ҏӍ˄ƭΪȴΦĵҳǸˌŭԒșˠԉОӽGѕξоˑ\\ɃĭǠƬ',
                    'resources': [
                            'зπǃѪ2ќ\u038b\x9e\x98Ѻ\x8fʎ>õԚ\x83´ÔӔӥĺЄ[ΓjʈӘΥ҅Ǖ',
                            'ҟƕđȵHƟõ˽ȼɡ˴.ӉҝɡǶҠȴ˲ƨǫόȿɒЬ_ɫʓȼi',
                            'ɏƎĦҋŁWąɈǝčȪơ˸ғþ«ʐюЉѲɊȝʃŞ҈ʧЌԊ§ǎ',
                            'ƎȶˤѽѸƮoĴґ\x9eϺàoј|ƊĘʘк˘«ʱГƋТΐőÕҩʵ',
                            '˯ўδƙэ£ȭíҌǌҴʃǽʌ¹8îɋʗʝηҟȔƝƦȖǾԉ³ө',
                            'Ԙԑдñмź¬ƏʓϞĜ˜ǊɪΕ҂ĶͻӄČǉǇWѬ=ɗɔӖҷɾ',
                            'ΟԨśЕȗ¡ӌůзӡ÷҈ϷψΔïЅŨύӽʎtȳԠǵӝ,\x80їȡ',
                            '҆ʪϒ˸τѤǆΚŜǀОxdɑԬѱɱЦɭĹĤ˵L1ЀҺ0ɜ´ė',
                            '\x95Ү¢ЦʥqɰŪ\x9cOͼȀ±ΙʨÙͺɝÅԦΕ\xadѩϜˈˇ˦ңѰк',
                            'Gɛ˅Џɂɻ˰ÇkéɄ͵ǿфɟЍŽȀǦKӑїӒϼʿˣυ˫Ӥɏ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'κѱς',

            'version': [
                -3791212013180937738,
                -5554667688371090225,
                -6027370839467082790,
            ],

            'location': [
                'ө',
            ],

            'runtime': 'Ϳ',

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
            'name': 'ǾǌΌȃǶiűЊԐƕ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ϯȰƕ',

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
            '$': 'ð¢Ӽ҃Ȇ¸ıΔĀ\x97"ѺɘB\x8fõГѷǀӧˈ5ЋÚũǹˁӺϽƁ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -437420924973080923,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 805886.1558482397,
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
            '$': '20210413:000902.493341:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '_ʿѲĜϰmΥψuϘȔµ\u03a2Җ˵ǟº\u0382әͽŸʔɿӈĤŚǾΦ%H',
                'ВΓѭ˽pӪˇ˴҆ϾςÈӢӃƬίϏǸЁҲ.ƦХȆҖѱʞȻĪα',
                'ʴѳ\x97±ѡŖѼ\x95ʿȤȾ\x8cѣǮɤǦúљÛ\x96ŵϳϋĢãʋЮʷԎ˩',
                'пȹÌоɲš˻ɓρĈĶ¿ǣѠǘç¢ӋŌ¼ȒďԨöŅ҉îLүӣ',
                'ʷÅŊҿΒĸƋԭјɊǮ˯ЙҦǛӷ ϕȎˑЯѪ°Ͻɔ\x8eҡ҅ðѠ',
                'ѯ϶ЛūҼɰő¨Ҍ`ѵŮϳͰΚϻʦƠ˃ϵΖɮ¢|ѱбȆÐʠƩ',
                'βǘ÷Ӭ˳ʒԫUɖ˝ԮӁ҆ΚΙ}ϭѢȡȺɌɁ˖н*ÝХƥsĖ',
                'ѬVϓɜ˰ә@ˇǨïԑÐƇЗDЮХĝΏν!Ç$¶Ȟ\x8bѾҩǳÇ',
                'ˈ˴ƁȒȘȒѥ¼κҝΗŀdƲԈ@ʹƙѺħˀԜӂLŢ\u0382ʠ÷À ',
                '\x80ȶdĘƃɎťËŖňǱɤĘƴӒȢ\x85ӿЖĘδӑ-ԇԡѻХʔOÝ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                8913758935939788747,
                -5038735004497064989,
                -590258884363617008,
                -5537438907557152213,
                2529798497893770915,
                6465957011879545473,
                -6105138236861332676,
                -6561577316626036841,
                -6938085299729988587,
                -8912762682367206288,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                613438.1276993739,
                512167.80717556167,
                492032.7969965183,
                826464.9575808024,
                236213.25048354047,
                253124.74451778218,
                679675.4926000612,
                838031.4008368583,
                751952.9513021224,
                348852.3357276361,
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
                True,
                False,
                True,
                True,
                False,
                False,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210413:000903.475520:+0000',
                '20210413:000903.494023:+0000',
                '20210413:000903.512106:+0000',
                '20210413:000903.529024:+0000',
                '20210413:000903.546438:+0000',
                '20210413:000903.563747:+0000',
                '20210413:000903.581709:+0000',
                '20210413:000903.599428:+0000',
                '20210413:000903.616315:+0000',
                '20210413:000903.632938:+0000',
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
            'name': 'ƭҊЃ˱ʆģ˃ΩͽÃ\x81˵ӘӬЛƥѸόі\x99˨Ǒz\x81ğ˺ҐЭʨƙ',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210413:000902.039845:+0000',
                    '20210413:000902.060354:+0000',
                    '20210413:000902.082531:+0000',
                    '20210413:000902.103068:+0000',
                    '20210413:000902.123047:+0000',
                    '20210413:000902.141595:+0000',
                    '20210413:000902.159839:+0000',
                    '20210413:000902.177955:+0000',
                    '20210413:000902.196421:+0000',
                    '20210413:000902.215924:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʮ',

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
            'catalog': 'űG˩ʰŒҩ˟ϙ!ӎԃϨΗӉ˳Ҫ\x8bɘǍйňԪƨ¥Ѱ˕ѫΩˢш',
            'message': 'ĬȿǺƍųæ£ӛ\x9blӦşҙġÏƢɸÙõƥҜ¿҇ҀɩĠǴΩРԃ',
            'arguments': [
                {
                    'name': 'Īыʎęϟ˺ӑΜǤŉМΰɌϟŴśȿ\u0379ƯӍϨӇ',
                    'value': {
                            '^': 'float',
                            '$': 525263.3264431678,
                        },
                },
                {
                    'name': 'ϛԖƅȸϽóÄИɆҖqǅu',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210413:000901.061469:+0000',
                                        '20210413:000901.075384:+0000',
                                        '20210413:000901.090363:+0000',
                                        '20210413:000901.107601:+0000',
                                        '20210413:000901.125793:+0000',
                                        '20210413:000901.142403:+0000',
                                        '20210413:000901.159586:+0000',
                                        '20210413:000901.176532:+0000',
                                        '20210413:000901.199456:+0000',
                                        '20210413:000901.222112:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ϘąŮӗʱҍćǢǍʼʍƔÁŢÖϬǣŕȎϺŜĴпϯȁʰΣȐҹǜ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        72331.33678762492,
                                        -30172.32154470429,
                                        888330.3435039535,
                                        455646.2382308162,
                                        666297.371315146,
                                        256724.75183266087,
                                        553910.3567620942,
                                        -41962.74932508796,
                                        884823.2045662823,
                                        867283.6335487788,
                                    ],
                        },
                },
                {
                    'name': 'ѓàɚˏҖǥЮƋǒ˖ŝ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        159376.43957469967,
                                        840737.7064450008,
                                        943374.3931357703,
                                        824810.2192020026,
                                        780894.2782372319,
                                        249514.00631448638,
                                        79232.32336276857,
                                        173239.37033082434,
                                        120161.25631577268,
                                        223712.2223721089,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '\x80ʥ',

            'message': 'Ԟ',

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
            'identifier': 'bϏŚԤ¿ɉȨθΠǬƐ\x87ҵƞӭ\x81ыВ҅ˉƱώğУÆ˼ĒԙϞĀ',
            'categories': [
                'invalid-user-action',
                'internal',
                'internal',
                'configuration',
                'os',
                'network',
                'invalid-user-action',
                'os',
                'invalid-user-action',
                'file',
            ],
            'source': 'lʈ±ʃԮÃϳ\u0379ʃģʋͿЊ³ɰȩVΣєɓάȱҲƯ\x97¬ȈԢʂä',
            'messages': [
                {
                    'catalog': '\x94ΝЃ\u0378Ǫӷ%ȍɆχăГӝѤƦ\xa0ēƕСұś˭}ǦрΞŹͺΫś',
                    'message': 'ĥґНɿ¥һҝԍӑ ÐȰ§ˈȁ¦υ\x92ɒɧ\x8fƹɧҷϒϲҾśĕǄ',
                    'arguments': [
                            {
                                        'name': 'ƍĮɞȬËϖȵϱӺλѿIϫҚGŦїѵѷİЮoŏ\x95ϢɳĬϐ˱˝',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɼϱMï˛ҷǩʇϓÔkˆŧҁŃʡ;ϕ;ŕúȾҵ\x8d',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'қEļlП˳ӨͼǃʖӱTȴȋˆ\x9dŶğȞҠҟ¨XXũŒƦЍϋһ',
                                                    },
                                    },
                            {
                                        'name': 'îYǽҗǵ\x95Ȱш˒ɨȉϚӌӭ;LôĂλФȥѤǻ϶˅ҍȳωӆӿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 21419.020445984046,
                                                    },
                                    },
                            {
                                        'name': 'ӯ-ĘæĻέϴ\x88ʅ\x87ɾĺGϖфϑϻӝĉҢвͻГƻзϾԐʙÝƗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ό:ɮѾ#ԇŒȝϕƽξ\x96Йʂλ"˲/Ǿ\x8fϴҤѺҕǂġʋNԁǶ',
                                                                            'ӦįΡʋģѨԎ«Ѩ҉ŬÜăмœƋұ:ҜƌËŋѤ,>şʉΔϡ\x99',
                                                                            'ǤгĜϦŬЭ.jǲEèǢӹӚŨ2ğ\x98ҴɖΡƳȞ±Џå8ƊϘǈ',
                                                                            'ÚÎ\u0378ҜʮȹÖƐ˶϶žЂ¿ͲǞŋԞżÿƑϠѯȌǲBAΧƊƣȟ',
                                                                            '\x9aģȼȖ°ƞǆèԢʍ2ƌŰgƔÜļӡˋǕ΄ŃΜˡӭӎ½ʏԗԖ',
                                                                            'ϻ˕әҙyѩѪťĢŰдÝҒ\x9bȌˤ½ʍˍˎ˦ҴˆԮɁŭƙϘ!ʇ',
                                                                            'ӺΕɴ˯ʳѳɡѦǾfƧԥЛïҭɴѼјǭҍκΙ3ӥʢɪ˾Ð-Ҁ',
                                                                            '˨өӥқʮЌјҟý\x96ђǸƁқ%ĽśБĜŃȓξԍ·PȰ;ĸIÂ',
                                                                            'ƠêаƙҺ˟\x9bѥƂǵĤөǹÒэП ¶cÙљøĦѢЪɷʁӏˑǎ',
                                                                            '˃ӏĒќ;˛ϞΫǈÛǠЎÆχŅÃѨ«η&8rϺʻ+ĬΠєɃƙ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҡȍ¢ȺđԭРÖʣƧȟ\x81ǡΞдһϭѹӱш',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6607663745106486590,
                                                                            3961674647153666470,
                                                                            -8157102138648888773,
                                                                            4326473585350671692,
                                                                            1405492345259120955,
                                                                            7990620004594067437,
                                                                            -1003933046439400124,
                                                                            -5945962886522453508,
                                                                            1427124720723813265,
                                                                            -8985524350199306300,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÉАɍÄНŞ˪˴ЂˌȶǑŪǞѴÀĪ*}ǪϤɭӴ҂ȍȌyΪѥҋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8512659369251405731,
                                                    },
                                    },
                            {
                                        'name': '΅ÂĩɃÇʓԐϚ0щȘŨFϖʑрϓ˔ɬ}Ŋ/Ҳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ҟ4ʔӠLӊǯƘǌśϊīŷӾ\x92áӖ[ĲΝʁȕʖŢӦĚҬΥ˼Ԏ',
                                                    },
                                    },
                            {
                                        'name': 'Ǽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            728708.5730916447,
                                                                            470369.22953500296,
                                                                            746976.7028287931,
                                                                            187223.74767053738,
                                                                            922607.4490456366,
                                                                            4772.30679815021,
                                                                            905392.1020583652,
                                                                            793967.1605648266,
                                                                            927383.5774080196,
                                                                            221565.63854453404,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'd˸ǼPˍӞҝʝ\u038dʎӭύȵɉӷŇѨʩϯԟϼåЀмВΜЛÞǧȭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:000852.926631:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΈĤԊϱǃÍнʒ±ԞͲwѼʧƈЗ[ԍӗԍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            928232.0669969694,
                                                                            786771.4884613923,
                                                                            275160.00096197426,
                                                                            351651.67780585686,
                                                                            337855.90270961967,
                                                                            619634.2190989072,
                                                                            57096.24044430524,
                                                                            878.1895530664624,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ß]γŔɰҎGԤǒрǜȧʉӄЭĘŕ^ȩэƨƓεǅЧҷ÷ȝÀʺ',
                    'message': 'ŵºΗϼbĤΏ\x99ʈÏϒԙĔĳЯƵĥƒ|Ϗ8ȎƊҋЅɮϿ΅ϗҲ',
                    'arguments': [
                            {
                                        'name': 'ѷɕƳșˠ\u0382ЯtǺΡɇҾК',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҚËβˑɥ\x8cĦ˜³CéѫΪϵӶѻƫȰќЯыӜνѓȡɓȆԂ˺ȼ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6232570333207985021,
                                                                            -8317540341657735877,
                                                                            1257637736699898980,
                                                                            -5234273715311373289,
                                                                            -1819409505430569714,
                                                                            -274579811019745043,
                                                                            3233472975533209462,
                                                                            8275724971683777074,
                                                                            -131733810900484764,
                                                                            -7445073307437482998,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҆ʺĞ˰ſУмζǆřӃ\x850ǋȳȄįЉʽƅúΕӨÙʴɁԢǏ˨Þ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x9fθŇϱÑβŌєіѩ˪ØҵΖʉķǌǄ\u038bϟÏҢϥ_ƹӉ¸˝ΰ϶',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϤƒϮxʴӶ˺ȍԮĵΜҥг҉ʲϚ҇Ϲϕʚι˪ɕɝԆҼʿҍӣŅ',
                                                                            'ÓҘԚƺʏɞȒ2γѕКҮҲʁ9ѰБ˨ƺƫίǠӜǳǗҨǁτӨΥ',
                                                                            'ђӥɐԪΖΜgќȂѰч1AѪ\u0381ω§ӖǸɛӷϷјѡǅ҉ɻԞĆФ',
                                                                            'ŜƤȆэÜŃÚř ÂO[МЏрʂΑƒlFљѼкσȖгʱҩȡԨ',
                                                                            'HǸӯχǝіǮƣĠԍư^еǹ\x95ыьҲЂкʙƎʳҟƻś϶Шīu',
                                                                            'ηљҘˎɦăϚҼԝßѭMû˰ιϟӪϢԡϼөǆдɜуӜ\x95ÅˠV',
                                                                            'Ʊ3˦ʥӘČŒΡŉɿβϦȱФɯÖÌϓũѹѭӟʵƎсȀʉԪɠэ',
                                                                            'ӪɊЯ˸Ӽɾ¾ƔˆҦͿ\u0383KǙÅ˓Ѡӷԣԗѥ\x8eҕ˝ǠĺҳЄǔй',
                                                                            'ǐʿĲɩ|ǃĊȪěǢŎӴįȅԔʑĔɠ{љʮˌʡԄ³ž-ʿɚΘ',
                                                                            'ѳʊЬșҙԁİȦ˨Ś\x81ϓˀơ˅ʕ³ÃǭԞ|ɂƺѬLľʫƢϔƤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŧ˽Ӟ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -813492622115873712,
                                                    },
                                    },
                            {
                                        'name': '=\x92ĔИȻÿР˰³\x83\x8cʦťȄʔqεǣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            239745.88178194134,
                                                                            642705.22223376,
                                                                            526938.9160900732,
                                                                            -85592.70777192821,
                                                                            707503.8937496309,
                                                                            168265.13651438098,
                                                                            634346.0516439716,
                                                                            676443.3977198979,
                                                                            205336.84443891566,
                                                                            708711.0748267279,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѡϠ&ΟЈȉ1ÌźӶϽƒԗɆéҟƙĮϑʒӼˣμǉԞɿԧӒƘŤ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɷӽөfϾIǚБɭԆӺƍβзѓ÷ƦÞѷÓĪέƞŕªƯl\x97ǌA',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000854.734504:+0000',
                                                                            '20210413:000854.750778:+0000',
                                                                            '20210413:000854.766322:+0000',
                                                                            '20210413:000854.783602:+0000',
                                                                            '20210413:000854.802571:+0000',
                                                                            '20210413:000854.819702:+0000',
                                                                            '20210413:000854.838971:+0000',
                                                                            '20210413:000854.855929:+0000',
                                                                            '20210413:000854.875905:+0000',
                                                                            '20210413:000854.894513:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '4ɰOȔŴɨʚ\x9cĕԣƩҟù',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            377964.16879737657,
                                                                            340921.5973095553,
                                                                            -28129.766613658852,
                                                                            628998.9543286669,
                                                                            -60821.67567073069,
                                                                            816988.1448593714,
                                                                            914657.8717352072,
                                                                            197165.06398989708,
                                                                            867481.1576728857,
                                                                            353691.7643312794,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȝʴɴϭӘƘԡћνЅүϽʊǁΎϷϡ˙нơѸăЉ\x8fƖ}Ӳ\x89ЎĠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '»\xa0ĕǠԕω˯īǸǁҿʹΫȠѭϴÀ¼Īʢυ\x7fˠлҽϠƀΕǶʻ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': ',Ȳɹ·ǒƄǲĔ\x92ɽʙȏhƌSӎËӳˏƜϚΜ¾DяʨâƉήɹ',
                    'message': 'ҒүƯƓǭі-ьѩωϵɑʸȯęNɫѬÈǁͽĿ˔ËѼƩЦˑкӔ',
                    'arguments': [
                            {
                                        'name': 'ÙҙƚĊ˅ѩο·',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:000855.431535:+0000',
                                                    },
                                    },
                            {
                                        'name': '\xadϟ¤фʭſÅЄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000855.499778:+0000',
                                                                            '20210413:000855.517848:+0000',
                                                                            '20210413:000855.534721:+0000',
                                                                            '20210413:000855.551821:+0000',
                                                                            '20210413:000855.568724:+0000',
                                                                            '20210413:000855.586313:+0000',
                                                                            '20210413:000855.603582:+0000',
                                                                            '20210413:000855.622080:+0000',
                                                                            '20210413:000855.639720:+0000',
                                                                            '20210413:000855.660725:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĚͱưӊԦԉǟZBȉ\x9fġҸӽʰwâȧȸ\x8bмòśʬԘȾ&Ówɘ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000855.762483:+0000',
                                                                            '20210413:000855.781027:+0000',
                                                                            '20210413:000855.798570:+0000',
                                                                            '20210413:000855.817272:+0000',
                                                                            '20210413:000855.834364:+0000',
                                                                            '20210413:000855.851155:+0000',
                                                                            '20210413:000855.867985:+0000',
                                                                            '20210413:000855.886969:+0000',
                                                                            '20210413:000855.906243:+0000',
                                                                            '20210413:000855.924527:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8d˥,Ӡƭ˄Ţ\x8dщķӴɭϤзʵԄѾƛѾe\x81Ġ҅ԐˁˊpμǞɀ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            228109.9672501086,
                                                                            590029.9461947347,
                                                                            728991.4589349389,
                                                                            998847.9532187011,
                                                                            406879.06638445234,
                                                                            919899.8369188687,
                                                                            597993.8492310942,
                                                                            2420.3583464166004,
                                                                            6276.931642739073,
                                                                            530583.4226243142,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȕ°źƑȖЬę\x97ӵϺŃ@ʂQǡűU\x9cöíӗϒOŒѪhMǯĿ¦',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 479810.6740598823,
                                                    },
                                    },
                            {
                                        'name': '\x80ǺɎϜӇԭʳҫί¾',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'MƱ˙çИ\x8fԆϞʕVķƾ˩ʌŌV>ĹȔʵӱѵ˷ɔvʮѿˇȀȿ',
                                                    },
                                    },
                            {
                                        'name': 'ӬИȜМϥхľǚǽδĠīźʤZUș³¢YƴǁϒԊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʄЁäԚɓϫγ҄ВȬьyÖNΆJϦǒϐ®Ԫ&.ӜǑɯҸӅʅU',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƫˊõҒɀӖʿŶňËϒΌƺ³ϒɷśЧūƁȑ\u038dӧӝʂſƷʲҞ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            405208.8677797514,
                                                                            984666.3319815188,
                                                                            235892.9750326801,
                                                                            379256.8931701623,
                                                                            274180.8952716997,
                                                                            211620.19681133382,
                                                                            69321.50819308142,
                                                                            750740.184926748,
                                                                            800803.7592394884,
                                                                            500311.9063500301,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "σ\x8eŸɎ.Ķ&\x84ĐȮ'ķѠҠúȣΠðë˷0ȡƓʦθŘΈҊѥȧ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʈҁӻǴαńć˚μ˦ƝĬ\x91˖\x97HɜƋʻȇъΩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            706000.5100616149,
                                                                            87277.1663312848,
                                                                            -57560.0239676325,
                                                                            635332.8707472526,
                                                                            43578.4235006737,
                                                                            737469.7121767342,
                                                                            850547.5442559812,
                                                                            75385.94576448019,
                                                                            402296.12272966886,
                                                                            739168.1562386611,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'οƍÇΎȕņɩȈD˗ѬӕHmʒѕİԤŔŗ҃êÅёԗǘRϢHɼ',
                    'message': 'ˁǥuХƻ˻ѝȯԬƷαƓΘĠƉȀђϚњγÆ\u0383oµфǭщǺϵɐ',
                    'arguments': [
                            {
                                        'name': 'ĝOǀ˻AӃɾƵҢ¬ƈҨǠϢʌ·Øć',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƦŎж1ӎȄƵÙɓɻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 496810.5967357424,
                                                    },
                                    },
                            {
                                        'name': 'ėқԠŰħöҥҩʇ\u0382®Ǵ˽ɴ\x95ƜȢɰнĦ˃ǣ5ɗѓŧ˯ѡÀ¥',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЈŉʼǮǰϳƘȒ˜ǿēˈ҅ˆҲǏͰŐ¹½ȉѿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 633046.1378287411,
                                                    },
                                    },
                            {
                                        'name': 'ɆǭȯȵßĠшƱЌů«íŢӑ˺ʋ\x95ďʈɑƥΚǿĶЏ҉',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000857.631676:+0000',
                                                                            '20210413:000857.652675:+0000',
                                                                            '20210413:000857.677254:+0000',
                                                                            '20210413:000857.697007:+0000',
                                                                            '20210413:000857.717266:+0000',
                                                                            '20210413:000857.736782:+0000',
                                                                            '20210413:000857.756297:+0000',
                                                                            '20210413:000857.776375:+0000',
                                                                            '20210413:000857.796351:+0000',
                                                                            '20210413:000857.815905:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȾŦŃa»еЙˡьΧџӅ҉ť(ϸɯ˅ȋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4647289993775836464,
                                                    },
                                    },
                            {
                                        'name': 'ȳҢåч\x85ǉƈÙІͳЦ¦ƫȴǾɄ2ɋCƳϑŏ\x8dѽɹnӬηˊɘ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '¿ÑĥӞςdќР\x8cϽ4ūʗϳǘϸćť,ʁǴgƚϵʓŞǾǴαв',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000858.050617:+0000',
                                                                            '20210413:000858.067804:+0000',
                                                                            '20210413:000858.084893:+0000',
                                                                            '20210413:000858.100485:+0000',
                                                                            '20210413:000858.117329:+0000',
                                                                            '20210413:000858.134568:+0000',
                                                                            '20210413:000858.151231:+0000',
                                                                            '20210413:000858.168232:+0000',
                                                                            '20210413:000858.188348:+0000',
                                                                            '20210413:000858.205632:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'λλŒǉ2{ǕΑ\x89ɞƚ\x91Ā\x97˾¯Ƙ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -729510809319179786,
                                                                            -4551887382671641278,
                                                                            -1739329976879891524,
                                                                            -2747261889985525388,
                                                                            1894483479084675952,
                                                                            -1566474205859635889,
                                                                            8251889528491879583,
                                                                            -5759430423008864506,
                                                                            6769164426891510224,
                                                                            2945613103206893099,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȱŸ\u0382ӐхώƻǂȬĴʋȑʜďԙƐͶѺïȝÖϛЬϽȉϿδŨĐƊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϩȐCάҿƗWӪМΥЭ\x8d\xadȊЩǑӶɉʻÑ˂ŭTѣʌԌĳθЗĶ',
                    'message': '¾ΠӨө§ʃɗßǈɉѫʰƿѥҲ#źyŨsπҹɾвЦʘƀƃĜІ',
                    'arguments': [
                            {
                                        'name': 'ƥԮЪѥĉʢŜζьÝʋԥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000858.691514:+0000',
                                                                            '20210413:000858.708780:+0000',
                                                                            '20210413:000858.726065:+0000',
                                                                            '20210413:000858.746317:+0000',
                                                                            '20210413:000858.766543:+0000',
                                                                            '20210413:000858.788457:+0000',
                                                                            '20210413:000858.805689:+0000',
                                                                            '20210413:000858.822974:+0000',
                                                                            '20210413:000858.843884:+0000',
                                                                            '20210413:000858.866247:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʫԅŀҎǏCȝԘʡVшĬĳÓРÐ˅ҝÙý\u0380ʣŝԞЁˎԇ¾Ҡĳ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 739722.9564634615,
                                                    },
                                    },
                            {
                                        'name': 'Хҫĵ\x9f',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            568008.0276789849,
                                                                            883492.85043301,
                                                                            273942.0047681679,
                                                                            726755.1071501598,
                                                                            805605.6058700343,
                                                                            113575.97497017938,
                                                                            5359.960674848611,
                                                                            669757.8158991605,
                                                                            761336.5699214237,
                                                                            319533.72478835436,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ň°ɘƬɜƀȒϟȣΰǆɃ¹ζ\x85ѰȔ{\x9cϦц˘ɇΐЛʹÜΟԐ\x8c',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ԐԭǣņӔ\u0379аήǒ͵ŝǙ\x86ΆŬίÏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            329262.6641321941,
                                                                            140236.2791057969,
                                                                            779885.9430240052,
                                                                            568204.8670774747,
                                                                            -61317.87148238703,
                                                                            244481.84827011375,
                                                                            3108.225063296748,
                                                                            50545.19312196743,
                                                                            795129.2351964047,
                                                                            482867.4219289243,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'á',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5077673612288585760,
                                                                            2918672625049712707,
                                                                            -7169649963953535079,
                                                                            288501469301539926,
                                                                            8169480146353431200,
                                                                            4529580074431782494,
                                                                            -4390423039893061837,
                                                                            7759204232955987725,
                                                                            7315783953296538468,
                                                                            3435688450693126242,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҲȋмѯƕɗƬӁƴҖҷȈɇŶϬǰ\x88˟ő+ѱљӣǳɭЋͳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000900.058628:+0000',
                                                                            '20210413:000900.075531:+0000',
                                                                            '20210413:000900.093245:+0000',
                                                                            '20210413:000900.110289:+0000',
                                                                            '20210413:000900.219924:+0000',
                                                                            '20210413:000900.236610:+0000',
                                                                            '20210413:000900.253804:+0000',
                                                                            '20210413:000900.267469:+0000',
                                                                            '20210413:000900.283367:+0000',
                                                                            '20210413:000900.298670:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȿȃDғá˻τĀòȂȽʇƨԥƼӳƳE҃[ɶԣԓӡȶǎ\x87Ϲǳ\x9e',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1709607216670322444,
                                                    },
                                    },
                            {
                                        'name': 'Ϸǰžȗ϶˘ӹoʠơȌʹ˨©ώÜ±µЈщǞѣ˟1ɪʂɒʄ\x92˘',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            450931.82431472803,
                                                                            -50119.326410920105,
                                                                            567806.7631551967,
                                                                            140953.0422224634,
                                                                            63041.68077428188,
                                                                            326868.29136344616,
                                                                            496105.12112638133,
                                                                            850738.0083157828,
                                                                            535161.523223264,
                                                                            -81451.8533561095,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǭÏȋ\x93/ˣѢɰmƂǁ˭ʰáʎɧŶJԥӹѴq΄Ҷ\x83æǅȴʂҰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɔɜƕҝԛŷіº*ӏ˵ŏԓТДҪϮëŮcƄвЍԜΚɉɝЅċʬ',
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

            'identifier': 'шWӹŅ%',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'ѭK',
                    'message': 'ɶ',
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
            'name': 'ʼОɦʘ5\x9cĴ ьφȟГƩíúʼǹĄǬνѡ˘ğōÛHӤӫŀ9',
            'error': {
                'identifier': 'r˩ǹŚӆ\x8dѩĈӳдƷĆԄԐĵǄ\x9bȸέˌƼ\u0380ǏϼͷǎӪğϏs',
                'categories': [
                    'invalid-user-action',
                    'invalid-user-action',
                    'file',
                    'configuration',
                    'os',
                    'configuration',
                    'file',
                    'network',
                    'os',
                    'network',
                ],
                'source': 'ϒ`ԂƧǗĊÜɏ҃`δąӦЎƯ\x8aɟşǍʎΗωИ1ȑũȸɋƨҁ',
                'messages': [
                    {
                            'catalog': 'ƂïɞǷФăͳ\u03a2Їʽή²ǨǦʬЭ\x8cƂђʠӵ\x8bͿ˄¸ϠˈȲͻѶ',
                            'message': 'Ї¢бʠЭўţΞΣõԨͽͿȌJƣԔɾϸодpИŜǨӢБŗԀΊ',
                            'arguments': [
                                        {
                                                        'name': 'ĵ\x9aʯŭёˤǲyÊʳǰŗφϩİƋ!\x9aǪKğӧϫƸ˞҈\x91ԘȪѭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1679153573595301675,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϣŧǌϣ҆ę¹ɔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȄӚʨƓŸРЕӂɡǘȑ\x9bѝÐVʚѢӜĿ¡ӧɫʉČƙˏÐϰɈϫ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦƴ˃ѤΏ¹ϯ˛ӳǥөԞȋŭ\x87Ш#ɩáŌĊ\u0379Ϻǲѥɸĭ˴Ŭƽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΚūΊkƭҡ˷юҢЇҜĉϚЕþΙʹӈӅσЀɆw҇ӽŷƗӤųɑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉ\u0381\x9eĠκӰǂΈʘӚПӽҢŁǮÇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7257523589262582627,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ξӏ$ӭ\x80ҤӈÅʿԫʓːɾϣʮƜÏ\u0381йǁāҵљ-ϊƭӴƆʂҮ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȱŶǗƦ$˜ѓкƚƆϘʘɅȇƸӽЀԥ˼ԠȉČúDʛǞĮʯѦ~',
                                                                        },
                                                    },
                                        {
                                                        'name': '¦ѧǳxʇ¬ȁ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3431179513702859959,
                                                                        },
                                                    },
                                        {
                                                        'name': '5',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 406761.57196555176,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћɏʘƪԝњʉ\u038bТͲϠ˚ȿҀɰКʥúÚʣʀШǺˆƠ\x95',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӻйΠQÛ¢1ѧͽÕƻʅŧΊЊɞшǍ/íΧɥüɕūȭƠķ:Ӱ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 638535.3060202027,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '$`ǉӏӓĤjȾĭÓȯʚ˵NƎ҈',
                            'message': '˪ʧěĮԜʟ¡҈¯нɻϷӅ\x9dÒҴԥӋȚ\x85˂ΑLˮÒ˹ΊƜ҅ˣ',
                            'arguments': [
                                        {
                                                        'name': 'үԬҲȞƞǷxҊɵдϔΘɨ!ő¼ƇϋΛKιԏŧPΕХ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΧɤƜҖ˅ŮpɷπӕЌБǊ˚ӻßԈƃŮȁɽșȤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˨˱9˂žҨҤҳқÐd\x9fϹΙȨ!ňϡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵ˳БʷӬŀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Åɛɾ\xa0ѦǧӷиҖȅ¡ȴȲəĕħqМΣʔɭӛҤɹӯ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '͵ϒƃ˔ɁԤȷ5\xadɉΝƇ\u0380ӒԈ#ΜȤǹˌÝșàȄʞ_ĂЊ҆Ǩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋҋÿϩΉӰ\u0381ːțï˴ˈ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Дǭʐԟ¦жѵȰ\u038d˭σҡǪɰʨǾƟνӂщ¡šʋʖӛQɶǄÿԈ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '©ĊˮŻ\x8cŐɓ]!ҡˠƝǠ8ї²ϝÛJæĝҮτƁѸɥKǞɘǛ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼϠЂĻĎýҝϐˤ\x99ƞǢѰŰӭƼǬ\x97ЅѠϝͳаèȸĤ§Ėŝӵ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɝȽθǂȎϐʲÌmҐ\u0379ĸϾƌжҙǴɦŨˡѰ\x9fĩȡéɪЧмϫӹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȟ˥*§\x82ɡȿƚ¥с5įшԈҽʷŇӍ9Ѽ˼ǅǓнӾжĭ[e',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǀΩԭʷoçПϡϘҤҺѴ\x9dɃӔƛɀwƦÝԎƣЫғȧƝˈɵ˺ɹ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'àƞʏΤÉҭƆ˒¦ƠҬт<>ɀгXҫăѭǒʴӱ\u038dӐӚ\x83ˮĿǌ',
                            'message': '\u0381ɒͼɡӆϫɞԅMɍƨԃ9Ə҄āũ˝ΤΈģ#Ӎ˜Ρ˒ӮƄĠӹ',
                            'arguments': [
                                        {
                                                        'name': 'ίɆҦǶӢƔӬϚâǆp\x93Њ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '҂ǜʂϳЬͲĞʧǹλˉʎß¬ҤǢѭқʗΜѽΨ˨Ŷĕ˳ˢ0˝ǅ',
                                                                        },
                                                    },
                                        {
                                                        'name': '±Yɖȭ¡·ʑðѭҸҌΥǚ˽˱EɔҏǵџЫȮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1093000556451117875,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Y˜\x8bďǅɵБğҷѸѭǺɻҠȃҀ~ӏхпҔ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000844.995157:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʓ\x81 ӴsΓˉɹǛԥӲŏ\x92ɛĺʍŴ˪˔ĲφρœÖʵɇЁλӇŝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6213449214310014796,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƣӋÉαȮiͲŽӎЌ{ʪƼΚĹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔóEМӒΨ˒˷ОӬ¢ы˦хƝƠŎԧϚθѰȈϞҡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑϏĢԥμáʖÝUϙεſŉƘ͵Ō\x9d˜ѕʻ˫іǼǠÍІϿǭʴӥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹΠŌďʧ Ú˝ӽōȆƮ\x97ТϋƘȮ˅мSҬБdΊÝäŝqѡ˅',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѹǨ ?ǦЁМÚɀԡô˪®ӲқРŖ\x98ԭΑ«ϸηŰҺǺӢȍoЕ',
                                                                        },
                                                    },
                                        {
                                                        'name': '7ʿҥ\x87ҥʠϑɔʇ\x88ɋýϫѫρƊЌϏ˟ԥġ\u038dăÀӔÆûь˓΄',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2573033637189396830,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĴˎȚĨÐĵǞ\x82ήӁɩİ\\\x85λζ˸ρϟ\x8f=ЬτӦįάÒҏӲҡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000845.637873:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǵȕÖԬҪҩǹӱÃ·ʕ\x80Γ½ƽϸӝò+ʱѭќĐʇЋЎӰʏ\x9dą',
                            'message': 'ʭ˟ҾɌ˹ʞ\x9cѪ\u03a2÷-ĩńɐӴǻχ·Ϥ\x90İ¿ċůΐӭśóν¡',
                            'arguments': [
                                        {
                                                        'name': 'Ϲ½ƯқƜϏ\u038bŎÖïѐӇĘʁȎϹφʚӼÔХ-ĹСҳЙҢӞl\x85',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2606445887848766071,
                                                                        },
                                                    },
                                        {
                                                        'name': '¦θČŇȇΔέƥђ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺʰćӻнѩĥÕĨûÑÔүɾͷůаˢ˶ҘфĥʻĚƌЋÞ`\x96\x98',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4618287497642039149,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÝƢѱі˃ņĶԙíʇʙшÎĊѭеȭȡĒӃҥю¯ǟЋаǁżǛϸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000846.003330:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ъ˪Ō\x92˗ŕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000846.073119:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Τŕϧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'УʇԖȪцǀ΅ҳ\x8aаģĢɷĦ-҃˒ǫџǇ\x7fϿ8Ŕє\x9a«lBс',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĥϊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌ¢йȔ¹ˏéȮ҅΅\x8f°Ü´ԮǓ˵ťӅ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'м',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˼ѺǤғȼľˈĽԆçĻƇŴ¥АƄǮ˹\x80žϚƻ˓ŵšųˆȦȳÂ',
                            'message': 'ņrЧſhĤӼʡЛđαϸҸ±ŝƒÇӬϺήėӀğ΅ɟċĐǧƉÒ',
                            'arguments': [
                                        {
                                                        'name': 'úԓƬΡѾɞбŷЂ/ÊȺŞKϷһǌĎɃŔʵ˰ӷ9§^ßϮǝƈ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѱ=Ѩ*ȼӯ\x86ðɬɰʟʽҘĎƕҪ4Щȉӯ˨ţӶĥÍϜŉ\x88ӡʇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -9069587774494775801,
                                                                        },
                                                    },
                                        {
                                                        'name': 'АöԄȮѸƧϯ¯Бǳʌ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Jû\u0380ЧҝȫѺɹ\u038bQʒĨҍγȦϻΚ˼ЋƔÚĦʛƦƚÿÀŦӝs',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000846.908846:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝȼ\x88ĦԬƏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɿȷ\x84Ȏ˴\x83ъȦŏĴӊͲҍџԩ҃öŊKǣ:ы¹ŜҠĚҍ7сӧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇˢ(ѯĉŃɩɩϐцˍΔʜкX',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƿ±ԋӜ8¸ԗԅíʌ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȝɩ;Ȳ ҥ\x84ȉƕѬŨѕôĘǅªАѴɢҲ\x96ШЕԥˡЖŐԔЙν',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӵɘ˼ӑBďҞƀáʃŵɱʾ\u038büҔʢιΐҷ?ʟӣǸ˭яȒŀǦŨ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȍɂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƩëȨÏũԖÝmϽф\x80ӦԢ¾λșąіŏ\x80×ŷƗŭąřˌ˱ʦU',
                            'message': '\u03a2/ĸǯƹ˟ȮӏǙſ\x84ϢǫƘǯ˘Ҡˋҫ\x82ЬźņԬ/Þԍɳӝώ',
                            'arguments': [
                                        {
                                                        'name': 'ƣāʱΗĹΞɬτóҫкοʮȸǗȒǧIå¶ϭŒ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѝÝ-РǢťΠƧ¯Ԉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥĐSңǝˍчͱȷ\x92Ø´үęȴĄĮɝғȭҽĠSŗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵÌȹˈ×ϑȊɔhЬėɇтǢǾӜGÝʤәŎИҀ~κϢɖѰкÕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 421440.4831567658,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӈͽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÁÛɼӴȉҪΠԬцŖʷ$şбҝ¸ԭƿ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¹ƑȱƇÀоԠԭ˖ӈ˹»;ΠƣȖԋ>ŇӠƵУлǴ\u0383ѳɯ˱εk',
                                                                        },
                                                    },
                                        {
                                                        'name': 'śEɍǵ˟ƙЙіɃʄŠô»Х*żϩoǴ·Įфєњȱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'гϹĦһɏΎĩ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЮǛǟв˂®QǬΌĞɪУȑԑҥʲФҀǇҩƔǏЫ҈˃ϐĞҺϑӗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3339879598307445933,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾǶ;ʌ&ŭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ʉ˸ϡƝΗƻϘ¨ƀЂΜϧʀʏΌƺɵ¨LĿÞπѭɋNTɏӉ\x94\x9f',
                            'message': 'БſыѺƔĆΞȧˠѓʳʈǻѳŤŊ´1Ԉӂҥƨƨбưǽ\u0383ЮŤ¸',
                            'arguments': [
                                        {
                                                        'name': 'ƨφ¿',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 836604.3057932006,
                                                                        },
                                                    },
                                        {
                                                        'name': 'НȈ;һÇͶtˏϷˁϲ\\ƾϗ[ĦÙˌκȃ˕ʗ]ӾɊьЧÈίъ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʫΨѳӲƵӄҟȑŜŻъɊӳȐӼӼYȾÕϬǢέčΖЁ \x9a\x9dФç',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȔÓӷŕ:ѶģѴȥϝÍҔʂƟÄLǭŁǣĽĢдFӋϮ˳ı\x98қȜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҏĠϙ?ʐдρɇ{˟ŧ·Ƶč˵',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉ%жɥȦѠ]Ȟ¶ψÚǂ¹ΟҺȍϢŜʸёłAδͺɁʡêƩǩҳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 530997.4121975406,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĶxǘOϲӲξЗϬҹ³ʫŅ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7318378997287913397,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΑʿʯґҚßɾǶӥԐ˸!ǂĪͳϵԅT˛ȹǌqЎɒˌɉɠȭҁϸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 871150.418445629,
                                                                        },
                                                    },
                                        {
                                                        'name': '!Шąυ´э¢\x99¹Ą\x94¦\x8fȨǖƫµ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѮӚȈ\x99WΆƍǁѠ˘Њѱ<ҫ΄ƊЖѨĐҨʩË',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -340124494169185932,
                                                                        },
                                                    },
                                        {
                                                        'name': 'шįëΜЁ˓ǅ®ʩϠҷˏѳɰǦͱЏ«',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000848.849534:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ìŲ˒ΡɳűҿεÝтƈ˳Ӧн%ҀʤɮVťx(ĩĺяĲò1ÅҘ',
                            'message': 'кƓtƼĽкƺÏλʇǵ<ӰȑȣӷԨĚŊɀŎēȎǿ\u0382o˩Ȳóɓ',
                            'arguments': [
                                        {
                                                        'name': 'ǘ˛ŏƭәʝҹƑɘĸɃŤԐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϩӰƝϮ҉ǠÃԉǘǔԖԪҡÕςδżϯӶʍƛo½sĻ˘ȶǚͳϱ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9eȴǆԝçƽƒ=lʿτɂȟҕðІяe',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 265839.3731922798,
                                                                        },
                                                    },
                                        {
                                                        'name': '>ӈʽÇ²ˆ5ūѳ˳ˬΐǇУ¸m&˓ŧНĸҬԜƋˉėʝϙɼĆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕYκˍ\x9bȳə¼ӮĂÝ@e¬βѶ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˄žБƒ}ɮÔКɒƅӼѥТƺȭȏǡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΏΟƑʚϤ\x8eéSѕУӣżĿɕӭˑƜȚҘÖѻǗҋȔŉħǿNʾħ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ű¶\x808ÃʿʛIːĬßƉʿʉ4¦äƌʚʫ}Ήʐͱʣ½',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 887475.0209781667,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ôӎ˴ĊӡŻƆιǎԆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҢˀɌƒӅĚϧс˝ҩĭÀš\x92Ͻϸё˳˱ϟΑƒ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'òɆǼЃϱR',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÞĥѵəĥǡөўҠҒԓсȽɳόǚ©ȈΧуÍϲрƅ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʻŠʇвĴ\x94ǲюȬÁƝԮϻnˮρ,ȲǘƇ˅ÆȇЅμȕǸȩ£õ',
                            'message': '\x9eïКϾѡԃŝȰҁɕːɂɶӀΟԬŀϹϛҢƂɋЖδȈÓ˞ɞϤӉ',
                            'arguments': [
                                        {
                                                        'name': 'ƯɎЧɍӉԀəˮÙÌӸѳӦɍƹмűϗάΐцлϏðăɾƚİύќ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '3АĤ:Ͳɱa\x8aŚҢ҇ήĢ«ʵЈӚʾ&',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍ\x7fʬҌϏĎĽВӏԁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǐǈ˾ɢҫҡȮϵҲ˓ćŹѾǕффЊFŧ\x9b\x9b·ĲѪΞȭ˪\x95οF',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒŐȋѲԄӅȖȔǾÏҪřˆ\x80þԍ˵ʊʳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϡ¥ϟʋϫѲǓоԬӭϝá¦ԠİІØóρѫЩȅҺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000850.019045:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ş;ƀÓʫǈǙΎË҉ЙЅϮĔɕӵђȿGƱѦ\u0382οШɸƈɬǤѲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'цĵυ,ʂʊÖԚԃњƿ˭ӁʈҧˆԊĝϽӡ΄гě\x8dēĆ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 464336.46144800214,
                                                                        },
                                                    },
                                        {
                                                        'name': "ƕȼĔʅȪ'ӗҳκͿǳӈˤӘÑĶќɚɻľSŅDƝƛƹƧƺƿȲ",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6068924428874067862,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҵ,\x8bΠɓҼȬŌϩǡѺӂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƗʇǘɱǩîKɍɼ4ģíԍ\x82ʨɍѕΦϭ\x92˽*òҒʤҊӬȍчʞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɔϥƢҁʃAȌϞƤ\x96ѫˑˊăĳӚЄʩĒȇÚɆşӱģƦǕ¦ãў',
                            'message': '(ԔϬԞ˜įϿ»ͷŮ(ǸŃŃȷԣǙԙʅƟ#ZаӻǅʶƟԪνǕ',
                            'arguments': [
                                        {
                                                        'name': 'ӳάӐмӯâªӂ1!Ϡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'űɻǕȰ¡Ț\x84¤Әöġʖɜ˦ҶԕѻąδΐȤӞʎżǫǈÆеϔȌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĸ҉ϐƦ˾ǜ\x81wĥǝЛЊѣǦɬŨˮʠψ\x8fȎëеĩŢ˹ŤȼʚӋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩКӝĂӺԗΏǰƄђϿrūǋöϞΥʀΦǪȺҰ}ʜéɧԀ˹ɩς',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉьЯċʹFυȹſ˵\u0383ƹΔƈʫȱҒǵ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΜǑќҨԫƙǒ\x80ЩȕҔâ˺ÆӧЀς҃zȯƓCϹÌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȡůȡӡǼəũԒRƹ\x9eá˽\x84ĉѽӄӦϑʢͲĀэŉ\u0382ʁюųѠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʺƵʴϋЃƸǝ˱ȠͱɂύͰҊϘӢȩϯˎȒțɻαдԋĤWԕІȉ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɗĠǰpɺʳ·ǎϞĚQ°\u0383ɫƍlϠΪɬҸ˒ƖɇӁɸ\x82hĲĉϤ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000850.954187:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˆŀĿÎȦŐȖћǯˀſғƭӵþӋцƾɼȟΈԅǚʮGγeƏқӨ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʙҪÖňԣәѷ5Уƽ?í+ҌǱǲŏǇoıԭƠԒǧϺĽ˱åϡˋ',
                                                                        },
                                                    },
                                        {
                                                        'name': "Ѭ'ȒʏӡʌŲωơȃ\x8b´ύëϚлȿ\u0380ȌWơіƷǶÉʹ˙Ȁ\u0380ɳ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĲҧхȒʤĄɖσԟηϪǊȳÎˑǑǫΪКӷːȔVƕPΦ˙\x8bêʶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000851.166394:+0000',
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

            'name': '͵ăğ',

            'error': {
                'identifier': 'ϯΉЬҍά',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': '-ʁ',
                            'message': 'ǽ',
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
            'event_id': 'Ԕԗ×ġ6ǃ˜ŸАϒōƎӘӄѦύӏМŴѵӆȫѼʥƂ΄Ӝңțc',
            'target_id': 'TɨąΞ˵ЉϤøƎϱŉôˉґžc\x8ckºMɓԪӗƆ\x8fƢɗƩťн',
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
                    'event_id': 'Ǭèƙ҈ϿѶӅãØτΐŚɸ£\x9aҚΉˁӾѪTƅЯǈԜЇӖȮԀŶ',
                    'target_id': 'ԏğÉł\x97\x96ŊƙăȤ\x8cӿҺщōpԗΰΤԤӞƃ<Ӿԃµӿǒϱü',
                },
                {
                    'event_id': 'Ӓ¨Ͽi³œҒΐȸfƼºÔÿɨӭ©ąɗзӸș{ӘŝɬѮ;ŹȦ',
                    'target_id': 'ȥ\x8eȶ˔ʠѪȓ"ҎͶ\u038bјҼӎΉʆԛÆȊĬѤʣʬɯͳÓĆј˰Ӄ',
                },
                {
                    'event_id': 'Aǧȯу»˝ơ\u038dϋıæʡȪеżſɺϏȧҵåĽδϹżԥȁǹ\x93ӽ',
                    'target_id': '˫Ȅ\u03a2ϏȘΎμыǲ˸ȡôƽϴĨȍб҇Ċ\x90\x9fӤԕϠ҂ѷƨǵϓń',
                },
                {
                    'event_id': 'ǡ˨ȂӔłĜΒ~ӝƴҵћ\x84ĬϬɿάԉaʴȶŝʴ\u03a2ъϓҲûĦǳ',
                    'target_id': 'ȤôѻÖȍʐÞғƨƗɁΰrŚÏ˃śȪÔċΔƩəϿ˯ԭӔËͻ\x96',
                },
                {
                    'event_id': 'żӬӇPԮǁџϟҹǘы\u038bϏʽζέʇĿ\u0378ƻӍҩΎґĀŹЙǡŎˤ',
                    'target_id': 'ǄЌӕGȃѣЈɫҎí÷1ǔwȹɲПıþ҇ˮНя˔ϟʯ\x8cфĐə',
                },
                {
                    'event_id': 'ѻǒȚЛԠǈаFςӱȃԭβŔҡ˲ƩюΞrȪӫʚňнƅеŇĄɠ',
                    'target_id': 'УҨÛӼÀɜфǬȫƆʙǀѧӈʈԘĒºMԥˏgӓӢĩόƮ4\u038dɁ',
                },
                {
                    'event_id': 'ԝ7Ò-Ѫ˥ҷƢȗϭӘ˙ĚͿɾƥǖӉΌǖԨŰΪ2ô˛ȈѼͶƮ',
                    'target_id': 'ϋíħ˅\x83΄ҧǰЗС£ӛǖȳԅǃΧĊӘҥ˳ӜʒŰ҃҈ƤͻϻǸ',
                },
                {
                    'event_id': 'ëɩΚ)Ȳőǁϫ\x96\x8eϐ˜Ͽ҈ӜүʥÕԪȄӃͷʞƌƲҲδhŔȘ',
                    'target_id': 'ťàҧúңҖгѦʣǼȴǙϡɨӵΩ;ǌqπѥҕȌ®ǰµԚɷñƥ',
                },
                {
                    'event_id': 'ÓωϓǀɬɑӛŢ\x8cʄ*',
                    'target_id': '˧ćƸϋˇπ\x8b¯ºӆÏŹȷŭƝù˵Ǿ6ЉàϺʌӞƁϒµɩ¸ʱ',
                },
                {
                    'event_id': 'ɉ%ѨʍŸƹȚȇϣ²ДԁƖиǿА˲νÑʞ?Ƕ\x817ȞҾĘ˃Σ˄',
                    'target_id': 'Ԗˋʌ҂ΓĪ\x94ЗƁƣУҋȗȌ˧δѧԉ˨ЬԉøÈ,ʏԍϑςҼ¢',
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
                    'event_id': '/Ԏ\u0383.ǢλďҾuĭȱϧãMƻȄHǪƕǈӾԒľȀŨԑԐ\u03a2ˈӎ',
                    'target_id': 'W˶ȓӎ?ˉǡʯӥțϲґǏеɔԐvɶӊŕÆϓДȻϸ¬ʰɝˉȧ',
                },
                {
                    'event_id': 'ѾЀƿӡЃʨКβʤӧΟđѸѪʴԀǕεªʩýеӔɄ˔Ѳǎʹςˁ',
                    'target_id': '£)Ҙѷˋ\x83´˱ĘɒИΛrŤг\x88Ǻʉ˄VHˆ\x9f8ʸ˚ƴˣʰƸ',
                },
                {
                    'event_id': 'ѓҷȈнFϲƆνY\x90DĶϕɏʷѸćӕÆlŇԝą)˙ʡҝӪĖ\x8e',
                    'target_id': 'ǽ»ѭ˃\x8eҵȪӥҳѐґϬ ЂǸŬѸ\x8d҆ÀӇÉ¯¯ Ԭşԛ)ɮ',
                },
                {
                    'event_id': 'ʱĻǿҮϟͿҫ|w\x9fԍ\x8d҇ѩ˘ΩɆȗƙƒҢм¯ӣӟɹκѝ¨Η',
                    'target_id': 'ʹµÿËaαZ·ǞΝǳԊÓ£ĻϯȏҳɞӌԠċϗőƙ¬êɕʜƭ',
                },
                {
                    'event_id': 'ƊЌҿƉɧѬɶƾ9ѤĽȽЮйƮǕ-ͼȃśñƅԃ«ŤԊӫϼЉ˳',
                    'target_id': 'æưԑeȿãū\x8eƺϤƗжˍӵĉԎΦʫл\x9d϶˸ĈӂҨơԧлԉҴ',
                },
                {
                    'event_id': 'Ļ»ʂЯКƤӅҌŔ\u0378άǺŮɟӕԁјϏ\x92ɭǱǈoԧíϕɜŗǯŅ',
                    'target_id': '˱ԛԔϬsϣǯдɲЧөčʰȲйƫͳӑρɋĆáРӬç҂ӑϹǜʬ',
                },
                {
                    'event_id': 'ӄ\x8aңČǷЩя˩ԑĝΡȇоЂɎϪƤӄŃ\u0378ȧȪˍvʔΘί®\x8aΚ',
                    'target_id': 'ǘʡҎpɔӞɬӫΞkǅȳȴȚĐƺɤԫʤƛÆпȏԛʐˇӄÒŜʑ',
                },
                {
                    'event_id': 'νҥǰ҄ɬѢѥԮɻ"ʩεΨ\u0382ǭ`Ӟͳ¬QҸѷʳ¬ɻϮǮӲɬс',
                    'target_id': 'ǘҷЁӤǙ˸ˆ',
                },
                {
                    'event_id': 'ǏМЃ\x8cŲѴ¸ĜǶӬ>ȌİũŊʯˮĽΌʒͻӸԤɹēĵw˵Ѻɺ',
                    'target_id': '\x81ċ\x7fлǵƏҚЩЈРǣҾѳ˙˅Ĺ=źԟ_ԤΊǊ˃ʡʯԌ:ŶȰ',
                },
                {
                    'event_id': '˼\x8aȜʨҿӷūwˬɾȻa˲ĹӧɬԛƵ.\x8aԮԅǻԟʗTŶÎΗ˂',
                    'target_id': 'ϊɪȻìѭÛϺ˃ÅȩѰ9ϋȥƳǓɭϧΎ˥ǓýăŦІʍϽƔНϗ',
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
