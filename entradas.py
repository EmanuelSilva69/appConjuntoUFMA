import random
import string

def gerar_conjunto_aleatorio(modo="numeros"):
    
    # Isso aqui é o gerador de valor aleatório, usando a biblioteca random do Python. Creio que não há problema em usar uma biblioteca.
  #  Gera um conjunto com 4 a 8 elementos aleatórios.
 #   Usa random.sample para garantir elementos únicos sem esforço extra.
 
    # Define o tamanho conforme o PDF (4 a 8)
    tamanho = random.randint(4, 8)
        
    if modo == "numeros":
            # Padrão: números de 1 a 30
            pool = range(1, 31)
    elif modo == "letras":
            # Apenas letras do alfabeto 
            pool = string.ascii_lowercase
    else:
            # Modo Misto: mistura números, letras e símbolos especiais
            simbolos = "!@#$%&*?"
            pool = list(range(1, 31)) + list(string.ascii_lowercases) + list(simbolos)

        # random.sample garante que os elementos sejam únicos
    selecao = random.sample(list(pool), tamanho)
        
    return set(selecao)
def obter_conjunto_usuario():

   # Solicita ao usuário entre 4 e 8 elementos.
    #Faz o tratamento de strings e validação de regras.
      # sim todos os passos estão comentados para facilitar o entendimento e vão ser em escadinha
    while True:
        print("\n--- Entrada de Dados Inteligente ---")
        entrada = input("Digite entre 4 e 8 elementos (separe por ESPAÇO ou VÍRGULA): ")
        
        # 1. Limpeza da string: substitui vírgulas por espaços
        entrada_limpa = entrada.replace(',', ' ')
        
        # 2. Divisão da string em partes (split)
        partes = entrada_limpa.split()
        
        # 3. Processamento Inteligente (Escadinha de conversão)
        elementos = set()
        for item in partes:
            try:
                # Tenta converter para número inteiro
                valor = int(item)
                elementos.add(valor)
            except ValueError:
                # Se falhar (for letra/símbolo), mantém como string limpa
                elementos.add(item.strip().lower())
        
        # 4. Validação do tamanho conforme o requisito da Unidade 1
        quantidade = len(elementos)
        
        if 4 <= quantidade <= 8:
            print(f"Sucesso! Conjunto aceito com {quantidade} elementos únicos.") #eu não gosto de comentar coisa que eu acho que é autoexplicativa pelo código, mas acho que isso aqui é importante pra mostrar pro usuário que a entrada foi aceita, e também pra mostrar quantos elementos únicos ele colocou, porque se ele colocar 5 elementos, mas um deles for repetido, ele vai mostrar que tem 4 elementos únicos, e isso pode ajudar o usuário a entender que errou 
            
            return elementos
        else:
            print(f"Erro: Você forneceu {quantidade} elementos únicos.")
            print("O conjunto deve ter no mínimo 4 e no máximo 8 elementos.")