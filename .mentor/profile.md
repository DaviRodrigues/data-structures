# Perfil do Estudante & Diário de Bordo (Mentoria DSA)

> **Objetivo:** Acompanhamento contínuo de aprendizado em Estruturas de Dados e Algoritmos com base no livro _Entendendo Algoritmos_ (Aditya Y. Bhargava) e desafios práticos.

---

## 👤 Perfil de Aprendizado

- **Estudante:** Davi (dark860)
- **Linguagem Principal de Estudo:** Python 3
- **Metodologia / Estilo de Aprendizagem:**
  - Aprendizado guiado com foco em **intuição visual e prática**.
  - Validação ativa de código via testes e depuração (_debugging_).
  - Análise crítica de complexidade assintótica (Notação Big $O$ de tempo e espaço).

---

## 📊 Progresso da Trilha

| Módulo       | Capítulo                          |        Status        | Destaques / Conceitos Chave                                       |
| :----------- | :-------------------------------- | :------------------: | :---------------------------------------------------------------- |
| **Módulo 1** | Cap. 1: Pesquisa Binária          |     ✅ Concluído     | $O(\log n)$, busca iterativa e limites                            |
| **Módulo 1** | Cap. 2: Ordenação por Seleção     |     ✅ Concluído     | $O(n^2)$, arrays vs listas encadeadas                             |
| **Módulo 1** | Cap. 3: Recursão                  |     ✅ Concluído     | Caso-base, caso recursivo, _Call Stack_                           |
| **Módulo 2** | Cap. 4: Quicksort & D&C           |     ✅ Concluído     | Dividir para Conquistar, escolha do pivô, ordenação _in-place_    |
| **Módulo 2** | Cap. 5: Tabelas Hash              |     ✅ Concluído     | Função hash, buckets, colisões, fator de carga e _Two Sum_ $O(n)$ |
| **Módulo 3** | Cap. 6: Pesquisa em Largura (BFS) | ⏳ Pronto p/ iniciar | Grafos não ponderados, filas (FIFO), menor rota                   |
| **Módulo 3** | Cap. 6: Pesquisa em Largura (BFS) | 🔄 Em Andamento      | Grafos não ponderados, filas (FIFO), menor rota, $O(V + E)$       |
| **Módulo 3** | Cap. 7: Algoritmo de Dijkstra     | ⏳ Pronto p/ iniciar | Grafos ponderados, tabelas de custo e menor caminho               |

---

## 📝 Diário de Bordo / Registro de Sessões

### 📅 Sessão: Módulo 3 - Capítulo 6 (Grafos e Pesquisa em Largura - BFS)

- **Conceitos & Intuição:**
  - Modelação de Grafos direcionados e não-direcionados utilizando Dicionários / Tabelas Hash (Listas de Adjacência).
  - Uso de Fila FIFO (`collections.deque`) para garantir a exploração em camadas de proximidade (1º grau, 2º grau, etc.) e encontrar o menor caminho em número de arestas.
  - Prevenção de ciclos e loops infinitos usando conjunto (`set`) de visitados com checagem em $O(1)$.
- **Análise Crítica do Estudante:**
  - **Percepção de Complexidade $O(V + E)$:** Notou corretamente que, apesar de existirem dois loops (o `while` que consome a fila e o `for` que itera sobre os vizinhos), a complexidade **não** é multiplicativa $O(n^2)$. Como o conjunto de visitados impede repetições, cada nó é processado uma vez e cada aresta é percorrida uma vez, resultando na soma linear de vértices e arestas $O(V + E)$.
  - **Evolução em Ferramentas:** Utilização ativa do depurador (_debugger_) para inspecionar o estado da fila, caminhos e variáveis a cada iteração do algoritmo.

---

### 📅 Sessão: Módulo 2 - Capítulo 4 (Quicksort & D&C)

- **Conceitos:**
  - Estratégia Dividir para Conquistar (D&C).
  - Impacto da escolha do pivô no Quicksort ($O(n \log n)$ caso médio vs $O(n^2)$ pior caso).
  - Vantagens práticas do Quicksort em relação ao Merge Sort (constantes menores, bom uso de cache de memória).
- **Exercícios:**
  - Respostas teóricas precisas sobre pior caso em arrays ordenados e comparação com Merge Sort.
  - Implementação com sucesso da Busca Binária recursiva usando D&C.

---

### 📅 Sessão: Módulo 2 - Capítulo 5 (Tabelas Hash)

- **Conceitos Abordados:**
  - Mapeamento direto de chaves para índices através de Funções Hash.
  - Uso do operador módulo (`% capacidade`) garantindo que o índice permaneça dentro dos limites do array.
  - Resolução de colisões por encadeamento separado (_Separate Chaining_).
  - Fator de Carga (_Load Factor_ $\approx 0.7$) e necessidade de redimensionamento (_resizing_ / _rehash_).
  - Casos de uso clássicos: lookups $O(1)$, prevenção de duplicados e cache/memoização.
- **Exercícios:**
  - **Exercício 1 (Teórico):** Excelente explicação do fator de carga e redimensionamento para evitar acúmulo de colisões.
  - **Exercício 2 (Teórico):** Domínio das três propriedades essenciais de uma boa função hash (consistência, domínio válido e distribuição uniforme).
  - **Exercício 3 (Prático - Two Sum):**
    - Identificou que a solução de força bruta $O(n^2)$ e a busca de vizinhos não atendiam casos gerais com elementos distantes.
    - Teve a intuição correta de que o problema poderia ser resolvido em um único loop.
    - Implementou com sucesso a técnica clássica de **armazenar `número -> índice`** na tabela hash e consultar o complemento (`alvo - num`) em tempo $O(1)$, atingindo complexidade total $O(n)$.

---

## 💡 Pontos Fortes & Recomendações

### 🌟 Pontos Fortes Observados:

1. **Intuição de Otimização:** Percebeu rapidamente quando um algoritmo poderia ser simplificado para uma única passada ($O(n)$).
2. **Postura Investigativa:** Uso ativo de depuração e testes passo a passo para validar a lógica das estruturas de dados.
3. **Compreensão de Mecânica de Baixo Nível:** Boa clareza sobre alocação de memória, call stack e custo de recursão.
1. **Análise de Complexidade Estruturada:** Compreendeu a diferença entre complexidade aninhada $O(n^2)$ e complexidade agregada em grafos $O(V + E)$, onde estruturas de apoio (`set`) evitam reprocessamento.
2. **Intuição de Otimização:** Percebeu rapidamente quando um algoritmo poderia ser simplificado para uma única passada ($O(n)$).
3. **Postura Investigativa & Depuração:** Uso ativo de depuração passo a passo com _debugger_ para rastrear a mutação de estado e ponteiros.
4. **Compreensão de Mecânica de Baixo Nível:** Boa clareza sobre alocação de memória, call stack e custo de recursão.

### 🎯 Dicas & Recomendações para os Próximos Módulos:

- **Padrão de Mapeamento Invertido:** Sempre que um problema exigir encontrar pares, complementos ou verificar ocorrências passadas em $O(1)$, lembre-se do padrão de mapear `dado -> índice` em vez de `índice -> dado`.
- **Grafos no Módulo 3:** Ao iniciar BFS, preste bastante atenção na escolha da estrutura de dados: Filas (`collections.deque` com `popleft()`) garantem $O(1)$ na remoção do início, enquanto listas normais em Python fariam $O(n)$ no `pop(0)`.
- **Depuração de APIs e Sistemas Assíncronos:** Em servidores web e APIs, lembre-se de que os _breakpoints_ funcionam sob demanda. A aplicação inicia, fica em estado de escuta (_listening_), e a pausa do depurador só é disparada quando a rota específica recebe uma requisição HTTP.
- **Transição de BFS para Dijkstra (Cap. 7):** O BFS encontra o menor caminho contando apenas o **número de arestas** (todos os passos têm peso 1). No Capítulo 7 (Dijkstra), aprenderemos o que fazer quando as arestas têm **pesos/custos diferentes** (ex: tempo em minutos, distância em km).
