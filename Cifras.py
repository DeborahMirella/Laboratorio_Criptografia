from Auxiliares import ALFABETO, Normaliza

def cesar_cifrar(texto, k):

    Texto = Normaliza(texto)
    Resultado = ""
    for char in Texto:
        if char in ALFABETO:
            Original = ALFABETO.find(char)
            Cifrada = (Original + k) % 26
            Resultado += ALFABETO[Cifrada]
        else:
            Resultado += char
    return Resultado

def cesar_decifrar(texto, k):

    return cesar_cifrar(texto, -k)

def vigenere_cifrar(texto, chave):

    Texto = Normaliza(texto)
    Chave = Normaliza(chave).replace(' ', '')
    Resultado = ""
    Indice_Chave = 0

    for char in Texto:
        if char in ALFABETO:
            Deslocamento = ALFABETO.find(Chave[Indice_Chave])
            Original = ALFABETO.find(char)
            Cifrada = (Original + Deslocamento) % 26
            Resultado += ALFABETO[Cifrada]
            Indice_Chave = (Indice_Chave + 1) % len(Chave)
        else:
            Resultado += char
    return Resultado

def vigenere_decifrar(texto, chave):

    Chave = Normaliza(chave).replace(' ', '')
    Chave_Inversa = ""

    for char in Chave:
        Deslocamento = ALFABETO.find(char)
        Deslocamento_Inverso = (26 - Deslocamento) % 26
        Chave_Inversa += ALFABETO[Deslocamento_Inverso]
    return vigenere_cifrar(texto, Chave_Inversa)
