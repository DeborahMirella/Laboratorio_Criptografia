import collections
import itertools
import math
from Auxiliares import ALFABETO, IC_PORTUGUES, NormalizaTexto, ScorePlausibilidade
from Cifras import CesarDecifrar, VigenereDecifrar

def AtaqueForcaBrutaCesar(ciphertext):
   
    candidatos = []
    for k in range(26):
        # 1. Decifra o texto MANTENDO os espaços
        hipotese_com_espacos = CesarDecifrar(ciphertext, k)
        
        # 2. O score é calculado sobre a hipótese (a função de score já remove os espaços para a análise)
        score = ScorePlausibilidade(hipotese_com_espacos)
        
        # 3. Armazena o texto com espaços para a exibição final
        candidatos.append({'chave': k, 'texto': hipotese_com_espacos, 'score': score})
        
    return sorted(candidatos, key=lambda x: x['score'], reverse=True)

def AtaqueFrequenciaCesar(ciphertext):
    
    texto_limpo = NormalizaTexto(ciphertext)
    if not texto_limpo: return None, "Texto cifrado vazio."
    letra_mais_frequente = collections.Counter(texto_limpo).most_common(1)[0][0]
    chave_estimada = (ALFABETO.find(letra_mais_frequente) - ALFABETO.find('a')) % 26
    return chave_estimada, CesarDecifrar(texto_limpo, chave_estimada)

def _CalculaIC(texto):
    
    n = len(texto)
    if n < 2: return 0.0
    contador = collections.Counter(texto)
    numerador = sum(freq * (freq - 1) for freq in contador.values())
    denominador = n * (n - 1)
    return numerador / denominador

def EstimarTamanhoChaveIC(ciphertext, max_len=10):
    
    texto_limpo = NormalizaTexto(ciphertext)
    resultados_ic = []
    
    print("1. Estimando Tamanho da Chave com Índice de Coincidência")
    
    # Primeiro, calcula o IC para todos os tamanhos de chave testados
    for tamanho in range(2, max_len + 1):
        ics_colunas = [_CalculaIC(texto_limpo[i::tamanho]) for i in range(tamanho)]
        ic_medio = sum(ics_colunas) / len(ics_colunas)
        # O score é a proximidade ao IC do Português (menor é melhor)
        score = abs(ic_medio - IC_PORTUGUES)
        resultados_ic.append({'tamanho': tamanho, 'ic_medio': ic_medio, 'score': score})
        
    # Ordena os resultados para encontrar os melhores (os mais próximos de IC_PORTUGUES)
    resultados_ordenados = sorted(resultados_ic, key=lambda x: x['score'])

    print("\nAs 5 Melhores Hipóteses para o Tamanho da Chave \n")
    print(" Tamanho | IC Médio | Score")
    print("---------|----------|-------------------------------")
    for resultado in resultados_ordenados[:5]:
        print(f"    {resultado['tamanho']:<4} |  {resultado['ic_medio']:.4f}  | {resultado['score']:.4f}")

    # Agora, aplica a lógica inteligente para a escolha final:
    # escolher o primeiro candidato promissor da lista *não ordenada*.
    LIMIAR_IC_ALTO = 0.065
    for resultado in resultados_ic: 
        if resultado['ic_medio'] > LIMIAR_IC_ALTO:
            return resultado['tamanho']

    return resultados_ordenados[0]['tamanho']
'''
def QuebrarVigenereCompleto(ciphertext, num_candidatos_por_coluna=5):
 
    from Cifras import VigenereDecifrar

    tamanho_chave = EstimarTamanhoChaveIC(ciphertext)
    print(f"\nMelhor hipótese para o tamanho da chave: {tamanho_chave}\n")
    
    texto_limpo_analise = NormalizaTexto(ciphertext)
    
    print(f"Gerando os {num_candidatos_por_coluna} Melhores Candidatos por Coluna \n")
    top_candidatos_por_coluna = []
    for i in range(tamanho_chave):
        coluna = texto_limpo_analise[i::tamanho_chave]
        candidatos_coluna = AtaqueForcaBrutaCesar(coluna)
        top_letras = [ALFABETO[c['chave']] for c in candidatos_coluna[:num_candidatos_por_coluna]]
        top_candidatos_por_coluna.append(top_letras)
        print(f"  Coluna {i}: Melhores letras candidatas -> {top_letras}")

    chaves_a_testar = list(itertools.product(*top_candidatos_por_coluna))
    total_combinacoes = len(chaves_a_testar)
    print(f"\nTestando todas as {total_combinacoes} combinações de chaves")
    
    resultados_finais = []
    for chave_tupla in chaves_a_testar:
        chave_str = "".join(chave_tupla)
        texto_decifrado = VigenereDecifrar(texto_limpo_analise, chave_str)
        score = ScorePlausibilidade(texto_decifrado)
        resultados_finais.append({'chave': chave_str, 'texto': texto_decifrado, 'score': score})
        
    melhor_solucao = sorted(resultados_finais, key=lambda x: x['score'], reverse=True)
    
    print("\nApresentando as 5 Melhores Soluções Encontradas")
    print("\n Chave   | Score     | Amostra do Texto Decifrado")
    print("---------|-----------|---------------------------------")
    for resultado in melhor_solucao[:5]:
        chave = resultado['chave'].upper()
        score = resultado['score']
        amostra = resultado['texto'][:25].upper()
        print(f" {chave:<7} | {score:<9.2f} | {amostra}")

    return melhor_solucao[0]
'''
def QuebrarVigenereCompleto(ciphertext, num_candidatos_por_coluna=5):
    """Orquestra o ataque combinatório completo."""
    tamanho_chave = EstimarTamanhoChaveIC(ciphertext)
    print(f"\nEscolha final para o tamanho da chave: {tamanho_chave}\n")
    
    texto_limpo_analise = NormalizaTexto(ciphertext)
    
    print(f"2. Gerando os {num_candidatos_por_coluna} Melhores Candidatos por Coluna")
    top_candidatos_por_coluna = []
    for i in range(tamanho_chave):
        coluna = texto_limpo_analise[i::tamanho_chave]
        candidatos_coluna = AtaqueForcaBrutaCesar(coluna)
        print(f"  Coluna {i}: Melhores letras candidatas (Letra | Score de Plausibilidade)")
        for candidato in candidatos_coluna[:num_candidatos_por_coluna]:
            letra = ALFABETO[candidato['chave']]
            score = candidato['score']
            print(f"    - '{letra}' | {score:.2f}")
        top_letras = [ALFABETO[c['chave']] for c in candidatos_coluna[:num_candidatos_por_coluna]]
        top_candidatos_por_coluna.append(top_letras)

    chaves_a_testar = list(itertools.product(*top_candidatos_por_coluna))
    total_combinacoes = len(chaves_a_testar)
    print(f"\n3. Testando todas as {total_combinacoes} combinações de chaves")
    
    resultados_finais = []
    for chave_tupla in chaves_a_testar:
        chave_str = "".join(chave_tupla)
        texto_decifrado_sem_espacos = VigenereDecifrar(texto_limpo_analise, chave_str)
        score = ScorePlausibilidade(texto_decifrado_sem_espacos)
        resultados_finais.append({'chave': chave_str, 'texto': texto_decifrado_sem_espacos, 'score': score})
        
    melhor_solucao = sorted(resultados_finais, key=lambda x: x['score'], reverse=True)
    
    print("\n4. Apresentando as 5 Melhores Soluções Encontradas")
    print("\n Chave   | Score     | Amostra do Texto Decifrado")
    print("---------|-----------|---------------------------------")
    for resultado in melhor_solucao[:5]:
        chave = resultado['chave'].upper()
        score = resultado['score']
        amostra = resultado['texto'][:25].upper()
        print(f" {chave:<7} | {score:<9.2f} | {amostra}")

    return melhor_solucao[0]
