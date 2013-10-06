#! /usr/bin/env python
# Rating related methods. Used in some activities

from math import sqrt

# ------------------------------------------
# TODO: Use methods from pymining.utils.dist
# ------------------------------------------

def euclidean_dist(dic1, dic2, term='eval'):
    """Calculate the euclidean distance between two dictionaries.
    Each dictionary should use the same evaluation item."""
    return sqrt(sum([pow(dic1[elem][term]-dic2[elem][term], 2)
                 for elem in dic1 if elem in dic2]))

def euclidean_similarity(dic1, dic2, term='eval'):
    """Calculate the euclidean similarity.
    Each dictionary should use the same evaluation item."""
    return 1/(1+euclidean_dist(dic1, dic2, term))

def pearson_coeff(dic1, dic2, term='eval'):
    """Calculate the pearson coefficient between two rating dictionaries.
    Each dictionary should use the same evaluation item."""
    # Get common elemnts
    commons  = [x for x in dic1 if x in dic2]
    n_commons = float(len(commons))

    # Nothing in common? Just return 0
    if n_commons==0:
        return 0

    # Calculate both means
    mean1 = sum([dic1[x][term] for x in commons])/n_commons
    mean2 = sum([dic2[x][term] for x in commons])/n_commons

    # Calculate numerator and denominator
    num  = sum([(dic1[x][term]-mean1)*(dic2[x][term]-mean2) for x in commons])
    den1 = sqrt(sum([pow(dic1[x][term]-mean1, 2) for x in commons]))
    den2 = sqrt(sum([pow(dic2[x][term]-mean2, 2) for x in commons]))
    den  = den1*den2

    # Prevent zero devition
    if den==0:
        return 0

    return num/den

# NOTE: Taken from 2.6_WeightedRatings.py
# Produces a sorted list of weighted ratings from a dictionary of
# user ratings and a user id.
# You can choose the function of similarity between users.
def weightedRating(dictio, user, similarity = pearson_coeff, term='eval'):
    # In the first place a dictionary is generated with the similarities
    # of our user with all other users.
    # This dictionary could be stored to avoid recomputing it.
    simils = {x: similarity(dictio[user], dictio[x], term)
              for x in dictio if x != user}

    # Auxiliary dictionaries {restId: [rating*users similarity]}
    # and {restId: [users similarity]} (numerator and denominator
    # of the weighted rating)
    numerator   = {}
    denominator = {}

    # The ratings dictionary is traversed, while filling the auxiliary
    # dictionaries with the values found.
    for userId in simils:
        for restId in dictio[userId]:
            if not numerator.has_key(restId):
                numerator  [restId] = []
                denominator[restId] = []
            s = simils[userId]
            numerator  [restId].append(dictio[userId][restId][term]*s)
            denominator[restId].append(s)

    # Compute and sort weighted ratings    
    result = []
    for restId in numerator:
        s1 = sum(numerator  [restId])
        s2 = sum(denominator[restId])
        if s2 == 0:
            mean = 0.0
        else:
            mean = s1/s2
        result.append((restId,mean))

    result.sort(key = lambda x: x[1], reverse=True)
    return result
