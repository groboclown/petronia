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
                'ąķηԒжѼŎǈǚċϫЭѹ|K]ȮӂÙУŏԝЧѕȚ§вԘĝÙ',
                'ǶˎӗŘƪҹӵȡӄӺϱWĬȌ˒ԙŝѫÁЅЃǟϕŢʇΓƿɛǽ˰',
                'ȣSƞƠԥʉ˽ϣɥҼ½НӼȈʵтΖÊԚďвͶʻvíɂѕшΫł',
                'ҵʝѱЋОƨ©ӾҼ˔îҋƦѳΝǽсLȉ^ԕ҇ѸŲä˟ϱԆʏҲ',
                "˨ƋԈˍԝс4˹őğʹ}vĦ÷ΤԅaƶŹʍlΩщѿјĄˤϛ'",
                'ȣԗ{,ћͺʳȨǊόDÎǧĥηћŞɚȖȶқӜƵ^˴Ѓ\x85Ԯėd',
                'ɭ˒л϶rɕȐëϒЕʐΝȪі5ґʞЀUҭöҙπξʕˮýǒÛғ',
                'ůǢ˕ýʠøӆ˷ӻǗęϾÔŞ=`ΓҶӫΎ\x8bЂȘōǓҜҶѳӱʓ',
                'ɫӗѬӽҍȭδƹŹԙʶ,υ>ХСΏЛԙɂaҿѨˇñԅ\x88ųȳʁ',
                'ƳŕϲßрŧŠȔϞǏϡĘŴЈϮП:НπӈǪɧɾ˫ѢӭȂ¢ԡŚ',
            ],
            'source_id_prefixes': [
                'ӧþǡɧΪ˖ωw\x9bǱ`ǽҨȗ˵ǼPȏҢō\x96ԗϬƳˠθʡȹћĿ',
                'ԏƴѰ\x98ђԫOВƅ\u0379ɢÏңʮ˞ѨªǣХɊ3ѡđ˼ĝШâɲɡ˱',
                '0ԐүˊԔȶΞϜӑȤƵɡMȶˋҼЙHƑȢγƟэģʃɼ˃ˁӰҷ',
                'łƼˢ\x98ĴϙƘʙϒǮǨҥǰħ҄ɯγҹʅӣ;ɮUɝ΅ÐҖȋ¯Ԗ',
                'ʿҩӮѴˆ\u0379ȼöһѻԊӉèԔɠȿŰ˶ņªВûӤìӌτÔШZǄ',
                'τԭѢˤĖʠ˝1˅ʈЧέɍ͵àŃˀƬ҄Ҡ<Ȯơιá4ҔĔҘÑ',
                'ɇҧlɬӺҫТƞҦιʨJĀϤÙƱɱdϚѼÜĜʹ\x92ηΉ2ȓʋǢ',
                "ɑįɿѮЦҦэűçҖӸϱ\x96Ѯɻǟĩő˘сΜʭˮњӼ'ҡϥєu",
                'ˣӨԬӡӔ3ļǖƒƜӛ˲ħaǢƙũцʢà\x82ѦѡěÝϿʥʗȋƖ',
                'ѩāŴďЍŴ˶ʒ\x91Ɏ\x81ӆƬmɢɦМȑʹɫŹˆЃąїnĜΖÆѐ',
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
            'action': 'ǣӬԭϮԩ\x80:ҪԩʴɅԓӅѠĿ\x90ɇӲҹΗӤWӼΊŌӥϰõӽɠ',
            'resources': [
                'ŰĿʠϡ˾ˑүȕʂϽǩҏŭЊԅȔƬԏĚĢѺАKÆѮßǃƀǇΪ',
                'ʍҚӼƞʢΟͻғ~µ˓ϨËԀϿʇҴłșѯȰŻǌҀ2ϖkă¾Ͼ',
                'ıïÕ\x8bЖВÓ\x90ɧ\u0378ſǙ¬\x9cÑʼÙİˣϨӯ˺ƿʎѶϫɓƿĥǃ',
                '˧ˀƚʟɲҏɷǲσԑˢ˼Čη\x9e˳ӌÇƫ%nԪƒΐʍˢÆψəҤ',
                'ȸɞʴδФǵԁʺÔŌԡƎԎϚЏǎƠԂΐћҞȪлǮͳȹоƖԨ#',
                'ЗȮÃöΞğȮȖ^ǹʄɆҔёYѭĖӞǀ\x9cǙ©ɝſĬƩKÒЮԏ',
                'ƻԂӀ8ӰЃΦ҉ʌ¸ųƟ)ΤυƊħҊΜѬωΓôƚ˱Ͳȃ²Ȥŗ',
                'ӗʳϮԡÉQɔӥӆ\x9cϦнӷŦƝʈэѲ°ŶяΪӎ9Ŭ˲˃ȓ0М',
                'ϦǄȌň;κǕ˩hEΓǨԊ\u038bӓАѽ\x88;ȂˣOȎ\\ԌźɠşԧΩ',
                'ԓǿ\x91ѦɫЅë\x83ѕ˩ɆτƙǦ˚ɗɭԑşӌñƲś҇őԇ`ôę¨',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ł',

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
            'name': 'ŒĀ6ҌʿϑȡήªƅȇďìͰʻҤτы˖Ǹž\x9aȫԏɁϠĦıɈP',
            'version': [
                -7299426777683480587,
                -2124452718224790967,
                -4793883813589074402,
            ],
            'location': [
                'Ƞ_ǉͳ\u038dӋƞåЪюʱӦɇȰqzѲƙϼǰɈʔǽůǘѾgŚʘѳ',
                'ɑpuӁцȞЅΙäʏȥΙ\x9eΞǑʢӱȋѥȊĜȋӈҷȈzņĘƖǑ',
                'ήˈəʊӒΘɜͶǛƪЉѨĆΑЭɶƽӸŵЈȮЛҒǪƠ¯½ɌζМ',
                'ýĳɶǘ¢ÜӞˎӆŉŤҝεɋɋ˃ː˶\x89ʹŊʶγңƇ\x9fŢ±ʁŷ',
                'ɸȉҾҮ˳Щį)űȆЄϢĪșƆҷΜϟ҉ŲӳхĘѻͻȅϛέơ3',
                'ǏоɛY\u0378ȅ»EԪнͰƜɢ˵/ŦˁοǎėҊȻÚԄˎϟÄӥ΄æ',
                '\x88\x88ʣʏʪҥʹ\x9fјȘФɰ\x9fӏϟHөOӁȹ\x93ŦЅĳǭȓγҡÇŃ',
                'ϣΆҳʍӢƭϽԢЄкǂĤΆāԈ҆ʧƣԜїθǗӢŕÝҾ҆ô\x9aϭ',
                'ÓҭŬѻėБɏɱЈɈǄЍˇĢɮԕżˉҍͲ˪ό\x80ÿƶГ¢ҐƥӮ',
                'ˠ˃ΠƊ˸ʅ ȊϛȔˋ\x9dЭοƝ˻³ӄͺ¬ɧƅДΡµͲiɿ:ȥ',
            ],
            'runtime': 'ҕͻǧćτȎAЃ˱˵ÅҦ?ϏѕǓ¤Ϫӂƞѳϔı˴ɖ;oĻϠƹ',
            'send_access': {
                'event_ids': [
                    'Ţǐȶìż\xa0ϓǕǡɸС˴ŇΫƩƿҜѨκɞŠƈǟˈÑЃϝōƥÊ',
                    '˰\u0378ȧ|ʆƳ\x9dŸ2ɶKчҪ0ԎǜѶĉʜӕŮrɡȓŮʠ\x8büˏЄ',
                    'ĿłȫȧĈȻΆªӕ|ӏŝЏїҗʵʆӿӦʒӣӦӜɥќɮѽ˸ǔȟ',
                    'ŃʴǵćҵҨϬƂϺϧēùγӬӈˉԡË|ϸ¶).λԖʑҩźgȉ',
                    'ƔӑԢЀˢƁχĕθƮϋÆΈŲΒҮӧ',
                    'ƹѯőȄԢ\x9aɭfı҆\u0379ǄñǎӄRǬƃ2˚ƷρҒнĆɱ\xa0ͻøÒ',
                    'ο\x9fӥɬҾWΆſʃɄO\x81Û˚Ƀ\u0378țĲȻȒϿʟîΆ˹ãJҧϙǾ',
                    'ųȾǾŜқԜԝ\x99\x82пΣЧζπǱЅʅ#ΚҽĢЗ$˂ʱĕĆʠԠ˛',
                    'ȖЈƴԫӃƴɰČʚçы0PСěͰͲǽԈ`ǷƟːΣNʶɌԆǩ)',
                    'çӅ˃ЊŠƔІԜϚʯ²ԡȼƥģ\x92ƓŰѓǢ\x84ƯıȶɘϦЗƱҠΣ',
                ],
                'source_id_prefixes': [
                    'ȮщԢǾТļмȽǘʏʎ]ˠȳҫǵȟŵɩ©rРӨЅϱʭaӜίȤ',
                    '\u0378ϨɪǽĹT\x95šŕʍçСԄɹƱЃèǨεΐԙǭǃĦõķƶɱʖЩ',
                    'ҏǧdËÔƵɓѥļƦȇ÷ʗJˤԝΡҀÀ\u0383\x9dԆ`Ņѯ\x7f7Α˕ʲ',
                    'ưʖӀéΒΏȌŹǲϜȱѩŵMӒȈјíǹAǺʇҟñƹˤӌRζȾ',
                    'İ1ţƐѱеǰŋȷƀöАɃĦҍǎӼϰҫŹǕ˚ІφԊ)˼Ʒŀ˪',
                    '\x8aІԃˀʤŅƉѕįѪǱȠʪ\x7fЫ\x8fҲи7+ҎгѼӈҫǋȺĀԊʎ',
                    'ѓ˄{ªЈơ®&5лǅσãιЁfįӌǂƃǌгѶœɱȁì',
                    'ϤǬŏȌúŖɝґЧɠοʆǎǾøĪ÷ˁǍүҹɧӹɮϏȗʿσąӸ',
                    'ºΘͶȈǍbΥћʚϨӔƠіʄѝgӕǓΠΒѹӦ©ÒɽӅƞɶ_ő',
                    'һƓ\x81\x85ġʍ\x8cЃŇˌ҆ϥ|ɶ˹ǇЉųҦ˫ʸΕҿҦ˅ƥΎŉʵЫ',
                ],
            },
            'configuration': 'ŰIжŵŉǌǵҝΌƆΒ\x81Ñ×ƔļҳοӷȀЋƞТͼҿѦӰԨэ\xa0',
            'permissions': [
                {
                    'action': '˝ˀmǹΓԄӌǮ\u0382Þ',
                    'resources': [
                            'ǐɋӽŘʷÉɜƋт˼ȆÀΆţőЛƃӳǈɵÑԜȦӊɠˈ\xadɷΟΐ',
                            'ʶȶzЍđ͵ЎϨəƲÊѿȋҾԎбОȍ˞ӖпɝҠφćǿŐѶњж',
                            'ƸØ»Ͳ˫ϕƐŌxǋҸjӏɽÞȓāʍÙѣŔǺ÷ˑÙȄɼҳЕƠ',
                            'ϪКɮćЫôùԗȿБϟȹɚʺБȝǜîÞ\x8b˾ǇɢĔƚĒЄ\u0379Už',
                            'ʑ\x80ћҙӌҝϷԂÕ»ǿӁbГǌÔӂv˚ʫйȮҨӷƛϋѬʚä¹',
                            '7҂ҋÛȧҾ·Ƽϻķϝч3ǹ˂Ύлԩ_ƠƤŔʊğ˜Іͺ¶ϥҷ',
                            'Ѝðіюʡ˶Ҡǩв?ʉːǮҚ\x87ǱƩÛʭˎȔӃћɱ¡Ҵ4MԓĄ',
                            'ÈӃɫbϜƓɌƥϿDӜƶǈŝ¶ƂӗԍϿ͵ºĢ0ƩҘѕӼΜʉȦ',
                            'Ȕқʅȴԉρϫă˚ҭXѹ«ɉżƬʜɼ\x85ґΥәNCʮȝпˌǻɦ',
                            'ЗIĤǤá¶Ȃ:ӶǇǺɇΣʐ҅үĸхЃȻÌ϶ĒʖôИɿ.ȑг',
                        ],
                },
                {
                    'action': 'Ǆđó¨ΒqͶèй"ˀŵГѲƋƶń˩җαςωͶϱǘȚąʍcʫ',
                    'resources': [
                            'ҤƁ\x96ӗϹ¯љƯ\x86ΧӮˋĝӻʵeҋ',
                            'äʡʹ˴ӠҚηɃƽ˭ŀθľÛɒϝĄƵȸʳNʥĖƀ\x90ϵǻȈрѤ',
                            'Ƹζ>ҶűĤʡļӳŬљĭĨǉ8ķжȞЌʩT˼ЅԓŊ\x8eǽ\x88țƧ',
                            'ĸ҈ʉЮљζ˺ѝūǶWǈӯʇa˒ʇȡEҏΒυ:ҭǅҚ+Τӧǭ',
                            'ІĭåċÎǽΤțȡʴȹη˨аŻʞӉɀΥ҄\x95HͲӾф¸ǅĩäĄ',
                            'ŘɈϡ˖Ⱥ˓ɤӔ˓\xadԑǵҹȠz\x9ańьƹ\x9fԞӧЛϾ_Ѣç\u0382ǕԂ',
                            '¨íˢʉԬ˗ΥΔÍŎѢÿͲșȖŰθȸxȝµϵ\u0381ĬǦУgȰҐԔ',
                            'ɪǛԎюʌΗΌĩа˪ʕʷӓϨʺІǦʘΆçʮ˶˂ʢ¨^\x8fҡ\x8cү',
                            'ñȩӎԘƉΣ˨äԘԑ΅Яȋ^ΠǀчğΨѯ˵ʧÌåФİБāěε',
                            'âԛƞʬʿҡʩĵӆȳ©ҀҵAǰ\x96ʃƨʳӖ\x9eϡuǾоǡǤ\x95Оԟ',
                        ],
                },
                {
                    'action': 'η\u0379Ҟ˳ñΊ1}ČЎʬɨӋϛ΅ƭѷň˺ыӛɆŻ\x81ӎȕӼġʣ¿',
                    'resources': [
                            'ϚљãԏʤϱăƢϰ¼4ԤQȨƛϞ§оȏų\u0382ʾϨǣ¯nʏϲč\x7f',
                            'ДϠϰVTǺŲ˙Ƥ˥ĬДɴѮÆκӎ\x8aɵø\x93ͳ˲ҥѳГŘà-҉',
                            'Ǽ˚(ùɯǎȫΕȍѯƷϯŋʅƲҏǷÄYωɠ~\x80Ц҆εΘѦрș',
                            "ѓȥßϭҧеAˠIȵϻíӱʢɟ¿'ʎǙǜȎĭȽӇɂʮƳʼj\x8d",
                            'ĝœͲʃϻ¡ȪϔĊŭɈ\x8bĮʮɑĽ=ʱԄΓӳǒйλȃǤƭkҨ-',
                            'ğ¯ǐȵŻϯʟūЍϺӎΣʷȉȏʮΜЃΚȸ1ӖӔ@Ō\x8cğ§ýΉ',
                            'ŶҖє͵ԊȥлҎũȻqȮɧѳĤҬä¸ԦÈ¯ĵʝ³ȍÈҸǎɍƴ',
                            'ЈIR˶҃ȫ\x97α£ѬȣЍ˞ԮλξĔɴQЊϬŋʤέȴłǐи{Ľ',
                            'ƊƫҟƛҲѬ΅κʊьϾȉϙϨŎ[ØӰˠ=҄wӘҖĆICЉдӁ',
                            'ÿϤӷ¯˲҃ӻϫʴŚ˔\u0382ӂ©ҀǆϹȞϮ\x88Ǆ\x87urȐ˲+҅ӥƳ',
                        ],
                },
                {
                    'action': 'ʴĀѰӎŸƔ<ԃȣɋ!ˤԦԢžƋ´сԠÊиӑ¡Ҵ~ˣϥTђѿ',
                    'resources': [
                            'ԫЕ-ȌĲзaЪǺѰƾӉ|жDĮҫƷөɑÆӄҪpэǚāȊʙȶ',
                            '˝ȭѾӲҭͲχ˚¶ŰĚˏĊņºϷΎ\u038bцɬɄï¸˽Ã³ǓΎɰɅ',
                            'ZӫʗԡЛ\u0379%êƺɷӍXſƿȪӲ¦ŇōЯώǕԅbĶ\x8fŶˡťʰ',
                            'ŉГкӦÖgϝҕͺςѨșʾŘзvКиȋˆҐ˰ҍJǽЬΪЎ˾ȣ',
                            'ʚԛϼǷŬҒș˵ʅΝМcрĞťѻΪѹ\x82ɿƱË\u038bФζǞӥљѥš',
                            'č&\x99ƆӒҡϒʻеιĕˢ˙Ȋώ.ΨԓѻêӁӻ˻\x8bʳǛқкƿЯ',
                            'ԃǉˎǨƇɠΪǙȟ¯\u0380ϰ#\x7fòκÅŢǫΩǒʨƖӣϞϢϧÊ О',
                            'ɏɩŘύJʃɤϸƨӄҭˤˤχĒĞɵĉӏϒɑÃǧƶ®ͺϨĄɖǻ',
                            'ǛΏǼϨȴЊȐӈҁM\x85ŀkБȝɱӠņόʲĝř8ҥŧѢşϙΔԁ',
                            'řјƟϯÿʜӅϟ¼CϯǇƯԀЇƆŸүҁȾƓԧ\u038dͺӹӢƁɕď¯',
                        ],
                },
                {
                    'action': 'ҽӷǺ®лǃӪϏˉӉþ˃ČƵś*ÀȽį&ΩŁљщ¥ϨҽĆHʖ',
                    'resources': [
                            'Ϡ\x94ȲӅÇAҼêʉͱ\x84ӷ҅ԣ˘Ӽ˩щɈʟòȉюΧsM\u03a2ĪԝȞ',
                            'Ҟҟќ˷ѶϷðľš˛КϊŠŤӋ˥ӺЏ˗łШʢÀ˳£ԟ;ȟͷû',
                            '˶ǼԎʀҡͰť¸˳ʻ&Ȗǳƀ\x8d]Ϳùдøͼ¸º˸Ԗîˇϑɹʩ',
                            'ћѸ˺ʍӪ«ʉƇKȞЖ˯ǖԆѹӱBǅ²êɍʰҍǣǅсвкȕ\x93',
                            'ƆέŞ#ťҳÐɫĝŚĶǹѕȊЯœÿҜřʶϣφϸɪЖΌњɖЪ˨',
                            'ŶΫΞȹҹʗÖƍϊԁҘЖͺɦӅϿϽþϯʬáѓѧҡʲ\x9fÆʪяҴ',
                            'Јɕ˸ҊƶĨɩ˚ӄǡøǈăŅґԖˌ«Ǩqƙïņɕ³ķ9ş=к',
                            'ʅʆǯєɏүДņ˷˚ɭӮмĚΩһĭʨљ\x9ftʪчҾ˱˄ԋŧƧŬ',
                            'ϙҞȏӅɽɇˈ5ʾ\x81ʂŽ\x86ɑ\x8bèѷʫ˲ǄȰͰʱǟҟȡîɖ˨Ϟ',
                            'СϒɌŶүΒȑҾ,ȭKҴɃƙˋǤɢм˷ӸőЀҁϩN´ϕīŜș',
                        ],
                },
                {
                    'action': 'ҏBυӚӐаSӡƙȔŠȮΦƦϫӹƚĩ΅ȲȰӼ\x8døȔʊӢĨƪɮ',
                    'resources': [
                            'ǺͽÅү%1AWkÐ˒\x8cĉƔȪӮɦɀϠ!Ӝ\x83ȶҠʇǤ%ǽӥÔ',
                            'ňӅȻ#ŏҟ˒җрӨ˽ɶцź÷ϡŢĸrχʙǚюχřϐΫˠsǣ',
                            '\u03a2ƭƥҐˉеԬĦъčâÌˮӤҪԘbӆҵǡӈҿԃǲКʰЊʹәÄ',
                            'ÑѫǃԝʲӨԪϪΛҍ\u0379ЀϯţӲʜњ3ҮǱǇ˄ӸŇ¡щɁɼˊʨ',
                            'оˇȆйöӓëԑȐƬ-ѴѮǻWȐþ3ϡэħFԚÑǠј\x9dҊɨɨ',
                            'ʭHǔɋ˦ƅҔŬΪьćǫƣɺ3ΖҺѫĺɝɃξƯŐҮPȺљȚό',
                            '˔ʐưρĔ˕ɟąƫӤŵfӤΟĢİԩƠĩ±$ԌҨԖңƭɀͲěǱ',
                            'ΑʄʱԪΞƜȨЁǆԂwĈΰԣɦю˄ҏƆɆϙ3ɈҤǙʕŽǧ˛Ѕ',
                            'Н͵ªӓɭƻҿԢ˼Ҳ¹ʶӲҵǾ҃ÎļÌЁɂԭʵő:\x9fҭƧě˽',
                            'ʆ\u0379ķǣǣɐʯӬςɥɞпԉʮԑаöΚ\u038bϼěiʋҫĦÔTȓȝӀ',
                        ],
                },
                {
                    'action': 'оˉҙǫφԗҡŻɦLЪΧ˳\x93L˳Gԕǋә\x8dԔѣњδYӛ+GƑ',
                    'resources': [
                            'ҸŦɯkΖʶ~ǈɮǼӯ˅ҹđˆʔϭȴȿтȋбβàˠнȀĚɰг',
                            'ϩƹQȍтŕ˙ԔÍ˒ԘӒÝ\x9c1ƒʦӁʷĺɬӋͷ҄ȫӝƙ˚×Ԯ',
                            'ʶǊÝǇǗĐԛЙúʴ',
                            'ʣϘξŢʤѧ[˫ΚҸ˨Ė^ӷģĵϺϞԆnԊxªҗjòŋЦÉƓ',
                            '+ɗ+Ł\x86¨ƩɅžУӓǕǌЁÉ¿ȭёʬ.ӣɿҷжƝzάƪęÁ',
                            'ôͱӂȿцȆǃмуƊ΄ȸoʉŦˊǊңOчƞêӎŊƔƂԉØĈɒ',
                            'ȯҹШʋvå·íͺхħÊЋŤѓ҆ԀĴЈéŒĦ³ÎҼɏĄϝīϟ',
                            'ϏБԒÄЭ=șӣЉҮ҇KɬĠТҠ\x91ʩƒСƪӬУхĎǅжCõӉ',
                            '\x85\x97˥Сȗε\x7fȵǧāЈϢǹÚл@ιĶƿ҃BƃԓǤƓƜҖϭҷā',
                            'ӽüәҠĦѽąɟKǩ˹УɽΒѩΓǥl¾4ĈƫӑőƳVήХ˗я',
                        ],
                },
                {
                    'action': "ӪЛνǵƳϹ!ΘұΣԬͿƲǂ'Ԯǃ{ѳƃŸʃЙ©˟ϩĿˑ´ʆ",
                    'resources': [
                            'ҤüΛƙЮϫǜСȎŹ˗ыҲ*Ѧ\x9cƑĬǣŨ\x8eѐбѨ¼ŏǮǥϧӻ',
                            'øȆԠaɟȗĆ¯ѷơ°đó/Ж˘˒ψͻɞʙԂȠϣȽ_ԟǜѣҵ',
                            'ɂҨéϐĶ\u0378ӴO©ӮϡtRҪΘŌϠÿƥЍɳόuȎpʹǟѼɊ÷',
                            'Ѐ˙ƅʫʍʴ˚ūƬѠаѫɜΑϹȵʗӎƯԝŠҿȐ«цχɘ¤Ͻˌ',
                            'ǿΰңΕЂЧԜɧ!УÂʩůΦHғǃӶ\x84ˁϻǦ\x80ӨȾσϞymҹ',
                            'пʭӭӲĔԗȶԛ©ȷşȄ ~ǪԑŶджě˧Ù×ӜǿɆŶяƖȔ',
                            '\x81/VҍìϖɛXԎĘËǉˑЌgǳžÞƸΟʂȠtƢɮĶɕåū\x83',
                            'Ԃ˨И҂ʄ˛<ơʏǏҙώВƻcԂȉȰęÆɯɡɖqéϿӜџʇʜ',
                            'ȣԁf;θηÓĄƬ˵p¦Ǣһ˻ӰƯǵħҦѳƷñǩҽӭҕǃÝҌ',
                            'қýƋǲѭ¹ӺʓөkјȤҺōФȖҙбѨϔ˶ϾȷΜfԫΔҴ\x93˚',
                        ],
                },
                {
                    'action': 'ʼƀMǿǜ~ɶԫːȫäȁѨ§Ɂŉ¾˰ЛʍЙǑЍ^ǐϩҗƨʜ',
                    'resources': [
                            '6бƘΘ ѼФÛɈȔ,ӱνǯңäɹƗĸʼБϴЋɦşȹŮӰб˥',
                            '@Р҈тãҩ¼ÉƜțɌ\xa0҆ƍҕƠΎʛ´ɩʃґč˯ϢӅϘΜ¯U',
                            'ˉWƔêɥďƲѐӕˎЁʮüɀĪҁğńĘ˂Ċʄàbȑɐˋɯ`4',
                            'ɢСȪϔ¡Ɛ˂ΆɎʊҚÁɝӘ˨ԡӸAğРΈɿ˫ĭƓҼǞʮҕǺ',
                            'w»ԆғɇȼʻѰǆüǂ~ːŀѼĿȬɳԝӮȖƓάσ¢ŚíĊǑЇ',
                            'ŬȒN˻ϋӉԟҏĴľƩѲ·ʺҋƖȵ\x92Ј»±rЏȅΎͿ҂қfҲ',
                            'ԅĽˏ˪ɞǔӚ˧҅Ϊ˒ʕϲΔǜέѥϢӍˡԎˆԪŹÔәΝȸДҖ',
                            'ӷƏėˠŧѹԛŸƫΓʔ¸ӾôȁжϦǦǓyŶӌҜӲ˪ĤωΘʥı',
                            'ÃҠһƷŵͿѼɑοјȮQ',
                            'ҙȮʲʧҖȃȵŞ\u038bӡƉө\x87Â˽©ɲУϺϼ{ӾџƐ\x8bҒ¯ĒˋƄ',
                        ],
                },
                {
                    'action': 'ΥҠɘԅĺϬǇѠωΏȀʗϕȚøҐðϗџàǌϧаʹpəŽηJϕ',
                    'resources': [
                            'ʉưŇɤ\x9cˬǘнɾt˝ŘØƚÃ·ўӚů҈ʭťƻďƇȋͼ\u038b«±',
                            'ԥ(ϛßƟˁ\x82ɛҗǨʿȥ5ҳѽ˹πεԋӯѹ\u03a2˻ĈϻʻkҍЂP',
                            'k¦ěŮɒħņŴɇȥÀǽLӞ\\ΈǑϙ˕Ɠþ˂Ϲж±\x8dɦǻŦË',
                            'ǰξπƁ˕˫пϛɔϿř˷Ĥ³\x8a.ѪʇϞȖӞ·ȠͻƴʚϤnɗα',
                            '˄Ƚ´ǪΒҏѝҷӗà\x89ʏΐşӏү˳žΗѕǵӨŕέєϏ)Ԓ§В',
                            'μɽɷѸйƴҜɠϦãÂЏґƙĨҍӦθλʿЧ`Ӗʒ%Κ¯˻˳Ǝ',
                            'ϢщŸ§ɏȖтȭҁƩĳΖǡ˖ϊbȗʊΈϨʴȏăMEĹ£ƻĀǇ',
                            'ђŜВLлʈôÁưҤűŷǨ\x8cǔŒͼƌʔя×ȟӞɜ˃£ϤB˾Щ',
                            'ŪˊΧͱ˛ɠƓľ˵ȼĝʝԡć¥ɍƏ',
                            'ȔҖȌӟǙρǏΗ<ѻ\x86ƃȲȼƼʈƚҵȨˎъąʂæέъτѴ\x80ƫ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˵ϥɍ',

            'version': [
                -9121106142981310981,
                -8868302582825678381,
                -4577837960039050869,
            ],

            'location': [
                'Ҋ',
            ],

            'runtime': 'χ',

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
            'name': 'ŰŻϠˬ\x88ƜΡƌ¹ϨȳßʗԀɁšrƢɆƲΪĤ\x84ҭɑĥ®ԕǼά',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'tÍӤ',

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
            '$': 'к˱Ϛ|#ơuEεϽɫԡԟԬǔųʻͻҿ˚\u0383ëЗԈήŲ>Ơ$ʕ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 7575308082666965342,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 454694.43158930005,
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
            '$': '20211104:181930.930028:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ʆΒNĭţαȳ,ƞŦҵģӺʨӎˈfωǼЧʟҶғ˖ԒŊĵХҙΩ',
                'yŘM҂дƽәģÜѡ\x95ɛѥǂˬƅÂ˄gʙ\x94ǿ\x8e|ӣϱʕѐƿƭ',
                'ӱơ;ōŝĄӫϟʨѹ҈ӞĲρϣ¶~ғԙʐħſʑʹ»ЏĽƁщı',
                '҅ӽԘɅƇЪѥ\x81ʳϛˆǮɲάӹμӊöнОŤҧпÑ~Ӓή\x86ʈɇ',
                'ої˯Ӷѷƛ˴ŧ\x84ΫˏЈќ£.ɘВɤħ ˹\x8fȩ˹ǼƎýӺҎӛ',
                'ϸĄӱҳОɸΩҐʧΧ6ńǏǵũŤwλŜơ5ɢȺJǓνѮ˟ȱ$',
                'ĖϐБƲҗɷʔņӞŒԦĊώќ\x9aȜ\x98ÖĭвӀɜπάUxԚʭƺǎ',
                'ǕλĤƜӣɰ˔ǡƃŬxƏʍǤƷɅӱǱėȠʐɴEʚАƐҺYʮɞ',
                '"ьԣӓ\u03a2ĵĒǉЀΥʱʅϟʸ\u0382Å\x97Ƿ3eͼѿ˾ʷѴ҂ӓøƍы',
                'ЕȮƏԊɎОʿZĽԇʜХτԤбҝͿͰʪ\x98Ŧ4ƫĩȗȗÜ˩ŧӳ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -5570543366110821302,
                -4156470806575087571,
                5647421594878598082,
                -7818824731944701816,
                -5731888045809620329,
                -1963240340316583469,
                -8491381029889529467,
                8910194415518365252,
                -31705472328630275,
                -8599157812727008918,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                720761.2260809863,
                682921.3728512239,
                760783.3506138551,
                93610.3795310857,
                213253.69721432123,
                995295.5489698944,
                758536.1168690596,
                -49967.85245548636,
                98434.37816143615,
                351316.9688498662,
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
                True,
                True,
                False,
                False,
                True,
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
                '20211104:181931.894794:+0000',
                '20211104:181931.911040:+0000',
                '20211104:181931.927434:+0000',
                '20211104:181931.943973:+0000',
                '20211104:181931.965766:+0000',
                '20211104:181931.983421:+0000',
                '20211104:181931.999699:+0000',
                '20211104:181932.015915:+0000',
                '20211104:181932.033745:+0000',
                '20211104:181932.054954:+0000',
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
            'name': '\x9dʋ;ҤӛƙĀϑƞǈϴЀʴĨ҈ƗƚǐȭɔӺƙǜάζ',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20211104:181930.618611:+0000',
                    '20211104:181930.636072:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '°',

            'value': {
                '^': 'string_list',
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
            'catalog': 'ȍƕķȲѴɩũĠ?tǧɑԝƆыʸϱĉЋԋʀˁƀĶ˲ыʠbȂɞ',
            'message': 'Ǉү\u03a2əņőîƷƨͼ(\x9dҷǤôӜjƟʯˢǗǖɁbʰȆШHʈ/',
            'arguments': [
                {
                    'name': 'ǯЄҖȩϏ&¸Ñ&ȷ¦ӺƜʮɢ˗ͺ\x9dΜŚҋȽӈЮȁΓŲ˅Ͳ¯',
                    'value': {
                            '^': 'datetime',
                            '$': '20211104:181929.500377:+0000',
                        },
                },
                {
                    'name': 'ƥ˥ͶǦүȩɎ˧ęκǓ¬єńƋӥǃŮ ',
                    'value': {
                            '^': 'datetime',
                            '$': '20211104:181929.570265:+0000',
                        },
                },
                {
                    'name': 'ǋêŦßΧˇʤNӘª\x95Ѽ\x96Ԙѩĸѥ=ǇɖĂȞэZƞɃЛѭѤ˾',
                    'value': {
                            '^': 'int',
                            '$': 8022987675710971170,
                        },
                },
                {
                    'name': 'Ӗ˖čĽćȪĵФҗ(ǇƴͲĜß҆҃ԑ¯Ӕ',
                    'value': {
                            '^': 'int',
                            '$': 4649562819041832210,
                        },
                },
                {
                    'name': 'АŇθϱʎԜԏϙæѐɓʚɽӱ˶ĘҘɁпϢґ\x88ʎɡӾǠƫԀˆ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20211104:181929.784477:+0000',
                                        '20211104:181929.801068:+0000',
                                        '20211104:181929.818619:+0000',
                                        '20211104:181929.835452:+0000',
                                        '20211104:181929.852279:+0000',
                                        '20211104:181929.869003:+0000',
                                        '20211104:181929.887943:+0000',
                                        '20211104:181929.904851:+0000',
                                        '20211104:181929.922022:+0000',
                                        '20211104:181929.942863:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ǝŊÇˀϛʈľɸȋ;ѨҔǥҍҶӵωϵhŴέӗ˪ιaŲгӦςˏ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': '¸Ŕ ǽ˓Ƕǀ¸EɒǼӐϗŌҵ¡ȽeҘϬÄЂɔɒ˧ԝñ҇ǣİ',
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
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ƈʧń϶ˊȤҨ\x93РÈˇʾҫˑԩеƏÝӢǫΫŏ¿҃ҵφÎ6ȳѰ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ʉӻԆJԒ>ѬԕΣ\x9fфę¨üѾÃƄįŠőΪ\x9fŉ҄µrƾʂāj',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': '»ßƻи6ĂĴʯѩǯɆ˕Ȑě˃˔ɳ˧ĉƻɲѸƭǹ£ï',
                    'value': {
                            '^': 'datetime',
                            '$': '20211104:181930.481513:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ǵƔ',

            'message': 'B',

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
            'identifier': 'ϑɌř3ӄȳĉεLІԨάİ|ȖȀȓʃʩѨĄsçӱӟԀÖЬƭϞ',
            'categories': [
                'internal',
                'access-restriction',
                'configuration',
                'network',
                'internal',
                'internal',
                'access-restriction',
                'internal',
                'invalid-user-action',
                'os',
            ],
            'source': 'λʋʽрΡɔΖÌΌЫҖŉʫφΟɹũŰǉÞǍȸĎǄǚĀ¼ȗΈӕ',
            'messages': [
                {
                    'catalog': '΄Ҟқˀ˟pˋ',
                    'message': 'ɾЉƢÁňѢ˗êӲԈ_ˈϬ]ϤÙї˼EӡǆήǽȣɳƮԄ2Ə+',
                    'arguments': [
                            {
                                        'name': '2wÎʢIǷʵҲѯȫмЋˤEѕƖ˶Ȧʆ͵яŊEөүфҫɝҍê',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ŷɪƼҜôƇȼЦыСēϔŐΞԚɉ˜ʷάǻǴԗϟт©ѮԊμ\u0382ό',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            34492.772287294414,
                                                                            -51823.08898342435,
                                                                            501489.69174827135,
                                                                            340152.5584689478,
                                                                            939867.0228662868,
                                                                            723436.7365351357,
                                                                            266153.92034324666,
                                                                            725860.9447759112,
                                                                            926451.2212172807,
                                                                            228695.5104649366,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x91ȨІ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:181914.069544:+0000',
                                                                            '20211104:181914.086050:+0000',
                                                                            '20211104:181914.102583:+0000',
                                                                            '20211104:181914.124560:+0000',
                                                                            '20211104:181914.142454:+0000',
                                                                            '20211104:181914.159558:+0000',
                                                                            '20211104:181914.176291:+0000',
                                                                            '20211104:181914.194072:+0000',
                                                                            '20211104:181914.211600:+0000',
                                                                            '20211104:181914.228026:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'И\u038bõȉԐƔȘţ4',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:181914.326121:+0000',
                                                                            '20211104:181914.343444:+0000',
                                                                            '20211104:181914.360192:+0000',
                                                                            '20211104:181914.380453:+0000',
                                                                            '20211104:181914.402152:+0000',
                                                                            '20211104:181914.423006:+0000',
                                                                            '20211104:181914.443501:+0000',
                                                                            '20211104:181914.464923:+0000',
                                                                            '20211104:181914.488776:+0000',
                                                                            '20211104:181914.514968:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҖυпЯǜ\x9eɡJ7ĘΚ*ƹ˩юöΟͽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': "ƸÓ¾'cМ]ԥѠʓ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6801290685694111255,
                                                                            -6579670722020530558,
                                                                            -6019795124537628508,
                                                                            -5346197126651256354,
                                                                            -3801035127534639501,
                                                                            -2131192119481578919,
                                                                            6104241233376507672,
                                                                            4250370813652167352,
                                                                            -7983543542625591622,
                                                                            104463159056321199,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɄюƷϙţϬ*ǨǚǳԔѠэʝ&όʙαĶ˸ÄȍěaÖӧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '~ÄҬҍѸʱ|ȾϤԊʼ˞ԫɟšҗŌϞηǂưЧяғħɸ΅rƺȬ',
                                                                            '.ԏ?pпȆȕхҴĥȁĵҽƽϏμҢȓ˨ºԄÏ˺ǕåάӬǡκе',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ł҅ˑԨʇļԩɍ·ǞɍɛȥҗȄϣɯӘ\x8eŠϑjA*Ƞ¡Ϧ4Ƌy',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƑѫҞЬƏȓϗӁΜИ\x9dІɫνɀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 871458.9247222317,
                                                    },
                                    },
                            {
                                        'name': 'ǐΜҋÇϘӊҩӾԌԑҝ˕ϿǾΟºqԊĺÌχ\x92ˬϗ}ÊÞσ[Ȟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x96Ɉ˻ԅѱΕӺĶÔҬċʔɪϊȭәÛŨǿɯȂʠʻϸȪϰϤĲɴţ',
                    'message': 'ȣΆɤЎϼ÷вκӽԌϮ@Λ\x8bѕєȚЛǷӭЙƧԃвhԈͳ¿жɳ',
                    'arguments': [
                            {
                                        'name': 'Пƞ˪ңL˯ԩ7ɜϡіѢΌįˍˣ«ȐƑΟ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            117526.61603858956,
                                                                            332785.5085000129,
                                                                            12479.984701728012,
                                                                            623610.1580865559,
                                                                            370461.2097847329,
                                                                            817177.7669632132,
                                                                            770120.7166158749,
                                                                            673651.5480645956,
                                                                            825685.7514064339,
                                                                            10307.26048616822,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǟʱ|\u0381ΘԙŪɍ˾',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7219350412094651883,
                                                                            8385802922639854829,
                                                                            3708106438296361519,
                                                                            7104124151262305181,
                                                                            3163112462450413256,
                                                                            5970507453773857837,
                                                                            -4019854673758178524,
                                                                            -3911295856383449295,
                                                                            3627204624192692614,
                                                                            -2996098183088807841,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѕ1ŜҸӉhį',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            66324.25322390691,
                                                                            763500.4128769257,
                                                                            711540.9211379726,
                                                                            316858.85238685436,
                                                                            174045.16316473397,
                                                                            960918.6909003067,
                                                                            917628.4787808567,
                                                                            165581.21067049337,
                                                                            -89291.54758178399,
                                                                            739735.9119476014,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΉӧÿŁ2ɷϧϏҗюɻTkȒʒѵůǯȦϙǱș˦Ξʌʙ\x80ү˹Ɛ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 911231.5806825638,
                                                    },
                                    },
                            {
                                        'name': 'Ƽū˾ʴҞð+ӲƔ@мҭ,ȢŵżªŏʫǧΏùӎ\x9fȿĚľӫĘГ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8616824371507363225,
                                                    },
                                    },
                            {
                                        'name': 'ȁΓӴαϘϷıԂ9ϋ.ƓŁùşȎAέɑƾ\x9dЊΊ҆пɢѐňԐб',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '!ĖӦʽΡЃȗ´҆Ƿ«ˌΌǽƱϱӍ\x9aҧƎΎ2Ĳѝ\x8eªΊŷӼƯ',
                                                    },
                                    },
                            {
                                        'name': '(ĴŠȡķʈǌ\x87ӨáƞϦ҂İQɷwǓԍ˹Ǎɔ!ˠԚϬηԈŜӕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΓҬʎӫϑȐƹîĠҎϜҶʚͳŻҪǒɉȿЛˤЪΣȚLʱΉʢҥȖ',
                                                                            '·ðҋ7˹ȔˆJдСԍΰıʯӉ9ǤƗ\x98ңʹɲ\x90ʜƎʛ!ƎӮȢ',
                                                                            'â¨\x8d˜Ȑфǁłʇ˧ŎZƳŢ\x83ƂԙԖˋАӽʔϭȊϚûϑԅҧɩ',
                                                                            'ЋͷΘÎөɱ÷ɘԋΐŅĊ©ɪĄ˨ԡĚнϳ\u0378ӳŸΟǒ7NœǙƢ',
                                                                            'ɠƻƊвƔ|ǹÍɾǌęɠ\x82ŮЧҀϦǬΩȕԚƅźƚɈÒƽƻüg',
                                                                            'ıńȾϧȓЃƅѺҝŇŨjɐǑÍϝџǒԄˇȔϠǶӣƻԋЕĦŸ6',
                                                                            'ãȾ˾ԁǯŘŞƚRҩ\u0381\x94ϘүƙζȢЄΧ\x90˙ҴЃ\x8cŝϕΤ)ǒƗ',
                                                                            'Ԙ˩ĕŕЯƼʬƆÁѢӏΦôĳŌɘчҭӅĠǖЃ\x89ÀҿíĿϔͱΰ',
                                                                            'ĔʔɨЯʨŇŗô\x94ĭGӉӿǟ¹ƜԎȵԐĞǪԌɃСҜɝ¢ҽƂЧ',
                                                                            'ƲƥšҘЂǙͺ˵ˤ;ɊíƈϿϽυω\x8bÄЋƭȂ$˸ɔıʋĹɰф',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЊԈΗӠӼҎ˅єšϦɂʁВνůѾ4ѱЅΙԌɐĔ΅Ā\x9dŚρρі',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            709239.7849625034,
                                                                            684067.6496976609,
                                                                            539245.2657990558,
                                                                            716083.7760549139,
                                                                            320769.4803949107,
                                                                            342589.0993081,
                                                                            440541.52432766743,
                                                                            579889.7432676895,
                                                                            183525.93633326096,
                                                                            610467.6244625291,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ö<',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            590688.8985148435,
                                                                            346772.59082696936,
                                                                            -32013.345221234995,
                                                                            315195.9085140101,
                                                                            256834.91510063573,
                                                                            59358.66139378442,
                                                                            93333.08212454629,
                                                                            716946.3317567119,
                                                                            431259.8535682979,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӧҭȴ\u03a2ćĲ˷CyŌϐĠøÞү˅ʣyу=ěƳ@ЀƹǠǱǸϽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ʩηԞĬε\x88XħƍΈ˽҈ʛ˗ΆѥҋҚ§ϸȔȢВɑ\x97ʜѝΠÔ'",
                    'message': 'ѨОũԦǡ!ϸȌѰȬαѻѻ\x88е҉ɴԡңКǛŨȳ~ǉŤǙLĭϣ',
                    'arguments': [
                            {
                                        'name': 'èåԣ˄²\x961Ӂ˪ǗʧʣƐѶʈMӍ\xa0',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ԪƖ¶ËɖҹȪШˌǺΈкšӃ|ԪŗſhϓҤ\u038dϰ\x9fͶʍƐͺ˺ϧ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:181917.411562:+0000',
                                                                            '20211104:181917.428850:+0000',
                                                                            '20211104:181917.445486:+0000',
                                                                            '20211104:181917.462344:+0000',
                                                                            '20211104:181917.479144:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӉƽѤbӕŠǩȭBÞ³ʷŢͱб(˂ΣӣΣɩ\x9bμҟȐǭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'вжƠōІÜȵʾϣħȬƷƀÞr\x9aҬzgĎ»҇ǸĩӇʻԐĿŵŰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȀǐǤȁąʮʆҖˠɸи=ɒԐǴɒŕӳдԃ˪ʯҪğùÒ\x85ɰʲȷ',
                                                    },
                                    },
                            {
                                        'name': 'ńҋÓʺqˆіɥѺɯ#',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 832837.63171218,
                                                    },
                                    },
                            {
                                        'name': 'ё?ɝPΒϧӄʃΒрƜ\x8f',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            537174.9295353917,
                                                                            948800.5308036555,
                                                                            751899.7827989736,
                                                                            619905.0894958153,
                                                                            175028.62759964733,
                                                                            984603.0388330822,
                                                                            -62990.448166921095,
                                                                            980240.9568133203,
                                                                            923261.0494345782,
                                                                            305004.9399544638,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8cЕĀƱϒҢҖĳϿŎžџφћȇƍє!@ʲє',
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
                                        'name': '7ƸЭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:181918.263262:+0000',
                                                                            '20211104:181918.281261:+0000',
                                                                            '20211104:181918.298102:+0000',
                                                                            '20211104:181918.322314:+0000',
                                                                            '20211104:181918.339733:+0000',
                                                                            '20211104:181918.357113:+0000',
                                                                            '20211104:181918.374760:+0000',
                                                                            '20211104:181918.392362:+0000',
                                                                            '20211104:181918.410111:+0000',
                                                                            '20211104:181918.427286:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԩ©ʝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            162311.84393185738,
                                                                            595565.318646232,
                                                                            617707.9316695092,
                                                                            612809.0457260116,
                                                                            224259.4966094636,
                                                                            576024.9956269707,
                                                                            864966.1514558379,
                                                                            781349.9812486521,
                                                                            695679.9740461577,
                                                                            447585.7060304207,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'èνɞˏͶʬǶģ£ȿɣ´ÁзȊтȾΒ˼ЍԢ҄ŕТɶĀĞɄɼˆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6294122424391065944,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȕĢ˻ыņҮȸgǟѱĢˮˉԒϲτϏҷʗˁşҊ*Ê]ЅӞ\x80Ɵʔ',
                    'message': 'ѵyɮϑƣ˘ŭ¸ѾòѬԗ˲ӹáǂ»ːśœԦćγѬȵлψԦɰi',
                    'arguments': [
                            {
                                        'name': 'Ң˪Ї\x84ǹʠėѹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9185224741249311524,
                                                    },
                                    },
                            {
                                        'name': 'Ů\u0383UџȖƄƒМƼγҹЮǍÚƨК',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4022407598512713385,
                                                    },
                                    },
                            {
                                        'name': 'Ҷřȡw˶\x81цphѬԢɆ4əƜċŴʽјλęȁӔµΣӜʏÀƨ_',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ǩv@жҢљZѯѕɡŸeĬƽĶˣЀȂĚˢīw8ΎÃĹҩϟČҵ',
                                                    },
                                    },
                            {
                                        'name': 'ѳ\x96ЋȊɨʎɨïΣӣʡЛ<ÇѵɂқПÜʄԫнűӛʽ~Ӧүʀv',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181919.177008:+0000',
                                                    },
                                    },
                            {
                                        'name': 'fǅά\x80ȔѼŔƍʁ˩έʻˠďŀвǟĊʍŦȈāѤɻňɞˎǤ\x84Ò',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            374567.9969075527,
                                                                            259251.47400117328,
                                                                            803968.5801000833,
                                                                            768663.7005238144,
                                                                            512372.0972772272,
                                                                            649027.1849096081,
                                                                            -50698.60097132809,
                                                                            282258.8864945027,
                                                                            472809.98792936595,
                                                                            9502.249664249626,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҩ!ғώкýӇƶǫÙáѯЩΤM½ʳIČʳǈӖӁœ¯ĉǼ҂ńC',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -2662.422819856787,
                                                    },
                                    },
                            {
                                        'name': 'ʚȖ϶ƳHϡъĎ\x876',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˷\x9bɌ˷ĂӽdǖʂÒ·Ӎԛ8ϘǼâȪӞёЏʱāŘӓɨхʰԊӆ',
                                                    },
                                    },
                            {
                                        'name': 'ʭҶԌ˩ƯȢЁűі\x8dpțƛ˾җЌΔÏӏƉ%\xa0Ȫƍ\x8cƀĦɭȎ¤',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƈ\x91ӡӺ˺ǨǀԔβӢʡĚϻȯ\x95¢ҲЯϼ\u038bƓfѺήŃĄĜɅ^ф',
                                                                            'ѤҗѺ3óҪʆӘČƂѰƕ\x8eν˜¯\xa0ΓƱоɸˮɕƙ\u0381ѓɷùˌˢ',
                                                                            'âĿĞư˖эȨ¥ǈίγŖĝ\x8bȱϞҐʠˋͺɵϧŌӟӊǼˮ\x7fƩ҇',
                                                                            '=ψΧǄˊWƽӺϥȆ˺ȉƹЮōѓӠĒЗ2ƛƨʂҚʹŁєήгM',
                                                                            '\u0379·qŁҼ˫ӛŃŏǈîǝҋƥͶĔƇҠ҈ĉĈҺǶыλ\x8dЭċŒԆ',
                                                                            'ʗŷȘўҿɕӫЎʠӥɥƅʷƏƚΙ˵ғңǇа3щ\u0380ƞҪµɨьʦ',
                                                                            'ɡѡƿǐʭʉ˧ʼње\u038dˤԧЯǇҼӐΟˠɝµŸ\x8cс\x9aѨ@ćЅɻ',
                                                                            'Ʈ˟ĘњòоǫҮӦɃʥϮѿʽ҉Є˝ӽɻԜģҒɷжʽȂŔϞq\u038b',
                                                                            'ʗEӵBǼȤņʠϞɍМ˵Ȅ¥ΉVȜĉɛσȗѸԠǝͽǲĖ\x8cүө',
                                                                            'ϠӕБ¾˫ȰυҷЫгģȪĸǢίӢӼïηԃƄзʠʁƄĪȎǀ8ķ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĻϏ\x84ȊЛНɤɢηÉԐ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɄɿĥӢΗˈ×\x85ԃʍǀҠ&ϗʖŶЭӻɯǃʀύ$',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            396845.5841060935,
                                                                            81325.93886550935,
                                                                            947924.0209328466,
                                                                            -39618.15574980555,
                                                                            120461.93513020169,
                                                                            805391.16082466,
                                                                            581356.0154301593,
                                                                            989088.8157204886,
                                                                            566760.2399429538,
                                                                            758861.9432271571,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'țj˄іʡȶʁɾ·Ӓǚʝʷ˾ǊӵѱˋϾhIĿ\u038dƂӰ;ɼq\x8c\x80',
                    'message': '¿ŷЁОǤѾШѕ-ʚµԅѵŹăͰϧRͺ/ҖɽǢĖˌƸЪҔɔȭ',
                    'arguments': [
                            {
                                        'name': 'ŕϩӳ\x88î',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 964699.1486107865,
                                                    },
                                    },
                            {
                                        'name': 'šʴͱǐͻηӯ\x92ȇƭӓǁšɂBŅ~-ТɬɌԠӣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4455663981973881054,
                                                    },
                                    },
                            {
                                        'name': 'ǱБʒíж˧ЊĈ¦ʮҔаАѭň',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'πɼӄξ˦ƌũѰƗŢɀϸѫɶѥɰ˶ψÂЦ<½Ƈ˔ҽОN\x8a\x958',
                                                                            '¿ЏəȌʥČϒԨҞѣwƧŻǐƳϒăɏδҒћɨȳ˼öĕƈԥғӔ',
                                                                            '}Ҟļȁπɟ\x9eƶІʠ҃ŲѤϜʐPFƙũȋʏ;ʔfǩь.ɅҾ˥',
                                                                            'ИĽӋԥ|ΟғǹǕОєøФӬ\x9aʴåЦɸγʶљԑȨӧӝ·Ðǿʍ',
                                                                            'RғŨY˹ΦİɏĜѝ×ʆеēŞфéˈȫʢʾ\x84ѓәҖɹ0Ȓɳɴ',
                                                                            "ӧԎЪΆ|ЯɽðΒЊ;\x9bƝǮԔϏƻǾ'¾\x8cɥхӐ˶ŤćʩӽŌ",
                                                                            'ǏҸҐ9ʵ˺ʴıНΡǡ8ӣœҙýŗ˥ªВͶɴĒϭ¨˨ǲǒƈƥ',
                                                                            'έɨf]҇ԮӉҢÇ#˯ȧӻ˪˻\x99ӊӇFȡöҩňɷòХɒ$ưЏ',
                                                                            '˛Ǽőһӧ%Ƶ¡ȎӭɽƣԛdӚЀІʪǁȎ!ыƈΞөɖϚšȭǂ',
                                                                            'ĸϼѻԀƈǻïʿϛʸƖ1ǣɂũшһΠρǑє§аɲҋ˩Ӆȑ\x8bʇ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'șǝD\x99ǟÅɷ҃Ԛˤɻ҂ƤԬ˓Ћ\x9aǊ4·Ⱥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĔЇϠЌΗьș@ДҌϷÎЙ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            497005.0765889257,
                                                                            725394.0931270809,
                                                                            50771.67435896309,
                                                                            647737.7872774218,
                                                                            644859.322172714,
                                                                            874454.9605239035,
                                                                            753522.1621350852,
                                                                            511009.48282056197,
                                                                            952398.1671723938,
                                                                            447660.91045269,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʛǵЙȢǅ\x9f',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɡGȱ\x7fУȁǻЭθ˂Ĝʿжέ\x97\x96ɛȓ˹ɶôˁъХʐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4813206029357883844,
                                                    },
                                    },
                            {
                                        'name': 'ǺŸϢĈǲУŻǘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ǘȍϥӟ˕\u03a2qϿѦԃ!ɖɓ҉˯y6˪Бĥ˄ӎ\x89ЦТƐɲȚҌő',
                                                    },
                                    },
                            {
                                        'name': '҅ʊşѪȨһˆъʍѹǅ\x92Ϋ˛ҋ%Ġ-ѱ:ҭĞȪŊʢυĊϚŷː',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4801874024109212671,
                                                                            -101359230533105924,
                                                                            3416606568996785338,
                                                                            7952080345317138790,
                                                                            2603317876680563070,
                                                                            -6424986910933485386,
                                                                            -7468825852315782507,
                                                                            1470909265451445738,
                                                                            4401317507938225839,
                                                                            -7886184884435097093,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '=ρċ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -63588.89025053142,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѤǶ¢ɶŸʰƸ\x908ÙϹӫѺϨǯѽsŦ',
                    'message': 'ńƋċu¨ΙˎЇûšӇЃԜȑɁҁõà`˴\x98ӅĸJТȕ/ĐˈЊ',
                    'arguments': [
                            {
                                        'name': 'Ĳʹ\x83ег',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181921.820060:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӾƈȽĚɻǱȌҜɇҁҲ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 776093.3376284064,
                                                    },
                                    },
                            {
                                        'name': 'ţf\x8cѽĨǃī\x7fεǕǕқЅӻǔЅÒӊҢ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181921.975412:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǤǿǻκѾʯô3ʙ³ԏȽǰϢŖє˜ΣɭâɅ±Ȏ҃ĪǜǦɎΐϵ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɡȖӃʅςӺзȮԧ˺ъȤ¼ͻģƸʕюÎȣҤƏ\x98',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʄҖҧυÞƐβȋӳgӱӆjԝϢǦŪʚȽǬŮͰԛéԔɊҺĉðR',
                                                                            'ȄƁѬ˛ƖƿсԠʺСԖπʆȃǺńӇ¤ůȠőӹ͵ǎ\x81ѥĘāʌʟ',
                                                                            'qtåŎŀďԫȗ˯ΨєЙÿƎѣįʧʉ®ΜƎˬǎ҂ʧ]ҍķΪп',
                                                                            'ԦԕǂͳкӬҪԇԠʷ]ӋɏнӁѴ-ԁȇǣҴȥīήŇʼԈxԑѡ',
                                                                            'ƍúԙǾϕˀÓMϷjɚ˅ӎWȱƦ¡\x9aʭèƵӓĕ\xad˟ϷˏþƦϾ',
                                                                            'ѶLѡ˃ûӲϋӁԦԊĶ:ʃпƎǭůĶʼȜç˼ӹǹѦәƻĒòƃ',
                                                                            'ĉƍЯĚď˪ԞöϻK\x88˃ɋӏ\x8ejÖĘȯӆ˓ЦΟȡҚĒĈѡӉѨ',
                                                                            'ǑȓȖΡİɳƅӥȦTɚȨɟӎɚ҄ȩō(ʪXȒ˛ʗнɾԤӽ\x89ѣ',
                                                                            'ϰȵſȐˤ¦ŸŷÇРƠšěѳțɰȵϓĉѬ/ȚӬψŬӐάĪɉñ',
                                                                            ':\x88ʀеȐ-ÅÅǙ¿щʴћKϬĈД҂ǗѹѐЉàҊ¬җ͵óҮp',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ʄŗɝ'έѩ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 980318.7597224722,
                                                    },
                                    },
                            {
                                        'name': 'ĄҝƟҵþЭт(ˑ¤ĕϋғԫшĻĜǧϺƐŗţǋȟºĔIӎĮź',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:181922.432330:+0000',
                                                                            '20211104:181922.448727:+0000',
                                                                            '20211104:181922.465206:+0000',
                                                                            '20211104:181922.481997:+0000',
                                                                            '20211104:181922.498497:+0000',
                                                                            '20211104:181922.517211:+0000',
                                                                            '20211104:181922.533811:+0000',
                                                                            '20211104:181922.550076:+0000',
                                                                            '20211104:181922.566360:+0000',
                                                                            '20211104:181922.582468:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'άК$ŁĴũȓǩЂŋʛԉсź0ӔǷ\x99ɃÉϤœŅзǙϟϭϼτ/',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ъӑǦϝȇρɨɹю͵ɳЫΖдʘȞŌƞ\x9f\x8eзтӌНҟЊŮѵΆА',
                                                    },
                                    },
                            {
                                        'name': 'ƯϔĀɓĿʜҋΣРɞ˘ұʋӇЬÃчêŏͻďѮ;ɉÌĵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181922.738075:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϒΦȗƭЈ/ҽӶһ\u0381ɬģη\u0380ĳҡţ˱%ψȿŴ\x90ƺмǭġя\x8eű',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            770204.7196484349,
                                                                            25805.251976645493,
                                                                            94767.68189856654,
                                                                            204488.8953795979,
                                                                            648294.2793301629,
                                                                            615346.3964997435,
                                                                            233428.86311984697,
                                                                            169913.53331099765,
                                                                            293231.2425972716,
                                                                            443771.91113224975,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'фҞŌχӯĠäЍÊUɾҿӟоҎőγB5&ǽƖӶǼ˟ɘЏœʙá',
                    'message': 'ҏьuåč;ʮɭĈĄīӋǋг(˲ѻɤɽɯѤ˴\x8aɀ,ɘģ\x80eò',
                    'arguments': [
                            {
                                        'name': 'Ǽ\x83ѧ¤Ƒ˪ƿ\x7fь\x83\x8bΊǻνˬʸɄʉҏѥBɲϾ¦#àΑU҇Ǜ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 263068.860092423,
                                                    },
                                    },
                            {
                                        'name': 'ЦŭΙɕ"ȅǫŹȦΩʮΪǎ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181923.202464:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϡĐΘŖŰ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:181923.272834:+0000',
                                                                            '20211104:181923.296094:+0000',
                                                                            '20211104:181923.313089:+0000',
                                                                            '20211104:181923.329621:+0000',
                                                                            '20211104:181923.345993:+0000',
                                                                            '20211104:181923.362535:+0000',
                                                                            '20211104:181923.379181:+0000',
                                                                            '20211104:181923.395916:+0000',
                                                                            '20211104:181923.413174:+0000',
                                                                            '20211104:181923.429591:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЯњϐЂłôˮѱΙȞҎКɛӪΊ\x91Ӧ\x83ȫǟĔ ǋ^\x8a˳ɯQѩŧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            818714.29178206,
                                                                            701668.3230181102,
                                                                            540188.4083537871,
                                                                            456729.3781461866,
                                                                            469471.7781942332,
                                                                            185558.56962390488,
                                                                            303808.77668792853,
                                                                            990810.0037231916,
                                                                            -15929.22384809803,
                                                                            208517.81542813923,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʺĺïԊ˩ƊӡIУƟɈͳōȔғ*ЌΕˊǑȖόкԎƪͼ\u038bΒŘЄ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 861848.1935463613,
                                                    },
                                    },
                            {
                                        'name': 'Ġ°ӝoˇԑӮЌŢɉҽǠŊɐ˹ҽϠԬÀ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181923.828516:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΊȌȢƫМ¿ʔˮŜ¹ƅĄFӆńΡ˦ƹЎÑӳЁϣȸ¾òû',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 256407.38095728407,
                                                    },
                                    },
                            {
                                        'name': 'ȯѨƝϨãĽҕѾǝĔѴřņŲ×\x93ţɊÜɧǠδɓҮӨʎňbjV',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181923.967494:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǶA$M\x81ƅrОǼ\x93ЦɝυƢϞ9đҔqӂÙжȐѣƼǪӝŊȧƂ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȭˠ҅˔ŻǰŏÂȐӓӅğŴȧƪ˴ǑȕjĢ´ėϋǩхԒȼ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            193389.40796438896,
                                                                            747419.0233389207,
                                                                            212357.51657455676,
                                                                            194018.25777809677,
                                                                            -6222.011368659718,
                                                                            184175.62493731064,
                                                                            364054.0976596572,
                                                                            -48274.895625871824,
                                                                            782890.4726098033,
                                                                            718872.4820502505,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɉԘē\x84Ҁ¾ϿӍȾª˷ӪŅ§ͶʊTƓśɶͽЕÿԌǀʅȞɹһĖ',
                    'message': 'ɼΨǱԌψҲʄǟĕˌĠmӢôҏbЂʱїӑćRȇςɾơÁз\x94ӱ',
                    'arguments': [
                            {
                                        'name': 'Ř˼˾\x9cĨʱˀɗԒ\x8b6Ą˓рHѶǵʇƟԣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԃʜƍGҰŀȄʽȒ\xa0\x9dʌ˱;',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181924.658383:+0000',
                                                    },
                                    },
                            {
                                        'name': 'зÐÓ»ɋ\x81Ɖ[К]ÃʛҶˈєk]žȀҗҿϸğ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            478319.49701759964,
                                                                            274944.01279904123,
                                                                            209034.54298632586,
                                                                            -74138.04219884149,
                                                                            946848.0555763263,
                                                                            289059.88540872,
                                                                            -89636.70509847926,
                                                                            670124.2759639644,
                                                                            206152.04888234194,
                                                                            404398.86220034526,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĉƝɵĒҚʪԞǂʂtɳʚǠèΚȲˁɓĄЍöӏʍΙşϲ˅§ϝͲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȈΓѵϜǐѼɛӇłIѶƯӅQύČhĪыɡɋÅȥзħѶȳȲ·ª',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181925.047401:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʮǛ[ÌƩŴϟʗ&H·ɥƩʕҫĐЅђǠжŻȥ6ƶȣKΨΜ\x8aʃ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѮӼǎь\u038dÒ˚єґϚΤɰЊԧҍѢҸθӆҒ±Pŀƀʰ\x9aϺɊԩĄ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˾Á$Ů\x81ǻѝǌÐºeɚȣǊӳËɟƶԧЀ²ɗ҉˶',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6167707873495658024,
                                                    },
                                    },
                            {
                                        'name': 'ɚʻƐϯшʛʛϒʐŘf\x7fɄ"ы˼ѴƖѠҗѰ}WйĿ`ӘøƲǟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЁɚϫԫӀƝѹÃԃяŋʅҷÀѳ·ǁӢʫӢɃfԟуųnÐǀԥӏ',
                                                    },
                                    },
                            {
                                        'name': 'сɉȜă\xadŧ?\u038dӈȋ˺īĬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 621375.4254531979,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӈϊкЋôʭΟÃӠϮʋϑϴԈӒЙ\x96вβ\x9dΜĺϙ˧егҜήcӊ',
                    'message': 'ɛ;șЂ~˺ςȏɹјҖɦéĀʯ-ǎӵϙÇʒŅʫЖǼǛәȝ×Ø',
                    'arguments': [
                            {
                                        'name': "ӱʄӢ\x86'¼«άȦ|Ȟ҅ʾǡԐȿԖԡ·˹",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7929391482012752008,
                                                                            -1073872332641535618,
                                                                            -7026161336072895878,
                                                                            5610085468033497368,
                                                                            -1652418197489577115,
                                                                            3957087525559379290,
                                                                            7397395367763426047,
                                                                            369252120542849127,
                                                                            -3555164510018362339,
                                                                            4884400796553069512,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˀʕʴ˙\x85íÏȂͷ˟ΏɩӖƣВσƼ\xadҞõҰǗǽwɇΕĐєǦq',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6642944518911425595,
                                                                            -5732307667728494456,
                                                                            -8377370840383790986,
                                                                            4034616547651352734,
                                                                            -7248773532028361876,
                                                                            4129840072483690948,
                                                                            -8473044260514972198,
                                                                            3636257960839636045,
                                                                            -2457132199763444229,
                                                                            7691321626857597897,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӜʕɅԬԪʪʊȑÑøìΣЯѠσˢÝ"',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ъҶƠȴΙ˗ӰОðϖͳӴè҄ϴ\u0382αȀʐư-үѹʵΆύ\x9eӪƪԝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 253890.86631902965,
                                                    },
                                    },
                            {
                                        'name': 'ĪíϓӼȉǒ!\x9flЍ\x95˫ĩѮλɔÜЅSǷЖƔ\u0382ϩ˭ǍҙӢĭƘ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:181926.515060:+0000',
                                                                            '20211104:181926.533599:+0000',
                                                                            '20211104:181926.550331:+0000',
                                                                            '20211104:181926.566527:+0000',
                                                                            '20211104:181926.587415:+0000',
                                                                            '20211104:181926.609731:+0000',
                                                                            '20211104:181926.631101:+0000',
                                                                            '20211104:181926.652010:+0000',
                                                                            '20211104:181926.673866:+0000',
                                                                            '20211104:181926.692936:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȞԝȖƣϴԈҞªԈɠӐѰҝɹǸҫǿƐʻƃӐŎĨ˖ǻϴȄсĩϑ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ρȅʄ\x9dʴҺӁɮǱ\u0381ʿӸѐӾԇϏә҃ʝ˃ȿńƌ҃ԙ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'őɣ˕ĂðÌʊʇӫēɢūѼҙʍԙЧūʚԩŊľҩ˵',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -32045.101680627995,
                                                    },
                                    },
                            {
                                        'name': 'ΘȶŅҭҴЂ\x9föӁӍÖƯúσΐůЃӆ˕ʥĈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѻÁȹ¼˲҈Ƥż½Ѽ6ʽԫ1ě\x7fĈɀ˹ʼ˜ӋƁԑϿ¦Łς/ӭ',
                                                    },
                                    },
                            {
                                        'name': 'ĭўƿƞ\x9aΠmůӻpФż¦ԥľƕӮĂǀӀĳӅϯЈɒѻɫĂô"',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            603504.564961002,
                                                                            922390.8711517691,
                                                                            809805.8382813702,
                                                                            195020.3022965183,
                                                                            464318.7902468385,
                                                                            867747.0869286576,
                                                                            601585.9669212752,
                                                                            799570.303504586,
                                                                            169810.00472723803,
                                                                            8666.33638078536,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x89ǎȷȬPǄȓuǇ\x82ķʠԤɆрƚϴǐƢɾӗңɫϒгҢ˹˩ɾǴ',
                    'message': 'ȰқɚǠɰʋѪκГԍȃŕһͽ˓Әϐ-ύΠӟǧŪќϠɚҐťɈ)',
                    'arguments': [
                            {
                                        'name': 'Ř¤Ϳ¥ʿɿ÷ó¥Ԁӿ˓ŀΗşӄԅŅŶŅӧńˀˮΐǾЗтԠс',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            863119.5703898896,
                                                                            58505.026383348944,
                                                                            379246.4103546494,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӺΠЏ˖ƲǼġϏȩǞҍЖͽ©ʬғҼЭɢԪӍԖÙėҞǥŗʱлҾ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                                        'name': 'ҕͶ&˥ˡЄƚ+ΞӕÞҜҗƢЎѵĂŻљȷȻΨɉ2ǩЧěˍίњ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181927.929343:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϋҹđŁƍΣxǀϺĘӍƩҵ©ӬŮʳȋ)îƍs(',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:181927.995633:+0000',
                                                                            '20211104:181928.012020:+0000',
                                                                            '20211104:181928.028078:+0000',
                                                                            '20211104:181928.044255:+0000',
                                                                            '20211104:181928.060962:+0000',
                                                                            '20211104:181928.078088:+0000',
                                                                            '20211104:181928.095039:+0000',
                                                                            '20211104:181928.111968:+0000',
                                                                            '20211104:181928.130991:+0000',
                                                                            '20211104:181928.150032:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĻɝϐЙзŪ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:181928.238837:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʂϢΈʟëπ?і˴şʟxέƕtѲƎθɍ\x8f˟Ȑ6ͱńǷç*ʔȳ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            494296.02650511777,
                                                                            779185.8049130403,
                                                                            224837.91360719944,
                                                                            316362.77001522755,
                                                                            8198.306165416318,
                                                                            515091.11059912865,
                                                                            658641.9529852017,
                                                                            946007.8749551971,
                                                                            253402.9552416684,
                                                                            696705.5157248143,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɣϻò',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -40314.368995796525,
                                                                            671456.7730599127,
                                                                            208964.96459541417,
                                                                            536056.1074413307,
                                                                            580304.5732497001,
                                                                            967810.1638404413,
                                                                            254525.80197598576,
                                                                            641698.6795099229,
                                                                            767065.0243863026,
                                                                            763805.7326476767,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '´jǹωЭӠЪŘĥÑŦʺ˭ÿ?ːΉӀǖȺΟŋԤÒƂˀ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:181928.817493:+0000',
                                                                            '20211104:181928.834791:+0000',
                                                                            '20211104:181928.852382:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΕȱǦR\xadȶϔϖΌďNƹ\x90ȝҮțń',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '¥',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            320973.02410229977,
                                                                            876885.3794600216,
                                                                            130347.51485491087,
                                                                            220298.28919664613,
                                                                            875622.8960742845,
                                                                            900301.8135446433,
                                                                            -39330.15379239212,
                                                                            903168.55420201,
                                                                            224438.16741066612,
                                                                            899157.9286410476,
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

            'identifier': 'ȄƶŠӃǀ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'ÊƆ',
                    'message': 'ɫ',
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
            'name': 'ӓơĜϕǃȊԢɻѪҌӬͳҨ˥ˋЙ£ýGʡƺύƤưÑ',
            'error': {
                'identifier': 'ϊБnĖԝ×ʼԚ6ѭȓʖΤȤĀʏϱǍʳҺƁÊȵҡŏњ5˦Мö',
                'categories': [
                    'file',
                    'access-restriction',
                    'invalid-user-action',
                    'file',
                    'access-restriction',
                    'network',
                    'file',
                    'file',
                    'network',
                    'access-restriction',
                ],
                'source': '9Ɂ¨\xadʡ\x81òѧôfԞ;\x9aÄʣɥ¡ÕςӚéɵţDӡɦŴēƟœ',
                'messages': [
                    {
                            'catalog': 'οïƢĖƼþϩdǡǶ',
                            'message': 'zҴŨʔѦҾɭǼȚӳ˚e;ӰӷČΞӧ\x8eÆÕʬąуĺМπʻƪ_',
                            'arguments': [
                                        {
                                                        'name': 'ʕȥԣўԃ*ʱƫЯќǒʛϤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˃ǶϦЗĳzǤÊҬћ˽ƕԪ\x94ƋǧӒȫƯ¨Ģ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȥƇӣҵŵǹӳӣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȬĸǏoуȘ\x91ɯѾŰσζ\u0382ɁɔΤѣŅȿϫҕĐԖļѮťƺҐә!',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯӇД҃ӴŵĖҘҾѐн`ϯ>ѡ.ūоʩîê2ӐͿ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 427078.09109045507,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˉĵϊķ˵ŋУѐȡɀ\x9eʹʁҾҢɺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181905.661205:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϛ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȓ˦-ɔ×ӪʦĔƌЦЛ˺įʆеǿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҴȺԥºʑɏȆβ:0дŶ҈ҟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԝnΡӱ\x85ūͿƻðƍѽʋɄ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 794882.3443520023,
                                                                        },
                                                    },
                                        {
                                                        'name': '9Ԝ¡ԈΌ=ѡЂʌяΕ˩ƯƄǅϽ˙ԂʓŜȪЩǢȦɾѶϘΝ¤ή',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҭǝЮʵɭçũѭЪ·ԜżѷɖҙϝQ˔èҠǈĥӺĶ҇ϙȰğБ/',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԍΏ˄Įȧα²˫ԃʬӌ?ˑ\x9bŇ˾ýѕĘΟπīчðʚÝɃЍʢè',
                            'message': 'ɽӪчȓ˯ӷáӫϼȞ©ʴɹäԐÀȍ˺ΊЏΦѠÏҪ ӯŞ˷Ƥ\x8a',
                            'arguments': [
                                        {
                                                        'name': 'ȮǚſЪϋ˺ƘɂǯŤӳ-όʓѻʹϵ˝фɣέϕʐЉĨùӦҽ²Ϳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ҭϩq\x91ҵǷlЯѳƛ$ΑѸſoƳҲNҪϖϴԬƖϚ˞ɩ\u038dε˓Ӊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'σϒύƧЫƶЍǉԖВѶk8Ʈж',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'јӜř',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʖƀАˢʹʾҭԦΦСǚFɤʨɓÃŨƷțχϭΛŭɎ\x92ϐӧιɉǱ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǶŭǬМȊ\x9eŃ˃ĕБ\x8cʊωüʕ½ԧēƩԘǢșsƀĩα§Æκ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԔΧˁɘɞÙƌƑϊǓ\x9dşҦǍѷȊӴĸ©ҝĝΣȞɘɡӐǿьӄЖ',
                                                                        },
                                                    },
                                        {
                                                        'name': '§ʗČĲįьқǹá҆!ЋļРçΆWԞƹŜQñśʄ\x86\xad&ÕƲ/',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ſȋǶР˾ʶ¾˳ɢΒǭ˔ĜŢĊғ˽ˊȄƿҧÓǊӻÓӲ҇!ăӹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1766736810218479155,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԣɧ¤ӟǒʉĎE-ѽʝ˴Ђзɛ[bҦЇȇɘ˭аǿ\u038d&˶zϵӧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɂоéíʉӫŘ˃ʿԕSŨĦMÜЎ¯˲ԟ¡˩ˀʗѶȰǸхТ϶ȣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɘΆ!ԝˏԓѮϒCԂÛ¤śɞrŝӘĵҕØĵéӤɍǹƍʔƇǢĞ',
                            'message': 'ǡȳqӬɱ#ªѨČͺʚĒқ\x94ΐȫǛ\u0381JәӞŉĖӐœȑѾ\x87ѕ¯',
                            'arguments': [
                                        {
                                                        'name': 'ǘӃľ\x91PƞûǁПͶɿԭȾɽ²ŋʼ¯ȍϟӀ˲Ƶή?βѕňȦ^',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\xadяЖӛ(ЄğԬҵʗǙİǩƿυbŀ5ȷѫǰÎџɐ˴ƞӱɛŎĈ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԎǖΫĕЃĂƫɋ&ʋʭ§ϚÈÂҁ\x85ю\x9fԦшɓ~νӲpљÔԮ΄',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ςόˊнşʎ\x96η΅\x88ˁã"ΥSʖĊ\u0382˛ЇɎϰHΦԁΩɖ\x87δǊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԅæø\x83\xa0ìɅѡĻəҵ\x8fƀÅȪŀԂ©ɬҋƙȲрԟԛœωuѨҜ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʞѓŵͲĺҐԅ˜ҁӂΖɾ\x93ȓҭÌЬ˾ȏˆџcƜ҈ĩþ"ˋ;\\',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -73355.41518187097,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɜѫϚǙ\x9cƿĸˑźԎÈøĚˈǰɧtȧǣʪ\x82ҹȓӜʼŸӎ˲ζʀ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÀӶʙŅҽѤĪχǬШ˻ʟ҄%Ҙ.ÄҲȌŻѕΦ˧Ǟ2ӺúώӹƇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1583648214526313073,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȆĽƙϋľő˱',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'οМĈӇņϑМǑЯ˷kͽϧѵυ%үҧ˖ǏхȓmёȪӟӸρĆϻ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ШԁɃKʚɃƁǇĸѲмɒҤѴ¿ΆȳԆĬŵCЙϣʤӸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'żʮϻǈȒ\x8dģԢÛİśǵԛŵҭŹÁӠǻθѳPьθԔņī\x92Ёʎ',
                            'message': 'ѡʻ˔ѓɯȥǹԞȐвĨЙΓҥîΡKϴƿˤAǬύqȍŖчÝЪŷ',
                            'arguments': [
                                        {
                                                        'name': 'Вɚ҃\x7fʭԏʭԜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɥҊƙĂ¬\u038bǜԟmӁϰ®ȽɗƍǔǄͼɏc',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɮ˚еȾѓϯ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ζsțhƃƳŻɦ˨ūĺɱΝƖʏҶď',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181907.754719:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҪȻı˺˲«×Јѳȃэ GҶӞȘѮҌϬȈ\x87ҬĮŶÿː˫ƹXҺ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǅë',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȺˬШĘŰǇЄƍҖϠĢIчɷАȞπїѬώԩΝөӿô҃ёʦżÓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'İЋʉŏ\\n\u0380ȖԤėSǒfȋɵǃϱҊɘāŨѵŢ§҆˪ԇδΡũ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181908.024757:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌԁˋΕӻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'џ͵Ȱ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϛȀŰɥñǼÈǂύ0ɍœĲșĉ˻ξ΄υβδЧ[Ӡ}΄ȭφRǎ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'чӨ\x81ƃʢ˗ʎҐͻԖɗeҟǬШ\x85bς҃ɋҁԤÏ¾Ҷ\x8csʥǔȡ',
                            'message': 'ƥȒԊ<µNζѦɕȬƉӆËϯѴϻƤŢȀљ{ԤҨϿИЃ0ʢ.ɪ',
                            'arguments': [
                                        {
                                                        'name': 'ĖԑΔąǳΈɛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181908.314449:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭƿηһϧиӤρŰҘԎЙİˍ\x8fωдӣƾǩѱ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˨ґČқзɠӧϚɭŶҬԨěƞƽҒ˩ʹ½',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382έƂҍ˻ĊİǩƢϸŮЙȓ\\Oӏϛ[ϒҰŉìɃǬӫӝζ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͱTԄϱʝɆʛѳ˙Ù',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņыUďȣҏÑǍӈȾѶĮʼөǇɜď',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 563890.6880010866,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԔȶЦƙ\x9b1ԇȖԍÏɡŀЭНƽҕӔ=ѤҐҬǒȱϿ\x86ҷȨѰΑИ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀxȦǪ ʀӢº©\x90AéÝb%\u0383ԃѳƬɬbӗĥϸǽ˞ӜƓυŵ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÊϳǤΤϾ˩ǗǮѰԓťeɅԒ҈~Ο\x96лΰī҆ʩł\x8c',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'έƌѧOӖϫ˩Ͱǥ҃ȝʔÂʼҾΛǉ˳ҎȠΊҊŔ˪Ëæw\x82Ԗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181908.948117:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɺɼӹ5ϨԃɱäɫʑŎźǰ"\x8dɽȍЙԜϑțCFѾ˶ҟ҅˖˙',
                            'message': 'ƟâзӲ\x8eƑжɋԟÞǶξȏЋǵÆϙ6ĜϩJȍӶʟūɭɗşиȑ',
                            'arguments': [
                                        {
                                                        'name': 'ЗӤØӞ+@đѕɁ]ŗgԛɓL÷Ǧ Ģ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӁȶɅȻ\x8cҟĔEёԚяèú',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƔѯȤԘĬʌ$ϘͻˀЎѳȫĈŮӎ҇ΗѥŋȚȃʷӅқˍˡԚřE',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181909.222656:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰԘň¤εƕȃəƾɃ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÈŹȵҫʐΑ¬ŚÁȑγԡEș×ԡиĨҙǙҐɱуѝ]ǡȑ˅Ɓы',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\xadƻ\x80ͺśѢӊīŅάʜ%ɟjǺΌΔcԉҾɺϬԗ÷҇ŸѰ£Ɍɩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҿьҵе',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɽтҮ÷,ҽӷɫШɆ\x81\x97¦ɹʐɑʛɖų&ˢϪ\x8fUзͺ\x8dȾǺγ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181909.579766:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȴѵлҹˇ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'љӊǌǐXzʯԞUΜӣÇаӚeȓҳҐʜҨˤƵȮͷʶҜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '$ϱʟ_*ĆTѷÚàҵӬҾƪǀκҾѴ˓ΩÃЅòɈgĢƿʫȆ#',
                            'message': 'ĘÒƼņσ\x93˨čԠЁԁϒŌȩȘҽǌ˶ЍѶԬʪϵО£Ɂǂ',
                            'arguments': [
                                        {
                                                        'name': 'ƣƌȳԊͼԐƴОǭƠĞƅJƥɒԏј7÷Χˎ͵λ˚TŋǇƢӫă',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ';ѡҝӘŴòʠӱŎʒўȀĖs˄ŀçņǭǮ/ǥĨѫϫǐȾtˌɽ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'OǌľˀȇѬӗѭήŦÃĂӛ*¯ŧbĸșƒȬʁþĊĭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'νҽ˂ϾԨ\x96ƲΧңѻ˖¼ǮɟĴXJŀҥ¼&wХŭЪɵʀÕҿˮ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '°ѝѿÎҨêɽҝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÙˋÍ҆=ǂԒǠÔ*°ҽӯʰҪΞήşҩζCФӻѻɣʒ˙Ɏ¯ɮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҲόФӖҭ;AɦȆΏπƺќ˴ŵӂѼӚѠѪǷˮСϜõȜΜǳωϞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'òҞүɣɍČŒǍӶΛŊњȗɛÒҰ˞ÒʛǧԊʥ©Ɋ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ťйAϝ¼ÁiҞįäʈʴδR',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'lϯʓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʁ½ŋQȱʕ®ȥǣJʙʩġӏĺК͵ѶЀӬɻŗҝʶȆƐŜγΗϡ',
                            'message': 'ˈδɲ*äΦȠǂϙЦęжȬ\u0379ǭЊŶƅˠyȡ/ʔϺȅΦу·мҌ',
                            'arguments': [
                                        {
                                                        'name': 'ĲӒԨѬʊǢ˔ʞǒŻй«ҕģҍõњҹƖZѴʕšő',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˫',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 715340.0851416532,
                                                                        },
                                                    },
                                        {
                                                        'name': '˛ĖϰΓƎα҇ӑìΕȊɒCĉ˄²ʿыɟϦȄ\u0383',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʓpùϚŖ˩ʒ¥\u0383ƏȯŗĬ˦ƹǃģ˶ŕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˚é˘ЇM5ǻĨМƗZ_žӻΕ˫όĄǌӮϵӉԖύʳǛĒϭǿĹ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 126532.36109876598,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂƩσњϰіѡǥĆєҦǧ;ǼCʃͷн*ыÒ͵Łѫ˼ĠϷϋ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưǶɌĦΉԘƑ7ȿνͲǬҠ˥ʟʔxʄԫЯƽȃиhѮIдȗˏ҅',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'аZиһӑWǦŷ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181911.179714:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃòǏʬǥª$ƣӫϜǧaˏ,ԭ8ʉȸӕӧ˟àӻ¾¬Ɠ5ƴķȟ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u03831ԆП˱ŕĂǰÎЈǃӌĲĬӪˠÎé¿ɂтψҪĒ\x88ϗҼȉÆɂ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˕JȎêӤӄӎԆȀȫфĿƈӂсǰ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ä\x8cȭԓƻɌŧçǿ˷ǡʠјϿѭǺĽʕ\x95{\x99ȼčǳĆũ˟ʄŷѬ',
                            'message': 'ŽԙɹɭѸ˴ȢЬ¥ĪˌɐѰӜľУȹĦӋӝɜǏȺżɂӡȨОίɘ',
                            'arguments': [
                                        {
                                                        'name': 'ɲҢӃˢǌӠӟ˨ΞɦϕŐ\x95Ñ˥ƌѺŋȗńʶĿǩ+',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 1757.8421524961595,
                                                                        },
                                                    },
                                        {
                                                        'name': '@Ң',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 767875.3846322363,
                                                                        },
                                                    },
                                        {
                                                        'name': '˾ʹȯķɉλƱƟȣԆĔ*&q',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƯѐìҲȧԀѝ.£\x89ʤåί/ͼҲ¼ЊʐÍλΔӑǁşĴȳĻ˫Ȇ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 763362.0336711219,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ⱦ˛ϢwҔђ˛Ї»ɶɠYʘ\x8c\x80ʽԙϜӹӸʞΣǪȧzΤʄҖÏå',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ђȐǲʖüȻƇ++ЙҿјœȁÜӟӭҹĲCІ\x91Ǌӑ˗ԟǨɆСӄ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǟӉΘɤľȋEȨĈƐúu\x90ϐяӺȆЭΪˮ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181911.847513:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʉΞȀ|ѮċGͷЦ˫ƾҋҟŨԧόҫ\x98ˀĕhɥ\x9eӂŗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181911.920405:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȒýҀéǘѳêȚĘģʖǙИɌѫƴΓόǝѨÀƂ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 343385.57318082306,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɎÚƋԎʝƜɻԭӑ¶ʡ\x9cËÊǭѴºŷfcĥЛŐЅƾ)Ιӣαɤ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:181912.056528:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԡаϧ>ĭʿаˌȋȔΫȉ¾ϦԋǹԂҰҊКǕ\x8fēǴȷЅʘҝϐѧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 846233.3086772094,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x94ʷ',
                            'message': '½ɅΏг΅зԢŇԓŪeшкYͶĲԎУІÈҺæ\x8b·ϫԤ;ĥѴѸ',
                            'arguments': [
                                        {
                                                        'name': 'Ы\x98ϩ˂\u0381ǰԆҝҌNǛҏ\x9fЗǇҕҴǭqˁϝҀ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1182765281153184298,
                                                                        },
                                                    },
                                        {
                                                        'name': '>ɻԨѾǶӀРϩƅɶăȿжӈšЛӉǟ¤ԟί\xa0įˠ¬dŜ\x9aʃѭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -23353.898846031545,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɆzŎʂχďϝș/ĥĘқ,ƐĨбţ\x9dŠʺӨ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -13842.726441992068,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŰΠЮƊŕƜɷ\x94ӺǲǓȻǻSȏ/7Ǒ<ӎƙ3˴їϢӿҵǧ«Ȏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņԓԈµ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x9fļμҽľțɢӴˇρЊƹǌϭ\x95ÊȹвËǯүԙ˟ŶƥҠϮºģ\u0383',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҠϚaĬѺĳĹɢЙȻ˫Ήȋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u038dдӯOя¿ЫĊ˓ҥϟόϣȿчЪəӞęɰӱю͵βĲæȷ>Ĭ˯',
                                                                        },
                                                    },
                                        {
                                                        'name': 'V˗ΛȬФІŊˬÀ5ǯȥφ˂ǮЏҀŖ|¸˝Цİě·Ȃůˋňɿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'нЏȆԛǤ\x93б҈ˇԓһΏƟΐɈõéӺÎ»ӔŽЊŝɭʍǽϔ˸ı',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҸЂǣƖ\x8bәƭ\x84ĉ˃ȝɕԑɑӡ³ϚĺɍȾóĨҎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҦɦЌSІɤȾǵŴԊɃǤΎh®ʂgϦɁȾҸ|сƹ³˒Ҕţţɚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'мĽПԈҊ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ãîŊ¿pӾħӄ\x9cʂӳ$ӢЊ\x9cĢʮ·æӱǀŬ˰ɺvǟΉʂ¡ԡ',
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

            'name': 'ӟóǒ',

            'error': {
                'identifier': 'ȜӹǶgƋ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'υƷ',
                            'message': '3',
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
            'event_id': 'ťѽѥ¬ПӠˣƉԌɺњʛÙΒA¢ϬФ_ԌµмǎɈҿϳÙͰͺ˒',
            'target_id': 'ʴѨҺSȬΝǼȯ?МƀʠğĪƹγΖǶ¯ǼҿőaǾ˷Щ_ŐΰѪ',
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
                    'event_id': 'ċƐü÷Ж͵ӦƇǙˍˆÌȶʔϯӶπqƋȐĹѨ&ͽѝÒʦȎЩ©',
                    'target_id': ']ƌƚ\x8cӬЇπӽƊ\x9eҹЀĥɎƒԤӠ[ğƱȋȱmāЛƠЮϓƥ\x96',
                },
                {
                    'event_id': 'ўȗҽϥ,§~ħɘзʯϬб\x85SǞŬʷƨǉŶÛΫјˀíǇŲѷâ',
                    'target_id': '2ɮǃțǿ˸ȇXÎȌȎʣ˹Γʏ°Ӛ˄ϪБƿȽȷ˱÷UĒѽҺ÷',
                },
                {
                    'event_id': 'ӋíōȅçН˔×ʅӼŞҼµvԣϲ:˚ǾˮǥӔΠαȒˑţTлϘ',
                    'target_id': 'ұǜÞ˳ȀɞuȆԂƗΧԗҮʆÙӦQ¥ǆǜǚΕɯǊ\x7fµЕȥϚĉ',
                },
                {
                    'event_id': 'Ʉ˷ЈɺаeɁ\u0383ҙƻǶѐįоцљӶÍ˗ãĜΏΰˬӂƋҊʸϼȗ',
                    'target_id': 'ģʒбtˮłȾţ\x83ԕ҄Ԑͳ҇\x94ԎƱӔƒРȗϗҠ˗ĕ˥ӈЊˌĆ',
                },
                {
                    'event_id': 'ˌî϶ɬˢÐΏüƹ\u0381ƻѹҶкȟλеƇӞҮԅԏ\u038bìЛżϘ?ШЖ',
                    'target_id': 'ˋŌªђǃ¢ԊʫʶѧƴǤȿĘʪɞɋvω{ώğӺӔȬԕΐZIǵ',
                },
                {
                    'event_id': 'ŊƳÝӸ¯ԗ:ԈĘƝԮӈҧŮθʉԫīҊ:Å˶ŔłΪþÄĬԧŸ',
                    'target_id': '\x91ǷӑʬϏ\x82¹ˬƄƩ0¡sȈϣűʗҩΐƌȌɗІӑŚɂđœҙѽ',
                },
                {
                    'event_id': 'ƎȀȟϼӤȽʣ˚ϛÿԮʌԤԞƟͻЧѓǅÙʢ˒ȷęŅ҆ӦϾȜʹ',
                    'target_id': 'ҕț$ȍ\x88tƍƯ²˗Ŭϛ¦Ҕʌ',
                },
                {
                    'event_id': 'LϯїӗɾVεͼҳκ-ӽ\x83ƹþťźѥʳ£˟ȒΏǏȲѼˤ\x9a˪ŝ',
                    'target_id': 'ɿ%ѹштΒǢćҭùİŪƑďĳʓɣϭοʥìϛɹ˞К\x9cҼʐ˓Ƀ',
                },
                {
                    'event_id': 'ʖ\x94үȉӟɆеȾӏνǍѪĒ}ŏȌ¨ɕϱȍȄЩ4Ȇ\u0381TǆˈӳĽ',
                    'target_id': 'ƚҢͻƽӏȉǥѨԁĜӪԞµǐɣϾеȚéƛДoÀτ˫Ƨ7\x88\x9bϗ',
                },
                {
                    'event_id': 'ѰͻǍȔҳͱл§*ŬĕǃˍƬӾ#ǨԖћ8ӳȎƺˋʋυЛϵ˾ǟ',
                    'target_id': 'rӳ\x8dκϒӰȬӕ\x91ϒsĩԃӘɯӖΥ»´ĚӺƢБѵΖ8жӴβХ',
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
                    'event_id': 'оŅѯΣҁͺńҟŝƞʹǨÄЕʵ҂ƇğϒѩХѹȂȹϺǧFF¬@',
                    'target_id': 'υYˋˍ·xǀУ\x8b+ˇʍѠȈw˫˷Ҟ¶ҳҷԩȩǋѨ\x7fr҃Шȏ',
                },
                {
                    'event_id': 'ҐȒɬ˾ɔȵƎĲ}ϥΰǈ`ñЕˬːЈĜƇÜ²ЌΝФʌοКϓȷ',
                    'target_id': 'ʽýǯŢўϢ-ѦɓӸһԍԏƷȾǟԔɰϮӌ\u0382Ϛљ',
                },
                {
                    'event_id': 'θҠҿ˄ԙ҅ҶͼbĚǬӂŞʝѰ κщʠʾŴɃ{ӁƮȏҿмàԗ',
                    'target_id': 'Җ˜\x93϶ʪȒŔĸњΨѷʬ³Aȭ©ȾȰчҏCǻʍԇĻϒGÉЭŋ',
                },
                {
                    'event_id': 'ǟɻʹʴȓҩйŕǸ¬ĀиƫəõÇœʃу°ŝ\u038bÖԡιξΩÓЈ%',
                    'target_id': 'Ԛэ˨ȏϥŴɅӃԭұСCӳβðƻǷǝԉФжѡöЀȐĭӹϳпё',
                },
                {
                    'event_id': '¹\x9eȖǒίϴф˖лüʭÞŝΜ\u0378˅ƴƎŦ¢ГˆɊиƺҦċѩǩφ',
                    'target_id': 'ү˲ÂϴїƲǫƈԧѮùΕʑŨҺľʙ¿¯ŅЪȉѿĴ·ʹƞƮѬΦ',
                },
                {
                    'event_id': 'ɃӣŔѦż*ӨÇ%Ɣǥ\x9b\x88ĉʣЏǰËЇƠ§ϿӚŻĮОҗİĕʠ',
                    'target_id': 'ӴӯLгŻԭԗӲЮƠЃЫƀѽϕαѼť',
                },
                {
                    'event_id': 'ĳӻȣʞҩΞ\x88ǓΝ˭ŕǿѐÔRģðˣ˚ȡȸǦӿ˯Ψƨɔ;áŶ',
                    'target_id': 'ŔӱÇóʍȥƠʚ¬ԝʥЕǨ\x96ʀѓҁjБҕˑȓǽҽϷƪѸʙўǘ',
                },
                {
                    'event_id': 'Ţďȃǰ@ǠʚǾƟʯǑîʊɻűʇŌǂΟӥȮχɤșʪŸӳȓ4Ӝ',
                    'target_id': 'лuԓϢĊÔÁǨȐʣІǠˣͿђƕÙăɽΰає˖ґāŮѭеѤΛ',
                },
                {
                    'event_id': '³ϓӑƁȼɰȔŎЂ2ϕ°˯Ҏҧȋë\x93˖șʁГ˸ĥ\x9aǩĞȼљİ',
                    'target_id': 'δǁ\x9bћӍ˽ВƅұЄҁҴŽΪΟˇˋЄʡȘÅ±ўѝͷҁjļԥҖ',
                },
                {
                    'event_id': 'ӌˡϛ¶Ͱ¡щӴĉΧʍНÄȒԣÄʗ˟ϯaǵįɋĎ*\x9bũώγ3',
                    'target_id': '\x85~Ƭļθʦ˛ҶΐЉ˨ͱƃtȉԋƑγ\x9fѓɼȥ˜ĸȹю¾ҕɝ\u0383',
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
