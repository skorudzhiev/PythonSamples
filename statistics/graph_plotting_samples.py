import matplotlib.pyplot as plt 

data=[3,4,2,4,3,5,3,6,4,3]

if False:
    plt.plot(data)
    print(plt.show())

# Plotting a line
if False:
    # x axis values 
	x = [1,2,3] 
	# corresponding y axis values 
	y = [2,4,1] 
	  
	# plotting the points  
	plt.plot(x, y) 
	  
	# naming the x axis 
	plt.xlabel('x - axis') 
	# naming the y axis 
	plt.ylabel('y - axis') 
	  
	# giving a title to my graph 
	plt.title('My first graph!') 
	  
	# function to show the plot 
	plt.show() 

# Sample bar chart
if False:
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]

    plt.figure(figsize=(9, 3))
    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.show()

# Histogram
if False:
	# frequencies 
	ages = [2,5,70,40,30,45,50,45,43,40,44, 
	        60,7,13,57,18,90,77,32,21,20,40] 
	  
	# setting the ranges and no. of intervals 
	range = (0, 100) 
	bins = 10  
	  
	# plotting a histogram 
	plt.hist(ages, bins, range, color = 'green', 
	        histtype = 'bar', rwidth = 0.8) 
	  
	# x-axis label 
	plt.xlabel('age') 
	# frequency label 
	plt.ylabel('No. of people') 
	# plot title 
	plt.title('My histogram') 
	  
	# function to show the plot 
	plt.show() 

# Scatter plot
if False:
	# x-axis values 
	x = [1,2,3,4,5,6,7,8,9,10] 
	# y-axis values 
	y = [2,4,5,7,6,8,9,11,12,12] 
	  
	# plotting points as a scatter plot 
	plt.scatter(x, y, label= "stars", color= "green",  
	            marker= "*", s=30) 
	  
	# x-axis label 
	plt.xlabel('x - axis') 
	# frequency label 
	plt.ylabel('y - axis') 
	# plot title 
	plt.title('My scatter plot!') 
	# showing legend 
	plt.legend() 
	  
	# function to show the plot 
	plt.show() 

# Pie-chart
if True:
	# defining labels 
	activities = ['eat', 'sleep', 'work', 'play'] 
	  
	# portion covered by each label 
	slices = [3, 7, 8, 6] 
	  
	# color for each label 
	colors = ['r', 'y', 'g', 'b'] 
	  
	# plotting the pie chart 
	plt.pie(slices, labels = activities, colors=colors,  
	        startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
	        radius = 1.2, autopct = '%1.1f%%') 
	  
	# plotting legend 
	plt.legend() 
	  
	# showing the plot 
	plt.show() 