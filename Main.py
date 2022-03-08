import sys

<<<<<<< HEAD
from view.view_win import Ui_Form
from controller.Controller import MainWindow
=======
from view.Main import Ui_Form
from controller.Controller import Controller
>>>>>>> 00ee73d4107f0fd285a62d36e4bb32d80c901096
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui,QtWidgets

class Controller(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.view = Ui_Form()
        self.view.setupUi(self)
        self.controller = Controller   
    
    def conexiones(self):
        
        self.view.ButtonAbrir.clicked.connect(self.ButtonAbrir)
        self.view.BtnGenerar.clicked.connect(self.DatosColumnas)
        self.view.BtnPClave.clicked.connect(self.filtroPalabras)
        self.view.BtnGuardar.clicked.connect(self.guardarArchivoFiltrado)
        self.view.BtnWordCloud.clicked.connect(self.WordCloud)
    
    def AbrirArchivo(self):
        self.controller.AbrirArchivo(self)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    app.exec_()