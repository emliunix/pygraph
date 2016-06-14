import unittest

from pygraph.fillpolygon_edge_2 import evalLineFun

class TestFillPolygonEdge2(unittest.TestCase):
    def test_evalLineFun(self):
        p1 = (1, 2)
        p2 = (6, 12)
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        dots = [
            (1, 2),
            (1, 3),
            (2, 4),
            (2, 5),
            (3, 6),
            (3, 7),
            (4, 8),
            (4, 9),
            (5, 10),
            (5, 11),
            (6, 12)
        ]
        l1 = [p[0] for p in dots]
        l2 = [evalLineFun(p[1], p1, dx, dy) for p in dots]
        self.assertListEqual(l1, l2)
