# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-29T19:26:16.870814

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import foreman


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
            'action': 'яѱбķ\u038bå\x9bΣɹŝÅА˘ȜϽ\\ʦӤЩԣɓϥƨɌȇϴʂʂˀҎ',
            'resources': [
                'ζ˩ƦŀоƐɹșëҚé¦ўƂÈǥƭѿȱǖЮæ\x98ζƎͶƀԆЊǗ',
                'ҽùGȌŮOǶΤēԧƳP<ɢϠƓȚΌ˛ƙҟНȿƆÃŶǟqэȨ',
                'ЇǕΡďʡӴӡǾɮΊƞȂ@ЅŰШԤϳôӼÑѨŲœы)άѐʎǘ',
                '¤҂˻ý˩\u0379ϡˇŹӥxҀǮ¬βǣȘ§ԐĬеʕтϘĚȩԏǲԄΟ',
                'Ã˞ʳüÉłƐšϞǮˈĐАĐĶäѣьʝВҌ\x97ҫȦϘϏӨϕҩѢ',
                'ӦϝʨѶċʤȦǽǤƻҊĉϮԃÉĸȑԤпēÈȦВϢӛ3ňƌѐʬ',
                'ˋɚҿʆɰ˟˳ЮȓϠɿĨ|ăҦƆȰѢѨžǇƻΩWʏŋϘԎŽϜ',
                'ΛȧIѰ,ӌӗǇԂџŴĮΑӵАƐϾȹǔΕШϭÕеŧ˴ʡS˕ω',
                'Ȝɕ®˛\x8eҽŰӭ3ЊЏΐėǳҍãϷo\x8a®ʂӼҸ˰ӒζrȚƮʫ',
                'ε\x85ϕЊ˕\x89ˠԢcӝ\x7fԦƶǃ˛ĒåÕөŕӌQˢĀ5ƍ±ԟɄ>',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ǽ',

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
            'name': 'Ο˼ёѡșȏþƲϵҮĘԏɬɻƐȴȕœДƊ3D\xa0˲ǆġÇȌɠ³',
            'version': [
                -5515494746312024185,
                -1313228349750248703,
                -2951044473247565966,
            ],
            'location': [
                'ҮʴѿӠÎҗδїƘɷ?ԇɁŚǲύZǅ˖ΟϺԂƁѤœм9Ȝƃɼ',
                'Ī*Н҄ŷŠʯĕѾǸeҬІŰ¡ÂeŌÖлſԏӉˆÃєõҴζ\x9c',
                '˼ӆҵщʇħǾӽΦмёǦФɷӷřӭÀQ΅қуԬȑʬɲŵƳȊχ',
                'ˇȴeӠԚ~×>BԏˬѺЁŦĴǐ˙ӄƅярҝŻʥĽŤû˨ԇŁ',
                'ԃöÛҭŊҫŤɦϨϟԝĉʲɥƙʓÂɂĭŕʶϕȒʬņjѧ\x8feĆ',
                '˺ĵēсŞƕԪ\x93ʼυӭўͿԞȱсϋ˚ʭϗȞSʬİJΆ\xa0҄Ȅɿ',
                'ʁυiҫƖńӨǨʝɗƯķz˽ԉҋОŊҧĹǤ҄əǄϷЎ\x96ƉΗǴ',
                'ǚȷȵ϶ԁ\x9eϛ\u038d×Ŕ%ʱҷƋǒˆˆьǯϢ~ÞȡЂɪʲͽŏΨȡ',
                'οȹ˜ŉȗɜɲӤßɀЩԝӓŊгƜˍºȨ*»ǈɅķϏɯίИèͿ',
                'ӈˤɏºԢΧЫƣξ˷Й5ϤɔŽ0ԉĮ˂ƵΨӡɤΖďź˟áƭǁ',
            ],
            'runtime': '´üԮʇЏ˴DəƏф¶їϒO˨ĒӴʒǊύʹѢѝѦƱ\x9eȅΐҖ΄',
            'send_access': [
                'ĄϺħ\x8d¡ѽҖBͷøǪmŃʑʫɑɌ΄nЖԐ(\x9eҪԟƮʋϏȍƲ',
                'Ƅνƣўɹ϶Ϯ½3ØӚԣ\x84Ԩʫџ΄ҔӶʈϝӾʕӞ\x7fƨƕȷ\u0383Ū',
                'ɘԀ˨ýǏɯ\x86ͻ¢gʛѧοѯ˧ƟǅӤЀϧɗǁϡԒŽόʖχАĨ',
                'ԕϾʴϢæǈȽΠŞѫȶ˶ŔÐà½ğ҇Ѡò¦с˽ӬϨсԇÇŤЛ',
                'θԨķɊȩҨКFҳԟ˲ʇģΫϕȐȚʠԦ¼|\xa0ÚоÜ\x8bɿƀƨα',
                'ΨÔʽ\x82ʛџӪд5ÉȾӉҠȷϹ\u03a2ӌmAɮƌҷŷJΆ˶γ¹Ȕƾ',
                'ɡðӏǱРΤҨƩԖǸǳЎӊМ\x9cԈҝԌˀ]ɡԫ\x9cŮʃѯȜʕЌɯ',
                'Ҏƕ˯ŃȄɘњʅɹɹӰΛʗŽĊˈѸȄ³ŁgЍЁԞŘΜЈêşƈ',
                'цGſѿ\x9a:ȲɨƺТ\xa0LôqǞÊĠDʻѲĭӒύ˕лӈУМƇч',
                'ԏɌχȻцǒѹԫ4ʲ˗ЪҶǿʠÁʀхЊøI¿҄\xadҶԚșχѬэ',
            ],
            'configuration': 'њɝÌʴ¼ĞȒƉͱƻD¦Ɓǀʹʣƻӥ0˄ȱñƌѨʆͱάиҠӛ',
            'permissions': [
                {
                    'action': 'ʞ|ƜșΈԥӧήˆЍȺӊʟɬӾπѭǟóȷɍǁӪӘȷV\x88Ȃϛƞ',
                    'resources': [
                            'Κ¯ʻ\x83ҭτ͵ǈʷϒʒLԮōǮ¹\u0379ϰAоʎ}ŁϬſ˂įˡÓҾ',
                            'ÜħǙʅ<ʺɴɠяUƯȺȧƳșʬƖÌ\x93ʟïӪƸůI˄şȉɔɢ',
                            'yʯåΎŅΥʤŋÓû˃ͶҧĵѺşüÛj+ƙʍ\x94ӶǌҊςɂˑŉ',
                            'ȒԖƮ˷өԩѭ˯µѫXыɚГȨΆȸ»Ń\u03a2ɇêѬʸɋȆӔӫɃә',
                            'ΨӒɞɻĜΙW\x80ȿӐЌµĩǭǲì@ŔɣҚϢѠƂҴƖ\x90óWʥƂ',
                            'ÂʂўǙ1ƞԇѼèӠύşΥ±ęΖȍʸ9÷ȵ˭Ń§ŒΛУӛîȜ',
                            'ȜŢƓ¡ˬɎĔǇԡʱԤĽɪ§ʈŦȓРȟΩгΉȶƒſ˳ÎȜχҐ',
                            'ӊ\u038däƫʠԫѾɼɼӋïЅǼ/ĞӲΪʼѧԬŧ6ӱ˜ӖҝqȎéȚ',
                            'ȝӝǿŞďĦñӉϜԡΉԥƀXǻȾϖκьӦɗӠ^ɩѡϢǿˠ\x8fҞ',
                            "Ġ˅ЊԕȻǗǦҒԀ\x8dƺҩǦԁԄĠƋīΪq\xa0ØΤĉ'ʧKiЭƔ",
                        ],
                },
                {
                    'action': 'ѠȹԥӉʪǱӲӆM',
                    'resources': [
                            'Ɗ=ȾɱŤВЪĕ§«ҜĈԌɃ¨×ʊ\x91ӝʡТӁØ~țǊ×ƚ\x8aŹ',
                            'ИāӌÜħơʢưěǜэУЦοɋĝįïТпƍчɇĂƒ\u0381ȤѠʟ®',
                            'ϸҙίȊΦȥȗĶ¶ǯɖȫgϬҍʸZВĮлǻHú΅˫ҷͱҒʚĒ',
                            'ϭĶ\x92ȹưˑԪŠʵРͰsÐÝ˞ơŶĹѠϑʪЪɉˌΖϐѵ˥TϏ',
                            'ϷʌҟŅѯѴεАʨ˕ĖVʾ¶ɳÅʻ}Ȅѵӎȿ¡ŲɎҁȌͰȝą',
                            'ΠΉʳЌʹҤωʹїФʨϋѬŸЛɵ˭ɆʼҩΑˊŧҹäƛχɝςͷ',
                            'ǾɾðǿˉŒ˂ʭǶƦw˄щЋǨɼ\u038bˤϕϟʹɷBґϨˣ˻wÂĸ',
                            'ÿƼχ\x84ϴƘΡÚʽŇǏ/3Z˭ЄʀԀ<ЈʻΑp\x86ĵâ˜ĀҲα',
                            'ŮǩňʞȓĹYΑŢǚЭƂѹmϿėȆŗȗƭŰӠ\xa0JӆɗӺθ8Ȃ',
                            'ǡüҀǣϥċ\xa0ԟӯČƪΒØƓǻʡɲʩåɜƘƢʵȠˍWȜɐŴŷ',
                        ],
                },
                {
                    'action': 'ǮόūёƬɖěʙˢȳȷӎр\u0379щ;ɡŗʿæΎɰźȴǍΞΦȖʄ˗',
                    'resources': [
                            'ԅ·ϫuǸǿúή:ǄÊԞǹӃЅγˍхЖÕºɫҢɌąюԮ˲өӚ',
                            'ϣҪʯÒеwǊƽϭϥвʐӽθłρƒ?ƘɕƺӀSVӮXȹζԢϮ',
                            'ŮЫjњǷаå\u0382ŭʊƱŔϤҘΐʒÄбÅɖ˂«ӼϪГȡ˘²XӃ',
                            'ǇØӉǤъ\x93ƗҤĂУhԪɅɯ/ƴӷǿӹzıйїԄƘɎҎ˵ȑͻ',
                            '®wΛӟϱŭXĝѧŚĭȨԏWÕѡÆĲκʗʪҁ;Ƣ˓ϖTгɀĄ',
                            '˱ȵ®č\x84єyұˎɨƑCéɼń҄ŀӨѠ\x98ʷԆʰǷԂ~ѓӤҲØ',
                            'ǽȯϫӗѺΔǇƩαӚfҪʹӑҠʖΎÄŘɎʶŨʗµ/Ѱíşԥ±',
                            'Ⱦǂȫ¨Î˩ǛԝǧРWǩДĬh7ϲȇ¸ȃWǐ=#ǋúg¬˦ȯ',
                            'ü&ȚÅþǬʰ\x83Ӵ²ǍɄśрύɓρϼĄʆҐQ^ĒȐ˟Ŷʍȱχ',
                            'ǛˑʨȇŢϢԟǤ˓Ԫɨʽèyˊĵġß˙РǸӨŧȬΊȓʄѶӨѕ',
                        ],
                },
                {
                    'action': 'Ĝ˃ȲŢÉȌҙȋˊˈƽ»ς·-үƔƮѨƖіӚнśŘ҃ғX˰S',
                    'resources': [
                            'јϱȉċȖ¯҃ʐ҂ЊųɛόҏҸ8ӈХýɭ.\x90҇·ЪƵǵ҅ԥN',
                            'ҡǢ^ˇıҾ˰ɆԧƭΜƼɰΛӳϨ\x9cШŉЛȹҞϗÝĒ3<ԀәΠ',
                            'xRԦҀÏ\x84έm¸ɜǶҩɹʇćÀиĪʤĄͲЭˠԙΐʼѧÉҴĺ',
                            'ϔǖдϔӟϊ®ӢƝʪӣЮȜƞťєŨԫҒαǐѢηӢɱζңӕˌҶ',
                            '\x83ȸģɲǰЂșȢŇʮȑћԖʸ\u0381ţ¾Ȼʉсɐ©ʪʖɗӑѭºɄʞ',
                            '҈όǛšőŗǀ\x82ȝϷÂÿƓ\x9d¥AʔƸөřǁʽˎűϽʔƥӨĉ\x98',
                            'ӊƥԬ+нϨ=źӘHҁэϧ\u0382čƏ@ʏȱʂŭΔĸȷѶĢӅѼɚƄ',
                            'ɷԞɆ3πɠњyЬæ*Ŋƕҭť\x8cхз\u0379ʦҞΐǌ-ЁΥƪ˟ΈΗ',
                            'ˏÕōқϫĵҜˤѻжȋԅӂyШɢįτɈӮýϪ\x8aǚɟӟʡɈҟԤ',
                            'үx΅Ț¼ԄɗѸΫҠ\x98ülȫĀȋμAԒқ϶аɔц\x9fŴǊЕĕC',
                        ],
                },
                {
                    'action': 'GͱϺģӤvm1Ś',
                    'resources': [
                            'Á\u038dӎțÕΐӢѷŨӈůϾҬāɌYǁ%ѯϬӑψ͵И҆ĆԐ͵ҏȵ',
                            'd_ȇӏɢѮԐҗƐԨȨ\x93OѯķЕĈͻȲdŠ҆*!Ҕȿō·˪ŀ',
                            '҂ԘңǬĹϫÊ½ȌȲĦĤá\x98Ǡ˥ҬŀǊ˱6XѶ\x83ӒϚУÀʟȟ',
                            'ˡīЕęìRʣ½ҝėóԪƟͿƚcƎ`ƂЌɕ\x8cŌӊʤàƍɱϼŕ',
                            'áōÞљԗȜԒБʀɪɹ©4¨ü\xa02Ԣ?ǇȣŽȥӗзǦðđíύ',
                            'ѸæԈӅǚϔħӃƣʖĈӌϝȕżφԬʑŴҼʛǻŧӿĺ˨ŝіǷȯ',
                            '˳ԈÔǒЅ#ӱśʉԋˡȫĂαcЬϊAϴþϻR;ГƊʓǳυϽØ',
                            'ԋѢΉņFŧØjǮ\x80ѿÑEҍκƌɇɐ\x96˽ͼăǿԔh˻ѱϫzҐ',
                            'ԑņ\x81ƍЉϡϴԥϲǕǸЋćʺ¹хäӧǸèɪŮг҄ѺiǭӪʩŞ',
                            'èiťҦT\x87ʸŁϔѵГТĽÔιɏϱŬùƺŝ҂ćΡԇοʀʐł\x87',
                        ],
                },
                {
                    'action': 'Ԅ҃ʐõВЪůǻԔīҊ҂ƉďѹϹɪ˪ǽіƮйх#ѫϴɦƏƬȐ',
                    'resources': [
                            'òʥрҪ˻ʿ\x93Сɣ˞ψΆψӞhĈԮȺȅĐьɑѤúϳӆɱԄư\x95',
                            'ԉʞƿ&ɠђ;ɥŀĪуǀѻ˽éŴĘйǯϽ˖ǪЏɂɪѝȔԊҥĪ',
                            '\u0378ԞϯőҝȨĿăų×˥²ΕϚƩЉΆȆŮƮΑ¶ćӽǳĊӦɊ\u0380ɷ',
                            'ψȔ\x91ſъȞNόИ»ɱȦƱǒˬĔšȔŘӧǛʟĢɵÌԬȧʼdç',
                            'øȫϕɑӳϑζǭə;ŐɍŃ!ѱǯԬƑ˳ϴ˾ĎˮГŁԂˈыʷЏ',
                            'å¬ɾȡ˥ϠфƂ¿ȹҾϸʚàęÔңǝDΡʤƵQĥƮqӖϕͿǚ',
                            'Ԓ}ԞҙºÍҔ¬Єš˲oɗöΞϒ˥ɂӐӢРĞΕЍďԝɺǬĚӐ',
                            'ªѰϡȴǕ:ʹϔv͵ĘԎɍÉĻҳŬФɖ£ӸɬԬń\x82ɵԩzŅΐ',
                            '\x8eʓɳӀɧƲÂїƤЬҷj\u0379тΘ˭ĽņѵЮ\u0382ͷ]ԮƳȖЂӀʜɤ',
                            'x\x8b\x9eŷĢҠƸşɰřџκκ/Ģʧǌͻ5ƫ˵\x8aŋҐϑӃɇȪɱΪ',
                        ],
                },
                {
                    'action': 'ԔΗЭź\u0380ˌʲХ˜ǕΓˆπÈЪȮȷˊ\u0379ĴŦрȨͻȰу\x8cΥƂf',
                    'resources': [
                            'ӷˢԑУл˗ǚŔƸĈε\x83Çι\x91ѭúƈŋĦЂƞÉӳǞĦ¡ʵìȑ',
                            'rɛУ϶ϿѬßϻϯϾ¸οӴˈыƊzӘ\u0382ԏř!˟ʵÞϺԚɷćӿ',
                            'ɥƂ_ÚѐϭѾő˄ÍɐĂ9ŠəӶƞŉқ˕ѺϹŏ˵ŉȞʘȂǟǁ',
                            'Σʲʌҕ¹ЂňҀǽ|Ѵd˱ҸԝǆıŬϐƺѩ\u0378ÑʁƸ#ԉЇÞʕ',
                            'ЕϢΉƕ҅зǩșyđãɉŒ\x87ФIŵĥȗŠʢÚˤ:қɌȹԇбѥ',
                            'ъǳ˂ǰǕɁʘŝÊȌăԦ±ĕĜϵΛӝ\x99ћ2ƥђ}σб\u0379z9ɷ',
                            'РćEǎКԛҽʚɣѪӦӗʹΏOĴe΅ƒ2Λŉ×τgUԉųƸƪ',
                            'Ňǔʉű˔¿\u0378˛ηƈŶQǣɚɿεηқ\u0382ԫӔʡяϿȩ˕кƯλ˒',
                            'SǐĜЫëW˽҄ˡpЄʛυ˗ЬdƘȑԓ\x9aʶΏ҄\x84ƾҷGƩǝɿ',
                            '´όψҞΘƎǯиǸp¨ԓΑʦƧԊʭðâč˩дͿjǭӔą,ƚ6',
                        ],
                },
                {
                    'action': 'íÏÏͻɸÁ˯ŔӨsƞŬ¼ƊԏBĉDҼѠУɒ˾Δѭň.Ʀǖԉ',
                    'resources': [
                            'ɥ¿Ɇďʌµ\x9cǬĞŲƕǙřѦʎгϘΟ¤ƐњƱýȘķǉœԙȒѽ',
                            "aɌӼϲ.Ï\x96ʸĹΪƚ҈ˆ'µę҃ҊǊԁҚɟűūǞΩďƾǁ$",
                            'ĞǼɥȜſȓq\u038dŸŲπԉĴşʥԕѵԥΩҪυǰѺҽͱFĔǥ!ӏ',
                            'ʱȗŶѻȆԝԠΣҙǝʍҗĶÉśТŹȳuÌɴҲϾƭтԞƦ˪ʩČ',
                            'όνƸĚӣԂsѴ~ʢӧȴʔΖЫʚ˲ęїΕǺВӀѪίʯOŜˎ\x8e',
                            'Ϧćўȹzλ´ƻ°˵xÉÎæИ¯Ĭɺπɕ`ƋЭ˔ǭϭ)ȊcЩ',
                            'ЄѨƟђ~ȼ·үȴϚYӀʍΠfõbʕÁŜʁƂсʐÛҼԖ]ʂѠ',
                            'ʙėҭɡŖ·ȷ˃ħҚʅȕҮʨШŁ>ӐĬ»˭SȳʨԙύȾѽɱԤ',
                            'ɌѡʐͷŖϞТȞԢūȄҨѯЕƉЕ\x9bіʶʍΦ˳ó˳Ȟʮɥ/Ͼ\\',
                            'ӡƆʗ:˵ЎȏȐӗ˸ϧɶĶ;1Ӎƽ\x7fƋԛҔǫҴ˧ԋѲǷ9ȩǨ',
                        ],
                },
                {
                    'action': 'À˂ŭÁlǣƢĭȨФÍ˯ɊΎL\u0378ӗˍɃʣɐЀȖtzӞѴϤŐє',
                    'resources': [
                            '»σ˙ɞɮĆ\x8bØңņ¾Δʖ§Á¸Ӷ¾ÜҶΌóŋЏбŮ˲ђ+Ǌ',
                            'ӏщ\xadɸˉŹƊҾǬԚŋЧÒɚǝɳÔΨļŹɦǀ`Ú΅:ԑƚ]Ҡ',
                            'ѶӕΊӹ҂δʅЏǠμθʠҐƨǸŔΫˬ˙TӃƌʣΣԧtӇĸЋǛ',
                            'ŚDś˃Ңү\x8bжǏϛʇˇȤƶȄүԗɋƼȄ\x99ŜʕĖӘΓʓÊŞƖ',
                            '|Żі¹ҔŠ˞Ϝ\x80ӱǫɄΰψİўǜ\u0381ж!ԟǍϥȉҿıѓӐȧɘ',
                            'ʪǦʟłκ.ƥċ\u03a2ӮϘтȫʱǑʩϗŭépԮӓιʕœÕЪǰĖԭ',
                            'ƫȵ\x82ĸԆ˂ɣЗȤ\x8eơѪ˝ÕƅϙȂ\u03a2øӧΡӮɼʕǠ@ɣӯāқ',
                            'ɽҗωԊȍ˽фǝҟІʸδĻ',
                            '°ʘˎȂҩʾΙўȓǵæǏϔЎ©\x93ʹρ&ɝÕĕԑ˔ԃÉ\u0383ϰ\x93Ȳ',
                            'ʀƧɲĕ\u038bЬкɍʹƉӑʍҊˊ\u038dӨϗҶʦ\x85ɪͽɩg?ŀѤʓӒΜ',
                        ],
                },
                {
                    'action': 'ŖΙӍƿƺҭҡűȘɩ°ж\u0379\\sи°!ňѯ˱ӰİҽǸ<ƢȟӑƔ',
                    'resources': [
                            'ƏŗӡǒųԘƧΙԚĸӀĖúЎˑύŖхӥīɈӭіĘњȩѹʶˍö',
                            'ƵԒȶü÷Ύǡ\x89ʴХʶҠùϺǑӨηǋɳ˒ːő\x96ŠǚʵƭӀЏͿ',
                            'ҳʻϲИāCŰƝ˖ԒдԋОǛКӑӪʆҮɝŰɘÂÀäúņ×Ӟ\x9b',
                            "ŪδǧïԇˢҺʔǾҲТ_AÁ'\x88ƍɇCӗʨĠĆƎfҝģƾËΫ",
                            'ÓĭѭůϘˉҕӑ]ԩʨĠϩ˦¹ԞɕΈȟѭΕͽªǍ˂ǹѷсϨҟ',
                            'ˁȵőoԔĕȁþªώɚŒĺΰȷНӈȅÓŠ˻бƟˤӅǺɩҐůɝ',
                            'аӂϑΉ1ƄǐÎ˲ĉɑçưÝ«Ϋ£čν©Ԓ˶ý\u0383ɢȴɨ·0Ƞ',
                            'ӣѨӭӰȲŁƑÎƌůŪӹ²·Ċ=Μ˂ѽлˏҙȕ¦ҳΪȱ*ŶY',
                            'ƑʦеΩɅЪ\u038bΈӳϿɊý£\x95ȁɼīȒЬvûϹ8əяƯҹcʈŊ',
                            'рϏԤѥoȮϪȦǉȶʟҋѬˡƌ\x8cĚʯ˄ʇӒğЪǒҧχȹϵƤΰ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'CµĿ',

            'version': [
                -2745726293697595104,
                -8614710202096843867,
                -2984552934778395994,
            ],

            'location': [
                'ӥ',
            ],

            'runtime': 'ȏ',

            'send_access': [
            ],

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
            'name': 'ΩĨƄǳЮғ˵ѐ\x97Ѹ/ӿ˟ǍԫvΏø¦ӃćˈϞɆĶ¹ɗɉѢӥ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '§Ċέ',

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
            '$': 'ÓȶÊJʺѧǢԠӊŲѮ¾ЦōŰЩˀZŊϾԂ\x82ɢďϿΰ˵_Ȑӗ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5047424177808945251,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 604906.0342735612,
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
            '$': '20210129:192616.808422:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ĵ?ŋɮƈġ¾9ƌϖ3ϬƗёƓȑʭŊԀːƓǪ˺хҐo5ΜҵƼ',
                'ƐůԓЂŕΈӑκÝOҍġ;ɷҒȲã·ǟӿǒȼÒϥʆΰŪ˙дȤ',
                'ƌɸϥÛώѠɹωǅϙͱӫҿҷŋȐԥĝр÷ϳ²ȶЁǈ¿љöȜ΄',
                'ĉ¨˪ʖŅζӕ\u0379ӂ҈өϔнƄğáГV©ʃƯΝłЩĭȳż&Ѡû',
                'ԒĵŸѡҼҌJʢǄżƪΪƘЙÇʲåɰԊʆĪÑоƫĕҪąŤ˂ȡ',
                'œǂΝʐӀcȹà\u038b˫đť%]Ѣԥ˵ȥıѝȦƢɬşüɃΙԀǵҬ',
                'ɏʬǳΗG\u0378ŹǙǬιȩLФпɚӤ\x9aπԜƺӠркöʠɢǰȊԍI',
                'іȖԧǕȈїĉϮԁȪГaʉǁһʬÞ®ӔɪÜŠʘĴƯӄÊǲBˑ',
                'ʲ\x8cȖÍϬƖǅŊ\x96Ļ҉Ҭ¤lӎӓƃԧπϾ˜ðϙʅЁҗљÃk˲',
                '^ӬӖǁυɺ\x8dʹƧ°ԉ\x99ȺŇҪҳǍҿԫßӣ0ЭɌ$ɴχӴ\x93Ⱦ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -8645583674276301301,
                -1670244762335499162,
                4073947233058916351,
                -6139616796337610401,
                -6899180819708869631,
                -6903863512078432207,
                254589040772349355,
                430568941647286456,
                8621389434040705467,
                -1965670742459033006,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                579479.0470492034,
                592106.0210576591,
                123384.63329486197,
                858339.2709673924,
                729622.7689562174,
                436836.960911463,
                566199.785693054,
                967621.4921639224,
                425813.1969816898,
                144187.398701042,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
                True,
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
                '20210129:192616.809232:+0000',
                '20210129:192616.809242:+0000',
                '20210129:192616.809247:+0000',
                '20210129:192616.809252:+0000',
                '20210129:192616.809257:+0000',
                '20210129:192616.809262:+0000',
                '20210129:192616.809266:+0000',
                '20210129:192616.809271:+0000',
                '20210129:192616.809275:+0000',
                '20210129:192616.809280:+0000',
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
            'name': 'ȱv˻ĕɤŔg\x7f˛˶Ü±ίє(ͱ¹ԧɄίȨǟ/\x83ӈӭɋ[ŤÕ',
            'value': {
                '^': 'int_list',
                '$': [
                    -5623138504302621960,
                    -6877400180674060461,
                    2066849571582472613,
                    -5957291004155889523,
                    2528478307892901627,
                    -8862021777195512120,
                    -7370202765628428309,
                    5015100287762597642,
                    -976846888852698122,
                    -120569638165520972,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x92',

            'value': {
                '^': 'datetime',
                '$': '20210129:192616.808283:+0000',
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
            'catalog': '˗µҊ˒ӳӟχҁˊ\x9aą¨ͼȻƢϨ±ʾÏɜΟÏԢҽ7ҕȦˊП^',
            'message': 'ɎůҩǓɕƥϮԛƜXϹȫÑŭԢюνѢɁΨζӤȫøúʬųё˄q',
            'arguments': [
                {
                    'name': 'КȦη˼ŗЎÙ˗ȺћҧǢɡH¨ԟҟ˓˸ʹǽ˹ӯ®ωƎҚҀǴȁ',
                    'value': {
                            '^': 'string',
                            '$': 'Ǥ\x93êƪԡ\x9f¦ĨΞͼΰĮɂîѫςßńʄωϪίӡőŞĽ÷ʵȩн',
                        },
                },
                {
                    'name': 'ӯӀȦѬĮˆȅɇҽέuϐfȿŽӂ',
                    'value': {
                            '^': 'string',
                            '$': 'ʔ\x80ϓ·ɳŊǳȻνĬѽ¯ӂѹǬń÷ҝçћȨЍŠʺƴϽŤԪЬҟ',
                        },
                },
                {
                    'name': 'ȠϟѣçҾ\x9f%\x9bЛÃłҗ\x85"ҘȱȢȜԇŻO',
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
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ЛΫϮȈΥȣƼ"Б|ƃ!Ȩ\x83ˊõУÃιɪ˟ʒêĞίĢ\x96ʥψŶ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        4216076545888876308,
                                        -6662592614615607998,
                                        7972342197279096662,
                                        4015375473945498000,
                                        -7934002426138782988,
                                        -239413327628034930,
                                        4472548659523599586,
                                        8685861899341698098,
                                        -2708265358609558397,
                                        3448517870777363328,
                                    ],
                        },
                },
                {
                    'name': 'êҺʥѢƛγ\x92ϽζcƶůcЄƵӊбȸԇÝʌɀěҙԬΪ©ɕЖɷ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ѴáГĐǎɃ»Ϝ˰¥ȼϞ8˾ԮͺǛã\x96^Óɭː{ǚϷťЪĥӦ',
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
                    'name': 'ǑʦȮђɼϸԤ',
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
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'Ͻ\x921ӬźɵӹМҁ$ΩΜҤ!\x99ΉҽҶǥĺӀʒ¾ʪʡ3Gπͷĕ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ԜȹʛʴрǋʐɸſШϙˆυϢҷÔʐλ˓Ƈ\x99ŶΐӪҪËдїЂx',
                                        'Ř˶ǥ\u0381˼ȿ§ʝʛĐIǼ˷˨οͱҿ\x8e0Ɲӝ΅ѝ¾đ¤ɞʘǚĥ',
                                        'оӡϕϵхEɓȒƀŀүǪԚʏ\x8dɪԈέћǘƶ\x85ǁīOˑΒřÀҴ',
                                        '"Ȑ\xa0ЉqӫԕҭјʊńȗєɘϪàϻļɡТҘԠµŬ΅ΆpΠΙъ',
                                        'ɯ\u0383ΆʡÅТ3ӜȿЄȡѯĞŒ϶¸ǀҽǴ͵ɄȔǆǝXϐɋȪ˰ș',
                                        'э˖φğˀͻ˸ĹȻʲӸӍǸΦǚơÊƲԂЌʒ҉ƄΟȓλνìƽd',
                                        'IҜʡʴÉƦʌ\x7fϵϗˊЬɅʴȑɶҚψԌƀ\u0381Ԙʴ±ҷxħҘИѵ',
                                        'aɃƞĦˌΐɅȽ²ѲʍЈӳорðȦҪŶƛŚĸ\u038bvȈΨΛʌԠВ',
                                        'ϗȹѽ%˂\\ʊҧÝôƼTIˌїŶνѿӟέ®Ήò˯ӮԩƠ[ŷӳ',
                                        'ƂυĮϩǾÓ\x82\x95ӢŗÜ҅ÁʜƂ¼ǷӾ&ϴӀ\u038bАѾƧʳѶbhs',
                                    ],
                        },
                },
                {
                    'name': 'Ǎ\u038d҆ŕōæEєĤьüŒR!ċҔ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210129:192616.807511:+0000',
                        },
                },
                {
                    'name': 'ĪĜ͵еЌƸΖŐμѧȨǩÍʀήŁeȡȃ;mE\x9dԄЕ¤ǵŚ',
                    'value': {
                            '^': 'int',
                            '$': -2852887507523361741,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ҏθ',

            'message': 'Ç',

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
                dict(field_name='error_message', name='Error'),
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
            'identifier': 'ӡЀӚųäǀǗ\x97ĴɀɒƀǜĂџԄРŌŝĔșǻȈԮŁϣЦĮȃҲ',
            'categories': [
                'access-restriction',
                'os',
                'os',
                'configuration',
                'file',
                'os',
                'network',
                'network',
                'configuration',
                'file',
            ],
            'source': 'ϡϒɹÅÉǥ\x9cîʹррɀɫ˛ЊũҏЁƨҭүή˷ʄ©¦вǫkѠ',
            'corrective_action': {
                'catalog': 'ӶƛȵфΧǩŘǦăƔӼÑΧѻӑÁ˟Ы\x85ёΪҳʱϝ\x80ÌЪȌŘҩ',
                'message': 'ʓŴχʤß:ʗƚÍҴǅɧqƯğԠϖʋʜԠ½ȌĻˆŹӊԛЪRÛ',
                'arguments': [
                    {
                            'name': 'ɑķ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'αǨΕƨ©ǉʥϦĦŻϓѝƗʚɥŨȺэ ác^ΪԨϬĎˉƝiǑ',
                                                        'ϐ\x9cӱÍϗͻƮʌ¯ĲԬüΰ˹ˤã˨ѻǹ-ғӚҿ@ѕƑƱʪҺ¬',
                                                        'oˠӑ˘Ҏ¿ƊʄʯҰƿÛ˰ԅāǘїϓўӃƝӐćΌ×\x9bȣҦ\x86ƍ',
                                                        '\x9aӪ!4ɑЂĦϾ˃ѲȎӾėʖǔψȈϸ˃ë\u0378Ɲ\x9bέɳǳ\u0381Ѯȧˌ',
                                                        'ѠjŜ˙ЍӽӲΩ˅ЂžľҐťϨĮŷɫƐďɕƔΔςiЌƑɕũӘ',
                                                        'èǂЋʹȱҞɻˮÐĨƖ,ЂƀBɐʁŇѰʖĳҒωШɿԀϒę҅φ',
                                                        'Ιˢ˚\x83ɥƷʵѨљáŮtЂ[+yҭʭ˷\x86őұӂϻJSp҃\u0383ă',
                                                        'ԨԀɢaʪ˭σʮřСҍǠñÆʠ\x91ɁĕʛɒԗҦʭЎĹÖΩϻҎʶ',
                                                        'ѠϢ\x9aϙʔȒʓǎҵ NȓҽQ˜Ҏǌñ,ďE˹\u038bȄҙϬКȂӭΗ',
                                                        'ĵкǷрʎњƟҴɯϨЊůƁʉΕȗʊеǵ;ӊs\u0383ǞĶ\x93ͷĉȏĆ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʴÞԭß£}ԝʁϚƈΓʼ˳ĺ*ɉЭĀΘԌʒКёǸ',
                            'value': {
                                        '^': 'string',
                                        '$': '×µϔŜǢćʪʠūǐƨưÕPÅȕўȸƧҦοʐҞpϩǓЖԎѮу',
                                    },
                        },
                    {
                            'name': 'ԞǫʧɘϹӳƀėɳÈqхƤҳ\x7fςȀТ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': '˕\x81¥μ',
                            'value': {
                                        '^': 'int',
                                        '$': 2004749817377604326,
                                    },
                        },
                    {
                            'name': 'ʲ9ӵìӊ¶ȯXС_ȮǴơÆğӖЫʄźŔ}ӦΫŰˈ˾ɱɨԟϕ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -6839321960524727796,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӽŕ\x98kԒƄıԏԬƠʷ[ŗιѐĕƔǪơɞΦσќӀԛҠİʦϿċ',
                            'value': {
                                        '^': 'float',
                                        '$': -59785.73211158798,
                                    },
                        },
                    {
                            'name': '˧¯ņԕҵəώHɌtЀɖŀԐ˦Αğȶԭȏ҇ёʚüҥѿ\x90ӜĬʴ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -1886348516550430230,
                                                        7966048434108621119,
                                                        -6503244865485574007,
                                                        -6749217153858762758,
                                                        8550299193448753264,
                                                        -6575579446528299202,
                                                        5369449336786226367,
                                                        5495595437485679622,
                                                        -6036125039494073979,
                                                        2341913910061076906,
                                                    ],
                                    },
                        },
                    {
                            'name': '\u0382ơJqҀӧϔFɝǣ˞ÏēүÜƫΟ\u0380',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -8069021404696595697,
                                                        1019500032175952069,
                                                        -7453755034081624832,
                                                        8281762322820076314,
                                                        942954919402213897,
                                                        -38045934508585433,
                                                        -8595610997341284315,
                                                        7990627699295344612,
                                                        -3569909201952073526,
                                                        2521207290374814175,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŃЈɢ\x98gơöÑɹÞƽƦʺԚΜҍɛϽMӕƔΐɌӓbʛЋ˃.\x9d',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                    ],
                                    },
                        },
                    {
                            'name': 'ň˩кŖɱ\u03a2',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ӜȕϨɋ]\x7fP\x8bƪɶKϱʍʳɜӍ\u038b÷ԝҊ¤ΠɌȪʕƜЃ÷ʕÛ',
                'message': 'ǙʰuǟԆЃǙŎËȫӜÖԅƐԉκӓɴʋĦVӵʻńëǙџ2њä',
                'arguments': [
                    {
                            'name': '´ơÓΰϐҟƇζÝ҅ҩòƻ˽ϐ·ǢƋƐԀäз˕¾ŀƃ΄ĔäĜ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -6071391720017010156,
                                                        -3433368184424824872,
                                                        282245158474856031,
                                                        3270597994634613824,
                                                        8026821462449924641,
                                                        8480182089739972036,
                                                        8425376431284774256,
                                                        -8085314754073974922,
                                                        3304778946998330823,
                                                        3746861720446232342,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĖȣИɛϘùͽΥWԠ_őƻʀҔIųˑʩĶԀWӐҧ\x88Ͷњφ\x9cЧ',
                            'value': {
                                        '^': 'float',
                                        '$': 293088.680130209,
                                    },
                        },
                    {
                            'name': 'ʪ҅LӠɝ˘ȌPϱϧʽΈχщѝŘȁĘ]',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -8162155403223222575,
                                                        -13572794162727116,
                                                        -2835255663225442652,
                                                        5755032955680075123,
                                                        1979919790223399574,
                                                        -8385946556107455512,
                                                        -8308342362489822260,
                                                        6653271236572148102,
                                                        4507868630111445702,
                                                        -3793891746224736501,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɼķӘïӍɹɶķ҈ǘӨЬ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -6250004574114009114,
                                                        -4976422173776800823,
                                                        2222512418627957226,
                                                        1318524786839869198,
                                                        -4558147102668469299,
                                                        -4435101234341827873,
                                                        3851630325504932856,
                                                        7645540359593597115,
                                                        -8334210230954317330,
                                                        1021426904492496712,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҺģƳάδƲũ°ηþäľʳΆŰԏҧˈӠŖҒǴҳǻπƣéʒ\x95Ν',
                            'value': {
                                        '^': 'string',
                                        '$': 'ĪșǭǴΆˍL}ǀѸșæ\x91ÔƀǊɊȣёҔ;ʥǿŬ ˧ΐѱɱѕ',
                                    },
                        },
                    {
                            'name': '҂ˇȾǧʒΊЬ±ȣȱӾücӆšÁԧǺ\x9cԒǦ˝ѡРǌƄѵ\u03a2ˤς',
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
                                                        True,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': '2ŬӅϮ˩ОӉĔrˡѠЗѴϲĒӻԏĉԃƚӫѺ',
                            'value': {
                                        '^': 'int',
                                        '$': 5335181846247600327,
                                    },
                        },
                    {
                            'name': 'zȳɃԎ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ҨǞȯʹŬˁΣЦЭǈΆʣДϔӤӖсЃıӗɮǵʠ:ȥάΎʷƻѲ',
                            'value': {
                                        '^': 'float',
                                        '$': 223881.7819930152,
                                    },
                        },
                    {
                            'name': 'Ϫċ\x81ÚʐӣϦʝÄΦѬ+ҰеѨҳǇԗȔSȧɟɮͽȡáǕΧȻƥ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ҖўĲÂԂ',

            'categories': [
                'file',
            ],

            'error_message': {
                'catalog': 'ϾÔ',
                'message': 'І',
            },

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
            'name': 'ɀϿ\x93ȧŘǃjůӖӦӌ\u03a2ǅÓɼUԒǣƬƁДԑÁњŉиӅ$˝Ӵ',
            'error': {
                'identifier': 'ӷͺğ\x9dÉΕćƩÙ˄\u038dɜдƢ\x8aĔġÒŵʖˤʔѧ³ĪАͷ¹Ҁʪ',
                'categories': [
                    'file',
                    'access-restriction',
                    'internal',
                    'invalid-user-action',
                    'configuration',
                    'file',
                    'file',
                    'internal',
                    'os',
                    'configuration',
                ],
                'source': "˥ůĨ\x87ȤӄɘȦσǹăʗѢҕϝýĪņԨƏШʟ'˝ĒӅɪAҷƠ",
                'corrective_action': {
                    'catalog': 'ϙĪũ¼ĞɎʗɁБǏƓKˇʋɵƓsϖΩÌŰǼȂϳƬӘԥ\x88ɢƴ',
                    'message': 'ȣыŀϦæњÚφѧͺʟʟԞ˘ˁúɛϨ7ɝ˩Œȿе\x8dĢťOʼ_',
                    'arguments': [
                            {
                                        'name': '?ϋ\x91ҩϯʲȩªɑŞŝԗκƨƽǱ˺øĢ˺ŢѧԑͰӡ˱Ҝ҃ϖҮ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            773051.0284475173,
                                                                            319622.59853338124,
                                                                            556113.8009802776,
                                                                            740292.2558772159,
                                                                            469736.0965351118,
                                                                            565237.4155201991,
                                                                            -98714.78263962019,
                                                                            998878.4474198162,
                                                                            140095.25130297727,
                                                                            173515.02750081703,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÝǹƫώƦ7ģԃɇǶƀ˘rȡЈҷ˵Ã\x82ӠÜυ˜\x9c',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȋ˅ňʭǦΉȳǗďʋȭѩΖɧGҋÚ.Ȁ\\%хͽə΄ʙӮ\x8fό\u0380',
                                                                            'ʛîѰѭΈӜҀ\x8fƹϟ}ΡðȷU\x96ɥгΞǺҌgēԃҼƩΈ˙˳F',
                                                                            'SрZкӆΓʦѴςȽ\x92ϼΗʍ˻-ǣŁϐǱ\x83ȵғĥêәʿЃԉϱ',
                                                                            'ϋƜԨʉӜҾɆЂąҙǉĶɊðFɚҨȥȠȁːόȿӣʶʊʵw\\ʎ',
                                                                            'Αõ˷ȆΒѠλîҷȲǙƺŰшԨмЇѻˇƃҋ¯èŘƓά\x86ΐԪд',
                                                                            'ɪНʹŧűӝΆԉѓɳa˼ҳοŴҶźԁxӏӥĖÒ˝Ȗ˥áB<ȵ',
                                                                            'ҷFȻgчƖΏDŨ%ơPԣéπЕмÉǨӱȩΜҐĒʘԘÍӄϮŋ',
                                                                            'ҏÚʄȡӜԧǦǛԔǓΒ¨υƉƵũĦJʤ˹·Ǔš-ǏҀ˱ŧѱă',
                                                                            'ЦԮЪ¾\x7fɞҩΌӉˆԍѮЂƪĶ˷˕ѯԓȷӀҽʼюӘ\xa0§ҾÍɨ',
                                                                            'ǜҕçȑϔиЯԛƳɢ҉¿ĒTҨҪЫğӭĸȡŢlśũ˜ӇƷÁƘ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ћ˔ӧàτǣĘԌìϥ5ʹÔˊǑКощǥrǛȻ˺ƟҼŀɶΙɂƵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210129:192616.797444:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ȣχ\x81ɂ˯ˍÛɼԣƈ˝ƏȴԚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210129:192616.798062:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɫñӗƠÁЙЩЬ˟Ӣ\x8býӪҊǾȠͳ˴ƚҹͶɺiҸğøʰĵԉ˪',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӰѿȦҕʂѩИÄƙƝˋƹʘηѻԂŒĹΤѝ\x9fȍ;ɐȱ2¡ƃӐϫ',
                                                    },
                                    },
                            {
                                        'name': 'ΩĤɇ˴ăӶÂɩϗɋvǭ~KʹΨĆԇ\x85ĬӘ\x99ӶČʮԡҨˊѣ\x87',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4035234765375314746,
                                                                            3484608321952611700,
                                                                            7408342655981068233,
                                                                            5189542290733799237,
                                                                            -5175385520562448663,
                                                                            302620738211482098,
                                                                            1089005640405721178,
                                                                            -1641189174978581347,
                                                                            -2755646359224877739,
                                                                            5511298239042129096,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǊǢȎжéħӠ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -275789514203672536,
                                                                            -927721612548631719,
                                                                            5917493989312495226,
                                                                            5557238840080413023,
                                                                            7403599026900158349,
                                                                            -394187555866148056,
                                                                            -6202160743823545652,
                                                                            -5752214181441980388,
                                                                            -4785946248399117397,
                                                                            -7354060093715597425,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ι¬ђȎ¢ɯÝǞǊȋ^ӵś˩5ˎ\x8eǏҼƧ<ɕԅqƤ˸âӝѹе',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 386693.8713873852,
                                                    },
                                    },
                            {
                                        'name': 'FĘӡӋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ÃūâѪЗɌɟɝ'Ԧ\u038bˣϤ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'τҕҝƦƼȼƑѼȱ\u038dѩӑȉMʰƄ˸Ԥ+ήǡЕ ҂ӯŅѲPФΩ',
                    'message': "Б\x7f\x8dљϿˍӁшΔ˲ЦπѬҸ˟^ʘЖ²Ɩ;āɜΰ˓Ǧ'ʉ¬Ǜ",
                    'arguments': [
                            {
                                        'name': 'ȞϩӅ\x9dӘӀПϏWǞÛǜѵАїǄǆӦԩhȝ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƍɭǣòƸӥʓӝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 304319.23099182313,
                                                    },
                                    },
                            {
                                        'name': 'ǡā˝ɫʽ˳˃ſĊ˸ɮÂқʉч±\x87ӔưſĠԫю˗ƗyɅǶǄӘ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                        'name': '¶ԣʻŶ˧',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 488735.6569753728,
                                                    },
                                    },
                            {
                                        'name': 'ԃɰɉǝμҹԫԐϠΘϢӮƖӾϘ͵ӤӷΫȧ\x81#ɏǣЀ±Ⱦʁ~˪',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6555771824942570409,
                                                    },
                                    },
                            {
                                        'name': 'ƟԕƮƁȲƶd\x94¡χɈ4ȕλȥżҚ˩ΛҢœ1ôřЃҷ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1962752484667912936,
                                                    },
                                    },
                            {
                                        'name': 'ȾқȃҰӕ@Á˘ȕb\x87œ˟¡фʪʊЂLɎí',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '^ŎǅʼʊΨ³ȔΉĄʙшƬˏɹӃύȭYǾƞΥǳҵœЙԎħŃ®',
                                                                            'gɟЦѨτǧͳÑƕԎѷċӕjҵрлǇӼԆǴ˧ӢȬ^Ŗѩ҂ҽӢ',
                                                                            'нmȶоɘƅ˸ϝȎ,Љ\x9bʏŊŋË\x8fҺ҄ȢдȓƭѱǨɱɎĥɿ_',
                                                                            'ǜТѯԪЁҩŵˑϰӦθϋΩϷ˱ǟдђ˷ǓѷʞÔŨϢϼƵßԑԄ',
                                                                            'ҕϿŚˠΣřɅƥϺÿȲϐ2ŇʝҺѴ¯ɄĘѫŠԘǬǬ¦ȩΗ-ʲ',
                                                                            'ХҘ[\x86ʕYϞ.ȄÕЄʒŹӕԦԪ\x98YќӼōƨƨԌ!ðӂӳŵƬ',
                                                                            ',ÊʆɷԣłϴïŞÚΉƟĩ\x97ԏˀωƆ\x9dŹ͵˸ҤĺӏЩƶСˀ£',
                                                                            'ȴ\u0382ôÙϯà>ЧʹΣ\x93¡ҤѲ˟˙ѪƦƞ ӏΰӌ˦ɊґȽɭΠH',
                                                                            'ԁαȠѱ\x96ζȅɱȲTlҫƾŜbϴӈɨэ˳ÚʭYɼʬûƻĤǅѽ',
                                                                            'ԅŞ˷ΧѬ҆ɰԀǑŤ"ÀĕÑӴÄ\u0378ǴϙȠҁϡˈ\x8føіȹĜӏΧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ґʓ˙Οҋӹ.ȯˠ\x88¿ƶш;ųώDͿх1ʿʽԝa\u0379ƴϙϸ\x8bô',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            810121.2959636871,
                                                                            346389.19147196354,
                                                                            335877.73010293086,
                                                                            -65861.4134914334,
                                                                            103035.28484814803,
                                                                            157405.81484913934,
                                                                            -76612.15549172973,
                                                                            341178.1456842753,
                                                                            156145.71631412566,
                                                                            368011.34070928383,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ďӞȅƆѩĴνňҊmӲҀǩÀÎ0ÖӚәȢǤʡӚ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 563425.3964590357,
                                                    },
                                    },
                            {
                                        'name': 'Ұ2\x88νӌƏϱԤȫΞ_ϐӇѬ˪\x8bȉƼΡǗғǎЈbɛa"ыđɑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                        ],
                },
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƠϨɁ',

            'error': {
                'identifier': 'ɆŠΏϜL',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': 'ЉΙ',
                    'message': 'Ÿ',
                },
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
            'event_id': 'ɡЏƮƣΟ:Ӿ\x9bӧҸĄqÓƌӨԔɈўƉϚıĝȻĀ`ΔŪ×ʜb',
            'target_id': 'mDІȢϏЗNЀԧǦ\u038dɇƴҩѢUǜVċҷ¯ԊͽюҒĽǼʪtπ',
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
                    'event_id': 'Ѣч\x85ˤɬŊѭǕʱІҭʠɴȩƫˮ>ƊͿʚϦĈźǈɕ\u0380јεĆƑ',
                    'target_id': '˅ÀǺĄѫǝűŤƬǿĠҵўʑś:ɟƗϚsäҁ͵˰ǚɍǋ˾Ĵе',
                },
                {
                    'event_id': 'ˑőˤ˧KŚҍρƶӓʽˋԋΆŸ\x96-ĄƝƠÁĆӶĜɇăƇˉԍҍ',
                    'target_id': '/ǵǹɞіӽϗ˹ώˆQӂ҉ȄlȾɕƟРԉH^ҡΖӘ&ϒȲȵĽ',
                },
                {
                    'event_id': 'Dˉȩġ-ȂƞϷØƢ˯ǂʒGżψϭȴӠǪŉŕɠ»Юƥ}ҔЛø',
                    'target_id': 'Ŏ˷ŞЊұ|ГʏҸпԡп˥Ǯѧʿʻ˄ˮˮ˨ɞȾĴϖnԖϙʊĲ',
                },
                {
                    'event_id': 'WΌМǟѼɺǰҡƟѢĆМƝbjϲӹɫи˱\x82ħ>¼л˫ƗŲˤԐ',
                    'target_id': 'ĒӍ˳ԧȭʹŗˤʸҗǫҬЪӟӎ',
                },
                {
                    'event_id': 'ңǓΆ4ĹӀѳNϯҝȲ\x98ӘӃŒȋʄɐmĹϗǏҀɪεͻǃȘЃΨ',
                    'target_id': 'κ«v΅ŲîŔҀƨҶΪƢмjϮϥ˚ЌϺΠсhѴ*ώԝȡƝ&τ',
                },
                {
                    'event_id': 'ƜϢӛҜ{ÏÛͳmθsǍ˖Åƺˁ*ȣӖΡʕÏƥȑǵǡʈȶʘƌ',
                    'target_id': '`}ӞƴΒžʶљǳ˹ԊʑҲȺǵϖͲϝЗȑѓтΖ§ԑËά(ɘВ',
                },
                {
                    'event_id': 'ƢҥԊӖȳӻõŨѷ΅ңÜˮԥӝєǉԬΜϙʙ¸ӞφŻ¶ȇϾ\u038d\x9b',
                    'target_id': 'ҧΟʉ˥ƔŭϿƐýɐӁˤŹħɪтĦϖƶǲŧτϾϣøћʡԕϋЅ',
                },
                {
                    'event_id': 'ә˴Вȿĺ"˺ŇÿϓɢǠÊӱȆƍҁĔ˸źĜӕƱĜҦ\x84ŪɱǠÐ',
                    'target_id': 'õȗǲÍfeУӌӂȰ\u0378ʿǤǑú˽Ȅω&ϢɠƫÜѹӀ\u0383ӳʋͰɟ',
                },
                {
                    'event_id': 'ӑҿƁМƃ˃\x999ˬћ\u038bƐМ^Ϥ΄Σ˵ɖȿïŉŁ\x98ɂʜƭҜϡ˷',
                    'target_id': 'ԐˁӆҜ¹БûǲəѠӕʘÓȽϣ\u038bӶќϔ6,ξԗӡҽ\x93\x98ʪΚ>',
                },
                {
                    'event_id': 'ͽ˴ϵęŠѤЙԈŕӕÁʭʕŃԇ[ӦӔĕ·ˤĞɛˀGþѺѿȄǶ',
                    'target_id': 'цƂҊΓȥyЯƃȪυќȽЗʈɪќϳԮrĉǩɷФʳҙƷäǣԎζ',
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
                    'event_id': 'ǆzӊǒǜԘÎǃQǣmȳ˻ȧϼȧÇϹҺтԙǘ˕ψ9ԥϏӶØȆ',
                    'target_id': 'MΚӼǽҿʫď҉ÉǛĲɳ˴ѝеƝĜǰĭƞŇʷȠǂªƿԋњӋŗ',
                },
                {
                    'event_id': 'ОȐȅțɯΑ\xa0ĖƜӲ΅ҥúɳǄǟ҃иԠЅˋϲéĎsƓҿ˂{Ӽ',
                    'target_id': '|Ңɹ@ūĴΨϾϷǭʠʪΐÍÌǼǮӌěǔѿȆňŚНÖʐϊӵӡ',
                },
                {
                    'event_id': " ^ĉǳ\x8aԔȓʄә³ξԢ'\u0382ȩҫÁƌԡҝϬlFǈшǞѩͳϏƶ",
                    'target_id': 'ΔͼӏѡÆȯƬƲlӋѲоŢAʷˤӋɻʋȾЄƋȷŔĹÙӡȂ¦˾',
                },
                {
                    'event_id': 'ùʘĽŌ϶Ǹʲ\u0382ЍϤƁԙ±Ü˼ΎØɼϒȍȖ˗\u0379ĺʎ˭˥\x81˅\u0381',
                    'target_id': '3ȩ\x96ђ\x911˧ɉ˒ǘˬHȇҡʌϲįgԠcƝĥȖĦƆÝŨiĳȥ',
                },
                {
                    'event_id': 'ӳɩɳ\x9eĝŪŁΡ©ɖ®ԚоҀŀǁŎԓɺĸȠƈʤнԙЅь»³Ԧ',
                    'target_id': 'κԌĞøǵČХԐ\\ǆҿ\xadƘϽĊyāοœ°˹µ¾ǠÖˈŚοӴɶ',
                },
                {
                    'event_id': 'ũņrȨƽÏȚʚġξsɝǣDHŞ˔\x84ƍѥďǳ%ȹϞ\xa0ŕ˷Ή\u0380',
                    'target_id': '&ǛaҐɳǿ\u0381+εƙŴзНˋÔǆϭŽϺəӦӸbȽĩÈԗӅϖӳ',
                },
                {
                    'event_id': 'ϭʕȈΜƄÑŬǁIťí˸њΈƷʹѫČƙ(РˌR˂ʼδė/ˋŅ',
                    'target_id': 'QҤʛƘȸєЭFăǸ¼ʔ\x98ƷŇ¼ϓüɡɿͺɪ˧ԋöĠΟŬċʎ',
                },
                {
                    'event_id': '/ƁɻƵ!śƨ,ƆÁƻɄɘȾƱĝ!ȴԚͻϒԀ\x9dԐΝǻИзҚӥ',
                    'target_id': 'ȾK\x83ЙϘƩǲӀƱǘˑ\u0383ʲњӶ˗нБǮſʍŎʤƥтˣɞЫăʆ',
                },
                {
                    'event_id': 'ċȽϩ˔ΛËѭΘʆUӧǑɜЛԢӲΜǎńϠӍ˸ÿÏƉɈ\x9cДТʬ',
                    'target_id': 'ӆǈĶŧЉԇϗġͳuӟ҃ǦЧYӵªΘ˞Ƴȣʐʩǂɫ.ĥǼҿĎ',
                },
                {
                    'event_id': '҂ǉƝκϴҗ˪ͿƕԟƙϻΆλΧȭjŽȸŻѻʟƮҚҼҙȿӘH)',
                    'target_id': '¡ȳӢ˽ĥƺϵɾ®ԪʗҶϱϺ6ʋЍ%ŌϡƌĉɬІGůўǦκҵ',
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
