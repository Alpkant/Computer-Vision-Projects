# Author:
# Alperen Kantarcı
# 150140140

import numpy as np
import cv2
from Histogram import Histogram


""" 
In order to run the program you should execute the following command
in the command line: python Mainapp.py
You need Mainapp.py, popup.py, ui.py, Histogram.py and HistogramMatcher.py 
files in order to run the program.
"""

class HistogramMatcher(object):
	""" 
	Histogram Matcher class takes two Histogram object and matches 
	the histograms using input and target objects. Matcher class also
	can generate image of the matched histogram result.
	
	    Args:
        inputCdf (Histogram) : Histogram object that will be used as input
		targetCdf (Histogram): Histogram object that will be used as target
		resultFilename (str) : Result image path that will be saved into
    	Attributes:
    	inputCDF (Histogram) :
    	targetCDF (Histogram):
        resultHistogram (numpy.ndarray): Matched histogram matrix that will be used as result
        lookupTable (numpy.ndarray): Lookup table that will be used for mapping from input to target histogram
        imageArray (numpy.ndarray): Image array of result that will be used for saving 
	"""	
	def __init__(self,inputCdf,targetCdf,resultFilename):
		self.inputCDF  = inputCdf
		self.targetCDF = targetCdf
		self.resultFilename = resultFilename
		self.resultHistogram = None
		self.lookupTable = None
		self.imageArray = None

	def createLookupTable(self):
		# Lookup table will have shape of (intensityRange,channel)
		self.lookupTable = np.zeros([self.inputCDF.intensityRange,self.inputCDF.channel])
		# Temp variable for counting intensity level
		gj = np.zeros([self.inputCDF.channel,1],dtype=np.uint8)
		for i in range(self.inputCDF.intensityRange):
			# For every level we need one value for lookup table
			for j in range(self.inputCDF.channel):
				# For all channels
				while self.targetCDF.cdfArray[gj[j,0],0,j] < self.inputCDF.cdfArray[i,0,j] and gj[j,0] < 255:
					# If target cdf value is bigger than current(i) instensity then save that intensity level to the lookup table
					# actually make mapping from i to gj[j,0] value 
					gj[j,0] += 1
				# Save the lookup table
				self.lookupTable[i,j] = gj[j,0]
				# Reset the temp values 
				gj[j,0] = 0


	def constructImage(self):
		# Read the image that will be mapped
		I = cv2.imread(self.inputCDF.imageFilename)
		# Make the mappings for each channel
		red = np.uint8(self.lookupTable[:,0][I])[:,:,0]
		green = np.uint8(self.lookupTable[:,1][I])[:,:,1]
		blue = np.uint8(self.lookupTable[:,2][I])[:,:,2]
		# Construct the rgb image from new mapped arrays
		image = np.dstack((red,green,blue))
		self.imageArray = image
		# Write image to the given path
		cv2.imwrite(self.resultFilename,self.imageArray,[cv2.IMWRITE_PNG_COMPRESSION, 3])
