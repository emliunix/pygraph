# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp

def mkGraph(shape):
    (w, h) = shape
    return np.zeros((h, w))
    
def printGText(graph):
    for row in graph:
        print(" ".join((str(x) for x in row)))
        
def printGGui(graph):
    plt.imshow(graph, cmp=mp.image.cm.gray)
    
def saveG(path, graph):
    plt.imsave(path, graph, cmap="Greys_r")
    
def enLarge(graph, scale=10):
    shape = tuple(scale * s for s in graph.shape)
    g = np.zeros(shape=shape)
    
    (h, w) = graph.shape
    for y in xrange(h):
        for x in xrange(w):
            g[y*scale:(y+1)*scale,x*scale:(x+1)*scale] = graph[y,x]
    return g