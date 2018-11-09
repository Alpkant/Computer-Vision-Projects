from PyQt5 import QtCore, QtGui, QtWidgets
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