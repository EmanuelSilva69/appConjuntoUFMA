#arquivo .py que é a base para manipulação de matemática do projeto
def uniao(a,b): #função que retorna a união de dois conjuntos
    resultado = list(a)
    for elemento in b:
        if elemento not in resultado:
            resultado.append(elemento)
    return set(resultado)
def intersecao(a,b): #função que retorna a interseção de dois conjuntos
    resultado = []
    for elemento in a:
        if elemento in b:
            resultado.append(elemento)
    return set(resultado)
def diferenca(a,b): #função que retorna a diferença entre dois conjuntos (mesma coisa do código anterior, eu só botei o not. que é pra não adicionar os elementos de B em A)
    resultado = []
    for elemento in a:
        if elemento not in b: #olha ele ali
            resultado.append(elemento)
    return set(resultado)
def complemento(universo, conjunto): #função que retorna o complemento de um conjunto em relação ao universo
    resultado = []
    for elemento in universo:
        if elemento not in conjunto:
            resultado.append(elemento)
    return set(resultado)
def diferenca_simetrica(a,b): #função que retorna a diferença simétrica entre dois conjuntos (a diferença simétrica é a união das diferenças entre os conjuntos)
    diferenca_ab = diferenca(a,b) #reutilizando a função diferença
    diferenca_ba = diferenca(b,a)
    return uniao(diferenca_ab, diferenca_ba) #reutilizando a função união

def cardinalidade(conjunto): #função que retorna a cardinalidade de um conjunto (quantidade de elementos)
    contador = 0
    for _ in conjunto:
        contador += 1
    return contador

#isso aqui é extra pq n sei se é obrigatório
def eh_subconjunto(a, b):
    #Verifica se A está contido em B (A ⊆ B)
    for elemento in a:
        if elemento not in b:
            return False
    return True

def sao_disjuntos(a, b):
    #Verifica se a interseção é vazia
    for elemento in a:
        if elemento in b:
            return False
    return True
def sao_iguais(a, b):
    # Dois conjuntos são iguais se A está contido em B e B está contido em A
    return eh_subconjunto(a, b) and eh_subconjunto(b, a)