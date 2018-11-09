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

	def cubic_interpolate(self,arr,y):
		return np.float64(arr[1] + 0.5 * y*(arr[2] - arr[0] + y*(2.0*arr[0] - 5.0*arr[1] + 4.0*arr[2] - arr[3] + y*(3.0*(arr[1] - arr[2]) + arr[3] - arr[0]))))

	def bicubic_interpolate(self,p,x,y):
		arr = np.zeros(4,dtype=np.float64)
		arr[0] = self.cubic_interpolate(p[0],y)
		arr[1] = self.cubic_interpolate(p[1],y)
		arr[2] = self.cubic_interpolate(p[2],y)
		arr[3] = self.cubic_interpolate(p[3],y)
		return self.cubic_interpolate(arr,x)

	def rotate(self,degree):
		if self.type != 0:
			raise Exception("Wrong type of instance!")

		origin_height,origin_width,channel = self.I.shape
		height = np.maximum(origin_width,origin_height)
		width = np.maximum(origin_width,origin_height)	
		center_x = width//2
		center_y = height//2

		self.newI = np.zeros((height,width,channel))

		i,j = np.meshgrid(range(height), range(width), indexing='ij')
		i = i.reshape((1,-1))
		j = j.reshape((1,-1))

		onesCol = np.ones((1,i.shape[1]))
		coords = np.concatenate((i,j,onesCol),axis=0)

		#Calculate backward mapping
		new_coords = np.matmul(np.linalg.inv(np.asarray([
			[np.cos(degree),-np.sin(degree),center_x],
			[np.sin(degree),np.cos(degree),center_y],
			[0,0,1]])),coords)
		counter = 0
		new_coords = np.int32(new_coords)
		new_coords[0,:] +=  center_x
		new_coords[1,:] +=  center_y 


		for i in range(height):
			for j in range(width):
				if new_coords[1,counter] >= origin_width or new_coords[0,counter] >= origin_height or new_coords[1,counter] < 0 or new_coords[0,counter] < 0:
					self.newI[i,j,:] = 0
				else:
					self.newI[i,j,:] = self.I[new_coords[0,counter],new_coords[1,counter],:]
				counter += 1

		row,column,channel = self.newI.shape
		qImg = QtGui.QImage(np.uint8(self.newI).copy(), column, row,3*column, QtGui.QImage.Format_RGB888).rgbSwapped()
		self.pixMap = QtGui.QPixmap.fromImage(qImg)
		return self.newI,self.pixMap


	def scale(self,scale_value):
		if self.type != 1:
			raise Exception("Wrong type of instance!")

		origin_height,origin_width,channel = self.I.shape
		height = np.uint32(origin_height * scale_value)
		width = np.uint32(origin_width *scale_value)
		self.newI = np.zeros((height,width,channel))

		i,j = np.meshgrid(range(height), range(width), indexing='ij')
		i = i.reshape((1,-1))
		j = j.reshape((1,-1))

		onesCol = np.ones((1,i.shape[1]))
		coords = np.concatenate((i,j,onesCol),axis=0)

		#Calculate backward mapping
		new_coords = np.matmul(np.linalg.inv(np.asarray([
			[scale_value,0,10],
			[0,scale_value,0],
			[0,0,1]])),coords)

		counter = 0
		new_coords = np.int32(new_coords)
		for i in range(height):
			for j in range(width):
				if new_coords[1,counter] >= origin_width or new_coords[0,counter] >= origin_height or new_coords[1,counter] < 0 or new_coords[0,counter] < 0:
					self.newI[i,j,:] = 0
				else:
					self.newI[i,j,:] = self.I[new_coords[0,counter],new_coords[1,counter],:]
				counter += 1


		row,column,channel = self.newI.shape
		qImg = QtGui.QImage(np.uint8(self.newI).copy(), column, row,3*column, QtGui.QImage.Format_RGB888).rgbSwapped()
		self.pixMap = QtGui.QPixmap.fromImage(qImg)
		return self.newI,self.pixMap

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
		

		origin_height,origin_width,channel = self.I.shape
		height = origin_height + np.abs(y_value)
		width  = origin_width + np.abs(x_value)
		self.newI = np.zeros((height,width,channel))

		i,j = np.meshgrid(range(height), range(width), indexing='ij')
		i = i.reshape((1,-1))
		j = j.reshape((1,-1))

		onesCol = np.ones((1,i.shape[1]))
		coords = np.concatenate((i,j,onesCol),axis=0)
		#Calculate backward mapping
		new_coords = np.matmul(np.linalg.inv(np.asarray([
			[1,0,y_value],
			[0,1,x_value],
			[0,0,1]])),coords)
		counter = 0
		new_coords = np.uint32(new_coords)
		# No need to interpolate because it is just translation and values are all integers 
		for i in range(height):
			for j in range(width):
				if new_coords[1,counter] >= origin_width or new_coords[0,counter] >= origin_height or new_coords[1,counter] < 0 or new_coords[0,counter] < 0:
					self.newI[i,j,:] = 0
				else:
					self.newI[i,j,:] = self.I[new_coords[0,counter],new_coords[1,counter],:]
				counter += 1

		row,column,channel = self.newI.shape
		qImg = QtGui.QImage(np.uint8(self.newI).copy(), column, row,3*column, QtGui.QImage.Format_RGB888).rgbSwapped()
		self.pixMap = QtGui.QPixmap.fromImage(qImg)
		return self.newI,self.pixMap