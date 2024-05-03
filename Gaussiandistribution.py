import math
import matplotlib.pyplot as plt
import seaborn as sns
from .Generaldistribution import Distribution

class Gaussian(Distribution):
	""" Gaussian distribution class for calculating and 
	visualizing a Gaussian distribution.
	
	Attributes:
		mean (float) representing the mean value of the distribution
		stdev (float) representing the standard deviation of the distribution
		data_list (list of floats) a list of floats extracted from the data file
			
	"""
	def _init_(self, mu=0, sigma=1):
		
		Distribution._init_(self, mu, sigma)
	
		
	
	def calculate_mean(self):
	
		"""Function to calculate the mean of the data set.
		
		Args: 
			None
		
		Returns: 
			float: mean of the data set
	
		"""
					
		avg = 1.0 * sum(self.data) / len(self.data)
		
		self.mean = avg
		
		return self.mean



	def calculate_stdev(self, sample=True):

		"""Function to calculate the standard deviation of the data set.
		
		Args: 
			sample (bool): whether the data represents a sample or population
		
		Returns: 
			float: standard deviation of the data set
	
		"""

		if sample:
			n = len(self.data) - 1
		else:
			n = len(self.data)
	
		mean = self.calculate_mean()
	
		sigma = 0
	
		for d in self.data:
			sigma += (d - mean) ** 2
		
		sigma = math.sqrt(sigma / n)
	
		self.stdev = sigma
		
		return self.stdev
		
		
		
	def plot_histogram(self):
		"""Function to output a histogram of the instance variable data using 
		matplotlib pyplot library.
		
		Args:
			None
			
		Returns:
			None
		"""
		sns.set_theme()
		plt.hist(self.data)
		plt.title('Histogram of Data')
		plt.xlabel('data')
		plt.ylabel('count')
		
		
		
	def pdf(self, x):
		
		"""Calculates the relative probability density at a specific point in the Gaussian distribution.

		Args:
			x (float): The point at which to calculate the relative probability density.

		Returns:
			float: The relative probability density at the specified point.
		"""
		
		return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
		

	def plot_histogram_pdf(self, n_spaces = 50):

		"""Function to plot the normalized histogram of the data and a plot of the 
		probability density function along the same range
		
		Args:
			n_spaces (int): number of data points 
		
		Returns:
			list: x values for the pdf plot
			list: y values for the pdf plot
			
		"""
		
		mu = self.mean
		sigma = self.stdev

		min_range = min(self.data)
		max_range = max(self.data)
		
		 # calculates the interval between x values
		interval = 1.0 * (max_range - min_range) / n_spaces

		x = []
		y = []
		
		# calculate the x values to visualize
		for i in range(n_spaces):
			tmp = min_range + interval*i
			x.append(tmp)
			y.append(self.pdf(tmp))

		# make the plots
		fig, axes = plt.subplots(figsize=(8,4.8))
		axes.hist(self.data, density=True)
		axes.plot(x, y, label='Probability Density Function')
		axes.set_title('Normalized Histogram of Data')
		axes.set_xlabel('data')
		axes.set_ylabel('Density')
		axes.legend()
		plt.show()

		
		
		
	def __add__(self, other):
		
		"""Function to add together two Gaussian distributions
		
		Args:
			other (Gaussian): Gaussian instance
			
		Returns:
			Gaussian: Gaussian distribution
			
		"""
		
		result = Gaussian()
		result.mean = self.mean + other.mean
		result.stdev = math.sqrt(self.stdev * 2 + other.stdev * 2)
		
		return result
		
		
	def __repr__(self):
	
		"""Function to output the characteristics of the Gaussian instance
		
		Args:
			None
		
		Returns:
			string: characteristics of the Gaussian
		
		"""
		
		return "mean {}, standard deviation {}".format(self.mean, self.stdev)