# -*- coding: utf-8 -*-

from __future__ import print_function

INSIDE = 0
TOP = 1
RIGHT = 2
BOTTOM = 4
LEFT = 8

class CohenSutherland(object):

    def __init__(self, x0, y0, x1, y1):
        # 注意y轴朝下
        # bottom left point and top right point
        (x0, x1) = sorted([x0, x1])
        (y1, y0) = sorted([y0, y1])
        self.x_min = x0
        self.x_max = x1
        self.y_max = y0
        self.y_min = y1




    def pointCode(self, point):
        x, y = point
        c = 0
        if   y < self.y_min:
            c |= TOP
        elif y > self.y_max:
            c |= BOTTOM
        if   x < self.x_min:
            c |= LEFT
        elif x > self.x_max:
            c |= RIGHT
        return c

    def clip(self, start, end):
        x0, y0 = start
        x1, y1 = end
        c0, c1 = self.pointCode(start), self.pointCode(end)
        isC0 = False # if true, p0 is outside, inside otherwise

        dx = x1 - x0
        dy = y1 - y0
        def toX(y): return x0 + dx * (y - y0) / dy
        def toY(x): return y0 + dy * (x - x0) / dx

        while True:
            if not (c0 | c1):
                return ((x0, y0), (x1, y1))
            elif c0 & c1:
                return None
            else:
                if c0:
                    code = c0
                    isC0 = True
                else:
                    code = c1
                    isC0 = False
                if   code & TOP:
                    x, y = toX(self.y_min), self.y_min
                elif code & RIGHT:
                    x, y = self.x_max, toY(self.x_max)
                elif code & BOTTOM:
                    x, y = toX(self.y_max), self.y_max
                elif code & LEFT:
                    x, y = self.x_min, toY(self.x_min)

                if isC0:
                    x0, y0, c0 = x, y, self.pointCode((x, y))
                else:
                    x1, y1, c1 = x, y, self.pointCode((x, y))
