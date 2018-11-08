# Author:
# Alperen Kantarcı
# 150140140


import numpy as np
import cv2
from PyQt5 import QtGui
class Transformer(object):
	def __init__(self,image,type):
		self.I = image
		self.newI = np.zeros(self.I.shape)
		self.pixMap = None
		if type == "rotate":
			self.type = 0
		elif type == "scale":
			self.type = 1
		elif type == "translate":
			self.type = 2
		else:
			raise Exception('invalid transforming type. Available ones rotate, scale, translate')


	def rotate(self,degree):
		if self.type != 0:
			raise Exception("Wrong type of instance!")


	def scale(self,scale_value):
		if self.type != 1:
			raise Exception("Wrong type of instance!")

		scale_mat = np.array([ 
			[scale_value,0,0],
			[0,scale_value,0],
			[0,0,1] ])

	def translate(self,direction):
		if self.type != 2:
			raise Exception("Wrong type of instance!")

		# Translation base pixel values
		x_value = 30
		y_value = 30
		if direction == -1: # Left
			x_value *= -1
			y_value = 0
		elif direction == 0: # Right
			y_value = 0
		elif direction == 1: # Down
			x_value = 0
		elif direction == 2: # Up
			x_value = 0
			y_value *= -1
		

		height,width,channel = self.I.shape
		i,j = np.meshgrid(range(height), range(width), indexing='ij')
		i = i.reshape((1,-1))
		j = j.reshape((1,-1))

		onesCol = np.ones((1,i.shape[1]))
		coords = np.concatenate((i,j,onesCol),axis=0)
		#Calculate backward mapping
		new_coords = np.matmul(np.linalg.inv(np.asarray([
			[1,0,y_value],
			[0,1,x_value],
			[0,0,1]])),coords,)
		counter = 0
		new_coords = np.uint32(new_coords)
		# No need to interpolate because it is just translation and values are all integers 
		for i in range(height):
			for j in range(width):
				if new_coords[1,counter] >= width or new_coords[0,counter] >= height or new_coords[1,counter] < 0 or new_coords[0,counter] < 0:
					self.newI[i,j,:] = 0
				else:
					self.newI[i,j,:] = self.I[new_coords[0,counter],new_coords[1,counter],:]
				counter += 1

		row,column,channel = self.newI.shape
		qImg = QtGui.QImage(np.uint8(self.newI).copy(), column, row,3*column, QtGui.QImage.Format_RGB888).rgbSwapped()
		self.pixMap = QtGui.QPixmap.fromImage(qImg)
		return self.newI,self.pixMap