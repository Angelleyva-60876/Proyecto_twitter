from glob import glob
import os
from statistics import mode
import sys
from os.path import dirname, realpath, join
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUiType
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from PyQt5 import QtCore
from stop_words import get_stop_words
from model.neuronalNewtork import NeuralNetwork
from model.WorldCloud import word
from model.Histograma import Histogram

scriptDir = dirname(realpath(__file__))
From_Main,_ = loadUiType(join(dirname(__file__), "../view/view_win.ui"))


class Controlador(QWidget,From_Main):
    df = []
    path = ""
    palabras = []
    listaPalabras = ""
    info = ""
    texto = ''
    data = ''

    def __init__(self):
        super(Controlador, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.word = word
        self.hist = Histogram

        self.question = [0 for i in range(0, 8)]

        self.ButtonAbrir.clicked.connect(self.AbrirArchivo)
        self.BtnGenerar.clicked.connect(self.DatosColumnas)
        self.BtnPClave.clicked.connect(self.filtroPalabras)
        self.BtnGuardar.clicked.connect(self.guardarArchivoFiltrado)
        self.BtnWordCloud.clicked.connect(self.crear_wordcloud)
        self.BtnHistograma.clicked.connect(self.crear_histograma)

        self.BtnEntrenar.clicked.connect(self.train)
        self.BtnEnviar.clicked.connect(self.send) 

        self.checkBoxAmigos.stateChanged.connect(self.onStateChanged)
        self.checkBoxFamilia.stateChanged.connect(self.onStateChanged)
        self.checkBoxFiesta.stateChanged.connect(self.onStateChanged)
        self.checkBoxGames.stateChanged.connect(self.onStateChanged)
        self.checkBoxHogar.stateChanged.connect(self.onStateChanged)
        self.checkBoxPlaya.stateChanged.connect(self.onStateChanged)
        self.checkBoxVacaciones.stateChanged.connect(self.onStateChanged)
        self.checkBoxVerano.stateChanged.connect(self.onStateChanged)

    def AbrirArchivo(self):
        global path
        try:
            path = QFileDialog.getOpenFileName(
                self, 'Abrir archivo', os.getenv('HOME'), 'CSV(*.csv)')[0]
            global df
            df = self.all_data = pd.read_csv(path)
        except:
            print(path)

    def getPalabras(self):
        pass

    def filtroPalabras(self):
        global palabras
        palabras = self.FiltrarPalabra.text().split()
        count = 0
        palabrasString = []

        for i in palabras:
            count = count + 1
            if count < len(palabras):
                palabrasString.append(i + "|")
            else:
                palabrasString.append(i)

        print(palabrasString)
        palabras = "".join(palabrasString)
        print(palabras)
        self.FiltrarPalabra.setText("")
        return palabras

    def guardarArchivoFiltrado(self):
        global palabras
        palabrasfiltradas = df[df['Texto'].str.contains(
            palabras, case=False, na=False, regex=True)]
        palabrasfiltradas.to_csv(os.path.abspath("PalabraClave.csv"))

    def DatosColumnas(self):
        numColomn = self.spinBox.value()
        if numColomn == 0:
            Numfilas = len(self.all_data.index)
        else:
            Numfilas = numColomn
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(Numfilas)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(Numfilas):
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        
    def crear_wordcloud(self):
        try:
            self.word.WordCloud(self)
        except:
            QMessageBox.about(self, "Error", "No se selecciono un archivo")
            
    def crear_histograma(self):
        try:
            self.hist.Histograma(self)
        except:
            QMessageBox.about(self, "Error", "No se selecciono un archivo")

    def load_data(self):
        global df
        df = self.all_data = pd.read_csv(path)
        
        input_columns =  self.all_data[['Amigos','Familia','Fiesta','Games','Hogar','Playa','Vacaciones','Verano']]
        output_column = self.all_data[['Salida']]
        
        self.training_set_inputs = input_columns[:].values
        self.training_set_outputs = output_column.values
        print(self.training_set_inputs)
        print(self.training_set_outputs)

    def train(self):
        self.load_data()
        self.neural_network = NeuralNetwork()
        self.neural_network.train(self.training_set_inputs, self.training_set_outputs)
        self.show_dialog()

    def show_dialog(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("")
        dlg.setText("¡El entrenamiento ha finalizado!")
        button = dlg.exec()
    
    def onStateChanged(self, state):
        
        if state == QtCore.Qt.Checked:
            if self.sender() == self.checkBoxAmigos:
                self.question[0] = 1
            elif self.sender() == self.checkBoxFamilia:
                self.question[1] = 1
            elif self.sender() == self.checkBoxFiesta:
                self.question[2] = 1
            elif self.sender() == self.checkBoxGames:
                self.question[3] = 1
            elif self.sender() == self.checkBoxHogar:
                self.question[4] = 1
            elif self.sender() == self.checkBoxPlaya:
                self.question[5] = 1
            elif self.sender() == self.checkBoxVacaciones:
                self.question[6] = 1
            elif self.sender() == self.checkBoxVerano:
                self.question[7] = 1
        else:
            if self.sender() == self.checkBoxAmigos:
                self.question[0] = 0
            elif self.sender() == self.checkBoxFamilia:
                self.question[1] = 0
            elif self.sender() == self.checkBoxFiesta:
                self.question[2] = 0
            elif self.sender() == self.checkBoxGames:
                self.question[3] = 0
            elif self.sender() == self.checkBoxHogar:
                self.question[4] = 0
            elif self.sender() == self.checkBoxPlaya:
                self.question[5] = 0
            elif self.sender() == self.checkBoxVacaciones:
                self.question[6] = 0
            elif self.sender() == self.checkBoxVerano:
                self.question[7] = 0
        print(self.question)
    
    def send(self):
        print (self.neural_network.think(np.array(self.question)))
        ans = np.array2string(self.neural_network.think(np.array(self.question)))
        self.lineEditAns.setText(ans)

app = QApplication(sys.argv)
sheet = Controlador()
sheet.show()
sys.exit(app.exec_())
 