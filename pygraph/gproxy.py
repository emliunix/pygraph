# -*- coding: utf-8 -*-

# Unable to implement
# slice赋值时因为x或y的值在转换时依赖于y或x，导致无法简单转换边界值
# 而是需要转换枚举出的所有值。这意味着直接通过proxy来实现转换没有效率可言
# class GraphProxy():
#     def __init__(self, g, transform):
#         self.g = g
#         self.t = transform

#     def __getitem__(self, coord):
#         pass

#     def __setitem__(self, coord, val):
#         pass

#     # def __getslice__(self, start, end):
#     #     pass

#     # def __setslice__(self, start, end, val):
#     #     pass
