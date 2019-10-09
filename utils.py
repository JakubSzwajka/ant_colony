
import math


def count_distance( point_a, point_b):
    distance = math.sqrt( pow(point_b[1]-point_a[1], 2 ) + pow( point_b[0]-point_a[0],2) ) 
    return distance; 