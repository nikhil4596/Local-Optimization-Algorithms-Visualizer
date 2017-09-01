#Implement the main tool
import matplotlib.pyplot as plt
import random

x = [x for x in range(0,100)]
# y = [0] + [random.randint(0,70) for _ in range(1,30)] + [random.randint(50,120) for _ in range(30,70)] \
#     + [random.randint(20,50) for _ in range(70,99)] + [0]
y = [0, 37, 47, 30, 61, 21, 46, 35, 34, 7, 65, 48, 8, 49, 29, 33, 40, 5, 9, 67, 58, 17, 59, 19, 32, 68, 56, 69, 53, 48, 99, 116, 92, 71, 65, 91, 112, 109, 70, 120, 106, 86, 105, 76, 108, 51, 90, 68, 101, 81, 50, 105, 97, 80, 103, 101, 64, 92, 111, 96, 93, 110, 85, 75, 104, 59, 109, 114, 58, 89, 31, 30, 24, 30, 44, 45, 44, 26, 50, 31, 40, 39, 42, 40, 27, 33, 21, 39, 37, 45, 38, 44, 41, 46, 46, 28, 48, 46, 26, 0]


print (sorted(y, reverse=True))
plt.plot(x,y)
plt.show()