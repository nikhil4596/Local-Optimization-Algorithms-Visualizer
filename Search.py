import math
import random


def hill_climbing(func):
    x = random.randint(0, 99)
    keep_running = True
    while keep_running:
        if func(x) < func((x + 1)):
            x = (x + 1)
        elif func(x) < func((x - 1)):
            x = (x - 1)
        else:
            keep_running = False

            # print (x, '\t', y_values(x))
    return x, func(x)


def operation(x):
    y = [0, 37, 47, 30, 61, 21, 46, 35, 34, 7, 65, 48, 8, 49, 29, 33, 40, 5, 9, 67, 58, 17, 59, 19, 32, 68, 56, 69, 53,
         48, 99, 116, 92, 71, 65, 91, 112, 109, 70, 120, 106, 86, 105, 76, 108, 51, 90, 68, 101, 81, 50, 105, 97, 80,
         103, 101, 64, 92, 111, 96, 93, 110, 85, 75, 104, 59, 109, 114, 58, 89, 31, 30, 24, 30, 44, 45, 44, 26, 50, 31,
         40, 39, 42, 40, 27, 33, 21, 39, 37, 45, 38, 44, 41, 46, 46, 28, 48, 46, 26, 0]
    # return 100* math.sin(x/10) + x + 40*math.cos(x/2)
    return y[x % len(y)]


def simulated_annealing(func):
    x = random.randint(0, 99)
    og = func(x)
    T = 5
    k = 2
    print(x, og, 123)
    while T > math.exp(-1.5):
        new = random.randint(0, 99)
        if func(x) < func(new):
            x = new
        elif math.exp((func(new) - func(x)) / T * 1.0) > random.random():
            x = new
        T = T - 0.02
        k += 1
        if func(x) > og:
            og = func(x)
        print(x, func(x))
    return x, og


def randomized_hill_climbing(func):
    og = hill_climbing(func)[0]
    for _ in range(random.randint(20, 25)):
        current = hill_climbing(func)[0]
        print(current)
        if func(current) > func(og):
            og = current
    return og, func(og)


def main():
    print(simulated_annealing(operation))


main()
