from plotting import *
from differential_equations_wrapper import *
import math

a=[1,2,3,4,5]
b=[1,2,3,4,5]
h=5

if False:
    print(barchart(a, b, h))

# Plots square root function from 0 to 100
if True:
	@show_plot
	def simple():
	    x_data = numpy.linspace(0., 100., 1000)
	
	    for x in x_data:
	        y = math.sqrt(x)
	        matplotlib.pyplot.scatter(x, y)
	
	    axes = matplotlib.pyplot.gca()
	    axes.set_xlabel('x')
	    axes.set_ylabel('y')
	
	print(simple())