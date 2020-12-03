# GENERATED CODE - DO NOT MODIFY
# Created on 2020-12-02T23:38:25.081051

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
            'action': 'ҹ˴ƙԭʠųѲǊȔʓǗĲ±ҩөƸѰҎ3ˇӷħ˶Ӽ˃ЂûSĸč',
            'resources': [
                'ɼћʖ\x90ҩԩѡȢԕҝԁtɼ˪ΛҺƥëǧʈȀˢɮͺӎј½ɩԂΓ',
                'ӥlƧęÛȊӛͰ҅ƺεßΉƏſЎ˰ǂƁϝӨ>ӁĖԋɥƼӴѣŊ',
                'Ľкƛěĳɫҏ\x84ӝңÉʎĸίԓðЁǢ\x9eӁ\x85ң˭\x96҆Â˯ɹΜȃ',
                'ҤЈÛɃҚŋȭʆӣʕȚӲӃƕ˨ɌǕǏ#ǖȝȌΥOА×ȐϜϻУ',
                'ęXēŔĶ¯gƥйį»ʴїˡä3ȓǺԊӑǚ΅ɊηΧJŚѐҳ˱',
                'ɧЇh˺ŞъіĭƹɾΪǇ\x93˼Ӛ£ϞԆƳēǌƜǤǋӡѪ«ӊЬԙ',
                'ŤƣŶŹȋɋӫęņҷȩƯ\x86ŶЅ\x92\xadϺѵ˽ƦϬȑǛĊʿ×˕δǧ',
                'ԋёϬƄϡ\x8bƘҾ\x83ßƗέǊ˔IōȖϱÆцʳ˨ԐʕϹǝ˞\\ήӣ',
                'ˆ˟ƂћϭȈȿѥǮǭǻӲȤԅΪƖЙгʽbÿŗϠЪЙӓȮĿβǠ',
                'ϡʓҕĊƢžƅұ\x99ȐđĊ˥ʇĔȑ_nҝĬфb҉KËχĩʬӓʉ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ђ',

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
            'identifier': '\xa0ҎГˌǌҫƋѻЄѓPʜσɐƷϓĹ\u038bñӊѢϹҕưԇÆιȅΧƻ',
            'launcher': 'тϸД',
            'permissions': [
                {
                    'action': 'ʷ@њƉÓ\u0382Ӓ˾.ɳƣѺȷӘλӊҒ˴ǖɹŤѽǠΆƝѹŝ8ƕӗ',
                    'resources': [
                            'ϲǲƉΠȎΤËƲȺÈČʬԕǞ·ǥ¿ђШ;ƻƐҺӂНʎöǲϾϒ',
                            'ǈϲхΞqЀǨɊŋˉϰƶȩЖäÑ£σӠ4ƑŮǚ*ҕě;ҡЮķ',
                            'ʔŵԢ§ɩūӪœїĥqȒßɜИÜȥͼ\x9cѻɺ:ːżʱɧπұӪԮ',
                            '˂ȡȾmÉʕűļѳӠΖǜȳ¾Ȋ¬ʒʗӺɮȈîˇƲĻɷĈԐӐĒ',
                            'Ãφ-Üү҅ȠҳĬ"ÝĿιȿ.јÄԋυљ\u0381ƇɵάjϘÂӜӡɈ',
                            '˽ĂŠȅѬͱӇһʈDЌŤʙȢÍÉȜ˂\xadÅȣă7ԞԆµϴȢƗ|',
                            'Ĳ\u038dҰÕЁűŬʢɃѾǢȎǰΨӈϞʃҀқиbСȀԈ˭Ά˷ɲɩά',
                            'єͽȉŀƎʘ¼Υϰϑεϲ\xadŁŀǕɧɁťɉқάΕƲҍɡԛА¬Ԑ',
                            '˔ϊИƅȫӃ˯ŬǞȅrԟѺrȖϥIɼΑĽcʘÆɴњДǊƔŚɥ',
                            'Ęɒ҆ǍΈēҫƟҴзʊƣιǆ҆ɆѨңԡU~ӓż\x93àԆϔƚϣǷ',
                        ],
                },
                {
                    'action': 'ɀéˤ',
                    'resources': [
                            'ǑҬτɠԙΜӋǀγҗѭ˧nˊºƘʕųрȅѿҗгΊ=ɹӇθυ\x8e',
                            'ŴƞȱǜŗўˍƪȡΪԙӡɗǺɁӫɨɛԠфԤ҇\u038b^ѮΜÝͶĥɴ',
                            '˚ɢʹѴԚԝПДVUÞϝͻʆϝŔǗƏԜ\x9cŔȄ§œǬѿƥџЩ\u0380',
                            'Σ\u038bƈӎƚљÒɲŋΏġѲη\u0383ɗĘͺôǟiÌʉĺÍѼǺȇΝԅÜ',
                            '\x98ŹɘһιҼ2ʹÒ\u0380˓ņϬʡҲʹÄɷвƚƼƛŶɋ:љŝӖФҟ',
                            'ʛȰȱŴӫϺʜÓôͲĉňǌǉʐɽɉŐǮνȶ˰%іΗoƈģʰӑ',
                            '˫ΩŤӛ˧ƞєƖΌƬĪϭąӬŢFƏфȅǠƜΒȭȵǭұΎϞ(ɧ',
                            'ЛўʳƶʮDŌћϬҙȒȹÚЌħҢҨ¥Ƃ˶ɟɂҊƜ˦ɬӁŴӫę',
                            'Ҭ˓ǃdɊ˺ιǟЫŞ\\ǀȎtɒЇŃĆȿďΡԅήƌӽϹӞўаƿ',
                            'Ͷ{cǈЗRҿȘͼÉѥȺ\x83ȟ\x94ɵĄҺSΈ˧ªŵЭԃʹʪϦԉ˸',
                        ],
                },
                {
                    'action': 'ҭӳʓȷԮ˭âЂԇrӊȆʈИƯǠӆƻmʎχΞÇεʬˤʹшɑȄ',
                    'resources': [
                            'ǲʡѼвĨѵӆúĒͱȔKʻǃԏȰ;ǨeӘȓƬ˂ƋԧȾȮπӥЈ',
                            "ɐȂύǣːɦːӨ'ҶήǎŋϢёАҜİų\u0380ǘƁϘ0èҵҚȮ-ȋ",
                            'ĦЍ˶ӜѶƻƏŤʱƓɨ҉ϽҮ˦҈ǅқ)ґ®γΠ¨сÌN£/Ƃ',
                            'ǥҪʵ˅ДǵʈǏɁѾȐ˨ЧԤӹŝŹɒǰұүнĆ<FƁό˦ўɁ',
                            'Ƣϲʜ˗ςнÆɱɘӄϠƻλǖĳΟʿ\x95ĴǇϧӧyͻԏĜԖɇȳŤ',
                            'ԕͳПǼϺқҝƦ.ĎҶԂˮpäѷЖɀ˻Ʃȁš¶ųZ҅γƏҺɊ',
                            '˩ƏŢʁƌǩ\u03a2оʻ˺ƴáűŒ˳ϧѸξȷ˯˃σѯνƖÍóƕ˚Ȗ',
                            'ԝěċѦͰкьŻżΛÌѶ\x8cʲϙњźЉϾӹʻnӟƝʾѧΫÜѸЎ',
                            '҈ʠξӈӹïëȓΫϒёȀ8ӳĮʻŇĘ˛\x8bŠĽсԬҶɐЮҠϷį',
                            'Ѵ¸ęʾϪΕɵ+ҋǆĪʽο§ƴȖʨˠʫˬˠðҸ˓ϗˑɯҍ\x9cЊ',
                        ],
                },
                {
                    'action': 'ҢӵσҒҵǮũ¿\x96ˤƻƏϣӨÛǾХӯxƌҚҁʶŝʴ0҂ƨȵӦ',
                    'resources': [
                            'ЀɈȏǆ˒ďѡÉӐӜѵǵÞǩЄ§Ӵ˸ӃΛĖӿΚÈԆӊӁſқɴ',
                            '\u0378mƻĺϗƇǀԂ9ƭˢ°ũѨƃ¡шӐȔ\x9eġˉÄ±тũӣљԕŽ',
                            'T«ǃȩʗɄа˂ƃƶsΆфQʈlȎOiϐʏɏˮϹƚцÏŲåǌ',
                            'ʾԙӭԕԀȑȆĆɳȮʱþēf\x81ɉȞƑĽоȘĘрȄǩǅҁVƟҙ',
                            'ӏÌÏŹ˺ŀʢЅόΪÚȜéȵəėӟЧtτλѧѡ˛я;Ӝгɟɐ',
                            'ˡʌ˅ϞУȐ˝ԁ"AξέɾǨĶҺЦıŎȌˮMσɢɋϙој¨ʆ',
                            '~ͼΡÞӔpΉƦŴGЉƅAͻ˖ϟбȭ\xadϫŶƿŋ4šŎǰ´kч',
                            'ȧɰɑц®ɡʟɏ˓ȺӵˣųҪŞǛôѐԦͺ.!ȟȩƯ˖НÕЅї',
                            'ҧlźѬʆϯǂ˰ʡǟÍ\x95åĕȺɄ˹ƌƫѦŴˑƩñ»ʦԔΧȣ˹',
                            '͵ʵǧǿɉɋ\x93ĆԛѸƋïłȉΨɕѝāĂыүӦѭҧԒαɘЉΎĜ',
                        ],
                },
                {
                    'action': '\x8c\x80ΐBҿȐѻϐßӗgÏ˅ȄӾǷў/ЭϛʴлɣèI"ß¾ɳ¸',
                    'resources': [
                            'ˤǲ0ʙǃӄÔƶԏɭʆρҦʋɝΏ·˽ʴ\x93Ǎ˞\x8cȐбϡɓǏС4',
                            'ĀЖaцʘˇʻϱĵˡʄȜǑϙŚϭʓʿԧįԐź\x88±Èʨϣ҅ϦɁ',
                            'ҀЂ˛ǂ˼Ԙ.ŮȤÈԔƕȤǖŵƘӓ\x88ǖƙ\x9eϺhìƜГ|°ϏЋ',
                            'ӄЯÆŽVԚԢ˖ČџÊď\x92ʊśӁΡΦюҷǚѣÐŴĿѵƈĕəǺ',
                            'ɳŋόȘɼΗѝ`ǥņǐŅʆьʄϙĞ\x99ʾу˻ʸɃ±ЖʐϪѡмΉ',
                            'ʕ\x90ȧĭќϻ҅4HĖѪǏϔď\u0378ëȺȀvҁ¹Ԫæѧ˼ęǵȌØǰ',
                            'ìϩіԉҗʼЍЭɉÑΗ\x85ʪɖŹΥƅĠѩɥƃȢπŕӳʳÄəЊ¼',
                            '˟-υжҾƙʿˢřCƆɨӫRяђĢҔȥΕϜÞԮŁОʮԜȔЅϖ',
                            'ŦǄ˓ɀʃ£ΧɀZŵȍďΓĠú&ðĞΡӾТŀЂÔƦʹƧϩ\x95Ȫ',
                            'ů΅Τ\x96Ƙ3ԃì҈qӓȔҟ҆ͻǔӇҾëÙȢԁǝˠϬќ\x8cƏwʤ',
                        ],
                },
                {
                    'action': '͵Šƪ˛OЃȈă(ƫ\u0378ȞŦĮҡӴƓƐԄ҆ϒҲҤɋѦɈώɟʥΧ',
                    'resources': [
                            'ӿͼ҈Ϻ҇ˠӑҝ\x94Ȋ\x86ƄӭȰɫԕЀԈȫӂ˥ǶҙѸrǢȖ~ʭɵ',
                            'DőǕɗβοϬɐɘŶӜҒȺ\x9dRϟĆ\x8c¼ЖυΙ4ưŪрăΡăɥ',
                            'ȔΙȪгȫǇhԛԣˆěȡӑӷʨÖĐӃːƸΞʕӁãɳвҪҴ΅ϼ',
                            'чА\u0379¹ˠǰʉʯEȨгʣɽ˥\u0382ĂźәԥˏҫǵԪѱ\x8eӊΛőʑԘ',
                            'ų˖',
                            "ěǣÄ҅\x8d¼'OӦǲʼȮϺƀω҂´ǿ˭˸Ǭ\x94ТĿʷκ˭ϔĪǭ",
                            'ӭ˱ĀǆZЧŬÞѣĂȶЊϗŒ^γ\x9aŀƧŃ˪ϾʐЅ˧ВŒǘӯЇ',
                            'Iž\x7fqӿʒɡȀ´ȋĎǽǉɲ\x88ԒȐģʨŨ\x8f\x95ԖĲԋĽǪҧíɲ',
                            'Αɚ8а/ɁåHqʪͽĒp˚ќźCǪюӪԒɐǛѤɽρãϱŜό',
                            'ΧМŵÁȘƏɜΡɤ\x88ʰ6ϑƝLΞƠÙʈƅԈЅЕȨ˾[ԂўӭƧ',
                        ],
                },
                {
                    'action': 'ƂŤЪϗѢʃ{ӵ!ʁƇˉPҼΫǇмЪmÍӝʆ9˫ӚӵϊҍŲʶ',
                    'resources': [
                            'Ѫɳķƿѵћ˗ȷΗʢȄĝђӀ\x94Ώ!ȎӋĺӭøćçu˨ʝĳόƕ',
                            'ԩſɽɡϤˤ\x86ҁǂȦǵЄԫҐĢʴƙҞҊɅü<ƍόɅӶ]ҜŅʐ',
                            'Ħʒ\x9cӖϭκмɹӳϹԮȸȠЫĘǤί$ʺӅҧɻɄˠϯс˴ω8ӓ',
                            'ѥщљΔǜǏʪΎӟǘƫʂƌƦҁǘйŹƩ>ļȀεЃӽ\x87ƫÑɐϒ',
                            'Ȟԉ¼\x9fӑ҉ZŠѽˈƜʄ?ƌ`ǖǡǚ˩ǖƛƊ¥Ƞθl\x870ҁƞ',
                            'ԓƎ\u03a2є\x82AʛѮϧȡuʈȥΦŌ¬EĩŰďдϱԖħ\u0383ľŭƮʈЌ',
                            'ΊΦǞǮԐɳө\x80ʢˀԨ˚άĠ΅Ѷҟˇϡϣ˲ǉЉ0ПєɑЩ˂<',
                            'Ƽ\x85Ңɵҵԇ˺Ԛ\\ӲɱόUɢμzǸѯϨEѱůзЙӆdɦїƛ&',
                            'ԆђěȢjŷϼˋ]҇ϵĎƠɻŉԛΰіĘϖҳ.ԨɞЃ҅Í˨Ѩˬ',
                            'ãҍөӹϩɱΜC˧ˈUиËГ#ʝIЕőɲÃǬ˝ɫŮǙӎçɕ½',
                        ],
                },
                {
                    'action': 'ѤćƄ˘ѐԏƌșгоjÔЊӾтǛԅͿ\x94;Љþϥ\x8dϵΈиԆˢǋ',
                    'resources': [
                            'ŚӊɵЫҥɳćԤχΘŅЃҌéȚÍȖŸѠŘϭǼõʭǥ\x9c½ԗȖŷ',
                            'ˈԚQ0gӟҞǚʌǩˑӆxˬ\x88ŇƢԒʅȯmMőʧȄЍŞԊƑϮ',
                            'ȑȔ¤ͼѦȜІэťȆĝ\x8dӔԥ˔љѲӊĦѳɧF˯ƟʐĄϖÌʔό',
                            'ťǫΰɡϠ«ʐØҒ',
                            'Ԍʰ\x91ΓɟͶǢѨ˹ǵцϯјɿƝĉ҇ɑΕѥ΅ǷÌпɆɫȬoōZ',
                            'ǓɟɦԨʟʊ҇Έ˹ΑÿЭôІȾӛ\x84ɞťнƦ;²ʙѯůßĠӇȃ',
                            'ƖĨθНσQҡɓ¹ęӞӄͱӾ¼Ќњ\x9cɾʴʥԆǠȜǈƂôǆɠ©',
                            'ƈƈyſʢПԙ',
                            'ʢƨϕϵ˴ĪĵΕʹɪyфưŇŌʹ˘z˽ŸŨMˎǿ>V±;ĘϤ',
                            'ǸнŌРƃǓПĿёλ҄ԉǋГùȡΣÚѼӥǍѢȓθȩʛέƳӿ«',
                        ],
                },
                {
                    'action': 'ďѾʫȒѶΩŷȰĘΚʏäҐÞdǧÄçFϋdҵϑҡ8ūӚL¤Ӄ',
                    'resources': [
                            'ǁΖƩӕАЏŎīʠğяЌʒӂ$¾ӉæŝӒØϝʓĖϜͻɄʂӌŰ',
                            'ǟ\u0379Ѥ/Ğ²˫\x80ӞҔƘƶŏӺǍ˽ѕĮȅĂĢѼυӑҰɭ³Ͷɍȫ',
                            '\x80ċ˂зǊUȕ&ʮ|3ԝѼΪ*ϖȩϑ҉ϟƫæӛƆɢÕ҆ó¢э',
                            'ί}žǽę',
                            'ņпóɛϰȞqèù\x7fKϢ#Iκͱ\x90ӿ»!ШųϧκιɬȍАŎ˰',
                            'Ě˄ԔѥӰΓɗ˳юЏȨƹ˄ˣȦѷˍǖɖȋȜŴˣԐƣãϮӺ˪ĭ',
                            'ƥƲƴеӫĈĐ΅ӱЯŭÙѸɆWъƵƇɒʰÚԓȟɐƯҩѱ˲Ⱦԧ',
                            'ӾгҴɘȸөŋÅʾҚԑˣ$×ςģӉƛӀǱΨȊѕԧԘ',
                            'пΕǷӿҕȉϡԚƙƅϱѼ%îDͽWʌsɃqкҊňƦȜӮϢϾs',
                            'δʻǂͲŇϗd·ʦӓ|\x96Ǔк˖ȷʠͷӀо˳ĖФ¼˶ƖӣȧͼԐ',
                        ],
                },
                {
                    'action': 'ĀӱìĘàǥĲˍȷ\x90ʁĥʞ{´ĻͺЊ\x92º×ԅbȗʑà¿ԖƖʏ',
                    'resources': [
                            'ʗɗȚĶϚϹŮʣ϶г˵ԜǴ8ŏͺˌԀѷӝ˾ΖhϩŪҴӵ\x91ӎʧ',
                            'Ҁίæ˶ƮӿǹϥыԜЄʢēҜ=ŚŁɪԖϴ{Ж҉њ\x9dҽɞϭыҟ',
                            'ϑKPřΐПĮӿǼӵҧșǮÍƄӑԇŶñЛ˳țͼȁҷƭŏɧјȇ',
                            'ǖɭˆʮě¾ҾȼëȣšʹΈҸӎö4Ԯ\x93Ђ\xa0ǔȊαџϑ\u0381!ϲɑ',
                            'uһ\x8asĭϮǓƶϑāϹ´ҳЁЁȪƋӟϨҦʁһȓĪȓϕɆƣӭϘ',
                            'ĖĂƢ>ǁ˔ΚˀǃШ˚ҔάĹď³ғĖуӔʊˉΗϛΓʾМʵ1ʵ',
                            '\x9fˌòǑȶήЭϛʼĊϭɟЩƆҺ#lƿŒ§ɵϰԛѲxǺʵԌAʤ',
                            'ӢӝҾһgùˣӇƝҟƠůҒťяӏȘȃýpҕīŗ}ŏīɿ®äț',
                            'ĠǂҦțʻшӡ\u0380ʠІɨbJ҃Ԁ5ϣÚɥԒϞǽǮɒƚ\u038dE˸ӷӤ',
                            'Ҿζ\x97ŭȈ¨ϢҒҫʹԪǭ;ʱˁɋ\x8aѴʌȭŅбȧȠ\x97ĀĎгǚǖ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'юĶá',

            'launcher': 'Ԅ',

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
            'identifier': 'ɹϡĕ˛\x86ɏ¼ϧȪ;ǳ·Ǐ',
            'target_id': 'ɐ_țħŶʡŰ©ǔ\x9aРȁӒНβԦϋʠ¾˙Я©ӿζŲȽňΣϒ-',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ʲƴφ',

            'target_id': 'ɶӆ˚Эһ',

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
            '$': 'ïʪ¿Ŏáɪ˾ŵчЭ+˫҅\x85ԆέÍĘĒӗџŖċåŷ\x9eĭȬǨХ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 445786734417388006,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -44474.763053386,
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
            'identifier': 'ԥDÒʪѱ[ьͳϠɬāǮ\x9aʅļĔ}ѕƄщѣǗϪʢ=ZѪ\x91ΞǞ',
            'source': 'τǙKżș˻ҊȣԢċÚΫǫϑʇʫәԃӡVҌµ:ȡ',
            'message': 'ҔʏÌ¿ѥÒĴȹΤͿĎÃƄğӁçΏ\x8cǯҐʇǿ˟Ȣ2ɮԠūєȐ',
            'arguments': [
                {
                    '^': 'float',
                    '$': 978163.8542845375,
                },
                {
                    '^': 'string',
                    '$': 'ƪǇЯȂӉ˞ĒϟϙΫɟ×ˬYɞŐɾԡѨƖɰɑΘҟĕ˱Ҽƃņ\x8a',
                },
                {
                    '^': 'int',
                    '$': 4201842379583997109,
                },
                {
                    '^': 'int',
                    '$': 3901848416507086883,
                },
                {
                    '^': 'int',
                    '$': 5579645460345132870,
                },
                {
                    '^': 'string',
                    '$': 'ғ\x86ʱʊo˃ǝĻȣƊԮɏΒɦúΥȲΗӅΞϩȺƤNАρѳ\u0381Ȥb',
                },
                {
                    '^': 'int',
                    '$': 4348854031122103974,
                },
                {
                    '^': 'string',
                    '$': 'ԁҧǢǔƣHʁȭɉ˟ɑЄȘʍʰǕÉΚ˹ӾɉĳŕǃӻŋӝʟϷʯ',
                },
                {
                    '^': 'string',
                    '$': 'ӆȗӥʹɃГɹͺ˽ҧJδσӶİΑӣӪ¥ԞƶƳΕҸ¥ČɠȥȄϳ',
                },
                {
                    '^': 'float',
                    '$': 585093.480297375,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Чæ',

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
            'identifier': 'ǭƪϑ(\x9aϡȎċǤȗӫƺ˖˞ӵʏ\x99ǳ˴ǉӾʼˈȦ˭ѳ;ӌȔǠ',
            'error': {
                'identifier': '½ˠWŁóӦ˄ŋƫjȉ˳ɱ\xa0ҶqŀϱϡсƕӹöϑƜѼƛҭ˘ɜ',
                'source': 'ǾƸŕƇİKÆŗΔɹ\x82źҭȜ®ȝԗΡ˔αĹ@Ш҂ʺȃǒ\x88ϳ\x94',
                'message': 'ӵԋɨļȬԆҀБʢѷü˼КyҙʯҸɲʄяɒìЖ\x83ʷ·IҲźƼ',
                'arguments': [
                    {
                            '^': 'float',
                            '$': 563341.2877567098,
                        },
                    {
                            '^': 'float',
                            '$': 163821.30734114104,
                        },
                    {
                            '^': 'int',
                            '$': 3924951504437439830,
                        },
                    {
                            '^': 'float',
                            '$': 214202.05775424867,
                        },
                    {
                            '^': 'float',
                            '$': 106525.35706126175,
                        },
                    {
                            '^': 'float',
                            '$': 825235.9743921414,
                        },
                    {
                            '^': 'float',
                            '$': 124685.65320689222,
                        },
                    {
                            '^': 'float',
                            '$': 258889.63344214665,
                        },
                    {
                            '^': 'int',
                            '$': 1789917430250342078,
                        },
                    {
                            '^': 'string',
                            '$': 'ƀ҉tҸ\x99ȧèhǓʦ%ϰε Ȁȴ}ҐήƀСʪɘͶćѠíʸĔȊ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ӅƸɵ',

            'error': {
                'identifier': '(ԧ',
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
            'name': 'ƣҮěΚԋӱİĜŴͺŁǕǳ¥ʰԜ0ϕňʮÓĥŬʺ˪Ȫƽ\x93ʞϕ',
            'version': [
                -8165693788401356427,
                -8910320712888456646,
                -1531367729903601586,
            ],
            'location': 'ƁҥĊѣaƎƶʧȂϏȤÄĈԮԆɑƠĊčǶƺϘĉѨƏāӠΑĂƟ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                6848280945922244360,
                5703312501626997516,
                4296732203478668234,
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
            'name': 'Ę\x95Ɣʼƌ\x92Țуȫɿǲ£¢ăϓ˵ѱζӑñʖ\x89ӈ´;ǒΤʽԮл',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

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
            'name': 'ʫÇФ˔\u0383ĘͽѰǎåĿɩĄϾѳŀʉνͼȅʭӟćƤУĿħ¾řˑ',
            'error': {
                'identifier': '\\ʚȢĨçΌʹʎ҆ÁˑЂ\x9cȮΖƭʺϜРϯǹϿʞňǽӤɀ\u03a2Éҕ',
                'source': 'ήҶĲŨ\x8cƂ\x98ώĠЪʑӭοǸ.ӈ±ɯǟˮüɾeηĴΐĿӑǾĠ',
                'message': 'ʥ%ʪÉ@rɜĺҶԣ3\x92ӨѢƨĹzϸǧҀǦË>«ōƒԙʹȤː',
                'arguments': [
                    {
                            '^': 'float',
                            '$': 602525.3449458122,
                        },
                    {
                            '^': 'float',
                            '$': 418019.67654763703,
                        },
                    {
                            '^': 'string',
                            '$': 'ӌǽ·ŗίŒƽ\x92ĽɑѽĂ÷ԥΨʡӤзȃʋљϟǾϧʲɫi2Ǔƣ',
                        },
                    {
                            '^': 'string',
                            '$': 'W§&ӝӲОұ\u0382ЯGò҆łĻFëʃǐśŖϻĖ',
                        },
                    {
                            '^': 'float',
                            '$': -82123.83100103893,
                        },
                    {
                            '^': 'string',
                            '$': 'ŌѺ~dRʭϨĖÃƖʯ\x96ƚД¥˾ɍǂ9ƣõӷňŜҒbVѱǀү',
                        },
                    {
                            '^': 'int',
                            '$': -4474366535173615217,
                        },
                    {
                            '^': 'string',
                            '$': 'ї\x7fœЉŰΰËĎɔЗϦ?đҜɉРϩȑӽʐˊ@ć˥Ǯԃŀ)fɠ',
                        },
                    {
                            '^': 'string',
                            '$': 'ˎЪɠŽʅΔȸEӉѦԛʆΞ)Ō&ĢӶиѳķōƘщŋȡųʜͿί',
                        },
                    {
                            '^': 'float',
                            '$': 29852.819613699976,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'error': {
                'identifier': 'ЛҘ',
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
            'event_id': 'іlǦϊћwȒäǗζθ\u038d¨ҵӹǎΈĀ¸wʻǍΊˉΖӪñəɇL',
            'target_id': 'сԡʆҹӢ«(φʓ\x91ǅĚӔɸAǗɫҶĞ¹Ь\x98AԎ˗λ҂Ǥø>',
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
            'extension_name': 'ũpǇJÚ˵˝ΊҧəӻBɮȟɒʤɕȏр˹\x8aŧҍiМ<ǱϡҫƖ',
            'events': [
                {
                    'event_id': 'Œ¸ǦІ×\x82ɼϜ\x87ĮѪЧ\u0380ňîȯȜƄҞĖ˪ԍƓʹ҂ŌŮύvύ',
                    'target_id': '\x90Љ\xad½ØίơyɈǗ4ƺ˒πҍνȑʩÞˮ҈Ř\x9d\x99ýƈ˺ȬǬǭ',
                },
                {
                    'event_id': 'ǯϛԀǨŏʱDϥӏхӏȝǈǏ¢Ą!ΦȚƛÄ\x89ñʊϪɅцʂ;B',
                    'target_id': 'Ԗ=ȪȮ˵ơ¯Ó˝ĖԮΑ¤ǞΗ·ΙĴўųëˑаӸοȔªżńϏ',
                },
                {
                    'event_id': 'ѿřÐέҢ¹\x86ӡѢ',
                    'target_id': '3wӄ΅Ш˕ÔɆî}ë\x92ƇǸˢӲƜȒɾθШԗԚĭQ\x80ƚºƦĤ',
                },
                {
                    'event_id': 'ȎbӼӭɧĸӛkĊɜϗӫŎԮƥԕģѥèΪƦӮόѪ΄ЄȫЖF˦',
                    'target_id': 'ŏôѢEɩзŞĜǺӿѾʂѡ\x92ΠĨЙӽȳ˓ӸӆҞӭǊːω³Ô\x9c',
                },
                {
                    'event_id': 'ɗѬԉŦ5ȸǪʐӦύϊȦңɾÜȨԡҮҰϕ»Ȓӄ]ōƓřʷŷи',
                    'target_id': 'ӶϨϝ˅ŁԒĝ¦ԄĴ϶ľɺôŚƔʸЗəǶąŋ˷ȱńƊχǁˑ?',
                },
                {
                    'event_id': 'ĔΨԧͰώÔŢS$ǢîҸҠӇҾDӸˮvʭxſ˖ă˜ӓ¿Єǈƴ',
                    'target_id': 'ǆЦƀ×Tѫɪ3Â©ԠȓлȫÇȊѴǻ+þĄƹƃǫȐѵǛź˨ƞ',
                },
                {
                    'event_id': 'âξΑϬǡ6ĘȊƩʹůÝЭͺƧʿɳĴǡƑԅʎ=ѱӵһöĮοƄ',
                    'target_id': 'Ǵȅˬ=_w\xadgʁÂξЈDİõΫȳŧ˯δ§ŗӁgҁѯƧ\x9d˘҄',
                },
                {
                    'event_id': '˷ˌБ\u0378˅ӱϏї½ƺǍǤήЙǦԜSѾmϕϼƻ˸ϸңųѹϕŸÊ',
                    'target_id': 'ś9ƚǚԂ˶ǀÓ(ɳ˱ҕʦ±˥äˆ\x7f3\x82ѡʴжӎǆȾĩSїǱ',
                },
                {
                    'event_id': 'ȜȳӪțɯƏĘʪʫǓńʾΊхУƭŠѩƂƦIŖОƪӳÏˌT;ǧ',
                    'target_id': 'ȲĤќҒΊ#ʊȒȦî\x9fîĠӳїϴ/3ξųf:\u038dɭEέӉƀȿɴ',
                },
                {
                    'event_id': 'ϷəȧµЊԕԏƏ\x93ΥʥúϒƟȥǒΩʊҦκϙĆҕϖσɃƗӰӽʒ',
                    'target_id': 'fӾñʇËÌȂʛӬƣ¤áíσʶȊ\x89\x87ѧά˒ҊľƔѨϹǠɞƄҺ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': '',

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
            'extension_name': 'ńϊéƪňăҸƁƑő\xadҟǌˋϰʃĲʑņϣȷJУΟ\u0383ԡχĭő\x8a',
            'events': [
                {
                    'event_id': '\x87śəŏХŖϘÝ¢ɏњԡƚͽ;ЩĚ˙ηāҺ\x94ӡԇȬȧԕБδь',
                    'target_id': "Ǎʏǅ˂I'&ƸƢӳқMĴЋԄǳșж)ћԇ˛ҘȜɼˈǢGÑƤ",
                },
                {
                    'event_id': 'ŚԪɂӔЭ˾ʋӈňӽɾϖėԒϳӗɠČĽûħЀʒɓȻҥȁөˍӑ',
                    'target_id': "CǢϵͳ'ƕʹеҏ|їˬӳąϽǀϸʑʧҗϾ҄ӷΗ\x91ЕľȧȻԣ",
                },
                {
                    'event_id': 'ӓΔШľҟưѦӘАȧʮεĪȋ\x87ŕӷӼ\x92Ȱ[ҵ\x95ҡљӘȾҁиµ',
                    'target_id': 'Z³˜ΖЯаȳϵ\x86ΏǽϽВȆӦľԍę\x8c¤Ϟ\x98ϰÀëшŘԞƶĊ',
                },
                {
                    'event_id': 'ɳƃʛˀ\x85ʔˊҾАÿƘџ\u0378Yɡǂ˔˓ѭɦԕϒÒϾǙƜ˺ϔ»ѝ',
                    'target_id': 'ΡӭŘƒ§áȵѨӯȶϬǦșȎңˏ/źϺ\x86ĭˏȘɓЭҼϨĥĖ˘',
                },
                {
                    'event_id': 'ӷFӂζΕɈ|bŹƽÜȖҝŘӬȽÇέ<ХѮϵŪŘӔӳѴķ҂Ɩ',
                    'target_id': 'ʱӎԪӔϫъԌŹԇ\x9bĩ͵ҦƅѫӳǥĳΨʌŶTѥƔѵӦçԣƢȮ',
                },
                {
                    'event_id': 'иūϖʨ;@ƍӢ%Eʆ˾ʔТǸХɐƸЌϸÑɷө½ͿԥӎҖӸҟ',
                    'target_id': '',
                },
                {
                    'event_id': 'эҟŜΡԨŉɏ˜иćҔʉȃ˚ČŷɇˁВΕѳĬΈ!ÍçϡҢĝѿ',
                    'target_id': 'ѴΪȿʑʴҐʼ¢хʱðȝӴȶťɌǧΕËƈM\u0378ёǀҤѮѤɷ\x98ê',
                },
                {
                    'event_id': 'ÑԞoǸ§ҹϚә²ҳΙĘʠƇ˶ȥƫЉԄƘđͻʀįԨŹÿəƿǨ',
                    'target_id': 'ϲɫθԀώįȨͽӟнҕlӦӮǏ˜Wґ$γÈĮι±ƴώ\x89ˎƳͶ',
                },
                {
                    'event_id': 'ŚǼ\u038dƥԍҟɳȴƍӺњģǫšʹĤǲʊƷϜɱ\xadǆͻϞϔӞɊțŗ',
                    'target_id': 'ĐźʏβõІÊɃϭ\x97ʴ\x8d˟ϜŦӻϖȏϸʯΏΦё ǽӷȳͰ7n',
                },
                {
                    'event_id': 'ãӒϩЄλԧčˋəșҗʙɈ\xadϓãɍҏʠbϺѬ\x8dԋϑÀ˓ғyɃ',
                    'target_id': '˕ƮΙρ\x9aw˜ɞÒȂȝӥîǜȶĐҡɆʡҥ\x80ōѢϗBѫƝкȜr',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': '',

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
