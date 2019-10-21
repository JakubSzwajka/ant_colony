import utils 
import numpy
import city
import route
from ant import Ant

# punkt startowy ze wzgledu na numer indeksu 3 – B

A = [1,2]
B = [3,1]
C = [3,6]
D = [6,7]
E = [5,2]

# nodes = [[1,2],[3,1],[3,6],[6,7],[5,2]]
nodes = [A,B,C,D,E]

alpha = 1 
beta = 1 
transition_probabilities=[]
tau = []
eta = []
ants = []
cities = []
numerator = 1

for node in nodes:
    cities.append( city.City(numerator , node[0], node[1] ))
    numerator += 1

# for city in cities:
#     print(city.index , city.x , city.y )

for city in cities: 
    city.add_cities( cities )

# for city in cities:
#     print(city.my_cities)

# for city in cities:
#     for city2 in cities:
#         if city != city2:        
#             single_route = route.Route(city.index, city2.index)#[city.index , city2.index]
#             if single_route not in tau:
#                 single_route.cityA, single_route.cityB = single_route.cityB , single_route.cityA
#                 if single_route not in tau:
#                     tau.append(single_route)

print("========================================================")

for route in tau:
    print (route.cityA , route.cityB)

for i in range(1):
    ants.append( Ant( cities ))

for ant in ants:
    ant.run()

# for ant in ants:
#     current_city = ant.current_location
    
#     for city in ant.route:
#         denominator = 0
#         numerator = (pow(tau[current_city][city],alpha)*(eta[current_city][city], beta))
#         for city in ant.route:
#             denominator += (pow(tau[current_city][city],alpha)*(eta[current_city][city], beta))
        
#         p_ij = numerator/float(denominator)
#         transition_probabilities.append(p_ij)
    
#     next_city = numpy.random.choice(ant.route, 1, transition_probabilities)  
#     print(next_city)