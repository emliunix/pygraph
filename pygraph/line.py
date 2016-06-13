# -*- coding: utf-8 -*-

from __future__ import division

import numpy as np
import util

# x = lambda p: p[0,0]
# y = lambda p: p[0,1]

def x(p): return p[0,0]
def _x(p): return p[0]
def y(p): return p[0,1]
def _y(p): return p[1]

def normalize(target):

    target = np.asmatrix(np.array(target, 'i'))
    mat = np.asmatrix(np.identity(2, 'i')) # id matrix
    
    # if target is on the left of origin
    if x(target) < 0:
        m = np.asmatrix(np.array([[-1, 0], [0, 1]], 'i'))
        mat = mat.dot(m)
        target = target.dot(m)
    # if target is at the bottom of start
    if y(target) < 0:
        m = np.asmatrix(np.array([[1, 0], [0, -1]], 'i'))
        mat = mat.dot(m)
        target = target.dot(m)
    # if k > 1
    if y(target) > x(target):
        m = np.asmatrix(np.array([[0, 1], [1, 0]], 'i'))
        mat = mat.dot(m)
        target = target.dot(m)
        
    return (target, mat)

def mkLine(g, start, stop):
    
    #if k in [-1, 1] step by x
    #else step by y
    (xs, ys) = start

    # set start as origin
    target = (_x(stop) - _x(start), _y(stop) - _y(start))
    
    (target_m, mat) = normalize(target)
    mat = mat.I.astype('i')
    def put(p):
        arr = p.dot(mat).getA1()
        (x, y) = tuple(arr)
        g[ys + y, xs + x] = 1
        
    (dx, dy) = tuple(target_m.getA1())
    
    e = 2 * dy - 1
    inc = 2 * dy
    unit = 2 * dx
    
    curr = np.asmatrix([0, 0], 'i')
    
    for i in xrange(dx):
        put(curr)
        e += inc
        if e > unit:
            e -= unit
            curr[0,1] += 1
        curr[0,0] += 1
            
    return g