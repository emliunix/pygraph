# -*- coding: utf-8 -*-

from pygraph.transform import Transform

t = Transform()
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
