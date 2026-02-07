# 🧮  Analisador de Conjuntos.
Este projeto é uma ferramenta interativa para manipulação e análise de conjuntos matemáticos, desenvolvida como parte de estudos em Matemática Discreta e Algoritmos. O software permite realizar operações fundamentais e verificar relações lógicas entre conjuntos inseridos pelo usuário e conjuntos gerados aleatoriamente.

## 📋 Visão Geral
A aplicação foca na manipulação manual de coleções, implementando a lógica algorítmica por trás de cada operação de conjunto.

<h3>🚀 Funcionalidades Principais</h3>

* **União e Interseção**: Agrupamento e filtragem de elementos comuns.
* **Diferenças**: Cálculo de diferença relativa e simétrica entre conjuntos.
* **Relações**: Verificação de igualdade e pertinência (subconjuntos).
* **Cardinalidade**: Contagem de elementos únicos.

## 🎨 Interface e Experiência do Usuário
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
* **PIL (Pillow)**: Gerenciamento de elementos visuais.
* **Estrutura de Módulos**:
    * `basemtm.py`: Implementação das funções matemáticas.
    * `design.py`: Gerenciamento de cores, fontes e temas globais.
    * `entradas.py`: Lógica de randomização e limpeza de inputs.
    * `main.py`: Orquestrador da interface e fluxo do app.
    

<h1>⚙️ Como Instalar e Executar</h1>

Siga estes passos para configurar o projeto na sua máquina:
1. **Clone o repositório** (ou baixe os arquivos):
   ```bash
   git clone https://github.com/EmanuelSilva69/appConjuntoUFMA.git

2. **Entrar na pasta do projeto**:
```bash
cd appConjuntoUFMA
```
3. **Instale as bibliotecas necessárias:**:
```PowerShell
py -m pip install customtkinter Pillow
```
 3. **Inicie a aplicação**:   
```PowerShell
py main.py
```
