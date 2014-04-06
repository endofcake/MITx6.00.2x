import numpy

varlist = [10, 4, 12, 15, 20, 5] 
mean = numpy.mean(varlist)

print(mean)

std = numpy.std(varlist)
print(std)
print(std / mean)