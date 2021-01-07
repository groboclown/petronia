# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-06T22:34:13.712371

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
            'action': 'Iҍʘɍц\xadЎѠßΩ˹й˘r\x9dʶџΟԘÿǮ¿2|ЂŕŖԏǮн',
            'resources': [
                'ͱǏӧuƐ҇ƨҧρǸѹљ҇çȈţ˅nŦǦÌɤıČŒԠиŨ˺ƈ',
                'ɫSɫȨʵƈѸ*˔ǦwҬԔ˻ȼŊˀˌВɝŶӪԆэӗ÷ʚΊЗƏ',
                'ЊˆɦˡîǵϻҴ\x83ÁѐɟʪϤҮТρ|χɿ\x93ǆĞ+ӿǻɛĐÇϏ',
                'Ġăκʖ˼ѡлԒҁѝҘŮ4ěλҧȠƾɥϔƻûăşƅ4ȁXԒĿ',
                'ƵǬσБŚϬ¿jԤǿ÷˛ÜȼԑƑͰһH',
                'șӺпȋҍӅƵдҶΠӝ\x9aӬ˰ȁ;ƿˠаԦŨѹ*ϺūèīǔēË',
                "ɕ#ή˹ǵ'˦ƸO\u0383ӆ°kΰ\x86ɿʀӹԠŒģʕђНϔƑËŽŜ\xa0",
                '͵ԡџɂ%üéъŧȶǎ\u0382ҪåøåȂ\x8d\x90ĻгʯѡȦϫĝ:Ň\x89\\',
                '˞rӖɄÛʵӉmDɠ¯%\x95БÌʟʬЋЀŦ˱ǒĠΞ\x84ɫ϶ŝ½S',
                'ĚǥˆԏɎҪ\x9bΚӣȉӸұÎҶ\u0378ɔ\x87\u0382ӴϾ`\x94ςҰҹɱаǮģк',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': '\x9c',

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
            'identifier': 'ɢĪҮ3εҦˋȧ~ѷ~ĉªРѭϯзѾǯͲɢǤʅІȵŴ°ХȭJ',
            'launcher': 'ԁԃ˓ĘȜŘӃРԮvΖːȥŵ˖ԏɁɠȓƍɞөҪȽʷȖ˩Ň˧ʳ',
            'permissions': [
                {
                    'action': 'оǸҰυҚӒzǫǾΌ΅ÆťͰĢƕΊèˤˍӀ˳ëŁъȠ˪\\ȧŌ',
                    'resources': [
                            'έЯӝɛԫϏˮҪĹâҟԒҠÙͲʛЦү.jͰҮȢԙğІҐΚʎŊ',
                            'ш\x94ʜЪɂԡȭ~ујρ.ÌσΨξƝФŴ\u0378ʄӤǵɫ\x80ϘɘӉƱϯ',
                            'kõĳˎ˨ԩԔҧыųξƘĐѽpЌfҕZʝ/эʞ΅ȂǿӫʖKƘ',
                            'ßЦȳʳ^˼˺ӿȷǤΎ\\¼ԥȂɆ6ɚȽĬēΓǪϘЭ˨Њԟ˖ͱ',
                            'ώѽɎԓĎТφҼˢӠĳƻӻǲUˊǇҙɨЧѨμ҂ƧǯϜƐԔЫǳ',
                            'ЬˬǦӰ9\x8bzǁóyŏвҊƘ˯ƃŜϡ\u038bӤbcȌaǜʤЪʯψǴ',
                            'ѥɯǍӤaѶҫҲҁгƲͱҦźϺҠГȄqϣɵŭӢζӆĝŖʰӷϺ',
                            'ƲƼǸ\u0378ʙLǇɃ½ʾԈȏԀ\x9f\x88τɽ·ńŠīқҠЄԝƒ:ŕĥı',
                            'ҵ·ǍШͺмƫҩ^ΰѰԬǨĎłĖɻӯӞφÆѥȉÛúӖEγҁѻ',
                            'ʉȂҎɝɟө½ιŤзѰԤǸҴʔÁѫХɧŖʛŃ˨ВŊκцņϧƎ',
                        ],
                },
                {
                    'action': 'ӗŬϲӕ˶Ϧ¦ЉҠԈΆҹ˳ȽûôϙŀӫUθǡ΅ŘϜäӧɰєЕ',
                    'resources': [
                            'Ҍ\x9aьõԜz˖ɀəĜκʑɱԄǨҞРіĜφγӦɝˣӔĵѭˍΎƊ',
                            'ďшˤ¶ˁ×ɯђϦÐ5ÕӢŘƽļκЕҕĬκʕΥʒřʔӼñҋҸ',
                            'ҥЗ;ũ˦ћϒȭǁʫłóɨǀéϽˏıюƥӐƾɣǙғ°˨Тɧǔ',
                            '҆ԩφŢɥ҃ƫʞŐŢЁǹȸŁˏӋʪɿ˺ӎʰӺ҄ȏϵԭԮːǼЈ',
                            'äϾĕжʹҶԅȐѱ\x99˙ņŇǤϤ=˗ɊʍѳyоϣƩÅŠOх%Қ',
                            'χ\u0379ȋȡhŠ҆ǅӿѳʕZΏɆŤиӰϨ˹ʇǧÂЌʘ4Ř)ˍъŭ',
                            '2М\x88ƬɹӞňÙŽӑʘӿlſӳȆƸ˚ϿǌЦĲԪЦ^оӆʆǖМ',
                            "Ҡ'ԣHɇŦɮƤ\\tӠƶϫӂȳĎԊğɸ\x9fȾƒ\x9d7¬®ЙğСĦ",
                            '\x94Ȯ\x82цƄΑôʪοȧԞҬǜɄԆˀÄҾƗгŪΨAʽɬЊтʁɜȳ',
                            '϶JӏϹҲÉӏφѾłLűīLʭԏȡњƛċšʴʛϮҷѷѮǸРҰ',
                        ],
                },
                {
                    'action': 'ëƽΥȄ%ːŝ҄ϼɎˡĞƂŃƞӦԛяʥÇԋÆάŸƦб/\x81ˊÚ',
                    'resources': [
                            '²yϏҕԊ¶%ΗӆρM[ӒŊǫȁƾŮϩѲϯˀʓπnΛƼΒɨΞ',
                            'IѕСĆáѣMǄĳʊ˓ҟѬȪʃϜѫƂȊεŌҁԍɣǗһÄѠ/З',
                            'Ȣ.ōƾͲĸΕ=1ѻԮώx˲ӒѾ˔ǺƶëμÂԥ×\x7fώLȝҹƙ',
                            'ɍŌʒӭƎʬΟÌǀύCӨƒũɹҐχԮÙƏǽӵǁůȒļЀkӥ¬',
                            'ȗˁҳƯMЩɏ¢ѧИǽΕӱӓюtѴг]Ӧдϗ͵ѳƒƫGnҿǚ',
                            'Ĭ҇ϏӒʉɩϕұð˽ҩӆòɇҀͲΖ\u038bƌȽçÃĔɥˠɧǳл¤Î',
                            'oėɟчǄǸěɟϧɑǷ˒ЗƌϯѦ\x8cҰςŋʫǚǁ˪ɰжǒĹӫˡ',
                            '`ˇpŴĪ΅ŃҸуƁȗǽЧӲčҢͳċ\x81λӳҨ»ҟʹȠ\x8bϹӭé',
                            'Ȭ˞uϥǥϠmĆ˭˻vƋϸʀϒАÖɱǯҐɯĀѬӣɳŉʜƼ˂Ӡ',
                            'Ԅąѷ¥Јüę\x99ɓlǋϲŉƏʗ(ѺʷΏҮӨ\x88ÃŝΚɨԂоœԥ',
                        ],
                },
                {
                    'action': 'ǜɰơͷєĈçõӹҩ5e˺[҈İ˱ʌkşȂóћ҈ʪ\x94˧\x8bϗȮ',
                    'resources': [
                            'ь¿\u038bҤ˚ĹǁÎ˹ȎĔҖÊĽțӘȢΎĽƉŇ˚tжѺ^ԢɤƱѥ',
                            'βΘwԏɘűйЪɹƮϫЗϲȚÜɏƢ˳ǓҔϸˏпǐӃӑǛſɲˎ',
                            'ƴϷȶqʁʸ\x92őԢ΄ɑўЪҫԍԀҐÂȕêʢϯŲΆӧƗтΌĭǟ',
                            '\u0378Ѻѐɔʩӱ˩ê\x7f¡Ӊǅťʾďƀ\x80ũҋǣωóџħȯτҒɒĊȫ',
                            'жĭӃĥΥϛmȺɤ˶ĜόʻŞȼσVEŚШиŀȷԞÿ4Ͻ!Ĝѻ',
                            '\x88ȴҵшΈįȩѓĒ7\x8fәɿŘÚȰğ\x99ŕП\x84ΎЅɾҸε˗Ъӫɕ',
                            'ŮԒԝϻtƍ1ЩԦʹћěɷˤŽΟwζƮɫąЃľЅDʁԫ\x8cƑů',
                            '҅ȐůƂɉϛɾȞ5εɘʕƀŅӎҶǜ\x81íǞЗȨȓƣҡwέͷƱя',
                            '¾ʣӗμϓζˠӟŧӊʈƠϗӌЩǶƓʑѶȢ˖ƣԈӹŵѐʹǿƤԨ',
                            '˝ƋдѡȵɟąͶɰ» ҅ԗԥƠʇǰ¹Ͻќȏϰɉç˝ÃяȵǤҀ',
                        ],
                },
                {
                    'action': 'ѳӱУӎÔъȿ҂ȼƁ\u0382Ԃϰƍ',
                    'resources': [
                            'ĥʊeċ#ȖØʵϏгϲΔƦҤҐѾȿ˵ϋЖ_Ė?<ȌőŗѠǵŝ',
                            'Ԇ˵ƉɃ\x81Ŝѩ´ȟ˓ӑω0ƷΗ˲ԩʙƓʔʼτΙŝ\u0379ľŶɁ,\u038d',
                            'ɿаɁϩЧ#MχԢȏ]ɔϺƫҴїϹsɀŔEǅǯǞJ¶Ӣɏѳˣ',
                            'ʷӞʌ\u0381ˡϒq\x84ƯɟɊǸ\x80Ҕ',
                            'ǜԙ˥ţΛҳʘŠǹƮѝɑYοúϯÀšþфƄБЦýɻď>ţÍѐ',
                            'Ϩ\x8bȥĆƱԙ[˜ԩšȦȆѓӀʛӴmMХ-ƨϖǸ\u0379Ӷоʑň×ʜ',
                            '@Îȡ¥}Ӥ¥ÀπSɭ\x82ǜӽ\u038dÔѨë҅ҋĖчӖĮŇ|ŁG¯ű',
                            'ӋȷӑȐ\x95ιɤҸĒɏΦԟĦ\x8aɽƆоʰiϟÑΊʰ\x80κƅӡҙȂμ',
                            'ιŲϑǇѠDϭɄԠɠҚ6ȖùǡƦњŊʆeũ΅\u0381лԃɌйɟ˧Ȝ',
                            'ΡҜɝŉɍϝƷǼŒɛnƑnƱϥ˦ęǀʙƔѾȤπơȠËИoP\x7f',
                        ],
                },
                {
                    'action': 'ƚʲϦҵ\x97ŢÉͶŲϋο¶wνŻҞ\x9e\x90łƈČ\x90Ä\x95ʻ+/¨ĕЃ',
                    'resources': [
                            'Ȇ#άԜǗҐ1ʛЭąiȑ·ſѵͱĠʭӎ\xa0wҒѫʃČďˇ©Ӹć',
                            'VɇàɅȖǺЍӾΑԑ˘҆Ġ\x81ø³˄Ȣ¤ŖԀď\x99ȸŹЂʐǒǖȂ',
                            'σшőŐЬâgКУʁϛӀńǈӑþʙǛȹΝѠȑĭ·Ĺʃɚþ%ǘ',
                            'ǸQĴ2ԉ\x97ľ·˂Ϧ$Ů]ŘƄτϮεǂƻ\u038dŘRϬʥȰѩ\u0378Ǜҿ',
                            'БÅƺͷŚΩƞ˨ĸ˥҆ƃͳԖɤě\x85ʇҩ҃ЄЍȿʽƮЛȍ',
                            'ʢԋҊďґѥУˈьȿ˚ӨҢŇĤÓ҂ԑκɪLςƖπ˜Ȗ˹ƧГm',
                            'ɚӜҫЊ\x82Ƶӛ˻ßŔɻρÂXүЮΜ\u038bɗˑȧȟ\\Γк˜\u038bӐĘr',
                            'ϨǾǆʺеŰľ˵bѬa˹ʻĤʲҶāɔ˨2ƼkϼԠȲÖʒΐǵһ',
                            'ƽɄĂřƂԉтΑĝ·˖Ԋөʩ¥˷\u03a2ǽȏ¦\xadɱưмrǕˑǦӥf',
                            '˱źsíˊ˪āШƬϮλӁҋǏѭҪǒΉĚЗØϭϢΦǐƵÐĐȫɄ',
                        ],
                },
                {
                    'action': 'Ȇ˕ý˙ƺǴƌʠʾԃ¥˾ǝʙʼCɷ¶ȍΡǣͲñɨҶǲO#5σ',
                    'resources': [
                            'ǱԋѶʚǇʒæŭǯѸӝϲȫɨ\u0379űƲ\u038bƒҭԙԉ˰ǦхōǕňȁʞ',
                            'ͼьůɂɬƟV»ĒЈɒҫ\u0381\xadźƞȊˍ˟Д¹lԨўĦεȻǘϮɢ',
                            'YҨЭЃЈƍAиGōЫӛ˃ƼŋҢƢȐҿǴԃʻԥҟȟlɐƤrȶ',
                            'ǹʙùΚʛȥҗȊҦF˱\x89ËѧĸϞόê\x97®ƾɶΓZΣMŖÛØǿ',
                            'нʬʁã\x8c˼:˯ƤКġ˵ƤʑȦÄϸȊӑΔƂóÒʀ1ѰþŘėȔ',
                            'ǎɭɶžώɦÚyȮ\x87X˾¹ÕŠŃʛӚĞ\x96˰ȡѤύ¼ҼѡФ÷w',
                            'ʂΚȔdɣͽǕɘRϱЈ\x8aûėƌҤҢю˻ԦɓàЊΎƳʡİȼ8ƽ',
                            'Ӟͽ¥Ɨџ˓ȑùӋŏќ`XӰǿ&ąҋǯԩԧԕĉӏĽҀӖÆȪǼ',
                            'ǽʈ˷ʹеÀƓŊũӍŘƱӗǔΈƾˏǤϖèÈЧɊYԭԉѥҖ˾ǣ',
                            '4ӵƣϾΕşĄϗɣѫgĬ/ȧԚΤǎκӍĕ\x81қĉǃԫԝȹʺŌű',
                        ],
                },
                {
                    'action': 'ΝǥѪ\x9cѩŶƵNˢӅʓìζԦɹTƮɩо\x86±˱âϳĺɚ\u0379żƳĀ',
                    'resources': [
                            'ĽҶйƟΙOζtшɿëŐ҈ȍ®kӟӼÇ\u0380ѡǄϥц˰ÇΗѧĻı',
                            '`Ǽ\x88ϩïŠԔҨˣπĤɳʚХӎʃʰП»ùӶÇǒʶǦʰŶҕűΉ',
                            'ǑEĚƸӯІϨhҪ®ҠЇӔˮСĪȭѽȢό˻əɚȚʀϩǣԉφr',
                            'đά\x93\u0381űͽӒȕƳ»ʋÊİ϶ԫȰˑӖÉΙѕӬɫ¨εȷԠɊÔŗ',
                            'ҿɤĽɠʅϻԃCɻxæҒȐʺƂˤԧ¸˩КЙǏҍ\x8cʸΒǒЃɚү',
                            'љ¬˧ҩ\\´ŃԤļ˥l?˘ϺĞːÙƭԧ҆ʇ[ǙĂƘƷȻʂ˘Ŕ',
                            'ʽƨʹʢѡǭŖcî҅ƌϐѧƚ.ȹƳ,ϫʍӫӤʒ"ŷɏį%ϥӟ',
                            'ǜӓиK҄ӄ\\ńϧ˽Ǖѹςϧκ˭ÇγɋϘĂӄͿeΘΟȣ-ʅǈ',
                            'ŋүŵĪӸԒɎҋҒŦȺˌ҃ӛī˝ӯǻȷɍÆψȞǦϒʨEƆ"ĳ',
                            'ĞŭŖб˲īʶŅżӏΡĎӱǃOҴĢ8Ќȯiťɣҹǩл¿ǙɚϬ',
                        ],
                },
                {
                    'action': 'ҷƲɊιӋ˝ұɮQɮ',
                    'resources': [
                            'ʏˍʴ)ɭʰϘͶ¡ԭɉǶĩΧʑ˭ЦЁҌʍЬµѝςƄȖµǎԭШ',
                            'ħЩӗŬ&ɁÌrȜшƁѸƈЖ÷ҙψʿӼԑˡěĚӭǖȁǔā!Ì',
                            'ʘѹÿԑŏŘǱƈѷțƵ˾³ϳѹĲά,ͷЅ˄ӋԃиʜͲžӤʓǱ',
                            'τƏӢŏ҇ЗѕΟȆʗҏΘʛұŕѭϞσӭѝȶѴũƄōĿ˵Ő(ɕ',
                            'ӣʸМԬOˮқщßƱѺšpҵìţԩǳЛŬÕӶĞƎ',
                            'ȁɘ҇ \x9c\x84ÇōǠҥ@$ͺ³£jĢíѠϿБŘʐӹ5ɳɢëҁě',
                            'ҤЁɤԟǖҰg,ΥζÄʳι˳AŚɽΙʠȚȟʃɆ˙ÝƦļȋQ|',
                            'zԅȡɑʚ\x93ɦƀ")ŏγɗйĵǍ\x80ū\x9fϮɥǐŹИ¤]ɒģďƪ',
                            'ѩЎˮνϣȆC˹ȴ˓Ø£Ώ\x99щȐӤÿˌһ\x8dN˃ȾĮɬǁńœҘ',
                            'þҰ\x89\\ƆʽѬΣϕƒӧӧ˺ИƶхãÕʂʧ҅ʬ\xadƾǽЩΆ#ϥ~',
                        ],
                },
                {
                    'action': 'ɌȗЮδȢʺƴÎҰНόβϲÚ©ţϱ˭ӡƑɞѲǡ˗ǿѕϐƽ˰Ċ',
                    'resources': [
                            '\u0378ˏ¬ńʚŀÒŊÄѩNǛŏĘƿɺƑ.қĺΡëΉϭΧЊˈҖϖ˽',
                            'ӈґҜТЛƢġĪłәĿȆʛƙĥ\u0381ťԝaȁĠɥƼҒˉ˵ʳɋRȭ',
                            'ɻŻôũЬӝ+ʪҡ/ЁȓǔφƍϦЃŷԈʡˮǅųǿЧŔЦлˢ}',
                            'ѺɜΗԄɢЁӍʘßɈǓʶ¤ˆâσqғʴӹŧǃщԁ',
                            'ʬΥ҈ͼǎÃŪFƦǭλĻ\u0380ϹğśϭΓãӆҫŝ§\x8aԭ\x86ʏ4Ωѳ',
                            'ʊ\u038bԛƊǔÔӆȍëȬȬkÖĆ˝Ϟ˦Ϭ{ˑȢӜӗϘÎүŌŻӒҁ',
                            'ŕʟ˘ԅ˔ΗҙɇʬȊŶϗĒʸѕΘΦº²˚ӖȦӨżˮŹԃϔѴԩ',
                            'ĭƳϋΊѴϒы\x9bƭϟβvȒɥӱϟ҆ԋӽѲψ8Ŝ\x9c\x7fԞԠіʔд',
                            'σѫά\x7fȐЉƼǝȷʒϑ\xa0˫ўĢϿԨϔűʞɂӓìҋȭȍŊЎѫҮ',
                            'ӉʦpɤԟȩʕƒūƗ\u03a2ɹԠ\x80ΠҡiԙƔRѠŹԧˌěχǝɡɛʖ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'αвʔ',

            'launcher': 'Ӑ',

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
            'identifier': 'ӺʷΤҰĉʜƥAʩ˻ǁ\x8aνϭЖʼDȥŦиӲУх2ӾǋìąƍԔ',
            'target_id': 'ǻěˇȶÉdřĲīӮÀ¾6ԊʜзҙɍӶɫЩ¶e\u038dɦ,ɴԠǠΡ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ç5¥',

            'target_id': 'üԋLЯǣ',

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
            '$': 'ҌРǛŽЛǰ!ȩʼĉϥǤЭќ˲\u0380ʲԜŌРӳϘҥ҂MƯԛǔӒӱ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 1349974919618860744,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 297804.9172974202,
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
            'identifier': 'ƹЃ\x83ǼcԐƊȨƪʥѶŦԔƾӟМ|ɪ§şȐˋ9ѠӔXϋʏԇĐ',
            'source': 'ӕ³:ˈqɔФ\x99цѺˑĘǼҽЧс\x89Еˎ+Ϛйˑɜ÷ǲɝСͰª',
            'message': 'Zζ±ѓŘșЙϷмɪҿɦКҲ·ͼǑӰ˞ŊѢВǝʤ͵ΑľҲʆƪ',
            'arguments': [
                {
                    '^': 'string',
                    '$': 'ÃѾϧϦӼӱ\x94˓¡ųˮϿʪрǁ\u038dζ4\x94ҹëʶчӓҾĖw\x9eȐх',
                },
                {
                    '^': 'float',
                    '$': 362358.0531966009,
                },
                {
                    '^': 'string',
                    '$': '˾ʝřȝҔŊӵ˯ӰÌϼԄÅԘ÷ӡ`',
                },
                {
                    '^': 'int',
                    '$': 3327719985630283268,
                },
                {
                    '^': 'float',
                    '$': 64566.54322511298,
                },
                {
                    '^': 'float',
                    '$': 560912.2458593966,
                },
                {
                    '^': 'float',
                    '$': 176175.44632497767,
                },
                {
                    '^': 'float',
                    '$': 958948.1496878383,
                },
                {
                    '^': 'int',
                    '$': -7894432989770888679,
                },
                {
                    '^': 'string',
                    '$': 'ń¿ŚѺҵΪ]ʠεĻԔʷҶӸłȸȣAļӋǎ˨ЇӅГϪŘɳĴʊ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Ŕι',

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
            'identifier': 'ǔӏȜĵĦĿǧМϬˬȭˤ˦ѮԥvҊСϛpԃmί-ȺӘˋ˰ĔĹ',
            'error': {
                'identifier': 'Ġ°ѐƪľЃђӣĒr0ǱĭΛǱѶӀӖњĝ˗˕ìȖĥҵ˞ϗI˭',
                'source': 'ŁȉvƔʄΐ¦˙\xa0Ϭ϶ĶȢMζΑȡˈ\x83Źȼ8ȰsȻ˩ɂʭ=ξ',
                'message': 'Кưİʾ\x95ɂ˧ʓЯͰƂύΆ˂yƗϙŖķƒ',
                'arguments': [
                    {
                            '^': 'float',
                            '$': 627192.6587608452,
                        },
                    {
                            '^': 'string',
                            '$': 'ħҡŵӦԂͱˆʟϱÙȻχʦԮ˻ѿϜ\x90ʟǳԇŭŰґ\x88Ǖ\x81ӬƜƀ',
                        },
                    {
                            '^': 'int',
                            '$': -1848048816419944798,
                        },
                    {
                            '^': 'float',
                            '$': 931071.6271904417,
                        },
                    {
                            '^': 'string',
                            '$': 'xĜ\u038dϏʶʔћɧ²ͿǐʬȉÜĶԒдˋťÆʇ\xadŧƇçʘϥз\x8eĝ',
                        },
                    {
                            '^': 'string',
                            '$': 'ňʈδŵδɟƯȀıǒχèƲ¤>ʡǮѠ&˶ԚлϝĎ·ǄĠǡáĈ',
                        },
                    {
                            '^': 'int',
                            '$': -4730131460947244532,
                        },
                    {
                            '^': 'float',
                            '$': -92395.34464984758,
                        },
                    {
                            '^': 'string',
                            '$': 'ɾЭўĉʚƗɍŲγȒȯȏѬбϑԁǆ˩ΤñѝӖӉðη\\ėȾϙǊ',
                        },
                    {
                            '^': 'string',
                            '$': 'ʞ\\ŋʜĖϿˬJқѬʪĊ\x95ͽџŮ&ĜӍӌ˭\x81®Ӭ\x9dо©ȻіǄ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ŗɷ\x8e',

            'error': {
                'identifier': 'ѽӍ',
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
            'name': 'ɟџQȥƑψʴĈԒɃȢѺήӭЖǑÐƮ˴Ѐǣ-ªЇѻ˕\u03a2ÎϖЮ',
            'version': [
                5059224406953462424,
                -5339128947697156472,
                792399985556379321,
            ],
            'location': 'οV˱ҹ\u03787ӂůιâЭȆӖĄ£Ѱ\x96\u0380őɼƇƬĿɳ\u03a2ǲŬҗ\x91ő',
            'configuration': '\x81҈Ƹԕ¦Ω\x89Cȓɉѵ˫҈ư>ЩλЇˇ¤\x7fĳ\x98ËǂϺɆТ˼s',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ŘШ\u0379',

            'version': [
                4997420549851045793,
                1595959416025061614,
                3555111852656735701,
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
            'name': 'ϖĀSȂˊ©ˡĮ\u0379яɚŏә¿ʵѫѪ#ҠуʭŗŦȸìͽđɮŤĚ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Č\x87Ȥ',

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
            'name': 'Ǹȸ Eĥȶåˌ˃ȉҕvͱхƒԠΘȺ6ǜñӨ²ǇˡѨϡɔǃʍ',
            'error': {
                'identifier': 'ё˪ȟ΅ŦπыǗǻdȰDЩȐĞаȘҮϩǛфİ3ǞЊ҇ϷƽԨǡ',
                'source': 'ľ\x82ĝǏɰȄ\x9fŧԜÇÖʸɒʡп\x83ǋђσæŵȲʽǻêɶѦѣ¸˫',
                'message': "LŐ'ÛӬӪőȦ&ʸҢҹˇȫ˞\x8e˞ÝӸƕʖșƫĎʗѠƍʡŊ~",
                'arguments': [
                    {
                            '^': 'string',
                            '$': 'ǡԅшӪҊªΆ+ԂӅ£κӏeˌ˒tҊŠǬķԫѹɊɊ\x81',
                        },
                    {
                            '^': 'int',
                            '$': 197197218868756528,
                        },
                    {
                            '^': 'float',
                            '$': 531703.3616000909,
                        },
                    {
                            '^': 'float',
                            '$': 848299.7704181867,
                        },
                    {
                            '^': 'int',
                            '$': -3634952705150586846,
                        },
                    {
                            '^': 'string',
                            '$': 'ҰӌnÅ˨\x93HȂɢӼ˚ԀгϙǫѴłŶ˯ϳВɝō˛ŬϪƿǺҵҮ',
                        },
                    {
                            '^': 'float',
                            '$': 987968.5876148576,
                        },
                    {
                            '^': 'int',
                            '$': 7700785142997227829,
                        },
                    {
                            '^': 'float',
                            '$': 269638.3265357361,
                        },
                    {
                            '^': 'int',
                            '$': -8131909630795583182,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ԟöǎ',

            'error': {
                'identifier': 'Ě˥',
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

]


EVENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'ѓ¶YƤƬԄѓҋԞ\xadҶρȷŋɊΎӆѪΈNŌЖˎξΑʕɟıʵ¬',
            'target_id': 'ˌԬϓǉӓʮƵǙ\x993Ď¤ҥΒȹ˕еƿƸȾӈű˺ɖɿщɲģԢѢ',
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
            'extension_name': 'җ\x9b˝ĸƁ˨Ԉ!ɢыЫΦŝûΌâƇÂėӟ.ϞϿԞ˓а˛ĝÌĸ',
            'events': [
                {
                    'event_id': 'ҙΈěɵɫɝUϨƼÇϱɩˊΟŐĳg/ƌѹâӫÜͿgΖɧŎþұ',
                    'target_id': '˵ǳÑʉ8ԃӿ',
                },
                {
                    'event_id': 'ǒΟ?ξVCʳǈɈȖ,ʼ+ːχü3{\x88Őͷ0³ʳô¹Ưˏ¼ӈ',
                    'target_id': 'ˠúȽŧCȲˏĀʪsƳȪŹěȴˊŶȶӤΛAʧΊүʐFƖ"ĉŢ',
                },
                {
                    'event_id': 'òŲŘƽáѪ\x9aвɣęhŧӡáȅȴɵȵ÷ˌ¬țԪÁ\x92ѦϬņvȤ',
                    'target_id': 'άӛџШȲϋΧĝԣ˘\u0382ñʪіϐɋлÏǍӕ\x82ɱʠɊԥϷǈ',
                },
                {
                    'event_id': 'ĜɺȌ˯ѸѝQԭϊҦϺȇŖĂΕʹǷӣѤƍнѪǠʃНVӰͺ^ҁ',
                    'target_id': 'Үԏ˸є\u0381҃ʙãĶŜȾҒшғ+ʼ˫ЎʙƆĮɊoϭȜ\x86fƚăȣ',
                },
                {
                    'event_id': '\x8eĩчʩ<Ϯ0Ȉ\x80ԓϹЈŘΊÇŁςƦϑƗԐ)ҡҡɝԛǔɛŰђ',
                    'target_id': 'Πɡ9AŪѭЧǀʾѼƎďȂǌpŮĥɚɪɕF\x9cÏʅόɑ˫ɻή[',
                },
                {
                    'event_id': 'ż1Ӗ`ÀȰʥĝȪϛʼ҆ƇәќνŊʦƢʴͲŦГςmÍɎΆď˳',
                    'target_id': 'Ɯɖ>˛әŔмӪˤýȇкΛѳќЊĪɕʹѣцǦaď\x9eʷЋŁƆ©',
                },
                {
                    'event_id': 'ѐĎǦɨԩΝʐ\x8dRбͷƿϏ˺ϊÆvĂŸΧӕȦΰ˼χDĹÔȏφ',
                    'target_id': 'ґϱ ǀГũŮʹFҵӻĖ˃Ǥāԩґ\u0383ϗԄѤўкԫ\x98˂óҏΒˣ',
                },
                {
                    'event_id': 'g˂ϰҀ΅ʦɃнņŴʩћȌЗϱΙжƸŰќǪӴ\x80ƐʈҊҶ\x9adǭ',
                    'target_id': 'ðɕėN_Ǽ\x9bǾŠ¨κÈǡ\u0380ЂԎѣԈоĜνɷ\x8bϗψ˞ÊʥȖИ',
                },
                {
                    'event_id': 'ȝ\x88ʴ˓ʫπ΄Kѭǹáƍ\x9bɘϊз`Wʛҕ·ʠȳˆКʸІΡʅϠ',
                    'target_id': 'ьӐńɂǞЭЇʲҳ=ƘɿΉĵϸˇ˱ŎƧēϤįɳǙԮĎҸ\x94ϛȻ',
                },
                {
                    'event_id': 'Ĥћұ\x9enƽƽƶΒͲ9ԆĠǚŋЛϣȪѿӷǭӞĳώƀƳˢ\x91ƪÔ',
                    'target_id': 'ϕȇQvԈȧфͼ\x9cç˙МЪΤˍҐŬZĝЋͺċɢˠêƝɐӡİĄ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': 'Ȗ\x9aѯ',

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
            'extension_name': '˺ˠôɦæȵҩ&jϳɿ˧˫¡ӋȥԔģҽѝʸʚͷɝųȈġǔӹA',
            'events': [
                {
                    'event_id': 'ɓү\x87UͿÅn˥7¾ɹōѺTƅħӞʘȧѭӰљӰ?ȶƪˢȉąǐ',
                    'target_id': 'ϵҴΙөĖҦӜҙԨʖđěȚȜы«ŽоӾ\x83ԘКXҤíΔ\\ȟɺÅ',
                },
                {
                    'event_id': "ĢԚʹUӿcɿЊԌƭõæƅөҸðy¿·'ƂѧƲǙĂфˋѪɳȹ",
                    'target_id': 'Ϟԥɿʒ®Ǉ\x9fǀřҤЯǨ\x81ʆХϾ\u038d"¿ǙʹέӴӉ3ǓԎMҸƫ',
                },
                {
                    'event_id': 'ýĭзΡ@гсПʢт$ԣѾêĈ˸ȫȕƞѐćƱŅ\x95ʥάeéԌˬ',
                    'target_id': '\x86\x91ʴо³ӄɝ҅ʔƨî\x94ѦʤʞƮɳЂ¹ÑMωәƚÐǽȜӬȓː',
                },
                {
                    'event_id': 'ӮΣθ\x7f+ύȺɭÍ',
                    'target_id': 'ʒϯÉÁ¿ɟԙ³ԂԃȯɗȳʞĀϯӦǰЦʏϣǲ͵Δ˟ŴҗǅԤș',
                },
                {
                    'event_id': 'ƔȎθҚ˰ҮϿͷɫӾѣ·ǇŬ¶ɻкǗîƶoπÉԊȣŘȜҷζŹ',
                    'target_id': 'ơ˹ɐî\x7fÉuОԖӚɁ:ӜѩѫóŚщŃ\x9d',
                },
                {
                    'event_id': 'ƥ;ǋ·Ϲǥ˔×ȇϐΕēȤ\\ƜŘřʁϧƃ0ÙƄӒƤѯϛAȽ˪',
                    'target_id': 'a´рѲπ\x84$ȎÓȂ˓ʀҝȜǒĿħβǇ',
                },
                {
                    'event_id': 'ˡɌЗҩza˖Ўˋ҇ɤùϚҊӜèЕƿЖȱɪЫϯ ¡ͷQ7ƒɐ',
                    'target_id': 'ȬƕgÞŻԂЇӲʚɽɮǱfΪƚ\x94ŶťѠɷ°\x90ʴƩνĂĄūƲо',
                },
                {
                    'event_id': 'ɅЇΪˬHȂȀҟίӬ\u0378őΰűņ˒Ѣ=БɫƗJʊ\x94ǂЬǩҷťʤ',
                    'target_id': 'тTȠpċÈ½ӺϷĐϱȰʉɔƒ¼Ƹҿ\u0380λпΰȲ˽ƝÙ˜άǈѷ',
                },
                {
                    'event_id': 'ġΒƕ˪șŪʊˁ[Е\x9fӕȭǠԔʫчɅʺʷӔĪӭǏԩ\u038b6ʱЈˇ',
                    'target_id': 'Ҩ˰ӺӻҷѿѬВϺ\x88uΆΐʿͲϒǦȱųȆkƪ\x86ƇóGӹê˳Ǫ',
                },
                {
                    'event_id': 'ɉβ˜îȣӣȨǦŸԟыŪǈþˡԙ΅ɶſǳӈЛ\x9dűԛҷɕ[ҶΠ',
                    'target_id': '˸ƙʻ͵˃ĎӄĢϖ϶ÁзѠˇŮ˯Ĉȸ×νҬϗYȚÜǿЭˌΰӌ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': 'ôɁџ',

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
