# Return the probability of flipping a coin
def flip_twice(p):
    return p * p

def flip_thrice(p):
    return 3 * p * (1 - p) * (1 - p)

#Return the probability of flipping one head each from two coins
def flip_two_coins(p1, p2):
    return p1 * p2

#Two coins have probabilities of heads of p1 and p2
#The probability of selecting the first coin is p0
#Return the probability of a flip landing on heads
def flip(p0, p1, p2):
    return p0 * p1 + (1 - p0) * p2


# Calculate the probability of a positive result given that
#p0 = P(C) - probability
#p1 = P(Positive|C) - sensitivity
#p2 = P(Negative|Not C) - specitivity
def positive_result_probability(p0, p1, p2):
    return p0 * p1 + (1 - p0) * (1 - p2)


'''
Example of the Bayes Rule on positive result
'''
#Return the probability of A conditioned on B given that 
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2 
def bayes_rule_positive(p0, p1, p2):
    return p0 * p1 / (p0 * p1 + (1 - p0) * (1 - p2))

'''
Example of the Bayes Rule on negative result
'''
#Return the probability of A conditioned on Not B given that 
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2 
def bayes_rule_negative(p0, p1, p2):
    return p0 * (1 - p1) / (p0 * (1 - p1) + (1 - p0) * p2)

print(bayes_rule_negative(0.1, 0.9, 0.8))
