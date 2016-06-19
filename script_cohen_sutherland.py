# -*- coding: utf-8 -*-

from pygraph.util import mkGraph, enLarge, printGGui
from pygraph.line2 import mkLine
from pygraph.cohensutherland import CohenSutherland
from pygraph.linestyle import SolidLineStyle, DashedLineStyle
import itertools

solid = SolidLineStyle()
dashed = DashedLineStyle()

shape = (500, 500)
g = mkGraph(shape)

rect = (
    (100, 100),
    (400, 400)
)

cohen = CohenSutherland(*(itertools.chain(*rect)))

lines = [
    ((50, 50), (450, 50)),
    ((50, 50), (250, 250)),
    ((50, 200), (300, 450)),
    ((300, 50), (400, 450)),
    ((375, 150), (375, 250))
]

for i in [100, 400]:
    mkLine(g, (i, 0), (i, 500), lstyle=dashed)
    mkLine(g, (0, i), (500, i), lstyle=dashed)

for l in lines:
    mkLine(g, l[0], l[1], lstyle=dashed)
    l = cohen.clip(*l)
    if l:
        mkLine(g, l[0], l[1], lstyle=solid)

printGGui(g, cmap="Greys")
