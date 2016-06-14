# -*- coding: utf-8 -*-

import unittest
from pygraph import util

class TestUtil(unittest.TestCase):
    def test_pointsToEdges(self):
        points = [(1, 1), (2, 2), (3, 3)]
        expected = [
            ((1, 1), (2, 2)),
            ((2, 2), (3, 3)),
            ((3, 3), (1, 1))
        ]

        self.assertListEqual(expected, util.pointsToEdges(points))
