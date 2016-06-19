# -*- coding: utf-8 -*-

from __future__ import print_function

import util
from linestyle import SolidLineStyle

x = lambda p: p[0]
y = lambda p: p[1]

def mkLine(g, start, stop, lstyle=None):
    if not lstyle:
        lstyle = SolidLineStyle()
    # ensure start is on the left of stop
    if(abs(y(stop) - y(start)) > abs(x(stop) - x(start))):
        def put(x, y):
            if lstyle.p():
                g[x, y] = 1
            lstyle.inc()
        genericLine((y(start), x(start)), (y(stop), x(stop)), put)
    else:
        def put(x, y):
            if lstyle.p():
                g[y, x] = 1
            lstyle.inc()
        genericLine(start, stop, put)


def genericLine(start, stop, put):
    if x(start) > x(stop):
        (start, stop) = (stop, start)
    
    (xs, ys) = start
    (xe, ye) = stop
    (dx, dy) = (xe - xs, ye - ys)
    
    flag = dy > 0
    dy = abs(dy)
    
    y = ys
    e = 2 * dy - 1
    inc = 2 * dy
    unit = 2 * dx
    
    for s in xrange(xs, xe):
        put(s, y)
        e += inc
        if e > unit:
            e -= unit
            if flag:
                y += 1
            else:
                y -= 1
