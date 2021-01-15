# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-15T16:34:23.373087

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import extension_loader


class LoadExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequestEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionRequestEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': '\x8c҃Ԫ\x8cӕÈƉňˈ©ԋ˖˰ӅѶ\x98˳DѳĻŽ\u038dЅŗʌӽ®ʿѡɠ',
            'minimum_version': [
                -5798342694904659491,
                -893137887231752371,
                1076040336908928748,
            ],
            'below_version': [
                5362175321124124331,
                -548485805096042218,
                -8414861151842793653,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɺά˜',

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
                res = extension_loader.Arguments.parse_data(test_data)
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
                res = extension_loader.Arguments.parse_data(test_data)
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
            '$': 'ʦϞÁйÖʳҟӞɬσ¤ǵľŘЏˣʄӮĖÁƾӻ³wȼ˩өЧӁЏ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2081078400913763032,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 64876.63513016893,
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
                res = extension_loader.Error.parse_data(test_data)
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
                res = extension_loader.Error.parse_data(test_data)
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
            'identifier': 'ԃɸμƑȤĖÒˌʃϴԨ5еɠĒҨϰ˻Ǚɑʉø\x9aʂ˯˛҄Ģεϲ',
            'source': 'ʲTǻϒƷɋȣ˝Ƹr¤яЊӛʔȱ˻¶ΚѻdϣȌƈҙ',
            'message': 'ԠɜϗƢ˰c{ЦҌɦǼÕҵ͵ыѿΠɛӏȲԏԥԢӢʌƆˠӶӖΆ',
            'arguments': [
                {
                    '^': 'string',
                    '$': 'ԓƟ¬Ӯϛhˣ˧ʊϹчė˝ԠжƋʾƮƧβˁμϏϸĜʫ+өĸΓ',
                },
                {
                    '^': 'string',
                    '$': 'Ǌɀэ\x8dɗĩЬ#ƚͶɍ/òƑ`ѾԑҒ!ãԚŃЉÑĆƨϋ҄%ǿ',
                },
                {
                    '^': 'string',
                    '$': 'Ц΅ΜBИӞԐԪĠOӗè!ŊɊųŔˤŜΡˇʃͼɪűƐϼ',
                },
                {
                    '^': 'float',
                    '$': 364432.7992898966,
                },
                {
                    '^': 'string',
                    '$': 'ȫϝ{řƷˁԌӜğ҉½PӔǚɷ\x7flҍО˰҉iĚΧðЛƊђ¦x',
                },
                {
                    '^': 'float',
                    '$': -39215.48585112853,
                },
                {
                    '^': 'int',
                    '$': 2619215346112601753,
                },
                {
                    '^': 'string',
                    '$': 'ƨŻΦǾˮͺӆĂөҊӮӪпҏʢАɫЎʞѸ\u0380іηȁɏҊʊԤϪͺ',
                },
                {
                    '^': 'int',
                    '$': -3945092814096294264,
                },
                {
                    '^': 'string',
                    '$': 'ԄϜ±úʑуӾˮǎ§Ѥ˴ƱԥԦÚʁӊӺȶҬɦėɽ˴ǯȋЀQá',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'v%',

            'message': '',

            'arguments': [
            ],

        },
    ),
]


class LoadExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailedEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='LoadExtensionFailedEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ʸςŵҢȰӋ~ΙȧВi!Č˻ȟaĄɱѐŔҧOEЁƘ\xa0\x807рƯ',
            'error': {
                'identifier': 'ʷúÜѮÊƏĜ˱ÊѼʟȬΤϡɀ˗',
                'source': 'ĭǽяʕрõϘΣĀǤ\x8aԢǌ\x90ðpПΩÛɓǌĈǏɯԙk˂ƑԘҌ',
                'message': 'ҴʽͲϓΉӹͳ҉Ӽɩ\x8bӍƸwӈ\u0382ѤɦĦғĂíxӝùѠůĂǯ®',
                'arguments': [
                    {
                            '^': 'string',
                            '$': 'ơ3ʒÈȮʆԙéȢΑßƝ˸ѪĄåћѧΊ¼ǌȷ҃ǉŭɖ˩ϴÍ§',
                        },
                    {
                            '^': 'string',
                            '$': 'ʎъDˆ\x8dƣΟͿǢßЩΌвʵƿθ+ϟ˂ȳɿԅѠҚҠċ÷Ź,¥',
                        },
                    {
                            '^': 'float',
                            '$': 123813.22041590791,
                        },
                    {
                            '^': 'float',
                            '$': 758268.3548048596,
                        },
                    {
                            '^': 'int',
                            '$': 1939577663779998854,
                        },
                    {
                            '^': 'int',
                            '$': 85206397816180901,
                        },
                    {
                            '^': 'float',
                            '$': 189643.01497118123,
                        },
                    {
                            '^': 'float',
                            '$': 195503.46986431524,
                        },
                    {
                            '^': 'float',
                            '$': 428745.4927791123,
                        },
                    {
                            '^': 'float',
                            '$': -68251.87053275171,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Kϛɂ',

            'error': {
                'identifier': 'ČǮ',
                'message': '',
                'arguments': [
                ],
            },

        },
    ),
]


class LoadExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccessEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionSuccessEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LoadExtensionSuccessEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ɠ\x8cj˳ƲԢɇǯӌįԎѦƓĐȤϱԥ˞˩ΰҔrŘl˶%ӝǆ',
            'version': [
                -4991116590184297827,
                7060587852492797176,
                7236968516734015802,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ĵҞº',

            'version': [
                878451203664257432,
                -4498014581166876365,
                4451685763839100025,
            ],

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
                res = extension_loader.Events.parse_data(test_data)
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
                res = extension_loader.Events.parse_data(test_data)
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
            'event_id': 'ΜŏΑ˖ˢˣΧ<ƱЕϫΗ˛ŔǕ¶ҘŪ˰+ĘE\xa0ŊѫɢҙȀӶϬ',
            'target_id': 'ã«ӠőϹԑƨįЭǉҘȹǞIӔȉҞ\x97©е%ĺɊʪțťӠ҈Ѕϣ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

        },
    ),
]


class RegisterExtensionListenersEventTest(unittest.TestCase):
    """
    Tests for RegisterExtensionListenersEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RegisterExtensionListenersEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RegisterExtensionListenersEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='RegisterExtensionListenersEvent'),
            ),

        ),
    ),

]


REGISTER_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'event_id': 'ѵҒ¶ϜΗɈҭΘ©ζǺ*ë˘ɪȱåżЯ´ЀϠǴȾ˜ãӀĳőҘ',
                    'target_id': 'uοė˙ƽÞ\u038dʞӡŴƴDсӮ\u0381ԩ`ӴӘŐʧ\x9cХĝЏӔǕǕƓʏ',
                },
                {
                    'event_id': 'ЏԤǫҦƦџҐѳɭģӳƌɪǱԁȉʀϽ·åüљЏʦVүũƶʻҪ',
                    'target_id': 'ѦΓͽӏƹɨLĘέАВЂыʚһŦ˥Ҟ˄Ɨ˻ЬZÇǝJƢѸҤ«',
                },
                {
                    'event_id': 'ʕń)ƬΪʪ$ѪăεϗԩϦСȺyҗӏОîЇʯʂʝģsϜĝκƦ',
                    'target_id': 'ѹӟƙUÎ\x8aӂΩʵ%ӯԇʷ\u0380ƑëԇȋĪԘх˖ԪǙɮԌLʬ§ˣ',
                },
                {
                    'event_id': 'ʐѣѨlřɀǜ×ʌжɸғůMÆĕË˯ҕӨФҜΥӫ£ͺ˨ƸџЋ',
                    'target_id': '\x93¾ћǅȅTȘсϚ:E\u0382ϟŕ҄ҡгӼ˓ԉϬġēϝǘƍӿǋΣЂ',
                },
                {
                    'event_id': '΅§ʋ\u0382fӫʵїΛ7ѣϱ\x92еӢƋ§ǂȆ_ӄT2Ũ~§шɁϳԃ',
                    'target_id': 'ФĮȎŘΝғԨӦƙȸĢŐ<ȨˌӌȠ˯ʘʸҨɒD˂ґ,ǢϧҮς',
                },
                {
                    'event_id': 'ÿƲϒ˚ΊʈˌѣоѢǝÐжҦȪɳ©˩ρʖŲҦǉŌƕōёĂԍö',
                    'target_id': 'уɻԌȢŵˌΙǯτкǘđлϚ϶\u038d\x91S˘ʥȎҸԜӠлȈ˓Ŏǭŝ',
                },
                {
                    'event_id': 'ϏԕӍŷưțƶиQԇͲȆͷǼѥύƘѺɔϘ÷ѵЍ˳mќƛ˾Ǆı',
                    'target_id': 'ѕЂʲƈм`Ì%БӥþҗEȽ,Ӵ\x91ŚʚƫȦґȮ˩Ѕ\u038bȧϊωШ',
                },
                {
                    'event_id': 'gʉ\x86ҚеɵΜĶĩθӬΤȤ˺ŅϔƉё˯ʟӴрӤARȲǠďÒ\x83',
                    'target_id': "ϰ¢ȜaʍȉӇĐņ\x8däиԀaӞˑˉXSғҵɽńÿҜ'ӒƎУЖ",
                },
                {
                    'event_id': '҅ʞˢĕķ¥«Œċ÷ʢӗʄƝȗεȲʺҁӺс҆ŨšǾɎԌϖΠø',
                    'target_id': 'ȼ˷ϹԒƏïķҬϘҳϏόMƾϕӊǈӢʀнѨ~ɌΣҮΌ²ɓσѠ',
                },
                {
                    'event_id': 'Йѓ\x97ϨӉ˵ӑίԙȃͰҭƎͰ҆ưыÍȞ±˧pÎԪʹŮİԂӖҚ',
                    'target_id': 'ɞ®;І\u038bǩҞǫ\x99Ѝȑˊ=΅Ԛɑƨгà¼ʷlΕǶǮ\x9cɶȣ΅Ԯ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
                {
                },
            ],

        },
    ),
]


class RemoveExtensionListenersEventTest(unittest.TestCase):
    """
    Tests for RemoveExtensionListenersEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REMOVE_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RemoveExtensionListenersEvent.parse_data(test_data)
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
        for test_name, test_data in REMOVE_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RemoveExtensionListenersEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REMOVE_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='RemoveExtensionListenersEvent'),
            ),

        ),
    ),

]


REMOVE_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'event_id': 'Ѥ˂vв\u03a2ˈ>öуͽӘƅҷɧǙūџԈђѿӟѣЧ~ѻʘɾҁϨϸ',
                    'target_id': 'ĞӥŌûΫÃȬѢŉɍě҈ÄĽɛ6ƑԁΎȗҚÍĢɾϾмº\x8bĨȌ',
                },
                {
                    'event_id': 'ǂɑȡ˖ŦϏɔĘïÕǎ¨˽Ⱥ(ҭҟƽƿĴϡЫƛȅȫҁлʇp\x81',
                    'target_id': '|źϋҼъȑϪƂѼӨ\u0382\x90͵ÊƂʎʏЇǙɆǟΤϑƻѦƮЯȵĽˈ',
                },
                {
                    'event_id': 'ςʶǠŜ\u0378ĥ¦ĚŢЊ˞ǶčĸƶƑĕɿЅдƴ5ΎɢʞԥǒȯʵЉ',
                    'target_id': 'ϴĮΖЕδğɗҊVЮшČď͵H˶ˑɮѺʚэǪЋйӫǓλͰǵǪ',
                },
                {
                    'event_id': 'ї\u03a2®ˮʉ\x84.Ӑǣ¨ԟǄ\x87ĩǟ¦ɿɄƉǰùœˡͰѮ¯¤ɬ\x9cȴ',
                    'target_id': 'ΗţƎ\x8fˎ"çʒԄΜµΌӬʓɾǭŷÄɈҨĻļȑɗɦҶƺ\x83\x9cš',
                },
                {
                    'event_id': 'һ\x8aȋЪBţƍɊүȪpǍǜ˦іšNԬą¬β҃ΟtËЈɆʤʯӱ',
                    'target_id': 'ǵҕҩļϪҠƁҋļӠ˶ΜĝѸɑҜжķх˟Ýƪԙԗ\x8bќ÷ҘFѢ',
                },
                {
                    'event_id': '\x99ʅяˌЧ`\x90ϋӬƟQǌɋĝtɈӳΐȅǓԡǒĺԘƏΥтÓ\x81ι',
                    'target_id': 'ƤҁɈщħԦÃЫԣҼǆɰлRɖөҎіƂ\x97ƄŪAԥȫ΄ΦЗʕÉ',
                },
                {
                    'event_id': 'ʝöΎ\u038b˸ƃ˰ˮҡϳԅԊѐǨ<ϊʐˠӜƛԄбӢ҉ͶƮԚüȂа',
                    'target_id': 'ηßйͶțh˲žԗҞ҃ɠǴԌ-ΜƘʲϗɧБɕȌɬмЗčӢϏɠ',
                },
                {
                    'event_id': 'ŁʨD˧˒πƯƷʥҕЍѰУ˪ЧĂɸΉɼɴĆƔƶҘƠϠʢȤҍҺ',
                    'target_id': 'ȅɟʋ\x9dʚƸƁϏˠʂѬϝѓʮӋÁӵʼƿ§ȃ_ѓ\xa0ʞ҉Ţ=ˌЏ',
                },
                {
                    'event_id': 'ҏŴřļÉΎкųĵǂɔζӑĞΜВſǓɲŁˇ.ӕų¼ζʐѼԁ\x85',
                    'target_id': 'ʁĢл˗ɅзʉǑΦƁ˴ı˷Ԡ¼ҡŌ˯ŚĩƌЕ˫ѕ˜υŝĲ˵Ү',
                },
                {
                    'event_id': 'ӲƺϺĄʂ˾ȉ\x92ȅҊ\x87ýʬȎ˛ʎƠҵɐяΨ\x85кӟѬÐҿúŐȑ',
                    'target_id': 'WμӠʪĚŬМӤΡƌÕĹіѢˢ˧ʹҤŔƕȜŲΗ3Ƀ\x93˙ƢǊò',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
                {
                },
            ],

        },
    ),
]


class SystemStartedEventTest(unittest.TestCase):
    """
    Tests for SystemStartedEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in SYSTEM_STARTED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.SystemStartedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SYSTEM_STARTED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class ExtensionsTest(unittest.TestCase):
    """
    Tests for Extensions
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSIONS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Extensions.parse_data(test_data)
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
        for test_name, test_data in EXTENSIONS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Extensions.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSIONS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='Extensions'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='Extensions'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='about', name='Extensions'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='Extensions'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='authors', name='Extensions'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='licenses', name='Extensions'),
            ),

        ),
    ),

]


EXTENSIONS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ƊǠgӲiÊɠǝĿѹΎɄŌÙђѼѦȞнϢҠ·ɁçϲϞʎϛĽ~',
            'version': [
                3367356776491174440,
                2090162281562452591,
                -1490052592796223443,
            ],
            'about': 'ŜĳДЃ`ʗƙʴǫТlѠ4DśǔѴʌмŠȊćҜȴϪǁǉǇϥΛ',
            'description': 'ԫʥJKŢãǑfӗʬÓʹKԉӒϝƏΛ˼ȲѫæӝõȴԂϿ¢Ͼȗ',
            'authors': [
                'Ͳ\x8aˮЃЏ҉ɊΧ˱ԂȌ\x9cѯȫϣϓ',
                'ί\x8cƙ\x86ԙ˲ġʬѿ',
                'БīʟƁ ʺÏΎ͵ȈɨĬw˨Ԝ©ҋѨ©ζ=ԦŦØQ΄Łσɲ˴',
                'VˢʌωɴÖҘҠˉԕ˼Х҈ʷ\x8dɬǸМО˛ħǴӜǱĮĸσ\x91ϋӈ',
                'μѪӏԒwȜǑʫԠʝԒȔԐӝӝψϷѪ˂ɸԟ\x97ĳЃ˟˻ȿĜɧï',
                'vҀɮŠǭ\x8dǩѰʮčӻ',
                'ѴȚԏ',
                'ʸǐʶҊѣӜѭʯɚϾʁħĐӺԍ:κΓϫэώǄɪ:Ӄӊv҆ŻϠ',
                'ˈȟϿǁǀûŇ\x8dҗʞmƱԌūƾΔżǮõԘΜ\x84ȱ7ӑϨʍӝNХ',
                'ҖɦʷѓſÍҒȋҹҮ\u0381ҹŜҁ˱иǨÀƟғБн\x83ØɿǶӫñĈɑ',
            ],
            'licenses': [
                'ÇɎÁǻԍϪĜҏ\x7fȅЅϬʛʞǗͶǈ˽Ǽω3ƧʂƒɊԏǞɽҁі',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ϸΡд',

            'version': [
                -6285572979900872538,
                -3404733906799049878,
                -7602770244600276049,
            ],

            'about': '',

            'description': '',

            'authors': [
            ],

            'licenses': [
            ],

        },
    ),
]


class ActiveExtensionsStateTest(unittest.TestCase):
    """
    Tests for ActiveExtensionsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_EXTENSIONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ActiveExtensionsState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_EXTENSIONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ActiveExtensionsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_EXTENSIONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='extensions', name='ActiveExtensionsState'),
            ),

        ),
    ),

]


ACTIVE_EXTENSIONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'extensions': [
                {
                    'name': 'ū°äșпӀʮŔ}Ѻ҈Қә҄ʿεʑӌӰΜҪȉԥҝɪ˼ŏ˘ȞЈ',
                    'version': [
                            1434677993178591131,
                            -2250950446052853465,
                            3189232921946033805,
                        ],
                    'about': 'ͳԕɑϠň\x84˦ԘςϾʨŜ\x81˳ӺƄƛΧʫȔřýҹzΑҾϥŖҋi',
                    'description': 'ɻΚХĈ³ѓɀϚЉJҜ\x8fЗґʀʍ˺˵ŹϴœȣǤňøȋõяįҟ',
                    'authors': [
                            'ȾŚЌϦCȿгΨчɂÔƗțЉѶαƦҒҨ\x80ҲԞʴ!ЎӞл`ҧǫ',
                            'ěȿƅӮʯȭӭFɍТȼͶÇƥԚɠΧĕCӝłʝʱʃҫȱͳˮӐƯ',
                            'Žҳ˫\x8eԦэ[ʂӎҖ¸ÖºŌʖѓʒǣÒЏɗ9íƿĝҊ˅ʳĠǊ',
                            'aδfȊ{~|ƊČɤӦҀƟŴЀc\x89ΫҳȀԡϬƙsöӂ_ԫԁ˫',
                            'әӧϡѯʸҡƄΙΩȋȚûκјÛǟ\x8bÒěӰǶҵíɾͲʝƷȬԝѯ',
                            'ӉϔÃ˅ɇ3¯ŻЈʛdҽσ˟ʇŹƓȯӃőɀ¦ȆʐНɻ¾®Ĳʮ',
                            'Р˜βУŶ΅fɽ-\xadҤĪʏ˲řƉȠɦtƋȇȺƃDқʕƊ+ųʛ',
                            'ȞϳƃbҊΦƞ˂ŕО˘ĕсɌã#\x89ʑƁƬ§\x8fЫC˱d\x9f}ƨ˱',
                            "þ\x9dƜІgǋϙ\x82ͶӜϭ¥ɁӽȷǯȂ1˦'pѫƢЎÞ˚ǑǹǙʫ",
                            'ΑŪȅцϰŷЀ˓ҢʥơvϱɧӖΒʱȣĚΗ\u0379ӃǳЖ/ɏҖΛċà',
                        ],
                    'licenses': [
                            'ǥΨӻŅϻÓƠϑçÕ˲ȩɉԖȟѮԣУɪƦǗʅѽȴʻȑſŝΦǯ',
                            'ɺȸϓΝɑlʶÐHϼĆЭɈƈȷǱğ\x90ԕĝ§ҍԊ΄ѿ«Ʋˈϣţ',
                            'ѣΖϛ¡ʌѝӤƩàѭіɤұӛЍԛŘʋѡбƣǿŹҵHɚ\x8d¢ԙ˼',
                            'ƨɶƸæӮ\x89ӂĕǅϏǒƙƴƗѹѕʰüЧˬpI\u038dlŽżӛɋ\x83\u0382',
                            'ŚjЌӝШҲƥͼ\x9fѪΦɖҐЪňӮӓŸǦαóΜш˨°˾ΚƆ/˟',
                        ],
                },
                {
                    'name': 'ЊΛԆĳ',
                    'version': [
                            7072519912741355291,
                            -5680371285000566002,
                            8942921594216248035,
                        ],
                    'about': 'хҭь\u03a2ӏƾʮІШƄʡҧ³ǧ§|ŖɻʁЁɤԫѷʠΧѾzʑýѢ',
                    'description': '&ʳƟǤ@ǍƆҰ\u0382Ħǐ˺ɵkʛї΄ƞͲjʎ˺#ŁˎәΕɁÎϝ',
                    'authors': [
                            'с\u0379ӿҝʹŔƩŎҋɱnBϞа®ԖӣҦĎЬǴɬЭ˪ϨҚKȿԞ\u0378',
                            'ĂɃǑѭƟφÈєʆ(ҍԓȥëȷʪȟԬҎŧ˫ȋđǢƷőғԝȗƅ',
                            'ж˹ȪĵːZʠӹɣɾǭјіϑϧЅý8Ѐёč˃ƃԡӴӗȩԉѯǾ',
                            'ѺϊȵɆpӋϗΰĠėÐѿҥԂ',
                            'ŧιĚǱĪҊƃεʼƆ·ѤÐҥ\u0383ȳ',
                            'Bː˚ʸȯf¢ġжĮӤʕŗ\u0382єҡɤҀçȾӈΥʰɹcΡ¬ΘΊP',
                            'ȹϲӣҥќƣƾԃϵ_σſ˷Ĩ±Ζ\x81˯Т~Ńҷėʌh`ľǘԍǤ',
                            'ŴͶ˘ЅƘԩŭǽ&ЬӇѰ˽҆˶Ҭѝøşϫ˅ǌ˽ƼɖfӀÅēŀ',
                            'э¸ϵΠ҇ΐĂǃūќŭ\x91φΰ\x9cũǿЈƃӥӤӪ_¶ʹÎȒƚЗŚ',
                            'ʚŊӒɭҢӽPǏҁȥʎç˜ѣѨеЦҳрӴŐԢҫǶϛЄë\x80ύҺ',
                        ],
                    'licenses': [
                            '%Ҽϳǽ˟ЌVɺƞǰ˄ήΦƮĜ<ПԖȎҝëκСO҄Ҫй#ѿљ',
                            '҄ԉԞ.Jҗ2Ě\x9f¥ӱҾôǬćʻҖƴǋĥsҒԛŻӣӥÈŞ',
                            'ˆĉ˝ɦ\u0379ÏǬıΣ҇ҋļ˙¼Υ{ǏӂɾсӳΝXϜҗɃʭϫӿɐ',
                            'OŏˀѦpɕѿϳzώѥˢ9ʟЍώʇү»ȕҢąːŚӏŬӷǠӓҲ',
                            'Ü\x92ӔđßĵŵңǮҞɬѭѮӀђӻ®ȐҔԃŪQԪúүъҏlцȫ',
                            'ҌʣȚѲюʺӒϫƷɤӵOǶĒыхǤǠѭԆâεϘˁŋĚɺҳŸќ',
                            '%ϵXƽĒͰј~ϷКɰZӡȉ>ПÑТҝɂѼŶȤ]ƣБʕ\x8e\x9cӸ',
                            'ÁνӜǏ[Ƶʵʡюѓ˾,ŸƁ\x84Ҝ¯ȼ˕ԕӫǲҭ˥ʒǂʹǑɑˋ',
                            'ȒʴŎŐͱǰїŪΌήѽтƌįíԙŅӀǹѡ\xadĐѼŠʽ˦ԡӺɅľ',
                        ],
                },
                {
                    'name': 'X\x8cҢ"ɄʶěϏÎѝȍїÜľы\u0382ǥŊҼ\x87ΛʄǑʵϥʪXz§Ҝ',
                    'version': [
                            989576912033719215,
                            4861781025371452769,
                            3153752657436808989,
                        ],
                    'about': 'ҔÛǽЁƤˤɼĳ)ɜ˔ϓŵʬƤƢĭǞʣV˕~;ˎˍԟü\u0380ÊɅ',
                    'description': '\x8bΘĲҹ\xadŧØšʢ¥ɫʅǒɔԎʱҦɗ\x98ɝǪ;ƃϐӜƉӿǦȯң',
                    'authors': [
                            'ȅӻӯòҋӮȦHѥжԗ˅Ưɗˊ҇ˊȃcϙȫɽbŔq˲\u03a2ʊӞӍ',
                            'ŌлʬƆϬСɕӄѿөϮӒȭυЏȓ˲Ө-ʾϕs\x87ŉɯдҧЄù/',
                            'ſƠԀŽБіΎʛη˼ԗZӌ',
                            'ЌÌϠōӠÚċӚϳǲӒӨãú΄ΦЗŒäͽĐѹʫӯΖÐψѪɝŏ',
                            'ќƐƳ;É¼яѓȔԅȢϥʂжƕκIҽ\xadϑ\u0383rɈҤϬӾČϔӚM',
                            'Ӟ×ŀƖϋҾЪz˧$ʔϳäķ˶ϵυƞ\x8aѼƏΤͿ͵˛Ńhҫёǧ',
                            'ÿ\x82ϪϼǫɷҰŹ\xadϠӀźƦ˧ѿɘάˎʽåǷңӮľɪƞ-СΞԬ',
                            'S>ŜАǙҪѣԀӽҰdԍ˪ğӢѣӵ:ҵҀЁę˃ɎǾԇЊόҚɉ',
                            'xόӅθºȐ÷ʼʑӂĿУ˥ǂ˕RѤŀӂȌɬϣɱϼǛȣłńԏŃ',
                            'ǣɎÉǐ"ӤЍíı7Г šǢfǽ˵Ϋˉ\x8cǜǤǊ2ÇԤѝēцϵ',
                        ],
                    'licenses': [
                            'Мҡʹŧƥ\x8dɰď:ĥΠъùʫӣ{ƟǄǃĜĤ¨Ҿùѱŉˁ±Ƕŋ',
                            'hȃГʨӀϧŅǌ҉ɼɌΨċЇϭǠȁШ',
                            'Ѽ8ȘDҮğªԚFȷϲԭˢϛɽĚŐғќґҖɆǓȳȿˉΛƳǿǸ',
                            'Ů\\ĮҮО˕˥ѡšӭ\x94ɩÚɳzǊѴϦžóɱʶƻƽlŔ>viʬ',
                            'ʚŹĦӟӅνµȟɢҺύψҗӺщ\x90ʚŪӼ˲ԫˁȶкϽŘ\x8aßѷƯ',
                            'ŝȽ˓ãηCҧŵǠïʏŷԄ ɼԀƺǓϵǭќɯŢΥ\x8aǵ˥ԗɘȸ',
                            'Ůŏʛ\x9aΘýрϛhκǭϒâŻҷĉЪǲαЪŴńǂïҲˎʊϋҌŔ',
                            'Ҳêȹ\xa0яӕoTȀŸ˚\u0379\x90ȤŉĖʱͿ˲ǩһôҍɬςÏĘҎ҈L',
                            '˩ɅӶΆƩŤ˦гϽǂ˥ȂͶǴУİ҉\u0379ÙΘȉËºҘΓ\x80ŬîѶ˯',
                        ],
                },
                {
                    'name': 'ȌȂHѦЉƋȑȗ˞ƴȗāѬЫθȶǏщҶұѕɶӷɊȬЍѵʸӐȮ',
                    'version': [
                            4940997653051633522,
                            2969287306058959386,
                            3171455656348392402,
                        ],
                    'about': 'ŉäԕġÊϔ\u0383Χ¦Ύӧȟу}ɀ\x8dŬԍǓȆȥ\x83ƈǘӂƷșɅoҕ',
                    'description': 'ȰɼȪӚʙɊ{ɟǌҀǱ]f©˥ġ%ӴµҦҜ\x96ҒʅɊέƓƲþǈ',
                    'authors': [
                            'âчҞι˨÷ˠЄĭĶҶ$ѳӋԅƪϩϜĆМ#ҕȜѐˋʨǨÈΟƜ',
                            ',ȻŻҝʫҿȥɲШÀԓӮȂɺŶʹCGʈѨțϲƳ³ʦ#ʁΎΎé',
                            'ԂϭµѻӟĕϘǳ×nΐ¼H$ȵƐ\x9aƮҷ˸ǽ=TÁϦƻèҪğǃ',
                            'ĺȋφğсԌψ}ϲԫхȧžЧ´ɹɯMþӌœЯlЖɾ\x97\x88Ӧϑ+',
                            'ǽѭҨЗϓŒňãҭƒѡԗЃΝФ\x8eWͷ˪ӱҶ!˹ѺżɿӳĚǰʼ',
                            'Ύ¿ϪɁΉ\x80ZȒƘ\x99Ц¨ӤʹԌβɿ˓X\u0380ʌʋ\u0383£²\u0383ƷƧíӻ',
                            'ЍԞȂЯͲʝӧŒȾ˫ыОѭ\x90ʦľȭȏʹǀϾќǡŴŮъǵůӉɬ',
                            '҇İǫpϛEδóӓϦÝʥԔҖÎԓԀ˦˘ɡјҏÍԀφķAT3ɪ',
                            'ҩҥɌўñɓЈŞɗā˩ƈєÞГϘ\x81ѡlȉǮԒţԘɸѾѻ,ȋʽ',
                            'ʐϺ×\u0380ǃǅãɾώŧăĨǆǢʢϿȬĄ®ӨΆĂɠΓʬūǡӜǙȿ',
                        ],
                    'licenses': [
                            'ƽǄȊŜþяϕƺӶҨӣɵƅʱɳԠ]È˰˷ ˢĉʴǮ˲ˋÿƱC',
                            'ǗƩг¸һ˓ȵƻʁєӧĺó¥ӥɜ:Ԫwϕ\x88ÅԫşēϩʝȠҺʳ',
                        ],
                },
                {
                    'name': 'ͲžĽʾŃӞƻȍǆΔ˔˧Ǡ˥ҭԟϪğОʬɑ˙ťʜǠo0ʷɰͽ',
                    'version': [
                            3777794873118882506,
                            2022088934832724582,
                            8346422836074478479,
                        ],
                    'about': 'Ɯ§ļɽÂԀӳѣуcԚ!ĻĔŹѧӜʨΑɤ,ҖȳѹȉӫԂʣťԟ',
                    'description': 'ȕņPѐĊɣ£ŀİǫѿç\x94ҎґǒϋƓĩұâôîҦԬӏŴԨáϚ',
                    'authors': [
                            'ӿ£пҵьяԅªюįӍ˟Њåзk҄ϦτƁt˵Ń\x90ˑƦҽԡнƣ',
                            'ˆŏΠʪ\x8bӄÓӑʧӊɩӀҘӅǏ§HɅÆ˰íыЯиȹōКɧHӺ',
                            "ʈȷ-§²њʵñȪƬɘдҏJƱįΡȧɞю'фöоƶâӢŤѕѠ",
                            'ʌƷǸ\u0381ɴɢϬМĤɻ˔ͲӋϺƦʰçþԂƂϸȉõνʮĦѩԧ_ʷ',
                            'ɥȻÌϮđk2ӯϼ\x81˲ªϥöıгƮɶ',
                            'ǠԊΏɊȻØͿΉΎƧϊpϑхũӁȁzsѕÀǮпƏήǈĉà<ӥ',
                            '£ҩğɡȖ\u0380Ŧ#ʳӢǘǵÛêԄƌɎоЗͱ˚çVō҂уɿ˦ˈʧ',
                            'ɑТмΖїȤƎΗɳsчěЦŴűɜƓ$ał\u0382ˬǭл\x82ѓԦ˸˵ů',
                            'ЬҁȋÝЀǰɃɖƖŴɉԝèţʭΤ;ŎŮ',
                            'ńŋXȽήđǚʯƲɟƑƭºЇȲΛҳʏΙ1ӈѩLE˾îѻȲȯǦ',
                        ],
                    'licenses': [
                            'ԜĿūʃŸęɈӄŉŁ˂\x98ȋŔѳɓκțˊПӝфVνӞ˭ƛƘŚɡ',
                            'Ìыκ˅ŜxӱрĶѴѶÈϬċԪ9',
                            'wԆӂϙó=˱ҀxϜҠŃϭȅӅҕҾΚα>Κ-ĞȚϣõɸҫǜ\x9b',
                            'Ɵ@ʢӱɳыũɫԛƷυpʑҟώQŸӻʪТж˰æɊҦƩɾͶ·ҷ',
                            'ƣԜųԧ\x90ȿŔ\x96Ðδøʹӣ˦¸ȦѐɌԞɻʌÀŉӌƩҢ˻ҩŰԋ',
                            'Ԩɫʗ˦үѱѺȖāЯĜ\x9fÜŚċ5мȾчΤƓģȷі\x8aǱм]ĺǰ',
                            'ʹϗѽԣУЬˍϙӃђЧϸе҈Ө,ΥϯŅĒŢҧtÏΐϛұȁΌ[',
                        ],
                },
                {
                    'name': 'ӂvĞǕ¯ӴʡňΑτơžɏ˞ťġâӗˈ|]҅ĭСñ/ŷγЌЧ',
                    'version': [
                            -1713806811118162379,
                            -3813986265630651369,
                            -2219497935874569688,
                        ],
                    'about': 'ʝτįľȅǭFƌƲƚɸɗҞнε^ҏƔwҒ$ɲяѲƮЉļȊԭІ',
                    'description': 'ϔкҜɿȬӂҖ~ϣ7ʨɐßαƚɖǺĚƥťįƺpɤЀʈʒʣњѫ',
                    'authors': [
                            '҇ƙЖŔˑ\x97ΘȧӿƱŝÀ˚Ùӵҿ˨pŪʆȟƥȶÐĪό·űǖw',
                            'Ƅ˱°;όϸȀɉӯŽƙΨ˂ʌˊї˄r}T҂эɫȪˀòʀgԝȵ',
                            'ǴϤ~¯яӑĽκIʇɱĿуʐԢðŵĒΩԁϴǞñҸƐȿě\xa0ǊѢ',
                            'g9ʶ˗ʮѺϞ˵ЕЍŘÑċÃӮҐϊËĄǠԚǉcϋ·\u0381PɄƧӝ',
                            'ŒϵºúΩǙєωϽȨɼʶĭ҈Ιwˊǁşыɳ¿ӜҰ\x84ҔӤԅǨџ',
                            'Ǟ\u03a2&\x90ϿµŌӜˑҟĘĊ\x93\x85ȗɔќǪrTƒʺÔѩɻÕөӓϞƷ',
                            'ȜӬԛЉĩԛЛ˭ĠŪȔüσŤϱԎċĔθɲϹӖʆӍĉ¨ŊÎʥŇ',
                            'ҼӟȺѡӥΤȕϯӼÛκ¢ƱƛԃʽӼϷΏΪΓŃ$ӍӤ˗ê\u0383З˧',
                            'ŶΔԝ$ɼ¢ԢƾĵʇͳЋŎďɨЄν*ɿӞĊĢɑЖvзǟӁϵU',
                            'Ƃ˭ɢ˝\x8eɭŮзΗơ҂ҲԀͳыĂŮԌȘʳʜӦб\x97ÍѭΩǲ6ʼ',
                        ],
                    'licenses': [
                            'ɷЩǢԘqҲ',
                            'ɊǈϭȺȜРȣӷСˈĭԫϨгҪѩϛ;ьɏЈųьĪƮӂȗčԧʔ',
                            'ΪèʓzҜȔ˞Eǩ\x89ʀǐȓʱțù\x91șԗҺёШȉèʿɑğɓш\u0381',
                            'ԉЕ\x89ήӨѰţʏĬƉсǹξūδӃ\xa0ҍxθԁүҌԒӎѨӧƎ҄Ő',
                            'аӦƥДϐ+δ\x90ʊÒǺʇǤәѕ\x9f\x8eǁԛȐƏϊʥȻǖҦǱ¡ŰƑ',
                            'šҵŔʜ²˴ƶƀҴŏˁϜϢƥĨ±ӅϚѼèXƦX\u0379ɬhɟȗʔӋ',
                        ],
                },
                {
                    'name': 'ѻʉǡҷ˼ЙǺɻӞBΗѺӘĎ°\x8aƀķ\x9dǈѭǗғʺіЄȊĖΝћ',
                    'version': [
                            -6357321378768454245,
                            6299377982408431613,
                            -663702864695997738,
                        ],
                    'about': 'ϋΑǞ˵ӵϨЋŗǲ{ŚԅдëǉeƋӵϡҬɱśɾÙϢȠÍЖȏй',
                    'description': 'ҶÐЊϙɛƓƌΕóƏϟʎɿӔӐԉ%҃əŪι4ąƠɈÓɀȋcν',
                    'authors': [
                            'ŧҽѧԞϹĨřȢÅҴǴ\x9bǭѮʍı½ˑӖϼǳϸύѷǂɾ҈ˠƝĘ',
                            'ǣM˽\x90¥´¯ѯҼ¡ĭӕЊâǕӂˬƜƒˌxά\x80ϱϤɽǠ\x93Ȕз',
                            'ɮ˵ԄƗɢƐθѻņͲСҖˠZDǱǁāȐв҇ɑʨ\x9fǇʂķҒͱǨ',
                            'ˌ=ʾӹ1Ӈɵ˯Íǰȷ',
                            '\u0381ΛʡmӓǢdƮʫʔǼśԐƮв˖ӹȣѿӂƯӧ>аȖҌϢˏ¹)',
                            'ΥОҏƖ¯гʤĿ(ӕʱ˒\x89ï\x8dŊԁ´ɣ\x83ԕĬ˔\x9e{жƱȰɿκ',
                        ],
                    'licenses': [
                            'ĔєÂǮ2Ƙԧ҈пȍͷĂùέǴˆʯӸ¾ǕȏíǩѬĔ÷ƱѿȽŶ',
                            'ƁǏɼÀˀɮ¾\x80\x8d&ǭǣџ¨ƅФ$ƢħҾĢȘjԠғÛďư`Ǎ',
                            'і\x9cȾ7˥ʍѠϵǩÿˢў4ëĞ\x87²˴ҌвҊaȻǂİøǑ˦Īͷ',
                            'Ϙ˦ʘ˺ǲԓҘƩŖѤрИ\u038dÛҎÿ˺\u038bƖŷƐəǓͲύĈȘ§Ԣ˧',
                            '&Ҫ\x86Ż\u0378ЛҰʩøǥ\x9dƅȝPɵǺШƟÎ,ɦƳ\x9fťĕǉŮəгŬ',
                        ],
                },
                {
                    'name': 'ҵȻ\\ώϐńɘǵЌϸǉɓ˂ϨˁϬѨʞ[ȬϯȸĝӒΛŀψΨЌÿ',
                    'version': [
                            -2926378534256567364,
                            -620067442039771626,
                            -8558779899720362908,
                        ],
                    'about': 'һ\x85v˂7ћнǛӊʑˌƆтəȘ҉ù¬Ʒ˶ŅЗҘШƏǣöñϼӣ',
                    'description': 'ůӁǰ΅ҡʨ×ʎξӦԊξřόȻӂхǝĭСȎʞʰƖϤҳØϞ©ѳ',
                    'authors': [
                            "˱ԠΣ0'ǵǦ`3½ǴɩƐυãƌӡǣ¢Шý˦uЦâ˴ͼŶӦđ",
                            'Ћ[Ü\x94ƯҟԕЙƑÁưʤŴϑ&ΩŞЖҫùԉ\x90ҏWљƺĥiяΒ',
                            "\x89ԭщe«Ôϛʁґ\\2Њϩ-ĉԤίÕϖȽoÑíʓĔǴ'ËѬȖ",
                            'αȢ2ЋƂҽʗЈԎɡ3т',
                            'ӭЧVΰҁӖʰĢӲНԜ˘ĖӏЎʪ\x8fτɜ\x99ɖɎԜӶд\x9eƍ#˨ƨ',
                            'ҾѸыЁѰŀѭęϪΨʆjϣ˒ȉwɥƃĊã)Һӹĵå\u0380˪Ⱦȓн',
                            'ŐɚđуӭЏάԏёθƷǉűΡdϏÅԦӚӯEѾơȔϘȼŖҴʚǹ',
                            'ʨǇόǣ7Ұѹƺˀ҄ɎrǰˤƘȉҩѭȼʀÌѩοФ˃Ƴ7Gξё',
                            'ň)ˁğ\u0383ɶүθɣÁΞʒЃˍ\x93Øԟʛʶϫԝhʛθ¡҅Ǜλ6Ѯ',
                            'ѩ`ˎҪȧϨšȜӚĵӰǠЕŴŏ',
                        ],
                    'licenses': [
                            'ĂӦƏчǳɮИϮǛЋ?пƷԥ*ԗʽҷɷΙúȽеtȌɞȺ˴ǷǛ',
                            'ſPÒǛȨŠӥ¾ɚˋӦQȞӥɺǃыˤԩʠЕƄȪʈΘϓ~ȭƤæ',
                        ],
                },
                {
                    'name': '҃Зʀ?дУƘ\x9cƣ˒ЁɵˁDѳЄǭ¬4ΑčӻʑѤîĜԬ_|ű',
                    'version': [
                            -7032759515334688575,
                            -1316406638326358891,
                            1572456733136182785,
                        ],
                    'about': 'DjҤɠ³ϔźͻ·ˤĀƣÞ˰ǰƪȊȑćȩʉɾ\x8cąӨϦǍZ\\ď',
                    'description': 'ñĿĿ˻¹ȌŉĹȝƋӏϐČѱʙ\\ԅαʲӢǮľнŇƘϫHӉƟΤ',
                    'authors': [
                            'жƦȪрιĈУǌѴ4ӗŝìǴˌ˂ӣȃĴЪҪʷϻН\u0380ѫ˴ò˸ϓ',
                            'Ŝ˸Ϗζ˴\xa0JƱБµʟűԈϥĹΡ\u038b˧ϩҹQcZpƈ\x9eϘπÍɟ',
                            'Ӑө\x87ȸťΏΥǩǍ˥ԧuƘеIƹ\x9eυÍʻσǦґˬʞʆһѽӪʿ',
                            'ϼ@ҸϏFȇ=ЦnÍРϏUVȾľӲ1҈ț;ɀɔыӼøĚȎԦʹ',
                            'ßÛάǭȗ˸?£ȞдҙȯĒ\u0379\x81ȅõɼͷǥ ђƂŁ˾ɪʲȢħ%',
                            'шӓѺ˧ǛСϰԇȝŜӇӢ\u0382ˌѼϯ\x96мѰĬǋƸŶɾԠ҅ǯ¡Ňȗ',
                            'ԦӌϙǀѶʹҨȐÑgˌΔ{ϐΫ\xa0χ»ҥɜΙɳǍĊɓѕ\xa0Ҡ¬Ĵ',
                            'ζ\u0381ŀ½ĳˈưϞʼ?ǤǡǗϓҗȵʯǡʐѻʧƬǵɇӳўɪҽнϔ',
                            'əaX˼΄ΪВ\x9fƺøϐȕ\x92ӶԃȖ\u038dˠӰ\x80Ȓðıъˑжѧˑ҃ǎ',
                            "sɕġɩԖóДƶäΌǡҋÙȄǘЃĊ˺ľͲиҵĸʳ'ԚһȹØЬ",
                        ],
                    'licenses': [
                            'c˔Ř҂ӻѓҀŻǌӭƝƌZЃɽȴư˨žƠǯȁČ=ϐʎ×ϽϒЩ',
                            'чϒԛѵϣәӰȅʙӡωϗȗәƱΔИ^âǃ-cΫϳ³шǗ\x80U˛',
                            'ĻȺӷѤДɤʈӾ¢1ƭŵͽɏΧĲҏʱĕÿМґƪԪųś:ʹԚԞ',
                            'ǻҬťΆoʨОǚÂеÂɦ˦ǴŷƜ҇ȈԟԧĞȥбŦ˛Ђſ\u038băː',
                            'ÀǮѵʬǰΊЙǷÄɅӹӫӪ¦ǧѾʚɛҩ҈\x8bǿȵ˒ƨȎγ\x9aΣɻ',
                        ],
                },
                {
                    'name': 'ӻǢϙɒe*ĐĜƸүѰC¹qиӕКǜ½\xa0ɂԡƢΝŧҞƚ¼Цr',
                    'version': [
                            1384772750831531915,
                            -5945565176713741763,
                            -8426154026391092754,
                        ],
                    'about': 'ʯӲĎȂĎ\x9aΫÄδѦĻҲǿǙ©ыөӑ´ĠĦȾÇѺӎюҷ\x83ˋß',
                    'description': 'иpΦҒ˗ÂɨҚKǴЁҩ\x89ӷԘȥҔʄҕK»ɉʘϪψЍ¤ЧǶǗ',
                    'authors': [
                            'ʯԤ{Ϧº¼(ĭЦϺ\u0379ȱВʃəʮԀÄΨğ˄ƴeөίϮӇ¦Гň',
                            '¥ҚȊȰƋċŪzǮʐŽɁæț\x9fªIæАϰɬɳT\x9dKăªơҵȭ',
                            'ZǯĨρʏȩ;ӌϡä[\x86ǰһӻū8ӃяӁθҔʻЊGʘԘġЊǔ',
                            'Λʳǂșµӝ˪Əɂк&ǘѾӫʹТĦȴȦʎǭ˦ӌЯєʪǎΥsſ',
                            'ʌ"\u03a2ϊϦ˥ƈȮŚҺuɕѲӮɆű½ȈʞΚЊȯȬmeʹѽξҺ\x9c',
                            'ʥˤѕɶ˄ũʆ˲ϦӉŻϷƃŵԓӱCιɦǊˤЎϮĝȪĤҜȧ\u0380ҝ',
                            'ЧşЏÞɏкȿ²џɧҵγÉșΆЪΆη˩øʯjͼŝ˓ƎɮćʡȌ',
                            'ŮǸʹǄХқōÙgϮ˩\x99ăǂ;ćǡºυĿƘWʦѷɜҥàrľь',
                            'ŞԛĐƵӨԑˎǢАǿ͵~ȝӁ!ɋ3',
                            'ϫ˧ӂѼ҄ʴ\x95ŝΎҢҩѨԉȘԅʨƫh9΅ΎÿȋμͿ;Гĝůԗ',
                        ],
                    'licenses': [
                            'ĦšҞԁәɮ]LǃЧċҩΰ˜ҫŏęʫǈОɲ\x7fmīҥԡѽ.:Ӄ',
                            'ĖʸÁûÔĮŵҟĴȤōҀǵťəϕAxыЛδģUƤđǄҒ2·ԓ',
                            'ȉǟɃϤĖґŁQʮӌǚѣԞʁuŅҦÍȷǳĨ˒ĨʯfѼѳяӮ˂',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extensions': [
                {
                    'name': 'ѢѤѐ',
                    'version': [
                            1314472723704366421,
                            4730095209567026924,
                            5861636235860524698,
                        ],
                    'about': '',
                    'description': '',
                    'authors': [
                        ],
                    'licenses': [
                        ],
                },
            ],

        },
    ),
]
