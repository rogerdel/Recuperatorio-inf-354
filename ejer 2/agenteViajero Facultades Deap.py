# -*- coding: utf-8 -*-
"""
Created on Mon Dec  21 15:30:26 2020

@author: Roger
"""

import array
import random

import pandas as pd
import numpy as np

from deap import algorithms
from deap import base
from deap import creator
from deap import tools


facultades = ["Agronomia", "Arquitecutra", "Ciencias econimicas", "Ciencias farmaceuticas",
              "Ciencias geologicas", "Ciencias puras y naturales", "Ciencias socilaes", "Derecho", "Humanidades",
              "Ingieneria", "Medicina", "Odontologia", "Tecnonologia"]

distancias = np.array([[0, 11, 5, 40, 58, 77, 58, 73, 38, 19, 27, 91, 82], 
                        [11, 0, 66, 66, 58, 36, 87, 99, 89, 98, 59, 85, 67], 
                        [5, 66, 0, 34, 95, 16, 71, 32, 14, 30, 89, 24, 92], 
                        [40, 66, 34, 0, 31, 89, 67, 5, 79, 10, 66, 78, 90], 
                        [58, 58, 95, 31, 0, 54, 36, 7, 67, 15, 39, 42, 57], 
                        [77, 36, 16, 89, 54, 0, 40, 97, 5, 51, 18, 38, 81], 
                        [58, 87, 71, 67, 36, 40, 0, 36, 20, 59, 20, 28, 12], 
                        [73, 99, 32, 5, 7, 97, 36, 0, 20, 98, 30, 45, 71], 
                        [38, 89, 14, 79, 67, 5, 20, 20, 0, 84, 43, 31, 35], 
                        [19, 98, 30, 10, 15, 51, 59, 98, 84, 0, 100, 34, 95], 
                        [27, 59, 89, 66, 39, 18, 20, 30, 43, 100, 0, 23, 14], 
                        [91, 85, 24, 78, 42, 38, 28, 45, 31, 34, 23, 0, 31], 
                        [82, 67, 92, 90, 57, 81, 12, 71, 35, 95, 14, 31, 0]])

print(distancias)
cantFacultades = len(facultades)


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)

toolbox = base.Toolbox()


toolbox.register("indices", random.sample, range(cantFacultades), cantFacultades)

toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalCamino(individual):
    distanciaGen = distancias[individual[-1]][individual[0]]
    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        distanciaGen += distancias[gene1][gene2]
    
    return distanciaGen,

toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalCamino)

def main():
    random.seed(169)
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    iteraciones = 40
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, iteraciones, stats=stats, halloffame=hof, verbose=True)
    
    return pop, stats, hof

if __name__ == "__main__":
    
    _,_, hof= main()
    data = hof[0]
    
    
    print("Hall of Fame:",data)
    print("Camino optimo: ", end = "\n\t")
    
    
    for i in data:
        print(facultades[i], end = ", " if i != data[len(data)-1] else "\n")
        
    total = 0
    for i in range(len(data)-1):
        total+= distancias[data[i]][data[i+1]]
    total+= distancias[data[0]][data[len(data)-1]];
    print("Menor coste de recorido: ",total)