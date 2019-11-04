

class City( ):
    def __init__(self, ind, x , y):
        self.index = ind
        self.x = x
        self.y = y 
        self.my_cities = []
        self.visited = False

    def add_cities( self, cities):
        # print("miasto:" , self.index)
        for city in cities:
            if city.index != self.index:
                # print(city.index)
                route = [city , 1000 ] # 1000 is pheromone 
                self.my_cities.append( route )

    def set_pheromone_to_city(self, city_to, phermonoe ):
        
        # print("index:" , self.index)
        # print("my cities" ,self.my_cities)
        # print(city_to)
        for city in self.my_cities:
            # print(city[0].index)
            # print(city_to.index)
            # print("------")
            if city[0] == city_to:
                # print("znalazlem")
                city[1] += phermonoe

        # print("my cities" ,self.my_cities)
        # print("==========================")

    def reset(self):
        self.visited = False 