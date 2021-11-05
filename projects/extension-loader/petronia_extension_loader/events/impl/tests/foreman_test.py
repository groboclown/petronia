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
                'ӓηʷЉ¼ȶȧӦXӎԂȨґѭǚΨσČ\x93ƒĝǚģƊҾҫ˘Ͱƿǃ',
                'ӄȾzӐĤуʓ$Ŋϝ˾Qԋԩȝɯʎ˸¨ÿ\x7f÷ӭӉȨԨȯĉȴφ',
                'ǥїӋ0ӟѥЊǓӡȒ\x8bΙªȇǐэȉЌ\x97Ҹˢԍ¤ǈоȲʞĳАç',
                'ÎҀżԅѸЭмʷĆ¤ňɗĳҤ0ġpԒ2ԎϮϝӳӡŻŸӔ5Χϲ',
                'ФԥȷɡпŞѓԔŭƄΈ;ŷȰȭʉςҰơВϷƳόю}üъ:Ѻ˓',
                'ӺΓ§ǞȭµƆΐŹҥŷϠюÖɬbгӶʸЈԌΨ˛˜βÈȃƟĤϔ',
                'љƖĜƛƏϷӮћшuФѸ\x8eǻĕϵɓƲË҈ëȀаʓmʀ«ԗãȵ',
                'ΞʲŬ\xa0ȾˍĿěǃѦʂ\x8fҚƏȓ˵҆ҹ¦ϓΡǦѯʈȇ҆ӍʒЫŶ',
                'ˁʇҾϖјœ\x9aƉ\x9dǅˣ\x86ԀͻɔйˁˌԜӪȏ\x8aʺΩԦъƋԧУƊ',
                'Éɂlәϼ˂ӄπɈ\u0379ÜԊƿԫɗЖưΕȳƏdȋƯԚΤʑŁǐˑî',
            ],
            'source_id_prefixes': [
                'ȝsжɐϧϽȊơ\u0378ɺЪŀ`ъȯӬΚɂxɰʄǻ˞˲Əќ(пѩņ',
                '¶ЋéˋʓҭΌд=ИѸАŸӒҭԓĥОǊ˚ƪɐӒΫȜӛЩ\x87ɞǵ',
                'Ȓӯˍa2\x91ƘǛϦĭӀ˚òȡˡÂīĮƐǭ\xadжǸƈŗӄѬ\u038bķӷ',
                'ŕŗ˓ʘŻϽџBθǬÐдɇЋɘҮʶɪQԙ¤ʕǱРEѡƏɇɿг',
                'ɬťМ˶ηҭĻЛϫщКǧȵȎʚ˥эŔͺǦǑϟôѰʼΡƧĆϡ˦',
                'ʆȬʷʢʁЌҎύЉ¶ЬͶ˓NИȄăʇÜǗѢӊ{ηǃКl҅Ȗӗ',
                '\u0383ȐέÂͼŎƷ˞ѫӱαĮϸЋͶΌϠȪˣI΄ʐͱŞƐЙӾ\u0380gȔ',
                'ϲƂăѨҩô_ϡʔӵԔƁҠ»ҵǡ@ԃхө\x8aÊΟ¼ΰƞӯĐʬȰ',
                'ԊɱѭќĭĽөŔљ\u0380¹ƝɵɽƓ\xa0ѝаϘǋԢΚȿ¤ǇŌĿҦ4O',
                'ӂԫ^ԒĭźǣßʅÔȾгǉv,ƂГҚǪŪɱs˔\x87\x8fԀɳк³ԏ',
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
            'action': 'ΔɿѸαΰȭǯ\x96ºE¯ƅˉҮϾџƭTˡ\x96ˊƓ*˧иӎåϙɻε',
            'resources': [
                'ƌF\u038bĒԌ·ӷƧĆΔû\x9bΎćӏӡUŔК>Ɩǀt§ĥжҦ˄Ǥӕ',
                "ŔϹԏ\x82Ӱ@4e˓Ǥ˟ĠЃǇŮǡ_ʷȗǽԂȱʻ¨ŤΪɇʻ'Ϲ",
                'шǧΑ˻ȈёǔԔǸsΥLP\x8ațÄȦèƉʍƤŨʾŲӬүӞӱɁħ',
                'ŦȦpӋϨҸŗʄǧΡɏɤɵӾ˪ɡқ\x94џ:c0!ĥˡĚĥԞːӈ',
                '1ǠdԤȹͱɓƦR\\¬ΪϱřϏŽ\x8aξԖůˇΟȪƋ*ϻыϠ\x8aԢ',
                ']ϷƭƛP˾ŒǩӷΘϏӜԅӻƐėѣӶиɨӕɰ\x80вцЋɣƁұē',
                '½ÿ˱ϸԋҕӳɘ˷ˏȦʓŖʜԥʘԇːʇǁRȎнԆѹ0ʦĚȧʛ',
                'Ϛ)ӷɆǇϜŘӆŠĂ˯ɶÊЕϲJҟΎϴčŗЬŮȻИĿŇGчА',
                'ǿŧǡşɜ҉¦ґʯɭяһűӊȠžԄˌíͶαÕɑȎѴĎӕëȹð',
                'fϽΨ˶ϽԠèpƈќɠρĳ¼ʟǕƮϷԞƶΒĮьdǶʀŇáԀ7',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ď',

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
            'name': '΅¦ĴɗƠѭô˻ĉĵ¯ȭʋΆϨǈų<¯ͲҚͱǙ)ЭǛҙтĈѶ',
            'version': [
                -2653099039217128477,
                -7986632891422265054,
                -2473926351119937033,
            ],
            'location': [
                'Ӛź˪ŽϤéѰĒjɞɷѿȵӯɈΰҔʚAjӤµЍʱΘˁ{ӠҋĒ',
                'ˉȏŞˀĆ\u03a2ԇ҅BʭȢљ4Ϣúz#}ǹː˄ОBЫн\x9bӸóҸ¤',
                'vøɱúӎɟŭӵʤįΆĄѢǃŁĴǈϑӠȂӂє˷Θ\x85ĤŞЪŰʐ',
                '\x84!ʛxľέӛ҈ƯýψȣɄφ\u0383\u0379Ɯ˨\x85ѷϊкĺĎ>ΞơǾԌҼ',
                '¡ԑҰƉӵӳª£ǷɒѼϷȈëΛΈ˾ҭϷŇǦˊÑӓ˜ÍŽ\x88ɬƆ',
                '_ұɫƞϽÍԕЩ¢ǾƩǃԄǴªʧБȄΗìȃғžЉÔʄӪ3҄Ŝ',
                'ϟӇ˷}ʬȅΊöі\u038dӌeԃȄ{·әӜ%ʍӍģŸɝԤɦмĝɊЬ',
                'Ŧ϶Ϥƙ$ʠΣɋȋvԖԌϋžǈӱQ\u0381˶Lӈʙ:ëţцИΌʇΡ',
                'хА˩вɭ\x90ŧʚϤӥjПʜuƊfӥÁϴԩӼ.ƚЕѳȚŪ\x82Tѿ',
                'ĺӳþԔӞϬˮѿ\x85Ӭȶ@ԓϻĂđɃӼŰȦ{ŷ\x84ĞOƩъȺӶѐ',
            ],
            'runtime': 'ýԟϯӿ;ԃ\x8cЉǬǣԮ¥ԢҤȏēԧϥ˗7ƈƵɀΔiнӵЛîƺ',
            'send_access': {
                'event_ids': [
                    'ґԘь*ЙćȘ\x9cuѼǨӼ˨ȃіȉĘ˲×ԛԃĹҟXЩ>Ē\x8a8Ж',
                    'ĎѐǤǑǷʅшģʯǝћőƼ-Њ϶ʝʺжòλ˶ȿ^ЅѢςϨӉʋ',
                    'æĄ/ϓѱɻȫĚɶ|þҋéҋǆɣɧҁȶ,`źӵʴӱʮʍÑŮĨ',
                    'ȿͳԄTɃЃŵˮœǾť˙ƧǻѲȕ΅ͻ˾ǸϠǠȖѕÃӳǣtӳ˝',
                    'Ğǅ\x8fĸԌǌƽȚѿЏ˩Ѧ+Ǡv@¢ș˳ҖӦǉĎǃǒƇΘİ³Ą',
                    '5эĦȆƯӇˋǁǈõҝmʎʱxпѺĄǬ˥ҨΗƈiKưȪƾԂ˅',
                    'ȼȵ\x97Ξѳ|ЋʝѦжʔПӎ҉ʜ¯ϼβĿĴȽ˨*qϨʧуσЫ\x8b',
                    'πƷʁƤϴɅԊťӇŞʌτĥгɹ˶ӄҼ»\x84ˇWУϐ҆ʽťȄƹž',
                    'ʫΛҍİӉϐ',
                    'йēϲҏȻëӋ˳\x9aӥɠŒîèӵ,ƄΚǫсϏȝλȾԦϡ˷wʮѓ',
                ],
                'source_id_prefixes': [
                    'ЁӒĥÓBԁȸƾzԀΰȇˣƤӻƔУвğȲȯĤȩÌϮкĞʲΦƮ',
                    'щϡњњVyǍɜRāɦξƴÄҒӫśˊϟįМȐŬʽȉŤӠӦp҇',
                    '΄ƪƈ˪ωĒǫԔҰѼʓɃʒГyůeӇϖuӥĄɝɿҲţÍСô͵',
                    'ϦѴʄɴǝνɈΧѷȫΣˋʠ҄Uæ\x87JĔƌŚʨʸҟѐ}Μ\x9bҕɐ',
                    'AuʡʑưɾŒѫҕ\x8cӂҦӦԉʺ9ǛԠY\x87ôɑ«ӕȆҍʒчѸ\u0383',
                    'ˁөӹͽƫҦŨҩԜʂУǞѶŭєTȎҿ\u0381ͼҬϾĕÕ\x91Ӝϓȕ˼Œ',
                    'ŧȸԛΩ˽ѸȊӿКƎȮƸƄї-ӁŪкǢıɚɨӊȮ]ƭʑѾ±Ӎ',
                    'Ү\x8dгŮɪҼȔЉΙϛĪϧѻΙӴǧŊӗʋĵҏ¢èҨ\x8aӼ:Șȡü',
                    'ԧyѼć÷Ȼ˽ŔĈz˯ǒƼ\x80ҌԨҀɃУҺȺĆ©ѫԒ\x8dǲҔȲʩ',
                    'Ԉŋŏʏӥ϶\x9aǾӡͺÌυԫɏ˪ϲԭҥԜӠŒρȎtҥʨǍɄǀѿ',
                ],
            },
            'configuration': '"ԘКƜĤљǳóŤǪӒɪƸǿɂƐ8ƨҖћӻĊ˘Ƅϕ϶˪-ђǶ',
            'permissions': [
                {
                    'action': 'Ѥмѵ?ңēǉcВ<ӮƣЎϱǤԤďϭľȗƺQԮOΝԌ#ͿɫǴ',
                    'resources': [
                            'ʜʎ˲ďºƄϿŸҗ\x95˥Ӥ9ѡѳɱԔƟėĦвǆԄыПɺŵҽ*ҙ',
                            '΅ăΊļÕúɥȭȶδáƣ˚ðΏ҇ȺӲКȬȺɹѭǈ˥ĬӦǔҏԑ',
                            'ʎŅ\x88зɺӢǲɅʂԋƐҙӅ|¹;P¤ϯŤˬɄһĖϪΥ\xadʈϼЋ',
                            'КӚȑǷ҈IϋӷҲƉȪmȬԆмŠΖƥδtʿȡϋͽ:˽TϊЄζ',
                            'ČӰ҃ѡфɬҶ˽Ϝ2Ĳ͵˰ӆҰӮΆԗÊϯB¿qǻʩĻǒʚΑӓ',
                            'ΕΝԩɧȈ@ѼɽͷřņҔѠOϺ?ҸЕӯǞԉ˯ůӶ˔ӡϑǂfϢ',
                            'ӌˎӺö˳¿¶ӆȯўüÃĐǆȡàýώĭɖ϶ȈϸˇӸgϾҖyѮ',
                            '\x97}ӱя[ɉʕяʺΤþǙˉЉ[ÛȇŻˋȃĎƋæƴԞιŢŃ\u038d2',
                            'kӅƅ¹Ǫˮ\u0381ӦŰʣ\x89ΉѦƣʈž²ԗϳƾϗуŜ҇˩οÛǫ˾ԁ',
                            'ƕƥŬʆӶȣ\x92·ϸŹГǼƝԥɢːǿąŐϝɕұԐ´ƘnӐѱâÍ',
                        ],
                },
                {
                    'action': 'ȤɰǓŭͰϡłʞ͵ŽƓБɰǯԋʼȬ0űɡʨӥëȬӪƤєϭτ',
                    'resources': [
                            'ɔ˕vâǌцҥʋǰτņЊϔÎʲМ˩¹ģ҅ȼЍЎNŃȕÚPǀτ',
                            'ΨϧӃˢ¡ɭÀÅЙ¦ȿʍȏťӌ\x84ŨЎį˲OʘǩŢήǯǐ«ǷϦ',
                            'ǚƄҵҹʑȉťϲ"Жё\x83ʋ\x8cϲʹДӡҕҴƛ·ѧyȈȅƴøЪű',
                            'ő˷σɻϡàφӈ˜ûſĀʙ҃ǲˈˡ´ƦЉАÙȐѽѽȿԈуʝҨ',
                            'ԟǡБƭЅмßԒ˲ǾʼЙ\u0378јƘЃďĖ҄ҠʟßҥѣǳϲӯҤǋЇ',
                            'ЫƠŻʔĸəˡȈІ1ȱĚÁɇ3ʯɗ±ŌϖȦЋȥԜȜӱ҉ǚʝ\u038d',
                            'ԂϏǝPˣΰŽōůӛÉEлȍɪȽԍ÷Ԁœ}ɒʌЙɫңŋÒcʥ',
                            'óƎ\x95WÊЎ҃ɆYк©ХʤȦÐŤƁϹhǷƉĺFРηśΣмҦэ',
                            'ҮƲȖÜǰʽȬŔԗȅĊь ɏē҇ȍžԉɽʲƒĲιЊŶ´ӏìɅ',
                            '\xadɆØѯǭȰΚӻȫѡΐηʠƚϡ(ԘϔȞȜүϛδĽǆΣƈәҧÎ',
                        ],
                },
                {
                    'action': 'ʉсǽҙάƖċūý\x9eҚȐӧԤƂƙжɨIƓ@ДӑǢþȽ{ˑĮƂ',
                    'resources': [
                            '2;НŉƅπѠѳϹȔ\x86Ыʗ\x87ȉʙ4ԌűЊγɷЕǼɢ¯ίӕ³É',
                            '˽´ЩĘɫѓǣІźϠÄΓɂϽƿŇΕώѯʏ˹ӻÑӽȗŽȨԒПƶ',
                            'ӐнίŷɻҨƓȌčǠѡπ¿ξІ\u038b¾ʿзΊӐʐԗԈ\x80Ϲ6Ӂ¨ϟ',
                            'ϞͰąˑǔțʤѼӚ\x80Ɛʌɥqҩu\x8b-КƴʑϯжʂʍȩˌȦЅϥ',
                            'ԂǐәēĐ\x96Ѐв¯ŝЇńԒÆΤӗӾЉŝǪʯĕ¬ўҙ˥ȞǽηҠ',
                            'ƲŃρ˓ʁ˄ʗ\x80Ȥ\\ɚźȼԠƂ\x95ȕʃƚԫǛΘʘȶҖΰГӡ\x98ǝ',
                            '˪ҪѠġƆҫ%%ѩÀHİ˙ұƕ\x8cQéŦƭ¯ʘѩȞĻʄªÇȥǊ',
                            'ĪҐǠєΕΘȐőƗǠ\u038dɐǕԓћÂǫƴԓĊ¡vȖĉ\x8d©ήďɒ\x84',
                            'ȯȜȥĜΦЛ;ϹȴŗxәƃūϥщȈǪƆЃӀǇɾ˙ǐ×Тĭ²5',
                            'ʎǴ~ŲþšӵΕҎ\x86ƪPѴĿūφď\xadӄˣȏñҸǗϣʠΟҚYϛ',
                        ],
                },
                {
                    'action': 'ÿԏ8҈IѦʢνśʎàϛϾϧ\u038bГ\u0379Ќп±ЫMҞßХɲТ\x86ųǃ',
                    'resources': [
                            'Ӈǔϭ·н\x95¤CԟÅїӸȑˡȐȧʉǌʒ5ƷųНȚοɥԥYˑğ',
                            'ɱʂĵσɳ˷ŴΣԔеÑɕàВ"ҼďõɎ˭ʬЏϚȼȭlϛǮӮҲ',
                            'ϤɁͰϠԒ\x83ÖӜЁɸˡрWϟӬςˆϽƽСоɹŜXƟҢͿüǂ<',
                            'ѥԗЄҷʌ\x8eƌԛęϾюɉɣӥɯЀÊӓɓ}ĈϮȨǴɍҸҍÒҥÓ',
                            'Ȕʱ+˧ͻѬϳɊˁΓʔ1+ǄҕʯӇ£ϰʭгМъ\x8fӱΔҾѸϞH',
                            'гǨˍɞďѡȂŲ¾ѮʿцӴӚӏүÁ˸ҕäƿ0ќџУȐԫηʀ˟',
                            'ǜɏέшÞ\x82ǰƒpЫϢŶȨɲөӂ˯ϾѲň˩«įĮhМ˹˺ĞȄ',
                            'ТkɀđѵʗÀ\x9fҥʲEҊѝÏwѳďźѯȧ҄ȵě5ȀǥԫɼҜ®',
                            'őŏhЇïΨǸŲӁʎΟĒƇʯӳԃ!ǏcǇѧȖǅǝО҉¼Ì˥Ǭ',
                            "ǒ,ǃүʿʬJԗəб-Ȓfɜˁȶ{џѥˊʄƄϲ\u0381ЍңƐ''$",
                        ],
                },
                {
                    'action': 'ȢѨΕȫĳέԮʱİЬFӢӘŞϐўʌ=ƾ¾ҺØ',
                    'resources': [
                            'Ȣ\u038dӍò\x85ϗюqɟхƹΈÞĂ͵ѧхdÞŐІǂцȖȮȍŠԪȲѣ',
                            'Ƨј]ϼҬ˥ҪεűЈԑгǞˑ˃ġɂ°ɢҕӾǟ2ӭ˰ǻӯɵoЦ',
                            'Ҕ˥Ķҿ˂}čșŇȩ҂ɣҖN\x80FӚԜϾTѥόˢϞѴБɧσƤʥ',
                            'ƕtAsНѯɦӎђƧgʫϑϵƿţzǏɚԢO˟\x9dԭ¤һÄчӃ°',
                            '¥ϼ/УЧȮ҂Ȑ҆ÅѻԦįĥӍ#ҿ\u0380¦ӋɢɀźӲ\x92тð\u0381Ǚк',
                            'ҞŜȓ˵ӬǋћԕǜӌʀπɋȚȺïĨ@ЙΣjȰƛӾːёӉ˪˾п',
                            'ӐÜÙßϠҀƄtБϿͶpӌĉӜčKȀɊҷʋчЪʽөπ\x89\u0383ыċ',
                            '¼ĎˊʥĒƹɫĕϭ˒ɀȹǮŸЧSÐĠѕӖ%ˏԃƱЯǍɋĜȯË',
                            'ԃ',
                            'ӶƛŰЂƝϪҰ˳ȮφԈ\x92ǃŜ"ÛƩΪ-ԧ˺Ԛ\x85ŰǋϬʋЗŏε',
                        ],
                },
                {
                    'action': 'ϒ)°wΜʳE',
                    'resources': [
                            'яÖç¸ÞЖğɝͼӡŉ\x7f˱ʠϥɘԉνůʝůŪƭЃYйϋсª¤',
                            'ҽź\xa0ш°Ѿ¿йɅõƊ˒ЌγǶ±>ĐƮāϑ·ƯөһϝҐЭ\x8ax',
                            'ӗψȖҍˁ¼ÏµӾŌΐơѓȧˏ\x89ѿ³ˠź\x82ЊϜӛӴϻǞΪϧƉ',
                            'ĿÝԤƹFͰάѵɈĞɃþÄϷŇOW\u0378ɗӹŴеҢʧȰʱȷ*Ɓӵ',
                            'ҡҀҲҥĠæİҒϥƒҮ˱ЙȍTȒƍ-=ÉѺţΏͲγȲт»ϣГ',
                            '\x92˜Ц½\x86вνǞԤӧéҔå˒ˬūʨˤƺĩɒǔβϹɎ3µPþƤ',
                            'öӺӎςɧv(ēӷьˇƈȢ϶Ʉӕҕāǳëά]ǱƃǾOøĵӄʳ',
                            '˽ȉηεҘïŸ\x9bĳʐјĄ˹ʩЮ=ԚӤԨʫÜӐͻϻԒӥŦАΠͶ',
                            'ǹĢгλ¶Ⱦ/HȎЩ£ÐƷЏӱý\x9aɕEҙʥѱūЕ$ɞÄ\x94ԊѾ',
                            'ԧ˴ԄǉƷǌɔуȟŶΡ\u038dÞҐϕԃ\x99ɿԎȀ®ŏҢĥɂ˖ԓҲҎ˂',
                        ],
                },
                {
                    'action': 'ӹϢфǛ˃Ћ¯ŁʒҧрǦUͺßǁƨѤł°Ϸ\x8aǨ@җ\x9fłӞǍn',
                    'resources': [
                            'Ɯ˄˩AɆʿφü¼ʝӎ\x89˨4әƃÉšƏжʠŰ\x8fұɌďŲЦ÷Ƅ',
                            'ԏˇ϶ȦӳřΦƻƎ\u0380ǣƍ±ҼȢеʤŇƧ9ԕǡɇΔ\u0380ǑŦ˛Ԡѥ',
                            ' еÉҰӨǼʹʘυ\x94õxҹƴӼΩҔɯˋǇǃȭȻĳ\x9f3Ϣϫʋ¤',
                            "ҳĕ҅ƣ\x7fпĳŊе'Ʀ«āˤϿĴ˭ŜǝЈЀϰέһ˶ʀʋʤпѬ",
                            'ʠЗҘɘřΧRĩӈ\\ɯƔMҷЗϚːlѪӁ=Ϊ΅c͵˥ͳҰҊĝ',
                            'ȧѝыſΉҜ϶ɈńŲԖÄˉÖСζǸ¥.ʿǟӶ҈\x94ϯŐŇEɴɘ',
                            'EDӬ\x8aћɂɦԐ˩ԦϿΪƎΊŌ˓ŇȳœԄЍҖǓаˑĉѡУNʆ',
                            'ʭÏȢ#ȋȒ҈¤ɶoӈҘА˫ƺҫдͳƬ&nţˏðӞϟǅɥҏĜ',
                            'ÞΫɊԝӜʶȆҩǌƈȕũ\u038bˑȻ-ǒӄ\xa0\u038dΒқҌӢȌ¢ĨťqƮ',
                            'ӁŹΎŻҠӁҶΈ\u0379^˒ʵƞǃäőҳȶȖʧӭфǁҹԪ\x80ьϳǹś',
                        ],
                },
                {
                    'action': 'Іϫ¢қҨ˗ƙβЖɗӉɃʥfW\x84Ϙѩω\xa0ʟϣŵŌѝӜǴɋԫԙ',
                    'resources': [
                            'ԕ/ȴȭəԞ©ǚ˕źÝ˥\x98éʍ0īģǰѹƧԘ§ņʟsԐʉμ&',
                            'ǔóп\x91ŕ¨ģӝïȒ˩Јŷ\xa0ɯжʹЋʷ˔ҋБȝ¯šō©ĄҖȳ',
                            'ȰÛȯӗ\x93жЃĀZˣЋɹ×ҧĔr,ϙ҃òǕѨтçѼ҈\x85\u0381ĄƟ',
                            'Wԡ»˂°ɠĀųʍÙ¾ҖǱ\u0378ѸЅŉЪȘƘІÛ\x8bʂǃԃҠʲȭЎ',
                            'ĽǒӀǮӾòmц\x8fȗԄёϱIѬӎҸȗӠӡϣ|ЃǗęĥΉĆâɢ',
                            'ǜͽѹŅѣӊʝԋәҡ\x86Ӛ˭ŒÖƿ\x84˧ɻͷƟÈΠҦ˚ȏȆ33ϋ',
                            'ĵЉȀʦԝгђǶ\x9aɚ˩<ɓЖІÿӦȍŬɋęϤ{˂ÞƁТǦЏʓ',
                            'ɹˮɟҖȋǏʄɌˡМ)ˌӮбΦŠGĪŷ²ŎӱŻȾɑвѡ&Ëȵ',
                            ']æϺҒЊʸΔЉʙԥԜʟˬ³ɚʵȖѫǑ7ɣʴяO',
                            'ʆÓԂϚǴ{ӛƺʶħ\\¦Ҁ˶SɳΚ\x8eКɮƃgëЀƄÄîú8\u0379',
                        ],
                },
                {
                    'action': 'Тāʻ',
                    'resources': [
                            '\u0380Уɂʆƒ',
                            'ōʶάÚȻʫƅˢ_ƈēӯӊŌЅƿ˚ԡˍæƚʊ˛·ӚɷӓŶїѢ',
                            'ɸԖÀĆŶʳȻɏҹBҲƥɫ͵',
                            'ǆD~Ңr҄Ӌͷƕ¹λӊԇ\x8bԌ#B_eĢԒԪ\x87ȎƉȱвRŃȒ',
                            '»ŮϡЀӃҊαӕ\u0380ƠƲɇĔ\x88ɁјԇżȷÛѪħǷ',
                            'ĺōˡӁɝ˛ƏʂЫϐAҪǒ}ѵƅѿ]ɷĕÝɑɞſɹЀƝĠǎǡ',
                            '\x97ɐņѫҤȵπţ˙˰ӅÙȷΧѾϫϬ;\x91ƔͿɫкΐԞЗҞ\x89r\u0383',
                            'ɏύҾЀӑҴ\x84ƴƂԅƎԋŪЈ¥ɻѴ>цĒʰRǵþϪeҊҬnɡ',
                            'ʾҿưʩƸɺɤѶӇɴѝƏиĊ\u038dʧ°ȊҭƜʬϲЇȌӽ\x89əЍƘΠ',
                            'ЃЮþǽȤҀАǬƠЕҾɩιa˶ʦΨƕŇԡσϼgϙΉßĿʔпX',
                        ],
                },
                {
                    'action': 'ƀԚɪԈXǁӃϦѥÒɹëˆѱҵ˳ѪVīӞӯ˦\x8aшϻɌωƘɅњ',
                    'resources': [
                            'ǑϺƱŒĺҔɟpΛƾЖȲ?NѩɏӢĖāň\x9cʆˈ&ȑÂӝûΘс',
                            'ϳҋǎӷα²ӒʡϚȩӼƮǶҵɉƨcΐϕ¥ɇѽɜЩȉɴǐқĄɳ',
                            'ώĎȚƍϵ»ЮҴ˙ԕ\u0378ŔĈýŀȶJïϏŵʶŶұрӗљʤ˨ёԜ',
                            'ʵԊʐљţӟЛ_ē˧ǈÌίϦЂʅ{ωȓԒǘϻ@иɌĊӱ\x9fʪҼ',
                            'Ò%ȶͱѪωƧ\u038bǖпŞԞъİȜŹћ°ǙѮϡеѩ;˩ˡǗΥļҋ',
                            'ƢÞǡŷҙƗ˜XĤrԙǥ-ȢӜŧkĴã˪Ĭͳǌ;ΚӜǗȴĊϳ',
                            '҄˗ȢɃǮɺ\x85þƸʛĿȎοψ¢ǍÕҰõ ԚЀĩĒУҕ˃ˌԒĈ',
                            '0ԙƲġԠžНOǈɡĽȟͺΐɿʯҳӑêХɷЭ`ҼĦǦӹӱĻѳ',
                            'Ģь<ΎvφҺɢЫ©ö\x83ȫӗ˽ӹǲͿŖDǁʇ>ЬԔńϰ\x8c»ӵ',
                            'ԑĻ˽Ǎ[ΠέǆЗʋ\xadϨē҄jЫΎŻѰuůǪӅԞġüп\x88D´',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x97Ѫń',

            'version': [
                -8156704404177167361,
                -6228255338537598801,
                -7492874083717493183,
            ],

            'location': [
                'Ё',
            ],

            'runtime': 'ϱ',

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
            'name': '9τʴˍɎĽ0ќϟůŇēԎĳϱ*˪ŵ˃ȻӚͰßɗˤϾʡǮӗʹ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ԟ˂н',

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
            '$': 'ȢɔЎʁǳǇѝԏȖҷƢҀӬʸ˦Åɘĕʚѫ˳¾ʸʻ\x88éˠ˘čц',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5124396231393901394,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 398214.897085861,
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
            '$': '20211104:182021.889030:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ɶЃΡ\xa0°њȰ\x98ȍѕŕϏưY©ɭБԡѣ®Җ\x89ĝŦǷϿɟOjμ',
                'ǯşƙˬԦƝț҆ƍӶIĻȞ*ʳәȴҎӫ÷ɍǐњϮ°ϞУ%ɩѤ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -57695770725271054,
                5768608200451023649,
                -8869107894389261370,
                3907730402497271141,
                -4036207117513024888,
                4105695770432896831,
                4162886473862400444,
                8522963092262185665,
                -2272043146389718622,
                -3989581706878712654,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                360051.51171326963,
                256245.84570660768,
                100637.10452186424,
                228099.69430053607,
                906510.4833177306,
                397991.7763859446,
                851255.2589051558,
                14593.512664291979,
                213513.329254538,
                232862.97289307875,
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
                '20211104:182022.693736:+0000',
                '20211104:182022.710303:+0000',
                '20211104:182022.727487:+0000',
                '20211104:182022.744577:+0000',
                '20211104:182022.761796:+0000',
                '20211104:182022.778787:+0000',
                '20211104:182022.795304:+0000',
                '20211104:182022.811981:+0000',
                '20211104:182022.835562:+0000',
                '20211104:182022.852375:+0000',
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
            'name': 'NӠ˶˞ĴRǲˇæФÊƫӥҳƩɽŏЫɧ%зđѲAɫì˞ϱʭĄ',
            'value': {
                '^': 'string_list',
                '$': [
                    'ҧĕχǦɜŝϠаHʅБȒ\x82ÎʁľҺĪџԆ¯FƑz|Иʑаώq',
                    'ɵӞҼАҒÈŻòƎƒЎǌʲΗИκˍȀИϢƘ\u0381ԟƲǈÒ&ƮCČ',
                    'ԀȗǦ˃\x97һƵŬ˕Ч˅}Ʉ6ǁϝήâ\xa0ԫҞɓǪϨʛРҷΐFζ',
                    'Іԉдȅĕ!+ΥЫåÿɼ\x87ȁΨ϶ԊƸqZԛȹǴǰƍȫǥȜȊ\x9b',
                    'φİpΠҢHηƬ^ßе\xad\x9cÝοɅďϑƸƖЈ0ü˱ȫȶũǄņ_',
                    'ÉêųÒǩҢ´˱ŭGК²ӔАϘ\u0383°ǴɇɧАʂȲѓɚъ»сѐĸ',
                    '\x8fҒɂӗGȕИɫ\x80ªˠ˅Ÿ·ɃѤŹ͵˗Ӎ˘Ç˼ҦǌɇҰżЯт',
                    'ƦŴşȄ˗Š҂άʥЉ\u038bDԫħ·ϝюϺЫнďÛ«ɐʘjɍʮӕŞ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'А',

            'value': {
                '^': 'float',
                '$': 812669.4419257555,
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
            'catalog': 'ʸŶкɍͽVūǷ»[ͶЫʪÆϰуԙƌҎ˳Ќө|Ԟĉ×Ģȶˊϣ',
            'message': 'җɮȍќҖΊɍҲǟ˦ˡŰɤҥʿӀøΣҒĜÖΆϕìǭʼʢҚΙо',
            'arguments': [
                {
                    'name': 'ǻԗЧѱεƱЉȠȈŤsŇԠsӍ¶ѲѽҔӔӮƏŭľùʛđŨӿʃ',
                    'value': {
                            '^': 'float',
                            '$': 455881.73324251315,
                        },
                },
                {
                    'name': 'CʄlӷǜϐƧċΠʈ˾GƚӬѵѠѴҰǛqɱɂҩ\x8fLΆθ\x8cӬɫ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        True,
                                        False,
                                        True,
                                        True,
                                        True,
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ǘƄ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20211104:182020.507281:+0000',
                                        '20211104:182020.524093:+0000',
                                        '20211104:182020.540547:+0000',
                                        '20211104:182020.556904:+0000',
                                        '20211104:182020.573553:+0000',
                                        '20211104:182020.591898:+0000',
                                        '20211104:182020.608581:+0000',
                                        '20211104:182020.625799:+0000',
                                        '20211104:182020.642075:+0000',
                                        '20211104:182020.658447:+0000',
                                    ],
                        },
                },
                {
                    'name': 'Ԙә˦â҄ωѳ=ƟҖԀԕΛϘυүŇ˚',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        492216.45267228596,
                                        887417.6210631133,
                                        627111.9244431433,
                                        712018.0991403981,
                                        838844.0745688785,
                                        660152.6502077929,
                                        157067.7350446055,
                                        960897.8688501862,
                                        858729.5944616775,
                                        716748.7667151882,
                                    ],
                        },
                },
                {
                    'name': 'ϮŪӺӑνÉǛFÎȪΧ',
                    'value': {
                            '^': 'float',
                            '$': 61558.790677533136,
                        },
                },
                {
                    'name': 'ʛѓĀͽź9rǴȦ˕ľԡШºǺȂǖҩҩ³ŹήиѩʅŞȦȈiЃ',
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
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'Ϥζ˖҄ϛ\u0380ϬђѴҽѱīс',
                    'value': {
                            '^': 'float',
                            '$': 507981.44063267147,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '˃ϐ',

            'message': 'Ʈ',

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
            'identifier': 'ơњѩȲÊ¼ˌFҥųĉ\u038dӡćɋŠɜȾdʦëùʫȘĴūӎʳŢ/',
            'categories': [
                'invalid-user-action',
                'access-restriction',
                'internal',
                'internal',
                'configuration',
                'network',
                'os',
                'invalid-user-action',
                'network',
                'file',
            ],
            'source': 'ʰΜλȸʒΈƥwȽтǖǄǼȧɴŋÖǸӣѓϹƚʾΔӵͶƚ҉Ҙ}',
            'messages': [
                {
                    'catalog': '¶Ҭǧʹ~Ē.\x7fœǄҋҗȡӁ\x83ðӑǑŦǾȔϿ˃ҠǅĈȞġӃȤ',
                    'message': 'ƮlњƞʨRɋѻŊƄƫρНϪŶԟŘǁѿХŰҥћϗǋ|ǫΌӖǈ',
                    'arguments': [
                            {
                                        'name': 'ǼàīŊЩӺь\xa0ªѮ˹Ƌ\x9dƽΚœȾѠŖŽӠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʮÉΒԓǯųħɴɢƧϒɽÊЍςςҊˏřϔΩԪ»ʇ³ѯϾŶˡԍ',
                                                    },
                                    },
                            {
                                        'name': 'ΓʅҕҪŭȵѺ˙ҩβ+ԍďŻƢʿφԩТǓҜ˸Ȕɘȶ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ŏǊήЋю\x92ûϊþ˭ΒͺѧɯɅʔΕЫĕîԜɽɴϙěԉÂ<',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182004.169370:+0000',
                                                                            '20211104:182004.186789:+0000',
                                                                            '20211104:182004.203463:+0000',
                                                                            '20211104:182004.220348:+0000',
                                                                            '20211104:182004.240262:+0000',
                                                                            '20211104:182004.256849:+0000',
                                                                            '20211104:182004.273685:+0000',
                                                                            '20211104:182004.290405:+0000',
                                                                            '20211104:182004.306953:+0000',
                                                                            '20211104:182004.325969:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʼɄΉʓů',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182004.412280:+0000',
                                                                            '20211104:182004.434288:+0000',
                                                                            '20211104:182004.452476:+0000',
                                                                            '20211104:182004.469138:+0000',
                                                                            '20211104:182004.486041:+0000',
                                                                            '20211104:182004.503214:+0000',
                                                                            '20211104:182004.520057:+0000',
                                                                            '20211104:182004.539524:+0000',
                                                                            '20211104:182004.556255:+0000',
                                                                            '20211104:182004.573912:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϭńςɝƢȁΑЉεέϣԣφq1ȝĂl',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3620007334407915147,
                                                    },
                                    },
                            {
                                        'name': 'gќԮѫśĺȖӃϽӹɁ\x8bӠʬoŢϠӸԜƤмϿǿϡ\u038dɴ¸ҽƖΩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϸκȌ6aʁğЁϣʟʏĎǭш\u0379ƫВʅ¦ϋӕȖʳϤțҚƢҹʨ&',
                                                    },
                                    },
                            {
                                        'name': 'ŎЂê˰šЗĘƮҭĬЁϷýɠǠ\u038dǖȱϝɵ˓ҿȕǶĕʅʐƴŵʋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'î\x94αпϺ;΅ɽ¥ԏɿȬȍzЕʉͻȏϹɡ¸\xa0ʙČ˟#\u0380ĸЦƂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ù\x9foΔĺΝƚʆɻ҂ƻǆ\x7fЪӡğˑϚƺ]ԃyѷӥəŹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182005.147134:+0000',
                                                                            '20211104:182005.163866:+0000',
                                                                            '20211104:182005.181239:+0000',
                                                                            '20211104:182005.198468:+0000',
                                                                            '20211104:182005.215447:+0000',
                                                                            '20211104:182005.232982:+0000',
                                                                            '20211104:182005.251788:+0000',
                                                                            '20211104:182005.268628:+0000',
                                                                            '20211104:182005.287185:+0000',
                                                                            '20211104:182005.309456:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɮxѧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -54019.777659498526,
                                                                            759355.1975432241,
                                                                            625666.4934579334,
                                                                            348979.7529278595,
                                                                            703930.33503314,
                                                                            143409.1266363086,
                                                                            877279.571256433,
                                                                            -52168.86410987096,
                                                                            292776.97413926653,
                                                                            861811.3332034347,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ːҹǇðБġ[ϔӒϹϒàùԕöƼ\x949ѩ\x9aѴԩ¯ϬӺĦӓǩ˥ľ',
                    'message': 'ӄȆӭƹǽѮ)ȅ8љƧ×Ȳ\u038dɜǿ¾ϝȚӌяϢԊȪNҊЁӑ÷ǰ',
                    'arguments': [
                            {
                                        'name': 'χӏƔԍʥßïǚˀȭmʤҍɧ\x83ϲ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182005.740057:+0000',
                                                                            '20211104:182005.758086:+0000',
                                                                            '20211104:182005.775575:+0000',
                                                                            '20211104:182005.792308:+0000',
                                                                            '20211104:182005.809904:+0000',
                                                                            '20211104:182005.830179:+0000',
                                                                            '20211104:182005.847183:+0000',
                                                                            '20211104:182005.865686:+0000',
                                                                            '20211104:182005.883512:+0000',
                                                                            '20211104:182005.900810:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѼÑɀɊōɀҡšЛѻƫǪ\x8aћȼӇé˥тȒǻśz\u0382Ѧ˧ѠВЁϙ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȸмӦɒ\u0381ҿοǰѻɯpɼҞң×¾Ǎɣҫӯǧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ο\x9fǪȇ*ȹ]їʏѐĨ\x92a°Ø3ȟUƢҀ"ɥ˱ǻĤƢƏԖѿӴ',
                                                    },
                                    },
                            {
                                        'name': 'ȗǧћǠ\x9aѨђĐϱМ.2ǽFα˪ΦàŹΛ´˩÷ðǂ\x87',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182006.131026:+0000',
                                                                            '20211104:182006.147805:+0000',
                                                                            '20211104:182006.164224:+0000',
                                                                            '20211104:182006.181184:+0000',
                                                                            '20211104:182006.197617:+0000',
                                                                            '20211104:182006.213847:+0000',
                                                                            '20211104:182006.230296:+0000',
                                                                            '20211104:182006.247456:+0000',
                                                                            '20211104:182006.264727:+0000',
                                                                            '20211104:182006.281575:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʵ\x99ʱ.Ӷ\u03a2ǱϵӮңԚƫѿϧϧƂșƫѝġҳ¨^[ϒϞȜсĈɕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182006.368081:+0000',
                                                                            '20211104:182006.384866:+0000',
                                                                            '20211104:182006.401689:+0000',
                                                                            '20211104:182006.418531:+0000',
                                                                            '20211104:182006.435562:+0000',
                                                                            '20211104:182006.452955:+0000',
                                                                            '20211104:182006.471309:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƴΔӐFēϱŁ˗б\x89ѯӭǵх',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɰǯǀˊİƘϕͲȓЋρƉϴɝӝĤцѤ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182006.630417:+0000',
                                                                            '20211104:182006.647401:+0000',
                                                                            '20211104:182006.664418:+0000',
                                                                            '20211104:182006.681098:+0000',
                                                                            '20211104:182006.698125:+0000',
                                                                            '20211104:182006.714866:+0000',
                                                                            '20211104:182006.732436:+0000',
                                                                            '20211104:182006.749963:+0000',
                                                                            '20211104:182006.766953:+0000',
                                                                            '20211104:182006.783833:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӰȍȱӦźŤ˲`ȴԅrǨ\u0380ԜõӴĽƷ?Ôœ^њҊ\x95bƁϪńñ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3660940345971019137,
                                                                            -8501319599126757190,
                                                                            479669995953695519,
                                                                            5325698904039769733,
                                                                            780664382557014628,
                                                                            -9022709341319893840,
                                                                            -6587157706641621423,
                                                                            6130026066578459050,
                                                                            -609505624516823090,
                                                                            -1930957924226741808,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϻπȳËRϱɜ[ȉxĤюƲҡ,ϟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʬҖǌʇŢʅԨɣŘŵƐˌϞÂ˵·ѣűͷƂѶόɞԤИǯƉδәԤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5725368343068197966,
                                                                            7013365518698736738,
                                                                            -5204879397749012732,
                                                                            4724625127861543828,
                                                                            -1763299571351699733,
                                                                            5852469913407985259,
                                                                            -1521261952548811286,
                                                                            6706643842873555690,
                                                                            1908319657027394498,
                                                                            4244481309854009820,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "XƿĴЋғ'±ʨ5ƽǍĘĬ\u038dµ0˰ĊĭӵɓϓċĩЏɫȉҍԩ˓",
                    'message': 'ǡ#іҭ¹Κśķ˩¦Ԛ3ȚɕéćȻōҒѾµ˧ϠņȠӦèʋɝÎ',
                    'arguments': [
                            {
                                        'name': '\u0382ǫ\x9cґġ˫ɭчÌ]Ү¯ĢНыʹȻҫҗ\x90ŠɍĒƽ˽ȩʚȬŦz',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȨʑԢӟţÎťȂӖШîƭUɂӖɑńƓʿҐĠɵҸҡɔĲŽӚԀÉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            869035157215634398,
                                                                            -7552439239714239955,
                                                                            2450001202844999122,
                                                                            7107666034141253329,
                                                                            -5635973494130126839,
                                                                            4654096713289374108,
                                                                            4162169030699667655,
                                                                            1925881720429595632,
                                                                            -1862477474482448979,
                                                                            -5408451150941838959,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҝ$ĢÓЍŜ^sʎ˄Š°RşʎҤɮ\x82űѺƑӈƩ«ѵĪĭƬÍp',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '0ѭåüġΦÞ®ΘćҎϦҖϏƛӫή\x86Ӑıӈɰǉ"ǮYŠΊɭԀ',
                                                                            '¥ɣʙǎӚƯǂȜĿĪĉÙǦФ\u0379}ȵԃ¤ьˣːs҇ͽЬҁʭƇЬ',
                                                                            'Ưφ[ŁLΑÏĄєЬɹé҄Ȉ3îƙƦ\u0381ĠӿɝԎфƲѬʢ˨Ƃť',
                                                                            'ĻСǤFåӔҾ\x8cϦÕұЎϷ˘ɢǈəǺē×˦ƍCʾ˶έρԗҢȯ',
                                                                            'ʵҮҠӫƯ˥ԦίʺԥӇŇƫīĎðӤ\x9aϼcǤȻӷΕѢˇͲÒΪӑ',
                                                                            '¶ҟɊ\u0378Щƹ˯¼8Ρԇφ˝Țԝ*Ȝ¾ĲӺԉѵxНmϬʩɤӉê',
                                                                            'ȂɍŎÝËTo·ƗƳρ£ҡЛԨξ˞ļP6˘ƃSԥƽӱ»Ÿξʸ',
                                                                            'ϻðƆĪȶˎҥ˦θĈΈѫЛ\x8bӒŕϡίÜ\x9dǆʊʢΑ7ɹ\x8bȸɸ҄',
                                                                            'уƻ[\x90Ƭ˗şǗƃ϶ɕƅȍКΖǢƫ˪ü&Ϭǉ0ƬЬǻ˼Þʮр',
                                                                            'ҽ\x81˟Е³Я\x8cӼ.ӵ˪LɰӪБѲƭŇʬʨȅơŠϭBŬҾÂĨþ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԃɅчԪoƩÕ]ʍûžЫTϮҤĞ˾ғ¬ʎĄбĿϨȪύƞ\x94Ѿž',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΡТǾСÌӳqӟ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182008.341807:+0000',
                                                                            '20211104:182008.358530:+0000',
                                                                            '20211104:182008.376011:+0000',
                                                                            '20211104:182008.393153:+0000',
                                                                            '20211104:182008.410267:+0000',
                                                                            '20211104:182008.427003:+0000',
                                                                            '20211104:182008.443853:+0000',
                                                                            '20211104:182008.460789:+0000',
                                                                            '20211104:182008.477729:+0000',
                                                                            '20211104:182008.496295:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĠÞΒĒθ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '҉˨ӯ\x8e˻ħǪϗ\x9fәȄщͲůNаνёǨ҆|ϕήşÝā˸ȣүͳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʵƪʎӔɄǦԦþдқ¸ȃǹҺ\x92˅ʩĩӉћəˢ\x8bӵʿӝұĬ˃Њ',
                                                    },
                                    },
                            {
                                        'name': 'ϡ¡κԠˊȳø',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            128961.28823385623,
                                                                            706838.9219315462,
                                                                            18167.73723791784,
                                                                            57883.16126128397,
                                                                            746332.3071685957,
                                                                            234312.82338813454,
                                                                            621689.6774164716,
                                                                            944066.4799276995,
                                                                            541101.9329340948,
                                                                            998840.333906888,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҏw\x91Ɂʵ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': '\x8eCԧÚ\x9fίȕǯǗȑ1Љ«˯ǮĵϵɳǌҥӨΩAɓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3901217160470611769,
                                                                            -4415815523004962229,
                                                                            -6001100854641797168,
                                                                            -8554864621396798508,
                                                                            1827661748427124625,
                                                                            3619001424400357192,
                                                                            8388424706163570135,
                                                                            -1346322656469424441,
                                                                            168685487791817662,
                                                                            5973706323715787139,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'EńʛǢҴĎÝȕ^Ł&ǳѵȭØǎьʹԝӎЃpɣĄѠ½}πȫщ',
                    'message': '\x7fζŗėϬÚԒҰĺϠęСȾfqˮőɴʡ˥ǥ˝\x93ȟѬӛԎ\x80ȶ˴',
                    'arguments': [
                            {
                                        'name': 'Ɩ˷3»¦ҡŧҒĉʷδŁˋǧфΖȟԃϛԕʹ\x90хų[',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɇɌӠ˽ңӡèҩĝɟÅȎӄȢΥœΗџЮiǿΠʏƪϱѡ,Ϡй',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӉԖ;ŠĝғȱЀ¼\u0380ɳġ¢ȨѮëɊĬϭԨàљϚΔЫĂ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 529461.625782578,
                                                    },
                                    },
                            {
                                        'name': 'ҲӥѓЌӪé\x90úαþҊΒ˔ΰˣӃϺYǎĞƍЊOȳҠôҹЭҒœ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182009.937437:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƺƒ˯ˬŮũʣÒ,˸Ɖ\u038dʬYЁɯšѵҕЄá˛Ƒ\x99"Zɝƙ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 393090.53453083057,
                                                    },
                                    },
                            {
                                        'name': 'уɌΦЭџω^КƔʽϪƓϽȷӠΫġéěɁЏʖƛʕʏʻτŚǀē',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 331306.2527812277,
                                                    },
                                    },
                            {
                                        'name': 'ˮǋ½ȈĈЛĊ©ӄдɅ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӯǣûζҘ˒H˒ƫƑ<χϻŨўћʅѦƗœԝƛʨζáПжϬȎÂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3862707458103906932,
                                                                            -5986503875158918108,
                                                                            1200822145462913446,
                                                                            145174113238020602,
                                                                            -6737730111862141130,
                                                                            -7469515627262052008,
                                                                            1262711864983242067,
                                                                            -268766935499112302,
                                                                            3502329917352232006,
                                                                            -1476049625773662479,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҉˾PѤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҬƺƉϋǾŖŊǠҏФȖʦ˼Ƒ\x82ΓȎsƵȅџΛɕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 240522.5703216268,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Òż\xad0ԗɛʴˇϹǨԌӓΆƂļπʹʷ¶ғԢʪҚҤĞKιǂ´Ā',
                    'message': 'ϹğɥƥђƶпfƂ}ЂêčѝŅӪǷVĂÈ~B¾џȐЄĹƗƮˍ',
                    'arguments': [
                            {
                                        'name': 'ʔěŏɓȵϹŇΙºʃʳʨ\x9cөѰˊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2922852391785292583,
                                                                            658063664875585563,
                                                                            -8713832116637221854,
                                                                            -5692115694056957225,
                                                                            8567749886690804423,
                                                                            -2096636853860322105,
                                                                            6803436680003543885,
                                                                            176434194092023134,
                                                                            -6902196897473148097,
                                                                            6970491261047429019,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˤԊǆӡɳʳύӏĳȄʡβˉэćȰʩÐ˝ūΚԭeȚƸŗҶˑԠ˕',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7541602552717489210,
                                                    },
                                    },
                            {
                                        'name': 'ÐƤЩǵ\x84ҽƦ©ϑA±+ǷӾ˥ʪӮƮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1505423981924423928,
                                                    },
                                    },
                            {
                                        'name': 'ǃѻǄįƫˋǸǔA«\x9bάԀҕŘКӝʠӎíѥƹƄĞƎϐśzѥƢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            537218.8031114993,
                                                                            489137.62555430876,
                                                                            912656.3694838971,
                                                                            180767.6286464411,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɣЎӮȂbĒҐŖ҃ʹʍř',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3997551361839095164,
                                                    },
                                    },
                            {
                                        'name': 'Ѕ²ˉ\u03a2ϐʫƪǣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʫnεЉŊуŰӃŒ˯бҾɸʑöɣɓǓҍʦȗǪũéƶ=ƓͷÇλ',
                                                    },
                                    },
                            {
                                        'name': 'Ş',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǯ¬ԡϠ˦ęɆĤШ"Ɏǹȩ\x94·ҖǣІԬ§*ήӅԇlÅΕčҗ\u0381',
                                                    },
                                    },
                            {
                                        'name': '\x91ĹþϐӘАѕЖбøpϢԔШǂ˙ӘǗ-aƨͳëʏԔȜԒȖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '҆ɜɪʉɭҭϢԁHԁȆjʮΎɔÆˣɍȸιõҿŇǃ˩ťΆˏțƓ',
                                                                            'ŌϤƖȽҬӱƯΆĆПĚΊϒӕ\xa0ʛұǷԓïъĭÛʙʨύƓХĿY',
                                                                            'æϣʍĥӊјĊӉRůNμźҪ§ĝϙӣê³ЦƮă&`>ԅЙƀŲ',
                                                                            'ʴԟϼźȢнÿG\x8dͲʴѕώǲɬȻŏéĂјҞǥíȄŦěW·˦ǒ',
                                                                            '˗ҷ˂ϓКωǥϥȠψȳЍƂBr¨dКѭ͵ǡɅ\x93ΓĒӖʿˑȚː',
                                                                            'ʬϧʀ×ʙ\u038dмɮˌϱÄÍħЩҥƞŤŤϦɠӎΰҤ\xa0¾ʝҮûNǃ',
                                                                            'ȆКБ\x98҅ƳЅ˘ͱ˫ѻǋųŤ\x87ѿ˥ěĔɦŅŪԠԣ=ëԘƌɰТ',
                                                                            'ǁVǥʥӎӝӼӗîǪȨg\u03a2Ų¸ҽъӺЏˮ\xa0҄Ɵͱӟˬη¯Ȯϔ',
                                                                            'ЖɺѹĊAʼťȝӈĒűē\x89ȌӟΕɍӊӧɅ~mҕЗǇ¬\x8aоͰӌ',
                                                                            '˩ӌRƠƙżЩ˵ΗǗҎˊȯԠӳǁӒƩкɵø˲ςeԭȅυъ˝϶',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϳ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҋӌϫ҃ɇԓȏǼΆԛ˥ϕКəȱņђĀČӃŌ4Ҭҡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҿΎй¼Ͻԉ˻ѤʸӈӣƖɓİԒĐʠӕȽąˇоĹЅǂЧφĘäӜ',
                                                                            'ɂҨȦàωԂφ8ɚѽſ0γ²Ӳ˪õǚ<ѸȷîºUÛ§\x9fɿΧł',
                                                                            'ђЁӵђΒЪȿԮĎǜǟǓӊЋʬlÅǮǽɷ¯˭˧ǝɝ8þΛԘȐ',
                                                                            'ȫƘȎćťӦüӖƓԅɏӑƎȄίЪԔ˅ǠЭȍɃу{УΔ\x94čШǲ',
                                                                            'ѶѴғŁүƳĈȐeŢ҈ҁϭˍȫҒèbѝώʵΚУЏÚűԌϥUÖ',
                                                                            'ҩaӐùƣĈʺϟ\x8eǣӋѽɴϱȵ±ԒӡɚǪVʃҒЁиÃγ\x84Ʀ¬',
                                                                            '\x9aɆФŝīƴXʥԙˣg\x8b¢Ň\u03a2ǃŅɐȔêЊ˹ҤǋƎÌaWЉQ',
                                                                            'ƆŗІђǀĩԑ˝ȒϱԠǄї÷űaѲčΤӢɬĲ˔ȡǐӖεӚϰæ',
                                                                            '¿ŸѷjɈβЋƃλ\\τĳƓʢВ˕û#ɆȂŜ\\µĐŕТѸǐňў',
                                                                            ' ӡZȞ\x94ƞǞɳĽυƼщǗʃȓˀʚɮѯ?˳ƻϴƦūѭγϵĚǂ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϬɎγѰƼҴԩњЩҽ˹Ұ˫ɘѳҾӗɀЩӂтԫѥBȤÏԭŔϷɾ',
                    'message': '\u038bҿΦӘӃĝдƔȥӬȼɢΒӝ\u038dӛ!ε\x99ʞҒƭɦ®&{4ҏęм',
                    'arguments': [
                            {
                                        'name': 'Ώґʱβ˛ӓȼϓʸϒϦęȬǰķ\x7fÁԜƜϹ\x80Ŏ¢ҴөѽƩş"Ή',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7688307388831767877,
                                                                            4566333210777619409,
                                                                            -8148978524015904834,
                                                                            5691019767427993600,
                                                                            -4554945967549449054,
                                                                            2189408505349028187,
                                                                            -5998178651950954973,
                                                                            4208392563520358451,
                                                                            -4309233638052741060,
                                                                            5927139552640510746,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'jʥ3ƨЙǝ˯χoҙҒ˃ʋзĹΧŨЫσȮʶǝUЬÀтЈҸȖp',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182012.413502:+0000',
                                                                            '20211104:182012.429969:+0000',
                                                                            '20211104:182012.446762:+0000',
                                                                            '20211104:182012.463185:+0000',
                                                                            '20211104:182012.479918:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˑ˕ԩĜіțǓ\x8d˺ʛӅǈԒШ˽\u0380ɋΠ=\x8fɵΠĿԄҳΈʄʤϬF',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ҨƇ¼ђӠцȕό¡HϘѵàúϋ˃ŒџĶöȪ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -87410.39490348942,
                                                    },
                                    },
                            {
                                        'name': 'ӢëʌſŏзƙǕ\u0381¹{ԩҊθǺþɬӰʹБћȃâ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɖˋÞƦY@ȍ`ӥŎxԆԔӎΝѫ,ƆӎʥҼeǸ˘еɆӈóñќ',
                                                    },
                                    },
                            {
                                        'name': 'ӝЫȢφķҟϗΗȧƉǚ\x9aΨɈ˽\u0382ċʉÖ˃ŐӐǾηʥŚŘОӥƎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 340868.7861389269,
                                                    },
                                    },
                            {
                                        'name': 'ΘԋҭΈÙÄ\x96С\x8f',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɡʢÌ˂',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'фӱ×ŞƷ:ȁȣЯʞ\x92ӦɤɘɓΛӅ,ɕЃèӕӦҥƂɎӮßԦǹ',
                                                                            '`ԘƅŞˀͺȼӫŏoԔÊw^\u0381FƠɡӓнÂśǁςĎ˘KL˓ɣ',
                                                                            "˰ϱϿԞćҢҐĄ{6ҝƛþʞũˑЀǔȤȣ'͵ɘɫƆϱùЌaô",
                                                                            'Ɠþ8óͲɁʖӁʑ˲ý\u038bўøМДђƹĻʦɿeúɿ{G_ԉøȵ',
                                                                            'Ϊņƃћ!BɲɦȞɵ˯ΌҨ°Ғʣvǎ9Ȍˤ;Ɔ6Ť϶ɗєʧŰ',
                                                                            'ƺ¬ĕµʏНĉȦћǴôïĐʽÚҀѥƒΧͺɳԁў\u0378ÓɽǤѧɀͺ',
                                                                            'Đcɝǘğ·ɷˍɁ҆ɖԭŤƺȖԓŧŲёϪЭκаΑ<ˡѧɫʔь',
                                                                            'ĥƸ&ˆФӫɞĵЎх¤Ņџԇ[ѣRӂϊXόΣˌ,өӄǶѦżӚ',
                                                                            'ѢŷǅŴŠҎНɴμΥ]ыMĂʣϮӗѸξʽ^ǢѕÒӻŝԑǪēƒ',
                                                                            'ǈΌΈĒάπƺǦγЀ;щzҔ˱ŅĻҘѮӨӷӿǅĔԭʑƢōņȽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˤѭҢ@Ŝvӱ˱ɔƪӞėȉʯ\x9cȕSÞŌjȾ˂ȽÄϦңșĜзʏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǥͺ$şYćЙΠˬ˂¾ƫӘğѤӀ¢Cǒе˔\x881ǉä²\x82GЇí',
                                                    },
                                    },
                            {
                                        'name': 'áǯƺˇƩƊǮʴÝɠоʟ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182013.615400:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǊӘŚ˱~ѹҰˮÌŪЋȬΌɐǸŏ\x88ӳ\x89ҁƐԥυԮΓǿˉ\x99 (',
                    'message': 'ĆȚҥ˳ƹʎ΅ˈǱ{ŨȗȚʙҋǽëѽR\x96ŪǚȤд@ĝĂǋѢɔ',
                    'arguments': [
                            {
                                        'name': 'ʪɲʲҚϫͷѡƏŚΎƟʵʓ$;Ѽ(ѕƊǩHșĘäбpχːșJ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8005390824033195634,
                                                                            6432858105370817637,
                                                                            -6387228934796166786,
                                                                            -3858850569090014300,
                                                                            6233484152672666551,
                                                                            -4470875637366285192,
                                                                            -133125842512290548,
                                                                            4146239999622589232,
                                                                            -7385606644236150082,
                                                                            -3322835118082788559,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ª©¢ҝȔǰʦ¤I',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 905860.4112037969,
                                                    },
                                    },
                            {
                                        'name': 'ҾǼïʶQӓëΐɼ6άɷȮӞΩŀŏЧԈҬɠҾ\x87Ŵϕ\x9f"ˈƪƊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182014.076768:+0000',
                                                                            '20211104:182014.093476:+0000',
                                                                            '20211104:182014.118142:+0000',
                                                                            '20211104:182014.134325:+0000',
                                                                            '20211104:182014.151056:+0000',
                                                                            '20211104:182014.167356:+0000',
                                                                            '20211104:182014.183760:+0000',
                                                                            '20211104:182014.202216:+0000',
                                                                            '20211104:182014.219729:+0000',
                                                                            '20211104:182014.236701:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϗ˧Ǧ˭ʍǪғɆѥЎ\x87¦Ů\xa0ͿҟϖϿŨ¹Ӥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -641467115300925113,
                                                    },
                                    },
                            {
                                        'name': 'ƃɼсǶϪ°ҳ¸ҭгѥ˒\x91ǔ\x82ϒƞѕÑΞӡϗiϦϙȔӏǫ\x85Ԣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            825439.5070628847,
                                                                            906129.8956321378,
                                                                            345250.1511518006,
                                                                            199013.94067380816,
                                                                            925932.0976398947,
                                                                            568279.0286641825,
                                                                            935913.7703714359,
                                                                            915040.1086058004,
                                                                            286192.12475978996,
                                                                            412474.8560330388,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɱĥĻɚӷΙ\x9fЄ\x8cȲñʊƳѺЗӇУũνˈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҹмļʔȴ4Űɯє΄þǘϮ\x9aкѨμέXĠkǱ;¡Ϟчѥ*ˁ҄',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182014.714618:+0000',
                                                                            '20211104:182014.731495:+0000',
                                                                            '20211104:182014.748372:+0000',
                                                                            '20211104:182014.765353:+0000',
                                                                            '20211104:182014.782046:+0000',
                                                                            '20211104:182014.798714:+0000',
                                                                            '20211104:182014.816657:+0000',
                                                                            '20211104:182014.836575:+0000',
                                                                            '20211104:182014.853780:+0000',
                                                                            '20211104:182014.870927:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'К(',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 488489.5649737001,
                                                    },
                                    },
                            {
                                        'name': 'ЁԊ˶ǀƗѿƍΚԁɲҕŐϯɧŒ\x93ʝɳ£ʼǭЎʌԨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182015.028290:+0000',
                                                                            '20211104:182015.045577:+0000',
                                                                            '20211104:182015.063776:+0000',
                                                                            '20211104:182015.081684:+0000',
                                                                            '20211104:182015.098830:+0000',
                                                                            '20211104:182015.117474:+0000',
                                                                            '20211104:182015.142604:+0000',
                                                                            '20211104:182015.163769:+0000',
                                                                            '20211104:182015.184224:+0000',
                                                                            '20211104:182015.205095:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˮȫǷȯхҘƈԬҼҍƓӉ;ҋȞΟŃ˖\x85˕АϿǸϏ˘øѴʈǚ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9036751312200484319,
                                                                            -1599386008846945970,
                                                                            -4126636215366744392,
                                                                            9027516898586373074,
                                                                            1167894823767677838,
                                                                            -8102432640415683637,
                                                                            1010942045367029129,
                                                                            -7369795882613114114,
                                                                            -12237347218981552,
                                                                            7061075820632802335,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '҈ßҮКϼ˖аϒЛǺ\x9dɾЗ\x97GĥƎόόǠʈŭӠԂŉҴϒƌЂ˚',
                    'message': 'әɸƹŖӃӊҍ˹ÒӧåʔCƲ\x8cѵƺɹăƆÑɩŘ\x8fЄǕβϵуӾ',
                    'arguments': [
                            {
                                        'name': 'ϻҘӥ\x93ŧȐƺãϳȇ%>ɟчƓӎцƧʻԇ_ɡŕ+òý]Ԟ$Ķ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʏ҈ԗ\x99Káč|ɂ(ϾɫǂGӬΗТǅǊҍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ð¾\x92Ԑń˛FҠΞϭÑқȗÜñþϛƙг˄μ"ʎ²ҧиκ˞˓ǻ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182015.898630:+0000',
                                                                            '20211104:182015.915801:+0000',
                                                                            '20211104:182015.932243:+0000',
                                                                            '20211104:182015.948774:+0000',
                                                                            '20211104:182015.966888:+0000',
                                                                            '20211104:182015.984808:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΙΜϏ\x8bØǆϐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'В¶~Ƹ\x93ɐƖнуˉҫɆƔźӄϤԒʴҊҵøΰЯӻҔǨʌӛΩӟ',
                                                    },
                                    },
                            {
                                        'name': 'Ŏ¼Β\xad\x84ǁӏǡЌŗhԦ҆Ðȸѷř¬ƴӝФ¾ŮȺÈÔǃǞʕ-',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            914928.8753657135,
                                                                            106916.53212472994,
                                                                            571457.9900273428,
                                                                            225501.90389144793,
                                                                            260127.9960719556,
                                                                            438159.1658798442,
                                                                            91773.78451986136,
                                                                            835368.9385949695,
                                                                            27925.152227142244,
                                                                            252294.86331939063,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʥѓĽԅΨų',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -889232318248834284,
                                                                            381520570183447086,
                                                                            3134086922406080730,
                                                                            3961044876962510058,
                                                                            269901068236609233,
                                                                            -940088408635968787,
                                                                            407838098982402089,
                                                                            3244549832713195589,
                                                                            418116572347708334,
                                                                            -8493725307137748238,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЯˮϹRŹϞſЏԡқʁҠɤq\x8dοғɠȯԐQǙƒи˾҈ʘİ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182016.617016:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʓȧѸҵͳӳвƱĴˮ\x99РŕӦӿҤѯ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 402549.3284455665,
                                                    },
                                    },
                            {
                                        'name': 'Πе˲А5˯\u0378ŽѕȍQӨĖWԕÀѶ/Ǔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8682015641813324222,
                                                                            -5982432864319220460,
                                                                            6061556896582682913,
                                                                            -5668493589317548309,
                                                                            4097337874574960293,
                                                                            2153199075150932384,
                                                                            -2819336817772925575,
                                                                            4506038845662639630,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѓȐ¥ȑҽĄ+ӴŷƜ\x93ĿǍʱǔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182016.985826:+0000',
                                                                            '20211104:182017.003723:+0000',
                                                                            '20211104:182017.020566:+0000',
                                                                            '20211104:182017.037693:+0000',
                                                                            '20211104:182017.054634:+0000',
                                                                            '20211104:182017.073022:+0000',
                                                                            '20211104:182017.090118:+0000',
                                                                            '20211104:182017.107083:+0000',
                                                                            '20211104:182017.124183:+0000',
                                                                            '20211104:182017.141156:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˻хƉӳϨһӐŬƋ\x85ĸĸŉʳʥϒƯЈϲéþΥЫɴќÌǑ\x8eӧЌ',
                    'message': 'Ѕ҂Рʨ\x88¯Ç"¢ϪҦȳ9ѺѻӹǓ϶ƗҺʹ¡ɆŞÎӲɌ˝ŧȶ',
                    'arguments': [
                            {
                                        'name': 'ҘūчÇԣԛȮĄł',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ū\u03a2ΫϐӧÏɍóǀʥƇŇ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '=˩ʆAԨЩXѫC˟ԭϛǚɌʿΪŏУȜĉʯĩȮџßPǼГĽͶ',
                                                    },
                                    },
                            {
                                        'name': 'ȡӱ!Ϳӏȿ˒uƝƋ˅ЕӢȌОΜʑ΄ӒΥʍΞlӎēӅʏɨιȮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ґɈĈǞӰͶʘʍʯęϩԑ¡Ȏ\x89ŹΒʘԈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8677525780134705340,
                                                    },
                                    },
                            {
                                        'name': 'ϩҔЇ˨ҁҿҏʊȬҊƬ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʌҕğϸԈҶӬØ:',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǴǍʞϸ"˳ĪϤȳˆιӹɳɀˏ˦ťԍӬɌΛøȬĭТϝź½ɝƣ',
                                                    },
                                    },
                            {
                                        'name': 'ʹҘǕƼ/ŝɔŸˎƛΆƠƢʂҹ\x85ȏӊƭ¦Е9ɝ9θԃϦĮЩϵ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Гѣ·\x95ɚĦӦΥƢʂΘҎ£ќСίм\u0379Ҡ\u0381śİ˧˥ϘѮϪƿ˄ː',
                                                    },
                                    },
                            {
                                        'name': 'ÀΓiˡǔɎ5Ʉʹ˳ѝѿҴѝΈåйʘ\x83',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7767986011347803144,
                                                    },
                                    },
                            {
                                        'name': 'ư҅"˱įɰΝΤДƢ҅ӏʝÔƜγΧн',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182018.065572:+0000',
                                                                            '20211104:182018.083541:+0000',
                                                                            '20211104:182018.101378:+0000',
                                                                            '20211104:182018.118237:+0000',
                                                                            '20211104:182018.135014:+0000',
                                                                            '20211104:182018.152094:+0000',
                                                                            '20211104:182018.168954:+0000',
                                                                            '20211104:182018.185641:+0000',
                                                                            '20211104:182018.203087:+0000',
                                                                            '20211104:182018.220024:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΒӍĊιʫЎѢӺ\x94өӲĨķҜ¾ӎӠ¾ǃ{Ĳыϯ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            568646.1119147107,
                                                                            971160.6396387119,
                                                                            718562.3234601193,
                                                                            989463.7374971248,
                                                                            220142.7788348248,
                                                                            -94626.06542711772,
                                                                            583715.195568902,
                                                                            679757.3653470563,
                                                                            227072.44971271226,
                                                                            23621.39961026034,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ұɢ4ſǟОŽˑɕԘ1ˀȺʶ{ȿɦԃаʣ4ҍӛΓҡÉƎLØĀ',
                    'message': '>ʶɹ\x96ԕϓ¡ʦŜș§BʨʘǍӽА¹ƝǱȕǂҷșϲł"ͿȕƟ',
                    'arguments': [
                            {
                                        'name': 'Ę5Ύ§ŃʬҁОϷ+ɨϿҫĆôˑύɵĴǐĭϮ³úԜŷ˜˷ͻÃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182018.617854:+0000',
                                                                            '20211104:182018.634608:+0000',
                                                                            '20211104:182018.652301:+0000',
                                                                            '20211104:182018.672060:+0000',
                                                                            '20211104:182018.688693:+0000',
                                                                            '20211104:182018.705155:+0000',
                                                                            '20211104:182018.721698:+0000',
                                                                            '20211104:182018.737999:+0000',
                                                                            '20211104:182018.754217:+0000',
                                                                            '20211104:182018.770822:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0382ԇ*РҏƮԖ҇˃ĵɹĽƏÉϐϰʦƬˆԈЩĻГʭӤԓГư',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182018.863273:+0000',
                                                    },
                                    },
                            {
                                        'name': 'дȊê҂Ԧθ?ϡʢΐ˩ƛ§ơаĔĝZΘ[r¼ϬӒǱ¡',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                            {
                                        'name': 'ċ¼¿Ԟ\x88ƘА®ÂҩȖ×ӖƼґҞÔ҃іňȊӭȑϽеȌчØ³ȃ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5635941005276166087,
                                                                            8396868813547791550,
                                                                            -4984703836269141069,
                                                                            4805416006663552670,
                                                                            -7322472433375455742,
                                                                            8055875815820442200,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȻƈʋҸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6581764666417110477,
                                                    },
                                    },
                            {
                                        'name': 'ĜҝѽΧɿœƫʛďĸăԢǲԪ\xa0ȡєҍԠl\u0381ӓȤŹÕÁӵƀʜ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 371754.9974540787,
                                                    },
                                    },
                            {
                                        'name': 'ŬӯŧYӱ÷zγ«ϛҚĭÞƒ]ЄЩԑiàŋćΧøȈɚļȯΧМ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1964086500384076897,
                                                    },
                                    },
                            {
                                        'name': 'ӐÛŜŃϗϟōǨǇÌѢϚҎЅс˾ʿ˱ĭСŽēuȨɔѩͽț\x82ӊ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЯЎϷӢҽпžҘϜƻýΎÖ«ԢÆɚЬэʸӒЍĻǏˁҿŖÙĬп',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 188748.91491256212,
                                                    },
                                    },
                            {
                                        'name': 'ǣтХ\x83ȴ\x9c`ДªԊԌmÀfͿƐŷцˡţŧÞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˩Ȏϡҙ˺ŞɑıԤÊӧѳȎМȉҕԁÂȼГҀνё\x89ѵҭЪ˘\x9eX',
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

            'identifier': 'ǩǇӢȆț',

            'categories': [
                'file',
            ],

            'messages': [
                {
                    'catalog': 'æл',
                    'message': 'Ϟ',
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
            'name': 'ǫBͷ˪ÝˠʷћƏƘŊŌӇſJсɃd˺ɛВ˵´ϙҜӇˤ˶ƪɹ',
            'error': {
                'identifier': 'ņуӳ\x84ż˙Ұ\x80Ë˸IǏυǦ\u038bɉ#;&ҙɞϜ¾һάɠɶηDԇ',
                'categories': [
                    'network',
                    'internal',
                    'file',
                    'file',
                    'access-restriction',
                    'file',
                    'network',
                    'file',
                    'access-restriction',
                    'access-restriction',
                ],
                'source': 'и˛УĹӚ&,ŷɈŹϛɡԩɫíĺͲɂӯʶ»˶Ƒȷϸʣƽ1Ҷѵ',
                'messages': [
                    {
                            'catalog': 'mӞ\xa0ԅѐϻȆļǱʡɤîѬќк+ϳцтЎӶʳԗ˗ºҁŖʼʵ\x86',
                            'message': 'íΫˁǅĆǘɳĹûɟņԏĪѥŶŔʮĖͺЌȇӪΦыʸͶƙӢŨӯ',
                            'arguments': [
                                        {
                                                        'name': 'ͷϱ³',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '}/ɪюЎ8öЍÜӼҵǕɐѦͻԊÓ˩ĻΧˡѴ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȿŸʎą\x89ĢЫ˄\u038dÓӡɝɨ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЄԦЃˎ¡TlΫđ˚¹tϰƯӾɤǳѻȶҝӸ\u0382ɋҔÈȔˉéӴГ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u0378˥Čȿȏҡº˓˻Ĵ®ӥϔʸƁsΏĭϕѩˤàƭӴŹǍɐ¿ˑǃ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x98ˣфȗɑ¦҂ұЖɨТÀΏ\x86ŃԟŧKԂųǇȤɼͻˎΎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ңϊĄɉЍyӮόϘˉχѐŭ(ÙʃĈˀ#ӪȤʟʇɢƸҐԃЁƮϨ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԌоͽнРѶ\xad¬˪ũ˽ϣŗШ˅öƻǎ/ҳŞƟӬľɝǩӬκҨƬ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɋɦƍБӛΚʩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǲԆʉϜλ],\x99Þ-хКþҙэԠ҄ɤɌ\u0378ʖʶżǞǏCЍaӃ˼',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƀ\x8fҽԕʳΫǐĕű\x88нǎƾѺИиϩĵʖ\u038dщϔӕɠӂˬӫȸʛѶ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ӹĴδƀƴÞ'҄ѹÉ\u0383Ž¹âě˧ѣέŢɿBУþºϜΆϵңшɥ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʋƓӠƁÁԜȨψˌϮóƞɂђƈӃĤԫŴåɷĵÃӢͿȢɦӌ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -28070.38306255867,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'фȚźˢĀӯʽϮϭ˲ϩël\u038dǉЉCώx˞Ѽǟȴ\x81Ҩ\xadԜҜˮʥ',
                            'message': 'Ⱥ¨ΧЖчƯ³дӒˇΒâĈƘϋèϴFΜ\x9cȧȇϛыŦːˍúɒ҆',
                            'arguments': [
                                        {
                                                        'name': 'ЂѷѨbȰİŀjҰПшç϶ӏ҈ƓÁϿĴОӆӉpɩêǶӏʙǡŽ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 226348.72629427694,
                                                                        },
                                                    },
                                        {
                                                        'name': '˛эɭԑͷŲӴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Мӌ&ȄҨƙнΊǣǚǱů˘Ǒҷ\x7f6βвґƖεƨȂҍҰİԩţå',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˗ӞĕʥǕˠԦΤ˧ʟƅ©ʐĢԖѢЮ7ӿ\u0382àơRԆÎɟS=Һò',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 291455.8728258637,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʎpçςкȖƳҚĳ!ЯˈВӿʸøąƜŢσɈÕҖȕɗɼӠȍȉѢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϋ%ĥƽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹɮФҭ\x8cԣʜϕ\x94ɸƤưEɯϵΌ\x80҆6>ćʚ҃ŭȫԎʸ"\x90Ԧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181958.299189:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'шɞҎӘǪԨͷѿȍҊ{ˬOǦӆϽǄʎɰtӃӪǜӃșŷҤȍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɰ\x8cįϧşǞƠкԧςSǈȅԩnÕFМ˭ĈŭǔȢҙ\x95ӂ}_˰ŋ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '&@\x9cˎɹāԘ/ЮˁxǻÓʎυǐʹȝҔԡãʙʖǬÈĥϥŐήä',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181958.523872:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʝϫʞАȼʑйЈӊǵԊЭȱµęӬR\x8cYһθȧОӐ҄ѺѶУεР',
                            'message': '©в\u0379\x83ϑȸŘϗрˋΤǁžӎԡԡǍȸƞƸĶʢɼҕϭ\x98ǥȭŗϗ',
                            'arguments': [
                                        {
                                                        'name': 'Ԧ,ϕӈңѴԧԖȆ˖ӷҵҵƾňϮìǫʹ×\u0383ʅфȟѪɈŃƎИȽ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƨġȯιĺӈVϖƎɏ)ÑԌΦĥĚԥуԙ»ҶѢȌю4Ɍњŧϭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƚЪŢ˚ˑƬrϧ¸ɾǡѧәӆӕӷķҫÚȰv',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɻёә˄Ȭʪ.ă\x97\xa0BęӠӉEɧˈʓȟԐǢ\x8cЪµӀǈҡʷÃͿ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ºȜԢԚʊЩā\\ʛͲĤΎÒĈĺҽӻӊĈ\u03a2ǣşǅʧ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'åķÙЈцΠŎȴƕԮ"ʙāшӼǾ|pѥʦΈǥǧ®ƢХǭԄδĭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ПėХћŐɔƨӍ˝Ìΰê\x96Çɍʣ\x91ϗɷЏƮǔŀ°ғ÷ϱԡ\x97ˬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'êҍͷ!ɀ\x999Çϯ\x8döàǖ˯ҠͰƏїͺǧЁƆͽɵϮџ\x9dʰöњ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'LŦ˥Ƹʎ8ӜöӊǔϷѫʫΜͲŁӚŦSǳ¤ɔ˴Ƽ0ƤŌįƱȓ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 2399.2047249486204,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǵ±ȋÚ±ϤΊUǹŲȩЀңƓҿ˪ъƭ·ʁäȟƠūϷөʗαĿɇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȳǁ҇ĩҔ҉pιѻӋ-ҀԠǯНа',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8204294630737290361,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǰγů°ЍǥƩĚƩkҖϼϬ˧рɮ\x87ѹɁΈђѤ3εƦȳɢԊ\xa0j',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 73562.48473128083,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'αüȧŎɽȮʜӬȬӣɗН˹˳¤іЭǽʑɸ\x8f0&±σƟË¥ʘɊ',
                            'message': 'ς©ʀϊȝƬƂm=ɾѠƴŔʀҘҏuƶԋРΒĎȸȍăͳΊgƱʅ',
                            'arguments': [
                                        {
                                                        'name': '\x9dӶΧϐÚɸѺΕȦѐİЫýϪКϪƛҡӶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŭɷӜğĸ\u0383',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǚ\x9aǘĻ\u0382ѤǎͲßʹ±˧ƕҴŃӮȌÇɨƸʞ˄ðɞǗы΄җ?¨',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϙĹɃĉČǟĶ¸Κ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1403865637113226542,
                                                                        },
                                                    },
                                        {
                                                        'name': 'MɪÀÆȑЖğΘԀȖɍůr',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x7fƒůΆӮιɮͷƓԭӮξŲšäÝҨüҿȇΑԬČҕŰѺѠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': ']ɍǵѤě£Ӕǃ\u03a2bɭƧȃȲԌˊĺͲȢ˄ɛ\u0382ĄϏӳĹGȝϔƐ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƞŽɪ˖vɔĘũ\x88\x8eфƿg6³οÎʇVͽŎ¢ĉƖЁ\u038dĚоңг',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 105670.61526100276,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĂƧȁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 214109.81360213,
                                                                        },
                                                    },
                                        {
                                                        'name': 'уi˄VüÎ˹ÉȔ¤ҿĭǫƷĲ˺\x93«ȍ\u0378ƼԍйŊҠѐЇeû',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 555114.1205577664,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǳΎĖαǄ¼ŀʵȼΓƫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'É:οΐƴɴӕЖǴϚǾϓίѵȨkʥӚʹÁɲ˰ҘĹ\x8dà˔řѴԙ',
                            'message': 'ßœɆ\u0383ǧпҨ\x96Ƙʄ:ǆǑнеŹԙȖͼɻТȡđЋԉǊБøɋ1',
                            'arguments': [
                                        {
                                                        'name': 'ƉɀƘkƩȘ5ưқΒӮŲɺξǠĻƎɅԧҊȪӼԣǸÈЁűɚʲ˕',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉӻÝѥЍϭ¹Ζί',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '?ǢέƄӟĆ˭ʩҔщԓѼˈ˖\x97Ƕ+ĝʖɢ˔\u0380ǺǵȾԍ\u0381ƆɽƬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԓɝΫ˴EǓʽƸɬҺςȸȐӽʡ¹ʢѼ˵ɡĦϬӢȮʮҽεɝȇ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182000.427082:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĴʪòȌρȀȓɻʡ;҅ŚÌų',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ұΨ˱\x8eʄǀʏƥι®ˆЮЇˮ˕²üȖĩ$ªʽΏòьɅʧɳΜʧ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʌ¦ƪ¢Ё',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8740323392828796391,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ːԣļӅѮ×ˤƗʯǉѾԘǦxѾ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 408997.6680575859,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɵ\\ɰjʄи҉ĘҺãѢ҇лμÌ˭ŉңψƂʒӈʬ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5106895651457239471,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ġѴċ=®ɬɧӹȦ\u03a2Ӷɩ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8072965314376897809,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɋéѸǭŝЭԓǠζΐΡҴϛÅȢΨƳƙ˯ԏɵÏ¢ŞʓŕʖɫːϪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɫʻÒƠ\x91Ǚe\x88ƚΈđѷΉϛЬȻĬKͺеҒСҩ´ςcɉ[˺Δ',
                            'message': 'ƈĩԖǟɁԞjӦ®ФѰˡѱзżŴŨӡϞ1Ͽѻԝ\x80ԝÅåЀȥɈ',
                            'arguments': [
                                        {
                                                        'name': '÷оӟӢҳĩǼƯ3ŘʟPǥ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Őз˩ǵҔ[ͶͼţËȟрґȡ˙гăϫΆɯİėİ\x88«îѬЛϖӏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˾ѡēȚɳɀȢɏęИҡĥЫÕҠϫ)ʥΐ˛˃ǶʫǧӮǸԥӊʞĵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1503330274240470638,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟƆӣΖ¨ō˓ӤАͻ×\u0380ѽǡĠԞҠҡǶѪΤǣǋȂ·Ġ˦¤ɋӎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 405866.967918058,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļӊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӱԚʥƚǋтǬJĹΛÇœń',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ðͲ\x98Èͼǟ¨ϓǧˍƊɻˁĈˍӠέԌÔƇɃяӖн˹пɺǁ×+',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĽЦ΅ҏўϭɕʠ˨ӥMЃɽɬm,ϖȡҙE˞ƞƠЬǪxÃ˭ƀІ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '°àӜӢ˞Ͳ¾ȥϕ°\x84QɆ\u0383ʞΨ˚ԙǊğˮЁŜíóŜƹʤ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'YԞȺǴҕ\x8dѫǜй҄Ӛ˥ƶкϨά',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӸǐũӢΫρťιҬѭ0ЭìǊN¯Ʃӽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȘќƂȢκӦ˅ќÃ˔ϿӔ\x97·ψд˾ȎѴʀԛҀļß¡НĵʯΈˈ',
                            'message': '!ъӠčҕ\x9bŚìӧȋŽДǁІęΪŚЌįҀqĿĬ´¼Èӄɻ$Ј',
                            'arguments': [
                                        {
                                                        'name': 'иг5ҹϘĴϘ:ŕ>ƳԈИҥoÂӟӌƝɅύğȿζ˚ìәҧ=B',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ']ҡȡOʔȳȘßԕɠɞfҚѷ\x90ѺǠΗюЌƕƴƠƽǸř˒FǬJ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '´\x87ˏˎĢɻäϒǏʈƔÉћ5ɰΖqĥΌȹǫǆȺҪ¶ŋϠ3Åv',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϝЛƟƚπȈѺνǃӎͷҍ˨ʔθ0ϼϙªɑϑԬѺӲʜϝ½λ˱Ò',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĘƠҋӖԫËƮ˂ϭːǡ˙ӠӄΰȠŮβƎҕҒ#țɾ҂¿½ÁƥƉ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļˊʌіοґºԞφȕĊϣ\u0380ԨϘӪ˵āʐÏʘπСɏȿǬǖʞҕω',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǾŌδȐȣѣɎҨəѷ\x8a¤ЬOь_ΚĲ\x80ԨΖ˹\x98УʹϦȲѹʵŏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƱYΐρ¹ͳӚɐļɳӠʜ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÏҽȻûѴԪʌŞǚʸĢєчɼĿ^ϏK˸âϴȶЫëđƥʨӑBԓ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182002.200275:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɥƕǱ҄ϤǢʿѓǅ˱ˀǪɡƚɡӷͰƌǅņӒѹˇʶɚɥŭˑ©ȴ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϓö\xa0éǞѰʠϒωǥϨ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'eɆюπƯǬʉƥȍ6%ȌÚўƓͺʦǒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŷƘ^ѕȳ˓СŘ^Ł\x8aƝòɥҮ˰ĝӝűªʒơЩҙъҏȯǔϑç',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '9ɴӬŘӷÞϨЃӷ˶ԩǧòŊБĭĂˬӛÞĜΈŧф˻đύϧ;x',
                            'message': 'ˊƟȍ6Ӈ˾ʭҹйŘãԆҔTû҂Ƭ¯Ǥŗ˼¾"ԮɞőİбԪћ',
                            'arguments': [
                                        {
                                                        'name': 'ÿѭōáԄМȷԀ˾˃ǀǼ˦ԧlȞșŊрэƫ˫Ʌѥҧɪüŧǐϟ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϡˇ˧ĠƯȡʻʘѦԫВǨŻΒɈ˪ӉŚӭ+ĆɻϙөȬԁʽ˂ɳ[',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8625979428005348242,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽӎſϾŜȍéyϱϤ:ͳмǏ¨\x9aǻ˼ƚ\xa0ԬѲАȞƨҠɟm\x8dŁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˏΝβĝӻɠԦрÖрƳƖǢȨïɆςɫҎҾɇAϱ\x83\x94˯ѓҔªŰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 155900.9553689209,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѭǘЏЎǘϿ˻_ϦǶʰШԃ\x82ȚϖƭΪņ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 836447.5128978129,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԝϰҴːƫ5ԏǧͿɏԚʇƦϐĖʷʭćХ˸ДΐŗeѨƕӢφӾã',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Φˇʔ˓ӊԅҁǑцʫчąʱǧйĺˇȤӁƹnɟ\x97Ύȋ@^ӌͽ˼',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ň¡ʕӺɠXƹόôȇƒϠҲ¥ƉȜˎˠʓʜΥ¨Ƨӷ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182003.057523:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͷȟ~ŵƼɵєͽü',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'řĽԛӯ§ӺҩĈЈʓȢɛαɺȢ\x96ƿ#ʑ҇οĨΜʰʔͳŻ»ͷΜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182003.192502:+0000',
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

            'name': 'ӕёɐ',

            'error': {
                'identifier': '~ȯӻҦΏ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ηa',
                            'message': 'ϊ',
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
            'event_id': 'ԣ\x810Ѭ_ˆ+ЎԂɮƏѰҸlϢWď\x87ɨȤ͵˲ԏбƉ+ˑűԟϬ',
            'target_id': 'ĩ҈#\u0381Ŭ}Ð7ӝ%è[ȋǖ?ɢʍҽŸǏӺNʃԖĺο6ϭҖ"',
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
                    'event_id': 'ªɠǦϏѮɆĹȣӸƝӝcѲȪπϏȦμӺԇˀǏ\x96κNɌćˬǿp',
                    'target_id': 'ԜÊґ¤ˈɛǚКĊʌϩìϢȐҨԅТɥЅĘςĤΈƐэʣˁʡǟȸ',
                },
                {
                    'event_id': 'ɟţŴŪѺìϒпʠǭ\x80ъȄČ\x877ʹ\x89ăýʏпĠ˖Ǻ\x9f×ʺηӦ',
                    'target_id': 'ɬȥ҅Сф¦ϷІƀϬϧŰӾˣGƛ˷ԫʾ¶OƚӁţÕ˄ȇ&άő',
                },
                {
                    'event_id': 'ԛНǑӶЎaʧϺЉ',
                    'target_id': 'ΥͱĪĂѫǫΙˉƁԤƠƿƚΎ\u0378˭ӽΎЙ\x7fПҐ {ͼξ\x95иϲŝ',
                },
                {
                    'event_id': 'ːȗЛŏƘčƏƷk˵ʕʮεҰPEƇöȐ˃ȣʕɏÔɪ4љĲǾ{',
                    'target_id': 'ˤŇˍŃзԢǟPbԩӷʐjѮÓȹ΄ƅωҮЕʁ˪P\x96ơǌǍҒҪ',
                },
                {
                    'event_id': '\x82ŴEŎӵϹɹȝĺİҜ\xadґөʧȗɪȂпԍ\xa0[θòӻŴƍˢˉʴ',
                    'target_id': 'ϊξΡ_-ԆԠ\x88ķїѮ¸ϡ\u0383ΦϼȌķЃéԉί\x8fwHǍЦɫ`Ƨ',
                },
                {
                    'event_id': 'Żšʘϥ\x93ġ΅ǳ˱ɠĄĪ˽ĕBʋѫƆŷ\x9bҚɚчғÆʁŌeʏƜ',
                    'target_id': 'ҿ¡ΦƍӋûѝƪӳɃĹÖćơôԤÇõúԂӭҸ÷ҼȠөЮӚϐɽ',
                },
                {
                    'event_id': 'хӂͼ½Мɉ҇˕ԉɝQә{ƐʑҢΐɏԤµΘƝѼÍ\x83\x86\u0381ěkĴ',
                    'target_id': 'ДӟΚŇʇ÷ŬτӛÛēͱʾҜĐɟɫǖśүȕнҍĄǼùÝ΅3ç',
                },
                {
                    'event_id': 'Ҥгͷʥӏ)ȏ´śʎüʀҷΌǠɬQĝõêѭӟѿīΠѱƳϠ\x90h',
                    'target_id': 'ϟȃˑϟƉΣİêŌ҇ҙчɩυˣ_ΓɐǾ4οѸԐ ƼŶʯÓƚԎ',
                },
                {
                    'event_id': 'ǮΐϳȅЕȴŘΎ?ʕЦʄ\u0383҄Ǫ¬ʏԝˡӅ*˪ΣҲ\x94ƀķǻÆŇ',
                    'target_id': 'ˋȃˊεƷǀҿɂsҞ\x9dȦƒ˙ǦȂЕӧ\\ļЮϤbƒġá\u0379ĿӿҖ',
                },
                {
                    'event_id': 'οǎƫӣԟ©ŞѰMϥ¡ǅϲЁҧґѳΆɍˢяƚɸ§Qȴʱéґc',
                    'target_id': 'JȈǶɽǳʻǧŔӍ˼pǪʞǋɣʓοȻСɯ\x8ceӪˣƭ˔ɘǎä9',
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
                    'event_id': 'ӥάӥȻ/ΥȫǤԒЦ\x8aăšƚ˱мś^ǰ\u0379Ȁ2кʴԃ˘ǣ\x99\x85Þ',
                    'target_id': 'ӁȒÀːпɩҷ_ȮĠŲĶăȩʐʔџԁʛƂҭγΩӁùԎŘűюƆ',
                },
                {
                    'event_id': 'ѽQЍƿ\x8dʽҊǴӱB˙ŤˍΏɎѲήúϼКǋțРϘŌΡxTӅѣ',
                    'target_id': 'ƴ˅0ӘÏшǈ˚ϛſ˺ɊѯũƤřŝԣǫͺƜƠϒ-єѼkӝѶˋ',
                },
                {
                    'event_id': "Ǯ'ŤѭвχʂǄkOǴћʣ\x95҈ϮΓϹϿϹɏÖ˯Ȁʐμĝøůǘ",
                    'target_id': 'ѨęƻҼȐȥɋӸľ',
                },
                {
                    'event_id': 'ӧOә͵+øĉ!Ō´ȌšA°ʧʝλǿҔУʐ΄аƾҷŖϋ¹ƩÑ',
                    'target_id': 'ǔ|ІŏȍȟʀʸѵATϠȤҩĦӪģ˺҉5ʬhǬѨǊѲĎүơҬ',
                },
                {
                    'event_id': 'ӊҢƊŪ˥ˤǚ\u0381¥ДɉϨȦҩҷʮӫ¶Ԍ5ϝίǑ%˛ҰjҒͻȒ',
                    'target_id': '\x85ӛτý ƏȺMӔх6үϺʹ6ϸҿˑÝƁѫɚŠǚȰҘҭҝĵϩ',
                },
                {
                    'event_id': 'ʛɺԛÃ³ƺδ\u0383ƕȰӼǈӘҢˋԖеĚ˔Œʱ˗\x94ŌɒüɄòňϬ',
                    'target_id': 'MǼԈ҉ÕϱÜ˭;ȯԖȉΥƷǜˋ\x9d·ɺǏǵʚȹ҇õѳȝ\x99ǧ˅',
                },
                {
                    'event_id': 'ϊʹ\x8fsWȨӅǼŘ˓ŦɞҵЯѱǼӣʚ\u0381ěΠǺӥcҺȒӟǬВˏ',
                    'target_id': 'ʋ(ѾȅЏŖԌкʃÏȪЯƼȏʝӀҴïԇɭĽǯÚӘʻΊ҄ʰ\x82О',
                },
                {
                    'event_id': 'ɋʪIĝļД\\ȵËĳƕϖԡôϼƲ¬ŷǑXțʄɕƇɍƷϫìġϛ',
                    'target_id': '˅ƏвƿҶĄ7҄ѫԥѦĮ;\x8fӗùėяŘłγЙѢƛɋéKͳ¶ӭ',
                },
                {
                    'event_id': 'ԍn!·ΙǙƒӵƞГӦ˺©ӱЕʥɥϏ҈ưʁʮƲƶϙѰӶƨˡ˾',
                    'target_id': 'Ĥǃϳ˟ӿƮҘ˗ɩφӡ¬ˑÔƲѢřŵʠ˟ô7ϟºˊǋԚƊПԄ',
                },
                {
                    'event_id': 'ÓƑϻӺÏΤȼʗӭъм҂»ʉɳɓ\x8eĝԪĚ©λΏɰǢҒ\x93϶Źѷ',
                    'target_id': "Ϊђπ°ƳkүBοƊ\x88оͲɄϩ'ʆ\u03a2Εώıȿџ¹ǀ˚ƍȋȕ1",
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
