import collections
from Auxiliares import NormalizaTexto, ALFABETO
from Cifras import CesarCifrar, CesarDecifrar, VigenereCifrar, VigenereDecifrar
from Ataques import AtaqueForcaBrutaCesar, AtaqueFrequenciaCesar, QuebrarVigenereCompleto

def ExecutarTarefa1():
    print("TAREFA 1: IMPLEMENTAÇÃO DA CIFRA DE CÉSAR \n")
    texto = "SEGURANCA DA INFORMACAO E IMPORTANTE"
    chave = 3
    cifrado = CesarCifrar(texto, chave)
    decifrado = CesarDecifrar(cifrado, chave)
    print(f"Texto Original: {texto.upper()}")
    print(f"Texto Cifrado (k = 3): {cifrado.upper()}")
    print(f"Texto Decifrado: {decifrado.upper()}")

def ExecutarTarefa2():

    print("TAREFA 2: ATAQUE DE FORÇA BRUTA EM CÉSAR \n")

    ciphertext = "SXBN N DV XCRVX NBCDMJWCN MJ DOVP"
    print(f"Texto Cifrado: {ciphertext.upper()}")
    
    candidatos = AtaqueForcaBrutaCesar(ciphertext)
    
    print("\nOs cinco Melhores Candidatos Encontrados \n")
    for i, candidato in enumerate(candidatos[:5]):
        print(f"  {i+1}: Chave k={candidato['chave']}, Score = {candidato['score']:.2f} -> '{candidato['texto'].upper()}'")
    
    melhor = candidatos[0]
    print("\nConclusão \n")
    print(f"A melhor chave é k = {melhor['chave']}.")
    print(f"Texto Decifrado Final: {melhor['texto'].upper()}")

def ExecutarTarefa3():

    print("TAREFA 3: ATAQUE POR ANÁLISE DE FREQUÊNCIA EM CÉSAR \n")
    ciphertext = "RKRHLV UV UZTZFERIZF V VWZTRQ TFEKIR JVEYRJ WIRTRJ"
    print(f"Texto Cifrado: {ciphertext.upper()}\n")
    
    texto_limpo = NormalizaTexto(ciphertext)
    
    print("1. Tabela de Frequências do Texto Cifrado \n")
    contador = collections.Counter(texto_limpo)
    letra_mais_frequente = contador.most_common(1)[0][0]
    for letra, contagem in sorted(contador.items()):
        print(f"  Letra '{letra.upper()}': {contagem} ocorrências")
    print(f"\nA letra mais frequente é '{letra_mais_frequente.upper()}'.\n")
    
    print("2. Teste de Hipóteses para a Chave k \n")
    
    chave_hipotese_e = (ALFABETO.find(letra_mais_frequente) - ALFABETO.find('e')) % 26
    plaintext_hipotese_e = CesarDecifrar(ciphertext, chave_hipotese_e)
    print(f"Hipótese 1 (R -> E): Chave k={chave_hipotese_e}")
    print(f"Texto Decifrado: {plaintext_hipotese_e.upper()}")

    chave_hipotese_a = (ALFABETO.find(letra_mais_frequente) - ALFABETO.find('a')) % 26
    plaintext_hipotese_a = CesarDecifrar(ciphertext, chave_hipotese_a)
    print(f"\nHipótese 2 (R -> A): Chave k={chave_hipotese_a}")
    print(f"Texto Decifrado: {plaintext_hipotese_a.upper()} \n")
    
    print("Ao validar as hipóteses através da leitura do texto decifrado, a Hipótese 2 produz um resultado perfeitamente legível: \n")
    print(f"{plaintext_hipotese_a.upper()} \n")

    print(f"Conclui-se que a chave correta, encontrada pelo método de análise de frequência, é k={chave_hipotese_a}.")


def ExecutarTarefa4():
    print("TAREFA 4: IMPLEMENTAÇÃO DA CIFRA DE VIGENÈRE \n")
    texto = "CIFRA DE VIGENERE E UM POUCO MAIS FORTE"
    chave = "SEGURO"
    cifrado = VigenereCifrar(texto, chave)
    decifrado = VigenereDecifrar(cifrado, chave)
    print(f"Texto Original: {texto.upper()}")
    print(f"Texto Cifrado (chave = 'SEGURO'): {cifrado.upper()}")
    print(f"Texto Decifrado: {decifrado.upper()}")

def ExecutarTarefa5():
    print("TAREFA 5: QUEBRA DA CIFRA DE VIGENÈRE \n")
    ciphertext = "ECXPFI WO QQYFO LX JWOXBSZX"
    print(f"Texto Cifrado: {ciphertext}\n")
    
    melhor_solucao = QuebrarVigenereCompleto(ciphertext)
    
    print("\n" + "-"*40)
    print("SOLUÇÃO FINAL DA TAREFA 5 ENCONTRADA \n")
    chave_final = melhor_solucao['chave']
    print(f"A melhor chave encontrada foi: {chave_final.upper()}")
    
    texto_decifrado_final = VigenereDecifrar(ciphertext, chave_final)
    print(f"Texto Decifrado: {texto_decifrado_final.upper()}")

if __name__ == "__main__":
    print("="*60)
    print("INICIANDO A EXECUÇÃO")
    print("="*60 + "\n")
    
    ExecutarTarefa1()
    print("\n" + "-"*60 + "\n")
    ExecutarTarefa2()
    print("\n" + "-"*60 + "\n")
    ExecutarTarefa3()
    print("\n" + "-"*60 + "\n")
    ExecutarTarefa4()
    print("\n" + "-"*60 + "\n")
    ExecutarTarefa5()
    print("\n" + "="*60)
    print("LABORATÓRIO CONCLUÍDO")
    print("="*60)
