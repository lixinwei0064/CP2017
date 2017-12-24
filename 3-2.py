import math
import random
def foverg(x):
    return math.pow(x,2.5)
def randometa():
    a = -math.log(1-random.random())
    return a
Sum = 0.
for i in range(1000000):
    Sum += foverg(randometa())
print Sum/1000000.
Sum = 0.
for i in range(100000):
    Sum += foverg(randometa())
print Sum/100000.
Sum = 0.
for i in range(10000):
    Sum += foverg(randometa())
print Sum/10000.
'''Output
3.31390213752
3.32196981219
3.2751089419
The exact value is 
3.32335
'''
