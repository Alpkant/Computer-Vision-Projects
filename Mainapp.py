import sys
from PyQt5.QtWidgets import QDialog,QMainWindow, QApplication
from ui import MainWindow

""" 
In order to run the program you should execute the following command
in the command line: python Mainapp.py
You need Mainapp.py, popup.py, ui.py, Histogram.py and HistogramMatcher.py 
files in order to run the program.
"""

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.show()  

app = QApplication(sys.argv)
window = AppWindow()
window.show()
sys.exit(app.exec_())
