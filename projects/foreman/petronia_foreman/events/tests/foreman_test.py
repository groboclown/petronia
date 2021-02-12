# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-12T16:50:45.910053+00:00

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
                '\u038dΓØŜʀƢԥςеΕΓªόϞϹѠµΕɬϮʈ˜đ˛ļÍɣҖǤѐ',
                'Ƌ·ȔǃënşʎÌҦØϡҲ˶АɽêϷþʄlʌѣˇ˜\u0378ҁǫJү',
                ',ԘоȑǃūǤ@ɊźƒѐȇңҐˈŒ?ĬɆѩӏċ\x86˰ŷΕ϶ȲǸ',
                '|ПǕʸ΄ĥɆɱ¿ӈԏ˜ҽńȻθԧѲ\x8eɆͶ˸\u0379ʨɫϤ\u0378ўѮҳ',
                'ίҊʳ҆Ę\u0380ʯɀҠўåÿϥΌbɠϵ˙1ϒӾ\x89ʣӣѫЬ~&ĽΏ',
                'Ûԝϛ¿ȌοӍÍƹĉǶχnÄ˃$ƨϖƍΡǣȡƺŰwÙ\x82ŊCά',
                'ΊƠLζȿЫӕΥãԩИǫȗʭҭǝωƏΆ\u0381÷ЊћдҋϜČȼӃ®',
                'κɉϻϑĨȲʸǔҭӔϽҒώέƋѶąҙϘƞʨ6ҤźiˋɻđҺş',
                'љʂϷľŲȃŦďʭέґ˾ǆƪʷͱЕ0οǓԛҭҔčũˉʲȖԁ˛',
                'ќęęàŮ]]ЊňʲǠŎӅ ªĕaӠɢУȇ\x80ǦʷѸƷӖѷϘЏ',
            ],
            'source_id_prefixes': [
                'ҊԤƙɐǘοѳ.aDǭǪŲϬīƗřɋƄȫϧGϣÅƿԔJɻȉǐ',
                '±бŬȘϵӴϘӈżͷЇ7ǧEҹ\u038bЄЂĜʮω϶б³6Ĳ˴źOĶ',
                'Éȫівȿ²ӄʛɬņÀѴ(ĖȽхFИˌƲǿϫϲƧ;ȔŵҫĦО',
                'õЀцʅġιӦԜǟȓϜ˹ЯFѰмԀһιӖ\u0383ðɹÌİɪΦ\x9eʚϦ',
                'ϧ"ļŧĮ҉ӗƯȌȤŝŅƲ]ӝɱ\x815ĭʉ\x94Ǚԁ*ѺɆЍʈҵǼ',
                'ďĹΈƲΜνƹ0ćԛђуѽǥЪęǚδҒƵКӊИКңЃńɇѫŉ',
                'ƤɞЖšćƻȁɟƓY:ҜɤɔϺŜЬľˉȐċϼΒºӋζʔǐ°ʲ',
                'ɍΊń|ѼӘɃņœȉƓӘɌΥȊŁŗǯ½ǉйȢɚӀл¥ԢϝĤə',
                'ΔιѾԨHȂtϤƍĝ8˃дʀ˲ɖħӨă\u0381\x90ϱɫțƆ˖>ɲЯϪ',
                'ʯčѪНнԓȡǗƼаλЋȋȕ˔Ҵԛ¬³Ə\x91ͻҸŊŲ҇н˸ʩĒ',
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
            'action': 'ϦєÏϡʄΞӄЀ¬įś:ʦĵыӯϚǫ_ƃςɧΩȕſχԙΩW/',
            'resources': [
                'љʚʟоҲҲĀӳɛțӼɼҶĻįʊƦlүƙɩ¾ҫʁZҡʎпŤǶ',
                'ȃӶҎɈ\x8eԊȆЏÔȤǪѦЇOњнęZӋfȍgÓȐѬҞø΄˗Ł',
                'ġȦӫБɜgˣȦ˺ʽѦӂҔӓĀҴɌƿҳ\x87ʌ=ԠŸƄʅӴԫȳɐ',
                'ͰɼŰFΑǣҿϟϓaɭˀƶҭηǕȴȥιϼҘǙǵԅĶ8ԦϿԭʪ',
                '{қҟ¹ʁȽ҉ΤƆʟïђŲ\x87ӤԊϙ^è˛ŎǠϯҟÚ\x88ͰίŘ˞',
                '҃\x9fъǚŖԎЦȫӂǮśʘɋǸсVˣɑɑŨԢ½ȈСрçǗŧâǷ',
                'ӠȣԏϮ\x9eҲϳӇ`\x96ƐːϔӪ"óƅţȂʣԍȰԦ˓ʸŸʉˆЭì',
                'ˁ¡ѝΪ£©Ȯż`Λ7ѭˑұVϓДүЪûȽǴǐŲϸКé\u0381ʡń',
                'ŨQǥŶѰ/ɿ\x85ĳʂ4рːyȱVԤʪñԡƭʕţԮ˛ȓą\x87OӲ',
                'μǊûįøϩĳԛEǾ{=ӪѭˊБʐͰêӪʪC.ϭц˂ƂĩӝҺ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': '£',

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
            'name': 'ϼŷʓʔ¸\x7fѺƔŖɄĭіˏѷ·˱ǭΓҲγǄ\x9eÛŁɔʻʔʬӽƕ',
            'version': [
                -3784591964811839531,
                -1458097673992220863,
                -1555336989653770695,
            ],
            'location': [
                'зʉӯĬԞǋȭɐЮɢȽԒғ\u03a2ӟӃãҵѪõʠǔ²ҖǂԀȄʮȊԓ',
                'äѓϛŸÊĎӀԭɆӫξʙżŁZšƀȚǎƊη҂ēºáÞǬKΔҼ',
                'ӝ\x8cӬʜяϣӟӕԤƘҙ\x8fɯĴҸЂʬʊΊʖȓŨæ҅ƃʒθýҭR',
                'ѕ\x93ÊЈOǝъɥҪīʓý\x8bӊžϷʦŊȝĻθϋ˷ҞЈAǅϲxԣ',
                '¯īÂèģHƲEǯÞμş҄џÛɬȉ¼ˡ:ƗɲĕȏɅҝѤɇɷ¾',
                '\u0379ΓƛϑΈˊ\x93\x94лХ¢ȻИ8˙&ǑԂ\x9bņς˶\x9cҿåǨȒˁƕǗ',
                'ҭϬԗÇχƠ1ЫŤѭëʉҐԉѲνɞØğĨ$ұȣȝƗŮŭƪǚę',
                'о*ιѧҮģ\x8dϥӈӐΑͻ˚WrΛɋФåǚɋҷʜϘŰŐůҶіѩ',
                'Ʒĸйàһƀu¼ƸЃ\x81\u0379ķˌΒ\x8ažɴˆЙƋoÊĔԌgŻԓĂȣ',
                'ŕͼȖ9ιɜΥżǖһ\u0379Ćʺ«ʺȁΗƟu҉Ҧ±ҷѾΆ˨ǐž\x9dɴ',
            ],
            'runtime': 'Ҹɘ¼Ψ¦Ъřɫ¨ČįƐ<;ϑНǷЊԅϥ¶˙җƍԇѨ}џԋԖ',
            'send_access': {
                'event_ids': [
                    'ÓҠǅѓԋ\x97ųϤƣȠ^Ӆ\x98Ό˧ө%ɫŎȓɟϡqȭѭɀϗЍɊ|',
                    'þӉ\x8eӁʭ¢еɢ;ɢǘϒŲ\x98ҁĐƫқäԃ˥ӑơӣҐӒNѼʞʪ',
                    'ǲƂǴȸɢЊ˲ҰπŌȲӥτλΘƨƳҢӺεćɅΥԕĮ;_ОВɷ',
                    'ѓ˛Ю҆ƨϋҗw*FŃĥ˯ƕͽîȻɬҖʹǵǼZӷȩıʕŠʲó',
                    'ʝÍμȟű-ӗ\x80ÞʜŪ\x94ʺ\x90\x87\x9dĨΞӒŕ0Ϧñďϵԇβ5ͻԡ',
                    'ąθǜƓЕʼɿɈʱ˙,\x82Ƴ«ȐÞąŠɇʴ˸ǖƎoǈѬȘҁŊ:',
                    'RӳϷÝȼЕ&ҎȿȪуӎзЙh¯OϹõ\x89ӂəҬɪýѶǱȯƼӆ',
                    'Ƿ\x82ӍǞź\x9cǝԓԀ]ч+ɷ\x89ӑ˚ȋėʊϏʊ\x9aɫӤьь\x88k8Ž',
                    'ӫВѻЂɸЫÙԢŖхӒΈȾŌˬ˪nӳɶԙȵ°ΘӀǡѐϷϤſʘ',
                    'rȭȭÍѓωңă\u03a2©ƹКӋŲɴ5ŒƿŶӕҧŻșѤÐ\x93ćɨҌ\x93',
                ],
                'source_id_prefixes': [
                    'Ϙ˙ŜΘͼǋɍÊĝӡΖȄ-pÇZԩ¹ɋЕŵƋӤŔŝƈ˧ʹ-ʎ',
                    'ƪ˧ϡʜϠ¹φ˃ӟʼˤȸȱЗŽȳԐΩĺ±іӮǥϔҟӆHΏƛ³',
                    'Ȝ6Ƚҭ͵ƯмƓ˒ѝˀʗĩˢΏͲ˺мϨȱ¬ӛĆʘɝÐưĆǥŤ',
                    'ҦǾҤɳт°ŰаʇÈЩúҥΗЖÔϫ\x8bʘ\u0381)δѻ>ыIɻŨΥɳ',
                    'φҟÏɠĭѷƪőʫӎ3ʓĴӁԉԋΥŰɡŮϷȼήșȴ:ØУѰÞ',
                    'ӉМĺǻ˝Ÿuȁɗ¾ȜWѦ҇ſŝɗǮɿŕԊй˄ѫʲӏϣǩƟŲ',
                    'ϡğҘ¡ɿ×ʰϡȏкǝĄłѱҤѱѿȼǡ8ϕΩԂÉеϠȬѰ5ӡ',
                    'Ȭ½˕ȤǠҮ˖ЪΤˁÆƠt]ǸǦ|˔ўŧ¹ԠϊɁ˨Iį\x8cѪа',
                    'ý(ӉȌ¢ĸе]ӗҁ˦ΕӣҍϲĔ҄ғЖҌφÐʈɇ!ǎĿɯƠȋ',
                    'ǴʁřӔȌǘïŦźdϽѻϦǴӤƈмϥʌΗǈĺҦɐƮϯɖƭ˧ɓ',
                ],
            },
            'configuration': 'ҀŲ~ϊ\u0382ǄђӑâѣȐNȸǒԝс\u038bůƩѫɏǙɕƕʓѰĊΩ\u03a2˺',
            'permissions': [
                {
                    'action': 'ɗΆɉȲĝǕѭíưȲĠӀĔπƀ\x97Ʈ\x91Ŝý3Õ\x90čďҲ®ϸ˂\x85',
                    'resources': [
                            'ӿL҄άŇȈԆįȂҏΓŕƦϧԗϖ˾n\u0378Ұfˢ˒ѸǑ\x7fԍǱw˨',
                            'ӋčӸĉѓώʚAÎԄȻŅ¿ǻǑϳԀɨoӫŨğǒӐɼĖɏȤԖɿ',
                            'ϐΥoΐ҇é±ɃȡŌ¬ѐĲ6ͽ}0ГиaʛıвЏΦˍњʀБǎ',
                            'ё˟ʱԉмԖǰʚӉʵӝǾτыƌӁх¾ʨéǉ\x83ѻЦˡǠΣ=ԝʆ',
                            'ĈщѰʇϿʾĤlƧИϜĐˇҷ˛öэʞϙӹжԓʈĝ»îϚǼЫʦ',
                            'ŀҐ˴ǢєǊԏĖӻÃ\x99ǌÕóʍɥɸ˹ϦưʟˆѳщžGɧϏ\x83ɵ',
                            'ˍʟʃЁBЌԆËѹø+Ίӌ\u0381Ǧʀ\x8dͶВ`˷ʸʗČ\x8bţ\u0383œБΏ',
                            'ƬŸƴʇѐ˝Ƥ~ũŁҘƚЮ;ǌӊҨфıÁӍƤμĹɬëӠĤǥƳ',
                            'ҮθŒ¶шԜБδƔǥː1ίmΣӬήLӱɀїƧβԌ`2Ūԩǀü',
                            'ˤԧɷԂŮӆѭ˙Ǔö\x8fҿч«qą&ʇǇĒßԖԎåɇ\u038dЉĤˤ˸',
                        ],
                },
                {
                    'action': 'Ҕʿԭȹʐ¥ωćϼѐмͺ©èщ\u03a2ӫ\x92ЧҊĮǪАϋʜɬúĽɠҥ',
                    'resources': [
                            'ČβѧōˆһɷԃɗiЌ˻ɂƐƛȧӜǫŬԁˋűџʉÕ˞ТʒԘҶ',
                            'ƊƐѸ\x91ӥƯ\u0379Ԗ˗τƤɬ¥М,źǝϣuơҸҝџěϡòӠљnG',
                            'ķ˾ÂÞҖвԍ\x8eЏ5ĚŮʼȸYŏɶҥūЅШǬЈχςeˈɈѝʍ',
                            'Ĝ."Ņɔˠñ\x9aMʧ҆Ӓǫ_ƨŀɁÓәʿϹϞӓӕоϕΌƹǲǜ',
                            'ǫǽβӫΒ˃ѳ˓$Ýò÷ȯ\x7ft!ǂHɫЦҲ\x8aŻϠӀҾUƎ\u0381ʵ',
                            'ǓʎʣŬđʤŃӻӌџԎ˙Οʷѵ¾˫jżƳɻɖƆƜƌȜɬ\\ǥԝ',
                            'ȉAóŒ\xa0ѱҏ˃ΦЯ`ЏǙʤˍҷͶϪȳ˨ȩҏӇҪāҼɔĥЎʕ',
                            'ЬʝǣϮɎҡΰżΟҡЂԓD}ѨͻȫƁºʩлǓĲňӗ˛Ѯȹь\x99',
                            'ђÂӮȨґȗОѷʡĚҀȣ¶ψ"÷ԀƻцʈđȦ\x94·\u0382ӮȗϿӖQ',
                            'öʆҙΛŧĳõ˧ȽŤʾлɹΧȃαʠĖű>ȮƤ>ÕƳ˲Ϝ!Ŗ˰',
                        ],
                },
                {
                    'action': 'еӧȑʃʀӵ7ĜEɼ¼ʴȗɌĖhҌɆ\x98҉ƛЩjRϨƞˁ',
                    'resources': [
                            'ΐċҫԚӁС~ԄUӇԄǼʋʉŞҒԢчҒҙλɩȎǥĹɦ(ϲˠѸ',
                            'ĨѢȟАŖѵƸїūԋʖɟƵΧžҭԭīӨóñĜɣƬƇԤǙԃԪǼ',
                            'ʈԧξ|јʴɊХíГӬȋÊǀӳҞΗѝӉԣĮʢ¿Ê\x90ƶύȓшť',
                            'ӯĠҾi\xa0\x81xѼɭŉ¹ũsƄǿˏɃΈҷɞhӢʖүfĚӿ°Ɉg',
                            'ˤȁιŰ¦˜ɳЅζɋ҆ρ\x92ӣǺƬӝ<-ѡͼ\x83σ˾§ΈʋɈȌ@',
                            'ɿЫϧĬ\x8aԫжŧȊǇԦFӐѝӚ·ɼ8ĬyΔπЃþѓĄŹȹȩÍ',
                            'ЂnӲȮɘ˺|˘ʺ«˝ǔΉӘєÃOӨ҅ʜǉȳԇĩϐȏӛ/ѦŌ',
                            'ǒɍӭɗ˩ȮšӁ±Ƹ|<Ұƴ¡ϒЀσԫђϷĞύϭԒŀ\x9cÑĸɉ',
                            'ɕΖȰ#əуңǇ\x80ңɠǹйӱӲˣȳŨƧЬƕƢƉСѺѾԧ¦±ѻ',
                            'ҳɧıɅЧμҢб҇¦¹\x93ȜȞȧwϲƵʠ6шɌАЬϕЕ!ӂƋу',
                        ],
                },
                {
                    'action': 'ʒ˟ʖȟѬȼ\x86ψƪȾÒϒԢȆˏԆҰóԇPȱ7ǥ\x99`\x8bĪҾ\x82\x8f',
                    'resources': [
                            'Į\x9bɴҕʴʨƢѕ\x8bӴǖºщѝƳРéǳќŻǄ¾ɴŦŴԊƅԕƥÓ',
                            'Y4ЋŌ©ЧõϮřϣҏƥѲ˯\x88άЙκĜΏ¦ǝŏƟǯФëѢаŵ',
                            'ǳαPˮɋȝβȿ\x91þѢɓßƹǒǐȌьҤƎԞöƼñ¨ɛʦΛЫü',
                            'ɰȜˌ\x96ˉĕųȳϗȮ˚ɋҜƃȡ˩ѕ\x81ρȩ\x8c˹ͿӅҌʝúҲŋҔ',
                            '0φԩнʆυͷӟтѻJԇÌԊіȷ"ĺѱ˯їËį˖ХæƣĻԡŗ',
                            'τŅɧǮеԪɷĄ4ϾȍɚĬҾԖǝеļƤͽƿʫ\x92ĺӻ˯ƎДŎ§',
                            'ɆЪ˽ЌÝɩƐШЏθЙʳ6ɒѬљʏϦђ˰(vЖ<KǷɧ5ύŨ',
                            '҇ͶϻҎŝ{×шƾʶûϠʒȩ-ʪҁØʽɞ\u0380Ԩ«ƴ˻˼ƍы$º',
                            'БԅƮB˾íʐѭʪʿɶ˹Ѓɻԩʪ%ήąλǞƀƣJԕȚӷϙӹҰ',
                            'ѓɰʟʆĆԈSϚȤҲЦǺдϿГˮмϧPΉáƧϠӞΉɶАzБɴ',
                        ],
                },
                {
                    'action': '5ИӕņïŝʯƏҠǏ8МϝˍҁҾθĢªʺȶĿ¤œɊҖ|ǦϪÄ',
                    'resources': [
                            'āϩ\u0381ήөԟ¯ӈ˯ɣƀʀғӅΪǗϬĺĞŀԐ҈щŖȰѡʅѓʡH',
                            'щʦЮƞϨ±$ˏȯΊέϐ˷Ȗ\x9dɌϲŻOú\u038bCͺЪҷόĳëŦЛ',
                            'ўȯʡɊ˶ǵɷɿҌʻΡ\x9dԎəǸφɷ˪ǦӢȖʇҫHν\x8cȇϴ\x99я',
                            '9ͽɻͷſǤѦϵǳɈʓˏȡϓȠʏɓĭӘĻϜİΡpʡåǮƶʑά',
                            '\x90ҘӡǜѰúҖeʇϠĤħęΆËϙȒˊŌΡUƉец\x91ȇƉҼΒǎ',
                            'Ν3ƏȌхпμǊӋ\u0381ѪǡơˑĈʳ҅ȫŧķʅµ\x8eӿΔň¶Ľ˪Ԉ',
                            'ˣȵˀѫÚÿɻĒϕŀÎȥȱ\u038dʭƝȩ¨ȁÐɺƭ\u0378ĭŗԛƐů&њ',
                            '˱ľ?іѝɻZǾȣÀ°ήMĩԥˤŽƁ%ѱʩɷėÌȸʭƱАƣӂ',
                            'ͳȝǫȮˍѧ{ӨҿҸʘјƯÒʥƸ҅Ȍ϶ĽǘĀқґǜÜǂ7жξ',
                            '³ϐӜȇуɃԛ\x84χUӯ҃ÑȢΜϛGυǫȦǛɑŇē\x89cѠD\x9eԙ',
                        ],
                },
                {
                    'action': 'ϺйʓĸĬǜωɫƾиċüнˮƌоöĎ"ғĈĮɁɇʩȆҮъӓʔ',
                    'resources': [
                            'ĒʃèҲѬlƀжўŎïƒǉѾ¼`ԢűΌǫ˙ƴØʧ',
                            'ĞȎĊșӐтԦǙ°ˋĨˤϡԀѧž˲ӭРȃŚЮԊѬŭӏҟНùӢ',
                            'aϔȀǦχԆɭȁȑaƄҳɩ\u0379(ʞ©ǉǄγѧȭТӰҽԛгƕѵЀ',
                            '2ÁҀѳď˦ҔDǞʹSĳҐϜϻmͼҭʨƘāɯȊŧǔǏȆӗ΄Ȼ',
                            'ΨǩʩƒlҤҐêȱ\u038d!ȬȾËÉSҎӭ3ԗǋҪƉЗћĄϾǤ^с',
                            'ΧӧČҁɃǈȩӺ`ωԨƥǃ¸ͺɫӄŷʅǺȵаʞƉYҙϴĸʓƧ',
                            'Ϯ\x98ƍ»ӨɝʰɨҤɟȀԌΒyϊňϸôǯ˨ΌïϋtȆͻȒÀ@Ι',
                            'ŖǪшǻF҂˫ӄɜǤɈÈȡɩÅʖņұ҄҇ÿɾŇƤƪԃŦϘĽɩ',
                            'Ԋ+єҗөĳŋ҈ĠεЩƷɡȲƼʤίûȏԏͶΖχĄҝĕʹƀ҂Ӧ',
                            'φţχӃ\u038dŢɻǙέӝͼʴfԟˠϐ\x86\x80Ď_îϸΚĐϻѝʁ;ΌΨ',
                        ],
                },
                {
                    'action': 'ӟцűȖЧǺĆλСӢӌİ\u038bōбșťӆƘВӢ{һļѐҬɓϊǎƐ',
                    'resources': [
                            'ΌǦRїʧ˘ӀłŗКŕЃǚłˣǭ}ƗȐѶĔϜǏƯ¸Aʹęđɺ',
                            'ÍxɅ¥ȴ΅£N\x83ϓΨʚѠ˭ƑèȪ\u0382ǜ˗ȔȌǦѾҧƳѶɫ\x9eԚ',
                            'ÆҶ\x83ʝƵʗŊ¨ϠPɾɻ˷ǒȯĢ҈Х\x96ԡƷßЂоӂˤƥѻ¨Ѕ',
                            'ȞҢѦђˌˌřȰԒϬԡ½ˆȓӋυʆƖ\u0378ϥĝɃĎłЭŐαԕɤq',
                            'ͽĦԈġΉ\x99ЭʹhϞXƧŰҕҁȮĆȶ˙ōWɄѰØ˅ԬӋͿԊώ',
                            'ѵӐю\u038dӃΐYƜÔÐřƽłψŞӔ]r\x9dŔϤĊŞШΎӽ"ёԤћ',
                            'ϲҿПÖ\x83ʠł8ĝ˔өϲõһѠȏÔãэξʹÄԦȩĪƊϲɈӛƌ',
                            'ԮϡÓʆǌŜ΅¨Јoѹ҉ʬӀηЉǿ\x87ÇéөƜϞәΛĕƻŽĪτ',
                            'ɒƲõóǱ©ϚҺsВʗƍTĹ\x9càѵҸėȃ¿ƻϷŅVǆȄ5Ѭ\u0383',
                            "¼Żǉ\x80ȡ=ԐȆПӔşƥ'ΝȂ=ǀОфҥǨǆҸϟԢǇӠӹĻ\x99",
                        ],
                },
                {
                    'action': 'ʙ$˓ȧ¹ĩ\u0381ӧάƵұŕ,ʱĜ˞Җ\x8bЌΚQȕǏ3èŪҿΛɀЬ',
                    'resources': [
                            'ģǝϠƵmŃÑγӖǃ¡ɠѕćVʒ\x8cҸ\x92Ο°ɉ˻ɶ°ɺğӚģ®',
                            'Пɀό"ƫѕƧҝʍӯѾĨɼǂGϗЄҾти¾ЎƲбUŌʵΜɐñ',
                            'ԈġƬ)hηĿҲȧЙ˰Ȋ¬ɚ¼ƨŮŇЍД˾ԤӆʙАÿtǯʶȭ',
                            '9҆ƶŢȓƋ>ʣҏ~˂ԅUѮȡèӵƖɷѼʜѫɑ~Ȭ\x92ɇYӄʹ',
                            'ҸɐêĹŀbӖüƭҟXƌ˞ҳԊҪĮȚiŕðǋƛŽŋҬ˙ЎҹР',
                            'ȝԚѴԜνυ¥ђԒά¶Ƙͼ<їĖʤƙМŜŞΊԭńʟԏÂЭȀϥ',
                            '®¡˴ˠԇӐˉFɆҠƕοˏʜŜ˟ѭжЉȀѶ¾ϜӨ)ǅǁʿQб',
                            'ĬʣԊĨĮԁʣŧYΘŀAɑӆɆōȖшǆʤƃөDȦµͶ˖Çώž',
                            'ɟĕҞǑПλŗϜϾҎǿcʌ(èŪĨƛƢ;ʉÅȈ\x88±ѢŸİÞ\xad',
                            'ԗĪ˄ȍѢȔǆÞǑӲ\xa0ĥʉǔԐƓƊԊğќĶ˴ȿԌǿȥӁƱáϹ',
                        ],
                },
                {
                    'action': 'ϡȿϢǑˬТʠ҆ψý',
                    'resources': [
                            'AùǛ΄˝ˎɟЎ]ƈԌӻCʠӴ˳ʋҫǗʻыӐɫШ|ȴΏҠβʒ',
                            'аřҸυȷǾά˭XĹҶǷǇʵҼҿ\x96ɦwҽ\x88ŌˎŅƤԝ\x7fʎ,Ĳ',
                            '˞\x86ÜԝҩʩϩҙӐĔάʚҒЧЖŴӢИɆԖˇĩςǊӂħԍϸҠА',
                            'ƘzėѬNĳγʦЅȧhɏkŬΑҡǵʓÊθͰ´ԁϡЮˢƥ\x8aȼњ',
                            'Ԫ;ϫǿ',
                            'Ц¹šʪüϤbąáɈtȳйѰȋԇ҅ξƭ',
                            'ϖʓǁÛӓɭΔЁОύƴ¡\u03a23ɁѦφœȇ˓ǕӬFƄ8ҴҜſύɑ',
                            'ƅnȬƉѷɰśĜ,ġɆϏ¡ƘžȜϦјʌ˔ȧɚЭɁԓԋƇÜʝʻ',
                            '˾҄ԉʨѫ>ɷФͰOΣoɤϼƞƽ\x89ӇË®´wľάǦƸѾɪͱғ',
                            'ʹΓŗԅŅӼϤщ´˼ԇņnªͲ\x85δ\u0382UҳɬѢȿϲҴ҉Ѵ΄ŽÃ',
                        ],
                },
                {
                    'action': 'ӿҡp˹ЋƿͶ`ŝfЀρ҇ȟҔǟβĲӘǏЧɽİϲNľƋҧ!Ó',
                    'resources': [
                            'ѹWďϦʅƼͶΣЛҸʂɞўǆӌȳɐƮӻ\x99ȉԇ\x99ʧΈƼϦċǃƼ',
                            'ɖΙцúʼʗ\x9cÉ<ÄҼ\x8bΔǯѪxʏжˡ˙ȾƼһ\x81ţγʤʨ˓ʮ',
                            "ƟŃ.ӬЋƛҋƝCӐ'Ūʲѱ\x98Ҭʚ\x80ˡSҞ£Ϳ\x8foʏȕχӾƼ",
                            'ɦƂƀӿŹҽŞɩƁҽұӥÌơўўǨДȅӍιƲȴň÷ε¿˷ѷʆ',
                            'ԞϟƌŭґBӶĩʿɨéΟԁͿΏiӆƲXǜϢѷϐȦϡ@дɎ˞Š',
                            'жвʕ\x82ɏǡʲʸʖԝüȾ;\u0383Ã°ŘϓʢŨɗÇ¨ó˳ϠҪȭŢЄ',
                            'Ҁ\x96ϨơǇˣɱӲκťnʕʙϫәԊŸ#áʎřʁҞҭќʛøȝĢ\x83',
                            'ýϐÅʊʳŶΥҨϤ\u0380үˣ˰ψΙ˙Çó˔ˎʽǨªΆˬþŢϲ˳ӎ',
                            'ЕZƤóԝwŮΘĻεϓŒųӉфγƄĿŅђŜɎʹ΅ҺԂEҷԚÍ',
                            'κƦǺƑ\x88\u0379őƪͺͲƆҒ\x99˞ƶ¨ҏͰˋfŷʗ!÷ĽӛĦƿӚȩ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'увŪ',

            'version': [
                -5660986637658267995,
                -1920978637524022535,
                -7711872373625752537,
            ],

            'location': [
                'ɻ',
            ],

            'runtime': 'ç',

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
            'name': 'ƌè˧ɔԦԄűĜҀѮàуӖ¢ɎʘmԠƹĀȂʹζĥӸʦƽʕͷέ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӣÝϖ',

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
            '$': 'пȦѳĢύŅϖǣҩɴƉ˕ԟȤʕұҙȸȯԟθȿʜɸ§ϒΖƬƗѡ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1974862795247738928,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 598100.4359274334,
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
            '$': '20210212:165045.856423:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ѯԘ˙ʝҋϙ˽\x90όҎҮұĕε\u0383ųǔҋƥԇţƀŔŌĘɷЌ\x9aѡˢ',
                "ůăԉ˅qķҏЁÄɃ'ÈϸԘДɑĩӦďͲɭҰ¢Ňí҉ѣΌƛ¡",
                'ɲϚΟҏƱΆЩˬŶĩҦїïǄ\x93Ğɱ\x80ȨϠÃ˒əȪŧɜ˖ԎLŽ',
                'ԞģʒЅπγčҮûêʱxԒӛѥńνƆţүǕðЅ\x83ҿϘНǐΤʾ',
                'ˌπʌȍǑǱўфԩŲԄMØ¬c\x8fэśÅʂҎÆʔΨʮŌμӱ<Ǹ',
                'ƋϬʯɈőӄŽӏӋ˖˹ɯďƹ˞Iэ2ΝǷЭč˞˃ѐ>ÉņɃϦ',
                'ƵԏɚŸɱВ˒ӶųчέǧĸρϝўӂŪʈƞʳӳƐx½ɒΣԈɩs',
                'žӞˢ¢ӪϾ£ŖҬʃ\u0382˸ßϝřӮ˛ѻ³ȕΡYυȥ˧y˥љӓƬ',
                'ŲşʗĊл?xƲģҫЌЂѮʅєȠŲJ˷Юˤ&ȜҨħцɏĺġ«',
                'ßҕ4ƨ[\x8fӨǈӶ8ǍĹģ{ѤÝˉъΗѶÝЮƧȯː;ΒǗ\x85ѹ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -8913858067050118622,
                -6045064644312402513,
                6221264564930314758,
                2594335609231055578,
                -4690897178986069914,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                383871.6788890468,
                893025.5011247785,
                726014.9686402561,
                873558.204976091,
                646191.1763755814,
                241374.21444670495,
                6656.543724910807,
                55561.6567321379,
                704961.3289173977,
                -42720.51846922155,
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
                True,
                True,
                False,
                False,
                True,
                False,
                True,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210212:165045.857309:+0000',
                '20210212:165045.857324:+0000',
                '20210212:165045.857332:+0000',
                '20210212:165045.857340:+0000',
                '20210212:165045.857346:+0000',
                '20210212:165045.857352:+0000',
                '20210212:165045.857358:+0000',
                '20210212:165045.857365:+0000',
                '20210212:165045.857371:+0000',
                '20210212:165045.857377:+0000',
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
            'name': 'Ģƛę4\x88ϋøȋ\x97ҸЃƛˏԂį²\u0381ĨҏʐaԥǇƓÝP˶',
            'value': {
                '^': 'int',
                '$': -8806582580757592978,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ȧ',

            'value': {
                '^': 'bool',
                '$': True,
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
            'catalog': 'ĖοʵŜӅɂЎʈ]ĖMŌԧѿғVΞȹҽɑŧÛѝ Ŝŭűĉ|Ȫ',
            'message': 'ȤÐґǞѐǯ˒řтˤƸҪà˛ӣPԀӕȠVěƦćǥŢƬ΅LȌȟ',
            'arguments': [
                {
                    'name': "Ә'ӧ\x8eĺHӿνÿiыӛюɀȦјΏ+ʠɄӵǁѩ;ӿƮǶԝӐ\x86",
                    'value': {
                            '^': 'float',
                            '$': 881245.3794933128,
                        },
                },
                {
                    'name': 'Ͻwȷχũ',
                    'value': {
                            '^': 'int',
                            '$': 7504401791404333973,
                        },
                },
                {
                    'name': 'ϹŵǼυͲƧĪВʬҳ҄ӠǜԓƵԠʱҗq',
                    'value': {
                            '^': 'datetime',
                            '$': '20210212:165045.854268:+0000',
                        },
                },
                {
                    'name': 'ͶǂͶхǒԔɩ\x80ǒŚɼhșЕϹЯȄўĊɝșψʝϬˉҸӝìƒɮ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        False,
                                        False,
                                        False,
                                        False,
                                        False,
                                        True,
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ȽǵέŻѿŀЮԟԟ¼2ѝ˾Ȥ=ӹĲwȐԌβbʯŃ)Ͷ\x7fġφɭ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ɗ˽Ȣϴ\x85ђԂɩčѺȥɝрӺψɭигǁ˺ʉEϒЮHƸŲǌĀї',
                                        '˙ŹԐєˏ\x96ѦжʹȜAњɣĄ¨ǫȈȱĉɨѓȼϪȘӬӨӿʍҞ!',
                                        'ΜşйʠƭӮɴʂұʣʂ˨\x9bƐȷ\u0380ҡϩӗ',
                                        'īņӹəuΏӥRʚɭ¯Ȱ҉Úщ2˚-ΙӭΝȁӀԡpӏ˺ѳ\u038bλ',
                                        'ԚȾҚђҕʒȮ\x92ɺғĊŜǀϡ¼Ԧɲνǋˊ\x8cǒɉųȦΏɕ\xadªÜ',
                                        'вòțɄʞ6ǞӸʈЫ˶ȄǞĪê\x9eСбЩΥҫˊ˸Ͱ҆ҎʁǹĵД',
                                        'ƳǯƪŸ¥¨ԜɩͻλƀӔЎɪʟǺ£˘±ѮΣˊӠϙ8ȐƧѐԪЂ',
                                        'ȧƱCɳ9ҐŝɐɤΑĝӗє\u0382ҏѤīĕĥʖˏϺǓ¦ƢŨѧľȶ¡',
                                        'ťѐΐŐǜˮώʩϙ˸ɯÎňȉwÅЋѦһɋ²Ɉ\x98Ѹ#Ԑɳĝ+ˇ',
                                        'ʦʹӋɳƉgǣѹԊρɞҪuƂԆˀҚˏÁæůϳǮȘɅŬТƐ\x8cД',
                                    ],
                        },
                },
                {
                    'name': 'ӆŎǕȣ\x83ƿӴԁ˳ʾƟԆϾңпӹŒΌōӓvǛåʥîhvϖԮQ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210212:165045.855134:+0000',
                        },
                },
                {
                    'name': 'õΤЄĺzřőɇǙΦҘƺâ',
                    'value': {
                            '^': 'float',
                            '$': -75.03405997193477,
                        },
                },
                {
                    'name': 'ǽĥñƣƽˢƽҞđΓŵșΠɺļǈϑл˯Ǭ(EŠƣɀřйҟȃǀ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        728921.1827400333,
                                        594463.408638424,
                                        437561.3515410952,
                                        -69110.71764083618,
                                        933160.0552735926,
                                        364057.59884780506,
                                        6764.154841520882,
                                        921644.0501503221,
                                        302466.3194993965,
                                        777623.3284853209,
                                    ],
                        },
                },
                {
                    'name': 'ȳɸ?ǙˈĨӲçЄƆʽҲ˶ěüΉҗӄЋЋī',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210212:165045.855617:+0000',
                                        '20210212:165045.855630:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ȴ«ɦӔō¾[Ğӷ·ΠҮԇRҠˆΥѴİ\x91ȴʱϢʕϨ\x85ˏϭŘϧ',
                    'value': {
                            '^': 'float',
                            '$': 836352.8244948247,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ιğ',

            'message': 's',

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
            'identifier': 'ǬˣɩҶqɬ;ҡɌαїƋʉȲȂѢȠνùʣÌĒŦϡɘżɀϋȠś',
            'categories': [
                'internal',
                'internal',
                'file',
                'invalid-user-action',
                'configuration',
                'invalid-user-action',
                'network',
                'network',
                'file',
                'invalid-user-action',
            ],
            'source': 'ұ˒Ǵ8ΙȄ|ϯʼЦˠΛɭrlVҕɖΔɒέӮǌǧƝӁѱǖRЩ',
            'messages': [
                {
                    'catalog': '˯ѬŐΕʜDюɣCôëȨ\x93ǄƔҡ,ÊҢʢЯϹõΫ0ϕǎ¡Х\x89',
                    'message': '¾ϲζϙʹЎˎȘĢȁŁѽ˓şЌšԑθ˟˷Є΄κȋ@ʬbҙȆǞ',
                    'arguments': [
                            {
                                        'name': 'ŎɔÒpǣ>˗âˆÃзЌG\x80ƾԎȠ˵ǀů',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÈеƥԇŸ¿ӢăȶȅӘ¹ŎJσӑѼǯɮоҿȒӺșѐΡұ˾ǪB',
                                                    },
                                    },
                            {
                                        'name': 'ʦĻƓ$*{Ư˛Ȓ¦Êô',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Μŋˊ½ǀvȯĚǚьҨѮūEÓчʬĨ¬ŎƐƻ˫ɌňœŮΈ˒Й',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'љÅÞɭҐŨϳşśɌ8¥ʎ˛òƁϫɯЂʲƔΣȢį\x89ʙē',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'нǭЏʒ\x81ũʥοȖƶQԠ\x9dɺ1ϙƲǤłxʹύƶВȅӟҙŕīϸ',
                                                                            'ͻҐ϶Γ¨ˌɶςȻŅаtķΚÂϗʲzÄƭ\u0378ѱɦÜʃÌпĔӷҦ',
                                                                            '×ηСȀǪЪӟµň΄ʎІϑɑҾǆ\x82À¬ԪǫӐԪΒûʷȥʤΣҮ',
                                                                            'ЁĘƔƜ҂˰ʅүȇȝҰɢӯ´ЕŻǿԤıЌȝεŰїĽĻҮхćӁ',
                                                                            '˥ͻµðßӞџӘϓǁ҄åƫþ\\vɟЂɢ҂θsȉ5ĽáȔԭdʞ',
                                                                            '@ɪРƻȭΩɶԫɆϝĈɏԈʈ\x84o\u038dҫ?¨ʊnϨөϣƑΠǈȚҎ',
                                                                            'ƖһʑǹÝӆ\x95Ћҍ˞-ЙȸӬѭ\u0378Ά9¹|³ʊƑnͿӰЦɕɕæ',
                                                                            '}Δņҕ\u0379ЊƮҟЊƃÅȘɤƒŁçɜҷ°ŚÍƀӴâћӧ˵ƴЮѤ',
                                                                            'àɳ\x8dǂĶȗȓƥЁƻʽΩѵǞΏΗϳθҫɩӘκԠӅħӎƟЯϴ¿',
                                                                            'Ӭ\x82ʴ҇Ǔ\x8dơɑӚʶȍoƷΘӸӘǹυȇɴ\x98ŝМ¨ÕˀѬӐϬ6',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϐɔ˵áФҺ}ɌƅԡɲԮҺſСлˀȺҵь×æԞ&å',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            59380593356578647,
                                                                            9083140140741036453,
                                                                            -6941367987956583599,
                                                                            5704815357735728263,
                                                                            -1399402598558822349,
                                                                            1474257166842674952,
                                                                            -5687643812169106909,
                                                                            7391966459256197308,
                                                                            -3239354110902266719,
                                                                            -4066333174045326091,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'чѳų',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5626698523869766191,
                                                    },
                                    },
                            {
                                        'name': 'ǌ=Ѵ\x90ŷæƪʢțҫɠȎʭˢȮǑϊûƏȲJϦɎ´˓¨ʢǧhí',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7534733558238151875,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'õËѰҍčԍѱJɀԝ˥ ÖіŗЦ#\x8eɔ˩ǊƩОИϰƲɜϕҚО',
                    'message': 'ϥƑĲʟт(Пӕέїиƶļ\x92ȼёƤœʩɰĭԧʫÿʨԋɷºϒȆ',
                    'arguments': [
                            {
                                        'name': 'ƋȼǠŹϫԗɞѦɥƧЪԕЃɟŃʵȩҔȱνԦʍɑĶǦʩ®',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԥҠЂɱŹÏPjЀЕԖȱдϰӹ\x80',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            787536.9377054338,
                                                                            408478.7292186044,
                                                                            974176.8298907983,
                                                                            842285.2544469653,
                                                                            459767.34120196453,
                                                                            -80667.23589178143,
                                                                            836283.3136652387,
                                                                            858815.9394736378,
                                                                            884609.6041593213,
                                                                            80214.53211007648,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0378ʧϙǍó˘ŪϺˇ»ђKʪҚƣŃ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 545124.9016378009,
                                                    },
                                    },
                            {
                                        'name': 'Ŝɵdў¡жȞҿȔƣԍϮ=\x9fşԖϯŐǐƺȦńÁӧҰâЈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3941516624941898195,
                                                                            -3576864782259704131,
                                                                            -3775363688193676264,
                                                                            -1069161703655508144,
                                                                            -3936583045028101251,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƫqԝԛԨŏӭɲ¦ʹåɗɞЭÆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -40233956899863495,
                                                                            -2779150260456453862,
                                                                            8485057316521580450,
                                                                            -7162369638827038524,
                                                                            -6188681133000355945,
                                                                            4796804691738509266,
                                                                            -6891827887998981717,
                                                                            5225942314506221276,
                                                                            -3832574102769273566,
                                                                            7568214589109449920,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʁˌÌȓҞџ¶Jͼ9ҝŹɗЯpΥѢ{ЌИϣŊΣѐлǅŻɉςɞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165045.831569:+0000',
                                                                            '20210212:165045.831598:+0000',
                                                                            '20210212:165045.831606:+0000',
                                                                            '20210212:165045.831613:+0000',
                                                                            '20210212:165045.831619:+0000',
                                                                            '20210212:165045.831625:+0000',
                                                                            '20210212:165045.831630:+0000',
                                                                            '20210212:165045.831636:+0000',
                                                                            '20210212:165045.831642:+0000',
                                                                            '20210212:165045.831648:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϱˠǜϻƚ.ɹԗūи£ĥѿϭʻ\x86χ¨ӳξǬӋɛƑԦҀэŵ¤Î',
                    'message': 'ʨȘĸ³ƓӘϚԢ°Ӝ͵{³ӉƷɩώΝ˴˪ýɱ\x90\u0380ӿǕӐƀȆы',
                    'arguments': [
                            {
                                        'name': 'ȦҹɭДǰеǓЃĀΨɋŵѦΝv|ɷΘЫ\x8bϨ˟Ǧεϫˋŷ˨˫ɾ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 446611.0781115856,
                                                    },
                                    },
                            {
                                        'name': 'ĮēӸ˩ʦȡ\u0382тźӯ҇Étɦ*ɇűȦ)ѺŚѫѓШȈʑōɇǈŽ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7109003610960006325,
                                                                            3324245836310393243,
                                                                            -4772270818996036445,
                                                                            -621712200754493501,
                                                                            867748583941578393,
                                                                            8069835394228147358,
                                                                            9165430795810897686,
                                                                            -780136935797838780,
                                                                            4850378889758392792,
                                                                            -3962770098151671902,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x83',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165045.832553:+0000',
                                                                            '20210212:165045.832570:+0000',
                                                                            '20210212:165045.832578:+0000',
                                                                            '20210212:165045.832584:+0000',
                                                                            '20210212:165045.832590:+0000',
                                                                            '20210212:165045.832596:+0000',
                                                                            '20210212:165045.832602:+0000',
                                                                            '20210212:165045.832608:+0000',
                                                                            '20210212:165045.832613:+0000',
                                                                            '20210212:165045.832619:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЯӍĮǭƩ(Ιϑºƶԏ˔ĕQҵśĖlċȳʃ\x7fҴk˹ϕ˨;ʹŖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            500591.7341428733,
                                                                            685578.6434754514,
                                                                            212999.34664351348,
                                                                            134622.12721541026,
                                                                            771149.5608360063,
                                                                            495255.6100010021,
                                                                            256206.72175335244,
                                                                            461568.16077029274,
                                                                            154036.6013665451,
                                                                            113726.94606231412,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǛȘѠŘóӔгȖĴрŽɫƩͺʸԖìˍĿǭã\x89ŗƅɮŲʮʓēЗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƽ˚ЍҨʗΪӰħҽ˔ȸÞqǋƚˋĖƔȘңɔǄʰǉԖaōʨӿƬ',
                                                                            'ÀɂΕ\x8cǯм2ǋjΉ\x83Ʃ˰v˥ӤʃŷʐʙȒȕɁşˡɋ³Śȣʙ',
                                                                            'ƌϩ˳ʨɾǱԍϖʳƆȠÚŐˏĄЫʻӯɻ?ɴĖĪϼdҿїPΘѯ',
                                                                            'ЎʏÅͱЛɖǚҩПʼоҡψǫѶЙҫʵĥΑ/ļý*Ι\x81Ůёяy',
                                                                            "·ΒȮѣӳȉŝλϣTԀ'ɉԛˠŋΐ\x81ҬӅͻŨǙΪтəѻȇʚŬ",
                                                                            'ēРΖЫ҇Җφ\u0380ҟќΑŵƉÿιԔ˯Ė¶ĕ˔ǓӆΪ\x8aõɇʠäƖ',
                                                                            '\x98ԠѡvӤҍ®εľǭǝϵŧĚʁĴɵ҂)ΰӨϪŀ\u03a2ƋĨŔ\u0383ԨҨ',
                                                                            'ƝǺiоɟʖɩ˙tɆƢϐŁǱëіȯ˥\u038dğˈќўԘɷæ·ɞчʆ',
                                                                            'Ͽ/pϪ<ԛ¹ѡͱĢ¥ƁҘ\x9cR(яęьԞ\x98ӹ҈ԂǼɸέíçѓ',
                                                                            'ЂρƥɜǇłψÄdφƲϽ˞˱ȦϦTǁăŐˀWͺĆƽϠɕîʕ\x97',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȷȇĊұӿЭԨȮ`ˍ¿û҉ĒȝűĠˑьʫˈɿɏλɒәʁĕȟУ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3816565235215651137,
                                                    },
                                    },
                            {
                                        'name': 'ʡҩҒԢ«дϑɔjǾѾύħӁƧǁĝǫƅσůȷǋЏϑćÜƀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 746051.5975136828,
                                                    },
                                    },
                            {
                                        'name': 'ʀƶ҆ыıԨÂϾʢΈȺǓĭεϹũ)\xad˶ÇȶГˈȌюưνƛ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 31129.015722128912,
                                                    },
                                    },
                            {
                                        'name': 'ŧź\x95ʸ\x9aʟĭʸӯʷ¤ɀηçƱǌԃӫΰʣŤӽОϧҴȡρȃʷʆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 46374625653127306,
                                                    },
                                    },
                            {
                                        'name': 'ͼǡԊѤȑºā˩˲ŵʣИʚũ\x90ȈнμίņşƱ"\x83ÔDѿȅӫӒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 279729.91943602165,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĻдǛǘɤƞЏȴ˃ΨǆӰѻł˗ѾӦρɠтϞĕȵˏŘǩă˓Ӧϧ',
                    'message': 'ДˏƐ°ό\u0382ÂΦĝˡqѶţ˳ɝɌӹPǟӋƠǚşyԜ!ȁäľƶ',
                    'arguments': [
                            {
                                        'name': '˭-ùԥ˔˶Ɩȧɤ«ÅǇЁʗȎθϭϝǮϊѣҭӓ˗@ԍӗɚЯǍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɉƄЉ҄ƲˉƲȁƙˠʼʔʓk҅3îʿÍˊVŒʬǸΈɹ¶Ǹ\u038bȌ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˯ͳҴƔȑĈΘΪŞҿԙŰѴѯѺЕБҺ»ʇɬϐҠԓƌуƧШǶȞ',
                                                    },
                                    },
                            {
                                        'name': '\x9bȤρȠҢʊɟϥЩ|=ǞƯͺ2ӀĊԢǗϑńg¡˽˘Ԓ˝ŤŁʵ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            139752.0794825222,
                                                                            319010.4076789171,
                                                                            972849.9895648791,
                                                                            836334.4603273215,
                                                                            -68179.84152419718,
                                                                            -54599.859033592125,
                                                                            417751.84623409563,
                                                                            368549.49595608737,
                                                                            25711.499652470273,
                                                                            716135.672949618,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Īϼԛ˟˖ҙ͵ϫʫŻƎġěõʟϼɩϭή«ɻëӮɖˡ\u0378ʰ˲¬q',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4767628088890217197,
                                                    },
                                    },
                            {
                                        'name': 'Ϛ°ŢłĀЛŵńŏʲYȭǸW)z*ǪɇūGţԐːδҜϊ¼ˍˣ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '¬Έϻ\x81˾Ωƀ˦ȫ˱\x94ӪԢщȨԕdÃ\x8eʝɅyҝƂĚ£Κ˷хé',
                                                                            '=Ġ1]ȫ³WŢǞӒǪ3&÷ɏɠˣǋǴ˸ӁDFǧÚБҒ˂ħŸ',
                                                                            'ǫΫɧûƠ_źҶʲɛЛaҙɫ*BΰњԢҕɞѫ˲ʤʌ%ǩ±ƀ҇',
                                                                            'Ѡ\u0379ΧďˀEæ´Įϫ˷ǒˣĭԑҥŰϓʵƛǈѣӽìЫƻ˱ɢîä',
                                                                            'σР\x81ėĉėбʾԌşśƤΎlƀɌǣӇʈǽϢ˯ζƿԗŚMʀƂ?',
                                                                            'ï\x98ґʕǣʻ\x93ӬƀϽ\x9aȸτϣĐȴPƍƪAɵŵΧȫυ\x9dÔњĀŔ',
                                                                            'т\x8fɫήŌ˦>ҿʁЪɍÝʭԋϕÀƟԜͶʠʤ¤·ĈЛƥɉ¹ƺ\u0379',
                                                                            'ǤŅсńϡĝъ\x97˷ҹǰϺ¢дԨ˧ģЩҢȘɃNхЅĨĀ΅ǖǦӘ',
                                                                            '\u0383˝ʷȽѰƧĘÎЪȐǉJʏр÷ÌѯƫǮҘϹœä]υǳƚɔȀƮ',
                                                                            'ѮҵӨŀфԬͷĪΆαΊʚӎˊгИќɬϔʈʃϿϠħӀǮη|ҔW',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'YϮŒŇϠƹƹԕϙҾǳįtԊμʘ˒ȍêԑӁɨƒΠƚІkƣЉ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1278040348396426328,
                                                    },
                                    },
                            {
                                        'name': 'ˉʽJӗûĄȻȫʟǢΪùϺӚĊПŰͽ¡ǌǽȠӠҴϊǔԉϱŨӌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3270748530919534151,
                                                                            4146845222798533942,
                                                                            1174662210163641603,
                                                                            -7680690462352473174,
                                                                            -3583335587796620230,
                                                                            -2830555618324059405,
                                                                            -2930884463808980528,
                                                                            5149412637107143663,
                                                                            1503610209470499879,
                                                                            -3260544787923111661,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'аƪ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.835732:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x89οӢ\u03a2ˮӘѵĶǗеūˑƙ^Ϟ\x8aĦ\x9aʖ,ƛΛĬƵǓƆŮчԝϹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɌąӄȿѦơДŌçЕɬqɄˊɨPɨӰ˶ĭɪċǫkΓÈ½zӝй',
                                                    },
                                    },
                            {
                                        'name': 'ǀRЉɕɰњҧÛϮƯЎǊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 829468.2471893537,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ВΑӶ˗˃ʫҦˆѴƺ˚ӆЂΟĄͷËːѪĝӧ\x85ʤÍɫиϸ˱ʺЖ',
                    'message': 'ʻѠʦ[ӷ˨җЖХ˕jɂɝLΆĕȷķªóÃϬǵӹԋ¡Ҁ,ĖЈ',
                    'arguments': [
                            {
                                        'name': 'ˌӃӐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʘȎқƪɖȵўƳȲǡ˞Ė\x8b˔ʰӅKӊnӭӹǺԑӦӔіʖϕȪǧ',
                                                                            'ұΜŲјə϶ӵԌѴ¯ƸӀЙǽΡĥʻȮнɂǳҪŇęʸϱҌʣˉ΅',
                                                                            'ʎғї˾Ζ\x81\x9fǪηŹɌ*ÇŘПɖ҂\x88ŴŘ9υŎ\x8euϽҿǿϹͳ',
                                                                            'ІӶҙ˭ҝМȝǀȟĝ°\u0383ôѣͲȋ@»%ũΈȝӞӬʪόÒȶ˯ʏ',
                                                                            'ȝϑԌȊơʄϺæĭĲžRΠŜӕАĞЦůʭʸÑƔȽϪÉӖЉΫʂ',
                                                                            '¯®˽ȖƾыΔн\x8fԤТ\\ͽќ3˝ȎҸʽéІŚϏ¹ДuɥҴ{ӊ',
                                                                            'δȼǇŻčϊ\x93^ӝĚΧ˳ҤɓjˆʘʄȐҹҼʑ˳˓ΝɿƄͺÀ¾',
                                                                            'ȍʱԓԨ^ϰʈЉя҆ʓΚʍɲG\x92ΈȾΰƠ{CЉΝӰîĿĶӹ˥',
                                                                            'ɞҘƩıøȍ˪æҬΩ"ƬĉÿτŘɼʸКϽъǙԐǷĸ·ԊŐėд',
                                                                            'ɾǒȞΡҘŷúӆőҐ·ȱӷŭӻˆԙ\x85\u0379ѪΦҍόöΠϴτγĂϤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȽÔɹē\x98äҽÚ*',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'зżŤƹJϫӾͿȅ҉њhϢƻΗÆԮµɉƴЬǃаqîsJɄдҥ',
                                                                            'ΠϕwĖ;ƣΦUƃÈ˞Ȉϳԧ\x86Ϧˌ.ʆɰǔΑʽķǃʌйǆӚҙ',
                                                                            'ѶƶHWΗҺ\x9bˤŹΌʹѡѤƽĺѧˉBӅĮʠњīѻΫΠӗΆљσ',
                                                                            'ӏÄхƪʍɯſʦɄÍͰĆӀ.эƇҋǬǀϭѬǮȽПӀіԗȞӴ˶',
                                                                            'ǲôĂоĐϐ)˝)\x9dΠʑ8ˠĝØͱIȾҰěķɴÖŗ\x84ŔðЊʃ',
                                                                            '0ϩ°ǈϝƾǭ\x8eǼĆϪȨͿÃĎҷˇjÊԠț\x9cX˔ӑɕ\x9aѳ˄\u0378',
                                                                            'ԙÝƹņэ˴ɻС\xadɚ5λsɀƴ҆Ŕĝφ˴\u0382àţ҆ʣľǻʒŗԭ',
                                                                            'ŊϤκіϿԥƔëӮńӽķŷ/ˋȸźљϞѾ˕ұҎȨŮɄĳˣŵ®',
                                                                            'ӛϐŨ˩ΚҊӾЖŐλĴǛāÊӱőąȍЀȿʿķӲͷãж˛Ԥеο',
                                                                            ']§Å´ƲԩԊѮ¦Ѕ<Ϳ\x89ʷȢҀǗȀǦ˪үƽūąǾЦОГĚƦ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѕЧÆɞÒǖņȂÊÕҢϘK˩˟ԑůҮ\\˃ӍӚ\x9eԊҌɅΧѤaÙ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x94˜ÆΣ\xa0ǴÑҴԃӝĈőEơʛһčκĦϔƵƮэƨŻыɵҕ·Ɇ',
                                                                            'ϊÛőԚɵğЋ˭ΧțԜàʚˈԇJ0Ѩ\\ԧҐįԀǤϸöΠľ˃Ԯ',
                                                                            'ĈӓͷúΗϬѱŸϺɌʠLǒԕʽȩѹͲʗCӽƥЊѹ\x81èѾлɢъ',
                                                                            'јϞÏЦљåȰϲǪϴìpð\u038dáϤʶ"ĠӼԚɵФȈͱżʬȟτѪ',
                                                                            'ΨǉÏɐЎϮϵĖāxΕʞǎśЕѽȽÃXҤ¨ИČҝƲЮʁɪӴЂ',
                                                                            'ɝʚvы½ͳ˼ĚËұΫʌēԉԬǃƨĆԐÛϫѨфʌńӈΑĝ\u03a2å',
                                                                            'ӝϬʢ͵ӈƟϮŀA\x98ɾϔˀȑƼқԁɟç\x85κŇĤĬ`ʑɘņȽŶ',
                                                                            'ѯɐȊυ˘ы\u03a2ԚȔEʥzțѸɌЩéыϧ˭˴ǠКĶÀөѺʡҫѤ',
                                                                            'ǓÅlɣĽѰĒ\x87ʒˑӉԫӚƣŤԡѓХĒʨ œĐŵn×ӑӀ\x9fɚ',
                                                                            'іőǐǰŌƍQI-ƖӸӴǪɀRџҳмԊӅŷȖтǪʞϷǊȪìԤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Mж\x9bϻσŢ\x88қþΛ˝ԉ˘ƍͲҀӾʲʿӣʟЫÇѤԉȝҷ˶Îœ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165045.837918:+0000',
                                                                            '20210212:165045.837939:+0000',
                                                                            '20210212:165045.837948:+0000',
                                                                            '20210212:165045.837955:+0000',
                                                                            '20210212:165045.837961:+0000',
                                                                            '20210212:165045.837968:+0000',
                                                                            '20210212:165045.837974:+0000',
                                                                            '20210212:165045.837980:+0000',
                                                                            '20210212:165045.837986:+0000',
                                                                            '20210212:165045.837992:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǩŦ˶εӮǄȜȩ˗рIðųӕȼĦґ¥\x9e\x9fϱёFЬûĸΩЫþȨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.838325:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԝčҿҽͻͱŜϠǭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 152165.91175659467,
                                                    },
                                    },
                            {
                                        'name': 'ʕǍ\u03a2ӾΝʂ[\x89Ԇ5χќǕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ӷ˳χðŏƲΫЁŴϻʗ˦ɪȚ\x88ɢΚˠɹɤȷ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.838695:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȦεƠʈ\x82ɘHʍй4ӯĲΆӠџ\x92$Ð',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 830806.3685912151,
                                                    },
                                    },
                            {
                                        'name': 'ïǂύÛƴ©Ї',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ġǯ¥G¸ˇȷƟҙѥɗǧϽÜĖԀӚҊӤԭς½Ѱ҉˾ϐɨʆ´ԑ',
                    'message': 'ȚԕǮǢˌϢŦ\x9e˥ɆřǳǞ°ΖɜӄwůҪЭЏȎͱŎ\x9fό)ԙª',
                    'arguments': [
                            {
                                        'name': 'ȗƿЧ\x86ЮÃϺSΫʞԀďԓƒΨѨ\x90ԉȢɃ9ҥҽoԌƙԂΞмɉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.839327:+0000',
                                                    },
                                    },
                            {
                                        'name': 'γș7Ш',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĈˢˊԇÚЛлʾȆ\x8aΔŦǲ˩!ć;ӅP\x83\x81)ўȪ\x89Қçҕ\x88',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8083516729555706163,
                                                                            5909655939279039456,
                                                                            398427038520454829,
                                                                            8439980178861791253,
                                                                            1341182432271111290,
                                                                            6633096143242424865,
                                                                            7891258644282095742,
                                                                            6282700252400082921,
                                                                            -6182772985657475908,
                                                                            5540457926980806554,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǞҼϣһҒћ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 271260.0461273344,
                                                    },
                                    },
                            {
                                        'name': 'ϫȭM\x9b˯ƝÍ¯ҥɄӈˌ˥єԆѾɇăȳĘųƨŴŎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            445136.7836547154,
                                                                            333112.7460709054,
                                                                            872798.6572480071,
                                                                            -45075.6263625885,
                                                                            119685.31482770684,
                                                                            26315.220540484734,
                                                                            627865.4983375192,
                                                                            338346.1468143324,
                                                                            98867.56075078412,
                                                                            107135.37037271212,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϿҕӺŞlнʟЌȋĜƅʛΡіlɚзӁl',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ɥɤ;\x91Ϯ'ˆɗnУÙ\xa0ҦĄɤŉˌӇ҅Ϧ\x8fĴѰʞӵɢžƌѲː",
                                                                            'ѓȕąɜçÐƠѬÓԕʮԃǁҀȶҁ^ăʊEiФȊ\x94оµҋʜχť',
                                                                            'ˤӺ¶ËҴӠЅЏȓҿʴԐřȽÂәɪ˂ȩ9\u038b;ӥ\u038dąӾѠεĿʼ',
                                                                            'ı˖ӛƥŦŪʨ˽Ѕ]ӏγЕɰʫƸϲѸˁȤ}ʼƬϐ¢ΰю˚ʍш',
                                                                            '+ưϭÉ}ҕ\u0379ȏԣľ\x87Ǻ˫ƓϛǭʁəɮҲȫÝ҈\x90\x9dϽȿT\u0378Ǫ',
                                                                            'ͼğ/ҙǶΫɑʨŪ҇ӜtƺԧǠ~ҙӸӏɄӟҾǪÞѽƳĤ¦δĆ',
                                                                            'ǐЩʴ\x83pҞɝȡ6ʢӇ®ӳòԠǒɟпөϮĢ\x80θχԣÖӭȻêǙ',
                                                                            'Д˞ӟ˕ΥԠѮƥƛǈČȄәÆϢʝϣƢ\u03a2Җ҈ΊǬŅӽǒǈΞ*ĺ',
                                                                            'Ƌ˴ʬȹ×ήΒӰԣó҉ɊѶϏˁŰʵƴ×˄ŤӤȲӚҘğCјǢŢ',
                                                                            '҅ƹɟцѪʛЗҵӅɛԎӵ҇ѩѐ4ʴӌ:ÞȼЖťҏѵUѱbĘ¸',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʹ2Ȥ˴ӀгпƹØˤԛʈҠɁˊ#фЦBȱ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7453919643717111976,
                                                    },
                                    },
                            {
                                        'name': '\x9aɊŜŰòҰɇʳɓЛЅ\x9fӀ˄',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ͶÿŸ·ҡʶ˚ƔȵǚuǷ˵ΕțςȹŋłȳҘɃɹеӑɂʏ\x9dʏ͵',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "łҏЮжÌѿȶʛ'ʚǪ˝9ц«ϽӻȱϺ\xadΝЩʡӠyèĭҗƭӘ",
                                                    },
                                    },
                            {
                                        'name': 'ƭ-ʕˋˤ?!ˏĴýŗϓ˖>ǪХƸ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȩɋ҄áҼƅˏ¨ȓβʖГʕǖĖӅǢԊɉςЕЇԈŌ\u038bŪĬ<!Ӎ',
                                                                            'ǁŵóȼJoΥt§џoѹÄ\u0382ʕȖĵqͽ˽іȐŋÕɂȁʝЫË¦',
                                                                            '˴\x90Ůӓɑ½Ėҟԅ>Ά¿ϦњʙӈШϒ҆Гӻĺʻԑ¾ǙτýѢɱ',
                                                                            'ӖǀФŦϷʝŞӂ"ĺԦ^ӕÂʹiφʨέӝ˷ϯҩѴҡð,ʇͽ\x9d',
                                                                            'ѭ>Ї˨ǏȦ˻ДƀůńͺˍŲ©FϞĉϢŻɡǚʖľ\x94ʡú˃Aӿ',
                                                                            'ʪŎԠш\x85ѽӌΒˊ\u038bΆǉтʋǒԮŽɋMúɔ4×ЌƤΎĬԭϋԬ',
                                                                            'ƙѪŷİ\xadӼ¶ɷϘҮӊȵǐҙɂÐQʫҜěǙԭѽԟ˒ԄùÕ\x8dĝ',
                                                                            'ҰьwȞ#\x84˽¶ФűȢϳЊ¸ӊ˥ʢžɪӸưŜщ«їϬԤжʾĆ',
                                                                            '\x86\u0381\x806ѽΏ%Ȭ7§ˤƗv˱бħŞԌ˶ƗĘƅѡζ>Ƚɂġΐˎ',
                                                                            'ҨªȺԒǐ΄ԑΎȚғΨľÛȾҔ»čȲϛÂȧɁɀәȆʃąШДƹ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȕȦȇȉũѻċYǈѱ˱˽ŦэĭǾƂѺʅˀϡӭΟ5ÛΆͷƣŞÅ',
                    'message': 'ϝȐ˾ċԋ¯χŴпƗΪϻŵԓĬԊîƍƳњŶЉИқlĝŧӦå\x91',
                    'arguments': [
                            {
                                        'name': 'ǷΌƶ΅ˍăӏǛęƱҲɮКl¼',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ŭƛƪϦїѴŰĜΕ˞ЦͿЭƃӟύǳӪ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԠǳǚҴ:Ʋ˻qÐśœϬ˪ҏòѕƴGԉĚTҏЊӝȂӨʦԗȼɈ',
                                                                            'Ί^ϹǽeԍɥęϵˌҀōξԔ7ȇy\x9b5·ʈԕ˩ѥеҌƐÿ˗³',
                                                                            'ӜϕƨԅϜőΆĺĭʝјȩʺ%\x7fȟʰлˀǊѯԪåТίЈϹ?ĳɀ',
                                                                            'ыƴÁЖŝѧˤӉǌ˪ĻˏŕȶͿΩğϬЬ͵ҟOɊϺɑpϼkVϱ',
                                                                            'OȆÀɟǋĂJǠЏϤӝҗҥˎŢРЏͿĐɱқȉЉӋ\x97FƌÅʖĦ',
                                                                            'ķ@ѦʯçжĩҲÒ>уʽΘ6а»ϽʬԒԠȎһ\x81*Х҄Ƚͻӷ®',
                                                                            'ȻьǇѭŦÕʧЉɕˁżíϛҁюɅȫҏӯҬτҤʡҹά/иĚЯˆ',
                                                                            'ҋüǰԂɘʦϧ\x81ɂšХtīÍόηøԥþĜқҨǥǴ Ͽҙүϝǻ',
                                                                            '0ӽчǖʽѼԊԖ\x9fѿҕј}θ1ǧÜÑƻǅ\x83qԮ˴ŉӷȋǤŤǭ',
                                                                            'ƟϒǻкұϹƌŀȃϗӍdӏԏΛЭ8ɔҬɘҙɗčԭƩƙ®ʛȎī',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'бӼƱŶЂĆ\x96ȴMУįʋƝö',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 844075.089727282,
                                                    },
                                    },
                            {
                                        'name': 'Ǒ˥Ƀ˞\u0379ǙԣϣƳǶΚҀҟόʢʏш',
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
                                        'name': 'ԑǼЄ/ȪҬpӼЭ˘˙ÛɡƎĭЯ×˶͵дϏɲñӏǾČИМ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.842567:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x8bԀʽΟɦӡ\u0379ŊԡϞΣʉƖɄʖƕ¿ʹέϦ\u0383\x91əσҬsЮǮɔв',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.842897:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƽйΗԅĢ˒ϖʔε%Ш¤ˀ͵ĘњΥ\u0379ȠͶNƳ˔΅ ·ʂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4920857473873329957,
                                                                            -37359135093170298,
                                                                            -1314945002090016418,
                                                                            -5470903040896183547,
                                                                            552332621386743167,
                                                                            3678215604244081659,
                                                                            4992984368376150826,
                                                                            -311742034270128982,
                                                                            7514246162501439872,
                                                                            -8045394152765421361,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƓЂ\x95ʛѴϦДâҶԘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.843595:+0000',
                                                    },
                                    },
                            {
                                        'name': 'íеśГðзǟВΎ°ѫӶʇұIʼ˖ϒҁ0ùτáˍԫōȃ¸Эō',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2120330129322415530,
                                                                            980306457733592902,
                                                                            -2219953870781468779,
                                                                            1919469664362275681,
                                                                            -5053968097321879542,
                                                                            -3752360579366223811,
                                                                            7148754804477357394,
                                                                            -5478292897763951921,
                                                                            -3656537166001167402,
                                                                            5256068911154090337,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϒƗӷƓɓĖǭhаƝЮÎǡĐʏϚҵĴ}ї;ѫўʊԂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            606758.9037561691,
                                                                            -60903.83147141433,
                                                                            129336.16408621342,
                                                                            276265.44861611334,
                                                                            182654.77143478446,
                                                                            540701.3405391558,
                                                                            6721.53348403261,
                                                                            452204.3141412039,
                                                                            350748.0799468729,
                                                                            913165.8999554536,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˌδϋеŝЅӒ\x8eӓjŎԦÅԥ\x9aͼĺҩԚǪŃҐɹɜơʘá˴Ϙϻ',
                    'message': 'Ҏ²~ɋ·ĀËʯ˚ƈͱӔƷʁÎѦ\x95ȓӌĮӑƉИʂ˞ԫӌϵɛЭ',
                    'arguments': [
                            {
                                        'name': '¦ƸϞЛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1259345050194052867,
                                                                            -4671615742099666907,
                                                                            -2375043665965451523,
                                                                            466252169278680564,
                                                                            -8982986767893061353,
                                                                            -2168791978417296075,
                                                                            681636463203036691,
                                                                            -213284280214869122,
                                                                            -483536265187733004,
                                                                            -5534363800540539429,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'áΥ;ʩǼΤĆюŇ˙џφŷЬʜĵ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƐɃӖÿ˪ӽ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'єʐʯǃ*ѧ˅ѽɞĮȷΩϝ˾ɔʼԈΤτâǺ\u0378ԕȖӞiоȘǬЭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.846451:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӧǭǍȦε˽љѵŌЈόł©с¿Ǵ\x98Ƌš\u038dòţÈ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.846677:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӊ˅',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7788842707478199610,
                                                    },
                                    },
                            {
                                        'name': 'ʄƨŇËˣťȷ˵ąҨ»Ĺѵ˓\x8fһǐԓȂɘ7УЙʌʾſԔЉËȥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĄѹŷУԭƠЗԕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -19713206312188624,
                                                                            715275688518136493,
                                                                            -3695679149228437611,
                                                                            3128240203874681997,
                                                                            -4040152588097139844,
                                                                            2325447866560662280,
                                                                            -1080078147495523376,
                                                                            -6738256880769656626,
                                                                            -7413597334778319434,
                                                                            -4910961183283757565,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'όΊÓņþy˕\x90ŽѫԢšŌŎԊфɂ\x8eǽΚǄωѳÊςʢȶtŰî',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԭĐȶÔw\x89ӂӋͻҭϵ͵\x9c;ҹľ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3137108100342388292,
                                                                            5847067353933994499,
                                                                            -4380006521263463738,
                                                                            -3517810936266719461,
                                                                            -3777350976277964535,
                                                                            -6724947218482307300,
                                                                            8449955070665248076,
                                                                            2417166916691947026,
                                                                            1110866705381434667,
                                                                            -136116371368704667,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'àŚфɰˏпĩρӆѳJºƔƐĸç,ӐҬƶɘÓӥʄʹȏӹҴ˵з',
                    'message': 'ϥБѕǀCЎԕĘΛƼºėƟƣʄΛɇύʍŏԣҫӎƳıȊơԠҘù',
                    'arguments': [
                            {
                                        'name': 'ҾҏӞθҴТȄ\x8cҌ<ƁœʞѡGӑ3vĲҳҨʫǧrҢ"ϢɇΠʦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.848490:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʗQӈđ×Ę',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.848692:+0000',
                                                    },
                                    },
                            {
                                        'name': '!ʅˤɋ¨ΐҏŏƖˈưԆѴsħvćӷбӳŰʃиɷŶɡġɰ\xa0ˡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.849001:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ČϽ¨ϣӔ¶ÆȆНÃɿ~ǝСυºgĝӺlΘǞ9ǧʷǠҵJǘʣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8511793056004250909,
                                                    },
                                    },
                            {
                                        'name': 'ήŴӧʀюмђҖɈ˹ʅ;MƫĠĪʚЖԞ\x97',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.849405:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӯ\x84ͳõɾӽǳŐū_¬҆ΡБµɕ˪òʿŕɜɰ)Εɒџǻ\x9ce˨',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ľ8ԜΔĶѳҘƼҲǎʿĴȶЄHĉʇӹΘӽϞǐG˞ϽˁÿѷȉԄ',
                                                    },
                                    },
                            {
                                        'name': "6H¶ϛ\x97õϋ'ȸRɪԁҟˮϛˆϑʦ³Сӭ~ŪǦ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1496381942230900013,
                                                                            -205764396320030304,
                                                                            2244592035868508102,
                                                                            7802519603131492153,
                                                                            -6010720902372001239,
                                                                            -5078200823361308643,
                                                                            -3126237491902276327,
                                                                            -7103954547702796605,
                                                                            4582632190855820199,
                                                                            -1842831936608643598,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ҒŸRɗҲʷӝҳѻɁFϪн'ƳȜЦȎ˱\u03a2ǿϮ\u038bɸɭɲöԙОú",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ŀ(ʴˌŽ\x8fʇŊҠҾ³άıƭΑƳ˖ūҔӗʈ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӕ˻|ɢҕиqí˟ӹȄԭ˗ƒПѴƜЅ\x81ǽоȇ¯ϣVǨƬύ˷ĳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5872976812564288273,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƢʻƩөǿҗÙ҂ԦԨ4ʡμќȼ\x8eԞ\x8dĝŹý˼чѻ΅îǣ˱ŰО',
                    'message': 'ϺφѝΚїŢE:\x85ùΈôȄʬтΡƜҖкƼɛ,҄ǘͺқļ\u0383ѡǖ',
                    'arguments': [
                            {
                                        'name': "ˊ\x9eʸŀřČ˹řÖǀҊΏľư*ґϱЗȧŁѳǙȠзѫӺ'Ѳ\x87",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            210705.44957882736,
                                                                            893982.8266137107,
                                                                            82550.00161588477,
                                                                            34209.600220038614,
                                                                            552775.531637815,
                                                                            857274.142441428,
                                                                            676693.7607949248,
                                                                            442200.09991772147,
                                                                            369103.5039262292,
                                                                            386706.6670055099,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʽöх\x95˂ǉǒʬɫɣȒĕKфҜʻȌʤˀĈŰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÑаɌāЁҼǊԋȜҧEԘõԐ{҆SυԣҫƎÒƳѵ˸ǃьϴɦǐ',
                                                    },
                                    },
                            {
                                        'name': 'ȏӰ}',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2074846339205068826,
                                                                            -7212437464807081997,
                                                                            -3078589935265439881,
                                                                            2239876937223523104,
                                                                            676607065017441840,
                                                                            -4103793767056532784,
                                                                            386299094047183056,
                                                                            -407694402192173707,
                                                                            -1053515123645894908,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '΅ŌŢ^ӜѴԋˏ¹Ӄ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1326150797791761342,
                                                                            -2745791566409087309,
                                                                            -7410171311796987545,
                                                                            -3615491717151308523,
                                                                            1756615810799019716,
                                                                            -7985412938968013354,
                                                                            4142060389883798560,
                                                                            -6773406687995349215,
                                                                            -7306077029545973198,
                                                                            -7089000407574742195,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӄҘωǃĊtԑϊ$ΟαЏԩϤАΡʲʗдӳ˛Ě§Ư&ĊѢ˓ԔɌ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 980642.8280359283,
                                                    },
                                    },
                            {
                                        'name': 'ɶʠԃЊʹʫŀĆʘɦԣӯŭиУMĈ=ǢƣéȡȉӪ˦τ\x95ѩ$ξ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '&ΖнӀӊӦbŅ˦РЉ\x86įҡµνı΅ɮ9ȩƊʔ8ƗŪʬӉуϓ',
                                                    },
                                    },
                            {
                                        'name': 'ͳ!ˊʺ1ӋȄïǀѣͿ\x92ԑϮЯҀҕđ˴ԫӪζϪοϓɃʽʠƟϯ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5785248929041935343,
                                                                            6833037344785022562,
                                                                            1245127752464936005,
                                                                            1650266003877169725,
                                                                            667929353955961621,
                                                                            -9099670300513220514,
                                                                            -6940809784658781509,
                                                                            -6197125636034018855,
                                                                            -6094928611358761192,
                                                                            511051816210996091,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʥ%ãӘч\x8aĭϦ˒ӡҽ\x9eΧҼKҀǤΏϗˏɭҞǅ9ϭӒ÷ӹeǫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165045.852241:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÉɵƧȞŪßˍӊʦяİѭǌŎ҄ЌΫȸЌЍ҂гъαҸȿѺκιw',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            472983.1218145158,
                                                                            120287.30341406219,
                                                                            852702.9853777479,
                                                                            737147.5009431173,
                                                                            -26074.997505449122,
                                                                            944351.3073992752,
                                                                            616181.9453201061,
                                                                            947085.8425624393,
                                                                            728465.9839459637,
                                                                            361234.2508655984,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¬ƅúƹЇаәȢʿƍŧӹŞ¦ʪƵ\u0379ƚЎːķΕʄé\x7fџҵӢȅŁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
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

            'identifier': 'ƳŜʢlȃ',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'ȥѓ',
                    'message': 'Ŕ',
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
            'name': 'ҮʀĳҦŠȗÃȿ϶ҹQOǫǔ\x85ĸϣɱǩʐхȵȥȝԈȧ>yƱ˝',
            'error': {
                'identifier': 'ȷŅ˒ИяѥҼӦȩҔїуӃȶӽӼtęǟƴ΅ƣƯɭː\x95ԙϟȽ@',
                'categories': [
                    'os',
                    'os',
                    'file',
                    'configuration',
                    'configuration',
                    'network',
                    'network',
                    'internal',
                    'file',
                ],
                'source': 'qƛϜƓϪFÂҡnǵǭĈɪɑʣхëɱӺ-ƍʽ(ŽơҰȒјџŠ',
                'messages': [
                    {
                            'catalog': 'ƒϿɽŲԗɃԭрĀȌ´ȌɀĈϏҧȒϮѷоΘʽμнǼȦªǋǎ\x89',
                            'message': 'ŧMӽƱԤ϶ѤɷԩΞԂÞͲʵ˦ŕšтқ҈ÇԡɼӧԐqӴЙÕŗ',
                            'arguments': [
                                        {
                                                        'name': 'ñӫХƭƥƺЕüŦɈ³˦ŽѦǮѿʾƅʘМʦӣӣ˹ƌʏ Πëι',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5486220874896658764,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԊӜԮʲʹϛϗƠMʖƷǘȪҚuēÿĬʔlЀʬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸӪȠ:˅ƆпʬƢƱΟŰԞʜИԝgτŤ\x8aɃȎɫǢőɔį',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʫÕĚԗӌѓšβ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9197949801872666381,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇԛmУΐÕÊѱϲǄȀҌӗԐӵҿ_Ҝ\u0380ȴΗĻ\x9e\x83C[Ķɞ҃Ǽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÕӣëÕɌŕǬӜƔ¤ǟŤəİҍо',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x82ɨʜ!ʅFεÊɅϲӯȶԞ$pŁӤСñ͵ʈɞ\x8c\x9d1ζɵ\x92Ɂ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 51300.60184532654,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϏαϷЗϪrŘ\x80ɕϬƖƶ҃Ї]ИϨǙOΨʋŧлфĬˇ\x9c',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҷѧǎîȏ%k',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÈȲÀϹЇȰҬƹĲɐǅˠĿΠHȉЧҲɗƘȌҜӴϱеōЋΟ˻Ƚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x88ċѝƌӵϛˈýѭЕџѬԫЍ\u0381ʻҀƑqRҷІɚϣyǪʈԟΧ˖',
                            'message': 'ȿȷ×ƀϟ·{ϬƦǍġɥƁʈǼyÚɈϝУ_ǉ8ͶµŞѾàӔƙ',
                            'arguments': [
                                        {
                                                        'name': 'ƲɎέɃlԒƤӜ˪ԢύӛҎ\u038dǇæ\x96ɧЭȩ;ӚͱƟΠʵŔȢ\u03a2y',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʃΧǬĥå`ӤʛĨG',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'đƎюђϺѬʼɑγĖӇԛ\x8eʵVɘĭƋýя×θѽÓvʒϚŰʻô',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӍɄʐńǗ҈ɜɳЅŕΪɩԗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѡȺК>wЀĥŰʷțōÀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐαρ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϻɽδЏҿӤ1nƀ\x8fĦŮϵŝȚ½\\ȋѕÁ3KƊӆȸϯͽ`ѤҚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʼԟҷłĠʒĺԃѱəʎïʑ"ȀΆƅÊȥ±Ǵϋʈ˕ƺӫĆѯіҼ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǜ˻ųԨŝĪͻҭįYɳȹɣʕȠҬȘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҁǏ˓©O<<ˆˎЮÔŨ|ˤ2ʐѭ\x8aϠοƲʁҖɤԫʾͻǶьӀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 291777.89958771545,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƍԀϐǼŏʛɻ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҉Ɍҝvјʄ˽ŧ]łʄ\x8eʹ˭ҳ\x83Q˃іҿԦʕPΥbʹϘȬ\xa0ǹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȭѫºҍėːӅΥ÷MѲчǓƸϮѠÎbɗWȔɟОñжΧʳ\x93ơƱ',
                            'message': 'ΊΑºĔȇ6ӅԚǍΒӷɖ\x8eèǂ˭ʮє϶ʝԛʘǕχƱИйţҡǝ',
                            'arguments': [
                                        {
                                                        'name': 'ǫǎͶǵЍǓ¯҅ѕ0ҝjǺЄҲɞϏЗƋɏӋȂϺͽ\x9eӎ9Ζʦ\u0378',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɔȋyφ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2218661360101527607,
                                                                        },
                                                    },
                                        {
                                                        'name': '¡өΏ¥ƽÿΕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ˍȖȚˁƸʮĵǎЗȕΗĩϒͱΕθƉӷ\xa0ҧ;ӥˊͽ¢pЇȫ'ɜ",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7633595096858191172,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӣˊ\x93¾vӫϣӆ7ϑρA\x8dԬ\x92Ҍ3Ѫο_®ҽƵΒι\x83ӥƩȯζ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӪƯ¢ï`ʴŢȺʑ=ʺƸѱƏʔ7ɪπАΟ\x94ȀҏєÔσ¶\u0378õǣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7522858936499425077,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĎϜȼѶȮԐȞεɂ˚\u03a2ĘƵԦ҇Ǚ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÓÙÕàʙѥǏȩƒͻЯҴӋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7236333598258546130,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϮǆџБʗŦΚɘɑȥʕϺɝƺ|ԫ\u03a2ͶÃʴϺӸȆɝԀΒ"ΚǠѭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÔԈçЪ˘ȓ˓ɔϲ˗ӗ˪ɏѭŅКɈϭŻЏǀÛĩˈŖԎӨ˗Çе',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ξʱ\u0381ɓsҷ',
                            'message': 'ΤFŀâoȋρƖмԭ\x8cʞģʪԝ˵»ӒȐ\x85ñǷāřԃɥUӡΟˡ',
                            'arguments': [
                                        {
                                                        'name': 'РĎѬǐČȹ6',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˬǦѐʑʮ\x80Ѽ˶',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165045.816521:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Òlӕ\x81Üѹѡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5405400999944564843,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ýʹ˽ͲѿyŲҖÇŦϑϸΆȈѭϊŷɠdɢǊPԫ\x9bČ\x85\x9f¶\x95ê',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ėЁNѐ(NѨʬρæѵÒǅ\u0380άӦɶäƼĝɩǃʨÜϪҜʻĬǀŞ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'чåЪҎƬʌɐÊʯлǊ½ȰȴċҶ¨ҧϫЋƎϳɡÈӬҏȽɫҵ\x81',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'έҥ_Ӑ҄ҢK\x86ȋ\x8eĘϐǠǄϽЈҹĚČǙY',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѱɦǣфԤΗƦÿˢĽÜɾȅǌҼ˷ΏЃ\x8cΓĪÐ"ūΌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʵӤį·иӮȯѣіʜӇǗԞϫ(Á¾ȣéw˺ЩˡŚ˭ѓǄȭȓά',
                                                                        },
                                                    },
                                        {
                                                        'name': '΄ЩĺưĉʎÌɿʯ\x8eƞ+\x94϶ʆ҇ʢʱ»ʀȔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'UԄϴԧĿŨΓɼϥȶµ\x86¸Ԍɽƈϲė}ɮ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165045.817629:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÑýT҂',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϒƹƐϕƼ\x91ӬҬΘ0ʭéǻƶΑҕԤιéŻś˖ˬǞšǡЕ˔єȘ',
                            'message': 'ȓ˵Βҟ\x90ӳʲԄŤǐɢʵώњĝəȎѮԘˊĀνĝԗˡǍť\x92Ϙ\x94',
                            'arguments': [
                                        {
                                                        'name': 'ӎНɵз϶´ˤɹʟǟǢϏԁ!ϡҨȰθâӋ˞ѭԩгźē˞ìŉғ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0378Ί2åЍВˍθϦ#аĲĈɑʻѢ˻ԫҜĂϧǮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'êǠȱǦǍn;Ϧ³Җ{\u0378śΩӱȮÑϭӟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЙÃϜШřÅħӐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˹˸ԧʼåϋΜƌö^ӜЏ&ƽԬȳ\\ÚԆÉČĒɲˈɀΨ\x9bþȪԬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'SЁǰɕӾʯσυ:çđòέ˗ӝү1b3ԤˤǨӅlԧʵԩ\x85\x93ј',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2989580113140552397,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʾ˰ҖŵȸŬӖ"ϘǡɍͼɣМϾÎʣ#',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ǫѸ^ҋіӁ'ǕӜȩѦ\xa0ƶ˝ɔcЋц҃\u0380ǊÑȆΰ»ȩŶƖͻҼ",
                            'message': 'ǁԍĶцƦӇӓ]ǹñƖɞ%҉\\ʥВƧˆuƍʨʩ¬[ѽɴźǪŬ',
                            'arguments': [
                                        {
                                                        'name': 'ŹǱŻ$ʥÅӉ\x8eӥϛȰԅңҏϓ˻ȒÃù_',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1040294459786712637,
                                                                        },
                                                    },
                                        {
                                                        'name': "K҆mĮĶÃӖŎΛρөйϔŦ'КѨƃ˲ӏ",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӲĩU\x9eRԒJʇӤӎoΌʆŢɋɻdІӷțJҞҭ˧ŲͺӇ˓ƁƔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԤγЍˤ΄҃ĵȗҔԐɴ˴ť\x8dԖʾßӚѝΎ(ϤЙĴΆвɮƳҷñ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': ']ϓҩē.˾ĉόТÚʪʀĳˠˈĄͻԎȟǴâ\x9bŔĲΰς¥¢zΟ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǴtÙƦХƖҦǬĐѸǱs|ɿа(ÍϻƛЭҿ\x9dŊ\u03a2ǳǼӀºţğ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 13965.693473482606,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ьm\x96ȒӳǏηвsҧìȡ\x93òżĀĖʍʝɉхŘȝԚŉϴŚęɖԭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɨ\x8cԤƀ>ɡҍf϶ύǦÚб\x92\x9bëŻЁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "§ӿмΧvԖӅȜǲ«ǕȫΨƹΗʥÀ˲Ŵ\x9dǅДӍǑɺн'ʸ",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˢәȗϞĘãΉõU˱®?Жө\u0382ӕтȲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165045.820319:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŸӪʹʘƠ¸\x98жϯŷӃɧӡʒ\u03a2',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -51269.05933176622,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Эʶ`ΰkǛEȾǜɿŤͰȝƉRӎОƜʑƇ΅ƙŋȴӳĵ^ĎĂŉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'тŉéђXǓ%',
                            'message': 'ԇҠҳz˕\x82ɌϜɮšÖԣϪɵЕΕӳʧŽǟÔŖFʁǾjҵɳСɲ',
                            'arguments': [
                                        {
                                                        'name': 'РǄ¥ҘȪßǑϻţƛҠŐ÷ɔæπȠԫÀƤԆ$҉\x92',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 70757.216105839,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǔϬ\xad\x8fӗç\x93˨ƥ˪ɰ<ӡӄ{ȁɂΔɳÂӶϋϴ.ϺІɓʿǝѓ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǓçSŨѓӶнҞ¾ʉϵOƹЫӴΎ»Ĭѐ(ȧŌ˲ѤԌɲǰȆӰǉ',
                            'message': 'ŔŖ˛ΏЈȿȷ˦ԇȕіãʾƷͱHΣʷƻԑ\x89ʎhҽоР_ǎĘЂ',
                            'arguments': [
                                        {
                                                        'name': '\x9fѹӠ¯΅ѿǗƅ\x80ʻқÏТȞЯFԦəйôΒaVȳλĭƢƂ4Ŝ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˏǃơɓԁ\x87ǢЦԊ¦ƐƉȥʍԦɴ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǭʸһΝ˻ҎΟŨѯ˃ǑŲĐƜα¿ÄƴƣӐԪΓҶǖɈǁƏʑЎv',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŨþƠҕпQĩÄÝĜтƮǎīцǳ\x99ώѮμÆωӇώэ¹ƌζʙV',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĂӣЩCѿШBčǧϩPĹεϮŝƸkϬ³ōνüϕȼ˺ɟЧ\xadԌѿ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165045.822458:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΙĝϘǛcbԮĊԩƨɝҲåΔǱ\u0378Ъ;ӸÎϩɳ\x93ѹή&IНŠԈ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˵\x89,жȢ6ԆˎžǱӣ\x8fӸϡj$ǡљŮԁϭԎғӧɰижҋǯʟ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԂёȄЇĞţǩӅ΄ͺЗѡ˺Ӥϧ˨Eś\x9eȖŁ5ϻЦŬζԈџtӚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѤɜcÃĔűśкƃӄƈqҮαçĠƹǗә\x9e˞ϏѴʤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x96ҙʭƂʷԓҼӎŉ(ҪǫмÁĠȮӸҎåȻБҥїˇëт%Юɋ¥',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8689262297005351122,
                                                                        },
                                                    },
                                        {
                                                        'name': '˲×ж҄ɱɳÌ˙ƭ\x85ʹȵϬƉиӶXłʹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '{\u038dѷǖ>һϙΈԔ°\u0381ӽǪò4ȉtФ˹çɳ9Γ0˜΅VѻΎԣ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЮëΡ҇\x8fϲʈŭȠɹ\x9fëŎɹ˛ūυҿǗʰҦԉϺêːӤĚǄԠΉ',
                            'message': 'Òɚʌ\x9bˮőϒÁʊºǙËΗјъɛ\x85ZϜЎɠ\u03a2ҮяďǢȔɠaΡ',
                            'arguments': [
                                        {
                                                        'name': 'ѸͽƷπӻϥÛȟҟ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'łŨƃWǊʘԤτǝÏɋȺӤĥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165045.823720:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮφŵȉϝĤƅÍąɢȽȽˊLɩυʢжV=\x85ȸңˁˬɪùѿԓͶ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 847537.4733338504,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾĚǜhʟƬѻYĮȆѷϓʵ\x81Ӗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165045.824010:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'зoÓŀæ\u03a2К\x92ųɒ\x8cǰ#ѥА˸υϚµĽ,Ӆ˘ƆθфǚΓӧɂ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĚǑǞѣӇɧǖϖ_ĺƮĈzʌǩҧ˰˪',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʙơѬюƐӢ¥ǋrԁŇЌѝӘuϝӈŅQʫŧ\x7fҌˣşȗ\x9eԐӐ±',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƄωŦԇΠƉ˰˶JîԬɼʬͳђǊĠǷӷ3ӦйӧĭȳƬҕºϩξ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƓǭɫÓνӛˎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ζӁǦĒġ%@ĪåΣʧҩҶǹТ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˲ԂŖӗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ϟӏ`ƸˠŒƝǪϺҝџЋǇʲ˄ԂŧɡŮǵԮɛʮҍϢјàʩȗһ',
                            'message': 'ǂȤÙΤÇƈ˟8ӮӘ.ʒӣͶѦһüϽѮɬȀӬƜȥȓǗԊǽâw',
                            'arguments': [
                                        {
                                                        'name': 'ɌͿǷОŖȆӁƐěʜԂѵ(\x92ľģ҇ԝɊӉѦӦ;ŤȩÀяĢ˷ѳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϭȱįŽġ\x8bƍѓδӏCҚɇӘϋѬʜ\u0378¾ͼȸΨԑǅɵԁҸϸ˷q',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2851498101801767253,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӜɣԝРӿСȝǌ\u0382ӖɼƏʤǎɎӓμӊɟȬпüăǫԒŧΓйǄǊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʴĠY\x9bˎǿЎŭĔѢљȔAϟҝɒĈȉƙȯƛɠİ)ϜʡуxƽҜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '=ҷïПΓǬǭȉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Aŏę˥Ƚώʬϧ҃²ȼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 409190.49767989136,
                                                                        },
                                                    },
                                        {
                                                        'name': '˂лѨƝÀΩũȶʠϢЛѨ\x9aNˊ˗ԑ˝Ж,ķȂԁcˑ\x88ĖĲŗ\x91',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4774863425896106525,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЫΫԕMΐEǕɍ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄èΡͺԖ˭ю=Ў˦Š˘Ҵˢɔ»ɷī\u038dӝқŐԨϫԧŖПĻ\xa0ѕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǩg',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
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

            'name': 'ϊɫċ',

            'error': {
                'identifier': 'ԚβȚäʿ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ҸΡ',
                            'message': 'І',
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
            'event_id': 'ɓƠǶt˄ʯ˙ȣӂΘƷʯǷτŬȃĖ˨϶ȞȩԕȭǥǟѳŁʟϮɭ',
            'target_id': 'қōʛ£ãȱŊĺӎȋȗҏɯɎȅѱӒƷцͿȅҽϑɑЬӦϝƂɹʳ',
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
                    'event_id': 'ӵѶϮʿϟ\x8c°»ʰƍŵʙĢеGȎȅͻԋćԡ˧ϝ(Rә+Ҩǳԓ',
                    'target_id': 'ѺϋĆҎƣӵ½ΗŮκʗЁɆѡȾ˅ɇĄεϰԗɋх˯æ©ΡǯƛͶ',
                },
                {
                    'event_id': 'ɆɗјӊǎӟЀˋŊԐ҈ǱɋȣϐÎʹřϥӮŇаМŧǙѹв©ҹѽ',
                    'target_id': 'zΦƜϛ¸ɌǨǔРѭʓŊʛʏԮѵŽѵӚѮǒǠJҏА·WѠԫȦ',
                },
                {
                    'event_id': '˽ɹΔķѤŮʈǊ¶\u0381ҳ5ōѠт¥УөƷɖηˮʾĂҲ!ɛ?пϫ',
                    'target_id': 'ӤӍĜĠIӂűÎѕ%ȠӻǐĬÙбĵʻǵƆ³ԫ\x9e\u0381ĩǥǌǉѼҚ',
                },
                {
                    'event_id': '˴#ŶмУɌǊǘŝøσΘЀȔǫќ#/:ΝþΊѭӰɮұҲШӂԙ',
                    'target_id': 'l\x9fлȠˬλċȰțƹЃ˴ɚǼł \x97ԫɐҝԘʝΫÆĴǹϫƺǾ\u0378',
                },
                {
                    'event_id': 'ĵžҐáǆɸ{ČĨϼìϿ\x9cфɄϙňơšŜǴԥђƲbӅӯƙԃƉ',
                    'target_id': 'θϡıɊȻŀĕ¹ҏʌΚαЪәЋˏԍʜϛɓǜȉǔŧɼŕZǹūŶ',
                },
                {
                    'event_id': 'ƈдӿ\x93ђӡԓԝҋƆțİe¸ȜþİĳӷȜūģԕĄБǦӑжȆԧ',
                    'target_id': 'ɊǯΟġťϝЁϚӃҸĠʕљӕԡӥȊʺҷȮʔўǫf˹Ǜęӓ˥Å',
                },
                {
                    'event_id': 'ͽΥѼВʌȴ¸¨ʚϴĆňϦӐыƖɡÂǫQρӚҸǄƘΙѬÌ»Ŋ',
                    'target_id': 'λӷΙŝÃʾ>ÃĮȄ\u038bĩЎ\u0380ВâʔЖΨϓųþȬǽêțųÌԏŪ',
                },
                {
                    'event_id': 'ΓԩȂѕˡΥʏɲϠx\x9aѴǉˌΗȺ¨ɁЂOƹďĳÓ\x88TŌɈùВ',
                    'target_id': 'ǞɷŜģңɳĔ˔҃`ѩч)ʼϵѶ˄ҴˇƮӬɍǉΐԂƺǭjƂv',
                },
                {
                    'event_id': 'Şʻɻɻɒ˂ͲΑuǰO.ĲЎä˜ΟϕʐЏʒʟΪƓФǂˇԍϱǰ',
                    'target_id': 'нЪѫ˖ɺİћȍ5ɇɥӷҨG˗Ĥϴ˦ϱѾǨŜʟǑʃǘ;ӅȮʰ',
                },
                {
                    'event_id': 'ϻЍǺє˂ɨu˟ʣ»',
                    'target_id': 'ЊϑϪΦӱ\xadɩɁӟ¼žŏǣЌƭǮǤÞˣ·ʸϯ˨ǮѩΨқӏϪҠ',
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
                    'event_id': 'ǜʖҺ\x85Jѥ˜ò˫ȯĳŤɪΧӆϡńԫѬɰǁˇ_˞њƱƿ˧Οԟ',
                    'target_id': 'ʅΒƴӎɋ\u0378ūǥņÙ\x8fňЛϡЬ΄όΤȫ\u0382ǾģƵǌʭɜϬùŉϊ',
                },
                {
                    'event_id': 'ѲVǵ_ζӬʎƟ\x8bΩŹȢŧʣƦ¥ͳƵДȀ҈ӬѦΩÜ\x95',
                    'target_id': 'ШʌХċɉʱʌԕNǷùҪҸԎ7ŝ',
                },
                {
                    'event_id': 'ӪnʱǐҋǢӀMԠĻЙ˸ѿȚǤОɽƣӂʂɑЌMҴҝǴѓôʫ4',
                    'target_id': 'ň҃}ǃʰȩʱyҩҡƾǉұȭȯ~ɫЯѷјʲ\x80˗вήÜӋԊԡŶ',
                },
                {
                    'event_id': 'ƔіķŕϨʏЅϴԮҗƀŐԎȷĖѦȆʊƱǹƠǃʐԊ˘ŵʄ¸ˀӯ',
                    'target_id': 'ìѧΙҚůªά^ΚԖŦȚϩ*RgĴ˴A҈ðɬʲƒˬŤ¸ԠΘŠ',
                },
                {
                    'event_id': 'ɑѡΓÿϤȺĬãΜƜь?ͰTɐVÞԗԧɰȺУĮˈїȖɟȯ«',
                    'target_id': 'HЧҳȑŏɅӐɱŨBɮԎƇ«ɒ\x7fн:ӊɴìfŘíӥȞʉȆΣх',
                },
                {
                    'event_id': 'łçɣθu˃ӟțȱŭǚĘòøѕ\\ǱǄЮčŨZƢʬПϐΗ±ɦΆ',
                    'target_id': '<Ϭ˚·ӰςŜӫ\x81țȸԞԑ\u038dаĥɋƣ7Ϯ˹ȍʙȽԑώˮ',
                },
                {
                    'event_id': 'ͱǽшǋœȔРʨƜεèҐһвȇǧЌɍǞϠıņɪą˹āãҾϠˀ',
                    'target_id': 'ėğґĳԜȆӔς˵ɗȈİĺƐƚӯĐwȯǶνϗѵϹӿʒфĞɵӻ',
                },
                {
                    'event_id': 'ŊÛ\x94Ȥơ¤Ԡφƭ¨ÌϔѾŨˤҥȰžӿHǤԅǍŔԠǲʂ¬+˵',
                    'target_id': 'ǟ\x9bЧ¥ţӗǶʚӕZ1\x86{ӮϐÛȲ§?ǡǜ˃ԔĮʤͱΪϢĊʺ',
                },
                {
                    'event_id': '˘ӈǓѨñôÀҪҮπȷ҂ϹŪĜѱȤŰӬĭԒØͲɚӳͳһ˾ʈʍ',
                    'target_id': 'ȺέɌҎĿҀɍ½ҒέҲɇ\x81ȏ¸Ιē´ӋϠÍϛǑ\x98ıɉpˬʈ˾',
                },
                {
                    'event_id': 'ЩkӨѼϙPǨыåԟΦԭԀвҺƶȖѫ\x96ȁ\u0378ÀÍćϺĨ\x8bЛӁ6',
                    'target_id': 'Sϓɖ˜ǮӋʍНGŏ?ҜŹԒϞҽǧÕӱŰѸɎϖԈӴІÆӪŊ҅',
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
