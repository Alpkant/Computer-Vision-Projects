import cv2
import numpy as np
import matplotlib.pyplot as plt

""" 
In order to run the program you should execute the following command
in the command line: python Mainapp.py
You need Mainapp.py, popup.py, ui.py, Histogram.py and HistogramMatcher.py 
files in order to run the program.
"""

class Histogram(object):
	""" 
	Histogram class takes input image filepath and
	creates an histogram for the image. Also using the instances
	one can create graphical represantation of the histogram. Also
	cumulative distribution of the pixel intensities can be constructed from the
	any histogram instance
	
	    Args:
        imageFilename : Full path of the image that will be used as source.

    	Attributes:
        imageFilename (str): Image file path.
        intensityRange (int): Intensity range of the image pixel. Default value is 256 for RGB.
        row (int): Number of rows in the image 
        column (int): Number of columns in the image
        channel (int): Number of the color channel of the image 
        histArray (np.ndarray): Numpy matrix that holds histogram values for all channels shape (intensityRange,1,channel)
        cdfArray (np.ndarray): Cumulative distribution of the intensities shape and type is same with histArray 
        histogramFilename (str): The output path of the histogram that will be saved there
	"""


	def __init__(self, imageFilename):
		self.imageFilename  = imageFilename
		self.intensityRange = 256
		self.row  = 0
		self.column = 0
		self.channel = 0
		# Histogram of the given image
		self.histArray = self.createHistogramArray() 
		# Cumulative Histogram Array shaped (intensityRange,1,channel)
		self.cdfArray = None
		self.histogramFilename = ""

	def createHistogramArray(self):
		"""
		Creates histogram of the intensities for each channel and save them into one numpy array
		"""
		# Read image
		I = cv2.imread(self.imageFilename)
		self.row , self.column , self.channel = I.shape
		# Create histogram array of the all channels
		hist = np.zeros([self.intensityRange, 1, self.channel])
		# Range through the intensity values and find the frequences
		for g in range(self.intensityRange):
			hist[g, 0,...] = np.sum(np.sum(I == g, 0), 0)
		return hist
	
	def createHistogramPlotImage(self,histogramFilename):
		""" 
		Creating Histogram for the each channel and save the plot
		to given path 
		"""
		figure,axarr = plt.subplots(self.channel,sharex = False)
		figure.suptitle('Histogram of the R G B channels')
		colors = ["r","g","b","k","c"]
		for i in range(self.channel):
			axarr[i].bar(np.arange(0,self.intensityRange),self.histArray[:,0,self.channel-i-1],color=colors[i % self.channel])	
		plt.savefig(histogramFilename)
		self.histogramFilename = histogramFilename
		# Since we have histogram we can create cumilative histogram too
		self.createCdfHistogram()

	def createCdfHistogram(self):
		# Create histogram that has all the channels with appropiate shape
		self.cdfArray = np.zeros([self.intensityRange,1,self.channel])
		# Temporary variable array for holding values
		temp = np.zeros([self.channel,1])
		totalPx = self.row * self.column
		for i in range(self.intensityRange):
			for j in range (self.channel):
				# Calculate cumilative probability
				temp[j] += self.histArray[i,0,j] / totalPx
				self.cdfArray[i,0,j] = temp[j]