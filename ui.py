# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1440, 1080)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 74, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 40, 74, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(950, 50, 74, 18))
        self.label_3.setObjectName("label_3")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(30, 70, 411, 841))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        
        self.input_image_label = QtWidgets.QLabel(self.frame_1)
        self.input_image_label.setGeometry(QtCore.QRect(70, 10, 277, 427))
        self.input_image_label.setText("")
        self.input_image_label.setObjectName("input_image_label")
        
        self.input_hist_label = QtWidgets.QLabel(self.frame_1)
        self.input_hist_label.setGeometry(QtCore.QRect(10, 450, 381, 381))
        self.input_hist_label.setText("")
        self.input_hist_label.setObjectName("input_hist_label")


        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(500, 70, 411, 841))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.target_image_label = QtWidgets.QLabel(self.frame_2)
        self.target_image_label.setGeometry(QtCore.QRect(70, 10, 277, 427))
        self.target_image_label.setText("")
        self.target_image_label.setObjectName("target_image_label")
        
        self.target_hist_label = QtWidgets.QLabel(self.frame_2)
        self.target_hist_label.setGeometry(QtCore.QRect(10, 450, 381, 381))
        self.target_hist_label.setText("")
        self.target_hist_label.setObjectName("target_hist_label")


        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(950, 70, 411, 841))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        self.final_image_label = QtWidgets.QLabel(self.frame_3)
        self.final_image_label.setGeometry(QtCore.QRect(70, 10, 277, 427))
        self.final_image_label.setText("")
        self.final_image_label.setObjectName("final_image_label")
        
        self.final_hist_label = QtWidgets.QLabel(self.frame_3)
        self.final_hist_label.setGeometry(QtCore.QRect(10, 450, 381, 381))
        self.final_hist_label.setText("")
        self.final_hist_label.setObjectName("final_hist_label")

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
        self.label_2.setText(_translate("mainWindow", "Target"))
        self.label_3.setText(_translate("mainWindow", "Result"))
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

    def openTargetFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","PNG Files (*.png);;Jpg Files (*.jpg)",options=options)
        if filename:
            pixMap = QtGui.QPixmap(filename)
            self.target_image_label.setPixmap(pixMap)      


