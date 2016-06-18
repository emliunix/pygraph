# -*- coding: utf-8 -*-

from __future__ import print_function

from util import pointsToEdges

def horizontalPred(edge): return edge[0][1] == edge[1][1]

def evalLineFun(y, p1, dx, dy):
    (xs, ys) = p1
    return int(dx * (y - ys) / dy) + xs # x = f(y)

def fillPolygonEdge2(g, *polygs):
    points = []
    edges = []

    # if there are more polygons, either nested or outside
    for ps in polygs:
        es = pointsToEdges(ps)
        es = filter(lambda e: not horizontalPred(e), es)
        
        points += ps
        edges += es

    #(p1, p2) -> (p1:0, p2:1, y_lower:2, y_upper:3, dx:4, dy:5)
    def expand(edge):
        p1 = edge[0]
        p2 = edge[1]
        if p1[1] > p2[1]:
            y_upper = p1[1]
            y_lower = p2[1]
        else:
            y_upper = p2[1]
            y_lower = p1[1]
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]

        return (p1, p2, y_lower, y_upper, dx, dy)

    items = [expand(e) for e in edges]

    # determine boundary
    # lx = [p[0] for p in points]
    ly = [p[1] for p in points]
    # x_max = max(lx)
    # x_min = min(lx)
    y_max = max(ly)
    y_min = min(ly)

    for y in xrange(y_min, y_max + 1):
        items_in_range = [i for i in items if y >= i[2] and y < i[3]] # y in range of edge

        x_vals = [evalLineFun(y, i[0], i[4], i[5]) for i in items_in_range] # if x is met, filp _inside_
        x_vals.sort()
        # x_vals.reverse() # smaller x on the right, convenient to pop out

        # pair up x_vals
        i = 0
        len_x_vals = len(x_vals)
        x_pairs = []
        # it must be an even value
        assert len_x_vals % 2 == 0

        while i < len_x_vals:
            x_pairs.append((x_vals[i], x_vals[i+1]))
            i += 2

        # inside = False
        # for x in xrange(x_min, x_max + 1):
        #     if len(x_vals) and x_vals[-1] == x:
        #         inside = not inside
        #         tmp = x_vals.pop()
        #         # current point is a lower point
        #         if len(x_vals) and tmp == x_vals[-1]:
        #             x_vals.pop()
        #             inside = not inside
        #             g[y, x] = 1
        #     if inside:
        #         g[y, x] = 1
        for p in x_pairs:
            g[y, p[0]:p[1]] = 1
