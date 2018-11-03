# Author:
# Alperen Kantarcı
# 150140140


import numpy as np
import cv2
from PyQt5 import QtGui
class GaussianFilter(object):

	def __init__(self,image,filter_size):
		#self.image = image
		self.I = image
		self.filter_size = filter_size
		self.newI = np.zeros(self.I.shape)
		self.pixMap = None

	def apply_filter(self):
		kernel = self.get_gauss_kernel(self.filter_size)
		# Add appropriate padding size to the image
		pad_s = self.filter_size//2
		self.I = np.pad(self.I,( (pad_s,pad_s),(pad_s,pad_s),(0,0) ),mode='constant')
		row , column , channel = self.I.shape

		for i in range(channel):
			for r in range(pad_s,row-pad_s):
				for c in range(pad_s,column-pad_s):
					self.newI[r-pad_s,c-pad_s,i] = np.sum(np.uint8(self.I[r-pad_s:r+pad_s+1,c-pad_s:c+pad_s+1,i]*kernel))

		row,column,channel = self.newI.shape
		qImg = QtGui.QImage(np.uint8(self.newI).copy(), column, row,3*column, QtGui.QImage.Format_RGB888).rgbSwapped()
		self.pixMap = QtGui.QPixmap.fromImage(qImg)
		return self.newI,self.pixMap


	def get_gauss_kernel(self,size,sigma=1):
	    center= size // 2
	    # Create 2d kernel
	    kernel=np.zeros((size,size))
	    for i in range(size):
	       for j in range(size):
	       		# Calculate gaussian formula for each i j
	        	diff=np.sqrt((i-center)**2+(j-center)**2)
	        	kernel[i,j]=np.exp(-(diff**2)/2*sigma**2)
	    return kernel/np.sum(kernel)