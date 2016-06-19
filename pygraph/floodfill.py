# -*- coding: utf-8 -*-

def floodFill(g, point):
    x, y = point
    coord = (y, x)
    q = []
    q.append(coord)
    g[coord] = 1
    while len(q):
        c = q.pop()
        y, x = c
        if not g[y - 1, x] > 0:
            g[y - 1, x] = 1
            q.append((y-1, x))
        if not g[y, x + 1] > 0:
            g[y, x+1] = 1
            q.append((y, x+1))
        if not g[y + 1, x] > 0:
            g[y+1, x] = 1
            q.append((y+1, x))
        if not g[y, x-1] > 0:
            g[y, x-1] = 1
            q.append((y, x-1))
