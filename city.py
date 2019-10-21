

class City( ):
    def __init__(self, ind, x , y):
        self.index = ind
        self.x = x
        self.y = y 
        self.my_cities = []

    def add_cities( self, cities):
        # print("miasto:" , self.index)
        for city in cities:
            if city.index != self.index:
                # print(city.index)
                route = [city , 0 ]
                self.my_cities.append( route )