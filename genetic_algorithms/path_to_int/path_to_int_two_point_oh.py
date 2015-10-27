import random as r

population = []
GOAL = 200

def init_pop(size):
    for i in range(size):
        population.append(r.randrange(0, 4294967295))

def decode(chromosome):
    def first_number(c):
        return (c & 255)
    def second_number(c):
        return (c & 65280 >> 8)
    def third_number(c):
        return (c & 16711680 >> 16)
    def fourth_number(c):
        return (c & 4278190080 >> 24)
    return first_number(chromosome) + second_number(chromosome) + third_number(chromosome) + fourth_number(chromosome)

def fitness(chromosome):
    pass

def select_partner(population):
    pass

def crossover(parents):
    def get_first_half(c):
        return (c & 65535)
    def get_second_half(c):
        return (c & 4294901760 >> 16)
    male_first_half = get_first_half(parents[0])
    male_second_half = get_second_half(parents[0])
    female_first_half = get_first_half(parents[1])
    female_second_half = get_second_half(parents[1])

def mutate(chromosome):
    pass

def main(goal):
    pass
