data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]
data2=[1,2,5,10,-20]
data3=[1,2,5,10,-20,5,5]

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

print(mode(data3))