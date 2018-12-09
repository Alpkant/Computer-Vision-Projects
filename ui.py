from PyQt5 import QtCore, QtGui, QtWidgets
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