# -*- coding: utf-8 -*-

from __future__ import print_function

import numpy as np
import numpy.matlib as mt

class Transform(object):
    def __init__(self, mat):
        self.mat = mat

    def __call__(self, (x, y)):
        x, y, i = (mt.mat([x, y, 1]).dot(self.mat)).astype('i').getA1()
        return (x, y)

    def __mul__(self, t):
        return Transform(self.mat * t.mat)

class Translate(Transform):
    def __init__(self, tx, ty):
        t = mt.eye(3, dtype='i')
        t[2,0] = tx
        t[2,1] = ty
        super(Translate, self).__init__(t)

class Symmetric(Transform):
    def __init__(self, vertical=False, horizontal=False, fortyfive=False):
        t = mt.eye(3, dtype=np.int)
        if vertical:
            t = t.dot(mt.mat('1 0 0; 0 -1 0; 0 0 1'))
        if horizontal:
            t = t.dot(mt.mat('-1 0 0; 0 1 0; 0 0 1'))
        if fortyfive:
            t = t.dot(mt.mat('0 1 0; 1 0 0; 0 0 1'))
        super(Symmetric, self).__init__(t)

class Rotate(Transform):
    def __init__(self):
        pass

