import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox
from stop_words import get_stop_words
import os

class Histogram:
    df = ''
    texto = ''
    data = ''
    palabras_irrelevantes = []
    
    def Histograma(self):
        global df
        
        df= pd.read_csv(os.path.abspath("PalabraClave.csv"))
        a = list(df['Texto'])
        global texto
        texto = ' '.join(str(e) for e in a)
        caracteres = ",;:.\n!\"'ÃÂðŸ€@¢âœïˆâïÃäº¾©*¡#£»´²³±¦"
        for caracter in caracteres:
            texto = texto.replace(caracter,"")
        texto= texto.lower()
        palabras = texto.split(" ")
        
        global palabras_irrelevantes
        palabras_irrelevantes = get_stop_words('spanish')
        stop_wordsunicos = ['Ã', 'Â', 'ð','ðŸ', 'Ÿ', '€','@', '¢' ,'https', 'âœ' 'âœˆï','ˆ','Ÿ','â','œ','ï', 'estÃ','dÃ','mÃ', 'ä', 'https://t.co/', 't', 'co', 'í', 'n']
        palabras_irrelevantes.extend(stop_wordsunicos)

        for i in range (len(palabras_irrelevantes)):
            try:
                while True:
                    palabras.remove(palabras_irrelevantes[i-1])
            except ValueError:
                pass
        diccionario_frecuencias = {}
        
        print(palabras)

        for palabra in palabras:
            if palabra in diccionario_frecuencias:
                diccionario_frecuencias[palabra] += 1
            else:
                diccionario_frecuencias[palabra] = 1

        for palabra in diccionario_frecuencias:
            frecuencia = diccionario_frecuencias[palabra]
        data = palabras
        
        n, bins, patches = plt.hist(data)
        plt.xlabel("Palabras")
        plt.ylabel("Frecuencia")
        plt.title("Histograma")
        plt.show()