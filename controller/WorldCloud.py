import os
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
class word:
    df = []
    archivo = ""
    
    def abrir_archivo(self):
        global archivo
        archivo = QFileDialog.getOpenFileName(
            parent=self,
            caption="Seleccione su archivo para filtrar",
            directory = os.getcwd(),
            filter='csv files (*csv*);; All files *.*')
        global df
        
        df= pd.read_csv(archivo[0], index_col=0,encoding='latin-1')

        return archivo
    
    def WordCloud(self):
        global info 
        frases = df["Texto"]
        frasesArreglo = []

        for i in frases:
            frasesArreglo.append(i)
        info = "".join(frasesArreglo)

        # generar stopwords
        stop_wordsunicos = ['Ã', 'Â', 'ð', 'ðŸ', 'Ÿ', '€', '@', '¢', 'https', 'âœ' 'âœˆï', 'ˆ',
                            'Ÿ', 'â', 'œ', 'ï', 'estÃ', 'dÃ', 'mÃ', 'ä', 'https://t.co/', 't', 'co', 'í', 'n']
        stop_words = stopwords.words('spanish')
        stop_words.extend(stop_wordsunicos)

        for val in df.Texto:

            # typecaste each val to string
            val = str(val)

            # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        info += " ".join(tokens)+" "

        wordcloud = WordCloud(width=800, height=800,
                              background_color='white',
                              stopwords=stop_words,
                              min_font_size=10).generate(info)

        # plot the WordCloud image
        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()