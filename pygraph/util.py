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
        
def printGGui(graph, cmap="Greys_r"):
    plt.imshow(graph, cmap=cmap)
    plt.show()
    
def saveG(path, graph, cmap="Greys_r"):
    plt.imsave(path, graph, cmap=cmap)
    
def enLarge(graph, scale=10):
    shape = tuple(scale * s for s in graph.shape)
    g = np.zeros(shape=shape)
    
    (h, w) = graph.shape
    for y in xrange(h):
        for x in xrange(w):
            g[y*scale:(y+1)*scale,x*scale:(x+1)*scale] = graph[y,x]
    return g

def pointsToEdges_gen(points):
    len_points = len(points)
    for i in xrange(len_points):
        yield (points[i], points[(i+1) % len_points])

def pointsToEdges(points):
    return list(pointsToEdges_gen(points))

def transformPoints(points, t):
    return [t(p) for p in points]
