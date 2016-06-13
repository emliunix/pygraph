# -*- coding: utf-8 -*-

from __future__ import print_function

import numpy as np

def mkCircle(g, pos, r, lstyle=None):
    (xo, yo) = pos
    def paint(x, y):
        if lstyle:
            lstyle.inc()
            if not lstyle.p():
                return
        for a in (x, -x):
            for b in (y, -y):
                g[yo + a, xo + b] = 1
                g[yo + b, xo + a] = 1
    d = 1 - r
    x = 0
    y = r

    while x <= y:
        paint(x, y)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1