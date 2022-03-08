import sys

from view.view_win import Ui_Form
from controller.Controller import MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui,QtWidgets

class MainWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.view = Ui_Form()
        self.view.setupUi(self)   
    
    def conexiones(self):
        
        self.view.ButtonAbrir.clicked.connect(self.ButtonAbrir())
        self.view.BtnGenerar.clicked.connect(self.DatosColumnas())
        self.view.BtnPClave.clicked.connect(self.filtroPalabras())
        self.view.BtnGuardar.clicked.connect(self.guardarArchivoFiltrado)
        self.view.BtnWordCloud.clicked.connect(self.WordCloud)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()