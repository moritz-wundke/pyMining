#! /usr/bin/env python
# -*- coding: utf-8 -*-
# kNN

def deuclidean(x, y):
   return sum(map(lambda a, b: (float(a) - float(b)) ** 2.0,
                  x, y)) ** 0.5

def count(l):
   p = {}
   for x in l:
      p.setdefault(x, 0)
      p[x] += 1
   return p
 
def kNN(t):
   ds = list(map(deuclidean, train, [t for x in range(len(train))]))
   kcl = count([sorted([(ds[i], classesTrain[i])
                         for i in range(len(train))],
                        key=lambda x: x[0])[i][1]
                 for i in range(k)])
   return max([(x , kcl[x]) for x in kcl.keys()],
              key=lambda x: x[1])[0]