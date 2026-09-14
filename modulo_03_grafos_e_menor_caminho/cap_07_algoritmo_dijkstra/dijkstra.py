"""
Módulo 3 - Capítulo 7: Algoritmo de Dijkstra (Menor Caminho em Grafos Ponderados)
Livro: Entendendo Algoritmos (Aditya Y. Bhargava)
"""

# =====================================================================
# 1. GRAFOS PONDERADOS: ESTRUTURAS DE DADOS
# =====================================================================
# Diferente da BFS (onde cada aresta vale 1 passo), no Dijkstra as arestas
# possuem PESOS (custo, tempo, distância, pedágio, etc.).
#
# Representamos o grafo ponderado com dicionários aninhados:
grafo = {
    "inicio": {"a": 6, "b": 2},
    "a": {"fim": 1},
    "b": {"a": 3, "fim": 5},
    "fim": {},
}

# Tabela de Custos: quanto custa para chegar em cada nó a partir do 'inicio'
# Nós que ainda não conhecemos o custo começam com infinito (float("inf"))
custos = {
    "a": 6,
    "b": 2,
    "fim": float("inf"),
}

# Tabela de Pais: guarda o caminho de menor custo (quem leva a quem)
pais = {
    "a": "inicio",
    "b": "inicio",
    "fim": None,
}


# =====================================================================
# 2. FUNÇÃO AUXILIAR: ENCONTRAR NÓ NÃO PROCESSADO DE MENOR CUSTO
# =====================================================================
def achar_no_mais_barato(custos: dict[str, float], processados: set[str]) -> str | None:
    """Encontra o nó com o menor custo que ainda não foi finalizado."""
    menor_custo = float("inf")
    nodo_mais_barato = None

    for nodo, custo in custos.items():
        if custo < menor_custo and nodo not in processados:
            menor_custo = custo
            nodo_mais_barato = nodo

    return nodo_mais_barato


# =====================================================================
# 3. O ALGORITMO DE DIJKSTRA
# =====================================================================
def dijkstra(
    grafo: dict[str, dict[str, float]],
    custos: dict[str, float],
    pais: dict[str, str | None],
) -> tuple[float, list[str]]:
    """
    Executa o Algoritmo de Dijkstra:
    1. Enquanto houver nós para processar:
       - Pega o nó de menor custo não processado.
       - Atualiza o custo de todos os seus vizinhos.
       - Se o custo para o vizinho for menor pelo caminho atual, atualiza 'custos' e 'pais'.
       - Marca o nó como processado.
    2. Reconstrói e retorna o custo total e a lista de nós do menor caminho.
    """
    processados = set()
    nodo = achar_no_mais_barato(custos, processados)

    while nodo is not None:
        custo = custos[nodo]
        vizinhos = grafo.get(nodo, {})

        # Percorre todos os vizinhos do nó atual
        for vizinho, peso in vizinhos.items():
            novo_custo = custo + peso
            # Se for mais barato chegar ao vizinho através deste nó:
            if novo_custo < custos.get(vizinho, float("inf")):
                custos[vizinho] = novo_custo
                pais[vizinho] = nodo

        processados.add(nodo)
        nodo = achar_no_mais_barato(custos, processados)

    # Reconstruindo a rota do início ao fim usando a tabela de pais
    caminho = ["fim"]
    passo = pais.get("fim")
    while passo is not None:
        caminho.append(passo)
        passo = pais.get(passo)
    caminho.reverse()

    return custos["fim"], caminho


if __name__ == "__main__":
    print("=" * 60)
    print("Algoritmo de Dijkstra: Menor Custo em Grafo Ponderado")
    print("=" * 60)
    print(f"Grafo: {grafo}")
    print(f"Custos Iniciais: {custos}")
    print(f"Pais Iniciais: {pais}\n")

    custo_total, rota = dijkstra(grafo, custos, pais)

    print(f"Custo total do caminho mais rápido: {custo_total}")
    print(f"Rota calculada: {' -> '.join(rota)}")
