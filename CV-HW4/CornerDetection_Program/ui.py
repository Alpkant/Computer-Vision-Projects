# Author:
# Alperen Kantarcı
# 150140140

""" 
In order to run the program you should execute the following command
in the command line: python Mainapp.py
You need Mainapp.py, popup.py, ui.py
files in order to run the program.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from popup import popup_dialog


class Ui_MainWindow(object):
	def setupUi(self, mainWindow):
	    mainWindow.setObjectName("mainWindow")
	    mainWindow.resize(1440, 728)
	    self.centralwidget = QtWidgets.QWidget(mainWindow)
	    self.centralwidget.setObjectName("centralwidget")
	    self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
	    self.horizontalLayout.setObjectName("horizontalLayout")
	    self.verticalLayout = QtWidgets.QVBoxLayout()
	    self.verticalLayout.setObjectName("verticalLayout")
	    self.label = QtWidgets.QLabel(self.centralwidget)
	    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
	    sizePolicy.setHorizontalStretch(1)
	    sizePolicy.setVerticalStretch(1)
	    sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
	    self.label.setSizePolicy(sizePolicy)
	    self.label.setObjectName("label")
	    self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
	    self.input_frame = QtWidgets.QFrame(self.centralwidget)
	    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
	    sizePolicy.setHorizontalStretch(0)
	    sizePolicy.setVerticalStretch(100)
	    sizePolicy.setHeightForWidth(self.input_frame.sizePolicy().hasHeightForWidth())
	    self.input_frame.setSizePolicy(sizePolicy)
	    self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
	    self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
	    self.input_frame.setObjectName("input_frame")
	    self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.input_frame)
	    self.verticalLayout_5.setObjectName("verticalLayout_5")
	    self.input_image_label = QtWidgets.QLabel(self.input_frame)
	    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
	    sizePolicy.setHorizontalStretch(0)
	    sizePolicy.setVerticalStretch(0)
	    sizePolicy.setHeightForWidth(self.input_image_label.sizePolicy().hasHeightForWidth())
	   
	    self.input_image_label.setSizePolicy(sizePolicy)
	    self.input_image_label.setText("")
	    self.input_image_label.setScaledContents(False)
	    self.input_image_label.setObjectName("input_image_label")

	    
	    self.verticalLayout_5.addWidget(self.input_image_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
	    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
	    sizePolicy.setHorizontalStretch(0)
	    sizePolicy.setVerticalStretch(0)
	    self.verticalLayout.addWidget(self.input_frame)
	    self.verticalLayout.setStretch(0, 1)
	    self.horizontalLayout.addLayout(self.verticalLayout)
	    self.verticalLayout_2 = QtWidgets.QVBoxLayout()
	    self.verticalLayout_2.setObjectName("verticalLayout_2")
	    self.label_4 = QtWidgets.QLabel(self.centralwidget)
	    self.label_4.setObjectName("label_4")
	    self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
	    self.result_frame = QtWidgets.QFrame(self.centralwidget)
	    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
	    sizePolicy.setHorizontalStretch(0)
	    sizePolicy.setVerticalStretch(100)
	    sizePolicy.setHeightForWidth(self.result_frame.sizePolicy().hasHeightForWidth())
	    self.result_frame.setSizePolicy(sizePolicy)
	    self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
	    self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
	    self.result_frame.setObjectName("result_frame")
	    self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.result_frame)
	    self.verticalLayout_6.setObjectName("verticalLayout_6")

	    self.result_image_label = QtWidgets.QLabel(self.result_frame)
	    self.result_image_label.setText("")
	    self.result_image_label.setObjectName("result_image_label")
	    
	    self.verticalLayout_6.addWidget(self.result_image_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
	    self.verticalLayout_2.addWidget(self.result_frame)
	    self.horizontalLayout.addLayout(self.verticalLayout_2)
	    
	    mainWindow.setCentralWidget(self.centralwidget)

	    self.menubar = QtWidgets.QMenuBar(mainWindow)
	    self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
	    self.menubar.setObjectName("menubar")
	    self.menuFile = QtWidgets.QMenu(self.menubar)
	    self.menuFile.setObjectName("menuFile")
	    mainWindow.setMenuBar(self.menubar)
	    self.statusbar = QtWidgets.QStatusBar(mainWindow)
	    self.statusbar.setEnabled(True)
	    self.statusbar.setObjectName("statusbar")
	    mainWindow.setStatusBar(self.statusbar)

	    self.actionOpen_Input = QtWidgets.QAction(mainWindow)
	    self.actionOpen_Input.setObjectName("actionOpen_Input")
	    self.actionOpen_Input.setShortcut("Ctrl+I")
	    # Open input file dialog for user image
	    self.actionOpen_Input.triggered.connect(self.openInputFileDialog)

	    self.actionExit = QtWidgets.QAction(mainWindow)
	    self.actionExit.setObjectName("actionExit")
	    self.actionExit.setShortcut("Ctrl+Q")
	    # Exit from the application
	    self.actionExit.triggered.connect(QtWidgets.qApp.quit)

	    self.actionSave_Result = QtWidgets.QAction(mainWindow)
	    self.actionSave_Result.setObjectName("actionSave_Result")
	    self.actionSave_Result.setShortcut("Ctrl+S")
	    # Open input file dialog for user image
	    self.actionSave_Result.triggered.connect(self.saveImage)

	    self.detectCorners = QtWidgets.QAction(mainWindow)
	    self.detectCorners.setObjectName("detectCorners")
	    self.detectCorners.setShortcut("Ctrl+D")
	    self.detectCorners.triggered.connect(self.detect)

	    self.menuFile.addAction(self.actionOpen_Input)
	    self.menuFile.addAction(self.actionSave_Result)
	    self.menuFile.addAction(self.actionExit)	    
	    self.menubar.addAction(self.menuFile.menuAction())
	    self.menubar.addAction(self.detectCorners)


	    self.retranslateUi(mainWindow)
	    QtCore.QMetaObject.connectSlotsByName(mainWindow)

	# Name strings of the each button
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Filtering & Geometric Transforms"))
		self.label.setText(_translate("mainWindow", "Input"))
		self.label_4.setText(_translate("mainWindow", "Result"))
		self.menuFile.setTitle(_translate("mainWindow", "File"))
		self.actionOpen_Input.setText(_translate("mainWindow", "Open Input"))
		self.actionSave_Result.setText(_translate("mainWindow", "Save"))
		self.actionExit.setText(_translate("mainWindow", "Exit"))
		self.detectCorners.setText(_translate("mainWindow","Detect Corners"))

	def openInputFileDialog(self):
	    options = QtWidgets.QFileDialog.Options()
	    filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","Jpg Files (*.jpg);;PNG Files (*.png)",options=options)
	    if filename:
	    	self.input_image_arr = cv2.imread(filename)
	    	pixMap = QtGui.QPixmap(filename)
	    	self.input_image_label.setPixmap(pixMap)

	def derivative_x(self,arr,x,y):
		# Centered x derivative
		return (int(arr[x+1,y]) - int(arr[x-1,y])) / 2

	def derivative_y(self,arr,x,y):
		# Centered y derivative
		return (int(arr[x,y+1]) - int(arr[x,y-1])) / 2

	def calculateG(self,x,y,derivatives,w_size):
		# Usin x and y derivatives create image structure kernel
		xsquare = 0
		xy = 0
		ysquare = 0
		w = w_size//2
		for i in range(x-w,x+w+1):
			for j in range(y-w,y+w+1):
				xsquare += derivatives[i,j][0]**2
				xy += derivatives[i,j][0]*derivatives[i,j][1]
				ysquare += derivatives[i,j][1]**2

		G = np.array([[xsquare,xy],[xy,ysquare]])
		return G

	def isCorner(self,treshold,G):
		# Calculate eigen values
		eigvals = np.linalg.eigvals(G)
		# Small k value
		k = 0.04
		# Calculate R
		R = (eigvals[0]*eigvals[1] - k * (eigvals[0]+eigvals[1])**2)
		# If R is above the treshold then it is a corner
		if R > treshold:
			return True
		return False

	def detect(self):
		if self.input_image_label.pixmap() is None: 
			self.showError()
			return

		smoothed_image = cv2.GaussianBlur(self.input_image_arr,(3,3),0.0125,0,cv2.BORDER_DEFAULT)
		height, width, channel = smoothed_image.shape

		pad_s = 3
		# Add padding for preventing edge errors
		smoothed_image = np.pad(smoothed_image,( (pad_s,pad_s),(pad_s,pad_s),(0,0) ),mode='edge')
		# We can only use a channel or use luminosity
		one_channel = smoothed_image[:,:,0]

		padded_derivative = np.zeros(one_channel.shape,dtype=(float,2))

		# Calculate x and y derivatives 
		for i in range(pad_s,height-pad_s):
			for j in range(pad_s,width-pad_s):
				padded_derivative[i,j] = (self.derivative_x(one_channel,i,j),self.derivative_y(one_channel,i,j))
		
		# Remove pads
		smoothed_image = smoothed_image[pad_s:-pad_s,pad_s:-pad_s,:]
		w_size = 3
		# Treshold for accepting a corner 
		treshold = 1000000
		# If pixel is above the treshold than mark as corner point
		for i in range(pad_s,height-pad_s):
			for j in range(pad_s,width-pad_s):
				if self.isCorner(treshold,self.calculateG(i,j,padded_derivative,w_size)):
					# Paint the pixels to red
					smoothed_image[i-2:i+1,j-2:j+1,:] = [0,0,255]  

		# Print output
		height, width, channel = smoothed_image.shape
		qImg = QtGui.QImage(np.uint8(smoothed_image).copy(), width, height,3*width, QtGui.QImage.Format_RGB888).rgbSwapped()
		self.result_image_label.setPixmap(QtGui.QPixmap.fromImage(qImg))


	# Save the current image as output image when user want to save
	def saveImage(self):
		pixMap = self.result_image_label.pixmap()
		if pixMap is not None:
			pixMap.save("result.png","PNG")

	def showError(self):
		self.popup_dialog = popup_dialog()
		self.popup_dialog.setupUi(self.popup_dialog)
		self.popup_dialog.show()
