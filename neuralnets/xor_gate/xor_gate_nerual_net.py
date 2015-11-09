#!/usr/bin/python
# coding: utf-8

# #GA Training an Artificial Neural Network

# ###Neuron
#     - in: list of weights + thresholds
#     - out: 1 or o


class Neuron(object):

    def __init__(self, set_of_input_weights, set_of_inputs, threshold):

        self.threshold = threshold

        self.set_of_input_weights = set_of_input_weights
        self.set_of_inputs = set_of_inputs
        self.num_of_inputs = len(self.set_of_inputs)

    def output(self):
        length = self.num_of_inputs
        activation = 0
        output = 0
        for i in range(length):
            activation += self.set_of_input_weights[i] * self.set_of_inputs[i]
        if activation > self.threshold:
            output = 1
        return output

# ###Initialize Random Population

import random as r

def init_population(pop_size):
    population = []
    for _ in xrange(pop_size):
        chrome = []
        for i in range(19):
            chrome.append(r.randrange(-255, 255))
        population.append(chrome)
    return population


# ###Run the Network
#
# #### Fitness
#         - in: weights[13] + thresholds[6]
#         - out: 10 if answer else int in range from 6 - 9

def fitness(chrome):
    weights = chrome[:13]
    thresholds = chrome[13:]
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    results = [0, 1, 1, 0]
    value = 0
    for i in range(4): # four posssible right answers
        if run_network(weights, thresholds, inputs[i]) == results[i]:
            value += 1
    return (10 - abs(value - 4))

def run_network(weights, thresholds, inputs):
    n0 = Neuron([weights[0], weights[3]], inputs, thresholds[0])
    n1 = Neuron([weights[1], weights[2]], inputs, thresholds[1])
    n2 = Neuron([weights[4], weights[7]], [n0.output(), n1.output()], thresholds[2])
    n3 = Neuron([weights[5], weights[8]], [n0.output(), n1.output()], thresholds[3])
    n4 = Neuron([weights[6], weights[9]], [n0.output(), n1.output()], thresholds[4])
    n5 = Neuron(
        [weights[10], weights[11], weights[12]],
        [n2.output(), n3.output(), n4.output()], thresholds[5])
    return n5.output()

def average_fitness(population):
    """
    in: population
    out: sum of all fitness scores / length of population
    """
    fits = [fitness(x) for x in population]
    return (sum(fits)/len(fits))

def max_fitness(population):
    fits = [fitness(x) for x in population]
    return max(fits)

def is_solution(chrome):
    if fitness(chrome) == 10:
        return True
    return False

def select_partner(population):
    """
    in: population
    out: index of population selected for breeding
    method: roulette
    """
    fits = [fitness(chrome) for chrome in population]
    totals = []
    running_total = 0
    for f in fits:
        running_total += f
        totals.append(running_total)
    rnd = r.random() * running_total
    for i, t in enumerate(totals):
        if rnd < t:
            return population[i]

def crossover(p1, p2):
    """
    in: parents [2]
    out: children [1]
    rate: 0.5
    """
    yes = r.randrange(0, 1)
    if yes:
        c = p1[:9] + p2[9:]
        return c
    elif not yes:
        c = r.choice([p1, p2])
        return c

def mutate(chromosome):
    """
    in: chromosome
    out: mutated chromosome
    rate: 1
    *
      note if rate is 0.5 takes significantly
      longer to find solution.
    *
    """
    value_to_mutate = r.randrange(0, 18)
    chromosome[value_to_mutate] = r.randrange(-255, 255)
    return chromosome

def create_new_child(chromosome, population):
    parent_one, parent_two = chromosome, select_partner(population)
    crossed_child = crossover(parent_one, parent_two)
    mutated_child = mutate(crossed_child)
    return mutated_child

def generations():
    gen = 0
    population_size = 50
    population = init_population(population_size)
    # for _ in xrange(gen_size): # generations
    while True:
        temp_pop = []
        for chrome in population:
            if is_solution(chrome):
                print "SOLUTION FOUND"
                print "Tried {0} different weights and threshold combinations.".format(gen * population_size)
                print "Result obtained in {0} generations".format(gen)
                return
            temp_pop.append(create_new_child(chrome, population))
        gen += 1
        print "Generation: ", gen
        print "Avergage Fitness: ", average_fitness(population)
        print "Maximum Fitness: ", max_fitness(population)
        print "\n"
        population = temp_pop

generations()
