#! /usr/bin/env python
# -*- coding: utf-8 -*-
# CL functions

from functools import reduce

def deuclideanCL(x, y):
   return sum(map(lambda a, b: (float(a) - float(b)) ** 2.0,
                  x[1], y)) ** 0.5
 
def classifyCL(t):
   ds = list(map(deuclideanCL, centroids,
                 [t for x in range(len(centroids))]))
   return min([(ds[i], centroids[i][0])
               for i in range(len(centroids))],
              key=lambda x: x[0])[1]

def calcCentroids(classe, t):
   filt = list(filter(lambda x: x[0] == x[1],
                    [(classesTrain[i], classe, t[i])
                     for i in range(len(t))]))
   transp = list(zip(*[filt[i][2] for i in range(len(filt))]))
   return (classe,
           list(map(lambda l: reduce(lambda a, b:
                                     float(a) + float(b),
                                     l) / classes[classe], transp)))