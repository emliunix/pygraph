# -*- coding: utf-8 -*-

from pygraph.floodfill import floodFill
from pygraph.circle import mkCircle
from pygraph.util import mkGraph, enLarge, printGGui

shape = (800, 600)
g = mkGraph(shape)

mkCircle(g, (400, 300), 200)
floodFill(g, (400, 300))

printGGui(g, cmap="Greys")
