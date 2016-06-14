# -*- coding: utf-8 -*-

from __future__ import print_function

from util import pointsToEdges
from line2 import mkLine

def fillPolygonEdge(g, points):
    edges = pointsToEdges(points)
    for e in edges:
        mkLine(g, e[0], e[1])
    lx = [p[0] for p in points]
    x_max = max(lx)
    x_min = min(lx)
    ly = [p[1] for p in points]
    y_max = max(ly) - 1
    y_min = min(ly) + 1

    for y in range(y_min, y_max + 1):
        inside_edge = False
        inside = False
        for x in range(x_min, x_max + 1):
            if g[y, x] > 0:
                if not inside_edge: # entering edge
                    inside = not inside
                inside_edge = True
            else:
                #if inside_edge: # leaving edge
                inside_edge = False
            if inside:
                g[y, x] = 1
