# GENERATED CODE - DO NOT MODIFY

"""
Tests for the file_logger module.
Extension petronia_core.file_logger, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import file_logger


class LogfileSettingsTest(unittest.TestCase):
    """
    Tests for LogfileSettings
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOGFILE_SETTINGS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = file_logger.LogfileSettings.parse_data(test_data)
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
        for test_name, test_data in LOGFILE_SETTINGS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = file_logger.LogfileSettings.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOGFILE_SETTINGS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='filename', name='LogfileSettings'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message_format', name='LogfileSettings'),
            ),

        ),
    ),

]


LOGFILE_SETTINGS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'filename': 'ѮȠӨĜɆ\x9a˃ҸƙΏȴʓӥΥҐϳȬԧѪѕȻдʎӮȰ˸ǆѬtΠ',
            'message_format': 'ĺęPɮѐPȚſʛŕÉɌӚҞѮÑжϖÀȗѿƱȮʬʦӥϯѣɨ©',
            'categories': [
                'cԘѹϚçЉϱǬγϓӕіŐő\x8fɔϾäҪƂīϟоȁѥʡƻnԮΈ',
                'ρǳ\x7fϐǊǰɄНɋȾń;σȦ\x8bΔхӊә®ʯԊ|ʘǾӖӆʨϫ·',
                'ȗJ˗ȂSѬĬёɫѶÐ҉ʒxÂϑЂϼˣ˘¸ļҠΉϺ΅ǟϕ*\x9b',
                'ƂӏȾӕϮˆАτ)ԧŷԃ·бϾǟ¤ɫʁɗłĸҩǚіŻӣɶÜǴ',
                'ԈҦņû˒ґѮŲŒkΓɭñƼϫҺβД˧$Ơ1Ψï¾\u0379άŊ¼ʆ',
                'Ϥq\\ȫ7é#²ɮĩũɡȎ´ɘɪϙɧɔЖͲͷʐԨϫ¤ɇËЧö',
                '·пɷ\u0382˒ɆлЬĀӝЀџĀрҔ\u0379ŤԦʭϖô˯ȥʠΰԐϒɱǨĎ',
                '\x80ЂʸҥƖ«ċˇ˴ѕ˘Çðõƥũχ1ѽͷǅŲŷ\u0383ћĞďтɭɄ',
                'ĉҶɟǿʤԌӂȧʕñ˰˔ƎȱȱѦВϱʶίЕŗӤzχȭέÿӟ˃',
                '·δȿƎɭČĂҲҠҿ\x84ʒˤŃŦљȨœňĬƹđƮþѵ\x8c±hjġ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'filename': '',

            'message_format': '',

        },
    ),
]


class ConfigurationStateTest(unittest.TestCase):
    """
    Tests for ConfigurationState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = file_logger.ConfigurationState.parse_data(test_data)
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
        for test_name, test_data in CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = file_logger.ConfigurationState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='files', name='ConfigurationState'),
            ),

        ),
    ),

]


CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'files': [
                {
                    'filename': 'ӗOԀӭƌјϚϫþŧƂƿ˗ƆϐЏoҤѦƥҷɑ˔ҡ5χâ˄ʗ]',
                    'message_format': 'ÔϳùηSІǕʓƃĂ[ƭƔ6ȎɼĀƸyЊȠȼȿҽɱηƵ¼κϢ',
                    'categories': [
                            'ĥ\x80ˬƑƀayӷҗŇÞɸɠϽԃϺƏ(ƞҜѠӫʾ°˰éʍgҢ\x80',
                            '˧ǹCēɦМɼЅƽԖҷ2ŢǾʲιYǱˡўҜӤ¤¸Ď8ԀЉİз',
                            'ʔϪWѢǆԌƍӓſˏϢɀ˝ĩДȔПǥɋБͶÈƸϟΒΘŲûәԤ',
                            'ιЗa©&6ԪˣҫчÉӧȕȶвƐ\x85aăԉũ¡Њ hδcοˏ\x84',
                            'ŀΘѠӅ҉ʛɃȍǔ˘í˪Ǆȝŀ\u0383²ĔΣLˤÐΉ\xa0ԙǱɊӷŖǟ',
                            'ːҖȴƑȥîõМ±˧mưЍĻÎҙ˰ҍkԎҞ\x87ӿӽʐ\x80νӣЋȵ',
                            'ѐLҨêŎʺԡқΘέ0Ԯёҋ5ӺˌњͳůǴԩҥђƈˮ˹Ӊě»',
                            'ǥтɧȴƳMтӵȺӨЂЇНǆƛе҄џļʈuwlҝĄĲ¥ɩАȇ',
                            'Ķʝ˖Ǽ@Һ\x96ʵǭӥ˦Mýɍ\x90ȝÁǝǭγʊԛΏ\u03a2ώ҃Ԉʻ҂Τ',
                            '·ξÂѪΗƈÔÙIȺΉøʾӺќŊʦԧǵʑ\x87ȲƙěǍŧƖ6Eү',
                        ],
                },
                {
                    'filename': 'ӮŔĨñίǽԗϋûљˑɲϵҨΙʂΚčďѸ@ɸ˹Ơάɽӛøɰ҃',
                    'message_format': 'șȤʝϢȫҢȝòɼέԤˡКѻõ\x92ǟ҅\x91ƝԮȨʠЦԭˇĺH°Ϧ',
                    'categories': [
                            'ЁǒΝƄϛяҼɍWҡȄl=ϑҝǜȔЕϞӽзĖƛίèςЖϟ',
                            'Ŧ"ȨӬͽǞƘǘѵ.ӫ˜©ʃɿӥЧάǒƂлDΏʎщďҙϒϐн',
                            'ѮԬĀtǓʐҗĂԪŤɜƙǗӢҬМƽľϞӡԂzѴǷӤ[ǡǩ\x80Χ',
                            'cȏӡҫжǗǏАв\x9fƁѱɤđϞɗſϫŀӝˇXɩϒ϶\u038b˗Ǽ¨Ρ',
                            'ɗ˔ΣήЪͷҰӁĊρĠīǺ΄Ŕǉ\x9e҈nΑБωǁǆÿJкSGϋ',
                            'сȆԫϞʖ2ɃǼ\u0381˅ɷ3˲ƌ',
                            'ʔˀэ`£ɑЎҖɇȯƓԧɪȔȨ0Ʀŏ',
                            'ǂɃƉƟνAǣźˊ\x88\x83Ԥ˱ϐðAƘL-ΨſϘϳ~Å¥m\u0379ӉÕ',
                            '˾\x90ҶϋǌϨŰʥćУJ;ƮӰȗÄƁ¢Өɦˉ\x9cѤаđгҹȓʆԀ',
                            'гˏͰɮƠeřŎԇœ˥ŘȺʞӖѽύɤYҰЧȽЇūϲħçȶbԌ',
                        ],
                },
                {
                    'filename': 'ƕýȶ\x99ϺƳϛșˏӠɒ.ΕʵĿӛ˷ϒƺȱҹή˴ɓʭ\xadР9Пʽ',
                    'message_format': 'ØЋ΄ϷЌӵ÷ϖЧʚ%ʣκǻΔ҇ÍԗűʛΐǳǳҎ\u0383ɠȇƯʑś',
                    'categories': [
                            '.ʼɗĦ8ȃƶӅцċЧɺӹ8йҏǼΐВƿԬǚËɕϲÜTϰĴӄ',
                            'Ѷǥ-χĔĢ$š΄ТиȫӖʙѢƱ\x9c˶ɜTĭӸқԁϏâԛПˏĹ',
                            '˖ÕƵлХӗΫͺѱϷїƍͿͰϖǚ\x98ГζcÀʾȠłԫćÁЅȁƛ',
                            'çɾŵˏԐőРίǞ½ӧȴϮȝРÛʩȫȃŕԗ\x87\x9cɐґȈ\x8c˯қł',
                            'ϹǾƊƂǩìŬ˚Ŋ×ӦROˎĂӂγȗʀX1ȠţāӂƖǅǘ\xad͵',
                            'ӂ;Ҫҿĥ҈ΞϏčÛЉѭȹСːțӻѬӡԔȒĤ҄ǯňћҤͼ°ǉ',
                            'Ȟ˜RϒӘŻҫϩǗ˾¬ȪЮʬκƲ˷ŨЊŠƵĳδǵƗȟɏүВї',
                            ' àʪӽʎӓϡįʼ<ãŜԖԩęԂǠ\x8f҄:ЩÍa\x99Ȯʑ˴ʼ\x92Û',
                            'ĿΛǯ˧тӾɺџѳǂĭƩϵȒ҂Ƃ\x95ʧ',
                            'êș½ŧԇ҄δ\x81\x89\x88ӴӵͳӴʸšюԢϗϙĹƊʕӑ҉ҒɴËȖȦ',
                        ],
                },
                {
                    'filename': 'ѻǔ´ǖψыɗƒҙϟҩŬҴÞǊƳɵҤѮřԊ,ɰӰĞҢŐӼʂӓ',
                    'message_format': 'ĥȊ1ϱʫ˕δκĦϋºɟЭíaXɱϮԥ4Û\x9eɊ˄Ŋ\x8dԑ҆øÝ',
                    'categories': [
                            'ʐҊʝϫŁťy/Ğ^҃ĦӛӎùΤҪƮſ+ɢ+ʟƦɞ\x92ƞήŏҥ',
                            'Ɩӊǅԇ\x84șя;Ǝ\x92aщ(ëϖŜҷňÕ³˖8ѩıзю¥ԄӥΚ',
                            'żе;ӓȯ;ʣ˻ʎŝ:ќȞȡȹԦÊʈďϩϤ\x89ɰǙōЈЮËɓӽ',
                            'CçΖ\x9eęāԏέɸ,ʒʠ<ĦԑӥŪԦHЎ˽р\x95\u038dɑҜɵʇöˌ',
                            'ӼΖëҿѺŒƲиçӊϘĜŭžưҺΜҳɥǪ˱ǃҢàȱΡ³˪-ì',
                            'Þҹ˙ˍāʑȤVǙɘˉЇуѹƾ˧αź\x99ǗtƏʬŰ¾æǪƎΣ\x92',
                            'В҃ȧϙˮӐʦzɡʧєӬȼEU<ӦєԚ²Ѕѯ³·íБьΪǾá',
                            'йĞî϶ԇɿ҆ҤƄί҃ЗηȆ¥ԈþǞΘƾǀǘӁUȘɳɔҖԌĿ',
                            'ҧҳΥэOȈĚ}κɱƔ\x8bϊОuΙҐã˻ѕΪ˷ԁóƾџͲӱҚǋ',
                            'ƯϥԟȁǓɨӉåÐΣΥҭԚƛëßБʠʁȓҝô{ʜԂɹ˚χxõ',
                        ],
                },
                {
                    'filename': 'Βҫǉ?ɡҁԄʢ¯ХʀѿĄϾàĝž˓ǔŮГrCҿӋˑk˅Ɂт',
                    'message_format': 'Ί˴ɶÒл¡ſё˦ϻѬΐ\u038d˝ϫǔȮȝǌ]ԂɲɾҖӜĖùєɦǕ',
                    'categories': [
                            'оƭȹʩʎȨƷҔȎō)ƵήҚɞǨǈЍǴϴ_;ġԐÖōɷ\x93\u038bң',
                            'ÉǨϦšѩ[\x91ʅɊȩɔ˃ɅƧȬĚŴϡ¿xëƥˁŴҩʩÅǊʱU',
                            'χҶԭѿȓɽ˙č˽\x92űѷϧŻЗӰʷԘ˒ȑȏɸů/\x86˜ɴ˦іʤ',
                            'ŅПϪ҃ɦ˱ɳ',
                            'ġ˙ѸӽϡҼӮŏǗɌ>ũ˖Ӂƍ\xa0˘ӹǟ¿Еɣѷ\x81ңͽҠͽӶџ',
                            'ӾAʁуΟ!ķϭ҃ÎʭɈίĄӛvJˠƱґˍXȖНЀȭʰ¹ȑȗ',
                            'єκЋɄ9ɓȟ˽У5#JíȼҘƮͳȺаǕEȑˣb>ЌŌҙŎӭ',
                            'НòƬȵѐˇ%Ģ˥sŻͺĤɆˢѨɪѭӟǿ˳ȐŧÎɣˮʛɂƞ¡',
                            'ȥéͺӦҁΚìȾѷŅђκκƆıҗ˼ҎΛәѶͳͽPрҜəИŦŮ',
                            'ʕɮҮa\x8fΫӸϤˇП˵īņӜ3í˙ҜT±ͽƲΜÿѡϊҘΗξˈ',
                        ],
                },
                {
                    'filename': 'ƻ@ώ˸ˀŕɝмѠɘī˯Ġĸǚ¦Ԣ҄ȓJѶԜЗԣёʥ)ʻΎ˖',
                    'message_format': '͵țħ \x7fĉËԀԢϾςӦƹ˟˰\x86\x83ǬҰϳLɂȻȺŦĲſʪԡt',
                    'categories': [
                            'кʼ\x7fȳƝǄéόΔ˩˞ŌːʬЭӏƠƠȏϘĖūƢƨŜϳϻȚɭÍ',
                            'sȸεұҷӮԪ˟ƮƤǫНӍŗԩώϲ\u0379ÒϙÒѢ³ɸӮ˱ũĞԉƥ',
                            'ǣǐ2ӆӯӢӥêˀΧȸȿƏ˰ʏԪΠϢԤͱŗҜƫ˅Ϸ*\u038bȰȭЕ',
                            'ҹɾłƔǍȻŘǂέ¿ɆĐ\x9eӌ˄˘ɴąǙɈаɿƞʺːƕѩäˏƄ',
                            'ѱĊºХʝѬŋ͵ȷǏŘɈYʙͺǐͰĮǒłõτβ˘Υϐœ©әʁ',
                            '(Іʌ°ʽЈŭφȊÆʺ¸ŗʕӽԕ\x94ΞǌϼǧǹҜNĲpЀԈСǌ',
                            'үϧɺƭԭĨȳԪ)ȴӞȋʞҋ\u0379ӂ҃҃ɠ`Ύ½ϽԆæ˺Βѫ˘:',
                            '˴ǌүСω\x8dġäӫ\u038bћ˰ǺƐщĶÌ˖õ\u0378ҫɚΦĿďϮϟԡ·ҷ',
                            'ATƵіǽ,ŲӑĿύɌˆӺȃɧˊŚХqΘǷзƻȎϯӋEλŧK',
                            '·ȫҡˏˢЃӹFǄӧVΖƼԖ˩Lǻҭɇ÷ҸǄË·˒űÙʠȴĽ',
                        ],
                },
                {
                    'filename': 'ƔùĊξщ˖ζ',
                    'message_format': 'ȭ˹ũƉʜǅ®:Ϥ˞Ìѐ˘ӿσǥѶӁԞнɐ\x96ѽҁΦĺ˝Ïȸƺ',
                    'categories': [
                            'Ǘ͵ԔȲ˂ČYƽ҂ĲΛӃұȨǧÖƭȹѪŏӉʘԬʚɁ΅ɏӹªÈ',
                            '҂ҳϤąIƼ˅ȥоãԫʕξʞҊŘмϚ\u038dƐƠĠì˺ψqҟ=ѷˏ',
                            'њΓȟƞӦÇӬźЉˌϿǯ®ΤÀҧȎŏˉ¥ԩ/ɫŖǬ.CÀ+Ǣ',
                            'ьӼÕ˞ԮŪӇ!ˍ=˦ʒdȴġƗˑƼɼӎ¯;\x91ӎǯͳ#ӝŞ«',
                            'Ö¦ǒԠΛʈМ',
                            'ӜƉɠӷǤν˭ƽƂƋ²γ˜őìés&ʔ2ǮǷҏ%їύ˪\x82Ȃ˥',
                            'ӖŭȰȬɬΨƴGʙ\\϶cӗΏīÛȀХџӧ˂ŝņǸĆԨFȴϧύ',
                            'ƖȚ&8ùǕ#\x93ӠɜєԚȣЕĩѯҊ6ƨȦȽůЫȱʞϻs˳ΤɅ',
                            'gήǌç:ŹɭѴɒϻΒҊԨˬбҲǤѸԅĵȬżĮʊħǀŚɎƆǷ',
                            'ɌԄ´ŎǁˉİҀϤȀϤȀԬюϏʍоƚpˠƓʺƱҍćħŹϠmӥ',
                        ],
                },
                {
                    'filename': 'ҢЇǂȈ˘Yϋʷ\x80φƭüРӼŌ˘ΣЏȊŦɜ҃SðƗˬυɟӿҳ',
                    'message_format': 'ҬŉŔ*ãёΏȸǩǉЮF\x99ƕƃɵƃɰԕKĠΦ҃˅Ǌɂ˄ѺгΚ',
                    'categories': [
                            'ӊȨɈыȼӤYƞΤϸϮĚǡѐ˻ӋʱȘȠìԆϞʗ˹kѝƕ·ˑ-',
                            'ȃ\x96ěˡƼjʮԬѳÀɨԞӈӳƯǏЪǸ¾ʖťіԒԭǿψʘŪɄɐ',
                            'DȂšѡƢNϦŔ"ʚӄŇ\x8eӵșǌŚΧ·ĄÂǅ҄zҏǇȨњԗ~',
                            'ǡƒχĒư¦Ȍ\x97ʶæ¢ɈĘǵԮĿшžʎÞӟΗѝѧ^ӜϦԢГZ',
                            '¢σ¸ë\x8fѠͼȩпɦƤǠѓƭМʫ+Е\x8aŷĕ=ˏêҀț£\x96ӆɦ',
                            'ˁȪʹąȻ\x9aɼʘƑӪʞǗʽҟҸȌПúϹ˒Һɜ ƔҚшȾ;ž˦',
                            'ØΉĒƁƐѯѼАˬʼ˰ϐ˫υŹϽқȽϼЮ\x99ϳί˗ʕϢĖȤҔ^',
                            'Ý͵φ҉ɣͶϽȋԌǺϧĐѧ3ʞ\\ѪӛҞ΅ůʥƵȫЉöûυԞÝ',
                            '£Ǩ˶ɮҪԒŵұƐ\u038bӻԦ˂˛Θ˫ѕάҰѺĉъӒ˯4ơƠҨϯг',
                            'ήǬ˭˾ȉ¡ùɛΩ\\śΖ\u038bϧǊίЇӊѩѾãǍϣҹʖŗ8ǈЮԧ',
                        ],
                },
                {
                    'filename': 'ϧʑΏ\x91ӦɣѰ\x8fmҲſӟχɘσϞԡϯԉ҆ԇˋ\x8aϬΰӫDÐʿƄ',
                    'message_format': 'Ɣ¸\x8bƉȔǂʾЀϧˈȽΟĞӐ\x93\xadȝԥԢ7WŒʖɀӭďҞȴδ,',
                    'categories': [
                            'ʳΗӶɬCΖÒ\x94ü·ĳ2χŭ\x85Íʆ\u0380ƃ΄ϫΥŮԛˉƜˏӫǻΗ',
                            'ŨСοɴѯѣѱĽ\x9dɶưǞӴɮӝԔXƌŌя@őXɔԑĜԗԦ\x84ж',
                            'ВƛʝѧƷʐӇѦòԠǛӓđ҇^=Ó²ŦˉԏÕѰϭɓӮʗΖ',
                            'ʔɮʜɮƙȠɳӂµʞ\x8dǑåфЖE!ӱƼЋϝѸǏ³ĠªĊҟǲʠ',
                            'ҠϏŷКʦ¥\u0379ɶϒʽ]ҌҨıͷԖʐŪìśłĝƽϙǼ©ϪaαƎ',
                            'ȯNȤǀˇ½sŁĩłÔÇɊʗʈԊĐäѢyпӼŲă˪Аϲɟʔɔ',
                            'ӷ^î\x9a_ÇɝĎԗñєӘbÐǷɳΌ×ȨɒѭƯʮԋŦãүҦǕ©',
                            'ЧȤˑµʎϑʽΰӋþС҃ѢʧįЕ˟ϼψß˩ωǒƹψąҊ',
                            'ʪѱƷƸ˦ʜşƞñʄQIӞэûƼϟϓņʥӲаƵǍϝdǕΗ×ґ',
                            'θɻѣĮΆѠӐȈЄ3Ɋ˸ǗÖЁϋŕŞęήԝ˫Ψe¾ӵȠјԑ0',
                        ],
                },
                {
                    'filename': 'ԍЃƹΠŕϫӅ\u0382ȭӨŜӯ˃ǵÏԭΚșƆ¥&ӧ>ҘÇǆӧÊ˛ȭ',
                    'message_format': '˧\x99ӛǯγÅѰȦđϧФԕlǍˑҋϿюœΔԏʮW˄ň\u0381\u038bʄпӧ',
                    'categories': [
                            'ΓͻΠ~\x80ԞϵӑS¢«ƴǽ҅ЖӷǝˬAɦKÌϪǩǍÎɯӮȌз',
                            'ƮÉϝӎ˔<9˸ЄɃŌāЩ˭ƉѬĨҧ~УҒӏˉԚ±ơÜΚÉʵ',
                            'Öӓ¾ϼʹȈåŦŲźĘğȈȱ·ӁƁȵӜĴǣªӢѥӺӴ\x8dӗχȯ',
                            'ŌɒƋ˵ɥêiFĔ°µjӝn¢ɍξǒ҃ƩǋÙɹїͲԌ˷ŋʪҼ',
                            'Δӏ½ӣǧȦɐʧ˄ʷɗķςėԤӏkŨ˘ӥvԦőǆͱ΅ϚÞƥâ',
                            'λŇŬǖϲ`ѧƠҡ½Ԉɘ˒ǼǮ҃ʏɉƦЌѓмщ\x93ѰӏǍѩТɼ',
                            'Ѯ\u0383ЯæřӐћӔˀ\u03a2³ˀɉËӴȥϦŊҹ½Ξөêɛѫήƴӝϔ˵',
                            '_Ӽ˟ΐʄıϳțŊ˃РӋΊĚђкҶҳʌƑƁƨ˴ǃ҇ЩȰÕšŪ',
                            'ѥүĎзǣĞɄɥΜɴȵ¨ɊԙҊ҆вԧҷʳҭԭȉԐΣɤĻбԚλ',
                            'Ȣ\x84ʐҖɲ҆ΛȺĔҒʽͿàƈЍǌėʷĥЅҹnǜƈ"˨HĄҿҵ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'files': [
            ],

        },
    ),
]
