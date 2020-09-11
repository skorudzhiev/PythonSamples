# Return the probability of flipping a coin
def flip_twice(p):
    return p * p

def flip_thrice(p):
    return 3 * p * (1 - p) * (1 - p)

#Return the probability of flipping one head each from two coins
def flip_two_coins(p1, p2):
    return p1 * p2

#Two coins have probabilities of heads of p1 andd p2
#The probability of selecting the first coin is p0
#Return the probability of a flip landing on heads
def flip(p0, p1, p2):
    return p0 * p1 + (1 - p0) * p2


# print(flip_twice(0.5))
# print(flip_thrice(0.8))
# print(flip_two_coins(0.1, 0.8))
print(flip(0.3, 0.5, 0.9))
