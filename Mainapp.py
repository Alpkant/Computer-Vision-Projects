import sys
from PyQt5.QtWidgets import QDialog,QMainWindow, QApplication
from ui import MainWindow

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
