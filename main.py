import utils 
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

# dist = utils.count_distance( A , B )

a = Ant(nodes)
a.run( )

