from math import sqrt

l=[199, 200, 201, 202, 203, 204]
h=200

def mean(l):
    return float(sum(l)) / len(l)

def var(l):
    m = mean(l)
    return sum([(x - m) ** 2 for x in l]) / len(l)

def factor(l):
    return 1.96

def conf(l):
    return factor(l) * sqrt(var(l) / len(l))

# Function of a Hypothesis test example
def test(l, h):
    m = mean(l)
    c = conf(l)
    return abs(h - m) <= c

print(mean(l))
print(conf(l))
print(test(l, h))