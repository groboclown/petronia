
"""
Unit tests for the extension finder.
"""

import unittest
from ....aid.std import ERROR
from ....aid.test_helper import EnabledLogs
from ..defs import LoadedExtension
from ..ext_finder import (
    find_extensions
)
from ..defs.discover_types import ExtensionCompatibility
from .mocks import (
    mk_disc,
    MockLoader,
)


class FindExtensionTest(unittest.TestCase):
    def test_default_platform(self) -> None:
        """
        Loading the default platform exposed an issue with the loader, where
        the one extension to load, with all of its dependencies, would be
        first in the returned list.

        :return:
        """
        with EnabledLogs(ERROR):
            ext1 = LoadedExtension('p1', True, (1, 0, 0,))
            cmp1 = ExtensionCompatibility('p1', (1, 0, 0,), None)
            ext2 = LoadedExtension('p2', True, (1, 0, 0,))
            cmp2 = ExtensionCompatibility('p2', (1, 0, 0,), None)
            ext3 = LoadedExtension('p3', True, (1, 0, 0,))
            cmp3 = ExtensionCompatibility('p3', (1, 0, 0,), None)
            disc1 = mk_disc('p1', (True, ext1.version), [], implements=cmp2)
            disc2 = mk_disc('p2', (True, (1, 0, 0,),), [cmp3])
            disc3 = mk_disc('p3', (True, (1, 0, 0,),), [], stand_alone=True)
            loader = MockLoader(disc1, disc2, disc3)
            res = find_extensions([cmp1], loader, False)
            self.maxDiff = None
            self.assertEqual(
                list(res),
                [disc3, disc2, disc1]
            )
