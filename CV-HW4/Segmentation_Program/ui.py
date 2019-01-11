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
		mainWindow.resize(1920, 1080)
		self.centralwidget = QtWidgets.QWidget(mainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName("verticalLayout")
		self.input = QtWidgets.QLabel(self.centralwidget)
		self.input.setMaximumSize(QtCore.QSize(16777215, 12))
		self.input.setObjectName("input")
		self.verticalLayout.addWidget(self.input, 0, QtCore.Qt.AlignHCenter)
		self.input_frame = QtWidgets.QFrame(self.centralwidget)
		self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.input_frame.setObjectName("input_frame")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.input_frame)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.input_image_label = QtWidgets.QLabel(self.input_frame)
		self.input_image_label.setText("")
		self.input_image_label.setObjectName("input_image_label")		
		self.verticalLayout_2.addWidget(self.input_image_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
		self.verticalLayout.addWidget(self.input_frame)
		self.results = QtWidgets.QLabel(self.centralwidget)
		self.results.setMaximumSize(QtCore.QSize(16777215, 16))
		self.results.setObjectName("results")
		self.verticalLayout.addWidget(self.results, 0, QtCore.Qt.AlignHCenter)
		self.result_frame = QtWidgets.QFrame(self.centralwidget)
		self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.result_frame.setObjectName("result_frame")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.result_frame)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.tresholded_label = QtWidgets.QLabel(self.result_frame)
		self.tresholded_label.setText("")
		self.tresholded_label.setObjectName("tresholded_label")
		self.horizontalLayout.addWidget(self.tresholded_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
		self.brain_label = QtWidgets.QLabel(self.result_frame)
		self.brain_label.setText("")
		self.brain_label.setObjectName("brain_label")
		self.horizontalLayout.addWidget(self.brain_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
		self.tumor_output_label = QtWidgets.QLabel(self.result_frame)
		self.tumor_output_label.setObjectName("tumor_output_label")
		self.horizontalLayout.addWidget(self.tumor_output_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
		self.verticalLayout.addWidget(self.result_frame)
        
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
		MainWindow.setWindowTitle(_translate("MainWindow", "Morphological Operations"))
		self.input.setText(_translate("mainWindow", "Input"))
		self.results.setText(_translate("mainWindow", "Results of operations"))
		self.menuFile.setTitle(_translate("mainWindow", "File"))
		self.actionOpen_Input.setText(_translate("mainWindow", "Open Input"))
		self.actionSave_Result.setText(_translate("mainWindow", "Save"))
		self.actionExit.setText(_translate("mainWindow", "Exit"))
		self.detectCorners.setText(_translate("mainWindow","Segment"))



	def openInputFileDialog(self):
		options = QtWidgets.QFileDialog.Options()
		filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Import an image ","","PNG Files (*.png);;Jpg Files (*.jpg)",options=options)
		if filename:
			pixMap = QtGui.QPixmap(filename)
			self.input_image_label.setPixmap(pixMap)
			self.input_image_arr = cv2.imread(filename)
			self.input_image_arr = cv2.cvtColor(self.input_image_arr, cv2.COLOR_BGR2GRAY)

	# This function finds closest cluster point to an intensity
	def closest_cluster(self,intensity,clusters):
		counter = len(clusters)
		min = float('inf')
		assigned_cluster = 0
		for i in range(counter):
			difference = abs(clusters[i]-intensity)
			if difference < min:
				min = difference
				assigned_cluster = i

		return assigned_cluster

	# Take the mean value of the assigned points for new cluster means
	def calculate_new_clusters(self,clusters,assigned_points,intensities):
		new_clusters = np.zeros(clusters.shape).astype('float')
		counter = np.zeros(new_clusters.shape).astype('int')
		for j,val in enumerate(assigned_points):
			new_clusters[val] += intensities[j]
			counter[val] += 1
		new_clusters /= counter
		return new_clusters

	def converge(self,old_clusters,clusters):
		return True if np.array_equal(old_clusters,clusters) else False

	def kMeans(self,intensities,k):
		clusters = np.random.randint(0,256,size=k,).astype('float')
		old_clusters = np.random.randint(0,256,size=k,).astype('float')		
		assigned_points = np.zeros(len(intensities),dtype=int)

		# While clusters are moving to new points
		while not self.converge(clusters,old_clusters):
			for i,val in enumerate(intensities):
				# Assign the point to the closest cluster
				assigned_points[i] = self.closest_cluster(val,clusters)
			
			old_clusters = np.copy(clusters)
			# Calculate new cluster centers
			clusters = self.calculate_new_clusters(clusters,assigned_points,intensities)

		return clusters,assigned_points	

	def detect(self):
		if self.input_image_label.pixmap() is None:
			self.showError()
			return

		# First using treshold show the brighter parts
		treshold = 50
		height, width = self.input_image_arr.shape
		tresholded_image = np.copy(self.input_image_arr)
		brain_region = np.copy(self.input_image_arr)
		for i in range(height):
			for j in range(width):
				if tresholded_image[i,j] > treshold:
					tresholded_image[i,j] = 255
				else:
					tresholded_image[i,j] = 0

		# Show the results
		qImg = QtGui.QImage(np.uint8(tresholded_image).copy(), width, height, tresholded_image.strides[0], QtGui.QImage.Format_Indexed8)
		self.tresholded_label.setPixmap(QtGui.QPixmap.fromImage(qImg))

		## Continue with morphological operations
		# Erosion operation to remove skull from image
		kernel = np.ones((4,4),np.uint8) # Structuring element
		tresholded_image = cv2.erode(tresholded_image,kernel,iterations = 5)

		# Show the only brain to user
		qImg = QtGui.QImage(np.uint8(tresholded_image).copy(), width, height, tresholded_image.strides[0], QtGui.QImage.Format_Indexed8)
		self.brain_label.setPixmap(QtGui.QPixmap.fromImage(qImg))

		# K means algorithm
		
		# First only get the brain region intensities
		for i in range(height):
			for j in range(width):
				if tresholded_image[i,j] == 0:
					brain_region[i,j] = 0
				else:
					brain_region[i,j] = self.input_image_arr[i,j]

		# Make them vector for easier access
		intensities = np.reshape(brain_region,(-1,1))
		# Calculate cluster centers and assign each intensity to cluster
		clusters,assigned_points = self.kMeans(intensities,k=2)
		assigned_points = np.reshape(assigned_points,(height,width))

		# After findind tumor and other parts only highlight the tumor region which has more intensity than other brain parts
		treshold = 0
		clusters = np.uint8(clusters)
		treshold =  clusters[0] if clusters[0] > clusters[1] else clusters[1] 
		brain_region[ brain_region >= treshold ] = 255
		brain_region[ brain_region < treshold ] = 0					

		# Remove the extra bright pixels which are in the brain part but not adjacent to the tumor which is not part of tumor
		kernel = np.ones((3,3),np.uint8)
		brain_region = cv2.erode(brain_region,kernel,iterations = 3)
		# In order to find the edge of the tumor blur the image and remove the blurred one from original
		smoothed_region = cv2.GaussianBlur(brain_region,(5,5),0.6,0,cv2.BORDER_DEFAULT)
		brain_region -= smoothed_region
		# We get only edge of the tumor

		colored_brain = cv2.cvtColor(brain_region, cv2.COLOR_GRAY2RGB)
		# Make the tumor edges blue
		colored_brain[brain_region > 0] = 255
		colored_brain[:,:,1] = 0
		colored_brain[:,:,2] = 0

		self.input_image_arr = cv2.cvtColor(self.input_image_arr, cv2.COLOR_GRAY2RGB)
		self.input_image_arr[colored_brain[:,:,0] > 0] = [255,0,0]
		
		# Show the output
		qImg = QtGui.QImage(np.uint8(self.input_image_arr).copy(), width, height,3*width, QtGui.QImage.Format_RGB888).rgbSwapped()
		self.tumor_output_label.setPixmap(QtGui.QPixmap.fromImage(qImg))

	# Save the current image as output image when user want to save
	def saveImage(self):
		pixMap = self.tumor_output_label.pixmap()
		pixMap2 = self.brain_label.pixmap()
		pixMap3 = self.tresholded_label.pixmap()

		if pixMap is not None:
			pixMap.save("result_output.png","PNG")
			pixMap2.save("brainmask.png","PNG")
			pixMap3.save("tresholded.png","PNG")



	def showError(self):
		self.popup_dialog = popup_dialog()
		self.popup_dialog.setupUi(self.popup_dialog)
		self.popup_dialog.show()
