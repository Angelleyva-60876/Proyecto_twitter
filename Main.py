import sys

from controller.Controller import Controller
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui,QtWidgets
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    app.exec_()