import collections
import unicodedata
import re

# Constantes fundamentais para a análise
ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
IC_PORTUGUES = 0.074

# Frequência de referência das letras em português
FREQUENCIA_PT = {
    'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99, 'e': 12.57, 'f': 1.02, 'g': 1.30, 
    'h': 1.28, 'i': 6.18, 'j': 0.40, 'k': 0.02, 'l': 2.78, 'm': 4.74, 'n': 5.05, 
    'o': 10.73, 'p': 2.52, 'q': 1.20, 'r': 6.53, 's': 7.81, 't': 4.34, 'u': 4.63, 
    'v': 1.67, 'w': 0.01, 'x': 0.21, 'y': 0.01, 'z': 0.47
}

# Pontuação de bônus para bigramas comuns
PONTUACAO_BIGRAMAS = {
    'de': 4.0, 'os': 3.5, 'as': 3.0, 'ra': 2.5, 'co': 2.0, 'nt': 2.0, 'en': 2.0, 
    'es': 1.8, 'ar': 1.8, 'do': 1.7, 'ad': 1.5, 'st': 1.5, 'qu': 1.5, 'or': 1.4, 
    'er': 1.3, 'em': 1.2, 'an': 1.1, 'se': 1.0, 'io': 1.0
}

def NormalizaTexto(texto, manter_espacos=False):

    texto_min = texto.lower()
    texto_sem_acentos = ''.join(c for c in unicodedata.normalize('NFD', texto_min) if unicodedata.category(c) != 'Mn')
    regex = r'[^a-z\s]' if manter_espacos else r'[^a-z]'
    return re.sub(regex, '', texto_sem_acentos)

def ScorePlausibilidade(texto):

    texto_limpo = NormalizaTexto(texto)
    if not texto_limpo: return -float('inf')
    penalidade_letras = sum(abs(((collections.Counter(texto_limpo).get(letra, 0) / len(texto_limpo)) * 100) - freq_ref) for letra, freq_ref in FREQUENCIA_PT.items())
    bonus_bigramas = sum(PONTUACAO_BIGRAMAS.get(texto_limpo[i:i+2], 0) for i in range(len(texto_limpo) - 1))
    return (bonus_bigramas * 10) - penalidade_letras
