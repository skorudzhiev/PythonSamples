import random
from math import sqrt
from plotting import *

# Convertions to float are used in the current scenario 
# for more precise calculations. 


def mean(data):
    return float(sum(data)) / len(data)

def variance(data):
    mu = mean(data)
    return sum( [(x - mu) ** 2 for x in data]) / len(data)

def flip(N):
    return [random.random() > 0.5 for x in range(N)]

def sample(N):
    return [mean(flip(N)) for x in range(N)]

N = 1000
outcomes = sample(N)
histplot(outcomes,nbins=30)

#print(mean(f))