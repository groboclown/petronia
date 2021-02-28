# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-28T02:46:02.195427+00:00

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
                'łŭȞ~ɞʺ\x84ưƝʛЕɨŏɏϐ\x86ΪѻӀȧФԔǥǃÉ§ʍǑŌΨ',
                'чѮЖωţҕϫ&ҢBŹ(Ͼ˕Ɉԫ÷łӪʟΑÅʼǚѢғ8Θɩʹ',
                'ϩ\x97ԔµǬ˨şǇѧʺǲЯϽɨ˴ĪӄӞɽѯҁρӲxźǟ\x8dÄğ³',
                'ЩӿXºĚdϻљҨσϐǝзɄӝ˅ӟIǛƊõҺƴīé\x80ţʊřа',
                'ϧӦάΊF\u038dѠǾԁѤţ©ЌDƣțӺbƽǙϙңπʕҔԝŋάЃҠ',
                'Є$ӒƘʴВЦάƭˏΉ½ǘϓӾƃҭҶ¥ɱ\u0380ȶ>ȬаȪÑɒԕ˷',
                'áωºԈżǩΩҧЛ;ʶФη\x90îϛýƗɞơWspƥÌåʼӒKo',
                'ˈÑ\x8bŘн\\ǃ\x8cʠΨʘĬBэѐίȉiďĺǘύ˼ӽɼȖąҿӊ҉',
                '҇ā˖əϰЛĺҢтҷǉøŗ7\u0381ϻʘƦпӴ©щҏȱŋʢ°ópϫ',
                'σǐԆţĐɮҒ˧ϪȪ\x9eɃJӋұȎӞӟѩʖʟȣςΩϗńѢϑí҈',
            ],
            'source_id_prefixes': [
                'ЍƵƷĕɺҹQɠŧʀɻЃЧʧҪĔ@ТЛѵÎŊԫǻȱ˼с˾Ѳʟ',
                '˺¯!ϚȉʣɥìǡåʈԂâzʿɴEǚЪø*ɱԥлԈƑȔȼpӥ',
                '\x95±,Ӏɱʨŕ\u0383ĺÛШ˼PǎBœ϶ˉΆ\\ʞƉΔЍ˯BĚҕĵø',
                'һĎˏɢĪӃ_ʓēyŝСϨԬҫʹƃȲƓԪŤβɮ\x83ćҖȊWƭ§',
                '͵қÅȄ®ƙ>ќʾ˛ŗʐӼЮɢŖǝԢ\x88.1ӜɇΌΠˣæƆҳä',
                'ɩĀєÿȾȐƗʴГ¸ЦοþŜǌ\x98őЊԇЁǎҝ1ҧӼϮԬ0ğƖ',
                'èˏӔЙ҃ϡҞѼȐǈƯ˫BҰƮˮđÓҫϩңȏ3ăѥŉтɃЍӎ',
                'ȵφсӝɘɤΫԡ϶ĨȌ$ǸǧªǕʇԐӗҖƶҀʵ¨˴зҿБ\xadƄ',
                'ÎͰ\x83ϡҾϹş˖ʻȠώʢǸɊǻĻîE®EĻң\x8f˗ĄӲʸЙʋԠ',
                'ɈêÙƣµR9Ƒeƴ^Ѹ\xadÏӣҪԮʵӡΊΦŻˈ;эǫԟËԏz',
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
            'action': 'γҲȤνǏε¤6ųɑϖŏʈơɻɝЬ$΅ηƾȕɻȈӂhŪ¤Ũɑ',
            'resources': [
                'oɦɜƺϲɄńёнġΠϯ҇Ư®ƥķ\x82ˁìϯ˂CêơЃÉʒƖ\u038b',
                'ԅȹ"d(ĴԄҏǗӏäǆ˲ђƶʲŹĞԮȗԨѬҕѸYԇɅž΅ǉ',
                'ĲȍѓĶǈԑȢǖДwɊԕĎ²¨Ӹ˚ƇȒɐρӁÕʢŏƫҐ˥˨Α',
                'ҞԈęɥØɻVZ҉уŀʉιˆµΌÐӽ·,ƹ&π\x99ƤϠÃƋҞɇ',
                'ĘɭMėϤӠԊȳȻ0âŊŨϳɧ\x80`ϿĆΰǍҗЄҿÜ©ˈǄϘҥ',
                'ʓͽȐ˙ȔͰ\u038bԌsϐʺͷϊюǰĈŸЮȫĢïɤĚΦǇˤ7ȚҲd',
                'Ȃɜ\x9băӾѪmCҖњ˃ǍůԘǽөǢǒԃʚ8˹ǐºԛԉġϵǥƴ',
                'ҰúźӊКîʤ}ԒǢǮҺàӐхͳх\x7fΏЛ˕ѝȢŁĳҪЛŨgε',
                '§ƈХϭθ͵ʛƹҧ\x98ΟӇǿ˂³×ӴŨOΙvҀϲбƚ+4ϋƽņ',
                '҉ϊ\x9fɛåϥƭЉű\x83ҒҨӦЯЇʊ\x94ȕ˪¶ǾІĪǱűʭʘťɘϘ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'З',

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
            'name': "ȋΒǔӦĺƇҭόɠƔšʃʟϽˬZøӗ'ǘơɡʛԭѢӹ%ȑЬA",
            'version': [
                -2226040971534710752,
                -1544491930001245779,
                -7512827164409249941,
            ],
            'location': [
                'ĩÉƱЌ\x8cÆÿʊχŲǬùϲӚÇȩȑϊħԙҥɌьџЂ\\ƝPɶË',
                'ĲɢǴÄнΤʌʏԋ˵ӌʍŇƃюčèǙԘņʵɆ\x98ĘьӉ˕ƯҺԖ',
                'ˀƧŇ˜Ȼ$БҘİԓÄǂǢĜӨǜɗ½ԗ$εѢʅŮ\x8dʥĶBŢ#',
                'ϑΰɷϋƽŏʀŒĥʬϹŠҚ\u0378ӝҜĭ΅ʰɟԎΧ)ŨǝñȴӪɬԙ',
                'ʌҰӲΧѓ˾\x85ȍĔqӚҁȎμʾǳoϙďЛƸʼɷ˷ӭкGƦʄɨ',
                'ȨуҦӠßХΣѓсƖҕδʬϱȶĝɍĴέʪѢŋ\x94ϞԠωЈқȡΨ',
                'ÚϪΚÓд¿ɂúɎɟʠϚŽӶʞѫKʁ˻ɧĞŤȠԝȑжªʆϮˣ',
                'ӛŔѷÏ҉ɴɞĺ˷ãЙŎ˼ΙǨ\u0378εƶGԧǔɵƥ£ˋ_Ũ?\u0381ȷ',
                'ɪƇ\x93ϥϐȋ`ԠԆƢҩӔæǈӠiŦӐvϷĺӻ\u038dқӼƵԮþˣЧ',
                'ŬоƮ˗юџƽƴQҸˇϕ˫\x96,ξȳЫʉӢʑ7ҫŚľņϲġ˓Ԉ',
            ],
            'runtime': 'Ĭ¸b!Đ',
            'send_access': {
                'event_ids': [
                    'ǣ˅эɃτҐϦͻȖÍ҂ʯŻїΰ¸ȂΆʣ˳ɛѣΩȢԔǛԋ˺Iҗ',
                    'Ԅ\x8dʝҊʶӼөԫЁʏHтδԋԬӸͰѴȯǮϱԙӘƘԭʧӹχΉǊ',
                    'ҥ^ȍφʦϻЗɭаѺҖŗäˬˇkŋǧ\xa0ǿҌȗǒ\x8bϽǎȊʮɇˁ',
                    'ŝ˸¦ԀњʍѡĚsQ*)ĲɕƠʉŠȻAҒȂюȢœѶӉtξúǕ',
                    'ʆǷӻÿè˃ψ$ӏč}ƀæӫǠΔЪұӿӉғȥ҈ĴӄԆеɃĻO',
                    "˜ʶ˲ţãϥϳ¬ȢʭӀԉȉЏ˄Ȍ\x9fϬЂVɔ')ӔīσǕȑЦӒ",
                    'ɕЩҕѰѴβΚI0xѺȣԇӏȵĆԒYшѻӽ\x7f\x8fŢҴͷЙzȒʊ',
                    'Ѡ\u038bľƌ£Ãӏѷѡρӽҗ[ɼɾǒ\x9d˛ʦʣʝҴūҤ9ю˴зǤy',
                    'ѫӐɢћӥұļѥnðɓϼҺԐʋÑ]ɪɒΈӣύ.˶ӏϴѸșӻº',
                    'ʻŏѩϯǥȶ',
                ],
                'source_id_prefixes': [
                    '1γŲɲǙԁ\u0381~ÙQΚ\x97ĉѨǯӋϼŘǂŖʐ0щ>źǈӆόӹѺ',
                    'ʈɥЀŮӨΧ×ɓӵɻ\x7fŪНʭŏӧ#ǲцɦĒȳúâӓʌêI\x83D',
                    "ʳŕƞEԬŮ˓ѳ\x88Ɍλʆ\x80XöƐ+ĦʙŮʉ'ŐǬá\u0380Ļǣӻи",
                    'хҀԫͿӡĜκƗʘԑΪϨӈЏȰ\u0379ĴϻʯˋàzӋɚdȟÏđŰʴ',
                    '·ɵМ\x90ɉԖҸϨȍϰ.ȖԚ˃ϸΚ\xa0òɷŖ·ü\u0378ȣҞƯӌɕ£ԉ',
                    'ƾƓʤͶ4ЍɄÿPɞҟĉǩȒԪÕԏ¥ȦƧӵԙҍͼԚǄ˻Τäɐ',
                    'ҷҋГǰΐЋ.ɎЅÿоԂȥ\x99ϋ\u0383ȇÅƱO҇TӻLΒӻǧư<ɽ',
                    'ЍƧʾĕÙυʼ\x90ˌЩӳΈҍӍ\xa0iϐμΦȺʭaҌѡѧĨǃϑÛ¿',
                    'гťʵ5ŋХʾ\u0383ԡҿδРģUşӑ\x90ӿɋǾʑȘҀžʝҊΙԆҩЗ',
                    'ǡГƹңɜɕŷϔȦ¬ҽɯˋÖȏϦЬ¦ɼʾԪŢϙ˧ϰЮ3ɅĐȈ',
                ],
            },
            'configuration': 'ЈʌФńЎNԃΦȶCњёϣШӐkǱ¯ȖɩȁVƨǅʐЛɇȆÀɰ',
            'permissions': [
                {
                    'action': 'ŃÛƠɕͳѼɰèѯӔŁЉɐȜȋǵѢҾҸƲɚBΘ|˼ΏƆɞФԈ',
                    'resources': [
                            'ʴ˵ǚеˊʅĉ©ЃļЙôǩɏлȣôÉʔ\x80ȪϊńԦǲ',
                            '0ЁļBɠǲӐЛȅ¾ķƴőŋѥȧϙӍǡҳɊϯėƹϸȡԚiһī',
                            'ɽҬŏϚĞϭ}ΝʫԥѯʃĶЎ҇ЯЛȢɑТȡȮƉԀʞǉÃȗѫЎ',
                            'ĺΓȦΙҗь¥ŖӄĠ]ǬǧҧÙ\u0378ҠԦwÒɧβǬέƋϩϧȘ6ѩ',
                            'Ǧ\xadӄɱѶzͼˋˡºȲʲ)ÖӄȒǭˑƘÎ˱ύŨȅHѲoŶвӂ',
                            'ӑҽЃɔ˷Ӄґϛɛ|ʭҒԇȽə˾ӼһɖѼǈǋ{γĸˎ',
                            'ǦҕӎεĬȘʉÌƂÏϬѐZĆʚуΐȦɌϺ\x95]ԥҘËѯȗȮǆɠ',
                            'Ϟč;½Ȧ;Ǜ˵øЊǑиЖҲý˒˫ƾŲˤȝȑоϼłϊɜǺƏϞ',
                            'ŨΥIҶńɐєΊ˽ƝȸƿŬʀ˘/ΗΤӊ]QčÏöŭȒɏӋјǃ',
                            'ŕ˭hӗҎƀÓԉÿÒѕӊԠǧȉȊԊ\x92ҷȀҷϐ²ʣԬ²ϙͳӵƂ',
                        ],
                },
                {
                    'action': 'ĂϳȼШǈËӤĄ˭ӡșćÏξ¾-ǱƖкƬщөɍˬϒNO˗Џј',
                    'resources': [
                            '\u038dđĤϢZʼʷȎЇ˼ԙԂʡϺĩҴ³ʂ҂ҁˑԠƮ\x9fșŖӡΖԖӥ',
                            'ƥƇҽюԌҵԜ\u0381ϕoïәǣØƺǛïЯɮHĎʴƅʳѤȊİҀƸʑ',
                            'ƋÓΙmЀïӸӺҢ҇ϴσѨûȉƥȤӞҁ\x8bΝ\x8a҆ӭЀʎȗҞǓɏ',
                            'ıаԮĜǛũ£йOA˲˅4ӃǊ·ǬѪʤ[ŶʱǂʉƷĸ҆щΠ\x8b',
                            'ЇӜːΤАñҐчĨǶȿǈɁЙǵ¾ԮЃҨːԗŻɑʹƽŉЁДшX',
                            'Σ϶ЯҸïċВ)ôơʟƅŗӅŪƩÐϩRѬӳŗчϲѺɨƀíɎѣ',
                            'HӁԄѽԭϨ&ÏȥÁΙӲӔѫѯƾ˦ːΪӎˆͽϕ<ěӌģҽüȱ',
                            'Ϥӻ ĉΥʎӬɀĽϭʖÂ\\ƍҵ\x9fʲӽȄϰǘȦaʗƂӧǨíͻс',
                            'ʴkȶӗңϔҽԧǷʮʲ:ˤсșɞӒǹȤǲҨèɕϪАҏӄǎϘɍ',
                            '®î˅ĩȝҽĦӄʪÇĄpзС˯ц˱ȒɁÞǼϤҠǤˋȅɬΆčԢ',
                        ],
                },
                {
                    'action': 'ʕҧ3WǐќˬGųȄ҄҈\x87ĠĹŎҺԃƮѲԬΜӧôpĖyƃЪ÷',
                    'resources': [
                            '\x97ĹƚʗºӵńóιɜðѐӶɦʁΗ\\xлЯ½ŵ\u0378їà\x80ʉЯȭŔ',
                            'ӖÆɼŗұõҡK/йќҙю˂÷ϝ\x83XʜѓËǙÎͻҼƼƊ¿Ɋ˂',
                            'ӟˎԘȏЊʞ\x84Ϟѣɥ)KʹԗлԟŴțeΕ£ϑʽΤÅĀńˊҵĴ',
                            '˃ӮÆÄҧѦтӤʞԉʮҺ¸ǇϙǈpƃОƈԖ&Ɵԣ˚ʋˌĚҹʖ',
                            'ɵgǹ˂Ǌ',
                            'ѱ*ԦɅʸ˨ϏƸӄ3ɷy˖ϊӮҊĂ6ѩƘ¹ǩ\u0381ɡϤӧǮǣ©˪',
                            'ξƦ˹\x7f´ˑӈyƧκʍӤāïψɁʋș3cңбќȻįѣɍϢԐҫ',
                            'иˏѷμϰ°ӗӹ!ӳRҿ˥фɃŢˎĸìҿƠюĔͽˇ/ԕȏȍΊ',
                            'đ=ØѠǩə$ƲòY\x94рԈʻҾĵÍǗԭ5ŰʎȇĕǞΦАWЖe',
                            'ǞѹѫҮȒhEȳ\u03a2¡˷ƨϤŤԮƙϔӿ§ƭʘ˸\\ϰùӤђφƅ˭',
                        ],
                },
                {
                    'action': 'ԙоķȧǙҀmĲбJҕǦȄѵҖΜґΞԬʹ!Ҁҥȵ҄ɣϧԘȡƄ',
                    'resources': [
                            '\x8eБҴȘGáȁϛԜǪĖӋӅÆʄʅҘNɗĂϐ\x92Ʃ\\ ҵɠˮÜЃ',
                            '_Қҥ×ОǋԣсҥƄǣͶʉƹˌ˨ǖǱȸ˖ŉѩɷӐњҍϝГϡ¾',
                            'ЎɭΝ˓Ӷ΄w·Λǝ϶ϑҙӝÅʷ:ƚ\x8dʌɟѓ·ϤŘҼŤFϳ¸',
                            'Ӵ˨ÐȚʰɚǚάϩ΄ãu_ȝԠE˩ȢȺǖŰȷ\xa0ȕʷ\xadӳҪŃ˨',
                            'ωĀſőIĖ˚ø˕Ѭø ɭѝӮȪЙԛĠ\x92ѹĴˉDӄЄҩӪð˽',
                            'üǵϛˁÿ¾ΙϺƳ`Ϙʴʢʽϻƹ˾Ҟхίϯƞ\x91ƩǖžƇ:҄Š',
                            "\x9dΠьèƚѶшкҕѴϽ҂)sƘԧƦҿЈ˒чǐɔ'ŤPƈĳԞґ",
                            'wζ=ϬſQмӽΖ®ĦșêȌķЮҌёІÊԏƒǛŪȥԖɏɲҩż',
                            '҉ǫư˓ҡ҈əæŒӆϳʹɼҰ,ɪЗԄÝgƮğӋ˱Ǎƙsɫȹԕ',
                            'ЪƲɻ˚ŭӳɉàǎп˙3ȵΔƲɒϩʭōİӹβιҊȷǹúԁɌũ',
                        ],
                },
                {
                    'action': '¾Ù\xa0зӖԆíъъˉƬɹ>˨ЋԡӝĂэĬ\x9eøп\x87¬Ӫ\x96ÿǐν',
                    'resources': [
                            'ɀɷĻÞŐČTԟѴЭϼѕ˕ǬɚĢэy҂γˌǡɦɽǩȟҁÓӤǭ',
                            'ŖOʪƑ¼ԩ®п\x8a\x9aƚǡƹĤԈϺˢǹȮщЍżΗσÎǍƝ¹ʑŝ',
                            'Ηʧ˱ǕҮӖ϶IƟǗ\u0381bƺ(c˕ұҫї˕ɌжWȾԬƂƖ˕ӆα',
                            '҅ƎԣЁρĐɳô˘Ήɢ˯ƌɩԔҿǲȭγ/H¥þɄŠ(ȥʠάŽ',
                            '΄ҢǃφJɿԓǔͶǴҏƢӾѕĬӼʌaЀƋÁ\x98Ʃ˘ГѿüĜ҆ү',
                            '˻ƒˮΓÙȩӤмɡkЮϞǗΑeЧ˒ñǆ}ǷǠ\xa0δфƶȫϬʘʗ',
                            '˝śώ«ǔйɳÐϰтβƋŅ˃Ņɋ˪ЯȋÁLʟϺԪ\u0380ӣ˕]щϵ',
                            'ũɮțÒÐтˠˍàʎİŸԋÎ\x99ǯӨļĊΰĊǫю2ӱϟ\x93˦\xadʀ',
                            'üѥʝңЈιНԖҦŷƜâҕĢҼƛЧϟ\x7fеɘʻ҈ƁԒѓӶʄĞL',
                            'ǥζȯĻє˹ĭë\x80ŕ\x9cĩ˦Ԍ˭ґj\x82ҮȒͻǝƵ¶Ҩ˭Өʝеø',
                        ],
                },
                {
                    'action': 'РŰÝͱÌқãӠҵǦΗĝ˄ĺϬэȍӚoɂɿ҇ǀɃ\u0382Ã˳ɠāĽ',
                    'resources': [
                            'ΐ҅ϾȃÝν?7QŮWĥŧǸӨ\x91ԥĞ=Ьѳȩ¶Ǳ;ŀɊŶԍà',
                            "ʭͷ'ɸɔҒÙӋʬȻʵŔѐˉԙӗţĵΩ\x97ѣѴѐ˝5ԅǋΨm]",
                            '˩ԨӒŜÝŗԗϟɾʭΙ˴Ƈиǹ]ŷʋˉІȔҍ҅ǉŌƃʥ@Fȶ',
                            '\x7fɆΧ˕õӠTǇŠψѻɚĿѼѕŁǤіЇc\xadҙŃИÔǮΘVȹf',
                            'ɻϻ¹ȠȘ\x9dƑƠӖЂ¤ƫ\x96һǦuƸϟϯƷ˯ˣΫȵŁĴ9Ķģʺ',
                            'ҰѩŽӪԗԥʠȊʕ$þūɹԉƯб\x93Ö$ƠŢ˱Ԗ˾Ћ¨Ԉ£šG',
                            'ȁҜȕԚПʕąĸˁĊϧʊΓɸÌȵà\x95ϑġǻҮȂҔѹӴξXǿȘ',
                            'ʢĬĨǔɻʃþ-áԉѨӢ˔ѕɝ҃ЃËóȷĻIɳǷԦЩdԅɭη',
                            "й˕ӂ®Ï@рĕԫòŪˀʚăʛƥѪͷʘŚӯ'|ҌɵŜ¹Õ˶À",
                            'ďČǖΪĭƱʶʯұ˹СҸǰŧ˃˳ҴҸ.Ϯјȇԡҹ˚ԒƧʈǵ҂',
                        ],
                },
                {
                    'action': 'ˣĥϯЇŁǾıeϬŁʚņ˙ŧбϘҴиŶƬĺɞӑƯˆƝЙɐҊɜ',
                    'resources': [
                            '\u03a2Ǧ˙ζȼ\x9dŪϏшƇ8ʡ˥ͳе˼σ,ǉíѬɍ\xadȿӧȼͼЮʾƨ',
                            'Ŝӏƿ.ʗϣʫ©\x9e½ԆȪěņ5˔·ˎ\xadŴзϦΛӯƿėЋӂtԃ',
                            'ӲΑǼфɧч.a҇*ƣӃӘsԡ\u0382ȦōϮ˘Ӌн;_Ħŀřχȃȥ',
                            'ҌĨϣИШīǙ˶ӃĽȌɃŨϱŎŴԋԜýļŲўˬƇNďēʯǮ\x8f',
                            'ŪȬͽȰȪϹÌӾ8ɶˍʏϺȱİөɻéǦɜ\u038dЭІҞʇøDνъԁ',
                            'Ӑω\u038bϚџŹϣѕȘˊƌǧϡźV!һGͼåѕσԌϙĩЈʡĄҰͼ',
                            'ũƜƣ°ƛϲ\x8fsҼIŃȊŘԝĬąɞ҂ɰ"сϒđјԦĕԧ\x9aԃ=',
                            'ЅˊǟǧÛúͷƁÁԋЖԥҰSí¾ҊûȇϫȆOҬңʊăȌɓ{ȭ',
                            'ӡƇҵķТʬeжΚwȵǳϴÝHþƞǝmѸɋǠ˒ƸŬрɹƱǮӸ',
                            'ǋ',
                        ],
                },
                {
                    'action': 'Џ(\x9e;ƪĩŏ ЍɊώƹʬρɕȒǏà¡҉ϺӴǮҭǾ˪ɰΙҫĘ',
                    'resources': [
                            'ЇŵͻʉӴęĊό©ǘϏʞҚʝˇǌêѓBʱѬԌǇɌƝϛǒɹѕ,',
                            'σёξўЗζϼɉЋϵӭʚǚӃʴ҃ЪԝǒϰăԄТ#ǌʥ\x7f²ԉǗ',
                            '˪Ϻ\x97ǡƙΆȴȿӖ\u0382ԉÖɁνǈԘ˲ʕɌƺ˖´ïώ#ĒЄʾҶЪ',
                            'ɣȔǱѻςԦɹϥόͶǽǬ\x94@ƟæƆЩνrʐǗýōԨǮȭSƪѥ',
                            'ЙŝŁʞȍƞʐƸұRɂȞʌȄ\x8dƏǧɳˇʄŰ|Әџԋ˫ҭϔˎm',
                            'Ҩ˼ȄϽɁҌϹԌƂӮϙɽyƋ΄V҅ŪĦɲŏϷӀÄæȗҭϽӱԠ',
                            '²>ǝȸʇʮȎŪɸΤƯʢ˨ŘώРԍфɾɎåΔCǹΐͳƶЪӤҀ',
                            'ĢóԨ\x86ĺƨӯԊВԠűϚʊҏμГʨӾƝˌĩ·ЏȓұÏѤѩȭɻ',
                            'ʝĎˈŪıїȚӊS˽ȵӜĄϔíʚƶԞƪűeʄǁϫʴ½ýѬʥǓ',
                            'ҕͺΠJͼà\xa0đʮʮɁϨȀʒnȼΐêӆÓîȗӭȲƠв҄ƀʄϑ',
                        ],
                },
                {
                    'action': 'ǉҎ˺ΓɈǢuԢĳóЧр\u0383Ҭ\x93ԟϲƂϫОϨƜыɚҨƟǊŎÓΟ',
                    'resources': [
                            'YEšӃѶɪŒUԄͺξįĖϛůϤĮГŤÎɉԗʕҩȎʛ÷\u0382Ѓϸ',
                            'ɖѮ͵\u0383ЛҮԙёŸÆҷԅȐʒuƳÖ˼ƈԊ!ʱӜƞǱ\x8b·ēʦʜ',
                            'ɚӭɬҀɑUŋ¾кŷąԩƝЬģ˂<ΌԌƷƐҬǽ\u038bʫŋǴҾțԧ',
                            'ɄqΞʼĽЮʟ҄ѐɀʻϦҐĚӥȶЈͰʌҗɼɿϦƅϱʆѶБԍ1',
                            'ȩóėʹĥкŗɧ\x9eӄΪɷǚĚҋƕΤȓˬŗǈÌвǂˮϻɃƘƓқ',
                            'űƷďϖԟČΚ˃þϡѼ',
                            '\x88ϣȸƪ˄\x83Ϯєýˇиǘ_¥\x80ʒϸфøEǙǘŦѣ\x98Κͼ>ћϯ',
                            'OˈӦθUѻԆ˱шǖкƂѴњӵŊΤȭʇ$рЋɽĲèάҔσ«ԟ',
                            'ǺϢˠӫȨӚˇӶǋ\x93ðѧ°ʠƸ\x8bʲ\x8bǌĸ¹ϧϡːƧÜ[ŭA˜',
                            '˻ƿDҥ!Ƹ[қīʏʎϻΟҦƲȎĐĦŝŦFͷƖɄԩőӏɱӂҬ',
                        ],
                },
                {
                    'action': 'ăBԮʭ',
                    'resources': [
                            'ˑĆьʟ«ΤԘǻgÕ˃Ƕƿ¶ǈԅϵӑǝǝԄâÖZҜ͵=ȱ\u0380Ř',
                            'ȓơϩŏȫǮѪҬ#ǢβņɨщӀŖɞŨ\u0383¦ŖpӤπ\x8bɟ҄ЋƉ˫',
                            'чΖμĿ{ǋΦŒƌLνƪѻŤÇџǮßǎɱӟЊì\x9e\x9dˁĢ\u0383÷ϩ',
                            'ǣʶ\x83Ɣ҈ćҭҨшĂeıѿŪɏäˁϩ\x8coɠȳȜѧќϚȅϰԮʅ',
                            'ԋȃŲͰQ°²ӟď˼Ό˖ЋƃηАŚ1υз˥žaȺŔt˸εљĪ',
                            'ŧʽіĳqǨʼ2ĿϚʹҼϿlЉјϝѦΡmʇ#ˡϏԙҳÇʇ҃н',
                            'ʜʽɋȲņǉ˯Ċ©fɰŊѲɹɐʝɨӫԎӀϏάʸυ·ѝʪӁöĂ',
                            'ó˓əɨźưđсɪƾɅҵʖМӊːơϑԠ¨ō˫оį&ūǮǎłŋ',
                            'ƥȘ´ҀÀʖňҫˤӑǵӂː\xa0\x9eʶԦǶАϯѹрƗЍ҅ǵˋŜ:ԃ',
                            'ȢȽԄŔϊњĈǎӋЃгΧŀҼŭ\x95ƩР3ѵϴίƸōŬуќĕӞЪ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'КҠғ',

            'version': [
                -6373344597744337325,
                -30369174262404122,
                -9189148721939893042,
            ],

            'location': [
                'Ш',
            ],

            'runtime': 'ː',

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
            'name': 'ʀ|ɍÆΡʲ\x87ȌӿŪûĮGԙȞрȘИӣәөȳӗѬ\x98ҋǏҺмѤ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ÁŘл',

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
            '$': 'ˎɻϖőχϋʤ\x85öǝӠеʃÅͻŴEПŭЫҜŀmж\x89˘ȣū҅˕',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2895711146395541695,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -57331.09636023782,
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
            '$': '20210228:024602.121418:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ˢ¾ɸβԬnĥǝϱϻʏňρȍȈʼ˝ţγɿц҆ĽǇҺӛЍ˸Ǯʐ',
                'ԧмϱʊ˯ɢˊԖч¸ɋРбƎϸɬ&ԕľȍɑΜЅūïɇЙwŊʒ',
                'ӹǻ˅ӽGƞɵɫT¬Эǥȏʔϙˉ϶ԔfԛԂŽȳϵЙӁ$Φĳʹ',
                'ƥũöǔáʇʨŔўҀϴƲÒϗȔ˄Ж˕ЈНϛɣȃϰҢЄcšΦ϶',
                'ʚͲПϝǖȻʞɋˤчâƧØů\x9fǈ͵҃Ѻɬ÷ΩʼǢʠHɂǶǸƆ',
                'ûǗӰӼҝϫĸ\u0378ˮͿˀǇƷĜɪ\u038bҁΘӎĚÎǠƎкũ¶üÐƎÀ',
                'ʰѷǨRѳфǟѨʼЃȱǓ&Хʀд\x94ΙʵѽұԂŏЙʝˀѢӪ\x8eƸ',
                '>\x87ƬΑͷɰҜǗȺȾ((ϼʞϼтԚυуǅXź˯ӸȒЪƣĂёһ',
                'ŴǄƐĂʦǦʲɐŭҠМmūȨzˣǤϰĝΦ¾εѡӑΈʉƞҺĖЬ',
                'ǩĮȆņLɋЀɢԦΡ\x80ԜǶȢ˪ź¢ưƭӳԃßÑԁCȪҲɳģԕ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                1825093893243863064,
                -547442147669748879,
                2422878999334373299,
                8987962971880384896,
                -5339716871960498568,
                -4382459485205999685,
                4332931207688782477,
                1194052515496634025,
                -7186969304723788372,
                -7075183634684264895,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                376578.7223515856,
                604487.6285835992,
                -12793.788560465196,
                373362.0228559188,
                -4105.485609444164,
                74934.79343432243,
                5209.883242808428,
                -33463.63504778086,
                461559.3461477158,
                692484.0299217838,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                False,
                True,
                False,
                True,
                False,
                True,
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
                '20210228:024602.122414:+0000',
                '20210228:024602.122430:+0000',
                '20210228:024602.122438:+0000',
                '20210228:024602.122444:+0000',
                '20210228:024602.122450:+0000',
                '20210228:024602.122456:+0000',
                '20210228:024602.122462:+0000',
                '20210228:024602.122468:+0000',
                '20210228:024602.122474:+0000',
                '20210228:024602.122480:+0000',
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
            'name': 'ԦȴҧǡӫɄ˩ëӮA˲Ǹr_ȄƞǮpʻȝǁȡa§ѱǂƕԈԛɽ',
            'value': {
                '^': 'bool_list',
                '$': [
                    True,
                    False,
                    True,
                    True,
                    True,
                    True,
                    True,
                    False,
                    False,
                    True,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԇ',

            'value': {
                '^': 'float',
                '$': 995819.7233354629,
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
            'catalog': 'ÝͺұαяɰƨeƙǦǈ+ëǐ\x9bļԇɏƈnԅǝɉ\u0383όѠѳĒ\x89ӡ',
            'message': 'ѐfʦƮǱ{ԈQӬíOύŴȺǓʩϿʧѣ͵ӰςͷǓЮӚ>\u0381ϔƟ',
            'arguments': [
                {
                    'name': 'њɶăʛűΦTȫʃƶʻϐҁ˂ӃΕŃҷ',
                    'value': {
                            '^': 'float',
                            '$': 651650.342290919,
                        },
                },
                {
                    'name': 'ɞϴNɇˁñΤ#²ΊԦӊ˅ʎƿʄǆɤѵμŃϰҦъЋϺԟɘs2',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        "TbýϱŹ'ԧʣÔЉøϜ϶ʨΰ˶ћѵԆӪϻȨ7ªǇɒӭĲǱȇ",
                                        'Ɛѕҗ\x9f˕ѬынÊȅɜIʬЏǵќ˴$ñǖϒҵәǏ¼ҽϺÚƓˌ',
                                        'þρ6ȔŐWʃ^ǧˏѷʀȧƫһȥмжʂǛͺ¸ǹȓûʿӑŐcˇ',
                                        '©eӨÊӞ\u03a2ҺƮɄѾG¶ʗЯƭӄΐҸˮ¦˅˶Š\x7fFжͳѦɸʋ',
                                        'ˍ\u0383Şϵ˽ԦΨђδԗǓԕļ~ԗѤĽýȻɥЮӲͱʫ\x97ӈ˱Ȗɺӛ',
                                        'Ӂ\x9aӶ-ϥΟѕÁì$NRЈϮѯ9Ƴ˴ǕѱЊԌȬ\x81ɵʊ\u0381\x8dõɔ',
                                        '\x8aȦЖʛɩѫeζê<ƳҗʛʍџǒκƁʠˣҍЬӁǹӤĲΧ˹Аĕ',
                                        'ȃȏL\x8aӶӟ҅ǅѴɭƾȱäƱ(ԖƙԡӵđŊӅ\u0379Ìƪ˪}οԌ\x80',
                                        'Ã{гȹ]ΦƲªӦѻӞΆĀ҃Ʋюϴʥ{ĕǭхӹbУéźʸƑІ',
                                        'ȼÿʒӽьѹʠ;˜ɔÕϚϜƽϥТ\u0379я\x9bѱτ\u0379ǸӮԬˌЖҥēE',
                                    ],
                        },
                },
                {
                    'name': 'пфҎębʫωǢƂƌǨѫºһҔ҂ĥҗ8«ҕӌѤÆǣ«ȂϾʒO',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        502089.64067405125,
                                        -9421.568533361424,
                                        314756.92633549566,
                                        279939.56337216566,
                                        790949.5148290807,
                                        360113.31583676476,
                                        187943.06351612374,
                                        -34003.229024061875,
                                        637966.6265100727,
                                        -18108.35838087002,
                                    ],
                        },
                },
                {
                    'name': 'ǹͻƤʭ¸˒ůϔ˂ЦlȬԃřb1ñӺ5ҐӔ˪UнĴȥв',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3055479648819430023,
                                        5342450472799878565,
                                        3132533159967280251,
                                        -6091188900625563004,
                                        -2660642480172644469,
                                        2236010526530688212,
                                        -2228904330054930937,
                                        -2055165877205662536,
                                        7688735746733868873,
                                        -8532671822454959804,
                                    ],
                        },
                },
                {
                    'name': 'ƹɔЌŒĈɅǷѠϣˈ¤êÆíжȋÉʅ͵ϲÆԄĴΕŃϴɂǊǅћ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        747894.5905921913,
                                        811789.5608037921,
                                        735637.4196753321,
                                        147178.7666109072,
                                        355368.70878843253,
                                        698963.522710684,
                                        307153.47435624537,
                                        896719.1558757591,
                                        956687.4860490777,
                                        191755.14032258047,
                                    ],
                        },
                },
                {
                    'name': 'ϿˀȿƘ\x85ǲ©ÆԀǨˡԀɇ',
                    'value': {
                            '^': 'string',
                            '$': '˨üŊĒĮʏɨsӃԔшхђ[ÒÄб҈ʚÛ÷ыωEƔѝșŦ+ê',
                        },
                },
                {
                    'name': '\x96ѲΒЯASĎű¡ϗŊƃ$ÔʁʋʉȈюϧӵ|҂Ͻ\x98®ѣKɉ҂',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210228:024602.119779:+0000',
                                        '20210228:024602.119799:+0000',
                                        '20210228:024602.119807:+0000',
                                        '20210228:024602.119814:+0000',
                                        '20210228:024602.119820:+0000',
                                        '20210228:024602.119826:+0000',
                                        '20210228:024602.119831:+0000',
                                        '20210228:024602.119837:+0000',
                                        '20210228:024602.119843:+0000',
                                        '20210228:024602.119849:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ɳȹиĬζ˧˰οßғ҉/[Ȼϗȡʙѝж\x9e˯ŅϸΚԒGà',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -2411891023636886615,
                                        -4386466610026599560,
                                        4055132421182608730,
                                        2124449896045710591,
                                        6225622873161111926,
                                        6207033075391731952,
                                        8104788040018623880,
                                        -3478698450889123135,
                                        -7234729282368765374,
                                        8731495878458573608,
                                    ],
                        },
                },
                {
                    'name': 'ʉϸԠʡΎǆЫ\x8fɑƃuĚ\x94Ϳɘ',
                    'value': {
                            '^': 'float',
                            '$': 489715.54997782793,
                        },
                },
                {
                    'name': 'žɼіɞþ\x90џϮИŬ\x84*ˤʛÁĶĸԘœ\x9dҟɐêĆϥӽɹȔҋΌ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ĿўŗӾĢ\x86шƠӹ~ĸΛʘЀŬɌƀБǵƝ¿ɟļüВ˩Υη\x989',
                                        'Ε\u0379ԦƻʑϙFЋӂæˋїяʹюcâǄʒҶɨ˺ѕĞԁμҠZƷѮ',
                                        'ȳŹҤɚȟ˶ԌϖņŘӖԚķӺνϘş\xa0ӃƸ×ʳͺʍ˙ӪύȽԀƛ',
                                        'ιһԌąоƒ,Ĭ¶ʈŵȠʫӡu˰ȮȰĲԌɓϷtҳIɃϊˮĜť',
                                        '1ӣԪЗÏǌ¤И«Ӳ¾ēԕǣԚŇÅТȞӑåЅŖʨ<ϗżɩŏ˹',
                                        "ԟŐŘļЊʋѥϊͱӶŨşǨяuϩ҅\x85ũõі\x9aGČɨϹǝϖ'Е",
                                        'ñŉҸˏћnƤŤǉŬʼҳͷɊФΞȵӄӮ\x96Ȍ˸ʵã\x80ɇÈŀӐɝ',
                                        'ҫȄˎѿˑϬţϖǜҟҐɌͷ\x82ʐŀßӵƀǏŲӵƐɚЁ\x87ɝǚ¬Κ',
                                        'ÎÿėёDѮ\x8bŎźӈӁӥϛϺԮ¶ϋ]ʶǴΓӅüů¶ƲŔ\x98ȁʴ',
                                        'æƥVǎрßӃ9ЛưðЁˮΒ҆ƏҴҒʛP)Ԇ˔Ϳ\x8aԝԛCψȏ',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ӄ˥',

            'message': 'ʜ',

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
            'identifier': 'рϑхӝŌҨȏƿŪǖ6vΊǿәƩҢʂǭѺӦҠɇƹ%Ԃ¡ĭєЬ',
            'categories': [
                'configuration',
                'internal',
                'network',
                'file',
                'network',
                'network',
                'internal',
                'internal',
                'os',
                'network',
            ],
            'source': '¨Ƚƾϱѕ϶в҂ΧЗìˆ[fʢ˸˳ǡѦůЯŕцćĕƜѳâһ\u0381',
            'messages': [
                {
                    'catalog': 'ɧɞѬԌыȦćɐƪˋãƺÌҕȕɰѡČфϘҟȖÉêю\x97Ѳê˦Җ',
                    'message': 'ҜˎͷLǎWʬɟ¨αřĀӵϴ\x85ȁ¯ʹЊЫ΄ǕɃǜϟҦźͶ\x85ʠ',
                    'arguments': [
                            {
                                        'name': '˟ɸĮќфўˌԅ4é\x86όɕ˽ćƻĺɘή˵ԈȈɂğă',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǝͽώǠÏўɔ˃Ɋԏ\x86ӛԚłҸkjϷƏчɒӝαƿҞш§ӄɘá',
                                                                            'ьɨǴˁҏȎЫԬĈŎ\x92ĚԢԠƨҝуьЁƙѶ§ӷ\x86ÈәƉαŨӲ',
                                                                            'ΑԬlɧӁ\u0383ŻΈȋɭ\xa0ѮSĨǝÍ\x7fíƵќ҇Ǭҝ\x86гȠLӰĦҭ',
                                                                            'ʾєäʧЩɀύ;QԪΝЅƻŖśԨ4Ќʃæ«ҬҪǙ]¨ȩϾѠӶ',
                                                                            'ŁКĺΜ\x9bɝƘӆgҒйΛǹŐ',
                                                                            'ĆúҢŅӳϕнЩǧɕӆңάεԎßθɟ\x98Ӝ˻ʬKʦͳ˟ƭ˩µР',
                                                                            'ɝɀ\u0378˝уʫԤӥ£KēɈ\x90vǍ\u0379ͰěǎưӢҔƲ˚ѭŰ\x8cԊӵÊ',
                                                                            '¿ʔӾ\x87Ð=+ƝʣϝηɊіļήðƚξť.ԍ½\x87·҂ƦҽgЪE',
                                                                            'ĆԚʎВΔӓЅΝЂʎеŐÝˊҫƻWҒЍԣřѩŲƦώ8ҋƛˇӂ',
                                                                            'Ũǡғȣ:ωԀϻ˕ǒϳÀ+ƑЮηÈɫҟɇΐȹ6˝˥ɢѿɋưҋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЕŦȥĐ$',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2900510215332475932,
                                                                            -2702246656557445562,
                                                                            -7235474197451860124,
                                                                            6171173236682928737,
                                                                            9142169898299147230,
                                                                            -2885831528939528795,
                                                                            4866227797453300120,
                                                                            -6635408564337021324,
                                                                            -5356917768004855751,
                                                                            -8876384922715959017,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҜӤÁTʿÏ/',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                        'name': 'ǾҔͳȝҐ\x86ȟӹ\x96NЖȽŖȼБȬӿƼԣпˊӌӢƺг',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ʒùӊһ˃Ǣ÷ϔзǿӤ¢ɖҐʐөǄԮɳĴĈůЭӢƻӂǅÈͶɔ',
                                                    },
                                    },
                            {
                                        'name': 'ҡ˚ˢǕ҈ǯʙæɟÑȨ\u038dƿψӋҕŧjƶėɨϥĔƚҺɹǆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1409689164916111585,
                                                                            -9104542541350329041,
                                                                            -6058795951751685201,
                                                                            -1995155665194973149,
                                                                            3077034560921781208,
                                                                            -5237439762306600270,
                                                                            -821358836817700624,
                                                                            -7330033177998895836,
                                                                            9209372629592117683,
                                                                            -4877812871558718613,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӡωЮǚǫѰýɾғǯ˱ѳrȧ\x9b\x85Ƹ\x8eƮ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            434701.80594524706,
                                                                            693958.4035125895,
                                                                            149402.47037965307,
                                                                            674282.8497471798,
                                                                            233004.7895561675,
                                                                            616407.9522542319,
                                                                            836656.46272631,
                                                                            323717.4939733567,
                                                                            900225.5831446775,
                                                                            296.00488519246574,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˤǱ¼бмʧԥoɰÃŭǑүӆ8\x9cƪβҗǕͼғςˤԓ\u0380ĲΕϻȣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5461701069829994744,
                                                    },
                                    },
                            {
                                        'name': 'Хº\xadЧΉȢӴˬωȮŅƒʌӤ˖ʆĩǤȥ˘Ƅ\x85ƘĉġǓƲȌƂұ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'N?Ň\u038bɨȓѝ3Һlƅ¡ɳûʑkɵţΒЋƁӱÎͱŝЁΕԧȮĜ',
                                                    },
                                    },
                            {
                                        'name': 'ƥˁѩ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024602.086206:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʞѭʫ˶ЕεßнƓԡƉ˘ђĘϺo҆ԫͼÅȁϫǹȕʀнʇԊƭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
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
                {
                    'catalog': 'ɾΕǍӘϠȆq¼ΠϫʲԪɩҿ»ќѝʷƱέȋ)ƽ*ԕΚɹ˧ɔ҉',
                    'message': 'ɵҩӎȿЅ\x84фϩ2ŊӮΦӟŦǏ²sӶѧxΫͺгӪƪưӿȖʵ=',
                    'arguments': [
                            {
                                        'name': 'ñŶϽήлѓƠĳͷĞ¡ТʬԑĦҏȘНҗґρҳƺe\x9aŝρ\u038d',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            67463.88656333441,
                                                                            -37723.03688330173,
                                                                            499998.746502078,
                                                                            293745.9415095726,
                                                                            599536.5681144512,
                                                                            919356.2173507744,
                                                                            192873.33806812734,
                                                                            815129.6664552747,
                                                                            -68219.45831819777,
                                                                            404981.1208883765,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '~Ƕ҈ɁɡԠϒфԫģʥѮ\u0378Uӊȭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˲ʐҰύɪԔѩΞƟ˞Ԁ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024602.089175:+0000',
                                                                            '20210228:024602.089207:+0000',
                                                                            '20210228:024602.089228:+0000',
                                                                            '20210228:024602.089247:+0000',
                                                                            '20210228:024602.089267:+0000',
                                                                            '20210228:024602.089284:+0000',
                                                                            '20210228:024602.089303:+0000',
                                                                            '20210228:024602.089322:+0000',
                                                                            '20210228:024602.089341:+0000',
                                                                            '20210228:024602.089359:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǲʖљǡńίԚ\x96ɖơϗ£ƋƋǀϊūѦ¿ЗеȡȁɋŰϚЗϛƯ˺',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ñ.ĖЌȗЁɒ_ЋДѶðłķѿúӞƄҔƝôҚӣʖżаɛƅúȺ',
                                                                            'œ7Ѫϗϻ\u0383ϽВǁϩɺѷѐξӯΎʓɃԦҮҘЦ\x88ҭɯŚǬҲʻ\x9e',
                                                                            'ɸοһʀӒǛŚϋѧɻÅЍӞǖĝʨĜɽѲ§ʍΒɑʒĥϗȎơԛƒ',
                                                                            'Ǉʉʭų«һȹÌӒ˼D˺×ŗʫɟѫɘ©ѓıӓȢԊɲȣЖːөs',
                                                                            'ʱ\x86ǀΩӷ§Ôʶ҉ӏƄДΒ\x99Ϫ_gǞҵSԕǱˣφ=ϖҬǕӜщ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '«ŞНːХǝ)ǏϘ¤\x93ɛ˱\x90ӲȻÈ˂с˓ŜÏIϺŒʖvĿŰȓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƠǚƮ˙ϊǥήȤԡϥɝӄĀôЗÖwTÑҭ˦͵ЊȞƹėҾҮȑ±',
                                                    },
                                    },
                            {
                                        'name': 'ёЊԁ˴ѣ˲Ӧ¤Ѩ҂²ФϠˍӺȱȚƔȊ¥҅ȍƆ˪˂ѣЌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6480024318925573213,
                                                                            1604033992302755961,
                                                                            -5230617810305830849,
                                                                            5541075754788731322,
                                                                            8181371749094677371,
                                                                            6127791087723509454,
                                                                            5914747402856593696,
                                                                            5985238330000244022,
                                                                            -5095513810714969198,
                                                                            4565740215678733046,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҺѪԌϫΩ\x9dŸ²-оĻɌûƬǵηŲĳ\u038dӄυЦΎΨ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            68734.05653496069,
                                                                            627960.9841624454,
                                                                            558068.0506694277,
                                                                            574840.0025125408,
                                                                            536995.4395425366,
                                                                            775793.882675269,
                                                                            -10665.16738853202,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '×äӍ\u03815şҰƈθʂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǊИŏyΊǾǪƃʺ˫čǓĺ(ҚQΘˎζɁà\x81?ϛő@ͽƐһ˪',
                                                                            'эlȻ?JƀȦŘУюˮƍėģЂE|ǖśbɯф´њУü\u0380ū\x93ä',
                                                                            '\x82Ӄ΅ŤӗV\x97Я-϶ΐÌĖȩUàǈɶчáʥOΫϢƛӷɆʬÑΥ',
                                                                            'źͷĴɪűīžŇxˢǜ˨ĿĽЮŦċŅήʌԗʂ#ЀĬƒνЈєΊ',
                                                                            'a@άȫ˅ƕǙԏɍԧάˍȗ\x90ɖŲμţęΒɷģ΅ζįQʱҌԉδ',
                                                                            'ԣ3ɱԟƥӣ!ж|ɵҳǦԖӨɈŀϼĲԪΈƂϼǥ5ʁŦѰ\x8eĹǡ',
                                                                            '3ŰɣLɰʐӥΥҹԟ½WȊĪɡψʢҽǖ ЦƘԍŉŹƭŒ҇ńɃ',
                                                                            'ɻԋɏҔʝ˧ĩɤДӆԧǐºͻцЄԉԭ4ć|ů\x84ÍƇҨÈ˞ӷØ',
                                                                            'ůOƇɂ˯цŕ\x98Үļц˖aƟɚж\u038dѐϫԕƠԗǸøųʤԒАӿǹ',
                                                                            'ъɄͱЦģɭ\x80ƿʱĥǴȥƸШ\u0383ԑĖ\x99ȇыɈ҅ˤŒľȩқҙȨҿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'İȝȾ\x86ƐѕϚɝ\x8b\x94ǗTȅѲĘ1\u0383ϯйӷŠʟʵΨàVьϨ{ũ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            268370319038719966,
                                                                            -9079689161655120274,
                                                                            9144731320543871415,
                                                                            2233192913899542892,
                                                                            7750136350865495366,
                                                                            3964102100285713031,
                                                                            6053233124075829616,
                                                                            6978829579524925986,
                                                                            5541447496954516502,
                                                                            7632228012687234160,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǘл˽ϙԑǨÑ͵ǴӒƍ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˒\u0382ϙƂăѴȹӌʹǊ#ɐҙƿíсǼϳ\u03a2ǇӶɂΙѧѮļԍԙçӋ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x85ɾҁ\x8eµôΕΜ\x9cҎŻΩťßţΘɹҡuâˇ¬ƽεϱҲOʈ²Ę',
                    'message': 'ŨϒĭÐ±\x97\u0379n˚eˈʊψԪǢɒǇôuӁǝʡłӎԙЃȾώЧN',
                    'arguments': [
                            {
                                        'name': 'ŵƬЎɸȠƛʱ΄ηҔæѲƌӼӯίʫҠΆԅþӤҧɭƌ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǀ½ůЮƗӾӂǵ<ƟœËzΕѾΔхȊʃŀǔɱҢѭťď˼ɖҳӦ',
                                                    },
                                    },
                            {
                                        'name': 'Ϛɗ\x99ĔΛiY\u0381ӃɢʚÁ»ē¥ĆԘ[чʜӺԈȞÁѪąѽÃǃԛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024602.096111:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԝē£ЦÇƃGќ\x80ŕÝϽǩώź҈˙άȕʏǲŷωЄџˑϡ<)ӆ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԛ&τ\u038bƙԬ1ӃșΊʺúӑʗɁϡщțԨŊāΫ˙ɿĳĕ·ȭ>Ӑ',
                                                                            'ɀӭƆёĺ\u038bԗԁ\x94Ȳȸ+¸ҾϻʾѣĲЯҐΠȼņʥҏĔƺšƧ\x90',
                                                                            'ˡԈ˫ϥҸƹ\x86ͿòŉѣҳҢѳƁǾþÎǌɜУʾmЀɆζϒ˘ѿӃ',
                                                                            'ƞ«ðĚȂƏɚϝɕÜƠӉgǢ¡YӮ˄ξːGʤхîӁϊϠʒӡŲ',
                                                                            'Ġ\x8fϖƽŞϹěˆŰέɏŚǛΕтѢíɾ\x98ʑӧʧўʳџlʋGʮɅ',
                                                                            'ϲĿʜˍѭʹIɐӪBű\x9aɿΞǕ¬ѣ-ԡŔϱ˹αұ,ƬÃĂƛʼ',
                                                                            '«ʁϒэŰǄȲўфÃӢ~ΊƷί\x94Ħӎ®\x85ǢƞL\x9fSɅ1³Ҍǿ',
                                                                            'zѶԢȊ\x9eƎƀѕɢũς6ŬøçˊʦʬʣÙҾǫύϨӜІбLıȎ',
                                                                            'Ҙԙ˂ǊƊəвҏӮΆôϻôѤвӁȓɒȵЅϒĹǨЉŃƬӂŽZƾ',
                                                                            'Ϛȕʎ˝`θѣĞĆϪάȾS¿ϱԈύgȳŤў9ԄЏԨԌПʠƣЫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˧Ͱ\x95ƿ\x8d\x9b҇ͺðŮ¥:Ʉ3\u03a2ǖĶԪȄƁ,',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ѵјoҀƷʧIЩˤʷСnŎѯϳ¦Ѫ#Ԇ·Ĳ\x8aӪѦŕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǰƘɌӲѶҺηş§ĥηɜʂ˸²ŀOƇҝҌüǝƬȝϣ¶ЙɋӖҌ',
                                                                            'ϊƨсҢ¢ƦĶ£ōԄȎǣΥʥНӓΖЉҲϛˎǳɱлǧӫĔĢΘɒ',
                                                                            'ӀǆҝӇŮ˯ԢûΰԞʪАʉцɷ˝ʆɪӎҙЎйˁɼԥŪÖ·ˊҕ',
                                                                            ')\x80ˊϱϋƢĚдɍǮ*fԉ҂ҏĩȚ҅ΌȮųøŁǶ¢˻ԥӲҌТ',
                                                                            'қӽȖϗŔϱΕΓȲя$ЫƖòHŘέºʀѴČ³#ȶ\x94ïʘԖõҪ',
                                                                            'Хϯɉ˲ǘʮvïǹƢѐȒúʁɿȷϞ\x9fǽϝňǂǲʒϩɖŘΓЈ¢',
                                                                            'ĢБ@φ©ȲňЯӄԃȝ\u03a2łĦ>ǚ˭ʲӈʽˇċјgԠŃԮ\u0382˓҂',
                                                                            'ˠƂFŎЅƞČѕŀǩӡŤ%Чϒˌ×ƹϚЩȚŇǚǶŕɬԣПɮѐ',
                                                                            'ÚѹłͺÃЂ\x84ȂĦΡ,Ӑ<ɏϴÄȚƣœӷħʽƽѼӷȞŀЏ˥ц',
                                                                            '˶ɰĩʀѶĶưϥʬγǰͳĵ#Ƚҭ\xa0ŀГɇЧUʶɡĂϗƔΈӿʕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǨԘηǵκ҆ɘˍӡɓĚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            660615.0342944202,
                                                                            669745.6504729782,
                                                                            382056.9194093108,
                                                                            722099.9780524977,
                                                                            219331.87643111573,
                                                                            254363.57804778352,
                                                                            576017.044818359,
                                                                            50573.854171164974,
                                                                            482035.01356168976,
                                                                            878998.223584675,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϓ\xa0ÎеƢѢI',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 354491.12660886336,
                                                    },
                                    },
                            {
                                        'name': 'Ǘӛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            359232.4298675945,
                                                                            40167.73010382973,
                                                                            59483.83338424712,
                                                                            689666.720398893,
                                                                            995403.8239972026,
                                                                            395078.18187431974,
                                                                            304728.49933845055,
                                                                            148055.4011498266,
                                                                            764046.5292355822,
                                                                            964494.0540140623,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'юϭĹˢǞʵÅҽˏǮƓϳι¹',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                    },
                            {
                                        'name': 'ÅĩԀəʺлϭҋǩѵčȗ˚ӽӛѴτҞԏŭɎЖ!ϿƎтα¬ãɡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024602.099722:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʶpªƅӘϚĉ˲ϚбѥƾUԆҹҦȯˑӢϰǚЅɠХѦ\x8b!҇Ď¥',
                    'message': 'ȼящʤȡԔåǍǡҚӈʍҘ8ѭқŪ*˯ÛɯѶɡŞɦdϑĨϭѦ',
                    'arguments': [
                            {
                                        'name': 'ņӖϐĉӭƖԢɛ˾ȫӞӝ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЩҞɇσԦR',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'Ý',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'úӟҝÝʂ|˗ǐξƺñŚɻȄwãϬȵқǭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -76202.1464732179,
                                                                            633426.125555613,
                                                                            648852.3305763283,
                                                                            656722.5988829057,
                                                                            -84275.56311580594,
                                                                            32343.054646550707,
                                                                            696645.8857634197,
                                                                            -76919.75381692502,
                                                                            -36721.48877474923,
                                                                            837227.9350341982,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӤʯьɽΊ˓ȶΝǸΨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '¹ьƝƛ͵Ĺљә©ȃGͲҜͽӒ˱Ǘƛʾ\x87ʚԏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1937161957269478910,
                                                    },
                                    },
                            {
                                        'name': 'ăÁƅ¤ĩ"xȿ³Ë',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¢ŶÜѓ¥ђҁ˙ȭƽѸԉМРΠƼ}рƾҴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3249418217707747341,
                                                    },
                                    },
                            {
                                        'name': 'ΊмƸèģԟҐ҇\x97ϥǠӄȇε˵ƁҗϵҹϳʡԐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӅƥĈ·1ɬüҏɸӕÔřđȁƷϭѶмƣǿzɇȔ˲ϧϧÑѳɹV',
                                                    },
                                    },
                            {
                                        'name': 'ƖрŭΈ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024602.102116:+0000',
                                                                            '20210228:024602.102134:+0000',
                                                                            '20210228:024602.102142:+0000',
                                                                            '20210228:024602.102148:+0000',
                                                                            '20210228:024602.102154:+0000',
                                                                            '20210228:024602.102160:+0000',
                                                                            '20210228:024602.102167:+0000',
                                                                            '20210228:024602.102172:+0000',
                                                                            '20210228:024602.102179:+0000',
                                                                            '20210228:024602.102185:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԌǻȠ˄ԎĸȞΓϼȾƝɉΏ',
                    'message': 'țĉѲʓǈɮͳ|ЗδǝʢɎƠ5ΰɥɍɫŃƺӨʻȲūԦϸţΠȁ',
                    'arguments': [
                            {
                                        'name': 'хĀāʗҥ9˘Ȍ"Şұͼ@ưԛƗʷŃа^˱ҐЫТɪΆҭ\\ʰˑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѷϠϖƂĩɏǢɊ˓ƘӰ˅ԅъƷǍƥ\x8fɍĔɫčÌʽPȡɀƀӊɧ',
                                                                            'ѺuƳˡӝ+ϭψĜ@ˬɲȇͶȥƭƈʮ\x84OʺϸтŁēΣ+ʼўʔ',
                                                                            'ƢđɠѦƵυԕԥǑ˯ԅǣ\x7f΅ȲȿɛϒĘ\x84ʀџ(ĿīƝъ{ŨɌ',
                                                                            '΄ǒВƶ˗ҘˌĦбʢѠʍ\u0382ȥуӺØκdjǂèɣƨԝƠԘ҉ʹ\u0378',
                                                                            'ķăʹԨMÊѶʿʴψȐӈЦԃҩϕ§ζѥЃɦҦζɃʃËȺɐ]ʮ',
                                                                            'ɿьwğӅЪȗÜAƖӱѝѕ¾ΟNИҏȚ˽ˢѷϽʽǲȠʪϮtʵ',
                                                                            'ѶϓČõȕΒәѡΓ\x9cґ1ǛɉÁuĞȯĦѴkǅƿǻԀıҪԉ˫Ȯ',
                                                                            'ƣъ˽КϠlЭ2˂ΒΨˌ\u0381КйГҞ˔ӒԃĄșʡ\xadǒŀӄөͰп',
                                                                            '/іðǔĥъӅCǈʫƺRögΛԘ´Ҵ¶˔Ξȏɀƫǜӕ&tąƳ',
                                                                            'ѕĊɶ΄ȥk\x95ɫҭЯSˤшȫĺҊө˯śůÈ©ӼǴҷǧǝǲӵК',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˝ӓԍΪι¿',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ŉ˰ӵљʛɄŏǞ0ӁĜѺ?ÄȤŊˋÈīǾνǖ\x80\u038bî-ŭ˗ź\x87',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'х¶ͿBŨҴɡȗńӖњjƄʇΖͿӑԟ\x93ʞΨɢ\x9ašń4Ż¨Εě',
                                                    },
                                    },
                            {
                                        'name': 'ѮöӕũŌǅ`´ɻˈґ6ѐғ¬ɠ÷дˏӸѫŻϟŀÊ˧\x84Ɨ҅°',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            828308.2484667533,
                                                                            579943.907570006,
                                                                            426414.3532441171,
                                                                            584819.8608596593,
                                                                            403200.6825237835,
                                                                            409502.3310353435,
                                                                            48263.4745476426,
                                                                            179818.12432684097,
                                                                            980641.3161285743,
                                                                            137971.32355837067,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѣŧǥʎһςQűѡÜϣρǴʴýȿŽџġƛтӼsġΈʮҁŗԬǵ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            165121.08674317255,
                                                                            -19382.16632368781,
                                                                            18381.28158247465,
                                                                            938914.8665265582,
                                                                            724302.674942943,
                                                                            903853.1162755513,
                                                                            786955.864697339,
                                                                            920436.0446810779,
                                                                            471548.02523874806,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '§ȊϠgĘԘ˦рϸφĆǄ@юŒЎϏјä',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "\x88϶'¸М§ǠēѻӦǾ¯ЀќÎΤ°ŽʤˌɅ9ɸԗтѮǕαʥħ",
                                                    },
                                    },
                            {
                                        'name': 'ҧͻѯХ˰ԔӅМĳӉԬҰĚϙ˂ɰÑƇ҂\x7fɩǌδ8"Ȁ&ԐϦԥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʷιåƺɱϷπˍҨΰЊ\x9cΛ%ȡǪüɮΔϨЭҺАͶ˨ʥ£¡Ēá',
                                                    },
                                    },
                            {
                                        'name': 'LîʍǆȶΌȋĎ˒ϿĩŪҽӞɠţ΄ҊʋЊ\u038d˹ŭҩ-ҷƣϸĤ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8826350882605430570,
                                                    },
                                    },
                            {
                                        'name': 'Ȭ҄ӡʘıӚȘÚѿЩFёˉѰі',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -81780.11156197457,
                                                                            153381.3074176728,
                                                                            14521.120584315722,
                                                                            867762.0581585645,
                                                                            690452.7301482288,
                                                                            284769.0861861296,
                                                                            447238.90508803714,
                                                                            611942.8286668762,
                                                                            643832.0025386562,
                                                                            915916.0100921007,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЂМņόŔΰŉʹơιϘȯÜɦ=БÿʧΪүɲтҟѪǩʞʃ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ĳï$ŭȟÆȪġŘҕNʰ:ˎΡԂɈeˍƯ_9ʓӽʚKɘʙ5ѱ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'äӀǤđӱĚӤˣʵ£ƠɅȊЅơɭ;ɟļғɿŹæҗȮΡϢ¦Úř',
                    'message': 'ǐȲΣˢгү=ʊǮӟǔҜӗʳƝg˪ˁcҼɫΗεǽʢƟƾÆɥЦ',
                    'arguments': [
                            {
                                        'name': 'Ͳ\u0378ȯӄńφr3ģ\x9d',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȣ\x9fʽ\x92њ\x8eҜÍ˞ϔÁȮφԬCʨƶβ?ɚŸʽøɄ&қɒʑcҹ',
                                                    },
                                    },
                            {
                                        'name': '~͵ЖčӯѶǓĤʳ~ЃфΝ\u0381ƕϦϨϔɜȋĭʆřОšȮȍ\x90Ӵp',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '>\u0379ŧПҵͼΑαǀ˽\x94ωӼ\u0383ʎѺȔҋǨаäΛɯҞ]ͷӏŕЛѢ',
                                                    },
                                    },
                            {
                                        'name': 'ɧʝí',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˍ҄Δ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƟҗӎѤˏ\x8a3ϥҁʟʽr\xad«ʣϪЍCҹѕ-ȜÀ˅ԝҶ\x94\x9dԠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƓϜАʏ˧\x92ű\x9dуȶиɃϯӔҫϑPЀɨ:ȴ×ÙΈ˰à\x80Йӈ˅',
                                                                            'ΫЄÚįӣƾѽ.ƞƀţśӎrą5$÷Ԯ¢ӤɐʤЙcОǳͰˎч',
                                                                            '|\xadƠśϾΧϝ\x93ԘǕԤ\x89ɰ(ԀʵXԅξıZӖ˨ǻǀĖàˤƈӤ',
                                                                            'ӔӂϦЩŚҲҵΓʽӡ\u0383ѻˉзĨұԦʵԏԬěʵtїΙϮҝ,ҿ}',
                                                                            'ˑí˺Ɂņ*ÞôԗĢ\x9fҩĚ\x8aΪԁ\x95ΕҐȰɎΖфέǹӠΣϷԭˍ',
                                                                            'ɥQӧҟϚɁϲɧ˷BɒҳВš˷еÇȫŅѣЗáƬƑZӤτģNɅ',
                                                                            'өΥfǻpđԅч°\x85ʎÖǠˈʂЩ_ŭʬ¨϶ŵ-ʙ ʧɚȡϫh',
                                                                            'ǛëǍͼВĻǈԆďɼȼöȀƊʕĩʺ˟ʣÂαèž\x8c¢°ǵĀ\u03a2ɰ',
                                                                            'ѠȶżAĥ©ӕ˓åįԒSõˬCƶǟȨόəα˩ԝʜ;Ԯ\x9bȑǸҬ',
                                                                            'ˬŊǠќǷƖŘЍιЬƙʱʁмѨ҄â˭M҅\x90\x95ȡ[ӱƂϷѵιĶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΣĶѥŗōçɮҎӅʜFÂˣˋƶ˷ӴΝѹԝ\x91ǿɖϋzдуǡġХ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6985860649066383139,
                                                                            8519557134204421957,
                                                                            -1713473293411324689,
                                                                            -810146042577106685,
                                                                            -8681392226062125233,
                                                                            5684185580066542263,
                                                                            -6891990075905921810,
                                                                            2490182563354517184,
                                                                            1957320304035034811,
                                                                            8588169802701927356,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʥƋƦӴ˙\x8a9ӓįÍʪԧͶ\u0381ɻǻ~Ф˲ɁͺšƀʐƢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ύ˴Ϭǳ\x8aˀΞûˬЭĦӷŋ҂ЃǐРϭġѱыΡϣυԚÆȫлÊύ',
                                                    },
                                    },
                            {
                                        'name': '\x9cϠŲɂŵíɯʳʿľϷғő!ƥѨҞт*КцņÇǪƫŦè;҂χ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            471836.00608087983,
                                                                            818231.7175333408,
                                                                            523280.06892656593,
                                                                            922222.8217348015,
                                                                            801876.8932400086,
                                                                            958926.7799635874,
                                                                            101464.44933776784,
                                                                            18040.638529158547,
                                                                            670579.047300225,
                                                                            153649.22855658672,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӷîԀJӐң˻ŭøù',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -59952.14065368826,
                                                    },
                                    },
                            {
                                        'name': 'ϵċӼ\x8eȷˌԙñЖǄԝŮäăӖ0Ȝ)ӺƩqIɜɒ:ƧϖśԭҾ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -32496.981684303013,
                                                                            135143.72890353928,
                                                                            732867.4761854075,
                                                                            454747.8617418448,
                                                                            -81774.87465211305,
                                                                            -44192.812805515,
                                                                            697907.9791391897,
                                                                            627215.3481570295,
                                                                            212105.91247182642,
                                                                            122117.98458396437,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ξт¤ȳȓЅĶ\x82Я˱ͰєŅĮʲÉԖǩӑϑ˯ƚι,ΛĖſˍşӌ',
                    'message': '\x98əãĀӜƟгľϚʢȒџTȲɕЫşȄȔΨǥ|]ΑǥΥğϐĔȚ',
                    'arguments': [
                            {
                                        'name': 'ңФ˙ȆŦϠϞȪνļ`ʙʓĒŐ\x98}Ԉ˹Ýǃ˪ȐԝzD˪σť§',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĥƄǶʐʽɉχĞԊɮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'Ѝʑ\u038bѪєςϧΞăŤԃ\x90·ʦҌƷsWě˥ӉĤдӅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ԫ;Mɗˡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7262734786025665192,
                                                                            -6917928975085847830,
                                                                            -1275827263593662655,
                                                                            7538613161694222029,
                                                                            829504508848655893,
                                                                            4900138167870762563,
                                                                            4317142282777669365,
                                                                            -4538983862842896291,
                                                                            -1900194193256593775,
                                                                            -1756146341022824526,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ōͼө#-ԍɮpϽJ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ıХЩɆª\x9dǥɕϿã˯xҨ\u0379eӉ.ЯɵɏόȒƂȔȚìόǊηĊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ϛ¡ŧʣ˾ʹɡӓаǝƵυǧ\u038b<',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3286193626257582815,
                                                                            -1684016792541825151,
                                                                            5367106069898313988,
                                                                            2452180475325682321,
                                                                            -5514598803061149996,
                                                                            1581379011025598741,
                                                                            2696834159307647106,
                                                                            7712153558471966592,
                                                                            759033988535461009,
                                                                            1445111743204747190,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'țȅȟʺѬˍƲIĮӸ1ÕӐȡӀ\x89ÌɨѨӥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            145575.56152590775,
                                                                            23705.086665394105,
                                                                            929517.1783083562,
                                                                            850814.2266158941,
                                                                            833916.9048399973,
                                                                            418216.66431085026,
                                                                            452793.3567507828,
                                                                            -50155.07064927931,
                                                                            -40234.728835060276,
                                                                            517191.72142022743,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӣÀŋ÷ʚΕʆԞǉѸφǧқǊ˺´ҌƸƩʁɄǙѧËǀѫӖԒȕȒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024602.109323:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Е?ĵ\x84ϒưĴ[ʻʲ&ҙɲҀыµλËŶҸƈȳŏα¯ѭǞùȭć',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024602.109474:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'óϞьҺԩĪXһ˶ϿѢźȱѣБѸćØ/?ĕвďМ·ǋԌФĆѢ',
                    'message': '·ɺµưξϷЗĝ\u0383.ǸƜΣӦÊԌǰЄȹұ¾ǣΐǅн*Ƃɱtϟ',
                    'arguments': [
                            {
                                        'name': 'ϭ·ɄÎJʣΝŶ˄ϦЂüŎʾîNМƮˉѷʖŶЕʳĕĶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ȫɲ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024602.110026:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɚɑ7\xad˃ʒĵ˶ӣɴѤƹMϕΡǟιԟCәт',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8536691883908700657,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЫγÄ£\x9aϪǦЈʓԪƏŚԃРϧҍʂӒǒƕ˸ʦ҆ƟĝеʦγŉĞ',
                    'message': 'ƨĹъјáΈМΰϘÏȥĥԗњ"ʡșљɉŰҏηȲ#ϊДºňÕŇ',
                    'arguments': [
                            {
                                        'name': '˗ӅȸԋÛϯƘƵԧźϑ\x92Qɶ\u0382ƴɿ²ϋԠüшʱżˬЪƳϰɬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ɖľ˄ʩĶʒÖƺдɗ˪ԞšԄнȃĽÊРĢƞΥĳ\x8fΉԉҲʒʜ˒',
                                                    },
                                    },
                            {
                                        'name': 'ɱƯ\x9fˈзnЂ\u0379ѣϒŤǖ]ӨΟŤ8\x90mÒɹΰŭӤг\x94ßϲŬƞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2033510140884308824,
                                                    },
                                    },
                            {
                                        'name': 'ˊƫҽʇLįѫҸȫŝưȺԀГҼԒѭЌϾѵƑ5ƿȤǵ¨+',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'ѽÁΓʞǑóЫςΐ΄ĢƗ¢ƹʞαș.˴ҫҖƼ˝ōѺňϻəȀҾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024602.111019:+0000',
                                                                            '20210228:024602.111032:+0000',
                                                                            '20210228:024602.111040:+0000',
                                                                            '20210228:024602.111047:+0000',
                                                                            '20210228:024602.111053:+0000',
                                                                            '20210228:024602.111059:+0000',
                                                                            '20210228:024602.111066:+0000',
                                                                            '20210228:024602.111072:+0000',
                                                                            '20210228:024602.111078:+0000',
                                                                            '20210228:024602.111084:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'θųÖ+÷ӭǠʮΨɭx',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ϭ6πɏɜϭѾ6_\xa0YŸØїÇǖҦĖ¥ˏѷďsˋºбȰӴB×',
                                                    },
                                    },
                            {
                                        'name': '>ѡˇӤӮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˱΄ѻȜ\u03a2\x81ɲƅҡХɿϴҋӣaЁп˽˕ѭȏʿȋƫƨΤΰǲǎ\x8e',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024602.111583:+0000',
                                                                            '20210228:024602.111596:+0000',
                                                                            '20210228:024602.111604:+0000',
                                                                            '20210228:024602.111610:+0000',
                                                                            '20210228:024602.111617:+0000',
                                                                            '20210228:024602.111623:+0000',
                                                                            '20210228:024602.111629:+0000',
                                                                            '20210228:024602.111635:+0000',
                                                                            '20210228:024602.111641:+0000',
                                                                            '20210228:024602.111647:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˆЍǗӨĚ˨ΕӘǊКϊ˖ÿɒϬγF˩Ǯ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024602.111877:+0000',
                                                                            '20210228:024602.111889:+0000',
                                                                            '20210228:024602.111897:+0000',
                                                                            '20210228:024602.111903:+0000',
                                                                            '20210228:024602.111909:+0000',
                                                                            '20210228:024602.111916:+0000',
                                                                            '20210228:024602.111922:+0000',
                                                                            '20210228:024602.111928:+0000',
                                                                            '20210228:024602.111934:+0000',
                                                                            '20210228:024602.111940:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΊʇkñƛϺŗҸϳϜÃҡтгȪCӶȫ҂ńŀԥĸιѶˀŌΫэО',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4916133184971629018,
                                                    },
                                    },
                            {
                                        'name': "Ӷł*ŹŴЧÇƈ\u0378˫ʫâʸǻМ'ȵүљɿԗҔʤɨƅÍƶǔЄǥ",
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
                        ],
                },
                {
                    'catalog': 'ƏϜɑФǁΆͶԆÃӜǭǫ;җęúѾ˺hĔӾԫȉńdĴoҩǊǒ',
                    'message': 'ŖԫXԬ˞ԖȚʏĥқǏɼŔȉΓĩҩǄҹȗ3ϢӋ\x9bφѕг~ǭʹ',
                    'arguments': [
                            {
                                        'name': 'ю',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            508338.702197941,
                                                                            451720.64181484224,
                                                                            549773.2380841081,
                                                                            673866.781240333,
                                                                            517403.3687765215,
                                                                            31158.95367953027,
                                                                            975786.9387581523,
                                                                            153789.5992761472,
                                                                            305328.17048810405,
                                                                            508827.94011155935,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÈıŭέɋɺĽΪАɏˮЫӆʓ\x81ѹ|űГƊȊʹœμȵƭ¸ǁŹŞ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024602.113102:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЗěŬÏʦҳȔʒҁΕË»ŴǦԭεҏíϜӇπØŃ\x86ԕҮΪÐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1208276974504822976,
                                                    },
                                    },
                            {
                                        'name': 'Ҕ+\x86CȱɔˣŌ˨ˀԙÎρҖÈƗԌϾ\x9eɚȱþ\x8cԚɥŚ҂dĈŲ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'Ŗ˪ǱǡȐ>ŠǳǕЬȱɿўц',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            895624.9656118022,
                                                                            857867.1498112087,
                                                                            693679.9488145496,
                                                                            671629.2454191332,
                                                                            214254.29029232403,
                                                                            599727.3128665324,
                                                                            61126.80078678389,
                                                                            350960.79573133413,
                                                                            840858.2881785912,
                                                                            283827.19836458267,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǻӫ$Лɨϕ˪Ԕ˽ŻΏԗEРљ˶ƽĩŋƈȌZϋСҸӔҰ<Ȉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            684209.0203355565,
                                                                            429364.7321955189,
                                                                            113776.72702208045,
                                                                            630643.0059531081,
                                                                            996459.0825624419,
                                                                            343307.4045416599,
                                                                            196598.67961717123,
                                                                            161695.85235810306,
                                                                            269315.93745395204,
                                                                            423487.68226071313,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x95҃ңΧȰģċŊóгK»˥ˮ˸ʔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024602.115898:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӥϋͿˆԋ¯ʽɆNѯϏƩĸ³Ԁŀãԉ·ҀаÀȃΖƹæӑμЌҗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ăʕԍԤ˭ϦƳ˫Ȯ6ĘʘÞҡвҸˍȤǑʴʓĸ\x7fũξɼ.ĿˆϷ',
                                                                            'zƮȣʦɤӪʝŌ\x95ƀ9ϏҦŤөʩԢËЊƻhѦ\u0383Ļ˹ӚѳŌԌΈ',
                                                                            'OĖөǇǅɠӅ6Λє˺Ȭ\x9cːTɿǹҗŽĎ¨Åû;ȬӒѿѭÐφ',
                                                                            '\x9dƞɧ2ЉӵȄϧʷ}ΑɓѤѨнɽϖŖǞĻòЖ\\\x9dϟǕѧѝӌ\x9e',
                                                                            'Ԛ?!ʩИ"ΧɾËțɦЕĒˈҨu˗ΟʕΊ\x96ϭOҚĭƧeЉ˗Ę',
                                                                            'PcʞҝűӏӘīǹ×ςӅyϺҿңғǑČГԂԏʉЛɖǌћǼΞЬ',
                                                                            'ЀƤŠÜЗħџƩνM͵ȩ˕ƾ<ɣҏɢϔϖӠϋƏɺĖҢʲǎӦʡ',
                                                                            'ԛ\x7fЀґÀʵҫхԟΜåԗȊ«\x81çʹɴȢZȣ˚ϳԢϫŤΞũǢď',
                                                                            '\x9dϻќƙʶ¯АÁȨƀȺԤεҺŏϗȦɉҵǑҽϞӕȸǢϏҏΜ·9',
                                                                            'ΊżʝXΑšǕϰǺǳ˂ŨJ\x8dȜНôϪӎТßʃԬРĂǛĿγʔþ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˄ŸҹʂʤԀԔȏǯǕŦӥˬŪЃĔǁʡ@ńΧѓӏӎˈˀȇήɩ\x89',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1017396296415709360,
                                                    },
                                    },
                            {
                                        'name': '8ђ"ʖʅǇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            603501.2923932262,
                                                                            -17156.22053365242,
                                                                            409369.9788245703,
                                                                            37394.22180720113,
                                                                            825745.4620392564,
                                                                            237762.85709200014,
                                                                            886561.5767487966,
                                                                            -87653.29082062925,
                                                                            927997.2060067968,
                                                                            65621.48063721549,
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

            'identifier': '\u0383ҡɚǨ˸',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'źϲ',
                    'message': 'ŭ',
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
            'name': 'Ⱦˠ¥ʑĩȟɽ¯ЏѨ\x91ƽͽɁѳŨ\x9cĊɠǩұӭǝ˺ϭá;ȵ˙Μ',
            'error': {
                'identifier': 'YԟǶƳˋøńȁ_óŬŜΔ',
                'categories': [
                    'invalid-user-action',
                    'network',
                    'access-restriction',
                    'configuration',
                    'access-restriction',
                    'configuration',
                    'file',
                    'invalid-user-action',
                    'os',
                    'invalid-user-action',
                ],
                'source': 'ɳУÄЉьҵʅЋʙŇҷͻͲΰϵɕÅȬȞζҪo\x81XƠМ\x83ҭǝɄ',
                'messages': [
                    {
                            'catalog': 'ҤҺʃϾɃΩћRϊΞ\x97лэDǺhΰɜҟ˹ʭҝНУёӢѾѨëӉ',
                            'message': '˝ʲȇǥŰČԩ?ѳɸɏ@įãΐԁ\u0378òǹƔϥěПЏԭӷ˶ɾђ¾',
                            'arguments': [
                                        {
                                                        'name': '9ξѿϊɇ¹ъϵøҳ˯N$ϸƏЧŮǚΖɳǂȄфɇƓз˥Ď÷½',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'κɊѭ±ѸĜРǾΣș¾ƶµʥ¦Ȗ\u0382ϭǧӫʣȆωϸAųɛ\x99ҌӨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6655988096134207945,
                                                                        },
                                                    },
                                        {
                                                        'name': ']҃ϓ_ʴѧƂʕʐͱӾ\u0379\x98Ư\u0381ϓϤÀɐ\x9aĖНÂȍΚѝȔӢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѝʉӣņǽҧ\xa0ƬƒΪƾӷоЕ\x8aʙύζԐ˱ʑҨÍӪȐ϶Ɉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ͽӟäЖԀƢğƸȮÿöɎɟȄtʤҾ˄çļШú»чͰƒŢɎÅǹ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƏɲʪӻɹҮɟїу˙0ӛʞȨɚìŶȪūδǀԜzơΤИȜ,ȟΔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˪ΏѝƘрǂþȾ¡ļ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѲԑӽӪˊƱ҅ƶ£Ʌԝȭ}Ӟ]ǗѴŀűŁȉгĦӯìРЮ˨VĔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝǠƅǱԦѠȗˢǣǍǳ\x91ȁԫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024602.065654:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'øʜGœÓԡҾƠɳҶCƁӰϳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ē љǫſŮǌ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӽǉ<ʘȉ˟ωͼ\u038bԠńȅ·ϪÓǳǓԚ҄ĐƆȨƑʍϢȣ\x93иȇԭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ȱ/ª.ȟǠɴǴфӺԗѯұҴȰˇƜĵȤќœ˦ЂΛéȢ҄Ͼԍʙ',
                            'message': 'ʂǫĥƘǿʟŤŚƉÁȭƄэʀĿƏȉ\x86пςɆεȹɎå>јɀίȅ',
                            'arguments': [
                                        {
                                                        'name': '\x7fwŐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'пӳ²ġԭяȎʲӵϧΪΧҍӰʃǱǵņʛƌǣʑƯҁ¶4˶ϤƉЁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'oϸȽ=ϺKͰӎѲʶʺzŗĒɾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'x',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1749371718339954723,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʳȯ˃ºе˖ǽʧϴ˩шΝÛ:áψȸƂщċÖԗϼ\x86ÒǋǶŢƝɇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԞѬϜȴҰԃ\x9c҇ƗYўLήŜŶѽәϰǤίǽϮθӅКÝęѿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'äƻӆĳÆŢʵF',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ó\x8eԕÈ'0ƓԠИϼǷƻÜʚͶvѢϴӇиѢ!ӑԚ¶)2ĳďϳ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫAӌϔӬͲɀԎόθ˨҅ıïԏ(ţӃλĎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʅœ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŸкҳǫЉӵjǅͳǬ^ђчʾǽÙɠӒǟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024602.069163:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ԣ҇ӿϥȔĚԂʚȉ;\x94ǒ˴ҒЋøɬϰŌƤɜʇ¢Ԃ˓ԓ¨ƒΫӖ',
                            'message': 'Ӱηǘѝɇǭɼƿ\x89˜Gϴɫſ¥ȿеņȻ}ČӺǤƬżωʛ¥ŀȍ',
                            'arguments': [
                                        {
                                                        'name': 'ÓҐϢƻìŠӌ\u0383txίʐҸГЙòņ;ˎD˅ǡΐͿǖІ(ĭ;\u038b',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɸjѶȸ¡лʦʳҒ˭ϔϦ¼Ӹɀ#ȋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -37602.494456954286,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĕÑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 362198.39746702794,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ċ+ʂѠӽˢdΤЈϴ\u03a2ȍȔΗԃҨѱԂˑβӓъПǼҐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɸƲѶʝυԏНţӺʶƑǠΪѺđθǢӚϹƥ¥6҈ɯØʡВ÷Ⱥь',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɷɆȏҰÇȠɭ\x9bҨÿҸϒЂaӁϾĜÎĺ\u03a2Ä%Ǌӥɧλ˯ĸѮD',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉŻƓԞƙƩƤɛӍͿõŬԏŪȎƩϟЋТʣƋĘйӧĸŹԪĉWѽ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¿ǶНɒԑҚ˞ӯԝҙȿԋÁѠƨʞ3ρȻˣƉºҠʾ®Ϻԗэ˄ġ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˸ӟ˱Ñ\x96υӈÊӁmȮΆaʢɔЌҔądԎρѲĦØÔӖлʻǭƱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϮяS\\ѨƬʈŔҞϭϽӈɄюǩŝҨ˝Ѭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024602.070951:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĳʊ´əг±фȧӰ҃ΖÂɋ΄ǁӜϗӯҨ\u0382ɓɬӻРȗċӡ\x83N*',
                            'message': 'ɈʯÈČ˺Ĉ«öӛrƚŨÍѼЁΥДʤЬҹȑŜ˜ɱøōǉFʯг',
                            'arguments': [
                                        {
                                                        'name': 'ĬӚƠĘΓЫҐ¸ξҊҸʽϑʉɳѸĶʌѩŜȟˈв˓Ϊ\x9cԩƊǧΘ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'φŸ\u038d\x93Ϸбÿ¤ƸDčΗŽȻˡӹҘfʚǞδtϟ¹ǯҠŮҭѦǉ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 925472.6095671953,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԜΤϳBţ\x96ѪΓâǹԘҮ[ǠƿϬɀӦӼÓЛΑ҉nžº˸ÛŅδ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024602.071676:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '"\x8aɯѶӚѭɢ΅ЂˁӬȲԩ\x8a\x7fŵˉҿϐˎmb@0ǰϬ¶·Śӎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5029785113942985157,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'їϵƏϒƹΜήԬϖȹŶκMԉҲҌΩћ¾ҳǦ˔ŃѩnԔţνңε',
                            'message': 'ȗрϦĢұȮ¥ԭЏʇĤOĬӸʝһѶƻ˷\u03a2ǿΑŀҧŬȍȫЍɔô',
                            'arguments': [
                                        {
                                                        'name': 'Ǭ¬1N҂ɸҶbÇƕĆԉҴѮѲƾ^7ԢӪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĵýǣӓʁȴϲ\x93ȉɬĩƛçш\xa0ξȼ«Мɧшɤʳ˥ԎЫԔ\x8dʥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Җ˃űȧ˴ʍ©ҘЕɷƥ·ǄÕ҉ԉɹИʨƟҸϬЕРʣȻȭѴԇˤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҃ǵόѫӨ\x97\x9cӂȘӬӡďšǻΥ҄ƑȶԆʪrΠѢQűƢԛѢѪ\x93',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ҧ}ƅ«WФѐĠϗ\xa0ĥϞƻƜмԅ\x96ȅqķ§ЍάɇНшȖʀΖɯ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϻŀÇˈϳʩĽЁԃ-ƍŋӿ˨˩ŮȃĹ҇ԛӭŊIȯ¦ҊʄɄƽӷ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024602.072961:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƵʦµʼȸѬ)ӡŋΊŠǐ?ҵˡʭʻvʳέҶҤ·˾G',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024602.073128:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'θ҂ξϛӣͳˋІɹǒоʣƭʭу˾ģćă',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƖBϴӃϛÞ½˒υӿ\u038dԕҞтðFЃxԤͳEҪˋǎԣѹϢɡӯΓ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫɤЇǤιȀƦԘҫRƃиçT0ʹFҺǈҖʹ=ȑ˞ʦϿѣҩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĥ˼÷бī',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҅ЃӸ҇ЁӛԀƱͲͱϚƿΓÊƎӼЫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȁâϵǪ\u0378ɋĮԇѢĳEóєϺuƵƲƷɣ|ĩʱ˲sԛº\x9dуԈΏ',
                            'message': 'Ӿ\x95Ѕûȅ҈<ʊтѭӆȹͻĥƷ¸ǲ϶\x81ӓǐΡˤԇɡΩƘӇT˲',
                            'arguments': [
                                        {
                                                        'name': '?ƲҹʃȆҭ=ϋӅєӅŷŏȬ҅˚ȺЮɎΊ7îνʒƻбƻ\u0378Í',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 588472886524718473,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȍɖ\x86ƶ\x9cʁїɢӲ«/зԒԁʪ"˚ӺԄʉų[ʰУˈӎΩΨȔө',
                            'message': 'ϓЙȘұϳѝЌҥ˒ĨÇʓϞЇӨ`ȉǥɟϐ\u0383ѯϽ˳ƳϴГǶҁ8',
                            'arguments': [
                                        {
                                                        'name': 'ѣԄƚ҃ąЀȬͿ¾ԏǯtό¢Ȍābӱʬí\x8c',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҠǊɃ˔ϻǥЦС˯їǦǌɰżĸˊ\x8bӗźҠŚүλҚЍ¢ҁĉñȨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ғѬȑԫӗʰӖƮԄ˩ҥ\x9dźϭ,Ф@ÿøĮʋöƊɍȝҚϥǎSɱ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024602.074944:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '{ǉҒğľЉȄ¤ПӂФTȐÒϘѫëŵ\u0383ŀЮȤͼҸ˚ΟҞǪʬš',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Дƻ\xadSΐԁ¢Cʏζ°ʵoǏқ\x86ӇȽĭƧƹӬƭOϝ˫ԭͱ3\x9c',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'νѺøϖŢʙ\x90ăϊ\x9cϰʊӃїãԕʊʷōИɉɲУԐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѵʕ\x7fĖ\x97ҴӪʤ\x98ʻҥĖ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'sÖƯϱɛÇ5ɣƅԈϥʉДěőѼϼ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "=ÅçϹӾɭ'ȾӨͽŞ˄ɍŇËθńӐřмʠϏԃġǷ˔ƪzне",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6817100695511096665,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ġ΄ƴэήӺӦȿӤĽȸāūѓ4ǭΓʌľÅƋǋШŚԁj˶ʆTє',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¤ȦİίΚмØŉüùˍƴӉͺɯªǯĵúƥѱ˾ҿîʄӣȔʦšt',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʴЖĘφѩьϥůʬϊɕʺƚɅqŖπԎ½ЎϏҜМаŧʝϒòȹ',
                            'message': 'ơӜΚқѳӑԣŠǐίʋДҗɆөGƓΉӟħ˲Эдңʓûԇɥɔɑ',
                            'arguments': [
                                        {
                                                        'name': 'ѯƙΦùͰƂ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖȘϫŴʝғʷԗͱŵȓиˉŕ^Έԕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹàíШȲ\u0383ЧƉȡԗϰ˨кʶ˕ʚĞōԑć·ӍǺȭα\u0381',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1307472264350763702,
                                                                        },
                                                    },
                                        {
                                                        'name': '(Ę\x94ǆp[CȂ҆ΏϠƝ¡Îʢ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 749777.9151509964,
                                                                        },
                                                    },
                                        {
                                                        'name': '˅КҒ®ĢԐҧǤϧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024602.077002:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "ԃ@˭ɄʨяxӕԊî5½ɨΪůϸȺŻȫǳɰϠ˯ǕтЁŎñá'",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'һ\xa0Љόԍƀ¶3Οϩ[Εǥ¤ѶӛѐÀҐΧ\x9b˖ʋƸΪvƭыҴб',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ııĞěɣʶtǡͻжĿӘǒԄˀӊˈǂ\x8c·ʢĩʜÍуӾŭĸΗŚ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɫдȇŔГǳ"ǤѢƋΖҲĖɭȃÂ\x89ȿ/ƽİ4Ϻ\x9cͱбΌԁњѹ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'әϿѸþђ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÝˡĹԨ\x87\x8bŸƷǋĨȤ{ӨШҊΙéр˶ǐЅ˝ЎȿǉˁЈ\x8dԁӴ',
                            'message': 'ЄϢĥĬčȚʫŊɬϥ҃?ʧÜȮɇυŪˉĈſћ¢ƞ"ʡğOʹЕ',
                            'arguments': [
                                        {
                                                        'name': '˗ͱɤ\x87ёĚuώϿȜČƣɁAèȵȃ#ϓȷƎˍ øǆé˵ͰʬΫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5545031671078409571,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǯԙɺȵɽǎӖӡӊþĸɄDσϯĚÏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6887299396331187411,
                                                                        },
                                                    },
                                        {
                                                        'name': 'öFbʡ\x8aѣȫϮĥ\x99Œô҂\u0378Êјόд°ÞɋӷҴCǩҒӔʘ8,',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ØӗɸƠɸĔɤ?ĉχѵҩ\x82ýɜ˯ō˷оğiͼƠɹ˳ӏɴ»ƍ҉',
                                                                        },
                                                    },
                                        {
                                                        'name': '¹ӫљƢȃӒƏϮ˧ƹӛԧΕďȭҦĜſǦӳƣˌѴώѺ\u0378ɋy\u0383ԑ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': "И˝ҲЌҴаǆϪūŏ'\u0383£öҿǾưШЎŗȧǲĭ¨ԏ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 585862.5403067871,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Q҇VΡĽċŽ#ȣīΎѯͱȫ˱Ȯ¤ћȣƦƸRțͺϪҶÓǪưѷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ќsŰӱ¯˜ͲΧλƏͽɑӆРǸó',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʻѪɔŸτȰǄȶǁàӆˌΣ:ҾɯѱʟɠѰɮÏȪϑҏˮt;Ѵъ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 683985.5742574288,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÇÛîȥƇˊƱԓÃĳcƻ͵\xadĿШȓpȺӹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʳ!7˕ǝʆƏȾʨÎŘx`ǴɋɁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȊϗÌѱ\x89!ԠѤ˕˸ΧÜɡϙʦ˙Ɍςюг5Ĵɂǥ¨Ӂ\xadɳƪŖ',
                            'message': 'ùŮЃҌëʣêŋπɵϊɋҘʌʑɇҷ(ɆW\x9cǌϊвψĴȵǫƜ˦',
                            'arguments': [
                                    ],
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ͻɽώ',

            'error': {
                'identifier': 'UΓÆ¬Ї',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'óą',
                            'message': 'Ϲ',
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
            'event_id': "ѬϼԄϖɳħȿ+љʒĥ'ɒʯmÈҙƮʸȺԦ\x9fƨű\x93Žɠ;ƋJ",
            'target_id': 'з˅ƞÜĵǬƕˠȔԄԮưɂΙγØŽаɖʖғӹԡǧø˚ƬĭΨϭ',
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
                    'event_id': 'ӑүԨȀаϨӖpơҺԧΐѧɚҡΠɄљί8ĭЖҝЛИºîӾƀˠ',
                    'target_id': "¶\x82ԐĚŝɭˏAӜĲɓɔ'\x81ƋǫɃΡнWǜҟΒчˑ»ϱӜɗ˷",
                },
                {
                    'event_id': '\x89ϦμğȡˆҎї.ȴЅԣȭǥ²dӍ\x93¢ĀԋҥƯÑπʕ"˝±Ԥ',
                    'target_id': 'πŔȖЊӕZŘӚәłʑbÑˉёƪя§ҮΠӿų÷»˄ɝǻ\xad;ǒ',
                },
                {
                    'event_id': '<ιĹìɹɵѢϫ.\x95Ӆ˰Ɖ>ѪЖϙƊàи}ɷҩшѨȽcVƣʖ',
                    'target_id': '³θ¸ưĀҤЗӌχкŐĎRëΚӖˎӠʔƇΧԚçǏЗɧąʷŐ×',
                },
                {
                    'event_id': 'ȝԖȳΟǋүːЧȴԆtӰЇʇ\u038dѼğ˱җǻҜĘɉҮĴ7Χӊʘѥ',
                    'target_id': 'ˉЀīǵɉCȼɫþĮпϭбʒĬ-ȢģʌƵӼùƣŰµԛА\x96ԝӁ',
                },
                {
                    'event_id': 'ʵďˌ˕ԦДǗoƋϞǬÊɥӟӪOӅȀÕΙʳǢϥČҗԏȃƏмԘ',
                    'target_id': '\x9cȏЬϽʑƎǏӷ҈Ȓȋ*ϾӹŴƜϳţ\u038bŉŭ\x9aуιѱʢҷ"ΕҰ',
                },
                {
                    'event_id': 'ҺłčӕʕЂϿĹǕǎÝ\x82ϻѩЋȪϰƪΚˍǓͶҵͻЙDЎΚ_Ē',
                    'target_id': 'ϙҧBϼˇ\x8eΔĮώŵŒtĺ]ЈҵyņѽҵͺԂΤԖʴȅˇΛόӑ',
                },
                {
                    'event_id': 'CǨΤʀѓНҴΆɩкÆӈ\x83Óı\x98ÓƏ-EƫΣ¶\x98\x99ýʬĥHʍ',
                    'target_id': 'Ȋ³Ӿ\x96ŊϷð?ƪ\x90эƼϭІũǀѝɳʷǢӒБΗ˨ÇëҸ$Ǝϼ',
                },
                {
                    'event_id': '\u0379ȐĄűҾ¶ƇȆƙҢάˢΐѷ϶ʧӁΠӉȉβ¿ɉË˭ΨѩȷϯŤ',
                    'target_id': '\x9b҅ВÍ:тĢȤǐΈԫ\x89Ŧǣђ9һϩΕѓƳú÷ЭEӄʬƊųS',
                },
                {
                    'event_id': 'өMԐЗʲï>ӊɕѴƼщúƤӹђІȺÁIѯƀϯĿʉωԛɃӃ΅',
                    'target_id': 'ȫĔʁʝқүϧԕŷï)ӝɒҀÞÕƵ0èαάиTϱʕнɳЙ˵Ǵ',
                },
                {
                    'event_id': '\x86¹ƱϔЉɾdŨΒ˔˄OҳJšӷŰˎɖʵʗэˎá˳ϭ¶ę\x9ew',
                    'target_id': '\u038b]ˊɛùңĆ>Ю\x86ӤѺɌΐҭɞϳǿ«ѧɓ°LПʸƮǣ\x89σϦ',
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
                    'event_id': 'ï\u0381ȓΟΞ\x8dҧęB\x8a˶ɖѷϱӧԖóҶϘ҇ϘѭӺэ\u0382ÅǶCҲȗ',
                    'target_id': '\x8cȶ\x9bѢǆҊɋ˳л65˺шǟқhќʀƉњCҸƫєԆɥіȘ\x88Ž',
                },
                {
                    'event_id': 'ųΛčŞ˵ÆрʫΝàν˪ĹњbԝзԭʉӜԈґȞʇѝѽԝ˄ΠƄ',
                    'target_id': 'ˣǨƕӄЫοsϝrϖƭ`ѼԟƘ˕άϗȮѥҕʘͲ',
                },
                {
                    'event_id': 'ˤ´ţ˄ѦƟUƎΥ˃ʭԜÃһȩmØʏ±ϿξԪЌΈДʶ˭Ԟ˸й',
                    'target_id': 'ɌЛįг\x82êɜȨӍʳůϊӬΪгʓʱǶРҳÿ\x87ԮԈǚɹԝʣшʷ',
                },
                {
                    'event_id': '\x8eÂ\x8f£Ӷ³΄ԒʑӰљЭCeǮ\x99ώѡšƕԮƠbˈɑεѶѓˋң',
                    'target_id': 'ӿѣʶőҹľfɰơϬБòʏ?vԠҕϳЌȻҟÐѹƯȳ',
                },
                {
                    'event_id': 'ǞђǢ\x8cĢѼ\xa0ĺѷŢcǈȮ˸ҕɓҰѝԂǌЧг@ҙȮɇ˓>ѣЭ',
                    'target_id': 'ƼŷǢƒ҆´ӖшÖ\x8bÞƹϲԗƕŪõҘӊfńȆŐҊɧҞƸýéĥ',
                },
                {
                    'event_id': 'ӈƑķŌ\x92òȔΚĠ\x91Аǯ%ɆʔђȌŇԏνӫΦύǭϿԅưȤӔb',
                    'target_id': 'ȑԎƱæͼԈ˹ϨөρưȾJуǩîɧúþȽƲϙù˨ɀ¯\x94Ӗȣϕ',
                },
                {
                    'event_id': 'В˯ҁȐȉυîÝȔҐцȒϮѨɘҴż^˵Ȑçԙ\x88ƄƷʼ˨Ǟʾƿ',
                    'target_id': 'ŪĳʋɫʗǶΪԠö˺ƙϧɖˠӛďɏǩǺτɛLΏƨϒκǖҿҎҠ',
                },
                {
                    'event_id': '_$ˆғʂԦķłю\xadʀȩЂзɯүÒɔǄĒĉ0҈Ǉ&ăģýӒɴ',
                    'target_id': '˖ӦЛȮ«ӧȨʤ˒ЭԟЁ˽ÒȔ~ҦԁҢ*ʴЦ2ӺѮ~ӸĩYʃ',
                },
                {
                    'event_id': '\x99˽ōԞӝžǩˊģɅǕoԄsӸъ9slįǰģóӉтƀμӡʭũ',
                    'target_id': '0ҿƘǣǀίӃǰӶȦјҞɄӟˬ҅ůÕˎřϱѻƛ\x9dЄӼƱћҲ\x9a',
                },
                {
                    'event_id': 'ΨÕªôʭƸÆҪ*ŭϖҭľ¡',
                    'target_id': 'ƜАÇўͺӤĢȘaɿԣ#аƉиĠ˧Õu·ƼΨŉЛγћØ7¬ď',
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
