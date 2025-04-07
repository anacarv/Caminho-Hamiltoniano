# Caminho-Hamiltoniano

## Sobre o Projeto

Um Caminho Hamiltoniano em um grafo é um caminho que visita cada vértice
exatamente uma vez. Encontrar esse caminho é um problema clássico em teoria
dos grafos e está associado a problemas de alta complexidade computacional,
como o Problema do Caixeiro Viajante. Este projeto tem como objetivo
implementar uma abordagem para determinar se um Caminho Hamiltoniano
existe em um grafo e, em caso afirmativo, encontrá-lo.

## Como Executar o Projeto

### Pré-requisitos

Este projeto requer **Python 3.x** instalado, e **não exige a instalação de nenhuma dependência adicional**.

### Rodando o código

1. Clone este repositório:
   ```sh
   git clone https://github.com/anacarv/Caminho-Hamiltoniano
   cd Caminho-Hamiltoniano
   ```
2. Execute o script:
   ```sh
   python main.py
   ```
3. Insira o número de vértices e a matriz de adjacência conforme solicitado.

## Relatório Técnico

### 1. Complexidade Computacional (P, NP, NP-Completo, NP-Difícil)

O problema do **Caminho Hamiltoniano** pertence à classe **NP-Completo**:

- **NP (Nondeterministic Polynomial Time)**: É possível verificar em tempo polinomial se uma solução é válida.
- **NP-Completo**: São problemas para os quais uma solução pode ser verificada em tempo polinomial e todos os problemas em NP podem ser reduzidos a ele em tempo polinomial.
- O **Caminho Hamiltoniano** é equivalente ao Problema do Caixeiro Viajante (TSP), cuja versão de decisão também é NP-Completa.
- Portanto, encontrar um caminho Hamiltoniano está entre os problemas mais difíceis da classe NP.

### 2. Complexidade Assintótica de Tempo

- A implementação mais comum para encontrar um caminho Hamiltoniano é **backtracking**.
- Nesse caso, o algoritmo tenta construir todos os caminhos possíveis e verifica se há um que passe por todos os vértices.
- Como existem `(n-1)!` possíveis caminhos em um grafo de `n` vértices (sem ciclos), a complexidade de tempo é **O(n!)**.

#### Método Utilizado

- A complexidade foi determinada usando **contagem de operações** e análise combinatória sobre o número de permutações possíveis.
- Para cada permutação, verificamos se as arestas existem entre os vértices, o que leva a `n` verificações por permutação.

### 3. Aplicação do Teorema Mestre

- O **Teorema Mestre** não se aplica ao algoritmo de backtracking para o Caminho Hamiltoniano.
- Isso porque o Teorema Mestre só se aplica a algoritmos recursivos com divisões regulares e número fixo de subproblemas, o que não é o caso aqui.
- O número de chamadas não é uniforme (depende do grafo) e o crescimento é fatorial, não recursivo simples.

### 4. Casos de Complexidade

- **Melhor Caso**: O primeiro caminho testado já é Hamiltoniano. Complexidade próxima de **O(n²)**.
- **Caso Médio**: Depende da ordem dos caminhos e da estrutura do grafo. Ainda exponencial.
- **Pior Caso**: O algoritmo testa todas as `(n-1)!` possibilidades sem sucesso. Complexidade **O(n!)**.

Essas variações demonstram o comportamento não determinístico do algoritmo, justificando sua inclusão na classe **NP-Completo**.
