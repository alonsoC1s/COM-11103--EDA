import time
import plotly
from plotly.graph_objs import Scatter, Figure, Layout
from Sorting import *
from Movie import *

sorting = Sorting()
sorting_algorithms = [('mergesort', sorting.mergesort), ('quicksort', sorting.quicksort),
                      ('bubblesort', sorting.bubblesort), ('selectionsort', sorting.selectionsort),
                      ('insertionsort', sorting.insertionsort)]

file = open('movie_titles2.txt', 'r')
movies = []
for line in file:
    line = line.split(',', 2)
    movies += [Movie(line[0], line[1], line[2][0:len(line[2])-1])]


def run_sorting_algorithms(arr, namePlot):
    x_axis = [10, 100, 1000, 2000, 5000, 10000, 12000, 15000, 17000]
    data_time = []
    data_comparisons = []

    for algorithm in sorting_algorithms:
        time_complexity = []
        number_comparisons = []
        for x in x_axis:
            data = arr[:x]
            initial_time = time.clock()
            number_comparisons += [algorithm[1](data)]
            time_complexity += [time.clock() - initial_time]
        data_time += [Scatter(x=x_axis, y=time_complexity, name=algorithm[0])]
        data_comparisons += [Scatter(x=x_axis, y=number_comparisons, name=algorithm[0])]

    plotly.offline.plot({
        'data': data_time,
        'layout': Layout(title=namePlot, showlegend=True, xaxis=dict(title='Número de datos'), yaxis=dict(title='Tiempo (s)'))
    }, filename='movies_time_{}.html'.format(namePlot.lower().replace(" ", "_")))

    plotly.offline.plot({
        'data': data_comparisons,
        'layout': Layout(title=namePlot, showlegend=True, xaxis=dict(title='Número de datos'), yaxis=dict(title='Número de comparaciones'))
    }, filename='movies_number_comparisons_{}.html'.format(namePlot.lower().replace(" ", "_")))


movies.sort()
run_sorting_algorithms(movies, 'Datos Ordenados')

movies.reverse()
run_sorting_algorithms(movies, 'Orden Inverso')

random.shuffle(movies)
run_sorting_algorithms(movies, 'Orden Aleatorio')