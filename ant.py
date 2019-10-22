
import utils
import random
import city
import numpy

class Ant( ):
    def __init__ (self, nodes):
        self.not_visited_locations = []
        self.all_loc_visited = False
        self.distance_travelled = 0.0
        self.route = nodes
        self.current_location = self.route[0]
        self.next_location = self.route[0]
        self.alpha = 1 
        self.beta = 1 
        self.transition_probabilities=[]
        
    def run(self):
        self.not_visited_locations = self.route
        # print( self.not_visited_locations )

        # while len(self.not_visited_locations) > 1:
        for i in range(len(self.route)): 
            self.next_location = self.find_path( )
            if self.current_location != self.next_location:
                self.go_to(self.current_location , self.next_location)  
        # print( "distance travelled" , self.distance_travelled )


    def find_path(self):
        for city in self.route:
            denominator = 0
            numerator = (pow(utils.sum_pheromone(self.route, self.current_location , city), self.alpha)* (pow(1/utils.count_distance(self.current_location , city), self.beta)))
            for city in self.route:
                denominator += (pow(utils.sum_pheromone(self.route, self.current_location , city), self.alpha)* (pow(1/utils.count_distance(self.current_location , city), self.beta)))
           
            p_ij = numerator / float(denominator)
            self.transition_probabilities.append(p_ij)
        next_city = numpy.random.choice(self.route, 1 , self.transition_probabilities )
        return next_city

    def go_to(self, current_location , next_location):
        self.distance_travelled = self.distance_travelled + utils.count_distance( current_location, next_location)
        self.current_location.set_pheromone_to_city(next_location , 1 / utils.count_distance( current_location, next_location))
        self.current_location = next_location

    def return_cities(self):
        # for city in self.route:
            # print(city.index)

        return self.route

    def set_cities(self, cities):
        self.route = cities




# city_to_go = city.City(0,0,0)
#         while True:
#             city_to_go = random.choice( self.route)
#             if city_to_go.visited == False:
#                 break
#         return city_to_go




