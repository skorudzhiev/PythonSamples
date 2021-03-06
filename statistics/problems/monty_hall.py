from random import randint

N = 1000

# The Monty Hall problem with guessing the Doors :)
# involving two trials which improves the probability to 2/3 given the range of N
def simulate(N):
    K = 0
    for i in range(N):
        truth = randint(1, 3)
        guess1 = randint(1, 3)

        if truth == guess1:
            monty = randint(1, 3)
            while monty == truth:
                monty = randint(1, 3)
        else:
            monty = 6 - truth - guess1

        guess2 = 6 - guess1 - monty
        if guess2 == truth:
            K = K + 1
    return float(K) / float(N)

print(simulate(N))