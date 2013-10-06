#! /usr/bin/env python
# Common methods used to perfrom on missing data

from collections import Counter
def mode_missing(l):
    """
    Substitude missing values '?' using the mode of the set
    """
    cl = Counter([l[i] for i in range(len(l)) if (l[i] != '?')])
    moda = float(cl.most_common()[0][0])
    return list(map(lambda x: moda if x=='?' else float(x), l))

from numpy import average
def mean_missing(l):
    """
    Substitude missing values '?' using the mean of the set
    """
    mean = average([l[i] for i in range(len(l)) if (l[i] != '?')])
    return list(map(lambda x: mean if x=='?' else float(x), l))