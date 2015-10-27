import random as r
import copy


GOAL = 200

def init_pop(size):
    """
    in: desired size of population
    out: first random population
    """
    population = []
    for i in range(size):
        population.append(r.randrange(0, 4294967295))
    print population
    return population

def decode(chromosome):
    """
    in: bitstring
    out: decoded result
    """
    first_number = (chromosome & 255)
    second_number = (chromosome & 65280 >> 8)
    third_number = (chromosome & 16711680 >> 16)
    fourth_number = (chromosome & 4278190080 >> 24)
    print first_number, " + ", second_number, " + ", third_number, " + ", fourth_number
    chrome_sum = first_number + second_number + third_number + fourth_number
    return chrome_sum

def select_partner(population):
    """
    in: population
    out: index of population selected for breeding
    method: roulette
    """
    fits = [fitness(x) for x in population]
    fit_sum = sum(fits)
    rnd = r.randrange(0, fit_sum)
    big_list = []
    for p in population:
        for f in xrange(fitness(p)):
            big_list.append(p)
    print "big_list: ", big_list
    return big_list[rnd]
    

def crossover(parents):
    """
    in: parents [2]
    out: children [2]
    rate: 0.5
    """
    def get_first_half(c):
        return (c & 65535)
    def get_second_half(c):
        return (c & 4294901760 >> 16)
    crossover_decision = r.randrange(0, 1)
    if crossover_decision:
        male_first_half = get_first_half(parents[0])
        male_second_half = get_second_half(parents[0])
        female_first_half = get_first_half(parents[1])
        female_second_half = get_second_half(parents[1])
        children = []
        children.append(male_first_half | female_second_half)
        children.append(female_first_half | male_second_half)
        return children
    else: return parents

def mutate(chromosome):
    """
    in: chromosome
    out: mutated chromosome 
    rate: 0.5
    """
    rand_num = r.randrange(0, 1)
    if rand_num:
        bit_to_flip = r.randrange(0, 31)
        mutated_chrome = chromosome ^ (1 << bit_to_flip)
        return mutated_chrome
    else: return chromosome
    
def fitness(chromosome):
    """
    in: chromosome
    out: 1000 - abs(chromosome - GOAL)
    """
    return 1000 - abs(decode(chromosome) - GOAL)
    
def is_solution(chromosome):
    if decode(chromosome) == GOAL:
        return True
    else: return False
    
def main():
    """
    pop = init_pop
    from 0 to generation do
        new_pop = []
        for p in pop
            if is_solution(p) do
                return p
            parents = [p, select_partner(pop)]
            children = [mutate(crossover(parents))]
            child = best(children)
            new_pop.append(child)
        pop = new_pop
    """
    population = init_pop(50)
    for i in range(100): # generations
        print "generation: ", i
        temp_population = []
        for chromosome in population:
            if is_solution(chromosome):
                print "SOLUTION FOUND"
                print decode(chromosome)
                return chromosome
                break
            parents = [chromosome, select_partner(population)]
            crossed_parents = crossover(parents)
            mutated_child_one = mutate(crossed_parents[0])
            mutated_child_two = mutate(crossed_parents[1])
            if fitness(mutated_child_one) > fitness(mutated_child_one):
                temp_population.append(mutated_child_one)
            elif fitness(mutated_child_one) > fitness(mutated_child_one):
                temp_population.append(mutated_child_two)
        population = temp_population

main()
        
        