# -*- coding: utf-8 -*-

from __future__ import print_function
from pygraph.line2 import mkLine
from pygraph.util import mkGraph, printGGui, enLarge
from pygraph.fillpolygon_edge_2 import fillPolygonEdge2

# line

g = mkGraph((800, 600))
ends = [
    (200, 100), (200, -100),
    (100, 200), (100, -200), 
    (-100, 200), (-100, -200), 
    (-200, 100), (-200, -100)
]

tends = [(x[0] + 400, x[1] + 300) for x in ends]

for end in tends:
    mkLine(g, (400, 300), end)
    
mkLine(g, (100, 200), (600, 500))

printGGui(g, cmap="Greys")

# circle

import script_circle_gui

# lineStyle

from pygraph.circle import mkCircle
from pygraph.linestyle import *

g = mkGraph((400, 300))

mkCircle(g, (100, 75), 70, SolidLineStyle())
mkCircle(g, (300, 75), 70, DashedLineStyle())
mkCircle(g, (100, 225), 70, DottedLineStyle())

printGGui(enLarge(g, 10), cmap="Greys")

# scanline fill

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

printGGui(enLarge(g, 5), cmap="Greys")

# flood fill

import script_flood_fill

# cohen sutherland

import script_cohen_sutherland

# symmetric transform

import script_transform
