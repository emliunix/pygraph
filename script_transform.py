# -*- coding: utf-8 -*-

from pygraph.util import mkGraph, printGGui, enLarge, transformPoints
from pygraph.line2 import mkLine
from pygraph.transform import Translate, Symmetric
from pygraph.fillpolygon_edge_2 import fillPolygonEdge2
from pygraph.linestyle import DashedLineStyle, SolidLineStyle

shape = (180, 120)
g = mkGraph(shape)

tri = [
    (-5, 5),
    (-5, 25),
    (-15, 5)
]

tri0 = transformPoints(tri, Translate(60 - 30, 60 - 30))
tri1 = transformPoints(tri, Symmetric(vertical=True) * Translate(120 - 30, 60 - 30))
tri2 = transformPoints(tri, Symmetric(horizontal=True) * Translate(180 - 30, 60 - 30))
tri3 = transformPoints(tri, Symmetric(fortyfive=True) * Translate(60 - 30, 120 - 30))
tri4 = transformPoints(tri, Symmetric(vertical=True, horizontal=True) * Translate(120 - 30, 120 - 30))

print tri
print tri0
print tri1
print tri2
print tri3
print tri4

fillPolygonEdge2(g, tri0)
fillPolygonEdge2(g, tri1)
fillPolygonEdge2(g, tri2)
fillPolygonEdge2(g, tri3)
fillPolygonEdge2(g, tri4)

dashed = DashedLineStyle()
solid = SolidLineStyle()
for x in [0, 30, 90, 150, 179]:
    mkLine(g, (x, 0), (x, 120), lstyle=dashed)
for x in [60, 120]:
    mkLine(g, (x, 0), (x, 120), lstyle=solid)

for y in [0, 30, 90, 119]:
    mkLine(g, (0, y), (180, y), lstyle=dashed)
mkLine(g, (0, 60), (180, 60), lstyle=solid)

printGGui(enLarge(g, 10))
