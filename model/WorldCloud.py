import os
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
class word:
    df = []
    archivo = ""
    
    def WordCloud(self):
        global info
        df = self.all_data = pd.read_csv("PalabraClave.csv")
        frases = df["Texto"]
        frasesArreglo = []

        for i in frases:
            frasesArreglo.append(i)
        info = "".join(frasesArreglo)

        stop_wordsunicos = ['Ã', 'Â', 'ð', 'ðŸ', 'Ÿ', '€', '@', '¢', 'https', 'âœ' 'âœˆï', 'ˆ',
                            'Ÿ', 'â', 'œ', 'ï', 'estÃ', 'dÃ', 'mÃ', 'ä', 'https://t.co/', 't', 'co', 'í', 'n']
        stop_words = stopwords.words('spanish')
        stop_words.extend(stop_wordsunicos)

        for val in df.Texto:

            val = str(val)
        tokens = val.split()

        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        info += " ".join(tokens)+" "

        wordcloud = WordCloud(width=800, height=800,
                              background_color='white',
                              stopwords=stop_words,
                              min_font_size=10).generate(info)

        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()