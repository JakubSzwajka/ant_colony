
import utils
import random

class Ant( ):
    def __init__ (self, nodes):
        self.not_visited_locations = []
        self.all_loc_visited = False
        self.distance_travelled = 0.0
        self.route = nodes
        self.location = self.route[0]
        self.next_location = self.route[0]
        
    def run(self):
        self.not_visited_locations = self.route
        print( self.not_visited_locations )
        while self.not_visited_locations:
           # while set(self.next_location) & set(self.location):
            self.next_location = self.find_path( )
            self.go_to(self.location , self.next_location)

        self.all_loc_visited = True
        print( self.distance_travelled )

    def find_path(self):
        return random.choice( self.not_visited_locations )


    def go_to(self, location , next_location):
        self.distance_travelled = self.distance_travelled + utils.count_distance( location , next_location)
        # print ( location )
        # print ( next_location )
        # print ( self.not_visited_locations )
        if location in self.not_visited_locations:
            self.not_visited_locations.remove(location)
        self.location = next_location


