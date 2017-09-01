import random, math

def hillClimbing(y_values):
    current = random.randint(0,99)
    keepRunning = True
    while (keepRunning):
        if y_values(current) < y_values((current + 1)%100):
            current = (current + 1) % 100
        elif y_values(current) < y_values((current - 1)%100):
            current = (current - 1) % 100
        else:
            keepRunning = False

        # print (current, '\t', y_values(current))
    return current

def func(x):
    y = [0, 37, 47, 30, 61, 21, 46, 35, 34, 7, 65, 48, 8, 49, 29, 33, 40, 5, 9, 67, 58, 17, 59, 19, 32, 68, 56, 69, 53,
         48, 99, 116, 92, 71, 65, 91, 112, 109, 70, 120, 106, 86, 105, 76, 108, 51, 90, 68, 101, 81, 50, 105, 97, 80,
         103, 101, 64, 92, 111, 96, 93, 110, 85, 75, 104, 59, 109, 114, 58, 89, 31, 30, 24, 30, 44, 45, 44, 26, 50, 31,
         40, 39, 42, 40, 27, 33, 21, 39, 37, 45, 38, 44, 41, 46, 46, 28, 48, 46, 26, 0]
    # return 100* math.sin(x/10) + x + 40*math.cos(x/2)
    return y[x]
def simulatedAnnealing(func):
    pass

def randomizedHillClimbing(func):
    og = hillClimbing(func)
    for _ in range(random.randint(20,25)):
        current = hillClimbing(func)
        print(current, func(current))
        if (func(current) > func(og)):
            og = current
    return og, func(og)

def gradientDecsent():
    pass

def stochasticGradientDescent():
    pass

print (randomizedHillClimbing(func))
