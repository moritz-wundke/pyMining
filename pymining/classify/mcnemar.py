#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Mc Nemmat tests module.

import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

def McNemar(predF, predG, classes):
    if compare(predF, predG):
        return False

    f = predF != classes
    g = predG == classes
    A = float(sum(map(lambda x, y: x and y, f, g)))
    f = predG != classes
    g = predF == classes
    B = float(sum(map(lambda x, y: x and y, f, g)))

    t = (abs(A - B) - 1) ** 2 / (A + B)
    return t > 3.842

def McNemarWikipedia(predF, predG, classes):
    if compare(predF, predG):
        return False
        
    b = float(len(list(filter(lambda x: (predG[x]=='0') and (predF[x]=='1'), range(len(predG))))))
    c = float(len(list(filter(lambda x: (predG[x]=='1') and (predF[x]=='0'), range(len(predG))))))
    t = (b - c) ** 2 / (b + c)
    return t > 3.842