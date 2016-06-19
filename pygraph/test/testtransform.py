# -*- coding: utf-8 -*-

import unittest
import numpy.matlib as mt
from pygraph.transform import Translate, Symmetric

class TestTransform(unittest.TestCase):
    def test_translate(self):
        t = Translate(1, 2)
        m = mt.mat('1 0 0; 0 1 0; 1 2 1')
        self.assertTrue((t.mat == m).all())

    def test_symmetric(self):
        v = Symmetric(vertical=True).mat
        h = Symmetric(horizontal=True).mat
        f = Symmetric(fortyfive=True).mat
        ev = mt.mat('1 0 0; 0 -1 0; 0 0 1')
        eh = mt.mat('-1 0 0; 0 1 0; 0 0 1')
        ef = mt.mat('0 1 0; 1 0 0; 0 0 1')

        self.assertTrue((v == ev).all(), str(v))
        self.assertTrue((h == eh).all(), str(h)) 
        self.assertTrue((f == ef).all(), str(f)) 
