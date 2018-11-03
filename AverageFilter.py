# Author:
# Alperen Kantarcı
# 150140140


import numpy as np
import cv2
from PyQt5 import QtGui
class AverageFilter(object):

	def __init__(self,image,filter_size):
		#self.image = image
		self.I = image
		self.filter_size = filter_size
		self.newI = np.zeros(self.I.shape)
		self.pixMap = None

	def apply_filter(self):
		# Add appropriate padding size to the image
		pad_s = self.filter_size//2
		self.I = np.pad(self.I,( (pad_s,pad_s),(pad_s,pad_s),(0,0) ),mode='constant')
		row , column , channel = self.I.shape
		for i in range(channel):
			for r in range(pad_s,row-pad_s):
				for c in range(pad_s,column-pad_s):
					# Get the mean value of the filter image multiplication
					self.newI[r-pad_s,c-pad_s,i] = np.uint8(np.mean(self.I[r-pad_s:r+pad_s,c-pad_s:c+pad_s,i]))

		row,column,channel = self.newI.shape
		qImg = QtGui.QImage(np.uint8(self.newI).copy(), column, row,3*column, QtGui.QImage.Format_RGB888).rgbSwapped()
		self.pixMap = QtGui.QPixmap.fromImage(qImg)
		return self.newI,self.pixMap

