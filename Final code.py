# -*- coding: utf-8 -*-
"""
Created on Fri May 17 00:29:56 2019

@author: Ebrahim Amer
"""


import numpy as np
import matplotlib.pyplot as plt
import xlrd 

n = 81
distance_list = []
city_list = []
vertical_list  = []
horizontal_list  = []
performance_list = []



coordinates = xlrd.open_workbook(r"C:\Users\Ebrahim Amer\Desktop\python projects\Final\Coordinates.xlsx")
distancematrix = xlrd.open_workbook(r"C:\Users\Ebrahim Amer\Desktop\python projects\Final\distancematrix.xls")

sheet1 = coordinates.sheet_by_index(0)
sheet2 = distancematrix.sheet_by_index(0)

# DISTANCE 
for i in range(n): 
    for j in range(n):
        value = sheet2.cell_value(i+3,j+2)
        distance_list.append(value)


value = np.arange(0,6562,81)


for i in range(n):
    distance_list[value[i] + i] = 0        

#RESHAPE THE DISTANCE LIST INTO 81 BY 81 MATRIX  
distance_matrix = np.reshape(distance_list,(81,81)) 


    #================================================
    #================================================

# COORDINATES
for i in range (n) : 
    city = sheet1.cell_value(i+1, 1) 
    vert_coor = sheet1.cell_value(i+1, 2)
    horiz_coor = sheet1.cell_value(i+1, 3)
    
    city_list.append(city)
    vertical_list.append(vert_coor)
    horizontal_list.append(horiz_coor)

matrix_total_coordinates = np.zeros((81, 2))

for i in range(81):
    matrix_total_coordinates[i][0] = vertical_list[i]
    matrix_total_coordinates[i][1] = horizontal_list[i]

#TRIP
trip_list = []
for i in range(n):
    trip = distance_matrix[i,:n]
    trip_list.append(trip)

    
shortest_trip = [] 
for i in range(n):
    tr = np.sort(trip_list[i])
    shortest_trip.append(tr)


for i in range(n) :
    plt.plot((horizontal_list[i]), (vertical_list[ i ]), '.-')
    
    #================================================

def get_a_path(n):

    # CREATES RANDOM PATH
    rand_path = np.arange(n)
    np.random.shuffle(rand_path)
    rand_path = np.append(rand_path,rand_path[0])
    return rand_path

def measure_path(path):
#   RETURNS THE TOTAL DISTANCE OF PATH
    def distance(i, j):
        return distance_matrix[i][j]
    total_distance = 0
    for i,j in zip(path[:-1], path[1:]):
        dist = distance(i,j)
        total_distance = total_distance + dist

    return total_distance

def draw_path(path0):

#    DRAWS THE PATH GIVEN AS PARAMETER
    for i,j in zip(path0[:-1],path0[1:]):
        plt.plot([matrix_total_coordinates[i][1],matrix_total_coordinates[j][1]],[matrix_total_coordinates[i][0],matrix_total_coordinates[j][0]],'-o')
    plt.show()
    
def crossover(path1, path2):

#    USES PATH1 AND PATH2 TO GENERATE PATH3 
    path1 = path1[:-1]
    path2 = path2[:-1]
    rand_int = np.random.randint(0,n)
    path3 = np.hstack((path1[:rand_int], path2[rand_int:])) 
    unique, counts = np.unique(path3, return_counts=True)
    dictionary = dict(zip(unique, counts))
    replacewith = []
#    print(unique)
    for i in dictionary:
        if dictionary[i] == 2:
            replacewith.append(i)    
    if len(set(path3))!=len(set(path2)):
        missing = list(set(path1)-set(path3))
        
        for i,j in zip(replacewith,missing):
            if np.random.rand() > 0.5:
                index = np.where(path3 == i)[0][0]
            else:
                index = np.where(path3 == i)[0][1]            
            path3[index] = j
            
#    INTRODUCE RANDOM MUTATION BY SWAPPING TWO POINTS
    if np.random.rand() > 0.1:
        a, b = np.random.randint(0, n, 2)

        path3[a], path3[b] = path3[b], path3[a]
    path3 = np.append(path3, path3[0]) 

    return path3

def get_population_fitness(population):
    
#    RETURNS AN ARRAY THAT STORES THE PERFORMANCE, OF EACH PATH OF A POPULATION
    perf_list = []
    for i in population:
        perf_list.append(measure_path(i))

    return np.array(perf_list)

def sort_population(population):
    
#    SORT THE POPULATION ACCORDING TO ITS PERFORMANCE
    performance = get_population_fitness(population)
    i = np.argsort(performance)

    return population[i]

def create_initial_population(n):

#    CREATES AND SORTS AN INITAL POPULATION OF SIZE n    
    population_list = []
    total_cities = 81
    for i in range(n):
        pop = get_a_path(total_cities)

        population_list.append(pop)
    population_list = np.array(population_list)
    population_list = sort_population(population_list)

    return population_list

population  = create_initial_population(100)

def multiply(population, n):
    
    population = population[:n]
    newpopulation_list = []
    for i in population:
        for j in population:
            newpopulation_list.append(crossover(i, j))
    newpopulation_list = np.array(newpopulation_list)
    newpopulation_list = sort_population(newpopulation_list)

    return newpopulation_list

    #================================================
    #================================================

###### RUNNING THE PROGRAME ######
for i in range(17000):
    print('Number of iteration',i, 'The possible shortest total distance is %5.2f' % measure_path(population[0]))
#    DRAW THE SHORTEST PATH
    draw_path(population[0])
    performance_list.append(measure_path(population[0]))
    plt.plot(performance_list,'.-')
    plt.show() 
    population = multiply(population, 10)

city = population[0]
city = np.delete(city, 81)

for i in(city):
    if city [i] == 5:
        ankara = i

route = np.hstack ((city[ankara:], city[:ankara]))
route = np.append(route,route[0])
print ("The shortest route started from Ankara defined by number of index: ",route) 