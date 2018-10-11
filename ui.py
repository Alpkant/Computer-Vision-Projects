from PyQt5 import QtCore, QtGui, QtWidgets 
from Histogram import Histogram
from HistogramMatcher import HistogramMatcher
from popup import Ui_Dialog

class MainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1920, 1080)
        
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
        self.input_hist_label = QtWidgets.QLabel(self.input_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_hist_label.sizePolicy().hasHeightForWidth())
        self.input_hist_label.setSizePolicy(sizePolicy)
        self.input_hist_label.setText("")
        self.input_hist_label.setScaledContents(False)
        self.input_hist_label.setObjectName("input_hist_label")
        self.verticalLayout_5.addWidget(self.input_hist_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
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
        self.verticalLayout_6.addWidget(self.target_image_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.target_hist_label = QtWidgets.QLabel(self.target_frame)
        self.target_hist_label.setText("")
        self.target_hist_label.setObjectName("target_hist_label")
        self.verticalLayout_6.addWidget(self.target_hist_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
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
        self.result_hist_label = QtWidgets.QLabel(self.result_frame)
        self.result_hist_label.setText("")
        self.result_hist_label.setObjectName("result_hist_label")
        self.verticalLayout_7.addWidget(self.result_hist_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
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

        self.actionEqualizeHistogram = QtWidgets.QAction(mainWindow)
        self.actionEqualizeHistogram.setObjectName("actionEqualizeHistogram")
        self.actionEqualizeHistogram.setShortcut("Ctrl+E")
        self.actionEqualizeHistogram.triggered.connect(self.equalizeHistogram)


        self.menuFile.addAction(self.actionOpen_Input)
        self.menuFile.addAction(self.actionOpen_Target)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.actionEqualizeHistogram)   

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Histogram Equalization"))
        self.label.setText(_translate("mainWindow", "Input"))
        self.label_4.setText(_translate("mainWindow", "Target"))
        self.label_7.setText(_translate("mainWindow", "Result"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.actionOpen_Input.setText(_translate("mainWindow", "Open Input"))
        self.actionOpen_Target.setText(_translate("mainWindow", "Open Target"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
        self.actionEqualizeHistogram.setText(_translate("mainWindow","Equalize Histogram"))


    def openInputFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","PNG Files (*.png);;Jpg Files (*.jpg)",options=options)
        if filename:
            pixMap = QtGui.QPixmap(filename)
            self.input_image_label.setPixmap(pixMap)
            hist = Histogram(filename)
            output = "input_histogram.png"
            hist.createHistogramPlotImage(output)
            pixMapHist = QtGui.QPixmap(output)
            self.input_hist_label.setPixmap(pixMapHist)
            # Save the object for matching
            self.input_hist = hist


    def openTargetFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","PNG Files (*.png);;JPG Files (*.jpg)",options=options)
        if filename:
            pixMap = QtGui.QPixmap(filename)
            self.target_image_label.setPixmap(pixMap)      
            hist = Histogram(filename)
            output = "target_histogram.png"
            hist.createHistogramPlotImage(output)
            pixMapHist = QtGui.QPixmap(output)
            self.target_hist_label.setPixmap(pixMapHist)  
            # Save the object for matching
            self.target_hist = hist

                     

    def equalizeHistogram(self):
        if(self.input_image_label.pixmap() is not None and self.target_image_label.pixmap() is not None):
            filename = "result.png"
            matcher = HistogramMatcher(self.input_hist,self.target_hist,filename)
            matcher.createLookupTable()
            matcher.constructImage()
            # Show new image
            pixMap = QtGui.QPixmap(filename)
            self.result_image_label.setPixmap(pixMap)
            # Create histogram of the result
            hist = Histogram(filename)
            hist_filename = "resultHistogram.png"
            hist.createHistogramPlotImage(hist_filename)
            # Show histogram
            pixMapHist = QtGui.QPixmap(hist_filename)
            self.result_hist_label.setPixmap(pixMapHist)
            self.result_hist = hist
        else:
            self.Ui_Dialog = Ui_Dialog()
            self.Ui_Dialog.setupUi(self.Ui_Dialog)
            self.Ui_Dialog.show()            

