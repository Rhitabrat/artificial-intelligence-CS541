from re import A
import numpy as np
import random
import matplotlib.pyplot as plt

POPULATION_SIZE = 10
NUM_OF_ITERATIONS = 10000
NUM_OF_QUEENS = 8


# generate population
arrangements = []

for i in range(POPULATION_SIZE):
    nums = []
    for j in range(8):
        arr = random.randint(1, 8)
        nums.append(arr)
    arrangements.append(nums)


def fitness_score(arrangement):
    score = 0

    for row in range(NUM_OF_QUEENS):
        col = arrangement[row]
        for other_row in range(NUM_OF_QUEENS):
            if other_row == row:
                continue
            if arrangement[other_row] == col:
                continue
            if other_row + arrangement[other_row] == row + col:
                continue
            if other_row - arrangement[other_row] == row - col:
                continue

            score += 1

    return score/2


def select_parent(arrangements):
    fitness_scores = []
    for i in range(4):
        fitness_scores.append(fitness_score(arrangements[i]))

    sum_score = sum(fitness_scores)
    prob = [x / sum_score for x in fitness_scores]

    return prob, max(fitness_scores)


def ga(arrangements):

    best_fitnesses = []

    for i in range(NUM_OF_ITERATIONS):
        # select 2 parents
        parent_scores, best_fitness = select_parent(arrangements)
        best_parent_indices = np.argpartition(parent_scores, -2)[-2:]
        selected_parent_1 = arrangements[best_parent_indices[0]]
        selected_parent_2 = arrangements[best_parent_indices[1]]

        # select random crossover point
        crossover_point = random.randint(0, 7)

        # do the crossover
        offspring_1 = selected_parent_1[:crossover_point] + \
            selected_parent_2[crossover_point:]
        offspring_2 = selected_parent_2[:crossover_point] + \
            selected_parent_1[crossover_point:]

        # do the mutation
        offspring_1[random.randint(0, 7)] = random.randint(1, 8)
        offspring_2[random.randint(0, 7)] = random.randint(1, 8)

        arrangements[best_parent_indices[0]] = offspring_1
        arrangements[best_parent_indices[1]] = offspring_2

        best_fitnesses.append(best_fitness)
        
        if best_fitness==28:
            print("Solution found at i =", i)
            print(arrangements)
            break

    return best_fitnesses


print("Initial")
print(arrangements)
print("Final")
fitnesses = ga(arrangements)
# print(fitnesses)

plt.ylim(0, 28)
plt.xlim(0, NUM_OF_ITERATIONS)
plt.xlabel("Number of generations")
plt.ylabel("Best fitness")
plt.yticks(range(0, 30, 2))

plt.plot(fitnesses, linewidth = '0.75')
plt.show()
