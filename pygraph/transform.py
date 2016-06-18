# -*- coding: utf-8 -*-

from __future__ import print_function

class Transform:
    def __getitem__(self, *args):
        print(args)

    def __setitem__(self, *args):
        print(args)

    def __getslice__(self, *args):
        print(args)

    def __setslice__(self, *args):
        print(args)

    def __len__(self, *args):
        return 10
