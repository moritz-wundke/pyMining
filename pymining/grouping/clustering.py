#! /usr/bin/env python
# CLustering related methods. Used in some activities

from math import sqrt
from utils import print_groups

# ------------------------------------------
# TODO: Use methods from pymining.utils.dist
# ------------------------------------------

def euclidean_dist(v1, v2):
    """Calculate the euclidean distance between two points"""
    return sqrt(sum(pow(x-y,2) for x,y in zip(v1,v2)))

def complete_link(points, g1, g2, dist = euclidean_dist):
    """Calculate the maximum distance between two points"""
    maximum = 0.0
    for p1 in g1:
        for p2 in g2:
            distance = dist(points[p1], points[p2])
            if distance > maximum:
                maximum = distance
    return maximum


def simple_link(points, g1, g2, dist = euclidean_dist):
    """Calculate the minimum distance between two points"""
    minimum = float("inf")
    for p1 in g1:
        for p2 in g2:
            distance = dist(points[p1], points[p2])
            if distance < minimum:
                minimum = distance
    return minimum

def join_groups(points, groups, criterion=complete_link,
                  dist=euclidean_dist):
    """Join the two nearest groups together and return
    modificated group set"""
    if len(groups) < 1: return
    
    # Search for the best candidates that have minimal distance
    minimum  = float("inf")
    keys = groups.keys()
    for i in range(len(keys)-1):
        for j in range(i+1, len(keys)):
            distance = criterion(points, groups[keys[i]],
                         groups[keys[j]], dist)
            if distance < minimum:
                minimum    = distance
                candidato = (keys[i], keys[j])

    # The new groups will lay in the slot with the lowest set
    newkey = min(candidato)
    oldKey = max(candidato)
    
    # Extend the new group with the old groups and delete the old group
    groups[newkey].extend(groups[oldKey])
    del(groups[oldKey])
    
def agglomerative_clustering(points, n_groups=4, criterion=complete_link,
                             dist=euclidean_dist):
    """Agglomerative hierarchical clustering: join groups until we get an 
    unique one"""
    # Each point shall be an initial group
    groups = {x:[x] for x in points}

    # The min number of groups is 1
    n_groups = max(1, n_groups)

    # Join all groups until we have more than 1
    while len(groups) > n_groups:
        join_groups(points, groups, criterion, dist)
    return groups
