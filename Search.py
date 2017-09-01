import random, math

def hillClimbing(y_values):
    current = random.randint(0,200)
    keepRunning = True
    while (keepRunning):
        if (y_values(current) < y_values(current + 1)):
            current += 1
        elif (y_values(current) < y_values(current - 1)):
            current -= 1
        else:
            keepRunning = False

        # print (current, '\t', y_values(current))
    return current

def func(x):
    return 100* math.sin(x/5) + x



def simulatedAnnealing():
    pass

def randomizedHillClimbing(func):
    og = hillClimbing(func)
    for _ in range(random.randint(7,12)):
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
