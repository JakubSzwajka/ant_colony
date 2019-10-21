
import math


def count_distance( point_a, point_b):
    distance = math.sqrt( pow(point_b.y -point_a.y, 2 ) + pow( point_b.x - point_a.x ,2) ) 
    # print(distance)
    return distance; 