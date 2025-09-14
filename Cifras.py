from Auxiliares import ALFABETO, NormalizaTexto

def CesarCifrar(texto, k):

    texto_proc = NormalizaTexto(texto, manter_espacos=True)
    resultado = ""
    for char in texto_proc:
        if char in ALFABETO:
            resultado += ALFABETO[(ALFABETO.find(char) + k) % 26]
        else:
            resultado += char
    return resultado

def CesarDecifrar(texto, k):

    return CesarCifrar(texto, -k)

def VigenereCifrar(texto, chave_str):

    chave_proc = NormalizaTexto(chave_str)
    key_indices = [ALFABETO.find(k) for k in chave_proc]
    texto_proc = NormalizaTexto(texto, manter_espacos=True)
    resultado, indice_chave = [], 0
    for char in texto_proc:
        if char in ALFABETO:
            deslocamento = key_indices[indice_chave % len(key_indices)]
            resultado.append(ALFABETO[(ALFABETO.find(char) + deslocamento) % 26])
            indice_chave += 1
        else:
            resultado.append(char)
    return "".join(resultado)

def VigenereDecifrar(ciphertext, key_str):

    chave_proc = NormalizaTexto(key_str)
    key_indices = [ALFABETO.find(k) for k in chave_proc]
    texto_proc = NormalizaTexto(ciphertext, manter_espacos=True)
    resultado, indice_chave = [], 0
    for char in texto_proc:
        if char in ALFABETO:
            deslocamento = key_indices[indice_chave % len(key_indices)]
            resultado.append(CesarDecifrar(char, deslocamento))
            indice_chave += 1
        else:
            resultado.append(char)
    return "".join(resultado)
