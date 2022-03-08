import sys

from view.view_winmain import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui,QtWidgets
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = Ui_Form()
        self.view.setupUi(self)
        
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()