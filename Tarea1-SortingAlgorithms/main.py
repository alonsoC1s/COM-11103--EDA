import time
import random
from Sorting import *
from Movie import *

file = open('movie_titles2.txt', 'r')
output = open('DatosAleatorios.txt', 'w')
arr = []
sorting = Sorting()
for data in file:
    line = data.split(',', 2)
    arr = arr + [Movie(line[0], line[1], line[2][0:len(line[2])-1])]

random.shuffle(arr)
sorting_algorithms = [('mergesort', sorting.mergesort), ('quicksort', sorting.quicksort),
                      ('bubblesort', Sorting().bubblesort), ('selectionsort', Sorting().selectionsort)]

output.writelines('DATOS ALEATORIOS\n')

for n in [10, 100, 1000, 10000, 15000, 17500]:
    output.writelines('\nPara ' + str(n) + ' elementos:\n')
    for algorithm in sorting_algorithms:
        _sorted = arr[:n]
        initial_time = time.clock()
        comparisons = algorithm[1](_sorted)
        runtime = time.clock() - initial_time
        output.writelines(algorithm[0] + " time: " + str(runtime) + ", comparisons: " + str(comparisons) + "\n")
