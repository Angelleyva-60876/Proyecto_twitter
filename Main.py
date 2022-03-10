import sys
from view.view_win import Ui_Form
from controller.Controller import Controlador
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui,QtWidgets
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Controlador()
    window.show()
    app.exec_()