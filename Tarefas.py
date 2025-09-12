from Cifras import cesar_cifrar, cesar_decifrar, vigenere_cifrar, vigenere_decifrar
from Ataques import Ataque_Forca_Bruta_Cesar, Ataque_Frequencia_Cesar, Ataque_Vigenere

def Tarefa_1():

    print("Tarefa 1: Validação da Cifra de César")
    Texto = "SEGURANCA DA INFORMACAO E IMPORTANTE"
    Chave = 3
    Cifrado = cesar_cifrar(Texto, Chave)
    Decifrado = cesar_decifrar(Cifrado, Chave)
    print(f"Original: {Texto}\nCifrado:  {Cifrado}\nDecifrado:{Decifrado}\n")


def Tarefa_2():

    print("Tarefa 2: Ataque de Força Bruta em César")

    ciphertext = "SXBN N DV XCRVX NBCDMJWCN MJ DOVP"

    print(f"Ciphertext: {ciphertext}")
    candidatos = Ataque_Forca_Bruta_Cesar(ciphertext)
    
    print("\nLista completa dos 25 candidatos (ranqueados por plausibilidade):")
    for i, candidato in enumerate(candidatos):
        print(f"  #{i+1}: Chave k={candidato['chave']}, Score={candidato['score']:.2f} -> '{candidato['texto']}'")
    print("\n")

def Tarefa_3():

    print("Tarefa 3: Ataque por Análise de Frequência em César")

    Ciphertext = "RKRHLV UV UZTZFERIZF V VWZTRQ TFEKIR JVEYRJ WIRTRJ"
    print(f"Ciphertext: {Ciphertext}\n")

    Chave_Hipotese_Inicial = 13
    Plaintext_Hipotese_Inicial = cesar_decifrar(Ciphertext, Chave_Hipotese_Inicial)
    
    print("Resultado da Hipótese Inicial ('R' -> 'E'):")
    print(f"  Chave k={Chave_Hipotese_Inicial}, Plaintext='{Plaintext_Hipotese_Inicial}'")

    Chave_Final, Plaintext_Final = Ataque_Frequencia_Cesar(Ciphertext)
    
    print("\nResultado Final (Melhor Hipótese Encontrada):")
    print(f"  Chave k={Chave_Final}, Plaintext='{Plaintext_Final}'\n")


def Tarefa_4():

    print("Tarefa 4: Validação da Cifra de Vigenère")
    Texto = "CIFRA DE VIGENERE E UM POUCO MAIS FORTE"
    Chave = "SEGURO"
    Cifrado = vigenere_cifrar(Texto, Chave)
    Decifrado = vigenere_decifrar(Cifrado, Chave)
    print(f"Original: {Texto}\nCifrado:  {Cifrado}\nDecifrado:{Decifrado}\n")


def Tarefa_5():
    print("Tarefa 5: Quebra da Cifra de Vigenère")
    Ciphertext = "ECXPFI WO QQYFO LX JWOXBSZX"
    print(f"Ciphertext: {Ciphertext}\n")
    Ataque_Vigenere(Ciphertext)
    print("\n")

if __name__ == "__main__":
    print("Iniciando Tarefas\n")

    Tarefa_1()
    print("-" * 60)
    Tarefa_2()
    print("-" * 60)
    Tarefa_3()
    print("-" * 60)
    Tarefa_4()
    print("-" * 60)
    Tarefa_5()
