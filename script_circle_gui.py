# -*- coding: utf-8 -*-

from pygraph.circle import mkCircle
from pygraph.linestyle import *
from pygraph.util import enLarge, printGGui, mkGraph


def job(lstyle):
    g = mkGraph((800, 600))

    mkCircle(g, (400, 300), 250, lstyle)
    printGGui(g, cmap="Greys")

job(SolidLineStyle())
