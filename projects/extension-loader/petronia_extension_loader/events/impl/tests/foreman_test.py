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
                'УǋϺ%\x7fϑǕӝǪϪŅőͲĝǯĎсѥʊǞȌŤξĘɃ\x96AҋӪϭ',
                'ҭǕżԔʒǒɏϒƻǝԣƮŀŇîΈNÚ϶tҊӘϒΉЄǲύŒќΛ',
                'ƖҼМФǶʿǯȴǟŁԌnǬMϪӓǃύϑȂǧrЊ¾ǘϾŐѶƽţ',
                'Э@ѕġȩǇˣgɱôЙȈӡйƉ>BЏƃ˟fŊԦƟ\u0383ȡвѾэԐ',
                'Оҳşΐ͵âԀǫōȳûƊɍÔĉϽқʮ<ĴʿюŐˢşŢЦ˾Ġҕ',
                'pǈӭǎӜнƀϘ˅ËѿŠÐː¤ƤԨĆɉǴƶǛ˓ҖLӴF˘çƂ',
                'ǌʌϏϑϛХʎςӌãΈLɤÚĮǮˋüā\x9aюUƭīЁўҔƏ\x98Ĩ',
                '-ҢҬƦӘǒҒȓȟ\x80ϽӍɷ`ϋԥ˗ʰA#ҍǕĤɼƷ҉ͼӥĴӨ',
                '˷Ʈνɾϱˈ"OѵZ˶Ό$ҩȬǥȫң;ǨΊ,Ǜɴ:ӶǂĤƾˠ',
                'ƜɥÎˆʁ\x96ǔˇԕԆţɴіόŲĹзĀΣЛѠdНŀͷҙǋŊ˺ř',
            ],
            'source_id_prefixes': [
                'ƓЭ²©ɞʞѸŊǺˋ\x91Żӈƥӥ˽}ϥɬұķǡ\x82ːɻŴӁāˤ8',
                '\x81ÍhѨѾʜϐ9ĥˀ÷åҞŐЩȰǽѦΨĉҿŧ҈ˤόǞ»ɂ˲\xad',
                'Ѧ˂\x8fɓƔŶÿƸ\x8eƿɹȄбǣыή˳$҇UȭǒŎΗӀkȗÉȳȩ',
                'ЉˢłνǕϛȝÑɘ\xa0ěǻÛԡѵ\x89ʇοƕƈƠĜʛCʧōk\x8a\u03a2ɟ',
                '/ƪӜэlӚƋʶĴϰŇ¢ѢӹσзqӚèӶ˛ƒøƔǝ¦Uƺ˚ʠ',
                'Þɮәơ}ʜʢĎ˵ΔҡΨʂǃ7ԮxѪʬȚϦϗѵɈP\x88ɽŷԄz',
                'Ǹ$Ԙ҆ʱШϛƋʿлӝȲȭέӧĴѳαʀ˗Ҡўƛ¤Μξөx:Ρ',
                'ĿùκʪϤԐшЦǎ\\ƨђҫʋʋʀһңłƯñßӯˊùШ´˧˕ǭ',
                'ЭŧкĥĴҼ҆϶\x8bҾϣ;zǴǿΘȵÅкʨľƔϚč\x8b8ǖЪҸш',
                'ɂъĻE҉ǎЉɀeƬҠәś¨ӵӧɘǱ\x93ҋȆϲȄǲ~πөʗÃƵ',
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
            'action': 'à#ǣɕʉƄȠХźʰǨîũŢ9ˠĳВƂĤŀɉңɋуɭҬʄԣɘ',
            'resources': [
                '/ƄɇˉČ',
                'ÒɣΤǟ0Γӆνқ\x8fƞ.ѶȑÎʸϕśҌI҂Ӷ½;ԗȟҋàľϣ',
                'Ǵ Ȓϼ˸ѠƴŐ_\x87\x89ȸʾĀtӽĭʌ˄Ɂ\x98Ǜ$Ά\xa0ӱʧҩʕȃ',
                'ǠʷѬϨƴ6ΌҌƍ.҂ưҡ<ͶҹΟŸǝѶɇҐȠҮϦĴκϮΩѩ',
                'ԗҲ҄H\x88Ʌ\x87¢ƍǙԘŝˈȊsԆԁƾǹҁӰѬҟӌǬѸ҆ϛϸΤ',
                'ʳ©ĊӑªϢПщζıŚ®ԡԕÍœƹδ˯ĢȊΣһŹԒ\x7f-Ĵсɓ',
                'ɤȅɌĵgҖϸ{ɑëhŭěɢĺ˰ZyĿǁԫ\u0379ƮҀūͰÉUýĈ',
                'ʑʙ«ϕɊӗŀȕȗɞ˱ԕƟʈšóZŢűǴҩӢôfƅҪΙĤϩӴ',
                'ҺƑԢϧǼʩΤͳИЍө˪Ƞ˄gŎ˕ʿ8υ¯ӯZBĝßўɉҨÆ',
                'ǇЁϹμɞŸҰѦȊΟʆђЇҤǯЁ´}ГЬʼ\x95ƾȫġγ8ůәЛ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ă',

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
            'name': 'ɗAԛǍ҇ƋΌÌҮǅɮʔÚф¹JŰŀǍԏёҨȿƞ',
            'version': [
                -112135036325602789,
                -1866518071805276979,
                -5947189304534904673,
            ],
            'location': [
                'ĊѰ.ĭõϓíш%ȞǹєʽШǀҸǂϑ˵ȁıɶӨʤԉˏʺӞԀq',
                'υɱԢŊӘͳ˸sӝɨǖӈɘͰʲԂ˶\u0381ɓХԑ\x85ʆLŻȰ2҆ԄҾ',
                'ȂԛͿВӷřǦϷ:Ͳǵ\u0381ţтƔдҦϹ-ϲЧяɶ~ѓӴйɹϢŖ',
                '<҅jːӌĞͰǡȀŵйЇӱ˰пʄʳɩ˪вȖǈ\xa0ΏńƚԅƷ\x9eз',
                'űԕʪѫïgζƞˁ\x8d˘®ƁɕȄÐйЀ2ӘƃaȞρ˟жԛɕϏS',
                'Ӿė˩ʠǔǶґԘчˮȋ&еËļ¦Ȫʺ§ʾʌХťϚȢƷӱīƆҹ',
                'ϵΞƹςƥЏʡǻшĆǠȈή!ѮοŋҘ?Ǎ\x8bԏжWӪȰоáÐˋ',
                'КτΛ.ǋDëɱΡǤ¹\x99ΑNҁž\x92ȁѸǫΩǀ#ЉȪʎӋðțӜ',
                'ǴчƯæ ȗĜҁɸȘˎĺ˰«ðǘϵƯӪ˯ƩɵK˭ǝЀǰLÁя',
                'РƹĹϺ>Τʤ¦ư\x96ЈˣЖЃćSƄéŶϓӑˑӧƮϬңűөŬԅ',
            ],
            'runtime': 'Óӱʢ®ϘʮˎӆȞόӳĮΨѢʬɠӉÜ˗ζăӠΨ¸˾ԅūǟ˘Ӽ',
            'send_access': {
                'event_ids': [
                    'Ò&YӊϗǢ˄Û2јɿвɹӎɳэѶϳ˽×ѯ»Ķ҉ƮȖґԈɰf',
                    'ǘθ\x8cˤϝ\u038bμŢΜ²ʕчˀ|χĤ\u0378Šя«Ǿ˜ӣǨҩǸԍˆȳİ',
                    'ӠßϭƂu\x98җѱϧ˹ѠϡΘЌʷƒ¡÷ϯˈҾγƴҮПͱϥϭ_Ǯ',
                    'UȜԦʷźЁҶɱǻǐҏcҊ\x9eҒҞΡ\u0382èԇ˒ʴʴŭцεýİʀń',
                    'ȡƃȿʢТÌ\u0380җʴɣŋўdˠγӢӢÉӟåѶªцϊӝʵ¦ȯūº',
                    '\x88\x8eĞģ\x7fďѹĿƫǍ"z˓ВԣȞәҁȣρłŊoǭӂȚ8ˣΖ\x95',
                    'ϰĪλΠ\x8cќǟƢϒɁҜ\x9fǈĿĝԀԋӨʑμϓʾƾĚĢβǋĳП˭',
                    '˪_ĤȣUΪҋäҧԙȗuǠÚԚģӥĲȧ+ͺɿϾ\u0381ҤƁǚԄɐǨ',
                    'ȁ¾їɮƺΣħąԨЂˋôʋɀŻӋ½ЬȮlФv˱ǾËĺ\u038bƪҘθ',
                    'ίƙҖůӂėϹʲLѲǉҮȯҥӒqϕΏҫЇϹэťюĜϷҐȢǬɏ',
                ],
                'source_id_prefixes': [
                    'ĕ¼\x89Ǒ˃ÛЍЊώˋǄ˅ɺǀSǻɆōԑ\x82ȘŀЏXԑћφSȳǿ',
                    '\xa0»оҒǜʺѺĄјΦѕƑɿǌТcÂúɱĊĀцʨǷ¡6¡]ɡȾ',
                    'ß\x8cƜΏŰĈºҕҩŁÐĐɔϦɏėʹϤ·ęôdJƚϡƤϜÌŘя',
                    '˰ʜ˘ē<ćŠС·ʛŬϧ˳ǋǦў>D=gЦ\xadρ·ƹΌȧҭřͿ',
                    'ƦȹğĸĆ\x89ϷʒжѹʮřԡǚӛӓѣʃǰđʒǢɕφʦɤӽɓοЏ',
                    '҅ȶɮԫ\x81ȯǿʼRӲӍËʜȰʥ^Ƶõτ%ɾˆ\x81ԕūƖ[^Ӹύ',
                    'јϣˮϬcқϊ\xa0ɩľĭϼŔϥȫǈԫЧѱ˕Ъû˨ΤʶÜɣ³ƣƨ',
                    'ċĎʄώʪ²żͿʐjαǆҜħÚǫˤƚ\\ǥǧŷĩĝҩçϧɩϯl',
                    '´Ɩȶ\xa0Ğщҿ\u0380§ˣõвƕОΓѧƩôǆºΦш³Ϋƕ˟ŅӢЗǀ',
                    'ʙфÇƃŶΓ΅͵ĺzïΆþΈΗ\x93˓ȶʾǢƗʯƃĈрɉťpƍЭ',
                ],
            },
            'configuration': 'к͵ԧèeбӼӲǟѓǅρŀ˓õŽϰԃȊѰˢȕ<ҥȞфĝǀΠ\u0379',
            'permissions': [
                {
                    'action': 'ѥÚéя¬ÑPĲјāѿˤɑŀ˒ɩɕlŠВѶŰƅΊΔǁˇҲΏʌ',
                    'resources': [
                            'ϩȩNǽɲǠOљȟϾƂîҹʤљлЃбȘǚιÔЄțԍ\x92ԦҜ°Ҙ',
                            'ТӾыǸė>ȿҷҘÝáȼʼ҃ė˽˶ȟʽȠXǳȯŚцЛŃɥ˂ԭ',
                            'ɥǵҫЈɫёēЙςɗl¨ȍʌÀ҄ϾΗÿǽ˷Р˔ƲӵϞҼ\u03a2=Ņ',
                            'ΚöΜŅʻɞǫʭԫäĢχ\x81\x9fʽГȣƷƎӳФʎŹҟ˂ΡÙҺǘ\x86',
                            'þęπ×ЅьХ\u038bĘĪŔʹĦĝΝƈԑ#ѹɿƦϿ˴ҒϟǪϙӎċӔ',
                            "ϧϧwϒτ1ʰѩΕͺɹù\x86çíȪѨʩèԨΪ'űӗԘˋЍӹɣȨ",
                            '×ҷű·-Ě҈ʹȿĪǏϨԘяǲπǦȡΆ҃ήħψҖWǪӦѯԅθ',
                            'aа2ԙе4ϓɹ\x82ԉʆĮƏŚ«ĐŜӫûʋÀʳϯҿăǣïɢͽz',
                            'ӅөÈťҒÔƎϓ\x8f˲çɺǶhŲʬfĹԖԋIĢɦ\u0383ƱʶųЫϛŤ',
                            'ˠЯγ҈ɿ\x92ŇυѷΚγȆӧТĶʝlҾʀʷɼ{ϸʹϖӷµəĜm',
                        ],
                },
                {
                    'action': 'вЋȋͰ˱ЯӢЁɪɍɲˆԁȧǺǹҍʁʭSʁТV҂ΡơԎ\x80ɸӉ',
                    'resources': [
                            "ÖԂƼƽǮUЄӿŉȎ'ĒѰƎȆΪ˳Ҽ\x87ԙĒĥɣźʒʵǑ.Ҷē",
                            'ԗȼ3ǡҤҹƋȩьщɣϾŜfщƑҬůɡѠȴȼҧ8ÜǝҰɂȫϕ',
                            'ɉŤ˲ѻљ\x91ëЮęȲœUҠƠԟɧ; _¸ƆɝϯtrƿРѐԥɍ',
                            'ŨˢśԜŷɹ4řӹʛĪ¯ƹ\x95ΥˎԁͲɞŋİԪҜӈǝ҂ƂùΊɮ',
                            'ԫ¤ϘǭдʑOɅǨҀÂЍk˸ΌǓèĶʟ\u0381Ȟϟ҆¯ԈLƣǖńʴ',
                            'ĶBѬȌƨšMԄ)ӀӡөưȞŎǣɕǊâΖӻǽ°ч˭ö˸kсŏ',
                            'ӕȽҳѕϵƔaӥɳ\x9bυǹo3ΔȎġӉϙіЂʧЪӉȶәӱԨҖҷ',
                            '$£YʮLӊÌҎĆѽíΞmɣƝǟɦӻĩǠLӉƺ˩ºΘ҆ʼ\x87Ƣ',
                            'ζ¥ЁɦƈѡɷŁ҇ǓӒҰĸ˥±ĳɟʂȐѫȺpѫŸǲʢЀƕiɃ',
                            'ϘˀƛȃǺȀŢƭ˘ŵηʿāϞƑėҰʾԀƩϡϠѳ˩˥ÑļåӔΞ',
                        ],
                },
                {
                    'action': 'όɓөŉɄʻĭ\x98δɿɠϜS˩ʁԒ\u0381ψČ÷ԁáЪ϶ˋϢЕâǟӉ',
                    'resources': [
                            'ˏΧǉΕɠѺЬЧКjϪ˄Ԑ~ӕȇνˈԠ\x9aїƝԈˎ˭ҲцԏԘƷ',
                            'ԠɳɝѽʡiЎ5Ӂé÷ıƕąѡҕƢλǵĚȟϹЄԛңʩ\x84Ϝҡ\u03a2',
                            '˾ǮӉɴυɖЖԭѤҨӒʣȆѹҜӿʻʄćήŞԜĹŀϸ˜ÖӓÎĻ',
                            'ƫƥϪĒќԋϋμάȓԛΜǧĳńѶýҭiŏόӓƍęž\x85˶ӖҺƙ',
                            'ʥʹʖ˥νѐʰϘǶӟԖѣɟȣưрҐżèˤ\x93ʖЂʰHƢü˭еѷ',
                            'ɭ˻҆çŶӜÚƑ¤ьūѡǕXМŗʱԚŞυҪӇ\x8aʠɄяӼЊƜʘ',
                            "ʐʘѼǥˠ¶'ϲɛНɤʋʭʰӳѵԃǮĉϪыΣȌζŒϰȳńͽȵ",
                            'ɢӸǌϕƣԂ\u038dϩєʌåԝʖΗҐ΅ʟʽ˒zɲү\x8eЂΈӿı˷ӫє',
                            'ΐϚʋӢΒƓmϺҪɶņς^ˏTôɃɄ/AЪ\x8bɝû\x8eĳςTʂŎ',
                            'ΜυáȷэԪǜŶ%ʤΕлԬҘȽɉь¨Ʌ6ӾɺƓГŐΕˑёɼB',
                        ],
                },
                {
                    'action': 'lĹȮĖѠƸ²у½ĤҗĴβƙđҴДnŁǸ˳ЖΊҜζαԡœϐΙ',
                    'resources': [
                            'ĨԬѫҊϣҎϒȲԃЎőʗМϡȝѰĎҫӍŚʲΰҾΑŤ˅ЖγȇȆ',
                            'ǕȪƫ\u0380Ěʟ',
                            'ʧЪыŇëʶ˱ԤԚĤƍ\u0379҆ǃĭφ҂ǤġϹϭϘ\x930ϽʟЂΒñʀ',
                            '҈ǎ˻ìΰɅūȑ°ɰˎƁÓŨņˏɦı˺ʔȠ˷үÂӓĈǋȎѮì',
                            'ǃtŮǭɮȟʉ˂ʮĐĨîΝNʐлǬМǤɇ¼ƥʅ\x81țǫǣǓƵº',
                            'ҩŏԤ ʱǁϤϸĳ|ΔҖԦěӻɃλ҈҈ŷљЍѳʃˢ\x9dԎßǜǲ',
                            'ːˡ]˹Ƞҷ[kȎșɱ[ƶµʠӶξċ%ŲʸƻҁӻμǴŜʥ˴Ǆ',
                            'Ĳ\x95ӱʸӠǧAѩԧϻͻ˘ӺŝӂɥҪԐΏЧɡəˏԕ"ӱˑѬɅ҆',
                            'ΌΎƩ"ʾɭ1ȫȽĜЍ\x89έҬŐɅòńӧȚHΉҲǑΗЍԞåҝȑ',
                            'ѻˀԎǘо~ҽʱҼɺΧεѶǱҫГΡėȯԋÉƽɸǶƥûɹΐȩŜ',
                        ],
                },
                {
                    'action': 'ТțͱŽɢƏɍ\xa0wÐУϮEͰӟkŌȶχӹʭŭӊϒƠ5y˘ѳƏ',
                    'resources': [
                            'ʠƈЌȴßϼśΛ-łԐŋsγ\x8bʽϐφĔƣŏԘҍęǀQԝȚѳċ',
                            'ҥʣͽЉ\x9aΟҔѫϵɼșĘҬƤǾùˍŷˍԀAKюҦɨ҂чӬԨ˚',
                            'ЙӓӤõˮԃԘÌОØʙŒ\x8bчǝȮɂĹ\u038d\x85ЉϏɹƬÉϡ0ӭʽԝ',
                            'ǟɺΎ˛Ͳť\x95ʐØçʡèћȣ҅Ĵ˶ͷȷɥã˪ҒеΪſɑЋθ\x9e',
                            '`ӽëœͻɋĦҳúEʡҞ˖¦ÀĈıǂϜÇԢҴђ9ЈéHȶѸ7',
                            'Ӌ',
                            'ԗ˩ЫήǆʧιF϶ЛӮ\x8bŠąЊӧӮ˹ӅȮѠҽɣʣЄҁɍ,Ïț',
                            'ŁɠЇҢцcŰӾтƺ$˖ς\x81čőЅăΌbӇɵƨКĘɘȎÌĨċ',
                            'бҿ҄ћƉȆ*Λбɟνϡ¤ɸˏԬüˇЎԎåԡˮŅʊϔ\x8aʹɞȣ',
                            'ÍњƤĬǰ5ΉѰǒĲϤŢđ҃ʒҺs*\x84ɫǶ˺ƊˤƽƖȫŸðѽ',
                        ],
                },
                {
                    'action': 'ɔʸĭǑѕƥβǦӈƦԊƠľȴŪԝƈŞĀǍÜѵƦșʽɃǫ9Yʠ',
                    'resources': [
                            'Ǔƺ&һ\x9dǷļɋQώˡәӓѹҙʬ\x91Ѵϯ҂ʿåѣɕԔʕ\x8cһ',
                            'ωƋȑҢϺɮĂͼ\x95ԆθŠ`ƺЮ.ΡέтǠŚɋƛÇǳԐťeɀœ',
                            'ѫϴƷQIƷɱǥňõҡɾȳϪŋ¦ũίĢҖ²ĞӻѨƃӉАǀӂА',
                            'ϦĨҢɅĘƾīԉȐ%ӿʀȽαʥǊ\u0381ˆǳцŸĹĿąіǅјдŐÛ',
                            "ρ\x7f'ѬӎĘğśϽ҃DƊӨ˒Ԭ\xa0ЩҨС҉қŲǶƕνǪÓǳƩΫ",
                            'љđmӷӃȁƘȺţĈӃŪ˸ʛнӘêǳϓŀӇʶͻǹсǧԘɲƨǫ',
                            'ЌĸȅӮЋýWɪ\x8cȦȓñŧЧɊқìԊΝ҃XĉӝԥȲӶҌȄ҂)',
                            'Ϸʵ¯ӽŠǰѵѯȱʆҸʩӼʼǔ*ɓƊ·ěǔ\u0380ɵΞyѾ`ΛɊҟ',
                            'ɢƀʮϬsϴϨc\x8d÷э|ňͱĘӦŅäҮxƗÉČӛӼƏƪǤǺɿ',
                            'tѧɞǆĀІˆΚŉĊʓ¡δʕØԢЮşáѾӽӢӞʷуϷјŅԀŗ',
                        ],
                },
                {
                    'action': 'úOǷY\x99ȽЪǵυУ˓ĠɋеļΦ',
                    'resources': [
                            'ӫ˶ÂʾiӴҿΞƄĔɻҼ£ХʹôѠɘ+ӱāMȧЕĳæвăòѳ',
                            'ƍіgЃ=Āʚɵ˒ɪYŹΟО1˝ҫӹʙϝƆӳ^ƓèȆƴʯŨϭ',
                            '\u0380žΪԭӔΚåҊӶɤāНԂșčǦøҲϥ|ȰȸǑą<ѕȴ˨-Ҫ',
                            'ϑ϶ʞ\x8bŵ˱Ò¬ɗâƺ)ћԐȓϞɐʟıɬʦǘdɷɦı\x83KҲϐ',
                            'ʽҮԔĕa\u0378ϗѩŦҍϘ\x91ђ\x87ҽŁĨ0ʡԦϸàӼҘǗԦǾϨàȒ',
                            'ǯͲĀ/ɡǻĔȿɠɛˀҺΏƱԪΦпҬӈùʏϲʸ˔ɞ˰ÓвЀ)',
                            'ήņшŎɫΜҚˇƜϿǥŦэюы`aφ\u038bѯļʊſʄҏŨӿ\u0378ΓԢ',
                            'ȆҊˏьˈĦßˌΦӓϋ\x83ҭξԆΒ\x8fȵŪìɢɜ|Ϣßï˩ЏԌ/',
                            'ȮïȨŅu\x87ǤSҖ_ҝ˴ŒƜ҉˕ͼԩГВʌÖΚςНŝɗϒBȢ',
                            'Ę\x90ǮȚƏÝϴӲƦξ?υЮР~ɲĒǹŊěΣʆ{тαǦ҈Ȁѯ˗',
                        ],
                },
                {
                    'action': 'ĜʒʺΑțͱԍϞҷҍÓƎҫӚɤț\x96ɌbƹƾÙϐ}ʏǵйĵǼɭ',
                    'resources': [
                            'ԙ¡ԕuȌΨЭǏĈȹϹӑʦJĵç»ȯӷƄȢ\x9bб\x96Ӊˇʡĵmþ',
                            'í3dучӒțȲʚ˶Ѵ½ϑӃ҆ѪğτÚ˲ϤƛǥĬȌϤƦԂͲû',
                            'ΠɐÂʄҥұƃԇŗɿƀɮĥӜԤXƠŐ΄ԀĄŅȫɷʎѣǣȣđѿ',
                            '˕ȁǖȶƥұɌ\x99ӡÖşԈӅνYӨɤǦԠҦķœ˵ϼʍǟǩЎΤϞ',
                            '~ҤƱѣӴ˵ƴνIϔƞČӲºұēǑͼԎ\x9b\u0383ˣԓSɐŔʐ<Ϧˋ',
                            '˛ƙΠǥԄϿʋȗɒîҖɊҏђZЧ\u038dŏ˯ȞƏѰŠœ>ѕїǚюԖ',
                            'γɬ*ғʆѐĤ˃ҚĵȿʕԦҤǍˡ\x98ĒǐÙϝӣӨѤơZәī\x87Ё',
                            'Ѣŭұ\x84ӰϛHÜҳ҃~˴ԑǢWЪȔĀΫ-Ÿ˕ǦĪŊŵӛҔҏѾ',
                            'ѺѿǝӋϡɱŮKӨùɻȀʎǇÌˈԎçλƜӯƠòɃS\x99Яś˞Υ',
                            'Ёȅÿ(Б\xa0ӈșԤƚʑƌÎͿÔΞÇƸʮҴΰͿ˺eɞȡʩo¬Ù',
                        ],
                },
                {
                    'action': 'ʨƾѫѝԋΆƺԞΛƖXíŔʭşϝ˳ȾҵȿυƲѾ΄ϟƓɯϐ.Ę',
                    'resources': [
                            'Ƃôԥƞ\x82ĉӠӹҠȹđ:ǇУõŶЏӫʩǤȝÝĂ4\x89\x95ɰѕȍѷ',
                            'ԫ\u0383OȷĘЖɨ˥ØɕͻνԃǬѰԎԨӘr§\x94үԂ˖ϝИýíѸ΄',
                            'Еͷǋ¯öΛтȿƆÚį\x9fӱϺIƳƪεÞĭҿҋӝfҩңŨüŸκ',
                            'ɏɀ\x97ƀшƿ˸Ѣɑњ\x8cĭμVҾψɗäRÚӾ\x93ͳ*6ΔϻӚīЁ',
                            'Ҫô˟ƫĬăŗ˵=δ,ĎǽǎXԐѳʈȇƓǎƂԩϰˢПȓȒĀN',
                            'ҦȔ\x96ϡƷ˻ÀϚ¶ʕŖĴύˎԀІ ʟʠпѝє2ϋǗӱШ\x93ȧφ',
                            'Ӿ´ʄԐƇȶɐѠƹȂØґȊ˟èɅûÀԭԦʹѝƫʂɦĶʛ ¸A',
                            '\x7fʌӡɓ«ƇӉċюҸÛ\x99Ϸʉ˹ҕ˙ǬêŧҶɑƵ\x8eʊʱѺΠʂΥ',
                            'Ċҩ˳φҏûƬæ\x8aɧȝ˷ӛ\u0379фБɃĻƦϕȔɡ\u0378Мʽ\x82ȔġІЕ',
                            'ŃщΞǻ0ȁ`ȉȆОCȞШΔàʁɱѤφǨ;ЭƙςŧπʼĞΜɢ',
                        ],
                },
                {
                    'action': 'Łǖ»ǬhŗЫʴ˱_ίВԮˈ˺ΚėҠĖӁҔϔ~ɟ\x81ЩƼlи˧',
                    'resources': [
                            '΄ӋåȃʼbфѬ{ǵԤ\x87\x8bİàӮϚϞΧɆȊғÎϪŋĹÉώɯ\x94',
                            'ƬjȡËӧúÿ3ԇѳźӵτӣɫŀĤҸę\x86өʰБ¾ξӵKƸʝԦ',
                            'ӴΝѬжßƿу˗MÕȝ£љɦ\u0382ԥʈ\x95ĊſŻΗҘџ\x92˭\x89ϾƻЎ',
                            'πɺȪΕѦɼʾĹԌШùå˩ΏɮпʚҬĩpǸʲΠʅřƽϔkǑα',
                            '¥ȒҦð~ԫ¡ӋǘƧϨȚϯˤюПҗуg\x8eѤʮӖӞĦ»ŐΚʸЁ',
                            'ƞȅ\x83ɞ¸ˋ˄ҕΗȴĠԗbzǄѻӪǑы©ˑƘˑΤЄ҄νɁɛˤ',
                            'ѯ˫Ç8ϻϞԠÚț˅˫уӫҢˠ´ҹϠňϿȲҍƔʶƥüӟŌɤЀ',
                            'm¸҅ԪǾБí&O˷ЯǹǛǴžСΪŐ˚ɽmΦʊƷЙƏ©ʗȱȲ',
                            'ϴ΄\u0379ӶʟеӈQҁśЇƁу\x89ĳϷĪӏˢƤЁѷŵʪÿ5',
                            'ȄΦɑҭLРъÜњϦyӐɷə\x85¡ώǰζкЦɑΕ¥ӣĖϥɹřѲ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Eƍԍ',

            'version': [
                -5624739081720116914,
                -5637784167004124667,
                -6379607765139893658,
            ],

            'location': [
                'ȹ',
            ],

            'runtime': 'ԭ',

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
            'name': 'ɆžʻҒϔұҭʀĨj&҈ԠʔƯ\xa0đ˨¨ȫ.ӜʮԓʮХȆԬ!Ѿ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ĭѾə',

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
            '$': 'ɨOsϡ¼ɭØț\xadЭƼ҅ήҚī@ЍŤȣǕĈ\x90ΧûźťϓĹ˟Ϣ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 8647487659758463486,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 69732.23966433769,
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
            '$': '20210910:161311.909913:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Ξϩї˘҆ǏĵѲĀō\x95ǵȣıƽHƙӟĀŰ҂ϏзÎӊӭыѹǖϺ',
                'ɻЩŤљώƕѷȀʘԂŮҠșПɂĽśɩɞƐѳQˊԫ.ƙҷćӴˬ',
                'Όƥɚ>UZɓďѿőήԍȱʴʛŸǝ·ɛƁϳɊͷϳʻȎҷvʍȌ',
                'ΝԒԅǎҳ\x8e˒қǢȂĶʏʒѨЮʳƞϯňǭΨ!Ϣ:Ϧв˜ǣȎд',
                '\x97ΟŃʦŨ\x86Ķ´ԤЙòȯԥίfɅѪïХЎžҿΠԚčώ҃Єөʐ',
                'Яõƺѕøˆ\x84ϟǺƟɬҚʉ¬ɪӜѥ\x9aËҳϠΏПЭϙҰҊЉȤЮ',
                'ԊĬѦѼұǛ˃ӌтЗҰϨ҇;ԆΏ²ΧѬʥһӂŏȤȓѝ1ʆʵ»',
                'ж\x9d\x9fȵĭ²ӉąӌŷˏΠǊȋ˖Ӓ˰ΏƦҝW4ӝȉŁԗԢĖлî',
                'ʇɡπŦʹӴˤҟӺЍƌɹƅҫǟɶЖЊˎͱõOӞðǿǃňҢ_Ă',
                'öBɠɖu\x96ɹӿДǃdǣȚԒԚҫŬ\x8dͻǯ΄žϚǽΔЗțԇ©Ы',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -8946743711939935176,
                -4840848588122990416,
                -6987166768722600593,
                -6760994871273381776,
                4287851054218738710,
                -4111535762950596952,
                -2246535399835402436,
                -5254880321643556108,
                -4885135671277186839,
                4414832576179568167,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                103709.34126915314,
                808979.0296041119,
                -70240.44747903818,
                23752.57365872791,
                903895.7270810246,
                602038.7911887855,
                -56479.451513857595,
                681283.1870814536,
                210323.80897382047,
                216955.4247579673,
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
                True,
                False,
                True,
                True,
                True,
                True,
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
                '20210910:161313.094127:+0000',
                '20210910:161313.111055:+0000',
                '20210910:161313.130532:+0000',
                '20210910:161313.152766:+0000',
                '20210910:161313.176932:+0000',
                '20210910:161313.213306:+0000',
                '20210910:161313.244555:+0000',
                '20210910:161313.266438:+0000',
                '20210910:161313.285356:+0000',
                '20210910:161313.304530:+0000',
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
            'name': 'ƕ[ǹyǝŔƗͽÝ`Ǜ\u038bћЀ\x82ʥ҈˯ϣ',
            'value': {
                '^': 'int_list',
                '$': [
                    4766458032096181178,
                    5470639412213521044,
                    -6060669981705742937,
                    6191235372824988584,
                    -1057668954610393116,
                    -7150768171982014565,
                    5331293476100335132,
                    7936677400181627036,
                    3687915509247884642,
                    -4463074671718025552,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ũ',

            'value': {
                '^': 'bool',
                '$': False,
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
            'catalog': 'ËȏĈiĄń9ӾğϕĳĮ\x9b\x8aûȕ\u0381ŔºѰ{Èǡʉ\x8f҅ǉ\u0381ζи',
            'message': 'ԣÆȆπжȥ¡ӻ˓щlїĚьƧԒêfŻɸ˦ϜϪʠǲςºʑɷy',
            'arguments': [
                {
                    'name': 'ͰûÐ˧ǆʂ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210910:161310.101017:+0000',
                                        '20210910:161310.119537:+0000',
                                        '20210910:161310.139459:+0000',
                                        '20210910:161310.163607:+0000',
                                        '20210910:161310.183403:+0000',
                                        '20210910:161310.199879:+0000',
                                        '20210910:161310.219940:+0000',
                                        '20210910:161310.245828:+0000',
                                        '20210910:161310.273415:+0000',
                                        '20210910:161310.300314:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ˣvƦCÎĭǫ˅ÖΆ<µϼіȿĜƻʭɖτz|ĐƵƲʳ½҄ѭӬ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ÒȄԖҽԪˊΑϾ˳ǒ·ΖĮýϑě˔˻ѴţʎƃȻҀʛѫÒǄJȗ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:161310.492584:+0000',
                        },
                },
                {
                    'name': 'ʠΧ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        445280.3545379146,
                                        101287.21983116583,
                                        214709.57143610774,
                                        694284.480106196,
                                        886054.1273627153,
                                        19428.371658568867,
                                        399718.5219208118,
                                        603603.2139601902,
                                        657823.8217391024,
                                        19921.980304120152,
                                    ],
                        },
                },
                {
                    'name': 'ˮĕǃϵBΆŉɡȇӿǳМ\\ѱĊǸ\xa0Ȼ\u0381¯ʗŎĻų;Ӣƭłj·',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:161310.858980:+0000',
                        },
                },
                {
                    'name': ')WϙÉДƤΫ˗Ω\x98ϟĨ˻ϽǕ˽ӄΖɡȲβжĒɣÀ*ȕʳɧp',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ŕͶɗӻ´ŊãȅʣǁȲТĠÆȪ҇ǦӊÓӚʤƑӔǸ\x9cΤː6',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:161311.019244:+0000',
                        },
                },
                {
                    'name': 'ɎȧąͲ\x86ӔҦʚоĶǫПĬԎҭØɳнƮɾʺѵʙOғҋŧԇ\x89Ԕ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ӄ\u03a2ҌǃȟǑ˞;ӬгƞʵĤʮ\x89ɇσԏhϖʯӓūԇԨ¯',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'öЛˮϞˏGјӥҧɂƷӈΏſԎ²ϗɌѢˌǻɻӲʖ¹ЅÄҏ3˞',
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

            'catalog': 'Ϥϗ',

            'message': 'H',

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
            'identifier': 'ûӈǿʛНÂbȦ+чȝľҽѦѳČφɋƭğѧȮϊɇŠӅϬʫ\x7fʐ',
            'categories': [
                'internal',
                'configuration',
                'configuration',
                'configuration',
                'access-restriction',
                'invalid-user-action',
                'os',
                'file',
                'access-restriction',
                'configuration',
            ],
            'source': 'ȓǶƝ˻өΛԟ˘ɼӕſЊɣ§ǓǁĹ\u038bѵӭϊЗƋ΄ȩĢ£ƈPѸ',
            'messages': [
                {
                    'catalog': 'ǙΏτŧįǯ\x84\u03a2ΖЁҾĺʊęʕƫϜŬӬȩʹɩ¹ƒƥϝćŒРɐ',
                    'message': 'μȣȩɛҍ\x94ȨϋԜίϞʵФԁŷηԅʭцȁ\x84ΐκέɄԍђŬӪʢ',
                    'arguments': [
                            {
                                        'name': '2ϸȽϛÕƳāӡɋԝƮ©ϗƌХȴź͵ɣͷđӞ˸¡Ñ5ӒÑӴ\u0379',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 17279.079711086975,
                                                    },
                                    },
                            {
                                        'name': 'ѸHǅʈǈ¯ɝƬ҂ǫЗƱŝŬȯ=ǃ\x9e)',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 506668.4550848886,
                                                    },
                                    },
                            {
                                        'name': 'ƦԔ˛ŭ¦ɱ¶\u03a2н4˄˅Ҽπɍ\x9eƬæäҲ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɔ˨ӄņˏȎ˼щΫѝǩɍҨòôɏԢȐ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': ';ʊȶęԅlӛԌZIˌҩԀDкòωȘʾԂ;Ÿъ҅ΖԑІϝŧ\x92',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 754184.6769902171,
                                                    },
                                    },
                            {
                                        'name': 'ЏӈщЈ\u0383ƤΊÆʏΒȱѨѹӑ˰¶',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            604363.1146171482,
                                                                            242238.2023664465,
                                                                            772619.8023094259,
                                                                            978321.6008349203,
                                                                            85947.76241732438,
                                                                            454393.4828353699,
                                                                            306134.53065236856,
                                                                            -53362.061009169214,
                                                                            -43092.60801401914,
                                                                            185510.32122723426,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Hŏ҇ɚ˟ȔȳÁϻͽAΞԆȐɴЧҋӤӃӛʶǩҙԐȜƻҢS',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ѶÕйѧΗÆĪϤɨŐǋԏɧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 675615.1673364965,
                                                    },
                                    },
                            {
                                        'name': 'ӠҪϥáŨƆÏѿǦ ʑΈɸÙ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϚԥȖ˴ЭľˬjӍԣԡ\x8bˊͽŮСĻұѴσѡgϡРΒҸʬΘϛ΅',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161254.273362:+0000',
                                                                            '20210910:161254.291491:+0000',
                                                                            '20210910:161254.308759:+0000',
                                                                            '20210910:161254.326317:+0000',
                                                                            '20210910:161254.343331:+0000',
                                                                            '20210910:161254.360158:+0000',
                                                                            '20210910:161254.378953:+0000',
                                                                            '20210910:161254.397325:+0000',
                                                                            '20210910:161254.425346:+0000',
                                                                            '20210910:161254.450172:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ЎϿэԟȤeĐƗʚΥѭŒѢԋІԕϩǬ'ņηϚȇʦĚмʧŭȮɳ",
                    'message': '˧ͷѠƣťQɼŽƍƷ¹ΞźϛЙȆţȂƖ˄@ҫɑŀƶԖяģ˟Ñ',
                    'arguments': [
                            {
                                        'name': 'ȵ\x90ÏΚԜŞɼæн\x81ĳȦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            392253.73934625613,
                                                                            511435.7625460429,
                                                                            -93859.96649871764,
                                                                            -7085.707961212276,
                                                                            768228.8292701605,
                                                                            119883.75593854251,
                                                                            -99080.01588727266,
                                                                            30202.261960926975,
                                                                            768145.4947698698,
                                                                            988172.124987287,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÅŤѤҩʫɜŃ҃ɅùǒƻԗʍÇʝϮшʌų"ÅɸҔªǑӃ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2809291499519423570,
                                                                            -2360165042983291696,
                                                                            -4050230736393115834,
                                                                            453908847270303313,
                                                                            1531949262903096035,
                                                                            5915893189549557234,
                                                                            -1655569413688881217,
                                                                            3124810498121455446,
                                                                            5728695275080351871,
                                                                            -4542754601077467074,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЋхŘфʝ˘Ҝŋ\x82Ӱʝ¢ԇЬ!Ӑnƭô',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161255.199121:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȤǓĈʒΏ\x92ĉΪɔʾĔŃVȵк΅˼ņþѠÏӪìǛˁĕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161255.295392:+0000',
                                                                            '20210910:161255.316411:+0000',
                                                                            '20210910:161255.336829:+0000',
                                                                            '20210910:161255.355056:+0000',
                                                                            '20210910:161255.374671:+0000',
                                                                            '20210910:161255.397772:+0000',
                                                                            '20210910:161255.414764:+0000',
                                                                            '20210910:161255.431865:+0000',
                                                                            '20210910:161255.450537:+0000',
                                                                            '20210910:161255.469294:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǌ˃ǵΪЎÈéͻ{ƄĹʾǤƒ?ϱӬÊӆ\u038dџϺԄ΅әǢȌɄĈˁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ќ>όӚTɗ˱\xadӊ\u0380ħʪ±ã\x92вӄÃҞĠɻӆ)µҶ³ɔʬˡа',
                                                    },
                                    },
                            {
                                        'name': 'ŽҲЩЖ%?ЃӘȬеüґ˗ɮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161255.635722:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ũ\x88ЮŁÚΦŜҊƛӯ\u0380ӵř¡ҺѰԚГšʒͶӴùėȤԚƿX',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҠĔԑҰҧKԃҺʐĨ.ǹȋъφҶЌU\u0379ѹӥѕQӋԋѹӾƤØɖ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˈƅƑȬϺiәȬԗԚѦÎŤÖҏJҹ§ӼЈ\x85ƌҀ ΜĎԛŨԗӘ',
                                                    },
                                    },
                            {
                                        'name': 'Ϭ˗',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʛϚħÌ¬ϊƌɅ˶ƥº,ǮƿВĔҌˌÛǳ\x9eѢSФƘӾ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȳΆʉ\u03a2ũ÷ʒʻʑȹЄ҆Ϻёɝ\x90Ɔ\x80ɝæӏĲĞнĖIàʋѴȰ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҫ\u0379Ϧ\u038bʍӐёϘǽ~ҡӒ˞ǾΰČϓȲÇΜӡӬб¶ʈǩH\x95ʒɷ',
                    'message': 'ºӗΒĐÁƳζёÕԫ˶ȏ˕ãÐҬďKќ9ʖɪTǤŭțɽø˳Ⱥ',
                    'arguments': [
                            {
                                        'name': 'КƭӐȖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161256.102833:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϗЩӨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϒҰηɲɭҭĴœĜɿ\x9eʻiǲ˚\xa0ʴñӛЌӺԄáØʉÆǢ˷ɴ΅',
                                                                            'ТǄàŎǯϡnɠơ҆£ФвԚϧ\x82ˤŀƉŹж¹ӒǧʿѕϞтΞĵ',
                                                                            'Ί\x92ȂQƈŰIŔΚ\x7fġ˜ςΛҀÓȴĂӸÐRƐʊәǣTӐƴͼԛ',
                                                                            'õ8ƛħ˼Юɦɿȵӯо˻aгѳ˾ŮÂɾϐėȖĨ\x80ËǀμɗƢҙ',
                                                                            'ɶӻw\x96ʳīũˮϴƍ˛ʞʽǫɛɰњŭʁʒsǈɭɄӄƈϭưǯԙ',
                                                                            'ʟˍɑіħѠбҥǰħȆ˟ý˯wzєƚϻ˝ӫɵɗѾHɏʸɢšʿ',
                                                                            'ʧŚԛĸÎ˘υӜ¡ѲЂσùŭīˎԘɱ;´Êұĕ˱ʞńėԏά»',
                                                                            'ѩКԟ×ÔˡАŖƙóъƝ\x87ǴʞʿũƤKņȘ\xadGӢӴƽΈǚYƫ',
                                                                            'Iɸ˸ÄƤ`I(ɷȋěÙҷщ˻ʉɯȍёæRΒǣ҅ƺ3Ƀʪъ=',
                                                                            'ʢǮшџɱɾΚΎҎȿǲʁʁȨϵҘəʷ2ЄʾϤƲĆǛê¿ĩiК',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѢmǃΏ¯Ⱥ\x81ҹ:ѧǴæϙŦŒ;ōƋĽΰдˊΈƣ×£ºИB\u0383',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǾӆǹΊɈ˨®˯Ƣʯ˴ā0ǵ˶ћɖԞl%ǯĿ˫їɯƣƗŲљǎ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x91ƟӫƼШƤѯ;ԊҕӼǺÅƬƅ²¯ɫАɈΝĕԛ\u038dѬǄŵ˴˟Ѧ',
                                                                            'Q\x9dˏƸưļƻѸӎŠɉ·ǒпÄÖƲлӓ\x9dɣȒԠŭҋϗʭξçq',
                                                                            '½ɝʩšӭˬϰӰƶѥƥèѐƧǈ©ʵрԤ^ĪɀǲbΣ\x95ģҌǀѶ',
                                                                            'Ӭ`²»òњσŭʶƪðΊͼҦġ҄ƣƷ4ҐƍͷԉԌч˩ĆϺřƏ',
                                                                            'ϦĬØϙΐɨήϵˇәÞēǽęɲɘŪƇ¢ǕɗӲȻΎČÉɧǌ»Ɓ',
                                                                            'ɠŏǸБћ˻yŢ´;\x7fŮѐǩɓɂũϟϜίń¸ɶÉԦǮΛΗˍċ',
                                                                            'їӨѓɝ˫ƜоǹЁЕF\x85ӫɝԛϭ˴ɬ÷\x83ҧÏşȖ\\ņŧɚǨľ',
                                                                            'Ӗƙɝ˩ɣӿΚŴиzҞİԈίԀρǢϿ҃ȑƱ˹ʈēÄ®ɵЍ¼Ϸ',
                                                                            'ÌƳӗҚˡŋѾƅŇʧģɿҋӬ˚˾ŞÓáЬοʋMǈн1d5ЈĶ',
                                                                            '˶˙ƂЙZϦɼˮ2\x91ųϠɕξnѺÒϖÿǻŹȫŵʣĿϰԊʑϽ%',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĹbиКӡĎëҌҎҽŵƹ\x9f˅Úа/ӧͷȆŎ˯íƞ҇āϕȼĿӽ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161256.815523:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҋūƛ\u038btyβńŭǥ\x89ǗԏŦ˙ɾϐѰΖřѥǹȯÌЋϖɞҞӛђ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʱҏԉďϐǓеHĖȏğȌ\x8eŻǎƾıȉ҈ʤżɬǐӆʰЗĻ;Ҋɪ',
                                                                            'єžʾÄʇǺӯéĿɱ˛ЃȾϣŇPЌȞĦЩɦԝ$ͽɻϱ\xad˩Ӯ\x96',
                                                                            'ř˂ǕԋûԅO;Ҥε£péɋ+ªȑƞŲӓ×ƹǈҋԋγǦȭȔΏ',
                                                                            'ìāĢӠο+ϯƀÕ=Oōʤú¡ǉŘĒſǞΝίοҏϑ¥ɝЙӠȄ',
                                                                            'ȖΧǞÜӂéƭÇцʟЁʃȚӊɹћţëˡԃ˲z\u0380\x8aѿʀγұ,T',
                                                                            'ĲʃŉҸȄсÙƚ#źħã2ыƘ\x9fƁʰϩӖȘҹÖРx˱`úKғ',
                                                                            'ȣŨϊЁɐʏʽĉjмÒԒȕǚƵϲĭɛëĄϓÐżԜʒ˨ŉƉ,g',
                                                                            'ԧɼȝϠѓԏФҒҥԃɎŖ˥ŝĎƠɌŘȉІʌʀĂiϒĭlӠʅҀ',
                                                                            'Ѣ¡ĊȁˎēƊΖɘҽfȣͳӰůЃο1ĕǾʍÜ҇ŮĳҧŮͲ»ѿ',
                                                                            'ѨɺöʩƦӕ×ԩȞԬΑąԁϮöϲȪʒɖȭЯĊǦ˟ǤҝӦċί0',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҖVӐĻͱԁЇ=ˣӒȔ˱Ƴęĕ˃ȶɳƨӧѹǹ˷ɵH±Ќδʖʡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161257.221729:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΓҖѭĬ\x80ӂŋӈ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɳĎ҂҃ìș',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ļҕ¼Ԋɡů\x87ȘȇϹϚɓҧĸӄӿϩÍӺǦϾɬάśηÍÖѵзˑ',
                                                                            '*ԛ˩\x83оԋÅԣ^\u0383Ȅƙİƙ˧ӂ\x87юЄŞǧÿ3нnЕѬłúЏ',
                                                                            'ȳþ&ӣ˃\u038b\x84ʯӖ˳ȡŖӟʱћNƦźӛԒúԅ2ȐѲ\u0379Ƥҏʃʎ',
                                                                            'ƊƈӨФұˍǐКѹˠ?ϒϼћͲĢɮ˖ǆԭrµÐӅɔĲӌЙԫЭ',
                                                                            'Ёϐ¦ӭνɋϡ˟CÛһɈ˗ÿöŲҞ\x93ŅΐӔ\x90ѠюɳˇȅӞ˹Ԅ',
                                                                            'ϺƼΪɈ¢ťîӷʘΕ΄˴ˑŔɓ҈ȟλѼƑȼà\u0380=İ#ƪΓ0Ѷ',
                                                                            'ˮѫȡʌď˽ĳ\x96Ǣ˫#ȏɞŅ˺\x8eѐκÒӧĮĩϑӎԥжɺĜȴԚ',
                                                                            'нέĭϛϺʈxǞû΄лԙԡЖϽ҆aíВ³ӍĜâͳʧôԬ\x8aѺ<',
                                                                            'ь\x9aԚˊЬǏϰϒ,ʉï˚ϣȻȡʋЌӥΐԚÐҎˮόː˕ɱȣŧȐ',
                                                                            'зΫÓēǶҥȺɹăǑ˰!ʺӎЀÐέĳ\x95ӧ\x97ƩӞ>˵İʪ\x8b˕Ɨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '!ѱǶSŞȒĩƸТfjϰƺ\x87ΎΡw\x83čӕ+Ƒ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            546416.9385667873,
                                                                            265223.71939171926,
                                                                            97230.05947536774,
                                                                            929317.4317726265,
                                                                            894102.7945265829,
                                                                            -15694.063396885555,
                                                                            263446.91980095604,
                                                                            939303.5100002566,
                                                                            559129.5509473758,
                                                                            414747.92837109376,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĩΣϦӨEǅӣȿXõɵʻDȪ\u038bКһΆɺɣσφĽӰͽÝĄȾӶ˒',
                    'message': 'Ű\u038dˉӦəӌӐÄĘǴ˗ƳýɅÃԂҢʆћcĳ˓ú4ĞӋűύƋʑ',
                    'arguments': [
                            {
                                        'name': 'ӺɷʌʀҜʮҽɠŶ¶ŚЮÉӜҫʢǈĄ0ͿЙưƯȭѪҒʉŻ\u038b',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -591053359228398962,
                                                                            9002710160021144097,
                                                                            -2070885209456093121,
                                                                            144307495882820628,
                                                                            4955631070070032228,
                                                                            -1869611007387642781,
                                                                            -3423653652568704902,
                                                                            -8156793038541116260,
                                                                            -7334639570048003466,
                                                                            6491995319836558478,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǁ¤ȒξҲБ%ɢɒлɣΌ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 329873.59267054434,
                                                    },
                                    },
                            {
                                        'name': 'ʻԀŜϯϚųɱӜϒΊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 837422.8718145497,
                                                    },
                                    },
                            {
                                        'name': 'Ӭǭ˰ȞԢƠЮ\x91ɢ\x9c%ƏȔņȏăϐœϚҦȧƒψƉ;˧ȒʭƨɎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1922607264835435153,
                                                    },
                                    },
                            {
                                        'name': 'ҋӟĤΙ˰ôǡCwńέýÑ\x82˒ʯČЦe\x9b4í4ҐӸÉő\x89ßΎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӟ\xa0ŹΧɒɨʇǱҬӌĆƜʋ;Q,ӘНʸĠϟMǼĘǢӛ˶ʈ{ƭ',
                                                    },
                                    },
                            {
                                        'name': 'Ǎӹ?ʃψŰǄ\x86bӻ^˒$Ђυ\u038b͵`˾ÄȀČƔΎÝĊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 296602.89041976014,
                                                    },
                                    },
                            {
                                        'name': 'Λѹrð\x8fÄYĈЗӂȘмǨØЙƍЃæ˜нŽηϾД',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161258.957246:+0000',
                                                                            '20210910:161258.980042:+0000',
                                                                            '20210910:161258.998046:+0000',
                                                                            '20210910:161259.018861:+0000',
                                                                            '20210910:161259.042766:+0000',
                                                                            '20210910:161259.069744:+0000',
                                                                            '20210910:161259.087565:+0000',
                                                                            '20210910:161259.104897:+0000',
                                                                            '20210910:161259.122406:+0000',
                                                                            '20210910:161259.141362:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Їȿ҃ӛ>ԤЌ\\ǼƆΎƶȀȊЍӒ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ʇϙЃɿȄЩͱӦϮĲғЋҥƌè˚ǵӰňм«ƚӎшԁԄļȤƏ¢',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x9ffI]ǋƀƱˎэϲʏčοϢҸʈ϶ѧƽ\x9bʨˉpмÇʈêƦ˨m',
                                                                            'ÄҲѭ½ЅʳҚǴǒķȘҮѵʏlȋȽϲ¤ǋɁ˦ˇˢÛɗ\x99AȄѷ',
                                                                            'ҲǴɋӕêȘȈ\x7fѬԀӗŨǎ˓ʒӅˍȸѦԗɎőσҢҎѾ\x9b\x88ąǄ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϻʽ|ϔŦXĤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 14719.215296640468,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΧЀɵӧʙʹǴɰĺŎҬőŃʰΐžþÓѿӌԔőõ\u0378˝ЯÌá˅Ė',
                    'message': '|ԥϘͳкƞĩôͶ\u038bϫӡν˂КϴƄōйʸȽíλӭǭԖGPĹź',
                    'arguments': [
                            {
                                        'name': 'πʋҋ\x97w/ɦÇЀʝÀõ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            286075.6940614628,
                                                                            941082.8653999752,
                                                                            687396.5750145987,
                                                                            930221.4062347374,
                                                                            884295.1377257826,
                                                                            533286.827836115,
                                                                            -43667.45916052559,
                                                                            208193.6823868042,
                                                                            428214.82320426614,
                                                                            65814.1322111669,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'фîˋӺӍѕ\x89ұɷӼŰќ\x8dϒƣǏŒG',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6832038439709564920,
                                                    },
                                    },
                            {
                                        'name': 'ŔϾνҮ˜éƖƜNʅβ:¬ʣǣЛ\x8cf˰ҜǐѳД˙ԣͰӦʨƾĒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5806510480591502264,
                                                    },
                                    },
                            {
                                        'name': 'ɻѳǋʗďĒñԒЎžЅӏχʭ˪ØӶȱȫ˂áѪτǴҁɪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1172003741322071706,
                                                    },
                                    },
                            {
                                        'name': 'ʈäņȁɣŴʧυʛƼĳʛPǒ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161300.462336:+0000',
                                                                            '20210910:161300.489899:+0000',
                                                                            '20210910:161300.516813:+0000',
                                                                            '20210910:161300.541067:+0000',
                                                                            '20210910:161300.563116:+0000',
                                                                            '20210910:161300.585177:+0000',
                                                                            '20210910:161300.606164:+0000',
                                                                            '20210910:161300.627170:+0000',
                                                                            '20210910:161300.647088:+0000',
                                                                            '20210910:161300.668099:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŋ%ăǰӈԚҔöȨ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ˌƗʏcHǝʤűȏɳҥҐɱƅȤ.ҷȒʯыАʿϒūϫέЏ˂ƿи',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÛЍЩƜηƫѴƣơ&\u038dҿRÉϭПѶʨġŸʔÎŚԖӠмʘ˷ԒΣ',
                                                    },
                                    },
                            {
                                        'name': 'ʦпĭƶ\x7f»øπθԮʂĲΙ˝ʴŷҹĐʦɿВ\x8cѨ5όÆĥǂèЇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161301.147473:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǻɱΤ˂ȌƓɧΠŤǷ˂ΨˤzSƱĢ8Β',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 67743.83240071501,
                                                    },
                                    },
                            {
                                        'name': 'ŖǕ˞҃ӠΓū˺ӓĮͺĚϓàӝԔ\\þӀŜȦ˧ηӎСƧƴ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ԃ\x82Пƥ2ɿʏƄӀɋӓʕєȗϠĮʺŨØԃ˚qΓóÆϖҲ˲ϋŖ',
                                                                            'ȾɌʒĮӲ3ϯ[ң\x87ɩʸǁǉ@ʚnȡȈÉǿ҄є˜ƩƏдЬҠ\x92',
                                                                            '΅гÊ\x87Ͱčʷðχ˯ΠˢΟCđnɂ\x8cңͲƌĦτӍ˘ΨӶ¦Æʊ',
                                                                            'ȒǒΏƐϲ½ĶrsDˡˌǦѻ҂k͵ȏZ\x97П4ȗǨʱ˳àƺųҪ',
                                                                            'ϖŜ¡ǡ\x83ӥʦ\x95įżґƜȖPͶƯ˟ƢŲȔʵщѧʹеӍӼҵŴѽ',
                                                                            '˳\u038b˴ɄҡʺΚѡOʅҺŅϙͶŠЋŢvGКʚĭ\xa0лǃĵҾŚǨΒ',
                                                                            'ϑčСȥͻ\x99ԝΦȣQѽӌÏ\x92ϿǒѐÄ«ɟв!+\x88ÊåɰƷԛũ',
                                                                            'ζѪѥêЋˮ˱WŶȵŗΟŃѯĮāưЩ\x85ġ+ԟȯ&ŬʡΈúǨǮ',
                                                                            '˩ΓϙțΏƦʖǷŮëžÝ@ӓǌÆδ¦҅˦ϹǣҽˮώКfʥΊÖ',
                                                                            'ĄĒВǀǗȷʁҾԫԈμêуİȍӼǾЈâŏǋ˱ͺǬıҺȳʘȲѤ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '!КǑҨǖĲѤśт˱Ϸ҂Ƨ8ѲˤϵÎƢʳtƁ\u0378ѧ\x86ӍѦƠƎ˧',
                    'message': 'ÕλĆӸ¿˵ҌǛҍҧʩİΌΪ\u0380°П\x98Ʌ˗ȘУǟʤԈýϗέĐҷ',
                    'arguments': [
                            {
                                        'name': '˧÷Ơ¨Ͼ\x8böҭĠĭxѳѡЁϷ҇ėΊҫӴ§ȜšΉλØɻŠýŅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϸԧͳŭŁƪѓK-ʝ\x9bŅĥӖƀiѶУùЖªʜǥԧIɞȰІɏӥ',
                                                                            'ȎźƳˡɍʴȪȭљљеƺό˫É¸ΝIʡЊлʓˡЗƁʑӥЏƌd',
                                                                            'ĚŸ®ԑϛҁˤ˓ɑOő˄ÅТϴâәѸԟҚʇ˰uŴƨϖ\u038b˖ǴЂ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˳ԝͱ\x93ҡҴ%Ǎϕ\x80о˚ȓ\x9eЌϦϏѭΦOŁˣʹͶɺǪҲƝЦӴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161302.035497:+0000',
                                                                            '20210910:161302.061845:+0000',
                                                                            '20210910:161302.141763:+0000',
                                                                            '20210910:161302.174685:+0000',
                                                                            '20210910:161302.195925:+0000',
                                                                            '20210910:161302.215305:+0000',
                                                                            '20210910:161302.236351:+0000',
                                                                            '20210910:161302.259619:+0000',
                                                                            '20210910:161302.286867:+0000',
                                                                            '20210910:161302.309230:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɪǪΙΡɨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6814564264785546952,
                                                    },
                                    },
                            {
                                        'name': 'шWūÈ\x8eǙЏөƓѳɲѱЊŅɒðԌÝ¬\x90ʌǮФɃDQ\x9døƥї',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161302.504543:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ćχˀԣãġҡ˼ȁżɠíͽӲҙʀcØГ[δВȰǦȨȬÀȇћ\u0382',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161302.611228:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҥϹ]ˉŅԎ¸ӥźҁʂŝňȧА|ȓ<ИԌɧöМ ӫŉ9ɐ҄Ȟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˺ȍǥъѥŦңϨŌ|\x99ЦŞ˰υfԧ\x9cŃʷԩѱήʎȅӚӣΣҴĝ',
                                                    },
                                    },
                            {
                                        'name': '҃ɐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˰ÐІÌӉғ˶ǯhðĮˣҖģýŠÀȪ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161302.878904:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ώӊȇӭáӷ$ЊϢρ\x9cʏŝƪӓχ>ú6ѳӤӖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            341952.71950760426,
                                                                            446019.5389137198,
                                                                            626500.4926353433,
                                                                            199293.3583490355,
                                                                            407677.7633974099,
                                                                            591993.1839591644,
                                                                            -36302.421131564835,
                                                                            178635.37208397378,
                                                                            -54767.66379016511,
                                                                            79383.34445236312,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ђƯаŐČғȧ¼¬αŚ;ΪФ;ȄŪöҤРŃʈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǡȥӎƘʌǥ×ϰĴĵˣˌɮτǧȇ˄ȥԮ˽ĭʨƶϩ\u0379ԗĿϷɪǆ',
                    'message': 'ӚȲѤʁóΌԎ˧˖˅ĬԁÕ иӟдΗΣǅVʢ\u0382ˆҭӒƦßwЪ',
                    'arguments': [
                            {
                                        'name': '҅ȣƟ\x82ĸȨϹъhĠѻ҂ÂƈʓƊ\x9fŝӥ)ϢʜЅң',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4417304134629749144,
                                                    },
                                    },
                            {
                                        'name': '˸ӜԔжɨEʣɱφ\u0378ģȭãԢЯӰѤHɿʎ\x9fgΓ«ūɄģŬЋ˦',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161303.536539:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 189243.09612961306,
                                                    },
                                    },
                            {
                                        'name': '\x9f¯ӫȧϮӘρðīɅ˕ɶИǃƶȬåŇΕș˼љʵɢӸͽ{ʄÜѝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            888076.6340240529,
                                                                            793386.4294221346,
                                                                            92072.34936576907,
                                                                            959159.6897234232,
                                                                            312740.0241905645,
                                                                            -29207.38768098381,
                                                                            765725.9890965247,
                                                                            294905.6183974328,
                                                                            733230.7618061438,
                                                                            900882.6352361401,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': ',рЇυÙ˥ť\x9dƅȕԫЫʟȏ˭ŵˌ@ǆɔШФɱƗӰĺéɒˇŀ',
                                                    },
                                    },
                            {
                                        'name': 'Ǝ˧λǪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1944571415486032342,
                                                    },
                                    },
                            {
                                        'name': 'ěˑӛϫЁƉνɧXʶ\x9cƴҲ\u0381ԉKψ҉´ĀǄǍǞΕʆWЎԡ/P',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5556490507194958898,
                                                    },
                                    },
                            {
                                        'name': 'αǳãɢԃӥԔǰvDǺԪуΥ\x81ȝΩΠӜɿȝĺϷĆċ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɉέ×˰˒\x97ÜȬϫτŭУ˘ĀƦʠЮɤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            967871.4309181941,
                                                                            908343.4147109694,
                                                                            -69009.87336775447,
                                                                            180080.37141144165,
                                                                            729031.5971168196,
                                                                            138638.27236452413,
                                                                            636410.3534988487,
                                                                            435867.71565362485,
                                                                            371388.2193561141,
                                                                            121503.0331414222,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҨǸнΚĶђєŝһ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'úǖТҵfʯŅЊǷœʿƷфϸȲŻĮҡϊțʜԖŬeΎДҍǀȯΐ',
                                                                            'ƼŝʬԎϮŷɢʒʝϘҿΖӤϨ&ǽδЈÔӛǐιҒɜλĪ˙Əýɝ',
                                                                            'жҵʞĮƚįѽ϶ǁʻȸȴԍϱH/ɯӂ®ųz»ј!ΤԐ\x95¹Ϊӵ',
                                                                            '£ǐţԜ\x80ϰǬΛєѮ҃ʯϒΩϒƦοˁNʽӜƓNƬӴАËĮǓğ',
                                                                            'Ȇʃ˝ɄЄ(Ư9ɼӏȧч҃ŲʮЅҭ\x83ł<ҥ¦šӐųϜǢɪ¦ө',
                                                                            'ĝдġΰɐПϼǯƋҤ÷Ǭ\x92қȚΕɨԣAГǘ@ѫχʗÂsɹϤӨ',
                                                                            'ΜƧƯʍıǷąиʦǾŧҮɗǅы½ЃͰȆȞϕѡˉ¿Ԉ¶Ϥŵ˜Ǡ',
                                                                            'ӛȅɵΚĿ¾Ɠ$ǥԫϱҽȮҶŬōѴʽ·ҴϜ˺ȎϨѽΤè¬ɣԟ',
                                                                            'ȐǨBҲжȰƈ¾Ϻ˞ҭɝ˝ˆҋʏΰƏɘ˳ʝӺPϟňčзÿǕӃ',
                                                                            'Ş\u038bӒªζĮ#ʶёôʄѹҀϔ҇ʪҕϼŎӃÁț˱ŃԚӠɄ¡ɭŶ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x9aшҁɢƽ˕ǲĊɊYɝDʹʓ2мǈʱĒӿѡʇӣϓӨϰȷç˓ͺ',
                    'message': '©ʮʿMЬņ®Ŭº˶ӄƛʌɮĝƑǒƍy\x89ƺеϸѴƫѕɮ\x88ϭǯ',
                    'arguments': [
                            {
                                        'name': 'ôɡtșώŠӬȳɇѠʒiʬǹђǞǫέҎƔԙÖҮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161305.083282:+0000',
                                                                            '20210910:161305.100933:+0000',
                                                                            '20210910:161305.118743:+0000',
                                                                            '20210910:161305.136710:+0000',
                                                                            '20210910:161305.153378:+0000',
                                                                            '20210910:161305.171979:+0000',
                                                                            '20210910:161305.198671:+0000',
                                                                            '20210910:161305.224732:+0000',
                                                                            '20210910:161305.250164:+0000',
                                                                            '20210910:161305.279946:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'º´нѢϓ˦ȾǨZŭț2Ü ѹŬɊ¢ϢƨϋјͿЃЃǔʏÇȵW',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 343266.39293855213,
                                                    },
                                    },
                            {
                                        'name': 'åӛu¦ҳʊΟ\x85ԒkÝș˥ʛЇƥπҊĭҭ{Ɛ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ýɓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'o\x8bѝƯsåȜŌOƟԝӃϻШ\u0382ӷңȾśӶѺЏ˜ƨˋɱӟɅѻh',
                                                    },
                                    },
                            {
                                        'name': 'ρҎXьǨɪJį½ǔă\x91˙Кd[Ԥ¼ȄǒÔɷɘїʺû´҅Ϩɒ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            916079.2599481987,
                                                                            864563.7237312456,
                                                                            518479.5056330076,
                                                                            42348.30331756864,
                                                                            529555.2138665315,
                                                                            117193.61683659742,
                                                                            297375.6088546261,
                                                                            635955.270504268,
                                                                            574513.3360169029,
                                                                            -79327.85474995586,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʇÜǇƍtǅún˩\x9aӈԆаϯҾŃǓϳšƌˍͼǩǫƔΗÂōВˠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161306.150082:+0000',
                                                                            '20210910:161306.167251:+0000',
                                                                            '20210910:161306.183454:+0000',
                                                                            '20210910:161306.201964:+0000',
                                                                            '20210910:161306.220973:+0000',
                                                                            '20210910:161306.239339:+0000',
                                                                            '20210910:161306.261326:+0000',
                                                                            '20210910:161306.282489:+0000',
                                                                            '20210910:161306.304750:+0000',
                                                                            '20210910:161306.328726:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'IѴƒЮɐðΎʊʯӷ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0381kԈ\x80ʇͲǡȌ˧кԆɔǑΗ»\x8dљħӯѾ΅ǲ\x94[ðӪЛaȿǴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161306.664340:+0000',
                                                    },
                                    },
                            {
                                        'name': '¬ҫɏӭӪð˒{Ȋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161306.737643:+0000',
                                                    },
                                    },
                            {
                                        'name': '˚ǂІ*Л˴Ã΄˴ɫƕΤʒƠοȩҢӃ˹Җυɸ\x96ƕѦФ9Bȼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '*ɉɰŪ\u0380\u0382ʥ҇ӲҰƆ²Θ-ǈŏɝάʸҫѱœĜӑǽȨϮƍřɯ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʘӟ¬Νʳ˱[ŷҝõԒĝǹҍƐàĥ˃BȷʥШ°}ςŸ;ńΒƻ',
                    'message': 'ɋЬϨѾãӨ҆ǹˤԬʥϕ.ƖϬȽҵ5ǶΕШұȚҪҚóCÌНĬ',
                    'arguments': [
                            {
                                        'name': 'эďԨԜѴŦ£\x7f«ҿͽ\u0382Ζ-ϕŅ%{ϦǴҲŇҾȲ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161306.962109:+0000',
                                                                            '20210910:161306.979770:+0000',
                                                                            '20210910:161307.000548:+0000',
                                                                            '20210910:161307.017601:+0000',
                                                                            '20210910:161307.034249:+0000',
                                                                            '20210910:161307.051918:+0000',
                                                                            '20210910:161307.068586:+0000',
                                                                            '20210910:161307.089165:+0000',
                                                                            '20210910:161307.107250:+0000',
                                                                            '20210910:161307.129658:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'дϲKɄΑѶǯͼ˰ùǹˇΪѽɫΈбİˊ\x81˹',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2327397205063655753,
                                                    },
                                    },
                            {
                                        'name': '˂ɵȂ˭ķ˳˘ĿǓ˽ģҶƸӪ΄ǶԟɐҶÖ˂кŦĥԂ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '=ʬԊϫƚȪĥЇǬ«ЮːԏЁo\x8cӿӾԭǏӜϢӴu\x81ъҎ;ɳÇ',
                                                    },
                                    },
                            {
                                        'name': 'ǫжɦɿҾԉ\x9fʹİӂŘȅҬϼ®ƙšЁȶΪɫϧĵГǚVǎύ;ŷ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1577836596831620300,
                                                                            1451626326569067741,
                                                                            -2457473491151167662,
                                                                            -6866305628852144932,
                                                                            4322166371959083988,
                                                                            -5480321092392530610,
                                                                            -8828912994111258510,
                                                                            8113176821762140768,
                                                                            -2999398646403050463,
                                                                            3730523295781338548,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҺԘήӟ\x89ΝʉǓ҅ӆĦɘϷŞΈЭХΐ©҉ЛњæȱĬλǴӭΨÍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʢҀ҂:ԨĤʃƷʆ¦ưȖψ¢ºȻјʱƥέ5ŭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161307.786888:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ҹ&Ȟ÷Б]Áʘϰ:ĔơqɆ×˨\xa0ƋўӃЁƦοÂлϣʤψЙű',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x94ŢnһМƎЖ\x9dɧĿυƐɎ\x95ЃmˣΏԂѻɅљӍ˺вːūбˎS',
                    'message': "ŀά˯'Ŏÿ×əƴĆǾƒ\x91ʽ\u0380Ėԅŭϯӡ˸ÕõȦӃJԅ¸Ҁȅ",
                    'arguments': [
                            {
                                        'name': 'ЏŹʶǖϓ³tȔBʳˤ¡ӅɎôS\u0378чĸΧӉҽÚğϟĴͶƘŏΜ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 213566.9523106306,
                                                    },
                                    },
                            {
                                        'name': 'ƅĘu҄НŽРåНŲѷʒĈɼƋɜĢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            672246.2852911147,
                                                                            -52314.20634615788,
                                                                            50387.12426795831,
                                                                            423976.91083531646,
                                                                            366405.75361123023,
                                                                            690311.9986094175,
                                                                            554980.9230288321,
                                                                            942497.791079428,
                                                                            332322.9953800192,
                                                                            -69075.4864068355,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϞѹЭ0ʔǮӆϩ˫ҮÌ×ǕtŠɟ͵ϣӤƳ\x99(ӥʧɹˇҊƅΫϐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8372563398166300344,
                                                    },
                                    },
                            {
                                        'name': '?ЩЀӄšƤѲ«Ԟ˫ҊʔŉĭrϠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161308.478994:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɁêǌȪӽёż\u0378ʘ\x92ȅò¿λ҃ƛʳϛŉɷÿоŐӟȻë',
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
                                        'name': 'fӮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161308.846265:+0000',
                                                    },
                                    },
                            {
                                        'name': '¶¤˝˭дǀɉĥŴgśĽɓňԢүɷºǵ´',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161308.917002:+0000',
                                                                            '20210910:161308.935375:+0000',
                                                                            '20210910:161308.953906:+0000',
                                                                            '20210910:161308.970492:+0000',
                                                                            '20210910:161308.986902:+0000',
                                                                            '20210910:161309.004502:+0000',
                                                                            '20210910:161309.021866:+0000',
                                                                            '20210910:161309.040730:+0000',
                                                                            '20210910:161309.062779:+0000',
                                                                            '20210910:161309.083508:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЌƄεĞϜ&šƿɰɟɦĻÂªҝɌɃ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ˉәÛЂΪΝɅɞÌŕԗºӒѢҵőÎҔ;NʖΨѸɨƠЌĶʦʛќ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161309.455316:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÿƇϭ`£Żϝϯԑ½ˍϼxѺǬōãȘǎ˕Ђuɥǒ"öΊʿԎɪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161309.553736:+0000',
                                                                            '20210910:161309.573450:+0000',
                                                                            '20210910:161309.592958:+0000',
                                                                            '20210910:161309.619268:+0000',
                                                                            '20210910:161309.637787:+0000',
                                                                            '20210910:161309.654875:+0000',
                                                                            '20210910:161309.671889:+0000',
                                                                            '20210910:161309.688014:+0000',
                                                                            '20210910:161309.704458:+0000',
                                                                            '20210910:161309.722039:+0000',
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

            'identifier': '˔Ɯ˧¢ƹ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'Сќ',
                    'message': '\x9d',
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
            'name': '˼ũǿϯπɦnώÜŮԐ҇ďʕʽʹԣȆѲ\u0378ЫɷĂмѨȻY;ͼǹ',
            'error': {
                'identifier': 'ԥӵɝҼƚҋҮŠżÆѤӓԡɴҴ҇ЋЏԝĉΚÃŚƕӜͺgǬǛĜ',
                'categories': [
                    'invalid-user-action',
                    'internal',
                    'internal',
                    'file',
                    'file',
                    'os',
                    'invalid-user-action',
                    'configuration',
                    'access-restriction',
                    'access-restriction',
                ],
                'source': 'ϨΘˏ]dӆьÁƅԗ΄·bʸǘéʣŤԜϖРӋ˫ƍψƂ%MϢ˧',
                'messages': [
                    {
                            'catalog': 'ȗПȌ\x90хɲșʾҡʄӮėӸ϶\x89jФțƜκʳӚʚϷ\x9c-ɱҲʻԬ',
                            'message': 'ŞʩƬƋƔЧũƶ©ɆΘɩűóȞе;ҹɶȸƙ\\eъɛȘŋƇѻЎ',
                            'arguments': [
                                        {
                                                        'name': 'Sʔ\x81ɔ\x7fǚе2ƵÎȢƇĐ(FĺĚѼ\x8fĜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҚʟʏʖeǏԀ\u0383˜ƩѵâіķŶқϕˆҢkͻǓ\x8eɵƅӝƊʊƸα',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'лɅġΜ×ЌȀѶϤƏÛ)ԥхʌ˨\x90ɥƉƖÅÈŘҧðĪ˩ЄŪȨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'νǭб',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ɯԛ\x85ѶǜɢˬϲҥȖӊĵĞʃBĐĠ˥ĉʹʳҔʺĈŉЧώSɩѼ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǘ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '×ѡ҅ѬX¦ɺǛͼɋȆˍş\x87ѡĝжǊʓĳȇҜʯˢȮʚίǴψт',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĘıЇȇͷҤϷŋĚЗțŢsȭŏùͷţǟӝL',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɘѸ˜ԥԪżɎκЇ\x84ɻřÐҒşʔѬчҀ˫\u0382÷ЙÅǕ¨7ƘNӥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161243.078254:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύϙ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΝźqΩ˹Вÿƛʽд˖εƦӫҭơÀã',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 226085.8155470229,
                                                                        },
                                                    },
                                        {
                                                        'name': '3\u0379ӯʅѠϒźȶÓ\u0381',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǼɄƳίǵϜѢϷȹσ©ȪɪĥћoϰӤώһǣ˷ƮğƟƪŮƱԋȻ',
                            'message': 'βˣȮǳ\x82ˀ҉ЙԑŽƍʡЃxΐҞȇóǎȬ\u038d,\x9dŃĖѳȰ\x8bӘԭ',
                            'arguments': [
                                        {
                                                        'name': 'ƖϫIаϑɲg˞Ѳә˽σȽͲɫΒW',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Dw\x85\x89ҖàǈÃ´гƩƁşҖŲɚӕрѦĻŖ\u0379҆șá\xa0ϥɠag',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x7fГМʀӹœðԫΜǬйƪ\x97˥ΜϷӔԧǯЛϠÚЊμ·',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁͼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʋСѮɨʮǥĦļ\u0380ŸŷĄШъƀλÝˋĨѥκ\x97ӬԍϫǇƧ»ƕη',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĕ\x80*Øʮ=ӦŅˌҜ\u038bϡÈŧѵӴj˞ĥŴХǰǋҝȈöΏȲǢÂ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x82ńőŋЄϳњѺҒʓԤϐƠ3ϠȡdƯЎĦïƍˁǂȜȺʲҰѵ7',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 855803.6926092403,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʆҌīƸλƇԪƍɁƐ(ŪÂʟԝB´˔ɢ΅цѺvĠδӸ^¬',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΝɶЫє¤ǕԎĕù\x87',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161244.074553:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '5ҌÍǶұԢҍԖӓԔΪҠ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟ×ӉŒЊӲŴ?µΓϷҡҀͽÜˍѵj\x94ĎωưɻıƙʩåȗːԨ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӳѻ˷\x9dOÈЖԚjͻǻßΏȧɽ',
                            'message': 'ϐϨƛіԂ˕ȮԜĠӴ£ΤԗJͼɀǾǼ´ǻƜưɵƲӢЫ˵ϻƶŪ',
                            'arguments': [
                                        {
                                                        'name': 'ϡѬɔϋЌȢ~!ͳʁӈ҂ӈͺǤѪˡϺ˜ϰɣǳʱȝѻэД\x9aє|',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Xȕ±ӵͿԇӝǬρŢʍǧҖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 744338.3779294214,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȗӂʗŁ8υŀԪү·϶\x9aηтѭo˻ȶÞѵªΧƆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'əȺӀpƁôȺƛÝaƨɶƣªҚӊҤĲ\u0379Ә \x95ήɨΐбνӵgм',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƉлɘáлºδФǥƖ˓ɚԑȿÓғʌӧϜžƙë\x90ǱϨĀɲӨѲĠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʏҜԊѶϓ²ӃɅбǴϭЄ\\Q',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161244.749293:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҪRѼʣӊɭˠϙĢԠ3ĀМʒҼŚώǊѶΝȽҟ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1378055390167647355,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʤʼɒœȑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 968250.5364201453,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԌӆʫНΉ˯ΰμЗǣӺ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˓˔\u038dżԫȩǽ§Ɂŧ·ǒÀԖõȠҭµώĩ˘Ʀ\x8aԣҔϝӨΛųӼ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴab\x90ԢGӰĔԬЗɕȘRΆњ˪ϿėŘѹʈʢè˸˓ʅҴ»ҋȄ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161245.047928:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΎϻƟũΖƆāΧżƘұГǸχ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϳԍеǠɈÞќbҮýɗκяŞΫǉȚтwƄƥͺюʡͳϢɵ˰ǬЧ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˧mĭɿҨ4ȿԃςыȪҖĽ¦ҖǭҥʖŗȢʕд˻Ʉɍћ҈ФȦƟ',
                            'message': 'ʿÒќĞϣĿӪԂʌŕɩӹŒƅƕʎÏǹ?ȱãƻÙԅ\x8bĊUԊΫΗ',
                            'arguments': [
                                        {
                                                        'name': 'ήɡѳё#˰´ǓƁэșƠʛΕͿѿҰИȐǱ҅ЖЏӢΆďɆΘИӯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'РʬðӦмȵőŵĈĨЉяˍЇҒԐ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĜȴƓ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΈӽǈȂЩϑͺԊӚ\x8bſԓʠ³ƱӴɐԂ˱ʣǪТ~Ҝ7OɓǴ\x8dƨ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Оҙѕ_ԣŇƁĿIĴɧѓӔԛƨǾҨӰǭγSϔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '~ӕёњƗώƺіϷЋȔύЙМ˼ǋƍwϡʓ\x9cǇ·ӥµûŎϛҠĴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161245.784163:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'пÀƹYԙԎȂӡJԛˡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161245.909801:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ůϘVԙғƻäѝϭͼˑԐŐhɯҐщƨʬʹIǠχˊgEÊƽĂѼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 944238.9158100383,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŔʕԁȡuŕщȄ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5865464390402473600,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌ&ȗ҃ʸѩ˭Ԭԫ\x9bʇIΪѥϞϹŦȷ¡ԫX͵Ђ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÝŷǄîҸѸʌ˵ȪѪ=\x8eʹʸЙ\x82ûԌζϛÀK!ЙȷÛсŃȜ?',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĤϰǾӭЧƅʉӞ²ʧƋЈǣvѼҋȪμϼʹҼ¾ϣȫ\u0379жˣжșȥ',
                            'message': "мЖΝ%λŞ˘ȓĸϾ'ŵǕçĤōчƂӘӦӛгˇзӊÓ¼ʁίҲ",
                            'arguments': [
                                        {
                                                        'name': 'ȑҹǔßɔԮƍ½ƞ˰рǝ\x9eќåǬɿμʲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ą\x8bҞȕȐҘЌ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 990454.7400818395,
                                                                        },
                                                    },
                                        {
                                                        'name': '[ќıwЭҤΧʟȊ˗ƎͲЧ/˪҃Ʀʴȷ^øDo',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌөϭ!ПÜĩȰÔƿԭpӅ˗6\x94ӣĆÞȌĴĴԮŊǬїćĂӭа',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3032519348227677826,
                                                                        },
                                                    },
                                        {
                                                        'name': 'c',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӻ˕\x8a÷ҧǁʸȁѵƗȮѯŁϓȫƗϳʎɱԛźϴaр\x92ŔʫȢźȖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4176843986806023331,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӘȞʖҠ҄ͷȡªƃ˲\x82ΪȖԠ\\ʴδӖ˪˭Ǧáš\x91ƞǀнɽƇ,',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3277725934739919085,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҺĜȴӑԟƙ]ŢɀіǠӁEȤȾɒѢӱɷΎϢҼȻӚӌԫΗ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΓƛҜ;ҏѶĚţѢτɾļĝ°ϢʱɂԇτпǜʒȻ¥ęыԠĉ\x94ǡ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɡ\x86ǒ\x97Ƨɰǟɓ¬ÈπǏʟЪʉ͵ĵŤɷԂʘŰЭӖɦʒ˙ˁʋ»',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƙˍлǐůȳɉ0тʠǠύƹʍ˭®ĸŹʰԋǨϨѳŲ˳ƨӅЂ£M',
                            'message': 'ͳłÈŭĲъ§ɽǊςæʘ˺ȒȃӮ˟ǧҍÈɭɬÿ\x8c ëÜǬǠ;',
                            'arguments': [
                                        {
                                                        'name': 'ʀƗ·Ęʳҷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ƹ\x83ŃÍΪӼѺƈīЀǌˤʡȦӂѸȁϻʝɞǗ¢ȹЖdҔɶЃǖƯ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ōψ¥ɮŷӓ˄zȁʫ6ȡËȵ\x91˱ҼǫÍ§ȚˁϔόˏǈҊҵ=Ѹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ҫ˯ԎǺĆɮԌLɀЬɃɱțиʖ˘ĥϳƐĊ¥ŌȚʼЩГљ¢ԣ7',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍƃ{\u03a2ήZÝɚӜʹʁǡ˄ŀв¯ңĦǢţŖŎϜÀ˚Ǔ\x98ȱȀ.',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĲҴŁм˭яϰəʹБƩҺϪŀȵԑӕɞЇԔ´PǧÏȕȺʜϙ®ȥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɢȡǟ¡ĳQȶ˰ŹʥˤkKğɨЮÈǄöŅŔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'АďэԣɂɟȄӝ8рπÚȟ_MêƲЧŻˉƄвƹВȥėΡπθȣ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƿť˪ƤҦĶʏ^ԌΑ\u0381ɎģvӕőȀѝ×',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǔKԧ\x9cÄӴtСǽȁÅѾǁҊԬȬͿG\u03a2үԠxdlUƇҭʀҮŦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʕJќȻԃƊ`ѣ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 276884.1581921477,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥxɏ҈ľƵƆҹӗϙǟјǜ\x99ʘƀ0ЀūŜŕ>ȱȊƔŷѼţ7ǃ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʾ\x85җԙèөЬǉĝǱĀƤ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ïџ|τӡĕ´кǒɺĊs',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѾûǡшFĆğӼãȲҋ<˷Ùˑ°ԥɢƚɗ£ΠŰЯȨt!Ơюé',
                            'message': 'ųďƒҴĲӒVɢ`ʳǬˑ˧ѕƴІźϋȘҠǈǒŗăȽϾ$ԔǅŜ',
                            'arguments': [
                                        {
                                                        'name': 'ʄԟǭǑ5ŞԞĹκȄԓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038b',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ř˽4¥ˀɧ\xa0¸όϧŷ3¤ӫȓëBΧîˑыˑƀÌЃǎ˦a\u0382Ӻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161248.648989:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀМέҩĖƒ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũ\x89ǩҎǭıI9ĄӰĎʔěХϾƽłӟ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ʻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЏäϢ˺èЦ҅Ãˡłѿƺ`³ːғЬҌŜЇƄÝΰo\u0383зǿäϪє',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 77075329689112938,
                                                                        },
                                                    },
                                        {
                                                        'name': 'њѐӨЮԃȷЏÜ˰ȶϣĨϐѭҮɚѴ4ƮӴŢçÛӼ¶èѕ©§ǜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ŏџІɖˮβ˺ԗĪѭśɿƴėƟʌЅҪŮɽНϜxʳBҪ'ȜʊŐ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɻϾӌ˶ûӾкπŠlΈȍþ˰ǈÑş¸žӷӶ˝ûɛ\x86ѳĈɖƼҖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161249.202461:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƓǏҪǓИҲΦʍǅѰəѐΔʁζĊӓНҝԒϽʐџD\x9a\x93\u0379єӌҁ',
                            'message': '5AŝҦ«ͶόΟɺˮŲzŚӻcԋȳ\x86җƞ˲ĒϕƊҺԊԫ?Ҋü',
                            'arguments': [
                                        {
                                                        'name': 'ԘΜԠüʆÛǬǰ ˳ɁςΖ͵_КĝŽȷĴɿāWͼŵǎƠǏϧǶ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌƮͲʌkŝϽ,ЊШ]ɔŭŦG@Ӱ\x8b~ԟœʫζңȧƖ҉ҋǴǊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 999902002630357702,
                                                                        },
                                                    },
                                        {
                                                        'name': '˯ѯȗpʃʘυЭÕȗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 382169.6229673133,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ű˄+ϭǖĳǰǃФɼҠėÛȟŜ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȨҦǜΕSĸǟνƖɘϹХǡ\xadǡӨÖ\x8fǌǜȟӞ%ȡƋŎʔŨμǷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӡƧűѼԝұԃ·҄',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯ¢фˆg˽˸ŇƂԧ\u038dȅђĨ΄Âȷȁ˅дЧïW˰ԉǩǂʧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 5262.763484392955,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͱćóȦΔąʐд',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161249.918978:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѓƴϩˑҰȈȚVɟƱ˷ĺYѮƛȃΞЁϪИξƩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÒҴ˓ŷɛ\x95Ǟ˄ŘțȀɰÍɱʑ+ƪԮϷ6KԭȜұʻǧ˗ϳɨˉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4358625463043737309,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƦǬbΧ҄pīɇƋθȖУјӥťćɶƉ]ȸİȴƯƛǦɒӶӌӇʵ',
                            'message': 'ʋğͶļԃΚв˅©dΩƿϵƟÀŏ˵ǊԜ˪ԨЪԧTԞûѷǱ`Ѩ',
                            'arguments': [
                                        {
                                                        'name': 'ӚƁ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˙ЄҤҫΪϱ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161250.313745:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͼӑSɧƶ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'sĕ˄ͽˢЉ\x8aԪƕĞҍŤƺξʨɴ ȼĹƺΕ,ɚѾJʾ˺\x92ʗ7',
                                                                        },
                                                    },
                                        {
                                                        'name': 'UΌʁɜԝδ§\x81˄GǧġʌУΈÎǡүͷԂȤΫԓDȻʇҪȈiǢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƻǣϔњʅŀ§ʮпҸΞʁ^иӵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8437118650318550452,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȚͱγҞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϙҜĲ˹ϑǝҟ\x9f',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2964282945010035297,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƩıȥҸȹųѥɢŲЯ˻Ύ&ƣЇǪϥʲӔ]u',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϮOϬ˷ԕǯхȸǻӮCg˄\x9f˥ɼϯƢ¹;μÁÞЅΆ҃üɊƫΙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 797964.855330808,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЁɍоѡžеǶXҫԡìɳҬ\x83љ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ԉɻ˶čюœ҉ĐЪϧФɒʫɻÊÙϊȆӲƼôЃNîƼ˸ѻǟЄÔ',
                            'message': 'ȗӊʦҹ˯eҚȍϡȠųӆɅǵøЩĭǲĵ!ŒΥƎӂöѱéǓӫӳ',
                            'arguments': [
                                        {
                                                        'name': 'ʙТĸǥǓŽ˺υ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '÷ԕɲьǦīÇǽǠɄСƮԒ¼ŸȭɇʹσΖĳIͰ·Ҽö҉ºѯϚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȑъ\x85͵ʠőȤ\u0378ě҂ȏҼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȭňŬщ@àĎ˕ʵƂɲϫ\x84ȗԙϋƋƞ҆ӘpϣӣčƷ҃ʼκԞӱ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ľ\x8aԥ˩ɞҮɁҝĶɯɺǏҚǤŸѠˡΊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 967350.8514816875,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƋʷϬЬԑμĝѹŘØˍХμʶƬЦÛǙӆƾ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ðԤȒҊȰXӟˆƠЂ˷ˢĻÃÍŵƗƿ϶',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņɺÌPȺüώǘΡϷїĭеÔǷÞɔΥ˭ңГӑŢϜϱˀ\x91ξʘŦ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3761752041444349455,
                                                                        },
                                                    },
                                        {
                                                        'name': 'yœγŒ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'СɠÓ9ůʴԡЏ}£ǎaųʟŘÆ˔:э˹ãʉɄê ЏȵρЖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 116556.94530245187,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8cŔιǰȈʏʀӂшƳΐʢŭǌɣ\x92',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161251.796078:+0000',
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

            'name': 'ʀԃˬ',

            'error': {
                'identifier': 'ĝsы\x81~',
                'categories': [
                    'internal',
                ],
                'messages': [
                    {
                            'catalog': 'όЀ',
                            'message': 'ǰ',
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
            'event_id': 'ӕǘÇФŧСǰȋΠфÎЩҢ˵RȋÕѤȽĉʥ,ѝӡ˷cUғʆл',
            'target_id': 'Ŧ_ΡɡƺңȾ\x8cĖӻӪʻϬÔZӴȠϗþҺȣĂϲʻ˙ƼɾҬİΡ',
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
                    'event_id': 'ƛ¨ȘǔѓλǊɟâЭϻ҄ΗȓξЀ¾αҺεĻ˵Ľͱü¯Ϟοѫȭ',
                    'target_id': 'ŠŃŔтϫɨЌβ/ϚқʰƞĜȼȘ˪ɿ\x9eʭӶšрΛȓѫ\x96ϰρԈ',
                },
                {
                    'event_id': 'ĸыіɁɂȜȧ[ԍßǞǋǖҥȄԣԋϭԜĉGȭφ"ÜǄʸ:\x8bε',
                    'target_id': "ʢĎƂԉōҲ'öӌͰЫĭȢϧɌѕӾĻÅpȜѠǧԓʲГoӧǑБ",
                },
                {
                    'event_id': 'ƷϠ˦Óг¦ӿǡ»ҸҠǗ5ϰÔüđ£аǩϚġŜγΫЮŲǙ͵Ǚ',
                    'target_id': 'ĦҠӚƖԥǟŚɛĭӦʸҺ˴α>ΙƎӽӆЋŒȌ˾ЊȩʳďǺƊ҆',
                },
                {
                    'event_id': 'ʩЀÉԔɍͿɗǗͿɪƒƶʗԕЀԔƥъϿ7ǋȝ´ĿфˇϑvǉΎ',
                    'target_id': 'ҜǬȖȼİĢъĠǍÚѸɔǥҳɞҡбҩʔpƦʵȠȜ\x81ϹǪӣēķ',
                },
                {
                    'event_id': 'ЙȺùπρǟhǣɎřȘɠžљԞ˲ϙĒňΕΫʉʝКƎūƔԣҹȳ',
                    'target_id': 'řÕzԝǗʭӱ˥АҤӊπźЎУԦȊӨΊăƿыћŦϡӫɰԨт\x89',
                },
                {
                    'event_id': 'åȘʺЬ҅äāԦɝʚ˵Ќɍҗ\u038dØDӻƠΞţʨơøȝƅқ˥ȫӃ',
                    'target_id': 'ѻʄѾȨħоŴϛԁ²ӄˆ5`ʅȞơƫ,ӂĸƼȰӠΚƽɪ@Ģ˕',
                },
                {
                    'event_id': 'ĸǀϐϐǱƃȱȷӗɪϺʦҥĚҙѼԚ',
                    'target_id': 'ɓұґԮԂƹǖĀíԏ҆{ӱɑh˫ǠӲ˂\x8dҌǋдԚɢƅǁӣӔҹ',
                },
                {
                    'event_id': '\x8aŢӜ¢ɽшɤԉÊΩȅϘĨыɧ\x7fÙҀɵŇʳǕ΅ҫ\x84Ɂ\x97Qǳ˲',
                    'target_id': 'ҼȷjpʻҍŗβȞ\u0379\x99ϠʐĬǤԧΙ\x88±ԫӔɯ)ϒ5ȺӠЈӗΈ',
                },
                {
                    'event_id': 'ɘӝǃmϰ˰шɰώIҫ{ʱɭʣʱϥťӅЉù҄Ѥ·ЖǔǶ\x88ԊĦ',
                    'target_id': 'ǈǳ´Г˴ľӐ&ˋȦĞÃ˃ӎ\u03a2ƉυҺΛҫŷѴЦӼԓŝʷӰ˘ȶ',
                },
                {
                    'event_id': 'ʈ˘ќξ҉ҏɣUҐι_\x87ǼzϮ¯ϪѨȂҨūϋÄӏZʰӦϒȵ˥',
                    'target_id': 'ӽόȩЃΑÉMsЮҏыѨΚş´ϱwй%ʠӫѕБ҂Ǭҗİ¬ʎЛ',
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
                    'event_id': 'ė\x8dƥŗȤłƆɈέҏĽЇŕī\x99\x96±ĀŖÓϛБѪГȑˠʔѓßń',
                    'target_id': 'ΪѤЫʟs҄ǁǖťʺЎȿ\x81ΰļūϽύΗǛ]ӆˑɄĸлȓԔŅΉ',
                },
                {
                    'event_id': 'ϮËǫϜ¸`ƣE˭ķÃíϝŁѷΣ˩Юƫ±ϒŇĆԟ)áΌ˻Σ¸',
                    'target_id': 'ѯҐ8ƊʀAįӗӅӂ\x8eҳυѰӢ˩ҾȍԮ\x99щxΦ.ďɽ,HǁΖ',
                },
                {
                    'event_id': 'ʖΐĊ\xadÀƑĈϋсϽљ·^њˋБ3ϥŭԚ{ӲǋγĜŪ¸Ѩǔ\x92',
                    'target_id': '˙Ǩƌφѷ\x87ĔԊԛNɀŅʧΈƦ\u0383ҺúŋͷζǿůЕэˌ\x8fƚԇʁ',
                },
                {
                    'event_id': 'ΗāÏΔ ɜԓŻĳÑОӼ˭чƒ˨ӾʵǟélԒɄʏӡёˉӣʓӬ',
                    'target_id': 'ƅȽuԠЛPƉ*ɑŻˬƷƷӀÃ2ΦΒəϩȢ£ˍȣȏώɶĚФ:',
                },
                {
                    'event_id': 'Ή?\x8d>ѰʌΟĘ2ΥtɖЕȽͷ\x9bƳǮ˦Ǹćă˅ZǴļď÷ʼж',
                    'target_id': 'Ǯ\xa0ЅΩǨя˾ҮɛјȭϼѮώҴԥ\x8d΅ÄԫэɞǬЬ\x89ʉɌÏˈʐ',
                },
                {
                    'event_id': 'ΟʔāԬUКƍʚǖρŎæтʷț%ǪàЏʱ˴ЯЇӗϦʩӖΈԛÛ',
                    'target_id': 'ЄΰǛȎ˒ƳÌȥȼǁũӵǜɩȆʯƴʼÁϙΡyϹƤѵɢ\u038bГϊѕ',
                },
                {
                    'event_id': 'ĸɒüӜЊ˞ӇƧĲƕӿĹʜζӬß=Ӈ\u0380ʻ(҆ӮH\x88ҫ*sɦQ',
                    'target_id': 'њΛǥҬũҐǜBȓʆϮƪĆΌĐԑȶŋpǮɹŏϑΌѴŧΪ½ѫθ',
                },
                {
                    'event_id': 'Ѡ˝ҝʴϥλþ6ñʐˡn÷ԙӚӖ˯\x96Ό[ǵє\x90Ϫ\x9bnʖΛʈѬ',
                    'target_id': 'Śɓъš\u0380ĽaÑΜƘøɞĢαӆǗĚҕò8˺В΄ҭƇh>ӄéɩ',
                },
                {
                    'event_id': "\x8eԜˏ\x85ҁjŔЃõĘҋчɞƟѣΑæ©ИȩӾӆ'Δā\x85ʚEľű",
                    'target_id': 'Ɛȿɜҍ\u0383TʸʻsɰéūԆǑСҡdʨő˽s%ƒ҇ðnӚɢϧё',
                },
                {
                    'event_id': 'Ǳ_ʞśԚ҄˭ʮrɨƠҽɔ˜ӗūɲ²ϤØŽҞԃɅӬǩͿƼэ\x97',
                    'target_id': 'ήԩićԖźӸΊBаВ4ųӈΒȶ°Žϲàƈ\x96ǭŐƙҡƬɶɶÅ',
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
