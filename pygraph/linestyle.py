# -*- coding: utf-8 -*-

class LineStyle:
    def inc(self):
        raise NotImplementedError()

    def p(self):
        raise NotImplementedError()

class SolidLineStyle(LineStyle):
    def inc(self):
        pass
    def p(self):
        return True

class DashedLineStyle(LineStyle):
    def __init__(self):
        self.tick = 0
        self.value = [1,1,1,1,0,0,1,0,0]

    def inc(self):
        self.tick = (self.tick + 1) % len(self.value)

    def p(self):
        return self.value[self.tick]

class DottedLineStyle(object):
    def __init__(self):
        self.tick = 0
        self.value = [1,1,0,0]

    def inc(self):
        self.tick = (self.tick + 1) % len(self.value)

    def p(self):
        return self.value[self.tick]