import matplotlib.pyplot as plt
import numpy as np



class Graph:

 	#def f(x):
		#return x

#f2=lambda x:x

	def __init__(self, function=lambda x:x):
		self.function = function



	def plot(self):
		y=[]
		x = np.arange(0, 5, 0.1);
		for i in np.arange(0,5,0.1):
			 
			y.append(self.function(i))
		plt.plot(x,y)
		plt.show()	