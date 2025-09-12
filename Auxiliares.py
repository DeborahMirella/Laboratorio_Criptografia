import unicodedata
import re
import collections

ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

FREQUENCIA = {
    'A': 14.63, 'B': 1.04, 'C': 3.88, 'D': 4.99, 'E': 12.57, 'F': 1.02, 
    'G': 1.30, 'H': 1.28, 'I': 6.18, 'J': 0.40, 'K': 0.02, 'L': 2.78, 
    'M': 4.74, 'N': 5.05, 'O': 10.73, 'P': 2.52, 'Q': 1.20, 'R': 6.53, 
    'S': 7.81, 'T': 4.34, 'U': 4.63, 'V': 1.67, 'W': 0.01, 'X': 0.21, 
    'Y': 0.01, 'Z': 0.47
}

def Normaliza(texto):

    Texto_sem_Acentos = ''.join(c for c in unicodedata.normalize('NFD', texto.upper())
                                if unicodedata.category(c) != 'Mn')
    Texto_Limpo = re.sub(r'[^A-Z\s]', '', Texto_sem_Acentos)

    return Texto_Limpo

def Score_Plausibilidade(texto):
    
    Frequencias_Texto = collections.Counter(Normaliza(texto).replace(' ', ''))
    Total_Letras = sum(Frequencias_Texto.values())
    Score = 0
    if Total_Letras == 0: return float('inf')

    for Letra, Freq_Ref in FREQUENCIA.items():
        Freq_Atual = (Frequencias_Texto.get(Letra, 0) / Total_Letras) * 100
        Score += abs(Freq_Atual - Freq_Ref)
    return Score
