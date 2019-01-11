from PyQt5 import QtCore, QtGui, QtWidgets
<<<<<<< HEAD
import cv2
import numpy as np
from popup import popup_dialog
from information import information_dialog
import random

def area(x1, y1, x2, y2, x3, y3): 
	return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0) 

  
# A function to check whether point P(x, y) 
# lies inside the triangle formed by  
# A(x1, y1), B(x2, y2) and C(x3, y3)  
def isInside(t_list, x, y): 
	x1 = t_list[0]
	y1=t_list[1]
	x2 = t_list[2]
	y2=t_list[3]
	x3 = t_list[4]
	y3=t_list[5]

	A = area (x1, y1, x2, y2, x3, y3) 
	A1 = area (x, y, x2, y2, x3, y3)   
	A2 = area (x1, y1, x, y, x3, y3) 
	A3 = area (x1, y1, x2, y2, x, y) 
    # Check if sum of A1, A2 and A3  
    # is same as A 
	if(A == A1 + A2 + A3): 
		return True
	else: 
		return False

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
	    self.input_image_label.mousePressEvent = self.inputImageMouseClickEvent

	    
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
	    self.target_frame = QtWidgets.QFrame(self.centralwidget)
	    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
	    sizePolicy.setHorizontalStretch(0)
	    sizePolicy.setVerticalStretch(100)
	    sizePolicy.setHeightForWidth(self.target_frame.sizePolicy().hasHeightForWidth())
	    self.target_frame.setSizePolicy(sizePolicy)
	    self.target_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
	    self.target_frame.setFrameShadow(QtWidgets.QFrame.Raised)
	    self.target_frame.setObjectName("target_frame")
	    self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.target_frame)
	    self.verticalLayout_6.setObjectName("verticalLayout_6")

	    self.target_image_label = QtWidgets.QLabel(self.target_frame)
	    self.target_image_label.setText("")
	    self.target_image_label.setObjectName("target_image_label")
	    self.target_image_label.mousePressEvent = self.targetImageMouseClickEvent
	    
	    self.verticalLayout_6.addWidget(self.target_image_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
	    self.verticalLayout_2.addWidget(self.target_frame)
	    self.horizontalLayout.addLayout(self.verticalLayout_2)
	    self.verticalLayout_3 = QtWidgets.QVBoxLayout()
	    self.verticalLayout_3.setObjectName("verticalLayout_3")
	    self.label_7 = QtWidgets.QLabel(self.centralwidget)
	    self.label_7.setObjectName("label_7")
	    self.verticalLayout_3.addWidget(self.label_7, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
	    self.result_frame = QtWidgets.QFrame(self.centralwidget)
	    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
	    sizePolicy.setHorizontalStretch(0)
	    sizePolicy.setVerticalStretch(100)
	    sizePolicy.setHeightForWidth(self.result_frame.sizePolicy().hasHeightForWidth())
	    self.result_frame.setSizePolicy(sizePolicy)
	    self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
	    self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
	    self.result_frame.setObjectName("result_frame")
	    self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.result_frame)
	    self.verticalLayout_7.setObjectName("verticalLayout_7")
	    self.result_image_label = QtWidgets.QLabel(self.result_frame)
	    self.result_image_label.setText("")
	    self.result_image_label.setObjectName("result_image_label")
	    self.verticalLayout_7.addWidget(self.result_image_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
	    self.verticalLayout_3.addWidget(self.result_frame)
	    self.horizontalLayout.addLayout(self.verticalLayout_3)
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

	    self.actionOpen_Target = QtWidgets.QAction(mainWindow)
	    self.actionOpen_Target.setObjectName("actionOpen_Target")
	    self.actionOpen_Target.setShortcut("Ctrl+T")
	    self.actionOpen_Target.triggered.connect(self.openTargetFileDialog)       

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

	    self.actionTriangulate = QtWidgets.QAction(mainWindow)
	    self.actionTriangulate.setObjectName("actionTriangulate")
	    self.actionTriangulate.setShortcut("Ctrl+P")
	    self.actionTriangulate.triggered.connect(self.triangulate)


	    self.actionMorph = QtWidgets.QAction(mainWindow)
	    self.actionMorph.setObjectName("actionMorph")
	    self.actionMorph.setShortcut("Ctrl+M")
	    self.actionMorph.triggered.connect(self.morph)


	    self.menuFile.addAction(self.actionOpen_Input)
	    self.menuFile.addAction(self.actionOpen_Target)
	    self.menuFile.addAction(self.actionSave_Result)
	    self.menuFile.addAction(self.actionExit)	    
	    self.menubar.addAction(self.menuFile.menuAction())
	    self.menubar.addAction(self.actionTriangulate)
	    self.menubar.addAction(self.actionMorph) 


	    self.retranslateUi(mainWindow)
	    QtCore.QMetaObject.connectSlotsByName(mainWindow)

	# Name strings of the each button
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Filtering & Geometric Transforms"))
		self.label.setText(_translate("mainWindow", "Input"))
		self.label_4.setText(_translate("mainWindow", "Target"))
		self.label_7.setText(_translate("mainWindow", "Result"))
		self.menuFile.setTitle(_translate("mainWindow", "File"))
		self.actionOpen_Input.setText(_translate("mainWindow", "Open Input"))
		self.actionOpen_Target.setText(_translate("mainWindow", "Open Target"))
		self.actionSave_Result.setText(_translate("mainWindow", "Save"))
		self.actionExit.setText(_translate("mainWindow", "Exit"))
		self.actionTriangulate.setText(_translate("mainWindow","Create Triangulation"))
		self.actionMorph.setText(_translate("mainWindow","Morph"))

	def openInputFileDialog(self):
	    options = QtWidgets.QFileDialog.Options()
	    filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","Jpg Files (*.jpg);;PNG Files (*.png)",options=options)
	    if filename:
	    	self.input_image_points = []
	    	self.target_image_points = []
	    	self.input_image_arr = cv2.imread(filename)
	    	pixMap = QtGui.QPixmap(filename)
	    	self.input_image_label.setPixmap(pixMap)


	def openTargetFileDialog(self):
	    options = QtWidgets.QFileDialog.Options()
	    filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","Jpg Files (*.jpg);;PNG Files (*.png)",options=options)
	    if filename:
	    	self.target_image_arr = cv2.imread(filename)
	    	pixMap = QtGui.QPixmap(filename)
	    	self.target_image_label.setPixmap(pixMap)
	    	self.showInfo()    

	# Save the current image as output image when user want to save
	def saveImage(self):
		pixMap = self.result_image_label.pixmap()
		if pixMap is not None:
			pixMap.save("result.png","PNG")


	def triangulate(self):
		input_image = self.input_image_label.pixmap()
		target_image = self.target_image_label.pixmap()

		if input_image is None or target_image is None:
			self.showError()
			return
		
		if len(self.input_image_points) == len(self.target_image_points) and len(self.target_image_points)!=0 :
			# Input image triangulation
			size = self.input_image_arr.shape
			rect = (0,0,size[1],size[0])
			subdiv = cv2.Subdiv2D(rect)
			for i in self.input_image_points:
				subdiv.insert(i)

			triangularList = subdiv.getTriangleList()
			for i in range(triangularList.shape[0]):
				painter = QtGui.QPainter()
				painter.begin(input_image)
				painter.setPen(QtGui.QPen(QtCore.Qt.white,2,QtCore.Qt.SolidLine))
				painter.drawPolygon(self.createPolygon(triangularList[i]))
				painter.end()
				self.input_image_label.setPixmap(input_image)

			self.input_triangularList = triangularList

			# Target image triangulation
			size = self.target_image_arr.shape
			rect = (0,0,size[1],size[0])
			subdiv = cv2.Subdiv2D(rect)
			for i in self.target_image_points:
				subdiv.insert(i)

			triangularList = subdiv.getTriangleList()
			for i in range(triangularList.shape[0]):
				painter = QtGui.QPainter()
				painter.begin(target_image)
				painter.setPen(QtGui.QPen(QtCore.Qt.white,2,QtCore.Qt.SolidLine))
				painter.drawPolygon(self.createPolygon(triangularList[i]))
				painter.end()
				self.target_image_label.setPixmap(target_image)

			self.target_triangularList = triangularList



		else:
			self.showInfo()





	def morph(self):
		input_image = self.input_image_label.pixmap()
		target_image = self.target_image_label.pixmap()
		if input_image is not None or target_image is not None :
			input_list = self.input_triangularList
			target_list = self.target_triangularList
			result_image_arr = np.zeros(self.input_image_arr.shape)
			for i in range(result_image_arr.shape[0]):
				for j in range(result_image_arr.shape[1]):
					for index,k in enumerate(target_list):
						if isInside(k,i,j):
							estimation_matrix = self.estimate(input_list[index],target_list[index])
							new_coords = np.matmul(np.linalg.inv(estimation_matrix),np.array([[i],[j],[1]])).astype(int)
							result_image_arr[i,j,:] = self.input_image_arr[new_coords[0][0],new_coords[1][0],:]
							break
		
			row,column,channel = result_image_arr.shape
			qImg = QtGui.QImage(np.uint8(result_image_arr).copy(), column, row,3*column, QtGui.QImage.Format_RGB888).rgbSwapped()
			pixmap = QtGui.QPixmap.fromImage(qImg)
			self.result_image_label.setPixmap(pixmap)

		else:
			self.showError()

	def estimate(self,input_row,target_row):
		
		array_a = np.array([ [input_row[0],input_row[2],input_row[4]],
							[input_row[1],input_row[3],input_row[5]],
							[1,1,1] ],dtype=np.uint32)
		array_b = np.array([ [target_row[0],target_row[2],target_row[4]],
							[target_row[1],target_row[3],target_row[5]],
							[1,1,1] ],dtype=np.uint32)

		transformation = np.linalg.solve(array_a,array_b)
		return transformation


	def inputImageMouseClickEvent(self, QMouseEvent):
		input_image = self.input_image_label.pixmap()
		target_image = self.target_image_label.pixmap()
		if input_image is not None and target_image is not None:
			print ("Input image at ::", QMouseEvent.pos())
			x_value = QMouseEvent.pos().x()
			y_value = QMouseEvent.pos().y()
			if len(self.input_image_points) - len(self.target_image_points) > 0:
				self.showInfo()
				return
			self.input_image_points.append((x_value,y_value))
			painter = QtGui.QPainter()
			painter.begin(input_image)
			painter.setPen(QtGui.QPen(QtCore.Qt.red,6,QtCore.Qt.SolidLine))
			painter.setBrush(QtGui.QBrush(QtCore.Qt.red,QtCore.Qt.SolidPattern))
			painter.drawEllipse(x_value-3,y_value-3,6,6)
			painter.end()
			self.input_image_label.setPixmap(input_image)
		else:
			self.showInfo() 

	def targetImageMouseClickEvent(self, QMouseEvent):
		input_image = self.input_image_label.pixmap()
		target_image = self.target_image_label.pixmap()
		if input_image is not None and target_image is not None:
			print ("Target image at ::", QMouseEvent.pos())
			x_value = QMouseEvent.pos().x()
			y_value = QMouseEvent.pos().y()
			if len(self.target_image_points) - len(self.input_image_points) > 0:
				self.showInfo()
				return
			self.target_image_points.append((x_value,y_value))
			painter = QtGui.QPainter()
			painter.begin(target_image)
			painter.setPen(QtGui.QPen(QtCore.Qt.red,6,QtCore.Qt.SolidLine))
			painter.setBrush(QtGui.QBrush(QtCore.Qt.red,QtCore.Qt.SolidPattern))
			painter.drawEllipse(x_value-3,y_value-3,6,6)
			painter.end()
			self.target_image_label.setPixmap(target_image)
		else:
			self.showInfo() 


	def showInfo(self):
			self.information_dialog = information_dialog()
			self.information_dialog.setupUi(self.information_dialog)
			self.information_dialog.show()   

	def showError(self):
		self.popup_dialog = popup_dialog()
		self.popup_dialog.setupUi(self.popup_dialog)
		self.popup_dialog.show()

	def createPolygon(self,coordinates):
		polygon = QtGui.QPolygon()
		for i in range(3):
			polygon.append(QtCore.QPoint(coordinates[i*2],coordinates[i*2+1]))
		return polygon
=======
from MedianFilter import MedianFilter
from AverageFilter import AverageFilter
from GaussianFilter import GaussianFilter
from Transformer import Transformer 
import cv2
import numpy as np
from popup import Ui_Dialog

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
	    MainWindow.setObjectName("MainWindow")
	    MainWindow.resize(1440, 728)
	    self.centralwidget = QtWidgets.QWidget(MainWindow)
	    self.centralwidget.setObjectName("centralwidget")
	    self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
	    self.horizontalLayout.setObjectName("horizontalLayout")
	    self.label = QtWidgets.QLabel(self.centralwidget)
	    self.label.setText("")
	    self.label.setObjectName("label")
	    self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
	    MainWindow.setCentralWidget(self.centralwidget)
	    self.menubar = QtWidgets.QMenuBar(MainWindow)
	    self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 23))
	    self.menubar.setObjectName("menubar")
	    self.menuFile = QtWidgets.QMenu(self.menubar)
	    self.menuFile.setObjectName("menuFile")
	    self.menuFilters = QtWidgets.QMenu(self.menubar)
	    self.menuFilters.setObjectName("menuFilters")
	    self.menuAverage_Filters = QtWidgets.QMenu(self.menuFilters)
	    self.menuAverage_Filters.setObjectName("menuAverage_Filters")
	    self.menuGaussian_Filters = QtWidgets.QMenu(self.menuFilters)
	    self.menuGaussian_Filters.setObjectName("menuGaussian_Filters")
	    self.menuMedian_Filters = QtWidgets.QMenu(self.menuFilters)
	    self.menuMedian_Filters.setObjectName("menuMedian_Filters")
	    self.menuGeometric_Transforms = QtWidgets.QMenu(self.menubar)
	    self.menuGeometric_Transforms.setObjectName("menuGeometric_Transforms")
	    self.menuRotate = QtWidgets.QMenu(self.menuGeometric_Transforms)
	    self.menuRotate.setObjectName("menuRotate")
	    self.menuScale = QtWidgets.QMenu(self.menuGeometric_Transforms)
	    self.menuScale.setObjectName("menuScale")
	    self.menuTranslate = QtWidgets.QMenu(self.menuGeometric_Transforms)
	    self.menuTranslate.setObjectName("menuTranslate")
	    MainWindow.setMenuBar(self.menubar)
	    self.statusbar = QtWidgets.QStatusBar(MainWindow)
	    self.statusbar.setObjectName("statusbar")
	    MainWindow.setStatusBar(self.statusbar)

	    # Opening image
	    self.actionOpen = QtWidgets.QAction(MainWindow)
	    self.actionOpen.setObjectName("actionOpen")
	    self.actionOpen.triggered.connect(self.openInputFileDialog)
	    self.actionOpen.setShortcut("Ctrl+I")

	    # Saving Image
	    self.actionSave = QtWidgets.QAction(MainWindow)
	    self.actionSave.setObjectName("actionSave")
	    self.actionSave.triggered.connect(self.saveImage)
	    self.actionSave.setShortcut("Ctrl+S")

	    # Exit from program
	    self.actionExit = QtWidgets.QAction(MainWindow)
	    self.actionExit.setObjectName("actionExit")
	    self.actionExit.setShortcut("Ctrl+Q")
	    self.actionExit.triggered.connect(QtWidgets.qApp.quit)

	    # Gaussian Filter
	    self.gaussian3x3 = QtWidgets.QAction(MainWindow)
	    self.gaussian5x5 = QtWidgets.QAction(MainWindow)
	    self.gaussian7x7 = QtWidgets.QAction(MainWindow)
	    self.gaussian9x9 = QtWidgets.QAction(MainWindow)
	    self.gaussian11x11 = QtWidgets.QAction(MainWindow)
	    self.gaussian13x13 = QtWidgets.QAction(MainWindow)
	    self.gaussian15x15 = QtWidgets.QAction(MainWindow)
	    self.gaussian3x3.setObjectName("gaussian3x3")
	    self.gaussian5x5.setObjectName("gaussian5x5")
	    self.gaussian7x7.setObjectName("gaussian7x7")
	    self.gaussian9x9.setObjectName("gaussian9x9")
	    self.gaussian11x11.setObjectName("gaussian11x11")
	    self.gaussian13x13.setObjectName("gaussian13x13")
	    self.gaussian15x15.setObjectName("gaussian15x15")
	    self.gaussian3x3.triggered.connect(lambda: self.gaussian_filter(3))
	    self.gaussian5x5.triggered.connect(lambda: self.gaussian_filter(5))
	    self.gaussian7x7.triggered.connect(lambda: self.gaussian_filter(7))
	    self.gaussian9x9.triggered.connect(lambda: self.gaussian_filter(9))
	    self.gaussian11x11.triggered.connect(lambda: self.gaussian_filter(11))
	    self.gaussian13x13.triggered.connect(lambda: self.gaussian_filter(13))
	    self.gaussian15x15.triggered.connect(lambda: self.gaussian_filter(15))


	    # Average Filters
	    self.average3x3 = QtWidgets.QAction(MainWindow)
	    self.average5x5 = QtWidgets.QAction(MainWindow)
	    self.average7x7 = QtWidgets.QAction(MainWindow)
	    self.average9x9 = QtWidgets.QAction(MainWindow)
	    self.average11x11 = QtWidgets.QAction(MainWindow)
	    self.average13x13 = QtWidgets.QAction(MainWindow)
	    self.average15x15 = QtWidgets.QAction(MainWindow)
	    self.average3x3.setObjectName("average3x3")
	    self.average5x5.setObjectName("average5x5")
	    self.average7x7.setObjectName("average7x7")
	    self.average9x9.setObjectName("average9x9")
	    self.average11x11.setObjectName("average11x11")
	    self.average13x13.setObjectName("average13x13")
	    self.average15x15.setObjectName("average15x15")
	    self.average3x3.triggered.connect(lambda: self.average_filter(3))
	    self.average5x5.triggered.connect(lambda: self.average_filter(5))
	    self.average7x7.triggered.connect(lambda: self.average_filter(7))
	    self.average9x9.triggered.connect(lambda: self.average_filter(9))
	    self.average11x11.triggered.connect(lambda: self.average_filter(11))
	    self.average13x13.triggered.connect(lambda: self.average_filter(13))
	    self.average15x15.triggered.connect(lambda: self.average_filter(15))

	    # Median Filters
	    self.median3x3 = QtWidgets.QAction(MainWindow)
	    self.median5x5 = QtWidgets.QAction(MainWindow)
	    self.median7x7 = QtWidgets.QAction(MainWindow)
	    self.median9x9 = QtWidgets.QAction(MainWindow)
	    self.median11x11 = QtWidgets.QAction(MainWindow)
	    self.median13x13 = QtWidgets.QAction(MainWindow)
	    self.median15x15 = QtWidgets.QAction(MainWindow)
	    self.median3x3.setObjectName("median3x3")
	    self.median5x5.setObjectName("median5x5")
	    self.median7x7.setObjectName("median7x7")
	    self.median9x9.setObjectName("median9x9")
	    self.median11x11.setObjectName("median11x11")
	    self.median13x13.setObjectName("median13x13")
	    self.median15x15.setObjectName("median15x15")
	    self.median3x3.triggered.connect(lambda: self.median_filter(3))
	    self.median5x5.triggered.connect(lambda: self.median_filter(5))
	    self.median7x7.triggered.connect(lambda: self.median_filter(7))
	    self.median9x9.triggered.connect(lambda: self.median_filter(9))
	    self.median11x11.triggered.connect(lambda: self.median_filter(11))
	    self.median13x13.triggered.connect(lambda: self.median_filter(13))
	    self.median15x15.triggered.connect(lambda: self.median_filter(15))

	    # Rotations
	    self.rotate_10_degree_right = QtWidgets.QAction(MainWindow)
	    self.rotate_10_degree_left = QtWidgets.QAction(MainWindow)
	    self.rotate_10_degree_right.setObjectName("rotate_10_degree_right")
	    self.rotate_10_degree_left.setObjectName("rotate_10_degree_left")
	    # Function for left rotate is -10 and right rotate is +10 
	    self.rotate_10_degree_left.triggered.connect(lambda: self.rotate(np.pi/18))
	    self.rotate_10_degree_right.triggered.connect(lambda: self.rotate(-np.pi/18))

	    # Scaling
	    self.scale2x = QtWidgets.QAction(MainWindow)
	    self.scale1_2x = QtWidgets.QAction(MainWindow)
	    self.scale2x.setObjectName("scale2x")
	    self.scale1_2x.setObjectName("scale1_2x")
	    self.scale2x.triggered.connect(lambda: self.scale(2))
	    self.scale1_2x.triggered.connect(lambda: self.scale(0.5))

	    
	    # Translating
	    self.translateLeft = QtWidgets.QAction(MainWindow)
	    self.translateRight = QtWidgets.QAction(MainWindow)
	    self.translateLeft.setObjectName("translateLeft")
	    self.translateRight.setObjectName("translateRight")
	    self.translateUp = QtWidgets.QAction(MainWindow)
	    self.translateDown = QtWidgets.QAction(MainWindow)
	    self.translateUp.setObjectName("translateUp")
	    self.translateDown.setObjectName("translateDown")
	    self.translateLeft.triggered.connect(lambda: self.translate(-1))
	    self.translateRight.triggered.connect(lambda: self.translate(0))
	    self.translateDown.triggered.connect(lambda: self.translate(1))
	    self.translateUp.triggered.connect(lambda: self.translate(2))


	    

	    self.menuFile.addAction(self.actionOpen)
	    self.menuFile.addAction(self.actionSave)
	    self.menuFile.addAction(self.actionExit)
	    self.menuGaussian_Filters.addAction(self.gaussian3x3)
	    self.menuGaussian_Filters.addAction(self.gaussian5x5)
	    self.menuGaussian_Filters.addAction(self.gaussian7x7)
	    self.menuGaussian_Filters.addAction(self.gaussian9x9)
	    self.menuGaussian_Filters.addAction(self.gaussian11x11)
	    self.menuGaussian_Filters.addAction(self.gaussian13x13)
	    self.menuGaussian_Filters.addAction(self.gaussian15x15)
	    self.menuAverage_Filters.addAction(self.average3x3)
	    self.menuAverage_Filters.addAction(self.average5x5)
	    self.menuAverage_Filters.addAction(self.average7x7)
	    self.menuAverage_Filters.addAction(self.average9x9)
	    self.menuAverage_Filters.addAction(self.average11x11)
	    self.menuAverage_Filters.addAction(self.average13x13)
	    self.menuAverage_Filters.addAction(self.average15x15)
	    self.menuMedian_Filters.addAction(self.median3x3)
	    self.menuMedian_Filters.addAction(self.median5x5)
	    self.menuMedian_Filters.addAction(self.median7x7)
	    self.menuMedian_Filters.addAction(self.median9x9)
	    self.menuMedian_Filters.addAction(self.median11x11)
	    self.menuMedian_Filters.addAction(self.median13x13)
	    self.menuMedian_Filters.addAction(self.median15x15)
	    self.menuFilters.addAction(self.menuAverage_Filters.menuAction())
	    self.menuFilters.addAction(self.menuGaussian_Filters.menuAction())
	    self.menuFilters.addAction(self.menuMedian_Filters.menuAction())
	    self.menuRotate.addAction(self.rotate_10_degree_right)
	    self.menuRotate.addAction(self.rotate_10_degree_left)
	    self.menuScale.addAction(self.scale2x)
	    self.menuScale.addAction(self.scale1_2x)
	    self.menuTranslate.addAction(self.translateRight)
	    self.menuTranslate.addAction(self.translateLeft)
	    self.menuTranslate.addAction(self.translateUp)
	    self.menuTranslate.addAction(self.translateDown)
	    self.menuGeometric_Transforms.addAction(self.menuRotate.menuAction())
	    self.menuGeometric_Transforms.addAction(self.menuScale.menuAction())
	    self.menuGeometric_Transforms.addAction(self.menuTranslate.menuAction())
	    self.menubar.addAction(self.menuFile.menuAction())
	    self.menubar.addAction(self.menuFilters.menuAction())
	    self.menubar.addAction(self.menuGeometric_Transforms.menuAction())

	    self.retranslateUi(MainWindow)
	    QtCore.QMetaObject.connectSlotsByName(MainWindow)

	# Name strings of the each button
	def retranslateUi(self, MainWindow):
	    _translate = QtCore.QCoreApplication.translate
	    MainWindow.setWindowTitle(_translate("MainWindow", "Filtering & Geometric Transforms"))
	    self.menuFile.setTitle(_translate("MainWindow", "File"))
	    self.menuFilters.setTitle(_translate("MainWindow", "Filters"))
	    self.menuAverage_Filters.setTitle(_translate("MainWindow", "Average Filters"))
	    self.menuGaussian_Filters.setTitle(_translate("MainWindow", "Gaussian Filters"))
	    self.menuMedian_Filters.setTitle(_translate("MainWindow", "Median Filters"))
	    self.menuGeometric_Transforms.setTitle(_translate("MainWindow", "Geometric Transforms"))
	    self.menuRotate.setTitle(_translate("MainWindow", "Rotate"))
	    self.menuScale.setTitle(_translate("MainWindow", "Scale"))
	    self.menuTranslate.setTitle(_translate("MainWindow", "Translate"))
	    self.actionOpen.setText(_translate("MainWindow", "Open"))
	    self.actionSave.setText(_translate("MainWindow", "Save"))
	    self.actionExit.setText(_translate("MainWindow", "Exit"))
	    self.gaussian3x3.setText(_translate("MainWindow", "3x3"))
	    self.gaussian5x5.setText(_translate("MainWindow", "5x5"))
	    self.gaussian7x7.setText(_translate("MainWindow", "7x7"))
	    self.gaussian9x9.setText(_translate("MainWindow", "9x9"))
	    self.gaussian11x11.setText(_translate("MainWindow", "11x11"))
	    self.gaussian13x13.setText(_translate("MainWindow", "13x13"))
	    self.gaussian15x15.setText(_translate("MainWindow", "15x15"))
	    self.average3x3.setText(_translate("MainWindow", "3x3"))
	    self.average5x5.setText(_translate("MainWindow", "5x5"))
	    self.average7x7.setText(_translate("MainWindow", "7x7"))
	    self.average9x9.setText(_translate("MainWindow", "9x9"))
	    self.average11x11.setText(_translate("MainWindow", "11x11"))
	    self.average13x13.setText(_translate("MainWindow", "13x13"))
	    self.average15x15.setText(_translate("MainWindow", "15x15"))
	    self.median3x3.setText(_translate("MainWindow", "3x3"))
	    self.median5x5.setText(_translate("MainWindow", "5x5"))
	    self.median7x7.setText(_translate("MainWindow", "7x7"))
	    self.median9x9.setText(_translate("MainWindow", "9x9"))
	    self.median11x11.setText(_translate("MainWindow", "11x11"))
	    self.median13x13.setText(_translate("MainWindow", "13x13"))
	    self.median15x15.setText(_translate("MainWindow", "15x15"))
	    self.rotate_10_degree_right.setText(_translate("MainWindow", "Rotate 10 Degree Right"))
	    self.rotate_10_degree_left.setText(_translate("MainWindow", "Rotate 10 Degree Left"))
	    self.scale2x.setText(_translate("MainWindow", "2x"))
	    self.scale1_2x.setText(_translate("MainWindow", "1/2x"))
	    self.translateRight.setText(_translate("MainWindow", "Right"))
	    self.translateLeft.setText(_translate("MainWindow", "Left"))
	    self.translateUp.setText(_translate("MainWindow", "Up"))
	    self.translateDown.setText(_translate("MainWindow", "Down"))



	def openInputFileDialog(self):
	    options = QtWidgets.QFileDialog.Options()
	    filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","PNG Files (*.png);;Jpg Files (*.jpg)",options=options)
	    if filename:
	    	self.label_img = cv2.imread(filename)
	    	pixMap = QtGui.QPixmap(filename)
	    	self.label.setPixmap(pixMap)

	# Save the current image as output image when user want to save
	def saveImage(self):
		pixMap = self.label.pixmap()
		pixMap.save("output.png","PNG")


	def gaussian_filter(self,filter_size):
		raw_image = self.label.pixmap()
		if raw_image is not None:
			filter = GaussianFilter(self.label_img,filter_size)
			self.label_img, pixMap = filter.apply_filter()
			self.label.setPixmap(pixMap)
		else:
			self.Ui_Dialog = Ui_Dialog()
			self.Ui_Dialog.setupUi(self.Ui_Dialog)
			self.Ui_Dialog.show()


	def average_filter(self,filter_size):
		raw_image = self.label.pixmap()
		if raw_image is not None:
			filter = AverageFilter(self.label_img,filter_size)
			self.label_img , pixMap = filter.apply_filter()
			self.label.setPixmap(pixMap)
		else:
			self.Ui_Dialog = Ui_Dialog()
			self.Ui_Dialog.setupUi(self.Ui_Dialog)
			self.Ui_Dialog.show()

	def median_filter(self,filter_size):
		raw_image = self.label.pixmap()
		if raw_image is not None:
			filter = MedianFilter(self.label_img,filter_size)
			self.label_img , pixMap = filter.apply_filter()
			self.label.setPixmap(pixMap)
		else:
			self.Ui_Dialog = Ui_Dialog()
			self.Ui_Dialog.setupUi(self.Ui_Dialog)
			self.Ui_Dialog.show()

	def rotate(self,degree):
		raw_image = self.label.pixmap()
		if raw_image is not None:
			transformer = Transformer(self.label_img,"rotate")
			self.label_img , pixMap = transformer.rotate(degree)
			self.label.setPixmap(pixMap)
		else:
			self.Ui_Dialog = Ui_Dialog()
			self.Ui_Dialog.setupUi(self.Ui_Dialog)
			self.Ui_Dialog.show()


	def scale(self,scale_val):
		raw_image = self.label.pixmap()
		if raw_image is not None:
			transformer = Transformer(self.label_img,"scale")
			self.label_img , pixMap = transformer.scale(scale_val)
			self.label.setPixmap(pixMap)
		else:
			self.Ui_Dialog = Ui_Dialog()
			self.Ui_Dialog.setupUi(self.Ui_Dialog)
			self.Ui_Dialog.show()

	def translate(self,direction):
		raw_image = self.label.pixmap()
		if raw_image is not None:
			transformer = Transformer(self.label_img,"translate")
			self.label_img , pixMap = transformer.translate(direction)
			self.label.setPixmap(pixMap)
		else:
			self.Ui_Dialog = Ui_Dialog()
			self.Ui_Dialog.setupUi(self.Ui_Dialog)
			self.Ui_Dialog.show()
>>>>>>> CV-HW2/master
