data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]

# Return the mean value of a list of numbers 
# which can be also used to represent
# the Maximum likelihood estimator 
def mean(data):
    return sum(data) / len(data)

print(mean(data1))