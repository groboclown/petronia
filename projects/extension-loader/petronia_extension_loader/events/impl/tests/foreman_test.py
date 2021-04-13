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
                'λ҇rȰҪԐŊΔʚҢɓӵρǾʋAýӥұ»ʭòґʟŀɊσǃΏǪ',
                '¯ȞІӘǜϳ\x8dʣƅΩȮƍǟїǴƣbϨʅԂĴʸΏЪ˷φñɾůН',
                '҄ƯcҩǑǵˑϹҜΊ¼BҤӇԩĔήȦʑǊǸğŪ˓\x9eüʵҹOP',
                'ӢŢdζɰƲѓЗǫɵΏĩСƱĩЯЊǡËĳĕ(ķ&2ĖTǍÔҐ',
                'Kȁ˝ҭǎИʕԆЙį\x80ǽ¾ΞϩƆɀšϿº˙ƛȟϾɡ˻eėϘŏ',
                'ɵË\u0381ȂζԪ0űÏSГ˚ԭѺơ\x95Ʃ\u0380ĕ˥ПǠŤΎɀӛтКˠǾ',
                'ѿɈʥWçƲŮ\x98FӅãɰОǾȗӮџΕϥȡãή\u0382ħ!úȌҜ)Ԡ',
                'ǹŲɱņϥҊзT3ŠҳҿƩфѠž˧ǆfÌƕǕԒȼǡҒiŷĿΐ',
                'Ҟӡŏӳ(§гΑûȌԜѹřů(үƁĶЀɸįš˥ѭ\xa0ЗԒӾ«Ɍ',
                'ʊůԚӯwǋӍ',
            ],
            'source_id_prefixes': [
                'ǎûȆѹӦʭүòȷÛFȦб:şѸ\x86ċԨϸ\x9aɋ\x90XͶȳƨʺҝʘ',
                'ʂȰϼġҸχÆĬӝοЉpӂ¨Κԗ¯ȜӴĽϣϳĬЂĝíȲ@ƑѪ',
                'ǎǲ\u0382Ϊ!ȂƘίѸ\u0378ϊ\x9aϛάϹÜ\x93oϩǉίɩ¾ΞΆȉъвÑë',
                'ŦkξXƮŎʧӶİΆ\x88ɬϧɷàԋɟñҶĿѨƖΝ5ȷȯЧζЀď',
                'ƿșõò\x80ύѶɹƏԃрӋϸƪďφόTɃϲȁƥ҈ʗпҦԆØƼR',
                'jҠήОϝōȿˁϠӔɌԃВªҬϘɫχƤÇ¼¡ŢʟƨԩΫԍкλ',
                'ȟǼэŭԃюφmЁʟȎҙLǬ˄˜εʲˡʳԎԖϋǲΏƼ˫ƔѼʉ',
                'ýŰʳǼʯêħEȶйüϬ˒È\x90Ͼԑ\u0380ԝўɯ;ϐúĕǶºȬԮǳ',
                'ςЈƀʢӰÛήÆƺȕЬˇң҉ƕҸĚŀčɑ¸҆ȴČȻҷҩ˪ˌl',
                'ιǸmюӰˌǂ',
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
            'action': 'ԀëԙȊȒǸҸҜũԧѨӣǦԠӯ\u038dγš±ϝϔçˁ˫ˈɛϪÌѵʙ',
            'resources': [
                'Ã½Uщҥνŋ}=ʪɜɋĮWХęҝт\x9fͷϛѮñþα\x81ɑȝҐь',
                '{˙[ÉμņȽlȯΎOҌPұˠԢǻ;ğŽɃǊčϲ˙ˠǒǴǾĆ',
                'ӌҙȂҲȪȀǼɄқǖ?ʏԖϋӵˮƦĚɐϺԥʮ˶҄ӀӜ!ʶӹɫ',
                'āωȋ҉yǨźУŸɅƘ˓pәȣ˚şɐɕ˔ȞˬџȄѿɿÍǥϷt',
                'ҫ\u0382âΦ˲ɕϱфɋǦƋĻʤ˖ҌƟŏƼ®ɹѶĜςĲоǦϖRϻ[',
                'ìӓǦώьϳӁɂɠӡƠÜôTӍtо(ƗŪЕӄɰaėыzԜѯӁ',
                'ԝ\u0381ɞ˚юнʮʊӦҗΨӋ<ŖЎÐñμĶ^¤ұЬρǗԮņ҇çϩ',
                'ԬϣÈňʊқŷРљΩ²θÌԠŇɳØˉƭ\x9eϒʡƠJȋƅȝ«ҌƢ',
                '˔\x87ϣ˞ѴɡҺƣȗ+ͱԗ8ϳˑ®âǝǱ˘×кԡȄχӃԛ\u0379¡Ԭ',
                '҇ĳMƶ˽ŐЏіɰзɫԖқӖѕǗYʥɖΩʡ\x87Ύ˴Νϫ҄ϰǹh',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ԩ',

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
            'name': ')ÖȊӼìТӻCȼǩͲǯɅǒŘ΄ϔvQȕjϛϱԩζӍġȈAѲ',
            'version': [
                -60448338514519076,
                -3207343612367613877,
                -3099168868742131592,
            ],
            'location': [
                'Äϭť»ˏ҃ĝǥѳԆÎɇʲʎƕϡÀҔ\x80ҀŭКŎҼmӝЍɂȮ-',
                'ːǬБџ@ғåȥ¢ɯУԀ˧ˑĳŤ/ʰ\x8aϬǧųņӄЕӱʩŰ9ϧ',
                'ekɋЯǆҭƍϢϔûщNʇƛĻǡ\xa0ıȘEΝԃң˙űɤŞCєҜ',
                'ïԏμĚȭʟˑΟğҤϮјǔЋƣƩcqǠć˱5ɤƿŠɶŎˈŻƌ',
                'ɔø˄ˊĸɃχʴɤǻŚ¤љŦŧьӇǜғƑÞɆÝĳȨØѲůʪġ',
                'ƕӇɿԝїŻȾҒĨwԉ%ҘʳЎХǋ\x82ǻóƽеĊǓfνϻО;ϗ',
                '˳ЧkӓҮϴʨӃ/ԜĿӀИ\x89ΎԑЛȽ¨ҁƳҲͰԔΙćҨńĄн',
                'Eđɍȧƒɥ˭ǔɶϙħƬč¨ćΑʜ˗ƯɫΓæȭ\u0379\x9fҥԁǤΗù',
                'àȊԏςLȐҧӲˊе˘ʪɮĴɹϳАÒ_өхΡӨώѾıʞȾЉԁ',
                'ύƓĶz\x90ӺΑɏˬċŞƿįƂ\x89ǱƑ®ɠȵƧЮ®Ƒы˦˪ӮεM',
            ],
            'runtime': 'ϋ',
            'send_access': {
                'event_ids': [
                    'ÍȌЦśʺӰɨʆҶ6яΛ˓\x96čƟƻ҅ˠýf˃ƾʦƸVӄèӠĺ',
                    'ϋʹӔԈԍͿi\x99\x9bԞ˷éȼʗɓ\x9dʈ\xadȀĹɯȒɕ˼ȋɢǤ\x80ЍØ',
                    'ӣ;ĩz\x90ÕӵӚϖΈɯȦúͿέϳȺˤÚфİɻΗУ˂ɴЫÑöё',
                    'ɖŪȿėүϋêğĲуϊЪƲϟ&ǊԐ˭ԅʋҺǮƇӚɢOˬǴƭѧ',
                    '\x90ЮҿҊĿȪРiҽϖ´ʶ\x83hƃвſΨƭÑӛʇçvŶӴӨҖΛņ',
                    'ҷѫөʬѬΊ˰ðɖǕÊġ˛æǡͷ>ЩʼϧQǲ˝ˣ?ϔμǴƭǚ',
                    'ȨпфǼ\x8aʉƃ=˒ʶőԝϋƹ.0˅\x8eӺШčћˠαĉʾʾëǕa',
                    'зηǓȃқҠ\x92ӬӴɖÈAÞÞƼЁŢЋΖѦƭЫůˣԊӜүϼ\x8dƺ',
                    'ǞǑƘӠӰˤ\x97Ĥ2ӱƼΗģͻžɜЁЙȳ\x9d˂yƌk˔ѮǾҢќν',
                    'ΚŹԐҀYɟɗɴʰԋɛaÕhɡƻξӚόɍԙзӴîΑbҨҗʓҙ',
                ],
                'source_id_prefixes': [
                    'ékëtӃӒӯąȿ\x87ӿįβÑ\x87ɊұӞɆʕΣӀЯдХưʣʯш¶',
                    'ɊўɫзĨĶʈƓƩǊ£ŜΘǸЉUӊҸĖϼϝˁϬʔ҈ϱȰ\x9bʋˋ',
                    'Ŷðʪʣmʜ:ĿA˽5ůĪМ;ЧĉǦđĐţiӛӟьėƸˑ3ϳ',
                    'gʉфơ˓ʀϚΓǕһΌМŅЭӗɿ˹ȼ\x86ȕƹȲ\x90ϣΐӄҜ¼ӈɥ',
                    'ȨȔɵр\u0378ѕӀΔŃѯȿƖʧ\\ˤԖϪ·ˮ³ӭʜkȍǛͰΎ6ϘĪ',
                    'ħϪɭŋʻҎ˅ӡɦϻ~ď\u0381јČÓŷɄɮRςϥʏѳT\x86˸΅Õ\x88',
                    '˻²˴!-ǂҝȐǢϐțƢϧϓЌйàșӗʋȄ)ȤţΈѴĳӯǤЭ',
                    'ƀ˛ЪĖˤƶďJѲȊӡÕ8NʀȊʟ4ЧҞǬћ˟ҩďɄŋ\x8e\x96Ø',
                    'ǐϼσȗӫϮĬΪPcǅ˥ʫʌѡȷƐҪ\x89\x97ə˾ˈЕˍӐȾɀʼӬ',
                    'Бўǝ3ƠơϭǘłԎԙԟØʰīНҸҁȌ¦õˤȥгʈХйȵžʜ',
                ],
            },
            'configuration': 'ɅΑϖԩcɟҝǆƪĚ|ПȆÜҿǿҸʀѤϷ\x90ÓϽǓʮЭӂȓԧʕ',
            'permissions': [
                {
                    'action': 'ĤΨƺŔ',
                    'resources': [
                            'ԂÉ¥Ԑν¶ǹǆЅùʸԃƶһŤîʵϑΦƭӈ^Ϭ$ȉķ˨ƫʥ£',
                            "Ǥ\u0383ЭȓȽʺ'ќƯΌɐȬƬԜќјӷΜ˸ÎΏmԮƄʉʇɫîƙŽ",
                            'ѾåQ&ШЪӢƉ9Ϯ\u0379ǶZɡǆϕƹǑςĀӾԗΥΞџƽϖ˚ŷΰ',
                            'âϪɭ²ʮЍƳ=ҐΐǦҦƆ7Ȍƾġ҇Ɛш\u0378CӝƵӴĞ˸ǟǳϢ',
                            'ьΓɪʎҔȯѲϮɁ˻ƎʦԣϰΌ҅ĥКϕĎˬĹ\x81ǄҌǥ\x8aϦƨü',
                            'ĚŬΦǉ˃ǴҜåΎƝΦΣ¿ƺbʧʟɵӶҘƅˮŢñɀѲ϶ʭƄj',
                            'ăģӑǱŷ\x89Ř˩@ǊΞǮҲɊǞӽzĺ\u0381Ĉ¤ʂȍ\x8cðЪȉŲGű',
                            'ӽš\x8ajϩĉҼІǫѳˑӮȖƱҏȂӷŽũ͵ɋяƉϭʲöИЁ\x89Σ',
                            'ãȔʼºЍř²\xa0ýZıӞϤĹðѤʟ§ĠȏҔͿĵƻԫͱƱдɆƏ',
                            'ÕɹҏЛŗɋ˖ɭΖФʐҡ&ӄΪAԑЉʚãəƳÁόЇκÙ͵ǮІ',
                        ],
                },
                {
                    'action': 'ɽˁȚӹѧҀʏ',
                    'resources': [
                            'ДͿʻѫŽӒǿÅʄԘ(\u0383ĸº\u038bÚȀǽƛƌńДɂ1ȤΜɿн%ǜ',
                            'HӽҎơȚčԞˍͷλЗÝЌϫƅǺˇʟşӯѨӈϸϛĽЀʻϯˊĉ',
                            'ˊɠǈƴΣèŉʣŅɣǌӫëКпƮƖĈ+\xa0ҧȐƙԆʗɢѫȨ7é',
                            'ŹԊßѱÐъŁЦЀркщ\x9dɐɢԥ:ʖǧ˯сɾĂʿú\\κѾ˜Ѓ',
                            'ɴ\u038bԛŋөńʔƑDŭɐƄΫĸUǷĨҀI=ƢðӅч>ҞÙóZǖ',
                            'ӺƤÆЗΪʝҎơAƴŦɀćŦƜhϋԇә|ǥƴ\x98ΐƃžȁԚʌҚ',
                            'ƷtϮʃĊōϲϫӁɰȪѰqΩëȭԆҺ5Ĺԙˑ¥¥ʖǺǟˋѶT',
                            'ΑОöӗƩȹǟ\x93oыʵ˳ѲϺм>єȗ˃ø˂΄ȮƂʿηɤŜëƵ',
                            'ȄҫŒҢ.ɵͲ˒ǙŃɃӲ^ʵ"ƲҫƱ˷ԝȢƀӲ˕ǞȓΓʮˤǢ',
                            'ºԍГĘĄƲʑʱѨϊˣǁϋ\x93ϹӤYʫɽɡjϧЧԋȼɏƼ˃˒ȅ',
                        ],
                },
                {
                    'action': 'ѪŲȀ)ҕãƫѠȎǄΚƖɡԏ\x8d\x86ǰ\u03a2˒ҚȒɗΤ˚ƊǨҦҿԇҴ',
                    'resources': [
                            'ɿȟˈȵÁЈӛϩ6ǱόͶɃҗѓʝɑŎȩƾԀԉǣțćɅÅСɒʯ',
                            '\x86ΏĞ˛ԟ\u0380ƼԔˍʙҩqҐЛǍԑġΨÈ¨ԌĮЏ(ʋǹͱǐ\x96p',
                            'ƳЮќѸƩƌƣҾĉϋϕʟўм"ǤԠȗƮʓǋ,ӫŬїӁƟϲĈϒ',
                            'ϘͲһ˫ǍӮǛңҊϫϮһŮĊΖύКʐӔѠˈϝȪùΤ³їȯɎŧ',
                            ';МƷѵ˨\x99ź\x91\u0379ηӊʨѾĚҦƺĚҧɁҪǩɈƜǖĨ{ɝԣԭĤ',
                            'Ӗoƴ+˪ˁ¯Ғ˫˼ʀûǡǣÇ]χŇɍĎcáӷʼŌɿϨĮʟB',
                            'ÙʑϔӾɵĚĶюǝҳГǔĘêʉøтÄ1ѼǱȌȐŢȖҟÓĆϤѾ',
                            'ӊʜҁɼǋȭеó>đŏ´Ë˓ҚĀӧő¶иҕƝԂĄļÔ¬`қȉ',
                            'Ɏȹ,ӋɨņϮԀ\x9fɈĳγˠϳBŔӬķԃМΈҎȐԒ˱șҽΰɯ*',
                            '5ȯɹȳҩȱŗƖÊөƴφx҈ɠѤХζµԭȟĵϊxɃƜπĹ#Ƈ',
                        ],
                },
                {
                    'action': 'Ъкq\x97\x94\u0382ƇƴПĨʿǠQЂӬ\x94¸ʭ§рӪҊͰ¼ǊƶˬȀЬɬ',
                    'resources': [
                            'ϋţ˭ϸΝĘĄ\x86!ғΔÑαΐŜ΄ϻԞ˽Şċʓԅҟ˘КƙćTҀ',
                            'ҔǗ4ʽŗ$ЮǨΚʒӜƗԖƨʵѐǪЇX˩Ł҇ӒÈȷǙHХβ´',
                            'GȚԓ½ϸȰɐď«Ƹʭþ\x9e\x9eÎƬŵÕЇƫΙғѾǬńПûȔӱƅ',
                            'κ˲Ψ˔Õ5ƝɸǝKǄ˧¯ÜΚ\u0383îğɊοшȅƇӦÔ\x84Hſŉϗ',
                            'Ǯϓ\u038dɨÖќПøѻϥеʘϱɛƎ\x8bĺĵŷҙѵӏýҟĠѦLϢЬ˒',
                            'ӽүüʹ_ŴʓƈӃƾxяȴđɳΤ{δƃ˦ЯƲ\x8eȌȽãƱVґʿ',
                            'șěŐѮ@ƪһŋԊŔѩœʝ\x8cғˋŮˋïNƤʔԒƢƼҒŽŹÜҿ',
                            'Ŗѐ\\ӜtƮ£ΐȂǓҖúɝҦ7+ϊѱˬǉӱӿӅͻҚʍҞɝžȯ',
                            'ɜƮϳВPˌŝԂƮӅáƼяΝӥ\x94ĲԂòĢŜǎСɉĜ˚Ť\x82Ϟ˱',
                            '˰İ\x9fǋ7ªcԆĶ˰ϞѓŨѾʋý«ҍέжɩɰӼčϮqČɚЖӬ',
                        ],
                },
                {
                    'action': '\x85ŜǑӅӧ\x83žŁļφȓԨ˰ʺΰƘӡКгє҄ҥ\x92ǉƖˎˤͶǤƺ',
                    'resources': [
                            'ӱǽʯˍǅҊ\x85ƯϊǵӈƒƠϫƾ¶Ѕ\x80lҰѱ͵ƳƟГ-Çӹɲ΄',
                            'Х˸ąȏΨʅбöϘkȩƑl!ö¡1ӟ©ӹʻ˞ŠȒϐąČɧľŅ',
                            'Ǚ9u4ɢɽȥȟєˍʽã˽˷A҃5_ӤӿǖԅВɭπbǮÛóʣ',
                            'ʘUҴϽĭу¢ʍ©ªŹРƀ·ӘƖζβɀϓHϭėĝÊłɈӉԆĐ',
                            '҇š͵mҸ˘ҬѤçӢęԒ\u0379ϸƙȞәԓώĦϨĲǁņǋ\x91ЪȡφϠ',
                            'ŴΓŝbɸȃʹ϶ԗƄϛʴŋԨŨԧωѧΕɇˁ°·ŘЂ˯ϴõʻ:',
                            'ԄАӲσƞǉĦ˝ɜ®ô?ɽҊԅˊŀЬӹЂ˴ňȋάѓǝȟ\x91gâ',
                            'Ρ)ʴÊŅ½h}ȿԮʊұƵϞˠô˳Ϋ˺êyΛóљǏŭǘϡоÏ',
                            'ʯ·°Ʊ\x95ÿЬDςҎɷɼºѶԛьǜѠuɮǓ\x9cӭƜӻęǢ',
                            'ϕҩGğʜĭȀӞȁΏȊʏѴ˯ӸǋͽҴĨõЅҹƄƤȉõїΑ˚Ƞ',
                        ],
                },
                {
                    'action': '\u0380ƈӘɋːЃÒ˾~˳ȨſȐҘPÒΗƆχ\x8dЪԤʱεǅƩЮǰɺ}',
                    'resources': [
                            'ÀƱԊʟ\x96іǳȳµ0Ɇ҆ƂϑżĤ͵˟Ò\x9dʉkѻҥѭIѝҽν±',
                            'ƁԥӊœɘҸϏ\x83҃}ͽ˦Ҥƥ@ЌʨѨѭƹWԛђϩӅțɴƓĺԜ',
                            'ˎИȧԠĬԆƃŹvѸÑåɱǆͿϜʯCkπ˥\x8aͰľÄөéҎѹÈ',
                            '˨ξȐʙ΅ӺӲȼСiʅƕīΪGǢӦɽӚwȿҥ\x9eƑȭ΅ÇԆԊű',
                            '˕ǥʣӐÉCІϪӇ\u0383ҷ\x82ûćΡˎюϣ<ӾķФǁ˲Ɠą2ΕƽΟ',
                            'ε\x9bŚΞѻ*ɱЯĴʟѶЖŗҮĜ\xadЀŧüʞˏӨ<ņԡû/êҹȘ',
                            'ԠơȤщӄϛБӢр:ϾRɒ˨јȎɶͼʊȘӏ',
                            'ґӏҸŬ\xad˲ʎŚäĤӥԏ˄©\x93˟εˉǥӫΰ',
                            'åŎξjʏɰʓԈS\x8dĖЃŧƱϩќЖȰϰ˝ǜеĽк˄ȧБӢȣä',
                            'ƾȎ҆ʥӣʟŝďςɂĴʂѥų˥ŹǼԟǕƣԞÔϴʮԡɖBʮȲä',
                        ],
                },
                {
                    'action': 'ȱԥŞɌΒК ę',
                    'resources': [
                            'ˢΞì˘řɴėϛтĻ"УQӮ˧ͼҞfԦςĺǙԗDʣːĊκĕԫ',
                            'Ӵҭ˗Ң¨ԗȒ\u0379ПćòˁаĜкϊԪʴŭΓʨ9ǠҁŐɀþʐŸԄ',
                            'ѬŶЮ×Ń\x83cҷήÈϑʎȺ\x97ӦÌԇȉтѓӝІȕΛ¾ѴΤҥ5ȁ',
                            'ūϾBʄԉκɵĆξ£Ƅ\u03a2ÁɳЉ¡ͷΣŪӬʠѳϯ\x8eӼͶʍɅѹƀ',
                            'ɜǭƞǫĭǉĚο\x85ϼȵÃÓˇѤляʉԫϋ2ĿСҍǆĤĳƈϥΨ',
                            'Ƚɍȥх®ϵϻԔѼӢБx˧ªăȘσȗΗϭԒѿȯѿϮǯÿąӨǭ',
                            'ˉɖΞTɤȧŵʺѹԬđԟ{ТˀȖˤ5κЅJѵԇŽʺӖǥ<ʒĥ',
                            'ŒͶĺȌϼɒʃɏ\x81ʆҚǪӘɅόŽɯËƫʆ\x9eɘȞД˦шÇӧһ',
                            'ÐǜӘҾcǱɠǉʉ0ԅԜ˛ƞ˖ȟȃЦҞEĴοβȠԚ·ϣōǓŇ',
                            'ˏιϴŕ˲Α҅~ӷǠԕ˺ʄΌӨ>͵ӽǠ©ʖРԧɤЉȰ˾һпd',
                        ],
                },
                {
                    'action': 'ҦʸͻPÿʻǵƬɌҟ΅ǴǜГÕϱˋȬδԌӠФ˽ТɍҗĢҔʇѷ',
                    'resources': [
                            'sʝ÷ϋΏˉǰѐʼͳ\x84ÊŴħ·ԐΊө·ĻӋѾìӥȁǌԧʽŝѳ',
                            'ҊԐ҂Ưʆьʀҩ˙Іiȵ˝ϚʐʺӑŻΰ҃ʅȶ\x9bѵσϫªȰ˵Ѯ',
                            'iŗɘe&3ΨõŠԜҴĪ\\ʠf\x8bȥѾÀԒȄѼʹβѤѐþ¬ɟǕ',
                            '˳ɽ7\x80˸½Ąɕóΐ)ĨяȲҢðзķɢɘʩkɜζÒЙϋĨȄ½',
                            '\x85\x8cш\x94ΕϪϝȽϔМӳԔ*ԤӐSƪӖҋƅȴԣŘӗǍŧɓϸÚЬ',
                            'įЀϐơ҄ōćǔƆξʺЙȞˆÙ²υҔʶUʕϬāвԮʶͽʹȈ\xa0',
                            'ĒӯШԥǲΘeƽҵùͽ/×ȥĭʪΒ6ӂӸҚӵʉˆˏˎҬ¯Ͱϗ',
                            'Ԟ\u038b˷ȠʅƨIɭӂПƌÎфȷʵӝɳĕȸӘ˨Ȯŏ\x82ȺҳɏǄĮʰ',
                            '·җɻҤǽɄʍιϡʭƁǆɐѷʣǫTȅÖƺΧɲœȐǏʴ¶ͿLŉ',
                            'ȬϭͶԋ\x93ɫǌǌāȩʽŅϿΪͶΛoЃǈϬŴ\x88ϡ:ʟƚțƍ0ӂ',
                        ],
                },
                {
                    'action': 'JЊѷѢϽϱӗϭњ9ҝʾѣaŷǲƶƩȄrәĠɶӺбԕɈФǸɷ',
                    'resources': [
                            'ϙ¤~ŵӝʴҚχĜѧӪǘɭӌŢηǤ\xa0ȤΙƍǉ\x9aԟɷԁƸɇ҇͵',
                            'ˡèўÓƃȒɤӊǆʡŚϰŃģɞǐȾҗ\x87ĵĺӃƍɺǚ˄ƵŭŻǳ',
                            'п˛Ξ\x91F\x8aгӖЯÝӞġѪΝhƊbԛ˼͵ҘħΖ~ȆԗԜǃΐ\x94',
                            'τҋƒнĻԓŞѝÑĥƦƭӶɺ˒ş(bˎЇƫϯ\\ӾŏҘƾбŬӫ',
                            'зȿÉǃɋϞĴǈ˴Ԁ\u038dãĨOͼÞĝж\x82ΪƼмɊιêȞϮıŗҁ',
                            '˥?AǤ\x9cµΗҝΠĝӛʙѮεʠ˼šӖ\x89ѼѴ1ƙȾāɏɢӓ=ː',
                            'кǫ(ū\x9dқӎȮУȨƨëʼĨӓӹϱĘԖ1ҹңåҪƲɉǓęĎǌ',
                            'ʃȩŦ\x8bϲчżʋӗǸ\u0380ʹˠŷÉйƔђЅWÎ\x85ÊϧϮҮӱʰƍ\x94',
                            'ɩțęԢCωǘuɽcҌŜϳɺȺÔ\x94ӶҙĜŒǝЇԏį¼ˆϪϟϽ',
                            'ʿͺ\x89ýΨȼ˓ӁǉӋԅΪɫōӼƯNԥåƀƱώəΘԓϹН\x91Ǚǣ',
                        ],
                },
                {
                    'action': 'ˤȃҞøDдΰŋҋȍԙȴұ¶ΥƬπdшԉñэӱƜѭȒ\x9aϑɁɌ',
                    'resources': [
                            'Ȧ\xa0OĠ\x92ϥБ4\x99ĬŎʱȯǘìCЊԙИ@пˑ\x84ԮҐūʪjɳґ',
                            'ϐ˘ӖӋʹķƜŤӧȉӀķϣƺͳ˘ҢԠ˧ļɇŘěɜ˞ƆȲѾōь',
                            'ӉɂϤɎΰĒȧŴɇåɓȇɭʹĄέ½ǠϟCθԀĆǯϘ˗ÓΛá\x93',
                            'ƗĥϰѩǑāBΈӍǕѤʓɬįӮƪÜϪʘɯąúĸ±ŗм\x98φƓʿ',
                            'ɳğɹϊӵƍʂҗþÁKϯȤÞɆ˱ΧŎ\x9dŉџÌɳҘԮͷʹόIъ',
                            '[K͵ľˠɺҽ\x94(ΆƮɦùšïԦ҉\x92ȽÖЋƏԙȚÛй˼Ίѓ\u0379',
                            '÷ėǑțаΐҙ˸\x86ӊϾĶ;ɉ\x99ăŀȩшҵ˲Ц҃Њз;ϣīҡɽ',
                            'ÒŒђЫѢӞì\u0381ǼČĒҗ?ҌɖAǱǞӕШϐǨѮǃâü¤kƞӝ',
                            '9ĮϽƻЀϗɌ\x88ϩȼ°ͽςσʎƕƚƤΛOƀŖ˪ɵœɁί\u038dɶӁ',
                            'Ɍg¸ɎƦ\x89ϗOО҃#Ư\x85ХƹȲП˜ʢƭΆ±йѠɵԝͿɠ\x8cε',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˦яƏ',

            'version': [
                -172599323821273892,
                -3997856138814274043,
                -5824700604201145685,
            ],

            'location': [
                'ь',
            ],

            'runtime': 'ѝ',

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
            'name': 'ΪΞȃНҀѮȐ+ŎȩԚɸˏʟҜȘӪξӁʃȅǹӟȼτʛҰɵůƃ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǻÖĳ',

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
            '$': 'ĸʣӸϙKэВϚĩǗȪԒ\x88ƼΏ@ыϣřƷӕѧǵƃ#ǼȉђŤʖ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 1958805812118404502,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 450479.75235717953,
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
            '$': '20210413:000954.057639:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'u;˔ɐΜȧҥfɺ»ˇΛ΄\u038dɏΓɎґλԣșłϰʎǦŴ¨ͼʹъ',
                'ŒҾЪѤфȭҁς#āÎОîǏȴįϿʜǭ\x9eʶӴbӱːʝ˪υβӱ',
                'ʅȂʊвҠԕѺRưºȍΥл\u0382ɈŰԐʺʾɶɨȭѧЌÒ1ȳϕɥГ',
                'O҄Ǡx\x9dХSŌРĹϘѳӏ\x9døǌȊƷǦ\x9bŕʚğ\u038b%ЊŮҳÓŞ',
                'ʒϾͱǤēĕěƱǖԍóϓνӏÉƘǨìώ©Яˁӄ"ДҐĵЬѢè',
                '\x86ҙӈũЫƈҳƵѿűúѪ¥ŃǥԜӾƛ·φΨ)҂ԣƮҶɟçԛȧ',
                'ż\\șJϭˡӛѹҧʸɠȞƓȥ˥ϊŝ´ґ1ǕƶÐȏŰMХĭʛѨ',
                'ȃňϬbœэ\x83ŌЉԇʠԒҫɭŲчíа΅ϫӷ<Ų²҈łԓǼǵЖ',
                'ȬКưА\x9cτԭ\x7fǢԍʧ˷ļ˄әyшϽeбҷӅɭIŶΉѭфŀ8',
                'ҡεԮɬËӿʄ˗)ʤŵŊʅθΩχԏͿȸĿϓ\x96ùHȩæϡƸέԫ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2977689962054125521,
                1247798539005498407,
                -1246785503292429696,
                5691133036269760252,
                8327516420363818254,
                481951938469865758,
                -8488597770243111911,
                8334923214684890591,
                -4107802280701591600,
                -2974702990830034394,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                756489.5068182888,
                984854.1453208353,
                188409.30201823998,
                706802.262456692,
                421700.84798350907,
                842273.8985091627,
                648855.9376655164,
                452433.71546764777,
                689572.0491226609,
                297724.0545725048,
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
                False,
                True,
                True,
                True,
                False,
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
                '20210413:000955.325494:+0000',
                '20210413:000955.348765:+0000',
                '20210413:000955.383304:+0000',
                '20210413:000955.403566:+0000',
                '20210413:000955.422640:+0000',
                '20210413:000955.440940:+0000',
                '20210413:000955.460301:+0000',
                '20210413:000955.480122:+0000',
                '20210413:000955.502693:+0000',
                '20210413:000955.525277:+0000',
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
            'name': '˗˷НõÑԄſȆ˂\u0379νīЋ;ӗ˪',
            'value': {
                '^': 'float_list',
                '$': [
                    43126.85086627805,
                    782745.4010894598,
                    771196.3270636549,
                    298265.0192757759,
                    603315.1410832988,
                    466731.7394942647,
                    280912.6889821813,
                    956349.930149063,
                    862898.1708404964,
                    806022.5650442762,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x96',

            'value': {
                '^': 'string',
                '$': '',
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
            'catalog': '5÷ȾʂʋưɐуӕʚĤlȫьέÖү˲ӏhȉӥϙђpǲȷ=Θǁ',
            'message': '\x8f¤ѝɅͷhʤҙԊ˒nĵЏm\x94ѯƏКϰƆϧǰӉзΏüƜϬηù',
            'arguments': [
                {
                    'name': 'ϗȒÔÁӊԠŞÆҸˊϺ¦Áƺҹ˅ĄԮ\x9aƌґɶi\u0383αϽʈÏԞИ',
                    'value': {
                            '^': 'int',
                            '$': 8680687573636638767,
                        },
                },
                {
                    'name': 'ǳɪϛɐɁŁ«Λ\x85ϭ;\x88ԖBĽӂ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        7871578695397216778,
                                        2240588328988294834,
                                        -3392178042873884209,
                                        5500325035503522732,
                                        728220176882654280,
                                        -6689249851130810349,
                                        8239474408809292587,
                                        3166559322055716899,
                                        7807836806293392443,
                                        5419792836559135407,
                                    ],
                        },
                },
                {
                    'name': '³иҹӡЏϸ\x8eʋҙʊԂѺҊӹĝ÷ƠɕőжЃӷҰʑƜΗĐŨӎӧ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'cәʹӐķ\x96˨ѫхϔѮʚʝӃɉӭſΤɣʕҕƶĆĮӼӟϿĕîß',
                                    ],
                        },
                },
                {
                    'name': '\x87ɖƃ#ɜЩŞ',
                    'value': {
                            '^': 'int',
                            '$': -5287910850718312692,
                        },
                },
                {
                    'name': 'ÝΡӸΆ˺åҢäžQЀҸȎę',
                    'value': {
                            '^': 'string',
                            '$': '˙ѷϲҊÜǬǁƪǛΏěɷиǅΘϗɦ\x96üЭƅɗ҉ø=˨ԀϿǩӿ',
                        },
                },
                {
                    'name': 'Ųƞ\x7fѭˢҊѨ',
                    'value': {
                            '^': 'float',
                            '$': 415378.1656911518,
                        },
                },
                {
                    'name': 'Ú҃ɜˌ\x87ŵīʷŮѥǞǍЬ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -8169131126143943195,
                                        6160393444639320847,
                                        -3883527673950888186,
                                        5304578906483086814,
                                        -410164555879230872,
                                        -4362668304897787850,
                                        -5707228712822713753,
                                        8819529641451635015,
                                        1500427197321539764,
                                        -3695218620351786820,
                                    ],
                        },
                },
                {
                    'name': '\x7fВ˔yФрĶВǂ\u0381Xтμ˸ˀԫŮɁΨнpР',
                    'value': {
                            '^': 'string',
                            '$': 'ѝ¿ĸɜŮЁ҇ҸĖΑчŕʢ˒ƊСҖɈηԇȝѐԟɢǇĲƂ\x91Ƨυ',
                        },
                },
                {
                    'name': 'Ц°ПƅԝÓĤŉÄvӍʩѺɎĭäҜŜɆƘеȲʪǸ͵ʢѳϷϕâ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        25839.94774397195,
                                        346788.53693749855,
                                        185043.26114288333,
                                        864265.7649022848,
                                        740231.8084411018,
                                        681750.592269369,
                                        341512.6726888639,
                                        -74217.64861801335,
                                        562399.9638806366,
                                        32358.863349575637,
                                    ],
                        },
                },
                {
                    'name': 'įpʠϸTŅϒѰɅϔʿÞǢˈĨùǛϪÓɓɩοȂñ\x80ӧέŮѡ\x9d',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210413:000953.236472:+0000',
                                        '20210413:000953.255086:+0000',
                                        '20210413:000953.275525:+0000',
                                        '20210413:000953.293979:+0000',
                                        '20210413:000953.313612:+0000',
                                        '20210413:000953.332543:+0000',
                                        '20210413:000953.351847:+0000',
                                        '20210413:000953.371634:+0000',
                                        '20210413:000953.391078:+0000',
                                        '20210413:000953.409751:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ȖԘ',

            'message': 'ŋ',

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
            'identifier': "ʊ,'·ρɧςɊϢдȪ˵ʙ΅C´\x80ǕѯѶЪ˱ЬǮȍгɌŒιы",
            'categories': [
                'network',
                'file',
                'access-restriction',
                'access-restriction',
                'configuration',
                'access-restriction',
                'access-restriction',
                'internal',
                'invalid-user-action',
                'invalid-user-action',
            ],
            'source': 'ϖİζǚӬΘ5ɽͼŵԨʭáżƂʝЗ˽ʔˊȳӨĳ˶ӶǔøԜԫԧ',
            'messages': [
                {
                    'catalog': '˲ʌ$Ҝ¹χŜŴŕėCΡɃȀǩӁ\x7fİčҲèҬҴʩ»\x83ĤΛǮч',
                    'message': 'āϦ˗ѼîƤǫ\x89çƖДӀӫ\x9bһьΌ;ΐ}1ϟȜaѯӹá\u0379Ƣƻ',
                    'arguments': [
                            {
                                        'name': 'ԏԤ¢ȴьJԟԑƘЯ\x88ƖԠtěȼҪŌƐɱ\x94ҋΡЏєǹ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            805892.296068899,
                                                                            -26912.82866942587,
                                                                            468630.64180057135,
                                                                            680301.3387762577,
                                                                            443032.6532117897,
                                                                            140557.83551815088,
                                                                            528105.3111201664,
                                                                            587561.1592976116,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '»Ԏʻ^\x9e˱ğ˜ϮƆ,ϰ¿',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŗ³ԗӔύŭԚ§őƥƐĥ҆Ɲд˓ì\x7f³ǐɾ\x9aĘȍ¨ÛɇҷĞa',
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
                                        'name': '|ʆˤΙûČύԥ\x97«ɵԦѪϋʞʺ¦ǚˈRȜʞΰӃӍ4˩~Κâ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3704915464821489998,
                                                                            7916858865645273431,
                                                                            6113145254292934995,
                                                                            -5847383167924762739,
                                                                            6669615671180495884,
                                                                            7510875110531909286,
                                                                            8630643118770872627,
                                                                            -1350186025558465257,
                                                                            127011976133325617,
                                                                            123319187423045041,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÐaʘҖӀöÙ˚ʵĺˀtЎИ:X΅ОϺЋʹƵ˧ã˼\x9déш˼ш',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6428048283238264326,
                                                    },
                                    },
                            {
                                        'name': "ϙӠξ®ɞìʳҠȒȉòб0ƐҍȒį!ǫ˧\x80'ϕҳȼɫĊôЬŚ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000937.780605:+0000',
                                                                            '20210413:000937.797774:+0000',
                                                                            '20210413:000937.814844:+0000',
                                                                            '20210413:000937.832123:+0000',
                                                                            '20210413:000937.849133:+0000',
                                                                            '20210413:000937.866981:+0000',
                                                                            '20210413:000937.885546:+0000',
                                                                            '20210413:000937.902384:+0000',
                                                                            '20210413:000937.919173:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¬ýųϷГɽГÑ\u0383ʊ\x96ΠʌӸªʥǡʰȜәǆϕζ˚Ƚę',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƥ¦\x8eƾ¿ϛȗ\x9aƖѝ˘ʁЦƮ\x85J¦ÎőƩϷΠĊǳѭʯӸǜέɃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ìʮг3ůΗԌSđӛ·УʉΔϴ¶&{эĄ˵џɰJшů%ƫԂʩ',
                                                                            'ȹηƱђûХÝʒɗʢҌ9¯ÝĜȠZʊύˢɩ˘εѥɄȭѼѽεǨ',
                                                                            'ąâĆЮӲʫX\u0382ѰĦΕoċǒяbɆ\u0380ШЬηǮ(ɼ£ȿΎ\x94ĉ÷',
                                                                            'ǂʷġοʗϢȀЃԝЄӼ҉ĳФʧҹҔȢȇԋĞì¨нЄ°ŜˇцӨ',
                                                                            'ĈʃƠǑ\x91æþȣǸρʨPǾȒǥδΟƞɅÝĽ¹ʭ¹hÓǧê©ɥ',
                                                                            '\x7fпԡҸęμӆшćԀɥǻƴű\x9aԓҮ˽Ȝ@˯Ӳxǰӛɜ6;яđ',
                                                                            'ЭͶД˯ȢϿŲĊ˖{ι҇Ȍͻʮԃħ˄ѓ˚ˇΊļҩæʀ:\x9eЌƸ',
                                                                            'ЍµΉƂĿҭƧh.ԖĒӠǠɒ´Ï<\x86ˬī\x9bīҡϫϨ˞ϼѯǐ9',
                                                                            'ɩѺȤȉƠƴҧΙԠʾѧŨŊˑ˳¡˃óʓːɀ\x96ΠǳβЩ¶ǳʠư',
                                                                            'ÁȎċĵΏӦΣϯDϿ·Эʧţ˄yʕļIʪʧǷƌȜb|ʃ¨ˍӻ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԩȊĔɡȣӮ*Ҝʵё33Īͳ\x94ӴӚХŤЮȭɛγΪ\x8cӷ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000938.579109:+0000',
                                                                            '20210413:000938.595819:+0000',
                                                                            '20210413:000938.610977:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƒ˺\u03a2яξɧɫʝӊβÙ˲йχǸ˚ӄȉŝâӉԚϊĴЋŴːĲӍʬ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÂͰнԃǶÍјȆǧѼѪʢкʘϷĂ²ƀƻ\x85ʏϹǧ¶ŝưҧǎņ˲',
                    'message': 'ҫɣЫȔӑĲҕƥΎǺϥϩȮǁƮȝśÅĤƲ\x83oӪθĭ\u038bӞvóÌ',
                    'arguments': [
                            {
                                        'name': 'ƀ˾сɊΫδΉU\u0378',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˨ƍδ˛4Ѷѹ˹ΉɽΖˆϨɱɇȓ\x98ǳȯσЧĮ϶сρ#\u038dϝˑҺ',
                                                                            '\x9b}ϔˀĭʪ˅ēȻñɎɹÛãϱˀͽŘɁˮТRë?\x8d\xa0ǊXɖƍ',
                                                                            'ҼdӠ˾ΫpСӇм®ҕӌПȔσ½ɟі¢_ҨʠɺԔɸҡÒϡЖ2',
                                                                            'ȊҩξŮÒŏƒыςҦƍȌ˓\u038bΐʜ¬҉ӫxɜȷԗÅǈȰqqƵӲ',
                                                                            'ӞΝмԎ/ӧʦóʱӡâ\x96Ѥ˨ӸȮůжɁ\x8aΛʈçė\x98Ʈнũř˔',
                                                                            'ü˹Û+ŞԆͲӥθЅѿӔэʻƻ˅Ρʈē3ƅŵѴ҅ûĹ\x9d˨ЉǞ',
                                                                            'Ьѣʦɯǰȋ˥ˣǆȞϥƉҮҽ˹ưʶŠ¿TɱЫͱ#ɔßԖɽĊі',
                                                                            'ҶǊǻȍàԞ2ŭҝęǻơ\x8ehďϕǍѪǙԎƔҁǯȼĻÌϯƄʩ÷',
                                                                            'ŶЖ\x86Ķ҇Ǎʷ2ŷԉӈϨ·Pρ͵ƕҼɸɪр£ñƅɤI;ǋ3Ӝ',
                                                                            'èϭơԔñÉƁӜɭÅѩȓӮЗĢ˒ɕjнʒdǋʼӿĀѦʦɥȭɺ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '.ζąŉȵɁψӶЃȑɻϠ&ÐĿЂTȐѳȧèǾ|Ϩȍ҆ŭ`ҵɪ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:000939.204693:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɘŗ~ӼΘӎЌHΛ҈ΉҎä\u0383ҒϠѯԎʛ\x8cɽxˬ8ǮЇΑǔ˯ƾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1328002041417032636,
                                                    },
                                    },
                            {
                                        'name': 'ǎ˾',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -42859.56921150693,
                                                                            315152.01995006145,
                                                                            839301.3845842157,
                                                                            192653.33598014578,
                                                                            967131.1001561822,
                                                                            898065.5299708782,
                                                                            969795.9841251008,
                                                                            363553.96866542444,
                                                                            -36049.49341578457,
                                                                            811808.2997768054,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŝrʚ½ǎӳǦϠРΧϓӨȴХ\\Ѝ˺',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -817935434490344074,
                                                    },
                                    },
                            {
                                        'name': 'ƘǪ>ÊʗďɽŴɺ˶ВTҳȍңҔʫÄǘ¹ú£ȶσϜƔʹžӜ\u0378',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            979145.6647682188,
                                                                            460377.06565843325,
                                                                            921577.8186794444,
                                                                            -99997.00016779966,
                                                                            646515.0038889888,
                                                                            433561.34099855635,
                                                                            -95753.87455685185,
                                                                            882067.821281787,
                                                                            878745.1801311008,
                                                                            968269.9921259636,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ȶ҆қѽì'\u0378ÏǮɱƙӣː«",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 488443.3847470988,
                                                    },
                                    },
                            {
                                        'name': '/ĠôɏǩſŮõ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƎҢƮûЇ˗Ϙт',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ԝȝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000940.542958:+0000',
                                                                            '20210413:000940.559853:+0000',
                                                                            '20210413:000940.579667:+0000',
                                                                            '20210413:000940.599863:+0000',
                                                                            '20210413:000940.619759:+0000',
                                                                            '20210413:000940.636171:+0000',
                                                                            '20210413:000940.652166:+0000',
                                                                            '20210413:000940.669274:+0000',
                                                                            '20210413:000940.685467:+0000',
                                                                            '20210413:000940.702043:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'a϶_ӨɑĤǗɒǩБƱſАƏЭѽʐÜĻѴ҂˲DÙǱÃŻ\u0383ӯ\x98',
                    'message': 'a\x9dξФґ\x9aƁƌɃщѼϏI¬ȯϻѵŀʌԌҪƌȷ\x93©Vʏūȋǝ',
                    'arguments': [
                            {
                                        'name': 'Ū\x7fϽȣП\\®ǘƭŨȾԊǲÊӝɪәʎōԚҲӄiцЙǖńƤӨĦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '!ǿѽ®ʃĕҞÉɍʣƆǱƾʖҔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҫӮȘхɽʕ\x90ǅǳӞ&÷μǋ΅Ȫ\x85ѵζZŮȐВŉҏƱ´ȚɤϿ',
                                                    },
                                    },
                            {
                                        'name': 'ԋʹҋӖˌʒӸɔâƝΥWЩŝŹƢϟʏʷӃȍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ǝ5ҐϖϤªСӢˌĉә˅ӂӇ¨˔éƉɳӍaèϩÝʣĕm8ǸƁ',
                                                                            'ϷӓύƷ5˒ʨӰʦӃĄӪνʥщɨӨƥѯƩàӺҏʓ˘Ӕ\x94ƧЀω',
                                                                            'ɽҫҾϜTĢŽhË:ѭ˂ǐԔѹʢҧΗOкӹҢΤňˮζfкμů',
                                                                            'ŏąʠ˳=ÅyKҺÀҢЧČΨɥЕҐԌƝϥĥÛʠ\x88ѡќњ)ʪԇ',
                                                                            'ӟ\x86ΐͻλķƎƠˬĂȏΤπŀ"ĴԒԉɛƗĽƦЍŠ\u038bʊƆȘɨw',
                                                                            'ƎѻяĠçҴÊѓȳ×ȿȈƊf@ŭҳҴçêԭpίӁҴͽưʅĻ¹',
                                                                            'ӀjĹʦѠĄԙԞοƲˀɠÒǙǻϯHɫźƱTџʊӑœƌ]Ǡş\x85',
                                                                            'ǊmƠчРƴ«Ãι˽ȓjǛĉɭēüЦ϶ǨǯÏƎś\x97фΐѡӒƉ',
                                                                            'úɹɪϙʔ="ˢĘԥ\x7fƤԖξǛΎǵіҏ«˩ǽÉ¡рν˭яʲż',
                                                                            'ȠԪ\x98аĀо{ԛ˖ŴʘϞȕđ\u0381ҌɁƇďеΰԤĘƟ˪ɦĹžǑů',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϋѵöɧѽϯϸ-',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4480084087025383070,
                                                    },
                                    },
                            {
                                        'name': 'ԡ\x8fȇҘӞʻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            21217.405003518157,
                                                                            634702.265018311,
                                                                            535255.6240692368,
                                                                            252962.15531359555,
                                                                            -96758.25087632115,
                                                                            718523.6077206582,
                                                                            245907.11125966418,
                                                                            654945.4973585072,
                                                                            287481.0619134831,
                                                                            176591.28973183356,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'żþƥƦԔÎ˵ǔѰӫJιˈ`úý¤ʳӔ4΅ͻӁĺѸӾ\u0378Ȉµ4',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:000941.577391:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƿѾЖѠÎ0˨ϤǯҹΘгţʚęӌϔЂ±ϗɓǵґѼ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6886848508451278112,
                                                    },
                                    },
                            {
                                        'name': 'љȷĢėüάӯԢƵǓ˃ҰƝіπβǴ\x85\x97Ȫϫиʫρ\x91źʓǭ˷ǆ',
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
                                        'name': 'ǡΩǛԥB',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѹχʄčñOїLεƻѨɚΣ˻ӘǴ˔χ§ŝ˘ѢýhɗҴ)ӼǆӴ',
                                                    },
                                    },
                            {
                                        'name': '҉ƒʢȕǕҕřӌӌŕѪ\x90īɫФıż{ɠǂāЀСɞɩӗϷɄșЉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            533505.8754916427,
                                                                            821824.857093393,
                                                                            48951.784816499276,
                                                                            581659.1837809682,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ӗ/ĶϕќʶàӋǙϞɸ˘Ӷ©ɯθɿƺĿRВΖâʍ\x99ȘŒņěȷ',
                    'message': 'ˁɰ͵Џ-ӜɍҋäǯĬ\x8bԠɛƾǼɎÈԃƔМoŚÊʐҊɋϖɻŢ',
                    'arguments': [
                            {
                                        'name': 'ұKɑĉđˁ¤Џɴñ˔\xadľÂфŻŻǼˤ҉ѵɾήӆΓƟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5701870684980962573,
                                                                            -5328515279069372409,
                                                                            476052337764187518,
                                                                            7507919599324651054,
                                                                            -7072650833776821134,
                                                                            -507253031710714121,
                                                                            3130406973908702089,
                                                                            -500814885343290315,
                                                                            3959232817763333981,
                                                                            -4167164352539093398,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'uϞ\x99ɚʼʉОϺE\\ҦʊΡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:000942.505613:+0000',
                                                    },
                                    },
                            {
                                        'name': '!ÓʡӭѨú¤ϭ˚ү\x7fВʹɳΣқƎϱπӍʨǋЈǊƕ]ƉяӕΘ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 990064.8350554048,
                                                    },
                                    },
                            {
                                        'name': 'ˊоѬ!ƖϩʴǎψхФŕЪɥÕѩʱͳ°ÊĜěɱȉоÁѪѤɾҺ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            300900.0855408089,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˵ǌĕȷ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ēΐѡĝĳΒÝδ\x88ǜњǭϒʖêƊёLԙƛӹ5SZκƆи`ҪǕ',
                                                                            'ЮħΖ˕ȃʐΔӞΨд˯ŗūҺȅʌ˾ɊӤǹÑčӈђ&ėƛ˄ǿê',
                                                                            'Ӈ\x95"ʾųǊΓɷ>ǈҺ¢ӲѰЩϒςԄǊr\x8eǅˈƻфѻ˭ǆЬī',
                                                                            'ҞșǞá˪ΧЯʡЃĨ\u0383øưӖȄƎȻJρɜˏ,Έфˉȧϫǅρʌ',
                                                                            'ќĢΌ\x91ȪĜӫˋ1ҐѳɿϒҀΗԧ΄XˊҝϩͿӔΉҗuȩ\x8e¬˸',
                                                                            "ĎǴˬŅĦ'b\x8dŋȘӧț¨ÿ϶ǀiЖÁχÍф{žɠʋȪo,ō",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѮƎÆˌѐǡӦȁ\u0378Ż\x91˂ĵİϥɍӘĺϔ\x81eȖԋȼȊώʷƶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            102804.85020558356,
                                                                            430978.4020367279,
                                                                            29549.26433428336,
                                                                            47580.62377400827,
                                                                            11583.620188571775,
                                                                            725332.506628715,
                                                                            -62757.221842219325,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȉƽӊї˰ƢŲķmɼиÃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000943.309213:+0000',
                                                                            '20210413:000943.328468:+0000',
                                                                            '20210413:000943.351889:+0000',
                                                                            '20210413:000943.372979:+0000',
                                                                            '20210413:000943.398625:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǶȱъĹˡÀ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            725883.4584890511,
                                                                            779278.550541758,
                                                                            186748.55523918296,
                                                                            695100.6089242921,
                                                                            378239.27885073307,
                                                                            619687.7442960558,
                                                                            826079.6064945024,
                                                                            103298.45809723728,
                                                                            926893.7773693965,
                                                                            527410.7206625683,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѭĎ˸ЕÒÔ\x90ϭƈǏΚůӔԊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ź\x96&șΟǻҢԀoϥΡҖȣԩɜαӱΥψÈї˹ϢŁȔŝɫƺø',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ԩϴӈʐɀў£ӷϤ*ŸƋ҅ҹɏж˜χąӟȅԤȋƭ˹ӺϘǼԣЪ',
                                                                            'ҞǋѢ\u0380\x9dˎĬƝÞŋҁľȱőκӥʏʲŞӧпԝҶӴΎԪ˧˗u˰',
                                                                            'ǙŋͽƠԑÏƅʞˡϭͰřǆΚϲѦѬӃăȀ\u0379à{>Ѩ˕Ý\\Àŕ',
                                                                            'ȯŹċhϻˑzϷ\x88ԅıφԛ΅ƍƧcOǚ4ХÕ϶ʸóǶȔҶӨɡ',
                                                                            'ƬzΝŋѴ\x83żćĈəƊѶҳʆЬÊϿǌıȭҶjþFǦťǡǤǨˮ',
                                                                            '^ӆřĉŷˏǎʗ҈ӞјȎĨ˃φϧΞY6ƶMOưϑ\x84ʧ¾˕Ыϵ',
                                                                            '.\u038bɻҘ˛ěǗω÷ȆΌе?ɃȆ\x80˫ҷʆѪʭЫcЄȡʢ8ҖýÑ',
                                                                            '˯үʱѠŬŽƟǕ\\ɠáiǽƀϠ¼όɲҊ~¡ŝƻԇϐ¢ͲϷҍ˱',
                                                                            'ͽƿԅŃŰūŲΎ#\u03a2ӜΆʠѷɮʷʋȫȇɊOуǫȼόiϠ˷ʳҡ',
                                                                            'ɗK\x88ʥȫŊσГūÌԀ¹К&ÒΎăĊ¯Ã÷ȃDŷ˥˳sҗ>Ρ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'àΫȵǇŀЩiϺ',
                    'message': 'ȭԊåĴΫЮ˥\x8bʯӡÔêɠЁѧɂȶĉʠàĵ\x8aԍĿӀΤШӂĎŬ',
                    'arguments': [
                            {
                                        'name': 'ӮI)˝ʏŘьʎżȵǫ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 192144.02803308197,
                                                    },
                                    },
                            {
                                        'name': '\x92Ͷ˸ԇľӲƐĔрǔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000944.260080:+0000',
                                                                            '20210413:000944.278030:+0000',
                                                                            '20210413:000944.296415:+0000',
                                                                            '20210413:000944.318160:+0000',
                                                                            '20210413:000944.332802:+0000',
                                                                            '20210413:000944.347768:+0000',
                                                                            '20210413:000944.360610:+0000',
                                                                            '20210413:000944.382699:+0000',
                                                                            '20210413:000944.400645:+0000',
                                                                            '20210413:000944.418877:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ă',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϋҡѓəƧӗ¸ԭϊͺ-ЈǢɡǮȭӷQ³ɃӾҐUėǐŏ@˂fД',
                                                    },
                                    },
                            {
                                        'name': 'ԚÅϮʞʵѹϮүȓ}½˙ĈΌͶ~їǃϝĎǠҸіRȨɎΆҳуǝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɈǙɏʣʡĂӁҌΠ§˴\x9bˣÛЇiӨʇŔѶÙԆφƮʮ$5Ԇİș',
                                                    },
                                    },
                            {
                                        'name': 'лέǣԈūˤǑŝàˀųæ\x86\x85˛Ʈˇ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӄáļǢk¥ʈĊөϞˇϵcϳѮɠëKԈȳ\xa0QŭЌчĭӂƷƭɩ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:000944.896121:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˏ\x99ɝ½ϺǾʚͼс',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΦǬEłєέӓǶȋ]ȈϤԜ[҄ɌҝɨƸάўčtӝ`ΫԢѦ˗ԉ',
                                                    },
                                    },
                            {
                                        'name': 'Ӎ#\x80òɆƁ\x9aФԞ˪ԢԊˀIƉɕ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ЏƅˑʼɆҘƇүȇҠŭ§ϔŉv#ɾȏ\x8d¿ĦϲѫɞƉ\u0383}ȭ\x94Т',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѪzќȊɘƆЧ;ďəĽώρ\u0379Z˯ͼƚɘʬ\u038bлĬϭɷϼ϶ʒФ\u0378',
                                                    },
                                    },
                            {
                                        'name': 'Κǜ©ʙӾҀ¾ą',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4086602151028742218,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'JÔ˯оeƵŕƞŲĀ˦ƍΞǭғϻʁǅįƿoŀʱntĪʣϤʪʀ',
                    'message': 'ŋӟԌ§ԟԫĦδѰ˂˪ǮеɛŜmʍāҲȵɎΏЗɸ\x9fêŹћÌċ',
                    'arguments': [
                            {
                                        'name': 'ǆΆςΫσˊȏěϰӷΖжʟ{ϰˋЕŴŴНѷΩҦǑӺœçЈȡĿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҭǄѯÈ҇Ï\u0379ǥ¶/NǇdԐȹͶ)=ǐ(ķлƥjЁ\x8dcǰǧφ',
                                                    },
                                    },
                            {
                                        'name': 'ԅηѡȋˑˑӦƠԩçÎɢɐӺҐϧӟѸШýΟʚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'тǃƧÑQţ°ԪµǃEƒŦɘπЙҌҮĉɻΩыν˨ЃӞƸĐɾʹ',
                                                    },
                                    },
                            {
                                        'name': 'ȿɂπӌʴĹĈǜнǃʟΐӐʀȩЧ\u038dʃʘ~ϣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȇ˾҆ѤҤĈϺβ*\x8eÏǟ˓ΛʃƄƍŞåǕΡŋǣϔÈʆҭʌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7221664803722653857,
                                                    },
                                    },
                            {
                                        'name': 'ʝŧÃʝǴҋόԚ§ʁИӟΑ6ԀƎƆŽǞӟыŊˡËйψǮf҇',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7369750724146870338,
                                                    },
                                    },
                            {
                                        'name': 'TȘѓΟŶșŔԟ΅ӣť»Юɰ)ȿѫӱąҭΛʨćӖϜѨӳОϮȦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӟԇʞ_йƃЁʗVɏȷȥ˟ʾE!ńӟѱǚКӐʤʡɷșɞʨҰǩ',
                                                    },
                                    },
                            {
                                        'name': 'ͱȿɸýԙȢƓʙѽӴîқȭϖ\x8dШĲРԍԞϐā˕үҝӔ+ЉŚ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3099485624100468787,
                                                                            8244848329969181131,
                                                                            2009673961256613361,
                                                                            3185595446712303670,
                                                                            -4515846521790316299,
                                                                            -4351577315140385399,
                                                                            -1015483515283926645,
                                                                            -5717812913748718866,
                                                                            1220223226565686446,
                                                                            -2389987681921320593,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѠϰҿҖʹΣϘѬȠAž\x88цƫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŁȌ˥ÝĠʦýѴǰǨΒКȧǠ¸ϵӕВɢσʭВζӯƨΰɿԏЉϧ',
                                                    },
                                    },
                            {
                                        'name': 'ǏΓͳӅŪӱóϻɭɒ\u0381ȖβϬөТȫʹç^ʐԫ\x83ȇςʔáκÔˊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000946.479284:+0000',
                                                                            '20210413:000946.496784:+0000',
                                                                            '20210413:000946.514560:+0000',
                                                                            '20210413:000946.532315:+0000',
                                                                            '20210413:000946.549308:+0000',
                                                                            '20210413:000946.566385:+0000',
                                                                            '20210413:000946.584025:+0000',
                                                                            '20210413:000946.600829:+0000',
                                                                            '20210413:000946.617824:+0000',
                                                                            '20210413:000946.634818:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЌĭƤΔɸҟΚȑúÐӐьʚjǏѥӫʃƅ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9062076278213554273,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'σҸζÚǬàÆµϹȩҫԏƇА/Ԇԭʞҧʂȧʥˡõ§Ԩ½ːχž',
                    'message': 'GЁʶυɈ˱ўĀƔҀď҂ԟ±ҡԈƃͺŜΥɥјϯ\x98ƖʽӺÏƛψ',
                    'arguments': [
                        ],
                },
                {
                    'catalog': 'ĨҭϋąϐԨ˕ƮūœŞѬҐҽɞҀXR(ϐʖҗЦ΄ӯΤϷpҾÉ',
                    'message': '¸μɚˈІXĝϽʕҘĠ:šʗѾɞĦaŚúŊ*řĞҺƿѩЏΒȶ',
                    'arguments': [
                            {
                                        'name': 'ĘǪŦǚөϸ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000946.935733:+0000',
                                                                            '20210413:000946.954432:+0000',
                                                                            '20210413:000946.972356:+0000',
                                                                            '20210413:000946.989821:+0000',
                                                                            '20210413:000947.007041:+0000',
                                                                            '20210413:000947.023784:+0000',
                                                                            '20210413:000947.041257:+0000',
                                                                            '20210413:000947.061302:+0000',
                                                                            '20210413:000947.081057:+0000',
                                                                            '20210413:000947.100400:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƹȴǅěÏʹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6593398229326094461,
                                                    },
                                    },
                            {
                                        'name': '1žŁǣ«Ėшрɦҟ%ђƷǚaɬξHΠʊ͵ƠʌојӴώƚѷ˂',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8850693256436739208,
                                                    },
                                    },
                            {
                                        'name': 'ӾġԧlиӒԪΣΎҒ\x91ƠʦĀɂǦYÅŴɒʶʉˎ\x98oɃϷ\x80C',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1933145881574368408,
                                                                            5932813181442142840,
                                                                            9042917099408444404,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĞdѿŒĲɅ҉҇ŗyѮ^ȵĖʟ˓á!ß˳ɵЋҁйĸŏжėԃЬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:000947.456872:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӸӶʠɥгӉȏʍYϞŇʝ\u038dϳӹӥ˔ԌĲr\x8a˼',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:000947.533910:+0000',
                                                    },
                                    },
                            {
                                        'name': 'οż\x9fæǜɂʊЄɮ͵ǕΆмŀУ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϿʐψˮʡʮͿ\x93Ԩƥ©ɗnԏÃѲѫǭΤuќʧѻ\x91ȧΆ҂ǩƣċ',
                                                                            'ńćԘEśĹИʺ˰*ʚǬŉүʒѧĆƛ)\x7fǌrӋŵ´ȁЉϻгà',
                                                                            'êˡ$ɰôӡͲƤϔĒԩĴĪːŠϜˮ}рЕЮϲŲϜɦtĜʏıɥ',
                                                                            '¹Г+¼ӘѹȫʧƯBӥǷїŬHЫy½ɘҶȊ˹ͰЧсОʯˁԩΉ',
                                                                            'M¹ѩ]ſ|ģƊɹÆEzЋ^ɦƊǡʺƪºƝнԑɡĮς˗ȸàǷ',
                                                                            'ӐġʥҀ\x92ˇʡɨЃƣƌȂ<ƻŶȿƐ˅ϓΗɧ˟ʇȜȍЧtӣЇχ',
                                                                            'ǋòɉВԔјŃȣњXвÖ\x820ϔϕ¼Aˎʣpɝʪт\x8dƍ˲лƎˡ',
                                                                            'ԟҐѰѬ˃ǅʶę˩ĭΜЁ¼ҴˎӬbɕĻкѮȗʃϝζ˲ЂɞȐѿ',
                                                                            'ҝѠͿτϗđøӓғηʒϧŐЧήΫŏȉƙLɉϱŪÿΐŌъūɕʒ',
                                                                            'ѵğɦƍЮj҆ƛѫĕӝɍo=ǑΠʿˬƎԚӒʶ\u0380Ϊũɐ\x82\x9fɛ&',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЏƽқϞԢϵøŗҮɅûъ*Ԕ\x9d˗ʨȗ\x84ѿԇҒοӝŌǵԌ\u0383θ&',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5271489987590031675,
                                                                            -525311905327631830,
                                                                            -1223961577883180105,
                                                                            5200058929146380552,
                                                                            -1850760687240730365,
                                                                            4749540758050231487,
                                                                            7884181430646636026,
                                                                            -499546934150322591,
                                                                            -5924322411541488147,
                                                                            7744649479091045505,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ο¼ʑɮъūCůÑż+ȓѝÊɭʇƧѢȶȤϩł',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                        'name': 'ňȳˬΣåΏȌЅʨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8734677568963751034,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӶUʵɫɞǳƏΓǮĮѴɊ[ГӊϟϒpÂÄÀзѲʫƭЗɴŌҊù',
                    'message': '5ȋѺͼŶǉ»Ͽϋωˋ˶ˑʓǭӂӲқԠƩȣΛԣŻѴv\x93åūŝ',
                    'arguments': [
                            {
                                        'name': 'ǯXʠͷҖĮӱɅӸ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000948.538877:+0000',
                                                                            '20210413:000948.556185:+0000',
                                                                            '20210413:000948.572870:+0000',
                                                                            '20210413:000948.589916:+0000',
                                                                            '20210413:000948.606215:+0000',
                                                                            '20210413:000948.623420:+0000',
                                                                            '20210413:000948.640589:+0000',
                                                                            '20210413:000948.657690:+0000',
                                                                            '20210413:000948.674521:+0000',
                                                                            '20210413:000948.691664:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĮŬȎЯɮϚ\x84',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 737345.0132945692,
                                                    },
                                    },
                            {
                                        'name': 'ҴɽӧķΚʒ¢ѐϰ\x9dǥŏϥȳȆˠǂОӕ\x9eƙǤŅ˔9ͼάЮ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            86887.21836656326,
                                                                            694986.9312030607,
                                                                            143685.24749181754,
                                                                            429490.8749020491,
                                                                            -43473.388312383664,
                                                                            419913.3471642392,
                                                                            149634.37802986347,
                                                                            756705.9605073471,
                                                                            458903.72975935566,
                                                                            732308.9459405892,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÔŤ\x83?©к҂ƆҥɷфW˾ͼÏǞþȉǯΙÔęГȗ˽Ѝҕ`ѝѐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '6ʙĎҀ\x83ԡŰƪɲҝӹˊĝ\x89ϞӥΑȒʇӻÄԃ˃ʧıˊϘϢǃȬ',
                                                    },
                                    },
                            {
                                        'name': "ÝêϡƼґŁϦӪ\x9eΪӓ'É[ƚӝҗŋ£ɹîϚҔǰЋǀϡĚϦԭ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:000949.194414:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ͱ[ȯªɼԏǳȉгĨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            990344487463254088,
                                                                            3905952126311308683,
                                                                            2157018216478955166,
                                                                            -4046647963889148021,
                                                                            2857326238630518945,
                                                                            -5733619955252126953,
                                                                            -8896619955154751554,
                                                                            -2635291065534254148,
                                                                            2251280344435219261,
                                                                            8697368089436487272,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƐеϥЧϛʿ:ѫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000949.653289:+0000',
                                                                            '20210413:000949.665331:+0000',
                                                                            '20210413:000949.677388:+0000',
                                                                            '20210413:000949.688774:+0000',
                                                                            '20210413:000949.702018:+0000',
                                                                            '20210413:000949.715833:+0000',
                                                                            '20210413:000949.729264:+0000',
                                                                            '20210413:000949.742808:+0000',
                                                                            '20210413:000949.756200:+0000',
                                                                            '20210413:000949.770148:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĔǄÄ:ψƉ&ӭȃϢǵѨƂϡҎ\u0383]ɂ8Ǡǿ\u0381ɹˑɪ˭Ĳȫ@ġ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6368264700607446111,
                                                    },
                                    },
                            {
                                        'name': 'èяϺɧ\x95ªƯв\x98μІƭĴΊƴҊĀÖ͵΅ϱÕӷϊЧɂËːƩ£',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˤҔϮϴӊʶȍǛϢЍŋ.ɂѸǤηĦԭѭ˻ҭ¹Ǔ˹ˢє¬ҹι\u0380',
                                                    },
                                    },
                            {
                                        'name': 'ǯ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            623028.5832543027,
                                                                            650769.2278377365,
                                                                            644094.3344347746,
                                                                            151710.19161442676,
                                                                            731352.9512615959,
                                                                            707944.3156494404,
                                                                            244608.9597400282,
                                                                            709641.9794117988,
                                                                            81522.08340616175,
                                                                            -34916.97645525719,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƫй;}Τ\x9cϱ·ġȉɳӦǇ˔ˎϧĀʆѼǞήκǍӬȚ͵5x\x80Ϙ',
                    'message': 'ʢԭƝ˜<ʼЂљ·¤жǤҴҙԟӕϥѫӺȪηʙȓΑʭHǝҜ}ǳ',
                    'arguments': [
                            {
                                        'name': 'Ȅˍȭ\x80ƐŜ#θӎť×ďχ͵оȿϾѝ.ѪȯϪȂʱǏçοɯǀŚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'åȥͳВ\x89ԆƕҜ}ӒԭΑȇûώӵԐƙ@ԟӨʚśƅҜȮȇŞԣѻ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2182366707731921532,
                                                    },
                                    },
                            {
                                        'name': 'ҜѸҗҨɢΉŗ¸μ˓=ŁCŠϔ\x95щͱ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '|еĲ˓ʵĄҕ^ϙˍȵ\u0381ƨԞ҆ɍ˫¬δǴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3898091759518671306,
                                                    },
                                    },
                            {
                                        'name': 'DɥɥΪǔλҴάʯǇȤԀǴČυĳřƚГ˷˜ӁĥӁЖǯň\x8bő\x97',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'xӣΫȼƅӛЮb!ԉ\x93ǴƘИԢ\x8fӹϗМԠʶ¤҅ϪàɈͱOҁz',
                                                                            'ƨЏǡǼƕǶǜm˂Ҹà+ɠòÂ\x9dҪɿǤҝȰҘľқȶ˛АЖJΡ',
                                                                            'ӎƒΎƫРк҆ɸӄŜѽтҎƻŜӃшњȑ@ШШć\x9dӆӤ.8ƑΙ',
                                                                            '҃ė÷ѝɽąȤЯļʑʏƃjνЖ\\ȞͿʇńɴҊąϯҸŶа3ӁƓ',
                                                                            'Ҫ˴Ƹ˂ˤ˨,еƬϢĦċЃϷãУж˕ŧŨĥǾԗѪҜ\x99˝GѾƌ',
                                                                            'ʭˑǴҌʝЭӃĪŃ şє҇ҐC<˪ѲԉМ\x9bʕиԢ³ɬԫ\x86ȷψ',
                                                                            'ΟʊËѺCϴŨƩĲåєȐóæǍЮήzmȳìȲəm1Ŕħġ9Ú',
                                                                            'vϧɁĪ¢ѫ΄ÒƗȧʅ˪ĄԉΖŒŌϐʯůғȕԨǬˠͷ˫ƴϿԭ',
                                                                            'ȡԤЧȰĳξЦƮɘǩƸǼȀÂƲ˛ӟπ\x88\u03a2¬ĥƐ҅Өӽз˃\x7fѯ',
                                                                            'ǣßεĞɸё˼ҡšŜɔ¤ҵºϢΏщ\x84ʊȁ\x9cǈǍ`ŗ(Ь˨éѭ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x911Ȕϝ\x86ãшĴβɨƎǇĭϴǚϋ]ªˆń',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4645500016707888352,
                                                    },
                                    },
                            {
                                        'name': 'ĎǍ;\x8a˷ѪͻԆӔ²Ŷ˾˛ůÕˣМƕķΠVϐьϢфØӐ҅.ʄ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -33803.57357264799,
                                                    },
                                    },
                            {
                                        'name': 'ɸĎɪƅ˾вȦf1ԬȕτЭԆ\u0381Ȃ\u0380ӋЮпŋǁëħ҆ӮHºǹȗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʒ\x99ɞŌȤvͶԙҜ҈ǀш˕ȻȉХɫԀGȝƯ{γŏơÍϩӼµȈ',
                                                                            'äƷӫϬЩOͲѦϬЎӫɂlϺɑȴuNïǅȕȜЧњӨɃƷϫԫΐ',
                                                                            'ÜΑԠǵ;`ҥΉʓŬp£ӉͻЙӺûЙďҸӜSAĝĞ=ˣәŐԜ',
                                                                            'Yɣ!РԦIΊȉñǢƎԈƮh϶ʡϱÚĢӪŭ˶ȷ¨ЃɒоɿДҦ',
                                                                            '¨ӑǱ°ƭĞԐmҽĎŮȵʼǛͼsНɵԭƜҬӆÏÈĊΝãĿЏŐ',
                                                                            'ƵƻćŌʨˮѠÿґәĆYǀҟǫԂɎҒʗĹДϱˣƉԩ\x98ŗ·Ζɗ',
                                                                            'ƥǂAʱӚŷȮÓЊϪŽʈɨѩЖǐ×˷ͰƢɧЎȧƞҰ|ӞœђƱ',
                                                                            'ŇԉƂ\u0383ɒҸԁæǍʔʫξѷϰȝ˒ĪѭʓŮΆσ˥ɣѱȆǄѻϢɿ',
                                                                            'ɴϛĘеϪʁӰοƿûÎù,ɵÐǢȔΌѧƞȨҀ1ŞðÈиâǙϒ',
                                                                            'Ӌ϶Νϯyт`ҸˮfɔΛʐ[ƦʻԍбűӹͶј@ΆȂɲ»\x7fÍЉ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɊҖϕԈbɹġƥҙͳүϑ0əҳCҰԫӳʫǶɀƢУ\u03a2ԪŪɃρЃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:000951.510342:+0000',
                                                                            '20210413:000951.533436:+0000',
                                                                            '20210413:000951.552007:+0000',
                                                                            '20210413:000951.569948:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɥŦИҰɩ[ΎϩɕНԆʲͿǁɔǟҵҪ`¿\x99ŰԔ\x96øʘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƇPљǒѕɋń[Ѭ\x7fǕпƆǮLЬGоΗɮƲԏλԧІƽƗȏÖβ',
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

            'identifier': 'ÞӨǿÕɧ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': "Ɠ'",
                    'message': 'ƿ',
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
            'name': 'ѕΛǽʵĎǿɺʕʩƗlȊЕǎӾʜÜȤʟÑĆ¦DʠʑѮDЫуƗ',
            'error': {
                'identifier': 'α\x80ҘԍΏ\x98Ӿ/ȪƔиɫ*ѻμӏһϽǙƏƵɆԐǡǄ˳ԍ\x9f˶ɾ',
                'categories': [
                    'invalid-user-action',
                    'os',
                    'os',
                    'invalid-user-action',
                    'access-restriction',
                    'file',
                    'network',
                    'os',
                    'configuration',
                    'internal',
                ],
                'source': 'ёˌԂͲ\x8fЃǧϬȸЈнɣά\xad{ʞǉŘů\x80ǇθǍϸƾϮǮƉͳҍ',
                'messages': [
                    {
                            'catalog': 'EƏǴȔǋƻō£lúƗСЦșяɷƹîȍŪĴ\x9dyðѷӳʥќʂǋ',
                            'message': 'ĥʡюΝЁâϏǃʙԣѹǞńǤϳ\x95Ҭų8ϛʝԢşǪҴѐϟƌԢ˵',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': 'ҡûǶƿɦӺϜŖѧȳÆĹH\x97ǋŉǊǇӃͱŜЕƨͽͻȢηҁШ§',
                            'message': 'яѫǍϻɵσĀʍʭ҅ƐɳǨϮτʉȬƖćªџǎТф\x9a҆Jжһğ',
                            'arguments': [
                                        {
                                                        'name': 'ӬΝˬOиƁǝɷңƖĆȧǡӯǫʇɝ\x91ǶϨфɠŘ˷',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 52050.72491193563,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ùɭ=Ѕ¶',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌӑʁ\x80ĠԨΞэɛčԚĕɈˁʧφNӏ¥ô',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'KЭ¸ɓ˻ÑŁÕәǰͿҰΕ&Ҋřŭ˘ʦ˗лΝ÷űɅ˘ëґŨÆ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'əџЫɷ¨ě\x90҈λŀΗǬͼķȔ\u0381·ɋф4р˦ʷƉҦ҇ҊӽˆĎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 536961.0550953578,
                                                                        },
                                                    },
                                        {
                                                        'name': 'N\u0379ҶȌʩ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9cƿăϮь',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000929.543996:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'О·˛ӏƳ\x95Ő\x98ˉƢ#âíń˺ϩӒЃˤ*\x96ĜӫѻӑӠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000929.618927:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɹѢƯLķƺԒæͼҶѨԘęɼˤƨȟԄʕäʏԐӹѺѪʏҁϾŌӉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌȦ҄ʅmÆÉ\x9eΈȽǾȀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ͻɐѸǈǟͶÄbҊȝȩQŮχЉɡΪʽ\x81^Ǚʣвhș˵ԡɚԪԏ',
                            'message': 'ǘѤʤǆ˵M˒ˠƈͽϟ΅ҟPŹĨŪ`ΐȥÔȄDΟɲӕϲȬɣ·',
                            'arguments': [
                                        {
                                                        'name': 'ΉԠϽKÓҋÞԢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȐȇɨϫÏ˳Ԧ-άǛȹϨЛÐ%ƶ8Ӱ˱\x99й˂ҍζӢEнȾ˛Ĵ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Æ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000929.969059:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ů}Ԗǽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋο´ТĹȝàΫңҡMôZɹΙˬú[ҠŖӦĝʰʯŃēҜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҍԩіһЁҊȺБɔŎЦΦǶϜӆН\x91ӿƝȻɍ¾ɹԜԋ˱ȘѬĻг',
                                                                        },
                                                    },
                                        {
                                                        'name': 'oȑϱňȧ½|°ɊɺΔĻÚφĴŠűєbӻӐ\x80К˱ЃØΒƌɛǵ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ДϟɄʋҔŧԥŉŧ͵ҋŦâ_уʢC\u0383ΜĚTʉӐȸ\x94İΔɾϹҀ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɛԃ\x9cҷѸӧҎШȘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5105273815782176680,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϜůǸԙҺЁźŽѢoɶ×ϒ*ñ\u0378ΤƆυTł',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϨАǰЗѦťǽξҖ˱бΑϜèȵǿğϡѨɌ<μɴɺʺћ\u0379Ƿ΅ԥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'PʤĐqǢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u03a2Ӥ˨eєɮÐϺдɤŻůԝ\u038dҺЋе_ɖϬ¢',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ГͱΟɒͻʦƄɮѐңİʺϳÞRҐȔˍ&ηԪĔτ˚ɾĤˁ1ƢŤ',
                            'message': 'Ʈƞ\x8aʆӫŲɴå\x92҉ˋяѺİǗЋʛîӍʶȎëΖʙʉʔԓϟϧә',
                            'arguments': [
                                        {
                                                        'name': 'І˦',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'εӛҪ\x87ǢEƌ]ΦгÕӪҿŇŞǾҡȳӜѯҺӗϡîàӶŝѦȂχ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'У˘ιыʺǄԎǨɢHâ-!Ǹ҅ԡŌŘ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'əʞ.¤ѼĤԂθԃӆо',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ʱ¯ͳ\x9eä˃ʕΙҙвѱÎĴθˁǹĴөƉɇ'χӽȰ+ӇÜŖҳɰ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 936367.1613923651,
                                                                        },
                                                    },
                                        {
                                                        'name': 'UϞǧώҡõ҈ҨʐŻǚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƠˉȢȋ|ШǘԐ҂ĲJ\x8cʓŖǏ]ɕўˆ˝ος˥)¥Ф¶øĬ5',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ųғ\x97óԩϻӲɣӌ\x88ϝИɷӟ4õ&ƶǩбȋχɶȍ\xadψŽъȅǋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѵӎºԉ,ӷľΦƒΔƃӳδѬΛ_ŘʺÏȮӘ:ҝǈɮƿԦԝȠʷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŶŇӟ5FҦǚˋSҁ\x96ҏΕʩɜʁŉʝϣкǨӯòrͷˏŢҳƦ=',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǞŲЇƩΉNƜԙҕηԜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ōψ˔҉ϊˬ>˯',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȩӛҍÃǛU҄ȓѪӕ\x7fԢψ2ùɩƎёȾвŉŪɬΏ˕ý\x93Ěëʛ',
                            'message': 'ʎҐȩ\x92\u0379¢ŞӸіʵƔâʐu¯Ӵd҅ӿѹŜ\x87щ ҺÆƐ\xadʈȢ',
                            'arguments': [
                                        {
                                                        'name': 'ŚҶ˖ӎ·ІˬτѰŷɐʢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǃɛӟ˙ɛ\u03a2ɢʥȤǧғǺϤȸǧǨϒԊ-ÖˍɷѶҎöǱĶƶʌԭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǵĬӸɣ҆ϩëęĳϔɜԙƁâʔԖpġû}ѽЫѝϷ˰ƒʚȯ˨ī',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000931.738075:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'f[\x97ϯəԢџ\x94ϝңǻǦӌΟɺ\x85ԙĨҢŸԮЂѺɦːцȢĨåԃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϓԂɗð ƊtԄΪЃҧŠӤǊѬŎΆҙτ5Ӭ\u0382ΝïʠğȎȇ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'űƌ¹Ė\\9ʋ®ԧӥŕϴş\x82ǡăнǝɨӍŻԇ˞ÊϙкҧϥѺ!',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -53653.33256896905,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԙÛȭѨoИʨΒ\x8eҜÇѱњ\x99҄ԑ¦ˀɌӬŠԣԪԗŭΞƾҕў',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000931.974734:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϕ[˓ˏЯԑ£kԐ˲8ѢǨӨ҃Γ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭŹΊƽĴԨǅɧԄǘ¨ԣǅҷκϥӇźʜƧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ôǎ\x89əпԝâǰɗ~μMұ\u0379ǣ·ĶҦџ˵ƑʳѺԮEӥӣǄЄĥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӁӬ0΄Ӛ˪ǐɨΤϢԭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЁʙəӡПΖ΅ԂӾʦƧQӉΓũ÷ˮМ½ſŰ\x97ǿǒŇȵÈ%ɔŔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4062777822158208326,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'юǎЊˁȾʚΝҩɤQ˒ʏΉҩķƆƇ-cŐʵāԮɴĦЇ˘ĀԞȣ',
                            'message': 'ôɥΉӠʲƃǌʝĘŉǿȺɾHƨƣȟįϬʆЯŷ½ŷǋǂɺϸѧ',
                            'arguments': [
                                        {
                                                        'name': 'ӐpԇȂӪɉΆϲͿ<ĢŝƾÚӓ˵з',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5104078144510154727,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǽǳȃԥCƣҒŝů¹ˆѢɓňҿʺ˜Ѭӂʓ,΅ҘʛþƥԈЁғđ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƴɯǧ\x98ҎŴƔԏɭÜȴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000932.694212:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'пß<¨ĔўˊԝƄҠţ˟ЯđѹΔ4ΒeԎȥĥʨpȜêиϛBԒ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 384078.71298032516,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĴbɌΆ(ččŌLͼɶѵŉҕßʸϽ?ӘϺǛíΰԉɏ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 739980.4642209674,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϡ@ŀYǱʭѢƾƘƹӽn\x90ÏÈ˨ηȷÄ¤Įʹ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '!ҍģȕƢƛîӝºˬѻÆǀˬŤԮъЪƥńԒ^ʜ\x8cɋţҸӔΐɯ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000932.955583:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҚъÈϸĿ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 685804.5737178351,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʟǖύйɲѩD³ϹԢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĒΛŇϒċьkѳȅɴśіDöѮĝǍҹɮÂ¶\x88ҍӴȦƚѡ%Ēϡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 800831.853038148,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˻ƂыĦ΅ªƐΙōé˦Àȩѭ¡Зʖ\x89ͰӫҘʔӽZ˗\u0383ӔцΟʹ',
                            'message': 'ŢǻÃÆϵƕȪϟҕʠ,ϴԘҹкșӣʋ˗ЂǪȡӖʵʅĚӨ¿¬с',
                            'arguments': [
                                        {
                                                        'name': "Җѻȥɑ¢ȲJfʁПӭǰȊΩ·\x9eϊǦ\x98ʿD#Хғ'Ĩчuq˧",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΡʽĽƉĹșªɁJy\\ȹΣнϮÇҧҨmɎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'лӠš\x8f\x9fΚҹĻőЕЮʔɜΛʔŞԀƆϔXʘİӹтİɵԥЇș?',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƱХУƜ¯cˤɠϵ\x96ҵł³YǴͶǅÒnqԋǲҼϨӏŝʑΫьƂ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǿ@˄¯ӓΓgЎϗ®˝ʬGɌLюwɄȲеʥfҶÖŸ\u0383ΰ\u038dиӴ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 860817.9938693134,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ПĞԉɕZҦԩɯѷΗĘˤЅ@ȑԤǓʱ¬',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 332891.4098276799,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǫԝ¤\x87ǿσřŏ(}ϗΔұơϋ˺ͺ_ː˺ʓаПĽԍԄƋʏԙ²',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'лԖ˓ԪɂДӛιȿϜȂˑĤĻɨʞʴêѯϼϪ҉ϊƞӑǓmǞɊͿ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӜˋПѯ\x9f°˅ӖƫŷǤѠ!ӝɛ˂ʘԙӀщ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'aфеӲǮӯѷԧMϨͳԔʚɀЄ\x87î\x95ҍ¿ΖŬ"ʊãЕӃıϦϔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽĺ¹ãʶѮÐιƕɼŀɛή®ÇƷ3ҼǪҧ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ɳԙԉӺϔΒ'ìίɇԥϻΎҳΏо¾ýǉΫӾѹöʒŕҜφȍĖГ",
                            'message': 'ϥԀ\u038dɊǈ\x90εӐŊʁȯԐ ĿжԧʗʭЮþǱƥˎʴ»xêĘΨȚ',
                            'arguments': [
                                        {
                                                        'name': 'uȈ˴ӫЦÎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000934.234256:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'аѹ>КŁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐл˗\x91wʊŪʟ\x84ŝǶˏŵȄĐýʦǘϜԛQԎōͶɾҨØ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯ&¥ƨӓWˌˑŖÕηԗ>ù˫ɧȚŐ£ĶȏʶӵKÑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '϶ϾʩӥΘ\xadƻ4ӟȈɢĀJŶ=ϬȖųҏşЛ˴џЉξԧӏĢďϳ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƊǫƂӹзԭʪƪªгǮʱX:ѬüʣǳЈƮ΄ϼРѴ˄¯ȩʤӚǖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000934.569829:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѣ\x88ҏ\x92ȈҝˋλƻϞǓӾ\x86ȼŕʆȡƨuĺϓɠȬҎɆԃΜǁ^Ь',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000934.762038:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȤћѢȊW˴˥ɑϑѱģȒƋƓ\u038bʟƩѡģɼĳѣŨҼYǷ Ǚģҏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣ"Ҧɽųӱąт',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҧԦҕȽϬƫҾ9Ǒ\x83ǅŌ\u038dθɤУn҆Ўѩ\u0383ӠȹħϸҦųӂϷΙ',
                            'message': 'ĨİиЄϟåϟВҮ˪Ü˔ҒɷԮёюлԔЏηɜǫθAÒϫçηΓ',
                            'arguments': [
                                        {
                                                        'name': 'Ǡ҄VРȒѹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǔƜ4ǤǷʽǧĝbϿkāɚĮŷƐǸƲħǒ϶_ʖPӗΥ\x9cɻΫӒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000935.178096:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϞˋŃƻɎȰъǯϯ϶ŷŇĪʦõқ˧ԁŌκƢʍɿԄäʌѝ\u0378о',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000935.247830:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӧôͼι',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱǡӮƮσʫѨЊŃӊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7997744328757154447,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ИƼˍͱԧуĦчìϲøɳзРĹЖȉʪрӜàÅѮ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˧АιɀE\u038bʊ\\ŴεÎŗJƫнıϦɺʋɗ\x95aϩπͷɁŴĕͰЈ',
                            'message': 'ΨȓΣɃ>Ȭîт¶ƝҭĜ!φȗġŧ²ƼɌѥϳЫǲιĳїСѮХ',
                            'arguments': [
                                        {
                                                        'name': 'ӐǞЂΣõʑОΝϕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 389705.4587631245,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃƬĻʯˢϕϬϙɼ{ȚһʁȖƇư×əŬʙ\x9eϧʀȞӶʁӟүϴȎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 906092.8195037433,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ωϩȿ҆tʏʹ\u0379ҙҥѥΐϜ\xadǇϓ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -78943.05843216642,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʍԜə¯',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϗʊ¢Ȓ҅ƱʑӮО)áӗӆlƃ˪',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1160877216628425377,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǔÐ˔ʈħӄɬɠǎҹƋsʻǢ\x99)ϑ\x9dѓμΙ7ӴȳDǤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǫͷȕŊȪśԥHҁ"',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:000936.015620:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "˶Ή\u038b˶q¡ҀяĘϾÝ'ίĂ˰ǯҿŖ(ƀțİҝǵUşŬƥAˌ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˬΚúŷŷdѳÎʰ˾Ѷ҃Ϥέ\x8bӼ{êȧƂȔ\x9fǰαϪͶ˟ɫɠҩ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6701228341690340821,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵΕĝпĨȦԫЬǐԩҵ\x82ї',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
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

            'name': 'Ĭ˳ɟ',

            'error': {
                'identifier': 'ʄ\u038bґĘŔ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': '˺Ɍ',
                            'message': 'К',
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
            'event_id': 'ŒôԪδҠ˺ġŮДҨѮɞȦЁΖϜҼ£ǞƄ͵ӹ\x82Һ>ё˄кʲӗ',
            'target_id': 'ÍǹƔɯψŸųģϧӺЌʝƍ4ćнș˧ň¬ӷĵɯʪʐӵʨϖҟȨ',
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
                    'event_id': 'ʎåͰӌ˭ˮѝˇϓӃ_ʉWƤёҀàķŪƳĒѕȘʐԜЋΆĕ҅ч',
                    'target_id': 'źΆќα\x7fÚĭ҃ńyȷЂƎoǙȱ¡ʽ˥¶ĶǜɥǆyƔԨӶйЛ',
                },
                {
                    'event_id': 'ơĆùǖǝԭǨϢϝϩІöZńĐҎļƩW0˃ΝͻɽưƼӂˋƙʹ',
                    'target_id': 'ѕÆϘʘxӐőƁ+ĵϔHΫ\x8dӰƏԉ͵ȍƱ¸ìǹʡ˅Ʊ\x84ԙư˃',
                },
                {
                    'event_id': 'ˇŋȿѓʝ=ԡ0ȦˌԗyƮɁКѓεМȎʐѱɝͽóĐZӫĵψҟ',
                    'target_id': 'ВÕƿɺķ˪ҵȎɁтΧĆυӓςҿϼɹҞҸǲ҅˽ĬŏĞɃŽΏͼ',
                },
                {
                    'event_id': 'ѾнѬǰͲθԥϠȟԧO˼˵ԣй7ƢΟЋǰлßĺƬ\x97ÏĝŚ^А',
                    'target_id': 'ƚȉϺȑåϾ˃TÎ6ſԓξėӑǆ(ҿʦЧӧͱŶɭԅύȒƟӱԅ',
                },
                {
                    'event_id': '·ΏӖӄ˕ƔēńÓɜ2ԖвʯwťϰRәĵ µÜ˙ȚȱеˌǹƬ',
                    'target_id': '«ԩϓΰυ:]ʰϰЯȧƴ҄÷ϕҵϲνʊҫIƇ\\ƃĉɌКȾΠ\x96',
                },
                {
                    'event_id': '*aǡќǏ˶ǰȄȗdȂʅƳѝÃҝǟŗïˈѪǜҵŖɦȺƏʏ²ƈ',
                    'target_id': 'ìͱαͽɈ5Ë˺РȼΓ"ԄɳŷЭʸ˼ȼϽёоȶЂɞˉŁҹ˾˩',
                },
                {
                    'event_id': 'oѱОMæʓǢγÜĸƎˡθĤʜÓʥϊ:˒ēдѝƪƱҠ˶ȟ?Ƣ',
                    'target_id': 'ўШӭǩҚƔ·ԫ¢0\x7fӏλАӛ\x86Ǘӱ\x99ĞďÝԈ²γΑѴȨкƶ',
                },
                {
                    'event_id': 'ΐӬÞʙǐȝǊǄĴҶԔʆ˖ˎ϶ēȪƆϣ\x95ѵƖü\u038dҞǲОԦЮɼ',
                    'target_id': 'ʕӵj>ҺǼϕƚǼ.,ʇœʡϐʘӻ˸ϫƾԕ҈ԊӋÊȉüѤʇÇ',
                },
                {
                    'event_id': 'й˹ΊƐТҏάǟ˰ώӾãǫҡΣʔȯқЪк£ͽ·qԙm¤Ѿǧ4',
                    'target_id': 'ρǰĦȨʣķRӥʸӆÏƕb\u0381Ä¨ȚÏ\x8dʻƧóОquϞΤÖʔǸ',
                },
                {
                    'event_id': 'ӄ&nÖƈΪŪÀŃȄ¹ьʨЖȓωυїƽπƥȮșR\u0381Đʌԍӄӳ',
                    'target_id': '˱ȪτϸҚ҈НǙřȇʩѷƥ(áӟ˯ԁǏΘ«ХXɞ\x95ъ°ѴˣѰ',
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
                    'event_id': 'ĆƷĝԥƎ:ƳäÊʈŭщɵʈɮǫҍʏ;ͱ~ӎǏǸȽˇϊĨ\x8eȷ',
                    'target_id': '3ʞɃьΞѲӦĦ\x8dӘʓҼ\x86äʜŷ˓˹ЊɥϾȆӶвϞÞ¶Цɂѫ',
                },
                {
                    'event_id': 'iHӺϓĴŧЮΛͺх¹ƧȤƚϫԊ\x8b×ЖŨġțĈʫѝø\xa0ѷͺ^',
                    'target_id': 'ȇҽɝRώ½ӾѻˌʠҌϊĬN\u0382ŪѡĈȌıҗф0ӭХэωǹρʑ',
                },
                {
                    'event_id': '҇ӗјŵŇϡI˞ӥѴԢɀӺбEҽ\x90Ӡƾư͵ͿɵРeϼеӨȃӐ',
                    'target_id': 'ǳʥѦ\x91жŒԫҰŨӌζƎ\x96ēԛƠͼϜDŖ\x9a½АʲǿAϖǲĐ´',
                },
                {
                    'event_id': '[ϐθеѐËљ\x97{Ȗů5ЌʙçÞа\x9aҞʺƄʏ˚Лєɵмкɦɕ',
                    'target_id': '˔ϋԛ9ʕŭĤuˊѐЈϋˎνÎȂԚΜԜϋӴϋоÿ©ȏɑ{Û\x95',
                },
                {
                    'event_id': 'ЛΔѷԏϻ÷ѵăгȺ\u038d\u0379\x87ȭԥþ\x89ŷ\x9aįО,ОƷҥԪԎͻùк',
                    'target_id': 'ϒĥ³ǅϨƵģȟʻиʹɯШÒħĵҥâȵ·ǈ˯kԧ\x81ƈÁɹȨΘ',
                },
                {
                    'event_id': 'ӲүɂѫBпǣҨƕʺӈ\u038b>ҒɚӈȣөəςÉϏʱƞϖɒʫȸʄġ',
                    'target_id': 'Ǹ˯τÀӠˋĎ\xa0ȋɹȇȘǏs\u0379;ӴLδΙʰѯd͵ȺɴǚŜПД',
                },
                {
                    'event_id': "Α'ϑ÷ʖʯɘʫĎԂóƔӟȉêĀҜǿЮтϦɽɅƎěȐʿǁҊƁ",
                    'target_id': 'ϸåӴѼÜФ5ϏѬ\x92ѨȷŃưӑǊпÀ˅сύˑĻϘƨϟͺɓνʄ',
                },
                {
                    'event_id': 'чҦԫîÇÊŖЀԄßäԍҳԘĂȻˑǃëҐȥ˥Ŧϴ·ОӚŒˈУ',
                    'target_id': 'Bťǡґ˼ΙӉǌͻİԐɼǔƄЀѣµгÆʑͺſȟũƍƭʥ˖ý',
                },
                {
                    'event_id': '\x95ȫųȽӏʴҥȳɘʏǨѾҔ\x8eǺʒ±ˈѦԠƚęҎΞɼԨӫɫ\x9eҜ',
                    'target_id': "ρˮ ˑ˦ɶ҂ƶЪȞɤӗȮ˴ŨțŃ'ũГèөЫ©ǸΜŉƄƻԟ",
                },
                {
                    'event_id': 'pЎůǩŐɂԞ\x7fǗƺƛdĀõºʦOϱɝUʓ˗ÕǡűƱͻ;ƞц',
                    'target_id': 'GӴ˟Ҙԋ6ǵƔɴљͼÔԜùюϋѺʘŖʹʇ\u0378zҠɱʭǟЍԙʡ',
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
