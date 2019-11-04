import utils 
# import numpy
import city
import route
from ant import Ant
from operator import itemgetter

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
tau = []
eta = []
ants = []
cities = []
numerator = 1
mem = []
shortest_way = []
shortest_distance = 0.0
shortest_iterator = 1
distances = []
storage = []

for node in nodes:
    cities.append( city.City(numerator , node[0], node[1] ))
    numerator += 1

for city in cities: 
    city.add_cities( cities )

#####################################################################

for i in range(5000):
    ants.append( Ant( cities ))

for ant in ants:
    ant.set_cities(cities)
    # print( 'Obiekt mrówki: ',ant )
    ant.run()
    cities = ant.return_cities()
    mem , distance = ant.get_memory( )
    print('memory: ',mem, '    distance: ', distance)

    utils.pheromone_leak(cities)
    for city in cities:
        city.reset()
    
    storage.append(distance)

    if distance <= shortest_distance or shortest_distance == 0:
        shortest_distance = distance
        shortest_way.append(mem)
        if distance == shortest_distance:
            shortest_iterator += 1
    
    
for item in storage:
    setter = [ item , storage.count(item)]
    if setter not in distances:
        distances.append(setter)

print( ' ===========  ')
print( 'shortest distnce:', shortest_distance , 'times: ' , shortest_iterator)
print( ' ===========  ')


sorted(distances , key=itemgetter(1))

for dist in distances:
    print(dist)

