# -*- coding: utf-8 -*-

from pygraph.fillpolygon_edge import fillPolygonEdge
from pygraph.util import mkGraph, saveG, enLarge

g = mkGraph((80, 60))
points = [
    (10, 40),
    (20, 10),
    (30, 10),
    (40, 5),
    (60, 10),
    (75, 25),
    (30, 50)
]

fillPolygonEdge(g, points)

saveG("polygon_edge.png", g)
saveG("polygon_edge_large.png", enLarge(g, 10))
