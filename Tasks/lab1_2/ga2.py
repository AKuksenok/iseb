# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:07:47 2020

@author: Администратор
"""

import numpy

# y = w1x1+w2x2+w3x3*w4x4+w5x5


def cal_pop_fitness(equation_inputs, pop):
    fitness = list()
    for row in pop:
        pairs = [a * b for a, b in zip(row, equation_inputs)]
        funcResult = pairs[0] + pairs[1] + pairs[2] * pairs[3] + pairs[4]
        fitness.append(funcResult)
    return fitness


def select_mating_pool(pop, fitness, num_parents):
    # Selecting the best individuals in the current
    #  generation as parents for producing the
    #  offspring of the next generation.
    pop_shape = pop.shape[1]
    parents = numpy.empty((num_parents, pop_shape))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    return parents


def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually it is at the center.
    parent1_idx = 0
    parent2_idx = 1
    for k in range(offspring_size[0]):
        crossover_point = numpy.random.randint(0,4)
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring


def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(-4.0, 4.0, 1)
        offspring_crossover[idx, numpy.random.randint(0, 4)] = (
            offspring_crossover[idx, numpy.random.randint(0, 4)] + random_value
        )
    return offspring_crossover
