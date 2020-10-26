import ga
import numpy

"""
The y=target is to maximize this equation ASAP:
    y = w1x1+w2x2+w3x3*w4x4+w5x5
    where (x1,x2,x3,x4,x5,x6)=(-4,-12,-3,2,8)
    What are the best values for the 6 weights w1 to w6?
    We are going to use the genetic algorithm for the 
    best possible values after a number of generations.
"""

equation_inputs = [-4, -12, -3, 2, 8]
num_weights = len(equation_inputs)
sol_per_pop = 8
num_parents_mating = 4

# Defining the population size.
pop_size = (
    sol_per_pop,
    num_weights,
)  
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)

num_generations = 30
for generation in range(num_generations):
    print("Generation : ", generation)
    #    the fitness of each chromosome in the population.
    fitness = ga.cal_pop_fitness(equation_inputs, new_population)

    # Selecting the best parents in the population for mating.
    parents = ga.select_mating_pool(new_population, fitness, num_parents_mating)

    # Generating next generation using crossover.
    offspring_size=(pop_size[0] - parents.shape[0], num_weights)
    offspring_crossover = ga.crossover(parents, offspring_size)

    # Adding some variations to the offsrping using mutation.
    offspring_mutation = ga.mutation(offspring_crossover)

    # Creating the new population based on the parents and offspring.
    new_population[0 : parents.shape[0], :] = parents
    new_population[parents.shape[0] :, :] = offspring_mutation

    # The best result in the current iteration.
    print(
        "Best result : ", numpy.max(numpy.sum(new_population * equation_inputs, axis=1))
    )

# Getting the best solution after iterating finishing all generations.
fitness = ga.cal_pop_fitness(equation_inputs, new_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.max(fitness))
best_match_idx = best_match_idx[0][0]
print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])