# Author:
# Alperen Kantarcı
# 150140140

""" 
In order to run the program you should execute the following command
in the command line: python Mainapp.py
<<<<<<< HEAD
You need Mainapp.py, popup.py, ui.py and information.py
=======
You need Mainapp.py, popup.py, ui.py, Histogram.py and HistogramMatcher.py 
>>>>>>> CV-HW2/master
files in order to run the program.
"""

from PyQt5 import QtCore, QtGui, QtWidgets

<<<<<<< HEAD
class popup_dialog(QtWidgets.QDialog):
=======
class Ui_Dialog(QtWidgets.QDialog):
>>>>>>> CV-HW2/master
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(669, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error"))
<<<<<<< HEAD
        self.label.setText(_translate("Dialog", "You should insert two images before morphing or triangulation."))
=======
        self.label.setText(_translate("Dialog", "You should insert an image before applying any operation."))
>>>>>>> CV-HW2/master

