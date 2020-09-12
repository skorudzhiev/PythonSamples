data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]
data2=[1,2,5,10,-20]
data3=[1,2,5,10,-20,5,5]
data4=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]

# Return the mean value of a list of numbers 
# which can be also used to represent
# the Maximum likelihood estimator 
def mean(data):
    return sum(data) / len(data)


# Return the median of a list of numbers 
def median(data):
    sdata = sorted(data)
    index = (len(data) - 1) // 2
    return sdata[index]


# Return the mode of a list of numbers
# being more frequently represented
def mode(data):
    modecnt = 0
    for i in range(len(data)):
        icount = data.count(data[i])
        if icount > modecnt:
            mode = data[i]
            modecnt = icount
    return mode

# Return the variance of a list of numbers
# hence the data spread
def variance(data):
    mu = mean(data)
    return mean([(x - mu) ** 2 for x in data])

print(variance(data4))
