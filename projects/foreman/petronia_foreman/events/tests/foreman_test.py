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
                'ÜЯāǸшѡȱŰъ\x90ӖӮѨʦĽ¤ŀʡĞβϲϾҤˑΜęӗʎԗͶ',
                'ҸӑŦΡʦ¬ʊѐϤЏĽ҅íǦɽҝǻȺүΟƦϳȎфѣΈƆҪȜ҇',
                "҉VÎ`\x9b˫Ȕʍøɼ\x8fӘԉӔȌљˠöѴÖʿΪ'Иʧϛàӊιϋ",
                'ȌΠƬǄɒȇXыƒƨ҆ŮűΔϱ(μлѳĠ\x88ʐЋ\x9b',
                'ʜÇʚŞǔ\x97Ʒ;ǓӼӃҾΤƪϽzǠÿ!ōΙǄӮǹϺȟ˱ͶΕ҉',
                'zŤӨȁҭȟǎ\u0379\x9d΅ƅ˱F\x93ɀȦ҅¿ƟЖȞʰҼФŘŽѺαҮө',
                'ńΖϘ\x86цNˢѐԢ\x83ӾΔJʐÉ([¶Ьɐ\u0382ӗʅŉɥƽɲǝW˩',
                'ƀʿȡɹΰʚ˨\u038dԀɛȢǚļōгΤ',
                'Йϩʑ΅ΎШ\u0380\x9eЊɍӦʭМǓЪ·BеƲЂ1m҄įĮĠϑѦȟϕ',
                'ȃǓьϔƱ¨Ҝ@ӮΙʒŁ\x99>ƄɛуÓѲϣƉэ³Υ$ȀǠǠέɛ',
            ],
            'source_id_prefixes': [
                'UƎ\x8cÄβƯԔӷѠѻмƱ\x85oӏєνǀɤź\u0382ȫŋĐҢńùąȏȖ',
                'ɤT×ȻϤʧӥϷέ;ȀÀӰʿèâрŠɬƠ˻čˤѶɶғюԨ6ù',
                ';Ϝѝʀƺ\x8aΡɎФɥk²ËďĴԔƦɄą˼ʅѤˇ/ȵΊΠȓĳѮ',
                'ÓõŦ¢Ǉ\x91ɩüȼӺд,3ĤИʿɭȉ\x87\xadҰʮѱȆr[ɚҪŷÌ',
                'ĵ¨ƊʊͶҮüăЪˋʫŕƻ£ԨɆȤзʒĞԐÓǌ\x85ͲҸǴσŕӕ',
                'ѦΪϐÓƈѕǽԅеƓӢҕɘùĂżdʃϸģуȫΚ\u0379Ƶʆ³Ҕĉˈ',
                'Ŗȗԓӻƣϟʝ]Ӊ×ǔÝ\u0381ēϑʱњțӷυ˧ƺČűʢыԙɘϿğ',
                'Ҩ;Ҍ\x82Ҧʓ7\x88ʟӲ"ɱϾσҬˮȑ˴я\x8aФŻʵѰ?ȑ9ʔΤи',
                'ѵʓɰ\x96ҸԞ]¹ԝɻл\u038dѲĿɑuȜƶЉоΨǨ˺û\x91AĩҤ*Ǌ',
                'ȺЎºԕƯțŖɷԆɤѐÿԇōӫ»ϔƘжʇɎ¡υҨʽ\x84©ѰҼϤ',
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
            'action': 'έʢɏbӗĄͿиѷǕŜńҽϡńҜǢƉȘЩǽɾúǂ\x8dƂӑ~ɞ8',
            'resources': [
                'ĲÑήʅ¦ЈǖϮ:xȬȵʈʀœǡʇƟéӴş}ȱλ\x8dµBόĿұ',
                'ļÔΨưȤϼtʽѴǘUʒÅрɽñȷlʝʇɩԃϕȞĕӵɼЧȖǬ',
                'ͽɪýɤЖПϔɠʎʑʛĲԅҜʶĨѷĪǗ\x80әу˞ϖŖĩˢÊȪˑ',
                'ĞȷҔ0ЯrǒӵϿ@ͷ^нԫӻàϜӜԢӱԇԁ.ʍC҇ŚƳËª',
                '˱\x92ӊԨҪʘҫŢļʓ˰ĺѲԒϰˊĠsă$ѐɲýһéõÀѪӐȾ',
                'āлé\u03a2нӲȟɿ\xadϒHɽеӣƑɥǘА]őî0ĭȎͺˁЅΪƿƓ',
                'πƐΫɩǰ©ӭЦ8тJįϢTϷԗȹ\x92ũɆұ˴Ĭԓń\x83ƙʉǎҍ',
                'źȾ\u038bËΚβȊŝћ·ǍҩԧбΣÃɶ˪ғ҂ːʰƙȍЄCˆɐǺş',
                'ʄȄШѨ4ĜҶД˄ρРѵNěөˤоtʆ³˥iăĕѐԒɚǜ\x89Ø',
                '$ΥlȧА´ɀȲοư9ǃΡҨġљēͶʙÍΥĖŞѫɉú7Ǧӄť',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ļ',

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
            'name': 'ŢΤʃǃͷӂԛ҄Ǫå!ʲŒʼÃȲѵӸȀÈљҽίγѾʲԫĪВЀ',
            'version': [
                -1628717815568276435,
                -5753106091670076278,
                -6233291926092626390,
            ],
            'location': [
                'ԖпƹƧê\u0380ƿ˨ȰˍʯɅSÅԕРЭ0ǬƺɃе\u0379ŻęΤϧʀʌË',
                'ԒђȭӺ҈ҿɐ}ːſʱʤ9\u0381Ʉ¼ȭľ\x92ӳɛıň4ԦʅǀʜǻϪ',
                "ƹȇǉ˳ˣϲ4Mī³Ͽ~Ӕӹ˾іØҞ\u0382'ΞɥιȃĬЇʟӪԖʗ",
                'ǍŴɁвȹmƙТėfѿgϟȠΕģѴʩƋƴśɥ,ΐϺ\x81ʚѿÖҝ',
                'ω¬ӱҍʻǼ\x94ϺɿԭГΝіƾӺ˟jȹɚϠeʨ\u0381ŮƪǵͻѬɬТ',
                'БτͶӃ×ǃ@ĉʗӆĹƪĶДþǕɕԕҢůԩƝ\x90ɉƆˋÆϽԁҌ',
                '˓ԣԈαОǓöЅȔɥȯƂхҬ҆ŝƑӑѢ3»ǽтԬЕΗNЪюͶ',
                'ΖϵΩȖɷ\x88ђԚXȔɉđɜ˲\x88˫҄ΔdȦѬǹΞѻԪŹČÏƸΘ',
                'ɁԚƎŔ\x85ʪӅҵLóśɛԦņλиǘ°ʴӷȄǰʙϡ\u0379ʊћʤɏů',
                'Ĺũ˄зѹúҜϝӥKȑͻϖɑˈӞϭè˘ΊñʛЫʘшȚ\x9aҋȱĝ',
            ],
            'runtime': 'ΑϾQӈҋǦǬěһƶÕɪϯЬάɲѧuЗˠ',
            'send_access': {
                'event_ids': [
                    'ÂǟУǾȬσĉȉїŬǕϹƥεόʥуȪθď϶:҈ϤǄƼВѪ˓ē',
                    'ýćъӤ8ǐӏϱҴʞĽТҮϼ˔ԆыȳӰƊiå3ȱ¥ǂåjȌX',
                    'ӳԈΆǳϔĮКˋƂӎǦȕƿŸѣάďǓĩΰͷÉέйʈ1ԟăĥŕ',
                    'tϢ¡ϡԬӻȿȹˠѾɣƽƏŦȶ?ĖВ×ϲӑăȭǴǛҔů',
                    'Ȋð×Ϧтý˻г=ʌɠ§ǊƉȘʦλɴСŒӐӅјŸĕ˔ΗȟäЍ',
                    '˾ďϨӆ˟ϝºťǁδ\x96ŃĺÌвԎ<ȱ҂ҀȺΰįů˾ЋŰƐɍǇ',
                    'ϿʑʙŊÑ-¯ʊъąʤ9Þӄҷʶԗ*ЬӬśӢĳӺ',
                    'ѯȄɱ\u038d\x8eЛò˯ȩΈԨ#ԏӶƣҩҭҁŘ\x8eŎϑ\x9fāǊɺѽſȾѩ',
                    'ɋǢʣҽԤÀʃǿ`ҽYЇºʯɃԬǹƘό˶˩ҳθπԅƙʎЋˆƽ',
                    'ʼХтԨƁΨӚҲѽÛƪϤʐŁƻΰĬ\x82ʠһКHɾӅΟǂʘѬńǡ',
                ],
                'source_id_prefixes': [
                    'ǐɁȍƳϺȤΩʖԫΚқҤbɹϳ˳ÏãјԗƲȟÜǷǺјԩ˲ǰĂ',
                    'ĀъíʍϋϯјӇĩʱʴμӌ\x9aȽõǲ<ɂƐʒauУͲӨԈϽƋu',
                    'ǖˊѫȇȶҗǥȽųiηшŖɟéŃɨĖǏѥȡ˨˓ũLѲȬҰԧɴ',
                    'sFǒѲϝϰ˧ǃǾĸǽǔ\x99ӧȵΙӳƔ',
                    'ȕΏøØџԝ5ĚĩЁϲ˒Ϗǣ˘ɞɞϺ˖ņόƥȞ\u0378ˢејϝ\u038bҮ',
                    'å҈ƠЭɄ˧ͱʲ ȬɴӾѭŘƫѾâù˺ȼȟòΎԡːșѪʌŌʀ',
                    'Ӓɡ7ƿ:ԫǑ³`ĆǱώŌŁƉ¦YŖcľȩѠЄӦ¶ī҉Ïб϶',
                    'φŜǢŋŴҰǩļrңȷ\x9bȯӠāҏԠ˹ˌҶɏÎƽǁƒ;Ȁ˾оƗ',
                    'ŋɧѭƷǧã³ŊĴ\x8fƣοȯĽƹǰʛ˗ɇʱ*ѥɤӅҳ®ҊҺɖĩ',
                    'Ө®ЩƐЈɉħģг\x90ȞęγǵəƪIŚ\x7fɤćǣщϮϝ҃нʦџч',
                ],
            },
            'configuration': '¥ǼЏƷ\u0378ƂȱǍΐȟӯƑђϳ·ҹOɧċ5˙Ļǻ#tқӄ:˼Ӑ',
            'permissions': [
                {
                    'action': 'ДӣȁzƲéŠʛԧџҾϩǜȀ6ұȽ˾İƦҞɹφȋγǍƝɶȯȁ',
                    'resources': [
                            'ԅЉPθvǹɩ|ơϔĪąǤу˼Ǳɤȡк\x9dцӲǩԐų϶˨˖ʦґ',
                            'ΧїTˏĢˎč҂ψԊęә˟ȫʿίИϼοÕҼȺɣ¨˳ņʯњδҮ',
                            'ȕ-ʬˊȑεːÁɃûɸі˧to?˪ѥɝυÓ÷\x93ԮϤѹΌφvˀ',
                            'ǓėζǄԮˤȮѾºЕѿԑǊɪǞӣÇĴèwѽҮӞòɡҎӸɫ\x86ƶ',
                            'ǧùԌɻʺƾӶΕЖӓĐĺǗaǅôśЖʩƦIЌŵ;CͳΑď\x87Ԗ',
                            'ÉˏʼԦŝ|ÜǇȾϡ˯7ПͻɩǊĨǂǊƟǌʤ³АӼȕÌӛжˢ',
                            'ԅɵ\x95ҁĪΉĸÁѵɃѦ˳ǰÏҢɑǶȴŸΌӟʷиǧǑәΌтcЂ',
                            'ŝԈiАǑȺˠĄ˒θțюūʆɿȍ\u0381ϘȠƩϥȘӀʪĀȵèԠшɷ',
                            'èɡĉǝǯΕ˸Ĉşʥ˝5Ǻ¾ɏǵžȱŲ˷¸ҎϵºʪӕӃŭћΧ',
                            'ӣˑԫŦτўЗԗƢҨÓпŕƼȫȫgŕʽ4ƒі˦юȒǁNLd}',
                        ],
                },
                {
                    'action': 'ņԅ˕ǖŘѼӇƭÆ\x82«Ϝ˸ŧДƛƹӀӗʏФņƕbǴʗɼƆϵϢ',
                    'resources': [
                            'Ȧ\u038dԭˏͺæІˡэųћԠAçҼʇɐȴӋϢИºû ȹåˌˑÓƗ',
                            'ʥ˵΅\x8cǇǠɑäэÈ\u03a2ѸΡͲԐː#ǺσΆɛƹkГƄȶ˾ӓƝ\x9d',
                            'źƋҶεˢƹО˛ǕƍþɵԘ¾ԑѩǂԆԥғюȾ\x96ĿDɷѠӌ˒˳',
                            'Ȟ\\ƕʕʟЧ"g˵ЕėƽɈģ/пĂΓФ\x9aԏŇV<\x7f\xadҊűǪӝ',
                            'ĿʠÐˍvī˫ύ\x99ӈη',
                            'ƚԪť҅«ÞƎҖŸɲԢ˘őPĎɤˁĳˏĻ˞ŕ8FҮӀӶŴ4ǹ',
                            'ԀƔƭ£Ŗûϯƈ}ЭѷЧƟŠϮŵϊȕӶěĒƕŀДύЭʫʇӿ\x8e',
                            'ȰėBWǆNϷ\x86ìŲӥȌӛʂϒʢɦіҷмōҭԝϥǖαɯơΣ\x85',
                            'ņ½ґ^ұͻԚŰͲȯƆŗщšƸpsKΙ¨Ȳʟ\x84ŀЗ˰ӗĭЍ҆',
                            'ǊƉHe2Ϲʈлʍ˅Ęǆ҆ŷɊ§ћӤīΟϨͰеΗШ&ʏbΓ$',
                        ],
                },
                {
                    'action': 'šgɃɂҳ\x86ʮїÿͻq~҆´ϐԠƓ/ҎÛΟʱǹԖȫǧĖùÇԭ',
                    'resources': [
                            'ҙШǷϻϖǴʒ÷ДǅΫ2҆ʇ˚ɄЃИτɄОԔĭҸ9«@ǗªɌ',
                            'ЏŜ(Ŝ]ʹɌÞѡӢ\u0379ƇϹÿʾUÒЌӅăĞҺҸƬ҇\u0379иɮɸ$',
                            'ʃɽçǡЭſǼǆҨΏƒщƠºʚƲ˦ѝʁуʍШ`Œƾ˯ŶwÙȜ',
                            'ԝǜҾрdӨŚδiϙ҆˺ʟğΞɽȺĚƒˁӃǎƽͷ_ƍϲŠϱ£',
                            'ʚůŷŋӬ˖ǈĄѕɵʺ҇ÄcɋƝ§ĀʽʺԮԘј¾ѕǚѫƒĤϘ',
                            '|ϵ\x8aɤɣXοЌmpģӈ/ʼϙdɷ\x8cʄ\x94ĨňԚϲʔԍ˝ʝȎĪ',
                            'ɾAȵ˱ЁԘŖʦѪĠѦѱҏԎðϜ.\u038bӇ<Ӧ˷ȦԌĜƲ)Ҧ\x93¹',
                            'ӈ>ƃɁO\x9dԛŜғ˯ĝϑF\x87"ǦҌľѨǱʼʉŪZʎάȘ\u0379ʡѤ',
                            '\x99ȪO\x84Ԕ"ЎŻӹĚˊңӸԆΡ(ЅҀБƹCώěýԦ\u0381˖Ʃњî',
                            'Ѷǩ\x81АŎ˺ǘ\x81γƉεΣƨˤɂʵ²ʛӺˮǟʂ˚ŁˢΔϦ2Ǫʜ',
                        ],
                },
                {
                    'action': 'ȈhΆκȦȈӝΓφȖŦԃŸýӷ\x95ŝˌˈ\x83ĦĻӱ\x9cƞȥȫǙōȗ',
                    'resources': [
                            'ȱɉŶʁҜѷȅԇοHĩЏшԪΪ;ė"ѲĶӼ\xad5Ϛҗ]ěҝԬȐ',
                            'ʩɤ˛ЈʍȡϥҜģȋïńӌªĪȀŤʯŉGϷϯϟԣƺŗǾҵ®˃',
                            '§ŗσÈ»ȓƹŵ\x8fȈȑÁԫ=вĉӇσƗŭ·ӈъΌΤτÐíǚʲ',
                            'еȤ҂ǵhȲԝ\x87ҿŨ"εњ˵ŤюǴƐ\x8aƲˁҘԣȉ_ɸȀ\u0380Ɍŝ',
                            '˕¦ǁɏѧơԧAĮɿԀԗɶЬKҕǽөӦŏwɂАƲĺÇȡė¨υ',
                            'ЏˆQƞѠʛ҈¤ƃ˨ǛͻʹΑѫϾ"Ѿīҗʐ[ƾϸaЬΫơƻʷ',
                            'ŽƛϰЬҨĢqʯłɩ\x99ʁΪϣ3ɍQӾƒӹʯLWΨҐˇŞš˓\x80',
                            'нą;ҲˁŇƇ@ŀ¦Ҡ°\u0382ˆΟ¬ѿCӃцǾϾиÁɋϞPЎŴɢ',
                            'ŘȒˤǗƏԢԒΒҙҭòµЈҩΥʡŵĜʆÊ\x87ѥƥ˾ĨŒԪBȁļ',
                            'їʽˑ&\x95ϨѮȲ',
                        ],
                },
                {
                    'action': 'ŁϠʹŉĨɲОͲ¥ШӢōγʨΣ#џǦΨͰɕʱ¼ɎƹɞʣԑϭƊ',
                    'resources': [
                            'ΤБΥ}ʰҔя\x9dĜǂϱȃ¹ƶʈџǉҊӫŢƷӖФʯ\xa0Ѭƀ·Ίǰ',
                            'ȉĳϞДμȰoˏοŎ˛ϥϲŃԅқĤĠԫHĽ˼кҽɁȁηͽΡŶ',
                            'ͼӑ·ŘѐǹĿǇźǄhжΫ˴ƽçЄñίҋʘҟÊÐϧã˒ƣCǰ',
                            'ŞĠҍѬūƿȐ2щĎɮ\x9e˷*ċƻƚÝԗΝǷ\x9dіJƁȿƅɣǵǆ',
                            'Í҈ǅг\u0382ԛ\x96˄úƿ\u0383ϙ҈ԦƟʀƶʓŽːηѦҋƊɣƎϗԑƭŭ',
                            '\x87\x8fςɑǀưƁϔ˲¨Ċϸ\x85ӊ\x83˫˻/ǱǝŖ˔ȟƦƐӾ\x86Иυ+',
                            'ІǗĪԓȖξˏ΅ɪ\x83ǻҔ·đǍ®фjѻŻӥ®\x9eƩéưϦѰƁ҆',
                            'ȚGˑҤʧь¹ԩТԆkÇgɺ˱ȡӳɥϸɲɦƕЏºЗδ\u0381ҡͱň',
                            'ȕƛĥ͵чԮԊēѪЃβЬȪǶɘƹɇͷԂąΘˤʴþZĳÀë\x93Ə',
                            'ɃωТґȐҥΒ ˣγҿїɳчӹžʤēǞȂ|ȧК҉Ő҄ӕǵZ¶',
                        ],
                },
                {
                    'action': 'ɳŜŠҭ!wyԊҦϸ¶ōˢ!ɥӗȓƥӗɕųԞ,Ѡʣѓ\x88ƂÂН',
                    'resources': [
                            'ԀӉйȬϭqӹ©ȹӖ@ŰƾˠÃϲҲϭкπIÊµѱƢϷǅǝ˫ɸ',
                            'ҲˊȺЗŊΡ˺иǅʄљ\xa0ШƸ\x8b˖/αͻҁҲÓΰçɴ˗IŻ΄Щ',
                            'Ӿĵ|.Ϙńɇҿˡӫʽ˙ФƊЅʞ®ʀМлϞńʶRϘϻǀʍĀȴ',
                            '\x7fԨśϝ˴ǏȮӡ*ϙǂˣӫ=ҙȀĹ_ÞҢ͵їѫ/ϰҰɭ&Ǖ˳',
                            'ҐҬҌ˦ϋѷĮąūϨŞìĳÊS)ƞϒӥąéƙǬɚξӰӡΈËē',
                            'ƌùɆĞʍҢǊʎ˺ƕƮїԭԡèşкæƳȧʎʗūЈˇÿ\x96ǝ\x80Ŝ',
                            '˴ŏȾǜӕüϤЉhIǐˡƹӲӯͰΡЌƻÂԠʅȠѯǴ˶φқżΠ',
                            'ѸДɧʱϘLȠˌƢ˲τ¤īҶ\x93ɡȿѫļԎвͿàϚЦϯ)ѭȵĲ',
                            'Ҩȼƣ}ӲѺ»ϐғԮ\x91ӃњƯԢύϼψĸ²ƐΪ\x9fǳԀͲʰʆǾˌ',
                            "ŰżƤјҶǇЎϟ¯ȭʼ\x97Ԧ7҇џŉѐʗĸҡѾ'ǃҴӟӱƧȃɑ",
                        ],
                },
                {
                    'action': 'ґ\x8aҭǌȹʋżͰǑϢɛҰŀúΗΡìύͱɻ4˳<ʃӦɖ²œƝˆ',
                    'resources': [
                            'ҀĐʒϽŚʂĶȕˊF·ȫ˼ЦӜȉƸèĚͻƪƲþȓǴϮѾƋċЄ',
                            'CɄ¸\x9cưһeʁӔźӄДϏƦÒ҇ȃљɫт˕ĒȜƻӇºñЈҀ\x89',
                            'ĠȆɻȱьХӳæŬûҹѻȔŶӧ\x94ϧfŲ҂ƲāÑϚ\x95ƆÐĭΧǯ',
                            'χɑѰ\u0379˪ǘĉƸβҔʓȲǵůȴѧǽ˙МζɿΧ>ҎόԤΣİȼһ',
                            'ΞϿâƝɩüɸћ/Ӳ\u0382ƽˈфΏȋɞˎθѼ@\x8cд|ȸɈѧ\x82Ęș',
                            'µ\x80ҶĈϚӍǦǠ\u0382ɬ¢͵4·πƑʳϔźQѯƕwĎӋ±lÆω»',
                            'ŭʽƛɈHÏ ]˝Ϛ:Йʞӄʰʿ\x9fԣŭДRҺ%ŷԩɽӔӼϛȊ',
                            'èǝDһ>әȵʧqѴǧыþǑȟGɝÊˁɩxɂЍ\x98ӋɋєԔ-Ћ',
                            "ėš˱ʝ'ҠúͺÇͰɸǲŪĠʅ5ǨʮϩɁŀ°øԑ\x88ȀǬǢƈҩ",
                            'ғûӉД\x8aΑЉÔÂҏˡǪŃқɜrиӑÖЏƫɢѯˬϔ˽τ˳ƢÆ',
                        ],
                },
                {
                    'action': 'ԙԜąьɂŘÑaѪˀӑƿԈˮэƓÑЮǟƭǴөϰԦӴ˙BҹșϢ',
                    'resources': [
                            'ҷԖԉƩÂȓɫǑЏĩʀȩȹԁʚǀҴкѻЪÚ҃җǿѧĦϜбӔç',
                            'ǟȃÃҴӗÝŰȁφ҃ƼÈȦȳҋ3Ǥƫ¡Ť˲XŧюɿƜЈÛϴ˷',
                            'ϩǇԪɄəɲ\u0378ʩªʍƿ±Ǥζ˦ǱϜԝǍxɟBː˝φȮʯϮδ_',
                            'ȍû˟ȉȐғΏïΘˬøƻ\x91\u03a2\x9bòʏӥ҇ǟƮťĹƜ?ЗӾωѸɌ',
                            'ɤ˶h˦ȔԌȏˀ4ĸˀĽəÅǩдӦúԕ3Ӵʍҙ\x8dɑŸʦź0Ͼ',
                            '\\\x92`\x88@ʀʑ6ʩŔʐЮбɯ½ъџЎϜʛѭ}phŤɾіАʻ¡',
                            'qțÏΕ\x8eʆΉԝӤcȴ³G͵ӿӂɍСпΊ\u0380λϙ\x9eˊӹєl%ɫ',
                            'ŊɶҖ˟ʈГȈͶrϛͻԟӿ¸ǨϴɤξУ˅ˊϤŖҎͼĎэė˥ҟ',
                            'ӥзʽͺϋΐыμƕпɲŞӂǃˌbмќϺҙĢ¼\x92ӛтăâέĻ5',
                            "Ц˞¯ӳʭ˫ģǰğ˅øʽϪҥɩtȂΘӉĶ͵ӞО'˦Τӈ˭ζҳ",
                        ],
                },
                {
                    'action': 'ӍӎҀҜήҥğʷҎěϣҎƫΘşХЧļҕ',
                    'resources': [
                            'Ѳ¸Ǡ\u03a2\u0383Ìʫ±ƒȄЇȝϸҞĹғӑΐԐц\x84ë>ƾҤЍĐӰяɚ',
                            'ʘʳŖт}ķȁ҂ΡÂұŷŉзÒ"аú˞ѰҮƌϗѷǻҫӈɼɡļ',
                            'ɏͱĤύʴĪԀԏЇ˸ƀ˥үȾЮˣőˌƾĪЕʇőϬԮӚɖ4БƯ',
                            'ƄʗϠ¡έǒƨҰϷԜΩȄ˝ˆċʾ@ˑԓȱɿ҇Ǝ˘ǈġȹÄľœ',
                            'Ң͵ӫͷѫӝГĝж˲óϵÒɹГαεk\x8e˲˩˧\x97NӾ;Ãгά',
                            'ЙĒȊԛҘāƌԈϾН\u0379ϺǲƭÓ²\x87ˑɗҤӺѯƧɲϩҦЧȧβ҉',
                            'ðȹɜĕŦ¤ӿyӧ˪ΞʏмěϽɝĦ2p\x97ВӘ˃рɅєY:άг',
                            'ŦҝπĎɍԣÔéƲΝ¥Ĉ\x9eˈЁȧǿă˽Ҍťж%κӲ˷ˣȺͲĪ',
                            'ϏġPɑ\x91κŽʓеХÕƗƲſȆɧŻԦæýƓѤƺԔϼʚӧˣΟʢ',
                            'ϱˍƾπĳĔϝЁRϾĎĹԦȩԠϏvԟǏȳϩҕԨҖЖƣΜʝөӻ',
                        ],
                },
                {
                    'action': 'вƹҚѢά&ПĭԀπуµ4ҏɑĕȨӀӞĮȋ0ɳ[ÔԧĿϽ\u0379Ʈ',
                    'resources': [
                            '˴ˣвƉƻьō\x90^ɘԕΖƦŇ¬ɒĂӿљ¹ƭ\u0378\x99ӪԎ\x82\x974ȁƦ',
                            'RwʆňѤʇùèӘқӲ¯Тҁ9˝ҀĳЍƬʾɰȚʫцƐʚҮ@Ӕ',
                            'ɗ˔ѸƜͰċσеʁӿ\x95\x97îƌăņĻǫDʊ΅ЍϤƿþ#ƨҟȧȰ',
                            '^ӊӜ˼ǓԬΟеŌƩɊɐtѫԌʵѿԗ½ӻәĭɽe ʁƓƊϪȰ',
                            'ўϭȣĩaȯO҅ћʃӖĈĐĖӌêɪҳǖ˶ԐӃ:ƏǸԢӢÌµĬ',
                            '˷˼ȍ¡˟ҩɩħȫĴóÓȍše˘ʘɾƚҒӤɾÄШϢʸѧҒѲҽ',
                            'Ŭ¤œɬōсŲƇoΈԤʴǩƏǱӚԛп)Ƭɓ\x85ϸ\x90üɖΜđ˖Ϟ',
                            '҇ǋƾΡӉΗQ0ӦϤȴèΡѲЩ˹xȬϷˠ¸Ķδ˲īĲDy\x8b¡',
                            'ǂʽƱʨƪĩĥºÙâѴrэ_ÜэŴǺɼǦάǒЬѝǥ¿ĐʧϤϺ',
                            'ʝ7љƯЦϗ҇ʋɾÍq˟\x84O¶ɭǆ\x89\xa0ʼ˵ȝđɢь˽ĖµϾˌ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Â\x90Ҍ',

            'version': [
                -6845911321897547514,
                -2316473214846225503,
                -3813652723839217955,
            ],

            'location': [
                "'",
            ],

            'runtime': 'Ϙ',

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
            'name': 'κșӓѾʏџ˃§ǒ5ɬЪʷˇȘΖƌ,ƢԥǢҏʰ1ϯǬεʖŻѳ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƪnљ',

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
            '$': 'Įĕĩđˡҥʸ\xadÌɊˋĸѴѓАȪȍӎʨóʻʴÐ»φӶſĲ˦˃',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 4397823177664305822,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -94410.36855010263,
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
            '$': '20210413:192519.417681:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '©ìĐѯ˭ʴ¢ŃҤС*ϚæԠтĪҎћBǡȀȰfκԂʬЀˁаČ',
                'ϯȴͽʙżxϔӘǚDųʃѵӹȲџҵ.˪ϿϊϡȆ˖ѠɪοĕƅN',
                'ðŁ|҅ɸÀ;њ҂ŢԛϜ\x96şнǖЌHӌϼӋϩÍӡεïɄìϺҧ',
                'ΙԀŊďƩƚôɘĨŋΞЃӍϩǛψµˤҳđӾŷ˚ϙҟȱŢşĤˢ',
                'ХćèȀȁãte˥ЫЗӡØтİŀŧțˋʏӓҥ\x8d˳ԥԮЗ.δƻ',
                'GѵǾoɵưYƕԎ¡ʞѽ˂ѸϢԩʱƣȬОū\x8eҷɤΑ˽Ìɏ˾҇',
                'Ĕ\x85đΨ§ÑӪΈ\x95ĘӗĲкN˅Ɯ·ǧċĪ1ä\x83ˎķԐԥԇϺͲ',
                "҇ϷǠǚśμöĲdhϯӮ'œνӿɽɟȒІЯΦWƛƒͷɍ®Ȫʬ",
                'ӎ1ҥӷŧҹȶBˊ:ӎ[ƾŻƶr%ν\x85ǨюѪѩҤҳͿͳȉE~',
                'ǅϷ˔Ǎ˕ҽšҮŐÔʭԧz˅ˠϓКӗjщ®ÅıИƐ7ӵǈӚǠ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -8458103107626756194,
                7993797834296044180,
                -4174098698083788501,
                -6830911977815805136,
                -1779729334250680494,
                -8195162539750098453,
                -2281794369632556761,
                142269584724485952,
                -4223963202242950734,
                -8194320736949273648,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                293596.02380481095,
                41705.71534555615,
                663894.9948440444,
                342685.60689152,
                -11203.846843939871,
                187881.67284349166,
                393330.5259554192,
                506214.001641579,
                36472.018440082116,
                581784.9124170439,
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
                False,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210413:192520.724063:+0000',
                '20210413:192520.742672:+0000',
                '20210413:192520.762050:+0000',
                '20210413:192520.783658:+0000',
                '20210413:192520.807035:+0000',
                '20210413:192520.829117:+0000',
                '20210413:192520.854239:+0000',
                '20210413:192520.879881:+0000',
                '20210413:192520.904799:+0000',
                '20210413:192520.929906:+0000',
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
            'name': 'ĭƚԍ˙ʗȶƤϻʂpԈùо6`ʢRҤȌƛɱԍơңČ',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210413:192518.956797:+0000',
                    '20210413:192518.984296:+0000',
                    '20210413:192519.002516:+0000',
                    '20210413:192519.019158:+0000',
                    '20210413:192519.036443:+0000',
                    '20210413:192519.054670:+0000',
                    '20210413:192519.073023:+0000',
                    '20210413:192519.091013:+0000',
                    '20210413:192519.108397:+0000',
                    '20210413:192519.127019:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Φ',

            'value': {
                '^': 'int',
                '$': 9109758003838137831,
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
            'catalog': 'ʹȊ\x8e\x8fȦȘʝƈΖÓƯЫ˓ѲŴѫөCӒҥɄөÜƎ˃ѺчȴɎɋ',
            'message': 'Ǘʰ\x84ʞҔϗ£åόÐɅ˷Ǒ\x94ȣÚȇѫĠͽ/я¹vԢíƉнƑ5',
            'arguments': [
                {
                    'name': 'ɋɳȔ»ǼĜǁʻһ',
                    'value': {
                            '^': 'int',
                            '$': -3031835274167332754,
                        },
                },
                {
                    'name': 'ġϲ',
                    'value': {
                            '^': 'string',
                            '$': 'ϔƝϩɤĢÖûӍȳ˓ɬƸõԋβɜ·ґš\x9bɽȨҒΒâОɐqGǻ',
                        },
                },
                {
                    'name': '\x80ǺzǝϤӺӰĐϦ\u0378υ\u0382ϨϯŨФѢǸ\u038dʌӯӂEɞħ¶ɯ˘Ӗ΅',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -5502758401812275679,
                                        5593788588092411938,
                                        -1246542091789730968,
                                        -4838394651595374773,
                                        -4325131795641518539,
                                        -6509808359408447984,
                                        2759681895808689791,
                                        5003301555401926077,
                                        -3611803766975645304,
                                        3055156523978124579,
                                    ],
                        },
                },
                {
                    'name': 'Îѫ÷',
                    'value': {
                            '^': 'datetime',
                            '$': '20210413:192517.172939:+0000',
                        },
                },
                {
                    'name': 'үĩ\xa0ѥŀӵé^ȟϪȉ#įɃG\x7fӑƍ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Zǻȼԩ\x92ȃȷѡӄ҃ɚôĂϟиµ"ɐϳqƋĐȀч¬ʦɣƏҜʶ',
                                        'ҦȜú8ͷɆӹӇçӎΜʤŘȲӧ§ŢɢɀɐЮ;ҰfЋȑɥɭхɷ',
                                        'ҺЮɁɻȾġчɬʆӎƨŨJӤѬΰʿƁϟÂyRŐɰőʞÈίԙҖ',
                                        'ɧɊ\x94\x83ɀәɻǨ5ό˔ΟʟҀIƊКФ\x8b¦ƕÀʶčϻɚżӹӮϿ',
                                        'ǑϩŽȧ§ԓ҂ƼпsǔИɸԧ˥˘ÜľǸтϴɓҬҴʒŁ\x8eː˶Ǵ',
                                        'ϏˀD˩ѓҺЃʰǑӛǲ҉ΟЪȬԊԬΦþŅ\x9e˗ёк»ǝΠÕӣП',
                                        'ʣĭĢЗЙÖԢ҅лŶҖЏȠҟгƷũǶ\x9fЇ\u0382ϭ,ʛƧȅɭЖǂ˷',
                                        'ƢCFτѬɱЅȤ\x96Éʀ¡ʪ˕8ǌƄԚъų˧ɭƂfɌɸɯГɸρ',
                                        '˧ÁĊǮ~ӾȁЌѤλӠɏӑdÈʼʓӮύ²ѳѬΙƼžȫƊΊʙÞ',
                                        '˷Ό_ĥūϪԙȷѝĄӚSӗĝΫņǡǜĢПƆàЊӈéɖ;ҕiA',
                                    ],
                        },
                },
                {
                    'name': 'Ȟ¥ǧʲҦÝƊɀѽ˭\x94<\x87ԙɎąҚԣħĜtЗƌ¡¥ԋǽӬìĒ',
                    'value': {
                            '^': 'int',
                            '$': 5736172596777874205,
                        },
                },
                {
                    'name': 'ƀϔͳϚӫΝӇɖҸHĭȺV˄ӃȧǏ˼ΨͱƺǠȁŕҮН`ɛÛн',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -3615737926228812483,
                                        -619097194324321764,
                                        -1554821070848247455,
                                        2110080514284538302,
                                        -1106361665685913709,
                                        3727510208079084732,
                                        -5592949449963467897,
                                        7237277923367244798,
                                        118979815014839204,
                                        -8637941001952783908,
                                    ],
                        },
                },
                {
                    'name': 'kKѧǎ\\ʹε£ȩѸϘʭӳӆЮƕΡӨЕʠԮƌƣϠџțҭʂOʄ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210413:192518.153558:+0000',
                        },
                },
                {
                    'name': 'ҘéäԝͳǝĖǾÍċƺçƪŜӆ¨҃ȏŻ:˂žĐħęųϸĔƍ˄',
                    'value': {
                            '^': 'int',
                            '$': 996524953560266245,
                        },
                },
                {
                    'name': 'ĵͺǍΊ\u0383ӡòʅ˧ҦȯЕƢɠӲșǱ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210413:192518.506592:+0000',
                                        '20210413:192518.528566:+0000',
                                        '20210413:192518.550026:+0000',
                                        '20210413:192518.569347:+0000',
                                        '20210413:192518.589811:+0000',
                                        '20210413:192518.608201:+0000',
                                        '20210413:192518.630209:+0000',
                                        '20210413:192518.654733:+0000',
                                        '20210413:192518.678783:+0000',
                                        '20210413:192518.702699:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ԐӐ',

            'message': 'ɶ',

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
            'identifier': 'ȚżѸҌŮǞзÁΫҨɩǶ\x95\x97]ђѿǛĲјɦѫ˱Ǜѿ®Ҧ\u0382ɴɔ',
            'categories': [
                'network',
                'access-restriction',
                'os',
                'internal',
                'network',
                'invalid-user-action',
                'invalid-user-action',
                'file',
                'access-restriction',
                'invalid-user-action',
            ],
            'source': 'Fƺ&ƀǛĺ0Ћ˝μӳõԄȎĸМ˽ȧϿƃ҂ʚǝю`ÌŦγ\x88ë',
            'messages': [
                {
                    'catalog': 'ƊǠȺфµΤДƟƱǢʩăƌŎˇӔˁӣĈЉ˕tɅ)ƨóƶǉ\x98Ŭ',
                    'message': 'ыͺɹϖϊІΐǗԜȣҀΒǐʐӯxƶ§øƭѱԜʳαϩƓ҄ҰɴО',
                    'arguments': [
                            {
                                        'name': 'ðɺпǣЀyӿǷȡ\x81ȶɮÆўŏ}Ѹ˨ˠƩŨѧʆǭȞγŎԘϕњ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѱӊĸ˳ʾĞ/ɁςϹϯҹʶάÐ҆ίɱɵŜΔϱƓȟƆʩԎɜòТ',
                                                    },
                                    },
                            {
                                        'name': '˰ӺɇȯıoqάɻѤƹ´ƇʔłӕȯğĲǓƌˎӢƏ]ɳ˓',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 404432.2402645972,
                                                    },
                                    },
                            {
                                        'name': 'ʅХƉȶѽΝʖѽԐччȽÒƣυʪώƀƄc˙Ðʽǟŕ҈\\ѹɄė',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѱÅϻѓĬȑΉћҼĿ¾4Џ,ҥБðDѧǄǩЭҳ϶Ϛ\x99˙Ή\x8eð',
                                                                            'ΪY˖ŻÌ_џӽҦ$Ԅδű˲xĠ˹ŎȄǫƖ˾sϣϗŪÌт\x9cç',
                                                                            'ёƼʻшԖŉQɒhZ˞ęůž˶ɥʃ6åĺĻŨЉˎɽΤ˱ѫңɌ',
                                                                            'ǝϱŅаζVȸć˨Щ˞ӮɟĄ\x8cƽoȻϰԎӹǨπǗ¥ÜνӫDќ',
                                                                            'ҜčŧςͼПҌɑżȃφ·ɹʳ7ȺȺŬ¼ӈԄʂǗѠļwȨȃŸś',
                                                                            'ʎtăɓȺŰ9ҙԡЍҊũâ΄\x81ϨЮȍȦŻʆӟȿɝҦȭŤ%ȥȩ',
                                                                            'ɐΠňίԩʄŻǉȵʳчòЇѧ\x9eΤ҅˔ƐˡŠцɛУӍǩћʍЬɛ',
                                                                            'ÕӤʍӐ\u0378ӭǿȐѪΑ˨İжZ˼ͰɲȁϩȿĂȾ˦Ш9цĢĆ˪\x82',
                                                                            'Ɵ҄˭\x7fœѝȇýƸӢȠӁʞˋ\x95Μ˷\x80ȥÈǳNФ\x87ƜīъŪfϵ',
                                                                            'Ɛeԭ9ϧÀĉƒRɖϜŦϙ˖ѦʼèaХϜθwύóуԪЩ0Ѕ˷',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɭhϓƳ\x9bų3ѕԅȾѥvɪŪ^6˨ϵѾ{',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˒ˡѕɥӼÑНÆҖʺÄѼӻǜȧÈ\u03833ԥƒӥÿŻȣȾϋа\x87λ\x8e',
                                                                            'ʉшЎƑҲȅϳ<ȮЁ\u0381ӵӎıųƂëԮƗƄǮɉģӲȀ\x89ǔ1Ίѕ',
                                                                            '»\x9cɁǩǮʏψŸбIΓĝѠƫ>ϬƁҶҐ˼ËĢˢϵΓΐч=ѳū',
                                                                            'Ө*ɡѸːȫжêϬǩѳɔҡĲèҋńźaӀ˨őҒɭčľÙʬǧō',
                                                                            'Ԭ\x87ˈÁɃȻYΗ½ƈůͳĵϦǬҫάp˘ͻԓãџˑǞǂԊùĶН',
                                                                            'ɝƐηЕԊ˶ԄʟǄҭϘϩǏƈ\x9cĝŋҢǤ˼϶ɟɼ~ӥčƱӷΣȦ',
                                                                            'ȨaɇgŤţ˶ѕʚПáǬ8ÍѲhȵǳâҚįɅͲKȮǊˏƻʈŤ',
                                                                            'OǷЫōġɧȈĊs˟ôǍϟĶG҉ɅLԒŘȬ˙ŋȪԚǿƨθʕӺ',
                                                                            'Њ˅t íˢǦѵǞԕŦǉʜξɼɯӴYΕǄҶ˙ÙЙ³ϻźȪ\x8cǾ',
                                                                            'Ƅԗš®ʞʀҢʑ҃ɦØΣɏ*Ϊ˕\x9dcʎӽƙƚԈʂʵˊ˝ˌϢƫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӎ!ԟ˓ϵ\u0378ӖĐҾԄΨӚāϢǄѹ=ΤƇʜóCˑɏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'RȼǴЁϫ¨β҉\u0378ѷȱ Ă\x84ȣąćȦζ˖оĎʘӦӺџ7Čò\x94',
                                                                            'ΟĽԂԈԤϸƒɝ˰țӈƢʮϽP˾ϟƵǗϸʇҪԣϠӯïӌȅΎӚ',
                                                                            'ÊЃѲŝϹǟúҊƣěnƏƸǜ8ԀԈǢΜǭϪǿȚ҇ʤӭ`Ϳ˨´',
                                                                            'cεҙȔϧɔ@Ǧ<?ҋβoɡǾɒЯϲ]˳ҁʎЄʵǬҋҼνĩѶ',
                                                                            'ˇɇȫũÑҨǝӆ2ӞͲÇ¶#ϛǱæиŧ-ёĶ˴ʆ.ν˾ŋӐº',
                                                                            'ҌԅȊҷΓÚɒ˦ԝɟ\x87ͱѓ\x80рǅȷˁʤѴεѲѽΈːŔhȳʩͽ',
                                                                            '¨ǀ΅ўĽźΖˏɩΈψͲʇԤ»˱ǆɨ9ԫΞ\u038dŏ\x8fԔƜѣǟȡŕ',
                                                                            'ˁ[їKжȁT@ʭΏjӒÒƠʔÈdүЅіˤʯ/ɹ\u0380ʲѤú\x9f:',
                                                                            '\xa0ưȤԗŮƍԫųΓ\\\u038d\x89Ȟ;ȓЄƺ$Ȗ\x93ԏҽŶǭțǵ\u0380kϢΌ',
                                                                            'ʳғГħѠˮĻʽûɾŗӹ9˪Ҿεʭт˳ɳɍƧҍθ˚ŝőԇԢθ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƓӟƃçǂʲÁррůǮ˹ȨҟĖ¿Ԡô¹ǢяӼȫˢBϴʪԮưҨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:192458.000905:+0000',
                                                                            '20210413:192458.023680:+0000',
                                                                            '20210413:192458.048440:+0000',
                                                                            '20210413:192458.072472:+0000',
                                                                            '20210413:192458.093126:+0000',
                                                                            '20210413:192458.112466:+0000',
                                                                            '20210413:192458.132603:+0000',
                                                                            '20210413:192458.151509:+0000',
                                                                            '20210413:192458.169143:+0000',
                                                                            '20210413:192458.189171:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÎρϮŵŤs~ƭґѳΗӪgʀΎҝѱǺǔ\u038bʙĦVɲш\x94ʹĕ©ȸ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӫͺчћҢ\u0378ЭϏҗҵɳĮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 483274.07017065154,
                                                    },
                                    },
                            {
                                        'name': 'ʂč͵ʒơĆƏŖϘÉËӞıŠʌɴȾɃ%ǝƗʺũħʹɰɂ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': ';',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1705748807460915154,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x91ÁӁˆϾˀαǛМӂцĿԚšҥԝ˂ɶвӞȠɤˏ-6ɑKȒYl',
                    'message': 'ϝľω˕ЭXіҠĮӃŖƕɠжƓŦӱΚ#ϨчsŉÏ΄бѱӮΞθ',
                    'arguments': [
                            {
                                        'name': 'ǏċđУɓɸ\x92',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:192458.692879:+0000',
                                                    },
                                    },
                            {
                                        'name': '˨άɄÕƚŘŇɨΡЦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:192458.779195:+0000',
                                                    },
                                    },
                            {
                                        'name': 'tˀĿάıʱ˷цҜƕόҤʼΣõ(ӢŝЭȣӜÌιjsǥ¾ēŃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'άȟˤȎҀʉ\x8dÈxǮӶ\x80\x93ˣÇ˽љźɒȶдӺ\x88?}ȕȺʣ\x8d®',
                                                                            'ШΝɋӫëлЊʛ´ƳiːӯΫ˻ϕ¶ѕȚҸȼѭ˅ɧ5Ӥ ʶƓʗ',
                                                                            'ʍ˝NȌˋ˘ċίĢСƽɡӄͰФźϭȕ˧ƋśåϏҴϺɀʐΝɠɐ',
                                                                            'ƛ¢4ƊӋ\x93ӹɦ\x90ԌԗεҬʉœБҵǂǺѴƾѤʁÆʖˑʵҷǙċ',
                                                                            'ĖˉΊ7ʁϷЕԫɴӴ¡ˠŰʎð^ԇ%ɯʓУΤɔϲȗͺȜgкʠ',
                                                                            'kǮƴϊəɡēЖ˵˭:ϟĎKΘÏ\u0382ˮ\u0378НԡÂÈ¸ȾҞѦДөR',
                                                                            'ʻȔŻΜӈъƾŐΤξώɣ·эĮɇƚԅƆӿτ˽\x83Ä˚ßΰ¯bʬ',
                                                                            'ȸǡ˱ķ{ōĎËӌƟ\x89Яˀûʳ\x96əaȵp\u0379ȿĬaˇҀϸó&Ѿ',
                                                                            "ϰLÇ˔mҲĐȍͶğҦĝӊȿ'xŜɨ\x92\x9bәƧ\x94ÜÔϩҢ&ʭǗ",
                                                                            'ǦşԤӱҝƬҨȷ\x7fuÔþį˭΅тʵҠĺş!Ӫԋƅʑ˥ǿɩΩċ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȑЖĥĽџµɞ\x97\x8eÃǷňН\x82ƿϚӍӸǱǟѥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 722934.9247070781,
                                                    },
                                    },
                            {
                                        'name': 'ˑĪ§ϻљʴ϶љӈοԞϢǙʢĬюāɌԋԅсԃΑϢӲΤÓДŦˡ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -81544.55141546177,
                                                    },
                                    },
                            {
                                        'name': 'įŰ9ӗǉuҁŦØщϏШϸОƨ˭ԑµԈқʶưƩаŁΒңȭñą',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            558350.0501544077,
                                                                            -55794.90121272042,
                                                                            -5746.520080795846,
                                                                            339841.0860501961,
                                                                            41604.23235952592,
                                                                            38534.24566630932,
                                                                            472854.48108511954,
                                                                            893577.622509239,
                                                                            -2115.519821582144,
                                                                            708040.4926752935,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8b+ƔщgǂЭʢѻЂϻЋʏȳɻʱƖʴȕ˓ʚƆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:192459.823660:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЏwϷ4CϰlҴԜC\x91ĶǸҐŶƪÒɪé҃k',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˹ȞϜĻĵʑӪ˻Цǿ˟ҜŶѳǖ½Ӿ\u0379ӓȝȅŒJαɨϷʋĻɗƢ',
                                                    },
                                    },
                            {
                                        'name': 'эZ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:192500.081956:+0000',
                                                                            '20210413:192500.104061:+0000',
                                                                            '20210413:192500.127176:+0000',
                                                                            '20210413:192500.149811:+0000',
                                                                            '20210413:192500.177445:+0000',
                                                                            '20210413:192500.200772:+0000',
                                                                            '20210413:192500.223883:+0000',
                                                                            '20210413:192500.247288:+0000',
                                                                            '20210413:192500.271562:+0000',
                                                                            '20210413:192500.303851:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Р',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1427707485751798668,
                                                                            -9173511810599552310,
                                                                            -5848138650890722001,
                                                                            -8314874140056647549,
                                                                            1215430999053247357,
                                                                            6512188203846783904,
                                                                            -3751828814618086706,
                                                                            6428975607954678120,
                                                                            -434412196598319446,
                                                                            7149305734645367626,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʵ\u0382ԨŧχЮĳ˦О²ͿŚәʫΒ˪¢ӷӧ҂φ\x88ˉ˾Ҵɰªˈà±',
                    'message': 'ĎѸφĜȘΨĺǛԁɔŌѓʠЪɡȈӷυĜÜҺŲȽƃтġѶυÓ¯',
                    'arguments': [
                            {
                                        'name': 'ïơԭҊѥӽʎţҡʦʨƩ˂҄¶ҖΒҍʠ˫ћƤˊ\x94ØöʄƷŕԏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȻʵƸд>ԋ΅ѧц˖ηɋQӏųȪʾŸҮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6125444114636127209,
                                                                            -2583610637337723096,
                                                                            -6231787834093793750,
                                                                            8009931751655960750,
                                                                            4358250582263933467,
                                                                            -3971074189800602653,
                                                                            -6048270612446879858,
                                                                            8165453517006051324,
                                                                            -5591702791439881889,
                                                                            1715521690444746847,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƖUЕäξϲѾ\x7fӁ˵ɇ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŁΚӥďд\x89оΏƆĻǕ¦κπѾɲFΛѼλ_łҦӘӷӐ¡ȰƴĽ',
                                                                            'Ǜԛ˦äԣEƌгƋșNʧзЬΗĈϡӀӡĢ\x8bӅŚʛ\x81meƑĜǘ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'МҽҺǼԒʦ\x9eΥӽ;ǇӬХӍґǆӎ¸кіұʱΗǓʫҬʹΝŀO',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5293260267293531324,
                                                    },
                                    },
                            {
                                        'name': 'ΎԋɬΖвɝȴˉ\u0383ͳЎ˽ыϢҴĢľìŌ˪ƜʺűŊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4773141545692330702,
                                                                            3009033403545431875,
                                                                            7985254395457312356,
                                                                            2766829135554385323,
                                                                            4301811982275214761,
                                                                            -6996615470202361031,
                                                                            940741097420590166,
                                                                            -2273946527310065555,
                                                                            7692316720997831926,
                                                                            942819115619643127,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԮӉ\x84ӊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ГϜƁңθΫƹĝź\u0382ӹ˸įсӝrŤϸΦԖǜŃϝŞǓǼ҇ÖЪ҄',
                                                    },
                                    },
                            {
                                        'name': 'ǍɜƔȰƣԁҧîϖºńϽӠЃřƄ§ρgʈņ˶XͻʎҒоϝԎВ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȠƴϧԩҽԉGΝ%ͳƁʧџęǗԈɈŵѷ9ГǐʸoѺęʦŢģñ',
                                                                            '\x89ɾҖӈ^ϩǢё,ȏΗ`\x9cˏӬƂЫ9ͳϺω\x83Rǒɜǵ\u0382ŠЉŌ',
                                                                            'ʦǸчԕƳ\x82ӠЭƺҎƧʨƁГЗƻЍ҇ˍ:ƵãȡɭʢƗ\x95ԑŬǱ',
                                                                            'ƓѬžȓȱΝ³Ѥį˓ҤϬѬɚ`ӹѠʫκǟϭȋƍSӬʯȐȩӼҖ',
                                                                            '\u0379ҡԀБԬ\x93čЀκĎёģɔΐǨξѾĮβϛϫԖɮżǒǔŚÛ˺\x8c',
                                                                            'ƐΆĘΆʕ7ɺχӲǳôɸţǚòԏˉҋ˥»ǽɕe¾ӣѹ*ĭ\u0379r',
                                                                            'ūԕˉКǘȆčȈǟ·ѷīɞѕ҈Ҕŧ\x88Eĉ3ÌȮ˛ȳŮάɝ¥Č',
                                                                            'ÕeǦΔϡʆѺȸцɒЖƆҍĻѝӓҾ\x7fԪΕΦѲǮ\x94ЊBȆɓѭ¾',
                                                                            '÷Ξ\x93ΎϹĴAӳѮƻ;ƄǱƃð҃ˬӭӗӟѼùύƜÿĠʲК·ȝ',
                                                                            'й΅÷ĿȷɅПɶѳŴ\x91νĔСχĆķyхӲʈŎĐ\x9fȶԦӀƢ\x91Ϥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÕƼӜϼʍůĉ˦цfȣЕΰɳĂјϴүɫȶҎǇəԐdʍϝɡҹķ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'úНάҌÆ!ϏÓƨ£ĭʈǍ˕ϭƨ҇0ҍ¶Ǡѣ\x9aHԇǐëϺ˞ʀ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2735389315861539731,
                                                                            8745060120720224217,
                                                                            -7642080504074088628,
                                                                            8470616835840515677,
                                                                            -7818237313472395146,
                                                                            1754545492888973939,
                                                                            -1867348935074148984,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'gϓǟƔѱԪɞϑ҇đΥϱ@˔¤ɍƵҪŁğgˁφϹԣӇ˗Ԅęȍ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѨŒχ˖ħхΑҐҲ%\x9fÚŞƉʖҏˉԄӎ3ɹΪѢɔµӱ·ѡ\x97ʥ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҩԚέ\u038d˼ѭʹӆ¬ɂҔȾцǍΒϾδǛŴͰϝŶҳȏȾӋɼԦƛŗ',
                    'message': '˽ҶЈίNЌ\x82âLцЪǛ\x9cǼϷä{ѬбзÔƸǴϱΉԞĩǲПr',
                    'arguments': [
                            {
                                        'name': 'ǂŗʕΡҖă9',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÊУûƾӦ|²љħиŇʜʸ˨ďʗϿȻʖɑʚĉ_',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:192502.547613:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԮЈŌΑзǱF#ҋǚѬǹԘȚ²лȂԗЅӼƸǙҖȋōſƜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˺Ȫƍ˫{ʴʇΧЃӴ3ƺЫԃμCƽ˖ĔǞ˽Ϡϱ\u03a2ćŜǚҾùÜ',
                                                    },
                                    },
                            {
                                        'name': '\x85ͿʣӖϮÁүʤº\x82Gɔ˩˜×ǜ¥тŤУƴ҆°ʈ˦\\ȪʎΪʁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 69236.99006733706,
                                                    },
                                    },
                            {
                                        'name': 'õ|¶Ϙțƴ˘ˈĦĬʢhƨĸ˲ȹ˓',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'СЪ҅µȊõǹӣɄŠɖύԠǟËɰɖǕìÀΗüԞΜҿɩћҀɀŧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2026852843158318917,
                                                    },
                                    },
                            {
                                        'name': 'үϰēқЊѹīѝΞȉüϝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:192503.207089:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ъҟϓƨ£öҬԥΨĈέЋ\x90ʦЏÇŹβӗɂȘȡµϩБдrϷ0ӫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Γ\x7fʲ\x80á϶úûҬƢſΆҊɻƜƜϫӟϙʸńā½əɥê˧˃ĠԠ',
                                                    },
                                    },
                            {
                                        'name': 'ԌәҚþ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:192503.404009:+0000',
                                                                            '20210413:192503.426308:+0000',
                                                                            '20210413:192503.448582:+0000',
                                                                            '20210413:192503.470729:+0000',
                                                                            '20210413:192503.492893:+0000',
                                                                            '20210413:192503.515407:+0000',
                                                                            '20210413:192503.537515:+0000',
                                                                            '20210413:192503.558882:+0000',
                                                                            '20210413:192503.580525:+0000',
                                                                            '20210413:192503.602253:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЋԝȘɼɒԚϣфȌɃЛɆÊѣƕΟӚřħb\x95ЇƈΓ;ʇȀʻΕ\x86',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9062439571762750778,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʽҢҰҖΟ]ѻŰɧƎ\u038bɒqҨŖњǉϐ_ήȈҚɷũ\x9dҮҬǤÊӨ',
                    'message': 'Дȹmˏ«Űˑ҅ɶϕЁƌΒБЌȷԪĻψӽόǼľ\x92ѴĮŔǻξ0',
                    'arguments': [
                            {
                                        'name': 'ȴѫǯұҤǎҍǢÓ\x9cǶ˯ȟƭƛ¡ŽԇbΊNɗʈÂӐ\x96â˨-ć',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2103574893121509468,
                                                    },
                                    },
                            {
                                        'name': '˝ǮĺΤϨ\x9eùfǋ\x84ζЄJ˩Ȗ\xadΞƼžfǮˣÖёāȀȡɽăǉ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7468949363960037774,
                                                    },
                                    },
                            {
                                        'name': 'ȽȮĴ\x99ňΰɩͰϩʀʜѵƷóIȹџЪ\x8aΣή',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԑӉǦÿƝИĒóǑԬǬeƸ¼ȃѐʱԢĵǺʪǉŊǅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʞćõƨύSάÎФ\xa0TҷēĕF΄ƖǌƏÆҭ͵ſaɿϮ~ĩοϟ',
                                                                            'ĪŠƚԘˠơ\x86ġӌĭ/ɨҺ˱ҳő5ɎԘŇįԈƊļԟDЭΫ͵Ҁ',
                                                                            '$Ɔ҅#ȌɎӒʹ϶ĿͺϲʵΪǷҭ<ͶџΈ\u0378ȒƄαҨҽ\x9bãƲȳ',
                                                                            'у˻ǲƔ˽ӊБŏюĸƻȵŲϝӥΠǴϵР˗ú÷DѯƯÈɌǪђÃ',
                                                                            'ӇџΞ¤Ȩŵ˕ҟȫЋҁǗš\u0379ӐІĲɩƖϹ\x86ХȖ;ČĈɱάÛ˨',
                                                                            '!οπĈͱ˧êӜºǦĕНȽƙѹēΚΐеǘĽǂԖ«Ōқҹԝʹǵ',
                                                                            'ǎʜӈ\x80ȭȺ\x84ȔʷҠʃȪǦԏ˼кçl΄ûºƽ°ʕЏ(ŴƞХâ',
                                                                            'ÁԆãĨƑÝȠ8ԝǶ.ɦɔŝοʜɀДʌӌ£ÃǞŕĻѩɗǐȅ\x9c',
                                                                            '˘љўƃľ\x9bĂӋɇʶƄϾҚɞµǑɼѹȴȓƓ ȮΟċ˰·ûȚμ',
                                                                            'Öӡϗȉʉб\x95ǯ˪BӋǘĢνĭӣͺ˕ŸΏǨˣӓŏɵˡâľˣd',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'QǿƘ\x85ʊԆϟůɜ?ĴǓΞļŕęĐΛѹëǿԝǝπԏLѢѯӎ˥',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:192504.569648:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʩúƧǗҼӋԅǾŕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȋʉɯѵӬŋƣϾмԞÀȰę{~ζţÈǞʇӞkƭǊɲɝυĢ˦ϔ',
                                                    },
                                    },
                            {
                                        'name': 'ɇŋŽǀȑ:Ȓ¤º\x9eːԮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4272739707698441617,
                                                                            1926189176619512541,
                                                                            -1319095613438433586,
                                                                            3341114975033306548,
                                                                            -6763086731154990935,
                                                                            -4200586430310510454,
                                                                            -8391321742012422799,
                                                                            -7645526204222824170,
                                                                            -188422101339948764,
                                                                            -8904685852308385026,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '»ȇҍћʎӣƝsőXś҃ˋƜҨͼѕϢʤɗϽг¯ԭӚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '.кƎʯǉӳԉԎťĠԝВūȏǣωÅɹ«¸ɆηԈϜԧБϪӈѻʤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4430344572593334529,
                                                                            7707319190163517593,
                                                                            -46225983233119144,
                                                                            1690909471238731232,
                                                                            3020547328013955697,
                                                                            -3878495608954914609,
                                                                            -3655756641730396777,
                                                                            -6008161374908980014,
                                                                            1424689904275562833,
                                                                            8362480086060010267,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӆІȉ#ɘͺΞÞƳҕϛǡƘ-ђʁ\x84ɀӨƨϭ͵$ʎ˳ѹɨјȮ˶',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˒Qøφ˾ˊїP˴ǩҼ\x8bLϤùӾƸтїҼǬԁ҇ӕЮΘӧκ\\Ƶ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʪħґʠ\x92ȅɴԇ',
                    'message': '6ґʩҞңȟθïѤ·сƏ\x95ѥОήί˙ȄÁ§˙ιŞǢћѤȹȫӚ',
                    'arguments': [
                            {
                                        'name': 'ǁΌ«ɨȼяІȂҩȞЕ˨Ρ\x8cӯԩǲӁǉШϓǭ˦њȗ˲ȽēЂĂ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 284225.919125351,
                                                    },
                                    },
                            {
                                        'name': 'ǘëȸȩǨȫŠƯѹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4433019884909840562,
                                                    },
                                    },
                            {
                                        'name': 'ΒЊΫuҙƥв\u03a2ɭƪͻȄȧł',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǳ¹ėǡ˔ԋLĶӫ\x83Pˆ6˧ɌĬŋӺƘȞéɡӟ˟ВɎў\x94ǿú',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2347295006113122799,
                                                                            -8029194964094404373,
                                                                            -7763197234884004515,
                                                                            -2793312315425627531,
                                                                            8524269136071404460,
                                                                            9210662337611400927,
                                                                            7786684318433673644,
                                                                            3840128349931181533,
                                                                            3157973151269133948,
                                                                            7968163811488763509,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƱúѬÏԋвю˴ŮԅˀÚΦťȎЋѫð\x95×ĹŲÉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǈì¶Í˥ěҒӲЌϧӣK\x95ǪъΧüʸƱӍƌѿɁӕ\x88ϫxӓӎό',
                                                                            'ș¢ȧʥɎэȖύîΦ҇ͷ\x93˛ӦȘϣхӦχ^ͷϓҞԂĸĔΤĽȬ',
                                                                            'в~ƋΏжәӣ·ʏɉŮƭķ6ӵ\x94ѬϽҹГǭθˬƘˌǻk\x82ǒƄ',
                                                                            '«ϭқѤ˰ǪƆľɂ\u0383ǚDɐЛЅ½єХ\x8aӨ\x9fğΗѝǢǭӐș˾Ŧ',
                                                                            'ŽϾʨԏĀĞśʢŬǚѸʾӎӨÓԢǞª˴ͲȟˤɩϢ҄ɕӌǝΖð',
                                                                            'лȆȊˀҟßƳ«ĒɶČƆĸӏgʍјań\x82ơș±ųǾͽаѬđҚ',
                                                                            'Ԅʸ\xa0Ѥ˚˺ϻϢÄȥưƇęʌÅǎͺӐϻțВѷ©2ńо϶ӵȑϤ',
                                                                            'Ǹăӥ˦\x93ҺĴȸȄԄˁˤaжнΥǌŊȼІҲŷƓΩШɀӠĒԌɧ',
                                                                            'ȢǑϋýʓțĔʵО҃ƇԋƂŰӅȅԍϾоûġºʺǞǹżЍǥǨѯ',
                                                                            'ϕΓԋǌȥҤóӁҲϾϸˢαаCïӊÊÒ\x92đΠҾIʵϥĒȨˊѢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҟɡ˙fşŕƋǻ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҁSźѸ˻ўȯȗѪѕzǲŃǮΉɫ§ą˄ȋƘŃɚ¦ͿPιǯʕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7328324001099952613,
                                                                            -7341869439381975638,
                                                                            -1107037121917983889,
                                                                            8932475485772162820,
                                                                            -5591040812431910963,
                                                                            7203339568757526010,
                                                                            5601604125524821365,
                                                                            -8446532006710734822,
                                                                            4061105133528866160,
                                                                            -5285318296610948367,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Å\xadΖǔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3375539281605018176,
                                                                            -7329377048959795391,
                                                                            -5891001667279450967,
                                                                            8338349753291871980,
                                                                            8972644945645035303,
                                                                            682083294519957453,
                                                                            1426202309009387010,
                                                                            -268224564394040840,
                                                                            1185276611584545931,
                                                                            -7893468664573832035,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȵƜʽΓаʴΓcԔύ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3434943106474153399,
                                                    },
                                    },
                            {
                                        'name': 'ϳ½Р&ѰӅ˕πҍĝŵŬŻҝǮǅøį',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5016703575282973987,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ȋī@\u0380=ȋʄʥ¤ïɀѦƖȕǰͳöҕЮASþʷГFԗ\x9dˎȼ8',
                    'message': 'ҩơƇΌŰ¯đїԁȴnԫɄďʏëE\u0379нӟɟ\x90fԃƄĠΜʎʰˎ',
                    'arguments': [
                            {
                                        'name': 'ƃҌ?ʌάϯǻӅдƦӺɼ\x9bГԥʅ¹ǺӝʷѥĳқâʜӉĹθʓҋ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʟȻūӫ˾ƱȞˈΒ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¡οҼǉ\x81ϚʔқǠɧń52ʏϳɈ¸ÕǢTlʃӌŌƑ1ԟϵӷɜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -243667140860130849,
                                                    },
                                    },
                            {
                                        'name': '\u0380Ͳӹë{)ӑώӧɆĸnƁŧá®ƕ\x81Ͳө\x9cĸ`ЄĶȻ·ɯũƭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2753414942993653537,
                                                    },
                                    },
                            {
                                        'name': '>ǽϭЯɊĿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:192508.282345:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ơʓΙѹΦȿҍшƱԑȄɰ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'эҜԮґ\u0383ΘǽϛÄ\x97æə×ҫđіȸ\u03a2ϸΖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:192508.746006:+0000',
                                                                            '20210413:192508.777339:+0000',
                                                                            '20210413:192508.808835:+0000',
                                                                            '20210413:192508.838375:+0000',
                                                                            '20210413:192508.859109:+0000',
                                                                            '20210413:192508.881404:+0000',
                                                                            '20210413:192508.901648:+0000',
                                                                            '20210413:192508.920558:+0000',
                                                                            '20210413:192508.938017:+0000',
                                                                            '20210413:192508.958141:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҙшɴ»˅ĽӋ˻ҟÒșƨΨǾν',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˰Ʊ&\x9cϷØіƘщɭʊΰˮǤΎeaèâ˃/Ρɭɛ?ǘҸȞ\u0383\\',
                                                                            'ϋ\u038dʑԈΖǄ˶ǒԙΦҙAǋʱǼǒҌɈƿԮӦīӥςɱҁчҝəͱ',
                                                                            '¥ϚʩƏβ\x87ʡв£tϏſȚƦȟΛΤ˙¬³ȷ϶£ǸЃʮѦȰȗƫ',
                                                                            'ΏɦԅӉϷѶ$ŇòʌǔŁMƿãʂ¼Ǹi˥[Áϟƅ/MϷ\x8fŽѸ',
                                                                            'ЍҳȵĕgΧůɉæҗǙ³EҠǪџ\x9c]әˉǒЌΙǻϮӸűɵ\x8cà',
                                                                            'ϯҎɷЇϐԊɟʲʍȪ¾ºƀ˗óŝfҥ\x8aɄӗԛĺХ!Ȟδɉúŭ',
                                                                            'ŹҺΩÎϟӾÎðơӳKԤυèАϝΛįΐМʋО8ƷρΒƈȦɻų',
                                                                            'ФÊӛ@˖ӡԠʈÂȩĵǒұ\u038dHƬǤʁǙΑԃPөê\x9aӱČιɩЄ',
                                                                            '\x99¯ҚԪş˸ģϹʛβƒМԘнÎƲѾϐ\x89ƄĢÞʜíʩ\x9bɐԃtǐ',
                                                                            'ÊȮѼ˛\x89ϡѿхEI\x8aďԩθӖáĽŕюűŏӃ\u038bˤΌύҝɕӲ\x84',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˎ\u03a2Ȩ>ÝÿăŮε\u038dʉҖȣˎʈȟѓɛѕǕŕțŗρ\x9bòɐƷӺΡ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЧұЖӔ\x9cӯσΖ`ΫѿǛ˙ӎ˶ǄÀǻŚǄȯþĞ;',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '©ĥøԪӝțәɧĿœʔ\x8eŪƬƮƌϑϸųΑōʌɡʯϡƉZ}ǡϵ',
                                                                            "Ҁԕʰ\x9b\x90ɸǪũɳgĎҷīқƏāOŢī˾ҰŷðӚȽʓά'ʽǼ",
                                                                            'ӠȊˋǓŊѣɁϯϏɎĮȀȦѥЅЌ˗у˒ӑЎӢǖƈōȻŮ˷һę',
                                                                            'ЪɉUǦcɏӯĵě\x9bȌβoʫҢǑʹŴʽDȲ\u0379ɑ\x88ČǨϩȒɺϫ',
                                                                            'ÙǥĹͱĿȺȣʗīпȯĒ\u0383ӝÔ\x9cȴȭȴɵmӓжϬοƒӤϴȹӱ',
                                                                            'jԗ\x97vŬŌөѣ\x81ƞҿˋԒϯĜÎӻˎŔή+ďŰӊƬϺʚӹʌӋ',
                                                                            'ηʚϾ\x89ԕω *ØƀӤȗԧ\x94ѱȧ˛СßɡΎΊˀȩ˚UΥ˓ʟΩ',
                                                                            'ӜϐңЗ\u0379͵ǂɎșόϕêțȎҋʂÐ˺вˮʆΛȇӡ˴ɦԖ¨ǧӋ',
                                                                            'äԋrǠǰʶїȄԮÞƴǑŪ˳ƨȪťӘӝϻRǇȣƇέ-Q\x92Ƞȿ',
                                                                            'ȔъϰҮʖ\x85\\ѐҪӬȉʶрЉӔŲĊǻƐŁźʌϳTʐ-ˀ˨ғɀ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˮПĵŬ«ä^ɗɞʋӛˠȓðƮΎɃǴы_ҶџÀґΏƩ.јЬ˻',
                    'message': 'ǰɸĩțȾ\x86ǒƬΈкΖ\x98\x88˗Ɏ#ȈěӇƣӔ®ӑ½\x94Ƈƿˉʹϙ',
                    'arguments': [
                            {
                                        'name': 'øĬȘɦԊǖ$҈үЫƵĎʙЎӓńɓ÷ҜФӤΎѕ\x8dòǼȋǝВǳ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 17785.105744566346,
                                                    },
                                    },
                            {
                                        'name': 'KΆʹƜӷΊ˴ȵɼμԅԂԎǅRȯƙĩψƵ\x91EѪԝˮυ\x93ʍ˽ϕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'IɁ¸ԐϐѮϽǜ϶DȈˡȭɇϾЍʽ(ƒʺǥԝКҖαĎȉӥ҈ʴ',
                                                    },
                                    },
                            {
                                        'name': 'àȞхȳΥԃѼϣθΫ\x8eĎé ȵ˷ԪƭΩИJl\x94ˣƗϰǮ.эȗ',
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
                                        'name': 'ͺŽǎτŹӿĺ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:192510.587163:+0000',
                                                                            '20210413:192510.609043:+0000',
                                                                            '20210413:192510.632738:+0000',
                                                                            '20210413:192510.654853:+0000',
                                                                            '20210413:192510.677000:+0000',
                                                                            '20210413:192510.698805:+0000',
                                                                            '20210413:192510.720293:+0000',
                                                                            '20210413:192510.742423:+0000',
                                                                            '20210413:192510.764244:+0000',
                                                                            '20210413:192510.785845:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '?ȖćµƍͲμԮƹдȯρłˮ\x8fΒǄϹϻ˧ӪĲɨΆŬƃƻǏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǅɭɪӉԭάÐϊҦuӿX\u0381÷īёӚϹÇʺі˄\x96_|ϹΚàçº',
                                                    },
                                    },
                            {
                                        'name': 'ʢϛερǘ˹\x84ӔͱňɎ˷µЩȃΆɹƙЀƶ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ПŝĹżˍ˵ҟSΝѿ\x80·˔țĵˏ˴aγ\x99ì½',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÔщЩ˯ќԩ\x80ǋԄíЄoˌWŰÜΐСīź½ǑђǕƛ]à҆Ɂɻ',
                                                    },
                                    },
                            {
                                        'name': 'Ľԭ¦ҥϒҎŴ\x9bЗʖO¹¸҇Ԟ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'nАʉӚľϸǪ@ʤӈßѯȨКéΉѵ˷ͽǐÇɺUƶȭӐǡϲŔԌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҁ¼ʛ%ÄɁƥǅǷcрϩӄŃ±ǺƤѳǝʖҁΊ<×Ɓ¸ś·ѝҶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˢ½Ǣӫϋ½KҦȽµ2ýǼжȪÏʈɽͶΧԭɌѐϦɮJąѬżǳ',
                    'message': 'ԩkïӝϫÍΧв\x8eŚ¸ʽȑίɶԬԌ)æđҍǜŸӷѳҬ˛Ǳɳƫ',
                    'arguments': [
                            {
                                        'name': 'шǁ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'AëԞɬьňζêǄ˃ˢβΥԋƢЧǂұćωԍӸΜǨ°ƒC³Ǐǹ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            722840.3253284285,
                                                                            272481.0891899163,
                                                                            -61456.81199255758,
                                                                            197982.89631445298,
                                                                            999997.8100886659,
                                                                            56219.243040757574,
                                                                            197907.75831985445,
                                                                            655477.8045198133,
                                                                            64806.97861283476,
                                                                            140079.31802844,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѭ˜\u038bıάŁρǯцύуĶɉZáÓ5ɒѶéÆɨzвѾȕ½',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2175519624479887203,
                                                    },
                                    },
                            {
                                        'name': 'ԌǷ|ϭźʈΗϒˠǥˬǴŧ\x96ęƱǻȜȴтÎȕŎӑ\x88ԣӹЇҫѠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӹƥ˂\x9eǃʲʹ\x94ҙȅiŴşԥȨȗőΜ\x80.ǤɭŹҽ£јηɀvͼ',
                                                                            'ѺĞșƙҝϚμУΐɱȵХǘ˺ϛĞ¡ΖǬĄӍԊʂ¥ýEìĸІă',
                                                                            "ſƒR˖Ƅ҆ԉҟSƾԊĴÅ'ÖRɏӤΠɸϜǄUҕҘuͷƌŒĐ",
                                                                            'ȐŶΖʺʋƍ˃ԞǇĮɗ\x99ЬƍΟ"Р´ħBÖΨˇōӜǵӯνϾʫ',
                                                                            'ƴоhǋȏżş˕ͿԂ˯ΦΟЖ¹҂ЁɄӨʵɼĠ·ȇԁǈΠ˱ϻν',
                                                                            'ҔɅѴı\x9fȸʺЁƷ[ɁԚɝȖ¬;įʖϓʶ®ˇɻΦ\u03a2җɯљĪø',
                                                                            'ŏYɳöɇҵʬӞʨŽïƆĪѮhѳǯùͳѶ҇Ȉԑĕʪ÷ΉïӜƶ',
                                                                            'ҺϋƯ_)ƳµÁ©ħтǉΟǰÝȃ:ŜŁėΖ˺ŽʒǾƜ˯ύƮƏ',
                                                                            'ҶnјòРʽǟо\u0379ɶλǥʯӴЋſӠә˥ԉtҡśǗӎѷԐƻ˴Þ',
                                                                            'ÁƘ҈ԫȍɢˁЇìжҊ\u0383φϊ\x87ЫșȺʲĒ;\u0382ńƱȢƗǅȔԘӳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˮфԪ˼ТÌƬaѷŝʩόҘȌчȏʐԀΟɱƳǡёпϼǿ˖ĝӥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɡGӲђҺӼ{\x82tϊɂģ\x9bƜĘ϶¼ď|ѫ@ЊЋĆϑčƻѓˋԍ',
                                                    },
                                    },
                            {
                                        'name': 'ƨԙԚ϶ƞԌǴԤӭӡȃрԅΧɋ=ѼǍȁӿҡ˟ʑ\x9b£˙ɯɿwЊ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'чàŢ\xa0ϝɪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4781255435576273955,
                                                    },
                                    },
                            {
                                        'name': 'ǹόԛś',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:192513.488980:+0000',
                                                                            '20210413:192513.512381:+0000',
                                                                            '20210413:192513.537129:+0000',
                                                                            '20210413:192513.559334:+0000',
                                                                            '20210413:192513.584184:+0000',
                                                                            '20210413:192513.611328:+0000',
                                                                            '20210413:192513.637782:+0000',
                                                                            '20210413:192513.663410:+0000',
                                                                            '20210413:192513.688145:+0000',
                                                                            '20210413:192513.713908:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŵѫêńΎφϲ*',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'bԌΠЪ\x98ӅӧʠȺџɍУơϹ҅ҴŨʑÕʔĨ҇ʵÛΠԢҡśӃѺ',
                                                                            'ƶ˝xѺƺēǞє\x82ʝʿΨɪÉӍȯήȬ\u0380ɻƚyɢˠȼˏϩ˦ͺӯ',
                                                                            'БŠΐΓ˦ΥξÑϼɦĺYà҉¿҉ʕϦԙҗѶӡ%\x81э\x84óβԍн',
                                                                            'ŕМѻɠǒŻ(ñĸȁˎǼ˻ʐ˟ӟӏҫ\u0380°ѭɑ\x85ǾжʎԪшӢ\x9d',
                                                                            'ȳʹбƮtęǞ£Ӹ©ˮӟƍŶъWҟЭϪԇЊĦȦŵlϣхǡӻć',
                                                                            'İȔʶԖȲӻöɭƐԏʮԐ\x89ƞʅ\x99Ƅ3˜£ȻʖԕԊѓԭ΄ԇǩÜ',
                                                                            'ӈԣϤϡƠбΞɦ˺ɡÁĂ§Ԭʂ˪ȖʱА͵ԅ½rҗδѦºȌéɤ',
                                                                            '¡āͰӄƸΣѣѬԃăΛİȜȄgϿʉŗͶΛ\x87ЦĶԚŽԟүĠˁʻ',
                                                                            'ōЗΈ˵ǂϓԭ´ҜѻÄƓЇӥβϣϪʿ҈ǰˠΎƜ¬ʵɢǺŽΦϲ',
                                                                            'ǧȼҏŃ,ӣ˷©ПƻÞ\u03a2ů\x87ɮŊЦǇʗ|Ƙʄӓĝ˄Џæǡӝӣ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Èȫ˲ĕŴԄČ΄јˏȂ·qСſү',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:192514.165311:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÄϽȁҝӢҮʎ˨ŹҐǊXȕЖ\x8fΘɢӸ˫ƿн˂NäɁ\x98ϥϙαʆ',
                    'message': '˗ĐҠȔΆѹɭȑʩšşτęϱʝ\x81ғJʛҊԛȀɎǗӡĢǠðӎ¡',
                    'arguments': [
                            {
                                        'name': 'ʗԧűȥņʅ¹ǝʶχeɗ9Ȥϔʿ¾ÄњЈҪũƁ΄\x84Ì\u0380˅ѝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҙɹҸ҄ƖҗѫɃ\x9fʜ\x96бÔԗ«ŧ˖ҎɤɇƵʾλõπơƼȘªʅ',
                                                    },
                                    },
                            {
                                        'name': 'ȁâʦZщˡЃǊӉӀԆӐšdǫȶЖԕҳϠčȫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            650400.2791761875,
                                                                            998776.5657482671,
                                                                            944727.76835546,
                                                                            -74909.57781631137,
                                                                            593426.8974287059,
                                                                            -75150.89242957153,
                                                                            725098.0082666844,
                                                                            267604.4000020488,
                                                                            361607.6792339066,
                                                                            207611.23120499402,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĭ,Ȋ˦ҙ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:192514.683587:+0000',
                                                    },
                                    },
                            {
                                        'name': 'с',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5121045282646467301,
                                                    },
                                    },
                            {
                                        'name': 'ѓɒʤĒԛЊʄˉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1245909905019910489,
                                                                            -3922436147873657926,
                                                                            -625850374207073801,
                                                                            -9008543126293875025,
                                                                            5770566629915502836,
                                                                            8946446815341369606,
                                                                            5988320043078469085,
                                                                            228099099407926182,
                                                                            4201164131612890681,
                                                                            1271900391584273711,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'R¦Υў\x81һŘԔš¶ĉǅ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:192515.168945:+0000',
                                                                            '20210413:192515.193388:+0000',
                                                                            '20210413:192515.218154:+0000',
                                                                            '20210413:192515.243630:+0000',
                                                                            '20210413:192515.264324:+0000',
                                                                            '20210413:192515.285095:+0000',
                                                                            '20210413:192515.305608:+0000',
                                                                            '20210413:192515.326183:+0000',
                                                                            '20210413:192515.345453:+0000',
                                                                            '20210413:192515.367440:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǐϛɹĞȢфɣӽѤϊҖɯǓϚĉԛҒϑ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            733985.3936936063,
                                                                            -67539.67841564567,
                                                                            451853.1164719458,
                                                                            842141.2807732049,
                                                                            402475.0718759067,
                                                                            80737.7162371609,
                                                                            335976.9917131672,
                                                                            94860.49318662239,
                                                                            621842.2306507851,
                                                                            858793.5676857108,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҕ?»у\x97Мǝʝȍԓ(ĝѢˈŵѯѧƇȕѴTřǋʒѝ˹Ə˨~җ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:192515.802233:+0000',
                                                                            '20210413:192515.823604:+0000',
                                                                            '20210413:192515.845699:+0000',
                                                                            '20210413:192515.866998:+0000',
                                                                            '20210413:192515.888665:+0000',
                                                                            '20210413:192515.910166:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԥͿАʦøȧɡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7731203643013939668,
                                                    },
                                    },
                            {
                                        'name': 'Ȱ ʭǞʕĲӛЌƫǆғДĆЍɮҠҒѳǼǤѹϱ҇',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɈÒӸ²ůwɫϚԦ\u038dͺ*?ʹқΣɆǖԔөϩĻ\x93җƟłĠʦƄϓ',
                                                                            'ɀНŪϖьȁɻԃʇҲɄПʶªɨШ4sOĬҹƺˍəӋΔƨťǧʵ',
                                                                            'з\u0382ǹξҫŁΦľȹξҶ˚ʨфöŹȝӀêźҿȧɄЛiͿǏґˎ¦',
                                                                            'ԜϏƷȁ˄ьȘıԌИМњ®īɒ«ϸ˩\x96ƳľΓѴáɹȎ¨ŒÙơ',
                                                                            'ԢҎɶ¿ʣңΘɶԬʞȢЁ@Š·əˉǯҰȯ\x97ƄƭϥҝŗŃOĎǧ',
                                                                            'ĤԐɢ҅ϧӤВӈԤÎҍӐǂЇǻɲΤ·ʒIƦOɗȺˀӎҘӠƦϨ',
                                                                            'Â\x82˼ƪҢӣąÇʴϬŢʱɤԮĮ&ĺ\u038dɫňbϫеŪ\x91ʝɾ˭\x82ɋ',
                                                                            'I˳ĩΚ#ʽʡСχ¸˧ħѧɰȑˤɚӐǊ\x90ЕƄμȢЫɻ˹ѹʰƍ',
                                                                            'ʔюȐΎͺПƉpȧΪ?ѺϙȟȻμƈƨǶȘɒ˟±Ǜ3ƜӂϼǄʊ',
                                                                            'ōрѡйǩɆ҅ŁǀʮʳƍȾơ³ФΛƉˈɏΕĒĂӞѡʘΪ[ɹÛ',
                                                                        ],
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

            'identifier': 'Пîʳнʾ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'Ȭϛ',
                    'message': '˓',
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
            'name': 'КӋǆĺѬҟԃ¬:ɮԉҌEßûАԬʘ¯Ɲс˳ҧǑßԚѬ˓hҰ',
            'error': {
                'identifier': 'єωˈϱϷǋ1ƻʰӧϠÅҎǛŮА\x99ƛ©ԋ\x80»Ŏ¾ȝ˞ǰơПФ',
                'categories': [
                    'access-restriction',
                    'os',
                    'os',
                    'invalid-user-action',
                    'internal',
                    'access-restriction',
                    'access-restriction',
                    'access-restriction',
                    'access-restriction',
                    'internal',
                ],
                'source': 'ȼŻŷř0mәԨҝ˄IſЗҥҼκƪǬ˂ͼʶ½Å-ρԘϛĆрФ',
                'messages': [
                    {
                            'catalog': 'ͺzşğ\x89ɚʊFɡнƥϼѝđòąПυƋϔΑ',
                            'message': 'VǾɖͼĎЊ˽ǠϼÆϳӫʭѼʰКǔĻАƔȓȈԔōӻɡǬҢԮː',
                            'arguments': [
                                        {
                                                        'name': 'ƵĤȗҜϻĥ\u03a2ŢΖʈӒӸѡʎ\x8bÄwҁʍѰɬʚҒә:ȆŬ+Ė\xad',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'һ;Ă΄ϬĚǫ\u038bǍɌŪԗҘӀ˲ЯɧϷǙġӆφаԝɧвőȅӁč',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3242295832233297485,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȓΡцӅӳЎя',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:192453.474978:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'υ˦¿ɔ¸ӾȠǭ\x8b¬ǘ\u03a2ɃəΊΠҜɌƗȔÄϣºɌëԐȰˠȬѼ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɎǅЩ˺ЙξʂԪлƗξăѶ˻ɘӇCχƙ÷ɦҶȃΕѦȾĉ·µҳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x80MԣЖǦȢ¶ԜÞʛ\x9cœǇџ9;Ϡ˚Ҡ´ʈЍƂĹ˲ņǨԮϪѓ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ОΪșȌɒӅӎ\x81ù˴ŞԒʞʷϚӶǃԥĔƥϞ˯νέƅƚȹĦȝ ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ąǚӀғͺǠȽTȋˈ¹gˍŤϴȜԥĩз*В',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:192453.903695:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɘĭţяӌ˃ȝ\x8eƤ0ϐy˃Ѫ\x8aɧԍ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:192454.006246:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƀɕȸģƈ\x80\x8eʅЕǣ×Ѕ)ȝ˧Ь)ϱʮɜӲ˾ѴċƖѓԜΑҞϤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7515679528198070214,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩȏɮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 857748.2681188011,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʬӮɁ.ˈǏƗˎǪƚZћϛ\x8dɾШůѫʵmƔYƚӸEєǵ\x9bϝЙ',
                            'message': 'È[ŘǳÝȥ˫ӛЁǭΫцŭ\x82ɂрǉķ:ɡȔӔ˶ͷΖҫȫOʆЂ',
                            'arguments': [
                                        {
                                                        'name': 'šԙϡ҂àʛѩӫυзƽ\x8d+ƽųþѫүŖfԣнԥc˼ǅˁŎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŽҳӔƎӧ\x9eÛˤɺǪʼχ)Đҳѭșȳϑ¾X§ȶγmŴˁċϵͳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7172469237385783922,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԜɂбҖ÷έǖŒƅ˪С\u038d\\М',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '9ħԝƦʍԦЛŏӁʫɠΨûöȫlυԥɞĭ,ˆĝʟӊʌʻϴʸӺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 't',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '">ƐΑɰӡĐȭķɾ˘ɧǋ@ǜ\u0382θŐʱӗʈҫϕΓʕǧгşˆΔ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'өƢÃÇˣnԢжпĔСĬшΣҺυс\u0382=ƿǩʯɳť¥ɠKɯϔō',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҙΌ˚˞ӯȔΘLÄо',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǚӿUĻįòΕˠˊţɆÛɖũˮȠßɤ҅YŀŨКĞʃҼ҇ҝҎƢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƊcŝǔOŭͿǁoШЖkЬӂ¨ɜѓcʲǄƠȈͰЍӳȣ\u0382ǏŶí',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗΘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˰«q˻\u0380ç˃ōʸΙ˦ÁψƜϽvϚΦǙό:ʙлӞнӸʄ϶Ĉ/',
                            'message': 'z¾Й»˦ɜYҡЈbăʍόӱҏԌί^а϶ɲēÃ˗ǘЅɃ҈˸е',
                            'arguments': [
                                        {
                                                        'name': 'ƜѡĔĻжӈɂȥλӱͿҸ\x9eŤʣǺһҒюŅQʴӲӪ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3344196770454081589,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѭΏΩɟЅʄͶʃˍǭĳёѫҖĈϲъưȍǜƑɐĴȓґʢɍӒȈb',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:192455.459163:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȍɌğěӄØńi',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 263256.176228897,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƔќōɷƺĠ˜г.ʦiUíËėˢŃ£ʾêʕǭȠѓwХčѢҫɀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x97Ʉͷҁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǘ҅҃ƕŴŖ\x8eхʝ\x9a$ĿȽЊȋ\u0379ȬƤʲ\x99ɗ\x9eà˭Dz',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6329399031550832387,
                                                                        },
                                                    },
                                        {
                                                        'name': "ßάˋ\x81[ӳȿƍǖˑԘʂ'Ҋ˗ͷӿ·ӤƟӞbȤлΧǚ\x8bĺļЬ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:192455.860756:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʈ¡fŁŵő',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӿŕđʼ˪ħΟοDɭńʐкԁč',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϳƗфʔVˆ\x94ˆBϢȠƝΙМȥ¾ј˹',
                                                        'value': {
                                                                            '^': 'int_list',
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

            'name': '\u0379%ɵ',

            'error': {
                'identifier': 'ȏԘƝӧą',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ĤĢ',
                            'message': 'ȹ',
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
            'event_id': 'ϤϪŸÜӀǑҫɳŉ¥ϢɸɨVȊͳǊƒ"šȿĬɖƓĽŋƦǒŻȐ',
            'target_id': '¥ȫ%ҿŧͶǳґԩ˽ˍɅжҪωоÓȽиӉǙѭΨɚùǫÚȷÃȘ',
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
                    'event_id': 'ηҾŉ<Ȭť˻T˖?\x81υI˛ζƚƻüқ˩тÚÝԬхǥĨƻ\x9aǝ',
                    'target_id': 'sϻŋŲѫǈđȾΉΊǗӳǉ˹ėƵëęтôΟƴԟ\u0380ǘŝњпѯӖ',
                },
                {
                    'event_id': 'ʨҢȋ\x90ЬЊљȯƲǀɦƨӂ\x8f;ҲǺõ·ЁˢԘѸbϵȴʶŪЮɥ',
                    'target_id': 'ԆƤ˖Ʃ(ʤvÁĬЫ˄ƇʲĝʕҾϜÿd˥Ƽ¢Ƕϛ×˳ЬǏIN',
                },
                {
                    'event_id': 'ʨȒŸʥɶAȵβ4˂\x8eВҎԉÓЙØǱǌѠσǗÅԛԙŒţgȃ§',
                    'target_id': 'ǅîĎӾʶMƎϋх˜ʽȮҹDƀӰƈ\u03a2ӡƂϷɇ<\x8aʩƔΒЁӇǬ',
                },
                {
                    'event_id': 'ѓ/БѓҎƤǸƂԋŢüį« ŶȷǑǟÀɇ\x97\x98ƪ˳ˎӢŴ˻űː',
                    'target_id': 'ϭԂƗѹȷȚEɽ0ԖɅǋ®ǆƏВǤŁŠɌϫтмѰěǝԄʴʰĪ',
                },
                {
                    'event_id': '·хʃёйѭЕѭ˄ΚɶΉÌˣ',
                    'target_id': 'ŶѾȻǍĤ˜ȎɇǂYɈÉĪÖƕĺʆÝӞʉƈ\x93óԘѪȐǤëʾѓ',
                },
                {
                    'event_id': 'ǸĲδɈаϧϓʟӃĉкϙмNˏВʜ\u038bʱπИôЊκΊǉƛÞVҪ',
                    'target_id': 'ǾԮ¨ѶИĮѽӷ˳ң£ӛђɰͷJ+sѡ*ƴȓБǩşǸӡҾӝɆ',
                },
                {
                    'event_id': 'ίδǣ«ҠǱÙſҝъѷϘʾmȏҸӗ҈ӝ˯ҭԘɷɍ¶ɶəȐуҼ',
                    'target_id': 'ƼЊŁ¦\x8fǽmѝSɾǱĀÊǵʬ5өΓȷǲȓʚíˬӗԆñ˽ƦĻ',
                },
                {
                    'event_id': 'ÆͱԩһŗҒϕőɘ0ЅżҤяʓϠ˵±dоśԋҰȟŔaėӽҨƧ',
                    'target_id': 'ɜǧҎҁҲφ˻А˂ҭBƊԀÕƬԇčҰɞǌȡſ½πƼŬȼ£Ӻщ',
                },
                {
                    'event_id': '\x9aҤҺăǰ:ØʿQƟӛΠ,΅ӑǭɚЎԧɅ\u0379ÕʕňȲŲѲ0ŮĈ',
                    'target_id': 'Ř<M¿ɫăӥԤǼüǉѺӎ¦ҡΖЏ\x96ˆfÝ)Ҿ®ßź\x99uϴϹ',
                },
                {
                    'event_id': 'Ͼé˴ҩӷù΄Ӟл\xa0ѷʿ¥İ˞\x80ϖ/ȷʷŉÈƝϟͱRјřǼÀ',
                    'target_id': 'Νʿ˒ȉлĈȩ6HǖȈ\x80ǑҶͳАвŪ҆ΤЮ9ÂĔԛ\x81ŝР4С',
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
                    'event_id': 'ӷҖ³ɨϩìӔ˥ϪӖΣî',
                    'target_id': 'ԥȣâѢ\x82˷ğ˕ĪÞÕŋɹŧ҈СÔ\x82ʒΉƋϾԙϸˣDҰђȍƮ',
                },
                {
                    'event_id': 'ʿ£/sǫдʒɱόˢÓʃįȾˇэӽǣϺΝїƳũ,ӇåϹƏŤφ',
                    'target_id': 'αЧЄŏˉņǘɾʥøҪ@ʷßǼєÜˇөŠƧ˙˰ƋŽǪ\x9eŕŻԭ',
                },
                {
                    'event_id': 'ʊÜѠҠʍΘʶ+ƁЩЦěНӯԅ^Ѻʔˊȧūў¢ƾñ˷ǻҋƉӳ',
                    'target_id': 'ȶԣӆӦʟ_ìКІӡЀŞБiʑƠΫΠЇʢrăƗǽѨɇӅИЧŎ',
                },
                {
                    'event_id': 'Ƥʺť¿ҵW˝ҍфҡѸѫхɎ_ǩȬƭНӋїзҖЇ\x9aŇϡԨȉʆ',
                    'target_id': '΅ϤΜ1Ѷ5šȒŭɖʍіĦƿǯҵѻοăɽϑšΤǋнјΪϣͺɤ',
                },
                {
                    'event_id': 'ЛȦӛԫθŽ\x81ԓŗɉʽѲƝђˎПҴǗLѻSưêѺɸәЖӳƅ\x9e',
                    'target_id': 'ӉӨ\x8fȻʼĴΰЄ»Ϧ\x9f˦ÏſѼˉǠĲāόӹýӔŽҴӆӘΓĶΘ',
                },
                {
                    'event_id': 'nƵ>"ɑɜĿѐ/ŅƏԮ®ĈγӦΖĬį҅ɧȋ\x92ăŅϚԀʌӢŧ',
                    'target_id': 'žЈŋʠҙÿ ъǊҴȂƊǅ˼ʽơΣЯСŊɾԑ1ȼӀӬЬˆѫȧ',
                },
                {
                    'event_id': "Yˣʚ҉ԅ'z˓ȪȟȷƵƫßķˡÎŤɀҝϭɕÿƥϗ\x7fФȠϥѭ",
                    'target_id': 'ɹԜʌѫ\x93ǘĨЦϮʍǁщƬȔӬǐ«TȊȩӭȓɝοϻΝΡŎѦǋ',
                },
                {
                    'event_id': 'ΘfƀĦ\x97˦ĥˋƝυ\xa0ЀԆɌ˽ηđěå\x7fҩWēô\x83Ӟzҭ"Ț',
                    'target_id': "ӶnĵΜӑŷbǫƐìͰǪ˧ϒ\x94зеԮԕϨ\u03a2'Ѝ4ϗ˚vŹʉσ",
                },
                {
                    'event_id': 'ʚɕƳήǁѶɨĞӯĿԈˋ¼˪ęƁǸ¶˹ȸǗЁдŜȸТˣԟјȞ',
                    'target_id': '΄ЫԖĉĞ-ȶ·ģˆƷҨМǊŘƱи˞Юŷπo\x90ơ\x89Ԥǫª\x9eϙ',
                },
                {
                    'event_id': 'Ӳȩ\x88ͱū »њÔ\x84ʵɾƏ¥ѻӴĥǃŹƺϓÓ\x88СďĴŅӯΧŝ',
                    'target_id': '·ҦнȚЊƮɀ0ɲĚŀӵiЇѮӉ~ǥyǀчпȥƂɃɁɤϨēȏ',
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
