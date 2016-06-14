# -*- coding: utf-8 -*-

from pygraph.fillpolygon_edge_2 import fillPolygonEdge2
from pygraph.util import mkGraph, saveG, enLarge

g = mkGraph((160, 120))
points = [
    (10, 40),
    (20, 10),
    (30, 10),
    (40, 20),
    (50, 5),
    (60, 10),
    (75, 25),
    (25, 30),
    (155, 40),
    (30, 50)
]

points2 = [
    (10, 60),
    (70, 70),
    (110, 10),
    (145, 10),
    (150, 110),
    (125, 90),
    (100, 100),
    (75, 90),
    (5, 100),
    (50, 80),
    (15, 70)
]

points3 = [
    (110, 60),
    (125, 30),
    (140, 60)
]

fillPolygonEdge2(g, points, points2, points3)

saveG("polygon_edge.png", g)
saveG("polygon_edge_large.png", enLarge(g, 5))
