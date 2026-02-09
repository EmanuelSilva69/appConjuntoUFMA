#   Analisador de Conjuntos.
Este projeto é uma ferramenta interativa para manipulação e análise de conjuntos matemáticos, desenvolvida como parte de estudos em Lógica e Matemática Discreta. O software permite realizar operações fundamentais e verificar relações lógicas entre conjuntos inseridos pelo usuário e conjuntos gerados aleatoriamente.

##  Visão Geral
A aplicação foca na manipulação manual de coleções, implementando a lógica algorítmica por trás de cada operação de conjunto.

<h3> Funcionalidades Principais</h3>

* **União e Interseção**: Agrupamento e filtragem de elementos comuns.
* **Diferenças**: Cálculo de diferença relativa e simétrica entre conjuntos.
* **Relações**: Verificação de igualdade e pertinência (subconjuntos).
* **Cardinalidade**: Contagem de elementos .
##  Fundamentos Teóricos
Este projeto implementa as operações clássicas da Teoria dos Conjuntos:

* **União (A ∪ B)**: Conjunto de todos os elementos que pertencem a A ou a B (ou ambos).
* **Interseção (A ∩ B)**: Conjunto de elementos que pertencem simultaneamente a A e B.
* **Diferença (A - B)**: Elementos que estão em A mas não estão em B.
* **Diferença Simétrica (A Δ B)**: (A - B) ∪ (B - A), elementos exclusivos de cada conjunto.
* **Complemento (Aᶜ)**: Elementos do universo U que não pertencem a A.
* **Cardinalidade (|A|)**: Número de elementos em um conjunto.

### Propriedades Verificadas
* **Subconjunto (A ⊆ B)**: Verifica se todos elementos de A estão em B.
* **Conjuntos Disjuntos**: A ∩ B = ∅ (não compartilham elementos).
  
##  Interface e Experiência do Usuário
O projeto utiliza a biblioteca CustomTkinter para oferecer uma interface moderna com suporte a temas e elementos visuais dinâmicos.
<h3> Funcionalidades da Interface</h3>

* **Validação em Tempo Real**: O sistema verifica se o conjunto inserido possui entre **4 e 8 elementos**, disparando um feedback visual temporário em caso de erro.
* **Geração Aleatória Dinâmica**: O usuário pode alternar entre modos (**números, letras ou misto**) para gerar o **Conjunto B** automaticamente, utilizando um seletor segmentado.
* **Visualização Formatada**: Os resultados são exibidos em blocos estilizados por cores através de uma classe de texto customizada:
    * **Azul/Roxo**: Listagem detalhada dos conjuntos (A, B e Universo).
    * **Icy Blue**: Resultados das operações matemáticas.
    * **Neon Ice**: Cálculos de cardinalidade.
    * **Roxo Escuro**: Análise de subconjuntos e disjunção.
* **Fallback para Conjunto Vazio**: Se a interseção for vazia, o app exibe o símbolo matemático $\emptyset$ para clareza acadêmica.

<h3> Identidade Visual (UI/UX)</h3>

O projeto adota uma estética **Modern Slate**, focada em legibilidade e conforto visual através de um modo escuro profundo.

### Paleta de Cores (Slate Style)
| Elemento | Cor | Hexadecimal |
| :--- | :--- | :--- |
| **Fundo** | Slate 900 | `#0F172A` |
| **Cards** | Slate 800 | `#1E293B` |
| **Destaque** | Sky Blue | `#38BDF8` |
| **Botão** | Indigo | `#6366F1` |
| **Sucesso** | Emerald | `#10B981` |
| **Erro** | Red/Rose | `#EF4444` |

<h3> Tecnologias Utilizadas</h3>

* **Python 3.x**: Linguagem base.
* **CustomTkinter**: Interface gráfica moderna com suporte a temas.

* **Estrutura de Módulos**:
    * `basemtm.py`: Implementação das funções matemáticas.
    * `design.py`: Gerenciamento de cores, fontes e temas globais.
    * `entradas.py`: Lógica de randomização e limpeza de inputs.
    * `main.py`: Orquestrador da interface e fluxo do app.
    * 
##  Arquitetura do Código

### [`basemtm.py`](basemtm.py) - Motor Matemático
Implementa manualmente cada operação usando algoritmos com loops e condicionais:

* `uniao(a, b)` → Adiciona elementos de B a A se não houver repetição
* `intersecao(a, b)` → Percorre A buscando elementos comuns em B
* `diferenca(a, b)` → Filtra elementos de A que não existem em B
* `complemento(universo, conjunto)` → Retorna elementos de U que não estão no conjunto
* `diferenca_simetrica(a, b)` → Reutiliza `diferenca()` e `uniao()`
* `cardinalidade(conjunto)` → Conta elementos manualmente com loop
* `eh_subconjunto(a, b)` → Verifica contenção (A ⊆ B)
* `sao_disjuntos(a, b)` → Verifica se a interseção é vazia

**Nota**: Todas as funções evitam propositalmente usar operadores nativos como `|`, `&`, `-` para demonstrar compreensão algorítmica.

### [`entradas.py`](entradas.py) - Gerenciamento de Inputs
* `gerar_conjunto_aleatorio(modo)` → Gera conjunto com 4-8 elementos usando `random.sample()`
* `obter_conjunto_usuario()` → Versão de terminal com validação em loop

### [`design.py`](design.py) - Sistema de Temas
* `CORES` → Dicionário com paleta "Slate Style"
* `FONTES` → Configurações tipográficas (Roboto, Montserrat)
* `CaixaTextoEstilizada` → Widget customizado com suporte a tags coloridas

### [`main_app.py`](main_app.py) - Interface Principal
Orquestra toda aplicação usando CustomTkinter:
* Validação de entrada (4-8 elementos)
* Geração dinâmica de B com seletor de modos
* Cálculo de todas operações
* Renderização formatada dos resultados

<h1> Como Instalar e Executar</h1>

Siga estes passos para configurar o projeto na sua máquina:
1. **Clone o repositório** (ou baixe os arquivos):
  ```bash
git clone https://github.com/EmanuelSilva69/appConjuntoUFMA.git
```
2. **Entrar na pasta do projeto**:
```bash
cd appConjuntoUFMA
```
3. **Instale as bibliotecas necessárias:**:
```PowerShell
py -m pip install customtkinter 
```
 3. **Inicie a aplicação**:   
```PowerShell
py main.py
```
