
import utils
import random
# import numpy as np

class Ant( ):
    def __init__ (self, nodes):
        self.not_visited_locations = []
        self.all_loc_visited = False
        self.distance_travelled = 0.0
        self.route = nodes
        self.current_location = self.route[0]
        self.next_location = self.route[0]
        
    def run(self):
        self.not_visited_locations = self.route
        # print( self.not_visited_locations )

        while self.not_visited_locations:
           # while set(self.next_location) & set(self.current_location):
            self.next_location = self.find_path( )
            if self.current_location != self.next_location or len(self.not_visited_locations) == 1 :
                self.go_to(self.current_location , self.next_location)

        self.all_loc_visited = True        
        print( "distance travelled" , self.distance_travelled )


    def find_path(self):
        return random.choice( self.not_visited_locations)


    def go_to(self, current_location , next_location):
        self.distance_travelled = self.distance_travelled + utils.count_distance( current_location, next_location)
        # print ( current_location )
        # print ( next_location )
        # print ( self.not_visited_locations )
        if current_location in self.not_visited_locations:
            self.not_visited_locations.remove(current_location)
        self.current_location = next_location

    def return_cities(self):
        return self.route

    def set_cities(self, cities):
        self.route = cities




