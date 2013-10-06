#! /usr/bin/env python
# Common methods to calculate distance between data sets

def euclidean_dist(dic1, dic2):
    """Compute the sum of squares of the elements common
    to both dictionaries"""
    return sqrt(sum([pow(dic1[elem]-dic2[elem], 2)
                for elem in dic1 if elem in dic2]))

def euclidean_similarity(dic1, dic2):
    """Calculate the euclidean similarity."""
    return 1/(1+euclidean_dist(dic1, dic2))

def pearson_coeff(dic1, dic2):
    """Retrieve the elements common to both dictionaries"""
    commons  = [x for x in dic1 if x in dic2]
    nCommons = float(len(commons))

    # If there are no common elements, return zero; otherwise
    # compute the coefficient
    if nCommons==0:
        return 0

    # Compute the means of each dictionary
    mean1 = sum([dic1[x] for x in commons])/nCommons
    mean2 = sum([dic2[x] for x in commons])/nCommons

    # Compute numerator and denominator
    num  = sum([(dic1[x]-mean1)*(dic2[x]-mean2) for x in commons])
    den1 = sqrt(sum([pow(dic1[x]-mean1, 2) for x in commons]))
    den2 = sqrt(sum([pow(dic2[x]-mean2, 2) for x in commons]))
    den  = den1*den2

    # Compute the coefficient if possible or return zero
    if den==0:
        return 0

    return num/den