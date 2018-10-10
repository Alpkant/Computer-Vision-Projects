import cv2
import numpy as np
import matplotlib.pyplot as plt
class Histogram(object):
	def __init__(self, imageFilename):
		self.imageFilename  = imageFilename
		self.intensity_range = 256
		self.row  = 0
		self.column = 0
		self.channel = 0
		self.histArray = self.createHistogramArray() 
		self.cdfArray = None
		self.histogramFilename = ""



	def createHistogramArray(self):
		#Read histogram
		I = cv2.imread(self.imageFilename)
		self.row , self.column , self.channel = I.shape
		hist = np.zeros([self.intensity_range, 1, self.channel])
		# Range through the intensity values and find the frequences
		for g in range(self.intensity_range):
			hist[g, 0,...] = np.sum(np.sum(I == g, 0), 0)
		return hist
	
	def createHistogramPlotImage(self,histogramFilename):
		figure,axarr = plt.subplots(self.channel,sharex = False)
		figure.suptitle('Histogram of the R G B channels')
		colors = ["r","g","b","k","c"]
		for i in range(self.channel):
			axarr[i].bar(np.arange(0,self.intensity_range),self.histArray[:,0,i],color=colors[i % self.channel])	
		plt.savefig(histogramFilename)
		self.histogramFilename = histogramFilename





