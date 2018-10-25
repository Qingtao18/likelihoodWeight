import numpy as np
import matplotlib.pyplot as plt
from random import *
n = 500000
pos = 2
randBinList = lambda n: [randint(0,1) for b in range(1,n+1)]
rand = randBinList(n)

prob = 0
weight = 0
sum = 0
plt.ion() # interactive mode on 
x = 0
y = 0
line, = plt.plot(x,y) # plot the data and specify the 2d line
ax = plt.gca() # get most of the figure elements
weightTemp = 0 
for i in range(n/10):
	fB = 0
	weightTemp = 0 
	for j in range(10):#from 0 to 10
		bIPos = i * 10 + j
		fB += 2**j * rand[bIPos];
	weightTemp += float(2)/float(3) * ((float(1)/float(5))**abs(128 - fB))
	if rand[i*10 + pos - 1] == 1:
		sum+=weightTemp
	weight+=weightTemp
	if weight != 0:
 		print prob
 		prob = float(sum)/float(weight)
	x = np.append(x, i)
	y = np.append(y, prob)
	line.set_xdata(x)
	line.set_ydata(y) # set the curve with new data
	ax.relim() # renew the data limits
	ax.autoscale_view(True, True, True) # rescale plot view
	plt.draw() # plot new figure
	plt.pause(1e-2) # pause to show the figure



#plt.plot(x,prob)
plt.savefig("2.png")
plt.show()




