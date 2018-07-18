# coding: utf8
from __future__ import unicode_literals

from lingpy.tests.util import test_data
from lingpy.tests.util_testing import WithTempDir


class Tests(WithTempDir):
    def test_star2qlc(self):
        from lingpy.read.starling import star2qlc

        star2qlc(test_data('rom.starling.tsv'), debug=True)
        res = star2qlc(test_data('rom.starling.tsv'))
        self.assertEqual(len(res), 208)
