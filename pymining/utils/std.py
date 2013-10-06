#! /usr/bin/env python
# Common methods used to perfrom standardization on data

from numpy import average, std
def standardize_matrix(m):
    """
    Standardize each colum of the matrix 'm'
    """
    averages = list(map(average, m))
    stds = list(map(std, m))

    return [list(map(lambda x: x if stds[i] == 0.0 else 
    	(x - averages[i]) / stds[i], m[i]))
        for i in range(len(m))]