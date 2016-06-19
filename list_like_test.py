# -*- coding: utf-8 -*-

from __future__ import print_function
from pygraph.transform import Transform

class Test():
    def __getitem__(self, *args):
        print("getitem: %s" % (str(args), ))
    def __setitem__(self, *args):
        print("setitem: %s" % (str(args), ))
    def __getslice__(self, *args):
        print("getslice: %s" % (str(args), ))
    def __setslice__(self, *args):
        print("setslice: %s" % (str(args), ))
    def __len__(self, *args):
        return 10

t = Test()
t[1]
t[2]
t[-1]
t[1,2]
t[1,2,3]
t[1:1]
t[-1:0]
t[-1:0:3]
t[1:2, 2:3, 3:4]

t[1] = 1
t[2] = 1
t[1,2,3] = 1
t[1:2:-1] = 1
t[1:2] = 1
t[1:2:1, 2:3:2] = 1

t[1, 2:3] = 1
