# -*- coding: utf-8 -*-

from __future__ import print_function
from pygraph.line2 import mkLine
from pygraph import util

g = util.mkGraph((80, 60))
ends = [
    (20, 10), (20, -10),
    (10, 20), (10, -20), 
    (-10, 20), (-10, -20), 
    (-20, 10), (-20, -10)
]

tends = [(x[0] + 40, x[1] + 30) for x in ends]

for end in tends:
    mkLine(g, (40, 30), end)
    
mkLine(g, (10, 20), (60, 50))

util.saveG("line2.png", util.enLarge(g))