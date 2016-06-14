# -*- coding: utf-8 -*-

import numpy as np
from pygraph.circle import mkCircle
import matplotlib.pyplot as plt
from pygraph.linestyle import *


def job(fname, lstyle):
    g = np.zeros((120, 160))

    mkCircle(g, (80, 60), 50, lstyle)

    def enlarge(g, scale=10):
        r = np.zeros(tuple(scale * x for x in g.shape))
        for y in xrange(g.shape[0]):
            for x in xrange(g.shape[1]):
                r[y*scale:(y+1)*scale, x*scale:(x+1)*scale] = g[y, x]
        return r

    plt.imsave(fname, g, cmap="Greys_r")
    fname = "%s-large.%s" % (fname[0:fname.find(".")], fname[fname.find(".")+1:])
    plt.imsave(fname, enlarge(g, 5), cmap="Greys_r")

job("circle.png", None)
job("circle-solid.png", SolidLineStyle())
job("circle-dashed.png", DashedLineStyle())
job("circle-dotted.png", DottedLineStyle())
