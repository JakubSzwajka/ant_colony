
import math


def count_distance( point_a, point_b):
    
    if point_a == point_b:
        return 1 
    else:
        distance = math.sqrt( pow(point_b.y -point_a.y, 2 ) + pow( point_b.x - point_a.x ,2) ) 
        return distance

def sum_pheromone(cities, city_from , city_to ):
    pheromone = 0
    for city in city_from.my_cities:
        if city[0] == city_to:
            pheromone += city[1]

    for city in city_to.my_cities:
        if city[0] == city_from:
            pheromone += city[1]

    return pheromone
        