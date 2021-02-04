# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-03T21:03:04.362879

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
                'ǁǻˀĿǨӛßѷҁǿΟ/ƚԡјγšʮǊŤūщϐǷΪѻ¸ӁĉВ',
                'é¨ˡǀſƹÜɃƳkӐȒԂǛŐШҔõÖЯɈ^ѿːӱɃ>иÃȷ',
                'ѓщøňχӶëǁɞӘӷˡxқ\x8f˫Kɂҡ˂ψ]ʸǵ\x82ÐѽҳуЬ',
                'ѩ7éɱѪ˃ǹ˭ҜʁʯŎé{ŕŋΣВɕƛƯԏƄĒͲѩĤҦƈ˞',
                'ɶӿ¾ţĪΖȚŻԖżԋʶҡ}ѯӴĀřӈøДĚԌŞĜëȇį˵Ϛ',
                'ҘɺҦƑдŒ˭¸ɦźҎҋȷӖʬѵѰБЧԟҨǍκƈȃʷͳπԏӇ',
                '7ə®ϣɇƓҌϦ\x96˧Ɗɽ&eӥƯMɺӵԕņ.˖ȘCɵȠƹͷ\x8b',
                'IԌMȑ\x87Ө҈˺ԐƋŨ\x7fĭ˜ƤѳɦЈ҂¯CШǌԗӌňзÄнʤ',
                'ǉǍӥĽªśА˺φ˟ʢɛë6ӟѦQфfɊǩɭІΰ{ŇиӗԝԈ',
                'В\x95ϼПʒӢƆрҾǞυӆлˤƭŢҰѷΨÛˑĭǧ\x96Ĵ˸˄',
            ],
            'source_id_prefixes': [
                'ӋċóИЎƅӏ8ΓćЮÄķ"ѯҟǊҩЀǙЗȯǷȉҟЪЙϺЃҞ',
                "ɜčǪȦϬȯŮϾüǤ҈Ԭĥ\x89ǃ\\ӴQĻϥӡ\u0382ȄȵMc'ãуҝ",
                'ũɈӏȬʑ\x9fЅŸ˭ȎĲŅĳͽ\x9a\\ыƽӣřӼшɻřӃǜɋͼɬœ',
                'ŎʞқϤѸPԔnԦ˔ΣͽǫπůɺŖϒˏ^LNөÑдΩԁԜЕӇ',
                'ȐŷзÌŽ\x8dÜδǞȠф4˲ΩΌ\x8cɨĦϱĊ˚˲;;ȦШʿѕԜy',
                'ͳҥѿЅʉƀÀ˴ΊȤ%ӆĢĠΞԂʴɪӄήӥ_ĦԒñĞҍÚ\x86Ļ',
                'ФυϿǃѫŮ=ртˬʻҊȗ\x94ӫɕӔâ]ƞӽ×Ɨɶȡ\xadҽҰԗv',
                'ƥjɃԘ^ǸNčξС*ҥĻġëūɲȢ҉ӴȤ˪Φ҃Ų˾ӦѯÑˬ',
                'ԃи\u0378 ˱ĜӝyƩ¿ȄĊ¡ΒĉŚҥƞ²ԛѣ+Ũ\u038bːőŵНûɡ',
                'ЦDɮŷџҕӁҎԬʵƊϬñæ\u038dÇǁϕŏǸŚnˇÊÚӬǯԟʅɨ',
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
            'action': 'ɄӐɲЛ1ʡ\x8dЎʷλĕԃ͵ƩíɱԍӿϬĀπ˰ԘӁƕпɧǕΔU',
            'resources': [
                "ӋÁ¾Ƿлҽ=ǰŰΰʚʁĹъǳ£˫ŽρʚèǡĶƧYʇϫ˲Ҋ'",
                'ɰdĈjҲĭΖʌÅkȚȶêȱί˙ȜĽʆĽ^ƛϣкǪɕɧǟЄɼ',
                'βȬǙγәƝ¨ЀɚϱԤΎēɨĪʀϓ?ұʕPǉͷʹïƁ',
                '?Ŀɖǃ\x9d\x91ҚĤĥǙЗпbmϙÏˊʴǎ\x99үǑʜ»ʅҚžëΑ˼',
                'ŦԖÆŵχơǕȠΗiѣŰȪǓѳ҂ȋÅ´РcĄǮʲľKϥӻĸӮ',
                '`ŻµҷRīЖҔʻƾψԫĪǑʹӊˇ·%іҿɷΣͻҶЇTƣψΡ',
                'ҙ\x98щӛˁ;ŘĀ˰ȸĄ¤ȭЊė˔ďέϠ҂ˁŵŖ\x961ǅҸҝˠ҉',
                "¶g'ӄ˴ʰʚǲϣɨőԛʪԍIѬжžɊŶТюӻѢĬσŬэɔѹ",
                'ѺƸȮӟǩΊ˧;ȗԘţƎʗңҟӠпʓǪkØCϗџđĠӠķ\x80ђ',
                'ҙϸȣŹҖŔϓϿƺҲ\x92϶ƘґӃƱȈɁλЖєͿĖpЯŬĲ¼ïя',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ȑ',

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
            'name': 'ō¿ŅЃ˚ТӾÜ҈ҰԠǴΑʄӱʐʔ4Ǝȵ#ĨѨΉϵ˽\x93ȕΆƹ',
            'version': [
                -4848449053866413094,
                -7641185615590023433,
                -3187389065392632982,
            ],
            'location': [
                'Eϋ¡ϋ҅żӐŦζ˜IĆԌȀɜĞȘϤʹł»ÛЁ˗Ҁɗ\u038däșʝ',
                'ΛРƆ˛î¯΄Σу\x9fʽɈћЧūƸΥҍӚűɩʟ˴ӥˣšшúѱӝ',
                'ϨӿԓуӵѯѦɿʃˠƱΈ8ƵțϝїώďǶıKЅͰĪϼɓɡӮɏ',
                'ӏ˴Ζӝ\u038b°ɽҽ˘$ӨԞɏҖŎȿдΪˬҵϮԌϧϯЎӡơЌҞρ',
                'MϘ˼ZПӡѰ]ĦΈ\u038bȄεͰąȓȤģɏŗĹȀȇͼĉҁӞҢІӯ',
                'ьΥp˜üЉӡȶӃˉӽҽȭƦƬȰʓÖǦјɭĕʌȖɏĝɸǣНϨ',
                'ΞқɣӁ˅ϏłΉòfđ˚Ʌ\x8e\x99\u038bΩːˍҦăҴԀ¤ςʾ\u0382ҪŨɩ',
                'ӊϟϷǩĞ˺gӌƛϦжįËϗʽŲEŨҧŢԣäЧƏƏқOǴ˵у',
                'ίГΆΓ02ǩ3ƞуɼϏȓҀơϊŖ˒ф҇ɣťĉ¡˸ÅҰөĘŻ',
                'ОίȥҐƶaΞɆΤѮǟ\x9f_ˡѭƫƯ\x9fǏɓМΆϿȁȳ˹ӺӤõ\xa0',
            ],
            'runtime': 'ϝcɘԛϬǩùÜђөϳϕеԩˑ\x88πÆԒӋԮҚŭԨΦȟΗǀӪİ',
            'send_access': {
                'event_ids': [
                    'ĵi:ӺÝƿӴϲҧϗѼƑƗϜʽӦÜ·4ǦгŒȺˠʖԩǷγ¥ά',
                    'ě\x83\x83ŋƊǨ҃ƂɨþЀÃϧdɿБΔΠ®ѳĝʸ˻ȧдΤÏҦиѸ',
                    'ŃÙ\x8aFƹЭǄʊǥʈƏіUͷ&ӯ',
                    'ѯāєƪÚӴɛĹѧɴ\x9aӭǝχұЩΪӭsˆФϘӴԌӐӌĈɞÏɖ',
                    'ԜǧƌʁӮҞқԂ˲ѵȅ϶ʹΑ˃ҫ\x99ѹ¾Ə)ÍϞlŖ\u0378Ѐӡ˟w',
                    'ō\x8cȸ˪ţňԃЦʙMhȯǊМБӺήÁԊüϭȪɩĈË5υ5Ʋʭ',
                    'ɂˇțũýΚѺͱÂćƳȎŽĝ,ÇԛǍŦŌȓ\x9aӇӝ ιǎXɎҔ',
                    "HɷυЖ΄ʈ'#vŶҊϚǪРԓΞӺԮǾĝƈ˭ƪɎѰѶӒʩѕ҃",
                    'ʝˁβͶŁёҦƔϕƘʰϒŻ˸Ӆˉʊ·ЩĨʦ˝Ϗҟ\x9bƹɥҺʇʄ',
                    'ԢÏԛҴѰϢέϕǡӆӝҌ˷ºΈѭÕŵòϕѫёŬɥǴӜǐҩėҿ',
                ],
                'source_id_prefixes': [
                    'íùȴīЩƜź"ÕŎȍϘɴ҆їҦϑĀɇϕʅΙўӔÑȻƼԃmƽ',
                    'мџЦВЖǭHΉқӓĀŭ»ĪϞϷÍһ±ìӒɃѧǲ@\x9eҢӖēə',
                    'ϘɧέҶKĘƜ΄ðŠƖʾϓƾ4ӌƺӻϓÉɆȠˮTӟĐŀоϪϪ',
                    'ǺѓěƑîмŉϸʁ÷ɞΒɂ:Hˇϊǒ\x9dЖƦЪũ×ςąƜϣԘJ',
                    'ҠŝԤưțǊгȕЂģʙʠ\u0378±®~ϲ¿\u038bӴ§ұ×ж\u038b˱Ƿ˲ϡǧ',
                    'þʟШǎѸϜҙTKǴĊçšӰ˰żΰԅήøЖǽŬϬѮŹσ9lɈ',
                    'ԝӛ|ŕѻƆϕʡÌˀʞơǯ˼ҙӌƱǢȣ¶,ɓаȱҗRӢʸϼȤ',
                    'åЌ¬ҥͿͷˢ҆ѥ|І÷Ř˧λȗȋĲĻĨ˟\u0378ұΉƳɞǦ϶ϫӛ',
                    '΅ƒCˮң¬кäЁȔһвΪğƥЪĬԉЖʛ˓ƁƠќúƤN[ωɄ',
                    '\x99ͼѐԈČ)ήǏ*тƌɆWκѢӊФƑɥԛ\u0383˃ϯ˸ʱʔƱКǙƯ',
                ],
            },
            'configuration': 'ҜZӯωõ)Ƚҫ͵\x82҅§\x9bЦАāȧǬÆЋѨǀХѹŴԄųѹ˽ͷ',
            'permissions': [
                {
                    'action': 'ϛϳɔǵяҏŮƩЅėçÈπΰȔǌЄĳrʺŽȋȼΥĬόûʅpû',
                    'resources': [
                            'ȊȁĤԈʘūȍxщNȐƂƬ˙ÐЅφѝФϵщŚӫĕԔɫɟWɒґ',
                            '҃˸ӗЫå҆ϲϡʸǖƾjʖѥ\x87ӊǏάԊΊƽΝыԋƇƿВǅȯԅ',
                            'ԙͶϥƟʘӭѾɗʇǼǆ)ӒѢͰȿ¹\x9dƥɇԨ\x92¢Ĥҿ\u0381ġȻÂǹ',
                            'ǯȡ\x88ˈԂԛƂ°\u0379ġБ8їюʚϤŐ\x84ŬМʮѢПщǀϸȞǌғİ',
                            'ΩӯƥêΔÙġ×ę®ȘǱΔ¢ʱ·ȇȁ˼ǱȯģÊh`Ěөͼ\x92ċ',
                            'Ћ¶ҞʳѸǾϮÇŃþѓ"ʟɹƧғҳӎɈƳŷɥε\x7fψɫԑòǰ˝',
                            "Δϓӏӡėцʖі\xa0џҳɊĮϘÁűѤÏƏСлӅ'ēхЃņѪѣҳ",
                            'ƺӚӬʚɽǶЇ:ƻǄӖȭďԔõʞĺˑ˕ԮӇȝsϟϓ\u0379ǴƨŔɳ',
                            'ÆΧƌNѫȵǣεϺ\x9eиǞƨь.ǒ:łȱѦΣĔʵïԙͲOЫԏǟ',
                            'ЪƄ϶ԜήŞβˏɟцą¥ώԇϹɏ˻ƬƄ&ɲˏȯīÞԏЫВЁŚ',
                        ],
                },
                {
                    'action': 'Βȣɵɥ2ԙɫ«ІĎĻИȌǫȬψĪøɟӉ\x95ͻŏÁ¼Ό',
                    'resources': [
                            '\x93˞¿łƏǖͿ\x9bӠȣĆΜZҐ*ЎG\u038bтԉ¬Ãӡ§ǜƺÓϘĖ\xa0',
                            'ЬʚgӈɧӤҩԞ˄ͻȩÑ˲ϡāȽ:§ƥǫƖǎҩӠȽˍȢ\x88ıư',
                            'ϔȣͲǽǓʲԋ҇ŉԂàęԎŤŬЄϙYͰԌ\x7fˮЎԛѵ\\b$ʄѠ',
                            'ғΗќϩƪƙŜĮёȑǊӆʾɅύ˦ʩ|˚ʚҵʀԂȑ]OїЉūǯ',
                            'Ì²ʤŠʑʾг\x8c϶ʋ£ćȻč\x9fĦѵŨΔŵʹжĖС˴ӫҜêȭԃ',
                            "ˈǝ\x9a˫ψӗ¬Τǡώ'´ˤ\x99nѲĆҨú΄ƦşхŚƪʸЖҧD˔",
                            'ś5=ӳđюǐѣÆŎƙĜƈ_ǳԪʊĚԓԚӮʎŐ҃ДрƜƍȾн',
                            '˻ʭϙҖϙʏɧɺӜùěҠΙƛėΙԩ˼ӭǫǨ',
                            'ûʗѽɼí9¦ҌһԐԛӏҡ¿ѣˑΆŢɕĊӻϋjȶ˵dʜЅÒс',
                            'вʍ2ƸҎ4ӡʄϢЪȦõĥÝʛΤ÷Ƥʈή˅ʽǿʙȜŒϭ҆"ɽ',
                        ],
                },
                {
                    'action': 'ЋԇƇƱɯħɻǺʎіżǽȎ˂ǉ˵Ɛ\x99ĮщǷѴʤʈΘҠ@ϼƂϜ',
                    'resources': [
                            'Юŧ˃êÓмУÈŗŢ бВϔͳâţτȾӶӯϋҸźȽĥŌƧ\u038dώ',
                            '×˕ԬЀ˜!ͺˋʊԊĊџǡŭ˦ϳ΄ШɈӌ\x99ä˂ӅӨѝѤaµҽ',
                            'ЬƙŝӖҎ˓ƪɲϧҔѻƟĎīʠʳɏʚӱ˘Õʪh˚ʏűʻЦ/Ƀ',
                            'ԋ\x85ɂÔΣҥ\x89eѧϮ\x9cӚˣĐԈŐɖ/ҁŊȀόćΝʒΞĐԊHΫ',
                            '\x9fҰęǚԥŸɶɽΤϬĐʺϼʊЭƞȴѩЕʈś˂ͰӲаóƓ˯²ɲ',
                            'ʬ¡\x89ѩǾüÝ¥hQϭīʽ§δ˥\x85нÑҢǳɶҖ\u0382?ҹЩɶОͳ',
                            'ΑϼYʏϟԭ\x96Ɔ˜ȉϸўΡҴϮ΄С½ƼSęÞѽǼҘĕҺԅəЈ',
                            'Ӎɠ˙\x8f Ѐп\x83)ɅԣȃҰ\x9fǥɺ˥ōʩіrȥϵӎѫÜԂƀTʍ',
                            'ƑhúȐәψŜiϑӲ\x95ѝБĎȶӄȦJƟȑѺ·ѲĤˣz˃ƧƹU',
                            'ҦӲHʹǭĐŁȗáɺ҈ǅʝӱ\x91˳ŹƃǪјҹґПҏђūҊĚˢѩ',
                        ],
                },
                {
                    'action': 'ӮΗʅϛ\x8dҐLċμĄʷĎгɻAÍ\x91ƝѪ˹ȉЂÔˌĿȶeöЪØ',
                    'resources': [
                            'ĮȻǞȃ-ӢȒӭĞĂǩ˟ǑƱϴØ[QŀǇȂϋƸȜϙΦĉѤҥɷ',
                            'έѲã˴ϵͲЭưϳǭ}҉ʪӣƏ×ϼƶӧ˒ϩ˅ǱԡȾȅýʂ¬б',
                            'ˊŋąȒ˘ӣ¸ѼϐԛϋʹІϩΓ\x8bΙɹ\u0381¿ǒ_ȕÊɀùĈƑψȚ',
                            '2\x8bɁªƏĞɇ҂Śəzßɉ½ɀοӻÙԗ&Ӡ˃ԆϨǻ˵^ц˕ʄ',
                            'ĦɤѧÚÅÅϔˌӷɀʲɎ;Єъŋѽ<ŭǠP\\ŴͰϊʕċЌȞͳ',
                            'ǃŷʳȘǼӛϙϒϙΑNʞ˗jǭɰӽʇҁөˤ·ɝϕϚӃи\x7fԤ£',
                            'ҡϼmӥɘϻИ\x9fҍŊɏƳ\x7fАӰɟö˖єȠԥҀʗŏξɋɜˌȼ\x8b',
                            'āғˡɾԓΪьűâǿХ\x9fŤȆīԖәҟԇĢǁВѦϣОҡ\x95ÊŤϟ',
                            'ȼϱʒˈM\x93ŐɓψёƔҏОȝí´ŸѠ˺ʦЇϺǼÀ,ҡзǺɻӧ',
                            'äԒъϱ\x84҇Ԕʋ҉Ҡșƣă4i7δўŏzʴŉ#ʈƆƧÙΤ»ņ',
                        ],
                },
                {
                    'action': 'ĢǙТɇù˗ÉҺαϣχԛˍπìʻOѯЫİѾӞŽʎƸѹΤёȣ\x9f',
                    'resources': [
                            'ӡêƹ¹Ő\x86::ѨO·ŇА˹ԝҼҞuκƀӜљ¡ӟſѭŌ˟Ҳҡ',
                            'Ğѧ˱PʰʔҀɺ,ФЖІā˷ȶϪҫfȺԂʦ˲ҔϐϓIăϛ¿Ȩ',
                            'ĹҭѦʄʶωmŴ˄ϑȕYĖȔĥѹìӹƛӽοѹʖƟOGKӾԐΡ',
                            '˅σĚŸŇ\x91ԐF˵Ă\x87ӿŢЉ7ǿÖˉҥƁ\u0382ǗöӦѺƹģɦĵˡ',
                            "ЙѠ%ϐɫǁƽѷƊƾʉėɷю¬ϵ'ζғύǙʦж˚ԅȾ˔2\x85ҧ",
                            '4ųȃʭ7ӫ\x9eˍĕ\x86ϴˠ˶ȻıǕőԣȻѱц\x91WāˀĘʁϥ\x8cǮ',
                            'ȦƔȾрӆҀɌÁНÊӢ˗ҿ\x90˖ϴĤŎӞЫșʞaŉ]Źʲˁ\x8fĶ',
                            'ɝ',
                            'Ćԟ¹ӊΣϛıŔðŢƕƌ\x91ѫǪӂ˓оȚԇ;ŜϝŶ\x9aǴĿκΉΣ',
                            'ͼЍԤѷϻҗŪҘƨӌ\x8aξ·ƽӿӱșkӤĊдȄÆ¯Ёр^¼͵ξ',
                        ],
                },
                {
                    'action': 'ʹϚ\x96Ť\x9fԒƋŝɁ\\ȸΠώ:Œ:ԈˡѸ \u038dѹӻ0·\x88Ŝɞtγ',
                    'resources': [
                            'ѶЩȉЙόӐŮҦƽŴƂϣìҿȶԡʹƋχɛɭȐ"ϝ.ƉӱιƃƩ',
                            'ҪɫĐǹŹҙΜӏ&@´҉ϡȲͻȊŇɧɱĬČˡÉƫć\x88җǉɎǒ',
                            'νˡ˄ɣЎʆӝİʡéΘ0˅ӺϴϟӬɆˈ¨ɤɬϪǆɨҘāɑ?:',
                            'χƑĬѝ"Ь҂ӎԅCǯȲǼċ\x7fβŐǏoҰưϊзǏoǓʟůȁǳ',
                            'ŒȼƴѦˈʞʹƷƅƼϯϽѰӟҭӛѻĊҳӿȆņԎĐʪѭ˦қRŝ',
                            '˚ÁԇЪȽЙɞяŅņʊƺ^э<ȹ¹ΩѸ¾=ϙϓϺӍϒƙωɾΗ',
                            "˽ƧқӘͻԋ\x82МƎ'ѻӡΥӛϾi˻қŇưgƧÄԪˇ˗ũЛԢё",
                            'ɧ¸\x87ӱҙϫкӮʈÖɗǴˬѦƻ\x8aԗȭ1ϚӍНԅǥʠyШͳѽԄ',
                            'Ʀý@ȟҺɼɷһɮϰҭǑҀӥԋѣƹĒſԖӽЋ҂ǘѴӯӇΕɦˢ',
                            'ÃǓΌŷһύǈҘ˨ԖӷYрǣшЧ\x96Ǫ´ŢșҢƃɫʊƦƝûCԋ',
                        ],
                },
                {
                    'action': '΅\x8aԧ£ÂԎ²ŲʶʌͻΏÈ\x8eÜԨ\x8bƻƶʺ\x9fĺǧɫ\x96΅ƴξÓͶ',
                    'resources': [
                            'ǺȢn¬Ӏa7ɝѠɃͲҙȸǃ\x9aжψµӫԝđůŚЄӜQҁþÖω',
                            '˹Ķїӏσù˘Ǳͽġ˓ǟʐˆΪƹɟԧΈ¾ӑӏŐԀ˵μʀѧ¡˹',
                            'ҫmĦʿҊ¶"Ϫű˓ƤԟÓҢΆŖƥyȋĢѼԂ˥˄ǚĲ΄ЗŨӊ',
                            'Ƌōſ1ȟОǵÊ5ȺϨԃɻɢȋɷ˃ŔΈˎϗþ\x83ѧÍБʹк˂˗',
                            "ʃƔTϻѿǺå\x8bŗ·ŦĳŮҷ'ӌʈPпӧà˪ѵǞąʞċȂѤÑ",
                            'ǽкр¹Іɣ7ŠϿˮɓǌÖɨҽʌơʿѷʭÍ˪Ԓȗ˶ƦҾΡҋѫ',
                            'ˍͺŜŜȶ¡ѽžͿοʝȬ˪ąɿϯσШԠƃъġύʨԡ˚ƮŹ˸ʫ',
                            'Ǵ҃ҏÝΆʦȄȓΙћ\u0379²ɆӪѝȳ :ӄĮ΅\\ÃˤЭòǙ1¬ǎ',
                            'ǭф\u0382ΘѳōîťʠðЪѭƨӆӸЧ¸Ɍ˰^NǝАƣ\x8eӖʻԔпĢ',
                            '˜Ӕ2ʅЍ͵ǅƙƼə˯ȠđÓԡθʵöęɁ˵ҬġʟʦϬ2қʐѴ',
                        ],
                },
                {
                    'action': 'ӁЈǥԚʴҍУɉӂüйÆį¾ф',
                    'resources': [
                            '+\x89oǟsΆҿ÷ӛǽƟǻЃЁɻʦƂΈɡɡҞіτʴƨФӼɹӋʂ',
                            'ȁǋűҨɶʤѷu˹řʇĵïϩħ÷ԓʭϫӢѦҵÉүWơŜұɕѰ',
                            'ьԌįӍʆȧƞʽȔЀòќѯ˨ǜӔ҆ŭƺӈжԟӊɩĺьɘԨvҖ',
                            'aŬǐǖώķǛãΒaÍƽƕԔӊ˻ÎʼγĉʇыºŃĲƨЩѿƗƅ',
                            'ɹǐѬӲƵэsʂ\x83ɠʂɻҁ˂ˢ·Ǵͻ@ϟЦƔÔЙЎҙɲԀϢØ',
                            'ćѯͳBˈǇƱˈŉӿȫŶɐsǕтʨȅϒí`ǎҋѕѣɾǬϟȨή',
                            'ѫcʄӁғ|´ľоҎ×ŢȻŲȘžīêʦmȅĻѯͷ\x9cβӯԗƝ$',
                            'üǅдƦлÆѧǘ\u0380ńЧ\x9bȯˇжѡԍ˒ȡ`Ļ\x8fϦƳжƵħϣ´Ö',
                            'ɰʘ\x86źƊѤΐѡѶÍҤѤ¨ċΨÙʑЗЪҚφǈŃΨćѫԅѪƗ-',
                            'ǵɅôŋĸþәхϛҽ\x80ҸĹ³ԓȆô¥ёĀƘȫƓ\x99rҐ˓˶ʋӑ',
                        ],
                },
                {
                    'action': 'ӻѮǡΉ(ЬȐʒ¿lʌԋ»Ŷŋ§þпʜȚŝӮƢş%҃ԂŃǨɊ',
                    'resources': [
                            'ͱɨJ1єϥĒ[ŸðXԅϡǙǂČǂǛѲɀѰˍϣҨш˄Ԃφ\x92¬',
                            'кɿл?ƞǃϧ˶ˆȖǺɸϧĻÐɓҋ҅ԑ¿\u0383Ϧ\x8bbѢȣϠ(ɉŃ',
                            'ҥккȇϗѝʭŖÝɲNȽǀΥD˓ӼΫѶɸђŭвψƄЊˏѴϽØ',
                            '\x8dʼφùɛƷӏÈϗϓ<Ϸɣrчӫɀ¨ĽяˆƮη΅ˢŢС;Čũ',
                            'ĪŞ˄ʱӍѥǙĔnȆӗӴȭԫΠĽèɀ`ЫЂʣτ\x8bͳ|ʱҋ҇Ņ',
                            'Λƫɕʺ\x91ѻҝ:ɕţĖÝњǈÜʱҖԪɰӚ#ǵƭɁҤКǕӏʆƩ',
                            'ɣк˹˸ƖƜ)ǘͼ|ņ\x91ɨЬȆӷρӎÎʫҖɫÛώð˸ŨǴ҉Ρ',
                            'ƎǸő',
                            'ŠҳƼӹVśϧȾª;ҽwȾә˚ŖмƤſƆωɿÛǗǹяřȏKĥ',
                            'EԥǬҋǞҋȲ˜ӥ҈æυұé˄±ƑǷǏϑźÁΗ˶ȄӌƢÍ3ƽ',
                        ],
                },
                {
                    'action': 'әƸ˹ӿԩʴѺ7ήĭǢRbӭ\x9eɊĽʥÓ\u0383ŏϕМhѴĭȸԆÕn',
                    'resources': [
                            'Зԅ\x9aǴǳԬҞʡǌЋȔɵɦɁ1˸ϰFЇńфǴŅº\x93˩ΝD˰Ӣ',
                            "'ǔȡŶιӺ҅ъ˰´(ˆϏ˵Ś˘ʟ˄ƓбϨ\u03a2ɬʔíѦԤӲɏǇ",
                            'ҁ%DӾÔǓȠ҂҄ǲуɅƕƗҁξѪϸy\x91ͼɤԒŜWνӀЩɄͽ',
                            '\x89Ҩ\x9fAʅ«γҖǱѶ-ɑ5ϨϔҕƠ®Ĭ˫ʲþuԡʻѬǟ\x8cųȁ',
                            '¤çΦƭԃ˒èƼȿԩͶƁˤʍщӭԓ\x90\u0379ȧĜЉɕgѬ\x8dʝǁɐЄ',
                            "өʛ\\ɼʷãԘɴ˭ɧΝȸΑÁøȰеȎ^ȁεѡ'8żԘΒӁÒΰ",
                            'ԐәѵʘŃȇѣȔȦЍ§ȤƱ\x93ûȬǥҾЁêÉҰXκǌĺ҆Ґϛ˼',
                            'ϱƈóǚΟɶĊΫληɋбgԊƝаɕǌǈǼɄϖ6ŝĀϕȇȖʂ˲',
                            'KÌƼӝӉʡγɑΐʀ˨ʓ˝εȂəѧΝҌĭ\x80Φ®ϹвӉƆ˺ӷŏ',
                            'Gǥӱ˄ĺƮeł҆ͶǺĝâʱϫyų·śǑкӗӛťе(ӺЯԎѳ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'D¶ϼ',

            'version': [
                -6333974215023077413,
                -8972698101340990817,
                -8625791165210272571,
            ],

            'location': [
                'ī',
            ],

            'runtime': 'À',

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
            'name': 'ӀŅήΚ˄ҤXƆԤ˻˳ԢŪ´ϤɚЏфǂεжϺǝȺЃĳEҖӄӬ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǚʑӒ',

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
            '$': 'îӯɐʤŗзϤȃƉЀϥѫɂ˞υҪӲţу¹ξԔЂSѴӾǿЩʍɇ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 4020850509703393661,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 808051.0059584682,
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
            '$': '20210203:210304.302883:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ѻ%ͷΔϾѦПɦЎPοʚŝ5\x9aϽH¨шԪɚԠťы¤š˒ʑĨ\u0382',
                'Ā˔ǘӿɘʖԡӈĭҚӱčυӪҾúτǅʧƝȕȆԞУç&©ϖŰɍ',
                'ӏ½\u038d\x83\x90ΩЇϧЪç\u038bɌʣ ē\x9dԇѠɎСϐϫ҂ɕϖuʿ˧ÐѴ',
                'ŰĆİ˛3ҴӴƪ҉ʶӀƝƨǿʳðΓҘрȄҙêӽŎˉʪϘʷ˺ϙ',
                'ϯŋ+ȶҒǂϼŠƀşȆɿǒɞӈӡƾȹ¶ʠĭɾǣŝĘӱƍ˫Ӽɷ',
                'фӂ@ƪрGԏϬеˍŎ҂ӵǴǹǎϷ5˵iǍˉ"ӦϙѺʕҖɻΧ',
                '\x84ĥǖɋƜѿ\x98ƔҩИӬ\u038dȗ˫ˇ\x80ДŤĘіϑGΗƽəƌ§RԬǡ',
                'ǢǷɽŅʚӰuǫJǴѧˏ˞˒҃ΛßưќЈŢȤѷϬŏɎʖӖ\u038dŦ',
                'ȝȳ(WҺԚжñ\x8f\x87#ʉſoʥ˝ЙƷȖЩċώxŚţЪβÞƿЭ',
                'òӿüǡƚʮѪƫ˨Ɍ\x93ŝрƲʕɒżàʅɃʩ5˔\x90ҰϨǔ¸äή',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2198088720698810420,
                1277370605619118293,
                4839674874195115452,
                777478239966570275,
                2673069407037554439,
                -6379591889946978096,
                3065872272598012590,
                2777185729819915550,
                -3470453521657714066,
                -572687358698635826,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                750601.4419564633,
                491753.58057986957,
                524221.218673563,
                180388.75364121387,
                825466.0352707155,
                -28281.95454928196,
                1243.6379781552387,
                914458.867461542,
                361100.39001685503,
                581115.2453233773,
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
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210203:210304.303779:+0000',
                '20210203:210304.303793:+0000',
                '20210203:210304.303799:+0000',
                '20210203:210304.303804:+0000',
                '20210203:210304.303809:+0000',
                '20210203:210304.303814:+0000',
                '20210203:210304.303819:+0000',
                '20210203:210304.303823:+0000',
                '20210203:210304.303828:+0000',
                '20210203:210304.303833:+0000',
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
            'name': 'Ŀ˩?GìŬЊЎRѿʅʅ;ǣӊӸeǩԗҕÒҬɝåEκҟţʷƗ',
            'value': {
                '^': 'string',
                '$': 'Ȼ¯»ɷʓϝȑӝͻƹФŢˍʺǏſȝkϜѻΧЩ%˘ȲʞӿƚŐƱ',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˂',

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
            'catalog': 'ЅΙӹЅˡˆń3ǲΏɰºϠȥΟЌŔÖˡɲ\u0381ѐpĔȗзŪϱŸɣ',
            'message': "˞ʒҧ¸ҪΩΈõҹѐźʋ҇ʍȦ΅ǨĻv'ðʝďƴʐЦƛåѶȱ",
            'arguments': [
                {
                    'name': 'Ϙkŕ҄җɶк˘Ʊˁȱӭ˅ӰʹƂŒѱюӁӆƘϹҦÝгɱŠ¥',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'nϳĕȵӚДöλD΄ԉȂҀфgԃǰʺ´ҷвDϞƊďҪжɪ¬ԃ',
                                        'ȢɛßϚє\x97ǽѸǳhЛӎŀʨԫϾЗɯ\x9cļӭȹС\x8fӹԏŢ΄ĸϞ',
                                        'ȔĮҊВĚˡћ÷ƟɚʫŊÕŊǲζΜWϑ¬ҏҤҏͺΡɲԇԍπɣ',
                                        'ɒњԕɖǄ«ªʾжŁ\x98ɱџ\u0378äӳϮbΝĲǖˤŵɻˁ\x9aԪǧκѝ',
                                        '\u0378ԂƳ΅ȼȶƎƣҷӓĥғϊƕȋΦʫƧˑĵѿűĴ}˩ӕӕȄ%Ѱ',
                                        'Д3ӸξªԏʰƢȱŔ\x8e˔ȉ\xadWʒνӼiÊďȚμҸҲȉΝΩ\x8aѹ',
                                        'ԀƋŔӟ҉ȖŵǕqźԡYɱbɗǽқΰŸňЅ{ÇƒԄώ@ìɤϮ',
                                        'ƫųϸ\u0381ĸŖϾӅŀеɾƾǰɕ.ϼțƍӲӃˈɆĹȰƘӬԔђ\x9aѕ',
                                        'ʀˢϗɦKŜǜĘѤƨƂӄπҚ\u0381ώľǒɬϵԄοЉbӼ¸ɣɨǷј',
                                        'ԇ]ÉǛϦţhԫκN\x8dԄ\x94ѽ\x93÷FΦѐѼҁԜŊƭͽǠǌɰƈȡ',
                                    ],
                        },
                },
                {
                    'name': '@ŚȊ\x9așĭŹʺϰчÅӤΆĺȮǼˍϲƓCĵԈʞk£ҭ',
                    'value': {
                            '^': 'float',
                            '$': 928973.8812849331,
                        },
                },
                {
                    'name': 'û»ΒǐnΓǭȕǥ˄Ό˙©ΝԠрŜΔÎʑ˯ĦɧόϠˣêHҏʻ',
                    'value': {
                            '^': 'int',
                            '$': -7269215837734276844,
                        },
                },
                {
                    'name': '3ӧɟȕ\u0382ũЍəɵƿѬӷжŰ\x80ːɔӔǾɢ;ѷОʗ\x8bșПԘϔē',
                    'value': {
                            '^': 'string',
                            '$': 'ЦņΝơϻķ®˽έ¬ˮÍɴÖӽϐÛŵёΰ¨\x80ӱr{È\\ΕƍƜ',
                        },
                },
                {
                    'name': 'δ¦яϳŸʘӤˬϋӫeԝρǟͿʓ\x9fŗ\u0383ҩ²Ŷҩ˺ӶnɌɱӌǛ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210203:210304.299767:+0000',
                        },
                },
                {
                    'name': 'дЧˑŖЫԩȦǕŔƆ',
                    'value': {
                            '^': 'float',
                            '$': 263890.81947694835,
                        },
                },
                {
                    'name': 'ȄŞӳĹύҺωʓ\x87ɜʷɭȖВɾϘІf˱ϩǓαʶŅЈĐ\x83Ɇŧƽ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'Ͼ˾ԐłȞçрͿǛˍʧљ϶ʴǮȬ(ǉűÑȮӎʾҸĦ\u038dǇõԤϑ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ǪѷɏҟԮZĥ\u0382ˉп\x90ósņӏȾӲɇҨǁͰË\x8bňќόҖʏ6Ԙ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210203:210304.300863:+0000',
                        },
                },
                {
                    'name': '\x95Ͳ¢ĥ\u0382ɻŔɾ\x8dȞԣԓӸ˹ΦΜɭŘǓ˛ѢќϿ\x9c/Ǩ´ŋѰу',
                    'value': {
                            '^': 'datetime',
                            '$': '20210203:210304.301160:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ԠȤ',

            'message': 'q',

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
            'identifier': '˦\u0379лŷӋӚΘ˖ĭĦʢŌƪөǱĤÐXϒ\u038dʼɞ>VѮKvÞ?҇',
            'categories': [
                'access-restriction',
                'network',
                'configuration',
                'file',
                'file',
                'network',
                'configuration',
                'file',
                'file',
                'os',
            ],
            'source': 'GƁɅʲϧŬѳĭԘYżZԏȿӆӬʬɸŚΫ\x9bÀôӼƽȃтƩqˈ',
            'corrective_action': {
                'catalog': 'żϡǟЅŘÕϏˆÚǛĚӯƇѧNŎTИɍΪͼΥΝԈӰJñ҇гЛ',
                'message': 'õ0ʶэϢ=т&ȡľɰҼ˘ѸϡÚΝ˰Ǣ&ȠWßƨєļēʰ0Ɵ',
                'arguments': [
                    {
                            'name': 'ʻhЃφΐȥӚƑ',
                            'value': {
                                        '^': 'float',
                                        '$': 868113.1166656187,
                                    },
                        },
                    {
                            'name': '\x95εŦ\x86ӊ҇ĹƁЯŘǘ\u0378Ӏ¼ʨцρҚͱӌϏʍωȠΏǖЅѭŜý',
                            'value': {
                                        '^': 'string',
                                        '$': '[ȃþЍʂă˫ˍŪɱғҏůđXSŋИЀǴʞEș¤σѾҵҞȇҾ',
                                    },
                        },
                    {
                            'name': 'î\u038dŜ',
                            'value': {
                                        '^': 'int',
                                        '$': 5833160950796937646,
                                    },
                        },
                    {
                            'name': 'ǼrҏįÞԓŷʚςŕѬǘ\u0383ȷȯǳўϚǇʇԡ+ʧӊ',
                            'value': {
                                        '^': 'int',
                                        '$': -3865734303632991307,
                                    },
                        },
                    {
                            'name': 'Пѓȭ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:210304.295841:+0000',
                                    },
                        },
                    {
                            'name': 'ĸґѝʮҽџǰрΊˍҡԍǈӐȠɽÎíǨ;',
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
                                                        False,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ǹ¶ӫԭ҆jʿʦϺƹļ.ΞǚĢĥŗɳɺҰњ΄ģ˥ĂȒҦɴ\x85˘',
                            'value': {
                                        '^': 'float',
                                        '$': 976613.815420348,
                                    },
                        },
                    {
                            'name': 'οԫĝҬȈƒӿӠчєШ·ň҂҆ʒϭȥɼīΐĕЌhѧҟТ҇ȯЀ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        -63274.41040795676,
                                                        699021.9975007859,
                                                        558646.5413219656,
                                                        -23385.010013969513,
                                                        117927.17057700336,
                                                        787637.7085022646,
                                                        881527.1080129287,
                                                        418487.71389484237,
                                                        -90746.12585599827,
                                                        440497.1882691897,
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'χĹѳƆЕёɕӂɧ˶ьʠºƹƴ\x95łԏҢéɏ*ԛSԀÑѷԜɵȰ',
                'message': 'ɱϋʙÑ\u0379ύȻǨɔɧȆʓϼϒʅç£ʙ˚ӏ\x90Ѻ¼ŭ҉Ҩ˫\x9bƸû',
                'arguments': [
                    {
                            'name': '\x9bɨˆȦϠ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        56912.8314240771,
                                                        945067.4240128143,
                                                        245068.98703313828,
                                                        260483.05038895138,
                                                        695442.1835119391,
                                                        -14459.559862800888,
                                                        -41173.55223909909,
                                                        826299.8566320749,
                                                        692213.636377044,
                                                        760914.3774147965,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǬHѩЫɯ<ʢǑлŲĀŒȅȺ\x8fӀϮīԤІΏō˓ŪʕƬ҇Ųрʦ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        True,
                                                        True,
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
                            'name': 'ɫʔŏƬëĴΝäĭѥ=µҥŲάƜаɒƟŃȬǝȲΑƍΗʩϙ 9',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:210304.304659:+0000',
                                                        '20210203:210304.304672:+0000',
                                                        '20210203:210304.304679:+0000',
                                                        '20210203:210304.304684:+0000',
                                                        '20210203:210304.304689:+0000',
                                                        '20210203:210304.304694:+0000',
                                                        '20210203:210304.304699:+0000',
                                                        '20210203:210304.304704:+0000',
                                                        '20210203:210304.304708:+0000',
                                                        '20210203:210304.304713:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '\u0380ȊǟԫόǢϢÅʢ~ɍýͻŭЪ',
                            'value': {
                                        '^': 'float',
                                        '$': 444417.5567657022,
                                    },
                        },
                    {
                            'name': 'ʿҋ\x86',
                            'value': {
                                        '^': 'string',
                                        '$': 'πȔΡԃЬͻёхΑƑnԣӏ×Ӻ˽Ͱ¦â˜ўϔϏŠπíȥgʺЊ',
                                    },
                        },
                    {
                            'name': 'ƟfƯưҞĊПОҿѵʀ¿Ҵԅ˴\u0379§ŴâƸԔҁϣНӆљɥʪ¦ы',
                            'value': {
                                        '^': 'float',
                                        '$': 279208.5490768763,
                                    },
                        },
                    {
                            'name': 'ҪǺȾǇѡɚԫžÃРʝѭǲĢʶɼe˰ϡʢƔ=ϙơɦԚȡ%ϨЊ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ëӟ\u0379ǥƴƅѺ\x85òѪǸϏˮҀ˶Ȃįɟʥ\x7fӨĜXȵϏˌÕѣӈB',
                                    },
                        },
                    {
                            'name': 'ʶeъϯλўѪƐȪƾǌ˼Ш˫ԋҮȠsԢƒ\u0379',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ƂǖůɘȯѬ\x97ʆ\x96ːԡΦţВАÕʷʫԫƮѠϪ+ʳрύůоʾΔ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        736087.6412867765,
                                                        750236.2104007959,
                                                        972156.2479549383,
                                                        387876.7430878021,
                                                        103896.69816433426,
                                                        655619.0557396532,
                                                        819110.0494898782,
                                                        627970.8291565272,
                                                        718295.6790625176,
                                                        337624.32393750804,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӽʅ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        658941.8096850648,
                                                        258996.99844668637,
                                                        302734.64493512106,
                                                        589877.0127696997,
                                                        86325.22288033785,
                                                        982073.4062502286,
                                                        832485.1981573496,
                                                        613460.690368058,
                                                        787517.3787730195,
                                                        876799.7391468743,
                                                    ],
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'mĒνͰʟ',

            'categories': [
                'access-restriction',
            ],

            'error_message': {
                'catalog': 'Ũë',
                'message': 'Ǭ',
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
            'name': 'èϜȩҕǆӠ͵¾įŬƗΏϪˌȔԬѨŖļŖӦѾöˁƂĺŅ\u038dʼȂ',
            'error': {
                'identifier': 'țΊʘϴĥϤͽҌǼҩѤɗʥȹźɎáϮŷTdʠλϊӢ²ʍōDʸ',
                'categories': [
                    'access-restriction',
                    'invalid-user-action',
                    'internal',
                    'os',
                    'network',
                    'access-restriction',
                    'file',
                    'configuration',
                    'network',
                    'internal',
                ],
                'source': 'ЇþˋͰкǏʨȷºµǭȪʣ\x93ÿ.ƙȐQԈĩ\x80˧źdɼԃrĸq',
                'corrective_action': {
                    'catalog': 'ƞυʴҠϽ·ċӬѝ',
                    'message': '˩ŻɓҘFҧƑ˝\x92ќиǳ˭ĢӱɖеɖŎмɱʐǓÎԬȱʞʢ<Ԩ',
                    'arguments': [
                            {
                                        'name': 'чŽÍɭŚ˦+ѝ\x91Ɗ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210304.277438:+0000',
                                                                            '20210203:210304.277475:+0000',
                                                                            '20210203:210304.277483:+0000',
                                                                            '20210203:210304.277488:+0000',
                                                                            '20210203:210304.277493:+0000',
                                                                            '20210203:210304.277498:+0000',
                                                                            '20210203:210304.277503:+0000',
                                                                            '20210203:210304.277508:+0000',
                                                                            '20210203:210304.277513:+0000',
                                                                            '20210203:210304.277518:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '«ї',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210304.283836:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ȥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1862816889009188210,
                                                    },
                                    },
                            {
                                        'name': 'ŪæÞːÐĦ:Ͳ҆їʇҢӉ\u0378ӞǢɻҦĬПДϊİҔʗ˴ǷÿuЎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6068193298016304710,
                                                    },
                                    },
                            {
                                        'name': 'öƭВʿƼІǦɝѠɲćˏϸԣƒʕSμˊҿӸɮȑǌôΊə˱ʷѮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˷ʦӭҴŒĬʱŝſҤΫŇŉɑƕɸϝȇ˱˔ыƢ3ɩҪɛҦӕΤű',
                                                                            'ŇϷè˝ǤήӌȢѾЌůɮѬûÌȷϴωσпʨщ\x95ȽԗĢƪҧŽЇ',
                                                                            '+ƱȲʭ,ұΕԊXќʫɉЉѦˀʤҪϷΫΥC8ď˼ȃƇɊѧ¤»',
                                                                            'ˠĢȶΚҕŲϙˀԑлԡíȵʭ˒HƕĜǳËƘȨϾЈƒǑLӌ,ɶ',
                                                                            '\x9fɥëZ͵ҊΖΡ\x9e>Ŏ˹Ӫл˨ѤϑǍѪ˶őmԒǍəȼª\x8fӣǊ',
                                                                            'ɚΆǋΔЗ\x7fϿϟӊȿɬ҉¬ŚԧʨɣɟϚʪϒĭɉҦ,Ҙ\x8fЗɳĥ',
                                                                            'ͰǞ\u038dԥȝ3ųǇˠʜɵtɝmǋͷ҈Ɔљ\x9eoºϼҏµġĆЌŋѥ',
                                                                            'ГώƲɯņνȢŞШ?ǎţƸ6ΥлũЋú\x89ˊŋǸȀƎӗϦà·Ӷ',
                                                                            'ŖȧĎ|ԡАƩØȽ˅ƄюʰˌΙČÆɅҋ|ƃ˰ʙï|ϵƆԎƘä',
                                                                            'ԄЕϩͰʘHȁˈēԟȤǣʹӤ>гƘˈ½ԌŮҚʥɱԬʰłĦΘ\x93',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÒƸϵԢ˙ïóѝԊʈВ˗\x92ӣˤ$ÊӕҦӶΩκ҄ŭӹû\x9c8Ǟд',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҷӻϝȫ\x84Ǳ˖ͻǲ«ɮΉʈʈҫ\x86\xa0ů¤ĚǾκǢγӪϤԔȜmѮ',
                                                    },
                                    },
                            {
                                        'name': 'МʨԓȨɐҏ҆ƾҽюЖҥ\x89҅Ҕѕǌ§¾άƦ˄\x8eɸĊ¦ɪȐŖη',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9043256902692422617,
                                                                            3609796355458106493,
                                                                            6233100363177494173,
                                                                            724287863896021136,
                                                                            -1168572833891961476,
                                                                            9086975770801378992,
                                                                            -8845341297420911784,
                                                                            -6821993596565774736,
                                                                            -8708552422161450779,
                                                                            -887773999231732607,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x95ҫϡӝƱѱǾȰǜӏȅ[ϓЊџү@ӊӋЮ˘ʤɋϢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210304.286715:+0000',
                                                                            '20210203:210304.286753:+0000',
                                                                            '20210203:210304.286762:+0000',
                                                                            '20210203:210304.286768:+0000',
                                                                            '20210203:210304.286775:+0000',
                                                                            '20210203:210304.286781:+0000',
                                                                            '20210203:210304.286787:+0000',
                                                                            '20210203:210304.286793:+0000',
                                                                            '20210203:210304.286799:+0000',
                                                                            '20210203:210304.286805:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϸš\x8bĘУɺԘ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4835205285072933835,
                                                    },
                                    },
                            {
                                        'name': 'ĲʶɺȄҰҸðvĨŦНЫƱʺӵŮ5ѪӀ½Ѝ\x83',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ùѹNŎȕǂȗӫ+ĶʸdɢѲtԚ<ĊЩïȟҕƑoϺҽB˛˥ĕ',
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ϒЪͰǄƽУʯ\u0380ƒϲӲȋʂɸǜ?Ê',
                    'message': '\x91"ĿƇȇѤʸԔԞίϏҀʘ҈Ԛѥ˔ѭԅ/ãÿ\x88ə˦ɷŬưkX',
                    'arguments': [
                            {
                                        'name': 'ѻǁĲċσїҤʖԐS',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ŦɁşȦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҟ\x87àɽӟщӪΌу¸',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210304.288721:+0000',
                                                    },
                                    },
                            {
                                        'name': 'gЭ˦bѩƸ\u0379ΡӁΚƲ\x7f·Әł˅ѰĶџ˦˳ʾΧҁ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ä',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210304.289505:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʿѻӕ®ĹƏҠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210304.289811:+0000',
                                                                            '20210203:210304.289830:+0000',
                                                                            '20210203:210304.289845:+0000',
                                                                            '20210203:210304.289859:+0000',
                                                                            '20210203:210304.289873:+0000',
                                                                            '20210203:210304.289887:+0000',
                                                                            '20210203:210304.289901:+0000',
                                                                            '20210203:210304.289915:+0000',
                                                                            '20210203:210304.289930:+0000',
                                                                            '20210203:210304.289944:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϩѷǡã¿ÓƎȂ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210304.290471:+0000',
                                                                            '20210203:210304.290492:+0000',
                                                                            '20210203:210304.290507:+0000',
                                                                            '20210203:210304.290522:+0000',
                                                                            '20210203:210304.290536:+0000',
                                                                            '20210203:210304.290550:+0000',
                                                                            '20210203:210304.290564:+0000',
                                                                            '20210203:210304.290579:+0000',
                                                                            '20210203:210304.290593:+0000',
                                                                            '20210203:210304.290607:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȁțRǡ\x9cҤǸİĂǐѹĳ\x8e¬¹ѐďåȜʘñǈГӫĮ͵ѹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɴΩ»',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6688511283266601278,
                                                    },
                                    },
                            {
                                        'name': 'ʅǟЙ҂ҵЇĻԪΧª˯ΛԈ˞Ǘ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɭʨ)ʧuѤɒГǁϐŖöӸД˕ƄЃʏɄ*ʤ˺πʹdӢŴA˒Π',
                                                                            'ĝɞ»ќөϱ\x85ąҗԏÜ[ԫaңɂӝýŚӇȓӵRЮēʻĬ\x99\x8a҈',
                                                                            'ԢÛїԛɭѡЙͻȷʳĐŇlέТǗÙϔưǁĒЈɇǫìԃιǪЄΎ',
                                                                            '˃ѡªČɛiӶʄέÿǏǜěЪȻˬəϮΉƲˤΉòÁˇʒɮbϔή',
                                                                            '\\ϯȏƣҜΓη˓ÜѶ+Žɀ˛ɮУűáǇϐȆˈӠuϔºӾЙ˾3',
                                                                            'ͺĄ\x8cţ˙ȷȍƫʈѿɑ\x9eĠч˘ɜǽȏ˜ЄϙkɇƵˀϒǙˣЙș',
                                                                            'ȓԔдɞüѶҝɕ¥ʎǡӄÈ˷ǐɑΉ\x82¢mɬɯήά\x9eƈԘƩȇh',
                                                                            'ĴϛȇǙϘɧҊƏϜģΞƫԉǳҐƕƜӽ˥;ӝŹΟƳǍĪĊѸňɤ',
                                                                            ')ΡʎӚΒАƲǌȒȦφǣѧЪаѶΙӣѶˑǽ˔7ˋӁ"ҸÉȰϚ',
                                                                            'ԟξ\u0382ȉҩӑúȡʜʯƆ\x81bgȌϻʀˑѴ˳ΣɤͼɭϿʀтҕį҈',
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

            'name': 'oôɻ',

            'error': {
                'identifier': 'Tѱʝ˭´',
                'categories': [
                    'invalid-user-action',
                ],
                'error_message': {
                    'catalog': 'ӡТ',
                    'message': 'ҕ',
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
            'event_id': 'ŋδʀҋ˝\x93ǭv÷ƃʕϬΘŅ˙ɉђ˺ɱԑɖȌˤҿҪǴêϨϛ˻',
            'target_id': 'ɤƓʁğŲΆθͲʐq҆ϟͿƧiО˵ƛgϊƭӬȒĐӏ¢!қѲŌ',
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
                    'event_id': '\x89қТˎҰԥӫЩ4ûԦ\x8aŊΟʯѕρвʬͼфËЖ\x9cǔƇñń_ӟ',
                    'target_id': 'ȨʚÂÝGҠʲ˕Υ·ƈ2ɾɟʯƅˡͱЅǉÂѽïǫœӝӷɬġ£',
                },
                {
                    'event_id': 'öѕ˯ΣƘȨԤ҄ѾϺƹȭȹĕƘƠ\x86ñɇȾΦ˺øːӍȉ\x8cвŘ˻',
                    'target_id': 'ĔʋѨҭŎżѦ¶Ưǜ˰ǳԋȊǢѣԙϟȕȱ˝ӞǚїµĥŐЫŌӏ',
                },
                {
                    'event_id': 'ł=ǩƒјӻ˨ȷ˓ŌãϜОӖŽЂѷ\x95ЙΏȯѝ*ěгFŮɛόȗ',
                    'target_id': 'țșϺ\x85Ôɏҕǫɽɻѱ\x90ÿԄ\x81ƅɳΌǣơĴӻǿɆ|Ҟςɰǎ˼',
                },
                {
                    'event_id': 'ʫ;Ò¼ʅԑʵĬǚɼƣȰǉʻƲƌѰȱ\x83nDрȪԧǴͼ*ƾŗԩ',
                    'target_id': 'ʅƘ҈ͷ\x88ɢĹƃƓɮ˶ǖŝȼɍŇѣӢɟνǒ0Ԍ˄ЉyƶӸϑŢ',
                },
                {
                    'event_id': 'ɘΛԡɚυ¾ƍЫȅʸ˘Ьѡ>Μ\x84\x87Ҿ˪\x84ãYˏǙʍұǝ\u0382ƪɩ',
                    'target_id': 'Рƛûʍ ÷kƥuԛYǬѴÄНĞЮƓѥĴɏƕÀϫђӫ΅ˁΈɼ',
                },
                {
                    'event_id': '\u0381\xa0ÂcĵʤʽáǿÎσȰбČ\u0379ԓɟǗˡŉӐɍ˂ȟƮÚϴʫΞю',
                    'target_id': 'CƘіƼǈfʿΌǌoԘє\x92ϚłȾ8ɅбˏɌ4ċ҅ëӓԭӍκå',
                },
                {
                    'event_id': '˚ΙȢвµ\x98Ê@$ʥèķүhăȁ˗Ύҿ˙ΚӺʓʵƽǹüмʅǏ',
                    'target_id': 'ҏвĉŵкˉĄԫʛѭǲКѦǇ@ˍƗ³Ğʖʔ˓\x9fԞαѶ\x8cЅƤȞ',
                },
                {
                    'event_id': 'ƅƠȏΛÀóȖ˸Оӯc\u03a2ӡȊΣĚ~ȽŹȕѼш\u038bϭӐuĵΔÝF',
                    'target_id': 'ѸǵӰ?ӘԞ˧xӣЪχ˼ϥʓóОŶӪ˨˰ɡ@ѻWҿӛҦ˂ϘĻ',
                },
                {
                    'event_id': 'ÏʰȨċίǝʆŮеǡΰȱœȜҲʍƢҏϢɷB\x88uǋɹӵ\x97ҴАҁ',
                    'target_id': 'ʆȤʄʿЋȋƀɆӌјЂ˭ˀӿψӂ\x98˘@ɨӪɩ/Ǭяәȁ\x91Țϐ',
                },
                {
                    'event_id': '»ſȫΏӍΜƪïï×êѳ·0ƯƹǁˤȤφ\x88ǬȟѱНˬӥŅöǔ',
                    'target_id': 'ȼ ǇϏӄҗΆɯ\x7fĵʂ\x91˧ƛòΙԂ¼ɪ%ÇŮͼʈĵͲҞЌēӍ',
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
                    'event_id': 'ƟН·¨ʢǦɗʻŠʑҢϵ͵ǤĲKǤ²\x97µͿǇǧӂӔәΚ\x8eЇϨ',
                    'target_id': 'ʞöĬщ\x83ўƩǳ ǉŃˇǊˎЩɉ+хǄıǓŴƻѰĉ˔zΌ˄ʞ',
                },
                {
                    'event_id': '\x7fV҆ĮɩsɊɥwĨƐǧcÏͽӫ˛жδΜ\x8d˱ДƹƓÁ˅ȷĘӁ',
                    'target_id': 'Șȓ\x8eυ҈ҸӓėĜΖɊĵʾx)ŧӗÎ΄FӈVμΆϸʚƨÃœƙ',
                },
                {
                    'event_id': 'ӳӲÑĕLϭЁɍɣ0ΪВ\x93ʈǢŭĥϦˬƪAîɤҞȹȄĵįҰѭ',
                    'target_id': 'ҴȬɹʣēƷLƉѮԖ\x82ǅØɽѸƘĞƟķĂŚƉӚËƱѬķ6ɢƇ',
                },
                {
                    'event_id': 'ǵΜғȦ¨ʟ#ƑҒŖΆϡϾɓćɩʣСѺɺԊӲǓӀǱӺʷόЃѠ',
                    'target_id': 'Ѣ˜Ä\x84ʢŠƸ]ȿǠÎɭ˹ǅЇ˃ҀġǊ÷НԝÌДӖ˅ƕӓȜÛ',
                },
                {
                    'event_id': 'δԙȋИԩȷĕøȨˎĎČŇԩĴʜĭѡԢƝЋόƢρ˗Ü Ђɽǃ',
                    'target_id': 'ӐԊûơÊǥǄûςӿ;бŦӢӭŻʄѴʕȶzÙŋǵӣўǩ҇Ԟƫ',
                },
                {
                    'event_id': 'éʛѺyǡàǨįʡпѶ\u0378ˮ¿ϕľťʽɾ\x89uф×ƞ\x7fЫƻ˝Ɨб',
                    'target_id': '˓Ӣ˩Àĳɗɸʱēσ˜ɭ˳\x9dŚӦӼíɮʄˬԍӺҋmǃӦģ¹Ƙ',
                },
                {
                    'event_id': '\x86)ʍ¸ˈîÙǾʒ;һ>αǚĭ\x88ǬӥʴơԮӣѡ#ÒŨýΕǊÊ',
                    'target_id': 'ȢǇǟ©ЁЋϋľˡξ˧ϛӹʍԐ\x84PȠʾЁ±ɣМ˨ØnǵͶɁӠ',
                },
                {
                    'event_id': 'ţǺ¨ӥˏњђĺ\x81ȱ´ŶǘȓyɗƐȯŻԪʛ˓§Ȍ҃ѮҍƺÍI',
                    'target_id': 'ŕŤ¨ҝɪɹ»ϻɧĘĈˡéɟǣԤŠЖΉԌVӺɀæĵѹǣΨĬǥ',
                },
                {
                    'event_id': 'ɇͶ\x81Ћй˩TǿǕ>˞ʘ\x98ȿД˸Ǉш\x95ģ`ϝ8ЗˮĄԘăЈԫ',
                    'target_id': 'ϰɽӸʙКǧ˟ΩęҰӃĩɿЩӗōѶӹ˱Ɏİө±¤ιȽѧ˲ȭǣ',
                },
                {
                    'event_id': 'ѥĥiȉӅɾǿύτ8ĪÑɺͿ\u0382ĬɼuǶ\u0381þȡЊƇǎĢcÙźϋ',
                    'target_id': '\x9dŇѽЪɴ҄ˮΈʇЀÌӘѡʚџŘíѬBԃ\x84·ʹɆϽӭƈ\xad&Ǣ',
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
