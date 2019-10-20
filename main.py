import utils 
import numpy
from ant import Ant

# punkt startowy ze wzgledu na numer indeksu 3 – B

A = [1,2]
B = [3,1]
C = [3,6]
D = [6,7]
E = [5,2]

nodes = [[1,2],[3,1],[3,6],[6,7],[5,2]]

alfa = 1 
beta = 1 
transition_probabilities=[]
tau = []
ants = []


for city in nodes:
    for city2 in nodes:
        if city != city2:        
            single_route = [city , city2]
            if single_route not in tau:
                single_route[0], single_route[1] = single_route[1] , single_route[0]
                if single_route not in tau:
                    tau.append(single_route)

print("===============================")

for city in tau:
    print (city)






for i in range(10):
    ants.append( Ant( nodes ))


for ant in ants:
    current_city = ant.current_location
    
    for city in ant.route:
        denominator = 0
        numerator = (pow(tau[current_city][city],alpha)*(eta[current_city][city], beta))
        for city in ant.route:
            denominator += (pow(tau[current_city][city],alpha)*(eta[current_city][city], beta))
        
        p_ij = numerator/float(denominator)
        transition_probabilities.append(p_ij)
    
    next_city = numpy.random.choice(ant.route, 1, transition_probabilities)  
    print(next_city)