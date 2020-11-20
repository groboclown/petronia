# GENERATED CODE - DO NOT MODIFY
# Created on 2020-11-19T23:28:00.563259

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
            'action': 'ɁDɘϤˆō7ϣĶˎʝʳŬԭĭǽgʼ&ʼώ³εϷпʵɟ˒ƐɄ',
            'resources': [
                'ɹһȢ˾ϗǣUςR\x80ĂȀӎɪΊҧӗΈƹɱAӭÿƖ|Эұ˶˼ŋ',
                'ʯʻƆ҅ÇϝҀŅԔВ\\˯Ӳăêơʴ\x83ѿ\u038bˋÓ\x96ŉùӶÉȺǙȸ',
                'ñ3ʜʎџüĥξʮ\u03a2ɬǅĠ҃ˣɧǉŋĝȻԈύȬΊNк1Àļџ',
                'Ċ˩ÁϐӱŹ\x82ʷŚӃŜȬřʭĜĥҨдӡ@ħƒƜǢǕԍԈòʼw',
                'ľzʣɊң<λІɓȨɓӊđѠōmùʢӹɴcэɓκĻVʕиˣ˭',
                'ØŷјИƩϹʖǖǳ\x97ʷнÙȚŷІˍʼϐӺ˕ƋΉѪŋс9ΖƟ˴',
                'İșӷʉȾ÷çιŋȣ¨ñӈӯԥΘηƙÒҠñöĥɠRȩºȂġԓ',
                'Ы\x94˝ίŴ=ˉԡԦ\x86ɅY\x95ÞȊΖò\x81ńÙȧÕѫŷҴ˃ʅɐѓ˔',
                ' ˗áɟҦ\u0378ґΧJѫÄ\u0379ϢƧзӸĥфǣПYĤɷѕҦʋŊѤđг',
                'ǡϬǵԋȠǭϥʓѥƎҖĢƉӊ҄ԃ˕ҶʍљԇNŹNþέô\u0383Лμ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ө',

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
            'identifier': 'ҶҶԙΡĠĜ\xa0ɺ˱ϊϒɼҐ`ʥǮȷ',
            'launcher': 'ơЉľŌѵģҤώ˷Xɫӑ',
            'permissions': [
                {
                    'action': '.Ԑ\u0379гǱÃ[Ёӳҿ7ȖˤΥш\x91ǓĹƙΉЯ¸ǩĒӹÊïҳ҇ʙ',
                    'resources': [
                            'ԒʣĻ˸҃ҟɭ\x9fЄ)ŦҎПʬȏбЕŚʧʢɥçΨЁɐϼɵӸϺț',
                            'ÏѐīĿȡȔ±ԨŽϸɫʷʦҀ¹ǈȖä˘¥ΕĹûɧΫɇΒìŃӄ',
                            'ˀʥРχ\u03797Ȯ\x9cǟPԘŌőћНʳşЃǸҞžǦκÄ˸ԙğт˗«',
                            'ŭęúԨҘɦ˽õҨ¶ʡŽȩŘ¿ʻΕͼ\x9dƨƊɋӶҤʌà2ǠðŁ',
                            'þαϼǨ#ѨñȹБ˕Ɖԓɚǝ4ƙŵҧÝ\\ԌƷŻϣҭÏŨ˛ʬ[',
                            'ćϗȮЭ\x8bѻʌυmÑɘΪЮĐγӲӿÆԐŦҿɻǦѕǙуdʒÚƈ',
                            'ɒЮȁɝфǃλϧԀĭǬ;Ű˪ɛĔӃрIӚ΄˚¥ǂĈɣɀǗ,ɡ',
                            '7ĺɍʯǓȭϺ~\x83Ǣëˮц˸˶ͿѬйҠʑȳ±ӢɥσąȁӴҹǷ',
                            'ŚXŽѵѰнƮɰɱΰ˧ǿΉɰêԡԆŃʡчʽü\x8f˭ӋΧT\x9eΐ#',
                            'юŏԒíȬфƱǯɸ\x9bʤ˻ҴYˆСǑ¯QӈŐƿѩĥáϦÎǅŔ\x8c',
                        ],
                },
                {
                    'action': 'ɁҭȽȇҜ³Ǵϖɧ^^Ö҂ϔAʹvӪĊԣļOǻŊԎ%Ѓκԓ=',
                    'resources': [
                            'F\x82ƸǿȻúθЉśȝѡʒ˓ɕfvÜАԧґʜώ ɕΗΟɉƋŋͺ',
                            'ҖͿȇӧȂˉԂӦөȈÆЛϔʮ*Ц͵ѧÚЍЂÜԧѝ\x81ԧâӔнш',
                            'ˎʹϵѩϲ\x83ıȝʽĶ§TύŨ/ȍȴ¿ßȧȮǟŻҗϣʸԝɰŬƞ',
                            'ȕśÀŖ˭ѮЋѠy˱óΔЀ@ˉԋΫɂƞɀgѐӔмӲƫʆCяα',
                            'ǡ˹Yǣʎ8ђĈЌԄǞĪϝ6ҼԢǩǻʐ[ńЄ:ϖ˒ҺʾӚÙB',
                            'ґњˈƷɰΑӕҢƳҀƲϥɸҸ\x9fАΏɵѥʖԑôҿǪԆɢƕӊĚҬ',
                            'ʤőіƭԊˎƝӷʃʃҦʳÞȭӁˣɑòϱϠ¡Qӥ΄ҁŮǱĔ˵Ҵ',
                            'ԣƻ\x99ζϷĲˁˉˤӵZɪˁȃԭɜЂѶȵ˲ƋŶƩǨôϷцƆΕ˟',
                            'У˅ӁÜȩҳҷDŧ=Ľƶ\x85ť5ŷ1ΎǞǛȵŧ΅Ӝ˽«İǇĆȪ',
                            'ЅҦőƷР¢3҂һӀϝˬ˄҄ʩԎƔĻɄ$ʾȖєԟԓHĳ²õV',
                        ],
                },
                {
                    'action': 'óȩ\x86ïÚƜԏϳѺҴΚ˫Ă\x9bĞǟɻѴɖŧƸѨʺȡȌӗ˨ñÿƑ',
                    'resources': [
                            '#ˆv˛vǠѦОԮπƑǖЬħɭγϧЯƍ\x93ɩˍԝԮГЪԒҿѱù',
                            'ӾѣѬѵϤϯѰӜ¸ЋÆǮлďxþό»ӠԌВͼCɸʢԐϗΔƲή',
                            'Ě´ӽȇԃŌҾY˲ǰЗɄŋɀƋπ˃ЧĴԅɂ˚ˍŸˉû-ȗ\x7fȣ',
                            'Ʊʋԟǌ×r·ѯŔÜƖӈѓˤéǓÝƘÚʃȁϠ§\x98ȫǓӥǔćǖ',
                            'ҺСѲчԍ\x91˦ǨΏɗʽɔͺċҊ¥šǶȿrÐɉýӂ1ҭʽQĸρ',
                            'Ӗ*ŦńÒĶƨʉϼţ\x96эĺºĤǲÓę2οĒǑ¢Ώɷìʒˇ÷Í',
                            'Ȁұb±ŹϿӐԣ/±ӠØȼӉ9ĮһӢѯȻΒίŶ϶ԝӲͶΫ»ɦ',
                            'Ŭ˞Ɉɐìϸ:¬ˍ&ǔҖȱӞȟVυǼʕưӊBĕ˧&ɨŘӟӆƉ',
                            'ƶ´®ӋЙчȈ*Ǥ¿ʓπâǉwɐхɨǾŕŖ(т˝Ѽ҆˳ǙƕQ',
                            'ѨҼ×иȘĮϤƠӪȜèϲƅϹӈǴȟӻ÷ԁӣþȷʘǋғǋԃϰӝ',
                        ],
                },
                {
                    'action': "ϏɌĉɣѓѕ˸yω%\x80'ǫʵʵɂĒήӭχȳ\x87ˁϚĥʝϘȻ¿Ö",
                    'resources': [
                            '«Ƕ+ǂΥÈǉ΄ӰƗĚ\x98ӼǝͳxKŝΞԎʹȔƷΚàʻӊ9˥ű',
                            'ӯˤӇ\x8dԎѲБ¾Ò¥ҢδƅϭϕǻԛǩӀʇЉ˛Őӿ҅¾еʳXҵ',
                            'ԓúыџϙȶ˖ƵȬӏҦҲӔȹǶ\x9aԕӼӫѴϗEЁʘÐʢ\x89Ƈʥѣ',
                            'ԡĽϋЀĹ)ưÉJҰаʡsǀЕ҈\\ȯбϰп½ŦΎӰӎȪęѮŦ',
                            'ҧǽĉӚɐȟΣɦƱԢɘ\x8céǀƘ˵КȒί˅ҶӱƚIͱωѪêͷс',
                            'ѳéñÕŧйJѹӷұϸΞTӀ²ӓğӿȱ\u0382Ȓʯԣҹɡį:˜љŴ',
                            'ȏɞe\x9aНĸӉƦЬȇƅŊ(`Ɵʋȥȣ\x84Ĺ\x87ƱɵϞҜϒΑϻĤԬ',
                            'ʖƍWӧSԣӮ',
                            'r^ɭȄǉîƇό҅ӌԛɇ}ß¿ˤóȰӦSғΊŚΗ˚Ԏӿ$ĩҺ',
                            'ƅĵʄԤ;ˍДˈĿҶʕǟǂΎȨɧ@ɆƻƥǕхŒѕԘϗΕӻԄП',
                        ],
                },
                {
                    'action': 'нFWđͼғAώϛϲЍʃƵԐҗǝǼӄʏōŸҦƤŌЄʴqʻЎȧ',
                    'resources': [
                            "ʤиΖΛСј˸ѽÆΏϋҚЙώНɎĂʋĎԋ'QŲưǗ ąτĉӗ",
                            'ĄƠй\x83ѿÃМŬцAоþ\u0381ÓķŧΪòүȢ\x83ƺӜǺѳ\x94φΠͷʘ',
                            'ӜҜӂʩѬϟӸ͵ȧ-ǹҧĬтǸΠѲИþ\x9cȽÞŌĴϻǦΨˤɴҴ',
                            'ԦʌΜҧCɁφƟ4\x91Яˇġʊόɛ˽ѾSѻȘҥ˟ǩțАϕӬƺԍ',
                            'ʿ˓φǯӆȺĚQZ¬ьƔþĞȚӞӛÛ3ǈʓЊϡÕϢΝʄOЇѶ',
                            'ŅˋMËʩХøÒ_ј˒Ԡ\u0380ŻE\x98ɤǠԄґ˛ͻԂŧъɲˊkǏԛ',
                            'ǚ҅ŤŮԅLːͻ0ГѢȲśɧ˙Ӆʁ¨ƼԮͿ҂ǫƕӑϽĎ6Cԧ',
                            'КŇ\x9cʖĂØόуȅϮ´ӛÉԉĪȫʝØȄѫ˲ΫʻГ˪ĐɲŸ1Ѹ',
                            'UVáȟ3ĿϿǷ\x97ƦmŲIÖǽЬʚԪЫAǉӁâϔϣαŔƄфЉ',
                            'ȥʕɀč\\ӭʛӗσʒʍƖŗǞп0´ѧпԅјҦϕʹѧǲȳϕǀΗ',
                        ],
                },
                {
                    'action': 'ЇõʭÚ˛ѶϳƖʤǆ.ѰȥѴǁ/җǾɸЇӒźЯƂμƊ;Ҝ\x9fÌ',
                    'resources': [
                            'Ȫ%ĽáԚБԟҞѦ\x88ĔɌhŬͻɮʈʱЪΩԇӊȶϑŪǇʖͰ\x99Ǫ',
                            'ΙɐǂÍHҧķȋӏԫɥѓȽ;єɓRĊĔ*ӕ\x90ǖ˰ӕƍϻŦҔɏ',
                            "ϲѿrċȷ˔кϯĿѻӂͼӏ1ÃΑӻŭӤ'ºʍͿĳθńcȈжӑ",
                            'ƵЋɚшҢÝɚɕƤйʾǿϛœÒθͳό˵ˎɐˇǃjϮ˧ƒɑ˭Τ',
                            'ȸ¸ӪǲʒsɕԨѶƔſȭśƙȨʉù§ʰcхϝɀÛЁȗĳѼϧÔ',
                            'µoƩ×ϭҋǘͶϹȀƎҐǅTîLŠĔWΨDϼхǒ\u0379ϲц¸ɊĤ',
                            'ėҁɦϊȈŊIԜµԖȗVƀÌɬҹxʟYƘӽǬҔΐ΄ҔӲğҍÐ',
                            '˦ȒӷԓҏԚİӾɧͶ҃΄Һʋ\xa0ǓӭɲǢćЦƚʙУÏȄȌТҟÜ',
                            'ɳʀϢӞùԄ¦Ьзҁß˰\x99Ej˙ƫʶƷԍȩѿӬǔʽȊ\x9bÍЖ>',
                            '~ҞœѻƆ\x99лąѳGĲɃʪѮɢfH\x94ԄЬʂΤƪ\x96ƭ\x8fшͲЖԩ',
                        ],
                },
                {
                    'action': '\xa0ɩpǍЍƹĳҜƹÝ\x83ƝȴͳȚÄΏΦ\u0383ηɭӝ˂8ˣΗňѪϚʻ',
                    'resources': [
                            'ĚԀ5йĢӷѺӎĳŦʀƎSĴÄұ˘ƭɩˏШънȘρ:ƒ\x98ɀƧ',
                            'ϝΫêɽΒβӲҿGſ\x82ȵŻԅӖɩѫѝÏyΥʿĖȘфÊχ˴˟h',
                            'ɻяRȏԜϥ˕ʈǏΛĘίwЗɿʬӢi҃ȞҸ˶ʨǌ^ǻӿɤӌԣ',
                            "ЖʄɵǵŬϗÓͰԮɒŷqԌķʊӰ\x80ˣȚȽҊʛʢ˵Ѓӻ'\u03a2ņÖ",
                            'ļϷƵ-ΊΊǇ¨žЧɭӉӳäȜԭȬ˄ɖϭԩɐʓҢɨєѝà\x89ʽ',
                            '˖ʗʅ\u0381ɒαȤϲϒͺČҗǃſԬϻȝéǠǱʿӌƸ\x99ˢ-ƗŘȱз',
                            'ˆӞӏғɷȔ\x8fŘƜŶҀǶƇԆԝ˒ϙ˴ʬȐϯ-»Ϧɣ˵ʭʼƱԫ',
                            'ɒU+1źƃɺҞĚğ\x95ȁɠʧǩʇŜTŎӉ\x9féIұŽˋȍǯưΪ',
                            'Ů˚ȳɻҀưŅļєĆʃƣ"ˑǷϿÚǦѨ˯ˁӂʰāŚļϮѺȟŧ',
                            'ˇӵϥҘôϚɵȥƢδʶ\x83ͻħˣîʍȳԆɾNǩӣΩ$°rˀǩɕ',
                        ],
                },
                {
                    'action': 'ɾƥуѤĮӔ\x95ŔϭɝӺҼϽˣǱĢѝρɎĽӮèΉqȴвɀɒƱ]',
                    'resources': [
                            'ǛӥӻжƣèjѠЁӮ{ƎğʾȏTΟҌԢʗϟӲƹ@ɤɿМϟǂԧ',
                            'ϫӼĈ҂)ʷԎԠǔ\x95ƲćʳǾЅĖęȡ\x9e-ąҎƌʙƆƱŷϗЂѫ',
                            'Į|¢ĐǗƵѿΜ.ΐԊҟ\x9dȉӧ]ʻЋcƆȳɩĈÍƳϰĚǩͳǽ',
                            'Ј',
                            'ӦȶөʋTΰMӞķԂĘΦĝÞǖϐď$ӉҬҭƕгĿzEɲ˅ӣ\x9f',
                            'έйԒ#ˮˮҚхЭ¹ϺФӶϨǳrͷθӌцǟӞˀȐьϛOƭ\x97ѻ',
                            'άФӫӁɦчӑԇɌ©.ϣŘä\x94τӿӑɸǇ˻ҺϏÒ¼υƺíѸ҉',
                            'Ǿˬ˝ЃǔXσGÖ\x9eʴԉ$Râҩùуψ¦ļēѳ\x9bӎ˨ϭˡМȱ',
                            'ɠҋʺ²ϹϾқɫϊɻżƇƁƿǟǮқɵҥŸ?ΘâӳŻˤ<ԣ҉ɍ',
                            'qҏ\x9eқψO\\κʞŽAǫЗҴ˜ŲӋɂɇъÛɣaǍʶÙÿԝ˵ı',
                        ],
                },
                {
                    'action': 'ЯЖЦ͵ЌɭǹǷϨԅϮɎ҇ȀvģÄGфGԆѕŁ½њŞҳԀҢc',
                    'resources': [
                            'ȚϳˠÃ˭ϠÿȖµÚ\u0383åŞːƙɴΑ³ī(Ԥ\u0381ȉȻԄÒǜВ ԣ',
                            '&Ш˦ёЕзД1Ϡ\x8e°úɧўʿǢωԪǝˈWЫΈĖхϫӡʯΘň',
                            'ЁԖ®ѾĿΆҦѣϹӗHǥɗϺɇÒ˲ȎЁɨɼήņб˗ϻЄӛɲΠ',
                            'иԖІ\x9aźƀ§Ӫͽoφѽ&Ѝ˃ԤʣȬԒͶǾǹ°ûsɄŽǜĭ°',
                            'ϜҦЏʴʪ\u0379Ư˼÷ΌԭÚ«ȞʈʪӧȌȟ˾θΔʙЭƾǕ¨Ϳǚ˩',
                            'ѴɞοªŻØ\u0382ӲԘ«û°ŨƐɸȦōʟԤҫZƵԞʄ¢øҮҝÝA',
                            '£ʊяʶñӫԈȑӏ˧νԁϿȳɗóӨӉǱэȕǞ?ēШʖɇÎУş',
                            'P˙ί×ӾΤԍϒèƣ÷ŷѯϴfЬӺԩȬ˟³ªԌɽȁȈľӰǆɦ',
                            'ƅϕϘϋ\u0383ĺ©Һčǻ³ΚӣʪʖͺŦǭ#œƶ\x95¢ҺùԍʧΑĹɻ',
                            'ÒɒȒĬ·ĈӣŃȊ˳ӵЍĴȮĒɬŠŦŁϥʔς˄ηƀȻǡӳʣϫ',
                        ],
                },
                {
                    'action': 'ѱʵųχЌѳӐУůɹЂǠʋʽãӖ)Ӫ@РūGÆɜ',
                    'resources': [
                            'ёЗ¶҅ˬаёǶǌƍωLþǙɴƏӛЏԥƇьӊ8Ԇ¹ƌ˪ćԀș',
                            'Ĩúӌ´ƪҍ^÷Ƽ.øΤЇdȻƞʹȬ6ŹїÆ\x9dëŀ\x86+ā\x9dό',
                            'ԀϾЗДÒoǌ\x89ȓҤӇǆϜԗјϾĴϵŀǲſё҉ƒʙ\x9cʧìĭΊ',
                            '&ЀIϝԑġŏȟĀǂϵκБƿȻƌʋѮӝ˾ɆͷǿƊŗ˷ȃӉυ\xad',
                            'ԥӔτÇǒŰĠǽĵҺÝ3ʩԩFɎɦʲʫɍҼӣςĉΩØδȆ#ӈ',
                            'âРǄӹɨɲϪʋæãϲƔώҾèͽφƘũςÛԡªσĶɱ\x87ҥǜǪ',
                            'ȸԩѯǼӑѰXҴpғÖŷЧɅ\x86ΌƭЦòʻÃн˪ҹǘE½ʖǚϑ',
                            'ЃСҸǾѩθʥϺ΄ӖŠ;ÇǄȤ˴ԇó,ƌĩ\x89Ȏȏʿώ\x80Ȧҝă',
                            'ȵHԖ°TèνǮӨʑ˔ԍшԘOΜȁӅƀŠЩʿɧѬ҇ѰѳɲƳӠ',
                            'v\x87˯ѹВLӾӏ˹ȿƟȐǀȒҿƆæʃΜǨȒјԆԛʇвϣɸϐʒ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ÑǗϮ',

            'launcher': 'Ϲ',

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

        ),
    ),
]


START_LAUNCHER_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': '\u038dɛšё7rԠ)áѺĊӆʗɐӾǵʄ΄ӼΰΓĜǦǆĢӤ˗ų˄ɍ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ŕưƩ',

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
            '$': 'ЂŗԄʗšĪϙʋŠĥѡɞüȿ˭ɘªЍŶƚIЏЁW@ûȜǷʬԁ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3026273231532917457,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 544083.1837296538,
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
            'identifier': 'ӢϾöñŐӃöǟѬeþ¯ȵԝţɨӼήЮһЉɶĉǩύѸϒȑČ˓',
            'source': '\u0383çǒúĨƊʒϽΖрɬBξőцԜŞԇ',
            'message': 'ĠχѦŒaŰпдӰŇϼрϋ҂ʩЗңjåÖȃ˽ϧƧѕÔԭ҅ƅɓ',
            'arguments': [
                {
                    '^': 'string',
                    '$': 'y6ȝƅˌɁϴУҐӷ˅ԀŢ*ΰQѿ\x9eΔ\x81ǯʴāӫӡ\x89CкĨм',
                },
                {
                    '^': 'float',
                    '$': 420546.4001302998,
                },
                {
                    '^': 'string',
                    '$': 'ƜѴĚíѾҍǈˑԭԬĿМѹȟӽєƂӬЕʱӡåŭū\x93ԓƛôźӕ',
                },
                {
                    '^': 'int',
                    '$': -3714643703696850200,
                },
                {
                    '^': 'float',
                    '$': -32945.355921395356,
                },
                {
                    '^': 'int',
                    '$': 205024329924151888,
                },
                {
                    '^': 'string',
                    '$': 'śɖ-ӡƾ˳ȬьßԮȮʐƱȇɸǾ',
                },
                {
                    '^': 'string',
                    '$': '-җͽϨѾzԐĔŃɛ\xa0ʑƙŞȼǠ\u0381ǛɄ˽ыʹ˺ӄѿԈCŁЁε',
                },
                {
                    '^': 'int',
                    '$': 744243099218381242,
                },
                {
                    '^': 'string',
                    '$': 'ɷȕѶĉɞľǌԡȃćӉԁ;ԍǪǪюŒҁЮǩYο;ϙӀ\x87˨ȣĳ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Ԣϻ',

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
            'identifier': '҅ʧϢӂʦǎȺ҂β¡ǆӭϯʜθӷȲ҆ǾV˔ʘ˓ԤΫ˽¨ƊŽɻ',
            'error': {
                'identifier': 'ґɇԒȑėĂʋӷȚá҅ĬέАԞʥϲьЯи¹',
                'source': "ʴѯҝѻӶМʮэȅļє˰ѐғФʄǳϿӽǯϏûƫ\x9f'ǾϲоʧǦ",
                'message': '/νȞƾȩĎ±ȰǃǨϯӄӔˎƚʤȵӵǎxѐіԕȳƴδưєϒƭ',
                'arguments': [
                    {
                            '^': 'int',
                            '$': -1110433000679345866,
                        },
                    {
                            '^': 'string',
                            '$': 'ȒԞӅşùΗQԢʿŲѯňɠӝɪԭ\x83϶ωǶƠǩӐѧɺΓȻΫǼL',
                        },
                    {
                            '^': 'string',
                            '$': 'й\x9fȁgʂ˹ΐŉţ˄ɽ҉ɸŪӔʁĬOͺ»©ÙȎȩķеƶθʣŊ',
                        },
                    {
                            '^': 'int',
                            '$': 5344175362594741719,
                        },
                    {
                            '^': 'string',
                            '$': 'ŤʈѿҋАȁӐj\u0382ǪɅ\u0383ɞĨöĈζÇѱԊНԜ¯ϞϜñӗ.ȅː',
                        },
                    {
                            '^': 'int',
                            '$': -3652282616414404951,
                        },
                    {
                            '^': 'int',
                            '$': 5353411551361877456,
                        },
                    {
                            '^': 'string',
                            '$': 'ǛԞϟ\x9fΡ˨ɗʍƝӭυѫȶȬ϶ЀƠȴӓŤѲзЃùϡϧмʒĝʓ',
                        },
                    {
                            '^': 'int',
                            '$': 8303697912106534638,
                        },
                    {
                            '^': 'int',
                            '$': -200640674771923155,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'źӲτ',

            'error': {
                'identifier': 'ʵn',
                'message': '',
                'arguments': [
                ],
            },

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
