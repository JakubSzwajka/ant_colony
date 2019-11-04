
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
        self.current_location = numpy.random.choice(self.route) #self.route[0]
        self.start_location = self.route.index(self.current_location)
        self.next_location = self.route[self.start_location]
        self.alpha = .5
        self.beta = 1.2 #1.2
        self.memory = []
        # self.transition_probabilities=[]
        
    def run(self):
        self.not_visited_locations = self.route
        
        # for cit in self.not_visited_locations:
        #     print( cit.index)
        #     print( cit.my_cities )
        while True:
        # for i in range(len(self.route)): 
            self.current_location.visited = True
            # self.not_visited_locations.remove(self.current_location)
            self.memory.append(self.current_location.index)
            self.next_location = self.find_path( )
            # print('JESTEM W: ', self.current_location)
            # print('Z tego miasta widze: ', self.current_location.my_cities )
            # print('IDE DO: ' , self.next_location)
            if self.all_loc_visited == True or self.next_location == None:
                # print('point')
                # print('IDE NA POCZATEK DO: ', self.route[self.start_location])
                self.go_to( self.current_location, self.route[self.start_location] )
                self.memory.append(self.current_location.index)
                break

            if self.current_location != self.next_location:
                # print( self.current_location , self.next_location)
                self.go_to( self.current_location , self.next_location)  

    def find_path(self):

        attractiveness = dict()
        sum_total = 0.0
        #for each possible location, find its attractiveness (it's (pheromone amount)*1/distance [tau*eta, from the algortihm])
        #sum all attrativeness amounts for calculating probability of each route in the next step
        for possible_next_location in self.not_visited_locations:
            if possible_next_location.visited == False:
                #NOTE: do all calculations as float, otherwise we get integer division at times for really hard to track down bugs
                pheromone_amount = float(utils.sum_pheromone(possible_next_location , self.current_location))
                distance = float(utils.count_distance(possible_next_location , self.current_location))
                
                #tau^alpha * eta^beta
                attractiveness[possible_next_location] = pow(pheromone_amount, self.alpha)*pow(1/distance, self.beta)
                sum_total += attractiveness[possible_next_location]
          
            # if sum_total == 0.0:
            #     def next_up(x):
            #         import math
            #         import struct
            #         # NaNs and positive infinity map to themselves.
            #         if math.isnan(x) or (math.isinf(x) and x > 0):
            #             return x
            #         # 0.0 and -0.0 both map to the smallest +ve float.
            #         if x == 0.0:
            #             x = 0.0
            #         n = struct.unpack('<q', struct.pack('<d', x))[0]
                
            #         if n >= 0:
            #             n += 1
            #         else:
            #             n -= 1
            #         return struct.unpack('<d', struct.pack('<q', n))[0]
                
            #     for key in attractiveness:
            #         attractiveness[key] = next_up(attractiveness[key])
            #     sum_total = next_up(sum_total)
        
        import random
        toss = random.random()
        
        cummulative = 0
        
        self.all_loc_visited = True
        for possible_next_location in attractiveness:
            if possible_next_location.visited == False:
                self.all_loc_visited = False
                weight = (attractiveness[possible_next_location] / sum_total)
                if toss <= weight + cummulative:
                    # print(possible_next_location)
                    return possible_next_location
                cummulative += weight
    

    def go_to(self, current_location , next_location):
        self.distance_travelled = self.distance_travelled + utils.count_distance( current_location, next_location)
        self.current_location.set_pheromone_to_city(next_location , 1000 / utils.count_distance( current_location, next_location))
        self.current_location.visited = True
        self.current_location = next_location
        

    def return_cities(self):
        return self.route

    def set_cities(self, cities):
        self.route = cities

    def get_memory(self):
        return self.memory, self.distance_travelled

