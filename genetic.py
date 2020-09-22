import random
import string

POPSIZE = 2048
ELITRATE = 0.10  # elitism rate
MUTATIONRATE = 0.25  # mutation rate
CHARS = string.ascii_letters + string.digits + string.punctuation + string.whitespace


def randstr():
    return "".join([random.choice(CHARS) for i in range(len(TARGET))])


def fitness(value):
    return sum([abs(ord(value[j]) - ord(TARGET[j])) for j in range(len(TARGET))])


def mate(population, buffer):
    esize = int(POPSIZE * ELITRATE)  # 204
    for i in range(esize):  # Elitism
        buffer[i] = population[i]
    for i in range(esize, POPSIZE):  # 204 - 2048
        i1 = random.randint(0, POPSIZE / 2)
        i2 = random.randint(0, POPSIZE / 2)
        spos = random.randint(0, len(TARGET))
        buffer[i] = population[i1][:spos] + population[i2][spos:]  # Mate
        if random.random() < MUTATIONRATE:  # Mutate
            pos = random.randint(0, len(TARGET) - 1)
            buffer[i] = buffer[i][:pos] + random.choice(CHARS) + buffer[i][pos + 1:]


def main(input_string):
    global TARGET
    TARGET = input_string  # computer
    ResultList = []
    population = [randstr() for i in range(POPSIZE)]

    buffer = [randstr() for i in range(POPSIZE)]
    i = 0
    while True:
        i += 1
        population = sorted(population, key=lambda c: fitness(c))
        generation = [i, fitness(population[0]), population[0]]
        ResultList.append(generation)
        if not fitness(population[0]):  # Best match found
            break
        mate(population, buffer)
        population, buffer = buffer, population

    return ResultList
