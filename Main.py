import sys
from view.view_win import Ui_Form
from controller.Controller import MainWindow
from view.view_winmain import Ui_Form
from controller.Controller import Controller
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui,QtWidgets
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    app.exec_()