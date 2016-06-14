# -*- coding: utf-8 -*-

import numpy as np
from pygraph.circle import mkCircle
import matplotlib.pyplot as plt
from pygraph.linestyle import *
from pygraph.util import enLarge, saveG


def job(fname, lstyle):
    g = np.zeros((120, 160))

    mkCircle(g, (80, 60), 50, lstyle)

    saveG(fname, g)
    fname = "%s-large.%s" % (fname[0:fname.find(".")], fname[fname.find(".")+1:])
    saveG(fname, enLarge(g, 5))

job("circle.png", None)
job("circle-solid.png", SolidLineStyle())
job("circle-dashed.png", DashedLineStyle())
job("circle-dotted.png", DottedLineStyle())
